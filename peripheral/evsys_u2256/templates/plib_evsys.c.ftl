/*******************************************************************************
  EVSYS Peripheral Library

  Company:
    Microchip Technology Inc.

  File Name:
    plib_evsys.c

  Summary:
    EVSYS Source File

  Description:
    None

*******************************************************************************/

/*******************************************************************************
Copyright (c) 2017 released Microchip Technology Inc.  All rights reserved.

Microchip licenses to you the right to use, modify, copy and distribute
Software only when embedded on a Microchip microcontroller or digital signal
controller that is integrated into your product or third party product
(pursuant to the sublicense terms in the accompanying license agreement).

You should refer to the license agreement accompanying this Software for
additional information regarding your rights and obligations.

SOFTWARE AND DOCUMENTATION ARE PROVIDED AS IS  WITHOUT  WARRANTY  OF  ANY  KIND,
EITHER EXPRESS  OR  IMPLIED,  INCLUDING  WITHOUT  LIMITATION,  ANY  WARRANTY  OF
MERCHANTABILITY, TITLE, NON-INFRINGEMENT AND FITNESS FOR A  PARTICULAR  PURPOSE.
IN NO EVENT SHALL MICROCHIP OR  ITS  LICENSORS  BE  LIABLE  OR  OBLIGATED  UNDER
CONTRACT, NEGLIGENCE, STRICT LIABILITY, CONTRIBUTION,  BREACH  OF  WARRANTY,  OR
OTHER LEGAL  EQUITABLE  THEORY  ANY  DIRECT  OR  INDIRECT  DAMAGES  OR  EXPENSES
INCLUDING BUT NOT LIMITED TO ANY  INCIDENTAL,  SPECIAL,  INDIRECT,  PUNITIVE  OR
CONSEQUENTIAL DAMAGES, LOST  PROFITS  OR  LOST  DATA,  COST  OF  PROCUREMENT  OF
SUBSTITUTE  GOODS,  TECHNOLOGY,  SERVICES,  OR  ANY  CLAIMS  BY  THIRD   PARTIES
(INCLUDING BUT NOT LIMITED TO ANY DEFENSE  THEREOF),  OR  OTHER  SIMILAR  COSTS.
*******************************************************************************/

#include "device.h"
#include "plib_evsys${INDEX?string}.h"

<#if EVSYS_INTERRUPT_MODE == true>
	<#lt>EVSYS_OBJECT evsys;
</#if>

void EVSYS${INDEX?string}_Initialize( void )
{
<#assign TOTAL_CHANNEL = EVSYS_CHANNEL_NUMBER?number >
<#assign TOTAL_USER = EVSYS_USER_NUMBER?number >
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
	EVSYS_REGS->EVSYS_CHANNEL[${i}] = EVSYS_CHANNEL_EVGEN(${.vars[GENERATOR]}) | EVSYS_CHANNEL_PATH(${.vars[PATH]}) | EVSYS_CHANNEL_EDGSEL(${.vars[EDGE]}) \
									${(.vars[RUNSTANDBY])?then('| EVSYS_CHANNEL_RUNSTDBY', '')} ${(.vars[ONDEMAND])?then('| EVSYS_CHANNEL_ONDEMAND', '')};
	while(EVSYS_REGS->EVSYS_CHSTATUS && EVSYS_CHSTATUS_USRRDY${i}_Msk != EVSYS_CHSTATUS_USRRDY${i}_Msk);
	
	</#if>
	</#if>
</#list>

	/*Event Channel User Configuration*/
<#list 0..TOTAL_USER as i>
	<#assign CHANNEL = "EVSYS_USER_" + i >
	<#if .vars[CHANNEL]?has_content>
	<#if .vars[CHANNEL] != '0'>
	EVSYS_REGS->EVSYS_USER[${i}] = EVSYS_USER_CHANNEL(${.vars[CHANNEL]});
	</#if>
	</#if>
</#list>
<#if EVSYS_INTERRUPT_MODE>

	/*Interupt setting for Event System*/
	EVSYS_REGS->EVSYS_INTESET = ${EVSYS_INTERRUPT_VALUE};
</#if>
}

<#if EVSYS_INTERRUPT_MODE == true>
		
	<#lt>void EVSYS${INDEX?string}_InterruptEnable(EVSYS_INT_MASK interrupt)
	<#lt>{
	<#lt>	EVSYS_REGS->EVSYS_INTENSET = interrupt;
	<#lt>}

	<#lt>void EVSYS${INDEX?string}_InterruptDisable(EVSYS_INT_MASK interrupt)
	<#lt>{
	<#lt>	EVSYS_REGS->EVSYS_INTENCLR = interrupt;
	<#lt>}

	<#lt>void EVSYS${INDEX?string}_CallbackRegister( EVSYS_CALLBACK callback, uintptr_t context )
	<#lt>{
	<#lt>	evsys.callback = callback;
	<#lt>	evsys.context = context;
	<#lt>}
</#if>

<#if EVSYS_INTERRUPT_MODE == true>
	<#lt>void EVSYS${INDEX?string}_InterruptHandler( void )
	<#lt>{
	<#lt>	volatile uint32_t status = EVSYS_REGS->EVSYS_INTFLAG;
	<#lt>	EVSYS_REGS->EVSYS_INTFLAG = EVSYS_INTFLAG_Msk;
	<#lt>	if(evsys.callback != NULL)
    <#lt>   {
    <#lt>   	evsys.callback(evsys.context, status);
    <#lt>   }
	<#lt>}
</#if>	