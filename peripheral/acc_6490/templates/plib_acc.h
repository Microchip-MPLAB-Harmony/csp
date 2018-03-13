/*******************************************************************************
  Analog Comparator Controller(ACC) Peripheral Library Interface Header File

  Company
    Microchip Technology Inc.

  File Name
    acc.h

  Summary
    Data Type definition of the ACC Peripheral Interface Plib.

  Description
    This file defines the Data Types for the ACC Plib.

  Remarks:
    None.
    
*******************************************************************************/
// DOM-IGNORE-BEGIN
/*******************************************************************************
Copyright (c) 2017 released Microchip Technology Inc.  All rights reserved.
Microchip licenses to you the right to use, modify, copy and distribute
Software only when embedded on a Microchip microcontroller or digital signal
controller that is integrated into your product or third-party product
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

#ifndef PLIB_ACC_H    // Guards against multiple inclusion
#define PLIB_ACC_H

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
    interface.
*/

// *****************************************************************************
/* ACC comparison status
   Summary:
    Identifies the ACC Comparison status

   Description:
    This data type identifies the ACC Comparison status

   Remarks:
    Refer to the specific device data sheet to determine availability.
*/
typedef enum
{
    /*ACC Output*/
    ACC_STATUS_SOURCE_COMPARATOR_OUTPUT = ACC_ISR_SCO_Msk,      

    /*ACC Interrupt*/
    ACC_STATUS_SOURCE_COMPARISON_EDGE = ACC_ISR_CE_Msk,

} ACC_STATUS_SOURCE;



typedef void (*ACC_CALLBACK) (uintptr_t context);

// *****************************************************************************
// *****************************************************************************
// Section: Local: **** Do Not Use ****
// *****************************************************************************
// *****************************************************************************

typedef struct
{    
    ACC_CALLBACK callback; 
    uintptr_t    context;
    
} ACC_OBJECT ;

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END
#endif // PLIB_ACC_H
