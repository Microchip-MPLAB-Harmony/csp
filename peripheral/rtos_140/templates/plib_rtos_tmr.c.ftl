/*******************************************************************************
  RTOS Timer Peripheral Library Interface Source File

  Company
    Microchip Technology Inc.

  File Name
    plib_${RTOS_TMR_INSTANCE_NAME?lower_case}.c

  Summary
    ${RTOS_TMR_INSTANCE_NAME} peripheral library source file.

  Description
    This file implements the interface to the RTOS Timer peripheral library.  This
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
#include "plib_${RTOS_TMR_INSTANCE_NAME?lower_case}_tmr.h"
#include "peripheral/ecia/plib_ecia.h"

static RTOS_TMR_OBJECT ${RTOS_TMR_INSTANCE_NAME?lower_case}TimerObj;

void ${RTOS_TMR_INSTANCE_NAME}Timer_Initialize(void)
{
    /* Disable RTOS timer. All registers are reset to the default state. */
    ${RTOS_TMR_INSTANCE_NAME}_REGS->RTOS_CTRL &= ~RTOS_CTRL_BLK_EN_Msk;
    
    ${RTOS_TMR_INSTANCE_NAME}_REGS->RTOS_PRLD = ${RTOS_TMR_PRELOAD_VALUE};
    
    /* Enable timer module. Set Auto-reload and hardware halt values based on user settings. Do not start the timer. */
    ${RTOS_TMR_INSTANCE_NAME}_REGS->RTOS_CTRL = RTOS_CTRL_BLK_EN_Msk <#if RTOS_TMR_AUTO_RELOAD_ENABLE == true> | RTOS_CTRL_AU_RELOAD_Msk </#if> <#if RTOS_TMR_HW_HALT_ENABLE == true> | RTOS_CTRL_EXT_HW_HALT_EN_Msk </#if>;
}


void ${RTOS_TMR_INSTANCE_NAME}Timer_Start(void)
{
    /* Loads pre-load register to the counter and starts the timer */
    ${RTOS_TMR_INSTANCE_NAME}_REGS->RTOS_CTRL |= RTOS_CTRL_TMR_STRT_Msk;
}

void ${RTOS_TMR_INSTANCE_NAME}Timer_Stop (void)
{
    /* Stops the timer, clears the counter to 0. Does not generate interrupt. */
    ${RTOS_TMR_INSTANCE_NAME}_REGS->RTOS_CTRL &= ~RTOS_CTRL_TMR_STRT_Msk;
}

void ${RTOS_TMR_INSTANCE_NAME}Timer_Halt(void)
{
    /* Loads preload register to the counter and starts the timer */
    ${RTOS_TMR_INSTANCE_NAME}_REGS->RTOS_CTRL |= RTOS_CTRL_FW_TMR_HALT_Msk;
}

void ${RTOS_TMR_INSTANCE_NAME}Timer_Resume(void)
{
    /* Stops the timer, clears the counter to 0. Does not generate interrupt. */
    ${RTOS_TMR_INSTANCE_NAME}_REGS->RTOS_CTRL &= ~RTOS_CTRL_FW_TMR_HALT_Msk;
}

void ${RTOS_TMR_INSTANCE_NAME}Timer_PeriodSet(uint32_t period)
{
    ${RTOS_TMR_INSTANCE_NAME}_REGS->RTOS_PRLD = period;
}

uint32_t ${RTOS_TMR_INSTANCE_NAME}Timer_PeriodGet(void)
{
    return ${RTOS_TMR_INSTANCE_NAME}_REGS->RTOS_PRLD;
}

uint32_t ${RTOS_TMR_INSTANCE_NAME}Timer_CounterGet(void)
{
    return ${RTOS_TMR_INSTANCE_NAME}_REGS->RTOS_CNT;
}

uint32_t ${RTOS_TMR_INSTANCE_NAME}Timer_FrequencyGet(void)
{
    return 32768;
}

void ${RTOS_TMR_INSTANCE_NAME}Timer_CallbackRegister( RTOS_TMR_CALLBACK callback_fn, uintptr_t context )
{
    ${RTOS_TMR_INSTANCE_NAME?lower_case}TimerObj.callback_fn = callback_fn;
    ${RTOS_TMR_INSTANCE_NAME?lower_case}TimerObj.context = context;
}

void ${RTOS_TMR_NVIC_INTERRUPT_NAME}_InterruptHandler(void)
{
    <#if RTOS_TMR_INTERRUPT_TYPE == "AGGREGATE">
    if (ECIA_GIRQResultGet(ECIA_AGG_INT_SRC_RTMR) != 0U)
    <#else>
    if (ECIA_GIRQResultGet(ECIA_DIR_INT_SRC_RTMR) != 0U)
    </#if>
    {
        <#if RTOS_TMR_INTERRUPT_TYPE == "AGGREGATE">
        ECIA_GIRQSourceClear(ECIA_AGG_INT_SRC_RTMR);
        <#else>
        ECIA_GIRQSourceClear(ECIA_DIR_INT_SRC_RTMR);
        </#if>

        if(${RTOS_TMR_INSTANCE_NAME?lower_case}TimerObj.callback_fn != NULL)
        {
            ${RTOS_TMR_INSTANCE_NAME?lower_case}TimerObj.callback_fn(${RTOS_TMR_INSTANCE_NAME?lower_case}TimerObj.context);
        }    
    }
}
