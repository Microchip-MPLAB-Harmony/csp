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

static volatile uint16_t nvm_error;
static uint16_t nvm_status;
static uint32_t smart_eep_status;

<#assign NVMCTRL_CTRLA_VAL = "">
<#assign NVMCTRL_SEECFG_VAL = "">
<#assign NVMCTRL_INTENSET_VAL = "">
<#if NVMCTRL_CTRLA_POWER_REDUCTION_MODE?has_content >
    <#if NVMCTRL_CTRLA_POWER_REDUCTION_MODE != "0" >
        <#if NVMCTRL_CTRLA_VAL != "">
            <#assign NVMCTRL_CTRLA_VAL = NVMCTRL_CTRLA_VAL + "| NVMCTRL_CTRLA_PRM("+NVMCTRL_CTRLA_POWER_REDUCTION_MODE+")">
        <#else>
            <#assign NVMCTRL_CTRLA_VAL = "NVMCTRL_CTRLA_PRM("+NVMCTRL_CTRLA_POWER_REDUCTION_MODE+")">
        </#if>
    </#if>
</#if>
<#if NVMCTRL_AHB0_CACHE_DISABLE == true>
    <#if NVMCTRL_CTRLA_VAL != "">
        <#assign NVMCTRL_CTRLA_VAL = NVMCTRL_CTRLA_VAL + " | NVMCTRL_CTRLA_CACHEDIS0_Msk">
    <#else>
        <#assign NVMCTRL_CTRLA_VAL = "NVMCTRL_CTRLA_CACHEDIS0_Msk">
    </#if>
</#if>
<#if NVMCTRL_AHB1_CACHE_DISABLE == true>
    <#if NVMCTRL_CTRLA_VAL != "">
        <#assign NVMCTRL_CTRLA_VAL = NVMCTRL_CTRLA_VAL + " | NVMCTRL_CTRLA_CACHEDIS1_Msk">
    <#else>
        <#assign NVMCTRL_CTRLA_VAL = "NVMCTRL_CTRLA_CACHEDIS1_Msk">
    </#if>
</#if>
<#if NVM_WMODE_ENABLE == true>
    <#if NVMCTRL_SEECFG_VAL != "">
        <#assign NVMCTRL_SEECFG_VAL = NVMCTRL_SEECFG_VAL + " | NVMCTRL_SEECFG_WMODE_Msk">
    <#else>
        <#assign NVMCTRL_SEECFG_VAL = "NVMCTRL_SEECFG_WMODE_Msk">
    </#if>
</#if>
<#if NVM_APRDIS_ENABLE == true>
    <#if NVMCTRL_SEECFG_VAL != "">
        <#assign NVMCTRL_SEECFG_VAL = NVMCTRL_SEECFG_VAL + " | NVMCTRL_SEECFG_APRDIS_Msk">
    <#else>
        <#assign NVMCTRL_SEECFG_VAL = "NVMCTRL_SEECFG_APRDIS_Msk">
    </#if>
</#if>
<#if INTERRUPT_ENABLE == true>
    <#if NVMCTRL_INTENSET_VAL != "">
        <#assign NVMCTRL_INTENSET_VAL = NVMCTRL_INTENSET_VAL + " | NVMCTRL_INTENSET_DONE_Msk">
    <#else>
        <#assign NVMCTRL_INTENSET_VAL = "NVMCTRL_INTENSET_DONE_Msk">
    </#if>
</#if>
<#if NVM_INTERRUPT1_ENABLE == true>
    <#if NVMCTRL_INTENSET_VAL != "">
        <#assign NVMCTRL_INTENSET_VAL = NVMCTRL_INTENSET_VAL + " | NVMCTRL_INTENSET_SEESFULL_Msk">
    <#else>
        <#assign NVMCTRL_INTENSET_VAL = "NVMCTRL_INTENSET_SEESFULL_Msk">
    </#if>
</#if>
// *****************************************************************************
// *****************************************************************************
// Section: ${NVMCTRL_INSTANCE_NAME} Implementation
// *****************************************************************************
// *****************************************************************************

<#if INTERRUPT_ENABLE == true >
    <#lt>NVMCTRL_CALLBACK_OBJECT ${NVMCTRL_INSTANCE_NAME?lower_case}CallbackObjMain;
</#if>

<#if NVM_INTERRUPT1_ENABLE == true >
    <#lt>NVMCTRL_CALLBACK_OBJECT ${NVMCTRL_INSTANCE_NAME?lower_case}CallbackObjSmartEE;
</#if>

void ${NVMCTRL_INSTANCE_NAME}_Initialize(void)
{
<#if NVMCTRL_AUTOWS_ENABLE != true>
    <#if NVMCTRL_CTRLA_VAL?has_content >
        <#lt>   ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_CTRLA = ${NVMCTRL_CTRLA_VAL} | NVMCTRL_CTRLA_RWS(${NVM_RWS});
    <#else>
        <#lt>   ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_CTRLA = NVMCTRL_CTRLA_RWS(${NVM_RWS});
    </#if>
<#else>
    <#if NVMCTRL_CTRLA_VAL?has_content >
    <#lt>   ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_CTRLA = ${NVMCTRL_CTRLA_VAL} | NVMCTRL_CTRLA_RWS(${NVM_RWS}) | NVMCTRL_CTRLA_AUTOWS_Msk;
    <#else>
    <#lt>   ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_CTRLA = NVMCTRL_CTRLA_RWS(${NVM_RWS}) | NVMCTRL_CTRLA_AUTOWS_Msk;    
    </#if>
</#if>
<#if NVMCTRL_SEECFG_VAL?has_content >
    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_SEECFG = ${NVMCTRL_SEECFG_VAL};
</#if>
<#if INTERRUPT_ENABLE == true || NVM_INTERRUPT1_ENABLE == true >
    /* Clear all interrupt flags */
    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_INTFLAG = NVMCTRL_INTFLAG_Msk;
</#if>
<#if NVMCTRL_INTENSET_VAL?has_content >
    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_INTENSET = ${NVMCTRL_INTENSET_VAL};
</#if>
}

bool ${NVMCTRL_INSTANCE_NAME}_Read( uint32_t *data, uint32_t length, const uint32_t address )
{
    memcpy((void *)data, (void *)address, length);
    
    return true;
}

void ${NVMCTRL_INSTANCE_NAME}_SetWriteMode(NVMCTRL_WRITEMODE mode)
{
    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_CTRLA = (${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_CTRLA & (~NVMCTRL_CTRLA_WMODE_Msk)) | mode;
}

bool ${NVMCTRL_INSTANCE_NAME}_QuadWordWrite(uint32_t *data, const uint32_t address)
{
    uint8_t i = 0;
    bool wr_status = false;
    uint32_t * paddress = (uint32_t *)address;
    uint32_t wr_mode = (${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_CTRLA & NVMCTRL_CTRLA_WMODE_Msk); 

    /* Clear global error flag */
    nvm_error = 0;

    /* If the address is not a quad word address, return error */
    if((address & 0x03) != 0)
    {
        wr_status = false;
    }
    else
    {
        /* Configure Quad Word Write */
        ${NVMCTRL_INSTANCE_NAME}_SetWriteMode(NVMCTRL_CTRLA_WMODE_AQW);

        /* Writing 32-bit data into the given address.  Writes to the page buffer must be 32 bits. */
        for (i = 0; i <= 3; i++)
        {
            *paddress++ = data[i];
        }
        /* Restore the write mode */
        ${NVMCTRL_INSTANCE_NAME}_SetWriteMode(wr_mode);
        wr_status = true;
    }
    return wr_status;
}

bool ${NVMCTRL_INSTANCE_NAME}_DoubleWordWrite(uint32_t *data, const uint32_t address)
{
    uint8_t i = 0;
    bool wr_status = false;
    uint32_t * paddress = (uint32_t *)address;
    uint32_t wr_mode = (${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_CTRLA & NVMCTRL_CTRLA_WMODE_Msk); 

    /* Clear global error flag */
    nvm_error = 0;

    /* If the address is not a double word address, return error */
    if((address & 0x01) != 0)
    {
        wr_status = false;
    }
    else
    {
        /* Configure Double Word Write */
        ${NVMCTRL_INSTANCE_NAME}_SetWriteMode(NVMCTRL_CTRLA_WMODE_ADW);

        /* Writing 32-bit data into the given address.  Writes to the page buffer must be 32 bits. */
        for (i = 0; i <= 1; i++)
        {
            *paddress++ = data[i];
        }
        /* Restore the write mode */
        ${NVMCTRL_INSTANCE_NAME}_SetWriteMode(wr_mode);
        wr_status = true;
    }
    return wr_status;
}

/* This function assumes that the page written is fresh or it is erased by
 * calling ${NVMCTRL_INSTANCE_NAME}_BlockErase
 */
bool ${NVMCTRL_INSTANCE_NAME}_PageWrite( uint32_t *data, const uint32_t address )
{
    uint32_t i = 0;
    uint32_t * paddress = (uint32_t *)address;

    /* Clear global error flag */
    nvm_error = 0;

    /* writing 32-bit data into the given address.  Writes to the page buffer must be 32 bits */
    for (i = 0; i < (${NVMCTRL_INSTANCE_NAME}_FLASH_PAGESIZE/4); i++)
    {
        *paddress++ = data[i];
    }

    /* If write mode is manual, */
    if ((${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_CTRLA & NVMCTRL_CTRLA_WMODE_MAN) == NVMCTRL_CTRLA_WMODE_MAN)
    {
        /* Set address and command */
        ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_CTRLB = NVMCTRL_CTRLB_CMD_WP | NVMCTRL_CTRLB_CMDEX_KEY;
    }
    
    return true;
}

bool ${NVMCTRL_INSTANCE_NAME}_BlockErase( uint32_t address )
{
    /* Clear global error flag */
    nvm_error = 0;

    /* Set address and command */
    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_ADDR = address;
    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_CTRLB = NVMCTRL_CTRLB_CMD_EB | NVMCTRL_CTRLB_CMDEX_KEY;
    
    return true;
}

uint16_t ${NVMCTRL_INSTANCE_NAME}_ErrorGet( void )
{
    nvm_error |= ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_INTFLAG;

    return nvm_error;
}

uint16_t ${NVMCTRL_INSTANCE_NAME}_StatusGet( void )
{
    nvm_status = ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_STATUS;
    
    return nvm_status;
}

bool ${NVMCTRL_INSTANCE_NAME}_IsBusy(void)
{
    return (bool)(!(${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_STATUS & NVMCTRL_STATUS_READY_Msk));
}

void ${NVMCTRL_INSTANCE_NAME}_RegionLock(uint32_t address)
{
    /* Set address and command */
    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_ADDR = address;

    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_CTRLB = NVMCTRL_CTRLB_CMD_LR | NVMCTRL_CTRLB_CMDEX_KEY;
}

void ${NVMCTRL_INSTANCE_NAME}_RegionUnlock(uint32_t address)
{
    /* Set address and command */
    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_ADDR = address;

    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_CTRLB = NVMCTRL_CTRLB_CMD_UR | NVMCTRL_CTRLB_CMDEX_KEY;
}

uint32_t ${NVMCTRL_INSTANCE_NAME}_RegionLockStatusGet (void)
{
    return (${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_RUNLOCK);
}

bool ${NVMCTRL_INSTANCE_NAME}_SmartEEPROM_IsBusy(void)
{
    return (bool)(${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_SEESTAT & NVMCTRL_SEESTAT_BUSY_Msk);
}

uint32_t ${NVMCTRL_INSTANCE_NAME}_SmartEEPROMStatusGet( void )
{
    smart_eep_status = ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_SEESTAT;
    
    return smart_eep_status;
}

bool ${NVMCTRL_INSTANCE_NAME}_SmartEEPROM_IsActiveSectorFull(void)
{
    return (bool)(${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_INTFLAG & NVMCTRL_INTFLAG_SEESFULL_Msk);
}

/* Use BankSwap only when there are valid applications in both NVM Banks */
void ${NVMCTRL_INSTANCE_NAME}_BankSwap(void)
{
    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_CTRLB = NVMCTRL_CTRLB_CMD_BKSWRST | NVMCTRL_CTRLB_CMDEX_KEY;
}

void ${NVMCTRL_INSTANCE_NAME}_SmartEEPROMSectorReallocate(void)
{
    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_CTRLB = NVMCTRL_CTRLB_CMD_SEERALOC | NVMCTRL_CTRLB_CMDEX_KEY;
}

void ${NVMCTRL_INSTANCE_NAME}_SmartEEPROMFlushPageBuffer(void)
{
    /* Clear global error flag */
    nvm_error = 0;

    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_CTRLB = NVMCTRL_CTRLB_CMD_SEEFLUSH | NVMCTRL_CTRLB_CMDEX_KEY;
}
<#if INTERRUPT_ENABLE == true >

void ${NVMCTRL_INSTANCE_NAME}_EnableMainFlashInterruptSource(NVMCTRL_INTERRUPT0_SOURCE int_source)
{
    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_INTENSET |= int_source;
}

void ${NVMCTRL_INSTANCE_NAME}_DisableMainFlashInterruptSource(NVMCTRL_INTERRUPT0_SOURCE int_source)
{
    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_INTENCLR |= int_source;
}
</#if>
<#if NVM_INTERRUPT1_ENABLE == true >

void ${NVMCTRL_INSTANCE_NAME}_EnableSmartEEPROMInterruptSource(NVMCTRL_INTERRUPT1_SOURCE int_source)
{
    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_INTENSET |= int_source;
}

void ${NVMCTRL_INSTANCE_NAME}_DisableSmartEEPROMInterruptSource(NVMCTRL_INTERRUPT1_SOURCE int_source)
{
    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_INTENCLR |= int_source;
}
</#if>

<#if INTERRUPT_ENABLE == true >
    <#lt>void ${NVMCTRL_INSTANCE_NAME}_CallbackRegister( NVMCTRL_CALLBACK callback, uintptr_t context )
    <#lt>{
    <#lt>    /* Register callback function */
    <#lt>    ${NVMCTRL_INSTANCE_NAME?lower_case}CallbackObjMain.callback_fn = callback;
    <#lt>    ${NVMCTRL_INSTANCE_NAME?lower_case}CallbackObjMain.context = context;
    <#lt>}
    <#lt>void ${NVMCTRL_INSTANCE_NAME}_Main_Interrupt_Handler(void)
    <#lt>{
    <#lt>    /* Store previous and current error flags */
    <#lt>    nvm_error |= ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_INTFLAG;

    <#lt>    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_INTFLAG = ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_INTFLAG;

    <#lt>    if(${NVMCTRL_INSTANCE_NAME?lower_case}CallbackObjMain.callback_fn != NULL)
    <#lt>    {
    <#lt>        ${NVMCTRL_INSTANCE_NAME?lower_case}CallbackObjMain.callback_fn(${NVMCTRL_INSTANCE_NAME?lower_case}CallbackObjMain.context);
    <#lt>    }
    <#lt>}
</#if>

<#if NVM_INTERRUPT1_ENABLE == true >
    <#lt>void ${NVMCTRL_INSTANCE_NAME}_SmartEEPROMCallbackRegister( NVMCTRL_CALLBACK callback, uintptr_t context )
    <#lt>{
    <#lt>    /* Register callback function */
    <#lt>    ${NVMCTRL_INSTANCE_NAME?lower_case}CallbackObjSmartEE.callback_fn = callback;
    <#lt>    ${NVMCTRL_INSTANCE_NAME?lower_case}CallbackObjSmartEE.context = context;
    <#lt>}
    <#lt>void ${NVMCTRL_INSTANCE_NAME}_SmartEEPROM_Interrupt_Handler(void)
    <#lt>{
    <#lt>    /* Store previous and current error flags */
    <#lt>    nvm_error |= ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_INTFLAG;

    <#lt>    ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_INTFLAG = ${NVMCTRL_INSTANCE_NAME}_REGS->NVMCTRL_INTFLAG;

    <#lt>    if(${NVMCTRL_INSTANCE_NAME?lower_case}CallbackObjSmartEE.callback_fn != NULL)
    <#lt>    {
    <#lt>        ${NVMCTRL_INSTANCE_NAME?lower_case}CallbackObjSmartEE.callback_fn(${NVMCTRL_INSTANCE_NAME?lower_case}CallbackObjSmartEE.context);
    <#lt>    }
    <#lt>}
</#if>
