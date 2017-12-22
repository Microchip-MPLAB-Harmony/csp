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

#ifndef _PLIB_USART_H
#define _PLIB_USART_H

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

<#--Interface To Use-->
// *****************************************************************************
// *****************************************************************************
// Section: Interface
// *****************************************************************************
// *****************************************************************************

typedef enum
{
    USART_ERROR_NONE = 0x00000000,
    USART_ERROR_OVERRUN = 0x00000020,
    USART_ERROR_PARITY = 0x00000080,
    USART_ERROR_FRAMING = 0x00000040

} USART_ERROR;

typedef enum
{
    USART_DIRECTION_TX,
    USART_DIRECTION_RX

} USART_DIRECTION;

typedef enum
{
    USART_TRANSFER_IDLE,
    USART_TRANSFER_PROCESSING,
    USART_TRANSFER_COMPLETE,
    USART_TRANSFER_ERROR,

} USART_TRANSFER_STATUS;

typedef void (* USART_CALLBACK)( USART_TRANSFER_STATUS status, USART_DIRECTION direction, uintptr_t context );

// *****************************************************************************
/* USART PLIB API Set for Higher Layers

  Summary:
  The set of PLIB APIs used by the driver.

  Description:
  The API set holds the function names available at the PLIb level for the 
  corresponding functionality. Driver may call these functions to make use of
  the features provided by the PLIB. For example, USART driver may call USART 
  PLIB initialize function to setup the specific instance of the USART 
  peripheral.

  Remarks:
    None.
*/

typedef struct
{
    /* Pointer to initialize the peripheral */
    void(*initialize)(void);
    
    /* Pointer to read a buffer from the peripheral */
    int32_t(*read)(void *buffer, const size_t size);
    
    /* Pointer to write a buffer to the peripheral */
    int32_t(*write)(void *buffer, const size_t size);

    /* Pointer to register a callback with the peripheral */
    void(*callbackRegister)(USART_CALLBACK callback, uintptr_t context);
    
    /* Pointer to get the processed length of buffer from the peripheral */
    size_t(*transferCountGet)(USART_DIRECTION direction);

} USART_PLIB_API;


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
    USART_TRANSFER_STATUS   txStatus;
    
    uint8_t *               rxBuffer;
    size_t                  rxSize;
    size_t                  rxProcessedSize;
    USART_TRANSFER_STATUS   rxStatus;
    
    USART_CALLBACK          callback; 
    uintptr_t               context;
    USART_ERROR             error;

} USART_OBJECT ;

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END
#endif // _PLIB_USART_H
