/*******************************************************************************
  Analog Comparator Controller(ACC) Peripheral Library Interface Header File

  Company
    Microchip Technology Inc.

  File Name
    plib_acc_common.h

  Summary
    Data Type definition of the ACC Peripheral Interface Plib.

  Description
    This file defines the Data Types for the ACC Plib.

  Remarks:
    None.
    
*******************************************************************************/
// DOM-IGNORE-BEGIN
/*******************************************************************************
* © 2018 Microchip Technology Inc. and its subsidiaries.
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

#ifndef PLIB_ACC_COMMON_H    // Guards against multiple inclusion
#define PLIB_ACC_COMMON_H

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
#endif // PLIB_ACC_COMMON_H
