/*******************************************************************************
Interface definition of ${QSPI_INSTANCE_NAME} PLIB.

 Company:
    Microchip Technology Inc.

 File Name:
    plib_${QSPI_INSTANCE_NAME?lower_case}_spi.h

 Summary:
    Interface definition of the Quad Serial Peripheral Interface Plib (${QSPI_INSTANCE_NAME})
    when operating in SPI mode.

 Description:
    This file defines the interface for the ${QSPI_INSTANCE_NAME} Plib.
    It allows user to setup ${QSPI_INSTANCE_NAME} and transfer data to and from slave devices
    attached when in SPI mode.
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

#ifndef PLIB_${QSPI_INSTANCE_NAME}_SPI_H // Guards against multiple inclusion
#define PLIB_${QSPI_INSTANCE_NAME}_SPI_H

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

bool ${QSPI_INSTANCE_NAME}_WriteRead (void* pTransmitData, size_t txSize, void* pReceiveData, size_t rxSize);

bool ${QSPI_INSTANCE_NAME}_Write(void* pTransmitData, size_t txSize);

bool ${QSPI_INSTANCE_NAME}_Read(void* pReceiveData, size_t rxSize);

bool ${QSPI_INSTANCE_NAME}_TransferSetup (QSPI_TRANSFER_SETUP * setup );

void ${QSPI_INSTANCE_NAME}_CallbackRegister (QSPI_CALLBACK callback, uintptr_t context);

bool ${QSPI_INSTANCE_NAME}_IsBusy(void);

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility
}
#endif
// DOM-IGNORE-END

#endif /* PLIB_${QSPI_INSTANCE_NAME}_SPI_H */