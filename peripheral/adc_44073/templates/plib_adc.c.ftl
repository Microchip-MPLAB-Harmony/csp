/*******************************************************************************
  ${ADC_INSTANCE_NAME} Peripheral Library Interface Source File

  Company
    Microchip Technology Inc.

  File Name
    plib_${ADC_INSTANCE_NAME?lower_case}.c

  Summary
    ${ADC_INSTANCE_NAME} peripheral library source.

  Description
    This file implements the ${ADC_INSTANCE_NAME} peripheral library.

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
#include "device.h"
#include "plib_${ADC_INSTANCE_NAME?lower_case}.h"

#define ADC_SEQ1_CHANNEL_NUM (8U)

<#compress> <#-- To remove unwanted new lines -->
<#assign ADC_COR_DIFF = "">
<#assign ADC_IER_EOC = "">
<#assign ADC_CHER_CH = "">
<#assign ADC_SEQR1_USCH = "">
<#assign ADC_SEQR2_USCH = "">
<#assign ADC_INTERRUPT = false>
<#assign ADC_OSR = "">
<#assign ADC_ASTE = "">
<#list 0..(ADC_NUM_CHANNELS - 1) as i>
<#assign ADC_CH_CHER = "ADC_"+i+"_CHER">
<#assign ADC_CH_POS_INP = "ADC_"+i+"_POS_INP">
<#assign ADC_CH_NEG_INP = "ADC_"+i+"_NEG_INP">
<#assign ADC_CH_IER_EOC = "ADC_"+i+"_IER_EOC">
<#assign ADC_CH_SEQR1_USCH = "ADC_SEQR1_USCH"+(i+1)>
<#assign ADC_CH_DIFF_PAIR = "">

<#if (.vars[ADC_CH_CHER] == true) && ((.vars[ADC_CH_IER_EOC] == true) || (ADC_IER_COMPE == true))>
    <#assign ADC_INTERRUPT = true>
</#if>

<#-- Differential mode -->
<#if i % 2 == 0>
    <#if .vars[ADC_CH_CHER] == true && .vars[ADC_CH_NEG_INP] != "GND">
        <#if ADC_COR_DIFF != "">
            <#assign ADC_COR_DIFF = ADC_COR_DIFF + " | " + "ADC_COR_DIFF"+i+"_Msk">
        <#else>
            <#assign ADC_COR_DIFF = "ADC_COR_DIFF"+i+"_Msk">
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
    <#if i < (ADC_NUM_CHANNELS - 1)>
    <#if .vars[ADC_CH_SEQR1_USCH] != "NONE">
        <#if i < 8>
            <#if ADC_SEQR1_USCH != "">
                <#assign ADC_SEQR1_USCH = ADC_SEQR1_USCH + " | \n\t\t" + "ADC_SEQR1_USCH"+(i+1)+"(ADC_"+.vars[ADC_CH_SEQR1_USCH]+")">
            <#else>
                <#assign ADC_SEQR1_USCH = "ADC_SEQR1_USCH"+(i+1)+"(ADC_"+.vars[ADC_CH_SEQR1_USCH]+")">
            </#if>
        <#else>
            <#if ADC_SEQR2_USCH != "">
                <#assign ADC_SEQR2_USCH = ADC_SEQR2_USCH + " | \n\t\t" + "ADC_SEQR2_USCH"+(i+1)+"(ADC_"+.vars[ADC_CH_SEQR1_USCH]+")">
            <#else>
                <#assign ADC_SEQR2_USCH = "ADC_SEQR2_USCH"+(i+1)+"(ADC_"+.vars[ADC_CH_SEQR1_USCH]+")">
            </#if>
        </#if>
        <#if ADC_CHER_CH != "">
            <#assign ADC_CHER_CH = ADC_CHER_CH + " | " + "ADC_CHER_CH"+i+"_Msk">
        <#else>
            <#assign ADC_CHER_CH = "ADC_CHER_CH"+i+"_Msk">
        </#if>
    </#if>
    </#if>
</#if>

</#list>

<#if ADC_EMR_OSR_VALUE == "0">
    <#assign ADC_OSR = "ADC_EMR_OSR_NO_AVERAGE">
    <#assign ADC_ASTE = "">
<#elseif ADC_EMR_OSR_VALUE == "1">
    <#assign ADC_OSR = "ADC_EMR_OSR_OSR4">
    <#assign ADC_ASTE = "| ADC_EMR_ASTE_Msk">
<#elseif ADC_EMR_OSR_VALUE == "2">
    <#assign ADC_OSR = "ADC_EMR_OSR_OSR4">
    <#assign ADC_ASTE = "">
<#elseif ADC_EMR_OSR_VALUE == "3">
    <#assign ADC_OSR = "ADC_EMR_OSR_OSR16">
    <#assign ADC_ASTE = "| ADC_EMR_ASTE_Msk">
<#elseif ADC_EMR_OSR_VALUE == "4">
    <#assign ADC_OSR = "ADC_EMR_OSR_OSR16">
    <#assign ADC_ASTE = "">
<#elseif ADC_EMR_OSR_VALUE == "5">
    <#assign ADC_OSR = "ADC_EMR_OSR_OSR64">
    <#assign ADC_ASTE = "| ADC_EMR_ASTE_Msk">
<#elseif ADC_EMR_OSR_VALUE == "6">
    <#assign ADC_OSR = "ADC_EMR_OSR_OSR64">
    <#assign ADC_ASTE = "">
<#elseif ADC_EMR_OSR_VALUE == "7">
    <#assign ADC_OSR = "ADC_EMR_OSR_OSR256">
    <#assign ADC_ASTE = "| ADC_EMR_ASTE_Msk">
<#elseif ADC_EMR_OSR_VALUE == "8">
    <#assign ADC_OSR = "ADC_EMR_OSR_OSR256">
    <#assign ADC_ASTE = "">
</#if>

</#compress>

<#-- *********************************************************************************************** -->
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
void ${ADC_INSTANCE_NAME}_Initialize()
{
    /* Software reset */
    ${ADC_INSTANCE_NAME}_REGS->ADC_CR = ADC_CR_SWRST_Msk;

    /* Prescaler and different time settings as per CLOCK section  */
    ${ADC_INSTANCE_NAME}_REGS->ADC_MR = ADC_MR_PRESCAL(${ADC_MR_PRESCAL}U) | ADC_MR_TRACKTIM(15U) | ADC_MR_STARTUP_SUT512 |
        ADC_MR_TRANSFER(2U) | ADC_MR_ANACH_ALLOWED<#rt>
        <#lt>${((ADC_TRGR_MODE == "TRGMOD_EXT_TRIG_RISE") || (ADC_TRGR_MODE == "TRGMOD_EXT_TRIG_FALL") || (ADC_TRGR_MODE == "TRGMOD_EXT_TRIG_ANY"))?then(' | ADC_MR_${ADC_MR_TRGSEL_VALUE}', '')}<#rt>
        <#lt>${(ADC_MR_SLEEP == true)?then(' | ADC_MR_SLEEP_Msk | ADC_MR_FWUP_${ADC_MR_FWUP}', '')};

    /* resolution<#if ADC_CLK_SRC??>, source clock</#if> and sign mode of result */
    ${ADC_INSTANCE_NAME}_REGS->ADC_EMR = ${ADC_OSR} ${ADC_ASTE} <#if ADC_CLK_SRC??>| ADC_EMR_SRCCLK_${ADC_CLK_SRC} </#if>
         | ADC_EMR_SIGNMODE_${ADC_EMR_SIGNMODE_VALUE} | ADC_EMR_TAG_Msk;

    /* Trigger mode */
    ${ADC_INSTANCE_NAME}_REGS->ADC_TRGR = ADC_TRGR_${ADC_TRGR_MODE}${(ADC_TRGR_MODE == "TRGMOD_PERIOD_TRIG")?then(' | ADC_TRGR_TRGPER(${ADC_TRGR_TRIGGER_PERIOD}U)', '')};

<#if ADC_COMP_WINDOW == true>
    /* Automatic Window Comparison */
    ${ADC_INSTANCE_NAME}_REGS->ADC_EMR |= ADC_EMR_${ADC_EMR_CMPMODE} | ADC_EMR_${ADC_EMR_CMPTYPE} | ${(ADC_EMR_CMPSEL == "All")?then('ADC_EMR_CMPALL_Msk','ADC_EMR_CMPSEL(ADC_${ADC_EMR_CMPSEL})')};
    ${ADC_INSTANCE_NAME}_REGS->ADC_CWR = ADC_CWR_LOWTHRES(${ADC_CWR_LOWTHRES_VALUE}U) | ADC_CWR_HIGHTHRES(${ADC_CWR_HIGHTHRES_VALUE}U);
<#if ADC_IER_COMPE == true>
    ${ADC_INSTANCE_NAME}_REGS->ADC_IER = ADC_IER_COMPE_Msk;
</#if>
</#if>
<#if ADC_COR_DIFF?has_content>
    /* Differential mode */
    ${ADC_INSTANCE_NAME}_REGS->ADC_COR = ${ADC_COR_DIFF};

</#if>
<#if ADC_MR_USEQ == true>
    /* User defined channel conversion sequence */
    ${ADC_INSTANCE_NAME}_REGS->ADC_MR |= ADC_MR_USEQ_Msk;
    <#if ADC_SEQR1_USCH?has_content>
    <#lt>    ${ADC_INSTANCE_NAME}_REGS->ADC_SEQR1 = ${ADC_SEQR1_USCH};
    </#if>
    <#if ADC_SEQR2_USCH?has_content>
    <#lt>    ${ADC_INSTANCE_NAME}_REGS->ADC_SEQR2 = ${ADC_SEQR2_USCH};
    </#if>
</#if>
<#if ADC_IER_EOC?has_content>
    /* Enable interrupt */
    ${ADC_INSTANCE_NAME}_REGS->ADC_IER = ${ADC_IER_EOC};
    ADC_CallbackObj.callback_fn = NULL;
</#if>
<#if ADC_CHER_CH?has_content>
    /* Enable channel */
    ${ADC_INSTANCE_NAME}_REGS->ADC_CHER = ${ADC_CHER_CH};
</#if>
}

/* Enable ADC channels */
void ${ADC_INSTANCE_NAME}_ChannelsEnable (ADC_CHANNEL_MASK channelsMask)
{
    ${ADC_INSTANCE_NAME}_REGS->ADC_CHER = channelsMask;
}

/* Disable ADC channels */
void ${ADC_INSTANCE_NAME}_ChannelsDisable (ADC_CHANNEL_MASK channelsMask)
{
    ${ADC_INSTANCE_NAME}_REGS->ADC_CHDR = channelsMask;
}

/* Enable channel end of conversion or Comparison event interrupt */
void ${ADC_INSTANCE_NAME}_ChannelsInterruptEnable (ADC_INTERRUPT_MASK channelsInterruptMask)
{
    ${ADC_INSTANCE_NAME}_REGS->ADC_IER = channelsInterruptMask;
}

/* Disable channel end of conversion or Comparison event interrupt */
void ${ADC_INSTANCE_NAME}_ChannelsInterruptDisable (ADC_INTERRUPT_MASK channelsInterruptMask)
{
    ${ADC_INSTANCE_NAME}_REGS->ADC_IDR = channelsInterruptMask;
}

/* Start the conversion with software trigger */
void ${ADC_INSTANCE_NAME}_ConversionStart(void)
{
    ${ADC_INSTANCE_NAME}_REGS->ADC_CR = ADC_CR_START_Msk;
}

/* Check if conversion result is available */
bool ${ADC_INSTANCE_NAME}_ChannelResultIsReady(ADC_CHANNEL_NUM channel)
{
    return (${ADC_INSTANCE_NAME}_REGS->ADC_ISR >> channel) & 0x1U;
}

/* Read the conversion result */
uint16_t ${ADC_INSTANCE_NAME}_ChannelResultGet(ADC_CHANNEL_NUM channel)
{
    return ${ADC_INSTANCE_NAME}_REGS->ADC_CDR[channel];
}

/* Configure the user defined conversion sequence */
void ${ADC_INSTANCE_NAME}_ConversionSequenceSet(ADC_CHANNEL_NUM *channelList, uint8_t numChannel)
{
    uint8_t channelIndex;
    ${ADC_INSTANCE_NAME}_REGS->ADC_SEQR1 = 0U;
    ${ADC_INSTANCE_NAME}_REGS->ADC_SEQR2 = 0U;

    for (channelIndex = 0U; channelIndex < ADC_SEQ1_CHANNEL_NUM; channelIndex++)
    {
        if (channelIndex >= numChannel)
            break;
        ${ADC_INSTANCE_NAME}_REGS->ADC_SEQR1 |= channelList[channelIndex] << (channelIndex * 4U);
    }
    if (numChannel > ADC_SEQ1_CHANNEL_NUM)
    {
        for (channelIndex = 0U; channelIndex < (numChannel - ADC_SEQ1_CHANNEL_NUM); channelIndex++)
        {
            if (channelIndex >= 3)
                break;
            ${ADC_INSTANCE_NAME}_REGS->ADC_SEQR2 |= channelList[channelIndex + ADC_SEQ1_CHANNEL_NUM] << (channelIndex * 4U);
        }
    }
}

/* Sets Low threshold and High threshold in comparison window */
void ${ADC_INSTANCE_NAME}_ComparisonWindowSet(uint16_t lowThreshold, uint16_t highThreshold)
{
    ${ADC_INSTANCE_NAME}_REGS->ADC_CWR = ADC_CWR_LOWTHRES(lowThreshold) | ADC_CWR_HIGHTHRES(highThreshold);
}

/* Check if Comparison event result is available */
bool ${ADC_INSTANCE_NAME}_ComparisonEventResultIsReady(void)
{
    return (${ADC_INSTANCE_NAME}_REGS->ADC_ISR >> ADC_ISR_COMPE_Pos) & 0x1U;
}

/* Restart the comparison function */
void ${ADC_INSTANCE_NAME}_ComparisonRestart(void)
{
    ${ADC_INSTANCE_NAME}_REGS->ADC_CR = ADC_CR_CMPRST_Msk;
}

<#if ADC_INTERRUPT == true>
    <#lt>/* Register the callback function */
    <#lt>void ${ADC_INSTANCE_NAME}_CallbackRegister(ADC_CALLBACK callback, uintptr_t context)
    <#lt>{
    <#lt>    ${ADC_INSTANCE_NAME}_CallbackObj.callback_fn = callback;
    <#lt>    ${ADC_INSTANCE_NAME}_CallbackObj.context = context;
    <#lt>}
</#if>
<#if ADC_INTERRUPT == true>
    <#lt>/* Interrupt Handler */
    <#lt>void ${ADC_INSTANCE_NAME}_InterruptHandler(void)
    <#lt>{
    <#lt>    if (${ADC_INSTANCE_NAME}_CallbackObj.callback_fn != NULL)
    <#lt>    {
    <#lt>        ${ADC_INSTANCE_NAME}_CallbackObj.callback_fn(${ADC_INSTANCE_NAME}_CallbackObj.context);
    <#lt>    }
    <#lt>}
</#if>
