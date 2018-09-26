/*******************************************************************************
  Direct Memory Access Controller (DMAC) PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_${DMA_INSTANCE_NAME?lower_case}.c

  Summary
    Source for ${DMA_INSTANCE_NAME} peripheral library interface Implementation.

  Description
    This file defines the interface to the DMAC peripheral library. This
    library provides access to and control of the DMAC controller.

  Remarks:
    None.

*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
Copyright (c) 2017 released Microchip Technology Inc. All rights reserved.
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

#include "plib_${DMA_INSTANCE_NAME?lower_case}.h"

// *****************************************************************************
// *****************************************************************************
// Section: Global Data
// *****************************************************************************
// *****************************************************************************

#define DMAC_CHANNELS_NUMBER        ${DMAC_HIGHEST_CHANNEL}

/* DMAC channels object configuration structure */
typedef struct
{
    uint8_t                inUse;
    DMAC_CHANNEL_CALLBACK  callback;
    uintptr_t              context;
    uint8_t                busyStatus;
} DMAC_CH_OBJECT ;

/* Initial write back memory section for DMAC */
static  dmacdescriptor_registers_t _write_back_section[DMAC_CHANNELS_NUMBER]    __attribute__((aligned(16)));

/* Descriptor section for DMAC */
static  dmacdescriptor_registers_t  descriptor_section[DMAC_CHANNELS_NUMBER]    __attribute__((aligned(16)));

/* DMAC Channels object information structure */
DMAC_CH_OBJECT dmacChannelObj[DMAC_CHANNELS_NUMBER];

// *****************************************************************************
// *****************************************************************************
// Section: DMAC PLib Interface Implementations
// *****************************************************************************
// *****************************************************************************

/*******************************************************************************
This function initializes the DMAC controller of the device.
********************************************************************************/

void ${DMA_INSTANCE_NAME}_Initialize( void )
{
    DMAC_CH_OBJECT *dmacChObj = (DMAC_CH_OBJECT *)&dmacChannelObj[0];
    DMAC_CHANNEL channel = 0;

    /* Initialize DMAC Channel objects */
    for(channel = 0; channel < DMAC_CHANNELS_NUMBER; channel++)
    {
        dmacChObj->inUse = 0;
        dmacChObj->callback = NULL;
        dmacChObj->context = 0;
        dmacChObj->busyStatus = false;

        /* Point to next channel object */
        dmacChObj += 1;
    }

    /* Update the Base address and Write Back address register */
    ${DMA_INSTANCE_NAME}_REGS->DMAC_BASEADDR = (uint32_t) descriptor_section;
    ${DMA_INSTANCE_NAME}_REGS->DMAC_WRBADDR  = (uint32_t)_write_back_section;

    /* Update the Priority Control register */
    ${DMA_INSTANCE_NAME}_REGS->DMAC_PRICTRL0 = DMAC_PRICTRL0_LVLPRI0(${DMAC_LVLXPRIO_0}) | DMAC_PRICTRL0_LVLPRI1(${DMAC_LVLXPRIO_1}) | DMAC_PRICTRL0_LVLPRI2(${DMAC_LVLXPRIO_2}) | DMAC_PRICTRL0_LVLPRI3(${DMAC_LVLXPRIO_3});
    <#list 0..DMAC_HIGHEST_CHANNEL - 1 as i>
        <#assign DMAC_CHCTRLA_ENABLE    = "DMAC_ENABLE_CH_"           + i>
        <#assign DMAC_CHCTRLA_RUNSTDBY  = "DMAC_CHCTRLA_RUNSTDBY_CH_" + i>
        <#assign DMAC_CHCTRLB_TRIGACT   = "DMAC_CHCTRLB_TRIGACT_CH_"  + i>
        <#assign DMAC_CHCTRLB_LVL       = "DMAC_CHCTRLB_LVL_CH_"      + i>
        <#assign DMAC_BTCTRL_SRCINC     = "DMAC_BTCTRL_SRCINC_CH_"    + i>
        <#assign DMAC_BTCTRL_DSTINC     = "DMAC_BTCTRL_DSTINC_CH_"    + i>
        <#assign DMAC_BTCTRL_BEATSIZE   = "DMAC_BTCTRL_BEATSIZE_CH_"  + i>
        <#assign DMAC_TRIGSRC_PERID_VAL = "DMAC_CHCTRLB_TRIGSRC_CH_" + i + "_PERID_VAL">

        <#if (.vars[DMAC_CHCTRLA_ENABLE] == true)>
        <#lt>   /***************** Configure DMA channel ${i} ********************/
        <#lt>   ${DMA_INSTANCE_NAME}_REGS->DMAC_CHID = ${i};
        <#lt>   <@compress single_line=true> <#if (.vars[DMAC_CHCTRLA_RUNSTDBY]) == true>
                <#lt>   ${DMA_INSTANCE_NAME}_REGS->DMAC_CHCTRLA |= DMAC_CHCTRLA_RUNSTDBY_Msk;
        <#lt>   </#if></@compress>
        <#lt>   <@compress single_line=true>${DMA_INSTANCE_NAME}_REGS->DMAC_CHCTRLB = DMAC_CHCTRLB_TRIGACT(${.vars[DMAC_CHCTRLB_TRIGACT]})
        <#lt>                                                       | DMAC_CHCTRLB_TRIGSRC(${.vars[DMAC_TRIGSRC_PERID_VAL]})
        <#lt>                                                       | DMAC_CHCTRLB_LVL(${.vars[DMAC_CHCTRLB_LVL]});
        <#lt>   </@compress>
        <#lt>   <@compress single_line=true>descriptor_section[${i}].BTCTRL = DMAC_DESCRIPTOR_BTCTRL_BLOCKACT_INT
        <#lt>                                                                       | DMAC_DESCRIPTOR_BTCTRL_BEATSIZE_${.vars[DMAC_BTCTRL_BEATSIZE]}
        <#lt>                                                                       | DMAC_DESCRIPTOR_BTCTRL_VALID_Msk
        <#lt>                                                                       ${(.vars[DMAC_BTCTRL_SRCINC] == "INCREMENTED_AM")?then('| DMAC_DESCRIPTOR_BTCTRL_SRCINC_Msk','')}
        <#lt>                                                                       ${(.vars[DMAC_BTCTRL_DSTINC] == "INCREMENTED_AM")?then('| DMAC_DESCRIPTOR_BTCTRL_DSTINC_Msk','')};
        <#lt>   </@compress>
        <#lt>   dmacChannelObj[${i}].inUse = 1;
        <#lt>   ${DMA_INSTANCE_NAME}_REGS->DMAC_CHINTENSET = (DMAC_CHINTENSET_TERR_Msk | DMAC_CHINTENSET_TCMPL_Msk);
        </#if>
    </#list>
    /* Enable the DMAC module & Priority Level x Enable */
    ${DMA_INSTANCE_NAME}_REGS->DMAC_CTRL = DMAC_CTRL_DMAENABLE_Msk | DMAC_CTRL_LVLEN0_Msk | DMAC_CTRL_LVLEN1_Msk | DMAC_CTRL_LVLEN2_Msk | DMAC_CTRL_LVLEN3_Msk;
}

/*******************************************************************************
    This function schedules a DMA transfer on the specified DMA channel.
********************************************************************************/

bool ${DMA_INSTANCE_NAME}_ChannelTransfer( DMAC_CHANNEL channel, const void *srcAddr, const void *destAddr, size_t blockSize )
{
    uint8_t beat_size = 0;
    bool returnStatus = false;

    if (dmacChannelObj[channel].busyStatus == false)
    {
        /* Get a pointer to the module hardware instance */
        dmacdescriptor_registers_t *const dmacDescReg = &descriptor_section[channel];

        dmacChannelObj[channel].busyStatus = true;

       /*Set source address */
        if ( dmacDescReg->BTCTRL & DMAC_DESCRIPTOR_BTCTRL_SRCINC_Msk)
        {
            dmacDescReg->SRCADDR = (uint32_t) (srcAddr + blockSize);
        }
        else
        {
            dmacDescReg->SRCADDR = (uint32_t) (srcAddr);
        }

        /* Set destination address */
        if ( dmacDescReg->BTCTRL & DMAC_DESCRIPTOR_BTCTRL_DSTINC_Msk)
        {
            dmacDescReg->DSTADDR = (uint32_t) (destAddr + blockSize);
        }
        else
        {
            dmacDescReg->DSTADDR = (uint32_t) (destAddr);
        }

        /*Calculate the beat size and then set the BTCNT value */
        beat_size = (dmacDescReg->BTCTRL & DMAC_DESCRIPTOR_BTCTRL_BEATSIZE_Msk) >> DMAC_DESCRIPTOR_BTCTRL_BEATSIZE_Pos;

        /* Set Block Transfer Count */
        dmacDescReg->BTCNT = blockSize / (1 << beat_size);

        /* Set the DMA channel */
        ${DMA_INSTANCE_NAME}_REGS->DMAC_CHID = channel;

        /* Enable the channel */
        ${DMA_INSTANCE_NAME}_REGS->DMAC_CHCTRLA |= DMAC_CHCTRLA_ENABLE_Msk;

        /* Verify if Trigger source is Software Trigger */
        if ( ((${DMA_INSTANCE_NAME}_REGS->DMAC_CHCTRLB & DMAC_CHCTRLB_TRIGSRC_Msk) >> DMAC_CHCTRLB_TRIGSRC_Pos) == 0x00)
        {
            /* Trigger the DMA transfer */
            ${DMA_INSTANCE_NAME}_REGS->DMAC_SWTRIGCTRL |= (1 << channel);
        }
        returnStatus = true;
    }

    return returnStatus;
}

/*******************************************************************************
    This function returns the status of the channel.
********************************************************************************/

bool ${DMA_INSTANCE_NAME}_ChannelIsBusy ( DMAC_CHANNEL channel )
{
    return (bool)dmacChannelObj[channel].busyStatus;
}

/*******************************************************************************
    This function disables the specified DMAC channel.
********************************************************************************/

void ${DMA_INSTANCE_NAME}_ChannelDisable ( DMAC_CHANNEL channel )
{
    /* Set the DMA Channel ID */
    ${DMA_INSTANCE_NAME}_REGS->DMAC_CHID = channel;

    /* Disable the DMA channel */
    ${DMA_INSTANCE_NAME}_REGS->DMAC_CHCTRLA &= (~DMAC_CHCTRLA_ENABLE_Pos);

    dmacChannelObj[channel].busyStatus=false;

}

<#if DMAC_LL_ENABLE = true>
/*******************************************************************************
    This function submit a list of DMA transfers.
********************************************************************************/

bool ${DMA_INSTANCE_NAME}_ChannelLinkedListTransfer (DMAC_CHANNEL channel, dmacdescriptor_registers_t* channelDesc)
{
    bool returnStatus = false;

    if (dmacChannelObj[channel].busyStatus == false)
    {
        /* Set the DMA channel */
        ${DMA_INSTANCE_NAME}_REGS->DMAC_CHID = channel;

        dmacChannelObj[channel].busyStatus = true;

        memcpy(&descriptor_section[channel], channelDesc, sizeof(dmacdescriptor_registers_t));

        /* Enable the channel */
        ${DMA_INSTANCE_NAME}_REGS->DMAC_CHCTRLA |= DMAC_CHCTRLA_ENABLE_Msk;

        /* Verify if Trigger source is Software Trigger */
        if (((${DMA_INSTANCE_NAME}_REGS->DMAC_CHCTRLB & DMAC_CHCTRLB_TRIGSRC_Msk) >> DMAC_CHCTRLB_TRIGSRC_Pos) == 0x00)
        {
            /* Trigger the DMA transfer */
            ${DMA_INSTANCE_NAME}_REGS->DMAC_SWTRIGCTRL |= (1 << channel);
        }
        returnStatus = true;
    }

    return returnStatus;
}
</#if>

/*******************************************************************************
    This function function allows a DMAC PLIB client to set an event handler.
********************************************************************************/

void ${DMA_INSTANCE_NAME}_ChannelCallbackRegister( DMAC_CHANNEL channel, const DMAC_CHANNEL_CALLBACK callback, const uintptr_t context )
{
    dmacChannelObj[channel].callback = callback;
    dmacChannelObj[channel].context  = context;
}

/*******************************************************************************
    This function returns the current channel settings for the specified DMAC Channel
********************************************************************************/

DMAC_CHANNEL_CONFIG ${DMA_INSTANCE_NAME}_ChannelSettingsGet (DMAC_CHANNEL channel)
{
    /* Get a pointer to the module hardware instance */
    dmacdescriptor_registers_t *const dmacDescReg = &descriptor_section[0];

    return (dmacDescReg[channel].BTCTRL);
}

/*******************************************************************************
    This function changes the current settings of the specified DMAC channel.
********************************************************************************/

bool ${DMA_INSTANCE_NAME}_ChannelSettingsSet (DMAC_CHANNEL channel, DMAC_CHANNEL_CONFIG setting)
{
    /* Get a pointer to the module hardware instance */
    dmacdescriptor_registers_t *const dmacDescReg = &descriptor_section[0];

    /* Disable the channel */
    /* Set the DMA Channel ID */
    ${DMA_INSTANCE_NAME}_REGS->DMAC_CHID = channel;

    /* Disable the DMA channel */
    ${DMA_INSTANCE_NAME}_REGS->DMAC_CHCTRLA &= (~DMAC_CHCTRLA_ENABLE_Pos);

    /* Set the new settings */
    dmacDescReg[channel].BTCTRL = setting;

    return true;
}

/*******************************************************************************
    This function handles the DMA interrupt events.
*/

void ${DMA_INSTANCE_NAME}_InterruptHandler( void )
{
    DMAC_CH_OBJECT  *dmacChObj = NULL;
    uint8_t channel = 0;
    volatile uint32_t chanIntFlagStatus = 0;
    DMAC_TRANSFER_EVENT event   = DMAC_TRANSFER_EVENT_ERROR;

    /* Get active channel number */
    channel =  ${DMA_INSTANCE_NAME}_REGS->DMAC_INTPEND & DMAC_INTPEND_ID_Msk;

	dmacChObj = (DMAC_CH_OBJECT *)&dmacChannelObj[channel]

    /* Update the DMAC channel ID */
    ${DMA_INSTANCE_NAME}_REGS->DMAC_CHID = DMAC_CHID_ID(channel);

    /* Get the DMAC channel interrupt status */
    chanIntFlagStatus = ${DMA_INSTANCE_NAME}_REGS->DMAC_CHINTFLAG;

    /* Verify if DMAC Channel Transfer complete flag is set */
    if (chanIntFlagStatus & DMAC_CHINTENCLR_TCMPL_Msk)
    {
        /* Clear the transfer complete flag */
        ${DMA_INSTANCE_NAME}_REGS->DMAC_CHINTFLAG = DMAC_CHINTENCLR_TCMPL_Msk;

        event = DMAC_TRANSFER_EVENT_COMPLETE;
        dmacChObj->busyStatus = false;
    }

    /* Verify if DMAC Channel Error flag is set */
    if (chanIntFlagStatus & DMAC_CHINTENCLR_TERR_Msk)
    {
        /* Clear transfer error flag */
        ${DMA_INSTANCE_NAME}_REGS->DMAC_CHINTFLAG = DMAC_CHINTENCLR_TERR_Msk;

        event = DMAC_TRANSFER_EVENT_ERROR;
        dmacChObj->busyStatus = false;
    }

    /* Execute the callback function */
    if (dmacChObj[channel].callback != NULL)
    {
        dmacChObj[channel].callback (event, dmacChObj[channel].context);
    }
}
