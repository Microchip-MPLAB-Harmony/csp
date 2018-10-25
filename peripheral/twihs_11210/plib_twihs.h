/*******************************************************************************
  TWIHS Peripheral Library Interface Header File

  Company
    Microchip Technology Inc.

  File Name
    plib_twihs.h

  Summary
    TWIHS peripheral library interface.

  Description
    This file defines the interface to the TWIHS peripheral library.  This
    library provides access to and control of the associated peripheral
    instance.

  Remarks:
    This header is for documentation only.  The actual plib_twihs<x> headers
    will be generated as required by the MCC (where <x> is the peripheral
    instance number).

    Every interface symbol has a lower-case 'x' in it following the "TWIHS"
    abbreviation.  This 'x' will be replaced by the peripheral instance number
    in the generated headers.  These are the actual functions that should be
    used.

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

#ifndef PLIB_TWIHSx_H
#define PLIB_TWIHSx_H

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

// *****************************************************************************
/* TWIHS Error Status

   Summary:
    TWIHS Error Status data type.

   Description:
    This enum defines the list of TWIHS Error Status. Any one error from the list 
    will be returned if the error status is queried.

   Remarks:
    None.
*/

typedef enum
{	
	/* No Error */
    TWIHS_ERROR_NONE,
	
	/* Slave returned Nack */
    TWIHS_ERROR_NACK,
	
} TWIHS_ERROR;

// *****************************************************************************
/* TWIHS Transfer Event Callback Function Pointer.

   Summary:
    Defines the data type and function signature for the TWIHS peripheral
    callback function.

   Description:
    This data type defines the function signature for the TWIHS peripheral
    callback function. The TWIHS peripheral will call back the client's
    function with this signature when the TWIHS Transfer event has occurred.

   Precondition:
    TWIHSx_Initialize must have been called for the given TWIHS peripheral
    instance and TWIHSx_CallbackRegister must have been called to set the
    function to be called.

   Parameters:
    status  - Complete or error status of the TWIHS transfer.

    context - Allows the caller to provide a context value (usually a pointer
    to the callers context for multi-instance clients).

   Returns:
    None.

   Example:
    <code>
    // Data tracking what each of my instances is doing.
    MY_DATA myData[2];

    void MyTWIHSCallback ( uintptr_t context )
    {
        MY_DATA *mePtr = (MY_DATA *)context;

        if(TWIHS_ERROR_NONE == TWIHS1_ErrorGet())
        {
            //Handle complete status here based on context
        }
        else
        {
            //Handle error here
        }
    }

    TWIHS1_CallbackSet(MyTWIHSCallback, &myData[0]);
    TWIHS2_CallbackSet(MyTWIHSCallback, &myData[1]);
    </code>

   Remarks:
    None.
*/
typedef void (*TWIHS_CALLBACK) (uintptr_t contextHandle);

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
    void TWIHSx_Initialize(void)

   Summary:
    Initializes given instance of the TWIHS peripheral.

   Description:
    This function initializes the given instance of the TWIHS peripheral as
    configured by the user from within the MHC.

   Precondition:
    None.

   Parameters:
    None.

   Returns:
    None

   Example:
    <code>
    	TWIHS1_Initialize();
    </code>

   Remarks:
    Stops the TWIHS if it was already running and reinitializes it.
*/

void TWIHSx_Initialize(void);

// *****************************************************************************
/* Function:
    bool TWIHSx_Read(uint16_t address, uint8_t *pdata, size_t length)

   Summary:
    Reads data from the slave.

   Description:
    This function reads the data of size in bytes equal to length into pdata buffer
	from the slave having given address. Master will generate Stop condition after
	completion of the read.

   Precondition:
    TWIHSx_Initialize must have been called for the associated TWIHS instance.

   Parameters:
    address - 7-bit / 10-bit slave address.
	pdata   - pointer to destination data buffer
	length  - length of data buffer in number of bytes.

   Returns:
    true - Read request was submitted successfully.
    
    false - Failed while submitting the read request.

   Example:
    <code>
	    uint8_t myData [NUM_BYTES];

	    if(!TWIHS1_Read( SLAVE_ADDR, &myData[0], NUM_BYTES ))
	    {
		    // error handling
	    }
    </code>

   Remarks:
    None.
*/

bool TWIHSx_Read(uint16_t address, uint8_t *pdata, size_t length);

// *****************************************************************************
/* Function:
    bool TWIHSx_Write(uint16_t address, uint8_t *pdata, size_t length)

   Summary:
    Writes data onto the slave.

   Description:
    This function writes the data from pdata buffer of size in bytes equal to
	length onto the slave with given address. Master will generate Stop
	condition after completion of the write.

   Precondition:
    TWIHSx_Initialize must have been called for the associated TWIHS instance.

   Parameters:
    address - 7-bit / 10-bit slave address.
	pdata   - pointer to source data buffer
	length  - length of data buffer in number of bytes.

   Returns:
    true - Write request was submitted successfully.
    
    false - Failed while submitting the write request.

   Example:
    <code>
	    uint8_t myData [NUM_BYTES] = {'1', '0', ' ', 'B', 'Y', 'T', 'E', 'S', '!', '!',};

	    if(!TWIHS1_Write( SLAVE_ADDR, &myData[0], NUM_BYTES ))
	    {
		    // error handling
	    }
    </code>

   Remarks:
    None.
*/

bool TWIHSx_Write(uint16_t address, uint8_t *pdata, size_t length);

// *****************************************************************************
/* Function:
    bool TWIHSx_WriteRead(uint16_t address, uint8_t *wdata, size_t wlength, uint8_t *rdata, size_t rlength)

   Summary:
    Write and Read data from Slave.

   Description:
    This function writes data from wdata buffer to the slave of given address and
	of size(in bytes) equal to wlength. Master then generates a repeated start and
	do a read operation. Read operation reads data into rdata buffer of size(in
    bytes) equal to rlength from the slave of given address. Master generates a stop
	condition after reading the data.

   Precondition:
    TWIHSx_Initialize must have been called for the associated TWIHS instance.

   Parameters:
    address - 7-bit / 10-bit slave address.
	wdata   - pointer to write data buffer
	wlength - write data length in bytes.
	rdata   - pointer to read data buffer.
	rlength - read data length in bytes.

   Returns:
    true - Write read request was submitted successfully.
    
    false - Failed while submitting the write read request.

   Example:
    <code>
	    uint8_t myTxData [NUM_BYTES] = {'1', '0', ' ', 'B', 'Y', 'T', 'E', 'S', '!', '!'};
		uint8_t myRxData [NUM_BYTES] = {0};

	    if(!TWIHSx_WriteRead( SLAVE_ADDR, &myTxData[0], NUM_BYTES, myRxData, NUM_BYTES ))
	    {
		    // error handling
	    }
    </code>

   Remarks:
    None.
*/

bool TWIHSx_WriteRead(uint16_t address, uint8_t *wdata, size_t wlength, uint8_t *rdata, size_t rlength);

// *****************************************************************************
/* Function:
    bool TWIHSx_IsBusy(void)

   Summary:
    Returns the TWIHS Peripheral busy status.
    
   Description:
    This function returns the TWIHS Peripheral busy status

   Precondition:
    TWIHSx_Initialize must have been called for the associated TWIHS instance.

   Parameters:
    None.

   Returns:
    true - Busy.
    
    false - Not busy.
    
   Example:
    <code>
    if(!TWIHS1_IsBusy())
    {
        // add another transfer request
    }
    </code>
    
   Remarks:
    None.
*/

bool TWIHSx_IsBusy(void);

// *****************************************************************************
/* Function:
    TWIHS_ERROR TWIHSx_ErrorGet(void)
	
   Summary:
    Returns the error during transfer.

   Description:
    This function returns the error during transfer.

   Precondition:
    TWIHSx_Initialize must have been called for the associated TWIHS instance.

   Parameters:
    None.
	
   Returns:
    TWIHS_ERROR_NONE - Transfer was successful.
    
    TWIHS_ERROR_NACK - Slave returned NACK during the transfer.
	
   Example:
    <code>
    if(TWIHS_ERROR_NONE == TWIHS1_ErrorGet())
    {
        //TWIHS transfer is completed, go to next state.
    }
    </code>

   Remarks:
    None.
*/

TWIHS_ERROR TWIHSx_ErrorGet(void);

// *****************************************************************************
/* Function:
    void TWIHSx_CallbackRegister(TWIHS_CALLBACK callback, uintptr_t contextHandle)

   Summary:
    Sets the pointer to the function (and it's context) to be called when the
    given TWIHS's transfer events occur.

   Description:
    This function sets the pointer to a client function to be called "back"
    when the given TWIHS's transfer events occur. It also passes a context value
    (usually a pointer to a context structure) that is passed into the
    function when it is called.

   Precondition:
    TWIHSx_Initialize must have been called for the associated TWIHS instance.

   Parameters:
    callback - A pointer to a function with a calling signature defined
	by the TWIHS_CALLBACK data type.

    context - A value (usually a pointer) passed (unused) into the function
	identified by the callback parameter.

   Returns:
    None.

   Example:
    <code>
    TWIHS1_CallbackRegister(MyTWIHSCallback, &myData);
    </code>

   Remarks:
    The context parameter is ignored if the pointer passed is NULL.
    To disable the callback function, pass a NULL for the callback parameter.
    See the TWIHS_CALLBACK type definition for additional information.
*/

void TWIHSx_CallbackRegister(TWIHS_CALLBACK callback, uintptr_t contextHandle);

// *****************************************************************************
/* Function:
    void TWIHSx_InterruptHandler(void)

   Summary:
    TWIHSx Peripheral Interrupt Handler.

   Description:
    This function is TWIHSx Peripheral Interrupt Handler and will
    called on every TWIHSx interrupt.

   Precondition:
    None.

   Parameters:
    None.

   Returns:
    None.

   Remarks:
    The function is called as peripheral instance's interrupt handler if the
	instance interrupt is enabled. If peripheral instance's interrupt is
	disabled, user need to call it from the main while loop of the application.
*/

void TWIHSx_InterruptHandler(void);

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END

#endif //PLIB_TWIHSx_H

/*******************************************************************************
 End of File
*/
