/*******************************************************************************
  FLEXCOM2 SPI PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_flexcom2_spi.h

  Summary:
   FLEXCOM2 SPI PLIB Header File.

  Description
    This file defines the interface to the FLEXCOM SPI peripheral library.
    This library provides access to and control of the associated
    peripheral instance.

  Remarks:
    None.

*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
Copyright (c) 2018 released Microchip Technology Inc. All rights reserved.
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

#ifndef PLIB_FLEXCOM2_SPI_H // Guards against multiple inclusion
#define PLIB_FLEXCOM2_SPI_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
/* This section lists the other files that are included in this file.
*/

#include "device.h"
#include "plib_flexcom_spi_local.h"

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility

extern "C" {

#endif

// DOM-IGNORE-END

/****************************** FLEXCOM2 SPI Interface *********************************/

void FLEXCOM2_SPI_Initialize( void );
bool FLEXCOM2_SPI_WriteRead( void * pTransmitData, size_t txSize, void * pReceiveData, size_t rxSize );
bool FLEXCOM2_SPI_Write( void * pTransmitData, size_t txSize );
bool FLEXCOM2_SPI_Read( void * pReceiveData, size_t rxSize );
bool FLEXCOM2_SPI_TransferSetup( FLEXCOM_SPI_TRANSFER_SETUP * setup, uint32_t spiSourceClock );
bool FLEXCOM2_SPI_IsBusy( void );
void FLEXCOM2_SPI_CallbackRegister( FLEXCOM_SPI_CALLBACK callback, uintptr_t context );

/* Provide C++ Compatibility */
#ifdef __cplusplus

    }

#endif

#endif // PLIB_FLEXCOM2_SPI_H

/*******************************************************************************
 End of File
*/
