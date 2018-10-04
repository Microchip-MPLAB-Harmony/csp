/*******************************************************************************
  Watch Dog Timer PLIB.

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${WDT_INSTANCE_NAME?lower_case}.h

  Summary:
    Interface definition of ${WDT_INSTANCE_NAME} PLIB.

  Description:
    This file defines the interface for the WDT Plib.
    It allows user to setup timeout duration and restart watch dog timer.
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

#ifndef PLIB_${WDT_INSTANCE_NAME}_H
#define PLIB_${WDT_INSTANCE_NAME}_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
/* This section lists the other files that are included in this file.
*/

#include <stdint.h>
#include <stdbool.h>
#include <stddef.h>
#include "device.h"

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility
extern "C" {
#endif
// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
/* Callback Function Pointer

  Summary:
    Defines the data type and function signature for the WDT peripheral callback
    function.

  Description:
    This data type defines the function signature for the WDT peripheral
    callback function. The WDT peripheral will call back the client's function
    with this signature when the a Early Warning Event occurred. This interrupt
    indicates to the application that an WDT timeout is about to occur.

  Precondition:
    WDT_Initialize must have been called for the given WDT peripheral instance
    and WDT_CallbackRegister must have been called to set the function to be
    called.

  Parameters:
    context - Allows the caller to provide a context value (usually a pointer
    to the callers context for multi-instance clients).

  Returns:
    None.
*/

typedef void (*WDT_CALLBACK)(uintptr_t context);

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
    void ${WDT_INSTANCE_NAME}_Initialize( void )

  Summary:
    Initializes given instance of the WDT peripheral.

  Description:
    This function initializes the given instance of the WDT peripheral as
    configured by the user from within the MCC.

  Precondition:
    None.

  Parameters:
    None.

  Returns:
    None.

  Example:
    <code>
    ${WDT_INSTANCE_NAME}_Initialize();
    </code>

  Remarks:
    The WDT peripheral is also configured by setting in the NVM User Row. These
    settings are specified though compiler provided fuse settings.
*/

void ${WDT_INSTANCE_NAME}_Initialize( void );

// *****************************************************************************
/* Function:
    void ${WDT_INSTANCE_NAME}_Enable( void )

  Summary:
    Enables the WDT peripheral.

  Description:
    This function enables the WDT peripheral. Calling this function will cause
    the WDT to start counting up to the configured timeout value.

  Precondition:
    None.

  Parameters:
    None.

  Returns:
    None.

  Example:
    <code>
    ${WDT_INSTANCE_NAME}_Enable();
    </code>

  Remarks:
    None.
*/

void ${WDT_INSTANCE_NAME}_Enable( void );

// *****************************************************************************
/* Function:
    void ${WDT_INSTANCE_NAME}_Disable( void )

  Summary:
    Disables the WDT peripheral.

  Description:
    This function is used to stop the WDT counter and disable WDT peripheral.

  Precondition:
    WDT must be enabled using ${WDT_INSTANCE_NAME}_Enable().

  Parameters:
    None

  Returns:
    None.

  Example:
    <code>
    ${WDT_INSTANCE_NAME}_Disable();
    </code>

  Remarks:
    Certain devices does not allow disabling Watchdog timers once enabled.
    This API will not have any effect if ALWAYSON bit in watchdog is enabled.
*/

void ${WDT_INSTANCE_NAME}_Disable( void );

// *****************************************************************************
/* Function:
    void ${WDT_INSTANCE_NAME}_Clear( void )

  Summary:
    Restarts the WDT counter.

  Description:
    This function is used to restart the WDT counter to avoid timeout. Calling
    this will clear the WDT timeout counter and restart the counting from 0.
    Failure to call this function before the WDT timeout period will cause the
    system to reset.

  Precondition:
    WDT must be enabled.

  Parameters:
    None.

  Returns:
    None.

  Example:
    <code>
    //Application

    ${WDT_INSTANCE_NAME}_Initialize();

    ${WDT_INSTANCE_NAME}_Enable();

    // Application Code executes here.
    // Clear the WDT periodically.
    ${WDT_INSTANCE_NAME}_Clear();

    </code>

  Remarks:
    None.
*/

void ${WDT_INSTANCE_NAME}_Clear( void );

<#if WDT_EW_ENABLE = true>
// *****************************************************************************
/* Function:
    void ${WDT_INSTANCE_NAME}_CallbackRegister( WDT_CALLBACK callback,
                                           uintptr_t context )

  Summary:
    Sets the pointer to the function (and it's context) to be called when the
    Early Warning event occurs.

  Description:
    This function sets the pointer to a client function to be called "back" when
    the WDT Early Warning event occurs. It also passes a context value that is
    passed into the callback function when it is called.  This function is
    available only if the Early Warning option (in MHC) is enabled at the time
    of generating the peripheral library.

    The time at which the Early warning interrupt occurs is defined by the Early
    Warning setting in the NVM User row. This is configured by using the
    compiler provided fuse options. Specifying the Early Warning offset to be
    larger than the WDT time out value will cause the Early Warning mechanism to
    be in-active.

  Precondition:
    WDT_Initialize must have been called for the associated WDT instance.
    Reset mode must be disabled in MCC configuration

  Parameters:
    callback - A pointer to a function with a calling signature defined by the
    ${WDT_INSTANCE_NAME}_CALLBACK data type.

    context -  A value (usually a pointer) passed (unused) into the function
    identified by the callback parameter.

  Returns:
    None.

  Example:
    <code>
    ${WDT_INSTANCE_NAME}_CallbackRegister(MyCallback, &myData);
    </code>

  Remarks:
    The context value may be set to NULL if it is not required. Note that the
    value of NULL will still be passed to the callback function.  To disable the
    callback function, pass a NULL for the callback parameter.  See the
    WDT_CALLBACK type definition for additional information.
*/

void ${WDT_INSTANCE_NAME}_CallbackRegister( WDT_CALLBACK callback, uintptr_t context );

// *****************************************************************************
/* Function:
    void ${WDT_INSTANCE_NAME}_InterruptHandler( void )

  Summary:
    WDT Interrupt Handler.

  Description:
    This function handles all the interrupts evoked in the WDT module.

  Precondition:
    WDT must be enabled.

  Parameters:
    None.

  Returns:
    None.

  Example:
    <code>
    //Application

    void ${WDT_INSTANCE_NAME}_InterruptHandler( void )
    {
        // serve interrupts
    }

    </code>
  Remarks:
    None.
*/

void ${WDT_INSTANCE_NAME}_InterruptHandler( void );
</#if>

#endif /* PLIB_${WDT_INSTANCE_NAME}_H */
