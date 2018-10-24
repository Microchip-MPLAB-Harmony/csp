/*******************************************************************************
  ${SDADC_INSTANCE_NAME} PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_${SDADC_INSTANCE_NAME?lower_case}.c

  Summary
    ${SDADC_INSTANCE_NAME} PLIB Implementation File.

  Description
    This file defines the interface to the SDADC peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

  Remarks:
    None.

*******************************************************************************/

// DOM-IGNORE-BEGIN
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
// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
/* This section lists the other files that are included in this file.
*/

#include "device.h"
#include "plib_${SDADC_INSTANCE_NAME?lower_case}.h"
<#compress>
<#assign SDADC_SEQCTRL_VAL = "">
<#assign SDADC_INTERRUPT_MODE = false>
<#assign SDADC_INTENSET_VAL = "">
<#assign SDADC_EVCTRL_VAL = "">
<#assign SDADC_CTRLA_VAL = "">

<#if SDADC_AUTO_SEQUENCE == true>
    <#list 0..2 as i>
        <#assign SDADC_SEQCTRL = "SDADC_SEQCTRL_SEQ" + i>
        <#if .vars[SDADC_SEQCTRL] == true>
            <#if SDADC_SEQCTRL_VAL != "">
                <#assign SDADC_SEQCTRL_VAL = SDADC_SEQCTRL_VAL + " | " + "SDADC_SEQCTRL_SEQEN(1U << " + i +")">
            <#else>
                <#assign SDADC_SEQCTRL_VAL = "SDADC_SEQCTRL_SEQEN(1U << " + i +")">
            </#if>
        </#if>
    </#list>
</#if>

<#if SDADC_INTENSET_RESRDY == true>
<#assign SDADC_INTERRUPT_MODE = true>
<#assign SDADC_INTENSET_VAL = "SDADC_INTENSET_RESRDY_Msk">
</#if>
<#if (SDADC_WINCTRL_WINMODE != "0") && SDADC_INTENSET_WINMON == true>
<#assign SDADC_INTERRUPT_MODE = true>
    <#if SDADC_INTENSET_VAL != "">
        <#assign SDADC_INTENSET_VAL = SDADC_INTENSET_VAL + " | SDADC_INTENSET_WINMON_Msk">
    <#else>
        <#assign SDADC_INTENSET_VAL = "SDADC_INTENSET_WINMON_Msk">
    </#if>
</#if>

<#if SDADC_EVCTRL_RESRDYEO == true>
<#assign SDADC_EVCTRL_VAL = "SDADC_EVCTRL_RESRDYEO_Msk">
</#if>
<#if SDADC_WINCTRL_WINMODE != "0" && SDADC_EVCTRL_WINMONEO == true>
    <#if SDADC_EVCTRL_VAL != "">
        <#assign SDADC_EVCTRL_VAL = SDADC_EVCTRL_VAL + " | SDADC_EVCTRL_WINMONEO_Msk">
    <#else>
        <#assign SDADC_EVCTRL_VAL = "SDADC_EVCTRL_WINMONEO_Msk">
    </#if>
</#if>

<#if SDADC_TRIGGER == "2">
    <#if SDADC_EVCTRL_FLUSH == "1">
        <#if SDADC_EVCTRL_VAL != "">
            <#assign SDADC_EVCTRL_VAL = SDADC_EVCTRL_VAL + " | SDADC_EVCTRL_FLUSHEI_Msk">
        <#else>
            <#assign SDADC_EVCTRL_VAL = "SDADC_EVCTRL_FLUSHEI_Msk">
        </#if>
    <#elseif SDADC_EVCTRL_FLUSH == "2">
        <#if SDADC_EVCTRL_VAL != "">
            <#assign SDADC_EVCTRL_VAL = SDADC_EVCTRL_VAL + " | SDADC_EVCTRL_FLUSHEI_Msk | SDADC_EVCTRL_FLUSHINV_Msk">
        <#else>
            <#assign SDADC_EVCTRL_VAL = "SDADC_EVCTRL_FLUSHEI_Msk | SDADC_EVCTRL_FLUSHINV_Msk">
        </#if>
    </#if>
    <#if SDADC_EVCTRL_START == "1">
        <#if SDADC_EVCTRL_VAL != "">
            <#assign SDADC_EVCTRL_VAL = SDADC_EVCTRL_VAL + " | SDADC_EVCTRL_STARTEI_Msk">
        <#else>
            <#assign SDADC_EVCTRL_VAL = "SDADC_EVCTRL_STARTEI_Msk">
        </#if>
    <#elseif SDADC_EVCTRL_START == "2">
        <#if SDADC_EVCTRL_VAL != "">
            <#assign SDADC_EVCTRL_VAL = SDADC_EVCTRL_VAL + " | SDADC_EVCTRL_STARTEI_Msk | SDADC_EVCTRL_STARTINV_Msk">
        <#else>
            <#assign SDADC_EVCTRL_VAL = "SDADC_EVCTRL_STARTEI_Msk | SDADC_EVCTRL_STARTINV_Msk">
        </#if>
    </#if>
</#if>

<#if SDADC_RUNSTDBY == true>
<#assign SDADC_CTRLA_VAL = "SDADC_CTRLA_RUNSTDBY_Msk">
</#if>
<#if SDADC_ONDEMAND == true>
    <#if SDADC_CTRLA_VAL != "">
        <#assign SDADC_CTRLA_VAL = SDADC_CTRLA_VAL + " | SDADC_CTRLA_ONDEMAND_Msk">
    <#else>
        <#assign SDADC_CTRLA_VAL = "SDADC_CTRLA_ONDEMAND_Msk">
    </#if>
</#if>
</#compress>
// *****************************************************************************
// *****************************************************************************
// Section: Global Data
// *****************************************************************************
// *****************************************************************************
// *****************************************************************************

<#if SDADC_INTERRUPT_MODE == true>
SDADC_CALLBACK_OBJECT ${SDADC_INSTANCE_NAME}_CallbackObj;
</#if>
// *****************************************************************************
// *****************************************************************************
// Section: ${SDADC_INSTANCE_NAME} Implementation
// *****************************************************************************
// *****************************************************************************

/* Initialize SDADC module as per MHC configurations */
void ${SDADC_INSTANCE_NAME}_Initialize( void )
{
    /* Software Reset */
    ${SDADC_INSTANCE_NAME}_REGS->SDADC_CTRLA = SDADC_CTRLA_SWRST_Msk;

    while((${SDADC_INSTANCE_NAME}_REGS->SDADC_SYNCBUSY & SDADC_SYNCBUSY_SWRST_Msk) == SDADC_SYNCBUSY_SWRST_Msk)
    {
        /* Wait for synchronization */
    }

    /* Set prescaler, over sampling ratio and skip count */
    ${SDADC_INSTANCE_NAME}_REGS->SDADC_CTRLB = SDADC_CTRLB_PRESCALER_${SDADC_CTRLB_PRESCALER} | SDADC_CTRLB_OSR_${SDADC_CTRLB_OSR} | SDADC_CTRLB_SKPCNT(2U);

    /* Configure reference voltage */
    ${SDADC_INSTANCE_NAME}_REGS->SDADC_REFCTRL = SDADC_REFCTRL_REFSEL_${SDADC_REFCTRL_REFSEL};

    <#if SDADC_TRIGGER == "0">
    ${SDADC_INSTANCE_NAME}_REGS->SDADC_CTRLC = SDADC_CTRLC_FREERUN_Msk;
    </#if>
    <#if SDADC_SEQCTRL_VAL?has_content>
    ${SDADC_INSTANCE_NAME}_REGS->SDADC_SEQCTRL = ${SDADC_SEQCTRL_VAL};
    </#if>
    <#if SDADC_AUTO_SEQUENCE == false>
    /* Configure positive and negative input pins */
    ${SDADC_INSTANCE_NAME}_REGS->SDADC_INPUTCTRL = SDADC_INPUTCTRL_MUXSEL_${SDADC_INPUTCTRL_MUXSEL};
    </#if>
    <#if SDADC_WINCTRL_WINMODE != "0">
    /* Window monitor configurations */
    ${SDADC_INSTANCE_NAME}_REGS->SDADC_WINCTRL = SDADC_WINCTRL_WINMODE(${SDADC_WINCTRL_WINMODE});
    ${SDADC_INSTANCE_NAME}_REGS->SDADC_WINLT = (int16_t)(${SDADC_WINLT}) << 8;
    ${SDADC_INSTANCE_NAME}_REGS->SDADC_WINUT = (int16_t)(${SDADC_WINUT}) << 8;
    </#if>

    /* Clear all interrupts */
    ${SDADC_INSTANCE_NAME}_REGS->SDADC_INTFLAG = SDADC_INTFLAG_Msk;

<#if SDADC_INTENSET_VAL?has_content>
    /* Enable interrupt */
    ${SDADC_INSTANCE_NAME}_REGS->SDADC_INTENSET = ${SDADC_INTENSET_VAL};
    ${SDADC_INSTANCE_NAME}_CallbackObj.callback = NULL;
</#if>

<#if SDADC_EVCTRL_VAL?has_content>
    ${SDADC_INSTANCE_NAME}_REGS->SDADC_EVCTRL = ${SDADC_EVCTRL_VAL};
</#if>

<#if SDADC_CTRLA_VAL?has_content>
   /* Configure Run in standby, On demand property */
    ${SDADC_INSTANCE_NAME}_REGS->SDADC_CTRLA |= ${SDADC_CTRLA_VAL};
</#if>

    /* Enable SDADC */
    ${SDADC_INSTANCE_NAME}_REGS->SDADC_CTRLA |= SDADC_CTRLA_ENABLE_Msk;

    while((${SDADC_INSTANCE_NAME}_REGS->SDADC_SYNCBUSY))
    {
        /* Wait for synchronization */
    }
}


void ${SDADC_INSTANCE_NAME}_ConversionStart( void )
{
    /* Start conversion */
    ${SDADC_INSTANCE_NAME}_REGS->SDADC_SWTRIG = SDADC_SWTRIG_START_Msk;

    while((${SDADC_INSTANCE_NAME}_REGS->SDADC_SYNCBUSY & SDADC_SYNCBUSY_SWTRIG_Msk) == SDADC_SYNCBUSY_SWTRIG_Msk)
    {
        /* Synchronization between SWTRIG start with the clock domain */
    }
}

bool ${SDADC_INSTANCE_NAME}_ConversionResultIsReady( void )
{
    return (${SDADC_INSTANCE_NAME}_REGS->SDADC_INTFLAG & SDADC_INTFLAG_RESRDY_Msk);
}

int16_t ${SDADC_INSTANCE_NAME}_ConversionResultGet( void )
{
    /* right-shift by 8-bits to get signed 16-bit result */
    return ((int16_t)(${SDADC_INSTANCE_NAME}_REGS->SDADC_RESULT >> 8));
}

bool ${SDADC_INSTANCE_NAME}_ConversionSequenceIsFinished(void)
{
    bool seq_status = false;
    if ((${SDADC_INSTANCE_NAME}_REGS->SDADC_SEQSTATUS & SDADC_SEQSTATUS_SEQBUSY_Msk) != SDADC_SEQSTATUS_SEQBUSY_Msk)
    {
        seq_status = true;
    }
    return seq_status;
}

void ${SDADC_INSTANCE_NAME}_ComparisonWindowSet(int16_t low_threshold, int16_t high_threshold)
{
    /* Update threshold values as 24-bit signed value */
    ${SDADC_INSTANCE_NAME}_REGS->SDADC_WINLT = low_threshold << 8;
    ${SDADC_INSTANCE_NAME}_REGS->SDADC_WINUT = high_threshold << 8;
}

<#if SDADC_INTERRUPT_MODE == true>
void ${SDADC_INSTANCE_NAME}_CallbackRegister( SDADC_CALLBACK callback, uintptr_t context )
{
    ${SDADC_INSTANCE_NAME}_CallbackObj.callback = callback;

    ${SDADC_INSTANCE_NAME}_CallbackObj.context = context;
}


void ${SDADC_INSTANCE_NAME}_InterruptHandler( void )
{
    if (${SDADC_INSTANCE_NAME}_CallbackObj.callback != NULL)
    {
        ${SDADC_INSTANCE_NAME}_CallbackObj.callback(${SDADC_INSTANCE_NAME}_CallbackObj.context);
    }
    /* Clear interrupt flags */
    ${SDADC_INSTANCE_NAME}_REGS->SDADC_INTFLAG = SDADC_INTFLAG_Msk;
}
</#if>
