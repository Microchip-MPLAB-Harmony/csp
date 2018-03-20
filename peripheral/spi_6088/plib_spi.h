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
    DATA_VALID_ON_CLOCK_TRAILING_EDGE,
    
    /* Input data is valid on clock leading edge and
    output data is ready on trailing edge */
    DATA_VALID_ON_CLOCK_LEADING_EDGE
    
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
    
}SPI_SETUP;

// *****************************************************************************
/* SPI Errors

   Summary:
    Identifies SPI Errors.

   Description:
    This enumeration identifies the possible SPI Errors.

   Remarks:
    None.
*/
typedef enum 
{
    /* No Error */
    SPI_ERROR_NONE,
    
    /* Overrun Error */
    SPI_ERROR_OVERRUN
    
}SPI_ERROR;

// *****************************************************************************
/* Function:
    void SPIx_Initialize (void);
    
  Summary:
    Initializes SPI x module of the device
    
  Description:
    This function initializes SPI x module of the device with the values
    configured in MCC GUI. Once the peripheral is initialized, exchange
    APIs can be used to exchange the data.
  
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
    bool SPIx_Setup(uint32_t spiSourceClock, SPI_SETUP *setup);
    
  Summary:
    Setup SPI operational parameters as desired by the client.
    
  Description:
    This function setup SPI x with the values needed by the client dynamically.
    User need not call this function if he has configured the setup in GUI and
    there is no dynamic change needed in any of the parameters.
  
  Precondition:
    SPI x must first be initialized using SPIx_Initialize().
  
  Parameters :
    spiSourceClock  Source Clock frequency in Hz on which SPI module is running.
                    If 0 is passed, then clock frequency set in MHC clock manager
                    will be taken by default.
    *setup   pointer to the data structure of type SPI_SETUP which has the
             list of elements to be setup for a client.
  
  Returns:
    true:   if setup was succesfull, API returns true.
    false:  if spiSourceClock and spi clock frequencies are such that resultant
            SCBR value is out of the possible range, then API returns false.
    
  Example:
    <code> 
        SPI_SETUP setup;
        setup.clockFrequency = 1000000;
        setup.clockPhase = DATA_VALID_ON_CLOCK_TRAILING_EDGE;
        setup.clockPolarity = SPI_CLOCK_POLARITY_IDLE_LOW;
        setup.dataBits = SPI_DATA_BITS_8;
        
        // Assuming 150 MHz as peripheral Master clock frequency
        if (false == SPI1_Setup (150000000, &setup))
        {
            // this means setup could not be done, debug the reason.
        }
        
    </code>
    
  Remarks:
    User need not call this function if he has configured the setup in
    GUI and there is no dynamic change needed in any of the parameters.
*/
bool SPIx_Setup (uint32_t spiSourceClock, SPI_SETUP *setup);

// *****************************************************************************
/* Function:
    bool SPIx_Exchange(
        void* pTransmitData,
        void* pReceiveData, 
        size_t size
    );

  Summary:
    Exchange data on SPI x peripheral 

  Description:
    This function should be used to exchange "size" number of bytes on
    SPI x module. Data pointed by pTransmitData is transmitted and received
    data is saved in the location pointed by pReceiveData. if pTransmitData
    is NULL, that means only reading is intended and if pReceiveData is NULL,
    that means only writing is intended. If pTransmitData and pReceiveData
    points to same location, then also this API works well and received data
    is saved in location pointed by pReceiveData (or pTransmitData)
    overwriting the data which was transmitted.
    
    The function will work differently as per the configuration done in
    MCC as described below:
    
    1.  Blocking Configuration (Non-Interrupt mode): When "Interrupt Mode"
        option is unchecked in GUI, the generated code for that particular
        SPI PLIB instance will be blocking. In this particular mode, the
        Exchange API will not return until all the requested data is exchanged.
                
        After exchanging all the data, boolean status 'True' is returned
        indicating operation completion.

    2.  Non-Blocking Configuration (Interrupt mode): When "Interrupt Mode"
        option is selected in GUI, the generated code for that
        particular SPI PLIb instance will be Non-blocking in nature. In this
        particular mode, application will give the data exchanging
        responsiblity to the PLIB and come back and start doing other
        activities, SPI Data transaction will happen in the corresponding ISR.
        in this mode, the transmit and receive data buffers provided by user 
        must remain valid until the data exchange is complete.
        Application can check the data exchange completion status via
        callback or polling mechanism. In case of callback, it needs to be
        registered prior to calling the Exchange API. Data exchange status
        polling can be done using "SPIx_IsBusy" API.
        
  Precondition:
    The SPIx_Initialize function must have been called.
    
    Callback has to be registered using SPIx_CallbackRegister API if the
    peripheral instance has been configured in Interrupt mode and
    buffer completion status needs to be communicated back to application via
    callback.

  Parameters:
    *pTransmitData  Pointer to the data which has to be transmitted. if it is
                    NULL, that means only data receiving is expected. For 9
                    to 15bit mode, data should be right aligned in the 16 bit
                    memory location.
    *pReceiveData   Pointer to the location where received data has to be stored.
                    It is user's responsibility to ensure pointed location has
                    sufficient memory to store the read data.
                    if it is NULL, that means only data transmission is expected.
                    For 9 to 15bit mode, received data will be right aligned in
                    the 16 bit memory location.
    size            Number of bytes to be exchanged. For 9 to 15bit mode, size
                    should be given as if it is 16bit mode.

  Returns:
    In Blocking mode, API returns True once the exchange is complete. It returns
    False if size parameter is 0.
    
    In interrupt mode, API returns true if the exchange request is accepted and
    False otherwise. If previous buffer request is not completed and a new
    exchange request comes, then this API will reject the new request and will
    return "False". Same as blocking mode, It returns False if size parameter is 0.

  Example:
    <code>
    uint8_t     txBuffer[10];
    uint8_t     rxBuffer[10];
    size_t      size = 10;    
    bool        reqAccepted;
    
    SPI1_Initialize();
    
    // Interrupt mode
    SPI1_CallbackRegister(&APP_SPITransferHandler, NULL);

    reqAccepted = SPI1_Exchange(&txBuffer, &rxBuffer, size);

    void APP_SPITransferHandler(void* contextHandle)
    {
        // Exchange is completed, user can check if any error occurred.
    }
    </code>

  Remarks:
    Non-blocking interrupt mode configuration implementation of this function
    will be used by Harmony driver implementation of DRV_SPI_BufferRead/Write
    APIs.
    
*/
bool SPIx_Exchange(
    void* pTransmitData,
    void* pReceiveData, 
    size_t size
);

// *****************************************************************************
/* Function:
    bool SPIx_IsBusy (void):
    
  Summary:
    Returns exchange status of particular request on SPI x
    
  Description:
    This function returns exchange status of particular request on SPI x module
    in interrupt mode.
  
  Precondition:
    None.
  
  Parameters:
    None.
  
  Returns:
    Returns the current status of exchange happening on SPI x.
        true: Exchange is completed
        false: Exchange is still in progress
    
  Example:
    <code>
        if (false == SPI1_IsBusy())
        {
            //Data Exchange is complete, do something else.
        }
    </code>
    
  Remarks:
    None.
*/
bool SPIx_IsBusy (void):

// *****************************************************************************
/* Function:
    SPI_ERROR SPIx_ErrorGet( void )

   Summary:
    Gets the error of the given SPI peripheral instance.

   Description:
    This function returns the errors associated with the given SPI peripheral 
    instance. After completing any echange, this API should be called and
    verified if any error occurred in the exchange or not.

   Precondition:
    None.

   Parameters:
    None.
  
   Returns:
    Errors occurred as listed by SPI_ERROR.

  Example:
    <code>
    if (SPI_ERROR_OVERRUN == SPI1_ErrorGet())
    {
        //Handle overrun error here
    }
    </code>

  Remarks:
    This API is available only for interrupt mode as blocking mode will
    not have any error.
*/

SPI_ERROR SPIx_ErrorGet( void );

// *****************************************************************************
/* SPI Event Handler Function Pointer

   Summary:
    Pointer to a SPI Event handler function.

   Description:
    This data type defines the required function signature for the 
    SPI event handling callback function. Application must register
    a pointer to an event handling function whose function signature (parameter
    and return value types) match the types specified by this function pointer
    in order to receive event calls back from the PLIB.

    The parameters and return values are described here and a partial example
    implementation is provided.

  Parameters:
    context         - Value identifying the context of the application that
                      registered the event handling function

  Returns:
    None.

  Example:
    <code>
    SPI1_CallbackRegister(&APP_SPITransferHandler, NULL);
    void APP_SPITransferHandler(uintptr_t contextHandle)
    {
        if( SPI_ERROR_NONE == SPI1_ErrorGet())
        {
            Exchange was completed without error, do something else now.
        }
    }
    </code>

  Remarks:
    The context parameter contains the a handle to the client context,
    provided at the time the event handling function was  registered using the
    SPIx_CallbackRegister function. This context handle value is
    passed back to the client as the "context" parameter.  It can be any value
    (such as a pointer to the client's data) necessary to identify the client
    context or instance  of the client that made the data exchange
    request.

    The event handler function executes in the PLIB's interrupt context. It is
    recommended of the application to not perform process intensive or blocking
    operations with in this function.
*/
typedef  void (*SPI_EVENT_HANDLER) (void* context);

// *****************************************************************************
/* Function:
    void SPIx_CallbackRegister
    (
        const SPI_EVENT_HANDLER* eventHandler,
        void* context
    );

  Summary:
    Allows application to register callback with PLIB.

  Description:
    This function allows application to register an event handling function
    for the PLIB to call back when requested data exchange operation has completed or
    any error has occurred.

    The callback should be registered before the client performs exchange operation. 
    
    At any point if application wants to stop the callback, it can call this function
    with "eventHandler" value as NULL.

  Precondition:
    The SPIx_Initialize function must have been called.

  Parameters:
    eventHandler - Pointer to the event handler function implemented by the user

    context      - The value of parameter will be passed back to the application
                   unchanged, when the eventHandler function is called. It can
                   be used to identify any application specific value that
                   identifies the instance of the client module (for example,
                   it may be a pointer to the client module's state structure).

  Returns:
    None.

  Example:
    <code>
    uint8_t     txBuffer[10];
    uint8_t     rxBuffer[10];
    size_t      size = 10;    
    size_t      reqAccepted;
    
    SPI1_Initialize();
    
    SPI1_CallbackRegister(&APP_SPITransferHandler, NULL);

    reqAccepted = SPI1_Exchange(&txBuffer, &rxBuffer, size);

    void APP_SPITransferHandler(void* contextHandle)
    {
        if( SPI_ERROR_NONE == SPI1_ErrorGet())
        {
            Exchange was completed without error, do something else now.
        }
    }
    </code>

  Remarks:
    If the client does not want to be notified when the queued operation
    has completed, it does not need to register a callback.
*/
void SPIx_CallbackRegister(const SPI_EVENT_HANDLER* eventHandler, void* context);