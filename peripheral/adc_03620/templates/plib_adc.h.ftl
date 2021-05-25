/*******************************************************************************
  ADC Peripheral Library Interface Header File

  Company
    Microchip Technology Inc.

  File Name
    plib_${ADC_INSTANCE_NAME?lower_case}.h

  Summary
    ${ADC_INSTANCE_NAME} peripheral library interface.

  Description
    This file defines the interface to the ADC peripheral library.  This
    library provides access to and control of the associated peripheral
    instance.

*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
* Copyright (C) 2021 Microchip Technology Inc. and its subsidiaries.
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

#ifndef PLIB_${ADC_INSTANCE_NAME}_H    // Guards against multiple inclusion
#define PLIB_${ADC_INSTANCE_NAME}_H


// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

/*  This section lists the other files that are included in this file.
*/

#include "plib_adc_common.h"

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

void ${ADC_INSTANCE_NAME}_Initialize (void);

void ${ADC_INSTANCE_NAME}_Enable( void );
void ${ADC_INSTANCE_NAME}_Disable( void );

void ${ADC_INSTANCE_NAME}_CompareEnable(ADC_CORE_NUM core, ADC_CHANNEL_NUM channel);
void ${ADC_INSTANCE_NAME}_CompareDisable(ADC_CORE_NUM core, ADC_CHANNEL_NUM channel);
void ${ADC_INSTANCE_NAME}_CompareWinThresholdSet(ADC_CORE_NUM core, uint16_t low_threshold, uint16_t high_threshold);
void ${ADC_INSTANCE_NAME}_CompareWinModeSet(ADC_CORE_NUM core, ADC_CMPCTRL mode);

ADC_GLOBAL_INT ${ADC_INSTANCE_NAME}_GlobalInterruptsStatusGet(void);
void ${ADC_INSTANCE_NAME}_CoreInterruptsEnable(ADC_CORE_NUM core, ADC_CORE_INT interruptMask);
void ${ADC_INSTANCE_NAME}_CoreInterruptsDisable(ADC_CORE_NUM core, ADC_CORE_INT interruptMask);
ADC_CORE_INT ${ADC_INSTANCE_NAME}_CoreInterruptsStatusGet(ADC_CORE_NUM core);
void ${ADC_INSTANCE_NAME}_CoreInterruptsStatusClear(ADC_CORE_NUM core, ADC_CORE_INT interruptMask);

void ${ADC_INSTANCE_NAME}_GlobalEdgeConversionStart(void);
void ${ADC_INSTANCE_NAME}_GlobalLevelConversionStart(void);
void ${ADC_INSTANCE_NAME}_GlobalLevelConversionStop(void);

void ${ADC_INSTANCE_NAME}_SyncTriggerEnable(void);
void ${ADC_INSTANCE_NAME}_SyncTriggerDisable(void);
void ${ADC_INSTANCE_NAME}_SyncTriggerCounterSet(uint16_t counterVal);

void ${ADC_INSTANCE_NAME}_SoftwareControlledConversionEnable(ADC_CORE_NUM core, ADC_CHANNEL_NUM channel);
void ${ADC_INSTANCE_NAME}_ChannelSamplingStart(void);
void ${ADC_INSTANCE_NAME}_ChannelSamplingStop(void);
void ${ADC_INSTANCE_NAME}_ChannelConversionStart(void);

bool ${ADC_INSTANCE_NAME}_ChannelResultIsReady(ADC_CORE_NUM core, ADC_CHANNEL_NUM channel);
bool ${ADC_INSTANCE_NAME}_EOSStatusGet(ADC_CORE_NUM core);
uint32_t ${ADC_INSTANCE_NAME}_ResultGet( ADC_CORE_NUM core, ADC_CHANNEL_NUM channel);

<#if ADC_PFFCTRL != "0">
uint32_t ${ADC_INSTANCE_NAME}_FIFORead( void );
uint32_t ${ADC_INSTANCE_NAME}_FIFOBufferRead( uint32_t* pBuffer, uint32_t size );
</#if>

<#if ADC_CTLINTENSET != "0">
void ${ADC_INSTANCE_NAME}_GlobalCallbackRegister(ADC_GLOBAL_CALLBACK callback, uintptr_t context);
</#if>

<#list 0..(ADC_NUM_SAR_CORES-1) as n>
        <#assign ADC_CORE_INT_ENABLED    = "ADC_CORE_" + n + "_ADC_INTENSET">
        <#if .vars[ADC_CORE_INT_ENABLED] != "0">
        <#lt>void ${ADC_INSTANCE_NAME}_CORE${n}CallbackRegister(ADC_CORE_CALLBACK callback, uintptr_t context);
        </#if>
</#list>

// *****************************************************************************

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

}
#endif
// DOM-IGNORE-END

#endif //PLIB_${ADC_INSTANCE_NAME}_H

/**
 End of File
*/
