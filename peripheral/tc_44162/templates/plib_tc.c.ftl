/*******************************************************************************
  TC Peripheral Library Interface Source File

  Company
    Microchip Technology Inc.

  File Name
    plib_${TC_INSTANCE_NAME?lower_case}.c

  Summary
    TC peripheral library source file.

  Description
    This file implements the interface to the TC peripheral library.  This
    library provides access to and control of the associated peripheral
    instance.

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

/*  This section lists the other files that are included in this file.
*/
#include "device.h"
#include "plib_${TC_INSTANCE_NAME?lower_case}.h"
<#compress>
<#assign TC_UNSIGNED_INT_TYPE = "uint16_t">
<#assign TC_SIGNED_INT_TYPE = "int16_t">
<#if TIMER_WIDTH == 32>
<#assign TC_UNSIGNED_INT_TYPE = "uint32_t">
<#assign TC_SIGNED_INT_TYPE = "int32_t">
</#if>
</#compress>
<#assign start = 0>
<#-- start index of the for loop. In quadrature position mode channel 0 and channel 1 are used. And in quadrature speed mode, all 3 channels are used -->
<#if TC_ENABLE_QEI == true>
    <#compress>
    <#if TC_BMR_POSEN == "POSITION">
        <#if TC_INDEX_PULSE == true>
            <#assign start = 2>
        <#else>
            <#assign start = 1>
        </#if>
    <#else>
        <#if TC_INDEX_PULSE == true>
            <#assign start = 3>
        <#else>
            <#assign start = 1>
        </#if>
    </#if>
    </#compress>
<#if TC_QIER_IDX == true || TC_QIER_QERR == true || TC_QEI_IER_CPCS == true>
/* Callback object for channel 0 */
TC_QUADRATURE_CALLBACK_OBJECT ${TC_INSTANCE_NAME}_CallbackObj;
</#if>

/* Initialize channel in quadrature mode */
void ${TC_INSTANCE_NAME}_QuadratureInitialize (void)
{
    uint32_t status;

    <#if TC_INDEX_PULSE == true>
        <#lt>    /* clock selection and waveform selection */
        <#lt>    ${TC_INSTANCE_NAME}_REGS->TC_CHANNEL[0].TC_CMR = TC_CMR_TCCLKS_XC0 | TC_CMR_CAPTURE_LDRA_RISING |
            TC_CMR_CAPTURE_ABETRG_Msk | TC_CMR_CAPTURE_ETRGEDG_RISING;

        <#lt>    ${TC_INSTANCE_NAME}_REGS->TC_CHANNEL[1].TC_CMR = TC_CMR_TCCLKS_XC0 | TC_CMR_CAPTURE_LDRA_RISING;

    <#else>
        <#lt>    /* clock selection and waveform selection */
        <#lt>    ${TC_INSTANCE_NAME}_REGS->TC_CHANNEL[0].TC_CMR = TC_CMR_TCCLKS_XC0 | TC_CMR_CAPTURE_LDRA_RISING | TC_CMR_CAPTURE_CPCTRG_Msk;
        <#lt>    ${TC_INSTANCE_NAME}_REGS->TC_CHANNEL[0].TC_RC = ${TC_QEI_NUM_PULSES}U;
        <#if TC_QEI_IER_CPCS == true>
            <#lt>    ${TC_INSTANCE_NAME}_REGS->TC_CHANNEL[0].TC_IER = TC_IER_CPCS_Msk;
        </#if>
    </#if>

    <#if TC_BMR_POSEN == "SPEED">
    /* Channel 2 configurations */
        <#if TC_MATRIX_PRESENT == true>
            <#if TC3_PCK7 == true>
            <#lt>    /* Enable PCK7 */
            <#lt>    MATRIX_REGS->CCFG_PCCR |= CCFG_PCCR_TC0CC_Msk;
            </#if>
        </#if>

        <#if TC3_CMR_TCCLKS == "">
        <#lt>    /* Use peripheral clock */
        <#lt>    ${TC_INSTANCE_NAME}_REGS->TC_CHANNEL[2].TC_EMR = TC_EMR_NODIVCLK_Msk;
        <#lt>    ${TC_INSTANCE_NAME}_REGS->TC_CHANNEL[2].TC_CMR = TC_CMR_WAVEFORM_WAVSEL_UP_RC | TC_CMR_WAVE_Msk;
        <#else>
        <#lt>    ${TC_INSTANCE_NAME}_REGS->TC_CHANNEL[2].TC_CMR = TC_CMR_TCCLKS_${TC3_CMR_TCCLKS} | TC_CMR_WAVEFORM_WAVSEL_UP_RC | TC_CMR_WAVE_Msk;
        </#if>
    <#lt>    ${TC_INSTANCE_NAME}_REGS->TC_CHANNEL[2].TC_RC = ${TC_QEI_PERIOD}U;
    </#if>

    /*Enable quadrature mode */
    ${TC_INSTANCE_NAME}_REGS->TC_BMR = TC_BMR_QDEN_Msk ${TC_BMR_SWAP?then('| (TC_BMR_SWAP_Msk)', '')} | TC_BMR_MAXFILT(${TC_BMR_MAXFILT}U) | TC_BMR_EDGPHA_Msk
        | ${(TC_BMR_POSEN == "POSITION")?then('(TC_BMR_POSEN_Msk)', 'TC_BMR_SPEEDEN_Msk')};

    <#if TC_QIER_IDX == true || TC_QIER_QERR == true>

    <#lt>    ${TC_INSTANCE_NAME}_REGS->TC_QIER = ${TC_QIER_IDX?then('(TC_QIER_IDX_Msk)', '')} <#if TC_QIER_IDX == true && TC_QIER_QERR == true> | </#if><#rt>
                                        <#lt>${TC_QIER_QERR?then('(TC_QIER_QERR_Msk)', '')};
    </#if>
    <#if TC_QIER_IDX == true || TC_QIER_QERR == true || TC_QEI_IER_CPCS == true>
    <#lt>    ${TC_INSTANCE_NAME}_CallbackObj.callback_fn = NULL;
    </#if>
    status = ${TC_INSTANCE_NAME}_REGS->TC_QISR;  /* Clear interrupt status */

    /* Ignore warning */
    (void)status;
}

void ${TC_INSTANCE_NAME}_QuadratureStart (void)
{
    ${TC_INSTANCE_NAME}_REGS->TC_CHANNEL[0].TC_CCR = (TC_CCR_CLKEN_Msk | TC_CCR_SWTRG_Msk);
    <#if TC_INDEX_PULSE == true>
        <#lt>    ${TC_INSTANCE_NAME}_REGS->TC_CHANNEL[1].TC_CCR = (TC_CCR_CLKEN_Msk | TC_CCR_SWTRG_Msk);
    </#if>
    <#if TC_BMR_POSEN == "SPEED">
        <#lt>    ${TC_INSTANCE_NAME}_REGS->TC_CHANNEL[2].TC_CCR = (TC_CCR_CLKEN_Msk | TC_CCR_SWTRG_Msk);
    </#if>
}

void ${TC_INSTANCE_NAME}_QuadratureStop (void)
{
    ${TC_INSTANCE_NAME}_REGS->TC_CHANNEL[0].TC_CCR = (TC_CCR_CLKDIS_Msk);
    <#if TC_INDEX_PULSE == true>
        <#lt>    ${TC_INSTANCE_NAME}_REGS->TC_CHANNEL[1].TC_CCR = (TC_CCR_CLKDIS_Msk);
    </#if>
    <#if TC_BMR_POSEN == "SPEED">
    <#lt>    ${TC_INSTANCE_NAME}_REGS->TC_CHANNEL[2].TC_CCR = (TC_CCR_CLKDIS_Msk);
    </#if>
}

<#if TC_QIER_IDX == true || TC_QIER_QERR == true || TC_QEI_IER_CPCS == true>
    <#lt>/* Register callback for quadrature interrupt */
    <#lt>void ${TC_INSTANCE_NAME}_QuadratureCallbackRegister(TC_QUADRATURE_CALLBACK callback, uintptr_t context)
    <#lt>{
    <#lt>    ${TC_INSTANCE_NAME}_CallbackObj.callback_fn = callback;
    <#lt>    ${TC_INSTANCE_NAME}_CallbackObj.context = context;
    <#lt>}

    <#lt>void ${TC_INSTANCE_NAME}_CH0_InterruptHandler(void)
    <#lt>{
    <#lt>    TC_QUADRATURE_STATUS quadrature_status = (TC_QUADRATURE_STATUS)(${TC_INSTANCE_NAME}_REGS->TC_QISR & TC_QUADRATURE_STATUS_MSK);
    <#lt>    /* Call registered callback function */
    <#lt>    if (${TC_INSTANCE_NAME}_CallbackObj.callback_fn != NULL)
    <#lt>    {
    <#lt>        ${TC_INSTANCE_NAME}_CallbackObj.callback_fn(quadrature_status, ${TC_INSTANCE_NAME}_CallbackObj.context);
    <#lt>    }
    <#lt>}

<#else>
TC_QUADRATURE_STATUS ${TC_INSTANCE_NAME}_QuadratureStatusGet(void)
{
    return (TC_QUADRATURE_STATUS)(${TC_INSTANCE_NAME}_REGS->TC_QISR & TC_QUADRATURE_STATUS_MSK);
}
</#if>
</#if> <#-- QUADRATURE -->

<#list start..(TC_MAX_CHANNELS - 1) as i>
    <#if i == TC_MAX_CHANNELS>
        <#break>
    </#if> <#-- break the loop if quadrature speed mode is used -->
    <#if TC_ENABLE_QEI == true && TC_INDEX_PULSE == false && TC_BMR_POSEN == "SPEED" && i == 2>
        <#break>
    </#if>
<#assign TC_CH_ENABLE = "TC" + i + "_ENABLE">
<#assign TC_CH_OPERATINGMODE = "TC" + i +"_OPERATING_MODE">
<#assign CH_NUM = i >
<#assign TC_TIMER_SYS_TIME_CONNECTED = "TC"+i+"_SYS_TIME_CONNECTED">
<#assign TC_CMR_TCCLKS = "TC"+ i +"_CMR_TCCLKS">
<#assign TC_PCK7 = "TC"+i+"_PCK7">
<#assign TC_CMR_CPCSTOP = "TC"+ i +"_CMR_CPCSTOP">
<#assign TC_TIMER_PERIOD_COUNT = "TC"+ i +"_TIMER_PERIOD_COUNT">
<#assign TC_TIMER_IER_CPCS = "TC"+i+"_IER_CPCS">
<#assign TC_TIMER_IER_CPAS = "TC"+i+"_IER_CPAS">
<#assign TC_CH_CLOCK_FREQ = "TC"+i+"_CLOCK_FREQ">

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

<#if (.vars[TC_TIMER_IER_CPCS] == true) || (.vars[TC_TIMER_IER_CPAS] == true)>
/* Callback object for channel ${CH_NUM} */
TC_TIMER_CALLBACK_OBJECT ${TC_INSTANCE_NAME}_CH${CH_NUM}_CallbackObj;
</#if>

/* Initialize channel in timer mode */
void ${TC_INSTANCE_NAME}_CH${CH_NUM}_TimerInitialize (void)
{
    <#if TC_MATRIX_PRESENT == true>
        <#if .vars[TC_PCK7] == true>
        <#lt>    /* Enable PCK7 */
        <#lt>    MATRIX_REGS->CCFG_PCCR |= CCFG_PCCR_TC0CC_Msk;

        </#if>
    </#if>
    <#if .vars[TC_CMR_TCCLKS] == "">
    /* Use peripheral clock */
    <#lt>    ${TC_INSTANCE_NAME}_REGS->TC_CHANNEL[${CH_NUM}].TC_EMR = TC_EMR_NODIVCLK_Msk;
    <#lt>    /* clock selection and waveform selection */
    <#lt>    ${TC_INSTANCE_NAME}_REGS->TC_CHANNEL[${CH_NUM}].TC_CMR =  TC_CMR_WAVEFORM_WAVSEL_UP_RC | TC_CMR_WAVE_Msk ${.vars[TC_CMR_CPCSTOP]?then('| (TC_CMR_WAVEFORM_CPCDIS_Msk)', '')};
    <#else>
    /* clock selection and waveform selection */
    <#lt>    ${TC_INSTANCE_NAME}_REGS->TC_CHANNEL[${CH_NUM}].TC_CMR = TC_CMR_TCCLKS_${.vars[TC_CMR_TCCLKS]} | TC_CMR_WAVEFORM_WAVSEL_UP_RC | \
                                                        TC_CMR_WAVE_Msk ${.vars[TC_CMR_CPCSTOP]?then('|(TC_CMR_WAVEFORM_CPCDIS_Msk)', '')};
    </#if>

    /* write period */
    ${TC_INSTANCE_NAME}_REGS->TC_CHANNEL[${CH_NUM}].TC_RC = ${.vars[TC_TIMER_PERIOD_COUNT]}U;

    <#compress>
    <#assign TIMER_INTERRUPT = "">
    <#if .vars[TC_TIMER_IER_CPAS] == true >
        <#assign TIMER_INTERRUPT = "TC_IER_CPAS_Msk">
    </#if>
    <#if .vars[TC_TIMER_IER_CPCS] == true>
        <#if TIMER_INTERRUPT != "">
            <#assign TIMER_INTERRUPT = TIMER_INTERRUPT + " | TC_IER_CPCS_Msk">
        <#else>
            <#assign TIMER_INTERRUPT = "TC_IER_CPCS_Msk">
        </#if>
    </#if>
    </#compress>

    <#if (.vars[TC_TIMER_IER_CPCS] == true) || (.vars[TC_TIMER_IER_CPAS] == true)>
    /* enable interrupt */
    <#lt>    ${TC_INSTANCE_NAME}_REGS->TC_CHANNEL[${CH_NUM}].TC_IER = ${TIMER_INTERRUPT};
    <#lt>    ${TC_INSTANCE_NAME}_CH${CH_NUM}_CallbackObj.callback_fn = NULL;
    </#if>
}

/* Start the timer */
void ${TC_INSTANCE_NAME}_CH${CH_NUM}_TimerStart (void)
{
    ${TC_INSTANCE_NAME}_REGS->TC_CHANNEL[${CH_NUM}].TC_CCR = (TC_CCR_CLKEN_Msk | TC_CCR_SWTRG_Msk);
}

/* Stop the timer */
void ${TC_INSTANCE_NAME}_CH${CH_NUM}_TimerStop (void)
{
    ${TC_INSTANCE_NAME}_REGS->TC_CHANNEL[${CH_NUM}].TC_CCR = (TC_CCR_CLKDIS_Msk);
}

uint32_t ${TC_INSTANCE_NAME}_CH${CH_NUM}_TimerFrequencyGet( void )
{
    return (uint32_t)(${.vars[TC_CH_CLOCK_FREQ]}UL);
}

/* Configure timer period */
void ${TC_INSTANCE_NAME}_CH${CH_NUM}_TimerPeriodSet (${TC_UNSIGNED_INT_TYPE} period)
{
    ${TC_INSTANCE_NAME}_REGS->TC_CHANNEL[${CH_NUM}].TC_RC = period;
}

<#if .vars[TC_TIMER_SYS_TIME_CONNECTED] == true>
/* Configure timer compare */
void ${TC_INSTANCE_NAME}_CH${CH_NUM}_TimerCompareSet (${TC_UNSIGNED_INT_TYPE} compare)
{
    ${TC_INSTANCE_NAME}_REGS->TC_CHANNEL[${CH_NUM}].TC_RA = compare;
}
</#if>

/* Read timer period */
${TC_UNSIGNED_INT_TYPE} ${TC_INSTANCE_NAME}_CH${CH_NUM}_TimerPeriodGet (void)
{
    return ${TC_INSTANCE_NAME}_REGS->TC_CHANNEL[${CH_NUM}].TC_RC;
}

/* Read timer counter value */
${TC_UNSIGNED_INT_TYPE} ${TC_INSTANCE_NAME}_CH${CH_NUM}_TimerCounterGet (void)
{
    return ${TC_INSTANCE_NAME}_REGS->TC_CHANNEL[${CH_NUM}].TC_CV;
}

<#if (.vars[TC_TIMER_IER_CPCS] == true) || (.vars[TC_TIMER_IER_CPAS] == true)>
/* Register callback for period interrupt */
void ${TC_INSTANCE_NAME}_CH${CH_NUM}_TimerCallbackRegister(TC_TIMER_CALLBACK callback, uintptr_t context)
{
    ${TC_INSTANCE_NAME}_CH${CH_NUM}_CallbackObj.callback_fn = callback;
    ${TC_INSTANCE_NAME}_CH${CH_NUM}_CallbackObj.context = context;
}

void ${TC_INSTANCE_NAME}_CH${CH_NUM}_InterruptHandler(void)
{
    TC_TIMER_STATUS timer_status = (TC_TIMER_STATUS)(${TC_INSTANCE_NAME}_REGS->TC_CHANNEL[${CH_NUM}].TC_SR & TC_TIMER_STATUS_MSK);
    /* Call registered callback function */
    if ((TC_TIMER_NONE != timer_status) && ${TC_INSTANCE_NAME}_CH${CH_NUM}_CallbackObj.callback_fn != NULL)
    {
        ${TC_INSTANCE_NAME}_CH${CH_NUM}_CallbackObj.callback_fn(timer_status, ${TC_INSTANCE_NAME}_CH${CH_NUM}_CallbackObj.context);
    }
}

<#else>
/* Check if timer period status is set */
bool ${TC_INSTANCE_NAME}_CH${CH_NUM}_TimerPeriodHasExpired(void)
{
    return (((${TC_INSTANCE_NAME}_REGS->TC_CHANNEL[${CH_NUM}].TC_SR) & TC_SR_CPCS_Msk) >> TC_SR_CPCS_Pos);
}
</#if>
</#if> <#-- TIMER -->

<#if .vars[TC_CH_OPERATINGMODE] == "CAPTURE">
<#if .vars[TC_CAPTURE_IER_LDRAS] == true || .vars[TC_CAPTURE_IER_LDRBS] == true || .vars[TC_CAPTURE_IER_COVFS] == true>
/* Callback object for channel ${CH_NUM} */
TC_CAPTURE_CALLBACK_OBJECT ${TC_INSTANCE_NAME}_CH${CH_NUM}_CallbackObj;
</#if>

/* Initialize channel in capture mode */
void ${TC_INSTANCE_NAME}_CH${CH_NUM}_CaptureInitialize (void)
{
    <#if TC_MATRIX_PRESENT == true>
        <#if .vars[TC_PCK7] == true>
        <#lt>    /* Enable PCK7 */
        <#lt>    MATRIX_REGS->CCFG_PCCR |= CCFG_PCCR_TC0CC_Msk;

        </#if>
    </#if>
    <#if .vars[TC_CMR_TCCLKS] == "">
    /* Use peripheral clock */
    ${TC_INSTANCE_NAME}_REGS->TC_CHANNEL[${CH_NUM}].TC_EMR = TC_EMR_NODIVCLK_Msk;
        /* clock selection and capture configurations */
    ${TC_INSTANCE_NAME}_REGS->TC_CHANNEL[${CH_NUM}].TC_CMR = TC_CMR_CAPTURE_LDRA_${.vars[TC_CMR_LDRA]} | TC_CMR_CAPTURE_LDRB_${.vars[TC_CMR_LDRB]}<#rt>
        <#lt>${.vars[TC_CAPTURE_CMR_LDBSTOP]?then('| (TC_CMR_CAPTURE_LDBSTOP_Msk)', '')};

    <#else>
    /* clock selection and capture configurations */
    ${TC_INSTANCE_NAME}_REGS->TC_CHANNEL[${CH_NUM}].TC_CMR = TC_CMR_TCCLKS_${.vars[TC_CMR_TCCLKS]} | TC_CMR_CAPTURE_LDRA_${.vars[TC_CMR_LDRA]} \
        | TC_CMR_CAPTURE_LDRB_${.vars[TC_CMR_LDRB]} <#rt>
        <#lt>${.vars[TC_CAPTURE_CMR_LDBSTOP]?then('| (TC_CMR_CAPTURE_LDBSTOP_Msk)', '')};
    </#if>

    <#if .vars[TC_CAPTURE_EXT_RESET] == true>
    /* external reset event configurations */
    ${TC_INSTANCE_NAME}_REGS->TC_CHANNEL[${CH_NUM}].TC_CMR |= <#if .vars[TC_CMR_ABETRG] == "TIOA"> TC_CMR_CAPTURE_ABETRG_Msk | </#if> TC_CMR_CAPTURE_ETRGEDG_${.vars[TC_CMR_ETRGEDG]};
    </#if>

    <#if .vars[TC_CAPTURE_IER_LDRAS] == true || .vars[TC_CAPTURE_IER_LDRBS] == true || .vars[TC_CAPTURE_IER_COVFS] == true>
    <#compress>
        <#assign CAPTURE_INTERRUPT = "">
        <#if .vars[TC_CAPTURE_IER_LDRAS] == true >
            <#assign CAPTURE_INTERRUPT = "TC_IER_LDRAS_Msk">
        </#if>
        <#if .vars[TC_CAPTURE_IER_LDRBS] == true >
            <#if CAPTURE_INTERRUPT != "">
                <#assign CAPTURE_INTERRUPT = CAPTURE_INTERRUPT + " | TC_IER_LDRBS_Msk">
            <#else>
                <#assign CAPTURE_INTERRUPT = "TC_IER_LDRBS_Msk">
            </#if>
        </#if>
        <#if .vars[TC_CAPTURE_IER_COVFS] == true >
            <#if CAPTURE_INTERRUPT != "">
                <#assign CAPTURE_INTERRUPT = CAPTURE_INTERRUPT + " | TC_IER_COVFS_Msk">
            <#else>
                <#assign CAPTURE_INTERRUPT = "TC_IER_COVFS_Msk">
            </#if>
        </#if>
    </#compress>
    /* enable interrupt */
    ${TC_INSTANCE_NAME}_REGS->TC_CHANNEL[${CH_NUM}].TC_IER = ${CAPTURE_INTERRUPT};
    ${TC_INSTANCE_NAME}_CH${CH_NUM}_CallbackObj.callback_fn = NULL;
    </#if>
}

/* Start the capture mode */
void ${TC_INSTANCE_NAME}_CH${CH_NUM}_CaptureStart (void)
{
    ${TC_INSTANCE_NAME}_REGS->TC_CHANNEL[${CH_NUM}].TC_CCR = (TC_CCR_CLKEN_Msk | TC_CCR_SWTRG_Msk);
}

/* Stop the capture mode */
void ${TC_INSTANCE_NAME}_CH${CH_NUM}_CaptureStop (void)
{
    ${TC_INSTANCE_NAME}_REGS->TC_CHANNEL[${CH_NUM}].TC_CCR = (TC_CCR_CLKDIS_Msk);
}

uint32_t ${TC_INSTANCE_NAME}_CH${CH_NUM}_CaptureFrequencyGet( void )
{
    return (uint32_t)(${.vars[TC_CH_CLOCK_FREQ]}UL);
}

/* Read last captured value of Capture A */
${TC_UNSIGNED_INT_TYPE} ${TC_INSTANCE_NAME}_CH${CH_NUM}_CaptureAGet (void)
{
    return ${TC_INSTANCE_NAME}_REGS->TC_CHANNEL[${CH_NUM}].TC_RA;
}

/* Read last captured value of Capture B */
${TC_UNSIGNED_INT_TYPE} ${TC_INSTANCE_NAME}_CH${CH_NUM}_CaptureBGet (void)
{
    return ${TC_INSTANCE_NAME}_REGS->TC_CHANNEL[${CH_NUM}].TC_RB;
}

<#if .vars[TC_CAPTURE_IER_LDRAS] == true || .vars[TC_CAPTURE_IER_LDRBS] == true || .vars[TC_CAPTURE_IER_COVFS] == true>
/* Register callback function */
void ${TC_INSTANCE_NAME}_CH${CH_NUM}_CaptureCallbackRegister(TC_CAPTURE_CALLBACK callback, uintptr_t context)
{
    ${TC_INSTANCE_NAME}_CH${CH_NUM}_CallbackObj.callback_fn = callback;
    ${TC_INSTANCE_NAME}_CH${CH_NUM}_CallbackObj.context = context;
}

void ${TC_INSTANCE_NAME}_CH${CH_NUM}_InterruptHandler(void)
{
    TC_CAPTURE_STATUS capture_status = (TC_CAPTURE_STATUS)(${TC_INSTANCE_NAME}_REGS->TC_CHANNEL[${CH_NUM}].TC_SR & TC_CAPTURE_STATUS_MSK);
    /* Call registered callback function */
    if ((TC_CAPTURE_NONE != capture_status) && ${TC_INSTANCE_NAME}_CH${CH_NUM}_CallbackObj.callback_fn != NULL)
    {
        ${TC_INSTANCE_NAME}_CH${CH_NUM}_CallbackObj.callback_fn(capture_status, ${TC_INSTANCE_NAME}_CH${CH_NUM}_CallbackObj.context);
    }
}
<#else>
TC_CAPTURE_STATUS ${TC_INSTANCE_NAME}_CH${CH_NUM}_CaptureStatusGet(void)
{
    return (TC_CAPTURE_STATUS)(${TC_INSTANCE_NAME}_REGS->TC_CHANNEL[${CH_NUM}].TC_SR & TC_CAPTURE_STATUS_MSK);
}
</#if>
</#if> <#-- CAPTURE -->

<#if .vars[TC_CH_OPERATINGMODE] == "COMPARE">
<#if .vars[TC_COMPARE_IER_CPCS] == true>
/* Callback object for channel ${CH_NUM} */
TC_COMPARE_CALLBACK_OBJECT ${TC_INSTANCE_NAME}_CH${CH_NUM}_CallbackObj;
</#if>

/* Initialize channel in compare mode */
void ${TC_INSTANCE_NAME}_CH${CH_NUM}_CompareInitialize (void)
{
    <#if TC_MATRIX_PRESENT == true>
        <#if .vars[TC_PCK7] == true>
        <#lt>    /* Enable PCK7 */
        <#lt>    MATRIX_REGS->CCFG_PCCR |= CCFG_PCCR_TC0CC_Msk;

        </#if>
    </#if>
    <#if .vars[TC_CMR_TCCLKS] == "">
    /* Use peripheral clock */
    ${TC_INSTANCE_NAME}_REGS->TC_CHANNEL[${CH_NUM}].TC_EMR = TC_EMR_NODIVCLK_Msk;
    /* clock selection and waveform selection */
    ${TC_INSTANCE_NAME}_REGS->TC_CHANNEL[${CH_NUM}].TC_CMR =  TC_CMR_WAVEFORM_WAVSEL_${.vars[TC_CMR_WAVSEL]} | TC_CMR_WAVE_Msk | \
                TC_CMR_WAVEFORM_ACPA_${.vars[TC_CMR_ACPA]} | TC_CMR_WAVEFORM_ACPC_${.vars[TC_CMR_ACPC]} | TC_CMR_WAVEFORM_AEEVT_${.vars[TC_CMR_AEEVT]}\
<#if .vars[TC_CMR_EEVT] != "TIOB">           | TC_CMR_WAVEFORM_BCPB_${.vars[TC_CMR_BCPB]} | TC_CMR_WAVEFORM_BCPC_${.vars[TC_CMR_BCPC]} | TC_CMR_WAVEFORM_BEEVT_${.vars[TC_CMR_BEEVT]}</#if> <#rt>
                <#lt>${.vars[TC_COMPARE_CMR_CPCSTOP]?then('| (TC_CMR_WAVEFORM_CPCSTOP_Msk)', '')};
    <#else>
    /* clock selection and waveform selection */
    ${TC_INSTANCE_NAME}_REGS->TC_CHANNEL[${CH_NUM}].TC_CMR = TC_CMR_TCCLKS_${.vars[TC_CMR_TCCLKS]} | TC_CMR_WAVEFORM_WAVSEL_${.vars[TC_CMR_WAVSEL]} | TC_CMR_WAVE_Msk | \
            TC_CMR_WAVEFORM_ACPA_${.vars[TC_CMR_ACPA]} | TC_CMR_WAVEFORM_ACPC_${.vars[TC_CMR_ACPC]} | TC_CMR_WAVEFORM_AEEVT_${.vars[TC_CMR_AEEVT]} \
<#if .vars[TC_CMR_EEVT] != "TIOB">           | TC_CMR_WAVEFORM_BCPB_${.vars[TC_CMR_BCPB]} | TC_CMR_WAVEFORM_BCPC_${.vars[TC_CMR_BCPC]} | TC_CMR_WAVEFORM_BEEVT_${.vars[TC_CMR_BEEVT]}</#if> <#rt>
                <#lt>${.vars[TC_COMPARE_CMR_CPCSTOP]?then('| (TC_CMR_CPCSTOP_Msk)', '')};
    </#if>

    /* external reset event configurations */
    ${TC_INSTANCE_NAME}_REGS->TC_CHANNEL[${CH_NUM}].TC_CMR |= TC_CMR_WAVEFORM_ENETRG_Msk | TC_CMR_WAVEFORM_EEVT_${.vars[TC_CMR_EEVT]} | \
                TC_CMR_WAVEFORM_EEVTEDG_${.vars[TC_CMP_CMR_ETRGEDG]};

    /* write period */
    ${TC_INSTANCE_NAME}_REGS->TC_CHANNEL[${CH_NUM}].TC_RC = ${.vars[TC_COMPARE_PERIOD_COUNT]}U;

    /* write compare values */
    ${TC_INSTANCE_NAME}_REGS->TC_CHANNEL[${CH_NUM}].TC_RA = ${.vars[TC_COMPARE_A]}U;
    ${TC_INSTANCE_NAME}_REGS->TC_CHANNEL[${CH_NUM}].TC_RB = ${.vars[TC_COMPARE_B]}U;

    <#if .vars[TC_COMPARE_IER_CPCS] == true>
    /* enable interrupt */
    ${TC_INSTANCE_NAME}_REGS->TC_CHANNEL[${CH_NUM}].TC_IER = TC_IER_CPCS_Msk;
    ${TC_INSTANCE_NAME}_CH${CH_NUM}_CallbackObj.callback_fn = NULL;
    </#if>
}

/* Start the compare mode */
void ${TC_INSTANCE_NAME}_CH${CH_NUM}_CompareStart (void)
{
    ${TC_INSTANCE_NAME}_REGS->TC_CHANNEL[${CH_NUM}].TC_CCR = (TC_CCR_CLKEN_Msk | TC_CCR_SWTRG_Msk);
}

/* Stop the compare mode */
void ${TC_INSTANCE_NAME}_CH${CH_NUM}_CompareStop (void)
{
    ${TC_INSTANCE_NAME}_REGS->TC_CHANNEL[${CH_NUM}].TC_CCR = (TC_CCR_CLKDIS_Msk);
}

uint32_t ${TC_INSTANCE_NAME}_CH${CH_NUM}_CompareFrequencyGet( void )
{
    return (uint32_t)(${.vars[TC_CH_CLOCK_FREQ]}UL);
}

/* Configure the period value */
void ${TC_INSTANCE_NAME}_CH${CH_NUM}_ComparePeriodSet (${TC_UNSIGNED_INT_TYPE} period)
{
    ${TC_INSTANCE_NAME}_REGS->TC_CHANNEL[${CH_NUM}].TC_RC = period;
}

/* Read the period value */
${TC_UNSIGNED_INT_TYPE} ${TC_INSTANCE_NAME}_CH${CH_NUM}_ComparePeriodGet (void)
{
    return ${TC_INSTANCE_NAME}_REGS->TC_CHANNEL[${CH_NUM}].TC_RC;
}

/* Set the compare A value */
void ${TC_INSTANCE_NAME}_CH${CH_NUM}_CompareASet (${TC_UNSIGNED_INT_TYPE} value)
{
    ${TC_INSTANCE_NAME}_REGS->TC_CHANNEL[${CH_NUM}].TC_RA = value;
}

/* Set the compare B value */
void ${TC_INSTANCE_NAME}_CH${CH_NUM}_CompareBSet (${TC_UNSIGNED_INT_TYPE} value)
{
    ${TC_INSTANCE_NAME}_REGS->TC_CHANNEL[${CH_NUM}].TC_RB = value;
}

<#if .vars[TC_COMPARE_IER_CPCS] == true>
/* Register callback function */
void ${TC_INSTANCE_NAME}_CH${CH_NUM}_CompareCallbackRegister(TC_COMPARE_CALLBACK callback, uintptr_t context)
{
    ${TC_INSTANCE_NAME}_CH${CH_NUM}_CallbackObj.callback_fn = callback;
    ${TC_INSTANCE_NAME}_CH${CH_NUM}_CallbackObj.context = context;
}

/* Interrupt Handler */
void ${TC_INSTANCE_NAME}_CH${CH_NUM}_InterruptHandler(void)
{
    TC_COMPARE_STATUS compare_status = (TC_COMPARE_STATUS)(${TC_INSTANCE_NAME}_REGS->TC_CHANNEL[${CH_NUM}].TC_SR & TC_COMPARE_STATUS_MSK);
    /* Call registered callback function */
    if ((TC_COMPARE_NONE != compare_status) && ${TC_INSTANCE_NAME}_CH${CH_NUM}_CallbackObj.callback_fn != NULL)
    {
        ${TC_INSTANCE_NAME}_CH${CH_NUM}_CallbackObj.callback_fn(compare_status, ${TC_INSTANCE_NAME}_CH${CH_NUM}_CallbackObj.context);
    }
}
<#else>
TC_COMPARE_STATUS ${TC_INSTANCE_NAME}_CH${CH_NUM}_CompareStatusGet(void)
{
    return (TC_COMPARE_STATUS)(${TC_INSTANCE_NAME}_REGS->TC_CHANNEL[${CH_NUM}].TC_SR & TC_COMPARE_STATUS_MSK);
}
</#if>
</#if> <#-- COMPARE -->

</#if> <#-- CH_ENABLE -->
</#list>

<#--  If a common interrupt symbol exists -->
<#if TC_COMMON_INTERRUPT_STATUS??>
<#--  If common interrupt is enabled -->
<#if TC_COMMON_INTERRUPT_STATUS == true>
/* Interrupt handler for ${TC_INSTANCE_NAME} */
void ${TC_INSTANCE_NAME}_InterruptHandler(void)
{
	<#if .vars[TC_INSTANCE_NAME + "_CH0_INTERRUPT_ENABLE"] == true>
	${TC_INSTANCE_NAME}_CH0_InterruptHandler();
	</#if>
	<#if .vars[TC_INSTANCE_NAME + "_CH1_INTERRUPT_ENABLE"] == true>

	${TC_INSTANCE_NAME}_CH1_InterruptHandler();
	</#if>
	<#if .vars[TC_INSTANCE_NAME + "_CH2_INTERRUPT_ENABLE"] == true>

	${TC_INSTANCE_NAME}_CH2_InterruptHandler();
	</#if>
}
</#if> <#-- common interrupt is enabled -->
</#if> <#-- common interrupt exists -->
/**
 End of File
*/
