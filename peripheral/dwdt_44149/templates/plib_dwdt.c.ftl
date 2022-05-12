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
* Copyright (C) 2021 Microchip Technology Inc. and its subsidiaries.
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
<#compress>
<#assign PS_MODE_VAL ="">
<#if !DWDT_PS_ENABLE>
<#assign PS_MODE_VAL = PS_MODE_VAL + "DWDT_PS_WDT_MR_WDDIS_Msk | ">
</#if>
<#if DWDT_PS_DEBUG_HALT>
<#assign PS_MODE_VAL = PS_MODE_VAL + "DWDT_PS_WDT_MR_WDDBGHLT_Msk | ">
</#if>
<#if DWDT_PS_IDLE_HALT>
<#assign PS_MODE_VAL = PS_MODE_VAL + "DWDT_PS_WDT_MR_WDIDLEHLT_Msk | ">
</#if>
<#if DWDT_PS_ENABLE && (DWDT_PS_EVENT == "Reset")>
<#assign PS_MODE_VAL = PS_MODE_VAL + "DWDT_PS_WDT_MR_PERIODRST_Msk | ">
</#if>
<#if DWDT_PS_REPEAT_THRESHOLD_ENABLE == "Reset">
<#assign PS_MODE_VAL = PS_MODE_VAL + "DWDT_PS_WDT_MR_RPTHRST_Msk | ">
</#if>
<#assign PS_INTERRUPT = "">
<#assign PS_INTERRUPT_DIS = "">
<#if DWDT_PS_EVENT == "Interrupt">
<#assign PS_INTERRUPT = PS_INTERRUPT + "DWDT_PS_WDT_IER_PERINT_Msk | ">
<#else>
<#assign PS_INTERRUPT_DIS = PS_INTERRUPT_DIS + "DWDT_PS_WDT_IDR_PERINT_Msk | ">
</#if>
<#if DWDT_PS_REPEAT_THRESHOLD_ENABLE == "Interrupt">
<#assign PS_INTERRUPT = PS_INTERRUPT + "DWDT_PS_WDT_IER_RPTHINT_Msk | ">
<#else>
<#assign PS_INTERRUPT_DIS = PS_INTERRUPT_DIS + "DWDT_PS_WDT_IDR_RPTHINT_Msk | ">
</#if>
<#if DWDT_PS_LEVEL_ENABLE>
<#assign PS_INTERRUPT = PS_INTERRUPT + "DWDT_PS_WDT_IER_LVLINT_Msk | ">
<#else>
<#assign PS_INTERRUPT_DIS = PS_INTERRUPT_DIS + "DWDT_PS_WDT_IDR_LVLINT_Msk | ">
</#if>
<#if DWDT_PS_NS_PERIOD_INTERRUPT_ENABLE>
<#assign PS_INTERRUPT = PS_INTERRUPT + "DWDT_PS_WDT_IER_NSPERINT_Msk | ">
<#else>
<#assign PS_INTERRUPT_DIS = PS_INTERRUPT_DIS + "DWDT_PS_WDT_IDR_NSPERINT_Msk | ">
</#if>
<#if DWDT_PS_NS_REPEAT_INTERRUPT_ENABLE>
<#assign PS_INTERRUPT = PS_INTERRUPT + "DWDT_PS_WDT_IER_NSRPTHINT_Msk | ">
<#else>
<#assign PS_INTERRUPT_DIS = PS_INTERRUPT_DIS + "DWDT_PS_WDT_IDR_NSRPTHINT_Msk | ">
</#if>
<#if (DWDT_PS_EVENT == "Interrupt") ||  (DWDT_PS_REPEAT_THRESHOLD_ENABLE == "Interrupt") || DWDT_PS_LEVEL_ENABLE || DWDT_PS_NS_PERIOD_INTERRUPT_ENABLE || DWDT_PS_NS_REPEAT_INTERRUPT_ENABLE>
<#assign DWDT_PS_INTERRUPT_ENABLE = true>
<#else>
<#assign DWDT_PS_INTERRUPT_ENABLE = false>
</#if>
<#assign NS_MODE_VAL = "">
<#if !DWDT_NS_ENABLE>
<#assign NS_MODE_VAL = "DWDT_NS_WDT_MR_WDDIS_Msk | ">
</#if>
<#if DWDT_NS_DEBUG_HALT>
<#assign NS_MODE_VAL = "DWDT_NS_WDT_MR_WDDBGHLT_Msk | ">
</#if>
<#if DWDT_NS_IDLE_HALT>
<#assign NS_MODE_VAL = "DWDT_NS_WDT_MR_WDIDLEHLT_Msk | ">
</#if>
<#if DWDT_NS_RPTHALM>
<#assign NS_MODE_VAL = "DWDT_NS_WDT_MR_RPTHALM_Msk | ">
</#if>
<#assign NS_INTERRUPT = "">
<#assign NS_INTERRUPT_DIS = "">
<#if DWDT_NS_PERIOD_ENABLE>
<#assign NS_INTERRUPT = NS_INTERRUPT + "DWDT_NS_WDT_IER_PERINT_Msk | ">
<#else>
<#assign NS_INTERRUPT_DIS = NS_INTERRUPT_DIS + "DWDT_NS_WDT_IDR_PERINT_Msk | ">
</#if>
<#if DWDT_NS_REPEAT_THRESHOLD_ENABLE>
<#assign NS_INTERRUPT = NS_INTERRUPT + "DWDT_NS_WDT_IER_RPTHINT_Msk | ">
<#else>
<#assign NS_INTERRUPT_DIS = NS_INTERRUPT_DIS + "DWDT_NS_WDT_IDR_RPTHINT_Msk | ">
</#if>
<#if DWDT_NS_LEVEL_ENABLE>
<#assign NS_INTERRUPT = NS_INTERRUPT + "DWDT_NS_WDT_IER_LVLINT_Msk | ">
<#else>
<#assign NS_INTERRUPT_DIS = NS_INTERRUPT_DIS + "DWDT_NS_WDT_IDR_LVLINT_Msk | ">
</#if>
<#if DWDT_NS_PERIOD_ENABLE || DWDT_NS_REPEAT_THRESHOLD_ENABLE || DWDT_NS_LEVEL_ENABLE>
<#assign DWDT_NS_INTERRUPT_ENABLE = true>
<#else>
<#assign DWDT_NS_INTERRUPT_ENABLE = false>
</#if>
</#compress>

#include <stddef.h>
#include "device.h"
<#if CoreSysIntFile == true>
#include "interrupts.h"
</#if>
#include "plib_dwdt.h"
<#if DWDT_PS_INTERRUPT_ENABLE || DWDT_NS_INTERRUPT_ENABLE>


typedef struct
{
    DWDT_CALLBACK pCallback;
    uintptr_t context;
}dwdtCallbackObjType;
<#if DWDT_PS_INTERRUPT_ENABLE>

static dwdtCallbackObjType dwdtPSCallbackObj;
</#if>
<#if DWDT_NS_INTERRUPT_ENABLE>

static dwdtCallbackObjType dwdtNSCallbackObj;
</#if>
</#if>


static void DWDT_PS_Initialize(void)
{
<#if DWDT_PS_ENABLE>

    /*Window level */
    DWDT_REGS->DWDT_PS_WDT_WL = DWDT_PS_WDT_WL_PERIOD(${DWDT_PS_PERIOD}U)${(DWDT_PS_REPEAT_THRESHOLD_ENABLE != "Disable")?string(" | DWDT_PS_WDT_WL_RPTH(${DWDT_PS_REPEAT_THRESHOLD}U)","")};
</#if>
<#if DWDT_PS_LEVEL_ENABLE>

    /* Interrupt Level */
    DWDT_REGS->DWDT_NS_WDT_IL = DWDT_PS_WDT_IL_LVLTH(${DWDT_PS_LEVEL}U);
</#if>

    /* Configure PS watchdog mode */
    uint32_t regVal = DWDT_REGS->DWDT_PS_WDT_MR & ~(DWDT_PS_WDT_MR_Msk);
<#if PS_MODE_VAL?has_content>

    regVal |= (${PS_MODE_VAL?remove_ending(" | ")});
</#if>

    DWDT_REGS->DWDT_PS_WDT_MR = regVal;
<#if DWDT_PS_LOCK_CONFIG>

    /* Lock PS WDT configurations */
    DWDT_REGS->DWDT_PS_WDT_CR = DWDT_PS_WDT_CR_KEY_PASSWD | DWDT_PS_WDT_CR_LOCKMR_Msk;
</#if>
<#if PS_INTERRUPT?has_content>

    /* Enable selected PS WDT interrupts */
    DWDT_REGS->DWDT_PS_WDT_IER = (${PS_INTERRUPT?remove_ending(" | ")});
</#if>
<#if PS_INTERRUPT_DIS?has_content>

    /* Disable PS WDT interrupts */
    DWDT_REGS->DWDT_PS_WDT_IDR = (${PS_INTERRUPT_DIS?remove_ending(" | ")});
</#if>
<#if (DWDT_PS_NS_LEVEL_MAX < 4095) || (DWDT_PS_NS_LEVEL_MIN > 0)>

    /* Configure level limit for NS WDT */
    DWDT_REGS->DWDT_NS_WDT_LVLLIM = DWDT_NS_WDT_LVLLIM_LVLMAX(${DWDT_PS_NS_LEVEL_MAX}U) | DWDT_NS_WDT_LVLLIM_LVLMIN(${DWDT_PS_NS_LEVEL_MIN}U);
</#if>
<#if (DWDT_PS_NS_REPEAT_MAX < 4095) || (DWDT_PS_NS_REPEAT_MIN > 0)>

    /* Configure repeat threshold limit for NS WDT */
    DWDT_REGS->DWDT_NS_WDT_RLIM = DWDT_NS_WDT_RLIM_RPTHMAX(${DWDT_PS_NS_REPEAT_MAX}U) | DWDT_NS_WDT_RLIM_RPTHMIN(${DWDT_PS_NS_REPEAT_MIN}U);
</#if>
<#if (DWDT_PS_NS_PERIOD_MAX < 4095) || (DWDT_PS_NS_PERIOD_MIN > 0)>

    /* Configure period limit for NS WDT */
    DWDT_REGS->DWDT_NS_WDT_PLIM = DWDT_NS_WDT_PLIM_PERMAX(${DWDT_PS_NS_PERIOD_MAX}U) | DWDT_NS_WDT_PLIM_PERMIN(${DWDT_PS_NS_PERIOD_MIN}U);
</#if>
}


static void DWDT_NS_Initialize(void)
{
    /* Configure PS watchdog mode */
    uint32_t regVal = DWDT_REGS->DWDT_NS_WDT_MR & ~(DWDT_NS_WDT_MR_Msk);
<#if NS_MODE_VAL?has_content>

    regVal |= (${NS_MODE_VAL?remove_ending(" | ")});
</#if>

    DWDT_REGS->DWDT_NS_WDT_MR = regVal;
<#if DWDT_NS_ENABLE>

    /* Window level */
    DWDT_REGS->DWDT_NS_WDT_WL = DWDT_NS_WDT_WL_PERIOD(${DWDT_NS_PERIOD}U)${(DWDT_NS_REPEAT_THRESHOLD_ENABLE)?string(" | DWDT_NS_WDT_WL_RPTH(${DWDT_NS_REPEAT_THRESHOLD}U)","")};
</#if>
<#if DWDT_NS_LEVEL_ENABLE>

    /* Interrupt Level threshold */
    DWDT_REGS->DWDT_NS_WDT_IL = DWDT_NS_WDT_IL_LVLTH(${DWDT_NS_LEVEL}U);
</#if>
<#if DWDT_NS_LOCK_CONFIG>

    /* Lock NS WDT configurations */
    DWDT_REGS->DWDT_NS_WDT_CR = DWDT_NS_WDT_CR_KEY_PASSWD | DWDT_NS_WDT_CR_LOCKMR_Msk;
</#if>
<#if NS_INTERRUPT?has_content>

    /* Enable selected NS WDT interrupts*/
    DWDT_REGS->DWDT_NS_WDT_IER = (${NS_INTERRUPT?remove_ending(" | ")});
</#if>
<#if NS_INTERRUPT_DIS?has_content>

    /* Disable NS WDT interrupts */
    DWDT_REGS->DWDT_NS_WDT_IDR = (${NS_INTERRUPT_DIS?remove_ending(" | ")});
</#if>
}


void DWDT_Initialize(void)
{
    DWDT_PS_Initialize();
    DWDT_NS_Initialize();
}
<#if DWDT_PS_ENABLE>


void DWDT_PS_Clear(void)
{
    /* Restart PS watchdog */
    DWDT_REGS->DWDT_PS_WDT_CR = (DWDT_PS_WDT_CR_KEY_PASSWD | DWDT_PS_WDT_CR_WDRSTT_Msk);
}
<#if !DWDT_PS_LOCK_CONFIG>


void DWDT_PS_Disable(void)
{
    /* Disable PS watchdog */
    DWDT_REGS->DWDT_PS_WDT_MR |= DWDT_PS_WDT_MR_WDDIS_Msk;
}
</#if>
</#if>
<#if DWDT_PS_INTERRUPT_ENABLE>


void DWDT_PS_CallbackRegister(DWDT_CALLBACK pCallback, uintptr_t context)
{
    dwdtPSCallbackObj.pCallback = pCallback;
    dwdtPSCallbackObj.context = context;
}


void DWDT_SW_InterruptHandler(void)
{
    uint32_t interruptStatus = DWDT_REGS->DWDT_PS_WDT_ISR;
    if (dwdtPSCallbackObj.pCallback != NULL)
    {
        dwdtPSCallbackObj.pCallback(interruptStatus, dwdtPSCallbackObj.context);
    }
}
</#if>
<#if DWDT_NS_ENABLE>


void DWDT_NS_Clear(void)
{
    /* Restart NS watchdog */
    DWDT_REGS->DWDT_NS_WDT_CR = (DWDT_NS_WDT_CR_KEY_PASSWD | DWDT_NS_WDT_CR_WDRSTT_Msk);
}
<#if !DWDT_NS_LOCK_CONFIG>


void DWDT_NS_Disable(void)
{
    /* Disable NS watchdog */
    DWDT_REGS->DWDT_NS_WDT_MR |= DWDT_NS_WDT_MR_WDDIS_Msk;
}
</#if>
</#if>
<#if DWDT_NS_INTERRUPT_ENABLE>


void DWDT_NS_CallbackRegister(DWDT_CALLBACK pCallback, uintptr_t context)
{
    dwdtNSCallbackObj.pCallback = pCallback;
    dwdtNSCallbackObj.context = context;
}


void DWDT_NSW_InterruptHandler(void)
{
    uint32_t interruptStatus = DWDT_REGS->DWDT_NS_WDT_ISR;
    if (dwdtNSCallbackObj.pCallback != NULL)
    {
        dwdtNSCallbackObj.pCallback(interruptStatus, dwdtNSCallbackObj.context);
    }
}
</#if>