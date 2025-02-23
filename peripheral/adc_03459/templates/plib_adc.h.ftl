<#assign showExample = false>
<#assign generateDoxygen = true>
/*******************************************************************************
  ${moduleName?lower_case} PLIB
 
  Company:
    Microchip Technology Inc.
 
  File Name:
    plib_${moduleName?lower_case}.h
 
  Summary:
    ${moduleName?lower_case} PLIB Header File
 
  Description:
    This file has prototype of all the interfaces provided for particular
    ${moduleName?lower_case} peripheral.
 
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

#ifndef PLIB_${moduleName}_H
#define PLIB_${moduleName}_H

// Section: Included Files

#include <xc.h>
#include <stdbool.h>
#include <stdint.h>
#include "plib_adc_common.h"

// /cond IGNORE_THIS
/* Provide C++ Compatibility */
#ifdef __cplusplus

    extern "C" {

#endif
// /endcond

// Section: Data Types

<#if generateDoxygen>
/**
 @enum     ADC${instance}_CHANNEL
 @brief    Defines the ADC channles that are selected
*/
</#if>
typedef enum
{
<#assign maxEnabledChannels = 0>
<#list 0..maxChannel as i>
<#if (.vars["ch"+i+"channelUsed"]??) && (.vars["ch"+i+"channelUsed"] == true)>
    ADC${instance}_CHANNEL${i} = ${i}U,   
<#assign maxEnabledChannels += 1>
</#if>    
</#list>   
    ADC${instance}_MAX_CHANNELS = ${maxEnabledChannels}
} ADC${instance}_CHANNEL;

<#if generateDoxygen>
/**
 @enum     ADC_PWM_INSTANCE
 @brief    Defines the ADC PWM trigger sources that are 
           available for the module to use.
*/
</#if>
typedef enum 
{
    <#list minPWM..maxPWM as x>
    ${moduleName}_PWM${x} = ${x},
    </#list>    
} ${moduleName}_PWM_INSTANCE;


// Section: Driver Interface Functions

<#if generateDoxygen>
/**
 * @brief    Initializes ${moduleName} module, using the given initialization data
 *           This function must be called before any other ${moduleName} function is called
 * @param    none
 * @return   none  
 */
</#if>
void ${moduleName}_Initialize (void);

<#if generateDoxygen>
/**
 * @brief    Deinitializes the ${moduleName} to POR values
 * @param    none
 * @return   none  
 */
</#if>
void ${moduleName}_Deinitialize(void);

<#if generateDoxygen>
/**
 * @brief    This inline function enables the ${moduleName} module
 * @pre      none
 * @param    none
 * @return   none  
 */
</#if>
inline static void ${moduleName}_Enable(void)
{
    AD${instance}CONbits.ON = 1;
    AD${instance}CONbits.MODE = 1;
    while(AD${instance}CONbits.ADRDY == 0U){};
}

<#if generateDoxygen>
/**
 * @brief    This inline function disables the ${moduleName} module
 * @pre      none
 * @param    none
 * @return   none  
 */
</#if>
inline static void ${moduleName}_Disable(void)
{
   AD${instance}CONbits.ON = 0;
}

<#if isChannelSelected == true>
<#if generateDoxygen>
/**
 * @brief    This inline function sets software common trigger
 * @pre      none
 * @param    none
 * @return   none  
 */
</#if>
inline static void ${moduleName}_SoftwareTriggerEnable(void)
{
   AD${instance}SWTRG = 0xFFFFFFFFU;
}

<#if generateDoxygen>
/**
 * @brief       This inline function sets individual software trigger
 * @pre         none
 * @param[in]   channel - Channel for conversion
 * @return      none  
 */
</#if>
inline static void ${moduleName}_ChannelSoftwareTriggerEnable(${moduleName}_CHANNEL channel)
{
    switch(channel)
    {
        <#list 0..maxChannel as i>
        <#if (.vars["ch"+i+"channelUsed"]??) && (.vars["ch"+i+"channelUsed"] == true)>
        case ADC${instance}_CHANNEL${i}:
                AD${instance}SWTRGbits.CH${i}TRG = 0x1U;
                break;
        </#if>
        </#list>
        default:
                /*Do Nothing*/
                break;
    }
}

<#if anyChannelWithIntOrWinConversion>
<#if generateDoxygen>
/**
 * @brief      This inline function returns the requested conversion count
 * @pre        none
 * @param[in]  channel - Channel for conversion  
 * @return     requested number of conversions  
 * @note       This function is applicable in Window mode and Integration conversion mode only 
 */
</#if>
inline static uint16_t ${moduleName}_SampleCountGet(${moduleName}_CHANNEL channel)
{
    uint16_t count = 0x0U;

    switch(channel)
    {
        <#list 0..maxChannel as i>
        <#if (.vars["ch"+i+"channelUsed"]??) && (.vars["ch"+i+"channelUsed"] == true)>
        case ADC${instance}_CHANNEL${i}:
                count = AD${instance}CH${i}CNTbits.CNT;
                break;
        </#if>
        </#list>
        default:
                /*Do Nothing*/
                break;
    }
    return count;
}

<#if generateDoxygen>
/**
 * @brief      This inline function returns the status of completed conversion count
 * @pre        none
 * @param[in]  channel - Channel for conversion  
 * @return     number of conversions completed  
 * @note       This function is applicable in Window mode and Integration conversion mode only 
 */
</#if>
inline static uint16_t ${moduleName}_SampleCountStatusGet(${moduleName}_CHANNEL channel)
{
    uint16_t countStatus = 0x0U;

    switch(channel)
    {
        <#list 0..maxChannel as i>
        <#if (.vars["ch"+i+"channelUsed"]??) && (.vars["ch"+i+"channelUsed"] == true)>
        case ADC${instance}_CHANNEL${i}:
                countStatus = AD${instance}CH${i}CNTbits.CNTSTAT;
                break;
        </#if>
        </#list>
        default:
                /*Do Nothing*/
                break;
    }
    return countStatus;
}

</#if>
<#if generateDoxygen>
/**
 * @brief      Returns the conversion value for the channel selected
 * @pre        This inline function returns the conversion value only after the conversion is complete. 
 *             Conversion completion status can be checked using 
 *             \ref ${moduleName}_IsConversionComplete(channel) function.
 * @param[in]  channel - Selected channel  
 * @return     Returns the analog to digital converted value  
 */
</#if>
inline static uint32_t ${moduleName}_ChannelResultGet(${moduleName}_CHANNEL channel)
{
    uint32_t result = 0x0U;

    switch(channel)
    {
        <#list 0..maxChannel as i>
        <#if (.vars["ch"+i+"channelUsed"]??) && (.vars["ch"+i+"channelUsed"] == true)>
        case ADC${instance}_CHANNEL${i}:
                result = AD${instance}CH${i}DATA;
                break;
        </#if>
        </#list>
        default:
                /*Do Nothing*/
                break;
    }
    return result;
}

<#if chWithIntConversionAndSecAcc>
<#if generateDoxygen>
/**
 * @brief      Returns secondary accumulator conversion value for the channel selected
 * @pre        This inline function returns the conversion value only after the conversion is complete. 
 *             Conversion completion status can be checked using 
 *             \ref ${moduleName}_IsConversionComplete(channel) function.
 * @param[in]  channel - Selected channel  
 * @return     Returns the analog to digital converted value
 * @note       Not all channels support secondary accumulator. Refer to device datasheet for more information. 
 */
</#if>
inline static uint32_t ${moduleName}_SecondaryAccumulatorGet(${moduleName}_CHANNEL channel)
{
    uint32_t result = 0x0U;

    switch(channel)
    {
        <#list 0..maxChannel as i>
        <#if (.vars["ch"+i+"channelUsed"]??) && (.vars["ch"+i+"channelUsed"] == true)>
        <#if (.vars["ch"+i+"SecAcc"]) !="">
        case ADC${instance}_CHANNEL${i}:
                result = AD${instance}CH${i}ACC;
                break;
        </#if>
        </#if>
        </#list>
        default:
                /*Do Nothing*/
                break;
    }
    return result;
}

</#if>
<#if generateDoxygen>
/**
 * @brief      This inline function returns the status of conversion.This function is used to 
 *             determine if conversion is completed. When conversion is complete 
 *             the function returns true otherwise false.
 * @pre        \ref ${moduleName}_SoftwareTriggerEnable() function should have been 
 *             called before calling this function.
 * @param[in]  channel - Selected channel  
 * @return     true - Conversion is complete.
 * @return     false - Conversion is not complete.  
 */
</#if>
inline static bool ${moduleName}_ChannelResultIsReady(${moduleName}_CHANNEL channel)
{
    bool status = false;

    switch(channel)
    {
        <#list 0..maxChannel as i>
        <#if (.vars["ch"+i+"channelUsed"]??) && (.vars["ch"+i+"channelUsed"] == true)>
        case ADC${instance}_CHANNEL${i}:
                status = AD${instance}STATbits.CH${i}RDY == 1U;
                break;
        </#if>
        </#list>
        default:
                /*Do Nothing*/
                break;
    }
    return status;
}

<#if generateDoxygen>
/**
 * @brief      This inline function enables individual channel interrupt
 * @param[in]  channel - Selected channel  
 * @return     none  
 */
</#if>
inline static void ${moduleName}_ChannelResultInterruptEnable(${moduleName}_CHANNEL channel)
{
    switch(channel)
    {
        <#list 0..maxChannel as i>
        <#if (.vars["ch"+i+"channelUsed"]??) && (.vars["ch"+i+"channelUsed"] == true)>
        case ADC${instance}_CHANNEL${i}:
                ${.vars["ch"+i+"InterruptEnableBit"]} = 1;
                break;
        </#if>
        </#list>
        default:
                /*Do Nothing*/
                break;
    }
}

<#if generateDoxygen>
/**
 * @brief      This inline function disables individual channel interrupt
 * @param[in]  channel - Selected channel  
 * @return     none  
 */
</#if>
inline static void ${moduleName}_ChannelResultInterruptDisable(${moduleName}_CHANNEL channel)
{
    switch(channel)
    {
        <#list 0..maxChannel as i>
        <#if (.vars["ch"+i+"channelUsed"]??) && (.vars["ch"+i+"channelUsed"] == true)>
        case ADC${instance}_CHANNEL${i}:
                ${.vars["ch"+i+"InterruptEnableBit"]} = 0;
                break;
        </#if>
        </#list>
        default:
                /*Do Nothing*/
                break;
    }
}

<#if generateDoxygen>
/**
 * @brief      This inline function clears individual channel interrupt flag
 * @pre        The flag is not cleared without reading the data from buffer.
 *             Hence call \ref ${moduleName}_ConversionResultGet() function to read data 
 *             before calling this function
 * @param[in]  channel - Selected channel  
 * @return     none  
 */
</#if>
inline static void ${moduleName}_ChannelResultFlagClear(${moduleName}_CHANNEL channel)
{
    switch(channel)
    {
        <#list 0..maxChannel as i>
        <#if (.vars["ch"+i+"channelUsed"]??) && (.vars["ch"+i+"channelUsed"] == true)>
        case ADC${instance}_CHANNEL${i}:
                ${.vars["ch"+i+"InterruptFlagBit"]} = 0;
                break;
        </#if>
        </#list>
        default:
                /*Do Nothing*/
                break;
    }
}

<#if generateDoxygen>
/**
 * @brief      This inline function returns the status of the comparator
 * @pre        none
 * @param[in]  channel - Selected channel  
 * @return     compare status  
 */
</#if>
inline static bool ${moduleName}_CompareStatusGet(${moduleName}_CHANNEL channel)
{
    bool status = false;
    switch(channel)
    {
        <#list 0..maxChannel as i>
        <#if (.vars["ch"+i+"channelUsed"]??) && (.vars["ch"+i+"channelUsed"] == true)>
        case ADC${instance}_CHANNEL${i}:
                status = AD${instance}CMPSTATbits.CH${i}CMP == 1U;
                //Clear status flag
                AD${instance}CMPSTATbits.CH${i}CMP = 0U;
                //clear the CMP ${i} interrupt flag
                ${.vars["cmp"+i+"InterruptFlagBit"]} = 0U;
                break;
        </#if>
        </#list>
        default:
                /*Do Nothing*/
                break;
    }
    return status;
}

<#if generateDoxygen>
/**
 * @brief      This inline function allows selection of priority for individual channel interrupt
 * @param[in]  channel - Selected channel 
 * @param[in]  priorityValue  -  The numerical value of interrupt priority
 * @return     none  
 */
</#if>
inline static void ${moduleName}_IndividualChannelInterruptPrioritySet(${moduleName}_CHANNEL channel, INTERRUPT_PRIORITY priorityValue)
{
	switch(channel)
	{
		<#list 0..maxChannel as i>
        <#if (.vars["ch"+i+"channelUsed"]??) && (.vars["ch"+i+"channelUsed"] == true)>
		case ADC${instance}_CHANNEL${i}:
				_AD${instance}CH${i}IP = (uint8_t)priorityValue;
				break;
		</#if>
        </#list>
		default:
                /*Do Nothing*/
				break;
	}
}

<#if generateDoxygen>
/**
 * @brief      This function can be used to define custom callback for ${moduleName} Channel event. 
 *             Read the conversion result of the corresponding channel in the custom callback.
 * @pre        none
 * @param[in]  channel - Selected channel.  
 * @param[in]  callback - Address of the channel callback function.  
 * @param[in]  context - A value (usually a pointer) passed (unused) into the function identified by the callback parameter.  
 * @return     none  
 */
</#if>
void ${moduleName}_ChannelCallbackRegister(${moduleName}_CHANNEL channel,ADC_CHANNEL_CALLBACK callback,uintptr_t context);

<#list 0..maxChannel as i>
<#if (.vars["ch"+i+"cmpUsed"]??) && (.vars["ch"+i+"cmpUsed"] == true)>
<#if (.vars["cmp"+i+"IntEnable"]) == true>
<#if generateDoxygen>
/**
 * @brief      This function can be used to define custom callback for ${moduleName} Comparator event
 * @pre        none
 * @param[in]  channel - Selected channel.  
 * @param[in]  callback - Address of the comparator callback function.  
 * @param[in]  context - A value (usually a pointer) passed (unused) into the function identified by the callback parameter.  
 * @return     none  
 */
</#if>
void ${moduleName}_ComparatorCallbackRegister(${moduleName}_CHANNEL channel,ADC_CMP_CALLBACK callback,uintptr_t context);

<#break>
</#if>
</#if>
</#list>

<#if generateDoxygen>
/**
 * @brief    Sets Trigger source as PWM Trigger 
 * @pre      PWM must be enabled and configured 
 * @param[in]  channel - Selected channel. 
 * @param[in]  pwmInstance - Instance of PWM. Refer Datasheet for available PWMs as trigger source
 * @param[in]  triggerNumber - Selection between Trigger 1 or Trigger 2 
 * @return   none  
 */
</#if>
void ${moduleName}_PWMTriggerSourceSet(ADC${instance}_CHANNEL channel, ${moduleName}_PWM_INSTANCE pwmInstance, ADC_PWM_TRIGGERS triggerNumber);

</#if>
#endif //PLIB_${moduleName}_H
    
/**
 End of File
*/

