/*******************************************************************************
Interface definition of EFC PLIB.

Company:
Microchip Technology Inc.

File Name:
plib_EFC.h

Summary:
Interface definition of EFC Plib.

Description:
This file defines the interface for the EFC Plib.
It allows user to Program, Erase and lock the on-chip FLASH memory.
*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
Copyright (c) 2017 released Microchip Technology Inc.  All rights reserved.
Microchip licenses to you the right to use, modify, copy and distribute
Software only when embedded on a Microchip microcontroller or digital signal
controller that is integrated into your product or third party product
(pursuant to the sublicense terms in the accompanying license agreement).
You should refer to the license agreement accompanying this Software for
additional information regarding your rights and obligations.
SOFTWARE AND DOCUMENTATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND,
EITHER EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION, ANY WARRANTY OF
MERCHANTABILITY, TITLE, NON-INFRINGEMENT AND FITNESS FOR A PARTICULAR PURPOSE.
IN NO EVENT SHALL MICROCHIP OR ITS LICENSORS BE LIABLE OR OBLIGATED UNDER
CONTRACT, NEGLIGENCE, STRICT LIABILITY, CONTRIBUTION, BREACH OF WARRANTY, OR
OTHER LEGAL EQUITABLE THEORY ANY DIRECT OR INDIRECT DAMAGES OR EXPENSES
INCLUDING BUT NOT LIMITED TO ANY INCIDENTAL, SPECIAL, INDIRECT, PUNITIVE OR
CONSEQUENTIAL DAMAGES, LOST PROFITS OR LOST DATA, COST OF PROCUREMENT OF
SUBSTITUTE GOODS, TECHNOLOGY, SERVICES, OR ANY CLAIMS BY THIRD PARTIES
(INCLUDING BUT NOT LIMITED TO ANY DEFENSE THEREOF), OR OTHER SIMILAR COSTS.
*******************************************************************************/

#include <string.h>
#include "${__PROCESSOR?lower_case}.h"
#include "plib_efc${INDEX?string}.h"

static uint32_t status = 0;

<#if INTERRUPT_ENABLE == true>
    <#lt>EFC_OBJECT efc;
</#if>

bool EFC${INDEX?string}_Read( uint32_t *data, uint32_t length, uint32_t address )
{
    memcpy((void *)data, (void *)address, length);
    return true;
}

bool EFC${INDEX?string}_SectorErase( uint32_t address )
{
    volatile uint16_t page_number;

    /*Calculate the Page number to be passed for FARG register*/
    page_number = (address - IFLASH_ADDR) / IFLASH_PAGE_SIZE;
    /* Issue the FLASH erase operation*/
    EFC_REGS->EEFC_FCR = (EEFC_FCR_FCMD_EPA|EEFC_FCR_FARG(page_number|0x2)|EEFC_FCR_FKEY_PASSWD);

    status = 0;

    <#if INTERRUPT_ENABLE == true>
        <#lt>    EFC_REGS->EEFC_FMR|= EEFC_FMR_FRDY_Msk;
    </#if>

    return true;
}

bool EFC${INDEX?string}_PageWrite( uint32_t *data, uint32_t address )
{
    volatile uint16_t page_number;
    /*Calculate the Page number to be passed for FARG register*/
    page_number = (address - IFLASH_ADDR) / IFLASH_PAGE_SIZE;

    for (int i = 0; i < IFLASH_PAGE_SIZE; i += 4)
    {
    *((uint32_t *)( IFLASH_ADDR + ( page_number * IFLASH_PAGE_SIZE ) + i )) =    *(( data++ ));
    }
    /* Issue the FLASH write operation*/
    EFC_REGS->EEFC_FCR = (EEFC_FCR_FCMD_WP | EEFC_FCR_FARG(page_number)| EEFC_FCR_FKEY_PASSWD);

    status = 0;

    <#if INTERRUPT_ENABLE == true>
        <#lt>        EFC_REGS->EEFC_FMR|= EEFC_FMR_FRDY_Msk;
    </#if>

    return true;
}

bool EFC${INDEX?string}_WriteQuadWord( uint32_t *data, uint32_t address )
{
    volatile uint16_t page_number;

    /*Calculate the Page number to be passed for FARG register*/
    page_number = (address - IFLASH_ADDR) / IFLASH_PAGE_SIZE;

    for (int i = 0; i < 16; i += 4)
    {
    *((uint32_t *)(( address ) + i )) =    *((uint32_t *)( data++ ));
    }
    /* Issue the FLASH write operation*/
    EFC_REGS->EEFC_FCR = (EEFC_FCR_FCMD_WP | EEFC_FCR_FARG(page_number)| EEFC_FCR_FKEY_PASSWD);

    status = 0;

    <#if INTERRUPT_ENABLE == true>
        <#lt>        EFC_REGS->EEFC_FMR|= EEFC_FMR_FRDY_Msk;
    </#if>

    return true;
}

void EFC${INDEX?string}_RegionLock(uint32_t address)
{
    volatile uint16_t page_number;
    /*Calculate the Page number to be passed for FARG register*/
    page_number = (address - IFLASH_ADDR) / IFLASH_PAGE_SIZE;
    EFC_REGS->EEFC_FCR = (EEFC_FCR_FCMD_SLB | EEFC_FCR_FARG(page_number)| EEFC_FCR_FKEY_PASSWD);

    status = 0;

    <#if INTERRUPT_ENABLE == true>
        <#lt>        EFC_REGS->EEFC_FMR|= EEFC_FMR_FRDY_Msk;
    </#if>
}

void EFC${INDEX?string}_RegionUnlock(uint32_t address)
{
    volatile uint16_t page_number;
    /*Calculate the Page number to be passed for FARG register*/
    page_number = (address - IFLASH_ADDR) / IFLASH_PAGE_SIZE;
    EFC_REGS->EEFC_FCR = (EEFC_FCR_FCMD_CLB | EEFC_FCR_FARG(page_number)| EEFC_FCR_FKEY_PASSWD);

    status = 0;

    <#if INTERRUPT_ENABLE == true>
        <#lt>        EFC_REGS->EEFC_FMR|= EEFC_FMR_FRDY_Msk;
    </#if>
}

bool EFC${INDEX?string}_IsBusy(void)
{
    status |= EFC_REGS->EEFC_FSR;
    return (bool)(!(status & EEFC_FSR_FRDY_Msk));
}

EFC_ERR EFC${INDEX?string}_ErrorGet( void )
{
    status |= EFC_REGS->EEFC_FSR;
    return status;
}

<#if INTERRUPT_ENABLE == true>
    <#lt>void EFC${INDEX?string}_CallbackRegister( EFC_CALLBACK callback, uintptr_t context )
    <#lt>{
    <#lt>    efc.callback = callback;
    <#lt>    efc.context = context;
    <#lt>}
</#if>

<#if INTERRUPT_ENABLE == true>
    <#lt>void EFC${INDEX?string}_InterruptHandler( void )
    <#lt>{
    <#lt>    uint32_t ul_fmr = EFC_REGS->EEFC_FMR;
    <#lt>    EFC_REGS->EEFC_FMR = ( ul_fmr & (~EEFC_FMR_FRDY_Msk));
    <#lt>    if(efc.callback != NULL)
    <#lt>        {
        <#lt>            efc.callback(efc.context);
    <#lt>        }
    <#lt>}
</#if>

<#if DRV_MEMORY_CONNECTED == true>
    <#lt>bool EFC${INDEX?string}_GeometryGet(EFC_GEOMETRY *geometry)
    <#lt>{
    <#lt>    /* Read block size and number of blocks */
    <#lt>    geometry->read_blockSize = 1;
    <#lt>    geometry->read_numBlocks = (EFC${INDEX?string}_MEDIA_SIZE * EFC${INDEX?string}_MEDIA_SIZE);

    <#lt>    /* Write block size and number of blocks */
    <#lt>    geometry->write_blockSize = EFC${INDEX?string}_PAGESIZE;
    <#lt>    geometry->write_numBlocks = (EFC${INDEX?string}_MEDIA_SIZE * EFC${INDEX?string}_MEDIA_SIZE) / EFC${INDEX?string}_PAGESIZE;

    <#lt>    /* Erase block size and number of blocks */
    <#lt>    geometry->erase_blockSize = EFC0_ROWSIZE;
    <#lt>    geometry->erase_numBlocks = (EFC${INDEX?string}_MEDIA_SIZE * EFC${INDEX?string}_MEDIA_SIZE) / EFC${INDEX?string}_ROWSIZE;

    <#lt>    geometry->numReadRegions = 1;
    <#lt>    geometry->numWriteRegions = 1;
    <#lt>    geometry->numEraseRegions = 1;

    <#lt>    geometry->blockStartAddress = 0x${START_ADDRESS};
    <#lt>    return true;
    <#lt>}
</#if>