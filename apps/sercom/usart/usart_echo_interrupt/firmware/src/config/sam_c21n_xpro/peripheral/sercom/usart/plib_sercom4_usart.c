/*******************************************************************************
  SERCOM Universal Synchronous/Asynchrnous Receiver/Transmitter PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_sercom4_usart.c

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

#include "plib_sercom4_usart.h"

// *****************************************************************************
// *****************************************************************************
// Section: Global Data
// *****************************************************************************
// *****************************************************************************

SERCOM_USART_OBJECT sercom4USARTObj;

// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************
/* The following functions make up the methods (set of possible operations) of
this interface.
*/

void SERCOM4_USART_Initialize( void )
{
    /* Reset USART */
    SERCOM4_REGS->USART.CTRLA = SERCOM_USART_CTRLA_SWRST_Msk;

    /* Wait for sync */
    while(SERCOM4_REGS->USART.SYNCBUSY);

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
    SERCOM4_REGS->USART.CTRLA = SERCOM_USART_CTRLA_MODE(0x1) | SERCOM_USART_CTRLA_RXPO(0x3) | SERCOM_USART_CTRLA_TXPO(0x1) | SERCOM_USART_CTRLA_DORD_Msk | SERCOM_USART_CTRLA_SAMPR(0) | SERCOM_USART_CTRLA_IBON_Msk | SERCOM_USART_CTRLA_FORM(0x0) ;

    /* Configure Baud Rate */
    SERCOM4_REGS->USART.BAUD = SERCOM_USART_BAUD_BAUD(63019);

    /*
     * Configures RXEN
     * Configures TXEN
     * Configures CHSIZE
     * Configures Parity
     * Configures Stop bits
     */
    SERCOM4_REGS->USART.CTRLB = SERCOM_USART_CTRLB_CHSIZE(0x0) | SERCOM_USART_CTRLB_RXEN_Msk | SERCOM_USART_CTRLB_TXEN_Msk;

    /* Wait for sync */
    while(SERCOM4_REGS->USART.SYNCBUSY);

    /* Enable the UART after the configurations */
    SERCOM4_REGS->USART.CTRLA |= SERCOM_USART_CTRLA_ENABLE_Msk;

    /* Wait for sync */
    while(SERCOM4_REGS->USART.SYNCBUSY);

    /* Initialize instance object */
    sercom4USARTObj.rxBuffer = NULL;
    sercom4USARTObj.rxSize = 0;
    sercom4USARTObj.rxProcessedSize = 0;
    sercom4USARTObj.rxBusyStatus = false;
    sercom4USARTObj.rxCallback = NULL;
    sercom4USARTObj.txBuffer = NULL;
    sercom4USARTObj.txSize = 0;
    sercom4USARTObj.txProcessedSize = 0;
    sercom4USARTObj.txBusyStatus = false;
    sercom4USARTObj.txCallback = NULL;
}

bool SERCOM4_USART_SerialSetup( USART_SERIAL_SETUP * serialSetup, uint32_t clkFrequency )
{
    bool setupStatus       = false;
    uint32_t sampleRate    = 0;
    uint32_t baudValue     = 0;

    if((sercom4USARTObj.rxBusyStatus == true) || (sercom4USARTObj.txBusyStatus == true))
    {
        /* Transaction is in progress, so return without updating settings */
        return setupStatus;
    }

    if((serialSetup != NULL) & (serialSetup->baudRate != 0))
    {
        if(clkFrequency == 0)
        {
            clkFrequency = SERCOM4_USART_FrequencyGet();
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
            SERCOM4_REGS->USART.CTRLA &= ~SERCOM_USART_CTRLA_ENABLE_Msk;

            /* Wait for sync */
            while(SERCOM4_REGS->USART.SYNCBUSY);

            /* Configure Baud Rate */
            SERCOM4_REGS->USART.BAUD = SERCOM_USART_BAUD_BAUD(baudValue);

            /* Configure Parity Options */
            if(serialSetup->parity == USART_PARITY_NONE)
            {
                SERCOM4_REGS->USART.CTRLA |= SERCOM_USART_CTRLA_SAMPR(sampleRate) | SERCOM_USART_CTRLA_FORM(0x0);

                SERCOM4_REGS->USART.CTRLB |= serialSetup->dataWidth | serialSetup->stopBits;
            }
            else
            {
                SERCOM4_REGS->USART.CTRLA |= SERCOM_USART_CTRLA_SAMPR(sampleRate) | SERCOM_USART_CTRLA_FORM(0x1);

                SERCOM4_REGS->USART.CTRLB |= serialSetup->dataWidth | serialSetup->parity | serialSetup->stopBits;
            }

            /* Wait for sync */
            while(SERCOM4_REGS->USART.SYNCBUSY);

            /* Enable the USART after the configurations */
            SERCOM4_REGS->USART.CTRLA |= SERCOM_USART_CTRLA_ENABLE_Msk;

            /* Wait for sync */
            while(SERCOM4_REGS->USART.SYNCBUSY);

            setupStatus = true;
        }
    }

    return setupStatus;
}

bool SERCOM4_USART_Write( void *buffer, const size_t size )
{
    bool writeStatus      = false;
    uint8_t *pu8Data      = (uint8_t*)buffer;

    if(pu8Data != NULL)
    {
        if(sercom4USARTObj.txBusyStatus == false)
        {
            sercom4USARTObj.txBuffer = pu8Data;
            sercom4USARTObj.txSize = size;
            sercom4USARTObj.txProcessedSize = 0;
            sercom4USARTObj.txBusyStatus = true;

            if(size == 0)
            {
                writeStatus = true;
            }
            else
            {
                /* Initiate the transfer by sending first byte */
                if((SERCOM4_REGS->USART.INTFLAG & SERCOM_USART_INTFLAG_DRE_Msk) == SERCOM_USART_INTFLAG_DRE_Msk)
                {
                    SERCOM4_REGS->USART.DATA = sercom4USARTObj.txBuffer[sercom4USARTObj.txProcessedSize++];
                }

                SERCOM4_REGS->USART.INTENSET = SERCOM_USART_INTFLAG_DRE_Msk;

                writeStatus = true;
            }
        }
    }

    return writeStatus;
}

bool SERCOM4_USART_WriteIsBusy ( void )
{
    return sercom4USARTObj.txBusyStatus;
}

size_t SERCOM4_USART_WriteCountGet( void )
{
    return sercom4USARTObj.txProcessedSize;
}

void SERCOM4_USART_WriteCallbackRegister( SERCOM_USART_CALLBACK callback, uintptr_t context )
{
    sercom4USARTObj.txCallback = callback;

    sercom4USARTObj.txContext = context;
}

bool SERCOM4_USART_Read( void *buffer, const size_t size )
{
    bool readStatus        = false;
    uint8_t *pu8Data       = (uint8_t*)buffer;
    uint8_t u8dummyData    = 0;

    if(pu8Data != NULL)
    {
        if(sercom4USARTObj.rxBusyStatus == false)
        {
            /* Checks for error before receiving */
            if(SERCOM4_USART_ErrorGet() != USART_ERROR_NONE)
            {
                /* Clear all error flags */
                SERCOM4_REGS->USART.INTFLAG = SERCOM_USART_INTFLAG_ERROR_Msk;

                /* Clear error statuses */
                SERCOM4_REGS->USART.STATUS = SERCOM_USART_STATUS_Msk;

                /* Flush existing error bytes from the RX FIFO */
                while((SERCOM4_REGS->USART.INTFLAG & SERCOM_USART_INTFLAG_RXC_Msk) == SERCOM_USART_INTFLAG_RXC_Msk)
                {
                    u8dummyData = SERCOM4_REGS->USART.DATA;
                }

                /* Ignore the warning */
                (void)u8dummyData;
            }

            sercom4USARTObj.rxBuffer = pu8Data;
            sercom4USARTObj.rxSize = size;
            sercom4USARTObj.rxProcessedSize = 0;
            sercom4USARTObj.rxBusyStatus = true;
            readStatus = true;

            /* Enable error interrupts */
            SERCOM4_REGS->USART.INTENSET |= SERCOM_USART_INTENSET_ERROR_Msk;

            /* Enable Receive Complete interrupt */
            SERCOM4_REGS->USART.INTENSET = SERCOM_USART_INTENSET_RXC_Msk;
        }
    }

    return readStatus;
}

bool SERCOM4_USART_ReadIsBusy( void )
{
    return sercom4USARTObj.rxBusyStatus;
}

size_t SERCOM4_USART_ReadCountGet( void )
{
    return sercom4USARTObj.rxProcessedSize;
}

void SERCOM4_USART_ReadCallbackRegister( SERCOM_USART_CALLBACK callback, uintptr_t context )
{
    sercom4USARTObj.rxCallback = callback;

    sercom4USARTObj.rxContext = context;
}

USART_ERROR SERCOM4_USART_ErrorGet( void )
{
    USART_ERROR errorStatus = USART_ERROR_NONE;

    errorStatus = SERCOM4_REGS->USART.STATUS & (SERCOM_USART_STATUS_PERR_Msk | SERCOM_USART_STATUS_FERR_Msk | SERCOM_USART_STATUS_BUFOVF_Msk);

    /* Clear Errors */
    SERCOM4_REGS->USART.STATUS = SERCOM_USART_STATUS_PERR_Msk | SERCOM_USART_STATUS_FERR_Msk | SERCOM_USART_STATUS_BUFOVF_Msk;

    return errorStatus;
}

void static SERCOM4_USART_ISR_ERR_Handler( void )
{
    USART_ERROR errorStatus = USART_ERROR_NONE;
    uint8_t  u8dummyData = 0;

    errorStatus = (SERCOM4_REGS->USART.STATUS &
                  (SERCOM_USART_STATUS_PERR_Msk |
                  SERCOM_USART_STATUS_FERR_Msk |
                  SERCOM_USART_STATUS_BUFOVF_Msk));

    if(errorStatus != USART_ERROR_NONE)
    {
        /* Clear all error flags */
        SERCOM4_REGS->USART.INTFLAG = SERCOM_USART_INTFLAG_ERROR_Msk;

        /* Clear error statuses */
        SERCOM4_REGS->USART.STATUS = SERCOM_USART_STATUS_Msk;

        /* Flush existing error bytes from the RX FIFO */
        while((SERCOM4_REGS->USART.INTFLAG & SERCOM_USART_INTFLAG_RXC_Msk) == SERCOM_USART_INTFLAG_RXC_Msk)
        {
            u8dummyData = SERCOM4_REGS->USART.DATA;
        }

        /* Ignore the warning */
        (void)u8dummyData;

        if(sercom4USARTObj.rxCallback != NULL)
        {
            sercom4USARTObj.rxCallback(sercom4USARTObj.rxContext);
        }
    }
}

void static SERCOM4_USART_ISR_RX_Handler( void )
{
    if(sercom4USARTObj.rxBusyStatus == true)
    {
        if(sercom4USARTObj.rxSize >= sercom4USARTObj.rxProcessedSize)
        {
            if(sercom4USARTObj.rxSize == sercom4USARTObj.rxProcessedSize)
            {
                sercom4USARTObj.rxBusyStatus = false;
                sercom4USARTObj.rxSize = 0;
                SERCOM4_REGS->USART.INTENCLR = SERCOM_USART_INTENCLR_RXC_Msk;

                if(sercom4USARTObj.rxCallback != NULL)
                {
                    sercom4USARTObj.rxCallback(sercom4USARTObj.rxContext);
                }
            }
            else
            {
                sercom4USARTObj.rxBuffer[sercom4USARTObj.rxProcessedSize++] = SERCOM4_REGS->USART.DATA;
            }
        }
    }
}

void static SERCOM4_USART_ISR_TX_Handler( void )
{
    if(sercom4USARTObj.txBusyStatus == true)
    {
        if(sercom4USARTObj.txSize >= sercom4USARTObj.txProcessedSize)
        {
            if(sercom4USARTObj.txSize == sercom4USARTObj.txProcessedSize)
            {
                sercom4USARTObj.txBusyStatus = false;
                sercom4USARTObj.txSize = 0;
                SERCOM4_REGS->USART.INTENCLR = SERCOM_USART_INTENCLR_DRE_Msk;

                if(sercom4USARTObj.txCallback != NULL)
                {
                    sercom4USARTObj.txCallback(sercom4USARTObj.txContext);
                }
            }
            else
            {
                SERCOM4_REGS->USART.DATA = sercom4USARTObj.txBuffer[sercom4USARTObj.txProcessedSize++];
            }
        }
    }
}

void SERCOM4_USART_InterruptHandler( void )
{
    if(SERCOM4_REGS->USART.INTENSET != 0)
    {
        /* Checks for data register empty flag */
        if((SERCOM4_REGS->USART.INTFLAG & SERCOM_USART_INTFLAG_DRE_Msk) == SERCOM_USART_INTFLAG_DRE_Msk)
        {
            SERCOM4_USART_ISR_TX_Handler();
        }

        /* Checks for receive complete empty flag */
        if((SERCOM4_REGS->USART.INTFLAG & SERCOM_USART_INTFLAG_RXC_Msk) == SERCOM_USART_INTFLAG_RXC_Msk)
        {
            SERCOM4_USART_ISR_RX_Handler();
        }

        /* Checks for error flag */
        if((SERCOM4_REGS->USART.INTFLAG & SERCOM_USART_INTFLAG_ERROR_Msk) == SERCOM_USART_INTFLAG_ERROR_Msk)
        {
            SERCOM4_USART_ISR_ERR_Handler();
        }
    }
}
