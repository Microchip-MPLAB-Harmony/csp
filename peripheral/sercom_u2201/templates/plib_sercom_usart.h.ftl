/*******************************************************************************
  SERCOM Universal Synchronous/Asynchrnous Receiver/Transmitter PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_${SERCOM_INSTANCE_NAME?lower_case}_usart.h

  Summary
    USART peripheral library interface.

  Description
    This file defines the interface to the USART peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

  Remarks:
    None.
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

#ifndef PLIB_${SERCOM_INSTANCE_NAME}_USART_H // Guards against multiple inclusion
#define PLIB_${SERCOM_INSTANCE_NAME}_USART_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

#include "plib_sercom_usart_common.h"

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility

	extern "C" {

#endif
// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************

void ${SERCOM_INSTANCE_NAME}_USART_Initialize( void );

bool ${SERCOM_INSTANCE_NAME}_USART_SerialSetup( USART_SERIAL_SETUP * serialSetup, uint32_t clkFrequency );

<#if USART_TX_ENABLE = true>
bool ${SERCOM_INSTANCE_NAME}_USART_Write( void *buffer, const size_t size );

<#if USART_INTERRUPT_MODE = true>
bool ${SERCOM_INSTANCE_NAME}_USART_WriteIsBusy( void );

size_t ${SERCOM_INSTANCE_NAME}_USART_WriteCountGet( void );

void ${SERCOM_INSTANCE_NAME}_USART_WriteCallbackRegister( SERCOM_USART_CALLBACK callback, uintptr_t context );
<#else>
bool ${SERCOM_INSTANCE_NAME}_USART_TransmitterIsReady( void );

bool ${SERCOM_INSTANCE_NAME}_USART_TransmitComplete( void );

void ${SERCOM_INSTANCE_NAME}_USART_WriteByte( int data );
</#if>
</#if>

<#if USART_RX_ENABLE = true>
bool ${SERCOM_INSTANCE_NAME}_USART_Read( void *buffer, const size_t size );

<#if USART_INTERRUPT_MODE = true>
bool ${SERCOM_INSTANCE_NAME}_USART_ReadIsBusy( void );

size_t ${SERCOM_INSTANCE_NAME}_USART_ReadCountGet( void );

void ${SERCOM_INSTANCE_NAME}_USART_ReadCallbackRegister( SERCOM_USART_CALLBACK callback, uintptr_t context );
<#else>
bool ${SERCOM_INSTANCE_NAME}_USART_ReceiverIsReady( void );

int ${SERCOM_INSTANCE_NAME}_USART_ReadByte( void );
</#if>
</#if>

USART_ERROR ${SERCOM_INSTANCE_NAME}_USART_ErrorGet( void );

uint32_t ${SERCOM_INSTANCE_NAME}_USART_FrequencyGet( void );

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END

#endif //PLIB_${SERCOM_INSTANCE_NAME}_USART_H
