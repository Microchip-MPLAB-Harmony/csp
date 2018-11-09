/*******************************************************************************
  AFEC Peripheral Library Interface Source File

  Company
    Microchip Technology Inc.

  File Name
    plib_${AFEC_INSTANCE_NAME?lower_case}.c

  Summary
    ${AFEC_INSTANCE_NAME} peripheral library source.

  Description
    This file implements the AFEC peripheral library.

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
#include "plib_${AFEC_INSTANCE_NAME?lower_case}.h"

#define AFEC_SEQ1_CHANNEL_NUM (8U)

#define AFEC_CGR_GAIN_X1   (0x00U)
#define AFEC_CGR_GAIN_X2   (0x01U)
#define AFEC_CGR_GAIN_X4   (0x03U)

<#compress> <#-- To remove unwanted new lines -->
<#assign AFEC_CGR_GAIN = "">
<#assign AFEC_DIFFR_DIFF = "">
<#assign AFEC_SHMR_DUAL = "">
<#assign AFEC_IER_EOC = "">
<#assign AFEC_CHER_CH = "">
<#assign AFEC_SEQ1R_USCH = "">
<#assign AFEC_SEQ2R_USCH = "">
<#assign AFEC_INTERRUPT = false>
<#assign AFEC_RES = "">
<#assign AFEC_STM = "">
<#assign AFEC_IBCTL = "">
<#if AFEC_CLK <= 500000>
    <#assign AFEC_IBCTL = "0x1U">
<#elseif (AFEC_CLK > 500000 && AFEC_CLK <= 1000000)>
    <#assign AFEC_IBCTL = "0x2U">
<#else>
    <#assign AFEC_IBCTL = "0x3U">
</#if>
<#list 0..(AFEC_NUM_CHANNELS - 1) as i>
<#assign AFEC_CH_CHER = "AFEC_"+i+"_CHER">
<#assign AFEC_CH_POS_INP = "AFEC_"+i+"_POS_INP">
<#assign AFEC_CH_NEG_INP = "AFEC_"+i+"_NEG_INP">
<#assign AFEC_CH_SHMR_DUAL = "AFEC_"+i+"_SHMR_DUAL">
<#assign AFEC_CH_CGR_GAIN = "AFEC_"+i+"_CGR_GAIN">
<#assign AFEC_CH_COCR_AOFF = "AFEC_"+i+"_COCR_AOFF">
<#assign AFEC_CH_IER_EOC = "AFEC_"+i+"_IER_EOC">
<#assign AFEC_CH_SEQ1R_USCH = "AFEC_SEQ1R_USCH"+i>
<#assign AFEC_CH_SHMR_DUAL_PAIR = "">
<#assign AFEC_CH_DIFF_PAIR = "">

<#if (.vars[AFEC_CH_CHER] == true) && (.vars[AFEC_CH_IER_EOC] == true)>
    <#assign AFEC_INTERRUPT = true>
</#if>

<#-- Differential mode -->
<#if i % 2 == 0>
    <#if .vars[AFEC_CH_CHER] == true && .vars[AFEC_CH_NEG_INP] != "GND">
        <#if AFEC_DIFFR_DIFF != "">
            <#assign AFEC_DIFFR_DIFF = AFEC_DIFFR_DIFF + " | " + "AFEC_DIFFR_DIFF"+i+"_Msk">
        <#else>
            <#assign AFEC_DIFFR_DIFF = "AFEC_DIFFR_DIFF"+i+"_Msk">
        </#if>
    </#if>
</#if>

<#if i % 2 !=0 >
<#-- Save the diff mode of the even channel. Do not configure odd paired channel if diff mode is enabled for even channel -->
    <#assign AFEC_CH_DIFF_PAIR = "AFEC_"+(i-1)+"_NEG_INP">
</#if>

<#if i gt 5>
<#-- Save the dual mode of the paired channel. Do not set the enable bit of the paired channel (channel > 5) if dual mode is enabled -->
    <#assign AFEC_CH_SHMR_DUAL_PAIR = "AFEC_"+(i-6)+"_SHMR_DUAL">
</#if>

<#-- GAIN -->
<#if .vars[AFEC_CH_CHER] == true>
    <#if (i % 2 != 0) && (.vars[AFEC_CH_DIFF_PAIR] != "GND")>
    <#else>
        <#if AFEC_CGR_GAIN != "">
            <#assign AFEC_CGR_GAIN = AFEC_CGR_GAIN + " | \n\t\t" + "AFEC_CGR_GAIN" + i +"(AFEC_CGR_GAIN_${.vars[AFEC_CH_CGR_GAIN]})">
        <#else>
            <#assign AFEC_CGR_GAIN = "AFEC_CGR_GAIN" + i +"(AFEC_CGR_GAIN_${.vars[AFEC_CH_CGR_GAIN]})">
        </#if>
    </#if>
</#if>

<#-- Interrupt -->
<#if .vars[AFEC_CH_CHER] == true && .vars[AFEC_CH_IER_EOC] == true>
    <#if (i % 2 != 0) && (.vars[AFEC_CH_DIFF_PAIR] != "GND")>
    <#else>
        <#if AFEC_IER_EOC != "">
            <#assign AFEC_IER_EOC = AFEC_IER_EOC + " | " + "AFEC_IER_EOC"+i+"_Msk">
        <#else>
            <#assign AFEC_IER_EOC = "AFEC_IER_EOC"+i+"_Msk">
        </#if>
    </#if>
</#if>

<#-- Dual sample and hold -->
<#if i < 6>
    <#if .vars[AFEC_CH_CHER] == true && .vars[AFEC_CH_SHMR_DUAL] == true>
        <#if (i % 2 != 0) && (.vars[AFEC_CH_DIFF_PAIR] != "GND")>
        <#else>
            <#if AFEC_SHMR_DUAL != "">
                <#assign AFEC_SHMR_DUAL = AFEC_SHMR_DUAL + " | " + "AFEC_SHMR_DUAL"+i+"_Msk">
            <#else>
                <#assign AFEC_SHMR_DUAL = "AFEC_SHMR_DUAL"+i+"_Msk">
            </#if>
        </#if>
    </#if>
</#if> <#-- (if i < 6) -->

<#-- Channel enable if user sequence is disabled -->
<#if AFEC_MR_USEQ == false>
    <#if .vars[AFEC_CH_CHER] == true>
        <#if ((i gt 5) && (.vars[AFEC_CH_SHMR_DUAL_PAIR] == true)) || ((i % 2 != 0) && (.vars[AFEC_CH_DIFF_PAIR] != "GND"))>
        <#else>
            <#if AFEC_CHER_CH != "">
                <#assign AFEC_CHER_CH = AFEC_CHER_CH + " | " + "AFEC_CHER_CH"+i+"_Msk">
            <#else>
                <#assign AFEC_CHER_CH = "AFEC_CHER_CH"+i+"_Msk">
            </#if>
        </#if>
    </#if>
</#if>

<#-- User conversion sequence -->
<#if AFEC_MR_USEQ == true>
    <#if .vars[AFEC_CH_SEQ1R_USCH] != "NONE">
        <#if i < 8>
            <#if AFEC_SEQ1R_USCH != "">
                <#assign AFEC_SEQ1R_USCH = AFEC_SEQ1R_USCH + " | \n\t\t" + "AFEC_SEQ1R_USCH"+i+"(AFEC_"+.vars[AFEC_CH_SEQ1R_USCH]+")">
            <#else>
                <#assign AFEC_SEQ1R_USCH = "AFEC_SEQ1R_USCH"+i+"(AFEC_"+.vars[AFEC_CH_SEQ1R_USCH]+")">
            </#if>
        <#else>
            <#if AFEC_SEQ2R_USCH != "">
                <#assign AFEC_SEQ2R_USCH = AFEC_SEQ2R_USCH + " | \n\t\t" + "AFEC_SEQ2R_USCH"+i+"(AFEC_"+.vars[AFEC_CH_SEQ1R_USCH]+")">
            <#else>
                <#assign AFEC_SEQ2R_USCH = "AFEC_SEQ2R_USCH"+i+"(AFEC_"+.vars[AFEC_CH_SEQ1R_USCH]+")">
            </#if>
        </#if>
        <#if AFEC_CHER_CH != "">
            <#assign AFEC_CHER_CH = AFEC_CHER_CH + " | " + "AFEC_CHER_CH"+i+"_Msk">
        <#else>
            <#assign AFEC_CHER_CH = "AFEC_CHER_CH"+i+"_Msk">
        </#if>
    </#if>
</#if>

</#list>

<#if AFEC_EMR_RES_VALUE == "0">
    <#assign AFEC_RES = "AFEC_EMR_RES_NO_AVERAGE">
    <#assign AFEC_STM = "">
<#elseif AFEC_EMR_RES_VALUE == "1">
    <#assign AFEC_RES = "AFEC_EMR_RES_OSR4">
    <#assign AFEC_STM = "| (AFEC_EMR_STM_Msk)">
<#elseif AFEC_EMR_RES_VALUE == "2">
    <#assign AFEC_RES = "AFEC_EMR_RES_OSR4">
    <#assign AFEC_STM = "">
<#elseif AFEC_EMR_RES_VALUE == "3">
    <#assign AFEC_RES = "AFEC_EMR_RES_OSR16">
    <#assign AFEC_STM = "| (AFEC_EMR_STM_Msk)">
<#elseif AFEC_EMR_RES_VALUE == "4">
    <#assign AFEC_RES = "AFEC_EMR_RES_OSR16">
    <#assign AFEC_STM = "">
<#elseif AFEC_EMR_RES_VALUE == "5">
    <#assign AFEC_RES = "AFEC_EMR_RES_OSR64">
    <#assign AFEC_STM = "| (AFEC_EMR_STM_Msk)">
<#elseif AFEC_EMR_RES_VALUE == "6">
    <#assign AFEC_RES = "AFEC_EMR_RES_OSR64">
    <#assign AFEC_STM = "">
<#elseif AFEC_EMR_RES_VALUE == "7">
    <#assign AFEC_RES = "AFEC_EMR_RES_OSR256">
    <#assign AFEC_STM = "| (AFEC_EMR_STM_Msk)">
<#elseif AFEC_EMR_RES_VALUE == "8">
    <#assign AFEC_RES = "AFEC_EMR_RES_OSR256">
    <#assign AFEC_STM = "">
</#if>

</#compress>

<#-- *********************************************************************************************** -->
// *****************************************************************************
// *****************************************************************************
// Section: ${AFEC_INSTANCE_NAME} Implementation
// *****************************************************************************
// *****************************************************************************
<#if AFEC_INTERRUPT == true>
    <#lt>/* Object to hold callback function and context */
    <#lt>AFEC_CALLBACK_OBJECT ${AFEC_INSTANCE_NAME}_CallbackObj;
</#if>

/* Initialize AFEC peripheral */
void ${AFEC_INSTANCE_NAME}_Initialize()
{
    /* Software reset */
    ${AFEC_INSTANCE_NAME}_REGS->AFEC_CR = AFEC_CR_SWRST_Msk;

    /* Prescaler and different time settings as per CLOCK section  */
    ${AFEC_INSTANCE_NAME}_REGS->AFEC_MR = AFEC_MR_PRESCAL(${AFEC_MR_PRESCAL}U) | AFEC_MR_TRACKTIM(15U) | AFEC_MR_STARTUP_SUT64 |
        AFEC_MR_TRANSFER(2U) | AFEC_MR_ONE_Msk ${(AFEC_CONV_MODE == "0")?then('| AFEC_MR_FREERUN_Msk', '')} <#rt>
        <#lt> ${(AFEC_CONV_MODE == "2")?then('| (AFEC_MR_TRGEN_Msk) | (AFEC_MR_${AFEC_MR_TRGSEL_VALUE})', '')};

    /* resolution and sign mode of result */
    ${AFEC_INSTANCE_NAME}_REGS->AFEC_EMR = ${AFEC_RES} ${AFEC_STM}
         | AFEC_EMR_SIGNMODE_${AFEC_EMR_SIGNMODE_VALUE} | AFEC_EMR_TAG_Msk;

    /* Enable gain amplifiers */
    ${AFEC_INSTANCE_NAME}_REGS->AFEC_ACR = AFEC_ACR_PGA0EN_Msk | AFEC_ACR_PGA1EN_Msk | AFEC_ACR_IBCTL(${AFEC_IBCTL});

<#if AFEC_CGR_GAIN?has_content>
    /* Gain */
    ${AFEC_INSTANCE_NAME}_REGS->AFEC_CGR = ${AFEC_CGR_GAIN};

</#if>
<#if AFEC_DIFFR_DIFF?has_content>
    /* Differential mode */
    ${AFEC_INSTANCE_NAME}_REGS->AFEC_DIFFR = ${AFEC_DIFFR_DIFF};

</#if>
<#if AFEC_SHMR_DUAL?has_content>
    /* Dual sample and hold mode */
    ${AFEC_INSTANCE_NAME}_REGS->AFEC_SHMR = ${AFEC_SHMR_DUAL};

</#if>
<#list 0..(AFEC_NUM_CHANNELS - 1) as i>
    <#assign AFEC_CH_CHER = "AFEC_"+i+"_CHER">
    <#assign AFEC_CH_OFFSET = "AFEC_"+i+"_COCR_AOFF">
    <#assign AFEC_CH_NEG_INP = "AFEC_"+i+"_NEG_INP">
    <#assign AFEC_CH_DIFF_PAIR = "">
    <#if i % 2 !=0 >
        <#assign AFEC_CH_DIFF_PAIR = "AFEC_"+(i-1)+"_NEG_INP">
    </#if>
    <#if .vars[AFEC_CH_CHER] == true>
        <#if (i % 2 != 0) && (.vars[AFEC_CH_DIFF_PAIR] != "GND")>
        <#else>
        <#lt>    /* Offset */
        <#lt>    ${AFEC_INSTANCE_NAME}_REGS->AFEC_CSELR = AFEC_CH${i};
        <#lt>    ${AFEC_INSTANCE_NAME}_REGS->AFEC_COCR = ${.vars[AFEC_CH_OFFSET]}U;
        </#if>
    </#if>
</#list>

<#if AFEC_MR_USEQ == true>
    /* User defined channel conversion sequence */
    ${AFEC_INSTANCE_NAME}_REGS->AFEC_MR |= AFEC_MR_USEQ_Msk;
    <#if AFEC_SEQ1R_USCH?has_content>
    <#lt>   ${AFEC_INSTANCE_NAME}_REGS->AFEC_SEQ1R = ${AFEC_SEQ1R_USCH};
    </#if>
    <#if AFEC_SEQ2R_USCH?has_content>
    <#lt>   ${AFEC_INSTANCE_NAME}_REGS->AFEC_SEQ2R = ${AFEC_SEQ2R_USCH};
    </#if>
</#if>

<#if AFEC_IER_EOC?has_content>
    /* Enable interrupt */
    ${AFEC_INSTANCE_NAME}_REGS->AFEC_IER = ${AFEC_IER_EOC};
    ${AFEC_INSTANCE_NAME}_CallbackObj.callback_fn = NULL;
</#if>

<#if AFEC_CHER_CH?has_content>
    /* Enable channel */
    ${AFEC_INSTANCE_NAME}_REGS->AFEC_CHER = ${AFEC_CHER_CH};
</#if>
}

/* Enable AFEC channels */
void ${AFEC_INSTANCE_NAME}_ChannelsEnable (AFEC_CHANNEL_MASK channelsMask)
{
    ${AFEC_INSTANCE_NAME}_REGS->AFEC_CHER |= channelsMask;
}

/* Disable AFEC channels */
void ${AFEC_INSTANCE_NAME}_ChannelsDisable (AFEC_CHANNEL_MASK channelsMask)
{
    ${AFEC_INSTANCE_NAME}_REGS->AFEC_CHDR |= channelsMask;
}

/* Enable channel end of conversion interrupt */
void ${AFEC_INSTANCE_NAME}_ChannelsInterruptEnable (AFEC_INTERRUPT_MASK channelsInterruptMask)
{
    ${AFEC_INSTANCE_NAME}_REGS->AFEC_IER |= channelsInterruptMask;
}

/* Disable channel end of conversion interrupt */
void ${AFEC_INSTANCE_NAME}_ChannelsInterruptDisable (AFEC_INTERRUPT_MASK channelsInterruptMask)
{
    ${AFEC_INSTANCE_NAME}_REGS->AFEC_IDR |= channelsInterruptMask;
}

/* Start the conversion with software trigger */
void ${AFEC_INSTANCE_NAME}_ConversionStart(void)
{
    ${AFEC_INSTANCE_NAME}_REGS->AFEC_CR = 0x1U << AFEC_CR_START_Pos;
}

/*Check if conversion result is available */
bool ${AFEC_INSTANCE_NAME}_ChannelResultIsReady(AFEC_CHANNEL_NUM channel)
{
    return (${AFEC_INSTANCE_NAME}_REGS->AFEC_ISR>> channel) & 0x1U;
}

/* Read the conversion result */
uint16_t ${AFEC_INSTANCE_NAME}_ChannelResultGet(AFEC_CHANNEL_NUM channel)
{
    ${AFEC_INSTANCE_NAME}_REGS->AFEC_CSELR = channel;
    return (${AFEC_INSTANCE_NAME}_REGS->AFEC_CDR);
}

/* Configure the user defined conversion sequence */
void ${AFEC_INSTANCE_NAME}_ConversionSequenceSet(AFEC_CHANNEL_NUM *channelList, uint8_t numChannel)
{
    uint8_t channelIndex;
    ${AFEC_INSTANCE_NAME}_REGS->AFEC_SEQ1R = 0U;
    ${AFEC_INSTANCE_NAME}_REGS->AFEC_SEQ2R = 0U;

    for (channelIndex = 0U; channelIndex < AFEC_SEQ1_CHANNEL_NUM; channelIndex++)
    {
        if (channelIndex >= numChannel)
            break;
        ${AFEC_INSTANCE_NAME}_REGS->AFEC_SEQ1R |= channelList[channelIndex] << (channelIndex * 4U);
    }
    if (numChannel > AFEC_SEQ1_CHANNEL_NUM)
    {
        for (channelIndex = 0U; channelIndex < (numChannel - AFEC_SEQ1_CHANNEL_NUM); channelIndex++)
        {
            ${AFEC_INSTANCE_NAME}_REGS->AFEC_SEQ2R |= channelList[channelIndex + AFEC_SEQ1_CHANNEL_NUM] << (channelIndex * 4U);
        }
    }
}

/* Set the channel gain */
void ${AFEC_INSTANCE_NAME}_ChannelGainSet(AFEC_CHANNEL_NUM channel, AFEC_CHANNEL_GAIN gain)
{
    ${AFEC_INSTANCE_NAME}_REGS->AFEC_CGR &= ~(0x03U << (2U * channel));
    ${AFEC_INSTANCE_NAME}_REGS->AFEC_CGR |= (gain << ( 2U * channel));
}

/* Set the channel offset */
void ${AFEC_INSTANCE_NAME}_ChannelOffsetSet(AFEC_CHANNEL_NUM channel, uint16_t offset)
{
    ${AFEC_INSTANCE_NAME}_REGS->AFEC_CSELR = channel;
    ${AFEC_INSTANCE_NAME}_REGS->AFEC_COCR = offset;
}

<#if AFEC_INTERRUPT == true>
    <#lt>/* Register the callback function */
    <#lt>void ${AFEC_INSTANCE_NAME}_CallbackRegister(AFEC_CALLBACK callback, uintptr_t context)
    <#lt>{
    <#lt>    ${AFEC_INSTANCE_NAME}_CallbackObj.callback_fn = callback;
    <#lt>    ${AFEC_INSTANCE_NAME}_CallbackObj.context = context;
    <#lt>}
</#if>

<#if AFEC_INTERRUPT == true>
    <#lt>/* Interrupt Handler */
    <#lt>void ${AFEC_INSTANCE_NAME}_InterruptHandler(void)
    <#lt>{
    <#lt>    if (${AFEC_INSTANCE_NAME}_CallbackObj.callback_fn != NULL)
    <#lt>    {
    <#lt>        ${AFEC_INSTANCE_NAME}_CallbackObj.callback_fn(${AFEC_INSTANCE_NAME}_CallbackObj.context);
    <#lt>    }
    <#lt>}
</#if>
