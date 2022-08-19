/*******************************************************************************
  Inter-Integrated Circuit (I2C) Library
  Source File

  Company:
    Microchip Technology Inc.

  File Name:
    plib_i2c${I2C_INSTANCE_NUM}_slave.c

  Summary:
    I2C PLIB Slave Implementation file

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
#include "../plib_i2c_smb_common.h"
#include "plib_i2c${I2C_INSTANCE_NUM}_slave.h"
#include "../../ecia/plib_ecia.h"
<#if I2C_SMBUS_PROTOCOL_EN == true>
#include "../../dma/plib_dma.h"
</#if>

// *****************************************************************************
// *****************************************************************************
// Section: Global Data
// *****************************************************************************
// *****************************************************************************
static I2C_SLAVE_OBJ i2c${I2C_INSTANCE_NUM}Obj;

void I2C${I2C_INSTANCE_NUM}_Initialize(void)
{
    /* Reset I2C */
    ${I2C_INSTANCE_NAME}_REGS->SMB_CFG[0] = SMB_CFG_RST_Msk;

    /* Reset bit must remain asserted for at-least 1 Baud clock period */
    asm("nop");asm("nop");asm("nop");asm("nop");asm("nop");
    asm("nop");asm("nop");asm("nop");asm("nop");asm("nop");
    asm("nop");asm("nop");asm("nop");asm("nop");asm("nop");
    asm("nop");asm("nop");asm("nop");asm("nop");asm("nop");

    /* Set the port associated with this instance of I2C peripheral */
    ${I2C_INSTANCE_NAME}_REGS->SMB_CFG[0] = SMB_CFG_PORT_SEL(${I2C_PORT_SEL});

    /* Set Slave address */
    ${I2C_INSTANCE_NAME}_REGS->SMB_OWN_ADDR = SMB_OWN_ADDR_ADDR1(0x${I2C_SLAVE_ADDDRESS_1}) | SMB_OWN_ADDR_ADDR2(0x${I2C_SLAVE_ADDDRESS_2});

    /* Repeated start hold time setup */
    ${I2C_INSTANCE_NAME}_REGS->SMB_RSHTM = I2C_SMB_RecommendedValues[2][0];

    /* Data timing register */
    ${I2C_INSTANCE_NAME}_REGS->SMB_DATATM = I2C_SMB_RecommendedValues[1][0];

    /* Enable I2C peripheral */
    ${I2C_INSTANCE_NAME}_REGS->SMB_CFG[0] |= SMB_CFG_EN_Msk;

    /* Enable Serial output, enable I2C interrupt and set ACK bit */
    ${I2C_INSTANCE_NAME}_REGS->SMB_WCTRL = (SMB_WCTRL_ESO_Msk | SMB_WCTRL_ENI_Msk | SMB_WCTRL_ACK_Msk);

    i2c${I2C_INSTANCE_NUM}Obj.callback = NULL;
    i2c${I2C_INSTANCE_NUM}Obj.error = I2C_SLAVE_ERROR_NONE;
}

/* I2C slave state machine */
static void I2C${I2C_INSTANCE_NUM}_TransferSM(void)
{
    uint32_t i2c_addr;
    uint8_t dummy;

    if (${I2C_INSTANCE_NAME}_REGS->SMB_RSTS & SMB_RSTS_BER_Msk)
    {
        i2c${I2C_INSTANCE_NUM}Obj.error = I2C_SLAVE_ERROR_BUS_COLLISION;

        if (i2c${I2C_INSTANCE_NUM}Obj.callback != NULL)
        {
            /* In the callback, slave must read out the error by calling I2Cx_ErrorGet() */
            (void)i2c${I2C_INSTANCE_NUM}Obj.callback(I2C_SLAVE_TRANSFER_EVENT_ERROR, i2c${I2C_INSTANCE_NUM}Obj.context);
        }

        return;
    }
    /* Check if addressed as slave (AAS) bit is set */
    if (${I2C_INSTANCE_NAME}_REGS->SMB_RSTS & SMB_RSTS_AAS_Msk)
    {
        i2c_addr = ${I2C_INSTANCE_NAME}_REGS->SMB_I2CDATA;

        i2c${I2C_INSTANCE_NUM}Obj.transferDir = (i2c_addr & 0x01)? I2C_SLAVE_TRANSFER_DIR_READ : I2C_SLAVE_TRANSFER_DIR_WRITE;

        if (i2c${I2C_INSTANCE_NUM}Obj.callback != NULL)
        {
            (void)i2c${I2C_INSTANCE_NUM}Obj.callback(I2C_SLAVE_TRANSFER_EVENT_ADDR_MATCH, i2c${I2C_INSTANCE_NUM}Obj.context);

            if (i2c${I2C_INSTANCE_NUM}Obj.transferDir == I2C_SLAVE_TRANSFER_DIR_READ)
            {
                /* I2C master wants to read (slave transmit) */
                /* In the callback, slave must write to transmit register by calling I2Cx_WriteByte() */
                (void)i2c${I2C_INSTANCE_NUM}Obj.callback(I2C_SLAVE_TRANSFER_EVENT_TX_READY, i2c${I2C_INSTANCE_NUM}Obj.context);
            }
        }
    }
    // Master reading from slave
    else if (i2c${I2C_INSTANCE_NUM}Obj.transferDir == I2C_SLAVE_TRANSFER_DIR_READ)
    {
        /* I2C master reading from slave */
        if ((${I2C_INSTANCE_NAME}_REGS->SMB_RSTS & SMB_RSTS_LRB_AD0_Msk) == 0)
        {
            /* ACK received, continue transmitting */
            if (i2c${I2C_INSTANCE_NUM}Obj.callback != NULL)
            {
                /* In the callback, slave must write to transmit register by calling I2Cx_WriteByte() */
                (void)i2c${I2C_INSTANCE_NUM}Obj.callback(I2C_SLAVE_TRANSFER_EVENT_TX_READY, i2c${I2C_INSTANCE_NUM}Obj.context);
            }
        }
        else
        {
            /* NAK received, stop transmission. Dummy write to clear the PIN status bit */
            ${I2C_INSTANCE_NAME}_REGS->SMB_I2CDATA = 0xFF;

            if (i2c${I2C_INSTANCE_NUM}Obj.callback != NULL)
            {
                (void)i2c${I2C_INSTANCE_NUM}Obj.callback(I2C_SLAVE_TRANSFER_EVENT_NAK_RECEIVED, i2c${I2C_INSTANCE_NUM}Obj.context);
            }
        }
    }
    // Master writing to slave
    else
    {
        /* I2C master writing to slave */
        if (${I2C_INSTANCE_NAME}_REGS->SMB_RSTS & SMB_RSTS_STS_Msk)
        {
            /* Stop received, do a dummy read to clear the PIN status bit */
            dummy = ${I2C_INSTANCE_NAME}_REGS->SMB_I2CDATA;
            dummy = dummy;

            if (i2c${I2C_INSTANCE_NUM}Obj.callback != NULL)
            {
                (void)i2c${I2C_INSTANCE_NUM}Obj.callback(I2C_SLAVE_TRANSFER_EVENT_STOP_BIT_RECEIVED, i2c${I2C_INSTANCE_NUM}Obj.context);
            }
        }
        else
        {
            if (i2c${I2C_INSTANCE_NUM}Obj.callback != NULL)
            {
                /* In the callback, slave must read data by calling I2Cx_ReadByte()  */
                (void)i2c${I2C_INSTANCE_NUM}Obj.callback(I2C_SLAVE_TRANSFER_EVENT_RX_READY, i2c${I2C_INSTANCE_NUM}Obj.context);
            }
        }
    }
}

uint8_t I2C${I2C_INSTANCE_NUM}_ReadByte(void)
{
    return ${I2C_INSTANCE_NAME}_REGS->SMB_I2CDATA;
}

void I2C${I2C_INSTANCE_NUM}_WriteByte(uint8_t wrByte)
{
    ${I2C_INSTANCE_NAME}_REGS->SMB_I2CDATA = wrByte;
}

uint8_t I2C${I2C_INSTANCE_NUM}_StatusFlagsGet(void)
{
    return (uint8_t)(${I2C_INSTANCE_NAME}_REGS->SMB_RSTS & SMB_RSTS_Msk);
}

void I2C${I2C_INSTANCE_NUM}_StatusFlagsReset(void)
{
    ${I2C_INSTANCE_NAME}_REGS->SMB_WCTRL |= SMB_WCTRL_PIN_Msk;
}

I2C_SLAVE_ACK_STATUS I2C${I2C_INSTANCE_NUM}_LastByteAckStatusGet(void)
{
    return (${I2C_INSTANCE_NAME}_REGS->SMB_RSTS & SMB_RSTS_LRB_AD0_Msk) ? I2C_SLAVE_ACK_STATUS_RECEIVED_NAK : I2C_SLAVE_ACK_STATUS_RECEIVED_ACK;
}

void I2C${I2C_INSTANCE_NUM}_CallbackRegister(I2C_SLAVE_CALLBACK callback, uintptr_t contextHandle)
{
    if (callback == NULL)
    {
        return;
    }

    i2c${I2C_INSTANCE_NUM}Obj.callback = callback;
    i2c${I2C_INSTANCE_NUM}Obj.context = contextHandle;
}

bool I2C${I2C_INSTANCE_NUM}_IsBusy(void)
{
    if ((${I2C_INSTANCE_NAME}_REGS->SMB_RSTS & SMB_RSTS_NBB_Msk) == 0)
    {
        return true;
    }
    else
    {
        return false;
    }
}

I2C_SLAVE_TRANSFER_DIR I2C${I2C_INSTANCE_NUM}_TransferDirGet(void)
{
    return i2c${I2C_INSTANCE_NUM}Obj.transferDir;
}

I2C_SLAVE_ERROR I2C${I2C_INSTANCE_NUM}_ErrorGet(void)
{
    I2C_SLAVE_ERROR error;

    error = i2c${I2C_INSTANCE_NUM}Obj.error;
    i2c${I2C_INSTANCE_NUM}Obj.error = I2C_SLAVE_ERROR_NONE;

    return error;
}

static void I2C${I2C_INSTANCE_NUM}_SLAVE_InterruptHandler(void)
{
    I2C${I2C_INSTANCE_NUM}_TransferSM();
}

void ${I2C_NVIC_INTERRUPT_NAME}_InterruptHandler(void)
{
    <#if I2C_INTERRUPT_TYPE == "AGGREGATE">
    ECIA_GIRQSourceClear(ECIA_AGG_INT_SRC_I2CSMB${I2C_INSTANCE_NUM});
    <#else>
    ECIA_GIRQSourceClear(ECIA_DIR_INT_SRC_I2CSMB${I2C_INSTANCE_NUM});
    </#if>

    I2C${I2C_INSTANCE_NUM}_SLAVE_InterruptHandler();
}