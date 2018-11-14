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

#include "device.h"
#include "plib_${EVSYS_INSTANCE_NAME?lower_case}.h"

<#if EVSYS_INTERRUPT_MODE0 || EVSYS_INTERRUPT_MODE1 || EVSYS_INTERRUPT_MODE2 || EVSYS_INTERRUPT_MODE3 || EVSYS_INTERRUPT_MODE_OTHER>
	<#lt>EVSYS_OBJECT evsys;
</#if>

void ${EVSYS_INSTANCE_NAME}_Initialize( void )
{
<#if EVSYS_CHANNEL_SCHEDULING == "1">
    ${EVSYS_INSTANCE_NAME}_REGS->EVSYS_PRICTRL = EVSYS_PRICTRL_RREN_Msk;
</#if>
<#assign TOTAL_CHANNEL = EVSYS_CHANNEL_NUMBER?number >
<#assign TOTAL_USER = EVSYS_USER_NUMBER?number >
	/*Event Channel User Configuration*/
<#list 0..TOTAL_USER as i>
	<#assign CHANNEL = "EVSYS_USER_" + i >
	<#if .vars[CHANNEL]?has_content>
	<#if .vars[CHANNEL] != '0'>
	${EVSYS_INSTANCE_NAME}_REGS->EVSYS_USER[${i}] = EVSYS_USER_CHANNEL(${.vars[CHANNEL]});
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
    <#if i < NUM_SYNC_CHANNELS>
        <#assign EVD = "EVSYS_CHANNEL_" + i + "_EVENT">
        <#assign OVERRUN = "EVSYS_CHANNEL_" + i + "_OVERRUN">
    </#if>
	<#if .vars[CHANNEL_ENABLE]?has_content>
	<#if (.vars[CHANNEL_ENABLE] != false)>
	/* Event Channel ${i} Configuration */
	${EVSYS_INSTANCE_NAME}_REGS->CHANNEL[${i}].EVSYS_CHANNEL = EVSYS_CHANNEL_EVGEN(${.vars[GENERATOR]}) | EVSYS_CHANNEL_PATH(${.vars[PATH]}) | EVSYS_CHANNEL_EDGSEL(${.vars[EDGE]}) \
									${(.vars[RUNSTANDBY])?then('| EVSYS_CHANNEL_RUNSTDBY_Msk', '')} ${(.vars[ONDEMAND])?then('| EVSYS_CHANNEL_ONDEMAND_Msk', '')};
    <#if .vars[PATH] != '2' >
    <#if (.vars[EVD] || .vars[OVERRUN])>
    <#if .vars[EVD]>
    ${EVSYS_INSTANCE_NAME}_REGS->CHANNEL[${i}].EVSYS_CHINTENSET = EVSYS_CHINTENSET_EVD_Msk ${(.vars[OVERRUN])?then('| EVSYS_CHINTENSET_OVR_Msk', '')};
    <#else>
    ${EVSYS_INSTANCE_NAME}_REGS->CHANNEL[${i}].EVSYS_CHINTENSET = EVSYS_CHINTENSET_OVR_Msk;
    </#if>
    </#if>
	</#if>
	</#if>
	</#if>
</#list>
}

<#if EVSYS_INTERRUPT_MODE0 || EVSYS_INTERRUPT_MODE1 || EVSYS_INTERRUPT_MODE2 || EVSYS_INTERRUPT_MODE3 || EVSYS_INTERRUPT_MODE_OTHER>

	<#lt>void ${EVSYS_INSTANCE_NAME}_InterruptEnable(EVSYS_CHANNEL channel, EVSYS_INT_MASK interrupt)
	<#lt>{
	<#lt>	${EVSYS_INSTANCE_NAME}_REGS->CHANNEL[channel].EVSYS_CHINTENSET = interrupt;
	<#lt>}

	<#lt>void ${EVSYS_INSTANCE_NAME}_InterruptDisable(EVSYS_CHANNEL channel, EVSYS_INT_MASK interrupt)
	<#lt>{
	<#lt>	${EVSYS_INSTANCE_NAME}_REGS->CHANNEL[channel].EVSYS_CHINTENCLR = interrupt;
	<#lt>}

	<#lt>void ${EVSYS_INSTANCE_NAME}_CallbackRegister( EVSYS_CALLBACK callback, uintptr_t context )
	<#lt>{
	<#lt>	evsys.callback = callback;
	<#lt>	evsys.context = context;
	<#lt>}
</#if>
<#list 0..3 as x>
<#assign INTERRUPT_MODE = "EVSYS_INTERRUPT_MODE" + x>
<#if .vars[INTERRUPT_MODE]>
	<#lt>void ${EVSYS_INSTANCE_NAME}_${x}_InterruptHandler( void )
	<#lt>{
	<#lt>	volatile uint32_t status = ${EVSYS_INSTANCE_NAME}_REGS->CHANNEL[${x}].EVSYS_CHINTFLAG;
	<#lt>	${EVSYS_INSTANCE_NAME}_REGS->CHANNEL[${x}].EVSYS_CHINTFLAG = EVSYS_CHINTFLAG_Msk;
	<#lt>	if(evsys.callback != NULL)
    <#lt>   {
    <#lt>   	evsys.callback(evsys.context, ${x}, status);
    <#lt>   }
	<#lt>}
</#if>
</#list>

<#if EVSYS_INTERRUPT_MODE_OTHER>
void ${EVSYS_INSTANCE_NAME}_OTHER_InterruptHandler( void )
{
    uint8_t channel = ${EVSYS_INSTANCE_NAME}_REGS->EVSYS_INTPEND & EVSYS_INTPEND_ID_Msk;
    volatile uint32_t status = ${EVSYS_INSTANCE_NAME}_REGS->CHANNEL[channel].EVSYS_CHINTFLAG;
    ${EVSYS_INSTANCE_NAME}_REGS->CHANNEL[channel].EVSYS_CHINTFLAG = EVSYS_CHINTFLAG_Msk;
    if(evsys.callback != NULL)
    {
    	evsys.callback(evsys.context, channel, status);
    }
}
</#if>
