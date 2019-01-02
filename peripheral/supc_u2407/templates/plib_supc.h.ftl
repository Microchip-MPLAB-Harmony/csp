/*******************************************************************************
  Supply Controller(${SUPC_INSTANCE_NAME}) PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_${SUPC_INSTANCE_NAME?lower_case}.h

  Summary
    ${SUPC_INSTANCE_NAME} Header File.

  Description
    This file defines the interface to the SUPC peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

  Remarks:
    None.

*******************************************************************************/

// DOM-IGNORE-BEGIN
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
// DOM-IGNORE-END

#ifndef PLIB_${SUPC_INSTANCE_NAME}_H    // Guards against multiple inclusion
#define PLIB_${SUPC_INSTANCE_NAME}_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
/* This section lists the other files that are included in this file.
*/

#include <stddef.h>
#include <stdbool.h>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility

    extern "C" {

#endif
// DOM-IGNORE-END

typedef enum
{
    OUT0 = 0,
    OUT1 = 1
}SUPC_OUTPIN;

typedef enum
{
    PTAT = 0,
    CTAT = 1
}SUPC_TSSEL;

void ${SUPC_INSTANCE_NAME}_SelectTempSenorChannel( SUPC_TSSEL sensor );

void ${SUPC_INSTANCE_NAME}_SetOutputPin( SUPC_OUTPIN pin );

void ${SUPC_INSTANCE_NAME}_ClearOutputPin( SUPC_OUTPIN pin );

<#if SUPC_INTERRUPT_ENABLE = true>
typedef void (*SUPC_BOD33_CALLBACK)( uintptr_t context );
</#if>

void ${SUPC_INSTANCE_NAME}_Initialize( void );

<#if SUPC_INTERRUPT_ENABLE = true>
void ${SUPC_INSTANCE_NAME}_BOD33CallbackRegister( SUPC_BOD33_CALLBACK callback, uintptr_t context );
</#if>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END

#endif /* PLIB_${SUPC_INSTANCE_NAME}_H */