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
#define ${NVMCTRL_INSTANCE_NAME}_FLASH_PAGESIZE             (${FLASH_PROGRAM_SIZE}U)
#define ${NVMCTRL_INSTANCE_NAME}_FLASH_ROWSIZE              (${FLASH_ERASE_SIZE}U)


/* No error */
#define   NVMCTRL_ERROR_NONE     ( 0x0U )

/* NVMCTRL invalid commands and/or bad keywords error */
#define    NVMCTRL_ERROR_PROG    ( 0x4U )

/* NVMCTRL lock error */
#define   NVMCTRL_ERROR_LOCK     ( 0x8U )

/* NVMCTRL programming or erase error */
#define    NVMCTRL_ERROR_NVM     ( 0x10U )

typedef uint16_t NVMCTRL_ERROR;

<#if FLASH_DATAFLASH_START_ADDRESS??>
    <#lt>#define ${NVMCTRL_INSTANCE_NAME}_DATAFLASH_START_ADDRESS    (${.vars["FLASH_DATAFLASH_START_ADDRESS"]}U)
    <#lt>#define ${NVMCTRL_INSTANCE_NAME}_DATAFLASH_PAGESIZE         (${FLASH_DATAFLASH_PROGRAM_SIZE}U)
    <#lt>#define ${NVMCTRL_INSTANCE_NAME}_DATAFLASH_ROWSIZE          (${FLASH_DATAFLASH_ERASE_SIZE}U)
</#if>

<#if FLASH_USERROW_START_ADDRESS??>
    <#lt>#define ${NVMCTRL_INSTANCE_NAME}_USERROW_START_ADDRESS     (${.vars["FLASH_USERROW_START_ADDRESS"]}U)
    <#lt>#define ${NVMCTRL_INSTANCE_NAME}_USERROW_SIZE              (${FLASH_USERROW_SIZE}U)
    <#lt>#define ${NVMCTRL_INSTANCE_NAME}_USERROW_PAGESIZE          (${FLASH_USERROW_PROGRAM_SIZE}U)
</#if>

<#if DRV_MEMORY_CONNECTED == true>
    <#lt>#define ${NVMCTRL_INSTANCE_NAME}_START_ADDRESS              0x${START_ADDRESS}
    <#lt>#define ${NVMCTRL_INSTANCE_NAME}_MEDIA_SIZE                 ${MEMORY_MEDIA_SIZE}
    <#lt>#define ${NVMCTRL_INSTANCE_NAME}_ERASE_BUFFER_SIZE          ${ERASE_BUFFER_SIZE}
</#if>

<#if NVMCTRL_ECC_TESTING_ENABLE?? && NVMCTRL_ECC_TESTING_ENABLE == true>
#define ${NVMCTRL_INSTANCE_NAME}_ECC_FLT_MODE_ON_READ  (0U)
#define ${NVMCTRL_INSTANCE_NAME}_ECC_FLT_MODE_ON_WRITE (0U)

typedef uint32_t ${NVMCTRL_INSTANCE_NAME}_ECC_FLT_MODE;
</#if>


<#if INTERRUPT_ENABLE == true>
    <#lt>typedef void (*NVMCTRL_CALLBACK)(uintptr_t context);
</#if>

void ${NVMCTRL_INSTANCE_NAME}_Initialize(void);

bool ${NVMCTRL_INSTANCE_NAME}_Read( uint32_t *data, uint32_t length, const uint32_t address );

bool ${WRITE_API_NAME}( uint32_t* data, const uint32_t address );

bool ${ERASE_API_NAME}( uint32_t address );
<#if FLASH_DATAFLASH_START_ADDRESS??>

bool ${NVMCTRL_INSTANCE_NAME}_DATA_FLASH_Read( uint32_t *data, uint32_t length, const uint32_t address );

bool ${NVMCTRL_INSTANCE_NAME}_DATA_FLASH_PageWrite( uint32_t* data, const uint32_t address );

bool ${NVMCTRL_INSTANCE_NAME}_DATA_FLASH_RowErase ( uint32_t address );

</#if>
NVMCTRL_ERROR ${NVMCTRL_INSTANCE_NAME}_ErrorGet( void );

bool ${NVMCTRL_INSTANCE_NAME}_IsBusy( void );

void ${NVMCTRL_INSTANCE_NAME}_RegionLock (uint32_t address);

void ${NVMCTRL_INSTANCE_NAME}_RegionUnlock (uint32_t address);

void ${NVMCTRL_INSTANCE_NAME}_SecurityBitSet(void);

void ${NVMCTRL_INSTANCE_NAME}_ChipEraseHardLockSet(void);

<#if INTERRUPT_ENABLE == true>
    <#lt>void ${NVMCTRL_INSTANCE_NAME}_CallbackRegister ( NVMCTRL_CALLBACK callback, uintptr_t context );
</#if>

<#if NVMCTRL_WRITE_POLICY == "MANUAL">
    <#lt>bool ${NVMCTRL_INSTANCE_NAME}_PageBufferWrite( uint32_t *data, const uint32_t address);

    <#lt>bool ${NVMCTRL_INSTANCE_NAME}_PageBufferCommit( const uint32_t address);
</#if>

<#if FLASH_USERROW_START_ADDRESS??>
    <#lt>bool ${USER_ROW_WRITE_API_NAME}( uint32_t *data, const uint32_t address );

    <#lt>bool ${USER_ROW_ERASE_API_NAME}( uint32_t address );
</#if>

void ${NVMCTRL_INSTANCE_NAME}_CacheInvalidate ( void );

uint32_t ${NVMCTRL_INSTANCE_NAME}_InterruptFlagGet(void);

<#if NVMCTRL_ECC_TESTING_ENABLE?? && NVMCTRL_ECC_TESTING_ENABLE == true>
void ${NVMCTRL_INSTANCE_NAME}_ECC_SingleBitFaultInject(uint32_t fltaddr, uint8_t fltBitPtr, NVMCTRL_ECC_FLT_MODE fltOnReadOrWrite);

void ${NVMCTRL_INSTANCE_NAME}_ECC_DoubleBitFaultInject(uint32_t fltaddr, uint8_t flt1BitPtr, uint8_t flt2BitPtr, NVMCTRL_ECC_FLT_MODE fltOnReadOrWrite);

void ${NVMCTRL_INSTANCE_NAME}_ECC_MainArrayDisable(void);

void ${NVMCTRL_INSTANCE_NAME}_ECC_DataFlashDisable(void);

uint32_t ${NVMCTRL_INSTANCE_NAME}_ECC_FaultCaptureAddrGet(void);

uint8_t ${NVMCTRL_INSTANCE_NAME}_ECC_FaultSyndromeGet(void);

uint8_t ${NVMCTRL_INSTANCE_NAME}_ECC_SECIN_FaultParityGet(void);

uint8_t ${NVMCTRL_INSTANCE_NAME}_ECC_SECOUT_FaultParityGet(void);

void ${NVMCTRL_INSTANCE_NAME}_ECC_SECErrorCountSet(uint8_t errorCount);

void ${NVMCTRL_INSTANCE_NAME}_ECC_FaultLogicReset(void);
</#if>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility
}
#endif
// DOM-IGNORE-END
#endif // PLIB_${NVMCTRL_INSTANCE_NAME}_H
