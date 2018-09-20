/*******************************************************************************
  Timer/Counter(TC) Peripheral Library Interface Header File

  Company
    Microchip Technology Inc.

  File Name
    plib_tc_common.h

  Summary
    TC peripheral library interface.

  Description
    This file defines the interface to the TC peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
Copyright (c) 2017 released Microchip Technology Inc.  All rights reserved.

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

#ifndef PLIB_TC_COMMON_H    // Guards against multiple inclusion
#define PLIB_TC_COMMON_H

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

typedef enum
{
    /* Capture status overflow */
    TC_CAPTURE_STATUS_OVERFLOW = 0x1,

    /* Capture status error */
    TC_CAPTURE_STATUS_ERROR = 0x2,

    /* Capture status ready for channel 0 */
    TC_CAPTURE_STAUTS_CAPTURE0_READY = 0x10,

    /* Capture status ready for channel 1 */
    TC_CAPTURE_STATUS_CAPTURE1_READY = 0x20,
    
    TC_CAPTURE_STATUS_MSK = TC_CAPTURE_STATUS_OVERFLOW | TC_CAPTURE_STATUS_ERROR | TC_CAPTURE_STAUTS_CAPTURE0_READY | TC_CAPTURE_STATUS_CAPTURE1_READY

} TC_CAPTURE_STATUS;



// *****************************************************************************


typedef void (*TC_CALLBACK)( uintptr_t context );

// *****************************************************************************
typedef struct
{
    TC_CALLBACK callback;

    uintptr_t context;

} TC_CALLBACK_OBJ;


// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END

#endif /* PLIB_TC_COMMON_H */
