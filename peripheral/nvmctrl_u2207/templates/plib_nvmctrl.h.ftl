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
Copyright (c) 2016 released Microchip Technology Inc.  All rights reserved.

Microchip licenses to you the right to use, modify, copy and distribute
Software only when embedded on a Microchip microcontroller or digital signal
controller that is integrated into your product or third party product
(pursuant to the sublicense terms in the accompanying license agreement).

You should refer to the license agreement accompanying this Software for
additional information regarding your rights and obligations.

SOFTWARE AND DOCUMENTATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND,
EITHER EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION, ANY WARRANTY OF
MERCHANTABILITY, TITLE, NON-INFRINGEMENT AND FITNESS FOR A PARTICULAR PURPOSE.
IN NO EVENT SHALL MICROCHIP OR ITS LICENSORS BE LIABLE OR OBLIGATED UNDER
CONTRACT, NEGLIGENCE, STRICT LIABILITY, CONTRIBUTION, BREACH OF WARRANTY, OR
OTHER LEGAL EQUITABLE THEORY ANY DIRECT OR INDIRECT DAMAGES OR EXPENSES
INCLUDING BUT NOT LIMITED TO ANY INCIDENTAL, SPECIAL, INDIRECT, PUNITIVE OR
CONSEQUENTIAL DAMAGES, LOST PROFITS OR LOST DATA, COST OF PROCUREMENT OF
SUBSTITUTE GOODS, TECHNOLOGY, SERVICES, OR ANY CLAIMS BY THIRD PARTIES
(INCLUDING BUT NOT LIMITED TO ANY DEFENSE THEREOF), OR OTHER SIMILAR COSTS.
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

#define ${NVMCTRL_INSTANCE_NAME}_FLASH_START_ADDRESS   (${.vars["FLASH_START_ADDRESS"]}U)
#define ${NVMCTRL_INSTANCE_NAME}_FLASH_SIZE            (${FLASH_SIZE}U)
#define ${NVMCTRL_INSTANCE_NAME}_FLASH_PAGESIZE        (${FLASH_PROGRAM_SIZE}U)
#define ${NVMCTRL_INSTANCE_NAME}_FLASH_ROWSIZE         (${FLASH_ERASE_SIZE}U)

<#if NVMCTRL_RWW_EEPROM == true>
    <#lt>#define ${NVMCTRL_INSTANCE_NAME}_RWWEEPROM_START_ADDRESS     (${.vars["FLASH_RWWEEPROM_START_ADDRESS"]}U)
    <#lt>#define ${NVMCTRL_INSTANCE_NAME}_RWWEEPROM_SIZE              (${FLASH_RWWEEPROM_SIZE}U)
    <#lt>#define ${NVMCTRL_INSTANCE_NAME}_RWWEEPROM_PAGESIZE          (${FLASH_RWWEEPROM_PROGRAM_SIZE}U)
    <#lt>#define ${NVMCTRL_INSTANCE_NAME}_RWWEEPROM_ROWSIZE           (${FLASH_RWWEEPROM_ERASE_SIZE}U)
</#if>

<#if DRV_MEMORY_CONNECTED == true>
    <#lt>#define ${NVMCTRL_INSTANCE_NAME}_START_ADDRESS       0x${START_ADDRESS}
    <#lt>#define ${NVMCTRL_INSTANCE_NAME}_MEDIA_SIZE          ${MEMORY_MEDIA_SIZE}
    <#lt>#define ${NVMCTRL_INSTANCE_NAME}_ERASE_BUFFER_SIZE   ${ERASE_BUFFER_SIZE}
</#if>

typedef enum
{
    /* No error */
    NVMCTRL_ERROR_NONE = 0x0,

    /* NVMCTRL invalid commands and/or bad keywords error */
    NVMCTRL_ERROR_PROG = 0x4,

    /* NVMCTRL lock error */
    NVMCTRL_ERROR_LOCK = 0x8,

    /* NVMCTRL programming or erase error */
    NVMCTRL_ERROR_NVM = 0x10,

} NVMCTRL_ERROR;

<#if INTERRUPT_ENABLE == true>
    <#lt>typedef void (*NVMCTRL_CALLBACK)(uintptr_t context);
</#if>

void ${NVMCTRL_INSTANCE_NAME}_Initialize(void);

bool ${NVMCTRL_INSTANCE_NAME}_Read( uint32_t *data, uint32_t length, uint32_t address );

bool ${NVMCTRL_INSTANCE_NAME}_PageWrite( uint32_t* data, uint32_t address );

bool ${NVMCTRL_INSTANCE_NAME}_RowErase( uint32_t address );

NVMCTRL_ERROR ${NVMCTRL_INSTANCE_NAME}_ErrorGet( void );

bool ${NVMCTRL_INSTANCE_NAME}_IsBusy( void );

<#if NVMCTRL_REGION_LOCK_UNLOCK == true>
    <#lt>void ${NVMCTRL_INSTANCE_NAME}_RegionLock (uint32_t address);

    <#lt>void ${NVMCTRL_INSTANCE_NAME}_RegionUnlock (uint32_t address);
</#if>

<#if NVMCTRL_RWW_EEPROM == true>
    <#lt>bool ${NVMCTRL_INSTANCE_NAME}_RWWEEPROM_Read( uint32_t *data, uint32_t length, const uint32_t address );
    <#lt>bool ${NVMCTRL_INSTANCE_NAME}_RWWEEPROM_PageWrite( uint32_t address, uint32_t* data );

    <#lt>bool ${NVMCTRL_INSTANCE_NAME}_RWWEEPROM_RowErase ( uint32_t address );
</#if>

<#if INTERRUPT_ENABLE == true>
    <#lt>void ${NVMCTRL_INSTANCE_NAME}_CallbackRegister ( NVMCTRL_CALLBACK callback, uintptr_t context );

    <#lt>void ${NVMCTRL_INSTANCE_NAME}_InterruptHandler(void);
</#if>

<#if NVMCTRL_CACHE_ENABLE == true>
    <#lt>void ${NVMCTRL_INSTANCE_NAME}_CacheInvalidate ( void );
</#if>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility
}
#endif
// DOM-IGNORE-END
#endif // PLIB_${NVMCTRL_INSTANCE_NAME}_H
