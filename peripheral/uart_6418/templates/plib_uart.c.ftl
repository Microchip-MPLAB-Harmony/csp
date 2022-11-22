/*******************************************************************************
  ${UART_INSTANCE_NAME} PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${UART_INSTANCE_NAME?lower_case}.c

  Summary:
    ${UART_INSTANCE_NAME} PLIB Implementation File

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
#include "plib_${UART_INSTANCE_NAME?lower_case}.h"
<#if core.CoreSysIntFile == true>
#include "interrupts.h"
</#if>

<#--Implementation-->
// *****************************************************************************
// *****************************************************************************
// Section: ${UART_INSTANCE_NAME} Implementation
// *****************************************************************************
// *****************************************************************************
<#assign useUARTRxDMA = false>
<#assign useUARTTxDMA = false>
<#if UART_INTERRUPT_MODE_ENABLE == true>
<#if USE_UART_RECEIVE_DMA??>
<#assign useUARTRxDMA = USE_UART_RECEIVE_DMA>
</#if>
<#if USE_UART_TRANSMIT_DMA??>
<#assign useUARTTxDMA = USE_UART_TRANSMIT_DMA>
</#if>

static UART_OBJECT ${UART_INSTANCE_NAME?lower_case}Obj;

<#if useUARTRxDMA == false>
static void ${UART_INSTANCE_NAME}_ISR_RX_Handler( void )
{
    if(${UART_INSTANCE_NAME?lower_case}Obj.rxBusyStatus == true)
    {
        while((UART_SR_RXRDY_Msk == (${UART_INSTANCE_NAME}_REGS->UART_SR& UART_SR_RXRDY_Msk)) && (${UART_INSTANCE_NAME?lower_case}Obj.rxSize > ${UART_INSTANCE_NAME?lower_case}Obj.rxProcessedSize) )
        {
            ${UART_INSTANCE_NAME?lower_case}Obj.rxBuffer[${UART_INSTANCE_NAME?lower_case}Obj.rxProcessedSize] = (uint8_t)(${UART_INSTANCE_NAME}_REGS->UART_RHR& UART_RHR_RXCHR_Msk);
            ${UART_INSTANCE_NAME?lower_case}Obj.rxProcessedSize++;
		}

        /* Check if the buffer is done */
        if(${UART_INSTANCE_NAME?lower_case}Obj.rxProcessedSize >= ${UART_INSTANCE_NAME?lower_case}Obj.rxSize)
        {
            ${UART_INSTANCE_NAME?lower_case}Obj.rxBusyStatus = false;

            /* Disable Read, Overrun, Parity and Framing error interrupts */
            ${UART_INSTANCE_NAME}_REGS->UART_IDR = (UART_IDR_RXRDY_Msk | UART_IDR_FRAME_Msk | UART_IDR_PARE_Msk | UART_IDR_OVRE_Msk);

            if(${UART_INSTANCE_NAME?lower_case}Obj.rxCallback != NULL)
            {
                ${UART_INSTANCE_NAME?lower_case}Obj.rxCallback(${UART_INSTANCE_NAME?lower_case}Obj.rxContext);
            }
        }
    }
    else
    {
        /* Nothing to process */
        ;
    }
}

</#if>
<#if useUARTTxDMA == false>
static void ${UART_INSTANCE_NAME}_ISR_TX_Handler( void )
{
    if(${UART_INSTANCE_NAME?lower_case}Obj.txBusyStatus == true)
    {
        while((UART_SR_TXRDY_Msk == (${UART_INSTANCE_NAME}_REGS->UART_SR & UART_SR_TXRDY_Msk)) && (${UART_INSTANCE_NAME?lower_case}Obj.txSize > ${UART_INSTANCE_NAME?lower_case}Obj.txProcessedSize) )
        {
            ${UART_INSTANCE_NAME}_REGS->UART_THR|= ${UART_INSTANCE_NAME?lower_case}Obj.txBuffer[${UART_INSTANCE_NAME?lower_case}Obj.txProcessedSize];
			${UART_INSTANCE_NAME?lower_case}Obj.txProcessedSize++;
        }

        /* Check if the buffer is done */
        if(${UART_INSTANCE_NAME?lower_case}Obj.txProcessedSize >= ${UART_INSTANCE_NAME?lower_case}Obj.txSize)
        {
            ${UART_INSTANCE_NAME?lower_case}Obj.txBusyStatus = false;
            ${UART_INSTANCE_NAME}_REGS->UART_IDR = UART_IDR_TXEMPTY_Msk;

            if(${UART_INSTANCE_NAME?lower_case}Obj.txCallback != NULL)
            {
                ${UART_INSTANCE_NAME?lower_case}Obj.txCallback(${UART_INSTANCE_NAME?lower_case}Obj.txContext);
            }
        }
    }
    else
    {
        /* Nothing to process */
        ;
    }
}

</#if>
void ${UART_INSTANCE_NAME}_InterruptHandler( void )
{
    /* Error status */
    uint32_t errorStatusx = (${UART_INSTANCE_NAME}_REGS->UART_SR & (UART_SR_OVRE_Msk | UART_SR_FRAME_Msk | UART_SR_PARE_Msk));

    if(errorStatusx != 0U)
    {
        /* Client must call UARTx_ErrorGet() function to clear the errors */

        /* Disable Read, Overrun, Parity and Framing error interrupts */
        <#if useUARTRxDMA == true>
        ${UART_INSTANCE_NAME}_REGS->UART_PTCR = UART_PTCR_RXTDIS_Msk;
        ${UART_INSTANCE_NAME}_REGS->UART_IDR = (UART_IDR_ENDRX_Msk | UART_IDR_FRAME_Msk | UART_IDR_PARE_Msk | UART_IDR_OVRE_Msk);
        <#else>
        ${UART_INSTANCE_NAME}_REGS->UART_IDR = (UART_IDR_RXRDY_Msk | UART_IDR_FRAME_Msk | UART_IDR_PARE_Msk | UART_IDR_OVRE_Msk);
        </#if>

        ${UART_INSTANCE_NAME?lower_case}Obj.rxBusyStatus = false;

        /* UART errors are normally associated with the receiver, hence calling
         * receiver callback */
        if( ${UART_INSTANCE_NAME?lower_case}Obj.rxCallback != NULL )
        {
            ${UART_INSTANCE_NAME?lower_case}Obj.rxCallback(${UART_INSTANCE_NAME?lower_case}Obj.rxContext);
        }
    }

    <#if useUARTRxDMA == true>
    if ((${UART_INSTANCE_NAME}_REGS->UART_PTSR & UART_PTSR_RXTEN_Msk) && (${UART_INSTANCE_NAME}_REGS->UART_SR & UART_SR_ENDRX_Msk))
    {
        if(${UART_INSTANCE_NAME?lower_case}Obj.rxBusyStatus == true)
        {
            ${UART_INSTANCE_NAME?lower_case}Obj.rxBusyStatus = false;
            ${UART_INSTANCE_NAME}_REGS->UART_PTCR = UART_PTCR_RXTDIS_Msk;
            ${UART_INSTANCE_NAME}_REGS->UART_IDR = (UART_IDR_ENDRX_Msk | UART_IDR_FRAME_Msk | UART_IDR_PARE_Msk | UART_IDR_OVRE_Msk);

            if( ${UART_INSTANCE_NAME?lower_case}Obj.rxCallback != NULL )
            {
                ${UART_INSTANCE_NAME?lower_case}Obj.rxCallback(${UART_INSTANCE_NAME?lower_case}Obj.rxContext);
            }
        }
    }
    <#else>
    /* Receiver status */
    if(UART_SR_RXRDY_Msk == (${UART_INSTANCE_NAME}_REGS->UART_SR & UART_SR_RXRDY_Msk))
    {
        ${UART_INSTANCE_NAME}_ISR_RX_Handler();
    }
    </#if>

    <#if useUARTTxDMA == true>
    if ((${UART_INSTANCE_NAME}_REGS->UART_PTSR & UART_PTSR_TXTEN_Msk) && (${UART_INSTANCE_NAME}_REGS->UART_SR & UART_SR_ENDTX_Msk))
    {
        if(${UART_INSTANCE_NAME?lower_case}Obj.txBusyStatus == true)
        {
            ${UART_INSTANCE_NAME?lower_case}Obj.txBusyStatus = false;
            ${UART_INSTANCE_NAME}_REGS->UART_PTCR = UART_PTCR_TXTDIS_Msk;
            ${UART_INSTANCE_NAME}_REGS->UART_IDR = UART_IDR_ENDTX_Msk;

            if( ${UART_INSTANCE_NAME?lower_case}Obj.txCallback != NULL )
            {
                ${UART_INSTANCE_NAME?lower_case}Obj.txCallback(${UART_INSTANCE_NAME?lower_case}Obj.txContext);
            }
        }
    }
    <#else>
    /* Transmitter status */
    if(UART_SR_TXRDY_Msk == (${UART_INSTANCE_NAME}_REGS->UART_SR & UART_SR_TXRDY_Msk))
    {
        ${UART_INSTANCE_NAME}_ISR_TX_Handler();
    }
    </#if>
}
</#if>

static void ${UART_INSTANCE_NAME}_ErrorClear( void )
{
    uint8_t dummyData = 0u;

    ${UART_INSTANCE_NAME}_REGS->UART_CR = UART_CR_RSTSTA_Msk;

    /* Flush existing error bytes from the RX FIFO */
    while( UART_SR_RXRDY_Msk == (${UART_INSTANCE_NAME}_REGS->UART_SR & UART_SR_RXRDY_Msk) )
    {
        dummyData = (uint8_t)(${UART_INSTANCE_NAME}_REGS->UART_RHR & UART_RHR_RXCHR_Msk);
    }

    /* Ignore the warning */
    (void)dummyData;
}

void ${UART_INSTANCE_NAME}_Initialize( void )
{
    /* Reset ${UART_INSTANCE_NAME} */
    ${UART_INSTANCE_NAME}_REGS->UART_CR = (UART_CR_RSTRX_Msk | UART_CR_RSTTX_Msk | UART_CR_RSTSTA_Msk);

    /* Enable ${UART_INSTANCE_NAME} */
    ${UART_INSTANCE_NAME}_REGS->UART_CR = (UART_CR_TXEN_Msk | UART_CR_RXEN_Msk);

    /* Configure ${UART_INSTANCE_NAME} mode */
    <#if UART_CLK_SRC??>
    ${UART_INSTANCE_NAME}_REGS->UART_MR = ((UART_MR_BRSRCCK_${UART_CLK_SRC}) | (UART_MR_PAR_${UART_MR_PAR}) | (${UART_MR_FILTER?then(1,0)}U << UART_MR_FILTER_Pos));
    <#else>
    ${UART_INSTANCE_NAME}_REGS->UART_MR = ((UART_MR_PAR_${UART_MR_PAR}) | (${UART_MR_FILTER?then(1,0)}U << UART_MR_FILTER_Pos));
    </#if>

    /* Configure ${UART_INSTANCE_NAME} Baud Rate */
    ${UART_INSTANCE_NAME}_REGS->UART_BRGR = UART_BRGR_CD(${BRG_VALUE});
<#if UART_INTERRUPT_MODE_ENABLE == true>

    /* Initialize instance object */
    ${UART_INSTANCE_NAME?lower_case}Obj.rxBuffer = NULL;
    ${UART_INSTANCE_NAME?lower_case}Obj.rxSize = 0;
    ${UART_INSTANCE_NAME?lower_case}Obj.rxProcessedSize = 0;
    ${UART_INSTANCE_NAME?lower_case}Obj.rxBusyStatus = false;
    ${UART_INSTANCE_NAME?lower_case}Obj.rxCallback = NULL;
    ${UART_INSTANCE_NAME?lower_case}Obj.txBuffer = NULL;
    ${UART_INSTANCE_NAME?lower_case}Obj.txSize = 0;
    ${UART_INSTANCE_NAME?lower_case}Obj.txProcessedSize = 0;
    ${UART_INSTANCE_NAME?lower_case}Obj.txBusyStatus = false;
    ${UART_INSTANCE_NAME?lower_case}Obj.txCallback = NULL;
</#if>
}

UART_ERROR ${UART_INSTANCE_NAME}_ErrorGet( void )
{
    UART_ERROR errors = UART_ERROR_NONE;
    uint32_t status = ${UART_INSTANCE_NAME}_REGS->UART_SR;

    errors = (UART_ERROR)(status & (UART_SR_OVRE_Msk | UART_SR_PARE_Msk | UART_SR_FRAME_Msk));

    if(errors != UART_ERROR_NONE)
    {
        ${UART_INSTANCE_NAME}_ErrorClear();
    }

    /* All errors are cleared, but send the previous error state */
    return errors;
}

bool ${UART_INSTANCE_NAME}_SerialSetup( UART_SERIAL_SETUP *setup, uint32_t srcClkFreq )
{
    bool status = false;
    uint32_t baud;
    uint32_t brgVal = 0;
    uint32_t uartMode;

<#if UART_INTERRUPT_MODE_ENABLE == true>
    if((${UART_INSTANCE_NAME?lower_case}Obj.rxBusyStatus == true) || (${UART_INSTANCE_NAME?lower_case}Obj.txBusyStatus == true))
    {
        /* Transaction is in progress, so return without updating settings */
        return false;
    }
</#if>
    if (setup != NULL)
    {
        baud = setup->baudRate;
        if(srcClkFreq == 0U)
        {
            srcClkFreq = ${UART_INSTANCE_NAME}_FrequencyGet();
        }

        /* Calculate BRG value */
        brgVal = srcClkFreq / (16U * baud);

        /* If the target baud rate is acheivable using this clock */
        if (brgVal <= 65535U)
        {
            /* Configure ${UART_INSTANCE_NAME} mode */
            uartMode = ${UART_INSTANCE_NAME}_REGS->UART_MR;
            uartMode &= ~UART_MR_PAR_Msk;
            ${UART_INSTANCE_NAME}_REGS->UART_MR = uartMode | setup->parity ;

            /* Configure ${UART_INSTANCE_NAME} Baud Rate */
            ${UART_INSTANCE_NAME}_REGS->UART_BRGR = UART_BRGR_CD(brgVal);

            status = true;
        }
    }

    return status;
}

bool ${UART_INSTANCE_NAME}_Read( void *buffer, const size_t size )
{
    bool status = false;
    UART_ERROR errorinfo;
<#if UART_INTERRUPT_MODE_ENABLE == false>
    uint32_t errorStatus = 0;
    size_t processedSize = 0;
</#if>

    uint8_t * lBuffer = (uint8_t *)buffer;

    if(NULL != lBuffer)
    {
        /* Clear errors before submitting the request.
         * ErrorGet clears errors internally. */
         errorinfo = ${UART_INSTANCE_NAME}_ErrorGet();
         
         if(errorinfo != 0U)
         {
             /* Nothing to do */
         }

<#if UART_INTERRUPT_MODE_ENABLE == false>
        while( size > processedSize )
        {
            /* Error status */
            errorStatus = (${UART_INSTANCE_NAME}_REGS->UART_SR & (UART_SR_OVRE_Msk | UART_SR_FRAME_Msk | UART_SR_PARE_Msk));

            if(errorStatus != 0U)
            {
                break;
            }

            if(UART_SR_RXRDY_Msk == (${UART_INSTANCE_NAME}_REGS->UART_SR & UART_SR_RXRDY_Msk))
            {
                *lBuffer++ = (uint8_t)(${UART_INSTANCE_NAME}_REGS->UART_RHR& UART_RHR_RXCHR_Msk);
                processedSize++;
            }
        }

        if(size == processedSize)
        {
            status = true;
        }
<#else>
        /* Check if receive request is in progress */
        if(${UART_INSTANCE_NAME?lower_case}Obj.rxBusyStatus == false)
        {
            ${UART_INSTANCE_NAME?lower_case}Obj.rxBuffer = lBuffer;
            ${UART_INSTANCE_NAME?lower_case}Obj.rxSize = size;
            ${UART_INSTANCE_NAME?lower_case}Obj.rxProcessedSize = 0;
            ${UART_INSTANCE_NAME?lower_case}Obj.rxBusyStatus = true;
            status = true;

            <#if useUARTRxDMA == true>
            ${UART_INSTANCE_NAME}_REGS->UART_RPR = (uint32_t)buffer;
            ${UART_INSTANCE_NAME}_REGS->UART_RCR = (uint32_t)size;
            ${UART_INSTANCE_NAME}_REGS->UART_PTCR = UART_PTCR_RXTEN_Msk;
            ${UART_INSTANCE_NAME}_REGS->UART_IER = (UART_IER_ENDRX_Msk | UART_IER_FRAME_Msk | UART_IER_PARE_Msk | UART_IER_OVRE_Msk);
            <#else>
            /* Enable Read, Overrun, Parity and Framing error interrupts */
            ${UART_INSTANCE_NAME}_REGS->UART_IER = (UART_IER_RXRDY_Msk | UART_IER_FRAME_Msk | UART_IER_PARE_Msk | UART_IER_OVRE_Msk);
            </#if>
        }
</#if>
    }

    return status;
}

bool ${UART_INSTANCE_NAME}_Write( void *buffer, const size_t size )
{
    bool status = false;
<#if UART_INTERRUPT_MODE_ENABLE == false>
    size_t processedSize = 0;
</#if>
    uint8_t * lBuffer = (uint8_t *)buffer;

    if(NULL != lBuffer)
    {
<#if UART_INTERRUPT_MODE_ENABLE == false>
        while( size > processedSize )
        {
            if(UART_SR_TXRDY_Msk == (${UART_INSTANCE_NAME}_REGS->UART_SR & UART_SR_TXRDY_Msk))
            {
                ${UART_INSTANCE_NAME}_REGS->UART_THR = (UART_THR_TXCHR(*lBuffer++) & UART_THR_TXCHR_Msk);
                processedSize++;
            }
        }

        status = true;
<#else>
        /* Check if transmit request is in progress */
        if(${UART_INSTANCE_NAME?lower_case}Obj.txBusyStatus == false)
        {
            ${UART_INSTANCE_NAME?lower_case}Obj.txBuffer = lBuffer;
            ${UART_INSTANCE_NAME?lower_case}Obj.txSize = size;
            ${UART_INSTANCE_NAME?lower_case}Obj.txProcessedSize = 0;
            ${UART_INSTANCE_NAME?lower_case}Obj.txBusyStatus = true;
            status = true;

            <#if useUARTTxDMA == true>
            ${UART_INSTANCE_NAME}_REGS->UART_TPR = (uint32_t)buffer;
            ${UART_INSTANCE_NAME}_REGS->UART_TCR = (uint32_t)size;
            ${UART_INSTANCE_NAME}_REGS->UART_PTCR = UART_PTCR_TXTEN_Msk;
            ${UART_INSTANCE_NAME}_REGS->UART_IER = UART_IER_ENDTX_Msk;
            <#else>
            /* Initiate the transfer by sending first byte */
            if(UART_SR_TXRDY_Msk == (${UART_INSTANCE_NAME}_REGS->UART_SR & UART_SR_TXRDY_Msk))
            {
                ${UART_INSTANCE_NAME}_REGS->UART_THR = (UART_THR_TXCHR(*lBuffer) & UART_THR_TXCHR_Msk);
                ${UART_INSTANCE_NAME?lower_case}Obj.txProcessedSize++;
            }

            ${UART_INSTANCE_NAME}_REGS->UART_IER = UART_IER_TXEMPTY_Msk;
            </#if>
        }
</#if>
    }

    return status;
}

<#if UART_INTERRUPT_MODE_ENABLE == true>
void ${UART_INSTANCE_NAME}_WriteCallbackRegister( UART_CALLBACK callback, uintptr_t context )
{
    ${UART_INSTANCE_NAME?lower_case}Obj.txCallback = callback;

    ${UART_INSTANCE_NAME?lower_case}Obj.txContext = context;
}

void ${UART_INSTANCE_NAME}_ReadCallbackRegister( UART_CALLBACK callback, uintptr_t context )
{
    ${UART_INSTANCE_NAME?lower_case}Obj.rxCallback = callback;

    ${UART_INSTANCE_NAME?lower_case}Obj.rxContext = context;
}

bool ${UART_INSTANCE_NAME}_WriteIsBusy( void )
{
    return ${UART_INSTANCE_NAME?lower_case}Obj.txBusyStatus;
}

bool ${UART_INSTANCE_NAME}_ReadIsBusy( void )
{
    return ${UART_INSTANCE_NAME?lower_case}Obj.rxBusyStatus;
}

size_t ${UART_INSTANCE_NAME}_WriteCountGet( void )
{
    <#if useUARTTxDMA == true>
    return (${UART_INSTANCE_NAME?lower_case}Obj.txSize - ${UART_INSTANCE_NAME}_REGS->UART_TCR);
    <#else>
    return ${UART_INSTANCE_NAME?lower_case}Obj.txProcessedSize;
    </#if>
}

size_t ${UART_INSTANCE_NAME}_ReadCountGet( void )
{
    <#if useUARTRxDMA == true>
    return (${UART_INSTANCE_NAME?lower_case}Obj.rxSize - ${UART_INSTANCE_NAME}_REGS->UART_RCR);
    <#else>
    return ${UART_INSTANCE_NAME?lower_case}Obj.rxProcessedSize;
    </#if>
}

bool ${UART_INSTANCE_NAME}_ReadAbort(void)
{
    if (${UART_INSTANCE_NAME?lower_case}Obj.rxBusyStatus == true)
    {
        <#if useUARTRxDMA == true>
        ${UART_INSTANCE_NAME}_REGS->UART_RCR = (uint32_t)0;
        ${UART_INSTANCE_NAME}_REGS->UART_PTCR = UART_PTCR_RXTDIS_Msk;
        ${UART_INSTANCE_NAME}_REGS->UART_IDR = (UART_IDR_ENDRX_Msk | UART_IDR_FRAME_Msk | UART_IDR_PARE_Msk | UART_IDR_OVRE_Msk);
        <#else>
        /* Disable Read, Overrun, Parity and Framing error interrupts */
        ${UART_INSTANCE_NAME}_REGS->UART_IDR = (UART_IDR_RXRDY_Msk | UART_IDR_FRAME_Msk | UART_IDR_PARE_Msk | UART_IDR_OVRE_Msk);
        </#if>

        ${UART_INSTANCE_NAME?lower_case}Obj.rxBusyStatus = false;

        /* If required application should read the num bytes processed prior to calling the read abort API */
        ${UART_INSTANCE_NAME?lower_case}Obj.rxSize = 0;
		${UART_INSTANCE_NAME?lower_case}Obj.rxProcessedSize = 0;
    }

    return true;
}

</#if>
<#if UART_INTERRUPT_MODE_ENABLE == false>
int ${UART_INSTANCE_NAME}_ReadByte(void)
{
	uint32_t readbyte = (${UART_INSTANCE_NAME}_REGS->UART_RHR& UART_RHR_RXCHR_Msk);
    return (int)readbyte;
}

void ${UART_INSTANCE_NAME}_WriteByte( int data )
{
    while (UART_SR_TXRDY_Msk == (${UART_INSTANCE_NAME}_REGS->UART_SR & UART_SR_TXRDY_Msk))
	{
		/* Do Nothing */	
	}

    ${UART_INSTANCE_NAME}_REGS->UART_THR = (UART_THR_TXCHR(data) & UART_THR_TXCHR_Msk);
}

bool ${UART_INSTANCE_NAME}_TransmitterIsReady( void )
{
    bool status = false;

    if(UART_SR_TXRDY_Msk == (${UART_INSTANCE_NAME}_REGS->UART_SR & UART_SR_TXRDY_Msk))
    {
        status = true;
    }

    return status;
}

bool ${UART_INSTANCE_NAME}_ReceiverIsReady( void )
{
    bool status = false;

    if(UART_SR_RXRDY_Msk == (${UART_INSTANCE_NAME}_REGS->UART_SR & UART_SR_RXRDY_Msk))
    {
        status = true;
    }

    return status;
}

</#if>

bool ${UART_INSTANCE_NAME}_TransmitComplete( void )
{
    bool status = false;

    if(UART_SR_TXEMPTY_Msk == (${UART_INSTANCE_NAME}_REGS->UART_SR & UART_SR_TXEMPTY_Msk))
    {
        status = true;
    }

    return status;
}