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

#include "device.h"
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
        while((US_CSR_RXRDY_Msk == (USART${INDEX?string}_REGS->US_CSR& US_CSR_RXRDY_Msk)) && (usart${INDEX?string}Obj.rxSize > usart${INDEX?string}Obj.rxProcessedSize) )
        {
            usart${INDEX?string}Obj.rxBuffer[usart${INDEX?string}Obj.rxProcessedSize++] = (USART${INDEX?string}_REGS->US_RHR& US_RHR_RXCHR_Msk);
        }

        /* Check if the buffer is done */
        if(usart${INDEX?string}Obj.rxProcessedSize >= usart${INDEX?string}Obj.rxSize)
        {
            if(usart${INDEX?string}Obj.rxCallback != NULL)
            {
                usart${INDEX?string}Obj.rxCallback(usart${INDEX?string}Obj.rxContext);
            }

            usart${INDEX?string}Obj.rxBusyStatus = false;
            usart${INDEX?string}Obj.rxSize = 0;
            usart${INDEX?string}Obj.rxProcessedSize = 0;

            /* Disable Read, Overrun, Parity and Framing error interrupts */
            USART${INDEX?string}_REGS->US_IDR = (US_IDR_RXRDY_Msk | US_IDR_FRAME_Msk | US_IDR_PARE_Msk | US_IDR_OVRE_Msk);
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
        while((US_CSR_TXEMPTY_Msk == (USART${INDEX?string}_REGS->US_CSR& US_CSR_TXEMPTY_Msk)) && (usart${INDEX?string}Obj.txSize > usart${INDEX?string}Obj.txProcessedSize) )
        {
            USART${INDEX?string}_REGS->US_THR|= usart${INDEX?string}Obj.txBuffer[usart${INDEX?string}Obj.txProcessedSize++];
        }

        /* Check if the buffer is done */
        if(usart${INDEX?string}Obj.txProcessedSize >= usart${INDEX?string}Obj.txSize)
        {
            usart${INDEX?string}Obj.txBusyStatus = false;
            usart${INDEX?string}Obj.txSize = 0;
            usart${INDEX?string}Obj.txProcessedSize = 0;
            USART${INDEX?string}_REGS->US_IDR = US_IDR_TXEMPTY_Msk;

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
    uint32_t errorStatus = (USART${INDEX?string}_REGS->US_CSR & (US_CSR_OVRE_Msk | US_CSR_FRAME_Msk | US_CSR_PARE_Msk));

    if(errorStatus != 0)
    {
        /* Client must call USARTx_ErrorGet() function to clear the errors */

        /* USART errors are normally associated with the receiver, hence calling
         * receiver context */
        if( usart${INDEX?string}Obj.rxCallback != NULL )
        {
            usart${INDEX?string}Obj.rxCallback(usart${INDEX?string}Obj.rxContext);
        }

        usart${INDEX?string}Obj.rxBusyStatus = false;
        usart${INDEX?string}Obj.rxSize = 0;
        usart${INDEX?string}Obj.rxProcessedSize = 0;

        /* Disable Read, Overrun, Parity and Framing error interrupts */
        USART${INDEX?string}_REGS->US_IDR = (US_IDR_RXRDY_Msk | US_IDR_FRAME_Msk | US_IDR_PARE_Msk | US_IDR_OVRE_Msk);
    }

    /* Receiver status */
    if(US_CSR_RXRDY_Msk == (USART${INDEX?string}_REGS->US_CSR& US_CSR_RXRDY_Msk))
    {
        USART${INDEX?string}_ISR_RX_Handler();
    }

    /* Transmitter status */
    if(US_CSR_TXEMPTY_Msk == (USART${INDEX?string}_REGS->US_CSR& US_CSR_TXEMPTY_Msk))
    {
        USART${INDEX?string}_ISR_TX_Handler();
    }

    return;
}

</#if>

void static USART${INDEX?string}_ErrorClear( void )
{
    uint8_t dummyData = 0u;

    USART${INDEX?string}_REGS->US_CR|= US_CR_RSTSTA_Msk;

    /* Flush existing error bytes from the RX FIFO */
    while( US_CSR_RXRDY_Msk == (USART${INDEX?string}_REGS->US_CSR& US_CSR_RXRDY_Msk) )
    {
        dummyData = (USART${INDEX?string}_REGS->US_RHR& US_RHR_RXCHR_Msk);
    }

    /* Ignore the warning */
    (void)dummyData;

    return;
}

void USART${INDEX?string}_Initialize( void )
{
    /* Reset USART${INDEX?string} */
    USART${INDEX?string}_REGS->US_CR = (US_CR_RSTRX_Msk | US_CR_RSTTX_Msk | US_CR_RSTSTA_Msk);

    /* Enable USART${INDEX?string} */
    USART${INDEX?string}_REGS->US_CR = (US_CR_TXEN_Msk | US_CR_RXEN_Msk);

    /* Configure USART${INDEX?string} mode */
    USART${INDEX?string}_REGS->US_MR = ((US_MR_USCLKS_${USART_CLK_SRC}) | (${USART_MR_MODE9?then(1,0)} << US_MR_MODE9_Pos) | US_MR_CHRL_${USART_MR_CHRL} | US_MR_PAR_${USART_MR_PAR} | US_MR_NBSTOP_${USART_MR_NBSTOP} | (${USART_MR_SYNC?then(1,0)} << US_MR_SYNC_Pos) | (${USART_MR_OVER?string} << US_MR_OVER_Pos));

    /* Configure USART${INDEX?string} Baud Rate */
    USART${INDEX?string}_REGS->US_BRGR = US_BRGR_CD(${BRG_VALUE});
<#if INTERRUPT_MODE == true>

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
    uint32_t status = USART${INDEX?string}_REGS->US_CSR;

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

    if(errors != USART_ERROR_NONE)
    {
        USART${INDEX?string}_ErrorClear();
    }

    /* All errors are cleared, but send the previous error state */
    return errors;
}

bool USART${INDEX?string}_SerialSetup( USART_SERIAL_SETUP *setup, uint32_t srcClkFreq )
{
    bool status = true;
    uint32_t clk = srcClkFreq;
    uint32_t baud = setup->baudRate;
    uint32_t brgVal = 0;
    uint32_t overSampVal = 0;
    uint32_t mode9Val = 0;
    uint32_t charLengthVal = 0;
    uint32_t parityVal = 0;
    uint32_t stopBitsVal = 0;

<#if INTERRUPT_MODE == true>
    if((usart${INDEX?string}Obj.rxBusyStatus == true) || (usart${INDEX?string}Obj.txBusyStatus == true))
    {
        /* Transaction is in progress, so return without updating settings */
        return false;
    }

</#if>
    if(clk == 0)
    {
        clk = USART${INDEX?string}_FrequencyGet();
    }

    /* Calculate BRG value */
    if (clk >= (16 * baud))
    {
        brgVal = (clk / (16 * baud));
    }
    else
    {
        brgVal = (clk / (8 * baud));
        overSampVal = (1 << US_MR_OVER_Pos) & US_MR_OVER_Msk;
    }

    /* Get Data width values */
    switch(setup->dataWidth)
    {
        case USART_DATA_5_BIT:
        case USART_DATA_6_BIT:
        case USART_DATA_7_BIT:
        case USART_DATA_8_BIT:
        {
            charLengthVal = US_MR_CHRL(setup->dataWidth);
            break;
        }
        case USART_DATA_9_BIT:
        {
            mode9Val = (1 << US_MR_MODE9_Pos) & US_MR_MODE9_Msk;
            break;
        }
        default:
        {
            status = false;
            break;
        }
    }

    /* Get Parity values */
    switch(setup->parity)
    {
        case USART_PARITY_ODD:
        case USART_PARITY_MARK:
        {
            parityVal = US_MR_PAR(setup->parity);
            break;
        }
        case USART_PARITY_NONE:
        {
            parityVal = US_MR_PAR_NO;
            break;
        }
        case USART_PARITY_EVEN:
        {
            parityVal = US_MR_PAR_EVEN;
            break;
        }
        case USART_PARITY_SPACE:
        {
            parityVal = US_MR_PAR_SPACE;
            break;
        }
        case USART_PARITY_MULTIDROP:
        {
            parityVal = US_MR_PAR_MULTIDROP;
            break;
        }
        default:
        {
            status = false;
            break;
        }
    }

    /* Get Stop bit values */
    switch(setup->stopBits)
    {
        case USART_STOP_1_BIT:
        case USART_STOP_1_5_BIT:
        case USART_STOP_2_BIT:
        {
            stopBitsVal = US_MR_NBSTOP(setup->stopBits);
            break;
        }
        default:
        {
            status = false;
            break;
        }
    }

    if(status != false)
    {
        /* Configure USART${INDEX?string} mode */
        USART${INDEX?string}_REGS->US_MR = (mode9Val | charLengthVal | parityVal | stopBitsVal | (${USART_MR_SYNC?then(1,0)} << US_MR_SYNC_Pos) | overSampVal);

        /* Configure USART${INDEX?string} Baud Rate */
        USART${INDEX?string}_REGS->US_BRGR = US_BRGR_CD(brgVal);
    }

    return status;
}

bool USART${INDEX?string}_Read( void *buffer, const size_t size )
{
    bool status = false;
<#if INTERRUPT_MODE == false>
    uint32_t errorStatus = 0;
    size_t processedSize = 0;
</#if>
    uint8_t * lBuffer = (uint8_t *)buffer;

    if(NULL != lBuffer)
    {
        /* Clear errors before submitting the request */
        USART${INDEX?string}_ErrorClear();

<#if INTERRUPT_MODE == false>
        while( size > processedSize )
        {
            /* Error status */
            errorStatus = (USART${INDEX?string}_REGS->US_CSR & (US_CSR_OVRE_Msk | US_CSR_FRAME_Msk | US_CSR_PARE_Msk));

            if(errorStatus != 0)
            {
                break;
            }

            if(US_CSR_RXRDY_Msk == (USART${INDEX?string}_REGS->US_CSR & US_CSR_RXRDY_Msk))
            {
                *lBuffer++ = (USART${INDEX?string}_REGS->US_RHR& US_RHR_RXCHR_Msk);
                processedSize++;
            }
        }

        if(size == processedSize)
        {
            status = true;
        }

<#else>
        /* Check if receive request is in progress */
        if(usart${INDEX?string}Obj.rxBusyStatus == false)
        {
            usart${INDEX?string}Obj.rxBuffer = lBuffer;
            usart${INDEX?string}Obj.rxSize = size;
            usart${INDEX?string}Obj.rxProcessedSize = 0;
            usart${INDEX?string}Obj.rxBusyStatus = true;
            status = true;

            /* Enable Read, Overrun, Parity and Framing error interrupts */
            USART${INDEX?string}_REGS->US_IER = (US_IER_RXRDY_Msk | US_IER_FRAME_Msk | US_IER_PARE_Msk | US_IER_OVRE_Msk);
        }
</#if>
    }

    return status;
}

bool USART${INDEX?string}_Write( void *buffer, const size_t size )
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
            if(US_CSR_TXEMPTY_Msk == (USART${INDEX?string}_REGS->US_CSR& US_CSR_TXEMPTY_Msk))
            {
                USART${INDEX?string}_REGS->US_THR = (US_THR_TXCHR(*lBuffer++) & US_THR_TXCHR_Msk);
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
            if(US_CSR_TXEMPTY_Msk == (USART${INDEX?string}_REGS->US_CSR& US_CSR_TXEMPTY_Msk))
            {
                USART${INDEX?string}_REGS->US_THR = (US_THR_TXCHR(*lBuffer) & US_THR_TXCHR_Msk);
                usart${INDEX?string}Obj.txProcessedSize++;
            }

            USART${INDEX?string}_REGS->US_IER = US_IER_TXEMPTY_Msk;
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

    if(US_CSR_TXEMPTY_Msk == (USART${INDEX?string}_REGS->US_CSR& US_CSR_TXEMPTY_Msk))
    {
        status = true;
    }

    return status;
}

bool USART${INDEX?string}_ReceiverIsReady( void )
{
    bool status = false;

    if(US_CSR_RXRDY_Msk == (USART${INDEX?string}_REGS->US_CSR& US_CSR_RXRDY_Msk))
    {
        status = true;
    }

    return status;
}

</#if>
