/*******************************************************************************
  FLEXCOM5 USART PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_flexcom5_usart.h

  Summary
    FLEXCOM5 USART peripheral library interface.

  Description
    This file defines the interface to the FLEXCOM5 USART peripheral library. This
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

#ifndef PLIB_FLEXCOM5_USART_H // Guards against multiple inclusion
#define PLIB_FLEXCOM5_USART_H

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

// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************
#define FLEXCOM5_USART_FrequencyGet()    (uint32_t)(200000000UL)

/****************************** FLEXCOM5 USART API *********************************/

void FLEXCOM5_USART_Initialize( void );

FLEXCOM_USART_ERROR FLEXCOM5_USART_ErrorGet( void );

bool FLEXCOM5_USART_SerialSetup( FLEXCOM_USART_SERIAL_SETUP *setup, uint32_t srcClkFreq );

bool FLEXCOM5_USART_Write( void *buffer, const size_t size );

bool FLEXCOM5_USART_Read( void *buffer, const size_t size );

bool FLEXCOM5_USART_WriteIsBusy( void );

bool FLEXCOM5_USART_ReadIsBusy( void );

size_t FLEXCOM5_USART_WriteCountGet( void );

size_t FLEXCOM5_USART_ReadCountGet( void );

void FLEXCOM5_USART_WriteCallbackRegister( FLEXCOM_USART_CALLBACK callback, uintptr_t context );

void FLEXCOM5_USART_ReadCallbackRegister( FLEXCOM_USART_CALLBACK callback, uintptr_t context );

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility
    }
#endif
// DOM-IGNORE-END

#endif //PLIB_FLEXCOM5_USART_H
