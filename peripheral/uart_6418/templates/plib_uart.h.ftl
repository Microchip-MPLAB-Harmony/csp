/*******************************************************************************
  UART${INDEX?string} PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_uart${INDEX?string}.h

  Summary:
    UART${INDEX?string} PLIB Header File

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

#ifndef PLIB_UART${INDEX?string}_H
#define PLIB_UART${INDEX?string}_H

#include "plib_uart.h"

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

/****************************** UART${INDEX?string} API *********************************/

void UART${INDEX?string}_Initialize( void );

UART_ERROR UART${INDEX?string}_ErrorGet( void );

size_t UART${INDEX?string}_Write( void *buffer, const size_t size );

size_t UART${INDEX?string}_Read( void *buffer, const size_t size );

<#if INTERRUPT_MODE == false>
bool UART${INDEX?string}_TransmitterIsReady( void );

bool UART${INDEX?string}_ReceiverIsReady( void );

</#if>
<#if INTERRUPT_MODE == true>
bool UART${INDEX?string}_WriteIsBusy( void );

bool UART${INDEX?string}_ReadIsBusy( void );

size_t UART${INDEX?string}_WriteCountGet( void );

size_t UART${INDEX?string}_ReadCountGet( void );

bool UART${INDEX?string}_WriteCallbackRegister( UART_CALLBACK callback, uintptr_t context );

bool UART${INDEX?string}_ReadCallbackRegister( UART_CALLBACK callback, uintptr_t context );

// *****************************************************************************
// *****************************************************************************
// Section: Local: **** Do Not Use ****
// *****************************************************************************
// *****************************************************************************

void UART${INDEX?string}_InterruptHandler( void );

</#if>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END
#endif // PLIB_UART${INDEX?string}_H
