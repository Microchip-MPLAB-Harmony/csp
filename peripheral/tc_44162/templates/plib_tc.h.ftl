/*******************************************************************************
  TC Peripheral Library Interface Header File

  Company
    Microchip Technology Inc.

  File Name
    plib_${TC_INSTANCE_NAME?lower_case}.h

  Summary
    TC peripheral library interface.

  Description
    This file defines the interface to the TC peripheral library.  This
    library provides access to and control of the associated peripheral
    instance.

******************************************************************************/

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

#ifndef PLIB_${TC_INSTANCE_NAME}_H    // Guards against multiple inclusion
#define PLIB_${TC_INSTANCE_NAME}_H


// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

/*  This section lists the other files that are included in this file.
*/


#include "plib_tc_common.h"

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

// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************
/* The following functions make up the methods (set of possible operations) of
   this interface.
*/

// *****************************************************************************
 <#compress>
<#assign TC_UNSIGNED_INT_TYPE = "uint16_t">
<#assign TC_SIGNED_INT_TYPE = "int16_t">
<#if TIMER_WIDTH == 32>
<#assign TC_UNSIGNED_INT_TYPE = "uint32_t">
<#assign TC_SIGNED_INT_TYPE = "int32_t">
</#if>
 </#compress>

<#assign start = 0>
<#-- start index of the for loop. In quadrature position mode channel 0 and channel 1 are used. And in quadrature speed mode, all 3 channels are used -->
<#if TC_ENABLE_QEI == true>
    <#compress>
    <#if TC_BMR_POSEN == "POSITION">
        <#if TC_INDEX_PULSE == true>
            <#assign start = 2>
        <#else>
            <#assign start = 1>
        </#if>
    <#else>
        <#if TC_INDEX_PULSE == true>
            <#assign start = 3>
        <#else>
            <#assign start = 1>
        </#if>
    </#if>
    </#compress>       
<#if TC_BMR_POSEN == "SPEED">
#define ${TC_INSTANCE_NAME}_CH2_FrequencyGet()     (uint32_t)(${TC3_CLOCK_FREQ}UL)

</#if>
void ${TC_INSTANCE_NAME}_QuadratureInitialize (void);

void ${TC_INSTANCE_NAME}_QuadratureStart (void);

void ${TC_INSTANCE_NAME}_QuadratureStop (void);

<#if TC_INDEX_PULSE == true>
__STATIC_INLINE ${TC_UNSIGNED_INT_TYPE} ${TC_INSTANCE_NAME}_QuadratureRevolutionsGet (void)
{
    return (${TC_INSTANCE_NAME}_REGS->TC_CHANNEL[1].TC_CV);
}
</#if>

<#if TC_BMR_POSEN == "SPEED">

__STATIC_INLINE ${TC_UNSIGNED_INT_TYPE} ${TC_INSTANCE_NAME}_QuadratureSpeedGet (void)
{
    return ${TC_INSTANCE_NAME}_REGS->TC_CHANNEL[0].TC_CV;
}

<#else>
__STATIC_INLINE ${TC_SIGNED_INT_TYPE} ${TC_INSTANCE_NAME}_QuadraturePositionGet (void)
{
    return (${TC_INSTANCE_NAME}_REGS->TC_CHANNEL[0].TC_CV);
}
</#if>

<#if TC_QIER_IDX == true || TC_QIER_QERR == true || TC_QEI_IER_CPCS == true>
    <#lt>/* Register callback for quadrature interrupt */
    <#lt>void ${TC_INSTANCE_NAME}_QuadratureCallbackRegister(TC_QUADRATURE_CALLBACK callback, uintptr_t context);
<#else>
TC_QUADRATURE_STATUS ${TC_INSTANCE_NAME}_QuadratureStatusGet(void);
</#if>
</#if>
<#list start..(TC_MAX_CHANNELS-1) as i>
    <#if i == TC_MAX_CHANNELS>
        <#break>
    </#if> <#-- break the loop if quadrature mode is enabled -->
    <#if TC_ENABLE_QEI == true && TC_INDEX_PULSE == false && TC_BMR_POSEN == "SPEED" && i == 2>
        <#break>
    </#if>
<#assign TC_CH_ENABLE = "TC" + i + "_ENABLE">
<#assign TC_CH_OPERATINGMODE = "TC" + i +"_OPERATING_MODE">
<#assign CH_NUM = i >
<#assign TC_TIMER_SYS_TIME_CONNECTED = "TC"+i+"_SYS_TIME_CONNECTED">
<#assign TC_CH_CLOCK_FREQ = "TC"+i+"_CLOCK_FREQ">
<#assign TC_TIMER_IER_CPCS = "TC"+i+"_IER_CPCS">
<#assign TC_TIMER_IER_CPAS = "TC"+i+"_IER_CPAS">
<#assign TC_COMPARE_IER_CPCS = "TC"+i+"_COMPARE_IER_CPCS">
<#assign TC_CAPTURE_IER_LDRAS = "TC"+i+"_CAPTURE_IER_LDRAS">
<#assign TC_CAPTURE_IER_LDRBS = "TC"+i+"_CAPTURE_IER_LDRBS">
<#assign TC_CAPTURE_IER_COVFS = "TC"+i+"_CAPTURE_IER_COVFS">

<#if .vars[TC_CH_ENABLE] == true>

<#if .vars[TC_CH_OPERATINGMODE] == "TIMER">

void ${TC_INSTANCE_NAME}_CH${CH_NUM}_TimerInitialize (void);

void ${TC_INSTANCE_NAME}_CH${CH_NUM}_TimerStart (void);

void ${TC_INSTANCE_NAME}_CH${CH_NUM}_TimerStop (void);

void ${TC_INSTANCE_NAME}_CH${CH_NUM}_TimerPeriodSet (${TC_UNSIGNED_INT_TYPE} period);

<#if .vars[TC_TIMER_SYS_TIME_CONNECTED] == true>
void ${TC_INSTANCE_NAME}_CH${CH_NUM}_TimerCompareSet (${TC_UNSIGNED_INT_TYPE} compare);
</#if>

uint32_t ${TC_INSTANCE_NAME}_CH${CH_NUM}_TimerFrequencyGet (void);

${TC_UNSIGNED_INT_TYPE} ${TC_INSTANCE_NAME}_CH${CH_NUM}_TimerPeriodGet (void);

${TC_UNSIGNED_INT_TYPE} ${TC_INSTANCE_NAME}_CH${CH_NUM}_TimerCounterGet (void);

<#if (.vars[TC_TIMER_IER_CPCS] == true) || (.vars[TC_TIMER_IER_CPAS] == true)>
void ${TC_INSTANCE_NAME}_CH${CH_NUM}_TimerCallbackRegister(TC_TIMER_CALLBACK callback, uintptr_t context);
<#else>
bool ${TC_INSTANCE_NAME}_CH${CH_NUM}_TimerPeriodHasExpired(void);
</#if>
</#if>

<#if .vars[TC_CH_OPERATINGMODE] == "CAPTURE">

void ${TC_INSTANCE_NAME}_CH${CH_NUM}_CaptureInitialize (void);

void ${TC_INSTANCE_NAME}_CH${CH_NUM}_CaptureStart (void);

void ${TC_INSTANCE_NAME}_CH${CH_NUM}_CaptureStop (void);

uint32_t ${TC_INSTANCE_NAME}_CH${CH_NUM}_CaptureFrequencyGet (void);

${TC_UNSIGNED_INT_TYPE} ${TC_INSTANCE_NAME}_CH${CH_NUM}_CaptureAGet (void);

${TC_UNSIGNED_INT_TYPE} ${TC_INSTANCE_NAME}_CH${CH_NUM}_CaptureBGet (void);

<#if .vars[TC_CAPTURE_IER_LDRAS] == true || .vars[TC_CAPTURE_IER_LDRBS] == true || .vars[TC_CAPTURE_IER_COVFS] == true>
void ${TC_INSTANCE_NAME}_CH${CH_NUM}_CaptureCallbackRegister(TC_CAPTURE_CALLBACK callback, uintptr_t context);

<#else>
TC_CAPTURE_STATUS ${TC_INSTANCE_NAME}_CH${CH_NUM}_CaptureStatusGet(void);
</#if>

</#if>

<#if .vars[TC_CH_OPERATINGMODE] == "COMPARE">

void ${TC_INSTANCE_NAME}_CH${CH_NUM}_CompareInitialize (void);

void ${TC_INSTANCE_NAME}_CH${CH_NUM}_CompareStart (void);

void ${TC_INSTANCE_NAME}_CH${CH_NUM}_CompareStop (void);

uint32_t ${TC_INSTANCE_NAME}_CH${CH_NUM}_CompareFrequencyGet (void);

void ${TC_INSTANCE_NAME}_CH${CH_NUM}_ComparePeriodSet (${TC_UNSIGNED_INT_TYPE} period);

${TC_UNSIGNED_INT_TYPE} ${TC_INSTANCE_NAME}_CH${CH_NUM}_ComparePeriodGet (void);

void ${TC_INSTANCE_NAME}_CH${CH_NUM}_CompareASet (${TC_UNSIGNED_INT_TYPE} value);

void ${TC_INSTANCE_NAME}_CH${CH_NUM}_CompareBSet (${TC_UNSIGNED_INT_TYPE} value);

<#if .vars[TC_COMPARE_IER_CPCS] == true>
void ${TC_INSTANCE_NAME}_CH${CH_NUM}_CompareCallbackRegister(TC_COMPARE_CALLBACK callback, uintptr_t context);

<#else>
TC_COMPARE_STATUS ${TC_INSTANCE_NAME}_CH${CH_NUM}_CompareStatusGet(void);
</#if>

</#if>

</#if>
</#list>

#endif //PLIB_${TC_INSTANCE_NAME}_H

/**
 End of File
*/
