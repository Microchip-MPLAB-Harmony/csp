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
<#assign DSEQCTRL_0_BIT =  "ADC_DSEQCTRL_INPUTCTRL_Msk">
<#assign DSEQCTRL_1_BIT =  "ADC_DSEQCTRL_CTRLB_Msk">
<#assign DSEQCTRL_2_BIT =  "ADC_DSEQCTRL_REFCTRL_Msk">
<#assign DSEQCTRL_3_BIT =  "ADC_DSEQCTRL_AVGCTRL_Msk">
<#assign DSEQCTRL_4_BIT =  "ADC_DSEQCTRL_SAMPCTRL_Msk">
<#assign DSEQCTRL_5_BIT =  "ADC_DSEQCTRL_WINLT_Msk">
<#assign DSEQCTRL_6_BIT =  "ADC_DSEQCTRL_WINUT_Msk">
<#assign DSEQCTRL_7_BIT =  "ADC_DSEQCTRL_GAINCORR_Msk">
<#assign DSEQCTRL_8_BIT =  "ADC_DSEQCTRL_OFFSETCORR_Msk">
<#assign DSEQCTRL_9_BIT =  "ADC_DSEQCTRL_AUTOSTART_Msk">
<#assign ADC_CTRLB_VAL = "">
<#assign ADC_INPUTCTRL_VAL = "">
<#assign ADC_SEQCTRL_VAL = "">
<#assign ADC_EVCTRL_VAL = "">
<#assign ADC_INTENSET_VAL = "">
<#assign ADC_CTRLA_VAL = "">
<#if ADC_INPUTCTRL_MUXNEG != "GND">
    <#assign ADC_INPUTCTRL_VAL = "ADC_INPUTCTRL_DIFFMODE_Msk">
</#if>
<#if ADC_CTRLB_LEFTADJ == true>
    <#if ADC_CTRLB_VAL != "">
        <#assign ADC_CTRLB_VAL = ADC_CTRLB_VAL + " | ADC_CTRLB_LEFTADJ_Msk">
    <#else>
        <#assign ADC_CTRLB_VAL = "ADC_CTRLB_LEFTADJ_Msk">
    </#if>
</#if>
<#if ADC_CTRLA_SLAVEEN == false>
<#if ADC_CONV_TRIGGER == "Free Run">
    <#if ADC_CTRLB_VAL != "">
        <#assign ADC_CTRLB_VAL = ADC_CTRLB_VAL + " | ADC_CTRLB_FREERUN_Msk">
    <#else>
        <#assign ADC_CTRLB_VAL = "ADC_CTRLB_FREERUN_Msk">
    </#if>
</#if>
</#if>

<#if ADC_SEQ_ENABLE == true>
    <#list 0..ADC_NUM_CHANNELS-1 as i>
        <#assign ADC_SEQCTRL = "ADC_SEQCTRL_SEQ" + i>
        <#if .vars[ADC_SEQCTRL] == true>
            <#if ADC_SEQCTRL_VAL != "">
                <#assign ADC_SEQCTRL_VAL = ADC_SEQCTRL_VAL + "\n\t\t | " + .vars["DSEQCTRL_" + i +"_BIT"]>
            <#else>
                <#assign ADC_SEQCTRL_VAL = .vars["DSEQCTRL_" + i + "_BIT"]>
            </#if>
        </#if>
    </#list>
</#if>

<#if ADC_EVCTRL_RESRDYEO == true>
    <#if ADC_EVCTRL_VAL != "">
        <#assign ADC_EVCTRL_VAL = ADC_EVCTRL_VAL + " | ADC_EVCTRL_RESRDYEO_Msk">
    <#else>
        <#assign ADC_EVCTRL_VAL = "ADC_EVCTRL_RESRDYEO_Msk">
    </#if>
</#if>
<#if ADC_CTRLB_WINMODE != "0" && ADC_WINDOW_OUTPUT_EVENT == true>
    <#if ADC_EVCTRL_VAL != "">
        <#assign ADC_EVCTRL_VAL = ADC_EVCTRL_VAL + " | ADC_EVCTRL_WINMONEO_Msk">
    <#else>
        <#assign ADC_EVCTRL_VAL = "ADC_EVCTRL_WINMONEO_Msk">
    </#if>
</#if>

<#if ADC_CONV_TRIGGER == "HW Event Trigger" && ADC_CTRLA_SLAVEEN == false>
    <#if ADC_EVCTRL_FLUSH == "1">
        <#if ADC_EVCTRL_VAL != "">
            <#assign ADC_EVCTRL_VAL = ADC_EVCTRL_VAL + " | ADC_EVCTRL_FLUSHEI_Msk">
        <#else>
            <#assign ADC_EVCTRL_VAL = "ADC_EVCTRL_FLUSHEI_Msk">
        </#if>
    <#elseif ADC_EVCTRL_FLUSH == "2">
        <#if ADC_EVCTRL_VAL != "">
            <#assign ADC_EVCTRL_VAL = ADC_EVCTRL_VAL + " | ADC_EVCTRL_FLUSHEI_Msk | ADC_EVCTRL_FLUSHINV_Msk">
        <#else>
            <#assign ADC_EVCTRL_VAL = "ADC_EVCTRL_FLUSHEI_Msk | ADC_EVCTRL_FLUSHINV_Msk">
        </#if>
    </#if>
    <#if ADC_EVCTRL_START == "1">
        <#if ADC_EVCTRL_VAL != "">
            <#assign ADC_EVCTRL_VAL = ADC_EVCTRL_VAL + " | ADC_EVCTRL_STARTEI_Msk">
        <#else>
            <#assign ADC_EVCTRL_VAL = "ADC_EVCTRL_STARTEI_Msk">
        </#if>
    <#elseif ADC_EVCTRL_START == "2">
        <#if ADC_EVCTRL_VAL != "">
            <#assign ADC_EVCTRL_VAL = ADC_EVCTRL_VAL + " | ADC_EVCTRL_STARTEI_Msk | ADC_EVCTRL_STARTINV_Msk">
        <#else>
            <#assign ADC_EVCTRL_VAL = "ADC_EVCTRL_STARTEI_Msk | ADC_EVCTRL_STARTINV_Msk">
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
<#if ADC_CTRLB_WINMODE != "0" && ADC_INTENSET_WINMON == true>
    <#if ADC_INTENSET_VAL != "">
        <#assign ADC_INTENSET_VAL = ADC_INTENSET_VAL + " | ADC_INTENSET_WINMON_Msk">
    <#else>
        <#assign ADC_INTENSET_VAL = "ADC_INTENSET_WINMON_Msk">
    </#if>
</#if>
<#if ADC_CTRLA_RUNSTDBY == true>
    <#assign ADC_CTRLA_VAL = "ADC_CTRLA_RUNSTDBY_Msk">
</#if>
<#if ADC_CTRLA_ONDEMAND == true>
    <#if ADC_CTRLA_VAL != "">
        <#assign ADC_CTRLA_VAL = ADC_CTRLA_VAL + " | ADC_CTRLA_ONDEMAND_Msk">
    <#else>
        <#assign ADC_CTRLA_VAL = "ADC_CTRLA_ONDEMAND_Msk">
    </#if>
</#if>
</#compress>

// *****************************************************************************
// *****************************************************************************
// Section: Global Data
// *****************************************************************************
// *****************************************************************************
<#if ADC_INTENSET_RESRDY = true || (ADC_CTRLB_WINMODE != "0" && ADC_INTENSET_WINMON = true)>
ADC_CALLBACK_OBJ ${ADC_INSTANCE_NAME}_CallbackObject;
</#if>

<#if ADC_INSTANCE_NAME = "ADC0">
#define ${ADC_INSTANCE_NAME}_BIASCOMP_POS  (2)
#define ${ADC_INSTANCE_NAME}_BIASCOMP_Msk   (0x7 << ${ADC_INSTANCE_NAME}_BIASCOMP_POS)

#define ${ADC_INSTANCE_NAME}_BIASREFBUF_POS  (5)
#define ${ADC_INSTANCE_NAME}_BIASREFBUF_Msk   (0x7 << ${ADC_INSTANCE_NAME}_BIASREFBUF_POS)

#define ${ADC_INSTANCE_NAME}_BIASR2R_POS  (8)
#define ${ADC_INSTANCE_NAME}_BIASR2R_Msk   (0x7 << ${ADC_INSTANCE_NAME}_BIASR2R_POS)

<#elseif ADC_INSTANCE_NAME = "ADC1">
#define ${ADC_INSTANCE_NAME}_BIASCOMP_POS  (16)
#define ${ADC_INSTANCE_NAME}_BIASCOMP_Msk   (0x7 << ${ADC_INSTANCE_NAME}_BIASCOMP_POS)

#define ${ADC_INSTANCE_NAME}_BIASREFBUF_POS  (19)
#define ${ADC_INSTANCE_NAME}_BIASREFBUF_Msk   (0x7 << ${ADC_INSTANCE_NAME}_BIASREFBUF_POS)

#define ${ADC_INSTANCE_NAME}_BIASR2R_POS  (22)
#define ${ADC_INSTANCE_NAME}_BIASR2R_Msk   (0x7 << ${ADC_INSTANCE_NAME}_BIASR2R_POS)
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

    /* Writing calibration values in BIASREFBUF, BIASCOMP and BIASR2R */
    ${ADC_INSTANCE_NAME}_REGS->ADC_CALIB =(uint32_t)(ADC_CALIB_BIASCOMP((((*(uint64_t*)SW0_ADDR) & ${ADC_INSTANCE_NAME}_BIASCOMP_Msk) >> ${ADC_INSTANCE_NAME}_BIASCOMP_POS))) \
            | ADC_CALIB_BIASR2R((((*(uint64_t*)SW0_ADDR) & ${ADC_INSTANCE_NAME}_BIASR2R_Msk) >> ${ADC_INSTANCE_NAME}_BIASR2R_POS))
            | ADC_CALIB_BIASREFBUF(((*(uint64_t*)SW0_ADDR) & ${ADC_INSTANCE_NAME}_BIASREFBUF_Msk)>> ${ADC_INSTANCE_NAME}_BIASREFBUF_POS );

<#if ADC_CTRLA_SLAVEEN == true>
    ${ADC_INSTANCE_NAME}_REGS->ADC_CTRLA = ADC_CTRLA_SLAVEEN_Msk;
<#else>
    /* prescaler */
    ${ADC_INSTANCE_NAME}_REGS->ADC_CTRLA = ADC_CTRLA_PRESCALER_${ADC_CTRLA_PRESCALER};
</#if>

    /* Sampling length */
    ${ADC_INSTANCE_NAME}_REGS->ADC_SAMPCTRL = ADC_SAMPCTRL_SAMPLEN(${ADC_SAMPCTRL_SAMPLEN - 1}U);

    /* reference */
    ${ADC_INSTANCE_NAME}_REGS->ADC_REFCTRL = ADC_REFCTRL_REFSEL_${ADC_REFCTRL_REFSEL};

<#if ADC_SEQCTRL_VAL?has_content>
    ${ADC_INSTANCE_NAME}_REGS->ADC_DSEQCTRL = ${ADC_SEQCTRL_VAL};
</#if>

    /* positive and negative input pins */
    <@compress single_line=true>${ADC_INSTANCE_NAME}_REGS->ADC_INPUTCTRL = ADC_POSINPUT_${ADC_INPUTCTRL_MUXPOS} | ADC_NEGINPUT_${ADC_INPUTCTRL_MUXNEG}
                                               <#if ADC_INPUTCTRL_VAL?has_content>| ${ADC_INPUTCTRL_VAL}</#if>;</@compress>

    /* Resolution & Operation Mode */
    <@compress single_line=true>${ADC_INSTANCE_NAME}_REGS->ADC_CTRLB = ADC_CTRLB_RESSEL_${ADC_CTRLB_RESSEL} | ADC_CTRLB_WINMODE(${ADC_CTRLB_WINMODE})
                                     <#if ADC_CTRLB_VAL?has_content>| ${ADC_CTRLB_VAL}</#if>;</@compress>

<#if ADC_CTRLB_RESSEL == "16BIT">
    /* Result averaging */
    ${ADC_INSTANCE_NAME}_REGS->ADC_AVGCTRL = ADC_AVGCTRL_SAMPLENUM_${ADC_AVGCTRL_SAMPLENUM} | ADC_AVGCTRL_ADJRES(${ADC_AVGCTRL_ADJRES});
</#if>

<#if ADC_CTRLB_WINMODE != "0">
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
<#if ADC_EVCTRL_VAL?has_content && ADC_CTRLA_SLAVEEN == false>
    /* Events configuration  */
    ${ADC_INSTANCE_NAME}_REGS->ADC_EVCTRL = ${ADC_EVCTRL_VAL};
</#if>

<#if ADC_CTRLA_VAL?has_content>
    <@compress single_line=true>${ADC_INSTANCE_NAME}_REGS->ADC_CTRLA |= ${ADC_CTRLA_VAL};</@compress>
</#if>
    while(${ADC_INSTANCE_NAME}_REGS->ADC_SYNCBUSY)
    {
        /* Wait for Synchronization */
    }
}

/* Enable ADC module */
void ${ADC_INSTANCE_NAME}_Enable( void )
{
    ${ADC_INSTANCE_NAME}_REGS->ADC_CTRLA |= ADC_CTRLA_ENABLE_Msk;
    while(${ADC_INSTANCE_NAME}_REGS->ADC_SYNCBUSY)
    {
        /* Wait for Synchronization */
    }
}

/* Disable ADC module */
void ${ADC_INSTANCE_NAME}_Disable( void )
{
    ${ADC_INSTANCE_NAME}_REGS->ADC_CTRLA &= ~ADC_CTRLA_ENABLE_Msk;
    while(${ADC_INSTANCE_NAME}_REGS->ADC_SYNCBUSY)
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

/* Configure window comparison threshold values */
void ${ADC_INSTANCE_NAME}_ComparisonWindowSet(uint16_t low_threshold, uint16_t high_threshold)
{
    ${ADC_INSTANCE_NAME}_REGS->ADC_WINLT = low_threshold;
    ${ADC_INSTANCE_NAME}_REGS->ADC_WINUT = high_threshold;
    while((${ADC_INSTANCE_NAME}_REGS->ADC_SYNCBUSY))
    {
        /* Wait for Synchronization */
    }
}

void ${ADC_INSTANCE_NAME}_WindowModeSet(ADC_WINMODE mode)
{
    ${ADC_INSTANCE_NAME}_REGS->ADC_CTRLB &= ~ADC_CTRLB_WINMODE_Msk;
    ${ADC_INSTANCE_NAME}_REGS->ADC_CTRLB |= mode << ADC_CTRLB_WINMODE_Pos;
    while((${ADC_INSTANCE_NAME}_REGS->ADC_SYNCBUSY))
    {
        /* Wait for Synchronization */
    }
}

/* Read the conversion result */
uint16_t ${ADC_INSTANCE_NAME}_ConversionResultGet( void )
{
    return (uint16_t)${ADC_INSTANCE_NAME}_REGS->ADC_RESULT;
}

/* Read the last conversion result */
uint16_t ${ADC_INSTANCE_NAME}_LastConversionResultGet( void )
{
    return (uint16_t)${ADC_INSTANCE_NAME}_REGS->ADC_RESS;
}

<#if ADC_INTENSET_RESRDY == true || (ADC_INTENSET_WINMON == true && ADC_CTRLB_WINMODE != "0")>
/* Register callback function */
void ${ADC_INSTANCE_NAME}_CallbackRegister( ADC_CALLBACK callback, uintptr_t context )
{
    ${ADC_INSTANCE_NAME}_CallbackObject.callback = callback;

    ${ADC_INSTANCE_NAME}_CallbackObject.context = context;
}

<#if ADC_INTENSET_RESRDY = true>
void ${ADC_INSTANCE_NAME}_RESRDY_InterruptHandler( void )
{
    volatile ADC_STATUS status;
    status = ${ADC_INSTANCE_NAME}_REGS->ADC_INTFLAG & ADC_INTFLAG_RESRDY_Msk;
    /* Clear interrupt flag */
    ${ADC_INSTANCE_NAME}_REGS->ADC_INTFLAG = ADC_INTFLAG_RESRDY_Msk;
    if (${ADC_INSTANCE_NAME}_CallbackObject.callback != NULL)
    {
        ${ADC_INSTANCE_NAME}_CallbackObject.callback(status, ${ADC_INSTANCE_NAME}_CallbackObject.context);
    }
}
<#else>
/* Check whether result is ready */
bool ${ADC_INSTANCE_NAME}_ConversionStatusGet( void )
{
    bool status;
    status =  (bool)((${ADC_INSTANCE_NAME}_REGS->ADC_INTFLAG & ADC_INTFLAG_RESRDY_Msk) >> ADC_INTFLAG_RESRDY_Pos);
    /* Clear interrupt flag */
    ${ADC_INSTANCE_NAME}_REGS->ADC_INTFLAG = ADC_INTFLAG_RESRDY_Msk;
    return status;
}
</#if>
<#if ADC_INTENSET_WINMON = true && ADC_CTRLB_WINMODE != "0">
void ${ADC_INSTANCE_NAME}_OTHER_InterruptHandler( void )
{
    volatile ADC_STATUS status;
    status = ${ADC_INSTANCE_NAME}_REGS->ADC_INTFLAG;
    /* Clear interrupt flag */
    ${ADC_INSTANCE_NAME}_REGS->ADC_INTFLAG = ADC_INTFLAG_WINMON_Msk | ADC_INTFLAG_OVERRUN_Msk;
    if (${ADC_INSTANCE_NAME}_CallbackObject.callback != NULL)
    {
        ${ADC_INSTANCE_NAME}_CallbackObject.callback(status, ${ADC_INSTANCE_NAME}_CallbackObject.context);
    }
}
<#else>
<#if ADC_CTRLB_WINMODE != "0">
/* Check whether window monitor result is ready */
bool ${ADC_INSTANCE_NAME}_WindowMonitorStatusGet( void )
{
    volatile bool status;
    status = (bool)((${ADC_INSTANCE_NAME}_REGS->ADC_INTFLAG & ADC_INTFLAG_WINMON_Msk) >> ADC_INTFLAG_WINMON_Pos);
    /* Clear interrupt flag */
    ${ADC_INSTANCE_NAME}_REGS->ADC_INTFLAG = ADC_INTFLAG_WINMON_Msk;

    return (status);
}
</#if>
</#if>
<#else>
/* Check whether result is ready */
bool ${ADC_INSTANCE_NAME}_ConversionStatusGet( void )
{
    bool status;
    status =  (bool)((${ADC_INSTANCE_NAME}_REGS->ADC_INTFLAG & ADC_INTFLAG_RESRDY_Msk) >> ADC_INTFLAG_RESRDY_Pos);
    if (status == true)
    {
        /* Clear interrupt flag */
        ${ADC_INSTANCE_NAME}_REGS->ADC_INTFLAG = ADC_INTFLAG_RESRDY_Msk;
    }
    return status;
}

<#if ADC_CTRLB_WINMODE != "0" && ADC_INTENSET_WINMON == false>
/* Check whether window monitor result is ready */
bool ${ADC_INSTANCE_NAME}_WindowMonitorStatusGet( void )
{
    volatile bool status;
    status = (bool)((${ADC_INSTANCE_NAME}_REGS->ADC_INTFLAG & ADC_INTFLAG_WINMON_Msk) >> ADC_INTFLAG_WINMON_Pos);
    if (status == true)
    {
        /* Clear interrupt flag */
        ${ADC_INSTANCE_NAME}_REGS->ADC_INTFLAG = ADC_INTFLAG_WINMON_Msk;
    }
    return (status);
}
</#if>
</#if>
