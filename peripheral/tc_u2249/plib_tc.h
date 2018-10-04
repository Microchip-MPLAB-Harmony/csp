/*******************************************************************************
  Timer/Counter(TC) Peripheral Library Interface Header File

  Company
    Microchip Technology Inc.

  File Name
    plib_tc.h

  Summary
    TC peripheral library interface.

  Description
    This file defines the interface to the TC peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

  Remarks:
    This header is for documentation only.  The actual tc<x> headers will be
    generated as required by the MHC (where <x> is the peripheral instance
    number).

    Every interface symbol has a lower-case 'x' in it following the "TC"
    abbreviation.  This 'x' will be replaced by the peripheral instance number
    in the generated headers.  These are the actual functions that should be
    used.

*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
* © 2018 Microchip Technology Inc. and its subsidiaries.
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

#ifndef PLIB_TCx_H    // Guards against multiple inclusion
#define PLIB_TCx_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
/*  This section lists the other files that are included in this file.
*/

#include <stdbool.h>
#include <stddef.h>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    extern "C" {

#endif
// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Section: Data Types
// *****************************************************************************
// *****************************************************************************
/*  The following data type definitions are used by the functions in this
    interface and should be considered part it.
*/

// *****************************************************************************
/* Interrupt source mask for capture mode

  Summary:
    Identifies channel interrupt source mask.

  Description:
    This enumeration identifies TC capture mode interrupt source mask.

  Remarks:
    None.
*/

typedef enum
{
    /* Capture status overflow */
    TC_CAPTURE_STATUS_OVERFLOW = 0x1,

    /* Capture status error */
    TC_CAPTURE_STATUS_ERROR = 0x2,

    /* Capture status ready for channel 0 */
    TC_CAPTURE_STAUTS_CAPTURE0_READY = 0x10,

    /* Capture status ready for channel 1 */
    TC_CAPTURE_STATUS_CAPTURE1_READY = 0x20,
    
    TC_CAPTURE_STATUS_MSK = TC_CAPTURE_STATUS_OVERFLOW | TC_CAPTURE_STATUS_ERROR | TC_CAPTURE_STAUTS_CAPTURE0_READY | TC_CAPTURE_STATUS_CAPTURE1_READY

} TC_CAPTURE_STATUS;



// *****************************************************************************
/* Callback Function Pointer

  Summary:
    Defines the function pointer data type and function signature for the tc
    callback function.

  Description:
    This data type defines the function pointer and function signature for the
    tc callback function. The library will call back the client's
    function with this signature from the interrupt routine.

  Function:
    void (*TC_CALLBACK)( uintptr_t context )

  Precondition:
    TCx_Initialize must have been called for the given TC channel
    instance and TCx_CallbackRegister must have been called to register the
    function to be called.

  Parameters:
    context  - Allows the caller to provide a context value (usually a pointer
    to the callers context for multi-instance clients).

  Returns:
    None.

  Example:
    <code>
    void TC_Callback_Fn ( uintptr_t context );

    TCx_TimerCallbackRegister(TC_Callback_Fn, NULL);
    </code>

  Remarks:
    Interrupt is different in each mode of TC peripheral.
    e.g. In timer mode and compare mode, period interrupt will be enabled and
    registered function will be called back.
    In Capture mode, registered function will be called from load event
    interrupt routine.
*/

typedef void (*TC_CALLBACK)( uintptr_t context );

// *****************************************************************************
typedef struct
{
    TC_CALLBACK callback;

    uintptr_t context;

} TC_CALLBACK_OBJ;

// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************
/* The following functions make up the methods (set of possible operations) of
   this interface.
*/

// *****************************************************************************
/* Function:
    void TCx_TimerInitialize( void );

  Summary:
    Initializes given instance of TC.

  Description:
    This function initializes given instance of TC with the values
    configured in MHC GUI.

  Precondition:
    MHC GUI should be configured with the right values.

  Parameters:
    None.

  Returns:
    None.

  Example:
    <code>
      TCx_TimerInitialize();
    </code>

  Remarks:
    This function must be called before any other TC function is
    called. This function should only be called once during system
    initialization.
*/

void TCx_TimerInitialize( void );

// *****************************************************************************
/* Function:
    void TCx_TimerStart( void );

  Summary:
    Starts the timer for given TC instance.

  Description:
    This function enables the clock and starts the timer.

  Precondition:
    TCx_TimerInitialize() function must have been called first.

  Parameters:
    None.

  Returns:
    None.

  Example:
    <code>
      TCx_TimerInitialize();
      TCx_TimerStart();
    </code>

  Remarks:
    None.
*/

void TCx_TimerStart( void );

// *****************************************************************************
/* Function:
    void TCx_TimerStop( void );

  Summary:
    Stops the timer for given TC instance.

  Description:
    This function stops the clock and thus timer.

  Precondition:
    TCx_TimerInitialize() function must have been called first.
    Also counter should have been started with TCx_TimerStart()
    function call.

  Parameters:
    None.

  Returns:
    None.

  Example:
    <code>
      TCx_TimerInitialize();
      TCx_TimerStart();
      TCx_TimerStop();
    </code>

  Remarks:
    None.
*/

void TCx_TimerStop( void );

// *****************************************************************************
/* Function:
    void TCx_Timer8bitPeriodSet( uint8_t period );

  Summary:
    Sets the period value of a given timer.

  Description:
    This function writes the period value. When timer counter matches period
    value,counter is reset and interrupt can be generated.

  Precondition:
    TCx_TimerInitialize() function must have been called first.

  Parameters:
    period - new period value to set for timer.

  Returns:
    None.

  Example:
    <code>
      uint8_t period = 0x500;
      TCx_TimerInitialize();
      TCx_Timer8bitPeriodSet(period);
    </code>

  Remarks:
    The caller must know the number of significant bytes of timer. Period
    value is right-aligned.
*/

void TCx_Timer8bitPeriodSet( uint8_t period );

// *****************************************************************************
/* Function:
    uint8_t TCx_Timer8bitPeriodGet( void );

  Summary:
    Reads the period value of given timer.

  Description:
    This function reads the value of period.

  Precondition:
    TCx_TimerInitialize() function must have been called first.

  Parameters:
    None.

  Returns:
    period - The timer's period value.

  Example:
    <code>
      uint8_t period = 0;
      TCx_TimerInitialize();
      period = TCx_Timer8bitPeriodGet();
    </code>

  Remarks:
    The caller must know the number of significant bytes of timer. Period
    value is right-aligned.
*/

uint8_t TCx_Timer8bitPeriodGet( void );

// *****************************************************************************
/* Function:
    uint8_t TCx_Timer8bitCounterGet( void );

  Summary:
    Reads the timer current count value.

  Description:
    This function reads the timer count value.

  Precondition:
    TCx_TimerInitialize() function must have been called first.

  Parameters:
    None.

  Returns:
    counter - The timer's current count value.

  Example:
    <code>
      uint8_t counter = 0;
      TCx_TimerInitialize();
      TCx_TimerStart();
      counter = TCx_Timer8bitCounterGet();
    </code>

  Remarks:
    The caller must know the number of significant bytes of timer. Period
    value is right-aligned.
*/

uint8_t TCx_Timer8bitCounterGet( void );

// *****************************************************************************
/* Function:
    void TCx_Timer8bitCounterSet( uint8_t count );

  Summary:
    Sets new timer counter value.

  Description:
    This function sets new timer counter value.

  Precondition:
    TCx_TimerInitialize() function must have been called first.

  Parameters:
    count - new counter value to set.

  Returns:
    None.

  Example:
    <code>
      uint8_t count = 0x10;
      TCx_TimerInitialize();
      TCx_TimerStart();
      TCx_Timer8bitCounterSet(count);
    </code>

  Remarks:
    The caller must know the number of significant bytes of timer. Counter
    value is right-aligned.
*/

void TCx_Timer8bitCounterSet( uint8_t count );

// *****************************************************************************
/* Function:
    void TCx_Timer16bitPeriodSet( uint16_t period );

  Summary:
    Sets the period value of a given timer.

  Description:
    This function writes the period value. When timer counter matches period
    value,counter is reset and interrupt can be generated.

  Precondition:
    TCx_TimerInitialize() function must have been called first.

  Parameters:
    period - new period value to set for timer.

  Returns:
    None.

  Example:
    <code>
      uint16_t period = 0x500;
      TCx_TimerInitialize();
      TCx_Timer16bitPeriodSet(period);
    </code>

  Remarks:
    The caller must know the number of significant bytes of timer. Period
    value is right-aligned.
*/

void TCx_Timer16bitPeriodSet( uint16_t period );

// *****************************************************************************
/* Function:
    uint16_t TCx_Timer16bitPeriodGet( void );

  Summary:
    Reads the period value of given timer.

  Description:
    This function reads the value of period.

  Precondition:
    TCx_TimerInitialize() function must have been called first.

  Parameters:
    None.

  Returns:
    period - The timer's period value.

  Example:
    <code>
      uint16_t period = 0;
      TCx_TimerInitialize();
      period = TCx_Timer16bitPeriodGet();
    </code>

  Remarks:
    The caller must know the number of significant bytes of timer. Period
    value is right-aligned.
*/

uint16_t TCx_Timer16bitPeriodGet( void );

// *****************************************************************************
/* Function:
    uint16_t TCx_Timer16bitCounterGet( void );

  Summary:
    Reads the timer current count value.

  Description:
    This function reads the timer count value.

  Precondition:
    TCx_TimerInitialize() function must have been called first.

  Parameters:
    None.

  Returns:
    counter - The timer's current count value.

  Example:
    <code>
      uint16_t counter = 0;
      TCx_TimerInitialize();
      TCx_TimerStart();
      counter = TCx_Timer16bitCounterGet();
    </code>

  Remarks:
    The caller must know the number of significant bytes of timer. Period
    value is right-aligned.
*/

uint16_t TCx_Timer16bitCounterGet( void );

// *****************************************************************************
/* Function:
    void TCx_Timer16bitCounterSet( uint16_t count );

  Summary:
    Sets new timer counter value.

  Description:
    This function sets new timer counter value.

  Precondition:
    TCx_TimerInitialize() function must have been called first.

  Parameters:
    count - new counter value to set.

  Returns:
    None.

  Example:
    <code>
      uint16_t count = 0x100;
      TCx_TimerInitialize();
      TCx_TimerStart();
      TCx_Timer16bitCounterSet(count);
    </code>

  Remarks:
    The caller must know the number of significant bytes of timer. Counter
    value is right-aligned.
*/

void TCx_Timer16bitCounterSet( uint16_t count );

// *****************************************************************************
/* Function:
    void TCx_Timer32bitPeriodSet( uint32_t period );

  Summary:
    Sets the period value of a given timer.

  Description:
    This function writes the period value. When timer counter matches period
    value,counter is reset and interrupt can be generated.

  Precondition:
    TCx_TimerInitialize() function must have been called first.

  Parameters:
    period - new period value to set for timer.

  Returns:
    None.

  Example:
    <code>
      uint32_t period = 0x500;
      TCx_TimerInitialize();
      TCx_Timer32bitPeriodSet(period);
    </code>

  Remarks:
    The caller must know the number of significant bytes of timer. Period
    value is right-aligned.
*/

void TCx_Timer32bitPeriodSet( uint32_t period );

// *****************************************************************************
/* Function:
    uint32_t TCx_Timer32bitPeriodGet( void );

  Summary:
    Reads the period value of given timer.

  Description:
    This function reads the value of period.

  Precondition:
    TCx_TimerInitialize() function must have been called first.

  Parameters:
    None.

  Returns:
    period - The timer's period value.

  Example:
    <code>
      uint32_t period = 0;
      TCx_TimerInitialize();
      period = TCx_Timer32bitPeriodGet();
    </code>

  Remarks:
    The caller must know the number of significant bytes of timer. Period
    value is right-aligned.
*/

uint32_t TCx_Timer32bitPeriodGet( void );

// *****************************************************************************
/* Function:
    uint32_t TCx_Timer32bitCounterGet( void );

  Summary:
    Reads the timer current count value.

  Description:
    This function reads the timer count value.

  Precondition:
    TCx_TimerInitialize() function must have been called first.

  Parameters:
    None.

  Returns:
    counter - The timer's current count value.

  Example:
    <code>
      uint32_t counter = 0;
      TCx_TimerInitialize();
      TCx_TimerStart();
      counter = TCx_Timer32bitCounterGet();
    </code>

  Remarks:
    The caller must know the number of significant bytes of timer. Period
    value is right-aligned.
*/

uint32_t TCx_Timer32bitCounterGet( void );

// *****************************************************************************
/* Function:
    void TCx_Timer32bitCounterSet( uint32_t count );

  Summary:
    Sets new timer counter value.

  Description:
    This function sets new timer counter value.

  Precondition:
    TCx_TimerInitialize() function must have been called first.

  Parameters:
    count - new counter value to set.

  Returns:
    None.

  Example:
    <code>
      uint32_t count = 0x100;
      TCx_TimerInitialize();
      TCx_TimerStart();
      TCx_Timer32bitCounterSet(count);
    </code>

  Remarks:
    The caller must know the number of significant bytes of timer. Counter
    value is right-aligned.
*/

void TCx_Timer32bitCounterSet( uint32_t count );

// *****************************************************************************
/* Function:
    bool TCx_TimerPeriodHasExpired( void );

  Summary:
    Checks whether timer period is elapsed.

  Description:
    This function checks the status of the timer period interrupt.

  Precondition:
    TCx_TimerInitialize() function must have been called first.

  Parameters:
    None.

  Returns:
    timerPeriodStatus - timer period elapsed status.

  Example:
    <code>
      bool timerPeriodStatus = false;
      TCx_TimerInitialize();
      timerPeriodStatus = TCx_TimerPeriodHasExpired();
    </code>

  Remarks:
    None.
*/

bool TCx_TimerPeriodHasExpired( void );

// *****************************************************************************
/* Function:
    uint32_t TCx_TimerFrequencyGet( void );

  Summary:
    Provides the given timer's counter-increment frequency.

  Description:
    This function provides the frequency at which the given counter
    increments. It can be used to convert differences between counter values
    to real time or real-time intervals to timer period values.

  Precondition:
    TCx_TimerInitialize() function must have been called first.

  Parameters:
    None.

  Returns:
    frequency - The frequency (in Hz) at which the timer's counter increments.

  Example:
    <code>
      uint32_t frequency = 0;
      TCx_TimerInitialize();
      frequency = TCx_TimerFrequencyGet();
    </code>

  Remarks:
    None.
*/

uint32_t TCx_TimerFrequencyGet( void );

// *****************************************************************************
/* Function:
    void TCx_TimerCallbackRegister( TC_CALLBACK callback, uintptr_t context );

  Summary:
    Registers the function to be called from interrupt.

  Description
    This function registers the callback function to be called from interrupt.

  Precondition:
    TCx_TimerInitialize() must have been called first.

  Parameters:
    callback - callback function pointer
    context  - Allows the caller to provide a context value (usually a pointer
               to the callers context for multi-instance clients).

  Returns:
    None.

  Example:
    <code>
      void TC_Callback_Fn( uintptr_t context );

      TCx_TimerInitialize();
      TCx_TimerCallbackRegister(TC_Callback_Fn, NULL);
    </code>

  Remarks:
    Context value can be set to NULL if not required.
    To disable callback function, pass NULL for the callback parameter.
*/

void TCx_TimerCallbackRegister( TC_CALLBACK callback, uintptr_t context );

// *****************************************************************************
/* Function:
    void TCx_CaptureInitialize( void );

  Summary:
    Initializes given instance of TC.

  Description:
    This function initializes given instance of TC with the values
    configured in MHC GUI.

  Precondition:
    MHC GUI should be configured with the right values.

  Parameters:
    None.

  Returns:
    None.

  Example:
    <code>
      TCx_CaptureInitialize();
    </code>

  Remarks:
    This function must be called before any other TC function is
    called. This function should only be called once during system
    initialization.
*/

void TCx_CaptureInitialize ( void );

// *****************************************************************************
/* Function:
    void TCx_CaptureStart ( void );

  Summary:
    Starts the timer for given TC instance.

  Description:
    This function enables the clock and starts the timer.

  Precondition:
    TCx_CaptureInitialize() function must have been called first.

  Parameters:
    None.

  Returns:
    None.

  Example:
    <code>
      TCx_CaptureInitialize();
      TCx_CaptureStart();
    </code>

  Remarks:
    None.
*/

void TCx_CaptureStart ( void );

// *****************************************************************************
/* Function:
    void TCx_CaptureStop ( void );

  Summary:
    Stops the timer for given TC instance.

  Description:
    This function stops the clock and thus timer.

  Precondition:
    TCx_CaptureInitialize() function must have been called first.

  Parameters:
    None.

  Returns:
    None.

  Example:
    <code>
      TCx_CaptureInitialize();
      TCx_CaptureStart();
      TCx_CaptureStop();
    </code>

  Remarks:
    None.
*/

void TCx_CaptureStop ( void );

// *****************************************************************************
/* Function:
    uint8_t TCx_Capture8bitChannel0Get( void );

  Summary:
    Reads capture value from channel 0.

  Description:
    This function reads the captured value stored in CC[0].
    Value can be read from interrupt routine or by polling.

  Precondition:
    TCx_CaptureInitialize() function must have been called first.

  Parameters:
    None.

  Returns:
    captureValue - Captured value from channel 0.

  Example:
    <code>
      uint8_t captureValue = 0;
      TCx_CaptureInitialize();
      TCx_CaptureStart();
      captureValue = TCx_Capture8bitChannel0Get();
    </code>

  Remarks:
    None.
*/

uint8_t TCx_Capture8bitChannel0Get( void );

// *****************************************************************************
/* Function:
    uint16_t TCx_Capture16bitChannel0Get( void );

  Summary:
    Reads capture value from channel 0.

  Description:
    This function reads the captured value stored in CC[0].
    Value can be read from interrupt routine or by polling.

  Precondition:
    TCx_CaptureInitialize() function must have been called first.

  Parameters:
    None.

  Returns:
    captureValue - Captured value from channel 0.

  Example:
    <code>
      uint16_t captureValue = 0;
      TCx_CaptureInitialize();
      TCx_CaptureStart();
      captureValue = TCx_Capture16bitChannel0Get();
    </code>

  Remarks:
    None.
*/

uint16_t TCx_Capture16bitChannel0Get( void );

// *****************************************************************************
/* Function:
    uint32_t TCx_Capture32bitChannel0Get( void );

  Summary:
    Reads capture value from channel 0.

  Description:
    This function reads the captured value stored in CC[0].
    Value can be read from interrupt routine or by polling.

  Precondition:
    TCx_CaptureInitialize() function must have been called first.

  Parameters:
    None.

  Returns:
    captureValue - Captured value from channel 0.

  Example:
    <code>
      uint32_t captureValue = 0;
      TCx_CaptureInitialize();
      TCx_CaptureStart();
      captureValue = TCx_Capture32bitChannel0Get();
    </code>

  Remarks:
    None.
*/

uint32_t TCx_Capture32bitChannel0Get( void );

// *****************************************************************************
/* Function:
    bool TCx_CaptureChannel0StatusGet( void );

  Summary:
    Reads capture status of channel 0.

  Description:
    This function reads the capture status of channel 0.

  Precondition:
    TCx_CaptureInitialize() function must have been called first.

  Parameters:
    None.

  Returns:
    captureStatus - Capture status of channel 0.

  Example:
    <code>
      bool captureStatus = false;
      TCx_CaptureInitialize();
      TCx_CaptureStart();
      captureStatus = TCx_CaptureChannel0StatusGet();
    </code>

  Remarks:
    None.
*/

bool TCx_CaptureChannel0StatusGet( void );

// *****************************************************************************
/* Function:
    uint8_t TCx_Capture8bitChannel1Get( void );

  Summary:
    Reads capture value from channel 1.

  Description:
    This function reads the captured value stored in CC[1].
    Value can be read from interrupt routine or by polling.

  Precondition:
    TCx_CaptureInitialize() function must have been called first.

  Parameters:
    None.

  Returns:
    captureValue - Captured value from channel 1.

  Example:
    <code>
      uint8_t captureValue = 0;
      TCx_CaptureInitialize();
      TCx_CaptureStart();
      captureValue = TCx_Capture8bitChannel1Get();
    </code>

  Remarks:
    None.
*/

uint8_t TCx_Capture8bitChannel1Get( void );

// *****************************************************************************
/* Function:
    uint16_t TCx_Capture16bitChannel1Get( void );

  Summary:
    Reads capture value from channel 1.

  Description:
    This function reads the captured value stored in CC[1].
    Value can be read from interrupt routine or by polling.

  Precondition:
    TCx_CaptureInitialize() function must have been called first.

  Parameters:
    None.

  Returns:
    captureValue - Captured value from channel 1.

  Example:
    <code>
      uint16_t captureValue = 0;
      TCx_CaptureInitialize();
      TCx_CaptureStart();
      captureValue = TCx_Capture16bitChannel1Get();
    </code>

  Remarks:
    None.
*/

uint16_t TCx_Capture16bitChannel1Get( void );

// *****************************************************************************
/* Function:
    uint32_t TCx_Capture32bitChannel1Get( void );

  Summary:
    Reads capture value from channel 1.

  Description:
    This function reads the captured value stored in CC[1].
    Value can be read from interrupt routine or by polling.

  Precondition:
    TCx_CaptureInitialize() function must have been called first.

  Parameters:
    None.

  Returns:
    captureValue - Captured value from channel 1.

  Example:
    <code>
      uint32_t captureValue = 0;
      TCx_CaptureInitialize();
      TCx_CaptureStart();
      captureValue = TCx_Capture32bitChannel1Get();
    </code>

  Remarks:
    None.
*/

uint32_t TCx_Capture32bitChannel1Get( void );

// *****************************************************************************
/* Function:
    TC_CAPTURE_STATUS TCx_CaptureStatusGet( void );

  Summary:
    Reads status capture operation.

  Description:
    This function reads the capture status.

  Precondition:
    TCx_CaptureInitialize() function must have been called first.

  Parameters:
    None.

  Returns:
    captureStatus - status of capture operation.

  Example:
    <code>
      TC_CAPTURE_STATUS captureStatus = TC_CAPTURE_STATUS_OVERFLOW;
      TCx_CaptureInitialize();
      TCx_CaptureStart();
      captureStatus = TCx_CaptureStatusGet();
    </code>

  Remarks:
    None.
*/

TC_CAPTURE_STATUS TCx_CaptureStatusGet( void );

// *****************************************************************************
/* Function:
    void TCx_CaptureCallbackRegister( TC_CALLBACK callback,
                                  TC_CAPTURE_STATUS status, uintptr_t context );

  Summary:
    Registers the function to be called from interrupt.

  Description
    This function registers the callback function to be called from interrupt.

  Precondition:
    TCx_CaptureInitialize() must have been called first.

  Parameters:
    callback - callback function pointer
    status   - capture status
    context  - Allows the caller to provide a context value (usually a pointer
               to the callers context for multi-instance clients).

  Returns:
    None.

  Example:
    <code>
      void TC_Callback_Fn( uintptr_t context );

      TC_CAPTURE_STATUS captureStatus = TC_CAPTURE_STATUS_OVERFLOW;
      TCx_CaptureInitialize();
      TCx_CaptureCallbackRegister(TC_Callback_Fn, captureStatus, NULL);
    </code>

  Remarks:
    Context value can be set to NULL if not required.
    To disable callback function, pass NULL for the callback parameter.
*/

void TCx_CaptureCallbackRegister( TC_CALLBACK callback, TC_CAPTURE_STATUS status, uintptr_t context );

// *****************************************************************************
/* Function:
    void TCx_CompareInitialize( void );

  Summary:
    Initializes given instance of TC.

  Description:
    This function initializes given instance of TC with the values
    configured in MHC GUI.

  Precondition:
    MHC GUI should be configured with the right values.

  Parameters:
    None.

  Returns:
    None.

  Example:
    <code>
      TCx_CompareInitialize();
    </code>

  Remarks:
    This function must be called before any other TC function is
    called. This function should only be called once during system
    initialization.
*/

void TCx_CompareInitialize( void );

// *****************************************************************************
/* Function:
    void TCx_CompareStart( void );

  Summary:
    Starts the timer for given TC instance.

  Description:
    This function enables the clock and starts the timer.

  Precondition:
    TCx_CompareInitialize() function must have been called first.

  Parameters:
    None.

  Returns:
    None.

  Example:
    <code>
      TCx_CompareInitialize();
      TCx_CompareStart();
    </code>

  Remarks:
    None.
*/

void TCx_CompareStart( void );

// *****************************************************************************
/* Function:
    void TCx_CompareStop( void );

  Summary:
    Stops the timer for given TC instance.

  Description:
    This function stops the clock and thus timer.

  Precondition:
    TCx_CompareInitialize() function must have been called first.
    Also counter should have been started with TCx_CompareStart()
    function call.

  Parameters:
    None.

  Returns:
    None.

  Example:
    <code>
      TCx_CompareInitialize();
      TCx_CompareStart();
      TCx_CompareStop();
    </code>

  Remarks:
    None.
*/

void TCx_CompareStop( void );

// *****************************************************************************
/* Function:
    void TCx_Compare8bitPeriodSet( uint8_t period );

  Summary:
    Sets the period value of a given timer.

  Description:
    This function writes the period value. When timer counter matches period
    value,counter is reset and interrupt can be generated.

  Precondition:
    TCx_CompareInitialize() function must have been called first.

  Parameters:
    period - new period value to set for timer.

  Returns:
    None.

  Example:
    <code>
      uint8_t period = 0x500;
      TCx_CompareInitialize();
      TCx_Compare8bitPeriodSet(period);
    </code>

  Remarks:
    The caller must know the number of significant bytes of timer. Period
    value is right-aligned.
*/

void TCx_Compare8bitPeriodSet( uint8_t period );

// *****************************************************************************
/* Function:
    uint8_t TCx_Compare8bitPeriodGet( void );

  Summary:
    Reads the period value of given timer.

  Description:
    This function reads the value of period.

  Precondition:
    TCx_CompareInitialize() function must have been called first.

  Parameters:
    None.

  Returns:
    period - The timer's period value.

  Example:
    <code>
      uint8_t period = 0;
      TCx_CompareInitialize();
      period = TCx_Compare8bitPeriodGet();
    </code>

  Remarks:
    The caller must know the number of significant bytes of timer. Period
    value is right-aligned.
*/

uint8_t TCx_Compare8bitPeriodGet( void );

// *****************************************************************************
/* Function:
    uint8_t TCx_Compare8bitCounterGet( void );

  Summary:
    Reads the timer current count value.

  Description:
    This function reads the timer count value.

  Precondition:
    TCx_CompareInitialize() function must have been called first.

  Parameters:
    None.

  Returns:
    counter - The timer's current count value.

  Example:
    <code>
      uint8_t counter = 0;
      TCx_CompareInitialize();
      TCx_CompareStart();
      counter = TCx_Compare8bitCounterGet();
    </code>

  Remarks:
    The caller must know the number of significant bytes of timer. Period
    value is right-aligned.
*/

uint8_t TCx_Compare8bitCounterGet( void );

// *****************************************************************************
/* Function:
    void TCx_Compare8bitCounterSet( uint8_t count );

  Summary:
    Sets new timer counter value.

  Description:
    This function sets new timer counter value.

  Precondition:
    TCx_CompareInitialize() function must have been called first.

  Parameters:
    count - new counter value to set.

  Returns:
    None.

  Example:
    <code>
      uint8_t count = 0x10;
      TCx_CompareInitialize();
      TCx_CompareStart();
      TCx_Compare8bitCounterSet(count);
    </code>

  Remarks:
    The caller must know the number of significant bytes of timer. Counter
    value is right-aligned.
*/

void TCx_Compare8bitCounterSet( uint8_t count );

// *****************************************************************************
/* Function:
    void TCx_Compare8bitSet( uint8_t compareValue );

  Summary:
    Writes compare value of the given compare channel 1.

  Description:
    Set CC[1] compare value.

  Precondition:
    TCx_CompareInitialize() function must have been called first.

  Parameters:
    compareValue - value to set for compare channel 1.

  Returns:
    None.

  Example:
    <code>
      uint8_t compareValue = 0x100;
      TCx_CompareInitialize();
      TCx_Compare8bitSet(compareValue);
    </code>

  Remarks:
    None
*/

void TCx_Compare8bitSet( uint8_t compareValue );

// *****************************************************************************
/* Function:
    void TCx_Compare16bitPeriodSet( uint16_t period );

  Summary:
    Sets the period value of a given timer.

  Description:
    This function writes the period value. When timer counter matches period
    value,counter is reset and interrupt can be generated.

  Precondition:
    TCx_CompareInitialize() function must have been called first.

  Parameters:
    period - new period value to set for timer.

  Returns:
    None.

  Example:
    <code>
      uint16_t period = 0x500;
      TCx_CompareInitialize();
      TCx_Compare16bitPeriodSet(period);
    </code>

  Remarks:
    The caller must know the number of significant bytes of timer. Period
    value is right-aligned.
*/

void TCx_Compare16bitPeriodSet( uint16_t period );

// *****************************************************************************
/* Function:
    uint16_t TCx_Compare16bitPeriodGet( void );

  Summary:
    Reads the period value of given timer.

  Description:
    This function reads the value of period.

  Precondition:
    TCx_CompareInitialize() function must have been called first.

  Parameters:
    None.

  Returns:
    period - The timer's period value.

  Example:
    <code>
      uint16_t period = 0;
      TCx_CompareInitialize();
      period = TCx_Compare16bitPeriodGet();
    </code>

  Remarks:
    The caller must know the number of significant bytes of timer. Period
    value is right-aligned.
*/

uint16_t TCx_Compare16bitPeriodGet( void );

// *****************************************************************************
/* Function:
    uint16_t TCx_Compare16bitCounterGet( void );

  Summary:
    Reads the timer current count value.

  Description:
    This function reads the timer count value.

  Precondition:
    TCx_CompareInitialize() function must have been called first.

  Parameters:
    None.

  Returns:
    counter - The timer's current count value.

  Example:
    <code>
      uint16_t counter = 0;
      TCx_CompareInitialize();
      TCx_CompareStart();
      counter = TCx_Compare16bitCounterGet();
    </code>

  Remarks:
    The caller must know the number of significant bytes of timer. Period
    value is right-aligned.
*/

uint16_t TCx_Compare16bitCounterGet( void );

// *****************************************************************************
/* Function:
    void TCx_Compare16bitCounterSet( uint16_t count );

  Summary:
    Sets new timer counter value.

  Description:
    This function sets new timer counter value.

  Precondition:
    TCx_CompareInitialize() function must have been called first.

  Parameters:
    count - new counter value to set.

  Returns:
    None.

  Example:
    <code>
      uint16_t count = 0x100;
      TCx_CompareInitialize();
      TCx_CompareStart();
      TCx_Compare16bitCounterSet(count);
    </code>

  Remarks:
    The caller must know the number of significant bytes of timer. Counter
    value is right-aligned.
*/

void TCx_Compare16bitCounterSet( uint16_t count );

// *****************************************************************************
/* Function:
    void TCx_Compare16bitSet( uint16_t compareValue );

  Summary:
    Writes compare value of the given compare channel 1.

  Description:
    Set CC[1] compare value.

  Precondition:
    TCx_CompareInitialize() function must have been called first.

  Parameters:
    compareValue - value to set for compare channel 1.

  Returns:
    None.

  Example:
    <code>
      uint16_t compareValue = 0x100;
      TCx_CompareInitialize();
      TCx_Compare16bitSet(compareValue);
    </code>

  Remarks:
    None
*/

void TCx_Compare16bitSet( uint16_t compareValue );

// *****************************************************************************
/* Function:
    void TCx_Compare32bitPeriodSet( uint32_t period );

  Summary:
    Sets the period value of a given timer.

  Description:
    This function writes the period value. When timer counter matches period
    value,counter is reset and interrupt can be generated.

  Precondition:
    TCx_CompareInitialize() function must have been called first.

  Parameters:
    period - new period value to set for timer.

  Returns:
    None.

  Example:
    <code>
      uint32_t period = 0x500;
      TCx_CompareInitialize();
      TCx_Compare32bitPeriodSet(period);
    </code>

  Remarks:
    The caller must know the number of significant bytes of timer. Period
    value is right-aligned.
*/

void TCx_Compare32bitPeriodSet( uint32_t period );

// *****************************************************************************
/* Function:
    uint32_t TCx_Compare32bitPeriodGet( void );

  Summary:
    Reads the period value of given timer.

  Description:
    This function reads the value of period.

  Precondition:
    TCx_CompareInitialize() function must have been called first.

  Parameters:
    None.

  Returns:
    period - The timer's period value.

  Example:
    <code>
      uint32_t period = 0;
      TCx_CompareInitialize();
      period = TCx_Compare32bitPeriodGet();
    </code>

  Remarks:
    The caller must know the number of significant bytes of timer. Period
    value is right-aligned.
*/

uint32_t TCx_Compare32bitPeriodGet( void );

// *****************************************************************************
/* Function:
    uint32_t TCx_Compare32bitCounterGet( void );

  Summary:
    Reads the timer current count value.

  Description:
    This function reads the timer count value.

  Precondition:
    TCx_CompareInitialize() function must have been called first.

  Parameters:
    None.

  Returns:
    counter - The timer's current count value.

  Example:
    <code>
      uint32_t counter = 0;
      TCx_CompareInitialize();
      TCx_CompareStart();
      counter = TCx_Compare32bitCounterGet();
    </code>

  Remarks:
    The caller must know the number of significant bytes of timer. Period
    value is right-aligned.
*/

uint32_t TCx_Compare32bitCounterGet( void );

// *****************************************************************************
/* Function:
    void TCx_Compare32bitCounterSet( uint32_t count );

  Summary:
    Sets new timer counter value.

  Description:
    This function sets new timer counter value.

  Precondition:
    TCx_CompareInitialize() function must have been called first.

  Parameters:
    count - new counter value to set.

  Returns:
    None.

  Example:
    <code>
      uint32_t count = 0x100;
      TCx_CompareInitialize();
      TCx_CompareStart();
      TCx_Compare32bitCounterSet(count);
    </code>

  Remarks:
    The caller must know the number of significant bytes of timer. Counter
    value is right-aligned.
*/

void TCx_Compare32bitCounterSet( uint32_t count );

// *****************************************************************************
/* Function:
    void TCx_Compare32bitSet( uint32_t compareValue );

  Summary:
    Writes compare value of the given compare channel 1.

  Description:
    Set CC[1] compare value.

  Precondition:
    TCx_CompareInitialize() function must have been called first.

  Parameters:
    compareValue - value to set for compare channel 1.

  Returns:
    None.

  Example:
    <code>
      uint32_t compareValue = 0x100;
      TCx_CompareInitialize();
      TCx_Compare32bitSet(compareValue);
    </code>

  Remarks:
    None
*/

void TCx_Compare32bitSet( uint32_t compareValue );

// *****************************************************************************
/* Function:
    uint32_t TCx_CompareFrequencyGet( void );

  Summary:
    Provides the given timer's counter-increment frequency.

  Description:
    This function provides the frequency at which the given counter
    increments. It can be used to convert differences between counter values
    to real time or real-time intervals to timer period values.

  Precondition:
    TCx_CompareInitialize() function must have been called first.

  Parameters:
    None.

  Returns:
    frequency - The frequency (in Hz) at which the timer's counter increments.

  Example:
    <code>
      uint32_t frequency = 0;
      TCx_CompareInitialize();
      frequency = TCx_CompareFrequencyGet();
    </code>

  Remarks:
    None.
*/

uint32_t TCx_CompareFrequencyGet( void );

// *****************************************************************************
/* Function:
    void TCx_CompareCallbackRegister( TC_CALLBACK callback, uintptr_t context );

  Summary:
    Registers the function to be called from interrupt.

  Description
    This function registers the callback function to be called from interrupt.

  Precondition:
    TCx_CompareInitialize() must have been called first.

  Parameters:
    callback - callback function pointer
    context  - Allows the caller to provide a context value (usually a pointer
               to the callers context for multi-instance clients).

  Returns:
    None.

  Example:
    <code>
      void TC_Callback_Fn( uintptr_t context );

      TCx_CompareInitialize();
      TCx_CompareCallbackRegister(TC_Callback_Fn, NULL);
    </code>

  Remarks:
    Context value can be set to NULL if not required.
    To disable callback function, pass NULL for the callback parameter.
*/

void TCx_CompareCallbackRegister( TC_CALLBACK callback, uintptr_t context );

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END

#endif /* PLIB_TCx_H */
