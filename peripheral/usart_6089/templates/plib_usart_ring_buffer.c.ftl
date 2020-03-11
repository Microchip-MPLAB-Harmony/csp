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

USART_RING_BUFFER_OBJECT ${USART_INSTANCE_NAME?lower_case}Obj;

#define ${USART_INSTANCE_NAME}_READ_BUFFER_SIZE      ${USART_RX_RING_BUFFER_SIZE}
/* Disable Read, Overrun, Parity and Framing error interrupts */
#define ${USART_INSTANCE_NAME}_RX_INT_DISABLE()      ${USART_INSTANCE_NAME}_REGS->US_IDR = (US_IDR_USART_RXRDY_Msk | US_IDR_USART_FRAME_Msk | US_IDR_USART_PARE_Msk | US_IDR_USART_OVRE_Msk);
/* Enable Read, Overrun, Parity and Framing error interrupts */
#define ${USART_INSTANCE_NAME}_RX_INT_ENABLE()       ${USART_INSTANCE_NAME}_REGS->US_IER = (US_IER_USART_RXRDY_Msk | US_IER_USART_FRAME_Msk | US_IER_USART_PARE_Msk | US_IER_USART_OVRE_Msk);

static uint8_t ${USART_INSTANCE_NAME}_ReadBuffer[${USART_INSTANCE_NAME}_READ_BUFFER_SIZE];

#define ${USART_INSTANCE_NAME}_WRITE_BUFFER_SIZE     ${USART_TX_RING_BUFFER_SIZE}
#define ${USART_INSTANCE_NAME}_TX_INT_DISABLE()      ${USART_INSTANCE_NAME}_REGS->US_IDR = US_IDR_USART_TXEMPTY_Msk;
#define ${USART_INSTANCE_NAME}_TX_INT_ENABLE()       ${USART_INSTANCE_NAME}_REGS->US_IER = US_IER_USART_TXEMPTY_Msk;

static uint8_t ${USART_INSTANCE_NAME}_WriteBuffer[${USART_INSTANCE_NAME}_WRITE_BUFFER_SIZE];

void ${USART_INSTANCE_NAME}_Initialize( void )
{
    /* Reset ${USART_INSTANCE_NAME} */
    ${USART_INSTANCE_NAME}_REGS->US_CR = (US_CR_USART_RSTRX_Msk | US_CR_USART_RSTTX_Msk | US_CR_USART_RSTSTA_Msk);

    /* Enable ${USART_INSTANCE_NAME} */
    ${USART_INSTANCE_NAME}_REGS->US_CR = (US_CR_USART_TXEN_Msk | US_CR_USART_RXEN_Msk);

    /* Configure ${USART_INSTANCE_NAME} mode */
    <#if USART_MR_MODE9 == true>
    ${USART_INSTANCE_NAME}_REGS->US_MR = (US_MR_USART_USCLKS_${USART_CLK_SRC} | US_MR_USART_MODE9_Msk | US_MR_USART_PAR_${USART_MR_PAR} | US_MR_USART_NBSTOP_${USART_MR_NBSTOP} | (${USART_MR_OVER?string} << US_MR_USART_OVER_Pos));
    <#else>
    ${USART_INSTANCE_NAME}_REGS->US_MR = (US_MR_USART_USCLKS_${USART_CLK_SRC} | US_MR_USART_CHRL_${USART_MR_CHRL} | US_MR_USART_PAR_${USART_MR_PAR} | US_MR_USART_NBSTOP_${USART_MR_NBSTOP} | (${USART_MR_OVER?string} << US_MR_USART_OVER_Pos));
    </#if>

    /* Configure ${USART_INSTANCE_NAME} Baud Rate */
    ${USART_INSTANCE_NAME}_REGS->US_BRGR = US_BRGR_CD(${BRG_VALUE});

    /* Initialize instance object */
    ${USART_INSTANCE_NAME?lower_case}Obj.rdCallback = NULL;
    ${USART_INSTANCE_NAME?lower_case}Obj.rdInIndex = ${USART_INSTANCE_NAME?lower_case}Obj.rdOutIndex = 0;
    ${USART_INSTANCE_NAME?lower_case}Obj.isRdNotificationEnabled = false;
    ${USART_INSTANCE_NAME?lower_case}Obj.isRdNotifyPersistently = false;
    ${USART_INSTANCE_NAME?lower_case}Obj.rdThreshold = 0;
    ${USART_INSTANCE_NAME?lower_case}Obj.wrCallback = NULL;
    ${USART_INSTANCE_NAME?lower_case}Obj.wrInIndex = ${USART_INSTANCE_NAME?lower_case}Obj.wrOutIndex = 0;
    ${USART_INSTANCE_NAME?lower_case}Obj.isWrNotificationEnabled = false;
    ${USART_INSTANCE_NAME?lower_case}Obj.isWrNotifyPersistently = false;
    ${USART_INSTANCE_NAME?lower_case}Obj.wrThreshold = 0;

    /* Enable Read, Overrun, Parity and Framing error interrupts */
    ${USART_INSTANCE_NAME}_RX_INT_ENABLE();
}

bool ${USART_INSTANCE_NAME}_SerialSetup( USART_SERIAL_SETUP *setup, uint32_t srcClkFreq )
{
    uint32_t baud = setup->baudRate;
    uint32_t brgVal = 0;
    uint32_t overSampVal = 0;
    uint32_t usartMode;
    bool status = false;

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
        else if (srcClkFreq >= (8 * baud))
        {
            brgVal = (srcClkFreq / (8 * baud));
            overSampVal = US_MR_USART_OVER(1);
        }
        else
        {
            return false;
        }

        if (brgVal > 65535)
        {
            /* The requested baud is so low that the ratio of srcClkFreq to baud exceeds the 16-bit register value of CD register */
            return false;
        }

        /* Configure ${USART_INSTANCE_NAME} mode */
        usartMode = ${USART_INSTANCE_NAME}_REGS->US_MR;
        usartMode &= ~(US_MR_USART_CHRL_Msk | US_MR_USART_MODE9_Msk | US_MR_USART_PAR_Msk | US_MR_USART_NBSTOP_Msk | US_MR_USART_OVER_Msk);
        ${USART_INSTANCE_NAME}_REGS->US_MR = usartMode | ((uint32_t)setup->dataWidth | (uint32_t)setup->parity | (uint32_t)setup->stopBits | (uint32_t)overSampVal);

        /* Configure ${USART_INSTANCE_NAME} Baud Rate */
        ${USART_INSTANCE_NAME}_REGS->US_BRGR = US_BRGR_CD(brgVal);
        status = true;
    }

    return status;
}

static void ${USART_INSTANCE_NAME}_ErrorClear( void )
{
    uint8_t dummyData = 0u;

    ${USART_INSTANCE_NAME}_REGS->US_CR = US_CR_USART_RSTSTA_Msk;

    /* Flush existing error bytes from the RX FIFO */
    while( US_CSR_USART_RXRDY_Msk == (${USART_INSTANCE_NAME}_REGS->US_CSR & US_CSR_USART_RXRDY_Msk) )
    {
        dummyData = (${USART_INSTANCE_NAME}_REGS->US_RHR & US_RHR_RXCHR_Msk);
    }

    /* Ignore the warning */
    (void)dummyData;
}

USART_ERROR ${USART_INSTANCE_NAME}_ErrorGet( void )
{
    USART_ERROR errors = USART_ERROR_NONE;
    uint32_t status = ${USART_INSTANCE_NAME}_REGS->US_CSR;

    errors = (USART_ERROR)(status & (US_CSR_USART_OVRE_Msk | US_CSR_USART_PARE_Msk | US_CSR_USART_FRAME_Msk));

    if(errors != USART_ERROR_NONE)
    {
        ${USART_INSTANCE_NAME}_ErrorClear();
    }

    /* All errors are cleared, but send the previous error state */
    return errors;
}

/* This routine is only called from ISR. Hence do not disable/enable USART interrupts. */
static inline bool ${USART_INSTANCE_NAME}_RxPushByte(uint8_t rdByte)
{
    uint32_t tempInIndex;
    bool isSuccess = false;

    tempInIndex = ${USART_INSTANCE_NAME?lower_case}Obj.rdInIndex + 1;

    if (tempInIndex >= ${USART_INSTANCE_NAME}_READ_BUFFER_SIZE)
    {
        tempInIndex = 0;
    }

    if (tempInIndex == ${USART_INSTANCE_NAME?lower_case}Obj.rdOutIndex)
    {
        /* Queue is full - Report it to the application. Application gets a chance to free up space by reading data out from the RX ring buffer */
        if(${USART_INSTANCE_NAME?lower_case}Obj.rdCallback != NULL)
        {
            ${USART_INSTANCE_NAME?lower_case}Obj.rdCallback(USART_EVENT_READ_BUFFER_FULL, ${USART_INSTANCE_NAME?lower_case}Obj.rdContext);

            /* Read the indices again in case application has freed up space in RX ring buffer */
            tempInIndex = ${USART_INSTANCE_NAME?lower_case}Obj.rdInIndex + 1;

            if (tempInIndex >= ${USART_INSTANCE_NAME}_READ_BUFFER_SIZE)
            {
                tempInIndex = 0;
            }
        }
    }

    if (tempInIndex != ${USART_INSTANCE_NAME?lower_case}Obj.rdOutIndex)
    {
        ${USART_INSTANCE_NAME}_ReadBuffer[${USART_INSTANCE_NAME?lower_case}Obj.rdInIndex] = rdByte;
        ${USART_INSTANCE_NAME?lower_case}Obj.rdInIndex = tempInIndex;
        isSuccess = true;
    }
    else
    {
        /* Queue is full. Data will be lost. */
    }

    return isSuccess;
}

/* This routine is only called from ISR. Hence do not disable/enable USART interrupts. */
static void ${USART_INSTANCE_NAME}_ReadNotificationSend(void)
{
    uint32_t nUnreadBytesAvailable;

    if (${USART_INSTANCE_NAME?lower_case}Obj.isRdNotificationEnabled == true)
    {
        nUnreadBytesAvailable = ${USART_INSTANCE_NAME}_ReadCountGet();

        if(${USART_INSTANCE_NAME?lower_case}Obj.rdCallback != NULL)
        {
            if (${USART_INSTANCE_NAME?lower_case}Obj.isRdNotifyPersistently == true)
            {
                if (nUnreadBytesAvailable >= ${USART_INSTANCE_NAME?lower_case}Obj.rdThreshold)
                {
                    ${USART_INSTANCE_NAME?lower_case}Obj.rdCallback(USART_EVENT_READ_THRESHOLD_REACHED, ${USART_INSTANCE_NAME?lower_case}Obj.rdContext);
                }
            }
            else
            {
                if (nUnreadBytesAvailable == ${USART_INSTANCE_NAME?lower_case}Obj.rdThreshold)
                {
                    ${USART_INSTANCE_NAME?lower_case}Obj.rdCallback(USART_EVENT_READ_THRESHOLD_REACHED, ${USART_INSTANCE_NAME?lower_case}Obj.rdContext);
                }
            }
        }
    }
}

size_t ${USART_INSTANCE_NAME}_Read(uint8_t* pRdBuffer, const size_t size)
{
    size_t nBytesRead = 0;

    while (nBytesRead < size)
    {
        ${USART_INSTANCE_NAME}_RX_INT_DISABLE();

        if (${USART_INSTANCE_NAME?lower_case}Obj.rdOutIndex != ${USART_INSTANCE_NAME?lower_case}Obj.rdInIndex)
        {
            pRdBuffer[nBytesRead++] = ${USART_INSTANCE_NAME}_ReadBuffer[${USART_INSTANCE_NAME?lower_case}Obj.rdOutIndex++];

            if (${USART_INSTANCE_NAME?lower_case}Obj.rdOutIndex >= ${USART_INSTANCE_NAME}_READ_BUFFER_SIZE)
            {
                ${USART_INSTANCE_NAME?lower_case}Obj.rdOutIndex = 0;
            }
            ${USART_INSTANCE_NAME}_RX_INT_ENABLE();
        }
        else
        {
            ${USART_INSTANCE_NAME}_RX_INT_ENABLE();
            break;
        }
    }

    return nBytesRead;
}

size_t ${USART_INSTANCE_NAME}_ReadCountGet(void)
{
    size_t nUnreadBytesAvailable;

    ${USART_INSTANCE_NAME}_RX_INT_DISABLE();

    if ( ${USART_INSTANCE_NAME?lower_case}Obj.rdInIndex >=  ${USART_INSTANCE_NAME?lower_case}Obj.rdOutIndex)
    {
        nUnreadBytesAvailable =  ${USART_INSTANCE_NAME?lower_case}Obj.rdInIndex -  ${USART_INSTANCE_NAME?lower_case}Obj.rdOutIndex;
    }
    else
    {
        nUnreadBytesAvailable =  (${USART_INSTANCE_NAME}_READ_BUFFER_SIZE -  ${USART_INSTANCE_NAME?lower_case}Obj.rdOutIndex) + ${USART_INSTANCE_NAME?lower_case}Obj.rdInIndex;
    }

    ${USART_INSTANCE_NAME}_RX_INT_ENABLE();

    return nUnreadBytesAvailable;
}

size_t ${USART_INSTANCE_NAME}_ReadFreeBufferCountGet(void)
{
    return (${USART_INSTANCE_NAME}_READ_BUFFER_SIZE - 1) - ${USART_INSTANCE_NAME}_ReadCountGet();
}

size_t ${USART_INSTANCE_NAME}_ReadBufferSizeGet(void)
{
    return (${USART_INSTANCE_NAME}_READ_BUFFER_SIZE - 1);
}

bool ${USART_INSTANCE_NAME}_ReadNotificationEnable(bool isEnabled, bool isPersistent)
{
    bool previousStatus = ${USART_INSTANCE_NAME?lower_case}Obj.isRdNotificationEnabled;

    ${USART_INSTANCE_NAME?lower_case}Obj.isRdNotificationEnabled = isEnabled;

    ${USART_INSTANCE_NAME?lower_case}Obj.isRdNotifyPersistently = isPersistent;

    return previousStatus;
}

void ${USART_INSTANCE_NAME}_ReadThresholdSet(uint32_t nBytesThreshold)
{
    if (nBytesThreshold > 0)
    {
        ${USART_INSTANCE_NAME?lower_case}Obj.rdThreshold = nBytesThreshold;
    }
}

void ${USART_INSTANCE_NAME}_ReadCallbackRegister( USART_RING_BUFFER_CALLBACK callback, uintptr_t context)
{
    ${USART_INSTANCE_NAME?lower_case}Obj.rdCallback = callback;

    ${USART_INSTANCE_NAME?lower_case}Obj.rdContext = context;
}

/* This routine is only called from ISR. Hence do not disable/enable USART interrupts. */
static bool ${USART_INSTANCE_NAME}_TxPullByte(uint8_t* pWrByte)
{
    bool isSuccess = false;

    if (${USART_INSTANCE_NAME?lower_case}Obj.wrOutIndex != ${USART_INSTANCE_NAME?lower_case}Obj.wrInIndex)
    {
        *pWrByte = ${USART_INSTANCE_NAME}_WriteBuffer[${USART_INSTANCE_NAME?lower_case}Obj.wrOutIndex++];

        if (${USART_INSTANCE_NAME?lower_case}Obj.wrOutIndex >= ${USART_INSTANCE_NAME}_WRITE_BUFFER_SIZE)
        {
            ${USART_INSTANCE_NAME?lower_case}Obj.wrOutIndex = 0;
        }
        isSuccess = true;
    }

    return isSuccess;
}

static inline bool ${USART_INSTANCE_NAME}_TxPushByte(uint8_t wrByte)
{
    uint32_t tempInIndex;
    bool isSuccess = false;

    tempInIndex = ${USART_INSTANCE_NAME?lower_case}Obj.wrInIndex + 1;

    if (tempInIndex >= ${USART_INSTANCE_NAME}_WRITE_BUFFER_SIZE)
    {
        tempInIndex = 0;
    }
    if (tempInIndex != ${USART_INSTANCE_NAME?lower_case}Obj.wrOutIndex)
    {
        ${USART_INSTANCE_NAME}_WriteBuffer[${USART_INSTANCE_NAME?lower_case}Obj.wrInIndex] = wrByte;
        ${USART_INSTANCE_NAME?lower_case}Obj.wrInIndex = tempInIndex;
        isSuccess = true;
    }
    else
    {
        /* Queue is full. Report Error. */
    }

    return isSuccess;
}

/* This routine is only called from ISR. Hence do not disable/enable USART interrupts. */
static void ${USART_INSTANCE_NAME}_WriteNotificationSend(void)
{
    uint32_t nFreeWrBufferCount;

    if (${USART_INSTANCE_NAME?lower_case}Obj.isWrNotificationEnabled == true)
    {
        nFreeWrBufferCount = ${USART_INSTANCE_NAME}_WriteFreeBufferCountGet();

        if(${USART_INSTANCE_NAME?lower_case}Obj.wrCallback != NULL)
        {
            if (${USART_INSTANCE_NAME?lower_case}Obj.isWrNotifyPersistently == true)
            {
                if (nFreeWrBufferCount >= ${USART_INSTANCE_NAME?lower_case}Obj.wrThreshold)
                {
                    ${USART_INSTANCE_NAME?lower_case}Obj.wrCallback(USART_EVENT_WRITE_THRESHOLD_REACHED, ${USART_INSTANCE_NAME?lower_case}Obj.wrContext);
                }
            }
            else
            {
                if (nFreeWrBufferCount == ${USART_INSTANCE_NAME?lower_case}Obj.wrThreshold)
                {
                    ${USART_INSTANCE_NAME?lower_case}Obj.wrCallback(USART_EVENT_WRITE_THRESHOLD_REACHED, ${USART_INSTANCE_NAME?lower_case}Obj.wrContext);
                }
            }
        }
    }
}

static size_t ${USART_INSTANCE_NAME}_WritePendingBytesGet(void)
{
    size_t nPendingTxBytes;

    if ( ${USART_INSTANCE_NAME?lower_case}Obj.wrInIndex >=  ${USART_INSTANCE_NAME?lower_case}Obj.wrOutIndex)
    {
        nPendingTxBytes =  ${USART_INSTANCE_NAME?lower_case}Obj.wrInIndex -  ${USART_INSTANCE_NAME?lower_case}Obj.wrOutIndex;
    }
    else
    {
        nPendingTxBytes =  (${USART_INSTANCE_NAME}_WRITE_BUFFER_SIZE -  ${USART_INSTANCE_NAME?lower_case}Obj.wrOutIndex) + ${USART_INSTANCE_NAME?lower_case}Obj.wrInIndex;
    }

    return nPendingTxBytes;
}

size_t ${USART_INSTANCE_NAME}_WriteCountGet(void)
{
    size_t nPendingTxBytes;

    ${USART_INSTANCE_NAME}_TX_INT_DISABLE();

    nPendingTxBytes = ${USART_INSTANCE_NAME}_WritePendingBytesGet();

    /* Enable transmit interrupt only if any data is pending for transmission */
    if (${USART_INSTANCE_NAME}_WritePendingBytesGet() > 0)
    {
        ${USART_INSTANCE_NAME}_TX_INT_ENABLE();
    }

    return nPendingTxBytes;
}

size_t ${USART_INSTANCE_NAME}_Write(uint8_t* pWrBuffer, const size_t size )
{
    size_t nBytesWritten  = 0;

    ${USART_INSTANCE_NAME}_TX_INT_DISABLE();

    while (nBytesWritten < size)
    {
        if (${USART_INSTANCE_NAME}_TxPushByte(pWrBuffer[nBytesWritten]) == true)
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
    if (${USART_INSTANCE_NAME}_WritePendingBytesGet() > 0)
    {
        /* Enable TX interrupt as data is pending for transmission */
        ${USART_INSTANCE_NAME}_TX_INT_ENABLE();
    }

    return nBytesWritten;
}

size_t ${USART_INSTANCE_NAME}_WriteFreeBufferCountGet(void)
{
    return (${USART_INSTANCE_NAME}_WRITE_BUFFER_SIZE - 1) - ${USART_INSTANCE_NAME}_WriteCountGet();
}

size_t ${USART_INSTANCE_NAME}_WriteBufferSizeGet(void)
{
    return (${USART_INSTANCE_NAME}_WRITE_BUFFER_SIZE - 1);
}

bool ${USART_INSTANCE_NAME}_WriteNotificationEnable(bool isEnabled, bool isPersistent)
{
    bool previousStatus = ${USART_INSTANCE_NAME?lower_case}Obj.isWrNotificationEnabled;

    ${USART_INSTANCE_NAME?lower_case}Obj.isWrNotificationEnabled = isEnabled;

    ${USART_INSTANCE_NAME?lower_case}Obj.isWrNotifyPersistently = isPersistent;

    return previousStatus;
}

void ${USART_INSTANCE_NAME}_WriteThresholdSet(uint32_t nBytesThreshold)
{
    if (nBytesThreshold > 0)
    {
        ${USART_INSTANCE_NAME?lower_case}Obj.wrThreshold = nBytesThreshold;
    }
}

void ${USART_INSTANCE_NAME}_WriteCallbackRegister( USART_RING_BUFFER_CALLBACK callback, uintptr_t context)
{
    ${USART_INSTANCE_NAME?lower_case}Obj.wrCallback = callback;

    ${USART_INSTANCE_NAME?lower_case}Obj.wrContext = context;
}

static void ${USART_INSTANCE_NAME}_ISR_RX_Handler( void )
{
    /* Keep reading until there is a character availabe in the RX FIFO */
    while(US_CSR_USART_RXRDY_Msk == (${USART_INSTANCE_NAME}_REGS->US_CSR& US_CSR_USART_RXRDY_Msk))
    {
        if (${USART_INSTANCE_NAME}_RxPushByte( (uint8_t )(${USART_INSTANCE_NAME}_REGS->US_RHR& US_RHR_RXCHR_Msk) ) == true)
        {
            ${USART_INSTANCE_NAME}_ReadNotificationSend();
        }
        else
        {
            /* UART RX buffer is full */
        }
    }
}

static void ${USART_INSTANCE_NAME}_ISR_TX_Handler( void )
{
    uint8_t wrByte;

    /* Keep writing to the TX FIFO as long as there is space */
    while(US_CSR_USART_TXEMPTY_Msk == (${USART_INSTANCE_NAME}_REGS->US_CSR& US_CSR_USART_TXEMPTY_Msk))
    {
        if (${USART_INSTANCE_NAME}_TxPullByte(&wrByte) == true)
        {
            ${USART_INSTANCE_NAME}_REGS->US_THR |= wrByte;

            /* Send notification */
            ${USART_INSTANCE_NAME}_WriteNotificationSend();
        }
        else
        {
            /* Nothing to transmit. Disable the data register empty interrupt. */
            ${USART_INSTANCE_NAME}_TX_INT_DISABLE();
            break;
        }
    }
}

void ${USART_INSTANCE_NAME}_InterruptHandler( void )
{
    /* Error status */
    uint32_t errorStatus = (${USART_INSTANCE_NAME}_REGS->US_CSR & (US_CSR_USART_OVRE_Msk | US_CSR_USART_FRAME_Msk | US_CSR_USART_PARE_Msk));

    if(errorStatus != 0)
    {
        /* Client must call USARTx_ErrorGet() function to clear the errors */

        /* Disable Read, Overrun, Parity and Framing error interrupts */
        ${USART_INSTANCE_NAME}_REGS->US_IDR = (US_IDR_USART_RXRDY_Msk | US_IDR_USART_FRAME_Msk | US_IDR_USART_PARE_Msk | US_IDR_USART_OVRE_Msk);

        /* USART errors are normally associated with the receiver, hence calling receiver callback */
        if( ${USART_INSTANCE_NAME?lower_case}Obj.rdCallback != NULL )
        {
            ${USART_INSTANCE_NAME?lower_case}Obj.rdCallback(USART_EVENT_READ_ERROR, ${USART_INSTANCE_NAME?lower_case}Obj.rdContext);
        }
    }

    /* Receiver status */
    if(US_CSR_USART_RXRDY_Msk == (${USART_INSTANCE_NAME}_REGS->US_CSR & US_CSR_USART_RXRDY_Msk))
    {
        ${USART_INSTANCE_NAME}_ISR_RX_Handler();
    }

    /* Transmitter status */
    if(US_CSR_USART_TXRDY_Msk == (${USART_INSTANCE_NAME}_REGS->US_CSR & US_CSR_USART_TXRDY_Msk))
    {
        ${USART_INSTANCE_NAME}_ISR_TX_Handler();
    }
}