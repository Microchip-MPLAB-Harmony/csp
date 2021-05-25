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

typedef uint32_t DMA_TRANSFER_EVENT;

/* Block was transferred successfully. */
#define DMA_TRANSFER_EVENT_BLOCK_TRANSFER_COMPLETE          0x01

/* Error while processing the request */
#define DMA_TRANSFER_EVENT_ERROR                            0x02

/* An start trigger event has been detected and the block transfer has started */
#define DMA_TRANSFER_EVENT_START_DETECTED                   0x04

/* An abort trigger event has been detected and the DMA transfer has been aborted */
#define DMA_TRANSFER_EVENT_TRANSFER_ABORTED                 0x08

/* A cell transfer has been completed (CSZ bytes has been transferred) */
#define DMA_TRANSFER_EVENT_CELL_TRANSFER_COMPLETE           0x10

/* A half block transfer has been completed */
#define DMA_TRANSFER_EVENT_HALF_BLOCK_TRANSFER_COMPLETE     0x20

/* A link list done event has been completed */
#define DMA_TRANSFER_EVENT_LINKED_LIST_TRANSFER_COMPLETE    0x40

typedef uint32_t DMA_INT;

#define DMA_INT_START_DETECTED								(DMA_CHINTF_SD_Msk)
#define DMA_INT_TRANSFER_ABORT								(DMA_CHINTF_TA_Msk)
#define DMA_INT_CELL_TRANSFER_COMPLETE						(DMA_CHINTF_CC_Msk)
#define DMA_INT_BLOCK_TRANSFER_COMPLETE						(DMA_CHINTF_BC_Msk)
#define DMA_INT_BLOCK_HALF_TRANSFER_COMPLETE				(DMA_CHINTF_BH_Msk)
#define DMA_INT_LINKED_LIST_DONE							(DMA_CHINTF_LL_Msk)
#define DMA_INT_WRITE_ERROR									(DMA_CHINTF_WRE_Msk)
#define DMA_INT_READ_ERROR									(DMA_CHINTF_RDE_Msk)

typedef enum
{
    /* Length of pattern match is 1 byte */
    DMA_PATTERN_MATCH_LEN_1BYTE,

    /* Length of pattern match is 2 bytes */
    DMA_PATTERN_MATCH_LEN_2BYTE,
}DMA_PATTERN_MATCH_LEN;

<#if DMA_LL_ENABLE == true>
#if !(defined(__ASSEMBLER__) || defined(__IAR_SYSTEMS_ASM__))

typedef union
{
    struct
    {
        uint32_t CTRLB      :1;
        uint32_t EVCTRL     :1;
        uint32_t SSA        :1;
        uint32_t DSA        :1;
        uint32_t SSTRD      :1;
        uint32_t DSTRD      :1;
        uint32_t XSIZ       :1;
        uint32_t PDAT       :1;
        uint32_t CTRLCRC    :1;
        uint32_t CTRLDAT    :1;
        uint32_t            :14;
        uint32_t ENABLE     :1;
        uint32_t LLEN       :1;
        uint32_t SWFRC      :1;
        uint32_t RUNSTDBY   :1;
        uint32_t            :4;
    };
    struct
    {
        uint32_t w          :32;
    };
} DMA_BDCFGbits_t;

typedef union
{
    struct
    {
        uint32_t WAS        :3;
        uint32_t            :1;
        uint32_t RAS        :3;
        uint32_t            :1;
        uint32_t PRI        :2;
        uint32_t            :3;
        uint32_t WBOEN      :1;
        uint32_t BYTORD     :2;
        uint32_t TRIG       :8;
        uint32_t PIGNEN     :1;
        uint32_t PATLEN     :1;
        uint32_t PATEN      :1;
        uint32_t            :2;
        uint32_t CASTEN     :1;
        uint32_t            :1;
        uint32_t CRCEN      :1;
    };
    struct
    {
        uint32_t w          :32;
    };
} DMA_BDCTRLBbits_t;

typedef union
{
    struct
    {
        uint16_t EVAUXACT   :2;
        uint16_t EVOMODE    :2;
        uint16_t            :1;
        uint16_t EVAUXIE    :1;
        uint16_t EVSTRIE    :1;
        uint16_t EVOE       :1;
        uint16_t            :8;
    };
    struct
    {
        uint16_t w          :16;
    };
} DMA_BDEVCTRLbits_t;

typedef union
{
    struct
    {
        uint16_t CRCMD      :3;
        uint16_t CRCAPP     :1;
        uint16_t            :1;
        uint16_t CRCXOR     :1;
        uint16_t CRCROUT    :1;
        uint16_t CRCRIN     :1;
        uint16_t            :8;
    };
    struct
    {
        uint16_t w          :16;
    };
} DMA_BDCTRLCRCbits_t;

typedef union
{
    struct
    {
        uint32_t CSZ        :10;
        uint32_t            :6;
        uint32_t BLKSZ      :16;
    };
    struct
    {
        uint32_t w          :32;
    };
} DMA_BDXSIZbits_t;

typedef union
{
    struct
    {
        uint32_t PDAT       :16;
        uint32_t            :8;
        uint32_t PIGN       :8;
    };
    struct
    {
        uint32_t w          :32;
    };
} DMA_BDPDATbits_t;

/** \brief DMA_DESCRIPTOR register API structure */
typedef struct
{  /* Direct Memory Access Controller */
    uint32_t                            DMA_BDNXT;
    DMA_BDCFGbits_t                     DMA_BDCFG;
    DMA_BDCTRLBbits_t                   DMA_BDCTRLB;
    DMA_BDEVCTRLbits_t                  DMA_BDEVCTRL;
    DMA_BDCTRLCRCbits_t                 DMA_BDCTRLCRC;
    uint32_t                            DMA_BDSSA;
    uint32_t                            DMA_BDDSA;
    uint16_t                            DMA_BDSSTRD;
    uint16_t                            DMA_BDDSTRD;
    DMA_BDXSIZbits_t                    DMA_BDXSIZ;
    DMA_BDPDATbits_t                    DMA_BDPDAT;
    uint32_t                            DMA_BDCRCDAT;
} DMA_DESCRIPTOR_REGS

#ifdef __GNUC__
  __attribute__ ((aligned (4)))
#endif
;
#endif
</#if>

typedef uint32_t DMA_CHANNEL_CONFIG;

typedef void (*DMA_CHANNEL_CALLBACK) (DMA_TRANSFER_EVENT event, uintptr_t contextHandle);

void ${DMA_INSTANCE_NAME}_Initialize( void );
bool ${DMA_INSTANCE_NAME}_ChannelTransfer( DMA_CHANNEL channel, const void *srcAddr, const void *destAddr, size_t blockSize );
<#if DMA_LL_ENABLE == true>
bool ${DMA_INSTANCE_NAME}_ChannelLinkedListTransfer (DMA_CHANNEL channel, DMA_DESCRIPTOR_REGS* channelDesc);
</#if>
void ${DMA_INSTANCE_NAME}_ChannelCallbackRegister( DMA_CHANNEL channel, const DMA_CHANNEL_CALLBACK callback, const uintptr_t context );
bool ${DMA_INSTANCE_NAME}_ChannelIsBusy ( DMA_CHANNEL channel );
void ${DMA_INSTANCE_NAME}_ChannelDisable ( DMA_CHANNEL channel );
void ${DMA_INSTANCE_NAME}_ChannelEnable ( DMA_CHANNEL channel );
uint32_t ${DMA_INSTANCE_NAME}_ChannelGetTransferredCount( DMA_CHANNEL channel );
void ${DMA_INSTANCE_NAME}_ChannelInterruptEnable ( DMA_CHANNEL channel, DMA_INT intSources );
void ${DMA_INSTANCE_NAME}_ChannelInterruptDisable ( DMA_CHANNEL channel, DMA_INT intSources );
DMA_INT ${DMA_INSTANCE_NAME}_ChannelInterruptFlagsGet ( DMA_CHANNEL channel );
void ${DMA_INSTANCE_NAME}_ChannelPatternMatchSetup ( DMA_CHANNEL channel, DMA_PATTERN_MATCH_LEN patternLen, uint16_t matchData );
void ${DMA_INSTANCE_NAME}_ChannelPatternMatchEnable ( DMA_CHANNEL channel );
void ${DMA_INSTANCE_NAME}_ChannelPatternMatchDisable ( DMA_CHANNEL channel );
void ${DMA_INSTANCE_NAME}_ChannelPatternIgnoreByteEnable ( DMA_CHANNEL channel );
void ${DMA_INSTANCE_NAME}_ChannelPatternIgnoreByteDisable ( DMA_CHANNEL channel );
void ${DMA_INSTANCE_NAME}_ChannelPatternIgnoreValue ( DMA_CHANNEL channel, uint8_t ignoreValue );
DMA_CHANNEL_CONFIG ${DMA_INSTANCE_NAME}_ChannelSettingsGet (DMA_CHANNEL channel);
bool ${DMA_INSTANCE_NAME}_ChannelSettingsSet (DMA_CHANNEL channel, DMA_CHANNEL_CONFIG setting);


// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END

#endif //PLIB_${DMA_INSTANCE_NAME}_H
