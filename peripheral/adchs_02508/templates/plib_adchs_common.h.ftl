/*******************************************************************************
  ADCHS Peripheral Library Interface Header File

  Company
    Microchip Technology Inc.

  File Name
    plib_adchs_common.h

  Summary
    Commonly needed stuff for the ADCHS peripheral libraries interfaces.

  Description
    This file defines several items commonly needed by the interfaces to
    the ADCHS peripheral libraries.

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

#ifndef PLIB_ADCHS_COMMON_H    // Guards against multiple inclusion
#define PLIB_ADCHS_COMMON_H


// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

/*  This section lists the other files that are included in this file.
*/

#include <stddef.h>
#include <stdbool.h>


// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

extern "C" {

#endif

// DOM-IGNORE-END

<#assign ADCHS_COMPARATOR_ENABLED = 0>
<#assign ADCHS_COMPARATOR_INT_ENABLED = 0>

<#list 1..(ADCHS_NUM_COMPARATORS) as i>
<#assign ADCHS_ADCCMPCON_ENDCMP = "ADCCMPCON" + i + "__ENDCMP">
<#assign ADCHS_DCx_INT_ENABLED = "ADCHS_DC" + i + "_INT_ENABLED">
<#if .vars[ADCHS_ADCCMPCON_ENDCMP]?has_content && .vars[ADCHS_ADCCMPCON_ENDCMP] == true>
<#assign ADCHS_COMPARATOR_ENABLED = 1>
<#if .vars[ADCHS_DCx_INT_ENABLED] == true>
<#assign ADCHS_COMPARATOR_INT_ENABLED = 1>
</#if>
</#if>
</#list>

<#assign ADCHS_FILTER_INT_ENABLED = 0>

<#list 1..(ADCHS_NUM_FILTERS) as i>
<#assign ADCFLTR_AFEN = "ADCFLTR" + i + "__AFEN">
<#assign ADCHS_DFx_INT_ENABLED = "ADCHS_DF" + i + "_INT_ENABLED">
<#if .vars[ADCFLTR_AFEN]?has_content && .vars[ADCFLTR_AFEN] == true && .vars[ADCHS_DFx_INT_ENABLED] == true>
<#assign ADCHS_FILTER_INT_ENABLED = 1>
</#if>
</#list>

// *****************************************************************************
// *****************************************************************************
// Section: Data Types
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************

typedef enum
{
<#if ADCHS_NUM_CLASS1_SIGNALS != 0>
<#list 0..((ADCHS_NUM_CLASS1_SIGNALS) - 1) as i>
    ADCHS_MODULE${i}_MASK = (1U << ${i}U),
</#list>
</#if>
    ADCHS_MODULE7_MASK = (1U << 7U)
}ADCHS_MODULE_MASK;


typedef enum
{
<#list 0..((ADCHS_NUM_SIGNALS) - 1) as i>
<#assign ADCHS_SIGNAL = "AN"+ i >
<#if .vars[ADCHS_SIGNAL]??>
    ADCHS_CH${i} = ${i}U,
</#if>
</#list>
}ADCHS_CHANNEL_NUM;

<#if ADCHS_COMPARATOR_ENABLED == 1>
typedef enum
{
    ADCHS_CMP_EVENT_MODE_IELOLO = 0x01,
    ADCHS_CMP_EVENT_MODE_IELOHI = 0x02,
    ADCHS_CMP_EVENT_MODE_IEHILO = 0x04,
    ADCHS_CMP_EVENT_MODE_IEHIHI = 0x08,
    ADCHS_CMP_EVENT_MODE_IEBTWN = 0x10,
}ADCHS_CMP_EVENT_MODE;
</#if>

<#if ADC_IS_DMA_AVAILABLE == true && (ADC_DMA_ENABLED?? && ADC_DMA_ENABLED == true)>
typedef enum
{
<#if ADCHS_NUM_CLASS1_SIGNALS != 0>
<#list 0..((ADCHS_NUM_CLASS1_SIGNALS) - 1) as i>
    ADCHS_DMA_STATUS_RAF${i} = (1U << ${i}U),
</#list>
<#list 0..((ADCHS_NUM_CLASS1_SIGNALS) - 1) as i>
    ADCHS_DMA_STATUS_RBF${i} = (1U << (16U + ${i}U)),
</#list>
</#if>
    ADCHS_DMA_STATUS_WROVERR = (1U << 23U)
}ADCHS_DMA_STATUS;
</#if>

// *****************************************************************************

typedef void (*ADCHS_CALLBACK)(ADCHS_CHANNEL_NUM channel, uintptr_t context);

typedef void (*ADCHS_EOS_CALLBACK)(uintptr_t context);

<#if ADC_IS_DMA_AVAILABLE == true && (ADC_DMA_ENABLED?? && ADC_DMA_ENABLED == true) && (ADC_DMA_INT_ENABLED?? && ADC_DMA_INT_ENABLED == true)>
typedef void (*ADCHS_DMA_CALLBACK)(ADCHS_DMA_STATUS dmaStatus, uintptr_t context);
</#if>

<#if ADCHS_COMPARATOR_INT_ENABLED == 1>
typedef void (*ADCHS_DC_CALLBACK)(ADCHS_CHANNEL_NUM channel, uintptr_t context);
</#if>

<#if ADCHS_FILTER_INT_ENABLED == 1>
typedef void (*ADCHS_DF_CALLBACK)(uintptr_t context);
</#if>

// *****************************************************************************

typedef struct
{
    ADCHS_CALLBACK callback_fn;
    uintptr_t context;
}ADCHS_CALLBACK_OBJECT;

typedef struct
{
    ADCHS_EOS_CALLBACK callback_fn;
    uintptr_t context;
}ADCHS_EOS_CALLBACK_OBJECT;

<#if ADC_IS_DMA_AVAILABLE == true && (ADC_DMA_ENABLED?? && ADC_DMA_ENABLED == true) && (ADC_DMA_INT_ENABLED?? && ADC_DMA_INT_ENABLED == true)>
typedef struct
{
    ADCHS_DMA_CALLBACK callback_fn;
    uintptr_t context;
}ADCHS_DMA_CALLBACK_OBJECT;
</#if>

<#if ADCHS_COMPARATOR_INT_ENABLED == 1>
typedef struct
{
    ADCHS_DC_CALLBACK callback_fn;
    uintptr_t context;
}ADCHS_DC_CALLBACK_OBJECT;
</#if>

<#if ADCHS_FILTER_INT_ENABLED == 1>
typedef struct
{
    ADCHS_DF_CALLBACK callback_fn;
    uintptr_t context;
}ADCHS_DF_CALLBACK_OBJECT;
</#if>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

}

#endif
// DOM-IGNORE-END

#endif //PLIB_ADCHS_COMMMON_H

/**
 End of File
*/
