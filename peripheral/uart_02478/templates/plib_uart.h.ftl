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
* Copyright (C) 2019 Microchip Technology Inc. and its subsidiaries.
*
* Subject to your compliance with these terms, you may use Microchip software
* and any derivatives exclusively with Microchip products. It is your
* responsibility to comply with third party license terms applicable to your
* use of third party software (including open source software) that may
* accompany Microchip software.
*
* THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS". NO WARRANTIES, WHETHER
* EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS SOFTWARE, INCLUDING ANY IMPLIED
* WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A
* PARTICULAR PURPOSE.
*
* IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL, PUNITIVE,
* INCIDENTAL OR CONSEQUENTIAL LOSS, DAMAGE, COST OR EXPENSE OF ANY KIND
* WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF MICROCHIP HAS
* BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO THE
* FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL CLAIMS IN
* ANY WAY RELATED TO THIS SOFTWARE WILL NOT EXCEED THE AMOUNT OF FEES, IF ANY,
* THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS SOFTWARE.
*******************************************************************************/

#ifndef PLIB_${UART_INSTANCE_NAME}_H
#define PLIB_${UART_INSTANCE_NAME}_H

#include <stddef.h>
#include <stdbool.h>
#include <stdint.h>
#include "device.h"
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

bool ${UART_INSTANCE_NAME}_SerialSetup( UART_SERIAL_SETUP *setup, uint32_t srcClkFreq );

bool ${UART_INSTANCE_NAME}_Write( void *buffer, const size_t size );

bool ${UART_INSTANCE_NAME}_Read( void *buffer, const size_t size );

UART_ERROR ${UART_INSTANCE_NAME}_ErrorGet( void );

<#if USART_INTERRUPT_MODE == true>
bool ${UART_INSTANCE_NAME}_ReadIsBusy( void );

size_t ${UART_INSTANCE_NAME}_ReadCountGet( void );

bool ${UART_INSTANCE_NAME}_WriteIsBusy( void );

size_t ${UART_INSTANCE_NAME}_WriteCountGet( void );

void ${UART_INSTANCE_NAME}_WriteCallbackRegister( UART_CALLBACK callback, uintptr_t context );

void ${UART_INSTANCE_NAME}_ReadCallbackRegister( UART_CALLBACK callback, uintptr_t context );
<#else>
int ${UART_INSTANCE_NAME}_ReadByte( void );

bool ${UART_INSTANCE_NAME}_ReceiverIsReady( void );

void ${UART_INSTANCE_NAME}_WriteByte( int data );

bool ${UART_INSTANCE_NAME}_TransmitterIsReady( void );
</#if>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END

#endif // PLIB_${UART_INSTANCE_NAME}_H
