/*******************************************************************************
  AFEC Peripheral Library Interface Header File

  Company
    Microchip Technology Inc.

  File Name
    plib_afec1.h

  Summary
    AFEC1 peripheral library interface.

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

#ifndef PLIB_AFEC1_H    // Guards against multiple inclusion
#define PLIB_AFEC1_H


// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

/*  This section lists the other files that are included in this file.
*/

#include "plib_afec_common.h"

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
#define AFEC1_CH0_MAX_OUTPUT (65535U)
#define AFEC1_CH0_MIN_OUTPUT (0U)
#define CHANNEL_0 (0U)
/***********************************************************************/
#define AFEC1_CH5_MAX_OUTPUT (65535U)
#define AFEC1_CH5_MIN_OUTPUT (0U)
#define CHANNEL_5 (5U)
/***********************************************************************/
#define AFEC1_CH6_MAX_OUTPUT (65535U)
#define AFEC1_CH6_MIN_OUTPUT (0U)
#define CHANNEL_6 (6U)
/***********************************************************************/

// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************
/* The following functions make up the methods (set of possible operations) of
   this interface.
*/

void AFEC1_Initialize (void);

void AFEC1_ChannelsEnable (AFEC_CHANNEL_MASK channelsMask);

void AFEC1_ChannelsDisable (AFEC_CHANNEL_MASK channelsMask);

void AFEC1_ChannelsInterruptEnable (AFEC_INTERRUPT_MASK channelsInterruptMask);

void AFEC1_ChannelsInterruptDisable (AFEC_INTERRUPT_MASK channelsInterruptMask);

void AFEC1_ConversionStart(void);

bool AFEC1_ChannelResultIsReady(AFEC_CHANNEL_NUM channel);

uint16_t AFEC1_ChannelResultGet(AFEC_CHANNEL_NUM channel);

void AFEC1_ConversionSequenceSet(AFEC_CHANNEL_NUM *channelList, uint8_t numChannel);

void AFEC1_ChannelGainSet(AFEC_CHANNEL_NUM channel, AFEC_CHANNEL_GAIN gain);

void AFEC1_ChannelOffsetSet(AFEC_CHANNEL_NUM channel, uint16_t offset);

// *****************************************************************************

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

}

#endif
// DOM-IGNORE-END

#endif //PLIB_AFEC1_H

/**
 End of File
*/

