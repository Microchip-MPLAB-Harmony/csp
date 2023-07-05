/*******************************************************************************
  Temperature Sensor (${TSENS_INSTANCE_NAME}) PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_${TSENS_INSTANCE_NAME?lower_case}.h

  Summary
    ${TSENS_INSTANCE_NAME} PLIB Header File.

  Description
    This file defines the interface to the TSENS peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

  Remarks:
    None.

*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
* Copyright (C) 2023 Microchip Technology Inc. and its subsidiaries.
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

#ifndef PLIB_${TSENS_INSTANCE_NAME}_H      // Guards against multiple inclusion
#define PLIB_${TSENS_INSTANCE_NAME}_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
/* This section lists the other files that are included in this file.
*/

#include "device.h"
#include "plib_tsens_common.h"

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C Compatibility

    extern "C" {

#endif
// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Section: Data Types
// *****************************************************************************
// *****************************************************************************
/* The following data type definitions are used by the functions in this
    interface and should be considered part it.
*/

// *****************************************************************************


// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************
/* The following functions make up the methods (set of possible operations) of
    this interface.
*/

void ${TSENS_INSTANCE_NAME}_Initialize( void );

void ${TSENS_INSTANCE_NAME}_Enable( void );

void ${TSENS_INSTANCE_NAME}_Disable( void );

void ${TSENS_INSTANCE_NAME}_ConversionStart( void );

uint32_t ${TSENS_INSTANCE_NAME}_ConversionResultGet( void );

void ${TSENS_INSTANCE_NAME}_ComparisonWindowSet(uint32_t low_threshold, uint32_t high_threshold);

void ${TSENS_INSTANCE_NAME}_WindowModeSet(TSENS_WINMODE mode);

void ${TSENS_INSTANCE_NAME}_InterruptsClear(TSENS_STATUS interruptMask);

void ${TSENS_INSTANCE_NAME}_InterruptsEnable(TSENS_STATUS interruptMask);

void ${TSENS_INSTANCE_NAME}_InterruptsDisable(TSENS_STATUS interruptMask);

<#if TSENS_INTENSET_RESRDY == true || (TSENS_CTRLC_WINMODE != "0" && TSENS_INTENSET_WINMON == true)>

void ${TSENS_INSTANCE_NAME}_CallbackRegister( TSENS_CALLBACK callback, uintptr_t context );
</#if>

<#if TSENS_INTENSET_RESRDY == false>
bool ${TSENS_INSTANCE_NAME}_ConversionStatusGet( void );
</#if>

<#if TSENS_CTRLC_WINMODE != "0" && TSENS_INTENSET_WINMON == false>
bool ${TSENS_INSTANCE_NAME}_WindowMonitorStatusGet( void );
</#if>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END

#endif /* PLIB_${TSENS_INSTANCE_NAME}_H */
