/*******************************************************************************
  Breathing/Blinking LED Peripheral Library Interface Source File

  Company
    Microchip Technology Inc.

  File Name
    plib_${LED_INSTANCE_NAME?lower_case}.c

  Summary
    ${LED_INSTANCE_NAME} peripheral library source file.

  Description
    This file implements the interface to the Breathing/Blinking LED peripheral library.
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
#include "plib_${LED_INSTANCE_NAME?lower_case}.h"
<#if LED_MODE == "LED_BLINKING">
#include "peripheral/ecia/plib_ecia.h"

<#if LED_CLK_SRC == "0x1">
static LED_WDT_CALLBACK_OBJ ${LED_INSTANCE_NAME}_CallbackObject;
</#if>
</#if>

void ${LED_INSTANCE_NAME}_Initialize(void)
{
    ${LED_INSTANCE_NAME}_REGS->LED_CFG |= LED_CFG_RST_Msk;

    asm("nop");asm("nop");asm("nop");asm("nop");asm("nop");

    <#if LED_MODE == "LED_BREATHING">
    ${LED_INSTANCE_NAME}_REGS->LED_CFG = LED_CFG_CTRL(1) | LED_CFG_SYMMETRY(${LED_SYMMETRY}) | LED_CFG_PWM_SIZE(${LED_PWM_SIZE});

    ${LED_INSTANCE_NAME}_REGS->LED_LIMIT = LED_LIMIT_MIN(${LED_DUTY_CYCLE_MIN}) | LED_LIMIT_MAX(${LED_DUTY_CYCLE_MAX});

    ${LED_INSTANCE_NAME}_REGS->LED_DLY = LED_DLY_HIGH_PULSE(${LED_HIGH_DELAY}) | LED_DLY_LOW_PULSE(${LED_LOW_DELAY});

    ${LED_INSTANCE_NAME}_REGS->LED_STEP = LED_STEP_S0(${LED_UPDATE_STEPSIZE_0}) | LED_STEP_S1(${LED_UPDATE_STEPSIZE_1}) | LED_STEP_S2(${LED_UPDATE_STEPSIZE_2}) | LED_STEP_S3(${LED_UPDATE_STEPSIZE_3}) | LED_STEP_S4(${LED_UPDATE_STEPSIZE_4}) | LED_STEP_S5(${LED_UPDATE_STEPSIZE_5}) | LED_STEP_S6(${LED_UPDATE_STEPSIZE_6}) | LED_STEP_S7(${LED_UPDATE_STEPSIZE_7});

    ${LED_INSTANCE_NAME}_REGS->LED_INTRVL = LED_INTRVL_I0(${LED_UPDATE_INTERVAL_0}) | LED_INTRVL_I1(${LED_UPDATE_INTERVAL_1}) | LED_INTRVL_I2(${LED_UPDATE_INTERVAL_2}) | LED_INTRVL_I3(${LED_UPDATE_INTERVAL_3}) | LED_INTRVL_I4(${LED_UPDATE_INTERVAL_4}) | LED_INTRVL_I5(${LED_UPDATE_INTERVAL_5}) | LED_INTRVL_I6(${LED_UPDATE_INTERVAL_6}) | LED_INTRVL_I7(${LED_UPDATE_INTERVAL_7});

    <#else>
    ${LED_INSTANCE_NAME}_REGS->LED_CFG = LED_CFG_CTRL(2) | LED_CFG_CLK_SRC(${LED_CLK_SRC}) <#if LED_CLK_SRC == "0x1"> | LED_CFG_WDT_RELOAD(${LED_WDT_RELOAD}) </#if>;

    ${LED_INSTANCE_NAME}_REGS->LED_DLY = LED_DLY_LOW_PULSE(${LED_CLK_PRESCALER});

    ${LED_INSTANCE_NAME}_REGS->LED_LIMIT = LED_LIMIT_MIN(${LED_DUTY_CYCLE});
    </#if>

    ${LED_INSTANCE_NAME}_REGS->LED_CFG |= LED_CFG_EN_UPDATE_Msk;
}

<#if LED_MODE == "LED_BREATHING">
void ${LED_INSTANCE_NAME}_DutyCycleMinSet(uint8_t min)
{
    ${LED_INSTANCE_NAME}_REGS->LED_LIMIT = (${LED_INSTANCE_NAME}_REGS->LED_LIMIT & LED_LIMIT_MIN_Msk) | min;
}

void ${LED_INSTANCE_NAME}_DutyCycleMaxSet(uint8_t max)
{
    ${LED_INSTANCE_NAME}_REGS->LED_LIMIT = (${LED_INSTANCE_NAME}_REGS->LED_LIMIT & ~LED_LIMIT_MAX_Msk) | (max << LED_LIMIT_MAX_Pos);
}

void ${LED_INSTANCE_NAME}_LowDelaySet(uint16_t ld)
{
    ${LED_INSTANCE_NAME}_REGS->LED_DLY = (${LED_INSTANCE_NAME}_REGS->LED_DLY & ~LED_DLY_LOW_PULSE_Msk) | (ld << LED_DLY_LOW_PULSE_Pos);
}

void ${LED_INSTANCE_NAME}_HighDelaySet(uint16_t hd)
{
    ${LED_INSTANCE_NAME}_REGS->LED_DLY = (${LED_INSTANCE_NAME}_REGS->LED_DLY & ~LED_DLY_HIGH_PULSE_Msk) | (hd << LED_DLY_HIGH_PULSE_Pos);
}

void ${LED_INSTANCE_NAME}_SymmetrySet(LED_SYM sym)
{
    ${LED_INSTANCE_NAME}_REGS->LED_CFG = (${LED_INSTANCE_NAME}_REGS->LED_CFG & ~LED_CFG_SYMMETRY_Msk) | (sym << LED_CFG_SYMMETRY_Pos);
}

void ${LED_INSTANCE_NAME}_SegmentsStepSizeSet(uint32_t stepSzVal)
{
    ${LED_INSTANCE_NAME}_REGS->LED_STEP = stepSzVal;
}

void ${LED_INSTANCE_NAME}_SegmentsIntervalSet(uint32_t intervalVal)
{
    ${LED_INSTANCE_NAME}_REGS->LED_INTRVL = intervalVal;
}

<#else>
void ${LED_INSTANCE_NAME}_ClockPrescalerSet(uint16_t prescaler)
{
    ${LED_INSTANCE_NAME}_REGS->LED_DLY = (${LED_INSTANCE_NAME}_REGS->LED_DLY & ~LED_DLY_LOW_PULSE_Msk) | (prescaler << LED_DLY_LOW_PULSE_Pos);
}

void ${LED_INSTANCE_NAME}_DutyCycleCountSet(uint8_t dutyCycle)
{
    ${LED_INSTANCE_NAME}_REGS->LED_LIMIT = (${LED_INSTANCE_NAME}_REGS->LED_LIMIT & ~LED_LIMIT_MIN_Msk) | dutyCycle;
}

<#if LED_CLK_SRC == "0x1">
void ${LED_INSTANCE_NAME}_WDTReloadCountSet(uint8_t reloadCnt)
{
    ${LED_INSTANCE_NAME}_REGS->LED_CFG = (${LED_INSTANCE_NAME}_REGS->LED_CFG & ~LED_CFG_WDT_RELOAD_Msk) | (reloadCnt << LED_CFG_WDT_RELOAD_Pos);
}

void ${LED_INSTANCE_NAME}_WDT_CallbackRegister( LED_WDT_CALLBACK callback, uintptr_t context )
{
    ${LED_INSTANCE_NAME}_CallbackObject.callback = callback;

    ${LED_INSTANCE_NAME}_CallbackObject.context = context;
}

<#compress>
<#assign INT_HANDLER_NAME_PREFIX = "">

<#if .vars["LED_WDT_INTERRUPT_TYPE"] == "AGGREGATE">
<#assign INT_HANDLER_NAME_PREFIX = "_GRP">
</#if>
</#compress>

void ${LED_INSTANCE_NAME}${INT_HANDLER_NAME_PREFIX}_InterruptHandler(void)
{
    <#if .vars["LED_WDT_INTERRUPT_TYPE"] == "AGGREGATE">
    if (ECIA_GIRQResultGet(ECIA_AGG_INT_SRC_${LED_INSTANCE_NAME}))
    <#else>
    if (ECIA_GIRQResultGet(ECIA_DIR_INT_SRC_${LED_INSTANCE_NAME}))
    </#if>
    {
        <#if .vars["LED_WDT_INTERRUPT_TYPE"] == "AGGREGATE">
        ECIA_GIRQSourceClear(ECIA_AGG_INT_SRC_${LED_INSTANCE_NAME});
        <#else>
        ECIA_GIRQSourceClear(ECIA_DIR_INT_SRC_${LED_INSTANCE_NAME});
        </#if>

        if (${LED_INSTANCE_NAME}_CallbackObject.callback != NULL)
        {
            ${LED_INSTANCE_NAME}_CallbackObject.callback(${LED_INSTANCE_NAME}_CallbackObject.context);
        }
    }
}

</#if>
</#if>

void ${LED_INSTANCE_NAME}_Update(void)
{
    ${LED_INSTANCE_NAME}_REGS->LED_CFG |= LED_CFG_EN_UPDATE_Msk;
}



