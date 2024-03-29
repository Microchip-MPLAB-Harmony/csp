/*******************************************************************************
  Parallel Master Port(${PMP_INSTANCE_NAME}) PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_${PMP_INSTANCE_NAME?lower_case}.h

  Summary
    ${PMP_INSTANCE_NAME} PLIB Header File.

  Description
    This file defines the interface to the PMP peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

  Remarks:
    None.

*******************************************************************************/

// DOM-IGNORE-BEGIN
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
// DOM-IGNORE-END

#ifndef PLIB_${PMP_INSTANCE_NAME}_H    // Guards against multiple inclusion
#define PLIB_${PMP_INSTANCE_NAME}_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

#include <stdbool.h>
#include <stddef.h>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility
    extern "C" {
#endif
// DOM-IGNORE-END

<#if PMP_INTERRUPT_MODE == true>

typedef void (*PMP_CALLBACK) (uintptr_t context);

typedef struct
{
    /* PMP Callback Handler */
    PMP_CALLBACK    callback;

    /* PMP Callback context */
    uintptr_t       context;

} PMP_CALLBACK_OBJ;
</#if>
// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************

void ${PMP_INSTANCE_NAME}_Initialize( void );

void ${PMP_INSTANCE_NAME}_AddressSet( uint32_t address );

uint32_t ${PMP_INSTANCE_NAME}_AddressGet( void );

void ${PMP_INSTANCE_NAME}_MasterSend( uint32_t data );

uint32_t ${PMP_INSTANCE_NAME}_MasterReceive( void );

bool ${PMP_INSTANCE_NAME}_PortIsBusy( void );

void ${PMP_INSTANCE_NAME}_AddressPortEnable( uint32_t portfunctions );

void ${PMP_INSTANCE_NAME}_AddressPortDisable( uint32_t portfunctions );

<#if PMP_INTERRUPT_MODE == true>
void ${PMP_INSTANCE_NAME}_CallbackRegister(PMP_CALLBACK callback, uintptr_t context);
</#if>
// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END

#endif /* PLIB_${PMP_INSTANCE_NAME}_H */
