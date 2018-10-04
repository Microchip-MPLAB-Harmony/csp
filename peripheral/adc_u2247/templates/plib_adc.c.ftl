/*******************************************************************************
  Analog-to-Digital Converter(${ADC_INSTANCE_NAME}) PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_${ADC_INSTANCE_NAME?lower_case}.c

  Summary
    ${ADC_INSTANCE_NAME} PLIB Implementation File.

  Description
    This file defines the interface to the ADC peripheral library. This
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

#include "plib_${ADC_INSTANCE_NAME?lower_case}.h"
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
ADC_CALLBACK_OBJ ${ADC_INSTANCE_NAME}_CallbackObject;
</#if>

// *****************************************************************************
// *****************************************************************************
// Section: ${ADC_INSTANCE_NAME} Implementation
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Initialize ADC module */
void ${ADC_INSTANCE_NAME}_Initialize( void )
{
    /* Reset ADC */
    ${ADC_INSTANCE_NAME}_REGS->ADC_CTRLA = ADC_CTRLA_SWRST_Msk;

    while((${ADC_INSTANCE_NAME}_REGS->ADC_SYNCBUSY & ADC_SYNCBUSY_SWRST_Msk) == ADC_SYNCBUSY_SWRST_Msk)
    {
        /* Wait for Synchronization */
    }

<#if ADC_CTRLA_SLAVEEN == true>
    ${ADC_INSTANCE_NAME}_REGS->ADC_CTRLA |= ADC_CTRLA_SLAVEEN_Msk;
<#else>
    /* prescaler */
    ${ADC_INSTANCE_NAME}_REGS->ADC_CTRLB = ADC_CTRLB_PRESCALER_${ADC_CTRLB_PRESCALER};
</#if>
    /* Sampling length */
    ${ADC_INSTANCE_NAME}_REGS->ADC_SAMPCTRL = ADC_SAMPCTRL_SAMPLEN(${ADC_SAMPCTRL_SAMPLEN}U);

    /* reference */
    ${ADC_INSTANCE_NAME}_REGS->ADC_REFCTRL = ADC_REFCTRL_REFSEL_${ADC_REFCTRL_REFSEL};

    /* positive and negative input pins */
    ${ADC_INSTANCE_NAME}_REGS->ADC_INPUTCTRL = ADC_POSINPUT_${ADC_INPUTCTRL_MUXPOS} | ADC_NEGINPUT_${ADC_INPUTCTRL_MUXNEG};

    while((${ADC_INSTANCE_NAME}_REGS->ADC_SYNCBUSY & ADC_SYNCBUSY_INPUTCTRL_Msk) == ADC_SYNCBUSY_INPUTCTRL_Msk)
    {
        /* Wait for Synchronization */
    }

    /* Resolution & Operation Mode */
    <@compress single_line=true>${ADC_INSTANCE_NAME}_REGS->ADC_CTRLC = ADC_CTRLC_RESSEL_${ADC_CTRLC_RESSEL}
                                     <#if ADC_CTRLC_VAL?has_content>| ${ADC_CTRLC_VAL}</#if>;</@compress>

    while((${ADC_INSTANCE_NAME}_REGS->ADC_SYNCBUSY & ADC_SYNCBUSY_CTRLC_Msk) == ADC_SYNCBUSY_CTRLC_Msk)
    {
        /* Wait for Synchronization */
    }

<#if ADC_CTRLC_RESSEL == "16BIT">
    /* Result averaging */
    ${ADC_INSTANCE_NAME}_REGS->ADC_AVGCTRL = ADC_AVGCTRL_SAMPLENUM_${ADC_AVGCTRL_SAMPLENUM} | ADC_AVGCTRL_ADJRES(${ADC_AVGCTRL_ADJRES});
</#if>

    /* Clear all interrupt flags */
    ${ADC_INSTANCE_NAME}_REGS->ADC_INTFLAG = ADC_INTFLAG_Msk;

<#if ADC_INTENSET_RESRDY = true>
    /* Enable RESRDY interrupt */
    ${ADC_INSTANCE_NAME}_REGS->ADC_INTENSET = ADC_INTENSET_RESRDY_Msk;
</#if>

<#if ADC_EVCTRL_VAL?has_content>
    /* events  */
    ${ADC_INSTANCE_NAME}_REGS->ADC_EVCTRL = ${ADC_EVCTRL_VAL};
</#if>

    /* Enable ADC & Configure run in standby and on demand */
    <@compress single_line=true>${ADC_INSTANCE_NAME}_REGS->ADC_CTRLA = ADC_CTRLA_ENABLE_Msk
                                      ${ADC_CTRLA_RUNSTDBY?then('| ADC_CTRLA_RUNSTDBY_Msk', '')}
                                      ${ADC_CTRLA_ONDEMAND?then('| ADC_CTRLA_ONDEMAND_Msk', '')};</@compress>

    while((${ADC_INSTANCE_NAME}_REGS->ADC_SYNCBUSY & ADC_SYNCBUSY_ENABLE_Msk) == ADC_SYNCBUSY_ENABLE_Msk)
    {
        /* Wait for Synchronization */
    }
}

/* Configure channel input */
void ${ADC_INSTANCE_NAME}_ChannelSelect( ADC_POSINPUT positiveInput, ADC_NEGINPUT negativeInput )
{
    /* Configure pin scan mode and positive and negative input pins */
    ${ADC_INSTANCE_NAME}_REGS->ADC_INPUTCTRL = positiveInput | negativeInput;

    while((${ADC_INSTANCE_NAME}_REGS->ADC_SYNCBUSY & ADC_SYNCBUSY_INPUTCTRL_Msk) == ADC_SYNCBUSY_INPUTCTRL_Msk)
    {
        /* Wait for Synchronization */
    }
}

/* Start the ADC conversion by SW */
void ${ADC_INSTANCE_NAME}_ConversionStart( void )
{
    /* Start conversion */
    ${ADC_INSTANCE_NAME}_REGS->ADC_SWTRIG |= ADC_SWTRIG_START_Msk;

    while((${ADC_INSTANCE_NAME}_REGS->ADC_SYNCBUSY & ADC_SYNCBUSY_SWTRIG_Msk) == ADC_SYNCBUSY_SWTRIG_Msk)
    {
        /* Wait for Synchronization */
    }
}

/* Check whether result is ready */
bool ${ADC_INSTANCE_NAME}_ConversionStatusGet( void )
{
    return (bool)((${ADC_INSTANCE_NAME}_REGS->ADC_INTFLAG & ADC_INTFLAG_RESRDY_Msk) == ADC_INTFLAG_RESRDY_Msk);
}

/* Read the conversion result */
uint16_t ${ADC_INSTANCE_NAME}_ConversionResultGet( void )
{
    return (uint16_t)${ADC_INSTANCE_NAME}_REGS->ADC_RESULT;
}

<#if ADC_INTENSET_RESRDY = true>
/* Register callback function */
void ${ADC_INSTANCE_NAME}_CallbackRegister( ADC_CALLBACK callback, uintptr_t context )
{
    ${ADC_INSTANCE_NAME}_CallbackObject.callback = callback;

    ${ADC_INSTANCE_NAME}_CallbackObject.context = context;
}


void ${ADC_INSTANCE_NAME}_InterruptHandler( void )
{
    if (${ADC_INSTANCE_NAME}_CallbackObject.callback != NULL)
    {
        ${ADC_INSTANCE_NAME}_CallbackObject.callback(${ADC_INSTANCE_NAME}_CallbackObject.context);
    }
}
</#if>



