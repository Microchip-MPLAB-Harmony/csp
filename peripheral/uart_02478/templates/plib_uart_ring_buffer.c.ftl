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
#define ${UART_INSTANCE_NAME}_READ_BUFFER_SIZE_9BIT (${UART_RX_RING_BUFFER_SIZE} >> 1)
#define ${UART_INSTANCE_NAME}_RX_INT_DISABLE()      ${UART_RX_IEC_REG}CLR = _${UART_RX_IEC_REG}_U${UART_INSTANCE_NUM}RXIE_MASK;
#define ${UART_INSTANCE_NAME}_RX_INT_ENABLE()       ${UART_RX_IEC_REG}SET = _${UART_RX_IEC_REG}_U${UART_INSTANCE_NUM}RXIE_MASK;

static uint8_t ${UART_INSTANCE_NAME}_ReadBuffer[${UART_INSTANCE_NAME}_READ_BUFFER_SIZE];

#define ${UART_INSTANCE_NAME}_WRITE_BUFFER_SIZE     ${UART_TX_RING_BUFFER_SIZE}
#define ${UART_INSTANCE_NAME}_WRITE_BUFFER_SIZE_9BIT       (${UART_TX_RING_BUFFER_SIZE} >> 1)
#define ${UART_INSTANCE_NAME}_TX_INT_DISABLE()      ${UART_TX_IEC_REG}CLR = _${UART_TX_IEC_REG}_U${UART_INSTANCE_NUM}TXIE_MASK;
#define ${UART_INSTANCE_NAME}_TX_INT_ENABLE()       ${UART_TX_IEC_REG}SET = _${UART_TX_IEC_REG}_U${UART_INSTANCE_NUM}TXIE_MASK;

static uint8_t ${UART_INSTANCE_NAME}_WriteBuffer[${UART_INSTANCE_NAME}_WRITE_BUFFER_SIZE];

#define ${UART_INSTANCE_NAME}_IS_9BIT_MODE_ENABLED()    ( U${UART_INSTANCE_NUM}MODE & (_U${UART_INSTANCE_NUM}MODE_PDSEL0_MASK | _U${UART_INSTANCE_NUM}MODE_PDSEL1_MASK)) == (_U${UART_INSTANCE_NUM}MODE_PDSEL0_MASK | _U${UART_INSTANCE_NUM}MODE_PDSEL1_MASK) ? true:false

void static ${UART_INSTANCE_NAME}_ErrorClear( void )
{
    UART_ERROR errors = UART_ERROR_NONE;
    uint8_t dummyData = 0u;

    errors = (UART_ERROR)(U${UART_INSTANCE_NUM}STA & (_U${UART_INSTANCE_NUM}STA_OERR_MASK | _U${UART_INSTANCE_NUM}STA_FERR_MASK | _U${UART_INSTANCE_NUM}STA_PERR_MASK));

    if(errors != UART_ERROR_NONE)
    {
        /* If it's a overrun error then clear it to flush FIFO */
        if(U${UART_INSTANCE_NUM}STA & _U${UART_INSTANCE_NUM}STA_OERR_MASK)
        {
            U${UART_INSTANCE_NUM}STACLR = _U${UART_INSTANCE_NUM}STA_OERR_MASK;
        }

        /* Read existing error bytes from FIFO to clear parity and framing error flags */
        while(U${UART_INSTANCE_NUM}STA & _U${UART_INSTANCE_NUM}STA_URXDA_MASK)
        {
            dummyData = U${UART_INSTANCE_NUM}RXREG;
        }

        /* Clear error interrupt flag */
        ${UART_FAULT_IFS_REG}CLR = _${UART_FAULT_IFS_REG}_U${UART_INSTANCE_NUM}EIF_MASK;

        /* Clear up the receive interrupt flag so that RX interrupt is not
         * triggered for error bytes */
        ${UART_FAULT_IFS_REG}CLR = _${UART_FAULT_IFS_REG}_U${UART_INSTANCE_NUM}RXIF_MASK;

    }

    // Ignore the warning
    (void)dummyData;
}

void ${UART_INSTANCE_NAME}_Initialize( void )
{
    /* Set up UxMODE bits */
    /* STSEL  = ${UART_STSEL}*/
    /* PDSEL = ${UART_PDSEL} */
    /* BRGH = ${UART_BRGH} */
    /* RXINV = ${UART_RXINV} */
    /* ABAUD = ${UART_ABAUD} */
    /* LPBACK = ${UART_LPBACK} */
    /* WAKE = ${UART_WAKE} */
    /* SIDL = ${UART_SIDL} */
    /* RUNOVF = ${UART_RUNOVF} */
    /* CLKSEL = ${UART_CLKSEL} */
    /* SLPEN = ${UART_SLPEN} */
    U${UART_INSTANCE_NUM}MODE = 0x${UMODE_VALUE};

    /* Enable ${UART_INSTANCE_NAME} Receiver, Transmitter and TX Interrupt selection */
    U${UART_INSTANCE_NUM}STASET = (_U${UART_INSTANCE_NUM}STA_UTXEN_MASK | _U${UART_INSTANCE_NUM}STA_URXEN_MASK | _U${UART_INSTANCE_NUM}STA_UTXISEL1_MASK <#if UART_AUTOMATIC_ADDR_DETECTION_ENABLE == true> | _U${UART_INSTANCE_NUM}STA_ADDEN_MASK | (0x${UART_9BIT_MODE_ADDR} << _U${UART_INSTANCE_NUM}STA_ADDR_POSITION) | (0x${UART_9BIT_MODE_ADDR_MASK} << _U${UART_INSTANCE_NUM}STA_MASK_POSITION) </#if>);

    /* BAUD Rate register Setup */
    U${UART_INSTANCE_NUM}BRG = ${BRG_VALUE};

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

    ${UART_INSTANCE_NAME?lower_case}Obj.errors = UART_ERROR_NONE;

<#if UART_AUTOMATIC_ADDR_DETECTION_ENABLE == true>
    ${UART_INSTANCE_NAME?lower_case}Obj.rdBufferSize = ${UART_INSTANCE_NAME}_READ_BUFFER_SIZE;
    ${UART_INSTANCE_NAME?lower_case}Obj.wrBufferSize = ${UART_INSTANCE_NAME}_WRITE_BUFFER_SIZE_9BIT;
<#else>
    if (${UART_INSTANCE_NAME}_IS_9BIT_MODE_ENABLED())
    {
        ${UART_INSTANCE_NAME?lower_case}Obj.rdBufferSize = ${UART_INSTANCE_NAME}_READ_BUFFER_SIZE_9BIT;
        ${UART_INSTANCE_NAME?lower_case}Obj.wrBufferSize = ${UART_INSTANCE_NAME}_WRITE_BUFFER_SIZE_9BIT;
    }
    else
    {
        ${UART_INSTANCE_NAME?lower_case}Obj.rdBufferSize = ${UART_INSTANCE_NAME}_READ_BUFFER_SIZE;
        ${UART_INSTANCE_NAME?lower_case}Obj.wrBufferSize = ${UART_INSTANCE_NAME}_WRITE_BUFFER_SIZE;
    }
</#if>


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

        /* Turn OFF ${UART_INSTANCE_NAME} */
        U${UART_INSTANCE_NUM}MODECLR = _U${UART_INSTANCE_NUM}MODE_ON_MASK;

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

<#if UART_AUTOMATIC_ADDR_DETECTION_ENABLE == false>
        if (${UART_INSTANCE_NAME}_IS_9BIT_MODE_ENABLED())
        {
            ${UART_INSTANCE_NAME?lower_case}Obj.rdBufferSize = ${UART_INSTANCE_NAME}_READ_BUFFER_SIZE_9BIT;
            ${UART_INSTANCE_NAME?lower_case}Obj.wrBufferSize = ${UART_INSTANCE_NAME}_WRITE_BUFFER_SIZE_9BIT;
        }
        else
        {
            ${UART_INSTANCE_NAME?lower_case}Obj.rdBufferSize = ${UART_INSTANCE_NAME}_READ_BUFFER_SIZE;
            ${UART_INSTANCE_NAME?lower_case}Obj.wrBufferSize = ${UART_INSTANCE_NAME}_WRITE_BUFFER_SIZE;
        }
</#if>

        U${UART_INSTANCE_NUM}MODESET = _U${UART_INSTANCE_NUM}MODE_ON_MASK;

        status = true;
    }

    return status;
}

/* This routine is only called from ISR. Hence do not disable/enable USART interrupts. */
static inline bool ${UART_INSTANCE_NAME}_RxPushByte(uint16_t rdByte)
{
    uint32_t tempInIndex;
    bool isSuccess = false;

    tempInIndex = ${UART_INSTANCE_NAME?lower_case}Obj.rdInIndex + 1;

    if (tempInIndex >= ${UART_INSTANCE_NAME?lower_case}Obj.rdBufferSize)
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

            if (tempInIndex >= ${UART_INSTANCE_NAME?lower_case}Obj.rdBufferSize)
            {
                tempInIndex = 0;
            }
        }
    }

    /* Attempt to push the data into the ring buffer */
    if (tempInIndex != ${UART_INSTANCE_NAME?lower_case}Obj.rdOutIndex)
    {
<#if UART_AUTOMATIC_ADDR_DETECTION_ENABLE == true>
        ${UART_INSTANCE_NAME}_ReadBuffer[${UART_INSTANCE_NAME?lower_case}Obj.rdInIndex] = (uint8_t)rdByte;
<#else>
        if (${UART_INSTANCE_NAME}_IS_9BIT_MODE_ENABLED())
        {
            ((uint16_t*)&${UART_INSTANCE_NAME}_ReadBuffer)[${UART_INSTANCE_NAME?lower_case}Obj.rdInIndex] = rdByte;
        }
        else
        {
            ${UART_INSTANCE_NAME}_ReadBuffer[${UART_INSTANCE_NAME?lower_case}Obj.rdInIndex] = (uint8_t)rdByte;
        }
</#if>

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
    uint32_t rdOutIndex = 0;
    uint32_t rdInIndex = 0;

    /* Take a snapshot of indices to avoid creation of critical section */
    rdOutIndex = ${UART_INSTANCE_NAME?lower_case}Obj.rdOutIndex;
    rdInIndex = ${UART_INSTANCE_NAME?lower_case}Obj.rdInIndex;

    while (nBytesRead < size)
    {
        if (rdOutIndex != rdInIndex)
        {
<#if UART_AUTOMATIC_ADDR_DETECTION_ENABLE == true>
            pRdBuffer[nBytesRead++] = ${UART_INSTANCE_NAME}_ReadBuffer[rdOutIndex++];
<#else>
            if (${UART_INSTANCE_NAME}_IS_9BIT_MODE_ENABLED())
            {
                ((uint16_t*)pRdBuffer)[nBytesRead++] = ((uint16_t*)&${UART_INSTANCE_NAME}_ReadBuffer)[rdOutIndex++];
            }
            else
            {
                pRdBuffer[nBytesRead++] = ${UART_INSTANCE_NAME}_ReadBuffer[rdOutIndex++];
            }
</#if>

            if (rdOutIndex >= ${UART_INSTANCE_NAME?lower_case}Obj.rdBufferSize)
            {
                rdOutIndex = 0;
            }
        }
        else
        {
            /* No more data available in the RX buffer */
            break;
        }
    }

    ${UART_INSTANCE_NAME?lower_case}Obj.rdOutIndex = rdOutIndex;

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
        nUnreadBytesAvailable =  (${UART_INSTANCE_NAME?lower_case}Obj.rdBufferSize -  rdOutIndex) + rdInIndex;
    }

    return nUnreadBytesAvailable;
}

size_t ${UART_INSTANCE_NAME}_ReadFreeBufferCountGet(void)
{
    return (${UART_INSTANCE_NAME?lower_case}Obj.rdBufferSize - 1) - ${UART_INSTANCE_NAME}_ReadCountGet();
}

size_t ${UART_INSTANCE_NAME}_ReadBufferSizeGet(void)
{
    return (${UART_INSTANCE_NAME?lower_case}Obj.rdBufferSize - 1);
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
static bool ${UART_INSTANCE_NAME}_TxPullByte(uint16_t* pWrByte)
{
    bool isSuccess = false;
    uint32_t wrOutIndex = ${UART_INSTANCE_NAME?lower_case}Obj.wrOutIndex;
    uint32_t wrInIndex = ${UART_INSTANCE_NAME?lower_case}Obj.wrInIndex;

    if (wrOutIndex != wrInIndex)
    {
        if (${UART_INSTANCE_NAME}_IS_9BIT_MODE_ENABLED())
        {
            *pWrByte = ((uint16_t*)&${UART_INSTANCE_NAME}_WriteBuffer)[wrOutIndex++];
        }
        else
        {
            *pWrByte = ${UART_INSTANCE_NAME}_WriteBuffer[wrOutIndex++];
        }

        if (wrOutIndex >= ${UART_INSTANCE_NAME?lower_case}Obj.wrBufferSize)
        {
            wrOutIndex = 0;
        }

        ${UART_INSTANCE_NAME?lower_case}Obj.wrOutIndex = wrOutIndex;

        isSuccess = true;
    }

    return isSuccess;
}

static inline bool ${UART_INSTANCE_NAME}_TxPushByte(uint16_t wrByte)
{
    uint32_t tempInIndex;
    bool isSuccess = false;

    uint32_t wrOutIndex = ${UART_INSTANCE_NAME?lower_case}Obj.wrOutIndex;
    uint32_t wrInIndex = ${UART_INSTANCE_NAME?lower_case}Obj.wrInIndex;

    tempInIndex = wrInIndex + 1;

    if (tempInIndex >= ${UART_INSTANCE_NAME?lower_case}Obj.wrBufferSize)
    {
        tempInIndex = 0;
    }
    if (tempInIndex != wrOutIndex)
    {
        if (${UART_INSTANCE_NAME}_IS_9BIT_MODE_ENABLED())
        {
            ((uint16_t*)&${UART_INSTANCE_NAME}_WriteBuffer)[wrInIndex] = wrByte;
        }
        else
        {
            ${UART_INSTANCE_NAME}_WriteBuffer[wrInIndex] = (uint8_t)wrByte;
        }

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
        nPendingTxBytes =  (${UART_INSTANCE_NAME?lower_case}Obj.wrBufferSize -  wrOutIndex) + wrInIndex;
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

    while (nBytesWritten < size)
    {
        if (${UART_INSTANCE_NAME}_IS_9BIT_MODE_ENABLED())
        {
            if (${UART_INSTANCE_NAME}_TxPushByte(((uint16_t*)pWrBuffer)[nBytesWritten]) == true)
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
    return (${UART_INSTANCE_NAME?lower_case}Obj.wrBufferSize - 1) - ${UART_INSTANCE_NAME}_WriteCountGet();
}

size_t ${UART_INSTANCE_NAME}_WriteBufferSizeGet(void)
{
    return (${UART_INSTANCE_NAME?lower_case}Obj.wrBufferSize - 1);
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
    UART_ERROR errors = ${UART_INSTANCE_NAME?lower_case}Obj.errors;

    ${UART_INSTANCE_NAME?lower_case}Obj.errors = UART_ERROR_NONE;

    /* All errors are cleared, but send the previous error state */
    return errors;
}

bool ${UART_INSTANCE_NAME}_AutoBaudQuery( void )
{
    if(U${UART_INSTANCE_NUM}MODE & _U${UART_INSTANCE_NUM}MODE_ABAUD_MASK)
        return true;
    else
        return false;
}

void ${UART_INSTANCE_NAME}_AutoBaudSet( bool enable )
{
    if( enable == true )
    {
        U${UART_INSTANCE_NUM}MODESET = _U${UART_INSTANCE_NUM}MODE_ABAUD_MASK;
    }

    /* Turning off ABAUD if it was on can lead to unpredictable behavior, so that
       direction of control is not allowed in this function.                      */
}

<#if UART_INTERRUPT_COUNT == 1>
static void ${UART_INSTANCE_NAME}_FAULT_InterruptHandler (void)
<#else>
void ${UART_INSTANCE_NAME}_FAULT_InterruptHandler (void)
</#if>
{
    /* Save the error to be reported later */
    ${UART_INSTANCE_NAME?lower_case}Obj.errors = (UART_ERROR)(U${UART_INSTANCE_NUM}STA & (_U${UART_INSTANCE_NUM}STA_OERR_MASK | _U${UART_INSTANCE_NUM}STA_FERR_MASK | _U${UART_INSTANCE_NUM}STA_PERR_MASK));

    ${UART_INSTANCE_NAME}_ErrorClear();

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
<#if (core.PRODUCT_FAMILY == "PIC32MX1402") || (core.PRODUCT_FAMILY == "PIC32MZW")>
    /* Clear ${UART_INSTANCE_NAME} RX Interrupt flag */
    ${UART_RX_IFS_REG}CLR = _${UART_RX_IFS_REG}_U${UART_INSTANCE_NUM}RXIF_MASK;

    /* Keep reading until there is a character availabe in the RX FIFO */
    while((U${UART_INSTANCE_NUM}STA & _U${UART_INSTANCE_NUM}STA_URXDA_MASK) == _U${UART_INSTANCE_NUM}STA_URXDA_MASK)
    {
        if (${UART_INSTANCE_NAME}_RxPushByte(  (uint16_t )(U${UART_INSTANCE_NUM}RXREG) ) == true)
        {
            ${UART_INSTANCE_NAME}_ReadNotificationSend();
        }
        else
        {
            /* UART RX buffer is full */
        }
    }
<#else>
    /* Keep reading until there is a character availabe in the RX FIFO */
    while((U${UART_INSTANCE_NUM}STA & _U${UART_INSTANCE_NUM}STA_URXDA_MASK) == _U${UART_INSTANCE_NUM}STA_URXDA_MASK)
    {
        if (${UART_INSTANCE_NAME}_RxPushByte(  (uint16_t )(U${UART_INSTANCE_NUM}RXREG) ) == true)
        {
            ${UART_INSTANCE_NAME}_ReadNotificationSend();
        }
        else
        {
            /* UART RX buffer is full */
        }
    }

    /* Clear ${UART_INSTANCE_NAME} RX Interrupt flag */
    ${UART_RX_IFS_REG}CLR = _${UART_RX_IFS_REG}_U${UART_INSTANCE_NUM}RXIF_MASK;
</#if>
}

<#if UART_INTERRUPT_COUNT == 1>
static void ${UART_INSTANCE_NAME}_TX_InterruptHandler (void)
<#else>
void ${UART_INSTANCE_NAME}_TX_InterruptHandler (void)
</#if>
{
    uint16_t wrByte;

    /* Check if any data is pending for transmission */
    if (${UART_INSTANCE_NAME}_WritePendingBytesGet() > 0)
    {
<#if (core.PRODUCT_FAMILY == "PIC32MX1402") || (core.PRODUCT_FAMILY == "PIC32MZW")>
        /* Clear ${UART_INSTANCE_NAME}TX Interrupt flag */
        ${UART_TX_IFS_REG}CLR = _${UART_TX_IFS_REG}_U${UART_INSTANCE_NUM}TXIF_MASK;

        /* Keep writing to the TX FIFO as long as there is space */
        while(!(U${UART_INSTANCE_NUM}STA & _U${UART_INSTANCE_NUM}STA_UTXBF_MASK))
        {
            if (${UART_INSTANCE_NAME}_TxPullByte(&wrByte) == true)
            {
                if (${UART_INSTANCE_NAME}_IS_9BIT_MODE_ENABLED())
                {
                    U${UART_INSTANCE_NUM}TXREG = wrByte;
                }
                else
                {
                    U${UART_INSTANCE_NUM}TXREG = (uint8_t)wrByte;
                }

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
<#else>
        /* Keep writing to the TX FIFO as long as there is space */
        while(!(U${UART_INSTANCE_NUM}STA & _U${UART_INSTANCE_NUM}STA_UTXBF_MASK))
        {
            if (${UART_INSTANCE_NAME}_TxPullByte(&wrByte) == true)
            {
                if (${UART_INSTANCE_NAME}_IS_9BIT_MODE_ENABLED())
                {
                    U${UART_INSTANCE_NUM}TXREG = wrByte;
                }
                else
                {
                    U${UART_INSTANCE_NUM}TXREG = (uint8_t)wrByte;
                }

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

        /* Clear ${UART_INSTANCE_NAME}TX Interrupt flag */
        ${UART_TX_IFS_REG}CLR = _${UART_TX_IFS_REG}_U${UART_INSTANCE_NUM}TXIF_MASK;

</#if>
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
    /* Call Error handler if Error interrupt flag is set */
    if ((${UART_FAULT_IFS_REG} & _${UART_FAULT_IFS_REG}_U${UART_INSTANCE_NUM}EIF_MASK) && (${UART_FAULT_IEC_REG} & _${UART_FAULT_IEC_REG}_U${UART_INSTANCE_NUM}EIE_MASK))
    {
        ${UART_INSTANCE_NAME}_FAULT_InterruptHandler();
    }
    /* Call RX handler if RX interrupt flag is set */
    if ((${UART_RX_IFS_REG} & _${UART_RX_IFS_REG}_U${UART_INSTANCE_NUM}RXIF_MASK) && (${UART_RX_IEC_REG} & _${UART_RX_IEC_REG}_U${UART_INSTANCE_NUM}RXIE_MASK))
    {
        ${UART_INSTANCE_NAME}_RX_InterruptHandler();
    }
    /* Call TX handler if TX interrupt flag is set */
    if ((${UART_TX_IFS_REG} & _${UART_TX_IFS_REG}_U${UART_INSTANCE_NUM}TXIF_MASK) && (${UART_TX_IEC_REG} & _${UART_TX_IEC_REG}_U${UART_INSTANCE_NUM}TXIE_MASK))
    {
        ${UART_INSTANCE_NAME}_TX_InterruptHandler();
    }

}
</#if>