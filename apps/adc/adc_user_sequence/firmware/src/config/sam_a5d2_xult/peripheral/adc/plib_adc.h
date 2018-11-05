/*******************************************************************************
  ADC Peripheral Library Interface Header File

  Company
    Microchip Technology Inc.

  File Name
    plib_adc.h

  Summary
    ADC peripheral library interface.

  Description
    This file defines the interface to the ADC peripheral library.  This
    library provides access to and control of the associated peripheral
    instance.

*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
Copyright (c) 2018 released Microchip Technology Inc.  All rights reserved.

Microchip licenses to you the right to use, modify, copy and distribute
Software only when embedded on a Microchip microcontroller or digital signal
controller that is integrated into your product or third party product
(pursuant to the sublicense terms in the accompanying license agreement).

You should refer to the license agreement accompanying this Software for
additional information regarding your rights and obligations.
SOFTWARE AND DOCUMENTATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND,
EITHER EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION, ANY WARRANTY OF
MERCHANTABILITY, TITLE, NON-INFRINGEMENT AND FITNESS FOR A PARTICULAR PURPOSE.
IN NO EVENT SHALL MICROCHIP OR ITS LICENSORS BE LIABLE OR OBLIGATED UNDER
CONTRACT, NEGLIGENCE, STRICT LIABILITY, CONTRIBUTION, BREACH OF WARRANTY, OR
OTHER LEGAL EQUITABLE THEORY ANY DIRECT OR INDIRECT DAMAGES OR EXPENSES
INCLUDING BUT NOT LIMITED TO ANY INCIDENTAL, SPECIAL, INDIRECT, PUNITIVE OR
CONSEQUENTIAL DAMAGES, LOST PROFITS OR LOST DATA, COST OF PROCUREMENT OF
SUBSTITUTE GOODS, TECHNOLOGY, SERVICES, OR ANY CLAIMS BY THIRD PARTIES
(INCLUDING BUT NOT LIMITED TO ANY DEFENSE THEREOF), OR OTHER SIMILAR COSTS.
*******************************************************************************/
// DOM-IGNORE-END

#ifndef PLIB_ADC_H    // Guards against multiple inclusion
#define PLIB_ADC_H


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
#define ADC_CH0_MAX_OUTPUT (4095U)
#define ADC_CH0_MIN_OUTPUT (0U)
#define CHANNEL_0 (0U)
/***********************************************************************/
#define ADC_CH5_MAX_OUTPUT (4095U)
#define ADC_CH5_MIN_OUTPUT (0U)
#define CHANNEL_5 (5U)
/***********************************************************************/
#define ADC_CH6_MAX_OUTPUT (4095U)
#define ADC_CH6_MIN_OUTPUT (0U)
#define CHANNEL_6 (6U)
/***********************************************************************/
// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************
/* The following functions make up the methods (set of possible operations) of
   this interface.
*/

void ADC_Initialize(void);

void ADC_ChannelsEnable(ADC_CHANNEL_MASK channelsMask);

void ADC_ChannelsDisable(ADC_CHANNEL_MASK channelsMask);

void ADC_ChannelsInterruptEnable(ADC_INTERRUPT_MASK channelsInterruptMask);

void ADC_ChannelsInterruptDisable(ADC_INTERRUPT_MASK channelsInterruptMask);

void ADC_ConversionStart(void);

bool ADC_ChannelResultIsReady(ADC_CHANNEL_NUM channel);

uint16_t ADC_ChannelResultGet(ADC_CHANNEL_NUM channel);

void ADC_ConversionSequenceSet(ADC_CHANNEL_NUM *channelList, uint8_t numChannel);

void ADC_ComparisonWindowSet(uint16_t lowThreshold, uint16_t highThreshold);

bool ADC_ComparisonEventResultIsReady(void);

void ADC_ComparisonRestart(void);

void ADC_CallbackRegister(ADC_CALLBACK callback, uintptr_t context);

void ADC_InterruptHandler(void);
// *****************************************************************************

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

}

#endif
// DOM-IGNORE-END

#endif //PLIB_ADC_H

/**
 End of File
*/

