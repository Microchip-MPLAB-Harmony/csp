/*******************************************************************************
  ${USART_INSTANCE_NAME} SPI PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${USART_INSTANCE_NAME?lower_case}_spi.h

  Summary:
    ${USART_INSTANCE_NAME} SPI PLIB Header File

  Description:
    None

*******************************************************************************/

/*******************************************************************************
* Copyright (C) 2020 Microchip Technology Inc. and its subsidiaries.
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

#ifndef PLIB_${USART_INSTANCE_NAME}_SPI_H
#define PLIB_${USART_INSTANCE_NAME}_SPI_H

#include "plib_usart_spi_common.h"

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

/****************************** ${USART_INSTANCE_NAME} SPI API *********************************/

void ${USART_INSTANCE_NAME}_SPI_Initialize( void );

bool ${USART_INSTANCE_NAME}_SPI_TransferSetup( USART_SPI_TRANSFER_SETUP * setup, uint32_t spiSourceClock );

bool ${USART_INSTANCE_NAME}_SPI_WriteRead( void* pTransmitData, size_t txSize, void* pReceiveData, size_t rxSize );

bool ${USART_INSTANCE_NAME}_SPI_Write( void* pTransmitData, size_t txSize );

bool ${USART_INSTANCE_NAME}_SPI_Read( void* pReceiveData, size_t rxSize );

<#if USART_SPI_INTERRUPT_MODE == true >
bool ${USART_INSTANCE_NAME}_SPI_IsBusy( void );

void ${USART_INSTANCE_NAME}_SPI_CallbackRegister( USART_SPI_CALLBACK callback, uintptr_t context );
</#if>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif

// DOM-IGNORE-END
#endif // PLIB_${USART_INSTANCE_NAME}_SPI_H
