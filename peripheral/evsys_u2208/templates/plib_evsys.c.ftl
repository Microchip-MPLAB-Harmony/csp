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

<#assign TOTAL_CHANNEL = EVSYS_CHANNEL_NUMBER?number >
<#assign CONFIGURED_CHANNEL = 0>
<#if EVSYS_INTERRUPT_MODE == true>
    <#list 0..TOTAL_CHANNEL as i>
        <#assign EVSYS_CHANNEL_ENABLE = "EVSYS_CHANNEL_" + i >
        <#if .vars[EVSYS_CHANNEL_ENABLE]?has_content>
            <#if .vars[EVSYS_CHANNEL_ENABLE] == true>
                <#assign CONFIGURED_CHANNEL = i + 1>
            </#if>
        </#if>
    </#list>
    <#if CONFIGURED_CHANNEL != 0>
        <#lt>static EVSYS_OBJECT evsys[${CONFIGURED_CHANNEL}];
    </#if>
</#if>

void ${EVSYS_INSTANCE_NAME}_Initialize( void )
{<#if EVSYS_CHANNEL_ONDEMAND>
    ${EVSYS_INSTANCE_NAME}_REGS->EVSYS_CTRL = EVSYS_CTRL_GCLKREQ_Msk;
 </#if>

<#assign TOTAL_USER = EVSYS_USER_NUMBER?number >
    /*Event Channel User Configuration*/
<#list 0..TOTAL_USER as i>
    <#assign CHANNEL = "EVSYS_USER_" + i >
    <#if .vars[CHANNEL]?has_content>
    <#if .vars[CHANNEL] != '0'>
    ${EVSYS_INSTANCE_NAME}_REGS->EVSYS_USER = EVSYS_USER_CHANNEL(${.vars[CHANNEL]}U) | EVSYS_USER_USER(${i}U);
    </#if>
    </#if>
</#list>

<#list 0..TOTAL_CHANNEL as i>
    <#assign CHANNEL_ENABLE = "EVSYS_CHANNEL_" + i >
    <#assign GENERATOR = "EVSYS_CHANNEL_" + i + "_GENERATOR">
    <#assign PATH = "EVSYS_CHANNEL_" + i + "_PATH">
    <#assign EDGE = "EVSYS_CHANNEL_" + i + "_EDGE">
    <#assign ONDEMAND = "EVSYS_CHANNEL_" + i + "_ONDEMAND">
    <#assign RUNSTANDBY = "EVSYS_CHANNEL_" + i + "_RUNSTANDBY">
    <#if .vars[CHANNEL_ENABLE]?has_content>
    <#if (.vars[CHANNEL_ENABLE] != false)>
    /* Event Channel ${i} Configuration */
    ${EVSYS_INSTANCE_NAME}_REGS->EVSYS_CHANNEL = EVSYS_CHANNEL_EVGEN(${.vars[GENERATOR]}U) | EVSYS_CHANNEL_PATH(${.vars[PATH]}U) | EVSYS_CHANNEL_EDGSEL(${.vars[EDGE]}U) \
                                    | EVSYS_CHANNEL_CHANNEL(${i}U);
    </#if>
    </#if>
</#list>

<#if EVSYS_INTERRUPT_MODE>

    /*Interrupt setting for Event System*/
    ${EVSYS_INSTANCE_NAME}_REGS->EVSYS_INTENSET = ${EVSYS_INTERRUPT_VALUE}U;
</#if>
}

<#list 0..EVSYS_CHANNEL_NUMBER as i>
    <#assign CHANNEL_ENABLE = "EVSYS_CHANNEL_" + i >
    <#if .vars[CHANNEL_ENABLE]?has_content && .vars[CHANNEL_ENABLE] != false>
    <#lt>void ${EVSYS_INSTANCE_NAME}_GeneratorEnable(EVSYS_CHANNEL channel, uint8_t generator)
    <#lt>{
    <#lt>   ${EVSYS_INSTANCE_NAME}_REGS->EVSYS_CHANNEL = (${EVSYS_INSTANCE_NAME}_REGS->EVSYS_CHANNEL & (~EVSYS_CHANNEL_EVGEN_Msk | ~EVSYS_CHANNEL_CHANNEL_Msk))
                                                          | EVSYS_CHANNEL_EVGEN((uint32_t)generator) | EVSYS_CHANNEL_CHANNEL((uint32_t)channel);
    <#lt>}

    <#lt>void ${EVSYS_INSTANCE_NAME}_GeneratorDisable(EVSYS_CHANNEL channel)
    <#lt>{
    <#lt>   ${EVSYS_INSTANCE_NAME}_REGS->EVSYS_CHANNEL = (${EVSYS_INSTANCE_NAME}_REGS->EVSYS_CHANNEL & ~EVSYS_CHANNEL_EVGEN_Msk) | EVSYS_CHANNEL_CHANNEL(channel);
    <#lt>}

    <#lt>void ${EVSYS_INSTANCE_NAME}_UserEnable(EVSYS_CHANNEL channel, uint8_t user)
    <#lt>{
    <#lt>   ${EVSYS_INSTANCE_NAME}_REGS->EVSYS_USER = EVSYS_USER_CHANNEL((uint16_t)(channel + 1U)) | EVSYS_USER_USER((uint16_t)user);
    <#lt>}

    <#lt>void ${EVSYS_INSTANCE_NAME}_UserDisable(void)
    <#lt>{
    <#lt>   ${EVSYS_INSTANCE_NAME}_REGS->EVSYS_USER = (${EVSYS_INSTANCE_NAME}_REGS->EVSYS_USER & (uint8_t)~EVSYS_USER_USER_Msk);
    <#lt>}
    <#break>
    </#if>
</#list>

<#if EVSYS_INTERRUPT_MODE == true>

    <#lt>void ${EVSYS_INSTANCE_NAME}_InterruptEnable(EVSYS_CHANNEL channel, EVSYS_INT_MASK interruptMask)
    <#lt>{
    <#lt>   if(channel > 7U)
    <#lt>   {
    <#lt>       channel = channel + 8U;
    <#lt>   }
    <#lt>   ${EVSYS_INSTANCE_NAME}_REGS->EVSYS_INTENSET = (uint32_t)interruptMask << channel;
    <#lt>}

    <#lt>void ${EVSYS_INSTANCE_NAME}_InterruptDisable(EVSYS_CHANNEL channel, EVSYS_INT_MASK interruptMask)
    <#lt>{
    <#lt>   if(channel > 7U)
    <#lt>   {
    <#lt>       channel = channel + 8U;
    <#lt>   }
    <#lt>   ${EVSYS_INSTANCE_NAME}_REGS->EVSYS_INTENCLR = (uint32_t)interruptMask << channel;
    <#lt>}

    <#lt>void ${EVSYS_INSTANCE_NAME}_CallbackRegister(EVSYS_CHANNEL channel, EVSYS_CALLBACK callback, uintptr_t context)
    <#lt>{
    <#lt>   evsys[channel].callback = callback;
    <#lt>   evsys[channel].context = context;
    <#lt>}
</#if>

<#if EVSYS_INTERRUPT_MODE == true>
    <#lt>void ${EVSYS_INSTANCE_NAME}_InterruptHandler( void )
    <#lt>{
         <#lt>    uint8_t currentChannel = 0U;
         <#lt>    uint8_t channel = 0U;
         <#lt>    uint32_t eventIntFlagStatus = 0U;
         <#lt>    uint32_t overrunIntFlagStatus = 0U;

         <#lt>    /* Find any triggered channels, run associated callback handlers */
         <#lt>    for (currentChannel = 0U; currentChannel < ${CONFIGURED_CHANNEL}U; currentChannel++)
         <#lt>    {
<#if CONFIGURED_CHANNEL gt 7 >
         <#lt>        if (currentChannel > 7U)
         <#lt>        {
         <#lt>            channel = currentChannel + 8U;
         <#lt>        }
         <#lt>        else
         <#lt>        {
         <#lt>            channel = currentChannel;
         <#lt>        }
<#else>
         <#lt>        channel = currentChannel;
</#if>
         <#lt>        /* Read the interrupt flag status */
         <#lt>        overrunIntFlagStatus = ${EVSYS_INSTANCE_NAME}_REGS->EVSYS_INTFLAG & ((uint32_t)EVSYS_INT_OVERRUN << channel);
         <#lt>        eventIntFlagStatus = ${EVSYS_INSTANCE_NAME}_REGS->EVSYS_INTFLAG & ((uint32_t)EVSYS_INT_EVENT_DETECT << channel);

         <#lt>        if ((eventIntFlagStatus | overrunIntFlagStatus) != 0U)
         <#lt>        {
         <#lt>            /* Find any associated callback entries in the callback table */
         <#lt>            if (evsys[currentChannel].callback != NULL)
         <#lt>            {
         <#lt>                evsys[currentChannel].callback((uint32_t)((eventIntFlagStatus | overrunIntFlagStatus) >> channel), evsys[currentChannel].context);
         <#lt>            }

         <#lt>            /* Clear interrupt flag */
         <#lt>            ${EVSYS_INSTANCE_NAME}_REGS->EVSYS_INTFLAG = ((uint32_t)EVSYS_INT_OVERRUN | (uint32_t)EVSYS_INT_EVENT_DETECT) << channel;
         <#lt>        }
         <#lt>    }
    <#lt>}
</#if>
