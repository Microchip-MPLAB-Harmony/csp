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

#include "plib_${PIT64B_INSTANCE_NAME?lower_case}.h"

<#if ENABLE_INTERRUPT == true>
typedef struct
{
    ${PIT64B_INSTANCE_NAME}_CALLBACK callback;
    uintptr_t context;
    volatile uint32_t tickCounter;
    bool running;
} ${PIT64B_INSTANCE_NAME}_OBJECT;

static ${PIT64B_INSTANCE_NAME}_OBJECT ${PIT64B_INSTANCE_NAME?lower_case};
</#if>

void ${PIT64B_INSTANCE_NAME}_TimerInitialize(void)
{
    ${PIT64B_INSTANCE_NAME}_REGS->PIT64B_CR = PIT64B_CR_SWRST_Msk;
    ${PIT64B_INSTANCE_NAME}_REGS->PIT64B_MR = PIT64B_MR_CONT(${CONT?string('1','0')}) | PIT64B_MR_SGCLK(${SGCLK?string('1','0')}) | PIT64B_MR_PRESCALER(${PRESCALER});
    ${PIT64B_INSTANCE_NAME}_REGS->PIT64B_MSBPR = ${PERIOD_MSB};
    ${PIT64B_INSTANCE_NAME}_REGS->PIT64B_LSBPR = ${PERIOD_LSB};
    ${PIT64B_INSTANCE_NAME}_REGS->PIT64B_MR |= PIT64B_MR_SMOD(${SMOD?string('1','0')});
<#if ENABLE_INTERRUPT == true>
    ${PIT64B_INSTANCE_NAME?lower_case}.running = 0;
    ${PIT64B_INSTANCE_NAME}_REGS->PIT64B_IDR = PIT64B_IDR_Msk;
    ${PIT64B_INSTANCE_NAME}_REGS->PIT64B_IER = PIT64B_IER_PERIOD(${PERIOD_INT?string('1','0')}) | PIT64B_IER_OVRE(${OVRE_INT?string('1','0')}) | PIT64B_IER_SECE(${SECE_INT?string('1','0')});
</#if>
}

void ${PIT64B_INSTANCE_NAME}_TimerRestart(void)
{
<#if SMOD == false>
    ${PIT64B_INSTANCE_NAME}_TimerInitialize();
    ${PIT64B_INSTANCE_NAME}_TimerStart();
<#else>
    ${PIT64B_INSTANCE_NAME}_REGS->PIT64B_MSBPR = ${PERIOD_MSB};
    ${PIT64B_INSTANCE_NAME}_REGS->PIT64B_LSBPR = ${PERIOD_LSB};
</#if>
<#if ENABLE_INTERRUPT == true>
    ${PIT64B_INSTANCE_NAME?lower_case}.running = 1;
</#if>
}

void ${PIT64B_INSTANCE_NAME}_TimerStart(void)
{
    ${PIT64B_INSTANCE_NAME}_REGS->PIT64B_CR = PIT64B_CR_START_Msk;
<#if ENABLE_INTERRUPT == true>
    ${PIT64B_INSTANCE_NAME?lower_case}.running = 1;
</#if>
}

void ${PIT64B_INSTANCE_NAME}_TimerStop(void)
{
    ${PIT64B_INSTANCE_NAME}_TimerInitialize();
<#if ENABLE_INTERRUPT == true>
    ${PIT64B_INSTANCE_NAME?lower_case}.running = 0;
</#if>
}

void ${PIT64B_INSTANCE_NAME}_TimerPeriodSet(uint64_t period)
{
    ${PIT64B_INSTANCE_NAME}_REGS->PIT64B_MSBPR = (period & 0xFFFFFFFF00000000)>>32;
    ${PIT64B_INSTANCE_NAME}_REGS->PIT64B_LSBPR = (period & 0xFFFFFFFF);
    <#if SMOD && ENABLE_INTERRUPT>
    ${PIT64B_INSTANCE_NAME?lower_case}.running = 1;
    </#if>
}

uint64_t ${PIT64B_INSTANCE_NAME}_TimerPeriodGet(void)
{
    uint64_t reg = ${PIT64B_INSTANCE_NAME}_REGS->PIT64B_MSBPR;
    reg = reg<<32;
    reg |= ${PIT64B_INSTANCE_NAME}_REGS->PIT64B_LSBPR;
    return reg;
}

uint64_t ${PIT64B_INSTANCE_NAME}_TimerCounterGet(void)
{
    uint64_t reg = ${PIT64B_INSTANCE_NAME}_REGS->PIT64B_TMSBR;
    reg = reg<<32;
    reg |= ${PIT64B_INSTANCE_NAME}_REGS->PIT64B_TLSBR;
    return reg;
}

uint32_t ${PIT64B_INSTANCE_NAME}_TimerFrequencyGet(void)
{
    return ${SRC_FREQ};
}

<#if ENABLE_INTERRUPT == false>
bool ${PIT64B_INSTANCE_NAME}_TimerPeriodHasExpired(void)
{
    return ((${PIT64B_INSTANCE_NAME}_REGS->PIT64B_ISR & PIT64B_ISR_PERIOD_Msk) == PIT64B_ISR_PERIOD_Msk);
}
<#elseif ENABLE_INTERRUPT == true>
void ${PIT64B_INSTANCE_NAME}_DelayMs(uint32_t delay)
{
    uint32_t tickStart;
    uint32_t delayTicks;

    if (${PIT64B_INSTANCE_NAME?lower_case}.running && ((${PIT64B_INSTANCE_NAME}_REGS->PIT64B_IMR & PIT64B_IMR_PERIOD_Msk) == PIT64B_IMR_PERIOD_Msk)) {
        tickStart=${PIT64B_INSTANCE_NAME?lower_case}.tickCounter;
        delayTicks=1000*delay/${PERIOD_US};

        while((${PIT64B_INSTANCE_NAME?lower_case}.tickCounter-tickStart) < delayTicks);
    }
}

void ${PIT64B_INSTANCE_NAME}_TimerCallbackSet(${PIT64B_INSTANCE_NAME}_CALLBACK callback, uintptr_t context)
{
    ${PIT64B_INSTANCE_NAME?lower_case}.callback = callback;
    ${PIT64B_INSTANCE_NAME?lower_case}.context = context;
}

void ${PIT64B_INSTANCE_NAME}_InterruptHandler(void)
{
    uint32_t reg = ${PIT64B_INSTANCE_NAME}_REGS->PIT64B_ISR;
    ${PIT64B_INSTANCE_NAME?lower_case}.tickCounter++;
    if(${PIT64B_INSTANCE_NAME?lower_case}.callback)
        ${PIT64B_INSTANCE_NAME?lower_case}.callback(${PIT64B_INSTANCE_NAME?lower_case}.context);
}
</#if>
