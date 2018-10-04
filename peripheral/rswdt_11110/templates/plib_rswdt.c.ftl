/*******************************************************************************
  RSWDT Peripheral Library

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${RSWDT_INSTANCE_NAME?lower_case}.c

  Summary:
    RSWDT Source File

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
#include "plib_${RSWDT_INSTANCE_NAME?lower_case}.h"

<#if rswdtinterruptMode == true>
	<#lt>RSWDT_OBJECT rswdt;
</#if>

void ${RSWDT_INSTANCE_NAME}_Initialize( void )
{
	${RSWDT_INSTANCE_NAME}_REGS->RSWDT_MR = RSWDT_MR_ALLONES_Msk | RSWDT_MR_WDV(${rswdtWDV}) \
							${rswdtdebugHalt?then(' | RSWDT_MR_WDDBGHLT_Msk','')}${rswdtidleHalt?then(' | RSWDT_MR_WDIDLEHLT_Msk','')}${rswdtEnableReset?then(' | RSWDT_MR_WDRSTEN_Msk','')}${rswdtinterruptMode?then(' | RSWDT_MR_WDFIEN_Msk','')};
							
}

void ${RSWDT_INSTANCE_NAME}_Clear(void)
{
	${RSWDT_INSTANCE_NAME}_REGS->RSWDT_CR = (RSWDT_CR_KEY_PASSWD|RSWDT_CR_WDRSTT_Msk);
}

<#if rswdtinterruptMode == true>
	<#lt>void ${RSWDT_INSTANCE_NAME}_CallbackRegister( RSWDT_CALLBACK callback, uintptr_t context )
	<#lt>{
	<#lt>	rswdt.callback = callback;
	<#lt>	rswdt.context = context;
	<#lt>}
</#if>

<#if rswdtinterruptMode == true>
	<#lt>void ${RSWDT_INSTANCE_NAME}_InterruptHandler( void )
	<#lt>{
	<#lt>   ${RSWDT_INSTANCE_NAME}_REGS->RSWDT_SR;	
	<#lt>	if(rswdt.callback != NULL)
    <#lt>        {
    <#lt>            rswdt.callback(rswdt.context);
    <#lt>        }
	<#lt>}
</#if>	
