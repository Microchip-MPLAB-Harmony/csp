/*******************************************************************************
  ${FLEXCOM_INSTANCE_NAME} USART PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${FLEXCOM_INSTANCE_NAME?lower_case}_usart.c

  Summary:
    ${FLEXCOM_INSTANCE_NAME} USART PLIB Implementation File

  Description
    This file defines the interface to the ${FLEXCOM_INSTANCE_NAME} USART peripheral library. This
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
#include "plib_${FLEXCOM_INSTANCE_NAME?lower_case}_${FLEXCOM_MODE?lower_case}.h"

<#--Implementation-->
// *****************************************************************************
// *****************************************************************************
// Section: ${FLEXCOM_INSTANCE_NAME} ${FLEXCOM_MODE} Implementation
// *****************************************************************************
// *****************************************************************************
<#if USART_INTERRUPT_MODE == true>

FLEXCOM_USART_OBJECT ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj;

void static ${FLEXCOM_INSTANCE_NAME}_USART_ISR_RX_Handler( void )
{
    if(${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxBusyStatus == true)
    {
        while((FLEX_US_CSR_RXRDY_Msk == (${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_CSR & FLEX_US_CSR_RXRDY_Msk)) && (${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxSize > ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxProcessedSize) )
        {
            ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxBuffer[${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxProcessedSize++] = (${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_RHR & FLEX_US_RHR_RXCHR_Msk);
        }

        /* Check if the buffer is done */
        if(${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxProcessedSize >= ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxSize)
        {
            ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxBusyStatus = false;

            /* Disable Read, Overrun, Parity and Framing error interrupts */
            ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_IDR = (FLEX_US_IDR_RXRDY_Msk | FLEX_US_IDR_FRAME_Msk | FLEX_US_IDR_PARE_Msk | FLEX_US_IDR_OVRE_Msk);

            if(${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxCallback != NULL)
            {
                ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxCallback(${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxContext);
            }
        }
    }
    else
    {
        /* Nothing to process */
        ;
    }

    return;
}

void static ${FLEXCOM_INSTANCE_NAME}_USART_ISR_TX_Handler( void )
{
    if(${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txBusyStatus == true)
    {
        while((FLEX_US_CSR_TXEMPTY_Msk == (${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_CSR & FLEX_US_CSR_TXEMPTY_Msk)) && (${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txSize > ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txProcessedSize) )
        {
            ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_THR = ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txBuffer[${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txProcessedSize++];
        }

        /* Check if the buffer is done */
        if(${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txProcessedSize >= ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txSize)
        {
            ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txBusyStatus = false;
            ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_IDR = FLEX_US_IDR_TXEMPTY_Msk;

            if(${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txCallback != NULL)
            {
                ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txCallback(${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txContext);
            }
        }
    }
    else
    {
        /* Nothing to process */
        ;
    }

    return;
}

void ${FLEXCOM_INSTANCE_NAME}_InterruptHandler( void )
{
    /* Channel status */
    uint32_t channelStatus = ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_CSR;
    <#if USE_USART_RX_DMA>
    if ((channelStatus & FLEX_US_CSR_ENDRX_Msk) == FLEX_US_CSR_ENDRX_Msk)
    {
        if( ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxDmaCallback != NULL )
        {
            ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxDmaCallback(USART_DMA_TRANSFER_EVENT_COMPLETE, ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxDmaCallback);
        }
        ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_IDR = FLEX_US_IDR_ENDRX_Msk;
    }
    </#if>

    <#if USE_USART_TX_DMA>
    if ((channelStatus & FLEX_US_CSR_ENDTX_Msk) == FLEX_US_CSR_ENDTX_Msk)
    {
        if( ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txDmaCallback != NULL )
        {
            ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txDmaCallback(USART_DMA_TRANSFER_EVENT_COMPLETE, ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txDmaCallback);
        }
        ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_IDR = FLEX_US_IDR_ENDTX_Msk;
    }
    </#if>

    /* Error status */
    uint32_t errorStatus = (channelStatus & (FLEX_US_CSR_OVRE_Msk | FLEX_US_CSR_FRAME_Msk | FLEX_US_CSR_PARE_Msk));

    if(errorStatus != 0)
    {
        ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxBusyStatus = false;

        /* Disable Read, Overrun, Parity and Framing error interrupts */
        ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_IDR = (FLEX_US_IDR_RXRDY_Msk | FLEX_US_IDR_FRAME_Msk | FLEX_US_IDR_PARE_Msk | FLEX_US_IDR_OVRE_Msk);

        /* Client must call ${FLEXCOM_INSTANCE_NAME}_USART_ErrorGet() function to clear the errors */

        /* USART errors are normally associated with the receiver, hence calling
         * receiver context */
        if( ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxCallback != NULL )
        {
            ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxCallback(${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxContext);
        }
    }

    /* Receiver status */
    if(FLEX_US_CSR_RXRDY_Msk == (channelStatus & FLEX_US_CSR_RXRDY_Msk))
    {
        ${FLEXCOM_INSTANCE_NAME}_USART_ISR_RX_Handler();
    }

    /* Transmitter status */
    if(FLEX_US_CSR_TXEMPTY_Msk == (channelStatus & FLEX_US_CSR_TXEMPTY_Msk))
    {
        ${FLEXCOM_INSTANCE_NAME}_USART_ISR_TX_Handler();
    }

    return;
}

</#if>

void static ${FLEXCOM_INSTANCE_NAME}_USART_ErrorClear( void )
{
    uint8_t dummyData = 0u;

    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_CR = FLEX_US_CR_RSTSTA_Msk;

    /* Flush existing error bytes from the RX FIFO */
    while( FLEX_US_CSR_RXRDY_Msk == (${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_CSR& FLEX_US_CSR_RXRDY_Msk) )
    {
        dummyData = (${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_RHR& FLEX_US_RHR_RXCHR_Msk);
    }

    /* Ignore the warning */
    (void)dummyData;

    return;
}

void ${FLEXCOM_INSTANCE_NAME}_USART_Initialize( void )
{
    /* Set FLEXCOM USART operating mode */
    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_MR = FLEX_MR_OPMODE_USART;

    /* Reset ${FLEXCOM_INSTANCE_NAME} USART */
    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_CR = (FLEX_US_CR_RSTRX_Msk | FLEX_US_CR_RSTTX_Msk | FLEX_US_CR_RSTSTA_Msk);

    /* Enable ${FLEXCOM_INSTANCE_NAME} USART */
    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_CR = (FLEX_US_CR_TXEN_Msk | FLEX_US_CR_RXEN_Msk);

    /* Configure ${FLEXCOM_INSTANCE_NAME} USART mode */
    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_MR = ((FLEX_US_MR_USCLKS_${FLEXCOM_USART_MR_USCLKS}) ${(FLEX_USART_MR_MODE9 == true)?then('| FLEX_US_MR_MODE9_Msk', '| FLEX_US_MR_CHRL${FLEX_USART_MR_CHRL}')} | FLEX_US_MR_PAR_${FLEX_USART_MR_PAR} | FLEX_US_MR_NBSTOP${FLEX_USART_MR_NBSTOP} | (${FLEXCOM_USART_MR_OVER} << FLEX_US_MR_OVER_Pos));

    /* Configure ${FLEXCOM_INSTANCE_NAME} USART Baud Rate */
    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_BRGR = FLEX_US_BRGR_CD(${BRG_VALUE});
<#if USART_INTERRUPT_MODE == true>

    /* Initialize instance object */
    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxBuffer = NULL;
    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxSize = 0;
    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxProcessedSize = 0;
    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxBusyStatus = false;
    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxCallback = NULL;
    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txBuffer = NULL;
    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txSize = 0;
    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txProcessedSize = 0;
    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txBusyStatus = false;
    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txCallback = NULL;
</#if>

    return;
}

FLEXCOM_USART_ERROR ${FLEXCOM_INSTANCE_NAME}_USART_ErrorGet( void )
{
    FLEXCOM_USART_ERROR errors = FLEXCOM_USART_ERROR_NONE;
    uint32_t status = ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_CSR;

    /* Collect all errors */
    if(status & FLEX_US_CSR_OVRE_Msk)
    {
        errors = FLEXCOM_USART_ERROR_OVERRUN;
    }
    if(status & FLEX_US_CSR_PARE_Msk)
    {
        errors |= FLEXCOM_USART_ERROR_PARITY;
    }
    if(status & FLEX_US_CSR_FRAME_Msk)
    {
        errors |= FLEXCOM_USART_ERROR_FRAMING;
    }

    if(errors != FLEXCOM_USART_ERROR_NONE)
    {
        ${FLEXCOM_INSTANCE_NAME}_USART_ErrorClear();
    }

    /* All errors are cleared, but send the previous error state */
    return errors;
}

bool ${FLEXCOM_INSTANCE_NAME}_USART_SerialSetup( FLEXCOM_USART_SERIAL_SETUP *setup, uint32_t srcClkFreq )
{
    uint32_t baud = 0;
    uint32_t brgVal = 0;
    uint32_t overSampVal = 0;
    uint32_t usartMode;
    bool status = false;

<#if USART_INTERRUPT_MODE == true>
    if((${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxBusyStatus == true) || (${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txBusyStatus == true))
    {
        /* Transaction is in progress, so return without updating settings */
        return false;
    }

</#if>
    if (setup != NULL)
    {
        baud = setup->baudRate;
        if(srcClkFreq == 0)
        {
            srcClkFreq = ${FLEXCOM_INSTANCE_NAME}_USART_FrequencyGet();
        }

        /* Calculate BRG value */
        if (srcClkFreq >= (16 * baud))
        {
            brgVal = (srcClkFreq / (16 * baud));
        }
        else
        {
            brgVal = (srcClkFreq / (8 * baud));
            overSampVal = (1 << FLEX_US_MR_OVER_Pos) & FLEX_US_MR_OVER_Msk;
        }

        /* Configure ${FLEXCOM_INSTANCE_NAME} USART mode */
        usartMode = ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_MR;
        usartMode &= ~(FLEX_US_MR_CHRL_Msk | FLEX_US_MR_MODE9_Msk | FLEX_US_MR_PAR_Msk | FLEX_US_MR_NBSTOP_Msk | FLEX_US_MR_OVER_Msk);
        ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_MR = usartMode | ((uint32_t)setup->dataWidth | (uint32_t)setup->parity | (uint32_t)setup->stopBits | overSampVal);

        /* Configure ${FLEXCOM_INSTANCE_NAME} USART Baud Rate */
        ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_BRGR = FLEX_US_BRGR_CD(brgVal);
        status = true;
    }

    return status;
}

bool ${FLEXCOM_INSTANCE_NAME}_USART_Read( void *buffer, const size_t size )
{
    bool status = false;
<#if USART_INTERRUPT_MODE == false>
    uint32_t errorStatus = 0;
    size_t processedSize = 0;
</#if>
    uint8_t * lBuffer = (uint8_t *)buffer;

    if(NULL != lBuffer)
    {
        /* Clear errors before submitting the request.
         * ErrorGet clears errors internally. */
        ${FLEXCOM_INSTANCE_NAME}_USART_ErrorGet();

<#if USART_INTERRUPT_MODE == false>
        while( size > processedSize )
        {
            /* Error status */
            errorStatus = (${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_CSR & (FLEX_US_CSR_OVRE_Msk | FLEX_US_CSR_FRAME_Msk | FLEX_US_CSR_PARE_Msk));

            if(errorStatus != 0)
            {
                break;
            }

            if(FLEX_US_CSR_RXRDY_Msk == (${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_CSR & FLEX_US_CSR_RXRDY_Msk))
            {
                *lBuffer++ = (${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_RHR& FLEX_US_RHR_RXCHR_Msk);
                processedSize++;
            }
        }

        if(size == processedSize)
        {
            status = true;
        }

<#else>
        /* Check if receive request is in progress */
        if(${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxBusyStatus == false)
        {
            ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxBuffer = lBuffer;
            ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxSize = size;
            ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxProcessedSize = 0;
            ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxBusyStatus = true;
            status = true;

            /* Enable Read, Overrun, Parity and Framing error interrupts */
            ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_IER = (FLEX_US_IER_RXRDY_Msk | FLEX_US_IER_FRAME_Msk | FLEX_US_IER_PARE_Msk | FLEX_US_IER_OVRE_Msk);
        }
</#if>
    }

    return status;
}

bool ${FLEXCOM_INSTANCE_NAME}_USART_Write( void *buffer, const size_t size )
{
    bool status = false;
<#if USART_INTERRUPT_MODE == false>
    size_t processedSize = 0;
</#if>
    uint8_t * lBuffer = (uint8_t *)buffer;

    if(NULL != lBuffer)
    {
<#if USART_INTERRUPT_MODE == false>
        while( size > processedSize )
        {
            if(FLEX_US_CSR_TXEMPTY_Msk == (${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_CSR& FLEX_US_CSR_TXEMPTY_Msk))
            {
                ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_THR = (FLEX_US_THR_TXCHR(*lBuffer++) & FLEX_US_THR_TXCHR_Msk);
                processedSize++;
            }
        }

        status = true;
<#else>
        /* Check if transmit request is in progress */
        if(${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txBusyStatus == false)
        {
            ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txBuffer = lBuffer;
            ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txSize = size;
            ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txProcessedSize = 0;
            ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txBusyStatus = true;
            status = true;

            /* Initiate the transfer by sending first byte */
            if(FLEX_US_CSR_TXEMPTY_Msk == (${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_CSR& FLEX_US_CSR_TXEMPTY_Msk))
            {
                ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_THR = (FLEX_US_THR_TXCHR(*lBuffer) & FLEX_US_THR_TXCHR_Msk);
                ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txProcessedSize++;
            }

            ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_IER = FLEX_US_IER_TXEMPTY_Msk;
        }
</#if>
    }

    return status;
}

<#if USART_INTERRUPT_MODE == true>
void ${FLEXCOM_INSTANCE_NAME}_USART_WriteCallbackRegister( FLEXCOM_USART_CALLBACK callback, uintptr_t context )
{
    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txCallback = callback;
    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txContext = context;
}

void ${FLEXCOM_INSTANCE_NAME}_USART_ReadCallbackRegister( FLEXCOM_USART_CALLBACK callback, uintptr_t context )
{
    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxCallback = callback;
    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxContext = context;
}

bool ${FLEXCOM_INSTANCE_NAME}_USART_WriteIsBusy( void )
{
    return ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txBusyStatus;
}

bool ${FLEXCOM_INSTANCE_NAME}_USART_ReadIsBusy( void )
{
    return ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxBusyStatus;
}

size_t ${FLEXCOM_INSTANCE_NAME}_USART_WriteCountGet( void )
{
    return ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txProcessedSize;
}

size_t ${FLEXCOM_INSTANCE_NAME}_USART_ReadCountGet( void )
{
    return ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxProcessedSize;
}

</#if>
<#if USART_INTERRUPT_MODE == false>
uint8_t ${FLEXCOM_INSTANCE_NAME}_ReadByte(void)
{
    return(${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_RHR & FLEX_US_RHR_RXCHR_Msk);
}

void ${FLEXCOM_INSTANCE_NAME}_WriteByte(uint8_t data)
{
    while ((FLEX_US_CSR_TXEMPTY_Msk == (${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_CSR & FLEX_US_CSR_TXEMPTY_Msk)) == 0);
    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_THR = (FLEX_US_THR_TXCHR(data) & FLEX_US_THR_TXCHR_Msk);
}

void inline ${FLEXCOM_INSTANCE_NAME}_Sync(void)
{
    while ((FLEX_US_CSR_TXEMPTY_Msk == (${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_CSR & FLEX_US_CSR_TXEMPTY_Msk)) == 0);
}

bool ${FLEXCOM_INSTANCE_NAME}_USART_TransmitterIsReady( void )
{
    bool status = false;

    if(FLEX_US_CSR_TXEMPTY_Msk == (${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_CSR& FLEX_US_CSR_TXEMPTY_Msk))
    {
        status = true;
    }

    return status;
}

bool ${FLEXCOM_INSTANCE_NAME}_USART_ReceiverIsReady( void )
{
    bool status = false;

    if(FLEX_US_CSR_RXRDY_Msk == (${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_CSR& FLEX_US_CSR_RXRDY_Msk))
    {
        status = true;
    }

    return status;
}

</#if>

<#if (USE_USART_TX_DMA )>
void ${FLEXCOM_INSTANCE_NAME}_USART_DmaTransmitCallbackRegister( FLEXCOM_USART_DMA_CALLBACK callback, uintptr_t context )
{
    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txDmaCallback = callback;
    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txDmaContext = context;
}

void ${FLEXCOM_INSTANCE_NAME}_USART_DMAWrite( void *buffer, const size_t size )
{
    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_TPR = (uint32_t) buffer;
    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_TCR = (uint32_t) size;
    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_PTCR = FLEX_US_PTCR_TXTEN_Msk;
    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_IER = FLEX_US_IER_ENDTX_Msk;
}
</#if>

<#if (USE_USART_RX_DMA )>
void ${FLEXCOM_INSTANCE_NAME}_USART_DmaReceiveCallbackRegister( FLEXCOM_USART_DMA_CALLBACK callback, uintptr_t context )
{
    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxDmaCallback = callback;
    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxDmaContext = context;
}

void ${FLEXCOM_INSTANCE_NAME}_USART_DMARead( void *buffer, const size_t size )
{
    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_RPR = (uint32_t) buffer;
    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_RCR = (uint32_t) size;
    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_PTCR = FLEX_US_PTCR_RXTEN_Msk;
    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_IER = FLEX_US_IER_ENDRX_Msk;
}
</#if>