/*******************************************************************************
  SPI Peripheral Target Peripheral Library Interface Source File

  Company
    Microchip Technology Inc.

  File Name
    plib_${SPT_INSTANCE_NAME?lower_case}.c

  Summary
    ${SPT_INSTANCE_NAME} peripheral library source file.

  Description
    This file implements the interface to the SPI Peripheral Target peripheral
    library. This library provides access to and control of the associated
    peripheral instance.

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


// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
#include "device.h"
<#if core.CoreSysIntFile == true>
#include "interrupts.h"
</#if>
#include "plib_${SPT_INSTANCE_NAME?lower_case}.h"
<#if SPT_MODE == "Advanced">
#include "peripheral/ecia/plib_ecia.h"

static SPT_CALLBACK_OBJ ${SPT_INSTANCE_NAME}_CallbackObject;
</#if>

void ${SPT_INSTANCE_NAME}_Initialize(void)
{
    <#if SPT_MODE == "Advanced">

    ${SPT_INSTANCE_NAME}_REGS->SPT_SPI_CFG = SPT_SPI_CFG_WAIT_TIME(${SPT_WAIT_TIME}) | SPT_SPI_CFG_TAR_TIM_SEL(${SPT_TAR_TIME}) <#if SPT_WIRE_CONFIG == "Quad"> | SPT_SPI_CFG_SNG_QUD_SEL_Msk</#if>;

    ${SPT_INSTANCE_NAME}_REGS->SPT_SPI_IEN = 0x${SPT_SPI_HOST_IEN_REG};

    ${SPT_INSTANCE_NAME}_REGS->SPT_EC_IEN = 0x${SPT_SPI_EC_IEN_REG};

    </#if>

    ${SPT_INSTANCE_NAME}_REGS->SPT_SYS_CFG = 0x${SPT_SYS_CFG_REG};
}

<#if SPT_MODE == "Advanced">
void ${SPT_INSTANCE_NAME}_WaitTimeSet(uint8_t wait_time)
{
    ${SPT_INSTANCE_NAME}_REGS->SPT_SPI_CFG = (${SPT_INSTANCE_NAME}_REGS->SPT_SPI_CFG & ~SPT_SPI_CFG_WAIT_TIME_Msk) | SPT_SPI_CFG_WAIT_TIME(wait_time);
}

void ${SPT_INSTANCE_NAME}_TARTimeSet(uint8_t tar_cycles)
{
    ${SPT_INSTANCE_NAME}_REGS->SPT_SPI_CFG = (${SPT_INSTANCE_NAME}_REGS->SPT_SPI_CFG & ~SPT_SPI_CFG_TAR_TIM_SEL_Msk) | SPT_SPI_CFG_TAR_TIM_SEL(tar_cycles);
}

void ${SPT_INSTANCE_NAME}_QuadModeEnable(void)
{
    ${SPT_INSTANCE_NAME}_REGS->SPT_SPI_CFG |= SPT_SPI_CFG_SNG_QUD_SEL_Msk;
}

void ${SPT_INSTANCE_NAME}_QuadModeDisable(void)
{
    ${SPT_INSTANCE_NAME}_REGS->SPT_SPI_CFG &= ~SPT_SPI_CFG_SNG_QUD_SEL_Msk;
}

void ${SPT_INSTANCE_NAME}_ECInterruptEnable(SPT_EC_INT int_en)
{
    ${SPT_INSTANCE_NAME}_REGS->SPT_EC_IEN = int_en;
}

uint32_t ${SPT_INSTANCE_NAME}_MailBoxRead(void)
{
    return ${SPT_INSTANCE_NAME}_REGS->SPT_SPIM2EC_MBX;
}

void ${SPT_INSTANCE_NAME}_MailBoxWrite(uint32_t data)
{
    ${SPT_INSTANCE_NAME}_REGS->SPT_EC2SPIM_MBX = data;
}

void ${SPT_INSTANCE_NAME}_CallbackRegister( SPT_CALLBACK callback, uintptr_t context )
{
    ${SPT_INSTANCE_NAME}_CallbackObject.callback = callback;

    ${SPT_INSTANCE_NAME}_CallbackObject.context = context;
}

<#else>
void ${SPT_INSTANCE_NAME}_ECDataAvailableSet(void)
{
    ${SPT_INSTANCE_NAME}_REGS->SPT_SYS_CFG |= SPT_SYS_CFG_ECDATL_Msk;
}
</#if>

uint32_t ${SPT_INSTANCE_NAME}_ECStatusRegGet(void)
{
    return ${SPT_INSTANCE_NAME}_REGS->SPT_SPI_EC_STS;
}

void ${SPT_INSTANCE_NAME}_ECStatusRegClear(uint32_t bitmask)
{
    ${SPT_INSTANCE_NAME}_REGS->SPT_SPI_EC_STS = bitmask;
}

void ${SPT_INSTANCE_NAME}_MEM0Config(uint32_t bar, uint32_t wr_lim, uint32_t rd_lim)
{
    ${SPT_INSTANCE_NAME}_REGS->SPT_MEM_BAR0 = bar;
    ${SPT_INSTANCE_NAME}_REGS->SPT_MEM_WR_LIM0 = wr_lim;
    ${SPT_INSTANCE_NAME}_REGS->SPT_MEM_RD_LIM0 = rd_lim;
    ${SPT_INSTANCE_NAME}_REGS->SPT_MEM_CFG |= SPT_MEM_CFG_BAR_EN0_SEL_Msk;
}

void ${SPT_INSTANCE_NAME}_MEM1Config(uint32_t bar, uint32_t wr_lim, uint32_t rd_lim)
{
    ${SPT_INSTANCE_NAME}_REGS->SPT_MEM_BAR1 = bar;
    ${SPT_INSTANCE_NAME}_REGS->SPT_MEM_WR_LIM1 = wr_lim;
    ${SPT_INSTANCE_NAME}_REGS->SPT_MEM_RD_LIM1 = rd_lim;
    ${SPT_INSTANCE_NAME}_REGS->SPT_MEM_CFG |= SPT_MEM_CFG_BAR_EN1_SEL_Msk;
}

void ${SPT_INSTANCE_NAME}_MEM0Enable(void)
{
    ${SPT_INSTANCE_NAME}_REGS->SPT_MEM_CFG |= SPT_MEM_CFG_BAR_EN0_SEL_Msk;
}

void ${SPT_INSTANCE_NAME}_MEM1Enable(void)
{
    ${SPT_INSTANCE_NAME}_REGS->SPT_MEM_CFG |= SPT_MEM_CFG_BAR_EN1_SEL_Msk;
}

void ${SPT_INSTANCE_NAME}_MEM0Disable(void)
{
    ${SPT_INSTANCE_NAME}_REGS->SPT_MEM_CFG &= ~SPT_MEM_CFG_BAR_EN0_SEL_Msk;
}

void ${SPT_INSTANCE_NAME}_MEM1Disable(void)
{
    ${SPT_INSTANCE_NAME}_REGS->SPT_MEM_CFG &= ~SPT_MEM_CFG_BAR_EN1_SEL_Msk;
}

uint32_t ${SPT_INSTANCE_NAME}_RXFIFOByteCountGet(void)
{
    return ${SPT_INSTANCE_NAME}_REGS->SPT_RXF_BYTE_CNT;
}

uint32_t ${SPT_INSTANCE_NAME}_TXFIFOByteCountGet(void)
{
    return ${SPT_INSTANCE_NAME}_REGS->SPT_TXF_BYTE_CNT;
}

uint32_t ${SPT_INSTANCE_NAME}_RXFIFOBaseAddrGet(void)
{
    return ${SPT_INSTANCE_NAME}_REGS->SPT_RXF_HOST_BAR;
}

uint32_t ${SPT_INSTANCE_NAME}_TXFIFOBaseAddrGet(void)
{
    return ${SPT_INSTANCE_NAME}_REGS->SPT_TXF_HOST_BAR;
}

void ${SPT_INSTANCE_NAME}_Enable(void)
{
    ${SPT_INSTANCE_NAME}_REGS->SPT_SYS_CFG |= SPT_SYS_CFG_SPI_SLV_EN_Msk;
}

void ${SPT_INSTANCE_NAME}_Disable(void)
{
    ${SPT_INSTANCE_NAME}_REGS->SPT_SYS_CFG &= ~SPT_SYS_CFG_SPI_SLV_EN_Msk;
}

uint32_t ${SPT_INSTANCE_NAME}_HostToECMBXRead(void)
{
    return ${SPT_INSTANCE_NAME}_REGS->SPT_SPIM2EC_MBX;
}

void ${SPT_INSTANCE_NAME}_HostToECMBXClr(void)
{
    ${SPT_INSTANCE_NAME}_REGS->SPT_SPIM2EC_MBX = 0xFFFFFFFF;
}

void ${SPT_INSTANCE_NAME}_ECToHostMBXWrite(uint32_t val)
{
    ${SPT_INSTANCE_NAME}_REGS->SPT_EC2SPIM_MBX = val;
}

uint32_t ${SPT_INSTANCE_NAME}_ECToHostMBXRead(void)
{
    return ${SPT_INSTANCE_NAME}_REGS->SPT_EC2SPIM_MBX;
}

<#if SPT_MODE == "Advanced">
<#compress>
<#assign INT_HANDLER_NAME_PREFIX = "">
<#if .vars["SPT_EC_INTERRUPT_TYPE"] == "AGGREGATE">
<#assign INT_HANDLER_NAME_PREFIX = "_GRP">
</#if>
</#compress>

void ${SPT_INSTANCE_NAME}${INT_HANDLER_NAME_PREFIX}_InterruptHandler(void)
{
    <#if .vars["SPT_EC_INTERRUPT_TYPE"] == "AGGREGATE">
    if (ECIA_GIRQResultGet(ECIA_AGG_INT_SRC_${SPT_INSTANCE_NAME}))
    <#else>
    if (ECIA_GIRQResultGet(ECIA_DIR_INT_SRC_${SPT_INSTANCE_NAME}))
    </#if>
    {
        uint32_t status = ${SPT_INSTANCE_NAME}_REGS->SPT_SPI_EC_STS;
        
        <#if .vars["SPT_EC_INTERRUPT_TYPE"] == "AGGREGATE">
        ECIA_GIRQSourceClear(ECIA_AGG_INT_SRC_${SPT_INSTANCE_NAME});
        <#else>
        ECIA_GIRQSourceClear(ECIA_DIR_INT_SRC_${SPT_INSTANCE_NAME});
        </#if>

        if (${SPT_INSTANCE_NAME}_CallbackObject.callback != NULL)
        {
            ${SPT_INSTANCE_NAME}_CallbackObject.callback(status, ${SPT_INSTANCE_NAME}_CallbackObject.context);
        }
        
        /* Clear the status bits */
        ${SPT_INSTANCE_NAME}_REGS->SPT_SPI_EC_STS = status;
    }
}
</#if>


