/*******************************************************************************
  TC Peripheral Library Interface Header File

  Company
    Microchip Technology Inc.

  File Name
    plib_tc${INDEX}.h

  Summary
    TC peripheral library interface.

  Description
    This file defines the interface to the TC peripheral library.  This 
    library provides access to and control of the associated peripheral 
    instance.

******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
Copyright (c) 2017 released Microchip Technology Inc.  All rights reserved.

Microchip licenses to you the right to use, modify, copy and distribute
Software only when embedded on a Microchip microcontroller or digital signal
controller that is integrated into your product or third party product
(pursuant to the sublicense terms in the accompanying license agreement).

You should refer to the license agreement accompanying this Software for
additional information regarding your rights and obligations.
SOFTWARE AND DOCUMENTATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND,
EITHER EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION, ANY WARRANTY OF
MERCHANTABILITY, TITLE, NON-INFRINGEMENT AND FITNESS FOR A PARTICULAR PURPOSE.
IN NO EVENT SHALL MICROCHIP OR ITS LICENSORS BE LIABLE OR OBLIGATED UNDER
CONTRACT, NEGLIGENCE, STRICT LIABILITY, CONTRIBUTION, BREACH OF WARRANTY, OR
OTHER LEGAL EQUITABLE THEORY ANY DIRECT OR INDIRECT DAMAGES OR EXPENSES
INCLUDING BUT NOT LIMITED TO ANY INCIDENTAL, SPECIAL, INDIRECT, PUNITIVE OR
CONSEQUENTIAL DAMAGES, LOST PROFITS OR LOST DATA, COST OF PROCUREMENT OF
SUBSTITUTE GOODS, TECHNOLOGY, SERVICES, OR ANY CLAIMS BY THIRD PARTIES
(INCLUDING BUT NOT LIMITED TO ANY DEFENSE THEREOF), OR OTHER SIMILAR COSTS.
*******************************************************************************/
// DOM-IGNORE-END

#ifndef PLIB_TC${INDEX}_H    // Guards against multiple inclusion
#define PLIB_TC${INDEX}_H


// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

/*  This section lists the other files that are included in this file.
*/

#include "plib_tc.h"

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
<#assign start = 0> 
<#-- start index of the for loop. In quadrature position mode channel 0 and channel 1 are used. And in quadrature speed mode, all 3 channels are used -->
<#if TC_ENABLE_QEI == true>
	<#compress>
	<#if TC_BMR_POSEN == "POSITION">
		<#assign start = 2>
	<#else>
		<#assign start = 3>
	</#if>
	</#compress>
<#if TC_BMR_POSEN == "SPEED">
#define TC${INDEX}_CH2_FrequencyGet() 	(uint32_t)(${TC3_CLOCK_FREQ}UL)

</#if>
void TC${INDEX}_QuadratureInitialize (void);

void TC${INDEX}_QuadratureStart (void);

void TC${INDEX}_QuadratureStop (void);

uint32_t TC${INDEX}_QuadraturePositionGet (void);
<#if TC_BMR_POSEN == "SPEED">

uint32_t TC${INDEX}_QuadratureSpeedGet (void);
</#if>

TC_QUADRATURE_STATUS TC${INDEX}_QuadratureStatusGet(void);

<#if TC_QIER_IDX == true || TC_QIER_QERR == true>
	<#lt>/* Register callback for quadrature interrupt */
	<#lt>void TC${INDEX}_QuadratureCallbackRegister(TC_CALLBACK callback, uintptr_t context);

	<#lt>void TC${INDEX}_CH0_InterruptHandler(void);	
	
</#if>
</#if>
<#list start..2 as i>
	<#if i == 3>
		<#break>
	</#if> <#-- break the loop if quadrature mode is enabled -->
<#assign TC_CH_ENABLE = "TC" + i + "_ENABLE">
<#assign TC_CH_OPERATINGMODE = "TC" + i +"_OPERATING_MODE">
<#assign CH_NUM = i >
<#assign TC_CH_CLOCK_FREQ = "TC"+i+"_CLOCK_FREQ">
<#assign TC_TIMER_IER_CPCS = "TC"+i+"_IER_CPCS">
<#assign TC_COMPARE_IER_CPCS = "TC"+i+"_COMPARE_IER_CPCS">
<#assign TC_CAPTURE_IER_LDRAS = "TC"+i+"_CAPTURE_IER_LDRAS">
<#assign TC_CAPTURE_IER_LDRBS = "TC"+i+"_CAPTURE_IER_LDRBS">
<#assign TC_CAPTURE_IER_COVFS = "TC"+i+"_CAPTURE_IER_COVFS">

<#if .vars[TC_CH_ENABLE] == true>

<#if .vars[TC_CH_OPERATINGMODE] == "TIMER">

#define TC${INDEX}_CH${CH_NUM}_TimerFrequencyGet() (uint32_t)(${.vars[TC_CH_CLOCK_FREQ]}UL)

void TC${INDEX}_CH${CH_NUM}_TimerInitialize (void);

void TC${INDEX}_CH${CH_NUM}_TimerStart (void);

void TC${INDEX}_CH${CH_NUM}_TimerStop (void);

void TC${INDEX}_CH${CH_NUM}_TimerPeriodSet (uint16_t period);

uint16_t TC${INDEX}_CH${CH_NUM}_TimerPeriodGet (void);

uint16_t TC${INDEX}_CH${CH_NUM}_TimerCounterGet (void);

bool TC${INDEX}_CH${CH_NUM}_TimerPeriodHasExpired(void);

<#if .vars[TC_TIMER_IER_CPCS] == true>
void TC${INDEX}_CH${CH_NUM}_TimerCallbackRegister(TC_CALLBACK callback, uintptr_t context);

void TC${INDEX}_CH${CH_NUM}_InterruptHandler(void);
</#if>
</#if>

<#if .vars[TC_CH_OPERATINGMODE] == "CAPTURE">

#define TC${INDEX}_CH${CH_NUM}_CaptureFrequencyGet() (uint32_t)(${.vars[TC_CH_CLOCK_FREQ]}UL)

void TC${INDEX}_CH${CH_NUM}_CaptureInitialize (void);

void TC${INDEX}_CH${CH_NUM}_CaptureStart (void);

void TC${INDEX}_CH${CH_NUM}_CaptureStop (void);

uint16_t TC${INDEX}_CH${CH_NUM}_CaptureAGet (void);

uint16_t TC${INDEX}_CH${CH_NUM}_CaptureBGet (void);

TC_CAPTURE_STATUS TC${INDEX}_CH${CH_NUM}_CaptureStatusGet(void);

<#if .vars[TC_CAPTURE_IER_LDRAS] == true || .vars[TC_CAPTURE_IER_LDRBS] == true || .vars[TC_CAPTURE_IER_COVFS] == true>
void TC${INDEX}_CH${CH_NUM}_CaptureCallbackRegister(TC_CALLBACK callback, uintptr_t context);

void TC${INDEX}_CH${CH_NUM}_InterruptHandler(void);
</#if>

</#if>

<#if .vars[TC_CH_OPERATINGMODE] == "COMPARE">

#define TC${INDEX}_CH${CH_NUM}_CompareFrequencyGet() (uint32_t)(${.vars[TC_CH_CLOCK_FREQ]}UL)

void TC${INDEX}_CH${CH_NUM}_CompareInitialize (void);

void TC${INDEX}_CH${CH_NUM}_CompareStart (void);

void TC${INDEX}_CH${CH_NUM}_CompareStop (void);

void TC${INDEX}_CH${CH_NUM}_ComparePeriodSet (uint16_t period);

uint16_t TC${INDEX}_CH${CH_NUM}_ComparePeriodGet (void);

void TC${INDEX}_CH${CH_NUM}_CompareASet (uint16_t value);

void TC${INDEX}_CH${CH_NUM}_CompareBSet (uint16_t value);

TC_COMPARE_STATUS TC${INDEX}_CH${CH_NUM}_CompareStatusGet(void);

<#if .vars[TC_COMPARE_IER_CPCS] == true>
void TC${INDEX}_CH${CH_NUM}_CompareCallbackRegister(TC_CALLBACK callback, uintptr_t context);

void TC${INDEX}_CH${CH_NUM}_InterruptHandler(void);
</#if>

</#if>

</#if>
</#list>

#endif //PLIB_TC${INDEX}_H

/**
 End of File
*/
