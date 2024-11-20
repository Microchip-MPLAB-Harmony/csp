/*******************************************************************************
 Interface definition of ${SEFC_INSTANCE_NAME} PLIB.

 Company:
    Microchip Technology Inc.

 File Name:
    plib_${SEFC_INSTANCE_NAME?lower_case}.h

 Summary:
    Interface definition of ${SEFC_INSTANCE_NAME} Plib.

 Description:
    This file defines the interface for the ${SEFC_INSTANCE_NAME} Plib.
    It allows user to Program, Erase and lock the on-chip FLASH memory.
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

#ifndef ${SEFC_INSTANCE_NAME}_H    // Guards against multiple inclusion
#define ${SEFC_INSTANCE_NAME}_H

#include <sys/attribs.h>
#include "plib_sefc_common.h"

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility
    extern "C" {
#endif
// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Section: Interface
// *****************************************************************************
// *****************************************************************************

#define ${SEFC_INSTANCE_NAME}_SECTORSIZE              ${FLASH_ERASE_SIZE}U
#define ${SEFC_INSTANCE_NAME}_PAGESIZE                ${FLASH_PROGRAM_SIZE}U
#define ${SEFC_INSTANCE_NAME}_LOCKSIZE                0x4000
<#if DRV_MEMORY_CONNECTED == true>
    <#lt>#define ${SEFC_INSTANCE_NAME}_START_ADDRESS           0x${START_ADDRESS}
    <#lt>#define ${SEFC_INSTANCE_NAME}_MEDIA_SIZE              ${MEMORY_MEDIA_SIZE}
    <#lt>#define ${SEFC_INSTANCE_NAME}_ERASE_BUFFER_SIZE       ${ERASE_BUFFER_SIZE}
</#if>

void ${SEFC_INSTANCE_NAME}_Initialize(void);

bool ${SEFC_INSTANCE_NAME}_Read( uint32_t *data, uint32_t length, uint32_t address );

bool ${SEFC_INSTANCE_NAME}_SectorErase( uint32_t address );

bool ${SEFC_INSTANCE_NAME}_PageErase( uint32_t address );

bool ${SEFC_INSTANCE_NAME}_PageBufferWrite( uint32_t *data, const uint32_t address);

bool ${SEFC_INSTANCE_NAME}_PageBufferCommit( const uint32_t address);

bool ${SEFC_INSTANCE_NAME}_PageWrite( uint32_t *data, uint32_t address );

bool ${SEFC_INSTANCE_NAME}_QuadWordWrite( uint32_t *data, uint32_t address );

SEFC_ERROR ${SEFC_INSTANCE_NAME}_ErrorGet( void );

bool ${SEFC_INSTANCE_NAME}_IsBusy(void);

void ${SEFC_INSTANCE_NAME}_RegionLock(uint32_t address);

void ${SEFC_INSTANCE_NAME}_RegionUnlock(uint32_t address);

__longramfunc__ void ${SEFC_INSTANCE_NAME}_GpnvmBitSet(uint8_t GpnvmBitNumber);

__longramfunc__ void ${SEFC_INSTANCE_NAME}_GpnvmBitClear(uint8_t GpnvmBitNumber);

__longramfunc__ uint32_t ${SEFC_INSTANCE_NAME}_GpnvmBitRead(void);

bool ${SEFC_INSTANCE_NAME}_UniqueIdentifierRead(uint32_t *data, uint32_t length);

void ${SEFC_INSTANCE_NAME}_UserSignatureRightsSet(uint32_t userSignatureRights);

uint32_t ${SEFC_INSTANCE_NAME}_UserSignatureRightsGet(void);

bool ${SEFC_INSTANCE_NAME}_UserSignatureRead(uint32_t *data, uint32_t length, SEFC_USERSIGNATURE_BLOCK block, SEFC_USERSIGNATURE_PAGE page);

bool ${SEFC_INSTANCE_NAME}_UserSignatureWrite(void *data, uint32_t length, SEFC_USERSIGNATURE_BLOCK block, SEFC_USERSIGNATURE_PAGE page);

void ${SEFC_INSTANCE_NAME}_UserSignatureErase(SEFC_USERSIGNATURE_BLOCK block);

void ${SEFC_INSTANCE_NAME}_CryptographicKeySend(uint16_t sckArg);

void ${SEFC_INSTANCE_NAME}_WriteProtectionSet(uint32_t mode);

uint32_t ${SEFC_INSTANCE_NAME}_WriteProtectionGet(void);

<#if INTERRUPT_ENABLE == true>
    <#lt>void ${SEFC_INSTANCE_NAME}_CallbackRegister( SEFC_CALLBACK callback, uintptr_t context );
</#if>

<#if SEFC_DUAL_PANEL == true>
uint32_t ${SEFC_INSTANCE_NAME}_FlashPanelBaseAddrGet(void);
</#if>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility
}
#endif
// DOM-IGNORE-END

#endif
