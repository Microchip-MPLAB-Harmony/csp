/*******************************************************************************
  Periodic Interval Timer (${PIT64B_INSTANCE_NAME})

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${PIT64B_INSTANCE_NAME?lower_case}.h

  Summary:
    Periodic Interval Timer (${PIT64B_INSTANCE_NAME}) PLIB.

  Description:
    This file declares the interface for the Periodic Interval Timer (${PIT64B_INSTANCE_NAME}).
*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
* Copyright (C) 2019 Microchip Technology Inc. and its subsidiaries.
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
#include "plib_${PIT64B_INSTANCE_NAME?lower_case}.h"
<#if core.CoreSysIntFile == true>
#include "interrupts.h"
</#if>

#define ${PIT64B_INSTANCE_NAME}_COUNTER_FREQUENCY (${SRC_FREQ}U / ${PRESCALER + 1}U)

typedef struct
{
    bool running;
    uint32_t periodLSB;
    uint32_t periodMSB;
<#if ENABLE_INTERRUPT == true>
    ${PIT64B_INSTANCE_NAME}_CALLBACK callback;
    uintptr_t context;
</#if>
} ${PIT64B_INSTANCE_NAME}_OBJECT;


static ${PIT64B_INSTANCE_NAME}_OBJECT ${PIT64B_INSTANCE_NAME?lower_case} = 
{
    false,
    ${PERIOD_LSB}U,
    ${PERIOD_MSB}U,
<#if ENABLE_INTERRUPT == true>
    NULL,
    0U
</#if>
};


static inline void ${PIT64B_INSTANCE_NAME}_PERIOD_SET(uint32_t periodLSB, uint32_t periodMSB)
{
    /* Note: MSBPR should be updated first, as writing into LSBPR while
       SMOD is set will restart the timer */
    ${PIT64B_INSTANCE_NAME}_REGS->PIT64B_MSBPR = periodMSB;
    ${PIT64B_INSTANCE_NAME}_REGS->PIT64B_LSBPR = periodLSB;
}


void ${PIT64B_INSTANCE_NAME}_TimerInitialize(void)
{
    ${PIT64B_INSTANCE_NAME}_REGS->PIT64B_CR = PIT64B_CR_SWRST_Msk;
    ${PIT64B_INSTANCE_NAME}_REGS->PIT64B_MR = PIT64B_MR_CONT(${CONT?string('1','0')}U) | PIT64B_MR_SGCLK(${SGCLK?string('1','0')}U) | PIT64B_MR_PRESCALER(${PRESCALER}U) | PIT64B_MR_SMOD(${SMOD?string('1','0')}U);
    ${PIT64B_INSTANCE_NAME}_PERIOD_SET(${PIT64B_INSTANCE_NAME?lower_case}.periodLSB, ${PIT64B_INSTANCE_NAME?lower_case}.periodMSB);

<#if ENABLE_INTERRUPT == true>
    ${PIT64B_INSTANCE_NAME}_REGS->PIT64B_IDR = PIT64B_IDR_Msk;
    ${PIT64B_INSTANCE_NAME}_REGS->PIT64B_IER = PIT64B_IER_PERIOD(${PERIOD_INT?string('1','0')}U) | PIT64B_IER_OVRE(${OVRE_INT?string('1','0')}U) | PIT64B_IER_SECE(${SECE_INT?string('1','0')}U);
</#if>
}


void ${PIT64B_INSTANCE_NAME}_TimerRestart(void)
{
<#if SMOD == false>
    ${PIT64B_INSTANCE_NAME}_TimerInitialize();
    ${PIT64B_INSTANCE_NAME}_TimerStart();
<#else>
    ${PIT64B_INSTANCE_NAME}_PERIOD_SET(${PIT64B_INSTANCE_NAME?lower_case}.periodLSB, ${PIT64B_INSTANCE_NAME?lower_case}.periodMSB);
    ${PIT64B_INSTANCE_NAME?lower_case}.running = true;
</#if>
}


void ${PIT64B_INSTANCE_NAME}_TimerStart(void)
{
    ${PIT64B_INSTANCE_NAME}_REGS->PIT64B_CR = PIT64B_CR_START_Msk;
    ${PIT64B_INSTANCE_NAME?lower_case}.running = true;
}


void ${PIT64B_INSTANCE_NAME}_TimerStop(void)
{
    ${PIT64B_INSTANCE_NAME}_TimerInitialize();
    ${PIT64B_INSTANCE_NAME?lower_case}.running = false;
}


void ${PIT64B_INSTANCE_NAME}_TimerPeriodSet(uint64_t period)
{
<#if core.COMPILER_CHOICE == "XC32">
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wlong-long"
</#if>
    ${PIT64B_INSTANCE_NAME?lower_case}.periodMSB = (uint32_t)((period & 0xFFFFFFFF00000000U) >> 32U);
    ${PIT64B_INSTANCE_NAME?lower_case}.periodLSB = (uint32_t)(period & 0xFFFFFFFFU);
<#if core.COMPILER_CHOICE == "XC32">
#pragma GCC diagnostic pop
</#if>
    ${PIT64B_INSTANCE_NAME}_PERIOD_SET(${PIT64B_INSTANCE_NAME?lower_case}.periodLSB, ${PIT64B_INSTANCE_NAME?lower_case}.periodMSB);
<#if SMOD>
    ${PIT64B_INSTANCE_NAME?lower_case}.running = true;
</#if>
}


uint64_t ${PIT64B_INSTANCE_NAME}_TimerPeriodGet(void)
{
    uint64_t reg = ${PIT64B_INSTANCE_NAME}_REGS->PIT64B_MSBPR;
    reg <<= 32U;
    reg |= ${PIT64B_INSTANCE_NAME}_REGS->PIT64B_LSBPR;
    return reg;
}


uint64_t ${PIT64B_INSTANCE_NAME}_TimerCounterGet(void)
{
    uint64_t reg = ${PIT64B_INSTANCE_NAME}_REGS->PIT64B_TMSBR;
    reg <<= 32U;
    reg |= ${PIT64B_INSTANCE_NAME}_REGS->PIT64B_TLSBR;
    return reg;
}


uint32_t ${PIT64B_INSTANCE_NAME}_TimerFrequencyGet(void)
{
    return ${PIT64B_INSTANCE_NAME}_COUNTER_FREQUENCY;
}


void ${PIT64B_INSTANCE_NAME}_DelayMs(uint32_t delay_ms)
{
    uint64_t newCount = 0U, deltaCount = 0U, elapsedCount = 0U;
    uint64_t period = ${PIT64B_INSTANCE_NAME}_TimerPeriodGet() + 1UL;
    uint64_t delayCount = (${PIT64B_INSTANCE_NAME}_COUNTER_FREQUENCY / 1000U) * (uint64_t)delay_ms;
    uint64_t oldCount = ${PIT64B_INSTANCE_NAME}_TimerCounterGet();
    if(${PIT64B_INSTANCE_NAME?lower_case}.running)
    {
        while(elapsedCount < delayCount)
        {
            newCount = ${PIT64B_INSTANCE_NAME}_TimerCounterGet();
            deltaCount = (newCount > oldCount) ? (newCount - oldCount) : (period - oldCount + newCount);
            elapsedCount += deltaCount;
            oldCount = newCount;
        }
    }
}


void ${PIT64B_INSTANCE_NAME}_DelayUs(uint32_t delay_us)
{
    uint64_t newCount = 0U, deltaCount = 0U, elapsedCount = 0U;
    uint64_t period = ${PIT64B_INSTANCE_NAME}_TimerPeriodGet() + 1UL;
    uint64_t delayCount = (${PIT64B_INSTANCE_NAME}_COUNTER_FREQUENCY / 1000000U) * (uint64_t)delay_us;
    uint64_t oldCount = ${PIT64B_INSTANCE_NAME}_TimerCounterGet();
    if(${PIT64B_INSTANCE_NAME?lower_case}.running)
    {
        while(elapsedCount < delayCount)
        {
            newCount = ${PIT64B_INSTANCE_NAME}_TimerCounterGet();
            deltaCount = (newCount > oldCount) ? (newCount - oldCount) : (period - oldCount + newCount);
            elapsedCount += deltaCount;
            oldCount = newCount;
        }
    }
}
<#if ENABLE_INTERRUPT == true>


void ${PIT64B_INSTANCE_NAME}_TimerCallbackSet(${PIT64B_INSTANCE_NAME}_CALLBACK callback, uintptr_t context)
{
    ${PIT64B_INSTANCE_NAME?lower_case}.callback = callback;
    ${PIT64B_INSTANCE_NAME?lower_case}.context = context;
}


void ${PIT64B_INSTANCE_NAME}_InterruptHandler(void)
{
    volatile uint32_t reg = ${PIT64B_INSTANCE_NAME}_REGS->PIT64B_ISR;
    (void)reg;
    if(${PIT64B_INSTANCE_NAME?lower_case}.callback != NULL)
    {
        ${PIT64B_INSTANCE_NAME?lower_case}.callback(${PIT64B_INSTANCE_NAME?lower_case}.context);
    }
}
<#else>


bool ${PIT64B_INSTANCE_NAME}_TimerPeriodHasExpired(void)
{
    return ((${PIT64B_INSTANCE_NAME}_REGS->PIT64B_ISR & PIT64B_ISR_PERIOD_Msk) != 0U);
}
</#if>
