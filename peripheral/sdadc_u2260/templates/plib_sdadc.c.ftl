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
<#if core.CoreSysIntFile == true>
#include "interrupts.h"
</#if>
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
                <#assign SDADC_SEQCTRL_VAL = SDADC_SEQCTRL_VAL + " | " + "SDADC_SEQCTRL_SEQEN(1UL << " + i +"U)">
            <#else>
                <#assign SDADC_SEQCTRL_VAL = "SDADC_SEQCTRL_SEQEN(1UL << " + i +"U)">
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
static volatile SDADC_CALLBACK_OBJECT ${SDADC_INSTANCE_NAME}_CallbackObj;
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
    ${SDADC_INSTANCE_NAME}_REGS->SDADC_CTRLA = (uint8_t)SDADC_CTRLA_SWRST_Msk;

    while((${SDADC_INSTANCE_NAME}_REGS->SDADC_SYNCBUSY & SDADC_SYNCBUSY_SWRST_Msk) == SDADC_SYNCBUSY_SWRST_Msk)
    {
        /* Wait for synchronization */
    }

    /* Set prescaler, over sampling ratio and skip count */
    ${SDADC_INSTANCE_NAME}_REGS->SDADC_CTRLB = (uint16_t)(SDADC_CTRLB_PRESCALER_${SDADC_CTRLB_PRESCALER} | SDADC_CTRLB_OSR_${SDADC_CTRLB_OSR} | SDADC_CTRLB_SKPCNT(2UL));

    /* Configure reference voltage */
    <#if SDADC_REFCTRL_REFSEL == "INTREF" || SDADC_REFCTRL_REFSEL == "DAC">
    ${SDADC_INSTANCE_NAME}_REGS->SDADC_REFCTRL = (uint8_t)(SDADC_REFCTRL_REFSEL_${SDADC_REFCTRL_REFSEL} | SDADC_REFCTRL_ONREFBUF_Msk);
    <#else>
    ${SDADC_INSTANCE_NAME}_REGS->SDADC_REFCTRL = (uint8_t)SDADC_REFCTRL_REFSEL_${SDADC_REFCTRL_REFSEL};
    </#if>

    <#if SDADC_TRIGGER == "0">
    ${SDADC_INSTANCE_NAME}_REGS->SDADC_CTRLC = (uint8_t)SDADC_CTRLC_FREERUN_Msk;
    </#if>
    <#if SDADC_SEQCTRL_VAL?has_content>
    ${SDADC_INSTANCE_NAME}_REGS->SDADC_SEQCTRL = ${SDADC_SEQCTRL_VAL};
    </#if>
    <#if SDADC_AUTO_SEQUENCE == false>
    /* Configure positive and negative input pins */
    ${SDADC_INSTANCE_NAME}_REGS->SDADC_INPUTCTRL = (uint8_t)SDADC_INPUTCTRL_MUXSEL_${SDADC_INPUTCTRL_MUXSEL};
    </#if>
    <#if SDADC_WINCTRL_WINMODE != "0">
    /* Window monitor configurations */
    ${SDADC_INSTANCE_NAME}_REGS->SDADC_WINCTRL = (uint8_t)SDADC_WINCTRL_WINMODE(${SDADC_WINCTRL_WINMODE}UL);
    ${SDADC_INSTANCE_NAME}_REGS->SDADC_WINLT = ${SDADC_WINLT}UL << 8U;
    ${SDADC_INSTANCE_NAME}_REGS->SDADC_WINUT = ${SDADC_WINUT}UL << 8U;
    </#if>

    /* Clear all interrupts */
    ${SDADC_INSTANCE_NAME}_REGS->SDADC_INTFLAG = (uint8_t)SDADC_INTFLAG_Msk;

<#if SDADC_INTENSET_VAL?has_content>
    /* Enable interrupt */
    ${SDADC_INSTANCE_NAME}_REGS->SDADC_INTENSET = (uint8_t)(${SDADC_INTENSET_VAL});
    ${SDADC_INSTANCE_NAME}_CallbackObj.callback = NULL;
</#if>

<#if SDADC_EVCTRL_VAL?has_content>
    ${SDADC_INSTANCE_NAME}_REGS->SDADC_EVCTRL = (uint8_t)(${SDADC_EVCTRL_VAL});
</#if>

<#if SDADC_CTRLA_VAL?has_content>
   /* Configure Run in standby, On demand property */
    ${SDADC_INSTANCE_NAME}_REGS->SDADC_CTRLA |= (uint8_t)(${SDADC_CTRLA_VAL});
</#if>

    /* Enable SDADC */
    ${SDADC_INSTANCE_NAME}_REGS->SDADC_CTRLA |= (uint8_t)SDADC_CTRLA_ENABLE_Msk;

    while((${SDADC_INSTANCE_NAME}_REGS->SDADC_SYNCBUSY) != 0U)
    {
        /* Wait for synchronization */
    }
}

void ${SDADC_INSTANCE_NAME}_Enable( void )
{
    ${SDADC_INSTANCE_NAME}_REGS->SDADC_CTRLA |= (uint8_t)SDADC_CTRLA_ENABLE_Msk;
    while((${SDADC_INSTANCE_NAME}_REGS->SDADC_SYNCBUSY & SDADC_SYNCBUSY_ENABLE_Msk) == SDADC_SYNCBUSY_ENABLE_Msk)
    {
        /* Wait for synchronization */
    }
}

void ${SDADC_INSTANCE_NAME}_Disable( void )
{
    ${SDADC_INSTANCE_NAME}_REGS->SDADC_CTRLA &= (uint8_t)(~SDADC_CTRLA_ENABLE_Msk);
    while((${SDADC_INSTANCE_NAME}_REGS->SDADC_SYNCBUSY & SDADC_SYNCBUSY_ENABLE_Msk) == SDADC_SYNCBUSY_ENABLE_Msk)
    {
        /* Wait for synchronization */
    }
}

<#if SDADC_TRIGGER == "1"> <#-- SW trigger -->
void ${SDADC_INSTANCE_NAME}_ConversionStart( void )
{
    /* Start conversion */
    ${SDADC_INSTANCE_NAME}_REGS->SDADC_SWTRIG = (uint8_t)SDADC_SWTRIG_START_Msk;

    while((${SDADC_INSTANCE_NAME}_REGS->SDADC_SYNCBUSY & SDADC_SYNCBUSY_SWTRIG_Msk) == SDADC_SYNCBUSY_SWTRIG_Msk)
    {
        /* Synchronization between SWTRIG start with the clock domain */
    }
}
</#if>

int16_t ${SDADC_INSTANCE_NAME}_ConversionResultGet( void )
{
    /* right-shift by 8-bits to get signed 16-bit result */
    uint32_t result = SDADC_REGS->SDADC_RESULT >> 8U;
    return ((int16_t)result);
}

<#if SDADC_AUTO_SEQUENCE == true>
bool ${SDADC_INSTANCE_NAME}_ConversionSequenceIsFinished(void)
{
    bool seq_status = false;
    if ((${SDADC_INSTANCE_NAME}_REGS->SDADC_SEQSTATUS & SDADC_SEQSTATUS_SEQBUSY_Msk) != SDADC_SEQSTATUS_SEQBUSY_Msk)
    {
        seq_status = true;
    }
    return seq_status;
}
</#if>

<#if SDADC_WINCTRL_WINMODE != "0">
void ${SDADC_INSTANCE_NAME}_ComparisonWindowSet(int16_t low_threshold, int16_t high_threshold)
{
    /* Update threshold values as 24-bit signed value */
    ${SDADC_INSTANCE_NAME}_REGS->SDADC_WINLT = ((uint32_t)low_threshold << 8U);
    ${SDADC_INSTANCE_NAME}_REGS->SDADC_WINUT = ((uint32_t)high_threshold << 8U);
    while((${SDADC_INSTANCE_NAME}_REGS->SDADC_SYNCBUSY) != 0U)
    {
        /* Wait for synchronization */
    }
}
</#if>

<#if SDADC_INTERRUPT_MODE == true>
void ${SDADC_INSTANCE_NAME}_CallbackRegister( SDADC_CALLBACK callback, uintptr_t context )
{
    ${SDADC_INSTANCE_NAME}_CallbackObj.callback = callback;

    ${SDADC_INSTANCE_NAME}_CallbackObj.context = context;
}


void __attribute__((used)) ${SDADC_INSTANCE_NAME}_InterruptHandler( void )
{
    SDADC_STATUS status;
    status = ${SDADC_INSTANCE_NAME}_REGS->SDADC_INTFLAG;
    /* Clear interrupt flags */
    ${SDADC_INSTANCE_NAME}_REGS->SDADC_INTFLAG = (uint8_t)SDADC_INTFLAG_Msk;

    if (${SDADC_INSTANCE_NAME}_CallbackObj.callback != NULL)
    {
        uintptr_t context = ${SDADC_INSTANCE_NAME}_CallbackObj.context;
        ${SDADC_INSTANCE_NAME}_CallbackObj.callback(status, context);
    }

}
</#if>

<#if SDADC_INTENSET_RESRDY == false>
bool ${SDADC_INSTANCE_NAME}_ConversionResultIsReady( void )
{
    bool status;
    status = (((${SDADC_INSTANCE_NAME}_REGS->SDADC_INTFLAG & SDADC_INTFLAG_RESRDY_Msk) >> SDADC_INTFLAG_RESRDY_Pos) != 0U);
    if (status)
    {
        ${SDADC_INSTANCE_NAME}_REGS->SDADC_INTFLAG = (uint8_t)SDADC_INTFLAG_RESRDY_Msk;
    }
    return status;
}
</#if>

<#if (SDADC_WINCTRL_WINMODE != "0") && SDADC_INTENSET_WINMON == false>
bool ${SDADC_INSTANCE_NAME}_WindowMonitorIsSet( void )
{
    bool status;
    status =  (((${SDADC_INSTANCE_NAME}_REGS->SDADC_INTFLAG & SDADC_INTFLAG_WINMON_Msk) >> SDADC_INTFLAG_WINMON_Pos) != 0U);
    if (status == true)
    {
        ${SDADC_INSTANCE_NAME}_REGS->SDADC_INTFLAG = (uint8_t)SDADC_INTFLAG_WINMON_Msk;
    }
    return status;
}
</#if>
