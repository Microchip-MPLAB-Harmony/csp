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

#ifndef PLIB_${ADC_INSTANCE_NAME}_H    // Guards against multiple inclusion
#define PLIB_${ADC_INSTANCE_NAME}_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

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
<#if (.vars[ADC_CH_ENABLE] == true) && (.vars[ADC_CH_IER_EOC] == true)>
    <#assign ADC_INTERRUPT = true>
</#if>

<#-- Find the max and min digital value based on the result resolution and single-ended/differential ended mode -->
<#if .vars[ADC_CH_ENABLE] == true>
    <#if (ADC_EMR_RES_VALUE == "NO_AVERAGE")>
        #define ${ADC_INSTANCE_NAME}_CH${CH_NUM}_MAX_OUTPUT  (4095U)
        #define ${ADC_INSTANCE_NAME}_CH${CH_NUM}_MIN_OUTPUT  (0U)
    <#elseif (ADC_EMR_RES_VALUE == "OSR4")>
        #define ${ADC_INSTANCE_NAME}_CH${CH_NUM}_MAX_OUTPUT  (8191U)
        #define ${ADC_INSTANCE_NAME}_CH${CH_NUM}_MIN_OUTPUT  (0U)
    <#elseif (ADC_EMR_RES_VALUE == "OSR16")>
        #define ${ADC_INSTANCE_NAME}_CH${CH_NUM}_MAX_OUTPUT  (16383U)
        #define ${ADC_INSTANCE_NAME}_CH${CH_NUM}_MIN_OUTPUT  (0U)
    <#elseif (ADC_EMR_RES_VALUE == "OSR64")>
        #define ${ADC_INSTANCE_NAME}_CH${CH_NUM}_MAX_OUTPUT  (32767U)
        #define ${ADC_INSTANCE_NAME}_CH${CH_NUM}_MIN_OUTPUT  (0U)
    <#else>
        #define ${ADC_INSTANCE_NAME}_CH${CH_NUM}_MAX_OUTPUT  (65535U)
        #define ${ADC_INSTANCE_NAME}_CH${CH_NUM}_MIN_OUTPUT  (0U)
    </#if>

#define ${.vars[ADC_CH_NAME]} (${CH_NUM}U)
/***********************************************************************/
</#if> <#-- CH ENABLE -->
</#list>

<#if ADC_IER_COMPE == true>
    <#assign ADC_INTERRUPT = true>
</#if>
</#compress>

// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************

void ${ADC_INSTANCE_NAME}_Initialize( void );

void ${ADC_INSTANCE_NAME}_ChannelsEnable( ADC_CHANNEL_MASK channelsMask );

void ${ADC_INSTANCE_NAME}_ChannelsDisable( ADC_CHANNEL_MASK channelsMask );

void ${ADC_INSTANCE_NAME}_ChannelsInterruptEnable( ADC_INTERRUPT_MASK channelsInterruptMask );

void ${ADC_INSTANCE_NAME}_ChannelsInterruptDisable( ADC_INTERRUPT_MASK channelsInterruptMask );

void ${ADC_INSTANCE_NAME}_ConversionStart( void );

bool ${ADC_INSTANCE_NAME}_ChannelResultIsReady( ADC_CHANNEL_NUM channel );

uint16_t ${ADC_INSTANCE_NAME}_ChannelResultGet( ADC_CHANNEL_NUM channel );

void ${ADC_INSTANCE_NAME}_ConversionSequenceSet( ADC_CHANNEL_NUM *channelList, uint8_t numChannel );

<#if ADC_INTERRUPT == true>
    <#lt>void ${ADC_INSTANCE_NAME}_CallbackRegister( ADC_CALLBACK callback, uintptr_t context );
<#else>
    <#lt>uint32_t ${ADC_INSTANCE_NAME}_StatusGet(void);
    <#lt>bool ${ADC_INSTANCE_NAME}_ComparatorStatusGet(void);
</#if>

void ${ADC_INSTANCE_NAME}_ComparatorChannelSet(ADC_CHANNEL_NUM channel);

void ${ADC_INSTANCE_NAME}_CompareAllChannelsEnable(void);

void ${ADC_INSTANCE_NAME}_CompareAllChannelsDisable(void);

void ${ADC_INSTANCE_NAME}_CompareRestart(void);

void ${ADC_INSTANCE_NAME}_ComparatorModeSet(ADC_COMPARATOR_MODE cmpMode);

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END

#endif //PLIB_${ADC_INSTANCE_NAME}_H
