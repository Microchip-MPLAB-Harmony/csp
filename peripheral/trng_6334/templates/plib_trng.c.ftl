/*******************************************************************************
  TRNG Peripheral Library

  Company:
    Microchip Technology Inc.

  File Name:
    plib_trng.c

  Summary:
    TRNG Source File

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

<#macro GenerateCode>
#include "${__PROCESSOR?lower_case}.h"
#include "plib_trng${INDEX?string}.h"

<#if trngEnableInterrupt == true>
	<#lt>TRNG_OBJECT trng;
	
	<#lt>void TRNG${INDEX?string}_RandomNumberGenerate( void )
	<#lt>{
	<#lt>	TRNG_REGS->TRNG_CR = TRNG_CR_KEY_PASSWD | TRNG_CR_ENABLE_Msk;
	<#lt>	TRNG_REGS->TRNG_IER = TRNG_IER_DATRDY_Msk;
	<#lt>}

	<#lt>void TRNG${INDEX?string}_CallbackRegister( TRNG_CALLBACK callback, uintptr_t context )
	<#lt>{
	<#lt>	trng.callback = callback;
	<#lt>	trng.context = context;
	<#lt>}
</#if>

<#if trngEnableInterrupt == false>
	<#lt>uint32_t TRNG${INDEX?string}_ReadData( void )
	<#lt>{
	<#lt>	TRNG_REGS->TRNG_CR = TRNG_CR_KEY_PASSWD | TRNG_CR_ENABLE_Msk;
	<#lt>	while(((TRNG_REGS->TRNG_ISR) & (TRNG_ISR_DATRDY_Msk)) != TRNG_ISR_DATRDY_Msk);			
	<#lt>	TRNG_REGS->TRNG_CR = TRNG_CR_KEY_PASSWD;
	<#lt>	return (TRNG_REGS->TRNG_ODATA);
	<#lt>}
</#if>

<#if trngEnableInterrupt == true>
	<#lt>void TRNG${INDEX?string}_InterruptHandler( void )
	<#lt>{
	<#lt>	TRNG_REGS->TRNG_CR = TRNG_CR_KEY_PASSWD;
	<#lt>	trng.data = TRNG_REGS->TRNG_ODATA;
	<#lt>	if(trng.callback != NULL)
    <#lt>   {
    <#lt>   	trng.callback(trng.context,trng.data);
    <#lt>   }
	<#lt>}
</#if>	
</#macro>

<#if TRNG_Reserved == false>
<@GenerateCode/>
<#else>
/**** Warning: This module is used and configured by Crypto Library ****/
</#if>

