/*******************************************************************************
  FLEXCOM5 USART PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_flexcom5_usart.c

  Summary:
    FLEXCOM5 USART PLIB Implementation File

  Description
    This file defines the interface to the FLEXCOM5 USART
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

#include "plib_flexcom5_usart.h"

#define FLEXCOM5_USART_READ_BUFFER_SIZE      20

/* Disable Read, Overrun, Parity and Framing error interrupts */
#define FLEXCOM5_USART_RX_INT_DISABLE()      FLEXCOM5_REGS->FLEX_US_IDR = (FLEX_US_IDR_RXRDY_Msk | FLEX_US_IDR_FRAME_Msk | FLEX_US_IDR_PARE_Msk | FLEX_US_IDR_OVRE_Msk)

/* Enable Read, Overrun, Parity and Framing error interrupts */		
#define FLEXCOM5_USART_RX_INT_ENABLE()       FLEXCOM5_REGS->FLEX_US_IER = (FLEX_US_IER_RXRDY_Msk | FLEX_US_IER_FRAME_Msk | FLEX_US_IER_PARE_Msk | FLEX_US_IER_OVRE_Msk)

static uint8_t FLEXCOM5_USART_ReadBuffer[FLEXCOM5_USART_READ_BUFFER_SIZE];

#define FLEXCOM5_USART_WRITE_BUFFER_SIZE     128
#define FLEXCOM5_USART_TX_INT_DISABLE()      FLEXCOM5_REGS->FLEX_US_IDR = FLEX_US_IDR_TXEMPTY_Msk
#define FLEXCOM5_USART_TX_INT_ENABLE()       FLEXCOM5_REGS->FLEX_US_IER = FLEX_US_IER_TXEMPTY_Msk

static uint8_t FLEXCOM5_USART_WriteBuffer[FLEXCOM5_USART_WRITE_BUFFER_SIZE];

// *****************************************************************************
// *****************************************************************************
// Section: FLEXCOM5 USART Ring Buffer Implementation
// *****************************************************************************
// *****************************************************************************

FLEXCOM_USART_RING_BUFFER_OBJECT flexcom5UsartObj;

void FLEXCOM5_USART_Initialize( void )
{
    /* Set FLEXCOM USART operating mode */
    FLEXCOM5_REGS->FLEX_MR = FLEX_MR_OPMODE_USART;

    /* Reset FLEXCOM5 USART */
    FLEXCOM5_REGS->FLEX_US_CR = (FLEX_US_CR_RSTRX_Msk | FLEX_US_CR_RSTTX_Msk | FLEX_US_CR_RSTSTA_Msk);

    /* Enable FLEXCOM5 USART */
    FLEXCOM5_REGS->FLEX_US_CR = (FLEX_US_CR_TXEN_Msk | FLEX_US_CR_RXEN_Msk);

    /* Configure FLEXCOM5 USART mode */
    FLEXCOM5_REGS->FLEX_US_MR = ((FLEX_US_MR_USCLKS_MCK) | FLEX_US_MR_CHRL_8_BIT | FLEX_US_MR_PAR_NO | FLEX_US_MR_NBSTOP_1_BIT | (0 << FLEX_US_MR_OVER_Pos));

    /* Configure FLEXCOM5 USART Baud Rate */
    FLEXCOM5_REGS->FLEX_US_BRGR = FLEX_US_BRGR_CD(108);
	
	flexcom5UsartObj.rdCallback = NULL;
    flexcom5UsartObj.rdInIndex = flexcom5UsartObj.rdOutIndex = 0;
    flexcom5UsartObj.isRdNotificationEnabled = false;
    flexcom5UsartObj.isRdNotifyPersistently = false;
    flexcom5UsartObj.rdThreshold = 0;
    flexcom5UsartObj.wrCallback = NULL;
    flexcom5UsartObj.wrInIndex = flexcom5UsartObj.wrOutIndex = 0;
    flexcom5UsartObj.isWrNotificationEnabled = false;
    flexcom5UsartObj.isWrNotifyPersistently = false;
    flexcom5UsartObj.wrThreshold = 0;   
	
	FLEXCOM5_USART_RX_INT_ENABLE();
}

void static FLEXCOM5_USART_ErrorClear( void )
{
    uint8_t dummyData = 0u;

    FLEXCOM5_REGS->FLEX_US_CR = FLEX_US_CR_RSTSTA_Msk;

    /* Flush existing error bytes from the RX FIFO */
    while( FLEX_US_CSR_RXRDY_Msk == (FLEXCOM5_REGS->FLEX_US_CSR& FLEX_US_CSR_RXRDY_Msk) )
    {
        dummyData = (FLEXCOM5_REGS->FLEX_US_RHR& FLEX_US_RHR_RXCHR_Msk);
    }

    /* Ignore the warning */
    (void)dummyData;

    return;
}

FLEXCOM_USART_ERROR FLEXCOM5_USART_ErrorGet( void )
{
    FLEXCOM_USART_ERROR errors = FLEXCOM_USART_ERROR_NONE;
    uint32_t status = FLEXCOM5_REGS->FLEX_US_CSR;

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
        FLEXCOM5_USART_ErrorClear();
    }

    /* All errors are cleared, but send the previous error state */
    return errors;
}

bool FLEXCOM5_USART_SerialSetup( FLEXCOM_USART_SERIAL_SETUP *setup, uint32_t srcClkFreq )
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
            srcClkFreq = FLEXCOM5_USART_FrequencyGet();
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

        /* Configure FLEXCOM5 USART mode */
        usartMode = FLEXCOM5_REGS->FLEX_US_MR;
        usartMode &= ~(FLEX_US_MR_CHRL_Msk | FLEX_US_MR_MODE9_Msk | FLEX_US_MR_PAR_Msk | FLEX_US_MR_NBSTOP_Msk | FLEX_US_MR_OVER_Msk);
        FLEXCOM5_REGS->FLEX_US_MR = usartMode | ((uint32_t)setup->dataWidth | (uint32_t)setup->parity | (uint32_t)setup->stopBits | overSampVal);

        /* Configure FLEXCOM5 USART Baud Rate */
        FLEXCOM5_REGS->FLEX_US_BRGR = FLEX_US_BRGR_CD(brgVal);
        status = true;
    }

    return status;
}

/* This routine is only called from ISR. Hence do not disable/enable USART interrupts. */
static bool FLEXCOM5_USART_TxPullByte(uint8_t* pWrByte)
{
    bool isSuccess = false;

    if (flexcom5UsartObj.wrOutIndex != flexcom5UsartObj.wrInIndex)
    {
        *pWrByte = FLEXCOM5_USART_WriteBuffer[flexcom5UsartObj.wrOutIndex++];

        if (flexcom5UsartObj.wrOutIndex >= FLEXCOM5_USART_WRITE_BUFFER_SIZE)
        {
            flexcom5UsartObj.wrOutIndex = 0;
        }
        isSuccess = true;
    }

    return isSuccess;
}

static inline bool FLEXCOM5_USART_TxPushByte(uint8_t wrByte)
{
    uint32_t tempInIndex;
    bool isSuccess = false;

    tempInIndex = flexcom5UsartObj.wrInIndex + 1;

    if (tempInIndex >= FLEXCOM5_USART_WRITE_BUFFER_SIZE)
    {
        tempInIndex = 0;
    }
    if (tempInIndex != flexcom5UsartObj.wrOutIndex)
    {
        FLEXCOM5_USART_WriteBuffer[flexcom5UsartObj.wrInIndex] = wrByte;
        flexcom5UsartObj.wrInIndex = tempInIndex;
        isSuccess = true;
    }
    else
    {
        /* Queue is full. Report Error. */
    }

    return isSuccess;
}

/* This routine is only called from ISR. Hence do not disable/enable USART interrupts. */
static void FLEXCOM5_USART_WriteNotificationSend(void)
{
    uint32_t nFreeWrBufferCount;

    if (flexcom5UsartObj.isWrNotificationEnabled == true)
    {
        nFreeWrBufferCount = FLEXCOM5_USART_WriteFreeBufferCountGet();

        if(flexcom5UsartObj.wrCallback != NULL)
        {
            if (flexcom5UsartObj.isWrNotifyPersistently == true)
            {
                if (nFreeWrBufferCount >= flexcom5UsartObj.wrThreshold)
                {
                    flexcom5UsartObj.wrCallback(FLEXCOM_USART_EVENT_WRITE_THRESHOLD_REACHED, flexcom5UsartObj.wrContext);
                }
            }
            else
            {
                if (nFreeWrBufferCount == flexcom5UsartObj.wrThreshold)
                {
                    flexcom5UsartObj.wrCallback(FLEXCOM_USART_EVENT_WRITE_THRESHOLD_REACHED, flexcom5UsartObj.wrContext);
                }
            }
        }
    }
}

static size_t FLEXCOM5_USART_WritePendingBytesGet(void)
{
    size_t nPendingTxBytes;

    if ( flexcom5UsartObj.wrInIndex >=  flexcom5UsartObj.wrOutIndex)
    {
        nPendingTxBytes =  flexcom5UsartObj.wrInIndex -  flexcom5UsartObj.wrOutIndex;
    }
    else
    {
        nPendingTxBytes =  (FLEXCOM5_USART_WRITE_BUFFER_SIZE -  flexcom5UsartObj.wrOutIndex) + flexcom5UsartObj.wrInIndex;
    }

    return nPendingTxBytes;
}

size_t FLEXCOM5_USART_WriteCountGet(void)
{
    size_t nPendingTxBytes;

    FLEXCOM5_USART_TX_INT_DISABLE();

    nPendingTxBytes = FLEXCOM5_USART_WritePendingBytesGet();

    /* Enable transmit interrupt only if any data is pending for transmission */
    if (FLEXCOM5_USART_WritePendingBytesGet() > 0)
    {
        FLEXCOM5_USART_TX_INT_ENABLE();
    }

    return nPendingTxBytes;
}

size_t FLEXCOM5_USART_Write(uint8_t* pWrBuffer, const size_t size )
{
    size_t nBytesWritten  = 0;

    FLEXCOM5_USART_TX_INT_DISABLE();

    while (nBytesWritten < size)
    {
        if (FLEXCOM5_USART_TxPushByte(pWrBuffer[nBytesWritten]) == true)
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
    if (FLEXCOM5_USART_WritePendingBytesGet() > 0)
    {
        /* Enable TX interrupt as data is pending for transmission */
        FLEXCOM5_USART_TX_INT_ENABLE();
    }

    return nBytesWritten;
}

size_t FLEXCOM5_USART_WriteFreeBufferCountGet(void)
{
    return (FLEXCOM5_USART_WRITE_BUFFER_SIZE - 1) - FLEXCOM5_USART_WriteCountGet();
}

size_t FLEXCOM5_USART_WriteBufferSizeGet(void)
{
    return (FLEXCOM5_USART_WRITE_BUFFER_SIZE - 1);
}

bool FLEXCOM5_USART_WriteNotificationEnable(bool isEnabled, bool isPersistent)
{
    bool previousStatus = flexcom5UsartObj.isWrNotificationEnabled;

    flexcom5UsartObj.isWrNotificationEnabled = isEnabled;

    flexcom5UsartObj.isWrNotifyPersistently = isPersistent;

    return previousStatus;
}

void FLEXCOM5_USART_WriteThresholdSet(uint32_t nBytesThreshold)
{
    if (nBytesThreshold > 0)
    {
        flexcom5UsartObj.wrThreshold = nBytesThreshold;
    }
}

void FLEXCOM5_USART_WriteCallbackRegister( FLEXCOM_USART_RING_BUFFER_CALLBACK callback, uintptr_t context)
{
    flexcom5UsartObj.wrCallback = callback;

    flexcom5UsartObj.wrContext = context;
}

/* This routine is only called from ISR. Hence do not disable/enable USART interrupts. */
static inline bool FLEXCOM5_USART_RxPushByte(uint8_t rdByte)
{
    uint32_t tempInIndex;
    bool isSuccess = false;

    tempInIndex = flexcom5UsartObj.rdInIndex + 1;

    if (tempInIndex >= FLEXCOM5_USART_READ_BUFFER_SIZE)
    {
        tempInIndex = 0;
    }

    if (tempInIndex == flexcom5UsartObj.rdOutIndex)
    {
        /* Queue is full - Report it to the application. Application gets a chance to free up space by reading data out from the RX ring buffer */
        if(flexcom5UsartObj.rdCallback != NULL)
        {
            flexcom5UsartObj.rdCallback(FLEXCOM_USART_EVENT_READ_BUFFER_FULL, flexcom5UsartObj.rdContext);

            /* Read the indices again in case application has freed up space in RX ring buffer */
            tempInIndex = flexcom5UsartObj.rdInIndex + 1;

            if (tempInIndex >= FLEXCOM5_USART_READ_BUFFER_SIZE)
            {
                tempInIndex = 0;
            }
        }
    }

    /* Attempt to push the data into the ring buffer */
    if (tempInIndex != flexcom5UsartObj.rdOutIndex)
    {
        FLEXCOM5_USART_ReadBuffer[flexcom5UsartObj.rdInIndex] = rdByte;
        flexcom5UsartObj.rdInIndex = tempInIndex;
        isSuccess = true;
    }
    else
    {
        /* Queue is full. Data will be lost. */
    }

    return isSuccess;
}

/* This routine is only called from ISR. Hence do not disable/enable USART interrupts. */
static void FLEXCOM5_USART_ReadNotificationSend(void)
{
    uint32_t nUnreadBytesAvailable;

    if (flexcom5UsartObj.isRdNotificationEnabled == true)
    {
        nUnreadBytesAvailable = FLEXCOM5_USART_ReadCountGet();

        if(flexcom5UsartObj.rdCallback != NULL)
        {
            if (flexcom5UsartObj.isRdNotifyPersistently == true)
            {
                if (nUnreadBytesAvailable >= flexcom5UsartObj.rdThreshold)
                {
                    flexcom5UsartObj.rdCallback(FLEXCOM_USART_EVENT_READ_THRESHOLD_REACHED, flexcom5UsartObj.rdContext);
                }
            }
            else
            {
                if (nUnreadBytesAvailable == flexcom5UsartObj.rdThreshold)
                {
                    flexcom5UsartObj.rdCallback(FLEXCOM_USART_EVENT_READ_THRESHOLD_REACHED, flexcom5UsartObj.rdContext);
                }
            }
        }
    }
}

size_t FLEXCOM5_USART_Read(uint8_t* pRdBuffer, const size_t size)
{
    size_t nBytesRead = 0;

    while (nBytesRead < size)
    {
        FLEXCOM5_USART_RX_INT_DISABLE();

        if (flexcom5UsartObj.rdOutIndex != flexcom5UsartObj.rdInIndex)
        {
            pRdBuffer[nBytesRead++] = FLEXCOM5_USART_ReadBuffer[flexcom5UsartObj.rdOutIndex++];

            if (flexcom5UsartObj.rdOutIndex >= FLEXCOM5_USART_READ_BUFFER_SIZE)
            {
                flexcom5UsartObj.rdOutIndex = 0;
            }
            FLEXCOM5_USART_RX_INT_ENABLE();
        }
        else
        {
            FLEXCOM5_USART_RX_INT_ENABLE();
            break;
        }
    }

    return nBytesRead;
}

size_t FLEXCOM5_USART_ReadCountGet(void)
{
    size_t nUnreadBytesAvailable;

    FLEXCOM5_USART_RX_INT_DISABLE();

    if ( flexcom5UsartObj.rdInIndex >=  flexcom5UsartObj.rdOutIndex)
    {
        nUnreadBytesAvailable =  flexcom5UsartObj.rdInIndex -  flexcom5UsartObj.rdOutIndex;
    }
    else
    {
        nUnreadBytesAvailable =  (FLEXCOM5_USART_READ_BUFFER_SIZE -  flexcom5UsartObj.rdOutIndex) + flexcom5UsartObj.rdInIndex;
    }

    FLEXCOM5_USART_RX_INT_ENABLE();

    return nUnreadBytesAvailable;
}

size_t FLEXCOM5_USART_ReadFreeBufferCountGet(void)
{
    return (FLEXCOM5_USART_READ_BUFFER_SIZE - 1) - FLEXCOM5_USART_ReadCountGet();
}

size_t FLEXCOM5_USART_ReadBufferSizeGet(void)
{
    return (FLEXCOM5_USART_READ_BUFFER_SIZE - 1);
}

bool FLEXCOM5_USART_ReadNotificationEnable(bool isEnabled, bool isPersistent)
{
    bool previousStatus = flexcom5UsartObj.isRdNotificationEnabled;

    flexcom5UsartObj.isRdNotificationEnabled = isEnabled;

    flexcom5UsartObj.isRdNotifyPersistently = isPersistent;

    return previousStatus;
}

void FLEXCOM5_USART_ReadThresholdSet(uint32_t nBytesThreshold)
{
    if (nBytesThreshold > 0)
    {
        flexcom5UsartObj.rdThreshold = nBytesThreshold;
    }
}

void FLEXCOM5_USART_ReadCallbackRegister( FLEXCOM_USART_RING_BUFFER_CALLBACK callback, uintptr_t context)
{
    flexcom5UsartObj.rdCallback = callback;

    flexcom5UsartObj.rdContext = context;
}

void static FLEXCOM5_USART_ISR_RX_Handler( void )
{
	/* Keep reading until there is a character availabe in the RX FIFO */
	while(FLEX_US_CSR_RXRDY_Msk == (FLEXCOM5_REGS->FLEX_US_CSR & FLEX_US_CSR_RXRDY_Msk))
    {
        if (FLEXCOM5_USART_RxPushByte( (uint8_t )(FLEXCOM5_REGS->FLEX_US_RHR & FLEX_US_RHR_RXCHR_Msk) ) == true)
        {
            FLEXCOM5_USART_ReadNotificationSend();
        }
        else
        {
            /* UART RX buffer is full */
        }
    }			    
}

void static FLEXCOM5_USART_ISR_TX_Handler( void )
{
	uint8_t wrByte;
	
	/* Keep writing to the TX FIFO as long as there is space */
    while(FLEX_US_CSR_TXEMPTY_Msk == (FLEXCOM5_REGS->FLEX_US_CSR & FLEX_US_CSR_TXEMPTY_Msk))
    {	
        if (FLEXCOM5_USART_TxPullByte(&wrByte) == true)
        {
			FLEXCOM5_REGS->FLEX_US_THR = wrByte;

            /* Send notification */
            FLEXCOM5_USART_WriteNotificationSend();
        }
        else
        {
            /* Nothing to transmit. Disable the data register empty interrupt. */
            FLEXCOM5_USART_TX_INT_DISABLE();
            break;
        }
    }		    
}

void FLEXCOM5_InterruptHandler( void )
{
    /* Channel status */
    uint32_t channelStatus = FLEXCOM5_REGS->FLEX_US_CSR;

    /* Error status */
    uint32_t errorStatus = (channelStatus & (FLEX_US_CSR_OVRE_Msk | FLEX_US_CSR_FRAME_Msk | FLEX_US_CSR_PARE_Msk));

    if(errorStatus != 0)
    {        
        /* Client must call FLEXCOM5_USART_ErrorGet() function to clear the errors */

        /* USART errors are normally associated with the receiver, hence calling
         * receiver context */
        if( flexcom5UsartObj.rdCallback != NULL )
        {
			flexcom5UsartObj.rdCallback(FLEXCOM_USART_EVENT_READ_ERROR, flexcom5UsartObj.rdContext);			            
        }
		
		/* Disable Read, Overrun, Parity and Framing error interrupts */
        FLEXCOM5_REGS->FLEX_US_IDR = (FLEX_US_IDR_RXRDY_Msk | FLEX_US_IDR_FRAME_Msk | FLEX_US_IDR_PARE_Msk | FLEX_US_IDR_OVRE_Msk);
    }

    /* Receiver status */
    if(FLEX_US_CSR_RXRDY_Msk == (channelStatus & FLEX_US_CSR_RXRDY_Msk))
    {
        FLEXCOM5_USART_ISR_RX_Handler();
    }
    
    /* Transmitter status */
    if(FLEX_US_CSR_TXEMPTY_Msk == (channelStatus & FLEX_US_CSR_TXEMPTY_Msk))
    {
        FLEXCOM5_USART_ISR_TX_Handler();
    }
}
