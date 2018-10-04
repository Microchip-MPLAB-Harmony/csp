/*******************************************************************************
  ${SDADC_INSTANCE_NAME} PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${SDADC_INSTANCE_NAME?lower_case}.h

  Summary:
    ${SDADC_INSTANCE_NAME} PLIB Header file

  Description:
    This file defines the interface to the SDADC peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

*******************************************************************************/
// DOM-IGNORE-BEGIN
/*******************************************************************************
* © 2018 Microchip Technology Inc. and its subsidiaries.
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

#ifndef PLIB_${SDADC_INSTANCE_NAME}_H
#define PLIB_${SDADC_INSTANCE_NAME}_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
/* This section lists the other files that are included in this file.
*/

#include "plib_sdadc_common.h"

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility
extern "C" {
#endif
// DOM-IGNORE-END

<#assign SDADC_INTERRUPT_MODE = false>
<#if SDADC_INTENSET_RESRDY == true>
<#assign SDADC_INTERRUPT_MODE = true>
</#if>
<#if (SDADC_WINCTRL_WINMODE != "0") && SDADC_INTENSET_WINMON == true>
<#assign SDADC_INTERRUPT_MODE = true>
</#if>

// *****************************************************************************
// *****************************************************************************
// Section: Global data
// *****************************************************************************
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************


// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************
/* The following functions make up the methods (set of possible operations) of
    this interface.
*/

// *****************************************************************************

void ${SDADC_INSTANCE_NAME}_Initialize( void );

void ${SDADC_INSTANCE_NAME}_ConversionStart( void );

bool ${SDADC_INSTANCE_NAME}_ConversionResultIsReady (void );

int16_t ${SDADC_INSTANCE_NAME}_ConversionResultGet( void );

bool ${SDADC_INSTANCE_NAME}_ConversionSequenceIsFinished(void);

void ${SDADC_INSTANCE_NAME}_ComparisonWindowSet(int16_t low_threshold, int16_t high_threshold);

<#if SDADC_INTERRUPT_MODE == true>
void ${SDADC_INSTANCE_NAME}_CallbackRegister(SDADC_CALLBACK callback, uintptr_t context);

void ${SDADC_INSTANCE_NAME}_InterruptHandler( void );
</#if>


// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility
}
#endif
// DOM-IGNORE-END

#endif /* PLIB_${SDADC_INSTANCE_NAME}_H */
