/*******************************************************************************
  SPI PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_spi0.h

  Summary:
    SPI0 PLIB Header File

  Description:
    This file has prototype of all the interfaces provided for particular
    SPI peripheral.

*******************************************************************************/

/*******************************************************************************
Copyright (c) 2018 released Microchip Technology Inc.  All rights reserved.

Microchip licenses to you the right to use, modify, copy and distribute
Software only when embedded on a Microchip microcontroller or digital signal
controller that is integrated into your product or third party product
(pursuant to the sublicense terms in the accompanying license agreement).

You should refer to the license agreement accompanying this Software for
additional information regarding your rights and obligations.

SOFTWARE AND DOCUMENTATION ARE PROVIDED AS IS  WITHOUT  WARRANTY  OF  ANY  KIND,
EITHER EXPRESS  OR  IMPLIED,  INCLUDING  WITHOUT  LIMITATION,  ANY  WARRANTY  OF
MERCHANTABILITY, TITLE, NON-INFRINGEMENT AND FITNESS FOR A  PARTICULAR  PURPOSE.
IN NO EVENT SHALL MICROCHIP OR  ITS  LICENSORS  BE  LIABLE  OR  OBLIGATED  UNDER
CONTRACT, NEGLIGENCE, STRICT LIABILITY, CONTRIBUTION,  BREACH  OF  WARRANTY,  OR
OTHER LEGAL  EQUITABLE  THEORY  ANY  DIRECT  OR  INDIRECT  DAMAGES  OR  EXPENSES
INCLUDING BUT NOT LIMITED TO ANY  INCIDENTAL,  SPECIAL,  INDIRECT,  PUNITIVE  OR
CONSEQUENTIAL DAMAGES, LOST  PROFITS  OR  LOST  DATA,  COST  OF  PROCUREMENT  OF
SUBSTITUTE  GOODS,  TECHNOLOGY,  SERVICES,  OR  ANY  CLAIMS  BY  THIRD   PARTIES
(INCLUDING BUT NOT LIMITED TO ANY DEFENSE  THEREOF),  OR  OTHER  SIMILAR  COSTS.
*******************************************************************************/

#ifndef PLIB_SPI0_H
#define PLIB_SPI0_H

#include "device.h"
#include "plib_spi_common.h"

/* Provide C++ Compatibility */
#ifdef __cplusplus

    extern "C" {

#endif

/****************************** SPI0 Interface *********************************/

void SPI0_Initialize ( void );

bool SPI0_WriteRead (void* pTransmitData, size_t txSize, void* pReceiveData, size_t rxSize);

static inline bool SPI0_Write(void* pTransmitData, size_t txSize)
{
    return(SPI0_WriteRead(pTransmitData, txSize, NULL, 0));
}

static inline bool SPI0_Read(void* pReceiveData, size_t rxSize)
{
    return(SPI0_WriteRead(NULL, 0, pReceiveData, rxSize));
}

bool SPI0_TransferSetup (SPI_TRANSFER_SETUP *setup, uint32_t spiSourceClock);

bool SPI0_IsBusy(void);

SPI_ERROR SPI0_ErrorGet ( void );

void SPI0_CallbackRegister(const SPI_CALLBACK callback, uintptr_t context);

void SPI0_InterruptHandler(void);

/* Provide C++ Compatibility */
#ifdef __cplusplus

    }

#endif

#endif // PLIB_SPI0_H

/*******************************************************************************
 End of File
*/
