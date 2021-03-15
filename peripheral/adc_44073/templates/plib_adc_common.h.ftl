/*******************************************************************************
  ADC Peripheral Library Interface Common Header File

  Company
    Microchip Technology Inc.

  File Name
    plib_adc_common.h

  Summary
    ADC peripheral library common interface.

  Description
    This file defines the common interface to the ADC peripheral library. This
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

#ifndef PLIB_ADC_COMMON_H    // Guards against multiple inclusion
#define PLIB_ADC_COMMON_H


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

// *****************************************************************************
// *****************************************************************************
// Section: Data Types
// *****************************************************************************
// *****************************************************************************

/* Identifies ADC channel mask */
typedef enum
{
<#list 0..(ADC_NUM_CHANNELS - 1) as i>
    ADC_CH${i}_MASK = (1U << ${i}U),
</#list>
}ADC_CHANNEL_MASK;

/* Analog channel numbers */
typedef enum
{
<#list 0..(ADC_NUM_CHANNELS - 1) as i>
    <#if i == 0>
    ADC_CH${i} = ${i}U,
    <#else>
    ADC_CH${i},
    </#if>
</#list>
}ADC_CHANNEL_NUM;

/* Interrupt sources number */
typedef enum
{
<#list 0..(ADC_NUM_CHANNELS - 1) as i>
    ADC_INTERRUPT_EOC_${i}_MASK = (1U << ${i}U),
</#list>
    ADC_INTERRUPT_DRDY_MASK = (1U << 24U),
    ADC_INTERRUPT_GOVRE_MASK = (1U << 25U),
    ADC_INTERRUPT_COMPE_MASK = (1U << 26U)
}ADC_INTERRUPT_MASK;

/* Callback Function Pointer */
typedef void (*ADC_CALLBACK)(uint32_t status, uintptr_t context);

/* Callback structure */
typedef struct
{
    ADC_CALLBACK callback_fn;
    uintptr_t context;
}ADC_CALLBACK_OBJECT;

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

}

#endif
// DOM-IGNORE-END

#endif //PLIB_ADC_COMMMON_H

/**
 End of File
*/
