/*******************************************************************************
  PWM Peripheral Library Interface Header File

  Company
    Microchip Technology Inc.

  File Name
    plib_pwm${INDEX}.h

  Summary
    PWM${INDEX} peripheral library interface.

  Description
    This file defines the interface to the PWM peripheral library.  This 
    library provides access to and control of the associated peripheral 
    instance.

******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
Copyright (c) 2017 released Microchip Technology Inc.  All rights reserved.

Microchip licenses to you the right to use, modify, copy and distribute
Software only when embedded on a Microchip microcontroller or digital signal
controller that is integrated into your product or third party product
(pursuant to the sublicense terms in the accompanying license agreement).

You should refer to the license agreement accompanying this Software for
additional information regarding your rights and obligations.
SOFTWARE AND DOCUMENTATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND,
EITHER EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION, ANY WARRANTY OF
MERCHANTABILITY, TITLE, NON-INFRINGEMENT AND FITNESS FOR A PARTICULAR PURPOSE.
IN NO EVENT SHALL MICROCHIP OR ITS LICENSORS BE LIABLE OR OBLIGATED UNDER
CONTRACT, NEGLIGENCE, STRICT LIABILITY, CONTRIBUTION, BREACH OF WARRANTY, OR
OTHER LEGAL EQUITABLE THEORY ANY DIRECT OR INDIRECT DAMAGES OR EXPENSES
INCLUDING BUT NOT LIMITED TO ANY INCIDENTAL, SPECIAL, INDIRECT, PUNITIVE OR
CONSEQUENTIAL DAMAGES, LOST PROFITS OR LOST DATA, COST OF PROCUREMENT OF
SUBSTITUTE GOODS, TECHNOLOGY, SERVICES, OR ANY CLAIMS BY THIRD PARTIES
(INCLUDING BUT NOT LIMITED TO ANY DEFENSE THEREOF), OR OTHER SIMILAR COSTS.
*******************************************************************************/
// DOM-IGNORE-END

#ifndef PLIB_PWM${INDEX}_H    // Guards against multiple inclusion
#define PLIB_PWM${INDEX}_H


// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

/*  This section lists the other files that are included in this file.
*/

#include "plib_pwm.h"

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

__inline__ void PWM${INDEX}_ChannelDutySet(PWM_CHANNEL_NUM channel, uint16_t duty)
{
  PWM${INDEX}_REGS->PWM_CH_NUM[channel].PWM_CDTYUPD= duty;
}

void PWM${INDEX}_Initialize (void);

void PWM${INDEX}_ChannelsStart (PWM_CHANNEL_MASK channelMask);

void PWM${INDEX}_ChannelsStop (PWM_CHANNEL_MASK channelMask);

void PWM${INDEX}_ChannelPeriodSet (PWM_CHANNEL_NUM channel, uint16_t period);

uint16_t PWM${INDEX}_ChannelPeriodGet (PWM_CHANNEL_NUM channel);

void PWM${INDEX}_ChannelDeadTimeSet (PWM_CHANNEL_NUM channel, uint16_t deadtime_high, uint16_t deadtime_low);

void PWM${INDEX}_CompareValueSet (PWM_COMPARE cmp_unit, uint16_t cmp_value);

void PWM${INDEX}_ChannelCounterEventEnable (PWM_CHANNEL_MASK channelMask);

void PWM${INDEX}_ChannelCounterEventDisable (PWM_CHANNEL_MASK  channelMask);

bool PWM${INDEX}_ChannelCounterEventStatusGet (PWM_CHANNEL_NUM channel);

void PWM${INDEX}_SyncUpdateEnable (void);

void PWM${INDEX}_FaultStatusClear(PWM_FAULT_ID fault_id);

<#if PWM_INTERRUPT == true>
void PWM${INDEX}_CallbackRegister(PWM_CALLBACK callback, uintptr_t context);
</#if>

#endif //PLIB_PWM${INDEX}_H

/**
 End of File
*/
