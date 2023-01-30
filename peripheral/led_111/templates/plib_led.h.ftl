/*******************************************************************************
  Breathing/Blinking Peripheral Library Interface Header File

  Company
    Microchip Technology Inc.

  File Name
    plib_${LED_INSTANCE_NAME?lower_case}.h

  Summary
    ${LED_INSTANCE_NAME} peripheral library interface.

  Description
    This file defines the interface to the Breathing/Blinking peripheral library.  This
    library provides access to and control of the associated peripheral
    instance.

******************************************************************************/

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

#ifndef PLIB_${LED_INSTANCE_NAME}_H    // Guards against multiple inclusion
#define PLIB_${LED_INSTANCE_NAME}_H


// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

/*  This section lists the other files that are included in this file.
*/

#include "plib_led_common.h"
#include "device.h"

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

extern "C" {

#endif

// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Section: Data Types
// *****************************************************************************
// *****************************************************************************
/*  The following data type definitions are used by the functions in this
    interface and should be considered part it.
*/

// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************
/* The following functions make up the methods (set of possible operations) of
   this interface.
*/
void ${LED_INSTANCE_NAME}_Initialize(void);

<#if LED_MODE == "LED_BREATHING">
void ${LED_INSTANCE_NAME}_DutyCycleMinSet(uint8_t min);

void ${LED_INSTANCE_NAME}_DutyCycleMaxSet(uint8_t max);

void ${LED_INSTANCE_NAME}_LowDelaySet(uint16_t ld);

void ${LED_INSTANCE_NAME}_HighDelaySet(uint16_t hd);

void ${LED_INSTANCE_NAME}_SymmetrySet(LED_SYM sym);

void ${LED_INSTANCE_NAME}_SegmentsStepSizeSet(uint32_t stepSzVal);

void ${LED_INSTANCE_NAME}_SegmentsIntervalSet(uint32_t intervalVal);

<#else>
void ${LED_INSTANCE_NAME}_ClockPrescalerSet(uint16_t prescaler);

void ${LED_INSTANCE_NAME}_DutyCycleCountSet(uint8_t dutyCycle);

<#if LED_CLK_SRC == "0x1">
void ${LED_INSTANCE_NAME}_WDTReloadCountSet(uint8_t reloadCnt);

void ${LED_INSTANCE_NAME}_WDT_CallbackRegister( LED_WDT_CALLBACK callback, uintptr_t context );
</#if>
</#if>

void ${LED_INSTANCE_NAME}_Update(void);


#ifdef __cplusplus // Provide C++ Compatibility
}
#endif

#endif //PLIB_${LED_INSTANCE_NAME}_H

/**
 End of File
*/
