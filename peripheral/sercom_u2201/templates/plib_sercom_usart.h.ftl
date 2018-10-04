/*******************************************************************************
  SERCOM Universal Synchronous/Asynchrnous Receiver/Transmitter PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_${SERCOM_INSTANCE_NAME?lower_case}_usart.h

  Summary
    USART peripheral library interface.

  Description
    This file defines the interface to the USART peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

  Remarks:
    None.
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

#ifndef PLIB_${SERCOM_INSTANCE_NAME}_USART_H // Guards against multiple inclusion
#define PLIB_${SERCOM_INSTANCE_NAME}_USART_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
/* This section lists the other files that are included in this file.
*/

#include "device.h"
#include "plib_sercom_usart_common.h"

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility
extern "C" {
#endif
// DOM-IGNORE-END

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
    void ${SERCOM_INSTANCE_NAME}_USART_Initialize( void )

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
    ${SERCOM_INSTANCE_NAME}_USART_Initialize();
    </code>

  Remarks:
    Stops the USART if it was already running and reinitializes it.
*/

void ${SERCOM_INSTANCE_NAME}_USART_Initialize( void );

<#if USART_SERIAL_SETUP_ENABLE = true>
// *****************************************************************************
/* Function:
    bool ${SERCOM_INSTANCE_NAME}_USART_SerialSetup( uint32_t clkFrequency,
                                            USART_SERIAL_SETUP * serialSetup )

  Summary:
    Sets up serial configurations for USART peripheral.

  Description:
    This function sets all the serial configurations of the peripheral.  It
    provides run-time interface to configure the baud, parity, stop bits and
    data character size parameters of the serial connection.

    Calling this function when a serial communication is in progress can disrupt
    the communication. The caller should be ensure that there is no serial
    communication in progress.

    The function will update all parameters specified in the serialSetup
    parameter, even if some parameter may have not changed since a previous call
    to this function.

  Precondition:
    ${SERCOM_INSTANCE_NAME}_USART_Initialize must have been called for the
    associated USART instance.

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

bool ${SERCOM_INSTANCE_NAME}_USART_SerialSetup( uint32_t clkFrequency,
                                    USART_SERIAL_SETUP * serialSetup );
</#if>

<#if USART_TX_ENABLE = true>
// *****************************************************************************
/* Function:
    bool ${SERCOM_INSTANCE_NAME}_USART_Write( void *buffer, const size_t size )

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
    calling the ${SERCOM_INSTANCE_NAME}_USART_WriteIsBusy() function. The success
    of the operation can be obtained by calling the
    ${SERCOM_INSTANCE_NAME}_USART_ErrorGet() function.

    If the ${SERCOM_INSTANCE_NAME}_USART_ErrorGet() function returns no error,
    then this means that the requested number of bytes have been processed. If
    the function returns some error, the SERCOMx_USART_WriteCountGet() function
    can be called to know the number of bytes that were transmitted till the
    error occurred.

    If the peripheral is configured for the non-interrupt mode, this function
    call returns only after the requested size of bytes are transmitted.

  Precondition:
    ${SERCOM_INSTANCE_NAME}_USART_Initialize must have been called for the
    associated USART instance.

  Parameters:
    buffer - Pointer to the user buffer. This contains the data to be
    transferred.

    size   - Number of bytes to be transferred.

  Returns:
    true - if the request was placed successfully (in interrupt mode) or if the
    specified number of bytes were transferred.

    false - if the arguments are not valid or if the peripheral is busy with
    another request.

  Example:
    <code>
    // Example of use in non-interrupt mode. The function call is blocking.

    char myData[COUNT] = {"hello"}; //COUNT is user message size
    if(false != ${SERCOM_INSTANCE_NAME}_USART_Write(&myData, COUNT))
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

    ${SERCOM_INSTANCE_NAME}_USART_WriteCallbackRegister(MyUsartWriteCallback,
                                                        &writeComplete);
    ${SERCOM_INSTANCE_NAME}_USART_Write(&myData, COUNT);

    // Write complete is updated in the callback function.
    while(writeComplete == false);

    // The write has completed. Check if there were any errors.
    if(${SERCOM_INSTANCE_NAME}_USART_ErrorGet() != USART_ERROR_NONE)
    {
        transmittedBytes = ${SERCOM_INSTANCE_NAME}_USART_WriteCountGet();
        // Handle the error.
    }

    // Example of use in interrupt mode with the
    // ${SERCOM_INSTANCE_NAME}_USART_WriteIsBusy() function.

    char myData[COUNT] = {"hello"}; //COUNT is user message size
    ${SERCOM_INSTANCE_NAME}_USART_Write(&myData, COUNT);

    // Wait till the write is complete.
    while(${SERCOM_INSTANCE_NAME}_USART_WriteIsBusy() == true);

    // The write has completed. Check if there were any errors.
    if(${SERCOM_INSTANCE_NAME}_USART_ErrorGet() != USART_ERROR_NONE)
    {
        // Handle the error.
    }

    </code>

  Remarks:
    Configuring the library for non-interrupt mode and calling a blocking
    function can affect the operation of other polled components in the
    application.
*/
bool ${SERCOM_INSTANCE_NAME}_USART_Write( void *buffer, const size_t size );
</#if>
<#if USART_RX_ENABLE = true>
// *****************************************************************************
/* Function:
    bool ${SERCOM_INSTANCE_NAME}_USART_Read( void *buffer, const size_t size )

  Summary:
    Submits a read buffer to the given USART peripheral to process.

  Description:
    This function submits a read buffer to the USART peripheral to process.  The
    behavior of this function  will vary based on the mode selected within MHC.

    If the peripheral is configured for interrupt mode operation, this function
    call is always non-blocking. A call to this function submits the buffer and
    the size to the peripheral library and returns immediately. The transfer
    completion status can either be checked through the callback mechanism or by
    calling the ${SERCOM_INSTANCE_NAME}_USART_ReadIsBusy() function. The success
    of the operation can be obtained by calling the
    ${SERCOM_INSTANCE_NAME}_USART_ErrorGet() function.

    If the ${SERCOM_INSTANCE_NAME}_USART_ErrorGet() function returns no error,
    then this means that the requested number of bytes have been processed. If
    the function returns some error, the
    ${SERCOM_INSTANCE_NAME}_USART_ReadCountGet() function can be called to know
    the number of bytes that were received till the error occurred.

    If the peripheral is configured for the non-interrupt mode, this function
    call returns only after the requested size of bytes are received.

  Precondition:
    ${SERCOM_INSTANCE_NAME}_USART_Initialize must have been called for the
    associated USART instance.

  Parameters:
    buffer - Pointer to the user buffer where receieved data will be placed.

    size - Number of bytes to be received.

  Returns:
    true - if the Read transaction is successful.

    false - if the arguments are not valid or if the device is busy or if an
    error occurred while receiving data.

  Example:
    <code>
    //Example to use in polled and blocking mode
    char myData[COUNT] = {"hello"}; //COUNT is user message size
    USART_ERROR error = USART_ERROR_NONE;

    if(false != ${SERCOM_INSTANCE_NAME}_USART_Read(&myData, COUNT))
    {
        //The transfer is completed
    }
    else
    {
        error = ${SERCOM_INSTANCE_NAME}_USART_ErrorGet();
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

    ${SERCOM_INSTANCE_NAME}_USART_ReadCallbackRegister(MyUsartReadCallback,
                                                        &readComplete);
    ${SERCOM_INSTANCE_NAME}_USART_Read(&myData, COUNT);

    // Read complete is updated in the callback function.
    while(readComplete == false);

    // The read has completed. Check if there were any errors.
    if(${SERCOM_INSTANCE_NAME}_USART_ErrorGet() != USART_ERROR_NONE)
    {
        receivedBytes = ${SERCOM_INSTANCE_NAME}_USART_ReadCountGet();
        // Handle the error.
    }

    // Example of use in interrupt mode with the
    // ${SERCOM_INSTANCE_NAME}_USART_ReadIsBusy() function.

    char myData[COUNT] = {"hello"}; //COUNT is user message size
    ${SERCOM_INSTANCE_NAME}_USART_Read(&myData, COUNT);

    // Wait till the read is complete.
    while(${SERCOM_INSTANCE_NAME}_USART_ReadIsBusy() == true);

    // The read has completed. Check if there were any errors.
    if(${SERCOM_INSTANCE_NAME}_USART_ErrorGet() != USART_ERROR_NONE)
    {
        // Handle the error.
    }

    </code>

  Remarks:
    Configuring the library for non-interrupt mode and calling a blocking
    function can affect the operation of other polled components in the
    application.
*/
bool ${SERCOM_INSTANCE_NAME}_USART_Read( void *buffer, const size_t size );
</#if>

// *****************************************************************************
// *****************************************************************************
// Section: Transaction (Write/Read) Status Interface
// *****************************************************************************
// *****************************************************************************

<#if USART_INTERRUPT_MODE = true>
<#if USART_TX_ENABLE = true>
// *****************************************************************************
/* Function:
    bool ${SERCOM_INSTANCE_NAME}_USART_WriteIsBusy( void )

  Summary:
    Returns the write request status associated with the given USART peripheral
    instance.

  Description:
    This function returns the write request status associated with the given
    USART peripheral instance. It can be used to check the completion status of
    the ${SERCOM_INSTANCE_NAME}_USART_Write() function when the library is
    configured for interrupt (non-blocking) mode. In that, the function can be
    used as an alternative to using a callback function to check for completion.

    This function is available only in interrupt or non-blocking mode of
    operation.

  Precondition:
    ${SERCOM_INSTANCE_NAME}_USART_Initialize must have been called for the
    associated USART instance.

  Parameters:
    None.

  Returns:
    true - USART is busy in processing the previous write request.

    false - USART is free and ready to accept a new write request.

  Example:
    <code>

    if(true == ${SERCOM_INSTANCE_NAME}_USART_WriteIsBusy())
    {
        //USART is currently processing the previous write request.
        //Wait to submit new request.
    }

    // Refer to ${SERCOM_INSTANCE_NAME}_USART_Write() function code example for
    additional usage
    // tips.

    </code>

  Remarks:
    None.
*/

bool ${SERCOM_INSTANCE_NAME}_USART_WriteIsBusy ( void );
</#if>
<#if USART_RX_ENABLE = true>
// *****************************************************************************
/* Function:
    bool ${SERCOM_INSTANCE_NAME}_USART_ReadIsBusy( void )

  Summary:
    Returns the read request status associated with the given USART peripheral
    instance.

  Description:
    This function returns the read request status associated with the given
    USART peripheral instance. It can be used to check the completion status of
    the ${SERCOM_INSTANCE_NAME}_USART_Read() function when the library is
    configured for interrupt (non-blocking) mode. In that, the function can be
    used as an alternative to using a callback function to check for completion.

    This function is available only in interrupt or non-blocking mode of
    operation.

  Precondition:
    ${SERCOM_INSTANCE_NAME}_USART_Initialize must have been called for the
    associated USART instance.

  Parameters:
    None.

  Returns:
    true - if USART is busy in processing the previous read request.

    false - if USART is free and ready to accept the new read request.

  Example:
    <code>
    if(true == ${SERCOM_INSTANCE_NAME}_USART_ReadIsBusy())
    {
        //USART is currently processing the previous read request.
        //Wait to submit new request.
    }

    // Refer to ${SERCOM_INSTANCE_NAME}_USART_Read() function code example for
    additional usage
    // tips.

    </code>

  Remarks:
    None.
*/

bool ${SERCOM_INSTANCE_NAME}_USART_ReadIsBusy ( void );
</#if>
</#if>

<#if USART_INTERRUPT_MODE = true>
<#if USART_TX_ENABLE = true>
// *****************************************************************************
/* Function:
    size_t ${SERCOM_INSTANCE_NAME}_USART_WriteCountGet( void )

  Summary:
    Gets the count of number of bytes processed for a given USART write
    operation.

  Description:
    This function gets the count of processed byte for an og-going or completed
    USART write operation. When the library is configured for non-interrupt
    blocking mode, it returns the number of bytes that were processed when the
    ${SERCOM_INSTANCE_NAME}_USART_Write() function completed. In interrupt
    non-blocking mode, this function will return the number of bytes that have
    currently been processed.

    The function can be used to check if the ${SERCOM_INSTANCE_NAME}_USART_Write()
    was able to transmit the requested number of bytes successfully.

  Precondition:
    ${SERCOM_INSTANCE_NAME}_USART_Initialize must have been called for the
    associated USART instance.

  Parameters:
    None.

  Returns:
    Returns count of bytes currently completed/processed from the current
    Transmit buffer for interrupt non-blocking mode. In non-interrupt blocking
    mode, this function return the number of bytes that were processed when the
    ${SERCOM_INSTANCE_NAME}_USART_Write function completed.

  Example:
    <code>
    size_t count; //COUNT_EXPECTED is the expected Transmit count value

    count = ${SERCOM_INSTANCE_NAME}_USART_WriteCountGet();

    if(COUNT_EXPECTED > count)
    {
        //More bytes are expected to transmit, wait
    }
    </code>

  Remarks:
    This write count gets reset every time the
    ${SERCOM_INSTANCE_NAME}_USART_Write() function is called.
*/

size_t ${SERCOM_INSTANCE_NAME}_USART_WriteCountGet( void );
</#if>

<#if USART_RX_ENABLE = true>
// *****************************************************************************
/* Function:
    size_t ${SERCOM_INSTANCE_NAME}_USART_ReadCountGet( void )

  Summary:
    Gets the count of number of bytes processed for a given USART read
    operation.

  Description:
    This function gets the count of processed byte for an og-going or completed
    USART Read operation. When the library is configured for non-interrupt
    blocking mode, it returns the number of bytes that were processed when the
    ${SERCOM_INSTANCE_NAME}_USART_Read() function completed. In interrupt
    non-blocking mode, this function will return the number of bytes that have
    currently been processed.

    The function can be used to check if the ${SERCOM_INSTANCE_NAME}_USART_Read()
    was able to transmit the requested number of bytes successfully. In case of
    non-interrupt blocking mode, if the value returned by this function does not
    match the byte count specified in the ${SERCOM_INSTANCE_NAME}_USART_Read()
    function, then would indicate that an error has occurred during the
    reception.

  Precondition:
    ${SERCOM_INSTANCE_NAME}_USART_Initialize must have been called for the
    associated USART instance.

  Parameters:
    None.

  Returns:
    Returns count of bytes completed/processed to the current Receive buffer.

  Example:
    <code>

    // This shows an example in interrupt non-blocking mode.

    size_t count;
    char buffer[COUNT_EXPECTED];

    ${SERCOM_INSTANCE_NAME}_USART_Read(buffer, COUNT_EXPECTED);

    count = ${SERCOM_INSTANCE_NAME}_USART_ReadCountGet();

    if(COUNT_EXPECTED > count)
    {
        //More bytes are expected, wait
    }

    // This shows an example in non-interrupt blocking mode.

    size_t count;
    char buffer[COUNT_EXPECTED];

    ${SERCOM_INSTANCE_NAME}_USART_Read(buffer, COUNT_EXPECTED);

    count = ${SERCOM_INSTANCE_NAME}_USART_ReadCountGet();

    if(COUNT_EXPECTED > count)
    {
        // Indicates that an error has occurred during data reception.
    }

    </code>

  Remarks:
    This function resets the read count every time a new transfer is submitted.
*/

size_t ${SERCOM_INSTANCE_NAME}_USART_ReadCountGet( void );
 </#if>
 </#if>

<#if USART_INTERRUPT_MODE = false>
<#if USART_TX_ENABLE = true>
// *****************************************************************************
/* Function:
    bool ${SERCOM_INSTANCE_NAME}_USART_TransmitterIsReady( void )

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
    ${SERCOM_INSTANCE_NAME}_USART_Write() function should be called with a buffer
    size of 1.

  Precondition:
    ${SERCOM_INSTANCE_NAME}_USART_Initialize must have been called for the
    associated USART instance.

  Parameters:
    None.

  Returns:
    true - if transmit hardware FIFO has empty space to accept data.

    false - if transmit hardware FIFO is full.

  Example:
    <code>
    if(true == ${SERCOM_INSTANCE_NAME}_USART_TransmitterIsReady())
    {
        // Empty space is available in Transmitter FIFO, hence can write a byte
        ${SERCOM_INSTANCE_NAME}_USART_Write(&txData, 1);
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

bool ${SERCOM_INSTANCE_NAME}_USART_TransmitterIsReady ( void );
</#if>
<#if USART_RX_ENABLE = true>
// *****************************************************************************
/* Function:
    bool ${SERCOM_INSTANCE_NAME}_USART_ReceiverIsReady( void )

  Summary:
    Returns the hardware status of the USART Receiver.

   Description:
    This function returns the hardware status associated with the Receive
    hardware FIFO of the given USART peripheral instance. When Receiver is
    ready, user can read the available data.

    This function is available only in non-interrupt mode of operation. It can
    be used to achieve non-blocking behavior of
    ${SERCOM_INSTANCE_NAME}_USART_Read() function even if the library is
    configured for blocking behavior. If this function returns true, calling the
    SERCOMx_USART_Read() function with a byte count of 1 will result in
    non-blocking behavior.

  Precondition:
    ${SERCOM_INSTANCE_NAME}_USART_Initialize must have been called for the
    associated USART instance.

  Parameters:
    None.

  Returns:
    true - if receive hardware FIFO has at least one data available to read.

    false - if receive hardware FIFO is empty.

  Example:
    <code>
    if(true == ${SERCOM_INSTANCE_NAME}_USART_ReceiverIsReady())
    {
        // At least one data is available in Receive FIFO, hence can read a byte
        ${SERCOM_INSTANCE_NAME}_USART_Read(&rxData, 1);
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

bool ${SERCOM_INSTANCE_NAME}_USART_ReceiverIsReady ( void );
 </#if>
 </#if>
// *****************************************************************************
/* Function:
    USART_ERROR ${SERCOM_INSTANCE_NAME}_USART_ErrorGet( void )

  Summary:
    Gets the error of the given USART peripheral instance.

  Description:
    This function returns the errors associated with the given USART peripheral
    instance. Multiple error conditions may be active. The function return value
    should be matched against each member of the USART_ERROR enumeration to
    handle all error cases. Calling the ${SERCOM_INSTANCE_NAME}_USART_Read or
    SERCOMx_USART_Write functions will clear the errors. Hence error handling
    must be perfomed before these functions are called again.

  Precondition:
    ${SERCOM_INSTANCE_NAME}_USART_Initialize must have been called for the
    associated USART instance.

  Parameters:
    None.

  Returns:
    Returns errors occurred as listed by USART_ERROR enumeration.

  Example:
    <code>
    if(USART_ERROR_NONE != ${SERCOM_INSTANCE_NAME}_USART_ErrorGet())
    {
        if (USART_ERROR_OVERRUN & ${SERCOM_INSTANCE_NAME}_USART_ErrorGet())
        {
            // Handle overrun error.
        }

        if(USART_ERROR_PARITY & ${SERCOM_INSTANCE_NAME}_USART_ErrorGet())
        {
            // Handle parity error.
        }
    }
    </code>

  Remarks:
    USART errors are normally associated with the receiver. Hence, it is
    recommended to use this function in receive context only.
*/

USART_ERROR ${SERCOM_INSTANCE_NAME}_USART_ErrorGet( void );

<#if USART_INTERRUPT_MODE = true>
// *****************************************************************************
// *****************************************************************************
// Section: Callback Interface
// *****************************************************************************
// *****************************************************************************

<#if USART_TX_ENABLE = true>
// *****************************************************************************
/* Function:
    void ${SERCOM_INSTANCE_NAME}_USART_WriteCallbackRegister( SERCOM_USART_CALLBACK
                                                            callback,
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
    ${SERCOM_INSTANCE_NAME}_USART_Initialize must have been called for the
    associated USART instance.

  Parameters:
    callback - Pointer to the function to be called when the
    ${SERCOM_INSTANCE_NAME}_USART_Write() function has completed. Setting this to
    NULL will disable the callback feature.

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

        if(USART_ERROR_NONE != ${SERCOM_INSTANCE_NAME}_USART_ErrorGet())
        {
            //Handle error case
        }
        else
        {
            //Transfer completed successfully
        }
    }

    ${SERCOM_INSTANCE_NAME}_USART_WriteCallbackRegister(MyUsartCallback,
                                                            &myData[0]);
    </code>

  Remarks:
    The context parameter is ignored if the pointer passed is NULL.  To disable
    the callback function, pass a NULL for the callback parameter.  See the
    SERCOM_USART_CALLBACK type definition for additional information.
*/

void ${SERCOM_INSTANCE_NAME}_USART_WriteCallbackRegister( SERCOM_USART_CALLBACK callback, uintptr_t context );
</#if>
<#if USART_RX_ENABLE = true>
// *****************************************************************************
/* Function:
    void ${SERCOM_INSTANCE_NAME}x_USART_ReadCallbackRegister( SERCOM_USART_CALLBACK
                                                            callback,
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
    ${SERCOM_INSTANCE_NAME}_USART_Initialize must have been called for the
    associated USART instance.

  Parameters:
    callback - Pointer to the function that will be called when
    ${SERCOM_INSTANCE_NAME}_USART_Read() function has completed. Setting this to
    NULl will disable the callback feature.

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

        if(USART_ERROR_NONE != ${SERCOM_INSTANCE_NAME}_USART_ErrorGet())
        {
            //Handle error case
        }
        else
        {
            //Transfer completed successfully
        }
    }

    ${SERCOM_INSTANCE_NAME}_USART_ReadCallbackRegister(MyUsartCallback, &myData[0]);
    </code>

  Remarks:
    The context parameter is ignored if the pointer passed is NULL.
    To disable the callback function, pass a NULL for the callback parameter.
    See the SERCOM_USART_CALLBACK type definition for additional information.
    Receive callback is evoked when the reception is completed or when
    some reception error has occured.
    rxCallBack will be invoked when the reception is completed or when reception
    error occurs.
*/

void ${SERCOM_INSTANCE_NAME}_USART_ReadCallbackRegister( SERCOM_USART_CALLBACK callback, uintptr_t context );
</#if>

// *****************************************************************************
/* Function:
    void ${SERCOM_INSTANCE_NAME}_USART_InterruptHandler( void )

  Summary:
    Sercom Handler, handles all sercom interrupt.

  Description:
    This function handles all the operations post interrupt for
    all sercom USART interrupts.

  Parameters:
    None.

  Returns:
    None.

  Example:
    <code>

    void ${SERCOM_INSTANCE_NAME}_USART_InterruptHandler( void )
    {
        // serve interrupts
    }

    </code>

  Remarks:
    None.
*/

void ${SERCOM_INSTANCE_NAME}_USART_InterruptHandler( void );
</#if>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility
    }
#endif
// DOM-IGNORE-END

#endif //PLIB_${SERCOM_INSTANCE_NAME}_USART_H
