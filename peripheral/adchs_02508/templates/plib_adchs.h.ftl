/*******************************************************************************
  ADCHS Peripheral Library Interface Header File

  Company
    Microchip Technology Inc.

  File Name
    plib_${ADCHS_INSTANCE_NAME?lower_case}.h

  Summary
    ${ADCHS_INSTANCE_NAME} peripheral library interface.

  Description
    This file defines the interface to the ADCHS peripheral library.  This
    library provides access to and control of the associated peripheral
    instance.

*******************************************************************************/

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

#ifndef PLIB_${ADCHS_INSTANCE_NAME}_H    // Guards against multiple inclusion
#define PLIB_${ADCHS_INSTANCE_NAME}_H


// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

/*  This section lists the other files that are included in this file.
*/

#include "plib_adchs_common.h"

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
<#compress>
<#list 0..(ADCHS_NUM_CHANNELS - 1) as i>
    <#assign ADCHS_CH_ENABLE = "ADCHS_"+i+"_ENABLE">
    <#assign ADCHS_CH_NAME = "ADCHS_"+i+"_NAME">
    <#assign CH_NUM = i>
    <#if .vars[ADCHS_CH_ENABLE] == true>

        #define ${.vars[ADCHS_CH_NAME]} (${CH_NUM}U)
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

void ${ADCHS_INSTANCE_NAME}_Initialize (void);

void ${ADCHS_INSTANCE_NAME}_ChannelsEnable (ADCHS_CHANNEL_MASK channelsMask);

void ${ADCHS_INSTANCE_NAME}_ChannelsDisable (ADCHS_CHANNEL_MASK channelsMask);

void ${ADCHS_INSTANCE_NAME}_ChannelsInterruptEnable (ADCHS_INTERRUPT_MASK channelsInterruptMask);

void ${ADCHS_INSTANCE_NAME}_ChannelsInterruptDisable (ADCHS_INTERRUPT_MASK channelsInterruptMask);

void ${ADCHS_INSTANCE_NAME}_ConversionStart(void);
void ${ADCHS_INSTANCE_NAME}_GlobalConversionStart(void);
void ${ADCHS_INSTANCE_NAME}_ChannelConversionStart(ADCHS_CHANNEL_NUM channel);

bool ${ADCHS_INSTANCE_NAME}_ChannelResultIsReady(ADCHS_CHANNEL_NUM channel);

uint16_t ${ADCHS_INSTANCE_NAME}_ChannelResultGet(ADCHS_CHANNEL_NUM channel);

<#-- void ${ADCHS_INSTANCE_NAME}_ConversionSequenceSet(ADCHS_CHANNEL_NUM *channelList, uint8_t numChannel);

void ${ADCHS_INSTANCE_NAME}_ChannelGainSet(ADCHS_CHANNEL_NUM channel, ADCHS_CHANNEL_GAIN gain);

void ${ADCHS_INSTANCE_NAME}_ChannelOffsetSet(ADCHS_CHANNEL_NUM channel, uint16_t offset);

<#if ADCHS_INTERRUPT == true>
    <#lt>void ${ADCHS_INSTANCE_NAME}_CallbackRegister(ADCHS_CALLBACK callback, uintptr_t context);
</#if>
 -->
// *****************************************************************************

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

}
#endif
// DOM-IGNORE-END

#endif //PLIB_${ADCHS_INSTANCE_NAME}_H

/**
 End of File
*/

