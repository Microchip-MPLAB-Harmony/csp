/*******************************************************************************
  ${USART_INSTANCE_NAME} SPI PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${USART_INSTANCE_NAME?lower_case}_spi.c

  Summary:
    ${USART_INSTANCE_NAME} SPI PLIB Implementation File

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
#include "plib_${USART_INSTANCE_NAME?lower_case}_spi.h"

// *****************************************************************************
// *****************************************************************************
// Section: ${USART_INSTANCE_NAME} SPI Implementation
// *****************************************************************************
// *****************************************************************************
<#if USART_SPI_INTERRUPT_MODE == true >
static USART_SPI_OBJECT ${USART_INSTANCE_NAME?lower_case}SPIObj;

<#if USE_USART_SPI_DMA?? && USE_USART_SPI_DMA == true>

static uint8_t ${USART_INSTANCE_NAME}_SPI_DummyDataBuffer[512];

static void ${USART_INSTANCE_NAME}_SPI_SetupDMA( void* pTransmitData, void* pReceiveData, size_t size )
{
    /* Always set up the rx channel first */
    ${USART_INSTANCE_NAME}_REGS->US_RPR = (uint32_t) pReceiveData;
    ${USART_INSTANCE_NAME}_REGS->US_RCR = (uint32_t) size;
    ${USART_INSTANCE_NAME}_REGS->US_TPR = (uint32_t) pTransmitData;
    ${USART_INSTANCE_NAME}_REGS->US_TCR = (uint32_t) size;
    ${USART_INSTANCE_NAME}_REGS->US_PTCR = US_PTCR_RXTEN_Msk | US_PTCR_TXTEN_Msk;
    ${USART_INSTANCE_NAME}_REGS->US_IER = US_IER_SPI_ENDRX_Msk;
}
</#if>
</#if>

void ${USART_INSTANCE_NAME}_SPI_Initialize( void )
{
    /* Configure ${USART_INSTANCE_NAME} mode to SPI Master (0x0E) */
    ${USART_INSTANCE_NAME}_REGS->US_MR = US_MR_SPI_USART_MODE(US_MR_SPI_USART_MODE_SPI_MASTER_Val);

    /* Reset SPI RX, SPI TX and SPI status */
    ${USART_INSTANCE_NAME}_REGS->US_CR = (US_CR_SPI_RSTRX_Msk | US_CR_SPI_RSTTX_Msk | US_CR_SPI_RSTSTA_Msk);

    /* Configure clock source, clock phase, clock polarity and CKO = 1 */
    ${USART_INSTANCE_NAME}_REGS->US_MR |= (US_MR_USART_USCLKS_${USART_CLK_SRC} | US_MR_SPI_CHRL(US_MR_SPI_CHRL_8_BIT_Val) | US_MR_SPI_CPHA(${USART_SPI_CLOCK_PHASE}) | US_MR_SPI_CPOL(${USART_SPI_CLOCK_POLARITY}) | US_MR_SPI_CLKO(1));

    /* Enable TX and RX */
    ${USART_INSTANCE_NAME}_REGS->US_CR = (US_CR_SPI_RXEN_Msk | US_CR_SPI_TXEN_Msk);

    /* Configure ${USART_INSTANCE_NAME} Baud Rate */
    ${USART_INSTANCE_NAME}_REGS->US_BRGR = US_BRGR_CD(${USART_SPI_BRG_VALUE});

    /* Initialize instance object */
<#if USART_SPI_INTERRUPT_MODE == true >
    ${USART_INSTANCE_NAME?lower_case}SPIObj.callback = NULL;
    ${USART_INSTANCE_NAME?lower_case}SPIObj.context = (uintptr_t)0;
    ${USART_INSTANCE_NAME?lower_case}SPIObj.transferIsBusy = false;
</#if>
}

bool ${USART_INSTANCE_NAME}_SPI_TransferSetup( USART_SPI_TRANSFER_SETUP * setup, uint32_t spiSourceClock )
{
    uint32_t clockDivider;

    if ((setup == NULL) || (setup->clockFrequency == 0))
    {
        return false;
    }

    if(spiSourceClock == 0)
    {
        // Fetch Master Clock Frequency directly
        spiSourceClock = ${USART_CLOCK_FREQ}UL;
    }

    clockDivider = spiSourceClock/setup->clockFrequency;

    if(clockDivider < 6)
    {
        clockDivider = 6;
    }
    else if(clockDivider > 65535)
    {
        clockDivider = 65535;
    }

    ${USART_INSTANCE_NAME}_REGS->US_MR = ((${USART_INSTANCE_NAME}_REGS->US_MR & ~US_MR_SPI_CPOL_Msk) | (uint32_t)setup->clockPolarity);
    ${USART_INSTANCE_NAME}_REGS->US_MR = ((${USART_INSTANCE_NAME}_REGS->US_MR & ~US_MR_SPI_CPHA_Msk) | (uint32_t)setup->clockPhase);
    ${USART_INSTANCE_NAME}_REGS->US_MR = ((${USART_INSTANCE_NAME}_REGS->US_MR & ~US_MR_SPI_CHRL_Msk) | (uint32_t)setup->dataBits);

    ${USART_INSTANCE_NAME}_REGS->US_BRGR = ((${USART_INSTANCE_NAME}_REGS->US_BRGR & ~US_BRGR_CD_Msk) | US_BRGR_CD(clockDivider));

    return true;
}

<#if USART_SPI_INTERRUPT_MODE == false >
bool ${USART_INSTANCE_NAME}_SPI_WriteRead( void* pTransmitData, size_t txSize, void* pReceiveData, size_t rxSize )
{
    size_t txCount = 0;
    size_t rxCount = 0;
    size_t dummySize = 0;
    uint8_t receivedData;
    uint32_t dummyData;
    bool isSuccess = false;

    /* Verify the request */
    if (((txSize > 0) && (pTransmitData != NULL)) || ((rxSize > 0) && (pReceiveData != NULL)))
    {
        if (pTransmitData == NULL)
        {
            txSize = 0;
        }
        if (pReceiveData == NULL)
        {
            rxSize = 0;
        }

        /* Reset over-run error if any */
        ${USART_INSTANCE_NAME}_REGS->US_CR = US_CR_SPI_RSTSTA_Msk;

        /* Flush out any unread data in SPI read buffer */
        if (${USART_INSTANCE_NAME}_REGS->US_CSR & US_CSR_SPI_RXRDY_Msk)
        {
            dummyData = ${USART_INSTANCE_NAME}_REGS->US_RHR;
            (void)dummyData;
        }

        if (rxSize > txSize)
        {
            dummySize = rxSize - txSize;
        }

        /* Make sure TXRDY is set */
        while(!(${USART_INSTANCE_NAME}_REGS->US_CSR & US_CSR_SPI_TXRDY_Msk));

        <#if USART_SPI_CHIP_SELECT != "GPIO">
        /* Force Chip Select */
        ${USART_INSTANCE_NAME}_REGS->US_CR = US_CR_SPI_FCS_Msk;
        </#if>

        while ((txCount != txSize) || (dummySize != 0))
        {
            if (txCount != txSize)
            {
                ${USART_INSTANCE_NAME}_REGS->US_THR = ((uint8_t*)pTransmitData)[txCount++];
            }
            else if (dummySize > 0)
            {
                ${USART_INSTANCE_NAME}_REGS->US_THR = 0x${USART_SPI_DUMMY_DATA};
                dummySize--;
            }

            if (rxCount == rxSize)
            {
                /* For transmit only request (or all data received), wait for TXRDY to set */
                while(!(${USART_INSTANCE_NAME}_REGS->US_CSR & US_CSR_SPI_TXRDY_Msk));
            }
            else
            {
                /* If data pending to be read, wait for RXRDY to set */
                while(!(${USART_INSTANCE_NAME}_REGS->US_CSR & US_CSR_SPI_RXRDY_Msk));

                receivedData = (uint8_t)${USART_INSTANCE_NAME}_REGS->US_RHR;

                if (rxCount < rxSize)
                {
                    ((uint8_t*)pReceiveData)[rxCount++] = receivedData;
                }
            }
        }

        /* Make sure no data is pending in the shift register */
        while (!(${USART_INSTANCE_NAME}_REGS->US_CSR & US_CSR_SPI_TXEMPTY_Msk));

        <#if USART_SPI_CHIP_SELECT != "GPIO">
        /* Release Chip Select */
        ${USART_INSTANCE_NAME}_REGS->US_CR = US_CR_SPI_RCS_Msk;
        </#if>

        isSuccess = true;
    }
    return isSuccess;
}
<#else>
bool ${USART_INSTANCE_NAME}_SPI_WriteRead( void* pTransmitData, size_t txSize, void* pReceiveData, size_t rxSize )
{
<#if USE_USART_SPI_DMA?? && USE_USART_SPI_DMA == true>
    bool isRequestAccepted = false;
    uint32_t size = 0;

    /* Verify the request */
    if((((txSize > 0) && (pTransmitData != NULL)) || ((rxSize > 0) && (pReceiveData != NULL))) && (${USART_INSTANCE_NAME?lower_case}SPIObj.transferIsBusy == false))
    {
        isRequestAccepted = true;

        ${USART_INSTANCE_NAME?lower_case}SPIObj.transferIsBusy = true;

        ${USART_INSTANCE_NAME?lower_case}SPIObj.txBuffer = pTransmitData;
        ${USART_INSTANCE_NAME?lower_case}SPIObj.rxBuffer = pReceiveData;
        ${USART_INSTANCE_NAME?lower_case}SPIObj.txCount = txSize;
        ${USART_INSTANCE_NAME?lower_case}SPIObj.rxCount = rxSize;

        if ((txSize > 0) && (rxSize > 0))
        {
            /* Find the lower value among txSize and rxSize */
            (txSize >= rxSize) ? (size = rxSize) : (size = txSize);

            /* Calculate the remaining tx/rx bytes and total bytes transferred */
            ${USART_INSTANCE_NAME?lower_case}SPIObj.rxCount -= size;
            ${USART_INSTANCE_NAME?lower_case}SPIObj.txCount -= size;
            ${USART_INSTANCE_NAME?lower_case}SPIObj.nBytesTransferred = size;

            ${USART_INSTANCE_NAME}_SPI_SetupDMA(pTransmitData, pReceiveData, size);
        }
        else
        {
            if (rxSize > 0)
            {
                /* txSize is 0. Need to use the dummy data buffer for transmission.
                 * Find out the max data that can be received, given the limited size of the dummy data buffer.
                 */
                (rxSize > sizeof(${USART_INSTANCE_NAME}_SPI_DummyDataBuffer)) ?
                    (size = sizeof(${USART_INSTANCE_NAME}_SPI_DummyDataBuffer)): (size = rxSize);

                /* Calculate the remaining rx bytes and total bytes transferred */
                ${USART_INSTANCE_NAME?lower_case}SPIObj.rxCount -= size;
                ${USART_INSTANCE_NAME?lower_case}SPIObj.nBytesTransferred = size;

                ${USART_INSTANCE_NAME}_SPI_SetupDMA(${USART_INSTANCE_NAME}_SPI_DummyDataBuffer, pReceiveData, size);
            }
            else
            {
                /* rxSize is 0. Need to use the dummy data buffer for reception.
                 * Find out the max data that can be transmitted, given the limited size of the dummy data buffer.
                 */
                (txSize > sizeof(${USART_INSTANCE_NAME}_SPI_DummyDataBuffer)) ?
                    (size = sizeof(${USART_INSTANCE_NAME}_SPI_DummyDataBuffer)): (size = txSize);

                /* Calculate the remaining tx bytes and total bytes transferred */
                ${USART_INSTANCE_NAME?lower_case}SPIObj.txCount -= size;
                ${USART_INSTANCE_NAME?lower_case}SPIObj.nBytesTransferred = size;

                ${USART_INSTANCE_NAME}_SPI_SetupDMA(pTransmitData, ${USART_INSTANCE_NAME}_SPI_DummyDataBuffer, size);
            }
        }
    }

    return isRequestAccepted;
<#else>
    bool isRequestAccepted = false;
    uint32_t dummyData;

    /* Verify the request */
    if((((txSize > 0) && (pTransmitData != NULL)) || ((rxSize > 0) && (pReceiveData != NULL))) && (${USART_INSTANCE_NAME?lower_case}SPIObj.transferIsBusy == false))
    {
        isRequestAccepted = true;

        ${USART_INSTANCE_NAME?lower_case}SPIObj.transferIsBusy = true;
        ${USART_INSTANCE_NAME?lower_case}SPIObj.txBuffer = pTransmitData;
        ${USART_INSTANCE_NAME?lower_case}SPIObj.rxBuffer = pReceiveData;
        ${USART_INSTANCE_NAME?lower_case}SPIObj.rxCount = 0;
        ${USART_INSTANCE_NAME?lower_case}SPIObj.txCount = 0;
        ${USART_INSTANCE_NAME?lower_case}SPIObj.dummySize = 0;

        if (pTransmitData != NULL)
        {
            ${USART_INSTANCE_NAME?lower_case}SPIObj.txSize = txSize;
        }
        else
        {
            ${USART_INSTANCE_NAME?lower_case}SPIObj.txSize = 0;
        }

        if (pReceiveData != NULL)
        {
            ${USART_INSTANCE_NAME?lower_case}SPIObj.rxSize = rxSize;
        }
        else
        {
            ${USART_INSTANCE_NAME?lower_case}SPIObj.rxSize = 0;
        }

        /* Reset over-run error if any */
        ${USART_INSTANCE_NAME}_REGS->US_CR = US_CR_SPI_RSTSTA_Msk;

        /* Flush out any unread data in SPI read buffer */
        if (${USART_INSTANCE_NAME}_REGS->US_CSR & US_CSR_SPI_RXRDY_Msk)
        {
            dummyData = ${USART_INSTANCE_NAME}_REGS->US_RHR;
            (void)dummyData;
        }

        if (${USART_INSTANCE_NAME?lower_case}SPIObj.rxSize > ${USART_INSTANCE_NAME?lower_case}SPIObj.txSize)
        {
            ${USART_INSTANCE_NAME?lower_case}SPIObj.dummySize = ${USART_INSTANCE_NAME?lower_case}SPIObj.rxSize - ${USART_INSTANCE_NAME?lower_case}SPIObj.txSize;
        }

        /* Start the first write here itself, rest will happen in ISR context */
        if ((${USART_INSTANCE_NAME}_REGS->US_MR & US_MR_SPI_CHRL_Msk) == US_MR_SPI_CHRL_8_BIT)
        {
            <#if USART_SPI_CHIP_SELECT != "GPIO">
            /* Force Chip Select */
            ${USART_INSTANCE_NAME}_REGS->US_CR = US_CR_SPI_FCS_Msk;
            </#if>

            if (${USART_INSTANCE_NAME?lower_case}SPIObj.txCount < ${USART_INSTANCE_NAME?lower_case}SPIObj.txSize)
            {
                ${USART_INSTANCE_NAME}_REGS->US_THR = *((uint8_t*)${USART_INSTANCE_NAME?lower_case}SPIObj.txBuffer);
                ${USART_INSTANCE_NAME?lower_case}SPIObj.txCount++;
            }
            else if (${USART_INSTANCE_NAME?lower_case}SPIObj.dummySize > 0)
            {
                ${USART_INSTANCE_NAME}_REGS->US_THR = (uint8_t)(0x${USART_SPI_DUMMY_DATA});
                ${USART_INSTANCE_NAME?lower_case}SPIObj.dummySize--;
            }
        }

        if (rxSize > 0)
        {
            /* Enable receive interrupt to complete the transfer in ISR context */
            ${USART_INSTANCE_NAME}_REGS->US_IER = US_IER_SPI_RXRDY_Msk;
        }
        else
        {
            /* Enable transmit interrupt to complete the transfer in ISR context */
            ${USART_INSTANCE_NAME}_REGS->US_IER = US_IER_SPI_TXRDY_Msk;
        }
    }

    return isRequestAccepted;
</#if>
}
</#if>

bool ${USART_INSTANCE_NAME}_SPI_Write( void* pTransmitData, size_t txSize )
{
    return(${USART_INSTANCE_NAME}_SPI_WriteRead(pTransmitData, txSize, NULL, 0));
}

bool ${USART_INSTANCE_NAME}_SPI_Read( void* pReceiveData, size_t rxSize )
{
    return(${USART_INSTANCE_NAME}_SPI_WriteRead(NULL, 0, pReceiveData, rxSize));
}

<#if USART_SPI_INTERRUPT_MODE == true >
bool ${USART_INSTANCE_NAME}_SPI_IsBusy( void )
{
    return ((${USART_INSTANCE_NAME?lower_case}SPIObj.transferIsBusy) || ((${USART_INSTANCE_NAME}_REGS->US_CSR & US_CSR_SPI_TXEMPTY_Msk) == 0));
}

void ${USART_INSTANCE_NAME}_SPI_CallbackRegister( USART_SPI_CALLBACK callback, uintptr_t context )
{
    ${USART_INSTANCE_NAME?lower_case}SPIObj.callback = callback;
    ${USART_INSTANCE_NAME?lower_case}SPIObj.context = context;
}

void ${USART_INSTANCE_NAME}_InterruptHandler( void )
{
<#if USE_USART_SPI_DMA?? && USE_USART_SPI_DMA == true>
    uint32_t size;
    uint32_t index;
<#else>
    uint32_t receivedData;
</#if>

    <#if USE_USART_SPI_DMA?? && USE_USART_SPI_DMA == true>
    if(${USART_INSTANCE_NAME?lower_case}SPIObj.rxCount > 0)
    {
        /* txPending is 0. Need to use the dummy data buffer for transmission.
         * Find out the max data that can be received, given the limited size of the dummy data buffer.
         */
        (${USART_INSTANCE_NAME?lower_case}SPIObj.rxCount > sizeof(${USART_INSTANCE_NAME}_SPI_DummyDataBuffer)) ?
            (size = sizeof(${USART_INSTANCE_NAME}_SPI_DummyDataBuffer)): (size = ${USART_INSTANCE_NAME?lower_case}SPIObj.rxCount);

        index = ${USART_INSTANCE_NAME?lower_case}SPIObj.nBytesTransferred;

        /* Calculate the remaining rx bytes and total bytes transferred */
        ${USART_INSTANCE_NAME?lower_case}SPIObj.rxCount -= size;
        ${USART_INSTANCE_NAME?lower_case}SPIObj.nBytesTransferred += size;

        ${USART_INSTANCE_NAME}_SPI_SetupDMA(${USART_INSTANCE_NAME}_SPI_DummyDataBuffer,(void *)&((uint8_t*)${USART_INSTANCE_NAME?lower_case}SPIObj.rxBuffer)[index], size);
    }
    else if(${USART_INSTANCE_NAME?lower_case}SPIObj.txCount > 0)
    {
        /* rxSize is 0. Need to use the dummy data buffer for reception.
         * Find out the max data that can be transmitted, given the limited size of the dummy data buffer.
         */
        (${USART_INSTANCE_NAME?lower_case}SPIObj.txCount > sizeof(${USART_INSTANCE_NAME}_SPI_DummyDataBuffer)) ?
            (size = sizeof(${USART_INSTANCE_NAME}_SPI_DummyDataBuffer)): (size = ${USART_INSTANCE_NAME?lower_case}SPIObj.txCount);

        index = ${USART_INSTANCE_NAME?lower_case}SPIObj.nBytesTransferred;

        /* Calculate the remaining rx bytes and total bytes transferred */
        ${USART_INSTANCE_NAME?lower_case}SPIObj.txCount -= size;
        ${USART_INSTANCE_NAME?lower_case}SPIObj.nBytesTransferred += size;

        ${USART_INSTANCE_NAME}_SPI_SetupDMA((void *)&((uint8_t*)${USART_INSTANCE_NAME?lower_case}SPIObj.txBuffer)[index], ${USART_INSTANCE_NAME}_SPI_DummyDataBuffer, size);
    }
    else
    {
        ${USART_INSTANCE_NAME?lower_case}SPIObj.transferIsBusy = false;

        <#if USART_SPI_CHIP_SELECT != "GPIO">
        /* Release Chip Select */
        ${USART_INSTANCE_NAME}_REGS->US_CR = US_CR_SPI_RCS_Msk;
        </#if>

        ${USART_INSTANCE_NAME}_REGS->US_PTCR = US_PTCR_RXTDIS_Msk | US_PTCR_TXTDIS_Msk;
        ${USART_INSTANCE_NAME}_REGS->US_IDR = US_IDR_SPI_ENDRX_Msk;

        if(${USART_INSTANCE_NAME?lower_case}SPIObj.callback != NULL)
        {
            ${USART_INSTANCE_NAME?lower_case}SPIObj.callback(${USART_INSTANCE_NAME?lower_case}SPIObj.context);
        }
    }

    <#else>

    if (${USART_INSTANCE_NAME}_REGS->US_CSR & US_CSR_SPI_RXRDY_Msk)
    {
        receivedData = ${USART_INSTANCE_NAME}_REGS->US_RHR;

        if (${USART_INSTANCE_NAME?lower_case}SPIObj.rxCount < ${USART_INSTANCE_NAME?lower_case}SPIObj.rxSize)
        {
            ((uint8_t*)${USART_INSTANCE_NAME?lower_case}SPIObj.rxBuffer)[${USART_INSTANCE_NAME?lower_case}SPIObj.rxCount++] = receivedData;
        }
    }

    if(${USART_INSTANCE_NAME}_REGS->US_CSR & US_CSR_SPI_TXRDY_Msk)
    {
        /* Disable the TXRDY interrupt. This will be enabled back if one or more
         * bytes are pending transmission */

        ${USART_INSTANCE_NAME}_REGS->US_IDR = US_IDR_SPI_TXRDY_Msk;

        if (${USART_INSTANCE_NAME?lower_case}SPIObj.txCount < ${USART_INSTANCE_NAME?lower_case}SPIObj.txSize)
        {
            ${USART_INSTANCE_NAME}_REGS->US_THR = ((uint8_t*)${USART_INSTANCE_NAME?lower_case}SPIObj.txBuffer)[${USART_INSTANCE_NAME?lower_case}SPIObj.txCount++];
        }
        else if (${USART_INSTANCE_NAME?lower_case}SPIObj.dummySize > 0)
        {
            ${USART_INSTANCE_NAME}_REGS->US_THR = (uint8_t)(0x${USART_SPI_DUMMY_DATA});
            ${USART_INSTANCE_NAME?lower_case}SPIObj.dummySize--;
        }

        if ((${USART_INSTANCE_NAME?lower_case}SPIObj.txCount == ${USART_INSTANCE_NAME?lower_case}SPIObj.txSize) && (${USART_INSTANCE_NAME?lower_case}SPIObj.dummySize == 0))
        {
            if (${USART_INSTANCE_NAME}_REGS->US_CSR & US_CSR_SPI_TXEMPTY_Msk)
            {
                /* Disable all interrupt sources - RXRDY, TXRDY and TXEMPTY */
                ${USART_INSTANCE_NAME}_REGS->US_IDR = (US_IDR_SPI_RXRDY_Msk | US_IDR_SPI_TXRDY_Msk | US_IDR_SPI_TXEMPTY_Msk);

                ${USART_INSTANCE_NAME?lower_case}SPIObj.transferIsBusy = false;

                <#if USART_SPI_CHIP_SELECT != "GPIO">
                /* Release Chip Select */
                ${USART_INSTANCE_NAME}_REGS->US_CR = US_CR_SPI_RCS_Msk;
                </#if>

                /* All characters are transmitted out and TX shift register is empty */
                if(${USART_INSTANCE_NAME?lower_case}SPIObj.callback != NULL)
                {
                    ${USART_INSTANCE_NAME?lower_case}SPIObj.callback(${USART_INSTANCE_NAME?lower_case}SPIObj.context);
                }
            }
            else
            {
                /* Enable TXEMPTY interrupt */
                ${USART_INSTANCE_NAME}_REGS->US_IER = US_IER_SPI_TXEMPTY_Msk;
            }
        }
        else if (${USART_INSTANCE_NAME?lower_case}SPIObj.rxCount == ${USART_INSTANCE_NAME?lower_case}SPIObj.rxSize)
        {
            /* Enable TXRDY interrupt as all the requested bytes are received
             * and can now make use of the internal transmit shift register.
             */
            ${USART_INSTANCE_NAME}_REGS->US_IDR = US_IDR_SPI_RXRDY_Msk;
            ${USART_INSTANCE_NAME}_REGS->US_IER = US_IER_SPI_TXRDY_Msk;
        }
    }
    </#if>
}
</#if>