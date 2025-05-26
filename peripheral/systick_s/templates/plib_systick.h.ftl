/*******************************************************************************
  Interface definition of SYSTICK PLIB.

  Company:
    Microchip Technology Inc.

  File Name:
    plib_systick.h

  Summary:
    Interface definition of the System Timer Plib (SYSTICK).

  Description:
    This file defines the interface for the SYSTICK Plib.
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

#ifndef PLIB_SYSTICK_H    // Guards against multiple inclusion
#define PLIB_SYSTICK_H

#include <stdint.h>
#include <stdbool.h>
#include <stddef.h>

#ifdef __cplusplus // Provide C++ Compatibility
    extern "C" {
#endif


// *****************************************************************************
// *****************************************************************************
// Section: Interface
// *****************************************************************************
// *****************************************************************************

<#if SYSTICK_SECURE_CLOCK == "0">
    <#lt>#define SYSTICK_FREQ       ${SYSTICK_CLOCK_FREQUENCY}U
</#if>
<#if SYSTICK_CLOCK == "1">
    <#lt>#define SYSTICK_FREQ   ${CPU_CLOCK_FREQUENCY}U
</#if>

<#if USE_SYSTICK_SECURE_INTERRUPT == true>
    <#lt>#define SYSTICK_INTERRUPT_PERIOD_IN_US  (${SYSTICK_SECURE_PERIOD_US}U)

    <#lt>typedef void (*SYSTICK_CALLBACK)(uintptr_t context);
</#if>

<#if USE_SYSTICK_SECURE_INTERRUPT == true>
	<#lt>typedef struct
	<#lt>{ 
	<#lt>    uint32_t start; 
	<#lt>    uint32_t count; 
	<#lt>}SYSTICK_TIMEOUT;
    <#lt>typedef struct
    <#lt>{
    <#lt>   SYSTICK_CALLBACK          callback;
    <#lt>   uintptr_t                 context;
    <#lt>   volatile uint32_t         tickCounter;
    <#lt>} SYSTICK_OBJECT ;
</#if>
/***************************** SYSTICK API *******************************/
void SYSTICK_TimerInitialize ( void );
void SYSTICK_TimerRestart ( void );
void SYSTICK_TimerStart ( void );
void SYSTICK_TimerStop ( void );
void SYSTICK_TimerPeriodSet ( uint32_t period );
uint32_t SYSTICK_TimerPeriodGet ( void );
uint32_t SYSTICK_TimerCounterGet ( void );
uint32_t SYSTICK_TimerFrequencyGet ( void );
void SYSTICK_DelayMs ( uint32_t delay_ms );
void SYSTICK_DelayUs ( uint32_t delay_us );

<#if USE_SYSTICK_SECURE_INTERRUPT == false>
    <#lt>bool SYSTICK_TimerPeriodHasExpired(void);
</#if>
<#if USE_SYSTICK_SECURE_INTERRUPT == true>
    <#lt>void SYSTICK_TimerCallbackSet ( SYSTICK_CALLBACK callback, uintptr_t context );
	<#lt>uint32_t SYSTICK_GetTickCounter(void);
	<#lt>void SYSTICK_StartTimeOut (SYSTICK_TIMEOUT* timeout, uint32_t delay_ms);
	<#lt>void SYSTICK_ResetTimeOut (SYSTICK_TIMEOUT* timeout);
	<#lt>bool SYSTICK_IsTimeoutReached (SYSTICK_TIMEOUT* timeout);
</#if>
#ifdef __cplusplus // Provide C++ Compatibility
 }
#endif

#endif
