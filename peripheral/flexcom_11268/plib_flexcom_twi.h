/*******************************************************************************
  FLEXCOM TWI Peripheral Library Interface Header File

  Company
    Microchip Technology Inc.

  File Name
    plib_flexcom_twi.h

  Summary
    FLEXCOM TWI peripheral library interface.

  Description
    This file defines the interface to the FLEXCOM TWI peripheral library.  This 
    library provides access to and control of the associated peripheral 
    instance.

  Remarks:
    This header is for documentation only.  The actual plib_flexcom<x>_twi headers 
    will be generated as required by the MHC (where <x> is the peripheral 
    instance number).

    Every interface symbol has a lower-case 'x' in it following the "FLEXCOM" 
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

#ifndef PLIB_FLEXCOMx_TWI_H   
#define PLIB_FLEXCOMx_TWI_H

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
/* FLEXCOM TWI Transfer Status

   Summary:
    FLEXCOM TWI Transfer Status data type.

   Description:
    This data type defines the FLEXCOM TWI Transfer Status.

   Remarks:
    None.
*/

typedef enum
{   
    /* No Error */
    FLEXCOM_TWI_ERROR_NONE,
    
    /* Slave returned Nack */
    FLEXCOM_TWI_ERROR_NACK,
    
} FLEXCOM_TWI_ERROR;

// *****************************************************************************
/* FLEXCOM TWI State.

   Summary:
    FLEXCOM TWI PLib Task State.

   Description:
    This data type defines the FLEXCOM TWI PLib Task State.

   Remarks:
    None.
  
*/

typedef enum {

    /* FLEXCOM TWI PLib Task Error State */
    FLEXCOM_TWI_STATE_ERROR = -1,
    
    /* FLEXCOM TWI PLib Task Idle State */
    FLEXCOM_TWI_STATE_IDLE,
    
    /* FLEXCOM TWI PLib Task Address Send State */
    FLEXCOM_TWI_STATE_ADDR_SEND,
    
    /* FLEXCOM TWI PLib Task Read Transfer State */
    FLEXCOM_TWI_STATE_TRANSFER_READ,
    
    /* FLEXCOM TWI PLib Task Write Transfer State */
    FLEXCOM_TWI_STATE_TRANSFER_WRITE,
    
    /* FLEXCOM TWI PLib Task Transfer Complete State */
    FLEXCOM_TWI_STATE_WAIT_FOR_TXCOMP,
    
    /* FLEXCOM TWI PLib Task Transfer Done State */
    FLEXCOM_TWI_STATE_TRANSFER_DONE,

} FLEXCOM_TWI_STATE;

// *****************************************************************************
/* FLEXCOM TWI Transfer Event Callback Function Pointer.

   Summary:
    Defines the data type and function signature for the FLEXCOM TWI peripheral 
    callback function.
	
   Description:
    This data type defines the function signature for the FLEXCOM TWI peripheral 
    callback function. The FLEXCOM TWI peripheral will call back the client's 
    function with this signature when the FLEXCOM TWI Transfer event has occurred.

   Precondition:
    FLEXCOMx_TWI_Initialize must have been called for the given FLEXCOM TWI peripheral 
    instance and FLEXCOMx_TWI_CallbackRegister must have been called to set the 
    function to be called.
	
   Parameters:
    status  - Complete or error status of the FLEXCOM TWI transfer.
    
    context - Allows the caller to provide a context value (usually a pointer
    to the callers context for multi-instance clients).
  
   Returns:
    None.

   Example:
    <code>
    // Data tracking what each of my instances is doing.
    MY_DATA myData[2];

    void MyFLEXCOMTWICallback (uintptr_t context )
    {
        MY_DATA *mePtr = (MY_DATA *)context;

        //Handle complete status or error here based on context 
    }

    FLEXCOM1_TWI_CallbackSet(MyFLEXCOMTWICallback, &myData[0]);
    FLEXCOM2_TWI_CallbackSet(MyFLEXCOMTWICallback, &myData[1]);
    </code>
	
   Remarks:
    None.
*/
typedef void (*FLEXCOM_TWI_CALLBACK) (uintptr_t contextHandle);

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
    void FLEXCOMx_TWI_Initialize(void)

   Summary:
    Initializes given instance of the FLEXCOM TWI peripheral.
    
   Description:
    This function initializes the given instance of the FLEXCOM TWI peripheral as
    configured by the user from within the MHC.

   Precondition:
    None.
    
   Parameters:
    None.
    
   Returns:
    None

   Example:
    <code>
    FLEXCOMx_TWI_Initialize();
    </code>

   Remarks:
    Stops the FLEXCOM TWI if it was already running and reinitializes it.
*/

void FLEXCOMx_TWI_Initialize(void);

// *****************************************************************************
/* Function:
    void FLEXCOMx_TWI_CallbackRegister(FLEXCOM_TWI_CALLBACK callback, uintptr_t contextHandle)
    
   Summary:
    Sets the pointer to the function (and it's context) to be called when the 
    given FLEXCOM TWI's transfer events occur.

   Description:
    This function sets the pointer to a client function to be called "back" 
    when the given FLEXCOM TWI's transfer events occur. It also passes a context value 
    (usually a pointer to a context structure) that is passed into the
    function when it is called.

   Precondition:
    FLEXCOMx_TWI_Initialize must have been called for the associated FLEXCOM TWI instance.

   Parameters:
    callback - A pointer to a function with a calling signature defined 
    by the FLEXCOM_TWI_CALLBACK data type.

    context - A value (usually a pointer) passed (unused) into the function 
    identified by the callback parameter.
  
   Returns:
    None.

   Example:
    <code>
    FLEXCOMx_TWI_CallbackRegister(MyFlexcomTwiCallback, &myData);
    </code>

   Remarks:
    The context parameter is ignored if the pointer passed is NULL.
    To disable the callback function, pass a NULL for the callback parameter.
    See the FLEXCOM_TWI_CALLBACK type definition for additional information.
*/

void FLEXCOMx_TWI_CallbackRegister(FLEXCOM_TWI_CALLBACK callback, uintptr_t contextHandle);

// *****************************************************************************
/* Function:
    bool FLEXCOMx_TWI_IsBusy(void)
    
   Summary:
    Returns the Peripheral busy status.
    
   Description:
    This function returns the peripheral's busy status.

   Precondition:
    FLEXCOMx_TWI_Initialize must have been called for the associated FLEXCOM TWI instance.

   Parameters:
    None.
    
   Returns:
    true - Busy.
    false - Not busy.
    
   Example:
    <code>
        uint8_t myData [NUM_BYTES] = {'1', '0', ' ', 'B', 'Y', 'T', 'E', 'S', '!', '!',};
      
        // wait for the current transfer to complete
        while(FLEXCOMx_TWI_IsBusy( ));
        
        // perform the next transfer
        if(!FLEXCOMx_TWI_Write( SLAVE_ADDR, &myData[0], NUM_BYTES ))
        {
            // error handling
        }
    
    </code>

   Remarks:
    None.
*/

bool FLEXCOMx_TWI_IsBusy(void);

// *****************************************************************************
/* Function:
    bool FLEXCOMx_TWI_Read(uint16_t address, uint8_t *pdata, size_t length)
    
   Summary:
    Reads data from the slave.

   Description:
    This function reads the data of size in bytes equal to length into pdata buffer 
    from the slave having given address. Master will generate Stop condition after 
    completion of the read.

   Precondition:
    FLEXCOMx_TWI_Initialize must have been called for the associated FLEXCOM TWI instance.

   Parameters:
    address - 7-bit / 10-bit slave address.
    pdata   - pointer to destination data buffer
    length  - length of data buffer in number of bytes.
  
   Returns:
    Read request status.
    True - Read request was successful.
    False - Read request has failed.

   Example:
    <code>
        uint8_t myData [NUM_BYTES];
      
        if(!FLEXCOMx_TWI_Read( SLAVE_ADDR, &myData[0], NUM_BYTES ))
        {
            // error handling
        }
    </code>

   Remarks:
    None.
*/

bool FLEXCOMx_TWI_Read(uint16_t address, uint8_t *pdata, size_t length);

// *****************************************************************************
/* Function:
    bool FLEXCOMx_TWI_Write(uint16_t address, uint8_t *pdata, size_t length)
    
   Summary:
    Writes data onto the slave.

   Description:
    This function writes the data from pdata buffer of size in bytes equal to 
    length onto the slave with given address. Master will generate Stop 
    condition after completion of the write.

   Precondition:
    FLEXCOMx_TWI_Initialize must have been called for the associated FLEXCOM TWI instance.

   Parameters:
    address - 7-bit / 10-bit slave address.
    pdata   - pointer to source data buffer
    length  - length of data buffer in number of bytes.
    
   Returns:
    Request status.
    True - Request was successful.
    False - Request has failed.

   Example:
    <code>
        uint8_t myData [NUM_BYTES] = {'1', '0', ' ', 'B', 'Y', 'T', 'E', 'S', '!', '!',};
      
        if(!FLEXCOMx_TWI_Write( SLAVE_ADDR, &myData[0], NUM_BYTES ))
        {
            // error handling
        }
    </code>

   Remarks:
    None.
*/

bool FLEXCOMx_TWI_Write(uint16_t address, uint8_t *pdata, size_t length);

// *****************************************************************************
/* Function:
    bool FLEXCOMx_TWI_WriteRead(uint16_t address, uint8_t *wdata, size_t wlength, uint8_t *rdata, size_t rlength)
    
   Summary:
    Write and Read data from Slave.

   Description:
    This function writes data from wdata buffer to the slave of given address and
    of size(in bytes) equal to wlength. Master then generates a repeated start and
    do a read operation. Read operation reads data into rdata buffer of size(in
    bytes) equal to rlength from the slave of given address. Master generates a stop
    condition after reading the data.

   Precondition:
    FLEXCOMx_TWI_Initialize must have been called for the associated FLEXCOM TWI instance.

   Parameters:
    address - 7-bit / 10-bit slave address.
    wdata   - pointer to write data buffer
    wlength - write data length in bytes.
    rdata   - pointer to read data buffer.
    rlength - read data length in bytes.
  
   Returns:
    Request status.
    True - Request was successful.
    False - Request has failed.

   Example:
    <code>
        uint8_t myTxData [NUM_BYTES] = {'1', '0', ' ', 'B', 'Y', 'T', 'E', 'S', '!', '!'};
        uint8_t myRxData [NUM_BYTES] = {0};
      
        if(!FLEXCOMx_TWI_WriteRead( SLAVE_ADDR, &myTxData[0], NUM_BYTES, myRxData, NUM_BYTES ))
        {
            // error handling
        }
    </code>

   Remarks:
*/

bool FLEXCOMx_TWI_WriteRead(uint16_t address, uint8_t *wdata, size_t wlength, uint8_t *rdata, size_t rlength);

// *****************************************************************************
/* Function:
    FLEXCOM_TWI_ERROR FLEXCOMx_TWI_ErrorGet(void)
    
   Summary:
    Returns the error during transfer.

   Description:
    This function returns the error during transfer.

   Precondition:
    FLEXCOMx_TWI_Initialize must have been called for the associated FLEXCOM TWI instance.

   Parameters:
    None.
    
   Returns:
    Request status.
    True - Request was successful.
    False - Request has failed.
	
   Example:
    <code>
    if(FLEXCOM_TWI_ERROR_NONE == FLEXCOMx_TWI_ErrorGet())
    {
        //FLEXCOM TWI transfer is completed, go to next state.
    }
    </code>

   Remarks:
    None.
*/

FLEXCOM_TWI_ERROR FLEXCOMx_TWI_ErrorGet(void);

// *****************************************************************************
/* Function:
    void FLEXCOMx_InterruptHandler(void)

   Summary:
    FLEXCOMx_TWI Peripheral Interrupt Handler.

   Description:
    This function is FLEXCOMx_TWI Peripheral Interrupt Handler and will
    called on every FLEXCOMx_TWI interrupt.

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

void FLEXCOMx_InterruptHandler(void);

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END


#endif //PLIB_FLEXCOMx_TWI_H

/*******************************************************************************
 End of File
*/
