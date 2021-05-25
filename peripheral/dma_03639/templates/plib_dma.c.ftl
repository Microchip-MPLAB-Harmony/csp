/*******************************************************************************
  Direct Memory Access Controller (DMA) PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_${DMA_INSTANCE_NAME?lower_case}.c

  Summary
    Source for ${DMA_INSTANCE_NAME} peripheral library interface Implementation.

  Description
    This file defines the interface to the DMA peripheral library. This
    library provides access to and control of the DMA controller.

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

#include "plib_${DMA_INSTANCE_NAME?lower_case}.h"
<#if CoreSysIntFile == true>
#include "interrupts.h"
</#if>

// *****************************************************************************
// *****************************************************************************
// Section: Global Data
// *****************************************************************************
// *****************************************************************************

#define DMA_CHANNELS_NUMBER        ${DMA_HIGHEST_CHANNEL}

/* DMA channels object configuration structure */
typedef struct
{
    DMA_CHANNEL_CALLBACK  callback;
    uintptr_t              context;
    uint8_t                busyStatus;
} DMA_CH_OBJECT ;

/* DMA Channels object information structure */
static DMA_CH_OBJECT dmaChannelObj[DMA_CHANNELS_NUMBER];

// *****************************************************************************
// *****************************************************************************
// Section: DMA PLib Interface Implementations
// *****************************************************************************
// *****************************************************************************

/*******************************************************************************
This function initializes the DMA controller of the device.
********************************************************************************/

void ${DMA_INSTANCE_NAME}_Initialize( void )
{
    uint32_t channel = 0;

    /* Initialize DMA Channel objects */
    for(channel = 0; channel < DMA_CHANNELS_NUMBER; channel++)
    {
        dmaChannelObj[channel].callback = NULL;
        dmaChannelObj[channel].context = 0;
        dmaChannelObj[channel].busyStatus = false;
    }

    <#list 0..DMA_HIGHEST_CHANNEL - 1 as i>
        <#assign DMA_CHCTRLA_ENABLE    = "DMA_ENABLE_CH_"           + i>
        <#assign DMA_CHCTRLA_RUNSTDBY  = "DMA_CHCTRLA_RUNSTDBY_CH_" + i>
        <#assign DMA_CHCTRLB_TRIG      = "DMA_CHCTRLB_TRIG_CH_" + i>
        <#assign DMA_CHCTRLB_PRI       = "DMA_CHCTRLB_PRI_CH_" + i>
        <#assign DMA_CHCTRLB_RAS       = "DMA_CHCTRLB_RAS_CH_" + i>
        <#assign DMA_CHCTRLB_WAS       = "DMA_CHCTRLB_WAS_CH_" + i>
        <#assign DMA_CHCTRLB_PATEN     = "DMA_CHCTRLB_PATEN_CH_" + i>
        <#assign DMA_CHCTRLB_PATLEN    = "DMA_CHCTRLB_PATLEN_CH_" + i>
        <#assign DMA_CHCTRLB_PIGNEN    = "DMA_CHCTRLB_PIGNEN_CH_" + i>
        <#assign DMA_CHCTRLB_CASTEN    = "DMA_CHCTRLB_CASTEN_CH_" + i>
        <#assign DMA_CHXSIZ_CSZ        = "DMA_CHXSIZ_CSZ_CH_" + i>
        <#assign DMA_CHPDAT_PDAT       = "DMA_CHPDAT_PDAT_CH_" + i>
        <#assign DMA_CHPDAT_PIGN       = "DMA_CHPDAT_PIGN_CH_" + i>

        <#if i < DMA_EVSYS_GENERATOR_COUNT>
            <#assign DMA_EVSYS_OUT = "DMA_ENABLE_EVSYS_OUT_" + i >
            <#assign DMA_EVSYS_EVOMODE = "DMA_BTCTRL_EVSYS_EVOMODE_" + i >
        </#if>
        <#if i < DMA_EVSYS_USER_COUNT>
            <#assign DMA_EVSYS_IN = "DMA_ENABLE_EVSYS_IN_" + i >
            <#assign DMA_ENABLE_EVSYS_AUX_IN = "DMA_ENABLE_EVSYS_AUX_IN_" + i >
            <#assign DMA_CHEVCTRL_EVACT = "DMA_CHEVCTRL_EVACT_" + i >
        </#if>

        <#if (.vars[DMA_CHCTRLA_ENABLE] == true)>

        <#lt>   /***************** Configure DMA channel ${i} ********************/
        <#lt>   <@compress single_line=true>${DMA_INSTANCE_NAME}_REGS->CHANNEL[${i}].DMA_CHCTRLB = DMA_CHCTRLB_TRIG(${.vars[DMA_CHCTRLB_TRIG]})
        <#lt>                                                                                      | DMA_CHCTRLB_PRI(DMA_CHCTRLB_PRI_${.vars[DMA_CHCTRLB_PRI]}_Val)
        <#lt>                                                                                      | DMA_CHCTRLB_RAS(DMA_CHCTRLB_RAS_${.vars[DMA_CHCTRLB_RAS]}_Val)
        <#lt>                                                                                      | DMA_CHCTRLB_WAS(DMA_CHCTRLB_WAS_${.vars[DMA_CHCTRLB_WAS]}_Val)
        <#lt>                                                                                      | DMA_CHCTRLB_CASTEN(${.vars[DMA_CHCTRLB_CASTEN]})
        <#lt>                                                                                      <#if (.vars[DMA_CHCTRLB_PATEN] == true)>
        <#lt>                                                                                      | DMA_CHCTRLB_PATEN_Msk
        <#lt>                                                                                      | DMA_CHCTRLB_PATLEN(${.vars[DMA_CHCTRLB_PATLEN]})
        <#lt>                                                                                      ${(.vars[DMA_CHCTRLB_PIGNEN])?then('| DMA_CHCTRLB_PIGNEN_Msk', '')}
        <#lt>                                                                                      </#if>
        <#lt>                                                                                      ;
        <#lt>   </@compress>
        <#lt>   <#if (.vars[DMA_EVSYS_IN] == true) || (.vars[DMA_ENABLE_EVSYS_AUX_IN] == true) || (.vars[DMA_EVSYS_OUT] == true)>
        <#lt>   <@compress single_line=true>${DMA_INSTANCE_NAME}_REGS->CHANNEL[${i}].DMA_CHEVCTRL = ${(.vars[DMA_EVSYS_IN])?then('DMA_CHEVCTRL_EVSTRIE(1)', 'DMA_CHEVCTRL_EVSTRIE(0)')}
        <#lt>                                                                                       <#if (.vars[DMA_EVSYS_OUT] == true)>
        <#lt>                                                                                       | DMA_CHEVCTRL_EVOE_Msk
        <#lt>                                                                                       | DMA_CHEVCTRL_EVOMODE(DMA_CHEVCTRL_EVOMODE_${.vars[DMA_EVSYS_EVOMODE]}_Val)
        <#lt>                                                                                       </#if>
        <#lt>                                                                                       <#if (.vars[DMA_ENABLE_EVSYS_AUX_IN] == true)>
        <#lt>                                                                                       | DMA_CHEVCTRL_EVAUXIE_Msk
        <#lt>                                                                                       | DMA_CHEVCTRL_EVAUXACT(DMA_CHEVCTRL_EVAUXACT_${.vars[DMA_CHEVCTRL_EVACT]}_Val)
        <#lt>                                                                                       </#if>
        <#lt>                                                                                       ;
        <#lt>   </@compress>
        <#lt>   </#if>

        <#lt>   <@compress single_line=true>${DMA_INSTANCE_NAME}_REGS->CHANNEL[${i}].DMA_CHXSIZ = DMA_CHXSIZ_CSZ(${.vars[DMA_CHXSIZ_CSZ]}); </@compress>

        <#lt>   <#if (.vars[DMA_CHCTRLB_PATEN] == true) || (.vars[DMA_CHCTRLB_PIGNEN] == true)>
        <#lt>   <@compress single_line=true>${DMA_INSTANCE_NAME}_REGS->CHANNEL[${i}].DMA_CHPDAT =   <#if (.vars[DMA_CHCTRLB_PATEN] == true) && (.vars[DMA_CHCTRLB_PIGNEN] == true)>
        <#lt>                                                                                       DMA_CHPDAT_PDAT(0x${.vars[DMA_CHPDAT_PDAT]?upper_case}) |
        <#lt>                                                                                       DMA_CHPDAT_PIGN(0x${.vars[DMA_CHPDAT_PIGN]?upper_case})
        <#lt>                                                                                       <#elseif (.vars[DMA_CHCTRLB_PATEN] == true)>
        <#lt>                                                                                       DMA_CHPDAT_PDAT(0x${.vars[DMA_CHPDAT_PDAT]?upper_case})
        <#lt>                                                                                       <#else>
        <#lt>                                                                                       DMA_CHPDAT_PIGN(0x${.vars[DMA_CHPDAT_PIGN]?upper_case})
        <#lt>                                                                                       </#if>
        <#lt>                                                                                       ;
        <#lt>   </@compress>
        <#lt>   </#if>

        <#lt>   <@compress single_line=true>${DMA_INSTANCE_NAME}_REGS->CHANNEL[${i}].DMA_CHINTENSET = DMA_CHINTENSET_BC_Msk; </@compress>

        <#lt>   <#if .vars[DMA_CHCTRLA_RUNSTDBY] == true >
        <#lt>   <@compress single_line=true>${DMA_INSTANCE_NAME}_REGS->CHANNEL[${i}].DMA_CHCTRLA = DMA_CHCTRLA_RUNSTDBY_Msk;
        <#lt>   </@compress>
        <#lt>   </#if>

        </#if>
    </#list>

    /* Global configuration */
    ${DMA_INSTANCE_NAME}_REGS->DMA_CTRLA = DMA_CTRLA_ENABLE_Msk;
}


/*******************************************************************************
    This function schedules a DMA transfer on the specified DMA channel.
********************************************************************************/

bool ${DMA_INSTANCE_NAME}_ChannelTransfer( DMA_CHANNEL channel, const void *srcAddr, const void *destAddr, size_t blockSize )
{
    bool returnStatus = false;

    if (dmaChannelObj[channel].busyStatus == false)
    {
        dmaChannelObj[channel].busyStatus = true;

        /*Set source address */
        ${DMA_INSTANCE_NAME}_REGS->CHANNEL[channel].DMA_CHSSA = (uint32_t) srcAddr;

        /*Set destination address */
        ${DMA_INSTANCE_NAME}_REGS->CHANNEL[channel].DMA_CHDSA = (uint32_t) destAddr;

        /* Set the block transfer size in bytes */
        ${DMA_INSTANCE_NAME}_REGS->CHANNEL[channel].DMA_CHXSIZ = (${DMA_INSTANCE_NAME}_REGS->CHANNEL[channel].DMA_CHXSIZ & ~DMA_CHXSIZ_BLKSZ_Msk) | (blockSize << DMA_CHXSIZ_BLKSZ_Pos);

        /* Enable the channel */
        ${DMA_INSTANCE_NAME}_REGS->CHANNEL[channel].DMA_CHCTRLA |= DMA_CHCTRLA_ENABLE_Msk;

        /* Verify if Trigger source is Software Trigger */
        if (((${DMA_INSTANCE_NAME}_REGS->CHANNEL[channel].DMA_CHCTRLB & DMA_CHCTRLB_TRIG_Msk) >> DMA_CHCTRLB_TRIG_Pos) == 0x00)
        {
            /* Trigger the DMA transfer */
            ${DMA_INSTANCE_NAME}_REGS->CHANNEL[channel].DMA_CHCTRLA |= DMA_CHCTRLA_SWFRC_Msk;
        }

        returnStatus = true;
    }

    return returnStatus;
}

<#if DMA_LL_ENABLE == true>
bool ${DMA_INSTANCE_NAME}_ChannelLinkedListTransfer (DMA_CHANNEL channel, DMA_DESCRIPTOR_REGS* channelDesc)
{
    bool returnStatus = false;

    if (dmaChannelObj[channel].busyStatus == false)
    {
        dmaChannelObj[channel].busyStatus = true;

        ${DMA_INSTANCE_NAME}_REGS->CHANNEL[channel].DMA_CHNXT = (uint32_t) channelDesc;

        /* Enable linked list completed interrupt */
        ${DMA_INSTANCE_NAME}_REGS->CHANNEL[channel].DMA_CHINTENSET = DMA_CHINTENSET_LL_Msk;

        /* Enable loading of linked list descriptor */
        ${DMA_INSTANCE_NAME}_REGS->CHANNEL[channel].DMA_CHCTRLA |= DMA_CHCTRLA_LLEN_Msk;

        returnStatus = true;
    }

    return returnStatus;
}
</#if>

/*******************************************************************************
    This function function allows a DMAC PLIB client to set an event handler.
********************************************************************************/

void ${DMA_INSTANCE_NAME}_ChannelCallbackRegister( DMA_CHANNEL channel, const DMA_CHANNEL_CALLBACK callback, const uintptr_t context )
{
    dmaChannelObj[channel].callback = callback;
    dmaChannelObj[channel].context  = context;
}

/*******************************************************************************
    This function returns the status of the channel.
********************************************************************************/

bool ${DMA_INSTANCE_NAME}_ChannelIsBusy ( DMA_CHANNEL channel )
{
    return (bool)dmaChannelObj[channel].busyStatus;
}

/*******************************************************************************
    This function disables the specified DMA channel.
********************************************************************************/
void ${DMA_INSTANCE_NAME}_ChannelEnable ( DMA_CHANNEL channel )
{
    /* Enable the DMA channel */
    ${DMA_INSTANCE_NAME}_REGS->CHANNEL[channel].DMA_CHCTRLA |= DMA_CHCTRLA_ENABLE_Msk;    

    dmaChannelObj[channel].busyStatus=true;

}

void ${DMA_INSTANCE_NAME}_ChannelDisable ( DMA_CHANNEL channel )
{
    /* Disable the DMA channel */
    ${DMA_INSTANCE_NAME}_REGS->CHANNEL[channel].DMA_CHCTRLA &= (~DMA_CHCTRLA_ENABLE_Msk);

    while((${DMA_INSTANCE_NAME}_REGS->CHANNEL[channel].DMA_CHCTRLA & DMA_CHCTRLA_ENABLE_Msk) != 0);

    dmaChannelObj[channel].busyStatus=false;

}

uint32_t ${DMA_INSTANCE_NAME}_ChannelGetTransferredCount( DMA_CHANNEL channel )
{
    return (${DMA_INSTANCE_NAME}_REGS->CHANNEL[channel].DMA_CHSTATBC & DMA_CHSTATBC_Msk);
}

void ${DMA_INSTANCE_NAME}_ChannelInterruptEnable ( DMA_CHANNEL channel, DMA_INT intSources )
{
    ${DMA_INSTANCE_NAME}_REGS->CHANNEL[channel].DMA_CHINTENSET = intSources;
}

void ${DMA_INSTANCE_NAME}_ChannelInterruptDisable ( DMA_CHANNEL channel, DMA_INT intSources )
{
    ${DMA_INSTANCE_NAME}_REGS->CHANNEL[channel].DMA_CHINTENCLR = intSources;
}

DMA_INT ${DMA_INSTANCE_NAME}_ChannelInterruptFlagsGet ( DMA_CHANNEL channel )
{
    return (uint8_t) (${DMA_INSTANCE_NAME}_REGS->CHANNEL[channel].DMA_CHINTF & DMA_CHINTF_Msk);
}

/*-----------------------DMA Pattern Match Related APIs-----------------------*/
void ${DMA_INSTANCE_NAME}_ChannelPatternMatchSetup ( DMA_CHANNEL channel, DMA_PATTERN_MATCH_LEN patternLen, uint16_t matchData )
{
    // CHCTRLBk is CHCTRLAk.ENABLE=1 write protected
    if (!(${DMA_INSTANCE_NAME}_REGS->CHANNEL[channel].DMA_CHCTRLA & DMA_CHCTRLA_ENABLE_Msk))
    {
		${DMA_INSTANCE_NAME}_REGS->CHANNEL[channel].DMA_CHPDAT = (${DMA_INSTANCE_NAME}_REGS->CHANNEL[channel].DMA_CHPDAT & ~DMA_CHPDAT_PDAT_Msk) | (matchData << DMA_CHPDAT_PDAT_Pos);
		
        if (patternLen == DMA_PATTERN_MATCH_LEN_1BYTE)
        {
            ${DMA_INSTANCE_NAME}_REGS->CHANNEL[channel].DMA_CHCTRLB &= ~DMA_CHCTRLB_PATLEN_Msk;
        }
        else
        {
            ${DMA_INSTANCE_NAME}_REGS->CHANNEL[channel].DMA_CHCTRLB |= DMA_CHCTRLB_PATLEN_Msk;
        }
						
		${DMA_INSTANCE_NAME}_REGS->CHANNEL[channel].DMA_CHCTRLB |= DMA_CHCTRLB_PATEN_Msk;
    }
}

void ${DMA_INSTANCE_NAME}_ChannelPatternMatchEnable ( DMA_CHANNEL channel )
{
    // CHCTRLBk is CHCTRLAk.ENABLE=1 write protected
    if (!(${DMA_INSTANCE_NAME}_REGS->CHANNEL[channel].DMA_CHCTRLA & DMA_CHCTRLA_ENABLE_Msk))
    {
        ${DMA_INSTANCE_NAME}_REGS->CHANNEL[channel].DMA_CHCTRLB |= DMA_CHCTRLB_PATEN_Msk;
    }
}

void ${DMA_INSTANCE_NAME}_ChannelPatternMatchDisable ( DMA_CHANNEL channel )
{
    // CHCTRLBk is CHCTRLAk.ENABLE=1 write protected
    if (!(${DMA_INSTANCE_NAME}_REGS->CHANNEL[channel].DMA_CHCTRLA & DMA_CHCTRLA_ENABLE_Msk))
    {
        ${DMA_INSTANCE_NAME}_REGS->CHANNEL[channel].DMA_CHCTRLB &= ~DMA_CHCTRLB_PATEN_Msk;
    }
}

void ${DMA_INSTANCE_NAME}_ChannelPatternIgnoreByteEnable ( DMA_CHANNEL channel )
{
    // CHCTRLBk is CHCTRLAk.ENABLE=1 write protected
    if (!(${DMA_INSTANCE_NAME}_REGS->CHANNEL[channel].DMA_CHCTRLA & DMA_CHCTRLA_ENABLE_Msk))
    {
        ${DMA_INSTANCE_NAME}_REGS->CHANNEL[channel].DMA_CHCTRLB |= DMA_CHCTRLB_PIGNEN_Msk;
    }
}

void ${DMA_INSTANCE_NAME}_ChannelPatternIgnoreByteDisable ( DMA_CHANNEL channel )
{
    // CHCTRLBk is CHCTRLAk.ENABLE=1 write protected
    if (!(${DMA_INSTANCE_NAME}_REGS->CHANNEL[channel].DMA_CHCTRLA & DMA_CHCTRLA_ENABLE_Msk))
    {
        ${DMA_INSTANCE_NAME}_REGS->CHANNEL[channel].DMA_CHCTRLB &= ~DMA_CHCTRLB_PIGNEN_Msk;
    }
}

void ${DMA_INSTANCE_NAME}_ChannelPatternIgnoreValue ( DMA_CHANNEL channel, uint8_t ignoreValue )
{
    // CHCTRLBk is CHCTRLAk.ENABLE=1 write protected
    if (!(${DMA_INSTANCE_NAME}_REGS->CHANNEL[channel].DMA_CHCTRLA & DMA_CHCTRLA_ENABLE_Msk))
    {
        ${DMA_INSTANCE_NAME}_REGS->CHANNEL[channel].DMA_CHPDAT = (${DMA_INSTANCE_NAME}_REGS->CHANNEL[channel].DMA_CHPDAT & ~DMA_CHPDAT_PIGN_Msk) | (ignoreValue << DMA_CHPDAT_PIGN_Pos);
    }
}

/*-----------------------------------------------------------------------------*/

/*******************************************************************************
    This function returns the current channel settings for the specified DMAC Channel
********************************************************************************/

DMA_CHANNEL_CONFIG ${DMA_INSTANCE_NAME}_ChannelSettingsGet (DMA_CHANNEL channel)
{
    return ${DMA_INSTANCE_NAME}_REGS->CHANNEL[channel].DMA_CHCTRLB;
}

/*******************************************************************************
    This function changes the current settings of the specified DMAC channel.
********************************************************************************/

bool ${DMA_INSTANCE_NAME}_ChannelSettingsSet (DMA_CHANNEL channel, DMA_CHANNEL_CONFIG setting)
{
    // CHCTRLBk is CHCTRLAk.ENABLE=1 write protected
    if (!(${DMA_INSTANCE_NAME}_REGS->CHANNEL[channel].DMA_CHCTRLA & DMA_CHCTRLA_ENABLE_Msk))
    {
        /* Set the new settings */
        ${DMA_INSTANCE_NAME}_REGS->CHANNEL[channel].DMA_CHCTRLB = setting;
        return true;
    }

    return false;
}

//*******************************************************************************
//    Functions to handle DMA interrupt events.
//*******************************************************************************
static void _DMA_interruptHandler(uint32_t channel)
{
    DMA_CH_OBJECT  *dmacChObj = NULL;
    volatile uint32_t chIntFlagStatus = 0;
    volatile uint32_t chIntFlagsEnabled = 0;

    DMA_TRANSFER_EVENT event = 0;

    dmacChObj = (DMA_CH_OBJECT *)&dmaChannelObj[channel];

    /* Get the DMA channel interrupt flag status */
    chIntFlagStatus = ${DMA_INSTANCE_NAME}_REGS->CHANNEL[channel].DMA_CHINTF;

    /* Update the event flag for the interrupts that have been enabled. Always update for Read and Write error interrupts */
    chIntFlagsEnabled = chIntFlagStatus & (${DMA_INSTANCE_NAME}_REGS->CHANNEL[channel].DMA_CHINTENSET | (DMA_CHINTF_WRE_Msk | DMA_CHINTF_RDE_Msk));

    /* An start trigger event has been detected and the block transfer has started */
    if (chIntFlagsEnabled & DMA_CHINTF_SD_Msk)
    {
        event |= DMA_TRANSFER_EVENT_START_DETECTED;
    }

    /* An abort trigger event has been detected and the DMA transfer has been aborted */
    if (chIntFlagsEnabled & DMA_CHINTF_TA_Msk)
    {
        event |= DMA_TRANSFER_EVENT_TRANSFER_ABORTED;
    }

    /* A cell transfer has been completed (CSZ bytes has been transferred) */
    if (chIntFlagsEnabled & DMA_CHINTF_CC_Msk)
    {
        event |= DMA_TRANSFER_EVENT_CELL_TRANSFER_COMPLETE;
    }

    /* A block transfer has been completed */
    if (chIntFlagsEnabled & DMA_CHINTF_BC_Msk)
    {
        event |= DMA_TRANSFER_EVENT_BLOCK_TRANSFER_COMPLETE;
    }

    /* A half block transfer has been completed */
    if (chIntFlagsEnabled & DMA_CHINTF_BH_Msk)
    {
        event |= DMA_TRANSFER_EVENT_HALF_BLOCK_TRANSFER_COMPLETE;
    }

    /* A link list done event has been completed */
    if (chIntFlagsEnabled & DMA_CHINTF_LL_Msk)
    {
        event |= DMA_TRANSFER_EVENT_LINKED_LIST_TRANSFER_COMPLETE;
    }
	
	/* A write error or read error event has been detected */
    if (chIntFlagsEnabled & (DMA_CHINTF_WRE_Msk | DMA_CHINTF_RDE_Msk))
    {
        event |= DMA_TRANSFER_EVENT_ERROR;
    }

    if (chIntFlagStatus & (DMA_CHINTF_WRE_Msk | DMA_CHINTF_RDE_Msk | DMA_CHINTF_LL_Msk | DMA_CHINTF_BC_Msk | DMA_CHINTF_TA_Msk))
    {
        dmacChObj->busyStatus = false;
    }

    /* Clear all the interrupt flags */
    ${DMA_INSTANCE_NAME}_REGS->CHANNEL[channel].DMA_CHINTF = chIntFlagStatus;

    /* Execute the callback function */
    if ((dmacChObj->callback != NULL) && (event != 0))
    {
        dmacChObj->callback (event, dmacChObj->context);
    }
}

<#list 1..DMA_NUM_INT_PRIO as i>
void DMA_PRI${i-1}_InterruptHandler( void )
{
    volatile uint32_t dmaIntPriority${i}Status = 0;
    uint32_t channel = 0;

    /* Get the DMA channel interrupt status */
    dmaIntPriority${i}Status = ${DMA_INSTANCE_NAME}_REGS->DMA_INTSTAT${i};

    for (channel = 0; channel < ${DMA_HIGHEST_CHANNEL}; channel++)
    {
        if (dmaIntPriority${i}Status & (1 << channel))
        {
            _DMA_interruptHandler(channel);
        }
    }
}
</#list>