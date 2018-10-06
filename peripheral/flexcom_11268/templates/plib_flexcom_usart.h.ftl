/*******************************************************************************
  ${FLEXCOM_INSTANCE_NAME} ${FLEXCOM_MODE} PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_${FLEXCOM_INSTANCE_NAME?lower_case}_${FLEXCOM_MODE?lower_case}.h

  Summary
    ${FLEXCOM_INSTANCE_NAME} ${FLEXCOM_MODE} peripheral library interface.

  Description
    This file defines the interface to the ${FLEXCOM_INSTANCE_NAME} ${FLEXCOM_MODE} peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

  Remarks:
    None.
*******************************************************************************/

/*******************************************************************************
Copyright (c) 2018 released Microchip Technology Inc. All rights reserved.
Microchip licenses to you the right to use, modify, copy and distribute
Software only when embedded on a Microchip microcontroller or digital signal
controller that is integrated into your product or third party product
(pursuant to the sublicense terms in the accompanying license agreement).
You should refer to the license agreement accompanying this Software for
additional information regarding your rights and obligations.
SOFTWARE AND DOCUMENTATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND,
EITHER EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION, ANY WARRANTY OF
MERCHANTABILITY, TITLE, NON-INFRINGEMENT AND FITNESS FOR A PARTICULAR PURPOSE.
IN NO EVENT SHALL MICROCHIP OR ITS LICENSORS BE LIABLE OR OBLIGATED UNDER
CONTRACT, NEGLIGENCE, STRICT LIABILITY, CONTRIBUTION, BREACH OF WARRANTY, OR
OTHER LEGAL EQUITABLE THEORY ANY DIRECT OR INDIRECT DAMAGES OR EXPENSES
INCLUDING BUT NOT LIMITED TO ANY INCIDENTAL, SPECIAL, INDIRECT, PUNITIVE OR
CONSEQUENTIAL DAMAGES, LOST PROFITS OR LOST DATA, COST OF PROCUREMENT OF
SUBSTITUTE GOODS, TECHNOLOGY, SERVICES, OR ANY CLAIMS BY THIRD PARTIES
(INCLUDING BUT NOT LIMITED TO ANY DEFENSE THEREOF), OR OTHER SIMILAR COSTS.
*******************************************************************************/

#ifndef PLIB_${FLEXCOM_INSTANCE_NAME}_${FLEXCOM_MODE}_H // Guards against multiple inclusion
#define PLIB_${FLEXCOM_INSTANCE_NAME}_${FLEXCOM_MODE}_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
/* This section lists the other files that are included in this file. */
#include "device.h"
#include "plib_flexcom_usart_local.h"

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility
extern "C" {
#endif
// DOM-IGNORE-END

<#--Interface To Use-->
// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************
#define ${FLEXCOM_INSTANCE_NAME}_USART_FrequencyGet()    (uint32_t)(${FLEX_USART_CLOCK_FREQ}UL)

/****************************** ${FLEXCOM_INSTANCE_NAME} USART API *********************************/

void ${FLEXCOM_INSTANCE_NAME}_USART_Initialize( void );

FLEXCOM_USART_ERROR ${FLEXCOM_INSTANCE_NAME}_USART_ErrorGet( void );

bool ${FLEXCOM_INSTANCE_NAME}_USART_SerialSetup( FLEXCOM_USART_SERIAL_SETUP *setup, uint32_t srcClkFreq );

bool ${FLEXCOM_INSTANCE_NAME}_USART_Write( void *buffer, const size_t size );

bool ${FLEXCOM_INSTANCE_NAME}_USART_Read( void *buffer, const size_t size );

<#if USART_INTERRUPT_MODE == false>
uint8_t ${FLEXCOM_INSTANCE_NAME}_ReadByte(void);

void ${FLEXCOM_INSTANCE_NAME}_WriteByte(uint8_t data);

void ${FLEXCOM_INSTANCE_NAME}_Sync(void);

bool ${FLEXCOM_INSTANCE_NAME}_USART_TransmitterIsReady( void );

bool ${FLEXCOM_INSTANCE_NAME}_USART_ReceiverIsReady( void );

</#if>
<#if USART_INTERRUPT_MODE == true>
bool ${FLEXCOM_INSTANCE_NAME}_USART_WriteIsBusy( void );

bool ${FLEXCOM_INSTANCE_NAME}_USART_ReadIsBusy( void );

size_t ${FLEXCOM_INSTANCE_NAME}_USART_WriteCountGet( void );

size_t ${FLEXCOM_INSTANCE_NAME}_USART_ReadCountGet( void );

bool ${FLEXCOM_INSTANCE_NAME}_USART_WriteCallbackRegister( FLEXCOM_USART_CALLBACK callback, uintptr_t context );

bool ${FLEXCOM_INSTANCE_NAME}_USART_ReadCallbackRegister( FLEXCOM_USART_CALLBACK callback, uintptr_t context );

// *****************************************************************************
// *****************************************************************************
// Section: Local: **** Do Not Use ****
// *****************************************************************************
// *****************************************************************************

void ${FLEXCOM_INSTANCE_NAME}_InterruptHandler( void );

</#if>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility
    }
#endif
// DOM-IGNORE-END

#endif //PLIB_${FLEXCOM_INSTANCE_NAME}_${FLEXCOM_MODE}_H
