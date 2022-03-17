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
* Copyright (C) 2019 Microchip Technology Inc. and its subsidiaries.
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

<#if core.CoreSysIntFile == true>
#include "interrupts.h"
</#if>
#include "plib_${ADC_INSTANCE_NAME?lower_case}.h"
<#compress>
<#assign ADC_CTRLC_VAL = "">
<#assign ADC_SEQCTRL_VAL = "">
<#assign ADC_EVCTRL_VAL = "">
<#assign ADC_INTENSET_VAL = "">
<#assign ADC_CTRLA_VAL = "">
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
<#if ADC_CTRLA_SLAVEEN == false>
<#if ADC_CONV_TRIGGER == "Free Run">
    <#if ADC_CTRLC_VAL != "">
        <#assign ADC_CTRLC_VAL = ADC_CTRLC_VAL + " | ADC_CTRLC_FREERUN_Msk">
    <#else>
        <#assign ADC_CTRLC_VAL = "ADC_CTRLC_FREERUN_Msk">
    </#if>
</#if>
</#if>

<#if ADC_CONV_TRIGGER != "Free Run" && ADC_SEQ_ENABLE == true>
    <#list 0..ADC_NUM_CHANNELS-1 as i>
        <#assign ADC_SEQCTRL = "ADC_SEQCTRL_SEQ" + i>
        <#if .vars[ADC_SEQCTRL]?has_content>
            <#if .vars[ADC_SEQCTRL] == true>
                <#if ADC_SEQCTRL_VAL != "">
                    <#assign ADC_SEQCTRL_VAL = ADC_SEQCTRL_VAL + "\n\t\t | " + "ADC_SEQCTRL_SEQEN(1U << " + i +"U)">
                <#else>
                    <#assign ADC_SEQCTRL_VAL = "ADC_SEQCTRL_SEQEN(1U << " + i +"U)">
                </#if>
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
<#if ADC_CTRLC_WINMODE != "0" && ADC_WINDOW_OUTPUT_EVENT == true>
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
<#if ADC_CTRLC_WINMODE != "0" && ADC_INTENSET_WINMON == true>
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
<#if ADC_INTENSET_RESRDY = true || (ADC_CTRLC_WINMODE != "0" && ADC_INTENSET_WINMON = true)>
static ADC_CALLBACK_OBJ ${ADC_INSTANCE_NAME}_CallbackObject;
</#if>

<#if ADC_LOAD_CALIB? has_content>
    <#if ADC_LOAD_CALIB == true >
        <#if ADC_INSTANCE_NAME = "ADC0">
            <#lt>#define ${ADC_INSTANCE_NAME}_LINEARITY_POS  (0U)
            <#lt>#define ${ADC_INSTANCE_NAME}_LINEARITY_Msk   (0x7UL << ${ADC_INSTANCE_NAME}_LINEARITY_POS)

            <#lt>#define ${ADC_INSTANCE_NAME}_BIASCAL_POS  (3U)
            <#lt>#define ${ADC_INSTANCE_NAME}_BIASCAL_Msk   (0x7UL << ${ADC_INSTANCE_NAME}_BIASCAL_POS)

        <#elseif ADC_INSTANCE_NAME = "ADC1">
            <#lt>#define ${ADC_INSTANCE_NAME}_LINEARITY_POS  (6U)
            <#lt>#define ${ADC_INSTANCE_NAME}_LINEARITY_Msk   (0x7UL << ${ADC_INSTANCE_NAME}_LINEARITY_POS)

            <#lt>#define ${ADC_INSTANCE_NAME}_BIASCAL_POS  (9U)
            <#lt>#define ${ADC_INSTANCE_NAME}_BIASCAL_Msk   (0x7UL << ${ADC_INSTANCE_NAME}_BIASCAL_POS)

        <#elseif ADC_INSTANCE_NAME = "ADC">
            <#lt>#define ${ADC_INSTANCE_NAME}_LINEARITY_POS  (0U)
            <#lt>#define ${ADC_INSTANCE_NAME}_LINEARITY_Msk   (0x7UL << ${ADC_INSTANCE_NAME}_LINEARITY_POS)

            <#lt>#define ${ADC_INSTANCE_NAME}_BIASCAL_POS  (3U)
            <#lt>#define ${ADC_INSTANCE_NAME}_BIASCAL_Msk   (0x7UL << ${ADC_INSTANCE_NAME}_BIASCAL_POS)
        </#if>
    </#if>
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
    ${ADC_INSTANCE_NAME}_REGS->ADC_CTRLA = (uint8_t)ADC_CTRLA_SWRST_Msk;

    while((${ADC_INSTANCE_NAME}_REGS->ADC_SYNCBUSY & ADC_SYNCBUSY_SWRST_Msk) == ADC_SYNCBUSY_SWRST_Msk)
    {
        /* Wait for Synchronization */
    }
<#if ADC_LOAD_CALIB? has_content>
    <#if ADC_LOAD_CALIB == true >
    <#lt>    /* Write linearity calibration in BIASREFBUF and bias calibration in BIASCOMP */
    <#lt>    uint32_t calib_low_word = (uint32_t)(*(uint64_t*)${ADC_NVM_CALIB_REG});
    <#lt>    ${ADC_INSTANCE_NAME}_REGS->ADC_CALIB = (uint16_t)((ADC_CALIB_BIASREFBUF((calib_low_word & ${ADC_INSTANCE_NAME}_LINEARITY_Msk) >> ${ADC_INSTANCE_NAME}_LINEARITY_POS)) | 
    <#lt>                                      (ADC_CALIB_BIASCOMP((calib_low_word & ${ADC_INSTANCE_NAME}_BIASCAL_Msk) >> ${ADC_INSTANCE_NAME}_BIASCAL_POS)));
    </#if>
</#if>

<#if ADC_CTRLA_SLAVEEN == true>
    ${ADC_INSTANCE_NAME}_REGS->ADC_CTRLA = (uint8_t)ADC_CTRLA_SLAVEEN_Msk;
<#else>
    /* Prescaler */
    ${ADC_INSTANCE_NAME}_REGS->ADC_CTRLB = (uint8_t)ADC_CTRLB_PRESCALER_${ADC_CTRLB_PRESCALER};
</#if>
    /* Sampling length */
    ${ADC_INSTANCE_NAME}_REGS->ADC_SAMPCTRL = (uint8_t)ADC_SAMPCTRL_SAMPLEN(${ADC_SAMPCTRL_SAMPLEN - 1}UL);

    /* Reference */
    ${ADC_INSTANCE_NAME}_REGS->ADC_REFCTRL = (uint8_t)ADC_REFCTRL_REFSEL_${ADC_REFCTRL_REFSEL};

<#if ADC_SEQCTRL_VAL?has_content>
    /*lint -e{9048} false positive about a missing 'U' literal */
    ${ADC_INSTANCE_NAME}_REGS->ADC_SEQCTRL = ${ADC_SEQCTRL_VAL};
<#else>
    <#if ADC_CTRLC_DIFFMODE == true>
    /* Positive and negative input pins */
    ${ADC_INSTANCE_NAME}_REGS->ADC_INPUTCTRL =  ((uint16_t)ADC_POSINPUT_${ADC_INPUTCTRL_MUXPOS} | (uint16_t)ADC_NEGINPUT_${ADC_INPUTCTRL_MUXNEG});
    <#else>
    /* Input pin */
    ${ADC_INSTANCE_NAME}_REGS->ADC_INPUTCTRL = (uint16_t) ADC_POSINPUT_${ADC_INPUTCTRL_MUXPOS};
    </#if>
</#if>

    /* Resolution & Operation Mode */
    <@compress single_line=true>${ADC_INSTANCE_NAME}_REGS->ADC_CTRLC = (uint16_t)(ADC_CTRLC_RESSEL_${ADC_CTRLC_RESSEL} | ADC_CTRLC_WINMODE(${ADC_CTRLC_WINMODE}UL)
                                     <#if ADC_CTRLC_VAL?has_content>| ${ADC_CTRLC_VAL}</#if>);</@compress>

<#if ADC_CTRLC_RESSEL == "16BIT">
    /* Result averaging */
    ${ADC_INSTANCE_NAME}_REGS->ADC_AVGCTRL = (uint8_t)(ADC_AVGCTRL_SAMPLENUM(${ADC_SAMPLENUM}UL) | ADC_AVGCTRL_ADJRES(${ADC_ADJRES}UL));
</#if>

<#if ADC_CTRLC_WINMODE != "0">
    /* Upper threshold for window mode  */
    ${ADC_INSTANCE_NAME}_REGS->ADC_WINUT = (uint16_t)(${ADC_WINUT});
    /* Lower threshold for window mode  */
    ${ADC_INSTANCE_NAME}_REGS->ADC_WINLT = (uint16_t)(${ADC_WINLT});
</#if>
    /* Clear all interrupt flags */
    ${ADC_INSTANCE_NAME}_REGS->ADC_INTFLAG = (uint8_t)ADC_INTFLAG_Msk;
<#if ADC_INTENSET_VAL?has_content >
    /* Enable interrupts */
    ${ADC_INSTANCE_NAME}_REGS->ADC_INTENSET = (uint8_t)(${ADC_INTENSET_VAL});
</#if>
<#if ADC_EVCTRL_VAL?has_content && ADC_CTRLA_SLAVEEN == false>
    /* Events configuration  */
    ${ADC_INSTANCE_NAME}_REGS->ADC_EVCTRL = (uint8_t)(${ADC_EVCTRL_VAL});
</#if>

<#if ADC_CTRLA_VAL?has_content>
    <@compress single_line=true>${ADC_INSTANCE_NAME}_REGS->ADC_CTRLA |= (uint8_t)(${ADC_CTRLA_VAL});</@compress>
</#if>
    while(0U != ${ADC_INSTANCE_NAME}_REGS->ADC_SYNCBUSY)
    {
        /* Wait for Synchronization */
    }
}

/* Enable ADC module */
void ${ADC_INSTANCE_NAME}_Enable( void )
{
    ${ADC_INSTANCE_NAME}_REGS->ADC_CTRLA |= (uint8_t)ADC_CTRLA_ENABLE_Msk;
    while(0U != ${ADC_INSTANCE_NAME}_REGS->ADC_SYNCBUSY)
    {
        /* Wait for Synchronization */
    }
}

/* Disable ADC module */
void ${ADC_INSTANCE_NAME}_Disable( void )
{
    ${ADC_INSTANCE_NAME}_REGS->ADC_CTRLA &= (uint8_t)(~ADC_CTRLA_ENABLE_Msk);
    while(0U != ${ADC_INSTANCE_NAME}_REGS->ADC_SYNCBUSY)
    {
        /* Wait for Synchronization */
    }
}

/* Configure channel input */
void ${ADC_INSTANCE_NAME}_ChannelSelect( ADC_POSINPUT positiveInput, ADC_NEGINPUT negativeInput )
{
    /* Configure pin scan mode and positive and negative input pins */
    ${ADC_INSTANCE_NAME}_REGS->ADC_INPUTCTRL = (uint16_t) positiveInput | (uint16_t) negativeInput;

    while((${ADC_INSTANCE_NAME}_REGS->ADC_SYNCBUSY & ADC_SYNCBUSY_INPUTCTRL_Msk) == ADC_SYNCBUSY_INPUTCTRL_Msk)
    {
        /* Wait for Synchronization */
    }
}

/* Start the ADC conversion by SW */
void ${ADC_INSTANCE_NAME}_ConversionStart( void )
{
    /* Start conversion */
    ${ADC_INSTANCE_NAME}_REGS->ADC_SWTRIG |= (uint8_t)ADC_SWTRIG_START_Msk;

    while((${ADC_INSTANCE_NAME}_REGS->ADC_SYNCBUSY & ADC_SYNCBUSY_SWTRIG_Msk) == ADC_SYNCBUSY_SWTRIG_Msk)
    {
        /* Wait for Synchronization */
    }
}

/* Check whether auto sequence conversion is done */
bool ${ADC_INSTANCE_NAME}_ConversionSequenceIsFinished(void)
{
    bool seq_status = false;
    if ((${ADC_INSTANCE_NAME}_REGS->ADC_SEQSTATUS & ADC_SEQSTATUS_SEQBUSY_Msk) != ADC_SEQSTATUS_SEQBUSY_Msk)
    {
        seq_status = true;
    }
    return seq_status;
}

/* Configure window comparison threshold values */
void ${ADC_INSTANCE_NAME}_ComparisonWindowSet(uint16_t low_threshold, uint16_t high_threshold)
{
    ${ADC_INSTANCE_NAME}_REGS->ADC_WINLT = low_threshold;
    ${ADC_INSTANCE_NAME}_REGS->ADC_WINUT = high_threshold;
    while(0U != (${ADC_INSTANCE_NAME}_REGS->ADC_SYNCBUSY))
    {
        /* Wait for Synchronization */
    }
}

void ${ADC_INSTANCE_NAME}_WindowModeSet(ADC_WINMODE mode)
{
	${ADC_INSTANCE_NAME}_REGS->ADC_CTRLC =  (${ADC_INSTANCE_NAME}_REGS->ADC_CTRLC & (uint16_t)(~ADC_CTRLC_WINMODE_Msk)) | (uint16_t)((uint32_t)mode << ADC_CTRLC_WINMODE_Pos);
    while(0U != (${ADC_INSTANCE_NAME}_REGS->ADC_SYNCBUSY))
    {
        /* Wait for Synchronization */
    }
}

/* Read the conversion result */
uint16_t ${ADC_INSTANCE_NAME}_ConversionResultGet( void )
{
    return (uint16_t)${ADC_INSTANCE_NAME}_REGS->ADC_RESULT;
}

void ${ADC_INSTANCE_NAME}_InterruptsClear(ADC_STATUS interruptMask)
{
    ${ADC_INSTANCE_NAME}_REGS->ADC_INTFLAG = (uint8_t)interruptMask;
}

void ${ADC_INSTANCE_NAME}_InterruptsEnable(ADC_STATUS interruptMask)
{
    ${ADC_INSTANCE_NAME}_REGS->ADC_INTENSET = (uint8_t)interruptMask;
}

void ${ADC_INSTANCE_NAME}_InterruptsDisable(ADC_STATUS interruptMask)
{
    ${ADC_INSTANCE_NAME}_REGS->ADC_INTENCLR = (uint8_t)interruptMask;
}

<#if MULTI_VECTOR_SUPPORT??>
<#if ADC_INTENSET_RESRDY == true || (ADC_INTENSET_WINMON == true && ADC_CTRLC_WINMODE != "0")>
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
    ${ADC_INSTANCE_NAME}_REGS->ADC_INTFLAG = (uint8_t)ADC_INTFLAG_RESRDY_Msk;
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
    if (status == true)
    {
        ${ADC_INSTANCE_NAME}_REGS->ADC_INTFLAG = (uint8_t)ADC_INTFLAG_RESRDY_Msk;
    }
    return status;
}
</#if>
<#if ADC_INTENSET_WINMON = true && ADC_CTRLC_WINMODE != "0">
void ${ADC_INSTANCE_NAME}_OTHER_InterruptHandler( void )
{
    ADC_STATUS status;
    status = (ADC_STATUS) (${ADC_INSTANCE_NAME}_REGS->ADC_INTFLAG);
    /* Clear interrupt flag */
    ${ADC_INSTANCE_NAME}_REGS->ADC_INTFLAG = (uint8_t)(ADC_INTFLAG_WINMON_Msk | ADC_INTFLAG_OVERRUN_Msk);
    if (${ADC_INSTANCE_NAME}_CallbackObject.callback != NULL)
    {
        ${ADC_INSTANCE_NAME}_CallbackObject.callback(status, ${ADC_INSTANCE_NAME}_CallbackObject.context);
    }
}
<#else>
<#if ADC_CTRLC_WINMODE != "0">
/* Check whether window monitor result is ready */
bool ${ADC_INSTANCE_NAME}_WindowMonitorStatusGet( void )
{
    bool status;
    status = (((${ADC_INSTANCE_NAME}_REGS->ADC_INTFLAG & ADC_INTFLAG_WINMON_Msk) >> ADC_INTFLAG_WINMON_Pos) != 0U);
    if (status == true)
    {
        ${ADC_INSTANCE_NAME}_REGS->ADC_INTFLAG = (uint8_t)ADC_INTFLAG_WINMON_Msk;
    }
    return status;
}
</#if>
</#if>
<#else>
/* Check whether result is ready */
bool ${ADC_INSTANCE_NAME}_ConversionStatusGet( void )
{
    bool status;
    status =  (((${ADC_INSTANCE_NAME}_REGS->ADC_INTFLAG & ADC_INTFLAG_RESRDY_Msk) >> ADC_INTFLAG_RESRDY_Pos) != 0U);
    if (status == true)
    {
        ${ADC_INSTANCE_NAME}_REGS->ADC_INTFLAG = (uint8_t)ADC_INTFLAG_RESRDY_Msk;
    }
    return status;
}

<#if ADC_CTRLC_WINMODE != "0" && ADC_INTENSET_WINMON == false>
/* Check whether window monitor result is ready */
bool ${ADC_INSTANCE_NAME}_WindowMonitorStatusGet( void )
{
    bool status;
    status = (((${ADC_INSTANCE_NAME}_REGS->ADC_INTFLAG & ADC_INTFLAG_WINMON_Msk) >> ADC_INTFLAG_WINMON_Pos) != 0U);
    if (status == true)
    {
        ${ADC_INSTANCE_NAME}_REGS->ADC_INTFLAG = (uint8_t)ADC_INTFLAG_WINMON_Msk;
    }
    return status;
}
</#if>
</#if>
<#else>
<#if ADC_INTENSET_RESRDY == true || (ADC_CTRLC_WINMODE != "0" && ADC_INTENSET_WINMON == true)>
/* Register callback function */
void ${ADC_INSTANCE_NAME}_CallbackRegister( ADC_CALLBACK callback, uintptr_t context )
{
    ${ADC_INSTANCE_NAME}_CallbackObject.callback = callback;

    ${ADC_INSTANCE_NAME}_CallbackObject.context = context;
}


void ${ADC_INSTANCE_NAME}_InterruptHandler( void )
{
    ADC_STATUS status;
    status = ${ADC_INSTANCE_NAME}_REGS->ADC_INTFLAG;
    /* Clear interrupt flag */
    ${ADC_INSTANCE_NAME}_REGS->ADC_INTFLAG = (uint8_t)(${ADC_INTENSET_VAL});
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
    status =  (((${ADC_INSTANCE_NAME}_REGS->ADC_INTFLAG & ADC_INTFLAG_RESRDY_Msk) >> ADC_INTFLAG_RESRDY_Pos) != 0U);
    if (status == true)
    {
        ${ADC_INSTANCE_NAME}_REGS->ADC_INTFLAG = (uint8_t)ADC_INTFLAG_RESRDY_Msk;
    }
    return status;
}
</#if>
<#if ADC_CTRLC_WINMODE != "0" && ADC_INTENSET_WINMON == false>
/* Check whether window monitor result is ready */
bool ${ADC_INSTANCE_NAME}_WindowMonitorStatusGet( void )
{
    bool status;
    status = (((${ADC_INSTANCE_NAME}_REGS->ADC_INTFLAG & ADC_INTFLAG_WINMON_Msk) >> ADC_INTFLAG_WINMON_Pos) != 0U);
    if (status == true)
    {
        ${ADC_INSTANCE_NAME}_REGS->ADC_INTFLAG = (uint8_t)ADC_INTFLAG_WINMON_Msk;
    }
    return status;
}
</#if>
</#if>