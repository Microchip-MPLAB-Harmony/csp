/*******************************************************************************
  Analog-to-Digital Converter(${ADC_INSTANCE_NAME}) PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_${ADC_INSTANCE_NAME?lower_case}.h

  Summary
    ${ADC_INSTANCE_NAME} PLIB Header File.

  Description
    This file defines the interface to the ADC peripheral library. This
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

#ifndef PLIB_${ADC_INSTANCE_NAME}_H      // Guards against multiple inclusion
#define PLIB_${ADC_INSTANCE_NAME}_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
/* This section lists the other files that are included in this file.
*/

#include "device.h"
#include "plib_adc_common.h"

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

void ${ADC_INSTANCE_NAME}_Initialize( void );

void ${ADC_INSTANCE_NAME}_Enable( void );

void ${ADC_INSTANCE_NAME}_Disable( void );

void ${ADC_INSTANCE_NAME}_ChannelSelect( ADC_POSINPUT positiveInput, ADC_NEGINPUT negativeInput );

void ${ADC_INSTANCE_NAME}_ConversionStart( void );

uint16_t ${ADC_INSTANCE_NAME}_ConversionResultGet( void );

void ${ADC_INSTANCE_NAME}_ComparisonWindowSet(uint16_t low_threshold, uint16_t high_threshold);

void ${ADC_INSTANCE_NAME}_WindowModeSet(ADC_WINMODE mode);

uint16_t ${ADC_INSTANCE_NAME}_LastConversionResultGet( void );

<#if ADC_INTENSET_RESRDY == true || (ADC_CTRLB_WINMODE != "0" && ADC_INTENSET_WINMON == true)>

void ${ADC_INSTANCE_NAME}_CallbackRegister( ADC_CALLBACK callback, uintptr_t context );
</#if>

<#if ADC_INTENSET_RESRDY == false>
bool ${ADC_INSTANCE_NAME}_ConversionStatusGet( void );
</#if>

<#if ADC_CTRLB_WINMODE != "0" && ADC_INTENSET_WINMON == false>
bool ${ADC_INSTANCE_NAME}_WindowMonitorStatusGet( void );
</#if>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END

#endif /* PLIB_${ADC_INSTANCE_NAME}_H */
