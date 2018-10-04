/*******************************************************************************
 Interface definition of TRNG PLIB.
 
 Company:
	Microchip Technology Inc.
	
 File Name:
	plib_trng.h
	
 Summary:
	Interface definition of the True Random Number Generator Plib (TRNG).
	
 Description:
	This file defines the interface for the True Random Number Generator (TRNG)
	Plib.
	It allows user to generate random numbers.
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

#ifndef TRNG_H // Guards against multiple inclusion
#define TRNG_H

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
/* Callback Function Pointer
 Summary:
	Defines the data type and function signature for the TRNG peripheral
	callback function.
	
 Description:
	This data type defines the function signature for the TRNG peripheral
	callback function. The TRNG peripheral will call back the client's
	function with this signature when the random data is ready to be read.
	
 Precondition:
	TRNGx_CallbackRegister must have been called to set the
	function to be called.
	
 Parameters:
	context - Allows the caller to provide a context value (usually a pointer
				to the callers context for multi-instance clients).
	random - The generated 32-bit random number that will be passed via callback.
	
 Returns:
	None.
*/

typedef void (*TRNG_CALLBACK)( uint32_t random, uintptr_t context);

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
	void TRNGx_RandomNumberGenerate( void )
	
 Summary:
	Initiates generation of random number using the TRNG peripheral.
	
 Description:
	This function triggers the TRNG peripheral to generate a 32-bit random number.
	The API will return in case of interrupt mode and wait for random number generation to complete
	in case of polled mode.
	
 Precondition:
	None.
	
 Parameters:
	None.
	
 Returns:
	None.
	
 Example:
	<code>
		TRNG0_RandomNumberGenerate();
	</code>
 Remarks:
	This API should be used when the library is configured in interrupt mode.
*/

void TRNGx_RandomNumberGenerate( void );

// *****************************************************************************
/* Function:
	uint32_t TRNGx_ReadData( void )
	
 Summary:
	Generates and return a 32-bit random number 
	
 Description:
	This function returns a 32-bit random integer.
	
 Precondition:
	None
	
 Parameters:
	None.
	
 Returns:
	uint32_t:- 32-bit true random number
	
 Example:
	<code>
		uint32_t data = TRNG0_ReadData();
	</code>
	
 Remarks:
	This API is required when the library is configured as blocking.
	In non-blocking mode the random number will be passed via callback.
*/

uint32_t TRNGx_ReadData( void );

// *****************************************************************************
/* Function:
	void TRNGx_CallbackRegister( TRNG_CALLBACK callback, uintptr_t context )
	
 Summary:
	Sets the pointer to the function (and it's context) to be called when the
	random number is ready to be read.
	
 Description:
	This function sets the pointer to a client function to be called "back"
	when the random number is ready. It also accepts a context value that is passed into the
	function when it is called.
	This function is available only in interrupt mode of operation.
	
 Precondition:
	None.
	
 Parameters:
	callback - A pointer to a function with a calling signature defined
	by the TRNG_CALLBACK data type.
	context - A value (usually a pointer) passed (unused) into the function
	identified by the callback parameter.
	
 Returns:
	None.
	
 Example:
	<code>
		uint32_t randomValue;
		void testCallback( uintptr_t context, uint32_t random)
		{
			randomValue= random;
		}
		TRNG0_CallbackRegister(testCallback, NULL);
	</code>
	
 Remarks:
	The context value may be set to NULL if it is not required. In this case the value
	NULL will be passed to the callback function.
	To disable the callback function, pass a NULL for the callback parameter.
	See the TRNG_CALLBACK type definition for additional information.
*/

void TRNGx_CallbackRegister( TRNG_CALLBACK callback, uintptr_t context );

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility
	}
#endif
// DOM-IGNORE-END
#endif