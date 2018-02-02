/*******************************************************************************
  SPI Plib

  Company:
    Microchip Technology Inc.

  File Name:
    plib_spi.h

  Summary:
    SPI Plib Header File

  Description:
    None

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

#ifndef PLIB_SPI_H
#define PLIB_SPI_H

#include <xc.h>
#include <stdint.h>
#include <stdbool.h>
#include <stddef.h>
#include <sys/attribs.h>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    extern "C" {

#endif
// DOM-IGNORE-END


// *****************************************************************************
// *****************************************************************************
// Section: Interface
// *****************************************************************************
// *****************************************************************************

typedef struct
{
    uint32_t    baudRate;
    bool        clockPhase;
    bool        clockPolarity;
}SPI_CONFIG;

typedef enum 
{
    SPI_UNDERRUN_ERROR  = 1 << 10,
    SPI_OVERRUN_ERROR = 1 << 3,
    SPI_MODE_FAULT_ERROR = 1 << 2,
    SPI_ERROR_NONE = 0
}SPI_ERROR;

typedef enum
{
    /* Peripheral is busy and cannot accept new request */
    SPI_EXCHANGE_BUSY,
    
    /* Previous request is completed successfully and can accept new request */
    SPI_EXCHANGE_SUCCESS,
    
    /* Error occurred in processing the previous request and can accept new request */
    SPI_EXCHANGE_ERROR
    
}SPI_EXCHANGE_STATUS;


typedef  void (*SPI_EVENT_HANDLER) (SPI_EXCHANGE_STATUS exchangeStatus,  void* context);


// *****************************************************************************
// *****************************************************************************
// Section: Local: **** Do Not Use ****
// *****************************************************************************
// *****************************************************************************

typedef struct
{
    uint8_t *               txBuffer;    
    uint8_t *               rxBuffer;
    size_t                  exchangeSize;
    size_t                  exchangedCount;
    SPI_EXCHANGE_STATUS     exchangeStatus;
    
    bool                    dataInProgress;
    
    SPI_EVENT_HANDLER       callback; 
    void*                   context;
    SPI_ERROR               error;

} SPI_OBJECT ;


// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END
#endif // PLIB_SPI_H

/*******************************************************************************
 End of File
*/