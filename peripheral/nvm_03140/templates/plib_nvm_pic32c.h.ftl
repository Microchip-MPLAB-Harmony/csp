/*******************************************************************************
  Non-Volatile Memory Controller(${NVM_INSTANCE_NAME}) PLIB.

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${NVM_INSTANCE_NAME?lower_case}.h

  Summary:
    Interface definition of ${NVM_INSTANCE_NAME} Plib.

  Description:
    This file defines the interface for the ${NVM_INSTANCE_NAME} Plib.
    It allows user to Program, Erase and lock the on-chip Non Volatile Flash
    Memory.

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

#ifndef PLIB_${NVM_INSTANCE_NAME}_H
#define PLIB_${NVM_INSTANCE_NAME}_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

#include "device.h"     // For device registers and uint32_t
#include <stdbool.h>    // For bool

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility

    extern "C" {

#endif

// DOM-IGNORE-END

#define ${NVM_INSTANCE_NAME}_FLASH_START_ADDRESS    (${.vars["FLASH_START_ADDRESS"]}U)
#ifndef ${NVM_INSTANCE_NAME}_FLASH_SIZE
#define ${NVM_INSTANCE_NAME}_FLASH_SIZE             (${FLASH_SIZE}U)
#endif
#define ${NVM_INSTANCE_NAME}_FLASH_ROWSIZE          (${FLASH_PROGRAM_SIZE}U)
#define ${NVM_INSTANCE_NAME}_FLASH_PAGESIZE         (${FLASH_ERASE_SIZE}U)


/* No error */
#define    NVM_ERROR_NONE      ( 0x0U )

/* NVM write error */
#define    NVM_ERROR_WRITE     ( NVM_NVMCON_WRERR_Msk )

/* NVM Low Voltage Detect error */
#define    NVM_ERROR_LOWVOLTAGE ( NVM_NVMCON_LVDERR_Msk )

typedef uint32_t NVM_ERROR;

<#if DRV_MEMORY_CONNECTED == true>
    <#lt>#define ${NVM_INSTANCE_NAME}_START_ADDRESS              0x${START_ADDRESS}
    <#lt>#define ${NVM_INSTANCE_NAME}_MEDIA_SIZE                 ${MEMORY_MEDIA_SIZE}
    <#lt>#define ${NVM_INSTANCE_NAME}_ERASE_BUFFER_SIZE          ${ERASE_BUFFER_SIZE}
</#if>


<#if INTERRUPT_ENABLE == true>
    <#lt>typedef void (*NVM_CALLBACK)(uintptr_t context);
</#if>

void ${NVM_INSTANCE_NAME}_Initialize( void );

bool ${NVM_INSTANCE_NAME}_Read( uint32_t *data, uint32_t length, const uint32_t address );

<#if FLASH_WRITE_WORD_SIZE == "32_BITS">
bool ${NVM_INSTANCE_NAME}_WordWrite( uint32_t data, uint32_t address );

bool ${NVM_INSTANCE_NAME}_QuadWordWrite( uint32_t *data, uint32_t address );
<#else>
bool ${NVM_INSTANCE_NAME}_SingleDoubleWordWrite( uint32_t *data, uint32_t address );

bool ${NVM_INSTANCE_NAME}_QuadDoubleWordWrite( uint32_t *data, uint32_t address );
</#if>

bool ${NVM_INSTANCE_NAME}_RowWrite( uint32_t *data, uint32_t address );

bool ${NVM_INSTANCE_NAME}_PageErase( uint32_t address );

NVM_ERROR ${NVM_INSTANCE_NAME}_ErrorGet( void );

bool ${NVM_INSTANCE_NAME}_IsBusy( void );

void ${NVM_INSTANCE_NAME}_ProgramFlashWriteProtect( uint32_t laddress, uint32_t haddress);

void ${NVM_INSTANCE_NAME}_ProgramFlashWriteProtectLock( void );

void ${NVM_INSTANCE_NAME}_BootFlashWriteProtectUnlock( uint32_t bootFlashPagesMsk );

void ${NVM_INSTANCE_NAME}_BootFlashWriteProtectLock( uint32_t bootFlashPagesMsk );

<#if INTERRUPT_ENABLE == true>
    <#lt>void ${NVM_INSTANCE_NAME}_CallbackRegister( NVM_CALLBACK callback, uintptr_t context );
</#if>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility

    }

#endif

// DOM-IGNORE-END
#endif // PLIB_${NVM_INSTANCE_NAME}_H
