/*******************************************************************************
  Data Type definition of Timer PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${CCP_INSTANCE_NAME?lower_case}.h

  Summary:
    Data Type definition of the Timer Peripheral Interface Plib.

  Description:
    This file defines the Data Types for the Timer Plib.

  Remarks:
    None.

*******************************************************************************/

/*******************************************************************************
* Copyright (C) 2025 Microchip Technology Inc. and its subsidiaries.
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

#ifndef PLIB_${CCP_INSTANCE_NAME}_H
#define PLIB_${CCP_INSTANCE_NAME}_H

#include <stddef.h>
#include <stdint.h>
#include "device.h"
#include "plib_ccp_common.h"

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
void ${CCP_INSTANCE_NAME}_TimerInitialize(void);

void ${CCP_INSTANCE_NAME}_TimerStart(void);

void ${CCP_INSTANCE_NAME}_TimerStop(void);

<#if CCP_CCPCON1_T32 == false>
void ${CCP_INSTANCE_NAME}_Timer16bitPeriodSet(uint16_t period);

uint16_t ${CCP_INSTANCE_NAME}_Timer16bitPeriodGet(void);

uint16_t ${CCP_INSTANCE_NAME}_Timer16bitCounterGet(void);
<#else>
void ${CCP_INSTANCE_NAME}_Timer32bitPeriodSet(uint32_t period);

uint32_t ${CCP_INSTANCE_NAME}_Timer32bitPeriodGet(void);

uint32_t ${CCP_INSTANCE_NAME}_Timer32bitCounterGet(void);
</#if>

uint32_t ${CCP_INSTANCE_NAME}_TimerFrequencyGet(void);

<#if CCP_TIMER_INTERRUPT == true>
void ${CCP_INSTANCE_NAME}_TimerInterruptEnable(void);

void ${CCP_INSTANCE_NAME}_TimerInterruptDisable(void);

void ${CCP_INSTANCE_NAME}_TimerCallbackRegister( CCP_TIMER_CALLBACK callback_fn, uintptr_t context );
</#if>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }
#endif
// DOM-IGNORE-END

#endif /* PLIB_${CCP_INSTANCE_NAME}_H */
