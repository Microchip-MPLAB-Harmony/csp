/*******************************************************************************
  Power Manager(${PM_INSTANCE_NAME}) PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_${PM_INSTANCE_NAME?lower_case}.h

  Summary
    ${PM_INSTANCE_NAME} PLIB Header File.

  Description
    This file defines the interface to the PM peripheral library. This
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

#ifndef PLIB_${PM_INSTANCE_NAME}_H    // Guards against multiple inclusion
#define PLIB_${PM_INSTANCE_NAME}_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
/* This section lists the other files that are included in this file.
*/

#include <stdbool.h>
#include <stddef.h>

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
/* Standby sleep mode types

  Summary:
    Identifies the possible PM sleep mode types.

  Description:
    This enumeration identifies PM standby and idle sleep modes.

  Remarks:
    None.
*/

typedef enum
{
    /* Idle Sleep Mode */
    PM_SLEEP_MODE_IDLE = 0x2,

    /* Standby Sleep Mode */
    PM_SLEEP_MODE_STANDBY = 0x4

} PM_SLEEP_MODE;

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
    void ${PM_INSTANCE_NAME}_Initialize( void );

  Summary:
    Initializes given instance of PM peripheral.

  Description:
    This function initializes the specified instance of PM peripheral with the
    values configured in MHC GUI.

  Precondition:
    MHC GUI should be configured with the right values.

  Parameters:
    None.

  Returns:
    None.

  Example:
    <code>
      ${PM_INSTANCE_NAME}_Initialize();
    </code>

  Remarks:
    This function should only be called once during system initialization
    before any other PM function is called.
*/

void ${PM_INSTANCE_NAME}_Initialize( void );

// *****************************************************************************
/* Function:
    void ${PM_INSTANCE_NAME}_SleepModeEnter( PM_SLEEP_MODE sleepMode );

  Summary:
    Puts the device into the specified sleep mode.

  Description:
    This function places the device in the specified sleep mode. The sleepMode
    parameter specifies the sleep mode that the device should be placed in. Once
    in sleep mode, the CPU will not execute any instruction unless it it woken
    up by a peripheral that is configured to operate in the specified sleep
    mode.

  Precondition:
    ${PM_INSTANCE_NAME}_Initialize() must have been called first for the associated
    instance.

  Parameters:
    sleepMode - Specifies the sleep mode that the device should be placed in.

  Returns:
    None.

  Example:
    <code>
      PM_SLEEP_MODE sleepMode = PM_SLEEP_MODE_IDLE;

      ${PM_INSTANCE_NAME}_Initialize();
      ${PM_INSTANCE_NAME}_StandbyModeEnter(sleepMode);
    </code>

  Remarks:
    None.
*/

void ${PM_INSTANCE_NAME}_SleepModeEnter( PM_SLEEP_MODE sleepMode );

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END

#endif /* PLIB_${PM_INSTANCE_NAME}_H */
