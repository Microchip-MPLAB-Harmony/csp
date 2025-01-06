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
<#if core.CoreSysIntFile == true>
#include "interrupts.h"
</#if>

<#--Implementation-->
// *****************************************************************************
// *****************************************************************************
// Section: ${UART_INSTANCE_NAME} Implementation
// *****************************************************************************
// *****************************************************************************

static volatile UART_RING_BUFFER_OBJECT ${UART_INSTANCE_NAME?lower_case}Obj;

#define ${UART_INSTANCE_NAME}_READ_BUFFER_SIZE      (${UART_RX_RING_BUFFER_SIZE}U)
#define ${UART_INSTANCE_NAME}_READ_BUFFER_SIZE_9BIT (${UART_RX_RING_BUFFER_SIZE}U >> 1)
#define ${UART_INSTANCE_NAME}_RX_INT_DISABLE()      ${UART_RX_IEC_REG}CLR = _${UART_RX_IEC_REG}_U${UART_INSTANCE_NUM}RXIE_MASK;
#define ${UART_INSTANCE_NAME}_RX_INT_ENABLE()       ${UART_RX_IEC_REG}SET = _${UART_RX_IEC_REG}_U${UART_INSTANCE_NUM}RXIE_MASK;

static volatile uint8_t ${UART_INSTANCE_NAME}_ReadBuffer[${UART_INSTANCE_NAME}_READ_BUFFER_SIZE];

#define ${UART_INSTANCE_NAME}_WRITE_BUFFER_SIZE      (${UART_TX_RING_BUFFER_SIZE}U)
#define ${UART_INSTANCE_NAME}_WRITE_BUFFER_SIZE_9BIT (${UART_TX_RING_BUFFER_SIZE}U >> 1)
#define ${UART_INSTANCE_NAME}_TX_INT_DISABLE()       ${UART_TX_IEC_REG}CLR = _${UART_TX_IEC_REG}_U${UART_INSTANCE_NUM}TXIE_MASK;
#define ${UART_INSTANCE_NAME}_TX_INT_ENABLE()        ${UART_TX_IEC_REG}SET = _${UART_TX_IEC_REG}_U${UART_INSTANCE_NUM}TXIE_MASK;

static volatile uint8_t ${UART_INSTANCE_NAME}_WriteBuffer[${UART_INSTANCE_NAME}_WRITE_BUFFER_SIZE];

#define ${UART_INSTANCE_NAME}_IS_9BIT_MODE_ENABLED()    ( (U${UART_INSTANCE_NUM}MODE) & (_U${UART_INSTANCE_NUM}MODE_PDSEL0_MASK | _U${UART_INSTANCE_NUM}MODE_PDSEL1_MASK)) == (_U${UART_INSTANCE_NUM}MODE_PDSEL0_MASK | _U${UART_INSTANCE_NUM}MODE_PDSEL1_MASK) ? true:false

static void ${UART_INSTANCE_NAME}_ErrorClear( void )
{
    UART_ERROR errors = UART_ERROR_NONE;
    uint8_t dummyData = 0u;

    errors = (UART_ERROR)(U${UART_INSTANCE_NUM}STA & (_U${UART_INSTANCE_NUM}STA_OERR_MASK | _U${UART_INSTANCE_NUM}STA_FERR_MASK | _U${UART_INSTANCE_NUM}STA_PERR_MASK));

    if(errors != UART_ERROR_NONE)
    {
        /* If it's a overrun error then clear it to flush FIFO */
        if((U${UART_INSTANCE_NUM}STA & _U${UART_INSTANCE_NUM}STA_OERR_MASK) != 0U)
        {
            U${UART_INSTANCE_NUM}STACLR = _U${UART_INSTANCE_NUM}STA_OERR_MASK;
        }

        /* Read existing error bytes from FIFO to clear parity and framing error flags */
        while((U${UART_INSTANCE_NUM}STA & _U${UART_INSTANCE_NUM}STA_URXDA_MASK) != 0U)
        {
            dummyData = (uint8_t)U${UART_INSTANCE_NUM}RXREG;
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
    U${UART_INSTANCE_NUM}STASET = (_U${UART_INSTANCE_NUM}STA_UTXEN_MASK | _U${UART_INSTANCE_NUM}STA_URXEN_MASK | _U${UART_INSTANCE_NUM}STA_UTXISEL1_MASK <#if UART_AUTOMATIC_ADDR_DETECTION_ENABLE == true> | _U${UART_INSTANCE_NUM}STA_ADDEN_MASK | (0x${UART_9BIT_MODE_ADDR}UL << _U${UART_INSTANCE_NUM}STA_ADDR_POSITION) | (0x${UART_9BIT_MODE_ADDR_MASK}UL << _U${UART_INSTANCE_NUM}STA_MASK_POSITION) </#if>);

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
    uint32_t status_ctrl;
    uint32_t uxbrg = 0;

    if (setup != NULL)
    {
        baud = setup->baudRate;

        if ((baud == 0U) || ((setup->dataWidth == UART_DATA_9_BIT) && (setup->parity != UART_PARITY_NONE)))
        {
            return status;
        }

        if(srcClkFreq == 0U)
        {
            srcClkFreq = ${UART_INSTANCE_NAME}_FrequencyGet();
        }

        /* Calculate BRG value */
<#if UART_BRGH?number == 0>
        uxbrg = (((srcClkFreq >> 4) + (baud >> 1)) / baud);
<#else>
        uxbrg = (((srcClkFreq >> 2) + (baud >> 1)) / baud);
</#if>

        /* Check if the baud value can be set with low baud settings */
        if (uxbrg < 1U)
        {
            return status;
        }

        uxbrg -= 1U;

        if (uxbrg > UINT16_MAX)
        {
            return status;
        }

        /* Turn OFF ${UART_INSTANCE_NAME}. Save UTXEN, URXEN and UTXBRK bits as these are cleared upon disabling UART */

        status_ctrl = U${UART_INSTANCE_NUM}STA & (_U${UART_INSTANCE_NUM}STA_UTXEN_MASK | _U${UART_INSTANCE_NUM}STA_URXEN_MASK | _U${UART_INSTANCE_NUM}STA_UTXBRK_MASK);

        U${UART_INSTANCE_NUM}MODECLR = _U${UART_INSTANCE_NUM}MODE_ON_MASK;

        if(setup->dataWidth == UART_DATA_9_BIT)
        {
            /* Configure ${UART_INSTANCE_NAME} mode */
            U${UART_INSTANCE_NUM}MODE = (U${UART_INSTANCE_NUM}MODE & (~_U${UART_INSTANCE_NUM}MODE_PDSEL_MASK)) | setup->dataWidth;
        }
        else
        {
            /* Configure ${UART_INSTANCE_NAME} mode */
            U${UART_INSTANCE_NUM}MODE = (U${UART_INSTANCE_NUM}MODE & (~_U${UART_INSTANCE_NUM}MODE_PDSEL_MASK)) | setup->parity;
        }

        /* Configure ${UART_INSTANCE_NAME} mode */
        U${UART_INSTANCE_NUM}MODE = (U${UART_INSTANCE_NUM}MODE & (~_U${UART_INSTANCE_NUM}MODE_STSEL_MASK)) | setup->stopBits;

        /* Configure ${UART_INSTANCE_NAME} Baud Rate */
        U${UART_INSTANCE_NUM}BRG = uxbrg;

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

        /* Restore UTXEN, URXEN and UTXBRK bits. */
        U${UART_INSTANCE_NUM}STASET = status_ctrl;

        status = true;
    }

    return status;
}

/* This routine is only called from ISR. Hence do not disable/enable USART interrupts. */
static inline bool ${UART_INSTANCE_NAME}_RxPushByte(uint16_t rdByte)
{
    uint32_t tempInIndex;
    bool isSuccess = false;
<#if UART_AUTOMATIC_ADDR_DETECTION_ENABLE == false>
    uint32_t rdInIdx;
</#if>

    tempInIndex = ${UART_INSTANCE_NAME?lower_case}Obj.rdInIndex + 1U;

    if (tempInIndex >= ${UART_INSTANCE_NAME?lower_case}Obj.rdBufferSize)
    {
        tempInIndex = 0U;
    }

    if (tempInIndex == ${UART_INSTANCE_NAME?lower_case}Obj.rdOutIndex)
    {
        /* Queue is full - Report it to the application. Application gets a chance to free up space by reading data out from the RX ring buffer */
        if(${UART_INSTANCE_NAME?lower_case}Obj.rdCallback != NULL)
        {
            uintptr_t rdContext = ${UART_INSTANCE_NAME?lower_case}Obj.rdContext;

            ${UART_INSTANCE_NAME?lower_case}Obj.rdCallback(UART_EVENT_READ_BUFFER_FULL, rdContext);

            /* Read the indices again in case application has freed up space in RX ring buffer */
            tempInIndex = ${UART_INSTANCE_NAME?lower_case}Obj.rdInIndex + 1U;

            if (tempInIndex >= ${UART_INSTANCE_NAME?lower_case}Obj.rdBufferSize)
            {
                tempInIndex = 0U;
            }
        }
    }

    /* Attempt to push the data into the ring buffer */
    if (tempInIndex != ${UART_INSTANCE_NAME?lower_case}Obj.rdOutIndex)
    {
        uint32_t rdInIndex = ${UART_INSTANCE_NAME?lower_case}Obj.rdInIndex;
<#if UART_AUTOMATIC_ADDR_DETECTION_ENABLE == true>
        ${UART_INSTANCE_NAME}_ReadBuffer[rdInIndex] = (uint8_t)rdByte;
<#else>
        if (${UART_INSTANCE_NAME}_IS_9BIT_MODE_ENABLED())
        {
            rdInIdx = ${UART_INSTANCE_NAME?lower_case}Obj.rdInIndex << 1U;
            ${UART_INSTANCE_NAME}_ReadBuffer[rdInIdx] = (uint8_t)rdByte;
            ${UART_INSTANCE_NAME}_ReadBuffer[rdInIdx + 1U] = (uint8_t)(rdByte >> 8U);
        }
        else
        {
            ${UART_INSTANCE_NAME}_ReadBuffer[rdInIndex] = (uint8_t)rdByte;
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
            uintptr_t rdContext = ${UART_INSTANCE_NAME?lower_case}Obj.rdContext;

            if (${UART_INSTANCE_NAME?lower_case}Obj.isRdNotifyPersistently == true)
            {
                if (nUnreadBytesAvailable >= ${UART_INSTANCE_NAME?lower_case}Obj.rdThreshold)
                {
                    ${UART_INSTANCE_NAME?lower_case}Obj.rdCallback(UART_EVENT_READ_THRESHOLD_REACHED, rdContext);
                }
            }
            else
            {
                if (nUnreadBytesAvailable == ${UART_INSTANCE_NAME?lower_case}Obj.rdThreshold)
                {
                    ${UART_INSTANCE_NAME?lower_case}Obj.rdCallback(UART_EVENT_READ_THRESHOLD_REACHED, rdContext);
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
<#if UART_AUTOMATIC_ADDR_DETECTION_ENABLE == false>
    uint32_t rdOut16Idx;
    uint32_t nBytesRead16Idx;
</#if>

    /* Take a snapshot of indices to avoid creation of critical section */
    rdOutIndex = ${UART_INSTANCE_NAME?lower_case}Obj.rdOutIndex;
    rdInIndex = ${UART_INSTANCE_NAME?lower_case}Obj.rdInIndex;

    while (nBytesRead < size)
    {
        if (rdOutIndex != rdInIndex)
        {
<#if UART_AUTOMATIC_ADDR_DETECTION_ENABLE == true>
            pRdBuffer[nBytesRead] = ${UART_INSTANCE_NAME}_ReadBuffer[rdOutIndex];
            nBytesRead++;
            rdOutIndex++;
<#else>
            if (${UART_INSTANCE_NAME}_IS_9BIT_MODE_ENABLED())
            {
                rdOut16Idx = rdOutIndex << 1U;
                nBytesRead16Idx = nBytesRead << 1U;

                pRdBuffer[nBytesRead16Idx] = ${UART_INSTANCE_NAME}_ReadBuffer[rdOut16Idx];
                pRdBuffer[nBytesRead16Idx + 1U] = ${UART_INSTANCE_NAME}_ReadBuffer[rdOut16Idx + 1U];
            }
            else
            {
                pRdBuffer[nBytesRead] = ${UART_INSTANCE_NAME}_ReadBuffer[rdOutIndex];
            }
            nBytesRead++;
            rdOutIndex++;
</#if>

            if (rdOutIndex >= ${UART_INSTANCE_NAME?lower_case}Obj.rdBufferSize)
            {
                rdOutIndex = 0U;
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
    return (${UART_INSTANCE_NAME?lower_case}Obj.rdBufferSize - 1U) - ${UART_INSTANCE_NAME}_ReadCountGet();
}

size_t ${UART_INSTANCE_NAME}_ReadBufferSizeGet(void)
{
    return (${UART_INSTANCE_NAME?lower_case}Obj.rdBufferSize - 1U);
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
    if (nBytesThreshold > 0U)
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
    uint32_t wrOut16Idx;

    if (wrOutIndex != wrInIndex)
    {
        if (${UART_INSTANCE_NAME}_IS_9BIT_MODE_ENABLED())
        {
            wrOut16Idx = wrOutIndex << 1U;
            pWrByte[0] = ${UART_INSTANCE_NAME}_WriteBuffer[wrOut16Idx];
            pWrByte[1] = ${UART_INSTANCE_NAME}_WriteBuffer[wrOut16Idx + 1U];
        }
        else
        {
            *pWrByte = ${UART_INSTANCE_NAME}_WriteBuffer[wrOutIndex];
        }
        wrOutIndex++;

        if (wrOutIndex >= ${UART_INSTANCE_NAME?lower_case}Obj.wrBufferSize)
        {
            wrOutIndex = 0U;
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
    uint32_t wrIn16Idx;

    tempInIndex = wrInIndex + 1U;

    if (tempInIndex >= ${UART_INSTANCE_NAME?lower_case}Obj.wrBufferSize)
    {
        tempInIndex = 0U;
    }
    if (tempInIndex != wrOutIndex)
    {
        if (${UART_INSTANCE_NAME}_IS_9BIT_MODE_ENABLED())
        {
            wrIn16Idx = wrInIndex << 1U;
            ${UART_INSTANCE_NAME}_WriteBuffer[wrIn16Idx] = (uint8_t)wrByte;
            ${UART_INSTANCE_NAME}_WriteBuffer[wrIn16Idx + 1U] = (uint8_t)(wrByte >> 8U);
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
            uintptr_t wrContext = ${UART_INSTANCE_NAME?lower_case}Obj.wrContext;

            if (${UART_INSTANCE_NAME?lower_case}Obj.isWrNotifyPersistently == true)
            {
                if (nFreeWrBufferCount >= ${UART_INSTANCE_NAME?lower_case}Obj.wrThreshold)
                {
                    ${UART_INSTANCE_NAME?lower_case}Obj.wrCallback(UART_EVENT_WRITE_THRESHOLD_REACHED, wrContext);
                }
            }
            else
            {
                if (nFreeWrBufferCount == ${UART_INSTANCE_NAME?lower_case}Obj.wrThreshold)
                {
                    ${UART_INSTANCE_NAME?lower_case}Obj.wrCallback(UART_EVENT_WRITE_THRESHOLD_REACHED, wrContext);
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
    uint16_t halfWordData = 0U;

    while (nBytesWritten < size)
    {
        if (${UART_INSTANCE_NAME}_IS_9BIT_MODE_ENABLED())
        {
            halfWordData = pWrBuffer[(2U * nBytesWritten) + 1U];
            halfWordData <<= 8U;
            halfWordData |= pWrBuffer[(2U * nBytesWritten)];
            if (${UART_INSTANCE_NAME}_TxPushByte(halfWordData) == true)
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
    if (${UART_INSTANCE_NAME}_WritePendingBytesGet() > 0U)
    {
        /* Enable TX interrupt as data is pending for transmission */
        ${UART_INSTANCE_NAME}_TX_INT_ENABLE();
    }

    return nBytesWritten;
}

size_t ${UART_INSTANCE_NAME}_WriteFreeBufferCountGet(void)
{
    return (${UART_INSTANCE_NAME?lower_case}Obj.wrBufferSize - 1U) - ${UART_INSTANCE_NAME}_WriteCountGet();
}

size_t ${UART_INSTANCE_NAME}_WriteBufferSizeGet(void)
{
    return (${UART_INSTANCE_NAME?lower_case}Obj.wrBufferSize - 1U);
}

bool ${UART_INSTANCE_NAME}_TransmitComplete(void)
{
    bool status = false;

    if((U${UART_INSTANCE_NUM}STA & _U${UART_INSTANCE_NUM}STA_TRMT_MASK) != 0U)
    {
        status = true;
    }
    return status;
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
    if (nBytesThreshold > 0U)
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
    bool autobaudcheck = false;

    if((U${UART_INSTANCE_NUM}MODE & _U${UART_INSTANCE_NUM}MODE_ABAUD_MASK) != 0U)
    {

        autobaudcheck = true;

    }
    return autobaudcheck;
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
static void __attribute__((used)) ${UART_INSTANCE_NAME}_FAULT_InterruptHandler (void)
<#else>
void __attribute__((used)) ${UART_INSTANCE_NAME}${UART_ERROR_NAME}_InterruptHandler (void)
</#if>
{
    /* Save the error to be reported later */
    ${UART_INSTANCE_NAME?lower_case}Obj.errors = (UART_ERROR)(U${UART_INSTANCE_NUM}STA & (_U${UART_INSTANCE_NUM}STA_OERR_MASK | _U${UART_INSTANCE_NUM}STA_FERR_MASK | _U${UART_INSTANCE_NUM}STA_PERR_MASK));

    ${UART_INSTANCE_NAME}_ErrorClear();

    /* Client must call UARTx_ErrorGet() function to clear the errors */
    if( ${UART_INSTANCE_NAME?lower_case}Obj.rdCallback != NULL )
    {
        uintptr_t rdContext = ${UART_INSTANCE_NAME?lower_case}Obj.rdContext;

        ${UART_INSTANCE_NAME?lower_case}Obj.rdCallback(UART_EVENT_READ_ERROR, rdContext);
    }
}

<#if UART_INTERRUPT_COUNT == 1>
static void __attribute__((used)) ${UART_INSTANCE_NAME}_RX_InterruptHandler (void)
<#else>
void __attribute__((used)) ${UART_INSTANCE_NAME}_RX_InterruptHandler (void)
</#if>
{
<#if (core.PRODUCT_FAMILY == "PIC32MK1402") || (core.PRODUCT_FAMILY == "PIC32MZW")>
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
static void __attribute__((used)) ${UART_INSTANCE_NAME}_TX_InterruptHandler (void)
<#else>
void __attribute__((used)) ${UART_INSTANCE_NAME}_TX_InterruptHandler (void)
</#if>
{
    uint16_t wrByte;

    /* Check if any data is pending for transmission */
    if (${UART_INSTANCE_NAME}_WritePendingBytesGet() > 0U)
    {
<#if (core.PRODUCT_FAMILY == "PIC32MK1402") || (core.PRODUCT_FAMILY == "PIC32MZW")>
        /* Clear ${UART_INSTANCE_NAME}TX Interrupt flag */
        ${UART_TX_IFS_REG}CLR = _${UART_TX_IFS_REG}_U${UART_INSTANCE_NUM}TXIF_MASK;

        /* Keep writing to the TX FIFO as long as there is space */
        while((U${UART_INSTANCE_NUM}STA & _U${UART_INSTANCE_NUM}STA_UTXBF_MASK) == 0U)
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
        while((U${UART_INSTANCE_NUM}STA & _U${UART_INSTANCE_NUM}STA_UTXBF_MASK) == 0U)
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
void __attribute__((used)) UART_${UART_INSTANCE_NUM}_InterruptHandler (void)
{
    uint32_t temp = ${UART_FAULT_IEC_REG};
    /* Call Error handler if Error interrupt flag is set */
    if (((${UART_FAULT_IFS_REG} & _${UART_FAULT_IFS_REG}_U${UART_INSTANCE_NUM}EIF_MASK) != 0U) && ((temp & _${UART_FAULT_IEC_REG}_U${UART_INSTANCE_NUM}EIE_MASK) != 0U))
    {
        ${UART_INSTANCE_NAME}_FAULT_InterruptHandler();
    }
    temp = ${UART_RX_IEC_REG};
    /* Call RX handler if RX interrupt flag is set */
    if (((${UART_RX_IFS_REG} & _${UART_RX_IFS_REG}_U${UART_INSTANCE_NUM}RXIF_MASK) != 0U) && ((temp & _${UART_RX_IEC_REG}_U${UART_INSTANCE_NUM}RXIE_MASK) != 0U))
    {
        ${UART_INSTANCE_NAME}_RX_InterruptHandler();
    }
    temp = ${UART_TX_IEC_REG};
    /* Call TX handler if TX interrupt flag is set */
    if (((${UART_TX_IFS_REG} & _${UART_TX_IFS_REG}_U${UART_INSTANCE_NUM}TXIF_MASK) != 0U) && ((temp & _${UART_TX_IEC_REG}_U${UART_INSTANCE_NUM}TXIE_MASK) != 0U))
    {
        ${UART_INSTANCE_NAME}_TX_InterruptHandler();
    }

}
</#if>