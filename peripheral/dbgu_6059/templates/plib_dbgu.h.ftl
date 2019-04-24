/*******************************************************************************
  ${DBGU_INSTANCE_NAME} PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${DBGU_INSTANCE_NAME?lower_case}.h

  Summary:
    ${DBGU_INSTANCE_NAME} PLIB Header File

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

#ifndef PLIB_${DBGU_INSTANCE_NAME}_H
#define PLIB_${DBGU_INSTANCE_NAME}_H

#include "plib_dbgu_common.h"

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    extern "C" {

#endif
// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Section: Interface
// *****************************************************************************
// *****************************************************************************
#define ${DBGU_INSTANCE_NAME}_FrequencyGet()    (uint32_t)(${DBGU_CLOCK_FREQ}UL)

/****************************** ${DBGU_INSTANCE_NAME} API *********************************/

void ${DBGU_INSTANCE_NAME}_Initialize(void);

DBGU_ERROR ${DBGU_INSTANCE_NAME}_ErrorGet(void);

bool ${DBGU_INSTANCE_NAME}_SerialSetup(DBGU_SERIAL_SETUP *setup, uint32_t srcClkFreq);

bool ${DBGU_INSTANCE_NAME}_Write(void *buffer, const size_t size);

bool ${DBGU_INSTANCE_NAME}_Read(void *buffer, const size_t size);

<#if USART_INTERRUPT_MODE == false>
uint8_t ${DBGU_INSTANCE_NAME}_ReadByte(void);

void ${DBGU_INSTANCE_NAME}_WriteByte(uint8_t data);

bool ${DBGU_INSTANCE_NAME}_TransmitterIsReady(void);

bool ${DBGU_INSTANCE_NAME}_ReceiverIsReady(void);

</#if>
<#if USART_INTERRUPT_MODE == true>
bool ${DBGU_INSTANCE_NAME}_WriteIsBusy(void);

bool ${DBGU_INSTANCE_NAME}_ReadIsBusy(void);

size_t ${DBGU_INSTANCE_NAME}_WriteCountGet(void);

size_t ${DBGU_INSTANCE_NAME}_ReadCountGet(void);

void ${DBGU_INSTANCE_NAME}_WriteCallbackRegister(DBGU_CALLBACK callback, uintptr_t context);

void ${DBGU_INSTANCE_NAME}_ReadCallbackRegister(DBGU_CALLBACK callback, uintptr_t context);

</#if>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END
#endif // PLIB_${DBGU_INSTANCE_NAME}_H
