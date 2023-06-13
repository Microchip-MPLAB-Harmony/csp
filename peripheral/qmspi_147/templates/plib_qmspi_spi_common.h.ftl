/*******************************************************************************
Interface definition of QMSPI PLIB.

 Company:
    Microchip Technology Inc.

 File Name:
    plib_qmspi_spi_common.h

 Summary:
    Interface definition of the Quad Serial Peripheral Interface Plib (QMSPI)
    configured in SPI mode.

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

#ifndef PLIB_QMSPI_SPI_COMMON_H // Guards against multiple inclusion
#define PLIB_QMSPI_SPI_COMMON_H

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
    QMSPI_SPI_CLOCK_PHASE_TRAILING_EDGE = QMSPI_MODE_CHPA_MOSI_Msk | QMSPI_MODE_CHPA_MISO_Msk,
    QMSPI_SPI_CLOCK_PHASE_LEADING_EDGE = 0,

    /* Force the compiler to reserve 32-bit space for each enum value */
    QMSPI_SPI_CLOCK_PHASE_INVALID = 0xFFFFFFFF

}QMSPI_SPI_CLOCK_PHASE;

typedef enum
{
    QMSPI_SPI_CLOCK_POLARITY_IDLE_LOW = 0,
    QMSPI_SPI_CLOCK_POLARITY_IDLE_HIGH = QMSPI_MODE_CPOL_Msk,

    /* Force the compiler to reserve 32-bit space for each enum value */
    QMSPI_SPI_CLOCK_POLARITY_INVALID = 0xFFFFFFFF

}QMSPI_SPI_CLOCK_POLARITY;

typedef struct
{
    uint32_t                    clockFrequency;
    QMSPI_SPI_CLOCK_PHASE       clockPhase;
    QMSPI_SPI_CLOCK_POLARITY    clockPolarity;

}QMSPI_SPI_TRANSFER_SETUP;

typedef  void (*QMSPI_SPI_CALLBACK) (uintptr_t context);



// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility
}
#endif
// DOM-IGNORE-END

#endif /* PLIB_QMSPI_SPI_COMMON_H */
