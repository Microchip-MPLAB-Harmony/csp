/*******************************************************************************
  WDT Peripheral Library

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${WDT_INSTANCE_NAME?lower_case}.c

  Summary:
    WDT Source File

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
#include "plib_${WDT_INSTANCE_NAME?lower_case}.h"

// *****************************************************************************
// *****************************************************************************
// Section: ${WDT_INSTANCE_NAME} Implementation
// *****************************************************************************
// *****************************************************************************
<#if WDT_ACTION == "Generate Interrupt">
static WDT_OBJECT wdt;
</#if>

<#assign wdt_ctrl = "">
<#if WDT_JTAG_STALL == true>
    <#if wdt_ctrl != "">
        <#assign wdt_ctrl = wdt_ctrl + " | WDT_CTRL_JTAG_STL_Msk">
    <#else>
        <#assign wdt_ctrl = "WDT_CTRL_JTAG_STL_Msk">
    </#if>
</#if>

<#if WDT_WEEK_TIMER_STALL == true>
    <#if wdt_ctrl != "">
        <#assign wdt_ctrl = wdt_ctrl + " | WDT_CTRL_WK_TMR_STL_Msk">
    <#else>
        <#assign wdt_ctrl = "WDT_CTRL_WK_TMR_STL_Msk">
    </#if>
</#if>

<#if WDT_HIBERNATION_TIMER_STALL == true>
    <#if wdt_ctrl != "">
        <#assign wdt_ctrl = wdt_ctrl + " | WDT_CTRL_HIB_TMR0_STL_Msk">
    <#else>
        <#assign wdt_ctrl = "WDT_CTRL_HIB_TMR0_STL_Msk">
    </#if>
</#if>

<#if WDT_ACTION == "Generate Interrupt">
    <#if wdt_ctrl != "">
        <#assign wdt_ctrl = wdt_ctrl + " | WDT_CTRL_WDT_RST_Msk">
    <#else>
        <#assign wdt_ctrl = "WDT_CTRL_WDT_RST_Msk">
    </#if>
</#if>

void ${WDT_INSTANCE_NAME}_Initialize( void )
{
    WDT_REGS->WDT_LOAD = ${WDT_TIMEOUT_PERIOD};

    <#if wdt_ctrl?has_content>
    WDT_REGS->WDT_CTRL = ${wdt_ctrl};
    </#if>

    <#if WDT_ACTION == "Generate Interrupt">
    WDT_REGS->WDT_IEN = WDT_IEN_Msk;
    </#if>

}
void ${WDT_INSTANCE_NAME}_Enable(void)
{
    WDT_REGS->WDT_CTRL |= WDT_CTRL_WDT_EN_Msk;
}

void ${WDT_INSTANCE_NAME}_Disable(void)
{
    WDT_REGS->WDT_CTRL &= ~WDT_CTRL_WDT_EN_Msk;
}

bool ${WDT_INSTANCE_NAME}_IsEnabled( void )
{
    return ((WDT_REGS->WDT_CTRL & WDT_CTRL_WDT_EN_Msk) != 0U);
}

void ${WDT_INSTANCE_NAME}_Clear(void)
{
    /* Clear WDT timer */
    WDT_REGS->WDT_KICK = 0;
}

uint16_t ${WDT_INSTANCE_NAME}_CountGet(void)
{
    /* Return WDT timer counter */
    return WDT_REGS->WDT_CNT;
}

bool ${WDT_INSTANCE_NAME}_isPowerFailWDTEventSet(void)
{
    bool check = false;
    if ((VTR_REG_BANK_REGS->VTR_REG_BANK_PFRS & VTR_REG_BANK_PFRS_WDT_EVT_Msk) != 0U)
    {
        check = true;
    }
    
    return check;
    
}

void ${WDT_INSTANCE_NAME}_PowerFailWDTEventClear(void)
{
    if ((VTR_REG_BANK_REGS->VTR_REG_BANK_PFRS & VTR_REG_BANK_PFRS_WDT_EVT_Msk) != 0U)
    {
        /* Write 1 to clear this bit */
        VTR_REG_BANK_REGS->VTR_REG_BANK_PFRS |= VTR_REG_BANK_PFRS_WDT_EVT_Msk;
    }
}

void ${WDT_INSTANCE_NAME}_PeriodLoad(uint16_t period)
{
    WDT_REGS->WDT_LOAD = period;
}

<#if WDT_ACTION == "Generate Interrupt">

void ${WDT_INSTANCE_NAME}_TimeoutActionSet(WDT_TIMEOUT_ACTION action)
{
    WDT_REGS->WDT_CTRL = (uint16_t)((WDT_REGS->WDT_CTRL & ~WDT_CTRL_WDT_RST_Msk) | ((uint16_t)action << WDT_CTRL_WDT_RST_Pos));
}

void ${WDT_INSTANCE_NAME}_CallbackRegister( WDT_CALLBACK callback, uintptr_t context )
{
   wdt.callback = callback;
   wdt.context = context;
}

void ${WDT_TMR_NVIC_INTERRUPT_NAME}_InterruptHandler( void )
{
    <#if WDT_TMR_INTERRUPT_TYPE == "AGGREGATE">
    if (ECIA_GIRQResultGet(ECIA_AGG_INT_SRC_WDT) != 0U)
    <#else>
    if (ECIA_GIRQResultGet(ECIA_DIR_INT_SRC_WDT) != 0U)
    </#if>
    {
        WDT_REGS->WDT_STS = WDT_STS_WDT_EV_IRQ_Msk;

        <#if WDT_TMR_INTERRUPT_TYPE == "AGGREGATE">
        ECIA_GIRQSourceClear(ECIA_AGG_INT_SRC_WDT);
        <#else>
        ECIA_GIRQSourceClear(ECIA_DIR_INT_SRC_WDT);
        </#if>

        if(wdt.callback != NULL)
        {
            wdt.callback(wdt.context);
        }
    }
}
</#if>