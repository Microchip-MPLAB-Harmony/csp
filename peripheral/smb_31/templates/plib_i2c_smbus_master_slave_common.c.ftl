/*******************************************************************************
  Inter-Integrated Circuit (I2C) Library
  Source File

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${I2C_INSTANCE_NAME?lower_case}_master_slave_common.c

  Summary:
    I2C PLIB Master-Slave Mode Common Implementation file

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
#include "plib_i2c_smb_common.h"
<#if I2C_SMBUS_LOW_LEVEL_API_ONLY == false>
#include "../ecia/plib_ecia.h"
</#if>
// *****************************************************************************
// *****************************************************************************
// Section: Global Data
// *****************************************************************************
// *****************************************************************************

void I2C${I2C_INSTANCE_NAME}_HostInitialize(void);
void I2C${I2C_INSTANCE_NAME}_TargetInitialize(void);
<#if I2C_SMBUS_LOW_LEVEL_API_ONLY == false>
void I2C${I2C_INSTANCE_NAME}_HostInterruptHandler(uint32_t completion_reg);
void I2C${I2C_INSTANCE_NAME}_TargetInterruptHandler(uint32_t completion_reg);
</#if>

void I2C${I2C_INSTANCE_NAME}_Initialize(void)
{
    /* Reset I2C */
    ${I2C_INSTANCE_NAME}_REGS->SMB_CFG[0] = SMB_CFG_RST_Msk;

    /* Reset bit must remain asserted for at-least 1 Baud clock period */
    asm("nop");asm("nop");asm("nop");asm("nop");asm("nop");

    ${I2C_INSTANCE_NAME}_REGS->SMB_CFG[0] &= ~SMB_CFG_RST_Msk;

    /* Set the port associated with this instance of I2C peripheral */
    ${I2C_INSTANCE_NAME}_REGS->SMB_CFG[0] = SMB_CFG_PORT_SEL(${I2C_PORT_SEL});

    I2C${I2C_INSTANCE_NAME}_HostInitialize();

    I2C${I2C_INSTANCE_NAME}_TargetInitialize();

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

    /* Enable Serial output and set ACK bit */
    ${I2C_INSTANCE_NAME}_REGS->SMB_WCTRL = (SMB_WCTRL_ESO_Msk | SMB_WCTRL_ACK_Msk);
}

<#if I2C_SMBUS_LOW_LEVEL_API_ONLY == false>
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

    I2C${I2C_INSTANCE_NAME}_HostInterruptHandler(completion_reg);
}
</#if>