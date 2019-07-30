/*******************************************************************************
  Interface definition of NMIC PLIB.
 
  Company:
    Microchip Technology Inc.
 
  File Name:
    plib_nmic.h
 
  Summary:
    Interface definition of the Non-Maskable Interrupt Controller (NMIC) Plib.
 
  Description:
    This file defines the interface for the NMIC Plib.
    It allows user to setup alarm and retrieve current date and time.
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
 
#ifndef NMIC_H    // Guards against multiple inclusion
#define NMIC_H
 
// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
 
/*  This section lists the other files that are included in this file.
*/
 
#include <stdint.h>
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
 
// *****************************************************************************
 /* NMIC_INT_SRC

   Summary:
    Defines the data type for the NMIC_INT_SRC Mask.

   Description:
    This is used to set up NMIC interrupt.

   Remarks:
    None.
*/

typedef enum 
{
	NMIC_NMI		= 0x01,      // External NMI
	CPU_FREQ_FAIL	= 0x02,      // Wrong CPU Frequency Monitor Detection
	XTAL_12M_FAIL	= 0x04,      // Fast XTAL Clock Failure Detection
	XTAL_32K_FAIL	= 0x08,	     // Slow XTAL 32KHZ Clock Failure Detection
	VDDIO_FAIL		= 0x10,		 // VDDIO Supply Monitor Failure Detection
	VDDCORE_FAIL	= 0x20       // VDDCORE Brownout Detector Failure Detection
} NMIC_INT_SRC;	
 	
 
// *****************************************************************************
// *****************************************************************************
/* Callback Function Pointer
 Summary:
	Defines the data type and function signature for the NMIC peripheral
	callback function.
 
 Description:
	This data type defines the function signature for the NMIC peripheral
	callback function. The NMIC peripheral will call back the client's
	function with this signature once the interrupt occurs.
 
 Precondition:
	NMIC_CallbackRegister must have been called to set the
	function to be called.
 
 Parameters:
	context - Allows the caller to provide a context value (usually a pointer
	to the callers context for multi-instance clients).
	
	int_cause - Specifies the source that lead to NMI interrupt
 
 Returns:
	None.
*/
typedef void (*NMIC_CALLBACK)(uintptr_t context, uint32_t int_cause);
 
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
    void NMICx_Initialize( void )

   Summary:
     Initializes given instance of the NMIC peripheral.

   Description:
     This function initializes the given instance of the NMIC peripheral as
     configured by the user from within the MCC.  

   Precondition:
     None.

   Parameters:
    None.
  
   Returns:
    None.

   Example:
    <code>
		NMIC0_Initialize();
    </code>

*/

void NMICx_Initialize( void );

// *****************************************************************************  
/* Function:
	void NMICx_CallbackRegister( NMIC_CALLBACK callback, uintptr_t context )
	
 Summary:
	Sets the pointer to the function (and it's context) to be called when the
	Timeout events occur.
	
 Description:
	This function sets the pointer to a client function to be called "back"
	when the interrupt occurs. It also passes a context value that is passed into the
	function when it is called.
	This function is available only in interrupt mode of operation.
	
 Precondition:
	None.
	
 Parameters:
	callback - A pointer to a function with a calling signature defined
				by the NMIC_CALLBACK data type.
	context - A value (usually a pointer) passed (unused) into the function
				identified by the callback parameter.
				
 Returns:
	None.
	
 Example:
	<code>
		NMIC0_CallbackRegister(MyCallback, &myData);
	</code>
	
 Remarks:
	The context value may be set to NULL if it is not required. In this case the
	value NULL will be passed to the callback function.
	To disable the callback function, pass a NULL for the callback parameter.
	See the NMIC_CALLBACK type definition for additional information.
*/
void NMIC_CallbackRegister( NMIC_CALLBACK callback, uintptr_t context );
 
// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility
 }
#endif
// DOM-IGNORE-END
#endif