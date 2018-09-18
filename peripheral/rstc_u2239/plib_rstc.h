/*******************************************************************************
  Reset Controller(RSTC) Peripheral Library Interface Header File

  Company
    Microchip Technology Inc.

  File Name
    plib_rstc.h

  Summary
    RSTC peripheral library interface.

  Description
    This file defines the interface to the RSTC peripheral library. This
    library provides access to and control of the associated Reset Controller.

  Remarks:
    This header is for documentation only.  The actual plib_rstc headers will be
    generated as required by the MCC.

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

#ifndef PLIB_RSTC_H      // Guards against multiple inclusion
#define PLIB_RSTC_H

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
    /* Power On Reset */
    RSTC_RESET_CAUSE_POR_RESET = RSTC_RCAUSE_POR_Msk,

    /* Brown Out CORE Detector Reset */
    RSTC_RESET_CAUSE_BODCORE_RESET = RSTC_RCAUSE_BODCORE_Msk,

    /* Brown Out VDD Detector Reset */
    RSTC_RESET_CAUSE_BODVDD_RESET = RSTC_RCAUSE_BODVDD_Msk,

    /* External Reset */
    RSTC_RESET_CAUSE_EXT_RESET = RSTC_RCAUSE_EXT_Msk,

    /* Watchdog Reset */
    RSTC_RESET_CAUSE_WDT_RESET = RSTC_RCAUSE_WDT_Msk,

    /* System Reset Request */
    RSTC_RESET_CAUSE_SYST_RESET = RSTC_RCAUSE_SYST_Msk,

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
    RSTC_RESET_CAUSE RSTC_ResetCauseGet (void);

  Summary:
    Reports the cause of the last reset.

  Description:
    This function returns the cause of the last reset. The reset could be due to
    multiple reasons. The application should compare the returned value against
    different values in the RSTC_RESET_CAUSE enumeration to identify the 
    possible causes.

  Precondition:
    None.

  Parameters:
    None.

  Returns:
    RSTC_RESET_CAUSE - Identifies type of reset.

  Example:
    <code>
       if ((RSTC_RESET_CAUSE_WDT_RESET|RSTC_RESET_CAUSE_BODVDD_RESET) == 
            RSTC_ResetCauseGet ())
       {
          //Application related tasks
       }
    </code>

  Remarks:
    None.
*/

RSTC_RESET_CAUSE RSTC_ResetCauseGet (void);

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif

#endif /* PLIB_RSTC_H */
