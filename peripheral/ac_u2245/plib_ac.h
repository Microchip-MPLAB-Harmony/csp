/*******************************************************************************
  Analog Comparator PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_ac.h

  Summary:
    AC Header File

  Description:
    This file defines the interface to the AC peripheral library.
    This library provides access to and control of the Analog Comparator.

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
#ifndef PLIB_AC_H     // Guards against multiple inclusion
#define PLIB_AC_H

#include <stdint.h>
#include <stdbool.h>
#include <stddef.h>
#include "${__PROCESSOR}.h"

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility
    extern "C" {
#endif
// DOM-IGNORE-END

// *****************************************************************************
/* AC Callback Function pointer
    typedef void (*AC_CALLBACK) (uintptr_t context)

  Summary:
    Pointer to a AC callback function

  Description:
    This data type defines the required function signature for the AC Callback
    function.
    A client must register a pointer to a callback function whose function
    signature (parameter and return value types) match the types specified by
    this function pointer in order to receive event callback.
    The parameters and return values and are described here and a partial
    example implementation is provided.

  Parameters:
    context - Value identifying the context of the application that registered
              the callback function.

  Returns:
    None.

  Example:
    Refer to the AC_CallbackRegister( ) function code example.

  Remarks:
    None
*/

typedef void (*AC_CALLBACK) (uintptr_t context);

// *****************************************************************************
// *****************************************************************************
// Section: Local: **** Do Not Use ****
// *****************************************************************************
// *****************************************************************************
// *****************************************************************************

/* Callback Structure

  Summary:
    Stores callback function pointer and context.

  Description:
    This structure stores callback function pointer and context.

  Remarks:
    Refer to the specific device data sheet to determine availability.
*/
typedef struct
{
    AC_CALLBACK callback;
    uintptr_t    context;

} AC_OBJECT ;

// *****************************************************************************
/* User AC Interrupt Modes

  Summary:
    Identifies the modes for AC Module.

  Description:
    This enums identifies either Output mode or window mode interrupt of
    AC module.

  Remarks:
    Refer to the specific device data sheet to determine availability.
*/
typedef enum
{
    /* Analog Comparator Output Interrupt */
    AC_OUTPUT_INTERRUPT = 0,

    /* Analog Comparator Window Mode Output Interrupt */
    AC_WIN_INTERRUPT = 1

} AC_INTERRUPTS;

// *****************************************************************************
/* User AC Output Modes

  Summary:
    Identifies the Output mode for AC Module.

  Description:
    This enums identifies either Interrupt or Non Interrupt or
    Window interrupt mode for output of AC module.

  Remarks:
    Refer to the specific device data sheet to determine availability.
*/
typedef enum
{
    /* Analog Comparator Output - Non Interrupt Mode */
    AC_OUTPUT = 0,

    /* Analog Comparator Output - Interrupt Mode */
    AC_INTERRUPT = 1,

    /* Analog Comparator Output - Window Mode */
    AC_WINDOW_INTERRUPT = 2

} AC_STATUS;

// *****************************************************************************
/* User AC Output Channels

  Summary:
    Identifies the AC output channel number.

  Description:
    This enums identifies the AC output channel number.

  Remarks:
    Refer to the specific device data sheet to determine availability.
*/
typedef enum
{
    /** Comparator channel 0 */
    AC_CHANNEL_0 = 0,

    /** Comparator channel 1*/
    AC_CHANNEL_1 = 1,

    /** Comparator channel 2*/
    AC_CHANNEL_2 = 2,

    /** Comparator channel 3*/
    AC_CHANNEL_3 = 3

} AC_CHANNEL;

// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Function:
    void AC_Initialize(void)

  Summary:
     Initializes given instance of the AC peripheral.

  Description:
    This function initializes the given instance of the AC peripheral as
    configured by the user from within the MHC.

  Precondition:
    None.

  Parameters:
    None.

  Returns:
    None.

  Example:
    <code>
    AC_Initialize();
    </code>

  Remarks:
    This function must be called before any other AC function is called and it
    should be called only once.
*/

void AC_Initialize (void);

// *****************************************************************************
/* Function:
    void AC_Start( void )

  Summary:
    Triggers a comparator to start comparison.

  Description:
    This routine triggers a comparator to start comparison

  Precondition:
    AC_Initialize() should have been called before calling this
    function.

  Parameters:
    None.

  Returns:
   Returns the comparison status.

  Example:
    <code>
    AC_Start();
    </code>

  Remarks:
    None.
*/

void AC_Start( void );

// *****************************************************************************
/* Function:
    void AC_SwapInputs( AC_CHANNEL channel_id )

  Summary:
    Swap inputs of a comparator.

  Description:
    This routine swaps inputs of a comparator.

  Remarks:
    Refer plib_${AC_INSTANCE_NAME?lower_case}.h file for more information.
*/

void AC_SwapInputs( AC_CHANNEL channel_id );

// *****************************************************************************
/* Function:
    bool AC_StatusGet(AC_STATUS status, AC_CHANNEL channel)

  Summary:
    Gets the current comparison status of the AC module.

  Description:
    This routine provides the current comparison status of the AC  module.

  Precondition:
    AC_Initialize() should have been called before calling this
    function.

  Parameters:
    status  - AC_OUTPUT, To know the comparator output status.
              AC_INTERRUPT, To know the comparator status for interrupt .
              AC_WINDOW_INTERRUPT, To know the comparator status for window
              interrupt mode.
    channel - Comparator Channel Number

  Returns:
   Returns the comparison status.

  Example:
    <code>
    bool status;
    status = AC_StatusGet(AC_OUTPUT,AC_CHANNEL_0);
    if (status)
    {
        // Application related tasks
    }
    </code>

  Remarks:
    None.
*/

bool ${AC_INSTANCE_NAME}_StatusGet ( AC_STATUS status, AC_CHANNEL channel);

// *****************************************************************************
/* AC Callback Function pointer
    typedef void (*AC_CALLBACK) (uintptr_t context)

  Summary:
    Pointer to a AC callback function

  Description:
    This data type defines the required function signature for the AC Callback
    function.
    A client must register a pointer to a callback function whose function
    signature (parameter and return value types) match the types specified by
    this function pointer in order to receive event callback.
    The parameters and return values and are described here and a partial
    example implementation is provided.

  Parameters:
    context - Value identifying the context of the application that registered
              the callback function.

  Returns:
    None.

  Example:
    Refer to the AC_CallbackRegister( ) function code example.

  Remarks:
    None
*/

typedef void (*AC_CALLBACK) (uintptr_t context);

// *****************************************************************************
/* Function:
    void AC_CallbackRegister (AC_CALLBACK callback, uintptr_t context)

  Summary:
    Allows a client to identify a callback function.

  Description:
    This routine allows a client to identify a callback function.

  Precondition:
    AC_Initialize() should have been called before calling this
    function.

  Parameters:
    callback - Pointer to the callback function.
    context  - The value of parameter will be passed back to the client
               unchanged, when the callback function is called.  It can be
               used to identify any client specific data object that identifies
               the instance of the client module (for example, it may be a
               pointer to the client module's state structure).

  Returns:
    None.

  Example:
    <code>
    MY_APP_OBJ myAppObj;

    void APP_AC_CallbackFunction (uintptr_t context)
    {
        // The context was set to an application specific object.
        // It is now retrievable easily in Callback function.
           MY_APP_OBJ myAppObj = (MY_APP_OBJ *) context;
        //Application related tasks
    }

    AC_CallbackRegister (APP_AC_CallbackFunction, (uintptr_t)&myAppObj);
    </code>

  Remarks:
    None.

*/
void AC_CallbackRegister (AC_CALLBACK callback, uintptr_t context);

#endif /* PLIB_AC_H */
