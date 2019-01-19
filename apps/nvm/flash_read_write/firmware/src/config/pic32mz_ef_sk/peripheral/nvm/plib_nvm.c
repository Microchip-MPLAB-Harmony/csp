/*******************************************************************************
  Non-Volatile Memory Controller(NVM) PLIB.

  Company:
    Microchip Technology Inc.

  File Name:
    plib_nvm.c

  Summary:
    Interface definition of NVM Plib.

  Description:
    This file defines the interface for the NVM Plib.
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

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

#include <string.h>
#include "plib_nvm.h"

/* ************************************************************************** */
/* ************************************************************************** */
/* Section: File Scope or Global Data                                         */
/* ************************************************************************** */
/* ************************************************************************** */
// *****************************************************************************

/* ************************************************************************** */
/* ************************************************************************** */
// Section: Local Functions                                                   */
/* ************************************************************************** */
/* ************************************************************************** */
// *****************************************************************************
// *****************************************************************************
// Section: NVM Implementation
// *****************************************************************************
// *****************************************************************************
/*******************************************
 * Internal operation type
 ******************************************/
typedef enum 
{
    PROGRAM_ERASE_OPERATION         = 0x7,
    UPPER_PROGRAM_ERASE_OPERATION   = 0x6,
    LOWER_PROGRAM_ERASE_OPERATION   = 0x5,
    PAGE_ERASE_OPERATION            = 0x4,
    ROW_PROGRAM_OPERATION           = 0x3,
    QUAD_WORD_PROGRAM_OPERATION      = 0x2,
    WORD_PROGRAM_OPERATION          = 0x1,
    NO_OPERATION                    = 0x0,
} NVM_OPERATION_MODE;

/*******************************************
 * Internal Flash Programming Unlock Keys
 ******************************************/
typedef enum {

    NVM_UNLOCK_KEY1 = 0xAA996655,
    NVM_UNLOCK_KEY2 = 0x556699AA

} NVM_UNLOCK_KEYS;

void NVM_StartOperationAtAddress( uint32_t address,  NVM_OPERATION_MODE operation) 
{
    // Set the target Flash address to be operated on (destination).
    NVMADDR = address;
    
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
    // Allow changing the flash operation, disallow starting the flash operation.
    NVMCONSET = _NVMCON_WREN_MASK;
    /* Clear and Set, as NVMCON contains status bits and 
       hence need to be accessed atomically.
      Using bit field access may erroneously cause status bits to get cleared */
    NVMCONCLR = _NVMCON_NVMOP_MASK;
    NVMCONSET = ( _NVMCON_NVMOP_MASK & (((uint32_t)operation) << _NVMCON_NVMOP_POSITION) );

    // DisAllow changing the flash operation, allow starting the flash operation.
    NVMCONCLR = _NVMCON_WREN_MASK;

    // Write the unlock key sequence
    NVMKEY = 0x0;
    NVMKEY = NVM_UNLOCK_KEY1;
    NVMKEY = NVM_UNLOCK_KEY2;

   // Start the operation
    NVMCONSET = _NVMCON_WR_MASK;

   // It is assumed that when the flash is busy, no reads are possible.
   // Thus, if the cpu is running out of the same flash panel, it is 
   // blocked globally. The exception to this is if code runs wholly in 
   // cache, if code runs in a second flash panel, or if code is run out
   // of RAM.
   // In which case the code should wait until the flash is NOT busy before
   // initiating another operation.  See NVM_IsBusy for more details.
}   

/* ************************************************************************** */
/* ************************************************************************** */
// Section: Interface Functions                                               */
/* ************************************************************************** */
/* ************************************************************************** */
bool NVM_Read( uint32_t *data, uint32_t length, const uint32_t address )
{
    memcpy((void *)data, (void *)address, length);
    return true;
}
bool NVM_WordWrite(uint32_t data, uint32_t address) 
{
    NVMDATA0 = (uint32_t )data;
    NVM_StartOperationAtAddress( address,  WORD_PROGRAM_OPERATION);
    return true;
}

bool NVM_QuadWordWrite(uint32_t *data, uint32_t address) 
{
   NVMDATA0 = *(data++);
   NVMDATA1 = *(data++);
   NVMDATA2 = *(data++);
   NVMDATA3 = *(data++);
   NVM_StartOperationAtAddress( address,  QUAD_WORD_PROGRAM_OPERATION);
   return true;
}

bool NVM_RowWrite(uint32_t *data, uint32_t address) 
{
   NVMSRCADDR = (uint32_t )data;
   NVM_StartOperationAtAddress( address,  ROW_PROGRAM_OPERATION);
   return true;
}

bool NVM_PageErase(uint32_t address) 
{
   NVM_StartOperationAtAddress(address,  PAGE_ERASE_OPERATION);
   return true;
}

NVM_ERROR NVM_ErrorGet( void )
{
    return (NVMCON & (_NVMCON_LVDERR_MASK | _NVMCON_WRERR_MASK));       // mask for WRERR and LVDERR bits
}

bool NVM_IsBusy( void ) 
{
    return (bool)NVMCONbits.WR;
}


/* *****************************************************************************
 End of File
 */




