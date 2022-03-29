/*******************************************************************************
  Timer/Counter(${TCC_INSTANCE_NAME}) PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_${TCC_INSTANCE_NAME?lower_case}.c

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

<#assign TCC_INTENSET_VAL = "">
<#assign TCC_EVCTRL_VAL = "">
<#if TCC_TIMER_INTENSET_OVF == true>
    <#if TCC_INTENSET_VAL != "">
        <#assign TCC_INTENSET_VAL = TCC_INTENSET_VAL + " | TCC_INTENSET_OVF_Msk">
    <#else>
        <#assign TCC_INTENSET_VAL = "TCC_INTENSET_OVF_Msk">
    </#if>
</#if>
<#if TCC_TIMER_INTENSET_MC1 == true>
    <#if TCC_INTENSET_VAL != "">
        <#assign TCC_INTENSET_VAL = TCC_INTENSET_VAL + " | TCC_INTENSET_MC1_Msk">
    <#else>
        <#assign TCC_INTENSET_VAL = "TCC_INTENSET_MC1_Msk">
    </#if>
</#if>
<#if TCC_TIMER_EVCTRL_OVFEO == true>
    <#if TCC_EVCTRL_VAL != "">
        <#assign TCC_EVCTRL_VAL = TCC_EVCTRL_VAL + " | TCC_EVCTRL_OVFEO_Msk">
    <#else>
        <#assign TCC_EVCTRL_VAL = "TCC_EVCTRL_OVFEO_Msk">
    </#if>
</#if>
<#if TCC_TIMER_EVCTRL_EVACT0 != "OFF">
    <#if TCC_EVCTRL_VAL != "">
        <#assign TCC_EVCTRL_VAL = TCC_EVCTRL_VAL + " | TCC_EVCTRL_TCEI0_Msk | TCC_EVCTRL_EVACT0_"+TCC_TIMER_EVCTRL_EVACT0>
    <#else>
        <#assign TCC_EVCTRL_VAL = "TCC_EVCTRL_TCEI0_Msk | TCC_EVCTRL_EVACT0_"+TCC_TIMER_EVCTRL_EVACT0>
    </#if>
    <#if TCC_TIMER_EVCTRL_TCINV0 == true>
    <#assign TCC_EVCTRL_VAL = TCC_EVCTRL_VAL + " | TCC_EVCTRL_TCINV0_Msk">
    </#if>
</#if>
<#if TCC_TIMER_EVCTRL_EVACT1 != "OFF">
    <#if TCC_EVCTRL_VAL != "">
        <#assign TCC_EVCTRL_VAL = TCC_EVCTRL_VAL + " | TCC_EVCTRL_TCEI1_Msk | TCC_EVCTRL_EVACT1_"+TCC_TIMER_EVCTRL_EVACT1>
    <#else>
        <#assign TCC_EVCTRL_VAL = "TCC_EVCTRL_TCEI1_Msk | TCC_EVCTRL_EVACT1_"+TCC_TIMER_EVCTRL_EVACT1>
    </#if>
    <#if TCC_TIMER_EVCTRL_TCINV1 == true>
    <#assign TCC_EVCTRL_VAL = TCC_EVCTRL_VAL + " | TCC_EVCTRL_TCINV1_Msk">
    </#if>
</#if>
// *****************************************************************************
// *****************************************************************************
// Section: Global Data
// *****************************************************************************
// *****************************************************************************

<#if TCC_TIMER_INTENSET_OVF = true || TCC_TIMER_INTENSET_MC1 == true>
static TCC_CALLBACK_OBJECT ${TCC_INSTANCE_NAME}_CallbackObject;
</#if>

// *****************************************************************************
// *****************************************************************************
// Section: ${TCC_INSTANCE_NAME} Implementation
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Initialize the TCC module in Timer mode */
void ${TCC_INSTANCE_NAME}_TimerInitialize( void )
{
    /* Reset TCC */
    ${TCC_INSTANCE_NAME}_REGS->TCC_CTRLA = TCC_CTRLA_SWRST_Msk;

    while((${TCC_INSTANCE_NAME}_REGS->TCC_SYNCBUSY & TCC_SYNCBUSY_SWRST_Msk) == TCC_SYNCBUSY_SWRST_Msk)
    {
        /* Wait for Write Synchronization */
    }

<#if TCC_SLAVE_MODE == true>
    /* Configure counter mode & prescaler */
    <@compress single_line=true>${TCC_INSTANCE_NAME}_REGS->TCC_CTRLA = TCC_CTRLA_PRESCALER_${TCC_CTRLA_PRESCALER}
                                | TCC_CTRLA_MSYNC_Msk ${TCC_CTRLA_RUNSTDBY?then('| TCC_CTRLA_RUNSTDBY_Msk', '')};</@compress>
<#else>
    /* Configure counter mode & prescaler */
    <@compress single_line=true>${TCC_INSTANCE_NAME}_REGS->TCC_CTRLA = TCC_CTRLA_PRESCALER_${TCC_CTRLA_PRESCALER}
                                ${TCC_CTRLA_RUNSTDBY?then('| TCC_CTRLA_RUNSTDBY_Msk', '')};</@compress>
</#if>
    /* Configure in Match Frequency Mode */
    ${TCC_INSTANCE_NAME}_REGS->TCC_WAVE = TCC_WAVE_WAVEGEN_NPWM;

<#if TCC_TIMER_CTRLBSET_ONESHOT == true>
    /* Configure timer one shot mode */
    ${TCC_INSTANCE_NAME}_REGS->TCC_CTRLBSET = (uint8_t)TCC_CTRLBSET_ONESHOT_Msk;
</#if>
    /* Configure timer period */
    ${TCC_INSTANCE_NAME}_REGS->TCC_PER = ${TCC_TIMER_PERIOD}U;

    /* Clear all interrupt flags */
    ${TCC_INSTANCE_NAME}_REGS->TCC_INTFLAG = TCC_INTFLAG_Msk;

<#if TCC_TIMER_INTENSET_OVF = true || TCC_TIMER_INTENSET_MC1 == true>
    ${TCC_INSTANCE_NAME}_CallbackObject.callback_fn = NULL;
    /* Enable interrupt*/
    <#if TCC_INTENSET_VAL?has_content>
    ${TCC_INSTANCE_NAME}_REGS->TCC_INTENSET = (${TCC_INTENSET_VAL});
    </#if>
</#if>

<#if TCC_EVCTRL_VAL?has_content>
    ${TCC_INSTANCE_NAME}_REGS->TCC_EVCTRL = (${TCC_EVCTRL_VAL});
</#if>

    while((${TCC_INSTANCE_NAME}_REGS->TCC_SYNCBUSY) != 0U)
    {
        /* Wait for Write Synchronization */
    }
}

/* Enable the TCC counter */
void ${TCC_INSTANCE_NAME}_TimerStart( void )
{
<#if TCC_TIMER_CTRLBSET_ONESHOT == true>
    /* In one-shot timer mode, first disable the timer */
    ${TCC_INSTANCE_NAME}_REGS->TCC_CTRLA &= ~TCC_CTRLA_ENABLE_Msk;
    while((${TCC_INSTANCE_NAME}_REGS->TCC_SYNCBUSY & TCC_SYNCBUSY_ENABLE_Msk) == TCC_SYNCBUSY_ENABLE_Msk)
    {
        /* Wait for Write Synchronization */
    }
</#if>
    ${TCC_INSTANCE_NAME}_REGS->TCC_CTRLA |= TCC_CTRLA_ENABLE_Msk;
    while((${TCC_INSTANCE_NAME}_REGS->TCC_SYNCBUSY & TCC_SYNCBUSY_ENABLE_Msk) == TCC_SYNCBUSY_ENABLE_Msk)
    {
        /* Wait for Write Synchronization */
    }
}

/* Disable the TCC counter */
void ${TCC_INSTANCE_NAME}_TimerStop( void )
{
    ${TCC_INSTANCE_NAME}_REGS->TCC_CTRLA &= ~TCC_CTRLA_ENABLE_Msk;
    while((${TCC_INSTANCE_NAME}_REGS->TCC_SYNCBUSY & TCC_SYNCBUSY_ENABLE_Msk) == TCC_SYNCBUSY_ENABLE_Msk)
    {
        /* Wait for Write Synchronization */
    }
}

uint32_t ${TCC_INSTANCE_NAME}_TimerFrequencyGet( void )
{
    return (uint32_t)(${TCC_MODULE_FREQUENCY}U);
}

void ${TCC_INSTANCE_NAME}_TimerCommandSet(TCC_COMMAND command)
{
    ${TCC_INSTANCE_NAME}_REGS->TCC_CTRLBSET = (uint8_t)((uint32_t)command << TCC_CTRLBSET_CMD_Pos);
    while((${TCC_INSTANCE_NAME}_REGS->TCC_SYNCBUSY) != 0U)
    {
        /* Wait for Write Synchronization */
    }    
}

<#if TCC_SIZE = 16>
/* Get the current timer counter value */
uint16_t ${TCC_INSTANCE_NAME}_Timer16bitCounterGet( void )
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

/* Configure timer counter value */
void ${TCC_INSTANCE_NAME}_Timer16bitCounterSet( uint16_t count )
{
    ${TCC_INSTANCE_NAME}_REGS->TCC_COUNT = count;

    while((${TCC_INSTANCE_NAME}_REGS->TCC_SYNCBUSY & TCC_SYNCBUSY_COUNT_Msk) == TCC_SYNCBUSY_COUNT_Msk)
    {
        /* Wait for Write Synchronization */
    }
}

/* Configure timer period */
void ${TCC_INSTANCE_NAME}_Timer16bitPeriodSet( uint16_t period )
{
    ${TCC_INSTANCE_NAME}_REGS->TCC_PER = period;
    while((${TCC_INSTANCE_NAME}_REGS->TCC_SYNCBUSY & TCC_SYNCBUSY_PER_Msk) == TCC_SYNCBUSY_PER_Msk)
    {
        /* Wait for Write Synchronization */
    }
}

/* Read the timer period value */
uint16_t ${TCC_INSTANCE_NAME}_Timer16bitPeriodGet( void )
{
    return (uint16_t)${TCC_INSTANCE_NAME}_REGS->TCC_PER;
}

<#if TCC_SYS_TIME_CONNECTED == true>
void ${TCC_INSTANCE_NAME}_Timer16bitCompareSet( uint16_t compare )
{
    ${TCC_INSTANCE_NAME}_REGS->TCC_CC[1] = compare;
    while((${TCC_INSTANCE_NAME}_REGS->TCC_SYNCBUSY & TCC_SYNCBUSY_CC1_Msk) == TCC_SYNCBUSY_CC1_Msk)
    {
        /* Wait for Write Synchronization */
    }
}
</#if>

<#elseif TCC_SIZE = 24>
/* Get the current timer counter value */
uint32_t ${TCC_INSTANCE_NAME}_Timer24bitCounterGet( void )
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

/* Configure timer counter value */
void ${TCC_INSTANCE_NAME}_Timer24bitCounterSet( uint32_t count )
{
    ${TCC_INSTANCE_NAME}_REGS->TCC_COUNT = count & 0xFFFFFFU;

    while((${TCC_INSTANCE_NAME}_REGS->TCC_SYNCBUSY & TCC_SYNCBUSY_COUNT_Msk) == TCC_SYNCBUSY_COUNT_Msk)
    {
        /* Wait for Write Synchronization */
    }
}

/* Configure timer period */
void ${TCC_INSTANCE_NAME}_Timer24bitPeriodSet( uint32_t period )
{
    ${TCC_INSTANCE_NAME}_REGS->TCC_PER = period & 0xFFFFFFU;
    while((${TCC_INSTANCE_NAME}_REGS->TCC_SYNCBUSY & TCC_SYNCBUSY_PER_Msk) == TCC_SYNCBUSY_PER_Msk)
    {
        /* Wait for Write Synchronization */
    }
}

/* Read the timer period value */
uint32_t ${TCC_INSTANCE_NAME}_Timer24bitPeriodGet( void )
{
    return ${TCC_INSTANCE_NAME}_REGS->TCC_PER;
}

<#if TCC_SYS_TIME_CONNECTED == true>
void ${TCC_INSTANCE_NAME}_Timer24bitCompareSet( uint32_t compare )
{
    ${TCC_INSTANCE_NAME}_REGS->TCC_CC[1] = compare & 0xFFFFFFU;
    while((${TCC_INSTANCE_NAME}_REGS->TCC_SYNCBUSY & TCC_SYNCBUSY_CC1_Msk) == TCC_SYNCBUSY_CC1_Msk)
    {
        /* Wait for Write Synchronization */
    }
}
</#if>

</#if>

<#if TCC_TIMER_INTENSET_OVF == true || TCC_TIMER_INTENSET_MC1 == true>
/* Register callback function */
void ${TCC_INSTANCE_NAME}_TimerCallbackRegister( TCC_CALLBACK callback, uintptr_t context )
{
    ${TCC_INSTANCE_NAME}_CallbackObject.callback_fn = callback;

    ${TCC_INSTANCE_NAME}_CallbackObject.context = context;
}

<#-- Single interrupt line -->
<#if TCC_NUM_INT_LINES == 0>
/* Timer Interrupt handler */
void ${TCC_INSTANCE_NAME}_InterruptHandler( void )
{
    uint32_t status;
    status = ${TCC_INSTANCE_NAME}_REGS->TCC_INTFLAG;
    /* Clear interrupt flags */
    ${TCC_INSTANCE_NAME}_REGS->TCC_INTFLAG = TCC_INTFLAG_Msk;
    (void)${TCC_INSTANCE_NAME}_REGS->TCC_INTFLAG;
    if( ${TCC_INSTANCE_NAME}_CallbackObject.callback_fn != NULL)
    {
        ${TCC_INSTANCE_NAME}_CallbackObject.callback_fn(status, ${TCC_INSTANCE_NAME}_CallbackObject.context);
    }

}
<#-- multiple interrupt lines -->
<#else>
<#if TCC_TIMER_INTENSET_OVF == true>
void ${TCC_INSTANCE_NAME}_OTHER_InterruptHandler( void )
{
    uint32_t status;
    status = (${TCC_INSTANCE_NAME}_REGS->TCC_INTFLAG & 0xFFFFU);
    /* Clear interrupt flags */
    ${TCC_INSTANCE_NAME}_REGS->TCC_INTFLAG = 0xFFFFU;
    (void)${TCC_INSTANCE_NAME}_REGS->TCC_INTFLAG;
    if( ${TCC_INSTANCE_NAME}_CallbackObject.callback_fn != NULL)
    {
        ${TCC_INSTANCE_NAME}_CallbackObject.callback_fn(status, ${TCC_INSTANCE_NAME}_CallbackObject.context);
    }
}
</#if>

<#if TCC_TIMER_INTENSET_MC1 == true>
        <#lt>void ${TCC_INSTANCE_NAME}_MC1_InterruptHandler(void)
        <#lt>{
        <#lt>    uint32_t status;
        <#lt>    status = TCC_INTFLAG_MC1_Msk;
        <#lt>    /* Clear interrupt flags */
        <#lt>    ${TCC_INSTANCE_NAME}_REGS->TCC_INTFLAG = TCC_INTFLAG_MC1_Msk;
        <#lt>    (void)${TCC_INSTANCE_NAME}_REGS->TCC_INTFLAG;
        <#lt>    if (${TCC_INSTANCE_NAME}_CallbackObj.callback_fn != NULL)
        <#lt>    {
        <#lt>        ${TCC_INSTANCE_NAME}_CallbackObj.callback_fn(status, ${TCC_INSTANCE_NAME}_CallbackObj.context);
        <#lt>    }
</#if>
</#if>  <#-- TCC_NUM_INT_LINES -->
</#if>


<#if TCC_TIMER_INTENSET_OVF == false>
/* Polling method to check if timer period interrupt flag is set */
bool ${TCC_INSTANCE_NAME}_TimerPeriodHasExpired( void )
{
    uint8_t timer_status = 0U;
    timer_status = (uint8_t)((${TCC_INSTANCE_NAME}_REGS->TCC_INTFLAG) & TCC_INTFLAG_OVF_Msk);
    ${TCC_INSTANCE_NAME}_REGS->TCC_INTFLAG = timer_status;
    return (timer_status != 0U);
}
</#if>
