/*******************************************************************************
  DMAC Peripheral Library Interface Header File

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${DMA_INSTANCE_NAME?lower_case}.h

  Summary:
    DMAC peripheral library interface.

  Description:
    This file defines the interface to the DMAC peripheral library. This
    library provides access to and control of the DMAC controller.

  Remarks:
    None.

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

#ifndef PLIB_${DMA_INSTANCE_NAME}_H    // Guards against multiple inclusion
#define PLIB_${DMA_INSTANCE_NAME}_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

/*  This section lists the other files that are included in this file.
*/
#include <device.h>
#include <string.h>
#include <stdbool.h>

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

// *****************************************************************************

typedef enum
{
<#list 0..DMAC_HIGHEST_CHANNEL - 1 as i>
    <#assign DMAC_CHCTRLA_ENABLE    = "DMAC_ENABLE_CH_"  + i>
    <#if (.vars[DMAC_CHCTRLA_ENABLE] == true)>
    /* DMAC Channel ${i} */
    DMAC_CHANNEL_${i} = ${i},
    </#if>
</#list>
} DMAC_CHANNEL;

typedef enum
{
    /* Data was transferred successfully. */
    DMAC_TRANSFER_EVENT_COMPLETE,

    /* Error while processing the request */
    DMAC_TRANSFER_EVENT_ERROR

} DMAC_TRANSFER_EVENT;

typedef uint32_t DMAC_CHANNEL_CONFIG;

typedef void (*DMAC_CHANNEL_CALLBACK) (DMAC_TRANSFER_EVENT event, uintptr_t contextHandle);

void ${DMA_INSTANCE_NAME}_Initialize( void );
void ${DMA_INSTANCE_NAME}_ChannelCallbackRegister (DMAC_CHANNEL channel, const DMAC_CHANNEL_CALLBACK eventHandler, const uintptr_t contextHandle);
bool ${DMA_INSTANCE_NAME}_ChannelTransfer (DMAC_CHANNEL channel, const void *srcAddr, const void *destAddr, size_t blockSize);
bool ${DMA_INSTANCE_NAME}_ChannelIsBusy ( DMAC_CHANNEL channel );
void ${DMA_INSTANCE_NAME}_ChannelDisable ( DMAC_CHANNEL channel );
<#if DMAC_LL_ENABLE = true>
bool ${DMA_INSTANCE_NAME}_ChannelLinkedListTransfer ( DMAC_CHANNEL channel, dmac_descriptor_registers_t * channelDesc );
</#if>
DMAC_CHANNEL_CONFIG  ${DMA_INSTANCE_NAME}_ChannelSettingsGet ( DMAC_CHANNEL channel );
bool  ${DMA_INSTANCE_NAME}_ChannelSettingsSet ( DMAC_CHANNEL channel, DMAC_CHANNEL_CONFIG settings );

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END

#endif //PLIB_${DMA_INSTANCE_NAME}_H
