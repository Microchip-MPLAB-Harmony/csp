/*******************************************************************************
  TRNG Peripheral Library

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${TRNG_INSTANCE_NAME?lower_case}.c

  Summary:
    TRNG Source File

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

<#macro GenerateCode>
#include "device.h"
#include "plib_${TRNG_INSTANCE_NAME?lower_case}.h"
<#if core.CoreSysIntFile == true>
#include "interrupts.h"
</#if>

/* MISRAC 2023 deviation block start */
/* MISRA C-2023 Rule 10.1 deviated in this file. Deviation record ID - H3_MISRAC_2023_R_10_1_DR_1 */
/* MISRA C-2023 Rule 10.4 deviated in this file. Deviation record ID - H3_MISRAC_2023_R_10_4_DR_1 */
/* MISRA C-2023 Rule 7.6 deviated in this file. Deviation record ID - H3_MISRAC_2023_R_7_6_DR_1 */
<#if core.COVERITY_SUPPRESS_DEVIATION?? && core.COVERITY_SUPPRESS_DEVIATION>
<#if core.COMPILER_CHOICE == "XC32">
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wunknown-pragmas"
</#if>
#pragma coverity compliance block deviate "MISRA C-2023 Rule 10.1" "H3_MISRAC_2023_R_10_1_DR_1"
#pragma coverity compliance block deviate "MISRA C-2023 Rule 10.4" "H3_MISRAC_2023_R_10_4_DR_1"
#pragma coverity compliance block deviate "MISRA C-2023 Rule 7.6" "H3_MISRAC_2023_R_7_6_DR_1"
</#if>

<#if trngEnableInterrupt == true>
    <#lt>static volatile TRNG_OBJECT trng;
</#if>

void ${TRNG_INSTANCE_NAME}_Initialize( void )
{<#if trngEnableEvent>
    ${TRNG_INSTANCE_NAME}_REGS->TRNG_EVCTRL =  TRNG_EVCTRL_DATARDYEO_Msk;
 </#if>
 <#if TRNG_STANDBY>
    ${TRNG_INSTANCE_NAME}_REGS->TRNG_CTRLA =  TRNG_CTRLA_RUNSTDBY_Msk;
 </#if>
}
<#if trngEnableInterrupt == true>

    <#lt>void ${TRNG_INSTANCE_NAME}_RandomNumberGenerate( void )
    <#lt>{
    <#lt>   ${TRNG_INSTANCE_NAME}_REGS->TRNG_CTRLA |= TRNG_CTRLA_ENABLE_Msk;
    <#lt>   ${TRNG_INSTANCE_NAME}_REGS->TRNG_INTENSET = TRNG_INTENSET_DATARDY_Msk;
    <#lt>}

    <#lt>void ${TRNG_INSTANCE_NAME}_CallbackRegister( TRNG_CALLBACK callback, uintptr_t context )
    <#lt>{
    <#lt>   trng.callback = callback;
    <#lt>   trng.context = context;
    <#lt>}
</#if>

<#if trngEnableInterrupt == false>
    <#lt>uint32_t ${TRNG_INSTANCE_NAME}_ReadData( void )
    <#lt>{
    <#lt>   ${TRNG_INSTANCE_NAME}_REGS->TRNG_CTRLA |= TRNG_CTRLA_ENABLE_Msk;
    <#lt>   while(((${TRNG_INSTANCE_NAME}_REGS->TRNG_INTFLAG) & (TRNG_INTFLAG_DATARDY_Msk)) != TRNG_INTFLAG_DATARDY_Msk)
    <#lt>   {
    <#lt>       /* Do Nothing */
    <#lt>   }
    <#lt>   ${TRNG_INSTANCE_NAME}_REGS->TRNG_CTRLA &= ~(TRNG_CTRLA_ENABLE_Msk);
    <#lt>   return (${TRNG_INSTANCE_NAME}_REGS->TRNG_DATA);
    <#lt>}
</#if>

<#if trngEnableInterrupt == true>
    <#lt>void __attribute__((used)) ${TRNG_INSTANCE_NAME}_InterruptHandler( void )
    <#lt>{
    <#lt>   ${TRNG_INSTANCE_NAME}_REGS->TRNG_CTRLA = ((${TRNG_INSTANCE_NAME}_REGS->TRNG_CTRLA) & (uint8_t)(~TRNG_CTRLA_ENABLE_Msk));
    <#lt>   ${TRNG_INSTANCE_NAME}_REGS->TRNG_INTENCLR = TRNG_INTENCLR_DATARDY_Msk;
    <#lt>   trng.data = ${TRNG_INSTANCE_NAME}_REGS->TRNG_DATA;
    <#lt>   if(trng.callback != NULL)
    <#lt>   {
    <#lt>       uint32_t data = trng.data;
    <#lt>       uintptr_t context = trng.context;
    <#lt>       trng.callback(data, context);
    <#lt>   }
    <#lt>}
</#if>

<#if core.COVERITY_SUPPRESS_DEVIATION?? && core.COVERITY_SUPPRESS_DEVIATION>
#pragma coverity compliance end_block "MISRA C-2023 Rule 10.1"
#pragma coverity compliance end_block "MISRA C-2023 Rule 10.4"
#pragma coverity compliance end_block "MISRA C-2023 Rule 7.6"
<#if core.COMPILER_CHOICE == "XC32">
#pragma GCC diagnostic pop
</#if>
</#if>
/* MISRAC 2023 deviation block end */
</#macro>

<#if TRNG_Reserved == false>
<@GenerateCode/>
<#else>
/**** Warning: This module is used and configured by Crypto Library ****/
</#if>

