/*******************************************************************************
  TC Peripheral Library Interface Source File

  Company
    Microchip Technology Inc.

  File Name
    plib_tc${INDEX}.c

  Summary
    TC peripheral library source file.

  Description
    This file implements the interface to the TC peripheral library.  This 
    library provides access to and control of the associated peripheral 
    instance.

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


// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

/*  This section lists the other files that are included in this file.
*/
#include "${__PROCESSOR}.h"
#include "plib_tc${INDEX}.h"
<#assign start = 0> 
<#-- start index of the for loop. In quadrature position mode channel 0 and channel 1 are used. And in quadrature speed mode, all 3 channels are used -->
<#if TC_ENABLE_QEI == true>
	<#compress>
	<#if TC_BMR_POSEN == "POSITION">
		<#assign start = 2>
	<#else>
		<#assign start = 3>
	</#if>
	</#compress>
	
<#if TC_QIER_IDX == true || TC_QIER_QERR == true>
/* Callback object for TC0 */
TC_CALLBACK_OBJECT TC${INDEX}_CallbackObj;
</#if>
/* Initialize channel in timer mode */
void TC${INDEX}_QuadratureInitialize (void)
{
	volatile uint32_t status = _TC${INDEX}_REGS->TC_QISR.w;  /* Clear interrupt status */
	/* clock selection and waveform selection */
	_TC${INDEX}_REGS->TC_CHANNEL[0].TC_CMR.w = TC_CMR_TCCLKS_XC0 | TC_CMR_LDRA_RISING | 
		TC_CMR_ABETRG_Msk | TC_CMR_ETRGEDG_RISING;
		
	_TC${INDEX}_REGS->TC_CHANNEL[1].TC_CMR.w = TC_CMR_TCCLKS_XC0 | TC_CMR_LDRA_RISING;
	
	<#if TC_BMR_POSEN == "SPEED">
	/* Channel 2 configurations */
		<#if TC3_PCK7 == true>
		<#lt>	/* Enable PCK7 */
		<#lt>	_MATRIX_REGS->CCFG_PCCR.w |= CCFG_PCCR_TC0CC_Msk;
		</#if>
		
		<#if TC3_CMR_TCCLKS == "">
		<#lt>	/* Use peripheral clock */
		<#lt>	_TC${INDEX}_REGS->TC_CHANNEL[2].TC_EMR.w = TC_EMR_NODIVCLK_Msk;
		<#lt>	_TC${INDEX}_REGS->TC_CHANNEL[2].TC_CMR.w = TC_CMR_WAVSEL_UP_RC | TC_CMR_WAVE_Msk;
		<#else>
		<#lt>	_TC${INDEX}_REGS->TC_CHANNEL[2].TC_CMR.w = TC_CMR_TCCLKS_${TC3_CMR_TCCLKS} | TC_CMR_WAVSEL_UP_RC | TC_CMR_WAVE_Msk;	
		</#if>
	<#lt>	_TC${INDEX}_REGS->TC_CHANNEL[2].TC_RC.w = ${TC_QEI_PERIOD}U;
	</#if>
	
	/*Enable quadrature mode */
	_TC${INDEX}_REGS->TC_BMR.w = TC_BMR_QDEN_Msk ${TC_BMR_SWAP?then('| (TC_BMR_SWAP_Msk)', '')} | TC_BMR_MAXFILT(${TC_BMR_MAXFILT}U) | TC_BMR_EDGPHA_Msk
		| ${(TC_BMR_POSEN == "POSITION")?then('(TC_BMR_POSEN_Msk)', 'TC_BMR_SPEEDEN_Msk')};
		
	<#if TC_QIER_IDX == true || TC_QIER_QERR == true>

	<#lt>	_TC${INDEX}_REGS->TC_QIER.w = ${TC_QIER_IDX?then('(TC_QIER_IDX_Msk)', '')} <#if TC_QIER_IDX == true && TC_QIER_QERR == true> | </#if><#rt>
										<#lt>${TC_QIER_QERR?then('(TC_QIER_QERR_Msk)', '')};
	</#if>
}

void TC${INDEX}_QuadratureStart (void)
{
	_TC${INDEX}_REGS->TC_CHANNEL[0].TC_CCR.w = (TC_CCR_CLKEN_Msk | TC_CCR_SWTRG_Msk);
	_TC${INDEX}_REGS->TC_CHANNEL[1].TC_CCR.w = (TC_CCR_CLKEN_Msk | TC_CCR_SWTRG_Msk);
	<#if TC_BMR_POSEN == "SPEED">
	<#lt>	_TC${INDEX}_REGS->TC_CHANNEL[2].TC_CCR.w = (TC_CCR_CLKEN_Msk | TC_CCR_SWTRG_Msk);
	</#if>
}

void TC${INDEX}_QuadratureStop (void)
{
	_TC${INDEX}_REGS->TC_CHANNEL[0].TC_CCR.w = (TC_CCR_CLKDIS_Msk);
	_TC${INDEX}_REGS->TC_CHANNEL[1].TC_CCR.w = (TC_CCR_CLKDIS_Msk);
	<#if TC_BMR_POSEN == "SPEED">
	<#lt>	_TC${INDEX}_REGS->TC_CHANNEL[2].TC_CCR.w = (TC_CCR_CLKDIS_Msk);
	</#if>
}

uint32_t TC${INDEX}_QuadraturePositionGet (void)
{
	return (_TC${INDEX}_REGS->TC_CHANNEL[0].TC_CV.w | (_TC${INDEX}_REGS->TC_CHANNEL[1].TC_CV.w << 16U) );
}
<#if TC_BMR_POSEN == "SPEED">
	<#lt>uint32_t TC${INDEX}_QuadratureSpeedGet (void)
	<#lt>{
	<#lt>	return _TC${INDEX}_REGS->TC_CHANNEL[0].TC_CV.w ;
	<#lt>}
</#if>

<#if TC_QIER_IDX == true || TC_QIER_QERR == true>
	<#lt>/* Register callback for quadrature interrupt */
	<#lt>void TC${INDEX}_QuadratureCallbackRegister(TC_CALLBACK callback, uintptr_t context)
	<#lt>{
	<#lt>	TC${INDEX}_CallbackObj.callback_fn = callback;
	<#lt>	TC${INDEX}_CallbackObj.context = context;
	<#lt>}
	
	<#lt>void TC${INDEX}_CH0_InterruptHandler(void)
	<#lt>{
	<#lt>	/* Call registered callback function */
	<#lt>	if (TC${INDEX}_CallbackObj.callback_fn != NULL)
	<#lt>	{
	<#lt>		TC${INDEX}_CallbackObj.callback_fn(TC${INDEX}_CallbackObj.context, 
	<#lt>			_TC${INDEX}_REGS->TC_QISR.w);
	<#lt>	}
	<#lt>}	
</#if>
</#if> <#-- QUADRATURE -->

<#list start..2 as i>
	<#if i == 3>
		<#break>
	</#if> <#-- break the loop if quadrature speed mode is used -->
<#assign TC_CH_ENABLE = "TC" + i + "_ENABLE">
<#assign TC_CH_OPERATINGMODE = "TC" + i +"_OPERATING_MODE">
<#assign CH_NUM = i >
<#assign TC_CMR_TCCLKS = "TC"+ i +"_CMR_TCCLKS">
<#assign TC_PCK7 = "TC"+i+"_PCK7">
<#assign TC_CMR_CPCSTOP = "TC"+ i +"_CMR_CPCSTOP">
<#assign TC_TIMER_PERIOD_COUNT = "TC"+ i +"_TIMER_PERIOD_COUNT">

<#assign TC_CMR_LDRA = "TC"+i+"_CMR_LDRA">
<#assign TC_CMR_LDRB = "TC"+i+"_CMR_LDRB">
<#assign TC_CAPTURE_IER_LDRAS = "TC"+i+"_CAPTURE_IER_LDRAS">
<#assign TC_CAPTURE_IER_LDRBS = "TC"+i+"_CAPTURE_IER_LDRBS">
<#assign TC_CAPTURE_IER_COVFS = "TC"+i+"_CAPTURE_IER_COVFS">
<#assign TC_CMR_ETRGEDG = "TC"+i+"_CMR_ETRGEDG">
<#assign TC_CMR_ABETRG = "TC"+i+"_CMR_ABETRG">
<#assign TC_CAPTURE_EXT_RESET = "TC"+i+"_CAPTURE_EXT_RESET">
<#assign TC_CAPTURE_CMR_LDBSTOP = "TC"+i+"_CAPTURE_CMR_LDBSTOP">

<#assign TC_CMR_ACPA = "TC"+i+"_CMR_ACPA">
<#assign TC_CMR_ACPC = "TC"+i+"_CMR_ACPC">
<#assign TC_CMR_AEEVT = "TC"+i+"_CMR_AEEVT">
<#assign TC_CMR_BCPB = "TC"+i+"_CMR_BCPB">
<#assign TC_CMR_BCPC = "TC"+i+"_CMR_BCPC">
<#assign TC_CMR_BEEVT = "TC"+i+"_CMR_BEEVT">
<#assign TC_CMR_WAVSEL = "TC"+i+"_CMR_WAVSEL">
<#assign TC_CMR_ENETRG = "TC"+i+"_CMR_ENETRG">
<#assign TC_CMR_EEVT = "TC"+i+"_CMR_EEVT">
<#assign TC_CMP_CMR_ETRGEDG = "TC"+i+"_CMP_CMR_ETRGEDG">
<#assign TC_COMPARE_PERIOD_COUNT = "TC"+i+"_COMPARE_PERIOD_COUNT">
<#assign TC_COMPARE_A = "TC"+i+"_COMPARE_A">
<#assign TC_COMPARE_B = "TC"+i+"_COMPARE_B">
<#assign TC_COMPARE_IER_CPCS = "TC"+i+"_COMPARE_IER_CPCS">
<#assign TC_COMPARE_CMR_CPCSTOP = "TC"+i+"_COMPARE_CMR_CPCSTOP">

<#if .vars[TC_CH_ENABLE] == true>
<#if .vars[TC_CH_OPERATINGMODE] == "TIMER">
/* Callback object for ${CH_NUM} */
TC_CALLBACK_OBJECT TC${INDEX}_CH${CH_NUM}_CallbackObj;

/* Initialize channel in timer mode */
void TC${INDEX}_CH${CH_NUM}_TimerInitialize (void)
{
	<#if .vars[TC_PCK7] == true>
	<#lt>	/* Enable PCK7 */
	<#lt>	_MATRIX_REGS->CCFG_PCCR.w |= CCFG_PCCR_TC0CC_Msk;
	
	</#if>
	<#if .vars[TC_CMR_TCCLKS] == "">
	/* Use peripheral clock */
	<#lt>	_TC${INDEX}_REGS->TC_CHANNEL[${CH_NUM}].TC_EMR.w = TC_EMR_NODIVCLK_Msk;
	<#lt>	/* clock selection and waveform selection */
	<#lt>	_TC${INDEX}_REGS->TC_CHANNEL[${CH_NUM}].TC_CMR.w =  TC_CMR_WAVSEL_UP_RC | TC_CMR_WAVE_Msk ${.vars[TC_CMR_CPCSTOP]?then('| (TC_CMR_CPCDIS_Msk)', '')};
	<#else>
	/* clock selection and waveform selection */
	<#lt>	_TC${INDEX}_REGS->TC_CHANNEL[${CH_NUM}].TC_CMR.w = TC_CMR_TCCLKS_${.vars[TC_CMR_TCCLKS]} | TC_CMR_WAVSEL_UP_RC | \
														TC_CMR_WAVE_Msk ${.vars[TC_CMR_CPCSTOP]?then('|(TC_CMR_CPCDIS_Msk)', '')};
	</#if>
	
	/* write period */
	_TC${INDEX}_REGS->TC_CHANNEL[${CH_NUM}].TC_RC.w = ${.vars[TC_TIMER_PERIOD_COUNT]}U;

	/* enable interrupt */
	_TC${INDEX}_REGS->TC_CHANNEL[${CH_NUM}].TC_IER.w = TC_IER_CPCS_Msk;
}

/* Start the timer */
void TC${INDEX}_CH${CH_NUM}_TimerStart (void)
{
	_TC${INDEX}_REGS->TC_CHANNEL[${CH_NUM}].TC_CCR.w = (TC_CCR_CLKEN_Msk | TC_CCR_SWTRG_Msk);
}

/* Stop the timer */
void TC${INDEX}_CH${CH_NUM}_TimerStop (void)
{
	_TC${INDEX}_REGS->TC_CHANNEL[${CH_NUM}].TC_CCR.w = (TC_CCR_CLKDIS_Msk);
}

/* Configure timer period */
void TC${INDEX}_CH${CH_NUM}_TimerPeriodSet (uint32_t period)
{
	_TC${INDEX}_REGS->TC_CHANNEL[${CH_NUM}].TC_RC.w = period;
}

/* Read timer period */
uint32_t TC${INDEX}_CH${CH_NUM}_TimerPeriodGet (void)
{
	return _TC${INDEX}_REGS->TC_CHANNEL[${CH_NUM}].TC_RC.w;
}

/* Read timer counter value */
uint32_t TC${INDEX}_CH${CH_NUM}_TimerCounterGet (void)
{
	return _TC${INDEX}_REGS->TC_CHANNEL[${CH_NUM}].TC_CV.w;
}

/* Register callback for period interrupt */
void TC${INDEX}_CH${CH_NUM}_TimerCallbackRegister(TC_CALLBACK callback, uintptr_t context)
{
	TC${INDEX}_CH${CH_NUM}_CallbackObj.callback_fn = callback;
	TC${INDEX}_CH${CH_NUM}_CallbackObj.context = context;
}

void TC${INDEX}_CH${CH_NUM}_InterruptHandler(void)
{
	/* Call registered callback function */
	if (TC${INDEX}_CH${CH_NUM}_CallbackObj.callback_fn != NULL)
	{
		TC${INDEX}_CH${CH_NUM}_CallbackObj.callback_fn(TC${INDEX}_CH${CH_NUM}_CallbackObj.context, 
			_TC${INDEX}_REGS->TC_CHANNEL[${CH_NUM}].TC_SR.w);
	}
}
</#if> <#-- TIMER -->

<#if .vars[TC_CH_OPERATINGMODE] == "CAPTURE">
<#if .vars[TC_CAPTURE_IER_LDRAS] == true || .vars[TC_CAPTURE_IER_LDRBS] == true || .vars[TC_CAPTURE_IER_COVFS] == true>
/* Callback object for ${CH_NUM} */
TC_CALLBACK_OBJECT TC${INDEX}_CH${CH_NUM}_CallbackObj;
</#if>

/* Initialize channel in capture mode */
void TC${INDEX}_CH${CH_NUM}_CaptureInitialize (void)
{
	<#if .vars[TC_PCK7] == true>
	<#lt>	/* Enable PCK7 */
	<#lt>	_MATRIX_REGS->CCFG_PCCR.w |= CCFG_PCCR_TC0CC_Msk;
	
	</#if>
	<#if .vars[TC_CMR_TCCLKS] == "">
	/* Use peripheral clock */
	_TC${INDEX}_REGS->TC_CHANNEL[${CH_NUM}].TC_EMR.w = TC_EMR_NODIVCLK_Msk;
		/* clock selection and capture configurations */
	_TC${INDEX}_REGS->TC_CHANNEL[${CH_NUM}].TC_CMR.w = TC_CMR_LDRA_${.vars[TC_CMR_LDRA]} | TC_CMR_LDRB_${.vars[TC_CMR_LDRB]}<#rt>
		<#lt>${.vars[TC_CAPTURE_CMR_LDBSTOP]?then('| (TC_CMR_LDBSTOP_Msk)', '')};

	<#else>
	/* clock selection and capture configurations */
	_TC${INDEX}_REGS->TC_CHANNEL[${CH_NUM}].TC_CMR.w = TC_CMR_TCCLKS_${.vars[TC_CMR_TCCLKS]} | TC_CMR_LDRA_${.vars[TC_CMR_LDRA]} \
		| TC_CMR_LDRB_${.vars[TC_CMR_LDRB]} <#rt>
		<#lt>${.vars[TC_CAPTURE_CMR_LDBSTOP]?then('| (TC_CMR_LDBSTOP_Msk)', '')};
	</#if>
	<#if .vars[TC_CMR_TCCLKS] == "PCK7">
	<#lt>	/* Enable PCK7 */
	<#lt>	_MATRIX_REGS->CCFG_PCCR |= CCFG_PCCR_TC0CC_Msk;
	</#if>
	<#if .vars[TC_CAPTURE_EXT_RESET] == true>
	/* external reset event configurations */
	_TC${INDEX}_REGS->TC_CHANNEL[${CH_NUM}].TC_CMR.w |= <#if .vars[TC_CMR_ABETRG] == "TIOA"> TC_CMR_ABETRG_Msk | </#if> TC_CMR_ETRGEDG_${.vars[TC_CMR_ETRGEDG]};
	</#if>
	
	<#if .vars[TC_CAPTURE_IER_LDRAS] == true || .vars[TC_CAPTURE_IER_LDRBS] == true || .vars[TC_CAPTURE_IER_COVFS] == true>
	/* enable interrupt */
	_TC${INDEX}_REGS->TC_CHANNEL[${CH_NUM}].TC_IER.w = <#if .vars[TC_CAPTURE_IER_LDRAS]>TC_IER_LDRAS_Msk </#if><#if .vars[TC_CAPTURE_IER_LDRBS]>| TC_IER_LDRBS_Msk </#if><#if .vars[TC_CAPTURE_IER_COVFS]>| TC_IER_COVFS_Msk </#if>;
	</#if>
}

/* Start the capture mode */
void TC${INDEX}_CH${CH_NUM}_CaptureStart (void)
{
	_TC${INDEX}_REGS->TC_CHANNEL[${CH_NUM}].TC_CCR.w = (TC_CCR_CLKEN_Msk | TC_CCR_SWTRG_Msk);
}

/* Stop the capture mode */
void TC${INDEX}_CH${CH_NUM}_CaptureStop (void)
{
	_TC${INDEX}_REGS->TC_CHANNEL[${CH_NUM}].TC_CCR.w = (TC_CCR_CLKDIS_Msk);
}

/* Register callback function */
<#if .vars[TC_CAPTURE_IER_LDRAS] == true || .vars[TC_CAPTURE_IER_LDRBS] == true || .vars[TC_CAPTURE_IER_COVFS] == true>
void TC${INDEX}_CH${CH_NUM}_CaptureCallbackRegister(TC_CALLBACK callback, uintptr_t context)
{
	TC${INDEX}_CH${CH_NUM}_CallbackObj.callback_fn = callback;
	TC${INDEX}_CH${CH_NUM}_CallbackObj.context = context;
}

void TC${INDEX}_CH${CH_NUM}_InterruptHandler(void)
{
	/* Call registered callback function */
	if (TC${INDEX}_CH${CH_NUM}_CallbackObj.callback_fn != NULL)
	{
		TC${INDEX}_CH${CH_NUM}_CallbackObj.callback_fn(TC${INDEX}_CH${CH_NUM}_CallbackObj.context,
			_TC${INDEX}_REGS->TC_CHANNEL[${CH_NUM}].TC_SR.w);
	}
}
</#if>

/* Read last captured value of Capture A */
uint16_t TC${INDEX}_CH${CH_NUM}_CaptureAGet (void)
{
	return _TC${INDEX}_REGS->TC_CHANNEL[${CH_NUM}].TC_RA.w;
}

/* Read last captured value of Capture B */
uint16_t TC${INDEX}_CH${CH_NUM}_CaptureBGet (void)
{
	return _TC${INDEX}_REGS->TC_CHANNEL[${CH_NUM}].TC_RB.w;
}

/* Check whether new value is captured in Capture A */
bool TC${INDEX}_CH${CH_NUM}_CaptureAEventOccured (void)
{
	return ((_TC${INDEX}_REGS->TC_CHANNEL[${CH_NUM}].TC_SR.w >> TC_IER_LDRAS_Pos) & 0x1U);
}

/* Check whether new value is captured in Capture B */
bool TC${INDEX}_CH${CH_NUM}_CaptureBEventOccured (void)
{
	return ((_TC${INDEX}_REGS->TC_CHANNEL[${CH_NUM}].TC_SR.w >> TC_IER_LDRBS_Pos) & 0x1U);
}
</#if> <#-- CAPTURE -->

<#if .vars[TC_CH_OPERATINGMODE] == "COMPARE">
<#if .vars[TC_COMPARE_IER_CPCS] == true>
/* Callback object for ${CH_NUM} */
TC_CALLBACK_OBJECT TC${INDEX}_CH${CH_NUM}_CallbackObj;
</#if>

/* Initialize channel in compare mode */
void TC${INDEX}_CH${CH_NUM}_CompareInitialize (void)
{
	<#if .vars[TC_PCK7] == true>
	<#lt>	/* Enable PCK7 */
	<#lt>	_MATRIX_REGS->CCFG_PCCR.w |= CCFG_PCCR_TC0CC_Msk;
	
	</#if>
	<#if .vars[TC_CMR_TCCLKS] == "">
	/* Use peripheral clock */
	_TC${INDEX}_REGS->TC_CHANNEL[${CH_NUM}].TC_EMR.w = TC_EMR_NODIVCLK_Msk;
	/* clock selection and waveform selection */
	_TC${INDEX}_REGS->TC_CHANNEL[${CH_NUM}].TC_CMR.w =  TC_CMR_WAVSEL_${.vars[TC_CMR_WAVSEL]} | TC_CMR_WAVE_Msk | \
				TC_CMR_ACPA_${.vars[TC_CMR_ACPA]} | TC_CMR_ACPC_${.vars[TC_CMR_ACPC]} | TC_CMR_AEEVT_${.vars[TC_CMR_AEEVT]} | \
				TC_CMR_BCPB_${.vars[TC_CMR_BCPB]} | TC_CMR_BCPC_${.vars[TC_CMR_BCPC]} | TC_CMR_BEEVT_${.vars[TC_CMR_BEEVT]} <#rt>
				<#lt>${.vars[TC_COMPARE_CMR_CPCSTOP]?then('| (TC_CMR_CPCSTOP_Msk)', '')};	
	<#else>
	/* clock selection and waveform selection */
	_TC${INDEX}_REGS->TC_CHANNEL[${CH_NUM}].TC_CMR.w = TC_CMR_TCCLKS_${.vars[TC_CMR_TCCLKS]} | TC_CMR_WAVSEL_${.vars[TC_CMR_WAVSEL]} | TC_CMR_WAVE_Msk | \
				TC_CMR_ACPA_${.vars[TC_CMR_ACPA]} | TC_CMR_ACPC_${.vars[TC_CMR_ACPC]} | TC_CMR_AEEVT_${.vars[TC_CMR_AEEVT]} | \
				TC_CMR_BCPB_${.vars[TC_CMR_BCPB]} | TC_CMR_BCPC_${.vars[TC_CMR_BCPC]} | TC_CMR_BEEVT_${.vars[TC_CMR_BEEVT]} <#rt>
				<#lt>${.vars[TC_COMPARE_CMR_CPCSTOP]?then('| (TC_CMR_CPCSTOP_Msk)', '')};
	</#if>
	
	<#if .vars[TC_CMR_TCCLKS] == "PCK7">
	<#lt>	/* Enable PCK7 */
	<#lt>	_MATRIX_REGS->CCFG_PCCR |= CCFG_PCCR_TC0CC_Msk;
	</#if>
	
	/* external reset event configurations */
	_TC${INDEX}_REGS->TC_CHANNEL[${CH_NUM}].TC_CMR.w |= TC_CMR_ENETRG_Msk | TC_CMR_EEVT_${.vars[TC_CMR_EEVT]} | \
				TC_CMR_EEVTEDG_${.vars[TC_CMP_CMR_ETRGEDG]};
	
	/* write period */
	_TC${INDEX}_REGS->TC_CHANNEL[${CH_NUM}].TC_RC.w = ${.vars[TC_COMPARE_PERIOD_COUNT]}U;
	
	/* write compare values */
	_TC${INDEX}_REGS->TC_CHANNEL[${CH_NUM}].TC_RA.w = ${.vars[TC_COMPARE_A]}U;
	_TC${INDEX}_REGS->TC_CHANNEL[${CH_NUM}].TC_RB.w = ${.vars[TC_COMPARE_B]}U;
	
	<#if .vars[TC_COMPARE_IER_CPCS] == true>
	/* enable interrupt */
	_TC${INDEX}_REGS->TC_CHANNEL[${CH_NUM}].TC_IER.w = TC_IER_CPCS_Msk;
	</#if>
}

/* Start the compare mode */
void TC${INDEX}_CH${CH_NUM}_CompareStart (void)
{
	_TC${INDEX}_REGS->TC_CHANNEL[${CH_NUM}].TC_CCR.w = (TC_CCR_CLKEN_Msk | TC_CCR_SWTRG_Msk);
}

/* Stop the compare mode */
void TC${INDEX}_CH${CH_NUM}_CompareStop (void)
{
	_TC${INDEX}_REGS->TC_CHANNEL[${CH_NUM}].TC_CCR.w = (TC_CCR_CLKDIS_Msk);
}

/* Configure the period value */
void TC${INDEX}_CH${CH_NUM}_ComparePeriodSet (uint32_t period)
{
	_TC${INDEX}_REGS->TC_CHANNEL[${CH_NUM}].TC_RC.w = period;
}

/* Read the period value */
uint32_t TC${INDEX}_CH${CH_NUM}_ComparePeriodGet (void)
{
	return _TC${INDEX}_REGS->TC_CHANNEL[${CH_NUM}].TC_RC.w;
}

/* Read timer counter value */
uint32_t TC${INDEX}_CH${CH_NUM}_CompareCounterGet (void)
{
	return _TC${INDEX}_REGS->TC_CHANNEL[${CH_NUM}].TC_CV.w;
}
<#if .vars[TC_COMPARE_IER_CPCS] == true>
/* Register callback function */
void TC${INDEX}_CH${CH_NUM}_CompareCallbackRegister(TC_CALLBACK callback, uintptr_t context)
{
	TC${INDEX}_CH${CH_NUM}_CallbackObj.callback_fn = callback;
	TC${INDEX}_CH${CH_NUM}_CallbackObj.context = context;
}

/* Interrupt Handler */
void TC${INDEX}_CH${CH_NUM}_InterruptHandler(void)
{
	/* Call registered callback function */
	if (TC${INDEX}_CH${CH_NUM}_CallbackObj.callback_fn != NULL)
	{
		TC${INDEX}_CH${CH_NUM}_CallbackObj.callback_fn(TC${INDEX}_CH${CH_NUM}_CallbackObj.context, 
			_TC${INDEX}_REGS->TC_CHANNEL[${CH_NUM}].TC_SR.w);
	}
}
</#if>

/* Set the compare A value */
void TC${INDEX}_CH${CH_NUM}_CompareASet (uint16_t value)
{
	_TC${INDEX}_REGS->TC_CHANNEL[${CH_NUM}].TC_RA.w = value;
}

/* Set the compare B value */
void TC${INDEX}_CH${CH_NUM}_CompareBSet (uint16_t value)
{
	_TC${INDEX}_REGS->TC_CHANNEL[${CH_NUM}].TC_RB.w = value;
}
</#if> <#-- COMPARE -->

</#if> <#-- CH_ENABLE -->
</#list>

/**
 End of File
*/
