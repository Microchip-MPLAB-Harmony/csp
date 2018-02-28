/*******************************************************************************
  TWI Peripheral Library Interface Header File

  Company
    Microchip Technology Inc.

  File Name
    plib_twi.h

  Summary
    TWI peripheral library interface.

  Description
    This file defines the interface to the TWI peripheral library.  This 
    library provides access to and control of the associated peripheral 
    instance.

  Remarks:
    This header is for documentation only.  The actual plib_twi<x> headers 
    will be generated as required by the MCC (where <x> is the peripheral 
    instance number).

    Every interface symbol has a lower-case 'x' in it following the "TWI" 
    abbreviation.  This 'x' will be replaced by the peripheral instance number
    in the generated headers.  These are the actual functions that should be
    used.
    
*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
Copyright (c) 2018 released Microchip Technology Inc.  All rights reserved.

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

#ifndef PLIB_TWIx_H   
#define PLIB_TWIx_H

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
/* TWI Transfer Events.

   Summary:
    Defines the data type for the TWI Transfer status
	
   Description:
    This enum defines the TWI Transfer status. Any one event from the list will
	be returned if the transfer status is queried or will be available in the
	transfer callback.

   Remarks:
    None.
*/

typedef enum
{	
	/* Peripheral is busy processing the transfer request */
    TWI_TRANSFER_BUSY,
	
	/* Peripheral successfully completed the transfer request */
    TWI_TRANSFER_SUCCESS,
	
	/* Error occured during the transfer request */
    TWI_TRANSFER_ERROR,
	
} TWI_TRANSFER_STATUS;

// *****************************************************************************
/* TWI Transfer Event Callback Function Pointer.

   Summary:
    Defines the data type and function signature for the TWI peripheral 
    callback function.
	
   Description:
    This data type defines the function signature for the TWI peripheral 
    callback function. The TWI peripheral will call back the client's 
    function with this signature when the TWI Transfer event has occurred.

   Precondition:
    TWIx_Initialize must have been called for the given TWI peripheral 
    instance and TWIx_CallbackRegister must have been called to set the 
    function to be called.
	
   Parameters:
    status  - Complete or error status of the TWI transfer.
    
    context - Allows the caller to provide a context value (usually a pointer
    to the callers context for multi-instance clients).
  
   Returns:
    None.

   Example:
    <code>
    // Data tracking what each of my instances is doing.
    MY_DATA myData[2];

    void MyTWICallback ( TWI_TRANSFER_STATUS status, uintptr_t context )
    {
        MY_DATA *mePtr = (MY_DATA *)context;

        if(TWI_TRANSFER_COMPLETE == status)
        {
            //Handle complete status here based on context
        } 
        else
        {
            //Handle error here 
        }
    }

    TWI1_CallbackSet(MyTWICallback, &myData[0]);
    TWI2_CallbackSet(MyTWICallback, &myData[1]);
    </code>
	
   Remarks:
    None.
*/
typedef void (*TWI_CALLBACK) 
( 
    /* Transfer event */
    TWI_TRANSFER_STATUS  status,   
  
    /* Transfer context */
    uintptr_t contextHandle 
);

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
    void TWIx_Initialize(void)

   Summary:
    Initializes given instance of the TWI peripheral.
	
   Description:
    This function initializes the given instance of the TWI peripheral as
    configured by the user from within the MCC.

   Precondition:
    None.
	
   Parameters:
    None.
	
   Returns:
    None

   Example:
    <code>
    TWI1_Initialize();
    </code>

   Remarks:
    Stops the TWI if it was already running and reinitializes it.
*/

void TWIx_Initialize(void);

// *****************************************************************************
/* Function:
    bool TWIx_TRBBuildRead(uint16_t address, uint8_t *pdata, uint8_t length)
	
   Summary:
    Allocates and Builds the Read Transaction Request Block.

   Description:
    This function allocates and builds the Read Transaction Block.

   Precondition:
    TWIx_Initialize must have been called for the associated TWI instance.
	The transfer status should not be busy.

   Parameters:
    address - 7-bit / 10-bit slave address.
	pdata   - pointer to destination data buffer
	length  - length of data buffer in number of bytes.
  
   Returns:
    true  - TRB submitted Successfully.
	false - Failure while submitting TRB.

   Example:
    <code>
	    uint8_t myData [NUM_BYTES];
	  
	    if(!TWIx_TRBBuildRead( SLAVE_ADDR, &myData[0], NUM_BYTES ))
	    {
		    // error handling
	    }
	  
	    if(!TWIx_TRBTransfer())
	    {
		    // error handling  
	    }
    
    </code>

   Remarks:
    Number of times TWIx_TRBBuildRead is called is limited to number of TRB's
	available.
*/

bool TWIx_TRBBuildRead(uint16_t address, uint8_t *pdata, uint8_t length);

// *****************************************************************************
/* Function:
    bool TWIx_TRBBuildWrite(uint16_t address, uint8_t *pdata, uint8_t length)
	
   Summary:
    Allocates and Builds the Read Transaction Request Block.
	
   Description:
    This function allocates and builds the Read Transaction Block.

   Precondition:
    TWIx_Initialize must have been called for the associated TWI instance.
	The transfer status should not be busy.

   Parameters:
    address - 7-bit / 10-bit slave address.
	pdata   - pointer to source data buffer
	length  - length of data buffer in number of bytes.
  
   Returns:
    true  - TRB submitted Successfully.
	false - Failure while submitting TRB.
	
   Example:
    <code>
	    uint8_t myData [NUM_BYTES] = {'1', '0', ' ', 'B', 'Y', 'T', 'E', 'S', '!', '!',};
	  
	    if(!TWIx_TRBBuildWrite( SLAVE_ADDR, &myData[0], NUM_BYTES ))
	    {
		    // error handling
	    }
	  
	    if(!TWIx_TRBTransfer())
	    {
		    // error handling  
	    }
    
    </code>

   Remarks:
    Number of times TWIx_TRBBuildWrite is called is limited to number of TRB's
	available.
*/

bool TWIx_TRBBuildWrite(uint16_t address, uint8_t *pdata, uint8_t length);

// *****************************************************************************
/* Function:
    bool TWIx_TRBTransfer(void)
	
   Summary:
    Submits all TRB's build for processing. 

   Description:
    This function submits all TRB's built by calling TWIx_TRBBuildRead and 
	TWIx_TRBBuildWrite. Once all TRB's are submitted for processing, transfer
	starts. A repeated start will occur on completion of a single TRB. Master 
	will generate Stop only after it process all TRB's.
	
   Precondition:
    TWIx_Initialize must have been called for the associated TWI instance.
	The transfer status should not be busy before calling TWIx_TRBTransfer.

   Parameters:
    None.
  
   Returns:
    true  - TRB submitted Successfully.
	false - Failure while submitting TRB.

   Example:
	<code>
	    uint8_t myTxData [NUM_BYTES] = {'1', '0', ' ', 'B', 'Y', 'T', 'E', 'S', '!', '!'};
		uint8_t myRxData [NUM_BYTES] = {0};
	  
	    if(!TWIx_TRBBuildWrite( SLAVE_ADDR, &myTxData[0], NUM_BYTES ))
	    {
		    // error handling
	    }
		
		if(!TWIx_TRBBuildRead( SLAVE_ADDR, &myRxData[0], NUM_BYTES ))
	    {
		    // error handling
	    }
	  
	    if(!TWIx_TRBTransfer())
	    {
		    // error handling  
	    }
    
    </code>

   Remarks:
    None.
*/

bool TWIx_TRBTransfer(void);

// *****************************************************************************
/* Function:
    bool TWIx_Read(uint16_t address, uint8_t *pdata, uint8_t length)
	
   Summary:
    Reads data from the slave.

   Description:
    This function reads the data of size in bytes equal to length into pdata buffer 
	from the slave having given address. Master will generate Stop condition after 
	completion of the read.

   Precondition:
    TWIx_Initialize must have been called for the associated TWI instance.
	The transfer status should not be busy before calling TWIx_TRBTransfer.
	Minimum one TRB should be available.

   Parameters:
    address - 7-bit / 10-bit slave address.
	pdata   - pointer to destination data buffer
	length  - length of data buffer in number of bytes.
  
   Returns:
    true  - TRB submitted Successfully.
	false - Failure while submitting TRB.

   Example:
    <code>
	    uint8_t myData [NUM_BYTES];
	  
	    if(!TWIx_Read( SLAVE_ADDR, &myData[0], NUM_BYTES ))
	    {
		    // error handling
	    }
    </code>

   Remarks:
    None.
*/

bool TWIx_Read(uint16_t address, uint8_t *pdata, uint8_t length);

// *****************************************************************************
/* Function:
    bool TWIx_Write(uint16_t address, uint8_t *pdata, uint8_t length)
	
   Summary:
    Writes data onto the slave.

   Description:
    This function writes the data from pdata buffer of size in bytes equal to 
	length onto the slave with given address. Master will generate Stop 
	condition after completion of the write.

   Precondition:
    TWIx_Initialize must have been called for the associated TWI instance.
	The transfer status should not be busy before calling TWIx_TRBTransfer.
	Minimum one TRB should be available.

   Parameters:
    address - 7-bit / 10-bit slave address.
	pdata   - pointer to source data buffer
	length  - length of data buffer in number of bytes.
	
   Returns:
    true  - TRB submitted Successfully.
	false - Failure while submitting TRB.

   Example:
    <code>
	    uint8_t myData [NUM_BYTES] = {'1', '0', ' ', 'B', 'Y', 'T', 'E', 'S', '!', '!',};
	  
	    if(!TWIx_Write( SLAVE_ADDR, &myData[0], NUM_BYTES ))
	    {
		    // error handling
	    }
    </code>

   Remarks:
    None.
*/

bool TWIx_Write(uint16_t address, uint8_t *pdata, uint8_t length);

// *****************************************************************************
/* Function:
    bool TWIx_WriteRead(uint16_t address, uint8_t *wdata, uint8_t wlength, uint8_t *rdata, uint8_t rlength)
	
   Summary:
    Write and Read data from Slave.

   Description:
    This function writes data from wdata buffer to the slave of given address and
	of size(in bytes) equal to wlength. Master then generates a repeated start and
	do a read operation. Read operation reads data into rdata buffer of size(in
    bytes) equal to rlength from the slave of given address. Master generates a stop
	condition after reading the data.

   Precondition:
    TWIx_Initialize must have been called for the associated TWI instance.
	The transfer status should not be busy before calling TWIx_TRBTransfer.
	Minimum two TRB's should be available.

   Parameters:
    address - 7-bit / 10-bit slave address.
	wdata   - pointer to write data buffer
	wlength - write data length in bytes.
	rdata   - pointer to read data buffer.
	rlength - read data length in bytes.
  
   Returns:
    true  - TRB submitted Successfully.
	false - Failure while submitting TRB.

   Example:
    <code>
	    uint8_t myTxData [NUM_BYTES] = {'1', '0', ' ', 'B', 'Y', 'T', 'E', 'S', '!', '!'};
		uint8_t myRxData [NUM_BYTES] = {0};
	  
	    if(!TWIx_WriteRead( SLAVE_ADDR, &myTxData[0], NUM_BYTES, myRxData, NUM_BYTES ))
	    {
		    // error handling
	    }
    </code>

   Remarks:
*/

bool TWIx_WriteRead(uint16_t address, uint8_t *wdata, uint8_t wlength, uint8_t *rdata, uint8_t rlength);

// *****************************************************************************
/* Function:
    TWI_TRANSFER_STATUS TWIx_TransferStatusGet(void)
	
   Summary:
    Returns the transfer status associated with the given TWI peripheral instance.

   Description:
    This function returns the complete or error transfer status associated with 
    the given TWI peripheral instance.

   Precondition:
    TWIx_Initialize must have been called for the associated TWI instance.

   Parameters:
    None.
	
   Returns:
    Status of the transfer.
	
   Example:
    <code>
    if(TWI_TRANSFER_COMPLETE == TWI1_TransferStatusGet())
    {
        //TWI transfer is completed, go to next state.
    }
    </code>

   Remarks:
    None.
*/

TWI_TRANSFER_STATUS TWIx_TransferStatusGet(void);

// *****************************************************************************
/* Function:
    void TWIx_CallbackRegister(TWI_CALLBACK callback, uintptr_t contextHandle)
	
   Summary:
    Sets the pointer to the function (and it's context) to be called when the 
    given TWI's transfer events occur.

   Description:
    This function sets the pointer to a client function to be called "back" 
    when the given TWI's transfer events occur. It also passes a context value 
    (usually a pointer to a context structure) that is passed into the
    function when it is called.

   Precondition:
    TWIx_Initialize must have been called for the associated TWI instance.

   Parameters:
    callback - A pointer to a function with a calling signature defined 
	by the TWI_CALLBACK data type.

    context - A value (usually a pointer) passed (unused) into the function 
	identified by the callback parameter.
  
   Returns:
    None.

   Example:
    <code>
    TWI1_CallbackRegister(MyTWICallback, &myData);
    </code>

   Remarks:
    The context parameter is ignored if the pointer passed is NULL.
    To disable the callback function, pass a NULL for the callback parameter.
    See the TWI_CALLBACK type definition for additional information.
*/

void TWIx_CallbackRegister(TWI_CALLBACK callback, uintptr_t contextHandle);

// *****************************************************************************
/* Function:
    void TWIx_InterruptHandler(void)

   Summary:
    TWIx Peripheral Interrupt Handler.

   Description:
    This function is TWIx Peripheral Interrupt Handler and will
    called on every TWIx interrupt.

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

void TWIx_InterruptHandler(void);

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END

#endif //PLIB_TWIx_H

/*******************************************************************************
 End of File
*/
