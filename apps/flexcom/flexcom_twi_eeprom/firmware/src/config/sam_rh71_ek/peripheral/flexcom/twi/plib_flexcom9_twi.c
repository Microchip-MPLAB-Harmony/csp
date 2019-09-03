/*******************************************************************************
  FLEXCOM TWI Peripheral Library Source File

  Company
    Microchip Technology Inc.

  File Name
    plib_flexcom9_twi.c

  Summary
    FLEXCOM TWI peripheral library interface.

  Description
    This file defines the interface to the FLEXCOM TWI peripheral library. This
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

// *****************************************************************************
// *****************************************************************************
// Included Files
// *****************************************************************************
// *****************************************************************************

#include "device.h"
#include "plib_flexcom9_twi.h"

// *****************************************************************************
// *****************************************************************************
// Local Data Type Definitions
// *****************************************************************************
// *****************************************************************************

#define FLEXCOM_TWI_MASTER_MAX_BAUDRATE        (400000U)
#define FLEXCOM_TWI_LOW_LEVEL_TIME_LIMIT       (384000U)
#define FLEXCOM_TWI_CLK_DIVIDER                     (2U)
#define FLEXCOM_TWI_CLK_CALC_ARGU                   (3U)
#define FLEXCOM_TWI_CLK_DIV_MAX                  (0xFFU)
#define FLEXCOM_TWI_CLK_DIV_MIN                     (7U)

// *****************************************************************************
// *****************************************************************************
// Global Data
// *****************************************************************************
// *****************************************************************************

static FLEXCOM_TWI_OBJ flexcom9TwiObj;
static flexcom_registers_t *FLEXCOM9_TWI_Module = FLEXCOM9_REGS;

// *****************************************************************************
// *****************************************************************************
// FLEXCOM9 TWI PLib Interface Routines
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Function:
    void FLEXCOM9_TWI_Initialize(void)

   Summary:
    Initializes given instance of the FLEXCOM TWI peripheral.

   Precondition:
    None.

   Parameters:
    None.

   Returns:
    None
*/

void FLEXCOM9_TWI_Initialize(void)
{
    /* Set FLEXCOM TWI operating mode */
    FLEXCOM9_REGS->FLEX_MR = FLEX_MR_OPMODE_TWI;

    // Reset the i2c Module
    FLEXCOM9_TWI_Module->FLEX_TWI_CR = FLEX_TWI_CR_SWRST_Msk;

    // Disable the I2C Master/Slave Mode
    FLEXCOM9_TWI_Module->FLEX_TWI_CR = FLEX_TWI_CR_MSDIS_Msk |
                                          FLEX_TWI_CR_SVDIS_Msk;

    // Set Baud rate
    FLEXCOM9_TWI_Module->FLEX_TWI_CWGR = ( FLEX_TWI_CWGR_HOLD_Msk & FLEXCOM9_TWI_Module->FLEX_TWI_CWGR) |
                                              FLEX_TWI_CWGR_BRSRCCLK_PERIPH_CLK |
                                            ( FLEX_TWI_CWGR_CLDIV(59) |
                                              FLEX_TWI_CWGR_CHDIV(59) |
                                              FLEX_TWI_CWGR_CKDIV(0) );

    // Starts the transfer by clearing the transmit hold register
    FLEXCOM9_TWI_Module->FLEX_TWI_CR = FLEX_TWI_CR_THRCLR_Msk;

    // Enables interrupt on nack and arbitration lost
    FLEXCOM9_TWI_Module->FLEX_TWI_IER = FLEX_TWI_IER_NACK_Msk |
                                           FLEX_TWI_IER_ARBLST_Msk;

    // Enable Master Mode
    FLEXCOM9_TWI_Module->FLEX_TWI_CR = FLEX_TWI_CR_MSEN_Msk;

    // Initialize the flexcom twi PLib Object
    flexcom9TwiObj.error   = FLEXCOM_TWI_ERROR_NONE;
    flexcom9TwiObj.state   = FLEXCOM_TWI_STATE_IDLE;
}


/******************************************************************************
Local Functions
******************************************************************************/

static void FLEXCOM9_TWI_InitiateRead(void)
{

    flexcom9TwiObj.state = FLEXCOM_TWI_STATE_TRANSFER_READ;

    FLEXCOM9_TWI_Module->FLEX_TWI_MMR |= FLEX_TWI_MMR_MREAD_Msk;

    /* When a single data byte read is performed,
    the START and STOP bits must be set at the same time */
    if(flexcom9TwiObj.readSize == 1)
    {
        FLEXCOM9_TWI_Module->FLEX_TWI_CR = FLEX_TWI_CR_START_Msk | FLEX_TWI_CR_STOP_Msk;
    }
    else
    {
        FLEXCOM9_TWI_Module->FLEX_TWI_CR = FLEX_TWI_CR_START_Msk;
    }

    __enable_irq();
    FLEXCOM9_TWI_Module->FLEX_TWI_IER = FLEX_TWI_IER_RXRDY_Msk | FLEX_TWI_IER_TXCOMP_Msk;
}




static void FLEXCOM9_TWI_InitiateTransfer(uint16_t address, bool type)
{
    // 10-bit Slave Address
    if( address > 0x007F )
    {
        FLEXCOM9_TWI_Module->FLEX_TWI_MMR = FLEX_TWI_MMR_DADR((address & 0x00007F00) >> 8) |
                                               FLEX_TWI_MMR_IADRSZ(1);

        // Set internal address
        FLEXCOM9_TWI_Module->FLEX_TWI_IADR = FLEX_TWI_IADR_IADR(address & 0x000000FF );
    }
    // 7-bit Slave Address
    else
    {
        FLEXCOM9_TWI_Module->FLEX_TWI_MMR = FLEX_TWI_MMR_DADR(address) | FLEX_TWI_MMR_IADRSZ(0);
    }

    flexcom9TwiObj.writeCount= 0;
    flexcom9TwiObj.readCount= 0;

    // Write transfer
    if(type == false)
    {
        // Single Byte Write
        if( flexcom9TwiObj.writeSize == 1 )
        {
            // Single Byte write only
            if(  flexcom9TwiObj.readSize ==0  )
            {
                // Load last byte in transmit register, issue stop condition
                // Generate TXCOMP interrupt after STOP condition has been sent
                flexcom9TwiObj.state = FLEXCOM_TWI_STATE_WAIT_FOR_TXCOMP;

                FLEXCOM9_TWI_Module->FLEX_TWI_THR = FLEX_TWI_THR_TXDATA(flexcom9TwiObj.writeBuffer[flexcom9TwiObj.writeCount++]);
                FLEXCOM9_TWI_Module->FLEX_TWI_CR =  FLEX_TWI_CR_STOP_Msk;
                FLEXCOM9_TWI_Module->FLEX_TWI_IER = FLEX_TWI_IER_TXCOMP_Msk;
            }
            // Single Byte write and than read transfer
            else
            {
                // START bit must be set before the byte is shifted out. Hence disabled interrupt
                __disable_irq();
                FLEXCOM9_TWI_Module->FLEX_TWI_THR = FLEX_TWI_THR_TXDATA(flexcom9TwiObj.writeBuffer[flexcom9TwiObj.writeCount++]);
                // Wait for control byte to be transferred before initiating repeat start for read
                while((FLEXCOM9_TWI_Module->FLEX_TWI_SR & (FLEX_TWI_SR_TXCOMP_Msk | FLEX_TWI_SR_TXRDY_Msk)) != 0);
                while((FLEXCOM9_TWI_Module->FLEX_TWI_SR & (FLEX_TWI_SR_TXRDY_Msk)) ==0);
                type=true;
            }
        }
        // Multi-Byte Write
        else
        {
            flexcom9TwiObj.state = FLEXCOM_TWI_STATE_TRANSFER_WRITE;

            FLEXCOM9_TWI_Module->FLEX_TWI_THR = FLEX_TWI_THR_TXDATA(flexcom9TwiObj.writeBuffer[flexcom9TwiObj.writeCount++]);
            FLEXCOM9_TWI_Module->FLEX_TWI_IER = FLEX_TWI_IDR_TXRDY_Msk | FLEX_TWI_IER_TXCOMP_Msk;
        }
    }
    // Read transfer
    if(type)
    {
        FLEXCOM9_TWI_InitiateRead();
    }
}

// *****************************************************************************
/* Function:
    void FLEXCOM9_TWI_CallbackRegister(FLEXCOM_TWI_CALLBACK callback, uintptr_t contextHandle)

   Summary:
    Sets the pointer to the function (and it's context) to be called when the
    given FLEXCOM TWI's transfer events occur.

   Precondition:
    FLEXCOM9_TWI_Initialize must have been called for the associated FLEXCOM TWI instance.

   Parameters:
    callback - A pointer to a function with a calling signature defined
    by the FLEXCOM_TWI_CALLBACK data type.

    context - A value (usually a pointer) passed (unused) into the function
    identified by the callback parameter.

   Returns:
    None.
*/

void FLEXCOM9_TWI_CallbackRegister(FLEXCOM_TWI_CALLBACK callback, uintptr_t contextHandle)
{
    if (callback == NULL)
    {
        return;
    }

    flexcom9TwiObj.callback = callback;
    flexcom9TwiObj.context = contextHandle;
}

// *****************************************************************************
/* Function:
    bool FLEXCOM9_TWI_IsBusy(void)

   Summary:
    Returns the Peripheral busy status.

   Precondition:
    FLEXCOM9_TWI_Initialize must have been called for the associated FLEXCOM TWI instance.

   Parameters:
    None.

   Returns:
    true - Busy.
    false - Not busy.
*/

bool FLEXCOM9_TWI_IsBusy(void)
{
    if( flexcom9TwiObj.state == FLEXCOM_TWI_STATE_IDLE )
    {
        return false;
    }
    else
    {
        return true;
    }
}



// *****************************************************************************
/* Function:
    bool FLEXCOM9_TWI_Read(uint16_t address, uint8_t *pdata, size_t length)

   Summary:
    Reads data from the slave.

   Precondition:
    FLEXCOM9_TWI_Initialize must have been called for the associated FLEXCOM TWI instance.

   Parameters:
    address - 7-bit / 10-bit slave address.
    pdata   - pointer to destination data buffer
    length  - length of data buffer in number of bytes.

   Returns:
    Request status.
    True - Request was successful.
    False - Request has failed.
*/

bool FLEXCOM9_TWI_Read(uint16_t address, uint8_t *pdata, size_t length)
{
    // Check for ongoing transfer
    if( flexcom9TwiObj.state != FLEXCOM_TWI_STATE_IDLE )
    {
        return false;
    }

    flexcom9TwiObj.address=address;
    flexcom9TwiObj.readBuffer=pdata;
    flexcom9TwiObj.readSize=length;
    flexcom9TwiObj.writeBuffer=NULL;
    flexcom9TwiObj.writeSize=0;
    flexcom9TwiObj.error = FLEXCOM_TWI_ERROR_NONE;

    FLEXCOM9_TWI_InitiateTransfer(address, true);

    return true;
}

// *****************************************************************************
/* Function:
    bool FLEXCOM9_TWI_Write(uint16_t address, uint8_t *pdata, size_t length)

   Summary:
    Writes data onto the slave.

   Precondition:
    FLEXCOM9_TWI_Initialize must have been called for the associated FLEXCOM TWI instance.

   Parameters:
    address - 7-bit / 10-bit slave address.
    pdata   - pointer to source data buffer
    length  - length of data buffer in number of bytes.

   Returns:
    Request status.
    True - Request was successful.
    False - Request has failed.
*/

bool FLEXCOM9_TWI_Write(uint16_t address, uint8_t *pdata, size_t length)
{
    // Check for ongoing transfer
    if( flexcom9TwiObj.state != FLEXCOM_TWI_STATE_IDLE )
    {
        return false;
    }

    flexcom9TwiObj.address=address;
    flexcom9TwiObj.readBuffer=NULL;
    flexcom9TwiObj.readSize=0;
    flexcom9TwiObj.writeBuffer=pdata;
    flexcom9TwiObj.writeSize=length;
    flexcom9TwiObj.error = FLEXCOM_TWI_ERROR_NONE;

    FLEXCOM9_TWI_InitiateTransfer(address, false);

    return true;
}

// *****************************************************************************
/* Function:
    bool FLEXCOM9_TWI_WriteRead(uint16_t address, uint8_t *wdata, size_t wlength, uint8_t *rdata, size_t rlength)

   Summary:
    Write and Read data from Slave.

   Precondition:
    FLEXCOM9_TWI_Initialize must have been called for the associated FLEXCOM TWI instance.

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
*/

bool FLEXCOM9_TWI_WriteRead(uint16_t address, uint8_t *wdata, size_t wlength, uint8_t *rdata, size_t rlength)
{

    // Check for ongoing transfer
    if( flexcom9TwiObj.state != FLEXCOM_TWI_STATE_IDLE )
    {
        return false;
    }

    flexcom9TwiObj.address=address;
    flexcom9TwiObj.readBuffer=rdata;
    flexcom9TwiObj.readSize=rlength;
    flexcom9TwiObj.writeBuffer=wdata;
    flexcom9TwiObj.writeSize=wlength;
    flexcom9TwiObj.error = FLEXCOM_TWI_ERROR_NONE;

    FLEXCOM9_TWI_InitiateTransfer(address, false);

    return true;
}

// *****************************************************************************
/* Function:
    FLEXCOM_TWI_ERROR FLEXCOM9_TWI_ErrorGet(void)

   Summary:
    Returns the error during transfer.

   Precondition:
    FLEXCOM9_TWI_Initialize must have been called for the associated FLEXCOM TWI instance.

   Parameters:
    None.

   Returns:
    Error during transfer.
*/

FLEXCOM_TWI_ERROR FLEXCOM9_TWI_ErrorGet(void)
{
    FLEXCOM_TWI_ERROR error;

    error = flexcom9TwiObj.error;
    flexcom9TwiObj.error = FLEXCOM_TWI_ERROR_NONE;

    return error;
}

bool FLEXCOM9_TWI_TransferSetup(FLEXCOM_TWI_TRANSFER_SETUP* setup, uint32_t srcClkFreq )
{       
    uint32_t i2cClkSpeed;
    uint32_t cldiv;
    uint8_t ckdiv = 0;
    
    if (setup == NULL)
    {
        return false;
    }        
        
    i2cClkSpeed = setup->clkSpeed;
    
    /* Maximum I2C clock speed in Master mode cannot be greater than 400 KHz */
    if (i2cClkSpeed > 4000000)
    {
        return false;
    }
    
    if( srcClkFreq == 0)
    {
        srcClkFreq = 50000000;
    }            
    
    /* Formula for calculating baud value involves two unknowns. Fix one unknown and calculate the other. 
       Fix the CKDIV value and see if CLDIV (or CHDIV) fits into the 8-bit register. */
       
    /* Calculate CLDIV with CKDIV set to 0 */
    cldiv = (srcClkFreq /(2 * i2cClkSpeed)) - 3;
                   
    /* CLDIV must fit within 8-bits and CKDIV must fit within 3-bits */
    while ((cldiv > 255) && (ckdiv < 7))
    {
        ckdiv++;
        cldiv /= 2;
    }
    
    if (cldiv > 255)
    {
        /* Could not generate CLDIV and CKDIV register values for the requested baud rate */
        return false;
    }
    
    // Set Baud rate
    FLEXCOM9_TWI_Module->FLEX_TWI_CWGR = ( FLEX_TWI_CWGR_HOLD_Msk & FLEXCOM9_TWI_Module->FLEX_TWI_CWGR) |
                                              FLEX_TWI_CWGR_BRSRCCLK_PERIPH_CLK |
                                            ( FLEX_TWI_CWGR_CLDIV(cldiv) |
                                              FLEX_TWI_CWGR_CHDIV(cldiv) |
                                              FLEX_TWI_CWGR_CKDIV(ckdiv) );

    return true;
}

// *****************************************************************************
/* Function:
    void FLEXCOM9_InterruptHandler(void)

   Summary:
    FLEXCOM9_TWI Peripheral Interrupt Handler.

   Description:
    This function is FLEXCOM9_TWI Peripheral Interrupt Handler and will
    called on every FLEXCOM9_TWI interrupt.

   Precondition:
    None.

   Parameters:
    None.

   Returns:
    None.

   Remarks:
    The function is called as peripheral instance's interrupt handler if the
    instance interrupt is enabled. If peripheral instance's interrupt is not
    enabled user need to call it from the main while loop of the application.
*/

void FLEXCOM9_InterruptHandler(void)
{
    uint32_t status;

    // Read the peripheral status
    status = FLEXCOM9_TWI_Module->FLEX_TWI_SR;

    /* checks if Slave has Nacked */
    if( status & FLEX_TWI_SR_NACK_Msk )
    {
        flexcom9TwiObj.state = FLEXCOM_TWI_STATE_ERROR;
        flexcom9TwiObj.error = FLEXCOM_TWI_ERROR_NACK;
    }

    if( status & FLEX_TWI_SR_TXCOMP_Msk )
    {
        /* Disable and Enable I2C Master */
        FLEXCOM9_TWI_Module->FLEX_TWI_CR = FLEX_TWI_CR_MSDIS_Msk;
        FLEXCOM9_TWI_Module->FLEX_TWI_CR = FLEX_TWI_CR_MSEN_Msk;

        /* Disable Interrupt */
        FLEXCOM9_TWI_Module->FLEX_TWI_IDR = FLEX_TWI_IDR_TXCOMP_Msk |
                                 FLEX_TWI_IDR_TXRDY_Msk  |
                                 FLEX_TWI_IDR_RXRDY_Msk;
    }

    /* checks if the arbitration is lost in multi-master scenario */
    if( status & FLEX_TWI_SR_ARBLST_Msk )
    {
        /* Re-initiate the transfer if arbitration is lost in
         * between of the transfer
         */
        flexcom9TwiObj.state = FLEXCOM_TWI_STATE_ADDR_SEND;
    }

    if( flexcom9TwiObj.error == FLEXCOM_TWI_ERROR_NONE )
    {
        switch( flexcom9TwiObj.state )
        {
            case FLEXCOM_TWI_STATE_ADDR_SEND:
            {
                if (flexcom9TwiObj.writeSize != 0 )
                {
                    // Initiate Write transfer
                    FLEXCOM9_TWI_InitiateTransfer(flexcom9TwiObj.address, false);
                }
                else
                {
                    // Initiate Read transfer
                    FLEXCOM9_TWI_InitiateTransfer(flexcom9TwiObj.address, true);
                }
            }
            break;

            case FLEXCOM_TWI_STATE_TRANSFER_WRITE:
            {
                /* checks if master is ready to transmit */
                if( status & FLEX_TWI_SR_TXRDY_Msk )
                {
                    // Write Last Byte and then initiate read transfer
                    if( ( flexcom9TwiObj.writeCount == (flexcom9TwiObj.writeSize -1) ) && ( flexcom9TwiObj.readSize != 0 ))
                    {
                        // START bit must be set before the last byte is shifted out to generate repeat start. Hence disabled interrupt
                        __disable_irq();
                        FLEXCOM9_TWI_Module->FLEX_TWI_IDR = FLEX_TWI_IDR_TXRDY_Msk;
                        FLEXCOM9_TWI_Module->FLEX_TWI_THR = FLEX_TWI_THR_TXDATA(flexcom9TwiObj.writeBuffer[flexcom9TwiObj.writeCount++]);
                        FLEXCOM9_TWI_InitiateRead();
                    }
                    // Write Last byte and then issue STOP condition
                    else if ( flexcom9TwiObj.writeCount == (flexcom9TwiObj.writeSize -1))
                    {
                        // Load last byte in transmit register, issue stop condition
                        // Generate TXCOMP interrupt after STOP condition has been sent
                        FLEXCOM9_TWI_Module->FLEX_TWI_THR = FLEX_TWI_THR_TXDATA(flexcom9TwiObj.writeBuffer[flexcom9TwiObj.writeCount++]);
                        FLEXCOM9_TWI_Module->FLEX_TWI_CR = FLEX_TWI_CR_STOP_Msk;
                        FLEXCOM9_TWI_Module->FLEX_TWI_IDR = FLEX_TWI_IDR_TXRDY_Msk;

                        /* Check TXCOMP to confirm if STOP condition has been sent, otherwise wait for TXCOMP interrupt */
                        status = FLEXCOM9_TWI_Module->FLEX_TWI_SR;
                        if( status & FLEX_TWI_SR_TXCOMP_Msk )
                        {
                            flexcom9TwiObj.state = FLEXCOM_TWI_STATE_TRANSFER_DONE;
                        }
                        else
                        {
                            flexcom9TwiObj.state = FLEXCOM_TWI_STATE_WAIT_FOR_TXCOMP;
                        }
                    }
                    // Write next byte
                    else
                    {
                        FLEXCOM9_TWI_Module->FLEX_TWI_THR = FLEX_TWI_THR_TXDATA(flexcom9TwiObj.writeBuffer[flexcom9TwiObj.writeCount++]);
                    }

                    // Dummy read to ensure that TXRDY bit is cleared
                    status = FLEXCOM9_TWI_Module->FLEX_TWI_SR;
                }

                break;
            }

            case FLEXCOM_TWI_STATE_TRANSFER_READ:
            {
                /* checks if master has received the data */
                if( status & FLEX_TWI_SR_RXRDY_Msk )
                {
                    // Set the STOP (or START) bit before reading the FLEX_TWI_RHR on the next-to-last access
                    if(  flexcom9TwiObj.readCount == (flexcom9TwiObj.readSize - 2) )
                    {
                        FLEXCOM9_TWI_Module->FLEX_TWI_CR = FLEX_TWI_CR_STOP_Msk;
                    }

                    /* read the received data */
                    flexcom9TwiObj.readBuffer[flexcom9TwiObj.readCount++] = (uint8_t)(FLEXCOM9_TWI_Module->FLEX_TWI_RHR & FLEX_TWI_RHR_RXDATA_Msk);

                    /* checks if transmission has reached at the end */
                    if( flexcom9TwiObj.readCount == flexcom9TwiObj.readSize )
                    {
                        /* Disable the RXRDY interrupt*/
                        FLEXCOM9_TWI_Module->FLEX_TWI_IDR = FLEX_TWI_IDR_RXRDY_Msk;

                        /* Check TXCOMP to confirm if STOP condition has been sent, otherwise wait for TXCOMP interrupt */
                        status = FLEXCOM9_TWI_Module->FLEX_TWI_SR;
                        if( status & FLEX_TWI_SR_TXCOMP_Msk )
                        {
                            flexcom9TwiObj.state = FLEXCOM_TWI_STATE_TRANSFER_DONE;
                        }
                        else
                        {
                            flexcom9TwiObj.state = FLEXCOM_TWI_STATE_WAIT_FOR_TXCOMP;
                        }
                    }
                }
                break;
            }

            case FLEXCOM_TWI_STATE_WAIT_FOR_TXCOMP:
            {
                if( status & FLEX_TWI_SR_TXCOMP_Msk )
                {
                    flexcom9TwiObj.state = FLEXCOM_TWI_STATE_TRANSFER_DONE;
                }
                break;
            }

            default:
            {
                break;
            }
        }
    }

    if (flexcom9TwiObj.state == FLEXCOM_TWI_STATE_ERROR)
    {
        // NACK is received,
        flexcom9TwiObj.state = FLEXCOM_TWI_STATE_IDLE;
        FLEXCOM9_TWI_Module->FLEX_TWI_IDR = FLEX_TWI_IDR_TXCOMP_Msk | FLEX_TWI_IDR_TXRDY_Msk | FLEX_TWI_IDR_RXRDY_Msk;

        // Disable and Enable I2C Master
        FLEXCOM9_TWI_Module->FLEX_TWI_CR = FLEX_TWI_CR_MSDIS_Msk;
        FLEXCOM9_TWI_Module->FLEX_TWI_CR = FLEX_TWI_CR_MSEN_Msk;

        if ( flexcom9TwiObj.callback != NULL )
        {
            flexcom9TwiObj.callback( flexcom9TwiObj.context );
        }
    }

    // check for completion of transfer
    if( flexcom9TwiObj.state == FLEXCOM_TWI_STATE_TRANSFER_DONE )
    {

        flexcom9TwiObj.error = FLEXCOM_TWI_ERROR_NONE;

        // Reset the PLib objects and Interrupts
        flexcom9TwiObj.state = FLEXCOM_TWI_STATE_IDLE;
        FLEXCOM9_TWI_Module->FLEX_TWI_IDR = FLEX_TWI_IDR_TXCOMP_Msk |
                                 FLEX_TWI_IDR_TXRDY_Msk  |
                                 FLEX_TWI_IDR_RXRDY_Msk;

        // Disable and Enable I2C Master
        FLEXCOM9_TWI_Module->FLEX_TWI_CR = FLEX_TWI_CR_MSDIS_Msk;
        FLEXCOM9_TWI_Module->FLEX_TWI_CR = FLEX_TWI_CR_MSEN_Msk;
        if ( flexcom9TwiObj.callback != NULL )
        {
            flexcom9TwiObj.callback( flexcom9TwiObj.context );
        }
    }

    return;
}

/*******************************************************************************
 End of File
*/
