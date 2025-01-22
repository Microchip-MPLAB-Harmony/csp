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

#include <stdbool.h>
#include <stdint.h>
#include "device.h"
#include "plib_cmp_common.h"

// Section: Data Type Definitions

<#if generateDoxygen> 
/**
 * @brief    This macro defines input clock for ${moduleName} 
 */
</#if>
#define ${moduleName}_DAC_CLOCK_FREQUENCY ${cmpDacInputClock}UL

// Section: ${moduleName} Module APIs

<#if generateDoxygen> 
/**
 * @brief    Initialize the ${moduleName} module
 * @param    none
 * @return   none  
 */
</#if>
void ${moduleName}_Initialize(void);

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
 * @brief    Calibrates the ${moduleName} module and enables ripple reduction mode
 * @param    none
 * @return   none  
 */
</#if>
void ${moduleName}_Calibrate(void);
 
<#if generateDoxygen>  
/**
 * @brief    This inline function returns the comparator output status 
 * @param    none
 * @return   true   - Comparator output is high
 * @return   false  - Comparator output is low
 */
</#if>
inline static bool ${moduleName}_StatusGet(void)
{
    return (bool)(DAC${instance}CONbits.CMPSTAT);
}

<#if generateDoxygen> 
/**
 * @brief    This inline function enables the common DAC module
 * @param    none
 * @return   none 
 */
</#if>
inline static void ${moduleName}_Enable(void)
{
    DACCTRL1bits.ON = 1U;
}

<#if generateDoxygen>     
/**
 * @brief    This inline function disables the common DAC module
 * @param    none
 * @return   none  
 */
</#if>
inline static void ${moduleName}_Disable(void)
{
    DACCTRL1bits.ON = 0U;
}

<#---if isDacDcModeEnabled == true--->
<#if DAC_MODE == "DC-Mode">
<#if generateDoxygen> 
/**
 * @brief    This inline function enables the individual DAC module
 * @param    none
 * @return   none 
 */
</#if>
inline static void ${moduleName}_DACEnable(void)
{
    DAC${instance}CONbits.DACEN = 1U;
}

<#if generateDoxygen>    
/**
 * @brief    This inline function disables the individual DAC module
 * @param    none
 * @return   none
 */
</#if>
inline static void ${moduleName}_DACDisable(void)
{
    DAC${instance}CONbits.DACEN = 0U;
}

<#if generateDoxygen>
/**
 * @brief      This inline function writes DAC data to register
 * @param[in]  value - DAC Data write value
 * @return     none 
 */
</#if>
inline static void ${moduleName}_DACDataWrite(size_t value)
{
    DAC${instance}DATbits.DACDAT = value;
}

</#if>
<#if DAC_SLPCON__SLOPEN == true>
<#if generateDoxygen>
/**
 * @brief    This inline function enables the individual DAC module
 * @param    none
 * @return   none 
 */
</#if>
inline static void ${moduleName}_DACEnable(void)
{
    DAC${instance}CONbits.DACEN = 1U;
}

<#if generateDoxygen>   
/**
 * @brief    This inline function disables the individual DAC module
 * @param    none
 * @return   none
 */
</#if>
inline static void ${moduleName}_DACDisable(void)
{
    DAC${instance}CONbits.DACEN = 0U;
}

<#if generateDoxygen>
/**
 * @brief       This inline function writes higher limit of the slope
 * @param[in]   dacHighLimit - higher limit of slope
 * @return      none
 */
</#if>
inline static void ${moduleName}_DACDataHighWrite(uint16_t dacHighLimit)
{
    DAC${instance}DATbits.DACDAT = dacHighLimit;
}

<#if generateDoxygen>
/**
 * @brief       This inline function writes lower limit of the slope
 * @param[in]   dacLowLimit - lower limit of slope
 * @return      none
 */
</#if>
inline static void ${moduleName}_DACDataLowWrite(uint16_t dacLowLimit)
{
    DAC${instance}DATbits.DACLOW = dacLowLimit;
}

<#if generateDoxygen>
/**
 * @brief       This inline function writes slope rate
 * @param[in]   slopeRate - inclination slope rate
 * @return      none
 */
</#if>
inline static void ${moduleName}_DACSlopeWrite(uint16_t slopeRate)
{
    DAC${instance}SLPDATbits.SLPDAT = slopeRate;
}

<#if generateDoxygen>
/**
 * @brief      This inline function sets the slope data update mode
 * @param[in]  \ref CMP_DAC_SLOPE_UPDATE_MODE - update modes
 * @return     none 
 */
</#if>
inline static void ${moduleName}_DACSlopeUpdateMode(CMP_DAC_SLOPE_UPDATE_MODE updateMode)
{
    DAC${instance}CONbits.EXTUPD = updateMode;
}

</#if>
<#if cmpIntEnable>
<#if generateDoxygen>
/**
 * @brief      This function can be used to override default callback and to 
 *             define custom callback for ${moduleName} event
 * @param[in]  handler - Address of the callback function.  
 * @return     none  
 */
</#if>
void ${moduleName}_EventCallbackRegister(CMP_CALLBACK callback,uintptr_t context);
</#if>

#endif //PLIB_${moduleName}_H

/**
  End of File
*/

