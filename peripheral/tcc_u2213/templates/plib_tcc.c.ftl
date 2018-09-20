/*******************************************************************************
  TCC Peripheral Library Interface Source File

  Company
    Microchip Technology Inc.

  File Name
    plib_${TCC_INSTANCE_NAME?lower_case}.c

  Summary
    ${TCC_INSTANCE_NAME} peripheral library source file.

  Description
    This file implements the interface to the TCC peripheral library.  This
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
#include "device.h"
#include "plib_${TCC_INSTANCE_NAME?lower_case}.h"

<#compress>
<#assign TCC_INTERRUPT = false>
<#assign TCC_WAVE_VAL = "">
<#assign TCC_WEXCTRL_DT_VAL = "">
<#assign TCC_DRVCTRL_FAULT_VAL = "">
<#assign TCC_PATT_VAL = "">
<#assign TCC_EVCTRL_VAL = "">
<#assign TCC_CTRLB_DIR = "">

<#list 0..(TCC_NUM_CHANNELS-1) as i>
<#assign CH_NUM = i >
<#assign TCC_POLARITY = "TCC_"+i+"_WAVE_POL">
<#assign TCC_MCEO = "TCC_"+i+"_EVCTRL_MCEO">
<#-- Dead Time -->
<#if TCC_IS_DEAD_TIME == 1>
    <#assign TCC_DT_ENABLE = "TCC_"+i+"_WEXCTRL_DTIEN">
    <#if .vars[TCC_DT_ENABLE] == true>
        <#if TCC_WEXCTRL_DT_VAL != "">
            <#assign TCC_WEXCTRL_DT_VAL = TCC_WEXCTRL_DT_VAL + " | TCC_WEXCTRL_DTIEN"+i+"_Msk">
        <#else>
            <#assign TCC_WEXCTRL_DT_VAL = "TCC_WEXCTRL_DTIEN"+i+"_Msk">
        </#if>
    </#if>
</#if> <#-- Dead Time End -->
<#-- swap -->
<#if TCC_IS_SWAP == 1>
    <#assign TCC_SWAP_ENABLE = "TCC_"+i+"_WAVE_SWAP">
    <#if .vars[TCC_SWAP_ENABLE] == true>
        <#if TCC_WAVE_VAL != "">
            <#assign TCC_WAVE_VAL = TCC_WAVE_VAL + " \n \t \t | TCC_WAVE_SWAP"+i+"_Msk">
        <#else>
            <#assign TCC_WAVE_VAL = "TCC_WAVE_SWAP"+i+"_Msk">
        </#if>
    </#if>
</#if> <#-- Swap End -->
<#-- polarity -->
<#if (TCC_WAVE_WAVEGEN == "DSBOTTOM") || (TCC_WAVE_WAVEGEN == "DSBOTH") || (TCC_WAVE_WAVEGEN == "DSTOP") >
    <#if TCC_WAVE_VAL != "">
        <#assign TCC_WAVE_VAL = TCC_WAVE_VAL + " | TCC_WAVE_POL"+i+"("+.vars[TCC_POLARITY]+"U)">
    <#else>
        <#assign TCC_WAVE_VAL = "TCC_WAVE_POL"+i+"("+.vars[TCC_POLARITY]+"U)">
    </#if>
</#if>
<#-- polarity end -->
<#-- Events -->
<#if .vars[TCC_MCEO] == true>
    <#if TCC_EVCTRL_VAL != "">
        <#assign TCC_EVCTRL_VAL = TCC_EVCTRL_VAL + " | TCC_EVCTRL_MCEO"+i+"_Msk">
    <#else>
        <#assign TCC_EVCTRL_VAL = "TCC_EVCTRL_MCEO"+i+"_Msk">
    </#if>
</#if>
</#list>

<#if TCC_WAVE_WAVEGEN == "NPWM">
    <#if TCC_CTRLBSET_DIR == true>
        <#assign TCC_CTRLB_DIR = "TCC_CTRLBSET_DIR_Msk">
    </#if>
</#if>

<#-- Fault -->
<#list 0..(TCC_NUM_OUTPUTS-1) as i>
<#assign CH_NUM = i >
<#assign TCC_FAULT_POLARITY = "TCC_"+i+"_DRVCTRL_NRE_NRV">
<#if .vars[TCC_FAULT_POLARITY] != "-1">
    <#if TCC_DRVCTRL_FAULT_VAL != "">
        <#assign TCC_DRVCTRL_FAULT_VAL = TCC_DRVCTRL_FAULT_VAL + " | TCC_DRVCTRL_NRE"+i+"("+.vars[TCC_FAULT_POLARITY]+"U)">
    <#else>
        <#assign TCC_DRVCTRL_FAULT_VAL = "TCC_DRVCTRL_NRE"+i+"("+.vars[TCC_FAULT_POLARITY]+"U)">
    </#if>
</#if>
</#list>

<#-- Pattern Generation -->
<#if TCC_IS_PG == 1>
<#list 0..(TCC_NUM_OUTPUTS-1) as i>
<#assign CH_NUM = i >
<#assign TCC_PATT_PGE = "TCC_"+i+"PATT_PGE">
<#assign TCC_PATT_PGV = "TCC_"+i+"PATT_PGV">
<#if .vars[TCC_PATT_PGE] == true>
        <#if TCC_PATT_VAL != "">
            <#assign TCC_PATT_VAL = TCC_PATT_VAL + " \n \t \t | TCC_PATT_PGE"+i+"_Msk | TCC_PATT_PGV"+i+"("+.vars[TCC_PATT_PGV]+"U)">
        <#else>
            <#assign TCC_PATT_VAL = "TCC_PATT_PGE"+i+"_Msk | TCC_PATT_PGV"+i+"("+.vars[TCC_PATT_PGV]+"U)">
        </#if>
</#if>
</#list>
</#if>
<#if TCC_INTENSET_OVF == true>
    <#assign TCC_INTERRUPT = true>
</#if>
<#assign TCC_WEXCTRL_DT_VAL = TCC_WEXCTRL_DT_VAL + "\n \t \t | TCC_WEXCTRL_DTLS(${TCC_WEXCTRL_DTLS}U) | TCC_WEXCTRL_DTHS(${TCC_WEXCTRL_DTHS}U)">

<#if TCC_EVCTRL_OVFEO == true>
    <#assign TCC_EVCTRL_VAL = TCC_EVCTRL_VAL + " | TCC_EVCTRL_OVFEO_Msk">
</#if>
</#compress>

static uint32_t ${TCC_INSTANCE_NAME}_status;  /* Saves interrupt status */

<#if TCC_INTERRUPT == true>
    <#lt>/* Object to hold callback function and context */
    <#lt>TCC_CALLBACK_OBJECT ${TCC_INSTANCE_NAME}_CallbackObj;
</#if>

/* Initialize TCC module */
void ${TCC_INSTANCE_NAME}_PWMInitialize(void)
{
    /* Reset TCC */
    ${TCC_INSTANCE_NAME}_REGS->TCC_CTRLA = TCC_CTRLA_SWRST_Msk;
    while (${TCC_INSTANCE_NAME}_REGS->TCC_SYNCBUSY & (TCC_SYNCBUSY_SWRST_Msk))
    {
        /* Wait for sync */
    }
    /* Clock prescaler */
    ${TCC_INSTANCE_NAME}_REGS->TCC_CTRLA = TCC_CTRLA_PRESCALER_${TCC_CTRLA_PRESCALER};
<#if TCC_CTRLB_DIR?has_content>
    ${TCC_INSTANCE_NAME}_REGS->TCC_CTRLBSET = ${TCC_CTRLB_DIR};
    while (${TCC_INSTANCE_NAME}_REGS->TCC_SYNCBUSY & (TCC_SYNCBUSY_CTRLB_Msk))
    {
        /* Wait for sync */
    }
</#if>
<#if TCC_IS_OTM == 1>
    ${TCC_INSTANCE_NAME}_REGS->TCC_WEXCTRL = TCC_WEXCTRL_OTMX(${TCC_WEXCTRL_OTMX}U);
</#if>
<#if TCC_WEXCTRL_DT_VAL?has_content && TCC_IS_DEAD_TIME == 1>
    ${TCC_INSTANCE_NAME}_REGS->TCC_WEXCTRL |= ${TCC_WEXCTRL_DT_VAL};
</#if>

    /* PWM Waveform type */
    ${TCC_INSTANCE_NAME}_REGS->TCC_WAVE = TCC_WAVE_WAVEGEN_${TCC_WAVE_WAVEGEN};
<#if TCC_WAVE_VAL?has_content>
    ${TCC_INSTANCE_NAME}_REGS->TCC_WAVE |= ${TCC_WAVE_VAL};
</#if>
    while (${TCC_INSTANCE_NAME}_REGS->TCC_SYNCBUSY & (TCC_SYNCBUSY_WAVE_Msk))
    {
        /* Wait for sync */
    }
    
    /* Configure duty cycle values */
<#list 0..(TCC_NUM_CHANNELS-1) as i>
    <#assign TCC_CC = "TCC_"+i+"_CC">
    <#assign CH_NUM = i>
    ${TCC_INSTANCE_NAME}_REGS->TCC_CC[${i}] = ${.vars[TCC_CC]}U;
    while (${TCC_INSTANCE_NAME}_REGS->TCC_SYNCBUSY & (TCC_SYNCBUSY_CC${CH_NUM}_Msk))
    {
        /* Wait for sync */
    }
</#list>

    ${TCC_INSTANCE_NAME}_REGS->TCC_PER = ${TCC_PER_PER}U;
    while (${TCC_INSTANCE_NAME}_REGS->TCC_SYNCBUSY & (TCC_SYNCBUSY_PER_Msk))
    {
        /* Wait for sync */
    }

<#if TCC_EVCTRL_EVACT != "Disabled">
    <#if TCC_EVCTRL_EVACT == "Event 0">
        <#lt>    ${TCC_INSTANCE_NAME}_REGS->TCC_EVCTRL = TCC_EVCTRL_EVACT0_FAULT;
        <#lt>    ${TCC_INSTANCE_NAME}_REGS->TCC_DRVCTRL = TCC_DRVCTRL_FILTERVAL0(${TCC_DRVCTRL_FILTERVAL}U) <#rt>
                        <#lt><#if TCC_DRVCTRL_FAULT_VAL?has_content>| ${TCC_DRVCTRL_FAULT_VAL}</#if>;
    <#elseif TCC_EVCTRL_EVACT == "Event 1">
        <#lt>    ${TCC_INSTANCE_NAME}_REGS->TCC_EVCTRL = TCC_EVCTRL_EVACT1_FAULT;
        <#lt>    ${TCC_INSTANCE_NAME}_REGS->TCC_DRVCTRL = TCC_DRVCTRL_FILTERVAL1(${TCC_DRVCTRL_FILTERVAL}U) <#rt>
                        <#lt><#if TCC_DRVCTRL_FAULT_VAL?has_content>| ${TCC_DRVCTRL_FAULT_VAL}</#if>;
    </#if>
</#if>

<#if TCC_PATT_VAL?has_content>
    ${TCC_INSTANCE_NAME}_REGS->TCC_PATT = ${TCC_PATT_VAL};
    while (${TCC_INSTANCE_NAME}_REGS->TCC_SYNCBUSY & (TCC_SYNCBUSY_PATT_Msk))
    {
        /* Wait for sync */
    }
</#if>

<#if TCC_INTENSET_OVF == true>
    ${TCC_INSTANCE_NAME}_REGS->TCC_INTENSET = TCC_INTENSET_OVF_Msk;
</#if>

<#if TCC_EVCTRL_VAL?has_content>
    ${TCC_INSTANCE_NAME}_REGS->TCC_EVCTRL |= ${TCC_EVCTRL_VAL};
</#if>
}


/* Start the PWM generation */
void ${TCC_INSTANCE_NAME}_PWMStart(void)
{
    ${TCC_INSTANCE_NAME}_REGS->TCC_CTRLA |= TCC_CTRLA_ENABLE_Msk;
    while (${TCC_INSTANCE_NAME}_REGS->TCC_SYNCBUSY & (TCC_SYNCBUSY_ENABLE_Msk))
    {
        /* Wait for sync */
    }
}

/* Stop the PWM generation */
void ${TCC_INSTANCE_NAME}_PWMStop (void)
{
    ${TCC_INSTANCE_NAME}_REGS->TCC_CTRLA &= ~TCC_CTRLA_ENABLE_Msk;
    while (${TCC_INSTANCE_NAME}_REGS->TCC_SYNCBUSY & (TCC_SYNCBUSY_ENABLE_Msk))
    {
        /* Wait for sync */
    }
}

/* Configure PWM period */
<#if TCC_SIZE == 24>
void ${TCC_INSTANCE_NAME}_PWMPeriodSet (uint32_t period)
<#elseif TCC_SIZE == 16>
void ${TCC_INSTANCE_NAME}_PWMPeriodSet (uint16_t period)
</#if>
{
    ${TCC_INSTANCE_NAME}_REGS->TCC_PERBUF = period;
}

/* Read TCC period */
<#if TCC_SIZE == 24>
uint32_t ${TCC_INSTANCE_NAME}_PWMPeriodGet (void)
<#elseif TCC_SIZE == 16>
uint16_t ${TCC_INSTANCE_NAME}_PWMPeriodGet (void)
</#if>
{
    while (${TCC_INSTANCE_NAME}_REGS->TCC_SYNCBUSY & (TCC_SYNCBUSY_PER_Msk))
    {
        /* Wait for sync */
    }
<#if TCC_SIZE == 24>
    return (${TCC_INSTANCE_NAME}_REGS->TCC_PER & 0xFFFFFF);
<#elseif TCC_SIZE == 16>
    return (uint16_t)${TCC_INSTANCE_NAME}_REGS->TCC_PER;
</#if>
}

<#if TCC_IS_DEAD_TIME == 1>
/* Configure dead time */
void ${TCC_INSTANCE_NAME}_PWMDeadTimeSet (uint8_t deadtime_high, uint8_t deadtime_low)
{
    ${TCC_INSTANCE_NAME}_REGS->TCC_WEXCTRL &= ~(TCC_WEXCTRL_DTHS_Msk | TCC_WEXCTRL_DTLS_Msk);
    ${TCC_INSTANCE_NAME}_REGS->TCC_WEXCTRL |= TCC_WEXCTRL_DTHS(deadtime_high) | TCC_WEXCTRL_DTLS(deadtime_low);
}
</#if>

/* Set the counter*/
<#if TCC_SIZE == 24>
void ${TCC_INSTANCE_NAME}_PWMCounterSet (uint32_t count_value)
<#elseif TCC_SIZE == 16>
void ${TCC_INSTANCE_NAME}_PWMCounterSet (uint16_t count_value)
</#if>
{
    ${TCC_INSTANCE_NAME}_REGS->TCC_COUNT = count_value;
    while (${TCC_INSTANCE_NAME}_REGS->TCC_SYNCBUSY & (TCC_SYNCBUSY_COUNT_Msk))
    {
        /* Wait for sync */
    }
}

/* Enable forced synchronous update */
void ${TCC_INSTANCE_NAME}_PWMForceUpdate(void)
{
    ${TCC_INSTANCE_NAME}_REGS->TCC_CTRLBSET |= TCC_CTRLBCLR_CMD_UPDATE;
    while (${TCC_INSTANCE_NAME}_REGS->TCC_SYNCBUSY & (TCC_SYNCBUSY_CTRLB_Msk))
    {
        /* Wait for sync */
    }
}

/* Enable the period interrupt - overflow or underflow interrupt */
void ${TCC_INSTANCE_NAME}_PWMPeriodInterruptEnable(void)
{
    ${TCC_INSTANCE_NAME}_REGS->TCC_INTENSET = TCC_INTENSET_OVF_Msk;
}

/* Disable the period interrupt - overflow or underflow interrupt */
void ${TCC_INSTANCE_NAME}_PWMPeriodInterruptDisable()
{
    ${TCC_INSTANCE_NAME}_REGS->TCC_INTENCLR = TCC_INTENCLR_OVF_Msk;
}

/* Read interrupt flags */
uint32_t ${TCC_INSTANCE_NAME}_PWMInterruptStatusGet(void)
{
    uint32_t interrupt_status;
    NVIC_DisableIRQ(${TCC_INSTANCE_NAME}_IRQn);
    interrupt_status = ${TCC_INSTANCE_NAME}_status | ${TCC_INSTANCE_NAME}_REGS->TCC_INTFLAG;
    ${TCC_INSTANCE_NAME}_status = 0U;
    /* Clear interrupt flags */
    ${TCC_INSTANCE_NAME}_REGS->TCC_INTFLAG = TCC_INTFLAG_Msk;
    NVIC_EnableIRQ(${TCC_INSTANCE_NAME}_IRQn);
    return interrupt_status;
}

<#if TCC_INTERRUPT == true>
    <#lt> /* Register callback function */
    <#lt>void ${TCC_INSTANCE_NAME}_PWMCallbackRegister(TCC_CALLBACK callback, uintptr_t context)
    <#lt>{
    <#lt>    ${TCC_INSTANCE_NAME}_CallbackObj.callback_fn = callback;
    <#lt>    ${TCC_INSTANCE_NAME}_CallbackObj.context = context;
    <#lt>}

    <#lt>/* Interrupt Handler */
    <#lt>void ${TCC_INSTANCE_NAME}_PWMInterruptHandler(void)
    <#lt>{
    <#lt>    ${TCC_INSTANCE_NAME}_status = ${TCC_INSTANCE_NAME}_REGS->TCC_INTFLAG;
    <#lt>    if (${TCC_INSTANCE_NAME}_CallbackObj.callback_fn != NULL)
    <#lt>    {
    <#lt>        ${TCC_INSTANCE_NAME}_CallbackObj.callback_fn(${TCC_INSTANCE_NAME}_CallbackObj.context);
    <#lt>    }
    <#lt>    /* Clear interrupt flags */
    <#lt>    ${TCC_INSTANCE_NAME}_REGS->TCC_INTFLAG = TCC_INTFLAG_Msk;
    <#lt>}
</#if>

/**
 End of File
*/
