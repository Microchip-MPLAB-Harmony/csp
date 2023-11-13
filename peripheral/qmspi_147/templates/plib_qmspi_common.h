/*******************************************************************************
Interface definition of QMSPI PLIB.

 Company:
    Microchip Technology Inc.

 File Name:
    plib_qmspi_common.h

 Summary:
    Interface definition of the Quad Serial Peripheral Interface Plib (QMSPI).

 Description:
    This file defines the interface for the QMSPI Plib.
    It allows user to setup QMSPI and transfer data to and from slave devices
    attached.
*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
* Copyright (C) 2022 Microchip Technology Inc. and its subsidiaries.
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

#ifndef PLIB_QMSPI_COMMON_H // Guards against multiple inclusion
#define PLIB_QMSPI_COMMON_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

/* This section lists the other files that are included in this file.
*/

#include <stdbool.h>
#include <stddef.h>

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
    QMSPI_CHIP_SELECT_0 = 0U,
    QMSPI_CHIP_SELECT_1
} QMSPI_CHIP_SELECT;

typedef enum
{
    SINGLE_BIT_SPI = 0U, /* Command(1):Address(1):Data(1) */
    DUAL_OUTPUT,         /* Command(1):Address(1):Data(2) */
    QUAD_OUTPUT,         /* Command(1):Address(1):Data(4) */
    DUAL_IO,             /* Command(1):Address(2):Data(2) */
    QUAD_IO,             /* Command(1):Address(4):Data(4) */
    DUAL_CMD,            /* Command(2):Address(2):Data(2) */
    QUAD_CMD             /* Command(4):Address(4):Data(4) */
} QMSPI_INTERFACE_MODE;

#define QMSPI_LDMA_CHANNEL_0 0U
#define QMSPI_LDMA_CHANNEL_1 1U
#define QMSPI_LDMA_CHANNEL_2 2U

typedef uint32_t QMSPI_LDMA_CHANNEL_NUM;


typedef enum
{
    QMSPI_CLOCK_PHASE_MOSI_0 = 0 << QMSPI_MODE_CHPA_MOSI_Pos,
    QMSPI_CLOCK_PHASE_MOSI_1 = 1 << QMSPI_MODE_CHPA_MOSI_Pos,

    /* Force the compiler to reserve 32-bit space for each enum value */
    QMSPI_CLOCK_PHASE_MOSI_INVALID = 0xFFFFFFFF
} QMSPI_CLOCK_PHASE_MOSI;

typedef enum
{
    QMSPI_CLOCK_PHASE_MISO_0 = 0 << QMSPI_MODE_CHPA_MISO_Pos,
    QMSPI_CLOCK_PHASE_MISO_1 = 1 << QMSPI_MODE_CHPA_MISO_Pos,

    /* Force the compiler to reserve 32-bit space for each enum value */
    QMSPI_CLOCK_PHASE_MISO_INVALID = 0xFFFFFFFF
} QMSPI_CLOCK_PHASE_MISO;

typedef enum
{
    QMSPI_CLOCK_POLARITY_IDLE_LOW = 0 << QMSPI_MODE_CPOL_Pos,
    QMSPI_CLOCK_POLARITY_IDLE_HIGH = 1 << QMSPI_MODE_CPOL_Pos,

    /* Force the compiler to reserve 32-bit space for each enum value */
    QMSPI_CLOCK_POLARITY_INVALID = 0xFFFFFFFF
} QMSPI_CLOCK_POLARITY;

typedef struct
{
    uint32_t               clockFrequency;
    QMSPI_CLOCK_PHASE_MOSI clockPhaseMOSI;
    QMSPI_CLOCK_PHASE_MISO clockPhaseMISO;
    QMSPI_CLOCK_POLARITY   clockPolarity;
} QMSPI_TRANSFER_SETUP;

typedef struct
{
    /* Command */
    uint8_t command;
    /* Address Enable */
    bool address_enable;
    /* 32-bit Address Enable */
    bool address_32_bit_en;
    /* Address */
    uint32_t address;
    /* Dummy Byte */
    uint8_t num_of_dummy_byte;
    /* QMSPI Mode */
    QMSPI_INTERFACE_MODE qmspi_ifc_mode;
} QMSPI_XFER_T;

typedef struct
{
    /* Command */
    uint8_t command;
    /* 32-bit Address Enable */
    bool address_32_bit_en;
    /* Address */
    uint32_t address;
    /* Dummy Byte */
    uint8_t num_of_dummy_byte;
    /* Local DMA Enable */
    bool ldma_enable;
    /* Local DMA Channel Number */
    QMSPI_LDMA_CHANNEL_NUM ldma_channel_num;
    /* Local DMA Increment Address Disable */
    bool ldma_incr_addr_disable;
    /* QMSPI Mode */
    QMSPI_INTERFACE_MODE qmspi_ifc_mode;
} QMSPI_DESCRIPTOR_XFER_T;

typedef  void (*QMSPI_CALLBACK) (uintptr_t context);

typedef struct
{
    QMSPI_CALLBACK callback;
    uintptr_t      context;
} QMSPI_OBJECT;



// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility
}
#endif
// DOM-IGNORE-END

#endif /* PLIB_QMSPI_COMMON_H */
