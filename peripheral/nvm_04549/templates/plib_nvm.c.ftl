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
* Copyright (C) 2024 Microchip Technology Inc. and its subsidiaries.
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
<#if core.CoreSysIntFile == true>
#include "interrupts.h"
</#if>
#include "plib_${NVM_INSTANCE_NAME?lower_case}.h"

#define  FLASH_ERASE_PAGE_SIZE_IN_INSTRUCTIONS  ${FLASH_ERASE_SIZE}U
#define  FLASH_ERASE_PAGE_MASK  (~((FLASH_ERASE_PAGE_SIZE_IN_INSTRUCTIONS * 4U) - 1U))
#define  FLASH_ADDRESS_MASK  ${NVM_WORD_WRITE_SIZE}U

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
    NVM_NO_OPERATION                      = 0x0,
    NVM_WORD_WRITE_OPERATION              = ${NVM_WORD_WRITE_OPCODE},
    NVM_ROW_WRITE_OPERATION               = ${NVM_ROW_WRITE_OPCODE},
    NVM_PAGE_ERASE_OPERATION              = ${NVM_PAGE_ERASE_OPCODE},
} NVM_OPERATION_MODE;

<#if INTERRUPT_ENABLE == true>
volatile static nvmCallbackObjType ${NVM_INSTANCE_NAME?lower_case}CallbackObj;
void __attribute__((used)) ${NVM_INSTANCE_NAME}_InterruptHandler( void );
</#if>
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
    <#lt>void ${NVM_INSTANCE_NAME}_CallbackRegister( NVM_CALLBACK callback, uintptr_t context )
    <#lt>{
    <#lt>    /* Register callback function */
    <#lt>    ${NVM_INSTANCE_NAME?lower_case}CallbackObj.CallbackFunc    = callback;
    <#lt>    ${NVM_INSTANCE_NAME?lower_case}CallbackObj.Context         = context;
    <#lt>}

    <#lt>void __attribute__((used)) ${NVM_INSTANCE_NAME}_InterruptHandler( void )
    <#lt>{
    <#lt>    _NVMIF = 0;

    <#lt>    if(${NVM_INSTANCE_NAME?lower_case}CallbackObj.CallbackFunc != NULL)
    <#lt>    {
    <#lt>        uintptr_t context = ${NVM_INSTANCE_NAME?lower_case}CallbackObj.Context;
    <#lt>        ${NVM_INSTANCE_NAME?lower_case}CallbackObj.CallbackFunc(context);
    <#lt>    }
    <#lt>}
</#if>


static void ${NVM_INSTANCE_NAME}_StartOperationAtAddress( uint32_t address,  NVM_OPERATION_MODE operation )
{
    // Set the target Flash address to be operated on (destination).
    NVMADR = address;

    // Set the flash operation:
    /***************************************************************************
     * Page erase: Erases the entire page which includes the target address
     *    (NVMADR) if it is not write-protected.
     * Quad Word (128-bit) program: Programs the 128 bit quad words in NVMDATA0
     *    through NVMDATA3 to flash address selected by NVMADR, if it they are
     *    not write-protected.
     * Row program: Programs the entire row from the physical address in
     *    NVMSRCADR to the flash address selected by NVMADR if it is not
     *    write-protected
     **************************************************************************/

    NVMCON = operation;

<#if INTERRUPT_ENABLE == true>
    //Enable interrupt just before initiating the write
    _NVMIE = 1;
</#if>

    // Initiate write operation
    NVMCONbits.WR = 1U;
}

/* ************************************************************************** */
/* ************************************************************************** */
// Section: Interface Functions                                               */
/* ************************************************************************** */
/* ************************************************************************** */

void ${NVM_INSTANCE_NAME}_Initialize( void )
{
    NVM_StartOperationAtAddress( NVMADR,  NVM_NO_OPERATION );
}


bool ${NVM_INSTANCE_NAME}_Read( uint32_t *data, uint32_t length, const uint32_t address )
{
    (void) memcpy(data, (uint32_t*)address, length);

    return true;
}

bool ${NVM_INSTANCE_NAME}_QuadWordWrite( uint32_t *data, uint32_t address )
{
   bool status = false;
   NVMDATA0 = *(data++);
   NVMDATA1 = *(data++);
   NVMDATA2 = *(data++);
   NVMDATA3 = *(data++);
   if(0U == (address % FLASH_ADDRESS_MASK))
   {
       ${NVM_INSTANCE_NAME}_StartOperationAtAddress( address,  NVM_WORD_WRITE_OPERATION);
       status = true;
   }

   return status;
}


bool ${NVM_INSTANCE_NAME}_RowWrite( uint32_t *data, uint32_t address )
{
    bool status = false;
    NVMSRCADR = (uint32_t)data;

    if(0U == (address % FLASH_ADDRESS_MASK))
    {
        ${NVM_INSTANCE_NAME}_StartOperationAtAddress( address,  NVM_ROW_WRITE_OPERATION);
        status = true;
    }

    return status;
}

bool ${NVM_INSTANCE_NAME}_PageErase( uint32_t address )
{
    address = (FLASH_ERASE_PAGE_MASK & address);
    ${NVM_INSTANCE_NAME}_StartOperationAtAddress(address,  NVM_PAGE_ERASE_OPERATION);
    return true;
}

NVM_ERROR ${NVM_INSTANCE_NAME}_ErrorGet( void )
{
    // mask for WREC and WRERR bits
    return (NVMCON & (_NVMCON_WREC_MASK | _NVMCON_WRERR_MASK));
}

bool ${NVM_INSTANCE_NAME}_IsBusy( void )
{
    return (bool)NVMCONbits.WR;
}
