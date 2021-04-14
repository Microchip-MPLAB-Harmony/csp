/*******************************************************************************
  Non-Volatile Memory Controller(${NVM_INSTANCE_NAME}) PLIB.

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${NVM_INSTANCE_NAME?lower_case}.c

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

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

#include <string.h>
#include "sys/kmem.h"
#include "plib_${NVM_INSTANCE_NAME?lower_case}.h"

/* ************************************************************************** */
/* ************************************************************************** */
/* Section: File Scope or Global Data                                         */
/* ************************************************************************** */
/* ************************************************************************** */
// *****************************************************************************

/*******************************************
 * Internal operation type
 ******************************************/
typedef enum
{
    PROGRAM_ERASE_OPERATION         = 0x7,
    PAGE_ERASE_OPERATION            = 0x4,
    ROW_PROGRAM_OPERATION           = 0x3,
    DOUBLE_WORD_PROGRAM_OPERATION   = 0x2,
    NO_OPERATION                    = 0x0,
} NVM_OPERATION_MODE;

/*******************************************
 * Internal Flash Programming Unlock Keys
 ******************************************/
typedef enum
{
    NVM_UNLOCK_KEY1 = 0xAA996655,
    NVM_UNLOCK_KEY2 = 0x556699AA
} NVM_UNLOCK_KEYS;

#define ${NVM_INSTANCE_NAME}_INTERRUPT_ENABLE_MASK   ${NVM_IEC_REG_VALUE}
#define ${NVM_INSTANCE_NAME}_INTERRUPT_FLAG_MASK     ${NVM_IFS_REG_VALUE}

/* ************************************************************************** */
/* ************************************************************************** */
// Section: Local Functions                                                   */
/* ************************************************************************** */
/* ************************************************************************** */

// *****************************************************************************
// *****************************************************************************
// Section: ${NVM_INSTANCE_NAME} Implementation
// *****************************************************************************
// *****************************************************************************

<#if INTERRUPT_ENABLE == true>
    <#lt>NVM_CALLBACK ${NVM_INSTANCE_NAME?lower_case}CallbackFunc;

    <#lt>uintptr_t ${NVM_INSTANCE_NAME?lower_case}Context;

    <#lt>void ${NVM_INSTANCE_NAME}_CallbackRegister( NVM_CALLBACK callback, uintptr_t context )
    <#lt>{
    <#lt>    /* Register callback function */
    <#lt>    ${NVM_INSTANCE_NAME?lower_case}CallbackFunc    = callback;
    <#lt>    ${NVM_INSTANCE_NAME?lower_case}Context         = context;
    <#lt>}

    <#lt>void ${NVM_INSTANCE_NAME}_InterruptHandler( void )
    <#lt>{
    <#lt>    ${NVM_IFS_REG}CLR = ${NVM_INSTANCE_NAME}_INTERRUPT_FLAG_MASK;

    <#lt>    if(${NVM_INSTANCE_NAME?lower_case}CallbackFunc != NULL)
    <#lt>    {
    <#lt>        ${NVM_INSTANCE_NAME?lower_case}CallbackFunc(${NVM_INSTANCE_NAME?lower_case}Context);
    <#lt>    }
    <#lt>}
</#if>

static void ${NVM_INSTANCE_NAME}_WriteUnlockSequence( void )
{
    // Write the unlock key sequence
    NVMKEY = 0x0;
    NVMKEY = NVM_UNLOCK_KEY1;
    NVMKEY = NVM_UNLOCK_KEY2;
}

static void ${NVM_INSTANCE_NAME}_StartOperationAtAddress( uint32_t address,  NVM_OPERATION_MODE operation )
{
    volatile uint32_t processorStatus;

    processorStatus = __builtin_disable_interrupts();

    // Set the target Flash address to be operated on (destination).
    NVMADDR = KVA_TO_PA(address);

    // Set the flash operation:
    /***************************************************************************
     * Page erase: Erases the entire page which includes the target address
     *    (NVMADDR) if it is not write-protected.
     * Double Word (64-bit) program: Programs the 64 bit quad words in NVMDATA0
     *    and NVMDATA1 to flash address selected by NVMADDR, if it they are
     *    not write-protected.
     * Row program: Programs the entire row from the physical address in
     *    NVMSRCADDR to the flash address selected by NVMADDR if it is not
     *    write-protected
     **************************************************************************/

    // NVMOP can be written only when WREN is zero. So, clear WREN.
    NVMCONCLR = _NVMCON_WREN_MASK;

    /* Clear and Set, as NVMCON contains status bits and hence need to be accessed atomically.
     * Using bit field access may erroneously cause status bits to get cleared */
    NVMCONCLR = _NVMCON_NVMOP_MASK;
    NVMCONSET = ( _NVMCON_NVMOP_MASK & (((uint32_t)operation) << _NVMCON_NVMOP_POSITION) );

    // Set WREN to enable writes to the WR bit and to prevent NVMOP modification
    NVMCONSET = _NVMCON_WREN_MASK;

    ${NVM_INSTANCE_NAME}_WriteUnlockSequence();

    // Start the operation
    NVMCONSET = _NVMCON_WR_MASK;

    __builtin_mtc0(12, 0, processorStatus);

<#if INTERRUPT_ENABLE == true>
    ${NVM_IEC_REG}SET   = ${NVM_INSTANCE_NAME}_INTERRUPT_ENABLE_MASK;
</#if>
}

/* ************************************************************************** */
/* ************************************************************************** */
// Section: Interface Functions                                               */
/* ************************************************************************** */
/* ************************************************************************** */

void ${NVM_INSTANCE_NAME}_Initialize( void )
{
    NVM_StartOperationAtAddress( NVMADDR,  NO_OPERATION );
}

bool ${NVM_INSTANCE_NAME}_Read( uint32_t *data, uint32_t length, const uint32_t address )
{
    memcpy((void *)data, (void *)KVA0_TO_KVA1(address), length);

    return true;
}

bool ${NVM_INSTANCE_NAME}_DoubleWordWrite( uint32_t *data, uint32_t address )
{
   NVMDATA0 = *(data++);
   NVMDATA1 = *(data++);

   ${NVM_INSTANCE_NAME}_StartOperationAtAddress( address,  DOUBLE_WORD_PROGRAM_OPERATION);

   return true;
}

bool ${NVM_INSTANCE_NAME}_RowWrite( uint32_t *data, uint32_t address )
{
   NVMSRCADDR = (uint32_t )KVA_TO_PA(data);

   ${NVM_INSTANCE_NAME}_StartOperationAtAddress( address,  ROW_PROGRAM_OPERATION);

   return true;
}

bool ${NVM_INSTANCE_NAME}_PageErase( uint32_t address )
{
   ${NVM_INSTANCE_NAME}_StartOperationAtAddress(address,  PAGE_ERASE_OPERATION);

   return true;
}

NVM_ERROR ${NVM_INSTANCE_NAME}_ErrorGet( void )
{
    // mask for WRERR and LVDERR bits
    return (NVMCON & (_NVMCON_LVDERR_MASK | _NVMCON_WRERR_MASK));
}

bool ${NVM_INSTANCE_NAME}_IsBusy( void )
{
    return (bool)NVMCONbits.WR;
}

void ${NVM_INSTANCE_NAME}_ProgramFlashWriteProtect( uint32_t address )
{
    volatile uint32_t processorStatus;

    processorStatus = __builtin_disable_interrupts();

    ${NVM_INSTANCE_NAME}_WriteUnlockSequence();

    /* Program the 24-Bit address till where the memory has to be protected
     * from start of flash memory.
     * The Page in which the address falls and all the lower pages below it will
     * be protected from writes
     */
    NVMPWPSET = (address & _NVMPWP_PWP_MASK);

    __builtin_mtc0(12, 0, processorStatus);
}

void ${NVM_INSTANCE_NAME}_ProgramFlashWriteProtectLock( void )
{
    volatile uint32_t processorStatus;

    processorStatus = __builtin_disable_interrupts();

    ${NVM_INSTANCE_NAME}_WriteUnlockSequence();

    // Lock the Program flash Write protect register
    NVMPWPCLR = _NVMPWP_PWPULOCK_MASK;

    __builtin_mtc0(12, 0, processorStatus);
}

void ${NVM_INSTANCE_NAME}_BootFlashWriteProtectEnable( NVM_BOOT_FLASH_WRITE_PROTECT writeProtectPage )
{
    volatile uint32_t processorStatus;

    processorStatus = __builtin_disable_interrupts();

    ${NVM_INSTANCE_NAME}_WriteUnlockSequence();

    // Protect the appropriate boot page to disable writes
    NVMBWPSET = writeProtectPage;

    __builtin_mtc0(12, 0, processorStatus);
}

void ${NVM_INSTANCE_NAME}_BootFlashWriteProtectDisable( NVM_BOOT_FLASH_WRITE_PROTECT writeProtectPage )
{
    volatile uint32_t processorStatus;

    processorStatus = __builtin_disable_interrupts();

    ${NVM_INSTANCE_NAME}_WriteUnlockSequence();

    // Un-Protect the appropriate boot page to enable writes
    NVMBWPCLR = writeProtectPage;

    __builtin_mtc0(12, 0, processorStatus);
}

void ${NVM_INSTANCE_NAME}_BootFlashWriteProtectLock()
{
    volatile uint32_t processorStatus;

    processorStatus = __builtin_disable_interrupts();

    ${NVM_INSTANCE_NAME}_WriteUnlockSequence();

    // Lock the Boot flash Write protect register
    NVMBWPCLR = _NVMBWP_BWPULOCK_MASK;

    __builtin_mtc0(12, 0, processorStatus);
}