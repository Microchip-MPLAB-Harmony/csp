/*******************************************************************************
  EC Register Bank Peripheral Library

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${ERB_INSTANCE_NAME?lower_case}.c

  Summary:
    EC Register Bank Source File

  Description:
    None

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
<#if CoreSysIntFile == true>
#include "interrupts.h"
</#if>
#include "peripheral/ecia/plib_ecia.h"
#include "plib_${ERB_INSTANCE_NAME?lower_case}.h"

// *****************************************************************************
// *****************************************************************************
// Section: ${ERB_INSTANCE_NAME} Implementation
// *****************************************************************************
// *****************************************************************************
<#compress>
<#assign pad_mon_ctrl_reg = "">
<#assign pad_mon_int_en_reg = "">

<#list 1..(2) as n>
    <#assign ERB_VTRx_PAD_MON_OVERRIDE_EN   = "ERB_VTR" + n + "_PAD_MON_OVERRIDE_EN">
    <#assign ERB_VTRx_INP_BUF_DIS           = "ERB_VTR" + n + "_INP_BUF_DIS">
    <#assign ERB_VTRx_PAD_MON_PROTECT_EN    = "ERB_VTR" + n + "_PAD_MON_PROTECT_EN">
    <#assign ERB_VTRx_CTRL                  = "ERB_VTR" + n + "_CTRL">
    
    <#assign ERB_PAD_MON_VTRx_PU_INT_EN     = "ERB_PAD_MON_VTR" + n + "_PU_INT_EN">
    <#assign ERB_PAD_MON_VTRx_PD_INT_EN     = "ERB_PAD_MON_VTR" + n + "_PD_INT_EN">
    
    <#if .vars[ERB_VTRx_PAD_MON_OVERRIDE_EN] == true>
        <#if pad_mon_ctrl_reg != "">
            <#assign pad_mon_ctrl_reg = pad_mon_ctrl_reg + " | EC_REG_BANK_PD_MON_CTRL_OVRD_VTR" + n + "_Msk">
        <#else>
            <#assign pad_mon_ctrl_reg = "EC_REG_BANK_PD_MON_CTRL_OVRD_VTR" + n + "_Msk">
        </#if>
    </#if>
    
    <#if .vars[ERB_VTRx_INP_BUF_DIS] == true>
        <#if pad_mon_ctrl_reg != "">
            <#assign pad_mon_ctrl_reg = pad_mon_ctrl_reg + " | EC_REG_BANK_PD_MON_CTRL_VTR" + n + "_INPT_DIS_Msk">
        <#else>
            <#assign pad_mon_ctrl_reg = "EC_REG_BANK_PD_MON_CTRL_VTR" + n + "_INPT_DIS_Msk">
        </#if>
    </#if>
    
    <#if .vars[ERB_VTRx_PAD_MON_PROTECT_EN] == false>
        <#if pad_mon_ctrl_reg != "">
            <#assign pad_mon_ctrl_reg = pad_mon_ctrl_reg + " | EC_REG_BANK_PD_MON_CTRL_VTR" + n + "_PROTECN_Msk">
        <#else>
            <#assign pad_mon_ctrl_reg = "EC_REG_BANK_PD_MON_CTRL_VTR" + n + "_PROTECN_Msk">
        </#if>
    </#if>
    
    <#if .vars[ERB_VTRx_CTRL] != "0x0">
        <#if pad_mon_ctrl_reg != "">
            <#assign pad_mon_ctrl_reg = pad_mon_ctrl_reg + " | EC_REG_BANK_PD_MON_CTRL_CTRL_VTR" + n + "(" + .vars[ERB_VTRx_CTRL] + ")">
        <#else>
            <#assign pad_mon_ctrl_reg = "EC_REG_BANK_PD_MON_CTRL_CTRL_VTR" + n + "(" + .vars[ERB_VTRx_CTRL] + ")">
        </#if>
    </#if>
    
    <#if .vars[ERB_PAD_MON_VTRx_PU_INT_EN] == true>
        <#if pad_mon_int_en_reg != "">
            <#assign pad_mon_int_en_reg = pad_mon_int_en_reg + " | EC_REG_BANK_PD_MON_INT_EN_VTR" + n + "_PU_INTEN_Msk">
        <#else>
            <#assign pad_mon_int_en_reg = "EC_REG_BANK_PD_MON_INT_EN_VTR" + n + "_PU_INTEN_Msk">
        </#if>
    </#if>
    
    <#if .vars[ERB_PAD_MON_VTRx_PD_INT_EN] == true>
        <#if pad_mon_int_en_reg != "">
            <#assign pad_mon_int_en_reg = pad_mon_int_en_reg + " | EC_REG_BANK_PD_MON_INT_EN_VTR" + n + "_PD_INTEN_Msk">
        <#else>
            <#assign pad_mon_int_en_reg = "EC_REG_BANK_PD_MON_INT_EN_VTR" + n + "_PD_INTEN_Msk">
        </#if>
    </#if>        
</#list>
</#compress>

EC_REG_BANK_OBJECT ec_reg_bank[2] = {0};

void ${ERB_INSTANCE_NAME}_Initialize( void )
{
    <#if ERB_AHB_ERROR_CTRL == true>
    EC_REG_BANK_REGS->EC_REG_BANK_AHB_ERR_CTRL = 1;
    </#if>
    
    <#if ERB_ALT_NVIC_INT_EN == false>
    EC_REG_BANK_REGS->EC_REG_BANK_AHB_ERR_CTRL = 0;
    </#if>
    
    <#if pad_mon_ctrl_reg != "">
    EC_REG_BANK_REGS->EC_REG_BANK_PD_MON_CTRL = ${pad_mon_ctrl_reg};
    </#if>
    
    <#if pad_mon_int_en_reg != "">
    EC_REG_BANK_REGS->EC_REG_BANK_PD_MON_INT_EN = ${pad_mon_int_en_reg};
    </#if>
    
}
uint32_t ${ERB_INSTANCE_NAME}_AHBErrorAddrGet(void)
{
    return EC_REG_BANK_REGS->EC_REG_BANK_AHB_ERR_ADDR;
}

void ${ERB_INSTANCE_NAME}_AHBErrorAddrClr(void)
{
    EC_REG_BANK_REGS->EC_REG_BANK_AHB_ERR_ADDR = 0;
}

void ${ERB_INSTANCE_NAME}_AHBErrorEnable(void)
{
    EC_REG_BANK_REGS->EC_REG_BANK_AHB_ERR_CTRL = 0;
}

void ${ERB_INSTANCE_NAME}_AHBErrorDisable(void)
{
    EC_REG_BANK_REGS->EC_REG_BANK_AHB_ERR_CTRL = 0;
}

void ${ERB_INSTANCE_NAME}_AltNVICVectorsEnable(void)
{
    EC_REG_BANK_REGS->EC_REG_BANK_INTR_CTRL = 1;
}

void ${ERB_INSTANCE_NAME}_VTR1PadMonDebounceCtrl(VTR_PAD_MON_DEB_CTRL ctrl)
{
    EC_REG_BANK_REGS->EC_REG_BANK_PD_MON_CTRL = (ctrl << EC_REG_BANK_PD_MON_CTRL_CTRL_VTR1_Pos);
}

void ${ERB_INSTANCE_NAME}_VTR1PadMonOverrideEn(void)
{
    EC_REG_BANK_REGS->EC_REG_BANK_PD_MON_CTRL |= EC_REG_BANK_PD_MON_CTRL_OVRD_VTR1_Msk;
}

void ${ERB_INSTANCE_NAME}_VTR1PadMonOverrideDis(void)
{
    EC_REG_BANK_REGS->EC_REG_BANK_PD_MON_CTRL &= ~EC_REG_BANK_PD_MON_CTRL_OVRD_VTR1_Msk;
}

void ${ERB_INSTANCE_NAME}_VTR1PadMonOverrideInpDis(void)
{
    EC_REG_BANK_REGS->EC_REG_BANK_PD_MON_CTRL |= EC_REG_BANK_PD_MON_CTRL_VTR1_INPT_DIS_Msk;
}

void ${ERB_INSTANCE_NAME}_VTR1PadMonOverrideInpEn(void)
{
    EC_REG_BANK_REGS->EC_REG_BANK_PD_MON_CTRL &= ~EC_REG_BANK_PD_MON_CTRL_VTR1_INPT_DIS_Msk;
}

void ${ERB_INSTANCE_NAME}_VTR1PadMonOverrideProtEn(void)
{
    EC_REG_BANK_REGS->EC_REG_BANK_PD_MON_CTRL &= ~EC_REG_BANK_PD_MON_CTRL_VTR1_PROTECN_Msk;
}

void ${ERB_INSTANCE_NAME}_VTR1PadMonOverrideProtDis(void)
{
    EC_REG_BANK_REGS->EC_REG_BANK_PD_MON_CTRL |= EC_REG_BANK_PD_MON_CTRL_VTR1_PROTECN_Msk;
}

void ${ERB_INSTANCE_NAME}_VTR1PadMonPUIntEn(void)
{
    EC_REG_BANK_REGS->EC_REG_BANK_PD_MON_INT_EN |= EC_REG_BANK_PD_MON_INT_EN_VTR1_PU_INTEN_Msk;
}

void ${ERB_INSTANCE_NAME}_VTR1PadMonPUIntDis(void)
{
    EC_REG_BANK_REGS->EC_REG_BANK_PD_MON_INT_EN &= ~EC_REG_BANK_PD_MON_INT_EN_VTR1_PU_INTEN_Msk;
}

void ${ERB_INSTANCE_NAME}_VTR1PadMonPDIntEn(void)
{
    EC_REG_BANK_REGS->EC_REG_BANK_PD_MON_INT_EN |= EC_REG_BANK_PD_MON_INT_EN_VTR1_PD_INTEN_Msk;
}

void ${ERB_INSTANCE_NAME}_VTR1PadMonPDIntDis(void)
{
    EC_REG_BANK_REGS->EC_REG_BANK_PD_MON_INT_EN &= ~EC_REG_BANK_PD_MON_INT_EN_VTR1_PD_INTEN_Msk;
}

void ${ERB_INSTANCE_NAME}_VTR2PadMonDebounceCtrl(VTR_PAD_MON_DEB_CTRL ctrl)
{
    EC_REG_BANK_REGS->EC_REG_BANK_PD_MON_CTRL = (ctrl << EC_REG_BANK_PD_MON_CTRL_CTRL_VTR2_Pos);
}

void ${ERB_INSTANCE_NAME}_VTR2PadMonOverrideEn(void)
{
    EC_REG_BANK_REGS->EC_REG_BANK_PD_MON_CTRL |= EC_REG_BANK_PD_MON_CTRL_OVRD_VTR2_Msk;
}

void ${ERB_INSTANCE_NAME}_VTR2PadMonOverrideDis(void)
{
    EC_REG_BANK_REGS->EC_REG_BANK_PD_MON_CTRL &= ~EC_REG_BANK_PD_MON_CTRL_OVRD_VTR2_Msk;
}

void ${ERB_INSTANCE_NAME}_VTR2PadMonOverrideInpDis(void)
{
    EC_REG_BANK_REGS->EC_REG_BANK_PD_MON_CTRL |= EC_REG_BANK_PD_MON_CTRL_VTR2_INPT_DIS_Msk;
}

void ${ERB_INSTANCE_NAME}_VTR2PadMonOverrideInpEn(void)
{
    EC_REG_BANK_REGS->EC_REG_BANK_PD_MON_CTRL &= ~EC_REG_BANK_PD_MON_CTRL_VTR2_INPT_DIS_Msk;
}

void ${ERB_INSTANCE_NAME}_VTR2PadMonOverrideProtEn(void)
{
    EC_REG_BANK_REGS->EC_REG_BANK_PD_MON_CTRL &= ~EC_REG_BANK_PD_MON_CTRL_VTR2_PROTECN_Msk;
}

void ${ERB_INSTANCE_NAME}_VTR2PadMonOverrideProtDis(void)
{
    EC_REG_BANK_REGS->EC_REG_BANK_PD_MON_CTRL |= EC_REG_BANK_PD_MON_CTRL_VTR2_PROTECN_Msk;
}

void ${ERB_INSTANCE_NAME}_VTR2PadMonPUIntEn(void)
{
    EC_REG_BANK_REGS->EC_REG_BANK_PD_MON_INT_EN |= EC_REG_BANK_PD_MON_INT_EN_VTR2_PU_INTEN_Msk;
}

void ${ERB_INSTANCE_NAME}_VTR2PadMonPUIntDis(void)
{
    EC_REG_BANK_REGS->EC_REG_BANK_PD_MON_INT_EN &= ~EC_REG_BANK_PD_MON_INT_EN_VTR2_PU_INTEN_Msk;
}

void ${ERB_INSTANCE_NAME}_VTR2PadMonPDIntEn(void)
{
    EC_REG_BANK_REGS->EC_REG_BANK_PD_MON_INT_EN |= EC_REG_BANK_PD_MON_INT_EN_VTR2_PD_INTEN_Msk;
}

void ${ERB_INSTANCE_NAME}_VTR2PadMonPDIntDis(void)
{
    EC_REG_BANK_REGS->EC_REG_BANK_PD_MON_INT_EN &= ~EC_REG_BANK_PD_MON_INT_EN_VTR2_PD_INTEN_Msk;
}

VTR1_PAD_MON_STS ${ERB_INSTANCE_NAME}_VTR1PadMonStatusGet(void)
{
    return EC_REG_BANK_REGS->EC_REG_BANK_PD_MON_STS & (EC_REG_BANK_PD_MON_STS_VTR1_PD_STS_Msk | EC_REG_BANK_PD_MON_STS_VTR1_PU_STS_Msk | EC_REG_BANK_PD_MON_STS_VTR1_CS_STS_Msk);
}

void ${ERB_INSTANCE_NAME}_VTR1PadMonStatusClr(VTR1_PAD_MON_STS statusBitMask)
{
    EC_REG_BANK_REGS->EC_REG_BANK_PD_MON_STS = statusBitMask;
}

VTR2_PAD_MON_STS ${ERB_INSTANCE_NAME}_VTR2PadMonStatusGet(void)
{
    return EC_REG_BANK_REGS->EC_REG_BANK_PD_MON_STS & (EC_REG_BANK_PD_MON_STS_VTR2_PD_STS_Msk | EC_REG_BANK_PD_MON_STS_VTR2_PU_STS_Msk | EC_REG_BANK_PD_MON_STS_VTR2_CS_STS_Msk);
}

void ${ERB_INSTANCE_NAME}_VTR2PadMonStatusClr(VTR2_PAD_MON_STS statusBitMask)
{
    EC_REG_BANK_REGS->EC_REG_BANK_PD_MON_STS = statusBitMask;
}

<#compress>
<#assign INT_HANDLER_NAME_PREFIX = "">
<#if ERB_PAD_MON_INTERRUPT_TYPE == "AGGREGATE">
<#assign INT_HANDLER_NAME_PREFIX = "_GRP">
</#if>
</#compress>

<#list 1..2 as n>
<#if .vars["ERB_PAD_MON_VTR" + n + "_PU_INT_EN"] == true || .vars["ERB_PAD_MON_VTR" + n + "_PD_INT_EN"] == true>

void ${ERB_INSTANCE_NAME}_VTR${n}_CallbackRegister( EC_REG_BANK_CALLBACK callback, uintptr_t context )
{
   ec_reg_bank[${n}].callback = callback;
   ec_reg_bank[${n}].context = context;
}

void VTR${n}_PAD_MON${INT_HANDLER_NAME_PREFIX}_InterruptHandler(void)
{
    <#if ERB_PAD_MON_INTERRUPT_TYPE == "AGGREGATE">
    if (ECIA_GIRQResultGet(ECIA_AGG_INT_SRC_VTR${n}_PAD_MON))
    <#else>
    if (ECIA_GIRQResultGet(ECIA_DIR_INT_SRC_VTR${n}_PAD_MON))
    </#if>
    {
        <#if ERB_PAD_MON_INTERRUPT_TYPE == "AGGREGATE">
        ECIA_GIRQSourceClear(ECIA_AGG_INT_SRC_VTR${n}_PAD_MON);
        <#else>
        ECIA_GIRQSourceClear(ECIA_DIR_INT_SRC_VTR${n}_PAD_MON);
        </#if>
        if (ec_reg_bank[${n}].callback != NULL)
        {
            ec_reg_bank[${n}].callback(ec_reg_bank[${n}].context);
        }
    }
}
</#if>
</#list>