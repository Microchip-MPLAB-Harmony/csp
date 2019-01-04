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

<#assign TOTAL_CHANNEL = EVSYS_CHANNEL_NUMBER?number >
<#if EVSYS_INTERRUPT_MODE == true>
	<#lt>EVSYS_OBJECT evsys[${TOTAL_CHANNEL}];
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
	${EVSYS_INSTANCE_NAME}_REGS->EVSYS_USER = EVSYS_USER_CHANNEL(${.vars[CHANNEL]}) | EVSYS_USER_USER(${i});
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
	${EVSYS_INSTANCE_NAME}_REGS->EVSYS_CHANNEL = EVSYS_CHANNEL_EVGEN(${.vars[GENERATOR]}) | EVSYS_CHANNEL_PATH(${.vars[PATH]}) | EVSYS_CHANNEL_EDGSEL(${.vars[EDGE]}) \
									| EVSYS_CHANNEL_CHANNEL(${i});
	</#if>
	</#if>
</#list>

<#if EVSYS_INTERRUPT_MODE>

	/*Interrupt setting for Event System*/
	${EVSYS_INSTANCE_NAME}_REGS->EVSYS_INTENSET = ${EVSYS_INTERRUPT_VALUE};
</#if>
}

<#if EVSYS_INTERRUPT_MODE == true>

	<#lt>void ${EVSYS_INSTANCE_NAME}_InterruptEnable(EVSYS_CHANNEL channel, EVSYS_INT_MASK interrupt)
	<#lt>{
    <#lt>   if(channel > 7)
    <#lt>   {
    <#lt>       channel = channel + 8;
    <#lt>   }
	<#lt>	${EVSYS_INSTANCE_NAME}_REGS->EVSYS_INTENSET = interrupt << channel;
	<#lt>}

	<#lt>void ${EVSYS_INSTANCE_NAME}_InterruptDisable(EVSYS_CHANNEL channel, EVSYS_INT_MASK interrupt)
	<#lt>{
    <#lt>   if(channel > 7)
    <#lt>   {
    <#lt>       channel = channel + 8;
    <#lt>   }
	<#lt>	${EVSYS_INSTANCE_NAME}_REGS->EVSYS_INTENCLR = interrupt << channel;
	<#lt>}

	<#lt>void ${EVSYS_INSTANCE_NAME}_CallbackRegister(EVSYS_CHANNEL channel, EVSYS_CALLBACK callback, uintptr_t context)
	<#lt>{
	<#lt>	evsys[channel].callback = callback;
	<#lt>	evsys[channel].context = context;
	<#lt>}
</#if>

<#if EVSYS_INTERRUPT_MODE == true>
	<#lt>void ${EVSYS_INSTANCE_NAME}_InterruptHandler( void )
	<#lt>{
         <#lt>    uint8_t currentChannel = 0;
         <#lt>    uint8_t channel = 0;
         <#lt>    uint32_t eventIntFlagStatus = 0;
         <#lt>    uint32_t overrunIntFlagStatus = 0;

         <#lt>    /* Find any triggered channels, run associated callback handlers */
         <#lt>    for (currentChannel = 0; currentChannel < ${TOTAL_CHANNEL}; currentChannel++)
         <#lt>    {
         <#lt>        if (currentChannel > 7)
         <#lt>        {
         <#lt>            channel = currentChannel + 8;
         <#lt>        }
         <#lt>        else
         <#lt>        {
         <#lt>            channel = currentChannel;
         <#lt>        }

         <#lt>        /* Read the interrupt flag status */
         <#lt>        overrunIntFlagStatus = ${EVSYS_INSTANCE_NAME}_REGS->EVSYS_INTFLAG & (EVSYS_INT_OVERRUN << channel);
         <#lt>        eventIntFlagStatus = ${EVSYS_INSTANCE_NAME}_REGS->EVSYS_INTFLAG & (EVSYS_INT_EVENT_DETECT << channel);

         <#lt>        if (eventIntFlagStatus | overrunIntFlagStatus)
         <#lt>        {
         <#lt>            /* Find any associated callback entries in the callback table */
         <#lt>            if (evsys[currentChannel].callback != NULL)
         <#lt>            {
         <#lt>                evsys[currentChannel].callback((uint32_t)((eventIntFlagStatus | overrunIntFlagStatus) >> channel), evsys[currentChannel].context);
         <#lt>            }

         <#lt>            /* Clear interrupt flag */
         <#lt>            ${EVSYS_INSTANCE_NAME}_REGS->EVSYS_INTFLAG = (EVSYS_INT_OVERRUN | EVSYS_INT_EVENT_DETECT) << channel;
         <#lt>        }
         <#lt>    }
	<#lt>}
</#if>
