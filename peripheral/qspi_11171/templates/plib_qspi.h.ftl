/*******************************************************************************
Interface definition of ${QSPI_INSTANCE_NAME} PLIB.

 Company:
    Microchip Technology Inc.

 File Name:
    plib_${QSPI_INSTANCE_NAME?lower_case}.h

 Summary:
    Interface definition of the Quad Serial Peripheral Interface Plib (${QSPI_INSTANCE_NAME}).

 Description:
    This file defines the interface for the ${QSPI_INSTANCE_NAME} Plib.
    It allows user to setup ${QSPI_INSTANCE_NAME} and transfer data to and from slave devices
    attached.
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

#ifndef PLIB_${QSPI_INSTANCE_NAME}_H // Guards against multiple inclusion
#define PLIB_${QSPI_INSTANCE_NAME}_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

/* This section lists the other files that are included in this file.
*/

#include "device.h"
#include "plib_qspi_common.h"

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

void ${QSPI_INSTANCE_NAME}_Initialize( void );

bool ${QSPI_INSTANCE_NAME}_CommandWrite( qspi_command_xfer_t *qspi_command_xfer, uint32_t address );

bool ${QSPI_INSTANCE_NAME}_RegisterRead( qspi_register_xfer_t *qspi_register_xfer, uint32_t *rx_data, uint8_t rx_data_length );

bool ${QSPI_INSTANCE_NAME}_RegisterWrite( qspi_register_xfer_t *qspi_register_xfer, uint32_t *tx_data, uint8_t tx_data_length );

bool ${QSPI_INSTANCE_NAME}_MemoryRead( qspi_memory_xfer_t *qspi_memory_xfer, uint32_t *rx_data, uint32_t rx_data_length, uint32_t address );

bool ${QSPI_INSTANCE_NAME}_MemoryWrite( qspi_memory_xfer_t *qspi_memory_xfer, uint32_t *tx_data, uint32_t tx_data_length, uint32_t address );

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility
}
#endif
// DOM-IGNORE-END

#endif /* PLIB_${QSPI_INSTANCE_NAME}_H */
