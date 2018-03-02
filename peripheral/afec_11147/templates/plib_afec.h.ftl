/*******************************************************************************
  AFEC Peripheral Library Interface Header File

  Company
    Microchip Technology Inc.

  File Name
    plib_afec${INDEX}.h

  Summary
    AFEC${INDEX} peripheral library interface.

  Description
    This file defines the interface to the AFEC peripheral library.  This 
    library provides access to and control of the associated peripheral 
    instance.

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
<#assign AFEC_INTERRUPT = false>
<#compress>
<#list 0..11 as i>
	<#assign AFEC_CH_ENABLE = "AFEC_"+i+"_CHER">
	<#assign AFEC_CH_NEG_INP = "AFEC_"+i+"_NEG_INP">
	<#assign AFEC_CH_NAME = "AFEC_"+i+"_NAME">
<#if i % 2 !=0 >
	<#assign AFEC_CH_DIFF_PAIR = "AFEC_"+(i-1)+"_NEG_INP">
</#if>
	<#assign CH_NUM = i>
	<#assign AFEC_CH_IER_EOC = "AFEC_"+i+"_IER_EOC">
<#if (.vars[AFEC_CH_ENABLE] == true) && (.vars[AFEC_CH_IER_EOC] == true)>
	<#assign AFEC_INTERRUPT = true>
</#if>

<#-- Find the max and min digital value based on the result resolution and single-ended/differential ended mode -->
<#if .vars[AFEC_CH_ENABLE] == true>
	<#if (i % 2 != 0) && (.vars[AFEC_CH_DIFF_PAIR] != "GND")>
	<#else>

		<#if .vars[AFEC_CH_NEG_INP] != "GND">
			<#if ((AFEC_EMR_SIGNMODE_VALUE == "ALL_UNSIGNED") || (AFEC_EMR_SIGNMODE_VALUE == "SE_SIGN_DF_UNSG")) >
				<#if (AFEC_EMR_RES_VALUE == "NO_AVERAGE")>
					#define AFEC${INDEX}_CH${CH_NUM}_MAX_OUTPUT  (4095U)
					#define AFEC${INDEX}_CH${CH_NUM}_MIN_OUTPUT  (0U)
				<#elseif (AFEC_EMR_RES_VALUE == "OSR4")>
					#define AFEC${INDEX}_CH${CH_NUM}_MAX_OUTPUT  (8191U)
					#define AFEC${INDEX}_CH${CH_NUM}_MIN_OUTPUT  (0U)
				<#elseif (AFEC_EMR_RES_VALUE == "OSR16")>
					#define AFEC${INDEX}_CH${CH_NUM}_MAX_OUTPUT  (16383U)
					#define AFEC${INDEX}_CH${CH_NUM}_MIN_OUTPUT  (0U)
				<#elseif (AFEC_EMR_RES_VALUE == "OSR64")>
					#define AFEC${INDEX}_CH${CH_NUM}_MAX_OUTPUT  (32767U)
					#define AFEC${INDEX}_CH${CH_NUM}_MIN_OUTPUT  (0U)
				<#else>
					#define AFEC${INDEX}_CH${CH_NUM}_MAX_OUTPUT  (65535U)
					#define AFEC${INDEX}_CH${CH_NUM}_MIN_OUTPUT  (0U)
				</#if>
			</#if>
			<#if ((AFEC_EMR_SIGNMODE_VALUE == "ALL_SIGNED") || (AFEC_EMR_SIGNMODE_VALUE == "SE_UNSG_DF_SIGN")) >
				<#if (AFEC_EMR_RES_VALUE == "NO_AVERAGE")>
					#define AFEC${INDEX}_CH${CH_NUM}_MAX_OUTPUT  (2047)
					#define AFEC${INDEX}_CH${CH_NUM}_MIN_OUTPUT  (-2048)
				<#elseif (AFEC_EMR_RES_VALUE == "OSR4")>
					#define AFEC${INDEX}_CH${CH_NUM}_MAX_OUTPUT  (4095)
					#define AFEC${INDEX}_CH${CH_NUM}_MIN_OUTPUT  (-4096)
				<#elseif (AFEC_EMR_RES_VALUE == "OSR16")>
					#define AFEC${INDEX}_CH${CH_NUM}_MAX_OUTPUT  (8191)
					#define AFEC${INDEX}_CH${CH_NUM}_MIN_OUTPUT  (-8192)
				<#elseif (AFEC_EMR_RES_VALUE == "OSR64")>
					#define AFEC${INDEX}_CH${CH_NUM}_MAX_OUTPUT  (16383)
					#define AFEC${INDEX}_CH${CH_NUM}_MIN_OUTPUT  (-16384)
				<#else>
					#define AFEC${INDEX}_CH${CH_NUM}_MAX_OUTPUT  (32767)
					#define AFEC${INDEX}_CH${CH_NUM}_MIN_OUTPUT  (-32768)
				</#if>
			</#if>
		<#else>
			<#if ((AFEC_EMR_SIGNMODE_VALUE == "ALL_UNSIGNED") || (AFEC_EMR_SIGNMODE_VALUE == "SE_UNSG_DF_SIGN")) >
				<#if (AFEC_EMR_RES_VALUE == "NO_AVERAGE")>
					#define AFEC${INDEX}_CH${CH_NUM}_MAX_OUTPUT  (4095U)
					#define AFEC${INDEX}_CH${CH_NUM}_MIN_OUTPUT  (0U)
				<#elseif (AFEC_EMR_RES_VALUE == "OSR4")>
					#define AFEC${INDEX}_CH${CH_NUM}_MAX_OUTPUT  (8191U)
					#define AFEC${INDEX}_CH${CH_NUM}_MIN_OUTPUT  (0U)
				<#elseif (AFEC_EMR_RES_VALUE == "OSR16")>
					#define AFEC${INDEX}_CH${CH_NUM}_MAX_OUTPUT  (16383U)
					#define AFEC${INDEX}_CH${CH_NUM}_MIN_OUTPUT  (0U)
				<#elseif (AFEC_EMR_RES_VALUE == "OSR64")>
					#define AFEC${INDEX}_CH${CH_NUM}_MAX_OUTPUT  (32767U)
					#define AFEC${INDEX}_CH${CH_NUM}_MIN_OUTPUT  (0U)
				<#else>
					#define AFEC${INDEX}_CH${CH_NUM}_MAX_OUTPUT  (65535U)
					#define AFEC${INDEX}_CH${CH_NUM}_MIN_OUTPUT  (0U)
				</#if>
			</#if>
			<#if ((AFEC_EMR_SIGNMODE_VALUE == "ALL_SIGNED") || (AFEC_EMR_SIGNMODE_VALUE == "SE_SIGN_DF_UNSG")) >
				<#if (AFEC_EMR_RES_VALUE == "NO_AVERAGE")>
					#define AFEC${INDEX}_CH${CH_NUM}_MAX_OUTPUT  (2047)
					#define AFEC${INDEX}_CH${CH_NUM}_MIN_OUTPUT  (-2048)
				<#elseif (AFEC_EMR_RES_VALUE == "OSR4")>
					#define AFEC${INDEX}_CH${CH_NUM}_MAX_OUTPUT  (4095)
					#define AFEC${INDEX}_CH${CH_NUM}_MIN_OUTPUT  (-4096)
				<#elseif (AFEC_EMR_RES_VALUE == "OSR16")>
					#define AFEC${INDEX}_CH${CH_NUM}_MAX_OUTPUT  (8191)
					#define AFEC${INDEX}_CH${CH_NUM}_MIN_OUTPUT  (-8192)
				<#elseif (AFEC_EMR_RES_VALUE == "OSR64")>
					#define AFEC${INDEX}_CH${CH_NUM}_MAX_OUTPUT  (16383)
					#define AFEC${INDEX}_CH${CH_NUM}_MIN_OUTPUT  (-16384)
				<#else>
					#define AFEC${INDEX}_CH${CH_NUM}_MAX_OUTPUT  (32767)
					#define AFEC${INDEX}_CH${CH_NUM}_MIN_OUTPUT  (-32768)
				</#if>
			</#if>
		</#if>

#define ${.vars[AFEC_CH_NAME]} (${CH_NUM}U)
/***********************************************************************/
	</#if>
</#if> <#-- CH ENABLE -->
</#list>
</#compress>


// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************
/* The following functions make up the methods (set of possible operations) of 
   this interface.
*/

void AFEC${INDEX}_Initialize (void);

void AFEC${INDEX}_ChannelsEnable (AFEC_CHANNEL_MASK channelsMask);

void AFEC${INDEX}_ChannelsDisable (AFEC_CHANNEL_MASK channelsMask);

void AFEC${INDEX}_ChannelsInterruptEnable (AFEC_INTERRUPT_MASK channelsInterruptMask);

void AFEC${INDEX}_ChannelsInterruptDisable (AFEC_INTERRUPT_MASK channelsInterruptMask);

void AFEC${INDEX}_ConversionStart(void);

bool AFEC${INDEX}_ChannelResultReady(AFEC_CHANNEL_NUM channel);

uint16_t AFEC${INDEX}_ChannelResultGet(AFEC_CHANNEL_NUM channel);

void AFEC${INDEX}_ConversionSequenceSet(AFEC_CHANNEL_NUM *channelList, uint8_t numChannel);

void AFEC${INDEX}_ChannelGainSet(AFEC_CHANNEL_NUM channel, AFEC_CHANNEL_GAIN gain);

void AFEC${INDEX}_ChannelOffsetSet(AFEC_CHANNEL_NUM channel, uint16_t offset);

<#if AFEC_INTERRUPT == true>
	<#lt>void AFEC${INDEX}_CallbackSet(AFEC_CALLBACK callback, uintptr_t context);
</#if>
// *****************************************************************************

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

}

#endif
// DOM-IGNORE-END

#endif //PLIB_AFEC${INDEX}_H

/**
 End of File
*/

