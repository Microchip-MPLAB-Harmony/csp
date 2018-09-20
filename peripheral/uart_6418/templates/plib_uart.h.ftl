/*******************************************************************************
  ${UART_INSTANCE_NAME} PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${UART_INSTANCE_NAME?lower_case}.h

  Summary:
    ${UART_INSTANCE_NAME} PLIB Header File

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

#ifndef PLIB_${UART_INSTANCE_NAME}_H
#define PLIB_${UART_INSTANCE_NAME}_H

#include "plib_uart_common.h"

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
#define ${UART_INSTANCE_NAME}_FrequencyGet()    (uint32_t)(${UART_CLOCK_FREQ}UL)

/****************************** ${UART_INSTANCE_NAME} API *********************************/

void ${UART_INSTANCE_NAME}_Initialize( void );

UART_ERROR ${UART_INSTANCE_NAME}_ErrorGet( void );

bool ${UART_INSTANCE_NAME}_SerialSetup( UART_SERIAL_SETUP *setup, uint32_t srcClkFreq );

bool ${UART_INSTANCE_NAME}_Write( void *buffer, const size_t size );

bool ${UART_INSTANCE_NAME}_Read( void *buffer, const size_t size );

<#if USART_INTERRUPT_MODE == false>
int ${UART_INSTANCE_NAME}_ReadByte( void );

void ${UART_INSTANCE_NAME}_WriteByte( int data );

void ${UART_INSTANCE_NAME}_Sync(void);

bool ${UART_INSTANCE_NAME}_TransmitterIsReady( void );

bool ${UART_INSTANCE_NAME}_ReceiverIsReady( void );

</#if>
<#if USART_INTERRUPT_MODE == true>
bool ${UART_INSTANCE_NAME}_WriteIsBusy( void );

bool ${UART_INSTANCE_NAME}_ReadIsBusy( void );

size_t ${UART_INSTANCE_NAME}_WriteCountGet( void );

size_t ${UART_INSTANCE_NAME}_ReadCountGet( void );

bool ${UART_INSTANCE_NAME}_WriteCallbackRegister( UART_CALLBACK callback, uintptr_t context );

bool ${UART_INSTANCE_NAME}_ReadCallbackRegister( UART_CALLBACK callback, uintptr_t context );

// *****************************************************************************
// *****************************************************************************
// Section: Local: **** Do Not Use ****
// *****************************************************************************
// *****************************************************************************

void ${UART_INSTANCE_NAME}_InterruptHandler( void );

</#if>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END
#endif // PLIB_${UART_INSTANCE_NAME}_H
