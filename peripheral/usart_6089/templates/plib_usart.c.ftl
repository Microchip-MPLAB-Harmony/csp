/*******************************************************************************
  ${USART_INSTANCE_NAME} PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${USART_INSTANCE_NAME?lower_case}.c

  Summary:
    ${USART_INSTANCE_NAME} PLIB Implementation File

  Description:
    None

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

#include "device.h"
#include "plib_${USART_INSTANCE_NAME?lower_case}.h"

<#--Implementation-->
// *****************************************************************************
// *****************************************************************************
// Section: ${USART_INSTANCE_NAME} Implementation
// *****************************************************************************
// *****************************************************************************
<#if USART_INTERRUPT_MODE == true>

USART_OBJECT ${USART_INSTANCE_NAME?lower_case}Obj;

void static ${USART_INSTANCE_NAME}_ISR_RX_Handler( void )
{
    if(${USART_INSTANCE_NAME?lower_case}Obj.rxBusyStatus == true)
    {
        while((US_CSR_RXRDY_Msk == (${USART_INSTANCE_NAME}_REGS->US_CSR& US_CSR_RXRDY_Msk)) && (${USART_INSTANCE_NAME?lower_case}Obj.rxSize > ${USART_INSTANCE_NAME?lower_case}Obj.rxProcessedSize) )
        {
            ${USART_INSTANCE_NAME?lower_case}Obj.rxBuffer[${USART_INSTANCE_NAME?lower_case}Obj.rxProcessedSize++] = (${USART_INSTANCE_NAME}_REGS->US_RHR& US_RHR_RXCHR_Msk);
        }

        /* Check if the buffer is done */
        if(${USART_INSTANCE_NAME?lower_case}Obj.rxProcessedSize >= ${USART_INSTANCE_NAME?lower_case}Obj.rxSize)
        {

            ${USART_INSTANCE_NAME?lower_case}Obj.rxBusyStatus = false;

            /* Disable Read, Overrun, Parity and Framing error interrupts */
            ${USART_INSTANCE_NAME}_REGS->US_IDR = (US_IDR_RXRDY_Msk | US_IDR_USART_LIN_FRAME_Msk | US_IDR_USART_LIN_PARE_Msk | US_IDR_OVRE_Msk);

            if(${USART_INSTANCE_NAME?lower_case}Obj.rxCallback != NULL)
            {
                ${USART_INSTANCE_NAME?lower_case}Obj.rxCallback(${USART_INSTANCE_NAME?lower_case}Obj.rxContext);
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

void static ${USART_INSTANCE_NAME}_ISR_TX_Handler( void )
{
    if(${USART_INSTANCE_NAME?lower_case}Obj.txBusyStatus == true)
    {
        while((US_CSR_TXEMPTY_Msk == (${USART_INSTANCE_NAME}_REGS->US_CSR& US_CSR_TXEMPTY_Msk)) && (${USART_INSTANCE_NAME?lower_case}Obj.txSize > ${USART_INSTANCE_NAME?lower_case}Obj.txProcessedSize) )
        {
            ${USART_INSTANCE_NAME}_REGS->US_THR|= ${USART_INSTANCE_NAME?lower_case}Obj.txBuffer[${USART_INSTANCE_NAME?lower_case}Obj.txProcessedSize++];
        }

        /* Check if the buffer is done */
        if(${USART_INSTANCE_NAME?lower_case}Obj.txProcessedSize >= ${USART_INSTANCE_NAME?lower_case}Obj.txSize)
        {
            ${USART_INSTANCE_NAME?lower_case}Obj.txBusyStatus = false;
            ${USART_INSTANCE_NAME}_REGS->US_IDR = US_IDR_TXEMPTY_Msk;

            if(${USART_INSTANCE_NAME?lower_case}Obj.txCallback != NULL)
            {
                ${USART_INSTANCE_NAME?lower_case}Obj.txCallback(${USART_INSTANCE_NAME?lower_case}Obj.txContext);
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

void ${USART_INSTANCE_NAME}_InterruptHandler( void )
{
    /* Error status */
    uint32_t errorStatus = (${USART_INSTANCE_NAME}_REGS->US_CSR & (US_CSR_OVRE_Msk | US_CSR_USART_LIN_FRAME_Msk | US_CSR_USART_LIN_PARE_Msk));

    if(errorStatus != 0)
    {
        /* Client must call USARTx_ErrorGet() function to clear the errors */

        /* Disable Read, Overrun, Parity and Framing error interrupts */
        ${USART_INSTANCE_NAME}_REGS->US_IDR = (US_IDR_RXRDY_Msk | US_IDR_USART_LIN_FRAME_Msk | US_IDR_USART_LIN_PARE_Msk | US_IDR_OVRE_Msk);

        ${USART_INSTANCE_NAME?lower_case}Obj.rxBusyStatus = false;

        /* USART errors are normally associated with the receiver, hence calling
         * receiver callback */
        if( ${USART_INSTANCE_NAME?lower_case}Obj.rxCallback != NULL )
        {
            ${USART_INSTANCE_NAME?lower_case}Obj.rxCallback(${USART_INSTANCE_NAME?lower_case}Obj.rxContext);
        }
    }

    /* Receiver status */
    if(US_CSR_RXRDY_Msk == (${USART_INSTANCE_NAME}_REGS->US_CSR & US_CSR_RXRDY_Msk))
    {
        ${USART_INSTANCE_NAME}_ISR_RX_Handler();
    }

    /* Transmitter status */
    if(US_CSR_TXRDY_Msk == (${USART_INSTANCE_NAME}_REGS->US_CSR & US_CSR_TXRDY_Msk))
    {
        ${USART_INSTANCE_NAME}_ISR_TX_Handler();
    }

    return;
}

</#if>

void static ${USART_INSTANCE_NAME}_ErrorClear( void )
{
    uint8_t dummyData = 0u;

    ${USART_INSTANCE_NAME}_REGS->US_CR|= US_CR_RSTSTA_Msk;

    /* Flush existing error bytes from the RX FIFO */
    while( US_CSR_RXRDY_Msk == (${USART_INSTANCE_NAME}_REGS->US_CSR& US_CSR_RXRDY_Msk) )
    {
        dummyData = (${USART_INSTANCE_NAME}_REGS->US_RHR& US_RHR_RXCHR_Msk);
    }

    /* Ignore the warning */
    (void)dummyData;

    return;
}

void ${USART_INSTANCE_NAME}_Initialize( void )
{
    /* Reset ${USART_INSTANCE_NAME} */
    ${USART_INSTANCE_NAME}_REGS->US_CR = (US_CR_RSTRX_Msk | US_CR_RSTTX_Msk | US_CR_RSTSTA_Msk);

    /* Enable ${USART_INSTANCE_NAME} */
    ${USART_INSTANCE_NAME}_REGS->US_CR = (US_CR_TXEN_Msk | US_CR_RXEN_Msk);

    /* Configure ${USART_INSTANCE_NAME} mode */
    <#if USART_MR_MODE9 == true>
    ${USART_INSTANCE_NAME}_REGS->US_MR = (US_MR_USCLKS_${USART_CLK_SRC} | US_MR_USART_MODE9_Msk | US_MR_USART_PAR_${USART_MR_PAR} | US_MR_USART_NBSTOP_${USART_MR_NBSTOP} | (${USART_MR_OVER?string} << US_MR_USART_OVER_Pos));
    <#else>
    ${USART_INSTANCE_NAME}_REGS->US_MR = (US_MR_USCLKS_${USART_CLK_SRC} | US_MR_CHRL_${USART_MR_CHRL} | US_MR_USART_PAR_${USART_MR_PAR} | US_MR_USART_NBSTOP_${USART_MR_NBSTOP} | (${USART_MR_OVER?string} << US_MR_USART_OVER_Pos));
    </#if>

    /* Configure ${USART_INSTANCE_NAME} Baud Rate */
    ${USART_INSTANCE_NAME}_REGS->US_BRGR = US_BRGR_CD(${BRG_VALUE});
<#if USART_INTERRUPT_MODE == true>

    /* Initialize instance object */
    ${USART_INSTANCE_NAME?lower_case}Obj.rxBuffer = NULL;
    ${USART_INSTANCE_NAME?lower_case}Obj.rxSize = 0;
    ${USART_INSTANCE_NAME?lower_case}Obj.rxProcessedSize = 0;
    ${USART_INSTANCE_NAME?lower_case}Obj.rxBusyStatus = false;
    ${USART_INSTANCE_NAME?lower_case}Obj.rxCallback = NULL;
    ${USART_INSTANCE_NAME?lower_case}Obj.txBuffer = NULL;
    ${USART_INSTANCE_NAME?lower_case}Obj.txSize = 0;
    ${USART_INSTANCE_NAME?lower_case}Obj.txProcessedSize = 0;
    ${USART_INSTANCE_NAME?lower_case}Obj.txBusyStatus = false;
    ${USART_INSTANCE_NAME?lower_case}Obj.txCallback = NULL;
</#if>

    return;
}

USART_ERROR ${USART_INSTANCE_NAME}_ErrorGet( void )
{
    USART_ERROR errors = USART_ERROR_NONE;
    uint32_t status = ${USART_INSTANCE_NAME}_REGS->US_CSR;

    errors = (USART_ERROR)(status & (US_CSR_OVRE_Msk | US_CSR_USART_LIN_PARE_Msk | US_CSR_USART_LIN_FRAME_Msk));

    if(errors != USART_ERROR_NONE)
    {
        ${USART_INSTANCE_NAME}_ErrorClear();
    }

    /* All errors are cleared, but send the previous error state */
    return errors;
}

bool ${USART_INSTANCE_NAME}_SerialSetup( USART_SERIAL_SETUP *setup, uint32_t srcClkFreq )
{
    uint32_t baud = setup->baudRate;
    uint32_t brgVal = 0;
    uint32_t overSampVal = 0;
    uint32_t usartMode;
    bool status = false;

<#if USART_INTERRUPT_MODE == true>
    if((${USART_INSTANCE_NAME?lower_case}Obj.rxBusyStatus == true) || (${USART_INSTANCE_NAME?lower_case}Obj.txBusyStatus == true))
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
            srcClkFreq = ${USART_INSTANCE_NAME}_FrequencyGet();
        }

        /* Calculate BRG value */
        if (srcClkFreq >= (16 * baud))
        {
            brgVal = (srcClkFreq / (16 * baud));
        }
        else
        {
            brgVal = (srcClkFreq / (8 * baud));
            overSampVal = US_MR_USART_OVER(1);
        }

        /* Configure ${USART_INSTANCE_NAME} mode */
        usartMode = ${USART_INSTANCE_NAME}_REGS->US_MR;
        usartMode &= ~(US_MR_CHRL_Msk | US_MR_USART_MODE9_Msk | US_MR_USART_PAR_Msk | US_MR_USART_NBSTOP_Msk | US_MR_USART_OVER_Msk);
        ${USART_INSTANCE_NAME}_REGS->US_MR = usartMode | (setup->dataWidth | setup->parity | setup->stopBits | overSampVal);

        /* Configure ${USART_INSTANCE_NAME} Baud Rate */
        ${USART_INSTANCE_NAME}_REGS->US_BRGR = US_BRGR_CD(brgVal);
        status = true;
    }

    return status;
}

bool ${USART_INSTANCE_NAME}_Read( void *buffer, const size_t size )
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
        ${USART_INSTANCE_NAME}_ErrorGet();

<#if USART_INTERRUPT_MODE == false>
        while( size > processedSize )
        {
            /* Error status */
            errorStatus = (${USART_INSTANCE_NAME}_REGS->US_CSR & (US_CSR_OVRE_Msk | US_CSR_USART_LIN_FRAME_Msk | US_CSR_USART_LIN_PARE_Msk));

            if(errorStatus != 0)
            {
                break;
            }

            if(US_CSR_RXRDY_Msk == (${USART_INSTANCE_NAME}_REGS->US_CSR & US_CSR_RXRDY_Msk))
            {
                *lBuffer++ = (${USART_INSTANCE_NAME}_REGS->US_RHR& US_RHR_RXCHR_Msk);
                processedSize++;
            }
        }

        if(size == processedSize)
        {
            status = true;
        }

<#else>
        /* Check if receive request is in progress */
        if(${USART_INSTANCE_NAME?lower_case}Obj.rxBusyStatus == false)
        {
            ${USART_INSTANCE_NAME?lower_case}Obj.rxBuffer = lBuffer;
            ${USART_INSTANCE_NAME?lower_case}Obj.rxSize = size;
            ${USART_INSTANCE_NAME?lower_case}Obj.rxProcessedSize = 0;
            ${USART_INSTANCE_NAME?lower_case}Obj.rxBusyStatus = true;
            status = true;

            /* Enable Read, Overrun, Parity and Framing error interrupts */
            ${USART_INSTANCE_NAME}_REGS->US_IER = (US_IER_RXRDY_Msk | US_IER_USART_LIN_FRAME_Msk | US_IER_USART_LIN_PARE_Msk | US_IER_OVRE_Msk);
        }
</#if>
    }

    return status;
}

bool ${USART_INSTANCE_NAME}_Write( void *buffer, const size_t size )
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
            if(US_CSR_TXRDY_Msk == (${USART_INSTANCE_NAME}_REGS->US_CSR & US_CSR_TXRDY_Msk))
            {
                ${USART_INSTANCE_NAME}_REGS->US_THR = (US_THR_TXCHR(*lBuffer++) & US_THR_TXCHR_Msk);
                processedSize++;
            }
        }

        status = true;
<#else>
        /* Check if transmit request is in progress */
        if(${USART_INSTANCE_NAME?lower_case}Obj.txBusyStatus == false)
        {
            ${USART_INSTANCE_NAME?lower_case}Obj.txBuffer = lBuffer;
            ${USART_INSTANCE_NAME?lower_case}Obj.txSize = size;
            ${USART_INSTANCE_NAME?lower_case}Obj.txProcessedSize = 0;
            ${USART_INSTANCE_NAME?lower_case}Obj.txBusyStatus = true;
            status = true;

            /* Initiate the transfer by sending first byte */
            if(US_CSR_TXRDY_Msk == (${USART_INSTANCE_NAME}_REGS->US_CSR & US_CSR_TXRDY_Msk))
            {
                ${USART_INSTANCE_NAME}_REGS->US_THR = (US_THR_TXCHR(*lBuffer) & US_THR_TXCHR_Msk);
                ${USART_INSTANCE_NAME?lower_case}Obj.txProcessedSize++;
            }

            ${USART_INSTANCE_NAME}_REGS->US_IER = US_IER_TXEMPTY_Msk;
        }
</#if>
    }

    return status;
}

<#if USART_INTERRUPT_MODE == false>
int ${USART_INSTANCE_NAME}_ReadByte(void)
{
    return(${USART_INSTANCE_NAME}_REGS->US_RHR & US_RHR_RXCHR_Msk);
}

void ${USART_INSTANCE_NAME}_WriteByte(int data)
{
    while ((US_CSR_TXRDY_Msk == (${USART_INSTANCE_NAME}_REGS->US_CSR & US_CSR_TXRDY_Msk)) == 0);

    ${USART_INSTANCE_NAME}_REGS->US_THR = (US_THR_TXCHR(data) & US_THR_TXCHR_Msk);
}

bool ${USART_INSTANCE_NAME}_TransmitterIsReady( void )
{
    if(US_CSR_TXRDY_Msk == (${USART_INSTANCE_NAME}_REGS->US_CSR & US_CSR_TXRDY_Msk))
    {
        return true;
    }

    return false;
}

bool ${USART_INSTANCE_NAME}_TransmitComplete( void )
{
    if(US_CSR_TXEMPTY_Msk == (${USART_INSTANCE_NAME}_REGS->US_CSR & US_CSR_TXEMPTY_Msk))
    {
        return true;
    }

    return false;
}

bool ${USART_INSTANCE_NAME}_ReceiverIsReady( void )
{
    if(US_CSR_RXRDY_Msk == (${USART_INSTANCE_NAME}_REGS->US_CSR & US_CSR_RXRDY_Msk))
    {
        return true;
    }

    return false;
}

</#if>

<#if USART_INTERRUPT_MODE == true>
void ${USART_INSTANCE_NAME}_WriteCallbackRegister( USART_CALLBACK callback, uintptr_t context )
{
    ${USART_INSTANCE_NAME?lower_case}Obj.txCallback = callback;

    ${USART_INSTANCE_NAME?lower_case}Obj.txContext = context;
}

void ${USART_INSTANCE_NAME}_ReadCallbackRegister( USART_CALLBACK callback, uintptr_t context )
{
    ${USART_INSTANCE_NAME?lower_case}Obj.rxCallback = callback;

    ${USART_INSTANCE_NAME?lower_case}Obj.rxContext = context;
}

bool ${USART_INSTANCE_NAME}_WriteIsBusy( void )
{
    return ${USART_INSTANCE_NAME?lower_case}Obj.txBusyStatus;
}

bool ${USART_INSTANCE_NAME}_ReadIsBusy( void )
{
    return ${USART_INSTANCE_NAME?lower_case}Obj.rxBusyStatus;
}

size_t ${USART_INSTANCE_NAME}_WriteCountGet( void )
{
    return ${USART_INSTANCE_NAME?lower_case}Obj.txProcessedSize;
}

size_t ${USART_INSTANCE_NAME}_ReadCountGet( void )
{
    return ${USART_INSTANCE_NAME?lower_case}Obj.rxProcessedSize;
}

</#if>
