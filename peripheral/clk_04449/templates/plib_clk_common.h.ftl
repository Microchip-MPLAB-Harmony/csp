<#assign generateDoxygen = false>
<#assign monIntTypes = ["rdy", "mon", "fail", "warn"]>
/*******************************************************************************
  Clock PLIB
 
  Company:
    Microchip Technology Inc.
 
  File Name:
    plib_clk_common.h
 
  Summary:
    Clock Common Header File
 
  Description:
    This file has prototype of all the interfaces which are common for all the
    Clock peripherals.
 
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

#ifndef PLIB_CLK_COMMON_H
#define PLIB_CLK_COMMON_H

// /cond IGNORE_THIS
/* Provide C++ Compatibility */
#ifdef __cplusplus

    extern "C" {

#endif
// /endcond

// Section: Included Files

#include <stdint.h>

<#if generateDoxygen>
/**
 @enum     CLOCK_GENERATOR
 @brief    CLOCK generator instances
*/
</#if>
typedef enum
{
    <#list 1..maxClockGen as i>
    <#if (.vars["clkGen"+i+"Enable"]??) && (.vars["clkGen"+i+"Enable"])>
    CLOCK_GENERATOR_${i} = ${i},    
	</#if>
    </#list>
    
${clockModuleString}

} CLOCK_GENERATOR;

<#if generateDoxygen>
/**
 @enum     CLOCK_FAIL_STATUS_MASKS
 @brief    Mask values for clock fail status 
*/
</#if>
typedef enum
{
    <#list 1..maxClockGen as i>
    <#if (.vars["clkGen"+i+"Enable"]??) && (.vars["clkGen"+i+"Enable"])>
    CLOCK_GEN${i}_FAIL_MASK = ${.vars["clkGen"+i+"ClkFailMask"]},   
    </#if>
    </#list>
    <#list 1..maxPllGen as i>
    <#if (.vars["pll"+i+"Enable"]??) && (.vars["pll"+i+"Enable"])>
    CLOCK_PLL${i}_FAIL_MASK = ${.vars["pll"+i+"ClkFailMask"]},    
    </#if>
    </#list>
} CLOCK_FAIL_STATUS_MASKS;
<#if useClockMonitor>

<#if generateDoxygen>
/**
 @enum     CLOCK_MONITOR
 @brief    CLOCK monitor instances
*/
</#if>
typedef enum
{
    <#list 1..maxClockMon as i>
    <#if (.vars["cm"+i+"Enable"]??) && (.vars["cm"+i+"Enable"] == true)>
    CLOCK_MONITOR_${i} = ${i},    
    </#if>
    </#list>
    CLOCK_MONITOR_MAX = ${maxClockMon}
} CLOCK_MONITOR;
</#if>

<#if useClockMonitor>
<#list monIntTypes as type>
<#list 1..maxClockMon as i>
<#if (.vars["cm"+i+type+"IntEnable"]??) &&  (.vars["cm"+i+type+"IntEnable"]== true)>
/** 
  @brief    Clock-Monitor callback function prototype
*/
typedef void (* CLOCK_Monitor${type?capitalize}Callback)(uintptr_t context);

<#break>
</#if>
</#list>
</#list>
</#if>
/** 
  @brief    Clock-Fail callback function prototype
*/
typedef void (* CLOCK_CombinedFailCallback)(uintptr_t context);

// /cond IGNORE_THIS
// Section: Local Objects **** Do Not Use ****

<#if useClockMonitor>
<#list monIntTypes as type>
<#list 1..maxClockMon as i>
<#if (.vars["cm"+i+type+"IntEnable"]??) &&  (.vars["cm"+i+type+"IntEnable"]== true)>
typedef struct
{
    CLOCK_Monitor${type?capitalize}Callback                        callback;
    uintptr_t                                           context;
} CLOCK_Monitor${type?capitalize}Object;

<#break>
</#if>
</#list>
</#list>
</#if>
typedef struct
{
    CLOCK_CombinedFailCallback                callback;
    uintptr_t                                 context;
} CLOCK_CombinedFailObject;

// /endcond

// /cond IGNORE_THIS
/* Provide C++ Compatibility */
#ifdef __cplusplus

    }

#endif
// /endcond

#endif // PLIB_CLK_COMMON_H

/*******************************************************************************
 End of File
*/


