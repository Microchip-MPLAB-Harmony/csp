/*******************************************************************************
Interface definition of SQI PLIB.

 Company:
    Microchip Technology Inc.

 File Name:
    plib_sqi_common.h

 Summary:
    Interface definition of the Quad Serial Peripheral Interface Plib (SQI).

 Description:
    This file defines the interface for the SQI Plib.
    It allows user to setup SQI and transfer data to and from slave devices
    attached.
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

#ifndef PLIB_SQI_COMMON_H // Guards against multiple inclusion
#define PLIB_SQI_COMMON_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

/* This section lists the other files that are included in this file.
*/
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <stdint.h>
#include <sys/attribs.h>

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


typedef void (*SQI_EVENT_HANDLER)(uintptr_t context);

typedef enum
{
    SQI_PIO_MODE = 0x1,
    SQI_DMA_MODE = 0x2,
    SQI_XIP_MODE = 0x3
} SQI_MODE;

typedef enum
{
    SINGLE_MODE = 0x0,
    DUAL_MODE   = 0x1,
    QUAD_MODE   = 0x2
} SQI_LANE_MODE;

typedef enum
{
    ZERO_ADDR_BYTES     = 0x0,
    ONE_ADDR_BYTES      = 0x1,
    TWO_ADDR_BYTES      = 0x2,
    THREE_ADDR_BYTES    = 0x3,
    FOUR_ADDR_BYTES     = 0x4,
} SQI_XIP_ADDR_BYTES;

typedef enum
{
    ZERO_DUMMY_BYTES    = 0x0,
    ONE_DUMMY_BYTES     = 0x1,
    TWO_DUMMY_BYTES     = 0x2,
    THREE_DUMMY_BYTES   = 0x3,
} SQI_XIP_DUMMY_BYTES;

typedef enum
{
    ZERO_MODE_BYTES     = 0x0,
    ONE_MODE_BYTES      = 0x1,
    TWO_MODE_BYTES      = 0x2,
    THREE_MODE_BYTES    = 0x3,
} SQI_XIP_MODE_BYTES;

typedef enum
{
    DEVICE_0            = 0x0,
    DEVICE_1            = 0x1,
} SQI_XIP_DEV_SELECT;

typedef struct sqi_dma_desc {
    uint32_t                bd_ctrl;
    uint32_t                bd_stat;
    uint32_t                *bd_bufaddr;
    struct sqi_dma_desc     *bd_nxtptr;
	uint8_t                 cache_align_dummy[16];
} sqi_dma_desc_t;

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility
}
#endif
// DOM-IGNORE-END

#endif /* PLIB_SQI_COMMON_H */
