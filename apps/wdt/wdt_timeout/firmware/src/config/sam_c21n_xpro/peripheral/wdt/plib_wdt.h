/*******************************************************************************
  Watch Dog Timer PLIB.

  Company:
    Microchip Technology Inc.

  File Name:
    plib_wdt.h

  Summary:
    Interface definition of WDT PLIB.

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

#ifndef PLIB_WDT_H
#define PLIB_WDT_H

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
    void WDT_Initialize( void )

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
    WDT_Initialize();
    </code>

  Remarks:
    The WDT peripheral is also configured by setting in the NVM User Row. These
    settings are specified though compiler provided fuse settings.
*/

void WDT_Initialize( void );

// *****************************************************************************
/* Function:
    void WDT_Enable( void )

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
    WDT_Enable();
    </code>

  Remarks:
    None.
*/

void WDT_Enable( void );

// *****************************************************************************
/* Function:
    void WDT_Disable( void )

  Summary:
    Disables the WDT peripheral.

  Description:
    This function is used to stop the WDT counter and disable WDT peripheral.

  Precondition:
    WDT must be enabled using WDT_Enable().

  Parameters:
    None

  Returns:
    None.

  Example:
    <code>
    WDT_Disable();
    </code>

  Remarks:
    Certain devices does not allow disabling Watchdog timers once enabled.
    This API will not have any effect if ALWAYSON bit in watchdog is enabled.
*/

void WDT_Disable( void );

// *****************************************************************************
/* Function:
    void WDT_Clear( void )

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

    WDT_Initialize();

    WDT_Enable();

    // Application Code executes here.
    // Clear the WDT periodically.
    WDT_Clear();

    </code>

  Remarks:
    None.
*/

void WDT_Clear( void );


#endif /* PLIB_WDT_H */
