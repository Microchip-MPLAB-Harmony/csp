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

#ifndef PLIB_UARTx_H    // Guards against multiple inclusion
#define PLIB_UARTx_H

#include <stddef.h>
#include <stdbool.h>
#include <stdint.h>

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

/*  This section lists the other files that are included in this file.
*/

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

typedef enum
{
    UART_PARITY_NONE = 0,

    UART_PARITY_ODD = 1,

    UART_PARITY_EVEN = 2,

    UART_PARITY_MARK = 3,

    UART_PARITY_SPACE = 4

} UART_PARITY;

// *****************************************************************************
/* UART Serial Setup

   Summary:
    Defines the data type for the UART serial setup.

   Description:
    This can be used to define a serial setup which may then be used to change
    the serial setup of the UART dynamically.

   Remarks:
    None.
*/

typedef struct
{
    uint32_t baudRate;

    UART_PARITY parity;

} UART_SERIAL_SETUP;


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
    instance and UARTx_WriteCallbackRegister or UARTx_ReadCallbackRegister
    must have been called to set the function to be called.

   Parameters:
    context  - Allows the caller to provide a context value (usually a pointer
    to the callers context for multi-instance clients).

   Returns:
    None.

   Example:
    <code>
    // Data tracking what each of my instances is doing.
    MY_DATA myData[2];

    void MyUartCallback ( uintptr_t context )
    {
        MY_DATA *myData = (MY_DATA *)context;

        if(UART_ERROR_NONE != UARTx_ErrorGet())
        {
            //Handle error case
        }
        else
        {
            //Transfer completed successfully
        }
    }

    UART1_WriteCallbackRegister(MyUartCallback, &myData[0]);
    </code>

   Remarks:
    None.
*/

typedef void (*UART_CALLBACK)( uintptr_t context );


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
// *****************************************************************************
// Section: Transaction (Write/Read) Request Interface
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Function:
    bool UARTx_Write( void *buffer, const size_t size )

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
    UARTx_WriteIsBusy.

    If the peripheral is configured for the non-interrupt mode, this
    function call returns only after requested size is transferred.

   Precondition:
    UARTx_Initialize must have been called for the associated UART instance.

   Parameters:
    buffer - Pointer to the user buffer.
    size - Number of bytes to be transferred.

   Returns:
    Write request status.
    True - Write request was successful.
    False - Write request has failed.

  Example:
    <code>
    //Example to use in non-interrupt mode
    char myData[COUNT] = {"hello"}; //COUNT is user message size

    if(false != UART1_Write(&myData, COUNT))
    {
        //The transfer is completed
    }
    else
    {
        //Write failed
    }
    </code>

  Remarks:
    None.
*/

bool UARTx_Write( void *buffer, const size_t size );

// *****************************************************************************
/* Function:
    void UARTx_WriteByte( int data )

   Summary:
    Submits a byte of data to the given UART peripheral to transfer.

   Description:
    This function submits a byte of data to the UART peripheral to transfer.
    This Function is available only in non-interrupt mode.

   Precondition:
    UARTx_Initialize must have been called for the associated UART instance.

   Parameters:
    data - Data byte to be transferred.

   Returns:
    None

  Example:
    <code>
    //Example to use in non-interrupt mode
    char myData = 0xAA;

    UART1_Write(&myData)

    </code>

  Remarks:
    None.
*/

bool UARTx_WriteByte( int data );


// *****************************************************************************
/* Function:
    bool UARTx_Read( void *buffer, const size_t size )

   Summary:
    Submits request to read n-Bytes of data to the given UART peripheral.

   Description:
    This function submits a request to read n-Bytes of data to the UART peripheral.
    The behavior of this function call will vary based on the mode
    selected within MCC.

    If the peripheral is configured for the interrupt mode, this function call
    is always non-blocking. Call to this function submits the buffer and the
    size to the peripheral library and returns immediately. User can check the
    transfer status either through callback mechanism or by calling
    UARTx_ReadIsBusy.

    If the peripheral is configured for the non-interrupt mode, this
    function call returns only after requested size is processed.

   Precondition:
    UARTx_Initialize must have been called for the associated UART instance.

   Parameters:
    buffer - Pointer to the user buffer.
    size - Number of bytes to be read.

   Returns:
    Read request status.
    True - Read request was successful.
    False - Read request has failed.

  Example:
    <code>
    //Example to use in non-interrupt
    char rxData[COUNT] = {}; //COUNT is expected size

    if(false != UART1_Read(&rxData, COUNT))
    {
        //The transfer is completed
    }
    else
    {
        //Read failed
    }
    </code>

  Remarks:
    None.
*/

bool UARTx_Read( void *buffer, const size_t size );

// *****************************************************************************
/* Function:
    int UARTx_ReadByte( void )

   Summary:
    Submits request to read a byte of data to the given UART peripheral.

   Description:
    This function submits request to read a byte of data to the given UART peripheral.
    This Function is available only in non-interrupt mode.

   Precondition:
    UARTx_Initialize must have been called for the associated UART instance.

   Parameters:
    None

   Returns:
    Read byte.

  Example:
    <code>
    //Example to use in non-interrupt
    char rxData;

    if(UART1_ReceiverIsReady() == true)
    {
        rxData = UART1_ReadByte();
    }
    </code>

  Remarks:
    None.
*/

int UARTx_ReadByte( void );

// *****************************************************************************
// *****************************************************************************
// Section: Transaction (Write/Read) Status Interface
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Function:
    bool UARTx_WriteIsBusy( void )

   Summary:
    Returns the write request status associated with the given UART peripheral
    instance.

   Description:
    This function returns the write request status associated with the given
    UART peripheral instance.

    This function is available only in interrupt or non-blocking mode of
    operation.

   Precondition:
    UARTx_Initialize must have been called for the associated UART instance.

   Parameters:
    None.

   Returns:
    Status of Write request.
    True - UART is busy in processing the previous write request.
    False - UART is free and ready to accept the new write request.

  Example:
    <code>
    if(true == UART1_WriteIsBusy())
    {
        //UART is currently processing the previous write request.
        //Wait to submit new request.
    }
    </code>

  Remarks:
    None.
*/

bool UARTx_WriteIsBusy( void );


// *****************************************************************************
/* Function:
    bool UARTx_ReadIsBusy( void )

   Summary:
    Returns the read request status associated with the given UART peripheral
    instance.

   Description:
    This function returns the read request status associated with the given
    UART peripheral instance.

    This function is available only in interrupt or non-blocking mode of
    operation.

   Precondition:
    UARTx_Initialize must have been called for the associated UART instance.

   Parameters:
    None.

   Returns:
    Status of Read request.
    True - UART is busy in processing the previous read request.
    False - UART is free and ready to accept the new read request.

  Example:
    <code>
    if(true == UART1_ReadIsBusy())
    {
        //UART is currently processing the previous read request.
        //Wait to submit new request.
    }
    </code>

  Remarks:
    None.
*/

bool UARTx_ReadIsBusy( void );


// *****************************************************************************
/* Function:
    size_t UARTx_WriteCountGet( void )

   Summary:
    Returns the count of number of bytes processed for a given UART write
    operation.

   Description:
    This function returns the count of number of bytes processed for a given
    UART write operation.

    This function is available only in interrupt or non-blocking mode of
    operation.

   Precondition:
    UARTx_Initialize must have been called for the associated UART instance.

   Parameters:
    None.

   Returns:
    Count of bytes completed/processed from the current Transmit buffer.
    This Function will return -1 if there is any error.

  Example:
    <code>
    size_t count; //COUNT_EXPECTED is the expected Transmit count value

    count = UART1_WriteCountGet();

    if(COUNT_EXPECTED > count)
    {
        //More bytes are expected to transmit, wait
    }
    </code>

  Remarks:
    This function resets the write count every time a new transfer is submitted.
*/

size_t UARTx_WriteCountGet( void );


// *****************************************************************************
/* Function:
    size_t UARTx_ReadCountGet( void )

   Summary:
    Returns the count of number of bytes processed for a given UART read
    operation.

   Description:
    This function returns the count of number of bytes processed for a given
    UART read operation.

    This function is available only in interrupt or non-blocking mode of
    operation.

   Precondition:
    UARTx_Initialize must have been called for the associated UART instance.

   Parameters:
    None.

   Returns:
    Count of bytes completed/processed to the current Receive buffer.
    This Function will return -1 if there is any error.

  Example:
    <code>
    size_t count; //COUNT_EXPECTED is the expected Receive count value

    count = UART1_ReadCountGet();

    if(COUNT_EXPECTED > count)
    {
        //More bytes are expected, wait
    }
    </code>

  Remarks:
    This function resets the read count every time a new transfer is submitted.
*/

size_t UARTx_ReadCountGet( void );

// *****************************************************************************
// *****************************************************************************
// Section: Peripheral (Write/Read) Status Interface
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Function:
    void UARTx_Sync( void )

   Summary:
    This Function busy waits unitll all transmit requests are completed.

   Description:
    This function is available only in non-interrupt mode of operation.
    It can be used to busy wait untill transmit fifo is empty.

   Precondition:
    UARTx_Initialize must have been called for the associated UART instance.

   Parameters:
    None.

   Returns:
    None

  Example:
    <code>
        UART1_Sync();
    </code>

  Remarks:
    None
*/

void UARTx_Sync( void );

// *****************************************************************************
/* Function:
    bool UARTx_TransmitterIsReady( void )

   Summary:
    Returns the hardware status of the UART Transmitter.

   Description:
    This function returns the hardware status associated with the Transmit
    hardware FIFO of the given UART peripheral instance.

    When Transmitter is ready, user can submit data to transmit.

    This function is available only in non-interrupt mode of operation. And can
    be used to achieve non-blocking behavior of write request. User has to check
    the Transmit ready status by calling this function and can submit write
    request for the buffer size of 1.

   Precondition:
    UARTx_Initialize must have been called for the associated UART instance.

   Parameters:
    None.

   Returns:
    true - Transmit hardware FIFO has empty space to accept the data.
    false - Transmit hardware FIFO is full.

  Example:
    <code>
    if(true == UART1_TransmitterIsReady())
    {
        // Empty space is available in Transmitter FIFO, hence can write a byte
        UART1_Write(&txData, 1);
    }
    else
    {
        //Transmitter is busy
    }
    </code>

  Remarks:
    If user submits write request for more than 1 byte after checking the ready
    status, then write API will block until the submitted length of data is
    processed. This is the native behavior of the write API in the non-interrupt
    or blocking mode of the library.
*/

bool UARTx_TransmitterIsReady( void );

// *****************************************************************************
/* Function:
    bool UARTx_ReceiverIsReady( void )

   Summary:
    Returns the hardware status of the UART Receiver.

   Description:
    This function returns the hardware status associated with the Receive
    hardware FIFO of the given UART peripheral instance.

    When Receiver is ready, user can read the available data.

    This function is available only in non-interrupt mode of operation. And can
    be used to achieve non-blocking behavior of read request. User has to check
    the Receiver ready status by calling this function and can submit a read
    request for the buffer size of 1.

   Precondition:
    UARTx_Initialize must have been called for the associated UART instance.

   Parameters:
    None.

   Returns:
    true - Receive hardware FIFO has at least one data available to read.
    false - Receive hardware FIFO is empty.

  Example:
    <code>
    if(true == UART1_ReceiverIsReady())
    {
        // At least one data is available in Receive FIFO, hence can read a byte
        UART1_Read(&rxData, 1);
    }
    else
    {
        //Receiver is empty
    }
    </code>

  Remarks:
    If user submits read request for more than 1 byte after checking the ready
    status, then read API will block until the submitted length of data is
    processed. This is the native behavior of the read API in the non-interrupt
    or blocking mode of the library.
*/

bool UARTx_ReceiverIsReady( void );


// *****************************************************************************
/* Function:
    UART_ERROR UARTx_ErrorGet( void )

   Summary:
    Gets the error of the given UART peripheral instance.

   Description:
    This function returns the errors associated with the given UART peripheral
    instance. The call to this function also clears all the associated errors.

   Precondition:
    UARTx_Initialize must have been called for the associated UART instance.

   Parameters:
    None.

   Returns:
    Errors occurred as listed by UART_ERROR.
    This function reports multiple UART errors if occurred.

  Example:
    <code>
    if (UART_ERROR_OVERRUN & UART1_ErrorGet())
    {
        //Errors are cleared by the API call, take respective action
        //for the overrun error case.
    }
    </code>

  Remarks:
    UART errors are normally associated with the receiver. Hence, it is
    recommended to use this function in receive context only.
*/

UART_ERROR UARTx_ErrorGet( void );


// *****************************************************************************
/* Function:
    void UARTx_SerialSetup(UART_SERIAL_SETUP * setup, uint32_t srcClkFreq)

   Summary:
    Sets the UART serial communication settings dynamically.

   Description:
    This function sets the UART serial communication settings dynamically.

   Precondition:
    UARTx_Initialize must have been called for the associated UART instance.
    The UART transmit or receive transfer status should not be busy.

   Parameters:
    setup - Pointer to the structure containing the serial setup.
    srcClkFreq - UART Peripheral Clock Source Frequency.

   Returns:
    true - Serial setup was updated Successfully.
    false - Failure while updating serial setup.

   Example:
    <code>
    UART_SERIAL_SETUP setup = {
            115200,
            UART_PARITY_ODD
        };

    UART1_SerialSetup(&setup, 0);
    </code>

   Remarks:
    srcClkFreq overrides any change in the peripheral clock frequency.
    If configured to zero PLib takes the peripheral clock frequency from MHC.
*/

bool UARTx_SerialSetup( UART_SERIAL_SETUP *setup, uint32_t srcClkFreq );

// *****************************************************************************
// *****************************************************************************
// Section: Callback Interface
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Function:
    bool UARTx_WriteCallbackRegister( UART_CALLBACK callback, uintptr_t context )

   Summary:
    Sets the pointer to the function (and it's context) to be called when the
    given UART's write events occur.

   Description:
    This function sets the pointer to a client function to be called "back"
    when the given UART's write events occur. It also passes a context value
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
    Callback registration status.
    True - Callback registration was successful
    False - Callback registration failed.

  Example:
    <code>
    // Data tracking what each of my instances is doing.
    MY_DATA myData[2];

    void MyUartCallback ( uintptr_t context )
    {
        MY_DATA *myData = (MY_DATA *)context;

        if(UART_ERROR_NONE != UARTx_ErrorGet())
        {
            //Handle error case
        }
        else
        {
            //Transfer completed successfully
        }
    }

    UART1_WriteCallbackRegister(MyUartCallback, &myData[0]);
    </code>

  Remarks:
    The context parameter is ignored if the pointer passed is NULL.
    To disable the callback function, pass a NULL for the callback parameter.
    See the UART_CALLBACK type definition for additional information.
*/

bool UARTx_WriteCallbackRegister( UART_CALLBACK callback, uintptr_t context );


// *****************************************************************************
/* Function:
    bool UARTx_ReadCallbackRegister( UART_CALLBACK callback, uintptr_t context )

   Summary:
    Sets the pointer to the function (and it's context) to be called when the
    given UART's read events occur.

   Description:
    This function sets the pointer to a client function to be called "back"
    when the given UART's read events occur. It also passes a context value
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
    Callback registration status.
    True - Callback registration was successful
    False - Callback registration failed.

  Example:
    <code>
    // Data tracking what each of my instances is doing.
    MY_DATA myData[2];

    void MyUartCallback ( uintptr_t context )
    {
        MY_DATA *myData = (MY_DATA *)context;

        if(UART_ERROR_NONE != UARTx_ErrorGet())
        {
            //Handle error case
        }
        else
        {
            //Transfer completed successfully
        }
    }

    UART1_ReadCallbackRegister(MyUartCallback, &myData[0]);
    </code>

  Remarks:
    The context parameter is ignored if the pointer passed is NULL.
    To disable the callback function, pass a NULL for the callback parameter.
    See the UART_CALLBACK type definition for additional information.
*/

bool UARTx_ReadCallbackRegister( UART_CALLBACK callback, uintptr_t context );


// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END

#endif //PLIB_UARTx_H
