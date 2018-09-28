/*******************************************************************************
  USART PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_usart.h

  Summary:
    USART PLIB Global Header File

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

#ifndef PLIB_USART_H
#define PLIB_USART_H

#include <stddef.h>
#include <stdbool.h>
#include <stdint.h>

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

typedef enum
{
    USART_ERROR_NONE = 0,
    USART_ERROR_OVERRUN = US_CSR_OVRE_Msk,
    USART_ERROR_PARITY = US_CSR_PARE_Msk,
    USART_ERROR_FRAMING = US_CSR_FRAME_Msk

} USART_ERROR;

typedef enum
{
    USART_DATA_5_BIT = US_MR_CHRL_5_BIT,
    USART_DATA_6_BIT = US_MR_CHRL_6_BIT,
    USART_DATA_7_BIT = US_MR_CHRL_7_BIT,
    USART_DATA_8_BIT = US_MR_CHRL_8_BIT,
    USART_DATA_9_BIT = US_MR_MODE9_Msk

} USART_DATA;

typedef enum
{
    USART_PARITY_NONE = US_MR_PAR_NO,
    USART_PARITY_ODD = US_MR_PAR_ODD,
    USART_PARITY_EVEN = US_MR_PAR_EVEN,
    USART_PARITY_MARK = US_MR_PAR_MARK,
    USART_PARITY_SPACE = US_MR_PAR_SPACE,
    USART_PARITY_MULTIDROP = US_MR_PAR_MULTIDROP

} USART_PARITY;

typedef enum
{
    USART_STOP_1_BIT = US_MR_NBSTOP_1_BIT,
    USART_STOP_1_5_BIT = US_MR_NBSTOP_1_5_BIT,
    USART_STOP_2_BIT = US_MR_NBSTOP_2_BIT

} USART_STOP;

typedef struct
{
    uint32_t baudRate;
    USART_DATA dataWidth;
    USART_PARITY parity;
    USART_STOP stopBits;

} USART_SERIAL_SETUP;

typedef void (* USART_CALLBACK)( uintptr_t context );


// *****************************************************************************
// *****************************************************************************
// Section: Local: **** Do Not Use ****
// *****************************************************************************
// *****************************************************************************

typedef struct
{
    uint8_t *               txBuffer;
    size_t                  txSize;
    size_t                  txProcessedSize;
    USART_CALLBACK          txCallback;
    uintptr_t               txContext;
    bool                    txBusyStatus;

    uint8_t *               rxBuffer;
    size_t                  rxSize;
    size_t                  rxProcessedSize;
    USART_CALLBACK          rxCallback;
    uintptr_t               rxContext;
    bool                    rxBusyStatus;

} USART_OBJECT ;

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END
#endif // PLIB_USART_H
