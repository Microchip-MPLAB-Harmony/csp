/*******************************************************************************
  Cyclic Redundancy Check (${CRC_INSTANCE_NAME}) PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${CRC_INSTANCE_NAME?lower_case}.h

  Summary:
    ${CRC_INSTANCE_NAME} PLIB Header file

  Description:
    This file defines the interface to the CRC peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

*******************************************************************************/
// DOM-IGNORE-BEGIN
/*******************************************************************************
* Copyright (C) 2021 Microchip Technology Inc. and its subsidiaries.
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

#ifndef PLIB_${CRC_INSTANCE_NAME}_H
#define PLIB_${CRC_INSTANCE_NAME}_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
/* This section lists the other files that are included in this file.
*/

#include <stdint.h>
#include <stdbool.h>
#include <stddef.h>
#include "device.h"

#ifdef __cplusplus // Provide C++ Compatibility
extern "C" {
#endif

typedef enum
{
    /* 8 Bit FIFO Depth. */
    CRC_DATA_WIDTH_BYTE     = 8,

    /* 16 Bit FIFO Depth. */
    CRC_DATA_WIDTH_HWORD    = 16,

    /* 32 Bit FIFO Depth. */
    CRC_DATA_WIDTH_WORD     = 32,

} CRC_DATA_WIDTH;

typedef struct
{
    /* CRCCON[LENDIAN]: The input data is bit reversed (reflected input) when enabled */
    bool reverse_crc_input;

    /* CRCCON[PLEN]: Determines the length of the polynomial Example: 16, 32 */
    uint8_t polynomial_length;

    /* CRCXOR: Polynomial for calculating the CRC */
    uint32_t polynomial;

    /* The calculated CRC is bit reversed (reflected output) before final XOR */
    bool reverse_crc_output;

    /* The XOR value used to generate final CRC output */
    uint32_t final_xor_value;
} CRC_SETUP;

void ${CRC_INSTANCE_NAME}_CRCSetup(CRC_SETUP CRCSetup);

uint32_t ${CRC_INSTANCE_NAME}_CRCCalculate(void *buffer, uint32_t length, uint32_t seed);

void ${CRC_INSTANCE_NAME}_CRCEnable( bool enable);

#ifdef __cplusplus  // Provide C++ Compatibility
}
#endif

#endif /* PLIB_${CRC_INSTANCE_NAME}_H */
