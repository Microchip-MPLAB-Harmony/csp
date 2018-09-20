/*******************************************************************************
  PWM Peripheral Library Interface Header File

  Company
    Microchip Technology Inc.

  File Name
    plib_pwm_common.h

  Summary
    PWM peripheral library interface.

  Description
    This file defines the interface to the PWM peripheral library.  This
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

#ifndef PLIB_PWM_COMMON_H    // Guards against multiple inclusion
#define PLIB_PWM_COMMON_H


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


typedef void (*PWM_CALLBACK)( uintptr_t context );
// *****************************************************************************

typedef enum
{
    PWM_CHANNEL_0,
    PWM_CHANNEL_1,
    PWM_CHANNEL_2,
    PWM_CHANNEL_3
}PWM_CHANNEL_NUM;
// *****************************************************************************

typedef enum
{
    PWM_CHANNEL_0_MASK = (1U << 0U),
    PWM_CHANNEL_1_MASK = (1U << 1U),
    PWM_CHANNEL_2_MASK = (1U << 2U),
    PWM_CHANNEL_3_MASK = (1U << 3U)
}PWM_CHANNEL_MASK;

// *****************************************************************************

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

typedef struct
{
    PWM_CALLBACK callback_fn;
    uintptr_t context;
}PWM_CALLBACK_OBJECT;


// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

}

#endif
// DOM-IGNORE-END

#endif //PLIB_PWM_COMMON_H

/**
 End of File
*/
