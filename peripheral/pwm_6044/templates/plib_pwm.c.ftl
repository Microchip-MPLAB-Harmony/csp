/*******************************************************************************
  PWM Peripheral Library Interface Source File

  Company
    Microchip Technology Inc.

  File Name
    plib_${PWM_INSTANCE_NAME}.c

  Summary
    ${PWM_INSTANCE_NAME} peripheral library source file.

  Description
    This file implements the interface to the PWM peripheral library.  This
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
#include "plib_${PWM_INSTANCE_NAME?lower_case}.h"

<#compress>
<#assign PWM_INTERRUPT = false>

<#list 0..3 as i>
    <#assign PWM_IER_CHID = "CH" + i + "_IER_CHID">
    <#assign PWM_CH_ENABLE = "CH" + i + "_EN">
    <#if .vars[PWM_CH_ENABLE] == true && .vars[PWM_IER_CHID] == true>
        <#assign PWM_INTERRUPT = true>
    </#if>
</#list>
</#compress>

<#if PWM_INTERRUPT == true>
    <#lt>/* Object to hold callback function and context */
    <#lt>PWM_CALLBACK_OBJECT ${PWM_INSTANCE_NAME}_CallbackObj;
</#if>

/* Initialize enabled PWM channels */
void ${PWM_INSTANCE_NAME}_Initialize (void)
{
<#if CLKA_EN == true && CLKB_EN == true>
    /* Clock configuration */
    ${PWM_INSTANCE_NAME}_REGS->PWM_MR = PWM_MR_PREA_${CLKA_PRES} | PWM_MR_DIVA(${CLKA_DIV}) |
        PWM_MR_PREB_${CLKB_PRES} | PWM_MR_DIVB(${CLKB_DIV});
<#elseif CLKA_EN == true>
    /* Clock configuration */
    ${PWM_INSTANCE_NAME}_REGS->PWM_MR = PWM_MR_PREA_${CLKA_PRES} | PWM_MR_DIVA(${CLKA_DIV});
<#elseif CLKB_EN == true>
    /* Clock configuration */
    ${PWM_INSTANCE_NAME}_REGS->PWM_MR = PWM_MR_PREB_${CLKB_PRES} | PWM_MR_DIVB(${CLKB_DIV});
</#if>

<#assign PWM_INTERRUPT = false>
<#list 0..3 as i>
<#assign CH_NUM = i >
<#assign PWM_CH_ENABLE = "CH" + i + "_EN">
<#assign PWM_IER_CHID  = "CH" + i + "_IER_CHID">
<#assign PWM_CMR_CPRE  = "CH" + i + "_PRES">
<#assign PWM_CMR_CALG  = "CH" + i + "_CALG">
<#assign PWM_CMR_CPOL  = "CH" + i + "_CPOL">
<#assign PWM_CPRD      = "CH" + i +"_CPRD">
<#assign PWM_CDTY      = "CH" + i + "_CDTY">
<#if .vars[PWM_CH_ENABLE] == true>

    /************** Channel ${CH_NUM} *************************/
    /* Channel Mode */
    ${PWM_INSTANCE_NAME}_REGS->PWM_CH_NUM[${CH_NUM}].PWM_CMR = PWM_CMR_CPRE_${.vars[PWM_CMR_CPRE]} | PWM_CMR_CALG_${.vars[PWM_CMR_CALG]} | \
                                                               PWM_CMR_CPOL_${.vars[PWM_CMR_CPOL]};

    /* Channel Period */
    ${PWM_INSTANCE_NAME}_REGS->PWM_CH_NUM[${CH_NUM}].PWM_CPRD = ${.vars[PWM_CPRD]}U;

    /* Channel Duty */
    ${PWM_INSTANCE_NAME}_REGS->PWM_CH_NUM[${CH_NUM}].PWM_CDTY  = ${.vars[PWM_CDTY]}U;
    <#if .vars[PWM_IER_CHID] == true>
        <#assign PWM_INTERRUPT = true>

        <#lt>    /* Enable counter event */
        <#lt>    ${PWM_INSTANCE_NAME}_REGS->PWM_IER = (0x1U << ${CH_NUM}U);
    </#if>
</#if><#-- PWM_CH_ENABLE -->
</#list>
<#if PWM_INTERRUPT == true>

    ${PWM_INSTANCE_NAME}_CallbackObj.callback_fn = NULL;
</#if><#-- PWM_INTERRUPT -->
}

void ${PWM_INSTANCE_NAME}_ChannelsStart (PWM_CHANNEL_MASK channelMask)
{
    ${PWM_INSTANCE_NAME}_REGS->PWM_ENA = channelMask;
}

void ${PWM_INSTANCE_NAME}_ChannelsStop (PWM_CHANNEL_MASK channelMask)
{
    ${PWM_INSTANCE_NAME}_REGS->PWM_DIS = channelMask;
}

void ${PWM_INSTANCE_NAME}_ChannelPeriodSet (PWM_CHANNEL_NUM channel, uint32_t period)
{
    if(0 != ((${PWM_INSTANCE_NAME}_REGS->PWM_SR >> channel) & 0x1U))
    {
        ${PWM_INSTANCE_NAME}_REGS->PWM_CH_NUM[channel].PWM_CMR |= PWM_CMR_CPD_Msk;
        ${PWM_INSTANCE_NAME}_REGS->PWM_CH_NUM[channel].PWM_CUPD = period;
    }
    else
    {
        ${PWM_INSTANCE_NAME}_REGS->PWM_CH_NUM[channel].PWM_CPRD = period;
    }
}

uint32_t ${PWM_INSTANCE_NAME}_ChannelPeriodGet (PWM_CHANNEL_NUM channel)
{
    return ${PWM_INSTANCE_NAME}_REGS->PWM_CH_NUM[channel].PWM_CPRD;
}

void ${PWM_INSTANCE_NAME}_ChannelDutySet(PWM_CHANNEL_NUM channel, uint32_t duty)
{
    if(0 != ((${PWM_INSTANCE_NAME}_REGS->PWM_SR >> channel) & 0x1U))
    {
        ${PWM_INSTANCE_NAME}_REGS->PWM_CH_NUM[channel].PWM_CMR &= ~PWM_CMR_CPD_Msk;
        ${PWM_INSTANCE_NAME}_REGS->PWM_CH_NUM[channel].PWM_CUPD = duty;
    }
    else
    {
        ${PWM_INSTANCE_NAME}_REGS->PWM_CH_NUM[channel].PWM_CDTY = duty;
    }
}

void ${PWM_INSTANCE_NAME}_ChannelInterruptEnable (PWM_CHANNEL_MASK channelMask)
{
    ${PWM_INSTANCE_NAME}_REGS->PWM_IER = channelMask;
}

void ${PWM_INSTANCE_NAME}_ChannelInterruptDisable (PWM_CHANNEL_MASK channelMask)
{
    ${PWM_INSTANCE_NAME}_REGS->PWM_IDR = channelMask;
}

<#if PWM_INTERRUPT == true>
    <#lt> /* Register callback function */
    <#lt>void ${PWM_INSTANCE_NAME}_CallbackRegister(PWM_CALLBACK callback, uintptr_t context)
    <#lt>{
    <#lt>    ${PWM_INSTANCE_NAME}_CallbackObj.callback_fn = callback;
    <#lt>    ${PWM_INSTANCE_NAME}_CallbackObj.context = context;
    <#lt>}

    <#lt>/* Interrupt Handler */
    <#lt>void ${PWM_INSTANCE_NAME}_InterruptHandler(void)
    <#lt>{
    <#lt>    uint32_t status;
    <#lt>    status = ${PWM_INSTANCE_NAME}_REGS->PWM_ISR;
    <#lt>    if (${PWM_INSTANCE_NAME}_CallbackObj.callback_fn != NULL)
    <#lt>    {
    <#lt>        ${PWM_INSTANCE_NAME}_CallbackObj.callback_fn(status, ${PWM_INSTANCE_NAME}_CallbackObj.context);
    <#lt>    }
    <#lt>}

<#else>

/* Check the status of counter event */
bool ${PWM_INSTANCE_NAME}_ChannelCounterEventStatusGet (PWM_CHANNEL_NUM channel)
{
    bool status;
    status = (${PWM_INSTANCE_NAME}_REGS->PWM_ISR >> channel) & 0x1U;
    return status;
}
</#if>

/**
 End of File
*/
