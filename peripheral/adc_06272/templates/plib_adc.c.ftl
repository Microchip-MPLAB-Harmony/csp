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
<#assign ADC_SEQCTRL_VAL = "">
<#assign ADC_EVCTRL_VAL = "">
<#assign ADC_INTENSET_VAL = "">
<#assign ADC_CTRLA_VAL = "">

<#if ADC_CONV_TRIGGER != "Free Run">
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
<#if ADC_EVCTRL_SAMPRDYEO == true>
    <#if ADC_EVCTRL_VAL != "">
        <#assign ADC_EVCTRL_VAL = ADC_EVCTRL_VAL + " | ADC_EVCTRL_SAMPRDYEO_Msk">
    <#else>
        <#assign ADC_EVCTRL_VAL = "ADC_EVCTRL_SAMPRDYEO_Msk">
    </#if>
</#if>
<#if ADC_WINCTRL_WINMODE != "0" && ADC_WINDOW_OUTPUT_EVENT == true>
    <#if ADC_EVCTRL_VAL != "">
        <#assign ADC_EVCTRL_VAL = ADC_EVCTRL_VAL + " | ADC_EVCTRL_WCMPEO_Msk">
    <#else>
        <#assign ADC_EVCTRL_VAL = "ADC_EVCTRL_WINMONEO_Msk">
    </#if>
</#if>

<#if ADC_CONV_TRIGGER == "HW Event Trigger">
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
<#if ADC_INTENSET_SAMPRDY == true>
    <#if ADC_INTENSET_VAL != "">
        <#assign ADC_INTENSET_VAL = ADC_INTENSET_VAL + " | ADC_INTENSET_SAMPRDY_Msk">
    <#else>
        <#assign ADC_INTENSET_VAL = "ADC_INTENSET_SAMPRDY_Msk">
    </#if>
</#if>
<#if ADC_WINCTRL_WINMODE != "0" && ADC_INTENSET_WCMP == true>
    <#if ADC_INTENSET_VAL != "">
        <#assign ADC_INTENSET_VAL = ADC_INTENSET_VAL + " | ADC_INTENSET_WCMP_Msk">
    <#else>
        <#assign ADC_INTENSET_VAL = "ADC_INTENSET_WCMP_Msk">
    </#if>
</#if>
<#if ADC_INTENSET_RESOVR == true>
    <#if ADC_INTENSET_VAL != "">
        <#assign ADC_INTENSET_VAL = ADC_INTENSET_VAL + " | ADC_INTENSET_RESOVR_Msk">
    <#else>
        <#assign ADC_INTENSET_VAL = "ADC_INTENSET_RESOVR_Msk">
    </#if>
</#if>
<#if ADC_INTENSET_SAMPOVR == true>
    <#if ADC_INTENSET_VAL != "">
        <#assign ADC_INTENSET_VAL = ADC_INTENSET_VAL + " | ADC_INTENSET_SAMPOVR_Msk">
    <#else>
        <#assign ADC_INTENSET_VAL = "ADC_INTENSET_SAMPOVR_Msk">
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
<#if (ADC_INTENSET_RESRDY == true) || (ADC_INTENSET_RESOVR == true) || (ADC_WINCTRL_WINMODE != "0x0" && ADC_INTENSET_WCMP == true) || (ADC_INTENSET_SAMPRDY == true) || (ADC_INTENSET_SAMPOVR == true)>
static volatile ADC_CALLBACK_OBJ ${ADC_INSTANCE_NAME}_CallbackObject;
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

    while((${ADC_INSTANCE_NAME}_REGS->ADC_STATUS & ADC_STATUS_ADCBUSY_Msk) != 0U)
    {
        /* Wait for Synchronization */
    }

    /* Prescaler and timebase configuration */
    ${ADC_INSTANCE_NAME}_REGS->ADC_CTRLB = (uint8_t)ADC_CTRLB_PRESCALER_${ADC_CTRLB_PRESCALER} | ADC_CTRLB_TIMEBASE(${ADC_CTRLB_TIMEBASE}UL) ;

    /* Sampling length */
    ${ADC_INSTANCE_NAME}_REGS->ADC_CTRLE = (uint8_t)ADC_CTRLE_SAMPLEN(${ADC_CTRLE_SAMPLEN - 1}UL);

    /* Reference */
    ${ADC_INSTANCE_NAME}_REGS->ADC_CTRLC = (uint8_t)ADC_CTRLC_REFSEL_${ADC_CTRLC_REFSEL};

<#if ADC_SEQCTRL_VAL?has_content>
    /*lint -e{9048} false positive about a missing 'U' literal */
    ${ADC_INSTANCE_NAME}_REGS->ADC_SEQCTRL = ${ADC_SEQCTRL_VAL};
    <#if ADC_COMMAND_DIFFMODE == true>
    ${ADC_INSTANCE_NAME}_REGS->ADC_INPUTCTRL =  ((uint16_t)ADC_NEGINPUT_${ADC_INPUTCTRL_MUXNEG});
    </#if>
<#else>
    <#if ADC_COMMAND_DIFFMODE == true>
    /* Positive and negative input pins */
    ${ADC_INSTANCE_NAME}_REGS->ADC_INPUTCTRL =  ((uint16_t)ADC_POSINPUT_${ADC_INPUTCTRL_MUXPOS} | (uint16_t)ADC_NEGINPUT_${ADC_INPUTCTRL_MUXNEG});
    <#else>
    /* Input pin */
    ${ADC_INSTANCE_NAME}_REGS->ADC_INPUTCTRL = (uint16_t) ADC_POSINPUT_${ADC_INPUTCTRL_MUXPOS};
    </#if>
</#if>

<#if (ADC_COMMAND_OPMODE == "0x2") || (ADC_COMMAND_OPMODE == "0x3")>
    /* Resolution,Scaling,Filter & Chopping Mode */
    <@compress single_line=true>${ADC_INSTANCE_NAME}_REGS->ADC_CTRLD = ADC_CTRLD_RESOLUTION_${ADC_CTRLD_RESOLUTION}
    <#if ADC_CTRLD_FILTER>
        | ADC_CTRLD_FILTER(1UL)
    <#else>
        | ADC_CTRLD_FILTER(0UL)
    </#if>
    <#if ADC_CTRLD_CHOPPING>
        | ADC_CTRLD_CHOPPING(1UL)
    <#else>
        | ADC_CTRLD_CHOPPING(0UL)
    </#if>
    | ADC_CTRLD_SCALING(${ADC_CTRLD_SCALING}UL)
    | ADC_CTRLD_SAMPNUM(${ADC_CTRLD_SAMPNUM}UL)
    <#if ADC_CONV_TRIGGER == "Free Run">
        | ADC_CTRLD_FREERUN_Msk
    </#if>;
    </@compress>
<#else>
    /* Resolution & Scaling */
    <@compress single_line=true>${ADC_INSTANCE_NAME}_REGS->ADC_CTRLD = ADC_CTRLD_RESOLUTION_${ADC_CTRLD_RESOLUTION} | ADC_CTRLD_SCALING(${ADC_CTRLD_SCALING}UL)
                                                                        <#if ADC_CONV_TRIGGER == "Free Run">
                                                                            | ADC_CTRLD_FREERUN_Msk
                                                                        </#if>
                                                                        <#if ADC_CTRLD_VPD>
                                                                            | ADC_CTRLD_VPD(1UL)
                                                                        <#else>
                                                                            | ADC_CTRLD_VPD(0UL)
                                                                        </#if>
                                                                        | ADC_CTRLD_SAMPNUM(${ADC_CTRLD_SAMPNUM}UL);</@compress>
</#if>

    /* Window Operation Mode */
    ${ADC_INSTANCE_NAME}_REGS->ADC_WINCTRL = (uint32_t)ADC_WINCTRL_WINMODE(${ADC_WINCTRL_WINMODE}UL);

<#if ADC_WINCTRL_WINMODE != "0x0">
    /* Upper threshold for window mode  */
    ${ADC_INSTANCE_NAME}_REGS->ADC_WINHT = (uint16_t)(${ADC_WINHT});
    /* Lower threshold for window mode  */
    ${ADC_INSTANCE_NAME}_REGS->ADC_WINLT = (uint16_t)(${ADC_WINLT});
    /* Source for window mode  */
    ${ADC_INSTANCE_NAME}_REGS->ADC_WINCTRL |= (uint32_t)ADC_WINCTRL_WINSRC(${ADC_WINCTRL_WINSRC}UL);
</#if>
    /* Clear all interrupt flags */
    ${ADC_INSTANCE_NAME}_REGS->ADC_INTFLAG = (uint8_t)ADC_INTFLAG_Msk;
<#if ADC_INTENSET_VAL?has_content >
    /* Enable interrupts */
    ${ADC_INSTANCE_NAME}_REGS->ADC_INTENSET = (uint8_t)(${ADC_INTENSET_VAL});
</#if>

<#if ADC_EVCTRL_VAL?has_content>
    /* Events configuration  */
    ${ADC_INSTANCE_NAME}_REGS->ADC_EVCTRL = (uint8_t)(${ADC_EVCTRL_VAL});
</#if>

<#if ADC_CTRLA_VAL?has_content>
    <@compress single_line=true>${ADC_INSTANCE_NAME}_REGS->ADC_CTRLA |= (uint8_t)(${ADC_CTRLA_VAL});</@compress>
</#if>

    /* Mode of opearation and Start type*/
    <#assign hexStr = ADC_COMMAND_OPMODE?replace("0x", "") />
    <#assign OPMODE = hexStr?number />
    <#assign hexStr = ADC_COMMAND_CTRLCONV?replace("0x", "") />
    <#assign STARTTYPE = hexStr?number />
    <@compress single_line=true>${ADC_INSTANCE_NAME}_REGS->ADC_COMMAND = (uint8_t)ADC_COMMAND_MODE(${OPMODE}UL) | (uint8_t)ADC_COMMAND_START(${STARTTYPE}UL)
                                            <#if ADC_COMMAND_DIFFMODE>
                                                | (uint8_t)ADC_COMMAND_DIFF_Msk
                                            </#if>;</@compress>

    while((${ADC_INSTANCE_NAME}_REGS->ADC_STATUS & ADC_STATUS_ADCBUSY_Msk) != 0U)
    {
        /* Wait for Synchronization */
    }
}

/* Enable ADC module */
void ${ADC_INSTANCE_NAME}_Enable( void )
{
    ${ADC_INSTANCE_NAME}_REGS->ADC_CTRLA |= (uint8_t)ADC_CTRLA_ENABLE_Msk;
    while((${ADC_INSTANCE_NAME}_REGS->ADC_STATUS & ADC_STATUS_ADCBUSY_Msk) != 0U)
    {
        /* Wait for Synchronization */
    }
}

/* Disable ADC module */
void ${ADC_INSTANCE_NAME}_Disable( void )
{
    ${ADC_INSTANCE_NAME}_REGS->ADC_CTRLA &= (uint8_t)(~ADC_CTRLA_ENABLE_Msk);
    while((${ADC_INSTANCE_NAME}_REGS->ADC_STATUS & ADC_STATUS_ADCBUSY_Msk) != 0U)
    {
        /* Wait for Synchronization */
    }
}

/* Configure channel input */
void ${ADC_INSTANCE_NAME}_ChannelSelect( ADC_POSINPUT positiveInput, ADC_NEGINPUT negativeInput )
{
    /* Configure pin scan mode and positive and negative input pins */
    ${ADC_INSTANCE_NAME}_REGS->ADC_INPUTCTRL = (uint16_t)((uint16_t) positiveInput | (uint16_t) negativeInput);

    while((${ADC_INSTANCE_NAME}_REGS->ADC_STATUS & ADC_STATUS_ADCBUSY_Msk) != 0U)
    {
        /* Wait for Synchronization */
    }
}

/* Start the ADC conversion by SW */
void ${ADC_INSTANCE_NAME}_ConversionStart( void )
{
    /* Start conversion */
    ${ADC_INSTANCE_NAME}_REGS->ADC_COMMAND |= (uint32_t)ADC_COMMAND_START_IMMEDIATE;

}

/* Select ADC conversion start type */
void ${ADC_INSTANCE_NAME}_ConversionStartModeSet( ADC_STARTMODE startMode )
{
    /* Start conversion */
    ${ADC_INSTANCE_NAME}_REGS->ADC_COMMAND |= (uint32_t)startMode;

    while((${ADC_INSTANCE_NAME}_REGS->ADC_STATUS & ADC_STATUS_ADCBUSY_Msk) != 0U)
    {
        /* Wait for Synchronization */
    }
}

/* Check if adc conversion is on going conversion completed*/
bool ${ADC_INSTANCE_NAME}_ConversionIsFinished( void )
{
    return ((${ADC_INSTANCE_NAME}_REGS->ADC_STATUS & ADC_STATUS_ADCBUSY_Msk) == 0U);
}

/* Configure window comparison threshold values */
void ${ADC_INSTANCE_NAME}_ComparisonWindowSet(uint16_t low_threshold, uint16_t high_threshold)
{
    ${ADC_INSTANCE_NAME}_REGS->ADC_WINLT = low_threshold;
    ${ADC_INSTANCE_NAME}_REGS->ADC_WINHT = high_threshold;
    while((${ADC_INSTANCE_NAME}_REGS->ADC_STATUS & ADC_STATUS_ADCBUSY_Msk) != 0U)
    {
        /* Wait for Synchronization */
    }
}

void ${ADC_INSTANCE_NAME}_WindowModeSet(ADC_WINMODE mode)
{
    ${ADC_INSTANCE_NAME}_REGS->ADC_WINCTRL =  (${ADC_INSTANCE_NAME}_REGS->ADC_WINCTRL & (uint16_t)(~ADC_WINCTRL_WINMODE_Msk)) | (uint16_t)((uint32_t)mode);
    while((${ADC_INSTANCE_NAME}_REGS->ADC_STATUS & ADC_STATUS_ADCBUSY_Msk) != 0U)
    {
        /* Wait for Synchronization */
    }
}

/* Read the conversion result */
uint32_t ${ADC_INSTANCE_NAME}_ConversionResultGet( void )
{
    return (uint32_t)${ADC_INSTANCE_NAME}_REGS->ADC_RESULT;
}

void ${ADC_INSTANCE_NAME}_InterruptsClear(ADC_INTERRUPTS interruptMask)
{
    ${ADC_INSTANCE_NAME}_REGS->ADC_INTFLAG = (uint8_t)interruptMask;
}

void ${ADC_INSTANCE_NAME}_InterruptsEnable(ADC_INTERRUPTS interruptMask)
{
    ${ADC_INSTANCE_NAME}_REGS->ADC_INTENSET = (uint8_t)interruptMask;
}

void ${ADC_INSTANCE_NAME}_InterruptsDisable(ADC_INTERRUPTS interruptMask)
{
    ${ADC_INSTANCE_NAME}_REGS->ADC_INTENCLR = (uint8_t)interruptMask;
}

<#if (ADC_INTENSET_RESRDY == true) || (ADC_INTENSET_RESOVR == true) || (ADC_WINCTRL_WINMODE != "0x0" && ADC_INTENSET_WCMP == true) || (ADC_INTENSET_SAMPRDY == true) || (ADC_INTENSET_SAMPOVR == true)>
/* Register callback function */
void ${ADC_INSTANCE_NAME}_CallbackRegister( ADC_CALLBACK callback, uintptr_t context )
{
    ${ADC_INSTANCE_NAME}_CallbackObject.callback = callback;

    ${ADC_INSTANCE_NAME}_CallbackObject.context = context;
}

void __attribute__((used)) ${ADC_INSTANCE_NAME}_InterruptHandler( void )
{
    ADC_STATUS status;
    status = ${ADC_INSTANCE_NAME}_REGS->ADC_INTFLAG;
    /* Clear interrupt flag */
    ${ADC_INSTANCE_NAME}_REGS->ADC_INTFLAG = (uint8_t)(${ADC_INTENSET_VAL});
    if (${ADC_INSTANCE_NAME}_CallbackObject.callback != NULL)
    {
        uintptr_t context = ${ADC_INSTANCE_NAME}_CallbackObject.context;
        ${ADC_INSTANCE_NAME}_CallbackObject.callback(status, context);
    }
}
</#if>
<#if ADC_INTENSET_RESRDY == false>
/* Check whether result is ready */
bool ${ADC_INSTANCE_NAME}_ResultReadyStatusGet( void )
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
<#if ADC_INTENSET_SAMPRDY == false>
/* Check whether sample is ready */
bool ${ADC_INSTANCE_NAME}_SampleReadyStatusGet( void )
{
    bool status;
    status =  (((${ADC_INSTANCE_NAME}_REGS->ADC_INTFLAG & ADC_INTFLAG_SAMPRDY_Msk) >> ADC_INTFLAG_SAMPRDY_Pos) != 0U);
    if (status == true)
    {
        ${ADC_INSTANCE_NAME}_REGS->ADC_INTFLAG = (uint8_t)ADC_INTFLAG_SAMPRDY_Msk;
    }
    return status;
}
</#if>
<#if ADC_WINCTRL_WINMODE != "0x0" && ADC_INTENSET_WCMP == false>
/* Check whether window monitor result is ready */
bool ${ADC_INSTANCE_NAME}_WindowMonitorStatusGet( void )
{
    bool status;
    status = (((${ADC_INSTANCE_NAME}_REGS->ADC_INTFLAG & ADC_INTFLAG_WCMP_Msk) >> ADC_INTFLAG_WCMP_Pos) != 0U);
    if (status == true)
    {
        ${ADC_INSTANCE_NAME}_REGS->ADC_INTFLAG = (uint8_t)ADC_INTFLAG_WCMP_Msk;
    }
    return status;
}
</#if>
