/*******************************************************************************
Interface definition of RTT PLIB.

Company:
    Microchip Technology Inc.

File Name:
    plib_rtt.c

Summary:
    Interface definition of RTT Plib.

Description:
    This file defines the interface for the RTT Plib.
    It allows user to configure and generate Periodic events using a real time
    timer.
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

#include "device.h"
#include "plib_${RTT_INSTANCE_NAME?lower_case}.h"
<#if core.CoreSysIntFile == true>
#include "interrupts.h"
</#if>

<#if rttINCIEN == true || rttALMIEN == true>
    <#lt>static volatile RTT_OBJECT rtt;

</#if>
<#assign RTT_MR_VAL = "RTT_MR_RTPRES(" + rttRTPRES + "U) | RTT_MR_RTTDIS_Msk">
<#if rttINCIEN>
<#assign RTT_MR_VAL = RTT_MR_VAL + " | RTT_MR_RTTINCIEN_Msk">
</#if>
<#if rttALMIEN>
<#assign RTT_MR_VAL = RTT_MR_VAL + " | RTT_MR_ALMIEN_Msk">
</#if>
<#if rttRTC1HZ>
<#assign RTT_MR_VAL = RTT_MR_VAL + " | RTT_MR_RTC1HZ_Msk">
</#if>
<#if RTT_INC2_SUPPORTED && rttINC2EN>
<#assign RTT_MR_VAL = RTT_MR_VAL + " | RTT_MR_INC2AEN_Msk">
</#if>
<#if RTT_EVA_SUPPORTED && rttEVAEN>
<#assign RTT_MR_VAL = RTT_MR_VAL + " | RTT_MR_EVAEN_Msk">
</#if>
<#assign RTT_MODR_VAL = "">
<#if RTT_INC2_SUPPORTED>
<#assign RTT_MODR_VAL = "RTT_MODR_SELINC2(" + RTT_SELINC2 +")">
</#if>
<#if RTT_EVA_SUPPORTED>
<#if RTT_MODR_VAL?has_content>
<#assign RTT_MODR_VAL = RTT_MODR_VAL + "| RTT_MODR_SELTRGEV(" + RTT_SELTRGEV +")">
<#else>
<#assign RTT_MODR_VAL = "RTT_MODR_SELTRGEV(" + RTT_SELTRGEV +")">
</#if>
</#if>
void ${RTT_INSTANCE_NAME}_Initialize(void)
{
    ${RTT_INSTANCE_NAME}_REGS->RTT_MR = RTT_MR_RTTRST_Msk;
    ${RTT_INSTANCE_NAME}_REGS->RTT_MR = ${RTT_MR_VAL};
    <#if RTT_MODR_VAL?has_content>
    ${RTT_INSTANCE_NAME}_REGS->RTT_MODR = ${RTT_MODR_VAL};
    </#if>
}

void ${RTT_INSTANCE_NAME}_Enable(void)
{
    ${RTT_INSTANCE_NAME}_REGS->RTT_MR|= RTT_MR_RTTRST_Msk;
    ${RTT_INSTANCE_NAME}_REGS->RTT_MR&= ~(RTT_MR_RTTDIS_Msk);
}

void ${RTT_INSTANCE_NAME}_Disable(void)
{
    ${RTT_INSTANCE_NAME}_REGS->RTT_MR|= RTT_MR_RTTDIS_Msk;
}

void ${RTT_INSTANCE_NAME}_PrescalarUpdate(uint16_t prescale)
{
    uint32_t rtt_mr = ${RTT_INSTANCE_NAME}_REGS->RTT_MR;
    uint32_t flag = rtt_mr & RTT_MR_RTTINCIEN_Msk;
    rtt_mr &= ~(RTT_MR_RTPRES_Msk | RTT_MR_RTTINCIEN_Msk);
    ${RTT_INSTANCE_NAME}_REGS->RTT_MR = rtt_mr | prescale | RTT_MR_RTTRST_Msk;
    if (flag != 0U)
    {
        ${RTT_INSTANCE_NAME}_REGS->RTT_MR|=  RTT_MR_RTTINCIEN_Msk;
    }
}

<#if rttINCIEN == true || rttALMIEN == true>
    <#lt>void ${RTT_INSTANCE_NAME}_AlarmValueSet(uint32_t alarm)
    <#lt>{
    <#lt>	uint32_t flag = 0;
    <#lt>	flag = ${RTT_INSTANCE_NAME}_REGS->RTT_MR& (RTT_MR_ALMIEN_Msk);
    <#lt>	${RTT_INSTANCE_NAME}_REGS->RTT_MR&= ~(RTT_MR_ALMIEN_Msk);
    <#lt>	${RTT_INSTANCE_NAME}_REGS->RTT_AR = alarm;
    <#lt>	if (flag != 0U)
    <#lt>	{
    <#lt>		${RTT_INSTANCE_NAME}_REGS->RTT_MR|= RTT_MR_ALMIEN_Msk;
    <#lt>	}
    <#lt>
    <#lt>}
    <#lt>
    <#lt>void ${RTT_INSTANCE_NAME}_EnableInterrupt (RTT_INTERRUPT_TYPE type)
    <#lt>{
    <#lt>	${RTT_INSTANCE_NAME}_REGS->RTT_MR|= (uint32_t)type;
    <#lt>}
    <#lt>
    <#lt>void ${RTT_INSTANCE_NAME}_DisableInterrupt(RTT_INTERRUPT_TYPE type)
    <#lt>{
    <#lt>	${RTT_INSTANCE_NAME}_REGS->RTT_MR&= ~((uint32_t)type);
    <#lt>}
    <#lt>
    <#lt>void ${RTT_INSTANCE_NAME}_CallbackRegister( RTT_CALLBACK callback, uintptr_t context )
    <#lt>{
    <#lt>	rtt.callback = callback;
    <#lt>	rtt.context = context;
    <#lt>}
</#if>

uint32_t ${RTT_INSTANCE_NAME}_TimerValueGet(void)
{
    uint32_t rtt_val = ${RTT_INSTANCE_NAME}_REGS->RTT_VR;
    while (rtt_val != ${RTT_INSTANCE_NAME}_REGS->RTT_VR)
    {
        rtt_val = ${RTT_INSTANCE_NAME}_REGS->RTT_VR;
    }
    return rtt_val;
}

uint32_t ${RTT_INSTANCE_NAME}_FrequencyGet(void)
{
    uint32_t flag = 0;

    flag =  (${RTT_INSTANCE_NAME}_REGS->RTT_MR) & (RTT_MR_RTC1HZ_Msk);

    if (flag !=0U)
    {
        return 1;
    }
    else
    {
        flag = (${RTT_INSTANCE_NAME}_REGS->RTT_MR) & (RTT_MR_RTPRES_Msk);
        if (flag == 0U)
        {
            return (0);
        }
        else
        {
            return (32768U / flag);
        }
    }
}
<#if rttINCIEN == true || rttALMIEN == true>

void __attribute__((used)) ${RTT_INSTANCE_NAME}_InterruptHandler(void)
{
    uint32_t rtt_status = ${RTT_INSTANCE_NAME}_REGS->RTT_SR;
    uint32_t flags = ${RTT_INSTANCE_NAME}_REGS->RTT_MR;
    /* Additional temporary variable used to prevent MISRA violations (Rule 13.x) */
    uintptr_t context = rtt.context;
    ${RTT_INSTANCE_NAME}_REGS->RTT_MR&= ~(RTT_MR_ALMIEN_Msk | RTT_MR_RTTINCIEN_Msk);
    if((flags & RTT_MR_RTTINCIEN_Msk) != 0U)
    {
        if((rtt_status & RTT_SR_RTTINC_Msk) != 0U)
        {
            if (rtt.callback != NULL)
            {
                rtt.callback(RTT_PERIODIC, context);
            }
        }
        ${RTT_INSTANCE_NAME}_REGS->RTT_MR|= (RTT_MR_RTTINCIEN_Msk);
    }
    if((flags & RTT_MR_ALMIEN_Msk) != 0U)
    {
        if((rtt_status & RTT_SR_ALMS_Msk) != 0U)
        {
            if (rtt.callback != NULL)
            {
                rtt.callback(RTT_ALARM, context);
            }
        }
        ${RTT_INSTANCE_NAME}_REGS->RTT_MR|= (RTT_MR_ALMIEN_Msk);
    }
}
</#if>
