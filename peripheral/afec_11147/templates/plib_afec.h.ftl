/*******************************************************************************
  AFEC Peripheral Library Interface Header File

  Company
    Microchip Technology Inc.

  File Name
    plib_afec${INDEX}.h

  Summary
    AFEC peripheral library interface.

  Description
    This file defines the interface to the AFEC peripheral library.  This 
    library provides access to and control of the associated peripheral 
    instance.

  Remarks:
    This header is for documentation only.  The actual afec<x> headers will be
    generated as required by the MCC (where <x> is the peripheral instance 
    number).

    Every interface symbol has a lower-case 'x' in it following the "AFEC" 
    abbreviation.  This 'x' will be replaced by the peripheral instance number
    in the generated headers.  These are the actual functions that should be
    used.
*******************************************************************************/

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

#ifndef PLIB_AFEC${INDEX}_H    // Guards against multiple inclusion
#define PLIB_AFEC${INDEX}_H


// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

/*  This section lists the other files that are included in this file.
*/

#include <xc.h>
#include <stdint.h>
#include <stdbool.h>
#include <sys/attribs.h>
#include <plib_afec.h>

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
<#if AFEC_CHER_CH0 == true>
<#if AFEC_CH0_NEG_INP != "GND">
<#if ((AFEC_EMR_SIGNMODE == "ALL_UNSIGNED") || (AFEC_EMR_SIGNMODE == "SE_SIGN_DF_UNSG")) >
<#if (AFEC_EMR_RES == "NO_AVERAGE")>
#define AFEC${INDEX}_CH0_MAX_OUTPUT  (4095U)
#define AFEC${INDEX}_CH0_MIN_OUTPUT  (0U)
<#elseif (AFEC_EMR_RES == "OSR4")>
#define AFEC${INDEX}_CH0_MAX_OUTPUT  (8191U)
#define AFEC${INDEX}_CH0_MIN_OUTPUT  (0U)
<#elseif (AFEC_EMR_RES == "OSR16")>
#define AFEC${INDEX}_CH0_MAX_OUTPUT  (16383U)
#define AFEC${INDEX}_CH0_MIN_OUTPUT  (0U)
<#elseif (AFEC_EMR_RES == "OSR64")>
#define AFEC${INDEX}_CH0_MAX_OUTPUT  (32767U)
#define AFEC${INDEX}_CH0_MIN_OUTPUT  (0U)
<#else>
#define AFEC${INDEX}_CH0_MAX_OUTPUT  (65535U)
#define AFEC${INDEX}_CH0_MIN_OUTPUT  (0U)
</#if>
</#if>
<#if ((AFEC_EMR_SIGNMODE == "ALL_SIGNED") || (AFEC_EMR_SIGNMODE == "SE_UNSG_DF_SIGN")) >
<#if (AFEC_EMR_RES == "NO_AVERAGE")>
#define AFEC${INDEX}_CH0_MAX_OUTPUT  (2047)
#define AFEC${INDEX}_CH0_MIN_OUTPUT  (-2048)
<#elseif (AFEC_EMR_RES == "OSR4")>
#define AFEC${INDEX}_CH0_MAX_OUTPUT  (4095)
#define AFEC${INDEX}_CH0_MIN_OUTPUT  (-4096)
<#elseif (AFEC_EMR_RES == "OSR16")>
#define AFEC${INDEX}_CH0_MAX_OUTPUT  (8191)
#define AFEC${INDEX}_CH0_MIN_OUTPUT  (-8192)
<#elseif (AFEC_EMR_RES == "OSR64")>
#define AFEC${INDEX}_CH0_MAX_OUTPUT  (16383)
#define AFEC${INDEX}_CH0_MIN_OUTPUT  (-16384)
<#else>
#define AFEC${INDEX}_CH0_MAX_OUTPUT  (32767)
#define AFEC${INDEX}_CH0_MIN_OUTPUT  (-32768)
</#if>
</#if>
<#else>
<#if ((AFEC_EMR_SIGNMODE == "ALL_UNSIGNED") || (AFEC_EMR_SIGNMODE == "SE_UNSG_DF_SIGN")) >
<#if (AFEC_EMR_RES == "NO_AVERAGE")>
#define AFEC${INDEX}_CH0_MAX_OUTPUT  (4095U)
#define AFEC${INDEX}_CH0_MIN_OUTPUT  (0U)
<#elseif (AFEC_EMR_RES == "OSR4")>
#define AFEC${INDEX}_CH0_MAX_OUTPUT  (8191U)
#define AFEC${INDEX}_CH0_MIN_OUTPUT  (0U)
<#elseif (AFEC_EMR_RES == "OSR16")>
#define AFEC${INDEX}_CH0_MAX_OUTPUT  (16383U)
#define AFEC${INDEX}_CH0_MIN_OUTPUT  (0U)
<#elseif (AFEC_EMR_RES == "OSR64")>
#define AFEC${INDEX}_CH0_MAX_OUTPUT  (32767U)
#define AFEC${INDEX}_CH0_MIN_OUTPUT  (0U)
<#else>
#define AFEC${INDEX}_CH0_MAX_OUTPUT  (65535U)
#define AFEC${INDEX}_CH0_MIN_OUTPUT  (0U)
</#if>
</#if>
<#if ((AFEC_EMR_SIGNMODE == "ALL_SIGNED") || (AFEC_EMR_SIGNMODE == "SE_SIGN_DF_UNSG")) >
<#if (AFEC_EMR_RES == "NO_AVERAGE")>
#define AFEC${INDEX}_CH0_MAX_OUTPUT  (2047)
#define AFEC${INDEX}_CH0_MIN_OUTPUT  (-2048)
<#elseif (AFEC_EMR_RES == "OSR4")>
#define AFEC${INDEX}_CH0_MAX_OUTPUT  (4095)
#define AFEC${INDEX}_CH0_MIN_OUTPUT  (-4096)
<#elseif (AFEC_EMR_RES == "OSR16")>
#define AFEC${INDEX}_CH0_MAX_OUTPUT  (8191)
#define AFEC${INDEX}_CH0_MIN_OUTPUT  (-8192)
<#elseif (AFEC_EMR_RES == "OSR64")>
#define AFEC${INDEX}_CH0_MAX_OUTPUT  (16383)
#define AFEC${INDEX}_CH0_MIN_OUTPUT  (-16384)
<#else>
#define AFEC${INDEX}_CH0_MAX_OUTPUT  (32767)
#define AFEC${INDEX}_CH0_MIN_OUTPUT  (-32768)
</#if>
</#if>
</#if>
// *****************************************************************************
</#if>

<#if AFEC_CHER_CH1 == true>
<#if AFEC_CH0_NEG_INP == "GND">
<#if ((AFEC_EMR_SIGNMODE == "ALL_UNSIGNED") || (AFEC_EMR_SIGNMODE == "SE_UNSG_DF_SIGN")) >
<#if (AFEC_EMR_RES == "NO_AVERAGE")>
#define AFEC${INDEX}_CH1_MAX_OUTPUT  (4095U)
#define AFEC${INDEX}_CH1_MIN_OUTPUT  (0U)
<#elseif (AFEC_EMR_RES == "OSR4")>
#define AFEC${INDEX}_CH1_MAX_OUTPUT  (8191U)
#define AFEC${INDEX}_CH1_MIN_OUTPUT  (0U)
<#elseif (AFEC_EMR_RES == "OSR16")>
#define AFEC${INDEX}_CH1_MAX_OUTPUT  (16383U)
#define AFEC${INDEX}_CH1_MIN_OUTPUT  (0U)
<#elseif (AFEC_EMR_RES == "OSR64")>
#define AFEC${INDEX}_CH1_MAX_OUTPUT  (32767U)
#define AFEC${INDEX}_CH1_MIN_OUTPUT  (0U)
<#else>
#define AFEC${INDEX}_CH1_MAX_OUTPUT  (65535U)
#define AFEC${INDEX}_CH1_MIN_OUTPUT  (0U)
</#if>
</#if>
<#if ((AFEC_EMR_SIGNMODE == "ALL_SIGNED") || (AFEC_EMR_SIGNMODE == "SE_SIGN_DF_UNSG")) >
<#if (AFEC_EMR_RES == "NO_AVERAGE")>
#define AFEC${INDEX}_CH1_MAX_OUTPUT  (2047)
#define AFEC${INDEX}_CH1_MIN_OUTPUT  (-2048)
<#elseif (AFEC_EMR_RES == "OSR4")>
#define AFEC${INDEX}_CH1_MAX_OUTPUT  (4095)
#define AFEC${INDEX}_CH1_MIN_OUTPUT  (-4096)
<#elseif (AFEC_EMR_RES == "OSR16")>
#define AFEC${INDEX}_CH1_MAX_OUTPUT  (8191)
#define AFEC${INDEX}_CH1_MIN_OUTPUT  (-8192)
<#elseif (AFEC_EMR_RES == "OSR64")>
#define AFEC${INDEX}_CH1_MAX_OUTPUT  (16383)
#define AFEC${INDEX}_CH1_MIN_OUTPUT  (-16384)
<#else>
#define AFEC${INDEX}_CH1_MAX_OUTPUT  (32767)
#define AFEC${INDEX}_CH1_MIN_OUTPUT  (-32768)
</#if>
</#if>
</#if>
// *****************************************************************************
</#if>

<#if AFEC_CHER_CH2 == true>
<#if AFEC_CH2_NEG_INP != "GND">
<#if ((AFEC_EMR_SIGNMODE == "ALL_UNSIGNED") || (AFEC_EMR_SIGNMODE == "SE_SIGN_DF_UNSG")) >
<#if (AFEC_EMR_RES == "NO_AVERAGE")>
#define AFEC${INDEX}_CH2_MAX_OUTPUT  (4095U)
#define AFEC${INDEX}_CH2_MIN_OUTPUT  (0U)
<#elseif (AFEC_EMR_RES == "OSR4")>
#define AFEC${INDEX}_CH2_MAX_OUTPUT  (8191U)
#define AFEC${INDEX}_CH2_MIN_OUTPUT  (0U)
<#elseif (AFEC_EMR_RES == "OSR16")>
#define AFEC${INDEX}_CH2_MAX_OUTPUT  (16383U)
#define AFEC${INDEX}_CH2_MIN_OUTPUT  (0U)
<#elseif (AFEC_EMR_RES == "OSR64")>
#define AFEC${INDEX}_CH2_MAX_OUTPUT  (32767U)
#define AFEC${INDEX}_CH2_MIN_OUTPUT  (0U)
<#else>
#define AFEC${INDEX}_CH2_MAX_OUTPUT  (65535U)
#define AFEC${INDEX}_CH2_MIN_OUTPUT  (0U)
</#if>
</#if>
<#if ((AFEC_EMR_SIGNMODE == "ALL_SIGNED") || (AFEC_EMR_SIGNMODE == "SE_UNSG_DF_SIGN")) >
<#if (AFEC_EMR_RES == "NO_AVERAGE")>
#define AFEC${INDEX}_CH2_MAX_OUTPUT  (2047)
#define AFEC${INDEX}_CH2_MIN_OUTPUT  (-2048)
<#elseif (AFEC_EMR_RES == "OSR4")>
#define AFEC${INDEX}_CH2_MAX_OUTPUT  (4095)
#define AFEC${INDEX}_CH2_MIN_OUTPUT  (-4096)
<#elseif (AFEC_EMR_RES == "OSR16")>
#define AFEC${INDEX}_CH2_MAX_OUTPUT  (8191)
#define AFEC${INDEX}_CH2_MIN_OUTPUT  (-8192)
<#elseif (AFEC_EMR_RES == "OSR64")>
#define AFEC${INDEX}_CH2_MAX_OUTPUT  (16383)
#define AFEC${INDEX}_CH2_MIN_OUTPUT  (-16384)
<#else>
#define AFEC${INDEX}_CH2_MAX_OUTPUT  (32767)
#define AFEC${INDEX}_CH2_MIN_OUTPUT  (-32768)
</#if>
</#if>
<#else>
<#if ((AFEC_EMR_SIGNMODE == "ALL_UNSIGNED") || (AFEC_EMR_SIGNMODE == "SE_UNSG_DF_SIGN")) >
<#if (AFEC_EMR_RES == "NO_AVERAGE")>
#define AFEC${INDEX}_CH2_MAX_OUTPUT  (4095U)
#define AFEC${INDEX}_CH2_MIN_OUTPUT  (0U)
<#elseif (AFEC_EMR_RES == "OSR4")>
#define AFEC${INDEX}_CH2_MAX_OUTPUT  (8191U)
#define AFEC${INDEX}_CH2_MIN_OUTPUT  (0U)
<#elseif (AFEC_EMR_RES == "OSR16")>
#define AFEC${INDEX}_CH2_MAX_OUTPUT  (16383U)
#define AFEC${INDEX}_CH2_MIN_OUTPUT  (0U)
<#elseif (AFEC_EMR_RES == "OSR64")>
#define AFEC${INDEX}_CH2_MAX_OUTPUT  (32767U)
#define AFEC${INDEX}_CH2_MIN_OUTPUT  (0U)
<#else>
#define AFEC${INDEX}_CH2_MAX_OUTPUT  (65535U)
#define AFEC${INDEX}_CH2_MIN_OUTPUT  (0U)
</#if>
</#if>
<#if ((AFEC_EMR_SIGNMODE == "ALL_SIGNED") || (AFEC_EMR_SIGNMODE == "SE_SIGN_DF_UNSG")) >
<#if (AFEC_EMR_RES == "NO_AVERAGE")>
#define AFEC${INDEX}_CH2_MAX_OUTPUT  (2047)
#define AFEC${INDEX}_CH2_MIN_OUTPUT  (-2048)
<#elseif (AFEC_EMR_RES == "OSR4")>
#define AFEC${INDEX}_CH2_MAX_OUTPUT  (4095)
#define AFEC${INDEX}_CH2_MIN_OUTPUT  (-4096)
<#elseif (AFEC_EMR_RES == "OSR16")>
#define AFEC${INDEX}_CH2_MAX_OUTPUT  (8191)
#define AFEC${INDEX}_CH2_MIN_OUTPUT  (-8192)
<#elseif (AFEC_EMR_RES == "OSR64")>
#define AFEC${INDEX}_CH2_MAX_OUTPUT  (16383)
#define AFEC${INDEX}_CH2_MIN_OUTPUT  (-16384)
<#else>
#define AFEC${INDEX}_CH2_MAX_OUTPUT  (32767)
#define AFEC${INDEX}_CH2_MIN_OUTPUT  (-32768)
</#if>
</#if>
</#if>
// *****************************************************************************
</#if>

<#if AFEC_CHER_CH3 == true>
<#if AFEC_CH2_NEG_INP == "GND">
<#if ((AFEC_EMR_SIGNMODE == "ALL_UNSIGNED") || (AFEC_EMR_SIGNMODE == "SE_UNSG_DF_SIGN")) >
<#if (AFEC_EMR_RES == "NO_AVERAGE")>
#define AFEC${INDEX}_CH3_MAX_OUTPUT  (4095U)
#define AFEC${INDEX}_CH3_MIN_OUTPUT  (0U)
<#elseif (AFEC_EMR_RES == "OSR4")>
#define AFEC${INDEX}_CH3_MAX_OUTPUT  (8191U)
#define AFEC${INDEX}_CH3_MIN_OUTPUT  (0U)
<#elseif (AFEC_EMR_RES == "OSR16")>
#define AFEC${INDEX}_CH3_MAX_OUTPUT  (16383U)
#define AFEC${INDEX}_CH3_MIN_OUTPUT  (0U)
<#elseif (AFEC_EMR_RES == "OSR64")>
#define AFEC${INDEX}_CH3_MAX_OUTPUT  (32767U)
#define AFEC${INDEX}_CH3_MIN_OUTPUT  (0U)
<#else>
#define AFEC${INDEX}_CH3_MAX_OUTPUT  (65535U)
#define AFEC${INDEX}_CH3_MIN_OUTPUT  (0U)
</#if>
</#if>
<#if ((AFEC_EMR_SIGNMODE == "ALL_SIGNED") || (AFEC_EMR_SIGNMODE == "SE_SIGN_DF_UNSG")) >
<#if (AFEC_EMR_RES == "NO_AVERAGE")>
#define AFEC${INDEX}_CH3_MAX_OUTPUT  (2047)
#define AFEC${INDEX}_CH3_MIN_OUTPUT  (-2048)
<#elseif (AFEC_EMR_RES == "OSR4")>
#define AFEC${INDEX}_CH3_MAX_OUTPUT  (4095)
#define AFEC${INDEX}_CH3_MIN_OUTPUT  (-4096)
<#elseif (AFEC_EMR_RES == "OSR16")>
#define AFEC${INDEX}_CH3_MAX_OUTPUT  (8191)
#define AFEC${INDEX}_CH3_MIN_OUTPUT  (-8192)
<#elseif (AFEC_EMR_RES == "OSR64")>
#define AFEC${INDEX}_CH3_MAX_OUTPUT  (16383)
#define AFEC${INDEX}_CH3_MIN_OUTPUT  (-16384)
<#else>
#define AFEC${INDEX}_CH3_MAX_OUTPUT  (32767)
#define AFEC${INDEX}_CH3_MIN_OUTPUT  (-32768)
</#if>
</#if>
</#if>
// *****************************************************************************
</#if>

<#if AFEC_CHER_CH4 == true>
<#if AFEC_CH4_NEG_INP != "GND">
<#if ((AFEC_EMR_SIGNMODE == "ALL_UNSIGNED") || (AFEC_EMR_SIGNMODE == "SE_SIGN_DF_UNSG")) >
<#if (AFEC_EMR_RES == "NO_AVERAGE")>
#define AFEC${INDEX}_CH4_MAX_OUTPUT  (4095U)
#define AFEC${INDEX}_CH4_MIN_OUTPUT  (0U)
<#elseif (AFEC_EMR_RES == "OSR4")>
#define AFEC${INDEX}_CH4_MAX_OUTPUT  (8191U)
#define AFEC${INDEX}_CH4_MIN_OUTPUT  (0U)
<#elseif (AFEC_EMR_RES == "OSR16")>
#define AFEC${INDEX}_CH4_MAX_OUTPUT  (16383U)
#define AFEC${INDEX}_CH4_MIN_OUTPUT  (0U)
<#elseif (AFEC_EMR_RES == "OSR64")>
#define AFEC${INDEX}_CH4_MAX_OUTPUT  (32767U)
#define AFEC${INDEX}_CH4_MIN_OUTPUT  (0U)
<#else>
#define AFEC${INDEX}_CH4_MAX_OUTPUT  (65535U)
#define AFEC${INDEX}_CH4_MIN_OUTPUT  (0U)
</#if>
</#if>
<#if ((AFEC_EMR_SIGNMODE == "ALL_SIGNED") || (AFEC_EMR_SIGNMODE == "SE_UNSG_DF_SIGN")) >
<#if (AFEC_EMR_RES == "NO_AVERAGE")>
#define AFEC${INDEX}_CH4_MAX_OUTPUT  (2047)
#define AFEC${INDEX}_CH4_MIN_OUTPUT  (-2048)
<#elseif (AFEC_EMR_RES == "OSR4")>
#define AFEC${INDEX}_CH4_MAX_OUTPUT  (4095)
#define AFEC${INDEX}_CH4_MIN_OUTPUT  (-4096)
<#elseif (AFEC_EMR_RES == "OSR16")>
#define AFEC${INDEX}_CH4_MAX_OUTPUT  (8191)
#define AFEC${INDEX}_CH4_MIN_OUTPUT  (-8192)
<#elseif (AFEC_EMR_RES == "OSR64")>
#define AFEC${INDEX}_CH4_MAX_OUTPUT  (16383)
#define AFEC${INDEX}_CH4_MIN_OUTPUT  (-16384)
<#else>
#define AFEC${INDEX}_CH4_MAX_OUTPUT  (32767)
#define AFEC${INDEX}_CH4_MIN_OUTPUT  (-32768)
</#if>
</#if>
<#else>
<#if ((AFEC_EMR_SIGNMODE == "ALL_UNSIGNED") || (AFEC_EMR_SIGNMODE == "SE_UNSG_DF_SIGN")) >
<#if (AFEC_EMR_RES == "NO_AVERAGE")>
#define AFEC${INDEX}_CH4_MAX_OUTPUT  (4095U)
#define AFEC${INDEX}_CH4_MIN_OUTPUT  (0U)
<#elseif (AFEC_EMR_RES == "OSR4")>
#define AFEC${INDEX}_CH4_MAX_OUTPUT  (8191U)
#define AFEC${INDEX}_CH4_MIN_OUTPUT  (0U)
<#elseif (AFEC_EMR_RES == "OSR16")>
#define AFEC${INDEX}_CH4_MAX_OUTPUT  (16383U)
#define AFEC${INDEX}_CH4_MIN_OUTPUT  (0U)
<#elseif (AFEC_EMR_RES == "OSR64")>
#define AFEC${INDEX}_CH4_MAX_OUTPUT  (32767U)
#define AFEC${INDEX}_CH4_MIN_OUTPUT  (0U)
<#else>
#define AFEC${INDEX}_CH4_MAX_OUTPUT  (65535U)
#define AFEC${INDEX}_CH4_MIN_OUTPUT  (0U)
</#if>
</#if>
<#if ((AFEC_EMR_SIGNMODE == "ALL_SIGNED") || (AFEC_EMR_SIGNMODE == "SE_SIGN_DF_UNSG")) >
<#if (AFEC_EMR_RES == "NO_AVERAGE")>
#define AFEC${INDEX}_CH4_MAX_OUTPUT  (2047)
#define AFEC${INDEX}_CH4_MIN_OUTPUT  (-2048)
<#elseif (AFEC_EMR_RES == "OSR4")>
#define AFEC${INDEX}_CH4_MAX_OUTPUT  (4095)
#define AFEC${INDEX}_CH4_MIN_OUTPUT  (-4096)
<#elseif (AFEC_EMR_RES == "OSR16")>
#define AFEC${INDEX}_CH4_MAX_OUTPUT  (8191)
#define AFEC${INDEX}_CH4_MIN_OUTPUT  (-8192)
<#elseif (AFEC_EMR_RES == "OSR64")>
#define AFEC${INDEX}_CH4_MAX_OUTPUT  (16383)
#define AFEC${INDEX}_CH4_MIN_OUTPUT  (-16384)
<#else>
#define AFEC${INDEX}_CH4_MAX_OUTPUT  (32767)
#define AFEC${INDEX}_CH4_MIN_OUTPUT  (-32768)
</#if>
</#if>
</#if>
// *****************************************************************************
</#if>

<#if AFEC_CHER_CH5 == true>
<#if AFEC_CH4_NEG_INP == "GND">
<#if ((AFEC_EMR_SIGNMODE == "ALL_UNSIGNED") || (AFEC_EMR_SIGNMODE == "SE_UNSG_DF_SIGN")) >
<#if (AFEC_EMR_RES == "NO_AVERAGE")>
#define AFEC${INDEX}_CH5_MAX_OUTPUT  (4095U)
#define AFEC${INDEX}_CH5_MIN_OUTPUT  (0U)
<#elseif (AFEC_EMR_RES == "OSR4")>
#define AFEC${INDEX}_CH5_MAX_OUTPUT  (8191U)
#define AFEC${INDEX}_CH5_MIN_OUTPUT  (0U)
<#elseif (AFEC_EMR_RES == "OSR16")>
#define AFEC${INDEX}_CH5_MAX_OUTPUT  (16383U)
#define AFEC${INDEX}_CH5_MIN_OUTPUT  (0U)
<#elseif (AFEC_EMR_RES == "OSR64")>
#define AFEC${INDEX}_CH5_MAX_OUTPUT  (32767U)
#define AFEC${INDEX}_CH5_MIN_OUTPUT  (0U)
<#else>
#define AFEC${INDEX}_CH5_MAX_OUTPUT  (65535U)
#define AFEC${INDEX}_CH5_MIN_OUTPUT  (0U)
</#if>
</#if>
<#if ((AFEC_EMR_SIGNMODE == "ALL_SIGNED") || (AFEC_EMR_SIGNMODE == "SE_SIGN_DF_UNSG")) >
<#if (AFEC_EMR_RES == "NO_AVERAGE")>
#define AFEC${INDEX}_CH5_MAX_OUTPUT  (2047)
#define AFEC${INDEX}_CH5_MIN_OUTPUT  (-2048)
<#elseif (AFEC_EMR_RES == "OSR4")>
#define AFEC${INDEX}_CH5_MAX_OUTPUT  (4095)
#define AFEC${INDEX}_CH5_MIN_OUTPUT  (-4096)
<#elseif (AFEC_EMR_RES == "OSR16")>
#define AFEC${INDEX}_CH5_MAX_OUTPUT  (8191)
#define AFEC${INDEX}_CH5_MIN_OUTPUT  (-8192)
<#elseif (AFEC_EMR_RES == "OSR64")>
#define AFEC${INDEX}_CH5_MAX_OUTPUT  (16383)
#define AFEC${INDEX}_CH5_MIN_OUTPUT  (-16384)
<#else>
#define AFEC${INDEX}_CH5_MAX_OUTPUT  (32767)
#define AFEC${INDEX}_CH5_MIN_OUTPUT  (-32768)
</#if>
</#if>
</#if>
// *****************************************************************************
</#if>

<#if AFEC_CHER_CH6 == true>
<#if AFEC_CH6_NEG_INP != "GND">
<#if ((AFEC_EMR_SIGNMODE == "ALL_UNSIGNED") || (AFEC_EMR_SIGNMODE == "SE_SIGN_DF_UNSG")) >
<#if (AFEC_EMR_RES == "NO_AVERAGE")>
#define AFEC${INDEX}_CH6_MAX_OUTPUT  (4095U)
#define AFEC${INDEX}_CH6_MIN_OUTPUT  (0U)
<#elseif (AFEC_EMR_RES == "OSR4")>
#define AFEC${INDEX}_CH6_MAX_OUTPUT  (8191U)
#define AFEC${INDEX}_CH6_MIN_OUTPUT  (0U)
<#elseif (AFEC_EMR_RES == "OSR16")>
#define AFEC${INDEX}_CH6_MAX_OUTPUT  (16383U)
#define AFEC${INDEX}_CH6_MIN_OUTPUT  (0U)
<#elseif (AFEC_EMR_RES == "OSR64")>
#define AFEC${INDEX}_CH6_MAX_OUTPUT  (32767U)
#define AFEC${INDEX}_CH6_MIN_OUTPUT  (0U)
<#else>
#define AFEC${INDEX}_CH6_MAX_OUTPUT  (65535U)
#define AFEC${INDEX}_CH6_MIN_OUTPUT  (0U)
</#if>
</#if>
<#if ((AFEC_EMR_SIGNMODE == "ALL_SIGNED") || (AFEC_EMR_SIGNMODE == "SE_UNSG_DF_SIGN")) >
<#if (AFEC_EMR_RES == "NO_AVERAGE")>
#define AFEC${INDEX}_CH6_MAX_OUTPUT  (2047)
#define AFEC${INDEX}_CH6_MIN_OUTPUT  (-2048)
<#elseif (AFEC_EMR_RES == "OSR4")>
#define AFEC${INDEX}_CH6_MAX_OUTPUT  (4095)
#define AFEC${INDEX}_CH6_MIN_OUTPUT  (-4096)
<#elseif (AFEC_EMR_RES == "OSR16")>
#define AFEC${INDEX}_CH6_MAX_OUTPUT  (8191)
#define AFEC${INDEX}_CH6_MIN_OUTPUT  (-8192)
<#elseif (AFEC_EMR_RES == "OSR64")>
#define AFEC${INDEX}_CH6_MAX_OUTPUT  (16383)
#define AFEC${INDEX}_CH6_MIN_OUTPUT  (-16384)
<#else>
#define AFEC${INDEX}_CH6_MAX_OUTPUT  (32767)
#define AFEC${INDEX}_CH6_MIN_OUTPUT  (-32768)
</#if>
</#if>
<#else>
<#if ((AFEC_EMR_SIGNMODE == "ALL_UNSIGNED") || (AFEC_EMR_SIGNMODE == "SE_UNSG_DF_SIGN")) >
<#if (AFEC_EMR_RES == "NO_AVERAGE")>
#define AFEC${INDEX}_CH6_MAX_OUTPUT  (4095U)
#define AFEC${INDEX}_CH6_MIN_OUTPUT  (0U)
<#elseif (AFEC_EMR_RES == "OSR4")>
#define AFEC${INDEX}_CH6_MAX_OUTPUT  (8191U)
#define AFEC${INDEX}_CH6_MIN_OUTPUT  (0U)
<#elseif (AFEC_EMR_RES == "OSR16")>
#define AFEC${INDEX}_CH6_MAX_OUTPUT  (16383U)
#define AFEC${INDEX}_CH6_MIN_OUTPUT  (0U)
<#elseif (AFEC_EMR_RES == "OSR64")>
#define AFEC${INDEX}_CH6_MAX_OUTPUT  (32767U)
#define AFEC${INDEX}_CH6_MIN_OUTPUT  (0U)
<#else>
#define AFEC${INDEX}_CH6_MAX_OUTPUT  (65535U)
#define AFEC${INDEX}_CH6_MIN_OUTPUT  (0U)
</#if>
</#if>
<#if ((AFEC_EMR_SIGNMODE == "ALL_SIGNED") || (AFEC_EMR_SIGNMODE == "SE_SIGN_DF_UNSG")) >
<#if (AFEC_EMR_RES == "NO_AVERAGE")>
#define AFEC${INDEX}_CH6_MAX_OUTPUT  (2047)
#define AFEC${INDEX}_CH6_MIN_OUTPUT  (-2048)
<#elseif (AFEC_EMR_RES == "OSR4")>
#define AFEC${INDEX}_CH6_MAX_OUTPUT  (4095)
#define AFEC${INDEX}_CH6_MIN_OUTPUT  (-4096)
<#elseif (AFEC_EMR_RES == "OSR16")>
#define AFEC${INDEX}_CH6_MAX_OUTPUT  (8191)
#define AFEC${INDEX}_CH6_MIN_OUTPUT  (-8192)
<#elseif (AFEC_EMR_RES == "OSR64")>
#define AFEC${INDEX}_CH6_MAX_OUTPUT  (16383)
#define AFEC${INDEX}_CH6_MIN_OUTPUT  (-16384)
<#else>
#define AFEC${INDEX}_CH6_MAX_OUTPUT  (32767)
#define AFEC${INDEX}_CH6_MIN_OUTPUT  (-32768)
</#if>
</#if>
</#if>
// *****************************************************************************
</#if>

<#if AFEC_CHER_CH7 == true>
<#if AFEC_CH6_NEG_INP == "GND">
<#if ((AFEC_EMR_SIGNMODE == "ALL_UNSIGNED") || (AFEC_EMR_SIGNMODE == "SE_UNSG_DF_SIGN")) >
<#if (AFEC_EMR_RES == "NO_AVERAGE")>
#define AFEC${INDEX}_CH7_MAX_OUTPUT  (4095U)
#define AFEC${INDEX}_CH7_MIN_OUTPUT  (0U)
<#elseif (AFEC_EMR_RES == "OSR4")>
#define AFEC${INDEX}_CH7_MAX_OUTPUT  (8191U)
#define AFEC${INDEX}_CH7_MIN_OUTPUT  (0U)
<#elseif (AFEC_EMR_RES == "OSR16")>
#define AFEC${INDEX}_CH7_MAX_OUTPUT  (16383U)
#define AFEC${INDEX}_CH7_MIN_OUTPUT  (0U)
<#elseif (AFEC_EMR_RES == "OSR64")>
#define AFEC${INDEX}_CH7_MAX_OUTPUT  (32767U)
#define AFEC${INDEX}_CH7_MIN_OUTPUT  (0U)
<#else>
#define AFEC${INDEX}_CH7_MAX_OUTPUT  (65535U)
#define AFEC${INDEX}_CH7_MIN_OUTPUT  (0U)
</#if>
</#if>
<#if ((AFEC_EMR_SIGNMODE == "ALL_SIGNED") || (AFEC_EMR_SIGNMODE == "SE_SIGN_DF_UNSG")) >
<#if (AFEC_EMR_RES == "NO_AVERAGE")>
#define AFEC${INDEX}_CH7_MAX_OUTPUT  (2047)
#define AFEC${INDEX}_CH7_MIN_OUTPUT  (-2048)
<#elseif (AFEC_EMR_RES == "OSR4")>
#define AFEC${INDEX}_CH7_MAX_OUTPUT  (4095)
#define AFEC${INDEX}_CH7_MIN_OUTPUT  (-4096)
<#elseif (AFEC_EMR_RES == "OSR16")>
#define AFEC${INDEX}_CH7_MAX_OUTPUT  (8191)
#define AFEC${INDEX}_CH7_MIN_OUTPUT  (-8192)
<#elseif (AFEC_EMR_RES == "OSR64")>
#define AFEC${INDEX}_CH7_MAX_OUTPUT  (16383)
#define AFEC${INDEX}_CH7_MIN_OUTPUT  (-16384)
<#else>
#define AFEC${INDEX}_CH7_MAX_OUTPUT  (32767)
#define AFEC${INDEX}_CH7_MIN_OUTPUT  (-32768)
</#if>
</#if>
</#if>
// *****************************************************************************
</#if>

<#if AFEC_CHER_CH8 == true>
<#if AFEC_CH8_NEG_INP != "GND">
<#if ((AFEC_EMR_SIGNMODE == "ALL_UNSIGNED") || (AFEC_EMR_SIGNMODE == "SE_SIGN_DF_UNSG")) >
<#if (AFEC_EMR_RES == "NO_AVERAGE")>
#define AFEC${INDEX}_CH8_MAX_OUTPUT  (4095U)
#define AFEC${INDEX}_CH8_MIN_OUTPUT  (0U)
<#elseif (AFEC_EMR_RES == "OSR4")>
#define AFEC${INDEX}_CH8_MAX_OUTPUT  (8191U)
#define AFEC${INDEX}_CH8_MIN_OUTPUT  (0U)
<#elseif (AFEC_EMR_RES == "OSR16")>
#define AFEC${INDEX}_CH8_MAX_OUTPUT  (16383U)
#define AFEC${INDEX}_CH8_MIN_OUTPUT  (0U)
<#elseif (AFEC_EMR_RES == "OSR64")>
#define AFEC${INDEX}_CH8_MAX_OUTPUT  (32767U)
#define AFEC${INDEX}_CH8_MIN_OUTPUT  (0U)
<#else>
#define AFEC${INDEX}_CH8_MAX_OUTPUT  (65535U)
#define AFEC${INDEX}_CH8_MIN_OUTPUT  (0U)
</#if>
</#if>
<#if ((AFEC_EMR_SIGNMODE == "ALL_SIGNED") || (AFEC_EMR_SIGNMODE == "SE_UNSG_DF_SIGN")) >
<#if (AFEC_EMR_RES == "NO_AVERAGE")>
#define AFEC${INDEX}_CH8_MAX_OUTPUT  (2047)
#define AFEC${INDEX}_CH8_MIN_OUTPUT  (-2048)
<#elseif (AFEC_EMR_RES == "OSR4")>
#define AFEC${INDEX}_CH8_MAX_OUTPUT  (4095)
#define AFEC${INDEX}_CH8_MIN_OUTPUT  (-4096)
<#elseif (AFEC_EMR_RES == "OSR16")>
#define AFEC${INDEX}_CH8_MAX_OUTPUT  (8191)
#define AFEC${INDEX}_CH8_MIN_OUTPUT  (-8192)
<#elseif (AFEC_EMR_RES == "OSR64")>
#define AFEC${INDEX}_CH8_MAX_OUTPUT  (16383)
#define AFEC${INDEX}_CH8_MIN_OUTPUT  (-16384)
<#else>
#define AFEC${INDEX}_CH8_MAX_OUTPUT  (32767)
#define AFEC${INDEX}_CH8_MIN_OUTPUT  (-32768)
</#if>
</#if>
<#else>
<#if ((AFEC_EMR_SIGNMODE == "ALL_UNSIGNED") || (AFEC_EMR_SIGNMODE == "SE_UNSG_DF_SIGN")) >
<#if (AFEC_EMR_RES == "NO_AVERAGE")>
#define AFEC${INDEX}_CH8_MAX_OUTPUT  (4095U)
#define AFEC${INDEX}_CH8_MIN_OUTPUT  (0U)
<#elseif (AFEC_EMR_RES == "OSR4")>
#define AFEC${INDEX}_CH8_MAX_OUTPUT  (8191U)
#define AFEC${INDEX}_CH8_MIN_OUTPUT  (0U)
<#elseif (AFEC_EMR_RES == "OSR16")>
#define AFEC${INDEX}_CH8_MAX_OUTPUT  (16383U)
#define AFEC${INDEX}_CH8_MIN_OUTPUT  (0U)
<#elseif (AFEC_EMR_RES == "OSR64")>
#define AFEC${INDEX}_CH8_MAX_OUTPUT  (32767U)
#define AFEC${INDEX}_CH8_MIN_OUTPUT  (0U)
<#else>
#define AFEC${INDEX}_CH8_MAX_OUTPUT  (65535U)
#define AFEC${INDEX}_CH8_MIN_OUTPUT  (0U)
</#if>
</#if>
<#if ((AFEC_EMR_SIGNMODE == "ALL_SIGNED") || (AFEC_EMR_SIGNMODE == "SE_SIGN_DF_UNSG")) >
<#if (AFEC_EMR_RES == "NO_AVERAGE")>
#define AFEC${INDEX}_CH8_MAX_OUTPUT  (2047)
#define AFEC${INDEX}_CH8_MIN_OUTPUT  (-2048)
<#elseif (AFEC_EMR_RES == "OSR4")>
#define AFEC${INDEX}_CH8_MAX_OUTPUT  (4095)
#define AFEC${INDEX}_CH8_MIN_OUTPUT  (-4096)
<#elseif (AFEC_EMR_RES == "OSR16")>
#define AFEC${INDEX}_CH8_MAX_OUTPUT  (8191)
#define AFEC${INDEX}_CH8_MIN_OUTPUT  (-8192)
<#elseif (AFEC_EMR_RES == "OSR64")>
#define AFEC${INDEX}_CH8_MAX_OUTPUT  (16383)
#define AFEC${INDEX}_CH8_MIN_OUTPUT  (-16384)
<#else>
#define AFEC${INDEX}_CH8_MAX_OUTPUT  (32767)
#define AFEC${INDEX}_CH8_MIN_OUTPUT  (-32768)
</#if>
</#if>
</#if>
// *****************************************************************************
</#if>

<#if AFEC_CHER_CH9 == true>
<#if AFEC_CH8_NEG_INP == "GND">
<#if ((AFEC_EMR_SIGNMODE == "ALL_UNSIGNED") || (AFEC_EMR_SIGNMODE == "SE_UNSG_DF_SIGN")) >
<#if (AFEC_EMR_RES == "NO_AVERAGE")>
#define AFEC${INDEX}_CH9_MAX_OUTPUT  (4095U)
#define AFEC${INDEX}_CH9_MIN_OUTPUT  (0U)
<#elseif (AFEC_EMR_RES == "OSR4")>
#define AFEC${INDEX}_CH9_MAX_OUTPUT  (8191U)
#define AFEC${INDEX}_CH9_MIN_OUTPUT  (0U)
<#elseif (AFEC_EMR_RES == "OSR16")>
#define AFEC${INDEX}_CH9_MAX_OUTPUT  (16383U)
#define AFEC${INDEX}_CH9_MIN_OUTPUT  (0U)
<#elseif (AFEC_EMR_RES == "OSR64")>
#define AFEC${INDEX}_CH9_MAX_OUTPUT  (32767U)
#define AFEC${INDEX}_CH9_MIN_OUTPUT  (0U)
<#else>
#define AFEC${INDEX}_CH9_MAX_OUTPUT  (65535U)
#define AFEC${INDEX}_CH9_MIN_OUTPUT  (0U)
</#if>
</#if>
<#if ((AFEC_EMR_SIGNMODE == "ALL_SIGNED") || (AFEC_EMR_SIGNMODE == "SE_SIGN_DF_UNSG")) >
<#if (AFEC_EMR_RES == "NO_AVERAGE")>
#define AFEC${INDEX}_CH9_MAX_OUTPUT  (2047)
#define AFEC${INDEX}_CH9_MIN_OUTPUT  (-2048)
<#elseif (AFEC_EMR_RES == "OSR4")>
#define AFEC${INDEX}_CH9_MAX_OUTPUT  (4095)
#define AFEC${INDEX}_CH9_MIN_OUTPUT  (-4096)
<#elseif (AFEC_EMR_RES == "OSR16")>
#define AFEC${INDEX}_CH9_MAX_OUTPUT  (8191)
#define AFEC${INDEX}_CH9_MIN_OUTPUT  (-8192)
<#elseif (AFEC_EMR_RES == "OSR64")>
#define AFEC${INDEX}_CH9_MAX_OUTPUT  (16383)
#define AFEC${INDEX}_CH9_MIN_OUTPUT  (-16384)
<#else>
#define AFEC${INDEX}_CH9_MAX_OUTPUT  (32767)
#define AFEC${INDEX}_CH9_MIN_OUTPUT  (-32768)
</#if>
</#if>
</#if>
// *****************************************************************************
</#if>

<#if AFEC_CHER_CH10 == true>
<#if AFEC_CH10_NEG_INP != "GND">
<#if ((AFEC_EMR_SIGNMODE == "ALL_UNSIGNED") || (AFEC_EMR_SIGNMODE == "SE_SIGN_DF_UNSG")) >
<#if (AFEC_EMR_RES == "NO_AVERAGE")>
#define AFEC${INDEX}_CH10_MAX_OUTPUT  (4095U)
#define AFEC${INDEX}_CH10_MIN_OUTPUT  (0U)
<#elseif (AFEC_EMR_RES == "OSR4")>
#define AFEC${INDEX}_CH10_MAX_OUTPUT  (8191U)
#define AFEC${INDEX}_CH10_MIN_OUTPUT  (0U)
<#elseif (AFEC_EMR_RES == "OSR16")>
#define AFEC${INDEX}_CH10_MAX_OUTPUT  (16383U)
#define AFEC${INDEX}_CH10_MIN_OUTPUT  (0U)
<#elseif (AFEC_EMR_RES == "OSR64")>
#define AFEC${INDEX}_CH10_MAX_OUTPUT  (32767U)
#define AFEC${INDEX}_CH10_MIN_OUTPUT  (0U)
<#else>
#define AFEC${INDEX}_CH10_MAX_OUTPUT  (65535U)
#define AFEC${INDEX}_CH10_MIN_OUTPUT  (0U)
</#if>
</#if>
<#if ((AFEC_EMR_SIGNMODE == "ALL_SIGNED") || (AFEC_EMR_SIGNMODE == "SE_UNSG_DF_SIGN")) >
<#if (AFEC_EMR_RES == "NO_AVERAGE")>
#define AFEC${INDEX}_CH10_MAX_OUTPUT  (2047)
#define AFEC${INDEX}_CH10_MIN_OUTPUT  (-2048)
<#elseif (AFEC_EMR_RES == "OSR4")>
#define AFEC${INDEX}_CH10_MAX_OUTPUT  (4095)
#define AFEC${INDEX}_CH10_MIN_OUTPUT  (-4096)
<#elseif (AFEC_EMR_RES == "OSR16")>
#define AFEC${INDEX}_CH10_MAX_OUTPUT  (8191)
#define AFEC${INDEX}_CH10_MIN_OUTPUT  (-8192)
<#elseif (AFEC_EMR_RES == "OSR64")>
#define AFEC${INDEX}_CH10_MAX_OUTPUT  (16383)
#define AFEC${INDEX}_CH10_MIN_OUTPUT  (-16384)
<#else>
#define AFEC${INDEX}_CH10_MAX_OUTPUT  (32767)
#define AFEC${INDEX}_CH10_MIN_OUTPUT  (-32768)
</#if>
</#if>
<#else>
<#if ((AFEC_EMR_SIGNMODE == "ALL_UNSIGNED") || (AFEC_EMR_SIGNMODE == "SE_UNSG_DF_SIGN")) >
<#if (AFEC_EMR_RES == "NO_AVERAGE")>
#define AFEC${INDEX}_CH10_MAX_OUTPUT  (4095U)
#define AFEC${INDEX}_CH10_MIN_OUTPUT  (0U)
<#elseif (AFEC_EMR_RES == "OSR4")>
#define AFEC${INDEX}_CH10_MAX_OUTPUT  (8191U)
#define AFEC${INDEX}_CH10_MIN_OUTPUT  (0U)
<#elseif (AFEC_EMR_RES == "OSR16")>
#define AFEC${INDEX}_CH10_MAX_OUTPUT  (16383U)
#define AFEC${INDEX}_CH10_MIN_OUTPUT  (0U)
<#elseif (AFEC_EMR_RES == "OSR64")>
#define AFEC${INDEX}_CH10_MAX_OUTPUT  (32767U)
#define AFEC${INDEX}_CH10_MIN_OUTPUT  (0U)
<#else>
#define AFEC${INDEX}_CH10_MAX_OUTPUT  (65535U)
#define AFEC${INDEX}_CH10_MIN_OUTPUT  (0U)
</#if>
</#if>
<#if ((AFEC_EMR_SIGNMODE == "ALL_SIGNED") || (AFEC_EMR_SIGNMODE == "SE_SIGN_DF_UNSG")) >
<#if (AFEC_EMR_RES == "NO_AVERAGE")>
#define AFEC${INDEX}_CH10_MAX_OUTPUT  (2047)
#define AFEC${INDEX}_CH10_MIN_OUTPUT  (-2048)
<#elseif (AFEC_EMR_RES == "OSR4")>
#define AFEC${INDEX}_CH10_MAX_OUTPUT  (4095)
#define AFEC${INDEX}_CH10_MIN_OUTPUT  (-4096)
<#elseif (AFEC_EMR_RES == "OSR16")>
#define AFEC${INDEX}_CH10_MAX_OUTPUT  (8191)
#define AFEC${INDEX}_CH10_MIN_OUTPUT  (-8192)
<#elseif (AFEC_EMR_RES == "OSR64")>
#define AFEC${INDEX}_CH10_MAX_OUTPUT  (16383)
#define AFEC${INDEX}_CH10_MIN_OUTPUT  (-16384)
<#else>
#define AFEC${INDEX}_CH10_MAX_OUTPUT  (32767)
#define AFEC${INDEX}_CH10_MIN_OUTPUT  (-32768)
</#if>
</#if>
</#if>
// *****************************************************************************
</#if>

<#if AFEC_CHER_CH11 == true>
<#if AFEC_CH10_NEG_INP == "GND">
<#if ((AFEC_EMR_SIGNMODE == "ALL_UNSIGNED") || (AFEC_EMR_SIGNMODE == "SE_UNSG_DF_SIGN")) >
<#if (AFEC_EMR_RES == "NO_AVERAGE")>
#define AFEC${INDEX}_CH11_MAX_OUTPUT  (4095U)
#define AFEC${INDEX}_CH11_MIN_OUTPUT  (0U)
<#elseif (AFEC_EMR_RES == "OSR4")>
#define AFEC${INDEX}_CH11_MAX_OUTPUT  (8191U)
#define AFEC${INDEX}_CH11_MIN_OUTPUT  (0U)
<#elseif (AFEC_EMR_RES == "OSR16")>
#define AFEC${INDEX}_CH11_MAX_OUTPUT  (16383U)
#define AFEC${INDEX}_CH11_MIN_OUTPUT  (0U)
<#elseif (AFEC_EMR_RES == "OSR64")>
#define AFEC${INDEX}_CH11_MAX_OUTPUT  (32767U)
#define AFEC${INDEX}_CH11_MIN_OUTPUT  (0U)
<#else>
#define AFEC${INDEX}_CH11_MAX_OUTPUT  (65535U)
#define AFEC${INDEX}_CH11_MIN_OUTPUT  (0U)
</#if>
</#if>
<#if ((AFEC_EMR_SIGNMODE == "ALL_SIGNED") || (AFEC_EMR_SIGNMODE == "SE_SIGN_DF_UNSG")) >
<#if (AFEC_EMR_RES == "NO_AVERAGE")>
#define AFEC${INDEX}_CH11_MAX_OUTPUT  (2047)
#define AFEC${INDEX}_CH11_MIN_OUTPUT  (-2048)
<#elseif (AFEC_EMR_RES == "OSR4")>
#define AFEC${INDEX}_CH11_MAX_OUTPUT  (4095)
#define AFEC${INDEX}_CH11_MIN_OUTPUT  (-4096)
<#elseif (AFEC_EMR_RES == "OSR16")>
#define AFEC${INDEX}_CH11_MAX_OUTPUT  (8191)
#define AFEC${INDEX}_CH11_MIN_OUTPUT  (-8192)
<#elseif (AFEC_EMR_RES == "OSR64")>
#define AFEC${INDEX}_CH11_MAX_OUTPUT  (16383)
#define AFEC${INDEX}_CH11_MIN_OUTPUT  (-16384)
<#else>
#define AFEC${INDEX}_CH11_MAX_OUTPUT  (32767)
#define AFEC${INDEX}_CH11_MIN_OUTPUT  (-32768)
</#if>
</#if>
</#if>
// *****************************************************************************
</#if>

/* Callback structure 

   Summary:
    Callback structure 

   Description:
    This stores the callback function pointer and context

   Remarks:
    None.
*/
typedef struct
{
    AFEC_CALLBACK callback_fn;
    uintptr_t context;
}AFEC${INDEX}_CALLBACK_PARAM;

AFEC${INDEX}_CALLBACK_PARAM AFEC${INDEX}_Callback_param;


// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************
/* The following functions make up the methods (set of possible operations) of 
   this interface.
*/

// ****************************************************************************
/* Function:
    void AFEC${INDEX}_Initialize (void);
    
  Summary:
    Initializes given instance of AFEC peripheral.
    
  Description:
    This function initializes given instance of AFEC peripheral of the device with the values
    configured in MCC GUI. Once the peripheral is initialized, peripheral can be used for conversion. 
  
  Precondition:
    MCC GUI should be configured with the right values.
  
  Parameters:
    None.
  
  Returns:
    None.
    
  Example:
    <code>
        AFEC${INDEX}_Initialize();
    </code>
    
  Remarks:
    This function must be called before any other AFEC function is
    called.
    
    This function should only be called once during system
    initialization.                                          
*/
void AFEC${INDEX}_Initialize (void);

// *****************************************************************************

/* Function:
    void AFEC${INDEX}_ChannelsEnable (AFEC_CHANNEL_MASK channelsMask);
    
  Summary:
    Enables the ADC channels
    
  Description:
    This function enables channels specified in channelsMask
  
  Precondition:
    AFEC${INDEX}_Initialize() function must have been called first for the associated instance.
  
  Parameters:
    channelsMask - set of channel numbers 
  
  Returns:
    None.
    
  Example:
    <code>
	    AFEC${INDEX}_Initialize();
        AFEC${INDEX}_ChannelsEnable(AFEC_CH0_MASK | AFEC_CH3_MASK);
    </code>
    
  Remarks:
    This function does not disable channels which are not included in the channel mask.                             
*/
void AFEC${INDEX}_ChannelsEnable (AFEC_CHANNEL_MASK channelsMask);

// *****************************************************************************

/* Function:
    void AFEC${INDEX}_ChannelsDisable (AFEC_CHANNEL_MASK channelsMask);
    
  Summary:
    Disables the ADC channels
    
  Description:
    This function disables channels specified in channelsMask
  
  Precondition:
    AFEC${INDEX}_Initialize() must have been called first for the associated instance.
  
  Parameters:
    channelsMask - set of channel numbers 
  
  Returns:
    None.
    
  Example:
    <code>
		AFEC${INDEX}_Initialize();
        AFEC${INDEX}_ChannelsDisable(AFEC_CH0_MASK | AFEC_CH3_MASK);
    </code>
    
  Remarks:
    This function does not enable channels which are not included in the channel mask.
*/
void AFEC${INDEX}_ChannelsDisable (AFEC_CHANNEL_MASK channelsMask);

// *****************************************************************************

/* Function:
    void AFEC${INDEX}_ChannelsInterruptEnable (AFEC_INTERRUPT_MASK channelsInterruptMask);
    
  Summary:
    Enables the ADC interrupt sources
    
  Description:
    This function enables interrupt sources specified in channelsInterruptMask. 
  
  Precondition:
    AFEC${INDEX}_Initialize() must have been called first for the associated instance.
  
  Parameters:
    channelsInterruptMask - interrupt sources
  
  Returns:
    None.
    
  Example:
    <code>
		AFEC${INDEX}_Initialize();
        AFEC${INDEX}_ChannelsInterruptEnable(AFEC_INTERRUPT_EOC_0_MASK);
    </code>
    
  Remarks:
    This function does not disable interrupts which are not included in the mask.
*/
void AFEC${INDEX}_ChannelsInterruptEnable (AFEC_INTERRUPT_MASK channelsInterruptMask);

// *****************************************************************************
/* Function:
    void AFEC${INDEX}_ChannelsInterruptDisable (AFEC_INTERRUPT_MASK channelsInterruptMask);
    
  Summary:
    Disables the ADC interrupt sources
    
  Description:
    This function disables interrupt sources specified in  channelsInterruptMask.
  
  Precondition:
	AFEC${INDEX}_Initialize() function must have been called first for the associated instance.
  
  Parameters:
    channelsInterruptMask - interrupt  sources
  
  Returns:
    None.
    
  Example:
    <code>
		AFEC${INDEX}_Initialize();
        AFEC${INDEX}_ChannelsInterruptDisable(AFEC_INTERRUPT_EOC_0_MASK);
    </code>
    
  Remarks:
    This function does not enable interrupts which are not included in the mask.
*/
void AFEC${INDEX}_ChannelsInterruptDisable (AFEC_INTERRUPT_MASK channelsInterruptMask);
// *****************************************************************************
/* Function:
    void AFEC${INDEX}_ConversionStart();
    
  Summary:
    Starts the ADC conversion of all the enabled channels with the software trigger
    
  Description:
    This function starts ADC conversion of all the enabled channels. Trigger is common for all the
	enabled channels. And channels are converted in sequential order or in user decided order based on
	configuration. 
  
  Precondition:
    AFEC${INDEX}_Initialize() function must have been called first for the associated instance and channels must have been enabled using
	AFEC${INDEX}_ChannelsEnable() function. 
  
  Parameters:
    None
  
  Returns:
    None.
    
  Example:
    <code>
		AFEC${INDEX}_Initialize();
		AFEC${INDEX}_ChannelsEnable(AFEC_CH0);
        AFEC${INDEX}_ConversionStart();
    </code>
    
  Remarks:
      This function should be called only when SW trigger for conversion is selected.         
*/
void AFEC${INDEX}_ConversionStart(void);
// *****************************************************************************

/* Function:
    bool AFEC${INDEX}_ChannelResultReady(AFEC_CHANNEL channel);
    
  Summary:
    Returns the status of the channel conversion
    
  Description:
    This function returns the status of the channel whether conversion is complete and result is
	available
	 
  Precondition:
    AFEC${INDEX}_Initialize() function must have been called first for the associated instance.
  
  Parameters:
    channel - channel number
  
  Returns:
    bool - status of the channel
	false: channel is disabled or conversion is not yet finished
	true: channel is enabled and result is available
    
  Example:
    <code>
        bool ch_status;
		AFEC${INDEX}_Initialize();
		AFEC${INDEX}_ChannelsEnable(AFEC_CH0);
		AFEC${INDEX}_ConversionStart();
		ch_status = AFEC${INDEX}_ChannelResultReady(AFEC_CH0);
    </code>
    
  Remarks:
    None
*/
bool AFEC${INDEX}_ChannelResultReady(AFEC_CHANNEL_NUM channel);
// *****************************************************************************

/* Function:
    uint16_t AFEC${INDEX}_ChannelResultGet (AFEC_CHANNEL channel);
    
  Summary:
    Reads the conversion result of the channel
    
  Description:
    This function reads the conversion result of the channel
  
  Precondition:
    AFEC${INDEX}_Initialize() must have been called first for the associated instance. And conversion must have been started. 
  
  Parameters:
    channel - channel number
  
  Returns:
    uint16_t - conversion result
    
  Example:
    <code>
		uint16_t result;
		bool status; 
		AFEC${INDEX}_Initialize();
		AFEC${INDEX}_ChannelsEnable(AFEC_CH0);
		AFEC${INDEX}_ConversionStart();
		status = AFEC${INDEX}_ChannelResultReady(AFEC_CH0);
		if (status)
		{
			result = AFEC${INDEX}_ChannelResultGet(AFEC_CH0);
		}
    </code>
    
  Remarks:
     This function can be called from interrupt or by polling the status when result is available.
	 User should decode the result based on sign mode (signed or unsigned result) and averaging 
	 (12, 13, 14, 15 or 16 bit result) configuration. 
*/
uint16_t AFEC${INDEX}_ChannelResultGet(AFEC_CHANNEL_NUM channel);

// *****************************************************************************

/* Function:
    void AFEC${INDEX}_ConversionSequenceSet (AFEC_CHANNEL *channelList, uint8_t numChannel);
    
  Summary:
    Sets the user sequence of the channel conversion 
    
  Description:
    This function sets the order in which channels are converted.
  
  Precondition:
    AFEC${INDEX}_Initialize() must have been called first for the associate instance. 
	Conversion should not be ongoing while changing the sequence. 
  
  Parameters:
    *channelList - pointer to the list of the channels which describes the order of conversion
	numChannel - Number of enabled channels in the list 
  
  Returns:
    None.
    
  Example:
    <code>
		AFEC_CHANNEL seq_order[4] = {AFEC_CH3, AFEC_CH5, AFEC_CH1, AFEC_CH2};
		AFEC${INDEX}_Initialize();
        AFEC${INDEX}_ConversionSequenceSet(seq_order, 0x4);
		AFEC${INDEX}_ChannelsEnable(AFEC_CH0_MASK | AFEC_CH1_MASK | AFEC_CH2_MASK | AFEC_CH3_MASK);
    </code>
    
  Remarks:
    Conversion order is set in this function and remains valid until user configures new conversion sequence order
	or reinitializes the peripheral. 
	Array pointed to by *channelList must be valid during the call to this function. This function copies
	the array data into AFEC HW registers. 
*/
void AFEC${INDEX}_ConversionSequenceSet(AFEC_CHANNEL_NUM *channelList, uint8_t numChannel);
// *****************************************************************************

/* Function:
    void AFEC${INDEX}_ChannelGainSet (AFEC_CHANNEL channel, AFEC_CHANNEL_GAIN gain);
    
  Summary:
    Writes the gain of the channel
    
  Description:
    This function writes the gain of the channel
  
  Precondition:
    AFEC${INDEX}_Initialize() must have been called first for the associated instance.
  
  Parameters:
    channel - channel number
	gain - channel gain of the amplifier
  
  Returns:
    None.
    
  Example:
    <code>
		AFEC${INDEX}_Initialize();
        AFEC${INDEX}_ChannelGainSet(AFEC_CH0, AFEC_CHANNEL_GAIN_2X);
    </code>
    
  Remarks:
    Input voltage range reduces as gain increases. 
	For gain = 1, range is (0) to (Vref)
	For gain = 2, range is (Vref/4) to (3 * Vref/4)
	For gain = 4, range is (3 * Vref/8) to (5 * Vref/8)
*/
void AFEC${INDEX}_ChannelGainSet(AFEC_CHANNEL_NUM channel, AFEC_CHANNEL_GAIN gain);
// *****************************************************************************

/* Function:
    void AFEC${INDEX}_ChannelOffsetSet (AFEC_CHANNEL channel, uint16_t offset);
    
  Summary:
    Writes the channel offset
    
  Description
    This function writes the offset value for the channel. This offset value is added to the
	value of sample to get the full range output (0 to Vref). Normally, this value should be set to Vref/2 in 10-bit format. 
  
  Precondition:
    AFEC${INDEX}_Initialize() must have been called first for the associated instance.
  
  Parameters:
    channel - channel number
	offset - 10-bit offset generated by internal DAC
  
  Returns:
    None.
    
  Example:
    <code>
		AFEC${INDEX}_Initialize();
        AFEC${INDEX}_ChannelOffsetSet(AFEC_CH0, 512);
    </code>
    
  Remarks:
     Offset should be set at the initialization. If this function is called when conversion is on-going, offset will be
	 applied from the next conversion.   
	Offset is added to the sample value and thus offset limits the input voltage range. 
	Offset less than Vref/2 will result in ADC saturation for input voltage greater than Vref/2. 
*/
void AFEC${INDEX}_ChannelOffsetSet(AFEC_CHANNEL_NUM channel, uint16_t offset);
// *****************************************************************************

/* Function:
    void AFEC${INDEX}_CallbackSet (AFEC${INDEX}_CALLBACK callback, uintptr_t context);
    
  Summary:
    Registers the function to be called from interrupt
    
  Description
    This function registers the callback function to be called from interrupt 
  
  Precondition:
    AFEC${INDEX}_Initialize() must have been called first for the associated instance.
  
  Parameters:
	callback - callback function pointer 
	context - Allows the caller to provide a context value (usually a pointer
	to the callers context for multi-instance clients).
  
  Returns:
    None.
    
  Example:
    <code>
		void AFEC${INDEX}_Callback_Fn(uintptr_t context, AFEC_INTERRUPT_MASK event_status);
		
		AFEC${INDEX}_Initialize();
        AFEC${INDEX}_CallbackSet(AFEC_Callback_Fn, NULL);
    </code>
    
  Remarks:
    Context value can be set to NULL if not required. 
	To disable callback function, pass NULL for the callback parameter. 
*/
void AFEC${INDEX}_CallbackSet(AFEC_CALLBACK callback, uintptr_t context);
// *****************************************************************************

<#if ((AFEC_CHER_CH0 == true && AFEC_IER_EOC0 == true) || (AFEC_CHER_CH1 == true && AFEC_IER_EOC1 == true) ||
(AFEC_CHER_CH2 == true && AFEC_IER_EOC2 == true) || (AFEC_CHER_CH3 == true && AFEC_IER_EOC3 == true) ||
(AFEC_CHER_CH4 == true && AFEC_IER_EOC4 == true) || (AFEC_CHER_CH5 == true && AFEC_IER_EOC5 == true) ||
(AFEC_CHER_CH6 == true && AFEC_IER_EOC6 == true) || (AFEC_CHER_CH7 == true && AFEC_IER_EOC7 == true) ||
(AFEC_CHER_CH8 == true && AFEC_IER_EOC8 == true) || (AFEC_CHER_CH9 == true && AFEC_IER_EOC9 == true) ||
(AFEC_CHER_CH10 == true && AFEC_IER_EOC10 == true) || (AFEC_CHER_CH11 == true && AFEC_IER_EOC11 == true)) >
/* Interrupt Handler */
void inline AFEC${INDEX}_EndOfConversionHandler(void)
{
    if (AFEC${INDEX}_Callback_param.callback_fn != NULL)
    {
        AFEC${INDEX}_Callback_param.callback_fn(AFEC${INDEX}_Callback_param.context, 
                                         _AFEC${INDEX}_REGS->AFEC_ISR.w);
    }
}
</#if>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

}

#endif
// DOM-IGNORE-END

#endif //PLIB_AFEC${INDEX}_H

/**
 End of File
*/

