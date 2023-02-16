/*******************************************************************************
  PWM Timer Peripheral Library Interface Source File

  Company
    Microchip Technology Inc.

  File Name
    plib_${PWM_INSTANCE_NAME?lower_case}.c

  Summary
    ${PWM_INSTANCE_NAME} peripheral library source file.

  Description
    This file implements the interface to the PWM Timer peripheral library.  This
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
#include "plib_${PWM_INSTANCE_NAME?lower_case}.h"

void ${PWM_INSTANCE_NAME}_Initialize(void)
{
    ${PWM_INSTANCE_NAME}_REGS->PWM_CFG &= ~PWM_CFG_PWM_EN_Msk;

    ${PWM_INSTANCE_NAME}_REGS->PWM_CNT_ON = ${PWM_ON_TIME_COUNTER};

    ${PWM_INSTANCE_NAME}_REGS->PWM_CNT_OFF = ${PWM_OFF_TIME_COUNTER};

    ${PWM_INSTANCE_NAME}_REGS->PWM_CFG = PWM_CFG_CLK_SEL(${PWM_CLOCK_SELECT}) | PWM_CFG_CLK_PRE_DIV(${PWM_CLOCK_DIVIDER}) <#if PWM_OUTPUT_INVERT == true> | PWM_CFG_INV_Msk </#if>;
}


void ${PWM_INSTANCE_NAME}_Start(void)
{
    ${PWM_INSTANCE_NAME}_REGS->PWM_CFG |= PWM_CFG_PWM_EN_Msk;
}

void ${PWM_INSTANCE_NAME}_Stop (void)
{
    ${PWM_INSTANCE_NAME}_REGS->PWM_CFG &= ~PWM_CFG_PWM_EN_Msk;
}

uint16_t ${PWM_INSTANCE_NAME}_OnCountGet (void)
{
    return (uint16_t)${PWM_INSTANCE_NAME}_REGS->PWM_CNT_ON;
}

uint16_t ${PWM_INSTANCE_NAME}_OffCountGet (void)
{
    return (uint16_t)${PWM_INSTANCE_NAME}_REGS->PWM_CNT_OFF;
}

void ${PWM_INSTANCE_NAME}_OnCountSet (uint16_t onCount)
{
    ${PWM_INSTANCE_NAME}_REGS->PWM_CNT_ON = onCount;
}

void ${PWM_INSTANCE_NAME}_OffCountSet (uint16_t offCount)
{
    ${PWM_INSTANCE_NAME}_REGS->PWM_CNT_OFF = offCount;
}

void ${PWM_INSTANCE_NAME}_ClkSelect (PWM_CLK_SEL pwmClk)
{
    ${PWM_INSTANCE_NAME}_REGS->PWM_CFG = (${PWM_INSTANCE_NAME}_REGS->PWM_CFG & ~PWM_CFG_CLK_SEL_Msk) | (pwmClk << PWM_CFG_CLK_SEL_Pos);
}

void ${PWM_INSTANCE_NAME}_ClkDividerSet (uint8_t divVal)
{
    ${PWM_INSTANCE_NAME}_REGS->PWM_CFG = (${PWM_INSTANCE_NAME}_REGS->PWM_CFG & ~PWM_CFG_CLK_PRE_DIV_Msk) | (divVal << PWM_CFG_CLK_PRE_DIV_Pos);
}

void ${PWM_INSTANCE_NAME}_OutputConfig (PWM_OUTPUT pwmOutput)
{
    ${PWM_INSTANCE_NAME}_REGS->PWM_CFG = (${PWM_INSTANCE_NAME}_REGS->PWM_CFG & ~PWM_CFG_INV_Msk) | (pwmOutput << PWM_CFG_INV_Pos);
}

