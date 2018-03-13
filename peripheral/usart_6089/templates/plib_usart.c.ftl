/*******************************************************************************
  USART${INDEX?string} PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_usart${INDEX?string}.c

  Summary:
    USART${INDEX?string} PLIB Implementation File

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
#include "plib_usart${INDEX?string}.h"

<#--Implementation-->
// *****************************************************************************
// *****************************************************************************
// Section: USART${INDEX?string} Implementation
// *****************************************************************************
// *****************************************************************************
<#if INTERRUPT_MODE == true>

USART_OBJECT usart${INDEX?string}Obj;

void static USART${INDEX?string}_ISR_RX_Handler( void )
{
    if(usart${INDEX?string}Obj.rxBusyStatus == true)
    {
        while((US_CSR_RXRDY_Msk == (_USART${INDEX?string}_REGS->US_CSR.w & US_CSR_RXRDY_Msk)) && (usart${INDEX?string}Obj.rxSize > usart${INDEX?string}Obj.rxProcessedSize) )
        {
            usart${INDEX?string}Obj.rxBuffer[usart${INDEX?string}Obj.rxProcessedSize++] = (_USART${INDEX?string}_REGS->US_RHR.w & US_RHR_RXCHR_Msk);
        }

        /* Check if the buffer is done */
        if(usart${INDEX?string}Obj.rxProcessedSize >= usart${INDEX?string}Obj.rxSize)
        {
            usart${INDEX?string}Obj.rxBusyStatus = false;
            usart${INDEX?string}Obj.rxSize = 0;
            usart${INDEX?string}Obj.rxProcessedSize = 0;
            _USART${INDEX?string}_REGS->US_IDR.w |= US_IDR_RXRDY_Msk;

            if(usart${INDEX?string}Obj.rxCallback != NULL)
            {
                usart${INDEX?string}Obj.rxCallback(usart${INDEX?string}Obj.rxContext);
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

void static USART${INDEX?string}_ISR_TX_Handler( void )
{
    if(usart${INDEX?string}Obj.txBusyStatus == true)
    {
        while((US_CSR_TXEMPTY_Msk == (_USART${INDEX?string}_REGS->US_CSR.w & US_CSR_TXEMPTY_Msk)) && (usart${INDEX?string}Obj.txSize > usart${INDEX?string}Obj.txProcessedSize) )
        {
            _USART${INDEX?string}_REGS->US_THR.w |= usart${INDEX?string}Obj.txBuffer[usart${INDEX?string}Obj.txProcessedSize++];
        }

        /* Check if the buffer is done */
        if(usart${INDEX?string}Obj.txProcessedSize >= usart${INDEX?string}Obj.txSize)
        {
            usart${INDEX?string}Obj.txBusyStatus = false;
            usart${INDEX?string}Obj.txSize = 0;
            usart${INDEX?string}Obj.txProcessedSize = 0;
            _USART${INDEX?string}_REGS->US_IDR.w |= US_IDR_TXEMPTY_Msk;

            if(usart${INDEX?string}Obj.txCallback != NULL)
            {
                usart${INDEX?string}Obj.txCallback(usart${INDEX?string}Obj.txContext);
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

void USART${INDEX?string}_InterruptHandler( void )
{
    /* Error status */
    uint32_t errorStatus = (_USART${INDEX?string}_REGS->US_CSR.w & (US_CSR_OVRE_Msk | US_CSR_FRAME_Msk | US_CSR_PARE_Msk));

    if(errorStatus != 0)
    {
        /* Client must call USARTx_ErrorGet() function to clear the errors */

        /* USART errors are normally associated with the receiver, hence calling
         * receiver context */
        if( usart${INDEX?string}Obj.rxCallback != NULL )
        {
            usart${INDEX?string}Obj.rxCallback(usart${INDEX?string}Obj.rxContext);
        }
    }

    /* Receiver status */
    if(US_CSR_RXRDY_Msk == (_USART${INDEX?string}_REGS->US_CSR.w & US_CSR_RXRDY_Msk))
    {
        USART${INDEX?string}_ISR_RX_Handler();
    }

    /* Transmitter status */
    if(US_CSR_TXEMPTY_Msk == (_USART${INDEX?string}_REGS->US_CSR.w & US_CSR_TXEMPTY_Msk))
    {
        USART${INDEX?string}_ISR_TX_Handler();
    }

    return;
}

</#if>

void USART${INDEX?string}_Initialize( void )
{
    /* Reset USART${INDEX?string} */
    _USART${INDEX?string}_REGS->US_CR.w = (US_CR_RSTRX_Msk | US_CR_RSTTX_Msk | US_CR_RSTSTA_Msk);

    /* Enable USART${INDEX?string} */
    _USART${INDEX?string}_REGS->US_CR.w = (US_CR_TXEN_Msk | US_CR_RXEN_Msk);

    /* Configure USART${INDEX?string} mode */
    _USART${INDEX?string}_REGS->US_MR.w = ((${USART_MR_MODE9?then(1,0)} << US_MR_MODE9_Pos) | US_MR_CHRL${USART_MR_CHRL} | US_MR_PAR_${USART_MR_PAR} | US_MR_NBSTOP${USART_MR_NBSTOP} | (${USART_MR_SYNC?then(1,0)} << US_MR_SYNC_Pos) | (${USART_MR_OVER?string} << US_MR_OVER_Pos));

    /* Configure USART${INDEX?string} Baud Rate */
    _USART${INDEX?string}_REGS->US_BRGR.w = US_BRGR_CD(${BRG_VALUE});
<#if INTERRUPT_MODE == true>

    /* Enable Overrun, Parity and Framing error interrupts */
    _USART${INDEX?string}_REGS->US_IER.w = (US_IER_FRAME_Msk | US_IER_PARE_Msk | US_IER_OVRE_Msk);

    /* Initialize instance object */
    usart${INDEX?string}Obj.rxBuffer = NULL;
    usart${INDEX?string}Obj.rxSize = 0;
    usart${INDEX?string}Obj.rxProcessedSize = 0;
    usart${INDEX?string}Obj.rxBusyStatus = false;
    usart${INDEX?string}Obj.rxCallback = NULL;
    usart${INDEX?string}Obj.txBuffer = NULL;
    usart${INDEX?string}Obj.txSize = 0;
    usart${INDEX?string}Obj.txProcessedSize = 0;
    usart${INDEX?string}Obj.txBusyStatus = false;
    usart${INDEX?string}Obj.txCallback = NULL;
</#if>

    return;
}

USART_ERROR USART${INDEX?string}_ErrorGet( void )
{
    USART_ERROR errors = USART_ERROR_NONE;
    uint8_t dummyData = 0u;
    uint32_t status = _USART${INDEX?string}_REGS->US_CSR.w;

    /* Collect all errors */
    if(status & US_CSR_OVRE_Msk)
    {
        errors = USART_ERROR_OVERRUN;
    }
    if(status & US_CSR_PARE_Msk)
    {
        errors |= USART_ERROR_PARITY;
    }
    if(status & US_CSR_FRAME_Msk)
    {
        errors |= USART_ERROR_FRAMING;
    }

    /* Clear all error flags */
    if(errors != USART_ERROR_NONE)
    {
        _USART${INDEX?string}_REGS->US_CR.w |= US_CR_RSTSTA_Msk;

        /* Flush existing error bytes from the RX FIFO */
        while( US_CSR_RXRDY_Msk == (_USART${INDEX?string}_REGS->US_CSR.w & US_CSR_RXRDY_Msk) )
        {
            dummyData = (_USART${INDEX?string}_REGS->US_RHR.w & US_RHR_RXCHR_Msk);
        }

        /* Ignore the warning */
        (void)dummyData;
    }

    /* All errors are cleared, but send the previous error state */
    return errors;
}

bool USART${INDEX?string}_Read( void *buffer, const size_t size )
{
    bool status = false;
    size_t processedSize = 0;
    uint8_t * lBuffer = (uint8_t *)buffer;

    if(NULL != lBuffer)
    {
<#if INTERRUPT_MODE == false>
        while( size > processedSize )
        {
            if(US_CSR_RXRDY_Msk == (_USART${INDEX?string}_REGS->US_CSR.w & US_CSR_RXRDY_Msk))
            {
                *lBuffer++ = (_USART${INDEX?string}_REGS->US_RHR.w & US_RHR_RXCHR_Msk);
                processedSize++;
            }
        }

        status = true;
<#else>
        /* Check if receive request is in progress */
        if(usart${INDEX?string}Obj.rxBusyStatus == false)
        {
            usart${INDEX?string}Obj.rxBuffer = lBuffer;
            usart${INDEX?string}Obj.rxSize = size;
            usart${INDEX?string}Obj.rxProcessedSize = 0;
            usart${INDEX?string}Obj.rxBusyStatus = true;
            status = true;

            _USART${INDEX?string}_REGS->US_IER.w = US_IER_RXRDY_Msk;
        }
</#if>
    }

    return status;
}

bool USART${INDEX?string}_Write( void *buffer, const size_t size )
{
    bool status = false;
    size_t processedSize = 0;
    uint8_t * lBuffer = (uint8_t *)buffer;

    if(NULL != lBuffer)
    {
<#if INTERRUPT_MODE == false>
        while( size > processedSize )
        {
            if(US_CSR_TXEMPTY_Msk == (_USART${INDEX?string}_REGS->US_CSR.w & US_CSR_TXEMPTY_Msk))
            {
                _USART${INDEX?string}_REGS->US_THR.w = (US_THR_TXCHR(*lBuffer++) & US_THR_TXCHR_Msk);
                processedSize++;
            }
        }

        status = true;
<#else>
        /* Check if transmit request is in progress */
        if(usart${INDEX?string}Obj.txBusyStatus == false)
        {
            usart${INDEX?string}Obj.txBuffer = lBuffer;
            usart${INDEX?string}Obj.txSize = size;
            usart${INDEX?string}Obj.txProcessedSize = 0;
            usart${INDEX?string}Obj.txBusyStatus = true;
            status = true;

            /* Initiate the transfer by sending first byte */
            if(US_CSR_TXEMPTY_Msk == (_USART${INDEX?string}_REGS->US_CSR.w & US_CSR_TXEMPTY_Msk))
            {
                _USART${INDEX?string}_REGS->US_THR.w = (US_THR_TXCHR(*lBuffer) & US_THR_TXCHR_Msk);
                usart${INDEX?string}Obj.txProcessedSize++;
            }

            _USART${INDEX?string}_REGS->US_IER.w = US_IER_TXEMPTY_Msk;
        }
</#if>
    }

    return status;
}

<#if INTERRUPT_MODE == true>
bool USART${INDEX?string}_WriteCallbackRegister( USART_CALLBACK callback, uintptr_t context )
{
    usart${INDEX?string}Obj.txCallback = callback;
    usart${INDEX?string}Obj.txContext = context;

    return true;
}

bool USART${INDEX?string}_ReadCallbackRegister( USART_CALLBACK callback, uintptr_t context )
{
    usart${INDEX?string}Obj.rxCallback = callback;
    usart${INDEX?string}Obj.rxContext = context;

    return true;
}

bool USART${INDEX?string}_WriteIsBusy( void )
{
    return usart${INDEX?string}Obj.txBusyStatus;
}

bool USART${INDEX?string}_ReadIsBusy( void )
{
    return usart${INDEX?string}Obj.rxBusyStatus;
}

size_t USART${INDEX?string}_WriteCountGet( void )
{
    return usart${INDEX?string}Obj.txProcessedSize;
}

size_t USART${INDEX?string}_ReadCountGet( void )
{
    return usart${INDEX?string}Obj.rxProcessedSize;
}

</#if>
<#if INTERRUPT_MODE == false>
bool USART${INDEX?string}_TransmitterIsReady( void )
{
    bool status = false;

    if(US_CSR_TXEMPTY_Msk == (_USART${INDEX?string}_REGS->US_CSR.w & US_CSR_TXEMPTY_Msk))
    {
        status = true;
    }

    return status;
}

bool USART${INDEX?string}_ReceiverIsReady( void )
{
    bool status = false;

    if(US_CSR_RXRDY_Msk == (_USART${INDEX?string}_REGS->US_CSR.w & US_CSR_RXRDY_Msk))
    {
        status = true;
    }

    return status;
}

</#if>
