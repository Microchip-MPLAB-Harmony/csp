/*******************************************************************************
  Timer/Counter(${TC_INSTANCE_NAME}) PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_${TC_INSTANCE_NAME?lower_case}.h

  Summary
    ${TC_INSTANCE_NAME} PLIB Header File.

  Description
    This file defines the interface to the TC peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

  Remarks:
    None.

*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
Copyright (c) 2017 released Microchip Technology Inc. All rights reserved.
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

#ifndef PLIB_${TC_INSTANCE_NAME}_H      // Guards against multiple inclusion
#define PLIB_${TC_INSTANCE_NAME}_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
/* This section lists the other files that are included in this file.
*/

#include "plib_tc_common.h"

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C Compatibility

    extern "C" {

#endif
// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Section: Data Types
// *****************************************************************************
// *****************************************************************************
/* The following data type definitions are used by the functions in this
    interface and should be considered part it.
*/

#define ${TC_INSTANCE_NAME}_TimerFrequencyGet()  (uint32_t)(${TC_FREQUENCY}UL)

// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************
/* The following functions make up the methods (set of possible operations) of
   this interface.
*/

// *****************************************************************************

void ${TC_INSTANCE_NAME}_TimerInitialize( void );

void ${TC_INSTANCE_NAME}_TimerStart( void );

void ${TC_INSTANCE_NAME}_TimerStop( void );

<#if TC_CTRLA_MODE = "COUNT8">

void ${TC_INSTANCE_NAME}_Timer8bitPeriodSet( uint8_t period );

uint8_t ${TC_INSTANCE_NAME}_Timer8bitPeriodGet( void );

uint8_t ${TC_INSTANCE_NAME}_Timer8bitCounterGet( void );

void ${TC_INSTANCE_NAME}_Timer8bitCounterSet( uint8_t count );

<#elseif TC_CTRLA_MODE = "COUNT16">

void ${TC_INSTANCE_NAME}_Timer16bitPeriodSet( uint16_t period );

uint16_t ${TC_INSTANCE_NAME}_Timer16bitPeriodGet( void );

uint16_t ${TC_INSTANCE_NAME}_Timer16bitCounterGet( void );

void ${TC_INSTANCE_NAME}_Timer16bitCounterSet( uint16_t count );

<#elseif TC_CTRLA_MODE = "COUNT32">

void ${TC_INSTANCE_NAME}_Timer32bitPeriodSet( uint32_t period );

uint32_t ${TC_INSTANCE_NAME}_Timer32bitPeriodGet( void );

uint32_t ${TC_INSTANCE_NAME}_Timer32bitCounterGet( void );

void ${TC_INSTANCE_NAME}_Timer32bitCounterSet( uint32_t count );
</#if>

bool ${TC_INSTANCE_NAME}_TimerPeriodHasExpired( void );

<#if TC_TIMER_INTERRUPT_MODE = true>

void ${TC_INSTANCE_NAME}_TimerCallbackRegister( TC_CALLBACK callback, uintptr_t context );

void ${TC_INSTANCE_NAME}_TimerInterruptHandler( void );
</#if>




// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END

#endif /* PLIB_${TC_INSTANCE_NAME}_H */
