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
#include "../ecia/plib_ecia.h"

<#--Implementation-->
// *****************************************************************************
// *****************************************************************************
// Section: ${UART_INSTANCE_NAME} Implementation
// *****************************************************************************
// *****************************************************************************

static UART_RING_BUFFER_OBJECT ${UART_INSTANCE_NAME?lower_case}Obj;

#define ${UART_INSTANCE_NAME}_READ_BUFFER_SIZE      ${UART_RX_RING_BUFFER_SIZE}
#define ${UART_INSTANCE_NAME}_RX_INT_DISABLE()      UART${UART_INSTANCE_NUM}_REGS->DATA.UART_IEN &= ~(UART_DATA_IEN_ERDAI_Msk | UART_DATA_IEN_ELSI_Msk)
#define ${UART_INSTANCE_NAME}_RX_INT_ENABLE()       UART${UART_INSTANCE_NUM}_REGS->DATA.UART_IEN |= (UART_DATA_IEN_ERDAI_Msk | UART_DATA_IEN_ELSI_Msk)

static uint8_t ${UART_INSTANCE_NAME}_ReadBuffer[${UART_INSTANCE_NAME}_READ_BUFFER_SIZE];

#define ${UART_INSTANCE_NAME}_WRITE_BUFFER_SIZE     ${UART_TX_RING_BUFFER_SIZE}
#define ${UART_INSTANCE_NAME}_TX_INT_DISABLE()      UART${UART_INSTANCE_NUM}_REGS->DATA.UART_IEN &= ~(UART_DATA_IEN_ETHREI_Msk)
#define ${UART_INSTANCE_NAME}_TX_INT_ENABLE()       UART${UART_INSTANCE_NUM}_REGS->DATA.UART_IEN |= (UART_DATA_IEN_ETHREI_Msk)

static uint8_t ${UART_INSTANCE_NAME}_WriteBuffer[${UART_INSTANCE_NAME}_WRITE_BUFFER_SIZE];

void ${UART_INSTANCE_NAME}_Initialize( void )
{
    <#if UART_REG_CONFIG_SEL != "0">
    UART${UART_INSTANCE_NUM}_REGS->DATA.UART_CFG_SEL = 0x${UART_REG_CONFIG_SEL};
    </#if>
    /* Set DLAB = 1 */
    UART${UART_INSTANCE_NUM}_REGS->DATA.UART_LCR |= UART_DATA_LCR_DLAB_Msk;
    UART${UART_INSTANCE_NUM}_REGS->DLAB.UART_BAUDRT_MSB = 0x${UART_REG_BAUD_GEN_MSB};
    UART${UART_INSTANCE_NUM}_REGS->DLAB.UART_BAUDRT_LSB = 0x${UART_REG_BAUD_GEN_LSB};
    /* Set DLAB = 0 */
    UART${UART_INSTANCE_NUM}_REGS->DATA.UART_LCR &= ~UART_DATA_LCR_DLAB_Msk;
    UART${UART_INSTANCE_NUM}_REGS->DATA.UART_LCR = 0x${UART_REG_LCR};
    UART${UART_INSTANCE_NUM}_REGS->DATA.UART_MCR = UART_DATA_MCR_OUT2_Msk;

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

    ${UART_INSTANCE_NAME?lower_case}Obj.rdBufferSize = ${UART_INSTANCE_NAME}_READ_BUFFER_SIZE;
    ${UART_INSTANCE_NAME?lower_case}Obj.wrBufferSize = ${UART_INSTANCE_NAME}_WRITE_BUFFER_SIZE;


    /* Turn ON ${UART_INSTANCE_NAME} */
    UART${UART_INSTANCE_NUM}_REGS->DATA.UART_ACTIVATE = 0x01;

    ${UART_INSTANCE_NAME}_RX_INT_ENABLE();
}

bool ${UART_INSTANCE_NAME}_SerialSetup( UART_SERIAL_SETUP *setup, uint32_t srcClkFreq )
{
    bool status = false;
    uint32_t baud;
    uint32_t baud_clk_src = 1843200;
    uint32_t baud_div;

    if (setup != NULL)
    {
        baud = setup->baudRate;

        /* Set DLAB = 1 */
        UART${UART_INSTANCE_NUM}_REGS->DATA.UART_LCR |= UART_DATA_LCR_DLAB_Msk;

        if ((UART${UART_INSTANCE_NUM}_REGS->DLAB.UART_BAUDRT_MSB & 0x80) != 0)
        {
            baud_clk_src = 48000000;
        }
        
        baud_div = (baud_clk_src >> 4)/baud;
        
        if ((baud_div < 1U) || (baud_div > 32767U))
        {
            /* Set DLAB = 0 */
            UART${UART_INSTANCE_NUM}_REGS->DATA.UART_LCR &= ~UART_DATA_LCR_DLAB_Msk;

            return status;
        }

        UART${UART_INSTANCE_NUM}_REGS->DLAB.UART_BAUDRT_LSB = (uint8_t)baud_div;
        UART${UART_INSTANCE_NUM}_REGS->DLAB.UART_BAUDRT_MSB |= (uint8_t)((baud_div & 0x7F00U) >> 8U);

        /* Set DLAB = 0 */
        UART${UART_INSTANCE_NUM}_REGS->DATA.UART_LCR &= ~UART_DATA_LCR_DLAB_Msk;
        
        UART${UART_INSTANCE_NUM}_REGS->DATA.UART_LCR = (UART${UART_INSTANCE_NUM}_REGS->DATA.UART_LCR & ~(UART_DATA_LCR_PAR_SEL_Msk | UART_DATA_LCR_STOP_BITS_Msk | UART_DATA_LCR_WORD_LEN_Msk)) | ((uint8_t)setup->parity | (uint8_t)setup->stopBits | (uint8_t)setup->dataWidth);

        if (setup->parity == UART_PARITY_NONE)
        {
            UART${UART_INSTANCE_NUM}_REGS->DATA.UART_LCR &= ~UART_DATA_LCR_EN_PAR_Msk;
        }
        else
        {
            UART${UART_INSTANCE_NUM}_REGS->DATA.UART_LCR |= UART_DATA_LCR_EN_PAR_Msk;
        }

        status = true;
    }

    return status;
}

/* This routine is only called from ISR. Hence do not disable/enable USART interrupts. */
static inline bool ${UART_INSTANCE_NAME}_RxPushByte(uint8_t rdByte)
{
    uint32_t tempInIndex;
    bool isSuccess = false;

    tempInIndex = ${UART_INSTANCE_NAME?lower_case}Obj.rdInIndex + 1U;

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
            tempInIndex = ${UART_INSTANCE_NAME?lower_case}Obj.rdInIndex + 1U;

            if (tempInIndex >= ${UART_INSTANCE_NAME?lower_case}Obj.rdBufferSize)
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
    uint32_t rdOutIndex = 0;
    uint32_t rdInIndex = 0;

    /* Take a snapshot of indices to avoid creation of critical section */
    rdOutIndex = ${UART_INSTANCE_NAME?lower_case}Obj.rdOutIndex;
    rdInIndex = ${UART_INSTANCE_NAME?lower_case}Obj.rdInIndex;

    while (nBytesRead < size)
    {
        if (rdOutIndex != rdInIndex)
        {
            pRdBuffer[nBytesRead] = ${UART_INSTANCE_NAME}_ReadBuffer[rdOutIndex];
            nBytesRead++;
            rdOutIndex++;

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
static bool ${UART_INSTANCE_NAME}_TxPullByte(uint8_t* pWrByte)
{
    bool isSuccess = false;
    uint32_t wrOutIndex = ${UART_INSTANCE_NAME?lower_case}Obj.wrOutIndex;
    uint32_t wrInIndex = ${UART_INSTANCE_NAME?lower_case}Obj.wrInIndex;

    if (wrOutIndex != wrInIndex)
    {
        *pWrByte = ${UART_INSTANCE_NAME}_WriteBuffer[wrOutIndex];
        wrOutIndex++;

        if (wrOutIndex >= ${UART_INSTANCE_NAME?lower_case}Obj.wrBufferSize)
        {
            wrOutIndex = 0;
        }

        ${UART_INSTANCE_NAME?lower_case}Obj.wrOutIndex = wrOutIndex;

        isSuccess = true;
    }

    return isSuccess;
}

static inline bool ${UART_INSTANCE_NAME}_TxPushByte(uint8_t wrByte)
{
    uint32_t tempInIndex;
    bool isSuccess = false;

    uint32_t wrOutIndex = ${UART_INSTANCE_NAME?lower_case}Obj.wrOutIndex;
    uint32_t wrInIndex = ${UART_INSTANCE_NAME?lower_case}Obj.wrInIndex;

    tempInIndex = wrInIndex + 1U;

    if (tempInIndex >= ${UART_INSTANCE_NAME?lower_case}Obj.wrBufferSize)
    {
        tempInIndex = 0;
    }
    if (tempInIndex != wrOutIndex)
    {
        ${UART_INSTANCE_NAME}_WriteBuffer[wrInIndex] = wrByte;

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

bool ${UART_INSTANCE_NAME}_TransmitComplete( void )
{    
    bool transmitComplete = false;

    if ((UART${UART_INSTANCE_NUM}_REGS->DATA.UART_LSR & UART_DATA_LSR_TRANS_ERR_Msk) != 0)
    {
        transmitComplete = true;
    }

    return transmitComplete;
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

static void ${UART_INSTANCE_NAME}_ERROR_InterruptHandler (void)
{
    uint8_t lsr;

    lsr = UART${UART_INSTANCE_NUM}_REGS->DATA.UART_LSR;

    /* Check for overrun, parity and framing errors */
    ${UART_INSTANCE_NAME?lower_case}Obj.errors = (lsr & (UART_DATA_LSR_OVERRUN_Msk | UART_DATA_LSR_PE_Msk | UART_DATA_LSR_FRAME_ERR_Msk));
    
    /* Client must call UARTx_ErrorGet() function to clear the errors */
    if( ${UART_INSTANCE_NAME?lower_case}Obj.rdCallback != NULL )
    {
        ${UART_INSTANCE_NAME?lower_case}Obj.rdCallback(UART_EVENT_READ_ERROR, ${UART_INSTANCE_NAME?lower_case}Obj.rdContext);
    }
}

static void ${UART_INSTANCE_NAME}_RX_InterruptHandler (void)
{
    if (${UART_INSTANCE_NAME}_RxPushByte( UART${UART_INSTANCE_NUM}_REGS->DATA.UART_RX_DAT ) == true)
    {
        ${UART_INSTANCE_NAME}_ReadNotificationSend();
    }
    else
    {
        /* UART RX buffer is full */
    }
}

static void ${UART_INSTANCE_NAME}_TX_InterruptHandler (void)
{
    uint8_t wrByte;

    if (${UART_INSTANCE_NAME}_TxPullByte(&wrByte) == true)
    {
        UART${UART_INSTANCE_NUM}_REGS->DATA.UART_TX_DAT = wrByte;

        /* Send notification */
        ${UART_INSTANCE_NAME}_WriteNotificationSend();
    }
    else
    {
        /* Nothing to transmit. Disable the data register empty interrupt. */
        ${UART_INSTANCE_NAME}_TX_INT_DISABLE();
    }
}

void ${UART_NVIC_INTERRUPT_NAME}_InterruptHandler (void)
{
    uint8_t int_id = 0;

    int_id = ((UART${UART_INSTANCE_NUM}_REGS->DLAB.UART_INT_ID & UART_DLAB_INT_ID_INTID_Msk) >> UART_DLAB_INT_ID_INTID_Pos);

    <#if UART_INTERRUPT_TYPE == "AGGREGATE">
    ECIA_GIRQSourceClear(ECIA_AGG_INT_SRC_UART${UART_INSTANCE_NUM});
    <#else>
    ECIA_GIRQSourceClear(ECIA_DIR_INT_SRC_UART${UART_INSTANCE_NUM});
    </#if>

    /* Interrupt type is Receiver Line Status */
    if (int_id == 0x03U)
    {
        ${UART_INSTANCE_NAME}_ERROR_InterruptHandler();
    }
    /* Interrupt type is Received data available */
    else if (int_id == 0x02U)
    {
        ${UART_INSTANCE_NAME}_RX_InterruptHandler();
    }
    /* Interrupt type is Transmit holding register empty */
    else if (int_id == 0x01U)
    {
        ${UART_INSTANCE_NAME}_TX_InterruptHandler();
    }
    else
    {
        /* Do nothing */
    }
}
