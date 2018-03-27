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

#ifndef PLIB_QSPI_H // Guards against multiple inclusion
#define PLIB_QSPI_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

/* This section lists the other files that are included in this file.
*/

#include <stdbool.h>

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

typedef enum
{
    ADDRL_24_BIT = QSPI_IFR_ADDRL__24_BIT,
    ADDRL_32_BIT = QSPI_IFR_ADDRL__32_BIT
} QSPI_ADDRESS_LENGTH;

typedef enum
{
    SINGLE_BIT_SPI = QSPI_IFR_WIDTH_SINGLE_BIT_SPI,
    DUAL_OUTPUT = QSPI_IFR_WIDTH_DUAL_OUTPUT,
    QUAD_OUTPUT = QSPI_IFR_WIDTH_QUAD_OUTPUT,
    DUAL_IO = QSPI_IFR_WIDTH_DUAL_IO,
    QUAD_IO = QSPI_IFR_WIDTH_QUAD_IO,
    DUAL_CMD = QSPI_IFR_WIDTH_DUAL_CMD,
    QUAD_CMD = QSPI_IFR_WIDTH_QUAD_CMD	
} QSPI_LANE_WIDTH;

typedef enum
{
    OPTL_1_BIT = QSPI_IFR_OPTL_OPTION_1BIT,
    OPTL_2_BIT = QSPI_IFR_OPTL_OPTION_2BIT,
    OPTL_4_BIT = QSPI_IFR_OPTL_OPTION_4BIT,
    OPTL_8_BIT = QSPI_IFR_OPTL_OPTION_8BIT
} QSPI_OPTION_LENGTH;

typedef struct {
    /* QSPI instruction code */
    uint8_t instruction;
    /* QSPI instruction Frame register informations */
    QSPI_LANE_WIDTH width;
    bool addr_en;
    QSPI_ADDRESS_LENGTH addr_len;
} qspi_command_xfer_t;

typedef struct {
    /* QSPI instruction code */
    uint8_t instruction;
    /* QSPI instruction Frame register informations */
    QSPI_LANE_WIDTH width;
    /* For Read Register */
    uint8_t dummy_cycles;
} qspi_register_xfer_t;

typedef struct {
    /* QSPI instruction code */
    uint8_t instruction;
    /* QSPI option code */
    uint8_t option;
    /* QSPI instruction Frame register informations */
    QSPI_LANE_WIDTH width;
    QSPI_ADDRESS_LENGTH addr_len;
    bool option_en;
    QSPI_OPTION_LENGTH option_len;
    /* For Read memory */
    uint8_t dummy_cycles;
} qspi_memory_xfer_t;


// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility
}
#endif
// DOM-IGNORE-END

#endif /* PLIB_QSPI_H */
