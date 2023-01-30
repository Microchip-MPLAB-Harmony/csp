/*******************************************************************************
  Data Type definition of CCT Timer PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${CCT_INSTANCE_NAME?lower_case}_tmr.h

  Summary:
    Data Type definition of the CCT Timer Peripheral Interface Plib.

  Description:
    This file defines the Data Types for the CCT Timer Plib.

  Remarks:
    None.

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

#ifndef PLIB_${CCT_INSTANCE_NAME}_H
#define PLIB_${CCT_INSTANCE_NAME}_H

#include <stddef.h>
#include <stdint.h>
#include "device.h"
#include "plib_cct_common.h"

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

// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
void ${CCT_INSTANCE_NAME}_Initialize(void);

void ${CCT_INSTANCE_NAME}_TimerActivate( void );

void ${CCT_INSTANCE_NAME}_TimerDeActivate( void );

void ${CCT_INSTANCE_NAME}_FreeRunningTimerStart( void );

void ${CCT_INSTANCE_NAME}_FreeRunningTimerStop( void );

void ${CCT_INSTANCE_NAME}_FreeRunningTimerReset( void );

uint32_t ${CCT_INSTANCE_NAME}_FreeRunningTimerGet( void );

void ${CCT_INSTANCE_NAME}_FreeRunningTimerSet( uint32_t count);

void ${CCT_INSTANCE_NAME}_FreqDivSet( uint32_t div );

uint32_t ${CCT_INSTANCE_NAME}_FrequencyGet(void);

<#if .vars["CCT_OVF_INTERRUPT_EN"] == true>
void ${CCT_INSTANCE_NAME}_CounterOverflowCallbackRegister( CCT_CALLBACK callback, uintptr_t context );
</#if>

<#list 0..(CCT_NUM_CAP_CH-1) as n>
<#if .vars["CCT_ENABLE_CAPTURE_" + n] == true>
<#if .vars["CCT_CAP_INTERRUPT_EN_" + n] == true>
void ${CCT_INSTANCE_NAME}_Capture${n}CallbackRegister( CCT_CALLBACK callback, uintptr_t context );
</#if>

uint32_t ${CCT_INSTANCE_NAME}_CaptureChannel${n}Get( void );

</#if>
</#list>

<#list 0..(CCT_NUM_CMP_CH-1) as n>
<#if .vars["CCT_ENABLE_COMPARE_" + n] == true>
<#if .vars["CCT_CMP_INTERRUPT_EN_" + n] == true>

void ${CCT_INSTANCE_NAME}_Compare${n}CallbackRegister( CCT_CALLBACK callback, uintptr_t context );
</#if>

uint32_t ${CCT_INSTANCE_NAME}_CompareChannel${n}PeriodGet( void );

void ${CCT_INSTANCE_NAME}_CompareChannel${n}PeriodSet( uint32_t period );

void ${CCT_INSTANCE_NAME}_CompareChannel${n}Enable( void );

void ${CCT_INSTANCE_NAME}_CompareChannel${n}Disable( void );

void ${CCT_INSTANCE_NAME}_CompareChannel${n}OutputSet( void );

void ${CCT_INSTANCE_NAME}_CompareChannel${n}OutputClear( void );

</#if>
</#list>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }
#endif
// DOM-IGNORE-END

#endif /* PLIB_${CCT_INSTANCE_NAME}_H */
