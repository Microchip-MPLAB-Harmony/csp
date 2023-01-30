/*******************************************************************************
  Data Type definition of 32-bit Timer PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${TMR32_INSTANCE_NAME?lower_case}_tmr.h

  Summary:
    Data Type definition of the 32-bit Timer Peripheral Interface Plib.

  Description:
    This file defines the Data Types for the 32-bit Timer Plib.

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

#ifndef PLIB_${TMR32_INSTANCE_NAME}_H
#define PLIB_${TMR32_INSTANCE_NAME}_H

#include <stddef.h>
#include <stdint.h>
#include <stdbool.h>
#include "device.h"
#include "plib_timer32_common.h"

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
void ${TMR32_INSTANCE_NAME}_Initialize(void);

void ${TMR32_INSTANCE_NAME}_PrescalerSet(uint16_t prescale_val);

uint32_t ${TMR32_INSTANCE_NAME}_FrequencyGet(void);

void ${TMR32_INSTANCE_NAME}_PreLoadCountSet(uint32_t count);

uint32_t ${TMR32_INSTANCE_NAME}_PreLoadCountGet(void);

void ${TMR32_INSTANCE_NAME}_CounterSet(uint32_t count);

uint32_t ${TMR32_INSTANCE_NAME}_CounterGet(void);

void ${TMR32_INSTANCE_NAME}_Start(void);

void ${TMR32_INSTANCE_NAME}_Stop(void);

void ${TMR32_INSTANCE_NAME}_Reload(void);

void ${TMR32_INSTANCE_NAME}_AutoReStartEnable(void);

void ${TMR32_INSTANCE_NAME}_AutoReStartDisable(void);

<#if TMR32_INTERRUPT_EN == true>
void TIMER32_${TMR32_INSTANCE_NUMBER}_CallbackRegister(TMR32_CALLBACK callback_fn, uintptr_t context );
<#else>
bool ${TMR32_INSTANCE_NAME}_PeriodHasExpired(void);
</#if>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }
#endif
// DOM-IGNORE-END

#endif /* PLIB_${TMR32_INSTANCE_NAME}_H */
