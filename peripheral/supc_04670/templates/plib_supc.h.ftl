/*******************************************************************************
  Supply Controller (SUPC) Peripheral Library (PLIB)

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${SUPC_INSTANCE_NAME?lower_case}.h

  Summary:
    Interface definition of the SUPC PLIB Header File

  Description:
    None

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

#ifndef PLIB_${SUPC_INSTANCE_NAME}_H // Guards against multiple inclusion
#define PLIB_${SUPC_INSTANCE_NAME}_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

#include "device.h"

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
typedef enum
{
<#list 0..(SYS_GPBR_REGISTER - 1) as i>
    GPBR_REGS_${i},

</#list>
} GPBR_REGS_INDEX;
<#if CPU_CORE_ID?? && CPU_CORE_ID == 0>

typedef enum
{
    WAITMODE_WKUP_RTT = PMC_FSMR_RTTAL_Msk,      // RTT

    WAITMODE_WKUP_RTC = PMC_FSMR_RTCAL_Msk      // RTC

} WAITMODE_WKUP_SOURCE;

typedef enum
{
    WAITMODE_FLASH_STANDBY = PMC_FSMR_FLPM_FLASH_STANDBY,

    WAITMODE_FLASH_DEEPSLEEP = PMC_FSMR_FLPM_FLASH_DEEP_POWERDOWN

} WAITMODE_FLASH_STATE;

<#if SUPC_IER_VDD3V3SMEV || SUPC_IER_VBATSMEV || SUPC_IER_LPDBC0 || SUPC_IER_LPDBC1 || SUPC_IER_LPDBC2 || SUPC_IER_LPDBC3 || SUPC_IER_LPDBC4>
typedef void (*SUPC_CALLBACK)(uint32_t supc_status, uintptr_t context);

typedef struct
{
    SUPC_CALLBACK callback;
    uintptr_t     context;
} SUPC_OBJECT;

</#if>
</#if>
// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************
<#if CPU_CORE_ID?? && CPU_CORE_ID == 0>

void ${SUPC_INSTANCE_NAME}_Initialize(void);

void ${SUPC_INSTANCE_NAME}_SleepModeEnter(void);

void ${SUPC_INSTANCE_NAME}_WaitModeEnter(WAITMODE_FLASH_STATE flash_lpm, WAITMODE_WKUP_SOURCE source);

void ${SUPC_INSTANCE_NAME}_BackupModeEnter(void);

<#if SUPC_IER_VDD3V3SMEV || SUPC_IER_VBATSMEV || SUPC_IER_LPDBC0 || SUPC_IER_LPDBC1 || SUPC_IER_LPDBC2 || SUPC_IER_LPDBC3 || SUPC_IER_LPDBC4>
void ${SUPC_INSTANCE_NAME}_CallbackRegister(SUPC_CALLBACK callback, uintptr_t context);

</#if>
</#if>
uint32_t ${SUPC_INSTANCE_NAME}_GPBRRead(GPBR_REGS_INDEX reg);

void ${SUPC_INSTANCE_NAME}_GPBRWrite(GPBR_REGS_INDEX reg, uint32_t data);



// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END

#endif // PLIB_${SUPC_INSTANCE_NAME}_H
