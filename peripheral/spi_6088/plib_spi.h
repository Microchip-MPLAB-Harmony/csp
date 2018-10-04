/*******************************************************************************
  SPI PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_spi.h

  Summary:
    SPI PLIB Header File for documentation

  Description:
    This library provides documentation of all the interfaces which can be used
    to control and interact with an instance of a Serial Peripheral Interface (SPI)
    controller.
    This file must not be included in any MPLAB Project.
*******************************************************************************/

/*******************************************************************************
* © 2018 Microchip Technology Inc. and its subsidiaries.
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

// *****************************************************************************
/* SPI Clock Phase

   Summary:
    Identifies SPI Clock Phase Options

   Description:
    This enumeration identifies possible SPI Clock Phase Options.

   Remarks:
    None.
*/
typedef enum
{
    /* Input data is valid on clock trailing edge and
    output data is ready on leading edge */
    SPI_CLOCK_PHASE_TRAILING_EDGE,

    /* Input data is valid on clock leading edge and
    output data is ready on trailing edge */
    SPI_CLOCK_PHASE_LEADING_EDGE

}SPI_CLOCK_PHASE;

// *****************************************************************************
/* SPI Clock Polarity

   Summary:
    Identifies SPI Clock Polarity Options

   Description:
    This enumeration identifies possible SPI Clock Polarity Options.

   Remarks:
    None.
*/
typedef enum
{
    /* The inactive state value of clock is logic level zero */
    SPI_CLOCK_POLARITY_IDLE_LOW,

    /* The inactive state value of clock is logic level one */
    SPI_CLOCK_POLARITY_IDLE_HIGH

}SPI_CLOCK_POLARITY;

// *****************************************************************************
/* SPI Data Bits

   Summary:
    Identifies SPI bits per transfer

   Description:
    This enumeration identifies number of bits per SPI transfer.

   Remarks:
    For 9 to 15bit modes, data should be right aligned in the 16 bit
    memory location.
*/
typedef enum
{
    /* 8 bits per transfer */
    SPI_DATA_BITS_8,

    /* 9 bits per transfer */
    SPI_DATA_BITS_9,

    /* 10 bits per transfer */
    SPI_DATA_BITS_10,

    /* 11 bits per transfer */
    SPI_DATA_BITS_11,

    /* 12 bits per transfer */
    SPI_DATA_BITS_12,

    /* 13 bits per transfer */
    SPI_DATA_BITS_13,

    /* 14 bits per transfer */
    SPI_DATA_BITS_14,

    /* 15 bits per transfer */
    SPI_DATA_BITS_15,

    /* 16 bits per transfer */
    SPI_DATA_BITS_16

}SPI_DATA_BITS;

// *****************************************************************************
/* SPI Setup Parameters

   Summary
    Identifies the setup parameters which can be changed dynamically.

   Description
    This structure identifies the possible setup parameters for SPI
    which can be changed dynamically if needed.

   Remarks:
    None.
*/
typedef struct
{

    /* Baud Rate or clock frequency */
    uint32_t            clockFrequency;

    /* Clock Phase */
    SPI_CLOCK_PHASE     clockPhase;

    /* Clock Polarity */
    SPI_CLOCK_POLARITY  clockPolarity;

    /* Number of bits per transfer */
    SPI_DATA_BITS       dataBits;

}SPI_TRANSFER_SETUP;

// *****************************************************************************
/* Function:
    void SPIx_Initialize (void);

  Summary:
    Initializes SPI x module of the device

  Description:
    This function initializes SPI x module of the device with the values
    configured in MHC GUI. Once the peripheral is initialized, transfer
    APIs can be used to transfer the data.

  Precondition:
    MCC GUI should be configured with the right values.

  Parameters:
    None.

  Returns:
    None.

  Example:
    <code>
        SPI1_Initialize();
    </code>

  Remarks:
    This function must be called only once and before any other SPI function is
    called.
*/
void SPIx_Initialize (void);

// *****************************************************************************
/* Function:
    bool SPIx_TransferSetup(SPI_TRANSFER_SETUP *setup, uint32_t spiSourceClock);

  Summary:
    Setup SPI operational parameters as desired by the client.

  Description:
    This function setup SPI x with the values needed by the client dynamically.
    Values passed through setup structure will be the new setup for SPI
    transmission. Even if user is not intending to modify all the setup
    parameters, he must update his setup structure with all its parameters. If
    user do not update all the setup structure elements, then unexpected SPI
    behavior may occur.

    User need not call this function if he has configured the setup in GUI and
    there is no dynamic change needed in any of the parameters.

  Precondition:
    SPI x must first be initialized using SPIx_Initialize().

  Parameters :
    spiSourceClock - Source Clock frequency in Hz on which SPI module is running.

    *setup - pointer to the data structure of type SPI_TRANSFER_SETUP which has the
             list of elements to be setup for a client.

  Returns:
    true  - if setup was successful, API returns true.
    false - if spiSourceClock and spi clock frequencies are such that resultant
            SCBR value is out of the possible range, then API returns false.

  Example:
    <code>
        SPI_TRANSFER_SETUP setup;
        setup.clockFrequency = 1000000;
        setup.clockPhase = SPI_CLOCK_PHASE_TRAILING_EDGE;
        setup.clockPolarity = SPI_CLOCK_POLARITY_IDLE_LOW;
        setup.dataBits = SPI_DATA_BITS_8;

        // Assuming 150 MHz as peripheral Master clock frequency
        if (SPI1_TransferSetup (&setup, 150000000) == false)
        {
            // this means setup could not be done, debug the reason.
        }

    </code>

  Remarks:
    User need not call this function if he has configured the setup in
    GUI and there is no dynamic change needed in any of the parameters.
*/
bool SPIx_TransferSetup (SPI_TRANSFER_SETUP *setup, uint32_t spiSourceClock);

// *****************************************************************************
/* Function:
    bool SPIx_WriteRead
	(
		void* pTransmitData,
		size_t txSize,
		void* pReceiveData,
		size_t rxSize
	);

  Summary:
    Write and Read data on SPI x peripheral

  Description:
    This function should be used to write "txSize" number of bytes and read
    "rxSize" number of bytes on SPI x module. Data pointed by pTransmitData
    is transmitted and received data is saved in the location pointed by
    pReceiveData.

    The function will work differently as per the configuration done in
    MCC as described below:

    1.  Blocking Configuration (Non-Interrupt mode): When "Interrupt Mode"
        option is unchecked in GUI, the generated code for that particular
        SPI PLIB instance will be blocking. In this particular mode, the
        WriteRead API will not return until all the requested data is transferred.

        After transferring all the data, boolean status 'True' is returned
        indicating operation completion.

    2.  Non-Blocking Configuration (Interrupt mode): When "Interrupt Mode"
        option is selected in GUI, the generated code for that
        particular SPI PLIB instance will be Non-blocking in nature. In this
        particular mode, application will give the data transfer
        responsibility to the PLIB and come back and start doing other
        activities, SPI Data transaction will happen in the corresponding ISR.
        in this mode, the transmit and receive data locations provided by user
        must remain valid until the data transfer is complete.
        Application can check the data transfer completion status via
        callback or polling mechanism. In case of callback, it needs to be
        registered prior to calling the WriteRead API. Data transfer status
        polling can be done using "SPIx_IsBusy" API.

  Precondition:
    The SPIx_Initialize function must have been called.

    Callback has to be registered using SPIx_CallbackRegister API if the
    peripheral instance has been configured in Interrupt mode and
    transfer completion status needs to be communicated back to application via
    callback.

  Parameters:
    *pTransmitData  Pointer to the data which has to be transmitted. if it is
                    NULL, that means only data receiving is expected. For 9
                    to 15bit mode, data should be right aligned in the 16 bit
                    memory location.
    txSize          Number of bytes to be transmitted. Always, size should be
                    given in terms of bytes. For example, if 5 16-bit data
                    are to be transmitted, the transmit size should be 10 bytes.
    *pReceiveData   Pointer to the location where received data has to be stored.
                    It is user's responsibility to ensure pointed location has
                    sufficient memory to store the read data.
                    if it is NULL, that means only data transmission is expected.
                    For 9 to 15bit mode, received data will be right aligned in
                    the 16 bit memory location.
    rxSize          Number of bytes to be received. Always, size should be
                    given in terms of bytes. For example, if 5 16-bit data
                    are to be received, the receive size should be 10 bytes.
                    if "n" number of bytes has to be received AFTER transmitting
                    "m" number of bytes, then "rxSize" should be set as "m+n".

  Returns:
    In Blocking mode, API returns True once the transfer is complete. It returns
    False if either of the size parameters are 0 and corresponding data pointer
    is NULL.

    In interrupt mode, if previous buffer request is not completed and a new
    transfer request comes, then this API will reject the new request and will
    return "False". Also, Same as blocking mode, It returns False if either of
    the size parameters are 0 and corresponding data pointer is NULL.

  Example:
    <code>
    uint8_t     txBuffer[4];
    uint8_t     rxBuffer[10];
    size_t      txSize = 4;
    size_t      rxSize = 10;
    bool        reqAccepted;

    SPI1_Initialize();

    SPI1_CallbackRegister(&APP_SPITransferHandler, NULL);

    reqAccepted = SPI1_WriteRead(&txBuffer, txSize, &rxBuffer, rxSize);

    void APP_SPITransferHandler(uintptr_t context)
    {

        //Transfer was completed without error, do something else now.

    }
    </code>

  Remarks:
    Non-blocking interrupt mode configuration implementation of this function
    will be used by Harmony driver implementation APIs.

*/
bool SPIx_WriteRead(
	void* pTransmitData,
	size_t txSize,
	void* pReceiveData,
	size_t rxSize);

// *****************************************************************************
/* Function:
    bool SPIx_Write(void* pTransmitData, size_t txSize);

  Summary:
    Write data on SPI x peripheral

  Description:
    This function should be used to write "txSize" number of bytes on
    SPI x module. Data pointed by pTransmitData is transmitted.

    The function will work differently as per the configuration done in
    MCC as described below:

    1.  Blocking Configuration (Non-Interrupt mode): When "Interrupt Mode"
        option is unchecked in GUI, the generated code for that particular
        SPI PLIB instance will be blocking. In this particular mode, the
        Write API will not return until all the requested data is transferred.

        After transferring all the data, boolean status 'True' is returned
        indicating operation completion.

    2.  Non-Blocking Configuration (Interrupt mode): When "Interrupt Mode"
        option is selected in GUI, the generated code for that
        particular SPI PLIB instance will be Non-blocking in nature. In this
        particular mode, application will give the data transfer
        responsibility to the PLIB and come back and start doing other
        activities, SPI Data transaction will happen in the corresponding ISR.
        in this mode, the transmit data locations provided by user
        must remain valid until the data transfer is complete.
        Application can check the data transfer completion status via
        callback or polling mechanism. In case of callback, it needs to be
        registered prior to calling the Write API. Data transfer status
        polling can be done using "SPIx_IsBusy" API.

  Precondition:
    The SPIx_Initialize function must have been called.

    Callback has to be registered using SPIx_CallbackRegister API if the
    peripheral instance has been configured in Interrupt mode and
    transfer completion status needs to be communicated back to application via
    callback.

  Parameters:
    *pTransmitData  Pointer to the data which has to be transmitted. if it is
                    NULL, that means only data receiving is expected. For 9
                    to 15bit mode, data should be right aligned in the 16 bit
                    memory location.
    txSize          Number of bytes to be transmitted. Always, size should be
                    given in terms of bytes. For example, if 5 16-bit data
                    are to be transmitted, the transmit size should be 10 bytes.

  Returns:
    In Blocking mode, API returns True once the transfer is complete. It returns
    False if txSize parameter is 0 and transmit data pointer is NULL.

    In interrupt mode, if previous buffer request is not completed and a new
    transfer request comes, then this API will reject the new request and will
    return "False". Also, Same as blocking mode, It returns False if txSize
    parameter is 0 and transmit data pointer is NULL.

  Example:
    <code>
    uint8_t     txBuffer[4];
    size_t      txSize = 4;
    bool        reqAccepted;

    SPI1_Initialize();

    SPI1_CallbackRegister(&APP_SPITransferHandler, NULL);

    reqAccepted = SPI1_Write(&txBuffer, txSize);

    void APP_SPITransferHandler(uintptr_t context)
    {

        //Transfer was completed without error, do something else now.

    }
    </code>

  Remarks:
    Non-blocking interrupt mode configuration implementation of this function
    will be used by Harmony driver implementation APIs.

*/
bool SPIx_Write(void* pTransmitData, size_t txSize);

// *****************************************************************************
/* Function:
    bool SPIx_Read(void* pReceiveData, size_t rxSize);

  Summary:
    Read data on SPI x peripheral

  Description:
    This function should be used to read "rxSize" number of bytes on
    SPI x module. Received data is saved in the location pointed by pReceiveData.

    The function will work differently as per the configuration done in
    MCC as described below:

    1.  Blocking Configuration (Non-Interrupt mode): When "Interrupt Mode"
        option is unchecked in GUI, the generated code for that particular
        SPI PLIB instance will be blocking. In this particular mode, the
        Read API will not return until all the requested data is transferred.

        After transferring all the data, boolean status 'True' is returned
        indicating operation completion.

    2.  Non-Blocking Configuration (Interrupt mode): When "Interrupt Mode"
        option is selected in GUI, the generated code for that
        particular SPI PLIB instance will be Non-blocking in nature. In this
        particular mode, application will give the data transfer
        responsibility to the PLIB and come back and start doing other
        activities, SPI Data transaction will happen in the corresponding ISR.
        in this mode, the receive data locations provided by user
        must remain valid until the data transfer is complete.
        Application can check the data transfer completion status via
        callback or polling mechanism. In case of callback, it needs to be
        registered prior to calling the Read API. Data transfer status
        polling can be done using "SPIx_IsBusy" API.

  Precondition:
    The SPIx_Initialize function must have been called.

    Callback has to be registered using SPIx_CallbackRegister API if the
    peripheral instance has been configured in Interrupt mode and
    transfer completion status needs to be communicated back to application via
    callback.

  Parameters:
    *pReceiveData   Pointer to the location where received data has to be stored.
                    It is user's responsibility to ensure pointed location has
                    sufficient memory to store the read data.
                    if it is NULL, that means only data transmission is expected.
                    For 9 to 15bit mode, received data will be right aligned in
                    the 16 bit memory location.
    rxSize          Number of bytes to be received. Always, size should be
                    given in terms of bytes. For example, if 5 16-bit data
                    are to be received, the receive size should be 10 bytes.

  Returns:
    In Blocking mode, API returns True once the transfer is complete. It returns
    False if rxSize is 0 and receive data pointer is NULL.

    In interrupt mode, if previous buffer request is not completed and a new
    transfer request comes, then this API will reject the new request and will
    return "False". Also, Same as blocking mode, It returns False if rxSize is
    0 and receive data pointer is NULL.

  Example:
    <code>
    uint8_t     rxBuffer[10];
    size_t      rxSize = 10;
    bool        reqAccepted;

    SPI1_Initialize();

    SPI1_CallbackRegister(&APP_SPITransferHandler, NULL);

    reqAccepted = SPI1_Read(&rxBuffer, rxSize);

    void APP_SPITransferHandler(uintptr_t context)
    {

        //Transfer was completed without error, do something else now.

    }
    </code>

  Remarks:
    Non-blocking interrupt mode configuration implementation of this function
    will be used by Harmony driver implementation APIs.

*/
bool SPIx_Read(void* pReceiveData, size_t rxSize);

// *****************************************************************************
/* Function:
    bool SPIx_IsBusy (void):

  Summary:
    Returns transfer status of SPI x

  Description:
    This function returns transfer status of last successful Write, Read or
    WriteRead request on SPI x module in interrupt mode.

  Precondition:
    None.

  Parameters:
    None.

  Returns:
    Returns the current status of transfer happening on SPI x.
        true:  Transfer is still in progress
        false: Transfer is completed

  Example:
    <code>
        if (SPI1_IsBusy() == false)
        {
            //Data Transfer is complete, do something else.
        }
    </code>

  Remarks:
    This API is available only for interrupt mode as blocking mode transfer
    APIs will always return only after completing the transfer.
*/
bool SPIx_IsBusy (void):

// *****************************************************************************
/* SPI Callback Function Pointer

   Summary:
    Pointer to a SPI Callback function.

   Description:
    This data type defines the required function signature for the SPI
    callback function. Application must register a pointer to a callback
    function whose function signature (parameter and return value types)
    match the types specified by this function pointer in order to
    receive callback from the PLIB.

    The parameters and return values are described here and a partial example
    implementation is provided.

  Parameters:
    context         - Value identifying the context of the application that
                      registered the callback function

  Returns:
    None.

  Example:
    <code>
    SPI1_CallbackRegister(&APP_SPITransferHandler, NULL);
    void APP_SPITransferHandler(uintptr_t context)
    {
        //Transfer was completed without error, do something else now.
    }
    </code>

  Remarks:
    The context parameter contains the a handle to the client context,
    provided at the time the callback function was registered using the
    SPIx_CallbackRegister function. This context handle value is
    passed back to the client as the "context" parameter.  It can be any value
    (such as a pointer to the client's data) necessary to identify the client
    context or instance  of the client that made the data transfer
    request.

    The callback function executes in the PLIB's interrupt context. It is
    recommended of the application to not perform process intensive or blocking
    operations with in this function.
*/
typedef  void (*SPI_CALLBACK) (uintptr_t context);

// *****************************************************************************
/* Function:
    void SPIx_CallbackRegister
    (
        const SPI_CALLBACK* callback,
        uintptr_t context
    );

  Summary:
    Allows application to register callback with PLIB.

  Description:
    This function allows application to register a callback function for the PLIB
    to call back when requested data transfer operation has completed.

    The callback should be registered before the client performs transfer operation.

    At any point if application wants to stop the callback, it can call this function
    with "callback" value as NULL.

  Precondition:
    The SPIx_Initialize function must have been called.

  Parameters:
    callback -     Pointer to the callback function implemented by the user

    context  -     The value of parameter will be passed back to the application
                   unchanged, when the callback function is called. It can
                   be used to identify any application specific value that
                   identifies the instance of the client module (for example,
                   it may be a pointer to the client module's state structure).

  Returns:
    None.

  Example:
    <code>
    uint8_t     txBuffer[4];
    uint8_t     rxBuffer[10];
    size_t      txSize = 4;
    size_t      rxSize = 10;
    bool        reqAccepted;

    SPI1_Initialize();

    SPI1_CallbackRegister(&APP_SPITransferHandler, NULL);

    reqAccepted = SPI1_WriteRead(&txBuffer, txSize, &rxBuffer, rxSize);

    void APP_SPITransferHandler(uintptr_t context)
    {
        //Transfer was completed without error, do something else now.
    }
    </code>

  Remarks:
    If the client does not want to be notified when the queued operation
    has completed, it does not need to register a callback.
*/
void SPIx_CallbackRegister(const SPI_CALLBACK* callback, uintptr_t context);