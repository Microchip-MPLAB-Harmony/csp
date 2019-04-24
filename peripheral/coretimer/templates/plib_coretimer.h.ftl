/*******************************************************************************
  Interface definition of Core Timer PLIB.

  Company:
    Microchip Technology Inc.

  File Name:
    plib_coretimer.h

  Summary:
    Interface definition of the Core Timer Plib .

  Description:
    This file defines the interface for the Core Timer Plib.
*******************************************************************************/

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

#ifndef PLIB_CORETIMER_H    // Guards against multiple inclusion
#define PLIB_CORETIMER_H

#include <stdint.h>

#ifdef __cplusplus // Provide C++ Compatibility
	extern "C" {
#endif

#define CORE_TIMER_FREQUENCY    ${CORE_TIMER_FREQUENCY}

<#if CORE_TIMER_INTERRUPT_MODE == true && CORE_TIMER_PERIODIC_INTERRUPT == true>
    <#lt>#define CORE_TIMER_INTERRUPT_PERIOD_VALUE    ${CORE_TIMER_PERIOD_VALUE}
    <#lt>#define CORE_TIMER_INTERRUPT_PERIOD_IN_US     ${CORE_TIMER_PERIOD_US}

    <#lt>typedef void (*CORETIMER_CALLBACK)(uint32_t status, uintptr_t context);

    <#lt>typedef struct
    <#lt>{
    <#lt>    CORETIMER_CALLBACK  callback;
    <#lt>    uintptr_t           context;
    <#lt>    volatile uint32_t   tickCounter;
    <#lt>    uint32_t            period;
    <#lt>} CORETIMER_OBJECT ;

    <#lt>void CORETIMER_Initialize( void );
    <#lt>void CORETIMER_CallbackSet ( CORETIMER_CALLBACK callback, uintptr_t context );
    <#lt>uint32_t CORETIMER_FrequencyGet ( void );
    <#lt>void CORETIMER_PeriodSet ( uint32_t period );
    <#lt>void CORETIMER_Start();
    <#lt>void CORETIMER_Stop();
    <#lt>void CORETIMER_DelayMs ( uint32_t delay_ms);
</#if>

<#if CORE_TIMER_INTERRUPT_MODE == true && CORE_TIMER_PERIODIC_INTERRUPT == false>
    <#lt>typedef void (*CORETIMER_CALLBACK)(uint32_t status, uintptr_t context);

    <#lt>typedef struct
    <#lt>{
    <#lt>    CORETIMER_CALLBACK  callback;
    <#lt>    uintptr_t           context;
    <#lt>} CORETIMER_OBJECT ;

    <#lt>void CORETIMER_Initialize( void );
    <#lt>void CORETIMER_CallbackSet ( CORETIMER_CALLBACK callback, uintptr_t context );
    <#lt>uint32_t CORETIMER_FrequencyGet ( void );
    <#lt>void CORETIMER_Start();
    <#lt>void CORETIMER_Stop();
    <#lt>uint32_t CORETIMER_CounterGet();
    <#lt>void CORETIMER_CompareSet(uint32_t compare);

    <#lt>void CORETIMER_DelayMs ( uint32_t delay_ms);
    <#lt>void CORETIMER_DelayUs ( uint32_t delay_us);
</#if>

<#if CORE_TIMER_INTERRUPT_MODE == false>
    <#lt>void CORETIMER_Initialize();
    <#lt>void CORETIMER_DelayMs ( uint32_t delay_ms);
    <#lt>void CORETIMER_DelayUs ( uint32_t delay_us);
</#if>

#ifdef __cplusplus // Provide C++ Compatibility
 }
#endif

#endif
