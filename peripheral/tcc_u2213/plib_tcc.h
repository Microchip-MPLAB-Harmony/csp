/*******************************************************************************
  Timer/Counter for Control(TCC) Peripheral Library Interface Header File

  Company
    Microchip Technology Inc.

  File Name
    plib_tcc.h

  Summary
    TCC peripheral library interface.

  Description
    This file defines the interface to the TCC peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

  Remarks:
    This header is for documentation only.  The actual tcc<x> headers will be
    generated as required by the MHC (where <x> is the peripheral instance
    number).

    Every interface symbol has a lower-case 'x' in it following the "TCC"
    abbreviation.  This 'x' will be replaced by the peripheral instance number
    in the generated headers.  These are the actual functions that should be
    used.

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

#ifndef PLIB_TCCx_H    // Guards against multiple inclusion
#define PLIB_TCCx_H

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
/* TCC Channel numbers

   Summary:
    Identifies channel number within TCC module

   Description:
    This enumeration identifies TCC channel number.

   Remarks:
    None.
*/
typedef enum
{
    TCCx_CHANNEL0,
    TCCx_CHANNEL1,
    TCCx_CHANNEL2,
    TCCx_CHANNEL3,
}TCCx_CHANNEL_NUM;
// *****************************************************************************
/* Callback Function Pointer

  Summary:
    Defines the function pointer data type and function signature for the tcc
    callback function.

  Description:
    This data type defines the function pointer and function signature for the
    tcc callback function. The library will call back the client's
    function with this signature from the interrupt routine.

  Function:
    void (*TCC_CALLBACK)( uint32_t status, uintptr_t context )

  Precondition:
    TCCx_Initialize must have been called for the given TCC channel
    instance and TCCx_CallbackRegister must have been called to register the
    function to be called.

  Parameters:
    status - interrupt status 
    context  - Allows the caller to provide a context value (usually a pointer
    to the callers context for multi-instance clients).

  Returns:
    None.

  Example:
    <code>
    void TCC_Callback_Fn ( uint32_t status, uintptr_t context );

    TCCx_TimerCallbackRegister(TCC_Callback_Fn, NULL);
    </code>

  Remarks:
    None
*/

typedef void (*TCC_CALLBACK)( uint32_t status, uintptr_t context );
// *****************************************************************************
/* Callback structure

   Summary:
    Callback structure

   Description:
    This stores the callback function pointer and context

   Remarks:
    None.
*/
typedef struct
{
    TCC_CALLBACK callback_fn;
    uintptr_t context;
}TCC_CALLBACK_OBJECT;

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
    void TCCx_PWMInitialize ( void );

  Summary:
    Initializes given instance of TCC

  Description:
    This function initializes given instance of TCC in PWM mode with
    the options configured in MCC GUI.

  Precondition:
    MCC GUI should be configured with the desired values.

  Parameters:
    None.

  Returns:
    None.

  Example:
    <code>
    TCC0_PWMInitialize();
    </code>

  Remarks:
    This function must be called before any other TCC function is
    called.  This function is normally only be called once during system
    initialization. Call TCCx_PWMStart to start the counter. 
*/

void TCCx_PWMInitialize ( void );

// *****************************************************************************
/* Function:
    void TCCx_PWMStart ( void );

  Summary:
    Starts PWM generation of given TCC instance

  Description:
    This function enables the TCC and starts the counter of associated instance.

  Precondition:
    TCCx_PWMInitialize() function must have been called first for the given
    instance.

  Parameters:
    None

  Returns:
    None.

  Example:
    <code>
    TCC0_PWMInitialize();
    TCC0_PWMStart();
    </code>

  Remarks:
    Due to synchronization, there is a delay from writing to register until peripheral
    is enabled. This function waits till sync operation is complete. 
*/
void TCCx_PWMStart ( void );

// *****************************************************************************
/* Function:
    void TCCx_PWMStop( void );

  Summary:
    Stops PWM generation of given TCC instance

  Description:
    This function stops the counter of associated instance.

  Precondition:
    TCCx_PWMInitialize() function must have been called first for the given
    instance.

  Parameters:
    None

  Returns:
    None.

  Example:
    <code>
    TCC0_PWMInitialize();
    TCC0_PWMStart();
    // Run application 
    TCC0_PWMStop();
    </code>

  Remarks:
    Due to synchronization, there is a delay from writing to register until peripheral
    is stopped. This function waits till sync operation is complete.
*/
void TCCx_PWMStop ( void );

// *****************************************************************************
/* Function:
    void TCCx_PWM24bitPeriodSet ( uint32_t period );

  Summary:
    Sets the period value of a given TCC instance.

  Description:
    This function writes the period value. Period value is shared between 
    all the channels of TCC instance. When counter matches period
    value interrupt can be generated. This function writes to the double buffered register. 
    Actual update happens on period match or zero match.

  Precondition:
    TCCx_PWMInitialize function must have been called first for the given
    channel.

  Parameters:
    period - Period value. Counter increments till this value.

  Returns:
    None.

  Example:
    <code>
    TCC0_PWMInitialize();
    TCC0_PWM24bitPeriodSet(0x500ul);
    </code>

  Remarks:
    None 
*/

void TCCx_PWM24bitPeriodSet ( uint32_t period );

// *****************************************************************************
/* Function:
    uint32_t TCCx_PWM24bitPeriodGet ( void );

  Summary:
    Reads the period value of a given TCC instance.

  Description:
    This function reads the period value. 

  Precondition:
    TCCx_PWMInitialize function must have been called first for the given
    channel.

  Parameters:
    None

  Returns:
    period - period value of TCC instance

  Example:
    <code>
    uint32_t period;
    TCC0_PWMInitialize();
    period = TCC0_PWM24bitPeriodGet();
    </code>

  Remarks:
    None
*/

uint32_t TCCx_PWM24bitPeriodGet ( void );

// *****************************************************************************
/* Function:
    void TCCx_PWM24bitDutySet (TCCx_CHANNEL_NUM channel, uint32_t duty);

  Summary:
    Sets the duty value of a given TCC channel.

  Description:
    This function writes the compare value. Every channel of TCC instance has its own compare register. 
    When counter matches compare value interrupt can be generated. This function writes to the double buffered register. 
    Actual update happens on period match or zero match.

  Precondition:
    TCCx_PWMInitialize function must have been called first for the given
    channel.

  Parameters:
    channel - TCC channel number
    duty - Compare value

  Returns:
    None

  Example:
    <code>

    TCC0_PWMInitialize();
    TCC0_PWM24bitDutySet(TCC0_CHANNEL0, 0x100U);
    </code>

  Remarks:
    None 
*/
void TCCx_PWM24bitDutySet(TCCx_CHANNEL_NUM channel, uint32_t duty);

// *****************************************************************************
/* Function:
    void TCCx_PWM24bitCounterSet(uint32_t count);

  Summary:
    Sets the counter value of a given TCC instance

  Description:
    This function updates the counter value. 

  Precondition:
    TCCx_PWMInitialize function must have been called first for the given
    channel.

  Parameters:
    count - counter value

  Returns:
    None

  Example:
    <code>
    TCC0_PWMInitialize();
    TCC0_PWM24bitCounterSet(0x100U);
    </code>

  Remarks:
    This function waits till sync operation is complete.
*/
void TCCx_PWM24bitCounterSet(uint32_t count);

// *****************************************************************************
/* Function:
    void TCCx_PWM16bitPeriodSet ( uint16_t period );

  Summary:
    Sets the period value of a given TCC instance.

  Description:
    This function writes the period value. Period value is shared between 
    all the channels of TCC instance. When counter matches period
    value interrupt can be generated. This function writes to the double buffered register. 
    Actual update happens on period match or zero match.

  Precondition:
    TCCx_PWMInitialize function must have been called first for the given
    channel.

  Parameters:
    period - Period value. Counter increments till this value.

  Returns:
    None.

  Example:
    <code>
    TCC0_PWMInitialize();
    TCC0_PWM16bitPeriodSet(0x500ul);
    </code>

  Remarks:
    None 
*/

void TCCx_PWM16bitPeriodSet ( uint16_t period );

// *****************************************************************************
/* Function:
    uint16_t TCCx_PWM16bitPeriodGet ( void );

  Summary:
    Reads the period value of a given TCC instance.

  Description:
    This function reads the period value. 

  Precondition:
    TCCx_PWMInitialize function must have been called first for the given
    channel.

  Parameters:
    None

  Returns:
    period - period value of TCC instance

  Example:
    <code>
    uint16_t period;
    TCC0_PWMInitialize();
    period = TCC0_PWM16bitPeriodGet();
    </code>

  Remarks:
    None
*/

uint16_t TCCx_PWM16bitPeriodGet ( void );

// *****************************************************************************
/* Function:
    void TCCx_PWM16bitDutySet (TCCx_CHANNEL_NUM channel, uint16_t duty);

  Summary:
    Sets the duty value of a given TCC channel.

  Description:
    This function writes the compare value. Every channel of TCC instance has its own compare register. 
    When counter matches compare value interrupt can be generated. This function writes to the double buffered register. 
    Actual update happens on period match or zero match.

  Precondition:
    TCCx_PWMInitialize function must have been called first for the given
    channel.

  Parameters:
    channel - TCC channel number
    duty - Compare value

  Returns:
    None

  Example:
    <code>

    TCC0_PWMInitialize();
    TCC0_PWM16bitDutySet(TCC0_CHANNEL0, 0x100U);
    </code>

  Remarks:
    None 
*/
void TCCx_PWM16bitDutySet(TCCx_CHANNEL_NUM channel, uint16_t duty);

// *****************************************************************************
/* Function:
    void TCCx_PWM16bitCounterSet(uint16_t count);

  Summary:
    Sets the counter value of a given TCC instance

  Description:
    This function updates the counter value. 

  Precondition:
    TCCx_PWMInitialize function must have been called first for the given
    channel.

  Parameters:
    count - counter value

  Returns:
    None

  Example:
    <code>
    TCC0_PWMInitialize();
    TCC0_PWM16bitCounterSet(0x100U);
    </code>

  Remarks:
    This function waits till sync operation is complete.
*/
void TCCx_PWM16bitCounterSet(uint16_t count);


// *****************************************************************************
/* Function:
    void TCCx_PWMDeadTimeSet(uint8_t deadtime_high, uint8_t deadtime_low);

  Summary:
    Sets the dead time of a given TCC module.

  Description:
    This function updates low-side and high-side dead time. 
    Dead time values are applicable to all the channels of the TCC module.

  Precondition:
    TCCx_PWMInitialize function must have been called first for the given
    channel. And TCC module is in disabled (stopped) state.

  Parameters:
    deadtime_high - dead-time for high side
    deadtime_low - dead-time for low side

  Returns:
    none

  Example:
    <code>
    TCC0_PWMInitialize();
    TCC0_PWMDeadTimeSet(0x100U, 0x100U);
    </code>

  Remarks:
    This function can be called only when TCC module is disabled.
*/
void TCCx_PWMDeadTimeSet(uint8_t deadtime_high, uint8_t deadtime_low);

// *****************************************************************************
/* Function:
    void TCCx_PWMForceUpdate(void);

  Summary:
    Updates double buffer register value to actual register asynchronously

  Description:
    This function updates double buffer register value to actual register asynchronously.

  Precondition:
    TCCx_PWMInitialize function must have been called first for the given
    channel and new value is written in double buffer register.

  Parameters:
    None

  Returns:
    None

  Example:
    <code>
    TCC0_PWMInitialize();
    TCC0_PWMForceUpdate();
    </code>

  Remarks:
    None
*/
void TCCx_PWMForceUpdate(void);

// *****************************************************************************
/* Function:
    void TCCx_PWMPeriodInterruptEnable(void);

  Summary:
    Enables period interrupt 

  Description:
    This function enables period interrupt when counter matches period value while counting UP or
    when counter matches zero while counting DOWN

  Precondition:
    TCCx_PWMInitialize function must have been called first for the given
    channel

  Parameters:
    None

  Returns:
    None

  Example:
    <code>
    TCC0_PWMInitialize();
    TCC0_PWMPeriodInterruptEnable();
    </code>

  Remarks:
    None
*/
void TCCx_PWMPeriodInterruptEnable(void);

// *****************************************************************************
/* Function:
    void TCCx_PWMPeriodInterruptDisable(void);

  Summary:
    Disables period interrupt 

  Description:
    This function disables period interrupt 

  Precondition:
    TCCx_PWMInitialize function must have been called first for the given
    channel

  Parameters:
    None

  Returns:
    None

  Example:
    <code>
    TCC0_PWMInitialize();
    TCC0_PWMPeriodInterruptDisable();
    </code>

  Remarks:
    None
*/
void TCCx_PWMPeriodInterruptDisable(void);

// *****************************************************************************
/* Function:
    void TCCx_PWMInterruptStatusGet(void);

  Summary:
    Reads the interrupt flags

  Description:
    This function reads interrupt flags to check which interrupt flag is set 

  Precondition:
    TCCx_PWMInitialize function must have been called first for the given
    channel

  Parameters:
    None

  Returns:
    None

  Example:
    <code>
    uint32_t interrupt_status;
    TCC0_PWMInitialize();
    interrupt_status = TCC0_PWMInterruptStatusGet();
    </code>

  Remarks:
    None
*/
uint32_t TCCx_PWMInterruptStatusGet(void);

// *****************************************************************************
/* Function:
    void TCC${TCC_INDEX}_PWMCallbackRegister(TCC_CALLBACK callback, uintptr_t context)

  Summary:
    Registers the function to be called from interrupt.

  Description
    This function registers the callback function to be called from interrupt

  Precondition:
    TCCx_PWMInitialize must have been called first.

  Parameters:
      callback  - Callback function pointer.

      context   - Value provided back to the caller by the callback (usually a
                  pointer to the caller's context for multi-instance clients).

  Returns:
    None.

  Example:
    <code>
    void TCC_CallbackFn(uintptr_t context);

    TCC0_PWMInitialize();
    TCC0_PWMCallbackRegister(TCC_CallbackFn, (uintptr_t)NULL);
    </code>

  Remarks:
    Context value can be set to NULL if not required.

    To disable callback function, pass NULL for the callback parameter.
*/

void TCCx_PWMCallbackRegister(TCC_CALLBACK callback, uintptr_t context);

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END

#endif /* PLIB_TCCx_H */
