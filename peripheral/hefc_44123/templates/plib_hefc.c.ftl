/*******************************************************************************
Interface definition of ${HEFC_INSTANCE_NAME} PLIB.

Company:
Microchip Technology Inc.

File Name:
plib_${HEFC_INSTANCE_NAME?lower_case}.h

Summary:
Interface definition of ${HEFC_INSTANCE_NAME} Plib.

Description:
This file defines the interface for the ${HEFC_INSTANCE_NAME} Plib.
It allows user to Program, Erase and lock the on-chip FLASH memory.
*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
* Copyright (C) 2018 Microchip Technology Inc. and its subsidiaries.
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
#include "plib_${HEFC_INSTANCE_NAME?lower_case}.h"
<#if core.CoreSysIntFile == true>
#include "interrupts.h"
</#if>

static uint32_t hefcStatus = 0;

<#if INTERRUPT_ENABLE == true>
    <#lt>static HEFC_OBJECT hefc;
</#if>

void ${HEFC_INSTANCE_NAME}_Initialize(void)
{
    <#if HEFC_FPSI??>
    <#if HEFC_FPSI != "0">
    ${HEFC_INSTANCE_NAME}_REGS->HEFC_FMR = HEFC_FMR_FPSI_Msk;
    </#if>
    </#if>
}
bool ${HEFC_INSTANCE_NAME}_Read( uint32_t *data, uint32_t length, uint32_t address )
{   uint32_t *pAddress = (uint32_t *)address;
    (void)memcpy(data, pAddress, length);
    return true;
}

bool ${HEFC_INSTANCE_NAME}_SectorErase( uint32_t address )
{
    uint16_t page_number;

    /*Calculate the Page number to be passed for FARG register*/
    page_number = (uint16_t)((address - IFLASH_ADDR) / IFLASH_PAGE_SIZE);
    /* Issue the FLASH erase operation*/
    ${HEFC_INSTANCE_NAME}_REGS->HEFC_FCR = (HEFC_FCR_FCMD_EPA| HEFC_FCR_FARG(((uint32_t)page_number << 2U)|0x2U)| HEFC_FCR_FKEY_PASSWD);

    hefcStatus = 0;

    <#if INTERRUPT_ENABLE == true>
        <#lt>    ${HEFC_INSTANCE_NAME}_REGS->HEFC_FMR |= HEFC_FMR_FRDY_Msk;
    </#if>

    return true;
}

bool ${HEFC_INSTANCE_NAME}_PageWrite( uint32_t *data, uint32_t address )
{
    uint16_t page_number;

    /*Calculate the Page number to be passed for FARG register*/
    page_number = (uint16_t)((address - IFLASH_ADDR) / IFLASH_PAGE_SIZE);

    for (uint32_t  i = 0U; i < IFLASH_PAGE_SIZE; i += 4U)
    {
    *((uint32_t *)( IFLASH_ADDR + ( page_number * IFLASH_PAGE_SIZE ) + i )) =    *data;
    data++;
    }

    __DSB();
    __ISB();

    /* Issue the FLASH write operation*/
    ${HEFC_INSTANCE_NAME}_REGS->HEFC_FCR = (HEFC_FCR_FCMD_WP | HEFC_FCR_FARG((uint32_t)page_number)| HEFC_FCR_FKEY_PASSWD);

    hefcStatus = 0;

    <#if INTERRUPT_ENABLE == true>
        <#lt>    ${HEFC_INSTANCE_NAME}_REGS->HEFC_FMR |= HEFC_FMR_FRDY_Msk;
    </#if>

    return true;
}


void ${HEFC_INSTANCE_NAME}_RegionLock(uint32_t address)
{
    uint16_t page_number;

    /*Calculate the Page number to be passed for FARG register*/
    page_number = (uint16_t)((address - IFLASH_ADDR) / IFLASH_PAGE_SIZE);
    ${HEFC_INSTANCE_NAME}_REGS->HEFC_FCR = (HEFC_FCR_FCMD_SLB | HEFC_FCR_FARG((uint32_t)page_number)| HEFC_FCR_FKEY_PASSWD);

    hefcStatus = 0;

    <#if INTERRUPT_ENABLE == true>
        <#lt>    ${HEFC_INSTANCE_NAME}_REGS->HEFC_FMR |= HEFC_FMR_FRDY_Msk;
    </#if>
}

void ${HEFC_INSTANCE_NAME}_RegionUnlock(uint32_t address)
{
    uint16_t page_number;

    /*Calculate the Page number to be passed for FARG register*/
    page_number = (uint16_t)((address - IFLASH_ADDR) / IFLASH_PAGE_SIZE);
    ${HEFC_INSTANCE_NAME}_REGS->HEFC_FCR = (HEFC_FCR_FCMD_CLB | HEFC_FCR_FARG((uint32_t)page_number)| HEFC_FCR_FKEY_PASSWD);

    hefcStatus = 0;

    <#if INTERRUPT_ENABLE == true>
        <#lt>    ${HEFC_INSTANCE_NAME}_REGS->HEFC_FMR |= HEFC_FMR_FRDY_Msk;
    </#if>
}

bool ${HEFC_INSTANCE_NAME}_IsBusy(void)
{
    hefcStatus |= ${HEFC_INSTANCE_NAME}_REGS->HEFC_FSR;
    return (bool)((hefcStatus & HEFC_FSR_FRDY_Msk) == 0U);
}

HEFC_ERROR ${HEFC_INSTANCE_NAME}_ErrorGet( void )
{
    hefcStatus |= ${HEFC_INSTANCE_NAME}_REGS->HEFC_FSR;
    return (HEFC_ERROR)hefcStatus;
}

<#if INTERRUPT_ENABLE == true>
    <#lt>void ${HEFC_INSTANCE_NAME}_CallbackRegister( HEFC_CALLBACK callback, uintptr_t context )
    <#lt>{
    <#lt>    hefc.callback = callback;
    <#lt>    hefc.context = context;
    <#lt>}
</#if>

<#if INTERRUPT_ENABLE == true>
    <#lt>void ${HEFC_INSTANCE_NAME}_InterruptHandler( void )
    <#lt>{
    <#lt>    uint32_t ul_fmr = ${HEFC_INSTANCE_NAME}_REGS->HEFC_FMR;
    <#lt>    ${HEFC_INSTANCE_NAME}_REGS->HEFC_FMR = ( ul_fmr & (~HEFC_FMR_FRDY_Msk));
    <#lt>    if(hefc.callback != NULL)
    <#lt>        {
        <#lt>            hefc.callback(hefc.context);
    <#lt>        }
    <#lt>}
</#if>
