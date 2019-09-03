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

/*******************************************************************************
  EEPROM Peripheral Library (PLIB)

  Company:
    Microchip Technology Inc.

  File Name:
    plib_eeprom.c

  Summary:
    EEPROM Source File

  Description:
    None

*******************************************************************************/
#include "plib_eeprom.h"

#define EEPROM_32BIT_BOUNDRY    0xFFC

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
    EEPROM_STATE_NOT_READY      = 0x0,  // Data EEPROM is not ready for access
    EEPROM_STATE_READY          = 0x1,  // Data EEPROM is ready for access
} EEPROM_READY_STATE;

typedef enum
{
    EEPROM_READ_WRITE_COMPLETED = 0x0,
    EEPROM_READ_WRITE_START     = 0x1,
} EEPROM_READ_WRITE_CTRL;

typedef enum
{
    EEPROM_DISABLE_PROGRAM      = 0x0,
    EEPROM_ENABLE_PROGRAM       = 0x1,
} EEPROM_WRITE_ENABLE;

typedef enum
{
    EEPROM_DISABLE              = 0x0,
    EEPROM_ENABLE               = 0x1,
} EEPROM_POWER_CTRL;

typedef enum
{
    EEPROM_WORD_READ_OPERATION      = 0x0,  // Word Read command (WREN bit must be clear)
    EEPROM_WORD_WRITE_OPERATION     = 0x1,  // Word Write command (WREN bit must be set)
    EEPROM_PAGE_ERASE_OPERATION     = 0x2,  // Data EEPROM memory Page Erase command (WREN bit must be set)
    EEPROM_BULK_ERASE_OPERATION     = 0x3,  // Data EEPROM memory Bulk Erase command (WREN bit must be set)
    EEPROM_CONFIG_WRITE_OPERATION   = 0x4,  // Configuration register Write command (WREN bit must be set)
    EEPROM_RESERVED_OPERATION       = 0x7,  // Reserved
} EEPROM_OPERATION_MODE;

/*******************************************
 * Internal Flash Programming Unlock Keys
 ******************************************/
typedef enum
{
    EEPROM_UNLOCK_KEY1 = 0xEDB7,
    EEPROM_UNLOCK_KEY2 = 0x1248
} EEPROM_UNLOCK_KEYS;

// *****************************************************************************

// *****************************************************************************
// Section: EEPROM Implementation
// *****************************************************************************
// *****************************************************************************

static void EEPROM_WriteExecute( bool waitForDone )
{
    volatile uint32_t processorStatus;

    processorStatus = __builtin_disable_interrupts();

    EEKEY    = EEPROM_UNLOCK_KEY1;
    EEKEY    = EEPROM_UNLOCK_KEY2;
    EECONSET = _EECON_RW_MASK;

    __builtin_mtc0(12, 0, processorStatus);

    if ( waitForDone == true )
        while ( EECONbits.RW == EEPROM_READ_WRITE_START );
}

void EEPROM_Initialize (void)
{
    /* Before accessing the Data EEPROM, configure the number of Wait states */
    CFGCON2bits.EEWS = 2;

    EECONbits.ON = EEPROM_ENABLE;                       // Turn on the EEPROM

    while ( EECONbits.RDY == EEPROM_STATE_NOT_READY );  // Wait until EEPROM is ready (~125 us)

    EECONSET = _EECON_WREN_MASK;                        // Enable writing to the EEPROM

    EECONbits.CMD = EEPROM_CONFIG_WRITE_OPERATION;      // Set the command to Configuration Write

    EEADDR = 0x00;                                      // Addr 0x00 = DEVEE0;
    EEDATA = DEVEE0;
    EEPROM_WriteExecute( true );                        // Execute write and wait for finish

    EEADDR = 0x04;                                      // Addr 0x04 = DEVEE1;
    EEDATA = DEVEE1;
    EEPROM_WriteExecute( true );                        // Execute write and wait for finish

    EEADDR = 0x08;                                      // Addr 0x08 = DEVEE2;
    EEDATA = DEVEE2;
    EEPROM_WriteExecute( true );                        // Execute write and wait for finish

    EEADDR = 0x0C;                                      // Addr 0x0C = DEVEE3;
    EEDATA = DEVEE3;
    EEPROM_WriteExecute( true );                        // Execute write and wait for finish


    EECONCLR = _EECON_WREN_MASK;                        // Turn off writes.
}

bool EEPROM_WordRead( uint32_t addr, uint32_t *data )
{
    bool result = false;

    if (EEPROM_IsBusy() == false)
    {
        EEADDR          = addr & EEPROM_32BIT_BOUNDRY;
        EECONbits.CMD   = EEPROM_WORD_READ_OPERATION;

        EECONCLR = _EECON_WREN_MASK;
        EECONSET = _EECON_RW_MASK;

        while ( EECONbits.RW == EEPROM_READ_WRITE_START );
        *data = EEDATA;

        result = true;
    }

    return (result);
}

bool EEPROM_WordWrite(uint32_t addr, uint32_t data)
{
    bool result = false;

    if (EEPROM_IsBusy() == false)
    {
        EEADDR          = addr & EEPROM_32BIT_BOUNDRY;
        EECONbits.CMD   = EEPROM_WORD_WRITE_OPERATION;
        EECONSET = _EECON_WREN_MASK;
        EEDATA   = data;

        EEPROM_WriteExecute( true );

        result = true;
    }

    return (result);
}

bool EEPROM_PageErase(uint32_t addr)
{
    bool result = false;

    if (EEPROM_IsBusy() == false)
    {
        EEADDR          = addr;
        EECONbits.CMD   = EEPROM_PAGE_ERASE_OPERATION;
        EECONSET        = _EECON_WREN_MASK;

        EEPROM_WriteExecute( true );

        result = true;
    }

    return (result);
}

bool EEPROM_BulkErase(void)
{
    bool result = false;

    if (EEPROM_IsBusy() == false)
    {
        EECONbits.CMD   = EEPROM_BULK_ERASE_OPERATION;
        EECONSET        = _EECON_WREN_MASK;

        EEPROM_WriteExecute( true );

        result = true;
    }

    return (result);
}

EEPROM_ERROR EEPROM_ErrorGet( void )
{
    return (EECON & (_EECON_ERR_MASK));
}

bool EEPROM_IsBusy( void )
{
    if ( EECONbits.RW == EEPROM_READ_WRITE_COMPLETED)
        return false;

    return true;
}