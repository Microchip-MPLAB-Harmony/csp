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

#include "plib_${SERCOM_INSTANCE_NAME?lower_case}_usart.h"

// *****************************************************************************
// *****************************************************************************
// Section: Global Data
// *****************************************************************************
// *****************************************************************************

<#assign USART_PLIB = "SERCOM_INSTANCE_NAME">
<#assign USART_PLIB_CLOCK_FREQUENCY = "core." + USART_PLIB?eval + "_CORE_CLOCK_FREQUENCY">

/* ${SERCOM_INSTANCE_NAME} USART baud value for ${USART_BAUD_RATE} Hz baud rate */
#define ${SERCOM_INSTANCE_NAME}_USART_INT_BAUD_VALUE            (${USART_BAUD_VALUE}U)

<#if USART_INTERRUPT_MODE = true>
SERCOM_USART_OBJECT ${SERCOM_INSTANCE_NAME?lower_case}USARTObj;
</#if>

// *****************************************************************************
// *****************************************************************************
// Section: ${SERCOM_INSTANCE_NAME} USART Interface Routines
// *****************************************************************************
// *****************************************************************************

void static ${SERCOM_INSTANCE_NAME}_USART_ErrorClear( void )
{
    uint8_t  u8dummyData = 0;

<#if USART_INTENSET_ERROR = true>
    /* Clear error flag */
    ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_INTFLAG = SERCOM_USART_INT_INTFLAG_ERROR_Msk;

</#if>
    /* Clear all errors */
    ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_STATUS = SERCOM_USART_INT_STATUS_PERR_Msk | SERCOM_USART_INT_STATUS_FERR_Msk | SERCOM_USART_INT_STATUS_BUFOVF_Msk;

    /* Flush existing error bytes from the RX FIFO */
    while((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_INTFLAG & SERCOM_USART_INT_INTFLAG_RXC_Msk) == SERCOM_USART_INT_INTFLAG_RXC_Msk)
    {
        u8dummyData = ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_DATA;
    }

    /* Ignore the warning */
    (void)u8dummyData;
}

void ${SERCOM_INSTANCE_NAME}_USART_Initialize( void )
{
    /*
     * Configures USART Clock Mode
     * Configures TXPO and RXPO
     * Configures Data Order
     * Configures Standby Mode
     * Configures Sampling rate
     * Configures IBON
     */
    <@compress single_line=true>${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_CTRLA = SERCOM_USART_INT_CTRLA_MODE_USART_INT_CLK |
                                                                                       SERCOM_USART_INT_CTRLA_RXPO_${USART_RXPO} |
                                                                                       SERCOM_USART_INT_CTRLA_TXPO_${USART_TXPO} |
                                                                                       SERCOM_USART_INT_CTRLA_DORD_Msk |
                                                                                       SERCOM_USART_INT_CTRLA_IBON_Msk |
                                                                                       SERCOM_USART_INT_CTRLA_FORM(${(USART_PARITY_MODE == "NONE")?then('0x0', '0x1')})
                                                                                       <#if USART_SAMPLE_RATE??>| SERCOM_USART_INT_CTRLA_SAMPR(${USART_SAMPLE_RATE})</#if>
                                                                                       ${USART_RUNSTDBY?then('| SERCOM_USART_INT_CTRLA_RUNSTDBY_Msk', '')};</@compress>

    /* Configure Baud Rate */
    ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_BAUD = SERCOM_USART_INT_BAUD_BAUD(${SERCOM_INSTANCE_NAME}_USART_INT_BAUD_VALUE);

    /*
     * Configures RXEN
     * Configures TXEN
     * Configures CHSIZE
     * Configures Parity
     * Configures Stop bits
     */
    <@compress single_line=true>${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_CTRLB = SERCOM_USART_INT_CTRLB_CHSIZE_${USART_CHARSIZE_BITS} |
                                                                                       SERCOM_USART_INT_CTRLB_SBMODE_${USART_STOP_BIT}
                                                                                       ${(USART_PARITY_MODE == "ODD")?then('| SERCOM_USART_INT_CTRLB_PMODE_Msk', '')}
                                                                                       ${USART_RX_ENABLE?then('| SERCOM_USART_INT_CTRLB_RXEN_Msk', '')}
                                                                                       ${USART_TX_ENABLE?then('| SERCOM_USART_INT_CTRLB_TXEN_Msk', '')};</@compress>

    /* Wait for sync */
<#if SERCOM_SYNCBUSY = false>
    while((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_STATUS & SERCOM_USART_INT_STATUS_SYNCBUSY_Msk) & SERCOM_USART_INT_STATUS_SYNCBUSY_Msk);
<#else>
    while(${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_SYNCBUSY);
</#if>

    /* Enable the UART after the configurations */
    ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_CTRLA |= SERCOM_USART_INT_CTRLA_ENABLE_Msk;

    /* Wait for sync */
<#if SERCOM_SYNCBUSY = false>
    while((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_STATUS & SERCOM_USART_INT_STATUS_SYNCBUSY_Msk) & SERCOM_USART_INT_STATUS_SYNCBUSY_Msk);
<#else>
    while(${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_SYNCBUSY);
</#if>
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

uint32_t ${SERCOM_INSTANCE_NAME}_USART_FrequencyGet( void )
{
<#if USART_PLIB_CLOCK_FREQUENCY?eval??>
    return (uint32_t) (${USART_PLIB_CLOCK_FREQUENCY?eval}UL);
<#else>
    return 0;
</#if>
}

bool ${SERCOM_INSTANCE_NAME}_USART_SerialSetup( USART_SERIAL_SETUP * serialSetup, uint32_t clkFrequency )
{
    bool setupStatus       = false;
    uint32_t baudValue     = 0;
<#if USART_SAMPLE_RATE??>
    uint32_t sampleRate    = 0;
</#if>

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

        <#if USART_SAMPLE_RATE??>
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
        <#else>
        if(clkFrequency >= (16 * serialSetup->baudRate))
        {
            baudValue = 65536 - ((uint64_t)65536 * 16 * serialSetup->baudRate) / clkFrequency;
        }
        </#if>

        if(baudValue != 0)
        {
            /* Disable the USART before configurations */
            ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_CTRLA &= ~SERCOM_USART_INT_CTRLA_ENABLE_Msk;

            /* Wait for sync */
            <#if SERCOM_SYNCBUSY = false>
            while((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_STATUS & SERCOM_USART_INT_STATUS_SYNCBUSY_Msk) & SERCOM_USART_INT_STATUS_SYNCBUSY_Msk);
            <#else>
            while(${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_SYNCBUSY);
            </#if>

            /* Configure Baud Rate */
            ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_BAUD = SERCOM_USART_INT_BAUD_BAUD(baudValue);

            /* Configure Parity Options */
            if(serialSetup->parity == USART_PARITY_NONE)
            {
                ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_CTRLA |= SERCOM_USART_INT_CTRLA_FORM(0x0) <#if USART_SAMPLE_RATE??>| SERCOM_USART_INT_CTRLA_SAMPR(sampleRate)</#if>;

                ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_CTRLB |= serialSetup->dataWidth | serialSetup->stopBits;
            }
            else
            {
                ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_CTRLA |= SERCOM_USART_INT_CTRLA_FORM(0x1) <#if USART_SAMPLE_RATE??>| SERCOM_USART_INT_CTRLA_SAMPR(sampleRate)</#if>;

                ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_CTRLB |= serialSetup->dataWidth | serialSetup->parity | serialSetup->stopBits;
            }

            /* Wait for sync */
            <#if SERCOM_SYNCBUSY = false>
            while((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_STATUS & SERCOM_USART_INT_STATUS_SYNCBUSY_Msk) & SERCOM_USART_INT_STATUS_SYNCBUSY_Msk);
            <#else>
            while(${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_SYNCBUSY);
            </#if>

            /* Enable the USART after the configurations */
            ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_CTRLA |= SERCOM_USART_INT_CTRLA_ENABLE_Msk;

            /* Wait for sync */
            <#if SERCOM_SYNCBUSY = false>
            while((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_STATUS & SERCOM_USART_INT_STATUS_SYNCBUSY_Msk) & SERCOM_USART_INT_STATUS_SYNCBUSY_Msk);
            <#else>
            while(${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_SYNCBUSY);
            </#if>

            setupStatus = true;
        }
    }

    return setupStatus;
}

USART_ERROR ${SERCOM_INSTANCE_NAME}_USART_ErrorGet( void )
{
    USART_ERROR errorStatus = USART_ERROR_NONE;

    errorStatus = ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_STATUS & (SERCOM_USART_INT_STATUS_PERR_Msk | SERCOM_USART_INT_STATUS_FERR_Msk | SERCOM_USART_INT_STATUS_BUFOVF_Msk);

    if(errorStatus != USART_ERROR_NONE)
    {
        ${SERCOM_INSTANCE_NAME}_USART_ErrorClear();
    }

    return errorStatus;
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
            /* Check if USART is ready for new data */
            while((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_INTFLAG & SERCOM_USART_INT_INTFLAG_DRE_Msk) != SERCOM_USART_INT_INTFLAG_DRE_Msk);

            /* Write data to USART module */
            ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_DATA = *pu8Data++;
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
                if((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_INTFLAG & SERCOM_USART_INT_INTFLAG_DRE_Msk) == SERCOM_USART_INT_INTFLAG_DRE_Msk)
                {
                    ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_DATA = ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.txBuffer[${SERCOM_INSTANCE_NAME?lower_case}USARTObj.txProcessedSize++];
                }

                ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_INTENSET = SERCOM_USART_INT_INTFLAG_DRE_Msk;

                writeStatus = true;
            }
        }
</#if>
    }

    return writeStatus;
}

<#if USART_INTERRUPT_MODE = true>
bool ${SERCOM_INSTANCE_NAME}_USART_WriteIsBusy( void )
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

    if((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_INTFLAG & SERCOM_USART_INT_INTFLAG_DRE_Msk) == SERCOM_USART_INT_INTFLAG_DRE_Msk)
    {
        transmitterStatus = true;
    }

    return transmitterStatus;
}

bool ${SERCOM_INSTANCE_NAME}_USART_TransmitComplete( void )
{
    bool transmitComplete = false;

    if((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_INTFLAG & SERCOM_USART_INT_INTFLAG_TXC_Msk) == SERCOM_USART_INT_INTFLAG_TXC_Msk)
    {
        transmitComplete = true;
    }

    return transmitComplete;
}

void ${SERCOM_INSTANCE_NAME}_USART_WriteByte( int data )
{
    /* Check if USART is ready for new data */
    while((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_INTFLAG & SERCOM_USART_INT_INTFLAG_DRE_Msk) != SERCOM_USART_INT_INTFLAG_DRE_Msk);

    ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_DATA = data;
}
</#if>
</#if>

<#if USART_RX_ENABLE = true>
bool ${SERCOM_INSTANCE_NAME}_USART_Read( void *buffer, const size_t size )
{
    bool readStatus        = false;
    uint8_t *pu8Data       = (uint8_t*)buffer;
<#if USART_INTERRUPT_MODE = false>
    uint32_t u32Length     = size;
    uint32_t processedSize = 0;
</#if>

    if(pu8Data != NULL)
    {
        /* Clear errors before submitting the request.
         * ErrorGet clears errors internally.
         */
        ${SERCOM_INSTANCE_NAME}_USART_ErrorGet();

<#if USART_INTERRUPT_MODE = false>
        while(u32Length--)
        {
            /* Check if USART has new data */
            while((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_INTFLAG & SERCOM_USART_INT_INTFLAG_RXC_Msk) != SERCOM_USART_INT_INTFLAG_RXC_Msk);

            /* Read data from USART module */
            *pu8Data++ = ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_DATA;
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
            ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxBuffer = pu8Data;
            ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxSize = size;
            ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxProcessedSize = 0;
            ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxBusyStatus = true;
            readStatus = true;

            <#if USART_INTENSET_ERROR = true>
            /* Enable error interrupt */
            ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_INTENSET = SERCOM_USART_INT_INTENSET_ERROR_Msk;

            </#if>
            /* Enable Receive Complete interrupt */
            ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_INTENSET = SERCOM_USART_INT_INTENSET_RXC_Msk;
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

    if((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_INTFLAG & SERCOM_USART_INT_INTFLAG_RXC_Msk) == SERCOM_USART_INT_INTFLAG_RXC_Msk)
    {
        receiverStatus = true;
    }

    return receiverStatus;
}

int ${SERCOM_INSTANCE_NAME}_USART_ReadByte( void )
{
    return ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_DATA;
}
</#if>
</#if>

<#if USART_INTERRUPT_MODE = true>
<#if USART_INTENSET_ERROR = true>
void static ${SERCOM_INSTANCE_NAME}_USART_ISR_ERR_Handler( void )
{
    USART_ERROR errorStatus = USART_ERROR_NONE;

    errorStatus = (${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_STATUS &
                  (SERCOM_USART_INT_STATUS_PERR_Msk |
                  SERCOM_USART_INT_STATUS_FERR_Msk |
                  SERCOM_USART_INT_STATUS_BUFOVF_Msk));

    if(errorStatus != USART_ERROR_NONE)
    {
        ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_INTENCLR = SERCOM_USART_INT_INTENCLR_ERROR_Msk;

        if(${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxCallback != NULL)
        {
            ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxCallback(${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxContext);
        }

        /* In case of errors are not cleared by client using ErrorGet API */
        ${SERCOM_INSTANCE_NAME}_USART_ErrorClear();
    }
}

</#if>
<#if USART_RX_ENABLE = true>
void static ${SERCOM_INSTANCE_NAME}_USART_ISR_RX_Handler( void )
{
    if(${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxBusyStatus == true)
    {
        if(${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxProcessedSize < ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxSize)
        {
            ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxBuffer[${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxProcessedSize++] = ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_DATA;

            if(${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxProcessedSize == ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxSize)
            {
                ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxBusyStatus = false;
                ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxSize = 0;
                ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_INTENCLR = SERCOM_USART_INT_INTENCLR_RXC_Msk;

                if(${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxCallback != NULL)
                {
                    ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxCallback(${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxContext);
                }
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
        if(${SERCOM_INSTANCE_NAME?lower_case}USARTObj.txProcessedSize < ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.txSize)
        {
            ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_DATA = ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.txBuffer[${SERCOM_INSTANCE_NAME?lower_case}USARTObj.txProcessedSize++];
        }

        if(${SERCOM_INSTANCE_NAME?lower_case}USARTObj.txProcessedSize >= ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.txSize)
        {
            ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.txBusyStatus = false;
            ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.txSize = 0;
            ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_INTENCLR = SERCOM_USART_INT_INTENCLR_DRE_Msk;

            if(${SERCOM_INSTANCE_NAME?lower_case}USARTObj.txCallback != NULL)
            {
                ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.txCallback(${SERCOM_INSTANCE_NAME?lower_case}USARTObj.txContext);
            }
        }
    }
}
</#if>

void ${SERCOM_INSTANCE_NAME}_USART_InterruptHandler( void )
{
    if(${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_INTENSET != 0)
    {
        <#if USART_TX_ENABLE = true>
        /* Checks for data register empty flag */
        if((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_INTFLAG & SERCOM_USART_INT_INTFLAG_DRE_Msk) == SERCOM_USART_INT_INTFLAG_DRE_Msk)
        {
            ${SERCOM_INSTANCE_NAME}_USART_ISR_TX_Handler();
        }

        </#if>
        <#if USART_RX_ENABLE = true>
        /* Checks for receive complete empty flag */
        if((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_INTFLAG & SERCOM_USART_INT_INTFLAG_RXC_Msk) == SERCOM_USART_INT_INTFLAG_RXC_Msk)
        {
            ${SERCOM_INSTANCE_NAME}_USART_ISR_RX_Handler();
        }

        </#if>
        <#if USART_INTENSET_ERROR = true>
        /* Checks for error flag */
        if((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_INTFLAG & SERCOM_USART_INT_INTFLAG_ERROR_Msk) == SERCOM_USART_INT_INTFLAG_ERROR_Msk)
        {
            ${SERCOM_INSTANCE_NAME}_USART_ISR_ERR_Handler();
        }
        </#if>
    }
}
</#if>
