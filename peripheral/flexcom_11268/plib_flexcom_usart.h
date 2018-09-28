/*******************************************************************************
  FLEXCOM USART Peripheral Library Interface Header File

  Company
    Microchip Technology Inc.

  File Name
    plib_flexcom_usart.h

  Summary
    FLEXCOM USART peripheral library interface.

  Description
    This file defines the interface to the FLEXCOM USART peripheral library. 
    This library provides access to and control of the associated peripheral
    instance.

  Remarks:
    This header is for documentation only.  The actual plib_flexcom<x>_usart
    headers will be generated as required by the MCC (where <x> is the
    peripheral instance number).

    Every interface symbol has a lower-case 'x' in it following the "FLEXCOM"
    abbreviation.  This 'x' will be replaced by the peripheral instance number
    in the generated headers.  These are the actual functions that should be
    used.
*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
Copyright (c) 2018 released Microchip Technology Inc. All rights reserved.
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

#ifndef PLIB_FLEXCOMx_USART_H // Guards against multiple inclusion
#define PLIB_FLEXCOMx_USART_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
/* This section lists the other files that are included in this file.
*/
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

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
/* FLEXCOM USART Errors

   Summary:
    Defines the data type for the FLEXCOM USART peripheral errors.

   Description:
    This may be used to check the type of error occurred with the FLEXCOM USART
    peripheral during error status.

   Remarks:
    None.
*/

typedef enum
{
    FLEXCOM_USART_ERROR_NONE = 0,
    FLEXCOM_USART_ERROR_OVERRUN = FLEX_US_CSR_OVRE_Msk,
    FLEXCOM_USART_ERROR_PARITY = FLEX_US_CSR_PARE_Msk,
    FLEXCOM_USART_ERROR_FRAMING = FLEX_US_CSR_FRAME_Msk

} FLEXCOM_USART_ERROR;


// *****************************************************************************
/* FLEXCOM USART Serial Setup

   Summary:
    Defines the data type for the FLEXCOM USART serial setup.

   Description:
    This can be used to define a serial setup which may then be used to change
    the serial setup of the FLEXCOM USART dynamically.

   Remarks:
    None.
*/

typedef enum
{
    FLEXCOM_USART_DATA_5_BIT = FLEX_US_MR_CHRL_5_BIT,
    FLEXCOM_USART_DATA_6_BIT = FLEX_US_MR_CHRL_6_BIT,
    FLEXCOM_USART_DATA_7_BIT = FLEX_US_MR_CHRL_7_BIT,
    FLEXCOM_USART_DATA_8_BIT = FLEX_US_MR_CHRL_8_BIT,
    FLEXCOM_USART_DATA_9_BIT = FLEX_US_MR_MODE9_Msk,

    /* Force the compiler to reserve 32-bit memory for each enum */
    FLEXCOM_USART_DATA_INVALID = 0xFFFFFFFF

} FLEXCOM_USART_DATA;

typedef enum
{
    FLEXCOM_USART_PARITY_NONE = FLEX_US_MR_PAR_NO,
    FLEXCOM_USART_PARITY_ODD = FLEX_US_MR_PAR_ODD,
    FLEXCOM_USART_PARITY_EVEN = FLEX_US_MR_PAR_EVEN,
    FLEXCOM_USART_PARITY_MARK = FLEX_US_MR_PAR_MARK,
    FLEXCOM_USART_PARITY_SPACE = FLEX_US_MR_PAR_SPACE,
    FLEXCOM_USART_PARITY_MULTIDROP = FLEX_US_MR_PAR_MULTIDROP,

    /* Force the compiler to reserve 32-bit memory for each enum */
    FLEXCOM_USART_PARITY_INVALID = 0xFFFFFFFF

} FLEXCOM_USART_PARITY;

typedef enum
{
    FLEXCOM_USART_STOP_1_BIT = FLEX_US_MR_NBSTOP_1_BIT,
    FLEXCOM_USART_STOP_1_5_BIT = FLEX_US_MR_NBSTOP_1_5_BIT,
    FLEXCOM_USART_STOP_2_BIT = FLEX_US_MR_NBSTOP_2_BIT,

    /* Force the compiler to reserve 32-bit memory for each enum */
    FLEXCOM_USART_STOP_INVALID = 0xFFFFFFFF

} FLEXCOM_USART_STOP;

typedef struct
{
    uint32_t baudRate;
    FLEXCOM_USART_DATA dataWidth;
    FLEXCOM_USART_PARITY parity;
    FLEXCOM_USART_STOP stopBits;

} FLEXCOM_USART_SERIAL_SETUP;


// *****************************************************************************
/* Callback Function Pointer

   Summary:
    Defines the data type and function signature for the FLEXCOM USART
    peripheral callback function.

   Description:
    This data type defines the function signature for the FLEXCOM USART
    peripheral callback function. The FLEXCOM USART peripheral will call back
    the client's function with this signature when the FLEXCOM USART buffer
    event has occurred.

   Precondition:
    FLEXCOMx_USART_Initialize must have been called for the given FLEXCOM USART
    peripheral instance and FLEXCOMx_USART_WriteCallbackRegister or 
    FLEXCOMx_USART_ReadCallbackRegister must have been called to set the
    function to be called.

   Parameters:
    context  - Allows the caller to provide a context value (usually a pointer
    to the callers context for multi-instance clients).

   Returns:
    None.

   Example:
    <code>
    // Data tracking what each of my instances is doing.
    MY_DATA myData[2];

    void MyUsartCallback ( uintptr_t context )
    {
        MY_DATA *myData = (MY_DATA *)context;

        if(FLEXCOM_USART_ERROR_NONE != FLEXCOMx_USART_ErrorGet())
        {
            //Handle error case
        }
        else
        {
            //Transfer completed successfully
        }
    }

    FLEXCOMx_USART_WriteCallbackRegister(MyUsartCallback, &myData[0]);
    </code>

   Remarks:
    None.
*/

typedef void (*FLEXCOM_USART_CALLBACK)( uintptr_t context );


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
    void FLEXCOMx_USART_Initialize( void )

   Summary:
    Initializes given instance of the FLEXCOM USART peripheral.

   Description:
    This function initializes the given instance of the FLEXCOM USART
    peripheral as configured by the user from within the MCC.

   Precondition:
    None.

   Parameters:
    None.

   Returns:
    None.

   Example:
    <code>
    FLEXCOMx_USART_Initialize();
    </code>

   Remarks:
    Stops the FLEXCOM USART if it was already running and reinitializes it.
*/

void FLEXCOMx_USART_Initialize( void );


// *****************************************************************************
// *****************************************************************************
// Section: Transaction (Write/Read) Request Interface
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Function:
    bool FLEXCOMx_USART_Write( void *buffer, const size_t size )

   Summary:
    Submits a write buffer to the given FLEXCOM USART peripheral to transfer.

   Description:
    This function submits a write buffer to the FLEXCOM USART peripheral to
    transfer. The behavior of this function call will vary based on the mode
    selected within MCC.

    If the peripheral is configured for the interrupt mode, this function call
    is always non-blocking. Call to this function submits the buffer and the
    size to the peripheral library and returns immediately. User can check the
    transfer status through callback mechanism.

    If the peripheral is configured for the non-interrupt mode, this
    function call returns only after requested size is transferred.

   Precondition:
    FLEXCOMx_USART_Initialize must have been called for the associated
    FLEXCOM USART instance.

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

    if(false != FLEXCOMx_USART_Write(&myData, COUNT))
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

bool FLEXCOMx_USART_Write( void *buffer, const size_t size );

// *****************************************************************************
/* Function:
    void FLEXCOMx_USART_WriteByte(uint8_t data)

   Summary:
    Submits a byte of data to the given FLEXCOM USART peripheral to transfer.

   Description:
    This function submits a byte of data to the FLEXCOM USART peripheral to transfer.
    This Function is available only in non-interrupt mode.

   Precondition:
    FLEXCOMx_USART_Initialize must have been called for the associated FLEXCOM USART instance.

   Parameters:
    data - Data byte to be transferred.

   Returns:
    None

  Example:
    <code>
    //Example to use in non-interrupt mode
    uint8_t myData = 0xAA;

    FLEXCOMx_USART_WriteByte(myData)

    </code>

  Remarks:
    None.
*/

void FLEXCOMx_USART_WriteByte(uint8_t data);

// *****************************************************************************
/* Function:
    bool FLEXCOMx_USART_Read( void *buffer, const size_t size )

   Summary:
    Submits a read buffer to the given FLEXCOM USART peripheral to process.

   Description:
    This function submits a read buffer to the FLEXCOM USART peripheral to
    process. The behavior of this function call will vary based on the mode
    selected within MCC.

    If the peripheral is configured for the interrupt mode, this function call
    is always non-blocking. Call to this function submits the buffer and the
    size to the peripheral library and returns immediately. User can check the
    transfer status through callback mechanism.

    If the peripheral is configured for the non-interrupt mode, this
    function call returns only after requested size is processed.

   Precondition:
    FLEXCOMx_USART_Initialize must have been called for the associated 
    FLEXCOM USART instance.

   Parameters:
    buffer - Pointer to the user buffer.
    size - Number of bytes to be transferred.

   Returns:
    Read request status.
    True - Read request was successful.
    False - Read request has failed.

  Example:
    <code>
    //Example to use in non-interrupt
    char rxData[COUNT] = {}; //COUNT is expected size

    if(false != FLEXCOMx_USART_Read(&rxData, COUNT))
    {
        //The transfer is completed
    }
    else
    {
        //Read Failed
    }
    </code>

  Remarks:
    None.
*/

bool FLEXCOMx_USART_Read( void *buffer, const size_t size );

// *****************************************************************************
/* Function:
    uint8_t FLEXCOMx_USART_ReadByte( void )

   Summary:
    Submits request to read a byte of data to the given FLEXCOM USART peripheral.

   Description:
    This function submits request to read a byte of data to the given FLEXCOM USART peripheral.
    This Function is available only in non-interrupt mode.

   Precondition:
    FLEXCOMx_USART_Initialize must have been called for the associated FLEXCOM USART instance.

   Parameters:
    None

   Returns:
    Read byte.

  Example:
    <code>
    //Example to use in non-interrupt
    uint8_t rxData;

    if(FLEXCOMx_USART_ReceiverIsReady() == true)
    {
        rxData = FLEXCOMx_USART_ReadByte();
    }
    </code>

  Remarks:
    None.
*/

uint8_t FLEXCOMx_USART_ReadByte( void );

// *****************************************************************************
// *****************************************************************************
// Section: Transaction (Write/Read) Status Interface
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Function:
    bool FLEXCOMx_USART_WriteIsBusy( void )

   Summary:
    Returns the write request status associated with the given FLEXCOM USART
    peripheral instance.

   Description:
    This function returns the write request status associated with the given
    FLEXCOM USART peripheral instance.

    This function is available only in interrupt or non-blocking mode of
    operation.

   Precondition:
    FLEXCOMx_USART_Initialize must have been called for the associated
    FLEXCOM USART instance.

   Parameters:
    None.

   Returns:
    Status of Write request.
    True - USART is busy in processing the previous write request.
    False - USART is free and ready to accept the new write request.

  Example:
    <code>
    if(true == FLEXCOMx_USART_WriteIsBusy())
    {
        //FLEXCOM USART is currently processing the previous write request.
        //Wait to submit new request.
    }
    </code>

  Remarks:
    None.
*/

bool FLEXCOMx_USART_WriteIsBusy( void );


// *****************************************************************************
/* Function:
    bool FLEXCOMx_USART_ReadIsBusy( void )

   Summary:
    Returns the read request status associated with the given FLEXCOM USART
    peripheral instance.

   Description:
    This function returns the read request status associated with the given
    FLEXCOM USART peripheral instance.

    This function is available only in interrupt or non-blocking mode of
    operation.

   Precondition:
    FLEXCOMx_USART_Initialize must have been called for the associated
    FLEXCOM USART instance.

   Parameters:
    None.

   Returns:
    Status of Read request.
    True - USART is busy in processing the previous read request.
    False - USART is free and ready to accept the new read request.

  Example:
    <code>
    if(true == FLEXCOMx_USART_ReadIsBusy())
    {
        //USART is currently processing the previous read request.
        //Wait to submit new request.
    }
    </code>

  Remarks:
    None.
*/

bool FLEXCOMx_USART_ReadIsBusy( void );


// *****************************************************************************
/* Function:
    size_t FLEXCOMx_USART_WriteCountGet( void )

   Summary:
    Returns the count of number of bytes processed for a given FLEXCOM USART
    write operation.

   Description:
    This function returns the count of number of bytes processed for a given
    FLEXCOM USART write operation.

    This function is available only in interrupt or non-blocking mode of
    operation.

   Precondition:
    FLEXCOMx_USART_Initialize must have been called for the associated
    FLEXCOM USART instance.

   Parameters:
    None.

   Returns:
    Count of bytes completed/processed from the current Transmit buffer.
    This Function will return -1 if there is any error.

  Example:
    <code>
    size_t count; //COUNT_EXPECTED is the expected Transmit count value

    count = FLEXCOMx_USART_WriteCountGet();

    if(COUNT_EXPECTED > count)
    {
        //More bytes are expected to transmit, wait
    }
    </code>

  Remarks:
    This function resets the write count every time a new transfer is submitted.
*/

size_t FLEXCOMx_USART_WriteCountGet( void );


// *****************************************************************************
/* Function:
    size_t FLEXCOMx_USART_ReadCountGet( void )

   Summary:
    Returns the count of number of bytes processed for a given FLEXCOM USART
    read operation.

   Description:
    This function returns the count of number of bytes processed for a given
    FLEXCOM USART read operation.

    This function is available only in interrupt or non-blocking mode of
    operation.

   Precondition:
    FLEXCOMx_USART_Initialize must have been called for the associated
    FLEXCOM USART instance.

   Parameters:
    None.

   Returns:
    Count of bytes completed/processed to the current Receive buffer.
    This Function will return -1 if there is any error.

  Example:
    <code>
    size_t count; //COUNT_EXPECTED is the expected Receive count value

    count = FLEXCOMx_USART_ReadCountGet();

    if(COUNT_EXPECTED > count)
    {
        //More bytes are expected, wait
    }
    </code>

  Remarks:
    This function resets the read count every time a new transfer is submitted.
*/

size_t FLEXCOMx_USART_ReadCountGet( void );

// *****************************************************************************
// *****************************************************************************
// Section: Peripheral (Write/Read) Status Interface
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Function:
    void FLEXCOMx_USART_Sync( void )

   Summary:
    This Function busy waits unitll all transmit requests are completed.

   Description:
    This function is available only in non-interrupt mode of operation.
    It can be used to busy wait untill transmit fifo is empty.

   Precondition:
    FLEXCOMx_USART_Initialize must have been called for the associated FLEXCOM USART instance.

   Parameters:
    None.

   Returns:
    None

  Example:
    <code>
        FLEXCOMx_USART_Sync();
    </code>

  Remarks:
    None
*/

void FLEXCOMx_USART_Sync( void );

// *****************************************************************************
/* Function:
    bool FLEXCOMx_USART_TransmitterIsReady( void )

   Summary:
    Returns the hardware status of the FLEXCOM USART Transmitter.

   Description:
    This function returns the hardware status associated with the Transmit
    hardware FIFO of the given FLEXCOM USART peripheral instance.

    When Transmitter is ready, user can submit data to transmit.

    This function is available only in non-interrupt mode of operation. And can
    be used to achieve non-blocking behavior of write request. User has to check
    the Transmit ready status by calling this function and can submit write
    request for the buffer size of 1.

   Precondition:
    FLEXCOMx_USART_Initialize must have been called for the associated 
    FLEXCOM USART instance.

   Parameters:
    None.

   Returns:
    true - Transmit hardware FIFO has empty space to accept the data.
    false - Transmit hardware FIFO is full.

  Example:
    <code>
    if(true == FLEXCOMx_USART_TransmitterIsReady())
    {
        // Empty space is available in Transmitter FIFO, hence can write a byte
        FLEXCOMx_USART_Write(&txData, 1);
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

bool FLEXCOMx_USART_TransmitterIsReady( void );


// *****************************************************************************
/* Function:
    bool FLEXCOMx_USART_ReceiverIsReady( void )

   Summary:
    Returns the hardware status of the FLEXCOM USART Receiver.

   Description:
    This function returns the hardware status associated with the Receive
    hardware FIFO of the given FLEXCOM USART peripheral instance.

    When Receiver is ready, user can read the available data.

    This function is available only in non-interrupt mode of operation. And can
    be used to achieve non-blocking behavior of read request. User has to check
    the Receiver ready status by calling this function and can submit a read
    request for the buffer size of 1.

   Precondition:
    FLEXCOMx_USART_Initialize must have been called for the associated
    FLEXCOM USART instance.

   Parameters:
    None.

   Returns:
    true - Receive hardware FIFO has at least one data available to read.
    false - Receive hardware FIFO is empty.

  Example:
    <code>
    if(true == FLEXCOMx_USART_ReceiverIsReady())
    {
        // At least one data is available in Receive FIFO, hence can read a byte
        FLEXCOMx_USART_Read(&rxData, 1);
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

bool FLEXCOMx_USART_ReceiverIsReady( void );


// *****************************************************************************
/* Function:
    FLEXCOM_USART_ERROR FLEXCOMx_USART_ErrorGet( void )

   Summary:
    Gets the error of the given FLEXCOM USART peripheral instance.

   Description:
    This function returns the errors associated with the given FLEXCOM USART
    peripheral instance. The call to this function also clears all the
    associated errors.

   Precondition:
    FLEXCOMx_USART_Initialize must have been called for the associated
    FLEXCOM USART instance.

   Parameters:
    None.

   Returns:
    Errors occurred as listed by FLEXCOM_USART_ERROR.
    This function reports multiple FLEXCOM USART errors if occurred.

  Example:
    <code>
    if (FLEXCOM_USART_ERROR_OVERRUN & FLEXCOMx_USART_ErrorGet())
    {
        //Errors are cleared by the API call, take respective action
        //for the overrun error case.
    }
    </code>

  Remarks:
    FLEXCOM USART errors are normally associated with the receiver. Hence,
    it is recommended to use this function in receive context only.
*/

FLEXCOM_USART_ERROR FLEXCOMx_USART_ErrorGet( void );


// *****************************************************************************
/* Function:
    void FLEXCOMx_USART_SerialSetup(FLEXCOM_USART_SERIAL_SETUP * setup, uint32_t srcClkFreq)

   Summary:
    Sets the FLEXCOM USART serial communication settings dynamically.

   Description:
    This function sets the FLEXCOM USART serial communication settings
    dynamically.

   Precondition:
    FLEXCOMx_USART_Initialize must have been called for the associated
    FLEXCOM USART instance. The FLEXCOM USART transmit or receive transfer
    status should not be busy.

   Parameters:
    setup - Pointer to the structure containing the serial setup.
    srcClkFreq - FLEXCOM USART Peripheral Clock Source Frequency.

   Returns:
    true - Serial setup was updated Successfully.
    false - Failure while updating serial setup.

   Example:
    <code>
    FLEXCOM_USART_SERIAL_SETUP setup = {
            115200,
            FLEXCOM_USART_DATA_8_BIT,
            FLEXCOM_USART_PARITY_ODD,
            FLEXCOM_USART_STOP_1_BIT
        };

    FLEXCOMx_USART_SerialSetup(&setup, 0);
    </code>

   Remarks:
    srcClkFreq overrides any change in the peripheral clock frequency.
    If configured to zero PLib takes the peripheral clock frequency from MHC.
*/

bool FLEXCOMx_USART_SerialSetup( FLEXCOM_USART_SERIAL_SETUP *setup, uint32_t srcClkFreq );


// *****************************************************************************
// *****************************************************************************
// Section: Callback Interface
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Function:
    bool FLEXCOMx_USART_WriteCallbackRegister( FLEXCOM_USART_CALLBACK callback, uintptr_t context )

   Summary:
    Sets the pointer to the function (and it's context) to be called when the
    given FLEXCOM USART's write events occur.

   Description:
    This function sets the pointer to a client function to be called "back"
    when the given FLEXCOM USART's write events occur. It also passes a context
    value (usually a pointer to a context structure) that is passed into the
    function when it is called.

    This function is available only in interrupt or non-blocking mode of
    operation.

   Precondition:
    FLEXCOMx_USART_Initialize must have been called for the associated
    FLEXCOM USART instance.

   Parameters:
    callback - A pointer to a function with a calling signature defined
    by the FLEXCOM_USART_CALLBACK data type.

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

    void MyUsartCallback ( uintptr_t context )
    {
        MY_DATA *myData = (MY_DATA *)context;

        if(FLEXCOM_USART_ERROR_NONE != FLEXCOMx_USART_ErrorGet())
        {
            //Handle error case
        }
        else
        {
            //Transfer completed successfully
        }
    }

    FLEXCOMx_USART_WriteCallbackRegister(MyUsartCallback, &myData[0]);
    </code>

  Remarks:
    The context parameter is ignored if the pointer passed is NULL.
    To disable the callback function, pass a NULL for the callback parameter.
    See the FLEXCOM_USART_CALLBACK type definition for additional information.
*/

bool FLEXCOMx_USART_WriteCallbackRegister( FLEXCOM_USART_CALLBACK callback, uintptr_t context );


// *****************************************************************************
/* Function:
    bool FLEXCOMx_USART_ReadCallbackRegister( FLEXCOM_USART_CALLBACK callback, uintptr_t context )

   Summary:
    Sets the pointer to the function (and it's context) to be called when the
    given FLEXCOM USART's read events occur.

   Description:
    This function sets the pointer to a client function to be called "back"
    when the given FLEXCOM USART's read events occur. It also passes a context
    value (usually a pointer to a context structure) that is passed into the
    function when it is called.

    This function is available only in interrupt or non-blocking mode of
    operation.

   Precondition:
    FLEXCOMx_USART_Initialize must have been called for the associated
    FLEXCOM USART instance.

   Parameters:
    callback - A pointer to a function with a calling signature defined
    by the FLEXCOM_USART_CALLBACK data type.

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

    void MyUsartCallback ( uintptr_t context )
    {
        MY_DATA *myData = (MY_DATA *)context;

        if(FLEXCOM_USART_ERROR_NONE != FLEXCOMx_USART_ErrorGet())
        {
            //Handle error case
        }
        else
        {
            //Transfer completed successfully
        }
    }

    FLEXCOMx_USART_ReadCallbackRegister(MyUsartCallback, &myData[0]);
    </code>

  Remarks:
    The context parameter is ignored if the pointer passed is NULL.
    To disable the callback function, pass a NULL for the callback parameter.
    See the FLEXCOM_USART_CALLBACK type definition for additional information.
*/

bool FLEXCOMx_USART_ReadCallbackRegister( FLEXCOM_USART_CALLBACK callback, uintptr_t context );


// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END

#endif //PLIB_FLEXCOMx_USART_H
