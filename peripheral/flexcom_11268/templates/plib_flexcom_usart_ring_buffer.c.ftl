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
<#if core.CoreSysIntFile == true>
#include "interrupts.h"
</#if>

#define FLEXCOM_USART_RHR_8BIT_REG      (*(volatile uint8_t* const)((${FLEXCOM_INSTANCE_NAME}_BASE_ADDRESS + FLEX_US_RHR_REG_OFST)))
#define FLEXCOM_USART_RHR_9BIT_REG      (*(volatile uint16_t* const)((${FLEXCOM_INSTANCE_NAME}_BASE_ADDRESS + FLEX_US_RHR_REG_OFST)))

#define FLEXCOM_USART_THR_8BIT_REG      (*(volatile uint8_t* const)((${FLEXCOM_INSTANCE_NAME}_BASE_ADDRESS + FLEX_US_THR_REG_OFST)))
#define FLEXCOM_USART_THR_9BIT_REG      (*(volatile uint16_t* const)((${FLEXCOM_INSTANCE_NAME}_BASE_ADDRESS + FLEX_US_THR_REG_OFST)))
<#if FLEXCOM_USART_FIFO_ENABLE == false>

/* Disable Read, Overrun, Parity and Framing error interrupts */
#define ${FLEXCOM_INSTANCE_NAME}_USART_RX_INT_DISABLE()      ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_IDR = (FLEX_US_IDR_RXRDY_Msk | FLEX_US_IDR_FRAME_Msk | FLEX_US_IDR_PARE_Msk | FLEX_US_IDR_OVRE_Msk)

/* Enable Read, Overrun, Parity and Framing error interrupts */
#define ${FLEXCOM_INSTANCE_NAME}_USART_RX_INT_ENABLE()       ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_IER = (FLEX_US_IER_RXRDY_Msk | FLEX_US_IER_FRAME_Msk | FLEX_US_IER_PARE_Msk | FLEX_US_IER_OVRE_Msk)

#define ${FLEXCOM_INSTANCE_NAME}_USART_TX_INT_DISABLE()      ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_IDR = FLEX_US_IDR_TXRDY_Msk
#define ${FLEXCOM_INSTANCE_NAME}_USART_TX_INT_ENABLE()       ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_IER = FLEX_US_IER_TXRDY_Msk

<#else>

#define ${FLEXCOM_INSTANCE_NAME}_USART_HW_RX_FIFO_THRES                 ${FLEXCOM_USART_RX_FIFO_THRESHOLD}U
#define ${FLEXCOM_INSTANCE_NAME}_USART_HW_TX_FIFO_THRES                 ${FLEXCOM_USART_TX_FIFO_THRESHOLD}U

/* Disable Read, Overrun, Parity and Framing error interrupts */
#define ${FLEXCOM_INSTANCE_NAME}_USART_RX_INT_DISABLE()      do { \
${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_IDR = (FLEX_US_IDR_FRAME_Msk | FLEX_US_IDR_PARE_Msk | FLEX_US_IDR_OVRE_Msk); \
${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_FIDR = FLEX_US_FIDR_RXFTHF_Msk; \
}while(false)

/* Enable Read, Overrun, Parity and Framing error interrupts */
#define ${FLEXCOM_INSTANCE_NAME}_USART_RX_INT_ENABLE()       do { \
${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_IER = (FLEX_US_IER_FRAME_Msk | FLEX_US_IER_PARE_Msk | FLEX_US_IER_OVRE_Msk); \
${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_FIER = FLEX_US_FIER_RXFTHF_Msk; \
}while(false)

#define ${FLEXCOM_INSTANCE_NAME}_USART_TX_INT_DISABLE()      do { \
${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_IDR = FLEX_US_IDR_TXRDY_Msk; \
${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_FIDR = (FLEX_US_FIDR_TXFTHF_Msk); \
}while(false)

#define ${FLEXCOM_INSTANCE_NAME}_USART_TX_INT_ENABLE()       do { \
${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_IER = FLEX_US_IER_TXRDY_Msk; \
${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_FIER = (FLEX_US_FIER_TXFTHF_Msk); \
}while(false)

</#if>
#define ${FLEXCOM_INSTANCE_NAME}_USART_READ_BUFFER_SIZE             ${USART_RX_RING_BUFFER_SIZE}U
#define ${FLEXCOM_INSTANCE_NAME}_USART_9BIT_READ_BUFFER_SIZE        (${USART_RX_RING_BUFFER_SIZE}U >> 1U)

#define ${FLEXCOM_INSTANCE_NAME}_USART_WRITE_BUFFER_SIZE            ${USART_TX_RING_BUFFER_SIZE}U
#define ${FLEXCOM_INSTANCE_NAME}_USART_9BIT_WRITE_BUFFER_SIZE       (${USART_TX_RING_BUFFER_SIZE}U >> 1U)

static uint8_t ${FLEXCOM_INSTANCE_NAME}_USART_ReadBuffer[${FLEXCOM_INSTANCE_NAME}_USART_READ_BUFFER_SIZE];
static uint8_t ${FLEXCOM_INSTANCE_NAME}_USART_WriteBuffer[${FLEXCOM_INSTANCE_NAME}_USART_WRITE_BUFFER_SIZE];

// *****************************************************************************
// *****************************************************************************
// Section: ${FLEXCOM_INSTANCE_NAME} ${FLEXCOM_MODE} Ring Buffer Implementation
// *****************************************************************************
// *****************************************************************************

static FLEXCOM_USART_RING_BUFFER_OBJECT ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj;

void ${FLEXCOM_INSTANCE_NAME}_USART_Initialize( void )
{
    /* Set FLEXCOM USART operating mode */
    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_MR = FLEX_MR_OPMODE_USART;

    /* Reset ${FLEXCOM_INSTANCE_NAME} USART */
    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_CR = (FLEX_US_CR_RSTRX_Msk | FLEX_US_CR_RSTTX_Msk | FLEX_US_CR_RSTSTA_Msk);

<#if FLEXCOM_USART_FIFO_ENABLE == true>
    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_CR = FLEX_US_CR_FIFOEN_Msk;

    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_FMR = FLEX_US_FMR_RXFTHRES(${FLEXCOM_INSTANCE_NAME}_USART_HW_RX_FIFO_THRES) | FLEX_US_FMR_TXFTHRES(${FLEXCOM_INSTANCE_NAME}_USART_HW_TX_FIFO_THRES)<#if FLEXCOM_USART_MR_USART_MODE == "HW_HANDSHAKING"> | FLEX_US_FMR_FRTSC_Msk </#if>;
</#if>

    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_TTGR = ${FLEXCOM_USART_TTGR};

    /* Enable ${FLEXCOM_INSTANCE_NAME} USART */
    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_CR = (FLEX_US_CR_TXEN_Msk | FLEX_US_CR_RXEN_Msk);

    /* Configure ${FLEXCOM_INSTANCE_NAME} USART mode */
    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_MR = ( FLEX_US_MR_USART_MODE_${FLEXCOM_USART_MR_USART_MODE} | FLEX_US_MR_USCLKS_${FLEXCOM_USART_MR_USCLKS} ${(FLEX_USART_MR_MODE9 == true)?then('| FLEX_US_MR_MODE9_Msk', '| FLEX_US_MR_CHRL_${FLEX_USART_MR_CHRL}')} | FLEX_US_MR_PAR_${FLEX_USART_MR_PAR} | FLEX_US_MR_NBSTOP_${FLEX_USART_MR_NBSTOP} | (${FLEXCOM_USART_MR_OVER}UL << FLEX_US_MR_OVER_Pos));

    /* Configure ${FLEXCOM_INSTANCE_NAME} USART Baud Rate */
    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_BRGR = FLEX_US_BRGR_CD(${BRG_VALUE}) | FLEX_US_BRGR_FP(${FP_VALUE});

    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rdCallback = NULL;
    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rdInIndex = 0;
    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rdOutIndex = 0;
    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.isRdNotificationEnabled = false;
    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.isRdNotifyPersistently = false;
    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rdThreshold = 0;
    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rdBufferSize = ${FLEXCOM_INSTANCE_NAME}_USART_READ_BUFFER_SIZE;
    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.wrCallback = NULL;
    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.wrInIndex = 0;
    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.wrOutIndex = 0;
    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.isWrNotificationEnabled = false;
    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.isWrNotifyPersistently = false;
    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.wrThreshold = 0;
    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.wrBufferSize = ${FLEXCOM_INSTANCE_NAME}_USART_WRITE_BUFFER_SIZE;
    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.errorStatus = FLEXCOM_USART_ERROR_NONE;
<#if FLEXCOM_USART_FIFO_ENABLE == true>
    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.isInterruptActive = false;
</#if>

    if ((${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_MR & FLEX_US_MR_MODE9_Msk) != 0U)
    {
        ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rdBufferSize = ${FLEXCOM_INSTANCE_NAME}_USART_9BIT_READ_BUFFER_SIZE;
        ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.wrBufferSize = ${FLEXCOM_INSTANCE_NAME}_USART_9BIT_WRITE_BUFFER_SIZE;
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
    /* Clear the error flags */
    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_CR = FLEX_US_CR_RSTSTA_Msk;

    /* Flush existing error bytes from the RX FIFO */
    while((${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_CSR & FLEX_US_CSR_RXRDY_Msk) != 0U)
    {
        if ((${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_MR & FLEX_US_MR_MODE9_Msk) != 0U)
        {
            (void)(FLEXCOM_USART_RHR_9BIT_REG);
        }
        else
        {
            (void)(FLEXCOM_USART_RHR_8BIT_REG);
        }
    }
}

FLEXCOM_USART_ERROR ${FLEXCOM_INSTANCE_NAME}_USART_ErrorGet( void )
{
    FLEXCOM_USART_ERROR errors = ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.errorStatus;

    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.errorStatus = FLEXCOM_USART_ERROR_NONE;

    /* All errors are cleared, but send the previous error state */
    return errors;
}

static void ${FLEXCOM_INSTANCE_NAME}_USART_BaudCalculate(uint32_t srcClkFreq, uint32_t reqBaud, uint8_t overSamp, uint32_t* cd, uint32_t* fp, uint32_t* baudError)
{
    uint32_t actualBaud = 0;

    *cd = srcClkFreq / (reqBaud * 8U * (2U - (uint32_t)overSamp));

    if (*cd > 0U)
    {
        *fp = ((srcClkFreq / (reqBaud * (2U - (uint32_t)overSamp))) - ((*cd) * 8U));
        actualBaud = (srcClkFreq / (((*cd) * 8U) + (*fp))) / (2U - overSamp);
        *baudError = ((100U * actualBaud)/reqBaud) - 100U;
    }
}

bool ${FLEXCOM_INSTANCE_NAME}_USART_SerialSetup( FLEXCOM_USART_SERIAL_SETUP *setup, uint32_t srcClkFreq )
{
    uint32_t baud = 0;
    uint32_t overSampVal = 0;
    uint32_t usartMode;
    uint32_t cd0, fp0, cd1, fp1, baudError0, baudError1;
    bool status = false;

    cd0 = fp0 = cd1 = fp1 = baudError0 = baudError1 = 0U;

    if (setup != NULL)
    {
        baud = setup->baudRate;

        if(srcClkFreq == 0U)
        {
            srcClkFreq = ${FLEXCOM_INSTANCE_NAME}_USART_FrequencyGet();
        }

        /* Calculate baud register values for 8x/16x oversampling values */

        ${FLEXCOM_INSTANCE_NAME}_USART_BaudCalculate(srcClkFreq, baud, 0, &cd0, &fp0, &baudError0);
        ${FLEXCOM_INSTANCE_NAME}_USART_BaudCalculate(srcClkFreq, baud, 1, &cd1, &fp1, &baudError1);

        if ( (!(cd0 > 0U && cd0 <= 65535U)) && (!(cd1 > 0U && cd1 <= 65535U)) )
        {
            /* Requested baud cannot be generated with current clock settings */
            return status;
        }

        if ( ((cd0 > 0U) && (cd0 <= 65535U)) && ((cd1 > 0U) && (cd1 <= 65535U)) )
        {
            /* Requested baud can be generated with both 8x and 16x oversampling. Select the one with less % error. */
            if (baudError1 < baudError0)
            {
                cd0 = cd1;
                fp0 = fp1;
                overSampVal = (1UL << FLEX_US_MR_OVER_Pos) & FLEX_US_MR_OVER_Msk;
            }
        }
        else
        {
            /* Requested baud can be generated with either with 8x oversampling or with 16x oversampling. Select valid one. */
            if ((cd1 > 0U) && (cd1 <= 65535U))
            {
                cd0 = cd1;
                fp0 = fp1;
                overSampVal = (1UL << FLEX_US_MR_OVER_Pos) & FLEX_US_MR_OVER_Msk;
            }
        }

        /* Configure ${FLEXCOM_INSTANCE_NAME} USART mode */
        usartMode = ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_MR;
        usartMode &= ~(FLEX_US_MR_CHRL_Msk | FLEX_US_MR_MODE9_Msk | FLEX_US_MR_PAR_Msk | FLEX_US_MR_NBSTOP_Msk | FLEX_US_MR_OVER_Msk);
        ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_MR = usartMode | ((uint32_t)setup->dataWidth | (uint32_t)setup->parity | (uint32_t)setup->stopBits | overSampVal);

        /* Configure ${FLEXCOM_INSTANCE_NAME} USART Baud Rate */
        ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_BRGR = FLEX_US_BRGR_CD(cd0) | FLEX_US_BRGR_FP(fp0);

        if ((${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_MR & FLEX_US_MR_MODE9_Msk) != 0U)
        {
            ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rdBufferSize = ${FLEXCOM_INSTANCE_NAME}_USART_9BIT_READ_BUFFER_SIZE;
            ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.wrBufferSize = ${FLEXCOM_INSTANCE_NAME}_USART_9BIT_WRITE_BUFFER_SIZE;
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
static bool ${FLEXCOM_INSTANCE_NAME}_USART_TxPullByte(void* pWrData)
{
    bool isSuccess = false;
    uint32_t wrOutIndex = ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.wrOutIndex;
    uint32_t wrInIndex = ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.wrInIndex;
    uint8_t* pWrByte = (uint8_t*)pWrData;
    if (wrOutIndex != wrInIndex)
    {
        if ((${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_MR & FLEX_US_MR_MODE9_Msk) != 0U)
        {
            uint32_t wrOutIdx = wrOutIndex << 1U;
            pWrByte[0] = ${FLEXCOM_INSTANCE_NAME}_USART_WriteBuffer[wrOutIdx];
            pWrByte[1] = ${FLEXCOM_INSTANCE_NAME}_USART_WriteBuffer[wrOutIdx + 1U];
        }
        else
        {
            *pWrByte = ${FLEXCOM_INSTANCE_NAME}_USART_WriteBuffer[wrOutIndex];
        }
        wrOutIndex++;

        if (wrOutIndex >= ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.wrBufferSize)
        {
            wrOutIndex = 0U;
        }

        ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.wrOutIndex = wrOutIndex;
        isSuccess = true;
    }
    return isSuccess;
}

static inline bool ${FLEXCOM_INSTANCE_NAME}_USART_TxPushByte(uint16_t wrByte)
{
    uint32_t tempInIndex;
    uint32_t wrOutIndex;
    uint32_t wrInIndex;
    bool isSuccess = false;

    /* Take a snapshot of indices to avoid creation of critical section */
    wrOutIndex = ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.wrOutIndex;
    wrInIndex = ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.wrInIndex;

    tempInIndex = wrInIndex + 1U;
    if (tempInIndex >= ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.wrBufferSize)
    {
        tempInIndex = 0U;
    }
    if (tempInIndex != wrOutIndex)
    {
        if ((${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_MR & FLEX_US_MR_MODE9_Msk) != 0U)
        {
            uint32_t wrInIdx = wrInIndex << 1U;
            ${FLEXCOM_INSTANCE_NAME}_USART_WriteBuffer[wrInIdx] = (uint8_t)wrByte;
            ${FLEXCOM_INSTANCE_NAME}_USART_WriteBuffer[wrInIdx + 1U] = (uint8_t)(wrByte >> 8U);
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
static void ${FLEXCOM_INSTANCE_NAME}_USART_SendWriteNotification(void)
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
        nPendingTxBytes =  wrInIndex -  wrOutIndex;
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
        if ((${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_MR & FLEX_US_MR_MODE9_Msk) != 0U)
        {
            uint16_t halfWordData = (uint16_t)(pWrBuffer[(2U * nBytesWritten) + 1U]);
            halfWordData <<= 8U;
            halfWordData |= (uint16_t)pWrBuffer[2U * nBytesWritten];
            if (${FLEXCOM_INSTANCE_NAME}_USART_TxPushByte(halfWordData) == true)
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
    if (${FLEXCOM_INSTANCE_NAME}_USART_WritePendingBytesGet() > 0U)
    {
        /* Enable TX interrupt as data is pending for transmission */
        ${FLEXCOM_INSTANCE_NAME}_USART_TX_INT_ENABLE();
    }

    return nBytesWritten;
}

size_t ${FLEXCOM_INSTANCE_NAME}_USART_WriteFreeBufferCountGet(void)
{
    return (${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.wrBufferSize - 1U) - ${FLEXCOM_INSTANCE_NAME}_USART_WriteCountGet();
}

size_t ${FLEXCOM_INSTANCE_NAME}_USART_WriteBufferSizeGet(void)
{
    return (${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.wrBufferSize - 1U);
}

bool ${FLEXCOM_INSTANCE_NAME}_USART_TransmitComplete(void)
{
    bool status = false;

    if ((${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_CSR & FLEX_US_CSR_TXEMPTY_Msk) != 0U)
    {
        status = true;
    }

    return status;
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
    if (nBytesThreshold > 0U)
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

    tempInIndex = ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rdInIndex + 1U;

    if (tempInIndex >= ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rdBufferSize)
    {
        tempInIndex = 0U;
    }

    if (tempInIndex == ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rdOutIndex)
    {
        /* Queue is full - Report it to the application. Application gets a chance to free up space by reading data out from the RX ring buffer */
        if(${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rdCallback != NULL)
        {
            ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rdCallback(FLEXCOM_USART_EVENT_READ_BUFFER_FULL, ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rdContext);

            /* Read the indices again in case application has freed up space in RX ring buffer */
            tempInIndex = ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rdInIndex + 1U;

            if (tempInIndex >= ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rdBufferSize)
            {
                tempInIndex = 0U;
            }
        }
    }

    /* Attempt to push the data into the ring buffer */
    if (tempInIndex != ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rdOutIndex)
    {
        if ((${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_MR & FLEX_US_MR_MODE9_Msk) != 0U)
        {
            uint32_t rdInIdx = ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rdInIndex << 1U;
            ${FLEXCOM_INSTANCE_NAME}_USART_ReadBuffer[rdInIdx] = (uint8_t)rdByte;
            ${FLEXCOM_INSTANCE_NAME}_USART_ReadBuffer[rdInIdx + 1U] = (uint8_t)(rdByte >> 8U);
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
static void ${FLEXCOM_INSTANCE_NAME}_USART_SendReadNotification(void)
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
    uint32_t rdOutIndex = 0;
    uint32_t rdInIndex = 0;

<#if FLEXCOM_USART_FIFO_ENABLE == true>
    if ((${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.isInterruptActive == false) && ((${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_CSR & FLEX_US_CSR_RXRDY_Msk) != 0U))
    {
        ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_IER = FLEX_US_IER_RXRDY_Msk;
        while ((${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_CSR & FLEX_US_CSR_RXRDY_Msk) != 0U)
        {
            /* Wait for RXRDY flag */
        }
        ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_IDR = FLEX_US_IDR_RXRDY_Msk;
    }
</#if>

    /* Take a snapshot of indices to avoid creation of critical section */
    rdOutIndex = ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rdOutIndex;
    rdInIndex = ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rdInIndex;

    while (nBytesRead < size)
    {
        if (rdOutIndex != rdInIndex)
        {
            if ((${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_MR & FLEX_US_MR_MODE9_Msk) != 0U)
            {
                uint32_t rdOutIdx = rdOutIndex << 1U;
                uint32_t nBytesReadIdx = nBytesRead << 1U;
                pRdBuffer[nBytesReadIdx] = ${FLEXCOM_INSTANCE_NAME}_USART_ReadBuffer[rdOutIdx];
                pRdBuffer[nBytesReadIdx + 1U] = ${FLEXCOM_INSTANCE_NAME}_USART_ReadBuffer[rdOutIdx + 1U];
                nBytesRead++;
                rdOutIndex++;
            }
            else
            {
                pRdBuffer[nBytesRead++] = ${FLEXCOM_INSTANCE_NAME}_USART_ReadBuffer[rdOutIndex];
                rdOutIndex++;
            }

            if (rdOutIndex >= ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rdBufferSize)
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

    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rdOutIndex = rdOutIndex;

    return nBytesRead;
}

size_t ${FLEXCOM_INSTANCE_NAME}_USART_ReadCountGet(void)
{
    size_t nUnreadBytesAvailable;
    uint32_t rdOutIndex;
    uint32_t rdInIndex;

<#if FLEXCOM_USART_FIFO_ENABLE == true>
    if ((${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.isInterruptActive == false) && ((${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_CSR & FLEX_US_CSR_RXRDY_Msk) != 0U))
    {
        ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_IER = FLEX_US_IER_RXRDY_Msk;

        while ((${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_CSR & FLEX_US_CSR_RXRDY_Msk) != 0U)
        {
            /* Wait for RXRDY flag */
        }

        ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_IDR = FLEX_US_IDR_RXRDY_Msk;
    }
</#if>

    /* Take a snapshot of indices to avoid creation of critical section */
    rdOutIndex = ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rdOutIndex;
    rdInIndex = ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rdInIndex;

    if ( rdInIndex >=  rdOutIndex)
    {
        nUnreadBytesAvailable =  rdInIndex -  rdOutIndex;
    }
    else
    {
        nUnreadBytesAvailable =  (${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rdBufferSize -  rdOutIndex) + rdInIndex;
    }

    return nUnreadBytesAvailable;
}

size_t ${FLEXCOM_INSTANCE_NAME}_USART_ReadFreeBufferCountGet(void)
{
    return (${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rdBufferSize - 1U) - ${FLEXCOM_INSTANCE_NAME}_USART_ReadCountGet();
}

size_t ${FLEXCOM_INSTANCE_NAME}_USART_ReadBufferSizeGet(void)
{
    return (${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rdBufferSize - 1U);
}

<#if FLEXCOM_USART_FIFO_ENABLE == true>
static void ${FLEXCOM_INSTANCE_NAME}_USART_UpdateRXFIFOThreshold(void)
{
    size_t nUnreadBytesAvailable = 0;
    size_t nBytesPendingForRDThreshold = 0;

    if (${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.isRdNotificationEnabled == true)
    {
        nUnreadBytesAvailable = ${FLEXCOM_INSTANCE_NAME}_USART_ReadCountGet();

        if (${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rdThreshold > nUnreadBytesAvailable)
        {
            /* Don't have RX threshold number of bytes in the receive buffer.
             * Setup the hardware FIFO threshold level based on number of bytes remaining to reach the rdThreshold level */

            nBytesPendingForRDThreshold = ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rdThreshold - nUnreadBytesAvailable;

            if (nBytesPendingForRDThreshold > ${FLEXCOM_INSTANCE_NAME}_USART_HW_RX_FIFO_THRES)
            {
                nBytesPendingForRDThreshold = ${FLEXCOM_INSTANCE_NAME}_USART_HW_RX_FIFO_THRES;
            }

            /* Set the new threshold level for hardware RX FIFO */
            ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_FMR = (${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_FMR & ~FLEX_US_FMR_RXFTHRES_Msk) | FLEX_US_FMR_RXFTHRES(nBytesPendingForRDThreshold);
        }
        else
        {
            /* Set the threshold to generate interrupt when the HW RX FIFO has RX threshold number of bytes */
            ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_FMR = (${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_FMR & ~FLEX_US_FMR_RXFTHRES_Msk) | FLEX_US_FMR_RXFTHRES(${FLEXCOM_INSTANCE_NAME}_USART_HW_RX_FIFO_THRES);
        }
    }
}
</#if>

bool ${FLEXCOM_INSTANCE_NAME}_USART_ReadNotificationEnable(bool isEnabled, bool isPersistent)
{
    bool previousStatus = ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.isRdNotificationEnabled;

    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.isRdNotificationEnabled = isEnabled;

    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.isRdNotifyPersistently = isPersistent;

<#if FLEXCOM_USART_FIFO_ENABLE == true>
    ${FLEXCOM_INSTANCE_NAME}_USART_UpdateRXFIFOThreshold();
</#if>

    return previousStatus;
}

void ${FLEXCOM_INSTANCE_NAME}_USART_ReadThresholdSet(uint32_t nBytesThreshold)
{
    if (nBytesThreshold > 0U)
    {
        ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rdThreshold = nBytesThreshold;

<#if FLEXCOM_USART_FIFO_ENABLE == true>
        ${FLEXCOM_INSTANCE_NAME}_USART_UpdateRXFIFOThreshold();
</#if>
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
    while(FLEX_US_CSR_RXRDY_Msk == (${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_CSR & FLEX_US_CSR_RXRDY_Msk))
    {
        if ((${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_MR & FLEX_US_MR_MODE9_Msk) != 0U)
        {
            rdData = FLEXCOM_USART_RHR_9BIT_REG & (uint16_t)FLEX_US_RHR_RXCHR_Msk;
        }
        else
        {
            rdData = (uint8_t)FLEXCOM_USART_RHR_8BIT_REG;
        }

        if (${FLEXCOM_INSTANCE_NAME}_USART_RxPushByte( rdData ) == true)
        {
            ${FLEXCOM_INSTANCE_NAME}_USART_SendReadNotification();
        }
        else
        {
            /* UART RX buffer is full */
        }
    }

<#if FLEXCOM_USART_FIFO_ENABLE == true>
    ${FLEXCOM_INSTANCE_NAME}_USART_UpdateRXFIFOThreshold();
</#if>

}

void static ${FLEXCOM_INSTANCE_NAME}_USART_ISR_TX_Handler( void )
{
    uint16_t wrByte;

    /* Keep writing to the TX FIFO as long as there is space */
    while(FLEX_US_CSR_TXRDY_Msk == (${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_CSR & FLEX_US_CSR_TXRDY_Msk))
    {
        if (${FLEXCOM_INSTANCE_NAME}_USART_TxPullByte(&wrByte) == true)
        {
            if ((${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_MR & FLEX_US_MR_MODE9_Msk) != 0U)
            {
                FLEXCOM_USART_THR_9BIT_REG = wrByte & (uint16_t)FLEX_US_THR_TXCHR_Msk;
            }
            else
            {
                FLEXCOM_USART_THR_8BIT_REG = (uint8_t)wrByte;
            }

            /* Send notification */
            ${FLEXCOM_INSTANCE_NAME}_USART_SendWriteNotification();
        }
        else
        {
            /* Nothing to transmit. Disable the data register empty/fifo Threshold interrupt. */
            ${FLEXCOM_INSTANCE_NAME}_USART_TX_INT_DISABLE();
            break;
        }
    }

<#if FLEXCOM_USART_FIFO_ENABLE == true>
    /* At this point, either FIFO is completly full or all bytes are transmitted (copied in FIFO). If FIFO is full, then threshold interrupt
    *  will be generated. If all bytes are transmitted then interrupts are disabled as interrupt generation is not needed in ring buffer mode
    */

    /* Always disable the TXRDY interrupt. It is only used to start off transmission. */
    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_IDR = FLEX_US_IDR_TXRDY_Msk;
</#if>
}

void ${FLEXCOM_INSTANCE_NAME}_InterruptHandler( void )
{
    /* Channel status */
    uint32_t channelStatus = ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_CSR;

    /* Error status */
    uint32_t errorStatus = (channelStatus & (FLEX_US_CSR_OVRE_Msk | FLEX_US_CSR_FRAME_Msk | FLEX_US_CSR_PARE_Msk));

<#if FLEXCOM_USART_FIFO_ENABLE == true>
    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.isInterruptActive = true;
</#if>

    if(errorStatus != 0U)
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

<#if FLEXCOM_USART_FIFO_ENABLE == true>
    /* Clear FIFO related interrupt flags */
    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_CR = FLEX_US_CR_RSTSTA_Msk;

    ${FLEXCOM_INSTANCE_NAME}_USART_ISR_RX_Handler();

    ${FLEXCOM_INSTANCE_NAME}_USART_ISR_TX_Handler();

    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.isInterruptActive = false;
<#else>
    /* Receiver status. RX interrupt is never disabled. */
    if ((channelStatus & FLEX_US_CSR_RXRDY_Msk) != 0U)
    {
        ${FLEXCOM_INSTANCE_NAME}_USART_ISR_RX_Handler();
    }

    /* Transmitter status */
    if( ((channelStatus & FLEX_US_CSR_TXRDY_Msk) != 0U) && ((${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_IMR & FLEX_US_IMR_TXRDY_Msk) != 0U) )
    {
        ${FLEXCOM_INSTANCE_NAME}_USART_ISR_TX_Handler();
    }
</#if>
}
