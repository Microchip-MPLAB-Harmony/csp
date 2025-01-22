<#assign generateDoxygen = false>
<#assign monIntTypes = ["rdy", "mon", "fail", "warn"]>
/**
 * Clock Generated Driver Types Header File
 * 
 * @file      plib_clk_common.h
 *            
 * @defgroup  plib_clk plib_clk_doc
 *            
 * @brief     Clock PLIB for dsPIC33A MCUs
 *
 * @skipline  Harmony Chip support Package Version  {core.libVersion}
 *            
 * @skipline  Device : {core.deviceName}
*/

//{core.disclaimer}

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
 @ingroup  clock_plib
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
 @ingroup  clock_plib
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
 @ingroup  clock_plib
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
  @ingroup  plib_clk
  @brief    Clock-Monitor callback function prototype
*/
typedef void (* CLOCK_Monitor${type?capitalize}Callback)(uintptr_t context);

<#break>
</#if>
</#list>
</#list>
</#if>
/** 
  @ingroup  plib_clk
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


