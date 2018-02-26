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

#include <stdint.h>
#include <stdbool.h>
#include <stddef.h>

/* Provide C++ Compatibility */
#ifdef __cplusplus  

    extern "C" {

#endif

/****************************** SPI${SPI_INDEX?string} Interface *********************************/
typedef struct
{
    uint32_t    baudRate;
    bool        clockPhase;
    bool        clockPolarity;
    
}SPI_SETUP;

typedef enum 
{
    SPI_ERROR_NONE = 0,
    SPI_OVERRUN_ERROR = 1 << 3

}SPI_ERROR;

void SPI${SPI_INDEX?string}_Initialize ( void );

bool SPI${SPI_INDEX?string}_Exchange(void* pTransmitData,void* pReceiveData, size_t wordSize);

SPI_ERROR SPI${SPI_INDEX?string}_ErrorGet ( void );

void SPI${SPI_INDEX?string}_Setup ( SPI_SETUP * spiSetup );

<#if SPI_INTERRUPT_MODE == true>     
bool SPI${SPI_INDEX?string}_IsBusy(void);

typedef  void (*SPI_EVENT_HANDLER) (void* context);

void SPI${SPI_INDEX?string}_CallbackRegister(const SPI_EVENT_HANDLER eventHandler, void* context);

void SPI${SPI_INDEX?string}_InterruptHandler(void);   


// *****************************************************************************
// *****************************************************************************
// Section: Local: **** Do Not Use ****
// *****************************************************************************
// *****************************************************************************

typedef struct
{
    void*                   txBuffer;    
    void*                   rxBuffer;
    size_t                  exchangeSize;
    size_t                  rxCount;
    size_t                  txCount;
    bool                    exchangeIsBusy;
    SPI_EVENT_HANDLER       callback; 
    void*                   context;
} SPI_OBJECT ;
</#if>

/* Provide C++ Compatibility */
#ifdef __cplusplus

    }
    
#endif

#endif // PLIB_SPI${SPI_INDEX?string}_H

/*******************************************************************************
 End of File
*/