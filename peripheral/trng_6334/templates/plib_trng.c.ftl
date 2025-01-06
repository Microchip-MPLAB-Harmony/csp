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

<#if trngEnableInterrupt == true>

    <#lt>typedef struct
    <#lt>{
    <#lt>    TRNG_CALLBACK          callback;
    <#lt>    uintptr_t               context;
    <#lt>} TRNG_OBJECT ;

    <#lt>static volatile TRNG_OBJECT trng;
</#if>

<#lt>void ${TRNG_INSTANCE_NAME}_Initialize( void )
<#lt>{
<#lt>    ${TRNG_INSTANCE_NAME}_REGS->TRNG_CR = TRNG_CR_${CRKEYNAME} | TRNG_CR_ENABLE_Msk;
<#lt>}

<#if trngEnableInterrupt == true>
    <#lt>void ${TRNG_INSTANCE_NAME}_RandomNumberGenerate( void )
    <#lt>{
    <#lt>    ${TRNG_INSTANCE_NAME}_REGS->TRNG_IER = TRNG_IER_DATRDY_Msk;
    <#lt>}

    <#lt>void ${TRNG_INSTANCE_NAME}_CallbackRegister( TRNG_CALLBACK callback, uintptr_t context )
    <#lt>{
    <#lt>    trng.callback = callback;
    <#lt>    trng.context = context;
    <#lt>}
</#if>

<#if trngEnableInterrupt == false>
    <#lt>uint32_t ${TRNG_INSTANCE_NAME}_ReadData( void )
    <#lt>{
    <#lt>    while(((${TRNG_INSTANCE_NAME}_REGS->TRNG_ISR) & (TRNG_ISR_DATRDY_Msk)) != TRNG_ISR_DATRDY_Msk)
    <#lt>    {
                 /* Wait for read to complete */
    <#lt>    }
    <#lt>    return (${TRNG_INSTANCE_NAME}_REGS->TRNG_ODATA);
    <#lt>}
</#if>

    <#lt>void ${TRNG_INSTANCE_NAME}_Enable( void )
    <#lt>{
    <#lt>    ${TRNG_INSTANCE_NAME}_REGS->TRNG_CR = TRNG_CR_${CRKEYNAME} | TRNG_CR_ENABLE_Msk;
    <#lt>}

    <#lt>void ${TRNG_INSTANCE_NAME}_Disable( void )
    <#lt>{
    <#lt>    ${TRNG_INSTANCE_NAME}_REGS->TRNG_CR = TRNG_CR_${CRKEYNAME};
    <#lt>}

<#if trngEnableInterrupt == true>
    <#lt>void __attribute__((used)) ${TRNG_INSTANCE_NAME}_InterruptHandler( void )
    <#lt>{
    <#lt>    uint32_t data;
    <#lt>    /* Additional temporary variable used to prevent MISRA violations (Rule 13.x) */
    <#lt>    uintptr_t context = trng.context;
    <#lt>    data = ${TRNG_INSTANCE_NAME}_REGS->TRNG_ODATA;
    <#lt>    ${TRNG_INSTANCE_NAME}_REGS->TRNG_IDR = TRNG_IDR_DATRDY_Msk;
    <#lt>    if ((trng.callback != NULL) && (${TRNG_INSTANCE_NAME}_REGS->TRNG_ISR & TRNG_ISR_DATRDY_Msk))
    <#lt>    {
    <#lt>         trng.callback(data, context);
    <#lt>    }
    <#lt>}
</#if>
</#macro>

<#if TRNG_Reserved == false>
<@GenerateCode/>
<#else>
/**** Warning: This module is used and configured by Crypto Library ****/
</#if>

