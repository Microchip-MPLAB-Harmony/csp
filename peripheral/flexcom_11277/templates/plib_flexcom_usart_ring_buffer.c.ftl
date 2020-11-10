/*******************************************************************************
  ${FLEXCOM_INSTANCE_NAME} USART PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${FLEXCOM_INSTANCE_NAME?lower_case}_usart.c

  Summary:
    ${FLEXCOM_INSTANCE_NAME} USART PLIB Implementation File

  Description
    This file defines the interface to the ${FLEXCOM_INSTANCE_NAME} USART
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

#include "plib_${FLEXCOM_INSTANCE_NAME?lower_case}_${FLEXCOM_MODE?lower_case}.h"

#define ${FLEXCOM_INSTANCE_NAME}_USART_READ_BUFFER_SIZE             ${USART_RX_RING_BUFFER_SIZE}
#define ${FLEXCOM_INSTANCE_NAME}_USART_READ_BUFFER_SIZE_9BIT        (${USART_RX_RING_BUFFER_SIZE} >> 1)

/* Disable Read, Overrun, Parity and Framing error interrupts */
#define ${FLEXCOM_INSTANCE_NAME}_USART_RX_INT_DISABLE()      USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_IDR = (US_IDR_RXRDY_Msk | US_IDR_FRAME_Msk | US_IDR_PARE_Msk | US_IDR_OVRE_Msk)
/* Enable Read, Overrun, Parity and Framing error interrupts */
#define ${FLEXCOM_INSTANCE_NAME}_USART_RX_INT_ENABLE()       USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_IER = (US_IER_RXRDY_Msk | US_IER_FRAME_Msk | US_IER_PARE_Msk | US_IER_OVRE_Msk)

static uint8_t ${FLEXCOM_INSTANCE_NAME}_USART_ReadBuffer[${FLEXCOM_INSTANCE_NAME}_USART_READ_BUFFER_SIZE];

#define ${FLEXCOM_INSTANCE_NAME}_USART_WRITE_BUFFER_SIZE            ${USART_TX_RING_BUFFER_SIZE}
#define ${FLEXCOM_INSTANCE_NAME}_USART_WRITE_BUFFER_SIZE_9BIT       (${USART_TX_RING_BUFFER_SIZE} >> 1)

#define ${FLEXCOM_INSTANCE_NAME}_USART_TX_INT_DISABLE()      USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_IDR = US_IDR_TXRDY_Msk
#define ${FLEXCOM_INSTANCE_NAME}_USART_TX_INT_ENABLE()       USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_IER = US_IER_TXRDY_Msk

static uint8_t ${FLEXCOM_INSTANCE_NAME}_USART_WriteBuffer[${FLEXCOM_INSTANCE_NAME}_USART_WRITE_BUFFER_SIZE];

// *****************************************************************************
// *****************************************************************************
// Section: ${FLEXCOM_INSTANCE_NAME} ${FLEXCOM_MODE} Ring Buffer Implementation
// *****************************************************************************
// *****************************************************************************

FLEXCOM_USART_RING_BUFFER_OBJECT ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj;

void ${FLEXCOM_INSTANCE_NAME}_USART_Initialize( void )
{
    /* Set FLEXCOM USART operating mode */
    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEXCOM_MR = FLEXCOM_MR_OPMODE_USART;

    /* Reset ${FLEXCOM_INSTANCE_NAME} USART */
    USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_CR = (US_CR_RSTRX_Msk | US_CR_RSTTX_Msk | US_CR_RSTSTA_Msk);

    /* Enable ${FLEXCOM_INSTANCE_NAME} USART */
    USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_CR = (US_CR_TXEN_Msk | US_CR_RXEN_Msk);

    /* Configure ${FLEXCOM_INSTANCE_NAME} USART mode */
    USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_MR = ((US_MR_USCLKS_${FLEXCOM_USART_MR_USCLKS}) ${(FLEX_USART_MR_MODE9 == true)?then('| US_MR_MODE9_Msk', '| US_MR_CHRL${FLEX_USART_MR_CHRL}')} | US_MR_PAR_${FLEX_USART_MR_PAR} | US_MR_NBSTOP${FLEX_USART_MR_NBSTOP} | (${FLEXCOM_USART_MR_OVER} << US_MR_OVER_Pos));

    /* Configure ${FLEXCOM_INSTANCE_NAME} USART Baud Rate */
    USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_BRGR = US_BRGR_CD(${BRG_VALUE});

    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rdCallback = NULL;
    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rdInIndex = 0;
    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rdOutIndex = 0;
    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.isRdNotificationEnabled = false;
    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.isRdNotifyPersistently = false;
    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rdThreshold = 0;
    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.wrCallback = NULL;
    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.wrInIndex = 0;
    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.wrOutIndex = 0;
    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.isWrNotificationEnabled = false;
    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.isWrNotifyPersistently = false;
    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.wrThreshold = 0;
    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.errorStatus = FLEXCOM_USART_ERROR_NONE;

    if (USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_MR & US_MR_MODE9_Msk)
    {
        ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rdBufferSize = ${FLEXCOM_INSTANCE_NAME}_USART_READ_BUFFER_SIZE_9BIT;
        ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.wrBufferSize = ${FLEXCOM_INSTANCE_NAME}_USART_WRITE_BUFFER_SIZE_9BIT;
    }
    else
    {
        ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rdBufferSize = ${FLEXCOM_INSTANCE_NAME}_USART_READ_BUFFER_SIZE;
        ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.wrBufferSize = ${FLEXCOM_INSTANCE_NAME}_USART_WRITE_BUFFER_SIZE;
    }

    ${FLEXCOM_INSTANCE_NAME}_USART_RX_INT_ENABLE();
}

void static ${FLEXCOM_INSTANCE_NAME}_USART_ErrorClear( void )
{
    uint8_t dummyData = 0u;

    USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_CR = US_CR_RSTSTA_Msk;

    /* Flush existing error bytes from the RX FIFO */
    while (USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_CSR& US_CSR_RXRDY_Msk)
    {
        dummyData = (USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_RHR & US_RHR_RXCHR_Msk);
    }

    /* Ignore the warning */
    (void)dummyData;
}

FLEXCOM_USART_ERROR ${FLEXCOM_INSTANCE_NAME}_USART_ErrorGet( void )
{
    FLEXCOM_USART_ERROR errors = ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.errorStatus;

    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.errorStatus = FLEXCOM_USART_ERROR_NONE;

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
        else if (srcClkFreq >= (8 * baud))
        {
            brgVal = (srcClkFreq / (8 * baud));
            overSampVal = (1 << US_MR_OVER_Pos) & US_MR_OVER_Msk;
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

        /* Configure ${FLEXCOM_INSTANCE_NAME} USART mode */
        usartMode = USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_MR;
        usartMode &= ~(US_MR_CHRL_Msk | US_MR_MODE9_Msk | US_MR_PAR_Msk | US_MR_NBSTOP_Msk | US_MR_OVER_Msk);
        USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_MR = usartMode | ((uint32_t)setup->dataWidth | (uint32_t)setup->parity | (uint32_t)setup->stopBits | overSampVal);

        /* Configure ${FLEXCOM_INSTANCE_NAME} USART Baud Rate */
        USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_BRGR = US_BRGR_CD(brgVal);

        if (USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_MR & US_MR_MODE9_Msk)
        {
            ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rdBufferSize = ${FLEXCOM_INSTANCE_NAME}_USART_READ_BUFFER_SIZE_9BIT;
            ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.wrBufferSize = ${FLEXCOM_INSTANCE_NAME}_USART_WRITE_BUFFER_SIZE_9BIT;
        }
        else
        {
            ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rdBufferSize = ${FLEXCOM_INSTANCE_NAME}_USART_READ_BUFFER_SIZE;
            ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.wrBufferSize = ${FLEXCOM_INSTANCE_NAME}_USART_WRITE_BUFFER_SIZE;
        }

        status = true;
    }

    return status;
}

/* This routine is only called from ISR. Hence do not disable/enable USART interrupts. */
static bool ${FLEXCOM_INSTANCE_NAME}_USART_TxPullByte(uint16_t* pWrByte)
{
    bool isSuccess = false;
    uint32_t wrOutIndex = ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.wrOutIndex;
    uint32_t wrInIndex = ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.wrInIndex;

    if (wrOutIndex != wrInIndex)
    {
        if (USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_MR & US_MR_MODE9_Msk)
        {
            *pWrByte = ((uint16_t*)&${FLEXCOM_INSTANCE_NAME}_USART_WriteBuffer)[wrOutIndex++];
        }
        else
        {
            *pWrByte = ${FLEXCOM_INSTANCE_NAME}_USART_WriteBuffer[wrOutIndex++];
        }


        if (wrOutIndex >= ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.wrBufferSize)
        {
            wrOutIndex = 0;
        }

        ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.wrOutIndex = wrOutIndex;

        isSuccess = true;
    }

    return isSuccess;
}

static inline bool ${FLEXCOM_INSTANCE_NAME}_USART_TxPushByte(uint16_t wrByte)
{
    uint32_t tempInIndex;
    uint32_t wrOutIndex = ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.wrOutIndex;
    uint32_t wrInIndex = ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.wrInIndex;

    bool isSuccess = false;

    tempInIndex = wrInIndex + 1;

    if (tempInIndex >= ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.wrBufferSize)
    {
        tempInIndex = 0;
    }
    if (tempInIndex != wrOutIndex)
    {
        if (USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_MR & US_MR_MODE9_Msk)
        {
            ((uint16_t*)&${FLEXCOM_INSTANCE_NAME}_USART_WriteBuffer)[wrInIndex] = wrByte;
        }
        else
        {
            ${FLEXCOM_INSTANCE_NAME}_USART_WriteBuffer[wrInIndex] = (uint8_t)wrByte;
        }

        ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.wrInIndex = tempInIndex;

        isSuccess = true;
    }
    else
    {
        /* Queue is full. Report Error. */
    }

    return isSuccess;
}

/* This routine is only called from ISR. Hence do not disable/enable USART interrupts. */
static void ${FLEXCOM_INSTANCE_NAME}_USART_WriteNotificationSend(void)
{
    uint32_t nFreeWrBufferCount;

    if (${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.isWrNotificationEnabled == true)
    {
        nFreeWrBufferCount = ${FLEXCOM_INSTANCE_NAME}_USART_WriteFreeBufferCountGet();

        if(${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.wrCallback != NULL)
        {
            if (${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.isWrNotifyPersistently == true)
            {
                if (nFreeWrBufferCount >= ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.wrThreshold)
                {
                    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.wrCallback(FLEXCOM_USART_EVENT_WRITE_THRESHOLD_REACHED, ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.wrContext);
                }
            }
            else
            {
                if (nFreeWrBufferCount == ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.wrThreshold)
                {
                    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.wrCallback(FLEXCOM_USART_EVENT_WRITE_THRESHOLD_REACHED, ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.wrContext);
                }
            }
        }
    }
}

static size_t ${FLEXCOM_INSTANCE_NAME}_USART_WritePendingBytesGet(void)
{
    size_t nPendingTxBytes;

    /* Take a snapshot of indices to avoid creation of critical section */
    uint32_t wrOutIndex = ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.wrOutIndex;
    uint32_t wrInIndex = ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.wrInIndex;

    if ( wrInIndex >=  wrOutIndex)
    {
        nPendingTxBytes =  wrInIndex - wrOutIndex;
    }
    else
    {
        nPendingTxBytes =  (${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.wrBufferSize -  wrOutIndex) + wrInIndex;
    }

    return nPendingTxBytes;
}

size_t ${FLEXCOM_INSTANCE_NAME}_USART_WriteCountGet(void)
{
    size_t nPendingTxBytes;

    nPendingTxBytes = ${FLEXCOM_INSTANCE_NAME}_USART_WritePendingBytesGet();

    return nPendingTxBytes;
}

size_t ${FLEXCOM_INSTANCE_NAME}_USART_Write(uint8_t* pWrBuffer, const size_t size )
{
    size_t nBytesWritten  = 0;

    while (nBytesWritten < size)
    {
        if (USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_MR & US_MR_MODE9_Msk)
        {
            if (${FLEXCOM_INSTANCE_NAME}_USART_TxPushByte(((uint16_t*)pWrBuffer)[nBytesWritten]) == true)
            {
                nBytesWritten++;
            }
            else
            {
                /* Queue is full, exit the loop */
                break;
            }
        }
        else
        {
            if (${FLEXCOM_INSTANCE_NAME}_USART_TxPushByte(pWrBuffer[nBytesWritten]) == true)
            {
                nBytesWritten++;
            }
            else
            {
                /* Queue is full, exit the loop */
                break;
            }
        }

    }

    /* Check if any data is pending for transmission */
    if (${FLEXCOM_INSTANCE_NAME}_USART_WritePendingBytesGet() > 0)
    {
        /* Enable TX interrupt as data is pending for transmission */
        ${FLEXCOM_INSTANCE_NAME}_USART_TX_INT_ENABLE();
    }

    return nBytesWritten;
}

size_t ${FLEXCOM_INSTANCE_NAME}_USART_WriteFreeBufferCountGet(void)
{
    return (${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.wrBufferSize - 1) - ${FLEXCOM_INSTANCE_NAME}_USART_WriteCountGet();
}

size_t ${FLEXCOM_INSTANCE_NAME}_USART_WriteBufferSizeGet(void)
{
    return (${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.wrBufferSize - 1);
}

bool ${FLEXCOM_INSTANCE_NAME}_USART_WriteNotificationEnable(bool isEnabled, bool isPersistent)
{
    bool previousStatus = ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.isWrNotificationEnabled;

    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.isWrNotificationEnabled = isEnabled;

    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.isWrNotifyPersistently = isPersistent;

    return previousStatus;
}

void ${FLEXCOM_INSTANCE_NAME}_USART_WriteThresholdSet(uint32_t nBytesThreshold)
{
    if (nBytesThreshold > 0)
    {
        ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.wrThreshold = nBytesThreshold;
    }
}

void ${FLEXCOM_INSTANCE_NAME}_USART_WriteCallbackRegister( FLEXCOM_USART_RING_BUFFER_CALLBACK callback, uintptr_t context)
{
    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.wrCallback = callback;

    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.wrContext = context;
}

/* This routine is only called from ISR. Hence do not disable/enable USART interrupts. */
static inline bool ${FLEXCOM_INSTANCE_NAME}_USART_RxPushByte(uint16_t rdByte)
{
    uint32_t tempInIndex;
    bool isSuccess = false;

    tempInIndex = ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rdInIndex + 1;

    if (tempInIndex >= ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rdBufferSize)
    {
        tempInIndex = 0;
    }

    if (tempInIndex == ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rdOutIndex)
    {
        /* Queue is full - Report it to the application. Application gets a chance to free up space by reading data out from the RX ring buffer */
        if(${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rdCallback != NULL)
        {
            ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rdCallback(FLEXCOM_USART_EVENT_READ_BUFFER_FULL, ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rdContext);

            /* Read the indices again in case application has freed up space in RX ring buffer */
            tempInIndex = ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rdInIndex + 1;

            if (tempInIndex >= ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rdBufferSize)
            {
                tempInIndex = 0;
            }
        }
    }

    /* Attempt to push the data into the ring buffer */
    if (tempInIndex != ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rdOutIndex)
    {
        if (USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_MR & US_MR_MODE9_Msk)
        {
            ((uint16_t*)&${FLEXCOM_INSTANCE_NAME}_USART_ReadBuffer)[${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rdInIndex] = rdByte;
        }
        else
        {
            ${FLEXCOM_INSTANCE_NAME}_USART_ReadBuffer[${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rdInIndex] = (uint8_t)rdByte;
        }

        ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rdInIndex = tempInIndex;
        isSuccess = true;
    }
    else
    {
        /* Queue is full. Data will be lost. */
    }

    return isSuccess;
}

/* This routine is only called from ISR. Hence do not disable/enable USART interrupts. */
static void ${FLEXCOM_INSTANCE_NAME}_USART_ReadNotificationSend(void)
{
    uint32_t nUnreadBytesAvailable;

    if (${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.isRdNotificationEnabled == true)
    {
        nUnreadBytesAvailable = ${FLEXCOM_INSTANCE_NAME}_USART_ReadCountGet();

        if(${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rdCallback != NULL)
        {
            if (${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.isRdNotifyPersistently == true)
            {
                if (nUnreadBytesAvailable >= ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rdThreshold)
                {
                    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rdCallback(FLEXCOM_USART_EVENT_READ_THRESHOLD_REACHED, ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rdContext);
                }
            }
            else
            {
                if (nUnreadBytesAvailable == ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rdThreshold)
                {
                    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rdCallback(FLEXCOM_USART_EVENT_READ_THRESHOLD_REACHED, ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rdContext);
                }
            }
        }
    }
}

size_t ${FLEXCOM_INSTANCE_NAME}_USART_Read(uint8_t* pRdBuffer, const size_t size)
{
    size_t nBytesRead = 0;
    uint32_t rdOutIndex = ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rdOutIndex;
    uint32_t rdInIndex = ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rdInIndex;

    while (nBytesRead < size)
    {
        if (rdOutIndex != rdInIndex)
        {
            if (USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_MR & US_MR_MODE9_Msk)
            {
                ((uint16_t*)pRdBuffer)[nBytesRead++] = ((uint16_t*)&${FLEXCOM_INSTANCE_NAME}_USART_ReadBuffer)[rdOutIndex++];
            }
            else
            {
                pRdBuffer[nBytesRead++] = ${FLEXCOM_INSTANCE_NAME}_USART_ReadBuffer[rdOutIndex++];
            }


            if (rdOutIndex >= ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rdBufferSize)
            {
                rdOutIndex = 0;
            }
        }
        else
        {
            break;
        }
    }

    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rdOutIndex = rdOutIndex;

    return nBytesRead;
}

size_t ${FLEXCOM_INSTANCE_NAME}_USART_ReadCountGet(void)
{
    size_t nUnreadBytesAvailable;
    uint32_t rdOutIndex;
    uint32_t rdInIndex;

    /* Take a snapshot of indices to avoid creation of critical section */
    rdOutIndex = ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rdOutIndex;
    rdInIndex = ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rdInIndex;

    if ( rdInIndex >= rdOutIndex)
    {
        nUnreadBytesAvailable =  rdInIndex - rdOutIndex;
    }
    else
    {
        nUnreadBytesAvailable =  (${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rdBufferSize -  rdOutIndex) + rdInIndex;
    }

    return nUnreadBytesAvailable;
}

size_t ${FLEXCOM_INSTANCE_NAME}_USART_ReadFreeBufferCountGet(void)
{
    return (${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rdBufferSize - 1) - ${FLEXCOM_INSTANCE_NAME}_USART_ReadCountGet();
}

size_t ${FLEXCOM_INSTANCE_NAME}_USART_ReadBufferSizeGet(void)
{
    return (${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rdBufferSize - 1);
}

bool ${FLEXCOM_INSTANCE_NAME}_USART_ReadNotificationEnable(bool isEnabled, bool isPersistent)
{
    bool previousStatus = ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.isRdNotificationEnabled;

    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.isRdNotificationEnabled = isEnabled;

    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.isRdNotifyPersistently = isPersistent;

    return previousStatus;
}

void ${FLEXCOM_INSTANCE_NAME}_USART_ReadThresholdSet(uint32_t nBytesThreshold)
{
    if (nBytesThreshold > 0)
    {
        ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rdThreshold = nBytesThreshold;
    }
}

void ${FLEXCOM_INSTANCE_NAME}_USART_ReadCallbackRegister( FLEXCOM_USART_RING_BUFFER_CALLBACK callback, uintptr_t context)
{
    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rdCallback = callback;

    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rdContext = context;
}

void static ${FLEXCOM_INSTANCE_NAME}_USART_ISR_RX_Handler( void )
{
    uint16_t rdData = 0;

    /* Keep reading until there is a character availabe in the RX FIFO */
    while(USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_CSR & US_CSR_RXRDY_Msk)
    {
        rdData = USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_RHR & US_RHR_RXCHR_Msk;

        if (${FLEXCOM_INSTANCE_NAME}_USART_RxPushByte( rdData ) == true)
        {
            ${FLEXCOM_INSTANCE_NAME}_USART_ReadNotificationSend();
        }
        else
        {
            /* UART RX buffer is full */
        }
    }
}

void static ${FLEXCOM_INSTANCE_NAME}_USART_ISR_TX_Handler( void )
{
    uint16_t wrByte;

    /* Keep writing to the TX FIFO as long as there is space */
    while (USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_CSR & US_CSR_TXRDY_Msk)
    {
        if (${FLEXCOM_INSTANCE_NAME}_USART_TxPullByte(&wrByte) == true)
        {
            if (USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_MR & US_MR_MODE9_Msk)
            {
                USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_THR = wrByte & US_THR_TXCHR_Msk;
            }
            else
            {
                USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_THR = (uint8_t)wrByte;
            }

            /* Send notification */
            ${FLEXCOM_INSTANCE_NAME}_USART_WriteNotificationSend();
        }
        else
        {
            /* Nothing to transmit. Disable the data register empty interrupt. */
            ${FLEXCOM_INSTANCE_NAME}_USART_TX_INT_DISABLE();
            break;
        }
    }
}

void ${FLEXCOM_INSTANCE_NAME}_InterruptHandler( void )
{
    /* Channel status */
    uint32_t channelStatus = USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_CSR;

    /* Error status */
    uint32_t errorStatus = (channelStatus & (US_CSR_OVRE_Msk | US_CSR_FRAME_Msk | US_CSR_PARE_Msk));

    if(errorStatus != 0)
    {
        /* Save the error so that it can be reported when application calls the ${FLEXCOM_INSTANCE_NAME}_USART_ErrorGet() API */
        ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.errorStatus = (FLEXCOM_USART_ERROR)errorStatus;

        /* Clear the error flags and flush out the error bytes */
        ${FLEXCOM_INSTANCE_NAME}_USART_ErrorClear();

        /* USART errors are normally associated with the receiver, hence calling receiver context */
        if( ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rdCallback != NULL )
        {
            ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rdCallback(FLEXCOM_USART_EVENT_READ_ERROR, ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rdContext);
        }
    }

    /* Receiver status */
    if (channelStatus & US_CSR_RXRDY_Msk)
    {
        ${FLEXCOM_INSTANCE_NAME}_USART_ISR_RX_Handler();
    }

    /* Transmitter status */
    if ( (channelStatus & US_CSR_TXRDY_Msk) && (USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_IMR & US_IMR_TXRDY_Msk) )
    {
        ${FLEXCOM_INSTANCE_NAME}_USART_ISR_TX_Handler();
    }
}
