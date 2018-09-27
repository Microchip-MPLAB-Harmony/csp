/*******************************************************************************
  SERCOM USART PLIB Header File

  Company
    Microchip Technology Inc.

  File Name
    plib_sercom_usart.h

  Summary
    USART peripheral library interface.

  Description
    This file defines the interface to the USART peripheral library. This
    library provides access to and control of the associated peripheral
    instance.
*******************************************************************************/

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

#ifndef PLIB_SERCOMx_USART_H // Guards against multiple inclusion
#define PLIB_SERCOMx_USART_H

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

// *****************************************************************************
/* USART Errors

  Summary:
    Defines the data type for the USART peripheral errors.

  Description:
    This may be used to check the type of error occurred with the USART
    peripheral during error status.

  Remarks:
    None.
*/

typedef enum
{
    /* Error status when no error has occurred */
    USART_ERROR_NONE,

    /* Error status when parity error has occurred */
    USART_ERROR_PARITY = SERCOM_USART_STATUS_PERR_Msk,

    /* Error status when framing error has occurred */
    USART_ERROR_FRAMING = SERCOM_USART_STATUS_FERR_Msk,

    /* Error status when overrun error has occurred */
    USART_ERROR_OVERRUN = SERCOM_USART_STATUS_BUFOVF_Msk

} USART_ERROR;

// *****************************************************************************
/* USART DATA

  Summary:
    Defines the data type for the USART peripheral data.

  Description:
    This may be used to check the type of data with the USART
    peripheral during serial setup.

  Remarks:
    None.
*/

typedef enum
{
    USART_DATA_5_BIT = SERCOM_USART_CTRLB_CHSIZE(0x5),

    USART_DATA_6_BIT = SERCOM_USART_CTRLB_CHSIZE(0x6),

    USART_DATA_7_BIT = SERCOM_USART_CTRLB_CHSIZE(0x7),

    USART_DATA_8_BIT = SERCOM_USART_CTRLB_CHSIZE(0x0),

    USART_DATA_9_BIT = SERCOM_USART_CTRLB_CHSIZE(0x1),

    /* Force the compiler to reserve 32-bit memory for each enum */
    USART_DATA_INVALID = 0xFFFFFFFF

} USART_DATA;

// *****************************************************************************
/* USART PARITY

  Summary:
    Defines the data type for the USART peripheral parity.

  Description:
    This may be used to check the type of parity with the USART
    peripheral during serial setup.

  Remarks:
    None.
*/

typedef enum
{
    USART_PARITY_EVEN = 0,

    USART_PARITY_ODD = SERCOM_USART_CTRLB_PMODE_Msk,

    /* This enum is defined to set frame format only
     * This value won't be written to register
     */
    USART_PARITY_NONE = 0x2,

    /* Force the compiler to reserve 32-bit memory for each enum */
    USART_PARITY_INVALID = 0xFFFFFFFF

} USART_PARITY;

// *****************************************************************************
/* USART STOP

  Summary:
    Defines the data type for the USART peripheral stop bits.

  Description:
    This may be used to check the type of stop bits with the USART
    peripheral during serial setup.

  Remarks:
    None.
*/

typedef enum
{
    USART_STOP_1_BIT = 0,

    USART_STOP_2_BIT = SERCOM_USART_CTRLB_SBMODE_Msk,

    /* Force the compiler to reserve 32-bit memory for each enum */
    USART_STOP_INVALID = 0xFFFFFFFF

} USART_STOP;

// *****************************************************************************
/* USART Serial Configuration

  Summary:
    Defines the data type for the USART serial configurations.

  Description:
    This may be used to set the serial configurations for USART.

  Remarks:
    None.
*/

typedef struct
{
    uint32_t baudRate;

    USART_DATA dataWidth;

    USART_PARITY parity;

    USART_STOP stopBits;

} USART_SERIAL_SETUP;

// *****************************************************************************
/* Callback Function Pointer

  Summary:
    Defines the data type and function signature of the USART peripheral library
    callback function.

  Description:
    This data type defines the function signature of the USART peripheral
    callback function. The USART peripheral will call back the client's function
    with this signature when the USART buffer event has occurred.

  Precondition:
    SERCOMx_USART_Initialize must have been called for the given USART
    peripheral instance and SERCOMx_USART_CallbackRegister must have been called
    to set the function to be called.

  Parameters:
    status - Complete or error status of the USART buffer transfer.

    direction - Direction of transfer associated with the event.

    context - Allows the caller to provide a context value (usually a pointer to
    the callers context for multi-instance clients).

  Returns:
    None.

  Example:
    <code>
    // Data tracking what each of my instances is doing.
    MY_DATA myData[2];

    void MyUsartReadCallback(uintptr_t context)
    {
        // This function will be called when a USART read has completed.
    }

    void MyUsartWriteCallback(uintptr_t context)
    {
        // This function will be called when a USART write has completed.
    }

    SERCOMx_USART_ReadCallbackRegister(MyUsartReadCallback, &myData[0]);
    SERCOMx_USART_WriteCallbackRegister(MyUsartWriteCallback, &myData[1]);
    </code>

  Remarks:
    Code within the callback function will execute in an interrupt context. The
    application should avoid calling hardware blocking functions or interrupt
    in-sensitive code in this function.
*/

typedef void (*SERCOM_USART_CALLBACK)( uintptr_t context );

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
    void SERCOMx_USART_Initialize( void )

  Summary:
    Initializes given instance of the USART peripheral.

  Description:
    This function initializes the given instance of the USART peripheral as
    configured by the user from MHC.

  Precondition:
    None.

  Parameters:
    None.

  Returns:
    None.

  Example:
    <code>
    SERCOMx_USART_Initialize();
    </code>

  Remarks:
    Stops the USART if it was already running and reinitializes it.
*/

void SERCOMx_USART_Initialize( void );

// *****************************************************************************
/* Function:
    bool SERCOMx_USART_SerialSetup(USART_SERIAL_SETUP * serialSetup,
                                                         uint32_t clkFrequency)

  Summary:
    Sets up serial configurations for USART peripheral.

  Description:
    This function sets all the serial configurations of the peripheral.  It
    provides run-time interface to configure the baud, parity, stop bits and
    data character size parameters of the serial connection.

    Calling this function when a serial communication is in progress can disrupt
    the communication. The caller should be ensure that there is no serial
    communication in progress.

    In case of success, the function will update all parameters specified in the
    serialSetup parameter, even if some parameter may have not changed since a
    previous call to this function. In case of failure, all parameter stay
    unchanged.

  Precondition:
    SERCOMx_USART_Initialize must have been called for the associated USART
    instance.

  Parameters:
    clkFrequency - Input clock frequency to the Baud Rate Generator.

    serialSetup  - Pointer with serial configuration details.

  Returns:
    true - if serial configuration was successful.

    false - if the specified serial congfiguration could not be supported. This,
    for example, could happen if the requested baud is not supported.

  Remarks:
    None.
*/

bool SERCOMx_USART_SerialSetup( USART_SERIAL_SETUP * serialSetup, uint32_t clkFrequency );

// *****************************************************************************
/* Function:
    bool SERCOMx_USART_Write( void *buffer, const size_t size )

  Summary:
    Submits a write buffer to the given USART peripheral to transfer.

  Description:
    This function submits a write buffer to be transmitted by the USART
    peripheral.  The function behavior will vary based on the mode selected
    within MHC.

    If the peripheral is configured for interrupt mode operation, this function
    call is always non-blocking. A call to this function submits the buffer and
    the size to the peripheral library and returns immediately. The transfer
    completion status can either be checked through the callback mechanism or by
    calling the SERCOMx_USART_WriteIsBusy() function. The completion success of
    the operation can be obtained by calling the SERCOMx_USART_ErrorGet()
    function.

    If the SERCOMx_USART_ErrorGet() function returns no error, then this means
    that the requested number of bytes have been processed. If the function
    returns some error, the SERCOMx_USART_WriteCountGet() function can be called
    to know the number of bytes that were transmitted till the error occurred.

    If the peripheral is configured for the non-interrupt mode, this function
    call returns only after the requested size of bytes are transmitted.

  Precondition:
    SERCOMx_USART_Initialize must have been called for the associated USART
    instance.

  Parameters:
    buffer - Pointer to the user buffer. This contains the data to be
    transferred.

    size   - Number of bytes to be transferred.

  Returns:
    true - if the request was placed successfully (in interrupt mode) or if the
    specified number of bytes were transferre or if the size requested is 0.

    false - if the arguments are not valid or if the peripheral is busy with
    another request.

  Example:
    <code>
    // Example of use in non-interrupt mode. The function call is blocking.

    char myData[COUNT] = {"hello"}; //COUNT is user message size
    if(false != SERCOMx_USART_Write(&myData, COUNT))
    {
        //The transfer is completed
    }
    else
    {
        //Invalid arguments
    }

    // Example of use in interrupt mode. The function call in not blocking.

    volatile bool writeComplete = false;
    size_t transmittedBytes = 0;
    char myData[COUNT] = {"hello"}; //COUNT is user message size

    void MyUsartWriteCallback(uintptr_t context)
    {
        volatile bool * status = (volatile bool *)(context);
        status = true;
    }

    SERCOMx_USART_WriteCallbackRegister(MyUsartWriteCallback, &writeComplete);
    SERCOMx_USART_Write(&myData, COUNT);

    // Write complete is updated in the callback function.
    while(writeComplete == false);

    // The write has completed. Check if there were any errors.
    if(SERCOMx_USART_ErrorGet() != USART_ERROR_NONE)
    {
        transmittedBytes = SERCOMx_USART_WriteCountGet();
        // Handle the error.
    }

    // Example of use in interrupt mode with the
    // SERCOMx_USART_WriteIsBusy() function.

    char myData[COUNT] = {"hello"}; //COUNT is user message size
    SERCOMx_USART_Write(&myData, COUNT);

    // Wait till the write is complete.
    while(SERCOMx_USART_WriteIsBusy() == true);

    // The write has completed. Check if there were any errors.
    if(SERCOMx_USART_ErrorGet() != USART_ERROR_NONE)
    {
        // Handle the error.
    }

    </code>

  Remarks:
    Configuring the library for non-interrupt mode and calling a blocking
    function can affect the operation of other polled components in the
    application.
*/

bool SERCOMx_USART_Write( void *buffer, const size_t size );

// *****************************************************************************
/* Function:
    bool SERCOMx_USART_Read( void *buffer, const size_t size )

  Summary:
    Submits a read buffer to the given USART peripheral to process.

  Description:
    This function submits a read buffer to the USART peripheral to process.  The
    behavior of this function  will vary based on the mode selected within MHC.

    If the peripheral is configured for interrupt mode operation, this function
    call is always non-blocking. A call to this function submits the buffer and
    the size to the peripheral library and returns immediately. The transfer
    completion status can either be checked through the callback mechanism or by
    calling the SERCOMx_USART_ReadIsBusy() function. The success of the
    operation can be obtained by calling the SERCOMx_USART_ErrorGet() function.

    If the SERCOMx_USART_ErrorGet() function returns no error, then this means
    that the requested number of bytes have been processed. If the function
    returns some error, the SERCOMx_USART_ReadCountGet() function can be called
    to know the number of bytes that were received till the error occurred.

    If the peripheral is configured for the non-interrupt mode, this function
    call returns only after the requested size of bytes are received.

  Precondition:
    SERCOMx_USART_Initialize must have been called for the associated USART
    instance.

  Parameters:
    buffer - Pointer to the user buffer where receieved data will be placed.

    size - Number of bytes to be received.

  Returns:
    true - if the Read transaction is successful or if the requested size is 0.

    false - if the arguments are not valid or if the device is busy or if an
    error occurred while receiving data.

  Example:
    <code>
    //Example to use in polled and blocking mode
    char myData[COUNT] = {"hello"}; //COUNT is user message size
    USART_ERROR error = USART_ERROR_NONE;

    if(false != SERCOMx_USART_Read(&myData, COUNT))
    {
        //The transfer is completed
    }
    else
    {
        error = SERCOMx_USART_ErrorGet();
    }

    // Example of use in interrupt mode. The function call in not blocking.

    volatile bool readComplete = false;
    size_t receivedBytes = 0;
    char myData[COUNT] = {"hello"}; //COUNT is user message size

    void MyUsartReadCallback(uintptr_t context)
    {
        volatile bool * status = (volatile bool *)(context);
        status = true;
    }

    SERCOMx_USART_ReadCallbackRegister(MyUsartReadCallback, &readComplete);
    SERCOMx_USART_Read(&myData, COUNT);

    // Read complete is updated in the callback function.
    while(readComplete == false);

    // The read has completed. Check if there were any errors.
    if(SERCOMx_USART_ErrorGet() != USART_ERROR_NONE)
    {
        receivedBytes = SERCOMx_USART_ReadCountGet();
        // Handle the error.
    }

    // Example of use in interrupt mode with the
    // SERCOMx_USART_ReadIsBusy() function.

    char myData[COUNT] = {"hello"}; //COUNT is user message size
    SERCOMx_USART_Read(&myData, COUNT);

    // Wait till the read is complete.
    while(SERCOMx_USART_ReadIsBusy() == true);

    // The read has completed. Check if there were any errors.
    if(SERCOMx_USART_ErrorGet() != USART_ERROR_NONE)
    {
        // Handle the error.
    }

    </code>

  Remarks:
    Configuring the library for non-interrupt mode and calling a blocking
    function can affect the operation of other polled components in the
    application.
*/

bool SERCOMx_USART_Read( void *buffer, const size_t size );

// *****************************************************************************
// *****************************************************************************
// Section: Transaction (Write/Read) Status Interface
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Function:
    bool SERCOMx_USART_WriteIsBusy( void )

  Summary:
    Returns the write request status associated with the given USART peripheral
    instance.

  Description:
    This function returns the write request status associated with the given
    USART peripheral instance. It can be used to check the completion status of
    the SERCOMx_USART_Write() function when the library is configured for
    interrupt (non-blocking) mode. In that, the function can be used as an
    alternative to using a callback function to check for completion.

    This function is available only in interrupt or non-blocking mode of
    operation.

  Precondition:
    SERCOMx_USART_Initialize must have been called for the associated USART
    instance.

  Parameters:
    None.

  Returns:
    true - USART is busy in processing the previous write request.

    false - USART is free and ready to accept a new write request.

  Example:
    <code>

    if(true == SERCOMx_USART_WriteIsBusy())
    {
        //USART is currently processing the previous write request.
        //Wait to submit new request.
    }

    // Refer to SERCOMx_USART_Write() function code example for additional usage
    // tips.

    </code>

  Remarks:
    None.
*/

bool SERCOMx_USART_WriteIsBusy ( void );

// *****************************************************************************
/* Function:
    bool SERCOMx_USART_ReadIsBusy( void )

  Summary:
    Returns the read request status associated with the given USART peripheral
    instance.

  Description:
    This function returns the read request status associated with the given
    USART peripheral instance. It can be used to check the completion status of
    the SERCOMx_USART_Read() function when the library is configured for
    interrupt (non-blocking) mode. In that, the function can be used as an
    alternative to using a callback function to check for completion.

    This function is available only in interrupt or non-blocking mode of
    operation.

  Precondition:
    SERCOMx_USART_Initialize must have been called for the associated USART
    instance.

  Parameters:
    None.

  Returns:
    true - if USART is busy in processing the previous read request.

    false - if USART is free and ready to accept the new read request.

  Example:
    <code>
    if(true == SERCOMx_USART_ReadIsBusy())
    {
        //USART is currently processing the previous read request.
        //Wait to submit new request.
    }

    // Refer to SERCOMx_USART_Read() function code example for additional usage
    // tips.

    </code>

  Remarks:
    None.
*/

bool SERCOMx_USART_ReadIsBusy ( void );

// *****************************************************************************
/* Function:
    size_t SERCOMx_USART_WriteCountGet( void )

  Summary:
    Gets the byte count of processed bytes for a given USART read operation.

  Description:
    This function gets the count of processed bytes for an og-going or last
    completed USART Transmit operation. This function is only available in
    interrupt non-blocking mode. This function can be used to track the progress
    of the non-blocking transmit operation.

  Precondition:
    SERCOMx_USART_Initialize must have been called for the associated USART
    instance.

  Parameters:
    None.

  Returns:
    Returns count of bytes currently completed/processed from the current
    Transmit buffer for interrupt non-blocking mode.

  Example:
    <code>
    size_t count; //COUNT_EXPECTED is the expected Transmit count value

    count = SERCOMx_USART_WriteCountGet();

    if(COUNT_EXPECTED > count)
    {
        //More bytes are expected to transmit, wait
    }
    </code>

  Remarks:
    This write count gets reset every time the SERCOMx_USART_Write() function is
    called.
*/

size_t SERCOMx_USART_WriteCountGet( void );

// *****************************************************************************
/* Function:
    size_t SERCOMx_USART_ReadCountGet( void )

  Summary:
    Gets the byte count of processed bytes for a given USART read operation.

  Description:
    This function gets the count of processed bytes for an og-going or last
    completed USART Read operation. This function is only available in interrupt
    non-blocking mode. This function can be used to track the progress of the
    non-blocking read operation. In case of an error, this function can be used
    to track the number of bytes that were received before the error occurred.

  Precondition:
    SERCOMx_USART_Initialize must have been called for the associated USART
    instance.

  Parameters:
    None.

  Returns:
    Returns count of bytes completed/processed to the current Receive buffer.

  Example:
    <code>

    // This shows an example in interrupt non-blocking mode.

    size_t count;
    char buffer[COUNT_EXPECTED];

    SERCOMx_USART_Read(buffer, COUNT_EXPECTED);

    count = SERCOMx_USART_ReadCountGet();

    if(COUNT_EXPECTED > count)
    {
        //More bytes are expected, wait
    }

    </code>

  Remarks:
    This function resets the read count every time a new transfer is submitted.
*/

size_t SERCOMx_USART_ReadCountGet( void );

// *****************************************************************************
/* Function:
    bool SERCOMx_USART_TransmitterIsReady( void )

  Summary:
    Returns the hardware status of the USART Transmitter.

  Description:
    This function returns the hardware status associated with the transmit
    hardware FIFO of the given USART peripheral instance. When the transmitter
    is ready, user can submit data to be transmitted.

    This function is available only in non-interrupt mode of operation. It can
    be used to achieve non-blocking behavior of write request in the
    non-interrupt mode. If non-blocking behavior is desired, this function
    should be called to check if the transmitter is ready and then the
    SERCOMx_USART_Write() function should be called with a buffer size of 1.

  Precondition:
    SERCOMx_USART_Initialize must have been called for the associated USART
    instance.

  Parameters:
    None.

  Returns:
    true - if transmit hardware FIFO has empty space to accept data.

    false - if transmit hardware FIFO is full.

  Example:
    <code>
    if(true == SERCOMx_USART_TransmitterIsReady())
    {
        // Empty space is available in Transmitter FIFO, hence can write a byte
        SERCOMx_USART_Write(&txData, 1);
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

bool SERCOMx_USART_TransmitterIsReady( void );

// *****************************************************************************
/* Function:
    bool SERCOMx_USART_ReceiverIsReady( void )

  Summary:
    Returns the hardware status of the USART Receiver.

   Description:
    This function returns the hardware status associated with the Receive
    hardware FIFO of the given USART peripheral instance. When Receiver is
    ready, user can read the available data.

    This function is available only in non-interrupt mode of operation. It can
    be used to achieve non-blocking behavior of SERCOMx_USART_Read() function
    even if the library is configured for blocking behavior. If this function
    returns true, calling the SERCOMx_USART_Read() function with a byte count
    of 1 will result in non-blocking behavior.

  Precondition:
    SERCOMx_USART_Initialize must have been called for the associated USART
    instance.

  Parameters:
    None.

  Returns:
    true - if receive hardware FIFO has at least one data available to read.

    false - if receive hardware FIFO is empty.

  Example:
    <code>
    if(true == SERCOMx_USART_ReceiverIsReady())
    {
        // At least one data is available in Receive FIFO, hence can read a byte
        SERCOMx_USART_Read(&rxData, 1);
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

bool SERCOMx_USART_ReceiverIsReady( void );

// *****************************************************************************
/* Function:
    USART_ERROR SERCOMx_USART_ErrorGet( void )

  Summary:
    Gets the error of the given USART peripheral instance.

  Description:
    This function returns the errors associated with the given USART peripheral
    instance. Multiple error conditions may be active. The function return value
    should be matched against each member of the USART_ERROR enumeration to
    handle all error cases. Calling the SERCOMx_USART_Read or
    SERCOMx_USART_Write functions will clear the erorrs. Hence error handling
    must be perfomed before these functions are called again.

  Precondition:
    SERCOMx_USART_Initialize must have been called for the associated USART
    instance.

  Parameters:
    None.

  Returns:
    Returns errors occurred as listed by USART_ERROR enumeration.

  Example:
    <code>
    if(USART_ERROR_NONE != SERCOMx_USART_ErrorGet())
    {
        if (USART_ERROR_OVERRUN & SERCOMx_USART_ErrorGet())
        {
            // Handle overrun error.
        }

        if(USART_ERROR_PARITY & SERCOMx_USART_ErrorGet())
        {
            // Handle parity error.
        }
    }
    </code>

  Remarks:
    USART errors are normally associated with the receiver. Hence, it is
    recommended to use this function in receive context only.
*/

USART_ERROR SERCOMx_USART_ErrorGet( void );

// *****************************************************************************
// *****************************************************************************
// Section: Callback Interface
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Function:
    void SERCOMx_USART_WriteCallbackRegister( SERCOM_USART_CALLBACK callback,
                                                        uintptr_t context )

  Summary:
    Sets the pointer to the function (and it's context) to be called when the
    given USART's write events occur.

  Description:
    This function sets the pointer to a client function to be called "back" when
    the given USART's write events occur. It also passes a context value
    (usually a pointer to a context structure) that is passed into the function
    when it is called.

    This function is available only in interrupt or non-blocking mode of
    operation.

  Precondition:
    SERCOMx_USART_Initialize must have been called for the associated USART
    instance.

  Parameters:
    callback - Pointer to the function to be called when the
    SERCOMx_USART_Write() function has completed. Setting this to NULL will
    disable the callback feature.

    context  - A value (usually a pointer) passed (unused) into the function
    identified by the callback parameter.

  Returns:
    None.

  Example:
    <code>
    // Data tracking what each of my instances is doing.
    MY_DATA myData[2];

    void MyUsartCallback ( uintptr_t context )
    {
        MY_DATA *myData = (MY_DATA *)context;

        if(USART_ERROR_NONE != SERCOMx_USART_ErrorGet())
        {
            //Handle error case
        }
        else
        {
            //Transfer completed successfully
        }
    }

    SERCOMx_USART_WriteCallbackRegister(MyUsartCallback, &myData[0]);
    </code>

  Remarks:
    The context parameter is ignored if the pointer passed is NULL.  To disable
    the callback function, pass a NULL for the callback parameter.  See the
    USART_CALLBACK type definition for additional information.
*/

void SERCOMx_USART_WriteCallbackRegister( SERCOM_USART_CALLBACK callback , uintptr_t context );

// *****************************************************************************
/* Function:
    void SERCOMx_USART_ReadCallbackRegister( SERCOM_USART_CALLBACK callback,
                                                        uintptr_t context )

  Summary:
    Sets the pointer to the function (and it's context) to be called when the
    given USART's read events occur.

  Description:
    This function sets the pointer to a client function to be called "back" when
    the given USART's read events occur. It also passes a context value (usually
    a pointer to a context structure) that is passed into the function when it
    is called.

    This function is available only in interrupt or non-blocking mode of
    operation.

  Precondition:
    SERCOMx_USART_Initialize must have been called for the associated USART
    instance.

  Parameters:
    callback - Pointer to the function that will be called when
    SERCOMx_USART_Read() function has completed. Setting this to NULl will
    disable the callback feature.

    context - A value (usually a pointer) passed (unused) into the function
    identified by the callback parameter.

  Returns:
    None.

  Example:
    <code>
    // Data tracking what each of my instances is doing.
    MY_DATA myData[2];

    void MyUsartCallback ( uintptr_t context )
    {
        MY_DATA *myData = (MY_DATA *)context;

        if(USART_ERROR_NONE != SERCOMx_USART_ErrorGet())
        {
            //Handle error case
        }
        else
        {
            //Transfer completed successfully
        }
    }

    SERCOMx_USART_ReadCallbackRegister(MyUsartCallback, &myData[0]);
    </code>

  Remarks:
    The context parameter is ignored if the pointer passed is NULL.
    To disable the callback function, pass a NULL for the callback parameter.
    See the USART_CALLBACK type definition for additional information.
*/

void SERCOMx_USART_ReadCallbackRegister( SERCOM_USART_CALLBACK callback , uintptr_t context );

// *****************************************************************************
/* Function:
    int SERCOMx_USART_ReadByte( void )

  Summary:
    Submits request to read a byte of data to the given USART peripheral.

  Description:
    This function submits request to read a byte of data to the given USART
    peripheral. This Function is available only in non-interrupt mode.

  Precondition:
    SERCOMx_USART_Initialize must have been called for the associated USART
    instance.

  Parameters:
    None

  Returns:
    Read byte.

  Example:
    <code>
    //Example to use in non-interrupt
    char rxData;

    if(SERCOMx_USART_ReceiverIsReady() == true)
    {
        rxData = SERCOMx_USART_ReadByte();
    }
    </code>

  Remarks:
    None.
*/

int SERCOMx_USART_ReadByte( void );

// *****************************************************************************
/* Function:
    void SERCOMx_USART_WriteByte( int data )

  Summary:
    Submits a byte of data to the given USART peripheral to transfer.

  Description:
    This function submits a byte of data to the USART peripheral to transfer.
    This Function is available only in non-interrupt mode.

  Precondition:
    SERCOMx_USART_Initialize must have been called for the associated USART
    instance.

  Parameters:
    data - Data byte to be transferred.

  Returns:
    None

  Example:
    <code>
    //Example to use in non-interrupt mode
    char myData = 0xAA;

    SERCOMx_USART_WriteByte(&myData)

    </code>

  Remarks:
    None.
*/

void SERCOMx_USART_WriteByte( int data );

// *****************************************************************************
/* Function:
    uint32_t SERCOMx_USART_FrequencyGet( void )

  Summary:
    Provides the given SERCOM peripheral frequency.

  Description:
    This function provides the frequency at which the given SERCOM operates.

  Precondition:
    SERCOMx_USART_Initialize must have been called for the associated USART
    instance.

  Parameters:
    None.

  Returns:
    The frequency (in Hz) at which the timer's counter increments.

  Example:
    <code>
    uint32_t frequency = 0;

    SERCOMx_USART_Initialize();
    frequency = SERCOMx_USART_FrequencyGet();
    </code>

  Remarks:
    None.
*/

uint32_t SERCOMx_USART_FrequencyGet( void );

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility
    }
#endif
// DOM-IGNORE-END

#endif //PLIB_SERCOMx_USART_H
