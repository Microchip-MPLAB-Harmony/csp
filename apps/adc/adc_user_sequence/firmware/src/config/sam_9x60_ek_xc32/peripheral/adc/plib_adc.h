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
#define ADC_CH1_MAX_OUTPUT (4095U)
#define ADC_CH1_MIN_OUTPUT (0U)
#define CHANNEL_1 (1U)
/***********************************************************************/
#define ADC_CH2_MAX_OUTPUT (4095U)
#define ADC_CH2_MIN_OUTPUT (0U)
#define CHANNEL_2 (2U)
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

