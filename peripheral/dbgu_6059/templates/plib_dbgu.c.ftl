/*******************************************************************************
  ${DBGU_INSTANCE_NAME} PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${DBGU_INSTANCE_NAME?lower_case}.c

  Summary:
    ${DBGU_INSTANCE_NAME} PLIB Implementation File

  Description:
    None

*******************************************************************************/

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

#include "device.h"
#include "plib_${DBGU_INSTANCE_NAME?lower_case}.h"

// *****************************************************************************
// *****************************************************************************
// Section: ${DBGU_INSTANCE_NAME} Implementation
// *****************************************************************************
// *****************************************************************************
<#if USART_INTERRUPT_MODE == true>

DBGU_OBJECT ${DBGU_INSTANCE_NAME?lower_case}Obj;

void static ${DBGU_INSTANCE_NAME}_ISR_RX_Handler(void)
{
    if (${DBGU_INSTANCE_NAME?lower_case}Obj.rxBusyStatus == true)
    {
        while ((DBGU_SR_RXRDY_Msk == (${DBGU_INSTANCE_NAME}_REGS->DBGU_SR & DBGU_SR_RXRDY_Msk)) && (${DBGU_INSTANCE_NAME?lower_case}Obj.rxSize > ${DBGU_INSTANCE_NAME?lower_case}Obj.rxProcessedSize) )
        {
            ${DBGU_INSTANCE_NAME?lower_case}Obj.rxBuffer[${DBGU_INSTANCE_NAME?lower_case}Obj.rxProcessedSize++] = (${DBGU_INSTANCE_NAME}_REGS->DBGU_RHR & DBGU_RHR_RXCHR_Msk);
        }

        /* Check if the buffer is done */
        if (${DBGU_INSTANCE_NAME?lower_case}Obj.rxProcessedSize >= ${DBGU_INSTANCE_NAME?lower_case}Obj.rxSize)
        {
            ${DBGU_INSTANCE_NAME?lower_case}Obj.rxBusyStatus = false;

            /* Disable Read, Overrun, Parity and Framing error interrupts */
            ${DBGU_INSTANCE_NAME}_REGS->DBGU_IDR = (DBGU_IDR_RXRDY_Msk | DBGU_IDR_FRAME_Msk | DBGU_IDR_PARE_Msk | DBGU_IDR_OVRE_Msk);

            if (${DBGU_INSTANCE_NAME?lower_case}Obj.rxCallback != NULL)
            {
                ${DBGU_INSTANCE_NAME?lower_case}Obj.rxCallback(${DBGU_INSTANCE_NAME?lower_case}Obj.rxContext);
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

void static ${DBGU_INSTANCE_NAME}_ISR_TX_Handler(void)
{
    if (${DBGU_INSTANCE_NAME?lower_case}Obj.txBusyStatus == true)
    {
        while ((DBGU_SR_TXEMPTY_Msk == (${DBGU_INSTANCE_NAME}_REGS->DBGU_SR & DBGU_SR_TXEMPTY_Msk)) && (${DBGU_INSTANCE_NAME?lower_case}Obj.txSize > ${DBGU_INSTANCE_NAME?lower_case}Obj.txProcessedSize) )
        {
            ${DBGU_INSTANCE_NAME}_REGS->DBGU_THR = ${DBGU_INSTANCE_NAME?lower_case}Obj.txBuffer[${DBGU_INSTANCE_NAME?lower_case}Obj.txProcessedSize++];
        }

        /* Check if the buffer is done */
        if (${DBGU_INSTANCE_NAME?lower_case}Obj.txProcessedSize >= ${DBGU_INSTANCE_NAME?lower_case}Obj.txSize)
        {
            ${DBGU_INSTANCE_NAME?lower_case}Obj.txBusyStatus = false;
            ${DBGU_INSTANCE_NAME}_REGS->DBGU_IDR = DBGU_IDR_TXEMPTY_Msk;

            if (${DBGU_INSTANCE_NAME?lower_case}Obj.txCallback != NULL)
            {
                ${DBGU_INSTANCE_NAME?lower_case}Obj.txCallback(${DBGU_INSTANCE_NAME?lower_case}Obj.txContext);
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

void ${DBGU_INSTANCE_NAME}_InterruptHandler(void)
{
    /* Error status */
    uint32_t errorStatus = (${DBGU_INSTANCE_NAME}_REGS->DBGU_SR & (DBGU_SR_OVRE_Msk | DBGU_SR_FRAME_Msk | DBGU_SR_PARE_Msk));

    if (errorStatus != 0)
    {
        /* Client must call DBGUx_ErrorGet() function to clear the errors */

        /* Disable Read, Overrun, Parity and Framing error interrupts */
        ${DBGU_INSTANCE_NAME}_REGS->DBGU_IDR = (DBGU_IDR_RXRDY_Msk | DBGU_IDR_FRAME_Msk | DBGU_IDR_PARE_Msk | DBGU_IDR_OVRE_Msk);

        ${DBGU_INSTANCE_NAME?lower_case}Obj.rxBusyStatus = false;

        /* DBGU errors are normally associated with the receiver, hence calling
         * receiver callback */
        if (${DBGU_INSTANCE_NAME?lower_case}Obj.rxCallback != NULL)
        {
            ${DBGU_INSTANCE_NAME?lower_case}Obj.rxCallback(${DBGU_INSTANCE_NAME?lower_case}Obj.rxContext);
        }
    }

    /* Receiver status */
    if (DBGU_SR_RXRDY_Msk == (${DBGU_INSTANCE_NAME}_REGS->DBGU_SR & DBGU_SR_RXRDY_Msk))
    {
        ${DBGU_INSTANCE_NAME}_ISR_RX_Handler();
    }

    /* Transmitter status */
    if (DBGU_SR_TXEMPTY_Msk == (${DBGU_INSTANCE_NAME}_REGS->DBGU_SR & DBGU_SR_TXEMPTY_Msk))
    {
        ${DBGU_INSTANCE_NAME}_ISR_TX_Handler();
    }

    return;
}

</#if>

void static ${DBGU_INSTANCE_NAME}_ErrorClear(void)
{
    uint8_t dummyData = 0u;

    ${DBGU_INSTANCE_NAME}_REGS->DBGU_CR = DBGU_CR_RSTSTA_Msk;

    /* Flush existing error bytes from the RX FIFO */
    while (DBGU_SR_RXRDY_Msk == (${DBGU_INSTANCE_NAME}_REGS->DBGU_SR & DBGU_SR_RXRDY_Msk))
    {
        dummyData = (${DBGU_INSTANCE_NAME}_REGS->DBGU_RHR & DBGU_RHR_RXCHR_Msk);
    }

    /* Ignore the warning */
    (void)dummyData;

    return;
}

void ${DBGU_INSTANCE_NAME}_Initialize(void)
{
    /* Reset ${DBGU_INSTANCE_NAME} */
    ${DBGU_INSTANCE_NAME}_REGS->DBGU_CR = (DBGU_CR_RSTRX_Msk | DBGU_CR_RSTTX_Msk | DBGU_CR_RSTSTA_Msk);

    /* Enable ${DBGU_INSTANCE_NAME} */
    ${DBGU_INSTANCE_NAME}_REGS->DBGU_CR = (DBGU_CR_TXEN_Msk | DBGU_CR_RXEN_Msk);

    /* Configure ${DBGU_INSTANCE_NAME} mode */
    ${DBGU_INSTANCE_NAME}_REGS->DBGU_MR = (DBGU_MR_BRSRCCK(${DBGU_CLK_SRC}) | (DBGU_MR_PAR_${DBGU_MR_PAR}) | (${DBGU_MR_FILTER?then(1,0)} << DBGU_MR_FILTER_Pos));

    /* Configure ${DBGU_INSTANCE_NAME} Baud Rate */
    ${DBGU_INSTANCE_NAME}_REGS->DBGU_BRGR = DBGU_BRGR_CD(${BRG_VALUE});
<#if USART_INTERRUPT_MODE == true>

    /* Initialize instance object */
    ${DBGU_INSTANCE_NAME?lower_case}Obj.rxBuffer = NULL;
    ${DBGU_INSTANCE_NAME?lower_case}Obj.rxSize = 0;
    ${DBGU_INSTANCE_NAME?lower_case}Obj.rxProcessedSize = 0;
    ${DBGU_INSTANCE_NAME?lower_case}Obj.rxBusyStatus = false;
    ${DBGU_INSTANCE_NAME?lower_case}Obj.rxCallback = NULL;
    ${DBGU_INSTANCE_NAME?lower_case}Obj.txBuffer = NULL;
    ${DBGU_INSTANCE_NAME?lower_case}Obj.txSize = 0;
    ${DBGU_INSTANCE_NAME?lower_case}Obj.txProcessedSize = 0;
    ${DBGU_INSTANCE_NAME?lower_case}Obj.txBusyStatus = false;
    ${DBGU_INSTANCE_NAME?lower_case}Obj.txCallback = NULL;
</#if>

    return;
}

DBGU_ERROR ${DBGU_INSTANCE_NAME}_ErrorGet(void)
{
    DBGU_ERROR errors = DBGU_ERROR_NONE;
    uint32_t status = ${DBGU_INSTANCE_NAME}_REGS->DBGU_SR;

    errors = (DBGU_ERROR)(status & (DBGU_SR_OVRE_Msk | DBGU_SR_PARE_Msk | DBGU_SR_FRAME_Msk));

    if (errors != DBGU_ERROR_NONE)
    {
        ${DBGU_INSTANCE_NAME}_ErrorClear();
    }

    /* All errors are cleared, but send the previous error state */
    return errors;
}

bool ${DBGU_INSTANCE_NAME}_SerialSetup(DBGU_SERIAL_SETUP *setup, uint32_t srcClkFreq)
{
    bool status = false;
    uint32_t baud = setup->baudRate;
    uint32_t brgVal = 0;
    uint32_t dbguMode;

<#if USART_INTERRUPT_MODE == true>
    if ((${DBGU_INSTANCE_NAME?lower_case}Obj.rxBusyStatus == true) || (${DBGU_INSTANCE_NAME?lower_case}Obj.txBusyStatus == true))
    {
        /* Transaction is in progress, so return without updating settings */
        return false;
    }
</#if>
    if (setup != NULL)
    {
        if (srcClkFreq == 0)
        {
            srcClkFreq = ${DBGU_INSTANCE_NAME}_FrequencyGet();
        }

        /* Calculate BRG value */
        brgVal = srcClkFreq / (16 * baud);

        /* Configure ${DBGU_INSTANCE_NAME} mode */
        dbguMode = ${DBGU_INSTANCE_NAME}_REGS->DBGU_MR;
        dbguMode &= ~DBGU_MR_PAR_Msk;
        ${DBGU_INSTANCE_NAME}_REGS->DBGU_MR = dbguMode | setup->parity ;

        /* Configure ${DBGU_INSTANCE_NAME} Baud Rate */
        ${DBGU_INSTANCE_NAME}_REGS->DBGU_BRGR = DBGU_BRGR_CD(brgVal);

        status = true;
    }

    return status;
}

bool ${DBGU_INSTANCE_NAME}_Read(void *buffer, const size_t size)
{
    bool status = false;
<#if USART_INTERRUPT_MODE == false>
    uint32_t errorStatus = 0;
    size_t processedSize = 0;
</#if>

    uint8_t * lBuffer = (uint8_t *)buffer;

    if (NULL != lBuffer)
    {
        /* Clear errors before submitting the request.
         * ErrorGet clears errors internally. */
        ${DBGU_INSTANCE_NAME}_ErrorGet();

<#if USART_INTERRUPT_MODE == false>
        while (size > processedSize)
        {
            /* Error status */
            errorStatus = (${DBGU_INSTANCE_NAME}_REGS->DBGU_SR & (DBGU_SR_OVRE_Msk | DBGU_SR_FRAME_Msk | DBGU_SR_PARE_Msk));

            if (errorStatus != 0)
            {
                break;
            }

            if (DBGU_SR_RXRDY_Msk == (${DBGU_INSTANCE_NAME}_REGS->DBGU_SR & DBGU_SR_RXRDY_Msk))
            {
                *lBuffer++ = (${DBGU_INSTANCE_NAME}_REGS->DBGU_RHR & DBGU_RHR_RXCHR_Msk);
                processedSize++;
            }
        }

        if (size == processedSize)
        {
            status = true;
        }
<#else>
        /* Check if receive request is in progress */
        if (${DBGU_INSTANCE_NAME?lower_case}Obj.rxBusyStatus == false)
        {
            ${DBGU_INSTANCE_NAME?lower_case}Obj.rxBuffer = lBuffer;
            ${DBGU_INSTANCE_NAME?lower_case}Obj.rxSize = size;
            ${DBGU_INSTANCE_NAME?lower_case}Obj.rxProcessedSize = 0;
            ${DBGU_INSTANCE_NAME?lower_case}Obj.rxBusyStatus = true;
            status = true;

            /* Enable Read, Overrun, Parity and Framing error interrupts */
            ${DBGU_INSTANCE_NAME}_REGS->DBGU_IER = (DBGU_IER_RXRDY_Msk | DBGU_IER_FRAME_Msk | DBGU_IER_PARE_Msk | DBGU_IER_OVRE_Msk);
        }
</#if>
    }

    return status;
}

bool ${DBGU_INSTANCE_NAME}_Write(void *buffer, const size_t size)
{
    bool status = false;
<#if USART_INTERRUPT_MODE == false>
    size_t processedSize = 0;
</#if>
    uint8_t * lBuffer = (uint8_t *)buffer;

    if (NULL != lBuffer)
    {
<#if USART_INTERRUPT_MODE == false>
        while (size > processedSize)
        {
            if (DBGU_SR_TXEMPTY_Msk == (${DBGU_INSTANCE_NAME}_REGS->DBGU_SR & DBGU_SR_TXEMPTY_Msk))
            {
                ${DBGU_INSTANCE_NAME}_REGS->DBGU_THR = (DBGU_THR_TXCHR(*lBuffer++) & DBGU_THR_TXCHR_Msk);
                processedSize++;
            }
        }

        status = true;
<#else>
        /* Check if transmit request is in progress */
        if (${DBGU_INSTANCE_NAME?lower_case}Obj.txBusyStatus == false)
        {
            ${DBGU_INSTANCE_NAME?lower_case}Obj.txBuffer = lBuffer;
            ${DBGU_INSTANCE_NAME?lower_case}Obj.txSize = size;
            ${DBGU_INSTANCE_NAME?lower_case}Obj.txProcessedSize = 0;
            ${DBGU_INSTANCE_NAME?lower_case}Obj.txBusyStatus = true;
            status = true;

            /* Initiate the transfer by sending first byte */
            if (DBGU_SR_TXEMPTY_Msk == (${DBGU_INSTANCE_NAME}_REGS->DBGU_SR & DBGU_SR_TXEMPTY_Msk))
            {
                ${DBGU_INSTANCE_NAME}_REGS->DBGU_THR = (DBGU_THR_TXCHR(*lBuffer) & DBGU_THR_TXCHR_Msk);
                ${DBGU_INSTANCE_NAME?lower_case}Obj.txProcessedSize++;
            }

            ${DBGU_INSTANCE_NAME}_REGS->DBGU_IER = DBGU_IER_TXEMPTY_Msk;
        }
</#if>
    }

    return status;
}

<#if USART_INTERRUPT_MODE == true>
void ${DBGU_INSTANCE_NAME}_WriteCallbackRegister(DBGU_CALLBACK callback, uintptr_t context)
{
    ${DBGU_INSTANCE_NAME?lower_case}Obj.txCallback = callback;

    ${DBGU_INSTANCE_NAME?lower_case}Obj.txContext = context;
}

void ${DBGU_INSTANCE_NAME}_ReadCallbackRegister(DBGU_CALLBACK callback, uintptr_t context)
{
    ${DBGU_INSTANCE_NAME?lower_case}Obj.rxCallback = callback;

    ${DBGU_INSTANCE_NAME?lower_case}Obj.rxContext = context;
}

bool ${DBGU_INSTANCE_NAME}_WriteIsBusy(void)
{
    return ${DBGU_INSTANCE_NAME?lower_case}Obj.txBusyStatus;
}

bool ${DBGU_INSTANCE_NAME}_ReadIsBusy(void)
{
    return ${DBGU_INSTANCE_NAME?lower_case}Obj.rxBusyStatus;
}

size_t ${DBGU_INSTANCE_NAME}_WriteCountGet(void)
{
    return ${DBGU_INSTANCE_NAME?lower_case}Obj.txProcessedSize;
}

size_t ${DBGU_INSTANCE_NAME}_ReadCountGet(void)
{
    return ${DBGU_INSTANCE_NAME?lower_case}Obj.rxProcessedSize;
}

</#if>
<#if USART_INTERRUPT_MODE == false>
uint8_t ${DBGU_INSTANCE_NAME}_ReadByte(void)
{
    return (${DBGU_INSTANCE_NAME}_REGS->DBGU_RHR & DBGU_RHR_RXCHR_Msk);
}

void ${DBGU_INSTANCE_NAME}_WriteByte(uint8_t data)
{
    while ((${DBGU_INSTANCE_NAME}_REGS->DBGU_SR & DBGU_SR_TXEMPTY_Msk) != DBGU_SR_TXEMPTY_Msk);
    ${DBGU_INSTANCE_NAME}_REGS->DBGU_THR = (DBGU_THR_TXCHR(data) & DBGU_THR_TXCHR_Msk);
}

bool ${DBGU_INSTANCE_NAME}_TransmitterIsReady(void)
{
    return ((${DBGU_INSTANCE_NAME}_REGS->DBGU_SR & DBGU_SR_TXEMPTY_Msk) == DBGU_SR_TXEMPTY_Msk);
}

bool ${DBGU_INSTANCE_NAME}_ReceiverIsReady(void)
{
    return ((${DBGU_INSTANCE_NAME}_REGS->DBGU_SR & DBGU_SR_RXRDY_Msk) == DBGU_SR_RXRDY_Msk);
}

</#if>
