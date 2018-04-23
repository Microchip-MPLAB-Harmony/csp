/*******************************************************************************
  Real Time Counter (RTC${RTC_INDEX}) PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_rtc${RTC_INDEX}.h

  Summary:
    RTC${RTC_INDEX} PLIB Header file

  Description:
    This file defines the interface to the RTC peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

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

#ifndef PLIB_RTC${RTC_INDEX}_H
#define PLIB_RTC${RTC_INDEX}_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
/*
 * This section lists the other files that are included in this file.
 */

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

<#if RTC_MODE2_INTERRUPT = true && RTC_MODULE_SELECTION = "MODE2" ||
     RTC_MODE1_INTERRUPT = true && RTC_MODULE_SELECTION = "MODE1" ||
     RTC_MODE0_INTERRUPT = true && RTC_MODULE_SELECTION = "MODE0" >
// *****************************************************************************
// *****************************************************************************
// Section: Data Types
// *****************************************************************************
// *****************************************************************************
/* The following functions make up the data types required by this interface. */

<#if RTC_MODULE_SELECTION = "MODE2">
// *****************************************************************************
/* RTC Alarm Mask Settings

  Summary:
    Possible RTC Alarm Mask Settings.

  Description:
    The RTC peripheral while operating in RTCC mode will generate an alarm by
    matching the configured alarm time and date with current time and date.
    The date and time field to be considered while matching are specified with
    the RTC Alarm Mask.
    The mask should be specified in the RTC${RTC_INDEX}_RTCCAlarmSet() function.

    For example, setting the mask to RTC_ALARM_MASK_MMSS will only match the
    minute and the seconds field of the specified alarm time and will ignore all
    other fields.

  Remarks:
    None.
*/

typedef enum
{
    /* Only match seconds field and ignore all other date and time fields */
    RTC_ALARM_MASK_SS = 0x1,

    /*
     * Only match seconds and minutes fields and ignore all other date and time
     * fields.
     */
    RTC_ALARM_MASK_MMSS,

    /*
     * Only match seconds, minutes and hour fields and ignore all other date
     * fields.
     */
    RTC_ALARM_MASK_HHMMSS,

    /*
     * Only match seconds, minutes, hour and day field and ignore all other date
     * fields.
     */
    RTC_ALARM_MASK_DDHHMMSS,

    /*
     * Only match seconds, minutes, hour, day and month fields and ignore all
     * other date fields.
     */
    RTC_ALARM_MASK_MMDDHHMMSS,

    /* Match all date and time fields. */
    RTC_ALARM_MASK_YYMMDDHHMMSS

} RTC_ALARM_MASK;

// *****************************************************************************
/* RTC Real Time Clock Calendar (RTCC) Mode events

  Summary:
    Possible RTC RTCC Mode Events.

  Description:
    This enumeration defines the possible events that can occur when the RTC
    peripheral is configured for Real Time Clock Calendar operation. These
    events are passed into the callback function registered through the
    RTC${RTC_INDEX}_RTCCCallbackRegister() function.

  Remarks:
    None.
*/

typedef enum
{
    /* An alarm has occurred. */
    RTC_CLOCK_EVENT_ALARM = 0x0100,

    /* The year counter has overflowed its maximum range of 64 */
    RTC_CLOCK_EVENT_YEAR_OVERFLOW = 0x8000

} RTC_CLOCK_EVENT;
<#elseif RTC_MODULE_SELECTION = "MODE0">
// *****************************************************************************
/* RTC 32-bit Timer Counter Mode Event

  Summary:
    Possible RTC 32-bit Timer Counter Mode Events.

  Description:
    This enumeration defines the possible events that can occur when the RTC
    peripheral is configured for 32-bit Timer Counter mode operation. These
    events are passed into the callback function registered through the
    RTC${RTC_INDEX}_Timer32CallbackRegister() function.

  Remarks:
    None.
*/

typedef enum
{
    /* The timer period has matched */
    RTC_TIMER32_EVENT_PERIOD_MATCH = 0x0100,

    /* The counter has overflowed */
    RTC_TIMER32_EVENT_COUNTER_OVERFLOW = 0x8000

} RTC_TIMER32_EVENT;
<#else>
// *****************************************************************************
/* RTC 16-bit Timer Counter Mode Event

  Summary:
    Possible RTC 16-bit Timer Counter Mode Events.

  Description:
    This enumeration defines the possible events that can occur when the RTC
    peripheral is configured for 16-bit Timer Counter mode operation. These
    events are passed into the callback function registered through the
    RTC${RTC_INDEX}_Timer16CallbackRegister() function.

  Remarks:
    None.
*/

typedef enum
{
    /*
     * The counter has matched the Compare 0 value. This event will be available
     * only if Compare 0 API is enabled in MHC.
     */
    RTC_TIMER16_EVENT_COMPARE0_MATCH = 0x0100,

    /*
     * The counter has matched the Compare 1 value. This event will be available
     * only if Compare 1 API is enabled in MHC.
     */
    RTC_TIMER16_EVENT_COMPARE1_MATCH = 0x0200,

    /* The timer period has matched */
    RTC_TIMER16_EVENT_PERIOD_MATCH = 0x8000

} RTC_TIMER16_EVENT;

</#if>
</#if>
<#if RTC_MODE2_INTERRUPT = true && RTC_MODULE_SELECTION = "MODE2" ||
     RTC_MODE1_INTERRUPT = true && RTC_MODULE_SELECTION = "MODE1" ||
     RTC_MODE0_INTERRUPT = true && RTC_MODULE_SELECTION = "MODE0" >

// *****************************************************************************
// *****************************************************************************
// Section: Interface Routine Pointers
// *****************************************************************************
// *****************************************************************************
/* The following interface rountine pointers are required by this interface. */

// *****************************************************************************
/* Periodic Interval Callback Function Pointer Type

  Summary:
    Defines the data type and function signature of the RTC Periodc Interval
    callback function.

  Description:
    This data type defines the function signature of the RTC Periodic Interval
    Callback function. The RTC peripheral will call back the client's function
    with this signature everytime when the configured periodic interval has
    completed.

    The application should register a callback function whose signature (input
    arguments and return type) must match the signature of this function. The
    calllback function should be registered by calling the
    RTC${RTC_INDEX}_PeriodicIntervalCallbackRegister() function. The callback
    function should be registered before starting the timer.

  Precondition:
    The RTC${RTC_INDEX}_Initialize() function should have been called to
    initialize the RTC peripheral.
    The RTC${RTC_INDEX}_PeriodicIntervalCallbackRegister() function should have
    been called to register the callback function. The Periodic Interval should
    have been configured in MHC.

  Parameters:
    context  - Allows the caller to provide a context value (usually a pointer
    to the callers context for multi-instance clients).

  Returns:
    None.

  Example:
    <code>

    bool peridoicIntervalHadExpired = false;

    void MyPeriodIntervalCallback ( uintptr_t context )
    {
        bool flag = (bool *)(context);
        flag = true;
    }

    // Initialize the RTC Peripheral and register the callback function.
    // Note how the pointer to the peridoicIntervalHadExpired flag is specified
    // as the context. This is passed back into the callback function.

    RTC${RTC_INDEX}_Initialize();
    RTC${RTC_INDEX}_PeriodicIntervalCallbackRegister( MyPeriodIntervalCallback,
                                           &peridoicIntervalHadExpired);

    </code>

   Remarks:
    The Periodic Interval feature is available in all operational modes of the
    RTC peripheral. The callback function will be execute in an interrupt
    context. Avoid calling blocking function , performing computationally
    intensive operations or calling interrupt un-safe functions from the
    callback function.
*/

typedef void (*RTC_PERIODIC_INTERVAL_CALLBACK)( uintptr_t context );

<#if RTC_MODULE_SELECTION = "MODE0" >

// *****************************************************************************
/* RTC 32-bit Timer Counter Callback Function Pointer Type

  Summary:
    Defines the data type and function signature of the RTC 32-bit Timer
    Counter callback function.

  Description:
    This data type defines the function signature of the RTC 32-bit Timer
    Counter Callback function. The RTC peripheral will call back the client's
    function with this signature every time when the 32-bit Time Counter related
    event has occurred. Refer to the description of the RTC_TIMER32_EVENT
    enumeration for possible events. Hardware event flags are cleared when the
    callback function exits.

    The application should register a callback function whose signature (input
    arguments and return type) must match the signature of this function. The
    calllback function should be registered by calling the
    RTC${RTC_INDEX}_Timer32CallbackRegister() function. The callback function
    should be registered before starting the timer.

  Precondition:
    The RTC${RTC_INDEX}_Initialize() function should have been called to
    initialize the RTC peripheral. The RTC${RTC_INDEX}_Timer32CallbackRegister()
    function should have been called to register the callback function.
    The RTC peripheral should have been configured for 32-bit Timer Counter mode
    in MHC. The RTC peripheral should have been configured for Interrupt mode
    operation in MHC.

  Parameters:

    event - The 32-bit Timer Counter event that caused the callback function to
    be called. Multiple events can be active. The application should check for
    all events in the callback function.

    context  - Allows the caller to provide a context value (usually a pointer
    to the callers context for multi-instance clients).

  Returns:
    None.

  Example:
    <code>

    void MyTimer32Callback (RTC_TIMER32_EVENT event, uintptr_t context )
    {
        if((event & RTC_TIMER32_EVENT_PERIOD_MATCH) ==
                                                RTC_TIMER32_EVENT_PERIOD_MATCH)
        {
            // The period has matched.
        }
        else if((event & RTC_TIMER32_EVENT_COUNTER_OVERFLOW) ==
                                            RTC_TIMER32_EVENT_COUNTER_OVERFLOW)
        {
            // Counter has overflowed.
        }
    }

    // Initialize the RTC Peripheral and register the callback function.
    // Note how the pointer to the peridoicIntervalHadExpired flag is specified
    // as the context. This is passed back into the callback function.

    RTC${RTC_INDEX}_Initialize();
    RTC${RTC_INDEX}_Timer32CounterSet(0);
    RTC${RTC_INDEX}_Timer32PeriodSet(0xFFF);
    RTC${RTC_INDEX}_Timer32CallbackRegister(MyTimer32Callback, NULL);
    RTC${RTC_INDEX}_Timer32Start();

    </code>

   Remarks:
    This callback if only available when the RTC peripheral is configured for
    32-bit Timer Counter operation. The callback function will be execute in an
    interrupt context. Avoid calling blocking , computationally intensive or
    interrupt un-safe function from the callback function.

*/

typedef void (*RTC_TIMER32_CALLBACK)( RTC_TIMER32_EVENT event, uintptr_t context );
<#elseif RTC_MODULE_SELECTION = "MODE2">

// *****************************************************************************
/* Real Time Clock Calendar Callback Function Pointer Type

  Summary:
    Defines the data type and function signature of the Real Time Clock Calendar
    callback function.

  Description:
    This data type defines the function signature of the RTC Real Time Clock
    Calendar Callback function. The RTC peripheral will call back the client's
    function with this signature when the configured RTCC Alarm has occurred.

    The application should register a callback function whose signature (input
    arguments and return type) must match the signature of this function. The
    calllback function should be registered by calling the
    RTC${RTC_INDEX}_RTCCCallbackRegister() function. The callback function
    should be registered before setting the alarm.

  Precondition:
    The RTC${RTC_INDEX}_Initialize() function should have been called to
    initialize the RTC peripheral. The RTC${RTC_INDEX}_RTCCCallbackRegister()
    function should have been called to register the callback function. The RTC
    peripheral  should have been configured for RTCC operation in MHC.
    The RTC peripheral should have been configured for interrupt mode of
    operation in MHC.

  Parameters:
    event - RTCC event that caused the callback function to be called. Multiple
    events could be active. Application should process all events in the
    callback function.

    context  - Allows the caller to provide a context value (usually a pointer
    to the callers context for multi-instance clients).

  Returns:
    None.

  Example:
    <code>

    void MyRTCCCallback ( RTC_CLOCK_EVENT event, uintptr_t context )
    {
        if((event & RTC_CLOCK_EVENT_YEAR_OVERFLOW) ==
                                                RTC_CLOCK_EVENT_YEAR_OVERFLOW)
        {
            // This means a year overflow has occurred.
        }
        else if ((event & RTC_CLOCK_EVENT_ALARM) == RTC_CLOCK_EVENT_ALARM)
        {
            // This means an alarm has occurred.
        }
    }

    // Initialize the RTC Peripheral and register the callback function.
    // Note how the pointer to the alarmOccurred flag is specified
    // as the context. This is passed back into the callback function.
    // Refer to the description of the RTC${RTC_INDEX}_RTCCTimeSet() and
    // RTC${RTC_INDEX}_RTCCAlarmSet() function for API usage details.

    RTC${RTC_INDEX}_Initialize();
    RTC${RTC_INDEX}_RTCCTimeSet(&time);
    RTC${RTC_INDEX}_RTCCAlarmSet(&alarm);
    RTC${RTC_INDEX}_PeriodicIntervalCallbackRegister( MyRTCCCallback,
                                                      &alarmOccurred);

    </code>

   Remarks:
    The Real Time Clock Calendar feature is available whe the RTC peripheral is
    configured for Real Time Clock Calendar mode. The callback function will be
    execute in an interrupt context. Avoid calling blocking functions ,
    performing computationally intensive operations or interrupt un-safe
    functions from the callback function.
*/

typedef void (*RTC_CALLBACK)( RTC_CLOCK_EVENT event, uintptr_t context );
<#else>

// *****************************************************************************
/* RTC 16-bit Timer Counter Callback Function Pointer Type

  Summary:
    Defines the data type and function signature of the RTC 16-bit Timer
    Counter callback function.

  Description:
    This data type defines the function signature of the RTC 16-bit Timer
    Counter Callback function. The RTC peripheral will call back the client's
    function with this signature everytime when the 16-bit Time Counter related
    event has occurred. Refer to the description of the RTC_TIMER16_EVENT
    enumeration for possible events. Hardware event flags are cleared when the
    callback function exits.

    The application should register a callback function whose signature (input
    arguments and return type) must match the signature of this function. The
    calllback function should be registered by calling the
    RTC${RTC_INDEX}_Timer16CallbackRegister() function. The callback function
    should be registered before starting the timer.

  Precondition:
    The RTC${RTC_INDEX}_Initialize() function should have been called to
    initialize the RTC peripheral. The RTC${RTC_INDEX}_Timer16CallbackRegister()
    function should have been called to register the callback function.
    The RTC peripheral should have been configured for 16-bit Timer Counter mode
    in MHC. The RTC peripheral should have been configured for Interrupt mode
    operation in MHC.

  Parameters:

    event - The 16-bit Timer Counter event that caused the callback function to
    be called. Multiple events can be active. The application should check for
    all events in the callback function.

    context  - Allows the caller to provide a context value (usually a pointer
    to the callers context for multi-instance clients).

  Returns:
    None.

  Example:
    <code>

    void MyTimer16Callback (RTC_TIMER16_EVENT event, uintptr_t context )
    {
        if((event & RTC_TIMER16_EVENT_PERIOD_MATCH) ==
                                                RTC_TIMER16_EVENT_PERIOD_MATCH)
        {
            // The period has matched.
        }
        else if((event & RTC_TIMER16_EVENT_COMPARE1_MATCH) ==
                                              RTC_TIMER16_EVENT_COMPARE1_MATCH)
        {
            // Compare 1 value has matched.
        }
        else if((event & RTC_TIMER16_EVENT_COMPARE0_MATCH) ==
                                              RTC_TIMER16_EVENT_COMPARE0_MATCH)
        {
            // Compare 0 value has matched.
        }
    }

    // Initialize the RTC Peripheral and register the callback function.
    // Note how the pointer to the peridoicIntervalHadExpired flag is specified
    // as the context. This is passed back into the callback function.

    RTC${RTC_INDEX}_Initialize();
    RTC${RTC_INDEX}_Timer16CounterSet(0);
    RTC${RTC_INDEX}_Timer16PeriodSet(0xFFF);
    RTC${RTC_INDEX}_Timer16CallbackRegister(MyTimer16Callback, NULL);
    RTC${RTC_INDEX}_Timer16Start();

    </code>

   Remarks:
    This callback if only available when the RTC peripheral is configured for
    16-bit Timer Counter operation. The callback function will be execute in an
    interrupt context. Avoid calling blocking , computationally intensive or
    interrupt un-safe function from the callback function.

*/

typedef void (*RTC_TIMER16_CALLBACK)( RTC_TIMER16_EVENT event, uintptr_t context );
</#if>

</#if>
// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************
/*
 * The following functions make up the methods (set of possible operations) of
 * this interface.
 */

// *****************************************************************************
/* Function:
    void RTC${RTC_INDEX}_Initialize(void)

  Summary:
    Initialize given instance of the RTC peripheral.

  Description:
    This function initialize the given instance of the RTC peripheral as
    configured by the user from the MHC.

  Precondition:
    None.

  Parameters:
    None.

  Returns:
    None.

  Example:
    <code>
        RTC${RTC_INDEX}_Initialize();
    </code>

  Remarks:
    This function should be called prior to calling any other RTC peripheral
    library function.
*/

void RTC${RTC_INDEX}_Initialize(void);
<#if (RTC_MODE0_FREQCORR = true && RTC_MODULE_SELECTION = "MODE0") ||
     (RTC_MODE1_FREQCORR = true && RTC_MODULE_SELECTION = "MODE1") ||
     (RTC_MODE2_FREQCORR = true && RTC_MODULE_SELECTION = "MODE2")  >

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

  Precondition:
    RTC${RTC_INDEX}_Initialize must have been called for the associated
    RTC instance. The Generate Frequency Correction API option in MHC should
    have been selected.

  Parameters:
    correction - Signed 8 bit correction value. If no correction is needed, set
    value to zero.

  Returns:
    None.

  Example:
    <code>
        RTC${RTC_INDEX}_Initialize();

        // Positive correction. This reduces frequency.
        RTC${RTC_INDEX}_FrequencyCorrect(5);

        // Negatvie correction. This increase frequency.
        RTC${RTC_INDEX}_FrequencyCorrect(-10);
    </code>

  Remarks:
    None.
*/

void RTC${RTC_INDEX}_FrequencyCorrect (int8_t correction);
</#if>
<#if (RTC_MODE0_INTERRUPT = false && RTC_MODULE_SELECTION = "MODE0") ||
     (RTC_MODE1_INTERRUPT = false && RTC_MODULE_SELECTION = "MODE1") ||
     (RTC_MODE2_INTERRUPT = false && RTC_MODULE_SELECTION = "MODE2") >
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

  Precondition:
    RTC${RTC_INDEX}_Initialize must have been called for the associated
    RTC instance. The Enable Periodic Interval Notification Option in MHC should
    be set to the desired periodic interval.

  Parameters:
    None.

  Returns:
    true  - Periodic interval has completed.
    false - Periodic interval has not completed.

  Example:
    <code>
        // Wait till the configured periodic interval has expired.
        bool periodIntervalCompleted = false;
        RTC${RTC_INDEX}_Initialize();
        RTC${RTC_INDEX}_Timer32CounterSet(0);
        RTC${RTC_INDEX}_Timer32Start();
        do
        {
            periodIntervalCompleted = RTC${RTC_INDEX}_PeriodicIntervalHasCompleted();

        } while(!periodIntervalCompleted);

    </code>

  Remarks:
    The application can alternatively register a callback function by calling
    the RTC${RTC_INDEX}_PeriodicIntervalCallbackRegister() function to receive
    aysnchronous notification.
*/

bool RTC${RTC_INDEX}_PeriodicIntervalHasCompleted (void);
</#if>
</#if>
<#if RTC_MODULE_SELECTION = "MODE0">

<#if RTC_MODE0_INTERRUPT = false>
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

  Precondition:
    RTC${RTC_INDEX}_Initialize, RTC${RTC_INDEX}_Timer32Start and
    RTC${RTC_INDEX}_Timer32PeriodSet must have been called for the associated
    RTC instance. The RTC peripheral should have been configured in 32-bit Timer
    Counter mode.

  Parameters:
    None.

  Returns:
    true  - Period has expired.
    false - Period has not expired.

  Example:
    <code>
        bool periodExpired = false;
        RTC${RTC_INDEX}_Initialize();
        RTC${RTC_INDEX}_Timer32PeriodSet(0x3000);
        RTC${RTC_INDEX}_Timer32CounterSet(0);
        RTC${RTC_INDEX}_Timer32Start();
        do
        {
            periodExpired = RTC${RTC_INDEX}_Timer32PeriodHasExpired();
        }
    </code>

  Remarks:
    None.
*/

bool RTC${RTC_INDEX}_Timer32PeriodHasExpired ( void );

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

  Precondition:
    RTC${RTC_INDEX}_Initialize, RTC${RTC_INDEX}_Timer32Start must have been
    called for the associated RTC instance. The RTC peripheral should have been
    configured in 32-bit Timer Counter mode.

  Parameters:
    None.

  Returns:
    true - Counter has overflowed.
    false - Counter not overflowed.

  Example:
    <code>
        uint32_t cycles = 0;
        RTC${RTC_INDEX}_Initialize();

        // Clear the period set as we want to operate as a counter.
        RTC${RTC_INDEX}_Timer32PeriodSet(0);
        RTC${RTC_INDEX}_Timer32CounterSet(0);
        RTC${RTC_INDEX}_Timer32Start();

        // This is the task who execution duration needs to be measured.
        SomeTask();

        RTC${RTC_INDEX}_Timer32Stop();
        if(!RTC${RTC_INDEX}_Timer32CounterHasOverflowed())
        {
            // cycles will contains the execution time of SomeTask() in terms of
            // timer count.
            cycles = RTC${RTC_INDEX}_Timer32CounterGet();
        }
        else
        {
            // Timer overflowed. Handle this differently.
        }
    </code>

  Remarks:
    None.
*/

bool RTC${RTC_INDEX}_Timer32CounterHasOverflowed ( void );

</#if>
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

  Precondition:
    RTC${RTC_INDEX}_Initialize must have been called for the associated
    RTC instance. The RTC peripheral should have been configured in 32-bit Timer
    Counter mode. The RTC${RTC_INDEX}_Timer32PeriodSet and
    RTC${RTC_INDEX}_Timer32CounterSet function should have been called to set
    the desired period and starting count.

  Parameters:
    None.

  Returns:
    None.

  Example:
    <code>
        RTC${RTC_INDEX}_Initialize();

        // Operate as a timer by setting a non-zero period.
        RTC${RTC_INDEX}_Timer32PeriodSet(0x3000);
        RTC${RTC_INDEX}_Timer32CounterSet(0);
        RTC${RTC_INDEX}_Timer32Start();

        // Wait till the period has expired.
        while(RTC${RTC_INDEX}_Timer32PeriodHasExpired());

        // Refer to the description of the RTC${RTC_INDEX}_Timer32CounterHasOverflowed()
        // function for example of counter mode operation.

    </code>

  Remarks:
    None.
*/

void RTC${RTC_INDEX}_Timer32Start ( void );

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

  Precondition:
    RTC${RTC_INDEX}_Initialize must have been called for the associated
    RTC instance. The RTC peripheral should have been configured in 32-bit Timer
    Counter mode.

  Parameters:
    None.

  Returns:
    None.

  Example:
    <code>

    // Refer to the description of the RTC${RTC_INDEX}_Timer32CounterHasOverflowed()
    // function for example usage of the RTC${RTC_INDEX}_Timer32Stop() function.

    </code>

  Remarks:
    None.
*/

void RTC${RTC_INDEX}_Timer32Stop ( void );

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

  Precondition:
    RTC${RTC_INDEX}_Initialize, RTC${RTC_INDEX}_Timer32Start must have been
    called for the associated RTC instance. The RTC peripheral should have been
    configured in 32-bit Timer Counter mode.

  Parameters:
    count - 32-bit value to be loaded in the counter.

  Returns:
    None.

  Example:
    <code>
        // Refer to the description of the RTC${RTC_INDEX}_Timer32CounterHasOverflowed()
        // function for example usage of the RTC${RTC_INDEX}_Timer32CounterSet()
        // function.
    </code>

  Remarks:
    None.
*/

void RTC${RTC_INDEX}_Timer32CounterSet ( uint32_t count );

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

  Precondition:
    RTC${RTC_INDEX}_Initialize must have been called for the
    associated RTC instance. The RTC peripheral should have been configured in
    32-bit Timer Counter mode.

  Parameters:
    period - timer period value.

  Returns:
    None.

  Example:
    <code>
        uint32_t period = 0x00000FFF;
        RTC${RTC_INDEX}_Initialize();
        RTC${RTC_INDEX}_Timer32PeriodSet(period);
        RTC${RTC_INDEX}_Timer32CounterSet(0);
        RTC${RTC_INDEX}_Timer32Start();
        while(!RTC${RTC_INDEX}_Timer32PeriodHasExpired());
    </code>

  Remarks:
    The RTC${RTC_INDEX}_Timer32Start() should typically be called after the
    period has been set.
*/

void RTC${RTC_INDEX}_Timer32PeriodSet ( uint32_t period );

// *****************************************************************************
/* Function:
    uint32_t RTC${RTC_INDEX}_Timer32PeriodGet ( void )

  Summary:
    Get 32-bit timer period Value.

  Description:
    This function returns the 32-bit timer period value which used to compare
    with the current counter value. This value will match the value that was set
    using the RTC${RTC_INDEX}_Timer32PeriodSet() function.

  Precondition:
    RTC${RTC_INDEX}_Initialize must have been called for the associated
    RTC instance. The RTC peripheral should have been configured in 32-bit Timer
    Counter mode.

  Parameters:
    None.

  Returns:
    The current 32-bit timer period value.

  Example:
    <code>
        uitnt32_t period = 0;
        RTC${RTC_INDEX}_Initialize();
        RTC${RTC_INDEX}_Timer32PeriodSet(0xFFF);

        // period will have the same value is 0xFFF.
        period = RTC${RTC_INDEX}_Timer32PeriodGet();

    </code>

  Remarks:
    None.
*/

uint32_t RTC${RTC_INDEX}_Timer32PeriodGet ( void );

// *****************************************************************************
/* Function:
    uint32_t RTC${RTC_INDEX}_Timer32CounterGet ( void )

  Summary:
    Get the current 32-bit counter value.

  Description:
    This function returns the current 32-bit count value. This function can be
    used to retrieve the counter value at the end of a time measurement.

  Precondition:
    RTC${RTC_INDEX}_Initialize must have been called for the associated
    RTC instance. The RTC peripheral should have been configured in 32-bit Timer
    Counter mode.

  Parameters:
    None.

  Returns:
    uint32_t returns the current 32 bit counter value.

  Example:
    <code>
        // The following code example stops the counter when the counter value
        // has reached 0xFFF.

        RTC${RTC_INDEX}_Initialize();
        RTC${RTC_INDEX}_Timer32PeriodSet(0);
        RTC${RTC_INDEX}_Timer32CounterSet(0);
        RTC${RTC_INDEX}_Timer32Start();
        while(RTC${RTC_INDEX}_Timer32CounterGet() < 0xFFF);

        // Stop the counter.
        RTC${RTC_INDEX}_Timer32Stop();
    </code>

  Remarks:
    None.
*/

uint32_t RTC${RTC_INDEX}_Timer32CounterGet ( void );

// *****************************************************************************
/* Function:
    uint32_t RTC${RTC_INDEX}_Timer32FrequencyGet ( void )

  Summary:
    Returns the frequency at which the 32-bit timer counter is operating.

  Description:
    This function returns the frequency at which the 32-bit timer counter is
    operating. The return value can be used to compute the period that needs to
    be set in order to operate the timer counter at a desired frequency.

  Precondition:
    None.

  Parameters:
    None.

  Returns:
    Returns the frequency at which the 32-bit timer counter is operating.

  Example:
    <code>
        // Compute the period required to operate the timer at 1KHz.

        uint32_t desiredFrequency = 1000;
        uint32_t period = RTC${RTC_INDEX}_Timer32FrequencyGet()/desiredFrequency;
        RTC${RTC_INDEX}_Initialize();
        RTC${RTC_INDEX}_Timer32PeriodSet(period);

    </code>

  Remarks:
    None.
*/

uint32_t RTC${RTC_INDEX}_Timer32FrequencyGet ( void );

<#elseif RTC_MODULE_SELECTION = "MODE1">

<#if RTC_MODE1_INTERRUPT = false>
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

  Precondition:
    RTC${RTC_INDEX}_Initialize, RTC${RTC_INDEX}_Timer16Start and
    RTC${RTC_INDEX}_Timer16PeriodSet must have been called for the associated
    RTC instance. The RTC peripheral should have been configured in 16-bit Timer
    Counter mode.

  Parameters:
    None.

  Returns:
    true  - Period has expired.
    false - Period has not expired.

  Example:
    <code>
        bool periodExpired = false;
        RTC${RTC_INDEX}_Initialize();
        RTC${RTC_INDEX}_Timer16PeriodSet(0x3000);
        RTC${RTC_INDEX}_Timer16CounterSet(0);
        RTC${RTC_INDEX}_Timer16Start();
        do
        {
            periodExpired = RTC${RTC_INDEX}_Timer16PeriodHasExpired();
        }
    </code>

  Remarks:
    None.
*/

bool RTC${RTC_INDEX}_Timer16PeriodHasExpired ( void );

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

  Precondition:
    RTC${RTC_INDEX}_Initialize, RTC${RTC_INDEX}_Timer16Start must have been
    called for the associated RTC instance. The RTC peripheral should have been
    onfigured in 16-bit Timer Counter mode.

  Parameters:
    None.

  Returns:
    true - Counter has overflowed.
    false - Counter not overflowed.

  Example:
    <code>
        uint32_t cycles = 0;
        RTC${RTC_INDEX}_Initialize();

        // Clear the period set as we want to operate as a counter.
        RTC${RTC_INDEX}_Timer16PeriodSet(0);
        RTC${RTC_INDEX}_Timer16CounterSet(0);
        RTC${RTC_INDEX}_Timer16Start();

        // This is the task who execution duration needs to be measured.
        SomeTask();

        RTC${RTC_INDEX}_Timer16Stop();
        if(!RTC${RTC_INDEX}_Timer16CounterHasOverflowed())
        {
            // cycles will contains the execution time of SomeTask() in terms of
            // timer count.
            cycles = RTC${RTC_INDEX}_Timer16CounterGet();
        }
        else
        {
            // Timer overflowed. Handle this differently.
        }
    </code>

  Remarks:
    None.
*/

bool RTC${RTC_INDEX}_Timer16CounterHasOverflowed ( void );
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

  Precondition:
    RTC${RTC_INDEX}_Initialize, RTC${RTC_INDEX}_Timer16Start must have been
    called for the associated RTC instance. The RTC value should have been
    configured for 16-bit Timer Counter Mode. The Generate Compare 0 API option
    in MHC should have been enabled.

  Parameters:
    None.

  Returns:
    true  - Counter has matched Compare 0 Value.
    false - Counter has not matched Compare 0 Value.

  Example:
    <code>
        RTC${RTC_INDEX}_Initialize();
        RTC${RTC_INDEX}_Timer16CounterSet(0);
        RTC${RTC_INDEX}_Timer16PeriodSet(0xFFF);

        // Calling the RTC${RTC_INDEX}_Timer16Compare0Set() function will
        // override the Compare 0 value that was set via MHC.
        RTC${RTC_INDEX}_Timer16Compare0Set(0x3F);
        RTC${RTC_INDEX}_Timer16Start();

        // Wait till the Compare 0 value has matched.
        while(!RTC${RTC_INDEX}_Timer16Compare0HasMatched());
    </code>

  Remarks:
    None.
*/

bool RTC${RTC_INDEX}_Timer16Compare0HasMatched(void);
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

  Precondition:
    RTC${RTC_INDEX}_Initialize, RTC${RTC_INDEX}_Timer16Start must have been
    called for the associated RTC instance. The RTC value should have been
    configured for 16-bit Timer Counter Mode. The Generate Compare 1 API option
    in MHC should have been enabled.

  Parameters:
    None.

  Returns:
    true  - Counter has matched Compare 1 Value.
    false - Counter has not matched Compare 1 Value.

  Example:
    <code>
        RTC${RTC_INDEX}_Initialize();
        RTC${RTC_INDEX}_Timer16CounterSet(0);
        RTC${RTC_INDEX}_Timer16PeriodSet(0xFFF);

        // Calling the RTC${RTC_INDEX}_Timer16Compare1Set() function will
        //  override the Compare 1 value that was set via MHC.
        RTC${RTC_INDEX}_Timer16Compare1Set(0x3F);
        RTC${RTC_INDEX}_Timer16Start();

        // Wait till the Compare 1 value has matched.
        while(!RTC${RTC_INDEX}_Timer16Compare1HasMatched());
    </code>

  Remarks:
    None.
*/

bool RTC${RTC_INDEX}_Timer16Compare1HasMatched(void);
</#if>
</#if>
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

  Precondition:
    RTC${RTC_INDEX}_Initialize must have been called for the associated
    RTC instance. The RTC peripheral should have been configured in 16-bit Timer
    Counter mode. The RTC${RTC_INDEX}_Timer16PeriodSet and
    RTC${RTC_INDEX}_Timer16CounterSet function should have been called to set
    the desired period and starting count.

  Parameters:
    None.

  Returns:
    None.

  Example:
    <code>
        RTC${RTC_INDEX}_Initialize();

        // Operate as a timer by setting a non-zero period.
        RTC${RTC_INDEX}_Timer16PeriodSet(0x3000);
        RTC${RTC_INDEX}_Timer16CounterSet(0);
        RTC${RTC_INDEX}_Timer16Start();

        // Wait till the period has expired.
        while(RTC${RTC_INDEX}_Timer16PeriodHasExpired());

        // Refer to the description of the RTC${RTC_INDEX}_Timer16CounterHasOverflowed()
        // function for example of counter mode operation.

    </code>

  Remarks:
    None.
*/

void RTC${RTC_INDEX}_Timer16Start ( void );

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

  Precondition:
    RTC${RTC_INDEX}_Initialize must have been called for the associated
    RTC instance. The RTC peripheral should have been configured in 16-bit Timer
    Counter mode.

  Parameters:
    None.

  Returns:
    None.

  Example:
    <code>

    // Refer to the description of the RTC${RTC_INDEX}_Timer16CounterHasOverflowed()
    // function for example usage of the RTC${RTC_INDEX}_Timer16Stop() function.

    </code>

  Remarks:
    None.
*/

void RTC${RTC_INDEX}_Timer16Stop ( void );

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

  Precondition:
    RTC${RTC_INDEX}_Initialize, RTC${RTC_INDEX}_Timer16Start must have been
    called for the associated RTC instance. The RTC peripheral should have been
    configured in 16-bit Timer Counter mode.

  Parameters:
    count - 16-bit value to be loaded in the counter.

  Returns:
    None.

  Example:
    <code>
        // Refer to the description of the RTC${RTC_INDEX}_Timer16CounterHasOverflowed()
        // function for example usage of the RTC${RTC_INDEX}_Timer16CounterSet()
        //function.
    </code>

  Remarks:
    None.
*/

void RTC${RTC_INDEX}_Timer16CounterSet ( uint16_t count );

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

  Precondition:
    RTC${RTC_INDEX}_Initialize must have been called for the
    associated RTC instance. The RTC peripheral should have been configured in
    16-bit Timer Counter mode.

  Parameters:
    period - timer period value.

  Returns:
    None.

  Example:
    <code>
        uint16_t period = 0x0FFF;
        RTC${RTC_INDEX}_Initialize();
        RTC${RTC_INDEX}_Timer16PeriodSet(period);
        RTC${RTC_INDEX}_Timer16CounterSet(0);
        RTC${RTC_INDEX}_Timer16Start();
        while(!RTC${RTC_INDEX}_Timer16PeriodHasExpired());
    </code>

  Remarks:
    The RTC${RTC_INDEX}_Timer16Start() should typically be called after the
    period has been set.
*/

void RTC${RTC_INDEX}_Timer16PeriodSet ( uint16_t period );

// *****************************************************************************
/* Function:
    uint16_t RTC${RTC_INDEX}_Timer16PeriodGet ( void )

  Summary:
    Get 16-bit timer period Value.

  Description:
    This function returns the 16-bit timer period value which used to compare
    with the current counter value. This value will match the value that was set
    using the RTC${RTC_INDEX}_Timer16PeriodSet() function.

  Precondition:
    RTC${RTC_INDEX}_Initialize must have been called for the associated
    RTC instance. The RTC peripheral should have been configured in 16-bit Timer
    Counter mode

  Parameters:
    None.

  Returns:
    The current 16-bit timer period value.

  Example:
    <code>
        uint16_t period = 0;
        RTC${RTC_INDEX}_Initialize();
        RTC${RTC_INDEX}_Timer16PeriodSet(0xFFF);

        // period will have the same value is 0xFFF.
        period = RTC${RTC_INDEX}_Timer16PeriodGet();

    </code>

  Remarks:
    None.
*/

uint16_t RTC${RTC_INDEX}_Timer16PeriodGet ( void );

// *****************************************************************************
/* Function:
  uint16_t RTC${RTC_INDEX}_Timer16CounterGet ( void )

  Summary:
    Get the current 16-bit counter value.

  Description:
    This function returns the current 16-bit count value. This function can be
    used to retrieve the counter value at the end of a time measurement.

  Precondition:
    RTC${RTC_INDEX}_Initialize must have been called for the associated
    RTC instance. The RTC peripheral should have been configured in 16-bit Timer
    Counter mode.

  Parameters:
    None.

  Returns:
    uint16_t returns the current 16 bit counter value.

  Example:
    <code>
        // The following code example stops the counter when the counter value
        // has reached 0xFFF.

        RTC${RTC_INDEX}_Initialize();
        RTC${RTC_INDEX}_Timer16PeriodSet(0);
        RTC${RTC_INDEX}_Timer16CounterSet(0);
        RTC${RTC_INDEX}_Timer16Start();
        while(RTC${RTC_INDEX}_Timer16CounterGet() < 0xFFF);

        // Stop the counter.
        RTC${RTC_INDEX}_Timer16Stop();
    </code>

  Remarks:
    None.
*/

uint16_t RTC${RTC_INDEX}_Timer16CounterGet ( void );

// *****************************************************************************
/* Function:
    uint32_t RTC${RTC_INDEX}_Timer16FrequencyGet ( void )

  Summary:
    Returns the frequency at which the 16-bit timer counter is operating.

  Description:
    This function returns the frequency at which the 16-bit timer counter is
    operating. The return value can be used to compute the period that needs to
    be set in order to operate the timer counter at a desired frequency.

  Precondition:
    None.

  Parameters:
    None.

  Returns:
    Returns the frequency at which the 16-bit timer counter is operating.

  Example:
    <code>
        // Compute the period required to operate the timer at 1KHz.

        uint16_t desiredFrequency = 1000;
        uint16_t period = RTC${RTC_INDEX}_Timer16FrequencyGet()/desiredFrequency;
        RTC${RTC_INDEX}_Initialize();
        RTC${RTC_INDEX}_Timer16PeriodSet(period);

    </code>

  Remarks:
    None.
*/

uint32_t RTC${RTC_INDEX}_Timer16FrequencyGet ( void );

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

  Precondition:
    RTC${RTC_INDEX}_Initialize must have been called for the associated
    RTC instance. The Interrupt option in MHC should have been enabled.
    The RTC peripheral should have been configured for 16-bit timer counter
    operation. A valid event handling callback function should have been
    registered by calling the RTC${RTC_INDEX}_Timer16CallbackRegister() function

  Parameters:
    true  - Enable the Compare 0 value match event generation. The
    RTC_TIMER16_EVENT_COMPARE0_MATCH will be generated when a match has
    occurred.

    false - Disable the Compare 0 value match event generation. The
    RTC_TIMER16_EVENT_COMPARE0_MATCH will not be generated when a match has
    occurred.

  Returns:
    None.

  Example:
    <code>

        void MyTimer16Callback(RTC_TIMER16_EVENT event, uintptr_t context)
        {
            if(event & RTC_TIMER16_EVENT_COMPARE0_MATCH)
            {
                // This event will generated only if the
                // RTC${RTC_INDEX}_Timer16Compare0EventEnable was called with
                // true argument.
            }
        }

        RTC${RTC_INDEX}_Initialize();
        RTC${RTC_INDEX}_Timer16CounterSet(0);
        RTC${RTC_INDEX}_Timer16PeriodSet(0xFFF);
        RTC${RTC_INDEX}_Timer16Compare0Set(0x3F);
        RTC${RTC_INDEX}_Timer16CallbackRegister(MyTimer16Callback, NULL);
        RTC${RTC_INDEX}_Timer16Start();

        // Disable the event generation.
        RTC${RTC_INDEX}_Timer16Compare0EventEnable(false);

     </code>

  Remarks:
    None.
*/

void RTC${RTC_INDEX}_Timer16Compare0EventEnable(bool enable);
</#if>
</#if>

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

  Precondition:
    RTC${RTC_INDEX}_Initialize must have been called for the associated
    RTC instance. The Interrupt option in MHC should have been enabled.
    The RTC peripheral should have been configured for 16-bit timer counter
    operation. A valid event handling callback function should have been
    registered by calling the RTC${RTC_INDEX}_Timer16CallbackRegister() function

  Parameters:
    true  - Enable the Compare 1 value match event generation. The
    RTC_TIMER16_EVENT_COMPARE1_MATCH will be generated when a match has
    occurred.

    false - Disable the Compare 1 value match event generation. The
    RTC_TIMER16_EVENT_COMPARE1_MATCH will not be generated when a match has
    occurred.

  Returns:
    None.

  Example:
    <code>

    void MyTimer16Callback(RTC_TIMER16_EVENT event, uintptr_t context)
    {
        if(event & RTC_TIMER16_EVENT_COMPARE1_MATCH)
        {
            // This event will generated only if the
            // RTC${RTC_INDEX}_Timer16Compare1EventEnable was called with true
            // argument.
        }
    }

    RTC${RTC_INDEX}_Initialize();
    RTC${RTC_INDEX}_Timer16CounterSet(0);
    RTC${RTC_INDEX}_Timer16PeriodSet(0xFFF);
    RTC${RTC_INDEX}_Timer16Compare1Set(0x3F);
    RTC${RTC_INDEX}_Timer16CallbackRegister(MyTimer16Callback, NULL);
    RTC${RTC_INDEX}_Timer16Start();

    // Disable the event generation.
    RTC${RTC_INDEX}_Timer16Compare1EventEnable(false);

     </code>

  Remarks:
    None.
*/

void RTC${RTC_INDEX}_Timer16Compare1EventEnable (bool enable);
</#if>
</#if>
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

  Precondition:
    RTC${RTC_INDEX}_Initialize, RTC${RTC_INDEX}_Timer16Start must have been
    called for the associated RTC instance. The module should have configured
    for 16-bit Timer Counter operation.

  Parameters:
    None.

  Returns:
    comparisionValue - 16-bit compare value compares with the current counter
    value.

  Example:
    <code>
        // Refer to the description of the RTC${RTC_INDEX}_Timer16Compare0HasMatched()
        // function for example usage of the RTC${RTC_INDEX}_Timer16Compare0Set()
        // function.
    </code>

  Remarks:
    None.
*/

void RTC${RTC_INDEX}_Timer16Compare0Set ( uint16_t comparisionValue );
</#if>
<#if RTC_MODE1_GENERATE_COMPARE1_API =true>

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

  Precondition:
    RTC${RTC_INDEX}_Initialize, RTC${RTC_INDEX}_Timer16Start must have been
    called for the associated RTC instance. The module should have configured
    for 16-bit Timer Counter operation.

  Parameters:
    None.

  Returns:
    comparisionValue - 16-bit compare value compares with the current counter
    value.

  Example:
    <code>
        // Refer to the description of the RTC${RTC_INDEX}_Timer16Compare1HasMatched()
        // function for example usage of the RTC${RTC_INDEX}_Timer16Compare1Set()
        // function.

    </code>

  Remarks:
    None.
*/

void RTC${RTC_INDEX}_Timer16Compare1Set ( uint16_t comparisionValue );
</#if>
<#else>

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

  Precondition:
    RTC${RTC_INDEX}_Initialize must have been called for the associated
    RTC instance. The RTC should have been configured for Real Time Clock
    Calendar operation.

  Parameters:
    initialTime - Initial time value from the user of type tm structure defined
    in the time.h header file

  Returns:
    None.

  Example:
    <code>
        struct tm initialTime;

        RTC${RTC_INDEX}_Initialize();

        // Set the time as 22:31:23 and date as 7 April 1980.
        // The Reference Year Configuration in MHC should be within
        // 64 years of 1980. Also note that tm structure needs the tm_year to
        // specified as years since 1900.

        initialTime.tm_sec = 23;
        initialTime.tm_min = 31;
        initialTime.tm_hour = 22;
        initialTime.tm_mday = 7;
        initialTime.tm_mon = 3;
        initialTime.tm_year = 80;

        RTC${RTC_INDEX}_RTCCTimeSet(&initialTime);
    </code>

  Remarks:
    None.
*/

void RTC${RTC_INDEX}_RTCCTimeSet (struct tm * initialTime );

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

  Precondition:
    RTC${RTC_INDEX}_Initialize must have been called for the associated
    RTC instance. The RTC should have been configured for Real Time Clock
    Calendar operation.

  Parameters:
    currentTime - pointer to a struct tm type pointer which will contain the
    current time when the function returns.

  Returns:
    None.

  Example:
    <code>
        struct tm initialTime;
        struct tm currentTime;

        RTC${RTC_INDEX}_Initialize();

        // Set the time as 22:31:23 and date as 7 April 1980.
        // The Reference Year Configuration in MHC should be within
        // 64 years of 1980. Also note that tm structure needs the tm_year to
        // specified as years since 1900.

        initialTime.tm_sec = 23;
        initialTime.tm_min = 31;
        initialTime.tm_hour = 22;
        initialTime.tm_mday = 7;
        initialTime.tm_mon = 3;
        initialTime.tm_year = 80;

        RTC${RTC_INDEX}_RTCCTimeSet(&initialTime);

        // Get the current time.
        RTC${RTC_INDEX}_RTCCTimeGet(&currentTime);

    </code>

  Remarks:
    None.
*/

void RTC${RTC_INDEX}_RTCCTimeGet ( struct tm * currentTime );
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

  Precondition:
    RTC${RTC_INDEX}_Initialize must have been called for the associated
    RTC instance. The RTC peripheral should have been configured for Real Time
    Clock Calendar mode. The RTC${RTC_INDEX}_RTCCTimeSet function should have
    been called to set the current time. Setting this mode will also enable
    interrupts.

  Parameters:
    alarmTime - Time structure defines the alarm time.

    mask - This enum value defines the date and time fields to be matched at the
    time of generating alarm. Refer to the description of the RTC_ALARM_MASK
    enumeration for more details.

  Returns:
    None.

  Example:
    <code>
        struct tm alarmTime, initialTime;

        RTC_ALARM_MASK mask = RTC_ALARM_MASK_HHMMSS;
        RTC${RTC_INDEX}_Initialize();

        // Set the time first to 22:31:23 on 7 April 1980.
        initialTime.tm_sec = 23;
        initialTime.tm_min = 31;
        initialTime.tm_hour = 22;
        initialTime.tm_mday = 7;
        initialTime.tm_mon = 3;
        initialTime.tm_year = 80;

        RTC${RTC_INDEX}_RTCCTimeSet(&initialTime);

        // Set the alarm time to 08:00:00.
        alarmTime.tm_sec = 00;
        alarmTime.tm_min = 00;
        alarmTime.tm_hour = 08;

        // The mask is specified to match all time field and ignore all date
        // fields.
        RTC${RTC_INDEX}_RTCCAlarmSet(&alarmTime, mask);
    </code>

  Remarks:
    None.
*/

void RTC${RTC_INDEX}_RTCCAlarmSet (struct tm * alarmTime, RTC_ALARM_MASK mask);
</#if>
</#if>
<#if (RTC_MODULE_SELECTION = "MODE0" && RTC_MODE0_INTERRUPT = true) ||
     (RTC_MODULE_SELECTION = "MODE1" && RTC_MODE1_INTERRUPT = true) ||
     (RTC_MODULE_SELECTION = "MODE2" && RTC_MODE2_INTERRUPT = true) >
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

  Precondition:
    The RTC${RTC_INDEX}_Initialize() function should have been called to
    initialize the RTC module. The periodic interval should have been configured
    in MHC. The library should have been configured for Interrupt operation mode
    in MHC.

  Parameters:
    callback - A pointer to a function with a calling signature defined by the
    RTC_PERIODIC_INTERVAL_CALLBACK data type. Passing a NULL value disables the
    callback.

    context - A value (usually a pointer) that passed into the callback
    function when the callback function is called.

  Returns:
    None.

  Example:
    <code>
        // Refer to the description of the RTC_PERIODIC_INTERVAL_CALLBACK
        // datatype for example usage of this function.
    </code>

  Remarks:
    To disable the callback function, pass a NULL for the callback parameter.
    See the RTC_PERIODIC_INTERVAL_CALLBACK type definition for additional
    information.
*/

void RTC${RTC_INDEX}_PeriodicIntervalCallbackRegister(RTC_PERIODIC_INTERVAL_CALLBACK callback, uintptr_t context);
</#if>
<#if RTC_MODULE_SELECTION = "MODE2">

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

  Precondition:
    The RTC${RTC_INDEX}_Initialize() function should have been called to
    initialize the RTC module. The module should have been conifgured for
    Real Time Clock Calendar operation in MHC. The library should have been
    configured for Interrupt mode operation.

  Parameters:
    callback - A pointer to a function with a calling signature defined by the
    RTC_CALLBACK data type. Passing a NULL value disables the callback.

    context  - A value (usually a pointer) that passed into the callback
    function when the callback function is called.

  Returns:
    None.

  Example:
    <code>
        // Refer to the description of the RTC_CALLBACK datatype for
        // example usage of this function.
    </code>

  Remarks:
    To disable the callback function, pass a NULL for the callback parameter.
    See the RTC_CALLBACK type definition for additional information.
*/

void RTC${RTC_INDEX}_RTCCCallbackRegister ( RTC_CALLBACK callback, uintptr_t context);
<#elseif RTC_MODULE_SELECTION = "MODE0">

// *****************************************************************************
/* Function:
    void RTC${RTC_INDEX}_Timer32CallbackRegister ( RTC_TIMER32_CALLBACK callback,
                                                           uintptr_t context )

  Summary:
    Register the callback function to be called when an 32-bit Timer Interrupt
    occurs.

  Description:
    This function registers the  callback function  that the library will call
    when an interrupt occurs. The library will return the event that has caused
    the interrupt and the application specified context in the callback
    function.

  Precondition:
    The RTC${RTC_INDEX}_Initialize() function should have been called to
    initialize the RTC module. The module should have been conifgured for
    32-bit Timer Counter operation in MHC. The library should have been
    configured for Interrupt mode operation.

  Parameters:
    callback - A pointer to a function with a calling signature defined by the
    RTC_TIMER32_CALLBACK data type. Passing a NULL value disables the callback.

    context  - A value (usually a pointer) that passed into the callback
    function when the callback function is called.

  Returns:
    None.

  Example:
    <code>
        // Refer to the description of the RTC_TIMER32_CALLBACK datatype for
        // example usage of this function.
    </code>

  Remarks:
    To disable the callback function, pass a NULL for the callback parameter.
    See the RTC_TIMER32_CALLBACK type definition for additional information.
*/

void RTC${RTC_INDEX}_Timer32CallbackRegister ( RTC_TIMER32_CALLBACK callback, uintptr_t context );
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

  Precondition:
    The RTC${RTC_INDEX}_Initialize() function should have been called to
    initialize the RTC module. The module should have been conifgured for 16-bit
    Timer Counter operation in MHC. The library should have been configured for
    Interrupt mode operation.

  Parameters:
    callback - A pointer to a function with a calling signature defined by the
    RTC_TIMER16_CALLBACK data type. Passing a NULL value disables the callback.

    context  - A value (usually a pointer) that passed into the callback
    function when the callback function is called.

  Returns:
    None.

  Example:
    <code>
        // Refer to the description of the RTC_TIMER16_CALLBACK data type for
        // example usage of this function.
    </code>

  Remarks:
    To disable the callback function, pass a NULL for the callback parameter.
    See the RTC_TIMER16_CALLBACK type definition for additional information.
*/

void RTC${RTC_INDEX}_Timer16CallbackRegister ( RTC_TIMER16_CALLBACK callback, uintptr_t context );
</#if>
</#if>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility
}
#endif
// DOM-IGNORE-END

#endif /* PLIB_RTC${RTC_INDEX}_H */