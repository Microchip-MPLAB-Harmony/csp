/*******************************************************************************
  UART${INDEX?string} PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_uart${INDEX?string}.c

  Summary:
    UART${INDEX?string} PLIB Implementation File

  Description:
    None

*******************************************************************************/

/*******************************************************************************
Copyright (c) 2017 released Microchip Technology Inc.  All rights reserved.

Microchip licenses to you the right to use, modify, copy and distribute
Software only when embedded on a Microchip microcontroller or digital signal
controller that is integrated into your product or third party product
(pursuant to the sublicense terms in the accompanying license agreement).

You should refer to the license agreement accompanying this Software for
additional information regarding your rights and obligations.

SOFTWARE AND DOCUMENTATION ARE PROVIDED AS IS  WITHOUT  WARRANTY  OF  ANY  KIND,
EITHER EXPRESS  OR  IMPLIED,  INCLUDING  WITHOUT  LIMITATION,  ANY  WARRANTY  OF
MERCHANTABILITY, TITLE, NON-INFRINGEMENT AND FITNESS FOR A  PARTICULAR  PURPOSE.
IN NO EVENT SHALL MICROCHIP OR  ITS  LICENSORS  BE  LIABLE  OR  OBLIGATED  UNDER
CONTRACT, NEGLIGENCE, STRICT LIABILITY, CONTRIBUTION,  BREACH  OF  WARRANTY,  OR
OTHER LEGAL  EQUITABLE  THEORY  ANY  DIRECT  OR  INDIRECT  DAMAGES  OR  EXPENSES
INCLUDING BUT NOT LIMITED TO ANY  INCIDENTAL,  SPECIAL,  INDIRECT,  PUNITIVE  OR
CONSEQUENTIAL DAMAGES, LOST  PROFITS  OR  LOST  DATA,  COST  OF  PROCUREMENT  OF
SUBSTITUTE  GOODS,  TECHNOLOGY,  SERVICES,  OR  ANY  CLAIMS  BY  THIRD   PARTIES
(INCLUDING BUT NOT LIMITED TO ANY DEFENSE  THEREOF),  OR  OTHER  SIMILAR  COSTS.
*******************************************************************************/

#include "${__PROCESSOR?lower_case}.h"
#include "plib_uart${INDEX?string}.h"

<#--Implementation-->
// *****************************************************************************
// *****************************************************************************
// Section: UART${INDEX?string} Implementation
// *****************************************************************************
// *****************************************************************************
<#if INTERRUPT_MODE == true>

UART_OBJECT uart${INDEX?string}Obj;

void static UART${INDEX?string}_ISR_RX_Handler( void )
{
    if(uart${INDEX?string}Obj.rxBusyStatus == true)
    {
        while((UART_SR_RXRDY_Msk == (UART${INDEX?string}_REGS->UART_SR& UART_SR_RXRDY_Msk)) && (uart${INDEX?string}Obj.rxSize > uart${INDEX?string}Obj.rxProcessedSize) )
        {
            uart${INDEX?string}Obj.rxBuffer[uart${INDEX?string}Obj.rxProcessedSize++] = (UART${INDEX?string}_REGS->UART_RHR& UART_RHR_RXCHR_Msk);
        }

        /* Check if the buffer is done */
        if(uart${INDEX?string}Obj.rxProcessedSize >= uart${INDEX?string}Obj.rxSize)
        {
            uart${INDEX?string}Obj.rxBusyStatus = false;
            uart${INDEX?string}Obj.rxSize = 0;
            uart${INDEX?string}Obj.rxProcessedSize = 0;
            UART${INDEX?string}_REGS->UART_IDR|= UART_IDR_RXRDY_Msk;

            if(uart${INDEX?string}Obj.rxCallback != NULL)
            {
                uart${INDEX?string}Obj.rxCallback(uart${INDEX?string}Obj.rxContext);
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

void static UART${INDEX?string}_ISR_TX_Handler( void )
{
    if(uart${INDEX?string}Obj.txBusyStatus == true)
    {
        while((UART_SR_TXEMPTY_Msk == (UART${INDEX?string}_REGS->UART_SR& UART_SR_TXEMPTY_Msk)) && (uart${INDEX?string}Obj.txSize > uart${INDEX?string}Obj.txProcessedSize) )
        {
            UART${INDEX?string}_REGS->UART_THR|= uart${INDEX?string}Obj.txBuffer[uart${INDEX?string}Obj.txProcessedSize++];
        }

        /* Check if the buffer is done */
        if(uart${INDEX?string}Obj.txProcessedSize >= uart${INDEX?string}Obj.txSize)
        {
            uart${INDEX?string}Obj.txBusyStatus = false;
            uart${INDEX?string}Obj.txSize = 0;
            uart${INDEX?string}Obj.txProcessedSize = 0;
            UART${INDEX?string}_REGS->UART_IDR|= UART_IDR_TXEMPTY_Msk;

            if(uart${INDEX?string}Obj.txCallback != NULL)
            {
                uart${INDEX?string}Obj.txCallback(uart${INDEX?string}Obj.txContext);
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

void UART${INDEX?string}_InterruptHandler( void )
{
    /* Error status */
    uint32_t errorStatus = (UART${INDEX?string}_REGS->UART_SR& (UART_SR_OVRE_Msk | UART_SR_FRAME_Msk | UART_SR_PARE_Msk));

    if(errorStatus != 0)
    {
        /* Client must call UARTx_ErrorGet() function to clear the errors */

        /* UART errors are normally associated with the receiver, hence calling
         * receiver context */
        if( uart${INDEX?string}Obj.rxCallback != NULL )
        {
            uart${INDEX?string}Obj.rxCallback(uart${INDEX?string}Obj.rxContext);
        }
    }

    /* Receiver status */
    if(UART_SR_RXRDY_Msk == (UART${INDEX?string}_REGS->UART_SR& UART_SR_RXRDY_Msk))
    {
        UART${INDEX?string}_ISR_RX_Handler();
    }

    /* Transmitter status */
    if(UART_SR_TXEMPTY_Msk == (UART${INDEX?string}_REGS->UART_SR& UART_SR_TXEMPTY_Msk))
    {
        UART${INDEX?string}_ISR_TX_Handler();
    }

    return;
}

</#if>

void UART${INDEX?string}_Initialize( void )
{
    /* Reset UART${INDEX?string} */
    UART${INDEX?string}_REGS->UART_CR = (UART_CR_RSTRX_Msk | UART_CR_RSTTX_Msk | UART_CR_RSTSTA_Msk);

    /* Enable UART${INDEX?string} */
    UART${INDEX?string}_REGS->UART_CR = (UART_CR_TXEN_Msk | UART_CR_RXEN_Msk);

    /* Configure UART${INDEX?string} mode */
    UART${INDEX?string}_REGS->UART_MR = ((UART_MR_PAR_${UART_MR_PAR}) | (${UART_MR_FILTER?then(1,0)} << UART_MR_FILTER_Pos));

    /* Configure UART${INDEX?string} Baud Rate */
    UART${INDEX?string}_REGS->UART_BRGR = UART_BRGR_CD(${BRG_VALUE});
<#if INTERRUPT_MODE == true>

    /* Enable Overrun, Parity and Framing error interrupts */
    UART${INDEX?string}_REGS->UART_IER = (UART_IER_FRAME_Msk | UART_IER_PARE_Msk | UART_IER_OVRE_Msk);

    /* Initialize instance object */
    uart${INDEX?string}Obj.rxBuffer = NULL;
    uart${INDEX?string}Obj.rxSize = 0;
    uart${INDEX?string}Obj.rxProcessedSize = 0;
    uart${INDEX?string}Obj.rxBusyStatus = false;
    uart${INDEX?string}Obj.rxCallback = NULL;
    uart${INDEX?string}Obj.txBuffer = NULL;
    uart${INDEX?string}Obj.txSize = 0;
    uart${INDEX?string}Obj.txProcessedSize = 0;
    uart${INDEX?string}Obj.txBusyStatus = false;
    uart${INDEX?string}Obj.txCallback = NULL;
</#if>

    return;
}

UART_ERROR UART${INDEX?string}_ErrorGet( void )
{
    UART_ERROR errors = UART_ERROR_NONE;
    uint8_t dummyData = 0u;
    uint32_t status = UART${INDEX?string}_REGS->UART_SR;

    /* Collect all errors */
    if(status & UART_SR_OVRE_Msk)
    {
        errors = UART_ERROR_OVERRUN;
    }
    if(status & UART_SR_PARE_Msk)
    {
        errors |= UART_ERROR_PARITY;
    }
    if(status & UART_SR_FRAME_Msk)
    {
        errors |= UART_ERROR_FRAMING;
    }

    /* Clear all error flags */
    if(errors != UART_ERROR_NONE)
    {
        UART${INDEX?string}_REGS->UART_CR|= UART_CR_RSTSTA_Msk;

        /* Flush existing error bytes from the RX FIFO */
        while( UART_SR_RXRDY_Msk == (UART${INDEX?string}_REGS->UART_SR& UART_SR_RXRDY_Msk) )
        {
            dummyData = (UART${INDEX?string}_REGS->UART_RHR& UART_RHR_RXCHR_Msk);
        }

        /* Ignore the warning */
        (void)dummyData;
    }

    /* All errors are cleared, but send the previous error state */
    return errors;
}

bool UART${INDEX?string}_Read( void *buffer, const size_t size )
{
    bool status = false;
<#if INTERRUPT_MODE == false>
    size_t processedSize = 0;
</#if>

    uint8_t * lBuffer = (uint8_t *)buffer;

    if(NULL != lBuffer)
    {
<#if INTERRUPT_MODE == false>
        while( size > processedSize )
        {
            if(UART_SR_RXRDY_Msk == (UART${INDEX?string}_REGS->UART_SR& UART_SR_RXRDY_Msk))
            {
                *lBuffer++ = (UART${INDEX?string}_REGS->UART_RHR& UART_RHR_RXCHR_Msk);
                processedSize++;
            }
        }

        status = true;
<#else>
        /* Check if receive request is in progress */
        if(uart${INDEX?string}Obj.rxBusyStatus == false)
        {
            uart${INDEX?string}Obj.rxBuffer = lBuffer;
            uart${INDEX?string}Obj.rxSize = size;
            uart${INDEX?string}Obj.rxProcessedSize = 0;
            uart${INDEX?string}Obj.rxBusyStatus = true;
            status = true;

            UART${INDEX?string}_REGS->UART_IER = UART_IER_RXRDY_Msk;
        }
</#if>
    }

    return status;
}

bool UART${INDEX?string}_Write( void *buffer, const size_t size )
{
    bool status = false;
<#if INTERRUPT_MODE == false>
    size_t processedSize = 0;
</#if>
    uint8_t * lBuffer = (uint8_t *)buffer;

    if(NULL != lBuffer)
    {
<#if INTERRUPT_MODE == false>
        while( size > processedSize )
        {
            if(UART_SR_TXEMPTY_Msk == (UART${INDEX?string}_REGS->UART_SR& UART_SR_TXEMPTY_Msk))
            {
                UART${INDEX?string}_REGS->UART_THR = (UART_THR_TXCHR(*lBuffer++) & UART_THR_TXCHR_Msk);
                processedSize++;
            }
        }

        status = true;
<#else>
        /* Check if transmit request is in progress */
        if(uart${INDEX?string}Obj.txBusyStatus == false)
        {
            uart${INDEX?string}Obj.txBuffer = lBuffer;
            uart${INDEX?string}Obj.txSize = size;
            uart${INDEX?string}Obj.txProcessedSize = 0;
            uart${INDEX?string}Obj.txBusyStatus = true;
            status = true;

            /* Initiate the transfer by sending first byte */
            if(UART_SR_TXEMPTY_Msk == (UART${INDEX?string}_REGS->UART_SR& UART_SR_TXEMPTY_Msk))
            {
                UART${INDEX?string}_REGS->UART_THR = (UART_THR_TXCHR(*lBuffer) & UART_THR_TXCHR_Msk);
                uart${INDEX?string}Obj.txProcessedSize++;
            }

            UART${INDEX?string}_REGS->UART_IER = UART_IER_TXEMPTY_Msk;
        }
</#if>
    }

    return status;
}

<#if INTERRUPT_MODE == true>
bool UART${INDEX?string}_WriteCallbackRegister( UART_CALLBACK callback, uintptr_t context )
{
    uart${INDEX?string}Obj.txCallback = callback;
    uart${INDEX?string}Obj.txContext = context;

    return true;
}

bool UART${INDEX?string}_ReadCallbackRegister( UART_CALLBACK callback, uintptr_t context )
{
    uart${INDEX?string}Obj.rxCallback = callback;
    uart${INDEX?string}Obj.rxContext = context;

    return true;
}

bool UART${INDEX?string}_WriteIsBusy( void )
{
    return uart${INDEX?string}Obj.txBusyStatus;
}

bool UART${INDEX?string}_ReadIsBusy( void )
{
    return uart${INDEX?string}Obj.rxBusyStatus;
}

size_t UART${INDEX?string}_WriteCountGet( void )
{
    return uart${INDEX?string}Obj.txProcessedSize;
}

size_t UART${INDEX?string}_ReadCountGet( void )
{
    return uart${INDEX?string}Obj.rxProcessedSize;
}

</#if>
<#if INTERRUPT_MODE == false>
bool UART${INDEX?string}_TransmitterIsReady( void )
{
    bool status = false;

    if(UART_SR_TXEMPTY_Msk == (UART${INDEX?string}_REGS->UART_SR& UART_SR_TXEMPTY_Msk))
    {
        status = true;
    }

    return status;
}

bool UART${INDEX?string}_ReceiverIsReady( void )
{
    bool status = false;

    if(UART_SR_RXRDY_Msk == (UART${INDEX?string}_REGS->UART_SR& UART_SR_RXRDY_Msk))
    {
        status = true;
    }

    return status;
}

</#if>
