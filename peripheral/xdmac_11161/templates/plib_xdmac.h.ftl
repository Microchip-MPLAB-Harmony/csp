/*******************************************************************************
  XDMAC PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${DMA_INSTANCE_NAME?lower_case}.h

  Summary:
    XDMAC PLIB Header File

  Description:
    None

*******************************************************************************/

/*******************************************************************************
Copyright (c) 2017 released Microchip Technology Inc.  All rights reserved.

Microchip licenses to you the right to use, modify, copy and distribute
Software only when embedded on a Microchip microcontroller or digital signal
controller that is integrated into your product or third party product
(pursuant to the sublicense terms in the accompanying license agreement).

You should refer to the license agreement accompanying this Software for
additional information regarding your rights and obligations.

SOFTWARE AND DOCUMENTATION ARE PROVIDED AS IS  WITHOUT  WARRANTY  OF  ANY  KIND,
EITHER EXPRESS  OR  IMPLIED,  INCLUDING  WITHOUT  LIMITATION,  ANY  WARRANTY  OF
MERCHANTABILITY, TITLE, NON-INFRINGEMENT AND FITNESS FOR A  PARTICULAR  PURPOSE.
IN NO EVENT SHALL MICROCHIP OR  ITS  LICENSORS  BE  LIABLE  OR  OBLIGATED  UNDER
CONTRACT, NEGLIGENCE, STRICT LIABILITY, CONTRIBUTION,  BREACH  OF  WARRANTY,  OR
OTHER LEGAL  EQUITABLE  THEORY  ANY  DIRECT  OR  INDIRECT  DAMAGES  OR  EXPENSES
INCLUDING BUT NOT LIMITED TO ANY  INCIDENTAL,  SPECIAL,  INDIRECT,  PUNITIVE  OR
CONSEQUENTIAL DAMAGES, LOST  PROFITS  OR  LOST  DATA,  COST  OF  PROCUREMENT  OF
SUBSTITUTE  GOODS,  TECHNOLOGY,  SERVICES,  OR  ANY  CLAIMS  BY  THIRD   PARTIES
(INCLUDING BUT NOT LIMITED TO ANY DEFENSE  THEREOF),  OR  OTHER  SIMILAR  COSTS.
*******************************************************************************/

#ifndef PLIB_XDMAC_H
#define PLIB_XDMAC_H

#include <stddef.h>
#include <stdbool.h>
#include "plib_xdmac_common.h"

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    extern "C" {

#endif
// DOM-IGNORE-END

<#--Interface To Use-->
// *****************************************************************************
// *****************************************************************************
// Section: Interface
// *****************************************************************************
// *****************************************************************************

/****************************** XDMAC Data Types ******************************/
/* XDMAC Channels */
typedef enum {
    <#list 0..DMA_CHANNEL_COUNT as i>
    <#assign XDMAC_CH_ENABLE = "XDMAC_CH" + i + "_ENABLE">
        <#if .vars[XDMAC_CH_ENABLE]?has_content>
            <#if (.vars[XDMAC_CH_ENABLE] != false)>
    XDMAC_CHANNEL_${i},
            </#if>
        </#if>
    </#list>
} XDMAC_CHANNEL;


/****************************** XDMAC API *********************************/

void ${DMA_INSTANCE_NAME}_Initialize( void );

void ${DMA_INSTANCE_NAME}_ChannelCallbackRegister( XDMAC_CHANNEL channel, const XDMAC_CHANNEL_CALLBACK eventHandler, const uintptr_t contextHandle );

bool ${DMA_INSTANCE_NAME}_ChannelTransfer( XDMAC_CHANNEL channel, const void *srcAddr, const void *destAddr, size_t blockSize );
<#if XDMAC_LL_ENABLE == true>

bool ${DMA_INSTANCE_NAME}_ChannelLinkedListTransfer( XDMAC_CHANNEL channel, uint32_t firstDescriptorAddress, XDMAC_DESCRIPTOR_CONTROL* firstDescriptorControl );
</#if>

bool ${DMA_INSTANCE_NAME}_ChannelIsBusy (XDMAC_CHANNEL channel);

void ${DMA_INSTANCE_NAME}_ChannelDisable (XDMAC_CHANNEL channel);

XDMAC_CHANNEL_CONFIG ${DMA_INSTANCE_NAME}_ChannelSettingsGet (XDMAC_CHANNEL channel);

bool ${DMA_INSTANCE_NAME}_ChannelSettingsSet (XDMAC_CHANNEL channel, XDMAC_CHANNEL_CONFIG setting);

void ${DMA_INSTANCE_NAME}_ChannelBlockLengthSet (XDMAC_CHANNEL channel, uint16_t length);

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END
#endif // PLIB_XDMAC_H
