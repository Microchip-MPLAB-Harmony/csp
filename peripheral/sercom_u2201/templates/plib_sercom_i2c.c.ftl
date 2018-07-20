/*******************************************************************************
  Serial Communication Interface Inter-Integrated Circuit (SERCOM I2C) Library
  Source File

  Company:
    Microchip Technology Inc.

  File Name:
    plibSERCOM${SERCOM_INDEX}_i2c.c

  Summary:
    SERCOM I2C PLIB Implementation file

  Description:
    This file defines the interface to the SERCOM I2C peripheral library.
    This library provides access to and control of the associated peripheral
    instance.

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
// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
/* This section lists the other files that are included in this file.
*/

#include "plib_sercom${SERCOM_INDEX}_i2c.h"
#include "device.h"

// *****************************************************************************
// *****************************************************************************
// Section: Local Data Type Definitions
// *****************************************************************************
// *****************************************************************************

#define I2C_MASTER_MODE                 (5U)

#define SDA_HOLD_TIME                   (${SDAHOLD_TIME}U)

#define INITIAL_BUS_STATE               (1U)

#define BAUD_REFERENCE_FREQUENCY        (4000000U)

#define SERCOM_I2C_SPEED                (${I2C_SPEED} * 1000U)

#define PHCTRL_INDEX                    (${SERCOM_PHCTRL_INDEX}U)

#define RIGHT_ALIGNED                   (8U)

#define TEN_BIT_ADDR_MASK               (0x78U)

#define NUM_TRBS                        (${I2CM_NUM_TRBS}U)

#define BAUD_REGISTER_VALUE             ( (BAUD_REFERENCE_FREQUENCY / ( 2 * SERCOM_I2C_SPEED) ) - 1)

// *****************************************************************************
/* Pointer to the sercom base address

  Summary:
    Pointer to the sercom${SERCOM_INDEX} base address.

  Description:
    Macro for the pointer to the sercom${SERCOM_INDEX} base address.

  Remarks:
    None.
*/

#define SERCOM${SERCOM_INDEX}_I2C SERCOM${SERCOM_INDEX}_REGS

// *****************************************************************************
// *****************************************************************************
// Section: MACRO Definitions
// *****************************************************************************
// *****************************************************************************

static SERCOM_I2C_OBJ sercom${SERCOM_INDEX}I2CObj;

static SERCOM_I2C_TRB sercom${SERCOM_INDEX}I2CTRBsList[NUM_TRBS];

// *****************************************************************************
// *****************************************************************************
// Section: Local Function Definition
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Function:
    void SERCOM_I2C_Start(SERCOM_I2C_TRB *trb)

   Summary:
    Send the 7-bit or 10-bit slave address.

   Description:
    This function send the 7-bit or 10-bit slave address with the direction
    (read/write). For first TRB sending the address will consider as the start
    of a transaction but for the next TRBs it will consider as the repeat start.

   Parameters:
    Transaction Request Block(TRB)

   Returns:
    None.

   Remarks:
    None.
*/

void SERCOM_I2C_Start(SERCOM_I2C_TRB *trb)
{
    /* Reset TRB Length */
    trb->length += sercom${SERCOM_INDEX}I2CObj.processedTRBDataLength;

    /* Reset processed TRB data length */
    sercom${SERCOM_INDEX}I2CObj.processedTRBDataLength = 0;

    /* Check for 10-bit address */
    if(trb->address > 0x007F)
    {
        if(trb->read)
        {
            sercom${SERCOM_INDEX}I2CObj.state = SERCOM_I2C_STATE_ADDR_SEND;
        }
        else
        {
            sercom${SERCOM_INDEX}I2CObj.state = SERCOM_I2C_STATE_TRANSFER_WRITE;
        }

        /*
         * Write ADDR.ADDR[10:1] with the 10-bit address.
         * Set direction bit (ADDR.ADDR[0]) equal to 0.
         * Set ADDR.TENBITEN equals to 1.
         */
        SERCOM${SERCOM_INDEX}_I2C->I2CM.ADDR.w = (trb->address << 1) | I2C_TRANSFER_WRITE | SERCOM_I2CM_ADDR_TENBITEN_Msk;
    }
    else
    {
        if(trb->read)
        {
            sercom${SERCOM_INDEX}I2CObj.state = SERCOM_I2C_STATE_TRANSFER_READ;

            /* Write 7bit address with direction (ADDR.ADDR[0]) equal to 1*/
            SERCOM${SERCOM_INDEX}_I2C->I2CM.ADDR.w = (trb->address << 1) | I2C_TRANSFER_READ;
        }
        else
        {
            sercom${SERCOM_INDEX}I2CObj.state = SERCOM_I2C_STATE_TRANSFER_WRITE;

            /* Write 7bit address with direction (ADDR.ADDR[0]) equal to 0*/
            SERCOM${SERCOM_INDEX}_I2C->I2CM.ADDR.w = (trb->address << 1) | I2C_TRANSFER_WRITE;
        }
    }
}

// *****************************************************************************
// *****************************************************************************
// Section: SERCOM I2C Implementation
// *****************************************************************************
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Function:
    void SERCOM${SERCOM_INDEX}_I2C_Initialize(void)

  Summary:
    Initializes the instance of the SERCOM peripheral operating in I2C mode.

  Description:
    This function initializes the given instance of the SERCOM I2C peripheral as
    configured by the user from the MHC.

  Remarks:
    Refer plibSERCOM${SERCOM_INDEX}_i2c.h for more information.
*/

void SERCOM${SERCOM_INDEX}_I2C_Initialize(void)
{

    /* Software Reset*/
    SERCOM${SERCOM_INDEX}_I2C->I2CM.CTRLA.w |= SERCOM_I2CM_CTRLA_SWRST_Msk;

    while((SERCOM${SERCOM_INDEX}_I2C->I2CM.SYNCBUSY.w & SERCOM_I2CM_SYNCBUSY_SWRST_Msk) == SERCOM_I2CM_SYNCBUSY_SWRST_Msk)
    {
        /* Wait for synchronization after software reset */
    }

    /* Set Operation Mode (Master), SDA Hold time*/
    SERCOM${SERCOM_INDEX}_I2C->I2CM.CTRLA.w |= SERCOM_I2CM_CTRLA_MODE(I2C_MASTER_MODE) | SERCOM_I2CM_CTRLA_SDAHOLD(SDA_HOLD_TIME);

    /* Baud rate - Master Baud Rate*/
    SERCOM${SERCOM_INDEX}_I2C->I2CM.BAUD.w |= SERCOM_I2CM_BAUD_BAUD(BAUD_REGISTER_VALUE);

    /* Set Run in Stand By */
    SERCOM${SERCOM_INDEX}_I2C->I2CM.CTRLA.w |= SERCOM_I2CM_CTRLA_RESETVALUE ${RUN_IN_STANDBY?then('| SERCOM_I2CM_CTRLA_RUNSTDBY_Msk','')};

    /* Enable I2C Master */
    SERCOM${SERCOM_INDEX}_I2C->I2CM.CTRLA.w |= SERCOM_I2CM_CTRLA_ENABLE_Msk;

    /* Synchronization */
    while((SERCOM${SERCOM_INDEX}_I2C->I2CM.SYNCBUSY.w & SERCOM_I2CM_SYNCBUSY_ENABLE_Msk) == SERCOM_I2CM_SYNCBUSY_ENABLE_Msk)
    {
        /* Wait for synchronization after enabling I2C */
    }

    /* Initial Bus State: IDLE */
    SERCOM${SERCOM_INDEX}_I2C->I2CM.STATUS.w |= SERCOM_I2CM_STATUS_BUSSTATE(INITIAL_BUS_STATE);

    while((SERCOM${SERCOM_INDEX}_I2C->I2CM.SYNCBUSY.w & SERCOM_I2CM_SYNCBUSY_SYSOP_Msk) == SERCOM_I2CM_SYNCBUSY_SYSOP_Msk)
    {
        /* Wait for System Operation Synchronization */
    }

    /* Disable all interrupts*/
    <@compress single_line=true>SERCOM${SERCOM_INDEX}_I2C->I2CM.INTENCLR.w |= SERCOM_I2CM_INTENCLR_MB_Msk | SERCOM_I2CM_INTENCLR_SB_Msk | SERCOM_I2CM_INTENCLR_ERROR_Msk;</@compress>

    /* Reset the PLib objects */
    sercom${SERCOM_INDEX}I2CObj.numTRBs = 0;
    sercom${SERCOM_INDEX}I2CObj.currentTRB = 0;
    sercom${SERCOM_INDEX}I2CObj.state = SERCOM_I2C_STATE_IDLE;
    sercom${SERCOM_INDEX}I2CObj.status = SERCOM_I2C_TRANSFER_STATUS_SUCCESS;
    sercom${SERCOM_INDEX}I2CObj.error = SERCOM_I2C_ERROR_NONE;
    sercom${SERCOM_INDEX}I2CObj.processedTRBDataLength = 0;
}

// *****************************************************************************
/* Function:
    void SERCOM${SERCOM_INDEX}_I2C_CallbackRegister(SERCOM_I2C_CALLBACK callback,
                                                    uintptr_t context)

   Summary:
    Sets the pointer to the function (and it's context) to be called when the
    given SERCOM I2C's transfer events occur.

  Description:
    This function sets the pointer to a client function to be called "back" when
    the given SERCOM I2C's transfer events occur. It also passes a context value
    (usually a pointer to a context structure) that is passed into the function
    when it is called. The specified callback function will be called from the
    peripheral interrupt context.

  Remarks:
    Refer plibSERCOM${SERCOM_INDEX}_i2c.h for more information.
*/

void SERCOM${SERCOM_INDEX}_I2C_CallbackRegister(SERCOM_I2C_CALLBACK callback, uintptr_t contextHandle)
{
    sercom${SERCOM_INDEX}I2CObj.callback = callback;
    sercom${SERCOM_INDEX}I2CObj.context  = contextHandle;
}

// *****************************************************************************
/* Function:
    bool SERCOM${SERCOM_INDEX}_I2C_TRBBuildRead(uint16_t address,
                                                uint8_t *pdata, uint8_t length)

  Summary:
    Allocates and builds the Read Transaction Request Block (TRB).

  Description:
    This function allocates and builds a Read Transaction Request Block. The
    transaction will be executed when the SERCOM${SERCOM_INDEX}_I2C_TRBTransfer()
    function is called. A transaction is marked complete when either all the
    request bytes have been received or when a bus error or a NAK condition has
    occurred. The application can build multiple Read TRBs.

    The transaction will be executed in the same order in which the build
    function was called. A I2C Repeated Start condition will be placed on the
    bus between each transaction.  The maximum number of TRBs that can be built
    is configurable in MHC. The application should not access the contents of
    the buffer pointed to by pData while a transfer is in progress.

    Calling this function does not initiate any activity on the I2C bus.

  Remarks:
    Refer plibSERCOM${SERCOM_INDEX}_i2c.h for more information.
*/

bool SERCOM${SERCOM_INDEX}_I2C_TRBBuildRead(uint16_t address, uint8_t *pdata, uint8_t length)
{
    bool trbBuildReadStatus = false;
    SERCOM_I2C_TRB * trb = NULL;

    /*
     * Check current TRB index cannot be more than available TRB's and
     * ongoing transfer.
     */
    if((sercom${SERCOM_INDEX}I2CObj.numTRBs <= NUM_TRBS) && (sercom${SERCOM_INDEX}I2CObj.state == SERCOM_I2C_STATE_IDLE))
    {
        trbBuildReadStatus = true;

        trb = &sercom${SERCOM_INDEX}I2CTRBsList[sercom${SERCOM_INDEX}I2CObj.numTRBs];

        /* Fill the TRB */
        trb->address = address;
        trb->read    = true;
        trb->length  = length;
        trb->pbuffer = pdata;

        /* Increment current TRB index */
        sercom${SERCOM_INDEX}I2CObj.numTRBs++;
    }

    return trbBuildReadStatus;
}

// *****************************************************************************
/* Function:
    bool SERCOM${SERCOM_INDEX}_I2C_TRBBuildWrite(uint16_t address,
                                                 uint8_t *pdata, uint8_t length)

  Summary:
    Allocates and Builds the Write Transaction Request Block.

  Description:
    This function allocates and builds a Write Transaction Request Block. The
    transaction will be executed when the SERCOM${SERCOM_INDEX}_I2C_TRBTransfer()
    function is called. A transaction is marked complete when either all the
    request bytes have been received or when a bus error or a NAK condition has
    occurred. The application can build multiple Write TRBs.

    The transaction will be executed in the same order in which the build
    function was called. A I2C Repeated Start condition will be placed on the
    bus between each transaction.  The maximum number of TRBs that can be built
    is configurable in MHC. The application should not access the contents of
    the buffer pointed to by pData while a transfer is in progress.

    Calling this function does not initiate any activity on the I2C bus.

  Remarks:
    Refer plibSERCOM${SERCOM_INDEX}_i2c.h for more information.
*/

bool SERCOM${SERCOM_INDEX}_I2C_TRBBuildWrite(uint16_t address, uint8_t *pdata, uint8_t length)
{
    bool trbBuildWriteStatus = false;
    SERCOM_I2C_TRB * trb = NULL;

    /*
     * Check current TRB index cannot be more than available TRB's and
     * ongoing transfer.
     */
    if((sercom${SERCOM_INDEX}I2CObj.numTRBs <= NUM_TRBS) && (sercom${SERCOM_INDEX}I2CObj.state == SERCOM_I2C_STATE_IDLE))
    {
        trbBuildWriteStatus = true;

        trb = &sercom${SERCOM_INDEX}I2CTRBsList[sercom${SERCOM_INDEX}I2CObj.numTRBs];

        /* Fill the TRB */
        trb->address = address;
        trb->read    = false;
        trb->length  = length;
        trb->pbuffer = pdata;

        /* Increment current TRB index */
        sercom${SERCOM_INDEX}I2CObj.numTRBs++;
    }

    return trbBuildWriteStatus;
}

// *****************************************************************************
/* Function:
    bool SERCOM${SERCOM_INDEX}_I2C_TRBTransfer(void)

  Summary:
    Submits all TRB's that were built for processing.

  Description:
    This function submits all TRB's that were built by calling
    SERCOM${SERCOM_INDEX}_I2C_TRBBuildRead and SERCOM${SERCOM_INDEX}_I2C_TRBBuildWrite.
    Calling the transfer function will start the transfer. A I2C Repeated Start
    condition will be placed on the bus after the completion of each TRB. A I2C
    Stop condition will placed on the bus after processing the the last TRB.

    The function is non-blocking. It will trigger bus activity and will return
    immediately. The TRBs will be processed in the SERCOM interrupt. The
    transfer function cannot be called while another transfer is in progress.
    Doing so will cause the function to return a false return value. The
    application must use the SERCOM${SERCOM_INDEX}_I2C_TransferStatusGet()
    function to get the status of an on-going transfer. Alternatively it can
    register a callback function through the SERCOM${SERCOM_INDEX}_I2C_CallbackRegister()
    function. This callback function will be called when all the TRBs have been
    processed or when an error has occurred.

    The transfer function will process TRBs in the same order in which they were
    built. When a transfer is complete successfully or unsuccessfully, all TRBs
    (including the unprocessed TRBs) will be discarded. In case of an error,
    this may require the TRBs to be re-submitted.

  Remarks:
    Refer plibSERCOM${SERCOM_INDEX}_i2c.h for more information.
*/

bool SERCOM${SERCOM_INDEX}_I2C_TRBTransfer(void)
{
    bool result = false;
    sercom${SERCOM_INDEX}I2CObj.currentTRB = 0;

    /* Minimum one filled TRB must be available and check ongoing transfer*/
    if((sercom${SERCOM_INDEX}I2CObj.numTRBs != 0 ) && (sercom${SERCOM_INDEX}I2CObj.state == SERCOM_I2C_STATE_IDLE))
    {
        result = true;

        /* Clear all flags */
        SERCOM${SERCOM_INDEX}_I2C->I2CM.INTFLAG.w = SERCOM_I2CM_INTFLAG_Msk;

        /* Reset Error Information */
        sercom${SERCOM_INDEX}I2CObj.error = SERCOM_I2C_ERROR_NONE;

        /* Enable all Interrupts */
        <@compress single_line=true>SERCOM${SERCOM_INDEX}_I2C->I2CM.INTENSET.w |= SERCOM_I2CM_INTENSET_MB_Msk | SERCOM_I2CM_INTENSET_SB_Msk | SERCOM_I2CM_INTENSET_ERROR_Msk;</@compress>

        /* Start first TRB by sending the address */
        SERCOM_I2C_Start(&sercom${SERCOM_INDEX}I2CTRBsList[sercom${SERCOM_INDEX}I2CObj.currentTRB]);
    }

    return result;
}

// *****************************************************************************
/* Function:
    bool SERCOM${SERCOM_INDEX}_I2C_Read(uint16_t address, uint8_t *pdata,
                                        uint8_t length)

  Summary:
    Reads data from the slave.

  Description:
    This function reads the data from a slave on the bus. The function will
    attempt to read length number of bytes into pdata buffer from a slave whose
    address is specified as address. The I2C Master generate a Start condition,
    read the data and then generate a Stop Condition. If the Master lost
    arbitration, then the library will attempt to regain the control of the bus.
    If the slave NAKs the request or a bus error is encountered on the bus, the
    transfer is terminated. The application can call the
    SERCOM${SERCOM_INDEX}_I2C_TransferStatusGet() function and the SERCOM${SERCOM_INDEX}_I2C_ErrorGet()
    function to know that cause of the error.

    The function is non-blocking. It initiates bus activity and returns
    immediately. The transfer is completed in the peripheral interrupt. A
    transfer request cannot be placed when another transfer is in progress.
    Calling the read function when another function is already in progress will
    cause the function to return false.

    The library will call the registered callback function when the transfer has
    terminated. Additionally, the SERCOM${SERCOM_INDEX}_I2C_TransferStatusGet()
    function will return SERCOM_I2C_TRANSFER_ERROR or SERCOM_I2C_TRANSFER_SUCCESS
    depending on the completion status of the transfer. If a callback is desired,
    this should have been registered (by calling the
    SERCOM${SERCOM_INDEX}_I2C_CallbackRegister) before calling the read function.

  Remarks:
    Refer plibSERCOM${SERCOM_INDEX}_i2c.h for more information.
*/

bool SERCOM${SERCOM_INDEX}_I2C_Read(uint16_t address, uint8_t *pdata, uint8_t length)
{
    bool readStatus = false;

    /* Build Read TRB and Initiate transfer */
    if (SERCOM${SERCOM_INDEX}_I2C_TRBBuildRead( address, pdata, length) && SERCOM${SERCOM_INDEX}_I2C_TRBTransfer())
    {
        readStatus = true;

    }

    return readStatus;
}

// *****************************************************************************
/* Function:
    bool SERCOM${SERCOM_INDEX}_I2C_Write(uint16_t address, uint8_t *pdata,
                                         uint8_t length)

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
    SERCOM${SERCOM_INDEX}_I2C_TransferStatusGet() function and the SERCOM${SERCOM_INDEX}_I2C_ErrorGet()
    function to know that cause of the error.

    The function is non-blocking. It initiates bus activity and returns
    immediately. The transfer is then completed in the peripheral interrupt. A
    transfer request cannot be placed when another transfer is in progress.
    Calling the write function when another function is already in progress will
    cause the function to return false.

    The library will call the registered callback function when the transfer has
    terminated. Additionally, the SERCOM${SERCOM_INDEX}_I2C_TransferStatusGet()
    function will return SERCOM_I2C_TRANSFER_ERROR or SERCOM_I2C_TRANSFER_SUCCESS
    depending on the completion status of the transfer. If a callback is desired,
    this should should have been register (by calling the
    SERCOM${SERCOM_INDEX}_I2C_CallbackRegister) before calling the write function.

  Remarks:
    Refer plibSERCOM${SERCOM_INDEX}_i2c.h for more information.
*/

bool SERCOM${SERCOM_INDEX}_I2C_Write(uint16_t address, uint8_t *pdata, uint8_t length)
{
    bool writeStatus = false;

    /* Build Write TRB and Initiate transfer */
    if(SERCOM${SERCOM_INDEX}_I2C_TRBBuildWrite( address, pdata, length ) && SERCOM${SERCOM_INDEX}_I2C_TRBTransfer())
    {
        writeStatus = true;
    }

    return writeStatus;
}

// *****************************************************************************
/* Function:
    bool SERCOM${SERCOM_INDEX}_I2C_WriteRead(uint16_t address, uint8_t *wdata,
                               uint8_t wlength, uint8_t *rdata, uint8_t rlength)

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
    the SERCOM${SERCOM_INDEX}_I2C_TransferStatusGet() function and the SERCOM${SERCOM_INDEX}_I2C_ErrorGet()
    function to know that cause of the error.

    The function is non-blocking. It initiates bus activity and returns
    immediately. The transfer is then completed in the peripheral interrupt. A
    transfer request cannot be placed when another transfer is in progress.
    Calling this function when another function is already in progress will
    cause the function to return false.

    The library will call the registered callback function when the transfer has
    terminated. Additionally, the SERCOM${SERCOM_INDEX}_I2C_TransferStatusGet()
    function will return SERCOM_I2C_TRANSFER_ERROR or SERCOM_I2C_TRANSFER_SUCCESS
    depending on the completion status of the transfer. If a callback is desired,
    this should should have been register (by calling the
    SERCOM${SERCOM_INDEX}_I2C_CallbackRegister) before calling the write function.

  Remarks:
    Refer plibSERCOM${SERCOM_INDEX}_i2c.h for more information.
*/

bool SERCOM${SERCOM_INDEX}_I2C_WriteRead(uint16_t address, uint8_t *wdata, uint8_t wlength, uint8_t *rdata, uint8_t rlength)
{
    bool writereadStatus = false;

    /* Build Write TRB and Read TRB */
    if ( SERCOM${SERCOM_INDEX}_I2C_TRBBuildWrite( address, wdata, wlength ) && SERCOM${SERCOM_INDEX}_I2C_TRBBuildRead( address, rdata, rlength ))
    {
        /* Initiate transfer */
        writereadStatus = SERCOM${SERCOM_INDEX}_I2C_TRBTransfer();
    }

    return writereadStatus;
}

// *****************************************************************************
/* Function:
    SERCOM_I2C_TRANSFER_STATUS SERCOM${SERCOM_INDEX}_I2C_TransferStatusGet(void)

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
    SERCOM${SERCOM_INDEX}_I2C_ErrorGet() function to find out the actuall error.

   Remarks:
    Refer plibSERCOM${SERCOM_INDEX}_i2c.h for more information.
*/

SERCOM_I2C_TRANSFER_STATUS SERCOM${SERCOM_INDEX}_I2C_TransferStatusGet(void)
{
    return sercom${SERCOM_INDEX}I2CObj.status;
}

// *****************************************************************************
/* Function:
    SERCOM_I2C_ERROR SERCOM${SERCOM_INDEX}_I2C_ErrorGet(void)

  Summary:
    Returns the latest error that occurred on the bus.

  Description:
    This function returns the latest error that occurred on the bus. The
    function can be called to identify the error cause when the
    SERCOM${SERCOM_INDEX}_I2C_TransferStatusGet() function returns a
    SERCOM_I2C_TRANSFER_ERROR status. The errors are cleared when the next
    transfer function is initiated.

  Remarks:
    Refer plibSERCOM${SERCOM_INDEX}_i2c.h for more information.
*/

SERCOM_I2C_ERROR SERCOM${SERCOM_INDEX}_I2C_ErrorGet(void)
{
    return sercom${SERCOM_INDEX}I2CObj.error;
}

// *****************************************************************************
/* Function:
    void SERCOM${SERCOM_INDEX}_InterruptHandler(void)

   Summary:
    SERCOM${SERCOM_INDEX} I2C Peripheral Interrupt Handler.

   Description:
    This function is SERCOM${SERCOM_INDEX} I2C Peripheral Interrupt Handler and will
    called on every SERCOM${SERCOM_INDEX} I2C interrupt.

   Precondition:
    None.

   Parameters:
    None.

   Returns:
    None.

   Remarks:
    None.
*/

void SERCOM${SERCOM_INDEX}_InterruptHandler(void)
{
    SERCOM_I2C_TRB * trb = NULL;
    bool currentTRBTransferDone = false;

    /* Check if transfer is initiated and atleast one TRB is available */
    if((sercom${SERCOM_INDEX}I2CObj.state != SERCOM_I2C_STATE_IDLE) && (sercom${SERCOM_INDEX}I2CObj.numTRBs != 0))
    {
        /* Get current TRB from TRB List */
        trb = &sercom${SERCOM_INDEX}I2CTRBsList[sercom${SERCOM_INDEX}I2CObj.currentTRB];

        /* Checks if the arbitration lost in multi-master scenario */
        if((SERCOM${SERCOM_INDEX}_I2C->I2CM.STATUS.w & SERCOM_I2CM_STATUS_ARBLOST_Msk) == SERCOM_I2CM_STATUS_ARBLOST_Msk)
        {
            /*
             * Re-initiate the transfer if arbitration is lost
             * in between of the transfer
             */
            sercom${SERCOM_INDEX}I2CObj.status = SERCOM_I2C_TRANSFER_STATUS_BUSY;

            /* Restart the current TRB. */
            SERCOM_I2C_Start(&sercom${SERCOM_INDEX}I2CTRBsList[sercom${SERCOM_INDEX}I2CObj.currentTRB]);
        }
        /* Check for Bus Error during transmission */
        else if((SERCOM${SERCOM_INDEX}_I2C->I2CM.STATUS.w & SERCOM_I2CM_STATUS_BUSERR_Msk) == SERCOM_I2CM_STATUS_BUSERR_Msk)
        {
            /* Set Error status */
            sercom${SERCOM_INDEX}I2CObj.status = SERCOM_I2C_TRANSFER_STATUS_ERROR;
            sercom${SERCOM_INDEX}I2CObj.error = SERCOM_I2C_ERROR_BUS;
        }
        else
        {
            switch(sercom${SERCOM_INDEX}I2CObj.state)
            {
                case SERCOM_I2C_STATE_IDLE:
                {
                }

                case SERCOM_I2C_STATE_ADDR_SEND:
                {
                    /* Checks slave acknowledge for address */
                    if((SERCOM${SERCOM_INDEX}_I2C->I2CM.STATUS.w & SERCOM_I2CM_STATUS_RXNACK_Msk) == SERCOM_I2CM_STATUS_RXNACK_Msk)
                    {
                        sercom${SERCOM_INDEX}I2CObj.status = SERCOM_I2C_TRANSFER_STATUS_ERROR;
                        sercom${SERCOM_INDEX}I2CObj.error = SERCOM_I2C_ERROR_NAK;
                    }
                    else
                    {
                        if(trb->read && ((SERCOM${SERCOM_INDEX}_I2C->I2CM.ADDR.w & SERCOM_I2CM_ADDR_TENBITEN_Msk) == SERCOM_I2CM_ADDR_TENBITEN_Msk))
                        {
                            /*
                            * Write ADDR[7:0] register to "11110 address[9:8] 1"
                            * ADDR.TENBITEN must be cleared
                            */
                            SERCOM${SERCOM_INDEX}_I2C->I2CM.ADDR.w = (((trb->address >> RIGHT_ALIGNED) | TEN_BIT_ADDR_MASK) << 1) | I2C_TRANSFER_READ;

                            sercom${SERCOM_INDEX}I2CObj.state = SERCOM_I2C_STATE_TRANSFER_READ;
                        }
                    }

                    break;
                }

                case SERCOM_I2C_STATE_TRANSFER_WRITE:
                {
                    /* Checks slave acknowledge for data */
                    if((SERCOM${SERCOM_INDEX}_I2C->I2CM.STATUS.w & SERCOM_I2CM_STATUS_RXNACK_Msk) == SERCOM_I2CM_STATUS_RXNACK_Msk)
                    {
                        sercom${SERCOM_INDEX}I2CObj.status = SERCOM_I2C_TRANSFER_STATUS_ERROR;
                        sercom${SERCOM_INDEX}I2CObj.error = SERCOM_I2C_ERROR_NAK;
                    }
                    else
                    {
                        if( 0 == trb->length )
                        {
                            /* Check for last TRB */
                            if( sercom${SERCOM_INDEX}I2CObj.currentTRB == (sercom${SERCOM_INDEX}I2CObj.numTRBs - 1) )
                            {
                                /* Execute acknowledge action succeeded by issuing a stop condition */
                                SERCOM${SERCOM_INDEX}_I2C->I2CM.CTRLB.w |= SERCOM_I2CM_CTRLB_CMD(3);
                            }

                            currentTRBTransferDone = true;
                        }
                        else
                        {
                            /* Write next data byte */
                            SERCOM${SERCOM_INDEX}_I2C->I2CM.DATA.w = *(trb->pbuffer++);

                            trb->length--;

                            sercom${SERCOM_INDEX}I2CObj.processedTRBDataLength++;
                        }
                    }

                    break;
                }

                case SERCOM_I2C_STATE_TRANSFER_READ:
                {
                    trb->length--;

                    sercom${SERCOM_INDEX}I2CObj.processedTRBDataLength++;

                    if(trb->length == 0)
                    {
                        /* Send NACK to the slave from master */
                        SERCOM${SERCOM_INDEX}_I2C->I2CM.CTRLB.w |= SERCOM_I2CM_CTRLB_ACKACT_Msk;

                        if(sercom${SERCOM_INDEX}I2CObj.currentTRB == (sercom${SERCOM_INDEX}I2CObj.numTRBs - 1))
                        {
                            /*
                             * Execute acknowledge action succeeded by issuing
                             * a stop condition.
                             */
                            SERCOM${SERCOM_INDEX}_I2C->I2CM.CTRLB.w |= SERCOM_I2CM_CTRLB_CMD(3);

                            while((SERCOM${SERCOM_INDEX}_I2C->I2CM.SYNCBUSY.w & SERCOM_I2CM_SYNCBUSY_SYSOP_Msk) == SERCOM_I2CM_SYNCBUSY_SYSOP_Msk)
                            {
                                /*
                                 * Wait for synchronization after issuing
                                 * stop command.
                                 */
                            }
                        }
                    }
                    else
                    {
                        /* Send ACK to the slave from master */
                        SERCOM${SERCOM_INDEX}_I2C->I2CM.CTRLB.w &= ~SERCOM_I2CM_CTRLB_ACKACT_Msk;

                        /*
                         * Execute acknowledge action succeeded by a byte read
                         * operation.
                         */
                        SERCOM${SERCOM_INDEX}_I2C->I2CM.CTRLB.w |= SERCOM_I2CM_CTRLB_CMD(2);

                        while((SERCOM${SERCOM_INDEX}_I2C->I2CM.SYNCBUSY.w & SERCOM_I2CM_SYNCBUSY_SYSOP_Msk) == SERCOM_I2CM_SYNCBUSY_SYSOP_Msk)
                        {
                            /*
                             * Wait for synchronization after issuing
                             * stop command.
                             */
                        }
                    }

                    /* Read the received data */
                    *(trb->pbuffer++) = SERCOM${SERCOM_INDEX}_I2C->I2CM.DATA.w;

                    if(trb->length == 0)
                    {
                        currentTRBTransferDone = true;
                    }

                    break;
                }
            }
        }

        /* Error Status */
        if(sercom${SERCOM_INDEX}I2CObj.status == SERCOM_I2C_TRANSFER_STATUS_ERROR)
        {
            if ( sercom${SERCOM_INDEX}I2CObj.callback != NULL )
            {
                sercom${SERCOM_INDEX}I2CObj.callback( sercom${SERCOM_INDEX}I2CObj.context );
            }

            /* Reset the PLib objects and Interrupts */
            sercom${SERCOM_INDEX}I2CObj.numTRBs = 0;
            sercom${SERCOM_INDEX}I2CObj.currentTRB = 0;
            sercom${SERCOM_INDEX}I2CObj.state = SERCOM_I2C_STATE_IDLE;
            SERCOM${SERCOM_INDEX}_I2C->I2CM.INTFLAG.w = SERCOM_I2CM_INTFLAG_MB_Msk | SERCOM_I2CM_INTFLAG_SB_Msk | SERCOM_I2CM_INTFLAG_ERROR_Msk;
        }
        /* Transfer Complete */
        else if(currentTRBTransferDone == true)
        {
            /* Check for last TRB*/
            if(sercom${SERCOM_INDEX}I2CObj.currentTRB == (sercom${SERCOM_INDEX}I2CObj.numTRBs -1))
            {
                sercom${SERCOM_INDEX}I2CObj.status = SERCOM_I2C_TRANSFER_STATUS_SUCCESS;

                if(sercom${SERCOM_INDEX}I2CObj.callback != NULL)
                {
                    sercom${SERCOM_INDEX}I2CObj.callback(sercom${SERCOM_INDEX}I2CObj.context);
                }

                /* Reset the PLib objects and interrupts */
                sercom${SERCOM_INDEX}I2CObj.numTRBs = 0;
                sercom${SERCOM_INDEX}I2CObj.currentTRB = 0;
                sercom${SERCOM_INDEX}I2CObj.state = SERCOM_I2C_STATE_IDLE;
                sercom${SERCOM_INDEX}I2CObj.error = SERCOM_I2C_ERROR_NONE;
                SERCOM${SERCOM_INDEX}_I2C->I2CM.INTFLAG.w = SERCOM_I2CM_INTFLAG_MB_Msk | SERCOM_I2CM_INTFLAG_SB_Msk | SERCOM_I2CM_INTFLAG_ERROR_Msk;
            }
            else
            {
                /*
                 * Get the next TRB from the TRBList, clear processed TRB data
                 * length and send the address.
                 */
                sercom${SERCOM_INDEX}I2CObj.currentTRB++;
                sercom${SERCOM_INDEX}I2CObj.processedTRBDataLength = 0;
                SERCOM_I2C_Start(&sercom${SERCOM_INDEX}I2CTRBsList[sercom${SERCOM_INDEX}I2CObj.currentTRB]);
            }
        }
    }
}
