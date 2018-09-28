/*******************************************************************************
  TC Peripheral Library Interface Header File

  Company
    Microchip Technology Inc.

  File Name
    plib_tc_common.h

  Summary
    TC peripheral library interface.

  Description
    This file defines the interface to the TC peripheral library.  This
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

typedef enum
{
    TC_TIMER_NONE = 0U,
    TC_TIMER_COMPARE_MATCH = TC_SR_CPAS_Msk,
    TC_TIMER_PERIOD_MATCH = TC_SR_CPCS_Msk,
    TC_TIMER_STATUS_MSK = TC_SR_CPAS_Msk | TC_SR_CPCS_Msk
}TC_TIMER_STATUS;

typedef enum
{
    TC_COMPARE_NONE = 0U,
    TC_COMPARE_A = TC_SR_CPAS_Msk,
    TC_COMPARE_B = TC_SR_CPBS_Msk,
    TC_COMPARE_C = TC_SR_CPCS_Msk,
    TC_COMPARE_STATUS_MSK = TC_SR_CPAS_Msk | TC_SR_CPBS_Msk | TC_SR_CPCS_Msk
}TC_COMPARE_STATUS;

typedef enum
{
    TC_CAPTURE_NONE = 0U,
    TC_CAPTURE_COUNTER_OVERFLOW = TC_SR_COVFS_Msk,
    TC_CAPTURE_LOAD_OVERRUN = TC_SR_LOVRS_Msk,
    TC_CAPTURE_A_LOAD = TC_SR_LDRAS_Msk,
    TC_CAPTURE_B_LOAD = TC_SR_LDRBS_Msk,
    TC_CAPTURE_STATUS_MSK = TC_SR_COVFS_Msk | TC_SR_LOVRS_Msk | TC_SR_LDRAS_Msk | TC_SR_LDRBS_Msk
}TC_CAPTURE_STATUS;

typedef enum
{
    TC_QUADRATURE_NONE = 0U,
    TC_QUADRATURE_INDEX = TC_QISR_IDX_Msk,
    TC_QUADRATURE_DIR_CHANGE = TC_QISR_DIRCHG_Msk,
    TC_QUADRATURE_ERROR = TC_QISR_QERR_Msk,
    TC_QUADRATURE_STATUS_MSK = TC_QISR_IDX_Msk | TC_QISR_DIRCHG_Msk | TC_QISR_QERR_Msk
}TC_QUADRATURE_STATUS;

// *****************************************************************************

typedef void (*TC_TIMER_CALLBACK) (TC_TIMER_STATUS status, uintptr_t context);

typedef void (*TC_COMPARE_CALLBACK) (TC_COMPARE_STATUS status, uintptr_t context);

typedef void (*TC_CAPTURE_CALLBACK) (TC_CAPTURE_STATUS status, uintptr_t context);

typedef void (*TC_QUADRATURE_CALLBACK) (TC_QUADRATURE_STATUS status, uintptr_t context);


// *****************************************************************************

typedef struct
{
    TC_TIMER_CALLBACK callback_fn;
    uintptr_t context;
}TC_TIMER_CALLBACK_OBJECT;

typedef struct
{
    TC_COMPARE_CALLBACK callback_fn;
    uintptr_t context;
}TC_COMPARE_CALLBACK_OBJECT;

typedef struct
{
    TC_CAPTURE_CALLBACK callback_fn;
    uintptr_t context;
}TC_CAPTURE_CALLBACK_OBJECT;

typedef struct
{
    TC_QUADRATURE_CALLBACK callback_fn;
    uintptr_t context;
}TC_QUADRATURE_CALLBACK_OBJECT;


// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

}

#endif
// DOM-IGNORE-END

#endif //_PLIB_TC_COMMON_H

/**
 End of File
*/