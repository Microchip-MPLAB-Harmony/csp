/*******************************************************************************
  Supply Controller(SUPC${SUPC_INDEX}) PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_supc${SUPC_INDEX}.h

  Summary
    SUPC${SUPC_INDEX} Header File.

  Description
    This file defines the interface to the SUPC peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

  Remarks:
    None.

*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
Copyright (c) 2017 released Microchip Technology Inc. All rights reserved.
Microchip licenses to you the right to use, modify, copy and distribute
Software only when embedded on a Microchip microcontroller or digital signal
controller that is integrated into your product or third party product
(pursuant to the sublicense terms in the accompanying license agreement).

You should refer to the license agreement accompanying this Software for
additional information regarding your rights and obligations.

SOFTWARE AND DOCUMENTATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND,
EITHER EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION, ANY WARRANTY OF
MERCHANTABILITY, TITLE, NON-INFRINGEMENT AND FITNESS FOR A PARTICULAR PURPOSE.
IN NO EVENT SHALL MICROCHIP OR ITS LICENSORS BE LIABLE OR OBLIGATED UNDER
CONTRACT, NEGLIGENCE, STRICT LIABILITY, CONTRIBUTION, BREACH OF WARRANTY, OR
OTHER LEGAL EQUITABLE THEORY ANY DIRECT OR INDIRECT DAMAGES OR EXPENSES
INCLUDING BUT NOT LIMITED TO ANY INCIDENTAL, SPECIAL, INDIRECT, PUNITIVE OR
CONSEQUENTIAL DAMAGES, LOST PROFITS OR LOST DATA, COST OF PROCUREMENT OF
SUBSTITUTE GOODS, TECHNOLOGY, SERVICES, OR ANY CLAIMS BY THIRD PARTIES
(INCLUDING BUT NOT LIMITED TO ANY DEFENSE THEREOF), OR OTHER SIMILAR COSTS.
*******************************************************************************/
// DOM-IGNORE-END

#ifndef PLIB_SUPC${SUPC_INDEX}_H    // Guards against multiple inclusion
#define PLIB_SUPC${SUPC_INDEX}_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
/* This section lists the other files that are included in this file.
*/

#include <stddef.h>
#include <stdbool.h>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility

    extern "C" {

#endif
// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Section: Data Types
// *****************************************************************************
// *****************************************************************************
/* The following data type definitions are used by the functions in this
    interface and should be considered part it.
*/

// *****************************************************************************
/* Callback function structure

  Summary:
    Defines the data type and function signature for the SUPC peripheral
    callback function.

  Description:
    This data type defines the function signature for the SUPC peripheral
    callback function. The SUPC peripheral will call back the client's function
    with this signature when a Brown Out event has been detected. This function
    will be called only if the BODVDD action in the NVM user row is set to
    interrupt.

  Function:
    void (*SUPC_BODVDD_CALLBACK)( uintptr_t context )

  Precondition:
    SUPC${SUPC_INDEX}_Initialize() must have been called for the given supc
    peripheral instance and SUPC${SUPC_INDEX}_BODVDDCallbackRegister() must have
    been called to set the function to be called.

  Parameters:
    context - Allows the caller to provide a context value (usually a pointer to
    the callers context for multi-instance clients).

  Returns:
    None.

  Example:
    <code>
      void APP_BrownOutEventHandler( uintptr_t context )
      {
           // do something
      }

      SUPC${SUPC_INDEX}_BODVDDCallbackRegister(APP_BrownOutEventHandler, 0);
    </code>

  Remarks:
    None.
*/

typedef void (*SUPC_BODVDD_CALLBACK)( uintptr_t context );

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
    void SUPC${SUPC_INDEX}_Initialize( void );

  Summary:
    Initializes given instance of SUPC peripheral.

  Description:
    This function initializes given instance of SUPC peripheral of the device
    with the values configured in MHC GUI.

  Precondition:
    MHC GUI should be configured with the right values.

  Parameters:
    None.

  Returns:
    None.

  Example:
    <code>
      SUPC${SUPC_INDEX}_Initialize();
    </code>

  Remarks:
    This function should only be called once during system initialization
    before any other SUPC function is called.
*/

void SUPC${SUPC_INDEX}_Initialize( void );

// *****************************************************************************
/* Function:
    void SUPC${SUPC_INDEX}_VoltageRegulatorEnable( bool enable );

  Summary:
    Enable/Disable voltage regulator.

  Description:
    This function will enable or disable the main voltage regulator.

  Precondition:
    SUPC${SUPC_INDEX}_Initialize() must have been called first for the
    associated instance.

  Parameters:
    enable - if true, enable voltage regulator. If false, disable voltage
    regulator.

  Returns:
    None.

  Example:
    <code>
      bool enable = true;
      SUPC${SUPC_INDEX}_Initialize();
      SUPC${SUPC_INDEX}_VoltageRegulatorEnable(enable);
    </code>

  Remarks:
    This function should only be called once during system initialization
    before any other SUPC function is called.
*/

void SUPC${SUPC_INDEX}_VoltageRegulatorEnable( bool enable );

// *****************************************************************************
/* Function:
    void SUPC${SUPC_INDEX}_BODVDDCallbackRegister( SUPC_BODVDD_CALLBACK callback,
                                                    uintptr_t context );

  Summary:
    Registers the function to be called when a Brown Out Event has occurred.

  Description
    This function registers the callback function to be called when a Brown Out
    event has occurred. Note that the callback function will be called only if
    the BODVDD action setting in NVM User Row is configured to generate an
    interrupt and not reset the system.

  Precondition:
    SUPC${SUPC_INDEX}_Initialize() must have been called first for the
    associated instance.

  Parameters:
    callback - callback function pointer.

    context  - Allows the caller to provide a context value (usually a pointer
    to the callers context for multi-instance clients).

  Returns:
    None.

  Example:
    <code>
      void SUPC_Callback_Fn( uintptr_t context )
      {
          // do something
      }

      SUPC${SUPC_INDEX}_Initialize();
      SUPC${SUPC_INDEX}_BODVDDCallbackRegister(SUPC_Callback_Fn, NULL);
    </code>

  Remarks:
    Context value can be set to NULL is not required.  To disable callback
    function, pass NULL for the callback parameter
*/

void SUPC${SUPC_INDEX}_BODVDDCallbackRegister( SUPC_BODVDD_CALLBACK callback, uintptr_t context );

// *****************************************************************************
/* Function:
    void SUPC${SUPC_INDEX}_InterruptHandler( void );

  Summary:
    SUPC interrupt handler for BODVDD event action.

  Description
    This function will trigger BODVDD callback.

  Precondition:
    SUPC${SUPC_INDEX}_Initialize() must have been called first.

  Parameters:
    None.

  Returns:
    None.

  Example:
    <code>
    </code>

  Remarks:
    This will be get called from device vector.So don't call this function
    explicitly.
*/

void SUPC${SUPC_INDEX}_InterruptHandler( void );

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END

#endif /* PLIB_SUPC${SUPC_INDEX}_H */
