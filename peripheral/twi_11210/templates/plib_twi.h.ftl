/*******************************************************************************
  TWI Peripheral Library Interface Header File

  Company
    Microchip Technology Inc.

  File Name
    twi.h

  Summary
    TWI peripheral library interface.

  Description
    This file defines the interface to the TWI peripheral library.  This 
    library provides access to and control of the associated peripheral 
    instance.

  Remarks:
    
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

#ifndef PLIB_TWI${INDEX?string}_H   
#define PLIB_TWI${INDEX?string}_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

/*  This section lists the other files that are included in this file.
*/
#include "plib_twi_master.h"

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
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************
/* The following functions make up the methods (set of possible operations) of 
   this interface.
*/

// *****************************************************************************
/* Function:
    void TWI${INDEX?string}_Initialize(void)

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

void TWI${INDEX?string}_Initialize(void);

// *****************************************************************************
/* Function:
    void TWI${INDEX?string}_TransferSetup(TWI_TRANSFER_SETUP * setup, uint32_t twiClockSrcFreq)

   Summary:
    Dynamic setup of TWI Peripheral.

   Precondition:
    TWI${INDEX?string}_Initialize must have been called for the associated TWI instance.
	The transfer status should not be busy.
	
   Parameters:
    setup - Pointer to the structure containing the transfer setup.
    twiClockSrcFreq - TWI Peripheral Clock Source Frequency.
	
   Returns:
    true - Transfer setup was updated Successfully.
    false - Failure while updating transfer setup.
    
   Example:
    <code>
    TWI_TRANSFER_SETUP setup = { 400000 };
    
    TWI1_TransferSetup( &setup, 0 );
    </code>

   Remarks:
    twiClockSrcFreq overrides any change in the peripheral clock frequency. 
    If configured to zero PLib takes the peripheral clock frequency from MHC.
*/

bool TWI${INDEX?string}_TransferSetup( TWI_TRANSFER_SETUP *setup, uint32_t twiClockSrcFreq );

// *****************************************************************************
/* Function:
    bool TWI${INDEX?string}_TRBBuildRead(uint16_t address, uint8_t *pdata, uint8_t length)
	
   Summary:
    Allocates and Builds the Read Transaction Request Block.

   Description:
    This function allocates and builds the Read Transaction Block.

   Precondition:
    TWI${INDEX?string}_Initialize must have been called for the associated TWI instance.
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
	  
	    if(!TWI${INDEX?string}_TRBBuildRead( SLAVE_ADDR, &myData[0], NUM_BYTES ))
	    {
		    // error handling
	    }
	  
	    if(!TWI${INDEX?string}_TRBTransfer())
	    {
		    // error handling  
	    }
    
    </code>

   Remarks:
    Number of times TWI${INDEX?string}_TRBBuildRead is called is limited to number of TRB's
	available.
*/

bool TWI${INDEX?string}_TRBBuildRead(uint16_t address, uint8_t *pdata, uint8_t length);

// *****************************************************************************
/* Function:
    bool TWI${INDEX?string}_TRBBuildWrite(uint16_t address, uint8_t *pdata, uint8_t length)
	
   Summary:
    Allocates and Builds the Read Transaction Request Block.
	
   Description:
    This function allocates and builds the Read Transaction Block.

   Precondition:
    TWI${INDEX?string}_Initialize must have been called for the associated TWI instance.
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
	  
	    if(!TWI${INDEX?string}_TRBBuildWrite( SLAVE_ADDR, &myData[0], NUM_BYTES ))
	    {
		    // error handling
	    }
	  
	    if(!TWI${INDEX?string}_TRBTransfer())
	    {
		    // error handling  
	    }
    
    </code>

   Remarks:
    Number of times TWI${INDEX?string}_TRBBuildWrite is called is limited to number of TRB's
	available.
*/

bool TWI${INDEX?string}_TRBBuildWrite(uint16_t address, uint8_t *pdata, uint8_t length);

// *****************************************************************************
/* Function:
    bool TWI${INDEX?string}_TRBTransfer(void)
	
   Summary:
    Submits all TRB's build for processing. 

   Description:
    This function submits all TRB's built by calling TWI${INDEX?string}_TRBBuildRead and 
	TWI${INDEX?string}_TRBBuildWrite. Once all TRB's are submitted for processing, transfer
	starts. A repeated start will occur on completion of a single TRB. Master 
	will generate Stop only after it process all TRB's.
	
   Precondition:
    TWI${INDEX?string}_Initialize must have been called for the associated TWI instance.
	The transfer status should not be busy before calling TWI${INDEX?string}_TRBTransfer.

   Parameters:
    None.
  
   Returns:
    true  - TRB submitted Successfully.
	false - Failure while submitting TRB.

   Example:
	<code>
	    uint8_t myTxData [NUM_BYTES] = {'1', '0', ' ', 'B', 'Y', 'T', 'E', 'S', '!', '!'};
		uint8_t myRxData [NUM_BYTES] = {0};
	  
	    if(!TWI${INDEX?string}_TRBBuildWrite( SLAVE_ADDR, &myTxData[0], NUM_BYTES ))
	    {
		    // error handling
	    }
		
		if(!TWI${INDEX?string}_TRBBuildRead( SLAVE_ADDR, &myRxData[0], NUM_BYTES ))
	    {
		    // error handling
	    }
	  
	    if(!TWI${INDEX?string}_TRBTransfer())
	    {
		    // error handling  
	    }
    
    </code>

   Remarks:
    None.
*/

bool TWI${INDEX?string}_TRBTransfer(void);

// *****************************************************************************
/* Function:
    bool TWI${INDEX?string}_Read(uint16_t address, uint8_t *pdata, uint8_t length)
	
   Summary:
    Reads data from the slave.

   Description:
    This function reads the data of size in bytes equal to length into pdata buffer 
	from the slave having given address. Master will generate Stop condition after 
	completion of the read.

   Precondition:
    TWI${INDEX?string}_Initialize must have been called for the associated TWI instance.
	The transfer status should not be busy before calling TWI${INDEX?string}_TRBTransfer.
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
	  
	    if(!TWI${INDEX?string}_Read( SLAVE_ADDR, &myData[0], NUM_BYTES ))
	    {
		    // error handling
	    }
    </code>

   Remarks:
    None.
*/

bool TWI${INDEX?string}_Read(uint16_t address, uint8_t *pdata, uint8_t length);

// *****************************************************************************
/* Function:
    bool TWI${INDEX?string}_Write(uint16_t address, uint8_t *pdata, uint8_t length)
	
   Summary:
    Writes data onto the slave.

   Description:
    This function writes the data from pdata buffer of size in bytes equal to 
	length onto the slave with given address. Master will generate Stop 
	condition after completion of the write.

   Precondition:
    TWI${INDEX?string}_Initialize must have been called for the associated TWI instance.
	The transfer status should not be busy before calling TWI${INDEX?string}_TRBTransfer.
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
	  
	    if(!TWI${INDEX?string}_Write( SLAVE_ADDR, &myData[0], NUM_BYTES ))
	    {
		    // error handling
	    }
    </code>

   Remarks:
    None.
*/

bool TWI${INDEX?string}_Write(uint16_t address, uint8_t *pdata, uint8_t length);

// *****************************************************************************
/* Function:
    bool TWI${INDEX?string}_WriteRead(uint16_t address, uint8_t *wdata, uint8_t wlength, uint8_t *rdata, uint8_t rlength)
	
   Summary:
    Write and Read data from Slave.

   Description:
    This function writes data from wdata buffer to the slave of given address and
	of size(in bytes) equal to wlength. Master then generates a repeated start and
	do a read operation. Read operation reads data into rdata buffer of size(in
    bytes) equal to rlength from the slave of given address. Master generates a stop
	condition after reading the data.

   Precondition:
    TWI${INDEX?string}_Initialize must have been called for the associated TWI instance.
	The transfer status should not be busy before calling TWI${INDEX?string}_TRBTransfer.
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
	  
	    if(!TWI${INDEX?string}_WriteRead( SLAVE_ADDR, &myTxData[0], NUM_BYTES, myRxData, NUM_BYTES ))
	    {
		    // error handling
	    }
    </code>

   Remarks:
*/

bool TWI${INDEX?string}_WriteRead(uint16_t address, uint8_t *wdata, uint8_t wlength, uint8_t *rdata, uint8_t rlength);

// *****************************************************************************
/* Function:
    TWI_TRANSFER_STATUS TWI${INDEX?string}_TransferStatusGet(void)
	
   Summary:
    Returns the transfer status associated with the given TWI peripheral instance.

   Description:
    This function returns the complete or error transfer status associated with 
    the given TWI peripheral instance.

   Precondition:
    TWI${INDEX?string}_Initialize must have been called for the associated TWI instance.

   Parameters:
    None.
	
   Returns:
    Status of the transfer.
	
   Example:
    <code>
    if(TWI_TRANSFER_COMPLETE == TWI${INDEX?string}_TransferStatusGet())
    {
        //TWI transfer is completed, go to next state.
    }
    </code>

   Remarks:
    None.
*/

TWI_TRANSFER_STATUS TWI${INDEX?string}_TransferStatusGet(void);

// *****************************************************************************
/* Function:
    void TWI${INDEX?string}_CallbackRegister(TWI_CALLBACK callback, uintptr_t contextHandle)
	
   Summary:
    Sets the pointer to the function (and it's context) to be called when the 
    given TWI's transfer events occur.

   Description:
    This function sets the pointer to a client function to be called "back" 
    when the given TWI's transfer events occur. It also passes a context value 
    (usually a pointer to a context structure) that is passed into the
    function when it is called.

   Precondition:
    TWI${INDEX?string}_Initialize must have been called for the associated TWI instance.

   Parameters:
    callback - A pointer to a function with a calling signature defined 
	by the TWI_CALLBACK data type.

    context - A value (usually a pointer) passed (unused) into the function 
	identified by the callback parameter.
  
   Returns:
    None.

   Example:
    <code>
    TWI${INDEX?string}_CallbackRegister(MyTWICallback, &myData);
    </code>

   Remarks:
    The context parameter is ignored if the pointer passed is NULL.
    To disable the callback function, pass a NULL for the callback parameter.
    See the TWI_CALLBACK type definition for additional information.
*/

void TWI${INDEX?string}_CallbackRegister(TWI_CALLBACK callback, uintptr_t contextHandle);

// *****************************************************************************
/* Function:
    void TWI${INDEX?string}_InterruptHandler(void)

   Summary:
    TWI${INDEX?string} Peripheral Interrupt Handler.

   Description:
    This function is TWI${INDEX?string} Peripheral Interrupt Handler and will
    called on every TWI${INDEX?string} interrupt.

   Precondition:
    None.

   Parameters:
    None.
  
   Returns:
    None.

   Remarks:
    The function is called as peripheral instance's interrupt handler if the 
	instance interrupt is enabled. If peripheral instance's interrupt is not
	enabled user need to call it from the main while loop of the application.
*/

void TWI${INDEX?string}_InterruptHandler(void);

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END

#endif //PLIB_TWI${INDEX?string}_H

/*******************************************************************************
 End of File
*/
