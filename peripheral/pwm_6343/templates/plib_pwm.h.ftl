/*******************************************************************************
  PWM Peripheral Library Interface Header File

  Company
    Microchip Technology Inc.

  File Name
    plib_${PWM_INSTANCE_NAME?lower_case}.h

  Summary
    ${PWM_INSTANCE_NAME} peripheral library interface.

  Description
    This file defines the interface to the PWM peripheral library.  This
    library provides access to and control of the associated peripheral
    instance.

******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
* Copyright (C) 2018 Microchip Technology Inc. and its subsidiaries.
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

#ifndef PLIB_${PWM_INSTANCE_NAME}_H    // Guards against multiple inclusion
#define PLIB_${PWM_INSTANCE_NAME}_H


// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

/*  This section lists the other files that are included in this file.
*/

#include "plib_pwm_common.h"

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

extern "C" {

#endif

// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Section: Data Types
// *****************************************************************************
// *****************************************************************************
/*  The following data type definitions are used by the functions in this
    interface and should be considered part it.
*/

// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************
/* The following functions make up the methods (set of possible operations) of
   this interface.
*/
<#assign PWM_INTERRUPT = false>
<#list 0..3 as i>
    <#assign PWM_IER1_CHID = "PWM_CH_"+i+"_IER1_CHID">
    <#assign PWM_CH_ENABLE = "PWM_CH_"+ i +"_ENABLE">
    <#if .vars[PWM_CH_ENABLE] == true && .vars[PWM_IER1_CHID] == true>
        <#assign PWM_INTERRUPT = true>
    </#if>
</#list>

__inline__ void ${PWM_INSTANCE_NAME}_ChannelDutySet(PWM_CHANNEL_NUM channel, uint16_t duty)
{
  ${PWM_INSTANCE_NAME}_REGS->PWM_CH_NUM[channel].PWM_CDTYUPD= duty;
}

void ${PWM_INSTANCE_NAME}_Initialize (void);

void ${PWM_INSTANCE_NAME}_ChannelsStart (PWM_CHANNEL_MASK channelMask);

void ${PWM_INSTANCE_NAME}_ChannelsStop (PWM_CHANNEL_MASK channelMask);

void ${PWM_INSTANCE_NAME}_ChannelPeriodSet (PWM_CHANNEL_NUM channel, uint16_t period);

uint16_t ${PWM_INSTANCE_NAME}_ChannelPeriodGet (PWM_CHANNEL_NUM channel);

void ${PWM_INSTANCE_NAME}_ChannelDeadTimeSet (PWM_CHANNEL_NUM channel, uint16_t deadtime_high, uint16_t deadtime_low);

void ${PWM_INSTANCE_NAME}_CompareValueSet (PWM_COMPARE cmp_unit, uint16_t cmp_value);

void ${PWM_INSTANCE_NAME}_ChannelCounterEventEnable (PWM_CHANNEL_MASK channelMask);

void ${PWM_INSTANCE_NAME}_ChannelCounterEventDisable (PWM_CHANNEL_MASK  channelMask);

bool ${PWM_INSTANCE_NAME}_ChannelCounterEventStatusGet (PWM_CHANNEL_NUM channel);

void ${PWM_INSTANCE_NAME}_SyncUpdateEnable (void);

void ${PWM_INSTANCE_NAME}_FaultStatusClear(PWM_FAULT_ID fault_id);

<#if PWM_INTERRUPT == true>
void ${PWM_INSTANCE_NAME}_CallbackRegister(PWM_CALLBACK callback, uintptr_t context);
</#if>

#endif //PLIB_${PWM_INSTANCE_NAME}_H

/**
 End of File
*/
