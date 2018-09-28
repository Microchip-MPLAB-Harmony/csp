/*******************************************************************************
  PWM Peripheral Library Interface Header File

  Company
    Microchip Technology Inc.

  File Name
    plib_pwm0.h

  Summary
    PWM0 peripheral library interface.

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

#ifndef PLIB_PWM0_H    // Guards against multiple inclusion
#define PLIB_PWM0_H


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

__inline__ void PWM0_ChannelDutySet(PWM_CHANNEL_NUM channel, uint16_t duty)
{
  PWM0_REGS->PWM_CH_NUM[channel].PWM_CDTYUPD= duty;
}

void PWM0_Initialize (void);

void PWM0_ChannelsStart (PWM_CHANNEL_MASK channelMask);

void PWM0_ChannelsStop (PWM_CHANNEL_MASK channelMask);

void PWM0_ChannelPeriodSet (PWM_CHANNEL_NUM channel, uint16_t period);

uint16_t PWM0_ChannelPeriodGet (PWM_CHANNEL_NUM channel);

void PWM0_ChannelDeadTimeSet (PWM_CHANNEL_NUM channel, uint16_t deadtime_high, uint16_t deadtime_low);

void PWM0_CompareValueSet (PWM_COMPARE cmp_unit, uint16_t cmp_value);

void PWM0_ChannelCounterEventEnable (PWM_CHANNEL_MASK channelMask);

void PWM0_ChannelCounterEventDisable (PWM_CHANNEL_MASK  channelMask);

bool PWM0_ChannelCounterEventStatusGet (PWM_CHANNEL_NUM channel);

void PWM0_SyncUpdateEnable (void);

void PWM0_FaultStatusClear(PWM_FAULT_ID fault_id);

void PWM0_CallbackRegister(PWM_CALLBACK callback, uintptr_t context);

#endif //PLIB_PWM0_H

/**
 End of File
*/
