/*******************************************************************************
  Real Time Counter (${RTC_INSTANCE_NAME}) PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${RTC_INSTANCE_NAME?lower_case}_timer.c

  Summary:
    ${RTC_INSTANCE_NAME} PLIB Implementation file

  Description:
    This file defines the interface to the RTC peripheral library. This
    library provides access to and control of the associated peripheral
    instance in timer mode.

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

#include "plib_${RTC_INSTANCE_NAME?lower_case}.h"
#include "device.h"
#include <stdlib.h>

<#if ( RTC_MODE0_INTERRUPT = true && RTC_MODULE_SELECTION = "MODE0" ) ||
     ( RTC_MODE1_INTERRUPT = true && RTC_MODULE_SELECTION = "MODE1" ) >
    <#lt>RTC_OBJECT ${RTC_INSTANCE_NAME?lower_case}Obj;

</#if>

void ${RTC_INSTANCE_NAME}_Initialize(void)
{
    ${RTC_INSTANCE_NAME}_REGS->${RTC_MODULE_SELECTION}.RTC_CTRL = RTC_${RTC_MODULE_SELECTION}_CTRL_SWRST_Msk;
    
    while((${RTC_INSTANCE_NAME}_REGS->${RTC_MODULE_SELECTION}.RTC_STATUS & RTC_STATUS_SYNCBUSY_Msk) == RTC_STATUS_SYNCBUSY_Msk)
    {
        /* Wait for Synchronization after Software Reset */
    }
    
    ${RTC_INSTANCE_NAME}_REGS->${RTC_MODULE_SELECTION}.RTC_READREQ |= RTC_READREQ_RCONT_Msk;

    <#if RTC_MODULE_SELECTION = "MODE0">
    <@compress single_line=true>${RTC_INSTANCE_NAME}_REGS->MODE0.RTC_CTRL = RTC_MODE0_CTRL_MODE(0) |
                                                            RTC_MODE0_CTRL_PRESCALER(${RTC_MODE0_PRESCALER})
                                                            ${RTC_MODE0_MATCHCLR?then("|RTC_MODE0_CTRL_MATCHCLR_Msk", "")};</@compress>


    ${RTC_INSTANCE_NAME}_REGS->MODE0.RTC_COMP = 0x${RTC_MODE0_TIMER_COMPARE};
        <#if RTC_MODE0_EVCTRL != "0">
            <#lt>${RTC_INSTANCE_NAME}_REGS->MODE0.RTC_EVCTRL = 0x${RTC_MODE0_EVCTRL};
        </#if>
    <#else>
        <#lt>   <@compress single_line=true>${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_CTRL = RTC_MODE1_CTRL_MODE(1) |
        <#lt>                                                        RTC_MODE1_CTRL_PRESCALER(${RTC_MODE1_PRESCALER}) |
        <#lt>                                                        RTC_MODE1_CTRL_COUNTSYNC_Msk;</@compress>
        <#lt>   ${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_COMP[0] = 0x${RTC_MODE1_COMPARE0_MATCH_VALUE};
        <#lt>   ${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_COMP[1] = 0x${RTC_MODE1_COMPARE1_MATCH_VALUE};
        <#lt>   ${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_PER = 0x${RTC_MODE1_TIMER_COUNTER_PERIOD};
        <#if    RTC_MODE1_EVCTRL != "0">
            <#lt>   ${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_EVCTRL = 0x${RTC_MODE1_EVCTRL};
        </#if>
    </#if>
}

<#if RTC_FREQCORR >
    <#lt>void ${RTC_INSTANCE_NAME}_FrequencyCorrect (int8_t correction)
    <#lt>{
    <#lt>    uint32_t newCorrectionValue = 0;

    <#lt>    newCorrectionValue = abs(correction);
        
    <#lt>    /* Convert to positive value and adjust register sign bit. */
    <#lt>    if (correction < 0)
    <#lt>    {
    <#lt>        newCorrectionValue |= RTC_FREQCORR_SIGN_Msk;
    <#lt>    }
        
    <#lt>    ${RTC_INSTANCE_NAME}_REGS->${RTC_MODULE_SELECTION}.RTC_FREQCORR = newCorrectionValue;
    <#lt>    while((${RTC_INSTANCE_NAME}_REGS->${RTC_MODULE_SELECTION}.RTC_STATUS & RTC_STATUS_SYNCBUSY_Msk) == RTC_STATUS_SYNCBUSY_Msk)
    <#lt>    {
    <#lt>        /* Wait for Synchronization after writing Value to FREQCORR */
    <#lt>    }
    <#lt>}
</#if>
<#if RTC_MODE0_INTERRUPT = false && RTC_MODULE_SELECTION = "MODE0" ||
     RTC_MODE1_INTERRUPT = false && RTC_MODULE_SELECTION = "MODE1" >

    <#lt>bool ${RTC_INSTANCE_NAME}_PeriodicIntervalHasCompleted (RTC_PERIODIC_INT_MASK period)
    <#lt>{
    <#lt>   bool periodIntervalComplete = false;
        <#if RTC_MODULE_SELECTION = "MODE0" >
    <#lt>   if( (${RTC_INSTANCE_NAME}_REGS->MODE0.RTC_INTFLAG & period) == period)
    <#lt>   {
    <#lt>       periodIntervalComplete = true;

    <#lt>       /* Clear Periodic Interval Interrupt */
    <#lt>       ${RTC_INSTANCE_NAME}_REGS->MODE0.RTC_INTFLAG = period;
    <#lt>   }
        <#elseif RTC_MODULE_SELECTION = "MODE1" >
    <#lt>   if( (${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_INTFLAG & period) == period)
    <#lt>   {
    <#lt>       periodIntervalComplete = true;

    <#lt>       /* Clear Periodic Interval Interrupt */
    <#lt>       ${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_INTFLAG = period;
    <#lt>   }
        </#if>

    <#lt>    return periodIntervalComplete;
    <#lt>}

    <#if RTC_MODULE_SELECTION = "MODE0">

    <#lt>bool ${RTC_INSTANCE_NAME}_Timer32CompareHasMatched(void)
    <#lt>{
    <#lt>   bool status = false;

    <#lt>   if((${RTC_INSTANCE_NAME}_REGS->MODE0.RTC_INTFLAG & RTC_MODE0_INTFLAG_CMP0_Msk) == RTC_MODE0_INTFLAG_CMP0_Msk)
    <#lt>   {
    <#lt>       status = true;
    <#lt>       ${RTC_INSTANCE_NAME}_REGS->MODE0.RTC_INTFLAG = RTC_MODE0_INTFLAG_CMP0_Msk;
    <#lt>   }

    <#lt>   return status;
    <#lt>}

    <#lt>bool ${RTC_INSTANCE_NAME}_Timer32CounterHasOverflowed ( void )
    <#lt>{
    <#lt>   bool status = false;

    <#lt>   if((${RTC_INSTANCE_NAME}_REGS->MODE0.RTC_INTFLAG & RTC_MODE0_INTFLAG_OVF_Msk) == RTC_MODE0_INTFLAG_OVF_Msk)
    <#lt>   {
    <#lt>       status = true;
    <#lt>       ${RTC_INSTANCE_NAME}_REGS->MODE0.RTC_INTFLAG = RTC_MODE0_INTFLAG_OVF_Msk;
    <#lt>   }

    <#lt>   return status;
    <#lt>}
    </#if>

    <#if RTC_MODULE_SELECTION = "MODE1">

    <#lt>bool ${RTC_INSTANCE_NAME}_Timer16PeriodHasExpired ( void )
    <#lt>{
    <#lt>   bool status = false;

    <#lt>   if((${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_INTFLAG & RTC_MODE1_INTFLAG_OVF_Msk ) == RTC_MODE1_INTFLAG_OVF_Msk)
    <#lt>   {
    <#lt>       status = true;
    <#lt>       ${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_INTFLAG = RTC_MODE1_INTFLAG_OVF_Msk;
    <#lt>   }
    <#lt>   return status;
    <#lt>}

    <#lt>bool ${RTC_INSTANCE_NAME}_Timer16CounterHasOverflowed ( void )
    <#lt>{
    <#lt>   bool status = false;

    <#lt>   if((${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_INTFLAG & RTC_MODE1_INTFLAG_OVF_Msk ) == RTC_MODE1_INTFLAG_OVF_Msk)
    <#lt>   {
    <#lt>       status = true;
    <#lt>            
    <#lt>       /* Clear Counter Overflow Interrupt */
    <#lt>       ${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_INTFLAG = RTC_MODE1_INTFLAG_OVF_Msk;
    <#lt>   }

    <#lt>   return status;
    <#lt>}

    <#lt>bool ${RTC_INSTANCE_NAME}_Timer16Compare0HasMatched(void)
    <#lt>{
    <#lt>   bool status = false;

    <#lt>   if((${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_INTFLAG & RTC_MODE1_INTFLAG_CMP0_Msk ) == RTC_MODE1_INTFLAG_CMP0_Msk)
    <#lt>   {
    <#lt>       status = true;

    <#lt>       /* Clear Compare 0 Match Flag */
    <#lt>       ${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_INTFLAG = RTC_MODE1_INTFLAG_CMP0_Msk;
    <#lt>   }

    <#lt>   return status;
    <#lt>}

    <#lt>bool ${RTC_INSTANCE_NAME}_Timer16Compare1HasMatched(void)
    <#lt>{
    <#lt>   bool status = false;

    <#lt>   if((${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_INTFLAG & RTC_MODE1_INTFLAG_CMP1_Msk ) == RTC_MODE1_INTFLAG_CMP1_Msk)
    <#lt>   {
    <#lt>       status = true;

    <#lt>       /* Clear Compare 1 Match Flag */
    <#lt>       ${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_INTFLAG = RTC_MODE1_INTFLAG_CMP1_Msk;
    <#lt>   }

    <#lt>   return status;
    <#lt>}
    </#if>
</#if>
<#if RTC_MODULE_SELECTION = "MODE0">

    <#lt>void ${RTC_INSTANCE_NAME}_Timer32Start ( void )
    <#lt>{
    <#lt>    ${RTC_INSTANCE_NAME}_REGS->MODE0.RTC_CTRL |= RTC_MODE0_CTRL_ENABLE_Msk;
        
    <#lt>    while((${RTC_INSTANCE_NAME}_REGS->${RTC_MODULE_SELECTION}.RTC_STATUS & RTC_STATUS_SYNCBUSY_Msk) == RTC_STATUS_SYNCBUSY_Msk)
    <#lt>    {
    <#lt>        /* Wait for synchronization after Enabling RTC */
    <#lt>    }
    <#lt>}


    <#lt>void ${RTC_INSTANCE_NAME}_Timer32Stop ( void )
    <#lt>{
    <#lt>    ${RTC_INSTANCE_NAME}_REGS->MODE0.RTC_CTRL &= ~(RTC_MODE0_CTRL_ENABLE_Msk);

    <#lt>    while((${RTC_INSTANCE_NAME}_REGS->${RTC_MODULE_SELECTION}.RTC_STATUS & RTC_STATUS_SYNCBUSY_Msk) == RTC_STATUS_SYNCBUSY_Msk)
    <#lt>    {
    <#lt>        /* Wait for Synchronization after Disabling RTC */
    <#lt>    }
    <#lt>}

    <#lt>void ${RTC_INSTANCE_NAME}_Timer32CounterSet ( uint32_t count )
    <#lt>{
    <#lt>    ${RTC_INSTANCE_NAME}_REGS->MODE0.RTC_COUNT = count;

    <#lt>    while((${RTC_INSTANCE_NAME}_REGS->${RTC_MODULE_SELECTION}.RTC_STATUS & RTC_STATUS_SYNCBUSY_Msk) == RTC_STATUS_SYNCBUSY_Msk)
    <#lt>    {
    <#lt>        /* Wait for Synchronization after writing value to Count Register */
    <#lt>    }
    <#lt>}


    <#lt>void ${RTC_INSTANCE_NAME}_Timer32CompareSet ( uint32_t compareValue )
    <#lt>{
    <#lt>    ${RTC_INSTANCE_NAME}_REGS->MODE0.RTC_COMP = compareValue;

    <#lt>    while((${RTC_INSTANCE_NAME}_REGS->${RTC_MODULE_SELECTION}.RTC_STATUS & RTC_STATUS_SYNCBUSY_Msk) == RTC_STATUS_SYNCBUSY_Msk)
    <#lt>    {
    <#lt>        /* Wait for Synchronization after writing Compare Value */
    <#lt>    }
    <#lt>}

    <#lt>uint32_t ${RTC_INSTANCE_NAME}_Timer32CounterGet ( void )
    <#lt>{
    <#lt>    while((${RTC_INSTANCE_NAME}_REGS->${RTC_MODULE_SELECTION}.RTC_STATUS & RTC_STATUS_SYNCBUSY_Msk) == RTC_STATUS_SYNCBUSY_Msk)
    <#lt>    {
    <#lt>        /* Wait for Synchronization before reading value from Count Register */
    <#lt>    }
        
    <#lt>    return(${RTC_INSTANCE_NAME}_REGS->MODE0.RTC_COUNT);
    <#lt>}

    <#lt>uint32_t ${RTC_INSTANCE_NAME}_Timer32PeriodGet ( void )
    <#lt>{
    <#lt>    /* Get 32Bit Compare Value */
    <#lt>    return (RTC_MODE0_COUNT_COUNT_Msk);
    <#lt>}

    <#lt>uint32_t ${RTC_INSTANCE_NAME}_Timer32FrequencyGet ( void )
    <#lt>{
    <#lt>    /* Return Frequency of RTC Clock */
    <#lt>    return RTC_COUNTER_CLOCK_FREQUENCY;
    <#lt>}

    <#if RTC_MODE0_INTERRUPT = true>
        <#lt>void ${RTC_INSTANCE_NAME}_Timer32InterruptEnable(RTC_TIMER32_INT_MASK interrupt)
        <#lt>{
        <#lt>    ${RTC_INSTANCE_NAME}_REGS->MODE0.RTC_INTENSET = interrupt;
        <#lt>}

        <#lt>void ${RTC_INSTANCE_NAME}_Timer32InterruptDisable(RTC_TIMER32_INT_MASK interrupt)
        <#lt>{
        <#lt>    ${RTC_INSTANCE_NAME}_REGS->MODE0.RTC_INTENCLR = interrupt;
        <#lt>}
            
    </#if>
<#else>

    <#lt>void ${RTC_INSTANCE_NAME}_Timer16Start ( void )
    <#lt>{
    <#lt>    ${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_CTRL |= RTC_MODE1_CTRL_ENABLE_Msk;

    <#lt>    while((${RTC_INSTANCE_NAME}_REGS->${RTC_MODULE_SELECTION}.RTC_STATUS & RTC_STATUS_SYNCBUSY_Msk) == RTC_STATUS_SYNCBUSY_Msk)
    <#lt>    {
    <#lt>        /* Wait for Synchronization after Enabling RTC */
    <#lt>    }
    <#lt>}

    <#lt>void ${RTC_INSTANCE_NAME}_Timer16Stop ( void )
    <#lt>{
    <#lt>    ${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_CTRL &= ~(RTC_MODE1_CTRL_ENABLE_Msk);

    <#lt>    while((${RTC_INSTANCE_NAME}_REGS->${RTC_MODULE_SELECTION}.RTC_STATUS & RTC_STATUS_SYNCBUSY_Msk) == RTC_STATUS_SYNCBUSY_Msk)
    <#lt>    {
    <#lt>        /* Wait for Synchronization after Disabling RTC */
    <#lt>    }
    <#lt>}


    <#lt>void ${RTC_INSTANCE_NAME}_Timer16CounterSet ( uint16_t count )
    <#lt>{
    <#lt>    ${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_COUNT = count;

    <#lt>    while((${RTC_INSTANCE_NAME}_REGS->${RTC_MODULE_SELECTION}.RTC_STATUS & RTC_STATUS_SYNCBUSY_Msk) == RTC_STATUS_SYNCBUSY_Msk)
    <#lt>    {
    <#lt>        /* Wait for Synchronization after writing value to Count Register */
    <#lt>    }
    <#lt>}


    <#lt>void ${RTC_INSTANCE_NAME}_Timer16PeriodSet ( uint16_t period )
    <#lt>{
    <#lt>    ${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_PER = period;

    <#lt>    while((${RTC_INSTANCE_NAME}_REGS->${RTC_MODULE_SELECTION}.RTC_STATUS & RTC_STATUS_SYNCBUSY_Msk) == RTC_STATUS_SYNCBUSY_Msk)
    <#lt>    {
    <#lt>        /* Wait for Synchronization after writing Counter Period */
    <#lt>    }
    <#lt>}

    <#lt>uint16_t ${RTC_INSTANCE_NAME}_Timer16CounterGet ( void )
    <#lt>{
    <#lt>    while((${RTC_INSTANCE_NAME}_REGS->${RTC_MODULE_SELECTION}.RTC_STATUS & RTC_STATUS_SYNCBUSY_Msk) == RTC_STATUS_SYNCBUSY_Msk)
    <#lt>    {
    <#lt>        /* Wait for Synchronization after reading value from Count Register */
    <#lt>    }
    <#lt>    return (${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_COUNT);
    <#lt>}

    <#lt>uint16_t ${RTC_INSTANCE_NAME}_Timer16PeriodGet ( void )
    <#lt>{
    <#lt>    return (${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_PER);
    <#lt>}

    <#lt>void ${RTC_INSTANCE_NAME}_Timer16Compare0Set ( uint16_t comparisionValue )
    <#lt>{
    <#lt>   ${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_COMP[0] = comparisionValue;

    <#lt>   while((${RTC_INSTANCE_NAME}_REGS->${RTC_MODULE_SELECTION}.RTC_STATUS & RTC_STATUS_SYNCBUSY_Msk) == RTC_STATUS_SYNCBUSY_Msk)
    <#lt>   {
    <#lt>       /* Wait for Synchronization after writing Compare Value */
    <#lt>   }
    <#lt>}

    <#lt>void ${RTC_INSTANCE_NAME}_Timer16Compare1Set ( uint16_t comparisionValue )
    <#lt>{
    <#lt>   ${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_COMP[1] = comparisionValue;

    <#lt>   while((${RTC_INSTANCE_NAME}_REGS->${RTC_MODULE_SELECTION}.RTC_STATUS & RTC_STATUS_SYNCBUSY_Msk) == RTC_STATUS_SYNCBUSY_Msk)
    <#lt>   {
    <#lt>       /* Wait for Synchronization after writing Compare Value */
    <#lt>   }
    <#lt>}

    <#lt>uint32_t ${RTC_INSTANCE_NAME}_Timer16FrequencyGet ( void )
    <#lt>{
    <#lt>    return RTC_COUNTER_CLOCK_FREQUENCY;
    <#lt>}

    <#if RTC_MODE1_INTERRUPT = true>

        <#lt>void ${RTC_INSTANCE_NAME}_Timer16InterruptEnable(RTC_TIMER16_INT_MASK interrupt)
        <#lt>{
        <#lt>    ${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_INTENSET = interrupt;
        <#lt>}

        <#lt>void ${RTC_INSTANCE_NAME}_Timer16InterruptDisable(RTC_TIMER16_INT_MASK interrupt)
        <#lt>{
        <#lt>    ${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_INTENCLR = interrupt;
        <#lt>}

    </#if>
</#if>

<#if ( RTC_MODE0_INTERRUPT = true && RTC_MODULE_SELECTION = "MODE0" ) ||
     ( RTC_MODE1_INTERRUPT = true && RTC_MODULE_SELECTION = "MODE1" ) >
    <#if RTC_MODULE_SELECTION = "MODE0" >
        <#lt>void ${RTC_INSTANCE_NAME}_Timer32CallbackRegister ( RTC_TIMER32_CALLBACK callback, uintptr_t context )
        <#lt>{
        <#lt>    ${RTC_INSTANCE_NAME?lower_case}Obj.timer32BitCallback = callback;
        <#lt>    ${RTC_INSTANCE_NAME?lower_case}Obj.context            = context;
        <#lt>}
    <#else>

        <#lt>void ${RTC_INSTANCE_NAME}_Timer16CallbackRegister ( RTC_TIMER16_CALLBACK callback, uintptr_t context )
        <#lt>{
        <#lt>    ${RTC_INSTANCE_NAME?lower_case}Obj.timer16BitCallback = callback;
        <#lt>    ${RTC_INSTANCE_NAME?lower_case}Obj.context            = context;
        <#lt>}
    </#if>

    <#lt>void ${RTC_INSTANCE_NAME}_InterruptHandler(void)
    <#lt>{
    <#if RTC_MODULE_SELECTION = "MODE0">
        <#lt>    ${RTC_INSTANCE_NAME?lower_case}Obj.timer32intCause = ${RTC_INSTANCE_NAME}_REGS->MODE0.RTC_INTFLAG;

        <#lt>    /* Invoke registered Callback function */
        <#lt>    if(${RTC_INSTANCE_NAME?lower_case}Obj.timer32BitCallback != NULL)
        <#lt>    {
        <#lt>        ${RTC_INSTANCE_NAME?lower_case}Obj.timer32BitCallback( ${RTC_INSTANCE_NAME?lower_case}Obj.timer32intCause, ${RTC_INSTANCE_NAME?lower_case}Obj.context );
        <#lt>    }
            
        <#lt>    ${RTC_INSTANCE_NAME}_REGS->MODE0.RTC_INTFLAG = RTC_MODE0_INTFLAG_Msk;
    <#else>
        <#lt>    /* Update the event in RTC Peripheral Callback object */
        <#lt>    ${RTC_INSTANCE_NAME?lower_case}Obj.timer16intCause = ${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_INTFLAG;

        <#lt>    /* Invoke registered Callback function */
        <#lt>    if(${RTC_INSTANCE_NAME?lower_case}Obj.timer16BitCallback != NULL)
        <#lt>    {
        <#lt>        ${RTC_INSTANCE_NAME?lower_case}Obj.timer16BitCallback( ${RTC_INSTANCE_NAME?lower_case}Obj.timer16intCause, ${RTC_INSTANCE_NAME?lower_case}Obj.context );
        <#lt>    }

        <#lt>    ${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_INTFLAG = RTC_MODE1_INTFLAG_Msk;
    </#if>
    <#lt>}
</#if>
