/*******************************************************************************
  (${RAM_INSTANCE_NAME}) PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${RAM_INSTANCE_NAME?lower_case}.h

  Summary:
    ${RAM_INSTANCE_NAME} PLIB Header file

  Description:
    This file defines the interface to the RAM peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

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

#ifndef PLIB_${RAM_INSTANCE_NAME}_H
#define PLIB_${RAM_INSTANCE_NAME}_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
/* This section lists the other files that are included in this file.
*/

#include <stdint.h>
#include <stdbool.h>
#include <stddef.h>
#include "device.h"

#ifdef __cplusplus // Provide C++ Compatibility
extern "C" {
#endif

<#if MCRAMC_ECC_TESTING_ENABLE == true>

#define ${RAM_INSTANCE_NAME}_ECC_STATUS_NONE      0U
// Single Bit Error
#define ${RAM_INSTANCE_NAME}_ECC_STATUS_SERR      MCRAMC_INTSTA_SERR_Msk
// Double Bit Error
#define ${RAM_INSTANCE_NAME}_ECC_STATUS_DERR      MCRAMC_INTSTA_DERR_Msk

typedef uint32_t ${RAM_INSTANCE_NAME}_ECC_STATUS;

typedef void (*${RAM_INSTANCE_NAME}_ECC_CALLBACK)(${RAM_INSTANCE_NAME}_ECC_STATUS status, uintptr_t context);

typedef struct
{
    ${RAM_INSTANCE_NAME}_ECC_CALLBACK callback;
    uintptr_t context;
}${RAM_INSTANCE_NAME}_ECC_CALLBACK_OBJ;

void ${RAM_INSTANCE_NAME}_ECC_Initialize(void);

void ${RAM_INSTANCE_NAME}_ECC_SingleBitFaultInject(uint32_t fltaddr, uint8_t fltBitPtr);

void ${RAM_INSTANCE_NAME}_ECC_DoubleBitFaultInject(uint32_t fltaddr, uint8_t flt1BitPtr, uint8_t flt2BitPtr);

void ${RAM_INSTANCE_NAME}_ECC_Enable(void);

void ${RAM_INSTANCE_NAME}_ECC_Disable(void);

void ${RAM_INSTANCE_NAME}_ECC_FaultEnable(void);

void ${RAM_INSTANCE_NAME}_ECC_FaultDisable(void);

uint32_t ${RAM_INSTANCE_NAME}_ECC_FaultCaptureAddrGet(void);

uint8_t ${RAM_INSTANCE_NAME}_ECC_FaultCaptureSyndromeGet(void);

uint8_t ${RAM_INSTANCE_NAME}_ECC_FaultCaptureParityGet(void);

<#if MCRAMC_ECC_SINGLE_BIT_ERR_INT_ENABLE == true || MCRAMC_ECC_DOUBLE_BIT_ERR_INT_ENABLE == true>
void ${RAM_INSTANCE_NAME}_ECC_CallbackRegister (${RAM_INSTANCE_NAME}_ECC_CALLBACK callback, uintptr_t context);
<#else>
${RAM_INSTANCE_NAME}_ECC_STATUS ${RAM_INSTANCE_NAME}_ECC_StatusGet(void);
</#if>

</#if>

bool ${RAM_INSTANCE_NAME}_Read( uint32_t *data, uint32_t length, const uint32_t address );

bool ${RAM_INSTANCE_NAME}_Write( uint32_t *data, uint32_t length, uint32_t address );

bool ${RAM_INSTANCE_NAME}_IsBusy(void);

#ifdef __cplusplus  // Provide C++ Compatibility
}
#endif

#endif /* PLIB_${RAM_INSTANCE_NAME}_H */
