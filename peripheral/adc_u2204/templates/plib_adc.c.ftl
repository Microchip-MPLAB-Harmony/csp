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
<#assign ADC_CTRLB_VAL = "">
<#assign ADC_EVCTRL_VAL = "">
<#assign ADC_INTENSET_VAL = "">
<#if ADC_INPUTCTRL_MUXNEG != "GND">
    <#assign ADC_CTRLB_VAL = "ADC_CTRLB_DIFFMODE_Msk">
</#if>
<#if ADC_CTRLB_LEFTADJ == true>
    <#if ADC_CTRLB_VAL != "">
        <#assign ADC_CTRLB_VAL = ADC_CTRLB_VAL + " | ADC_CTRLB_LEFTADJ_Msk">
    <#else>
        <#assign ADC_CTRLB_VAL = "ADC_CTRLB_LEFTADJ_Msk">
    </#if>
</#if>
<#if ADC_CONV_TRIGGER == "Free Run">
    <#if ADC_CTRLB_VAL != "">
        <#assign ADC_CTRLB_VAL = ADC_CTRLB_VAL + " | ADC_CTRLB_FREERUN_Msk">
    <#else>
        <#assign ADC_CTRLB_VAL = "ADC_CTRLB_FREERUN_Msk">
    </#if>
</#if>

<#if ADC_EVCTRL_RESRDYEO == true>
    <#if ADC_EVCTRL_VAL != "">
        <#assign ADC_EVCTRL_VAL = ADC_EVCTRL_VAL + " | ADC_EVCTRL_RESRDYEO_Msk">
    <#else>
        <#assign ADC_EVCTRL_VAL = "ADC_EVCTRL_RESRDYEO_Msk">
    </#if>
</#if>
<#if ADC_WINCTRL_WINMODE != "DISABLE" && ADC_WINDOW_OUTPUT_EVENT == true>
    <#if ADC_EVCTRL_VAL != "">
        <#assign ADC_EVCTRL_VAL = ADC_EVCTRL_VAL + " | ADC_EVCTRL_WINMONEO_Msk">
    <#else>
        <#assign ADC_EVCTRL_VAL = "ADC_EVCTRL_WINMONEO_Msk">
    </#if>
</#if>

<#if ADC_CONV_TRIGGER == "HW Event Trigger">
    <#if ADC_EVCTRL_FLUSH == true>
        <#if ADC_EVCTRL_VAL != "">
            <#assign ADC_EVCTRL_VAL = ADC_EVCTRL_VAL + " | ADC_EVCTRL_SYNCEI_Msk">
        <#else>
            <#assign ADC_EVCTRL_VAL = "ADC_EVCTRL_SYNCEI_Msk">
        </#if>
    </#if>
    <#if ADC_EVCTRL_START == true>
        <#if ADC_EVCTRL_VAL != "">
            <#assign ADC_EVCTRL_VAL = ADC_EVCTRL_VAL + " | ADC_EVCTRL_STARTEI_Msk">
        <#else>
            <#assign ADC_EVCTRL_VAL = "ADC_EVCTRL_STARTEI_Msk">
        </#if>
    </#if>
</#if>

<#if ADC_INTENSET_RESRDY == true>
    <#if ADC_INTENSET_VAL != "">
        <#assign ADC_INTENSET_VAL = ADC_INTENSET_VAL + " | ADC_INTENSET_RESRDY_Msk">
    <#else>
        <#assign ADC_INTENSET_VAL = "ADC_INTENSET_RESRDY_Msk">
    </#if>
</#if>
<#if ADC_WINCTRL_WINMODE != "DISABLE" && ADC_INTENSET_WINMON == true>
    <#if ADC_INTENSET_VAL != "">
        <#assign ADC_INTENSET_VAL = ADC_INTENSET_VAL + " | ADC_INTENSET_WINMON_Msk">
    <#else>
        <#assign ADC_INTENSET_VAL = "ADC_INTENSET_WINMON_Msk">
    </#if>
</#if>
</#compress>

// *****************************************************************************
// *****************************************************************************
// Section: Global Data
// *****************************************************************************
// *****************************************************************************
<#if ADC_INTENSET_RESRDY = true || (ADC_WINCTRL_WINMODE != "DISABLE" && ADC_INTENSET_WINMON = true)>
ADC_CALLBACK_OBJ ${ADC_INSTANCE_NAME}_CallbackObject;
</#if>

<#if ADC_MCU_FAMILY == "SAMD">
#define ADC_LINEARITY0_POS  (27)
#define ADC_LINEARITY0_Msk   ((0x1F << ADC_LINEARITY0_POS))

#define ADC_LINEARITY1_POS  (0)
#define ADC_LINEARITY1_Msk   ((0x7 << ADC_LINEARITY1_POS))

#define ADC_BIASCAL_POS  (3)
#define ADC_BIASCAL_Msk   ((0x7 << ADC_BIASCAL_POS))
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

    while(${ADC_INSTANCE_NAME}_REGS->ADC_STATUS & ADC_STATUS_SYNCBUSY_Msk)
    {
        /* Wait for Synchronization */
    }

<#if ADC_MCU_FAMILY == "SAMD">
    uint32_t adc_linearity0 = (((*(uint64_t*)OTP4_ADDR) & ADC_LINEARITY0_Msk) >> ADC_LINEARITY0_POS);
    uint32_t adc_linearity1 = (((*(uint64_t*)OTP4_ADDR) & ADC_LINEARITY0_Msk) >> ADC_LINEARITY0_POS);

    /* Write linearity calibration and bias calibration */
    ADC_REGS->ADC_CALIB = (uint32_t)(ADC_CALIB_LINEARITY_CAL(adc_linearity0 | (adc_linearity1 << 5))) \
        | ADC_CALIB_BIAS_CAL((((*(uint64_t*)OTP4_ADDR + 1) & ADC_BIASCAL_Msk) >> ADC_BIASCAL_POS));

</#if>
    /* Sampling length */
    ${ADC_INSTANCE_NAME}_REGS->ADC_SAMPCTRL = ADC_SAMPCTRL_SAMPLEN(${ADC_SAMPCTRL_SAMPLEN - 1}U);

    /* reference */
    ${ADC_INSTANCE_NAME}_REGS->ADC_REFCTRL = ADC_REFCTRL_REFSEL_${ADC_REFCTRL_REFSEL};

    /* positive and negative input pins */
    ${ADC_INSTANCE_NAME}_REGS->ADC_INPUTCTRL = ADC_POSINPUT_${ADC_INPUTCTRL_MUXPOS} | ADC_NEGINPUT_${ADC_INPUTCTRL_MUXNEG} \
        | ADC_INPUTCTRL_INPUTSCAN(${ADC_INPUTCTRL_INPUTSCAN}) | ADC_INPUTCTRL_INPUTOFFSET(${ADC_INPUTCTRL_INPUTOFFSET}) | ADC_INPUTCTRL_GAIN_${ADC_INPUTCTRL_GAIN};

    /* Prescaler, Resolution & Operation Mode */
    <@compress single_line=true>${ADC_INSTANCE_NAME}_REGS->ADC_CTRLB = ADC_CTRLB_PRESCALER_${ADC_CTRLB_PRESCALER} | ADC_CTRLB_RESSEL_${ADC_CTRLB_RESSEL}
                                     <#if ADC_CTRLB_VAL?has_content>| ${ADC_CTRLB_VAL}</#if>;</@compress>

<#if ADC_CTRLB_RESSEL == "16BIT">
    /* Result averaging */
    ${ADC_INSTANCE_NAME}_REGS->ADC_AVGCTRL = ADC_AVGCTRL_SAMPLENUM_${ADC_AVGCTRL_SAMPLENUM} | ADC_AVGCTRL_ADJRES(${ADC_AVGCTRL_ADJRES});
</#if>

<#if ADC_WINCTRL_WINMODE != "DISABLE">
    /* Window mode configurations */
    ${ADC_INSTANCE_NAME}_REGS->ADC_WINCTRL = ADC_WINCTRL_WINMODE_${ADC_WINCTRL_WINMODE};
    /* Upper threshold for window mode  */
    ${ADC_INSTANCE_NAME}_REGS->ADC_WINUT = ${ADC_WINUT};
    /* Lower threshold for window mode  */
    ${ADC_INSTANCE_NAME}_REGS->ADC_WINLT = ${ADC_WINLT};
</#if>
    /* Clear all interrupt flags */
    ${ADC_INSTANCE_NAME}_REGS->ADC_INTFLAG = ADC_INTFLAG_Msk;
<#if ADC_INTENSET_VAL?has_content >
    /* Enable interrupts */
    ${ADC_INSTANCE_NAME}_REGS->ADC_INTENSET = ${ADC_INTENSET_VAL};
</#if>
<#if ADC_EVCTRL_VAL?has_content>
    /* Events configuration  */
    ${ADC_INSTANCE_NAME}_REGS->ADC_EVCTRL = ${ADC_EVCTRL_VAL};
</#if>

<#if ADC_CTRLA_RUNSTDBY == true>
    <@compress single_line=true>${ADC_INSTANCE_NAME}_REGS->ADC_CTRLA |=
                                      ${ADC_CTRLA_RUNSTDBY?then('ADC_CTRLA_RUNSTDBY_Msk', '')};</@compress>
</#if>
    while(${ADC_INSTANCE_NAME}_REGS->ADC_STATUS & ADC_STATUS_SYNCBUSY_Msk)
    {
        /* Wait for Synchronization */
    }
}

/* Enable ADC module */
void ${ADC_INSTANCE_NAME}_Enable( void )
{
    ${ADC_INSTANCE_NAME}_REGS->ADC_CTRLA |= ADC_CTRLA_ENABLE_Msk;
    while(${ADC_INSTANCE_NAME}_REGS->ADC_STATUS & ADC_STATUS_SYNCBUSY_Msk)
    {
        /* Wait for Synchronization */
    }
}

/* Disable ADC module */
void ${ADC_INSTANCE_NAME}_Disable( void )
{
    ${ADC_INSTANCE_NAME}_REGS->ADC_CTRLA &= ~ADC_CTRLA_ENABLE_Msk;
    while(${ADC_INSTANCE_NAME}_REGS->ADC_STATUS & ADC_STATUS_SYNCBUSY_Msk)
    {
        /* Wait for Synchronization */
    }
}

/* Configure channel input */
void ${ADC_INSTANCE_NAME}_ChannelSelect( ADC_POSINPUT positiveInput, ADC_NEGINPUT negativeInput )
{
    /* Configure pin scan mode and positive and negative input pins */
    ${ADC_INSTANCE_NAME}_REGS->ADC_INPUTCTRL = positiveInput | negativeInput;

    while(${ADC_INSTANCE_NAME}_REGS->ADC_STATUS & ADC_STATUS_SYNCBUSY_Msk)
    {
        /* Wait for Synchronization */
    }
}

/* Start the ADC conversion by SW */
void ${ADC_INSTANCE_NAME}_ConversionStart( void )
{
    /* Start conversion */
    ${ADC_INSTANCE_NAME}_REGS->ADC_SWTRIG |= ADC_SWTRIG_START_Msk;

    while(${ADC_INSTANCE_NAME}_REGS->ADC_STATUS & ADC_STATUS_SYNCBUSY_Msk)
    {
        /* Wait for Synchronization */
    }
}

/* Configure window comparison threshold values */
void ${ADC_INSTANCE_NAME}_ComparisonWindowSet(uint16_t low_threshold, uint16_t high_threshold)
{
    ${ADC_INSTANCE_NAME}_REGS->ADC_WINLT = low_threshold;
    ${ADC_INSTANCE_NAME}_REGS->ADC_WINUT = high_threshold;
    while(${ADC_INSTANCE_NAME}_REGS->ADC_STATUS & ADC_STATUS_SYNCBUSY_Msk)
    {
        /* Wait for Synchronization */
    }
}

void ${ADC_INSTANCE_NAME}_WindowModeSet(ADC_WINMODE mode)
{
    ${ADC_INSTANCE_NAME}_REGS->ADC_WINCTRL = mode << ADC_WINCTRL_WINMODE_Pos;
    while(${ADC_INSTANCE_NAME}_REGS->ADC_STATUS & ADC_STATUS_SYNCBUSY_Msk)
    {
        /* Wait for Synchronization */
    }
}


/* Read the conversion result */
uint16_t ${ADC_INSTANCE_NAME}_ConversionResultGet( void )
{
    return (uint16_t)${ADC_INSTANCE_NAME}_REGS->ADC_RESULT;
}

<#if ADC_INTENSET_RESRDY = true || (ADC_WINCTRL_WINMODE != "DISABLE" && ADC_INTENSET_WINMON = true)>
/* Register callback function */
void ${ADC_INSTANCE_NAME}_CallbackRegister( ADC_CALLBACK callback, uintptr_t context )
{
    ${ADC_INSTANCE_NAME}_CallbackObject.callback = callback;

    ${ADC_INSTANCE_NAME}_CallbackObject.context = context;
}


void ${ADC_INSTANCE_NAME}_InterruptHandler( void )
{
    volatile ADC_STATUS status;
    status = ${ADC_INSTANCE_NAME}_REGS->ADC_INTFLAG;
    /* Clear interrupt flag */
    ${ADC_INSTANCE_NAME}_REGS->ADC_INTFLAG =  ${ADC_INTENSET_VAL};
    if (${ADC_INSTANCE_NAME}_CallbackObject.callback != NULL)
    {
        ${ADC_INSTANCE_NAME}_CallbackObject.callback(status, ${ADC_INSTANCE_NAME}_CallbackObject.context);
    }
}
</#if>

<#if ADC_INTENSET_RESRDY == false>
/* Check whether result is ready */
bool ${ADC_INSTANCE_NAME}_ConversionStatusGet( void )
{
    bool status;
    status =  (bool)((${ADC_INSTANCE_NAME}_REGS->ADC_INTFLAG & ADC_INTFLAG_RESRDY_Msk) >> ADC_INTFLAG_RESRDY_Pos);
    if (status == true)
    {
        ${ADC_INSTANCE_NAME}_REGS->ADC_INTFLAG = ADC_INTFLAG_RESRDY_Msk;
    }
    return status;
}
</#if>
<#if ADC_WINCTRL_WINMODE != "DISABLE" && ADC_INTENSET_WINMON == false>
/* Check whether window monitor result is ready */
bool ${ADC_INSTANCE_NAME}_WindowMonitorStatusGet( void )
{
    bool status;
    status = (bool)((${ADC_INSTANCE_NAME}_REGS->ADC_INTFLAG & ADC_INTFLAG_WINMON_Msk) >> ADC_INTFLAG_WINMON_Pos);
    if (status == true)
    {
        ${ADC_INSTANCE_NAME}_REGS->ADC_INTFLAG = ADC_INTFLAG_WINMON_Msk;
    }
    return status;
}
</#if>
