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

<#if HAS_BKOUT_REG??>
typedef enum
{
    SUPC_OUTPIN_OUT0 = 0,
    SUPC_OUTPIN_OUT1 = 1
}SUPC_OUTPIN;

void ${SUPC_INSTANCE_NAME}_SetOutputPin( SUPC_OUTPIN pin );

void ${SUPC_INSTANCE_NAME}_ClearOutputPin( SUPC_OUTPIN pin );

</#if>
<#if HAS_SEL_BIT??>
typedef enum
{
    SUPC_VREGSEL_LDO = 0,
    SUPC_VREGSEL_BUCK = 1
}SUPC_VREGSEL;

void ${SUPC_INSTANCE_NAME}_SelectVoltageRegulator(SUPC_VREGSEL regsel);

</#if>

<#if SUPC_INTERRUPT_ENABLE>
typedef void (*SUPC_${SUPC_BOD_NAME}_CALLBACK)( uintptr_t context );

</#if>
void ${SUPC_INSTANCE_NAME}_Initialize( void );

<#if SUPC_INTERRUPT_ENABLE>
void ${SUPC_INSTANCE_NAME}_${SUPC_BOD_NAME}CallbackRegister( SUPC_${SUPC_BOD_NAME}_CALLBACK callback, uintptr_t context );
</#if>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END

#endif /* PLIB_${SUPC_INSTANCE_NAME}_H */
