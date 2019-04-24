/*******************************************************************************
  Non-Volatile Memory Controller(${NVMCTRL_INSTANCE_NAME}) PLIB.

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${NVMCTRL_INSTANCE_NAME?lower_case}.c

  Summary:
    Interface definition of ${NVMCTRL_INSTANCE_NAME} Plib.

  Description:
    This file defines the interface for the ${NVMCTRL_INSTANCE_NAME} Plib.
    It allows user to Program, Erase and lock the on-chip Non Volatile Flash
    Memory.
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

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

#include <string.h>
#include "plib_${NVMCTRL_INSTANCE_NAME?lower_case}.h"

static uint32_t status = 0;

// *****************************************************************************
// *****************************************************************************
// Section: ${NVMCTRL_INSTANCE_NAME} Implementation
// *****************************************************************************
// *****************************************************************************

<#if INTERRUPT_ENABLE == true>
    <#lt>NVMCTRL_CALLBACK ${NVMCTRL_INSTANCE_NAME?lower_case}CallbackFunc;

    <#lt>uintptr_t ${NVMCTRL_INSTANCE_NAME?lower_case}Context;

    <#lt>void ${NVMCTRL_INSTANCE_NAME}_CallbackRegister( NVMCTRL_CALLBACK callback, uintptr_t context )
    <#lt>{
    <#lt>    /* Register callback function */
    <#lt>    ${NVMCTRL_INSTANCE_NAME?lower_case}CallbackFunc = callback;
    <#lt>    ${NVMCTRL_INSTANCE_NAME?lower_case}Context = context;
    <#lt>}

    <#lt>void ${NVMCTRL_INSTANCE_NAME}_InterruptHandler(void)
    <#lt>{
    <#lt>    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_INTENCLR = NVMCTRL_INTENCLR_READY_Msk;

    <#lt>    if(${NVMCTRL_INSTANCE_NAME?lower_case}CallbackFunc != NULL)
    <#lt>    {
    <#lt>        ${NVMCTRL_INSTANCE_NAME?lower_case}CallbackFunc(${NVMCTRL_INSTANCE_NAME?lower_case}Context);
    <#lt>    }
    <#lt>}
</#if>

void ${NVMCTRL_INSTANCE_NAME}_Initialize(void)
{
    <@compress single_line=true>${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_CTRLB = ${NVMCTRL_CACHE_ENABLE?then('', 'NVMCTRL_CTRLB_CACHEDIS_Msk |')}
    <#lt>                       NVMCTRL_CTRLB_READMODE_${NVMCTRL_CTRLB_READMODE_SELECTION} |
    <#lt>                       NVMCTRL_CTRLB_SLEEPPRM_${NVMCTRL_CTRLB_POWER_REDUCTION_MODE} | NVMCTRL_CTRLB_RWS(${NVM_RWS})
    <#lt>                       ${(NVMCTRL_WRITE_POLICY == "MANUAL")?then('| NVMCTRL_CTRLB_MANW_Msk', ' ')};</@compress>
}

<#if NVMCTRL_CACHE_ENABLE == true>
    <#lt>void ${NVMCTRL_INSTANCE_NAME}_CacheInvalidate(void)
    <#lt>{
    <#lt>    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_CTRLA = NVMCTRL_CTRLA_CMD_INVALL | NVMCTRL_CTRLA_CMDEX_KEY;
    <#lt>}
</#if>
<#if FLASH_RWWEEPROM_START_ADDRESS??>
bool ${NVMCTRL_INSTANCE_NAME}_RWWEEPROM_Read( uint32_t *data, uint32_t length, const uint32_t address )
{
    memcpy((void *)data, (void *)address, length);
    return true;
}

bool ${NVMCTRL_INSTANCE_NAME}_RWWEEPROM_PageWrite ( uint32_t *data, const uint32_t address )
{
    uint32_t i = 0;
    uint32_t * paddress = (uint32_t *)address;

    /* Clear global error flag */
    status = 0;

    /* Writing 32-bit words in the given address */
    for ( i = 0; i < (${NVMCTRL_INSTANCE_NAME}_RWWEEPROM_PAGESIZE/4); i++)
    {
        *paddress++ = data[i];
    }

<#if NVMCTRL_WRITE_POLICY == "MANUAL">
     /* Set address and command */
    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_ADDR = address >> 1;

    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_CTRLA = NVMCTRL_CTRLA_CMD_RWWEEWP | NVMCTRL_CTRLA_CMDEX_KEY;
</#if>

<#if INTERRUPT_ENABLE == true>
    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_INTENSET = NVMCTRL_INTENSET_READY_Msk;
</#if>
    return true;
}

bool ${NVMCTRL_INSTANCE_NAME}_RWWEEPROM_RowErase( uint32_t address )
{
    /* Clear global error flag */
    status = 0;

     /* Set address and command */
    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_ADDR = address >> 1;

    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_CTRLA = NVMCTRL_CTRLA_CMD_RWWEEER | NVMCTRL_CTRLA_CMDEX_KEY;

<#if INTERRUPT_ENABLE == true>
    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_INTENSET = NVMCTRL_INTENSET_READY_Msk;
</#if>
    return true;
}
</#if>
bool ${NVMCTRL_INSTANCE_NAME}_Read( uint32_t *data, uint32_t length, const uint32_t address )
{
    memcpy((void *)data, (void *)address, length);
    return true;
}

bool ${NVMCTRL_INSTANCE_NAME}_PageWrite( uint32_t *data, const uint32_t address )
{
    uint32_t i = 0;
    uint32_t * paddress = (uint32_t *)address;

    /* Clear global error flag */
    status = 0;

    /* writing 32-bit data into the given address */
    for (i = 0; i < (${NVMCTRL_INSTANCE_NAME}_FLASH_PAGESIZE/4); i++)
    {
        *paddress++ = data[i];
    }

<#if NVMCTRL_WRITE_POLICY == "MANUAL">
     /* Set address and command */
    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_ADDR = address >> 1;

    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_CTRLA = NVMCTRL_CTRLA_CMD_WP_Val | NVMCTRL_CTRLA_CMDEX_KEY;
</#if>

<#if INTERRUPT_ENABLE == true>
    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_INTENSET = NVMCTRL_INTENSET_READY_Msk;
</#if>
    return true;
}

bool ${NVMCTRL_INSTANCE_NAME}_RowErase( uint32_t address )
{
    /* Clear global error flag */
    status = 0;

    /* Set address and command */
    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_ADDR = address >> 1;

    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_CTRLA = NVMCTRL_CTRLA_CMD_ER_Val | NVMCTRL_CTRLA_CMDEX_KEY;

<#if INTERRUPT_ENABLE == true>
    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_INTENSET = NVMCTRL_INTENSET_READY_Msk;
</#if>
    return true;
}

NVMCTRL_ERROR ${NVMCTRL_INSTANCE_NAME}_ErrorGet( void )
{
    status |= ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_STATUS;
    return status;
}

bool ${NVMCTRL_INSTANCE_NAME}_IsBusy(void)
{
    return (bool)(!(${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_INTFLAG & NVMCTRL_INTFLAG_READY_Msk));
}

void ${NVMCTRL_INSTANCE_NAME}_RegionLock(uint32_t address)
{
    /* Clear global error flag */
    status = 0;

    /* Set address and command */
    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_ADDR = address >> 1;

    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_CTRLA = NVMCTRL_CTRLA_CMD_LR_Val | NVMCTRL_CTRLA_CMDEX_KEY;
}

void ${NVMCTRL_INSTANCE_NAME}_RegionUnlock(uint32_t address)
{
    /* Clear global error flag */
    status = 0;

    /* Set address and command */
    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_ADDR = address >> 1;

    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_CTRLA = NVMCTRL_CTRLA_CMD_UR_Val | NVMCTRL_CTRLA_CMDEX_KEY;
}
