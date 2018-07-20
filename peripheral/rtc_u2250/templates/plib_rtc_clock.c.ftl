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

// *****************************************************************************
// *****************************************************************************
// Section: Macro Definitions
// *****************************************************************************
// *****************************************************************************

/* Maximum correction value */
#define MAX_CORRECTION_VALUE        (0x7FU)

/* Correction value is Zero */
#define CORRECTION_VALUE_ZERO       (0U)

/* Reference Year */
#define REFERENCE_YEAR              (${RTC_MODE2_REFERENCE_YEAR}U)

/* Refernce Year in tm structure year (C standard) */
#define TM_STRUCT_REFERENCE_YEAR    (1900U)

/* Clock Hour Mask */
#define CLOCK_HOUR_MASK             (0x0001F000U)

/* Clock Minute Mask */
#define CLOCK_MINUTE_MASK           (0x00000FC0U)

/* Clock Second Mask */
#define CLOCK_SECOND_MASK           (0x0000003FU)

/* Calendar Month Mask */
#define CALENDAR_MONTH_MASK         (0x03C00000U)

/* Calendar Year Mask */
#define CALENDAR_YEAR_MASK          (0xFC000000U)

/* Calendar Day Mask */
#define CALENDAR_DAY_MASK           (0x003E0000U)

/* Adjust user year with respect to tm structure year (C Standard) */
#define ADJUST_TM_YEAR(year)        (year + TM_STRUCT_REFERENCE_YEAR)

/* Adjust user month */
#define ADJUST_MONTH(month)         (month + 1)

/* Adjust to tm structure month */
#define ADJUST_TM_STRUCT_MONTH(mon) (mon - 1)

<#if RTC_MODE2_INTERRUPT = true >
// *****************************************************************************
// *****************************************************************************
// Section: Interface Routine Pointers
// *****************************************************************************
// *****************************************************************************

/* RTC Callback Object

  Summary:
    RTC peripheral callback object.

  Description:
    This local data object holds the function signature for the RTC peripheral
    callback function.

  Remarks:
    None.
*/

typedef struct
{
    /* Periodic Interval Callback */
    RTC_PERIODIC_INTERVAL_CALLBACK periodicCallback;

    /* RTC Clock Event */
    RTC_CLOCK_EVENT clockEvent;

    /* RTC Clock/Calendar */
    RTC_CALLBACK alarmCallback;

    uintptr_t context;

} RTC_OBJECT;

RTC_OBJECT rtc${RTC_INDEX}Obj;

</#if>
// *****************************************************************************
// *****************************************************************************
// Section: RTC Implementation
// *****************************************************************************
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Function:
    void RTC${RTC_INDEX}_Initialize(void)

  Summary:
    Initialize given instance of the RTC peripheral.

  Description:
    This function initialize the given instance of the RTC peripheral as
    configured by the user from the MHC.

  Remarks:
    Refer plib_rtc${RTC_INDEX}.h for more information.
*/

void RTC${RTC_INDEX}_Initialize(void)
{
    /* Software Reset */
    _RTC_REGS->MODE2.CTRLA.w |= RTC_MODE2_CTRLA_SWRST_Msk;

    while((_RTC_REGS->MODE2.SYNCBUSY.w & RTC_MODE2_SYNCBUSY_SWRST_Msk) == RTC_MODE2_SYNCBUSY_SWRST_Msk)
    {
        /* Wait for synchronization after Software Reset */
    }

    /*
     * Set Operating mode,prescaler,clocksync and
     * clock representation(12Hr/24Hr)
     */
    <@compress single_line=true>_RTC_REGS->MODE2.CTRLA.w |= RTC_MODE2_CTRLA_MODE(2) |
                                                            RTC_MODE2_CTRLA_PRESCALER(${RTC_MODE2_PRESCALER}) |
                                                            RTC_MODE2_CTRLA_CLOCKSYNC_Msk
                                                            ${RTC_MODE2_CLKREP?then('| RTC_MODE2_CTRLA_CLKREP_Msk','')};</@compress>

    /* Disable all Interrupts */
    RTC_REGS->MODE2.INTENCLR.w |= RTC_MODE2_INTENCLR_Msk;

    /* Clear all Interrupts */
    RTC_REGS->MODE2.INTFLAG.w = RTC_MODE2_INTFLAG_Msk;

    /* Enable RTC */
    RTC_REGS->MODE2.CTRLA.w |= RTC_MODE2_CTRLA_ENABLE_Msk;

    while((RTC_REGS->MODE2.SYNCBUSY.w & RTC_MODE2_SYNCBUSY_ENABLE_Msk) == RTC_MODE2_SYNCBUSY_ENABLE_Msk)
    {
        /* Wait for Synchronization after Enabling RTC */
    }
<#if RTC_MODE2_INTERRUPT = true && RTC_MODE2_PERIOD != "NO">

    /* Enable Period Interrupt */
    RTC_REGS->MODE2.INTENSET.w |= RTC_MODE2_INTENSET_${RTC_MODE2_PERIOD}_Msk;
</#if>
}
<#if RTC_MODE2_FREQCORR = true >

// *****************************************************************************
/* Function:
    void RTC${RTC_INDEX}_FrequencyCorrect (int8_t correction)

  Summary:
    Calibrate for too-slow or too-fast oscillator.

  Description:
    The RTC will compensate for inaccurate oscillator. The RTC module will add
    or subtract cycles from the RTC prescaler to adjust the frequency. The
    provided correction value should be between 0 and 127, allowing for a
    maximum 127 PPM correction.

  Remarks:
    Refer plib_rtc${RTC_INDEX}.h for more information.
*/

void RTC${RTC_INDEX}_FrequencyCorrect (int8_t correction)
{
    uint32_t newCorrectionValue = 0;

    /* Load the new Correction value as a positive value, sign added later */
    newCorrectionValue = abs(correction);

    /* Convert to positive value and adjust Register sign bit. */
    if (correction < CORRECTION_VALUE_ZERO)
    {
        newCorrectionValue |= RTC_MODE2_FREQCORR_SIGN_Msk;
    }

    /* Set New Correction Value */
    RTC_REGS->MODE2.FREQCORR.w = newCorrectionValue;

    while((RTC_REGS->MODE2.SYNCBUSY.w & RTC_MODE2_SYNCBUSY_FREQCORR_Msk) == RTC_MODE2_SYNCBUSY_FREQCORR_Msk)
    {
        /* Wait for synchronization after writing value to FREQCORR */
    }
}
</#if>
<#if RTC_MODE2_INTERRUPT = false && RTC_MODE2_PERIOD != "NO">

// *****************************************************************************
/* Function:
    bool RTC${RTC_INDEX}_PeriodicIntervalHasCompleted (void)

  Summary:
    Check if the configured periodic interval has expired.

  Description:
    This function will check if the configured periodic interval expired. The
    RTC module can be configured to generate notification at periodic intervals.
    This function provides a polling method to check if a periodic interval is
    complete. The interval is configured via MHC.

  Remarks:
    Refer plib_rtc${RTC_INDEX}.h for more information.
*/

bool RTC${RTC_INDEX}_PeriodicIntervalHasCompleted (void)
{
    bool periodIntervalComplete = false;

    /* Check for the Period interval has completed */
    if( RTC_REGS->MODE2.INTFLAG.w & RTC_MODE2_INTFLAG_${RTC_MODE2_PERIOD}_Msk )
    {
        periodIntervalComplete = true;

        /* Clear Periodic Interval Interrupt */
        RTC_REGS->MODE2.INTFLAG.w = RTC_MODE2_INTFLAG_${RTC_MODE2_PERIOD}_Msk;
    }

    return periodIntervalComplete;
}
</#if>

// *****************************************************************************
/* Function:
    void RTC${RTC_INDEX}_RTCCTimeSet (struct tm * initialTime )

  Summary:
    Sets the Real Time Clock Calendar time and date.

  Description:
    This function sets the Real Time Clock Calendar time and date. The time and
    date should be specified via the struct tm structure. The isdst, tm_wday,
    tm_yday member of the initialTime data structure is ignored.

    The reference year parameter in MHC should be adjusted to be within 64 years
    of the input year range. In that, the function will subtract the reference
    year from the input year while setting the calendar year.

  Remarks:
    Refer plib_rtc${RTC_INDEX}.h for more information.
*/

void RTC${RTC_INDEX}_RTCCTimeSet (struct tm * initialTime )
{
    uint32_t registerValue = 0;

    /*
     * Add 1900 to the tm_year member and the adjust for the RTC reference year
     * Set YEAR(according to Reference Year), MONTH and DAY
     */
    registerValue = ((TM_STRUCT_REFERENCE_YEAR + initialTime->tm_year) - REFERENCE_YEAR) << RTC_MODE2_CLOCK_YEAR_Pos |
                    ((ADJUST_MONTH(initialTime->tm_mon)) << RTC_MODE2_CLOCK_MONTH_Pos) |
                    (initialTime->tm_mday << RTC_MODE2_CLOCK_DAY_Pos);

    /* Set HOUR, MINUTE and SECOND */
    registerValue |= (initialTime->tm_hour << RTC_MODE2_CLOCK_HOUR_Pos) |
                     (initialTime->tm_min << RTC_MODE2_CLOCK_MINUTE_Pos) |
                     (initialTime->tm_sec << RTC_MODE2_CLOCK_SECOND_Pos);

    /* Set the clock value from user to CLOCK Register */
    RTC_REGS->MODE2.CLOCK.w = registerValue;

    while((RTC_REGS->MODE2.SYNCBUSY.w & RTC_MODE2_SYNCBUSY_CLOCK_Msk) == RTC_MODE2_SYNCBUSY_CLOCK_Msk)
    {
        /* Synchronization after writing value to CLOCK Register */
    }
}

// *****************************************************************************
/* Function:
    void RTC${RTC_INDEX}_RTCCTimeGet (struct tm * currentTime )

  Summary:
    Gets the current time and date.

  Description:
    This function gets the current time and date. The time and date are returned
    in the struct tm structure. The isdst, tm_wday, tm_yday member of the
    currentTime data structure are not updated and should be ignored. The year
    specified in the tm_year field of current time will be years since 1900.

  Remarks:
    Refer plib_rtc${RTC_INDEX}.h for more information.
*/

void RTC${RTC_INDEX}_RTCCTimeGet ( struct tm * currentTime )
{
    uint32_t dataClockCalendar = 0;

    while((RTC_REGS->MODE2.SYNCBUSY.w & RTC_MODE2_SYNCBUSY_CLOCKSYNC_Msk) == RTC_MODE2_SYNCBUSY_CLOCKSYNC_Msk)
    {
        /* Synchronization before reading value from CLOCK Register */
    }

    /* Get Clock/Calendar value from CLOCK register */
    dataClockCalendar = RTC_REGS->MODE2.CLOCK.w;

    /* Get Clock value from CLOCK register */
    currentTime->tm_hour =  (dataClockCalendar & CLOCK_HOUR_MASK) >> RTC_MODE2_CLOCK_HOUR_Pos;
    currentTime->tm_min  =  (dataClockCalendar & CLOCK_MINUTE_MASK) >> RTC_MODE2_CLOCK_MINUTE_Pos;
    currentTime->tm_sec  =  (dataClockCalendar & CLOCK_SECOND_MASK) >> RTC_MODE2_CLOCK_SECOND_Pos;

    /* Get Calendar values from CLOCK register */
    currentTime->tm_mon  =  ADJUST_TM_STRUCT_MONTH(((dataClockCalendar & CALENDAR_MONTH_MASK) >> RTC_MODE2_CLOCK_MONTH_Pos));
    currentTime->tm_year =  (((dataClockCalendar & CALENDAR_YEAR_MASK)>> RTC_MODE2_CLOCK_YEAR_Pos) + REFERENCE_YEAR) - TM_STRUCT_REFERENCE_YEAR;
    currentTime->tm_mday =  (dataClockCalendar & CALENDAR_DAY_MASK) >> RTC_MODE2_CLOCK_DAY_Pos;
}
<#if RTC_MODE2_INTERRUPT = true>

// *****************************************************************************
/* Function:
    void RTC${RTC_INDEX}_RTCCAlarmSet(struct tm *alarmTime, RTC_ALARM_MASK mask)

  Summary:
    Set an alarm.

  Description:
    This function allows the application to set the time at which the alarm
    should occur. The date and time fields to be compared while generating the
    alarm can also be specified.

  Remarks:
    Refer plib_rtc${RTC_INDEX}.h for more information.
*/

void RTC${RTC_INDEX}_RTCCAlarmSet (struct tm * alarmTime, RTC_ALARM_MASK mask)
{
    uint32_t registerValue = 0;

    /* Enable Alarm Interrupt */
    RTC_REGS->MODE2.INTENSET.w |= RTC_MODE2_INTENSET_ALARM0_Msk;

    /*
     * Add 1900 to the tm_year member and the adjust for the RTC reference year
     * Set YEAR(according to Reference Year), MONTH and DAY
     */
    registerValue = ((TM_STRUCT_REFERENCE_YEAR + alarmTime->tm_year) - REFERENCE_YEAR) << RTC_MODE2_CLOCK_YEAR_Pos |
                    (ADJUST_MONTH(alarmTime->tm_mon) << RTC_MODE2_CLOCK_MONTH_Pos) |
                    (alarmTime->tm_mday << RTC_MODE2_CLOCK_DAY_Pos);

    /* Set HOUR value */
    registerValue |= (alarmTime->tm_hour << RTC_MODE2_CLOCK_HOUR_Pos) |
                     (alarmTime->tm_min << RTC_MODE2_CLOCK_MINUTE_Pos) |
                     (alarmTime->tm_sec << RTC_MODE2_CLOCK_SECOND_Pos);

    /* Set the value to ALARM Register */
    RTC_REGS->MODE2.Mode2Alarm.w = registerValue;

    while((RTC_REGS->MODE2.SYNCBUSY.w & RTC_MODE2_SYNCBUSY_ALARM0_Msk) == RTC_MODE2_SYNCBUSY_ALARM0_Msk)
    {
        /* Synchronization after writing to ALARM register */
    }

    /* Set Alarm Mask */
    RTC_REGS->MODE2.Mode2AlarmMask.w = mask;

    while((RTC_REGS->MODE2.SYNCBUSY.w & RTC_MODE2_SYNCBUSY_MASK0_Msk) == RTC_MODE2_SYNCBUSY_MASK0_Msk)
    {
        /* Synchronization after writing value to MASK Register */
    }
}

// *****************************************************************************
/* Function:
    void RTC${RTC_INDEX}_PeriodicIntervalCallbackRegister
                  (RTC_PERIODIC_INTERVAL_CALLBACK callback, uintptr_t context);

  Summary:
    Register the callback function to be called when a configured RTC Periodic
    Interval has completd.

  Description:
    This function registers the  callback function  that the library will call
    when a configured RTC Periodic Interval has completed. The library will the
    pass the application specified context into the callback function.

  Remarks:
    Refer plib_rtc${RTC_INDEX}.h for more information.
*/

void RTC${RTC_INDEX}_PeriodicIntervalCallbackRegister(RTC_PERIODIC_INTERVAL_CALLBACK callback, uintptr_t context)
{
    rtc${RTC_INDEX}Obj.periodicCallback = callback;
    rtc${RTC_INDEX}Obj.context          = context;
}

// *****************************************************************************
/* Function:
    void RTC${RTC_INDEX}_RTCCCallbackRegister ( RTC_CALLBACK callback, uintptr_t context )

  Summary:
    Register the callback function to be called when an RTCC Interrupt occurs.

  Description:
    This function registers the  callback function  that the library will call
    when an RTCC interrupt occurs. The library will return the event that has
    caused the interrupt and the application specified context in the callback
    function.

  Remarks:
    Refer plib_rtc${RTC_INDEX}.h for more information.
*/

void RTC${RTC_INDEX}_RTCCCallbackRegister ( RTC_CALLBACK callback, uintptr_t context)
{
    rtc${RTC_INDEX}Obj.alarmCallback = callback;
    rtc${RTC_INDEX}Obj.context       = context;
}

// *****************************************************************************
/* Function:
    void RTC${RTC_INDEX}_InterruptHandler(void)

  Summary:
    Handle RTC Interrupts

  Description:
    This function is called from the RTC handler to handle the interrupts.
    Invoke the callback function which is already registered in corresponding
    mode.

  Remarks:
    None.
*/

void RTC${RTC_INDEX}_InterruptHandler(void)
{
<#if RTC_MODE2_PERIOD != "NO">
    /* Check Periodic Interval has Expired */
    if((RTC_REGS->MODE2.INTFLAG.w & RTC_MODE2_INTFLAG_${RTC_MODE2_PERIOD}_Msk) == RTC_MODE2_INTFLAG_${RTC_MODE2_PERIOD}_Msk)
    {
        if(rtc${RTC_INDEX}Obj.periodicCallback != NULL)
        {
            rtc${RTC_INDEX}Obj.periodicCallback(rtc${RTC_INDEX}Obj.context);
        }
    }
</#if>

    /* Check Alarm */
    if((RTC_REGS->MODE2.INTFLAG.w & RTC_MODE2_INTFLAG_ALARM0_Msk) == RTC_MODE2_INTFLAG_ALARM0_Msk)
    {
        rtc0Obj.clockEvent = RTC_REGS->MODE2.INTFLAG.w;

        if(rtc${RTC_INDEX}Obj.alarmCallback != NULL)
        {
            rtc${RTC_INDEX}Obj.alarmCallback(rtc0Obj.clockEvent, rtc${RTC_INDEX}Obj.context);
        }
    }

    /* Clear All Interrupts */
    RTC_REGS->MODE2.INTFLAG.w = RTC_MODE2_INTFLAG_Msk;
}
</#if>