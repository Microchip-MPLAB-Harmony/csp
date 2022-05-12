/*******************************************************************************
  Dual watchdog  timer (DWDT) PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_dwdt.h

  Summary
    DWDT PLIB Header File.

  Description
    This file defines the interface to the DWDT peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

  Remarks:
    None.
*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
* Copyright (C) 2021 Microchip Technology Inc. and its subsidiaries.
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
<#compress>
<#if (DWDT_PS_EVENT == "Interrupt") ||  (DWDT_PS_REPEAT_THRESHOLD_ENABLE == "Interrupt") || DWDT_PS_LEVEL_ENABLE || DWDT_PS_NS_PERIOD_INTERRUPT_ENABLE || DWDT_PS_NS_REPEAT_INTERRUPT_ENABLE>
<#assign DWDT_PS_INTERRUPT_ENABLE = true>
<#else>
<#assign DWDT_PS_INTERRUPT_ENABLE = false>
</#if>
<#if DWDT_NS_PERIOD_ENABLE || DWDT_NS_REPEAT_THRESHOLD_ENABLE || DWDT_NS_LEVEL_ENABLE>
<#assign DWDT_NS_INTERRUPT_ENABLE = true>
<#else>
<#assign DWDT_NS_INTERRUPT_ENABLE = false>
</#if>
</#compress>
/* Guards against multiple inclusion */
#ifndef PLIB_DWDT_H
#define PLIB_DWDT_H

#ifdef __cplusplus // Provide C++ Compatibility
extern "C" {
#endif /* __cplusplus */

#include <stdbool.h>

typedef void (*DWDT_CALLBACK) (uint32_t interruptStatus, uintptr_t context);

void DWDT_Initialize(void);
<#if DWDT_PS_ENABLE>
void DWDT_PS_Clear(void);
<#if DWDT_PS_LOCK_CONFIG>
void DWDT_PS_Disable(void);
</#if>
</#if>
<#if DWDT_PS_INTERRUPT_ENABLE>
void DWDT_PS_CallbackRegister(DWDT_CALLBACK pCallback, uintptr_t context);
</#if>
<#if DWDT_NS_ENABLE>
void DWDT_NS_Clear(void);
<#if DWDT_NS_LOCK_CONFIG>
void DWDT_NS_Disable(void);
</#if>
</#if>
<#if DWDT_NS_INTERRUPT_ENABLE>
void DWDT_NS_CallbackRegister(DWDT_CALLBACK pCallback, uintptr_t context);
</#if>
#ifdef __cplusplus // Provide C++ Compatibility
}
#endif /* __cplusplus */

#endif //PLIB_DWDT_H