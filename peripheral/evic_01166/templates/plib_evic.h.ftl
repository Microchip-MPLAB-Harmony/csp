/*******************************************************************************
  EVIC PLIB Header

  Company:
    Microchip Technology Inc.

  File Name:
    plib_evic.h

  Summary:
    PIC32M Interrupt Module PLIB Header File

  Description:
    None

*******************************************************************************/

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

#ifndef PLIB_EVIC_H
#define PLIB_EVIC_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

#include <device.h>
#include <stddef.h>
#include <stdbool.h>
#include <device.h>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    extern "C" {

#endif
// DOM-IGNORE-END

<#assign NumOfEnabledExtInt = 0>

<#list 0..4 as i>
    <#assign EXT_INT_PIN = "EXTERNAL_" + i + "_EXTERNAL_INTERRUPT_UPDATE">
    <#if .vars[EXT_INT_PIN]?has_content && .vars[EXT_INT_PIN] == true>
        <#assign NumOfEnabledExtInt = NumOfEnabledExtInt + 1>
    </#if>
</#list>
// *****************************************************************************
// *****************************************************************************
// Section: Data Types
// *****************************************************************************
// *****************************************************************************

typedef enum
{
<#if EVIC_IRQ_MIN != -1 && EVIC_IRQ_MAX != -1>
<#list EVIC_IRQ_MIN..EVIC_IRQ_MAX as i>
    <#assign SUB_IRQ_COUNT = "EVIC_" + i + "_SUB_IRQ_COUNT">
    <#if .vars[SUB_IRQ_COUNT]?? && ((.vars[SUB_IRQ_COUNT] > 1) == true)>
        <#list 0..(.vars[SUB_IRQ_COUNT]) as j>
            <#assign INT_NAME = "EVIC_" + i + "_" + j + "_IRQ_NAME">
            <#assign IRQ_NAME = "EVIC_" + i + "_" + j + "_IRQ">
            <#if .vars[INT_NAME]?? && .vars[IRQ_NAME]?? && .vars[INT_NAME] != "None" && .vars[IRQ_NAME] != "None">
                <#lt>    INT_SOURCE_${.vars[INT_NAME]} = ${.vars[IRQ_NAME]},

            </#if>
        </#list>
    <#else>
        <#assign INT_NAME = "EVIC_" + i + "_IRQ_NAME">
        <#assign IRQ_NAME = "EVIC_" + i + "_IRQ">
        <#if .vars[INT_NAME]?? && .vars[IRQ_NAME]?? && .vars[INT_NAME] != "None" && .vars[IRQ_NAME] != "None">
            <#lt>    INT_SOURCE_${.vars[INT_NAME]} = ${.vars[IRQ_NAME]},

        </#if>
    </#if>
</#list>
<#else>
<#list EVIC_VECTOR_MIN..EVIC_VECTOR_MAX as i>
    <#assign INT_NAME = "EVIC_" + i + "_NAME">
    <#assign VECT_NAME = "EVIC_" + i + "_VECTOR">
    <#if .vars[INT_NAME]?? && .vars[VECT_NAME]?? && .vars[INT_NAME] != "None" && .vars[VECT_NAME] != "None">
        <#lt>    INT_SOURCE_${.vars[INT_NAME]} = ${.vars[VECT_NAME]},

    </#if>
</#list>
</#if>
} INT_SOURCE;

<#if 0 < NumOfEnabledExtInt>
typedef enum
{
<#list 0..4 as i>
    <#assign EXT_INT_PIN = "EXTERNAL_" + i + "_EXTERNAL_INTERRUPT_UPDATE">
    <#if .vars[EXT_INT_PIN]?has_content && .vars[EXT_INT_PIN] == true>
        <#lt>    EXTERNAL_INT_${i} = _IEC0_INT${i}IE_MASK,
    </#if>
</#list>
}EXTERNAL_INT_PIN;

typedef  void (*EXTERNAL_INT_PIN_CALLBACK) (EXTERNAL_INT_PIN pin, uintptr_t context);
</#if>

// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************

void EVIC_Initialize( void );

void EVIC_SourceEnable( INT_SOURCE source );

void EVIC_SourceDisable( INT_SOURCE source );

bool EVIC_SourceIsEnabled( INT_SOURCE source );

bool EVIC_SourceStatusGet( INT_SOURCE source );

void EVIC_SourceStatusSet( INT_SOURCE source );

void EVIC_SourceStatusClear( INT_SOURCE source );

<#if 0 < NumOfEnabledExtInt>
bool EVIC_ExternalInterruptCallbackRegister(
        EXTERNAL_INT_PIN extIntPin,
        const EXTERNAL_INT_PIN_CALLBACK callback,
        uintptr_t context
    );

void EVIC_ExternalInterruptEnable( EXTERNAL_INT_PIN extIntPin );

void EVIC_ExternalInterruptDisable( EXTERNAL_INT_PIN extIntPin );

typedef struct {

    /* Callback for event on target pin*/
    EXTERNAL_INT_PIN_CALLBACK        callback;

    /* Callback Context */
    uintptr_t               context;
    
} EXT_INT_PIN_CALLBACK_OBJ;
</#if>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility
    }
#endif
// DOM-IGNORE-END

#endif // PLIB_EVIC_H
