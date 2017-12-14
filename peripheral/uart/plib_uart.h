/*******************************************************************************
  UART Peripheral Library Interface Header File

  Company
    Microchip Technology Inc.

  File Name
    plib_uart.h

  Summary
    UART peripheral library interface.

  Description
    This file defines the interface to the UART peripheral library.  This 
    library provides access to and control of the associated peripheral 
    instance.

  Remarks:
    This header is for documentation only.  The actual plib_uart<x> headers 
    will be generated as required by the MCC (where <x> is the peripheral 
    instance number).

    Every interface symbol has a lower-case 'x' in it following the "UART" 
    abbreviation.  This 'x' will be replaced by the peripheral instance number
    in the generated headers.  These are the actual functions that should be
    used.
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

#ifndef _PLIB_UARTx_H    // Guards against multiple inclusion
#define _PLIB_UARTx_H


// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

/*  This section lists the other files that are included in this file.
*/

#include <xc.h>
#include <stdint.h>
#include <stdbool.h>
#include <stddef.h>
#include <sys/attribs.h>

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
/* UART Errors

   Summary:
    Defines the data type for the UART peripheral errors.

   Description:
    This may be used to check the type of error occurred with the UART 
    peripheral during error status.

   Remarks:
    None.
*/

typedef enum
{
    
    UART_ERROR_NONE,
    
    UART_ERROR_OVERRUN,
    
    UART_ERROR_PARITY,
    
    UART_ERROR_FRAMING

} UART_ERROR;


// *****************************************************************************
/* UART Transfer Direction

   Summary:
    Defines the data type for the UART peripheral transfer direction.

   Description:
    This may be used in the callback or status check function to verify the 
    ready status or event is triggered from either Transmit or Receive.

   Remarks:
    None.
*/

typedef enum
{
    
    UART_TRANSMIT,
    
    UART_RECEIVE

} UART_DIRECTION;


// *****************************************************************************
/* UART Transfer Status

   Summary:
    Defines the data type for the UART peripheral transfer status.

   Description:
    This may be used to check the type of status for the transfer that client 
    has requested to the peripheral.
    
   Remarks:
    None.
*/

typedef enum
{
    
    /* Initial state of the peripheral */
    UART_TRANSFER_IDLE,
    
    /* Status when peripheral is processing the buffer */
    UART_TRANSFER_PROCESSING,
    
    /* Status when peripheral has completed processing the buffer */
    UART_TRANSFER_COMPLETE,
    
    /* Status when peripheral has encountered an error while processing 
     * the buffer */
    UART_TRANSFER_ERROR,

} UART_TRANSFER_STATUS;


// *****************************************************************************
/* Callback Function Pointer

   Summary:
    Defines the data type and function signature for the UART peripheral 
    callback function.

   Description:
    This data type defines the function signature for the UART peripheral 
    callback function. The UART peripheral will call back the client's 
    function with this signature when the UART buffer event has occurred.

   Precondition:
    UARTx_Initialize must have been called for the given UART peripheral 
    instance and UARTx_CallbackRegister must have been called to set the 
    function to be called.

   Parameters:
    status  - Complete or error status of the UART buffer transfer.
    
    direction  - Direction of transfer associated with the event.
    
    context  - Allows the caller to provide a context value (usually a pointer
    to the callers context for multi-instance clients).
  
   Returns:
    None.

   Example:
    <code>
    // Data tracking what each of my instances is doing.
    MY_DATA myData[2];

    void MyUartCallback ( UART_TRANSFER_STATUS status, 
        UART_DIRECTION direction, uintptr_t context )
    {
        MY_DATA *mePtr = (MY_DATA *)context;

        if(UART_TRANSFER_COMPLETE == status)
        {
            //Handle complete status here based on direction and context
        } 
        else
        {
            //Handle error here 
        }
    }

    UART1_CallbackSet(MyUartCallback, &myData[0]);
    UART2_CallbackSet(MyUartCallback, &myData[1]);
    </code>

   Remarks:
    None.
*/

typedef void (*UARTx_CALLBACK)( UART_TRANSFER_STATUS status,  UART_DIRECTION direction, uintptr_t context );


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
    void UARTx_Initialize( void )

   Summary:
     Initializes given instance of the UART peripheral.

   Description:
     This function initializes the given instance of the UART peripheral as
     configured by the user from within the MCC.  

   Precondition:
     None.

   Parameters:
    None.
  
   Returns:
    None.

   Example:
    <code>
    UART1_Initialize();
    </code>

   Remarks:
    Stops the UART if it was already running and reinitializes it.
*/

void UARTx_Initialize( void );


// *****************************************************************************
/* Function:
    UART_ERROR UARTx_ErrorGet( void )

   Summary:
    Gets the error of the given UART peripheral instance.

   Description:
    This function returns the errors associated with the given UART peripheral 
    instance.

   Precondition:
    UARTx_Initialize must have been called for the associated UART instance.

   Parameters:
    None.
  
   Returns:
    Errors occurred as listed by UART_ERROR.

  Example:
    <code>
    if (UART_ERROR_OVERRUN == UART1_ErrorGet())
    {
        //Handle overrun error here
    }
    </code>

  Remarks:
    None.
*/

UART_ERROR UARTx_ErrorGet( void );


// *****************************************************************************
/* Function:
    size_t UARTx_Write( void *buffer, const size_t size )

   Summary:
    Submits a write buffer to the given UART peripheral to transfer.

   Description:
    This function submits a write buffer to the UART peripheral to transfer.
    The behavior of this function call will vary based on the mode 
    selected within MCC.
    
    If the peripheral is configured for the interrupt mode, this function call 
    is always non-blocking. Call to this function submits the buffer and the 
    size to the peripheral library and returns immediately. User can check the 
    transfer status either through callback mechanism or by calling 
    UARTx_TransferStatusGet.
    
    If the peripheral is configured for the non-interrupt mode, this 
    function call returns only after requested size is transferred.    

   Precondition:
    UARTx_Initialize must have been called for the associated UART instance.

   Parameters:
    buffer - Pointer to the user buffer.
    size - Number of bytes to be transferred.
  
   Returns:
    Number of bytes processed.
    Returns -1 if the arguments are not valid or if the library is in an error 
	state.

  Example:
    <code>
    //Example to use in non-interrupt mode
    char myData[COUNT] = {"hello"}; //COUNT is user message size
    
    if(-1 != UART1_Write(&myData, COUNT))
    {
        //The transfer is completed
    }
    else
    {
        //Invalid arguments
    }
    </code>

  Remarks:
    None.
*/

size_t UARTx_Write( void *buffer, const size_t size );


// *****************************************************************************
/* Function:
    size_t UARTx_Read( void *buffer, const size_t size )

   Summary:
    Submits a read buffer to the given UART peripheral to process.

   Description:
    This function submits a read buffer to the UART peripheral to process.
    The behavior of this function call will vary based on the mode 
    selected within MCC.
    
    If the peripheral is configured for the interrupt mode, this function call 
    is always non-blocking. Call to this function submits the buffer and the 
    size to the peripheral library and returns immediately. User can check the 
    transfer status either through callback mechanism or by calling 
    UARTx_TransferStatusGet.
    
    If the peripheral is configured for the non-interrupt mode, this 
    function call returns only after requested size is processed.    

   Precondition:
    UARTx_Initialize must have been called for the associated UART instance.

   Parameters:
    buffer - Pointer to the user buffer.
    size - Number of bytes to be transferred.
  
   Returns:
    Number of bytes processed.
    Returns -1 if the arguments are not valid or if the library is in an error 
	state.

  Example:
    <code>
    //Example to use in non-interrupt
    char rxData[COUNT] = {}; //COUNT is expected size
    
    if(-1 != UART1_Read(&rxData, COUNT))
    {
        //The transfer is completed
    }
    else
    {
        //Invalid arguments
    }
    </code>

  Remarks:
    None.
*/

size_t UARTx_Read( void *buffer, const size_t size );


// *****************************************************************************
/* Function:
    void UARTx_CallbackRegister( UART_CALLBACK callback, uintptr_t context )

   Summary:
    Sets the pointer to the function (and it's context) to be called when the 
    given UART's transfer events occur.

   Description:
    This function sets the pointer to a client function to be called "back" 
    when the given UART's transfer events occur. It also passes a context value 
    (usually a pointer to a context structure) that is passed into the
    function when it is called.
    
    This function is available only in interrupt or non-blocking mode of 
    operation.

   Precondition:
    UARTx_Initialize must have been called for the associated UART instance.

   Parameters:
    callback - A pointer to a function with a calling signature defined 
	by the UART_CALLBACK data type.

    context - A value (usually a pointer) passed (unused) into the function 
	identified by the callback parameter.
  
   Returns:
    None.

  Example:
    <code>
    UART1_CallbackRegister(MyuartCallback, &myData);
    </code>

  Remarks:
    The context parameter is ignored if the pointer passed is NULL.

    To disable the callback function, pass a NULL for the callback parameter.

    See the UART_CALLBACK type definition for additional information.
*/

void UARTx_CallbackRegister( UART_CALLBACK callback, uintptr_t context );


// *****************************************************************************
/* Function:
    UART_TRANSFER_STATUS UARTx_TransferStatusGet( UART_DIRECTION direction )

   Summary:
    Returns the transfer status associated with the given UART peripheral 
    instance.

   Description:
    This function returns the complete or error transfer status associated with 
    the given UART peripheral instance and the direction.
    
    This function is available only in interrupt or non-blocking mode of 
    operation.

   Precondition:
    UARTx_Initialize must have been called for the associated UART instance.

   Parameters:
    direction - Direction of transfer of which the status is requested.
  
   Returns:
    Status of either the Transmit or Receive transfer.

  Example:
    <code>
    if(UART_TRANSFER_COMPLETE == UART1_TransferStatusGet(UART_RECEIVE))
    {
        //UART Receive buffer transfer is completed, go to next state.
    }
    </code>

  Remarks:
    None.
*/

UART_TRANSFER_STATUS UARTx_TransferStatusGet( UART_DIRECTION direction );


// *****************************************************************************
/* Function:
    size_t UARTx_TransferCountGet( UART_DIRECTION direction )

   Summary:
    Returns the count of number of bytes processed for a given UART peripheral 
    instance.

   Description:
    This function returns the count of number of bytes processed for a given 
    UART peripheral instance and the direction.
    
    This function is available only in interrupt or non-blocking mode of 
    operation.

   Precondition:
    UARTx_Initialize must have been called for the associated UART instance.

   Parameters:
    direction - Direction of transfer of which the status is requested.
  
   Returns:
    Count of bytes completed/processed from the current Transmit or Receive 
	buffer.
    This Function may return -1 if there is any error.

  Example:
    <code>
    size_t count; //COUNT_EXPECTED is the expected Receive count value
    
    count = UART1_TransferCountGet(UART_RECEIVE);
    
    if(COUNT_EXPECTED > count)
    {
        //More bytes expected, wait
    }
    </code>

  Remarks:
    This function resets the count for associated direction every time a new 
	transfer is submitted.
*/

size_t UARTx_TransferCountGet( UART_DIRECTION direction );


// *****************************************************************************
/* Function:
    void UARTx_ErrorClear( void )

   Summary:
    Clears all the errors of the given UART peripheral instance.

   Description:
    This function clears the errors associated with the given UART peripheral 
    instance.
	
    This function is available only in non-interrupt mode of operation. 
	In interrupt mode, peripheral library will clear the errors and provides an 
	error event through callback.

   Precondition:
    UARTx_Initialize must have been called for the associated UART instance.

   Parameters:
    None.
  
   Returns:
    None.

  Example:
    <code>
    if (UART_ERROR_OVERRUN == UART1_ErrorGet())
    {
        //Handle overrun error here
		UART1_ErrorClear();
    }
    </code>

  Remarks:
    None.
*/

void UARTx_ErrorClear( void );


// *****************************************************************************
/* Function:
    bool UARTx_ReadyStatusGet( UART_DIRECTION direction )

   Summary:
    Returns the hardware status of Transmit or Receive associated with the given 
	UART peripheral instance.

   Description:
    This function returns the hardware status associated with 
    the Transmit or Receive hardware FIFO of the given UART peripheral 
	instance.
	
	When Transmit is ready, user can submit data for the transmit. 
	When Receive is ready, user can read the received data.
	
	This function is available only in non-interrupt mode of operation. And can
	be used to achieve non-blocking behavior of write and read requests. User 
	has to check the Transmit or Receive ready status by calling this function 
	and can submit write or read request for the buffer size of 1.  

   Precondition:
    UARTx_Initialize must have been called for the associated UART instance.

   Parameters:
    direction - Direction of transfer of which the ready status is requested.
  
   Returns:
    true - Transmit hardware FIFO has empty space to accept the data for the 
	transfer or Receive hardware FIFO has data available to be read.
	false - Transmit hardware FIFO is full or Receive hardware FIFO is empty.

  Example:
    <code>
    if(true == UART1_ReadyStatusGet(UART_RECEIVE))
    {
		// Data is available and can read a byte
        UART1_Read(&rxData, 1);
    }
	else
	{
		//Data is not available to read
	}
    </code>

  Remarks:
    If user submits read or write request for more than 1 byte after checking 
	the ready status, then read or write API will block until the submitted 
	length of data is processed. This is the native behavior of read and write 
	API in the non-interrupt mode of library.
*/

bool UARTx_ReadyStatusGet( UART_DIRECTION direction );


// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END

#endif //_PLIB_UARTx_H
