/*******************************************************************************
  ${DBGU_INSTANCE_NAME} PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${DBGU_INSTANCE_NAME?lower_case}.c

  Summary:
    ${DBGU_INSTANCE_NAME} PLIB Implementation File

  Description:
    None

*******************************************************************************/

/*******************************************************************************
* Copyright (C) 2020 Microchip Technology Inc. and its subsidiaries.
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
#include "plib_${DBGU_INSTANCE_NAME?lower_case}.h"

<#--Implementation-->
// *****************************************************************************
// *****************************************************************************
// Section: ${DBGU_INSTANCE_NAME} Implementation
// *****************************************************************************
// *****************************************************************************

DBGU_RING_BUFFER_OBJECT ${DBGU_INSTANCE_NAME?lower_case}Obj;

#define ${DBGU_INSTANCE_NAME}_READ_BUFFER_SIZE      ${DBGU_RX_RING_BUFFER_SIZE}
/* Disable Read, Overrun, Parity and Framing error interrupts */
#define ${DBGU_INSTANCE_NAME}_RX_INT_DISABLE()      ${DBGU_INSTANCE_NAME}_REGS->DBGU_IDR = (DBGU_IDR_RXRDY_Msk | DBGU_IDR_FRAME_Msk | DBGU_IDR_PARE_Msk | DBGU_IDR_OVRE_Msk);
/* Enable Read, Overrun, Parity and Framing error interrupts */
#define ${DBGU_INSTANCE_NAME}_RX_INT_ENABLE()       ${DBGU_INSTANCE_NAME}_REGS->DBGU_IER = (DBGU_IER_RXRDY_Msk | DBGU_IER_FRAME_Msk | DBGU_IER_PARE_Msk | DBGU_IER_OVRE_Msk);

static uint8_t ${DBGU_INSTANCE_NAME}_ReadBuffer[${DBGU_INSTANCE_NAME}_READ_BUFFER_SIZE];

#define ${DBGU_INSTANCE_NAME}_WRITE_BUFFER_SIZE     ${DBGU_TX_RING_BUFFER_SIZE}
#define ${DBGU_INSTANCE_NAME}_TX_INT_DISABLE()      ${DBGU_INSTANCE_NAME}_REGS->DBGU_IDR = DBGU_IDR_TXRDY_Msk;
#define ${DBGU_INSTANCE_NAME}_TX_INT_ENABLE()       ${DBGU_INSTANCE_NAME}_REGS->DBGU_IER = DBGU_IER_TXRDY_Msk;

static uint8_t ${DBGU_INSTANCE_NAME}_WriteBuffer[${DBGU_INSTANCE_NAME}_WRITE_BUFFER_SIZE];

void ${DBGU_INSTANCE_NAME}_Initialize( void )
{
    /* Reset ${DBGU_INSTANCE_NAME} */
    ${DBGU_INSTANCE_NAME}_REGS->DBGU_CR = (DBGU_CR_RSTRX_Msk | DBGU_CR_RSTTX_Msk | DBGU_CR_RSTSTA_Msk);

    /* Enable ${DBGU_INSTANCE_NAME} */
    ${DBGU_INSTANCE_NAME}_REGS->DBGU_CR = (DBGU_CR_TXEN_Msk | DBGU_CR_RXEN_Msk);

    /* Configure ${DBGU_INSTANCE_NAME} mode */
    <#if DBGU_CLK_SRC??>
    ${DBGU_INSTANCE_NAME}_REGS->DBGU_MR = (DBGU_MR_BRSRCCK(${DBGU_CLK_SRC}) | (DBGU_MR_PAR_${DBGU_MR_PAR}) | (${DBGU_MR_FILTER?then(1,0)} << DBGU_MR_FILTER_Pos));
    <#else>
    ${DBGU_INSTANCE_NAME}_REGS->DBGU_MR = ((DBGU_MR_PAR_${DBGU_MR_PAR}) | (${DBGU_MR_FILTER?then(1,0)} << DBGU_MR_FILTER_Pos));
    </#if>

    /* Configure ${DBGU_INSTANCE_NAME} Baud Rate */
    ${DBGU_INSTANCE_NAME}_REGS->DBGU_BRGR = DBGU_BRGR_CD(${BRG_VALUE});

    /* Initialize instance object */
    ${DBGU_INSTANCE_NAME?lower_case}Obj.rdCallback = NULL;
    ${DBGU_INSTANCE_NAME?lower_case}Obj.rdInIndex = 0;
    ${DBGU_INSTANCE_NAME?lower_case}Obj.rdOutIndex = 0;
    ${DBGU_INSTANCE_NAME?lower_case}Obj.isRdNotificationEnabled = false;
    ${DBGU_INSTANCE_NAME?lower_case}Obj.isRdNotifyPersistently = false;
    ${DBGU_INSTANCE_NAME?lower_case}Obj.rdThreshold = 0;
    ${DBGU_INSTANCE_NAME?lower_case}Obj.wrCallback = NULL;
    ${DBGU_INSTANCE_NAME?lower_case}Obj.wrInIndex = 0;
    ${DBGU_INSTANCE_NAME?lower_case}Obj.wrOutIndex = 0;
    ${DBGU_INSTANCE_NAME?lower_case}Obj.isWrNotificationEnabled = false;
    ${DBGU_INSTANCE_NAME?lower_case}Obj.isWrNotifyPersistently = false;
    ${DBGU_INSTANCE_NAME?lower_case}Obj.wrThreshold = 0;

    /* Enable receive interrupt */
    ${DBGU_INSTANCE_NAME}_RX_INT_ENABLE()
}

bool ${DBGU_INSTANCE_NAME}_SerialSetup( DBGU_SERIAL_SETUP *setup, uint32_t srcClkFreq )
{
    bool status = false;
    uint32_t baud = setup->baudRate;
    uint32_t brgVal = 0;
    uint32_t dbguMode;

    if (setup != NULL)
    {
        if(srcClkFreq == 0)
        {
            srcClkFreq = ${DBGU_INSTANCE_NAME}_FrequencyGet();
        }

        /* Calculate BRG value */
        brgVal = srcClkFreq / (16 * baud);

        /* If the target baud rate is acheivable using this clock */
        if (brgVal <= 65535)
        {
            /* Configure ${DBGU_INSTANCE_NAME} mode */
            dbguMode = ${DBGU_INSTANCE_NAME}_REGS->DBGU_MR;
            dbguMode &= ~DBGU_MR_PAR_Msk;
            ${DBGU_INSTANCE_NAME}_REGS->DBGU_MR = dbguMode | setup->parity ;

            /* Configure ${DBGU_INSTANCE_NAME} Baud Rate */
            ${DBGU_INSTANCE_NAME}_REGS->DBGU_BRGR = DBGU_BRGR_CD(brgVal);

            status = true;
        }
    }

    return status;
}

static void ${DBGU_INSTANCE_NAME}_ErrorClear( void )
{
    uint8_t dummyData = 0u;

    ${DBGU_INSTANCE_NAME}_REGS->DBGU_CR = DBGU_CR_RSTSTA_Msk;

    /* Flush existing error bytes from the RX FIFO */
    while( DBGU_SR_RXRDY_Msk == (${DBGU_INSTANCE_NAME}_REGS->DBGU_SR & DBGU_SR_RXRDY_Msk) )
    {
        dummyData = (${DBGU_INSTANCE_NAME}_REGS->DBGU_RHR & DBGU_RHR_RXCHR_Msk);
    }

    /* Ignore the warning */
    (void)dummyData;
}

DBGU_ERROR ${DBGU_INSTANCE_NAME}_ErrorGet( void )
{
    DBGU_ERROR errors = DBGU_ERROR_NONE;
    uint32_t status = ${DBGU_INSTANCE_NAME}_REGS->DBGU_SR;

    errors = (DBGU_ERROR)(status & (DBGU_SR_OVRE_Msk | DBGU_SR_PARE_Msk | DBGU_SR_FRAME_Msk));

    if(errors != DBGU_ERROR_NONE)
    {
        ${DBGU_INSTANCE_NAME}_ErrorClear();
    }

    /* All errors are cleared, but send the previous error state */
    return errors;
}

/* This routine is only called from ISR. Hence do not disable/enable DBGU interrupts. */
static inline bool ${DBGU_INSTANCE_NAME}_RxPushByte(uint8_t rdByte)
{
    uint32_t tempInIndex;
    bool isSuccess = false;

    tempInIndex = ${DBGU_INSTANCE_NAME?lower_case}Obj.rdInIndex + 1;

    if (tempInIndex >= ${DBGU_INSTANCE_NAME}_READ_BUFFER_SIZE)
    {
        tempInIndex = 0;
    }

    if (tempInIndex == ${DBGU_INSTANCE_NAME?lower_case}Obj.rdOutIndex)
    {
        /* Queue is full - Report it to the application. Application gets a chance to free up space by reading data out from the RX ring buffer */
        if(${DBGU_INSTANCE_NAME?lower_case}Obj.rdCallback != NULL)
        {
            ${DBGU_INSTANCE_NAME?lower_case}Obj.rdCallback(DBGU_EVENT_READ_BUFFER_FULL, ${DBGU_INSTANCE_NAME?lower_case}Obj.rdContext);
        }

        /* Read the indices again in case application has freed up space in RX ring buffer */
        tempInIndex = ${DBGU_INSTANCE_NAME?lower_case}Obj.rdInIndex + 1;

        if (tempInIndex >= ${DBGU_INSTANCE_NAME}_READ_BUFFER_SIZE)
        {
            tempInIndex = 0;
        }

    }

    if (tempInIndex != ${DBGU_INSTANCE_NAME?lower_case}Obj.rdOutIndex)
    {
        ${DBGU_INSTANCE_NAME}_ReadBuffer[${DBGU_INSTANCE_NAME?lower_case}Obj.rdInIndex] = rdByte;
        ${DBGU_INSTANCE_NAME?lower_case}Obj.rdInIndex = tempInIndex;
        isSuccess = true;
    }
    else
    {
        /* Queue is full. Data will be lost. */
    }

    return isSuccess;
}

/* This routine is only called from ISR. Hence do not disable/enable DBGU interrupts. */
static void ${DBGU_INSTANCE_NAME}_ReadNotificationSend(void)
{
    uint32_t nUnreadBytesAvailable;

    if (${DBGU_INSTANCE_NAME?lower_case}Obj.isRdNotificationEnabled == true)
    {
        nUnreadBytesAvailable = ${DBGU_INSTANCE_NAME}_ReadCountGet();

        if(${DBGU_INSTANCE_NAME?lower_case}Obj.rdCallback != NULL)
        {
            if (${DBGU_INSTANCE_NAME?lower_case}Obj.isRdNotifyPersistently == true)
            {
                if (nUnreadBytesAvailable >= ${DBGU_INSTANCE_NAME?lower_case}Obj.rdThreshold)
                {
                    ${DBGU_INSTANCE_NAME?lower_case}Obj.rdCallback(DBGU_EVENT_READ_THRESHOLD_REACHED, ${DBGU_INSTANCE_NAME?lower_case}Obj.rdContext);
                }
            }
            else
            {
                if (nUnreadBytesAvailable == ${DBGU_INSTANCE_NAME?lower_case}Obj.rdThreshold)
                {
                    ${DBGU_INSTANCE_NAME?lower_case}Obj.rdCallback(DBGU_EVENT_READ_THRESHOLD_REACHED, ${DBGU_INSTANCE_NAME?lower_case}Obj.rdContext);
                }
            }
        }
    }
}

size_t ${DBGU_INSTANCE_NAME}_Read(uint8_t* pRdBuffer, const size_t size)
{
    size_t nBytesRead = 0;
    uint32_t rdOutIndex;
    uint32_t rdInIndex;

    while (nBytesRead < size)
    {
        ${DBGU_INSTANCE_NAME}_RX_INT_DISABLE();

        rdOutIndex = ${DBGU_INSTANCE_NAME?lower_case}Obj.rdOutIndex;
        rdInIndex = ${DBGU_INSTANCE_NAME?lower_case}Obj.rdInIndex;

        if (rdOutIndex != rdInIndex)
        {
            pRdBuffer[nBytesRead++] = ${DBGU_INSTANCE_NAME}_ReadBuffer[${DBGU_INSTANCE_NAME?lower_case}Obj.rdOutIndex++];

            if (${DBGU_INSTANCE_NAME?lower_case}Obj.rdOutIndex >= ${DBGU_INSTANCE_NAME}_READ_BUFFER_SIZE)
            {
                ${DBGU_INSTANCE_NAME?lower_case}Obj.rdOutIndex = 0;
            }
            ${DBGU_INSTANCE_NAME}_RX_INT_ENABLE();
        }
        else
        {
            ${DBGU_INSTANCE_NAME}_RX_INT_ENABLE();
            break;
        }
    }

    return nBytesRead;
}

size_t ${DBGU_INSTANCE_NAME}_ReadCountGet(void)
{
    size_t nUnreadBytesAvailable;
    uint32_t rdInIndex;
    uint32_t rdOutIndex;

    /* Take  snapshot of indices to avoid creation of critical section */
    rdInIndex = ${DBGU_INSTANCE_NAME?lower_case}Obj.rdInIndex;
    rdOutIndex = ${DBGU_INSTANCE_NAME?lower_case}Obj.rdOutIndex;

    if ( rdInIndex >=  rdOutIndex)
    {
        nUnreadBytesAvailable =  rdInIndex - rdOutIndex;
    }
    else
    {
        nUnreadBytesAvailable =  (${DBGU_INSTANCE_NAME}_READ_BUFFER_SIZE -  rdOutIndex) + rdInIndex;
    }

    return nUnreadBytesAvailable;
}

size_t ${DBGU_INSTANCE_NAME}_ReadFreeBufferCountGet(void)
{
    return (${DBGU_INSTANCE_NAME}_READ_BUFFER_SIZE - 1) - ${DBGU_INSTANCE_NAME}_ReadCountGet();
}

size_t ${DBGU_INSTANCE_NAME}_ReadBufferSizeGet(void)
{
    return (${DBGU_INSTANCE_NAME}_READ_BUFFER_SIZE - 1);
}

bool ${DBGU_INSTANCE_NAME}_ReadNotificationEnable(bool isEnabled, bool isPersistent)
{
    bool previousStatus = ${DBGU_INSTANCE_NAME?lower_case}Obj.isRdNotificationEnabled;

    ${DBGU_INSTANCE_NAME?lower_case}Obj.isRdNotificationEnabled = isEnabled;

    ${DBGU_INSTANCE_NAME?lower_case}Obj.isRdNotifyPersistently = isPersistent;

    return previousStatus;
}

void ${DBGU_INSTANCE_NAME}_ReadThresholdSet(uint32_t nBytesThreshold)
{
    if (nBytesThreshold > 0)
    {
        ${DBGU_INSTANCE_NAME?lower_case}Obj.rdThreshold = nBytesThreshold;
    }
}

void ${DBGU_INSTANCE_NAME}_ReadCallbackRegister( DBGU_RING_BUFFER_CALLBACK callback, uintptr_t context)
{
    ${DBGU_INSTANCE_NAME?lower_case}Obj.rdCallback = callback;

    ${DBGU_INSTANCE_NAME?lower_case}Obj.rdContext = context;
}

/* This routine is only called from ISR. Hence do not disable/enable DBGU interrupts. */
static bool ${DBGU_INSTANCE_NAME}_TxPullByte(uint8_t* pWrByte)
{
    bool isSuccess = false;
    uint32_t wrOutIndex = ${DBGU_INSTANCE_NAME?lower_case}Obj.wrOutIndex;
    uint32_t wrInIndex = ${DBGU_INSTANCE_NAME?lower_case}Obj.wrInIndex;

    if (wrOutIndex != wrInIndex)
    {
        *pWrByte = ${DBGU_INSTANCE_NAME}_WriteBuffer[${DBGU_INSTANCE_NAME?lower_case}Obj.wrOutIndex++];

        if (${DBGU_INSTANCE_NAME?lower_case}Obj.wrOutIndex >= ${DBGU_INSTANCE_NAME}_WRITE_BUFFER_SIZE)
        {
            ${DBGU_INSTANCE_NAME?lower_case}Obj.wrOutIndex = 0;
        }
        isSuccess = true;
    }

    return isSuccess;
}

static inline bool ${DBGU_INSTANCE_NAME}_TxPushByte(uint8_t wrByte)
{
    uint32_t tempInIndex;
    bool isSuccess = false;

    tempInIndex = ${DBGU_INSTANCE_NAME?lower_case}Obj.wrInIndex + 1;

    if (tempInIndex >= ${DBGU_INSTANCE_NAME}_WRITE_BUFFER_SIZE)
    {
        tempInIndex = 0;
    }
    if (tempInIndex != ${DBGU_INSTANCE_NAME?lower_case}Obj.wrOutIndex)
    {
        ${DBGU_INSTANCE_NAME}_WriteBuffer[${DBGU_INSTANCE_NAME?lower_case}Obj.wrInIndex] = wrByte;
        ${DBGU_INSTANCE_NAME?lower_case}Obj.wrInIndex = tempInIndex;
        isSuccess = true;
    }
    else
    {
        /* Queue is full. Report Error. */
    }

    return isSuccess;
}

/* This routine is only called from ISR. Hence do not disable/enable DBGU interrupts. */
static void ${DBGU_INSTANCE_NAME}_WriteNotificationSend(void)
{
    uint32_t nFreeWrBufferCount;

    if (${DBGU_INSTANCE_NAME?lower_case}Obj.isWrNotificationEnabled == true)
    {
        nFreeWrBufferCount = ${DBGU_INSTANCE_NAME}_WriteFreeBufferCountGet();

        if(${DBGU_INSTANCE_NAME?lower_case}Obj.wrCallback != NULL)
        {
            if (${DBGU_INSTANCE_NAME?lower_case}Obj.isWrNotifyPersistently == true)
            {
                if (nFreeWrBufferCount >= ${DBGU_INSTANCE_NAME?lower_case}Obj.wrThreshold)
                {
                    ${DBGU_INSTANCE_NAME?lower_case}Obj.wrCallback(DBGU_EVENT_WRITE_THRESHOLD_REACHED, ${DBGU_INSTANCE_NAME?lower_case}Obj.wrContext);
                }
            }
            else
            {
                if (nFreeWrBufferCount == ${DBGU_INSTANCE_NAME?lower_case}Obj.wrThreshold)
                {
                    ${DBGU_INSTANCE_NAME?lower_case}Obj.wrCallback(DBGU_EVENT_WRITE_THRESHOLD_REACHED, ${DBGU_INSTANCE_NAME?lower_case}Obj.wrContext);
                }
            }
        }
    }
}

static size_t ${DBGU_INSTANCE_NAME}_WritePendingBytesGet(void)
{
    size_t nPendingTxBytes;

    /* Take a snapshot of indices to avoid creation of critical section */
    uint32_t wrOutIndex = ${DBGU_INSTANCE_NAME?lower_case}Obj.wrOutIndex;
    uint32_t wrInIndex = ${DBGU_INSTANCE_NAME?lower_case}Obj.wrInIndex;

    if ( wrInIndex >=  wrOutIndex)
    {
        nPendingTxBytes =  wrInIndex -  wrOutIndex;
    }
    else
    {
        nPendingTxBytes =  (${DBGU_INSTANCE_NAME}_WRITE_BUFFER_SIZE -  wrOutIndex) + wrInIndex;
    }

    return nPendingTxBytes;
}

size_t ${DBGU_INSTANCE_NAME}_WriteCountGet(void)
{
    size_t nPendingTxBytes;

    nPendingTxBytes = ${DBGU_INSTANCE_NAME}_WritePendingBytesGet();

    return nPendingTxBytes;
}

size_t ${DBGU_INSTANCE_NAME}_Write(uint8_t* pWrBuffer, const size_t size )
{
    size_t nBytesWritten  = 0;

    ${DBGU_INSTANCE_NAME}_TX_INT_DISABLE();

    while (nBytesWritten < size)
    {
        if (${DBGU_INSTANCE_NAME}_TxPushByte(pWrBuffer[nBytesWritten]) == true)
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
    if (${DBGU_INSTANCE_NAME}_WritePendingBytesGet() > 0)
    {
        /* Enable TX interrupt as data is pending for transmission */
        ${DBGU_INSTANCE_NAME}_TX_INT_ENABLE();
    }

    return nBytesWritten;
}

size_t ${DBGU_INSTANCE_NAME}_WriteFreeBufferCountGet(void)
{
    return (${DBGU_INSTANCE_NAME}_WRITE_BUFFER_SIZE - 1) - ${DBGU_INSTANCE_NAME}_WriteCountGet();
}

size_t ${DBGU_INSTANCE_NAME}_WriteBufferSizeGet(void)
{
    return (${DBGU_INSTANCE_NAME}_WRITE_BUFFER_SIZE - 1);
}

bool ${DBGU_INSTANCE_NAME}_TransmitComplete(void)
{
    return ((${DBGU_INSTANCE_NAME}_REGS->DBGU_SR & DBGU_SR_TXEMPTY_Msk) == DBGU_SR_TXEMPTY_Msk);
}

bool ${DBGU_INSTANCE_NAME}_WriteNotificationEnable(bool isEnabled, bool isPersistent)
{
    bool previousStatus = ${DBGU_INSTANCE_NAME?lower_case}Obj.isWrNotificationEnabled;

    ${DBGU_INSTANCE_NAME?lower_case}Obj.isWrNotificationEnabled = isEnabled;

    ${DBGU_INSTANCE_NAME?lower_case}Obj.isWrNotifyPersistently = isPersistent;

    return previousStatus;
}

void ${DBGU_INSTANCE_NAME}_WriteThresholdSet(uint32_t nBytesThreshold)
{
    if (nBytesThreshold > 0)
    {
        ${DBGU_INSTANCE_NAME?lower_case}Obj.wrThreshold = nBytesThreshold;
    }
}

void ${DBGU_INSTANCE_NAME}_WriteCallbackRegister( DBGU_RING_BUFFER_CALLBACK callback, uintptr_t context)
{
    ${DBGU_INSTANCE_NAME?lower_case}Obj.wrCallback = callback;

    ${DBGU_INSTANCE_NAME?lower_case}Obj.wrContext = context;
}

static void ${DBGU_INSTANCE_NAME}_ISR_RX_Handler( void )
{
    /* Keep reading until there is a character availabe in the RX FIFO */
    while(DBGU_SR_RXRDY_Msk == (${DBGU_INSTANCE_NAME}_REGS->DBGU_SR& DBGU_SR_RXRDY_Msk))
    {
        if (${DBGU_INSTANCE_NAME}_RxPushByte( (uint8_t )(${DBGU_INSTANCE_NAME}_REGS->DBGU_RHR& DBGU_RHR_RXCHR_Msk) ) == true)
        {
            ${DBGU_INSTANCE_NAME}_ReadNotificationSend();
        }
        else
        {
            /* DBGU RX buffer is full */
        }
    }
}

static void ${DBGU_INSTANCE_NAME}_ISR_TX_Handler( void )
{
    uint8_t wrByte;

    /* Keep writing to the TX FIFO as long as there is space */
    while(DBGU_SR_TXRDY_Msk == (${DBGU_INSTANCE_NAME}_REGS->DBGU_SR & DBGU_SR_TXRDY_Msk))
    {
        if (${DBGU_INSTANCE_NAME}_TxPullByte(&wrByte) == true)
        {
            ${DBGU_INSTANCE_NAME}_REGS->DBGU_THR |= wrByte;

            /* Send notification */
            ${DBGU_INSTANCE_NAME}_WriteNotificationSend();
        }
        else
        {
            /* Nothing to transmit. Disable the data register empty interrupt. */
            ${DBGU_INSTANCE_NAME}_TX_INT_DISABLE();
            break;
        }
    }
}

void ${DBGU_INSTANCE_NAME}_InterruptHandler( void )
{
    /* Error status */
    uint32_t errorStatus = (${DBGU_INSTANCE_NAME}_REGS->DBGU_SR & (DBGU_SR_OVRE_Msk | DBGU_SR_FRAME_Msk | DBGU_SR_PARE_Msk));

    if(errorStatus != 0)
    {
        /* Client must call DBGUx_ErrorGet() function to clear the errors */

        /* Disable Read, Overrun, Parity and Framing error interrupts */

        ${DBGU_INSTANCE_NAME}_REGS->DBGU_IDR = (DBGU_IDR_RXRDY_Msk | DBGU_IDR_FRAME_Msk | DBGU_IDR_PARE_Msk | DBGU_IDR_OVRE_Msk);

        /* DBGU errors are normally associated with the receiver, hence calling
         * receiver callback */
        if( ${DBGU_INSTANCE_NAME?lower_case}Obj.rdCallback != NULL )
        {
            ${DBGU_INSTANCE_NAME?lower_case}Obj.rdCallback(DBGU_EVENT_READ_ERROR, ${DBGU_INSTANCE_NAME?lower_case}Obj.rdContext);
        }
    }

    /* Receiver status */
    if(DBGU_SR_RXRDY_Msk == (${DBGU_INSTANCE_NAME}_REGS->DBGU_SR & DBGU_SR_RXRDY_Msk))
    {
        ${DBGU_INSTANCE_NAME}_ISR_RX_Handler();
    }

    /* Transmitter status */
    if(DBGU_SR_TXRDY_Msk == (${DBGU_INSTANCE_NAME}_REGS->DBGU_SR & DBGU_SR_TXRDY_Msk))
    {
        ${DBGU_INSTANCE_NAME}_ISR_TX_Handler();
    }

}