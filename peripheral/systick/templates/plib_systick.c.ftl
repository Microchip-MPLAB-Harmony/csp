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

#include "device.h"
#include "peripheral/systick/plib_systick.h"

<#if USE_SYSTICK_INTERRUPT == true>
	<#lt>SYSTICK_OBJECT systick;
</#if>

void SYSTICK_TimerInitialize ( void )
{
	SysTick->CTRL = 0;
	SysTick->VAL = 0;
	SysTick->LOAD = ${SYSTICK_PERIOD} - 1;
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

void SYSTICK_TimerRestart ( void )
{
	SysTick->CTRL &= ~(SysTick_CTRL_ENABLE_Msk);
	SysTick->VAL = 0;
	SysTick->CTRL |= SysTick_CTRL_ENABLE_Msk;
}

void SYSTICK_TimerStart ( void )
{
	SysTick->VAL = 0;
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
	<#lt>		delayTicks=(1000 * delay)/SYSTICK_INTERRUPT_PERIOD_IN_US;  // Number of tick interrupts for a given delay (in ms)

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
