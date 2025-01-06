/*******************************************************************************
  ${FLEXCOM_INSTANCE_NAME} SPI PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${FLEXCOM_INSTANCE_NAME?lower_case}_spi_master.c

  Summary:
    ${FLEXCOM_INSTANCE_NAME} SPI Master PLIB Implementation File.

  Description:
    This file defines the interface to the FLEXCOM SPI Master peripheral library.
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

// *****************************************************************************
// *****************************************************************************
// Section: ${FLEXCOM_INSTANCE_NAME} SPI Implementation
// *****************************************************************************
// *****************************************************************************

<#if SPI_INTERRUPT_MODE == true>
/* Global object to save FLEXCOM SPI Exchange related data */
static volatile FLEXCOM_SPI_OBJECT ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj;

<#if USE_SPI_DMA?? && USE_SPI_DMA == true>
static volatile uint8_t dummyDataBuffer[512];

static void setupDMA( volatile void* pTransmitData, volatile void* pReceiveData, size_t size )
{
    /* Always set up the rx channel first */
    SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_RPR = (volatile uint32_t)(volatile uint32_t*)pReceiveData;
    SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_RCR = (uint32_t) size;
    SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_TPR = (volatile uint32_t)(volatile uint32_t*)pTransmitData;
    SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_TCR = (uint32_t) size;
    SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_PTCR = SPI_PTCR_RXTEN_Msk | SPI_PTCR_TXTEN_Msk;
    SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_IER = SPI_IER_ENDRX_Msk;
}

</#if>
</#if>
void ${FLEXCOM_INSTANCE_NAME}_SPI_Initialize( void )
{
    /* Set FLEXCOM SPI operating mode */
    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEXCOM_MR = FLEXCOM_MR_OPMODE_SPI;

    /* Disable and Reset the FLEXCOM SPI */
    SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_CR = SPI_CR_SPIDIS_Msk | SPI_CR_SWRST_Msk;

<#if FLEXCOM_SPI_MR_MSTR == "MASTER">
    /* Enable Master mode, select clock source, select particular NPCS line for chip select and disable mode fault detection */
    SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_MR = SPI_MR_MSTR_Msk | SPI_MR_BRSRCCLK_${FLEXCOM_SPI_MR_BRSRCCLK} | SPI_MR_DLYBCS(${FLEXCOM_SPI_MR_DLYBCS}) <#if FLEXCOM_SPI_EN_NPCS0?? && FLEXCOM_SPI_EN_NPCS0 == true>| SPI_MR_PCS(FLEXCOM_SPI_CHIP_SELECT_NPCS0)<#elseif FLEXCOM_SPI_EN_NPCS1?? && FLEXCOM_SPI_EN_NPCS1 == true>| SPI_MR_PCS(FLEXCOM_SPI_CHIP_SELECT_NPCS1) <#elseif FLEXCOM_SPI_EN_NPCS2?? && FLEXCOM_SPI_EN_NPCS2 == true>| SPI_MR_PCS(FLEXCOM_SPI_CHIP_SELECT_NPCS2) <#elseif FLEXCOM_SPI_EN_NPCS3?? && FLEXCOM_SPI_EN_NPCS3 == true>| SPI_MR_PCS(FLEXCOM_SPI_CHIP_SELECT_NPCS3)</#if> | SPI_MR_MODFDIS_Msk;
</#if>

<#if FLEXCOM_SPI_EN_NPCS0?? && FLEXCOM_SPI_EN_NPCS0 == true>
    /* Set up clock Polarity, data phase, Communication Width, Baud Rate */
    SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_CSR[0] = SPI_CSR_CPOL(${FLEXCOM_SPI_CSR0_CPOL}) | SPI_CSR_NCPHA(${FLEXCOM_SPI_CSR0_NCPHA}) | SPI_CSR_BITS${FLEXCOM_SPI_CSR0_BITS} | SPI_CSR_SCBR(${FLEXCOM_SPI_CSR0_SCBR_VALUE})| SPI_CSR_DLYBS(${FLEXCOM_SPI_CSR0_DLYBS}) | SPI_CSR_DLYBCT(${FLEXCOM_SPI_CSR0_DLYBCT}) <#if FLEXCOM_SPI_CSR0_CSAAT == true> | SPI_CSR_CSAAT_Msk <#elseif FLEXCOM_SPI_CSR0_CSNAAT == true>  | SPI_CSR_CSNAAT_Msk </#if>;
</#if>

<#if FLEXCOM_SPI_EN_NPCS1?? && FLEXCOM_SPI_EN_NPCS1 == true>
    /* Set up clock Polarity, data phase, Communication Width, Baud Rate */
    SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_CSR[1] = SPI_CSR_CPOL(${FLEXCOM_SPI_CSR1_CPOL}) | SPI_CSR_NCPHA(${FLEXCOM_SPI_CSR1_NCPHA}) | SPI_CSR_BITS${FLEXCOM_SPI_CSR1_BITS} | SPI_CSR_SCBR(${FLEXCOM_SPI_CSR1_SCBR_VALUE})| SPI_CSR_DLYBS(${FLEXCOM_SPI_CSR1_DLYBS}) | SPI_CSR_DLYBCT(${FLEXCOM_SPI_CSR1_DLYBCT}) <#if FLEXCOM_SPI_CSR1_CSAAT == true> | SPI_CSR_CSAAT_Msk <#elseif FLEXCOM_SPI_CSR1_CSNAAT == true>  | SPI_CSR_CSNAAT_Msk </#if>;
</#if>

<#if FLEXCOM_SPI_EN_NPCS2?? && FLEXCOM_SPI_EN_NPCS2 == true>
    /* Set up clock Polarity, data phase, Communication Width, Baud Rate */
    SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_CSR[2] = SPI_CSR_CPOL(${FLEXCOM_SPI_CSR2_CPOL}) | SPI_CSR_NCPHA(${FLEXCOM_SPI_CSR2_NCPHA}) | SPI_CSR_BITS${FLEXCOM_SPI_CSR2_BITS} | SPI_CSR_SCBR(${FLEXCOM_SPI_CSR2_SCBR_VALUE})| SPI_CSR_DLYBS(${FLEXCOM_SPI_CSR2_DLYBS}) | SPI_CSR_DLYBCT(${FLEXCOM_SPI_CSR2_DLYBCT}) <#if FLEXCOM_SPI_CSR2_CSAAT == true> | SPI_CSR_CSAAT_Msk <#elseif FLEXCOM_SPI_CSR2_CSNAAT == true>  | SPI_CSR_CSNAAT_Msk </#if>;
</#if>

<#if FLEXCOM_SPI_EN_NPCS3?? && FLEXCOM_SPI_EN_NPCS3 == true>
    /* Set up clock Polarity, data phase, Communication Width, Baud Rate */
    SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_CSR[3] = SPI_CSR_CPOL(${FLEXCOM_SPI_CSR3_CPOL}) | SPI_CSR_NCPHA(${FLEXCOM_SPI_CSR3_NCPHA}) | SPI_CSR_BITS${FLEXCOM_SPI_CSR3_BITS} | SPI_CSR_SCBR(${FLEXCOM_SPI_CSR3_SCBR_VALUE})| SPI_CSR_DLYBS(${FLEXCOM_SPI_CSR3_DLYBS}) | SPI_CSR_DLYBCT(${FLEXCOM_SPI_CSR3_DLYBCT}) <#if FLEXCOM_SPI_CSR3_CSAAT == true> SPI_CSR_CSAAT_Msk <#elseif FLEXCOM_SPI_CSR3_CSNAAT == true>  | SPI_CSR_CSNAAT_Msk </#if>;
</#if>


<#if SPI_INTERRUPT_MODE == true >
    /* Initialize global variables */
    ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.transferIsBusy = false;
    ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.callback = NULL;
</#if>

    /* Enable ${FLEXCOM_INSTANCE_NAME} SPI */
    SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_CR = SPI_CR_SPIEN_Msk;
}

<#if FLEXCOM_SPI_NUM_CSR != 1>
static uint8_t ${FLEXCOM_INSTANCE_NAME}_SPI_ChipSelectGet(void)
{
    uint8_t pcs = (uint8_t)((SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_MR  & SPI_MR_PCS_Msk) >> SPI_MR_PCS_Pos);

    if (pcs == (uint8_t)FLEXCOM_SPI_CHIP_SELECT_NPCS0)
    {
        return 0;
    }
<#if FLEXCOM_SPI_EN_NPCS1??>
    else if (pcs == (uint8_t)FLEXCOM_SPI_CHIP_SELECT_NPCS1)
    {
        return 1;
    }
</#if>
<#if FLEXCOM_SPI_EN_NPCS2??>
    else if (pcs == (uint8_t)FLEXCOM_SPI_CHIP_SELECT_NPCS2)
    {
        return 2;
    }
</#if>
<#if FLEXCOM_SPI_EN_NPCS3??>
    else if (pcs == (uint8_t)FLEXCOM_SPI_CHIP_SELECT_NPCS3)
    {
        return 3;
    }
</#if>
    else
    {
        return 0;
    }
}

void ${FLEXCOM_INSTANCE_NAME}_SPI_ChipSelectSetup(FLEXCOM_SPI_CHIP_SELECT chipSelect)
{
    SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_MR =  (SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_MR & ~SPI_MR_PCS_Msk) | SPI_MR_PCS(chipSelect);
}
</#if>

<#if SPI_INTERRUPT_MODE == false>
bool ${FLEXCOM_INSTANCE_NAME}_SPI_WriteRead( void* pTransmitData, size_t txSize, void* pReceiveData, size_t rxSize )
{
    size_t txCount = 0;
    size_t rxCount = 0;
    size_t dummySize = 0;
    size_t receivedData = 0;
    uint32_t dataBits = 0U;
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
        dataBits = SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_CSR[${FLEXCOM_SPI_CSR_INDEX}] & SPI_CSR_BITS_Msk;
<#else>
        dataBits = SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_CSR[${FLEXCOM_INSTANCE_NAME}_SPI_ChipSelectGet()] & SPI_CSR_BITS_Msk;
</#if>

        /* Flush out any unread data in SPI read buffer from the previous transfer */
        receivedData = (SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_RDR & SPI_RDR_RD_Msk) >> SPI_RDR_RD_Pos;

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
        while((SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_SR & SPI_SR_TDRE_Msk) == 0U)
        {
            /* Wait for TDRE flag to rise */
        }

        while ((txCount != txSize) || (dummySize != 0U))
        {
            if (txCount != txSize)
            {
                if(dataBits == SPI_CSR_BITS_8_BIT)
                {
                    SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_TDR = ((uint8_t*)pTransmitData)[txCount++];
                }
                else
                {
                    SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_TDR = ((uint16_t*)pTransmitData)[txCount++];
                }
            }
            else if (dummySize > 0U)
            {
                SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_TDR = 0x${FLEXCOM_SPI_DUMMY_DATA};
                dummySize--;
            }
            else
            {
                /* Do nothing */
            }

            if (rxSize == 0U)
            {
                /* For transmit only request, wait for TDR to become empty */
                while((SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_SR & SPI_SR_TDRE_Msk) == 0U)
                {
                   /* Wait for TDRE flag to rise */
                }
            }
            else
            {
                /* If data is read, wait for the Receiver Data Register to become full*/
                while((SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_SR & SPI_SR_RDRF_Msk) == 0U)
                {
                    /* Wait for RDRF flag to rise */
                }

                receivedData = (SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_RDR & SPI_RDR_RD_Msk) >> SPI_RDR_RD_Pos;

                if (rxCount < rxSize)
                {
                    if(dataBits == SPI_CSR_BITS_8_BIT)
                    {
                        ((uint8_t*)pReceiveData)[rxCount++] = (uint8_t)receivedData;
                    }
                    else
                    {
                        ((uint16_t*)pReceiveData)[rxCount++] = (uint16_t)receivedData;
                    }
                }
            }
        }

        /* Make sure no data is pending in the shift register */
        while ((SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_SR & SPI_SR_TXEMPTY_Msk) == 0U)
        {
            /* Wait for TXEMPTY flag to rise */
        }

        <#if FLEXCOM_SPI_MR_PCS != "GPIO">
        /* Set Last transfer to deassert NPCS after the last byte written in TDR has been transferred. */
        SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_CR = SPI_CR_LASTXFER_Msk;

        </#if>
        isSuccess = true;
    }

    return isSuccess;
}
<#else>
bool ${FLEXCOM_INSTANCE_NAME}_SPI_WriteRead( void* pTransmitData, size_t txSize, void* pReceiveData, size_t rxSize )
{
    bool isRequestAccepted = false;
<#if USE_SPI_DMA?? && USE_SPI_DMA == true>
    uint32_t size = 0U;

    /* Verify the request */
    if (${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.transferIsBusy == false)
    {
        if(((txSize > 0U) && (pTransmitData != NULL)) || ((rxSize > 0U) && (pReceiveData != NULL)))
        {
            isRequestAccepted = true;

            ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.transferIsBusy = true;

            ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txBuffer = pTransmitData;
            ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.rxBuffer = pReceiveData;
            ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txCount = txSize;
            ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.rxCount = rxSize;

            if ((txSize > 0U) && (rxSize > 0U))
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
                if (rxSize > 0U)
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
    }

    return isRequestAccepted;
<#else>
    uint32_t dummyData;
    size_t txSz;

    /* Verify the request */
    if (${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.transferIsBusy == false)
    {
        if(((txSize > 0U) && (pTransmitData != NULL)) || ((rxSize > 0U) && (pReceiveData != NULL)))
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
            dummyData = (SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_RDR & SPI_RDR_RD_Msk) >> SPI_RDR_RD_Pos;
            (void)dummyData;

            txSz = ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txSize;

            if (${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.rxSize > txSz)
            {
                ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.dummySize = ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.rxSize - txSz;
            }

<#if FLEXCOM_SPI_NUM_CSR == 1>
            /* Start the first write here itself, rest will happen in ISR context */
            if((SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_CSR[${FLEXCOM_SPI_CSR_INDEX}] & SPI_CSR_BITS_Msk) == SPI_CSR_BITS_8_BIT)
<#else>
            if((SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_CSR[${FLEXCOM_INSTANCE_NAME}_SPI_ChipSelectGet()] & SPI_CSR_BITS_Msk) == SPI_CSR_BITS_8_BIT)
</#if>
            {
                if (${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txCount < txSz)
                {
                    SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_TDR = *((uint8_t*)${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txBuffer);
                    ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txCount++;
                }
                else if (${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.dummySize > 0U)
                {
                    SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_TDR = (uint8_t)(0x${FLEXCOM_SPI_DUMMY_DATA});
                    ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.dummySize--;
                }
                else
                {
                    /* Do Nothing */
                }
            }
            else
            {
                ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txSize >>= 1;
                ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.dummySize >>= 1;
                ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.rxSize >>= 1;

                txSz = ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txSize;

                if (${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txCount < txSz)
                {
                    SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_TDR = *((uint16_t*)${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txBuffer);
                    ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txCount++;
                }
                else if (${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.dummySize > 0U)
                {
                    SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_TDR = (uint16_t)(0x${FLEXCOM_SPI_DUMMY_DATA});
                    ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.dummySize--;
                }
                else
                {
                    /* Do Nothing */
                }
            }

            if (rxSize > 0U)
            {
                /* Enable receive interrupt to complete the transfer in ISR context */
                SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_IER = SPI_IER_RDRF_Msk;
            }
            else
            {
                /* Enable transmit interrupt to complete the transfer in ISR context */
                SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_IER = SPI_IER_TDRE_Msk;
            }
        }
    }

    return isRequestAccepted;
</#if>
}
</#if>

bool ${FLEXCOM_INSTANCE_NAME}_SPI_TransferSetup( FLEXCOM_SPI_TRANSFER_SETUP * setup, uint32_t spiSourceClock )
{
<#assign flexcomClockSymbol = "core." + FLEXCOM_INSTANCE_NAME + "_CLOCK_FREQUENCY">
    uint32_t scbr;

    if ((setup == NULL) || (setup->clockFrequency == 0U))
    {
        return false;
    }
    if(spiSourceClock == 0U)
    {
        // Fetch Master Clock Frequency directly
        spiSourceClock = ${flexcomClockSymbol?eval};
    }

    scbr = spiSourceClock/setup->clockFrequency;

    if(scbr == 0U)
    {
        scbr = 1U;
    }
    else if(scbr > 255U)
    {
        scbr = 255U;
    }
    else
    {
        /* Do Nothing */
    }

<#if FLEXCOM_SPI_NUM_CSR == 1>
    SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_CSR[${FLEXCOM_SPI_CSR_INDEX}] = (SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_CSR[${FLEXCOM_SPI_CSR_INDEX}] & ~(SPI_CSR_CPOL_Msk | SPI_CSR_NCPHA_Msk | SPI_CSR_BITS_Msk | SPI_CSR_SCBR_Msk)) | ((uint32_t)setup->clockPolarity | (uint32_t)setup->clockPhase | (uint32_t)setup->dataBits | SPI_CSR_SCBR(scbr));
<#else>
    SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_CSR[${FLEXCOM_INSTANCE_NAME}_SPI_ChipSelectGet()] = (SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_CSR[${FLEXCOM_SPI_CSR_INDEX}] & ~(SPI_CSR_CPOL_Msk | SPI_CSR_NCPHA_Msk | SPI_CSR_BITS_Msk | SPI_CSR_SCBR_Msk)) | ((uint32_t)setup->clockPolarity | (uint32_t)setup->clockPhase | (uint32_t)setup->dataBits | SPI_CSR_SCBR(scbr));
</#if>

    return true;
}

bool ${FLEXCOM_INSTANCE_NAME}_SPI_Write( void* pTransmitData, size_t txSize )
{
    return (${FLEXCOM_INSTANCE_NAME}_SPI_WriteRead(pTransmitData, txSize, NULL, 0));
}

bool ${FLEXCOM_INSTANCE_NAME}_SPI_Read( void* pReceiveData, size_t rxSize )
{
    return (${FLEXCOM_INSTANCE_NAME}_SPI_WriteRead(NULL, 0, pReceiveData, rxSize));
}

bool ${FLEXCOM_INSTANCE_NAME}_SPI_IsTransmitterBusy( void )
{
    return ((SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_SR & SPI_SR_TXEMPTY_Msk) == 0U);
}

<#if SPI_INTERRUPT_MODE == true>
void ${FLEXCOM_INSTANCE_NAME}_SPI_CallbackRegister( FLEXCOM_SPI_CALLBACK callback, uintptr_t context )
{
    ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.callback = callback;
    ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.context = context;
}

bool ${FLEXCOM_INSTANCE_NAME}_SPI_IsBusy( void )
{
    bool transferIsBusy = ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.transferIsBusy;

    return (((SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_SR & SPI_SR_TXEMPTY_Msk) == 0U) || (transferIsBusy));
}

void __attribute__((used)) ${FLEXCOM_INSTANCE_NAME}_InterruptHandler( void )
{
<#if !(USE_SPI_DMA?? && USE_SPI_DMA == true)>
    uint32_t dataBits;
    uint32_t receivedData;
<#if FLEXCOM_SPI_NUM_CSR == 1>
    dataBits = SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_CSR[${FLEXCOM_SPI_CSR_INDEX}] & SPI_CSR_BITS_Msk;
<#else>
    dataBits = SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_CSR[${FLEXCOM_INSTANCE_NAME}_SPI_ChipSelectGet()] & SPI_CSR_BITS_Msk;
</#if>

    static bool isLastByteTransferInProgress = false;
<#else>
    uint32_t size;
    uint32_t index;
</#if>

    uintptr_t context = ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.context;

    /* save the status in global object before it gets cleared */
    ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.status = SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_SR;

    <#if USE_SPI_DMA?? && USE_SPI_DMA == true>
    SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_PTCR = SPI_PTCR_ERRCLR_Msk;

    if(${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.rxCount > 0U)
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

        setupDMA(dummyDataBuffer, &((uint8_t*)${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.rxBuffer)[index],size);
    }
    else if(${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txCount > 0U)
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

        setupDMA(&((uint8_t*)${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txBuffer)[index], dummyDataBuffer, size);
    }
    else
    {
        ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.transferIsBusy = false;

        <#if FLEXCOM_SPI_MR_PCS != "GPIO">
        /* Set Last transfer to deassert NPCS after the last byte written in TDR has been transferred. */
        SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_CR = SPI_CR_LASTXFER_Msk;

        </#if>
        SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_PTCR = SPI_PTCR_RXTDIS_Msk | SPI_PTCR_TXTDIS_Msk;
        SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_IDR = SPI_IDR_ENDRX_Msk;

        if( ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.callback != NULL )
        {
            ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.callback(context);
        }
    }
    <#else>

    size_t rxCount = ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.rxCount;
    size_t txCount = ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txCount;
    size_t txSize = ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txSize;

    if ((SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_SR & SPI_SR_RDRF_Msk) == SPI_SR_RDRF_Msk)
    {
        receivedData = (SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_RDR & SPI_RDR_RD_Msk) >> SPI_RDR_RD_Pos;

        if (rxCount < ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.rxSize)
        {
            if(dataBits == SPI_CSR_BITS_8_BIT)
            {
                ((uint8_t*)${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.rxBuffer)[rxCount] = (uint8_t)receivedData;
            }
            else
            {
                ((uint16_t*)${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.rxBuffer)[rxCount] = (uint16_t)receivedData;
            }
            rxCount++;
        }
    }

    /* If there are more words to be transmitted, then transmit them here and keep track of the count */
    if((SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_SR & SPI_SR_TDRE_Msk) == SPI_SR_TDRE_Msk)
    {
        /* Disable the TDRE interrupt. This will be enabled back if more than
         * one byte is pending to be transmitted */
        SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_IDR = SPI_IDR_TDRE_Msk;

        if(dataBits == SPI_CSR_BITS_8_BIT)
        {
            if (txCount < txSize)
            {
                SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_TDR = ((uint8_t*)${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txBuffer)[txCount];
                txCount++;
            }
            else if (${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.dummySize > 0U)
            {
                SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_TDR = (uint8_t)(0x${FLEXCOM_SPI_DUMMY_DATA});
                ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.dummySize--;
            }
            else
            {
                /* Do Nothing */
            }
        }
        else
        {
            if (txCount < txSize)
            {
                SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_TDR = ((uint16_t*)${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txBuffer)[txCount];
                txCount++;
            }
            else if (${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.dummySize > 0U)
            {
                SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_TDR = (uint16_t)(0x${FLEXCOM_SPI_DUMMY_DATA});
                ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.dummySize--;
            }
            else
            {
                /* Do Nothing */
            }
        }
        if ((${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.dummySize == 0U) && (txCount == txSize))
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
            <#if FLEXCOM_SPI_MR_PCS != "GPIO">

            /* Set Last transfer to deassert NPCS after the last byte written in TDR has been transferred. */
            SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_CR = SPI_CR_LASTXFER_Msk;
            </#if>
        }
        else if (rxCount == ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.rxSize)
        {
            /* Enable TDRE interrupt as all the requested bytes are received
             * and can now make use of the internal transmit shift register.
             */
            SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_IDR = SPI_IDR_RDRF_Msk;
            SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_IER = SPI_IDR_TDRE_Msk;
        }
        else
        {
            /* Do Nothing */
        }
    }

    ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.rxCount = rxCount;
    ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.txCount = txCount;

    /* See if Exchange is complete */
    if ((isLastByteTransferInProgress == true) && ((SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_SR & SPI_SR_TXEMPTY_Msk) == SPI_SR_TXEMPTY_Msk))
    {
        if (rxCount == ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.rxSize)
        {
            ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.transferIsBusy = false;

            /* Disable TDRE, RDRF and TXEMPTY interrupts */
            SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_IDR = SPI_IDR_TDRE_Msk | SPI_IDR_RDRF_Msk | SPI_IDR_TXEMPTY_Msk;

            isLastByteTransferInProgress = false;

            if(${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.callback != NULL)
            {
                ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.callback(context);
            }
        }
    }
    if (isLastByteTransferInProgress == true)
    {
        /* For the last byte transfer, the TDRE interrupt is already disabled.
         * Enable TXEMPTY interrupt to ensure no data is present in the shift
         * register before application callback is called.
         */
        SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_IER = SPI_IER_TXEMPTY_Msk;
    }

    </#if>
}
</#if>