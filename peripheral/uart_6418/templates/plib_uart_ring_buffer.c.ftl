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

<#--Implementation-->
// *****************************************************************************
// *****************************************************************************
// Section: ${UART_INSTANCE_NAME} Implementation
// *****************************************************************************
// *****************************************************************************

UART_RING_BUFFER_OBJECT ${UART_INSTANCE_NAME?lower_case}Obj;

#define ${UART_INSTANCE_NAME}_READ_BUFFER_SIZE      ${UART_RX_RING_BUFFER_SIZE}
/* Disable Read, Overrun, Parity and Framing error interrupts */
#define ${UART_INSTANCE_NAME}_RX_INT_DISABLE()      ${UART_INSTANCE_NAME}_REGS->UART_IDR = (UART_IDR_RXRDY_Msk | UART_IDR_FRAME_Msk | UART_IDR_PARE_Msk | UART_IDR_OVRE_Msk);
/* Enable Read, Overrun, Parity and Framing error interrupts */
#define ${UART_INSTANCE_NAME}_RX_INT_ENABLE()       ${UART_INSTANCE_NAME}_REGS->UART_IER = (UART_IER_RXRDY_Msk | UART_IER_FRAME_Msk | UART_IER_PARE_Msk | UART_IER_OVRE_Msk);

static uint8_t ${UART_INSTANCE_NAME}_ReadBuffer[${UART_INSTANCE_NAME}_READ_BUFFER_SIZE];

#define ${UART_INSTANCE_NAME}_WRITE_BUFFER_SIZE     ${UART_TX_RING_BUFFER_SIZE}
#define ${UART_INSTANCE_NAME}_TX_INT_DISABLE()      ${UART_INSTANCE_NAME}_REGS->UART_IDR = UART_IDR_TXEMPTY_Msk;
#define ${UART_INSTANCE_NAME}_TX_INT_ENABLE()       ${UART_INSTANCE_NAME}_REGS->UART_IER = UART_IER_TXEMPTY_Msk;

static uint8_t ${UART_INSTANCE_NAME}_WriteBuffer[${UART_INSTANCE_NAME}_WRITE_BUFFER_SIZE];

void ${UART_INSTANCE_NAME}_Initialize( void )
{
    /* Reset ${UART_INSTANCE_NAME} */
    ${UART_INSTANCE_NAME}_REGS->UART_CR = (UART_CR_RSTRX_Msk | UART_CR_RSTTX_Msk | UART_CR_RSTSTA_Msk);

    /* Enable ${UART_INSTANCE_NAME} */
    ${UART_INSTANCE_NAME}_REGS->UART_CR = (UART_CR_TXEN_Msk | UART_CR_RXEN_Msk);

    /* Configure ${UART_INSTANCE_NAME} mode */
    <#if UART_CLK_SRC??>
    ${UART_INSTANCE_NAME}_REGS->UART_MR = ((UART_MR_BRSRCCK_${UART_CLK_SRC}) | (UART_MR_PAR_${UART_MR_PAR}) | (${UART_MR_FILTER?then(1,0)} << UART_MR_FILTER_Pos));
    <#else>
    ${UART_INSTANCE_NAME}_REGS->UART_MR = ((UART_MR_PAR_${UART_MR_PAR}) | (${UART_MR_FILTER?then(1,0)} << UART_MR_FILTER_Pos));
    </#if>

    /* Configure ${UART_INSTANCE_NAME} Baud Rate */
    ${UART_INSTANCE_NAME}_REGS->UART_BRGR = UART_BRGR_CD(${BRG_VALUE});

    /* Initialize instance object */
    ${UART_INSTANCE_NAME?lower_case}Obj.rdCallback = NULL;
    ${UART_INSTANCE_NAME?lower_case}Obj.rdInIndex = 0;
	${UART_INSTANCE_NAME?lower_case}Obj.rdOutIndex = 0;
    ${UART_INSTANCE_NAME?lower_case}Obj.isRdNotificationEnabled = false;
    ${UART_INSTANCE_NAME?lower_case}Obj.isRdNotifyPersistently = false;
    ${UART_INSTANCE_NAME?lower_case}Obj.rdThreshold = 0;
    ${UART_INSTANCE_NAME?lower_case}Obj.wrCallback = NULL;
    ${UART_INSTANCE_NAME?lower_case}Obj.wrInIndex = 0;
	${UART_INSTANCE_NAME?lower_case}Obj.wrOutIndex = 0;
    ${UART_INSTANCE_NAME?lower_case}Obj.isWrNotificationEnabled = false;
    ${UART_INSTANCE_NAME?lower_case}Obj.isWrNotifyPersistently = false;
    ${UART_INSTANCE_NAME?lower_case}Obj.wrThreshold = 0;

    /* Enable receive interrupt */
    ${UART_INSTANCE_NAME}_RX_INT_ENABLE()
}

bool ${UART_INSTANCE_NAME}_SerialSetup( UART_SERIAL_SETUP *setup, uint32_t srcClkFreq )
{
    bool status = false;
    uint32_t baud = setup->baudRate;
    uint32_t brgVal = 0;
    uint32_t uartMode;

    if (setup != NULL)
    {
        if(srcClkFreq == 0)
        {
            srcClkFreq = ${UART_INSTANCE_NAME}_FrequencyGet();
        }

        /* Calculate BRG value */
        brgVal = srcClkFreq / (16 * baud);

        /* If the target baud rate is acheivable using this clock */
        if (brgVal <= 65535)
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

static void ${UART_INSTANCE_NAME}_ErrorClear( void )
{
    uint8_t dummyData = 0u;

    ${UART_INSTANCE_NAME}_REGS->UART_CR = UART_CR_RSTSTA_Msk;

    /* Flush existing error bytes from the RX FIFO */
    while( UART_SR_RXRDY_Msk == (${UART_INSTANCE_NAME}_REGS->UART_SR & UART_SR_RXRDY_Msk) )
    {
        dummyData = (${UART_INSTANCE_NAME}_REGS->UART_RHR & UART_RHR_RXCHR_Msk);
    }

    /* Ignore the warning */
    (void)dummyData;
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

/* This routine is only called from ISR. Hence do not disable/enable USART interrupts. */
static inline bool ${UART_INSTANCE_NAME}_RxPushByte(uint8_t rdByte)
{
    uint32_t tempInIndex;
    bool isSuccess = false;

    tempInIndex = ${UART_INSTANCE_NAME?lower_case}Obj.rdInIndex + 1;

    if (tempInIndex >= ${UART_INSTANCE_NAME}_READ_BUFFER_SIZE)
    {
        tempInIndex = 0;
    }

    if (tempInIndex == ${UART_INSTANCE_NAME?lower_case}Obj.rdOutIndex)
    {
        /* Queue is full - Report it to the application. Application gets a chance to free up space by reading data out from the RX ring buffer */
        if(${UART_INSTANCE_NAME?lower_case}Obj.rdCallback != NULL)
        {
            ${UART_INSTANCE_NAME?lower_case}Obj.rdCallback(UART_EVENT_READ_BUFFER_FULL, ${UART_INSTANCE_NAME?lower_case}Obj.rdContext);
        }

        /* Read the indices again in case application has freed up space in RX ring buffer */
        tempInIndex = ${UART_INSTANCE_NAME?lower_case}Obj.rdInIndex + 1;

        if (tempInIndex >= ${UART_INSTANCE_NAME}_READ_BUFFER_SIZE)
        {
            tempInIndex = 0;
        }

    }

    if (tempInIndex != ${UART_INSTANCE_NAME?lower_case}Obj.rdOutIndex)
    {
        ${UART_INSTANCE_NAME}_ReadBuffer[${UART_INSTANCE_NAME?lower_case}Obj.rdInIndex] = rdByte;
        ${UART_INSTANCE_NAME?lower_case}Obj.rdInIndex = tempInIndex;
        isSuccess = true;
    }
    else
    {
        /* Queue is full. Data will be lost. */
    }

    return isSuccess;
}

/* This routine is only called from ISR. Hence do not disable/enable USART interrupts. */
static void ${UART_INSTANCE_NAME}_ReadNotificationSend(void)
{
    uint32_t nUnreadBytesAvailable;

    if (${UART_INSTANCE_NAME?lower_case}Obj.isRdNotificationEnabled == true)
    {
        nUnreadBytesAvailable = ${UART_INSTANCE_NAME}_ReadCountGet();

        if(${UART_INSTANCE_NAME?lower_case}Obj.rdCallback != NULL)
        {
            if (${UART_INSTANCE_NAME?lower_case}Obj.isRdNotifyPersistently == true)
            {
                if (nUnreadBytesAvailable >= ${UART_INSTANCE_NAME?lower_case}Obj.rdThreshold)
                {
                    ${UART_INSTANCE_NAME?lower_case}Obj.rdCallback(UART_EVENT_READ_THRESHOLD_REACHED, ${UART_INSTANCE_NAME?lower_case}Obj.rdContext);
                }
            }
            else
            {
                if (nUnreadBytesAvailable == ${UART_INSTANCE_NAME?lower_case}Obj.rdThreshold)
                {
                    ${UART_INSTANCE_NAME?lower_case}Obj.rdCallback(UART_EVENT_READ_THRESHOLD_REACHED, ${UART_INSTANCE_NAME?lower_case}Obj.rdContext);
                }
            }
        }
    }
}

size_t ${UART_INSTANCE_NAME}_Read(uint8_t* pRdBuffer, const size_t size)
{
    size_t nBytesRead = 0;
	uint32_t rdOutIndex;
	uint32_t rdInIndex;

    while (nBytesRead < size)
    {
        ${UART_INSTANCE_NAME}_RX_INT_DISABLE();
		
		rdOutIndex = ${UART_INSTANCE_NAME?lower_case}Obj.rdOutIndex;
		rdInIndex = ${UART_INSTANCE_NAME?lower_case}Obj.rdInIndex;

        if (rdOutIndex != rdInIndex)
        {
            pRdBuffer[nBytesRead++] = ${UART_INSTANCE_NAME}_ReadBuffer[${UART_INSTANCE_NAME?lower_case}Obj.rdOutIndex++];

            if (${UART_INSTANCE_NAME?lower_case}Obj.rdOutIndex >= ${UART_INSTANCE_NAME}_READ_BUFFER_SIZE)
            {
                ${UART_INSTANCE_NAME?lower_case}Obj.rdOutIndex = 0;
            }
            ${UART_INSTANCE_NAME}_RX_INT_ENABLE();
        }
        else
        {
            ${UART_INSTANCE_NAME}_RX_INT_ENABLE();
            break;
        }
    }

    return nBytesRead;
}

size_t ${UART_INSTANCE_NAME}_ReadCountGet(void)
{
    size_t nUnreadBytesAvailable;
	uint32_t rdInIndex;
	uint32_t rdOutIndex;

    ${UART_INSTANCE_NAME}_RX_INT_DISABLE();
	
	rdInIndex = ${UART_INSTANCE_NAME?lower_case}Obj.rdInIndex;
	rdOutIndex = ${UART_INSTANCE_NAME?lower_case}Obj.rdOutIndex;

    if ( rdInIndex >=  rdOutIndex)
    {
        nUnreadBytesAvailable =  rdInIndex - rdOutIndex;
    }
    else
    {
        nUnreadBytesAvailable =  (${UART_INSTANCE_NAME}_READ_BUFFER_SIZE -  rdOutIndex) + rdInIndex;
    }

    ${UART_INSTANCE_NAME}_RX_INT_ENABLE();

    return nUnreadBytesAvailable;
}

size_t ${UART_INSTANCE_NAME}_ReadFreeBufferCountGet(void)
{
    return (${UART_INSTANCE_NAME}_READ_BUFFER_SIZE - 1) - ${UART_INSTANCE_NAME}_ReadCountGet();
}

size_t ${UART_INSTANCE_NAME}_ReadBufferSizeGet(void)
{
    return (${UART_INSTANCE_NAME}_READ_BUFFER_SIZE - 1);
}

bool ${UART_INSTANCE_NAME}_ReadNotificationEnable(bool isEnabled, bool isPersistent)
{
    bool previousStatus = ${UART_INSTANCE_NAME?lower_case}Obj.isRdNotificationEnabled;

    ${UART_INSTANCE_NAME?lower_case}Obj.isRdNotificationEnabled = isEnabled;

    ${UART_INSTANCE_NAME?lower_case}Obj.isRdNotifyPersistently = isPersistent;

    return previousStatus;
}

void ${UART_INSTANCE_NAME}_ReadThresholdSet(uint32_t nBytesThreshold)
{
    if (nBytesThreshold > 0)
    {
        ${UART_INSTANCE_NAME?lower_case}Obj.rdThreshold = nBytesThreshold;
    }
}

void ${UART_INSTANCE_NAME}_ReadCallbackRegister( UART_RING_BUFFER_CALLBACK callback, uintptr_t context)
{
    ${UART_INSTANCE_NAME?lower_case}Obj.rdCallback = callback;

    ${UART_INSTANCE_NAME?lower_case}Obj.rdContext = context;
}

/* This routine is only called from ISR. Hence do not disable/enable USART interrupts. */
static bool ${UART_INSTANCE_NAME}_TxPullByte(uint8_t* pWrByte)
{
    bool isSuccess = false;
	uint32_t wrOutIndex = ${UART_INSTANCE_NAME?lower_case}Obj.wrOutIndex;
	uint32_t wrInIndex = ${UART_INSTANCE_NAME?lower_case}Obj.wrInIndex;

    if (wrOutIndex != wrInIndex)
    {
        *pWrByte = ${UART_INSTANCE_NAME}_WriteBuffer[${UART_INSTANCE_NAME?lower_case}Obj.wrOutIndex++];

        if (${UART_INSTANCE_NAME?lower_case}Obj.wrOutIndex >= ${UART_INSTANCE_NAME}_WRITE_BUFFER_SIZE)
        {
            ${UART_INSTANCE_NAME?lower_case}Obj.wrOutIndex = 0;
        }
        isSuccess = true;
    }

    return isSuccess;
}

static inline bool ${UART_INSTANCE_NAME}_TxPushByte(uint8_t wrByte)
{
    uint32_t tempInIndex;
    bool isSuccess = false;

    tempInIndex = ${UART_INSTANCE_NAME?lower_case}Obj.wrInIndex + 1;

    if (tempInIndex >= ${UART_INSTANCE_NAME}_WRITE_BUFFER_SIZE)
    {
        tempInIndex = 0;
    }
    if (tempInIndex != ${UART_INSTANCE_NAME?lower_case}Obj.wrOutIndex)
    {
        ${UART_INSTANCE_NAME}_WriteBuffer[${UART_INSTANCE_NAME?lower_case}Obj.wrInIndex] = wrByte;
        ${UART_INSTANCE_NAME?lower_case}Obj.wrInIndex = tempInIndex;
        isSuccess = true;
    }
    else
    {
        /* Queue is full. Report Error. */
    }

    return isSuccess;
}

/* This routine is only called from ISR. Hence do not disable/enable USART interrupts. */
static void ${UART_INSTANCE_NAME}_WriteNotificationSend(void)
{
    uint32_t nFreeWrBufferCount;

    if (${UART_INSTANCE_NAME?lower_case}Obj.isWrNotificationEnabled == true)
    {
        nFreeWrBufferCount = ${UART_INSTANCE_NAME}_WriteFreeBufferCountGet();

        if(${UART_INSTANCE_NAME?lower_case}Obj.wrCallback != NULL)
        {
            if (${UART_INSTANCE_NAME?lower_case}Obj.isWrNotifyPersistently == true)
            {
                if (nFreeWrBufferCount >= ${UART_INSTANCE_NAME?lower_case}Obj.wrThreshold)
                {
                    ${UART_INSTANCE_NAME?lower_case}Obj.wrCallback(UART_EVENT_WRITE_THRESHOLD_REACHED, ${UART_INSTANCE_NAME?lower_case}Obj.wrContext);
                }
            }
            else
            {
                if (nFreeWrBufferCount == ${UART_INSTANCE_NAME?lower_case}Obj.wrThreshold)
                {
                    ${UART_INSTANCE_NAME?lower_case}Obj.wrCallback(UART_EVENT_WRITE_THRESHOLD_REACHED, ${UART_INSTANCE_NAME?lower_case}Obj.wrContext);
                }
            }
        }
    }
}

static size_t ${UART_INSTANCE_NAME}_WritePendingBytesGet(void)
{
    size_t nPendingTxBytes;
	uint32_t wrOutIndex = ${UART_INSTANCE_NAME?lower_case}Obj.wrOutIndex;
	uint32_t wrInIndex = ${UART_INSTANCE_NAME?lower_case}Obj.wrInIndex;

    if ( wrInIndex >=  wrOutIndex)
    {
        nPendingTxBytes =  wrInIndex -  wrOutIndex;
    }
    else
    {
        nPendingTxBytes =  (${UART_INSTANCE_NAME}_WRITE_BUFFER_SIZE -  wrOutIndex) + wrInIndex;
    }

    return nPendingTxBytes;
}

size_t ${UART_INSTANCE_NAME}_WriteCountGet(void)
{
    size_t nPendingTxBytes;

    ${UART_INSTANCE_NAME}_TX_INT_DISABLE();

    nPendingTxBytes = ${UART_INSTANCE_NAME}_WritePendingBytesGet();

    /* Enable transmit interrupt only if any data is pending for transmission */
    if (nPendingTxBytes > 0)
    {
        ${UART_INSTANCE_NAME}_TX_INT_ENABLE();
    }

    return nPendingTxBytes;
}

size_t ${UART_INSTANCE_NAME}_Write(uint8_t* pWrBuffer, const size_t size )
{
    size_t nBytesWritten  = 0;

    ${UART_INSTANCE_NAME}_TX_INT_DISABLE();

    while (nBytesWritten < size)
    {
        if (${UART_INSTANCE_NAME}_TxPushByte(pWrBuffer[nBytesWritten]) == true)
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
    if (${UART_INSTANCE_NAME}_WritePendingBytesGet() > 0)
    {
        /* Enable TX interrupt as data is pending for transmission */
        ${UART_INSTANCE_NAME}_TX_INT_ENABLE();
    }

    return nBytesWritten;
}

size_t ${UART_INSTANCE_NAME}_WriteFreeBufferCountGet(void)
{
    return (${UART_INSTANCE_NAME}_WRITE_BUFFER_SIZE - 1) - ${UART_INSTANCE_NAME}_WriteCountGet();
}

size_t ${UART_INSTANCE_NAME}_WriteBufferSizeGet(void)
{
    return (${UART_INSTANCE_NAME}_WRITE_BUFFER_SIZE - 1);
}

bool ${UART_INSTANCE_NAME}_WriteNotificationEnable(bool isEnabled, bool isPersistent)
{
    bool previousStatus = ${UART_INSTANCE_NAME?lower_case}Obj.isWrNotificationEnabled;

    ${UART_INSTANCE_NAME?lower_case}Obj.isWrNotificationEnabled = isEnabled;

    ${UART_INSTANCE_NAME?lower_case}Obj.isWrNotifyPersistently = isPersistent;

    return previousStatus;
}

void ${UART_INSTANCE_NAME}_WriteThresholdSet(uint32_t nBytesThreshold)
{
    if (nBytesThreshold > 0)
    {
        ${UART_INSTANCE_NAME?lower_case}Obj.wrThreshold = nBytesThreshold;
    }
}

void ${UART_INSTANCE_NAME}_WriteCallbackRegister( UART_RING_BUFFER_CALLBACK callback, uintptr_t context)
{
    ${UART_INSTANCE_NAME?lower_case}Obj.wrCallback = callback;

    ${UART_INSTANCE_NAME?lower_case}Obj.wrContext = context;
}

static void ${UART_INSTANCE_NAME}_ISR_RX_Handler( void )
{
    /* Keep reading until there is a character availabe in the RX FIFO */
    while(UART_SR_RXRDY_Msk == (${UART_INSTANCE_NAME}_REGS->UART_SR& UART_SR_RXRDY_Msk))
    {
        if (${UART_INSTANCE_NAME}_RxPushByte( (uint8_t )(${UART_INSTANCE_NAME}_REGS->UART_RHR& UART_RHR_RXCHR_Msk) ) == true)
        {
            ${UART_INSTANCE_NAME}_ReadNotificationSend();
        }
        else
        {
            /* UART RX buffer is full */
        }
    }
}

static void ${UART_INSTANCE_NAME}_ISR_TX_Handler( void )
{
    uint8_t wrByte;

    /* Keep writing to the TX FIFO as long as there is space */
    while(UART_SR_TXRDY_Msk == (${UART_INSTANCE_NAME}_REGS->UART_SR & UART_SR_TXRDY_Msk))
    {
        if (${UART_INSTANCE_NAME}_TxPullByte(&wrByte) == true)
        {
            ${UART_INSTANCE_NAME}_REGS->UART_THR |= wrByte;

            /* Send notification */
            ${UART_INSTANCE_NAME}_WriteNotificationSend();
        }
        else
        {
            /* Nothing to transmit. Disable the data register empty interrupt. */
            ${UART_INSTANCE_NAME}_TX_INT_DISABLE();
            break;
        }
    }
}

void ${UART_INSTANCE_NAME}_InterruptHandler( void )
{
    /* Error status */
    uint32_t errorStatus = (${UART_INSTANCE_NAME}_REGS->UART_SR & (UART_SR_OVRE_Msk | UART_SR_FRAME_Msk | UART_SR_PARE_Msk));

    if(errorStatus != 0)
    {
        /* Client must call UARTx_ErrorGet() function to clear the errors */

        /* Disable Read, Overrun, Parity and Framing error interrupts */

        ${UART_INSTANCE_NAME}_REGS->UART_IDR = (UART_IDR_RXRDY_Msk | UART_IDR_FRAME_Msk | UART_IDR_PARE_Msk | UART_IDR_OVRE_Msk);

        /* UART errors are normally associated with the receiver, hence calling
         * receiver callback */
        if( ${UART_INSTANCE_NAME?lower_case}Obj.rdCallback != NULL )
        {
            ${UART_INSTANCE_NAME?lower_case}Obj.rdCallback(UART_EVENT_READ_ERROR, ${UART_INSTANCE_NAME?lower_case}Obj.rdContext);
        }
    }

    /* Receiver status */
    if(UART_SR_RXRDY_Msk == (${UART_INSTANCE_NAME}_REGS->UART_SR & UART_SR_RXRDY_Msk))
    {
        ${UART_INSTANCE_NAME}_ISR_RX_Handler();
    }

    /* Transmitter status */
    if(UART_SR_TXRDY_Msk == (${UART_INSTANCE_NAME}_REGS->UART_SR & UART_SR_TXRDY_Msk))
    {
        ${UART_INSTANCE_NAME}_ISR_TX_Handler();
    }

}