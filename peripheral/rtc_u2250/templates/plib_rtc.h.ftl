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
// *****************************************************************************
// *****************************************************************************
// Section:Preprocessor macros
// *****************************************************************************
// *****************************************************************************
// *****************************************************************************

<#if RTC_MODULE_SELECTION = "MODE0">
    <#lt>/* Frequency of Counter Clock for RTC */
    <#if RTC_MODE0_PRESCALER = "0x0">
        <#lt>#define RTC_COUNTER_CLOCK_FREQUENCY         0U
    <#else>
        <#lt>#define RTC_COUNTER_CLOCK_FREQUENCY        (${core.RTC_CLOCK_FREQUENCY}U / (1UL << (${RTC_MODE0_PRESCALER}U - 1U)))
    </#if>
<#elseif RTC_MODULE_SELECTION = "MODE1">
    <#lt>/* Frequency of Counter Clock for RTC */
    <#if RTC_MODE1_PRESCALER = "0x0">
        <#lt>#define RTC_COUNTER_CLOCK_FREQUENCY         0U
    <#else>
        <#lt>#define RTC_COUNTER_CLOCK_FREQUENCY        (${core.RTC_CLOCK_FREQUENCY}U / (1UL << (${RTC_MODE1_PRESCALER}U - 1U)))
    </#if>
</#if>

<#if RTC_MODULE_SELECTION = "MODE2">
    <#lt><#list 0..(RTC_MODE2_INT - 1) as i>
    <#lt><#assign interruptName = "RTC_MODE2_" + i>
#define RTC_CLOCK_INT_MASK_${.vars[interruptName]}  RTC_MODE2_INTENSET_${.vars[interruptName]}_Msk
    <#lt></#list>
#define RTC_CLOCK_INT_MASK_INVALID  0xFFFFFFFFU
<#elseif RTC_MODULE_SELECTION = "MODE0">
    <#lt><#list 0..(RTC_MODE0_INT - 1) as i>
    <#lt><#assign interruptName = "RTC_MODE0_" + i>
#define RTC_TIMER32_INT_MASK_${.vars[interruptName]}  RTC_MODE0_INTENSET_${.vars[interruptName]}_Msk
    <#lt></#list>
#define RTC_TIMER32_INT_MASK_INVALID 0xFFFFFFFFU
<#elseif RTC_MODULE_SELECTION = "MODE1">
    <#lt><#list 0..(RTC_MODE1_INT - 1) as i>
    <#lt><#assign interruptName = "RTC_MODE1_" + i>
#define RTC_TIMER16_INT_MASK_${.vars[interruptName]}  RTC_MODE1_INTENSET_${.vars[interruptName]}_Msk
    <#lt></#list>
#define RTC_TIMER16_INT_MASK_INVALID 0xFFFFFFFFU
</#if>
// *****************************************************************************
// *****************************************************************************
// Section: Data Types
// *****************************************************************************
// *****************************************************************************
// *****************************************************************************

<#if RTC_MODE2_INTERRUPT = true && RTC_MODULE_SELECTION = "MODE2" ||
     RTC_MODE1_INTERRUPT = true && RTC_MODULE_SELECTION = "MODE1" ||
     RTC_MODE0_INTERRUPT = true && RTC_MODULE_SELECTION = "MODE0" >
    <#if RTC_MODULE_SELECTION = "MODE2">
        <#lt>typedef enum
        <#lt>{
        <#lt>    RTC_ALARM_MASK_SS = 0x1U,    //Alarm every minute
        <#lt>    RTC_ALARM_MASK_MMSS,        //Alarm every Hour
        <#lt>    RTC_ALARM_MASK_HHMMSS,      //Alarm Every Day
        <#lt>    RTC_ALARM_MASK_DDHHMMSS,    //Alarm Every Month
        <#lt>    RTC_ALARM_MASK_MMDDHHMMSS,  //Alarm Every year
        <#lt>    RTC_ALARM_MASK_YYMMDDHHMMSS //Alarm Once
        <#lt>} RTC_ALARM_MASK;

        <#lt>typedef uint32_t RTC_CLOCK_INT_MASK;

    <#elseif RTC_MODULE_SELECTION = "MODE0">
        <#lt>typedef uint32_t RTC_TIMER32_INT_MASK;
    <#else>
        <#lt>typedef uint32_t RTC_TIMER16_INT_MASK;
    </#if>
<#else>
        <#lt>typedef enum
        <#lt>{
        <#lt>    RTC_PER0_MASK = 0x0001U,
        <#lt>    RTC_PER1_MASK = 0x0002U,
        <#lt>    RTC_PER2_MASK = 0x0004U,
        <#lt>    RTC_PER3_MASK = 0x0008U,
        <#lt>    RTC_PER4_MASK = 0x0010U,
        <#lt>    RTC_PER5_MASK = 0x0020U,
        <#lt>    RTC_PER6_MASK = 0x0040U,
        <#lt>    RTC_PER7_MASK = 0x0080U
        <#lt>} RTC_PERIODIC_INT_MASK;
</#if>
<#if TAMP_DETECTION_SUPPORTED??>
    <#if TAMP_DETECTION_SUPPORTED>
        <#if RTC_BKUP_SUPPORTED??>
            <#lt>typedef enum
            <#lt>{
            <#lt>    BACKUP_REGISTER_0 = 0U,
            <#lt>    BACKUP_REGISTER_1 = 1U,
            <#lt>    BACKUP_REGISTER_2 = 2U,
            <#lt>    BACKUP_REGISTER_3 = 3U,
            <#lt>    BACKUP_REGISTER_4 = 4U,
            <#lt>    BACKUP_REGISTER_5 = 5U,
            <#lt>    BACKUP_REGISTER_6 = 6U,
            <#lt>    BACKUP_REGISTER_7 = 7U
            <#lt>} BACKUP_REGISTER;
        </#if>       
        <#list 0..(TAMPER_CHANNEL_NUMBER - 1) as i>
            <#lt> #define   TAMPER_CHANNEL_${i}  (${i}U)
        </#list>
        <#lt>typedef uint32_t TAMPER_CHANNEL;
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
     RTC_MODE1_INTERRUPT = false && RTC_MODULE_SELECTION = "MODE1" ||
	 RTC_MODE2_INTERRUPT = false && RTC_MODULE_SELECTION = "MODE2">
    <#lt>bool ${RTC_INSTANCE_NAME}_PeriodicIntervalHasCompleted ( RTC_PERIODIC_INT_MASK period );
</#if>
<#if RTC_MODULE_SELECTION = "MODE0">
    <#if RTC_MODE0_INTERRUPT = false>
        <#lt>bool ${RTC_INSTANCE_NAME}_Timer32CounterHasOverflowed ( void );
        <#if RTC_MODE0_NUM_COMP == 1>
        <#lt>bool ${RTC_INSTANCE_NAME}_Timer32CompareHasMatched( void );
        <#else>
        <#list 0..(RTC_MODE0_NUM_COMP - 1) as i>
        <#lt>bool ${RTC_INSTANCE_NAME}_Timer32Compare${i}HasMatched( void );
        </#list>
        </#if>
    </#if>
	<#lt>void ${RTC_INSTANCE_NAME}_Timer32CountSyncEnable ( void );
	<#lt>void ${RTC_INSTANCE_NAME}_Timer32CountSyncDisable ( void );
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
        <#lt>void ${RTC_INSTANCE_NAME}_Timer32InterruptEnable( RTC_TIMER32_INT_MASK interruptMask );
        <#lt>void ${RTC_INSTANCE_NAME}_Timer32InterruptDisable( RTC_TIMER32_INT_MASK interruptMask );
    </#if>
<#elseif RTC_MODULE_SELECTION = "MODE1">
    <#if RTC_MODE1_INTERRUPT = false>
        <#lt>bool ${RTC_INSTANCE_NAME}_Timer16PeriodHasExpired ( void );
        <#lt>bool ${RTC_INSTANCE_NAME}_Timer16CounterHasOverflowed ( void );
        <#list 0..(RTC_MODE1_NUM_COMP - 1) as i>
            <#lt>bool ${RTC_INSTANCE_NAME}_Timer16Compare${i}HasMatched( void );
        </#list>
    </#if>
	<#lt>void ${RTC_INSTANCE_NAME}_Timer16CountSyncEnable ( void );
	<#lt>void ${RTC_INSTANCE_NAME}_Timer16CountSyncDisable ( void );
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
        <#lt>void ${RTC_INSTANCE_NAME}_Timer16InterruptEnable( RTC_TIMER16_INT_MASK interruptMask );
        <#lt>void ${RTC_INSTANCE_NAME}_Timer16InterruptDisable( RTC_TIMER16_INT_MASK interruptMask );
    </#if>
<#else>
	<#lt>void ${RTC_INSTANCE_NAME}_RTCCClockSyncEnable ( void );
	<#lt>void ${RTC_INSTANCE_NAME}_RTCCClockSyncDisable ( void );
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
        <#if RTC_BKUP_SUPPORTED??>
            <#lt>void ${RTC_INSTANCE_NAME}_BackupRegisterSet( BACKUP_REGISTER reg, uint32_t value );
            <#lt>uint32_t ${RTC_INSTANCE_NAME}_BackupRegisterGet( BACKUP_REGISTER reg );
        </#if>
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
