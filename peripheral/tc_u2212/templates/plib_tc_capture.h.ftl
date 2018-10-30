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

#ifndef PLIB_${TC_INSTANCE_NAME}_H       // Guards against multiple inclusion
#define PLIB_${TC_INSTANCE_NAME}_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
/* This section lists the other files that are included in this file.
*/

#include "device.h"
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

void ${TC_INSTANCE_NAME}_CaptureInitialize ( void );

void ${TC_INSTANCE_NAME}_CaptureStart ( void );

void ${TC_INSTANCE_NAME}_CaptureStop ( void );

uint32_t ${TC_INSTANCE_NAME}_CaptureFrequencyGet();

<#if TC_CTRLA_MODE = "COUNT8">
uint8_t ${TC_INSTANCE_NAME}_Capture8bitChannel0Get( void );

uint8_t ${TC_INSTANCE_NAME}_Capture8bitChannel1Get( void );

<#elseif TC_CTRLA_MODE = "COUNT16">

uint16_t ${TC_INSTANCE_NAME}_Capture16bitChannel0Get( void );

uint16_t ${TC_INSTANCE_NAME}_Capture16bitChannel1Get( void );

<#elseif TC_CTRLA_MODE = "COUNT32">

uint32_t ${TC_INSTANCE_NAME}_Capture32bitChannel0Get( void );

uint32_t ${TC_INSTANCE_NAME}_Capture32bitChannel1Get( void );
</#if>

<#if TC_INTSET_VAL != "">
void ${TC_INSTANCE_NAME}_CaptureCallbackRegister(TC_CAPTURE_CALLBACK callback, uintptr_t context);

<#else>
TC_CAPTURE_STATUS ${TC_INSTANCE_NAME}_CaptureStatusGet( void );
</#if>


// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END

#endif /* PLIB_${TC_INSTANCE_NAME}_H */
