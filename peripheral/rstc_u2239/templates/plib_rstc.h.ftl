/*******************************************************************************
  Reset Controller(${RSTC_INSTANCE_NAME}) PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_${RSTC_INSTANCE_NAME?lower_case}.h

  Summary
    ${RSTC_INSTANCE_NAME} PLIB Header File.

  Description
    This file defines the interface to the RSTC peripheral library.
    This library provides access to and control of the associated
    Reset Controller.

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

#ifndef PLIB_${RSTC_INSTANCE_NAME}_H      // Guards against multiple inclusion
#define PLIB_${RSTC_INSTANCE_NAME}_H

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
/* User Reset type

  Summary:
    Identifies the type of reset.

  Description:
    This enums identifies either General, Backup, Watchdog, Software
    or User Reset.

  Remarks:
    Refer to the specific device data sheet to determine availability.
*/

typedef enum
{

<#list 0..(RSTC_RCAUSE_LENGTH - 1) as i>
    <#assign resetReason = "RSTC_RCAUSE" + i>
    RSTC_RESET_CAUSE_${.vars[resetReason]}_RESET = RSTC_RCAUSE_${.vars[resetReason]}_Msk,

</#list>
} RSTC_RESET_CAUSE;

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
    RSTC_RESET_CAUSE ${RSTC_INSTANCE_NAME}_ResetCauseGet( void );

  Summary:
    Reports the cause of the last reset.

  Description:
    This function returns the cause of the last reset. The reset could be due to
    multiple reasons. The application should compare the returned value against
    different values in the RSTC_RESET_CAUSE enumeration to identify the possible
    causes.

  Precondition:
    None.

  Parameters:
    None.

  Returns:
    RSTC_RESET_CAUSE - Identifies type of reset.

  Example:
   <code>

    RSTC_RESET_CAUSE resetCause = RSTC_RESET_CAUSE_WDT_RESET | 
                                  RSTC_RESET_CAUSE_BODVDD_RESET;

    if (resetCause == ${RSTC_INSTANCE_NAME}_ResetCauseGet())
    {
        //Application related tasks
    }
    </code>

  Remarks:
    None.
*/

RSTC_RESET_CAUSE ${RSTC_INSTANCE_NAME}_ResetCauseGet (void);

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif

#endif /* PLIB_${RSTC_INSTANCE_NAME}_H */
