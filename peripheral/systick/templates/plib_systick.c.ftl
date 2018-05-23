/*******************************************************************************
  SysTick Peripheral Library

  Company:
    Microchip Technology Inc.

  File Name:
    plib_systick.c

  Summary:
    Systick Source File

  Description:
    None

*******************************************************************************/

/*******************************************************************************
Copyright (c) 2017 released Microchip Technology Inc.  All rights reserved.

Microchip licenses to you the right to use, modify, copy and distribute
Software only when embedded on a Microchip microcontroller or digital signal
controller that is integrated into your product or third party product
(pursuant to the sublicense terms in the accompanying license agreement).

You should refer to the license agreement accompanying this Software for
additional information regarding your rights and obligations.

SOFTWARE AND DOCUMENTATION ARE PROVIDED AS IS  WITHOUT  WARRANTY  OF  ANY  KIND,
EITHER EXPRESS  OR  IMPLIED,  INCLUDING  WITHOUT  LIMITATION,  ANY  WARRANTY  OF
MERCHANTABILITY, TITLE, NON-INFRINGEMENT AND FITNESS FOR A  PARTICULAR  PURPOSE.
IN NO EVENT SHALL MICROCHIP OR  ITS  LICENSORS  BE  LIABLE  OR  OBLIGATED  UNDER
CONTRACT, NEGLIGENCE, STRICT LIABILITY, CONTRIBUTION,  BREACH  OF  WARRANTY,  OR
OTHER LEGAL  EQUITABLE  THEORY  ANY  DIRECT  OR  INDIRECT  DAMAGES  OR  EXPENSES
INCLUDING BUT NOT LIMITED TO ANY  INCIDENTAL,  SPECIAL,  INDIRECT,  PUNITIVE  OR
CONSEQUENTIAL DAMAGES, LOST  PROFITS  OR  LOST  DATA,  COST  OF  PROCUREMENT  OF
SUBSTITUTE  GOODS,  TECHNOLOGY,  SERVICES,  OR  ANY  CLAIMS  BY  THIRD   PARTIES
(INCLUDING BUT NOT LIMITED TO ANY DEFENSE  THEREOF),  OR  OTHER  SIMILAR  COSTS.
*******************************************************************************/

#include "device.h"
#include "peripheral/systick/plib_systick.h"

<#if USE_SYSTICK_INTERRUPT == true>
	<#lt>SYSTICK_OBJECT systick;
</#if>

void SYSTICK_TimerInitialize ( void )
{
	SysTick->CTRL = 0;
	SysTick->VAL = 0;
	SysTick->LOAD = 0x${SYSTICK_PERIOD} - 1;
	<#if USE_SYSTICK_INTERRUPT == true && SYSTICK_CLOCK == "0">
		<#lt>	SysTick->CTRL = SysTick_CTRL_TICKINT_Msk;
	</#if>
	<#if USE_SYSTICK_INTERRUPT == true && SYSTICK_CLOCK == "1">
		<#lt>	SysTick->CTRL = SysTick_CTRL_TICKINT_Msk | SysTick_CTRL_CLKSOURCE_Msk;
	</#if>
	<#if USE_SYSTICK_INTERRUPT == false && SYSTICK_CLOCK == "1">
		<#lt>	SysTick->CTRL = SysTick_CTRL_CLKSOURCE_Msk;
	</#if>
	<#if USE_SYSTICK_INTERRUPT == true >

		<#lt>	systick.tickCounter = 0;
		<#lt>	systick.callback = NULL;
	</#if>
}

void SYSTICK_TimerStart ( void )
{
	SysTick->CTRL |= SysTick_CTRL_ENABLE_Msk;
}

void SYSTICK_TimerStop ( void )
{
	SysTick->CTRL &= ~(SysTick_CTRL_ENABLE_Msk);
}

void SYSTICK_TimerPeriodSet ( uint32_t period )
{
	SysTick->LOAD = period - 1;
}

uint32_t SYSTICK_TimerPeriodGet ( void )
{
		return(SysTick->LOAD);
}

uint32_t SYSTICK_TimerCounterGet ( void )
{
	return (SysTick->VAL);
}

uint32_t SYSTICK_TimerFrequencyGet ( void )
{
	return (SYSTICK_FREQ);
}

<#if USE_SYSTICK_INTERRUPT == false>
	<#lt>bool SYSTICK_TimerPeriodHasExpired(void)
	<#lt>{
	<#lt>	return (SysTick->CTRL & SysTick_CTRL_COUNTFLAG_Msk) > 0;
	<#lt>}
</#if>

<#if USE_SYSTICK_INTERRUPT == true>
	<#lt>void SYSTICK_DelayMs ( uint32_t delay)
	<#lt>{
	<#lt>	uint32_t tickStart, delayTicks;

	<#lt>	if( (SysTick->CTRL & (SysTick_CTRL_TICKINT_Msk | SysTick_CTRL_ENABLE_Msk)) == (SysTick_CTRL_TICKINT_Msk | SysTick_CTRL_ENABLE_Msk))
	<#lt>	{
	<#lt>		tickStart=systick.tickCounter;
	<#lt>		delayTicks=(1000*delay)/SYSTICK_INTERRUPT_PERIOD_IN_US;  // Number of tick interrupts for a given delay (in ms)

	<#lt>		while((systick.tickCounter-tickStart)<delayTicks)
	<#lt>		{
	<#lt>		}
	<#lt>	}
	<#lt>}
	
	<#lt>void SYSTICK_TimerCallbackSet ( SYSTICK_CALLBACK callback, uintptr_t context )
	<#lt>{
	<#lt>	systick.callback = callback;
	<#lt>	systick.context = context;
	<#lt>}

	<#lt>void SysTick_Handler()
	<#lt>{
	<#lt>	systick.tickCounter++;
	<#lt>	if(systick.callback != NULL)
	<#lt>	{
	<#lt>		systick.callback(systick.context);
	<#lt>	}
	<#lt>}
</#if>
