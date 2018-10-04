/*******************************************************************************
  Power Manager(PM) Peripheral Library Interface Header File

  Company
    Microchip Technology Inc.

  File Name
    plib_pm.h

  Summary
    PM peripheral library interface.

  Description
    This file defines the interface to the PM peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

  Remarks:
    This header is for documentation only. The actual pm<x> headers will be
    generated as required by the MHC (where <x> is the peripheral instance
    number).

    Every interface symbol has a lower-case 'x' in it following the "PM"
    abbreviation. This 'x' will be replaced by the peripheral instance number
    in the generated headers. These are the actual functions that should be
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

#ifndef PLIB_PMx_H       // Guards against multiple inclusion
#define PLIB_PMx_H

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
    void PMx_Initialize( void );

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
      PMx_Initialize();
    </code>

  Remarks:
    This function should only be called once during system initialization
    before any other PM function is called.
*/

void PMx_Initialize( void );

// *****************************************************************************
/* Function:
    void PMx_SleepModeEnter( PM_SLEEP_MODE sleepMode );

  Summary:
    Puts the device into the specified sleep mode.

  Description:
    This function places the device in the specified sleep mode. The sleepMode
    parameter specifies the sleep mode that the device should be placed in. Once
    in sleep mode, the CPU will not execute any instruction unless it it woken
    up by a peripheral that is configured to operate in the specified sleep
    mode.

  Precondition:
    PMx_Initialize() must have been called first for the associated instance.

  Parameters:
    sleepMode - Specifies the sleep mode that the device should be placed in.

  Returns:
    None.

  Example:
    <code>
      PM_SLEEP_MODE sleepMode = PM_SLEEP_MODE_IDLE;

      PMx_Initialize();
      PMx_SleepModeEnter(sleepMode);

    </code>

  Remarks:
    None.
*/

void PMx_SleepModeEnter( PM_SLEEP_MODE sleepMode );

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END

#endif /* PLIB_PMx_H */
