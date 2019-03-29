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
    <#if ENABLE_INTERRUPT == true>
        <#assign INTENABLE=1>
    <#else>
        <#assign INTENABLE=0>
    </#if>
    ${PIT_INSTANCE_NAME}_REGS->PIT_PIVR;
    ${PIT_INSTANCE_NAME}_REGS->PIT_MR = PIT_MR_PIV(${PERIOD_TICKS}-1) | PIT_MR_PITEN(${ENABLE_COUNTER?string('1', '0')}) | PIT_MR_PITIEN(${INTENABLE});
}

void ${PIT_INSTANCE_NAME}_TimerRestart(void)
{
    ${PIT_INSTANCE_NAME}_REGS->PIT_MR &= ~PIT_MR_PITEN_Msk;
    while((${PIT_INSTANCE_NAME}_REGS->PIT_PIIR & PIT_PIIR_CPIV_Msk) != 0) {
        ;
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
    while ((${PIT_INSTANCE_NAME}_REGS->PIT_PIIR & PIT_PIIR_CPIV_Msk) != 0) {
        ;
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
    return ${core.PIT_CLOCK_FREQUENCY} / 16;
}

<#if ENABLE_INTERRUPT == false>
bool ${PIT_INSTANCE_NAME}_TimerPeriodHasExpired(void)
{
    return !!(${PIT_INSTANCE_NAME}_REGS->PIT_SR & PIT_SR_PITS_Msk);
}
</#if>
<#if ENABLE_INTERRUPT == true>
void ${PIT_INSTANCE_NAME}_DelayMs(uint32_t delay)
{
    uint32_t tickStart, delayTicks;

    if((${PIT_INSTANCE_NAME}_REGS->PIT_MR & (PIT_MR_PITEN_Msk | PIT_MR_PITIEN_Msk)) == (PIT_MR_PITEN_Msk | PIT_MR_PITIEN_Msk))
    {
        tickStart=${PIT_INSTANCE_NAME?lower_case}.tickCounter;
        delayTicks=delay/${PERIOD_MS};

        while( (${PIT_INSTANCE_NAME?lower_case}.tickCounter-tickStart) < delayTicks ) {
            ;
        }
    }
}

void ${PIT_INSTANCE_NAME}_TimerCallbackSet(PIT_CALLBACK callback, uintptr_t context)
{
    ${PIT_INSTANCE_NAME?lower_case}.callback = callback;
    ${PIT_INSTANCE_NAME?lower_case}.context = context;
}

void ${PIT_INSTANCE_NAME}_InterruptHandler(void)
{
    uint32_t interruptStatus = ${PIT_INSTANCE_NAME}_REGS->PIT_SR;
    if( interruptStatus ) {
        uint32_t reg = ${PIT_INSTANCE_NAME}_REGS->PIT_PIVR;
        ${PIT_INSTANCE_NAME?lower_case}.tickCounter++;
        if(${PIT_INSTANCE_NAME?lower_case}.callback) {
            ${PIT_INSTANCE_NAME?lower_case}.callback(${PIT_INSTANCE_NAME?lower_case}.context);
        }
    }
}
</#if>
/*******************************************************************************
 End of File
*/
