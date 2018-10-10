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
Copyright (c) 2018 released Microchip Technology Inc.  All rights reserved.

Microchip licenses to you the right to use, modify, copy and distribute
Software only when embedded on a Microchip microcontroller or digital signal
controller that is integrated into your product or third party product
(pursuant to the sublicense terms in the accompanying license agreement).

You should refer to the license agreement accompanying this Software for
additional information regarding your rights and obligations.

SOFTWARE AND DOCUMENTATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND,
EITHER EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION, ANY WARRANTY OF
MERCHANTABILITY, TITLE, NON-INFRINGEMENT AND FITNESS FOR A PARTICULAR PURPOSE.
IN NO EVENT SHALL MICROCHIP OR ITS LICENSORS BE LIABLE OR OBLIGATED UNDER
CONTRACT, NEGLIGENCE, STRICT LIABILITY, CONTRIBUTION, BREACH OF WARRANTY, OR
OTHER LEGAL EQUITABLE THEORY ANY DIRECT OR INDIRECT DAMAGES OR EXPENSES
INCLUDING BUT NOT LIMITED TO ANY INCIDENTAL, SPECIAL, INDIRECT, PUNITIVE OR
CONSEQUENTIAL DAMAGES, LOST PROFITS OR LOST DATA, COST OF PROCUREMENT OF
SUBSTITUTE GOODS, TECHNOLOGY, SERVICES, OR ANY CLAIMS BY THIRD PARTIES
(INCLUDING BUT NOT LIMITED TO ANY DEFENSE THEREOF), OR OTHER SIMILAR COSTS.
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
    ${PIT_INSTANCE_NAME}_REGS->PIT_MR = PIT_MR_PIV(${PERIOD_TICKS}-1) | PIT_MR_PITEN(${ENABLE_COUNTER?string('1', '0')}) | PIT_MR_PITIEN(${INTENABLE});
}

void ${PIT_INSTANCE_NAME}_TimerRestart(void)
{
    ${PIT_INSTANCE_NAME}_REGS->PIT_MR &= ~PIT_MR_PITEN_Msk;
    while ((${PIT_INSTANCE_NAME}_REGS->PIT_PIIR & PIT_PIIR_CPIV_Msk) != 0);
    ${PIT_INSTANCE_NAME}_REGS->PIT_MR |= PIT_MR_PITEN_Msk;
}

void ${PIT_INSTANCE_NAME}_TimerStart(void)
{
    ${PIT_INSTANCE_NAME}_REGS->PIT_MR |= PIT_MR_PITEN_Msk;
}

void ${PIT_INSTANCE_NAME}_TimerStop(void)
{
    ${PIT_INSTANCE_NAME}_REGS->PIT_MR &= ~PIT_MR_PITEN_Msk;
    while ((${PIT_INSTANCE_NAME}_REGS->PIT_PIIR & PIT_PIIR_CPIV_Msk) != 0);
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

uint32_t ${PIT_INSTANCE_NAME}_TimerFrequencyGet(void)
{
    return ${core.MASTER_CLOCK_FREQUENCY} / 16;
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

		while((${PIT_INSTANCE_NAME?lower_case}.tickCounter-tickStart)<delayTicks);
	}
}

void ${PIT_INSTANCE_NAME}_TimerCallbackSet(PIT_CALLBACK callback, uintptr_t context)
{
    ${PIT_INSTANCE_NAME?lower_case}.callback = callback;
    ${PIT_INSTANCE_NAME?lower_case}.context = context;
}

void ${PIT_INSTANCE_NAME}_InterruptHandler(void)
{
    uint32_t reg = ${PIT_INSTANCE_NAME}_REGS->PIT_PIVR;
    ${PIT_INSTANCE_NAME?lower_case}.tickCounter++;
    if(${PIT_INSTANCE_NAME?lower_case}.callback)
        ${PIT_INSTANCE_NAME?lower_case}.callback(${PIT_INSTANCE_NAME?lower_case}.context);
}
</#if>
/*******************************************************************************
 End of File
*/
