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
<#if CoreSysIntFile == true>
#include "interrupts.h"
</#if>

#define GENERIC_TIMER_FREQUENCY ${SYSTEM_COUNTER_FREQUENCY}U

<#if GENERIC_TIMER_INTERRUPT>
volatile static uint64_t compareDelta = ${GENERIC_TIMER_COMPARE_DELTA}UL;

<#if RTOS_INTERRUPT_HANDLER == "">

#define GENERIC_TIMER_INTERRUPT_PERIOD_IN_US  (${(GENERIC_TIMER_PERIOD_US != 0)?then(GENERIC_TIMER_PERIOD_US, "1")}U)

volatile static struct callbackObject
{
    GENERIC_TIMER_CALLBACK  pCallback;
    uintptr_t               context;
    volatile uint32_t       tickCounter;
}genericTimerObj;
</#if>

</#if>

void GENERIC_TIMER_Initialize(void)
{
    PL1_SetCounterFrequency(GENERIC_TIMER_FREQUENCY);
    <#if GENERIC_TIMER_AUTOSTART == true>
    GENERIC_TIMER_Start();
    </#if>
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

uint32_t GENERIC_TIMER_GetTickCounter(void)
{
    return genericTimerObj.tickCounter;
}

void GENERIC_TIMER_StartTimeOut (GENERIC_TIMER_TIMEOUT* timeout, uint32_t delay_ms)
{
    timeout->start = GENERIC_TIMER_GetTickCounter();
    timeout->count = (delay_ms*1000U)/GENERIC_TIMER_INTERRUPT_PERIOD_IN_US;
}

void GENERIC_TIMER_ResetTimeOut (GENERIC_TIMER_TIMEOUT* timeout)
{
    timeout->start = GENERIC_TIMER_GetTickCounter();
}

bool GENERIC_TIMER_IsTimeoutReached (GENERIC_TIMER_TIMEOUT* timeout)
{
    bool valTimeout  = true;
    if ((GENERIC_TIMER_GetTickCounter() - timeout->start) < timeout->count)
    {
        valTimeout = false;
    }

    return valTimeout;
}

void GENERIC_TIMER_CallbackRegister(GENERIC_TIMER_CALLBACK pCallback, uintptr_t context)
{
    genericTimerObj.pCallback = pCallback;
    genericTimerObj.context = context;
}


void __attribute__((used)) GENERIC_TIMER_InterruptHandler (void)
{
    uint64_t currentCompVal = PL1_GetPhysicalCompareValue();
    /* Additional temporary variable used to prevent MISRA violations (Rule 13.x) */
    uintptr_t context = genericTimerObj.context;
    PL1_SetPhysicalCompareValue(currentCompVal + compareDelta);
    genericTimerObj.tickCounter++;
    if(genericTimerObj.pCallback != NULL)
    {
        genericTimerObj.pCallback(context);
    }
}
</#if>
</#if>