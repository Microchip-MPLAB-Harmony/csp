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
  EEPROM Peripheral Library Interface Header File

  Company:
    Microchip Technology Inc.

  File Name:
    plib_eeprom.h

  Summary:
    EEPROM PLIB Header File

  Description:
    None

*******************************************************************************/

#ifndef _PLIB_EEPROM_H
#define _PLIB_EEPROM_H

#include <stddef.h>
#include <stdbool.h>
#include <stdint.h>
#include "device.h"

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility
    extern "C" {
#endif
// DOM-IGNORE-END

typedef enum
{
    /* No error */
    EEPROM_ERROR_NONE = 0x0,

    /* 11 = A BOR event has occurred
     * 10 = An attempted execution of a read or write operation with an invalid write OR command with a misaligned address (EEADDR<1:0> != 00)
     * 01 = A Bulk or Page Erase or a Word Program verify error has occurred
     * 00 = No error condition */
    EEPROM_ERROR_STATUS = _EECON_ERR_MASK,

} EEPROM_ERROR;

// *****************************************************************************
// Section: Interface
// *****************************************************************************
// *****************************************************************************

/********************************** EEPROM API ********************************/
// *****************************************************************************

void EEPROM_Initialize ( void );

bool EEPROM_WordRead ( uint32_t addr, uint32_t *data );

bool EEPROM_WordWrite ( uint32_t addr, uint32_t data );

bool EEPROM_PageErase ( uint32_t addr );

bool EEPROM_BulkErase ( void );

bool EEPROM_IsBusy( void );

EEPROM_ERROR EEPROM_ErrorGet( void );

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility
    }
#endif

// DOM-IGNORE-END
#endif // _PLIB_EEPROM_H
