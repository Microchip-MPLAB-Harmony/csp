/*******************************************************************************
  USART Peripheral Library Interface Header File

  Company
    Microchip Technology Inc.

  File Name
    plib_usart.h

  Summary
    USART peripheral library interface.

  Description
    This file defines the interface to the USART peripheral library.  This
    library provides access to and control of the associated peripheral
    instance.

  Remarks:
    This header is for documentation only.  The actual plib_usart<x> headers
    will be generated as required by the MHC (where <x> is the peripheral
    instance number).

    Every interface symbol has a lower-case 'x' in it following the "USART"
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

#ifndef PLIB_USARTx_H    // Guards against multiple inclusion
#define PLIB_USARTx_H

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
    USART_ERROR_NONE,

    USART_ERROR_OVERRUN,

    USART_ERROR_PARITY,

    USART_ERROR_FRAMING

} USART_ERROR;

// *****************************************************************************
/* USART Data Bits

   Summary:
    Defines the data type for the USART data bit length.

   Description:
    This is used to define length of data bits.

   Remarks:
    None.
*/
typedef enum
{
    USART_DATA_BIT_5,

    USART_DATA_BIT_6,

    USART_DATA_BIT_7,

    USART_DATA_BIT_8,

    USART_DATA_BIT_9

} USART_DATA_BIT;

// *****************************************************************************
/* USART Parity

   Summary:
    Defines the type of parity for USART peripheral.

   Description:
    This defines the type of parity for USART peripheral.

   Remarks:
    None.
*/
typedef enum
{
    USART_PARITY_NONE,

    USART_PARITY_ODD,

    USART_PARITY_EVEN,

    USART_PARITY_MARK,

    USART_PARITY_SPACE,

    USART_PARITY_MULTIDROP

} USART_PARITY;

// *****************************************************************************
/* USART Stop Bits

   Summary:
    Defines the length of stop bits.

   Description:
    This data type defines the length of stop bits for USART peripheral.

   Remarks:
    None.
*/
typedef enum
{
    USART_STOP_BIT_1,

    USART_STOP_BIT_1_5,

    USART_STOP_BIT_2

} USART_STOP_BIT;

// *****************************************************************************
/* USART Serial Setup

   Summary:
    Defines the data type for the USART serial setup.

   Description:
    This can be used to define a serial setup which may then be used to change
    the serial setup of the USART dynamically.

   Remarks:
    None.
*/
typedef struct
{
    uint32_t baudRate;

    USART_DATA_BIT dataWidth;

    USART_PARITY parity;

    USART_STOP_BIT stopBits;

} USART_SERIAL_SETUP;

// *****************************************************************************
/* Callback Function Pointer

   Summary:
    Defines the data type and function signature for the USART peripheral
    callback function.

   Description:
    This data type defines the function signature for the USART peripheral
    callback function. The USART peripheral will call back the client's
    function with this signature when the USART buffer event has occurred.

   Precondition:
    - USARTx_Initialize must have been called for the given USART peripheral
      instance.
    - Callback must have been registered using USARTx_WriteCallbackRegister or
      USARTx_ReadCallbackRegister.

   Parameters:
    context  - Allows the caller to provide a context value (usually a pointer
               to the callers context for multiple clients).

   Returns:
    None.

   Example:
    <code>
    void MyUsartCallback(uintptr_t context)
    {
        if(USART1_ErrorGet() != USART_ERROR_NONE)
        {
            //Handle error case
        }
        else
        {
            //Transfer completed successfully
        }
    }

    USART1_WriteCallbackRegister(MyUsartCallback, (uintptr_t)NULL);
    </code>

   Remarks:
    None.
*/

typedef void (*USART_CALLBACK)( uintptr_t context );


// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Function:
    void USARTx_Initialize( void )

   Summary:
     Initializes given instance of the USART peripheral.

   Description:
     This function initializes the given instance of the USART peripheral as
     configured by the user in MHC.

   Precondition:
     None.

   Parameters:
    None.

   Returns:
    None.

   Example:
    <code>
    USART1_Initialize();
    </code>

   Remarks:
    Stops the USART if it was already running and reinitializes it.
*/

void USARTx_Initialize( void );


// *****************************************************************************
// *****************************************************************************
// Section: Transaction (Write/Read) Request Interface
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Function:
    bool USARTx_Write( void *buffer, const size_t size )

   Summary:
    Submits a write buffer to the given USART peripheral to transfer.

   Description:
    This function submits a write buffer to the USART peripheral to transfer.
    The behavior of this function call will vary based on the mode
    selected within MHC.

    If the peripheral is configured for the interrupt mode, this function call
    is always non-blocking. Call to this function submits the buffer and the
    size to the peripheral library and returns immediately. User can check the
    transfer status either through callback mechanism or by calling
    USARTx_WriteIsBusy.

    If the peripheral is configured for the non-interrupt mode, this
    function call returns only after requested size is transferred.

   Precondition:
    USARTx_Initialize must have been called for the associated USART instance.

   Parameters:
    buffer - Pointer to the user buffer.
    size - Number of bytes to be transferred.

   Returns:
    - True - Write request was successful.
    - False - Write request has failed.

  Example:
    <code>
    //Example to use in non-interrupt mode
    char myData[6] = {"hello"};

    if(USART1_Write(&myData, 6) == true)
    {
        //The transfer is completed
    }
    </code>

  Remarks:
    None.
*/

bool USARTx_Write( void *buffer, const size_t size );

// *****************************************************************************
/* Function:
    void USARTx_WriteByte( int data )

   Summary:
    Submits a byte of data to the given USART peripheral to transfer.

   Description:
    This function submits a byte of data to the USART peripheral to transfer.
    This Function is available only in non-interrupt mode.

   Precondition:
    - USARTx_Initialize must have been called for the associated USART instance.
    - Transmitter readiness must be confirmed using USARTx_TransmitterIsReady.

   Parameters:
    data - Data byte to be transferred.

   Returns:
    None

  Example:
    <code>
        USART1_WriteByte(0xAA);
    </code>

  Remarks:
    None.
*/

void USARTx_WriteByte(int data);

// *****************************************************************************
/* Function:
    bool USARTx_Read( void *buffer, const size_t size )

   Summary:
    Submits a read buffer to the given USART peripheral to process.

   Description:
    This function submits a request to read n-Bytes of data to the UART peripheral.
    The behavior of this function call will vary based on the mode
    selected within MHC.

    If the peripheral is configured for the interrupt mode, this function call
    is always non-blocking. Call to this function submits the buffer and the
    size to the peripheral library and returns immediately. User can check the
    transfer status either through callback mechanism or by calling
    USARTx_ReadIsBusy.

    If the peripheral is configured for the non-interrupt mode, this
    function call returns only after requested size is processed.

   Precondition:
    USARTx_Initialize must have been called for the associated USART instance.

   Parameters:
    buffer - Pointer to the user buffer.
    size - Number of bytes to be transferred.

   Returns:
    - True - Read request was successful.
    - False - Read request has failed.

  Example:
    <code>
    //Example to use in non-interrupt

    #define COUNT  6
    char rxData[COUNT] = {}; //COUNT is expected size

    if(USART1_Read(&rxData, COUNT) == true)
    {
        //The transfer is completed
    }
    </code>

  Remarks:
    None.
*/

bool USARTx_Read( void *buffer, const size_t size );

// *****************************************************************************
/* Function:
    int USARTx_ReadByte( void )

   Summary:
    Submits request to read a byte of data to the given USART peripheral.

   Description:
    This function submits request to read a byte of data to the given USART
    peripheral.
    This Function is available only in non-interrupt mode.

   Precondition:
    - USARTx_Initialize must have been called for the associated USART instance.
    - Receiver readiness must be confirmed using USARTx_ReceiverIsReady.

   Parameters:
    None

   Returns:
    Read byte.

  Example:
    <code>
    char rxData;

    if(USART1_ReceiverIsReady() == true)
    {
        rxData = USART1_ReadByte();
    }
    </code>

  Remarks:
    None.
*/

int USARTx_ReadByte( void );

// *****************************************************************************
// *****************************************************************************
// Section: Transaction (Write/Read) Status Interface
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Function:
    bool USARTx_WriteIsBusy( void )

   Summary:
    Returns the write request status associated with the given USART peripheral
    instance.

   Description:
    This function returns the status of the write request which was made using
    USART1_Write function. It can be used to poll the write status if callback
    is not intended.

    This function is available only in interrupt mode of operation.

   Precondition:
    USARTx_Initialize must have been called for the associated USART instance.

   Parameters:
    None.

   Returns:
    - true - USART is busy in processing write request.
    - false - USART is free and ready to accept the new write request.

  Example:
    <code>
    if(true == USART1_WriteIsBusy())
    {
        //USART is currently processing the write request.
    }
    else
    {
        // write is completed.
    }
    </code>

  Remarks:
    None.
*/

bool USARTx_WriteIsBusy( void );


// *****************************************************************************
/* Function:
    bool USARTx_ReadIsBusy( void )

   Summary:
    Returns the read request status associated with the given USART peripheral
    instance.

   Description:
    This function returns the status of the read request which was made using
    USART1_Read function. It can be used to poll the read status if callback
    is not intended.

    This function is available only in interrupt mode of operation.

   Precondition:
    USARTx_Initialize must have been called for the associated USART instance.

   Parameters:
    None.

   Returns:
    - true - USART is busy in processing the read request.
    - false - USART is free and ready to accept the new read request.

  Example:
    <code>
    if(true == USART1_ReadIsBusy())
    {
        //USART is currently processing the previous read request.
    }
    else
    {
        // read is completed
    }
    </code>

  Remarks:
    None.
*/

bool USARTx_ReadIsBusy( void );


// *****************************************************************************
/* Function:
    size_t USARTx_WriteCountGet( void )

   Summary:
    Returns the count of number of bytes processed for a given USART write
    operation.

   Description:
    This function returns the count of number of bytes processed for the last
    USART write request.

    This function is available only in interrupt mode of operation.

   Precondition:
    USARTx_Initialize must have been called for the associated USART instance.

   Parameters:
    None.

   Returns:
    Count of bytes completed/processed for the last write request.

  Example:
    <code>
    size_t count; //COUNT_EXPECTED is the expected Transmit count value

    count = USART1_WriteCountGet();

    if(COUNT_EXPECTED > count)
    {
        //More bytes are expected to transmit, wait
    }
    </code>

  Remarks:
    This function resets the write count every time a new transfer is submitted.
*/

size_t USARTx_WriteCountGet( void );


// *****************************************************************************
/* Function:
    size_t USARTx_ReadCountGet( void )

   Summary:
    Returns the count of number of bytes processed for a given USART read
    operation.

   Description:
    This function returns the count of number of bytes processed for the last
    USART read operation.

    This function is available only in interrupt mode of operation.

   Precondition:
    USARTx_Initialize must have been called for the associated USART instance.

   Parameters:
    None.

   Returns:
    Count of bytes processed for the last read request.

    In case of error, the API returns the count of successful read bytes.

  Example:
    <code>
    size_t count; //COUNT_EXPECTED is the expected Receive count value

    count = USART1_ReadCountGet();

    if(COUNT_EXPECTED > count)
    {
        //More bytes are expected, wait
    }
    </code>

  Remarks:
    This function resets the read count every time a new transfer is submitted.
*/

size_t USARTx_ReadCountGet( void );

// *****************************************************************************
// *****************************************************************************
// Section: Peripheral (Write/Read) Status Interface
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Function:
    bool USARTx_TransmitterIsReady( void )

   Summary:
    Returns the hardware status of the USART Transmitter.

   Description:
    This function returns the hardware status associated with the Transmit
    hardware FIFO of the given USART peripheral instance.When Transmitter is
    ready, user can submit data to transmit.

    This function is available only in non-interrupt mode of operation and it
    should be used to check transmitter readiness before calling
    USART1_WriteByte function.

   Precondition:
    USARTx_Initialize must have been called for the associated USART instance.

   Parameters:
    None.

   Returns:
    - true - Transmit hardware FIFO has empty space to accept the data.
    - false - Transmit hardware FIFO is full.

  Example:
    <code>
    if(true == USART1_TransmitterIsReady())
    {
        // Empty space is available in Transmitter FIFO, hence can write a byte
        USART1_WriteByte('A');
    }
    else
    {
        //Transmitter is busy
    }
    </code>

  Remarks:
    None.
*/

bool USARTx_TransmitterIsReady( void );


// *****************************************************************************
/* Function:
    bool USARTx_ReceiverIsReady( void )

   Summary:
    Returns the hardware status of the USART Receiver.

   Description:
    This function returns the hardware status associated with the Receive
    hardware FIFO of the given USART peripheral instance.

    When Receiver is ready, user can read the available data.

    This function is available only in non-interrupt mode of operation and it
    should be used to check receiver readiness before calling
    USART1_ReadByte function.

   Precondition:
    USARTx_Initialize must have been called for the associated USART instance.

   Parameters:
    None.

   Returns:
    - true - Receive hardware FIFO has at least one data available to read.
    - false - Receive hardware FIFO is empty.

  Example:
    <code>
    char rxData;
    if(true == USART1_ReceiverIsReady())
    {
        // At least one data is available in Receive FIFO, hence can read a byte
        rxData = USART1_ReadByte();
    }
    else
    {
        //Receiver is empty
    }
    </code>

  Remarks:
    None.
*/

bool USARTx_ReceiverIsReady( void );


// *****************************************************************************
/* Function:
    USART_ERROR USARTx_ErrorGet( void )

   Summary:
    Gets the error of the given USART peripheral instance.

   Description:
    This function returns the errors associated with the given USART peripheral
    instance. It reports all the USART errors ORed together. The call to this
    function also clears all the associated errors.

   Precondition:
    USARTx_Initialize must have been called for the associated USART instance.

   Parameters:
    None.

   Returns:
    Errors occurred as listed by USART_ERROR.

  Example:
    <code>
    if ((USART_ERROR_OVERRUN & USART1_ErrorGet()) == USART_ERROR_OVERRUN)
    {
        //Errors are cleared by the API call, take respective action
        //for the overrun error case.
    }
    </code>

  Remarks:
    USART errors are normally associated with the receiver. Hence, it is
    recommended to use this function in receive context only.
*/

USART_ERROR USARTx_ErrorGet( void );


// *****************************************************************************
/* Function:
    void USARTx_SerialSetup(USART_SERIAL_SETUP * setup, uint32_t srcClkFreq)

   Summary:
    Sets the USART serial communication settings dynamically.

   Description:
    This function sets the USART serial communication settings dynamically.

   Precondition:
    USARTx_Initialize must have been called for the associated USART instance.

    The USART transmit or receive transfer status should not be busy.

   Parameters:
    setup - Pointer to the structure containing the serial setup.
    srcClkFreq - USART Peripheral Clock Source Frequency.

   Returns:
    - true - Serial setup was updated Successfully.
    - false - Failure while updating serial setup.

   Example:
    <code>
    USART_SERIAL_SETUP setup = {
            115200,
            USART_DATA_8_BIT,
            USART_PARITY_ODD,
            USART_STOP_1_BIT
        };

    USART1_SerialSetup(&setup, 0);
    </code>

   Remarks:
    srcClkFreq overrides any change in the peripheral clock frequency.
    If configured to zero, PLIB takes the peripheral clock frequency from MHC.
*/

bool USARTx_SerialSetup( USART_SERIAL_SETUP *setup, uint32_t srcClkFreq );


// *****************************************************************************
// *****************************************************************************
// Section: Callback Interface
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Function:
    bool USARTx_WriteCallbackRegister( USART_CALLBACK callback, uintptr_t context )

   Summary:
    Sets the pointer to the function (and it's context) to be called when the
    given USART's write events occur.

   Description:
    This function sets the pointer to a client function to be called "back"
    when the given USART's write events occur. It also passes a context value
    (usually a pointer to a context structure) that is passed into the
    function when it is called.

    This function is available only in interrupt mode of operation.

   Precondition:
    USARTx_Initialize must have been called for the associated USART instance.

   Parameters:
    callback - A pointer to a function with a calling signature defined by the
               USART_CALLBACK data type.

    context - A value (usually a pointer) passed (unused) into the function
              identified by the callback parameter.

   Returns:
    - True - Callback registration was successful
    - False - Callback registration failed

  Example:
    <code>
    void MyUsartCallback(uintptr_t context)
    {
        if(USART1_ErrorGet() != USART_ERROR_NONE)
        {
            //Handle error case
        }
        else
        {
            //Transfer completed successfully
        }
    }

    USART1_WriteCallbackRegister(MyUsartCallback, (uintptr_t)NULL);
    </code>

  Remarks:
    The context parameter is ignored if the pointer passed is NULL.
    To disable the callback function, pass a NULL for the callback parameter.
    See the USART_CALLBACK type definition for additional information.
*/
bool USARTx_WriteCallbackRegister( USART_CALLBACK callback, uintptr_t context );

// *****************************************************************************
/* Function:
    bool USARTx_ReadCallbackRegister( USART_CALLBACK callback, uintptr_t context )

   Summary:
    Sets the pointer to the function (and it's context) to be called when the
    given USART's read events occur.

   Description:
    This function sets the pointer to a client function to be called "back"
    when the given USART's read events occur. It also passes a context value
    (usually a pointer to a context structure) that is passed into the
    function when it is called.

    This function is available only in interrupt mode of operation.

   Precondition:
    USARTx_Initialize must have been called for the associated USART instance.

   Parameters:
    callback - A pointer to a function with a calling signature defined by the
               USART_CALLBACK data type.

    context - A value (usually a pointer) passed (unused) into the function
              identified by the callback parameter.

   Returns:
    - True - Callback registration was successful
    - False - Callback registration failed

  Example:
    <code>
    void MyUsartCallback(uintptr_t context)
    {
        if(USART1_ErrorGet() != USART_ERROR_NONE)
        {
            //Handle error case
        }
        else
        {
            //Transfer completed successfully
        }
    }

    USART1_ReadCallbackRegister(MyUsartCallback, (uintptr_t)NULL);
    </code>

  Remarks:
    The context parameter is ignored if the pointer passed is NULL.
    To disable the callback function, pass a NULL for the callback parameter.
    See the USART_CALLBACK type definition for additional information.
*/

bool USARTx_ReadCallbackRegister( USART_CALLBACK callback, uintptr_t context );


// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END

#endif //PLIB_USARTx_H
