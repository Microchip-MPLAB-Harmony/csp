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
* Copyright (C) 2018 Microchip Technology Inc. and its subsidiaries.
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

UART_ERROR ${UART_INSTANCE_NAME}_ErrorGet( void );

size_t ${UART_INSTANCE_NAME}_Write(uint8_t* pWrBuffer, const size_t size );

size_t ${UART_INSTANCE_NAME}_WriteCountGet(void);

size_t ${UART_INSTANCE_NAME}_WriteFreeBufferCountGet(void);

size_t ${UART_INSTANCE_NAME}_WriteBufferSizeGet(void);

bool ${UART_INSTANCE_NAME}_TransmitComplete(void);

bool ${UART_INSTANCE_NAME}_WriteNotificationEnable(bool isEnabled, bool isPersistent);

void ${UART_INSTANCE_NAME}_WriteThresholdSet(uint32_t nBytesThreshold);

void ${UART_INSTANCE_NAME}_WriteCallbackRegister( UART_RING_BUFFER_CALLBACK callback, uintptr_t context);

size_t ${UART_INSTANCE_NAME}_Read(uint8_t* pRdBuffer, const size_t size);

size_t ${UART_INSTANCE_NAME}_ReadCountGet(void);

size_t ${UART_INSTANCE_NAME}_ReadFreeBufferCountGet(void);

size_t ${UART_INSTANCE_NAME}_ReadBufferSizeGet(void);

bool ${UART_INSTANCE_NAME}_ReadNotificationEnable(bool isEnabled, bool isPersistent);

void ${UART_INSTANCE_NAME}_ReadThresholdSet(uint32_t nBytesThreshold);

void ${UART_INSTANCE_NAME}_ReadCallbackRegister( UART_RING_BUFFER_CALLBACK callback, uintptr_t context);

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif

// DOM-IGNORE-END
#endif // PLIB_${UART_INSTANCE_NAME}_H
