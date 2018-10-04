/*******************************************************************************
  PWM Peripheral Library Interface Header File

  Company
    Microchip Technology Inc.

  File Name
    plib_pwm.h

  Summary
    PWM peripheral library interface.

  Description
    This file defines the interface to the PWM peripheral library.  This
    library provides access to and control of the associated peripheral
    instance.

  Remarks:
    This header is for documentation only.  The actual PWM<x> headers will be
    generated as required by the MCC (where <x> is the peripheral instance
    number).

    Every interface symbol has a lower-case 'x' in it following the "PWM"
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

#ifndef PLIB_PWMx_H    // Guards against multiple inclusion
#define PLIB_PWMx_H


// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

/*  This section lists the other files that are included in this file.
*/

#include <stddef.h>
#include <stdbool.h>

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
/* Callback Function Pointer

   Summary:
    Defines the data type and function signature for the PWM peripheral
    callback function.

   Description:
    This data type defines the function signature for the PWM peripheal
    callback function. The library will call back the client's
    function with this signature from the interrupt context.

   Function:
    void (*PWMx_CALLBACK)( uintptr_t context )

   Precondition:
    PWMx_Initialize must have been called for the given PWM peripheral
    instance and PWMx_CallbackRegister must have been called to register the
    function to be called.

   Parameters:
    context  - Allows the caller to provide a context value (usually a pointer
    to the callers context for multi-instance clients).

   Returns:
    None.

   Example:
    <code>
    // callback function
    void PWM_Counter_Callback (uintptr_t context);

    // register callback function
    PWMx_CallbackRegister(PWM_Counter_Callback, NULL);
    </code>

    Remarks:
        None.
*/
typedef void (*PWM_CALLBACK)( uintptr_t context );
// *****************************************************************************
/* PWM channel number

   Summary:
    Identifies PWM channel number in a PWM peripheral

   Description:
    This enumeration identifies PWM channel number in a PWM peripheral. This
    can be used as an argument in the APIs

   Remarks:
    None.
*/
typedef enum
{
    PWM_CHANNEL_0,
    PWM_CHANNEL_1,
    PWM_CHANNEL_2,
    PWM_CHANNEL_3
}PWM_CHANNEL_NUM;
// *****************************************************************************
/* PWM channel number mask

   Summary:
    Identifies PWM channel mask

   Description:
    This enumeration identifies PWM channel mask. This can be ORed together
    to start/stop channels together.

   Remarks:
    None.
*/
typedef enum
{
    PWM_CHANNEL_0_MASK = (1U << 0U),
    PWM_CHANNEL_1_MASK = (1U << 1U),
    PWM_CHANNEL_2_MASK = (1U << 2U),
    PWM_CHANNEL_3_MASK = (1U << 3U)
}PWM_CHANNEL_MASK;

// *****************************************************************************
/* PWM compare unit

   Summary:
    Identifies PWM compare unit

   Description:
    This enumeration identifies PWM compare unit.

   Remarks:
    None.
*/
typedef enum
{
    PWM_COMPARE_0,
    PWM_COMPARE_1,
    PWM_COMPARE_2,
    PWM_COMPARE_3,
    PWM_COMPARE_4,
    PWM_COMPARE_5,
    PWM_COMPARE_6,
    PWM_COMPARE_7,
}PWM_COMPARE;

// *****************************************************************************
/* PWM fault ID

   Summary:
    Identifies PWM fault input ids

   Description:
    This enumeration defines the PWM fault IDs

   Remarks:
    None.
*/
typedef enum
{
    PWM_FAULT_ID_0,
    PWM_FAULT_ID_1,
    PWM_FAULT_ID_2,
    PWM_FAULT_ID_3,
    PWM_FAULT_ID_4,
    PWM_FAULT_ID_5,
    PWM_FAULT_ID_6,
    PWM_FAULT_ID_7,
}PWM_FAULT_ID;

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
    PWM_CALLBACK callback_fn;
    uintptr_t context;
}PWM_CALLBACK_OBJECT;

// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************
/* The following functions make up the methods (set of possible operations) of
   this interface.
*/

// *****************************************************************************/

/* **************************************************************************** */
/* Function:
    void PWMx_Initialize (void);

  Summary:
    Initializes given instance of PWM peripheral

  Description:
    This function initializes given instance of PWM periphral with the values
    configured in MCC GUI. This initializes all the selected channels of given peripheal in MCC GUI.

  Precondition:
    MCC GUI should be configured with the right values.

  Parameters:
    None.

  Returns:
    None.

  Example:
    <code>
        PWM0_Initialize();
    </code>

  Remarks:
    This function must be called before any other PWM function is
    called.

    This function should only be called once during system
    initialization.
*/
void PWMx_Initialize (void);
// *****************************************************************************

/* Function:
    void PWMx_ChannelsStart (PWM_CHANNEL_MASK channelMask);

  Summary:
    Starts the given PWM channels

  Description:
    This function enables the PWM channels specified in channelMask. If channels are
    configured in sync mode, only channel 0 should be enabled which will ensure all sync
    channels are started together.

  Precondition:
    PWMx_Initialize() function must have been called first for the associated instance.

  Parameters:
    channelMask - set of channel numbers

  Returns:
    None.

  Example:
    <code>
        PWM0_Initialize();
        PWM0_ChannelsStart(PWM_CHANNEL_0_MASK);
    </code>

  Remarks:
    None
*/
void PWMx_ChannelsStart (PWM_CHANNEL_MASK channelMask);
// *****************************************************************************

/* Function:
    void PWMx_ChannelsStop (PWM_CHANNEL_MASK channelMask);

  Summary:
    Stops the given PWM channels

  Description:
    This function disables the PWM channels specified in channelMask. If channels are
    configured in sync mode, only channel 0 should be disabled which will ensure all sync
    channels are stopped together.

  Precondition:
    PWMx_Initialize() function must have been called first for the associated instance.

  Parameters:
    channelMask - set of channel numbers

  Returns:
    None.

  Example:
    <code>
        PWM0_Initialize();
        PWM0_ChannelsStart(PWM_CHANNEL_0_MASK);
        PWM0_ChannelsStop(PWM_CHANNEL_0_MASK);
    </code>

  Remarks:
    None
*/
void PWMx_ChannelsStop (PWM_CHANNEL_MASK channelMask);
// *****************************************************************************

/* Function:
    void PWMx_ChannelPeriodSet (PWM_CHANNEL_NUM channel, uint32_t period);

  Summary:
    Sets the period value of given PWM channel

  Description:
    This function writes the period value in double buffer register. Update to the
    actual period register happens at the next period border.
    For left-aligned mode, update occurs when counter value = period value
    For center-aligned mode, update occurs when counter value = 0 while decrementing

  Precondition:
    PWMx_Initialize() function must have been called first for the associated instance.
    And associated channel must be running.

  Parameters:
    channel - PWM channel number
    period - period value corresponding to PWM frequency

  Returns:
    None.

  Example:
    <code>
        PWM0_Initialize();
        PWM0_ChannelsStart(PWM_CHANNEL_0_MASK);
        PWM0_ChannelPeriodSet(PWM_CHANNEL_0, 0x500);
    </code>

  Remarks:
    In sync mode, unlock bit (PWM_SCUC.UPDULOCK) should be set explicitly to trigger the update of period value
    at the next PWM period border. Use API PWMx_SyncUpdateEnable to set the PWM_SCUC.UPDULOCK bit.
*/
void PWMx_ChannelPeriodSet (PWM_CHANNEL_NUM channel, uint16_t period);
// *****************************************************************************

/* Function:
    uint16_t PWMx_ChannelPeriodGet (PWM_CHANNEL_NUM channel);

  Summary:
    Reads the period value of given PWM channel

  Description:
    This function reads the period value of given PWM channel.

  Precondition:
    PWMx_Initialize() function must have been called first for the associated instance.

  Parameters:
    channel - PWM channel

  Returns:
    The PWM channel's period value

  Example:
    <code>
        uint16_t period;
        PWM0_Initialize();
        period = PWM0_ChannelPeriodGet(PWM_CHANNEL_0);
    </code>

  Remarks:
    None
*/
uint16_t PWMx_ChannelPeriodGet (PWM_CHANNEL_NUM channel);
// *****************************************************************************

/* Function:
    void PWMx_ChannelDutySet(PWM_CHANNEL_NUM channel);

  Summary:
    Writes the duty cycle value of given PWM channel

  Description:
    This function writes the duty cycle value in double buffer register. Update to the
    actual duty cycle register happens at the next period border.
    For left-aligned mode, update occurs when counter value = period value
    For center-aligned mode, update occurs when counter value = 0 while decrementing OR
                                                counter value = period value while incrementing

  Precondition:
    PWMx_Initialize() function must have been called first for the associated instance.
    And associated channel must be running.

  Parameters:
    channel - PWM channel number
    duty - duty cycle value which determines ON time of waveform

  Returns:
    channel - PWM channel number
    duty - duty cycle value

  Example:
    <code>
        PWM0_Initialize();
        PWM0_ChannelsStart(PWM_CHANNEL_0_MASK);
        PWM0_ChannelDutySet(PWM_CHANNEL_0, 0x200);
    </code>

  Remarks:
    In sync mode update method 0 (manual update of duty cycle), unlock bit (PWM_SCUC.UPDULOCK) should be set
    explicitly to trigger the update of duty cycle value at the next PWM period border.
    Use API PWMx_SyncUpdateEnable to set the PWM_SCUC.UPDULOCK bit.
*/
void PWMx_ChannelDutySet(PWM_CHANNEL_NUM channel, uint16_t duty);
// *****************************************************************************

/* Function:
    void PWMx_ChannelDeadTimeSet (PWM_CHANNEL_NUM channel, uint16_t deadtime_high, uint16_t deadtime_low);

  Summary:
    Writes dead time values of given PWM channel.

  Description:
    This function writes the dead time value in double buffer register. Update to the
    actual dead time register happens at the next period border.
    For left-aligned mode, update occurs when counter value = period value
    For center-aligned mode, update occurs when counter value = 0 while decrementing

  Precondition:
    PWMx_Initialize() function must have been called first for associated channel.
    And associated PWM channel must be running.

  Parameters:
    channel - PWM channel number
    deadtime_high - dead time inserted on high side output waveform
    deadtime_low - dead time inserted on low side output waveform

  Returns:
    None

  Example:
    <code>
        PWM0_Initialize();
        PWM0_ChannelsStart(PWM_CHANNEL_0_MASK);
        PWM0_ChannelDeadTimeSet(PWM_CHANNEL_0, 0x250, 0x50);
    </code>

  Remarks:
    Dead time is inserted between the edges of the two complementary outputs DTOHx and DTOLx to safely drive
    the external power control switches.

    In sync mode, unlock bit (PWM_SCUC.UPDULOCK) should be set explicitly to trigger the update of dead time value
    at the next PWM period border. Use API PWMx_SyncUpdateEnable to set the PWM_SCUC.UPDULOCK bit.
*/
void PWMx_ChannelDeadTimeSet (PWM_CHANNEL_NUM channel, uint16_t deadtime_high, uint16_t deadtime_low);
// *****************************************************************************

/* Function:
    void PWMx_CompareValueSet (PWM_COMPARE cmp_unit, uint16_t cmp_value);

  Summary:
    Writes the compare value for given PWM peripheral and given comparison unit

  Description:
    This function writes compare value in a double buffer register. Update to the actual
    compare value register happens at the PWM period border when compare period counter expires.

  Precondition:
    PWMx_Initialize() function must have been called first for the associated instance.
    And associated channel must be running.

  Parameters:
    cmp_unit - compare unit number
    cmp_value - compare value which is compared with channel 0 counter

  Returns:
    None

  Example:
    <code>
        PWM0_Initialize();
        PWM0_ChannelsStart(PWM_CHANNEL_0_MASK);
        PWM0_CompareValueSet(PWM_COMPARE_0, 0x25);
    </code>

  Remarks:
    When compare value matches the counter of PWM channel 0, interrupt is generated and
    also pulse is generated on PWM event line which can be used to synchronize ADC conversion.
*/
void PWMx_CompareValueSet (PWM_COMPARE cmp_unit, uint16_t cmp_value);
// *****************************************************************************

/* Function:
    void PWMx_ChannelCounterEventEnable (PWM_CHANNEL_MASK channelMask);

  Summary:
    Enables counter event of given channels

  Description:
    This function enables the counter event of channels specified in channelMask.
    For left-aligned mode, counter event occurs when counter value = period value
    For center-aligned mode, counter event is based on configuration
    counter value = period value or
    counter value = period value and counter value = 0 while decrementing

  Precondition:
    PWMx_Initialize() function must have been called first for the associated instance.

  Parameters:
    channelMask - set of channel numbers

  Returns:
    None

  Example:
    <code>
        PWM0_Initialize();
        PWM0_ChannelCounterEventEnable(PWM_CHANNEL_0_MASK);
    </code>

  Remarks:
    None
*/
void PWMx_ChannelCounterEventEnable (PWM_CHANNEL_MASK channelMask);

// *****************************************************************************

/* Function:
    void PWMx_ChannelCounterEventDisable (PWM_CHANNEL_MASK channelMask);

  Summary:
    Disables counter event of given channels

  Description:
    This function disables the counter event of channels specified in channelMask.

  Precondition:
    PWMx_Initialize() function must have been called first for the associated instance.

  Parameters:
    channelMask - set of channel numbers

  Returns:
    None

  Example:
    <code>
        PWM0_Initialize();
        PWM0_ChannelCounterEventDisable(PWM_CHANNEL_0_MASK);
    </code>

  Remarks:
    None
*/
void PWMx_ChannelCounterEventDisable (PWM_CHANNEL_MASK  channelMask);

// *****************************************************************************

/* Function:
    bool PWMx_ChannelCounterEventStatusGet (PWM_CHANNEL_MASK  channelMask);

  Summary:
    Disables counter event of given channels

  Description:
    This function disables the counter event of channels specified in channelMask.

  Precondition:
    PWMx_Initialize() function must have been called first for the associated instance.

  Parameters:
    channel - channel number

  Returns:
    status of an interrupt
    True - counter event of a channel occured
    False - counter event of a channel is not yet occured

  Example:
    <code>
        bool status;
        PWM0_Initialize();
        status = PWM0_ChannelCounterEventStatusGet(PWM_CHANNEL_0);
    </code>

  Remarks:
    None
*/
bool PWMx_ChannelCounterEventStatusGet (PWM_CHANNEL_NUM channel);

// *****************************************************************************

/* Function:
    void PWMx_SyncUpdateEnable (void);

  Summary:
    This sets the synchronous update unlock bit

  Description:
    This function sets the synchronous update unlock bit which enables
    update of period, duty and dead-time values from double buffer register to actual register at the next
    PWM period border.

  Precondition:
    PWMx_Initialize() function must have been called first for the associated instance.
    And new period or duty or dead-time value must have been written in a double buffer register.

  Parameters:
    None

  Returns:
    None

  Example:
    <code>
        PWM0_Initialize();
        PWM0_SyncUpdateEnable();
    </code>

  Remarks:
    In sync mode update method 1 (manual update), this function has to be called to update period, duty and
    dead-time values to actual register.
    In sync mode update method 2 (automatic update), this function has to be called to update only period and dead-time.
    Duty value update happens automatically.
*/
void PWMx_SyncUpdateEnable (void);

// *****************************************************************************
/* Function:
    void PWMx_FaultStatusClear(PWM_FAULT_ID fault_id);

  Summary:
    This function clears the status of the given fault id

  Description:
    This function clears the fault status of the given id. When fault mode is set as "fault is active
    until cleared at peripheral level and also at the register level", this function clears
    the fault status at the register level.

  Precondition:
    PWMx_Initialize() function must have been called first for the associated instance.

  Parameters:
    None

  Returns:
    None

  Example:
    <code>
        PWM0_Initialize();
        PWM0_FaultStatusClear(PWM_FAULT_ID_0);
    </code>

  Remarks:
    Fault becomes inactive after this function call, only if fault input level is cleared.
*/
void PWMx_FaultStatusClear(PWM_FAULT_ID fault_id);

// *****************************************************************************
/* Function:
    void PWMx_CallbackRegister (PWM_CALLBACK callback, uintptr_t context);

  Summary:
    Registers the function to be called from interrupt

  Description
    This function registers the callback function to be called from interrupt

  Precondition:
    PWMx_Initialize() must have been called first for the associated instance.

  Parameters:
    callback - callback function pointer
    context - Allows the caller to provide a context value (usually a pointer
    to the callers context for multi-instance clients).

  Returns:
    None.

  Example:
    <code>
        void PWM_Callback_Fn(uintptr_t context);

        PWM0_Initialize();
        PWMx_CallbackRegister(PWM_Callback_Fn, NULL);
    </code>

  Remarks:
    Context value can be set to NULL if not required.
    To disable callback function, pass NULL for the callback parameter.
*/
void PWMx_CallbackRegister(PWM_CALLBACK callback, uintptr_t context);

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

}

#endif
// DOM-IGNORE-END

#endif //PLIB_PWMx_H

/**
 End of File
*/
