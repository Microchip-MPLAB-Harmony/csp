/*******************************************************************************
  Inter-Integrated Circuit (I2C) Library
  Source File

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${I2C_INSTANCE_NAME?lower_case}_slave.c

  Summary:
    I2C PLIB SMBUS Slave Implementation file

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
#include "plib_${I2C_INSTANCE_NAME?lower_case}_slave.h"

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
#define ${I2C_INSTANCE_NAME}_STXB   (uint32_t*)(SMB${I2C_INSTANCE_NUM}_BASE_ADDRESS + SMB_SLV_TXB_REG_OFST)
#define ${I2C_INSTANCE_NAME}_SRXB   (uint32_t*)(SMB${I2C_INSTANCE_NUM}_BASE_ADDRESS + SMB_SLV_RXB_REG_OFST)

static I2C_SMB_TARGET_OBJ ${I2C_INSTANCE_NAME?lower_case}TargetObj;
static uint8_t i2c${I2C_INSTANCE_NAME?lower_case}TargetWrBuffer[64];
static uint8_t i2c${I2C_INSTANCE_NAME?lower_case}TargetRdBuffer[64];
</#if>

<#if I2C_OPERATING_MODE == "Slave">
void I2C${I2C_INSTANCE_NAME}_Initialize(void)
{
    /* Reset I2C */
    ${I2C_INSTANCE_NAME}_REGS->SMB_CFG[0] = SMB_CFG_RST_Msk;

    /* Reset bit must remain asserted for at-least 1 Baud clock period */
    NOP();NOP();NOP();NOP();NOP();

    ${I2C_INSTANCE_NAME}_REGS->SMB_CFG[0] &= ~SMB_CFG_RST_Msk;

    /* Set the port associated with this instance of I2C peripheral */
    ${I2C_INSTANCE_NAME}_REGS->SMB_CFG[0] = SMB_CFG_PORT_SEL(${I2C_PORT_SEL});

    /* Set Slave address */
    ${I2C_INSTANCE_NAME}_REGS->SMB_OWN_ADDR = SMB_OWN_ADDR_ADDR1(0x${I2C_SLAVE_ADDDRESS_1}) | SMB_OWN_ADDR_ADDR2(0x${I2C_SLAVE_ADDDRESS_2});

    <#if I2C_SMBUS_PEC_ENABLE == true>${I2C_INSTANCE_NAME}_REGS->SMB_PEC = 0;</#if>

    /* Repeated start hold time setup */
    ${I2C_INSTANCE_NAME}_REGS->SMB_RSHTM = I2C_SMB_RecommendedValues[2][0];

    /* Data timing register */
    ${I2C_INSTANCE_NAME}_REGS->SMB_DATATM = I2C_SMB_RecommendedValues[1][0];

    <#if I2C_SMBUS_TIMING_CHK_ENABLE == true>
    /* Timeout scaling register setup */
    ${I2C_INSTANCE_NAME}_REGS->SMB_TMOUTSC = I2C_SMB_RecommendedValues[4][0];
    ${I2C_INSTANCE_NAME}_REGS->SMB_COMPL[0] |= SMB_COMPL_SCEN_Msk;
    </#if>

    /* Enable I2C peripheral */
    ${I2C_INSTANCE_NAME}_REGS->SMB_CFG[0] |= SMB_CFG_EN_Msk <#if I2C_SMBUS_PEC_ENABLE == true>| SMB_CFG_PECEN_Msk </#if> <#if I2C_SMBUS_TIMING_CHK_ENABLE == true>| SMB_CFG_TCEN_Msk</#if>;

    /* Enable Serial output, enable I2C interrupt and set ACK bit */
    ${I2C_INSTANCE_NAME}_REGS->SMB_WCTRL = (SMB_WCTRL_ESO_Msk | SMB_WCTRL_ACK_Msk);

<#if I2C_SMBUS_LOW_LEVEL_API_ONLY == false>
    ${I2C_INSTANCE_NAME?lower_case}TargetObj.callback = NULL;
    ${I2C_INSTANCE_NAME?lower_case}TargetObj.error = I2C_SMB_TARGET_ERROR_NONE;
</#if>
}
<#else>
void I2C${I2C_INSTANCE_NAME}_TargetInitialize(void)
{
    /* Set Slave address */
    ${I2C_INSTANCE_NAME}_REGS->SMB_OWN_ADDR = SMB_OWN_ADDR_ADDR1(0x${I2C_SLAVE_ADDDRESS_1}) | SMB_OWN_ADDR_ADDR2(0x${I2C_SLAVE_ADDDRESS_2});

<#if I2C_SMBUS_LOW_LEVEL_API_ONLY == false>
    ${I2C_INSTANCE_NAME?lower_case}TargetObj.callback = NULL;

    ${I2C_INSTANCE_NAME?lower_case}TargetObj.error = I2C_SMB_TARGET_ERROR_NONE;
</#if>
}
</#if>

<#if I2C_SMBUS_LOW_LEVEL_API_ONLY == false>

static void I2C${I2C_INSTANCE_NAME}_TargetReInitialize(void)
{
    /* Reset I2C */
    ${I2C_INSTANCE_NAME}_REGS->SMB_CFG[0] = SMB_CFG_RST_Msk;

    /* Reset bit must remain asserted for at-least 1 Baud clock period */
    NOP();NOP();NOP();NOP();NOP();

    ${I2C_INSTANCE_NAME}_REGS->SMB_CFG[0] &= ~SMB_CFG_RST_Msk;

    /* Set the port associated with this instance of I2C peripheral */
    ${I2C_INSTANCE_NAME}_REGS->SMB_CFG[0] = SMB_CFG_PORT_SEL(${I2C_PORT_SEL});

    /* Set Slave address */
    ${I2C_INSTANCE_NAME}_REGS->SMB_OWN_ADDR = SMB_OWN_ADDR_ADDR1(0x${I2C_SLAVE_ADDDRESS_1}) | SMB_OWN_ADDR_ADDR2(0x${I2C_SLAVE_ADDDRESS_2});

    <#if I2C_SMBUS_PEC_ENABLE == true>${I2C_INSTANCE_NAME}_REGS->SMB_PEC = 0;</#if>

    /* Repeated start hold time setup */
    ${I2C_INSTANCE_NAME}_REGS->SMB_RSHTM = I2C_SMB_RecommendedValues[2][0];

    /* Data timing register */
    ${I2C_INSTANCE_NAME}_REGS->SMB_DATATM = I2C_SMB_RecommendedValues[1][0];

    <#if I2C_SMBUS_TIMING_CHK_ENABLE == true>
    /* Timeout scaling register setup */
    ${I2C_INSTANCE_NAME}_REGS->SMB_TMOUTSC = I2C_SMB_RecommendedValues[4][0];
    ${I2C_INSTANCE_NAME}_REGS->SMB_COMPL[0] |= SMB_COMPL_SCEN_Msk;
    </#if>

    /* Enable I2C peripheral */
    ${I2C_INSTANCE_NAME}_REGS->SMB_CFG[0] |= SMB_CFG_EN_Msk <#if I2C_SMBUS_PEC_ENABLE == true>| SMB_CFG_PECEN_Msk </#if> <#if I2C_SMBUS_TIMING_CHK_ENABLE == true>| SMB_CFG_TCEN_Msk</#if>;

    /* Enable Serial output, enable I2C interrupt and set ACK bit */
    ${I2C_INSTANCE_NAME}_REGS->SMB_WCTRL = (SMB_WCTRL_ESO_Msk | SMB_WCTRL_ACK_Msk);
}

void I2C${I2C_INSTANCE_NAME}_TargetCallbackRegister(I2C_SMB_TARGET_CALLBACK callback, uintptr_t contextHandle)
{
    if (callback == NULL)
    {
        return;
    }

    ${I2C_INSTANCE_NAME?lower_case}TargetObj.callback = callback;
    ${I2C_INSTANCE_NAME?lower_case}TargetObj.context = contextHandle;
}

bool I2C${I2C_INSTANCE_NAME}_TargetIsBusy(void)
{
    if ((${I2C_INSTANCE_NAME}_REGS->SMB_RSTS & SMB_RSTS_NBB_Msk) == 0U)
    {
        return true;
    }
    else
    {
        return false;
    }
}

I2C_SMB_TARGET_TRANSFER_DIR I2C${I2C_INSTANCE_NAME}_TargetTransferDirGet(void)
{
    return ${I2C_INSTANCE_NAME?lower_case}TargetObj.transferDir;
}

I2C_SMB_TARGET_ERROR I2C${I2C_INSTANCE_NAME}_TargetErrorGet(void)
{
    I2C_SMB_TARGET_ERROR error;

    error = ${I2C_INSTANCE_NAME?lower_case}TargetObj.error;
    ${I2C_INSTANCE_NAME?lower_case}TargetObj.error = I2C_SMB_TARGET_ERROR_NONE;

    return error;
}

void I2C${I2C_INSTANCE_NAME}_TargetStart(void)
{
    uint8_t PECConfig = ((${I2C_INSTANCE_NAME}_REGS->SMB_CFG[0] & SMB_CFG_PECEN_Msk) != 0U)? 1U: 0U;

    ${I2C_INSTANCE_NAME?lower_case}TargetObj.dmaDir = I2C_SMB_TARGET_DMA_DIR_PER_TO_MEM;

    /* Configure DMA for Slave RX */
    (void)DMA_ChannelTransfer(DMA_CHANNEL_${I2C_SMBUS_SLAVE_DMA_CHANNEL}, ${I2C_INSTANCE_NAME}_SRXB, (void*)i2c${I2C_INSTANCE_NAME?lower_case}TargetRdBuffer, sizeof(i2c${I2C_INSTANCE_NAME?lower_case}TargetRdBuffer));

    /* Enable SDONE (Slave Done) interrupt */
    ${I2C_INSTANCE_NAME}_REGS->SMB_CFG[0] |= SMB_CFG_ENSI_Msk;

    /* Set the target command and start the transfer */
    ${I2C_INSTANCE_NAME}_REGS->SMB_SCMD[0] = SMB_SCMD_RD_CNT(sizeof(i2c${I2C_INSTANCE_NAME?lower_case}TargetRdBuffer)) | SMB_SCMD_SRUN_Msk | SMB_SCMD_SPROCEED_Msk | SMB_SCMD_PEC(PECConfig);
}

uint32_t I2C${I2C_INSTANCE_NAME}_TargetBufferRead(void* pBuffer)
{
    uint32_t i;
    uint32_t numBytesAvailable = ${I2C_INSTANCE_NAME?lower_case}TargetObj.rxCount;

    for (i = 0; i < numBytesAvailable; i++)
    {
        ((uint8_t*)pBuffer)[i] = i2c${I2C_INSTANCE_NAME?lower_case}TargetRdBuffer[i];
    }

    ${I2C_INSTANCE_NAME?lower_case}TargetObj.rxCount = 0;

    return numBytesAvailable;
}

void I2C${I2C_INSTANCE_NAME}_TargetBufferWrite(void* pBuffer, uint32_t nBytes)
{
    uint32_t i = 0;

    for (i = 0; i < nBytes; i++)
    {
        i2c${I2C_INSTANCE_NAME?lower_case}TargetWrBuffer[i] = ((uint8_t*)pBuffer)[i];
    }

    ${I2C_INSTANCE_NAME?lower_case}TargetObj.txCount = nBytes;
}

void I2C${I2C_INSTANCE_NAME}_TargetInterruptHandler(uint32_t completion_reg)
{
    uint8_t PECConfig = ((${I2C_INSTANCE_NAME}_REGS->SMB_CFG[0] & SMB_CFG_PECEN_Msk) != 0U)? 1U: 0U;

    if ((completion_reg & SMB_COMPL_SDONE_Msk) != 0U)
    {
        DMA_ChannelTransferAbort(DMA_CHANNEL_${I2C_SMBUS_SLAVE_DMA_CHANNEL});

        if ((completion_reg & SMB_COMPL_BER_Msk) != 0U)
        {
            ${I2C_INSTANCE_NAME?lower_case}TargetObj.error |= I2C_SMB_TARGET_ERROR_BUS_COLLISION;
        }
        if ((completion_reg & SMB_COMPL_TIMERR_Msk) != 0U)
        {
            ${I2C_INSTANCE_NAME?lower_case}TargetObj.error |= I2C_SMB_TARGET_ERROR_TIMEOUT;
        }
        if (((${I2C_INSTANCE_NAME}_REGS->SMB_SCMD[0] & SMB_SCMD_SRUN_Msk) != 0U) && (${I2C_INSTANCE_NAME?lower_case}TargetObj.error == I2C_SMB_TARGET_ERROR_NONE))
        {
            if ((${I2C_INSTANCE_NAME}_REGS->SMB_SCMD[0] & SMB_SCMD_SPROCEED_Msk) == 0U)
            {
                if (((completion_reg & SMB_COMPL_REP_RD_Msk) != 0U) || ((completion_reg & SMB_COMPL_REP_WR_Msk) != 0U))
                {
                    if (${I2C_INSTANCE_NAME?lower_case}TargetObj.dmaDir == I2C_SMB_TARGET_DMA_DIR_PER_TO_MEM)
                    {
                        /* Read DMA transfer count and discard the address byte and the address byte received after repeated start. Additionally discard the PEC register written by slave state machine if PEC is enabled. */
                        ${I2C_INSTANCE_NAME?lower_case}TargetObj.rxCount = (DMA_ChannelGetTransferredCount(DMA_CHANNEL_${I2C_SMBUS_SLAVE_DMA_CHANNEL}) - 2U) - ((PECConfig == 1U)? 1U : 0U);

                        if (${I2C_INSTANCE_NAME?lower_case}TargetObj.callback != NULL)
                        {
                            (void)${I2C_INSTANCE_NAME?lower_case}TargetObj.callback(I2C_SMB_TARGET_TRANSFER_EVENT_RX_READY, ${I2C_INSTANCE_NAME?lower_case}TargetObj.context);
                        }
                    }
                    else
                    {
                        /* Target was transmitting. Check and notify if WR_COUNT became 0 before Host sent NAK or Host sent NAK before WR_COUNT became 0. */
                        if ((completion_reg & SMB_COMPL_SPROT_Msk) != 0U)
                        {
                            ${I2C_INSTANCE_NAME?lower_case}TargetObj.error |= I2C_SMB_TARGET_ERROR_SPROT;
                            (void)${I2C_INSTANCE_NAME?lower_case}TargetObj.callback(I2C_SMB_TARGET_TRANSFER_EVENT_ERROR, ${I2C_INSTANCE_NAME?lower_case}TargetObj.context);
                        }
                    }
                    if ((completion_reg & SMB_COMPL_REP_RD_Msk) != 0U)
                    {
                        if (${I2C_INSTANCE_NAME?lower_case}TargetObj.callback != NULL)
                        {
                            /* Application is expected to frame the response and make the response available by calling the I2C${I2C_INSTANCE_NAME}_TargetBufferWrite() API */
                            (void)${I2C_INSTANCE_NAME?lower_case}TargetObj.callback(I2C_SMB_TARGET_TRANSFER_EVENT_TX_READY, ${I2C_INSTANCE_NAME?lower_case}TargetObj.context);
                        }

                        ${I2C_INSTANCE_NAME?lower_case}TargetObj.transferDir = I2C_SMB_TARGET_TRANSFER_DIR_READ;
                    }
                    else
                    {
                        ${I2C_INSTANCE_NAME?lower_case}TargetObj.transferDir = I2C_SMB_TARGET_TRANSFER_DIR_WRITE;
                    }
                }
                else if (((${I2C_INSTANCE_NAME}_REGS->SMB_RSTS & SMB_RSTS_AAS_Msk) != 0U) && ((${I2C_INSTANCE_NAME}_REGS->SMB_SHDW_DATA & 0x01U) != 0U))
                {
                    /* This is executed when Host sends a Read request after a normal start bit (not repeated start). Application is expected to frame the response and make the response available by calling the I2C${I2C_INSTANCE_NAME}_SMBUSBufferWrite() API */
                    (void)${I2C_INSTANCE_NAME?lower_case}TargetObj.callback(I2C_SMB_TARGET_TRANSFER_EVENT_TX_READY, ${I2C_INSTANCE_NAME?lower_case}TargetObj.context);
                    ${I2C_INSTANCE_NAME?lower_case}TargetObj.transferDir = I2C_SMB_TARGET_TRANSFER_DIR_READ;
                }
                else
                {
                    /* Do nothing */
                }

                ${I2C_INSTANCE_NAME?lower_case}TargetObj.error = I2C_SMB_TARGET_ERROR_NONE;

                if (${I2C_INSTANCE_NAME?lower_case}TargetObj.transferDir == I2C_SMB_TARGET_TRANSFER_DIR_WRITE)
                {
                    /* Enter here when a Repeated Write request is received. Configure DMA for Target RX (peripheral to memory). */
                    (void)DMA_ChannelTransfer(DMA_CHANNEL_${I2C_SMBUS_SLAVE_DMA_CHANNEL}, ${I2C_INSTANCE_NAME}_SRXB, (void*)i2c${I2C_INSTANCE_NAME?lower_case}TargetRdBuffer, sizeof(i2c${I2C_INSTANCE_NAME?lower_case}TargetRdBuffer));

                    /* Set the target command and start the transfer */
                    ${I2C_INSTANCE_NAME}_REGS->SMB_SCMD[0] = SMB_SCMD_RD_CNT(sizeof(i2c${I2C_INSTANCE_NAME?lower_case}TargetRdBuffer)) | SMB_SCMD_SRUN_Msk | SMB_SCMD_SPROCEED_Msk | SMB_SCMD_PEC(PECConfig);

                    ${I2C_INSTANCE_NAME?lower_case}TargetObj.dmaDir = I2C_SMB_TARGET_DMA_DIR_PER_TO_MEM;
                }
                else
                {
                    /* Enter here when Repeated Read request is received. Configure DMA for Target TX (memory to peripheral) */
                    (void)DMA_ChannelTransfer(DMA_CHANNEL_${I2C_SMBUS_SLAVE_DMA_CHANNEL}, (void*)i2c${I2C_INSTANCE_NAME?lower_case}TargetWrBuffer, ${I2C_INSTANCE_NAME}_STXB, sizeof(i2c${I2C_INSTANCE_NAME?lower_case}TargetWrBuffer));

                    /* Set the target command and start the transfer */
                    ${I2C_INSTANCE_NAME}_REGS->SMB_SCMD[0] = SMB_SCMD_WR_CNT(${I2C_INSTANCE_NAME?lower_case}TargetObj.txCount) | SMB_SCMD_SRUN_Msk | SMB_SCMD_SPROCEED_Msk | SMB_SCMD_PEC(PECConfig);

                    ${I2C_INSTANCE_NAME?lower_case}TargetObj.dmaDir = I2C_SMB_TARGET_DMA_DIR_MEM_TO_PER;
                }
            }
        }
        else
        {
            if (${I2C_INSTANCE_NAME?lower_case}TargetObj.error == I2C_SMB_TARGET_ERROR_NONE)
            {
                if (${I2C_INSTANCE_NAME?lower_case}TargetObj.dmaDir == I2C_SMB_TARGET_DMA_DIR_PER_TO_MEM)
                {
                    /* Target was receiving. Discard the address byte */
                    ${I2C_INSTANCE_NAME?lower_case}TargetObj.rxCount = DMA_ChannelGetTransferredCount(DMA_CHANNEL_${I2C_SMBUS_SLAVE_DMA_CHANNEL}) - 1U;

                    if (PECConfig == 1U)
                    {
                        if (${I2C_INSTANCE_NAME}_REGS->SMB_SLV_RXB != 0U)
                        {
                            ${I2C_INSTANCE_NAME?lower_case}TargetObj.error |= I2C_SMB_TARGET_ERROR_PEC;
                        }
                        /* Discard the PEC byte sent by master (last byte) */
                        ${I2C_INSTANCE_NAME?lower_case}TargetObj.rxCount -= 1U;
                    }

                    if (${I2C_INSTANCE_NAME?lower_case}TargetObj.callback != NULL)
                    {
                        if (${I2C_INSTANCE_NAME?lower_case}TargetObj.error == I2C_SMB_TARGET_ERROR_NONE)
                        {
                            (void)${I2C_INSTANCE_NAME?lower_case}TargetObj.callback(I2C_SMB_TARGET_TRANSFER_EVENT_RX_READY, ${I2C_INSTANCE_NAME?lower_case}TargetObj.context);
                        }
                    }
                }
                else
                {
                    /* Target was transmitting. Check and notify if WR_COUNT became 0 before Host sent NAK or Host sent NAK before WR_COUNT became 0. */
                    if ((completion_reg & SMB_COMPL_SPROT_Msk) != 0U)
                    {
                        ${I2C_INSTANCE_NAME?lower_case}TargetObj.error |= I2C_SMB_TARGET_ERROR_SPROT;
                    }
                }
            }

            if ((${I2C_INSTANCE_NAME?lower_case}TargetObj.error & (I2C_SMB_TARGET_ERROR_TIMEOUT | I2C_SMB_TARGET_ERROR_BUS_COLLISION)) != 0U)
            {
                /* Controller must be reset and then re-initialized */
                I2C${I2C_INSTANCE_NAME}_TargetReInitialize();

                /* Enable SDONE (Slave Done) interrupt */
                ${I2C_INSTANCE_NAME}_REGS->SMB_CFG[0] |= SMB_CFG_ENSI_Msk;
            }

            if (${I2C_INSTANCE_NAME?lower_case}TargetObj.callback != NULL)
            {
                if (${I2C_INSTANCE_NAME?lower_case}TargetObj.error == I2C_SMB_TARGET_ERROR_NONE)
                {
                    (void)${I2C_INSTANCE_NAME?lower_case}TargetObj.callback(I2C_SMB_TARGET_TRANSFER_EVENT_DONE, ${I2C_INSTANCE_NAME?lower_case}TargetObj.context);
                }
                else
                {
                    (void)${I2C_INSTANCE_NAME?lower_case}TargetObj.callback(I2C_SMB_TARGET_TRANSFER_EVENT_ERROR, ${I2C_INSTANCE_NAME?lower_case}TargetObj.context);
                }
            }

            ${I2C_INSTANCE_NAME?lower_case}TargetObj.error = I2C_SMB_TARGET_ERROR_NONE;
            ${I2C_INSTANCE_NAME?lower_case}TargetObj.dmaDir = I2C_SMB_TARGET_DMA_DIR_PER_TO_MEM;

            (void)DMA_ChannelTransfer(DMA_CHANNEL_${I2C_SMBUS_SLAVE_DMA_CHANNEL}, ${I2C_INSTANCE_NAME}_SRXB, (void*)i2c${I2C_INSTANCE_NAME?lower_case}TargetRdBuffer, sizeof(i2c${I2C_INSTANCE_NAME?lower_case}TargetRdBuffer));
            /* Set the target command and start the transfer */
            ${I2C_INSTANCE_NAME}_REGS->SMB_SCMD[0] = SMB_SCMD_RD_CNT(sizeof(i2c${I2C_INSTANCE_NAME?lower_case}TargetRdBuffer)) | SMB_SCMD_SRUN_Msk | SMB_SCMD_SPROCEED_Msk | SMB_SCMD_PEC(PECConfig);
        }
    }
}

<#if I2C_OPERATING_MODE == "Slave">
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

    I2C${I2C_INSTANCE_NAME}_TargetInterruptHandler(completion_reg);
}
</#if>
</#if>