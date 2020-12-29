/*******************************************************************************
  Timer/Counter(${TCC_INSTANCE_NAME}) PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_${TCC_INSTANCE_NAME}.c

  Summary
    ${TCC_INSTANCE_NAME} PLIB Implementation File.

  Description
    This file defines the interface to the TCC peripheral library. This
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
<#if core.CoreSysIntFile == true>
#include "interrupts.h"
</#if>
#include "plib_${TCC_INSTANCE_NAME?lower_case}.h"

// *****************************************************************************
// *****************************************************************************
// Section: Global Data
// *****************************************************************************
// *****************************************************************************
<#compress>

<#assign TCC_CTRLA_VAL = "">
<#assign TCC_INTENSET_VAL = "">
<#assign TCC_EVCTRL_VAL = "">

<#list 0..(TCC_NUM_CHANNELS-1) as i>
<#assign TCC_CTRLA_ENABLE = "TCC_CAPTURE_CTRLA_CAPTEN"+ i>
    <#if .vars[TCC_CTRLA_ENABLE] == true>
        <#if TCC_CTRLA_VAL != "">
            <#assign TCC_CTRLA_VAL = TCC_CTRLA_VAL + " | TCC_CTRLA_CPTEN" + i + "_Msk">
        <#else>
            <#assign TCC_CTRLA_VAL = "TCC_CTRLA_CPTEN" + i + "_Msk">
        </#if>
    </#if>        
</#list>
<#if TCC_SLAVE_MODE == true>
    <#if TCC_CTRLA_VAL != "">
        <#assign TCC_CTRLA_VAL = TCC_CTRLA_VAL + " | TCC_CTRLA_MSYNC_Msk">
    <#else>
        <#assign TCC_CTRLA_VAL = "TCC_CTRLA_MSYNC_Msk">
    </#if>
</#if>

<#-- Interrupt -->
<#if TCC_CAPTURE_OVF_INTERRUPT_MODE == true>
    <#if TCC_INTENSET_VAL != "">
        <#assign TCC_INTENSET_VAL = TCC_INTENSET_VAL + " | TCC_INTENSET_OVF_Msk">
    <#else>
        <#assign TCC_INTENSET_VAL = "TCC_INTENSET_OVF_Msk">
    </#if>
</#if>
<#if TCC_CAPTURE_ERR_INTERRUPT_MODE == true>
    <#if TCC_INTENSET_VAL != "">
        <#assign TCC_INTENSET_VAL = TCC_INTENSET_VAL + " | TCC_INTENSET_ERR_Msk">
    <#else>
        <#assign TCC_INTENSET_VAL = "TCC_INTENSET_ERR_Msk">
    </#if>
</#if>
<#list 0..(TCC_NUM_CHANNELS-1) as i>
<#assign TCC_INTENSET_MC = "TCC_CAPTURE_INTENSET_MC"+ i>
    <#if .vars[TCC_INTENSET_MC] == true>
        <#if TCC_INTENSET_VAL != "">
            <#assign TCC_INTENSET_VAL = TCC_INTENSET_VAL + " | TCC_INTENSET_MC"+i+"_Msk">
        <#else>
            <#assign TCC_INTENSET_VAL = "TCC_INTENSET_MC"+i+"_Msk">
        </#if>
    </#if>        
</#list>

<#-- Events -->
<#list 0..(TCC_NUM_CHANNELS-1) as i>
<#assign TCC_EVCTRL_MC = "TCC_CAPTURE_EVCTRL_MCEO"+ i>
    <#if .vars[TCC_EVCTRL_MC] == true>
        <#if TCC_EVCTRL_VAL != "">
            <#assign TCC_EVCTRL_VAL = TCC_EVCTRL_VAL + " | TCC_EVCTRL_MCEO"+i+"_Msk">
        <#else>
            <#assign TCC_EVCTRL_VAL = "TCC_EVCTRL_MCEO"+i+"_Msk">
        </#if>
    </#if>        
</#list>
<#if TCC_CAPTURE_EVCTRL_EVACT1 != "OFF">
    <#if TCC_EVCTRL_VAL != "">
        <#assign TCC_EVCTRL_VAL = TCC_EVCTRL_VAL + " | TCC_EVCTRL_TCEI1_Msk | TCC_EVCTRL_EVACT1_"+TCC_CAPTURE_EVCTRL_EVACT1>
    <#else>
        <#assign TCC_EVCTRL_VAL = "TCC_EVCTRL_TCEI1_Msk | TCC_EVCTRL_EVACT1_"+TCC_CAPTURE_EVCTRL_EVACT1>
    </#if>
    <#if TCC_CAPTURE_EVCTRL_TCINV1 == true>
        <#assign TCC_EVCTRL_VAL = TCC_EVCTRL_VAL + "| TCC_EVCTRL_TCINV1_Msk">
    </#if>
</#if>
<#list 0..(TCC_NUM_CHANNELS-1) as i>
<#assign TCC_CTRLA_ENABLE = "TCC_CAPTURE_CTRLA_CAPTEN"+ i>
    <#if .vars[TCC_CTRLA_ENABLE] == true>
        <#if TCC_EVCTRL_VAL != "">
            <#assign TCC_EVCTRL_VAL = TCC_EVCTRL_VAL + " | TCC_EVCTRL_MCEI" + i + "_Msk">
        <#else>
            <#assign TCC_EVCTRL_VAL = "TCC_EVCTRL_MCEI" + i + "_Msk">
        </#if>
    </#if>        
</#list>
</#compress>

<#if TCC_CAPTURE_INTERRUPT_MODE = true>
static TCC_CALLBACK_OBJECT ${TCC_INSTANCE_NAME}_CallbackObject;
</#if>
// *****************************************************************************
// *****************************************************************************
// Section: ${TCC_INSTANCE_NAME} Implementation
// *****************************************************************************
// *****************************************************************************

void ${TCC_INSTANCE_NAME}_CaptureInitialize( void )
{
    /* Reset TCC */
    ${TCC_INSTANCE_NAME}_REGS->TCC_CTRLA = TCC_CTRLA_SWRST_Msk;

    while((${TCC_INSTANCE_NAME}_REGS->TCC_SYNCBUSY & TCC_SYNCBUSY_SWRST_Msk) == TCC_SYNCBUSY_SWRST_Msk)
    {
        /* Wait for Write Synchronization */
    }

    /* Configure prescaler, standby & capture mode */
    <#if TCC_CTRLA_VAL?has_content>
    ${TCC_INSTANCE_NAME}_REGS->TCC_CTRLA = TCC_CTRLA_PRESCALER_${TCC_CTRLA_PRESCALER} | TCC_CTRLA_PRESCSYNC_PRESC
                                  | ${TCC_CTRLA_VAL}
                                  ${TCC_CTRLA_RUNSTDBY?then('| TCC_CTRLA_RUNSTDBY_Msk', '')};
    <#else>
    ${TCC_INSTANCE_NAME}_REGS->TCC_CTRLA = TCC_CTRLA_PRESCALER_${TCC_CTRLA_PRESCALER} | TCC_CTRLA_PRESCSYNC_PRESC
                                  ${TCC_CTRLA_RUNSTDBY?then('| TCC_CTRLA_RUNSTDBY_Msk', '')};
    </#if>                                      


    <#if TCC_EVCTRL_VAL?has_content>
    ${TCC_INSTANCE_NAME}_REGS->TCC_EVCTRL = ${TCC_EVCTRL_VAL};
    </#if>

    /* Clear all interrupt flags */
    ${TCC_INSTANCE_NAME}_REGS->TCC_INTFLAG = TCC_INTFLAG_Msk;

    <#if TCC_INTENSET_VAL?has_content>
    ${TCC_INSTANCE_NAME}_CallbackObject.callback_fn = NULL;
    ${TCC_INSTANCE_NAME}_REGS->TCC_INTENSET = ${TCC_INTENSET_VAL};
    </#if>
    while((${TCC_INSTANCE_NAME}_REGS->TCC_SYNCBUSY) != 0U)
    {
        /* Wait for Write Synchronization */
    }
}


void ${TCC_INSTANCE_NAME}_CaptureStart( void )
{
    /* Enable TCC */
    ${TCC_INSTANCE_NAME}_REGS->TCC_CTRLA |= TCC_CTRLA_ENABLE_Msk;

    while((${TCC_INSTANCE_NAME}_REGS->TCC_SYNCBUSY & TCC_SYNCBUSY_ENABLE_Msk) == TCC_SYNCBUSY_ENABLE_Msk)
    {
        /* Wait for Write Synchronization */
    }
}

void ${TCC_INSTANCE_NAME}_CaptureStop( void )
{
    /* Disable TCC */
    ${TCC_INSTANCE_NAME}_REGS->TCC_CTRLA &= ~TCC_CTRLA_ENABLE_Msk;

    while((${TCC_INSTANCE_NAME}_REGS->TCC_SYNCBUSY & TCC_SYNCBUSY_ENABLE_Msk) == TCC_SYNCBUSY_ENABLE_Msk)
    {
        /* Wait for Write Synchronization */
    }
}


void ${TCC_INSTANCE_NAME}_CaptureCommandSet(TCC_COMMAND command)
{
    ${TCC_INSTANCE_NAME}_REGS->TCC_CTRLBSET = (uint8_t)((uint32_t)command << TCC_CTRLBSET_CMD_Pos);
    while((${TCC_INSTANCE_NAME}_REGS->TCC_SYNCBUSY) != 0U)
    {
        /* Wait for Write Synchronization */
    }    
}

<#if TCC_SIZE = 16>

uint16_t ${TCC_INSTANCE_NAME}_Capture16bitValueGet( ${TCC_INSTANCE_NAME}_CHANNEL_NUM channel )
{
    return (uint16_t)${TCC_INSTANCE_NAME}_REGS->TCC_CC[channel];
}

<#elseif TCC_SIZE = 24>

uint32_t ${TCC_INSTANCE_NAME}_Capture24bitValueGet( ${TCC_INSTANCE_NAME}_CHANNEL_NUM channel )
{
    return (${TCC_INSTANCE_NAME}_REGS->TCC_CC[channel] & 0xFFFFFFU);
}

</#if>

uint32_t ${TCC_INSTANCE_NAME}_CaptureFrequencyGet( void )
{
    return (uint32_t)(${TCC_MODULE_FREQUENCY}U);
}

<#if TCC_SIZE = 16>
/* Get the current counter value */
uint16_t ${TCC_INSTANCE_NAME}_Capture16bitCounterGet( void )
{
    /* Write command to force COUNT register read synchronization */
    ${TCC_INSTANCE_NAME}_REGS->TCC_CTRLBSET |= (uint8_t)TCC_CTRLBSET_CMD_READSYNC;

    while((${TCC_INSTANCE_NAME}_REGS->TCC_SYNCBUSY & TCC_SYNCBUSY_CTRLB_Msk) == TCC_SYNCBUSY_CTRLB_Msk)
    {
        /* Wait for Write Synchronization */
    }

    while((${TCC_INSTANCE_NAME}_REGS->TCC_CTRLBSET & TCC_CTRLBSET_CMD_Msk) != 0U)
    {
        /* Wait for CMD to become zero */
    }

    /* Read current count value */
    return (uint16_t)${TCC_INSTANCE_NAME}_REGS->TCC_COUNT;
}

<#elseif TCC_SIZE == 24>
/* Get the current counter value */
uint32_t ${TCC_INSTANCE_NAME}_Capture24bitCounterGet( void )
{
    /* Write command to force COUNT register read synchronization */
    ${TCC_INSTANCE_NAME}_REGS->TCC_CTRLBSET |= (uint8_t)TCC_CTRLBSET_CMD_READSYNC;

    while((${TCC_INSTANCE_NAME}_REGS->TCC_SYNCBUSY & TCC_SYNCBUSY_CTRLB_Msk) == TCC_SYNCBUSY_CTRLB_Msk)
    {
        /* Wait for Write Synchronization */
    }

    while((${TCC_INSTANCE_NAME}_REGS->TCC_CTRLBSET & TCC_CTRLBSET_CMD_Msk) != 0U)
    {
        /* Wait for CMD to become zero */
    }

    /* Read current count value */
    return ${TCC_INSTANCE_NAME}_REGS->TCC_COUNT;
}
</#if>

<#if TCC_CAPTURE_INTERRUPT_MODE = true>
/* Register callback function */
void ${TCC_INSTANCE_NAME}_CaptureCallbackRegister( TCC_CALLBACK callback, uintptr_t context )
{
    ${TCC_INSTANCE_NAME}_CallbackObject.callback_fn = callback;

    ${TCC_INSTANCE_NAME}_CallbackObject.context = context;
}

<#-- Single interrupt line -->
<#if TCC_NUM_INT_LINES == 0>
/* Capture interrupt handler */
void ${TCC_INSTANCE_NAME}_InterruptHandler( void )
{
    uint32_t status;
    status = ${TCC_INSTANCE_NAME}_REGS->TCC_INTFLAG;
    /* clear period interrupt */
    ${TCC_INSTANCE_NAME}_REGS->TCC_INTFLAG = TCC_INTFLAG_Msk;
    if(${TCC_INSTANCE_NAME}_CallbackObject.callback_fn != NULL)
    {
        ${TCC_INSTANCE_NAME}_CallbackObject.callback_fn(status, ${TCC_INSTANCE_NAME}_CallbackObject.context);
    }
}

<#-- Multiple interrupt lines -->
<#else>
        <#if TCC_CAPTURE_OVF_INTERRUPT_MODE == true || TCC_CAPTURE_ERR_INTERRUPT_MODE == true>
            <#lt>/* Interrupt Handler */
            <#lt>void ${TCC_INSTANCE_NAME}_InterruptHandler(void)
            <#lt>{
            <#lt>    uint32_t status;
            <#lt>    status = (uint32_t)(${TCC_INSTANCE_NAME}_REGS->TCC_INTFLAG & 0xFFFFU);
            <#lt>    /* Clear interrupt flags */
            <#lt>    ${TCC_INSTANCE_NAME}_REGS->TCC_INTFLAG = 0xFFFFU;
            <#lt>    if (${TCC_INSTANCE_NAME}_CallbackObject.callback_fn != NULL)
            <#lt>    {
            <#lt>        ${TCC_INSTANCE_NAME}_CallbackObject.callback_fn(status, ${TCC_INSTANCE_NAME}_CallbackObject.context);
            <#lt>    }

            <#lt>}
        </#if>

        <#list 0..(TCC_NUM_CHANNELS-1) as i>
        <#assign TCC_INT_MC = "TCC_CAPTURE_INTENSET_MC" + i>
            <#if .vars[TCC_INT_MC] == true>
                <#lt>/* Interrupt Handler */
                <#lt>void ${TCC_INSTANCE_NAME}_MC${i}_InterruptHandler(void)
                <#lt>{
                <#lt>    uint32_t status;
                <#lt>    status = (uint32_t)TCC_INTFLAG_MC${i}_Msk;
                <#lt>    /* Clear interrupt flags */
                <#lt>    ${TCC_INSTANCE_NAME}_REGS->TCC_INTFLAG = TCC_INTFLAG_MC${i}_Msk;
                <#lt>    if (${TCC_INSTANCE_NAME}_CallbackObject.callback_fn != NULL)
                <#lt>    {
                <#lt>        ${TCC_INSTANCE_NAME}_CallbackObject.callback_fn(status, ${TCC_INSTANCE_NAME}_CallbackObject.context);
                <#lt>    }

                <#lt>}
            </#if>
        </#list>
</#if>  <#-- End of TCC_NUM_INT_LINES -->

<#-- Interrupt mode is disabled -->
<#else>

uint32_t ${TCC_INSTANCE_NAME}_CaptureStatusGet( void )
{
    uint32_t capture_status;
    capture_status = ((${TCC_INSTANCE_NAME}_REGS->TCC_INTFLAG));
    ${TCC_INSTANCE_NAME}_REGS->TCC_INTFLAG = capture_status;
    return capture_status;
}
</#if>


