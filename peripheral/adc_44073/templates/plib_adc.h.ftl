/*******************************************************************************
  ${ADC_INSTANCE_NAME} Peripheral Library Interface Header File

  Company
    Microchip Technology Inc.

  File Name
    plib_${ADC_INSTANCE_NAME?lower_case}.h

  Summary
    ${ADC_INSTANCE_NAME} peripheral library interface.

  Description
    This file defines the interface to the ${ADC_INSTANCE_NAME} peripheral library.  This
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
<#assign ADC_INTERRUPT = false>
<#compress>
<#list 0..(ADC_NUM_CHANNELS - 1) as i>
    <#assign ADC_CH_ENABLE = "ADC_"+i+"_CHER">
    <#assign ADC_CH_NEG_INP = "ADC_"+i+"_NEG_INP">
    <#assign ADC_CH_NAME = "ADC_"+i+"_NAME">
<#if i % 2 !=0 >
    <#assign ADC_CH_DIFF_PAIR = "ADC_"+(i-1)+"_NEG_INP">
</#if>
    <#assign CH_NUM = i>
    <#assign ADC_CH_IER_EOC = "ADC_"+i+"_IER_EOC">
<#if (.vars[ADC_CH_ENABLE] == true) && ((.vars[ADC_CH_IER_EOC] == true) || (ADC_IER_COMPE == true))>
    <#assign ADC_INTERRUPT = true>
</#if>

<#-- Find the max and min digital value based on the result resolution and single-ended/differential ended mode -->
<#if .vars[ADC_CH_ENABLE] == true>
    <#if (i % 2 != 0) && (.vars[ADC_CH_DIFF_PAIR] != "GND")>
    <#else>

        <#if .vars[ADC_CH_NEG_INP] != "GND">
            <#if ((ADC_EMR_SIGNMODE_VALUE == "ALL_UNSIGNED") || (ADC_EMR_SIGNMODE_VALUE == "SE_SIGN_DF_UNSG")) >
                <#if (ADC_EMR_OSR_VALUE == "0")>
                    #define ${ADC_INSTANCE_NAME}_CH${CH_NUM}_MAX_OUTPUT  (4095U)
                    #define ${ADC_INSTANCE_NAME}_CH${CH_NUM}_MIN_OUTPUT  (0U)
                <#elseif (ADC_EMR_OSR_VALUE == "1" || ADC_EMR_OSR_VALUE == "2")>
                    #define ${ADC_INSTANCE_NAME}_CH${CH_NUM}_MAX_OUTPUT  (8191U)
                    #define ${ADC_INSTANCE_NAME}_CH${CH_NUM}_MIN_OUTPUT  (0U)
                <#elseif (ADC_EMR_OSR_VALUE == "3" || ADC_EMR_OSR_VALUE == "4")>
                    #define ${ADC_INSTANCE_NAME}_CH${CH_NUM}_MAX_OUTPUT  (16383U)
                    #define ${ADC_INSTANCE_NAME}_CH${CH_NUM}_MIN_OUTPUT  (0U)
                </#if>
            </#if>
            <#if ((ADC_EMR_SIGNMODE_VALUE == "ALL_SIGNED") || (ADC_EMR_SIGNMODE_VALUE == "SE_UNSG_DF_SIGN")) >
                <#if (ADC_EMR_OSR_VALUE == "0")>
                    #define ${ADC_INSTANCE_NAME}_CH${CH_NUM}_MAX_OUTPUT  (2047)
                    #define ${ADC_INSTANCE_NAME}_CH${CH_NUM}_MIN_OUTPUT  (-2048)
                <#elseif (ADC_EMR_OSR_VALUE == "1" || ADC_EMR_OSR_VALUE == "2")>
                    #define ${ADC_INSTANCE_NAME}_CH${CH_NUM}_MAX_OUTPUT  (4095)
                    #define ${ADC_INSTANCE_NAME}_CH${CH_NUM}_MIN_OUTPUT  (-4096)
                <#elseif (ADC_EMR_OSR_VALUE == "3" || ADC_EMR_OSR_VALUE == "4")>
                    #define ${ADC_INSTANCE_NAME}_CH${CH_NUM}_MAX_OUTPUT  (8191)
                    #define ${ADC_INSTANCE_NAME}_CH${CH_NUM}_MIN_OUTPUT  (-8192)
                </#if>
            </#if>
        <#else>
            <#if ((ADC_EMR_SIGNMODE_VALUE == "ALL_UNSIGNED") || (ADC_EMR_SIGNMODE_VALUE == "SE_UNSG_DF_SIGN")) >
                <#if (ADC_EMR_OSR_VALUE == "0")>
                    #define ${ADC_INSTANCE_NAME}_CH${CH_NUM}_MAX_OUTPUT  (4095U)
                    #define ${ADC_INSTANCE_NAME}_CH${CH_NUM}_MIN_OUTPUT  (0U)
                <#elseif (ADC_EMR_OSR_VALUE == "1" || ADC_EMR_OSR_VALUE == "2")>
                    #define ${ADC_INSTANCE_NAME}_CH${CH_NUM}_MAX_OUTPUT  (8191U)
                    #define ${ADC_INSTANCE_NAME}_CH${CH_NUM}_MIN_OUTPUT  (0U)
                <#elseif (ADC_EMR_OSR_VALUE == "3" || ADC_EMR_OSR_VALUE == "4")>
                    #define ${ADC_INSTANCE_NAME}_CH${CH_NUM}_MAX_OUTPUT  (16383U)
                    #define ${ADC_INSTANCE_NAME}_CH${CH_NUM}_MIN_OUTPUT  (0U)
                </#if>
            </#if>
            <#if ((ADC_EMR_SIGNMODE_VALUE == "ALL_SIGNED") || (ADC_EMR_SIGNMODE_VALUE == "SE_SIGN_DF_UNSG")) >
                <#if (ADC_EMR_OSR_VALUE == "0")>
                    #define ${ADC_INSTANCE_NAME}_CH${CH_NUM}_MAX_OUTPUT  (2047)
                    #define ${ADC_INSTANCE_NAME}_CH${CH_NUM}_MIN_OUTPUT  (-2048)
                <#elseif (ADC_EMR_OSR_VALUE == "1" || ADC_EMR_OSR_VALUE == "2")>
                    #define ${ADC_INSTANCE_NAME}_CH${CH_NUM}_MAX_OUTPUT  (4095)
                    #define ${ADC_INSTANCE_NAME}_CH${CH_NUM}_MIN_OUTPUT  (-4096)
                <#elseif (ADC_EMR_OSR_VALUE == "3" || ADC_EMR_OSR_VALUE == "4")>
                    #define ${ADC_INSTANCE_NAME}_CH${CH_NUM}_MAX_OUTPUT  (8191)
                    #define ${ADC_INSTANCE_NAME}_CH${CH_NUM}_MIN_OUTPUT  (-8192)
                </#if>
            </#if>
        </#if>

#define ${.vars[ADC_CH_NAME]} (${CH_NUM}U)
/***********************************************************************/
    </#if>
</#if> <#-- CH ENABLE -->
</#list>
</#compress>

// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************
/* The following functions make up the methods (set of possible operations) of
   this interface.
*/

void ${ADC_INSTANCE_NAME}_Initialize(void);

void ${ADC_INSTANCE_NAME}_ChannelsEnable(ADC_CHANNEL_MASK channelsMask);

void ${ADC_INSTANCE_NAME}_ChannelsDisable(ADC_CHANNEL_MASK channelsMask);

void ${ADC_INSTANCE_NAME}_ChannelsInterruptEnable(ADC_INTERRUPT_MASK channelsInterruptMask);

void ${ADC_INSTANCE_NAME}_ChannelsInterruptDisable(ADC_INTERRUPT_MASK channelsInterruptMask);

void ${ADC_INSTANCE_NAME}_ConversionStart(void);

bool ${ADC_INSTANCE_NAME}_ChannelResultIsReady(ADC_CHANNEL_NUM channel);

uint16_t ${ADC_INSTANCE_NAME}_ChannelResultGet(ADC_CHANNEL_NUM channel);

void ${ADC_INSTANCE_NAME}_ConversionSequenceSet(ADC_CHANNEL_NUM *channelList, uint8_t numChannel);

void ${ADC_INSTANCE_NAME}_ComparisonWindowSet(uint16_t lowThreshold, uint16_t highThreshold);

bool ${ADC_INSTANCE_NAME}_ComparisonEventResultIsReady(void);

void ${ADC_INSTANCE_NAME}_ComparisonRestart(void);
<#if ADC_INTERRUPT == true>

void ${ADC_INSTANCE_NAME}_CallbackRegister(ADC_CALLBACK callback, uintptr_t context);

void ${ADC_INSTANCE_NAME}_InterruptHandler(void);
</#if>
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

