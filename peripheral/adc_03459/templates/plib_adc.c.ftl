<#assign adconModeOptions = ["POWERED_DOWN","STANDBY","ON"]>
<#assign adchconModeOptions = ["SINGLE_SAMPLE","WINDOW","INTEGRATION","OVERSAMPLING"]>
<#assign adchconAccnumOptions = ["4_SAMPLES","16_SAMPLES","64_SAMPLES","256_SAMPLES"]>
<#assign adchconCmpmodOptions = ["DISABLED","OUT_OF_BOUNDS","IN_BOUNDS","GRATER_THAN","LESS_THAN_OR_EQUAL"]>
/*******************************************************************************
  ${moduleName?lower_case} PLIB
 
  Company:
    Microchip Technology Inc.
 
  File Name:
    plib_${moduleName?lower_case}.c
 
  Summary:
    ${moduleName?lower_case} PLIB Source File
 
  Description:
    None
 
*******************************************************************************/
 
/*******************************************************************************
* Copyright (C) 2024 Microchip Technology Inc. and its subsidiaries.
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

//{core.disclaimer}

// Section: Included Files

#include <stdint.h>
#include <stddef.h>
#include <stdbool.h>
#include "device.h"
#include "interrupts.h"
#include "plib_adc_common.h"
#include "plib_${moduleName?lower_case}.h"

// Section: Macro Definitions

//ADC AD${instance}CON MODE options
<#list adconModeOptions as options>
#define AD${instance}CON_MODE_${options}          ((uint32_t)(_AD${instance}CON_MODE_MASK & ((uint32_t)(${options_index}) << _AD${instance}CON_MODE_POSITION))) 
</#list>

//ADC AD${instance}CON RPTCNT set
#define AD${instance}CON_RPTCNT_SET(value)              ((uint32_t)(_AD${instance}CON_RPTCNT_MASK & ((uint32_t)(value) << _AD${instance}CON_RPTCNT_POSITION))) 

<#list 0..maxChannel as i>
<#if (.vars["ch"+i+"channelUsed"]??) && (.vars["ch"+i+"channelUsed"] == true)>
//ADC AD${instance}CH${i}CON MODE options
<#list adchconModeOptions as options>
#define AD${instance}CH${i}CON_MODE_${options}          ((uint32_t)(_AD${instance}CH${i}CON_MODE_MASK & ((uint32_t)(${options_index}) << _AD${instance}CH${i}CON_MODE_POSITION))) 
</#list>

//ADC AD${instance}CH${i}CON ACCNUM options
<#list adchconAccnumOptions as options>
#define AD${instance}CH${i}CON_ACCNUM_${options}          ((uint32_t)(_AD${instance}CH${i}CON_ACCNUM_MASK & ((uint32_t)(${options_index}) << _AD${instance}CH${i}CON_ACCNUM_POSITION))) 
</#list>

//ADC AD${instance}CH${i}CON TRG2SRC set
#define AD${instance}CH${i}CON_TRG2SRC_SET(value)              ((uint32_t)(_AD${instance}CH${i}CON_TRG2SRC_MASK & ((uint32_t)(value) << _AD${instance}CH${i}CON_TRG2SRC_POSITION))) 

//ADC AD${instance}CH${i}CON CMPMOD options
<#list adchconCmpmodOptions as options>
#define AD${instance}CH${i}CON_CMPMOD_${options}          ((uint32_t)(_AD${instance}CH${i}CON_CMPMOD_MASK & ((uint32_t)(${options_index}) << _AD${instance}CH${i}CON_CMPMOD_POSITION))) 
</#list>

//ADC AD${instance}CH${i}CON PINSEL set
#define AD${instance}CH${i}CON_PINSEL_SET(value)              ((uint32_t)(_AD${instance}CH${i}CON_PINSEL_MASK & ((uint32_t)(value) << _AD${instance}CH${i}CON_PINSEL_POSITION))) 

//ADC AD${instance}CH${i}CON NINSEL set
#define AD${instance}CH${i}CON_NINSEL_SET(value)              ((uint32_t)(_AD${instance}CH${i}CON_NINSEL_MASK & ((uint32_t)(value) << _AD${instance}CH${i}CON_NINSEL_POSITION))) 

//ADC AD${instance}CH${i}CON SAMC set
#define AD${instance}CH${i}CON_SAMC_SET(value)              ((uint32_t)(_AD${instance}CH${i}CON_SAMC_MASK & ((uint32_t)(value) << _AD${instance}CH${i}CON_SAMC_POSITION))) 

//ADC AD${instance}CH${i}CON TRG1SRC set
#define AD${instance}CH${i}CON_TRG1SRC_SET(value)              ((uint32_t)(_AD${instance}CH${i}CON_TRG1SRC_MASK & ((uint32_t)(value) << _AD${instance}CH${i}CON_TRG1SRC_POSITION))) 

//ADC AD${instance}CH${i}CNT CNT set
#define AD${instance}CH${i}CNT_CNT_SET(value)              ((uint32_t)(_AD${instance}CH${i}CNT_CNT_MASK & ((uint32_t)(value) << _AD${instance}CH${i}CNT_CNT_POSITION))) 

</#if>
</#list>

// Section: File specific functions

<#if isChannelSelected == true>
volatile static ADC_CHANNEL_OBJECT ${moduleName?lower_case}ChannelObj[${maxChannel}];
volatile static ADC_CMP_OBJECT ${moduleName?lower_case}CmpObj[${maxChannel}];


typedef enum {
    <#list minPWM..maxPWM as x>
    PWM${x}_TRIGGER1 = ${triggerInitVal?number + x_index*2}, 
    PWM${x}_TRIGGER2 = ${triggerInitVal?number + x_index*2 + 1}, 
    </#list>
}${moduleName}_PWM_TRIGGERS;

static uint16_t ${moduleName}_TriggerSourceValueGet(${moduleName}_PWM_INSTANCE pwmInstance, ADC_PWM_TRIGGERS triggerNumber);
</#if>

// Section: ISR declaration

<#list 0..maxChannel as i>
<#if (.vars["ch"+i+"channelUsed"]??) && (.vars["ch"+i+"channelUsed"] == true)>
void ${.vars["ch"+i+"IsrHandlerName"]}(void);
</#if>
</#list>
<#list 0..maxChannel as i>
<#if (.vars["ch"+i+"cmpUsed"]??) && (.vars["ch"+i+"cmpUsed"] == true)>
void ${.vars["cmp"+i+"IsrHandlerName"]}(void);
</#if>
</#list>

// Section: ${moduleName} Implementation

void ${moduleName}_Initialize(void)
{
    AD${instance}CON = AD${instance}CON_RPTCNT_SET(${.vars["AD_CON__RPTCNT"]?number});
    //Clear CMP status
    AD${instance}CMPSTAT = 0x0U;
    
    <#list 0..maxChannel as i>
    <#if (.vars["ch"+i+"channelUsed"]??) && (.vars["ch"+i+"channelUsed"] == true)>
    AD${instance}CH${i}CON = (AD${instance}CH${i}CON_MODE_${adchconModeOptions[.vars["AD_CH"+i+"CON__MODE"]?number]}
                            |AD${instance}CH${i}CON_ACCNUM_${adchconAccnumOptions[.vars["AD_CH"+i+"CON__ACCNUM"]?number]}<#if .vars["AD_CH"+i+"CON__ACCBRST"]?number == 1>
                            |_AD${instance}CH${i}CON_ACCBRST_MASK</#if><#if .vars["AD_CH"+i+"CON__ACCRO"]?number == 1>
                            |_AD${instance}CH${i}CON_ACCRO_MASK</#if><#if .vars["AD_CH"+i+"CON__EIEN"]?number == 1>
                            |_AD${instance}CH${i}CON_EIEN_MASK</#if>
                            |AD${instance}CH${i}CON_TRG2SRC_SET(${.vars["AD_CH"+i+"CON__TRG2SRC"]?number})
                            |AD${instance}CH${i}CON_CMPMOD_${adchconCmpmodOptions[.vars["AD_CH"+i+"CON__CMPMOD"]?number]}<#if .vars["AD_CH"+i+"CON__DIFF"]?number == 1>
                            |_AD${instance}CH${i}CON_DIFF_MASK</#if>
                            |AD${instance}CH${i}CON_PINSEL_SET(${.vars["AD_CH"+i+"CON__PINSEL"]?number})<#if .vars["AD_CH"+i+"CON__LEFT"]?number == 1>
                            |_AD${instance}CH${i}CON_LEFT_MASK</#if>
                            |AD${instance}CH${i}CON_NINSEL_SET(${.vars["AD_CH"+i+"CON__NINSEL"]?number})
                            |AD${instance}CH${i}CON_SAMC_SET(${.vars["AD_CH"+i+"CON__SAMC"]?number})
                            |AD${instance}CH${i}CON_TRG1SRC_SET(${.vars["AD_CH"+i+"CON__TRG1SRC"]?number}));
    AD${instance}CH${i}CNT = AD${instance}CH${i}CNT_CNT_SET(${.vars["AD_CH"+i+"CNT__CNT"]?number});
    <#if .vars["AD_CH" + i + "CMPLO"]??>
    AD${instance}CH${i}CMPLO = 0X${.vars["AD_CH" + i + "CMPLO"]}UL;
    </#if>
    <#if .vars["AD_CH" + i + "CMPHI"]??>
    AD${instance}CH${i}CMPHI = 0X${.vars["AD_CH" + i + "CMPHI"]}UL;
    </#if>
    
    </#if>
    </#list>  
    
    <#list 0..maxChannel as i>
    <#if (.vars["ch"+i+"channelUsed"]??) && (.vars["ch"+i+"channelUsed"] == true)>
    <#if (.vars["ch"+i+"IntEnable"]) == true>
    // Clearing CH ${i} interrupt flag.
    ${.vars["ch"+i+"InterruptFlagBit"]} = 0U;
    // Enabling CH ${i} interrupt.
    ${.vars["ch"+i+"InterruptEnableBit"]} = 1U;
    
    </#if>
    <#if (.vars["cmp"+i+"IntEnable"]) == true>
    // Clearing CMP ${i} interrupt flag.
    ${.vars["cmp"+i+"InterruptFlagBit"]} = 0U;
    // Enabling CMP ${i} interrupt.
    ${.vars["cmp"+i+"InterruptEnableBit"]} = 1U;
    
    </#if>
    </#if>
    </#list>
    //Mode change to run mode and enable ADC
    AD${instance}CON |= (AD${instance}CON_MODE_ON | _AD${instance}CON_ON_MASK);
    while(AD${instance}CONbits.ADRDY == 0U){};
}

void ${moduleName}_Deinitialize(void)
{
    uint32_t  __attribute__ ((unused)) dummy;
    
    ${moduleName}_Disable();
    
    <#list 0..maxChannel as i>
    <#if (.vars["ch"+i+"channelUsed"]??) && (.vars["ch"+i+"channelUsed"] == true)>
    dummy = AD${instance}CH${i}DATA;
    (void)dummy;
    _AD${instance}CH${i}IF = 0U;
    _AD${instance}CH${i}IE = 0U;
    </#if>
    </#list>
    
${regPorSet}
    
}

<#if isChannelSelected == true>
void ${moduleName}_SharedCoreCalibration (void) 
{
    AD${instance}CONbits.CALREQ = 1U;    
    while(AD${instance}CONbits.CALRDY == 0U)
    {
    }  
}

static uint16_t ${moduleName}_TriggerSourceValueGet(${moduleName}_PWM_INSTANCE pwmInstance, ADC_PWM_TRIGGERS triggerNumber)
{
    uint16_t adcTriggerSourceValue = 0x0U;
    switch(pwmInstance)
    {
    <#list maxPWM..maxPWM as x>
        case ${moduleName}_PWM${x}:
                if(triggerNumber == ADC_PWM_TRIGGER_1)
                {
                    adcTriggerSourceValue = PWM${x}_TRIGGER1;
                }
                else if(triggerNumber == ADC_PWM_TRIGGER_2)
                {
                    adcTriggerSourceValue = PWM${x}_TRIGGER2;
                }
                else
                {
                }
                break;
    </#list>
         default:
                break;
    }
    return adcTriggerSourceValue;
}

void ${moduleName}_PWMTriggerSourceSet(ADC${instance}_CHANNEL channel, ${moduleName}_PWM_INSTANCE pwmInstance, ADC_PWM_TRIGGERS triggerNumber)
{
    uint16_t adcTriggerValue;
    adcTriggerValue= ${moduleName}_TriggerSourceValueGet(pwmInstance, triggerNumber);
    switch(channel)
    {
        <#list 0..maxChannel as i>
        <#if (.vars["ch"+i+"channelUsed"]??) && (.vars["ch"+i+"channelUsed"] == true)>
        case ADC${instance}_CHANNEL${i}:
                AD${instance}CH${i}CONbits.TRG1SRC = adcTriggerValue;
                break;
        </#if>
        </#list>
        default:
                break;
    }
}

void ${moduleName}_ChannelCallbackRegister(ADC${instance}_CHANNEL channel,ADC_CHANNEL_CALLBACK callback,uintptr_t context)
{
    ${moduleName?lower_case}ChannelObj[channel].callback = callback;
    ${moduleName?lower_case}ChannelObj[channel].context = context;
} 

void ${moduleName}_ComparatorCallbackRegister(ADC${instance}_CHANNEL channel,ADC_CMP_CALLBACK callback,uintptr_t context)
{
    ${moduleName?lower_case}CmpObj[channel].callback = callback;
    ${moduleName?lower_case}CmpObj[channel].context = context;
}

<#list 0..maxChannel as i>
<#if (.vars["ch"+i+"channelUsed"]??) && (.vars["ch"+i+"channelUsed"] == true)>
void ${.vars["ch"+i+"IsrHandlerName"]}(void)
{
    uint32_t valChannel${i}Data;
    //Read the ADC value from the ADCH${i}DATA
    valChannel${i}Data = AD${instance}CH${i}DATA;
    
    if(${moduleName?lower_case}ChannelObj[${i}].callback != NULL)
    {
      ${moduleName?lower_case}ChannelObj[${i}].callback(valChannel${i}Data, ${moduleName?lower_case}ChannelObj[${i}].context);
    }

    //clear the CH ${i} interrupt flag
    ${.vars["ch"+i+"InterruptFlagBit"]} = 0U;
}

</#if>
</#list>
<#list 0..maxChannel as i>
<#if (.vars["ch"+i+"cmpUsed"]??) && (.vars["ch"+i+"cmpUsed"] == true)>
void ${.vars["cmp"+i+"IsrHandlerName"]}(void)
{
    if(${moduleName?lower_case}CmpObj[${i}].callback != NULL)
    {
      ${moduleName?lower_case}CmpObj[${i}].callback(${moduleName?lower_case}CmpObj[${i}].context);
    }
    
    //Clear status flag
    AD${instance}CMPSTATbits.CH${i}CMP = 0U;
    //clear the CMP ${i} interrupt flag
    ${.vars["cmp"+i+"InterruptFlagBit"]} = 0U;
}
</#if>
</#list>

</#if>
