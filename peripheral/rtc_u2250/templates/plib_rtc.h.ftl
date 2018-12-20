/*******************************************************************************
  Real Time Counter (${RTC_INSTANCE_NAME}) PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${RTC_INSTANCE_NAME?lower_case}.h

  Summary:
    ${RTC_INSTANCE_NAME} PLIB Header file

  Description:
    This file defines the interface to the RTC peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

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

#ifndef PLIB_${RTC_INSTANCE_NAME}_H
#define PLIB_${RTC_INSTANCE_NAME}_H

#include "device.h"
#include <stddef.h>
#include <stdbool.h>
#include <stdint.h>
<#if RTC_MODULE_SELECTION ="MODE2">
#include <time.h>
</#if>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility
extern "C" {
#endif
// DOM-IGNORE-END

<#if RTC_MODULE_SELECTION = "MODE0">
    <#lt>/* Frequency of Counter Clock for RTC */
    <#if RTC_MODE0_PRESCALER = "0x0">
        <#lt>#define RTC_COUNTER_CLOCK_FREQUENCY         0
    <#else>
        <#lt>#define RTC_COUNTER_CLOCK_FREQUENCY        (${core.RTC_CLOCK_FREQUENCY} / (1 << (${RTC_MODE0_PRESCALER} - 1)))
    </#if>
<#elseif RTC_MODULE_SELECTION = "MODE1">
    <#lt>/* Frequency of Counter Clock for RTC */
    <#if RTC_MODE1_PRESCALER = "0x0">
        <#lt>#define RTC_COUNTER_CLOCK_FREQUENCY         0
    <#else>
        <#lt>#define RTC_COUNTER_CLOCK_FREQUENCY        (${core.RTC_CLOCK_FREQUENCY} / (1 << (${RTC_MODE1_PRESCALER} - 1)))
    </#if>
</#if>

<#if RTC_MODE2_INTERRUPT = true && RTC_MODULE_SELECTION = "MODE2" ||
     RTC_MODE1_INTERRUPT = true && RTC_MODULE_SELECTION = "MODE1" ||
     RTC_MODE0_INTERRUPT = true && RTC_MODULE_SELECTION = "MODE0" >
    <#if RTC_MODULE_SELECTION = "MODE2">
        <#lt>typedef enum
        <#lt>{
        <#lt>    RTC_ALARM_MASK_SS = 0x1,    //Alarm every minute
        <#lt>    RTC_ALARM_MASK_MMSS,        //Alarm every Hour
        <#lt>    RTC_ALARM_MASK_HHMMSS,      //Alarm Every Day
        <#lt>    RTC_ALARM_MASK_DDHHMMSS,    //Alarm Every Month
        <#lt>    RTC_ALARM_MASK_MMDDHHMMSS,  //Alarm Every year
        <#lt>    RTC_ALARM_MASK_YYMMDDHHMMSS //Alarm Once
        <#lt>} RTC_ALARM_MASK;

        <#lt>typedef enum
        <#lt>{<#list 0..(RTC_MODE2_INT - 1) as i>
            <#assign interruptName = "RTC_MODE2_" + i>
                <#lt>    RTC_CLOCK_INT_MASK_${.vars[interruptName]} = RTC_MODE2_INTENSET_${.vars[interruptName]}_Msk,</#list>
                <#lt>   /* Force the compiler to reserve 32-bit memory for enum */
                <#lt>    RTC_CLOCK_INT_MASK_INVALID = 0xFFFFFFFF
        <#lt>} RTC_CLOCK_INT_MASK;

    <#elseif RTC_MODULE_SELECTION = "MODE0">
        <#lt>typedef enum
        <#lt>{<#list 0..(RTC_MODE0_INT - 1) as i>
            <#assign interruptName = "RTC_MODE0_" + i>
                <#lt>    RTC_TIMER32_INT_MASK_${.vars[interruptName]} = RTC_MODE0_INTENSET_${.vars[interruptName]}_Msk,</#list>
                <#lt>   /* Force the compiler to reserve 32-bit memory for enum */
                <#lt>    RTC_TIMER32_INT_MASK_INVALID = 0xFFFFFFFF
        <#lt>} RTC_TIMER32_INT_MASK;
    <#else>
        <#lt>typedef enum
        <#lt>{
        <#list 0..(RTC_MODE1_INT - 1) as i>
            <#assign interruptName = "RTC_MODE1_" + i>
                <#lt>    RTC_TIMER16_INT_MASK_${.vars[interruptName]} = RTC_MODE1_INTENSET_${.vars[interruptName]}_Msk,</#list>
                <#lt>   /* Force the compiler to reserve 32-bit memory for enum */
                <#lt>    RTC_TIMER16_INT_MASK_INVALID = 0xFFFFFFFF
        <#lt>} RTC_TIMER16_INT_MASK;
    </#if>
    <#else>
        <#lt>typedef enum
        <#lt>{
        <#lt>    RTC_PER0_MASK = 0x0001,
        <#lt>    RTC_PER1_MASK = 0x0002,
        <#lt>    RTC_PER2_MASK = 0x0004,
        <#lt>    RTC_PER3_MASK = 0x0008,
        <#lt>    RTC_PER4_MASK = 0x0010,
        <#lt>    RTC_PER5_MASK = 0x0020,
        <#lt>    RTC_PER6_MASK = 0x0040,
        <#lt>    RTC_PER7_MASK = 0x0080
        <#lt>} RTC_PERIODIC_INT_MASK;
</#if>
<#if TAMP_DETECTION_SUPPORTED??>
    <#if TAMP_DETECTION_SUPPORTED>
        <#lt>typedef enum
        <#lt>{
        <#lt>    BACKUP_REGISTER_0 = 0,
        <#lt>    BACKUP_REGISTER_1 = 1,
        <#lt>    BACKUP_REGISTER_2 = 2,
        <#lt>    BACKUP_REGISTER_3 = 3,
        <#lt>    BACKUP_REGISTER_4 = 4,
        <#lt>    BACKUP_REGISTER_5 = 5,
        <#lt>    BACKUP_REGISTER_6 = 6,
        <#lt>    BACKUP_REGISTER_7 = 7
        <#lt>} BACKUP_REGISTER;

        <#lt>typedef enum
        <#lt>{
        <#lt>    TAMPER_CHANNEL_0 = 0,
        <#lt>    TAMPER_CHANNEL_1 = 1,
        <#lt>    TAMPER_CHANNEL_2 = 2,
        <#lt>    TAMPER_CHANNEL_3 = 3,
        <#lt>    TAMPER_CHANNEL_4 = 4
        <#lt>} TAMPER_CHANNEL;
    </#if>
</#if>
<#if RTC_MODE2_INTERRUPT = true && RTC_MODULE_SELECTION = "MODE2" ||
     RTC_MODE1_INTERRUPT = true && RTC_MODULE_SELECTION = "MODE1" ||
     RTC_MODE0_INTERRUPT = true && RTC_MODULE_SELECTION = "MODE0" >
    <#if RTC_MODULE_SELECTION = "MODE0" >
        <#lt>typedef void (*RTC_TIMER32_CALLBACK)( RTC_TIMER32_INT_MASK intCause, uintptr_t context );
    <#elseif RTC_MODULE_SELECTION = "MODE2">
        <#lt>typedef void (*RTC_CALLBACK)( RTC_CLOCK_INT_MASK intCause, uintptr_t context );
    <#else>
        <#lt>typedef void (*RTC_TIMER16_CALLBACK)( RTC_TIMER16_INT_MASK intCause, uintptr_t context );
    </#if>
</#if>

<#if ( RTC_MODE0_INTERRUPT = true && RTC_MODULE_SELECTION = "MODE0" ) ||
     ( RTC_MODE1_INTERRUPT = true && RTC_MODULE_SELECTION = "MODE1" ) ||
     ( RTC_MODE2_INTERRUPT = true && RTC_MODULE_SELECTION = "MODE2" )>
typedef struct
{
<#if RTC_MODULE_SELECTION = "MODE0" >
    /* Timer 32Bit */
    RTC_TIMER32_CALLBACK timer32BitCallback;
    RTC_TIMER32_INT_MASK timer32intCause;
<#elseif RTC_MODULE_SELECTION = "MODE1">
    /* Timer 16Bit */
    RTC_TIMER16_CALLBACK timer16BitCallback;
    RTC_TIMER16_INT_MASK timer16intCause;
<#else>
    /* RTC Clock*/
    RTC_CLOCK_INT_MASK intCause;
    RTC_CALLBACK alarmCallback;
</#if>
    uintptr_t context;
} RTC_OBJECT;
</#if>

void ${RTC_INSTANCE_NAME}_Initialize(void);
<#if RTC_FREQCORR>
    <#lt>void ${RTC_INSTANCE_NAME}_FrequencyCorrect ( int8_t correction );
</#if>
<#if RTC_MODE0_INTERRUPT = false && RTC_MODULE_SELECTION = "MODE0" ||
     RTC_MODE1_INTERRUPT = false && RTC_MODULE_SELECTION = "MODE1" >
    <#lt>bool ${RTC_INSTANCE_NAME}_PeriodicIntervalHasCompleted ( RTC_PERIODIC_INT_MASK period );
</#if>
<#if RTC_MODULE_SELECTION = "MODE0">
    <#if RTC_MODE0_INTERRUPT = false>
        <#lt>bool ${RTC_INSTANCE_NAME}_Timer32CounterHasOverflowed ( void );
        <#if RTC_MODE0_NUM_COMP == 0>
        <#lt>bool ${RTC_INSTANCE_NAME}_Timer32CompareHasMatched( void );
        <#else>
        <#list 0..(RTC_MODE0_NUM_COMP - 1) as i>
        <#lt>bool ${RTC_INSTANCE_NAME}_Timer32Compare${i}HasMatched( void );
        </#list>
        </#if>
    </#if>
    <#lt>void ${RTC_INSTANCE_NAME}_Timer32Start ( void );
    <#lt>void ${RTC_INSTANCE_NAME}_Timer32Stop ( void );
    <#lt>void ${RTC_INSTANCE_NAME}_Timer32CounterSet ( uint32_t count );
    <#lt>uint32_t ${RTC_INSTANCE_NAME}_Timer32CounterGet ( void );
    <#lt>uint32_t ${RTC_INSTANCE_NAME}_Timer32FrequencyGet ( void );
    <#if RTC_MODE0_NUM_COMP == 1>
    <#lt>void ${RTC_INSTANCE_NAME}_Timer32CompareSet ( uint32_t compareValue );
    <#else>
    <#list 0..(RTC_MODE0_NUM_COMP - 1) as i>
    <#lt>void ${RTC_INSTANCE_NAME}_Timer32Compare${i}Set ( uint32_t compareValue );
    </#list>
    </#if>
    <#lt>uint32_t ${RTC_INSTANCE_NAME}_Timer32PeriodGet ( void );
    <#if RTC_MODE0_INTERRUPT = true>
        <#lt>void ${RTC_INSTANCE_NAME}_Timer32InterruptEnable( RTC_TIMER32_INT_MASK interrupt );
        <#lt>void ${RTC_INSTANCE_NAME}_Timer32InterruptDisable( RTC_TIMER32_INT_MASK interrupt );
    </#if>
<#elseif RTC_MODULE_SELECTION = "MODE1">
    <#if RTC_MODE1_INTERRUPT = false>
        <#lt>bool ${RTC_INSTANCE_NAME}_Timer16PeriodHasExpired ( void );
        <#lt>bool ${RTC_INSTANCE_NAME}_Timer16CounterHasOverflowed ( void );
        <#list 0..(RTC_MODE1_NUM_COMP - 1) as i>
            <#lt>bool ${RTC_INSTANCE_NAME}_Timer16Compare${i}HasMatched( void );
        </#list>
    </#if>
    <#lt>void ${RTC_INSTANCE_NAME}_Timer16Start ( void );
    <#lt>void ${RTC_INSTANCE_NAME}_Timer16Stop ( void );
    <#lt>void ${RTC_INSTANCE_NAME}_Timer16CounterSet ( uint16_t count );
    <#lt>void ${RTC_INSTANCE_NAME}_Timer16PeriodSet ( uint16_t period );
    <#lt>uint16_t ${RTC_INSTANCE_NAME}_Timer16PeriodGet ( void );
    <#lt>uint16_t ${RTC_INSTANCE_NAME}_Timer16CounterGet ( void );
    <#lt>uint32_t ${RTC_INSTANCE_NAME}_Timer16FrequencyGet ( void );
    <#list 0..(RTC_MODE1_NUM_COMP - 1) as i>
        <#lt>void ${RTC_INSTANCE_NAME}_Timer16Compare${i}Set ( uint16_t comparisionValue );
    </#list>
    <#if RTC_MODE1_INTERRUPT = true>
        <#lt>void ${RTC_INSTANCE_NAME}_Timer16InterruptEnable( RTC_TIMER16_INT_MASK interrupt );
        <#lt>void ${RTC_INSTANCE_NAME}_Timer16InterruptDisable( RTC_TIMER16_INT_MASK interrupt );
    </#if>
<#else>
    <#lt>bool ${RTC_INSTANCE_NAME}_RTCCTimeSet (struct tm * initialTime );
    <#lt>void ${RTC_INSTANCE_NAME}_RTCCTimeGet ( struct tm * currentTime );
    <#if RTC_MODE2_INTERRUPT = true>
        <#if RTC_MODE2_NUM_ALARM == 1>
        <#lt>bool ${RTC_INSTANCE_NAME}_RTCCAlarmSet ( struct tm * alarmTime, RTC_ALARM_MASK mask );
        <#else>
        <#list 0..(RTC_MODE2_NUM_ALARM - 1) as i>
        <#lt>bool ${RTC_INSTANCE_NAME}_RTCCAlarm${i}Set ( struct tm * alarmTime, RTC_ALARM_MASK mask );
        </#list>
        </#if>
    </#if>
</#if>
<#if TAMP_DETECTION_SUPPORTED??>
    <#if TAMP_DETECTION_SUPPORTED>
        <#lt>void ${RTC_INSTANCE_NAME}_BackupRegisterSet( BACKUP_REGISTER reg, uint32_t value );
        <#lt>uint32_t ${RTC_INSTANCE_NAME}_BackupRegisterGet( BACKUP_REGISTER reg );
        <#lt>TAMPER_CHANNEL ${RTC_INSTANCE_NAME}_TamperSourceGet( void );
        <#if RTC_MODULE_SELECTION = "MODE0">
        <#lt>uint32_t ${RTC_INSTANCE_NAME}_Timer32TimeStampGet( void );
        <#elseif RTC_MODULE_SELECTION = "MODE1">
        <#lt>uint16_t ${RTC_INSTANCE_NAME}_Timer16TimeStampGet( void );
        <#else>
        <#lt>void ${RTC_INSTANCE_NAME}_RTCCTimeStampGet( struct tm * timeStamp );
        <#lt>
        </#if>
    </#if>
</#if>
<#if (RTC_MODULE_SELECTION = "MODE0" && RTC_MODE0_INTERRUPT = true) ||
     (RTC_MODULE_SELECTION = "MODE1" && RTC_MODE1_INTERRUPT = true) ||
     (RTC_MODULE_SELECTION = "MODE2" && RTC_MODE2_INTERRUPT = true) >
    <#if RTC_MODULE_SELECTION = "MODE2">
        <#lt>void ${RTC_INSTANCE_NAME}_RTCCCallbackRegister ( RTC_CALLBACK callback, uintptr_t context);
    <#elseif RTC_MODULE_SELECTION = "MODE0">
        <#lt>void ${RTC_INSTANCE_NAME}_Timer32CallbackRegister ( RTC_TIMER32_CALLBACK callback, uintptr_t context );
    <#else>
        <#lt>void ${RTC_INSTANCE_NAME}_Timer16CallbackRegister ( RTC_TIMER16_CALLBACK callback, uintptr_t context );
    </#if>
</#if>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility
}
#endif
// DOM-IGNORE-END

#endif /* PLIB_${RTC_INSTANCE_NAME}_H */
