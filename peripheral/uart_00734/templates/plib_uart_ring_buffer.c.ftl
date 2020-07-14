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
* Copyright (C) 2019 Microchip Technology Inc. and its subsidiaries.
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
#define ${UART_INSTANCE_NAME}_RX_INT_DISABLE()      ${UART_RX_IEC_REG}CLR = _${UART_RX_IEC_REG}_U${UART_INSTANCE_NUM}RXIE_MASK;
#define ${UART_INSTANCE_NAME}_RX_INT_ENABLE()       ${UART_RX_IEC_REG}SET = _${UART_RX_IEC_REG}_U${UART_INSTANCE_NUM}RXIE_MASK;

static uint8_t ${UART_INSTANCE_NAME}_ReadBuffer[${UART_INSTANCE_NAME}_READ_BUFFER_SIZE];

#define ${UART_INSTANCE_NAME}_WRITE_BUFFER_SIZE     ${UART_TX_RING_BUFFER_SIZE}
#define ${UART_INSTANCE_NAME}_TX_INT_DISABLE()      ${UART_TX_IEC_REG}CLR = _${UART_TX_IEC_REG}_U${UART_INSTANCE_NUM}TXIE_MASK;
#define ${UART_INSTANCE_NAME}_TX_INT_ENABLE()       ${UART_TX_IEC_REG}SET = _${UART_TX_IEC_REG}_U${UART_INSTANCE_NUM}TXIE_MASK;

static uint8_t ${UART_INSTANCE_NAME}_WriteBuffer[${UART_INSTANCE_NAME}_WRITE_BUFFER_SIZE];

void static ${UART_INSTANCE_NAME}_ErrorClear( void )
{
    /* rxBufferLen = (FIFO level + RX register) */
    uint8_t rxBufferLen = UART_RXFIFO_DEPTH;
    uint8_t dummyData = 0u;

    /* If it's a overrun error then clear it to flush FIFO */
    if(U${UART_INSTANCE_NUM}STA & _U${UART_INSTANCE_NUM}STA_OERR_MASK)
    {
        U${UART_INSTANCE_NUM}STACLR = _U${UART_INSTANCE_NUM}STA_OERR_MASK;
    }

    /* Read existing error bytes from FIFO to clear parity and framing error flags */
    while(U${UART_INSTANCE_NUM}STA & (_U${UART_INSTANCE_NUM}STA_FERR_MASK | _U${UART_INSTANCE_NUM}STA_PERR_MASK))
    {
        dummyData = (uint8_t )(U${UART_INSTANCE_NUM}RXREG );
        rxBufferLen--;

        /* Try to flush error bytes for one full FIFO and exit instead of
         * blocking here if more error bytes are received */
        if(rxBufferLen == 0u)
        {
            break;
        }
    }

    // Ignore the warning
    (void)dummyData;

    /* Clear error interrupt flag */
    ${UART_FAULT_IFS_REG}CLR = _${UART_FAULT_IFS_REG}_U${UART_INSTANCE_NUM}EIF_MASK;

    /* Clear up the receive interrupt flag so that RX interrupt is not
     * triggered for error bytes */
    ${UART_FAULT_IFS_REG}CLR = _${UART_FAULT_IFS_REG}_U${UART_INSTANCE_NUM}RXIF_MASK;

    return;
}

void ${UART_INSTANCE_NAME}_Initialize( void )
{
    /* Set up UxMODE bits */
    /* STSEL  = ${UART_STOPBIT_SELECT} */
    /* PDSEL = ${UART_PDBIT_SELECT} */

    U${UART_INSTANCE_NUM}MODE = 0x${UMODE_VALUE};

    /* Enable ${UART_INSTANCE_NAME} Receiver and Transmitter */
    U${UART_INSTANCE_NUM}STASET = (_U${UART_INSTANCE_NUM}STA_UTXEN_MASK | _U${UART_INSTANCE_NUM}STA_URXEN_MASK);

    /* BAUD Rate register Setup */
    U${UART_INSTANCE_NUM}BRG = ${BRG_VALUE};

    /* Disable Interrupts */
    ${UART_FAULT_IEC_REG}CLR = _${UART_FAULT_IEC_REG}_U${UART_INSTANCE_NUM}EIE_MASK;

    ${UART_RX_IEC_REG}CLR = _${UART_RX_IEC_REG}_U${UART_INSTANCE_NUM}RXIE_MASK;

    ${UART_TX_IEC_REG}CLR = _${UART_TX_IEC_REG}_U${UART_INSTANCE_NUM}TXIE_MASK;

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

    /* Turn ON ${UART_INSTANCE_NAME} */
    U${UART_INSTANCE_NUM}MODESET = _U${UART_INSTANCE_NUM}MODE_ON_MASK;

    /* Enable ${UART_INSTANCE_NAME}_FAULT Interrupt */
    ${UART_FAULT_IEC_REG}SET = _${UART_FAULT_IEC_REG}_U${UART_INSTANCE_NUM}EIE_MASK;

    /* Enable ${UART_INSTANCE_NAME}_RX Interrupt */
    ${UART_RX_IEC_REG}SET = _${UART_RX_IEC_REG}_U${UART_INSTANCE_NUM}RXIE_MASK;
}

bool ${UART_INSTANCE_NAME}_SerialSetup( UART_SERIAL_SETUP *setup, uint32_t srcClkFreq )
{
    bool status = false;
    uint32_t baud;
    int32_t brgValHigh = 0;
    int32_t brgValLow = 0;
    uint32_t brgVal = 0;
    uint32_t uartMode;

    if (setup != NULL)
    {
        baud = setup->baudRate;

        if (baud == 0)
        {
            return status;
        }

        if(srcClkFreq == 0)
        {
            srcClkFreq = ${UART_INSTANCE_NAME}_FrequencyGet();
        }

        /* Calculate BRG value */
        brgValLow = (((srcClkFreq >> 4) + (baud >> 1)) / baud ) - 1;
        brgValHigh = (((srcClkFreq >> 2) + (baud >> 1)) / baud ) - 1;

        /* Check if the baud value can be set with low baud settings */
        if((brgValLow >= 0) && (brgValLow <= UINT16_MAX))
        {
            brgVal =  brgValLow;
            U${UART_INSTANCE_NUM}MODECLR = _U${UART_INSTANCE_NUM}MODE_BRGH_MASK;
        }
        else if ((brgValHigh >= 0) && (brgValHigh <= UINT16_MAX))
        {
            brgVal = brgValHigh;
            U${UART_INSTANCE_NUM}MODESET = _U${UART_INSTANCE_NUM}MODE_BRGH_MASK;
        }
        else
        {
            return status;
        }

        if(setup->dataWidth == UART_DATA_9_BIT)
        {
            if(setup->parity != UART_PARITY_NONE)
            {
               return status;
            }
            else
            {
               /* Configure ${UART_INSTANCE_NAME} mode */
               uartMode = U${UART_INSTANCE_NUM}MODE;
               uartMode &= ~_U${UART_INSTANCE_NUM}MODE_PDSEL_MASK;
               U${UART_INSTANCE_NUM}MODE = uartMode | setup->dataWidth;
            }
        }
        else
        {
            /* Configure ${UART_INSTANCE_NAME} mode */
            uartMode = U${UART_INSTANCE_NUM}MODE;
            uartMode &= ~_U${UART_INSTANCE_NUM}MODE_PDSEL_MASK;
            U${UART_INSTANCE_NUM}MODE = uartMode | setup->parity ;
        }

        /* Configure ${UART_INSTANCE_NAME} mode */
        uartMode = U${UART_INSTANCE_NUM}MODE;
        uartMode &= ~_U${UART_INSTANCE_NUM}MODE_STSEL_MASK;
        U${UART_INSTANCE_NUM}MODE = uartMode | setup->stopBits ;

        /* Configure ${UART_INSTANCE_NAME} Baud Rate */
        U${UART_INSTANCE_NUM}BRG = brgVal;

        status = true;
    }

    return status;
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

            /* Read the indices again in case application has freed up space in RX ring buffer */
            tempInIndex = ${UART_INSTANCE_NAME?lower_case}Obj.rdInIndex + 1;

            if (tempInIndex >= ${UART_INSTANCE_NAME}_READ_BUFFER_SIZE)
            {
                tempInIndex = 0;
            }
        }
    }

    /* Attempt to push the data into the ring buffer */
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

    /* Take a snapshot of indices to avoid processing in critical section */
    rdInIndex = ${UART_INSTANCE_NAME?lower_case}Obj.rdInIndex;
    rdOutIndex = ${UART_INSTANCE_NAME?lower_case}Obj.rdOutIndex;

    if ( rdInIndex >=  rdOutIndex)
    {
        nUnreadBytesAvailable =  rdInIndex -  rdOutIndex;
    }
    else
    {
        nUnreadBytesAvailable =  (${UART_INSTANCE_NAME}_READ_BUFFER_SIZE -  rdOutIndex) + rdInIndex;
    }

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

    /* Take a snapshot of indices to avoid processing in critical section */
    uint32_t wrOutIndex = ${UART_INSTANCE_NAME?lower_case}Obj.wrOutIndex;
    uint32_t wrInIndex = ${UART_INSTANCE_NAME?lower_case}Obj.wrInIndex;

    if ( wrInIndex >=  wrOutIndex)
    {
        nPendingTxBytes =  wrInIndex - wrOutIndex;
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

    nPendingTxBytes = ${UART_INSTANCE_NAME}_WritePendingBytesGet();

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

UART_ERROR ${UART_INSTANCE_NAME}_ErrorGet( void )
{
    UART_ERROR errors = UART_ERROR_NONE;
    uint32_t status = U${UART_INSTANCE_NUM}STA;

    errors = (UART_ERROR)(status & (_U${UART_INSTANCE_NUM}STA_OERR_MASK | _U${UART_INSTANCE_NUM}STA_FERR_MASK | _U${UART_INSTANCE_NUM}STA_PERR_MASK));

    if(errors != UART_ERROR_NONE)
    {
        ${UART_INSTANCE_NAME}_ErrorClear();
    }

    /* All errors are cleared, but send the previous error state */
    return errors;
}

<#if UART_INTERRUPT_COUNT == 1>
static void ${UART_INSTANCE_NAME}_FAULT_InterruptHandler (void)
<#else>
void ${UART_INSTANCE_NAME}_FAULT_InterruptHandler (void)
</#if>
{
    /* Disable the fault interrupt */
    ${UART_FAULT_IEC_REG}CLR = _${UART_FAULT_IEC_REG}_U${UART_INSTANCE_NUM}EIE_MASK;
    /* Disable the receive interrupt */
    ${UART_RX_IEC_REG}CLR = _${UART_RX_IEC_REG}_U${UART_INSTANCE_NUM}RXIE_MASK;

    /* Client must call UARTx_ErrorGet() function to clear the errors */
    if( ${UART_INSTANCE_NAME?lower_case}Obj.rdCallback != NULL )
    {
        ${UART_INSTANCE_NAME?lower_case}Obj.rdCallback(UART_EVENT_READ_ERROR, ${UART_INSTANCE_NAME?lower_case}Obj.rdContext);
    }
}

<#if UART_INTERRUPT_COUNT == 1>
static void ${UART_INSTANCE_NAME}_RX_InterruptHandler (void)
<#else>
void ${UART_INSTANCE_NAME}_RX_InterruptHandler (void)
</#if>
{
    /* Clear ${UART_INSTANCE_NAME} RX Interrupt flag */
    ${UART_RX_IFS_REG}CLR = _${UART_RX_IFS_REG}_U${UART_INSTANCE_NUM}RXIF_MASK;

    /* Keep reading until there is a character availabe in the RX FIFO */
    while((U${UART_INSTANCE_NUM}STA & _U${UART_INSTANCE_NUM}STA_URXDA_MASK) == _U${UART_INSTANCE_NUM}STA_URXDA_MASK)
    {
        if (${UART_INSTANCE_NAME}_RxPushByte( (uint8_t )(U${UART_INSTANCE_NUM}RXREG) ) == true)
        {
            ${UART_INSTANCE_NAME}_ReadNotificationSend();
        }
        else
        {
            /* UART RX buffer is full */
        }
    }
}

<#if UART_INTERRUPT_COUNT == 1>
static void ${UART_INSTANCE_NAME}_TX_InterruptHandler (void)
<#else>
void ${UART_INSTANCE_NAME}_TX_InterruptHandler (void)
</#if>
{
    uint8_t wrByte;

    /* Check if any data is pending for transmission */
    if (${UART_INSTANCE_NAME}_WritePendingBytesGet() > 0)
    {
        /* Clear ${UART_INSTANCE_NAME}TX Interrupt flag */
        ${UART_TX_IFS_REG}CLR = _${UART_TX_IFS_REG}_U${UART_INSTANCE_NUM}TXIF_MASK;

        /* Keep writing to the TX FIFO as long as there is space */
        while(!(U${UART_INSTANCE_NUM}STA & _U${UART_INSTANCE_NUM}STA_UTXBF_MASK))
        {
            if (${UART_INSTANCE_NAME}_TxPullByte(&wrByte) == true)
            {
                U${UART_INSTANCE_NUM}TXREG = wrByte;

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
    else
    {
        /* Nothing to transmit. Disable the data register empty interrupt. */
        ${UART_INSTANCE_NAME}_TX_INT_DISABLE();
    }
}

<#if UART_INTERRUPT_COUNT == 1>
void UART_${UART_INSTANCE_NUM}_InterruptHandler (void)
{
    /* Call RX handler if RX interrupt flag is set */
    if ((${UART_RX_IFS_REG} & _${UART_RX_IFS_REG}_U${UART_INSTANCE_NUM}RXIF_MASK) && (${UART_RX_IEC_REG} & _${UART_RX_IEC_REG}_U${UART_INSTANCE_NUM}RXIE_MASK))
    {
        ${UART_INSTANCE_NAME}_RX_InterruptHandler();
    }
    /* Call TX handler if TX interrupt flag is set */
    else if ((${UART_TX_IFS_REG} & _${UART_TX_IFS_REG}_U${UART_INSTANCE_NUM}TXIF_MASK) && (${UART_TX_IEC_REG} & _${UART_TX_IEC_REG}_U${UART_INSTANCE_NUM}TXIE_MASK))
    {
        ${UART_INSTANCE_NAME}_TX_InterruptHandler();
    }
    /* Call Error handler if Error interrupt flag is set */
    else if ((${UART_FAULT_IFS_REG} & _${UART_FAULT_IFS_REG}_U${UART_INSTANCE_NUM}EIF_MASK) && (${UART_FAULT_IEC_REG} & _${UART_FAULT_IEC_REG}_U${UART_INSTANCE_NUM}EIE_MASK))
    {
        ${UART_INSTANCE_NAME}_FAULT_InterruptHandler();
    }
}
</#if>