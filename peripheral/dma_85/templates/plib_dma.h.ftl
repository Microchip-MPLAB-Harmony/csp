/*******************************************************************************
  DMAC Peripheral Library Interface Header File

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${DMA_INSTANCE_NAME?lower_case}.h

  Summary:
    DMA peripheral library interface.

  Description:
    This file defines the interface to the DMAC peripheral library. This
    library provides access to and control of the DMAC controller.

  Remarks:
    None.

*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
* Copyright (C) 2021 Microchip Technology Inc. and its subsidiaries.
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
<#list 0..DMA_HIGHEST_CHANNEL-1 as i>
    <#assign DMA_CHCTRLA_ENABLE    = "DMA_ENABLE_CH_"  + i>
    <#if (.vars[DMA_CHCTRLA_ENABLE] == true)>
    /* DMA Channel ${i} */
    DMA_CHANNEL_${i} = ${i},
    </#if>
</#list>
} DMA_CHANNEL;

<#if DMA_LOW_LEVEL_API_ONLY == false>
typedef enum
{
    /* No event */
    DMA_TRANSFER_EVENT_NONE = 0,

    /* Data was transferred successfully. */
    DMA_TRANSFER_EVENT_COMPLETE = 1,

    /* Error while processing the request */
    DMA_TRANSFER_EVENT_ERROR = 2

} DMA_TRANSFER_EVENT;

typedef uint8_t DMA_INT;

#define DMA_INT_BUS_ERROR                                   (DMA_CHAN00_ISTS_BUS_ERR_Msk)
#define DMA_INT_HW_FLOW_CONTROL                             (DMA_CHAN00_ISTS_FLOW_CTRL_Msk)
#define DMA_INT_TRANSFER_DONE                               (DMA_CHAN00_ISTS_DONE_Msk)

typedef uint32_t DMA_CHANNEL_CONFIG;

typedef void (*DMA_CHANNEL_CALLBACK) (DMA_TRANSFER_EVENT event, uintptr_t contextHandle);
<#else>
#define BUSY_TIMEOUT_COUNTER    8000
</#if>

void ${DMA_INSTANCE_NAME}_Initialize( void );
<#if DMA_LOW_LEVEL_API_ONLY == false>
bool ${DMA_INSTANCE_NAME}_ChannelTransfer( DMA_CHANNEL channel, const void *srcAddr, const void *destAddr, size_t blockSize );
void ${DMA_INSTANCE_NAME}_ChannelCallbackRegister( DMA_CHANNEL channel, const DMA_CHANNEL_CALLBACK callback, const uintptr_t context );
bool ${DMA_INSTANCE_NAME}_ChannelIsBusy ( DMA_CHANNEL channel );
void ${DMA_INSTANCE_NAME}_ChannelDisable ( DMA_CHANNEL channel );
void ${DMA_INSTANCE_NAME}_ChannelEnable ( DMA_CHANNEL channel );
void ${DMA_INSTANCE_NAME}_ChannelTransferAbort ( DMA_CHANNEL channel );
uint32_t ${DMA_INSTANCE_NAME}_ChannelGetTransferredCount( DMA_CHANNEL channel );
void ${DMA_INSTANCE_NAME}_ChannelInterruptEnable ( DMA_CHANNEL channel, DMA_INT intSources );
void ${DMA_INSTANCE_NAME}_ChannelInterruptDisable ( DMA_CHANNEL channel, DMA_INT intSources );
DMA_INT ${DMA_INSTANCE_NAME}_ChannelInterruptFlagsGet ( DMA_CHANNEL channel );
DMA_CHANNEL_CONFIG ${DMA_INSTANCE_NAME}_ChannelSettingsGet (DMA_CHANNEL channel);
bool ${DMA_INSTANCE_NAME}_ChannelSettingsSet (DMA_CHANNEL channel, DMA_CHANNEL_CONFIG setting);
<#if DMA_CRC_ENABLE_CH_0 == true>
void ${DMA_INSTANCE_NAME}_CRCEnable( void );
void ${DMA_INSTANCE_NAME}_CRCDisable( void );
uint32_t ${DMA_INSTANCE_NAME}_CRCRead( void );
</#if>
<#if DMA_FILL_ENABLE_CH_1 == true>
void ${DMA_INSTANCE_NAME}_FillDataSet( uint32_t fillData );
</#if>

<#else>
void ${DMA_INSTANCE_NAME}_MemIncrCfg(DMA_CHANNEL channel, uint8_t mem_incr_sts);
void ${DMA_INSTANCE_NAME}_ChannelAbort(DMA_CHANNEL channel);
void ${DMA_INSTANCE_NAME}_Activate(uint8_t activate);
void ${DMA_INSTANCE_NAME}_SoftReset(void);
void ${DMA_INSTANCE_NAME}_Enable(void);
void ${DMA_INSTANCE_NAME}_Disable(void);
void ${DMA_INSTANCE_NAME}_ChannelActivate(DMA_CHANNEL channel);
void ${DMA_INSTANCE_NAME}_ChannelDeactivate(DMA_CHANNEL channel);
void ${DMA_INSTANCE_NAME}_Stop(DMA_CHANNEL channel);
void ${DMA_INSTANCE_NAME}_Start(DMA_CHANNEL channel);
uint8_t ${DMA_INSTANCE_NAME}_WaitTillFree(DMA_CHANNEL channel);
void ${DMA_INSTANCE_NAME}_SetupTx(DMA_CHANNEL channel, const uint8_t device, const uint32_t dataAHBAddress, uint32_t dma_buffer_tx, const uint8_t transfer_bytes_count);
void ${DMA_INSTANCE_NAME}_SetupRx(DMA_CHANNEL channel, const uint8_t device, const uint32_t dataAHBAddress, uint32_t dma_buffer_rx, const uint8_t transfer_bytes_count, const bool incrMemAddrFlag);
void ${DMA_INSTANCE_NAME}_SwitchTxToRx(DMA_CHANNEL channel, const uint8_t device, const uint32_t dataAHBAddress);
uint8_t ${DMA_INSTANCE_NAME}_GetDeviceId(const uint8_t device_name, const uint8_t device_instance);
void ${DMA_INSTANCE_NAME}_EnableInterrupt(DMA_CHANNEL channel);
void ${DMA_INSTANCE_NAME}_DisableInterrupt(DMA_CHANNEL channel);

</#if>


// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END

#endif //PLIB_${DMA_INSTANCE_NAME}_H
