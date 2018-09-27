/*******************************************************************************
  SERCOM Universal Synchronous/Asynchrnous Receiver/Transmitter PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_${SERCOM_INSTANCE_NAME?lower_case}_usart.c

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

#include "plib_${SERCOM_INSTANCE_NAME?lower_case}_usart.h"

// *****************************************************************************
// *****************************************************************************
// Section: Global Data
// *****************************************************************************
// *****************************************************************************

<#if USART_INTERRUPT_MODE = true>
SERCOM_USART_OBJECT ${SERCOM_INSTANCE_NAME?lower_case}USARTObj;
</#if>

// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************
/* The following functions make up the methods (set of possible operations) of
this interface.
*/

void ${SERCOM_INSTANCE_NAME}_USART_Initialize( void )
{
    /* Reset USART */
    ${SERCOM_INSTANCE_NAME}_REGS->USART.CTRLA = SERCOM_USART_CTRLA_SWRST_Msk;

    /* Wait for sync */
    while(${SERCOM_INSTANCE_NAME}_REGS->USART.SYNCBUSY);

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
    <@compress single_line=true>${SERCOM_INSTANCE_NAME}_REGS->USART.CTRLA = SERCOM_USART_CTRLA_MODE(${(SERCOM_MODE == "USART_INT")?then('0x1', '0x0')}) |
                                                                            SERCOM_USART_CTRLA_RXPO(${USART_RXPO}) |
                                                                            SERCOM_USART_CTRLA_TXPO(${USART_TXPO}) |
                                                                            SERCOM_USART_CTRLA_DORD_Msk |
                                                                            SERCOM_USART_CTRLA_SAMPR(${USART_SAMPLE_RATE}) |
                                                                            SERCOM_USART_CTRLA_IBON_Msk |
                                                                            SERCOM_USART_CTRLA_FORM(${(USART_PARITY_MODE == "0x2")?then('0x0', '0x1')})
                                                                            ${USART_RUNSTDBY?then('| SERCOM_USART_CTRLA_RUNSTDBY_Msk', '')};</@compress>

    /* Configure Baud Rate */
    ${SERCOM_INSTANCE_NAME}_REGS->USART.BAUD = SERCOM_USART_BAUD_BAUD(${USART_BAUD_VALUE});

    /*
     * Configures RXEN
     * Configures TXEN
     * Configures CHSIZE
     * Configures Parity
     * Configures Stop bits
     */
    <@compress single_line=true>${SERCOM_INSTANCE_NAME}_REGS->USART.CTRLB = SERCOM_USART_CTRLB_CHSIZE(${USART_CHARSIZE_BITS})
                                                                            ${(USART_PARITY_MODE == "0x1")?then('| SERCOM_USART_CTRLB_PMODE_Msk', '')}
                                                                            ${(USART_STOP_BIT == "0x1")?then('| SERCOM_USART_CTRLB_SBMODE_Msk', '')}
                                                                            ${USART_RX_ENABLE?then('| SERCOM_USART_CTRLB_RXEN_Msk', '')}
                                                                            ${USART_TX_ENABLE?then('| SERCOM_USART_CTRLB_TXEN_Msk', '')};</@compress>

    /* Wait for sync */
    while(${SERCOM_INSTANCE_NAME}_REGS->USART.SYNCBUSY);

    /* Enable the UART after the configurations */
    ${SERCOM_INSTANCE_NAME}_REGS->USART.CTRLA |= SERCOM_USART_CTRLA_ENABLE_Msk;

    /* Wait for sync */
    while(${SERCOM_INSTANCE_NAME}_REGS->USART.SYNCBUSY);

<#if USART_INTERRUPT_MODE = true>
    /* Initialize instance object */
    ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxBuffer = NULL;
    ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxSize = 0;
    ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxProcessedSize = 0;
    ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxBusyStatus = false;
    ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxCallback = NULL;
    ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.txBuffer = NULL;
    ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.txSize = 0;
    ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.txProcessedSize = 0;
    ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.txBusyStatus = false;
    ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.txCallback = NULL;
</#if>
}

bool ${SERCOM_INSTANCE_NAME}_USART_SerialSetup( USART_SERIAL_SETUP * serialSetup, uint32_t clkFrequency )
{
    bool setupStatus       = false;
    uint32_t sampleRate    = 0;
    uint32_t baudValue     = 0;

<#if USART_INTERRUPT_MODE == true>
    if((${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxBusyStatus == true) || (${SERCOM_INSTANCE_NAME?lower_case}USARTObj.txBusyStatus == true))
    {
        /* Transaction is in progress, so return without updating settings */
        return setupStatus;
    }

</#if>
    if((serialSetup != NULL) & (serialSetup->baudRate != 0))
    {
        if(clkFrequency == 0)
        {
            clkFrequency = ${SERCOM_INSTANCE_NAME}_USART_FrequencyGet();
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
            ${SERCOM_INSTANCE_NAME}_REGS->USART.CTRLA &= ~SERCOM_USART_CTRLA_ENABLE_Msk;

            /* Wait for sync */
            while(${SERCOM_INSTANCE_NAME}_REGS->USART.SYNCBUSY);

            /* Configure Baud Rate */
            ${SERCOM_INSTANCE_NAME}_REGS->USART.BAUD = SERCOM_USART_BAUD_BAUD(baudValue);

            /* Configure Parity Options */
            if(serialSetup->parity == USART_PARITY_NONE)
            {
                ${SERCOM_INSTANCE_NAME}_REGS->USART.CTRLA |= SERCOM_USART_CTRLA_SAMPR(sampleRate) | SERCOM_USART_CTRLA_FORM(0x0);

                ${SERCOM_INSTANCE_NAME}_REGS->USART.CTRLB |= serialSetup->dataWidth | serialSetup->stopBits;
            }
            else
            {
                ${SERCOM_INSTANCE_NAME}_REGS->USART.CTRLA |= SERCOM_USART_CTRLA_SAMPR(sampleRate) | SERCOM_USART_CTRLA_FORM(0x1);

                ${SERCOM_INSTANCE_NAME}_REGS->USART.CTRLB |= serialSetup->dataWidth | serialSetup->parity | serialSetup->stopBits;
            }

            /* Wait for sync */
            while(${SERCOM_INSTANCE_NAME}_REGS->USART.SYNCBUSY);

            /* Enable the USART after the configurations */
            ${SERCOM_INSTANCE_NAME}_REGS->USART.CTRLA |= SERCOM_USART_CTRLA_ENABLE_Msk;

            /* Wait for sync */
            while(${SERCOM_INSTANCE_NAME}_REGS->USART.SYNCBUSY);

            setupStatus = true;
        }
    }

    return setupStatus;
}

<#if USART_TX_ENABLE = true>
bool ${SERCOM_INSTANCE_NAME}_USART_Write( void *buffer, const size_t size )
{
    bool writeStatus      = false;
    uint8_t *pu8Data      = (uint8_t*)buffer;
<#if USART_INTERRUPT_MODE = false>
    uint32_t u32Length    = size;
</#if>

    if(pu8Data != NULL)
    {
<#if USART_INTERRUPT_MODE = false>
        /* Blocks while buffer is being transferred */
        while(u32Length--)
        {
            while((${SERCOM_INSTANCE_NAME}_REGS->USART.INTFLAG & SERCOM_USART_INTFLAG_DRE_Msk) != SERCOM_USART_INTFLAG_DRE_Msk)
            {
                /* Check if USART is ready for new data */
            }

            /* Write data to USART module */
            ${SERCOM_INSTANCE_NAME}_REGS->USART.DATA = *pu8Data++;
        }

        writeStatus = true;
<#else>
        if(${SERCOM_INSTANCE_NAME?lower_case}USARTObj.txBusyStatus == false)
        {
            ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.txBuffer = pu8Data;
            ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.txSize = size;
            ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.txProcessedSize = 0;
            ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.txBusyStatus = true;

            if(size == 0)
            {
                writeStatus = true;
            }
            else
            {
                /* Initiate the transfer by sending first byte */
                if((${SERCOM_INSTANCE_NAME}_REGS->USART.INTFLAG & SERCOM_USART_INTFLAG_DRE_Msk) == SERCOM_USART_INTFLAG_DRE_Msk)
                {
                    ${SERCOM_INSTANCE_NAME}_REGS->USART.DATA = ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.txBuffer[${SERCOM_INSTANCE_NAME?lower_case}USARTObj.txProcessedSize++];
                }

                ${SERCOM_INSTANCE_NAME}_REGS->USART.INTENSET = SERCOM_USART_INTFLAG_DRE_Msk;

                writeStatus = true;
            }
        }
</#if>
    }

    return writeStatus;
}

<#if USART_INTERRUPT_MODE = true>
bool ${SERCOM_INSTANCE_NAME}_USART_WriteIsBusy ( void )
{
    return ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.txBusyStatus;
}

size_t ${SERCOM_INSTANCE_NAME}_USART_WriteCountGet( void )
{
    return ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.txProcessedSize;
}

void ${SERCOM_INSTANCE_NAME}_USART_WriteCallbackRegister( SERCOM_USART_CALLBACK callback, uintptr_t context )
{
    ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.txCallback = callback;

    ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.txContext = context;
}
<#else>
bool ${SERCOM_INSTANCE_NAME}_USART_TransmitterIsReady( void )
{
    bool transmitterStatus = false;

    if((${SERCOM_INSTANCE_NAME}_REGS->USART.INTFLAG & SERCOM_USART_INTFLAG_DRE_Msk) == SERCOM_USART_INTFLAG_DRE_Msk)
    {
        transmitterStatus = true;
    }

    return transmitterStatus;
}

void ${SERCOM_INSTANCE_NAME}_USART_WriteByte( int data )
{
    while((${SERCOM_INSTANCE_NAME}_REGS->USART.INTFLAG & SERCOM_USART_INTFLAG_DRE_Msk) != SERCOM_USART_INTFLAG_DRE_Msk)
    {
        /* Check if USART is ready for new data */
    }

    ${SERCOM_INSTANCE_NAME}_REGS->USART.DATA = data;
}
</#if>
</#if>

<#if USART_RX_ENABLE = true>
bool ${SERCOM_INSTANCE_NAME}_USART_Read( void *buffer, const size_t size )
{
    bool readStatus        = false;
    uint8_t *pu8Data       = (uint8_t*)buffer;
    uint8_t u8dummyData    = 0;
<#if USART_INTERRUPT_MODE = false>
    uint32_t u32Length     = size;
    uint32_t processedSize = 0;
</#if>

    if(pu8Data != NULL)
    {
<#if USART_INTERRUPT_MODE = false>
        /* Checks for error before receiving */
        if(${SERCOM_INSTANCE_NAME}_USART_ErrorGet() != USART_ERROR_NONE)
        {
            /* Clear all error flags */
            ${SERCOM_INSTANCE_NAME}_REGS->USART.INTFLAG = SERCOM_USART_INTFLAG_ERROR_Msk;

            /* Clear error statuses */
            ${SERCOM_INSTANCE_NAME}_REGS->USART.STATUS = SERCOM_USART_STATUS_Msk;

            /* Flush existing error bytes from the RX FIFO */
            while((${SERCOM_INSTANCE_NAME}_REGS->USART.INTFLAG & SERCOM_USART_INTFLAG_RXC_Msk) == SERCOM_USART_INTFLAG_RXC_Msk)
            {
                u8dummyData = ${SERCOM_INSTANCE_NAME}_REGS->USART.DATA;
            }

            /* Ignore the warning */
            (void)u8dummyData;
        }

        while(u32Length--)
        {
            while((${SERCOM_INSTANCE_NAME}_REGS->USART.INTFLAG & SERCOM_USART_INTFLAG_RXC_Msk) != SERCOM_USART_INTFLAG_RXC_Msk)
            {
                /* Check if USART has new data */
            }

            /* Read data from USART module */
            *pu8Data++ = ${SERCOM_INSTANCE_NAME}_REGS->USART.DATA;
            processedSize++;

            if(${SERCOM_INSTANCE_NAME}_USART_ErrorGet() != USART_ERROR_NONE)
            {
                break;
            }
        }

        if(size == processedSize)
        {
            readStatus = true;
        }
<#else>
        if(${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxBusyStatus == false)
        {
            /* Checks for error before receiving */
            if(${SERCOM_INSTANCE_NAME}_USART_ErrorGet() != USART_ERROR_NONE)
            {
                /* Clear all error flags */
                ${SERCOM_INSTANCE_NAME}_REGS->USART.INTFLAG = SERCOM_USART_INTFLAG_ERROR_Msk;

                /* Clear error statuses */
                ${SERCOM_INSTANCE_NAME}_REGS->USART.STATUS = SERCOM_USART_STATUS_Msk;

                /* Flush existing error bytes from the RX FIFO */
                while((${SERCOM_INSTANCE_NAME}_REGS->USART.INTFLAG & SERCOM_USART_INTFLAG_RXC_Msk) == SERCOM_USART_INTFLAG_RXC_Msk)
                {
                    u8dummyData = ${SERCOM_INSTANCE_NAME}_REGS->USART.DATA;
                }

                /* Ignore the warning */
                (void)u8dummyData;
            }

            ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxBuffer = pu8Data;
            ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxSize = size;
            ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxProcessedSize = 0;
            ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxBusyStatus = true;
            readStatus = true;

            /* Enable error interrupts */
            ${SERCOM_INSTANCE_NAME}_REGS->USART.INTENSET |= SERCOM_USART_INTENSET_ERROR_Msk;

            /* Enable Receive Complete interrupt */
            ${SERCOM_INSTANCE_NAME}_REGS->USART.INTENSET = SERCOM_USART_INTENSET_RXC_Msk;
        }
</#if>
    }

    return readStatus;
}

<#if USART_INTERRUPT_MODE = true>
bool ${SERCOM_INSTANCE_NAME}_USART_ReadIsBusy( void )
{
    return ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxBusyStatus;
}

size_t ${SERCOM_INSTANCE_NAME}_USART_ReadCountGet( void )
{
    return ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxProcessedSize;
}

void ${SERCOM_INSTANCE_NAME}_USART_ReadCallbackRegister( SERCOM_USART_CALLBACK callback, uintptr_t context )
{
    ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxCallback = callback;

    ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxContext = context;
}
<#else>
bool ${SERCOM_INSTANCE_NAME}_USART_ReceiverIsReady( void )
{
    bool receiverStatus = false;

    if((${SERCOM_INSTANCE_NAME}_REGS->USART.INTFLAG & SERCOM_USART_INTFLAG_RXC_Msk) == SERCOM_USART_INTFLAG_RXC_Msk)
    {
        receiverStatus = true;
    }

    return receiverStatus;
}

int ${SERCOM_INSTANCE_NAME}_USART_ReadByte( void )
{
    return ${SERCOM_INSTANCE_NAME}_REGS->USART.DATA;
}
</#if>
</#if>

USART_ERROR ${SERCOM_INSTANCE_NAME}_USART_ErrorGet( void )
{
    USART_ERROR errorStatus = USART_ERROR_NONE;

    errorStatus = ${SERCOM_INSTANCE_NAME}_REGS->USART.STATUS & (SERCOM_USART_STATUS_PERR_Msk | SERCOM_USART_STATUS_FERR_Msk | SERCOM_USART_STATUS_BUFOVF_Msk);

    /* Clear Errors */
    ${SERCOM_INSTANCE_NAME}_REGS->USART.STATUS = SERCOM_USART_STATUS_PERR_Msk | SERCOM_USART_STATUS_FERR_Msk | SERCOM_USART_STATUS_BUFOVF_Msk;

    return errorStatus;
}

<#if USART_INTERRUPT_MODE = true>
void static ${SERCOM_INSTANCE_NAME}_USART_ISR_ERR_Handler( void )
{
    USART_ERROR errorStatus = USART_ERROR_NONE;
    uint8_t  u8dummyData = 0;

    errorStatus = (${SERCOM_INSTANCE_NAME}_REGS->USART.STATUS &
                  (SERCOM_USART_STATUS_PERR_Msk |
                  SERCOM_USART_STATUS_FERR_Msk |
                  SERCOM_USART_STATUS_BUFOVF_Msk));

    if(errorStatus != USART_ERROR_NONE)
    {
        /* Clear all error flags */
        ${SERCOM_INSTANCE_NAME}_REGS->USART.INTFLAG = SERCOM_USART_INTFLAG_ERROR_Msk;

        /* Clear error statuses */
        ${SERCOM_INSTANCE_NAME}_REGS->USART.STATUS = SERCOM_USART_STATUS_Msk;

        /* Flush existing error bytes from the RX FIFO */
        while((${SERCOM_INSTANCE_NAME}_REGS->USART.INTFLAG & SERCOM_USART_INTFLAG_RXC_Msk) == SERCOM_USART_INTFLAG_RXC_Msk)
        {
            u8dummyData = ${SERCOM_INSTANCE_NAME}_REGS->USART.DATA;
        }

        /* Ignore the warning */
        (void)u8dummyData;

        if(${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxCallback != NULL)
        {
            ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxCallback(${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxContext);
        }
    }
}

<#if USART_RX_ENABLE = true>
void static ${SERCOM_INSTANCE_NAME}_USART_ISR_RX_Handler( void )
{
    if(${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxBusyStatus == true)
    {
        if(${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxSize >= ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxProcessedSize)
        {
            if(${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxSize == ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxProcessedSize)
            {
                ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxBusyStatus = false;
                ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxSize = 0;
                ${SERCOM_INSTANCE_NAME}_REGS->USART.INTENCLR = SERCOM_USART_INTENCLR_RXC_Msk;

                if(${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxCallback != NULL)
                {
                    ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxCallback(${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxContext);
                }
            }
            else
            {
                ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxBuffer[${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxProcessedSize++] = ${SERCOM_INSTANCE_NAME}_REGS->USART.DATA;
            }
        }
    }
}
</#if>

<#if USART_TX_ENABLE = true>
void static ${SERCOM_INSTANCE_NAME}_USART_ISR_TX_Handler( void )
{
    if(${SERCOM_INSTANCE_NAME?lower_case}USARTObj.txBusyStatus == true)
    {
        if(${SERCOM_INSTANCE_NAME?lower_case}USARTObj.txSize >= ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.txProcessedSize)
        {
            if(${SERCOM_INSTANCE_NAME?lower_case}USARTObj.txSize == ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.txProcessedSize)
            {
                ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.txBusyStatus = false;
                ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.txSize = 0;
                ${SERCOM_INSTANCE_NAME}_REGS->USART.INTENCLR = SERCOM_USART_INTENCLR_DRE_Msk;

                if(${SERCOM_INSTANCE_NAME?lower_case}USARTObj.txCallback != NULL)
                {
                    ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.txCallback(${SERCOM_INSTANCE_NAME?lower_case}USARTObj.txContext);
                }
            }
            else
            {
                ${SERCOM_INSTANCE_NAME}_REGS->USART.DATA = ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.txBuffer[${SERCOM_INSTANCE_NAME?lower_case}USARTObj.txProcessedSize++];
            }
        }
    }
}
</#if>

void ${SERCOM_INSTANCE_NAME}_USART_InterruptHandler( void )
{
    if(${SERCOM_INSTANCE_NAME}_REGS->USART.INTENSET != 0)
    {
        /* Checks for data register empty flag */
        if((${SERCOM_INSTANCE_NAME}_REGS->USART.INTFLAG & SERCOM_USART_INTFLAG_DRE_Msk) == SERCOM_USART_INTFLAG_DRE_Msk)
        {
            ${SERCOM_INSTANCE_NAME}_USART_ISR_TX_Handler();
        }

        /* Checks for receive complete empty flag */
        if((${SERCOM_INSTANCE_NAME}_REGS->USART.INTFLAG & SERCOM_USART_INTFLAG_RXC_Msk) == SERCOM_USART_INTFLAG_RXC_Msk)
        {
            ${SERCOM_INSTANCE_NAME}_USART_ISR_RX_Handler();
        }

        /* Checks for error flag */
        if((${SERCOM_INSTANCE_NAME}_REGS->USART.INTFLAG & SERCOM_USART_INTFLAG_ERROR_Msk) == SERCOM_USART_INTFLAG_ERROR_Msk)
        {
            ${SERCOM_INSTANCE_NAME}_USART_ISR_ERR_Handler();
        }
    }
}
</#if>
