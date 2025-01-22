<#assign generateDoxygen = false>
<#assign monIntTypes = ["rdy", "mon", "fail", "warn"]>
/**
 * Clock Generated PLIB Header File
 * 
 * @file      plib_clk.h
 *            
 * @ingroup   plib_clk
 *            
 * @brief     This is the generated plib header file for the Clock
 *
 * @skipline  Harmony Chip support Package Version  {core.libVersion}
 *            
 * @skipline  Device : {core.deviceName}
*/

//{core.disclaimer}

#ifndef PLIB_CLK_H
#define PLIB_CLK_H

// /cond IGNORE_THIS
/* Provide C++ Compatibility */
#ifdef __cplusplus

    extern "C" {

#endif
// /endcond

// Section: Included Files

#include "device.h"
#include <stdint.h>
#include <stdbool.h>
#include "plib_clk_common.h"

// Section: CLOCK APIs

<#if generateDoxygen>
/**
 * @ingroup  clock_plib
 * @brief    Initializes all the CLOCK sources and clock switch configurations. 
 * @pre      none
 * @param    none
 * @return   none  
 */
</#if>
void CLOCK_Initialize(void);

<#if generateDoxygen>
/**
 * @ingroup     clock_plib
 * @brief       This inline function returns clock generator frequency in Hz
 * @pre         none
 * @param[in]   generator - instance of clock generator
 * @return      Clock frequency in Hz
 */
</#if>
inline static uint32_t CLOCK_GeneratorFrequencyGet(CLOCK_GENERATOR generator)
{
    uint32_t genFrequency = 0x0U;

    switch(generator)
    {
        <#list 1..maxClockGen as i>
        <#if (.vars["clkGen"+i+"Enable"]??) && (.vars["clkGen"+i+"Enable"])>
        case CLOCK_GENERATOR_${i}:
                genFrequency = ${.vars["clkGen"+i+"OutFrequency"]}UL;
                break;
        </#if>
        </#list>
        default:
                break;
    }
    return genFrequency;
}

<#if generateDoxygen>
/**
 * @ingroup     clock_plib
 * @brief       This inline function returns clock generator failure status.
 * @pre         none
 * @param       none
 * @return      32-bit status value. Use status masks in \ref CLOCK_FAIL_STATUS_MASKS to derive individual status.
 * @note        In interrupt mode this function has to be called inside  CombinedClockFailCallback 
 *              to know the status during failure event.
 */
</#if>
inline static uint32_t CLOCK_FailStatusGet(void)
{
    uint32_t failStatus = (uint32_t)CLKFAIL;
    CLKFAIL =  0x0U;
    return failStatus;   
}

<#if useClockMonitor>
<#if generateDoxygen>
/**
 * @ingroup     clock_plib
 * @brief       This inline function enables clock monitor
 * @pre         none
 * @param[in]   monitor - instance of clock monitor
 * @return      Clock frequency in Hz
 */
</#if>
inline static void CLOCK_MonitorEnable(CLOCK_MONITOR monitor)
{
    switch(monitor)
    {
        <#list 1..maxClockMon as i>
        <#if (.vars["cm"+i+"Enable"]??) &&  (.vars["cm"+i+"Enable"]== true)>
        case CLOCK_MONITOR_${i}:
            CM${i}CONbits.ON = 1U;
            break;
        </#if>
        </#list>
        default:
            break;
    }
}

<#if generateDoxygen>
/**
 * @ingroup     clock_plib
 * @brief       This inline function disables clock monitor
 * @pre         none
 * @param[in]   monitor - instance of clock monitor
 * @return      none
 */
</#if>
inline static void CLOCK_MonitorDisable(CLOCK_MONITOR monitor)
{
    switch(monitor)
    {
        <#list 1..maxClockMon as i>
        <#if (.vars["cm"+i+"Enable"]??) &&  (.vars["cm"+i+"Enable"]== true)>
        case CLOCK_MONITOR_${i}:
            CM${i}CONbits.ON = 0U;
            break;
        </#if>
        </#list>
        default:
            break;
    }
}

<#if generateDoxygen>
/**
 * @ingroup     clock_plib
 * @brief       This inline function checks if the clock monitor capture data is ready
 * @pre         none
 * @param[in]   monitor - instance of clock monitor
 * @return      true - clock capture data available
 * @return      false - clock capture data not started or in progress 
 */
</#if>
inline static bool CLOCK_MonitorIsReady(CLOCK_MONITOR monitor)
{
    bool status = false;
    switch(monitor)
    {
        <#list 1..maxClockMon as i>
        <#if (.vars["c"+i+"rdyInterruptFlagBit"]??) &&  (.vars["cm"+i+"Enable"]??) &&  (.vars["cm"+i+"Enable"]== true)>
        case CLOCK_MONITOR_${i}:
            status = (bool)${.vars["c"+i+"rdyInterruptFlagBit"]}; 
            ${.vars["c"+i+"rdyInterruptFlagBit"]} = 0U;
            break;
        </#if>
        </#list>
        default:
            break;
    }
    return status;
}

<#if generateDoxygen>
/**
 * @ingroup     clock_plib
 * @brief       This inline function returns the accumulated data after the capture.
 * @pre         \ref CLOCK_Monitor_IsReady to be called before calling this function in non-interrupt operation
 * @param[in]   monitor - instance of clock monitor
 * @return      Captured count
 */
</#if>
inline static uint32_t CLOCK_MonitorAccumulatedCountGet(CLOCK_MONITOR monitor)
{
    uint32_t capturedValue = 0x0U;
    switch(monitor)
    {
        <#list 1..maxClockMon as i>
        <#if (.vars["cm"+i+"Enable"]??) &&  (.vars["cm"+i+"Enable"]== true)>
        case CLOCK_MONITOR_${i}:
            capturedValue = (uint32_t)CM${i}BUF;
            break;
        </#if>
        </#list>
        default:
            break;
    }
    return capturedValue;
}

</#if>
<#if clockFailIntEnable == true>
<#if generateDoxygen>
/**
 * @ingroup     clock_plib
 * @brief       This function can be used to override default callback and to 
 *              define custom callback for CLOCK Combined Clock Fail event
 * @param       callback - Address of the callback routine
 * @param       context -  A value (usually a pointer) passed (unused) into the function 
 *              identified by the callback parameter
 * @return      none  
 */
</#if>
void CLOCK_CombinedClockFailCallbackRegister(CLOCK_CombinedFailCallback callback, uintptr_t context);
</#if>

<#if useClockMonitor>
<#list monIntTypes as type>
<#list 1..maxClockMon as i>
<#if (.vars["cm"+i+"Enable"]??) && (.vars["cm"+i+"Enable"] == true)>
<#if (.vars["cm"+i+type+"IntEnable"]??) &&  (.vars["cm"+i+type+"IntEnable"]== true)>
<#if generateDoxygen>
/**
 * @ingroup     clock_plib
 * @brief       This function can be used to override default callback 
 *              \ref CLOCK_Monitor${type}Callback and to define custom callback for 
 *              CLOCK Monitor ${type} event.
 * @param       monitor - Instance of the clock monitor
 * @param       callback - Address of the callback routine
 * @param       context -  A value (usually a pointer) passed (unused) into the function 
 *              identified by the callback parameter
 * @return      none
 */
</#if>
void CLOCK_Monitor${type?capitalize}CallbackRegister(CLOCK_MONITOR monitor, CLOCK_Monitor${type?capitalize}Callback callback, uintptr_t context);

<#break>
</#if>
</#if>
</#list>
</#list>
</#if>
// /cond IGNORE_THIS
/* Provide C++ Compatibility */
#ifdef __cplusplus

    }

#endif
// /endcond

#endif // PLIB_CLK_H

/*******************************************************************************
 End of File
*/

