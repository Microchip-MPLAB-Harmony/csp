/*******************************************************************************
  Serial Communication Interface Inter-Integrated Circuit (SERCOM I2C) Library
  Interface Header File

  Company:
    Microchip Technology Inc.

  File Name:
    plib_sercom_i2c.h

  Summary:
    SERCOM I2C Peripheral Library Interface

  Description:
    This file defines the interface to the SERCOM I2C peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

  Remarks:
    This header is for documentation only.  The actual plib_sercom<x>_i2c
    headers will be generated as required by the MCC (where <x> is the
    peripheral instance number).

    Every interface symbol has a lower-case 'x' in it following the "SERCOM" 
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

#ifndef PLIB_SERCOMx_I2C_H
#define PLIB_SERCOMx_I2C_H

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
/* SERCOM I2C Transfer Status

   Summary:
    Defines the possible statuses of a SERCOM I2C Transfer.

   Description:
    This enum defines the possible statuses of SERCOM I2C Transfer. Any one
    status from this will be returned if the transfer status is queried through
    the SERCOMx_I2C_TransferStatusGet() function.

   Remarks:
    None.
*/

typedef enum
{
    /* Peripheral is busy, processing the transfer request */
    SERCOM_I2C_TRANSFER_STATUS_BUSY,

    /* Peripheral successfully completed the transfer request */
    SERCOM_I2C_TRANSFER_STATUS_SUCCESS,

    /* Error occurred during the transfer request */
    SERCOM_I2C_TRANSFER_STATUS_ERROR,

} SERCOM_I2C_TRANSFER_STATUS;

// *****************************************************************************
/* SERCOM I2C Error.

  Summary:
    Defines the possible errors that the SERCOM I2C peripheral can generate.

  Description:
    This enum defines the possible error the SERCOM I2C peripheral can generate.
    An error of this type is returned by the SERCOMx_I2C_ErrorGet() function.

  Remarks:
    None.
*/

typedef enum
{
    /* No error has occurred. */
    SERCOM_I2C_ERROR_NONE,

    /* A bus transaction was NAK'ed */
    SERCOM_I2C_ERROR_NAK,

    /* A bus error has occurred. */
    SERCOM_I2C_ERROR_BUS,

} SERCOM_I2C_ERROR;

// *****************************************************************************
/* SERCOM I2C Transfer Event Callback Function Pointer.

  Summary:
    Defines the data type and function signature for the SERCOM I2C peripheral
    callback function.

  Description:
    This data type defines the function signature for the SERCOM I2C peripheral
    callback function. The SERCOM I2C peripheral will call back the client's
    function with this signature when the SERCOM I2C Transfer has completed.

  Precondition:
    SERCOMx_I2C_Initialize must have been called for the given SERCOM I2C
    peripheral instance and SERCOMx_I2C_CallbackRegister must have been called
    to set the function to be called. The callback register function should have
    been called before a read, write or transfer function has been initiated.

  Parameters:
    context - Allows the caller to provide a context value (usually a pointer
    to the callers context for multi-instance clients).

  Returns:
    None.

  Example:
    <code>
    // Data tracking what each of my instances is doing.
    MY_DATA myData[2];

    void MyI2CCallback ( uintptr_t context )
    {
        MY_DATA *mePtr = (MY_DATA *)context;

        if(SERCOM_I2C_TRANSFER_COMPLETE == SERCOM1_I2C_TransferStatusGet())
        {
            //Handle complete status here based on context
        }
        else
        {
            //Handle error here
        }
    }

    SERCOMx_I2C_CallbackRegister(MyI2CCallback, &myData[0]);
    </code>

  Remarks:
    None.
*/

typedef void (*SERCOM_I2C_CALLBACK) (uintptr_t contextHandle);

// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************

/*
 * The following functions make up the methods (set of possible operations) of
 * this interface.
 */

// *****************************************************************************
/* Function:
    void SERCOMx_I2C_Initialize(void)

  Summary:
    Initializes the instance of the SERCOM peripheral operating in I2C mode.

  Description:
    This function initializes the given instance of the SERCOM I2C peripheral as
    configured by the user from the MHC.

  Precondition:
    The Generic Clock Generator should have been assigned to the SERCOMx
    Peripheral Clock Channel.

  Parameters:
    None.

  Returns:
    None.

  Example:
    <code>
        SERCOMx_I2C_Initialize();
    </code>

  Remarks:
    Stops the SERCOM I2C if it was already running and reinitializes it.
*/

void SERCOMx_I2C_Initialize(void);

// *****************************************************************************
/* Function:
    bool SERCOMx_I2C_TransferSetup( I2C_TRANSFER_SETUP * setup,
                                                           uint32_t srcClkFreq )

  Summary:
    Configure SERCOM I2C operational parameters at run time.

  Description:
    This function allows the application to change the SERCOM I2C operational
    parameter at run time. The application can thus override the MHC defined
    configuration for these parameters. The parameter are specified via the
    I2C_TRANSFER_SETUP type setup parameter. Each member of this parameter
    should be initialized to the desired value.

    The application may feel need to call this function in situation where
    multiple I2C slaves, each with different operation paramertes, are connected
    to one I2C master. This function can thus be used to setup the I2C Master to
    meet the communication needs of the slave.

    Calling this function will affect any ongoing communication. The application
    must thus ensure that there is no on-going communication on the I2C before
    calling this function.

  Precondition:
    SERCOMx_I2C_Initialize must have been called for the
    associated SERCOM instance. The transfer status should not be busy.

  Parameters:
    setup - Pointer to the structure containing the transfer setup.
    srcClkFreq - I2C Peripheral Clock Source Frequency.

  Returns:
    true - Transfer setup was updated Successfully.
    false - Failure while updating transfer setup.

  Example:
    <code>
        I2C_TRANSFER_SETUP setup = { 400000 };

        SERCOMx_I2C_TransferSetup( &setup, 0 );
    </code>

  Remarks:
    srcClkFreq overrides any change in the peripheral clock frequency.
    If configured to zero PLib takes the peripheral clock frequency from MHC.
*/

bool SERCOMx_I2C_TransferSetup( I2C_TRANSFER_SETUP * setup, uint32_t srcClkFreq );

// *****************************************************************************
/* Function:
    bool SERCOMx_I2C_TRBBuildRead(uint16_t address, uint8_t *pdata, uint8_t length)

  Summary:
    Allocates and builds the Read Transaction Request Block (TRB).

  Description:
    This function allocates and builds a Read Transaction Request Block. The
    transaction will be executed when the SERCOMx_I2C_TRBTransfer() function is
    called. A transaction is marked complete when either all the requeste bytes
    have been received or when a bus error or a NAK condition has occurred. The
    application can build multiple Read TRBs.

    The transaction will be executed in the same order in which the build
    function was called. A I2C Repeated Start condition will be placed on the
    bus between each transaction.  The maximum number of TRBs that can be built
    is configurable in MHC. The application should not access the contents of
    the buffer pointed to by pData while a transfer is in progress.

    Calling this function does not initiate any activity on the I2C bus.

  Precondition:
    SERCOMx_I2C_Initialize must have been called for the associated SERCOMx I2C
    instance. The required number of TRB should have been configured in MHC.

  Parameters:
    address - 7-bit / 10-bit slave address.

    pdata   - pointer to destination data buffer where the received data will be
              stored. The application should not access the buffer while a
              transfer is in progress.

    length  - Number of bytes to receive. Also the size of the receive buffer.

  Returns:
    true  - TRB submitted successfully and will be executed when the
           SERCOMx_I2C_TRBTransfer() function is called.

    false - Failure while submitting TRB. This can happen if the maximum number
            of TRBs have been built, or if a transfer is in progress, or
            if pdata pointer is NULL or if length is 0.

  Example:
    <code>
        // Refer to the description of the SERCOMx_I2C_TRBTransfer function for
        // example usage.
    </code>

  Remarks:
    Number of times SERCOMx_I2C_TRBBuildRead is called is limited to number of
    TRB's available.
*/

bool SERCOMx_I2C_TRBBuildRead(uint16_t address, uint8_t *pdata, uint8_t length);

// *****************************************************************************
/* Function:
    bool SERCOMx_I2C_TRBBuildWrite(uint16_t address, uint8_t *pdata, uint8_t length)

  Summary:
    Allocates and Builds the Write Transaction Request Block.

  Description:
    This function allocates and builds a Write Transaction Request Block. The
    transaction will be executed when the SERCOMx_I2C_TRBTransfer() function is
    called. A transaction is marked complete when either all the requeste bytes
    have been received or when a bus error or a NAK condition has occurred. The
    application can build multiple Write TRBs.

    The transaction will be executed in the same order in which the build
    function was called. A I2C Repeated Start condition will be placed on the
    bus between each transaction.  The maximum number of TRBs that can be built
    is configurable in MHC. The application should not access the contents of
    the buffer pointed to by pData while a transfer is in progress.

    Calling this function does not initiate any activity on the I2C bus.

  Precondition:
    SERCOMx_I2C_Initialize must have been called for the associated SERCOMx I2C
    instance. The required number of TRB should have been configured in MHC.

  Parameters:
    address - 7-bit / 10-bit slave address.

    pdata   - pointer to source data buffer containing the data to be
              transmitted. The application should not access the buffer while
              a transfer is in progress.

    length - Number of bytes to transmit. Also the size of the transmit buffer.

  Returns:
    true  - TRB submitted successfully and will be executed when the
            SERCOMx_I2C_TRBTransfer() function is called.

    false - Failure while submitting TRB. This can happen if the maximum number
            of TRBs have been built, or if a transfer is in progress, or
            if pdata pointer is NULL or if length is 0.

  Example:
    <code>
        // Refer to the description of the SERCOMx_I2C_TRBTransfer function for
        // example usage.
    </code>

  Remarks:
    Number of times SERCOMx_I2C_TRBBuildWrite is called is limited to number of
    TRB's available.
*/

bool SERCOMx_I2C_TRBBuildWrite(uint16_t address, uint8_t *pdata, uint8_t length);

// *****************************************************************************
/* Function:
    bool SERCOMx_I2C_TRBTransfer(void)

  Summary:
    Submits all TRB's that were built for processing. 

  Description:
    This function submits all TRB's that were built by calling
    SERCOMx_I2C_TRBBuildRead and SERCOMx_I2C_TRBBuildWrite. Calling the transfer
    function will start the transfer. A I2C Repeated Start condition will be
    placed on the bus after the completion of each TRB. A I2C Stop condition
    will placed on the bus after processing the the last TRB.

    The function is non-blocking. It will trigger bus activity and will return
    immediately. The TRBs will be processed in the SERCOM interrupt. The
    transfer function cannot be called while another transfer is in progress.
    Doing so will cause the function to return a false return value. The
    application must use the SERCOM1_I2C_TransferStatusGet() function to get the
    status of an on-going transfer. Alternatively it can register a callback
    function through the SERCOMx_I2C_CallbackRegister() function. This callback
    function will be called when all the TRBs have been processed or when an
    error has occurred.

    The transfer function will process TRBs in the same order in which they were
    built. When a transfer is complete successfully or unsuccessfully, all TRBs
    (including the unprocessed TRBs) will be discarded. In case of an error,
    this may require the TRBs to be re-submitted.

  Precondition:
    SERCOMx_I2C_Initialize must have been called for the associated SERCOM I2C
    instance. The required TRBs should have been built. If a callback function
    is to be called, this should have been registered before calling starting
    the transfer.

  Parameters:
    None.

  Returns:
    true  - TRB processing started successfully and bus activity has been
            initiated.

    false - Failure while submitting TRB. No TRBs were built or there is a
            already a transfer in progress.

  Example:
    <code>
        // The following code example shows how the SERCOMx_I2C_TRBTransfer()
        // function. This example assume that the number of TRB configured in
        // MHC is 3.

        uint8_t writeBuffer[4];
        uint8_t readBuffer1[10];
        uint8_t readBuffer2[20];
        uint16_t slaveAddress = 0x4C;
        bool transferDone = true;
        SERCOM_I2C_ERROR error = SERCOM_I2C_ERROR_NONE;

        void MyI2CCallback(uintptr_t context)
        {
            bool * done = (bool *)(context);
            *done = true;
        }

        SERCOMx_I2C_Initialize();
        SERCOMx_I2C_CallbackRegister(MyI2CCallback, &transferDone);

        // Build the 3 TRBs.
        SERCOMx_I2C_TRBBuildWrite(slaveAddress, writeBuffer, 4);
        SERCOMx_I2C_TRBBuildRead(slaveAddress, readBuffer1, 10);
        SERCOMx_I2C_TRBBuildRead(slaveAddress, readBuffer2, 10);

        // Start processing the TRBs
        SERCOMx_I2C_TRBTransfer();

        // The transferDone flag gets done in the callback function.
        while(transferDone == false);

        // Alternatively we could have called SERCOM1_I2C_TransferStatusGet()
        // function to check if the transfer completed.
        // while(SERCOM_I2C_TRANSFER_BUSY == SERCOMx_I2C_TransferStatusGet());

        if(SERCOM_I2C_TRANSFER_ERROR == SERCOMx_I2C_TransferStatusGet())
        {
            // The transfer completed with an error.
            error = SERCOMx_I2C_ErrorGet();
        }

    </code>

  Remarks:
    None.
*/

bool SERCOMx_I2C_TRBTransfer(void);

// *****************************************************************************
/* Function:
    bool SERCOMx_I2C_Read(uint16_t address, uint8_t *pdata, uint8_t length)

  Summary:
    Reads data from the slave.

  Description:
    This function reads the data from a slave on the bus. The function will
    attempt to read length number of bytes into pdata buffer from a slave whose
    address is specified as address. The I2C Master generate a Start condition,
    read the data and then generate a Stop Conditioni. If the Master lost
    arbitration, then the library will attempt to regain the control of the bus.
    If the slave NAKs the request or a bus error is encountered on the bus, the
    transfer is terminated. The application can call the
    SERCOMx_I2C_TransferStatusGet() function and the SERCOMx_I2C_ErrorGet()
    function to know that cause of the error.

    The function is non-blocking. It initiates bus activity and returns
    immediately. The transfer is completed in the peripheral interrupt. A
    transfer request cannot be placed when another transfer is in progress.
    Calling the read function when another function is already in progress will
    cause the function to return false.

    The library will call the registered callback function when the transfer has
    terminated. Additionally, the SERCOMx_I2C_TransferStatusGet() function will
    return SERCOM_I2C_TRANSFER_ERROR or SERCOM_I2C_TRANSFER_SUCCESS depending on
    the completion status of the transfer. If a callback is desired, this should
    have been registered (by calling the SERCOMx_I2C_CallbackRegister) before
    calling the read function.

  Precondition:
    SERCOMx_I2C_Initialize must have been called for the associated SERCOM I2C
    instance.  At least one TRB should be available.

  Parameters:
    address - 7-bit / 10-bit slave address.

    data    - pointer to destination data buffer where the received data should
              be stored.

    length  - length of data buffer in number of bytes. Also the number of bytes
              to be read.

  Returns:
    true  - The request was placed successfully and the bus activity was
            initiated.

    false - The request failed. No bus activity was initiated. This can happen
            if the receive buffer pointer is NULL, or if the lenght parameter
            is 0 or if there was already a transfer in progress when this
            function was called or if a TRB was not available.

  Example:
    <code>
        uint8_t myData [NUM_BYTES];
        uint8_t myData [NUM_BYTES];
        void MyI2CCallback(uintptr_t context)
        {
            // This function will be called when the transfer completes. Note
            // that this functioin executes in the context of the I2C interrupt.
        }

        SERCOMx_I2C_Initialize();
        SERCOMx_I2C_CallbackRegister(MyI2CCallback, NULL);

        if(!SERCOMx_I2C_Read( SLAVE_ADDR, &myData[0], NUM_BYTES ))
        {
            // error handling
        }

        while(SERCOM_I2C_TRANSFER_BUSY == SERCOMx_I2C_TransferStatusGet())
        {
            // Wait till the transfer completes.
        }

    </code>

  Remarks:
    None.
*/

bool SERCOMx_I2C_Read(uint16_t address, uint8_t *pdata, uint8_t length);

// *****************************************************************************
/* Function:
    bool SERCOMx_I2C_Write(uint16_t address, uint8_t *pdata, uint8_t length)

  Summary:
    Writes data to the slave.

  Description:
    This function writes data to a slave on the bus. The function will attempt
    to write length number of bytes from pdata buffer to a slave whose address
    is specified by address. The I2C Master will generate a Start condition,
    write the data and then generate a Stop Conditioni. If the Master lost
    arbitration, then the library will attempt to regain the control of the bus.
    If the slave NAKs the request or a bus error was encountered on the bus, the
    transfer is terminated. The application can call the
    SERCOMx_I2C_TransferStatusGet() function and the SERCOMx_I2C_ErrorGet()
    function to know that cause of the error.

    The function is non-blocking. It initiates bus activity and returns
    immediately. The transfer is then completed in the peripheral interrupt. A
    transfer request cannot be placed when another transfer is in progress.
    Calling the write function when another function is already in progress will
    cause the function to return false.

    The library will call the registered callback function when the transfer has
    terminated. Additionally, the SERCOMx_I2C_TransferStatusGet() function will
    return SERCOM_I2C_TRANSFER_ERROR or SERCOM_I2C_TRANSFER_SUCCESS depending on
    the completion status of the transfer. If a callback is desired, this should
    should have been register (by calling the SERCOMx_I2C_CallbackRegister)
    before calling the write function.

  Precondition:
    SERCOMx_I2C_Initialize must have been called for the associated SERCOM I2C
    instance.  At least one TRB should be available.

  Parameters:
    address - 7-bit / 10-bit slave address.

    data    - pointer to source data buffer that contains the data to be
              transmitted.

    length  - length of data buffer in number of bytes. Also the number of bytes
              to be written.

  Returns:
    true  - The request was placed successfully and the bus activity was
            initiated.

    false - The request failed. No bus activity was initiated. This can happen
            if the transmit buffer pointer is NULL, or if the lenght parameter
            is 0 or if there was already a transfer in progress when this
            function was called or if a TRB is not available.

  Example:
    <code>
        uint8_t myData [NUM_BYTES];
        void MyI2CCallback(uintptr_t context)
        {
            // This function will be called when the transfer completes. Note
            // that this functioin executes in the context of the I2C interrupt.
        }

        SERCOMx_I2C_Initialize();
        SERCOMx_I2C_CallbackRegister(MyI2CCallback, NULL);

        if(!SERCOMx_I2C_Read( SLAVE_ADDR, &myData[0], NUM_BYTES ))
        {
            // error handling
        }

        while(SERCOM_I2C_TRANSFER_BUSY == SERCOMx_I2C_TransferStatusGet())
        {
            // Wait till the transfer completes.
        }
    </code>

  Remarks:
    None.
*/

bool SERCOMx_I2C_Write(uint16_t address, uint8_t *pdata, uint8_t length);

// *****************************************************************************
/* Function:
    bool SERCOMx_I2C_WriteRead(uint16_t address, uint8_t *wdata, uint8_t wlength,
                                                uint8_t *rdata, uint8_t rlength)

  Summary:
    Write and Read data from Slave.

  Description:
    This function writes data from the wdata to the bus and then reads data from
    the slave and stores the received in the rdata. The function generates a
    Start condition on the bus and will then send wlength number of bytes
    contained in wdata. The function will then insert a Repeated start condition
    and proceeed to read rlength number of bytes from the slave. The received
    bytes are stored in rdata buffer. A Stop condition is generated after the
    last byte has been received.

    If the Master lost arbitration, then the library will attempt to regain the
    control of the bus.  If the slave NAKs the request or a bus error was
    encountered on the bus, the transfer is terminated. The application can call
    the SERCOMx_I2C_TransferStatusGet() function and the SERCOMx_I2C_ErrorGet()
    function to know that cause of the error.

    The function is non-blocking. It initiates bus activity and returns
    immediately. The transfer is then completed in the peripheral interrupt. A
    transfer request cannot be placed when another transfer is in progress.
    Calling this function when another function is already in progress will
    cause the function to return false.

    The library will call the registered callback function when the transfer has
    terminated. Additionally, the SERCOMx_I2C_TransferStatusGet() function will
    return SERCOM_I2C_TRANSFER_ERROR or SERCOM_I2C_TRANSFER_SUCCESS depending on
    the completion status of the transfer. If a callback is desired, this should
    should have been register (by calling the SERCOMx_I2C_CallbackRegister)
    before calling the write function.

  Precondition:
    SERCOMx_I2C_Initialize must have been called for the associated SERCOM I2C
    instance. A minimum of two TRB's should be available.

  Parameters:
    address - 7-bit / 10-bit slave address.

    wdata   - pointer to write data buffer

    wlength - write data length in bytes.

    rdata   - pointer to read data buffer.

    rlength - read data length in bytes.

  Returns:
    true  - The request was placed successfully and the bus activity was
    initiated.

    false - The request failed. No bus activity was initiated. This can happen
            if the transmit/receive buffer pointer is NULL, or if the
            rlength/wlength parameter is 0 or if there was already a transfer
            in progress when this function was called or if a TRB is not
            available.

  Example:
    <code>
        uint8_t myTxData [NUM_BYTES] = {'1', '0', ' ', 'B', 'Y', 'T', 'E', 'S', '!', '!'};
        uint8_t myRxData [NUM_BYTES] = {0};

        void MyI2CCallback(uintptr_t context)
        {
            // This function will be called when the transfer completes. Note
            // that this functioin executes in the context of the I2C interrupt.
        }

        SERCOMx_I2C_Initialize();
        SERCOMx_I2C_CallbackRegister(MyI2CCallback, NULL);
        if(!SERCOMx_I2C_WriteRead( SLAVE_ADDR, &myTxData[0], NUM_BYTES, myRxData, NUM_BYTES ))
        {
            // error handling
        }

        while(SERCOM_I2C_TRANSFER_BUSY == SERCOMx_I2C_TransferStatusGet())
        {
            // Wait till the transfer completes.
        }

    </code>

  Remarks:
    Calling this function is not the same as calling the SERCOMx_I2C_Write()
    function and then calling the SERCOMx_I2C_Read() function.
    The SERCOMx_I2C_WriteRead function will insert a Repeated Start condition
    between the Write and the Read stages. The SERCOMx_I2C_Write() and the
    SERCOMx_I2C_Read() function insert a stop condtion after the write and
    the read has completed.
*/

bool SERCOMx_I2C_WriteRead(uint16_t address, uint8_t *wdata, uint8_t wlength, uint8_t *rdata, uint8_t rlength);

// *****************************************************************************
/* Function:
    SERCOM_I2C_TRANSFER_STATUS SERCOMx_I2C_TransferStatusGet(void)

   Summary:
    Returns the status of an on-going or the last completed transfer.

   Description:
    This function returns the status of an og-going or completed transfer. It
    allows the application to poll the status of the transfer. The function can
    be called in a while loop to implement a blocking check or periodically to
    implement a non-blocking check. The function will return a busy status when
    the transfer is in progress. It will return a successful status if the
    transfer was completed without errors. It will return an error status if the
    transfer completed with errors. The application can call the
    SERCOMx_I2C_ErrorGet() function to find out the actuall error.

   Precondition:
    SERCOMx_I2C_Initialize must have been called for the associated SERCOM I2C
    instance. Any of the transfer functions should have been called atleast once
    before this function is called.

   Parameters:
    None.

   Returns:
    A SERCOM_I2C_TRANSFER_STATUS status of the transfer. Refer to the
    description of the SERCOM_I2C_TRANSFER_STATUS enumeration for details.

   Example:
    <code>
        // Refer to the description of the SERCOMx_I2C_WriteRead() function for
        // example usage.
    </code>

   Remarks:
    None.
*/

SERCOM_I2C_TRANSFER_STATUS SERCOMx_I2C_TransferStatusGet(void);

// *****************************************************************************
/* Function:
    bool SERCOMx_I2C_IsBusy(void)

  Summary:
    Returns the Peripheral busy status.

  Description:
    This function ture if the SERCOMx I2C module is busy with a
    transfer. The application can use the function to check if SERCOMx I2C
    module is busy before calling any of the data transfer functions. The
    library does not allow a data transfer operation if another transfer
    operation is already in progress.

  Precondition:
    SERCOMx_I2C_Initialize must have been called for the
    associated SERCOM instance.

  Parameters:
    None.

  Returns:
    true - Busy.
    false - Not busy.

  Example:
    <code>
        uint8_t myData [NUM_BYTES] = {'1', '0', ' ', 'B', 'Y', 'T', 'E', 'S', '!', '!'};

        // wait for the current transfer to complete
        while(SERCOMx_I2C_IsBusy( ));

        // perform the next transfer
        if(!SERCOMx_I2C_Write( SLAVE_ADDR, &myData[0], NUM_BYTES ))
        {
            // error handling
        }

    </code>

  Remarks:
    None.
*/

bool SERCOMx_I2C_IsBusy(void);

// *****************************************************************************
/* Function:
    SERCOM_I2C_ERROR SERCOMx_I2C_ErrorGet(void)

  Summary:
    Returns the latest error that occurred on the bus.

  Description:
    This function returns the latest error that occurred on the bus. The
    function can be called to identify the error cause when the
    SERCOMx_I2C_TransferStatusGet() function returns a SERCOM_I2C_TRANSFER_ERROR
    status. The errors are cleared when the next transfer function is initiated.

  Precondition:
    SERCOMx_I2C_Initialize must have been called for the associated SERCOM I2C
    instance.

  Parameters:
    None.

  Returns:
    Returns a SERCOM_I2C_ERROR type of status identifying the error that has
    occurred.

  Example:
    <code>
    // Refer to the description of the SERCOMx_I2C_TRBTransfer() function for
    // example usage.
    </code>

  Remarks:
    None.
*/

SERCOM_I2C_ERROR SERCOMx_I2C_ErrorGet(void);

// *****************************************************************************
/* Function:
    void SERCOMx_I2C_CallbackRegister(SERCOM_I2C_CALLBACK callback, uintptr_t context)

   Summary:
    Sets the pointer to the function (and it's context) to be called when the
    given SERCOM I2C's transfer events occur.

  Description:
    This function sets the pointer to a client function to be called "back" when
    the given SERCOM I2C's transfer events occur. It also passes a context value
    (usually a pointer to a context structure) that is passed into the function
    when it is called. The specified callback function will be called from the
    peripheral interrupt context.

  Precondition:
    SERCOMx_I2C_Initialize must have been called for the associated SERCOM I2C
    instance.

  Parameters:
    callback      - A pointer to a function with a calling signature defined by
                    the SERCOM_I2C_CALLBACK data type. Setting this to NULl
                    disables the callback feature.

    contextHandle - A value (usually a pointer) passed (unused) into the
                    function identified by the callback parameter.

  Returns:
    None.

  Example:
    <code>
        // Refer to the description of the SERCOM_I2C_CALLBACK data type for
        // example usage.
    </code>

  Remarks:
    None.
*/

void SERCOMx_I2C_CallbackRegister(SERCOM_I2C_CALLBACK callback, uintptr_t contextHandle);

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility
}
#endif
// DOM-IGNORE-END

#endif /* PLIB_SERCOMx_I2C_H */