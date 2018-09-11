/*******************************************************************************
  Non-Volatile Memory Controller(NVMCTRL${NVMCTRL_INDEX?string}) PLIB.

  Company:
    Microchip Technology Inc.

  File Name:
    plib_nvmctrl${NVMCTRL_INDEX?string}.c

  Summary:
    Interface definition of NVMCTRL${NVMCTRL_INDEX?string} Plib.

  Description:
    This file defines the interface for the NVMCTRL${NVMCTRL_INDEX?string} Plib.
    It allows user to Program, Erase and lock the on-chip Non Volatile Flash
    Memory.
*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
Copyright (c) 2016 released Microchip Technology Inc.  All rights reserved.

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
// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

#include <string.h>
#include "plib_nvmctrl${NVMCTRL_INDEX?string}.h"

static uint32_t status = 0;

// *****************************************************************************
// *****************************************************************************
// Section: NVMCTRL${NVMCTRL_INDEX?string} Implementation
// *****************************************************************************
// *****************************************************************************

<#if NVMCTRL_INTERRUPT_MODE == true>

    <#lt>NVMCTRL_CALLBACK nvmctrl${NVMCTRL_INDEX?string}CallbackFunc;

    <#lt>uintptr_t nvmctrl${NVMCTRL_INDEX?string}context;

    <#lt>void NVMCTRL${NVMCTRL_INDEX?string}_CallbackRegister( NVMCTRL_CALLBACK callback, uintptr_t context )
    <#lt>{
    <#lt>    /* Register callback function */
    <#lt>    nvmctrl${NVMCTRL_INDEX?string}CallbackFunc = callback;
    <#lt>    nvmctrl${NVMCTRL_INDEX?string}context = context;
    <#lt>}

    <#lt>void NVMCTRL${NVMCTRL_INDEX?string}_InterruptHandler(void)
    <#lt>{
    <#lt>    if(( NVMCTRL_REGS->NVMCTRL_INTFLAG & NVMCTRL_INTFLAG_READY_Msk ) && (NVMCTRL_REGS->NVMCTRL_INTENSET & NVMCTRL_INTENSET_READY_Msk))
    <#lt>    {
    <#lt>        if(*nvmctrl0CallbackFunc != NULL)
    <#lt>        {
    <#lt>            /* Calling callback func */
    <#lt>            (*nvmctrl0CallbackFunc)(nvmctrl0context);
    <#lt>        }

    <#lt>        /* Clear interrupt */
    <#lt>        NVMCTRL_REGS->NVMCTRL_INTENCLR = NVMCTRL_INTENCLR_READY_Msk;
    <#lt>    }
    <#lt>}
</#if>

void NVMCTRL${NVMCTRL_INDEX?string}_Initialize(void)
{
    /* Disable Manual Write */
    <@compress single_line=true>NVMCTRL_REGS->NVMCTRL_CTRLB = NVMCTRL_CTRLB_READMODE_${NVMCTRL_CTRLB_READMODE_SELECTION}
                                                         | NVMCTRL_CTRLB_SLEEPPRM_${NVMCTRL_CTRLB_POWER_REDUCTION_MODE}
                                                         ${NVMCTRL_CACHE_ENABLE?then('', '| NVMCTRL_CTRLB_CACHEDIS_Msk')};</@compress>

    /* Clear error flags */
    NVMCTRL_REGS->NVMCTRL_STATUS = (0x00U);

<#if NVMCTRL_INTERRUPT_MODE == true>
    /* Clear interrupt flag */
    NVMCTRL_REGS->NVMCTRL_INTENCLR = NVMCTRL_INTENCLR_READY_Msk;
</#if>
}

<#if NVMCTRL_CACHE_ENABLE == true>
    <#lt>void NVMCTRL${NVMCTRL_INDEX?string}_CacheInvalidate(void)
    <#lt>{
    <#lt>    NVMCTRL_REGS->NVMCTRL_CTRLA = NVMCTRL_CTRLA_CMD_INVALL | NVMCTRL_CTRLA_CMDEX_KEY;
    <#lt>}
</#if>

<#if NVMCTRL_RWW_EEPROM == true>
    <#lt>bool NVMCTRL${NVMCTRL_INDEX?string}_RWWEEPROM_Read( uint32_t *data, uint32_t length, const uint32_t address )
    <#lt>{
    <#lt>    memcpy((void *)data, (void *)address, length);
    <#lt>    return true;
    <#lt>}

    <#lt>bool NVMCTRL${NVMCTRL_INDEX?string}_RWWEEPROM_PageWrite ( uint32_t *data, const uint32_t address )
    <#lt>{
    <#lt>    uint32_t i = 0;
    <#lt>    uint32_t * paddress = (uint32_t *)address;

    <#lt>    /* Clear error flags */
    <#lt>    NVMCTRL_REGS->NVMCTRL_STATUS = 0x1C;

    <#lt>    /* Clear global error flag */
    <#lt>    status = 0;

    <#lt>    /* Erase the page buffer before buffering new data */
    <#lt>    NVMCTRL_REGS->NVMCTRL_CTRLA = NVMCTRL_CTRLA_CMD_PBC_Val | NVMCTRL_CTRLA_CMDEX_KEY;

    <#lt>    /* Writing 32-bit words in the given address */
    <#lt>    for ( i = 0; i < (NVMCTRL${NVMCTRL_INDEX?string}_RWWEEPROM_PAGESIZE/4); i++)
    <#lt>    {
    <#lt>        *paddress++ = data[i];
    <#lt>    }

    <#lt><#if NVMCTRL_INTERRUPT_MODE == true>
    <#lt>    NVMCTRL_REGS->NVMCTRL_INTENSET = NVMCTRL_INTENSET_READY_Msk;
    <#lt><#else>
    <#lt>    /* Check if the module is busy */
    <#lt>    while((NVMCTRL_REGS->NVMCTRL_INTFLAG & NVMCTRL_INTFLAG_READY_Msk) != NVMCTRL_INTFLAG_READY_Msk)
    <#lt>    {
    <#lt>        /* Force-wait for the buffer clear to complete */
    <#lt>    }
    <#lt></#if>

    <#lt>     return true;

    <#lt>}

    <#lt>bool NVMCTRL${NVMCTRL_INDEX?string}_RWWEEPROM_RowErase( uint32_t address )
    <#lt>{
    <#lt>    /* Clear error flags */
    <#lt>    NVMCTRL_REGS->NVMCTRL_STATUS = 0x1C;

    <#lt>    /* Clear global error flag */
    <#lt>    status = 0;

    <#lt>     /* Set address and command */
    <#lt>    NVMCTRL_REGS->NVMCTRL_ADDR = address >> 1;

    <#lt>    NVMCTRL_REGS->NVMCTRL_CTRLA = NVMCTRL_CTRLA_CMD_RWWEEER | NVMCTRL_CTRLA_CMDEX_KEY;

    <#lt><#if NVMCTRL_INTERRUPT_MODE == true>
    <#lt>    NVMCTRL_REGS->NVMCTRL_INTENSET = NVMCTRL_INTENSET_READY_Msk;
    <#lt><#else>
    <#lt>    /* Check if the module is busy */
    <#lt>    while((NVMCTRL_REGS->NVMCTRL_INTFLAG & NVMCTRL_INTFLAG_READY_Msk) != NVMCTRL_INTFLAG_READY_Msk)
    <#lt>    {
    <#lt>        /* Force-wait for the buffer clear to complete */
    <#lt>    }
    <#lt></#if>

    <#lt>     return true;

    <#lt>}
</#if>

bool NVMCTRL${NVMCTRL_INDEX?string}_Read( uint32_t *data, uint32_t length, const uint32_t address )
{
    memcpy((void *)data, (void *)address, length);
    return true;
}

bool NVMCTRL${NVMCTRL_INDEX?string}_PageWrite( uint32_t *data, const uint32_t address )
{
    uint32_t i = 0;
    uint32_t * paddress = (uint32_t *)address;

    /* Clear error flags */
    NVMCTRL_REGS->NVMCTRL_STATUS = 0x1C;

    /* Clear global error flag */
    status = 0;

    /* Erase the page buffer before buffering new data */
    NVMCTRL_REGS->NVMCTRL_CTRLA = NVMCTRL_CTRLA_CMD_PBC_Val | NVMCTRL_CTRLA_CMDEX_KEY;

    /* writing 32-bit data into the given address */
    for (i = 0; i < (NVMCTRL${NVMCTRL_INDEX?string}_FLASH_PAGESIZE/4); i++)
    {
        *paddress++ = data[i];
    }

<#if NVMCTRL_INTERRUPT_MODE == true>
    NVMCTRL_REGS->NVMCTRL_INTENSET = NVMCTRL_INTENSET_READY_Msk;
<#else>
    /* Check if the module is busy */
    while((NVMCTRL_REGS->NVMCTRL_INTFLAG & NVMCTRL_INTFLAG_READY_Msk) != NVMCTRL_INTFLAG_READY_Msk)
    {
        /* Force-wait for the buffer clear to complete */
    }
</#if>

    return true;
}

bool NVMCTRL${NVMCTRL_INDEX?string}_RowErase( uint32_t address )
{
    /* Clear error flags */
    NVMCTRL_REGS->NVMCTRL_STATUS = 0x1C;

    /* Clear global error flag */
    status = 0;

    /* Set address and command */
    NVMCTRL_REGS->NVMCTRL_ADDR = address >> 1;

    NVMCTRL_REGS->NVMCTRL_CTRLA = NVMCTRL_CTRLA_CMD_ER_Val | NVMCTRL_CTRLA_CMDEX_KEY;

<#if NVMCTRL_INTERRUPT_MODE == true>
    NVMCTRL_REGS->NVMCTRL_INTENSET = NVMCTRL_INTENSET_READY_Msk;
<#else>
    /* Check if the module is busy */
    while((NVMCTRL_REGS->NVMCTRL_INTFLAG & NVMCTRL_INTFLAG_READY_Msk) != NVMCTRL_INTFLAG_READY_Msk)
    {
        /* Force-wait for the buffer clear to complete */
    }
</#if>

    return true;
}

NVMCTRL_ERROR NVMCTRL${NVMCTRL_INDEX?string}_ErrorGet( void )
{
    return (status |= NVMCTRL_REGS->NVMCTRL_STATUS);
}

bool NVMCTRL${NVMCTRL_INDEX?string}_IsBusy(void)
{
    return (!(NVMCTRL_REGS->NVMCTRL_INTFLAG & NVMCTRL_INTFLAG_READY_Msk));
}

<#if NVMCTRL_REGION_LOCK_UNLOCK == true>
    <#lt>void NVMCTRL${NVMCTRL_INDEX?string}_RegionLock(uint32_t address)
    <#lt>{
    <#lt>    /* Clear error flags */
    <#lt>    NVMCTRL_REGS->NVMCTRL_STATUS = 0x1C;

    <#lt>    /* Clear global error flag */
    <#lt>    status = 0;

    <#lt>    /* Set address and command */
    <#lt>    NVMCTRL_REGS->NVMCTRL_ADDR = address >> 1;

    <#lt>    NVMCTRL_REGS->NVMCTRL_CTRLA = NVMCTRL_CTRLA_CMD_LR_Val | NVMCTRL_CTRLA_CMDEX_KEY;
    <#lt>}

    <#lt>void NVMCTRL${NVMCTRL_INDEX?string}_RegionUnlock(uint32_t address)
    <#lt>{
    <#lt>    /* Clear error flags */
    <#lt>    NVMCTRL_REGS->NVMCTRL_STATUS = 0x1C;

    <#lt>    /* Clear global error flag */
    <#lt>    status = 0;

    <#lt>    /* Set address and command */
    <#lt>    NVMCTRL_REGS->NVMCTRL_ADDR = address >> 1;

    <#lt>    NVMCTRL_REGS->NVMCTRL_CTRLA = NVMCTRL_CTRLA_CMD_UR_Val | NVMCTRL_CTRLA_CMDEX_KEY;
    <#lt>}
</#if>
