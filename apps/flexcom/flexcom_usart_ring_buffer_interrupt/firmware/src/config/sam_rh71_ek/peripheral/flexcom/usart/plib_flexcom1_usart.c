/*******************************************************************************
  FLEXCOM1 USART PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_flexcom1_usart.c

  Summary:
    FLEXCOM1 USART PLIB Implementation File

  Description
    This file defines the interface to the FLEXCOM1 USART
    peripheral library. This library provides access to and control of the
    associated peripheral instance.

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

#include "plib_flexcom1_usart.h"

#define FLEXCOM1_USART_READ_BUFFER_SIZE      20

/* Disable Read, Overrun, Parity and Framing error interrupts */
#define FLEXCOM1_USART_RX_INT_DISABLE()      FLEXCOM1_REGS->FLEX_US_IDR = (FLEX_US_IDR_RXRDY_Msk | FLEX_US_IDR_FRAME_Msk | FLEX_US_IDR_PARE_Msk | FLEX_US_IDR_OVRE_Msk)

/* Enable Read, Overrun, Parity and Framing error interrupts */		
#define FLEXCOM1_USART_RX_INT_ENABLE()       FLEXCOM1_REGS->FLEX_US_IER = (FLEX_US_IER_RXRDY_Msk | FLEX_US_IER_FRAME_Msk | FLEX_US_IER_PARE_Msk | FLEX_US_IER_OVRE_Msk)

static uint8_t FLEXCOM1_USART_ReadBuffer[FLEXCOM1_USART_READ_BUFFER_SIZE];

#define FLEXCOM1_USART_WRITE_BUFFER_SIZE     128
#define FLEXCOM1_USART_TX_INT_DISABLE()      FLEXCOM1_REGS->FLEX_US_IDR = FLEX_US_IDR_TXEMPTY_Msk
#define FLEXCOM1_USART_TX_INT_ENABLE()       FLEXCOM1_REGS->FLEX_US_IER = FLEX_US_IER_TXEMPTY_Msk

static uint8_t FLEXCOM1_USART_WriteBuffer[FLEXCOM1_USART_WRITE_BUFFER_SIZE];

// *****************************************************************************
// *****************************************************************************
// Section: FLEXCOM1 USART Ring Buffer Implementation
// *****************************************************************************
// *****************************************************************************

FLEXCOM_USART_RING_BUFFER_OBJECT flexcom1UsartObj;

void FLEXCOM1_USART_Initialize( void )
{
    /* Set FLEXCOM USART operating mode */
    FLEXCOM1_REGS->FLEX_MR = FLEX_MR_OPMODE_USART;

    /* Reset FLEXCOM1 USART */
    FLEXCOM1_REGS->FLEX_US_CR = (FLEX_US_CR_RSTRX_Msk | FLEX_US_CR_RSTTX_Msk | FLEX_US_CR_RSTSTA_Msk);

    /* Enable FLEXCOM1 USART */
    FLEXCOM1_REGS->FLEX_US_CR = (FLEX_US_CR_TXEN_Msk | FLEX_US_CR_RXEN_Msk);

    /* Configure FLEXCOM1 USART mode */
    FLEXCOM1_REGS->FLEX_US_MR = ((FLEX_US_MR_USCLKS_MCK) | FLEX_US_MR_CHRL_8_BIT | FLEX_US_MR_PAR_NO | FLEX_US_MR_NBSTOP_1_BIT | (0 << FLEX_US_MR_OVER_Pos));

    /* Configure FLEXCOM1 USART Baud Rate */
    FLEXCOM1_REGS->FLEX_US_BRGR = FLEX_US_BRGR_CD(27);
	
	flexcom1UsartObj.rdCallback = NULL;
    flexcom1UsartObj.rdInIndex = flexcom1UsartObj.rdOutIndex = 0;
    flexcom1UsartObj.isRdNotificationEnabled = false;
    flexcom1UsartObj.isRdNotifyPersistently = false;
    flexcom1UsartObj.rdThreshold = 0;
    flexcom1UsartObj.wrCallback = NULL;
    flexcom1UsartObj.wrInIndex = flexcom1UsartObj.wrOutIndex = 0;
    flexcom1UsartObj.isWrNotificationEnabled = false;
    flexcom1UsartObj.isWrNotifyPersistently = false;
    flexcom1UsartObj.wrThreshold = 0;   
	
	FLEXCOM1_USART_RX_INT_ENABLE();
}

void static FLEXCOM1_USART_ErrorClear( void )
{
    uint8_t dummyData = 0u;

    FLEXCOM1_REGS->FLEX_US_CR = FLEX_US_CR_RSTSTA_Msk;

    /* Flush existing error bytes from the RX FIFO */
    while( FLEX_US_CSR_RXRDY_Msk == (FLEXCOM1_REGS->FLEX_US_CSR& FLEX_US_CSR_RXRDY_Msk) )
    {
        dummyData = (FLEXCOM1_REGS->FLEX_US_RHR& FLEX_US_RHR_RXCHR_Msk);
    }

    /* Ignore the warning */
    (void)dummyData;

    return;
}

FLEXCOM_USART_ERROR FLEXCOM1_USART_ErrorGet( void )
{
    FLEXCOM_USART_ERROR errors = FLEXCOM_USART_ERROR_NONE;
    uint32_t status = FLEXCOM1_REGS->FLEX_US_CSR;

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
        FLEXCOM1_USART_ErrorClear();
    }

    /* All errors are cleared, but send the previous error state */
    return errors;
}

bool FLEXCOM1_USART_SerialSetup( FLEXCOM_USART_SERIAL_SETUP *setup, uint32_t srcClkFreq )
{
    uint32_t baud = 0;
    uint32_t brgVal = 0;
    uint32_t overSampVal = 0;
    uint32_t usartMode;
    bool status = false;

    if (setup != NULL)
    {
        baud = setup->baudRate;
        if(srcClkFreq == 0)
        {
            srcClkFreq = FLEXCOM1_USART_FrequencyGet();
        }

        /* Calculate BRG value */
        if (srcClkFreq >= (16 * baud))
        {
            brgVal = (srcClkFreq / (16 * baud));
        }
        else if (srcClkFreq >= (8 * baud))
        {
            brgVal = (srcClkFreq / (8 * baud));
            overSampVal = (1 << FLEX_US_MR_OVER_Pos) & FLEX_US_MR_OVER_Msk;
        }
        else
        {
            /* The input clock source - srcClkFreq, is too low to generate the desired baud */
            return status;
        }
        if (brgVal > 65535)
        {
            /* The requested baud is so low that the ratio of srcClkFreq to baud exceeds the 16-bit register value of CD register */
            return status;
        }

        /* Configure FLEXCOM1 USART mode */
        usartMode = FLEXCOM1_REGS->FLEX_US_MR;
        usartMode &= ~(FLEX_US_MR_CHRL_Msk | FLEX_US_MR_MODE9_Msk | FLEX_US_MR_PAR_Msk | FLEX_US_MR_NBSTOP_Msk | FLEX_US_MR_OVER_Msk);
        FLEXCOM1_REGS->FLEX_US_MR = usartMode | ((uint32_t)setup->dataWidth | (uint32_t)setup->parity | (uint32_t)setup->stopBits | overSampVal);

        /* Configure FLEXCOM1 USART Baud Rate */
        FLEXCOM1_REGS->FLEX_US_BRGR = FLEX_US_BRGR_CD(brgVal);
        status = true;
    }

    return status;
}

/* This routine is only called from ISR. Hence do not disable/enable USART interrupts. */
static bool FLEXCOM1_USART_TxPullByte(uint8_t* pWrByte)
{
    bool isSuccess = false;

    if (flexcom1UsartObj.wrOutIndex != flexcom1UsartObj.wrInIndex)
    {
        *pWrByte = FLEXCOM1_USART_WriteBuffer[flexcom1UsartObj.wrOutIndex++];

        if (flexcom1UsartObj.wrOutIndex >= FLEXCOM1_USART_WRITE_BUFFER_SIZE)
        {
            flexcom1UsartObj.wrOutIndex = 0;
        }
        isSuccess = true;
    }

    return isSuccess;
}

static inline bool FLEXCOM1_USART_TxPushByte(uint8_t wrByte)
{
    uint32_t tempInIndex;
    bool isSuccess = false;

    tempInIndex = flexcom1UsartObj.wrInIndex + 1;

    if (tempInIndex >= FLEXCOM1_USART_WRITE_BUFFER_SIZE)
    {
        tempInIndex = 0;
    }
    if (tempInIndex != flexcom1UsartObj.wrOutIndex)
    {
        FLEXCOM1_USART_WriteBuffer[flexcom1UsartObj.wrInIndex] = wrByte;
        flexcom1UsartObj.wrInIndex = tempInIndex;
        isSuccess = true;
    }
    else
    {
        /* Queue is full. Report Error. */
    }

    return isSuccess;
}

/* This routine is only called from ISR. Hence do not disable/enable USART interrupts. */
static void FLEXCOM1_USART_WriteNotificationSend(void)
{
    uint32_t nFreeWrBufferCount;

    if (flexcom1UsartObj.isWrNotificationEnabled == true)
    {
        nFreeWrBufferCount = FLEXCOM1_USART_WriteFreeBufferCountGet();

        if(flexcom1UsartObj.wrCallback != NULL)
        {
            if (flexcom1UsartObj.isWrNotifyPersistently == true)
            {
                if (nFreeWrBufferCount >= flexcom1UsartObj.wrThreshold)
                {
                    flexcom1UsartObj.wrCallback(FLEXCOM_USART_EVENT_WRITE_THRESHOLD_REACHED, flexcom1UsartObj.wrContext);
                }
            }
            else
            {
                if (nFreeWrBufferCount == flexcom1UsartObj.wrThreshold)
                {
                    flexcom1UsartObj.wrCallback(FLEXCOM_USART_EVENT_WRITE_THRESHOLD_REACHED, flexcom1UsartObj.wrContext);
                }
            }
        }
    }
}

static size_t FLEXCOM1_USART_WritePendingBytesGet(void)
{
    size_t nPendingTxBytes;

    if ( flexcom1UsartObj.wrInIndex >=  flexcom1UsartObj.wrOutIndex)
    {
        nPendingTxBytes =  flexcom1UsartObj.wrInIndex -  flexcom1UsartObj.wrOutIndex;
    }
    else
    {
        nPendingTxBytes =  (FLEXCOM1_USART_WRITE_BUFFER_SIZE -  flexcom1UsartObj.wrOutIndex) + flexcom1UsartObj.wrInIndex;
    }

    return nPendingTxBytes;
}

size_t FLEXCOM1_USART_WriteCountGet(void)
{
    size_t nPendingTxBytes;

    FLEXCOM1_USART_TX_INT_DISABLE();

    nPendingTxBytes = FLEXCOM1_USART_WritePendingBytesGet();

    /* Enable transmit interrupt only if any data is pending for transmission */
    if (FLEXCOM1_USART_WritePendingBytesGet() > 0)
    {
        FLEXCOM1_USART_TX_INT_ENABLE();
    }

    return nPendingTxBytes;
}

size_t FLEXCOM1_USART_Write(uint8_t* pWrBuffer, const size_t size )
{
    size_t nBytesWritten  = 0;

    FLEXCOM1_USART_TX_INT_DISABLE();

    while (nBytesWritten < size)
    {
        if (FLEXCOM1_USART_TxPushByte(pWrBuffer[nBytesWritten]) == true)
        {
            nBytesWritten++;
        }
        else
        {
            /* Queue is full, exit the loop */
            break;
        }
    }

    /* Check if any data is pending for transmission */
    if (FLEXCOM1_USART_WritePendingBytesGet() > 0)
    {
        /* Enable TX interrupt as data is pending for transmission */
        FLEXCOM1_USART_TX_INT_ENABLE();
    }

    return nBytesWritten;
}

size_t FLEXCOM1_USART_WriteFreeBufferCountGet(void)
{
    return (FLEXCOM1_USART_WRITE_BUFFER_SIZE - 1) - FLEXCOM1_USART_WriteCountGet();
}

size_t FLEXCOM1_USART_WriteBufferSizeGet(void)
{
    return (FLEXCOM1_USART_WRITE_BUFFER_SIZE - 1);
}

bool FLEXCOM1_USART_WriteNotificationEnable(bool isEnabled, bool isPersistent)
{
    bool previousStatus = flexcom1UsartObj.isWrNotificationEnabled;

    flexcom1UsartObj.isWrNotificationEnabled = isEnabled;

    flexcom1UsartObj.isWrNotifyPersistently = isPersistent;

    return previousStatus;
}

void FLEXCOM1_USART_WriteThresholdSet(uint32_t nBytesThreshold)
{
    if (nBytesThreshold > 0)
    {
        flexcom1UsartObj.wrThreshold = nBytesThreshold;
    }
}

void FLEXCOM1_USART_WriteCallbackRegister( FLEXCOM_USART_RING_BUFFER_CALLBACK callback, uintptr_t context)
{
    flexcom1UsartObj.wrCallback = callback;

    flexcom1UsartObj.wrContext = context;
}

/* This routine is only called from ISR. Hence do not disable/enable USART interrupts. */
static inline bool FLEXCOM1_USART_RxPushByte(uint8_t rdByte)
{
    uint32_t tempInIndex;
    bool isSuccess = false;

    tempInIndex = flexcom1UsartObj.rdInIndex + 1;

    if (tempInIndex >= FLEXCOM1_USART_READ_BUFFER_SIZE)
    {
        tempInIndex = 0;
    }

    if (tempInIndex == flexcom1UsartObj.rdOutIndex)
    {
        /* Queue is full - Report it to the application. Application gets a chance to free up space by reading data out from the RX ring buffer */
        if(flexcom1UsartObj.rdCallback != NULL)
        {
            flexcom1UsartObj.rdCallback(FLEXCOM_USART_EVENT_READ_BUFFER_FULL, flexcom1UsartObj.rdContext);

            /* Read the indices again in case application has freed up space in RX ring buffer */
            tempInIndex = flexcom1UsartObj.rdInIndex + 1;

            if (tempInIndex >= FLEXCOM1_USART_READ_BUFFER_SIZE)
            {
                tempInIndex = 0;
            }
        }
    }

    /* Attempt to push the data into the ring buffer */
    if (tempInIndex != flexcom1UsartObj.rdOutIndex)
    {
        FLEXCOM1_USART_ReadBuffer[flexcom1UsartObj.rdInIndex] = rdByte;
        flexcom1UsartObj.rdInIndex = tempInIndex;
        isSuccess = true;
    }
    else
    {
        /* Queue is full. Data will be lost. */
    }

    return isSuccess;
}

/* This routine is only called from ISR. Hence do not disable/enable USART interrupts. */
static void FLEXCOM1_USART_ReadNotificationSend(void)
{
    uint32_t nUnreadBytesAvailable;

    if (flexcom1UsartObj.isRdNotificationEnabled == true)
    {
        nUnreadBytesAvailable = FLEXCOM1_USART_ReadCountGet();

        if(flexcom1UsartObj.rdCallback != NULL)
        {
            if (flexcom1UsartObj.isRdNotifyPersistently == true)
            {
                if (nUnreadBytesAvailable >= flexcom1UsartObj.rdThreshold)
                {
                    flexcom1UsartObj.rdCallback(FLEXCOM_USART_EVENT_READ_THRESHOLD_REACHED, flexcom1UsartObj.rdContext);
                }
            }
            else
            {
                if (nUnreadBytesAvailable == flexcom1UsartObj.rdThreshold)
                {
                    flexcom1UsartObj.rdCallback(FLEXCOM_USART_EVENT_READ_THRESHOLD_REACHED, flexcom1UsartObj.rdContext);
                }
            }
        }
    }
}

size_t FLEXCOM1_USART_Read(uint8_t* pRdBuffer, const size_t size)
{
    size_t nBytesRead = 0;

    while (nBytesRead < size)
    {
        FLEXCOM1_USART_RX_INT_DISABLE();

        if (flexcom1UsartObj.rdOutIndex != flexcom1UsartObj.rdInIndex)
        {
            pRdBuffer[nBytesRead++] = FLEXCOM1_USART_ReadBuffer[flexcom1UsartObj.rdOutIndex++];

            if (flexcom1UsartObj.rdOutIndex >= FLEXCOM1_USART_READ_BUFFER_SIZE)
            {
                flexcom1UsartObj.rdOutIndex = 0;
            }
            FLEXCOM1_USART_RX_INT_ENABLE();
        }
        else
        {
            FLEXCOM1_USART_RX_INT_ENABLE();
            break;
        }
    }

    return nBytesRead;
}

size_t FLEXCOM1_USART_ReadCountGet(void)
{
    size_t nUnreadBytesAvailable;

    FLEXCOM1_USART_RX_INT_DISABLE();

    if ( flexcom1UsartObj.rdInIndex >=  flexcom1UsartObj.rdOutIndex)
    {
        nUnreadBytesAvailable =  flexcom1UsartObj.rdInIndex -  flexcom1UsartObj.rdOutIndex;
    }
    else
    {
        nUnreadBytesAvailable =  (FLEXCOM1_USART_READ_BUFFER_SIZE -  flexcom1UsartObj.rdOutIndex) + flexcom1UsartObj.rdInIndex;
    }

    FLEXCOM1_USART_RX_INT_ENABLE();

    return nUnreadBytesAvailable;
}

size_t FLEXCOM1_USART_ReadFreeBufferCountGet(void)
{
    return (FLEXCOM1_USART_READ_BUFFER_SIZE - 1) - FLEXCOM1_USART_ReadCountGet();
}

size_t FLEXCOM1_USART_ReadBufferSizeGet(void)
{
    return (FLEXCOM1_USART_READ_BUFFER_SIZE - 1);
}

bool FLEXCOM1_USART_ReadNotificationEnable(bool isEnabled, bool isPersistent)
{
    bool previousStatus = flexcom1UsartObj.isRdNotificationEnabled;

    flexcom1UsartObj.isRdNotificationEnabled = isEnabled;

    flexcom1UsartObj.isRdNotifyPersistently = isPersistent;

    return previousStatus;
}

void FLEXCOM1_USART_ReadThresholdSet(uint32_t nBytesThreshold)
{
    if (nBytesThreshold > 0)
    {
        flexcom1UsartObj.rdThreshold = nBytesThreshold;
    }
}

void FLEXCOM1_USART_ReadCallbackRegister( FLEXCOM_USART_RING_BUFFER_CALLBACK callback, uintptr_t context)
{
    flexcom1UsartObj.rdCallback = callback;

    flexcom1UsartObj.rdContext = context;
}

void static FLEXCOM1_USART_ISR_RX_Handler( void )
{
	/* Keep reading until there is a character availabe in the RX FIFO */
	while(FLEX_US_CSR_RXRDY_Msk == (FLEXCOM1_REGS->FLEX_US_CSR & FLEX_US_CSR_RXRDY_Msk))
    {
        if (FLEXCOM1_USART_RxPushByte( (uint8_t )(FLEXCOM1_REGS->FLEX_US_RHR & FLEX_US_RHR_RXCHR_Msk) ) == true)
        {
            FLEXCOM1_USART_ReadNotificationSend();
        }
        else
        {
            /* UART RX buffer is full */
        }
    }			    
}

void static FLEXCOM1_USART_ISR_TX_Handler( void )
{
	uint8_t wrByte;
	
	/* Keep writing to the TX FIFO as long as there is space */
    while(FLEX_US_CSR_TXEMPTY_Msk == (FLEXCOM1_REGS->FLEX_US_CSR & FLEX_US_CSR_TXEMPTY_Msk))
    {	
        if (FLEXCOM1_USART_TxPullByte(&wrByte) == true)
        {
			FLEXCOM1_REGS->FLEX_US_THR = wrByte;

            /* Send notification */
            FLEXCOM1_USART_WriteNotificationSend();
        }
        else
        {
            /* Nothing to transmit. Disable the data register empty interrupt. */
            FLEXCOM1_USART_TX_INT_DISABLE();
            break;
        }
    }		    
}

void FLEXCOM1_InterruptHandler( void )
{
    /* Channel status */
    uint32_t channelStatus = FLEXCOM1_REGS->FLEX_US_CSR;

    /* Error status */
    uint32_t errorStatus = (channelStatus & (FLEX_US_CSR_OVRE_Msk | FLEX_US_CSR_FRAME_Msk | FLEX_US_CSR_PARE_Msk));

    if(errorStatus != 0)
    {        
        /* Client must call FLEXCOM1_USART_ErrorGet() function to clear the errors */

        /* USART errors are normally associated with the receiver, hence calling
         * receiver context */
        if( flexcom1UsartObj.rdCallback != NULL )
        {
			flexcom1UsartObj.rdCallback(FLEXCOM_USART_EVENT_READ_ERROR, flexcom1UsartObj.rdContext);			            
        }
		
		/* Disable Read, Overrun, Parity and Framing error interrupts */
        FLEXCOM1_REGS->FLEX_US_IDR = (FLEX_US_IDR_RXRDY_Msk | FLEX_US_IDR_FRAME_Msk | FLEX_US_IDR_PARE_Msk | FLEX_US_IDR_OVRE_Msk);
    }

    /* Receiver status */
    if(FLEX_US_CSR_RXRDY_Msk == (channelStatus & FLEX_US_CSR_RXRDY_Msk))
    {
        FLEXCOM1_USART_ISR_RX_Handler();
    }
    
    /* Transmitter status */
    if(FLEX_US_CSR_TXEMPTY_Msk == (channelStatus & FLEX_US_CSR_TXEMPTY_Msk))
    {
        FLEXCOM1_USART_ISR_TX_Handler();
    }
}
