/*******************************************************************************
  Motor Control PWM (MCPWM) Peripheral Library Interface Header File

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${MCPWM_INSTANCE_NAME?lower_case}.h

  Summary:
    MCPWM PLIB Header File

  Description:
    None

*******************************************************************************/

/*******************************************************************************
* Copyright (C) 2019 Microchip Technology Inc. and its subsidiaries.
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

#ifndef _PLIB_${MCPWM_INSTANCE_NAME}_H
#define _PLIB_${MCPWM_INSTANCE_NAME}_H

#include <stddef.h>
#include <stdbool.h>
#include <stdint.h>
#include "device.h"
#include "plib_mcpwm_common.h"

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility
    extern "C" {
#endif
// DOM-IGNORE-END


// *****************************************************************************
// Section: Interface
// *****************************************************************************
// *****************************************************************************

// *************************** ${MCPWM_INSTANCE_NAME} API ***************************************/
// *****************************************************************************
<#assign interrupt_mode = false>
<#list 1 .. MCPWM_NUM_CHANNELS as i>
<#assign interrupt = "MCPWM_EVIC" + i>
<#if .vars[interrupt] == 1>
<#assign interrupt_mode = true>
</#if>
</#list>

void ${MCPWM_INSTANCE_NAME}_Initialize (void);

void ${MCPWM_INSTANCE_NAME}_Start (void);

void ${MCPWM_INSTANCE_NAME}_Stop (void);

void ${MCPWM_INSTANCE_NAME}_PrimaryPeriodSet(uint16_t period);

uint16_t ${MCPWM_INSTANCE_NAME}_PrimaryPeriodGet(void);

void ${MCPWM_INSTANCE_NAME}_SecondaryPeriodSet(uint16_t period);

uint16_t ${MCPWM_INSTANCE_NAME}_SecondaryPeriodGet(void);

void ${MCPWM_INSTANCE_NAME}_ChannelPrimaryDutySet(MCPWM_CH_NUM channel, uint16_t duty);

void ${MCPWM_INSTANCE_NAME}_ChannelSecondaryDutySet(MCPWM_CH_NUM channel, uint16_t duty);

void ${MCPWM_INSTANCE_NAME}_ChannelDeadTimeSet(MCPWM_CH_NUM channel, uint16_t high_deadtime, uint16_t low_deadtime);

void ${MCPWM_INSTANCE_NAME}_ChannelPrimaryTriggerSet(MCPWM_CH_NUM channel, uint16_t trigger);

void ${MCPWM_INSTANCE_NAME}_ChannelSecondaryTriggerSet(MCPWM_CH_NUM channel, uint16_t trigger);

void ${MCPWM_INSTANCE_NAME}_ChannelLeadingEdgeBlankingDelaySet(MCPWM_CH_NUM channel, uint16_t delay);

<#if PTCON__SEIEN == true>
void ${MCPWM_INSTANCE_NAME}_PrimaryEventCallbackRegister(MCPWM_CALLBACK callback, uintptr_t context);
</#if>

<#if STCON__SSEIEN == true>
void ${MCPWM_INSTANCE_NAME}_SecondaryEventCallbackRegister(MCPWM_CALLBACK callback, uintptr_t context);
</#if>

<#if interrupt_mode == true>
void ${MCPWM_INSTANCE_NAME}_CallbackRegister(MCPWM_CH_NUM channel, MCPWM_CH_CALLBACK callback, uintptr_t context);
</#if>


// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility
    }
#endif

// DOM-IGNORE-END
#endif // _PLIB_${MCPWM_INSTANCE_NAME}_H
