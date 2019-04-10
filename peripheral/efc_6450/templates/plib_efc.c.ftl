/*******************************************************************************
Interface definition of ${EFC_INSTANCE_NAME} PLIB.

Company:
Microchip Technology Inc.

File Name:
plib_${EFC_INSTANCE_NAME?lower_case}.h

Summary:
Interface definition of ${EFC_INSTANCE_NAME} Plib.

Description:
This file defines the interface for the ${EFC_INSTANCE_NAME} Plib.
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
#include "plib_${EFC_INSTANCE_NAME?lower_case}.h"

static uint32_t status = 0;

<#if INTERRUPT_ENABLE == true>
    <#lt>EFC_OBJECT efc;
</#if>

void ${EFC_INSTANCE_NAME}_Initialize(void)
{
    ${EFC_INSTANCE_NAME}_REGS->EEFC_FMR = EEFC_FMR_FWS(${NVM_RWS}) | EEFC_FMR_CLOE_Msk;
}
bool ${EFC_INSTANCE_NAME}_Read( uint32_t *data, uint32_t length, uint32_t address )
{
    memcpy((void *)data, (void *)address, length);
    return true;
}

bool ${EFC_INSTANCE_NAME}_SectorErase( uint32_t address )
{
    uint16_t page_number;

    /*Calculate the Page number to be passed for FARG register*/
    page_number = (address - IFLASH_ADDR) / IFLASH_PAGE_SIZE;
    /* Issue the FLASH erase operation*/
    ${EFC_INSTANCE_NAME}_REGS->EEFC_FCR = (EEFC_FCR_FCMD_EPA|EEFC_FCR_FARG(page_number|0x2)|EEFC_FCR_FKEY_PASSWD);

    status = 0;

    <#if INTERRUPT_ENABLE == true>
        <#lt>    ${EFC_INSTANCE_NAME}_REGS->EEFC_FMR |= EEFC_FMR_FRDY_Msk;
    </#if>

    return true;
}

bool ${EFC_INSTANCE_NAME}_PageWrite( uint32_t *data, uint32_t address )
{
    uint16_t page_number;

    /*Calculate the Page number to be passed for FARG register*/
    page_number = (address - IFLASH_ADDR) / IFLASH_PAGE_SIZE;

    for (int i = 0; i < IFLASH_PAGE_SIZE; i += 4)
    {
    *((uint32_t *)( IFLASH_ADDR + ( page_number * IFLASH_PAGE_SIZE ) + i )) =    *(( data++ ));
    }

    __DSB();
    __ISB();

    /* Issue the FLASH write operation*/
    ${EFC_INSTANCE_NAME}_REGS->EEFC_FCR = (EEFC_FCR_FCMD_WP | EEFC_FCR_FARG(page_number)| EEFC_FCR_FKEY_PASSWD);

    status = 0;

    <#if INTERRUPT_ENABLE == true>
        <#lt>    ${EFC_INSTANCE_NAME}_REGS->EEFC_FMR |= EEFC_FMR_FRDY_Msk;
    </#if>

    return true;
}

bool ${EFC_INSTANCE_NAME}_QuadWordWrite( uint32_t *data, uint32_t address )
{
    uint16_t page_number;

    /*Calculate the Page number to be passed for FARG register*/
    page_number = (address - IFLASH_ADDR) / IFLASH_PAGE_SIZE;

    for (int i = 0; i < 16; i += 4)
    {
    *((uint32_t *)(( address ) + i )) =    *((uint32_t *)( data++ ));
    }
    /* Issue the FLASH write operation*/
    ${EFC_INSTANCE_NAME}_REGS->EEFC_FCR = (EEFC_FCR_FCMD_WP | EEFC_FCR_FARG(page_number)| EEFC_FCR_FKEY_PASSWD);

    status = 0;

    <#if INTERRUPT_ENABLE == true>
        <#lt>    ${EFC_INSTANCE_NAME}_REGS->EEFC_FMR |= EEFC_FMR_FRDY_Msk;
    </#if>

    return true;
}

void ${EFC_INSTANCE_NAME}_RegionLock(uint32_t address)
{
    uint16_t page_number;

    /*Calculate the Page number to be passed for FARG register*/
    page_number = (address - IFLASH_ADDR) / IFLASH_PAGE_SIZE;
    ${EFC_INSTANCE_NAME}_REGS->EEFC_FCR = (EEFC_FCR_FCMD_SLB | EEFC_FCR_FARG(page_number)| EEFC_FCR_FKEY_PASSWD);

    status = 0;

    <#if INTERRUPT_ENABLE == true>
        <#lt>    ${EFC_INSTANCE_NAME}_REGS->EEFC_FMR |= EEFC_FMR_FRDY_Msk;
    </#if>
}

void ${EFC_INSTANCE_NAME}_RegionUnlock(uint32_t address)
{
    uint16_t page_number;

    /*Calculate the Page number to be passed for FARG register*/
    page_number = (address - IFLASH_ADDR) / IFLASH_PAGE_SIZE;
    ${EFC_INSTANCE_NAME}_REGS->EEFC_FCR = (EEFC_FCR_FCMD_CLB | EEFC_FCR_FARG(page_number)| EEFC_FCR_FKEY_PASSWD);

    status = 0;

    <#if INTERRUPT_ENABLE == true>
        <#lt>    ${EFC_INSTANCE_NAME}_REGS->EEFC_FMR |= EEFC_FMR_FRDY_Msk;
    </#if>
}

bool ${EFC_INSTANCE_NAME}_IsBusy(void)
{
    status |= ${EFC_INSTANCE_NAME}_REGS->EEFC_FSR;
    return (bool)(!(status & EEFC_FSR_FRDY_Msk));
}

EFC_ERROR ${EFC_INSTANCE_NAME}_ErrorGet( void )
{
    status |= ${EFC_INSTANCE_NAME}_REGS->EEFC_FSR;
    return status;
}

<#if INTERRUPT_ENABLE == true>
    <#lt>void ${EFC_INSTANCE_NAME}_CallbackRegister( EFC_CALLBACK callback, uintptr_t context )
    <#lt>{
    <#lt>    efc.callback = callback;
    <#lt>    efc.context = context;
    <#lt>}
</#if>

<#if INTERRUPT_ENABLE == true>
    <#lt>void ${EFC_INSTANCE_NAME}_InterruptHandler( void )
    <#lt>{
    <#lt>    uint32_t ul_fmr = ${EFC_INSTANCE_NAME}_REGS->EEFC_FMR;
    <#lt>    ${EFC_INSTANCE_NAME}_REGS->EEFC_FMR = ( ul_fmr & (~EEFC_FMR_FRDY_Msk));
    <#lt>    if(efc.callback != NULL)
    <#lt>        {
        <#lt>            efc.callback(efc.context);
    <#lt>        }
    <#lt>}
</#if>
