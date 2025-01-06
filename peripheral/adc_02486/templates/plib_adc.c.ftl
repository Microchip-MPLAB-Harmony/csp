/*******************************************************************************
  ADC Peripheral Library Interface Source File

  Company
    Microchip Technology Inc.

  File Name
    plib_${ADC_INSTANCE_NAME?lower_case}.c

  Summary
    ${ADC_INSTANCE_NAME} peripheral library source.

  Description
    This file implements the ADC peripheral library.

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
#include "device.h"
#include "plib_${ADC_INSTANCE_NAME?lower_case}.h"
<#if core.CoreSysIntFile == true>
#include "interrupts.h"
</#if>

// *****************************************************************************
// *****************************************************************************
// Section: ${ADC_INSTANCE_NAME} Implementation
// *****************************************************************************
// *****************************************************************************

<#if ADC_INTERRUPT == true>
    <#lt>/* Object to hold callback function and context */
    <#lt>static volatile ADC_CALLBACK_OBJECT ${ADC_INSTANCE_NAME}_CallbackObj;
</#if>

void ${ADC_INSTANCE_NAME}_Initialize(void)
{
    AD1CON1CLR = _AD1CON1_ON_MASK;

<#if ADC_AD1CON1 != "0">
    AD1CON1 = 0x${ADC_AD1CON1};
</#if>
<#if ADC_AD1CON2 != "0">
    AD1CON2 = 0x${ADC_AD1CON2};
</#if>
<#if ADC_AD1CON3 != "0">
    AD1CON3 = 0x${ADC_AD1CON3};
</#if>
<#if ADC_AD1CHS != "0">
    AD1CHS = 0x${ADC_AD1CHS};
</#if>
<#if ADC_AD1CSSL != "0" && AD1CON2__CSCNA == true>
    /* Input Scan */
    AD1CSSL = 0x${ADC_AD1CSSL};
</#if>
<#if (core.PRODUCT_FAMILY == "PIC32MX1290") && ADC_AD1CSSL2?has_content && (ADC_AD1CSSL2 != "0")>
    AD1CSSL2 = 0x${ADC_AD1CSSL2};
</#if>

<#if ADC_INTERRUPT == true>
    /* Clear interrupt flag */
    IFS${ADC_IFS_REG_INDEX}CLR = _IFS${ADC_IFS_REG_INDEX}_AD1IF_MASK;
    /* Interrupt Enable */
    IEC${ADC_IFS_REG_INDEX}SET = _IEC${ADC_IFS_REG_INDEX}_AD1IE_MASK;
</#if>

    /* Turn ON ADC */
    AD1CON1SET = _AD1CON1_ON_MASK;
}

void ${ADC_INSTANCE_NAME}_Enable(void)
{
    AD1CON1SET = _AD1CON1_ON_MASK;
}

void ${ADC_INSTANCE_NAME}_Disable(void)
{
    AD1CON1CLR = _AD1CON1_ON_MASK;
}

void ${ADC_INSTANCE_NAME}_SamplingStart(void)
{
    AD1CON1CLR = _AD1CON1_DONE_MASK;
    AD1CON1SET = _AD1CON1_SAMP_MASK;
}

void ${ADC_INSTANCE_NAME}_ConversionStart(void)
{
    AD1CON1CLR = _AD1CON1_SAMP_MASK;
}

void ${ADC_INSTANCE_NAME}_InputSelect(${ADC_INSTANCE_NAME}_MUX muxType, ${ADC_INSTANCE_NAME}_INPUT_POSITIVE positiveInput, ${ADC_INSTANCE_NAME}_INPUT_NEGATIVE negativeInput)
{
    if (muxType == ADC_MUX_B)
    {
        AD1CHSbits.CH0SB = (uint8_t)positiveInput;
        AD1CHSbits.CH0NB = (uint8_t)negativeInput;
    }
    else
    {
        AD1CHSbits.CH0SA = (uint8_t)positiveInput;
        AD1CHSbits.CH0NA = (uint8_t)negativeInput;
    }
}

void ${ADC_INSTANCE_NAME}_InputScanSelect(${ADC_INSTANCE_NAME}_INPUTS_SCAN scanInputs)
{
    AD1CSSL = (uint32_t)scanInputs;
}

<#if AD1CSSL__CSSL_COUNT gt 31>
void ${ADC_INSTANCE_NAME}_InputScanSelect2(${ADC_INSTANCE_NAME}_INPUTS_SCAN2 scanInputs)
{
<#if core.PRODUCT_FAMILY == "PIC32MX1290">
    AD1CSSL2 = (uint32_t)scanInputs;
</#if>
}
</#if>

/*Check if conversion result is available */
bool ${ADC_INSTANCE_NAME}_ResultIsReady(void)
{
    return ((AD1CON1bits.DONE) != 0U);
}


/* Read the conversion result */
uint32_t ${ADC_INSTANCE_NAME}_ResultGet(ADC_RESULT_BUFFER bufferNumber)
{
    return (*((&ADC1BUF0) + (bufferNumber << 2)));
}

<#if ADC_INTERRUPT == true>
void ${ADC_INSTANCE_NAME}_CallbackRegister(ADC_CALLBACK callback, uintptr_t context)
{
    ${ADC_INSTANCE_NAME}_CallbackObj.callback_fn = callback;
    ${ADC_INSTANCE_NAME}_CallbackObj.context = context;
}

void __attribute__((used)) ${ADC_INSTANCE_NAME}_InterruptHandler(void)
{
    IFS${ADC_IFS_REG_INDEX}CLR = _IFS0_AD1IF_MASK;

    if (${ADC_INSTANCE_NAME}_CallbackObj.callback_fn != NULL)
    {
        uintptr_t context = ${ADC_INSTANCE_NAME}_CallbackObj.context;

        ${ADC_INSTANCE_NAME}_CallbackObj.callback_fn(context);
    }
}
</#if>
