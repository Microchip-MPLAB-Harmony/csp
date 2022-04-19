/*******************************************************************************
  Periodic Interval Timer (PIT) 

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${PIT_INSTANCE_NAME?lower_case}.c

  Summary:
    Periodic Interval Timer (PIT) PLIB.

  Description:
    This file defines the interface for the Periodic Interval Timer (PIT).
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
#include "plib_${PIT_INSTANCE_NAME?lower_case}.h"
#include "device.h"

#define PIT_COUNTER_FREQUENCY       (${core.PIT_CLOCK_FREQUENCY}U / 16U)


// *****************************************************************************
// *****************************************************************************
// Section: File Scope Data Types
// *****************************************************************************
// *****************************************************************************
<#if ENABLE_INTERRUPT == true>
typedef struct
{
    PIT_CALLBACK        callback;
    uintptr_t           context;
    volatile uint32_t   tickCounter;
} PIT_OBJECT;

// *****************************************************************************
// *****************************************************************************
// Section: File Scope or Global Constants
// *****************************************************************************
// *****************************************************************************
static PIT_OBJECT ${PIT_INSTANCE_NAME?lower_case};
</#if>


void ${PIT_INSTANCE_NAME}_TimerInitialize(void)
{
    ${PIT_INSTANCE_NAME}_REGS->PIT_PIVR;
    ${PIT_INSTANCE_NAME}_REGS->PIT_MR = PIT_MR_PIV(${PERIOD_TICKS - 1}U)${ENABLE_COUNTER?string(' | PIT_MR_PITEN_Msk', "")}${ENABLE_INTERRUPT?string(" | PIT_MR_PITIEN_Msk", "")};
}

void ${PIT_INSTANCE_NAME}_TimerRestart(void)
{
    ${PIT_INSTANCE_NAME}_REGS->PIT_MR &= ~PIT_MR_PITEN_Msk;
    while((${PIT_INSTANCE_NAME}_REGS->PIT_PIIR & PIT_PIIR_CPIV_Msk) != 0U)
    {
        //do nothing
    }
    ${PIT_INSTANCE_NAME}_REGS->PIT_MR |= PIT_MR_PITEN_Msk;
}

void ${PIT_INSTANCE_NAME}_TimerStart(void)
{
    ${PIT_INSTANCE_NAME}_REGS->PIT_MR |= PIT_MR_PITEN_Msk;
}

void ${PIT_INSTANCE_NAME}_TimerStop(void)
{
    ${PIT_INSTANCE_NAME}_REGS->PIT_MR &= ~PIT_MR_PITEN_Msk;
    while ((${PIT_INSTANCE_NAME}_REGS->PIT_PIIR & PIT_PIIR_CPIV_Msk) != 0U)
    {
        //do nothing
    }
}

void ${PIT_INSTANCE_NAME}_TimerPeriodSet(uint32_t period)
{
    ${PIT_INSTANCE_NAME}_TimerStop();
    ${PIT_INSTANCE_NAME}_REGS->PIT_MR &= ~PIT_MR_PIV_Msk;
    ${PIT_INSTANCE_NAME}_REGS->PIT_MR |= PIT_MR_PIV(period);
    ${PIT_INSTANCE_NAME}_TimerStart();
}

uint32_t ${PIT_INSTANCE_NAME}_TimerPeriodGet(void)
{
    return ${PIT_INSTANCE_NAME}_REGS->PIT_MR & PIT_MR_PIV_Msk;
}

uint32_t ${PIT_INSTANCE_NAME}_TimerCounterGet(void)
{
    return (${PIT_INSTANCE_NAME}_REGS->PIT_PIIR & PIT_PIIR_CPIV_Msk) >> PIT_PIIR_CPIV_Pos;
}

void ${PIT_INSTANCE_NAME}_TimerCompareSet( uint16_t compare )
{
    (void) compare;
}

uint32_t ${PIT_INSTANCE_NAME}_TimerFrequencyGet(void)
{
    return PIT_COUNTER_FREQUENCY;
}

void ${PIT_INSTANCE_NAME}_DelayMs(uint32_t delay_ms)
{
    uint32_t period = (${PIT_INSTANCE_NAME}_REGS->PIT_MR & PIT_MR_PIV_Msk) + 1U;
    uint32_t delayCount = (PIT_COUNTER_FREQUENCY / 1000U) * delay_ms;
    uint32_t oldCount = ${PIT_INSTANCE_NAME}_REGS->PIT_PIIR & PIT_PIIR_CPIV_Msk;
    uint32_t newCount = 0U, deltaCount = 0U, elapsedCount = 0U;

    if((${PIT_INSTANCE_NAME}_REGS->PIT_MR & PIT_MR_PITEN_Msk) != 0U)
    {
        while(elapsedCount < delayCount)
        {
            newCount = ${PIT_INSTANCE_NAME}_REGS->PIT_PIIR & PIT_PIIR_CPIV_Msk;
            deltaCount = (newCount > oldCount) ? (newCount - oldCount) : (period - oldCount + newCount);
            elapsedCount += deltaCount;
            oldCount = newCount;
        }
    }
}

void ${PIT_INSTANCE_NAME}_DelayUs(uint32_t delay_us)
{
    uint32_t period = (${PIT_INSTANCE_NAME}_REGS->PIT_MR & PIT_MR_PIV_Msk) + 1U;
    uint32_t delayCount = (PIT_COUNTER_FREQUENCY / 1000000U) * delay_us;
    uint32_t oldCount = ${PIT_INSTANCE_NAME}_REGS->PIT_PIIR & PIT_PIIR_CPIV_Msk;
    uint32_t newCount = 0U, deltaCount = 0U, elapsedCount = 0U;

    if((${PIT_INSTANCE_NAME}_REGS->PIT_MR & PIT_MR_PITEN_Msk) != 0U)
    {
        while(elapsedCount < delayCount)
        {
            newCount = ${PIT_INSTANCE_NAME}_REGS->PIT_PIIR & PIT_PIIR_CPIV_Msk;
            deltaCount = (newCount > oldCount) ? (newCount - oldCount) : (period - oldCount + newCount);
            elapsedCount += deltaCount;
            oldCount = newCount;
        }
    }
}

<#if ENABLE_INTERRUPT == true>
void ${PIT_INSTANCE_NAME}_TimerCallbackSet(PIT_CALLBACK callback, uintptr_t context)
{
    ${PIT_INSTANCE_NAME?lower_case}.callback = callback;
    ${PIT_INSTANCE_NAME?lower_case}.context = context;
}

void ${PIT_INSTANCE_NAME}_InterruptHandler(void)
{
    uint32_t interruptStatus = ${PIT_INSTANCE_NAME}_REGS->PIT_SR;
    if(interruptStatus != 0U)
	{
        volatile uint32_t reg = ${PIT_INSTANCE_NAME}_REGS->PIT_PIVR;
        (void)reg;
        ${PIT_INSTANCE_NAME?lower_case}.tickCounter++;
        if((${PIT_INSTANCE_NAME?lower_case}.callback) != NULL)
        {
            ${PIT_INSTANCE_NAME?lower_case}.callback(${PIT_INSTANCE_NAME?lower_case}.context);
        }
    }
}
<#else>

bool ${PIT_INSTANCE_NAME}_TimerPeriodHasExpired(void)
{
    return ((${PIT_INSTANCE_NAME}_REGS->PIT_SR & PIT_SR_PITS_Msk) != 0U);
}
</#if>
/*******************************************************************************
 End of File
*/
