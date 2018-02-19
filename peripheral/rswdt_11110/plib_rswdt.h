/*******************************************************************************
Interface definition of RSWDT PLIB.

 Company:
	Microchip Technology Inc.

 File Name:
	plib_rswdt.h

 Summary:
	Interface definition of the Watch Dog Timer Plib (RSWDT).

 Description:
	This file defines the interface for the RSWDT Plib.
	It allows user to setup timeout duration and restart watch dog timer.
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

#ifndef _RSWDT_H // Guards against multiple inclusion
#define _RSWDT_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

/* This section lists the other files that are included in this file.
*/

#include <xc.h>
#include <stdint.h>
#include <stdbool.h>
#include <stddef.h>
#include <sys/attribs.h>

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
/* RSWDT Mode

 Summary:
	Defines the data type for the RSWDT Modes.

 Description:
	This may be used to initialize the RSWDT in window or normal mode.

 Remarks:
	None.
*/

typedef enum
{
	/*Normal Mode of Operation*/
	RSWDT_MODE_NORMAL,

	/*Window mode of operation*/
	RSWDT_MODE_WINDOW
} RSWDT_MODE;

// *****************************************************************************
// *****************************************************************************
/* Callback Function Pointer
 Summary:
	Defines the data type and function signature for the RSWDT peripheral
	callback function.
 Description:
	This data type defines the function signature for the RSWDT peripheral
	callback function. The RSWDT peripheral will call back the client's
	function with this signature when the Timeout event has occurred.
	This feature may or may not be available based on device.
 Precondition:
	RSWDT_Initialize must have been called for the given RSWDT peripheral
	instance and RSWDT_CallbackRegister must have been called to set the
	function to be called.
 Parameters:

	context - Allows the caller to provide a context value (usually a pointer
	to the callers context for multi-instance clients).

 Returns:
	None.
*/
typedef void (*RSWDT_CALLBACK)(uintptr_t context);

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
	void RSWDT_Initialize( void )
	
 Summary:
	Initializes given instance of the RSWDT peripheral.
	
 Description:
	This function initializes the given instance of the RSWDT peripheral as
	configured by the user.
	
 Precondition:
	None.

 Parameters:
	None.

 Returns:
	None.
 Example:
	<code>
		RSWDT_Initialize();
	</code>
*/
void RSWDT_Initialize( void );

// *****************************************************************************
/* Function:
	void RSWDT_Enable( bool windowmode )
	
 Summary:
	Enables the RSWDT peripheral with/without Windowmode.
	
 Description:
	This function Enables the RSWDT peripheral.
	
 Precondition:
	None.
	
 Parameters:
 None.

 Returns:
	None.
	
 Example:
	<code>
		bool windowModeEnable = true;

		RSWDT_Enable(windowModeEnable);
	</code>
 Remarks:
	Certain devices does not allow disabling Watchdog timers.
*/

// *****************************************************************************
void RSWDT_Enable( RSWDT_MODE mode );

/* Function:
	void RSWDT_Disable( void )
 Summary:
	Disables the RSWDT peripheral.
	
 Description:
	This function is used to stop the RSWDT counter and disable RSWDT peripheral.
	
 Precondition:
	None
	
 Parameters:
	None

 Returns:
	None.
	
 Example:
	<code>
		RSWDT_Disable();
	</code>

 Remarks:
	Certain devices does not allow disabling Watchdog timers once enabled.
*/
void RSWDT_Disable( void );

// *****************************************************************************
/* Function:
	void RSWDT_Clear( void )
 Summary:
	Restart the RSWDT counter.
 Description:
	This function is used to restart the RSWDT counter to avoid timeout reset/interrupt.
 Precondition:
	None
 Parameters:
	None.

 Returns:
	None.
 Example:
	<code>
		//Application loop
		while(1)
		{
			RSWDT_Clear();
			//user code
		}
	</code>
*/

void RSWDT_Clear( void );

// *****************************************************************************
/* Function:
	void RSWDT_CallbackRegister( RSWDT_CALLBACK callback, uintptr_t context )
	
 Summary:
	Sets the pointer to the function (and it's context) to be called when the
	Timeout events occur.
 Description:
	This function sets the pointer to a client function to be called "back"
	when the Timeout event occurs. It also passes a context value that is passed into the
	function when it is called.
	This function is available only in interrupt mode of operation.
 Precondition:
	RSWDT_Initialize must have been called for the associated RSWDT instance.
	Reset mode must be disabled in MCC configuration
 Parameters:
	callback - A pointer to a function with a calling signature defined
				by the RSWDT_CALLBACK data type.
	context - A value (usually a pointer) passed (unused) into the function
				identified by the callback parameter.
				
 Returns:
	None.

 Example:
	<code>
		RSWDT_CallbackRegister(MyCallback, &myData);
	</code>
 Remarks:
	The context value may be set to NULL if it is not required. Note that the
	value of NULL will still be passed to the callback function.
	To disable the callback function, pass a NULL for the callback parameter.
	See the RSWDT_CALLBACK type definition for additional information.
	This feature may or may not be available based on device.
*/
void RSWDT_CallbackRegister( RSWDT_CALLBACK callback, uintptr_t context );

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility
}
#endif
// DOM-IGNORE-END
#endif