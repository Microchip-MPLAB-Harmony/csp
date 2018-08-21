/*******************************************************************************
  Timer/Counter(TC${TC_INDEX}) PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_tc${TC_INDEX}.h

  Summary
    TC${TC_INDEX} PLIB Header File.

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

#ifndef PLIB_TC${TC_INDEX}_H       // Guards against multiple inclusion
#define PLIB_TC${TC_INDEX}_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
/* This section lists the other files that are included in this file.
*/

#include "plib_tc.h"

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

#define TC${TC_INDEX}_CaptureFrequencyGet()  (uint32_t)(${TC_FREQUENCY}UL)

// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************
/* The following functions make up the methods (set of possible operations) of
   this interface.
*/
<#compress>
<#assign TC_INTSET_VAL = "">
<#list 0..(TC_NUM_CHANNELS - 1) as i>
<#assign TC_CAPTURE_INTERRUPT = "TC_CAPTURE_INTSET_MC"+i>
    <#if .vars[TC_CAPTURE_INTERRUPT] == true>
        <#if TC_INTSET_VAL != "">
            <#assign TC_INTSET_VAL = TC_INTSET_VAL + " | TC_INTENSET_MC"+i+"_Msk">
        <#else>
            <#assign TC_INTSET_VAL = "TC_INTENSET_MC"+i+"_Msk">
        </#if>
    </#if>
</#list>
<#if TC_CAPTURE_ERR_INTERRUPT_MODE == true>
    <#if TC_INTSET_VAL != "">
        <#assign TC_INTSET_VAL = TC_INTSET_VAL + " | TC_INTENSET_ERR_Msk">
    <#else>
        <#assign TC_INTSET_VAL = "TC_INTENSET_ERR_Msk">
    </#if>
</#if>

<#if TC_CAPTURE_OVF_INTERRUPT_MODE == true>
    <#if TC_INTSET_VAL != "">
        <#assign TC_INTSET_VAL = TC_INTSET_VAL + " | TC_INTENSET_OVF_Msk">
    <#else>
        <#assign TC_INTSET_VAL = "TC_INTENSET_OVF_Msk">
    </#if>
</#if>
</#compress>

void TC${TC_INDEX}_CaptureInitialize ( void );

void TC${TC_INDEX}_CaptureStart ( void );

void TC${TC_INDEX}_CaptureStop ( void );

<#if TC_CTRLA_MODE = "COUNT8">
uint8_t TC${TC_INDEX}_Capture8bitChannel0Get( void );

uint8_t TC${TC_INDEX}_Capture8bitChannel1Get( void );

<#elseif TC_CTRLA_MODE = "COUNT16">

uint16_t TC${TC_INDEX}_Capture16bitChannel0Get( void );

uint16_t TC${TC_INDEX}_Capture16bitChannel1Get( void );

<#elseif TC_CTRLA_MODE = "COUNT32">

uint32_t TC${TC_INDEX}_Capture32bitChannel0Get( void );

uint32_t TC${TC_INDEX}_Capture32bitChannel1Get( void );
</#if>

TC_CAPTURE_STATUS TC${TC_INDEX}_CaptureStatusGet( void );

<#if TC_INTSET_VAL != "">
void TC${TC_INDEX}_CaptureCallbackRegister(TC_CALLBACK callback, uintptr_t context);

void TC${TC_INDEX}_CaptureInterruptHandler( void );
</#if>


// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END

#endif /* PLIB_TC${TC_INDEX}_H */
