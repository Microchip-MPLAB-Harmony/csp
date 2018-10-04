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
* © 2018 Microchip Technology Inc. and its subsidiaries.
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

    <#lt>uintptr_t ${NVMCTRL_INSTANCE_NAME?lower_case}context;

    <#lt>void ${NVMCTRL_INSTANCE_NAME}_CallbackRegister( NVMCTRL_CALLBACK callback, uintptr_t context )
    <#lt>{
    <#lt>    /* Register callback function */
    <#lt>    ${NVMCTRL_INSTANCE_NAME?lower_case}CallbackFunc = callback;
    <#lt>    ${NVMCTRL_INSTANCE_NAME?lower_case}context = context;
    <#lt>}

    <#lt>void ${NVMCTRL_INSTANCE_NAME}_InterruptHandler(void)
    <#lt>{
    <#lt>    if(( ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_INTFLAG & NVMCTRL_INTFLAG_READY_Msk ) && (${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_INTENSET & NVMCTRL_INTENSET_READY_Msk))
    <#lt>    {
    <#lt>        if(*nvmctrl0CallbackFunc != NULL)
    <#lt>        {
    <#lt>            /* Calling callback func */
    <#lt>            (*nvmctrl0CallbackFunc)(nvmctrl0context);
    <#lt>        }

    <#lt>        /* Clear interrupt */
    <#lt>        ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_INTENCLR = NVMCTRL_INTENCLR_READY_Msk;
    <#lt>    }
    <#lt>}
</#if>

void ${NVMCTRL_INSTANCE_NAME}_Initialize(void)
{
    /* Disable Manual Write */
    <@compress single_line=true>${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_CTRLB = NVMCTRL_CTRLB_READMODE_${NVMCTRL_CTRLB_READMODE_SELECTION}
                                                         | NVMCTRL_CTRLB_SLEEPPRM_${NVMCTRL_CTRLB_POWER_REDUCTION_MODE}
                                                         ${NVMCTRL_CACHE_ENABLE?then('', '| NVMCTRL_CTRLB_CACHEDIS_Msk')};</@compress>

    /* Clear error flags */
    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_STATUS = (0x00U);

<#if INTERRUPT_ENABLE == true>
    /* Clear interrupt flag */
    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_INTENCLR = NVMCTRL_INTENCLR_READY_Msk;
</#if>
}

<#if NVMCTRL_CACHE_ENABLE == true>
    <#lt>void ${NVMCTRL_INSTANCE_NAME}_CacheInvalidate(void)
    <#lt>{
    <#lt>    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_CTRLA = NVMCTRL_CTRLA_CMD_INVALL | NVMCTRL_CTRLA_CMDEX_KEY;
    <#lt>}
</#if>

<#if NVMCTRL_RWW_EEPROM == true>
    <#lt>bool ${NVMCTRL_INSTANCE_NAME}_RWWEEPROM_Read( uint32_t *data, uint32_t length, const uint32_t address )
    <#lt>{
    <#lt>    memcpy((void *)data, (void *)address, length);
    <#lt>    return true;
    <#lt>}

    <#lt>bool ${NVMCTRL_INSTANCE_NAME}_RWWEEPROM_PageWrite ( uint32_t *data, const uint32_t address )
    <#lt>{
    <#lt>    uint32_t i = 0;
    <#lt>    uint32_t * paddress = (uint32_t *)address;

    <#lt>    /* Clear error flags */
    <#lt>    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_STATUS = 0x1C;

    <#lt>    /* Clear global error flag */
    <#lt>    status = 0;

    <#lt>    /* Erase the page buffer before buffering new data */
    <#lt>    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_CTRLA = NVMCTRL_CTRLA_CMD_PBC_Val | NVMCTRL_CTRLA_CMDEX_KEY;

    <#lt>    /* Writing 32-bit words in the given address */
    <#lt>    for ( i = 0; i < (${NVMCTRL_INSTANCE_NAME}_RWWEEPROM_PAGESIZE/4); i++)
    <#lt>    {
    <#lt>        *paddress++ = data[i];
    <#lt>    }

    <#lt><#if INTERRUPT_ENABLE == true>
    <#lt>    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_INTENSET = NVMCTRL_INTENSET_READY_Msk;
    <#lt><#else>
    <#lt>    /* Check if the module is busy */
    <#lt>    while((${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_INTFLAG & NVMCTRL_INTFLAG_READY_Msk) != NVMCTRL_INTFLAG_READY_Msk)
    <#lt>    {
    <#lt>        /* Force-wait for the buffer clear to complete */
    <#lt>    }
    <#lt></#if>

    <#lt>     return true;

    <#lt>}

    <#lt>bool ${NVMCTRL_INSTANCE_NAME}_RWWEEPROM_RowErase( uint32_t address )
    <#lt>{
    <#lt>    /* Clear error flags */
    <#lt>    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_STATUS = 0x1C;

    <#lt>    /* Clear global error flag */
    <#lt>    status = 0;

    <#lt>     /* Set address and command */
    <#lt>    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_ADDR = address >> 1;

    <#lt>    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_CTRLA = NVMCTRL_CTRLA_CMD_RWWEEER | NVMCTRL_CTRLA_CMDEX_KEY;

    <#lt><#if INTERRUPT_ENABLE == true>
    <#lt>    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_INTENSET = NVMCTRL_INTENSET_READY_Msk;
    <#lt><#else>
    <#lt>    /* Check if the module is busy */
    <#lt>    while((${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_INTFLAG & NVMCTRL_INTFLAG_READY_Msk) != NVMCTRL_INTFLAG_READY_Msk)
    <#lt>    {
    <#lt>        /* Force-wait for the buffer clear to complete */
    <#lt>    }
    <#lt></#if>

    <#lt>     return true;

    <#lt>}
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

    /* Clear error flags */
    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_STATUS = 0x1C;

    /* Clear global error flag */
    status = 0;

    /* Erase the page buffer before buffering new data */
    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_CTRLA = NVMCTRL_CTRLA_CMD_PBC_Val | NVMCTRL_CTRLA_CMDEX_KEY;

    /* writing 32-bit data into the given address */
    for (i = 0; i < (${NVMCTRL_INSTANCE_NAME}_FLASH_PAGESIZE/4); i++)
    {
        *paddress++ = data[i];
    }

<#if INTERRUPT_ENABLE == true>
    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_INTENSET = NVMCTRL_INTENSET_READY_Msk;
<#else>
    /* Check if the module is busy */
    while((${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_INTFLAG & NVMCTRL_INTFLAG_READY_Msk) != NVMCTRL_INTFLAG_READY_Msk)
    {
        /* Force-wait for the buffer clear to complete */
    }
</#if>

    return true;
}

bool ${NVMCTRL_INSTANCE_NAME}_RowErase( uint32_t address )
{
    /* Clear error flags */
    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_STATUS = 0x1C;

    /* Clear global error flag */
    status = 0;

    /* Set address and command */
    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_ADDR = address >> 1;

    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_CTRLA = NVMCTRL_CTRLA_CMD_ER_Val | NVMCTRL_CTRLA_CMDEX_KEY;

<#if INTERRUPT_ENABLE == true>
    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_INTENSET = NVMCTRL_INTENSET_READY_Msk;
<#else>
    /* Check if the module is busy */
    while((${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_INTFLAG & NVMCTRL_INTFLAG_READY_Msk) != NVMCTRL_INTFLAG_READY_Msk)
    {
        /* Force-wait for the buffer clear to complete */
    }
</#if>

    return true;
}

NVMCTRL_ERROR ${NVMCTRL_INSTANCE_NAME}_ErrorGet( void )
{
    return (status |= ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_STATUS);
}

bool ${NVMCTRL_INSTANCE_NAME}_IsBusy(void)
{
    return (!(${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_INTFLAG & NVMCTRL_INTFLAG_READY_Msk));
}

<#if NVMCTRL_REGION_LOCK_UNLOCK == true>
    <#lt>void ${NVMCTRL_INSTANCE_NAME}_RegionLock(uint32_t address)
    <#lt>{
    <#lt>    /* Clear error flags */
    <#lt>    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_STATUS = 0x1C;

    <#lt>    /* Clear global error flag */
    <#lt>    status = 0;

    <#lt>    /* Set address and command */
    <#lt>    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_ADDR = address >> 1;

    <#lt>    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_CTRLA = NVMCTRL_CTRLA_CMD_LR_Val | NVMCTRL_CTRLA_CMDEX_KEY;
    <#lt>}

    <#lt>void ${NVMCTRL_INSTANCE_NAME}_RegionUnlock(uint32_t address)
    <#lt>{
    <#lt>    /* Clear error flags */
    <#lt>    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_STATUS = 0x1C;

    <#lt>    /* Clear global error flag */
    <#lt>    status = 0;

    <#lt>    /* Set address and command */
    <#lt>    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_ADDR = address >> 1;

    <#lt>    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_CTRLA = NVMCTRL_CTRLA_CMD_UR_Val | NVMCTRL_CTRLA_CMDEX_KEY;
    <#lt>}
</#if>
