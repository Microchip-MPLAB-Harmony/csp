/*******************************************************************************
  ADC Peripheral Library Interface Source File

  Company
    Microchip Technology Inc.

  File Name
    plib_${ADC_INSTANCE_NAME?lower_case}.c

  Summary
    ${ADC_INSTANCE_NAME} peripheral library source.

  Description
    This file implements the ADC peripheral library.

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

#include "device.h"
#include "plib_${ADC_INSTANCE_NAME?lower_case}.h"
<#if core.CoreSysIntFile == true>
#include "interrupts.h"
</#if>

#define ADC_SEQ1_CHANNEL_NUM (8U)

<#compress> <#-- To remove unwanted new lines -->
<#assign ADC_DIFFR_DIFF = "">
<#assign ADC_SHMR_DUAL = "">
<#assign ADC_IER_EOC = "">
<#assign ADC_CHER_CH = "">
<#assign ADC_SEQ1R_USCH = "">
<#assign ADC_SEQ2R_USCH = "">
<#assign ADC_INTERRUPT = false>
<#assign ADC_RES = "">
<#assign ADC_STM = "">

<#list 0..(ADC_NUM_CHANNELS - 1) as i>
<#assign ADC_CH_CHER = "ADC_"+i+"_CHER">
<#assign ADC_CH_POS_INP = "ADC_"+i+"_POS_INP">
<#assign ADC_CH_NEG_INP = "ADC_"+i+"_NEG_INP">
<#assign ADC_CH_SHMR_DUAL = "ADC_"+i+"_SHMR_DUAL">
<#assign ADC_CH_CGR_GAIN = "ADC_"+i+"_CGR_GAIN">
<#assign ADC_CH_COCR_AOFF = "ADC_"+i+"_COCR_AOFF">
<#assign ADC_CH_IER_EOC = "ADC_"+i+"_IER_EOC">
<#assign ADC_CH_SEQ1R_USCH = "ADC_SEQ1R_USCH"+i>
<#assign ADC_CH_DIFF_PAIR = "">

<#if (.vars[ADC_CH_CHER] == true) && (.vars[ADC_CH_IER_EOC] == true)>
    <#assign ADC_INTERRUPT = true>
</#if>

<#-- Differential mode -->
<#if i % 2 == 0>
    <#if (i == 0) || (i > 0 && (ADC_MR_ANACH?? && ADC_MR_ANACH == false))>
        <#if .vars[ADC_CH_CHER] == true && .vars[ADC_CH_NEG_INP] != "GND">
            <#if ADC_DIFFR_DIFF != "">
                <#assign ADC_DIFFR_DIFF = ADC_DIFFR_DIFF + " | " + "ADC_COR_DIFF"+i+"_Msk">
            <#else>
                <#assign ADC_DIFFR_DIFF = "ADC_COR_DIFF"+i+"_Msk">
            </#if>
        </#if>
    </#if>
</#if>

<#if i % 2 !=0 >
<#-- Save the diff mode of the even channel. Do not configure odd paired channel if diff mode is enabled for even channel -->
    <#assign ADC_CH_DIFF_PAIR = "ADC_"+(i-1)+"_NEG_INP">
</#if>

<#-- Interrupt -->
<#if .vars[ADC_CH_CHER] == true && .vars[ADC_CH_IER_EOC] == true>
    <#if (i % 2 != 0) && (.vars[ADC_CH_DIFF_PAIR] != "GND")>
    <#else>
        <#if ADC_IER_EOC != "">
            <#assign ADC_IER_EOC = ADC_IER_EOC + " | " + "ADC_IER_EOC"+i+"_Msk">
        <#else>
            <#assign ADC_IER_EOC = "ADC_IER_EOC"+i+"_Msk">
        </#if>
    </#if>
</#if>

<#-- Channel enable if user sequence is disabled -->
<#if ADC_MR_USEQ == false>
    <#if .vars[ADC_CH_CHER] == true>
        <#if ((i % 2 != 0) && (.vars[ADC_CH_DIFF_PAIR] != "GND"))>
        <#else>
            <#if ADC_CHER_CH != "">
                <#assign ADC_CHER_CH = ADC_CHER_CH + " | " + "ADC_CHER_CH"+i+"_Msk">
            <#else>
                <#assign ADC_CHER_CH = "ADC_CHER_CH"+i+"_Msk">
            </#if>
        </#if>
    </#if>
</#if>

<#-- User conversion sequence -->
<#if ADC_MR_USEQ == true>
    <#if .vars[ADC_CH_SEQ1R_USCH]?? && .vars[ADC_CH_SEQ1R_USCH] != "NONE">
        <#if i < 8>
            <#if ADC_SEQ1R_USCH != "">
                <#assign ADC_SEQ1R_USCH = ADC_SEQ1R_USCH + " | " + "ADC_SEQR1_USCH"+(i+1)+"(ADC_"+.vars[ADC_CH_SEQ1R_USCH]+")">
            <#else>
                <#assign ADC_SEQ1R_USCH = "ADC_SEQR1_USCH"+(i+1)+"(ADC_"+.vars[ADC_CH_SEQ1R_USCH]+")">
            </#if>
        <#else>
            <#if ADC_SEQ2R_USCH != "">
                <#assign ADC_SEQ2R_USCH = ADC_SEQ2R_USCH + " | " + "ADC_SEQ2R_USCH"+i+"(ADC_"+.vars[ADC_CH_SEQ1R_USCH]+")">
            <#else>
                <#assign ADC_SEQ2R_USCH = "ADC_SEQ2R_USCH"+i+"(ADC_"+.vars[ADC_CH_SEQ1R_USCH]+")">
            </#if>
        </#if>
        <#if ADC_CHER_CH != "">
            <#assign ADC_CHER_CH = ADC_CHER_CH + " | " + "ADC_CHER_CH"+i+"_Msk">
        <#else>
            <#assign ADC_CHER_CH = "ADC_CHER_CH"+i+"_Msk">
        </#if>
    </#if>
</#if>

</#list>

<#if ADC_EMR_RES_VALUE == "0">
    <#assign ADC_RES = "ADC_EMR_OSR_NO_AVERAGE">
    <#assign ADC_STM = "">
<#elseif ADC_EMR_RES_VALUE == "1">
    <#assign ADC_RES = "ADC_EMR_OSR_OSR4">
    <#assign ADC_STM = "| (ADC_EMR_ASTE_Msk)">
<#elseif ADC_EMR_RES_VALUE == "2">
    <#assign ADC_RES = "ADC_EMR_OSR_OSR4">
    <#assign ADC_STM = "">
<#elseif ADC_EMR_RES_VALUE == "3">
    <#assign ADC_RES = "ADC_EMR_OSR_OSR16">
    <#assign ADC_STM = "| (ADC_EMR_ASTE_Msk)">
<#elseif ADC_EMR_RES_VALUE == "4">
    <#assign ADC_RES = "ADC_EMR_OSR_OSR16">
    <#assign ADC_STM = "">
<#elseif ADC_EMR_RES_VALUE == "5">
    <#assign ADC_RES = "ADC_EMR_OSR_OSR64">
    <#assign ADC_STM = "| (ADC_EMR_ASTE_Msk)">
<#elseif ADC_EMR_RES_VALUE == "6">
    <#assign ADC_RES = "ADC_EMR_OSR_OSR64">
    <#assign ADC_STM = "">
<#elseif ADC_EMR_RES_VALUE == "7">
    <#assign ADC_RES = "ADC_EMR_OSR_OSR256">
    <#assign ADC_STM = "| (ADC_EMR_ASTE_Msk)">
<#elseif ADC_EMR_RES_VALUE == "8">
    <#assign ADC_RES = "ADC_EMR_OSR_OSR256">
    <#assign ADC_STM = "">
</#if>

</#compress>

// *****************************************************************************
// *****************************************************************************
// Section: ${ADC_INSTANCE_NAME} Implementation
// *****************************************************************************
// *****************************************************************************

<#if ADC_INTERRUPT == true>
    <#lt>/* Object to hold callback function and context */
    <#lt>ADC_CALLBACK_OBJECT ${ADC_INSTANCE_NAME}_CallbackObj;
</#if>

/* Initialize ADC peripheral */
void ${ADC_INSTANCE_NAME}_Initialize( void )
{
    /* Software reset */
    ${ADC_INSTANCE_NAME}_REGS->ADC_CR = ADC_CR_SWRST_Msk;

    /* Prescaler and different time settings as per CLOCK section  */
    <@compress single_line=true>${ADC_INSTANCE_NAME}_REGS->ADC_MR = ADC_MR_PRESCAL(${ADC_MR_PRESCAL}U)
                                                                    | ADC_MR_TRACKTIM(15U)
                                                                    | ADC_MR_STARTUP_SUT64
                                                                    | ADC_MR_TRANSFER(2U)
                                                                    <#if ADC_MR_ANACH??>${(ADC_MR_ANACH == false)?then('| ADC_MR_ANACH_Msk', '')}</#if>
                                                                    ${(ADC_CONV_MODE == "0")?then('| ADC_MR_FREERUN_Msk', '')}
                                                                    ${(ADC_CONV_MODE == "2")?then('| ADC_MR_TRGEN_Msk | ADC_MR_${ADC_MR_TRGSEL_VALUE}', '')};</@compress>

    /* resolution and sign mode of result */
    ${ADC_INSTANCE_NAME}_REGS->ADC_EMR = ${ADC_RES} ${ADC_STM}<#if ADC_CLK_SRC??> | ADC_EMR_${ADC_CLK_SRC}</#if> | ADC_EMR_TAG_Msk;

<#if ADC_DIFFR_DIFF?has_content>
    /* Differential mode */
    ${ADC_INSTANCE_NAME}_REGS->ADC_COR = ${ADC_DIFFR_DIFF};

</#if>
<#if ADC_MR_USEQ == true>
    /* User defined channel conversion sequence */
    ${ADC_INSTANCE_NAME}_REGS->ADC_MR |= ADC_MR_USEQ_Msk;

    <#if ADC_SEQ1R_USCH?has_content>
    <#lt>    ${ADC_INSTANCE_NAME}_REGS->ADC_SEQR1 = ${ADC_SEQ1R_USCH};

    </#if>
    <#if ADC_SEQ2R_USCH?has_content>
    <#lt>    ${ADC_INSTANCE_NAME}_REGS->ADC_SEQ2R = ${ADC_SEQ2R_USCH};

    </#if>
</#if>
<#if ADC_IER_EOC?has_content>
    /* Enable interrupt */
    ${ADC_INSTANCE_NAME}_REGS->ADC_IER = ${ADC_IER_EOC};

    ${ADC_INSTANCE_NAME}_CallbackObj.callback_fn = NULL;

</#if>
<#if ADC_CHER_CH?has_content>
    /* Enable channel */
    ${ADC_INSTANCE_NAME}_REGS->ADC_CHER = ${ADC_CHER_CH};
</#if>
}

/* Enable ADC channels */
void ${ADC_INSTANCE_NAME}_ChannelsEnable( ADC_CHANNEL_MASK channelsMask )
{
    ${ADC_INSTANCE_NAME}_REGS->ADC_CHER |= channelsMask;
}

/* Disable ADC channels */
void ${ADC_INSTANCE_NAME}_ChannelsDisable( ADC_CHANNEL_MASK channelsMask )
{
    ${ADC_INSTANCE_NAME}_REGS->ADC_CHDR |= channelsMask;
}

/* Enable channel end of conversion interrupt */
void ${ADC_INSTANCE_NAME}_ChannelsInterruptEnable( ADC_INTERRUPT_MASK channelsInterruptMask )
{
    ${ADC_INSTANCE_NAME}_REGS->ADC_IER |= channelsInterruptMask;
}

/* Disable channel end of conversion interrupt */
void ${ADC_INSTANCE_NAME}_ChannelsInterruptDisable( ADC_INTERRUPT_MASK channelsInterruptMask )
{
    ${ADC_INSTANCE_NAME}_REGS->ADC_IDR |= channelsInterruptMask;
}

/* Start the conversion with software trigger */
void ${ADC_INSTANCE_NAME}_ConversionStart( void )
{
    ${ADC_INSTANCE_NAME}_REGS->ADC_CR = 0x1U << ADC_CR_START_Pos;
}

/* Check if conversion result is available */
bool ${ADC_INSTANCE_NAME}_ChannelResultIsReady( ADC_CHANNEL_NUM channel )
{
    return (${ADC_INSTANCE_NAME}_REGS->ADC_ISR >> channel) & 0x1U;
}

/* Read the conversion result */
uint16_t ${ADC_INSTANCE_NAME}_ChannelResultGet( ADC_CHANNEL_NUM channel )
{
    return (${ADC_INSTANCE_NAME}_REGS->ADC_CDR[channel]);
}

/* Configure the user defined conversion sequence */
void ${ADC_INSTANCE_NAME}_ConversionSequenceSet( ADC_CHANNEL_NUM *channelList, uint8_t numChannel )
{
    uint8_t channelIndex;

    ${ADC_INSTANCE_NAME}_REGS->ADC_SEQR1 = 0U;

    for (channelIndex = 0U; channelIndex < ADC_SEQ1_CHANNEL_NUM; channelIndex++)
    {
        ${ADC_INSTANCE_NAME}_REGS->ADC_SEQR1 |= channelList[channelIndex] << (channelIndex * 4U);
    }
}

<#if ADC_INTERRUPT == true>
/* Register the callback function */
void ${ADC_INSTANCE_NAME}_CallbackRegister( ADC_CALLBACK callback, uintptr_t context )
{
    ${ADC_INSTANCE_NAME}_CallbackObj.callback_fn = callback;

    ${ADC_INSTANCE_NAME}_CallbackObj.context = context;
}

/* Interrupt Handler */
void ${ADC_INSTANCE_NAME}_InterruptHandler( void )
{
    uint32_t status = ${ADC_INSTANCE_NAME}_REGS->ADC_ISR;

    if (${ADC_INSTANCE_NAME}_CallbackObj.callback_fn != NULL)
    {
        ${ADC_INSTANCE_NAME}_CallbackObj.callback_fn(status, ${ADC_INSTANCE_NAME}_CallbackObj.context);
    }
}
</#if>
