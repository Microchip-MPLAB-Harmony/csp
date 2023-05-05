/*******************************************************************************
  32-bit Timer Peripheral Library Interface Source File

  Company
    Microchip Technology Inc.

  File Name
    plib_${TMR32_INSTANCE_NAME?lower_case}.c

  Summary
    ${TMR32_INSTANCE_NAME} peripheral library source file.

  Description
    This file implements the interface to the 32-bit timer peripheral library.  This
    library provides access to and control of the associated peripheral
    instance.

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
#include "plib_${TMR32_INSTANCE_NAME?lower_case}.h"
#include "peripheral/ecia/plib_ecia.h"

<#if TMR32_INTERRUPT_EN == true>
static TMR32_OBJECT ${TMR32_INSTANCE_NAME?lower_case}Obj;
</#if>

void ${TMR32_INSTANCE_NAME}_Initialize(void)
{
    TIMER32_${TMR32_INSTANCE_NUMBER}_REGS->TIMER32_CTRL = TIMER32_CTRL_PRESCALE(${TMR32_PRESCALE_VALUE}) <#if TMR32_AUTO_RESTART_EN == true> | TIMER32_CTRL_AU_RESTRT_Msk </#if> <#if TMR32_COUNT_DIR == "Up"> | TIMER32_CTRL_CNT_UP_Msk </#if> | TIMER32_CTRL_EN_Msk;
    
    <#if TMR32_AUTO_RESTART_EN == true>
    TIMER32_${TMR32_INSTANCE_NUMBER}_REGS->TIMER32_PRLD = ${TMR32_COUNT_INIT_VAL};
    </#if>
    
    TIMER32_${TMR32_INSTANCE_NUMBER}_REGS->TIMER32_CNT = ${TMR32_COUNT_INIT_VAL};
    
    <#if TMR32_INTERRUPT_EN == true>
    TIMER32_${TMR32_INSTANCE_NUMBER}_REGS->TIMER32_IEN = TIMER32_IEN_Msk;
    </#if>
}

void ${TMR32_INSTANCE_NAME}_PrescalerSet(uint16_t prescale_val)
{
    TIMER32_${TMR32_INSTANCE_NUMBER}_REGS->TIMER32_CTRL = (TIMER32_${TMR32_INSTANCE_NUMBER}_REGS->TIMER32_CTRL & ~TIMER32_CTRL_PRESCALE_Msk) | ((uint32_t)prescale_val << TIMER32_CTRL_PRESCALE_Pos);
}

uint32_t ${TMR32_INSTANCE_NAME}_FrequencyGet(void)
{
    uint32_t prescale = ((TIMER32_${TMR32_INSTANCE_NUMBER}_REGS->TIMER32_CTRL & TIMER32_CTRL_PRESCALE_Msk) >> TIMER32_CTRL_PRESCALE_Pos) + 1U;
    return (48000000U/prescale);
}

void ${TMR32_INSTANCE_NAME}_PreLoadCountSet(uint32_t count)
{
    TIMER32_${TMR32_INSTANCE_NUMBER}_REGS->TIMER32_PRLD = count;
}

uint32_t ${TMR32_INSTANCE_NAME}_PreLoadCountGet(void)
{
    return TIMER32_${TMR32_INSTANCE_NUMBER}_REGS->TIMER32_PRLD;
}

void ${TMR32_INSTANCE_NAME}_CounterSet(uint32_t count)
{
    TIMER32_${TMR32_INSTANCE_NUMBER}_REGS->TIMER32_CNT  = count;
}

uint32_t ${TMR32_INSTANCE_NAME}_CounterGet(void)
{
    return TIMER32_${TMR32_INSTANCE_NUMBER}_REGS->TIMER32_CNT;
}

void ${TMR32_INSTANCE_NAME}_Start(void)
{
    TIMER32_${TMR32_INSTANCE_NUMBER}_REGS->TIMER32_CTRL |= TIMER32_CTRL_STRT_Msk;
}

void ${TMR32_INSTANCE_NAME}_Stop(void)
{
    TIMER32_${TMR32_INSTANCE_NUMBER}_REGS->TIMER32_CTRL &= ~TIMER32_CTRL_STRT_Msk;
}

void ${TMR32_INSTANCE_NAME}_Reload(void)
{
    TIMER32_${TMR32_INSTANCE_NUMBER}_REGS->TIMER32_CTRL |= TIMER32_CTRL_RLD_Msk;
}

void ${TMR32_INSTANCE_NAME}_AutoReStartEnable(void)
{
    TIMER32_${TMR32_INSTANCE_NUMBER}_REGS->TIMER32_CTRL |= TIMER32_CTRL_AU_RESTRT_Msk;
}

void ${TMR32_INSTANCE_NAME}_AutoReStartDisable(void)
{
    TIMER32_${TMR32_INSTANCE_NUMBER}_REGS->TIMER32_CTRL &= ~TIMER32_CTRL_AU_RESTRT_Msk;
}

<#if TMR32_INTERRUPT_EN == true>
void TIMER32_${TMR32_INSTANCE_NUMBER}_CallbackRegister(TMR32_CALLBACK callback_fn, uintptr_t context )
{
    /* Save callback_fn and context in local memory */
    ${TMR32_INSTANCE_NAME?lower_case}Obj.callback_fn = callback_fn;
    ${TMR32_INSTANCE_NAME?lower_case}Obj.context = context;
}

<#if TMR32_INTERRUPT_TYPE == "AGGREGATE">
void ${TMR32_INSTANCE_NAME}_GRP_InterruptHandler(void)
{
    if (ECIA_GIRQResultGet(ECIA_AGG_INT_SRC_TIMER32_${TMR32_INSTANCE_NUMBER}) != 0U)
    {
        ECIA_GIRQSourceClear(ECIA_AGG_INT_SRC_TIMER32_${TMR32_INSTANCE_NUMBER});
<#else>
void ${TMR32_INSTANCE_NAME}_InterruptHandler(void)
{
    if (ECIA_GIRQResultGet(ECIA_DIR_INT_SRC_TIMER32_${TMR32_INSTANCE_NUMBER}) != 0U)
    {
        ECIA_GIRQSourceClear(ECIA_DIR_INT_SRC_TIMER32_${TMR32_INSTANCE_NUMBER});
</#if>
        uint32_t status = TIMER32_${TMR32_INSTANCE_NUMBER}_REGS->TIMER32_STS;
        
        /* Clear the interrupt status bit */
        TIMER32_${TMR32_INSTANCE_NUMBER}_REGS->TIMER32_STS = TIMER32_STS_EVT_INT_Msk;
        
        if (${TMR32_INSTANCE_NAME?lower_case}Obj.callback_fn != NULL)
        {
            ${TMR32_INSTANCE_NAME?lower_case}Obj.callback_fn(status, ${TMR32_INSTANCE_NAME?lower_case}Obj.context);
        }
    }
}
<#else>
bool ${TMR32_INSTANCE_NAME}_PeriodHasExpired(void)
{
    if ((TIMER32_${TMR32_INSTANCE_NUMBER}_REGS->TIMER32_STS & TIMER32_STS_EVT_INT_Msk) != 0U)
    {
        /* Clear the interrupt status bit */
        TIMER32_${TMR32_INSTANCE_NUMBER}_REGS->TIMER32_STS = TIMER32_STS_EVT_INT_Msk;
        return true;
    }
    else
    {
        return false;
    }
}
</#if>
