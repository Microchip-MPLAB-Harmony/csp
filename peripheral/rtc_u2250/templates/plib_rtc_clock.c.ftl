/*******************************************************************************
  Real Time Counter (RTC${RTC_INDEX}) PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_rtc${RTC_INDEX}_clock.c

  Summary:
    RTC${RTC_INDEX} PLIB Implementation file

  Description:
    This file defines the interface to the RTC peripheral library. This
    library provides access to and control of the associated peripheral
    instance in clock/calendar mode.

*******************************************************************************/
// DOM-IGNORE-BEGIN
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
// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
/* This section lists the other files that are included in this file.
*/

#include "plib_rtc${RTC_INDEX}.h"
#include "device.h"
#include <stdlib.h>

/* Reference Year */
#define REFERENCE_YEAR              (${RTC_MODE2_REFERENCE_YEAR}U)

/* Refernce Year in tm structure year (C standard) */
#define TM_STRUCT_REFERENCE_YEAR    (1900U)

/* Adjust user year with respect to tm structure year (C Standard) */
#define ADJUST_TM_YEAR(year)        (year + TM_STRUCT_REFERENCE_YEAR)

/* Adjust user month */
#define ADJUST_MONTH(month)         (month + 1)

/* Adjust to tm structure month */
#define ADJUST_TM_STRUCT_MONTH(mon) (mon - 1)

<#if RTC_MODE2_INTERRUPT = true >
    <#lt>RTC_OBJECT rtc${RTC_INDEX}Obj;
</#if>

void RTC${RTC_INDEX}_Initialize(void)
{
    RTC_REGS->MODE2.CTRLA |= RTC_MODE2_CTRLA_SWRST_Msk;

    while((RTC_REGS->MODE2.SYNCBUSY & RTC_MODE2_SYNCBUSY_SWRST_Msk) == RTC_MODE2_SYNCBUSY_SWRST_Msk)
    {
        /* Wait for synchronization after Software Reset */
    }

    <@compress single_line=true>RTC_REGS->MODE2.CTRLA = RTC_MODE2_CTRLA_MODE(2) |
                                                            RTC_MODE2_CTRLA_PRESCALER(${RTC_MODE2_PRESCALER}) |
                                                            RTC_MODE2_CTRLA_CLOCKSYNC_Msk |
                                                            RTC_MODE2_CTRLA_ENABLE_Msk;</@compress>


    while((RTC_REGS->MODE2.SYNCBUSY & RTC_MODE2_SYNCBUSY_ENABLE_Msk) == RTC_MODE2_SYNCBUSY_ENABLE_Msk)
    {
        /* Wait for Synchronization after Enabling RTC */
    }
    
    <#if RTC_MODE2_EVCTRL != "0">
        <#lt>RTC_REGS->MODE2.EVCTRL = 0x${RTC_MODE2_EVCTRL};
    </#if>
}
<#if RTC_FREQCORR = true >

    <#lt>void RTC${RTC_INDEX}_FrequencyCorrect (int8_t correction)
    <#lt>{
    <#lt>    uint32_t newCorrectionValue = 0;
    <#lt>
    <#lt>    newCorrectionValue = abs(correction);
    <#lt>
    <#lt>    /* Convert to positive value and adjust Register sign bit. */
    <#lt>    if (correction < 0)
    <#lt>    {
    <#lt>        newCorrectionValue |= RTC_MODE2_FREQCORR_SIGN_Msk;
    <#lt>    }

    <#lt>    RTC_REGS->MODE2.FREQCORR = newCorrectionValue;

    <#lt>    while((RTC_REGS->MODE2.SYNCBUSY & RTC_MODE2_SYNCBUSY_FREQCORR_Msk) == RTC_MODE2_SYNCBUSY_FREQCORR_Msk)
    <#lt>    {
    <#lt>        /* Wait for synchronization after writing value to FREQCORR */
    <#lt>    }
    <#lt>}
</#if>

<#if RTC_MODE2_INTERRUPT = false>

    <#lt>bool RTC${RTC_INDEX}_PeriodicIntervalHasCompleted (RTC_PERIODIC_INT_MASK period)
    <#lt>{
    <#lt>    bool periodIntervalComplete = false;

    <#lt>    if( (RTC_REGS->MODE2.INTFLAG & period) == period )
    <#lt>    {
    <#lt>        periodIntervalComplete = true;

    <#lt>        /* Clear Periodic Interval Interrupt */
    <#lt>        RTC_REGS->MODE2.INTFLAG = period;
    <#lt>    }

    <#lt>    return periodIntervalComplete;
    <#lt>}
</#if>

void RTC${RTC_INDEX}_RTCCTimeSet (struct tm * initialTime )
{
    /*
     * Add 1900 to the tm_year member and the adjust for the RTC reference year
     * Set YEAR(according to Reference Year), MONTH and DAY
     *set Hour Minute and Second
     */
    RTC_REGS->MODE2.CLOCK = ((TM_STRUCT_REFERENCE_YEAR + initialTime->tm_year) - REFERENCE_YEAR) << RTC_MODE2_CLOCK_YEAR_Pos |
                    ((ADJUST_MONTH(initialTime->tm_mon)) << RTC_MODE2_CLOCK_MONTH_Pos) |
                    (initialTime->tm_mday << RTC_MODE2_CLOCK_DAY_Pos) |
                    (initialTime->tm_hour << RTC_MODE2_CLOCK_HOUR_Pos) |
                    (initialTime->tm_min << RTC_MODE2_CLOCK_MINUTE_Pos) |
                    (initialTime->tm_sec << RTC_MODE2_CLOCK_SECOND_Pos);

    while((RTC_REGS->MODE2.SYNCBUSY & RTC_MODE2_SYNCBUSY_CLOCK_Msk) == RTC_MODE2_SYNCBUSY_CLOCK_Msk)
    {
        /* Synchronization after writing value to CLOCK Register */
    }
}

void RTC${RTC_INDEX}_RTCCTimeGet ( struct tm * currentTime )
{
    uint32_t dataClockCalendar = 0;

    while((RTC_REGS->MODE2.SYNCBUSY & RTC_MODE2_SYNCBUSY_CLOCKSYNC_Msk) == RTC_MODE2_SYNCBUSY_CLOCKSYNC_Msk)
    {
        /* Synchronization before reading value from CLOCK Register */
    }

    dataClockCalendar = RTC_REGS->MODE2.CLOCK;

    currentTime->tm_hour =  (dataClockCalendar & RTC_MODE2_CLOCK_HOUR_Msk) >> RTC_MODE2_CLOCK_HOUR_Pos;
    currentTime->tm_min  =  (dataClockCalendar & RTC_MODE2_CLOCK_MINUTE_Msk) >> RTC_MODE2_CLOCK_MINUTE_Pos;
    currentTime->tm_sec  =  (dataClockCalendar & RTC_MODE2_CLOCK_SECOND_Msk) >> RTC_MODE2_CLOCK_SECOND_Pos;

    currentTime->tm_mon  =  ADJUST_TM_STRUCT_MONTH(((dataClockCalendar & RTC_MODE2_CLOCK_MONTH_Msk) >> RTC_MODE2_CLOCK_MONTH_Pos));
    currentTime->tm_year =  (((dataClockCalendar & RTC_MODE2_CLOCK_YEAR_Msk)>> RTC_MODE2_CLOCK_YEAR_Pos) + REFERENCE_YEAR) - TM_STRUCT_REFERENCE_YEAR;
    currentTime->tm_mday =  (dataClockCalendar & RTC_MODE2_CLOCK_DAY_Msk) >> RTC_MODE2_CLOCK_DAY_Pos;
}
<#if RTC_MODE2_INTERRUPT = true>

    <#lt>void RTC${RTC_INDEX}_RTCCAlarmSet (struct tm * alarmTime, RTC_ALARM_MASK mask)
    <#lt>{
    <#lt>    /*
    <#lt>     * Add 1900 to the tm_year member and the adjust for the RTC reference year
    <#lt>     * Set YEAR(according to Reference Year), MONTH and DAY
    <#lt>     * Set Hour, Minute and second
    <#lt>     */
    <#lt>    RTC_REGS->MODE2.Mode2Alarm = ((TM_STRUCT_REFERENCE_YEAR + alarmTime->tm_year) - REFERENCE_YEAR) << RTC_MODE2_CLOCK_YEAR_Pos |
    <#lt>                    (ADJUST_MONTH(alarmTime->tm_mon) << RTC_MODE2_CLOCK_MONTH_Pos) |
    <#lt>                    (alarmTime->tm_mday << RTC_MODE2_CLOCK_DAY_Pos) |
    <#lt>                    (alarmTime->tm_hour << RTC_MODE2_CLOCK_HOUR_Pos) |
    <#lt>                     (alarmTime->tm_min << RTC_MODE2_CLOCK_MINUTE_Pos) |
    <#lt>                     (alarmTime->tm_sec << RTC_MODE2_CLOCK_SECOND_Pos);

    <#lt>    while((RTC_REGS->MODE2.SYNCBUSY & RTC_MODE2_SYNCBUSY_ALARM0_Msk) == RTC_MODE2_SYNCBUSY_ALARM0_Msk)
    <#lt>    {
    <#lt>        /* Synchronization after writing to ALARM register */
    <#lt>    }

    <#lt>    RTC_REGS->MODE2.Mode2AlarmMask = mask;

    <#lt>    while((RTC_REGS->MODE2.SYNCBUSY & RTC_MODE2_SYNCBUSY_MASK0_Msk) == RTC_MODE2_SYNCBUSY_MASK0_Msk)
    <#lt>    {
    <#lt>        /* Synchronization after writing value to MASK Register */
    <#lt>    }
        
    <#lt>    RTC_REGS->MODE2.INTENSET = RTC_MODE2_INTENSET_ALARM0_Msk;
    <#lt>}

    <#lt>void RTC${RTC_INDEX}_RTCCCallbackRegister ( RTC_CALLBACK callback, uintptr_t context)
    <#lt>{
    <#lt>    rtc${RTC_INDEX}Obj.alarmCallback = callback;
    <#lt>    rtc${RTC_INDEX}Obj.context       = context;
    <#lt>}


    <#lt>void RTC${RTC_INDEX}_InterruptHandler(void)
    <#lt>{
    <#lt>    rtc0Obj.intCause = RTC_REGS->MODE2.INTFLAG;

    <#lt>    if(rtc${RTC_INDEX}Obj.alarmCallback != NULL)
    <#lt>    {
    <#lt>        rtc${RTC_INDEX}Obj.alarmCallback(rtc0Obj.intCause, rtc${RTC_INDEX}Obj.context);
    <#lt>    }

    <#lt>    /* Clear All Interrupts */
    <#lt>    RTC_REGS->MODE2.INTFLAG = RTC_MODE2_INTFLAG_Msk;
    <#lt>}
</#if>