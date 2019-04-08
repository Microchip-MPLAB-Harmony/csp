/*******************************************************************************
  Non-Volatile Memory Controller(${NVMCTRL_INSTANCE_NAME}) PLIB.

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${NVMCTRL_INSTANCE_NAME?lower_case}.h

  Summary:
    Interface definition of ${NVMCTRL_INSTANCE_NAME} Plib.

  Description:
    This file defines the interface for the ${NVMCTRL_INSTANCE_NAME} Plib.
    It allows user to Program, Erase and lock the on-chip Non Volatile Flash
    Memory.
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

#ifndef PLIB_${NVMCTRL_INSTANCE_NAME}_H
#define PLIB_${NVMCTRL_INSTANCE_NAME}_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

#include "device.h"
#include <stdint.h>
#include <stdbool.h>
#include <stddef.h>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility
 extern "C" {
#endif

// DOM-IGNORE-END

#define ${NVMCTRL_INSTANCE_NAME}_FLASH_START_ADDRESS        (${.vars["FLASH_START_ADDRESS"]}U)
#define ${NVMCTRL_INSTANCE_NAME}_FLASH_SIZE                 (${FLASH_SIZE}U)
#define ${NVMCTRL_INSTANCE_NAME}_FLASH_PAGESIZE             (${FLASH_PROGRAM_SIZE}U)
#define ${NVMCTRL_INSTANCE_NAME}_FLASH_BLOCKSIZE            (${FLASH_ERASE_SIZE}U)

<#if DRV_MEMORY_CONNECTED == true>
    <#lt>#define ${NVMCTRL_INSTANCE_NAME}_START_ADDRESS              0x${START_ADDRESS}
    <#lt>#define ${NVMCTRL_INSTANCE_NAME}_MEDIA_SIZE                 ${MEMORY_MEDIA_SIZE}
    <#lt>#define ${NVMCTRL_INSTANCE_NAME}_ERASE_BUFFER_SIZE          ${ERASE_BUFFER_SIZE}
</#if>

<#if INTERRUPT_ENABLE == true || NVM_INTERRUPT1_ENABLE == true>
typedef void (*NVMCTRL_CALLBACK)(uintptr_t context);

typedef struct
{
    NVMCTRL_CALLBACK callback_fn;
    uintptr_t context;
}NVMCTRL_CALLBACK_OBJECT;
</#if>

/* NVM supports four write modes */
typedef enum
{
    NVMCTRL_WMODE_MAN = NVMCTRL_CTRLA_WMODE_MAN,
    NVMCTRL_WMODE_ADW = NVMCTRL_CTRLA_WMODE_ADW,
    NVMCTRL_WMODE_AQW = NVMCTRL_CTRLA_WMODE_AQW,
    NVMCTRL_WMODE_AP = NVMCTRL_CTRLA_WMODE_AP,
} NVMCTRL_WRITEMODE;

<#if INTERRUPT_ENABLE == true>
/* Interrupt sources for the main flash */
typedef enum
{
    NVMCTRL_INT_DONE = NVMCTRL_INTENCLR_DONE_Msk,
    NVMCTRL_INT_ADDRE = NVMCTRL_INTENCLR_ADDRE_Msk,
    NVMCTRL_INT_PROGE = NVMCTRL_INTENCLR_PROGE_Msk,
    NVMCTRL_INT_LOCKE = NVMCTRL_INTENCLR_LOCKE_Msk,
    NVMCTRL_INT_ECCSE = NVMCTRL_INTENCLR_ECCSE_Msk,
    NVMCTRL_INT_ECCDE = NVMCTRL_INTENCLR_ECCDE_Msk,
    NVMCTRL_INT_NVME = NVMCTRL_INTENCLR_NVME_Msk,
    NVMCTRL_INT_SUSP = NVMCTRL_INTENCLR_SUSP_Msk
} NVMCTRL_INTERRUPT0_SOURCE;
</#if>

<#if NVM_INTERRUPT1_ENABLE == true>
/* Interrupt sources for SmartEEPROM */
typedef enum
{
    NVMCTRL_INT_SEESFULL = NVMCTRL_INTENCLR_SEESFULL_Msk,
    NVMCTRL_INT_SEESOVF = NVMCTRL_INTENCLR_SEESOVF_Msk,
    NVMCTRL_INT_SEEWRC = NVMCTRL_INTENCLR_SEEWRC_Msk,
} NVMCTRL_INTERRUPT1_SOURCE;
</#if>

void ${NVMCTRL_INSTANCE_NAME}_Initialize(void);

bool ${NVMCTRL_INSTANCE_NAME}_Read( uint32_t *data, uint32_t length, uint32_t address );

void ${NVMCTRL_INSTANCE_NAME}_SetWriteMode(NVMCTRL_WRITEMODE mode);

bool ${NVMCTRL_INSTANCE_NAME}_QuadWordWrite(uint32_t *data, const uint32_t address);

bool ${NVMCTRL_INSTANCE_NAME}_DoubleWordWrite(uint32_t *data, const uint32_t address);

bool ${NVMCTRL_INSTANCE_NAME}_PageWrite( uint32_t* data, uint32_t address );

bool ${NVMCTRL_INSTANCE_NAME}_BlockErase( uint32_t address );

uint16_t ${NVMCTRL_INSTANCE_NAME}_ErrorGet( void );

uint16_t ${NVMCTRL_INSTANCE_NAME}_StatusGet( void );

bool ${NVMCTRL_INSTANCE_NAME}_IsBusy( void );

void ${NVMCTRL_INSTANCE_NAME}_RegionLock (uint32_t address);

void ${NVMCTRL_INSTANCE_NAME}_RegionUnlock (uint32_t address);

uint32_t ${NVMCTRL_INSTANCE_NAME}_RegionLockStatusGet (void);

bool ${NVMCTRL_INSTANCE_NAME}_SmartEEPROM_IsBusy(void);

uint16_t ${NVMCTRL_INSTANCE_NAME}_SmartEepromStatusGet( void );

bool ${NVMCTRL_INSTANCE_NAME}_SmartEEPROM_IsActiveSectorFull(void);

void ${NVMCTRL_INSTANCE_NAME}_SmartEepromSectorReallocate(void);

void ${NVMCTRL_INSTANCE_NAME}_SmartEepromFlushPageBuffer(void);

void ${NVMCTRL_INSTANCE_NAME}_BankSwap(void);

<#if INTERRUPT_ENABLE == true>
    <#lt>void ${NVMCTRL_INSTANCE_NAME}_CallbackRegister( NVMCTRL_CALLBACK callback, uintptr_t context );
    <#lt>void ${NVMCTRL_INSTANCE_NAME}_EnableMainFlashInterruptSource(NVMCTRL_INTERRUPT0_SOURCE int_source);
    <#lt>void ${NVMCTRL_INSTANCE_NAME}_DisableMainFlashInterruptSource(NVMCTRL_INTERRUPT0_SOURCE int_source);
</#if>
<#if NVM_INTERRUPT1_ENABLE == true>
    <#lt>void ${NVMCTRL_INSTANCE_NAME}_SmartEEPROMCallbackRegister( NVMCTRL_CALLBACK callback, uintptr_t context );
    <#lt>void ${NVMCTRL_INSTANCE_NAME}_EnableSmartEepromInterruptSource(NVMCTRL_INTERRUPT1_SOURCE int_source);
    <#lt>void ${NVMCTRL_INSTANCE_NAME}_DisableSmartEepromInterruptSource(NVMCTRL_INTERRUPT1_SOURCE int_source);
</#if>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility
}
#endif
// DOM-IGNORE-END
#endif // PLIB_${NVMCTRL_INSTANCE_NAME}_H
