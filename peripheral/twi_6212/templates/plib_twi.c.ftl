/*******************************************************************************
  TWI Peripheral Library Source File

  Company
    Microchip Technology Inc.

  File Name
    plib_${TWI_INSTANCE_NAME?lower_case}.c

  Summary
    TWI peripheral library interface.

  Description

  Remarks:

*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
* Copyright (C) 2019 Microchip Technology Inc. and its subsidiaries.
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
<#if core.CoreSysIntFile == true>
#include "interrupts.h"
</#if>
#include "device.h"
#include "plib_${TWI_INSTANCE_NAME?lower_case}.h"

// *****************************************************************************
// *****************************************************************************
// Global Data
// *****************************************************************************
// *****************************************************************************

static TWI_OBJ ${TWI_INSTANCE_NAME?lower_case}Obj;

// *****************************************************************************
// *****************************************************************************
// ${TWI_INSTANCE_NAME} PLib Interface Routines
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Function:
    void ${TWI_INSTANCE_NAME}_Initialize(void)

   Summary:
    Initializes given instance of the TWI peripheral.

   Precondition:
    None.

   Parameters:
    None.

   Returns:
    None
*/

void ${TWI_INSTANCE_NAME}_Initialize(void)
{
    // Reset the i2c Module
    ${TWI_INSTANCE_NAME}_REGS->TWI_CR = TWI_CR_SWRST_Msk;

    // Disable the I2C Master/Slave Mode
    ${TWI_INSTANCE_NAME}_REGS->TWI_CR = TWI_CR_MSDIS_Msk | TWI_CR_SVDIS_Msk;

    // Set Baud rate
    ${TWI_INSTANCE_NAME}_REGS->TWI_CWGR = TWI_CWGR_CLDIV(${TWI_CWGR_CLDIV}U) | TWI_CWGR_CHDIV(${TWI_CWGR_CHDIV}U) | TWI_CWGR_CKDIV(${TWI_CWGR_CKDIV}U);

    // Enables interrupt on nack and arbitration lost
    ${TWI_INSTANCE_NAME}_REGS->TWI_IER = TWI_IER_NACK_Msk | TWI_IER_ARBLST_Msk;

    // Enable Master Mode
    ${TWI_INSTANCE_NAME}_REGS->TWI_CR = TWI_CR_MSEN_Msk;

    // Initialize the twi PLib Object
    ${TWI_INSTANCE_NAME?lower_case}Obj.error   = TWI_ERROR_NONE;
    ${TWI_INSTANCE_NAME?lower_case}Obj.state   = TWI_STATE_IDLE;
}

/******************************************************************************
Local Functions
******************************************************************************/

static void ${TWI_INSTANCE_NAME}_InitiateRead(void)
{
    ${TWI_INSTANCE_NAME?lower_case}Obj.state = TWI_STATE_TRANSFER_READ;

    ${TWI_INSTANCE_NAME}_REGS->TWI_MMR |= TWI_MMR_MREAD_Msk;

    /* When a single data byte read is performed,
    the START and STOP bits must be set at the same time */
    if(${TWI_INSTANCE_NAME?lower_case}Obj.readSize == 1U)
    {
        ${TWI_INSTANCE_NAME}_REGS->TWI_CR = TWI_CR_START_Msk | TWI_CR_STOP_Msk;
    }
    else
    {
        ${TWI_INSTANCE_NAME}_REGS->TWI_CR = TWI_CR_START_Msk;
    }

    __enable_irq();
    ${TWI_INSTANCE_NAME}_REGS->TWI_IER = TWI_IER_RXRDY_Msk | TWI_IER_TXCOMP_Msk;
}




static void ${TWI_INSTANCE_NAME}_InitiateTransfer(uint16_t address, bool type)
{
    // 10-bit Slave Address
    if( address > 0x007FU )
    {
        ${TWI_INSTANCE_NAME}_REGS->TWI_MMR = TWI_MMR_DADR(((uint32_t)address & 0x00007F00U) >> 8U) | TWI_MMR_IADRSZ(1U);

        // Set internal address
        ${TWI_INSTANCE_NAME}_REGS->TWI_IADR = TWI_IADR_IADR((uint32_t)address & 0x000000FFU );
    }
    // 7-bit Slave Address
    else
    {
        ${TWI_INSTANCE_NAME}_REGS->TWI_MMR = TWI_MMR_DADR((uint32_t)address) | TWI_MMR_IADRSZ(0U);
    }

    ${TWI_INSTANCE_NAME?lower_case}Obj.writeCount= 0;
    ${TWI_INSTANCE_NAME?lower_case}Obj.readCount= 0;

    // Write transfer
    if(type == false)
    {
        // Single Byte Write
        if( ${TWI_INSTANCE_NAME?lower_case}Obj.writeSize == 1U )
        {
            // Single Byte write only
            if(  ${TWI_INSTANCE_NAME?lower_case}Obj.readSize ==0U  )
            {
                // Load last byte in transmit register, issue stop condition
                // Generate TXCOMP interrupt after STOP condition has been sent
                ${TWI_INSTANCE_NAME?lower_case}Obj.state = TWI_STATE_WAIT_FOR_TXCOMP;

                ${TWI_INSTANCE_NAME}_REGS->TWI_THR = TWI_THR_TXDATA((uint32_t)${TWI_INSTANCE_NAME?lower_case}Obj.writeBuffer[${TWI_INSTANCE_NAME?lower_case}Obj.writeCount]);
                ${TWI_INSTANCE_NAME?lower_case}Obj.writeCount++;
                ${TWI_INSTANCE_NAME}_REGS->TWI_CR =  TWI_CR_STOP_Msk;
                ${TWI_INSTANCE_NAME}_REGS->TWI_IER = TWI_IER_TXCOMP_Msk;
            }
            // Single Byte write and than read transfer
            else
            {
                // START bit must be set before the byte is shifted out. Hence disabled interrupt
                __disable_irq();
                ${TWI_INSTANCE_NAME}_REGS->TWI_THR = TWI_THR_TXDATA((uint32_t)${TWI_INSTANCE_NAME?lower_case}Obj.writeBuffer[${TWI_INSTANCE_NAME?lower_case}Obj.writeCount]);
                ${TWI_INSTANCE_NAME?lower_case}Obj.writeCount++;

                // Wait for control byte to be transferred before initiating repeat start for read
                while((${TWI_INSTANCE_NAME}_REGS->TWI_SR & (TWI_SR_TXCOMP_Msk | TWI_SR_TXRDY_Msk)) != 0U)
                    {

                    }
                while((${TWI_INSTANCE_NAME}_REGS->TWI_SR & (TWI_SR_TXRDY_Msk)) ==0U)
                    {

                    }
                type=true;
            }
        }
        // Multi-Byte Write
        else
        {
            ${TWI_INSTANCE_NAME?lower_case}Obj.state = TWI_STATE_TRANSFER_WRITE;

            ${TWI_INSTANCE_NAME}_REGS->TWI_THR = TWI_THR_TXDATA((uint32_t)${TWI_INSTANCE_NAME?lower_case}Obj.writeBuffer[${TWI_INSTANCE_NAME?lower_case}Obj.writeCount]);
            ${TWI_INSTANCE_NAME?lower_case}Obj.writeCount++;
            ${TWI_INSTANCE_NAME}_REGS->TWI_IER = TWI_IDR_TXRDY_Msk | TWI_IER_TXCOMP_Msk;
        }
    }
    // Read transfer
    if(type)
    {
        ${TWI_INSTANCE_NAME}_InitiateRead();
    }
}


// *****************************************************************************
/* Function:
    void ${TWI_INSTANCE_NAME}_CallbackRegister(TWI_CALLBACK callback, uintptr_t contextHandle)

   Summary:
    Sets the pointer to the function (and it's context) to be called when the
    given TWI's transfer events occur.

   Precondition:
    TWIx_Initialize must have been called for the associated TWI instance.

   Parameters:
    callback - A pointer to a function with a calling signature defined
    by the TWI_CALLBACK data type.

    context - A value (usually a pointer) passed (unused) into the function
    identified by the callback parameter.

   Returns:
    None.
*/

void ${TWI_INSTANCE_NAME}_CallbackRegister(TWI_CALLBACK callback, uintptr_t contextHandle)
{
    if (callback != NULL)
    {
        ${TWI_INSTANCE_NAME?lower_case}Obj.callback = callback;
        ${TWI_INSTANCE_NAME?lower_case}Obj.context = contextHandle;
    }
}

// *****************************************************************************
/* Function:
    bool ${TWI_INSTANCE_NAME}_IsBusy(void)

   Summary:
    Returns the Peripheral busy status.

   Precondition:
    TWIx_Initialize must have been called for the associated TWI instance.

   Parameters:
    None.

   Returns:
    true - Busy.
    false - Not busy.
*/

bool ${TWI_INSTANCE_NAME}_IsBusy(void)
{
    return (${TWI_INSTANCE_NAME?lower_case}Obj.state != TWI_STATE_IDLE );
}

// *****************************************************************************
/* Function:
    bool ${TWI_INSTANCE_NAME}_Read(uint16_t address, uint8_t *pdata, size_t length)

   Summary:
    Reads data from the slave.

   Precondition:
    TWIx_Initialize must have been called for the associated TWI instance.

   Parameters:
    address - 7-bit / 10-bit slave address.
    pdata   - pointer to destination data buffer
    length  - length of data buffer in number of bytes.

   Returns:
    Request status.
    True - Request was successful.
    False - Request has failed.
*/

bool ${TWI_INSTANCE_NAME}_Read(uint16_t address, uint8_t *pdata, size_t length)
{
    bool readStatus = false;
    // Check for ongoing transfer
    if( ${TWI_INSTANCE_NAME?lower_case}Obj.state == TWI_STATE_IDLE )
    {
        ${TWI_INSTANCE_NAME?lower_case}Obj.address=address;
        ${TWI_INSTANCE_NAME?lower_case}Obj.readBuffer=pdata;
        ${TWI_INSTANCE_NAME?lower_case}Obj.readSize=length;
        ${TWI_INSTANCE_NAME?lower_case}Obj.writeBuffer=NULL;
        ${TWI_INSTANCE_NAME?lower_case}Obj.writeSize=0;
        ${TWI_INSTANCE_NAME?lower_case}Obj.error = TWI_ERROR_NONE;

        ${TWI_INSTANCE_NAME}_InitiateTransfer(address, true);
        readStatus = true ;
    }
        return readStatus;
}

// *****************************************************************************
/* Function:
    bool ${TWI_INSTANCE_NAME}_Write(uint16_t address, uint8_t *pdata, size_t length)

   Summary:
    Writes data onto the slave.

   Precondition:
    TWIx_Initialize must have been called for the associated TWI instance.

   Parameters:
    address - 7-bit / 10-bit slave address.
    pdata   - pointer to source data buffer
    length  - length of data buffer in number of bytes.

   Returns:
    Request status.
    True - Request was successful.
    False - Request has failed.
*/

bool ${TWI_INSTANCE_NAME}_Write(uint16_t address, uint8_t *pdata, size_t length)
{
    bool writeStatus = false;
    // Check for ongoing transfer
    if( ${TWI_INSTANCE_NAME?lower_case}Obj.state == TWI_STATE_IDLE )
    {
        ${TWI_INSTANCE_NAME?lower_case}Obj.address=address;
        ${TWI_INSTANCE_NAME?lower_case}Obj.readBuffer=NULL;
        ${TWI_INSTANCE_NAME?lower_case}Obj.readSize=0;
        ${TWI_INSTANCE_NAME?lower_case}Obj.writeBuffer=pdata;
        ${TWI_INSTANCE_NAME?lower_case}Obj.writeSize=length;
        ${TWI_INSTANCE_NAME?lower_case}Obj.error = TWI_ERROR_NONE;

        ${TWI_INSTANCE_NAME}_InitiateTransfer(address, false);
        writeStatus = true;
    }
        return writeStatus;
}

// *****************************************************************************
/* Function:
    bool ${TWI_INSTANCE_NAME}_WriteRead(uint16_t address, uint8_t *wdata, size_t wlength, uint8_t *rdata, size_t rlength)

   Summary:
    Write and Read data from Slave.

   Precondition:
    TWIx_Initialize must have been called for the associated TWI instance.

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

bool ${TWI_INSTANCE_NAME}_WriteRead(uint16_t address, uint8_t *wdata, size_t wlength, uint8_t *rdata, size_t rlength)
{
    bool wrrdStatus = false;

    // Check for ongoing transfer
    if( ${TWI_INSTANCE_NAME?lower_case}Obj.state == TWI_STATE_IDLE )
    {
        ${TWI_INSTANCE_NAME?lower_case}Obj.address=address;
        ${TWI_INSTANCE_NAME?lower_case}Obj.readBuffer=rdata;
        ${TWI_INSTANCE_NAME?lower_case}Obj.readSize=rlength;
        ${TWI_INSTANCE_NAME?lower_case}Obj.writeBuffer=wdata;
        ${TWI_INSTANCE_NAME?lower_case}Obj.writeSize=wlength;
        ${TWI_INSTANCE_NAME?lower_case}Obj.error = TWI_ERROR_NONE;

        ${TWI_INSTANCE_NAME}_InitiateTransfer(address, false);
        wrrdStatus = true;
    }
        return wrrdStatus;
}

// *****************************************************************************
/* Function:
    TWI_ERROR ${TWI_INSTANCE_NAME}_ErrorGet(void)

   Summary:
    Returns the error during transfer.

   Precondition:
    TWIx_Initialize must have been called for the associated TWI instance.

   Parameters:
    None.

   Returns:
    Error during transfer.
*/

TWI_ERROR ${TWI_INSTANCE_NAME}_ErrorGet(void)
{
    TWI_ERROR error;

    error = ${TWI_INSTANCE_NAME?lower_case}Obj.error;
    ${TWI_INSTANCE_NAME?lower_case}Obj.error = TWI_ERROR_NONE;

    return error;
}

bool ${TWI_INSTANCE_NAME}_TransferSetup( TWI_TRANSFER_SETUP* setup, uint32_t srcClkFreq )
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
    if (i2cClkSpeed > 4000000U)
    {
        return false;
    }

    if(srcClkFreq == 0U)
    {
        srcClkFreq = ${TWI_CLK_SRC_FREQ};
    }

    /* Formula for calculating baud value involves two unknowns. Fix one unknown and calculate the other.
       Fix the CKDIV value and see if CLDIV (or CHDIV) fits into the 8-bit register. */

    /* Calculate CLDIV with CKDIV set to 0 */
    cldiv = (srcClkFreq /(2U * i2cClkSpeed)) - 4U;

    /* CLDIV must fit within 8-bits and CKDIV must fit within 3-bits */
    while ((cldiv > 255U) && (ckdiv < 7U))
    {
        ckdiv++;
        cldiv /= 2U;
    }

    if (cldiv > 255U)
    {
        /* Could not generate CLDIV and CKDIV register values for the requested baud rate */
        return false;
    }

    /* set clock waveform generator register */
    <@compress single_line=true>${TWI_INSTANCE_NAME}_REGS->TWI_CWGR = (TWI_CWGR_HOLD_Msk & ${TWI_INSTANCE_NAME}_REGS->TWI_CWGR)
                                                                          | TWI_CWGR_CLDIV(cldiv)
                                                                          | TWI_CWGR_CHDIV(cldiv)
                                                                          | TWI_CWGR_CKDIV((uint32_t)ckdiv)</@compress>;

    return true;
}

void ${TWI_INSTANCE_NAME}_TransferAbort( void )
{
    ${TWI_INSTANCE_NAME?lower_case}Obj.error = TWI_ERROR_NONE;

    // Reset the PLib objects and Interrupts
    ${TWI_INSTANCE_NAME?lower_case}Obj.state = TWI_STATE_IDLE;
    ${TWI_INSTANCE_NAME}_REGS->TWI_IDR = TWI_IDR_TXCOMP_Msk | TWI_IDR_TXRDY_Msk | TWI_IDR_RXRDY_Msk;

    /* Disable and Enable I2C Master */
    ${TWI_INSTANCE_NAME}_REGS->TWI_CR = TWI_CR_MSDIS_Msk;
    ${TWI_INSTANCE_NAME}_REGS->TWI_CR = TWI_CR_MSEN_Msk;
}

// *****************************************************************************
/* Function:
    void ${TWI_INSTANCE_NAME}_InterruptHandler(void)

   Summary:
    ${TWI_INSTANCE_NAME} Peripheral Interrupt Handler.

   Description:
    This function is ${TWI_INSTANCE_NAME} Peripheral Interrupt Handler and will
    called on every ${TWI_INSTANCE_NAME} interrupt.

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

void ${TWI_INSTANCE_NAME}_InterruptHandler(void)
{
    uint32_t status;

    // Read the peripheral status
    status = ${TWI_INSTANCE_NAME}_REGS->TWI_SR;

    /* checks if Slave has Nacked */
    if( (status & TWI_SR_NACK_Msk) != 0U )
    {
        ${TWI_INSTANCE_NAME?lower_case}Obj.state = TWI_STATE_ERROR;
        ${TWI_INSTANCE_NAME?lower_case}Obj.error = TWI_ERROR_NACK;
    }


    if( (status & TWI_SR_TXCOMP_Msk) != 0U )
    {
        /* Disable and Enable I2C Master */
        ${TWI_INSTANCE_NAME}_REGS->TWI_CR = TWI_CR_MSDIS_Msk;
        ${TWI_INSTANCE_NAME}_REGS->TWI_CR = TWI_CR_MSEN_Msk;

        /* Disable Interrupt */
        ${TWI_INSTANCE_NAME}_REGS->TWI_IDR = TWI_IDR_TXCOMP_Msk |
                                 TWI_IDR_TXRDY_Msk  |
                                 TWI_IDR_RXRDY_Msk;
    }

    /* checks if the arbitration is lost in multi-master scenario */
    if( (status & TWI_SR_ARBLST_Msk) != 0U )
    {
        /* Re-initiate the transfer if arbitration is lost in
         * between of the transfer
         */
        ${TWI_INSTANCE_NAME?lower_case}Obj.state = TWI_STATE_ADDR_SEND;
    }


    if( ${TWI_INSTANCE_NAME?lower_case}Obj.error == TWI_ERROR_NONE)
    {
        switch( ${TWI_INSTANCE_NAME?lower_case}Obj.state )
        {
            case TWI_STATE_ADDR_SEND:
            {
                if (${TWI_INSTANCE_NAME?lower_case}Obj.writeSize != 0U )
                {
                    // Initiate Write transfer
                    ${TWI_INSTANCE_NAME}_InitiateTransfer(${TWI_INSTANCE_NAME?lower_case}Obj.address, false);
                }
                else
                {
                    // Initiate Read transfer
                    ${TWI_INSTANCE_NAME}_InitiateTransfer(${TWI_INSTANCE_NAME?lower_case}Obj.address, true);
                }
            }
            break;

            case TWI_STATE_TRANSFER_WRITE:
            {
                /* checks if master is ready to transmit */
                if( (status & TWI_SR_TXRDY_Msk) != 0U )
                {
                    // Write Last Byte and then initiate read transfer
                    if( ( ${TWI_INSTANCE_NAME?lower_case}Obj.writeCount == (${TWI_INSTANCE_NAME?lower_case}Obj.writeSize -1U) ) && ( ${TWI_INSTANCE_NAME?lower_case}Obj.readSize != 0U ))
                    {
                        // START bit must be set before the last byte is shifted out to generate repeat start. Hence disabled interrupt
                        __disable_irq();
                        ${TWI_INSTANCE_NAME}_REGS->TWI_IDR = TWI_IDR_TXRDY_Msk;
                        ${TWI_INSTANCE_NAME}_REGS->TWI_THR = TWI_THR_TXDATA((uint32_t)${TWI_INSTANCE_NAME?lower_case}Obj.writeBuffer[${TWI_INSTANCE_NAME?lower_case}Obj.writeCount]);
                        ${TWI_INSTANCE_NAME?lower_case}Obj.writeCount++;
                        ${TWI_INSTANCE_NAME}_InitiateRead();
                    }
                    // Write Last byte and then issue STOP condition
                    else if ( ${TWI_INSTANCE_NAME?lower_case}Obj.writeCount == (${TWI_INSTANCE_NAME?lower_case}Obj.writeSize -1U))
                    {
                        // Load last byte in transmit register, issue stop condition
                        // Generate TXCOMP interrupt after STOP condition has been sent
                        ${TWI_INSTANCE_NAME}_REGS->TWI_THR = TWI_THR_TXDATA((uint32_t)${TWI_INSTANCE_NAME?lower_case}Obj.writeBuffer[${TWI_INSTANCE_NAME?lower_case}Obj.writeCount]);
                        ${TWI_INSTANCE_NAME?lower_case}Obj.writeCount++;
                        ${TWI_INSTANCE_NAME}_REGS->TWI_CR = TWI_CR_STOP_Msk;
                        ${TWI_INSTANCE_NAME}_REGS->TWI_IDR = TWI_IDR_TXRDY_Msk;

                        /* Check TXCOMP to confirm if STOP condition has been sent, otherwise wait for TXCOMP interrupt */
                        status = ${TWI_INSTANCE_NAME}_REGS->TWI_SR;
                        if( (status & TWI_SR_TXCOMP_Msk) != 0U )
                        {
                            ${TWI_INSTANCE_NAME?lower_case}Obj.state = TWI_STATE_TRANSFER_DONE;
                        }
                        else
                        {
                            ${TWI_INSTANCE_NAME?lower_case}Obj.state = TWI_STATE_WAIT_FOR_TXCOMP;
                        }
                    }
                    // Write next byte
                    else
                    {
                        ${TWI_INSTANCE_NAME}_REGS->TWI_THR = TWI_THR_TXDATA((uint32_t)${TWI_INSTANCE_NAME?lower_case}Obj.writeBuffer[${TWI_INSTANCE_NAME?lower_case}Obj.writeCount]);
                        ${TWI_INSTANCE_NAME?lower_case}Obj.writeCount++;
                    }

                    // Dummy read to ensure that TXRDY bit is cleared
                    status = ${TWI_INSTANCE_NAME}_REGS->TWI_SR;
                    (void)status;
                }

                break;
            }

            case TWI_STATE_TRANSFER_READ:
            {
                /* checks if master has received the data */
                if( (status & TWI_SR_RXRDY_Msk) != 0U )
                {
                    // Set the STOP (or START) bit before reading the TWI_RHR on the next-to-last access
                    if(  ${TWI_INSTANCE_NAME?lower_case}Obj.readCount == (${TWI_INSTANCE_NAME?lower_case}Obj.readSize - 2U) )
                    {
                        ${TWI_INSTANCE_NAME}_REGS->TWI_CR = TWI_CR_STOP_Msk;
                    }

                    /* read the received data */
                    ${TWI_INSTANCE_NAME?lower_case}Obj.readBuffer[${TWI_INSTANCE_NAME?lower_case}Obj.readCount] = (uint8_t)(${TWI_INSTANCE_NAME}_REGS->TWI_RHR & TWI_RHR_RXDATA_Msk);
                    ${TWI_INSTANCE_NAME?lower_case}Obj.readCount++;

                    /* checks if transmission has reached at the end */
                    if( ${TWI_INSTANCE_NAME?lower_case}Obj.readCount == ${TWI_INSTANCE_NAME?lower_case}Obj.readSize )
                    {
                        /* Disable the RXRDY interrupt*/
                        ${TWI_INSTANCE_NAME}_REGS->TWI_IDR = TWI_IDR_RXRDY_Msk;

                        /* Check TXCOMP to confirm if STOP condition has been sent, otherwise wait for TXCOMP interrupt */
                        status = ${TWI_INSTANCE_NAME}_REGS->TWI_SR;
                        if( (status & TWI_SR_TXCOMP_Msk) != 0U )
                        {
                            ${TWI_INSTANCE_NAME?lower_case}Obj.state = TWI_STATE_TRANSFER_DONE;
                        }
                        else
                        {
                            ${TWI_INSTANCE_NAME?lower_case}Obj.state = TWI_STATE_WAIT_FOR_TXCOMP;
                        }
                    }
                }
                break;
            }

            case TWI_STATE_WAIT_FOR_TXCOMP:
            {
                if( (status & TWI_SR_TXCOMP_Msk) != 0U )
                {
                    ${TWI_INSTANCE_NAME?lower_case}Obj.state = TWI_STATE_TRANSFER_DONE;
                }
                break;
            }

            default:
            {
                /*default*/
                break;
            }
        }
    }
    if (${TWI_INSTANCE_NAME?lower_case}Obj.state == TWI_STATE_ERROR)
    {
        // NACK is received,
        ${TWI_INSTANCE_NAME?lower_case}Obj.state = TWI_STATE_IDLE;
        ${TWI_INSTANCE_NAME}_REGS->TWI_IDR = TWI_IDR_TXCOMP_Msk | TWI_IDR_TXRDY_Msk | TWI_IDR_RXRDY_Msk;

        // Disable and Enable I2C Master
        ${TWI_INSTANCE_NAME}_REGS->TWI_CR = TWI_CR_MSDIS_Msk;
        ${TWI_INSTANCE_NAME}_REGS->TWI_CR = TWI_CR_MSEN_Msk;

        if ( ${TWI_INSTANCE_NAME?lower_case}Obj.callback != NULL )
        {
            ${TWI_INSTANCE_NAME?lower_case}Obj.callback( ${TWI_INSTANCE_NAME?lower_case}Obj.context );
        }
    }
    // check for completion of transfer
    if( ${TWI_INSTANCE_NAME?lower_case}Obj.state == TWI_STATE_TRANSFER_DONE )
    {

        ${TWI_INSTANCE_NAME?lower_case}Obj.error = TWI_ERROR_NONE;

        // Reset the PLib objects and Interrupts
        ${TWI_INSTANCE_NAME?lower_case}Obj.state = TWI_STATE_IDLE;
        ${TWI_INSTANCE_NAME}_REGS->TWI_IDR = TWI_IDR_TXCOMP_Msk |
                                 TWI_IDR_TXRDY_Msk  |
                                 TWI_IDR_RXRDY_Msk;

        // Disable and Enable I2C Master
        ${TWI_INSTANCE_NAME}_REGS->TWI_CR = TWI_CR_MSDIS_Msk;
        ${TWI_INSTANCE_NAME}_REGS->TWI_CR = TWI_CR_MSEN_Msk;

        if ( ${TWI_INSTANCE_NAME?lower_case}Obj.callback != NULL )
        {
            ${TWI_INSTANCE_NAME?lower_case}Obj.callback( ${TWI_INSTANCE_NAME?lower_case}Obj.context );
        }
    }

    return;
}
