/*******************************************************************************
  Power PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_power.h

  Summary
    Power PLIB Header File.

  Description
    This file defines the interface to the DSCTRL peripheral library.
    This library provides access to and control of the associated Resets.

  Remarks:
    None.

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

#ifndef PLIB_POWER_H      // Guards against multiple inclusion
#define PLIB_POWER_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

#include <stdbool.h>
#include <stddef.h>
#include "device.h"

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility

    extern "C" {

#endif
// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Section: Data Types
// *****************************************************************************
// *****************************************************************************

typedef enum {

    LOW_POWER_IDLE_MODE,
    LOW_POWER_SLEEP_MODE,
<#if DREAM_MODE_EXIST??>
    LOW_POWER_DREAM_MODE,
</#if>
<#if DEEP_SLEEP_MODE_EXIST??>
    LOW_POWER_DEEP_SLEEP_MODE,
</#if>
    LOW_POWER_EXTREME_DEEP_SLEEP_MODE,
} POWER_LOW_POWER_MODE;

<#if DEEP_SLEEP_MODE_EXIST??>
typedef enum
{
<#list 0..(DS_WAKEUP_CAUSE_COUNT - 1) as i>
    <#assign DS_WAKEUP_CAUSE = "DS_WAKEUP_CAUSE_" + i>
    POWER_DS_WAKEUP_SOURCE_${.vars[DS_WAKEUP_CAUSE]} = DSCON_DSWAKE_${.vars[DS_WAKEUP_CAUSE]}_Msk,

</#list>
} POWER_DS_WAKEUP_SOURCE;

typedef enum
{
    POWER_DS_SEMAPHORE_1,
    
    POWER_DS_EXTENDED_SEMAPHORE_1,
} POWER_DS_SEMAPHORE;
</#if>
// *****************************************************************************
// *****************************************************************************
// Section: Interface
// *****************************************************************************
// *****************************************************************************

void POWER_LowPowerModeEnter( POWER_LOW_POWER_MODE mode );
<#if DEEP_SLEEP_MODE_EXIST??>
void POWER_Initialize( void );
POWER_DS_WAKEUP_SOURCE POWER_DS_WakeupSourceGet( void );
void POWER_DS_SoftwareRestore(void);
void POWER_DS_WakeupSourceClear( POWER_DS_WAKEUP_SOURCE wakeupSource );
void POWER_DS_ExtendedSemaphoreEnable(void);
void POWER_DS_ExtendedSemaphoreDisable(void);
void POWER_DS_RTCC_PowerEnable(void);
void POWER_DS_RTCC_PowerDisable(void);
void POWER_DS_RTCC_WakeupEnable(void);
void POWER_DS_RTCC_WakeupDisable(void);
void POWER_DS_SemaphoreWrite(POWER_DS_SEMAPHORE sema, uint32_t semaValue);
uint32_t POWER_DS_SemaphoreRead(POWER_DS_SEMAPHORE sema);
</#if>
// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END

#endif /* PLIB_POWER_H */
