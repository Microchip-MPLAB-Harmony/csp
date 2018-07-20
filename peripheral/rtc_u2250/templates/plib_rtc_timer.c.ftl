/*******************************************************************************
  Real Time Counter (RTC${RTC_INDEX}) PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_rtc${RTC_INDEX}_timer.c

  Summary:
    RTC${RTC_INDEX} PLIB Implementation file

  Description:
    This file defines the interface to the RTC peripheral library. This
    library provides access to and control of the associated peripheral
    instance in timer mode.

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

<#if RTC_MODULE_SELECTION = "MODE0">
/* Frequency of RTC Clock */
#define RTC_CLOCK_FREQUENCY        (32678 / (2 ^ ${RTC_MODE0_PRESCALER}))

/* Mode 0 Period Value */
#define RTC_MODE0_PERIOD           (0x${RTC_MODE0_TIMER_COUNTER_PERIOD}U)

/* Mode 0 Compare 0 and Overflow Interrupt Mask*/
#define RTC_32BIT_INTERRUPT_MASK   (0x8100U)
<#elseif RTC_MODULE_SELECTION = "MODE1">
/* Frequency of RTC Clock */
#define RTC_CLOCK_FREQUENCY        (32678 / (2 ^ ${RTC_MODE1_PRESCALER}))

/* Mode 1 Period Value */
#define RTC_MODE1_PERIOD           (0x${RTC_MODE1_TIMER_COUNTER_PERIOD}U)

/* Timer 16-bit Compare 0 Value */
#define RTC_MODE1_COMPARE0_VALUE   (0x${RTC_MODE1_COMPARE0_MATCH_VALUE}U)

/* Timer 16-bit Compare 1 Value */
#define RTC_MODE1_COMPARE1_VALUE   (0x${RTC_MODE1_COMPARE1_MATCH_VALUE}U)

/* Mode 1 Compare 0, Compare 1 and Overflow Interrupt Mask */
#define RTC_16BIT_INTERRUPT_MASK   (0x8300U)
</#if>

/* Correction value is Zero */
#define CORRECTION_VALUE_ZERO      (0U)

<#if ( RTC_MODE0_INTERRUPT = true && RTC_MODULE_SELECTION = "MODE0" ) ||
     ( RTC_MODE1_INTERRUPT = true && RTC_MODULE_SELECTION = "MODE1" ) >
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

<#if RTC_MODULE_SELECTION = "MODE0" >
    /* Timer 32Bit */
    RTC_TIMER32_CALLBACK timer32BitCallback;

    /* 32Bit Timer Event */
    RTC_TIMER32_EVENT timer32BitEvent;
<#else>
    /* Timer 16Bit */
    RTC_TIMER16_CALLBACK timer16BitCallback;

    /* 16Bit Timer Event */
    RTC_TIMER16_EVENT timer16BitEvent;
</#if>

    uintptr_t context;

} RTC_OBJECT;

RTC_OBJECT rtc${RTC_INDEX}Obj;

</#if>
// *****************************************************************************
// *****************************************************************************
// Section: RTC Implementation
// *****************************************************************************
// *****************************************************************************
/* The following functions make up the methods (set of possible operations) of
   this interface.
*/

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
    RTC_REGS->${RTC_MODULE_SELECTION}.CTRLA.w |= RTC_${RTC_MODULE_SELECTION}_CTRLA_SWRST_Msk;

    while((RTC_REGS->${RTC_MODULE_SELECTION}.SYNCBUSY.w & RTC_${RTC_MODULE_SELECTION}_SYNCBUSY_SWRST_Msk) == RTC_${RTC_MODULE_SELECTION}_SYNCBUSY_SWRST_Msk)
    {
        /* Wait for Synchronization after Software Reset */
    }

<#if RTC_MODULE_SELECTION = "MODE0">
    /* Set Operating Mode, Prescaler and COUNT Read Synchronization */
    <@compress single_line=true>RTC_REGS->MODE0.CTRLA.w |= RTC_MODE0_CTRLA_MODE(0) |
                                                            RTC_MODE0_CTRLA_PRESCALER(${RTC_MODE0_PRESCALER}) |
                                                            RTC_MODE0_CTRLA_COUNTSYNC_Msk;</@compress>

    /* Disable all Interrupts */
    RTC_REGS->MODE0.INTENCLR.w |= RTC_MODE0_INTENCLR_Msk;

    /* 32-bit Period Value */
    RTC_REGS->MODE0.COMP.w = RTC_MODE0_PERIOD;
<#else>
    /* Set Operating Mode, Prescaler and COUNT Read Synchronization */
    <@compress single_line=true>RTC_REGS->MODE1.CTRLA.w |= RTC_MODE1_CTRLA_MODE(1) |
                                                            RTC_MODE1_CTRLA_PRESCALER(${RTC_MODE1_PRESCALER}) |
                                                            RTC_MODE1_CTRLA_COUNTSYNC_Msk;</@compress>

    /* Disable all Interrupts */
    RTC_REGS->MODE1.INTENCLR.w |= RTC_MODE1_INTENCLR_Msk;

<#if RTC_MODE1_INTERRUPT = false>
    <#if RTC_MODE1_GENERATE_COMPARE0_API = true>
    /* 16-bit Timer Compare 0 Value */
    RTC_REGS->MODE1.COMP[0].w = RTC_MODE1_COMPARE0_VALUE;

    </#if>
    <#if RTC_MODE1_GENERATE_COMPARE1_API = true>
    /* 16-bit Timer Compare 0 Value */
    RTC_REGS->MODE1.COMP[1].w = RTC_MODE1_COMPARE1_VALUE;

    </#if>
</#if>
    /* 16-bit Period Value */
    RTC_REGS->MODE1.PER.w = RTC_MODE1_PERIOD;

</#if>
}
<#if (RTC_MODE0_FREQCORR = true && RTC_MODULE_SELECTION = "MODE0") ||
     (RTC_MODE1_FREQCORR = true && RTC_MODULE_SELECTION = "MODE1") >

// *****************************************************************************
/* Function:
    void RTC${RTC_INDEX}_FrequencyCorrect (int8_t correction)

  Summary:
    Calibrate for too-slow or too-fast oscillator.

  Description:
    This function allows the application to calibrate the RTC frequency. The RTC
    module will add or subtract cycles from the RTC prescaler to adjust the
    frequency in steps of approximately 1ppm. The provided correction value
    should be between -127 to 127. A positive correction value adds counts and
    increase the period, thus reducing the frequency. A negative count will have
    the reverse effect.

  Remarks:
    Refer plib_rtc${RTC_INDEX}.h for more information.
*/

void RTC${RTC_INDEX}_FrequencyCorrect (int8_t correction)
{
    uint32_t newCorrectionValue = 0;

    /* Load the new Correction Value as a positive value, sign added later */
    newCorrectionValue = abs(correction);

    /* Convert to positive value and adjust register sign bit. */
    if (correction < CORRECTION_VALUE_ZERO)
    {
        newCorrectionValue |= RTC_${RTC_MODULE_SELECTION}_FREQCORR_SIGN_Msk;
    }

    /* Set Correction Value */
    RTC_REGS->${RTC_MODULE_SELECTION}.FREQCORR.w = newCorrectionValue;

    while((RTC_REGS->${RTC_MODULE_SELECTION}.SYNCBUSY.w & RTC_${RTC_MODULE_SELECTION}_SYNCBUSY_FREQCORR_Msk) == RTC_${RTC_MODULE_SELECTION}_SYNCBUSY_FREQCORR_Msk)
    {
        /* Wait for Synchronization after writing Value to FREQCORR */
    }
}
</#if>
<#if RTC_MODE0_INTERRUPT = false && RTC_MODULE_SELECTION = "MODE0" ||
     RTC_MODE1_INTERRUPT = false && RTC_MODULE_SELECTION = "MODE1" >
<#if RTC_MODE0_PERIOD != "NO" && RTC_MODE0_PERIOD != "NO" >

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

<#if RTC_MODULE_SELECTION = "MODE0" >
    /* Check for the Period interval has completed */
    if( (RTC_REGS->MODE0.INTFLAG.w & RTC_MODE0_INTFLAG_${RTC_MODE0_PERIOD}_Msk ) == RTC_MODE0_INTFLAG_${RTC_MODE0_PERIOD}_Msk)
    {
        periodIntervalComplete = true;

        /* Clear Periodic Interval Interrupt */
        RTC_REGS->MODE0.INTFLAG.w = RTC_MODE0_INTFLAG_${RTC_MODE0_PERIOD}_Msk;
    }

<#elseif RTC_MODULE_SELECTION = "MODE1" >
    /* Check for the Period interval has completed */
    if( (RTC_REGS->MODE1.INTFLAG.w & RTC_MODE1_INTFLAG_${RTC_MODE1_PERIOD}_Msk ) == RTC_MODE1_INTFLAG_${RTC_MODE1_PERIOD}_Msk)
    {
        periodIntervalComplete = true;

        /* Clear Periodic Interval Interrupt */
        RTC_REGS->MODE1.INTFLAG.w = RTC_MODE1_INTFLAG_${RTC_MODE1_PERIOD}_Msk;
    }
</#if>

    return periodIntervalComplete;
}
</#if>
<#if RTC_MODULE_SELECTION = "MODE0">

// *****************************************************************************
/* Function:
    bool RTC${RTC_INDEX}_Timer32PeriodHasExpired ( void )

  Summary:
    Check for 32-bit Timer Period Expiry.

  Description:
    This function returns true if the counter value has matched the configured
    32-bit timer period. The counter will be reset and start counting again.

    The API can be used to poll period completion when using the timer counter
    as a timer. Calling the function will clear the internal period match flags
    if these flags were set at the time of calling the function.

  Remarks:
    Refer plib_rtc${RTC_INDEX}.h for more information.
*/

bool RTC${RTC_INDEX}_Timer32PeriodHasExpired ( void )
{
    bool periodHasExpired = false;

    /* Check Counter Value exceeds Compare/Period Value */
    if((RTC_REGS->MODE0.INTFLAG.w & RTC_MODE0_INTFLAG_CMP0_Msk) == RTC_MODE0_INTFLAG_CMP0_Msk)
    {
        periodHasExpired = true;

        /* Clear Period Interrupt */
        RTC_REGS->MODE0.INTFLAG.w = RTC_MODE0_INTFLAG_CMP0_Msk;
    }

    return periodHasExpired;
}

// *****************************************************************************
/* Function:
    bool RTC${RTC_INDEX}_Timer32CounterHasOverflowed ( void )

  Summary:
    Check if the 32-bit counter overflow.

  Description:
    This function will return true if the 32-bit counter has overflowed. An
    overflow occurs when the counter values transitions from 0xFFFFFFFF to 0x0.
    This function can be used to validate the timer count when using the timer
    counter as a counter. Calling the function will clear the internal overflow
    flags if these flags were set at the time of calling the function.

  Remarks:
    Refer plib_rtc${RTC_INDEX}.h for more information.
*/

bool RTC${RTC_INDEX}_Timer32CounterHasOverflowed ( void )
{
    bool counterHasOverflowed = false;

    /* Check Counter Value exceeds maximum COUNT Value(0xFFFFFFFF) */
    if((RTC_REGS->MODE0.INTFLAG.w & RTC_MODE0_INTFLAG_OVF_Msk) == RTC_MODE0_INTFLAG_OVF_Msk)
    {
        counterHasOverflowed = true;

        /* Clear Counter Overflow Interrupt */
        RTC_REGS->MODE0.INTFLAG.w = RTC_MODE0_INTFLAG_OVF_Msk;
    }

    return counterHasOverflowed;
}
</#if>
<#if RTC_MODULE_SELECTION = "MODE1">

// *****************************************************************************
/* Function:
    bool RTC${RTC_INDEX}_Timer16PeriodHasExpired ( void )

  Summary:
    Check for 16-bit Timer Period Expiry.

  Description:
    This function returns true if the counter value has matched the configured
    16-bit timer period. The counter will be reset and start counting again.

    The API can be used to poll period completion when using the timer counter
    as a timer. Calling the function will clear the internal period match flags
    if these flags were set at the time of calling the function.

  Remarks:
    Refer plib_rtc${RTC_INDEX}.h for more information.
*/

bool RTC${RTC_INDEX}_Timer16PeriodHasExpired ( void )
{
    bool periodHasExpired = false;

    /* Check Counter Value exceeds Period Value */
    if((RTC_REGS->MODE1.INTFLAG.w & RTC_MODE1_INTFLAG_OVF_Msk ) == RTC_MODE1_INTFLAG_OVF_Msk)
    {
        periodHasExpired = true;

        /* Clear Period/Overflow Interrupts */
        RTC_REGS->MODE1.INTFLAG.w = RTC_MODE1_INTFLAG_OVF_Msk;
    }

    return periodHasExpired;
}

// *****************************************************************************
/* Function:
    bool RTC${RTC_INDEX}_Timer16CounterHasOverflowed ( void )

  Summary:
    Check if the 16-bit counter overflow.

  Description:
    This function will return true if the 16-bit counter has overflowed. An
    overflow occurs when the counter values transitions from 0xFFFF to 0x0.
    This function can be used to validate the timer count when using the timer
    counter as a counter. Calling the function will clear the internal overflow
    flags if these flags were set at the time of calling the function.

  Remarks:
    Refer plib_rtc${RTC_INDEX}.h for more information.
*/

bool RTC${RTC_INDEX}_Timer16CounterHasOverflowed ( void )
{
    bool counterHasOverflowed = false;

    /* Check Counter Value exceeds maximum value */
    if((RTC_REGS->MODE1.INTFLAG.w & RTC_MODE1_INTFLAG_OVF_Msk ) == RTC_MODE1_INTFLAG_OVF_Msk)
    {
        counterHasOverflowed = true;

        /* Clear Counter Overflow Interrupt */
        RTC_REGS->MODE1.INTFLAG.w = RTC_MODE1_INTFLAG_OVF_Msk;
    }

    return counterHasOverflowed;
}
<#if RTC_MODE1_GENERATE_COMPARE0_API = true>

// *****************************************************************************
/* Function:
    bool RTC${RTC_INDEX}_Timer16Compare0HasMatched(void)

  Summary:
    Returns true if the 16-bit Timer Compare 0 value has matched the counter.

  Description:
    This function returns true if the 16-bit Timer Compare 0 value has matched
    the counter. When operating in 16-bit Timer Counter mode, the RTC
    peripheral compares the counter value with two defined compare values
    (Compare 0 and Compare 1). This function will return true if the counter
    value has matched the Compare 0 value and also resets the hardware status
    flags if when match has occurred.

    The Compare 0 Value could have been configured via MHC or at run time by
    calling the RTC${RTC_INDEX}_Timer16Compare0Set() function. The
    RTC${RTC_INDEX}_Timer16Compare0ValueMatched() function allows the
    application to poll for the compare value match.

  Remarks:
    Refer plib_rtc${RTC_INDEX}.h for more information.
*/

bool RTC${RTC_INDEX}_Timer16Compare0HasMatched(void)
{
    bool compare0ValueMatch = false;

    /* Check Compare 0 Value Match */
    if((RTC_REGS->MODE1.INTFLAG.w & RTC_MODE1_INTFLAG_CMP0_Msk ) == RTC_MODE1_INTFLAG_CMP0_Msk)
    {
        compare0ValueMatch = true;

        /* Clear Compare 0 Match Flag */
        RTC_REGS->MODE1.INTFLAG.w = RTC_MODE1_INTFLAG_CMP0_Msk;
    }

    return compare0ValueMatch;
}
</#if>
<#if RTC_MODE1_GENERATE_COMPARE1_API = true>

// *****************************************************************************
/* Function:
    bool RTC${RTC_INDEX}_Timer16Compare1HasMatched(void)

  Summary:
    Returns true if the 16-bit Timer Compare 1 value has matched the counter.

  Description:
    This function returns true if the 16-bit Timer Compare 1 value has matched
    the counter. When operating in 16-bit Timer Counter mode, the RTC
    peripheral compares the counter value with two defined compare values
    (Compare 1 and Compare 1). This function will return true if the counter
    value has matched the Compare 1 value and also resets the hardware status
    flags if when match has occurred.

    The Compare 1 Value could have been configured via MHC or at run time by
    calling the RTC${RTC_INDEX}_Timer16Compare1Set() function. The
    RTC${RTC_INDEX}_Timer16Compare1ValueMatched() function allows the
    application to poll for the compare value match.

  Remarks:
    Refer plib_rtc${RTC_INDEX}.h for more information.
*/

bool RTC${RTC_INDEX}_Timer16Compare1HasMatched(void)
{
    bool compare1ValueMatch = false;

    /* Check Compare 1 Value Match */
    if((RTC_REGS->MODE1.INTFLAG.w & RTC_MODE1_INTFLAG_CMP1_Msk ) == RTC_MODE1_INTFLAG_CMP1_Msk)
    {
        compare1ValueMatch = true;

        /* Clear Compare 1 Match Flag */
        RTC_REGS->MODE1.INTFLAG.w = RTC_MODE1_INTFLAG_CMP1_Msk;
    }

    return compare1ValueMatch;
}
</#if>
</#if>
</#if>
<#if RTC_MODULE_SELECTION = "MODE0">

// *****************************************************************************
/* Function:
    void RTC${RTC_INDEX}_Timer32Start ( void )

  Summary:
    Starts the 32-bit timer.

  Description:
    This function starts the 32-bit timer. The timer will start counting up from
    the value that was set using the RTC${RTC_INDEX}_Timer32CounterSet()
    function. The timer will count at a rate configured by the input clock and
    the input prescalar.

    The timer can be configured to count up till a specific non-zero value. This
    value is specified using the RTC${RTC_INDEX}_Timer32PeriodSet() function.
    Setting a non-zero will cause the timer counter to operate as timer.
    The counter will count up to the period value and then reset and start
    counting again. This causes a period expiry event. Timer type operations are
    preferred to implement a delay or obtain periodic notification.

    Setting the period to 0 will result in a counter type operation. In this
    mode, starting the timer will cause the counter to count upto 0xFFFFFFFF and
    then overflow to 0 and continue counting. This causes an overflow event. A
    counter can be used to count in timer inputn clock units. This is useful
    when needed to perform temporal measurements.

    The counter can be stopped by calling the RTC${RTC_INDEX}_Timer32Stop
    function. Calling the RTC${RTC_INDEX}_Timer32Start() will again start
    the counting from the current counter value.

  Remarks:
    Refer plib_rtc${RTC_INDEX}.h for more information.
*/

void RTC${RTC_INDEX}_Timer32Start ( void )
{
    /* Clear all Interrupts */
    RTC_REGS->MODE0.INTFLAG.w = RTC_MODE0_INTFLAG_Msk;

<#if RTC_MODE0_INTERRUPT = true>
<#if RTC_MODE0_PERIOD != "NO">
    /* Enable Period and Overflow Interrupt */
    RTC_REGS->MODE0.INTENSET.w |= RTC_MODE0_INTENSET_${RTC_MODE0_PERIOD}_Msk | RTC_MODE0_INTENSET_OVF_Msk;
<#else>
    /* Enable Overflow Interrupt */
    RTC_REGS->MODE0.INTENSET.w |= RTC_MODE0_INTENSET_OVF_Msk;
</#if>
</#if>

    /* Enable RTC */
    RTC_REGS->MODE0.CTRLA.w |= RTC_MODE0_CTRLA_ENABLE_Msk;

    while((RTC_REGS->MODE0.SYNCBUSY.w & RTC_MODE0_SYNCBUSY_ENABLE_Msk) == RTC_MODE0_SYNCBUSY_ENABLE_Msk)
    {
        /* Wait for synchronization after Enabling RTC */
    }

}

// *****************************************************************************
/* Function:
    void RTC${RTC_INDEX}_Timer32Stop ( void )

  Summary:
    Stops the 32-bit timer from counting.

  Description:
    This function will stop the 32-bit timer from counting. Any on-going
    timing/counting operations will be affected. Stopping the timer does not
    reset the counter. This must be explicitly done by calling the
    RTC${RTC_INDEX}_Timer32CounterSet() function.

    Calling this function if the timer is already stopped will result in a
    functional no-operation. An application may need to stop the timer if it
    does not require delay services or if the counting needs to paused.

  Remarks:
    Refer plib_rtc${RTC_INDEX}.h for more information.
*/

void RTC${RTC_INDEX}_Timer32Stop ( void )
{
    /* Disable RTC */
    RTC_REGS->MODE0.CTRLA.w &= ~(RTC_MODE0_CTRLA_ENABLE_Msk);

    while((RTC_REGS->MODE0.SYNCBUSY.w & RTC_MODE0_SYNCBUSY_ENABLE_Msk) == RTC_MODE0_SYNCBUSY_ENABLE_Msk)
    {
        /* Wait for Synchronization after Disabling RTC */
    }

    /* Disable all Interrupts */
    RTC_REGS->MODE0.INTENCLR.w = RTC_MODE0_INTENCLR_Msk;
}

// *****************************************************************************
/* Function:
    void RTC${RTC_INDEX}_Timer32CounterSet ( uint32_t count )

  Summary:
    Set the 32-bit Timer Counter Value.

  Description:
    This function sets the 32-bit timer counter value. The counter will start to
    count up from this count value. The application may typically set the
    counter to 0 before starting a timing or counting operation. Calling this
    function when the timer is running will overwrite the current counter value.

  Remarks:
    Refer plib_rtc${RTC_INDEX}.h for more information.
*/

void RTC${RTC_INDEX}_Timer32CounterSet ( uint32_t count )
{
    /* Set 32Bit Counter Value */
    RTC_REGS->MODE0.COUNT.w = count;

    while((RTC_REGS->MODE0.SYNCBUSY.w & RTC_MODE0_SYNCBUSY_COUNT_Msk) == RTC_MODE0_SYNCBUSY_COUNT_Msk)
    {
        /* Wait for Synchronization after writing value to Count Register */
    }
}

// *****************************************************************************
/* Function:
    void RTC${RTC_INDEX}_Timer32PeriodSet ( uint32_t period )

  Summary:
    Set the 32-bit timer period value.

  Description:
    This function sets the 32-bit timer period value. The counter value will be
    compared against the period value and a period expiry event will occur when
    the counter matches the period. If the library is configured for interrupt
    mode and if a event handler function has been set through the
    RTC${RTC_INDEX}_Timer32CallbackRegister() function, the event handling
    function will be called.
    Additionally the RTC${RTC_INDEX}_Timer32PeriodHasExpired() function will
    return true. When the match occurs, the counter will be reset and the
    counting will start again.

    Setting the period to a non-zero value will cause the timer counter to
    operate as a timer that counts up to a specific value and resets. Setting
    the period to 0 will cause the timer counter to operate as counter, using
    the full range of the 32-bit timer, that can be used to measure a time
    duration.

  Remarks:
    Refer plib_rtc${RTC_INDEX}.h for more information.
*/

void RTC${RTC_INDEX}_Timer32PeriodSet ( uint32_t period )
{
    /* Clear Counter when there is a match */
    RTC_REGS->MODE0.CTRLA.w |= RTC_MODE0_CTRLA_MATCHCLR_Msk;

<#if RTC_MODE0_INTERRUPT = true>
    /* Enable Compare Interrupt */
    RTC_REGS->MODE0.INTENSET.w |= RTC_MODE0_INTENSET_CMP0_Msk;

</#if>
    /* Set 32Bit Compare Value */
    RTC_REGS->MODE0.COMP.w = period;

    while((RTC_REGS->MODE0.SYNCBUSY.w & RTC_MODE0_SYNCBUSY_COMP0_Msk) == RTC_MODE0_SYNCBUSY_COMP0_Msk)
    {
        /* Wait for Synchronization after writing Compare Value */
    }
}

// *****************************************************************************
/* Function:
    uint32_t RTC${RTC_INDEX}_Timer32CounterGet ( void )

  Summary:
    Get the current 32-bit counter value.

  Description:
    This function returns the current 32-bit count value. This function can be
    used to retrieve the counter value at the end of a time measurement.

  Remarks:
    Refer plib_rtc${RTC_INDEX}.h for more information.
*/

uint32_t RTC${RTC_INDEX}_Timer32CounterGet ( void )
{
    uint32_t count = 0;

    while((RTC_REGS->MODE0.SYNCBUSY.w & RTC_MODE0_SYNCBUSY_COUNTSYNC_Msk) == RTC_MODE0_SYNCBUSY_COUNTSYNC_Msk)
    {
        /* Wait for Synchronization before reading value from Count Register */
    }

    /* Get 32Bit Count Value from COUNT register */
    count = RTC_REGS->MODE0.COUNT.w;

    return count;
}

// *****************************************************************************
/* Function:
    uint32_t RTC${RTC_INDEX}_Timer32PeriodGet ( void )

  Summary:
    Get 32-bit timer period Value.

  Description:
    This function returns the 32-bit timer period value which used to compare
    with the current counter value. This value will match the value that was set
    using the RTC${RTC_INDEX}_Timer32PeriodSet() function.

  Remarks:
    Refer plib_rtc${RTC_INDEX}.h for more information.
*/

uint32_t RTC${RTC_INDEX}_Timer32PeriodGet ( void )
{
    /* Get 32Bit Compare Value */
    return (RTC_REGS->MODE0.COMP.w);
}

// *****************************************************************************
/* Function:
    uint32_t RTC${RTC_INDEX}_Timer32FrequencyGet ( void )

  Summary:
    Returns the frequency at which the 32-bit timer counter is operating.

  Description:
    This function returns the frequency at which the 32-bit timer counter is
    operating. The return value can be used to compute the period that needs to
    be set in order to operate the timer counter at a desired frequency.

  Remarks:
    Refer plib_rtc${RTC_INDEX}.h for more information.
*/

uint32_t RTC${RTC_INDEX}_Timer32FrequencyGet ( void )
{
    /* Return Frequency of RTC Clock */
    return RTC_CLOCK_FREQUENCY;
}
<#else>

// *****************************************************************************
/* Function:
    void RTC${RTC_INDEX}_Timer16Start ( void )

  Summary:
    Starts the 16-bit timer.

  Description:
    This function starts the 16-bit timer. The timer will start counting up from
    the value that was set using the RTC${RTC_INDEX}_Timer16CounterSet()
    function. The timer will count at a rate configured by the input clock and
    the input prescalar.

    The timer can be configured to count up till a specific non-zero value. This
    value is specified using the RTC${RTC_INDEX}_Timer16PeriodSet() function.
    Setting a non-zero will cause the timer counter to operate as timer.
    The counter will count up to the period value and then reset and start
    counting again. This causes a period expiry event. Timer type operations are
    preferred to implement a delay or obtain periodic notification.

    Setting the period to 0 will result in a counter type operation. In this
    mode, starting the timer will cause the counter to count up to 0xFFFF and
    then overflow to 0 and continue counting. This causes an overflow event. A
    counter can be used to count in timer input clock units. This is useful
    when needed to perform temporal measurements.

    The counter can be stopped by calling the RTC${RTC_INDEX}_Timer16Stop
    function. Calling the RTC${RTC_INDEX}_Timer16Start() will again start the
    counting from the current counter value.

  Remarks:
    Refer plib_rtc${RTC_INDEX}.h for more information.
*/

void RTC${RTC_INDEX}_Timer16Start ( void )
{
    /* Clear all Interrupts */
    RTC_REGS->MODE1.INTFLAG.w = RTC_MODE1_INTFLAG_Msk;

<#if RTC_MODE1_INTERRUPT = true>
<#if RTC_MODE1_PERIOD != "NO">
    /* Enable Period and Overflow Interrupt */
    RTC_REGS->MODE1.INTENSET.w |= RTC_MODE1_INTENSET_${RTC_MODE1_PERIOD}_Msk | RTC_MODE1_INTENSET_OVF_Msk;
<#else>
    /* Enable Overflow Interrupt */
    RTC_REGS->MODE1.INTENSET.w |= RTC_MODE1_INTENSET_OVF_Msk;
</#if>
</#if>

    /* Enable RTC */
    RTC_REGS->MODE1.CTRLA.w |= RTC_MODE1_CTRLA_ENABLE_Msk;

    while((RTC_REGS->MODE1.SYNCBUSY.w & RTC_MODE1_SYNCBUSY_ENABLE_Msk) == RTC_MODE1_SYNCBUSY_ENABLE_Msk)
    {
        /* Wait for Synchronization after Enabling RTC */
    }
}

// *****************************************************************************
/* Function:
    void RTC${RTC_INDEX}_Timer16Stop ( void )

  Summary:
    Stops the 16-bit timer from counting.

  Description:
    This function will stop the 16-bit timer from counting. Any on-going
    timing/counting operations will be affected. Stopping the timer does not
    reset the counter. This must be explicitly done by calling the
    RTC${RTC_INDEX}_Timer16CounterSet() function.

    Calling this function if the timer is already stopped will result in a
    functional no-operation. An application may need to stop the timer if it
    does not require delay services or if the counting needs to paused.

  Remarks:
    Refer plib_rtc${RTC_INDEX}.h for more information.
*/

void RTC${RTC_INDEX}_Timer16Stop ( void )
{
    /* Disable RTC */
    RTC_REGS->MODE1.CTRLA.w &= ~(RTC_MODE1_CTRLA_ENABLE_Msk);

    while((RTC_REGS->MODE1.SYNCBUSY.w & RTC_MODE1_SYNCBUSY_ENABLE_Msk) == RTC_MODE1_SYNCBUSY_ENABLE_Msk)
    {
        /* Wait for Synchronization after Disabling RTC */
    }

    /* Disable all Interrupts */
    RTC_REGS->MODE1.INTENCLR.w = RTC_MODE1_INTENCLR_Msk;
}

// *****************************************************************************
/* Function:
    void RTC${RTC_INDEX}_Timer16CounterSet ( uint16_t count )

  Summary:
    Set the 16-bit Timer Counter Value.

  Description:
    This function sets the 16-bit timer counter value. The counter will start to
    count up from this count value. The application may typically set the
    counter to 0 before starting a timing or counting operation. Calling this
    function when the timer is running will overwrite the current counter value.

  Remarks:
    Refer plib_rtc${RTC_INDEX}.h for more information.
*/

void RTC${RTC_INDEX}_Timer16CounterSet ( uint16_t count )
{
    /* Set 16Bit Count Value to COUNT Register */
    RTC_REGS->MODE1.COUNT.w = count;

    while((RTC_REGS->MODE1.SYNCBUSY.w & RTC_MODE1_SYNCBUSY_COUNT_Msk) == RTC_MODE1_SYNCBUSY_COUNT_Msk)
    {
        /* Wait for Synchronization after writing value to Count Register */
    }
}

// *****************************************************************************
/* Function:
    void RTC${RTC_INDEX}_Timer16PeriodSet ( uint16_t period )

  Summary:
    Set the 16-bit timer period value.

  Description:
    This function sets the 16-bit timer period value. The counter value will be
    compared against the period value and a period expiry event will occur when
    the counter matches the period. If the library is configured for interrupt
    mode and if a event handler function has been set through the
    RTC${RTC_INDEX}_Timer16CallbackRegister() function, the event handling
    function will be called.
    Additionally the RTC${RTC_INDEX}_Timer16PeriodHasExpired() function will
    return true. When the match occurs, the counter will be reset and the
    counting will start again.

    Setting the period to a non-zero value will cause the timer counter to
    operate as a timer that counts up to a specific value and resets. Setting
    the period to 0 will cause the timer counter to operate as counter, using
    the full range of the 16-bit timer, that can be used to measure a time
    duration.

  Remarks:
    Refer plib_rtc${RTC_INDEX}.h for more information.
*/

void RTC${RTC_INDEX}_Timer16PeriodSet ( uint16_t period )
{
    /* Set maximum 16Bit Counter Period */
    RTC_REGS->MODE1.PER.w = period;

    while((RTC_REGS->MODE1.SYNCBUSY.w & RTC_MODE1_SYNCBUSY_PER_Msk) == RTC_MODE1_SYNCBUSY_PER_Msk)
    {
        /* Wait for Synchronization after writing Counter Period */
    }
}

// *****************************************************************************
/* Function:
  uint16_t RTC${RTC_INDEX}_Timer16CounterGet ( void )

  Summary:
    Get the current 16-bit counter value.

  Description:
    This function returns the current 16-bit count value. This function can be
    used to retrieve the counter value at the end of a time measurement.

  Remarks:
    Refer plib_rtc${RTC_INDEX}.h for more information.
*/

uint16_t RTC${RTC_INDEX}_Timer16CounterGet ( void )
{
    uint16_t count = 0;

    while((RTC_REGS->MODE1.SYNCBUSY.w & RTC_MODE1_SYNCBUSY_COUNTSYNC_Msk) == RTC_MODE1_SYNCBUSY_COUNTSYNC_Msk)
    {
        /* Wait for Synchronization after reading value from Count Register */
    }

    /* Get 16Bit Count Value from COUNT Register */
    count = RTC_REGS->MODE1.COUNT.w;

    return count;
}

// *****************************************************************************
/* Function:
    uint16_t RTC${RTC_INDEX}_Timer16PeriodGet ( void )

  Summary:
    Get 16-bit timer period Value.

  Description:
    This function returns the 16-bit timer period value which used to compare
    with the current counter value. This value will match the value that was set
    using the RTC${RTC_INDEX}_Timer16PeriodSet() function.

  Remarks:
    Refer plib_rtc${RTC_INDEX}.h for more information.
*/

uint16_t RTC${RTC_INDEX}_Timer16PeriodGet ( void )
{
    /* Get 16Bit Compare Value */
    return (RTC_REGS->MODE1.PER.w);
}
<#if RTC_MODE1_GENERATE_COMPARE0_API = true>

// *****************************************************************************
/* Function:
    void RTC${RTC_INDEX}_Timer16Compare0Set ( uint16_t comparisionValue )

  Summary:
    Set the 16-Bit Counter Compare 0 Value.

  Description:
    This function will set the Counter Compare 0 Value. The module will compare
    the counter against this value and will signal a match when the counter
    equals the compare value. If the library was configured for interrupt mode,
    the Compare 0 event is enabled and if a valid callback is registered, the
    library will call the registered callback function with the
    RTC_TIMER16_EVENT_COMPARE0_MATCH event.
    The RTC${RTC_INDEX}_Timer16Compare0HasMatched() function will return true
    when the match occurs.

  Remarks:
    Refer plib_rtc${RTC_INDEX}.h for more information.
*/

void RTC${RTC_INDEX}_Timer16Compare0Set ( uint16_t comparisionValue )
{
     /* Set 16Bit Compare Value */
     RTC_REGS->MODE1.COMP[0].w = comparisionValue;

     while((RTC_REGS->MODE1.SYNCBUSY.w & RTC_MODE1_SYNCBUSY_COMP0_Msk) == RTC_MODE1_SYNCBUSY_COMP0_Msk)
     {
         /* Wait for Synchronization after writing Compare Value */
     }
}
</#if>
<#if RTC_MODE1_GENERATE_COMPARE1_API = true>

// *****************************************************************************
/* Function:
    void RTC${RTC_INDEX}_Timer16Compare1Set ( uint16_t comparisionValue )

  Summary:
    Set the 16-Bit Counter Compare 1 Value.

  Description:
    This function will set the Counter Compare 1 Value. The module will compare
    the counter against this value and will signal a match when the counter
    equals the compare value. If the library was configured for interrupt mode,
    the Compare 1 event is enabled and if a valid callback is registered, the
    library will call the registered callback function with the
    RTC_TIMER16_EVENT_COMPARE0_MATCH event.
    The RTC${RTC_INDEX}_Timer16Compare1HasMatched() function will return true
    when the match occurs.

  Remarks:
    Refer plib_rtc${RTC_INDEX}.h for more information.
*/

void RTC${RTC_INDEX}_Timer16Compare1Set ( uint16_t comparisionValue )
{
    /* Set 16Bit Compare Value */
    RTC_REGS->MODE1.COMP[1].w = comparisionValue;

    while((RTC_REGS->MODE1.SYNCBUSY.w & RTC_MODE1_SYNCBUSY_COMP1_Msk) == RTC_MODE1_SYNCBUSY_COMP1_Msk)
    {
        /* Wait for Synchronization after writing Compare Value */
    }
}
</#if>

// *****************************************************************************
/* Function:
    uint32_t RTC${RTC_INDEX}_Timer16FrequencyGet ( void )

  Summary:
    Returns the frequency at which the 16-bit timer counter is operating.

  Description:
    This function returns the frequency at which the 16-bit timer counter is
    operating. The return value can be used to compute the period that needs to
    be set in order to operate the timer counter at a desired frequency.

  Remarks:
    Refer plib_rtc${RTC_INDEX}.h for more information.
*/

uint32_t RTC${RTC_INDEX}_Timer16FrequencyGet ( void )
{
    /* Return Frequency of RTC Clock */
    return RTC_CLOCK_FREQUENCY;
}
<#if RTC_MODE1_INTERRUPT = true>
<#if RTC_MODE1_GENERATE_COMPARE1_API = true>

// *****************************************************************************
/* Function:
    void RTC${RTC_INDEX}_Timer16Compare1EventEnable (bool enable)

  Summary:
    Enables or disables Compare 1 Match Event Generation.

  Description:
    This function allows the application to control the generation of the
    Compare 1 Match Event.  If this function is called with enable set to true,
    the Compare 1 Match Event generation is enabled and the registered event
    handling callback function will be called with the
    RTC_TIMER16_EVENT_COMPARE1_MATCH when a Compare 1 Value match has occurred.

  Remarks:
    Refer plib_rtc${RTC_INDEX}.h for more information.
*/

void RTC${RTC_INDEX}_Timer16Compare1EventEnable (bool enable)
{
    if(enable)
    {
        /* Enable Comparator1 comparison */
        RTC_REGS->MODE1.INTENSET.w |= RTC_MODE1_INTENSET_CMP1_Msk;
    }
    else
    {
        /* Disable Comparator1 comparison */
        RTC_REGS->MODE1.INTENSET.w &= ~(RTC_MODE1_INTENSET_CMP1_Msk);
    }
}
</#if>
</#if>
<#if RTC_MODE1_INTERRUPT = true>
<#if RTC_MODE1_GENERATE_COMPARE0_API = true>

// *****************************************************************************
/* Function:
    void RTC${RTC_INDEX}_Timer16Compare0EventEnable (bool enable)

  Summary:
    Enables or disables Compare 0 Match Event Generation.

  Description:
    This function allows the application to control the generation of the
    Compare 0 Match Event.  If this function is called with enable set to true,
    the Compare 0 Match Event generation is enabled and the registered event
    handling callback function will be called with the
    RTC_TIMER16_EVENT_COMPARE0_MATCH when a Compare 0 Value match has occurred.

  Remarks:
    Refer plib_rtc${RTC_INDEX}.h for more information.
*/

void RTC${RTC_INDEX}_Timer16Compare0EventEnable(bool enable)
{
    if(enable)
    {
        /* Enable Comparator0 comparison */
        RTC_REGS->MODE1.INTENSET.w |= RTC_MODE1_INTENSET_CMP0_Msk;
    }
    else
    {
        /* Disable Comparator0 comparison */
        RTC_REGS->MODE1.INTENSET.w &= ~(RTC_MODE1_INTENSET_CMP0_Msk);
    }
}
</#if>
</#if>
</#if>
<#if (RTC_MODE0_INTERRUPT = true && RTC_MODULE_SELECTION = "MODE0") ||
     (RTC_MODE1_INTERRUPT = true && RTC_MODULE_SELECTION = "MODE1") >
<#if RTC_MODE0_PERIOD != "NO" || RTC_MODE1_PERIOD != "NO" >

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
    rtc${RTC_INDEX}Obj.context  = context;
}
</#if>
<#if RTC_MODULE_SELECTION = "MODE0" >

// *****************************************************************************
/* Function:
    void RTC${RTC_INDEX}_Timer32CallbackRegister( RTC_TIMER32_CALLBACK callback,
                                                  uintptr_t context )

  Summary:
    Register the callback function to be called when an 32-bit Timer Interrupt
    occurs.

  Description:
    This function registers the  callback function  that the library will call
    when an interrupt occurs. The library will return the event that has caused
    the interrupt and the application specified context in the callback
    function.

  Remarks:
    Refer plib_rtc${RTC_INDEX}.h for more information.
*/

void RTC${RTC_INDEX}_Timer32CallbackRegister ( RTC_TIMER32_CALLBACK callback, uintptr_t context )
{
    rtc${RTC_INDEX}Obj.timer32BitCallback = callback;
    rtc${RTC_INDEX}Obj.context            = context;
}
<#else>

// *****************************************************************************
/* Function:
    void RTC${RTC_INDEX}_Timer16CallbackRegister ( RTC_TIMER16_CALLBACK callback,
                                                   uintptr_t context )

  Summary:
    Register the callback function to be called when an 16-bit Timer Interrupt
    occurs.

  Description:
    This function registers the  callback function  that the library will call
    when an interrupt occurs. The library will return the event that has caused
    the interrupt and the application specified context in the callback
    function.

  Remarks:
    Refer plib_rtc${RTC_INDEX}.h for more information.
*/

void RTC${RTC_INDEX}_Timer16CallbackRegister ( RTC_TIMER16_CALLBACK callback, uintptr_t context )
{
    rtc${RTC_INDEX}Obj.timer16BitCallback = callback;
    rtc${RTC_INDEX}Obj.context            = context;
}
</#if>

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
<#if RTC_MODULE_SELECTION = "MODE0">
<#if RTC_MODE0_PERIOD != "NO">
    /* Check Periodic interval has expired */
    if((RTC_REGS->MODE0.INTFLAG.w & RTC_MODE0_INTFLAG_${RTC_MODE0_PERIOD}_Msk) == RTC_MODE0_INTFLAG_${RTC_MODE0_PERIOD}_Msk)
    {
        if(rtc${RTC_INDEX}Obj.periodicCallback != NULL)
        {
            rtc${RTC_INDEX}Obj.periodicCallback(rtc${RTC_INDEX}Obj.context);
        }
    }

</#if>
    /* Check Period and Overflow has expired */
    if((RTC_REGS->MODE0.INTFLAG.w & RTC_REGS->MODE0.INTENSET.w) & RTC_32BIT_INTERRUPT_MASK)
    {
        /* Update the event in RTC Peripheral Callback object */
        rtc${RTC_INDEX}Obj.timer32BitEvent = RTC_REGS->MODE0.INTFLAG.w;

        /* Invoke registered Callback function */
        if(rtc${RTC_INDEX}Obj.timer32BitCallback != NULL)
        {
            rtc${RTC_INDEX}Obj.timer32BitCallback( rtc${RTC_INDEX}Obj.timer32BitEvent, rtc${RTC_INDEX}Obj.context );
        }
    }

    /* Clear all Interrupts */
    RTC_REGS->MODE0.INTFLAG.w = RTC_MODE0_INTFLAG_Msk;
<#else>
<#if RTC_MODE1_PERIOD != "NO">

    /* Check Periodic interval has expired */
    if((RTC_REGS->MODE1.INTFLAG.w & RTC_MODE1_INTFLAG_${RTC_MODE1_PERIOD}_Msk) == RTC_MODE1_INTFLAG_${RTC_MODE1_PERIOD}_Msk)
    {
        if(rtc${RTC_INDEX}Obj.periodicCallback != NULL)
        {
            rtc${RTC_INDEX}Obj.periodicCallback(rtc${RTC_INDEX}Obj.context);
        }
    }

</#if>
    /* Check Compare 0, Compare 1 and Overflow Interrupt */
    if((RTC_REGS->MODE1.INTFLAG.w & RTC_REGS->MODE1.INTENSET.w) & RTC_16BIT_INTERRUPT_MASK)
    {
        /* Update the event in RTC Peripheral Callback object */
        rtc${RTC_INDEX}Obj.timer16BitEvent = RTC_REGS->MODE1.INTFLAG.w;

        /* Invoke registered Callback function */
        if(rtc${RTC_INDEX}Obj.timer16BitCallback != NULL)
        {
            rtc${RTC_INDEX}Obj.timer16BitCallback( rtc${RTC_INDEX}Obj.timer16BitEvent, rtc${RTC_INDEX}Obj.context );
        }
    }

    /* Clear all Interrupts */
    RTC_REGS->MODE1.INTFLAG.w = RTC_MODE1_INTFLAG_Msk;
</#if>
}
</#if>