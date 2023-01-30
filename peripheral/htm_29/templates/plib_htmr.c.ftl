/*******************************************************************************
  Hibernation Timer Peripheral Library Interface Source File

  Company
    Microchip Technology Inc.

  File Name
    plib_${HTM_TMR_INSTANCE_NAME?lower_case}.c

  Summary
    ${HTM_TMR_INSTANCE_NAME} peripheral library source file.

  Description
    This file implements the interface to the Hibernation Timer peripheral library.
    This library provides access to and control of the associated peripheral
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
#include "plib_${HTM_TMR_INSTANCE_NAME?lower_case}.h"
#include "peripheral/ecia/plib_ecia.h"

static HTM_TMR_OBJECT ${HTM_TMR_INSTANCE_NAME?lower_case}Obj;

void ${HTM_TMR_INSTANCE_NAME}_Initialize(void)
{
    <#if HTM_TMR_RESOLUTION == "8_HZ">
    ${HTM_TMR_INSTANCE_NAME}_REGS->HTM_CTRL = HTM_CTRL_CTRL_Msk;
    </#if>

    ${HTM_TMR_INSTANCE_NAME}_REGS->HTM_PRLD = ${HTM_TMR_PRELOAD_VALUE};
}


void ${HTM_TMR_INSTANCE_NAME}_PeriodSet(uint16_t preload_val)
{
    /* Writing non-zero value resets and starts the hibernation timer */
    ${HTM_TMR_INSTANCE_NAME}_REGS->HTM_PRLD = preload_val;
}

uint16_t ${HTM_TMR_INSTANCE_NAME}_PeriodGet(void)
{
    return ${HTM_TMR_INSTANCE_NAME}_REGS->HTM_PRLD;
}

uint16_t ${HTM_TMR_INSTANCE_NAME}_CountGet (void)
{
    return ${HTM_TMR_INSTANCE_NAME}_REGS->HTM_CNT;
}

void ${HTM_TMR_INSTANCE_NAME}_ResolutionSet(HTM_TMR_RESOLUTION resolution)
{
    ${HTM_TMR_INSTANCE_NAME}_REGS->HTM_CTRL = (resolution << HTM_CTRL_CTRL_Pos);
}

void ${HTM_TMR_INSTANCE_NAME}_CallbackRegister( HTM_TMR_CALLBACK callback_fn, uintptr_t context )
{
    ${HTM_TMR_INSTANCE_NAME?lower_case}Obj.callback_fn = callback_fn;
    ${HTM_TMR_INSTANCE_NAME?lower_case}Obj.context = context;
}
<#assign HTMR_AGG_INT_SRC = "ECIA_AGG_INT_SRC_HTMR" + HTM_TMR_INSTANCE_NUM>
<#assign HTMR_DIR_INT_SRC = "ECIA_DIR_INT_SRC_HTMR" + HTM_TMR_INSTANCE_NUM>

void ${HTM_TMR_NVIC_INTERRUPT_NAME}_InterruptHandler(void)
{
    <#if HTM_TMR_INTERRUPT_TYPE == "AGGREGATE">
    if (ECIA_GIRQResultGet(${HTMR_AGG_INT_SRC}))
    <#else>
    if (ECIA_GIRQResultGet(${HTMR_DIR_INT_SRC}))
    </#if>
    {
        <#if HTM_TMR_INTERRUPT_TYPE == "AGGREGATE">
        ECIA_GIRQSourceClear(${HTMR_AGG_INT_SRC});
        <#else>
        ECIA_GIRQSourceClear(${HTMR_DIR_INT_SRC});
        </#if>

        if(${HTM_TMR_INSTANCE_NAME?lower_case}Obj.callback_fn != NULL)
        {
            ${HTM_TMR_INSTANCE_NAME?lower_case}Obj.callback_fn(${HTM_TMR_INSTANCE_NAME?lower_case}Obj.context);
        }
    }
}
