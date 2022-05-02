/*******************************************************************************
  Generic Timer PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_generic_timer.c

  Summary
    Source for Generic Timer peripheral library interface Implementation.

  Description
    This file defines the interface to the Generic Timer peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

  Remarks:
    None.

*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
* Copyright (C) 2021 Microchip Technology Inc. and its subsidiaries.
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

#include <stddef.h>
#include "device.h"
#include "plib_generic_timer.h"

#define GENERIC_TIMER_FREQUENCY ${SYSTEM_COUNTER_FREQUENCY}U
<#if GENERIC_TIMER_INTERRUPT>

static uint64_t compareDelta = ${GENERIC_TIMER_COMPARE_DELTA}UL;
<#if RTOS_INTERRUPT_HANDLER == "">

static struct callbackObject
{
    GENERIC_TIMER_CALLBACK pCallback;
    uintptr_t context;
}genericTimerCallbackObj;
</#if>
</#if>


void GENERIC_TIMER_Initialize(void)
{
    PL1_SetCounterFrequency(GENERIC_TIMER_FREQUENCY);
}


uint64_t GENERIC_TIMER_CounterValueGet(void)
{
    return PL1_GetCurrentPhysicalValue();
}


uint32_t GENERIC_TIMER_CounterFrequencyGet(void)
{
    return GENERIC_TIMER_FREQUENCY;
}


void GENERIC_TIMER_DelayUs(uint32_t delay_us)
{
    /* System counter is not expected to roll-over between two resets */
    uint64_t finalCount = GENERIC_TIMER_CounterValueGet() +
      (uint64_t)((GENERIC_TIMER_FREQUENCY /1000000UL) * (uint64_t)delay_us);
    while(GENERIC_TIMER_CounterValueGet() < finalCount)
	{
		
	}
}


void GENERIC_TIMER_DelayMs(uint32_t delay_ms)
{
    /* System counter is not expected to roll-over between two resets */
    uint64_t finalCount = GENERIC_TIMER_CounterValueGet() +
      (uint64_t)((GENERIC_TIMER_FREQUENCY /1000UL) * (uint64_t)delay_ms);
    while(GENERIC_TIMER_CounterValueGet() < finalCount)
	{
		
	}
}
<#if GENERIC_TIMER_INTERRUPT>

void GENERIC_TIMER_Start(void)
{
    uint64_t currentValue = PL1_GetCurrentPhysicalValue();
    PL1_SetPhysicalCompareValue(currentValue + compareDelta);
    PL1_SetControl(1U);
}


void GENERIC_TIMER_PeriodSet(uint64_t period)
{
    uint32_t control = PL1_GetControl();
    /* Mask Interrupt before updating delta */
    PL1_SetControl(control & 0x5U);
    compareDelta = period;
    PL1_SetControl(control);
}


uint64_t GENERIC_TIMER_PeriodGet(void)
{
    return compareDelta;
}


void GENERIC_TIMER_Stop(void)
{
    PL1_SetControl(2U);
}
<#if RTOS_INTERRUPT_HANDLER == "">


void GENERIC_TIMER_CallbackRegister(GENERIC_TIMER_CALLBACK pCallback, uintptr_t context)
{
    genericTimerCallbackObj.pCallback = pCallback;
    genericTimerCallbackObj.context = context;
}


void GENERIC_TIMER_InterruptHandler (void)
{
    uint64_t currentCompVal = PL1_GetPhysicalCompareValue();
    PL1_SetPhysicalCompareValue(currentCompVal + compareDelta);
    if(genericTimerCallbackObj.pCallback != NULL)
    {
        genericTimerCallbackObj.pCallback(genericTimerCallbackObj.context);
    }
}
</#if>
</#if> 