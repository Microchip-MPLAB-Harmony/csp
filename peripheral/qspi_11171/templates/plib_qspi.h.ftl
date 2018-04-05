/*******************************************************************************
Interface definition of QSPI PLIB.

 Company:
    Microchip Technology Inc.

 File Name:
    plib_qspi.h

 Summary:
    Interface definition of the Quad Serial Peripheral Interface Plib (QSPI).

 Description:
    This file defines the interface for the QSPI Plib.
    It allows user to setup QSPI and transfer data to and from slave devices
    attached.
*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
Copyright (c) 2016 released Microchip Technology Inc. All rights reserved.

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

#ifndef PLIB_QSPI${INDEX?string}_H // Guards against multiple inclusion
#define PLIB_QSPI${INDEX?string}_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

/* This section lists the other files that are included in this file.
*/

#include "device.h"
#include "plib_qspi.h"

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility
    extern "C" {
#endif
// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Section: Data Types
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************

void QSPI${INDEX?string}_Initialize( void );

bool QSPI${INDEX?string}_CommandWrite( qspi_command_xfer_t *qspi_command_xfer, uint32_t address );

bool QSPI${INDEX?string}_RegisterRead( qspi_register_xfer_t *qspi_register_xfer, uint32_t *rx_data, uint8_t rx_data_length );

bool QSPI${INDEX?string}_RegisterWrite( qspi_register_xfer_t *qspi_register_xfer, uint32_t *tx_data, uint8_t tx_data_length );

bool QSPI${INDEX?string}_MemoryRead( qspi_memory_xfer_t *qspi_memory_xfer, uint32_t *rx_data, uint32_t rx_data_length, uint32_t address );

bool QSPI${INDEX?string}_MemoryWrite( qspi_memory_xfer_t *qspi_memory_xfer, uint32_t *tx_data, uint32_t tx_data_length, uint32_t address );

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility
}
#endif
// DOM-IGNORE-END

#endif /* PLIB_QSPI${INDEX?string}_H */
