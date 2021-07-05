/*******************************************************************************
  EVSYS Peripheral Library

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${EVSYS_INSTANCE_NAME?lower_case}.c

  Summary:
    EVSYS Source File

  Description:
    None

*******************************************************************************/

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

#include "plib_${EVSYS_INSTANCE_NAME?lower_case}.h"
<#if core.CoreSysIntFile == true>
#include "interrupts.h"
</#if>

<#assign EVSYS_REG_NAME = EVSYS_INSTANCE_NAME>

<#list 0..EVSYS_CHANNEL_NUMBER as i>
<#assign CHANNEL_ENABLE = "EVSYS_CHANNEL_" + i >
<#assign EVSYS_NONSEC = "EVSYS_NONSEC_" + i >
<#if .vars[CHANNEL_ENABLE]?has_content && .vars[CHANNEL_ENABLE] != false>
<#if .vars[EVSYS_NONSEC]?has_content && .vars[EVSYS_NONSEC] == "NON-SECURE">
void ${EVSYS_INSTANCE_NAME}_GeneratorEnable(EVSYS_CHANNEL channel, uint8_t generator)
{
    ${EVSYS_REG_NAME}_REGS->CHANNEL[channel].EVSYS_CHANNEL = (${EVSYS_REG_NAME}_REGS->CHANNEL[channel].EVSYS_CHANNEL & ~EVSYS_CHANNEL_EVGEN_Msk) | EVSYS_CHANNEL_EVGEN(generator);
}

void ${EVSYS_INSTANCE_NAME}_GeneratorDisable(EVSYS_CHANNEL channel)
{
    ${EVSYS_REG_NAME}_REGS->CHANNEL[channel].EVSYS_CHANNEL = (${EVSYS_REG_NAME}_REGS->CHANNEL[channel].EVSYS_CHANNEL & ~EVSYS_CHANNEL_EVGEN_Msk);
}

void ${EVSYS_INSTANCE_NAME}_UserEnable(EVSYS_CHANNEL channel, uint8_t user)
{
    ${EVSYS_REG_NAME}_REGS->EVSYS_USER[user] = EVSYS_USER_CHANNEL((channel + 1));
}

void ${EVSYS_INSTANCE_NAME}_UserDisable(uint8_t user)
{
    ${EVSYS_REG_NAME}_REGS->EVSYS_USER[user] = 0x0;
}
<#break>
</#if>
</#if>
</#list>

<#if INTERRUPT_ACTIVE>
<#assign CONFIGURED_SYNC_CHANNEL = 0>
    <#list 0..NUM_SYNC_CHANNELS as i>
        <#assign EVSYS_CHANNEL_ENABLE = "EVSYS_CHANNEL_" + i >
        <#if .vars[EVSYS_CHANNEL_ENABLE]?has_content>
            <#if .vars[EVSYS_CHANNEL_ENABLE] == true>
                <#assign EVSYS_NONSEC = "EVSYS_NONSEC_" + i >
                <#if .vars[EVSYS_NONSEC]?has_content>
                    <#if .vars[EVSYS_NONSEC] == "NON-SECURE">
                        <#assign CONFIGURED_SYNC_CHANNEL = i + 1>
                    </#if>
                </#if>
            </#if>
        </#if>
    </#list>
    <#if CONFIGURED_SYNC_CHANNEL != 0>
        <#lt>EVSYS_OBJECT evsys[${CONFIGURED_SYNC_CHANNEL}];
    </#if>
</#if>

<#if INTERRUPT_ACTIVE>
<#list 0..NUM_SYNC_CHANNELS as i>
    <#assign EVSYS_NONSEC = "EVSYS_NONSEC_" + i >
    <#if .vars[EVSYS_NONSEC]?has_content>
    <#if .vars[EVSYS_NONSEC] == "NON-SECURE">

    <#lt>void ${EVSYS_INSTANCE_NAME}_InterruptEnable(EVSYS_CHANNEL channel, EVSYS_INT_MASK interruptMask)
    <#lt>{
    <#lt>   ${EVSYS_REG_NAME}_REGS->CHANNEL[channel].EVSYS_CHINTENSET = interruptMask;
    <#lt>}

    <#lt>void ${EVSYS_INSTANCE_NAME}_InterruptDisable(EVSYS_CHANNEL channel, EVSYS_INT_MASK interruptMask)
    <#lt>{
    <#lt>   ${EVSYS_REG_NAME}_REGS->CHANNEL[channel].EVSYS_CHINTENCLR = interruptMask;
    <#lt>}

    <#lt>void ${EVSYS_INSTANCE_NAME}_CallbackRegister(EVSYS_CHANNEL channel, EVSYS_CALLBACK callback, uintptr_t context )
    <#lt>{
    <#lt>   evsys[channel].callback = callback;
    <#lt>   evsys[channel].context = context;
    <#lt>}
    <#break>
    </#if>
    </#if>
</#list>
</#if>
<#list 0..NUM_SYNC_CHANNELS as x>
<#assign INTERRUPT_MODE = "EVSYS_INTERRUPT_MODE" + x>
    <#if .vars[INTERRUPT_MODE]??>
        <#if .vars[INTERRUPT_MODE]>
        <#assign EVSYS_NONSEC = "EVSYS_NONSEC_" + x >
            <#if .vars[EVSYS_NONSEC]?has_content>
                <#if .vars[EVSYS_NONSEC] == "NON-SECURE">
                    <#lt>void ${EVSYS_INSTANCE_NAME}_${x}_InterruptHandler( void )
                    <#lt>{
                    <#lt>   volatile uint32_t status = ${EVSYS_REG_NAME}_REGS->CHANNEL[${x}].EVSYS_CHINTFLAG;
                    <#lt>   ${EVSYS_REG_NAME}_REGS->CHANNEL[${x}].EVSYS_CHINTFLAG = EVSYS_CHINTFLAG_Msk;
                    <#lt>   if(evsys[${x}].callback != NULL)
                    <#lt>   {
                    <#lt>       evsys[${x}].callback(status, evsys[${x}].context);
                    <#lt>   }
                    <#lt>}
                </#if>
            </#if>
        </#if>
    </#if>
</#list>

<#if EVSYS_INTERRUPT_MODE_OTHER??>
<#if EVSYS_INTERRUPT_MODE_OTHER>
void ${EVSYS_INSTANCE_NAME}_OTHER_InterruptHandler( void )
{
    uint8_t channel = ${EVSYS_REG_NAME}_REGS->EVSYS_INTPEND & EVSYS_INTPEND_ID_Msk;
    volatile uint32_t status = ${EVSYS_REG_NAME}_REGS->CHANNEL[channel].EVSYS_CHINTFLAG;
    if(evsys[channel].callback != NULL)
    {
        evsys[channel].callback(status, evsys[channel].context);
    }
    ${EVSYS_REG_NAME}_REGS->CHANNEL[channel].EVSYS_CHINTFLAG = EVSYS_CHINTFLAG_Msk;
}
</#if>
</#if>
