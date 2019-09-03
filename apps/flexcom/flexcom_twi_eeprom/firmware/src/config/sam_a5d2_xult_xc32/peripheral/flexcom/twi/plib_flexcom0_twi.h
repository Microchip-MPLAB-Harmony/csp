/*******************************************************************************
  FLEXCOM TWI Peripheral Library Interface Header File

  Company
    Microchip Technology Inc.

  File Name
    plib_flexcom0_twi.h

  Summary
    FLEXCOM TWI peripheral library interface.

  Description
    This file defines the interface to the FLEXCOM TWI peripheral library.  This
    library provides access to and control of the associated peripheral
    instance.

  Remarks:

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

#ifndef PLIB_FLEXCOM0_TWI_H
#define PLIB_FLEXCOM0_TWI_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

/*  This section lists the other files that are included in this file.
*/
#include "plib_flexcom_twi_master.h"

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
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************
/* The following functions make up the methods (set of possible operations) of
   this interface.
*/

// *****************************************************************************
/* Function:
    void FLEXCOM0_TWI_Initialize(void)

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
    FLEXCOM0_TWI_Initialize();
    </code>

   Remarks:
    Stops the FLEXCOM TWI if it was already running and reinitializes it.
*/

void FLEXCOM0_TWI_Initialize(void);

// *****************************************************************************
/* Function:
    void FLEXCOM0_TWI_CallbackRegister(FLEXCOM_TWI_CALLBACK callback, uintptr_t contextHandle)

   Summary:
    Sets the pointer to the function (and it's context) to be called when the
    given FLEXCOM TWI's transfer events occur.

   Description:
    This function sets the pointer to a client function to be called "back"
    when the given FLEXCOM TWI's transfer events occur. It also passes a context value
    (usually a pointer to a context structure) that is passed into the
    function when it is called.

   Precondition:
    FLEXCOM0_TWI_Initialize must have been called for the associated FLEXCOM TWI instance.

   Parameters:
    callback - A pointer to a function with a calling signature defined
    by the FLEXCOM_TWI_CALLBACK data type.

    context - A value (usually a pointer) passed (unused) into the function
    identified by the callback parameter.

   Returns:
    None.

   Example:
    <code>
    FLEXCOM0_TWI_CallbackRegister(MyFlexcomTwiCallback, &myData);
    </code>

   Remarks:
    The context parameter is ignored if the pointer passed is NULL.
    To disable the callback function, pass a NULL for the callback parameter.
    See the FLEXCOM_TWI_CALLBACK type definition for additional information.
*/

void FLEXCOM0_TWI_CallbackRegister(FLEXCOM_TWI_CALLBACK callback, uintptr_t contextHandle);

// *****************************************************************************
/* Function:
    bool FLEXCOM0_TWI_IsBusy(void)

   Summary:
    Returns the Peripheral busy status.

   Description:
    This function returns the peripheral's busy status.

   Precondition:
    FLEXCOM0_TWI_Initialize must have been called for the associated FLEXCOM TWI instance.

   Parameters:
    None.

   Returns:
    true - Busy.
    false - Not busy.

   Example:
    <code>
        uint8_t myData [NUM_BYTES] = {'1', '0', ' ', 'B', 'Y', 'T', 'E', 'S', '!', '!',};

        // wait for the current transfer to complete
        while(FLEXCOM0_TWI_IsBusy( ));

        // perform the next transfer
        if(!FLEXCOM0_TWI_Write( SLAVE_ADDR, &myData[0], NUM_BYTES ))
        {
            // error handling
        }

    </code>

   Remarks:
    None.
*/

bool FLEXCOM0_TWI_IsBusy(void);

// *****************************************************************************
/* Function:
    bool FLEXCOM0_TWI_Read(uint16_t address, uint8_t *pdata, size_t length)

   Summary:
    Reads data from the slave.

   Description:
    This function reads the data of size in bytes equal to length into pdata buffer
    from the slave having given address. Master will generate Stop condition after
    completion of the read.

   Precondition:
    FLEXCOM0_TWI_Initialize must have been called for the associated FLEXCOM TWI instance.

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

        if(!FLEXCOM0_TWI_Read( SLAVE_ADDR, &myData[0], NUM_BYTES ))
        {
            // error handling
        }
    </code>

   Remarks:
    None.
*/

bool FLEXCOM0_TWI_Read(uint16_t address, uint8_t *pdata, size_t length);

// *****************************************************************************
/* Function:
    bool FLEXCOM0_TWI_Write(uint16_t address, uint8_t *pdata, size_t length)

   Summary:
    Writes data onto the slave.

   Description:
    This function writes the data from pdata buffer of size in bytes equal to
    length onto the slave with given address. Master will generate Stop
    condition after completion of the write.

   Precondition:
    FLEXCOM0_TWI_Initialize must have been called for the associated FLEXCOM TWI instance.

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

        if(!FLEXCOM0_TWI_Write( SLAVE_ADDR, &myData[0], NUM_BYTES ))
        {
            // error handling
        }
    </code>

   Remarks:
    None.
*/

bool FLEXCOM0_TWI_Write(uint16_t address, uint8_t *pdata, size_t length);

// *****************************************************************************
/* Function:
    bool FLEXCOM0_TWI_WriteRead(uint16_t address, uint8_t *wdata, size_t wlength, uint8_t *rdata, size_t rlength)

   Summary:
    Write and Read data from Slave.

   Description:
    This function writes data from wdata buffer to the slave of given address and
    of size(in bytes) equal to wlength. Master then generates a repeated start and
    do a read operation. Read operation reads data into rdata buffer of size(in
    bytes) equal to rlength from the slave of given address. Master generates a stop
    condition after reading the data.

   Precondition:
    FLEXCOM0_TWI_Initialize must have been called for the associated FLEXCOM TWI instance.

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

        if(!FLEXCOM0_TWI_WriteRead( SLAVE_ADDR, &myTxData[0], NUM_BYTES, myRxData, NUM_BYTES ))
        {
            // error handling
        }
    </code>

   Remarks:
*/

bool FLEXCOM0_TWI_WriteRead(uint16_t address, uint8_t *wdata, size_t wlength, uint8_t *rdata, size_t rlength);

// *****************************************************************************
/* Function:
    FLEXCOM_TWI_ERROR FLEXCOM0_TWI_ErrorGet(void)

   Summary:
    Returns the error during transfer.

   Description:
    This function returns the error during transfer.

   Precondition:
    FLEXCOM0_TWI_Initialize must have been called for the associated FLEXCOM TWI instance.

   Parameters:
    None.

   Returns:
    Request status.
    True - Request was successful.
    False - Request has failed.

   Example:
    <code>
    if(FLEXCOM_TWI_ERROR_NONE == FLEXCOM0_TWI_ErrorGet())
    {
        //FLEXCOM TWI transfer is completed, go to next state.
    }
    </code>

   Remarks:
    None.
*/

FLEXCOM_TWI_ERROR FLEXCOM0_TWI_ErrorGet(void);

// *****************************************************************************
/* Function:
    bool FLEXCOM0_TWI_TransferSetup(FLEXCOM_TWI_TRANSFER_SETUP* setup, uint32_t srcClkFreq)

   Summary:
    Dynamic setup of FLEXCOM TWI Peripheral.

   Precondition:
    FLEXCOM0_Initialize must have been called for the associated TWI instance.
    The transfer status should not be busy.

   Parameters:
    setup - Pointer to the structure containing the transfer setup.
    srcClkFreq - TWI Peripheral Clock Source Frequency.

   Returns:
    true - Transfer setup was updated Successfully.
    false - Failure while updating transfer setup.

   Example:
    <code>

    FLEXCOM_TWI_TRANSFER_SETUP setup;

    setup.clkSpeed = 400000;

    // Make sure that the I2C is not busy before changing the I2C clock frequency
    if (FLEXCOM0_TWI_IsBusy() == false)
    {
        if (FLEXCOM0_TWI_TransferSetup( &setup, 0 ) == true)
        {
            // Transfer Setup updated successfully
        }
    }
    </code>

   Remarks:
    srcClkFreq overrides any change in the peripheral clock frequency.
    If configured to zero PLib takes the peripheral clock frequency from MHC.
*/

bool FLEXCOM0_TWI_TransferSetup(FLEXCOM_TWI_TRANSFER_SETUP* setup, uint32_t srcClkFreq );

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END

#endif //PLIB_FLEXCOM0_TWI_H

/*******************************************************************************
 End of File
*/
