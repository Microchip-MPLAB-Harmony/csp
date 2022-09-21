/*******************************************************************************
  ${QMSPI_INSTANCE_NAME} Peripheral Library Source File

  Company
    Microchip Technology Inc.

  File Name
    plib_${QMSPI_INSTANCE_NAME?lower_case}.c

  Summary
    ${QMSPI_INSTANCE_NAME} peripheral library interface.

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
#include "plib_${QMSPI_INSTANCE_NAME?lower_case}.h"
<#if QMSPI_INTERRUPT_MODE == true>
#include "../ecia/plib_ecia.h"
</#if>

<#assign QMSPI_IFCTRL_VAL = "">
<#assign QMSPI_CPOL_CHPA = "">
<#if QMSPI_HOLD_OUT_ENABLE == true>
  <#assign QMSPI_IFCTRL_VAL = "QMSPI_IFCTRL_HLD_OUT_EN_Msk">
  <#if QMSPI_HOLD_OUT_VALUE == "HIGH">
    <#assign QMSPI_IFCTRL_VAL = QMSPI_IFCTRL_VAL + " | QMSPI_IFCTRL_HLD_OUT_VAL_Msk">
  </#if>
</#if>
<#if QMSPI_WRITE_PROTECT_OUT_ENABLE == true>
  <#if QMSPI_IFCTRL_VAL != "">
    <#assign QMSPI_IFCTRL_VAL = QMSPI_IFCTRL_VAL + " | QMSPI_IFCTRL_WR_PRCT_OUT_EN_Msk">
  <#else>
    <#assign QMSPI_IFCTRL_VAL = "QMSPI_IFCTRL_WR_PRCT_OUT_EN_Msk">
  </#if>
  <#if QMSPI_WRITE_PROTECT_OUT_VALUE == "HIGH">
    <#assign QMSPI_IFCTRL_VAL = QMSPI_IFCTRL_VAL + " | QMSPI_IFCTRL_WR_PRCT_OUT_VAL_Msk">
  </#if>
</#if>
<#if QMSPI_CPOL == "LOW">
  <#if QMSPI_CPHA_MOSI == "RISING">
    <#assign QMSPI_CPOL_CHPA = "QMSPI_MODE_CHPA_MOSI_Msk">
  </#if>
  <#if QMSPI_CPHA_MISO == "FALLING">
    <#if QMSPI_CPOL_CHPA != "">
      <#assign QMSPI_CPOL_CHPA = QMSPI_CPOL_CHPA + " | QMSPI_MODE_CHPA_MISO_Msk">
    <#else>
      <#assign QMSPI_CPOL_CHPA = "QMSPI_MODE_CHPA_MISO_Msk">
    </#if>
  </#if>
<#else>
  <#assign QMSPI_CPOL_CHPA = "QMSPI_MODE_CPOL_Msk">
  <#if QMSPI_CPHA_MOSI == "FALLING">
    <#assign QMSPI_CPOL_CHPA = QMSPI_CPOL_CHPA + " | QMSPI_MODE_CHPA_MOSI_Msk">
  </#if>
  <#if QMSPI_CPHA_MISO == "RISING">
    <#assign QMSPI_CPOL_CHPA = QMSPI_CPOL_CHPA + " | QMSPI_MODE_CHPA_MISO_Msk">
  </#if>
</#if>

#define QMSPI_SOURCE_CLOCK_FREQUENCY (${QMSPI_SRC_CLK_FREQ}U)
#define QMSPI_MAX_DESCR              (${QMSPI_NUM_OF_DESC}U)
#define SWAP32(x)                    ((((x) & 0xffU) << 24U) | (((x) & 0xff00U) << 8U) | (((x) & 0xff0000U) >> 8U) | (((x) & 0xff000000U) >> 24U))
<#if QMSPI_INTERRUPT_MODE == true>
static QMSPI_OBJECT ${QMSPI_INSTANCE_NAME?lower_case}Obj;
</#if>
static const uint8_t qmspiIoMode[7U][3U] = {{0U, 0U ,0U}, /* IO mode for Command, Address, Data */
                                            {0U, 0U, 1U},
                                            {0U, 0U, 2U},
                                            {0U, 1U, 1U},
                                            {0U, 2U, 2U},
                                            {1U, 1U, 1U},
                                            {2U, 2U, 2U}};

// *****************************************************************************
// *****************************************************************************
// ${QMSPI_INSTANCE_NAME} Local Functions
// *****************************************************************************
// *****************************************************************************

static uint8_t ${QMSPI_INSTANCE_NAME}_DMALenGet(uint32_t address, uint32_t size)
{
    if (((address | size) & 0x03U) == 0U)
    {
        return 2U;
    }
    else if (((address | size) & 0x01U) == 0U)
    {
        return 1U;
    }
    else
    {
        return 0U;
    }
}

static uint8_t ${QMSPI_INSTANCE_NAME}_XferUnitLenGet(uint32_t size)
{
    if ((size & 0x0FU) == 0U)
    {
        return 3U;
    }
    else if ((size & 0x03U) == 0U)
    {
        return 2U;
    } else
    {
        return 1U;
    }
}

static uint8_t ${QMSPI_INSTANCE_NAME}_XferUnitShiftGet(uint32_t size)
{
    if ((size & 0x0FU) == 0U)
    {
        return 4U;
    }
    else if ((size & 0x03U) == 0U)
    {
        return 2U;
    }
    else
    {
        return 0U;
    }
}

// *****************************************************************************
// *****************************************************************************
// ${QMSPI_INSTANCE_NAME} PLIB Interface Routines
// *****************************************************************************
// *****************************************************************************

void ${QMSPI_INSTANCE_NAME}_Initialize(void)
{
    // Reset the QMSPI Block
    ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_MODE = QMSPI_MODE_SOFT_RESET_Msk;

    ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_MODE = QMSPI_MODE_CLK_DIV(${QMSPI_CLOCK_DIVIDE}U)<#if QMSPI_CPOL_CHPA?has_content> | ${QMSPI_CPOL_CHPA}</#if>;

    <#if QMSPI_IFCTRL_VAL?has_content>
    ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_IFCTRL |= ${QMSPI_IFCTRL_VAL};

    </#if>
    // Activate the QMSPI Block
    ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_MODE |= QMSPI_MODE_ACT_Msk;
}

void ${QMSPI_INSTANCE_NAME}_ChipSelectSetup(QMSPI_CHIP_SELECT chipSelect)
{
    ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_MODE = (${QMSPI_INSTANCE_NAME}_REGS->QMSPI_MODE & ~QMSPI_MODE_CS_Msk) | QMSPI_MODE_CS(chipSelect);
}

bool ${QMSPI_INSTANCE_NAME}_TransferSetup (QMSPI_TRANSFER_SETUP *setup)
{
    uint32_t clock_divide;
    bool setupStatus = false;

    if (setup != NULL)
    {
        clock_divide = QMSPI_SOURCE_CLOCK_FREQUENCY / setup->clockFrequency;

        if (clock_divide >= 256U)
        {
            clock_divide = 0;
        }

        ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_MODE = ((${QMSPI_INSTANCE_NAME}_REGS->QMSPI_MODE & ~QMSPI_MODE_CLK_DIV_Msk) | QMSPI_MODE_CLK_DIV(clock_divide))
                                                 | ((${QMSPI_INSTANCE_NAME}_REGS->QMSPI_MODE & ~QMSPI_MODE_CPOL_Msk) | (uint32_t)setup->clockPolarity)
                                                 | ((${QMSPI_INSTANCE_NAME}_REGS->QMSPI_MODE & ~QMSPI_MODE_CHPA_MOSI_Msk) | (uint32_t)setup->clockPhaseMOSI)
                                                 | ((${QMSPI_INSTANCE_NAME}_REGS->QMSPI_MODE & ~QMSPI_MODE_CHPA_MISO_Msk) | (uint32_t)setup->clockPhaseMISO);
        setupStatus = true;
    }
    return setupStatus;
}

/* Manual mode - command, register and memory write */
bool ${QMSPI_INSTANCE_NAME}_Write(QMSPI_XFER_T *qmspiXfer, void* pTransmitData, size_t txSize)
{
    size_t xferLength = 0U;
    size_t count = 0U;
    bool   status = false;

    if (qmspiXfer != NULL)
    {
        if ((${QMSPI_INSTANCE_NAME}_REGS->QMSPI_STS & QMSPI_STS_TRANS_ACTIV_Msk) == 0U)
        {
            ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_EXE = QMSPI_EXE_CLR_DAT_BUFF_Msk;
            ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_STS = QMSPI_STS_Msk;

            *(volatile uint8_t *)(&${QMSPI_INSTANCE_NAME}_REGS->QMSPI_TX_FIFO[0]) = qmspiXfer->command;
            ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_CTRL = QMSPI_CTRL_TX_MODE(qmspiIoMode[qmspiXfer->qmspi_ifc_mode][0]) | QMSPI_CTRL_TX_TRANS_EN(1U) | QMSPI_CTRL_TRANS_UNITS(1U) | QMSPI_CTRL_TRANS_LEN(1U);
            ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_EXE = QMSPI_EXE_START_Msk;
            while ((${QMSPI_INSTANCE_NAME}_REGS->QMSPI_STS & QMSPI_STS_TX_BUFF_EMP_Msk) == 0U)
            {
                // wait if transmit buffer is not empty
            }

            if (qmspiXfer->address_enable)
            {
                /* Check if 32-bit address enable */
                if (qmspiXfer->address_32_bit_en)
                {
                    ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_TX_FIFO[0] = SWAP32(qmspiXfer->address);
                    xferLength = 4U;
                } else
                {
                    uint32_t shift = 24U;
                    xferLength = 3U;
                    count = 0;
                    while(count < xferLength)
                    {
                        shift -= 8U;
                        *(volatile uint8_t *)(&${QMSPI_INSTANCE_NAME}_REGS->QMSPI_TX_FIFO[0]) = (uint8_t)((qmspiXfer->address >> shift) & 0xFFU);
                        count++;
                    }
                }

                ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_CTRL = QMSPI_CTRL_TX_MODE(qmspiIoMode[qmspiXfer->qmspi_ifc_mode][1]) | QMSPI_CTRL_TX_TRANS_EN(1U) | QMSPI_CTRL_TRANS_UNITS(1U) | QMSPI_CTRL_TRANS_LEN(xferLength);
                ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_EXE = QMSPI_EXE_START_Msk;
                while ((${QMSPI_INSTANCE_NAME}_REGS->QMSPI_STS & QMSPI_STS_TX_BUFF_EMP_Msk) == 0U)
                {
                    // wait if transmit buffer is not empty
                }
            }

            while (txSize > 0U)
            {
                if (txSize >= (QMSPI_CTRL_TRANS_LEN_Msk >> QMSPI_CTRL_TRANS_LEN_Pos))
                {
                    xferLength = (QMSPI_CTRL_TRANS_LEN_Msk >> QMSPI_CTRL_TRANS_LEN_Pos);
                }
                else
                {
                    xferLength = txSize;
                }
                ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_CTRL = QMSPI_CTRL_TX_MODE(qmspiIoMode[qmspiXfer->qmspi_ifc_mode][2]) | QMSPI_CTRL_TX_TRANS_EN(1U) | QMSPI_CTRL_TRANS_UNITS(1U) | QMSPI_CTRL_TRANS_LEN(xferLength);
                ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_EXE = QMSPI_EXE_START_Msk;

                count = 0U;
                while (count < xferLength)
                {
                    while ((${QMSPI_INSTANCE_NAME}_REGS->QMSPI_STS & QMSPI_STS_TX_BUFF_FULL_Msk) != 0U)
                    {
                        // wait if transmit buffer is full
                    }
                    *(volatile uint8_t *)(&${QMSPI_INSTANCE_NAME}_REGS->QMSPI_TX_FIFO[0]) = ((uint8_t *)pTransmitData)[count];
                    count++;
                }
                while ((${QMSPI_INSTANCE_NAME}_REGS->QMSPI_STS & QMSPI_STS_TX_BUFF_EMP_Msk) == 0U)
                {
                    // wait if transmit buffer is not empty
                }
                txSize -= xferLength;
            }

            ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_CTRL |= QMSPI_CTRL_CLOSE_TRANS_EN_Msk;
            ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_EXE = QMSPI_EXE_STOP_Msk;
            status = true;
        }
    }
    return status;
}

/* Manual mode - register and memory read */
bool ${QMSPI_INSTANCE_NAME}_Read(QMSPI_XFER_T *qmspiXfer, void* pReceiveData, size_t rxSize)
{
    size_t xferLength = 0U;
    size_t count = 0U;
    bool   status = false;

    if ((qmspiXfer != NULL) && (rxSize > 0U) && (pReceiveData != NULL))
    {
        if ((${QMSPI_INSTANCE_NAME}_REGS->QMSPI_STS & QMSPI_STS_TRANS_ACTIV_Msk) == 0U)
        {
            ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_EXE = QMSPI_EXE_CLR_DAT_BUFF_Msk;
            ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_STS = QMSPI_STS_Msk;

            *(volatile uint8_t *)(&${QMSPI_INSTANCE_NAME}_REGS->QMSPI_TX_FIFO[0]) = qmspiXfer->command;
            ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_CTRL = QMSPI_CTRL_TX_MODE(qmspiIoMode[qmspiXfer->qmspi_ifc_mode][0]) | QMSPI_CTRL_TX_TRANS_EN(1U) | QMSPI_CTRL_TRANS_UNITS(1U) | QMSPI_CTRL_TRANS_LEN(1U);
            ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_EXE = QMSPI_EXE_START_Msk;
            while ((${QMSPI_INSTANCE_NAME}_REGS->QMSPI_STS & QMSPI_STS_TX_BUFF_EMP_Msk) == 0U)
            {
                // wait if transmit buffer is not empty
            }

            if (qmspiXfer->address_enable)
            {
                /* Check if 32-bit address enable */
                if (qmspiXfer->address_32_bit_en)
                {
                    ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_TX_FIFO[0] = SWAP32(qmspiXfer->address);
                    xferLength = 4U;
                } else
                {
                    uint32_t shift = 24U;
                    xferLength = 3U;
                    count = 0;
                    while(count < xferLength)
                    {
                        shift -= 8U;
                        *(volatile uint8_t *)(&${QMSPI_INSTANCE_NAME}_REGS->QMSPI_TX_FIFO[0]) = (uint8_t)((qmspiXfer->address >> shift) & 0xFFU);
                        count++;
                    }
                }

                ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_CTRL = QMSPI_CTRL_TX_MODE(qmspiIoMode[qmspiXfer->qmspi_ifc_mode][1]) | QMSPI_CTRL_TX_TRANS_EN(1U) | QMSPI_CTRL_TRANS_UNITS(1U) | QMSPI_CTRL_TRANS_LEN(xferLength);
                ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_EXE = QMSPI_EXE_START_Msk;
                while ((${QMSPI_INSTANCE_NAME}_REGS->QMSPI_STS & QMSPI_STS_TX_BUFF_EMP_Msk) == 0U)
                {
                    // wait if transmit buffer is not empty
                }
            }

            if (qmspiXfer->num_of_dummy_byte > 0U)
            {
                ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_CTRL = QMSPI_CTRL_TX_MODE(qmspiIoMode[qmspiXfer->qmspi_ifc_mode][2]) | QMSPI_CTRL_TRANS_UNITS(1U) | QMSPI_CTRL_TRANS_LEN(qmspiXfer->num_of_dummy_byte);
                ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_EXE = QMSPI_EXE_START_Msk;
                while ((${QMSPI_INSTANCE_NAME}_REGS->QMSPI_STS & QMSPI_STS_TRANS_COMPL_Msk) == 0U)
                {
                    // wait for transmit complete
                }
            }

            while (rxSize > 0U)
            {
                if (rxSize >= (QMSPI_CTRL_TRANS_LEN_Msk >> QMSPI_CTRL_TRANS_LEN_Pos))
                {
                    xferLength = (QMSPI_CTRL_TRANS_LEN_Msk >> QMSPI_CTRL_TRANS_LEN_Pos);
                }
                else
                {
                    xferLength = rxSize;
                }
                ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_CTRL = QMSPI_CTRL_TX_MODE(qmspiIoMode[qmspiXfer->qmspi_ifc_mode][2]) | QMSPI_CTRL_RX_TRANS_EN(1U) | QMSPI_CTRL_TRANS_UNITS(1U) | QMSPI_CTRL_TRANS_LEN(xferLength);
                ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_EXE = QMSPI_EXE_START_Msk;

                count = 0U;
                while (count < xferLength)
                {
                    while ((${QMSPI_INSTANCE_NAME}_REGS->QMSPI_STS & QMSPI_STS_RX_BUFF_EMP_Msk) != 0U)
                    {
                        // wait if receive buffer is empty
                    }
                    ((uint8_t *)pReceiveData)[count] = *(volatile uint8_t *)(&${QMSPI_INSTANCE_NAME}_REGS->QMSPI_RX_FIFO[0]);
                    count++;
                }
                rxSize -= xferLength;
            }

            ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_CTRL |= QMSPI_CTRL_CLOSE_TRANS_EN_Msk;
            ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_EXE = QMSPI_EXE_STOP_Msk;
            status = true;
        }
    }
    return status;
}

bool ${QMSPI_INSTANCE_NAME}_IsTransmitterBusy(void)
{
    return ((${QMSPI_INSTANCE_NAME}_REGS->QMSPI_STS & QMSPI_STS_TX_BUFF_EMP_Msk) == 0U);
}

/* Memory write with Local/Central DMA */
uint32_t ${QMSPI_INSTANCE_NAME}_DMATransferWrite(QMSPI_DESCRIPTOR_XFER_T *qmspiDescXfer, void* pTransmitData, size_t txSize)
{
    uint32_t desc_id, size, xferLength;
    uint32_t txBytes = 0U;
    uint8_t len, xferUnitLen, xferUnitShift;

    if ((qmspiDescXfer != NULL) && (txSize > 0U))
    {

        if ((${QMSPI_INSTANCE_NAME}_REGS->QMSPI_STS & QMSPI_STS_TRANS_ACTIV_Msk) == 0U)
        {
            ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_CTRL = QMSPI_CTRL_DESCR_BUFF_EN_Msk;
            ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_EXE = QMSPI_EXE_CLR_DAT_BUFF_Msk;
            ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_STS = QMSPI_STS_Msk;

            *(volatile uint8_t *)(&${QMSPI_INSTANCE_NAME}_REGS->QMSPI_TX_FIFO[0]) = qmspiDescXfer->command;
            desc_id = 0;
            /* Descriptor 0 - Command */
            ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_DESCR[desc_id] = QMSPI_DESCR_INFACE_MOD(qmspiIoMode[qmspiDescXfer->qmspi_ifc_mode][0])
                                                              | QMSPI_DESCR_TX_TRANS_EN(1U)
                                                              | QMSPI_DESCR_TRANS_LEN(1U)
                                                              | QMSPI_DESCR_DESCR_BUF_NXT_PTR((desc_id + 1U))
                                                              | QMSPI_DESCR_TX_LEN(1U);
            desc_id++;

            /* Check if 32-bit address enable */
            if (qmspiDescXfer->address_32_bit_en)
            {
                ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_TX_FIFO[0] = SWAP32(qmspiDescXfer->address);
                xferLength = 4U;
            } else
            {
                uint32_t shift = 24U;
                xferLength = 3U;
                txBytes = 0;
                while(txBytes < xferLength)
                {
                    shift -= 8U;
                    *(volatile uint8_t *)(&${QMSPI_INSTANCE_NAME}_REGS->QMSPI_TX_FIFO[0]) = (uint8_t)((qmspiDescXfer->address >> shift) & 0xFFU);
                    txBytes++;
                }
            }

            /* Descriptor 1 - Address */
            ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_DESCR[desc_id] = QMSPI_DESCR_INFACE_MOD(qmspiIoMode[qmspiDescXfer->qmspi_ifc_mode][1])
                                                              | QMSPI_DESCR_TX_TRANS_EN(1U)
                                                              | QMSPI_DESCR_TRANS_LEN(1U)
                                                              | QMSPI_DESCR_DESCR_BUF_NXT_PTR((desc_id + 1U))
                                                              | QMSPI_DESCR_TX_LEN(xferLength);
            desc_id++;

            len = ${QMSPI_INSTANCE_NAME}_DMALenGet((uint32_t)((uint32_t*)pTransmitData), txSize);

            if (qmspiDescXfer->ldma_enable)
            {
                ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_MODE |= QMSPI_MODE_LDMA_TXEN_Msk;

                ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_DESCR[desc_id] = QMSPI_DESCR_INFACE_MOD(qmspiIoMode[qmspiDescXfer->qmspi_ifc_mode][2])
                                                              | QMSPI_DESCR_TX_DMA_EN((qmspiDescXfer->ldma_channel_num + 1U))
                                                              | QMSPI_DESCR_TX_TRANS_EN(1U)
                                                              | QMSPI_DESCR_DESCR_BUF_NXT_PTR((desc_id + 1U))
                                                              | QMSPI_DESCR_DESCR_BUF_LAST_Msk
                                                              | QMSPI_DESCR_CLOSE_TRANS_EN_Msk;

                ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_DESC_LDMA_TXEN = QMSPI_DESC_LDMA_TXEN_DESC_LDMA_TXEN_Msk;

                ${QMSPI_INSTANCE_NAME}_REGS->LDMA_TX[qmspiDescXfer->ldma_channel_num].QMSPI_LDMA_TXCTRL = QMSPI_LDMA_TXCTRL_CH_EN_Msk
                                                              | QMSPI_LDMA_TXCTRL_OVRD_LEN_Msk
                                                              | QMSPI_LDMA_TXCTRL_ACS_SZ(len);
                if (qmspiDescXfer->ldma_incr_addr_disable == false)
                {
                    ${QMSPI_INSTANCE_NAME}_REGS->LDMA_TX[qmspiDescXfer->ldma_channel_num].QMSPI_LDMA_TXCTRL |= QMSPI_LDMA_TXCTRL_INC_ADDR_EN_Msk;
                }
                ${QMSPI_INSTANCE_NAME}_REGS->LDMA_TX[qmspiDescXfer->ldma_channel_num].QMSPI_LDMA_TXSTRT_ADDR = (uint32_t)((uint32_t*)pTransmitData);
                ${QMSPI_INSTANCE_NAME}_REGS->LDMA_TX[qmspiDescXfer->ldma_channel_num].QMSPI_LDMA_TX_LEN = txSize;
                txBytes = txSize;
            }
            else
            {
                ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_MODE &= ~QMSPI_MODE_LDMA_TXEN_Msk;
                xferUnitLen = ${QMSPI_INSTANCE_NAME}_XferUnitLenGet(txSize);
                xferUnitShift = ${QMSPI_INSTANCE_NAME}_XferUnitShiftGet(txSize);
                size = txSize >> xferUnitShift;
                while (size > 0U)
                {
                    xferLength = size;
                    if (size > (QMSPI_DESCR_TX_LEN_Msk >> QMSPI_DESCR_TX_LEN_Pos))
                    {
                        xferLength = (QMSPI_DESCR_TX_LEN_Msk >> QMSPI_DESCR_TX_LEN_Pos);
                    }

                    ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_DESCR[desc_id] = QMSPI_DESCR_INFACE_MOD(qmspiIoMode[qmspiDescXfer->qmspi_ifc_mode][2]) | QMSPI_DESCR_TX_TRANS_EN(1U)
                                                                | QMSPI_DESCR_TRANS_LEN(xferUnitLen) | QMSPI_DESCR_TX_DMA_EN(((uint32_t)len + 1U))
                                                                | QMSPI_DESCR_TX_LEN(xferLength) | QMSPI_DESCR_DESCR_BUF_NXT_PTR((desc_id + 1U));
                    size -= xferLength;

                    desc_id++;
                    if (desc_id >= QMSPI_MAX_DESCR)
                    {
                        break;
                    }
                }
                if (desc_id != 0U)
                {
                    desc_id--;
                }
                ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_DESCR[desc_id] |= QMSPI_DESCR_DESCR_BUF_LAST_Msk | QMSPI_DESCR_CLOSE_TRANS_EN_Msk;
                txBytes = (txSize - (size << xferUnitShift));
            }
            <#if QMSPI_INTERRUPT_MODE == true>
            ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_IEN |= QMSPI_IEN_TRANS_COMPL_EN_Msk;
            </#if>
            ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_EXE = QMSPI_EXE_START_Msk;
            <#if QMSPI_INTERRUPT_MODE == false>
            while ((${QMSPI_INSTANCE_NAME}_REGS->QMSPI_STS & QMSPI_STS_TRANS_COMPL_Msk) == 0U)
            {
                // wait for transfer complete
            }
            </#if>
        }
    }
    return txBytes;
}

/* Memory read with Local/Central DMA */
uint32_t ${QMSPI_INSTANCE_NAME}_DMATransferRead(QMSPI_DESCRIPTOR_XFER_T *qmspiDescXfer, void* pReceiveData, size_t rxSize)
{
    uint32_t desc_id, count, xferLength;
    uint32_t size = 0U;
    uint8_t len, xferUnitLen, xferUnitShift;

    if ((qmspiDescXfer != NULL) && (rxSize > 0U) && (pReceiveData != NULL))
    {
        ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_CTRL = QMSPI_CTRL_DESCR_BUFF_EN_Msk;
        ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_EXE = QMSPI_EXE_CLR_DAT_BUFF_Msk;
        ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_STS = QMSPI_STS_Msk;

        *(volatile uint8_t *)(&${QMSPI_INSTANCE_NAME}_REGS->QMSPI_TX_FIFO[0]) = qmspiDescXfer->command;
        desc_id = 0;
        /* Descriptor 0 - Command */
        ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_DESCR[desc_id] = QMSPI_DESCR_INFACE_MOD(qmspiIoMode[qmspiDescXfer->qmspi_ifc_mode][0])
                                                          | QMSPI_DESCR_TX_TRANS_EN(1U)
                                                          | QMSPI_DESCR_TRANS_LEN(1U)
                                                          | QMSPI_DESCR_DESCR_BUF_NXT_PTR((desc_id + 1U))
                                                          | QMSPI_DESCR_TX_LEN(1U);
        desc_id++;

        /* Check if 32-bit address enable */
        if (qmspiDescXfer->address_32_bit_en)
        {
            ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_TX_FIFO[0] = SWAP32(qmspiDescXfer->address);
            xferLength = 4U;
        } else
        {
            uint32_t shift = 24U;
            xferLength = 3U;
            count = 0;
            while(count < xferLength)
            {
                shift -= 8U;
                *(volatile uint8_t *)(&${QMSPI_INSTANCE_NAME}_REGS->QMSPI_TX_FIFO[0]) = (uint8_t)((qmspiDescXfer->address >> shift) & 0xFFU);
                count++;
            }
        }

        /* Descriptor 1 - Address */
        ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_DESCR[desc_id] = QMSPI_DESCR_INFACE_MOD(qmspiIoMode[qmspiDescXfer->qmspi_ifc_mode][1])
                                                          | QMSPI_DESCR_TX_TRANS_EN(1U)
                                                          | QMSPI_DESCR_TRANS_LEN(1U)
                                                          | QMSPI_DESCR_DESCR_BUF_NXT_PTR((desc_id + 1U))
                                                          | QMSPI_DESCR_TX_LEN(xferLength);
        desc_id++;

        /* Dummy Bytes */
        if (qmspiDescXfer->num_of_dummy_byte > 0U)
        {
            ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_DESCR[desc_id] = QMSPI_DESCR_INFACE_MOD(qmspiIoMode[qmspiDescXfer->qmspi_ifc_mode][2])
                                                          | QMSPI_DESCR_TRANS_LEN(1U)
                                                          | QMSPI_DESCR_DESCR_BUF_NXT_PTR((desc_id + 1U))
                                                          | QMSPI_DESCR_TX_LEN(qmspiDescXfer->num_of_dummy_byte);
            desc_id++;
        }

        len = ${QMSPI_INSTANCE_NAME}_DMALenGet((uint32_t)((uint32_t*)pReceiveData), rxSize);

        if (qmspiDescXfer->ldma_enable)
        {
            ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_MODE |= QMSPI_MODE_LDMA_RXEN_Msk;

            ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_DESCR[desc_id] = QMSPI_DESCR_INFACE_MOD(qmspiIoMode[qmspiDescXfer->qmspi_ifc_mode][2])
                                                          | QMSPI_DESCR_RX_DMA_EN((qmspiDescXfer->ldma_channel_num + 1U))
                                                          | QMSPI_DESCR_RX_TRANS_EN_Msk
                                                          | QMSPI_DESCR_DESCR_BUF_NXT_PTR((desc_id + 1U))
                                                          | QMSPI_DESCR_DESCR_BUF_LAST_Msk
                                                          | QMSPI_DESCR_CLOSE_TRANS_EN_Msk;

            ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_DESC_LDMA_RXEN = QMSPI_DESC_LDMA_RXEN_DESC_LDMA_RXEN_Msk;

            ${QMSPI_INSTANCE_NAME}_REGS->LDMA_RX[qmspiDescXfer->ldma_channel_num].QMSPI_LDMA_RXCTRL = QMSPI_LDMA_RXCTRL_CH_EN_Msk
                                                          | QMSPI_LDMA_RXCTRL_OVRD_LEN_Msk
                                                          | QMSPI_LDMA_RXCTRL_ACS_SZ(len);
            if (qmspiDescXfer->ldma_incr_addr_disable == false)
            {
                ${QMSPI_INSTANCE_NAME}_REGS->LDMA_RX[qmspiDescXfer->ldma_channel_num].QMSPI_LDMA_RXCTRL |= QMSPI_LDMA_RXCTRL_INC_ADDR_EN_Msk;
            }
            ${QMSPI_INSTANCE_NAME}_REGS->LDMA_RX[qmspiDescXfer->ldma_channel_num].QMSPI_LDMA_RXSTRT_ADDR = (uint32_t)((uint32_t*)pReceiveData);
            ${QMSPI_INSTANCE_NAME}_REGS->LDMA_RX[qmspiDescXfer->ldma_channel_num].QMSPI_LDMA_RX_LEN = rxSize;
            size = rxSize;
        }
        else
        {
            ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_MODE &= ~QMSPI_MODE_LDMA_RXEN_Msk;
            xferUnitLen = ${QMSPI_INSTANCE_NAME}_XferUnitLenGet(rxSize);
            xferUnitShift = ${QMSPI_INSTANCE_NAME}_XferUnitShiftGet(rxSize);
            size = rxSize >> xferUnitShift;

            count = 0U;
            while (count < size)
            {
                xferLength = size - count;
                if (xferLength > (QMSPI_DESCR_TX_LEN_Msk >> QMSPI_DESCR_TX_LEN_Pos))
                {
                    xferLength = (QMSPI_DESCR_TX_LEN_Msk >> QMSPI_DESCR_TX_LEN_Pos);
                }
                count += xferLength;

                ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_DESCR[desc_id] = QMSPI_DESCR_INFACE_MOD(qmspiIoMode[qmspiDescXfer->qmspi_ifc_mode][2]) | QMSPI_DESCR_RX_TRANS_EN_Msk
                                                                | QMSPI_DESCR_TRANS_LEN(xferUnitLen) | QMSPI_DESCR_RX_DMA_EN(((uint32_t)len + 1U))
                                                                | QMSPI_DESCR_TX_LEN(xferLength) | QMSPI_DESCR_DESCR_BUF_NXT_PTR((desc_id + 1U));

                desc_id++;
                if (desc_id >= QMSPI_MAX_DESCR)
                {
                    break;
                }
            }

            if (desc_id != 0U)
            {
                desc_id--;
            }
            ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_DESCR[desc_id] |= QMSPI_DESCR_DESCR_BUF_LAST_Msk | QMSPI_DESCR_CLOSE_TRANS_EN_Msk;

            size = (count << xferUnitShift);
        }
        <#if QMSPI_INTERRUPT_MODE == true>
        ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_IEN |= QMSPI_IEN_TRANS_COMPL_EN_Msk;
        </#if>
        ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_EXE = QMSPI_EXE_START_Msk;
        <#if QMSPI_INTERRUPT_MODE == false>
        while ((${QMSPI_INSTANCE_NAME}_REGS->QMSPI_STS & QMSPI_STS_TRANS_COMPL_Msk) == 0U)
        {
            // wait for transfer complete
        }
        </#if>
    }
    return size;
}

<#if QMSPI_INTERRUPT_MODE == true>
void ${QMSPI_INSTANCE_NAME}_CallbackRegister(QMSPI_CALLBACK callback, uintptr_t context)
{
    ${QMSPI_INSTANCE_NAME?lower_case}Obj.callback = callback;
    ${QMSPI_INSTANCE_NAME?lower_case}Obj.context = context;
}

void ${QMSPI_NVIC_INTERRUPT_NAME}_InterruptHandler(void)
{
    <#if QMSPI_INTERRUPT_TYPE == "AGGREGATE">
    ECIA_GIRQSourceClear(ECIA_AGG_INT_SRC_QMSPI${QMSPI_INSTANCE_NUM});
    <#else>
    ECIA_GIRQSourceClear(ECIA_DIR_INT_SRC_QMSPI${QMSPI_INSTANCE_NUM});
    </#if>

    if ((${QMSPI_INSTANCE_NAME}_REGS->QMSPI_STS & QMSPI_STS_TRANS_COMPL_Msk) != 0U)
    {
        ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_STS |= QMSPI_STS_TRANS_COMPL_Msk;
        ${QMSPI_INSTANCE_NAME}_REGS->QMSPI_IEN &= ~QMSPI_IEN_TRANS_COMPL_EN_Msk;
        if(${QMSPI_INSTANCE_NAME?lower_case}Obj.callback != NULL)
        {
            ${QMSPI_INSTANCE_NAME?lower_case}Obj.callback(${QMSPI_INSTANCE_NAME?lower_case}Obj.context);
        }
    }
}
</#if>

/*******************************************************************************
 End of File
*/
