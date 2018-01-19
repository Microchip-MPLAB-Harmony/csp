/*******************************************************************************
  AFEC Peripheral Library Interface Source File

  Company
    Microchip Technology Inc.

  File Name
    plib_afec.c

  Summary
    AFEC peripheral library source.

  Description
    This file implements the AFEC peripheral library.  

*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
Copyright (c) 2017 released Microchip Technology Inc.  All rights reserved.

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
#include "${__PROCESSOR}.h" 
#include "plib_afec${INDEX}.h"

#define AFEC_SEQ1_CHANNEL_NUM (8U)

#define AFEC_CGR_GAIN_X1   (0x00U)
#define AFEC_CGR_GAIN_X2   (0x01U)
#define AFEC_CGR_GAIN_x4   (0x03U)

<#compress> <#-- To remove unwanted new lines -->
<#assign AFEC_CGR_GAIN = "">
<#assign AFEC_DIFFR_DIFF = "">
<#assign AFEC_SHMR_DUAL = "">
<#assign AFEC_IER_EOC = "">
<#assign AFEC_CHER_CH = "">
<#assign AFEC_SEQ1R_USCH = "">
<#assign AFEC_SEQ2R_USCH = "">
<#assign AFEC_INTERRUPT = false>

<#list 0..11 as i>
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
</#compress>
<#-- *********************************************************************************************** -->
<#if AFEC_INTERRUPT == true>
	<#lt>/* Object to hold callback function and context */
	<#lt>AFEC_CALLBACK_OBJECT AFEC${INDEX}_CallbackObj;
</#if>

/* Initialize AFEC peripheral */
void AFEC${INDEX}_Initialize()
{
	/* Software reset */
	_AFEC${INDEX}_REGS->AFEC_CR.w = AFEC_CR_SWRST_Msk;
	
	/* Prescaler and different time settings as per CLOCK section  */
	_AFEC${INDEX}_REGS->AFEC_MR.w = AFEC_MR_PRESCAL(${AFEC_MR_PRESCAL}U) | AFEC_MR_TRACKTIM(15U) |
		AFEC_MR_TRANSFER(2U) | AFEC_MR_ONE_Msk ${AFEC_MR_FREERUN?then('| AFEC_MR_FREERUN_Msk', '')} <#rt>
		<#lt>${AFEC_MR_TRGEN?then('| (AFEC_MR_TRGEN_Msk) | (AFEC_MR_${AFEC_MR_TRGSEL_VALUE})', '')};
		
	/* resolution and sign mode of result */
	_AFEC${INDEX}_REGS->AFEC_EMR.w = AFEC_EMR_RES_${AFEC_EMR_RES_VALUE} 
		${AFEC_EMR_STM?then(' | (AFEC_EMR_STM_Mask)', '')} | AFEC_EMR_SIGNMODE_${AFEC_EMR_SIGNMODE_VALUE} | AFEC_EMR_TAG_Msk;
		
	/* Enable gain amplifiers */
	_AFEC${INDEX}_REGS->AFEC_ACR.w = AFEC_ACR_PGA0EN_Msk | AFEC_ACR_PGA1EN_Msk;
	
<#if AFEC_CGR_GAIN?hasContent>
	/* Gain */
	_AFEC${INDEX}_REGS->AFEC_CGR.w = ${AFEC_CGR_GAIN};
	
</#if>
<#if AFEC_DIFFR_DIFF?hasContent>
	/* Differential mode */
	_AFEC${INDEX}_REGS->AFEC_DIFFR.w = ${AFEC_DIFFR_DIFF};
	
</#if>
<#if AFEC_SHMR_DUAL?hasContent>
	/* Dual sample and hold mode */
	_AFEC${INDEX}_REGS->AFEC_SHMR.w = ${AFEC_SHMR_DUAL};
	
</#if>
<#list 0..11 as i>
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
			/* Offset */
		<#lt>	_AFEC${INDEX}_REGS->AFEC_CSELR.w = AFEC_CH${i};
		<#lt>	_AFEC${INDEX}_REGS->AFEC_COCR.w = ${.vars[AFEC_CH_OFFSET]}U;
		</#if>
	</#if>
</#list>

<#if AFEC_MR_USEQ == true>
	/* User defined channel conversion sequence */
	_AFEC${INDEX}_REGS->AFEC_MR.w |= AFEC_MR_USEQ_Msk;
	<#if AFEC_SEQ1R_USCH?hasContent>
	<#lt>	_AFEC${INDEX}_REGS->AFEC_SEQ1R.w = ${AFEC_SEQ1R_USCH};
	</#if>
	<#if AFEC_SEQ2R_USCH?hasContent>
	<#lt>	_AFEC${INDEX}_REGS->AFEC_SEQ2R.w = ${AFEC_SEQ2R_USCH}; 
	</#if>
</#if>
	
<#if AFEC_IER_EOC?hasContent>
	/* Enable interrupt */
	_AFEC${INDEX}_REGS->AFEC_IER.w = ${AFEC_IER_EOC};
</#if>
	
<#if AFEC_CHER_CH?hasContent>
	/* Enable channel */
	_AFEC${INDEX}_REGS->AFEC_CHER.w = ${AFEC_CHER_CH};
</#if>
}

/* Enable AFEC channels */
void AFEC${INDEX}_ChannelsEnable (AFEC_CHANNEL_MASK channelsMask)
{
	_AFEC${INDEX}_REGS->AFEC_CHER.w |= channelsMask;
}

/* Disable AFEC channels */
void AFEC${INDEX}_ChannelsDisable (AFEC_CHANNEL_MASK channelsMask)
{
	_AFEC${INDEX}_REGS->AFEC_CHDR.w |= channelsMask;
}

/* Enable channel end of conversion interrupt */
void AFEC${INDEX}_ChannelsInterruptEnable (AFEC_INTERRUPT_MASK channelsInterruptMask)
{
	_AFEC${INDEX}_REGS->AFEC_IER.w |= channelsInterruptMask;
}

/* Disable channel end of conversion interrupt */
void AFEC${INDEX}_ChannelsInterruptDisable (AFEC_INTERRUPT_MASK channelsInterruptMask)
{
	_AFEC${INDEX}_REGS->AFEC_IDR.w |= channelsInterruptMask;
}

/* Start the conversion with software trigger */
void AFEC${INDEX}_ConversionStart(void)
{
	_AFEC${INDEX}_REGS->AFEC_CR.w = 0x1U << AFEC_CR_START_Pos;
}

/*Check if conversion result is available */
bool AFEC${INDEX}_ChannelResultReady(AFEC_CHANNEL_NUM channel)
{
	return (_AFEC${INDEX}_REGS->AFEC_ISR.w >> channel) & 0x1U;
}

/* Read the conversion result */
uint16_t AFEC${INDEX}_ChannelResultGet(AFEC_CHANNEL_NUM channel)
{
	_AFEC${INDEX}_REGS->AFEC_CSELR.w = channel;
	return (_AFEC${INDEX}_REGS->AFEC_CDR.w);
}

/* Configure the user defined conversion sequence */
void AFEC${INDEX}_ConversionSequenceSet(AFEC_CHANNEL_NUM *channelList, uint8_t numChannel)
{
	uint8_t channelIndex;
	_AFEC${INDEX}_REGS->AFEC_SEQ1R.w = 0U;
	_AFEC${INDEX}_REGS->AFEC_SEQ2R.w = 0U;

	for (channelIndex = 0U; channelIndex < AFEC_SEQ1_CHANNEL_NUM; channelIndex++)
	{
		if (channelIndex >= numChannel) 
			break;
		_AFEC${INDEX}_REGS->AFEC_SEQ1R.w |= channelList[channelIndex] << (channelIndex * 4U);
	}
	if (numChannel > AFEC_SEQ1_CHANNEL_NUM)
	{
		for (channelIndex = 0U; channelIndex < (numChannel - AFEC_SEQ1_CHANNEL_NUM); channelIndex++)
		{
			_AFEC${INDEX}_REGS->AFEC_SEQ2R.w |= channelList[channelIndex + AFEC_SEQ1_CHANNEL_NUM] << (channelIndex * 4U);
		}
	}
}

/* Set the channel gain */
void AFEC${INDEX}_ChannelGainSet(AFEC_CHANNEL_NUM channel, AFEC_CHANNEL_GAIN gain)
{
	_AFEC${INDEX}_REGS->AFEC_CGR.w &= ~(0x03U << (2U * channel));
	_AFEC${INDEX}_REGS->AFEC_CGR.w |= (gain << ( 2U * channel));
}

/* Set the channel offset */
void AFEC${INDEX}_ChannelOffsetSet(AFEC_CHANNEL_NUM channel, uint16_t offset)
{
	_AFEC${INDEX}_REGS->AFEC_CSELR.w = channel;
	_AFEC${INDEX}_REGS->AFEC_COCR.w = offset;
}

<#if AFEC_INTERRUPT == true>
	<#lt>/* Register the callback function */
	<#lt>void AFEC${INDEX}_CallbackSet(AFEC_CALLBACK callback, uintptr_t context)
	<#lt>{
	<#lt>	AFEC${INDEX}_CallbackObj.callback_fn = callback;
	<#lt>	AFEC${INDEX}_CallbackObj.context = context;
	<#lt>}
</#if>

<#if AFEC_INTERRUPT == true>
	<#lt>/* Interrupt Handler */
	<#lt>void AFEC${INDEX}_InterruptHandler(void)
	<#lt>{
	<#lt>	if (AFEC${INDEX}_CallbackObj.callback_fn != NULL)
	<#lt>	{
	<#lt>		AFEC${INDEX}_CallbackObj.callback_fn(AFEC${INDEX}_CallbackObj.context, 
	<#lt>										 _AFEC${INDEX}_REGS->AFEC_ISR.w);
	<#lt>	}
	<#lt>}
</#if>
