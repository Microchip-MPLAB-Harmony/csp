/*******************************************************************************
  TWIHS Peripheral Library Source File

  Company
    Microchip Technology Inc.

  File Name
    plib_${TWIHS_INSTANCE_NAME?lower_case}_master.c

  Summary
    TWIHS Master peripheral library interface.

  Description

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
#include "plib_${TWIHS_INSTANCE_NAME?lower_case}_master.h"

// *****************************************************************************
// *****************************************************************************
// Global Data
// *****************************************************************************
// *****************************************************************************

static TWIHS_OBJ ${TWIHS_INSTANCE_NAME?lower_case}Obj;

// *****************************************************************************
// *****************************************************************************
// ${TWIHS_INSTANCE_NAME} PLib Interface Routines
// *****************************************************************************
// *****************************************************************************

void ${TWIHS_INSTANCE_NAME}_Initialize( void )
{
    // Reset the i2c Module
    ${TWIHS_INSTANCE_NAME}_REGS->TWIHS_CR = TWIHS_CR_SWRST_Msk;

    // Disable the I2C Master/Slave Mode
    ${TWIHS_INSTANCE_NAME}_REGS->TWIHS_CR = TWIHS_CR_MSDIS_Msk | TWIHS_CR_SVDIS_Msk;

    // Set Baud rate
    <@compress single_line=true>${TWIHS_INSTANCE_NAME}_REGS->TWIHS_CWGR = (TWIHS_CWGR_HOLD_Msk & ${TWIHS_INSTANCE_NAME}_REGS->TWIHS_CWGR)
                                                                          | TWIHS_CWGR_CLDIV(${TWIHS_CWGR_CLDIV})
                                                                          | TWIHS_CWGR_CHDIV(${TWIHS_CWGR_CHDIV})
                                                                          | TWIHS_CWGR_CKDIV(${TWIHS_CWGR_CKDIV})
                                                                          <#if TWIHS_CLK_SRC??>| TWIHS_CWGR_CKSRC_${TWIHS_CLK_SRC}</#if></@compress>;

<#if TWIHS_CR_THRCLR>
    // Starts the transfer by clearing the transmit hold register
    ${TWIHS_INSTANCE_NAME}_REGS->TWIHS_CR = TWIHS_CR_THRCLR_Msk;

</#if>
    // Enables interrupt on nack and arbitration lost
    ${TWIHS_INSTANCE_NAME}_REGS->TWIHS_IER = TWIHS_IER_NACK_Msk | TWIHS_IER_ARBLST_Msk;

    // Enable Master Mode
    ${TWIHS_INSTANCE_NAME}_REGS->TWIHS_CR = TWIHS_CR_MSEN_Msk;

    // Initialize the twihs PLib Object
    ${TWIHS_INSTANCE_NAME?lower_case}Obj.error = TWIHS_ERROR_NONE;
    ${TWIHS_INSTANCE_NAME?lower_case}Obj.state = TWIHS_STATE_IDLE;
}

static void ${TWIHS_INSTANCE_NAME}_InitiateRead( void )
{
    ${TWIHS_INSTANCE_NAME?lower_case}Obj.state = TWIHS_STATE_TRANSFER_READ;

    ${TWIHS_INSTANCE_NAME}_REGS->TWIHS_MMR |= TWIHS_MMR_MREAD_Msk;

    /* When a single data byte read is performed,
     * the START and STOP bits must be set at the same time
     */
    if(${TWIHS_INSTANCE_NAME?lower_case}Obj.readSize == 1)
    {
        ${TWIHS_INSTANCE_NAME}_REGS->TWIHS_CR = TWIHS_CR_START_Msk | TWIHS_CR_STOP_Msk;
    }
    else
    {
        ${TWIHS_INSTANCE_NAME}_REGS->TWIHS_CR = TWIHS_CR_START_Msk;
    }

    __enable_irq();

    ${TWIHS_INSTANCE_NAME}_REGS->TWIHS_IER = TWIHS_IER_RXRDY_Msk | TWIHS_IER_TXCOMP_Msk;
}

static void ${TWIHS_INSTANCE_NAME}_InitiateTransfer( uint16_t address, bool type )
{
    // 10-bit Slave Address
    if( address > 0x007F )
    {
        ${TWIHS_INSTANCE_NAME}_REGS->TWIHS_MMR = TWIHS_MMR_DADR((address & 0x00007F00) >> 8) | TWIHS_MMR_IADRSZ(1);

        // Set internal address
        ${TWIHS_INSTANCE_NAME}_REGS->TWIHS_IADR = TWIHS_IADR_IADR(address & 0x000000FF );
    }
    // 7-bit Slave Address
    else
    {
        ${TWIHS_INSTANCE_NAME}_REGS->TWIHS_MMR = TWIHS_MMR_DADR(address) | TWIHS_MMR_IADRSZ(0);
    }

    ${TWIHS_INSTANCE_NAME?lower_case}Obj.writeCount = 0;
    ${TWIHS_INSTANCE_NAME?lower_case}Obj.readCount = 0;

    // Write transfer
    if(type == false)
    {
        // Single Byte Write
        if( ${TWIHS_INSTANCE_NAME?lower_case}Obj.writeSize == 1 )
        {
            // Single Byte write only
            if( ${TWIHS_INSTANCE_NAME?lower_case}Obj.readSize == 0 )
            {
                // Load last byte in transmit register, issue stop condition
                // Generate TXCOMP interrupt after STOP condition has been sent
                ${TWIHS_INSTANCE_NAME?lower_case}Obj.state = TWIHS_STATE_WAIT_FOR_TXCOMP;

                ${TWIHS_INSTANCE_NAME}_REGS->TWIHS_THR = TWIHS_THR_TXDATA(${TWIHS_INSTANCE_NAME?lower_case}Obj.writeBuffer[${TWIHS_INSTANCE_NAME?lower_case}Obj.writeCount++]);
                ${TWIHS_INSTANCE_NAME}_REGS->TWIHS_CR = TWIHS_CR_STOP_Msk;
                ${TWIHS_INSTANCE_NAME}_REGS->TWIHS_IER = TWIHS_IER_TXCOMP_Msk;
            }
            // Single Byte write and than read transfer
            else
            {
                // START bit must be set before the byte is shifted out. Hence disabled interrupt
                __disable_irq();

                ${TWIHS_INSTANCE_NAME}_REGS->TWIHS_THR = TWIHS_THR_TXDATA(${TWIHS_INSTANCE_NAME?lower_case}Obj.writeBuffer[${TWIHS_INSTANCE_NAME?lower_case}Obj.writeCount++]);

                // Wait for control byte to be transferred before initiating repeat start for read
                while((${TWIHS_INSTANCE_NAME}_REGS->TWIHS_SR & (TWIHS_SR_TXCOMP_Msk | TWIHS_SR_TXRDY_Msk)) != 0);

                while((${TWIHS_INSTANCE_NAME}_REGS->TWIHS_SR & (TWIHS_SR_TXRDY_Msk)) == 0);

                type = true;
            }
        }
        // Multi-Byte Write
        else
        {
            ${TWIHS_INSTANCE_NAME?lower_case}Obj.state = TWIHS_STATE_TRANSFER_WRITE;

            ${TWIHS_INSTANCE_NAME}_REGS->TWIHS_THR = TWIHS_THR_TXDATA(${TWIHS_INSTANCE_NAME?lower_case}Obj.writeBuffer[${TWIHS_INSTANCE_NAME?lower_case}Obj.writeCount++]);

            ${TWIHS_INSTANCE_NAME}_REGS->TWIHS_IER = TWIHS_IDR_TXRDY_Msk | TWIHS_IER_TXCOMP_Msk;
        }
    }
    // Read transfer
    if(type)
    {
        ${TWIHS_INSTANCE_NAME}_InitiateRead();
    }
}

void ${TWIHS_INSTANCE_NAME}_CallbackRegister( TWIHS_CALLBACK callback, uintptr_t contextHandle )
{
    if (callback != NULL)
    {
        ${TWIHS_INSTANCE_NAME?lower_case}Obj.callback = callback;

        ${TWIHS_INSTANCE_NAME?lower_case}Obj.context = contextHandle;
    }
}

bool ${TWIHS_INSTANCE_NAME}_IsBusy( void )
{
    // Check for ongoing transfer
    if( ${TWIHS_INSTANCE_NAME?lower_case}Obj.state == TWIHS_STATE_IDLE )
    {
        return false;
    }
    else
    {
        return true;
    }
}

bool ${TWIHS_INSTANCE_NAME}_Read( uint16_t address, uint8_t *pdata, size_t length )
{
    // Check for ongoing transfer
    if( ${TWIHS_INSTANCE_NAME?lower_case}Obj.state != TWIHS_STATE_IDLE )
    {
        return false;
    }

    ${TWIHS_INSTANCE_NAME?lower_case}Obj.address = address;
    ${TWIHS_INSTANCE_NAME?lower_case}Obj.readBuffer = pdata;
    ${TWIHS_INSTANCE_NAME?lower_case}Obj.readSize = length;
    ${TWIHS_INSTANCE_NAME?lower_case}Obj.writeBuffer = NULL;
    ${TWIHS_INSTANCE_NAME?lower_case}Obj.writeSize = 0;
    ${TWIHS_INSTANCE_NAME?lower_case}Obj.error = TWIHS_ERROR_NONE;

    ${TWIHS_INSTANCE_NAME}_InitiateTransfer(address, true);

    return true;
}

bool ${TWIHS_INSTANCE_NAME}_Write( uint16_t address, uint8_t *pdata, size_t length )
{
    // Check for ongoing transfer
    if( ${TWIHS_INSTANCE_NAME?lower_case}Obj.state != TWIHS_STATE_IDLE )
    {
        return false;
    }

    ${TWIHS_INSTANCE_NAME?lower_case}Obj.address = address;
    ${TWIHS_INSTANCE_NAME?lower_case}Obj.readBuffer = NULL;
    ${TWIHS_INSTANCE_NAME?lower_case}Obj.readSize = 0;
    ${TWIHS_INSTANCE_NAME?lower_case}Obj.writeBuffer = pdata;
    ${TWIHS_INSTANCE_NAME?lower_case}Obj.writeSize = length;
    ${TWIHS_INSTANCE_NAME?lower_case}Obj.error = TWIHS_ERROR_NONE;

    ${TWIHS_INSTANCE_NAME}_InitiateTransfer(address, false);

    return true;
}

bool ${TWIHS_INSTANCE_NAME}_WriteRead( uint16_t address, uint8_t *wdata, size_t wlength, uint8_t *rdata, size_t rlength )
{

    // Check for ongoing transfer
    if( ${TWIHS_INSTANCE_NAME?lower_case}Obj.state != TWIHS_STATE_IDLE )
    {
        return false;
    }

    ${TWIHS_INSTANCE_NAME?lower_case}Obj.address = address;
    ${TWIHS_INSTANCE_NAME?lower_case}Obj.readBuffer = rdata;
    ${TWIHS_INSTANCE_NAME?lower_case}Obj.readSize = rlength;
    ${TWIHS_INSTANCE_NAME?lower_case}Obj.writeBuffer = wdata;
    ${TWIHS_INSTANCE_NAME?lower_case}Obj.writeSize = wlength;
    ${TWIHS_INSTANCE_NAME?lower_case}Obj.error = TWIHS_ERROR_NONE;

    ${TWIHS_INSTANCE_NAME}_InitiateTransfer(address, false);

    return true;
}

TWIHS_ERROR ${TWIHS_INSTANCE_NAME}_ErrorGet( void )
{
    TWIHS_ERROR error = TWIHS_ERROR_NONE;

    error = ${TWIHS_INSTANCE_NAME?lower_case}Obj.error;

    ${TWIHS_INSTANCE_NAME?lower_case}Obj.error = TWIHS_ERROR_NONE;

    return error;
}

bool ${TWIHS_INSTANCE_NAME}_TransferSetup( TWIHS_TRANSFER_SETUP* setup, uint32_t srcClkFreq )
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

    if(srcClkFreq == 0)
    {
        srcClkFreq = ${TWIHS_CLK_SRC_FREQ};
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

    /* set clock waveform generator register */
    <@compress single_line=true>${TWIHS_INSTANCE_NAME}_REGS->TWIHS_CWGR = (TWIHS_CWGR_HOLD_Msk & ${TWIHS_INSTANCE_NAME}_REGS->TWIHS_CWGR)
                                                                          | TWIHS_CWGR_CLDIV(cldiv)
                                                                          | TWIHS_CWGR_CHDIV(cldiv)
                                                                          | TWIHS_CWGR_CKDIV(ckdiv)</@compress>;

    return true;
}

void ${TWIHS_INSTANCE_NAME}_InterruptHandler( void )
{
    uint32_t status;

    // Read the peripheral status
    status = ${TWIHS_INSTANCE_NAME}_REGS->TWIHS_SR;

    /* checks if Slave has Nacked */
    if( status & TWIHS_SR_NACK_Msk )
    {
        ${TWIHS_INSTANCE_NAME?lower_case}Obj.state = TWIHS_STATE_ERROR;
        ${TWIHS_INSTANCE_NAME?lower_case}Obj.error = TWIHS_ERROR_NACK;
    }

    if( status & TWIHS_SR_TXCOMP_Msk )
    {
        /* Disable and Enable I2C Master */
        ${TWIHS_INSTANCE_NAME}_REGS->TWIHS_CR = TWIHS_CR_MSDIS_Msk;
        ${TWIHS_INSTANCE_NAME}_REGS->TWIHS_CR = TWIHS_CR_MSEN_Msk;

        /* Disable Interrupt */
        ${TWIHS_INSTANCE_NAME}_REGS->TWIHS_IDR = TWIHS_IDR_TXCOMP_Msk | TWIHS_IDR_TXRDY_Msk | TWIHS_IDR_RXRDY_Msk;
    }

    /* checks if the arbitration is lost in multi-master scenario */
    if( status & TWIHS_SR_ARBLST_Msk )
    {
        /* Re-initiate the transfer if arbitration is lost in
         * between of the transfer
         */
        ${TWIHS_INSTANCE_NAME?lower_case}Obj.state = TWIHS_STATE_ADDR_SEND;
    }

    if( ${TWIHS_INSTANCE_NAME?lower_case}Obj.error == TWIHS_ERROR_NONE)
    {
        switch( ${TWIHS_INSTANCE_NAME?lower_case}Obj.state )
        {
            case TWIHS_STATE_ADDR_SEND:
            {
                if (${TWIHS_INSTANCE_NAME?lower_case}Obj.writeSize != 0 )
                {
                    // Initiate Write transfer
                    ${TWIHS_INSTANCE_NAME}_InitiateTransfer(${TWIHS_INSTANCE_NAME?lower_case}Obj.address, false);
                }
                else
                {
                    // Initiate Read transfer
                    ${TWIHS_INSTANCE_NAME}_InitiateTransfer(${TWIHS_INSTANCE_NAME?lower_case}Obj.address, true);
                }
            }
            break;

            case TWIHS_STATE_TRANSFER_WRITE:
            {
                /* checks if master is ready to transmit */
                if( status & TWIHS_SR_TXRDY_Msk )
                {
                    // Write Last Byte and then initiate read transfer
                    if( ( ${TWIHS_INSTANCE_NAME?lower_case}Obj.writeCount == (${TWIHS_INSTANCE_NAME?lower_case}Obj.writeSize -1) ) && ( ${TWIHS_INSTANCE_NAME?lower_case}Obj.readSize != 0 ))
                    {
                        // START bit must be set before the last byte is shifted out to generate repeat start. Hence disabled interrupt
                        __disable_irq();
                        ${TWIHS_INSTANCE_NAME}_REGS->TWIHS_IDR = TWIHS_IDR_TXRDY_Msk;
                        ${TWIHS_INSTANCE_NAME}_REGS->TWIHS_THR = TWIHS_THR_TXDATA(${TWIHS_INSTANCE_NAME?lower_case}Obj.writeBuffer[${TWIHS_INSTANCE_NAME?lower_case}Obj.writeCount++]);
                        ${TWIHS_INSTANCE_NAME}_InitiateRead();
                    }
                    // Write Last byte and then issue STOP condition
                    else if ( ${TWIHS_INSTANCE_NAME?lower_case}Obj.writeCount == (${TWIHS_INSTANCE_NAME?lower_case}Obj.writeSize -1))
                    {
                        // Load last byte in transmit register, issue stop condition
                        // Generate TXCOMP interrupt after STOP condition has been sent
                        ${TWIHS_INSTANCE_NAME}_REGS->TWIHS_THR = TWIHS_THR_TXDATA(${TWIHS_INSTANCE_NAME?lower_case}Obj.writeBuffer[${TWIHS_INSTANCE_NAME?lower_case}Obj.writeCount++]);
                        ${TWIHS_INSTANCE_NAME}_REGS->TWIHS_CR = TWIHS_CR_STOP_Msk;
                        ${TWIHS_INSTANCE_NAME}_REGS->TWIHS_IDR = TWIHS_IDR_TXRDY_Msk;

                        /* Check TXCOMP to confirm if STOP condition has been sent, otherwise wait for TXCOMP interrupt */
                        status = ${TWIHS_INSTANCE_NAME}_REGS->TWIHS_SR;

                        if( status & TWIHS_SR_TXCOMP_Msk )
                        {
                            ${TWIHS_INSTANCE_NAME?lower_case}Obj.state = TWIHS_STATE_TRANSFER_DONE;
                        }
                        else
                        {
                            ${TWIHS_INSTANCE_NAME?lower_case}Obj.state = TWIHS_STATE_WAIT_FOR_TXCOMP;
                        }
                    }
                    // Write next byte
                    else
                    {
                        ${TWIHS_INSTANCE_NAME}_REGS->TWIHS_THR = TWIHS_THR_TXDATA(${TWIHS_INSTANCE_NAME?lower_case}Obj.writeBuffer[${TWIHS_INSTANCE_NAME?lower_case}Obj.writeCount++]);
                    }

                    // Dummy read to ensure that TXRDY bit is cleared
                    status = ${TWIHS_INSTANCE_NAME}_REGS->TWIHS_SR;
                }

                break;
            }

            case TWIHS_STATE_TRANSFER_READ:
            {
                /* checks if master has received the data */
                if( status & TWIHS_SR_RXRDY_Msk )
                {
                    // Set the STOP (or START) bit before reading the TWIHS_RHR on the next-to-last access
                    if(  ${TWIHS_INSTANCE_NAME?lower_case}Obj.readCount == (${TWIHS_INSTANCE_NAME?lower_case}Obj.readSize - 2) )
                    {
                        ${TWIHS_INSTANCE_NAME}_REGS->TWIHS_CR = TWIHS_CR_STOP_Msk;
                    }

                    /* read the received data */
                    ${TWIHS_INSTANCE_NAME?lower_case}Obj.readBuffer[${TWIHS_INSTANCE_NAME?lower_case}Obj.readCount++] = (uint8_t)(${TWIHS_INSTANCE_NAME}_REGS->TWIHS_RHR & TWIHS_RHR_RXDATA_Msk);

                    /* checks if transmission has reached at the end */
                    if( ${TWIHS_INSTANCE_NAME?lower_case}Obj.readCount == ${TWIHS_INSTANCE_NAME?lower_case}Obj.readSize )
                    {
                        /* Disable the RXRDY interrupt*/
                        ${TWIHS_INSTANCE_NAME}_REGS->TWIHS_IDR = TWIHS_IDR_RXRDY_Msk;

                        /* Check TXCOMP to confirm if STOP condition has been sent, otherwise wait for TXCOMP interrupt */
                        status = ${TWIHS_INSTANCE_NAME}_REGS->TWIHS_SR;
                        if( status & TWIHS_SR_TXCOMP_Msk )
                        {
                            ${TWIHS_INSTANCE_NAME?lower_case}Obj.state = TWIHS_STATE_TRANSFER_DONE;
                        }
                        else
                        {
                            ${TWIHS_INSTANCE_NAME?lower_case}Obj.state = TWIHS_STATE_WAIT_FOR_TXCOMP;
                        }
                    }
                }
                break;
            }

            case TWIHS_STATE_WAIT_FOR_TXCOMP:
            {
                if( status & TWIHS_SR_TXCOMP_Msk )
                {
                    ${TWIHS_INSTANCE_NAME?lower_case}Obj.state = TWIHS_STATE_TRANSFER_DONE;
                }
                break;
            }

            default:
            {
                break;
            }
        }
    }
    if (${TWIHS_INSTANCE_NAME?lower_case}Obj.state == TWIHS_STATE_ERROR)
    {
        // NACK is received,
        ${TWIHS_INSTANCE_NAME?lower_case}Obj.state = TWIHS_STATE_IDLE;
        ${TWIHS_INSTANCE_NAME}_REGS->TWIHS_IDR = TWIHS_IDR_TXCOMP_Msk | TWIHS_IDR_TXRDY_Msk | TWIHS_IDR_RXRDY_Msk;

        // Disable and Enable I2C Master
        ${TWIHS_INSTANCE_NAME}_REGS->TWIHS_CR = TWIHS_CR_MSDIS_Msk;
        ${TWIHS_INSTANCE_NAME}_REGS->TWIHS_CR = TWIHS_CR_MSEN_Msk;

        if ( ${TWIHS_INSTANCE_NAME?lower_case}Obj.callback != NULL )
        {
            ${TWIHS_INSTANCE_NAME?lower_case}Obj.callback( ${TWIHS_INSTANCE_NAME?lower_case}Obj.context );
        }
    }
    // check for completion of transfer
    if( ${TWIHS_INSTANCE_NAME?lower_case}Obj.state == TWIHS_STATE_TRANSFER_DONE )
    {
        ${TWIHS_INSTANCE_NAME?lower_case}Obj.error = TWIHS_ERROR_NONE;

        // Reset the PLib objects and Interrupts
        ${TWIHS_INSTANCE_NAME?lower_case}Obj.state = TWIHS_STATE_IDLE;
        ${TWIHS_INSTANCE_NAME}_REGS->TWIHS_IDR = TWIHS_IDR_TXCOMP_Msk | TWIHS_IDR_TXRDY_Msk | TWIHS_IDR_RXRDY_Msk;

        // Disable and Enable I2C Master
        ${TWIHS_INSTANCE_NAME}_REGS->TWIHS_CR = TWIHS_CR_MSDIS_Msk;
        ${TWIHS_INSTANCE_NAME}_REGS->TWIHS_CR = TWIHS_CR_MSEN_Msk;

        if ( ${TWIHS_INSTANCE_NAME?lower_case}Obj.callback != NULL )
        {
            ${TWIHS_INSTANCE_NAME?lower_case}Obj.callback( ${TWIHS_INSTANCE_NAME?lower_case}Obj.context );
        }
    }

    return;
}