<#assign dacconIrqmOptions = ["DISABLED","RISING","FALLING","RISING_OR_FALLING"]>
<#assign dacconInselOptions = ["CMPxA","CMPxB","CMPxC","CMPxD"]>
<#assign dacconHysselOptions = ["NO_HYS","15_mV","30_mV","45_mV"]>
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
* Copyright (C) 2025 Microchip Technology Inc. and its subsidiaries.
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

// Section: Included Files

#include <stdint.h>
#include <stddef.h>
#include <stdbool.h>
#include "device.h"
#include "interrupts.h"
#include "plib_cmp_common.h"
#include "plib_${moduleName?lower_case}.h"

//CMP DACCTRL2 SSTIME set
#define DACCTRL2_SSTIME_SET(value)              ((uint32_t)(_DACCTRL2_SSTIME_MASK & ((uint32_t)(value) << _DACCTRL2_SSTIME_POSITION))) 

//CMP DACCTRL2 TMODTIME set
#define DACCTRL2_TMODTIME_SET(value)              ((uint32_t)(_DACCTRL2_TMODTIME_MASK & ((uint32_t)(value) << _DACCTRL2_TMODTIME_POSITION))) 

//CMP DAC${instance}CON TMCB set
#define DAC${instance}CON_TMCB_SET(value)              ((uint32_t)(_DAC${instance}CON_TMCB_MASK & ((uint32_t)(value) << _DAC${instance}CON_TMCB_POSITION))) 

//CMP DAC${instance}CON IRQM options
<#list dacconIrqmOptions as options>
#define DAC${instance}CON_IRQM_${options}          ((uint32_t)(_DAC${instance}CON_IRQM_MASK & ((uint32_t)(${options_index}) << _DAC${instance}CON_IRQM_POSITION))) 
</#list>

//CMP DAC${instance}CON INSEL options
<#list dacconInselOptions as options>
#define DAC${instance}CON_INSEL_${options}          ((uint32_t)(_DAC${instance}CON_INSEL_MASK & ((uint32_t)(${options_index}) << _DAC${instance}CON_INSEL_POSITION))) 
</#list>

//CMP DAC${instance}CON HYSSEL options
<#list dacconHysselOptions as options>
#define DAC${instance}CON_HYSSEL_${options}          ((uint32_t)(_DAC${instance}CON_HYSSEL_MASK & ((uint32_t)(${options_index}) << _DAC${instance}CON_HYSSEL_POSITION))) 
</#list>

//CMP DAC${instance}DAT DACDATAH set
#define DAC${instance}DAT_DACDAT_SET(value)              ((uint32_t)(_DAC${instance}DAT_DACDAT_MASK & ((uint32_t)(value) << _DAC${instance}DAT_DACDAT_POSITION))) 

//CMP DAC${instance}DAT DACDATAL set
#define DAC${instance}DAT_DACLOW_SET(value)              ((uint32_t)(_DAC${instance}DAT_DACLOW_MASK & ((uint32_t)(value) << _DAC${instance}DAT_DACLOW_POSITION))) 

//CMP DAC${instance}SLPCON HCFSEL set
#define DAC${instance}SLPCON_HCFSEL_SET(value)              ((uint32_t)(_DAC${instance}SLPCON_HCFSEL_MASK & ((uint32_t)(value) << _DAC${instance}SLPCON_HCFSEL_POSITION))) 

//CMP DAC${instance}SLPCON SLPSTOPA set
#define DAC${instance}SLPCON_SLPSTOPA_SET(value)              ((uint32_t)(_DAC${instance}SLPCON_SLPSTOPA_MASK & ((uint32_t)(value) << _DAC${instance}SLPCON_SLPSTOPA_POSITION))) 

//CMP DAC${instance}SLPCON SLPSTOPB set
#define DAC${instance}SLPCON_SLPSTOPB_SET(value)              ((uint32_t)(_DAC${instance}SLPCON_SLPSTOPB_MASK & ((uint32_t)(value) << _DAC${instance}SLPCON_SLPSTOPB_POSITION))) 

//CMP DAC${instance}SLPCON SLPSTRT set
#define DAC${instance}SLPCON_SLPSTRT_SET(value)              ((uint32_t)(_DAC${instance}SLPCON_SLPSTRT_MASK & ((uint32_t)(value) << _DAC${instance}SLPCON_SLPSTRT_POSITION))) 

#define CMP_FPDMDAC_ADDRESS ${calibrationFlashAddress}UL

// Section: Global Data

<#if cmpIntEnable>
static volatile CMP_OBJECT ${moduleName?lower_case}Obj;

</#if>
// Section: ${moduleName} Module APIs

void ${moduleName}_Initialize(void)
{           
    // Comparator Register settings
    DACCTRL1bits.FCLKDIV = ${DACCTRL_CTRL1__FCLKDIV}U; 
    <#if DAC_SLPCON__SLOPEN == true>
    DACCTRL2 = (DACCTRL2_SSTIME_SET(0x${DACCTRL_CTRL2__SSTIME}UL)
                |DACCTRL2_TMODTIME_SET(0x${DACCTRL_CTRL2__TMODTIME}UL));
    </#if>
    DAC${instance}CON =  (DAC${instance}CON_TMCB_SET(0x${.vars["DAC_CON__TMCB"]?number}U)
              |DAC${instance}CON_IRQM_${dacconIrqmOptions[.vars["DAC_CON__IRQM"]?number]}<#if DAC_CON__CBE>
              |_DAC${instance}CON_CBE_MASK</#if><#if DAC_CON__DACOEN>
              |_DAC${instance}CON_DACOEN_MASK</#if><#if DAC_CON__FLTREN>
              |_DAC${instance}CON_FLTREN_MASK</#if><#if DAC_CON__CMPPOL>
              |_DAC${instance}CON_CMPPOL_MASK</#if>
              |DAC${instance}CON_INSEL_${dacconInselOptions[.vars["DAC_CON__INSEL"]?number]}<#if DAC_CON__HYSPOL>
              |_DAC${instance}CON_HYSPOL_MASK</#if>
              |DAC${instance}CON_HYSSEL_${dacconHysselOptions[.vars["DAC_CON__HYSSEL"]?number]});
    
    //DAC Settings
    DAC${instance}DAT = (DAC${instance}DAT_DACDAT_SET(0x${.vars["DAC_DAT__DACDATAH"]}UL)
              |DAC${instance}DAT_DACLOW_SET(0x${.vars["DAC_DAT__DACDATAL"]}UL));
    
    DAC${instance}SLPCON = (DAC${instance}SLPCON_HCFSEL_SET(${.vars["DAC_SLPCON__HCFSEL"]?number})
              |DAC${instance}SLPCON_SLPSTOPA_SET(${.vars["DAC_SLPCON__SLPSTOPA"]?number})
              |DAC${instance}SLPCON_SLPSTOPB_SET(${.vars["DAC_SLPCON__SLPSTOPB"]?number})
              |DAC${instance}SLPCON_SLPSTRT_SET(${.vars["DAC_SLPCON__SLPSTRT"]?number})<#if DAC_SLPCON__SLOPEN>
              |_DAC${instance}SLPCON_SLOPEN_MASK</#if><#if DAC_SLPCON__HME>
              |_DAC${instance}SLPCON_HME_MASK</#if><#if DAC_SLPCON__TWME>
              |_DAC${instance}SLPCON_TWME_MASK</#if><#if DAC_SLPCON__PSE>
              |_DAC${instance}SLPCON_PSE_MASK</#if>);
    
    DAC${instance}SLPDAT = 0x${SLPDAT}UL;
    
    <#if cmpIntEnable == true>
    // Clearing IF flag before enabling the interrupt.
    _CMP${instance}IF = 0U;
    // Enabling ${moduleName} interrupt.
    _CMP${instance}IE = 1U;
    
    </#if>
    DAC${instance}CONbits.DACEN = 1U;
    DACCTRL1bits.ON = 1U;
}

void ${moduleName}_Deinitialize(void)
{ 
    DACCTRL1bits.ON = 0U;
    
    <#if cmpIntEnable == true>
    _CMP${instance}IF = 0U;
    _CMP${instance}IE = 0U;
    </#if>
    
    // Comparator Register settings
    DACCTRL1 = ${porDacctrl1};
    DACCTRL2 = ${porDacctrl2};
    DAC${instance}CON = 0x0UL;
    
    //DAC Settings
    DAC${instance}DAT = 0x0UL;
    DAC${instance}SLPCON = 0x0UL;
    DAC${instance}SLPDAT = 0x0UL;
}

void ${moduleName}_Calibrate(void)
{
    uint32_t *fpdmdac = (uint32_t*)CMP_FPDMDAC_ADDRESS;
    uint32_t fpdmdac_value = *fpdmdac;

    DACCTRL1bits.POSINLADJ = (uint8_t)((fpdmdac_value & _DACCTRL1_POSINLADJ_MASK) >> _DACCTRL1_POSINLADJ_POSITION);
    DACCTRL1bits.NEGINLADJ = (uint8_t)((fpdmdac_value & _DACCTRL1_NEGINLADJ_MASK) >> _DACCTRL1_NEGINLADJ_POSITION);
    DACCTRL1bits.DNLADJ = (uint8_t)((fpdmdac_value & _DACCTRL1_DNLADJ_MASK) >> _DACCTRL1_DNLADJ_POSITION);
    DACCTRL1bits.RREN = 1U;
}

<#if cmpIntEnable>
void ${moduleName}_EventCallbackRegister(CMP_CALLBACK callback,uintptr_t context)
{
    ${moduleName?lower_case}Obj.callback = callback;
    ${moduleName?lower_case}Obj.context = context;
}

void ${cmpIsrHandlerName}(void)
{
    // ${moduleName} callback function 
    if(${moduleName?lower_case}Obj.callback != NULL)
    {
        uintptr_t context = ${moduleName?lower_case}Obj.context;
        ${moduleName?lower_case}Obj.callback(context);
    } 
    
    // clear the ${moduleName} interrupt flag
    _CMP${instance}IF = 0U;
}
</#if>

/**
 End of File
*/