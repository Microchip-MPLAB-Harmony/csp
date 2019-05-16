/*******************************************************************************
  Timer/Counter(${TC_INSTANCE_NAME}) PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_${TC_INSTANCE_NAME?lower_case}.c

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

<#assign TC_INTENSET_VAL = "">
<#assign TC_EVCTRL_VAL = "">
<#if TC_TIMER_INTENSET_OVF == true>
    <#if TC_INTENSET_VAL != "">
        <#assign TC_INTENSET_VAL = TC_INTENSET_VAL + " | TC_INTENSET_OVF_Msk">
    <#else>
        <#assign TC_INTENSET_VAL = "TC_INTENSET_OVF_Msk">
    </#if>
</#if>
<#if TC_TIMER_INTENSET_MC1 == true>
    <#if TC_INTENSET_VAL != "">
        <#assign TC_INTENSET_VAL = TC_INTENSET_VAL + " | TC_INTENSET_MC1_Msk">
    <#else>
        <#assign TC_INTENSET_VAL = "TC_INTENSET_MC1_Msk">
    </#if>
</#if>
<#if TC_TIMER_EVCTRL_OVFEO == true>
    <#if TC_EVCTRL_VAL != "">
        <#assign TC_EVCTRL_VAL = TC_EVCTRL_VAL + " | TC_EVCTRL_OVFEO_Msk">
    <#else>
        <#assign TC_EVCTRL_VAL = "TC_EVCTRL_OVFEO_Msk">
    </#if>
</#if>
<#if TC_TIMER_EVCTRL_EV == true>
    <#if TC_EVCTRL_VAL != "">
        <#assign TC_EVCTRL_VAL = TC_EVCTRL_VAL + " | TC_EVCTRL_TCEI_Msk | TC_EVCTRL_EVACT_"+TC_TIMER_EVCTRL_EVACT>
    <#else>
        <#assign TC_EVCTRL_VAL = "TC_EVCTRL_TCEI_Msk | TC_EVCTRL_EVACT_"+TC_TIMER_EVCTRL_EVACT>
    </#if>
</#if>
// *****************************************************************************
// *****************************************************************************
// Section: Global Data
// *****************************************************************************
// *****************************************************************************

<#if TC_TIMER_INTENSET_OVF = true || TC_TIMER_INTENSET_MC1 == true>
TC_TIMER_CALLBACK_OBJ ${TC_INSTANCE_NAME}_CallbackObject;
</#if>

// *****************************************************************************
// *****************************************************************************
// Section: ${TC_INSTANCE_NAME} Implementation
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Initialize the TC module in Timer mode */
void ${TC_INSTANCE_NAME}_TimerInitialize( void )
{
    /* Reset TC */
    ${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_CTRLA = TC_CTRLA_SWRST_Msk;

    while((${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_SYNCBUSY & TC_SYNCBUSY_SWRST_Msk) == TC_SYNCBUSY_SWRST_Msk)
    {
        /* Wait for Write Synchronization */
    }

    /* Configure counter mode & prescaler */
    <@compress single_line=true>${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_CTRLA = TC_CTRLA_MODE_${TC_CTRLA_MODE}
                                | TC_CTRLA_PRESCALER_${TC_CTRLA_PRESCALER}
                                | TC_CTRLA_PRESCSYNC_PRESC
                                ${TC_CTRLA_RUNSTDBY?then('| TC_CTRLA_RUNSTDBY_Msk', '')}
                                ${TC_CTRLA_ONDEMAND?then('| TC_CTRLA_ONDEMAND_Msk', '')};</@compress>

    /* Configure in Match Frequency Mode */
    ${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_WAVE = TC_WAVE_WAVEGEN_MPWM;

<#if TC_TIMER_CTRLBSET_ONESHOT == true>
    /* Configure timer one shot mode */
    ${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_CTRLBSET = TC_CTRLBSET_ONESHOT_Msk;
</#if>
    /* Configure timer period */
    ${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_CC[0U] = ${TC_TIMER_PERIOD}U;

    /* Clear all interrupt flags */
    ${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_INTFLAG = TC_INTFLAG_Msk;

<#if TC_TIMER_INTENSET_OVF = true || TC_TIMER_INTENSET_MC1 == true>
    ${TC_INSTANCE_NAME}_CallbackObject.callback = NULL;
    /* Enable interrupt*/
    <#if TC_INTENSET_VAL?has_content>
    ${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_INTENSET = ${TC_INTENSET_VAL};
    </#if>
</#if>

<#if TC_EVCTRL_VAL?has_content>
    ${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_EVCTRL = ${TC_EVCTRL_VAL};
</#if>

    while((${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_SYNCBUSY))
    {
        /* Wait for Write Synchronization */
    }
}

/* Enable the TC counter */
void ${TC_INSTANCE_NAME}_TimerStart( void )
{
<#if TC_TIMER_CTRLBSET_ONESHOT == true>
    /* In one-shot timer mode, first disable the timer */
    ${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_CTRLA &= ~TC_CTRLA_ENABLE_Msk;
    while((${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_SYNCBUSY & TC_SYNCBUSY_ENABLE_Msk) == TC_SYNCBUSY_ENABLE_Msk)
    {
        /* Wait for Write Synchronization */
    }
</#if>
    ${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_CTRLA |= TC_CTRLA_ENABLE_Msk;
    while((${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_SYNCBUSY & TC_SYNCBUSY_ENABLE_Msk) == TC_SYNCBUSY_ENABLE_Msk)
    {
        /* Wait for Write Synchronization */
    }
}

/* Disable the TC counter */
void ${TC_INSTANCE_NAME}_TimerStop( void )
{
    ${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_CTRLA &= ~TC_CTRLA_ENABLE_Msk;
    while((${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_SYNCBUSY & TC_SYNCBUSY_ENABLE_Msk) == TC_SYNCBUSY_ENABLE_Msk)
    {
        /* Wait for Write Synchronization */
    }
}

uint32_t ${TC_INSTANCE_NAME}_TimerFrequencyGet( void )
{
    return (uint32_t)(${TC_FREQUENCY}UL);
}

<#if TC_CTRLA_MODE = "COUNT8">
/* Get the current timer counter value */
uint8_t ${TC_INSTANCE_NAME}_Timer8bitCounterGet( void )
{
    /* Write command to force COUNT register read synchronization */
    ${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_CTRLBSET |= TC_CTRLBSET_CMD_READSYNC;

    while((${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_SYNCBUSY & TC_SYNCBUSY_CTRLB_Msk) == TC_SYNCBUSY_CTRLB_Msk)
    {
        /* Wait for Write Synchronization */
    }

    /* Read current count value */
    return (uint8_t)${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_COUNT;
}

/* Configure timer counter value */
void ${TC_INSTANCE_NAME}_Timer8bitCounterSet( uint8_t count )
{
    ${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_COUNT = count;

    while((${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_SYNCBUSY & TC_SYNCBUSY_COUNT_Msk) == TC_SYNCBUSY_COUNT_Msk)
    {
        /* Wait for Write Synchronization */
    }
}

/* Configure timer period */
void ${TC_INSTANCE_NAME}_Timer8bitPeriodSet( uint8_t period )
{
    ${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_CC[0] = period;
    while((${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_SYNCBUSY & TC_SYNCBUSY_CC0_Msk) == TC_SYNCBUSY_CC0_Msk)
    {
        /* Wait for Write Synchronization */
    }
}

/* Read the timer period value */
uint8_t ${TC_INSTANCE_NAME}_Timer8bitPeriodGet( void )
{
    return (uint8_t)${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_CC[0];
}

<#if TC_SYS_TIME_CONNECTED == true>
void ${TC_INSTANCE_NAME}_Timer8bitCompareSet( uint8_t compare )
{
    ${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_CC[1] = compare;
    while((${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_SYNCBUSY & TC_SYNCBUSY_CC1_Msk) == TC_SYNCBUSY_CC1_Msk)
    {
        /* Wait for Write Synchronization */
    }
}
</#if>

<#elseif TC_CTRLA_MODE = "COUNT16">
/* Get the current timer counter value */
uint16_t ${TC_INSTANCE_NAME}_Timer16bitCounterGet( void )
{
    /* Write command to force COUNT register read synchronization */
    ${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_CTRLBSET |= TC_CTRLBSET_CMD_READSYNC;

    while((${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_SYNCBUSY & TC_SYNCBUSY_CTRLB_Msk) == TC_SYNCBUSY_CTRLB_Msk)
    {
        /* Wait for Write Synchronization */
    }

    /* Read current count value */
    return (uint16_t)${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_COUNT;
}

/* Configure timer counter value */
void ${TC_INSTANCE_NAME}_Timer16bitCounterSet( uint16_t count )
{
    ${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_COUNT = count;

    while((${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_SYNCBUSY & TC_SYNCBUSY_COUNT_Msk) == TC_SYNCBUSY_COUNT_Msk)
    {
        /* Wait for Write Synchronization */
    }
}

/* Configure timer period */
void ${TC_INSTANCE_NAME}_Timer16bitPeriodSet( uint16_t period )
{
    ${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_CC[0] = period;
    while((${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_SYNCBUSY & TC_SYNCBUSY_CC0_Msk) == TC_SYNCBUSY_CC0_Msk)
    {
        /* Wait for Write Synchronization */
    }
}

/* Read the timer period value */
uint16_t ${TC_INSTANCE_NAME}_Timer16bitPeriodGet( void )
{
    return (uint16_t)${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_CC[0];
}

<#if TC_SYS_TIME_CONNECTED == true>
void ${TC_INSTANCE_NAME}_Timer16bitCompareSet( uint16_t compare )
{
    ${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_CC[1] = compare;
    while((${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_SYNCBUSY & TC_SYNCBUSY_CC1_Msk) == TC_SYNCBUSY_CC1_Msk)
    {
        /* Wait for Write Synchronization */
    }
}
</#if>

<#elseif TC_CTRLA_MODE = "COUNT32">
/* Get the current timer counter value */
uint32_t ${TC_INSTANCE_NAME}_Timer32bitCounterGet( void )
{
    /* Write command to force COUNT register read synchronization */
    ${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_CTRLBSET |= TC_CTRLBSET_CMD_READSYNC;

    while((${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_SYNCBUSY & TC_SYNCBUSY_CTRLB_Msk) == TC_SYNCBUSY_CTRLB_Msk)
    {
        /* Wait for Write Synchronization */
    }

    /* Read current count value */
    return ${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_COUNT;

}

/* Configure timer counter value */
void ${TC_INSTANCE_NAME}_Timer32bitCounterSet( uint32_t count )
{
    ${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_COUNT = count;

    while((${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_SYNCBUSY & TC_SYNCBUSY_COUNT_Msk) == TC_SYNCBUSY_COUNT_Msk)
    {
        /* Wait for Write Synchronization */
    }
}

/* Configure timer period */
void ${TC_INSTANCE_NAME}_Timer32bitPeriodSet( uint32_t period )
{
    ${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_CC[0] = period;
    while((${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_SYNCBUSY & TC_SYNCBUSY_COUNT_Msk) == TC_SYNCBUSY_COUNT_Msk)
    {
        /* Wait for Write Synchronization */
    }
}

/* Read the timer period value */
uint32_t ${TC_INSTANCE_NAME}_Timer32bitPeriodGet( void )
{
    return ${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_CC[0];
}

<#if TC_SYS_TIME_CONNECTED == true>
void ${TC_INSTANCE_NAME}_Timer32bitCompareSet( uint32_t compare )
{
    ${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_CC[1] = compare;
    while((${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_SYNCBUSY & TC_SYNCBUSY_CC1_Msk) == TC_SYNCBUSY_CC1_Msk)
    {
        /* Wait for Write Synchronization */
    }
}
</#if>

</#if>

<#if TC_TIMER_INTENSET_OVF = true || TC_TIMER_INTENSET_MC1 == true>
/* Register callback function */
void ${TC_INSTANCE_NAME}_TimerCallbackRegister( TC_TIMER_CALLBACK callback, uintptr_t context )
{
    ${TC_INSTANCE_NAME}_CallbackObject.callback = callback;

    ${TC_INSTANCE_NAME}_CallbackObject.context = context;
}

/* Timer Interrupt handler */
void ${TC_INSTANCE_NAME}_TimerInterruptHandler( void )
{
    if (${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_INTENSET != 0)
    {
        TC_TIMER_STATUS status;
        status = ${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_INTFLAG;
        /* Clear interrupt flags */
        ${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_INTFLAG = TC_INTFLAG_Msk;
        if((status != TC_TIMER_STATUS_NONE) && ${TC_INSTANCE_NAME}_CallbackObject.callback != NULL)
        {
            ${TC_INSTANCE_NAME}_CallbackObject.callback(status, ${TC_INSTANCE_NAME}_CallbackObject.context);
        }
    }
}

<#else>
/* Polling method to check if timer period interrupt flag is set */
bool ${TC_INSTANCE_NAME}_TimerPeriodHasExpired( void )
{
    bool timer_status;
    timer_status = ((${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_INTFLAG) & TC_INTFLAG_OVF_Msk);
    ${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_INTFLAG = timer_status;
    return timer_status;
}
</#if>
