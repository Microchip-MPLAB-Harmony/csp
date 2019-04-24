/*******************************************************************************
 Interface definition of ${EFC_INSTANCE_NAME} PLIB.

 Company:
    Microchip Technology Inc.

 File Name:
    plib_${EFC_INSTANCE_NAME?lower_case}.h

 Summary:
    Interface definition of ${EFC_INSTANCE_NAME} Plib.

 Description:
    This file defines the interface for the ${EFC_INSTANCE_NAME} Plib.
    It allows user to Program, Erase and lock the on-chip FLASH memory.
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

#ifndef ${EFC_INSTANCE_NAME}_H    // Guards against multiple inclusion
#define ${EFC_INSTANCE_NAME}_H

#include <stdint.h>
#include <stdbool.h>
#include <stddef.h>

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

#define ${EFC_INSTANCE_NAME}_SECTORSIZE              ${FLASH_ERASE_SIZE}
#define ${EFC_INSTANCE_NAME}_PAGESIZE                ${FLASH_PROGRAM_SIZE}
#define ${EFC_INSTANCE_NAME}_LOCKSIZE                0x4000
<#if DRV_MEMORY_CONNECTED == true>
    <#lt>#define ${EFC_INSTANCE_NAME}_START_ADDRESS           0x${START_ADDRESS}
    <#lt>#define ${EFC_INSTANCE_NAME}_MEDIA_SIZE              ${MEMORY_MEDIA_SIZE}
    <#lt>#define ${EFC_INSTANCE_NAME}_ERASE_BUFFER_SIZE       ${ERASE_BUFFER_SIZE}
</#if>


typedef enum
{
    EFC_ERROR_NONE = 0x1,
    /*In-valid command*/
    EFC_CMD_ERROR = 0x2,
    /*Flash region is locked*/
    EFC_LOCK_ERROR = 0x4,
    /*Flash Error*/
    EFC_FLERR_ERROR = 0x8,
    /*Flash Encountered an ECC error*/
    EFC_ECC_ERROR = 0xF0000,
} EFC_ERROR;

<#if INTERRUPT_ENABLE == true>
    <#lt>typedef void (*EFC_CALLBACK)(uintptr_t context);
    <#lt>typedef struct
    <#lt>{
        <#lt>    EFC_CALLBACK          callback;
        <#lt>    uintptr_t               context;
    <#lt>} EFC_OBJECT ;
</#if>

void ${EFC_INSTANCE_NAME}_Initialize(void);

bool ${EFC_INSTANCE_NAME}_Read( uint32_t *data, uint32_t length, uint32_t address );

bool ${EFC_INSTANCE_NAME}_SectorErase( uint32_t address );

bool ${EFC_INSTANCE_NAME}_PageWrite( uint32_t *data, uint32_t address );

bool ${EFC_INSTANCE_NAME}_QuadWordWrite( uint32_t *data, uint32_t address );

EFC_ERROR ${EFC_INSTANCE_NAME}_ErrorGet( void );

bool ${EFC_INSTANCE_NAME}_IsBusy(void);

void ${EFC_INSTANCE_NAME}_RegionLock(uint32_t address);

void ${EFC_INSTANCE_NAME}_RegionUnlock(uint32_t address);

<#if INTERRUPT_ENABLE == true>
    <#lt>void ${EFC_INSTANCE_NAME}_CallbackRegister( EFC_CALLBACK callback, uintptr_t context );
</#if>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility
}
#endif
// DOM-IGNORE-END

#endif
