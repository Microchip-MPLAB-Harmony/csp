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
    PROGRAM_ERASE_OPERATION                 = 0x7,
    PAGE_ERASE_OPERATION                    = 0x4,
    ROW_PROGRAM_OPERATION                   = 0x3,
    QUAD_WORD_PROGRAM_OPERATION             = 0x2,
    WORD_PROGRAM_OPERATION                  = 0x1,
    NO_OPERATION                            = 0x0,
} NVM_OPERATION_MODE;

/*******************************************
 * Internal Flash Programming Unlock Keys
 ******************************************/
typedef enum
{
    NVM_UNLOCK_KEY1 = 0xAA996655,
    NVM_UNLOCK_KEY2 = 0x556699AA
} NVM_UNLOCK_KEYS;

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
    <#lt>    if(${NVM_INSTANCE_NAME?lower_case}CallbackFunc != NULL)
    <#lt>    {
    <#lt>        ${NVM_INSTANCE_NAME?lower_case}CallbackFunc(${NVM_INSTANCE_NAME?lower_case}Context);
    <#lt>    }
    <#lt>}
</#if>

static void ${NVM_INSTANCE_NAME}_WriteUnlockSequence( void )
{
    // Write the unlock key sequence
    NVM_REGS->NVM_NVMKEY = 0x0;
    NVM_REGS->NVM_NVMKEY = NVM_UNLOCK_KEY1;
    NVM_REGS->NVM_NVMKEY = NVM_UNLOCK_KEY2;
}

static void ${NVM_INSTANCE_NAME}_StartOperationAtAddress( uint32_t address,  NVM_OPERATION_MODE operation )
{
    uint32_t old_primask = __get_PRIMASK();
    __disable_irq();

    // Set the target Flash address to be operated on (destination).
    NVM_REGS->NVM_NVMADDR = address;

    // Set the flash operation:
    /***************************************************************************
     * Page erase: Erases the entire page which includes the target address
     *    (NVMADDR) if it is not write-protected.
     * Word (32-bit) program: Programs the 32 bit word in NVMDATA0 to the flash
     *    address selected by NVMADDR, if it is not write-protected.
     * Quad Word (128-bit) program: Programs the 128 bit quad words in NVMDATA0
     *    through NVMDATA3 to flash address selected by NVMADDR, if it they are
     *    not write-protected.
     * Row program: Programs the entire row from the physical address in
     *    NVMSRCADDR to the flash address selected by NVMADDR if it is not
     *    write-protected
     **************************************************************************/

    // NVMOP can be written only when WREN is zero. So, clear WREN.
    NVM_REGS->NVM_NVMCONCLR = NVM_NVMCON_WREN_Msk;

    /* Clear and Set, as NVMCON contains status bits and hence need to be accessed atomically.
     * Using bit field access may erroneously cause status bits to get cleared */
    NVM_REGS->NVM_NVMCONCLR = NVM_NVMCON_NVMOP_Msk;
    NVM_REGS->NVM_NVMCONSET = ( NVM_NVMCON_NVMOP_Msk & (((uint32_t)operation) << NVM_NVMCON_NVMOP_Pos) );

    // Set WREN to enable writes to the WR bit and to prevent NVMOP modification
    NVM_REGS->NVM_NVMCONSET = NVM_NVMCON_WREN_Msk;

    ${NVM_INSTANCE_NAME}_WriteUnlockSequence();

    // Start the operation
    NVM_REGS->NVM_NVMCONSET = NVM_NVMCON_WR_Msk;

    __set_PRIMASK( old_primask );
}

/* ************************************************************************** */
/* ************************************************************************** */
// Section: Interface Functions                                               */
/* ************************************************************************** */
/* ************************************************************************** */

void ${NVM_INSTANCE_NAME}_Initialize( void )
{
    ${NVM_INSTANCE_NAME}_StartOperationAtAddress( NVM_REGS->NVM_NVMADDR,  NO_OPERATION );
}

bool ${NVM_INSTANCE_NAME}_Read( uint32_t *data, uint32_t length, const uint32_t address )
{
    memcpy((void *)data, (void *)address, length);

    return true;
}

bool ${NVM_INSTANCE_NAME}_WordWrite( uint32_t data, uint32_t address )
{
   NVM_REGS->NVM_NVMDATA0 = data;

   ${NVM_INSTANCE_NAME}_StartOperationAtAddress( address,  WORD_PROGRAM_OPERATION);

   return true;
}

bool ${NVM_INSTANCE_NAME}_QuadWordWrite( uint32_t *data, uint32_t address )
{
   NVM_REGS->NVM_NVMDATA0 = *(data++);
   NVM_REGS->NVM_NVMDATA1 = *(data++);
   NVM_REGS->NVM_NVMDATA2 = *(data++);
   NVM_REGS->NVM_NVMDATA3 = *(data++);

   ${NVM_INSTANCE_NAME}_StartOperationAtAddress( address,  QUAD_WORD_PROGRAM_OPERATION);

   return true;
}

bool ${NVM_INSTANCE_NAME}_RowWrite( uint32_t *data, uint32_t address )
{
   NVM_REGS->NVM_NVMSRCADDR = (uint32_t )data;

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
    return (NVM_REGS->NVM_NVMCON & (NVM_NVMCON_LVDERR_Msk | NVM_NVMCON_WRERR_Msk));
}

bool ${NVM_INSTANCE_NAME}_IsBusy( void )
{
    return (bool)((NVM_REGS->NVM_NVMCON & NVM_NVMCON_WR_Msk) >> NVM_NVMCON_WR_Pos);
}

void ${NVM_INSTANCE_NAME}_ProgramFlashWriteProtect( uint32_t laddress, uint32_t haddress )
{
    uint32_t old_primask = __get_PRIMASK();
    __disable_irq();

    ${NVM_INSTANCE_NAME}_WriteUnlockSequence();
	
	// Unlock the Program flash Write protect register
    NVM_REGS->NVM_NVMPWPLT = NVM_NVMPWPLT_ULOCK_Msk;
	NVM_REGS->NVM_NVMPWPGTESET = NVM_NVMPWPGTE_ULOCK_Msk;

    /* Program the address range */
    NVM_REGS->NVM_NVMPWPLT = (laddress & NVM_NVMPWPLT_PWPLT_Msk) | NVM_NVMPWPLT_ULOCK_Msk;
    NVM_REGS->NVM_NVMPWPGTE = (haddress & NVM_NVMPWPGTE_PWPGTE_Msk) | NVM_NVMPWPGTE_ULOCK_Msk;

    __set_PRIMASK( old_primask );
}

void ${NVM_INSTANCE_NAME}_ProgramFlashWriteProtectLock( void )
{
    uint32_t old_primask = __get_PRIMASK();
    __disable_irq();

    ${NVM_INSTANCE_NAME}_WriteUnlockSequence();

    // Lock the Program flash Write protect register
    NVM_REGS->NVM_NVMPWPLTCLR = NVM_NVMPWPLT_ULOCK_Msk;
	NVM_REGS->NVM_NVMPWPGTECLR = NVM_NVMPWPGTE_ULOCK_Msk;

    __set_PRIMASK( old_primask );
}
