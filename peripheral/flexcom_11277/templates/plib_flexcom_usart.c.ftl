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

// *****************************************************************************
// *****************************************************************************
// Section: ${FLEXCOM_INSTANCE_NAME} ${FLEXCOM_MODE} Implementation
// *****************************************************************************
// *****************************************************************************

#define FLEXCOM_USART_RHR_8BIT_REG      (*(volatile uint8_t* const)((USART${FLEXCOM_INSTANCE_NUMBER}_BASE_ADDRESS + US_RHR_REG_OFST)))
#define FLEXCOM_USART_RHR_9BIT_REG      (*(volatile uint16_t* const)((USART${FLEXCOM_INSTANCE_NUMBER}_BASE_ADDRESS + US_RHR_REG_OFST)))

#define FLEXCOM_USART_THR_8BIT_REG      (*(volatile uint8_t* const)((USART${FLEXCOM_INSTANCE_NUMBER}_BASE_ADDRESS + US_THR_REG_OFST)))
#define FLEXCOM_USART_THR_9BIT_REG      (*(volatile uint16_t* const)((USART${FLEXCOM_INSTANCE_NUMBER}_BASE_ADDRESS + US_THR_REG_OFST)))

<#if FLEXCOM_USART_INTERRUPT_MODE_ENABLE == true>
static FLEXCOM_USART_OBJECT ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj;
</#if>

void static ${FLEXCOM_INSTANCE_NAME}_USART_ErrorClear( void )
{
    if ((USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_CSR & (US_CSR_OVRE_Msk | US_CSR_FRAME_Msk | US_CSR_PARE_Msk)) != 0U)
    {
        USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_CR = US_CR_RSTSTA_Msk;

        /* Flush existing error bytes from the RX FIFO */
        while ((USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_CSR & US_CSR_RXRDY_Msk) != 0U)
        {
            (void)USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_RHR;
        }
    }
}

<#if FLEXCOM_USART_INTERRUPT_MODE_ENABLE == true>

<#if !(USE_USART_RECEIVE_DMA??) || (USE_USART_RECEIVE_DMA == false)>
void static ${FLEXCOM_INSTANCE_NAME}_USART_ISR_RX_Handler( void )
{
    if(${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxBusyStatus == true)
    {
        while (((USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_CSR & US_CSR_RXRDY_Msk) != 0U) && (${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxSize > ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxProcessedSize))
        {
            if ((USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_MR & US_MR_MODE9_Msk) != 0U)
            {
                ((uint16_t*)${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxBuffer)[${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxProcessedSize] = (FLEXCOM_USART_RHR_9BIT_REG & (uint16_t)US_RHR_RXCHR_Msk);
            }
            else
            {
                ((uint8_t*)${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxBuffer)[${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxProcessedSize] = FLEXCOM_USART_RHR_8BIT_REG;
            }
            ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxProcessedSize++;
        }

        /* Check if the buffer is done */
        if(${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxProcessedSize >= ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxSize)
        {
            ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxBusyStatus = false;

            /* Disable Read, Overrun, Parity and Framing error interrupts */
            USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_IDR = (US_IDR_RXRDY_Msk | US_IDR_FRAME_Msk | US_IDR_PARE_Msk | US_IDR_OVRE_Msk);

            if(${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxCallback != NULL)
            {
                ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxCallback(${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxContext);
            }
        }
    }
    else
    {
        /* Nothing to process */
    }
}

</#if>
<#if !(USE_USART_TRANSMIT_DMA??) || (USE_USART_TRANSMIT_DMA == false)>
void static ${FLEXCOM_INSTANCE_NAME}_USART_ISR_TX_Handler( void )
{
    if(${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txBusyStatus == true)
    {
        while( ((USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_CSR & US_CSR_TXRDY_Msk) != 0U) && (${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txSize > ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txProcessedSize) )
        {
            if ((USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_MR & US_MR_MODE9_Msk) != 0U)
            {
                FLEXCOM_USART_THR_9BIT_REG = ((uint16_t*)${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txBuffer)[${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txProcessedSize] & (uint16_t)US_THR_TXCHR_Msk;
            }
            else
            {
                FLEXCOM_USART_THR_8BIT_REG = ((uint8_t*)${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txBuffer)[${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txProcessedSize];
            }
            ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txProcessedSize++;
        }

        /* Check if the buffer is done */
        if(${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txProcessedSize >= ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txSize)
        {
            ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txBusyStatus = false;

            USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_IDR = US_IDR_TXRDY_Msk;

            if(${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txCallback != NULL)
            {
                ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txCallback(${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txContext);
            }
        }
    }
    else
    {
        /* Nothing to process */
    }
}
</#if>

void ${FLEXCOM_INSTANCE_NAME}_InterruptHandler( void )
{
    /* Channel status */
    uint32_t channelStatus = USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_CSR;

    <#if (USE_USART_TRANSMIT_DMA?? && USE_USART_TRANSMIT_DMA == true) || (USE_USART_RECEIVE_DMA?? && USE_USART_RECEIVE_DMA == true)>
    USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_PTCR = US_PTCR_ERRCLR_Msk;
    </#if>

    <#if USE_USART_RECEIVE_DMA?? && USE_USART_RECEIVE_DMA == true>
    if (((USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_PTSR & US_PTSR_RXTEN_Msk) != 0U) && ((channelStatus & US_CSR_ENDRX_Msk) != 0U))
    {
        if(${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxBusyStatus == true)
        {
            ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxBusyStatus = false;
            USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_PTCR = US_PTCR_RXTDIS_Msk;
            USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_IDR = US_IDR_ENDRX_Msk;

            if( ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxCallback != NULL )
            {
                ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxCallback(${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxContext);
            }
        }
    }
    <#else>
    /* Error status */
    uint32_t errorStatus = (channelStatus & (US_CSR_OVRE_Msk | US_CSR_FRAME_Msk | US_CSR_PARE_Msk));

    if(errorStatus != 0U)
    {
        /* Save error to report it later */
        ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.errorStatus = (FLEXCOM_USART_ERROR)errorStatus;

        /* Clear error flags and flush the error data */
        ${FLEXCOM_INSTANCE_NAME}_USART_ErrorClear();

        ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxBusyStatus = false;

        /* Disable Read, Overrun, Parity and Framing error interrupts */
        USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_IDR = (US_IDR_RXRDY_Msk | US_IDR_FRAME_Msk | US_IDR_PARE_Msk | US_IDR_OVRE_Msk);

        /* USART errors are normally associated with the receiver, hence calling receiver context */

        if( ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxCallback != NULL )
        {
            ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxCallback(${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxContext);
        }
    }

    /* Receiver status */
    if((channelStatus & US_CSR_RXRDY_Msk) != 0U)
    {
        ${FLEXCOM_INSTANCE_NAME}_USART_ISR_RX_Handler();
    }
    </#if>

    <#if USE_USART_TRANSMIT_DMA?? && USE_USART_TRANSMIT_DMA == true>
    if (((USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_PTSR & US_PTSR_TXTEN_Msk) != 0U) && ((channelStatus & US_CSR_ENDTX_Msk) != 0U))
    {
        if(${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txBusyStatus == true)
        {
            ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txBusyStatus = false;
            USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_PTCR = US_PTCR_TXTDIS_Msk;
            USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_IDR = US_IDR_ENDTX_Msk;

            if( ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txCallback != NULL )
            {
                ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txCallback(${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txContext);
            }
        }
    }
    <#else>
    /* Transmitter status */
    if((channelStatus & US_CSR_TXRDY_Msk) != 0U)
    {
        ${FLEXCOM_INSTANCE_NAME}_USART_ISR_TX_Handler();
    }
    </#if>
}
</#if>

void ${FLEXCOM_INSTANCE_NAME}_USART_Initialize( void )
{
    /* Set FLEXCOM USART operating mode */
    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEXCOM_MR = FLEXCOM_MR_OPMODE_USART;

    /* Reset ${FLEXCOM_INSTANCE_NAME} USART */
    USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_CR = (US_CR_RSTRX_Msk | US_CR_RSTTX_Msk | US_CR_RSTSTA_Msk);

    /* Enable ${FLEXCOM_INSTANCE_NAME} USART */
    USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_CR = (US_CR_TXEN_Msk | US_CR_RXEN_Msk);

    /* Configure ${FLEXCOM_INSTANCE_NAME} USART mode */
    USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_MR = ((US_MR_USCLKS_${FLEXCOM_USART_MR_USCLKS}) ${(FLEX_USART_MR_MODE9 == true)?then('| US_MR_MODE9_Msk', '| US_MR_CHRL${FLEX_USART_MR_CHRL}')} | US_MR_PAR_${FLEX_USART_MR_PAR} | US_MR_NBSTOP${FLEX_USART_MR_NBSTOP} | (${FLEXCOM_USART_MR_OVER}UL << US_MR_OVER_Pos));

    /* Configure ${FLEXCOM_INSTANCE_NAME} USART Baud Rate */
    USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_BRGR = US_BRGR_CD(${BRG_VALUE}) | US_BRGR_FP(${FP_VALUE});
<#if FLEXCOM_USART_INTERRUPT_MODE_ENABLE == true>

    /* Initialize instance object */
    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxBuffer = NULL;
    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxSize = 0;
    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxProcessedSize = 0;
    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxBusyStatus = false;
    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxCallback = NULL;
    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.errorStatus = FLEXCOM_USART_ERROR_NONE;
    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txBuffer = NULL;
    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txSize = 0;
    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txProcessedSize = 0;
    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txBusyStatus = false;
    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txCallback = NULL;
</#if>
}

<#if FLEXCOM_USART_INTERRUPT_MODE_ENABLE == true>
FLEXCOM_USART_ERROR ${FLEXCOM_INSTANCE_NAME}_USART_ErrorGet( void )
{
    FLEXCOM_USART_ERROR errorStatus = ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.errorStatus;

    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.errorStatus = FLEXCOM_USART_ERROR_NONE;

    /* All errors are cleared, but send the previous error state */
    return errorStatus;
}
<#else>
FLEXCOM_USART_ERROR ${FLEXCOM_INSTANCE_NAME}_USART_ErrorGet( void )
{
    FLEXCOM_USART_ERROR errors = FLEXCOM_USART_ERROR_NONE;
    uint32_t status = USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_CSR;

    /* Collect all errors */
    if((status & US_CSR_OVRE_Msk) != 0U)
    {
        errors = FLEXCOM_USART_ERROR_OVERRUN;
    }

    if((status & US_CSR_PARE_Msk) != 0U)
    {
        errors |= FLEXCOM_USART_ERROR_PARITY;
    }

    if((status & US_CSR_FRAME_Msk) != 0U)
    {
        errors |= FLEXCOM_USART_ERROR_FRAMING;
    }

    if(errors != FLEXCOM_USART_ERROR_NONE)
    {
        ${FLEXCOM_INSTANCE_NAME}_USART_ErrorClear();
    }

    /* All errors are cleared, but send the previous error state */
    return errors;
}
</#if>

static void ${FLEXCOM_INSTANCE_NAME}_USART_BaudCalculate(uint32_t srcClkFreq, uint32_t reqBaud, uint8_t overSamp, uint32_t* cd, uint32_t* fp, uint32_t* baudError)
{
    uint32_t actualBaud = 0U;

    *cd = srcClkFreq / (reqBaud * 8U * (2U - overSamp));

    if (*cd > 0U)
    {
        *fp = ((srcClkFreq / (reqBaud * (2U - (uint32_t)overSamp))) - ((*cd) * 8U));
        actualBaud = (srcClkFreq / (((*cd) * 8U) + (*fp))) / (2U - (uint32_t)overSamp);
        *baudError = ((100U * actualBaud)/reqBaud) - 100U;
    }
}

bool ${FLEXCOM_INSTANCE_NAME}_USART_SerialSetup( FLEXCOM_USART_SERIAL_SETUP *setup, uint32_t srcClkFreq )
{
    uint32_t baud = 0U;
    uint32_t overSampVal = 0U;
    uint32_t usartMode;
    uint32_t cd0, fp0, cd1, fp1, baudError0, baudError1;
    bool status = false;

    cd0 = 0U;
    fp0 = 0U;
    cd1 = 0U;
    fp1 = 0U;
    baudError0 = 0U;
    baudError1 = 0U;

<#if FLEXCOM_USART_INTERRUPT_MODE_ENABLE == true>
    if((${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxBusyStatus == true) || (${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txBusyStatus == true))
    {
        /* Transaction is in progress, so return without updating settings */
        return false;
    }

</#if>
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

        if ( !(cd0 > 0U && cd0 <= 65535U) && !(cd1 > 0U && cd1 <= 65535U) )
        {
            /* Requested baud cannot be generated with current clock settings */
            return status;
        }

        if ( (cd0 > 0U && cd0 <= 65535U) && (cd1 > 0U && cd1 <= 65535U) )
        {
            /* Requested baud can be generated with both 8x and 16x oversampling. Select the one with less % error. */
            if (baudError1 < baudError0)
            {
                cd0 = cd1;
                fp0 = fp1;
                overSampVal = (1UL << US_MR_OVER_Pos) & US_MR_OVER_Msk;
            }
        }
        else
        {
            /* Requested baud can be generated with either with 8x oversampling or with 16x oversampling. Select valid one. */
            if (cd1 > 0U && cd1 <= 65535U)
            {
                cd0 = cd1;
                fp0 = fp1;
                overSampVal = (1UL << US_MR_OVER_Pos) & US_MR_OVER_Msk;
            }
        }

        /* Configure ${FLEXCOM_INSTANCE_NAME} USART mode */
        usartMode = USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_MR;
        usartMode &= ~(US_MR_CHRL_Msk | US_MR_MODE9_Msk | US_MR_PAR_Msk | US_MR_NBSTOP_Msk | US_MR_OVER_Msk);
        USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_MR = usartMode | ((uint32_t)setup->dataWidth | (uint32_t)setup->parity | (uint32_t)setup->stopBits | overSampVal);

        /* Configure ${FLEXCOM_INSTANCE_NAME} USART Baud Rate */
        USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_BRGR = US_BRGR_CD(cd0) | US_BRGR_FP(fp0);
        status = true;
    }

    return status;
}

bool ${FLEXCOM_INSTANCE_NAME}_USART_Read( void *pBuffer, const size_t size )
{
    bool status = false;
<#if FLEXCOM_USART_INTERRUPT_MODE_ENABLE == false>
    uint32_t errorStatus = 0U;
    size_t processedSize = 0U;
</#if>

    if(pBuffer != NULL)
    {
<#if FLEXCOM_USART_INTERRUPT_MODE_ENABLE == false>
        /* Clear errors that may have got generated when there was no active read request pending */
        ${FLEXCOM_INSTANCE_NAME}_USART_ErrorClear();

        while( size > processedSize )
        {
            while ((USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_CSR & US_CSR_RXRDY_Msk) == 0U)
            {
                /* Wait for RXRDY flag */
            }

            /* Error status */
            errorStatus = (USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_CSR & (US_CSR_OVRE_Msk | US_CSR_FRAME_Msk | US_CSR_PARE_Msk));

            if(errorStatus != 0U)
            {
                break;
            }

            if ((USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_MR & US_MR_MODE9_Msk) != 0U)
            {
                ((uint16_t*)pBuffer)[processedSize] = FLEXCOM_USART_RHR_9BIT_REG & (uint16_t)US_RHR_RXCHR_Msk;
            }
            else
            {
                ((uint8_t*)pBuffer)[processedSize] = FLEXCOM_USART_RHR_8BIT_REG;
            }

            processedSize++;
        }

        if(size == processedSize)
        {
            status = true;
        }

<#else>
        /* Check if receive request is in progress */
        if(${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxBusyStatus == false)
        {
            /* Clear errors that may have got generated when there was no active read request pending */
            ${FLEXCOM_INSTANCE_NAME}_USART_ErrorClear();

            status = true;

            ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxBuffer = pBuffer;
            ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxSize = size;
            ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxProcessedSize = 0;
            ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxBusyStatus = true;
            ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.errorStatus = FLEXCOM_USART_ERROR_NONE;

            <#if USE_USART_RECEIVE_DMA?? && USE_USART_RECEIVE_DMA == true>
            USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_RPR = (uint32_t)(uint8_t*)pBuffer;
            USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_RCR = (uint32_t) size;
            USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_PTCR = US_PTCR_RXTEN_Msk;
            USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_IER = US_IER_ENDRX_Msk;
            <#else>

            /* Enable Read, Overrun, Parity and Framing error interrupts */
            USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_IER = (US_IER_RXRDY_Msk | US_IER_FRAME_Msk | US_IER_PARE_Msk | US_IER_OVRE_Msk);
            </#if>
        }
</#if>
    }

    return status;
}

bool ${FLEXCOM_INSTANCE_NAME}_USART_Write( void *pBuffer, const size_t size )
{
    bool status = false;
<#if FLEXCOM_USART_INTERRUPT_MODE_ENABLE == false>
    size_t processedSize = 0U;
</#if>

    if(pBuffer != NULL)
    {
<#if FLEXCOM_USART_INTERRUPT_MODE_ENABLE == false>
        while( size > processedSize )
        {
            while ((USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_CSR & US_CSR_TXRDY_Msk) == 0U)
            {
                /* Do Nothing */
            }

            if ((USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_MR & US_MR_MODE9_Msk) != 0U)
            {
                FLEXCOM_USART_THR_9BIT_REG = ((uint16_t*)pBuffer)[processedSize] & (uint16_t)US_THR_TXCHR_Msk;
            }
            else
            {
                FLEXCOM_USART_THR_8BIT_REG = ((uint8_t*)pBuffer)[processedSize];
            }
            processedSize++;
        }
        status = true;
<#else>
        /* Check if transmit request is in progress */
        if(${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txBusyStatus == false)
        {
            status = true;

            ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txBuffer = pBuffer;
            ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txSize = size;
            ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txProcessedSize = 0;
            ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txBusyStatus = true;

            <#if USE_USART_TRANSMIT_DMA?? && USE_USART_TRANSMIT_DMA == true>

            USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_TPR = (uint32_t)(uint8_t*)pBuffer;
            USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_TCR = (uint32_t) size;
            USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_PTCR = US_PTCR_TXTEN_Msk;
            USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_IER = US_IER_ENDTX_Msk;

            <#else>

            /* Initiate the transfer by sending first byte */
            while (((USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_CSR & US_CSR_TXRDY_Msk) != 0U) && (${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txProcessedSize < ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txSize))
            {
                if ((USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_MR & US_MR_MODE9_Msk) != 0U)
                {
                    FLEXCOM_USART_THR_9BIT_REG = ((uint16_t*)pBuffer)[${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txProcessedSize] & (uint16_t)US_THR_TXCHR_Msk;
                }
                else
                {
                    FLEXCOM_USART_THR_8BIT_REG = ((uint8_t*)pBuffer)[${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txProcessedSize];
                }
                ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txProcessedSize++;
            }
            USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_IER = US_IER_TXRDY_Msk;
            </#if>
        }
</#if>
    }
    return status;
}

<#if FLEXCOM_USART_INTERRUPT_MODE_ENABLE == true>
void ${FLEXCOM_INSTANCE_NAME}_USART_WriteCallbackRegister( FLEXCOM_USART_CALLBACK callback, uintptr_t context )
{
    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txCallback = callback;
    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txContext = context;
}

void ${FLEXCOM_INSTANCE_NAME}_USART_ReadCallbackRegister( FLEXCOM_USART_CALLBACK callback, uintptr_t context )
{
    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxCallback = callback;
    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxContext = context;
}

bool ${FLEXCOM_INSTANCE_NAME}_USART_WriteIsBusy( void )
{
    return ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txBusyStatus;
}

bool ${FLEXCOM_INSTANCE_NAME}_USART_ReadIsBusy( void )
{
    return ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxBusyStatus;
}

size_t ${FLEXCOM_INSTANCE_NAME}_USART_WriteCountGet( void )
{
    <#if USE_USART_TRANSMIT_DMA?? && USE_USART_TRANSMIT_DMA == true>
    return (${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txSize - USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_TCR);
    <#else>
    return ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txProcessedSize;
    </#if>
}

size_t ${FLEXCOM_INSTANCE_NAME}_USART_ReadCountGet( void )
{
    <#if USE_USART_RECEIVE_DMA?? && USE_USART_RECEIVE_DMA == true>
    return (${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxSize - USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_RCR);
    <#else>
    return ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxProcessedSize;
    </#if>
}

bool ${FLEXCOM_INSTANCE_NAME}_USART_ReadAbort(void)
{
    if (${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxBusyStatus == true)
    {
        <#if USE_USART_RECEIVE_DMA?? && USE_USART_RECEIVE_DMA == true>
        /* Disable PDA channel transfer */
        USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_RCR = (uint32_t) 0U;
        USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_PTCR = US_PTCR_RXTDIS_Msk;
        USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_IDR = US_IDR_ENDRX_Msk;
        <#else>
        /* Disable Read, Overrun, Parity and Framing error interrupts */
        USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_IDR = (US_IDR_RXRDY_Msk | US_IDR_FRAME_Msk | US_IDR_PARE_Msk | US_IDR_OVRE_Msk);
        </#if>

        ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxBusyStatus = false;

        /* If required application should read the num bytes processed prior to calling the read abort API */
        ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxSize = 0;
        ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxProcessedSize = 0;
    }

    return true;
}

</#if>
<#if FLEXCOM_USART_INTERRUPT_MODE_ENABLE == false>
uint8_t ${FLEXCOM_INSTANCE_NAME}_USART_ReadByte( void )
{
    return (uint8_t)(USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_RHR & US_RHR_RXCHR_Msk);
}

void ${FLEXCOM_INSTANCE_NAME}_USART_WriteByte( uint8_t data )
{
    while ((USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_CSR & US_CSR_TXRDY_Msk) == 0U)
    {
        /* Wait for TXRDY flag to rise */
    }
    USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_THR = (US_THR_TXCHR(data) & US_THR_TXCHR_Msk);
}

bool ${FLEXCOM_INSTANCE_NAME}_USART_TransmitterIsReady( void )
{
    bool status = false;

    if ((USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_CSR & US_CSR_TXRDY_Msk) != 0U)
    {
        status = true;
    }

    return status;
}

bool ${FLEXCOM_INSTANCE_NAME}_USART_ReceiverIsReady( void )
{
    bool status = false;

    if ((USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_CSR & US_CSR_RXRDY_Msk) != 0U)
    {
        status = true;
    }

    return status;
}
</#if>

bool ${FLEXCOM_INSTANCE_NAME}_USART_TransmitComplete( void )
{
    bool status = false;

    if ((USART${FLEXCOM_INSTANCE_NUMBER}_REGS->US_CSR & US_CSR_TXEMPTY_Msk) != 0U)
    {
        status = true;
    }

    return status;
}