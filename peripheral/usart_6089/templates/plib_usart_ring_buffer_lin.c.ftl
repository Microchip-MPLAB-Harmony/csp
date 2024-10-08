/*******************************************************************************
  ${USART_INSTANCE_NAME} PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${USART_INSTANCE_NAME?lower_case}_LIN.c

  Summary:
    ${USART_INSTANCE_NAME} PLIB Implementation File in LIN mode

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
#include "plib_${USART_INSTANCE_NAME?lower_case}_lin.h"
<#if core.CoreSysIntFile == true>
#include "interrupts.h"
</#if>

<#--Implementation-->
// *****************************************************************************
// *****************************************************************************
// Section: ${USART_INSTANCE_NAME} Implementation
// *****************************************************************************
// *****************************************************************************

#define ${USART_INSTANCE_NAME}_READ_BUFFER_SIZE      ${USART_RX_RING_BUFFER_SIZE}U
#define ${USART_INSTANCE_NAME}_READ_BUFFER_SIZE_9BIT        (${USART_RX_RING_BUFFER_SIZE}U >> 1)
/* Disable Read, Overrun, Parity and Framing error interrupts */
#define ${USART_INSTANCE_NAME}_RX_INT_DISABLE()      ${USART_INSTANCE_NAME}_REGS->US_IDR = (US_IDR_USART_RXRDY_Msk |  US_IDR_LIN_OVRE_Msk | US_IDR_LIN_FRAME_Msk | US_IDR_LIN_PARE_Msk | US_IDR_LIN_TIMEOUT_Msk \
																							| US_IDR_LIN_LINBE_Msk | US_IDR_LIN_LINISFE_Msk | US_IDR_LIN_LINIPE_Msk \
																							| US_IDR_LIN_LINCE_Msk | US_IDR_LIN_LINSNRE_Msk | US_IDR_LIN_LINSTE_Msk | US_IDR_LIN_LINHTE_Msk);
/* Enable Read, Overrun, Parity and Framing error interrupts */
#define ${USART_INSTANCE_NAME}_RX_INT_ENABLE()       ${USART_INSTANCE_NAME}_REGS->US_IER = (US_IER_USART_RXRDY_Msk | US_IER_LIN_OVRE_Msk | US_IER_LIN_FRAME_Msk | US_IER_LIN_PARE_Msk | US_IER_LIN_TIMEOUT_Msk \
																							| US_IER_LIN_LINBE_Msk | US_IER_LIN_LINISFE_Msk | US_IER_LIN_LINIPE_Msk \
																							| US_IER_LIN_LINCE_Msk | US_IER_LIN_LINSNRE_Msk | US_IER_LIN_LINSTE_Msk | US_IER_LIN_LINHTE_Msk);

#define ${USART_INSTANCE_NAME}_WRITE_BUFFER_SIZE     ${USART_TX_RING_BUFFER_SIZE}U
#define ${USART_INSTANCE_NAME}_WRITE_BUFFER_SIZE_9BIT       (${USART_TX_RING_BUFFER_SIZE}U >> 1)
#define ${USART_INSTANCE_NAME}_TX_INT_DISABLE()      ${USART_INSTANCE_NAME}_REGS->US_IDR = US_IDR_USART_TXRDY_Msk;
#define ${USART_INSTANCE_NAME}_TX_INT_ENABLE()       ${USART_INSTANCE_NAME}_REGS->US_IER = US_IER_USART_TXRDY_Msk;

/* LIN related Interrupts */
#define ${USART_INSTANCE_NAME}_LIN_LINTC_INT_DISABLE()      ${USART_INSTANCE_NAME}_REGS->US_IDR = US_IDR_LIN_LINTC_Msk;
#define ${USART_INSTANCE_NAME}_LIN_LINTC_INT_ENABLE()       ${USART_INSTANCE_NAME}_REGS->US_IER = US_IER_LIN_LINTC_Msk;

#define ${USART_INSTANCE_NAME}_LIN_LINID_INT_DISABLE()      ${USART_INSTANCE_NAME}_REGS->US_IDR = US_IDR_LIN_LINID_Msk;
#define ${USART_INSTANCE_NAME}_LIN_LINID_INT_ENABLE()       ${USART_INSTANCE_NAME}_REGS->US_IER = US_IER_LIN_LINID_Msk;

#define ${USART_INSTANCE_NAME}_LIN_LINBK_INT_DISABLE()      ${USART_INSTANCE_NAME}_REGS->US_IDR = US_IDR_LIN_LINBK_Msk;
#define ${USART_INSTANCE_NAME}_LIN_LINBK_INT_ENABLE()       ${USART_INSTANCE_NAME}_REGS->US_IER = US_IER_LIN_LINBK_Msk;

volatile static uint8_t ${USART_INSTANCE_NAME}_ReadBuffer[${USART_INSTANCE_NAME}_READ_BUFFER_SIZE];
volatile static USART_RING_BUFFER_OBJECT ${USART_INSTANCE_NAME?lower_case}Obj;
volatile static uint8_t ${USART_INSTANCE_NAME}_WriteBuffer[${USART_INSTANCE_NAME}_WRITE_BUFFER_SIZE];
volatile static USART_LIN_CALLBACK_OBJECT ${USART_INSTANCE_NAME?lower_case}LinObj;

void ${USART_INSTANCE_NAME}_Initialize( void )
{
    /* Reset ${USART_INSTANCE_NAME} */
    ${USART_INSTANCE_NAME}_REGS->US_CR = (US_CR_USART_RSTRX_Msk | US_CR_USART_RSTTX_Msk | US_CR_USART_RSTSTA_Msk);

    /* Enable ${USART_INSTANCE_NAME} */
    ${USART_INSTANCE_NAME}_REGS->US_CR = (US_CR_USART_TXEN_Msk | US_CR_USART_RXEN_Msk);

    /* Configure ${USART_INSTANCE_NAME} mode */
    <#if USART_MR_MODE9 == true>
    ${USART_INSTANCE_NAME}_REGS->US_MR = (US_MR_USART_USCLKS_${USART_CLK_SRC} | US_MR_USART_MODE9_Msk | US_MR_USART_PAR_${USART_MR_PAR} | US_MR_USART_NBSTOP_${USART_MR_NBSTOP} | US_MR_USART_OVER(${USART_MR_OVER?string}));
    <#else>
    ${USART_INSTANCE_NAME}_REGS->US_MR = (US_MR_USART_USCLKS_${USART_CLK_SRC} | US_MR_USART_CHRL_${USART_MR_CHRL} | US_MR_USART_PAR_${USART_MR_PAR} | US_MR_USART_NBSTOP_${USART_MR_NBSTOP} | US_MR_USART_OVER(${USART_MR_OVER?string}));
    </#if>

    <#if USART_MODE == "LIN_MASTER" || USART_MODE == "LIN_SLAVE">
    ${USART_INSTANCE_NAME}_REGS->US_MR |= US_MR_USART_MODE_${USART_MODE};
 <@compress>${USART_INSTANCE_NAME}_REGS->US_LINMR = ${USART_LIN_LINMR_PARDIS?then('US_LINMR_PARDIS_Msk |', '')}
        ${USART_LIN_LINMR_CHKDIS?then('US_LINMR_CHKDIS_Msk |', '')}
        ${USART_LIN_LINMR_FSDIS?then('US_LINMR_FSDIS_Msk |', '')}
        ${USART_LIN_LINMR_SYNCDIS?then('US_LINMR_SYNCDIS_Msk |', '')}
        US_LINMR_CHKTYP(${USART_LIN_LINMR_CHKTYP}U) | US_LINMR_DLM(${USART_LIN_LINMR_DLM}U) |
        US_LINMR_DLC(${USART_LIN_LINMR_DLC}U) | US_LINMR_WKUPTYP(${USART_LIN_LINMR_WKUPTYP}U); </@compress>    
    </#if>

    /* Configure ${USART_INSTANCE_NAME} Baud Rate */
    ${USART_INSTANCE_NAME}_REGS->US_BRGR = US_BRGR_CD(${BRG_VALUE}U);

    /* Initialize instance object */
    ${USART_INSTANCE_NAME?lower_case}Obj.rdCallback = NULL;
    ${USART_INSTANCE_NAME?lower_case}Obj.rdInIndex = 0;
    ${USART_INSTANCE_NAME?lower_case}Obj.rdOutIndex = 0;
    ${USART_INSTANCE_NAME?lower_case}Obj.isRdNotificationEnabled = false;
    ${USART_INSTANCE_NAME?lower_case}Obj.isRdNotifyPersistently = false;
    ${USART_INSTANCE_NAME?lower_case}Obj.rdThreshold = 0;
    ${USART_INSTANCE_NAME?lower_case}Obj.errorStatus = USART_ERROR_NONE;
    ${USART_INSTANCE_NAME?lower_case}Obj.wrCallback = NULL;
    ${USART_INSTANCE_NAME?lower_case}Obj.wrInIndex = 0;
    ${USART_INSTANCE_NAME?lower_case}Obj.wrOutIndex = 0;
    ${USART_INSTANCE_NAME?lower_case}Obj.isWrNotificationEnabled = false;
    ${USART_INSTANCE_NAME?lower_case}Obj.isWrNotifyPersistently = false;
    ${USART_INSTANCE_NAME?lower_case}Obj.wrThreshold = 0;

    if((${USART_INSTANCE_NAME}_REGS->US_MR & US_MR_USART_MODE9_Msk) != 0U)
    {
        ${USART_INSTANCE_NAME?lower_case}Obj.rdBufferSize = ${USART_INSTANCE_NAME}_READ_BUFFER_SIZE_9BIT;
        ${USART_INSTANCE_NAME?lower_case}Obj.wrBufferSize = ${USART_INSTANCE_NAME}_WRITE_BUFFER_SIZE_9BIT;
    }
    else
    {
        ${USART_INSTANCE_NAME?lower_case}Obj.rdBufferSize = ${USART_INSTANCE_NAME}_READ_BUFFER_SIZE;
        ${USART_INSTANCE_NAME?lower_case}Obj.wrBufferSize = ${USART_INSTANCE_NAME}_WRITE_BUFFER_SIZE;
    }

    /* Enable Read, Overrun, Parity and Framing error interrupts */
    ${USART_INSTANCE_NAME}_RX_INT_ENABLE();
	
<#if USART_LIN_OPERATING_MODE == "RING_BUFFER">
	<#if USART_LIN_LINID_INTERRUPT_ENABLE == true>
	/* Enable LIN ID interrupt */
	${USART_INSTANCE_NAME}_LIN_LINID_INT_ENABLE();
    </#if>
	
	<#if USART_LIN_LINTC_INTERRUPT_ENABLE == true>
	/* Enable LIN Transfer Complete interrupt */
    ${USART_INSTANCE_NAME}_LIN_LINTC_INT_ENABLE();
    </#if>
	
	<#if USART_LIN_LINBK_INTERRUPT_ENABLE == true>
	/* Enable LIN Break interrupt */
    ${USART_INSTANCE_NAME}_LIN_LINBK_INT_ENABLE();
	</#if>
</#if>
}

bool ${USART_INSTANCE_NAME}_SerialSetup( USART_SERIAL_SETUP *setup, uint32_t srcClkFreq )
{
    uint32_t baud;
    uint32_t brgVal = 0;
    uint32_t overSampVal = 0;
    uint32_t usartMode;
    bool status = (setup != NULL);

    /*Valid pointer */
    if(status)
    {
        baud = setup->baudRate;
        if(srcClkFreq == 0U)
        {
            srcClkFreq = ${USART_INSTANCE_NAME}_FrequencyGet();
        }

        /* Calculate BRG value */
        if (srcClkFreq >= (16U * baud))
        {
            brgVal = (srcClkFreq / (16U * baud));
        }
        else if (srcClkFreq >= (8U * baud))
        {
            brgVal = (srcClkFreq / (8U * baud));
            overSampVal = US_MR_USART_OVER(1U);
        }
        else
        {
           /* Invalid clock */
           status = false;
        }

        status = status && (brgVal <= 65535U);
        /* Target baud is achievable */
        if(status)
        {
            /* Configure ${USART_INSTANCE_NAME} mode */
            usartMode = ${USART_INSTANCE_NAME}_REGS->US_MR;
            usartMode &= ~(US_MR_USART_CHRL_Msk | US_MR_USART_MODE9_Msk | US_MR_USART_PAR_Msk | US_MR_USART_NBSTOP_Msk | US_MR_USART_OVER_Msk);
            ${USART_INSTANCE_NAME}_REGS->US_MR = usartMode | ((uint32_t)setup->dataWidth | (uint32_t)setup->parity | (uint32_t)setup->stopBits | (uint32_t)overSampVal);

            /* Configure ${USART_INSTANCE_NAME} Baud Rate */
            ${USART_INSTANCE_NAME}_REGS->US_BRGR = US_BRGR_CD(brgVal);

            if((${USART_INSTANCE_NAME}_REGS->US_MR & US_MR_USART_MODE9_Msk) != 0U)
            {
                ${USART_INSTANCE_NAME?lower_case}Obj.rdBufferSize = ${USART_INSTANCE_NAME}_READ_BUFFER_SIZE_9BIT;
                ${USART_INSTANCE_NAME?lower_case}Obj.wrBufferSize = ${USART_INSTANCE_NAME}_WRITE_BUFFER_SIZE_9BIT;
            }
            else
            {
                ${USART_INSTANCE_NAME?lower_case}Obj.rdBufferSize = ${USART_INSTANCE_NAME}_READ_BUFFER_SIZE;
                ${USART_INSTANCE_NAME?lower_case}Obj.wrBufferSize = ${USART_INSTANCE_NAME}_WRITE_BUFFER_SIZE;
            }

        }
    }
    return status;
}

static void ${USART_INSTANCE_NAME}_ErrorClear( void )
{
    uint32_t dummyData = 0U;

    ${USART_INSTANCE_NAME}_REGS->US_CR = US_CR_USART_RSTSTA_Msk;

    /* Flush existing error bytes from the RX FIFO */
    while( US_CSR_USART_RXRDY_Msk == (${USART_INSTANCE_NAME}_REGS->US_CSR & US_CSR_USART_RXRDY_Msk))
    {
        dummyData = (${USART_INSTANCE_NAME}_REGS->US_RHR & US_RHR_RXCHR_Msk);
    }

    /* Ignore the warning */
    (void)dummyData;
}

USART_ERROR ${USART_INSTANCE_NAME}_ErrorGet( void )
{
    USART_ERROR errors = ${USART_INSTANCE_NAME?lower_case}Obj.errorStatus;

    ${USART_INSTANCE_NAME?lower_case}Obj.errorStatus = USART_ERROR_NONE;

    /* All errors are cleared, but send the previous error state */
    return errors;
}

/* This routine is only called from ISR. Hence do not disable/enable USART interrupts. */
static inline bool ${USART_INSTANCE_NAME}_RxPushByte(uint16_t rdByte)
{
    uint32_t tempInIndex;
    bool isSuccess = false;
    uint32_t rdInIdx;

    tempInIndex = ${USART_INSTANCE_NAME?lower_case}Obj.rdInIndex + 1U;

    if (tempInIndex >= ${USART_INSTANCE_NAME?lower_case}Obj.rdBufferSize)
    {
        tempInIndex = 0U;
    }

    if (tempInIndex == ${USART_INSTANCE_NAME?lower_case}Obj.rdOutIndex)
    {
        /* Queue is full - Report it to the application. Application gets a chance to free up space by reading data out from the RX ring buffer */
        if(${USART_INSTANCE_NAME?lower_case}Obj.rdCallback != NULL)
        {
            uintptr_t rdContext = ${USART_INSTANCE_NAME?lower_case}Obj.rdContext;

            ${USART_INSTANCE_NAME?lower_case}Obj.rdCallback(USART_EVENT_READ_BUFFER_FULL, rdContext);

            /* Read the indices again in case application has freed up space in RX ring buffer */
            tempInIndex = ${USART_INSTANCE_NAME?lower_case}Obj.rdInIndex + 1U;

            if (tempInIndex >= ${USART_INSTANCE_NAME?lower_case}Obj.rdBufferSize)
            {
                tempInIndex = 0U;
            }
        }
    }

    if (tempInIndex != ${USART_INSTANCE_NAME?lower_case}Obj.rdOutIndex)
    {
        if ((${USART_INSTANCE_NAME}_REGS->US_MR & US_MR_USART_MODE9_Msk) != 0U)
        {
            rdInIdx = ${USART_INSTANCE_NAME?lower_case}Obj.rdInIndex << 1U;
            ${USART_INSTANCE_NAME}_ReadBuffer[rdInIdx] = (uint8_t)rdByte;
            ${USART_INSTANCE_NAME}_ReadBuffer[rdInIdx + 1U] = (uint8_t)(rdByte >> 8U);
        }
        else
        {
            uint32_t rdInIndex = ${USART_INSTANCE_NAME?lower_case}Obj.rdInIndex;

            ${USART_INSTANCE_NAME}_ReadBuffer[rdInIndex] = (uint8_t)rdByte;
        }

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
            uintptr_t rdContext = ${USART_INSTANCE_NAME?lower_case}Obj.rdContext;

            if (${USART_INSTANCE_NAME?lower_case}Obj.isRdNotifyPersistently == true)
            {
                if (nUnreadBytesAvailable >= ${USART_INSTANCE_NAME?lower_case}Obj.rdThreshold)
                {
                    ${USART_INSTANCE_NAME?lower_case}Obj.rdCallback(USART_EVENT_READ_THRESHOLD_REACHED, rdContext);
                }
            }
            else
            {
                if (nUnreadBytesAvailable == ${USART_INSTANCE_NAME?lower_case}Obj.rdThreshold)
                {
                    ${USART_INSTANCE_NAME?lower_case}Obj.rdCallback(USART_EVENT_READ_THRESHOLD_REACHED, rdContext);
                }
            }
        }
    }
}

size_t ${USART_INSTANCE_NAME}_Read(uint8_t* pRdBuffer, const size_t size)
{
    size_t nBytesRead = 0;

    /* Take a snapshot of indices to avoid creation of critical section */
    uint32_t rdOutIndex = ${USART_INSTANCE_NAME?lower_case}Obj.rdOutIndex;
    uint32_t rdInIndex = ${USART_INSTANCE_NAME?lower_case}Obj.rdInIndex;
    uint32_t rdOut16Idx;
    uint32_t nBytesRead16Idx;

    while (nBytesRead < size)
    {
        if (rdOutIndex != rdInIndex)
        {
            if ((${USART_INSTANCE_NAME}_REGS->US_MR & US_MR_USART_MODE9_Msk) != 0U)
            {
                rdOut16Idx = rdOutIndex << 1U;
                nBytesRead16Idx = nBytesRead << 1U;

                pRdBuffer[nBytesRead16Idx] = ${USART_INSTANCE_NAME}_ReadBuffer[rdOut16Idx];
                pRdBuffer[nBytesRead16Idx + 1U] = ${USART_INSTANCE_NAME}_ReadBuffer[rdOut16Idx + 1U];
            }
            else
            {
                pRdBuffer[nBytesRead] = ${USART_INSTANCE_NAME}_ReadBuffer[rdOutIndex];
            }

            nBytesRead++;
            rdOutIndex++;

            if (rdOutIndex >= ${USART_INSTANCE_NAME?lower_case}Obj.rdBufferSize)
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

    ${USART_INSTANCE_NAME?lower_case}Obj.rdOutIndex = rdOutIndex;

    return nBytesRead;
}

size_t ${USART_INSTANCE_NAME}_ReadCountGet(void)
{
    size_t nUnreadBytesAvailable;

    /* Take a snapshot of indices to avoid creation of critical section */
    uint32_t rdOutIndex = ${USART_INSTANCE_NAME?lower_case}Obj.rdOutIndex;
    uint32_t rdInIndex = ${USART_INSTANCE_NAME?lower_case}Obj.rdInIndex;

    if ( rdInIndex >=  rdOutIndex)
    {
        nUnreadBytesAvailable =  rdInIndex - rdOutIndex;
    }
    else
    {
        nUnreadBytesAvailable =  (${USART_INSTANCE_NAME?lower_case}Obj.rdBufferSize -  rdOutIndex) + rdInIndex;
    }

    return nUnreadBytesAvailable;
}

size_t ${USART_INSTANCE_NAME}_ReadFreeBufferCountGet(void)
{
    return (${USART_INSTANCE_NAME?lower_case}Obj.rdBufferSize - 1U) - ${USART_INSTANCE_NAME}_ReadCountGet();
}

size_t ${USART_INSTANCE_NAME}_ReadBufferSizeGet(void)
{
    return (${USART_INSTANCE_NAME?lower_case}Obj.rdBufferSize - 1U);
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
    if (nBytesThreshold > 0U)
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
static bool ${USART_INSTANCE_NAME}_TxPullByte(void* pWrData)
{
    uint8_t* pWrByte = (uint8_t*)pWrData;
    uint32_t wrOutIndex = ${USART_INSTANCE_NAME?lower_case}Obj.wrOutIndex;
    uint32_t wrInIndex = ${USART_INSTANCE_NAME?lower_case}Obj.wrInIndex;
    uint32_t wrOut16Idx;
    bool isSuccess = false;

    if (wrOutIndex != wrInIndex)
    {
        if((${USART_INSTANCE_NAME}_REGS->US_MR & US_MR_USART_MODE9_Msk) != 0U)
        {
            wrOut16Idx = wrOutIndex << 1U;
            pWrByte[0] = ${USART_INSTANCE_NAME}_WriteBuffer[wrOut16Idx];
            pWrByte[1] = ${USART_INSTANCE_NAME}_WriteBuffer[wrOut16Idx + 1U];
        }
        else
        {
            *pWrByte = ${USART_INSTANCE_NAME}_WriteBuffer[wrOutIndex];
        }

        wrOutIndex++;
        if (wrOutIndex >= ${USART_INSTANCE_NAME?lower_case}Obj.wrBufferSize)
        {
            wrOutIndex = 0U;
        }

        ${USART_INSTANCE_NAME?lower_case}Obj.wrOutIndex = wrOutIndex;

        isSuccess = true;
    }

    return isSuccess;
}

static inline bool ${USART_INSTANCE_NAME}_TxPushByte(uint16_t wrByte)
{
    uint32_t tempInIndex;
    uint32_t wrOutIndex = ${USART_INSTANCE_NAME?lower_case}Obj.wrOutIndex;
    uint32_t wrInIndex = ${USART_INSTANCE_NAME?lower_case}Obj.wrInIndex;
    uint32_t wrIn16Idx;
    bool isSuccess = false;

    tempInIndex = wrInIndex + 1U;

    if (tempInIndex >= ${USART_INSTANCE_NAME?lower_case}Obj.wrBufferSize)
    {
        tempInIndex = 0U;
    }
    if (tempInIndex != wrOutIndex)
    {
        if((${USART_INSTANCE_NAME}_REGS->US_MR & US_MR_USART_MODE9_Msk) != 0U)
        {
            wrIn16Idx = wrInIndex << 1U;
            ${USART_INSTANCE_NAME}_WriteBuffer[wrIn16Idx] = (uint8_t)wrByte;
            ${USART_INSTANCE_NAME}_WriteBuffer[wrIn16Idx + 1U] = (uint8_t)(wrByte >> 8U);
        }
        else
        {
            ${USART_INSTANCE_NAME}_WriteBuffer[wrInIndex] = (uint8_t)wrByte;
        }

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
            uintptr_t wrContext = ${USART_INSTANCE_NAME?lower_case}Obj.wrContext;

            if (${USART_INSTANCE_NAME?lower_case}Obj.isWrNotifyPersistently == true)
            {
                if (nFreeWrBufferCount >= ${USART_INSTANCE_NAME?lower_case}Obj.wrThreshold)
                {
                    ${USART_INSTANCE_NAME?lower_case}Obj.wrCallback(USART_EVENT_WRITE_THRESHOLD_REACHED, wrContext);
                }
            }
            else
            {
                if (nFreeWrBufferCount == ${USART_INSTANCE_NAME?lower_case}Obj.wrThreshold)
                {
                    ${USART_INSTANCE_NAME?lower_case}Obj.wrCallback(USART_EVENT_WRITE_THRESHOLD_REACHED, wrContext);
                }
            }
        }
    }
}

static size_t ${USART_INSTANCE_NAME}_WritePendingBytesGet(void)
{
    size_t nPendingTxBytes;

    /* Take a snapshot of indices to avoid creation of critical section */
    uint32_t wrOutIndex = ${USART_INSTANCE_NAME?lower_case}Obj.wrOutIndex;
    uint32_t wrInIndex = ${USART_INSTANCE_NAME?lower_case}Obj.wrInIndex;

    if ( wrInIndex >= wrOutIndex)
    {
        nPendingTxBytes =  wrInIndex -  wrOutIndex;
    }
    else
    {
        nPendingTxBytes =  (${USART_INSTANCE_NAME?lower_case}Obj.wrBufferSize -  wrOutIndex) + wrInIndex;
    }

    return nPendingTxBytes;
}

size_t ${USART_INSTANCE_NAME}_WriteCountGet(void)
{
    size_t nPendingTxBytes;

    nPendingTxBytes = ${USART_INSTANCE_NAME}_WritePendingBytesGet();

    return nPendingTxBytes;
}

size_t ${USART_INSTANCE_NAME}_Write(uint8_t* pWrBuffer, const size_t size )
{
    size_t nBytesWritten  = 0U;
    uint16_t halfWordData = 0U;

    while (nBytesWritten < size)
    {
        if ((${USART_INSTANCE_NAME}_REGS->US_MR & US_MR_USART_MODE9_Msk) != 0U)
        {
            halfWordData = pWrBuffer[(2U * nBytesWritten) + 1U];
            halfWordData <<= 8U;
            halfWordData |= pWrBuffer[(2U * nBytesWritten)];
            if (${USART_INSTANCE_NAME}_TxPushByte(halfWordData) == true)
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
    }

    /* Check if any data is pending for transmission */
    if (${USART_INSTANCE_NAME}_WritePendingBytesGet() > 0U)
    {
        /* Enable TX interrupt as data is pending for transmission */
        ${USART_INSTANCE_NAME}_TX_INT_ENABLE();
    }

    return nBytesWritten;
}

size_t ${USART_INSTANCE_NAME}_WriteFreeBufferCountGet(void)
{
    return (${USART_INSTANCE_NAME?lower_case}Obj.wrBufferSize - 1U) - ${USART_INSTANCE_NAME}_WriteCountGet();
}

size_t ${USART_INSTANCE_NAME}_WriteBufferSizeGet(void)
{
    return (${USART_INSTANCE_NAME?lower_case}Obj.wrBufferSize - 1U);
}

bool ${USART_INSTANCE_NAME}_TransmitComplete(void)
{
    return ((${USART_INSTANCE_NAME}_REGS->US_CSR & US_CSR_USART_TXEMPTY_Msk) != 0U);
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
    if (nBytesThreshold > 0U)
    {
        ${USART_INSTANCE_NAME?lower_case}Obj.wrThreshold = nBytesThreshold;
    }
}

void ${USART_INSTANCE_NAME}_WriteCallbackRegister( USART_RING_BUFFER_CALLBACK callback, uintptr_t context)
{
    ${USART_INSTANCE_NAME?lower_case}Obj.wrCallback = callback;
    ${USART_INSTANCE_NAME?lower_case}Obj.wrContext = context;
}

static void __attribute__((used)) ${USART_INSTANCE_NAME}_ISR_RX_Handler( void )
{
    uint32_t rdData = 0;

    /* Keep reading until there is a character availabe in the RX FIFO */
    while ((${USART_INSTANCE_NAME}_REGS->US_CSR & US_CSR_USART_RXRDY_Msk) != 0U)
    {
        rdData = ${USART_INSTANCE_NAME}_REGS->US_RHR & US_RHR_RXCHR_Msk;

        if (${USART_INSTANCE_NAME}_RxPushByte((uint16_t)rdData ) == true)
        {
            ${USART_INSTANCE_NAME}_ReadNotificationSend();
        }
        else
        {
            /* UART RX buffer is full */
        }
    }
}

static void __attribute__((used)) ${USART_INSTANCE_NAME}_ISR_TX_Handler( void )
{
    uint16_t wrByte = 0U;

    /* Keep writing to the TX FIFO as long as there is space */
    while ((${USART_INSTANCE_NAME}_REGS->US_CSR & US_CSR_USART_TXRDY_Msk) != 0U)
    {
        if (${USART_INSTANCE_NAME}_TxPullByte(&wrByte) == true)
        {
            if ((${USART_INSTANCE_NAME}_REGS->US_MR & US_MR_USART_MODE9_Msk) != 0U)
            {
                ${USART_INSTANCE_NAME}_REGS->US_THR = ((uint32_t)wrByte & US_THR_TXCHR_Msk);
            }
            else
            {
                ${USART_INSTANCE_NAME}_REGS->US_THR = (uint8_t)wrByte;
            }

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

void __attribute__((used)) ${USART_INSTANCE_NAME}_InterruptHandler( void )
{
    /* Error status */
    uint32_t errorStatus = (${USART_INSTANCE_NAME}_REGS->US_CSR & (US_CSR_LIN_OVRE_Msk | US_CSR_LIN_FRAME_Msk | US_CSR_LIN_PARE_Msk | US_CSR_LIN_TIMEOUT_Msk
																	| US_CSR_LIN_LINBE_Msk | US_CSR_LIN_LINISFE_Msk | US_CSR_LIN_LINIPE_Msk
																	| US_CSR_LIN_LINCE_Msk | US_CSR_LIN_LINSNRE_Msk | US_CSR_LIN_LINSTE_Msk | US_CSR_LIN_LINHTE_Msk));

    if(errorStatus != 0U)
    {
        /* Save the error so that it can be reported when application calls the ${USART_INSTANCE_NAME}_ErrorGet() API */
        ${USART_INSTANCE_NAME?lower_case}Obj.errorStatus = (USART_ERROR)errorStatus;

        /* Clear the error flags and flush out the error bytes */
        ${USART_INSTANCE_NAME}_ErrorClear();

        /* USART errors are normally associated with the receiver, hence calling receiver callback */
        if( ${USART_INSTANCE_NAME?lower_case}Obj.rdCallback != NULL)
        {
            uintptr_t rdContext = ${USART_INSTANCE_NAME?lower_case}Obj.rdContext;

            ${USART_INSTANCE_NAME?lower_case}Obj.rdCallback(USART_EVENT_READ_ERROR, rdContext);
        }
    }

    /* Receiver status */
    if((${USART_INSTANCE_NAME}_REGS->US_CSR & US_CSR_USART_RXRDY_Msk) != 0U)
    {
        ${USART_INSTANCE_NAME}_ISR_RX_Handler();
    }

    /* Transmitter status */
    if((${USART_INSTANCE_NAME}_REGS->US_CSR & US_CSR_USART_TXRDY_Msk) != 0U)
    {
        ${USART_INSTANCE_NAME}_ISR_TX_Handler();
    }
<#if USART_LIN_OPERATING_MODE == "RING_BUFFER">
	<#if USART_LIN_LINBK_INTERRUPT_ENABLE == true>
	/* LIN Break Detected */
    if((${USART_INSTANCE_NAME}_REGS->US_CSR & US_CSR_LIN_LINBK_Msk) != 0U)
    {
        ${USART_INSTANCE_NAME}_REGS->US_CR = US_CR_USART_RSTSTA_Msk;
       
        if( ${USART_INSTANCE_NAME?lower_case}LinObj.breakCallback != NULL)
        {
            uintptr_t breakContext = ${USART_INSTANCE_NAME?lower_case}LinObj.breakContext;
            ${USART_INSTANCE_NAME?lower_case}LinObj.breakCallback(breakContext);
        }
    }
	</#if>
    
	<#if USART_LIN_LINID_INTERRUPT_ENABLE == true>
    /* LIN ID Receive */
    if((${USART_INSTANCE_NAME}_REGS->US_CSR & US_CSR_LIN_LINID_Msk) != 0U)
    {
        ${USART_INSTANCE_NAME}_REGS->US_CR = US_CR_USART_RSTSTA_Msk;
       
        if( ${USART_INSTANCE_NAME?lower_case}LinObj.idCallback != NULL)
        {
            uintptr_t idContext = ${USART_INSTANCE_NAME?lower_case}LinObj.idContext;
            ${USART_INSTANCE_NAME?lower_case}LinObj.idCallback(idContext);
        }
    }
    </#if>
	
	<#if USART_LIN_LINTC_INTERRUPT_ENABLE == true>
    /* LIN Transfer Complete */
    if((${USART_INSTANCE_NAME}_REGS->US_CSR & US_CSR_LIN_LINTC_Msk) != 0U)
    {
        ${USART_INSTANCE_NAME}_REGS->US_CR = US_CR_USART_RSTSTA_Msk;
       
        if( ${USART_INSTANCE_NAME?lower_case}LinObj.tranferCallback != NULL)
        {
            uintptr_t transferContext = ${USART_INSTANCE_NAME?lower_case}LinObj.tranferContext;
            ${USART_INSTANCE_NAME?lower_case}LinObj.tranferCallback(transferContext);
        }
    }
	</#if>
</#if>
}


<#if USART_MODE == "LIN_MASTER" || USART_MODE == "LIN_SLAVE">

void ${USART_INSTANCE_NAME}_LIN_NodeActionSet( USART_LIN_NACT action )
{
    ${USART_INSTANCE_NAME}_REGS->US_LINMR &= ~(US_LINMR_NACT_Msk);
    ${USART_INSTANCE_NAME}_REGS->US_LINMR |= US_LINMR_NACT(action);
}

bool ${USART_INSTANCE_NAME}_LIN_IdentifierWrite( uint8_t id)
{
	bool status = false; 
	${USART_INSTANCE_NAME}_REGS->US_CR = US_CR_USART_RSTSTA_Msk;
    
    if((${USART_INSTANCE_NAME}_REGS->US_CSR & US_CSR_USART_TXRDY_Msk) != 0U)
    {
        ${USART_INSTANCE_NAME}_REGS->US_LINIR = id;
		status = true;
    }
	
	return status;
}

uint8_t ${USART_INSTANCE_NAME}_LIN_IdentifierRead( void)
{
    return (uint8_t)(${USART_INSTANCE_NAME}_REGS->US_LINIR);
}

void ${USART_INSTANCE_NAME}_LIN_ParityEnable(bool parityEnable)
{
    if(parityEnable == true)
    {
        USART0_REGS->US_LINMR &= ~US_LINMR_PARDIS_Msk;
    }
    else
    {
        USART0_REGS->US_LINMR |= US_LINMR_PARDIS_Msk;
    }
}

void ${USART_INSTANCE_NAME}_LIN_ChecksumEnable(bool checksumEnable)
{
    if(checksumEnable == true)
    {
        ${USART_INSTANCE_NAME}_REGS->US_LINMR &= ~US_LINMR_CHKDIS_Msk;
    }
    else
    {
        ${USART_INSTANCE_NAME}_REGS->US_LINMR |= US_LINMR_CHKDIS_Msk;
    }
}

void ${USART_INSTANCE_NAME}_LIN_ChecksumTypeSet(USART_LIN_CHECKSUM_TYPE checksumType)
{
	${USART_INSTANCE_NAME}_REGS->US_LINMR &= ~US_LINMR_CHKTYP_Msk;
	${USART_INSTANCE_NAME}_REGS->US_LINMR |= (uint32_t)checksumType;
}

<#if USART_MODE == "LIN_MASTER">
void ${USART_INSTANCE_NAME}_LIN_FrameSlotEnable(bool frameSlotEnable)
{
    if(frameSlotEnable == true)
    {
        ${USART_INSTANCE_NAME}_REGS->US_LINMR &= ~US_LINMR_FSDIS_Msk;
    }
    else
    {
        ${USART_INSTANCE_NAME}_REGS->US_LINMR |= US_LINMR_FSDIS_Msk;
    }
}
</#if>

void ${USART_INSTANCE_NAME}_LIN_DataLenModeSet(USART_LIN_DATA_LEN dataLenMode)
{
    ${USART_INSTANCE_NAME}_REGS->US_LINMR &= ~US_LINMR_DLM_Msk;
    ${USART_INSTANCE_NAME}_REGS->US_LINMR |= (uint32_t)dataLenMode;    
}

void ${USART_INSTANCE_NAME}_LIN_ResponseDataLenSet(uint8_t len)
{
    ${USART_INSTANCE_NAME}_REGS->US_LINMR &= ~US_LINMR_DLC_Msk;
    ${USART_INSTANCE_NAME}_REGS->US_LINMR |= US_LINMR_DLC((uint32_t)len-1U);
}

uint8_t ${USART_INSTANCE_NAME}_LIN_TransferComplete(void)
{
	return (uint8_t)((USART0_REGS->US_CSR & US_CSR_LIN_LINTC_Msk) > 0U);
}

<#if USART_LIN_OPERATING_MODE == "RING_BUFFER">
<#if USART_LIN_LINID_INTERRUPT_ENABLE == true>
void ${USART_INSTANCE_NAME}_LINIdCallbackRegister( USART_LIN_CALLBACK callback, uintptr_t context)
{
    ${USART_INSTANCE_NAME?lower_case}LinObj.idCallback = callback;
    ${USART_INSTANCE_NAME?lower_case}LinObj.idContext = context;
}
</#if>

<#if USART_LIN_LINTC_INTERRUPT_ENABLE == true>
void ${USART_INSTANCE_NAME}_LINTcCallbackRegister( USART_LIN_CALLBACK callback, uintptr_t context)
{
    ${USART_INSTANCE_NAME?lower_case}LinObj.tranferCallback = callback;
    ${USART_INSTANCE_NAME?lower_case}LinObj.tranferContext = context;
}
</#if>

<#if USART_LIN_LINBK_INTERRUPT_ENABLE == true>
void ${USART_INSTANCE_NAME}_LINBreakCallbackRegister( USART_LIN_CALLBACK callback, uintptr_t context)
{
    ${USART_INSTANCE_NAME?lower_case}LinObj.breakCallback = callback;
    ${USART_INSTANCE_NAME?lower_case}LinObj.breakContext = context;
}
</#if>
</#if>

</#if>