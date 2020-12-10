/*******************************************************************************
  SPI PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${SPI_INSTANCE_NAME?lower_case}_master.c

  Summary:
    ${SPI_INSTANCE_NAME} Master Source File

  Description:
    This file has implementation of all the interfaces provided for particular
    SPI peripheral.

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

#include "plib_${SPI_INSTANCE_NAME?lower_case}_master.h"

// *****************************************************************************
// *****************************************************************************
// Section: ${SPI_INSTANCE_NAME} Implementation
// *****************************************************************************
// *****************************************************************************
<#if SPI_INTERRUPT_MODE == true>

/* Global object to save SPI Exchange related data */
SPI_OBJECT ${SPI_INSTANCE_NAME?lower_case}Obj;
<#if USE_SPI_DMA?? && USE_SPI_DMA == true>

static uint8_t dummyDataBuffer[512];

static void setupDMA( void* pTransmitData, void* pReceiveData, size_t size )
{
    /* Always set up the rx channel first */
    ${SPI_INSTANCE_NAME}_REGS->SPI_RPR = (uint32_t) pReceiveData;
    ${SPI_INSTANCE_NAME}_REGS->SPI_RCR = (uint32_t) size;
    ${SPI_INSTANCE_NAME}_REGS->SPI_TPR = (uint32_t) pTransmitData;
    ${SPI_INSTANCE_NAME}_REGS->SPI_TCR = (uint32_t) size;
    ${SPI_INSTANCE_NAME}_REGS->SPI_PTCR = SPI_PTCR_RXTEN_Msk | SPI_PTCR_TXTEN_Msk;
    ${SPI_INSTANCE_NAME}_REGS->SPI_IER = SPI_IER_ENDRX_Msk;
}
</#if>
</#if>

void ${SPI_INSTANCE_NAME}_Initialize( void )
{
    /* Disable and Reset the SPI*/
    ${SPI_INSTANCE_NAME}_REGS->SPI_CR = SPI_CR_SPIDIS_Msk | SPI_CR_SWRST_Msk;

<#if SPI_INTERRUPT_MODE == true && SPI_FIFO_ENABLE == true>
    ${SPI_INSTANCE_NAME}_REGS->SPI_CR = SPI_CR_FIFOEN_Msk;
</#if>

<#if SPI_MR_MSTR =="MASTER">
    /* Enable Master mode, <#if SPI_CLK_SRC??>select source clock, </#if>select particular NPCS line for chip select and disable mode fault detection */
    ${SPI_INSTANCE_NAME}_REGS->SPI_MR = SPI_MR_MSTR_Msk | SPI_MR_DLYBCS(${SPI_MR_DLYBCS}) <#if SPI_CLK_SRC??>| SPI_MR_BRSRCCLK_${SPI_CLK_SRC} </#if><#if SPI_EN_NPCS0?? && SPI_EN_NPCS0 == true>| SPI_MR_PCS_NPCS0 <#elseif SPI_EN_NPCS1?? && SPI_EN_NPCS1 == true>| SPI_MR_PCS_NPCS1<#elseif SPI_EN_NPCS2?? && SPI_EN_NPCS2 == true> | SPI_MR_PCS_NPCS2 <#elseif SPI_EN_NPCS3?? && SPI_EN_NPCS3 == true> | SPI_MR_PCS_NPCS3 </#if> | SPI_MR_MODFDIS_Msk;
</#if>

<#if SPI_EN_NPCS0?? && SPI_EN_NPCS0 == true>
    /* Set up clock Polarity, data phase, Communication Width, Baud Rate */
    ${SPI_INSTANCE_NAME}_REGS->SPI_CSR[0] = SPI_CSR_CPOL_${SPI_CSR0_CPOL} | SPI_CSR_NCPHA_${SPI_CSR0_NCPHA} | SPI_CSR_BITS${SPI_CSR0_BITS} | SPI_CSR_SCBR(${SPI_CSR0_SCBR_VALUE})| SPI_CSR_DLYBS(${SPI_CSR0_DLYBS}) | SPI_CSR_DLYBCT(${SPI_CSR0_DLYBCT}) | SPI_CSR_CSAAT_Msk;
</#if>

<#if SPI_EN_NPCS1?? && SPI_EN_NPCS1 == true>
    /* Set up clock Polarity, data phase, Communication Width, Baud Rate */
    ${SPI_INSTANCE_NAME}_REGS->SPI_CSR[1] = SPI_CSR_CPOL_${SPI_CSR1_CPOL} | SPI_CSR_NCPHA_${SPI_CSR1_NCPHA} | SPI_CSR_BITS${SPI_CSR1_BITS} | SPI_CSR_SCBR(${SPI_CSR1_SCBR_VALUE})| SPI_CSR_DLYBS(${SPI_CSR1_DLYBS}) | SPI_CSR_DLYBCT(${SPI_CSR1_DLYBCT}) | SPI_CSR_CSAAT_Msk;
</#if>

<#if SPI_EN_NPCS2?? && SPI_EN_NPCS2 == true>
    /* Set up clock Polarity, data phase, Communication Width, Baud Rate */
    ${SPI_INSTANCE_NAME}_REGS->SPI_CSR[2] = SPI_CSR_CPOL_${SPI_CSR2_CPOL} | SPI_CSR_NCPHA_${SPI_CSR2_NCPHA} | SPI_CSR_BITS${SPI_CSR2_BITS} | SPI_CSR_SCBR(${SPI_CSR2_SCBR_VALUE})| SPI_CSR_DLYBS(${SPI_CSR2_DLYBS}) | SPI_CSR_DLYBCT(${SPI_CSR2_DLYBCT}) | SPI_CSR_CSAAT_Msk;
</#if>

<#if SPI_EN_NPCS3?? && SPI_EN_NPCS3 == true>
    /* Set up clock Polarity, data phase, Communication Width, Baud Rate */
    ${SPI_INSTANCE_NAME}_REGS->SPI_CSR[3] = SPI_CSR_CPOL_${SPI_CSR3_CPOL} | SPI_CSR_NCPHA_${SPI_CSR3_NCPHA} | SPI_CSR_BITS${SPI_CSR3_BITS} | SPI_CSR_SCBR(${SPI_CSR3_SCBR_VALUE})| SPI_CSR_DLYBS(${SPI_CSR3_DLYBS}) | SPI_CSR_DLYBCT(${SPI_CSR3_DLYBCT}) | SPI_CSR_CSAAT_Msk;
</#if>


<#if SPI_INTERRUPT_MODE == true >
    /* Initialize global variables */
    ${SPI_INSTANCE_NAME?lower_case}Obj.transferIsBusy = false;
    ${SPI_INSTANCE_NAME?lower_case}Obj.callback = NULL;
</#if>

    /* Enable ${SPI_INSTANCE_NAME} */
    ${SPI_INSTANCE_NAME}_REGS->SPI_CR = SPI_CR_SPIEN_Msk;
}

<#if SPI_NUM_CSR != 1>
static uint8_t ${SPI_INSTANCE_NAME}_ChipSelectGet(void)
{
    uint8_t pcs = (uint8_t)((${SPI_INSTANCE_NAME}_REGS->SPI_MR  & SPI_MR_PCS_Msk) >> SPI_MR_PCS_Pos);
    if (pcs == SPI_CHIP_SELECT_NPCS0)
    {
        return 0;
    }
<#if SPI_EN_NPCS1??>
    else if (pcs == SPI_CHIP_SELECT_NPCS1)
    {
        return 1;
    }
</#if>
<#if SPI_EN_NPCS2??>
    else if (pcs == SPI_CHIP_SELECT_NPCS2)
    {
        return 2;
    }
</#if>
<#if SPI_EN_NPCS3??>
    else if (pcs == SPI_CHIP_SELECT_NPCS3)
    {
        return 3;
    }
</#if>
    else
    {
        return 0;
    }
}

void ${SPI_INSTANCE_NAME}_ChipSelectSetup(SPI_CHIP_SELECT chipSelect)
{
    ${SPI_INSTANCE_NAME}_REGS->SPI_MR =  (${SPI_INSTANCE_NAME}_REGS->SPI_MR & ~SPI_MR_PCS_Msk) | SPI_MR_PCS(chipSelect);
}
</#if>

<#if SPI_INTERRUPT_MODE == false >
bool ${SPI_INSTANCE_NAME}_WriteRead( void* pTransmitData, size_t txSize, void* pReceiveData, size_t rxSize )
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

<#if SPI_NUM_CSR == 1>
        dataBits = ${SPI_INSTANCE_NAME}_REGS->SPI_CSR[${SPI_CSR_INDEX}] & SPI_CSR_BITS_Msk;
<#else>
        dataBits = ${SPI_INSTANCE_NAME}_REGS->SPI_CSR[${SPI_INSTANCE_NAME}_ChipSelectGet()] & SPI_CSR_BITS_Msk;
</#if>

        /* Flush out any unread data in SPI read buffer from the previous transfer */
        receivedData = (${SPI_INSTANCE_NAME}_REGS->SPI_RDR & SPI_RDR_RD_Msk) >> SPI_RDR_RD_Pos;

        if (rxSize > txSize)
        {
            dummySize = rxSize - txSize;
        }
        if (dataBits != SPI_CSR_BITS_8_BIT)
        {
            rxSize >>= 1;
            txSize >>= 1;
            dummySize >>= 1;
        }

        /* Make sure TDR is empty */
        while((bool)((${SPI_INSTANCE_NAME}_REGS->SPI_SR & SPI_SR_TDRE_Msk) >> SPI_SR_TDRE_Pos) == false);

        while ((txCount != txSize) || (dummySize != 0))
        {
            if (txCount != txSize)
            {
                if(dataBits == SPI_CSR_BITS_8_BIT)
                {
                    ${SPI_INSTANCE_NAME}_REGS->SPI_TDR = ((uint8_t*)pTransmitData)[txCount++];
                }
                else
                {
                    ${SPI_INSTANCE_NAME}_REGS->SPI_TDR = ((uint16_t*)pTransmitData)[txCount++];
                }
            }
            else if (dummySize > 0)
            {
                if(dataBits == SPI_CSR_BITS_8_BIT)
                {
                    ${SPI_INSTANCE_NAME}_REGS->SPI_TDR = 0x${SPI_DUMMY_DATA};
                }
                else
                {
                    ${SPI_INSTANCE_NAME}_REGS->SPI_TDR = (uint16_t)(0x${SPI_DUMMY_DATA}${SPI_DUMMY_DATA});
                }
                dummySize--;
            }

            if (rxSize == 0)
            {
                /* For transmit only request, wait for TDR to become empty */
                while((bool)((${SPI_INSTANCE_NAME}_REGS->SPI_SR & SPI_SR_TDRE_Msk) >> SPI_SR_TDRE_Pos) == false);
            }
            else
            {
                /* If data is read, wait for the Receiver Data Register to become full*/
                while((bool)((${SPI_INSTANCE_NAME}_REGS->SPI_SR & SPI_SR_RDRF_Msk) >> SPI_SR_RDRF_Pos) == false)
                {
                }

                receivedData = (${SPI_INSTANCE_NAME}_REGS->SPI_RDR & SPI_RDR_RD_Msk) >> SPI_RDR_RD_Pos;

                if (rxCount < rxSize)
                {
                    if(dataBits == SPI_CSR_BITS_8_BIT)
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
        while ((bool)((${SPI_INSTANCE_NAME}_REGS->SPI_SR & SPI_SR_TXEMPTY_Msk) >> SPI_SR_TXEMPTY_Pos) == false);

        /* Set Last transfer to deassert NPCS after the last byte written in TDR has been transferred. */
        ${SPI_INSTANCE_NAME}_REGS->SPI_CR = SPI_CR_LASTXFER_Msk;

        isSuccess = true;
    }
        return isSuccess;
}
<#else>

<#if SPI_FIFO_ENABLE == false>
bool ${SPI_INSTANCE_NAME}_WriteRead( void* pTransmitData, size_t txSize, void* pReceiveData, size_t rxSize )
{
    bool isRequestAccepted = false;
<#if USE_SPI_DMA?? && USE_SPI_DMA == true>
    uint32_t size = 0;

    /* Verify the request */
    if((((txSize > 0) && (pTransmitData != NULL)) || ((rxSize > 0) && (pReceiveData != NULL))) && (${SPI_INSTANCE_NAME?lower_case}Obj.transferIsBusy == false))
    {
        isRequestAccepted = true;

        ${SPI_INSTANCE_NAME?lower_case}Obj.transferIsBusy = true;

        ${SPI_INSTANCE_NAME?lower_case}Obj.txBuffer = pTransmitData;
        ${SPI_INSTANCE_NAME?lower_case}Obj.rxBuffer = pReceiveData;
        ${SPI_INSTANCE_NAME?lower_case}Obj.txCount = txSize;
        ${SPI_INSTANCE_NAME?lower_case}Obj.rxCount = rxSize;

        if ((txSize > 0) && (rxSize > 0))
        {
            /* Find the lower value among txSize and rxSize */
            (txSize >= rxSize) ? (size = rxSize) : (size = txSize);

            /* Calculate the remaining tx/rx bytes and total bytes transferred */
            ${SPI_INSTANCE_NAME?lower_case}Obj.rxCount -= size;
            ${SPI_INSTANCE_NAME?lower_case}Obj.txCount -= size;
            ${SPI_INSTANCE_NAME?lower_case}Obj.nBytesTransferred = size;

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
                ${SPI_INSTANCE_NAME?lower_case}Obj.rxCount -= size;
                ${SPI_INSTANCE_NAME?lower_case}Obj.nBytesTransferred = size;

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
                ${SPI_INSTANCE_NAME?lower_case}Obj.txCount -= size;
                ${SPI_INSTANCE_NAME?lower_case}Obj.nBytesTransferred = size;

                setupDMA(pTransmitData, dummyDataBuffer, size);
            }
        }
    }

    return isRequestAccepted;
<#else>
    uint32_t dummyData;

    /* Verify the request */
    if((((txSize > 0) && (pTransmitData != NULL)) || ((rxSize > 0) && (pReceiveData != NULL))) && (${SPI_INSTANCE_NAME?lower_case}Obj.transferIsBusy == false))
    {
        isRequestAccepted = true;
        ${SPI_INSTANCE_NAME?lower_case}Obj.txBuffer = pTransmitData;
        ${SPI_INSTANCE_NAME?lower_case}Obj.rxBuffer = pReceiveData;
        ${SPI_INSTANCE_NAME?lower_case}Obj.rxCount = 0;
        ${SPI_INSTANCE_NAME?lower_case}Obj.txCount = 0;
        ${SPI_INSTANCE_NAME?lower_case}Obj.dummySize = 0;

        if (pTransmitData != NULL)
        {
            ${SPI_INSTANCE_NAME?lower_case}Obj.txSize = txSize;
        }
        else
        {
            ${SPI_INSTANCE_NAME?lower_case}Obj.txSize = 0;
        }

        if (pReceiveData != NULL)
        {
            ${SPI_INSTANCE_NAME?lower_case}Obj.rxSize = rxSize;
        }
        else
        {
            ${SPI_INSTANCE_NAME?lower_case}Obj.rxSize = 0;
        }

        ${SPI_INSTANCE_NAME?lower_case}Obj.transferIsBusy = true;

        /* Flush out any unread data in SPI read buffer */
        dummyData = (${SPI_INSTANCE_NAME}_REGS->SPI_RDR & SPI_RDR_RD_Msk) >> SPI_RDR_RD_Pos;
        (void)dummyData;

        if (${SPI_INSTANCE_NAME?lower_case}Obj.rxSize > ${SPI_INSTANCE_NAME?lower_case}Obj.txSize)
        {
            ${SPI_INSTANCE_NAME?lower_case}Obj.dummySize = ${SPI_INSTANCE_NAME?lower_case}Obj.rxSize - ${SPI_INSTANCE_NAME?lower_case}Obj.txSize;
        }

        /* Start the first write here itself, rest will happen in ISR context */
<#if SPI_NUM_CSR == 1>
        if((${SPI_INSTANCE_NAME}_REGS->SPI_CSR[${SPI_CSR_INDEX}] & SPI_CSR_BITS_Msk) == SPI_CSR_BITS_8_BIT)
<#else>
        if((${SPI_INSTANCE_NAME}_REGS->SPI_CSR[${SPI_INSTANCE_NAME}_ChipSelectGet()] & SPI_CSR_BITS_Msk) == SPI_CSR_BITS_8_BIT)
</#if>
        {
            if (${SPI_INSTANCE_NAME?lower_case}Obj.txCount < ${SPI_INSTANCE_NAME?lower_case}Obj.txSize)
            {
                ${SPI_INSTANCE_NAME}_REGS->SPI_TDR = *((uint8_t*)${SPI_INSTANCE_NAME?lower_case}Obj.txBuffer);
                ${SPI_INSTANCE_NAME?lower_case}Obj.txCount++;
            }
            else if (${SPI_INSTANCE_NAME?lower_case}Obj.dummySize > 0)
            {
                ${SPI_INSTANCE_NAME}_REGS->SPI_TDR = (uint8_t)(0x${SPI_DUMMY_DATA});
                ${SPI_INSTANCE_NAME?lower_case}Obj.dummySize--;
            }
        }
        else
        {
            ${SPI_INSTANCE_NAME?lower_case}Obj.txSize >>= 1;
            ${SPI_INSTANCE_NAME?lower_case}Obj.dummySize >>= 1;
            ${SPI_INSTANCE_NAME?lower_case}Obj.rxSize >>= 1;

            if (${SPI_INSTANCE_NAME?lower_case}Obj.txCount < ${SPI_INSTANCE_NAME?lower_case}Obj.txSize)
            {
                ${SPI_INSTANCE_NAME}_REGS->SPI_TDR = *((uint16_t*)${SPI_INSTANCE_NAME?lower_case}Obj.txBuffer);
                ${SPI_INSTANCE_NAME?lower_case}Obj.txCount++;
            }
            else if (${SPI_INSTANCE_NAME?lower_case}Obj.dummySize > 0)
            {
                ${SPI_INSTANCE_NAME}_REGS->SPI_TDR = (uint16_t)(0x${SPI_DUMMY_DATA}${SPI_DUMMY_DATA});
                ${SPI_INSTANCE_NAME?lower_case}Obj.dummySize--;
            }
        }

        if (rxSize > 0)
        {
            /* Enable receive interrupt to complete the transfer in ISR context */
            ${SPI_INSTANCE_NAME}_REGS->SPI_IER = SPI_IER_RDRF_Msk;
        }
        else
        {
            /* Enable transmit interrupt to complete the transfer in ISR context */
            ${SPI_INSTANCE_NAME}_REGS->SPI_IER = SPI_IER_TDRE_Msk;
        }
    }

    return isRequestAccepted;
</#if>
}

<#else>
static uint8_t ${SPI_INSTANCE_NAME}_FIFO_Fill(void)
{
    uint8_t nDataCopiedToFIFO = 0;
<#if SPI_NUM_CSR == 1>
    uint32_t dataBits = ${SPI_INSTANCE_NAME}_REGS->SPI_CSR[${SPI_CSR_INDEX}] & SPI_CSR_BITS_Msk;
<#else>
    uint32_t dataBits = ${SPI_INSTANCE_NAME}_REGS->SPI_CSR[${SPI_INSTANCE_NAME}_ChipSelectGet()] & SPI_CSR_BITS_Msk;
</#if>

    while ((nDataCopiedToFIFO < 16) && (${SPI_INSTANCE_NAME}_REGS->SPI_SR & SPI_SR_TDRE_Msk))
    {
        if(dataBits == SPI_CSR_BITS_8_BIT)
        {
            if (${SPI_INSTANCE_NAME?lower_case}Obj.txCount < ${SPI_INSTANCE_NAME?lower_case}Obj.txSize)
            {
                *((uint8_t*)&${SPI_INSTANCE_NAME}_REGS->SPI_TDR) =  ((uint8_t*)${SPI_INSTANCE_NAME?lower_case}Obj.txBuffer)[${SPI_INSTANCE_NAME?lower_case}Obj.txCount++];
            }
            else if (${SPI_INSTANCE_NAME?lower_case}Obj.dummySize > 0)
            {
                *((uint8_t*)&${SPI_INSTANCE_NAME}_REGS->SPI_TDR) = (uint8_t)(0x${SPI_DUMMY_DATA});
                ${SPI_INSTANCE_NAME?lower_case}Obj.dummySize--;
            }
            else
            {
                break;
            }
        }
        else
        {
            if (${SPI_INSTANCE_NAME?lower_case}Obj.txCount < ${SPI_INSTANCE_NAME?lower_case}Obj.txSize)
            {
                *((uint16_t*)&${SPI_INSTANCE_NAME}_REGS->SPI_TDR) =  ((uint16_t*)${SPI_INSTANCE_NAME?lower_case}Obj.txBuffer)[${SPI_INSTANCE_NAME?lower_case}Obj.txCount++];
            }
            else if (${SPI_INSTANCE_NAME?lower_case}Obj.dummySize > 0)
            {
                *((uint16_t*)&${SPI_INSTANCE_NAME}_REGS->SPI_TDR) = (uint16_t)(0x${SPI_DUMMY_DATA}${SPI_DUMMY_DATA});
                ${SPI_INSTANCE_NAME?lower_case}Obj.dummySize--;
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

bool ${SPI_INSTANCE_NAME}_WriteRead (void* pTransmitData, size_t txSize, void* pReceiveData, size_t rxSize)
{
    bool isRequestAccepted = false;
    uint32_t nTxPending = 0;
    uint8_t rxThreshold = 0;

    /* Verify the request */
    if((((txSize > 0) && (pTransmitData != NULL)) || ((rxSize > 0) && (pReceiveData != NULL))) && (${SPI_INSTANCE_NAME?lower_case}Obj.transferIsBusy == false))
    {
        isRequestAccepted = true;
        ${SPI_INSTANCE_NAME?lower_case}Obj.txBuffer = pTransmitData;
        ${SPI_INSTANCE_NAME?lower_case}Obj.rxBuffer = pReceiveData;
        ${SPI_INSTANCE_NAME?lower_case}Obj.rxCount = 0;
        ${SPI_INSTANCE_NAME?lower_case}Obj.txCount = 0;
        ${SPI_INSTANCE_NAME?lower_case}Obj.dummySize = 0;

        if (pTransmitData != NULL)
        {
            ${SPI_INSTANCE_NAME?lower_case}Obj.txSize = txSize;
        }
        else
        {
            ${SPI_INSTANCE_NAME?lower_case}Obj.txSize = 0;
        }

        if (pReceiveData != NULL)
        {
            ${SPI_INSTANCE_NAME?lower_case}Obj.rxSize = rxSize;
        }
        else
        {
            ${SPI_INSTANCE_NAME?lower_case}Obj.rxSize = 0;
        }

        ${SPI_INSTANCE_NAME?lower_case}Obj.transferIsBusy = true;

        if (${SPI_INSTANCE_NAME?lower_case}Obj.rxSize > ${SPI_INSTANCE_NAME?lower_case}Obj.txSize)
        {
            ${SPI_INSTANCE_NAME?lower_case}Obj.dummySize = ${SPI_INSTANCE_NAME?lower_case}Obj.rxSize - ${SPI_INSTANCE_NAME?lower_case}Obj.txSize;
        }

<#if SPI_NUM_CSR == 1>
    if((${SPI_INSTANCE_NAME}_REGS->SPI_CSR[${SPI_CSR_INDEX}] & SPI_CSR_BITS_Msk) != SPI_CSR_BITS_8_BIT)
<#else>
    if((${SPI_INSTANCE_NAME}_REGS->SPI_CSR[${SPI_INSTANCE_NAME}_ChipSelectGet()] & SPI_CSR_BITS_Msk) != SPI_CSR_BITS_8_BIT)
</#if>
        {
            ${SPI_INSTANCE_NAME?lower_case}Obj.txSize >>= 1;
            ${SPI_INSTANCE_NAME?lower_case}Obj.dummySize >>= 1;
            ${SPI_INSTANCE_NAME?lower_case}Obj.rxSize >>= 1;
        }

        /* Clear TX and RX FIFO */
        ${SPI_INSTANCE_NAME}_REGS->SPI_CR = (SPI_CR_RXFCLR_Msk | SPI_CR_TXFCLR_Msk);

        nTxPending = (${SPI_INSTANCE_NAME?lower_case}Obj.txSize - ${SPI_INSTANCE_NAME?lower_case}Obj.txCount) + ${SPI_INSTANCE_NAME?lower_case}Obj.dummySize;

        if (nTxPending < 16)
        {
            rxThreshold = nTxPending;
        }
        else
        {
            rxThreshold = 16;
        }

        /* Set RX FIFO level so as to generate interrupt after all bytes are transmitted and response from slave is received for all the bytes */
        /* RX FIFO level must be set first or else FIFO may be filled before RX threshold is set and hardware may not recognize threshold crossover and not generate threshold interrupt */
        ${SPI_INSTANCE_NAME}_REGS->SPI_FMR = (${SPI_INSTANCE_NAME}_REGS->SPI_FMR & ~SPI_FMR_RXFTHRES_Msk) | SPI_FMR_RXFTHRES(rxThreshold);

        (void) ${SPI_INSTANCE_NAME}_FIFO_Fill();

        /* Enable RX FIFO Threshold interrupt */
        ${SPI_INSTANCE_NAME}_REGS->SPI_IER = SPI_IER_RXFTHF_Msk;
    }

    return isRequestAccepted;
}
</#if>
</#if>

bool ${SPI_INSTANCE_NAME}_Write( void* pTransmitData, size_t txSize )
{
    return(${SPI_INSTANCE_NAME}_WriteRead(pTransmitData, txSize, NULL, 0));
}

bool ${SPI_INSTANCE_NAME}_Read( void* pReceiveData, size_t rxSize )
{
    return(${SPI_INSTANCE_NAME}_WriteRead(NULL, 0, pReceiveData, rxSize));
}

bool ${SPI_INSTANCE_NAME}_TransferSetup( SPI_TRANSFER_SETUP * setup, uint32_t spiSourceClock )
{
    uint32_t scbr;

    if ((setup == NULL) || (setup->clockFrequency == 0))
    {
        return false;
    }

    if(spiSourceClock == 0)
    {
        // Fetch Master Clock Frequency directly
        spiSourceClock = ${SPI_MASTER_CLOCK};
    }

    scbr = spiSourceClock/setup->clockFrequency;

    if(scbr == 0)
    {
        scbr = 1;
    }
    else if(scbr > 255)
    {
        scbr = 255;
    }

<#if SPI_NUM_CSR == 1>
    ${SPI_INSTANCE_NAME}_REGS->SPI_CSR[${SPI_CSR_INDEX}] = (${SPI_INSTANCE_NAME}_REGS->SPI_CSR[${SPI_CSR_INDEX}] & ~(SPI_CSR_CPOL_Msk | SPI_CSR_NCPHA_Msk | SPI_CSR_BITS_Msk | SPI_CSR_SCBR_Msk)) |((uint32_t)setup->clockPolarity | (uint32_t)setup->clockPhase | (uint32_t)setup->dataBits | SPI_CSR_SCBR(scbr));
<#else>
    ${SPI_INSTANCE_NAME}_REGS->SPI_CSR[${SPI_INSTANCE_NAME}_ChipSelectGet()] = (${SPI_INSTANCE_NAME}_REGS->SPI_CSR[${SPI_INSTANCE_NAME}_ChipSelectGet()] & ~(SPI_CSR_CPOL_Msk | SPI_CSR_NCPHA_Msk | SPI_CSR_BITS_Msk | SPI_CSR_SCBR_Msk)) |((uint32_t)setup->clockPolarity | (uint32_t)setup->clockPhase | (uint32_t)setup->dataBits | SPI_CSR_SCBR(scbr));
</#if>

    return true;
}

<#if SPI_INTERRUPT_MODE == true >
void ${SPI_INSTANCE_NAME}_CallbackRegister( SPI_CALLBACK callback, uintptr_t context )
{
    ${SPI_INSTANCE_NAME?lower_case}Obj.callback = callback;
    ${SPI_INSTANCE_NAME?lower_case}Obj.context = context;
}

bool ${SPI_INSTANCE_NAME}_IsBusy( void )
{
    return ((${SPI_INSTANCE_NAME?lower_case}Obj.transferIsBusy) || ((${SPI_INSTANCE_NAME}_REGS->SPI_SR & SPI_SR_TXEMPTY_Msk) == 0));
}
<#if SPI_FIFO_ENABLE == false>
void ${SPI_INSTANCE_NAME}_InterruptHandler( void )
{
<#if USE_SPI_DMA?? && USE_SPI_DMA == true>
    uint32_t size;
    uint32_t index;
<#else>
    uint32_t dataBits;
    uint32_t receivedData;
    static bool isLastByteTransferInProgress = false;

<#if SPI_NUM_CSR == 1>
    dataBits = ${SPI_INSTANCE_NAME}_REGS->SPI_CSR[${SPI_CSR_INDEX}] & SPI_CSR_BITS_Msk;
<#else>
    dataBits = ${SPI_INSTANCE_NAME}_REGS->SPI_CSR[${SPI_INSTANCE_NAME}_ChipSelectGet()] & SPI_CSR_BITS_Msk;
</#if>

</#if>

    <#if USE_SPI_DMA?? && USE_SPI_DMA == true>
    if(${SPI_INSTANCE_NAME?lower_case}Obj.rxCount > 0)
    {
        /* txPending is 0. Need to use the dummy data buffer for transmission.
         * Find out the max data that can be received, given the limited size of the dummy data buffer.
         */
        (${SPI_INSTANCE_NAME?lower_case}Obj.rxCount > sizeof(dummyDataBuffer)) ?
            (size = sizeof(dummyDataBuffer)): (size = ${SPI_INSTANCE_NAME?lower_case}Obj.rxCount);

        index = ${SPI_INSTANCE_NAME?lower_case}Obj.nBytesTransferred;

        /* Calculate the remaining rx bytes and total bytes transferred */
        ${SPI_INSTANCE_NAME?lower_case}Obj.rxCount -= size;
        ${SPI_INSTANCE_NAME?lower_case}Obj.nBytesTransferred += size;

        setupDMA(dummyDataBuffer,(void *)&((uint8_t*)${SPI_INSTANCE_NAME?lower_case}Obj.rxBuffer)[index],size);
    }
    else if(${SPI_INSTANCE_NAME?lower_case}Obj.txCount > 0)
    {
        /* rxSize is 0. Need to use the dummy data buffer for reception.
         * Find out the max data that can be transmitted, given the limited size of the dummy data buffer.
         */
        (${SPI_INSTANCE_NAME?lower_case}Obj.txCount > sizeof(dummyDataBuffer)) ?
            (size = sizeof(dummyDataBuffer)): (size = ${SPI_INSTANCE_NAME?lower_case}Obj.txCount);

        index = ${SPI_INSTANCE_NAME?lower_case}Obj.nBytesTransferred;

        /* Calculate the remaining rx bytes and total bytes transferred */
        ${SPI_INSTANCE_NAME?lower_case}Obj.txCount -= size;
        ${SPI_INSTANCE_NAME?lower_case}Obj.nBytesTransferred += size;

        setupDMA((void *)&((uint8_t*)${SPI_INSTANCE_NAME?lower_case}Obj.txBuffer)[index], dummyDataBuffer, size);
    }
    else
    {
        ${SPI_INSTANCE_NAME?lower_case}Obj.transferIsBusy = false;

        /* Set Last transfer to deassert NPCS after the last byte written in TDR has been transferred. */
        ${SPI_INSTANCE_NAME}_REGS->SPI_CR = SPI_CR_LASTXFER_Msk;

        ${SPI_INSTANCE_NAME}_REGS->SPI_PTCR = SPI_PTCR_RXTDIS_Msk | SPI_PTCR_TXTDIS_Msk;
        ${SPI_INSTANCE_NAME}_REGS->SPI_IDR = SPI_IDR_ENDRX_Msk;

        if( ${SPI_INSTANCE_NAME?lower_case}Obj.callback != NULL )
        {
            ${SPI_INSTANCE_NAME?lower_case}Obj.callback(${SPI_INSTANCE_NAME?lower_case}Obj.context);
        }
    }
    <#else>
    if ((${SPI_INSTANCE_NAME}_REGS->SPI_SR & SPI_SR_RDRF_Msk ) == SPI_SR_RDRF_Msk)
    {
        receivedData = (${SPI_INSTANCE_NAME}_REGS->SPI_RDR & SPI_RDR_RD_Msk) >> SPI_RDR_RD_Pos;

        if (${SPI_INSTANCE_NAME?lower_case}Obj.rxCount < ${SPI_INSTANCE_NAME?lower_case}Obj.rxSize)
        {
            if(dataBits == SPI_CSR_BITS_8_BIT)
            {
                ((uint8_t*)${SPI_INSTANCE_NAME?lower_case}Obj.rxBuffer)[${SPI_INSTANCE_NAME?lower_case}Obj.rxCount++] = receivedData;
            }
            else
            {
                ((uint16_t*)${SPI_INSTANCE_NAME?lower_case}Obj.rxBuffer)[${SPI_INSTANCE_NAME?lower_case}Obj.rxCount++] = receivedData;
            }
        }
    }

    /* If there are more words to be transmitted, then transmit them here and keep track of the count */
    if((${SPI_INSTANCE_NAME}_REGS->SPI_SR & SPI_SR_TDRE_Msk) == SPI_SR_TDRE_Msk)
    {
        /* Disable the TDRE interrupt. This will be enabled back if more than
         * one byte is pending to be transmitted */
        ${SPI_INSTANCE_NAME}_REGS->SPI_IDR = SPI_IDR_TDRE_Msk;

        if(dataBits == SPI_CSR_BITS_8_BIT)
        {
            if (${SPI_INSTANCE_NAME?lower_case}Obj.txCount < ${SPI_INSTANCE_NAME?lower_case}Obj.txSize)
            {
                ${SPI_INSTANCE_NAME}_REGS->SPI_TDR = ((uint8_t*)${SPI_INSTANCE_NAME?lower_case}Obj.txBuffer)[${SPI_INSTANCE_NAME?lower_case}Obj.txCount++];
            }
            else if (${SPI_INSTANCE_NAME?lower_case}Obj.dummySize > 0)
            {
                ${SPI_INSTANCE_NAME}_REGS->SPI_TDR = (uint8_t)(0x${SPI_DUMMY_DATA});
                ${SPI_INSTANCE_NAME?lower_case}Obj.dummySize--;
            }
        }
        else
        {
            if (${SPI_INSTANCE_NAME?lower_case}Obj.txCount < ${SPI_INSTANCE_NAME?lower_case}Obj.txSize)
            {
                ${SPI_INSTANCE_NAME}_REGS->SPI_TDR = ((uint16_t*)${SPI_INSTANCE_NAME?lower_case}Obj.txBuffer)[${SPI_INSTANCE_NAME?lower_case}Obj.txCount++];
            }
            else if (${SPI_INSTANCE_NAME?lower_case}Obj.dummySize > 0)
            {
                ${SPI_INSTANCE_NAME}_REGS->SPI_TDR = (uint16_t)(0x${SPI_DUMMY_DATA}${SPI_DUMMY_DATA});
                ${SPI_INSTANCE_NAME?lower_case}Obj.dummySize--;
            }
        }
        if ((${SPI_INSTANCE_NAME?lower_case}Obj.txCount == ${SPI_INSTANCE_NAME?lower_case}Obj.txSize) && (${SPI_INSTANCE_NAME?lower_case}Obj.dummySize == 0))
        {
            /* At higher baud rates, the data in the shift register can be
             * shifted out and TXEMPTY flag can get set resulting in a
             * callback been given to the application with the SPI interrupt
             * pending with the application. This will then result in the
             * interrupt handler being called again with nothing to transmit.
             * To avoid this, a software flag is set, but
             * the TXEMPTY interrupt is not enabled until the very end.
             */

            isLastByteTransferInProgress = true;

        }
        else if (${SPI_INSTANCE_NAME?lower_case}Obj.rxCount == ${SPI_INSTANCE_NAME?lower_case}Obj.rxSize)
        {
            /* Enable TDRE interrupt as all the requested bytes are received
             * and can now make use of the internal transmit shift register.
             */
            ${SPI_INSTANCE_NAME}_REGS->SPI_IDR = SPI_IDR_RDRF_Msk;
            ${SPI_INSTANCE_NAME}_REGS->SPI_IER = SPI_IDR_TDRE_Msk;
        }
    }

    /* See if Exchange is complete */
    if ((isLastByteTransferInProgress == true) && ((${SPI_INSTANCE_NAME}_REGS->SPI_SR & SPI_SR_TXEMPTY_Msk) == SPI_SR_TXEMPTY_Msk))
    {
        if (${SPI_INSTANCE_NAME?lower_case}Obj.rxCount == ${SPI_INSTANCE_NAME?lower_case}Obj.rxSize)
        {
            /* Set Last transfer to deassert NPCS after the last byte written in TDR has been transferred. */
            ${SPI_INSTANCE_NAME}_REGS->SPI_CR = SPI_CR_LASTXFER_Msk;

            ${SPI_INSTANCE_NAME?lower_case}Obj.transferIsBusy = false;

            /* Disable TDRE, RDRF and TXEMPTY interrupts */
            ${SPI_INSTANCE_NAME}_REGS->SPI_IDR = SPI_IDR_TDRE_Msk | SPI_IDR_RDRF_Msk | SPI_IDR_TXEMPTY_Msk;

            isLastByteTransferInProgress = false;

            if(${SPI_INSTANCE_NAME?lower_case}Obj.callback != NULL)
            {
                ${SPI_INSTANCE_NAME?lower_case}Obj.callback(${SPI_INSTANCE_NAME?lower_case}Obj.context);
            }
        }
    }
    if (isLastByteTransferInProgress == true)
    {
        /* For the last byte transfer, the TDRE interrupt is already disabled.
         * Enable TXEMPTY interrupt to ensure no data is present in the shift
         * register before application callback is called.
         */
        ${SPI_INSTANCE_NAME}_REGS->SPI_IER = SPI_IER_TXEMPTY_Msk;
    }
    </#if>
}
<#else>
void ${SPI_INSTANCE_NAME}_InterruptHandler(void)
{
<#if SPI_NUM_CSR == 1>
    uint32_t dataBits = ${SPI_INSTANCE_NAME}_REGS->SPI_CSR[${SPI_CSR_INDEX}] & SPI_CSR_BITS_Msk;
<#else>
    uint32_t dataBits = ${SPI_INSTANCE_NAME}_REGS->SPI_CSR[${SPI_INSTANCE_NAME}_ChipSelectGet()] & SPI_CSR_BITS_Msk;
</#if>
    uint32_t nTxPending = 0;
    uint8_t rxThreshold = 0;

    while ((${SPI_INSTANCE_NAME}_REGS->SPI_SR & SPI_SR_RDRF_Msk ) && (${SPI_INSTANCE_NAME?lower_case}Obj.rxCount < ${SPI_INSTANCE_NAME?lower_case}Obj.rxSize))
    {
        if(dataBits == SPI_CSR_BITS_8_BIT)
        {
            ((uint8_t*)${SPI_INSTANCE_NAME?lower_case}Obj.rxBuffer)[${SPI_INSTANCE_NAME?lower_case}Obj.rxCount++] = *((uint8_t*)&${SPI_INSTANCE_NAME}_REGS->SPI_RDR);
        }
        else
        {
            ((uint16_t*)${SPI_INSTANCE_NAME?lower_case}Obj.rxBuffer)[${SPI_INSTANCE_NAME?lower_case}Obj.rxCount++] = *((uint16_t*)&${SPI_INSTANCE_NAME}_REGS->SPI_RDR);
        }
    }

    /* Clear RX FIFO. This is done for the case where RX size is less than TX size and hence data is not read and copied into the application rx buffer. */
    ${SPI_INSTANCE_NAME}_REGS->SPI_CR = SPI_CR_RXFCLR_Msk;

    nTxPending = (${SPI_INSTANCE_NAME?lower_case}Obj.txSize - ${SPI_INSTANCE_NAME?lower_case}Obj.txCount) + ${SPI_INSTANCE_NAME?lower_case}Obj.dummySize;

    if (nTxPending > 0)
    {
        if (nTxPending < 16)
        {
            rxThreshold = nTxPending;
        }
        else
        {
            rxThreshold = 16;
        }

        /* Set RX FIFO level so as to generate interrupt after all bytes are transmitted and response from slave is received for all the bytes */
        /* RX FIFO level must be set first or else FIFO may be filled before RX threshold is set and hardware may not recognize threshold crossover and not generate threshold interrupt */
        ${SPI_INSTANCE_NAME}_REGS->SPI_FMR = (${SPI_INSTANCE_NAME}_REGS->SPI_FMR & ~SPI_FMR_RXFTHRES_Msk) | SPI_FMR_RXFTHRES(rxThreshold);

        (void) ${SPI_INSTANCE_NAME}_FIFO_Fill();
    }
    else
    {
        /* Set Last transfer to deassert NPCS after the last byte written in TDR has been transferred. */
        ${SPI_INSTANCE_NAME}_REGS->SPI_CR = SPI_CR_LASTXFER_Msk;

        ${SPI_INSTANCE_NAME?lower_case}Obj.transferIsBusy = false;

        /* Disable Receive FIFO Threshold interrupt */
        ${SPI_INSTANCE_NAME}_REGS->SPI_IDR = SPI_IDR_RXFTHF_Msk;

        if(${SPI_INSTANCE_NAME?lower_case}Obj.callback != NULL)
        {
            ${SPI_INSTANCE_NAME?lower_case}Obj.callback(${SPI_INSTANCE_NAME?lower_case}Obj.context);
        }
    }
}
</#if>
</#if>