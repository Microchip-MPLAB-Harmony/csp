/*******************************************************************************
  Dual watchdog timer (DWDT) PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_dwdt.c

  Summary
    Source for DWDT peripheral library interface Implementation.

  Description
    This file defines the interface to the DWDT peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

  Remarks:
    None.

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
#include <stddef.h>
#include "device.h"
<#if CoreSysIntFile == true>
#include "interrupts.h"
</#if>
#include "plib_dwdt.h"

typedef struct
{
    DWDT_CALLBACK pCallback;
    uintptr_t context;
}dwdtCallback_t;

<#list 0..1 as i>
<#compress>
<#assign WDT_MODE_VAL ="">
<#if !.vars["WDT" + i + "_ENABLE"]>
    <#assign WDT_MODE_VAL =WDT_MODE_VAL + "DWDT_WDT" + i + "_MR_WDDIS_Msk | ">
</#if>
<#if .vars["WDT" + i + "_DBG1HLT"]>
    <#assign WDT_MODE_VAL =WDT_MODE_VAL + "DWDT_WDT" + i + "_MR_WDDBG1HLT_Msk | ">
</#if>
<#if .vars["WDT" + i + "_DBG0HLT"]>
    <#assign WDT_MODE_VAL =WDT_MODE_VAL + "DWDT_WDT" + i + "_MR_WDDBG0HLT_Msk | ">
</#if>
<#if .vars["WDT" + i + "_IDLEHLT"]>
    <#assign WDT_MODE_VAL =WDT_MODE_VAL + "DWDT_WDT" + i + "_MR_WDIDLEHLT_Msk | ">
</#if>
<#if .vars["WDT" + i + "_NRSTDIS"]>
    <#assign WDT_MODE_VAL =WDT_MODE_VAL + "DWDT_WDT" + i + "_MR_WDNRSTDIS_Msk | ">
</#if>
<#if .vars["WDT" + i + "_EVENT"] == "Reset">
    <#assign WDT_MODE_VAL =WDT_MODE_VAL + "DWDT_WDT" + i + "_MR_PERIODRST_Msk | ">
</#if>
<#if .vars["WDT" + i + "_RPTH_ENABLE"] == "Reset">
    <#assign WDT_MODE_VAL =WDT_MODE_VAL + "DWDT_WDT" + i + "_MR_RPTHRST_Msk | ">
</#if>
<#assign WDT_INTERRUPT_EN ="">
<#assign WDT_INTERRUPT_DIS = "">
<#if .vars["WDT" + i + "_EVENT"] == "Interrupt">
    <#assign WDT_INTERRUPT_EN = WDT_INTERRUPT_EN + "DWDT_WDT" + i + "_IER_PERINT_Msk | ">
<#else>
    <#assign WDT_INTERRUPT_DIS = WDT_INTERRUPT_DIS + "DWDT_WDT" + i + "_IDR_PERINT_Msk | ">
</#if>
<#if .vars["WDT" + i + "_LEVEL_ENABLE"]>
    <#assign WDT_INTERRUPT_EN = WDT_INTERRUPT_EN + "DWDT_WDT" + i + "_IER_LVLINT_Msk | ">
<#else>
    <#assign WDT_INTERRUPT_DIS = WDT_INTERRUPT_DIS + "DWDT_WDT" + i + "_IDR_LVLINT_Msk | ">
</#if>
<#if .vars["WDT" + i + "_RPTH_ENABLE"] == "Interrupt">
    <#assign WDT_INTERRUPT_EN = WDT_INTERRUPT_EN + "DWDT_WDT" + i + "_IER_RPTHINT_Msk | ">
<#else>
    <#assign WDT_INTERRUPT_DIS = WDT_INTERRUPT_DIS + "DWDT_WDT" + i + "_IDR_RPTHINT_Msk | ">
</#if>
<#if .vars["WDT" + i + "_RLDERR_ENABLE"]>
    <#assign WDT_INTERRUPT_EN = WDT_INTERRUPT_EN + "DWDT_WDT" + i + "_IER_RLDERR_Msk | ">
<#else>
    <#assign WDT_INTERRUPT_DIS = WDT_INTERRUPT_DIS + "DWDT_WDT" + i + "_IDR_RLDERR_Msk | ">
</#if>
<#if  (i == 0) && WDT0_W1PERINT_ENABLE>
    <#assign WDT_INTERRUPT_EN = WDT_INTERRUPT_EN + "DWDT_WDT0_IER_W1PERINT_Msk | ">
<#else>
    <#assign WDT_INTERRUPT_DIS = WDT_INTERRUPT_DIS + "DWDT_WDT0_IDR_W1PERINT_Msk | ">
</#if>
<#if  (i == 0) && WDT0_W1RPTHINT_ENABLE>
    <#assign WDT_INTERRUPT_EN = WDT_INTERRUPT_EN + "DWDT_WDT0_IER_W1RPTHINT_Msk | ">
<#else>
    <#assign WDT_INTERRUPT_DIS = WDT_INTERRUPT_DIS + "DWDT_WDT0_IDR_W1RPTHINT_Msk | ">
</#if>
<#assign WDT_WL_VAL = "">
<#if .vars["WDT" + i + "_ENABLE"]>
    <#assign WDT_WL_VAL = WDT_WL_VAL + "DWDT_WDT" + i+ "_WL_PERIOD(" + .vars["WDT" + i +"_PERIOD"] + "U)">
</#if>
<#if .vars["WDT" + i + "_RPTH_ENABLE"] != "Disable">
    <#assign WDT_WL_VAL = WDT_WL_VAL + " | DWDT_WDT" + i + "_WL_RPTH(" + .vars["WDT" + i +"_RPTH"] + "U)">
</#if>
<#assign WDT_IL_VAL = "DWDT_WDT" + i + "_IL_PRESC_" + .vars["WDT" + i +"_PRESCALER"]>
<#if .vars["WDT" + i + "_LEVEL_ENABLE"]>
    <#assign WDT_IL_VAL = WDT_IL_VAL + " | DWDT_WDT" + i + "_IL_LVLTH(" + .vars["WDT" + i +"_LEVEL"] + "U)">
</#if>
</#compress>
<#if .vars["WDT" + i + "_INTERRUPT_ENABLE"]>

static dwdtCallback_t dwdt${i}CallbackObj;
</#if>


static void WDT${i}_Initialize(void)
{
<#if .vars["WDT" + i + "_ENABLE"]>
    /* Configure Period ${(.vars["WDT" + i + "_RPTH_ENABLE"] != "Disable")?string("and repeat threshold", "")} */
    DWDT_REGS->DWDT_WDT${i}_WL = ${WDT_WL_VAL};

    /* Configure prescaler ${.vars["WDT" + i + "_LEVEL_ENABLE"]?string("and level threshold", "")} */
    DWDT_REGS->DWDT_WDT${i}_IL = ${WDT_IL_VAL};
    <#if WDT_MODE_VAL?has_content>

        <#lt>    /* Configure WDT${i} modes */
        <#lt>    DWDT_REGS->DWDT_WDT${i}_MR = ${WDT_MODE_VAL?remove_ending(" | ")};
    </#if>
    <#if .vars["WDT" + i + "_LOCK_CONFIG"]>

        <#lt>    /* Lock WDT${i} configurations */
        <#lt>    DWDT_REGS->DWDT_WDT${i}_CR = DWDT_WDT${i}_CR_KEY_PASSWD | DWDT_WDT${i}_CR_LOCKMR_Msk;
    </#if>
    <#if .vars["WDT" + i + "_INTERRUPT_ENABLE"]>
        <#if WDT_INTERRUPT_EN?has_content>

            <#lt>    /*Enable configured interrupts */
            <#lt>    DWDT_REGS->DWDT_WDT${i}_IER = ${WDT_INTERRUPT_EN?remove_ending(" | ")};
        </#if>
        <#if WDT_INTERRUPT_DIS?has_content>

            <#lt>    /*Disable interrupts that are not enabled */
            <#lt>    DWDT_REGS->DWDT_WDT${i}_IDR = ${WDT_INTERRUPT_DIS?remove_ending(" | ")};
        </#if>
    <#else>

        <#lt>    /* Disable all interrupts */
        <#lt>    DWDT_REGS->DWDT_WDT${i}_IDR = DWDT_WDT${i}_IDR_Msk;
    </#if>
    <#if (i == 1) && ((WDT1_PERIOD_MAX lt 4095) || (WDT1_PERIOD_MIN gt 0))>

        <#lt>    /* Set wdt1 period limits */
        <#lt>    DWDT_REGS->DWDT_WDT1_PLIM  = DWDT_WDT1_PLIM_PERMAX(${WDT1_PERIOD_MAX}U) | DWDT_WDT1_PLIM_PERMIN(${WDT1_PERIOD_MIN}U);
    </#if>
    <#if (i == 1) && ((WDT1_RPTH_MAX lt 4095) || (WDT1_RPTH_MIN gt 0))>

        <#lt>    /* Set wdt1 repeat threshold limits */
        <#lt>    DWDT_REGS->DWDT_WDT1_RLIM  = DWDT_WDT1_RLIM_RPTHMAX(${WDT1_RPTH_MAX}U) | DWDT_WDT1_RLIM_RPTHMIN(${WDT1_RPTH_MIN}U);
    </#if>
    <#if (i == 1) && ((WDT1_LEVEL_MAX lt 4095) || (WDT1_LEVEL_MIN gt 0))>

        <#lt>    /* Set wdt1 level threshold limits */
        <#lt>    DWDT_REGS->DWDT_WDT1_LVLLIM  = DWDT_WDT1_LVLLIM_LVLMAX(${WDT1_LEVEL_MAX}U) | DWDT_WDT1_LVLLIM_LVLMIN(${WDT1_LEVEL_MIN}U);
    </#if>
<#else>

        <#lt>    /* Disable WDT${i} */
        <#lt>    DWDT_REGS->DWDT_WDT${i}_MR |= DWDT_WDT${i}_MR_WDDIS_Msk;
</#if>
}
<#if .vars["WDT" + i + "_ENABLE"]>


void DWDT_WDT${i}_Clear(void)
{
    /* Restart WDT${i} */
    DWDT_REGS->DWDT_WDT${i}_CR = DWDT_WDT${i}_CR_KEY_PASSWD | DWDT_WDT${i}_CR_WDRSTT_Msk;
}
<#if !.vars["WDT" + i + "_LOCK_CONFIG"]>


void DWDT_WDT${i}_Disable(void)
{
    /* Disable WDT${i} */
    DWDT_REGS->DWDT_WDT${i}_MR |= DWDT_WDT${i}_MR_WDDIS_Msk;
}
</#if>
<#if .vars["WDT" + i + "_INTERRUPT_ENABLE"]>


void DWDT_WDT${i}_RegisterCallback(DWDT_CALLBACK pCallback, uintptr_t context)
{
    dwdt${i}CallbackObj.pCallback = pCallback;
    dwdt${i}CallbackObj.context = context;
}


void DWDT${i}_InterruptHandler(void)
{
    uint32_t interruptStatus = DWDT_REGS->DWDT_WDT${i}_ISR;
    if (dwdt${i}CallbackObj.pCallback != NULL)
    {
        dwdt${i}CallbackObj.pCallback(interruptStatus, dwdt${i}CallbackObj.context);
    }
}
</#if>
</#if>
</#list>


void DWDT_Initialize(void)
{
    WDT0_Initialize();
    WDT1_Initialize();
}