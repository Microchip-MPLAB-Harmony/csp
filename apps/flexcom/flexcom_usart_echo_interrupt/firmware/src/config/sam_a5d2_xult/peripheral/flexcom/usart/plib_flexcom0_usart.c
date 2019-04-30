/*******************************************************************************
  FLEXCOM0 USART PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_flexcom0_usart.c

  Summary:
    FLEXCOM0 USART PLIB Implementation File

  Description
    This file defines the interface to the FLEXCOM0 USART peripheral library. This
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
#include "plib_flexcom0_usart.h"

// *****************************************************************************
// *****************************************************************************
// Section: FLEXCOM0 USART Implementation
// *****************************************************************************
// *****************************************************************************

FLEXCOM_USART_OBJECT flexcom0UsartObj;

void static FLEXCOM0_USART_ISR_RX_Handler( void )
{
    if(flexcom0UsartObj.rxBusyStatus == true)
    {
        while((FLEX_US_CSR_RXRDY_Msk == (FLEXCOM0_REGS->FLEX_US_CSR & FLEX_US_CSR_RXRDY_Msk)) && (flexcom0UsartObj.rxSize > flexcom0UsartObj.rxProcessedSize) )
        {
            flexcom0UsartObj.rxBuffer[flexcom0UsartObj.rxProcessedSize++] = (FLEXCOM0_REGS->FLEX_US_RHR & FLEX_US_RHR_RXCHR_Msk);
        }

        /* Check if the buffer is done */
        if(flexcom0UsartObj.rxProcessedSize >= flexcom0UsartObj.rxSize)
        {
            flexcom0UsartObj.rxBusyStatus = false;

            /* Disable Read, Overrun, Parity and Framing error interrupts */
            FLEXCOM0_REGS->FLEX_US_IDR = (FLEX_US_IDR_RXRDY_Msk | FLEX_US_IDR_FRAME_Msk | FLEX_US_IDR_PARE_Msk | FLEX_US_IDR_OVRE_Msk);

            if(flexcom0UsartObj.rxCallback != NULL)
            {
                flexcom0UsartObj.rxCallback(flexcom0UsartObj.rxContext);
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

void static FLEXCOM0_USART_ISR_TX_Handler( void )
{
    if(flexcom0UsartObj.txBusyStatus == true)
    {
        while((FLEX_US_CSR_TXEMPTY_Msk == (FLEXCOM0_REGS->FLEX_US_CSR & FLEX_US_CSR_TXEMPTY_Msk)) && (flexcom0UsartObj.txSize > flexcom0UsartObj.txProcessedSize) )
        {
            FLEXCOM0_REGS->FLEX_US_THR = flexcom0UsartObj.txBuffer[flexcom0UsartObj.txProcessedSize++];
        }

        /* Check if the buffer is done */
        if(flexcom0UsartObj.txProcessedSize >= flexcom0UsartObj.txSize)
        {
            flexcom0UsartObj.txBusyStatus = false;
            FLEXCOM0_REGS->FLEX_US_IDR = FLEX_US_IDR_TXEMPTY_Msk;

            if(flexcom0UsartObj.txCallback != NULL)
            {
                flexcom0UsartObj.txCallback(flexcom0UsartObj.txContext);
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

void FLEXCOM0_InterruptHandler( void )
{
    /* Channel status */
    uint32_t channelStatus = FLEXCOM0_REGS->FLEX_US_CSR;

    /* Error status */
    uint32_t errorStatus = (channelStatus & (FLEX_US_CSR_OVRE_Msk | FLEX_US_CSR_FRAME_Msk | FLEX_US_CSR_PARE_Msk));

    if(errorStatus != 0)
    {
        /* Client must call FLEXCOM0_USART_ErrorGet() function to clear the errors */

        /* USART errors are normally associated with the receiver, hence calling
         * receiver context */
        if( flexcom0UsartObj.rxCallback != NULL )
        {
            flexcom0UsartObj.rxCallback(flexcom0UsartObj.rxContext);
        }

        flexcom0UsartObj.rxBusyStatus = false;

        /* Disable Read, Overrun, Parity and Framing error interrupts */
        FLEXCOM0_REGS->FLEX_US_IDR = (FLEX_US_IDR_RXRDY_Msk | FLEX_US_IDR_FRAME_Msk | FLEX_US_IDR_PARE_Msk | FLEX_US_IDR_OVRE_Msk);
    }

    /* Receiver status */
    if(FLEX_US_CSR_RXRDY_Msk == (channelStatus & FLEX_US_CSR_RXRDY_Msk))
    {
        FLEXCOM0_USART_ISR_RX_Handler();
    }

    /* Transmitter status */
    if(FLEX_US_CSR_TXEMPTY_Msk == (channelStatus & FLEX_US_CSR_TXEMPTY_Msk))
    {
        FLEXCOM0_USART_ISR_TX_Handler();
    }

    return;
}


void static FLEXCOM0_USART_ErrorClear( void )
{
    uint8_t dummyData = 0u;

    FLEXCOM0_REGS->FLEX_US_CR = FLEX_US_CR_RSTSTA_Msk;

    /* Flush existing error bytes from the RX FIFO */
    while( FLEX_US_CSR_RXRDY_Msk == (FLEXCOM0_REGS->FLEX_US_CSR& FLEX_US_CSR_RXRDY_Msk) )
    {
        dummyData = (FLEXCOM0_REGS->FLEX_US_RHR& FLEX_US_RHR_RXCHR_Msk);
    }

    /* Ignore the warning */
    (void)dummyData;

    return;
}

void FLEXCOM0_USART_Initialize( void )
{
    /* Set FLEXCOM USART operating mode */
    FLEXCOM0_REGS->FLEX_MR = FLEX_MR_OPMODE_USART;

    /* Reset FLEXCOM0 USART */
    FLEXCOM0_REGS->FLEX_US_CR = (FLEX_US_CR_RSTRX_Msk | FLEX_US_CR_RSTTX_Msk | FLEX_US_CR_RSTSTA_Msk);

    /* Enable FLEXCOM0 USART */
    FLEXCOM0_REGS->FLEX_US_CR = (FLEX_US_CR_TXEN_Msk | FLEX_US_CR_RXEN_Msk);

    /* Configure FLEXCOM0 USART mode */
    FLEXCOM0_REGS->FLEX_US_MR = ((FLEX_US_MR_USCLKS_MCK) | FLEX_US_MR_CHRL_8_BIT | FLEX_US_MR_PAR_NO | FLEX_US_MR_NBSTOP_1_BIT | (0 << FLEX_US_MR_OVER_Pos));

    /* Configure FLEXCOM0 USART Baud Rate */
    FLEXCOM0_REGS->FLEX_US_BRGR = FLEX_US_BRGR_CD(45);

    /* Initialize instance object */
    flexcom0UsartObj.rxBuffer = NULL;
    flexcom0UsartObj.rxSize = 0;
    flexcom0UsartObj.rxProcessedSize = 0;
    flexcom0UsartObj.rxBusyStatus = false;
    flexcom0UsartObj.rxCallback = NULL;
    flexcom0UsartObj.txBuffer = NULL;
    flexcom0UsartObj.txSize = 0;
    flexcom0UsartObj.txProcessedSize = 0;
    flexcom0UsartObj.txBusyStatus = false;
    flexcom0UsartObj.txCallback = NULL;

    return;
}

FLEXCOM_USART_ERROR FLEXCOM0_USART_ErrorGet( void )
{
    FLEXCOM_USART_ERROR errors = FLEXCOM_USART_ERROR_NONE;
    uint32_t status = FLEXCOM0_REGS->FLEX_US_CSR;

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
        FLEXCOM0_USART_ErrorClear();
    }

    /* All errors are cleared, but send the previous error state */
    return errors;
}

bool FLEXCOM0_USART_SerialSetup( FLEXCOM_USART_SERIAL_SETUP *setup, uint32_t srcClkFreq )
{
    uint32_t baud = 0;
    uint32_t brgVal = 0;
    uint32_t overSampVal = 0;
    uint32_t usartMode;
    bool status = false;

    if((flexcom0UsartObj.rxBusyStatus == true) || (flexcom0UsartObj.txBusyStatus == true))
    {
        /* Transaction is in progress, so return without updating settings */
        return false;
    }

    if (setup != NULL)
    {
        baud = setup->baudRate;
        if(srcClkFreq == 0)
        {
            srcClkFreq = FLEXCOM0_USART_FrequencyGet();
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

        /* Configure FLEXCOM0 USART mode */
        usartMode = FLEXCOM0_REGS->FLEX_US_MR;
        usartMode &= ~(FLEX_US_MR_CHRL_Msk | FLEX_US_MR_MODE9_Msk | FLEX_US_MR_PAR_Msk | FLEX_US_MR_NBSTOP_Msk | FLEX_US_MR_OVER_Msk);
        FLEXCOM0_REGS->FLEX_US_MR = usartMode | ((uint32_t)setup->dataWidth | (uint32_t)setup->parity | (uint32_t)setup->stopBits | overSampVal);

        /* Configure FLEXCOM0 USART Baud Rate */
        FLEXCOM0_REGS->FLEX_US_BRGR = FLEX_US_BRGR_CD(brgVal);
        status = true;
    }

    return status;
}

bool FLEXCOM0_USART_Read( void *buffer, const size_t size )
{
    bool status = false;
    uint8_t * lBuffer = (uint8_t *)buffer;

    if(NULL != lBuffer)
    {
        /* Clear errors before submitting the request.
         * ErrorGet clears errors internally. */
        FLEXCOM0_USART_ErrorGet();

        /* Check if receive request is in progress */
        if(flexcom0UsartObj.rxBusyStatus == false)
        {
            flexcom0UsartObj.rxBuffer = lBuffer;
            flexcom0UsartObj.rxSize = size;
            flexcom0UsartObj.rxProcessedSize = 0;
            flexcom0UsartObj.rxBusyStatus = true;
            status = true;

            /* Enable Read, Overrun, Parity and Framing error interrupts */
            FLEXCOM0_REGS->FLEX_US_IER = (FLEX_US_IER_RXRDY_Msk | FLEX_US_IER_FRAME_Msk | FLEX_US_IER_PARE_Msk | FLEX_US_IER_OVRE_Msk);
        }
    }

    return status;
}

bool FLEXCOM0_USART_Write( void *buffer, const size_t size )
{
    bool status = false;
    uint8_t * lBuffer = (uint8_t *)buffer;

    if(NULL != lBuffer)
    {
        /* Check if transmit request is in progress */
        if(flexcom0UsartObj.txBusyStatus == false)
        {
            flexcom0UsartObj.txBuffer = lBuffer;
            flexcom0UsartObj.txSize = size;
            flexcom0UsartObj.txProcessedSize = 0;
            flexcom0UsartObj.txBusyStatus = true;
            status = true;

            /* Initiate the transfer by sending first byte */
            if(FLEX_US_CSR_TXEMPTY_Msk == (FLEXCOM0_REGS->FLEX_US_CSR& FLEX_US_CSR_TXEMPTY_Msk))
            {
                FLEXCOM0_REGS->FLEX_US_THR = (FLEX_US_THR_TXCHR(*lBuffer) & FLEX_US_THR_TXCHR_Msk);
                flexcom0UsartObj.txProcessedSize++;
            }

            FLEXCOM0_REGS->FLEX_US_IER = FLEX_US_IER_TXEMPTY_Msk;
        }
    }

    return status;
}

void FLEXCOM0_USART_WriteCallbackRegister( FLEXCOM_USART_CALLBACK callback, uintptr_t context )
{
    flexcom0UsartObj.txCallback = callback;
    flexcom0UsartObj.txContext = context;
}

void FLEXCOM0_USART_ReadCallbackRegister( FLEXCOM_USART_CALLBACK callback, uintptr_t context )
{
    flexcom0UsartObj.rxCallback = callback;
    flexcom0UsartObj.rxContext = context;
}

bool FLEXCOM0_USART_WriteIsBusy( void )
{
    return flexcom0UsartObj.txBusyStatus;
}

bool FLEXCOM0_USART_ReadIsBusy( void )
{
    return flexcom0UsartObj.rxBusyStatus;
}

size_t FLEXCOM0_USART_WriteCountGet( void )
{
    return flexcom0UsartObj.txProcessedSize;
}

size_t FLEXCOM0_USART_ReadCountGet( void )
{
    return flexcom0UsartObj.rxProcessedSize;
}

