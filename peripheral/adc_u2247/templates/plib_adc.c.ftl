/*******************************************************************************
  Analog-to-Digital Converter(ADC${ADC_INDEX}) PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_adc${ADC_INDEX}.c

  Summary
    ADC${ADC_INDEX} PLIB Implementation File.

  Description
    This file defines the interface to the ADC peripheral library. This
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

#include "plib_adc${ADC_INDEX}.h"
<#compress>
<#assign ADC_CTRLC_VAL = "">
<#assign ADC_EVCTRL_VAL = "">
<#if ADC_CTRLC_DIFFMODE == true>
    <#assign ADC_CTRLC_VAL = "ADC_CTRLC_DIFFMODE_Msk">
</#if>
<#if ADC_CTRLC_LEFTADJ == true>
    <#if ADC_CTRLC_VAL != "">
        <#assign ADC_CTRLC_VAL = ADC_CTRLC_VAL + " | ADC_CTRLC_LEFTADJ_Msk">
    <#else>
        <#assign ADC_CTRLC_VAL = "ADC_CTRLC_LEFTADJ_Msk">
    </#if>
</#if>
<#if ADC_CONV_TRIGGER == "Free Run">
    <#if ADC_CTRLC_VAL != "">
        <#assign ADC_CTRLC_VAL = ADC_CTRLC_VAL + " | ADC_CTRLC_FREERUN_Msk">
    <#else>
        <#assign ADC_CTRLC_VAL = "ADC_CTRLC_FREERUN_Msk">
    </#if>
</#if>

<#if ADC_EVCTRL_RSERDYEO == true>
    <#if ADC_EVCTRL_VAL != "">
        <#assign ADC_EVCTRL_VAL = ADC_EVCTRL_VAL + " | ADC_EVCTRL_RESRDYEO_Msk">
    <#else>
        <#assign ADC_EVCTRL_VAL = "ADC_EVCTRL_RESRDYEO_Msk">
    </#if>
</#if>
<#if ADC_CONV_TRIGGER == "HW Event Trigger" && ADC_CTRLA_SLAVEEN == false>
    <#if ADC_EVCTRL_VAL != "">
        <#assign ADC_EVCTRL_VAL = ADC_EVCTRL_VAL + " | ADC_EVCTRL_FLUSHEI_Msk">
    <#else>
        <#assign ADC_EVCTRL_VAL = "ADC_EVCTRL_FLUSHEI_Msk">
    </#if>
</#if>
<#if ADC_CONV_TRIGGER == "HW Event Trigger" && ADC_CTRLA_SLAVEEN == false && ADC_EVCTRL_FLUSHINV == true>
    <#if ADC_EVCTRL_VAL != "">
        <#assign ADC_EVCTRL_VAL = ADC_EVCTRL_VAL + " | ADC_EVCTRL_FLUSHINV_Msk">
    <#else>
        <#assign ADC_EVCTRL_VAL = "ADC_EVCTRL_FLUSHINV_Msk">
    </#if>
</#if>
</#compress>

// *****************************************************************************
// *****************************************************************************
// Section: Global Data
// *****************************************************************************
// *****************************************************************************

<#if ADC_INTENSET_RESRDY = true>
ADC_CALLBACK_OBJ ADC${ADC_INDEX}_CallbackObject;
</#if>

// *****************************************************************************
// *****************************************************************************
// Section: ADC${ADC_INDEX} Implementation
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Initialize ADC module */
void ADC${ADC_INDEX}_Initialize( void )
{
    /* Reset ADC */
    ADC${ADC_INDEX}_REGS->ADC_CTRLA = ADC_CTRLA_SWRST_Msk;

    while((ADC${ADC_INDEX}_REGS->ADC_SYNCBUSY & ADC_SYNCBUSY_SWRST_Msk) == ADC_SYNCBUSY_SWRST_Msk)
    {
        /* Wait for Synchronization */
    }

<#if ADC_CTRLA_SLAVEEN == true>
    ADC${ADC_INDEX}_REGS->ADC_CTRLA |= ADC_CTRLA_SLAVEEN_Msk;
<#else>
    /* prescaler */
    ADC${ADC_INDEX}_REGS->ADC_CTRLB = ADC_CTRLB_PRESCALER_${ADC_CTRLB_PRESCALER};
</#if>
    /* Sampling length */
    ADC${ADC_INDEX}_REGS->ADC_SAMPCTRL = ADC_SAMPCTRL_SAMPLEN(${ADC_SAMPCTRL_SAMPLEN}U);

    /* reference */
    ADC${ADC_INDEX}_REGS->ADC_REFCTRL = ADC_REFCTRL_REFSEL_${ADC_REFCTRL_REFSEL};

    /* positive and negative input pins */
    ADC${ADC_INDEX}_REGS->ADC_INPUTCTRL = ADC_POSINPUT_${ADC_INPUTCTRL_MUXPOS} | ADC_NEGINPUT_${ADC_INPUTCTRL_MUXNEG};

    while((ADC${ADC_INDEX}_REGS->ADC_SYNCBUSY & ADC_SYNCBUSY_INPUTCTRL_Msk) == ADC_SYNCBUSY_INPUTCTRL_Msk)
    {
        /* Wait for Synchronization */
    }

    /* Resolution & Operation Mode */
    <@compress single_line=true>ADC${ADC_INDEX}_REGS->ADC_CTRLC = ADC_CTRLC_RESSEL_${ADC_CTRLC_RESSEL}
                                     <#if ADC_CTRLC_VAL?has_content>| ${ADC_CTRLC_VAL}</#if>;</@compress>

    while((ADC${ADC_INDEX}_REGS->ADC_SYNCBUSY & ADC_SYNCBUSY_CTRLC_Msk) == ADC_SYNCBUSY_CTRLC_Msk)
    {
        /* Wait for Synchronization */
    }

<#if ADC_CTRLC_RESSEL == "16BIT">
    /* Result averaging */
    ADC${ADC_INDEX}_REGS->ADC_AVGCTRL = ADC_AVGCTRL_SAMPLENUM_${ADC_AVGCTRL_SAMPLENUM} | ADC_AVGCTRL_ADJRES(${ADC_AVGCTRL_ADJRES});
</#if>

    /* Clear all interrupt flags */
    ADC${ADC_INDEX}_REGS->ADC_INTFLAG = ADC_INTFLAG_Msk;

<#if ADC_INTENSET_RESRDY = true>
    /* Enable RESRDY interrupt */
    ADC${ADC_INDEX}_REGS->ADC_INTENSET = ADC_INTENSET_RESRDY_Msk;
</#if>

<#if ADC_EVCTRL_VAL?has_content>
    /* events  */
    ADC${ADC_INDEX}_REGS->ADC_EVCTRL = ${ADC_EVCTRL_VAL};
</#if>

    /* Enable ADC & Configure run in standby and on demand */
    <@compress single_line=true>ADC${ADC_INDEX}_REGS->ADC_CTRLA = ADC_CTRLA_ENABLE_Msk
                                      ${ADC_CTRLA_RUNSTDBY?then('| ADC_CTRLA_RUNSTDBY_Msk', '')}
                                      ${ADC_CTRLA_ONDEMAND?then('| ADC_CTRLA_ONDEMAND_Msk', '')};</@compress>

    while((ADC${ADC_INDEX}_REGS->ADC_SYNCBUSY & ADC_SYNCBUSY_ENABLE_Msk) == ADC_SYNCBUSY_ENABLE_Msk)
    {
        /* Wait for Synchronization */
    }
}

/* Configure channel input */
void ADC${ADC_INDEX}_ChannelSelect( ADC_POSINPUT positiveInput, ADC_NEGINPUT negativeInput )
{
    /* Configure pin scan mode and positive and negative input pins */
    ADC${ADC_INDEX}_REGS->ADC_INPUTCTRL = positiveInput | negativeInput;

    while((ADC${ADC_INDEX}_REGS->ADC_SYNCBUSY & ADC_SYNCBUSY_INPUTCTRL_Msk) == ADC_SYNCBUSY_INPUTCTRL_Msk)
    {
        /* Wait for Synchronization */
    }
}

/* Start the ADC conversion by SW */
void ADC${ADC_INDEX}_ConversionStart( void )
{
    /* Start conversion */
    ADC${ADC_INDEX}_REGS->ADC_SWTRIG |= ADC_SWTRIG_START_Msk;

    while((ADC${ADC_INDEX}_REGS->ADC_SYNCBUSY & ADC_SYNCBUSY_SWTRIG_Msk) == ADC_SYNCBUSY_SWTRIG_Msk)
    {
        /* Wait for Synchronization */
    }
}

/* Check whether result is ready */
bool ADC${ADC_INDEX}_ConversionStatusGet( void )
{
    return (bool)((ADC${ADC_INDEX}_REGS->ADC_INTFLAG & ADC_INTFLAG_RESRDY_Msk) == ADC_INTFLAG_RESRDY_Msk);
}

/* Read the conversion result */
uint16_t ADC${ADC_INDEX}_ConversionResultGet( void )
{
    return (uint16_t)ADC${ADC_INDEX}_REGS->ADC_RESULT;
}

<#if ADC_INTENSET_RESRDY = true>
/* Register callback function */
void ADC${ADC_INDEX}_CallbackRegister( ADC_CALLBACK callback, uintptr_t context )
{
    ADC${ADC_INDEX}_CallbackObject.callback = callback;

    ADC${ADC_INDEX}_CallbackObject.context = context;
}


void ADC${ADC_INDEX}_InterruptHandler( void )
{
    if (ADC${ADC_INDEX}_CallbackObject.callback != NULL)
    {
        ADC${ADC_INDEX}_CallbackObject.callback(ADC${ADC_INDEX}_CallbackObject.context);
    }
}
</#if>



