/*******************************************************************************
  AFEC Peripheral Library Interface Header File

  Company
    Microchip Technology Inc.

  File Name
    plib_afec.h

  Summary
    AFEC peripheral library interface.

  Description
    This file defines the interface to the AFEC peripheral library.  This 
    library provides access to and control of the associated peripheral 
    instance.

  Remarks:
    This header is for documentation only.  The actual afec<x> headers will be
    generated as required by the MCC (where <x> is the peripheral instance 
    number).

    Every interface symbol has a lower-case 'x' in it following the "AFEC" 
    abbreviation.  This 'x' will be replaced by the peripheral instance number
    in the generated headers.  These are the actual functions that should be
    used.
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


#include "plib_afec${INDEX}.h"

#define AFEC_SEQ1_CHANNEL_NUM (8U)

#define AFEC_CGR_GAIN_X1   (0x00)
#define AFEC_CGR_GAIN_X2   (0x01)
#define AFEC_CGR_GAIN_x4   (0x03)

#define AFEC_NONE (0x00)

void AFEC${INDEX}_Initialize()
{
	/* Enable peripheral clock */
	<#if INDEX == 0>   
    _PMC_REGS->PMC_PCER0.w |= PMC_PCER0_PID29_Msk;
	<#else>
    _PMC_REGS->PMC_PCER1.w |= PMC_PCER1_PID40_Msk;
	</#if>

	/* Software reset */
	_AFEC${INDEX}_REGS->AFEC_CR.w = AFEC_CR_SWRST_Msk;
	
	/* Prescaler and different time settings as per CLOCK section  */
	_AFEC${INDEX}_REGS->AFEC_MR.w = AFEC_MR_PRESCAL(${AFEC_MR_PRESCAL}) | AFEC_MR_TRACKTIM(15) |
		AFEC_MR_TRANSFER(2) | AFEC_MR_ONE_Msk;
	
	/* resolution and sign mode of result */
	_AFEC${INDEX}_REGS->AFEC_EMR.w = AFEC_EMR_RES_${AFEC_EMR_RES} |
		AFEC_EMR_SIGNMODE_${AFEC_EMR_SIGNMODE} | AFEC_EMR_TAG_Msk;

	<#if AFEC_MR_FREERUN == true>
	/* free run mode */
	_AFEC${INDEX}_REGS->AFEC_MR.w |= AFEC_MR_FREERUN_Msk;
	</#if>
	
	<#if AFEC_MR_TRGEN == true>
	/* trigger settings  */
	_AFEC${INDEX}_REGS->AFEC_MR.w |= (AFEC_MR_TRGEN_Msk) | (AFEC_MR_TRGSEL_${AFEC_MR_TRGSEL});
	</#if>
	
	/* Enable gain amplifiers */
	_AFEC${INDEX}_REGS->AFEC_ACR.w = AFEC_ACR_PGA0EN_Msk | AFEC_ACR_PGA1EN_Msk;
	
<#if AFEC_CHER_CH0 == true>
	/**** Channel 0 *********/
	_AFEC${INDEX}_REGS->AFEC_CGR.w = AFEC_CGR_GAIN0(AFEC_CGR_GAIN_${AFEC_CGR_GAIN0});
	/* offset */
	_AFEC${INDEX}_REGS->AFEC_CSELR.w = AFEC_CH0;
	_AFEC${INDEX}_REGS->AFEC_COCR.w = ${AFEC_COCR_AOFF0};
	<#if AFEC_CH0_NEG_INP != "GND">
	/* Differential input mode */
	_AFEC${INDEX}_REGS->AFEC_DIFFR.w = AFEC_DIFFR_DIFF0_Msk; 
	</#if>
	<#if AFEC_SHMR_DUAL0 >
	/* Dual sample and hold */
	_AFEC${INDEX}_REGS->AFEC_SHMR.w = AFEC_SHMR_DUAL0_Msk;
	</#if>
	<#if AFEC_IER_EOC0 >
	/* End of conversion interrupt */
	_AFEC${INDEX}_REGS->AFEC_IER.w = AFEC_IER_EOC0_Msk; 
	</#if>
	<#if AFEC_MR_USEQ == false>
	/* Enable channel */
	_AFEC${INDEX}_REGS->AFEC_CHER.w = AFEC_CHER_CH0_Msk;
	</#if>
</#if>

<#if AFEC_CHER_CH1 == true>
	/**** Channel 1 *********/
	_AFEC${INDEX}_REGS->AFEC_CGR.w |= AFEC_CGR_GAIN1(AFEC_CGR_GAIN_${AFEC_CGR_GAIN1});
	/* offset */
	_AFEC${INDEX}_REGS->AFEC_CSELR.w = AFEC_CH1;
	_AFEC${INDEX}_REGS->AFEC_COCR.w = ${AFEC_COCR_AOFF1};
	<#if AFEC_SHMR_DUAL1 >
	/* Dual sample and hold */
	_AFEC${INDEX}_REGS->AFEC_SHMR.w |= AFEC_SHMR_DUAL1_Msk;
	</#if>
	<#if AFEC_IER_EOC1 >
	/* End of conversion interrupt */
	_AFEC${INDEX}_REGS->AFEC_IER.w |= AFEC_IER_EOC1_Msk; 
	</#if>
	<#if AFEC_MR_USEQ == false>
	/* Enable channel */
	_AFEC${INDEX}_REGS->AFEC_CHER.w |= AFEC_CHER_CH1_Msk;
	</#if>
</#if>

<#if AFEC_CHER_CH2 == true>
	/**** Channel 2 *********/
	_AFEC${INDEX}_REGS->AFEC_CGR.w |= AFEC_CGR_GAIN2(AFEC_CGR_GAIN_${AFEC_CGR_GAIN2});
	/* offset */
	_AFEC${INDEX}_REGS->AFEC_CSELR.w = AFEC_CH2;
	_AFEC${INDEX}_REGS->AFEC_COCR.w = ${AFEC_COCR_AOFF2};
	<#if AFEC_CH2_NEG_INP != "GND">
	/* Differential input mode */
	_AFEC${INDEX}_REGS->AFEC_DIFFR.w |= AFEC_DIFFR_DIFF2_Msk; 
	</#if>
	<#if AFEC_SHMR_DUAL2 >
	/* Dual sample and hold */
	_AFEC${INDEX}_REGS->AFEC_SHMR.w |= AFEC_SHMR_DUAL2_Msk;
	</#if>
	<#if AFEC_IER_EOC2 >
	/* End of conversion interrupt */
	_AFEC${INDEX}_REGS->AFEC_IER.w |= AFEC_IER_EOC2_Msk; 
	</#if>
	<#if AFEC_MR_USEQ == false>
	/* Enable channel */
	_AFEC${INDEX}_REGS->AFEC_CHER.w |= AFEC_CHER_CH2_Msk;
	</#if>
</#if>

<#if AFEC_CHER_CH3 == true>
	/**** Channel 3 *********/
	_AFEC${INDEX}_REGS->AFEC_CGR.w |= AFEC_CGR_GAIN3(AFEC_CGR_GAIN_${AFEC_CGR_GAIN3});
	/* offset */
	_AFEC${INDEX}_REGS->AFEC_CSELR.w = AFEC_CH3;
	_AFEC${INDEX}_REGS->AFEC_COCR.w = ${AFEC_COCR_AOFF3};
	<#if AFEC_SHMR_DUAL3 >
	/* Dual sample and hold */
	_AFEC${INDEX}_REGS->AFEC_SHMR.w |= AFEC_SHMR_DUAL3_Msk;
	</#if>
	<#if AFEC_IER_EOC3 >
	/* End of conversion interrupt */
	_AFEC${INDEX}_REGS->AFEC_IER.w |= AFEC_IER_EOC3_Msk; 
	</#if>
	<#if AFEC_MR_USEQ == false>
	/* Enable channel */
	_AFEC${INDEX}_REGS->AFEC_CHER.w |= AFEC_CHER_CH3_Msk;
	</#if>
</#if>

<#if AFEC_CHER_CH4 == true>
	/**** Channel 4 *********/
	_AFEC${INDEX}_REGS->AFEC_CGR.w |= AFEC_CGR_GAIN4(AFEC_CGR_GAIN_${AFEC_CGR_GAIN4});
	/* offset */
	_AFEC${INDEX}_REGS->AFEC_CSELR.w = AFEC_CH4;
	_AFEC${INDEX}_REGS->AFEC_COCR.w = ${AFEC_COCR_AOFF4};
	<#if AFEC_CH4_NEG_INP != "GND">
	/* Differential input mode */
	_AFEC${INDEX}_REGS->AFEC_DIFFR.w |= AFEC_DIFFR_DIFF4_Msk; 
	</#if>
	<#if AFEC_SHMR_DUAL4 >
	/* Dual sample and hold */
	_AFEC${INDEX}_REGS->AFEC_SHMR.w |= AFEC_SHMR_DUAL4_Msk;
	</#if>
	<#if AFEC_IER_EOC4 >
	/* End of conversion interrupt */
	_AFEC${INDEX}_REGS->AFEC_IER.w |= AFEC_IER_EOC4_Msk; 
	</#if>
	<#if AFEC_MR_USEQ == false>
	/* Enable channel */
	_AFEC${INDEX}_REGS->AFEC_CHER.w |= AFEC_CHER_CH4_Msk;
	</#if>
</#if>

<#if AFEC_CHER_CH5 == true>
	/**** Channel 5 *********/
	_AFEC${INDEX}_REGS->AFEC_CGR.w |= AFEC_CGR_GAIN5(AFEC_CGR_GAIN_${AFEC_CGR_GAIN5});
	/* offset */
	_AFEC${INDEX}_REGS->AFEC_CSELR.w = AFEC_CH5;
	_AFEC${INDEX}_REGS->AFEC_COCR.w = ${AFEC_COCR_AOFF5};
	<#if AFEC_SHMR_DUAL5 >
	/* Dual sample and hold */
	_AFEC${INDEX}_REGS->AFEC_SHMR.w |= AFEC_SHMR_DUAL5_Msk;
	</#if>
	<#if AFEC_IER_EOC5 >
	/* End of conversion interrupt */
	_AFEC${INDEX}_REGS->AFEC_IER.w |= AFEC_IER_EOC5_Msk; 
	</#if>
	<#if AFEC_MR_USEQ == false>
	/* Enable channel */
	_AFEC${INDEX}_REGS->AFEC_CHER.w |= AFEC_CHER_CH5_Msk;
	</#if>
</#if>

<#if AFEC_CHER_CH6 == true || AFEC_SHMR_DUAL0 == true>
	/**** Channel 6 *********/
	_AFEC${INDEX}_REGS->AFEC_CGR.w |= AFEC_CGR_GAIN6(AFEC_CGR_GAIN_${AFEC_CGR_GAIN6});
	/* offset */
	_AFEC${INDEX}_REGS->AFEC_CSELR.w = AFEC_CH6;
	_AFEC${INDEX}_REGS->AFEC_COCR.w = ${AFEC_COCR_AOFF6};
	<#if AFEC_CH6_NEG_INP != "GND">
	/* Differential input mode */
	_AFEC${INDEX}_REGS->AFEC_DIFFR.w |= AFEC_DIFFR_DIFF6_Msk; 
	</#if>
	<#if AFEC_IER_EOC6 >
	/* End of conversion interrupt */
	_AFEC${INDEX}_REGS->AFEC_IER.w |= AFEC_IER_EOC6_Msk; 
	</#if>
	<#if AFEC_MR_USEQ == false>
	/* Enable channel */
	_AFEC${INDEX}_REGS->AFEC_CHER.w |= AFEC_CHER_CH6_Msk;
	</#if>
</#if>

<#if AFEC_CHER_CH7 == true || AFEC_SHMR_DUAL1 == true>
	/**** Channel 7 *********/
	_AFEC${INDEX}_REGS->AFEC_CGR.w |= AFEC_CGR_GAIN7(AFEC_CGR_GAIN_${AFEC_CGR_GAIN7});
	/* offset */
	_AFEC${INDEX}_REGS->AFEC_CSELR.w = AFEC_CH7;
	_AFEC${INDEX}_REGS->AFEC_COCR.w = ${AFEC_COCR_AOFF7};
	<#if AFEC_IER_EOC7 >
	/* End of conversion interrupt */
	_AFEC${INDEX}_REGS->AFEC_IER.w |= AFEC_IER_EOC7_Msk; 
	</#if>
	<#if AFEC_MR_USEQ == false>
	/* Enable channel */
	_AFEC${INDEX}_REGS->AFEC_CHER.w |= AFEC_CHER_CH7_Msk;
	</#if>
</#if>

<#if AFEC_CHER_CH8 == true || AFEC_SHMR_DUAL2 == true>
	/**** Channel 8 *********/
	_AFEC${INDEX}_REGS->AFEC_CGR.w |= AFEC_CGR_GAIN8(AFEC_CGR_GAIN_${AFEC_CGR_GAIN8});
	/* offset */
	_AFEC${INDEX}_REGS->AFEC_CSELR.w = AFEC_CH8;
	_AFEC${INDEX}_REGS->AFEC_COCR.w = ${AFEC_COCR_AOFF8};
	<#if AFEC_CH8_NEG_INP != "GND">
	/* Differential input mode */
	_AFEC${INDEX}_REGS->AFEC_DIFFR.w |= AFEC_DIFFR_DIFF8_Msk; 
	</#if>
	<#if AFEC_IER_EOC6 >
	/* End of conversion interrupt */
	_AFEC${INDEX}_REGS->AFEC_IER.w |= AFEC_IER_EOC8_Msk; 
	</#if>
	<#if AFEC_MR_USEQ == false>
	/* Enable channel */
	_AFEC${INDEX}_REGS->AFEC_CHER.w |= AFEC_CHER_CH8_Msk;
	</#if>
</#if>

<#if AFEC_CHER_CH9 == true || AFEC_SHMR_DUAL3 == true>
	/**** Channel 9 *********/
	_AFEC${INDEX}_REGS->AFEC_CGR.w |= AFEC_CGR_GAIN9(AFEC_CGR_GAIN_${AFEC_CGR_GAIN9});
	/* offset */
	_AFEC${INDEX}_REGS->AFEC_CSELR.w = AFEC_CH9;
	_AFEC${INDEX}_REGS->AFEC_COCR.w = ${AFEC_COCR_AOFF9};
	<#if AFEC_IER_EOC7 >
	/* End of conversion interrupt */
	_AFEC${INDEX}_REGS->AFEC_IER.w |= AFEC_IER_EOC9_Msk; 
	</#if>
	<#if AFEC_MR_USEQ == false>
	/* Enable channel */
	_AFEC${INDEX}_REGS->AFEC_CHER.w |= AFEC_CHER_CH9_Msk;
	</#if>
</#if>

<#if AFEC_CHER_CH10 == true || AFEC_SHMR_DUAL4 == true>
	/**** Channel 10 *********/
	_AFEC${INDEX}_REGS->AFEC_CGR.w |= AFEC_CGR_GAIN10(AFEC_CGR_GAIN_${AFEC_CGR_GAIN10});
	/* offset */
	_AFEC${INDEX}_REGS->AFEC_CSELR.w = AFEC_CH10;
	_AFEC${INDEX}_REGS->AFEC_COCR.w = ${AFEC_COCR_AOFF10};
	<#if AFEC_CH6_NEG_INP != "GND">
	/* Differential input mode */
	_AFEC${INDEX}_REGS->AFEC_DIFFR.w |= AFEC_DIFFR_DIFF10_Msk; 
	</#if>
	<#if AFEC_IER_EOC10 >
	/* End of conversion interrupt */
	_AFEC${INDEX}_REGS->AFEC_IER.w |= AFEC_IER_EOC10_Msk; 
	</#if>
	<#if AFEC_MR_USEQ == false>
	/* Enable channel */
	_AFEC${INDEX}_REGS->AFEC_CHER.w |= AFEC_CHER_CH10_Msk;
	</#if>
</#if>

<#if AFEC_CHER_CH11 == true || AFEC_SHMR_DUAL5 == true>
	/**** Channel 11 *********/
	_AFEC${INDEX}_REGS->AFEC_CGR.w |= AFEC_CGR_GAIN11(AFEC_CGR_GAIN_${AFEC_CGR_GAIN11});
	/* offset */
	_AFEC${INDEX}_REGS->AFEC_CSELR.w = AFEC_CH11;
	_AFEC${INDEX}_REGS->AFEC_COCR.w = ${AFEC_COCR_AOFF11};
	<#if AFEC_IER_EOC11 >
	/* End of conversion interrupt */
	_AFEC${INDEX}_REGS->AFEC_IER.w |= AFEC_IER_EOC11_Msk; 
	</#if>
	<#if AFEC_MR_USEQ == false>
	/* Enable channel */
	_AFEC${INDEX}_REGS->AFEC_CHER.w |= AFEC_CHER_CH11_Msk;
	</#if>
</#if>
	
	<#if AFEC_MR_USEQ == true>
	/* User defined channel conversion sequence */
	_AFEC${INDEX}_REGS->AFEC_MR.w |= AFEC_MR_USEQ_Msk;
	
	_AFEC${INDEX}_REGS->AFEC_SEQ1R.w = AFEC_SEQ1R_USCH0(AFEC_${AFEC_SEQ1R_USCH0}) | AFEC_SEQ1R_USCH1(AFEC_${AFEC_SEQ1R_USCH1}) | AFEC_SEQ1R_USCH2(AFEC_${AFEC_SEQ1R_USCH2})
	| AFEC_SEQ1R_USCH3(AFEC_${AFEC_SEQ1R_USCH3}) | AFEC_SEQ1R_USCH4(AFEC_${AFEC_SEQ1R_USCH4}) | AFEC_SEQ1R_USCH5(AFEC_${AFEC_SEQ1R_USCH5})
	| AFEC_SEQ1R_USCH6(AFEC_${AFEC_SEQ1R_USCH6}) | AFEC_SEQ1R_USCH7(AFEC_${AFEC_SEQ1R_USCH7});
	
	_AFEC${INDEX}_REGS->AFEC_SEQ2R.w = AFEC_SEQ2R_USCH8(AFEC_${AFEC_SEQ2R_USCH8}) | AFEC_SEQ2R_USCH9(AFEC_${AFEC_SEQ2R_USCH9}) 
	| AFEC_SEQ2R_USCH10(AFEC_${AFEC_SEQ2R_USCH10}) | AFEC_SEQ2R_USCH11(AFEC_${AFEC_SEQ2R_USCH11});
	
	/* Enable channel */
	_AFEC${INDEX}_REGS->AFEC_CHER.w = 
	<#if AFEC_SEQ1R_USCH0 != "NONE">
					AFEC_CHER_CH0_Msk
	</#if>
	<#if AFEC_SEQ1R_USCH1 != "NONE">
					| AFEC_CHER_CH1_Msk
	</#if>
	<#if AFEC_SEQ1R_USCH2 != "NONE">
					| AFEC_CHER_CH2_Msk
	</#if>
	<#if AFEC_SEQ1R_USCH3 != "NONE">
					| AFEC_CHER_CH3_Msk
	</#if>
	<#if AFEC_SEQ1R_USCH4 != "NONE">
					| AFEC_CHER_CH4_Msk
	</#if>
	<#if AFEC_SEQ1R_USCH5 != "NONE">
					| AFEC_CHER_CH5_Msk
	</#if>
	<#if AFEC_SEQ1R_USCH6 != "NONE">
					| AFEC_CHER_CH6_Msk
	</#if>
	<#if AFEC_SEQ1R_USCH7 != "NONE">
					| AFEC_CHER_CH7_Msk
	</#if>
	<#if AFEC_SEQ2R_USCH8 != "NONE">
					| AFEC_CHER_CH8_Msk
	</#if>
	<#if AFEC_SEQ2R_USCH9 != "NONE">
					| AFEC_CHER_CH9_Msk
	</#if>
	<#if AFEC_SEQ2R_USCH10 != "NONE">
					| AFEC_CHER_CH10_Msk
	</#if>
	<#if AFEC_SEQ2R_USCH11 != "NONE">
					| AFEC_CHER_CH11_Msk
	</#if>
	<#if (AFEC_SEQ1R_USCH0 == " ") && (AFEC_SEQ1R_USCH1 == " ") && (AFEC_SEQ1R_USCH2 == " ") && (AFEC_SEQ1R_USCH3 == " ") &&
	(AFEC_SEQ1R_USCH4 == " ") && (AFEC_SEQ1R_USCH5 == " ") && (AFEC_SEQ1R_USCH6 == " ") && (AFEC_SEQ1R_USCH7 == " ") &&
	(AFEC_SEQ2R_USCH8 == " ") && (AFEC_SEQ2R_USCH9 == " ") && (AFEC_SEQ2R_USCH10 == " ") && (AFEC_SEQ2R_USCH11 == " ")>
	0
	</#if> 
	;
	</#if>
}

void AFEC${INDEX}_ChannelsEnable (AFEC_CHANNEL_MASK channelsMask)
{
	_AFEC${INDEX}_REGS->AFEC_CHER.w |= channelsMask;
}

void AFEC${INDEX}_ChannelsDisable (AFEC_CHANNEL_MASK channelsMask)
{
	_AFEC${INDEX}_REGS->AFEC_CHDR.w |= channelsMask;
}

void AFEC${INDEX}_ChannelsInterruptEnable (AFEC_INTERRUPT_MASK channelsInterruptMask)
{
	_AFEC${INDEX}_REGS->AFEC_IER.w |= channelsInterruptMask;
}

void AFEC${INDEX}_ChannelsInterruptDisable (AFEC_INTERRUPT_MASK channelsInterruptMask)
{
	_AFEC${INDEX}_REGS->AFEC_IDR.w |= channelsInterruptMask;
}

void AFEC${INDEX}_ConversionStart(void)
{
	_AFEC${INDEX}_REGS->AFEC_CR.w = 0x1U << AFEC_CR_START_Pos;
}

bool AFEC${INDEX}_ChannelResultReady(AFEC_CHANNEL_NUM channel)
{
	return (_AFEC${INDEX}_REGS->AFEC_ISR.w >> channel) & 0x1U;
}

uint16_t AFEC${INDEX}_ChannelResultGet(AFEC_CHANNEL_NUM channel)
{
	_AFEC${INDEX}_REGS->AFEC_CSELR.w = channel;
	return (_AFEC${INDEX}_REGS->AFEC_CDR.w);
}

void AFEC${INDEX}_ConversionSequenceSet(AFEC_CHANNEL_NUM *channelList, uint8_t numChannel)
{
	uint8_t channelIndex;
	_AFEC${INDEX}_REGS->AFEC_SEQ1R.w = 0U;
	_AFEC${INDEX}_REGS->AFEC_SEQ2R.w = 0U;
	
	if (numChannel < AFEC_SEQ1_CHANNEL_NUM)
	{
		for (channelIndex = 0U; channelIndex < numChannel; channelIndex++)
		{
			_AFEC${INDEX}_REGS->AFEC_SEQ1R.w |= channelList[channelIndex] << (channelIndex * 4U);
		}
	}
	else
	{
		for (channelIndex = 0U; channelIndex < AFEC_SEQ1_CHANNEL_NUM; channelIndex++)
		{
			_AFEC${INDEX}_REGS->AFEC_SEQ1R.w |= channelList[channelIndex] << (channelIndex * 4U);
		}
		for (channelIndex = 0U; channelIndex < (numChannel - AFEC_SEQ1_CHANNEL_NUM); channelIndex++)
		{
			_AFEC${INDEX}_REGS->AFEC_SEQ2R.w |= channelList[channelIndex + AFEC_SEQ1_CHANNEL_NUM] << (channelIndex * 4U);
		}
	}
}

void AFEC${INDEX}_ChannelGainSet(AFEC_CHANNEL_NUM channel, AFEC_CHANNEL_GAIN gain)
{
	_AFEC${INDEX}_REGS->AFEC_CGR.w &= ~(0x03U << (2U * channel));
	_AFEC${INDEX}_REGS->AFEC_CGR.w |= (gain << ( 2U * channel));
}

void AFEC${INDEX}_ChannelOffsetSet(AFEC_CHANNEL_NUM channel, uint16_t offset)
{
	_AFEC${INDEX}_REGS->AFEC_CSELR.w = channel;
	_AFEC${INDEX}_REGS->AFEC_COCR.w = offset;
}

void AFEC${INDEX}_CallbackSet(AFEC_CALLBACK callback, uintptr_t context)
{
	AFEC${INDEX}_Callback_param.callback_fn = callback;
	AFEC${INDEX}_Callback_param.context = context;
}




