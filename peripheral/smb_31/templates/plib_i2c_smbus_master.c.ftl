/*******************************************************************************
  Inter-Integrated Circuit (I2C) Library
  Source File

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${I2C_INSTANCE_NAME?lower_case}_master.c

  Summary:
    I2C PLIB Master Mode Implementation file

  Description:
    This file defines the interface to the I2C peripheral library.
    This library provides access to and control of the associated peripheral
    instance.

*******************************************************************************/
// DOM-IGNORE-BEGIN
/*******************************************************************************
* Copyright (C) 2018-2019 Microchip Technology Inc. and its subsidiaries.
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

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
#include "device.h"
<#if core.CoreSysIntFile == true>
#include "interrupts.h"
</#if>
#include "plib_${I2C_INSTANCE_NAME?lower_case}_master.h"
<#if I2C_SMBUS_LOW_LEVEL_API_ONLY == false>
#include "../plib_i2c_smb_common.h"
#include "../../ecia/plib_ecia.h"
#include "../../dma/plib_dma.h"

// *****************************************************************************
// *****************************************************************************
// Section: Global Data
// *****************************************************************************
// *****************************************************************************
#define NOP()    asm("NOP")
#define ${I2C_INSTANCE_NAME}_MTXB   (uint32_t*)(SMB${I2C_INSTANCE_NUM}_BASE_ADDRESS + SMB_MTR_TXB_REG_OFST)
#define ${I2C_INSTANCE_NAME}_MRXB   (uint32_t*)(SMB${I2C_INSTANCE_NUM}_BASE_ADDRESS + SMB_MTR_RXB_REG_OFST)

static I2C_SMB_HOST_OBJ ${I2C_INSTANCE_NAME?lower_case}HostObj;
static uint8_t i2c${I2C_INSTANCE_NAME?lower_case}HostWrBuffer[64];
static uint8_t i2c${I2C_INSTANCE_NAME?lower_case}HostRdBuffer[64];
</#if>

<#if I2C_OPERATING_MODE == "Master">
void I2C${I2C_INSTANCE_NAME}_Initialize(void)
{
    /* Reset I2C */
    ${I2C_INSTANCE_NAME}_REGS->SMB_CFG[0] = SMB_CFG_RST_Msk;

    /* Reset bit must remain asserted for at-least 1 Baud clock period */
    NOP();NOP();NOP();NOP();NOP();

    ${I2C_INSTANCE_NAME}_REGS->SMB_CFG[0] &= ~SMB_CFG_RST_Msk;

    /* Set the port associated with this instance of I2C peripheral */
    ${I2C_INSTANCE_NAME}_REGS->SMB_CFG[0] = SMB_CFG_PORT_SEL(${I2C_PORT_SEL});

    <#if I2C_SMBUS_PEC_ENABLE == true>${I2C_INSTANCE_NAME}_REGS->SMB_PEC = 0;</#if>

    /* Repeated start hold time setup */
    ${I2C_INSTANCE_NAME}_REGS->SMB_RSHTM = I2C_SMB_RecommendedValues[2][${BUS_FREQ_VAL_INDEX}];

    /* Data timing register */
    ${I2C_INSTANCE_NAME}_REGS->SMB_DATATM = I2C_SMB_RecommendedValues[1][${BUS_FREQ_VAL_INDEX}];

    <#if I2C_SMBUS_TIMING_CHK_ENABLE == true>
    /* Timeout scaling register setup */
    ${I2C_INSTANCE_NAME}_REGS->SMB_TMOUTSC = I2C_SMB_RecommendedValues[4][${BUS_FREQ_VAL_INDEX}];
    </#if>

    /* Enable I2C peripheral */
    ${I2C_INSTANCE_NAME}_REGS->SMB_CFG[0] |= SMB_CFG_EN_Msk <#if I2C_SMBUS_PEC_ENABLE == true>| SMB_CFG_PECEN_Msk </#if> <#if I2C_SMBUS_TIMING_CHK_ENABLE == true>| SMB_CFG_TCEN_Msk</#if>;

    /* I2C bus clock frequency */
    ${I2C_INSTANCE_NAME}_REGS->SMB_BUSCLK = SMB_BUSCLK_HIGH_PER(${BRG_VALUE}) | SMB_BUSCLK_LOW_PER(${BRG_VALUE});

    /* Enable Serial output and set ACK bit */
    ${I2C_INSTANCE_NAME}_REGS->SMB_WCTRL = (SMB_WCTRL_ESO_Msk | SMB_WCTRL_ACK_Msk);

<#if I2C_SMBUS_LOW_LEVEL_API_ONLY == false>
    ${I2C_INSTANCE_NAME?lower_case}HostObj.callback = NULL;

    ${I2C_INSTANCE_NAME?lower_case}HostObj.state = I2C_SMB_HOST_STATE_IDLE;

    ${I2C_INSTANCE_NAME?lower_case}HostObj.error = I2C_SMB_HOST_ERROR_NONE;
</#if>
}
<#else>
void I2C${I2C_INSTANCE_NAME}_HostInitialize(void)
{
    /* I2C bus clock frequency */
    ${I2C_INSTANCE_NAME}_REGS->SMB_BUSCLK = SMB_BUSCLK_HIGH_PER(${BRG_VALUE}) | SMB_BUSCLK_LOW_PER(${BRG_VALUE});

<#if I2C_SMBUS_LOW_LEVEL_API_ONLY == false>
    ${I2C_INSTANCE_NAME?lower_case}HostObj.callback = NULL;

    ${I2C_INSTANCE_NAME?lower_case}HostObj.state = I2C_SMB_HOST_STATE_IDLE;

    ${I2C_INSTANCE_NAME?lower_case}HostObj.error = I2C_SMB_HOST_ERROR_NONE;
</#if>
}
</#if>

<#if I2C_SMBUS_LOW_LEVEL_API_ONLY == false>

static void I2C${I2C_INSTANCE_NAME}_HostReInitialize(void)
{
    /* Reset I2C */
    ${I2C_INSTANCE_NAME}_REGS->SMB_CFG[0] = SMB_CFG_RST_Msk;

    /* Reset bit must remain asserted for at-least 1 Baud clock period */
    NOP();NOP();NOP();NOP();NOP();

    ${I2C_INSTANCE_NAME}_REGS->SMB_CFG[0] &= ~SMB_CFG_RST_Msk;

    /* Set the port associated with this instance of I2C peripheral */
    ${I2C_INSTANCE_NAME}_REGS->SMB_CFG[0] = SMB_CFG_PORT_SEL(${I2C_PORT_SEL});

    <#if I2C_SMBUS_PEC_ENABLE == true>${I2C_INSTANCE_NAME}_REGS->SMB_PEC = 0;</#if>

    /* Repeated start hold time setup */
    ${I2C_INSTANCE_NAME}_REGS->SMB_RSHTM = I2C_SMB_RecommendedValues[2][${BUS_FREQ_VAL_INDEX}];

    /* Data timing register */
    ${I2C_INSTANCE_NAME}_REGS->SMB_DATATM = I2C_SMB_RecommendedValues[1][${BUS_FREQ_VAL_INDEX}];

    <#if I2C_SMBUS_TIMING_CHK_ENABLE == true>
    /* Timeout scaling register setup */
    ${I2C_INSTANCE_NAME}_REGS->SMB_TMOUTSC = I2C_SMB_RecommendedValues[4][${BUS_FREQ_VAL_INDEX}];
    </#if>

    /* Enable I2C peripheral */
    ${I2C_INSTANCE_NAME}_REGS->SMB_CFG[0] |= SMB_CFG_EN_Msk <#if I2C_SMBUS_PEC_ENABLE == true>| SMB_CFG_PECEN_Msk </#if> <#if I2C_SMBUS_TIMING_CHK_ENABLE == true>| SMB_CFG_TCEN_Msk</#if>;

    /* I2C bus clock frequency */
    ${I2C_INSTANCE_NAME}_REGS->SMB_BUSCLK = SMB_BUSCLK_HIGH_PER(${BRG_VALUE}) | SMB_BUSCLK_LOW_PER(${BRG_VALUE});

    /* Enable Serial output and set ACK bit */
    ${I2C_INSTANCE_NAME}_REGS->SMB_WCTRL = (SMB_WCTRL_ESO_Msk | SMB_WCTRL_ACK_Msk);
}

bool I2C${I2C_INSTANCE_NAME}_HostIsBusy(void)
{
    if((${I2C_INSTANCE_NAME}_REGS->SMB_COMPL[0] & SMB_COMPL_IDLE_Msk) != 0U)
    {
        return false;
    }
    else
    {
        return true;
    }
}

void I2C${I2C_INSTANCE_NAME}_HostCallbackRegister(I2C_SMB_HOST_CALLBACK callback, uintptr_t contextHandle)
{
    if (callback == NULL)
    {
        return;
    }

    ${I2C_INSTANCE_NAME?lower_case}HostObj.callback = callback;
    ${I2C_INSTANCE_NAME?lower_case}HostObj.context = contextHandle;
}

I2C_SMB_HOST_ERROR I2C${I2C_INSTANCE_NAME}_HostErrorGet(void)
{
    I2C_SMB_HOST_ERROR error;

    error = ${I2C_INSTANCE_NAME?lower_case}HostObj.error;
    ${I2C_INSTANCE_NAME?lower_case}HostObj.error = I2C_SMB_HOST_ERROR_NONE;

    return error;
}

bool I2C${I2C_INSTANCE_NAME}_HostTransferSetup(I2C_SMB_HOST_TRANSFER_SETUP* setup, uint32_t srcClkFreq )
{
    uint32_t high_low_period;
    uint32_t i2cBusFreq;
    uint32_t timingValuesIndex = 0;
    float temp;

    if ((setup == NULL) || (${I2C_INSTANCE_NAME?lower_case}HostObj.state != I2C_SMB_HOST_STATE_IDLE))
    {
        return false;
    }

    i2cBusFreq = setup->clkSpeed;

    /* Maximum I2C clock speed cannot be greater than 1 MHz */
    if (i2cBusFreq > 1000000U)
    {
        return false;
    }

    if( srcClkFreq == 0U)
    {
        srcClkFreq = ${I2C_INPUT_CLOCK_FREQ}UL;
    }

    temp = ((((float)srcClkFreq/(float)i2cBusFreq)/2.0f) - 1.0f);

    high_low_period = (uint32_t)temp;

    /* high/low baud period value cannot be greater than 255 */
    if (high_low_period > 255U)
    {
        high_low_period = 255U;
    }

    /* Clear the ESO bit(Serial output) before changing the baud value */
    ${I2C_INSTANCE_NAME}_REGS->SMB_WCTRL &= ~SMB_WCTRL_ESO_Msk;

    ${I2C_INSTANCE_NAME}_REGS->SMB_BUSCLK = SMB_BUSCLK_HIGH_PER(high_low_period) | SMB_BUSCLK_LOW_PER(high_low_period);

    if (i2cBusFreq < 250000U)
    {
        timingValuesIndex = 0;
    }
    else if (i2cBusFreq < 750000U)
    {
        timingValuesIndex = 1U;
    }
    else
    {
        timingValuesIndex  = 2U;
    }

    /* Repeated start hold time setup */
    ${I2C_INSTANCE_NAME}_REGS->SMB_RSHTM = I2C_SMB_RecommendedValues[2][timingValuesIndex];

    /* Data timing register */
    ${I2C_INSTANCE_NAME}_REGS->SMB_DATATM = I2C_SMB_RecommendedValues[1][timingValuesIndex];

    /* Timeout scaling register setup */
    ${I2C_INSTANCE_NAME}_REGS->SMB_TMOUTSC = I2C_SMB_RecommendedValues[4][timingValuesIndex];

    /* Set the ESO bit (Serial output) after changing the baud value */
    ${I2C_INSTANCE_NAME}_REGS->SMB_WCTRL |= SMB_WCTRL_ESO_Msk;

    return true;
}

static uint8_t I2C${I2C_INSTANCE_NAME}_HostPacketForm(I2C_SMB_HOST_PROTOCOL protocol, uint8_t address, uint8_t cmd, void* pWrdata, uint32_t nWrBytes)
{
    uint8_t* pProtoBuff = i2c${I2C_INSTANCE_NAME?lower_case}HostWrBuffer;
    uint8_t len = 0;

    pProtoBuff[len++] = (address << 1) | (uint8_t)I2C_SMB_HOST_TRANSFER_TYPE_WRITE;
    pProtoBuff[len++] = cmd;

    switch(protocol)
    {
        case I2C_SMB_HOST_PROTOCOL_WR_BYTE:
        case I2C_SMB_HOST_PROTOCOL_WR_WORD:
            /* Nothing to do here */
            break;
        case I2C_SMB_HOST_PROTOCOL_WR_BLK:
        case I2C_SMB_HOST_PROTOCOL_WR_BLK_RD_BLK:
            pProtoBuff[len++] = (uint8_t)nWrBytes;
            break;
        case I2C_SMB_HOST_PROTOCOL_RD_BYTE:
        case I2C_SMB_HOST_PROTOCOL_RD_WORD:
        case I2C_SMB_HOST_PROTOCOL_RD_BLK:
            pProtoBuff[len++] = (address << 1) | (uint8_t)I2C_SMB_HOST_TRANSFER_TYPE_READ;
            break;
        default:
            /* Default case, should not enter here. */
            break;
    }

    if (nWrBytes != 0U)
    {
        (void)memcpy((void*)&pProtoBuff[len], (const void*)pWrdata, nWrBytes);
        len += (uint8_t)nWrBytes;
    }
    if (protocol == I2C_SMB_HOST_PROTOCOL_WR_BLK_RD_BLK)
    {
        pProtoBuff[len++] = (address << 1) | I2C_SMB_HOST_TRANSFER_TYPE_READ;
    }

    return len;
}

static void I2C${I2C_INSTANCE_NAME}_HostWriteRead(I2C_SMB_HOST_PROTOCOL protocol, uint8_t nWrBytes, uint32_t nRdBytes)
{
    uint32_t hostCmd = 0;
    uint8_t PECConfig = ((${I2C_INSTANCE_NAME}_REGS->SMB_CFG[0] & SMB_CFG_PECEN_Msk) != 0U)? 1U: 0U;

    ${I2C_INSTANCE_NAME?lower_case}HostObj.dmaDirChange = false;

    ${I2C_INSTANCE_NAME?lower_case}HostObj.error = I2C_SMB_HOST_ERROR_NONE;

    /* Start by flushing off host transmit and receive buffers */
    ${I2C_INSTANCE_NAME}_REGS->SMB_CFG[0] |= SMB_CFG_FLUSH_MRBUF_Msk | SMB_CFG_FLUSH_MXBUF_Msk;

    /* Configure DMA transfer for the write part (memory to peripheral) of the transfer. DMA channel will be reconfigured for reading (Peripheral to memory ) in the I2CSMB interrupt, once the write part is complete. */
    (void)DMA_ChannelTransfer(DMA_CHANNEL_${I2C_SMBUS_MASTER_DMA_CHANNEL}, (void*)i2c${I2C_INSTANCE_NAME?lower_case}HostWrBuffer, ${I2C_INSTANCE_NAME}_MTXB, nWrBytes);

    ${I2C_INSTANCE_NAME?lower_case}HostObj.state = I2C_SMB_HOST_STATE_TRANSMIT;

    hostCmd = (SMB_MCMD_WR_CNT(nWrBytes) | SMB_MCMD_START0_Msk | SMB_MCMD_MPROCEED_Msk | SMB_MCMD_MRUN_Msk | SMB_MCMD_STOP_Msk);

    if ((protocol == I2C_SMB_HOST_PROTOCOL_RD_BYTE) || (protocol == I2C_SMB_HOST_PROTOCOL_RD_WORD) || (protocol == I2C_SMB_HOST_PROTOCOL_RD_BLK) || (protocol == I2C_SMB_HOST_PROTOCOL_WR_BLK_RD_BLK))
    {
        /* Specify the number of bytes to read from target, generate repeated start and read PEC byte when RD_CNT becomes 0 */
        hostCmd |= (SMB_MCMD_RD_CNT(nRdBytes) | SMB_MCMD_STARTN_Msk) | SMB_MCMD_READ_PEC(PECConfig);
        ${I2C_INSTANCE_NAME?lower_case}HostObj.dmaRdBytes = nRdBytes + (PECConfig == 1U? 2U : 0U);
        ${I2C_INSTANCE_NAME?lower_case}HostObj.dmaDirChange = true;
    }
    else
    {
        /* Transmit PEC once the WR_CNT becomes 0 */
        hostCmd |= SMB_MCMD_PEC_TERM(PECConfig);
    }

    if ((protocol == I2C_SMB_HOST_PROTOCOL_RD_BLK) || (protocol == I2C_SMB_HOST_PROTOCOL_WR_BLK_RD_BLK))
    {
        /* Set RD_CNT with max possible read count. It will be over-written (READM) by the first byte received from I2C slave. */
        hostCmd |= SMB_MCMD_READM_Msk;
    }

    ${I2C_INSTANCE_NAME?lower_case}HostObj.protocol = protocol;

    /* Enable MDONE interrupt */
    ${I2C_INSTANCE_NAME}_REGS->SMB_CFG[0] |= SMB_CFG_ENMI_Msk;

    /* If timeout check is enabled, then enable timeout related interrupts */
    if ((${I2C_INSTANCE_NAME}_REGS->SMB_CFG[0] & SMB_CFG_TCEN_Msk) != 0U)
    {
        ${I2C_INSTANCE_NAME}_REGS->SMB_COMPL[0] |= SMB_COMPL_DTEN_Msk | SMB_COMPL_MCEN_Msk | SMB_COMPL_BIDEN_Msk;
    }
    else
    {
        ${I2C_INSTANCE_NAME}_REGS->SMB_COMPL[0] &= ~(SMB_COMPL_DTEN_Msk | SMB_COMPL_MCEN_Msk | SMB_COMPL_BIDEN_Msk);
    }

    /* Set the host command and start the transfer */
    ${I2C_INSTANCE_NAME}_REGS->SMB_MCMD[0] = hostCmd;
}

void I2C${I2C_INSTANCE_NAME}_HostWriteByte(uint8_t address, uint8_t cmd, void* pWrdata)
{
    /* <slave_add> <cmd> <data0> */
    uint8_t wrLen = I2C${I2C_INSTANCE_NAME}_HostPacketForm(I2C_SMB_HOST_PROTOCOL_WR_BYTE, address, cmd, pWrdata, 1);
    I2C${I2C_INSTANCE_NAME}_HostWriteRead(I2C_SMB_HOST_PROTOCOL_WR_BYTE, wrLen, 0);
}

void I2C${I2C_INSTANCE_NAME}_HostWriteWord(uint8_t address, uint8_t cmd, void* pWrdata)
{
    /* <slave_add> <cmd> <data0> <data1> */
    uint8_t wrLen = I2C${I2C_INSTANCE_NAME}_HostPacketForm(I2C_SMB_HOST_PROTOCOL_WR_WORD, address, cmd, pWrdata, 2);
    I2C${I2C_INSTANCE_NAME}_HostWriteRead(I2C_SMB_HOST_PROTOCOL_WR_WORD, wrLen, 0);
}

void I2C${I2C_INSTANCE_NAME}_HostWriteBlock(uint8_t address, uint8_t cmd, void* pWrdata, uint32_t nWrBytes)
{
    /* <slave_add> <cmd> <wr_block_sz> <data0> <data1> .. <datan>*/
    uint8_t wrLen = I2C${I2C_INSTANCE_NAME}_HostPacketForm(I2C_SMB_HOST_PROTOCOL_WR_BLK, address, cmd, pWrdata, nWrBytes);
    I2C${I2C_INSTANCE_NAME}_HostWriteRead(I2C_SMB_HOST_PROTOCOL_WR_BLK, wrLen, 0);
}

void I2C${I2C_INSTANCE_NAME}_HostReadByte(uint8_t address, uint8_t cmd)
{
    /* <slave_add> <cmd> <slave_add> <data0> */
    uint8_t wrLen = I2C${I2C_INSTANCE_NAME}_HostPacketForm(I2C_SMB_HOST_PROTOCOL_RD_BYTE, address, cmd, NULL, 0);
    I2C${I2C_INSTANCE_NAME}_HostWriteRead(I2C_SMB_HOST_PROTOCOL_RD_BYTE, wrLen, 1);
}

void I2C${I2C_INSTANCE_NAME}_HostReadWord(uint8_t address, uint8_t cmd)
{
    /* <slave_add> <cmd> <slave_add> <data0> <data1> */
    uint8_t wrLen = I2C${I2C_INSTANCE_NAME}_HostPacketForm(I2C_SMB_HOST_PROTOCOL_RD_WORD, address, cmd, NULL, 0);
    I2C${I2C_INSTANCE_NAME}_HostWriteRead(I2C_SMB_HOST_PROTOCOL_RD_WORD, wrLen, 2);
}

void I2C${I2C_INSTANCE_NAME}_HostReadBlock(uint8_t address, uint8_t cmd)
{
    /* <slave_add> <cmd> <slave_add> <rd_block_sz> <data0> <data1> .. <datan>*/
    uint8_t wrLen = I2C${I2C_INSTANCE_NAME}_HostPacketForm(I2C_SMB_HOST_PROTOCOL_RD_BLK, address, cmd, NULL, 0);
    /* Set nRdBytes with max possible read count. It will be over-written by the first byte received from I2C slave. */
    I2C${I2C_INSTANCE_NAME}_HostWriteRead(I2C_SMB_HOST_PROTOCOL_RD_BLK, wrLen, sizeof(i2c${I2C_INSTANCE_NAME?lower_case}HostRdBuffer));
}

void I2C${I2C_INSTANCE_NAME}_HostWriteReadBlock(uint8_t address, uint8_t cmd, void* pWrdata, uint32_t nWrBytes)
{
    /* <slave_add> <cmd> <wr_block_sz> <data0> <data1> .. <datan> <slave_add> <rd_block_sz> <data0> <data1> .. <datan>*/
    uint8_t wrLen = I2C${I2C_INSTANCE_NAME}_HostPacketForm(I2C_SMB_HOST_PROTOCOL_WR_BLK_RD_BLK, address, cmd, pWrdata, nWrBytes);
    /* Set nRdBytes with max possible read count. It will be over-written by the first byte received from I2C slave. */
    I2C${I2C_INSTANCE_NAME}_HostWriteRead(I2C_SMB_HOST_PROTOCOL_WR_BLK_RD_BLK, wrLen, sizeof(i2c${I2C_INSTANCE_NAME?lower_case}HostRdBuffer));
}

uint32_t I2C${I2C_INSTANCE_NAME}_HostTransferCountGet(void)
{
    return DMA_ChannelGetTransferredCount(DMA_CHANNEL_${I2C_SMBUS_MASTER_DMA_CHANNEL});
}

uint32_t I2C${I2C_INSTANCE_NAME}_HostBufferRead(void* pBuffer)
{
    uint32_t i;
    uint32_t numBytesAvailable = DMA_ChannelGetTransferredCount(DMA_CHANNEL_${I2C_SMBUS_MASTER_DMA_CHANNEL});
    uint8_t PECConfig = ((${I2C_INSTANCE_NAME}_REGS->SMB_CFG[0] & SMB_CFG_PECEN_Msk) != 0U)? 1U: 0U;

    /* Discard the PEC byte received from the slave and the PEC register copied by the Master state machine */
    numBytesAvailable -= (PECConfig == 1U)? 2U : 0U;

    /* First byte in i2c${I2C_INSTANCE_NAME?lower_case}HostRdBuffer is always the address byte and hence not copied to application buffer */
    for (i = 0; i < numBytesAvailable; i++)
    {
        ((uint8_t*)pBuffer)[i] = i2c${I2C_INSTANCE_NAME?lower_case}HostRdBuffer[i];
    }

    return numBytesAvailable;
}

void I2C${I2C_INSTANCE_NAME}_HostInterruptHandler(uint32_t completion_reg)
{
    uint8_t PECConfig = ((${I2C_INSTANCE_NAME}_REGS->SMB_CFG[0] & SMB_CFG_PECEN_Msk) != 0U)? 1U: 0U;

    if ((completion_reg & SMB_COMPL_MDONE_Msk) != 0U)
    {
        if ((completion_reg & SMB_COMPL_BER_Msk) != 0U)
        {
            ${I2C_INSTANCE_NAME?lower_case}HostObj.error = ((uint32_t)${I2C_INSTANCE_NAME?lower_case}HostObj.error) | I2C_SMB_HOST_ERROR_BUS_COLLISION;
        }
        if ((completion_reg & SMB_COMPL_LAB_Msk) != 0U)
        {
            ${I2C_INSTANCE_NAME?lower_case}HostObj.error = ((uint32_t)${I2C_INSTANCE_NAME?lower_case}HostObj.error) | I2C_SMB_HOST_ERROR_ARBITRATION_LOST;
        }
        if ((completion_reg & SMB_COMPL_MNAKX_Msk) != 0U)
        {
            ${I2C_INSTANCE_NAME?lower_case}HostObj.error = ((uint32_t)${I2C_INSTANCE_NAME?lower_case}HostObj.error) | I2C_SMB_HOST_ERROR_NACK;
        }
        if ((completion_reg & SMB_COMPL_TIMERR_Msk) != 0U)
        {
            ${I2C_INSTANCE_NAME?lower_case}HostObj.error = ((uint32_t)${I2C_INSTANCE_NAME?lower_case}HostObj.error) | I2C_SMB_HOST_ERROR_TIMEOUT;
        }

        if (${I2C_INSTANCE_NAME?lower_case}HostObj.error == I2C_SMB_HOST_ERROR_NONE)
        {
            if ((${I2C_INSTANCE_NAME}_REGS->SMB_MCMD[0] & SMB_MCMD_MRUN_Msk) != 0U)
            {
                if ((${I2C_INSTANCE_NAME}_REGS->SMB_MCMD[0] & SMB_MCMD_MPROCEED_Msk) == 0U)
                {
                    if (${I2C_INSTANCE_NAME?lower_case}HostObj.dmaDirChange)
                    {
                        ${I2C_INSTANCE_NAME?lower_case}HostObj.dmaDirChange = false;

                        ${I2C_INSTANCE_NAME?lower_case}HostObj.state = I2C_SMB_HOST_STATE_RECEIVE;

                        (void)DMA_ChannelTransfer(DMA_CHANNEL_${I2C_SMBUS_MASTER_DMA_CHANNEL}, ${I2C_INSTANCE_NAME}_MRXB, (void*)i2c${I2C_INSTANCE_NAME?lower_case}HostRdBuffer, ${I2C_INSTANCE_NAME?lower_case}HostObj.dmaRdBytes);

                        /* Re-start the paused host state machine */
                        ${I2C_INSTANCE_NAME}_REGS->SMB_MCMD[0] |= SMB_MCMD_MPROCEED_Msk;
                    }
                }
            }
            else
            {
                /* Transfer completed without error. Abort the transfer on DMA channel for bulk read transfers. */
                if (((${I2C_INSTANCE_NAME?lower_case}HostObj.protocol == I2C_SMB_HOST_PROTOCOL_RD_BLK) || (${I2C_INSTANCE_NAME?lower_case}HostObj.protocol == I2C_SMB_HOST_PROTOCOL_WR_BLK_RD_BLK)) && (DMA_ChannelIsBusy(DMA_CHANNEL_${I2C_SMBUS_MASTER_DMA_CHANNEL})))
                {
                    DMA_ChannelTransferAbort(DMA_CHANNEL_${I2C_SMBUS_MASTER_DMA_CHANNEL});
                }

                if (${I2C_INSTANCE_NAME?lower_case}HostObj.state == I2C_SMB_HOST_STATE_RECEIVE)
                {
                    /* Check for PEC error here if enabled. The RXB register will be loaded with the PEC register by the Host state machine and the PEC register will be 0 if there is no PEC error. */
                    if ((PECConfig == 1U) && (${I2C_INSTANCE_NAME}_REGS->SMB_MTR_RXB != 0U))
                    {
                        ${I2C_INSTANCE_NAME?lower_case}HostObj.error |= I2C_SMB_HOST_ERROR_PEC;
                    }
                    else
                    {
                        if (${I2C_INSTANCE_NAME?lower_case}HostObj.callback != NULL)
                        {
                            ${I2C_INSTANCE_NAME?lower_case}HostObj.callback(I2C_SMB_HOST_TRANSFER_EVENT_RX_READY, ${I2C_INSTANCE_NAME?lower_case}HostObj.context);
                        }
                    }
                }

                ${I2C_INSTANCE_NAME?lower_case}HostObj.state = I2C_SMB_HOST_STATE_IDLE;

                if (${I2C_INSTANCE_NAME?lower_case}HostObj.callback != NULL)
                {
                    if (${I2C_INSTANCE_NAME?lower_case}HostObj.error == I2C_SMB_HOST_ERROR_NONE)
                    {
                        (void)${I2C_INSTANCE_NAME?lower_case}HostObj.callback(I2C_SMB_HOST_TRANSFER_EVENT_DONE, ${I2C_INSTANCE_NAME?lower_case}HostObj.context);
                    }
                    else
                    {
                        (void)${I2C_INSTANCE_NAME?lower_case}HostObj.callback(I2C_SMB_HOST_TRANSFER_EVENT_ERROR, ${I2C_INSTANCE_NAME?lower_case}HostObj.context);
                    }
                }
            }
        }
        else
        {
            /* Transfer complete with error. Abort the DMA channel and give callback */
            if (DMA_ChannelIsBusy(DMA_CHANNEL_${I2C_SMBUS_MASTER_DMA_CHANNEL}))
            {
                DMA_ChannelTransferAbort(DMA_CHANNEL_${I2C_SMBUS_MASTER_DMA_CHANNEL});
            }

            if ((${I2C_INSTANCE_NAME?lower_case}HostObj.error & (I2C_SMB_HOST_ERROR_BUS_COLLISION | I2C_SMB_HOST_ERROR_TIMEOUT)) != 0U)
            {
                I2C${I2C_INSTANCE_NAME}_HostReInitialize();
            }

            ${I2C_INSTANCE_NAME?lower_case}HostObj.state = I2C_SMB_HOST_STATE_IDLE;

            if (${I2C_INSTANCE_NAME?lower_case}HostObj.callback != NULL)
            {
                ${I2C_INSTANCE_NAME?lower_case}HostObj.callback(I2C_SMB_HOST_TRANSFER_EVENT_ERROR, ${I2C_INSTANCE_NAME?lower_case}HostObj.context);
            }
        }
    }
}

<#if I2C_OPERATING_MODE == "Master">
void ${I2C_NVIC_INTERRUPT_NAME}_InterruptHandler(void)
{
    uint32_t completion_reg;

    <#if I2C_INTERRUPT_TYPE == "AGGREGATE">
    ECIA_GIRQSourceClear(ECIA_AGG_INT_SRC_I2CSMB${I2C_INSTANCE_NUM});
    <#else>
    ECIA_GIRQSourceClear(ECIA_DIR_INT_SRC_I2CSMB${I2C_INSTANCE_NUM});
    </#if>

    completion_reg = ${I2C_INSTANCE_NAME}_REGS->SMB_COMPL[0];

    /* Clear the status bits */
    ${I2C_INSTANCE_NAME}_REGS->SMB_COMPL[0] = completion_reg;

    I2C${I2C_INSTANCE_NAME}_HostInterruptHandler(completion_reg);
}
</#if>
</#if>