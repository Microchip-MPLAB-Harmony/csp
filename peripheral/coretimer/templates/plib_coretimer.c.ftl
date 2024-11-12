/*******************************************************************************
  Core Timer Peripheral Library

  Company:
    Microchip Technology Inc.

  File Name:
    plib_coretimer.c

  Summary:
    Core timer Source File

  Description:
    None

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

#include "device.h"
#include "peripheral/coretimer/plib_coretimer.h"
<#if core.CoreSysIntFile == true>
#include "interrupts.h"
</#if>

<#if CORE_TIMER_INTERRUPT_MODE == true && CORE_TIMER_PERIODIC_INTERRUPT == true>
    <#lt>volatile static CORETIMER_OBJECT coreTmr;
    <#lt>
    <#lt>void CORETIMER_Initialize(void)
    <#lt>{
    <#lt>    // Disable Timer by setting Disable Count (DC) bit
    <#lt>    _CP0_SET_CAUSE(_CP0_GET_CAUSE() | _CP0_CAUSE_DC_MASK);
    <#lt>
    <#lt><#if CORE_TIMER_STOP_IN_DEBUG == true>
    <#lt>    _CP0_SET_DEBUG(_CP0_GET_DEBUG() & ~_CP0_DEBUG_COUNTDM_MASK);
    <#lt></#if>
    <#lt>
    <#lt>    coreTmr.period=CORE_TIMER_INTERRUPT_PERIOD_VALUE;
    <#lt>    coreTmr.tickCounter = 0;
    <#lt>    coreTmr.callback = NULL;
    <#lt><#if CORE_TIMER_AUTOSTART == true>
    <#lt>    CORETIMER_Start();
    <#lt></#if>
    <#lt>}
    <#lt>
    <#lt>void CORETIMER_CallbackSet ( CORETIMER_CALLBACK callback, uintptr_t context )
    <#lt>{
    <#lt>    coreTmr.callback = callback;
    <#lt>    coreTmr.context = context;
    <#lt>}
    <#lt>
    <#lt>void CORETIMER_PeriodSet ( uint32_t period )
    <#lt>{
    <#lt>    coreTmr.period = period;
    <#lt>
    <#lt>}
    <#lt>
    <#lt>void CORETIMER_Start(void)
    <#lt>{
    <#lt>    // Disable Timer by setting Disable Count (DC) bit
    <#lt>    _CP0_SET_CAUSE(_CP0_GET_CAUSE() | _CP0_CAUSE_DC_MASK);
    <#lt>
    <#lt>    // Disable Interrupt
    <#lt>    ${CORE_TIMER_IEC_REG}CLR=${CORE_TIMER_IEC_REG_VALUE};
    <#lt>
    <#lt>    // Clear Core Timer
    <#lt>    _CP0_SET_COUNT(0);
    <#lt>    _CP0_SET_COMPARE(coreTmr.period);
    <#lt>
    <#lt>    // Enable Timer by clearing Disable Count (DC) bit
    <#lt>    _CP0_SET_CAUSE(_CP0_GET_CAUSE() & (~_CP0_CAUSE_DC_MASK));
    <#lt>
    <#lt>    // Enable Interrupt
    <#lt>    ${CORE_TIMER_IEC_REG}SET=${CORE_TIMER_IEC_REG_VALUE};
    <#lt>}
    <#lt>
    <#lt>void CORETIMER_Stop( void )
    <#lt>{
    <#lt>    // Disable Timer by setting Disable Count (DC) bit
    <#lt>    _CP0_SET_CAUSE(_CP0_GET_CAUSE() | _CP0_CAUSE_DC_MASK);
    <#lt>
    <#lt>    // Disable Interrupt
    <#lt>    ${CORE_TIMER_IEC_REG}CLR=${CORE_TIMER_IEC_REG_VALUE};
    <#lt>}
    <#lt>
    <#lt>
    <#lt>uint32_t CORETIMER_FrequencyGet ( void )
    <#lt>{
    <#lt>    return (CORE_TIMER_FREQUENCY);
    <#lt>}
    
    <#lt>uint32_t CORETIMER_GetTickCounter(void)
    <#lt>{
    <#lt>    return coreTmr.tickCounter;
    <#lt>}
    
    <#lt>void CORETIMER_StartTimeOut (CORETIMER_TIMEOUT* timeout, uint32_t delay_ms)
    <#lt>{
    <#lt>    timeout->start = CORETIMER_GetTickCounter();
    <#lt>    timeout->count = (delay_ms*1000U)/CORE_TIMER_INTERRUPT_PERIOD_IN_US;
    <#lt>}
    
    <#lt>void CORETIMER_ResetTimeOut (CORETIMER_TIMEOUT* timeout)
    <#lt>{
    <#lt>    timeout->start = CORETIMER_GetTickCounter();
    <#lt>}
    
    <#lt>bool CORETIMER_IsTimeoutReached (CORETIMER_TIMEOUT* timeout)
    <#lt>{
    <#lt>    bool valTimeout  = true;
    <#lt>    if ((coreTmr.tickCounter - timeout->start) < timeout->count)
    <#lt>    {
    <#lt>        valTimeout = false;
    <#lt>    }
    <#lt>
    <#lt>    return valTimeout;
    <#lt>
    <#lt>}
    
    <#lt>void __attribute__((used)) CORE_TIMER_InterruptHandler (void)
    <#lt>{
    <#lt>    uint32_t count, newCompare;
    <#lt>    uint32_t status = ${CORE_TIMER_IFS_REG}bits.CTIF;
    <#lt>    ${CORE_TIMER_IFS_REG}CLR = ${CORE_TIMER_IFS_REG_VALUE};
    <#lt>
    <#lt>    // Start Critical Section
    <#lt>    (void) __builtin_disable_interrupts();
    <#lt>
    <#lt>    count=_CP0_GET_COUNT();
    <#lt>
    <#lt>    newCompare=_CP0_GET_COMPARE() + coreTmr.period;
    <#lt>
    <#lt>    if (50U < newCompare-count)
    <#lt>    {
    <#lt>        _CP0_SET_COMPARE(newCompare);
    <#lt>    }
    <#lt>    else
    <#lt>    {
    <#lt>        _CP0_SET_COMPARE(count+50U);
    <#lt>    }
    <#lt>    // End Critical Section
    <#lt>    (void) __builtin_enable_interrupts();
    <#lt>
    <#lt>    coreTmr.tickCounter++;
    <#lt>    if(coreTmr.callback != NULL)
    <#lt>    {
    <#lt>        uintptr_t context = coreTmr.context;
    <#lt>        coreTmr.callback(status, context);
    <#lt>    }
    <#lt>}
</#if>

<#if CORE_TIMER_INTERRUPT_MODE == true && CORE_TIMER_PERIODIC_INTERRUPT == false>
    <#lt>volatile static CORETIMER_OBJECT coreTmr;
    <#lt>
    <#lt>void CORETIMER_Initialize( void )
    <#lt>{
    <#lt>    // Disable Timer by setting Disable Count (DC) bit
    <#lt>    _CP0_SET_CAUSE(_CP0_GET_CAUSE() | _CP0_CAUSE_DC_MASK);
    <#lt>
    <#lt><#if CORE_TIMER_STOP_IN_DEBUG == true>
    <#lt>    _CP0_SET_DEBUG(_CP0_GET_DEBUG() & ~_CP0_DEBUG_COUNTDM_MASK);
    <#lt></#if>
    <#lt>    coreTmr.callback = NULL;
    <#lt>}

    <#lt>void CORETIMER_CallbackSet ( CORETIMER_CALLBACK callback, uintptr_t context )
    <#lt>{
    <#lt>    coreTmr.callback = callback;
    <#lt>    coreTmr.context = context;
    <#lt>}

    <#lt>void CORETIMER_Start( void )
    <#lt>{
    <#lt>    // Disable Timer by setting Disable Count (DC) bit
    <#lt>    _CP0_SET_CAUSE(_CP0_GET_CAUSE() | _CP0_CAUSE_DC_MASK);
    <#lt>
    <#lt>    // Disable Interrupt
    <#lt>    ${CORE_TIMER_IEC_REG}CLR = ${CORE_TIMER_IEC_REG_VALUE};
    <#lt>
    <#lt>    // Clear Core Timer
    <#lt>    _CP0_SET_COUNT(0);
    <#lt>    _CP0_SET_COMPARE(0xFFFFFFFF);
    <#lt>
    <#lt>    // Enable Timer by clearing Disable Count (DC) bit
    <#lt>    _CP0_SET_CAUSE(_CP0_GET_CAUSE() & (~_CP0_CAUSE_DC_MASK));
    <#lt>
    <#lt>    // Enable Interrupt
    <#lt>    ${CORE_TIMER_IEC_REG}SET = ${CORE_TIMER_IEC_REG_VALUE};
    <#lt>}

    <#lt>void CORETIMER_Stop( void )
    <#lt>{
    <#lt>    // Disable Timer by setting Disable Count (DC) bit
    <#lt>    _CP0_SET_CAUSE(_CP0_GET_CAUSE() | _CP0_CAUSE_DC_MASK);
    <#lt>
    <#lt>    // Disable Interrupt
    <#lt>    ${CORE_TIMER_IEC_REG}CLR = ${CORE_TIMER_IEC_REG_VALUE};
    <#lt>}

    <#lt>uint32_t CORETIMER_FrequencyGet ( void )
    <#lt>{
    <#lt>    return (CORE_TIMER_FREQUENCY);
    <#lt>}

    <#lt>void CORETIMER_CompareSet ( uint32_t compare )
    <#lt>{
    <#lt>    _CP0_SET_COMPARE(compare);
    <#lt>}

    <#lt>uint32_t CORETIMER_CounterGet ( void )
    <#lt>{
    <#lt>    uint32_t count;
    <#lt>    count = _CP0_GET_COUNT();
    <#lt>    return count;
    <#lt>}

    <#lt>void __attribute__((used)) CORE_TIMER_InterruptHandler (void)
    <#lt>{
    <#lt>    uint32_t status = ${CORE_TIMER_IFS_REG}bits.CTIF;
    <#lt>    ${CORE_TIMER_IFS_REG}CLR = ${CORE_TIMER_IFS_REG_VALUE};
    <#lt>    if(coreTmr.callback != NULL)
    <#lt>    {
    <#lt>        uintptr_t context = coreTmr.context;
    <#lt>        coreTmr.callback(status, context);
    <#lt>    }
    <#lt>}
</#if>

<#if CORE_TIMER_INTERRUPT_MODE == false >
    <#lt>static uint32_t compareValue = CORE_TIMER_COMPARE_VALUE;

    <#lt>void CORETIMER_Initialize( void )
    <#lt>{
    <#lt><#if CORE_TIMER_STOP_IN_DEBUG == true>
    <#lt>    _CP0_SET_DEBUG(_CP0_GET_DEBUG() & ~_CP0_DEBUG_COUNTDM_MASK);
    <#lt></#if>

    <#lt>    // Clear Core Timer
    <#lt>    _CP0_SET_COUNT(0);
    <#lt>    _CP0_SET_COMPARE(compareValue);

    <#lt>    // Enable Timer by clearing Disable Count (DC) bit
    <#lt>    _CP0_SET_CAUSE(_CP0_GET_CAUSE() & (~_CP0_CAUSE_DC_MASK));
    <#lt>
    <#lt>}

    <#lt>void CORETIMER_Start( void )
    <#lt>{
    <#lt>    // Disable Timer by setting Disable Count (DC) bit
    <#lt>    _CP0_SET_CAUSE(_CP0_GET_CAUSE() | _CP0_CAUSE_DC_MASK);

    <#lt>    // Clear Compare Timer Interrupt Flag
    <#lt>    ${CORE_TIMER_IFS_REG}CLR = ${CORE_TIMER_IFS_REG_VALUE};

    <#lt>    // Clear Core Timer
    <#lt>    _CP0_SET_COUNT(0);

    <#lt>    _CP0_SET_COMPARE(compareValue);

    <#lt>    // Enable Timer by clearing Disable Count (DC) bit
    <#lt>    _CP0_SET_CAUSE(_CP0_GET_CAUSE() & (~_CP0_CAUSE_DC_MASK));

    <#lt>}

    <#lt>void CORETIMER_Stop( void )
    <#lt>{
    <#lt>    // Disable Timer by setting Disable Count (DC) bit
    <#lt>    _CP0_SET_CAUSE(_CP0_GET_CAUSE() | _CP0_CAUSE_DC_MASK);
    <#lt>}

    <#lt>uint32_t CORETIMER_FrequencyGet ( void )
    <#lt>{
    <#lt>    return (CORE_TIMER_FREQUENCY);
    <#lt>}

    <#lt>void CORETIMER_CompareSet ( uint32_t compare )
    <#lt>{
    <#lt>    compareValue = compare;
    <#lt>    _CP0_SET_COMPARE(compareValue);
    <#lt>}

    <#lt>uint32_t CORETIMER_CounterGet ( void )
    <#lt>{
    <#lt>    uint32_t count;
    <#lt>    count = _CP0_GET_COUNT();
    <#lt>    return count;
    <#lt>}

    <#lt>bool CORETIMER_CompareHasExpired( void )
    <#lt>{
    <#lt>    bool flagStatus = false;
    <#lt>    if (${CORE_TIMER_IFS_REG}bits.CTIF != 0U)
    <#lt>    {
    <#lt>       // Clear Compare Timer Interrupt Flag
    <#lt>       ${CORE_TIMER_IFS_REG}CLR = ${CORE_TIMER_IFS_REG_VALUE};
    <#lt>       flagStatus = true;
    <#lt>    }
    <#lt>    return flagStatus;
    <#lt>}
</#if>

void CORETIMER_DelayMs ( uint32_t delay_ms)
{
    uint32_t startCount, endCount;

    /* Calculate the end count for the given delay */
    endCount=(CORE_TIMER_FREQUENCY / 1000U) * delay_ms;

    startCount=_CP0_GET_COUNT();
    while((_CP0_GET_COUNT() - startCount) < endCount)
    {
        /* Wait for compare match */
    }
}

void CORETIMER_DelayUs ( uint32_t delay_us)
{
    uint32_t startCount, endCount;

    /* Calculate the end count for the given delay */
    endCount=(CORE_TIMER_FREQUENCY / 1000000U) * delay_us;

    startCount=_CP0_GET_COUNT();
    while((_CP0_GET_COUNT() - startCount) < endCount)
    {
        /* Wait for compare match */
    }
}

