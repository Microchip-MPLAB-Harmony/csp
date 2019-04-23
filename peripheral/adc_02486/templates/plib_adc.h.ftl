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

/*  This section lists the other files that are included in this file.
*/
#include <device.h>
#include <stdint.h>
#include <stdbool.h>
#include <stddef.h>

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
typedef enum {
    ADC_MUX_A,
    ADC_MUX_B
} ${ADC_INSTANCE_NAME}_MUX;

typedef enum {
    ADC_RESULT_BUFFER_0 = 0,
    ADC_RESULT_BUFFER_1,
    ADC_RESULT_BUFFER_2,
    ADC_RESULT_BUFFER_3,
    ADC_RESULT_BUFFER_4,
    ADC_RESULT_BUFFER_5,
    ADC_RESULT_BUFFER_6,
    ADC_RESULT_BUFFER_7,
    ADC_RESULT_BUFFER_8,
    ADC_RESULT_BUFFER_9,
    ADC_RESULT_BUFFER_10,
    ADC_RESULT_BUFFER_11,
    ADC_RESULT_BUFFER_12,
    ADC_RESULT_BUFFER_13,
    ADC_RESULT_BUFFER_14,
    ADC_RESULT_BUFFER_15
}${ADC_INSTANCE_NAME}_RESULT_BUFFER;

typedef enum
{
<#list 0..((AD1CHS__CH0SA_COUNT) - 1) as i>
    <#assign ADC_SIGNAL = "AD1CHS__CH0SA_ENUM_NAME_"+ i >
    <#assign ADC_VALUE = "AD1CHS__CH0SA_ENUM_VALUE_"+ i >
    <#if .vars[ADC_SIGNAL]?? && .vars[ADC_VALUE]??>
        <#lt>    ${ADC_INSTANCE_NAME}_INPUT_POSITIVE_${.vars[ADC_SIGNAL]} = ${.vars[ADC_VALUE]},
    </#if>
</#list>
}${ADC_INSTANCE_NAME}_INPUT_POSITIVE;

typedef enum
{
<#list 0..((AD1CHS__CH0NA_COUNT) - 1) as i>
    <#assign ADC_SIGNAL = "AD1CHS__CH0NA_ENUM_NAME_"+ i >
    <#assign ADC_VALUE = "AD1CHS__CH0NA_ENUM_VALUE_"+ i >
    <#if .vars[ADC_SIGNAL]?? && .vars[ADC_VALUE]??>
        <#lt>    ${ADC_INSTANCE_NAME}_INPUT_NEGATIVE_${.vars[ADC_SIGNAL]} = ${.vars[ADC_VALUE]},
    </#if>
</#list>
}${ADC_INSTANCE_NAME}_INPUT_NEGATIVE;

typedef enum
{
<#list 0..((AD1CSSL__CSSL_COUNT) - 1) as i>
    <#assign ADC_SIGNAL = "AD1CSSL__CSSL_ENUM_NAME_"+ i >
    <#assign ADC_VALUE = "AD1CSSL__CSSL_ENUM_VALUE_"+ i >
    <#if .vars[ADC_SIGNAL]?? && .vars[ADC_VALUE]??>
        <#if i gt 32>
            <#lt>    ${ADC_INSTANCE_NAME}_INPUT_SCAN_${.vars[ADC_SIGNAL]} = 0x${.vars[ADC_VALUE]}00000000,
        <#else>
            <#lt>    ${ADC_INSTANCE_NAME}_INPUT_SCAN_${.vars[ADC_SIGNAL]} = 0x${.vars[ADC_VALUE]},
        </#if>
    </#if>
</#list>
}${ADC_INSTANCE_NAME}_INPUTS_SCAN;


// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************
/* The following functions make up the methods (set of possible operations) of
   this interface.
*/

void ${ADC_INSTANCE_NAME}_Initialize (void);

void ${ADC_INSTANCE_NAME}_Enable();
void ${ADC_INSTANCE_NAME}_Disable();

void ${ADC_INSTANCE_NAME}_SamplingStart(void);
void ${ADC_INSTANCE_NAME}_ConversionStart(void);

void ${ADC_INSTANCE_NAME}_InputSelect(${ADC_INSTANCE_NAME}_MUX muxType, ${ADC_INSTANCE_NAME}_INPUT_POSITIVE positiveInput, ${ADC_INSTANCE_NAME}_INPUT_NEGATIVE negativeInput );
void ${ADC_INSTANCE_NAME}_InputScanSelect(${ADC_INSTANCE_NAME}_INPUTS_SCAN scanInputs);

bool ${ADC_INSTANCE_NAME}_ResultIsReady();
uint32_t ${ADC_INSTANCE_NAME}_ResultGet(ADC_RESULT_BUFFER bufferNumber);

<#if ADC_INTERRUPT == true>
typedef void (*ADC_CALLBACK)(uintptr_t context);

typedef struct
{
    ADC_CALLBACK callback_fn;
    uintptr_t context;
}ADC_CALLBACK_OBJECT;

    <#lt>void ${ADC_INSTANCE_NAME}_CallbackRegister(ADC_CALLBACK callback, uintptr_t context);
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
