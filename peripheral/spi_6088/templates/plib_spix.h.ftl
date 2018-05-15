/*******************************************************************************
  SPI PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_spi${SPI_INDEX?string}.h

  Summary:
    SPI${SPI_INDEX?string} PLIB Header File

  Description:
    This file has prototype of all the interfaces provided for particular
    SPI peripheral.

*******************************************************************************/

/*******************************************************************************
Copyright (c) 2017 released Microchip Technology Inc.  All rights reserved.

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

#ifndef PLIB_SPI${SPI_INDEX?string}_H
#define PLIB_SPI${SPI_INDEX?string}_H

#include "device.h"
#include "plib_spi.h"

/* Provide C++ Compatibility */
#ifdef __cplusplus  

    extern "C" {

#endif

/****************************** SPI${SPI_INDEX?string} Interface *********************************/

void SPI${SPI_INDEX?string}_Initialize ( void );

bool SPI${SPI_INDEX?string}_WriteRead (void* pTransmitData, size_t txSize, void* pReceiveData, size_t rxSize);

static inline bool SPI${SPI_INDEX?string}_Write(void* pTransmitData, size_t txSize)
{
    return(SPI${SPI_INDEX?string}_WriteRead(pTransmitData, txSize, NULL, 0));
}

static inline bool SPI${SPI_INDEX?string}_Read(void* pReceiveData, size_t rxSize)
{
    return(SPI${SPI_INDEX?string}_WriteRead(NULL, 0, pReceiveData, rxSize));
}

bool SPI${SPI_INDEX?string}_TransferSetup (SPI_TRANSFER_SETUP *setup, uint32_t spiSourceClock);

<#if SPI_INTERRUPT_MODE == true>     
bool SPI${SPI_INDEX?string}_IsBusy(void);

SPI_ERROR SPI${SPI_INDEX?string}_ErrorGet ( void );

void SPI${SPI_INDEX?string}_CallbackRegister(const SPI_CALLBACK callback, uintptr_t context);

void SPI${SPI_INDEX?string}_InterruptHandler(void);
</#if>

/* Provide C++ Compatibility */
#ifdef __cplusplus

    }
    
#endif

#endif // PLIB_SPI${SPI_INDEX?string}_H

/*******************************************************************************
 End of File
*/