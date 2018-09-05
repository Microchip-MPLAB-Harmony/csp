/*******************************************************************************
  SDADC${SDADC_INDEX} PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_sdadc${SDADC_INDEX}.c

  Summary
    SDADC${SDADC_INDEX} PLIB Implementation File.

  Description
    This file defines the interface to the SDADC peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

  Remarks:
    None.

*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
Copyright (c) 2017 released Microchip Technology Inc. All rights reserved.
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
// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
/* This section lists the other files that are included in this file.
*/

#include "device.h"
#include "plib_sdadc${SDADC_INDEX}.h"
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
SDADC_CALLBACK_OBJECT SDADC${SDADC_INDEX}_CallbackObj;
</#if>
// *****************************************************************************
// *****************************************************************************
// Section: SDADC${SDADC_INDEX} Implementation
// *****************************************************************************
// *****************************************************************************

/* Initialize SDADC module as per MHC configurations */
void SDADC${SDADC_INDEX}_Initialize( void )
{
    /* Software Reset */
    SDADC_REGS->SDADC_CTRLA = SDADC_CTRLA_SWRST_Msk;

    while((SDADC_REGS->SDADC_SYNCBUSY & SDADC_SYNCBUSY_SWRST_Msk) == SDADC_SYNCBUSY_SWRST_Msk)
    {
        /* Wait for synchronization */
    }

    /* Set prescaler, over sampling ratio and skip count */
    SDADC_REGS->SDADC_CTRLB = SDADC_CTRLB_PRESCALER_${SDADC_CTRLB_PRESCALER} | SDADC_CTRLB_OSR_${SDADC_CTRLB_OSR} | SDADC_CTRLB_SKPCNT(2U);

    /* Configure reference voltage */
    SDADC_REGS->SDADC_REFCTRL = SDADC_REFCTRL_REFSEL_${SDADC_REFCTRL_REFSEL};

    <#if SDADC_TRIGGER == "0">
    SDADC_REGS->SDADC_CTRLC = SDADC_CTRLC_FREERUN_Msk;
    </#if>
    <#if SDADC_TRIGGER == "2">
    SDADC_REGS->SDADC_EVCTRL = SDADC_EVCTRL_STARTEI_Msk ${SDADC_EVENT_INVERT?then(' | SDADC_EVCTRL_STARTINV_Msk','')};
    </#if>
    <#if SDADC_SEQCTRL_VAL?has_content>
    SDADC_REGS->SDADC_SEQCTRL = ${SDADC_SEQCTRL_VAL};
    </#if>
    <#if SDADC_AUTO_SEQUENCE == false>
    /* Configure positive and negative input pins */
    SDADC_REGS->SDADC_INPUTCTRL = SDADC_INPUTCTRL_MUXSEL_${SDADC_INPUTCTRL_MUXSEL};
    </#if>
    <#if SDADC_WINCTRL_WINMODE != "0">
    /* Window monitor configurations */
    SDADC_REGS->SDADC_WINCTRL = SDADC_WINCTRL_WINMODE(${SDADC_WINCTRL_WINMODE});
    SDADC_REGS->SDADC_WINLT = (int16_t)(${SDADC_WINLT}) << 8;
    SDADC_REGS->SDADC_WINUT = (int16_t)(${SDADC_WINUT}) << 8;
    </#if>

    /* Clear all interrupts */
    SDADC_REGS->SDADC_INTFLAG = SDADC_INTFLAG_Msk;

<#if SDADC_INTENSET_VAL?has_content>
    /* Enable interrupt */
    SDADC_REGS->SDADC_INTENSET = ${SDADC_INTENSET_VAL};
    SDADC${SDADC_INDEX}_CallbackObj.callback = NULL;
</#if>

<#if SDADC_EVCTRL_VAL?has_content>
    SDADC_REGS->SDADC_EVCTRL |= ${SDADC_EVCTRL_VAL};
</#if>

<#if SDADC_CTRLA_VAL?has_content>
   /* Configure Run in standby, On demand property */
    SDADC_REGS->SDADC_CTRLA |= ${SDADC_CTRLA_VAL};
</#if>

    /* Enable SDADC */
    SDADC_REGS->SDADC_CTRLA |= SDADC_CTRLA_ENABLE_Msk;

    while((SDADC_REGS->SDADC_SYNCBUSY))
    {
        /* Wait for synchronization */
    }
}


void SDADC${SDADC_INDEX}_ConversionStart( void )
{
    /* Start conversion */
    SDADC_REGS->SDADC_SWTRIG = SDADC_SWTRIG_START_Msk;

    while((SDADC_REGS->SDADC_SYNCBUSY & SDADC_SYNCBUSY_SWTRIG_Msk) == SDADC_SYNCBUSY_SWTRIG_Msk)
    {
        /* Synchronization between SWTRIG start with the clock domain */
    }
}

bool SDADC${SDADC_INDEX}_ConversionResultIsReady( void )
{
    return (SDADC_REGS->SDADC_INTFLAG & SDADC_INTFLAG_RESRDY_Msk);
}

int16_t SDADC${SDADC_INDEX}_ConversionResultGet( void )
{
    /* right-shift by 8-bits to get signed 16-bit result */
    return ((int16_t)(SDADC_REGS->SDADC_RESULT >> 8));
}

bool SDADC${SDADC_INDEX}_ConversionSequenceIsFinished(void)
{
    bool seq_status = false;
    if ((SDADC_REGS->SDADC_SEQSTATUS & SDADC_SEQSTATUS_SEQBUSY_Msk) != SDADC_SEQSTATUS_SEQBUSY_Msk)
    {
        seq_status = true;
    }
    return seq_status;
}

void SDADC${SDADC_INDEX}_ComparisonWindowSet(int16_t low_threshold, int16_t high_threshold)
{
    /* Update threshold values as 24-bit signed value */
    SDADC_REGS->SDADC_WINLT = low_threshold << 8;
    SDADC_REGS->SDADC_WINUT = high_threshold << 8;
}

<#if SDADC_INTERRUPT_MODE == true>
void SDADC${SDADC_INDEX}_CallbackRegister( SDADC_CALLBACK callback, uintptr_t context )
{
    SDADC${SDADC_INDEX}_CallbackObj.callback = callback;

    SDADC${SDADC_INDEX}_CallbackObj.context = context;
}


void SDADC${SDADC_INDEX}_InterruptHandler( void )
{
    if (SDADC${SDADC_INDEX}_CallbackObj.callback != NULL)
    {
        SDADC${SDADC_INDEX}_CallbackObj.callback(SDADC${SDADC_INDEX}_CallbackObj.context);
    }
    /* Clear interrupt flags */
    SDADC_REGS->SDADC_INTFLAG = SDADC_INTFLAG_Msk;
}
</#if>