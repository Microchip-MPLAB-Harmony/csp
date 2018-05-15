/******************************************************************************
  SERIAL COMMUNICATION SERIAL PERIPHERAL INTERFACE (SERCOM SPI) PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_sercom_spi.h

  Summary
   SERCOM_SPI Peripheral Library Interface Header File.

  Description
    This file defines the interface to the SERCOM SPI peripheral library.
    This library provides access to and control of the associated
    peripheral instance.

  Remarks:
    This header is for documentation only.  The actual plib_sercom<x>_spi
    headers will be generated as required by the MCC (where <x> is the
    sercom instance number).

    Every interface symbol has a lower-case 'x' in it following the "SERCOM"
    abbreviation.  This 'x' will be replaced by the sercom instance number
    in the generated headers.  These are the actual functions that should be
    used.

*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
Copyright (c) 2017 released Microchip Technology Inc. All rights reserved.
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

#ifndef PLIB_SERCOMx_SPI_H
#define PLIB_SERCOMx_SPI_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
/* This section lists the other files that are included in this file.
*/

#include <stdint.h>
#include <stddef.h>
#include <stdbool.h>

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
    /* Input data is valid on clock trailing edge and output data is ready on
       leading edge */
    SPI_CLOCK_PHASE_TRAILING_EDGE,
    
    /* Input data is valid on clock leading edge and output data is ready on
       trailing edge */
    SPI_CLOCK_PHASE_LEADING_EDGE
    
} SPI_CLOCK_PHASE;

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
    
} SPI_CLOCK_POLARITY;

// *****************************************************************************
/* SPI Data Bits

   Summary:
    Identifies SPI bits per transfer

   Description:
    This enumeration identifies number of bits per SPI transfer.

   Remarks:
    For 9 modes, data should be right aligned in the 16 bit memory location.
*/

typedef enum
{
    /* 8 bits per transfer */
    SPI_DATA_BITS_8,
    
    /* 9 bits per transfer */    
    SPI_DATA_BITS_9,
    
} SPI_DATA_BITS;

// *****************************************************************************
/* SPI Setup Parameters

   Summary
    Identifies the setup parameters which can be changed at run time.

   Description
    This structure identifies the possible setup parameters for SPI which can be
    changed at run time.

   Remarks:
    None.
*/

typedef struct
{   

    /* Baud Rate or clock frequency in bits per second */
    uint32_t clockFrequency;
    
    /* Clock Phase */
    SPI_CLOCK_PHASE clockPhase;
    
    /* Clock Polarity */
    SPI_CLOCK_POLARITY clockPolarity;
    
    /* Number of bits per transfer */
    SPI_DATA_BITS dataBits;
    
} SPI_TRANSFER_SETUP;

// *****************************************************************************
/* SPI Errors

   Summary:
    Identifies the possible SPI Errors.

   Description:
    This enumeration identifies the possible SPI Errors.

   Remarks:
    None.
*/

typedef enum 
{
    /* No Error */
    SPI_ERROR_NONE,
    
    /* SPI Receive Overrun Error */
    SPI_ERROR_OVERRUN
    
} SPI_ERROR;

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
    void SERCOMx_SPI_Initialize (void);
    
  Summary:
    Initializes instance x of the SERCOM module operating in SPI mode.
    
  Description:
    This function initializes instance x of SERCOM module operating in SPI mode.
    This function should be called before any other library function. The SERCOM
    module will be configured as per the MHC settings. 
  
  Precondition:
    MCC GUI should be configured with the right values. The Generic Clock
    configuration and the SERCOM Peripheral Clock channel should have been
    configured in the clock manager GUI.The function will itself enable the
    required peripheral clock channel and main clock.
  
  Parameters:
    None.
  
  Returns:
    None.
    
  Example:
    <code>
        SERCOM1_SPI_Initialize();
    </code>
    
  Remarks:
    This function must be called once before any other SPI function is called.                                            
*/

void SERCOMx_SPI_Initialize (void);

// *****************************************************************************
/* Function:
    bool SPIx_TransferSetup(SPI_TRANSFER_SETUP *setup, uint32_t spiSourceClock);
    
  Summary:
    Configure SERCOM SPI operational parameters at run time.
    
  Description:
    This function allows the application to change the SERCOM SPI operational
    parameter at run time. The application can thus override the MHC defined
    configuration for these parameters. The parameter are specified via the
    SPI_TRANSFER_SETUP type setup parameter. Each member of this parameter
    should be initialized to the desired value.

    The application may feel need to call this function in situation where
    multiple SPI slaves, each with different operation parameters, are connected
    to one SPI master. This function can thus be used to setup the SPI Master to
    meet the communication needs of the slave.

    Calling this function will affect any ongoing communication. The application
    must thus ensure that there is no on-going communication on the SPI before
    calling this function. 
  
  Precondition:
    SERCOM x SPI must first be initialized using SERCOMx_SPI_Initialize().
  
  Parameters :
    setup - pointer to the data structure of type SPI_TRANSFER_SETUP containing
    the operation parameters. Each operation parameter must be specified even if
    the parameter does not need to change.

    spiSourceClock - Current value of GCLK frequency feeding the SERCOMx core.
  
  Returns:
    true - setup was successful.
    
    false - if spiSourceClock and spi clock frequencies are such that resultant
    baud value is out of the possible range.
    
  Example:
    <code> 
        SPI_TRANSFER_SETUP setup;
        setup.clockFrequency = 1000000;
        setup.clockPhase = SPI_CLOCK_PHASE_TRAILING_EDGE;
        setup.clockPolarity = SPI_CLOCK_POLARITY_IDLE_LOW;
        setup.dataBits = SPI_DATA_BITS_8;
        
        // Assuming 20 MHz as peripheral Master clock frequency
        if (SERCOM1_SPI_TransferSetup (&setup, 20000000) == false)
        {
            // this means setup could not be done, debug the reason.
        }
        
    </code>
    
  Remarks:
    The application would need to call this function only if the operational
    parameter need to be different than the ones configured in MHC.
*/

bool SERCOMx_SPI_TransferSetup (SPI_TRANSFER_SETUP *setup, uint32_t spiSourceClock);

// *****************************************************************************
/* Function:
    bool SERCOMx_SPI_WriteRead ( void * pTransmitData, size_t txSize, 
                                        void * pReceiveData, size_t rxSize);

  Summary:
    Write and Read data on SERCOM x SPI peripheral. 

  Description:
    This function transmits "txSize" number of bytes and receives "rxSize"
    number of bytes on SERCOM x SPI module. Data pointed by pTransmitData is
    transmitted and received data is saved in the location pointed by
    pReceiveData. The function will transfer the maximum of "txSize" or "rxSize"
    data units towards completion.
    
    When "Interrupt Mode" option is unchecked in MHC, this function will be
    blocking in nature.  In this mode, the function will not return until all
    the requested data is transferred.  The function returns true after
    transferring all the data.  This indicates that the operation has been
    completed.

    When "Interrupt Mode" option is selected in MHC, the function will be
    non-blocking in nature.  The function returns immediately. The data transfer
    process continues in the peripheral interrupt.  The application specified
    transmit and receive buffer  are owned by the library until the data
    transfer is complete and should not be modified by the application till the
    transfer is complete.  Only one transfer is allowed at any time. The
    Application can use a callback function or a polling function to check for
    completion of the transfer. If a callback is required, this should be
    registered prior to calling the SERCOMx_SPI_WriteRead() function. The
    application can use the SERCOMx_SPI_IsBusy() to poll for completion.
        
  Precondition:
    The SERCOMx_SPI_Initialize function must have been called.  If the
    peripheral instance has been configured for Interrupt mode and transfer
    completion status needs to be communicated back to application via callback,
    a callback should have been registered using SERCOMx_SPI_CallbackRegister()
    function.

  Parameters:
    pTransmitData - Pointer to the data which has to be transmitted. In a case
    where only data reception is required, this pointer can be set to NULL. If
    the module is configured for 9 bit data length, the data should be right
    aligned in a 16 bit memory location. The size of this buffer should be
    txSize.

    txSize - Number of bytes to be transmitted. This value is always the number
    of bytes contained in the buffer. For 9 bit data length, this value should
    be even. This value can be different from rxSize.
                    
    pReceiveData - Pointer to the location where the received data has to be
    stored.  It is user's responsibility to ensure that this location has
    sufficient memory to store rxSize amount of data. In a case where only data
    transmission is required, this pointer can be set to NULL.  If the module is
    configured for 9 bit data length, received data will be right aligned and
    will be stored in a 16 bit memory location.

    rxSize - Number of bytes to be received. This value can be different from
    txSize. This value is always the number of bytes contained in the buffer.
    For 9 bit data length, this value should be even..  

  Returns:
    true - If configured for Non-interrupt mode, the function has recevied and
    transmitted the requested number of bytes. If configured for Interrupt mode,
    the request was accepted successfully and will be processed in the
    interrupt.

    false - If both pTransmitData and pReceiveData are NULL, or if both txSize
    and rxSize are 0 or if txSize is non-zero but the pTransmitData is set to
    NULL or rxSize is non-zero but pReceiveData is NULL. In Interrupt mode, the
    function returns false if there is an on-going data transfer at the time of
    calling the function.

  Example:
    <code>

    // The following code snippet shows an example using the
    // SERCOMx_SPI_WriteRead() function in interrupt mode operation using the
    // callback function.

    uint8_t     txBuffer[4];
    uint8_t     rxBuffer[10];
    size_t      txSize = 4; 
    size_t      rxSize = 10;
    bool        reqAccepted;
    
    void APP_SPITransferHandler(uintptr_t context)
    {
        if(SERCOM1_SPI_ErrorGet() == SPI_ERROR_NONE)
        {
            //Transfer was completed without error, do something else now.
        }
    }

    SERCOM1_SPI_Initialize();
    SERCOM1_SPI_CallbackRegister(&APP_SPITransferHandler, NULL);
    reqAccepted = SERCOM1_SPI_WriteRead(&txBuffer, txSize, &rxBuffer, rxSize);

    // The following code snippet shows non-interrupt or blocking mode
    // operation.

    uint8_t txBuffer[4];
    uint8_t rxBuffer[10];
    size_t txSize = 4; 
    size_t rxSize = 10;
    bool reqAccepted;
    
    SERCOM1_SPI_Initialize();

    // This function call will block.
    SERCOM1_SPI_WriteRead(&txBuffer, txSize, &rxBuffer, rxSize);

    </code>

  Remarks:
    None.
*/

bool SERCOMx_SPI_WriteRead( void* pTransmitData, size_t txSize, void* pReceiveData, size_t rxSize);

// *****************************************************************************
/* Function:
    bool SERCOMx_SPI_Write(void* pTransmitData, size_t txSize);

  Summary:
    Writes data to SERCOM x SPI peripheral. 

  Description:
    This function writes "txSize" number of bytes on SERCOM x SPI module. Data
    pointed by pTransmitData is transmitted.
    
    When "Interrupt Mode" option is unchecked in MHC, this function will be
    blocking in nature.  In this mode, the function will not return until all
    the requested data is transferred.  The function returns true after
    transferring all the data.  This indicates that the operation has been
    completed.

    When "Interrupt Mode" option is selected in MHC, the function will be
    non-blocking in nature.  The function returns immediately. The data transfer
    process continues in the peripheral interrupt.  The application specified
    transmit buffer  is owned by the library until the data transfer is
    complete and should not be modified by the application till the transfer is
    complete.  Only one transfer is allowed at any time. The application can use
    a callback function or a polling function to check for completion of the
    transfer. If a callback is required, this should be registered prior to
    calling the SERCOMx_SPI_WriteRead() function. The application can use the
    SERCOMx_SPI_IsBusy() to poll for completion.
        
  Precondition:
    The SERCOMx_SPI_Initialize function must have been called.
    
    Callback has to be registered using SERCOMx_SPI_CallbackRegister API if the
    peripheral instance has been configured in Interrupt mode and
    transfer completion status needs to be communicated back to application via
    callback.

  Parameters:
    pTransmitData - Pointer to the buffer containing the data which has to be
    transmitted.  For 9 bit mode, data should be right aligned in the 16 bit
    memory location. In "Interrupt Mode", this buffer should not be modified
    after calling the function and before the callback function has been called
    or the SERCOMx_SPI_IsBusy() function returns false.

    txSize - Number of bytes to be transmitted. This value is always the byte
    count of the buffer. For 9 bit data length, this should be an even number. 

  Returns:
    true - If configured for Non-interrupt mode, the function has transmitted
    the requested number of bytes. If configured for Interrupt mode, the request
    was accepted successfully and will be processed in the interrupt.

    false - If pTransmitData is NULL. In Interrupt mode, the function will
    additionally return false if there is an on-going data transfer at the time
    of calling the function.

  Example:
    <code>
    uint8_t txBuffer[4];
    size_t txSize = 4; 
    bool reqAccepted;

    void APP_SPITransferHandler(uintptr_t context)
    {
        if(SERCOM1_SPI_ErrorGet() == SPI_ERROR_NONE)
        {
            Transfer was completed without error, do something else now.
        }
    }
   
    SERCOM1_SPI_Initialize();
    SERCOM1_SPI_CallbackRegister(&APP_SPITransferHandler, NULL);
    reqAccepted = SERCOM1_SPI_Write(&txBuffer, txSize);

    </code>

  Remarks:
    None.
    
*/

bool SERCOMx_SPI_Write(void* pTransmitData, size_t txSize);
    
// *****************************************************************************
/* Function:
    bool SERCOMx_SPI_Read(void* pReceiveData, size_t rxSize);

  Summary:
    Reads data on the SERCOM x SPI peripheral. 

  Description:
    This function reads "rxSize" number of bytes on SERCOM x SPI module. The
    received data is stored in the buffer pointed by pReceiveData.
    
    When "Interrupt Mode" option is unchecked in MHC, this function will be
    blocking in nature.  In this mode, the function will not return until all
    the requested data is transferred.  The function returns true after
    receiving "rxSize" number of bytes.  This indicates that the operation has
    been completed.

    When "Interrupt Mode" option is selected in MHC, the function will be
    non-blocking in nature.  The function returns immediately. The data transfer
    process continues in the peripheral interrupt.  The application specified
    receive buffer  is owned by the library until the data transfer is
    complete and should not be modified by the application till the transfer is
    complete.  Only one transfer is allowed at any time. The application can use
    a callback function or a polling function to check for completion of the
    transfer. If a callback is required, this should be registered prior to
    calling the SERCOMx_SPI_WriteRead() function. The application can use the
    SERCOMx_SPI_IsBusy() to poll for completion.
        
  Precondition:
    The SERCOMx_SPI_Initialize function must have been called.
    
    Callback has to be registered using SERCOMx_SPI_CallbackRegister API if the
    peripheral instance has been configured in Interrupt mode and
    transfer completion status needs to be communicated back to application via
    callback.

  Parameters:
    pReceiveData - Pointer to the buffer where the received data will be stored.
    For 9 bit mode, data should be right aligned in the 16 bit memory location.
    In "Interrupt Mode", this buffer should not be modified after calling the
    function and before the callback function has been called or the
    SERCOMx_SPI_IsBusy() function returns false.

    rxSize - Number of bytes to be received. This value is the byte size of the
    buffer. For 9 bit data length, this is an even number.

  Returns:
    true - If configured for Non-interrupt mode, the function has received the
    requested number of bytes. If configured for Interrupt mode, the request was
    accepted successfully and will be processed in the interrupt.

    false - If pReceiveData is NULL. In Interrupt mode, the function will
    additionally return false if there is an on-going data transfer at the time
    of calling the function.

  Example:
    <code>
    uint8_t     rxBuffer[10]; 
    size_t      rxSize = 10;
    bool        reqAccepted;
 
    void APP_SPITransferHandler(uintptr_t context)
    {
        if(SERCOM1_SPI_ErrorGet() == SPI_ERROR_NONE)
        {
            Transfer was completed without error, do something else now.
        }
    }
   
    SERCOM1_SPI_Initialize();
    SERCOM1_SPI_CallbackRegister(&APP_SPITransferHandler, NULL);
    reqAccepted = SERCOM1_SPI_Read(&rxBuffer, rxSize);

    </code>

  Remarks:
    None.
*/

bool SERCOMx_SPI_Read(void* pReceiveData, size_t rxSize);
    
// *****************************************************************************
/* Function:
    bool SERCOMx_SPI_IsBusy (void):
    
  Summary:
    Returns transfer status of SERCOM x SPI.
    
  Description:
    This function ture if the SERCOM x SPI module is busy with a transfer. The
    application can use the function to check if SERCOM x SPI module is busy
    before calling any of the data transfer functions. The library does not
    allow a data transfer operation if another transfer operation is already in
    progress.

    This function can be used as an alternative to the callback function when
    the library is operating interrupt mode. The allow the application to
    implement a synchronous interface to the library.
  
  Precondition:
    The SERCOMx_SPI_Initialize() should have been called once. The module should
    have been configured for interrupt mode operation in MHC.
  
  Parameters:
    None.
  
  Returns:
    true -  Transfer is still in progress
    false - Transfer is completed or no transfer is currently in progress.
    
  Example:
    <code>
        // The following code example demonstrates the use of the
        // SERCOMx_SPI_IsBusy() function. This example shows a blocking while
        // loop. The function can also be called periodically.

        uint8_t dataBuffer[20];

        SERCOM1_SPI_Initialize();
        SERCOM1_SPI_Write(databuffer, 20);

        while (SERCOM1_SPI_IsBusy() == true)
        {
            // Wait here till the transfer is done.
        }
    </code>
    
  Remarks:
    None.
*/

bool SERCOMx_SPI_IsBusy (void):

// *****************************************************************************
/* Function:
    SPI_ERROR SERCOMx_SPI_ErrorGet( void )

   Summary:
    Gets the error for the given SERCOM x SPI peripheral instance.

   Description:
    This function returns the errors associated with the given SERCOM x SPI
    peripheral instance. An error may occur after a transfer has completed. This
    API can be called to verify if any error has occurred while the transfer was
    in progress. The error returned by this API will be cleared when the
    WriteRead or Write or Read function is called.

   Precondition:
    The SERCOMx_SPI_Initialize() function should have been called once. The
    function is only available in Interrupt operation mode.

   Parameters:
    None.
  
   Returns:
    Errors occurred as listed by SPI_ERROR.

  Example:
    <code>
    if (SERCOM1_SPI_ErrorGet() == SPI_ERROR_OVERRUN)
    {
        //Handle overrun error here
    }
    </code>

  Remarks:
    This API is available only for interrupt mode as non-interrupt mode will
    not have any error.
*/

SPI_ERROR SERCOMx_SPI_ErrorGet( void );

// *****************************************************************************
/* SERCOM x SPICallback Function Pointer

  Summary:
    Pointer to a SERCOM x SPI Callback function.

  Description:
    This data type defines the required function signature for the SERCOM x
    SPIcallback function. Application must register a pointer to a callback
    function whose function signature (parameter and return value types) match
    the types specified by this function pointer in order to receive callback
    from the PLIB.

    The parameters and return values are described here and a partial example
    implementation is provided.

  Parameters:
    context - Value identifying the context of the application that registered
    the callback function

  Returns:
    None.

  Example:
    <code>
    SERCOM1_SPI_CallbackRegister(&APP_SPITransferHandler, NULL);
    void APP_SPITransferHandler(uintptr_t context)
    {
        if(SERCOM1_SPI_ErrorGet() == SPI_ERROR_NONE)
        {
            Transfer was completed without error, do something else now.
        }
    }
    </code>

  Remarks:
    The context parameter contains the a handle to the client context, provided
    at the time the callback function was registered using the
    SERCOMx_SPI_CallbackRegister function. This context handle value is passed
    back to the client as the "context" parameter.  It can be any value (such as
    a pointer to the client's data) necessary to identify the client context or
    instance  of the client that made the data transfer request.

    The callback function executes in the PLIB's interrupt context. It is
    recommended of the application to not perform process intensive or blocking
    operations with in this function.
*/

typedef  void (*SERCOMx_SPI_CALLBACK) (uintptr_t context);

// *****************************************************************************
/* Function:
    void SERCOMx_SPI_CallbackRegister
    (
        const SPI_CALLBACK* callback,
        uintptr_t context
    );

  Summary:
    Allows application to register a callback function with PLIB.

  Description:
    This function allows application to register a callback function for the
    PLIB to call back when the requested data transfer operation has completed.
    The callback should be registered before a transfer operation is requested. 
   
  Precondition:
    The SERCOMx_SPI_Initialize function must have been called. This function is
    only available if the library is configured for interrupt operation mode.

  Parameters:
    callback - Pointer to the callback function implemented by the user. Setting
    this to NULL disables the callback feature.

    context - The value of parameter will be passed back to the application
    unchanged, when the callback function is called. It can be used to identify
    any application specific value that identifies the instance of the client
    module (for example, it may be a pointer to the client module's state
    structure).

  Returns:
    None.

  Example:
    <code>
    uint8_t     txBuffer[4];
    uint8_t     rxBuffer[10];
    size_t      txSize = 4; 
    size_t      rxSize = 10;
    bool        reqAccepted;
 
    void APP_SPITransferHandler(uintptr_t context)
    {
        if(SERCOM1_SPI_ErrorGet() == SPI_ERROR_NONE)
        {
            Transfer was completed without error, do something else now.
        }
    }
   
    SERCOM1_SPI_Initialize();
    SERCOM1_SPI_CallbackRegister(&APP_SPITransferHandler, NULL);
    reqAccepted = SERCOM1_SPI_WriteRead(&txBuffer, txSize, &rxBuffer, rxSize);

    </code>

  Remarks:
    None.
*/

void SERCOMx_SPI_CallbackRegister(const SPI_CALLBACK* callback, uintptr_t context);

#ifdef __cplusplus // Provide C++ Compatibility
}
#endif

#endif /* PLIB_SERCOMx_SPI_H */
