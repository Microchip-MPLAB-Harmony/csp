/*******************************************************************************
  Timer/Counter(${TC_INSTANCE_NAME}) PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_${TC_INSTANCE_NAME}.c

  Summary
    ${TC_INSTANCE_NAME} PLIB Implementation File.

  Description
    This file defines the interface to the TC peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

  Remarks:
    None.

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
/* This section lists the other files that are included in this file.
*/

#include "plib_${TC_INSTANCE_NAME?lower_case}.h"

// *****************************************************************************
// *****************************************************************************
// Section: Global Data
// *****************************************************************************
// *****************************************************************************

<#compress>

<#assign TC_CTRLC_VAL = "">
<#assign TC_EVCTRL_VAL = "">
<#assign TC_INTSET_VAL = "">

<#if TC_CAPTURE_CTRLC_CPTEN0 == true>
    <#if TC_CTRLC_VAL != "">
        <#assign TC_CTRLC_VAL = TC_CTRLC_VAL + " | TC_CTRLC_CPTEN0_Msk">
    <#else>
        <#assign TC_CTRLC_VAL = "TC_CTRLC_CPTEN0_Msk">
    </#if>

    <#if TC_CAPTURE_TRIGGER_ACTION0 == "PPW" || TC_CAPTURE_TRIGGER_ACTION0 == "PWP">
        <#if TC_CTRLC_VAL != "">
            <#assign TC_CTRLC_VAL = TC_CTRLC_VAL + " | TC_CTRLC_CPTEN1_Msk">
        <#else>
            <#assign TC_CTRLC_VAL = "TC_CTRLC_CPTEN1_Msk">
        </#if>
    <#else>
        <#if TC_CAPTURE_CTRLC_CPTEN1 == true>
            <#if TC_CTRLC_VAL != "">
                <#assign TC_CTRLC_VAL = TC_CTRLC_VAL + " | TC_CTRLC_CPTEN1_Msk">
            <#else>
                <#assign TC_CTRLC_VAL = "TC_CTRLC_CPTEN1_Msk">
            </#if>
        </#if>
    </#if>
    <#assign TC_EVCTRL_VAL = "TC_EVCTRL_EVACT_" + TC_CAPTURE_TRIGGER_ACTION0>
    <#if TC_CAPTURE_TRIGGER_EDGE0 == "0">
        <#if TC_EVCTRL_VAL != "">
            <#assign TC_EVCTRL_VAL = TC_EVCTRL_VAL + " | TC_EVCTRL_TCEI_Msk">
        <#else>
            <#assign TC_EVCTRL_VAL = "TC_EVCTRL_TCEI_Msk">
        </#if>
    </#if>
    <#if TC_CAPTURE_TRIGGER_EDGE0 == "1">
        <#if TC_EVCTRL_VAL != "">
            <#assign TC_EVCTRL_VAL = TC_EVCTRL_VAL + " | TC_EVCTRL_TCEI_Msk | TC_EVCTRL_TCINV_Msk">
        <#else>
            <#assign TC_EVCTRL_VAL = "TC_EVCTRL_TCEI_Msk | TC_EVCTRL_TCINV_Msk">
        </#if>
    </#if>

</#if>

<#list 0..(TC_NUM_CHANNELS - 1) as i>
<#assign TC_CAPTURE_ENABLE = "TC_CAPTURE_CTRLC_CPTEN"+i>
<#assign TC_CAPTURE_EVENT_OUT = "TC_CAPTURE_EVCTRL_MCEO"+i>
<#assign TC_CAPTURE_INTERRUPT = "TC_CAPTURE_INTSET_MC"+i>

<#if .vars[TC_CAPTURE_ENABLE] == true>
    <#if .vars[TC_CAPTURE_EVENT_OUT] == true>
        <#if TC_EVCTRL_VAL != "">
            <#assign TC_EVCTRL_VAL = TC_EVCTRL_VAL + " | TC_EVCTRL_MCEO"+i+"_Msk">
        <#else>
            <#assign TC_EVCTRL_VAL = "TC_EVCTRL_MCEO"+i+"_Msk">
        </#if>
    </#if>
    <#if .vars[TC_CAPTURE_INTERRUPT] == true>
        <#if TC_INTSET_VAL != "">
            <#assign TC_INTSET_VAL = TC_INTSET_VAL + " | TC_INTENSET_MC"+i+"_Msk">
        <#else>
            <#assign TC_INTSET_VAL = "TC_INTENSET_MC"+i+"_Msk">
        </#if>
    </#if>
</#if>   <#-- CAPTURE_ENABLE -->
</#list>

<#if TC_CAPTURE_ERR_INTERRUPT_MODE == true>
    <#if TC_INTSET_VAL != "">
        <#assign TC_INTSET_VAL = TC_INTSET_VAL + " | TC_INTENSET_ERR_Msk">
    <#else>
        <#assign TC_INTSET_VAL = "TC_INTENSET_ERR_Msk">
    </#if>
</#if>

<#if TC_CAPTURE_OVF_INTERRUPT_MODE == true>
    <#if TC_INTSET_VAL != "">
        <#assign TC_INTSET_VAL = TC_INTSET_VAL + " | TC_INTENSET_OVF_Msk">
    <#else>
        <#assign TC_INTSET_VAL = "TC_INTENSET_OVF_Msk">
    </#if>
</#if>

</#compress>

<#if TC_INTSET_VAL != "">
TC_CAPTURE_CALLBACK_OBJ ${TC_INSTANCE_NAME}_CallbackObject;
</#if>

// *****************************************************************************
// *****************************************************************************
// Section: ${TC_INSTANCE_NAME} Implementation
// *****************************************************************************
// *****************************************************************************

void ${TC_INSTANCE_NAME}_CaptureInitialize( void )
{
    /* Reset TC */
    ${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_CTRLA = TC_CTRLA_SWRST_Msk;

    while((${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_STATUS & TC_STATUS_SYNCBUSY_Msk))
    {
        /* Wait for Write Synchronization */
    }

    /* Configure counter mode, prescaler, standby */
    ${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_CTRLA = TC_CTRLA_MODE_${TC_CTRLA_MODE} | TC_CTRLA_PRESCALER_${TC_CTRLA_PRESCALER} <#rt>
                                  <#lt>${TC_CTRLA_RUNSTDBY?then('| TC_CTRLA_RUNSTDBY_Msk', '')};

<#if TC_CTRLC_VAL?has_content>
    ${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_CTRLC = ${TC_CTRLC_VAL};
</#if>

<#if TC_EVCTRL_VAL?has_content>
    ${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_EVCTRL = ${TC_EVCTRL_VAL};
</#if>

    /* Clear all interrupt flags */
    ${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_INTFLAG = TC_INTFLAG_Msk;

<#if TC_INTSET_VAL != "">
    /* Enable Interrupt */
    ${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_INTENSET = ${TC_INTSET_VAL};
    ${TC_INSTANCE_NAME}_CallbackObject.callback = NULL;
</#if>
}


void ${TC_INSTANCE_NAME}_CaptureStart( void )
{
    /* Enable TC */
    ${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_CTRLA |= TC_CTRLA_ENABLE_Msk;

    while((${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_STATUS & TC_STATUS_SYNCBUSY_Msk))
    {
        /* Wait for Write Synchronization */
    }
}

void ${TC_INSTANCE_NAME}_CaptureStop( void )
{
    /* Disable TC */
    ${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_CTRLA &= ~TC_CTRLA_ENABLE_Msk;

    while((${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_STATUS & TC_STATUS_SYNCBUSY_Msk))
    {
        /* Wait for Write Synchronization */
    }
}

uint32_t ${TC_INSTANCE_NAME}_CaptureFrequencyGet( void )
{
    return (uint32_t)(${TC_FREQUENCY}UL);
}

<#if TC_CTRLA_MODE = "COUNT8">

uint8_t ${TC_INSTANCE_NAME}_Capture8bitChannel0Get( void )
{
    /* Write command to force CC register read synchronization */
    ${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_READREQ = TC_READREQ_RREQ_Msk | TC_${TC_CTRLA_MODE}_CC_REG_OFST;

    while((${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_STATUS & TC_STATUS_SYNCBUSY_Msk))
    {
        /* Wait for Write Synchronization */
    }
    return (uint8_t)${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_CC[0];
}

uint8_t ${TC_INSTANCE_NAME}_Capture8bitChannel1Get( void )
{
    /* Write command to force CC register read synchronization */
    ${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_READREQ = TC_READREQ_RREQ_Msk | TC_${TC_CTRLA_MODE}_CC_REG_OFST;

    while((${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_STATUS & TC_STATUS_SYNCBUSY_Msk))
    {
        /* Wait for Write Synchronization */
    }
    return (uint8_t)${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_CC[1];
}

<#elseif TC_CTRLA_MODE = "COUNT16">

uint16_t ${TC_INSTANCE_NAME}_Capture16bitChannel0Get( void )
{
    /* Write command to force CC register read synchronization */
    ${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_READREQ = TC_READREQ_RREQ_Msk | TC_${TC_CTRLA_MODE}_CC_REG_OFST;

    while((${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_STATUS & TC_STATUS_SYNCBUSY_Msk))
    {
        /* Wait for Write Synchronization */
    }
    return (uint16_t)${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_CC[0];
}

uint16_t ${TC_INSTANCE_NAME}_Capture16bitChannel1Get( void )
{
    /* Write command to force CC register read synchronization */
    ${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_READREQ = TC_READREQ_RREQ_Msk | TC_${TC_CTRLA_MODE}_CC_REG_OFST;

    while((${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_STATUS & TC_STATUS_SYNCBUSY_Msk))
    {
        /* Wait for Write Synchronization */
    }
    return (uint16_t)${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_CC[1];
}
<#elseif TC_CTRLA_MODE = "COUNT32">

uint32_t ${TC_INSTANCE_NAME}_Capture32bitChannel0Get( void )
{
    /* Write command to force CC register read synchronization */
    ${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_READREQ = TC_READREQ_RREQ_Msk | TC_${TC_CTRLA_MODE}_CC_REG_OFST;

    while((${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_STATUS & TC_STATUS_SYNCBUSY_Msk))
    {
        /* Wait for Write Synchronization */
    }
    return ${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_CC[0];
}

uint32_t ${TC_INSTANCE_NAME}_Capture32bitChannel1Get( void )
{
    /* Write command to force CC register read synchronization */
    ${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_READREQ = TC_READREQ_RREQ_Msk | TC_${TC_CTRLA_MODE}_CC_REG_OFST;

    while((${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_STATUS & TC_STATUS_SYNCBUSY_Msk))
    {
        /* Wait for Write Synchronization */
    }
    return ${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_CC[1];
}
</#if>

<#if TC_INTSET_VAL != "">
void ${TC_INSTANCE_NAME}_CaptureCallbackRegister( TC_CAPTURE_CALLBACK callback, uintptr_t context )
{
    ${TC_INSTANCE_NAME}_CallbackObject.callback = callback;
    ${TC_INSTANCE_NAME}_CallbackObject.context = context;
}

void ${TC_INSTANCE_NAME}_CaptureInterruptHandler( void )
{
    TC_CAPTURE_STATUS status;
    status = ${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_INTFLAG;
    /* Clear all interrupts */
    ${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_INTFLAG = TC_INTFLAG_Msk;

    if(${TC_INSTANCE_NAME}_CallbackObject.callback != NULL)
    {
        ${TC_INSTANCE_NAME}_CallbackObject.callback(status, ${TC_INSTANCE_NAME}_CallbackObject.context);
    }
}

<#else>

TC_CAPTURE_STATUS ${TC_INSTANCE_NAME}_CaptureStatusGet(void)
{
    TC_CAPTURE_STATUS capture_status;
    capture_status = (${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_INTFLAG) & TC_CAPTURE_STATUS_MSK;
    ${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_INTFLAG = capture_status;
    return capture_status;
}
</#if>
