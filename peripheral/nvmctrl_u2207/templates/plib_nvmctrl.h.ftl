/*******************************************************************************
  Non-Volatile Memory Controller(NVMCTRL${NVMCTRL_INDEX?string}) PLIB.

  Company:
    Microchip Technology Inc.

  File Name:
    plib_nvmctrl${NVMCTRL_INDEX?string}.h

  Summary:
    Interface definition of NVMCTRL${NVMCTRL_INDEX?string} Plib.

  Description:
    This file defines the interface for the NVMCTRL${NVMCTRL_INDEX?string} Plib.
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

#ifndef PLIB_NVMCTRL${NVMCTRL_INDEX?string}_H
#define PLIB_NVMCTRL${NVMCTRL_INDEX?string}_H

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

#define NVMCTRL${NVMCTRL_INDEX?string}_FLASH_START_ADDRESS   (${.vars["FLASH_START_ADDRESS"]}U)
#define NVMCTRL${NVMCTRL_INDEX?string}_FLASH_SIZE            (${FLASH_SIZE}U)
#define NVMCTRL${NVMCTRL_INDEX?string}_FLASH_PAGESIZE        (${FLASH_PROGRAM_SIZE}U)
#define NVMCTRL${NVMCTRL_INDEX?string}_FLASH_ROWSIZE         (${FLASH_ERASE_SIZE}U)

<#if NVMCTRL_RWW_EEPROM == true>
    <#lt>#define NVMCTRL${NVMCTRL_INDEX?string}_RWWEEPROM_START_ADDRESS     (${.vars["FLASH_RWWEEPROM_START_ADDRESS"]}U)
    <#lt>#define NVMCTRL${NVMCTRL_INDEX?string}_RWWEEPROM_SIZE              (${FLASH_RWWEEPROM_SIZE}U)
    <#lt>#define NVMCTRL${NVMCTRL_INDEX?string}_RWWEEPROM_PAGESIZE          (${FLASH_RWWEEPROM_PROGRAM_SIZE}U)
    <#lt>#define NVMCTRL${NVMCTRL_INDEX?string}_RWWEEPROM_ROWSIZE           (${FLASH_RWWEEPROM_ERASE_SIZE}U)
</#if>

<#if DRV_MEMORY_CONNECTED == true>
    <#lt>#define NVMCTRL${NVMCTRL_INDEX?string}_START_ADDRESS       0x${START_ADDRESS}
    <#lt>#define NVMCTRL${NVMCTRL_INDEX?string}_MEDIA_SIZE          ${MEMORY_MEDIA_SIZE}
    <#lt>#define NVMCTRL${NVMCTRL_INDEX?string}_ERASE_BUFFER_SIZE   ${ERASE_BUFFER_SIZE}
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

<#if NVMCTRL_INTERRUPT_MODE == true>
    <#lt>typedef void (*NVMCTRL_CALLBACK)(uintptr_t context);
</#if>

void NVMCTRL${NVMCTRL_INDEX?string}_Initialize(void);

bool NVMCTRL${NVMCTRL_INDEX?string}_Read( uint32_t *data, uint32_t length, uint32_t address );

bool NVMCTRL${NVMCTRL_INDEX?string}_PageWrite( uint32_t* data, uint32_t address );

bool NVMCTRL${NVMCTRL_INDEX?string}_RowErase( uint32_t address );

NVMCTRL_ERROR NVMCTRL${NVMCTRL_INDEX?string}_ErrorGet( void );

bool NVMCTRL${NVMCTRL_INDEX?string}_IsBusy( void );

<#if NVMCTRL_REGION_LOCK_UNLOCK == true>
    <#lt>void NVMCTRL${NVMCTRL_INDEX?string}_RegionLock (uint32_t address);

    <#lt>void NVMCTRL${NVMCTRL_INDEX?string}_RegionUnlock (uint32_t address);
</#if>

<#if NVMCTRL_RWW_EEPROM == true>
    <#lt>bool NVMCTRL${NVMCTRL_INDEX?string}_RWWEEPROM_Read( uint32_t *data, uint32_t length, const uint32_t address );
    <#lt>bool NVMCTRL${NVMCTRL_INDEX?string}_RWWEEPROM_PageWrite( uint32_t address, uint32_t* data );

    <#lt>bool NVMCTRL${NVMCTRL_INDEX?string}_RWWEEPROM_RowErase ( uint32_t address );
</#if>

<#if NVMCTRL_INTERRUPT_MODE == true>
    <#lt>void NVMCTRL${NVMCTRL_INDEX?string}_CallbackRegister ( NVMCTRL_CALLBACK callback, uintptr_t context );

    <#lt>void NVMCTRL${NVMCTRL_INDEX?string}_InterruptHandler(void);
</#if>

<#if NVMCTRL_CACHE_ENABLE == true>
    <#lt>void NVMCTRL${NVMCTRL_INDEX?string}_CacheInvalidate ( void );
</#if>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility
}
#endif
// DOM-IGNORE-END
#endif // PLIB_NVMCTRL${NVMCTRL_INDEX?string}_H
