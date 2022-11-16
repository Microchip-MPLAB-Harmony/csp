/*******************************************************************************
  ${FLEXCOM_INSTANCE_NAME} SPI PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${FLEXCOM_INSTANCE_NAME?lower_case}_spi_master.c

  Summary:
    ${FLEXCOM_INSTANCE_NAME} SPI Master PLIB Implementation File.

  Description:
    This file defines the interface to the FLEXCOM SPI peripheral library.
    This library provides access to and control of the associated
    peripheral instance.

  Remarks:
    None.

*******************************************************************************/

// DOM-IGNORE-BEGIN
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
// DOM-IGNORE-END

#include "plib_${FLEXCOM_INSTANCE_NAME?lower_case}_spi_master.h"
<#if core.CoreSysIntFile == true>
#include "interrupts.h"
</#if>

#define FLEXCOM_SPI_TDR_8BIT_REG      (*(volatile uint8_t* const)((${FLEXCOM_INSTANCE_NAME}_BASE_ADDRESS + FLEX_SPI_TDR_REG_OFST)))

#define FLEXCOM_SPI_TDR_9BIT_REG      (*(volatile uint16_t* const)((${FLEXCOM_INSTANCE_NAME}_BASE_ADDRESS + FLEX_SPI_TDR_REG_OFST)))



#define FLEXCOM_SPI_RDR_8BIT_REG      (*(volatile uint8_t* const)((${FLEXCOM_INSTANCE_NAME}_BASE_ADDRESS + FLEX_SPI_RDR_REG_OFST)))

#define FLEXCOM_SPI_RDR_9BIT_REG      (*(volatile uint16_t* const)((${FLEXCOM_INSTANCE_NAME}_BASE_ADDRESS + FLEX_SPI_RDR_REG_OFST)))
// *****************************************************************************
// *****************************************************************************
// Section: ${FLEXCOM_INSTANCE_NAME} SPI Implementation
// *****************************************************************************
// *****************************************************************************
<#if SPI_INTERRUPT_MODE == true>
/* Global object to save FLEXCOM SPI Exchange related data */
static FLEXCOM_SPI_OBJECT ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj;

<#if USE_SPI_DMA?? && USE_SPI_DMA == true>
static uint8_t dummyDataBuffer[512];

static void setupDMA( void* pTransmitData, void* pReceiveData, size_t size )
{
    /* Always set up the rx channel first */
    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_RPR = (uint32_t) pReceiveData;
    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_RCR = (uint32_t) size;
    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_TPR = (uint32_t) pTransmitData;
    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_TCR = (uint32_t) size;
    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_PTCR = FLEX_PTCR_RXTEN_Msk | FLEX_PTCR_TXTEN_Msk;
    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_SPI_IER = FLEX_SPI_IER_ENDRX_Msk;
}

</#if>
</#if>

void ${FLEXCOM_INSTANCE_NAME}_SPI_Initialize ( void )
{
    /* Set FLEXCOM SPI operating mode */
    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_MR = FLEX_MR_OPMODE_SPI;

    /* Disable and Reset the FLEXCOM SPI */
    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_SPI_CR = FLEX_SPI_CR_SPIDIS_Msk | FLEX_SPI_CR_SWRST_Msk;

<#if SPI_INTERRUPT_MODE == true && FLEXCOM_SPI_FIFO_ENABLE == true>
    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_SPI_CR = FLEX_SPI_CR_FIFOEN_Msk;
</#if>

<#if FLEXCOM_SPI_MR_MSTR =="MASTER">
    /* Enable Master mode, select clock source, select particular NPCS line for chip select and disable mode fault detection */
    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_SPI_MR = FLEX_SPI_MR_MSTR_Msk | FLEX_SPI_MR_BRSRCCLK_${FLEXCOM_SPI_MR_BRSRCCLK} | FLEX_SPI_MR_DLYBCS(${FLEXCOM_SPI_MR_DLYBCS}U) <#if FLEXCOM_SPI_EN_NPCS0?? && FLEXCOM_SPI_EN_NPCS0 == true>| FLEX_SPI_MR_PCS((uint32_t)FLEXCOM_SPI_CHIP_SELECT_NPCS0)<#elseif FLEXCOM_SPI_EN_NPCS1?? && FLEXCOM_SPI_EN_NPCS1 == true>| FLEX_SPI_MR_PCS(FLEXCOM_SPI_CHIP_SELECT_NPCS1) <#elseif FLEXCOM_SPI_EN_NPCS2?? && FLEXCOM_SPI_EN_NPCS2 == true>| FLEX_SPI_MR_PCS(FLEXCOM_SPI_CHIP_SELECT_NPCS2) <#elseif FLEXCOM_SPI_EN_NPCS3?? && FLEXCOM_SPI_EN_NPCS3 == true>| FLEX_SPI_MR_PCS(FLEXCOM_SPI_CHIP_SELECT_NPCS3)</#if> | FLEX_SPI_MR_MODFDIS_Msk;
</#if>

<#if FLEXCOM_SPI_EN_NPCS0?? && FLEXCOM_SPI_EN_NPCS0 == true>
    /* Set up clock Polarity, data phase, Communication Width, Baud Rate */
    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_SPI_CSR[0]= FLEX_SPI_CSR_CPOL(${FLEXCOM_SPI_CSR0_CPOL}U) | FLEX_SPI_CSR_NCPHA(${FLEXCOM_SPI_CSR0_NCPHA}U) | FLEX_SPI_CSR_BITS_${FLEXCOM_SPI_CSR0_BITS} | FLEX_SPI_CSR_SCBR(${FLEXCOM_SPI_CSR0_SCBR_VALUE}U) | FLEX_SPI_CSR_DLYBS(${FLEXCOM_SPI_CSR0_DLYBS}U) | FLEX_SPI_CSR_DLYBCT(${FLEXCOM_SPI_CSR0_DLYBCT}U) | FLEX_SPI_CSR_CSAAT_Msk;
</#if>

<#if FLEXCOM_SPI_EN_NPCS1?? && FLEXCOM_SPI_EN_NPCS1 == true>
    /* Set up clock Polarity, data phase, Communication Width, Baud Rate */
    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_SPI_CSR[1]= FLEX_SPI_CSR_CPOL(${FLEXCOM_SPI_CSR1_CPOL}) | FLEX_SPI_CSR_NCPHA(${FLEXCOM_SPI_CSR1_NCPHA}) | FLEX_SPI_CSR_BITS_${FLEXCOM_SPI_CSR1_BITS} | FLEX_SPI_CSR_SCBR(${FLEXCOM_SPI_CSR1_SCBR_VALUE}) | FLEX_SPI_CSR_DLYBS(${FLEXCOM_SPI_CSR1_DLYBS}) | FLEX_SPI_CSR_DLYBCT(${FLEXCOM_SPI_CSR1_DLYBCT}) | FLEX_SPI_CSR_CSAAT_Msk;
</#if>

<#if FLEXCOM_SPI_EN_NPCS2?? && FLEXCOM_SPI_EN_NPCS2 == true>
    /* Set up clock Polarity, data phase, Communication Width, Baud Rate */
    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_SPI_CSR[2]= FLEX_SPI_CSR_CPOL(${FLEXCOM_SPI_CSR2_CPOL}) | FLEX_SPI_CSR_NCPHA(${FLEXCOM_SPI_CSR2_NCPHA}) | FLEX_SPI_CSR_BITS_${FLEXCOM_SPI_CSR2_BITS} | FLEX_SPI_CSR_SCBR(${FLEXCOM_SPI_CSR2_SCBR_VALUE}) | FLEX_SPI_CSR_DLYBS(${FLEXCOM_SPI_CSR2_DLYBS}) | FLEX_SPI_CSR_DLYBCT(${FLEXCOM_SPI_CSR2_DLYBCT}) | FLEX_SPI_CSR_CSAAT_Msk;
</#if>

<#if FLEXCOM_SPI_EN_NPCS3?? && FLEXCOM_SPI_EN_NPCS3 == true>
    /* Set up clock Polarity, data phase, Communication Width, Baud Rate */
    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_SPI_CSR[3]= FLEX_SPI_CSR_CPOL(${FLEXCOM_SPI_CSR3_CPOL}) | FLEX_SPI_CSR_NCPHA(${FLEXCOM_SPI_CSR3_NCPHA}) | FLEX_SPI_CSR_BITS_${FLEXCOM_SPI_CSR3_BITS} | FLEX_SPI_CSR_SCBR(${FLEXCOM_SPI_CSR3_SCBR_VALUE}) | FLEX_SPI_CSR_DLYBS(${FLEXCOM_SPI_CSR3_DLYBS}) | FLEX_SPI_CSR_DLYBCT(${FLEXCOM_SPI_CSR3_DLYBCT}) | FLEX_SPI_CSR_CSAAT_Msk;
</#if>

<#if SPI_INTERRUPT_MODE == true >
    /* Initialize global variables */
    ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.transferIsBusy = false;
    ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.callback = NULL;
</#if>

    /* Enable ${FLEXCOM_INSTANCE_NAME} SPI */
    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_SPI_CR = FLEX_SPI_CR_SPIEN_Msk;
    return;
}

<#if FLEXCOM_SPI_NUM_CSR != 1>
static uint8_t ${FLEXCOM_INSTANCE_NAME}_SPI_ChipSelectGet(void)
{
    uint8_t pcs = (uint8_t)((${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_SPI_MR  & FLEX_SPI_MR_PCS_Msk) >> FLEX_SPI_MR_PCS_Pos);

    if (pcs == (uint8_t)FLEXCOM_SPI_CHIP_SELECT_NPCS0)
    {
        return 0U;
    }
<#if FLEXCOM_SPI_EN_NPCS1??>
    else if (pcs == (uint8_t)FLEXCOM_SPI_CHIP_SELECT_NPCS1)
    {
        return 1U;
    }
</#if>
<#if FLEXCOM_SPI_EN_NPCS2??>
    else if (pcs == (uint8_t)FLEXCOM_SPI_CHIP_SELECT_NPCS2)
    {
        return 2U;
    }
</#if>
<#if FLEXCOM_SPI_EN_NPCS3??>
    else if (pcs == (uint8_t)FLEXCOM_SPI_CHIP_SELECT_NPCS3)
    {
        return 3U;
    }
</#if>
    else
    {
        return 0U;
    }
}

void ${FLEXCOM_INSTANCE_NAME}_SPI_ChipSelectSetup(FLEXCOM_SPI_CHIP_SELECT chipSelect)
{
    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_SPI_MR =  (${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_SPI_MR & ~FLEX_SPI_MR_PCS_Msk) | FLEX_SPI_MR_PCS(chipSelect);
}
</#if>

<#if SPI_INTERRUPT_MODE == false >
bool ${FLEXCOM_INSTANCE_NAME}_SPI_WriteRead(void* pTransmitData, size_t txSize, void* pReceiveData, size_t rxSize)
{
    size_t txCount = 0;
    size_t rxCount = 0;
    size_t dummySize = 0;
    size_t receivedData;
    uint32_t dataBits;
    bool isSuccess = false;

    /* Verify the request */
    if (((txSize > 0U) && (pTransmitData != NULL)) || ((rxSize > 0U) && (pReceiveData != NULL)))
    {
        if (pTransmitData == NULL)
        {
            txSize = 0;
        }
        if (pReceiveData == NULL)
        {
            rxSize = 0;
        }
<#if FLEXCOM_SPI_NUM_CSR == 1>
        dataBits = ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_SPI_CSR[${FLEXCOM_SPI_CSR_INDEX}] & FLEX_SPI_CSR_BITS_Msk;
<#else>
        dataBits = ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_SPI_CSR[${FLEXCOM_INSTANCE_NAME}_SPI_ChipSelectGet()] & FLEX_SPI_CSR_BITS_Msk;
</#if>

        /* Flush out any unread data in SPI read buffer from the previous transfer */
        receivedData = (${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_SPI_RDR & FLEX_SPI_RDR_RD_Msk) >> FLEX_SPI_RDR_RD_Pos;

        if (rxSize > txSize)
        {
            dummySize = rxSize - txSize;
        }
        if (dataBits != FLEX_SPI_CSR_BITS_8_BIT)
        {
            rxSize >>= 1;
            txSize >>= 1;
            dummySize >>= 1;
        }

        /* Make sure TDR is empty */
        while((bool)((${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_SPI_SR & FLEX_SPI_SR_TDRE_Msk) >> FLEX_SPI_SR_TDRE_Pos) == false)
        {
            /* Nothing to do */
        }

        while ((txCount != txSize) || (dummySize != 0U))
        {
            if (txCount != txSize)
            {
                if(dataBits == FLEX_SPI_CSR_BITS_8_BIT)
                {
                    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_SPI_TDR = ((uint8_t*)pTransmitData)[txCount];
                    txCount++;
                }
                else
                {
                    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_SPI_TDR = ((uint16_t*)pTransmitData)[txCount];
                    txCount++;
                }
            }
            else if (dummySize > 0U)
            {
                if(dataBits == FLEX_SPI_CSR_BITS_8_BIT)
                {
                    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_SPI_TDR = 0x${FLEXCOM_SPI_DUMMY_DATA};
                }
                else
                {
                    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_SPI_TDR = 0x${FLEXCOM_SPI_DUMMY_DATA}${FLEXCOM_SPI_DUMMY_DATA};
                }
                dummySize--;
            }
            else
            {
                /* Nothing to do */
            }

            if (rxSize == 0U)
            {
                /* For transmit only request, wait for TDR to become empty */
                while((bool)((${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_SPI_SR & FLEX_SPI_SR_TDRE_Msk) >> FLEX_SPI_SR_TDRE_Pos) == false)
                {
                    /* Nothing to do */
                }
            }
            else
            {
                /* If data is read, wait for the Receiver Data Register to become full*/
                while((bool)((${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_SPI_SR & FLEX_SPI_SR_RDRF_Msk) >> FLEX_SPI_SR_RDRF_Pos) == false)
                {
                    /* Nothing to do */
                }

                receivedData = (${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_SPI_RDR & FLEX_SPI_RDR_RD_Msk) >> FLEX_SPI_RDR_RD_Pos;

                if (rxCount < rxSize)
                {
                    if(dataBits == FLEX_SPI_CSR_BITS_8_BIT)
                    {
                        ((uint8_t*)pReceiveData)[rxCount] = (uint8_t)receivedData;
                        rxCount++;
                    }
                    else
                    {
                        ((uint16_t*)pReceiveData)[rxCount] = (uint16_t)receivedData;
                        rxCount++;
                    }
                }
            }
        }

        /* Make sure no data is pending in the shift register */
        while ((bool)((${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_SPI_SR & FLEX_SPI_SR_TXEMPTY_Msk) >> FLEX_SPI_SR_TXEMPTY_Pos) == false)
        {
            /* Nothing to do */
        }

        /* Set Last transfer to deassert NPCS after the last byte written in TDR has been transferred. */
        ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_SPI_CR = FLEX_SPI_CR_LASTXFER_Msk;

        isSuccess = true;
    }
    return isSuccess;
}
<#else>

<#if FLEXCOM_SPI_FIFO_ENABLE == false>
bool ${FLEXCOM_INSTANCE_NAME}_SPI_WriteRead (void* pTransmitData, size_t txSize, void* pReceiveData, size_t rxSize)
{
    bool isRequestAccepted = false;
<#if USE_SPI_DMA?? && USE_SPI_DMA == true>
    uint32_t size = 0;

    /* Verify the request */
    if((((txSize > 0) && (pTransmitData != NULL)) || ((rxSize > 0) && (pReceiveData != NULL))) && (${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.transferIsBusy == false))
    {
        isRequestAccepted = true;

        ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.transferIsBusy = true;

        ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txBuffer = pTransmitData;
        ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.rxBuffer = pReceiveData;
        ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txCount = txSize;
        ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.rxCount = rxSize;

        if ((txSize > 0) && (rxSize > 0))
        {
            /* Find the lower value among txSize and rxSize */
            (txSize >= rxSize) ? (size = rxSize) : (size = txSize);

            /* Calculate the remaining tx/rx bytes and total bytes transferred */
            ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.rxCount -= size;
            ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txCount -= size;
            ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.nBytesTransferred = size;

            setupDMA(pTransmitData, pReceiveData, size);
        }
        else
        {
            if (rxSize > 0)
            {
                /* txSize is 0. Need to use the dummy data buffer for transmission.
                 * Find out the max data that can be received, given the limited size of the dummy data buffer.
                 */
                (rxSize > sizeof(dummyDataBuffer)) ?
                    (size = sizeof(dummyDataBuffer)): (size = rxSize);

                /* Calculate the remaining rx bytes and total bytes transferred */
                ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.rxCount -= size;
                ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.nBytesTransferred = size;

                setupDMA(dummyDataBuffer, pReceiveData, size);
            }
            else
            {
                /* rxSize is 0. Need to use the dummy data buffer for reception.
                 * Find out the max data that can be transmitted, given the limited size of the dummy data buffer.
                 */
                (txSize > sizeof(dummyDataBuffer)) ?
                    (size = sizeof(dummyDataBuffer)): (size = txSize);

                /* Calculate the remaining tx bytes and total bytes transferred */
                ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txCount -= size;
                ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.nBytesTransferred = size;

                setupDMA(pTransmitData, dummyDataBuffer, size);
            }
        }
    }

    return isRequestAccepted;
<#else>
    uint32_t dummyData;

    /* Verify the request */
    if((((txSize > 0U) && (pTransmitData != NULL)) || ((rxSize > 0U) && (pReceiveData != NULL))) && (${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.transferIsBusy == false))
    {
        isRequestAccepted = true;
        ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txBuffer = pTransmitData;
        ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.rxBuffer = pReceiveData;
        ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.rxCount = 0;
        ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txCount = 0;
        ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.dummySize = 0;
        if (pTransmitData != NULL)
        {
            ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txSize = txSize;
        }
        else
        {
            ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txSize = 0;
        }

        if (pReceiveData != NULL)
        {
            ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.rxSize = rxSize;
        }
        else
        {
            ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.rxSize = 0;
        }

        ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.transferIsBusy = true;

        /* Flush out any unread data in SPI read buffer */
        dummyData = (${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_SPI_RDR & FLEX_SPI_RDR_RD_Msk) >> FLEX_SPI_RDR_RD_Pos;
        (void)dummyData;

        if (${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.rxSize > ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txSize)
        {
            ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.dummySize = ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.rxSize - ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txSize;
        }

        /* Start the first write here itself, rest will happen in ISR context */
<#if FLEXCOM_SPI_NUM_CSR == 1>
        if((${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_SPI_CSR[${FLEXCOM_SPI_CSR_INDEX}] & FLEX_SPI_CSR_BITS_Msk) == FLEX_SPI_CSR_BITS_8_BIT)
<#else>
        if((${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_SPI_CSR[${FLEXCOM_INSTANCE_NAME}_SPI_ChipSelectGet()] & FLEX_SPI_CSR_BITS_Msk) == FLEX_SPI_CSR_BITS_8_BIT)
</#if>
        {
            if (${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txCount < ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txSize)
            {
                ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_SPI_TDR = *((uint8_t*)${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txBuffer);
                ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txCount++;
            }
            else if (${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.dummySize > 0U)
            {
                ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_SPI_TDR = (uint8_t)(0x${FLEXCOM_SPI_DUMMY_DATA});
                ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.dummySize--;
            }
            else
            {
                /* Do nothing */
            }
        }
        else
        {
            ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txSize >>= 1;
            ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.dummySize >>= 1;
            ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.rxSize >>= 1;

            if (${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txCount < ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txSize)
            {
                ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_SPI_TDR = *((uint16_t*)${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txBuffer);
                ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txCount++;
            }
            else if (${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.dummySize > 0U)
            {
                ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_SPI_TDR = (uint16_t)(0x${FLEXCOM_SPI_DUMMY_DATA}${FLEXCOM_SPI_DUMMY_DATA});
                ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.dummySize--;
            }
            else
            {
                /* Do nothing */
            }
        }

        if (rxSize > 0U)
        {
            /* Enable receive interrupt to complete the transfer in ISR context */
            ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_SPI_IER = FLEX_SPI_IER_RDRF_Msk;
        }
        else
        {
            /* Enable transmit interrupt to complete the transfer in ISR context */
            ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_SPI_IER = FLEX_SPI_IER_TDRE_Msk;
        }
    }

    return isRequestAccepted;
</#if>
}
<#else>

<#if !(USE_SPI_DMA?? && USE_SPI_DMA == true)>
static uint8_t ${FLEXCOM_INSTANCE_NAME}_SPI_FIFO_Fill(void)
{
    uint8_t nDataCopiedToFIFO = 0;
<#if FLEXCOM_SPI_NUM_CSR == 1>
    uint32_t dataBits = ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_SPI_CSR[${FLEXCOM_SPI_CSR_INDEX}] & FLEX_SPI_CSR_BITS_Msk;
<#else>
    uint32_t dataBits = ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_SPI_CSR[${FLEXCOM_INSTANCE_NAME}_SPI_ChipSelectGet()] & FLEX_SPI_CSR_BITS_Msk;
</#if>

    while ((nDataCopiedToFIFO < ${FLEXCOM_SPI_FIFO_SIZE}U) && ((${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_SPI_SR & FLEX_SPI_SR_TDRE_Msk) != 0U))
    {
        if(dataBits == FLEX_SPI_CSR_BITS_8_BIT)
        {
            if (${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txCount < ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txSize)
            {
                FLEXCOM_SPI_TDR_8BIT_REG =  ((uint8_t*)${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txBuffer)[${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txCount];
                ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txCount++;
            }
            else if (${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.dummySize > 0U)
            {
                FLEXCOM_SPI_TDR_8BIT_REG = (uint8_t)(0x${FLEXCOM_SPI_DUMMY_DATA});
                ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.dummySize--;
            }
            else
            {
                break;
            }
        }
        else
        {
            if (${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txCount < ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txSize)
            {
                FLEXCOM_SPI_TDR_9BIT_REG =  ((uint16_t*)${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txBuffer)[${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txCount];
                ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txCount++;
            }
            else if (${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.dummySize > 0U)
            {
                FLEXCOM_SPI_TDR_9BIT_REG = (uint16_t)(0x${FLEXCOM_SPI_DUMMY_DATA}${FLEXCOM_SPI_DUMMY_DATA});
                ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.dummySize--;
            }
            else
            {
                break;
            }
        }

        nDataCopiedToFIFO++;
    }

    return nDataCopiedToFIFO;
}
</#if>

bool ${FLEXCOM_INSTANCE_NAME}_SPI_WriteRead (void* pTransmitData, size_t txSize, void* pReceiveData, size_t rxSize)
{
    bool isRequestAccepted = false;
<#if !(USE_SPI_DMA?? && USE_SPI_DMA == true)>
    uint32_t nTxPending = 0;
    uint8_t rxThreshold = 0;
</#if>
<#if USE_SPI_DMA?? && USE_SPI_DMA == true>
    uint32_t size = 0;

    /* Verify the request */
    if((((txSize > 0U) && (pTransmitData != NULL)) || ((rxSize > 0U) && (pReceiveData != NULL))) && (${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.transferIsBusy == false))
    {
        isRequestAccepted = true;

        ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.transferIsBusy = true;

        ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txBuffer = pTransmitData;
        ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.rxBuffer = pReceiveData;
        ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txCount = txSize;
        ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.rxCount = rxSize;

        if ((txSize > 0) && (rxSize > 0))
        {
            /* Find the lower value among txSize and rxSize */
            (txSize >= rxSize) ? (size = rxSize) : (size = txSize);

            /* Calculate the remaining tx/rx bytes and total bytes transferred */
            ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.rxCount -= size;
            ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txCount -= size;
            ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.nBytesTransferred = size;

            setupDMA(pTransmitData, pReceiveData, size);
        }
        else
        {
            if (rxSize > 0)
            {
                /* txSize is 0. Need to use the dummy data buffer for transmission.
                 * Find out the max data that can be received, given the limited size of the dummy data buffer.
                 */
                (rxSize > sizeof(dummyDataBuffer)) ?
                    (size = sizeof(dummyDataBuffer)): (size = rxSize);

                /* Calculate the remaining rx bytes and total bytes transferred */
                ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.rxCount -= size;
                ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.nBytesTransferred = size;

                setupDMA(dummyDataBuffer, pReceiveData, size);
            }
            else
            {
                /* rxSize is 0. Need to use the dummy data buffer for reception.
                 * Find out the max data that can be transmitted, given the limited size of the dummy data buffer.
                 */
                (txSize > sizeof(dummyDataBuffer)) ?
                    (size = sizeof(dummyDataBuffer)): (size = txSize);

                /* Calculate the remaining tx bytes and total bytes transferred */
                ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txCount -= size;
                ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.nBytesTransferred = size;

                setupDMA(pTransmitData, dummyDataBuffer, size);
            }
        }
    }
    return isRequestAccepted;

    <#else>
    /* Verify the request */
    if((((txSize > 0) && (pTransmitData != NULL)) || ((rxSize > 0) && (pReceiveData != NULL))) && (${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.transferIsBusy == false))
    {
        isRequestAccepted = true;
        ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txBuffer = pTransmitData;
        ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.rxBuffer = pReceiveData;
        ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.rxCount = 0;
        ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txCount = 0;
        ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.dummySize = 0;

        if (pTransmitData != NULL)
        {
            ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txSize = txSize;
        }
        else
        {
            ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txSize = 0;
        }

        if (pReceiveData != NULL)
        {
            ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.rxSize = rxSize;
        }
        else
        {
            ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.rxSize = 0;
        }

        ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.transferIsBusy = true;

        if (${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.rxSize > ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txSize)
        {
            ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.dummySize = ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.rxSize - ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txSize;
        }

<#if FLEXCOM_SPI_NUM_CSR == 1>
        if((${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_SPI_CSR[${FLEXCOM_SPI_CSR_INDEX}] & FLEX_SPI_CSR_BITS_Msk) != FLEX_SPI_CSR_BITS_8_BIT)
<#else>
        if((${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_SPI_CSR[${FLEXCOM_INSTANCE_NAME}_SPI_ChipSelectGet()] & FLEX_SPI_CSR_BITS_Msk) != FLEX_SPI_CSR_BITS_8_BIT)
</#if>
        {
            ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txSize >>= 1;
            ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.dummySize >>= 1;
            ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.rxSize >>= 1;
        }

        /* Clear TX and RX FIFO */
        ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_SPI_CR = (FLEX_SPI_CR_RXFCLR_Msk | FLEX_SPI_CR_TXFCLR_Msk);

        nTxPending = (${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txSize - ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txCount) + ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.dummySize;

        if (nTxPending < ${FLEXCOM_SPI_FIFO_SIZE}U)
        {
            rxThreshold = (uint8_t)nTxPending;
        }
        else
        {
            rxThreshold = ${FLEXCOM_SPI_FIFO_SIZE};
        }

        /* Set RX FIFO level so as to generate interrupt after all bytes are transmitted and response from slave is received for all the bytes */
        /* RX FIFO level must be set first or else FIFO may be filled before RX threshold is set and hardware may not recognize threshold crossover and not generate threshold interrupt */
        ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_SPI_FMR = (${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_SPI_FMR & ~FLEX_SPI_FMR_RXFTHRES_Msk) | FLEX_SPI_FMR_RXFTHRES(rxThreshold);

        (void) ${FLEXCOM_INSTANCE_NAME}_SPI_FIFO_Fill();

        /* Enable RX FIFO Threshold interrupt */
        ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_SPI_IER = FLEX_SPI_IER_RXFTHF_Msk;
    }

    return isRequestAccepted;
    </#if>
}
</#if>
</#if>

bool ${FLEXCOM_INSTANCE_NAME}_SPI_TransferSetup (FLEXCOM_SPI_TRANSFER_SETUP * setup, uint32_t spiSourceClock )
{
<#assign flexcomClockSymbol = "core." + FLEXCOM_INSTANCE_NAME + "_CLOCK_FREQUENCY">
    uint32_t scbr;
    bool setupStatus = false;
    if ((setup != NULL) && (setup->clockFrequency != 0U))
    {
        if(spiSourceClock == 0U)
        {
            // Fetch Master Clock Frequency directly
            spiSourceClock = ${flexcomClockSymbol?eval};
        }

        scbr = spiSourceClock/setup->clockFrequency;

        if(scbr == 0U)
        {
            scbr = 1;
        }
        else if(scbr > 255U)
        {
            scbr = 255;
        }
        else
        {
            /* Do nothing */
        }

    <#if FLEXCOM_SPI_NUM_CSR == 1>
        ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_SPI_CSR[${FLEXCOM_SPI_CSR_INDEX}]= (${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_SPI_CSR[${FLEXCOM_SPI_CSR_INDEX}] & ~(FLEX_SPI_CSR_CPOL_Msk | FLEX_SPI_CSR_NCPHA_Msk | FLEX_SPI_CSR_BITS_Msk | FLEX_SPI_CSR_SCBR_Msk)) | ((uint32_t)setup->clockPolarity | (uint32_t)setup->clockPhase | (uint32_t)setup->dataBits | FLEX_SPI_CSR_SCBR(scbr));
    <#else>
        ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_SPI_CSR[${FLEXCOM_INSTANCE_NAME}_SPI_ChipSelectGet()]= (${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_SPI_CSR[${FLEXCOM_INSTANCE_NAME}_SPI_ChipSelectGet()] & ~(FLEX_SPI_CSR_CPOL_Msk | FLEX_SPI_CSR_NCPHA_Msk | FLEX_SPI_CSR_BITS_Msk | FLEX_SPI_CSR_SCBR_Msk)) | ((uint32_t)setup->clockPolarity | (uint32_t)setup->clockPhase | (uint32_t)setup->dataBits | FLEX_SPI_CSR_SCBR(scbr));
    </#if>

        setupStatus = true;
    }
    return setupStatus;
}

bool ${FLEXCOM_INSTANCE_NAME}_SPI_Write(void* pTransmitData, size_t txSize)
{
    return(${FLEXCOM_INSTANCE_NAME}_SPI_WriteRead(pTransmitData, txSize, NULL, 0));
}

bool ${FLEXCOM_INSTANCE_NAME}_SPI_Read(void* pReceiveData, size_t rxSize)
{
    return(${FLEXCOM_INSTANCE_NAME}_SPI_WriteRead(NULL, 0, pReceiveData, rxSize));
}

bool ${FLEXCOM_INSTANCE_NAME}_SPI_IsTransmitterBusy(void)
{
    return ((${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_SPI_SR & FLEX_SPI_SR_TXEMPTY_Msk) == 0U);
}

<#if SPI_INTERRUPT_MODE == true >
void ${FLEXCOM_INSTANCE_NAME}_SPI_CallbackRegister (FLEXCOM_SPI_CALLBACK callback, uintptr_t context)
{
    ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.callback = callback;
    ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.context = context;
}

bool ${FLEXCOM_INSTANCE_NAME}_SPI_IsBusy(void)
{
    return ((${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.transferIsBusy) || ((${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_SPI_SR & FLEX_SPI_SR_TXEMPTY_Msk) == 0U));
}

<#if FLEXCOM_SPI_FIFO_ENABLE == false>
void ${FLEXCOM_INSTANCE_NAME}_InterruptHandler(void)
{
<#if !(USE_SPI_DMA?? && USE_SPI_DMA == true)>
    uint32_t dataBits ;
    uint32_t receivedData;
<#if FLEXCOM_SPI_NUM_CSR == 1>
    dataBits = ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_SPI_CSR[${FLEXCOM_SPI_CSR_INDEX}] & FLEX_SPI_CSR_BITS_Msk;
<#else>
    dataBits = ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_SPI_CSR[${FLEXCOM_INSTANCE_NAME}_SPI_ChipSelectGet()] & FLEX_SPI_CSR_BITS_Msk;
</#if>

    static bool isLastByteTransferInProgress = false;
<#else>
    uint32_t size;
    uint32_t index;
</#if>

    /* save the status in global object before it gets cleared */
    ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.status = ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_SPI_SR;

    <#if USE_SPI_DMA?? && USE_SPI_DMA == true>
    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_PTCR = FLEX_PTCR_ERRCLR_Msk;

    if(${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.rxCount > 0)
    {
        /* txPending is 0. Need to use the dummy data buffer for transmission.
         * Find out the max data that can be received, given the limited size of the dummy data buffer.
         */
        (${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.rxCount > sizeof(dummyDataBuffer)) ?
            (size = sizeof(dummyDataBuffer)): (size = ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.rxCount);

        index = ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.nBytesTransferred;

        /* Calculate the remaining rx bytes and total bytes transferred */
        ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.rxCount -= size;
        ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.nBytesTransferred += size;

        setupDMA(dummyDataBuffer,(void *)&((uint8_t*)${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.rxBuffer)[index],size);
    }
    else if(${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txCount > 0)
    {
        /* rxSize is 0. Need to use the dummy data buffer for reception.
         * Find out the max data that can be transmitted, given the limited size of the dummy data buffer.
         */
        (${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txCount > sizeof(dummyDataBuffer)) ?
            (size = sizeof(dummyDataBuffer)): (size = ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txCount);

        index = ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.nBytesTransferred;

        /* Calculate the remaining rx bytes and total bytes transferred */
        ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txCount -= size;
        ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.nBytesTransferred += size;

        setupDMA((void *)&((uint8_t*)${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txBuffer)[index], dummyDataBuffer, size);
    }
    else
    {
        ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.transferIsBusy = false;

        <#if FLEXCOM_SPI_MR_PCS != "GPIO">
        /* Set Last transfer to deassert NPCS after the last byte written in TDR has been transferred. */
        ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_SPI_CR = FLEX_SPI_CR_LASTXFER_Msk;

        </#if>
        ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_PTCR = FLEX_PTCR_RXTDIS_Msk | FLEX_PTCR_TXTDIS_Msk;
        ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_SPI_IDR = FLEX_SPI_IDR_ENDRX_Msk; 

        if( ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.callback != NULL )
        {
            ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.callback(${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.context);
        }
    }
    <#else>

    if ((${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_SPI_SR & FLEX_SPI_SR_RDRF_Msk ) == FLEX_SPI_SR_RDRF_Msk)
    {
        receivedData = (${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_SPI_RDR & FLEX_SPI_RDR_RD_Msk) >> FLEX_SPI_RDR_RD_Pos;

        if (${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.rxCount < ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.rxSize)
        {
            if(dataBits == FLEX_SPI_CSR_BITS_8_BIT)
            {
                ((uint8_t*)${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.rxBuffer)[${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.rxCount] = (uint8_t)receivedData;
                ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.rxCount++;
            }
            else
            {
                ((uint16_t*)${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.rxBuffer)[${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.rxCount] = (uint16_t)receivedData;
                ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.rxCount++;
            }
        }
    }

    /* If there are more words to be transmitted, then transmit them here and keep track of the count */
    if((${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_SPI_SR & FLEX_SPI_SR_TDRE_Msk) == FLEX_SPI_SR_TDRE_Msk)
    {
        /* Disable the TDRE interrupt. This will be enabled back if more than
         * one byte is pending to be transmitted */
        ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_SPI_IDR = FLEX_SPI_IDR_TDRE_Msk;

        if(dataBits == FLEX_SPI_CSR_BITS_8_BIT)
        {
            if (${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txCount < ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txSize)
            {
                ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_SPI_TDR = ((uint8_t*)${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txBuffer)[${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txCount];
                ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txCount++;
            }
            else if (${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.dummySize > 0U)
            {
                ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_SPI_TDR = (uint8_t)(0x${FLEXCOM_SPI_DUMMY_DATA});
                ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.dummySize--;
            }
            else
            {
                /* Do nothing */
            }
        }
        else
        {
            if (${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txCount < ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txSize)
            {
                ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_SPI_TDR = ((uint16_t*)${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txBuffer)[${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txCount];
                ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txCount++;
            }
            else if (${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.dummySize > 0U)
            {
                ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_SPI_TDR = (uint16_t)(0x${FLEXCOM_SPI_DUMMY_DATA}${FLEXCOM_SPI_DUMMY_DATA});
                ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.dummySize--;
            }
            else
            {
                /* Do nothing */
            }
        }
        if ((${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txCount == ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txSize) && (${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.dummySize == 0U))
        {
            /* At higher baud rates, the data in the shift register can be
             * shifted out and TXEMPTY flag can get set resulting in a
             * callback been given to the application with the SPI interrupt
             * pending with the application. This will then result in the
             * interrupt handler being called again with nothing to transmit.
             * To avoid the above mentioned issue, a software flag is set, but
             * the TXEMPTY interrupt is not enabled until the very end.
             * At higher baud rates, if the software flag is set and the
             * TXEMPTY status bit is set, then it means that the transfer is
             * complete and a callback can be given to the application. Since
             * the TXEMPTY interrupt is not enabled there is no need to
             * explicitly clear the pending interrupt from the Interrupt controller.
             */

            isLastByteTransferInProgress = true;
        }
        else if (${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.rxCount == ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.rxSize)
        {
            /* Enable TDRE interrupt as all the requested bytes are received
             * and can now make use of the internal transmit shift register.
             */
            ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_SPI_IDR = FLEX_SPI_IDR_RDRF_Msk;
            ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_SPI_IER = FLEX_SPI_IDR_TDRE_Msk;
        }
        else
        {
            /* Do nothing */
        }
    }

    /* See if Exchange is complete */
    if ((isLastByteTransferInProgress == true) && ((${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_SPI_SR & FLEX_SPI_SR_TXEMPTY_Msk) == FLEX_SPI_SR_TXEMPTY_Msk))
    {
        if (${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.rxCount == ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.rxSize)
        {
            /* Set Last transfer to deassert NPCS after the last byte written in TDR has been transferred. */
            ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_SPI_CR = FLEX_SPI_CR_LASTXFER_Msk;

            ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.transferIsBusy = false;

            /* Disable TDRE, RDRF and TXEMPTY interrupts */
            ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_SPI_IDR = FLEX_SPI_IDR_TDRE_Msk | FLEX_SPI_IDR_RDRF_Msk | FLEX_SPI_IDR_TXEMPTY_Msk;

            isLastByteTransferInProgress = false;

            if(${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.callback != NULL)
            {
                ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.callback(${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.context);
            }
        }
    }
    if (isLastByteTransferInProgress == true)
    {
        /* For the last byte transfer, the TDRE interrupt is already disabled.
         * Enable TXEMPTY interrupt to ensure no data is present in the shift
         * register before application callback is called.
         */
        ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_SPI_IER = FLEX_SPI_IER_TXEMPTY_Msk;
    }

    </#if>
}
<#else>
void ${FLEXCOM_INSTANCE_NAME}_InterruptHandler(void)
{
<#if !(USE_SPI_DMA?? && USE_SPI_DMA == true)>
<#if FLEXCOM_SPI_NUM_CSR == 1>
    uint32_t dataBits = ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_SPI_CSR[${FLEXCOM_SPI_CSR_INDEX}] & FLEX_SPI_CSR_BITS_Msk;
<#else>
    uint32_t dataBits = ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_SPI_CSR[${FLEXCOM_INSTANCE_NAME}_SPI_ChipSelectGet()] & FLEX_SPI_CSR_BITS_Msk;
</#if>
    uint32_t nTxPending = 0;
    uint8_t rxThreshold = 0;
<#else>
    uint32_t size;
    uint32_t index;
</#if>

    <#if USE_SPI_DMA?? && USE_SPI_DMA == true>
    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_PTCR = FLEX_PTCR_ERRCLR_Msk;

    if(${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.rxCount > 0)
    {
        /* txPending is 0. Need to use the dummy data buffer for transmission.
         * Find out the max data that can be received, given the limited size of the dummy data buffer.
         */
        (${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.rxCount > sizeof(dummyDataBuffer)) ?
            (size = sizeof(dummyDataBuffer)): (size = ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.rxCount);

        index = ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.nBytesTransferred;

        /* Calculate the remaining rx bytes and total bytes transferred */
        ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.rxCount -= size;
        ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.nBytesTransferred += size;

        setupDMA(dummyDataBuffer,(void *)&((uint8_t*)${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.rxBuffer)[index],size);
    }
    else if(${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txCount > 0)
    {
        /* rxSize is 0. Need to use the dummy data buffer for reception.
         * Find out the max data that can be transmitted, given the limited size of the dummy data buffer.
         */
        (${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txCount > sizeof(dummyDataBuffer)) ?
            (size = sizeof(dummyDataBuffer)): (size = ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txCount);

        index = ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.nBytesTransferred;

        /* Calculate the remaining rx bytes and total bytes transferred */
        ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txCount -= size;
        ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.nBytesTransferred += size;

        setupDMA((void *)&((uint8_t*)${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txBuffer)[index], dummyDataBuffer, size);
    }
    else
    {
        ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.transferIsBusy = false;

        <#if FLEXCOM_SPI_MR_PCS != "GPIO">
        /* Set Last transfer to deassert NPCS after the last byte written in TDR has been transferred. */
        ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_SPI_CR = FLEX_SPI_CR_LASTXFER_Msk;

        </#if>
        ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_PTCR = FLEX_PTCR_RXTDIS_Msk | FLEX_PTCR_TXTDIS_Msk;
        ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_SPI_IDR = FLEX_SPI_IDR_ENDRX_Msk;

        if( ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.callback != NULL )
        {
            ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.callback(${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.context);
        }
    }

    <#else>
    while ((${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_SPI_SR & FLEX_SPI_SR_RDRF_Msk ) && (${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.rxCount < ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.rxSize))
    {
        if(dataBits == FLEX_SPI_CSR_BITS_8_BIT)
        {
            ((uint8_t*)${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.rxBuffer)[${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.rxCount] = FLEXCOM_SPI_RDR_8BIT_REG;
            ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.rxCount++;
        }
        else
        {
            ((uint16_t*)${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.rxBuffer)[${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.rxCount] = FLEXCOM_SPI_RDR_9BIT_REG;
            ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.rxCount++;
        }
    }

    /* Clear RX FIFO. This is done for the case where RX size is less than TX size and hence data is not read and copied into the application rx buffer. */
    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_SPI_CR = FLEX_SPI_CR_RXFCLR_Msk;

    nTxPending = (${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txSize - ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txCount) + ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.dummySize;

    if (nTxPending > 0U)
    {
        if (nTxPending < ${FLEXCOM_SPI_FIFO_SIZE}U)
        {
            rxThreshold = (uint8_t)nTxPending;
        }
        else
        {
            rxThreshold = ${FLEXCOM_SPI_FIFO_SIZE};
        }

        /* Set RX FIFO level so as to generate interrupt after all bytes are transmitted and response from slave is received for all the bytes */
        /* RX FIFO level must be set first or else FIFO may be filled before RX threshold is set and hardware may not recognize threshold crossover and not generate threshold interrupt */
        ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_SPI_FMR = (${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_SPI_FMR & ~FLEX_SPI_FMR_RXFTHRES_Msk) | FLEX_SPI_FMR_RXFTHRES(rxThreshold);

        (void) ${FLEXCOM_INSTANCE_NAME}_SPI_FIFO_Fill();
    }
    else
    {
        /* Set Last transfer to deassert NPCS after the last byte written in TDR has been transferred. */
        ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_SPI_CR = FLEX_SPI_CR_LASTXFER_Msk;

        ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.transferIsBusy = false;

        /* Disable Receive FIFO Threshold interrupt */
        ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_SPI_IDR = FLEX_SPI_IDR_RXFTHF_Msk;

        if(${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.callback != NULL)
        {
            ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.callback(${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.context);
        }
    }
    </#if>
}
</#if>
</#if>


/*******************************************************************************
 End of File
*/

