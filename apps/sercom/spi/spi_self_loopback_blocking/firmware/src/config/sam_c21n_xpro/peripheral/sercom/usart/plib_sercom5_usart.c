/*******************************************************************************
  SERCOM Universal Synchronous/Asynchrnous Receiver/Transmitter PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_sercom5_usart.c

  Summary
    USART peripheral library interface.

  Description
    This file defines the interface to the USART peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

  Remarks:
    None.
*******************************************************************************/

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

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
/* This section lists the other files that are included in this file.
*/

#include "plib_sercom5_usart.h"

// *****************************************************************************
// *****************************************************************************
// Section: Global Data
// *****************************************************************************
// *****************************************************************************

SERCOM_USART_OBJECT sercom5USARTObj;

// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************
/* The following functions make up the methods (set of possible operations) of
this interface.
*/

void SERCOM5_USART_Initialize( void )
{
    /* Reset USART */
    SERCOM5_REGS->USART.CTRLA = SERCOM_USART_CTRLA_SWRST_Msk;

    /* Wait for sync */
    while(SERCOM5_REGS->USART.SYNCBUSY);

    /*
     * Configures USART Clock Mode
     * Configures TXPO and RXPO
     * Configures Data Order
     * Configures Standby Mode
     * Configures sampling rate
     * Configures IBON
     * Configures Parity
     * Configures Stop bits
     */
    SERCOM5_REGS->USART.CTRLA = SERCOM_USART_CTRLA_MODE(0x1) | SERCOM_USART_CTRLA_RXPO(0x0) | SERCOM_USART_CTRLA_TXPO(0x0) | SERCOM_USART_CTRLA_DORD_Msk | SERCOM_USART_CTRLA_SAMPR(0) | SERCOM_USART_CTRLA_IBON_Msk | SERCOM_USART_CTRLA_FORM(0x0) ;

    /* Configure Baud Rate */
    SERCOM5_REGS->USART.BAUD = SERCOM_USART_BAUD_BAUD(35337);

    /*
     * Configures RXEN
     * Configures TXEN
     * Configures CHSIZE
     * Configures Parity
     * Configures Stop bits
     */
    SERCOM5_REGS->USART.CTRLB = SERCOM_USART_CTRLB_CHSIZE(0x0) | SERCOM_USART_CTRLB_RXEN_Msk | SERCOM_USART_CTRLB_TXEN_Msk;

    /* Wait for sync */
    while(SERCOM5_REGS->USART.SYNCBUSY);

    /* Enable the UART after the configurations */
    SERCOM5_REGS->USART.CTRLA |= SERCOM_USART_CTRLA_ENABLE_Msk;

    /* Wait for sync */
    while(SERCOM5_REGS->USART.SYNCBUSY);

    /* Initialize instance object */
    sercom5USARTObj.rxBuffer = NULL;
    sercom5USARTObj.rxSize = 0;
    sercom5USARTObj.rxProcessedSize = 0;
    sercom5USARTObj.rxBusyStatus = false;
    sercom5USARTObj.rxCallback = NULL;
    sercom5USARTObj.txBuffer = NULL;
    sercom5USARTObj.txSize = 0;
    sercom5USARTObj.txProcessedSize = 0;
    sercom5USARTObj.txBusyStatus = false;
    sercom5USARTObj.txCallback = NULL;
}

bool SERCOM5_USART_SerialSetup( USART_SERIAL_SETUP * serialSetup, uint32_t clkFrequency )
{
    bool setupStatus       = false;
    uint32_t sampleRate    = 0;
    uint32_t baudValue     = 0;

    if((sercom5USARTObj.rxBusyStatus == true) || (sercom5USARTObj.txBusyStatus == true))
    {
        /* Transaction is in progress, so return without updating settings */
        return setupStatus;
    }

    if((serialSetup != NULL) & (serialSetup->baudRate != 0))
    {
        if(clkFrequency == 0)
        {
            clkFrequency = SERCOM5_USART_FrequencyGet();
        }

        if(clkFrequency >= (16 * serialSetup->baudRate))
        {
            baudValue = 65536 - ((uint64_t)65536 * 16 * serialSetup->baudRate) / clkFrequency;
            sampleRate = 0;
        }
        else if(clkFrequency >= (8 * serialSetup->baudRate))
        {
            baudValue = 65536 - ((uint64_t)65536 * 8 * serialSetup->baudRate) / clkFrequency;
            sampleRate = 2;
        }
        else if(clkFrequency >= (3 * serialSetup->baudRate))
        {
            baudValue = 65536 - ((uint64_t)65536 * 3 * serialSetup->baudRate) / clkFrequency;
            sampleRate = 4;
        }

        if(baudValue != 0)
        {
            /* Disable the USART before configurations */
            SERCOM5_REGS->USART.CTRLA &= ~SERCOM_USART_CTRLA_ENABLE_Msk;

            /* Wait for sync */
            while(SERCOM5_REGS->USART.SYNCBUSY);

            /* Configure Baud Rate */
            SERCOM5_REGS->USART.BAUD = SERCOM_USART_BAUD_BAUD(baudValue);

            /* Configure Parity Options */
            if(serialSetup->parity == USART_PARITY_NONE)
            {
                SERCOM5_REGS->USART.CTRLA |= SERCOM_USART_CTRLA_SAMPR(sampleRate) | SERCOM_USART_CTRLA_FORM(0x0);

                SERCOM5_REGS->USART.CTRLB |= serialSetup->dataWidth | serialSetup->stopBits;
            }
            else
            {
                SERCOM5_REGS->USART.CTRLA |= SERCOM_USART_CTRLA_SAMPR(sampleRate) | SERCOM_USART_CTRLA_FORM(0x1);

                SERCOM5_REGS->USART.CTRLB |= serialSetup->dataWidth | serialSetup->parity | serialSetup->stopBits;
            }

            /* Wait for sync */
            while(SERCOM5_REGS->USART.SYNCBUSY);

            /* Enable the USART after the configurations */
            SERCOM5_REGS->USART.CTRLA |= SERCOM_USART_CTRLA_ENABLE_Msk;

            /* Wait for sync */
            while(SERCOM5_REGS->USART.SYNCBUSY);

            setupStatus = true;
        }
    }

    return setupStatus;
}

bool SERCOM5_USART_Write( void *buffer, const size_t size )
{
    bool writeStatus      = false;
    uint8_t *pu8Data      = (uint8_t*)buffer;

    if(pu8Data != NULL)
    {
        if(sercom5USARTObj.txBusyStatus == false)
        {
            sercom5USARTObj.txBuffer = pu8Data;
            sercom5USARTObj.txSize = size;
            sercom5USARTObj.txProcessedSize = 0;
            sercom5USARTObj.txBusyStatus = true;

            if(size == 0)
            {
                writeStatus = true;
            }
            else
            {
                /* Initiate the transfer by sending first byte */
                if((SERCOM5_REGS->USART.INTFLAG & SERCOM_USART_INTFLAG_DRE_Msk) == SERCOM_USART_INTFLAG_DRE_Msk)
                {
                    SERCOM5_REGS->USART.DATA = sercom5USARTObj.txBuffer[sercom5USARTObj.txProcessedSize++];
                }

                SERCOM5_REGS->USART.INTENSET = SERCOM_USART_INTFLAG_DRE_Msk;

                writeStatus = true;
            }
        }
    }

    return writeStatus;
}

bool SERCOM5_USART_WriteIsBusy ( void )
{
    return sercom5USARTObj.txBusyStatus;
}

size_t SERCOM5_USART_WriteCountGet( void )
{
    return sercom5USARTObj.txProcessedSize;
}

void SERCOM5_USART_WriteCallbackRegister( SERCOM_USART_CALLBACK callback, uintptr_t context )
{
    sercom5USARTObj.txCallback = callback;

    sercom5USARTObj.txContext = context;
}

bool SERCOM5_USART_Read( void *buffer, const size_t size )
{
    bool readStatus        = false;
    uint8_t *pu8Data       = (uint8_t*)buffer;
    uint8_t u8dummyData    = 0;

    if(pu8Data != NULL)
    {
        if(sercom5USARTObj.rxBusyStatus == false)
        {
            /* Checks for error before receiving */
            if(SERCOM5_USART_ErrorGet() != USART_ERROR_NONE)
            {
                /* Clear all error flags */
                SERCOM5_REGS->USART.INTFLAG = SERCOM_USART_INTFLAG_ERROR_Msk;

                /* Clear error statuses */
                SERCOM5_REGS->USART.STATUS = SERCOM_USART_STATUS_Msk;

                /* Flush existing error bytes from the RX FIFO */
                while((SERCOM5_REGS->USART.INTFLAG & SERCOM_USART_INTFLAG_RXC_Msk) == SERCOM_USART_INTFLAG_RXC_Msk)
                {
                    u8dummyData = SERCOM5_REGS->USART.DATA;
                }

                /* Ignore the warning */
                (void)u8dummyData;
            }

            sercom5USARTObj.rxBuffer = pu8Data;
            sercom5USARTObj.rxSize = size;
            sercom5USARTObj.rxProcessedSize = 0;
            sercom5USARTObj.rxBusyStatus = true;
            readStatus = true;

            /* Enable error interrupts */
            SERCOM5_REGS->USART.INTENSET |= SERCOM_USART_INTENSET_ERROR_Msk;

            /* Enable Receive Complete interrupt */
            SERCOM5_REGS->USART.INTENSET = SERCOM_USART_INTENSET_RXC_Msk;
        }
    }

    return readStatus;
}

bool SERCOM5_USART_ReadIsBusy( void )
{
    return sercom5USARTObj.rxBusyStatus;
}

size_t SERCOM5_USART_ReadCountGet( void )
{
    return sercom5USARTObj.rxProcessedSize;
}

void SERCOM5_USART_ReadCallbackRegister( SERCOM_USART_CALLBACK callback, uintptr_t context )
{
    sercom5USARTObj.rxCallback = callback;

    sercom5USARTObj.rxContext = context;
}

USART_ERROR SERCOM5_USART_ErrorGet( void )
{
    USART_ERROR errorStatus = USART_ERROR_NONE;

    errorStatus = SERCOM5_REGS->USART.STATUS & (SERCOM_USART_STATUS_PERR_Msk | SERCOM_USART_STATUS_FERR_Msk | SERCOM_USART_STATUS_BUFOVF_Msk);

    /* Clear Errors */
    SERCOM5_REGS->USART.STATUS = SERCOM_USART_STATUS_PERR_Msk | SERCOM_USART_STATUS_FERR_Msk | SERCOM_USART_STATUS_BUFOVF_Msk;

    return errorStatus;
}

void static SERCOM5_USART_ISR_ERR_Handler( void )
{
    USART_ERROR errorStatus = USART_ERROR_NONE;
    uint8_t  u8dummyData = 0;

    errorStatus = (SERCOM5_REGS->USART.STATUS &
                  (SERCOM_USART_STATUS_PERR_Msk |
                  SERCOM_USART_STATUS_FERR_Msk |
                  SERCOM_USART_STATUS_BUFOVF_Msk));

    if(errorStatus != USART_ERROR_NONE)
    {
        /* Clear all error flags */
        SERCOM5_REGS->USART.INTFLAG = SERCOM_USART_INTFLAG_ERROR_Msk;

        /* Clear error statuses */
        SERCOM5_REGS->USART.STATUS = SERCOM_USART_STATUS_Msk;

        /* Flush existing error bytes from the RX FIFO */
        while((SERCOM5_REGS->USART.INTFLAG & SERCOM_USART_INTFLAG_RXC_Msk) == SERCOM_USART_INTFLAG_RXC_Msk)
        {
            u8dummyData = SERCOM5_REGS->USART.DATA;
        }

        /* Ignore the warning */
        (void)u8dummyData;

        if(sercom5USARTObj.rxCallback != NULL)
        {
            sercom5USARTObj.rxCallback(sercom5USARTObj.rxContext);
        }
    }
}

void static SERCOM5_USART_ISR_RX_Handler( void )
{
    if(sercom5USARTObj.rxBusyStatus == true)
    {
        if(sercom5USARTObj.rxSize >= sercom5USARTObj.rxProcessedSize)
        {
            if(sercom5USARTObj.rxSize == sercom5USARTObj.rxProcessedSize)
            {
                sercom5USARTObj.rxBusyStatus = false;
                sercom5USARTObj.rxSize = 0;
                SERCOM5_REGS->USART.INTENCLR = SERCOM_USART_INTENCLR_RXC_Msk;

                if(sercom5USARTObj.rxCallback != NULL)
                {
                    sercom5USARTObj.rxCallback(sercom5USARTObj.rxContext);
                }
            }
            else
            {
                sercom5USARTObj.rxBuffer[sercom5USARTObj.rxProcessedSize++] = SERCOM5_REGS->USART.DATA;
            }
        }
    }
}

void static SERCOM5_USART_ISR_TX_Handler( void )
{
    if(sercom5USARTObj.txBusyStatus == true)
    {
        if(sercom5USARTObj.txSize >= sercom5USARTObj.txProcessedSize)
        {
            if(sercom5USARTObj.txSize == sercom5USARTObj.txProcessedSize)
            {
                sercom5USARTObj.txBusyStatus = false;
                sercom5USARTObj.txSize = 0;
                SERCOM5_REGS->USART.INTENCLR = SERCOM_USART_INTENCLR_DRE_Msk;

                if(sercom5USARTObj.txCallback != NULL)
                {
                    sercom5USARTObj.txCallback(sercom5USARTObj.txContext);
                }
            }
            else
            {
                SERCOM5_REGS->USART.DATA = sercom5USARTObj.txBuffer[sercom5USARTObj.txProcessedSize++];
            }
        }
    }
}

void SERCOM5_USART_InterruptHandler( void )
{
    if(SERCOM5_REGS->USART.INTENSET != 0)
    {
        /* Checks for data register empty flag */
        if((SERCOM5_REGS->USART.INTFLAG & SERCOM_USART_INTFLAG_DRE_Msk) == SERCOM_USART_INTFLAG_DRE_Msk)
        {
            SERCOM5_USART_ISR_TX_Handler();
        }

        /* Checks for receive complete empty flag */
        if((SERCOM5_REGS->USART.INTFLAG & SERCOM_USART_INTFLAG_RXC_Msk) == SERCOM_USART_INTFLAG_RXC_Msk)
        {
            SERCOM5_USART_ISR_RX_Handler();
        }

        /* Checks for error flag */
        if((SERCOM5_REGS->USART.INTFLAG & SERCOM_USART_INTFLAG_ERROR_Msk) == SERCOM_USART_INTFLAG_ERROR_Msk)
        {
            SERCOM5_USART_ISR_ERR_Handler();
        }
    }
}
