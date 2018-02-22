/*******************************************************************************
  USART${INDEX?string} PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_usart${INDEX?string}.h

  Summary:
    USART${INDEX?string} PLIB Header File

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

#ifndef PLIB_USART${INDEX?string}_H
#define PLIB_USART${INDEX?string}_H

#include "plib_usart.h"

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

/****************************** USART${INDEX?string} API *********************************/

void USART${INDEX?string}_Initialize( void );

USART_ERROR USART${INDEX?string}_ErrorGet( void );

size_t USART${INDEX?string}_Write( void *buffer, const size_t size );

size_t USART${INDEX?string}_Read( void *buffer, const size_t size );

<#if INTERRUPT_MODE == false>
bool USART${INDEX?string}_TransmitterIsReady( void );

bool USART${INDEX?string}_ReceiverIsReady( void );

</#if>
<#if INTERRUPT_MODE == true>
bool USART${INDEX?string}_WriteIsBusy( void );

bool USART${INDEX?string}_ReadIsBusy( void );

size_t USART${INDEX?string}_WriteCountGet( void );

size_t USART${INDEX?string}_ReadCountGet( void );

bool USART${INDEX?string}_WriteCallbackRegister( USART_CALLBACK callback, uintptr_t context );

bool USART${INDEX?string}_ReadCallbackRegister( USART_CALLBACK callback, uintptr_t context );

// *****************************************************************************
// *****************************************************************************
// Section: Local: **** Do Not Use ****
// *****************************************************************************
// *****************************************************************************

void USART${INDEX?string}_InterruptHandler( void );

</#if>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END
#endif // PLIB_USART${INDEX?string}_H
