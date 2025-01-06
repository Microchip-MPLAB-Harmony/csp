/*******************************************************************************
  MCSPI PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${MCSPI_INSTANCE_NAME?lower_case}_master.c

  Summary:
    ${MCSPI_INSTANCE_NAME} Master Source File

  Description:
    This file has implementation of all the interfaces provided for particular
    MCSPI peripheral.

*******************************************************************************/

/*******************************************************************************
* Copyright (C) 2022 Microchip Technology Inc. and its subsidiaries.
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

#include "plib_${MCSPI_INSTANCE_NAME?lower_case}_master.h"
<#if core.CoreSysIntFile == true>
#include "interrupts.h"
</#if>

// *****************************************************************************
// *****************************************************************************
// Section: ${MCSPI_INSTANCE_NAME} Implementation
// *****************************************************************************
// *****************************************************************************
#define MCSPI_TDR_8BIT_REG      (*(volatile uint8_t* const)((${MCSPI_INSTANCE_NAME}_BASE_ADDRESS + MCSPI_TDR_REG_OFST)))
#define MCSPI_TDR_16BIT_REG     (*(volatile uint16_t* const)((${MCSPI_INSTANCE_NAME}_BASE_ADDRESS + MCSPI_TDR_REG_OFST)))

#define MCSPI_RDR_8BIT_REG      (*(volatile uint8_t* const)((${MCSPI_INSTANCE_NAME}_BASE_ADDRESS + MCSPI_RDR_REG_OFST)))
#define MCSPI_RDR_16BIT_REG     (*(volatile uint16_t* const)((${MCSPI_INSTANCE_NAME}_BASE_ADDRESS + MCSPI_RDR_REG_OFST)))

<#if MCSPI_INTERRUPT_MODE == true>

/* Global object to save MCSPI Exchange related data */
static volatile MCSPI_OBJECT ${MCSPI_INSTANCE_NAME?lower_case}Obj;
<#if USE_MCSPI_DMA?? && USE_MCSPI_DMA == true>
<#if MCSPI_FIFO_ENABLE == false>

static volatile uint8_t dummyDataBuffer[512];

static void setupDMA( volatile void* pTransmitData, volatile void* pReceiveData, size_t size )
{
    /* Always set up the rx channel first */
    ${MCSPI_INSTANCE_NAME}_REGS->MCSPI_RPR = (volatile uint32_t) (volatile uint32_t*)pReceiveData;
    ${MCSPI_INSTANCE_NAME}_REGS->MCSPI_RCR = (uint32_t) size;
    ${MCSPI_INSTANCE_NAME}_REGS->MCSPI_TPR = (volatile uint32_t) (volatile uint32_t*)pTransmitData;
    ${MCSPI_INSTANCE_NAME}_REGS->MCSPI_TCR = (uint32_t) size;
    ${MCSPI_INSTANCE_NAME}_REGS->MCSPI_PTCR = MCSPI_PTCR_RXTEN_Msk | MCSPI_PTCR_TXTEN_Msk;
    ${MCSPI_INSTANCE_NAME}_REGS->MCSPI_IER = MCSPI_IER_ENDRX_Msk;
}
</#if>
</#if>
</#if>

void ${MCSPI_INSTANCE_NAME}_Initialize( void )
{
    /* Disable and Reset the MCSPI*/
    ${MCSPI_INSTANCE_NAME}_REGS->MCSPI_CR = MCSPI_CR_SPIDIS_Msk | MCSPI_CR_SWRST_Msk;

<#if MCSPI_INTERRUPT_MODE == true && MCSPI_FIFO_ENABLE == true>
    ${MCSPI_INSTANCE_NAME}_REGS->MCSPI_CR = MCSPI_CR_FIFOEN_Msk;
</#if>

<#if MCSPI_MR_MSTR =="MASTER">
    /* Enable Master mode, <#if MCSPI_CLK_SRC??>select source clock, </#if>select particular NPCS line for chip select and disable mode fault detection */
    ${MCSPI_INSTANCE_NAME}_REGS->MCSPI_MR = MCSPI_MR_MSTR_Msk | MCSPI_MR_DLYBCS(${MCSPI_MR_DLYBCS}) <#if MCSPI_CLK_SRC??>| MCSPI_MR_BRSRCCLK_${MCSPI_CLK_SRC} </#if><#if MCSPI_EN_NPCS0?? && MCSPI_EN_NPCS0 == true>| MCSPI_MR_PCS(MCSPI_CHIP_SELECT_NPCS0) <#elseif MCSPI_EN_NPCS1?? && MCSPI_EN_NPCS1 == true>| MCSPI_MR_PCS(MCSPI_CHIP_SELECT_NPCS1)<#elseif MCSPI_EN_NPCS2?? && MCSPI_EN_NPCS2 == true> | MCSPI_MR_PCS(MCSPI_CHIP_SELECT_NPCS2) <#elseif MCSPI_EN_NPCS3?? && MCSPI_EN_NPCS3 == true> | MCSPI_MR_PCS(MCSPI_CHIP_SELECT_NPCS3) </#if> | MCSPI_MR_MODFDIS_Msk;
</#if>

<#if MCSPI_EN_NPCS0?? && MCSPI_EN_NPCS0 == true>
    /* Set up clock Polarity, data phase, Communication Width, Baud Rate */
    ${MCSPI_INSTANCE_NAME}_REGS->MCSPI_CSR[0] = MCSPI_CSR_CPOL(${MCSPI_CSR0_CPOL}) | MCSPI_CSR_NCPHA(${MCSPI_CSR0_NCPHA}) | MCSPI_CSR_BITS${MCSPI_CSR0_BITS} | MCSPI_CSR_SCBR(${MCSPI_CSR0_SCBR_VALUE})| MCSPI_CSR_DLYBS(${MCSPI_CSR0_DLYBS}) | MCSPI_CSR_DLYBCT(${MCSPI_CSR0_DLYBCT}) | MCSPI_CSR_CSAAT_Msk;
</#if>

<#if MCSPI_EN_NPCS1?? && MCSPI_EN_NPCS1 == true>
    /* Set up clock Polarity, data phase, Communication Width, Baud Rate */
    ${MCSPI_INSTANCE_NAME}_REGS->MCSPI_CSR[1] = MCSPI_CSR_CPOL(${MCSPI_CSR1_CPOL}) | MCSPI_CSR_NCPHA(${MCSPI_CSR1_NCPHA}) | MCSPI_CSR_BITS${MCSPI_CSR1_BITS} | MCSPI_CSR_SCBR(${MCSPI_CSR1_SCBR_VALUE})| MCSPI_CSR_DLYBS(${MCSPI_CSR1_DLYBS}) | MCSPI_CSR_DLYBCT(${MCSPI_CSR1_DLYBCT}) | MCSPI_CSR_CSAAT_Msk;
</#if>

<#if MCSPI_EN_NPCS2?? && MCSPI_EN_NPCS2 == true>
    /* Set up clock Polarity, data phase, Communication Width, Baud Rate */
    ${MCSPI_INSTANCE_NAME}_REGS->MCSPI_CSR[2] = MCSPI_CSR_CPOL(${MCSPI_CSR2_CPOL}) | MCSPI_CSR_NCPHA(${MCSPI_CSR2_NCPHA}) | MCSPI_CSR_BITS${MCSPI_CSR2_BITS} | MCSPI_CSR_SCBR(${MCSPI_CSR2_SCBR_VALUE})| MCSPI_CSR_DLYBS(${MCSPI_CSR2_DLYBS}) | MCSPI_CSR_DLYBCT(${MCSPI_CSR2_DLYBCT}) | MCSPI_CSR_CSAAT_Msk;
</#if>

<#if MCSPI_EN_NPCS3?? && MCSPI_EN_NPCS3 == true>
    /* Set up clock Polarity, data phase, Communication Width, Baud Rate */
    ${MCSPI_INSTANCE_NAME}_REGS->MCSPI_CSR[3] = MCSPI_CSR_CPOL(${MCSPI_CSR3_CPOL}) | MCSPI_CSR_NCPHA(${MCSPI_CSR3_NCPHA}) | MCSPI_CSR_BITS${MCSPI_CSR3_BITS} | MCSPI_CSR_SCBR(${MCSPI_CSR3_SCBR_VALUE})| MCSPI_CSR_DLYBS(${MCSPI_CSR3_DLYBS}) | MCSPI_CSR_DLYBCT(${MCSPI_CSR3_DLYBCT}) | MCSPI_CSR_CSAAT_Msk;
</#if>


<#if MCSPI_INTERRUPT_MODE == true >
    /* Initialize global variables */
    ${MCSPI_INSTANCE_NAME?lower_case}Obj.transferIsBusy = false;
    ${MCSPI_INSTANCE_NAME?lower_case}Obj.callback = NULL;
</#if>

    /* Enable ${MCSPI_INSTANCE_NAME} */
    ${MCSPI_INSTANCE_NAME}_REGS->MCSPI_CR = MCSPI_CR_SPIEN_Msk;
}

<#if MCSPI_NUM_CSR != 1>
static uint8_t ${MCSPI_INSTANCE_NAME}_ChipSelectGet(void)
{
    uint8_t pcs = (uint8_t)((${MCSPI_INSTANCE_NAME}_REGS->MCSPI_MR  & MCSPI_MR_PCS_Msk) >> MCSPI_MR_PCS_Pos);
    if (pcs == (uint8_t)MCSPI_CHIP_SELECT_NPCS0)
    {
        return 0;
    }
<#if MCSPI_EN_NPCS1??>
    else if (pcs == (uint8_t)MCSPI_CHIP_SELECT_NPCS1)
    {
        return 1;
    }
</#if>
<#if MCSPI_EN_NPCS2??>
    else if (pcs == (uint8_t)MCSPI_CHIP_SELECT_NPCS2)
    {
        return 2;
    }
</#if>
<#if MCSPI_EN_NPCS3??>
    else if (pcs == (uint8_t)MCSPI_CHIP_SELECT_NPCS3)
    {
        return 3;
    }
</#if>
    else
    {
        return 0;
    }
}

void ${MCSPI_INSTANCE_NAME}_ChipSelectSetup(MCSPI_CHIP_SELECT chipSelect)
{
    ${MCSPI_INSTANCE_NAME}_REGS->MCSPI_MR =  (${MCSPI_INSTANCE_NAME}_REGS->MCSPI_MR & ~MCSPI_MR_PCS_Msk) | MCSPI_MR_PCS(chipSelect);
}
</#if>

<#if MCSPI_INTERRUPT_MODE == false >
bool ${MCSPI_INSTANCE_NAME}_WriteRead( void* pTransmitData, size_t txSize, void* pReceiveData, size_t rxSize )
{
    size_t txCount = 0;
    size_t rxCount = 0;
    size_t dummySize = 0;
    size_t receivedData;
    uint32_t dataBits;
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

<#if MCSPI_NUM_CSR == 1>
        dataBits = ${MCSPI_INSTANCE_NAME}_REGS->MCSPI_CSR[${MCSPI_CSR_INDEX}] & MCSPI_CSR_BITS_Msk;
<#else>
        dataBits = ${MCSPI_INSTANCE_NAME}_REGS->MCSPI_CSR[${MCSPI_INSTANCE_NAME}_ChipSelectGet()] & MCSPI_CSR_BITS_Msk;
</#if>

        /* Flush out any unread data in MCSPI read buffer from the previous transfer */
        receivedData = (${MCSPI_INSTANCE_NAME}_REGS->MCSPI_RDR & MCSPI_RDR_RD_Msk) >> MCSPI_RDR_RD_Pos;

        if (rxSize > txSize)
        {
            dummySize = rxSize - txSize;
        }
        if (dataBits != MCSPI_CSR_BITS_8_BIT)
        {
            rxSize >>= 1;
            txSize >>= 1;
            dummySize >>= 1;
        }

        /* Make sure TDR is empty */
        while((bool)((${MCSPI_INSTANCE_NAME}_REGS->MCSPI_SR & MCSPI_SR_TDRE_Msk) >> MCSPI_SR_TDRE_Pos) == false);

        while ((txCount != txSize) || (dummySize != 0U))
        {
            if (txCount != txSize)
            {
                if(dataBits == MCSPI_CSR_BITS_8_BIT)
                {
                    ${MCSPI_INSTANCE_NAME}_REGS->MCSPI_TDR = ((uint8_t*)pTransmitData)[txCount++];
                }
                else
                {
                    ${MCSPI_INSTANCE_NAME}_REGS->MCSPI_TDR = ((uint16_t*)pTransmitData)[txCount++];
                }
            }
            else if (dummySize > 0U)
            {
                if(dataBits == MCSPI_CSR_BITS_8_BIT)
                {
                    ${MCSPI_INSTANCE_NAME}_REGS->MCSPI_TDR = 0x${MCSPI_DUMMY_DATA};
                }
                else
                {
                    ${MCSPI_INSTANCE_NAME}_REGS->MCSPI_TDR = (uint16_t)(0x${MCSPI_DUMMY_DATA}${MCSPI_DUMMY_DATA});
                }
                dummySize--;
            }

            if (rxSize == 0U)
            {
                /* For transmit only request, wait for TDR to become empty */
                while((bool)((${MCSPI_INSTANCE_NAME}_REGS->MCSPI_SR & MCSPI_SR_TDRE_Msk) >> MCSPI_SR_TDRE_Pos) == false);
            }
            else
            {
                /* If data is read, wait for the Receiver Data Register to become full*/
                while((bool)((${MCSPI_INSTANCE_NAME}_REGS->MCSPI_SR & MCSPI_SR_RDRF_Msk) >> MCSPI_SR_RDRF_Pos) == false)
                {
                }

                receivedData = (${MCSPI_INSTANCE_NAME}_REGS->MCSPI_RDR & MCSPI_RDR_RD_Msk) >> MCSPI_RDR_RD_Pos;

                if (rxCount < rxSize)
                {
                    if(dataBits == MCSPI_CSR_BITS_8_BIT)
                    {
                        ((uint8_t*)pReceiveData)[rxCount++] = receivedData;
                    }
                    else
                    {
                        ((uint16_t*)pReceiveData)[rxCount++] = receivedData;
                    }
                }
            }
        }

        /* Make sure no data is pending in the shift register */
        while ((bool)((${MCSPI_INSTANCE_NAME}_REGS->MCSPI_SR & MCSPI_SR_TXEMPTY_Msk) >> MCSPI_SR_TXEMPTY_Pos) == false);

        /* Set Last transfer to deassert NPCS after the last byte written in TDR has been transferred. */
        ${MCSPI_INSTANCE_NAME}_REGS->MCSPI_CR = MCSPI_CR_LASTXFER_Msk;

        isSuccess = true;
    }
        return isSuccess;
}
<#else>

<#if MCSPI_FIFO_ENABLE == false>
bool ${MCSPI_INSTANCE_NAME}_WriteRead( void* pTransmitData, size_t txSize, void* pReceiveData, size_t rxSize )
{
    bool isRequestAccepted = false;
<#if USE_MCSPI_DMA?? && USE_MCSPI_DMA == true>
    uint32_t size = 0;

    if (${MCSPI_INSTANCE_NAME?lower_case}Obj.transferIsBusy == false)
    {
        /* Verify the request */
        if(((txSize > 0U) && (pTransmitData != NULL)) || ((rxSize > 0U) && (pReceiveData != NULL)))
        {
            isRequestAccepted = true;

            ${MCSPI_INSTANCE_NAME?lower_case}Obj.transferIsBusy = true;

            ${MCSPI_INSTANCE_NAME?lower_case}Obj.txBuffer = pTransmitData;
            ${MCSPI_INSTANCE_NAME?lower_case}Obj.rxBuffer = pReceiveData;
            ${MCSPI_INSTANCE_NAME?lower_case}Obj.txCount = txSize;
            ${MCSPI_INSTANCE_NAME?lower_case}Obj.rxCount = rxSize;

            if ((txSize > 0U) && (rxSize > 0U))
            {
                /* Find the lower value among txSize and rxSize */
                (txSize >= rxSize) ? (size = rxSize) : (size = txSize);

                /* Calculate the remaining tx/rx bytes and total bytes transferred */
                ${MCSPI_INSTANCE_NAME?lower_case}Obj.rxCount -= size;
                ${MCSPI_INSTANCE_NAME?lower_case}Obj.txCount -= size;
                ${MCSPI_INSTANCE_NAME?lower_case}Obj.nBytesTransferred = size;

                setupDMA(pTransmitData, pReceiveData, size);
            }
            else
            {
                if (rxSize > 0U)
                {
                    /* txSize is 0. Need to use the dummy data buffer for transmission.
                     * Find out the max data that can be received, given the limited size of the dummy data buffer.
                     */
                    (rxSize > sizeof(dummyDataBuffer)) ?
                        (size = sizeof(dummyDataBuffer)): (size = rxSize);

                    /* Calculate the remaining rx bytes and total bytes transferred */
                    ${MCSPI_INSTANCE_NAME?lower_case}Obj.rxCount -= size;
                    ${MCSPI_INSTANCE_NAME?lower_case}Obj.nBytesTransferred = size;

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
                    ${MCSPI_INSTANCE_NAME?lower_case}Obj.txCount -= size;
                    ${MCSPI_INSTANCE_NAME?lower_case}Obj.nBytesTransferred = size;

                    setupDMA(pTransmitData, dummyDataBuffer, size);
                }
            }
        }
    }

    return isRequestAccepted;
<#else>
    uint32_t dummyData;

    if (${MCSPI_INSTANCE_NAME?lower_case}Obj.transferIsBusy == false)
    {
        /* Verify the request */
        if(((txSize > 0U) && (pTransmitData != NULL)) || ((rxSize > 0U) && (pReceiveData != NULL)))
        {
            isRequestAccepted = true;
            ${MCSPI_INSTANCE_NAME?lower_case}Obj.txBuffer = pTransmitData;
            ${MCSPI_INSTANCE_NAME?lower_case}Obj.rxBuffer = pReceiveData;
            ${MCSPI_INSTANCE_NAME?lower_case}Obj.rxCount = 0;
            ${MCSPI_INSTANCE_NAME?lower_case}Obj.txCount = 0;
            ${MCSPI_INSTANCE_NAME?lower_case}Obj.dummySize = 0;

            if (pTransmitData != NULL)
            {
                ${MCSPI_INSTANCE_NAME?lower_case}Obj.txSize = txSize;
            }
            else
            {
                ${MCSPI_INSTANCE_NAME?lower_case}Obj.txSize = 0;
            }

            if (pReceiveData != NULL)
            {
                ${MCSPI_INSTANCE_NAME?lower_case}Obj.rxSize = rxSize;
            }
            else
            {
                ${MCSPI_INSTANCE_NAME?lower_case}Obj.rxSize = 0;
            }

            ${MCSPI_INSTANCE_NAME?lower_case}Obj.transferIsBusy = true;

            /* Flush out any unread data in MCSPI read buffer */
            dummyData = (${MCSPI_INSTANCE_NAME}_REGS->MCSPI_RDR & MCSPI_RDR_RD_Msk) >> MCSPI_RDR_RD_Pos;
            (void)dummyData;

            size_t txSz = ${MCSPI_INSTANCE_NAME?lower_case}Obj.txSize;

            if (${MCSPI_INSTANCE_NAME?lower_case}Obj.rxSize > txSz)
            {
                ${MCSPI_INSTANCE_NAME?lower_case}Obj.dummySize = ${MCSPI_INSTANCE_NAME?lower_case}Obj.rxSize - txSz;
            }

            /* Start the first write here itself, rest will happen in ISR context */
    <#if MCSPI_NUM_CSR == 1>
            if((${MCSPI_INSTANCE_NAME}_REGS->MCSPI_CSR[${MCSPI_CSR_INDEX}] & MCSPI_CSR_BITS_Msk) == MCSPI_CSR_BITS_8_BIT)
    <#else>
            if((${MCSPI_INSTANCE_NAME}_REGS->MCSPI_CSR[${MCSPI_INSTANCE_NAME}_ChipSelectGet()] & MCSPI_CSR_BITS_Msk) == MCSPI_CSR_BITS_8_BIT)
    </#if>
            {
                if (${MCSPI_INSTANCE_NAME?lower_case}Obj.txCount < txSz)
                {
                    ${MCSPI_INSTANCE_NAME}_REGS->MCSPI_TDR = *((uint8_t*)${MCSPI_INSTANCE_NAME?lower_case}Obj.txBuffer);
                    ${MCSPI_INSTANCE_NAME?lower_case}Obj.txCount++;
                }
                else if (${MCSPI_INSTANCE_NAME?lower_case}Obj.dummySize > 0U)
                {
                    ${MCSPI_INSTANCE_NAME}_REGS->MCSPI_TDR = (uint8_t)(0x${MCSPI_DUMMY_DATA});
                    ${MCSPI_INSTANCE_NAME?lower_case}Obj.dummySize--;
                }
                else
                {
                    /* Nothing to do */
                }
            }
            else
            {
                ${MCSPI_INSTANCE_NAME?lower_case}Obj.txSize >>= 1;
                ${MCSPI_INSTANCE_NAME?lower_case}Obj.dummySize >>= 1;
                ${MCSPI_INSTANCE_NAME?lower_case}Obj.rxSize >>= 1;

                txSz = ${MCSPI_INSTANCE_NAME?lower_case}Obj.txSize;

                if (${MCSPI_INSTANCE_NAME?lower_case}Obj.txCount < txSz)
                {
                    ${MCSPI_INSTANCE_NAME}_REGS->MCSPI_TDR = *((uint16_t*)${MCSPI_INSTANCE_NAME?lower_case}Obj.txBuffer);
                    ${MCSPI_INSTANCE_NAME?lower_case}Obj.txCount++;
                }
                else if (${MCSPI_INSTANCE_NAME?lower_case}Obj.dummySize > 0U)
                {
                    ${MCSPI_INSTANCE_NAME}_REGS->MCSPI_TDR = (uint16_t)(0x${MCSPI_DUMMY_DATA}${MCSPI_DUMMY_DATA});
                    ${MCSPI_INSTANCE_NAME?lower_case}Obj.dummySize--;
                }
                else
                {
                    /* Nothing to do */
                }
            }

            if (rxSize > 0U)
            {
                /* Enable receive interrupt to complete the transfer in ISR context */
                ${MCSPI_INSTANCE_NAME}_REGS->MCSPI_IER = MCSPI_IER_RDRF_Msk;
            }
            else
            {
                /* Enable transmit interrupt to complete the transfer in ISR context */
                ${MCSPI_INSTANCE_NAME}_REGS->MCSPI_IER = MCSPI_IER_TDRE_Msk;
            }
        }
    }

    return isRequestAccepted;
</#if>
}

<#else>
static uint8_t ${MCSPI_INSTANCE_NAME}_FIFO_Fill(void)
{
    uint8_t nDataCopiedToFIFO = 0;
<#if MCSPI_NUM_CSR == 1>
    uint32_t dataBits = ${MCSPI_INSTANCE_NAME}_REGS->MCSPI_CSR[${MCSPI_CSR_INDEX}] & MCSPI_CSR_BITS_Msk;
<#else>
    uint32_t dataBits = ${MCSPI_INSTANCE_NAME}_REGS->MCSPI_CSR[${MCSPI_INSTANCE_NAME}_ChipSelectGet()] & MCSPI_CSR_BITS_Msk;
</#if>

    size_t txCount = ${MCSPI_INSTANCE_NAME?lower_case}Obj.txCount;

    while ((nDataCopiedToFIFO < 16U) && ((${MCSPI_INSTANCE_NAME}_REGS->MCSPI_SR & MCSPI_SR_TDRE_Msk) != 0U))
    {
        if(dataBits == MCSPI_CSR_BITS_8_BIT)
        {
            if (txCount < ${MCSPI_INSTANCE_NAME?lower_case}Obj.txSize)
            {
                MCSPI_TDR_8BIT_REG =  ((uint8_t*)${MCSPI_INSTANCE_NAME?lower_case}Obj.txBuffer)[txCount];
                txCount++;
            }
            else if (${MCSPI_INSTANCE_NAME?lower_case}Obj.dummySize > 0U)
            {
                MCSPI_TDR_8BIT_REG = (uint8_t)(0x${MCSPI_DUMMY_DATA});
                ${MCSPI_INSTANCE_NAME?lower_case}Obj.dummySize--;
            }
            else
            {
                break;
            }
        }
        else
        {
            if (txCount < ${MCSPI_INSTANCE_NAME?lower_case}Obj.txSize)
            {
                MCSPI_TDR_16BIT_REG =  ((uint16_t*)${MCSPI_INSTANCE_NAME?lower_case}Obj.txBuffer)[txCount];
                txCount++;
            }
            else if (${MCSPI_INSTANCE_NAME?lower_case}Obj.dummySize > 0U)
            {
                MCSPI_TDR_16BIT_REG = (uint16_t)(0x${MCSPI_DUMMY_DATA}${MCSPI_DUMMY_DATA});
                ${MCSPI_INSTANCE_NAME?lower_case}Obj.dummySize--;
            }
            else
            {
                break;
            }
        }

        nDataCopiedToFIFO++;
    }

    ${MCSPI_INSTANCE_NAME?lower_case}Obj.txCount = txCount;

    return nDataCopiedToFIFO;
}

bool ${MCSPI_INSTANCE_NAME}_WriteRead (void* pTransmitData, size_t txSize, void* pReceiveData, size_t rxSize)
{
    bool isRequestAccepted = false;
    uint32_t nTxPending = 0;
    uint8_t rxThreshold = 0;

    if (${MCSPI_INSTANCE_NAME?lower_case}Obj.transferIsBusy == false)
    {
        /* Verify the request */
        if(((txSize > 0U) && (pTransmitData != NULL)) || ((rxSize > 0U) && (pReceiveData != NULL)))
        {
            isRequestAccepted = true;
            ${MCSPI_INSTANCE_NAME?lower_case}Obj.txBuffer = pTransmitData;
            ${MCSPI_INSTANCE_NAME?lower_case}Obj.rxBuffer = pReceiveData;
            ${MCSPI_INSTANCE_NAME?lower_case}Obj.rxCount = 0;
            ${MCSPI_INSTANCE_NAME?lower_case}Obj.txCount = 0;
            ${MCSPI_INSTANCE_NAME?lower_case}Obj.dummySize = 0;

            if (pTransmitData != NULL)
            {
                ${MCSPI_INSTANCE_NAME?lower_case}Obj.txSize = txSize;
            }
            else
            {
                ${MCSPI_INSTANCE_NAME?lower_case}Obj.txSize = 0;
            }

            if (pReceiveData != NULL)
            {
                ${MCSPI_INSTANCE_NAME?lower_case}Obj.rxSize = rxSize;
            }
            else
            {
                ${MCSPI_INSTANCE_NAME?lower_case}Obj.rxSize = 0;
            }

            ${MCSPI_INSTANCE_NAME?lower_case}Obj.transferIsBusy = true;

            size_t txSz = ${MCSPI_INSTANCE_NAME?lower_case}Obj.txSize;

            if (${MCSPI_INSTANCE_NAME?lower_case}Obj.rxSize > txSz)
            {
                ${MCSPI_INSTANCE_NAME?lower_case}Obj.dummySize = ${MCSPI_INSTANCE_NAME?lower_case}Obj.rxSize - txSz;
            }

    <#if MCSPI_NUM_CSR == 1>
        if((${MCSPI_INSTANCE_NAME}_REGS->MCSPI_CSR[${MCSPI_CSR_INDEX}] & MCSPI_CSR_BITS_Msk) != MCSPI_CSR_BITS_8_BIT)
    <#else>
        if((${MCSPI_INSTANCE_NAME}_REGS->MCSPI_CSR[${MCSPI_INSTANCE_NAME}_ChipSelectGet()] & MCSPI_CSR_BITS_Msk) != MCSPI_CSR_BITS_8_BIT)
    </#if>
            {
                ${MCSPI_INSTANCE_NAME?lower_case}Obj.txSize >>= 1;
                ${MCSPI_INSTANCE_NAME?lower_case}Obj.dummySize >>= 1;
                ${MCSPI_INSTANCE_NAME?lower_case}Obj.rxSize >>= 1;
            }

            txSz = ${MCSPI_INSTANCE_NAME?lower_case}Obj.txSize;

            /* Clear TX and RX FIFO */
            ${MCSPI_INSTANCE_NAME}_REGS->MCSPI_CR = (MCSPI_CR_RXFCLR_Msk | MCSPI_CR_TXFCLR_Msk);

            nTxPending = (txSz - ${MCSPI_INSTANCE_NAME?lower_case}Obj.txCount);
            nTxPending += ${MCSPI_INSTANCE_NAME?lower_case}Obj.dummySize;

            if (nTxPending < 16U)
            {
                rxThreshold = (uint8_t)nTxPending;
            }
            else
            {
                rxThreshold = 16;
            }

            /* Set RX FIFO level so as to generate interrupt after all bytes are transmitted and response from slave is received for all the bytes */
            /* RX FIFO level must be set first or else FIFO may be filled before RX threshold is set and hardware may not recognize threshold crossover and not generate threshold interrupt */
            ${MCSPI_INSTANCE_NAME}_REGS->MCSPI_FMR = (${MCSPI_INSTANCE_NAME}_REGS->MCSPI_FMR & ~MCSPI_FMR_RXFTHRES_Msk) | MCSPI_FMR_RXFTHRES(rxThreshold);

            (void) ${MCSPI_INSTANCE_NAME}_FIFO_Fill();

            /* Enable RX FIFO Threshold interrupt */
            ${MCSPI_INSTANCE_NAME}_REGS->MCSPI_IER = MCSPI_IER_RXFTHF_Msk;
        }
    }

    return isRequestAccepted;
}
</#if>
</#if>

bool ${MCSPI_INSTANCE_NAME}_Write( void* pTransmitData, size_t txSize )
{
    return(${MCSPI_INSTANCE_NAME}_WriteRead(pTransmitData, txSize, NULL, 0));
}

bool ${MCSPI_INSTANCE_NAME}_Read( void* pReceiveData, size_t rxSize )
{
    return(${MCSPI_INSTANCE_NAME}_WriteRead(NULL, 0, pReceiveData, rxSize));
}

bool ${MCSPI_INSTANCE_NAME}_TransferSetup( MCSPI_TRANSFER_SETUP * setup, uint32_t mcspiSourceClock )
{
    uint32_t scbr;

    if ((setup == NULL) || (setup->clockFrequency == 0U))
    {
        return false;
    }

    if(mcspiSourceClock == 0U)
    {
        // Fetch Master Clock Frequency directly
        mcspiSourceClock = ${MCSPI_MASTER_CLOCK};
    }

    scbr = mcspiSourceClock/setup->clockFrequency;

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
        /* Nothing to do */
    }

<#if MCSPI_NUM_CSR == 1>
    ${MCSPI_INSTANCE_NAME}_REGS->MCSPI_CSR[${MCSPI_CSR_INDEX}] = (${MCSPI_INSTANCE_NAME}_REGS->MCSPI_CSR[${MCSPI_CSR_INDEX}] & ~(MCSPI_CSR_CPOL_Msk | MCSPI_CSR_NCPHA_Msk | MCSPI_CSR_BITS_Msk | MCSPI_CSR_SCBR_Msk)) |((uint32_t)setup->clockPolarity | (uint32_t)setup->clockPhase | (uint32_t)setup->dataBits | MCSPI_CSR_SCBR(scbr));
<#else>
    ${MCSPI_INSTANCE_NAME}_REGS->MCSPI_CSR[${MCSPI_INSTANCE_NAME}_ChipSelectGet()] = (${MCSPI_INSTANCE_NAME}_REGS->MCSPI_CSR[${MCSPI_INSTANCE_NAME}_ChipSelectGet()] & ~(MCSPI_CSR_CPOL_Msk | MCSPI_CSR_NCPHA_Msk | MCSPI_CSR_BITS_Msk | MCSPI_CSR_SCBR_Msk)) |((uint32_t)setup->clockPolarity | (uint32_t)setup->clockPhase | (uint32_t)setup->dataBits | MCSPI_CSR_SCBR(scbr));
</#if>

    return true;
}

bool ${MCSPI_INSTANCE_NAME}_IsTransmitterBusy( void )
{
    return ((${MCSPI_INSTANCE_NAME}_REGS->MCSPI_SR & MCSPI_SR_TXEMPTY_Msk) == 0U)? true : false;
}

<#if MCSPI_INTERRUPT_MODE == true >
void ${MCSPI_INSTANCE_NAME}_CallbackRegister( MCSPI_CALLBACK callback, uintptr_t context )
{
    ${MCSPI_INSTANCE_NAME?lower_case}Obj.callback = callback;
    ${MCSPI_INSTANCE_NAME?lower_case}Obj.context = context;
}

bool ${MCSPI_INSTANCE_NAME}_IsBusy( void )
{
    bool transferIsBusy = ${MCSPI_INSTANCE_NAME?lower_case}Obj.transferIsBusy;

    return (((${MCSPI_INSTANCE_NAME}_REGS->MCSPI_SR & MCSPI_SR_TXEMPTY_Msk) == 0U) || (transferIsBusy));
}
<#if MCSPI_FIFO_ENABLE == false>
void __attribute__((used)) ${MCSPI_INSTANCE_NAME}_InterruptHandler( void )
{
<#if USE_MCSPI_DMA?? && USE_MCSPI_DMA == true>
    uint32_t size;
    uint32_t index;
<#else>
    uint32_t dataBits;
    uint32_t receivedData;
    static bool isLastByteTransferInProgress = false;

<#if MCSPI_NUM_CSR == 1>
    dataBits = ${MCSPI_INSTANCE_NAME}_REGS->MCSPI_CSR[${MCSPI_CSR_INDEX}] & MCSPI_CSR_BITS_Msk;
<#else>
    dataBits = ${MCSPI_INSTANCE_NAME}_REGS->MCSPI_CSR[${MCSPI_INSTANCE_NAME}_ChipSelectGet()] & MCSPI_CSR_BITS_Msk;
</#if>

</#if>

    uintptr_t context = ${MCSPI_INSTANCE_NAME?lower_case}Obj.context;

    <#if USE_MCSPI_DMA?? && USE_MCSPI_DMA == true>
    if(${MCSPI_INSTANCE_NAME?lower_case}Obj.rxCount > 0U)
    {
        /* txPending is 0. Need to use the dummy data buffer for transmission.
         * Find out the max data that can be received, given the limited size of the dummy data buffer.
         */
        (${MCSPI_INSTANCE_NAME?lower_case}Obj.rxCount > sizeof(dummyDataBuffer)) ?
            (size = sizeof(dummyDataBuffer)): (size = ${MCSPI_INSTANCE_NAME?lower_case}Obj.rxCount);

        index = ${MCSPI_INSTANCE_NAME?lower_case}Obj.nBytesTransferred;

        /* Calculate the remaining rx bytes and total bytes transferred */
        ${MCSPI_INSTANCE_NAME?lower_case}Obj.rxCount -= size;
        ${MCSPI_INSTANCE_NAME?lower_case}Obj.nBytesTransferred += size;

        setupDMA(dummyDataBuffer, &((uint8_t*)${MCSPI_INSTANCE_NAME?lower_case}Obj.rxBuffer)[index],size);
    }
    else if(${MCSPI_INSTANCE_NAME?lower_case}Obj.txCount > 0U)
    {
        /* rxSize is 0. Need to use the dummy data buffer for reception.
         * Find out the max data that can be transmitted, given the limited size of the dummy data buffer.
         */
        (${MCSPI_INSTANCE_NAME?lower_case}Obj.txCount > sizeof(dummyDataBuffer)) ?
            (size = sizeof(dummyDataBuffer)): (size = ${MCSPI_INSTANCE_NAME?lower_case}Obj.txCount);

        index = ${MCSPI_INSTANCE_NAME?lower_case}Obj.nBytesTransferred;

        /* Calculate the remaining rx bytes and total bytes transferred */
        ${MCSPI_INSTANCE_NAME?lower_case}Obj.txCount -= size;
        ${MCSPI_INSTANCE_NAME?lower_case}Obj.nBytesTransferred += size;

        setupDMA(&((uint8_t*)${MCSPI_INSTANCE_NAME?lower_case}Obj.txBuffer)[index], dummyDataBuffer, size);
    }
    else
    {
        ${MCSPI_INSTANCE_NAME?lower_case}Obj.transferIsBusy = false;

        /* Set Last transfer to deassert NPCS after the last byte written in TDR has been transferred. */
        ${MCSPI_INSTANCE_NAME}_REGS->MCSPI_CR = MCSPI_CR_LASTXFER_Msk;

        ${MCSPI_INSTANCE_NAME}_REGS->MCSPI_PTCR = MCSPI_PTCR_RXTDIS_Msk | MCSPI_PTCR_TXTDIS_Msk;
        ${MCSPI_INSTANCE_NAME}_REGS->MCSPI_IDR = MCSPI_IDR_ENDRX_Msk;

        if( ${MCSPI_INSTANCE_NAME?lower_case}Obj.callback != NULL )
        {
            ${MCSPI_INSTANCE_NAME?lower_case}Obj.callback(context);
        }
    }
    <#else>
    size_t rxSize = ${MCSPI_INSTANCE_NAME?lower_case}Obj.rxSize;

    if ((${MCSPI_INSTANCE_NAME}_REGS->MCSPI_SR & MCSPI_SR_RDRF_Msk ) == MCSPI_SR_RDRF_Msk)
    {
        receivedData = (${MCSPI_INSTANCE_NAME}_REGS->MCSPI_RDR & MCSPI_RDR_RD_Msk) >> MCSPI_RDR_RD_Pos;

        size_t rxCount = ${MCSPI_INSTANCE_NAME?lower_case}Obj.rxCount;

        if (rxCount < ${MCSPI_INSTANCE_NAME?lower_case}Obj.rxSize)
        {
            if(dataBits == MCSPI_CSR_BITS_8_BIT)
            {
                ((uint8_t*)${MCSPI_INSTANCE_NAME?lower_case}Obj.rxBuffer)[rxCount] = (uint8_t)receivedData;
                rxCount++;
            }
            else
            {
                ((uint16_t*)${MCSPI_INSTANCE_NAME?lower_case}Obj.rxBuffer)[rxCount] = (uint16_t)receivedData;
                rxCount++;
            }
        }

        ${MCSPI_INSTANCE_NAME?lower_case}Obj.rxCount = rxCount;
    }

    /* If there are more words to be transmitted, then transmit them here and keep track of the count */
    if((${MCSPI_INSTANCE_NAME}_REGS->MCSPI_SR & MCSPI_SR_TDRE_Msk) == MCSPI_SR_TDRE_Msk)
    {
        /* Disable the TDRE interrupt. This will be enabled back if more than
         * one byte is pending to be transmitted */
        ${MCSPI_INSTANCE_NAME}_REGS->MCSPI_IDR = MCSPI_IDR_TDRE_Msk;

        size_t txCount = ${MCSPI_INSTANCE_NAME?lower_case}Obj.txCount;

        if(dataBits == MCSPI_CSR_BITS_8_BIT)
        {
            if (txCount < ${MCSPI_INSTANCE_NAME?lower_case}Obj.txSize)
            {
                ${MCSPI_INSTANCE_NAME}_REGS->MCSPI_TDR = ((uint8_t*)${MCSPI_INSTANCE_NAME?lower_case}Obj.txBuffer)[txCount];
                txCount++;
            }
            else if (${MCSPI_INSTANCE_NAME?lower_case}Obj.dummySize > 0U)
            {
                ${MCSPI_INSTANCE_NAME}_REGS->MCSPI_TDR = (uint8_t)(0x${MCSPI_DUMMY_DATA});
                ${MCSPI_INSTANCE_NAME?lower_case}Obj.dummySize--;
            }
            else
            {
                /* Nothing to do */
            }
        }
        else
        {
            if (txCount < ${MCSPI_INSTANCE_NAME?lower_case}Obj.txSize)
            {
                ${MCSPI_INSTANCE_NAME}_REGS->MCSPI_TDR = ((uint16_t*)${MCSPI_INSTANCE_NAME?lower_case}Obj.txBuffer)[txCount];
                txCount++;
            }
            else if (${MCSPI_INSTANCE_NAME?lower_case}Obj.dummySize > 0U)
            {
                ${MCSPI_INSTANCE_NAME}_REGS->MCSPI_TDR = (uint16_t)(0x${MCSPI_DUMMY_DATA}${MCSPI_DUMMY_DATA});
                ${MCSPI_INSTANCE_NAME?lower_case}Obj.dummySize--;
            }
            else
            {
                /* Nothing to do */
            }

        }

        size_t dummySize = ${MCSPI_INSTANCE_NAME?lower_case}Obj.dummySize;
        ${MCSPI_INSTANCE_NAME?lower_case}Obj.txCount = txCount;

        if ((txCount == ${MCSPI_INSTANCE_NAME?lower_case}Obj.txSize) && (dummySize == 0U))
        {
            /* At higher baud rates, the data in the shift register can be
             * shifted out and TXEMPTY flag can get set resulting in a
             * callback been given to the application with the MCSPI interrupt
             * pending with the application. This will then result in the
             * interrupt handler being called again with nothing to transmit.
             * To avoid this, a software flag is set, but
             * the TXEMPTY interrupt is not enabled until the very end.
             */

            isLastByteTransferInProgress = true;

        }
        else if (${MCSPI_INSTANCE_NAME?lower_case}Obj.rxCount == rxSize)
        {
            /* Enable TDRE interrupt as all the requested bytes are received
             * and can now make use of the internal transmit shift register.
             */
            ${MCSPI_INSTANCE_NAME}_REGS->MCSPI_IDR = MCSPI_IDR_RDRF_Msk;
            ${MCSPI_INSTANCE_NAME}_REGS->MCSPI_IER = MCSPI_IDR_TDRE_Msk;
        }
        else
        {
            /* Nothing to do */
        }
    }

    /* See if Exchange is complete */
    if ((isLastByteTransferInProgress == true) && ((${MCSPI_INSTANCE_NAME}_REGS->MCSPI_SR & MCSPI_SR_TXEMPTY_Msk) == MCSPI_SR_TXEMPTY_Msk))
    {
        if (${MCSPI_INSTANCE_NAME?lower_case}Obj.rxCount == rxSize)
        {
            /* Set Last transfer to deassert NPCS after the last byte written in TDR has been transferred. */
            ${MCSPI_INSTANCE_NAME}_REGS->MCSPI_CR = MCSPI_CR_LASTXFER_Msk;

            ${MCSPI_INSTANCE_NAME?lower_case}Obj.transferIsBusy = false;

            /* Disable TDRE, RDRF and TXEMPTY interrupts */
            ${MCSPI_INSTANCE_NAME}_REGS->MCSPI_IDR = MCSPI_IDR_TDRE_Msk | MCSPI_IDR_RDRF_Msk | MCSPI_IDR_TXEMPTY_Msk;

            isLastByteTransferInProgress = false;

            if(${MCSPI_INSTANCE_NAME?lower_case}Obj.callback != NULL)
            {
                ${MCSPI_INSTANCE_NAME?lower_case}Obj.callback(context);
            }
        }
    }
    if (isLastByteTransferInProgress == true)
    {
        /* For the last byte transfer, the TDRE interrupt is already disabled.
         * Enable TXEMPTY interrupt to ensure no data is present in the shift
         * register before application callback is called.
         */
        ${MCSPI_INSTANCE_NAME}_REGS->MCSPI_IER = MCSPI_IER_TXEMPTY_Msk;
    }
    </#if>
}
<#else>
void __attribute__((used)) ${MCSPI_INSTANCE_NAME}_InterruptHandler(void)
{
<#if MCSPI_NUM_CSR == 1>
    uint32_t dataBits = ${MCSPI_INSTANCE_NAME}_REGS->MCSPI_CSR[${MCSPI_CSR_INDEX}] & MCSPI_CSR_BITS_Msk;
<#else>
    uint32_t dataBits = ${MCSPI_INSTANCE_NAME}_REGS->MCSPI_CSR[${MCSPI_INSTANCE_NAME}_ChipSelectGet()] & MCSPI_CSR_BITS_Msk;
</#if>
    uint32_t nTxPending = 0;
    uint8_t rxThreshold = 0;
    size_t rxCount = ${MCSPI_INSTANCE_NAME?lower_case}Obj.rxCount;
    size_t rxSize = ${MCSPI_INSTANCE_NAME?lower_case}Obj.rxSize;
    size_t txSize = ${MCSPI_INSTANCE_NAME?lower_case}Obj.txSize;

    while (((${MCSPI_INSTANCE_NAME}_REGS->MCSPI_SR & MCSPI_SR_RDRF_Msk ) != 0U) && (rxCount < rxSize))
    {
        if(dataBits == MCSPI_CSR_BITS_8_BIT)
        {
            ((uint8_t*)${MCSPI_INSTANCE_NAME?lower_case}Obj.rxBuffer)[rxCount] = MCSPI_RDR_8BIT_REG;
            rxCount++;
        }
        else
        {
            ((uint16_t*)${MCSPI_INSTANCE_NAME?lower_case}Obj.rxBuffer)[rxCount] = MCSPI_RDR_16BIT_REG;
            rxCount++;
        }
    }

    ${MCSPI_INSTANCE_NAME?lower_case}Obj.rxCount = rxCount;

    /* Clear RX FIFO. This is done for the case where RX size is less than TX size and hence data is not read and copied into the application rx buffer. */
    ${MCSPI_INSTANCE_NAME}_REGS->MCSPI_CR = MCSPI_CR_RXFCLR_Msk;

    nTxPending = (txSize - ${MCSPI_INSTANCE_NAME?lower_case}Obj.txCount);
    nTxPending += ${MCSPI_INSTANCE_NAME?lower_case}Obj.dummySize;

    if (nTxPending > 0U)
    {
        if (nTxPending < 16U)
        {
            rxThreshold = (uint8_t)nTxPending;
        }
        else
        {
            rxThreshold = 16;
        }

        /* Set RX FIFO level so as to generate interrupt after all bytes are transmitted and response from slave is received for all the bytes */
        /* RX FIFO level must be set first or else FIFO may be filled before RX threshold is set and hardware may not recognize threshold crossover and not generate threshold interrupt */
        ${MCSPI_INSTANCE_NAME}_REGS->MCSPI_FMR = (${MCSPI_INSTANCE_NAME}_REGS->MCSPI_FMR & ~MCSPI_FMR_RXFTHRES_Msk) | MCSPI_FMR_RXFTHRES(rxThreshold);

        (void) ${MCSPI_INSTANCE_NAME}_FIFO_Fill();
    }
    else
    {
        /* Set Last transfer to deassert NPCS after the last byte written in TDR has been transferred. */
        ${MCSPI_INSTANCE_NAME}_REGS->MCSPI_CR = MCSPI_CR_LASTXFER_Msk;

        ${MCSPI_INSTANCE_NAME?lower_case}Obj.transferIsBusy = false;

        /* Disable Receive FIFO Threshold interrupt */
        ${MCSPI_INSTANCE_NAME}_REGS->MCSPI_IDR = MCSPI_IDR_RXFTHF_Msk;

        if(${MCSPI_INSTANCE_NAME?lower_case}Obj.callback != NULL)
        {
            uintptr_t context = ${MCSPI_INSTANCE_NAME?lower_case}Obj.context;
            ${MCSPI_INSTANCE_NAME?lower_case}Obj.callback(context);
        }
    }
}
</#if>
</#if>