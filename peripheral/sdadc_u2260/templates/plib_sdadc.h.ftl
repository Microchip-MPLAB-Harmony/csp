/*******************************************************************************
  SDADC${SDADC_INDEX} PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_sdadc${SDADC_INDEX}.h

  Summary:
    SDADC${SDADC_INDEX} PLIB Header file

  Description:
    This file defines the interface to the SDADC peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

*******************************************************************************/
// DOM-IGNORE-BEGIN
/*******************************************************************************
Copyright (c) 2017 released Microchip Technology Inc.  All rights reserved.

Microchip licenses to you the right to use, modify, copy and distribute
Software only when embedded on a Microchip microcontroller or digital signal
controller that is integrated into your product or third party product
(pursuant to the sublicense terms in the accompanying license agreement).

You should refer to the license agreement accompanying this Software for
additional information regarding your rights and obligations.

SOFTWARE AND DOCUMENTATION ARE PROVIDED AS IS  WITHOUT  WARRANTY  OF  ANY  KIND,
EITHER EXPRESS  OR  IMPLIED,  INCLUDING  WITHOUT  LIMITATION,  ANY  WARRANTY  OF
MERCHANTABILITY, TITLE, NON-INFRINGEMENT AND FITNESS FOR A  PARTICULAR  PURPOSE.
IN NO EVENT SHALL MICROCHIP OR  ITS  LICENSORS  BE  LIABLE  OR  OBLIGATED  UNDER
CONTRACT, NEGLIGENCE, STRICT LIABILITY, CONTRIBUTION,  BREACH  OF  WARRANTY,  OR
OTHER LEGAL  EQUITABLE  THEORY  ANY  DIRECT  OR  INDIRECT  DAMAGES  OR  EXPENSES
INCLUDING BUT NOT LIMITED TO ANY  INCIDENTAL,  SPECIAL,  INDIRECT,  PUNITIVE  OR
CONSEQUENTIAL DAMAGES, LOST  PROFITS  OR  LOST  DATA,  COST  OF  PROCUREMENT  OF
SUBSTITUTE  GOODS,  TECHNOLOGY,  SERVICES,  OR  ANY  CLAIMS  BY  THIRD   PARTIES
(INCLUDING BUT NOT LIMITED TO ANY DEFENSE  THEREOF),  OR  OTHER  SIMILAR  COSTS.
*******************************************************************************/
// DOM-IGNORE-END

#ifndef PLIB_SDADC${SDADC_INDEX}_H
#define PLIB_SDADC${SDADC_INDEX}_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
/* This section lists the other files that are included in this file.
*/

#include "plib_sdadc.h"

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

void SDADC${SDADC_INDEX}_Initialize( void );

void SDADC${SDADC_INDEX}_ConversionStart( void );

bool SDADC${SDADC_INDEX}_ConversionResultIsReady (void );

int16_t SDADC${SDADC_INDEX}_ConversionResultGet( void );

bool SDADC${SDADC_INDEX}_ConversionSequenceIsFinished(void);

void SDADC${SDADC_INDEX}_ComparisonWindowSet(int16_t low_threshold, int16_t high_threshold);

<#if SDADC_INTERRUPT_MODE == true>
void SDADC${SDADC_INDEX}_CallbackRegister(SDADC_CALLBACK callback, uintptr_t context);

void SDADC${SDADC_INDEX}_InterruptHandler( void );
</#if>


// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility
}
#endif
// DOM-IGNORE-END

#endif /* PLIB_SDADC${SDADC_INDEX}_H */