/*******************************************************************************
  FLEXCOM SPI PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_flexcom_spi.h

  Summary:
    FLEXCOM SPI PLIB Header File for documentation

  Description:
    This library provides documentation of all the interfaces which can be used
    to control and interact with an instance of a FLEXCOM SPI controller.
    This file must not be included in any MPLAB Project.

  Remarks:
    This header is for documentation only.  The actual plib_flexcom<x>_spi headers 
    will be generated as required by the MHC (where <x> is the peripheral 
    instance number).

    Every interface symbol has a lower-case 'x' in it following the "FLEXCOM" 
    abbreviation.  This 'x' will be replaced by the peripheral instance number
    in the generated headers.  These are the actual functions that should be
    used.
*******************************************************************************/

/*******************************************************************************
Copyright (c) 2018 released Microchip Technology Inc.  All rights reserved.

Microchip licenses to you the right to use, modify, copy and distribute
Software only when embedded on a Microchip microcontroller or digital signal
controller that is integrated into your product or third party product
(pursuant to the sublicense terms in the accompanying license agreement).

You should refer to the license agreement accompanying this Software for
additional information regarding your rights and obligations.

SOFTWARE AND DOCUMENTATION ARE PROVIDED AS IS  WITHOUT  WARRANTY  OF  ANY  KIND,
EITHER EXPRESS  OR  IMPLIED,  INCLUDING  WITHOUT  LIMITATION,  ANY  WARRANTY  OF
MERCHANTABILITY, TITLE, NON-INFRINGEMENT AND FITNESS FOR A  PARTICULAR  PURPOSE.
IN NO EVENT SHALL MICROCHIP OR  ITS  LICENSORS  BE  LIABLE  OR  OBLIGATED  UNDER
CONTRACT, NEGLIGENCE, STRICT LIABILITY, CONTRIBUTION,  BREACH  OF  WARRANTY,  OR
OTHER LEGAL  EQUITABLE  THEORY  ANY  DIRECT  OR  INDIRECT  DAMAGES  OR  EXPENSES
INCLUDING BUT NOT LIMITED TO ANY  INCIDENTAL,  SPECIAL,  INDIRECT,  PUNITIVE  OR
CONSEQUENTIAL DAMAGES, LOST  PROFITS  OR  LOST  DATA,  COST  OF  PROCUREMENT  OF
SUBSTITUTE  GOODS,  TECHNOLOGY,  SERVICES,  OR  ANY  CLAIMS  BY  THIRD   PARTIES
(INCLUDING BUT NOT LIMITED TO ANY DEFENSE  THEREOF),  OR  OTHER  SIMILAR  COSTS.
*******************************************************************************/

#ifndef PLIB_FLEXCOMx_SPI_H  // Guards against multiple inclusion
#define PLIB_FLEXCOMx_SPI_H

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
/* FLEXCOM SPI Clock Phase

   Summary:
    Identifies FLEXCOM SPI Clock Phase Options

   Description:
    This enumeration identifies possible FLEXCOM SPI Clock Phase Options.

   Remarks:
    None.
*/
typedef enum
{
    /* Input data is valid on clock trailing edge and
    output data is ready on leading edge */
    FLEXCOM_SPI_CLOCK_PHASE_TRAILING_EDGE = 0 << FLEX_SPI_CSR_NCPHA_Pos,
    
    /* Input data is valid on clock leading edge and
    output data is ready on trailing edge */
    FLEXCOM_SPI_CLOCK_PHASE_LEADING_EDGE = 1 << FLEX_SPI_CSR_NCPHA_Pos,

    /* Force the compiler to reserve 32-bit space for each enum value */
    FLEXCOM_SPI_CLOCK_PHASE_INVALID = 0xFFFFFFFF
    
}FLEXCOM_SPI_CLOCK_PHASE;

// *****************************************************************************
/* FLEXCOM SPI Clock Polarity

   Summary:
    Identifies FLEXCOM SPI Clock Polarity Options

   Description:
    This enumeration identifies possible FLEXCOM SPI Clock Polarity Options.

   Remarks:
    None.
*/
typedef enum
{
    /* The inactive state value of clock is logic level zero */
    FLEXCOM_SPI_CLOCK_POLARITY_IDLE_LOW = 0 << FLEX_SPI_CSR_CPOL_Pos,
    
    /* The inactive state value of clock is logic level one */
    FLEXCOM_SPI_CLOCK_POLARITY_IDLE_HIGH = 1 << FLEX_SPI_CSR_CPOL_Pos,

    /* Force the compiler to reserve 32-bit space for each enum value */
    FLEXCOM_SPI_CLOCK_POLARITY_INVALID = 0xFFFFFFFF
    
}FLEXCOM_SPI_CLOCK_POLARITY;

// *****************************************************************************
/* FLEXCOM SPI Data Bits

   Summary:
    Identifies FLEXCOM SPI bits per transfer

   Description:
    This enumeration identifies number of bits per FLEXCOM SPI transfer.

   Remarks:
    For 9 to 15bit modes, data should be right aligned in the 16 bit
    memory location.
*/
typedef enum
{
    /* 8 bits per transfer */
    FLEXCOM_SPI_DATA_BITS_8 = FLEX_SPI_CSR_BITS_8_BIT_Val << FLEX_SPI_CSR_BITS_Pos,
    /* 9 bits per transfer */
    FLEXCOM_SPI_DATA_BITS_9 = FLEX_SPI_CSR_BITS_9_BIT_Val << FLEX_SPI_CSR_BITS_Pos,
    /* 10 bits per transfer */
    FLEXCOM_SPI_DATA_BITS_10 = FLEX_SPI_CSR_BITS_10_BIT_Val << FLEX_SPI_CSR_BITS_Pos,
    /* 11 bits per transfer */
    FLEXCOM_SPI_DATA_BITS_11 = FLEX_SPI_CSR_BITS_11_BIT_Val << FLEX_SPI_CSR_BITS_Pos,
    /* 12 bits per transfer */
    FLEXCOM_SPI_DATA_BITS_12 = FLEX_SPI_CSR_BITS_12_BIT_Val << FLEX_SPI_CSR_BITS_Pos,
    /* 13 bits per transfer */
    FLEXCOM_SPI_DATA_BITS_13 = FLEX_SPI_CSR_BITS_13_BIT_Val << FLEX_SPI_CSR_BITS_Pos,
    /* 14 bits per transfer */
    FLEXCOM_SPI_DATA_BITS_14 = FLEX_SPI_CSR_BITS_14_BIT_Val << FLEX_SPI_CSR_BITS_Pos,
    /* 15 bits per transfer */
    FLEXCOM_SPI_DATA_BITS_15 = FLEX_SPI_CSR_BITS_15_BIT_Val << FLEX_SPI_CSR_BITS_Pos,
    /* 16 bits per transfer */
    FLEXCOM_SPI_DATA_BITS_16 = FLEX_SPI_CSR_BITS_16_BIT_Val << FLEX_SPI_CSR_BITS_Pos,

    /* Force the compiler to reserve 32-bit space for each enum value */
    FLEXCOM_SPI_DATA_BITS_INVALID = 0xFFFFFFFF

}FLEXCOM_SPI_DATA_BITS;

// *****************************************************************************
/* FLEXCOM SPI Setup Parameters

   Summary
    Identifies the setup parameters which can be changed dynamically.

   Description
    This structure identifies the possible setup parameters for FLEXCOM SPI
    which can be changed dynamically if needed.

   Remarks:
    None.
*/
typedef struct
{   

    /* Baud Rate or clock frequency */
    uint32_t            clockFrequency;
    
    /* Clock Phase */
    FLEXCOM_SPI_CLOCK_PHASE     clockPhase;
    
    /* Clock Polarity */
    FLEXCOM_SPI_CLOCK_POLARITY  clockPolarity;
    
    /* Number of bits per transfer */
    FLEXCOM_SPI_DATA_BITS       dataBits;
    
}FLEXCOM_SPI_TRANSFER_SETUP;

// *****************************************************************************
/* Function:
    void FLEXCOMx_SPI_Initialize (void);
    
  Summary:
    Initializes FLEXCOMx SPI  module of the device
    
  Description:
    This function initializes FLEXCOMx SPI  module of the device with the values
    configured in MHC GUI. Once the peripheral is initialized, transfer
    APIs can be used to transfer the data.
  
  Precondition:
    MHC GUI should be configured with the right values.
  
  Parameters:
    None.
  
  Returns:
    None.
    
  Example:
    <code>
        FLEXCOMx_SPI_Initialize();
    </code>
    
  Remarks:
    This function must be called only once and before any other FLEXCOM SPI function is
    called.                                            
*/
void FLEXCOMx_SPI_Initialize (void);

// *****************************************************************************
/* Function:
    bool FLEXCOMx_SPI_TransferSetup(FLEXCOM_SPI_TRANSFER_SETUP *setup, uint32_t spiSourceClock);
    
  Summary:
    Setup FLEXCOM SPI operational parameters as desired by the client.
    
  Description:
    This function setup FLEXCOMx SPI  with the values needed by the client dynamically.
    User need not call this function if he has configured the setup in GUI and
    there is no dynamic change needed in any of the parameters.
  
  Precondition:
    FLEXCOMx SPI must first be initialized using FLEXCOMx_SPI_Initialize().
  
  Parameters :
    spiSourceClock - Source Clock frequency in Hz on which FLEXCOM SPI module is running.

    *setup - pointer to the data structure of type FLEXCOM_SPI_TRANSFER_SETUP which has the
             list of elements to be setup for a client.
  
  Returns:
    true  - if setup was successful, API returns true.
    false - if spiSourceClock and spi clock frequencies are such that resultant
            SCBR value is out of the possible range, then API returns false.
    
  Example:
    <code> 
        FLEXCOM_SPI_TRANSFER_SETUP setup;
        setup.clockFrequency = 1000000;
        setup.clockPhase = FLEXCOM_SPI_CLOCK_PHASE_TRAILING_EDGE;
        setup.clockPolarity = FLEXCOM_SPI_CLOCK_POLARITY_IDLE_LOW;
        setup.dataBits = FLEXCOM_SPI_DATA_BITS_8;
        
        // Assuming 150 MHz as peripheral Master clock frequency
        if (FLEXCOMx_SPI_TransferSetup (&setup, 150000000) == false)
        {
            // this means setup could not be done, debug the reason.
        }
        
    </code>
    
  Remarks:
    User need not call this function if he has configured the setup in
    GUI and there is no dynamic change needed in any of the parameters.
*/
bool FLEXCOMx_SPI_TransferSetup (FLEXCOM_SPI_TRANSFER_SETUP *setup, uint32_t spiSourceClock);

// *****************************************************************************
/* Function:
    bool FLEXCOMx_SPI_WriteRead
	(
		void* pTransmitData,
		size_t txSize,
		void* pReceiveData,
		size_t rxSize
	);

  Summary:
    Write and Read data on FLEXCOMx SPI  peripheral 

  Description:
    This function should be used to write "txSize" number of bytes and read
    "rxSize" number of bytes on FLEXCOMx SPI  module. Data pointed by pTransmitData
    is transmitted and received data is saved in the location pointed by
    pReceiveData.
    
    The function will work differently as per the configuration done in
    MHC as described below:
    
    1.  Blocking Configuration (Non-Interrupt mode): When "Interrupt Mode"
        option is unchecked in GUI, the generated code for that particular
        FLEXCOM SPI PLIB instance will be blocking. In this particular mode, the
        WriteRead API will not return until all the requested data is transferred.
                
        After transferring all the data, boolean status 'True' is returned
        indicating operation completion.

    2.  Non-Blocking Configuration (Interrupt mode): When "Interrupt Mode"
        option is selected in GUI, the generated code for that
        particular FLEXCOM SPI PLIB instance will be Non-blocking in nature. In this
        particular mode, application will give the data transfer
        responsibility to the PLIB and come back and start doing other
        activities, FLEXCOM SPI Data transaction will happen in the corresponding ISR.
        in this mode, the transmit and receive data locations provided by user 
        must remain valid until the data transfer is complete.
        Application can check the data transfer completion status via
        callback or polling mechanism. In case of callback, it needs to be
        registered prior to calling the WriteRead API. Data transfer status
        polling can be done using "FLEXCOMx_SPI_IsBusy" API.
        
  Precondition:
    The FLEXCOMx_SPI_Initialize function must have been called.
    
    Callback has to be registered using FLEXCOMx_SPI_CallbackRegister API if the
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
    
    FLEXCOMx_SPI_Initialize();
    
    FLEXCOMx_SPI_CallbackRegister(&APP_SPITransferHandler, NULL);

    reqAccepted = FLEXCOMx_SPI_WriteRead(&txBuffer, txSize, &rxBuffer, rxSize);

    void APP_SPITransferHandler(uintptr_t context)
    {
        if(FLEXCOMx_SPI_ErrorGet() == FLEXCOM_SPI_ERROR_NONE)
        {
            Transfer was completed without error, do something else now.
        }
    }
    </code>

  Remarks:
    Non-blocking interrupt mode configuration implementation of this function
    will be used by Harmony driver implementation APIs.
    
*/
bool FLEXCOMx_SPI_WriteRead(
	void* pTransmitData,
	size_t txSize,
	void* pReceiveData,
	size_t rxSize);

// *****************************************************************************
/* Function:
    bool FLEXCOMx_SPI_Write(void* pTransmitData, size_t txSize);

  Summary:
    Write data on FLEXCOMx SPI  peripheral 

  Description:
    This function should be used to write "txSize" number of bytes on
    FLEXCOMx SPI  module. Data pointed by pTransmitData is transmitted.
    
    The function will work differently as per the configuration done in
    MHC as described below:
    
    1.  Blocking Configuration (Non-Interrupt mode): When "Interrupt Mode"
        option is unchecked in GUI, the generated code for that particular
        FLEXCOM SPI PLIB instance will be blocking. In this particular mode, the
        Write API will not return until all the requested data is transferred.
                
        After transferring all the data, boolean status 'True' is returned
        indicating operation completion.

    2.  Non-Blocking Configuration (Interrupt mode): When "Interrupt Mode"
        option is selected in GUI, the generated code for that
        particular FLEXCOM SPI PLIB instance will be Non-blocking in nature. In this
        particular mode, application will give the data transfer
        responsibility to the PLIB and come back and start doing other
        activities, FLEXCOM SPI Data transaction will happen in the corresponding ISR.
        in this mode, the transmit data locations provided by user 
        must remain valid until the data transfer is complete.
        Application can check the data transfer completion status via
        callback or polling mechanism. In case of callback, it needs to be
        registered prior to calling the Write API. Data transfer status
        polling can be done using "FLEXCOMx_SPI_IsBusy" API.
        
  Precondition:
    The FLEXCOMx_SPI_Initialize function must have been called.
    
    Callback has to be registered using FLEXCOMx_SPI_CallbackRegister API if the
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
    
    FLEXCOMx_SPI_Initialize();
    
    FLEXCOMx_SPI_CallbackRegister(&APP_SPITransferHandler, NULL);

    reqAccepted = FLEXCOMx_SPI_Write(&txBuffer, txSize);

    void APP_SPITransferHandler(uintptr_t context)
    {
        if(FLEXCOMx_SPI_ErrorGet() == FLEXCOM_SPI_ERROR_NONE)
        {
            Transfer was completed without error, do something else now.
        }
    }
    </code>

  Remarks:
    Non-blocking interrupt mode configuration implementation of this function
    will be used by Harmony driver implementation APIs.
    
*/
bool FLEXCOMx_SPI_Write(void* pTransmitData, size_t txSize);
    
// *****************************************************************************
/* Function:
    bool FLEXCOMx_SPI_Read(void* pReceiveData, size_t rxSize);

  Summary:
    Read data on FLEXCOMx SPI  peripheral 

  Description:
    This function should be used to read "rxSize" number of bytes on
    FLEXCOMx SPI  module. Received data is saved in the location pointed by pReceiveData.
    
    The function will work differently as per the configuration done in
    MHC as described below:
    
    1.  Blocking Configuration (Non-Interrupt mode): When "Interrupt Mode"
        option is unchecked in GUI, the generated code for that particular
        FLEXCOM SPI PLIB instance will be blocking. In this particular mode, the
        Read API will not return until all the requested data is transferred.
                
        After transferring all the data, boolean status 'True' is returned
        indicating operation completion.

    2.  Non-Blocking Configuration (Interrupt mode): When "Interrupt Mode"
        option is selected in GUI, the generated code for that
        particular FLEXCOM SPI PLIB instance will be Non-blocking in nature. In this
        particular mode, application will give the data transfer
        responsibility to the PLIB and come back and start doing other
        activities, FLEXCOM SPI Data transaction will happen in the corresponding ISR.
        in this mode, the receive data locations provided by user 
        must remain valid until the data transfer is complete.
        Application can check the data transfer completion status via
        callback or polling mechanism. In case of callback, it needs to be
        registered prior to calling the Read API. Data transfer status
        polling can be done using "FLEXCOMx_SPI_IsBusy" API.
        
  Precondition:
    The FLEXCOMx_SPI_Initialize function must have been called.
    
    Callback has to be registered using FLEXCOMx_SPI_CallbackRegister API if the
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
    
    FLEXCOMx_SPI_Initialize();
    
    FLEXCOMx_SPI_CallbackRegister(&APP_SPITransferHandler, NULL);

    reqAccepted = FLEXCOMx_SPI_Read(&rxBuffer, rxSize);

    void APP_SPITransferHandler(uintptr_t context)
    {
        if(FLEXCOMx_SPI_ErrorGet() == FLEXCOM_SPI_ERROR_NONE)
        {
            Transfer was completed without error, do something else now.
        }
    }
    </code>

  Remarks:
    Non-blocking interrupt mode configuration implementation of this function
    will be used by Harmony driver implementation APIs.
    
*/
bool FLEXCOMx_SPI_Read(void* pReceiveData, size_t rxSize);
    
// *****************************************************************************
/* Function:
    bool FLEXCOMx_SPI_IsBusy (void):
    
  Summary:
    Returns transfer status of FLEXCOMx SPI 
    
  Description:
    This function returns transfer status of last successful Write, Read or
    WriteRead request on FLEXCOMx SPI  module in interrupt mode.
  
  Precondition:
    None.
  
  Parameters:
    None.
  
  Returns:
    Returns the current status of transfer happening on FLEXCOMx SPI .
        true:  Transfer is still in progress
        false: Transfer is completed
    
  Example:
    <code>
        if (FLEXCOMx_SPI_IsBusy() == false)
        {
            //Data Transfer is complete, do something else.
        }
    </code>
    
  Remarks:
    This API is available only for interrupt mode as blocking mode transfer
    APIs will always return only after completing the transfer.
*/
bool FLEXCOMx_SPI_IsBusy (void):

// *****************************************************************************
/* FLEXCOM SPI Callback Function Pointer

   Summary:
    Pointer to a FLEXCOM SPI Callback function.

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
    FLEXCOMx_SPI_CallbackRegister(&APP_SPITransferHandler, NULL);
    void APP_SPITransferHandler(uintptr_t context)
    {
        if(FLEXCOMx_SPI_ErrorGet() == FLEXCOM_SPI_ERROR_NONE)
        {
            Transfer was completed without error, do something else now.
        }
    }
    </code>

  Remarks:
    The context parameter contains the a handle to the client context,
    provided at the time the callback function was registered using the
    FLEXCOMx_SPI_CallbackRegister function. This context handle value is
    passed back to the client as the "context" parameter.  It can be any value
    (such as a pointer to the client's data) necessary to identify the client
    context or instance  of the client that made the data transfer
    request.

    The callback function executes in the PLIB's interrupt context. It is
    recommended of the application to not perform process intensive or blocking
    operations with in this function.
*/
typedef  void (*FLEXCOM_SPI_CALLBACK) (uintptr_t context);

// *****************************************************************************
/* Function:
    void FLEXCOMx_SPI_CallbackRegister(FLEXCOM_SPI_CALLBACK callback, uintptr_t context);

  Summary:
    Allows application to register callback with PLIB.

  Description:
    This function allows application to register a callback function for the PLIB
    to call back when requested data transfer operation has completed or any error
    has occurred.

    The callback should be registered before the client performs transfer operation. 
    
    At any point if application wants to stop the callback, it can call this function
    with "callback" value as NULL.

  Precondition:
    The FLEXCOMx_SPI_Initialize function must have been called.

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
    
    FLEXCOMx_SPI_Initialize();
    
    FLEXCOMx_SPI_CallbackRegister(&APP_SPITransferHandler, NULL);

    reqAccepted = FLEXCOMx_SPI_WriteRead(&txBuffer, txSize, &rxBuffer, rxSize);

    void APP_SPITransferHandler(uintptr_t context)
    {
        if(FLEXCOMx_SPI_ErrorGet() == FLEXCOM_SPI_ERROR_NONE)
        {
            Transfer was completed without error, do something else now.
        }
    }
    </code>

  Remarks:
    If the client does not want to be notified when the queued operation
    has completed, it does not need to register a callback.
*/
void FLEXCOMx_SPI_CallbackRegister(FLEXCOM_SPI_CALLBACK callback, uintptr_t context);

#ifdef __cplusplus // Provide C++ Compatibility
}
#endif

#endif /* PLIB_FLEXCOMx_SPI_H */

/*******************************************************************************
 End of File
*/