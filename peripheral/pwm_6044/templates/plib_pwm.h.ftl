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
#include "device.h"

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
    <#assign PWM_IER_CHID = "CH" + i + "_IER_CHID">
    <#assign PWM_CH_ENABLE = "CH" + i + "_EN">
    <#if .vars[PWM_CH_ENABLE] == true && .vars[PWM_IER_CHID] == true>
        <#assign PWM_INTERRUPT = true>
    </#if>
</#list>

void ${PWM_INSTANCE_NAME}_Initialize (void);

void ${PWM_INSTANCE_NAME}_ChannelsStart (PWM_CHANNEL_MASK channelMask);

void ${PWM_INSTANCE_NAME}_ChannelsStop (PWM_CHANNEL_MASK channelMask);

void ${PWM_INSTANCE_NAME}_ChannelPeriodSet (PWM_CHANNEL_NUM channel, uint32_t period);

uint32_t ${PWM_INSTANCE_NAME}_ChannelPeriodGet (PWM_CHANNEL_NUM channel);

void ${PWM_INSTANCE_NAME}_ChannelDutySet(PWM_CHANNEL_NUM channel, uint32_t duty);

uint32_t ${PWM_INSTANCE_NAME}_ChannelPeriodGet (PWM_CHANNEL_NUM channel);

void ${PWM_INSTANCE_NAME}_ChannelInterruptEnable (PWM_CHANNEL_MASK channelMask);

void ${PWM_INSTANCE_NAME}_ChannelInterruptDisable (PWM_CHANNEL_MASK  channelMask);

<#if PWM_INTERRUPT == true>
void ${PWM_INSTANCE_NAME}_CallbackRegister(PWM_CALLBACK callback, uintptr_t context);
<#else>
bool ${PWM_INSTANCE_NAME}_ChannelCounterEventStatusGet (PWM_CHANNEL_NUM channel);
</#if>

#endif //PLIB_${PWM_INSTANCE_NAME}_H

/**
 End of File
*/
