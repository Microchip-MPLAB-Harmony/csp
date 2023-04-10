/*******************************************************************************
Interface definition of ${SEFC_INSTANCE_NAME} PLIB.

Company:
Microchip Technology Inc.

File Name:
plib_${SEFC_INSTANCE_NAME?lower_case}.h

Summary:
Interface definition of ${SEFC_INSTANCE_NAME} Plib.

Description:
This file defines the interface for the ${SEFC_INSTANCE_NAME} Plib.
It allows user to Program, Erase and lock the on-chip FLASH memory.
*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
* Copyright (C) 2022 Microchip Technology Inc. and its subsidiaries.
*
* Subject to your compliance with these terms, you may use Microchip software
* and any derivatives exclusively with Microchip products. It is your
* responsibility to comply with third party license terms applicable to your
* use of third party software (including open source software) that may
* accompany Microchip software.
*
* THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS". NO WARRANTIES, WHETHER
* EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS SOFTWARE, INCLUDING ANY IMPLIED
* WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A
* PARTICULAR PURPOSE.
*
* IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL, PUNITIVE,
* INCIDENTAL OR CONSEQUENTIAL LOSS, DAMAGE, COST OR EXPENSE OF ANY KIND
* WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF MICROCHIP HAS
* BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO THE
* FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL CLAIMS IN
* ANY WAY RELATED TO THIS SOFTWARE WILL NOT EXCEED THE AMOUNT OF FEES, IF ANY,
* THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS SOFTWARE.
*******************************************************************************/
// DOM-IGNORE-END

#include <string.h>
#include "device.h"
#include "plib_${SEFC_INSTANCE_NAME?lower_case}.h"
<#if core.CoreSysIntFile == true>
#include "interrupts.h"
</#if>

static uint32_t sefc_status = 0;

<#if INTERRUPT_ENABLE == true>
    <#lt>volatile static SEFC_OBJECT sefc;
</#if>

// *****************************************************************************
// *****************************************************************************
// ${SEFC_INSTANCE_NAME} Local Functions
// *****************************************************************************
// *****************************************************************************
// *****************************************************************************

__longramfunc__ static bool ${SEFC_INSTANCE_NAME}_sequenceRead(uint32_t cmdStart, uint32_t cmdStop,
                                               uint32_t *data, uint32_t length, uint32_t address)
{
    uint32_t count = 0;
    uint32_t sefcFmrReg;
    uint32_t *pAddress = (uint32_t *)address;

    /* Disable Sequential Code Optimization */
    sefcFmrReg = ${SEFC_INSTANCE_NAME}_REGS->SEFC_EEFC_FMR;
    ${SEFC_INSTANCE_NAME}_REGS->SEFC_EEFC_FMR |= SEFC_EEFC_FMR_SCOD_Msk;

    ${SEFC_INSTANCE_NAME}_REGS->SEFC_EEFC_FCR = (cmdStart | SEFC_EEFC_FCR_FKEY_PASSWD);

    while ((${SEFC_INSTANCE_NAME}_REGS->SEFC_EEFC_FSR & SEFC_EEFC_FSR_FRDY_Msk) == SEFC_EEFC_FSR_FRDY_Msk)
    {
        // Wait for the flash ready falls
    }

    for (count = 0; count < length; count++)
    {
        data[count] = pAddress[count];
    }

    ${SEFC_INSTANCE_NAME}_REGS->SEFC_EEFC_FCR = (cmdStop | SEFC_EEFC_FCR_FKEY_PASSWD);

    while ((${SEFC_INSTANCE_NAME}_REGS->SEFC_EEFC_FSR & SEFC_EEFC_FSR_FRDY_Msk) == 0U)
    {
        // Wait for the flash ready
    }

    /* Enable Sequential Code Optimization */
    if ((sefcFmrReg & SEFC_EEFC_FMR_SCOD_Msk) == 0U)
    {
        ${SEFC_INSTANCE_NAME}_REGS->SEFC_EEFC_FMR &= ~SEFC_EEFC_FMR_SCOD_Msk;
    }

    return true;
}

// *****************************************************************************
// *****************************************************************************
// ${SEFC_INSTANCE_NAME} PLib Interface Routines
// *****************************************************************************
// *****************************************************************************
// *****************************************************************************

void ${SEFC_INSTANCE_NAME}_Initialize(void)
{
    ${SEFC_INSTANCE_NAME}_REGS->SEFC_EEFC_FMR = SEFC_EEFC_FMR_FWS(${NVM_RWS}U) | SEFC_EEFC_FMR_CLOE_Msk | SEFC_EEFC_FMR_ALWAYS1_Msk;
}

bool ${SEFC_INSTANCE_NAME}_Read( uint32_t *data, uint32_t length, uint32_t address )
{
    uint32_t *pAddress = (uint32_t*)address;
    (void)memcpy(data, pAddress, length);
    return true;
}

bool ${SEFC_INSTANCE_NAME}_SectorErase( uint32_t address )
{
    uint16_t page_number;

    /* Calculate the Page number to be passed for FARG register */
    page_number = (uint16_t)((address - ${MEM_SEGMENT_NAME}_ADDR) / ${MEM_SEGMENT_NAME}_PAGE_SIZE);

    /* Issue the FLASH erase operation */
    ${SEFC_INSTANCE_NAME}_REGS->SEFC_EEFC_FCR = (SEFC_EEFC_FCR_FCMD_EPA | SEFC_EEFC_FCR_FARG((uint32_t)page_number | 0x2U) | SEFC_EEFC_FCR_FKEY_PASSWD);

    sefc_status = 0;

    <#if INTERRUPT_ENABLE == true>
        <#lt>    ${SEFC_INSTANCE_NAME}_REGS->SEFC_EEFC_FMR |= SEFC_EEFC_FMR_FRDY_Msk;
    </#if>

    return true;
}

bool ${SEFC_INSTANCE_NAME}_PageBufferWrite( uint32_t *data, const uint32_t address)
{
    uint16_t page_number;

    /* Calculate the Page number to be passed for FARG register */
    page_number = (uint16_t)((address - ${MEM_SEGMENT_NAME}_ADDR) / ${MEM_SEGMENT_NAME}_PAGE_SIZE);

    for (uint32_t i = 0; i < ${MEM_SEGMENT_NAME}_PAGE_SIZE; i += 4U)
    {
        *((uint32_t *)( ${MEM_SEGMENT_NAME}_ADDR + ( page_number * ${MEM_SEGMENT_NAME}_PAGE_SIZE ) + i )) = *data ;
        data++;
    }

    __DSB();
    __ISB();

    return true;
}

bool ${SEFC_INSTANCE_NAME}_PageBufferCommit( const uint32_t address)
{
    uint16_t page_number;

    /* Calculate the Page number to be passed for FARG register */
    page_number = (uint16_t)((address - ${MEM_SEGMENT_NAME}_ADDR) / ${MEM_SEGMENT_NAME}_PAGE_SIZE);

    __DSB();
    __ISB();

    /* Issue the FLASH write operation*/
    ${SEFC_INSTANCE_NAME}_REGS->SEFC_EEFC_FCR = (SEFC_EEFC_FCR_FCMD_WP | SEFC_EEFC_FCR_FARG((uint32_t)page_number) | SEFC_EEFC_FCR_FKEY_PASSWD);

    sefc_status = 0;

    <#if INTERRUPT_ENABLE == true>
        <#lt>    ${SEFC_INSTANCE_NAME}_REGS->SEFC_EEFC_FMR |= SEFC_EEFC_FMR_FRDY_Msk;
    </#if>

    return true;
}

bool ${SEFC_INSTANCE_NAME}_PageWrite( uint32_t *data, uint32_t address )
{
    uint16_t page_number;

    /* Calculate the Page number to be passed for FARG register */
    page_number = (uint16_t)((address - ${MEM_SEGMENT_NAME}_ADDR) / ${MEM_SEGMENT_NAME}_PAGE_SIZE);

    for (uint32_t i = 0; i < ${MEM_SEGMENT_NAME}_PAGE_SIZE; i += 4U)
    {
        *((uint32_t *)( ${MEM_SEGMENT_NAME}_ADDR + ( page_number * ${MEM_SEGMENT_NAME}_PAGE_SIZE ) + i )) = *data;
        data++;
    }

    __DSB();
    __ISB();

    /* Issue the FLASH write operation*/
    ${SEFC_INSTANCE_NAME}_REGS->SEFC_EEFC_FCR = (SEFC_EEFC_FCR_FCMD_WP | SEFC_EEFC_FCR_FARG((uint32_t)page_number) | SEFC_EEFC_FCR_FKEY_PASSWD);

    sefc_status = 0;

    <#if INTERRUPT_ENABLE == true>
        <#lt>    ${SEFC_INSTANCE_NAME}_REGS->SEFC_EEFC_FMR |= SEFC_EEFC_FMR_FRDY_Msk;
    </#if>

    return true;
}

bool ${SEFC_INSTANCE_NAME}_QuadWordWrite( uint32_t *data, uint32_t address )
{
    uint16_t page_number;

    /* Calculate the Page number to be passed for FARG register */
    page_number = (uint16_t)((address - ${MEM_SEGMENT_NAME}_ADDR) / ${MEM_SEGMENT_NAME}_PAGE_SIZE);

    for (uint32_t i = 0; i < 16U; i += 4U)
    {
        *((uint32_t *)(( address ) + i )) = *data;
        data++;
    }
    /* Issue the FLASH write operation */
    ${SEFC_INSTANCE_NAME}_REGS->SEFC_EEFC_FCR = (SEFC_EEFC_FCR_FCMD_WP | SEFC_EEFC_FCR_FARG((uint32_t)page_number) | SEFC_EEFC_FCR_FKEY_PASSWD);

    sefc_status = 0;

    <#if INTERRUPT_ENABLE == true>
        <#lt>    ${SEFC_INSTANCE_NAME}_REGS->SEFC_EEFC_FMR |= SEFC_EEFC_FMR_FRDY_Msk;
    </#if>

    return true;
}

void ${SEFC_INSTANCE_NAME}_RegionLock(uint32_t address)
{
    uint16_t page_number;

    /*Calculate the Page number to be passed for FARG register*/
    page_number = (uint16_t)((address - ${MEM_SEGMENT_NAME}_ADDR) / ${MEM_SEGMENT_NAME}_PAGE_SIZE);
    ${SEFC_INSTANCE_NAME}_REGS->SEFC_EEFC_FCR = (SEFC_EEFC_FCR_FCMD_SLB | SEFC_EEFC_FCR_FARG((uint32_t)page_number) | SEFC_EEFC_FCR_FKEY_PASSWD);

    sefc_status = 0;

    <#if INTERRUPT_ENABLE == true>
        <#lt>    ${SEFC_INSTANCE_NAME}_REGS->SEFC_EEFC_FMR |= SEFC_EEFC_FMR_FRDY_Msk;
    </#if>
}

void ${SEFC_INSTANCE_NAME}_RegionUnlock(uint32_t address)
{
    uint16_t page_number;

    /*Calculate the Page number to be passed for FARG register*/
    page_number = (uint16_t)((address - ${MEM_SEGMENT_NAME}_ADDR) / ${MEM_SEGMENT_NAME}_PAGE_SIZE);
    ${SEFC_INSTANCE_NAME}_REGS->SEFC_EEFC_FCR = (SEFC_EEFC_FCR_FCMD_CLB | SEFC_EEFC_FCR_FARG((uint32_t)page_number) | SEFC_EEFC_FCR_FKEY_PASSWD);

    sefc_status = 0;

    <#if INTERRUPT_ENABLE == true>
        <#lt>    ${SEFC_INSTANCE_NAME}_REGS->SEFC_EEFC_FMR |= SEFC_EEFC_FMR_FRDY_Msk;
    </#if>
}

__longramfunc__ void ${SEFC_INSTANCE_NAME}_GpnvmBitSet(uint8_t GpnvmBitNumber)
{
    ${SEFC_INSTANCE_NAME}_REGS->SEFC_EEFC_FCR = (SEFC_EEFC_FCR_FCMD_SGPB | SEFC_EEFC_FCR_FARG((uint32_t)GpnvmBitNumber) | SEFC_EEFC_FCR_FKEY_PASSWD);

    while ((${SEFC_INSTANCE_NAME}_REGS->SEFC_EEFC_FSR & SEFC_EEFC_FSR_FRDY_Msk) == 0U)
    {
        // Wait for the flash ready
    }
}

__longramfunc__ void ${SEFC_INSTANCE_NAME}_GpnvmBitClear(uint8_t GpnvmBitNumber)
{
    ${SEFC_INSTANCE_NAME}_REGS->SEFC_EEFC_FCR = (SEFC_EEFC_FCR_FCMD_CGPB | SEFC_EEFC_FCR_FARG((uint32_t)GpnvmBitNumber) | SEFC_EEFC_FCR_FKEY_PASSWD);

    while ((${SEFC_INSTANCE_NAME}_REGS->SEFC_EEFC_FSR & SEFC_EEFC_FSR_FRDY_Msk) == 0U)
    {
        // Wait for the flash ready
    }
}

__longramfunc__ uint32_t ${SEFC_INSTANCE_NAME}_GpnvmBitRead(void)
{
    ${SEFC_INSTANCE_NAME}_REGS->SEFC_EEFC_FCR = (SEFC_EEFC_FCR_FCMD_GGPB | SEFC_EEFC_FCR_FKEY_PASSWD);

    while ((${SEFC_INSTANCE_NAME}_REGS->SEFC_EEFC_FSR & SEFC_EEFC_FSR_FRDY_Msk) == 0U)
    {
        // Wait for the flash ready
    }

    return (uint32_t)${SEFC_INSTANCE_NAME}_REGS->SEFC_EEFC_FRR;
}

bool ${SEFC_INSTANCE_NAME}_UniqueIdentifierRead(uint32_t *data, uint32_t length)
{
    /* Check Unique Identifier length (128 bits) */
    if (length > 4U)
    {
        return false;
    }

    return ${SEFC_INSTANCE_NAME}_sequenceRead(SEFC_EEFC_FCR_FCMD_STUI, SEFC_EEFC_FCR_FCMD_SPUI, data, length, ${MEM_SEGMENT_NAME}_ADDR);
}

void ${SEFC_INSTANCE_NAME}_UserSignatureRightsSet(uint32_t userSignatureRights)
{
    ${SEFC_INSTANCE_NAME}_REGS->SEFC_EEFC_USR = userSignatureRights;
}

uint32_t ${SEFC_INSTANCE_NAME}_UserSignatureRightsGet(void)
{
    return ${SEFC_INSTANCE_NAME}_REGS->SEFC_EEFC_USR;
}

bool ${SEFC_INSTANCE_NAME}_UserSignatureRead(uint32_t *data, uint32_t length, SEFC_USERSIGNATURE_BLOCK block, SEFC_USERSIGNATURE_PAGE page)
{
    uint32_t address;

    address = ${MEM_SEGMENT_NAME}_ADDR + ((((uint32_t)block * 8U) + (uint32_t)page) * ${SEFC_INSTANCE_NAME}_PAGESIZE);

    return ${SEFC_INSTANCE_NAME}_sequenceRead(SEFC_EEFC_FCR_FCMD_STUS, SEFC_EEFC_FCR_FCMD_SPUS, data, length, address);
}

bool ${SEFC_INSTANCE_NAME}_UserSignatureWrite(void *data, uint32_t length, SEFC_USERSIGNATURE_BLOCK block, SEFC_USERSIGNATURE_PAGE page)
{
    uint32_t count = 0U;
    uint64_t *dest = NULL;
    uint64_t *src = (uint64_t *)data;
    uint32_t page_number = 0U;

    if (length > (${MEM_SEGMENT_NAME}_PAGE_SIZE >> 2))
    {
        return false;
    }

    page_number = (((uint32_t)block * 8U) + (uint32_t)page);

    dest = (uint64_t *)(${MEM_SEGMENT_NAME}_ADDR + (page_number * ${MEM_SEGMENT_NAME}_PAGE_SIZE));

    /* Writing 8-bit and 16-bit data is not allowed and may lead to unpredictable data corruption */
    for (count = 0; count < (length >> 1); count++)
    {
        *dest = *src;
        dest++;
        src++;
    }

    __DSB();
    __ISB();

    /* Issue the FLASH write operation*/
    ${SEFC_INSTANCE_NAME}_REGS->SEFC_EEFC_FCR = (SEFC_EEFC_FCR_FCMD_WUS | SEFC_EEFC_FCR_FARG(page_number) | SEFC_EEFC_FCR_FKEY_PASSWD);

    sefc_status = 0;

    <#if INTERRUPT_ENABLE == true>
        <#lt>    ${SEFC_INSTANCE_NAME}_REGS->SEFC_EEFC_FMR |= SEFC_EEFC_FMR_FRDY_Msk;
    </#if>

    return true;
}

void ${SEFC_INSTANCE_NAME}_UserSignatureErase(SEFC_USERSIGNATURE_BLOCK block)
{
    ${SEFC_INSTANCE_NAME}_REGS->SEFC_EEFC_FCR = (SEFC_EEFC_FCR_FCMD_EUS | SEFC_EEFC_FCR_FARG((uint32_t)((uint32_t)block << 3U)) | SEFC_EEFC_FCR_FKEY_PASSWD);

    sefc_status = 0;

    <#if INTERRUPT_ENABLE == true>
        <#lt>    ${SEFC_INSTANCE_NAME}_REGS->SEFC_EEFC_FMR |= SEFC_EEFC_FMR_FRDY_Msk;
    </#if>
}

void ${SEFC_INSTANCE_NAME}_CryptographicKeySend(uint16_t sckArg)
{
    ${SEFC_INSTANCE_NAME}_REGS->SEFC_EEFC_FCR = (SEFC_EEFC_FCR_FCMD_SCK | SEFC_EEFC_FCR_FARG((uint32_t)sckArg) | SEFC_EEFC_FCR_FKEY_PASSWD);

    sefc_status = 0;

    <#if INTERRUPT_ENABLE == true>
        <#lt>    ${SEFC_INSTANCE_NAME}_REGS->SEFC_EEFC_FMR |= SEFC_EEFC_FMR_FRDY_Msk;
    </#if>
}

bool ${SEFC_INSTANCE_NAME}_IsBusy(void)
{
    sefc_status |= ${SEFC_INSTANCE_NAME}_REGS->SEFC_EEFC_FSR;
    return (bool)((sefc_status & SEFC_EEFC_FSR_FRDY_Msk) == 0U);
}

SEFC_ERROR ${SEFC_INSTANCE_NAME}_ErrorGet( void )
{
    sefc_status |= ${SEFC_INSTANCE_NAME}_REGS->SEFC_EEFC_FSR;
    return (SEFC_ERROR)sefc_status;
}

void ${SEFC_INSTANCE_NAME}_WriteProtectionSet(uint32_t mode)
{
    ${SEFC_INSTANCE_NAME}_REGS->SEFC_EEFC_WPMR = SEFC_EEFC_WPMR_WPKEY_PASSWD | mode;
}

uint32_t ${SEFC_INSTANCE_NAME}_WriteProtectionGet(void)
{
    return ${SEFC_INSTANCE_NAME}_REGS->SEFC_EEFC_WPMR;
}

<#if INTERRUPT_ENABLE == true>
    <#lt>void ${SEFC_INSTANCE_NAME}_CallbackRegister( SEFC_CALLBACK callback, uintptr_t context )
    <#lt>{
    <#lt>    sefc.callback = callback;
    <#lt>    sefc.context = context;
    <#lt>}
</#if>

<#if INTERRUPT_ENABLE == true>
    <#lt>void __attribute__((used)) ${SEFC_INSTANCE_NAME}_InterruptHandler( void )
    <#lt>{
    <#lt>    uint32_t ul_fmr = ${SEFC_INSTANCE_NAME}_REGS->SEFC_EEFC_FMR;
    <#lt>    ${SEFC_INSTANCE_NAME}_REGS->SEFC_EEFC_FMR = ( ul_fmr & (~SEFC_EEFC_FMR_FRDY_Msk));
    <#lt>    if(sefc.callback != NULL)
    <#lt>    {
    <#lt>        uintptr_t context = sefc.context;
    <#lt>        sefc.callback(context);
    <#lt>    }
    <#lt>}
</#if>
