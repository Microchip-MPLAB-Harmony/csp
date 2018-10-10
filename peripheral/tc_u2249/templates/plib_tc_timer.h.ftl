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

uint32_t ${TC_INSTANCE_NAME}_TimerFrequencyGet();

<#if TC_CTRLA_MODE = "COUNT8">

void ${TC_INSTANCE_NAME}_Timer8bitPeriodSet( uint8_t period );

uint8_t ${TC_INSTANCE_NAME}_Timer8bitPeriodGet( void );

uint8_t ${TC_INSTANCE_NAME}_Timer8bitCounterGet( void );

void ${TC_INSTANCE_NAME}_Timer8bitCounterSet( uint8_t count );

<#if TC_SYS_TIME_CONNECTED == true>
void ${TC_INSTANCE_NAME}_Timer8bitCompareSet( uint8_t compare );
</#if>

<#elseif TC_CTRLA_MODE = "COUNT16">

void ${TC_INSTANCE_NAME}_Timer16bitPeriodSet( uint16_t period );

uint16_t ${TC_INSTANCE_NAME}_Timer16bitPeriodGet( void );

uint16_t ${TC_INSTANCE_NAME}_Timer16bitCounterGet( void );

void ${TC_INSTANCE_NAME}_Timer16bitCounterSet( uint16_t count );

<#if TC_SYS_TIME_CONNECTED == true>
void ${TC_INSTANCE_NAME}_Timer16bitCompareSet( uint16_t compare );
</#if>

<#elseif TC_CTRLA_MODE = "COUNT32">

void ${TC_INSTANCE_NAME}_Timer32bitPeriodSet( uint32_t period );

uint32_t ${TC_INSTANCE_NAME}_Timer32bitPeriodGet( void );

uint32_t ${TC_INSTANCE_NAME}_Timer32bitCounterGet( void );

void ${TC_INSTANCE_NAME}_Timer32bitCounterSet( uint32_t count );

<#if TC_SYS_TIME_CONNECTED == true>
void ${TC_INSTANCE_NAME}_Timer32bitCompareSet( uint32_t compare );
</#if>
</#if>

<#if TC_TIMER_INTENSET_OVF = true || TC_TIMER_INTENSET_MC1 == true>

void ${TC_INSTANCE_NAME}_TimerCallbackRegister( TC_TIMER_CALLBACK callback, uintptr_t context );

<#else>
bool ${TC_INSTANCE_NAME}_TimerPeriodHasExpired( void );
</#if>




// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END

#endif /* PLIB_${TC_INSTANCE_NAME}_H */
