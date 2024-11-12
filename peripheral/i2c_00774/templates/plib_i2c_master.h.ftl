/*******************************************************************************
  Serial Communication Interface Inter-Integrated Circuit (I2C) Library
  Instance Header File

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${I2C_INSTANCE_NAME?lower_case}_master.h

  Summary:
    I2C PLIB Master Mode Header file

  Description:
    This file defines the interface to the I2C peripheral library. This
    library provides access to and control of the associated peripheral
    instance.
*******************************************************************************/
// DOM-IGNORE-BEGIN
/*******************************************************************************
* Copyright (C) 2018-2019 Microchip Technology Inc. and its subsidiaries.
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

#ifndef PLIB_${I2C_INSTANCE_NAME}_MASTER_H
#define PLIB_${I2C_INSTANCE_NAME}_MASTER_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
/* This section lists the other files that are included in this file.
*/

#include "plib_i2c_master_common.h"

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

/*
 * The following functions make up the methods (set of possible operations) of
 * this interface.
 */

// *****************************************************************************
/* Function:
    void ${I2C_INSTANCE_NAME}_Initialize(void)

  Summary:
    Initializes the instance of the I2C peripheral operating in I2C mode.

  Description:
    This function initializes the given instance of the I2C peripheral as
    configured by the user from the MHC.

  Precondition:
    The Generic Clock Generator should have been assigned to the I2Cx
    Peripheral Clock Channel.

  Parameters:
    None.

  Returns:
    None.

  Example:
    <code>
        ${I2C_INSTANCE_NAME}_Initialize();
    </code>

  Remarks:
    Stops the I2C if it was already running and reinitializes it.
*/

void ${I2C_INSTANCE_NAME}_Initialize(void);

// *****************************************************************************
/* Function:
    bool ${I2C_INSTANCE_NAME}_Read(uint16_t address, uint8_t *pdata, size_t length)

  Summary:
    Reads data from the slave.

  Description:
    This function reads the data from a slave on the bus. The function will
    attempt to read length number of bytes into pdata buffer from a slave whose
    address is specified as address. The I2C Master generate a Start condition,
    read the data and then generate a Stop Condition.
    If the slave NAKs the request or a bus error is encountered on the bus, the
    transfer is terminated. The application can call ${I2C_INSTANCE_NAME}_ErrorGet()
    function to know that cause of the error.

    The function is non-blocking. It initiates bus activity and returns
    immediately. The transfer is completed in the peripheral interrupt. A
    transfer request cannot be placed when another transfer is in progress.
    Calling the read function when another function is already in progress will
    cause the function to return false.

    The library will call the registered callback function when the transfer has
    terminated if callback is registered.

  Precondition:
    ${I2C_INSTANCE_NAME}_Initialize must have been called for the associated
    I2C instance.

  Parameters:
    address - 7-bit / 10-bit slave address.

    data    - pointer to destination data buffer where the received data should
              be stored.

    length  - length of data buffer in number of bytes. Also the number of bytes
              to be read.

  Returns:
    true  - The request was placed successfully and the bus activity was
            initiated.

    false - The request fails,if there was already a transfer in progress when this
            function was called.

  Example:
    <code>
        uint8_t myData [NUM_BYTES];
        uint8_t myData [NUM_BYTES];
        void MyI2CCallback(uintptr_t context)
        {

        }

        ${I2C_INSTANCE_NAME}_Initialize();
        ${I2C_INSTANCE_NAME}_CallbackRegister(MyI2CCallback, NULL);

        if(!${I2C_INSTANCE_NAME}_Read( SLAVE_ADDR, &myData[0], NUM_BYTES ))
        {

        }


    </code>

  Remarks:
    None.
*/

bool ${I2C_INSTANCE_NAME}_Read(uint16_t address, uint8_t* rdata, size_t rlength);

// *****************************************************************************
/* Function:
    bool ${I2C_INSTANCE_NAME}_Write(uint16_t address, uint8_t *pdata, size_t length)

  Summary:
    Writes data to the slave.

  Description:
    This function writes data to a slave on the bus. The function will attempt
    to write length number of bytes from pdata buffer to a slave whose address
    is specified by address. The I2C Master will generate a Start condition,
    write the data and then generate a Stop Condition. If the slave NAKs the request
    or a bus error was encountered on the bus, the transfer is terminated. The
    application can call the ${I2C_INSTANCE_NAME}_ErrorGet() function to know that
    cause of the error.

    The function is non-blocking. It initiates bus activity and returns
    immediately. The transfer is then completed in the peripheral interrupt. A
    transfer request cannot be placed when another transfer is in progress.
    Calling the write function when another function is already in progress will
    cause the function to return false.

    The library will call the registered callback function when the transfer has
    terminated.

  Precondition:
    ${I2C_INSTANCE_NAME}_Initialize must have been called for the associated
    I2C instance.

  Parameters:
    address - 7-bit / 10-bit slave address.

    pdata   - pointer to source data buffer that contains the data to be
              transmitted.

    length  - length of data buffer in number of bytes. Also the number of bytes
              to be written.

  Returns:
    true  - The request was placed successfully and the bus activity was
    initiated.

    false - The request fails,if there was already a transfer in progress when this function
            was called. .

  Example:
    <code>
        uint8_t myData [NUM_BYTES];
        void MyI2CCallback(uintptr_t context)
        {

        }

        ${I2C_INSTANCE_NAME}_Initialize();
        ${I2C_INSTANCE_NAME}_CallbackRegister(MyI2CCallback, NULL);

        if(!${I2C_INSTANCE_NAME}_Write( SLAVE_ADDR, &myData[0], NUM_BYTES ))
        {

        }

    </code>

  Remarks:
    None.
*/

bool ${I2C_INSTANCE_NAME}_Write(uint16_t address, uint8_t* wdata, size_t wlength);

<#if I2C_INCLUDE_FORCED_WRITE_API == true>
// *****************************************************************************
/* Function:
    bool ${I2C_INSTANCE_NAME}_WriteForced(uint16_t address, uint8_t* pdata, size_t length)

  Summary:
    Writes data to the slave.

  Description:
    Master calls this function to transmit the entire buffer to the slave even
    if the slave ACKs or NACKs the address or any of the data bytes. This is
    typically used for slaves that have to initiate a reset sequence by sending
    a dummy I2C transaction. Since the slave is still in reset, any or all the
    bytes can be NACKed. In the normal operation, if the address or data byte is
    NACKed, then the transmission is aborted and a STOP condition is asserted on
    the bus.

    This function writes data to a slave on the bus. The function will attempt
    to write length number of bytes from pdata buffer to a slave whose address
    is specified by address. The I2C Master will generate a Start condition,
    write the data and then generate a Stop Condition.

    The function is non-blocking. It initiates bus activity and returns
    immediately. The transfer is then completed in the peripheral interrupt. A
    transfer request cannot be placed when another transfer is in progress.

    The library will call the registered callback function when the transfer has
    terminated.

  Precondition:
    ${I2C_INSTANCE_NAME}_Initialize must have been called for the associated
    I2C instance.

  Parameters:
    address - 7-bit / 10-bit slave address.

    pdata   - pointer to source data buffer that contains the data to be
              transmitted.

    length  - length of data buffer in number of bytes. Also the number of bytes
              to be written.

  Returns:
    true  - The request was placed successfully and the bus activity was
    initiated.

    false - The request fails,if there was already a transfer in progress when this function
            was called.

  Example:
    <code>
        uint8_t myData [NUM_BYTES];
        void MyI2CCallback(uintptr_t context)
        {

        }

        ${I2C_INSTANCE_NAME}_Initialize();
        ${I2C_INSTANCE_NAME}_CallbackRegister(MyI2CCallback, NULL);

        if(!${I2C_INSTANCE_NAME}_WriteForced( SLAVE_ADDR, &myData[0], NUM_BYTES ))
        {

        }

    </code>

  Remarks:
    None.
*/

bool ${I2C_INSTANCE_NAME}_WriteForced(uint16_t address, uint8_t* wdata, size_t wlength);
</#if>

// *****************************************************************************
/* Function:
    bool ${I2C_INSTANCE_NAME}_WriteRead(uint16_t address, uint8_t* wdata,
                               size_t wlength, uint8_t* rdata, size_t rlength)

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

    If the slave NAKs the request or a bus error was encountered on the bus,
    the transfer is terminated. The application can call ${I2C_INSTANCE_NAME}_ErrorGet()
    function to know that cause of the error.

    The function is non-blocking. It initiates bus activity and returns
    immediately. The transfer is then completed in the peripheral interrupt. A
    transfer request cannot be placed when another transfer is in progress.
    Calling this function when another function is already in progress will
    cause the function to return false.

    The library will call the registered callback function when the transfer has
    terminated.

  Precondition:
    ${I2C_INSTANCE_NAME}_Initialize must have been called for the associated
    I2C instance.

  Parameters:
    address - 7-bit / 10-bit slave address.

    wdata   - pointer to write data buffer

    wlength - write data length in bytes.

    rdata   - pointer to read data buffer.

    rlength - read data length in bytes.

  Returns:
    true  - The request was placed successfully and the bus activity was
    initiated.

    false - The request fails, if there was already a transfer in progress when this
    function was called.

  Example:
    <code>
        uint8_t myTxData [NUM_BYTES] = {'1', '0', ' ', 'B', 'Y', 'T', 'E', 'S'};
        uint8_t myRxData [NUM_BYTES] = {0};

        void MyI2CCallback(uintptr_t context)
        {

        }

        ${I2C_INSTANCE_NAME}_Initialize();
        ${I2C_INSTANCE_NAME}_CallbackRegister(MyI2CCallback, NULL);
        if(!${I2C_INSTANCE_NAME}_WriteRead( SLAVE_ADDR, &myTxData[0], NUM_BYTES, myRxData, NUM_BYTES ))
        {

        }


    </code>

  Remarks:
    Calling this function is not the same as calling the ${I2C_INSTANCE_NAME}_Write()
    function and then calling the ${I2C_INSTANCE_NAME}_Read() function.
    The ${I2C_INSTANCE_NAME}_WriteRead function will insert a Repeated Start
    condition between the Write and the Read stages. The ${I2C_INSTANCE_NAME}_Write()
    and the ${I2C_INSTANCE_NAME}_Read() function insert a stop condtion after
    the write and the read has completed.
*/

bool ${I2C_INSTANCE_NAME}_WriteRead(uint16_t address, uint8_t* wdata, size_t wlength, uint8_t* rdata, size_t rlength);


// *****************************************************************************
/* Function:
    bool ${I2C_INSTANCE_NAME}_IsBusy(void)

  Summary:
    Returns the Peripheral busy status.

  Description:
    This function ture if the I2C ${I2C_INSTANCE_NAME}I2C module is busy with a
    transfer. The application can use the function to check if I2C
    ${I2C_INSTANCE_NAME}I2C module is busy before calling any of the data transfer
    functions. The library does not allow a data transfer operation if another
    transfer operation is already in progress.

  Precondition:
    ${I2C_INSTANCE_NAME}_Initialize must have been called for the
    associated I2C instance.

  Parameters:
    None.

  Returns:
    true - Busy.
    false - Not busy.

  Example:
    <code>
        uint8_t myData [NUM_BYTES] = {'1', '0', ' ', 'B', 'Y', 'T', 'E', 'S', '!', '!'};


        while(${I2C_INSTANCE_NAME}_IsBusy( ));

        if(!${I2C_INSTANCE_NAME}_Write( SLAVE_ADDR, &myData[0], NUM_BYTES ))
        {

        }

    </code>

  Remarks:
    None.
*/

bool ${I2C_INSTANCE_NAME}_IsBusy(void);

// *****************************************************************************
/* Function:
    I2C_ERROR ${I2C_INSTANCE_NAME}_ErrorGet(void)

  Summary:
    Returns the error occured during transfer.

  Description:
    This function returns the error during transfer.

  Precondition:
    ${I2C_INSTANCE_NAME}_Initialize must have been called for the
    associated I2C instance.

  Parameters:
    None.

  Returns:
    Returns a I2C_ERROR type of status identifying the error that has
    occurred.

    Example:
    <code>
    if(I2C_ERROR_NONE == ${I2C_INSTANCE_NAME}_ErrorGet())
    {

    }
    </code>

  Remarks:
    None.
*/

I2C_ERROR ${I2C_INSTANCE_NAME}_ErrorGet(void);

// *****************************************************************************
/* Function:
    void ${I2C_INSTANCE_NAME}_CallbackRegister(I2C_CALLBACK callback,
                                                              uintptr_t context)

   Summary:
    Sets the pointer to the function (and it's context) to be called when the
    given I2C's transfer events occur.

  Description:
    This function sets the pointer to a client function to be called "back" when
    the given I2C's transfer events occur. It also passes a context value
    (usually a pointer to a context structure) that is passed into the function
    when it is called. The specified callback function will be called from the
    peripheral interrupt context.

  Precondition:
    ${I2C_INSTANCE_NAME}_Initialize must have been called for the associated
    I2C instance.

  Parameters:
    callback      - A pointer to a function with a calling signature defined by
                    the I2C_CALLBACK data type. Setting this to NULL
                    disables the callback feature.

    contextHandle - A value (usually a pointer) passed (unused) into the
                    function identified by the callback parameter.

  Returns:
    None.

  Example:
    <code>

    </code>

  Remarks:
    None.
*/

void ${I2C_INSTANCE_NAME}_CallbackRegister(I2C_CALLBACK callback, uintptr_t contextHandle);

// *****************************************************************************
/* Function:
    bool ${I2C_INSTANCE_NAME}_TransferSetup(I2C_TRANSFER_SETUP* setup, uint32_t srcClkFreq)

   Summary:
    Dynamic setup of I2C Peripheral.

   Precondition:
    ${I2C_INSTANCE_NAME}_Initialize must have been called for the associated I2C instance.
    The transfer status should not be busy.

   Parameters:
    setup - Pointer to the structure containing the transfer setup.
    srcClkFreq - I2C Peripheral Clock Source Frequency.

   Returns:
    true - Transfer setup was updated Successfully.
    false - Failure while updating transfer setup.

   Example:
    <code>

    I2C_TRANSFER_SETUP setup;

    setup.clkSpeed = 400000;

    Make sure that the I2C is not busy before changing the I2C clock frequency
    if (${I2C_INSTANCE_NAME}_IsBusy() == false)
    {
        if (${I2C_INSTANCE_NAME}_TransferSetup( &setup, 0 ) == true)
        {

        }
    }
    </code>

   Remarks:
    srcClkFreq overrides any change in the peripheral clock frequency.
    If configured to zero PLib takes the peripheral clock frequency from MHC.
*/

bool ${I2C_INSTANCE_NAME}_TransferSetup(I2C_TRANSFER_SETUP* setup, uint32_t srcClkFreq );

void ${I2C_INSTANCE_NAME}_TransferAbort( void );

// *****************************************************************************
/* Function:
    bool ${I2C_INSTANCE_NAME}_BusScan(uint16_t start_addr, uint16_t end_addr, void* pDevicesList, uint8_t* nDevicesFound)

   Summary:
    Scan the target devices on the I2C bus.

   Precondition:
    ${I2C_INSTANCE_NAME}_Initialize must have been called for the associated I2C instance.
    The transfer status should not be busy.

   Parameters:
    start_addr - Starting address of the target device.
    end_addr - Ending address of the target device.
    pDevicesList - Pointer to the application buffer where the address of the devices found on the bus will be returned.
    nDevicesFound - Indicates number of devices found on the bus

   Returns:
    true - The call to this API executed successfully.
    false - There was an error during the execution of this API.

   Example:
    <code>

    uint8_t nDevicesFoundList[10] = {0};
    uint8_t nDevFound = 0;

    ${I2C_INSTANCE_NAME}_BusScan(0x08, 0x77, nDevicesFoundList, &nDevFound);

    </code>

   Remarks:
    If there is a mix of devices with 8 and 10 bit addresses on the bus, then this API must be called separately for
    devices with 8-bit addresses and then for devices with 10-bit addresses.
*/
bool ${I2C_INSTANCE_NAME}_BusScan(uint16_t start_addr, uint16_t end_addr, void* pDevicesList, uint8_t* nDevicesFound);


// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility
}
#endif
// DOM-IGNORE-END

#endif /* PLIB_${I2C_INSTANCE_NAME}_MASTER_H */





















