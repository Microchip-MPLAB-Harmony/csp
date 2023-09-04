/*******************************************************************************
  ${QMSPI_INSTANCE_NAME} SPI Peripheral Library Source File

  Company
    Microchip Technology Inc.

  File Name
    plib_${QMSPI_INSTANCE_NAME?lower_case}_spi.c

  Summary
    ${QMSPI_INSTANCE_NAME} SPI mode peripheral library interface.

  Description

  Remarks:

*******************************************************************************/

// DOM-IGNORE-BEGIN
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
// DOM-IGNORE-END
<#if core.CoreSysIntFile == true>
#include "interrupts.h"
</#if>
#include "plib_${QMSPI_INSTANCE_NAME?lower_case}_spi.h"
<#if QMSPI_INTERRUPT_MODE == true || QMSPI_DMA_EN == true>
#include "../ecia/plib_ecia.h"
</#if>

<#if QMSPI_DMA_EN == true>
typedef struct
{
    uint8_t*                pTxBuffer;
    uint8_t*                pRxBuffer;
    size_t                  txSize;
    size_t                  rxSize;
    size_t                  rxCount;
    size_t                  txCount;
    size_t                  rxPending;
    size_t                  txPending;
    uint32_t                txDummyData;
    uint32_t                rxDummyData;
    bool                    transferIsBusy;
<#if QMSPI_DESCRIPTOR_MODE_EN?? && QMSPI_DESCRIPTOR_MODE_EN == true>
    bool                    dmaDescInProgress;
</#if>
    QMSPI_SPI_CALLBACK      callback;
    uintptr_t               context;

} QMSPI_SPI_OBJECT ;
<#elseif QMSPI_INTERRUPT_MODE == true>
typedef struct
{
    uint8_t*                pTxBuffer;
    uint8_t*                pRxBuffer;
    size_t                  txSize;
    size_t                  rxSize;
    size_t                  dummySize;
    size_t                  rxCount;
    size_t                  txCount;
    bool                    transferIsBusy;
    QMSPI_SPI_CALLBACK      callback;
    uintptr_t               context;

} QMSPI_SPI_OBJECT ;
</#if>


<#if QMSPI_INTERRUPT_MODE == true || QMSPI_DMA_EN == true>
/* Global object to save SPI Exchange related data */
volatile static QMSPI_SPI_OBJECT ${QMSPI_INSTANCE_NAME?lower_case}Obj;
</#if>

// *****************************************************************************
// *****************************************************************************
// ${QMSPI_INSTANCE_NAME} PLIB Interface Routines
// *****************************************************************************
// *****************************************************************************

<#assign QMSPI_CPHA_VAL = "0">
<#if QMSPI_CPOL == "LOW">
    <#if QMSPI_CPHA == "FALLING">
        <#assign QMSPI_CPHA_VAL = "1">
    </#if>
<#else>
    <#if QMSPI_CPHA == "RISING">
        <#assign QMSPI_CPHA_VAL = "1">
    </#if>
</#if>

void ${QMSPI_INSTANCE_NAME}_SPI_Initialize(void)
{
    /* Reset the QMSPI Block */
    ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_MODE = QMSPI_MODE_SOFT_RESET_Msk;

    ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_MODE = <@compress single_line=true>
    QMSPI_MODE_CLK_DIV(${QMSPI_CLOCK_DIVIDE}U) |
    QMSPI_MODE_CHPA_MOSI(${QMSPI_CPHA_VAL}) |
    QMSPI_MODE_CHPA_MISO(${QMSPI_CPHA_VAL})
    <#if QMSPI_HARDWARE_CS_EN == true> | QMSPI_MODE_CS(${QMSPI_HARDWARE_CS_SEL}) </#if>
    <#if QMSPI_CPOL == "HIGH"> | QMSPI_MODE_CPOL_Msk </#if>
    </@compress>;

    /* Activate the QMSPI Block */
    ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_MODE |= QMSPI_MODE_ACT_Msk;
}

bool ${QMSPI_INSTANCE_NAME}_SPI_TransferSetup (QMSPI_SPI_TRANSFER_SETUP *setup)
{
    uint32_t clock_divide;
    bool setupStatus = false;

    if (setup != NULL)
    {
        clock_divide = ${QMSPI_SRC_CLK_FREQ}U / setup->clockFrequency;

        if (clock_divide >= 256U)
        {
            clock_divide = 0;
        }

        ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_MODE =
        ( (${QMSPI_INSTANCE_NAME}_REGS->QMSPI_MODE & ~(QMSPI_MODE_CLK_DIV_Msk | QMSPI_MODE_CHPA_MOSI_Msk | QMSPI_MODE_CHPA_MISO_Msk | QMSPI_MODE_CPOL_Msk)) | (QMSPI_MODE_CLK_DIV(clock_divide) | (uint32_t)setup->clockPhase | (uint32_t)setup->clockPolarity));

        setupStatus = true;
    }
    return setupStatus;
}

bool ${QMSPI_INSTANCE_NAME}_SPI_Write(void* pTransmitData, size_t txSize)
{
    return(${QMSPI_INSTANCE_NAME}_SPI_WriteRead(pTransmitData, txSize, NULL, 0));
}

bool ${QMSPI_INSTANCE_NAME}_SPI_Read(void* pReceiveData, size_t rxSize)
{
    return(${QMSPI_INSTANCE_NAME}_SPI_WriteRead(NULL, 0, pReceiveData, rxSize));
}

<#if QMSPI_INTERRUPT_MODE == true || QMSPI_DMA_EN == true>

void ${QMSPI_INSTANCE_NAME}_SPI_CallbackRegister(QMSPI_SPI_CALLBACK callback, uintptr_t context)
{
    ${QMSPI_INSTANCE_NAME?lower_case}Obj.callback = callback;
    ${QMSPI_INSTANCE_NAME?lower_case}Obj.context = context;
}

bool ${QMSPI_INSTANCE_NAME}_SPI_IsBusy (void)
{
    bool transferIsBusy = ${QMSPI_INSTANCE_NAME?lower_case}Obj.transferIsBusy;

    return transferIsBusy;
}


bool ${QMSPI_INSTANCE_NAME}_SPI_IsTransmitterBusy(void)
{
    return ((${QMSPI_INSTANCE_NAME}_REGS->QMSPI_STS & QMSPI_STS_TRANS_ACTIV_Msk) != 0U);
}

</#if>

<#if QMSPI_DMA_EN == true>
<#-- DMA Mode -->
bool ${QMSPI_INSTANCE_NAME}_SPI_WriteRead (void* pTransmitData, size_t txSize, void* pReceiveData, size_t rxSize)
{
    bool rxAddrInc = false;
    bool txAddrInc = false;
    bool isSuccess = false;
    size_t transferSize;

    /* Verify the request */
    if(((txSize > 0U) && (pTransmitData != NULL)) || ((rxSize > 0U) && (pReceiveData != NULL)))
    {
        if(pTransmitData == NULL)
        {
            txSize = 0U;
        }

        if(pReceiveData == NULL)
        {
            rxSize = 0U;
        }

        ${QMSPI_INSTANCE_NAME?lower_case}Obj.txSize = txSize;
        ${QMSPI_INSTANCE_NAME?lower_case}Obj.rxSize = rxSize;
        ${QMSPI_INSTANCE_NAME?lower_case}Obj.pTxBuffer = pTransmitData;
        ${QMSPI_INSTANCE_NAME?lower_case}Obj.pRxBuffer = pReceiveData;
        ${QMSPI_INSTANCE_NAME?lower_case}Obj.rxPending = 0;
        ${QMSPI_INSTANCE_NAME?lower_case}Obj.txPending = 0;
        ${QMSPI_INSTANCE_NAME?lower_case}Obj.txDummyData = 0xFFFFFFFFU;

        if ((rxSize == txSize) || (rxSize == 0U) || (txSize == 0U))
        {
            // Transfer size will be the max of ${QMSPI_INSTANCE_NAME?lower_case}Obj.rxSize and ${QMSPI_INSTANCE_NAME?lower_case}Obj.txSize
            transferSize = rxSize > txSize ? rxSize : txSize;
        }
        else
        {
            // Transfer size will be min of ${QMSPI_INSTANCE_NAME?lower_case}Obj.rxSize and ${QMSPI_INSTANCE_NAME?lower_case}Obj.txSize
            transferSize = rxSize > txSize ? txSize : rxSize;

            if (rxSize > txSize)
            {
                ${QMSPI_INSTANCE_NAME?lower_case}Obj.rxPending = (rxSize - txSize);
            }
            else
            {
                ${QMSPI_INSTANCE_NAME?lower_case}Obj.txPending = (txSize - rxSize);
            }
        }

        rxAddrInc = ${QMSPI_INSTANCE_NAME?lower_case}Obj.rxSize == 0U ? false:true;

        txAddrInc = ${QMSPI_INSTANCE_NAME?lower_case}Obj.txSize == 0U ? false:true;

        ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_MODE |= QMSPI_MODE_LDMA_RXEN_Msk | QMSPI_MODE_LDMA_TXEN_Msk;

        /* Flush out any unread data in SPI DATA Register from the previous transfer */
        ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_EXE = QMSPI_EXE_CLR_DAT_BUFF_Msk;

        ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_CTRL = QMSPI_CTRL_TRANS_UNITS(0x01) | QMSPI_CTRL_TRANS_LEN(transferSize) | QMSPI_CTRL_TX_TRANS_EN(0x01) | QMSPI_CTRL_TX_DMA_EN(1) | QMSPI_CTRL_RX_TRANS_EN_Msk | QMSPI_CTRL_RX_DMA_EN(1);

        <#if QMSPI_HARDWARE_CS_EN == true>
        if (${QMSPI_INSTANCE_NAME?lower_case}Obj.txPending == 0U)
        {
            if (${QMSPI_INSTANCE_NAME?lower_case}Obj.rxPending == 0U)
            {
                ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_CTRL |= QMSPI_CTRL_CLOSE_TRANS_EN_Msk;
            }
        }
        </#if>

        if (txAddrInc)
        {
            ${QMSPI_INSTANCE_NAME}_REGS->LDMA_TX[0].QMSPI_LDMA_TXCTRL = QMSPI_LDMA_TXCTRL_CH_EN_Msk | QMSPI_LDMA_TXCTRL_INC_ADDR_EN_Msk;
            ${QMSPI_INSTANCE_NAME}_REGS->LDMA_TX[0].QMSPI_LDMA_TXSTRT_ADDR = (uint32_t)${QMSPI_INSTANCE_NAME?lower_case}Obj.pTxBuffer;
        }
        else
        {
            ${QMSPI_INSTANCE_NAME}_REGS->LDMA_TX[0].QMSPI_LDMA_TXCTRL = QMSPI_LDMA_TXCTRL_CH_EN_Msk;
            ${QMSPI_INSTANCE_NAME}_REGS->LDMA_TX[0].QMSPI_LDMA_TXSTRT_ADDR = (uint32_t)&${QMSPI_INSTANCE_NAME?lower_case}Obj.txDummyData;
        }

        ${QMSPI_INSTANCE_NAME}_REGS->LDMA_TX[0].QMSPI_LDMA_TX_LEN = transferSize;

        if (rxAddrInc)
        {
            ${QMSPI_INSTANCE_NAME}_REGS->LDMA_RX[0].QMSPI_LDMA_RXCTRL = QMSPI_LDMA_RXCTRL_CH_EN_Msk | QMSPI_LDMA_RXCTRL_INC_ADDR_EN_Msk;
            ${QMSPI_INSTANCE_NAME}_REGS->LDMA_RX[0].QMSPI_LDMA_RXSTRT_ADDR = (uint32_t)${QMSPI_INSTANCE_NAME?lower_case}Obj.pRxBuffer;
        }
        else
        {
            ${QMSPI_INSTANCE_NAME}_REGS->LDMA_RX[0].QMSPI_LDMA_RXCTRL = QMSPI_LDMA_RXCTRL_CH_EN_Msk;
            ${QMSPI_INSTANCE_NAME}_REGS->LDMA_RX[0].QMSPI_LDMA_RXSTRT_ADDR = (uint32_t)&${QMSPI_INSTANCE_NAME?lower_case}Obj.rxDummyData;
        }

        ${QMSPI_INSTANCE_NAME?lower_case}Obj.transferIsBusy = true;

        ${QMSPI_INSTANCE_NAME}_REGS->LDMA_RX[0].QMSPI_LDMA_RX_LEN = transferSize;

        ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_IEN = QMSPI_IEN_TRANS_COMPL_EN_Msk;
        ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_EXE = QMSPI_EXE_START_Msk;

        isSuccess = true;
    }

    return isSuccess;
}

void __attribute__((used)) ${QMSPI_NVIC_INTERRUPT_NAME}_InterruptHandler(void)
{
    bool txAddrInc = false;
    bool rxAddrInc = false;
    size_t transferSize;
    size_t txPending = ${QMSPI_INSTANCE_NAME?lower_case}Obj.txPending;
    size_t rxPending = ${QMSPI_INSTANCE_NAME?lower_case}Obj.rxPending;
    size_t txSize = ${QMSPI_INSTANCE_NAME?lower_case}Obj.txSize;
    size_t rxSize = ${QMSPI_INSTANCE_NAME?lower_case}Obj.rxSize;

    <#if QMSPI_INTERRUPT_TYPE == "AGGREGATE">
    if (ECIA_GIRQResultGet(ECIA_AGG_INT_SRC_QMSPI${QMSPI_INSTANCE_NUM}) != 0U)
    <#else>
    if (ECIA_GIRQResultGet(ECIA_DIR_INT_SRC_QMSPI${QMSPI_INSTANCE_NUM}) != 0U)
    </#if>
    {
        <#if QMSPI_INTERRUPT_TYPE == "AGGREGATE">
        ECIA_GIRQSourceClear(ECIA_AGG_INT_SRC_QMSPI${QMSPI_INSTANCE_NUM});
        <#else>
        ECIA_GIRQSourceClear(ECIA_DIR_INT_SRC_QMSPI${QMSPI_INSTANCE_NUM});
        </#if>

        if ((${QMSPI_INSTANCE_NAME}_REGS->QMSPI_STS & QMSPI_STS_TRANS_COMPL_Msk) != 0U)
        {
            ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_STS |= QMSPI_STS_TRANS_COMPL_Msk;

            if ( ((${QMSPI_INSTANCE_NAME}_REGS->QMSPI_CTRL & QMSPI_CTRL_DESCR_BUFF_EN_Msk) == 0U) && ((txPending > 0U) || (rxPending > 0U)) )
            {
                txAddrInc = ${QMSPI_INSTANCE_NAME?lower_case}Obj.txPending > 0U? true : false;
                rxAddrInc = ${QMSPI_INSTANCE_NAME?lower_case}Obj.rxPending > 0U? true : false;

                transferSize = txPending > rxPending? txPending : rxPending;

                ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_CTRL = QMSPI_CTRL_TRANS_UNITS(0x01) | QMSPI_CTRL_TRANS_LEN(transferSize) | QMSPI_CTRL_TX_TRANS_EN(0x01) | QMSPI_CTRL_TX_DMA_EN(1) | QMSPI_CTRL_RX_TRANS_EN_Msk | QMSPI_CTRL_RX_DMA_EN(1) <#if QMSPI_HARDWARE_CS_EN == true> | QMSPI_CTRL_CLOSE_TRANS_EN_Msk </#if>;

                if (txAddrInc)
                {
                    ${QMSPI_INSTANCE_NAME}_REGS->LDMA_TX[0].QMSPI_LDMA_TXCTRL = QMSPI_LDMA_TXCTRL_CH_EN_Msk | QMSPI_LDMA_TXCTRL_INC_ADDR_EN_Msk;
                    ${QMSPI_INSTANCE_NAME}_REGS->LDMA_TX[0].QMSPI_LDMA_TXSTRT_ADDR = (uint32_t)&${QMSPI_INSTANCE_NAME?lower_case}Obj.pTxBuffer[txSize - txPending];
                }
                else
                {
                    ${QMSPI_INSTANCE_NAME}_REGS->LDMA_TX[0].QMSPI_LDMA_TXCTRL = QMSPI_LDMA_TXCTRL_CH_EN_Msk;
                    ${QMSPI_INSTANCE_NAME}_REGS->LDMA_TX[0].QMSPI_LDMA_TXSTRT_ADDR = (uint32_t)&${QMSPI_INSTANCE_NAME?lower_case}Obj.txDummyData;
                }

                ${QMSPI_INSTANCE_NAME}_REGS->LDMA_TX[0].QMSPI_LDMA_TX_LEN = transferSize;

                if (rxAddrInc)
                {
                    ${QMSPI_INSTANCE_NAME}_REGS->LDMA_RX[0].QMSPI_LDMA_RXCTRL = QMSPI_LDMA_RXCTRL_CH_EN_Msk | QMSPI_LDMA_RXCTRL_INC_ADDR_EN_Msk;
                    ${QMSPI_INSTANCE_NAME}_REGS->LDMA_RX[0].QMSPI_LDMA_RXSTRT_ADDR = (uint32_t)&${QMSPI_INSTANCE_NAME?lower_case}Obj.pRxBuffer[rxSize - rxPending];
                }
                else
                {
                    ${QMSPI_INSTANCE_NAME}_REGS->LDMA_RX[0].QMSPI_LDMA_RXCTRL = QMSPI_LDMA_RXCTRL_CH_EN_Msk;
                    ${QMSPI_INSTANCE_NAME}_REGS->LDMA_RX[0].QMSPI_LDMA_RXSTRT_ADDR = (uint32_t)&${QMSPI_INSTANCE_NAME?lower_case}Obj.rxDummyData;
                }

                ${QMSPI_INSTANCE_NAME?lower_case}Obj.txPending = ${QMSPI_INSTANCE_NAME?lower_case}Obj.rxPending = 0;

                ${QMSPI_INSTANCE_NAME}_REGS->LDMA_RX[0].QMSPI_LDMA_RX_LEN = transferSize;

                ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_IEN = QMSPI_IEN_TRANS_COMPL_EN_Msk;
                ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_EXE = QMSPI_EXE_START_Msk;
            }
            else
            {
                ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_IEN &= ~QMSPI_IEN_TRANS_COMPL_EN_Msk;

                ${QMSPI_INSTANCE_NAME?lower_case}Obj.transferIsBusy = false;

                if (${QMSPI_INSTANCE_NAME?lower_case}Obj.callback != NULL)
                {
                    uintptr_t context = ${QMSPI_INSTANCE_NAME?lower_case}Obj.context;

                    ${QMSPI_INSTANCE_NAME?lower_case}Obj.callback(context);
                }
            }
        }
    }
}

<#if QMSPI_DESCRIPTOR_MODE_EN?? && QMSPI_DESCRIPTOR_MODE_EN == true>
void QMSPI_TransferDescriptorSetup(uint8_t descNum, QMSPI_SPI_DMA_TRANS_DESC desc)
{
    ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_MODE |= QMSPI_MODE_LDMA_RXEN_Msk | QMSPI_MODE_LDMA_TXEN_Msk;

    ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_DESC_LDMA_RXEN = QMSPI_DESC_LDMA_RXEN_Msk;
    ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_DESC_LDMA_TXEN = QMSPI_DESC_LDMA_TXEN_Msk;

    ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_CTRL = QMSPI_CTRL_DESCR_BUFF_EN_Msk | QMSPI_CTRL_DESCR_BUFF_PTR(0);

    ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_DESCR[descNum] = QMSPI_DESCR_TX_LEN(desc.transfer_length) |
                                                        QMSPI_DESCR_DESCR_BUF_LAST(desc.is_desc_last == true? 1:0) |
                                                        QMSPI_DESCR_DESCR_BUF_NXT_PTR(desc.next_desc_num) |
                                                        QMSPI_DESCR_TRANS_LEN(1) |
                                                        QMSPI_DESCR_CLOSE_TRANS_EN(desc.close_transfer_en == true? 1:0) |
                                                        QMSPI_DESCR_RX_TRANS_EN(desc.rx_en == true? 1:0) |
                                                        QMSPI_DESCR_TX_TRANS_EN(desc.tx_en == true? 1:0) |
                                                        QMSPI_DESCR_RX_DMA_EN(desc.rx_en == true? (desc.rx_dma_ch_num + 1) :0) |
                                                        QMSPI_DESCR_TX_DMA_EN(desc.tx_en == true? (desc.tx_dma_ch_num + 1) :0) |
                                                        QMSPI_DESCR_INFACE_MOD(desc.interface_mode);
    if (desc.rx_en)
    {
        ${QMSPI_INSTANCE_NAME}_REGS->LDMA_RX[desc.rx_dma_ch_num].QMSPI_LDMA_RXCTRL = QMSPI_LDMA_RXCTRL_CH_EN_Msk | QMSPI_LDMA_RXCTRL_INC_ADDR_EN(desc.rx_addr_inc == true? 1: 0);
        ${QMSPI_INSTANCE_NAME}_REGS->LDMA_RX[desc.rx_dma_ch_num].QMSPI_LDMA_RXSTRT_ADDR = desc.rx_des_addr;
        ${QMSPI_INSTANCE_NAME}_REGS->LDMA_RX[desc.rx_dma_ch_num].QMSPI_LDMA_RX_LEN = desc.transfer_length;
    }

    if (desc.tx_en)
    {
        ${QMSPI_INSTANCE_NAME}_REGS->LDMA_TX[desc.tx_dma_ch_num].QMSPI_LDMA_TXCTRL = QMSPI_LDMA_TXCTRL_CH_EN_Msk | QMSPI_LDMA_TXCTRL_INC_ADDR_EN(desc.tx_addr_inc == true? 1: 0);
        ${QMSPI_INSTANCE_NAME}_REGS->LDMA_TX[desc.tx_dma_ch_num].QMSPI_LDMA_TXSTRT_ADDR = desc.tx_src_addr;
        ${QMSPI_INSTANCE_NAME}_REGS->LDMA_TX[desc.tx_dma_ch_num].QMSPI_LDMA_TX_LEN = desc.transfer_length;
    }

    if (desc.is_desc_last)
    {
        ${QMSPI_INSTANCE_NAME?lower_case}Obj.transferIsBusy = true;

        ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_EXE = QMSPI_EXE_CLR_DAT_BUFF_Msk;
        ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_IEN = QMSPI_IEN_TRANS_COMPL_EN_Msk;
        ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_EXE = QMSPI_EXE_START_Msk;
    }
}
</#if>
</#if>

<#if QMSPI_INTERRUPT_MODE == true && QMSPI_DMA_EN == false>
<#-- Interrupt Mode -->
bool ${QMSPI_INSTANCE_NAME}_SPI_WriteRead (void* pTransmitData, size_t txSize, void* pReceiveData, size_t rxSize)
{
    bool isRequestAccepted = false;
    size_t txCount = 0;
    size_t dummySize = 0;

    /* Verify the request */
    if((${QMSPI_INSTANCE_NAME?lower_case}Obj.transferIsBusy == false) && (((txSize > 0U) && (pTransmitData != NULL)) || ((rxSize > 0U) && (pReceiveData != NULL))))
    {
        if(pTransmitData == NULL)
        {
            txSize = 0U;
        }

        if(pReceiveData == NULL)
        {
            rxSize = 0U;
        }

        ${QMSPI_INSTANCE_NAME?lower_case}Obj.txSize = txSize;
        ${QMSPI_INSTANCE_NAME?lower_case}Obj.rxSize = rxSize;
        ${QMSPI_INSTANCE_NAME?lower_case}Obj.pTxBuffer = pTransmitData;
        ${QMSPI_INSTANCE_NAME?lower_case}Obj.pRxBuffer = pReceiveData;
        ${QMSPI_INSTANCE_NAME?lower_case}Obj.rxCount = 0;
        ${QMSPI_INSTANCE_NAME?lower_case}Obj.txCount = 0;
        ${QMSPI_INSTANCE_NAME?lower_case}Obj.dummySize = 0;

        ${QMSPI_INSTANCE_NAME?lower_case}Obj.transferIsBusy = true;

        /* Flush out any unread data in SPI DATA Register from the previous transfer */
        ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_EXE = QMSPI_EXE_CLR_DAT_BUFF_Msk;

        if(rxSize > txSize)
        {
            dummySize = rxSize - txSize;
        }

        while (((${QMSPI_INSTANCE_NAME}_REGS->QMSPI_STS & QMSPI_STS_TX_BUFF_FULL_Msk) == 0U) && ((txCount != txSize) || (dummySize > 0U)))
        {
            if (txCount != txSize)
            {
                *((volatile uint8_t*)&${QMSPI_INSTANCE_NAME}_REGS->QMSPI_TX_FIFO[0]) = ${QMSPI_INSTANCE_NAME?lower_case}Obj.pTxBuffer[txCount];
                txCount++;
            }
            else if (dummySize > 0U)
            {
                *((volatile uint8_t*)&${QMSPI_INSTANCE_NAME}_REGS->QMSPI_TX_FIFO[0]) = 0xFFU;
                dummySize--;
            }
            else
            {
                /* Do nothing */
            }
        }

        uint32_t transferCount = ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_BUF_CNT_STS & QMSPI_BUF_CNT_STS_TX_BUFF_CNT_Msk;

        ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_CTRL = QMSPI_CTRL_TRANS_UNITS(0x01) | QMSPI_CTRL_TRANS_LEN(transferCount) | QMSPI_CTRL_TX_TRANS_EN(0x01) | QMSPI_CTRL_RX_TRANS_EN_Msk;

        <#if QMSPI_HARDWARE_CS_EN == true>
        if ((txCount == txSize) && (dummySize == 0U))
        {
            ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_CTRL |= QMSPI_CTRL_CLOSE_TRANS_EN_Msk;
        }
        </#if>

        ${QMSPI_INSTANCE_NAME?lower_case}Obj.txCount = txCount;
        ${QMSPI_INSTANCE_NAME?lower_case}Obj.dummySize = dummySize;

        ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_IEN = QMSPI_IEN_TRANS_COMPL_EN_Msk;
        ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_EXE = QMSPI_EXE_START_Msk;

        isRequestAccepted = true;
    }

    return isRequestAccepted;
}

void __attribute__((used)) ${QMSPI_NVIC_INTERRUPT_NAME}_InterruptHandler(void)
{
    volatile uint8_t receivedData;
    uint32_t rxSize = ${QMSPI_INSTANCE_NAME?lower_case}Obj.rxSize;
    uint32_t rxCount = ${QMSPI_INSTANCE_NAME?lower_case}Obj.rxCount;
    uint32_t txSize = ${QMSPI_INSTANCE_NAME?lower_case}Obj.txSize;
    uint32_t txCount = ${QMSPI_INSTANCE_NAME?lower_case}Obj.txCount;
    uint32_t dummySize = ${QMSPI_INSTANCE_NAME?lower_case}Obj.dummySize;

    <#if QMSPI_INTERRUPT_TYPE == "AGGREGATE">
    if (ECIA_GIRQResultGet(ECIA_AGG_INT_SRC_QMSPI${QMSPI_INSTANCE_NUM}) != 0U)
    <#else>
    if (ECIA_GIRQResultGet(ECIA_DIR_INT_SRC_QMSPI${QMSPI_INSTANCE_NUM}) != 0U)
    </#if>
    {
        <#if QMSPI_INTERRUPT_TYPE == "AGGREGATE">
        ECIA_GIRQSourceClear(ECIA_AGG_INT_SRC_QMSPI${QMSPI_INSTANCE_NUM});
        <#else>
        ECIA_GIRQSourceClear(ECIA_DIR_INT_SRC_QMSPI${QMSPI_INSTANCE_NUM});
        </#if>

        if ((${QMSPI_INSTANCE_NAME}_REGS->QMSPI_STS & QMSPI_STS_TRANS_COMPL_Msk) != 0U)
        {
            ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_STS |= QMSPI_STS_TRANS_COMPL_Msk;

            /* Read the received data from the FIFO */
            while ((${QMSPI_INSTANCE_NAME}_REGS->QMSPI_STS & QMSPI_STS_RX_BUFF_EMP_Msk) == 0U)
            {
                receivedData = *((volatile uint8_t*)&${QMSPI_INSTANCE_NAME}_REGS->QMSPI_RX_FIFO[0]);
                if(rxCount < rxSize)
                {
                    ${QMSPI_INSTANCE_NAME?lower_case}Obj.pRxBuffer[rxCount] = (uint8_t)receivedData;
                    rxCount++;
                }
            }

            ${QMSPI_INSTANCE_NAME?lower_case}Obj.rxCount = rxCount;

            if ((txCount == txSize) && (rxCount == rxSize))
            {
                ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_IEN &= ~QMSPI_IEN_TRANS_COMPL_EN_Msk;

                ${QMSPI_INSTANCE_NAME?lower_case}Obj.transferIsBusy = false;

                if (${QMSPI_INSTANCE_NAME?lower_case}Obj.callback != NULL)
                {
                    uintptr_t context = ${QMSPI_INSTANCE_NAME?lower_case}Obj.context;

                    ${QMSPI_INSTANCE_NAME?lower_case}Obj.callback(context);
                }
            }
            else
            {
                while ( ((${QMSPI_INSTANCE_NAME}_REGS->QMSPI_STS & QMSPI_STS_TX_BUFF_FULL_Msk) == 0U) && ((txCount != txSize) || (dummySize > 0U)) )
                {
                    if (txCount != txSize)
                    {
                        *((volatile uint8_t*)&${QMSPI_INSTANCE_NAME}_REGS->QMSPI_TX_FIFO[0]) = ${QMSPI_INSTANCE_NAME?lower_case}Obj.pTxBuffer[txCount];
                        txCount++;
                    }
                    else if (dummySize > 0U)
                    {
                        *((volatile uint8_t*)&${QMSPI_INSTANCE_NAME}_REGS->QMSPI_TX_FIFO[0]) = 0xFFU;
                        dummySize--;
                    }
                    else
                    {
                        /* Do nothing */
                    }
                }

                ${QMSPI_INSTANCE_NAME?lower_case}Obj.txCount = txCount;
                ${QMSPI_INSTANCE_NAME?lower_case}Obj.dummySize = dummySize;

                uint32_t transferCount = ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_BUF_CNT_STS & QMSPI_BUF_CNT_STS_TX_BUFF_CNT_Msk;

                ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_CTRL = QMSPI_CTRL_TRANS_UNITS(0x01) | QMSPI_CTRL_TRANS_LEN(transferCount) | QMSPI_CTRL_TX_TRANS_EN(0x01) | QMSPI_CTRL_RX_TRANS_EN_Msk;

                <#if QMSPI_HARDWARE_CS_EN == true>
                if ((txCount == txSize) && (dummySize == 0U))
                {
                    ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_CTRL |= QMSPI_CTRL_CLOSE_TRANS_EN_Msk;
                }
                </#if>

                ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_IEN = QMSPI_IEN_TRANS_COMPL_EN_Msk;
                ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_EXE = QMSPI_EXE_START_Msk;
            }
        }
    }
}
</#if>

<#if QMSPI_INTERRUPT_MODE == false && QMSPI_DMA_EN == false>
<#-- Blocking Mode -->
bool ${QMSPI_INSTANCE_NAME}_SPI_WriteRead (void* pTransmitData, size_t txSize, void* pReceiveData, size_t rxSize)
{
    size_t txCount = 0U;
    size_t rxCount = 0U;
    size_t dummySize = 0U;
    uint32_t transferCount;
    uint8_t receivedData;
    bool isSuccess = false;

    /* Verify the request */
    if(((txSize > 0U) && (pTransmitData != NULL)) || ((rxSize > 0U) && (pReceiveData != NULL)))
    {
        if(pTransmitData == NULL)
        {
            txSize = 0U;
        }

        if(pReceiveData == NULL)
        {
            rxSize = 0U;
        }

        /* Flush out any unread data in SPI DATA Register from the previous transfer */
        ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_EXE = QMSPI_EXE_CLR_DAT_BUFF_Msk;

        if(rxSize > txSize)
        {
            dummySize = rxSize - txSize;
        }

        while((txCount != txSize) || (dummySize > 0U))
        {
            if (txCount != txSize)
            {
                while((txCount != txSize) && ((${QMSPI_INSTANCE_NAME}_REGS->QMSPI_STS & QMSPI_STS_TX_BUFF_FULL_Msk) == 0U))
                {
                    *((uint8_t*)&${QMSPI_INSTANCE_NAME}_REGS->QMSPI_TX_FIFO[0]) = ((uint8_t*)pTransmitData)[txCount];
                    txCount++;
                }
            }
            else if (dummySize > 0U)
            {
                while((dummySize > 0U) && ((${QMSPI_INSTANCE_NAME}_REGS->QMSPI_STS & QMSPI_STS_TX_BUFF_FULL_Msk) == 0U))
                {
                    *((uint8_t*)&${QMSPI_INSTANCE_NAME}_REGS->QMSPI_TX_FIFO[0]) = 0xFFU;
                    dummySize--;
                }
            }
            else
            {
                /* Do nothing */
            }

            transferCount = ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_BUF_CNT_STS & QMSPI_BUF_CNT_STS_TX_BUFF_CNT_Msk;

            ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_CTRL = QMSPI_CTRL_TRANS_UNITS(0x01) | QMSPI_CTRL_TRANS_LEN(transferCount) | QMSPI_CTRL_TX_TRANS_EN(0x01) | QMSPI_CTRL_RX_TRANS_EN_Msk;

            <#if QMSPI_HARDWARE_CS_EN == true>
            if ((txCount == txSize) && (dummySize == 0U))
            {
                ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_CTRL |= QMSPI_CTRL_CLOSE_TRANS_EN_Msk;
            }
            </#if>

            ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_EXE = QMSPI_EXE_START_Msk;

            /* Wait for the entire FIFO to become empty*/
            while ((${QMSPI_INSTANCE_NAME}_REGS->QMSPI_STS & QMSPI_STS_TX_BUFF_EMP_Msk) == 0U)
            {

            }

            /* Read all the data from the RX FIFO*/
            while (((${QMSPI_INSTANCE_NAME}_REGS->QMSPI_BUF_CNT_STS & QMSPI_BUF_CNT_STS_RX_BUFF_CNT_Msk) >> QMSPI_BUF_CNT_STS_RX_BUFF_CNT_Pos) != transferCount)
            {

            }

            while ((${QMSPI_INSTANCE_NAME}_REGS->QMSPI_STS & QMSPI_STS_RX_BUFF_EMP_Msk) == 0U)
            {
                receivedData = *((uint8_t*)&${QMSPI_INSTANCE_NAME}_REGS->QMSPI_RX_FIFO[0]);
                if(rxCount < rxSize)
                {
                    ((uint8_t*)pReceiveData)[rxCount++] = (uint8_t)receivedData;
                }
            }
        }
        isSuccess = true;
    }

    return isSuccess;
}
</#if>




/*******************************************************************************
 End of File
*/
