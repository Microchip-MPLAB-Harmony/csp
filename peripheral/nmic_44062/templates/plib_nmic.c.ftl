/*******************************************************************************
Interface definition of EFC PLIB.

Company:
 Microchip Technology Inc.

File Name:
 plib_nmic.c

Summary:
 Source file for NMIC Plib.

Description:
 This file defines the interface for the EFC Plib.
 It allows user to configure the sources for Non-maskable interrupt.
*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
Copyright (c) 2017 released Microchip Technology Inc.  All rights reserved.
Microchip licenses to you the right to use, modify, copy and distribute
Software only when embedded on a Microchip microcontroller or digital signal
controller that is integrated into your product or third party product
(pursuant to the sublicense terms in the accompanying license agreement).
You should refer to the license agreement accompanying this Software for
additional information regarding your rights and obligations.
SOFTWARE AND DOCUMENTATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND,
EITHER EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION, ANY WARRANTY OF
MERCHANTABILITY, TITLE, NON-INFRINGEMENT AND FITNESS FOR A PARTICULAR PURPOSE.
IN NO EVENT SHALL MICROCHIP OR ITS LICENSORS BE LIABLE OR OBLIGATED UNDER
CONTRACT, NEGLIGENCE, STRICT LIABILITY, CONTRIBUTION, BREACH OF WARRANTY, OR
OTHER LEGAL EQUITABLE THEORY ANY DIRECT OR INDIRECT DAMAGES OR EXPENSES
INCLUDING BUT NOT LIMITED TO ANY INCIDENTAL, SPECIAL, INDIRECT, PUNITIVE OR
CONSEQUENTIAL DAMAGES, LOST PROFITS OR LOST DATA, COST OF PROCUREMENT OF
SUBSTITUTE GOODS, TECHNOLOGY, SERVICES, OR ANY CLAIMS BY THIRD PARTIES
(INCLUDING BUT NOT LIMITED TO ANY DEFENSE THEREOF), OR OTHER SIMILAR COSTS.
*******************************************************************************/
#include <stddef.h>
#include "plib_${NMIC_INSTANCE_NAME?lower_case}.h"
<#if core.CoreSysIntFile == true>
#include "interrupts.h"
</#if>

NMIC_OBJECT nmic;

void ${NMIC_INSTANCE_NAME}_Initialize( void )
{
<#list 0..NUM_NMIC_SOURCE-1 as i>
	<#assign NMIC_ENABLE = "NMIC_SRC_EN_" + i >
	<#assign NMIC_LVL = "NMIC_SRC_" + i + "_LVL">
	<#assign NMIC_POL = "NMIC_SRC_" + i + "_POL">
	<#assign NMIC_GF_EN = "NMIC_SRC_GF_EN_" + i>
	<#assign NMIC_GFSEL = "NMIC_SRC_GFSEL_" + i>
	<#assign NMIC_FZ = "NMIC_SRC_FZ_" + i>
	<#if .vars[NMIC_ENABLE]?has_content>
	<#if (.vars[NMIC_ENABLE] != false)>
	<#if i == 0>
	<#lt>	NMIC_REGS->NMIC_SCFG${i}R = NMIC_SCFG${i}R_EN_Msk ${(.vars[NMIC_LVL] == '1')?then('| NMIC_SCFG${i}R_LVL_Msk', '')} ${.vars[NMIC_FZ]?then('| NMIC_SCFG${i}R_FRZ_Msk', '')}\
							 ${(.vars[NMIC_POL] == '1')?then('| NMIC_SCFG${i}R_POL_Msk', '')} ${.vars[NMIC_GF_EN]?then('| NMIC_SCFG${i}R_GFEN_Msk | NMIC_SCFG${i}R_GFSEL(${.vars[NMIC_GFSEL]})', '')};
	<#elseif i == 4>
	<#lt>	NMIC_REGS->NMIC_SCFG${i}R = NMIC_SCFG${i}R_EN_Msk | (NMIC_REGS->NMIC_SCFG${i}R & (~NMIC_SCFG${i}R_POL_Msk));
	<#else>
	<#lt>	NMIC_REGS->NMIC_SCFG${i}R |= NMIC_SCFG${i}R_EN_Msk;
	</#if>
	</#if>
	</#if>
</#list>
<#lt>	NMIC_REGS->NMIC_IER = 0x${NMIC_INTERRUPT};
}


void ${NMIC_INSTANCE_NAME}_CallbackRegister( NMIC_CALLBACK callback, uintptr_t context )
{
	nmic.callback = callback;
	nmic.context = context;
}


void ${NMIC_INSTANCE_NAME}_InterruptHandler( void )
{
	volatile uint32_t status = NMIC_REGS->NMIC_ISR;
	if(nmic.callback != NULL)
    {
        nmic.callback(nmic.context, status);
    }
}
