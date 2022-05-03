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
<#if core.CoreSysIntFile == true>
#include "interrupts.h"
</#if>
#include "plib_${NVMCTRL_INSTANCE_NAME?lower_case}.h"

// *****************************************************************************
// *****************************************************************************
// Section: ${NVMCTRL_INSTANCE_NAME} Implementation
// *****************************************************************************
// *****************************************************************************

<#if INTERRUPT_ENABLE == true>
    <#lt>static NVMCTRL_CALLBACK ${NVMCTRL_INSTANCE_NAME?lower_case}CallbackFunc;

    <#lt>static uintptr_t ${NVMCTRL_INSTANCE_NAME?lower_case}Context;

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
    <#lt>                       NVMCTRL_CTRLB_SLEEPPRM_${NVMCTRL_CTRLB_POWER_REDUCTION_MODE} | NVMCTRL_CTRLB_RWS(${NVM_RWS}UL)
    <#lt>                       ${(NVMCTRL_WRITE_POLICY == "MANUAL")?then('| NVMCTRL_CTRLB_MANW_Msk', ' ')};</@compress>
}

<#if NVMCTRL_CACHE_ENABLE == true>
    <#lt>void ${NVMCTRL_INSTANCE_NAME}_CacheInvalidate(void)
    <#lt>{
    <#lt>    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_CTRLA = (uint16_t)(NVMCTRL_CTRLA_CMD_INVALL | NVMCTRL_CTRLA_CMDEX_KEY);
    <#lt>}
</#if>
<#if FLASH_RWWEEPROM_START_ADDRESS??>
bool ${NVMCTRL_INSTANCE_NAME}_RWWEEPROM_Read( uint32_t *data, uint32_t length, const uint32_t address )
{
    uint32_t *paddress = (uint32_t*)address;
    (void)memcpy(data, paddress, length);
    return true;
}

bool ${NVMCTRL_INSTANCE_NAME}_RWWEEPROM_PageWrite ( uint32_t *data, const uint32_t address )
{
    uint32_t i = 0U;
    uint32_t * paddress = (uint32_t *)address;

    /* Writing 32-bit words in the given address */
    for ( i = 0U; i < (${NVMCTRL_INSTANCE_NAME}_RWWEEPROM_PAGESIZE/4U); i++)
    {
        *paddress = *(data + i);
        paddress++;
    }

<#if NVMCTRL_WRITE_POLICY == "MANUAL">
     /* Set address and command */
    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_ADDR = address >> 1U;

    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_CTRLA = (uint16_t)(NVMCTRL_CTRLA_CMD_RWWEEWP | NVMCTRL_CTRLA_CMDEX_KEY);
</#if>

<#if INTERRUPT_ENABLE == true>
    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_INTENSET = NVMCTRL_INTENSET_READY_Msk;
</#if>
    return true;
}

bool ${NVMCTRL_INSTANCE_NAME}_RWWEEPROM_RowErase( uint32_t address )
{
     /* Set address and command */
    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_ADDR = address >> 1U;

    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_CTRLA = (uint16_t)(NVMCTRL_CTRLA_CMD_RWWEEER | NVMCTRL_CTRLA_CMDEX_KEY);

<#if INTERRUPT_ENABLE == true>
    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_INTENSET = NVMCTRL_INTENSET_READY_Msk;
</#if>
    return true;
}
</#if>
bool ${NVMCTRL_INSTANCE_NAME}_Read( uint32_t *data, uint32_t length, const uint32_t address )
{
    uint32_t *paddress = (uint32_t*)address;
    (void)memcpy(data, paddress, length);
    return true;
}

<#if NVMCTRL_WRITE_POLICY == "MANUAL">
bool ${NVMCTRL_INSTANCE_NAME}_PageBufferWrite( uint32_t *data, const uint32_t address)
{
    uint32_t i = 0U;
    uint32_t * paddress = (uint32_t *)address;

    /* writing 32-bit data into the given address */
    for (i = 0U; i < (${NVMCTRL_INSTANCE_NAME}_FLASH_PAGESIZE/4U); i++)
    {
        *paddress = *(data + i);
        paddress++;
    }

    return true;
}

bool ${NVMCTRL_INSTANCE_NAME}_PageBufferCommit( const uint32_t address)
{
    uint16_t command = NVMCTRL_CTRLA_CMD_WP_Val;

    /* Set address and command */
    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_ADDR = address >> 1U;

<#if FLASH_RWWEEPROM_START_ADDRESS?? >
    if (address >= ${NVMCTRL_INSTANCE_NAME}_RWWEEPROM_START_ADDRESS)
    {
        command = NVMCTRL_CTRLA_CMD_RWWEEWP;
    }
</#if>

    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_CTRLA = (uint16_t)(command | NVMCTRL_CTRLA_CMDEX_KEY);

<#if INTERRUPT_ENABLE == true>
    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_INTENSET = NVMCTRL_INTENSET_READY_Msk;
</#if>

    return true;
}
</#if>

bool ${NVMCTRL_INSTANCE_NAME}_PageWrite( uint32_t *data, const uint32_t address )
{
    uint32_t i = 0U;
    uint32_t * paddress = (uint32_t *)address;

    /* writing 32-bit data into the given address */
    for (i = 0U; i < (${NVMCTRL_INSTANCE_NAME}_FLASH_PAGESIZE/4U); i++)
    {
        *paddress = *(data + i);
        paddress++;
    }

<#if NVMCTRL_WRITE_POLICY == "MANUAL">
     /* Set address and command */
    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_ADDR = address >> 1U;

    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_CTRLA = (uint16_t)(NVMCTRL_CTRLA_CMD_WP_Val | NVMCTRL_CTRLA_CMDEX_KEY);
</#if>

<#if INTERRUPT_ENABLE == true>
    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_INTENSET = NVMCTRL_INTENSET_READY_Msk;
</#if>
    return true;
}

bool ${NVMCTRL_INSTANCE_NAME}_RowErase( uint32_t address )
{
    /* Set address and command */
    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_ADDR = address >> 1U;

    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_CTRLA = (uint16_t)(NVMCTRL_CTRLA_CMD_ER_Val | NVMCTRL_CTRLA_CMDEX_KEY);

<#if INTERRUPT_ENABLE == true>
    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_INTENSET = NVMCTRL_INTENSET_READY_Msk;
</#if>
    return true;
}

<#if FLASH_USERROW_START_ADDRESS??>
    <#lt>bool ${USER_ROW_WRITE_API_NAME}( uint32_t *data, const uint32_t address )
    <#lt>{
    <#lt>    uint32_t i = 0U;
    <#lt>    uint32_t * paddress = (uint32_t *)address;
    <#lt>    bool pagewrite_val = false;

    <#lt>    if ((address >= ${NVMCTRL_INSTANCE_NAME}_USERROW_START_ADDRESS) && (address <= ((${NVMCTRL_INSTANCE_NAME}_USERROW_START_ADDRESS + ${NVMCTRL_INSTANCE_NAME}_USERROW_SIZE) - ${NVMCTRL_INSTANCE_NAME}_USERROW_PAGESIZE)))
    <#lt>    {
    <#lt>        /* writing 32-bit data into the given address */
    <#lt>        for (i = 0U; i < (${NVMCTRL_INSTANCE_NAME}_USERROW_PAGESIZE/4U); i++)
    <#lt>        {
    <#lt>            *paddress = data[i];
                      paddress++;
    <#lt>        }

    <#lt>        /* Set address and command */
    <#lt>        ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_ADDR = address >> 1U;

    <#lt>        ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_CTRLA = NVMCTRL_CTRLA_CMD_WAP_Val | NVMCTRL_CTRLA_CMDEX_KEY;

    <#if INTERRUPT_ENABLE == true>
        <#lt>        ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_INTENSET = NVMCTRL_INTENSET_READY_Msk;
    </#if>

    <#lt>        pagewrite_val = true;
    <#lt>    }

    <#lt>    return pagewrite_val;
    <#lt>}

    <#lt>bool ${USER_ROW_ERASE_API_NAME}( uint32_t address )
    <#lt>{
    <#lt>     bool rowerase = false;
    <#lt>    if ((address >= ${NVMCTRL_INSTANCE_NAME}_USERROW_START_ADDRESS) && (address <= (${NVMCTRL_INSTANCE_NAME}_USERROW_START_ADDRESS + ${NVMCTRL_INSTANCE_NAME}_USERROW_SIZE)))
    <#lt>    {
    <#lt>        /* Set address and command */
    <#lt>        ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_ADDR = address >> 1U;

    <#lt>        ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_CTRLA = NVMCTRL_CTRLA_CMD_EAR_Val | NVMCTRL_CTRLA_CMDEX_KEY;

    <#if INTERRUPT_ENABLE == true>
        <#lt>        ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_INTENSET = NVMCTRL_INTENSET_READY_Msk;
    </#if>

    <#lt>        rowerase = true;
    <#lt>    }

    <#lt>    return rowerase;
    <#lt>}
</#if>

NVMCTRL_ERROR ${NVMCTRL_INSTANCE_NAME}_ErrorGet( void )
{
    uint16_t nvm_error = 0;

    /* Get the error bits set */
    nvm_error = (${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_STATUS & (NVMCTRL_STATUS_NVME_Msk | NVMCTRL_STATUS_LOCKE_Msk | NVMCTRL_STATUS_PROGE_Msk));

    /* Clear the error bits in both STATUS and INTFLAG register */
    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_STATUS |= nvm_error;

    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_INTFLAG = NVMCTRL_INTFLAG_ERROR_Msk;

    return ((NVMCTRL_ERROR) nvm_error);
}

bool ${NVMCTRL_INSTANCE_NAME}_IsBusy(void)
{
    return ((${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_INTFLAG & NVMCTRL_INTFLAG_READY_Msk)!= NVMCTRL_INTFLAG_READY_Msk);
}

void ${NVMCTRL_INSTANCE_NAME}_RegionLock(uint32_t address)
{
    /* Set address and command */
    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_ADDR = address >> 1U;

    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_CTRLA = (uint16_t)(NVMCTRL_CTRLA_CMD_LR_Val | NVMCTRL_CTRLA_CMDEX_KEY);
}

void ${NVMCTRL_INSTANCE_NAME}_RegionUnlock(uint32_t address)
{
    /* Set address and command */
    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_ADDR = address >> 1U;

    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_CTRLA = (uint16_t)(NVMCTRL_CTRLA_CMD_UR_Val | NVMCTRL_CTRLA_CMDEX_KEY);
}

void ${NVMCTRL_INSTANCE_NAME}_SecurityBitSet(void)
{
    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_CTRLA = (uint16_t)(NVMCTRL_CTRLA_CMD_SSB_Val | NVMCTRL_CTRLA_CMDEX_KEY);
}
