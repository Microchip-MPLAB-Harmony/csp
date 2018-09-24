/*******************************************************************************
  Periodic Interval Timer (PIT) 

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${PERIPH_INSTANCE_NAME?lower_case}.c

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
#include "plib_${PERIPH_INSTANCE_NAME?lower_case}.h"
#include "device.h"


// *****************************************************************************
// *****************************************************************************
// Section: File Scope Data Types
// *****************************************************************************
// *****************************************************************************
<#if USE_INTERRUPT == true>
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
static PIT_OBJECT ${PERIPH_INSTANCE_NAME?lower_case};
</#if>


void ${PERIPH_INSTANCE_NAME}_TimerInitialize(void)
{
    <#if USE_INTERRUPT == true && ENABLE_INTERRUPT == true>
        <#assign INTENABLE=1>
    <#else>
        <#assign INTENABLE=0>
    </#if>
    ${PERIPH_INSTANCE_NAME}_REGS->PIT_MR = PIT_MR_PIV(${PERIOD_TICKS}-1) | PIT_MR_PITEN(${ENABLE_COUNTER?string('1', '0')}) | PIT_MR_PITIEN(${INTENABLE});
}

void ${PERIPH_INSTANCE_NAME}_TimerRestart(void)
{
    ${PERIPH_INSTANCE_NAME}_REGS->PIT_MR &= ~PIT_MR_PITEN_Msk;
    while ((${PERIPH_INSTANCE_NAME}_REGS->PIT_PIIR & PIT_PIIR_CPIV_Msk) != 0);
    ${PERIPH_INSTANCE_NAME}_REGS->PIT_MR |= PIT_MR_PITEN_Msk;
}

void ${PERIPH_INSTANCE_NAME}_TimerStart(void)
{
    ${PERIPH_INSTANCE_NAME}_REGS->PIT_MR |= PIT_MR_PITEN_Msk;
}

void ${PERIPH_INSTANCE_NAME}_TimerStop(void)
{
    ${PERIPH_INSTANCE_NAME}_REGS->PIT_MR &= ~PIT_MR_PITEN_Msk;
    while ((${PERIPH_INSTANCE_NAME}_REGS->PIT_PIIR & PIT_PIIR_CPIV_Msk) != 0);
}

void ${PERIPH_INSTANCE_NAME}_TimerPeriodSet(uint32_t period)
{
    ${PERIPH_INSTANCE_NAME}_TimerStop();
    ${PERIPH_INSTANCE_NAME}_REGS->PIT_MR &= ~PIT_MR_PIV_Msk;
    ${PERIPH_INSTANCE_NAME}_REGS->PIT_MR |= PIT_MR_PIV(period);
    ${PERIPH_INSTANCE_NAME}_TimerStart();

}

uint32_t ${PERIPH_INSTANCE_NAME}_TimerPeriodGet(void)
{
    return ${PERIPH_INSTANCE_NAME}_REGS->PIT_MR & PIT_MR_PIV_Msk;
}

uint32_t ${PERIPH_INSTANCE_NAME}_TimerCounterGet(void)
{
    return (${PERIPH_INSTANCE_NAME}_REGS->PIT_PIIR & PIT_PIIR_CPIV_Msk) >> PIT_PIIR_CPIV_Pos;
}

uint32_t ${PERIPH_INSTANCE_NAME}_TimerFrequencyGet(void)
{
    return ${core.MASTER_CLOCK_FREQUENCY} / 16;
}

<#if USE_INTERRUPT == false>
bool ${PERIPH_INSTANCE_NAME}_TimerPeriodHasExpired(void)
{
    return !!(${PERIPH_INSTANCE_NAME}_REGS->PIT_SR & PIT_SR_PITS_Msk);
}
</#if>
<#if USE_INTERRUPT == true>
void ${PERIPH_INSTANCE_NAME}_DisableInterrupt()
{
    ${PERIPH_INSTANCE_NAME}_REGS->PIT_MR &= ~PIT_MR_PITIEN_Msk;
}

void ${PERIPH_INSTANCE_NAME}_EnableInterrupt()
{
    ${PERIPH_INSTANCE_NAME}_REGS->PIT_MR |= PIT_MR_PITIEN_Msk;
}

void ${PERIPH_INSTANCE_NAME}_DelayMS(uint32_t delay)
{
	uint32_t tickStart, delayTicks;

	if((${PERIPH_INSTANCE_NAME}_REGS->PIT_MR & (PIT_MR_PITEN_Msk | PIT_MR_PITIEN_Msk)) == (PIT_MR_PITEN_Msk | PIT_MR_PITIEN_Msk))
	{
		tickStart=${PERIPH_INSTANCE_NAME?lower_case}.tickCounter;
		delayTicks=delay/${PERIOD_MS};

		while((${PERIPH_INSTANCE_NAME?lower_case}.tickCounter-tickStart)<delayTicks);
	}
}

void ${PERIPH_INSTANCE_NAME}_TimerCallbackSet(PIT_CALLBACK callback, uintptr_t context)
{
    ${PERIPH_INSTANCE_NAME?lower_case}.callback = callback;
    ${PERIPH_INSTANCE_NAME?lower_case}.context = context;
}

void ${PERIPH_INSTANCE_NAME}_InterruptHandler(void)
{
    uint32_t reg = ${PERIPH_INSTANCE_NAME}_REGS->PIT_PIVR;
    ${PERIPH_INSTANCE_NAME?lower_case}.tickCounter++;
    if(${PERIPH_INSTANCE_NAME?lower_case}.callback)
        ${PERIPH_INSTANCE_NAME?lower_case}.callback(${PERIPH_INSTANCE_NAME?lower_case}.context);
}
</#if>
/*******************************************************************************
 End of File
*/
