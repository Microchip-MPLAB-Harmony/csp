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

#include "plib_${DMA_INSTANCE_NAME?lower_case}.h"
<#if CoreSysIntFile == true>
#include "interrupts.h"
</#if>

<#assign DMA_INTERRUPT_ENABLED = false>
<#list 0..DMAC_HIGHEST_CHANNEL as i>
    <#assign CHANENABLE = "DMAC_ENABLE_CH_" + i>
    <#assign CHANINTENABLE = "DMAC_ENABLE_CH_" + i + "_INTERRUPT">
    <#if .vars[CHANENABLE] == true && .vars[CHANINTENABLE] == true>
        <#assign DMA_INTERRUPT_ENABLED = true>
    </#if>
</#list>

// *****************************************************************************
// *****************************************************************************
// Section: Global Data
// *****************************************************************************
// *****************************************************************************

#define DMAC_CHANNELS_NUMBER        (${DMAC_HIGHEST_CHANNEL+1}U)

#define DMAC_CRC_CHANNEL_OFFSET     (0x20U)

/* DMAC channels object configuration structure */
typedef struct
{
    bool                inUse;
<#if DMA_INTERRUPT_ENABLED == true>
    DMAC_CHANNEL_CALLBACK  callback;
    uintptr_t              context;
</#if>
    bool                isBusy;
} DMAC_CH_OBJECT ;

/* Initial write back memory section for DMAC */
static  dmac_descriptor_registers_t write_back_section[DMAC_CHANNELS_NUMBER]    __ALIGNED(8);

/* Descriptor section for DMAC */
static  dmac_descriptor_registers_t  descriptor_section[DMAC_CHANNELS_NUMBER]    __ALIGNED(8);

/* DMAC Channels object information structure */
static DMAC_CH_OBJECT dmacChannelObj[DMAC_CHANNELS_NUMBER];

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
    uint32_t channel = 0U;

    /* Initialize DMAC Channel objects */
    for(channel = 0U; channel < DMAC_CHANNELS_NUMBER; channel++)
    {
        dmacChObj->inUse = false;
<#if DMA_INTERRUPT_ENABLED == true>
        dmacChObj->callback = NULL;
        dmacChObj->context = 0U;
</#if>
        dmacChObj->isBusy = false;

        /* Point to next channel object */
        dmacChObj++;
    }

    /* Update the Base address and Write Back address register */
    ${DMA_INSTANCE_NAME}_REGS->DMAC_BASEADDR = (uint32_t) descriptor_section;
    ${DMA_INSTANCE_NAME}_REGS->DMAC_WRBADDR  = (uint32_t) write_back_section;

    /* Update the Priority Control register */
    <@compress single_line=true>${DMA_INSTANCE_NAME}_REGS->DMAC_PRICTRL0 = DMAC_PRICTRL0_LVLPRI0(${DMAC_LVLXPRIO_0}U) | <#if DMAC_LVLXPRIO_0 == "1">DMAC_PRICTRL0_RRLVLEN0_Msk |</#if>
                                                                           DMAC_PRICTRL0_LVLPRI1(${DMAC_LVLXPRIO_1}U) | <#if DMAC_LVLXPRIO_1 == "1">DMAC_PRICTRL0_RRLVLEN1_Msk |</#if>
                                                                           DMAC_PRICTRL0_LVLPRI2(${DMAC_LVLXPRIO_2}U) | <#if DMAC_LVLXPRIO_2 == "1">DMAC_PRICTRL0_RRLVLEN2_Msk |</#if>
                                                                           DMAC_PRICTRL0_LVLPRI3(${DMAC_LVLXPRIO_3}U)<#if DMAC_LVLXPRIO_3 == "1"> | DMAC_PRICTRL0_RRLVLEN3_Msk</#if>;</@compress>
    <#list 0..DMAC_HIGHEST_CHANNEL as i>
        <#assign DMAC_CHCTRLA_ENABLE    = "DMAC_ENABLE_CH_"           + i>
        <#assign DMAC_CHCTRLA_RUNSTDBY  = "DMAC_CHCTRLA_RUNSTDBY_CH_" + i>
        <#assign DMAC_CHCTRLA_TRIGACT   = "DMAC_CHCTRLA_TRIGACT_CH_"  + i>
        <#assign DMAC_CHCTRLA_LVL       = "DMAC_CHCTRLA_LVL_CH_"      + i>
        <#assign DMAC_BTCTRL_SRCINC     = "DMAC_BTCTRL_SRCINC_CH_"    + i>
        <#assign DMAC_BTCTRL_DSTINC     = "DMAC_BTCTRL_DSTINC_CH_"    + i>
        <#assign DMAC_BTCTRL_BEATSIZE   = "DMAC_BTCTRL_BEATSIZE_CH_"  + i>
        <#assign DMAC_TRIGSRC_PERID_VAL = "DMAC_CHCTRLA_TRIGSRC_CH_" + i + "_PERID_VAL">
        <#assign DMAC_BURSTLEN = "DMAC_CHCTRLA_BURSTLEN_CH_" + i>
        <#assign DMAC_THRESH = "DMAC_CHCTRLA_THRESH_CH_" + i>
        <#assign DMAC_INT_ENABLE = "DMAC_ENABLE_CH_" + i + "_INTERRUPT">
        <#if i < DMA_EVSYS_GENERATOR_COUNT>
            <#assign DMAC_EVSYS_OUT = "DMAC_ENABLE_EVSYS_OUT_" + i >
            <#assign DMAC_EVSYS_EVOSEL = "DMAC_BTCTRL_EVSYS_EVOSEL_" + i >
            <#assign DMAC_EVSYS_EVOMODE = "DMAC_BTCTRL_EVSYS_EVOMODE_" + i >
        </#if>
        <#if i < DMA_EVSYS_USER_COUNT>
            <#assign DMAC_EVSYS_IN = "DMAC_ENABLE_EVSYS_IN_" + i >
            <#assign DMAC_EVSYS_EVACT = "DMAC_CHEVCTRL_EVACT_" + i >
        </#if>

        <#if (.vars[DMAC_CHCTRLA_ENABLE] == true)>
        <#lt>   /***************** Configure DMA channel ${i} ********************/
        <#lt>   <@compress single_line=true>${DMA_INSTANCE_NAME}_REGS->CHANNEL[${i}].DMAC_CHCTRLA = DMAC_CHCTRLA_TRIGACT(${.vars[DMAC_CHCTRLA_TRIGACT]}U)
        <#lt>                                                       | DMAC_CHCTRLA_TRIGSRC(${.vars[DMAC_TRIGSRC_PERID_VAL]}U)
        <#lt>                                                       | DMAC_CHCTRLA_THRESHOLD(${.vars[DMAC_THRESH]}U)
        <#lt>                                                       | DMAC_CHCTRLA_BURSTLEN(${.vars[DMAC_BURSTLEN]}U)
        <#lt>                                                       ${(.vars[DMAC_CHCTRLA_RUNSTDBY])?then('| DMAC_CHCTRLA_RUNSTDBY_Msk','')}
        <#lt>                                                       ;
        <#lt>   </@compress>
        <#lt>

        <#lt>   <@compress single_line=true>descriptor_section[${i}].DMAC_BTCTRL = DMAC_BTCTRL_BLOCKACT_INT
        <#lt>                                                                       | DMAC_BTCTRL_BEATSIZE_${.vars[DMAC_BTCTRL_BEATSIZE]}
        <#lt>                                                                       | DMAC_BTCTRL_VALID_Msk
        <#lt>                                                                       ${(.vars[DMAC_BTCTRL_SRCINC] == "INCREMENTED_AM")?then('| DMAC_BTCTRL_SRCINC_Msk','')}
        <#lt>                                                                       ${(.vars[DMAC_BTCTRL_DSTINC] == "INCREMENTED_AM")?then('| DMAC_BTCTRL_DSTINC_Msk','')}
        <#lt>                                                                       <#if i < DMA_EVSYS_GENERATOR_COUNT>
        <#lt>                                                                       ${(.vars[DMAC_EVSYS_OUT])?then('| DMAC_BTCTRL_EVOSEL(${.vars[DMAC_EVSYS_EVOSEL]}U)','')}
        <#lt>                                                                       </#if>
        <#lt>                                                                       ;
        <#lt>   </@compress>

        <#lt>   ${DMA_INSTANCE_NAME}_REGS->CHANNEL[${i}].DMAC_CHPRILVL = DMAC_CHPRILVL_PRILVL(${.vars[DMAC_CHCTRLA_LVL]}U);

        <#lt>   dmacChannelObj[${i}].inUse = true;

        <#if (.vars[DMAC_INT_ENABLE] == true)>
        <#lt>   ${DMA_INSTANCE_NAME}_REGS->CHANNEL[${i}].DMAC_CHINTENSET = (DMAC_CHINTENSET_TERR_Msk | DMAC_CHINTENSET_TCMPL_Msk);
        </#if>

        <#if i < DMA_EVSYS_USER_COUNT>
        <#if (.vars[DMAC_EVSYS_OUT] == true) || (.vars[DMAC_EVSYS_IN] == true)>
        <#lt>   <@compress single_line=true>${DMA_INSTANCE_NAME}_REGS->CHANNEL[${i}].DMAC_CHEVCTRL = DMAC_CHEVCTRL_EVACT(${.vars[DMAC_EVSYS_EVACT]}U)
                                                                                            <#if i < DMA_EVSYS_GENERATOR_COUNT>
        <#lt>                                                                                ${(.vars[DMAC_EVSYS_OUT])?then('| DMAC_CHEVCTRL_EVOE_Msk | DMAC_CHEVCTRL_EVOMODE(${.vars[DMAC_EVSYS_EVOMODE]}U)','')}
                                                                                            </#if>
        <#lt>                                                                                ${(.vars[DMAC_EVSYS_IN])?then('| DMAC_CHEVCTRL_EVIE_Msk','')}
        <#lt>
        <#lt>;</@compress>
        </#if>
        </#if>
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
    uint8_t beat_size = 0U;
    bool returnStatus = false;
    const uint32_t* pu32srcAddr = (const uint32_t*)srcAddr;
    const uint32_t* pu32dstAddr = (const uint32_t*)destAddr;

    if ((!dmacChannelObj[channel].isBusy) || ((${DMA_INSTANCE_NAME}_REGS->CHANNEL[channel].DMAC_CHINTFLAG & (DMAC_CHINTENCLR_TCMPL_Msk | DMAC_CHINTENCLR_TERR_Msk)) != 0U))
    {
        /* Clear the transfer complete flag */
        ${DMA_INSTANCE_NAME}_REGS->CHANNEL[channel].DMAC_CHINTFLAG = DMAC_CHINTENCLR_TCMPL_Msk | DMAC_CHINTENCLR_TERR_Msk;

        dmacChannelObj[channel].isBusy = true;

        /* Get a pointer to the module hardware instance */
        dmac_descriptor_registers_t *const dmacDescReg = &descriptor_section[channel];

       /*Set source address */
        if (( dmacDescReg->DMAC_BTCTRL & DMAC_BTCTRL_SRCINC_Msk) != 0U)
        {
            dmacDescReg->DMAC_SRCADDR = ((uintptr_t)pu32srcAddr + blockSize);
        }
        else
        {
            dmacDescReg->DMAC_SRCADDR = (uintptr_t)(pu32srcAddr);
        }

        /* Set destination address */
        if (( dmacDescReg->DMAC_BTCTRL & DMAC_BTCTRL_DSTINC_Msk) != 0U)
        {
            dmacDescReg->DMAC_DSTADDR = ((uintptr_t)pu32dstAddr + blockSize);
        }
        else
        {
            if ((${DMA_INSTANCE_NAME}_REGS->DMAC_CRCCTRL & DMAC_CRCCTRL_CRCMODE_Msk) == DMAC_CRCCTRL_CRCMODE_DEFAULT)
            {
                dmacDescReg->DMAC_DSTADDR = (uintptr_t)(pu32dstAddr);
            }
            else
            {
                /* Store the Value in the destination address as seed to the CRC engine in Memory modes */
                dmacDescReg->DMAC_DSTADDR = *(pu32dstAddr);
            }
        }

        /*Calculate the beat size and then set the BTCNT value */
        beat_size = (uint8_t)((dmacDescReg->DMAC_BTCTRL & DMAC_BTCTRL_BEATSIZE_Msk) >> DMAC_BTCTRL_BEATSIZE_Pos);

        /* Set Block Transfer Count */
        dmacDescReg->DMAC_BTCNT = ((uint16_t)blockSize / ((uint16_t)1U << beat_size));

        /* Enable the channel */
        ${DMA_INSTANCE_NAME}_REGS->CHANNEL[channel].DMAC_CHCTRLA |= DMAC_CHCTRLA_ENABLE_Msk;

        /* Verify if Trigger source is Software Trigger */
        if ((((${DMA_INSTANCE_NAME}_REGS->CHANNEL[channel].DMAC_CHCTRLA & DMAC_CHCTRLA_TRIGSRC_Msk) >> DMAC_CHCTRLA_TRIGSRC_Pos) == 0x00U)
                                                && (((${DMA_INSTANCE_NAME}_REGS->CHANNEL[channel].DMAC_CHEVCTRL & DMAC_CHEVCTRL_EVIE_Msk)) != DMAC_CHEVCTRL_EVIE_Msk))
        {
            /* Trigger the DMA transfer */
            ${DMA_INSTANCE_NAME}_REGS->DMAC_SWTRIGCTRL |= ((uint32_t)1U << channel);
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
    bool busy_check = false;
    if ((dmacChannelObj[channel].isBusy) && ((${DMA_INSTANCE_NAME}_REGS->CHANNEL[channel].DMAC_CHINTFLAG & (DMAC_CHINTENCLR_TCMPL_Msk | DMAC_CHINTENCLR_TERR_Msk)) == 0U))
    {
        busy_check = true;
    }
    return busy_check;
}

DMAC_TRANSFER_EVENT ${DMA_INSTANCE_NAME}_ChannelTransferStatusGet(DMAC_CHANNEL channel)
{
    uint32_t chanIntFlagStatus = 0U;
    DMAC_TRANSFER_EVENT event = DMAC_TRANSFER_EVENT_NONE;

    /* Get the DMAC channel interrupt status */
    chanIntFlagStatus = ${DMA_INSTANCE_NAME}_REGS->CHANNEL[channel].DMAC_CHINTFLAG;

    if ((chanIntFlagStatus & DMAC_CHINTENCLR_TCMPL_Msk) != 0U)
    {
        event = DMAC_TRANSFER_EVENT_COMPLETE;
    }

    /* Verify if DMAC Channel Error flag is set */
    if ((chanIntFlagStatus & DMAC_CHINTENCLR_TERR_Msk) != 0U)
    {
        event = DMAC_TRANSFER_EVENT_ERROR;
    }

    return event;
}

/*******************************************************************************
    This function disables the specified DMAC channel.
********************************************************************************/

void ${DMA_INSTANCE_NAME}_ChannelDisable ( DMAC_CHANNEL channel )
{
    /* Disable the DMA channel */
    ${DMA_INSTANCE_NAME}_REGS->CHANNEL[channel].DMAC_CHCTRLA &= (~DMAC_CHCTRLA_ENABLE_Msk);

    while((${DMA_INSTANCE_NAME}_REGS->CHANNEL[channel].DMAC_CHCTRLA & DMAC_CHCTRLA_ENABLE_Msk) != 0U)
    {
        /* Wait for channel to be disabled */
    }

    dmacChannelObj[channel].isBusy = false;
}

uint16_t ${DMA_INSTANCE_NAME}_ChannelGetTransferredCount( DMAC_CHANNEL channel )
{
    uint16_t transferredCount = descriptor_section[channel].DMAC_BTCNT;
    transferredCount -= write_back_section[channel].DMAC_BTCNT;
    return(transferredCount);
}

<#if DMAC_LL_ENABLE = true>
void ${DMA_INSTANCE_NAME}_LinkedListDescriptorSetup (dmac_descriptor_registers_t* currentDescriptor,
                                                    DMAC_CHANNEL_CONFIG setting,
                                                    const void *srcAddr,
                                                    const void *destAddr,
                                                    size_t blockSize,
                                                    dmac_descriptor_registers_t* nextDescriptor)
{
    uint8_t beat_size = 0U;
    currentDescriptor->DMAC_BTCTRL = (uint16_t)setting;
    const uint32_t* pu32srcAddrr = (const uint32_t*)srcAddr;
    const uint32_t* pu32dstAddrr = (const uint32_t*)destAddr;

    /*Set source address */
    if (( currentDescriptor->DMAC_BTCTRL & DMAC_BTCTRL_SRCINC_Msk) != 0U)
    {
        currentDescriptor->DMAC_SRCADDR = ((uintptr_t)pu32srcAddrr + blockSize);
    }
    else
    {
        currentDescriptor->DMAC_SRCADDR = (uintptr_t)(pu32srcAddrr);
    }

    /* Set destination address */
    if (( currentDescriptor->DMAC_BTCTRL & DMAC_BTCTRL_DSTINC_Msk) != 0U)
    {
        currentDescriptor->DMAC_DSTADDR = ((uintptr_t)pu32dstAddrr + blockSize);
    }
    else
    {
        if ((${DMA_INSTANCE_NAME}_REGS->DMAC_CRCCTRL & DMAC_CRCCTRL_CRCMODE_Msk) == DMAC_CRCCTRL_CRCMODE_DEFAULT)
        {
            currentDescriptor->DMAC_DSTADDR = (uintptr_t)(pu32dstAddrr);
        }
        else
        {
            /* Store the Value in the destination address as seed to the CRC engine in Memory modes */
            currentDescriptor->DMAC_DSTADDR = *(pu32dstAddrr);
        }
    }

    /*Calculate the beat size and then set the BTCNT value */
    beat_size = (uint8_t)((currentDescriptor->DMAC_BTCTRL & DMAC_BTCTRL_BEATSIZE_Msk) >> DMAC_BTCTRL_BEATSIZE_Pos);

    /* Set Block Transfer Count */
    currentDescriptor->DMAC_BTCNT = (uint16_t)(blockSize / ((uint32_t)1U << beat_size));

    currentDescriptor->DMAC_DESCADDR = (uint32_t) nextDescriptor;
}
/*******************************************************************************
    This function submit a list of DMA transfers.
********************************************************************************/
bool ${DMA_INSTANCE_NAME}_ChannelLinkedListTransfer (DMAC_CHANNEL channel, dmac_descriptor_registers_t* channelDesc)
{
    bool returnStatus = false;

    if ((!dmacChannelObj[channel].isBusy) || ((${DMA_INSTANCE_NAME}_REGS->CHANNEL[channel].DMAC_CHINTFLAG & (DMAC_CHINTENCLR_TCMPL_Msk | DMAC_CHINTENCLR_TERR_Msk)) != 0U))
    {
        /* Clear the transfer complete flag */
        ${DMA_INSTANCE_NAME}_REGS->CHANNEL[channel].DMAC_CHINTFLAG = DMAC_CHINTENCLR_TCMPL_Msk | DMAC_CHINTENCLR_TERR_Msk;

        dmacChannelObj[channel].isBusy = false;

        (void)memcpy(&descriptor_section[channel], channelDesc, sizeof(dmac_descriptor_registers_t));

        /* Enable the channel */
        ${DMA_INSTANCE_NAME}_REGS->CHANNEL[channel].DMAC_CHCTRLA |= DMAC_CHCTRLA_ENABLE_Msk;

        /* Verify if Trigger source is Software Trigger */
        if (((${DMA_INSTANCE_NAME}_REGS->CHANNEL[channel].DMAC_CHCTRLA & DMAC_CHCTRLA_TRIGSRC_Msk) >> DMAC_CHCTRLA_TRIGSRC_Pos) == 0x00U)
        {
            /* Trigger the DMA transfer */
            ${DMA_INSTANCE_NAME}_REGS->DMAC_SWTRIGCTRL |= ((uint32_t)1U << channel);
        }
        returnStatus = true;
    }

    return returnStatus;
}
</#if>

/*******************************************************************************
    This function function allows a DMAC PLIB client to set an event handler.
********************************************************************************/
<#if DMA_INTERRUPT_ENABLED == true>
void ${DMA_INSTANCE_NAME}_ChannelCallbackRegister( DMAC_CHANNEL channel, const DMAC_CHANNEL_CALLBACK callback, const uintptr_t context )
{
    dmacChannelObj[channel].callback = callback;
    dmacChannelObj[channel].context  = context;
}
</#if>

/*******************************************************************************
    This function returns the current channel settings for the specified DMAC Channel
********************************************************************************/

DMAC_CHANNEL_CONFIG ${DMA_INSTANCE_NAME}_ChannelSettingsGet (DMAC_CHANNEL channel)
{
    /* Get a pointer to the module hardware instance */
    dmac_descriptor_registers_t *const dmacDescReg = &descriptor_section[0];

    return (dmacDescReg[channel].DMAC_BTCTRL);
}

/*******************************************************************************
    This function changes the current settings of the specified DMAC channel.
********************************************************************************/

bool ${DMA_INSTANCE_NAME}_ChannelSettingsSet (DMAC_CHANNEL channel, DMAC_CHANNEL_CONFIG setting)
{
    /* Get a pointer to the module hardware instance */
    dmac_descriptor_registers_t *const dmacDescReg = &descriptor_section[0];

    /* Disable the DMA channel */
    ${DMA_INSTANCE_NAME}_REGS->CHANNEL[channel].DMAC_CHCTRLA &= (~DMAC_CHCTRLA_ENABLE_Msk);

    /* Wait for channel to be disabled */
    while((${DMA_INSTANCE_NAME}_REGS->CHANNEL[channel].DMAC_CHCTRLA & DMAC_CHCTRLA_ENABLE_Msk) != 0U)
    {

    }

    /* Set the new settings */
    dmacDescReg[channel].DMAC_BTCTRL = (uint16_t)setting;

    return true;
}

void ${DMA_INSTANCE_NAME}_ChannelSuspend ( DMAC_CHANNEL channel )
{
    ${DMA_INSTANCE_NAME}_REGS->CHANNEL[channel].DMAC_CHCTRLB = (${DMA_INSTANCE_NAME}_REGS->CHANNEL[channel].DMAC_CHCTRLB & (uint8_t)(~DMAC_CHCTRLB_CMD_Msk)) | DMAC_CHCTRLB_CMD_SUSPEND;
}

void ${DMA_INSTANCE_NAME}_ChannelResume ( DMAC_CHANNEL channel )
{
    ${DMA_INSTANCE_NAME}_REGS->CHANNEL[channel].DMAC_CHCTRLB = (${DMA_INSTANCE_NAME}_REGS->CHANNEL[channel].DMAC_CHCTRLB & (uint8_t)(~DMAC_CHCTRLB_CMD_Msk)) | DMAC_CHCTRLB_CMD_RESUME;
}

/*******************************************************************************
    This function Disables the CRC engine and clears the CRC Control register
********************************************************************************/
void ${DMA_INSTANCE_NAME}_CRCDisable( void )
{
    ${DMA_INSTANCE_NAME}_REGS->DMAC_CRCCTRL = DMAC_CRCCTRL_RESETVALUE;
}

/*******************************************************************************
    This function sets the CRC Engine to use DMAC channel for calculating CRC.

    This Function has to be called before submitting DMA transfer request for
    the channel to calculate CRC
********************************************************************************/

void ${DMA_INSTANCE_NAME}_ChannelCRCSetup(DMAC_CHANNEL channel, DMAC_CRC_SETUP CRCSetup)
{
    /* Disable CRC Engine and clear the CRC Control register before configuring */
    ${DMA_INSTANCE_NAME}_CRCDisable();

    /* Store Initial Seed value only in default mode */
    if (CRCSetup.crc_mode == DMAC_CRC_MODE_DEFAULT)
    {
        ${DMA_INSTANCE_NAME}_REGS->DMAC_CRCCHKSUM = CRCSetup.seed;
    }

    /* Setup the CRC engine to use DMA Channel.
     * CRC engine is enabled by writing the DMA channel to the DMAC_CRCCTRL_CRCSRC bits
     */
    ${DMA_INSTANCE_NAME}_REGS->DMAC_CRCCTRL = (DMAC_CRCCTRL_CRCPOLY((uint16_t)CRCSetup.polynomial_type) | DMAC_CRCCTRL_CRCMODE((uint16_t)CRCSetup.crc_mode) | DMAC_CRCCTRL_CRCSRC((DMAC_CRC_CHANNEL_OFFSET + (uint16_t)channel)));
}

/*******************************************************************************
    This function returns the Caclculated CRC Value.
********************************************************************************/

uint32_t ${DMA_INSTANCE_NAME}_CRCRead( void )
{
    return (${DMA_INSTANCE_NAME}_REGS->DMAC_CRCCHKSUM);
}

/*******************************************************************************
    This function sets the CRC Engine in IO mode to get the data using the CPU
    which will be written in CRCDATAIN register. It internally calculates the
    Beat Size to be used based on the buffer length.

    This function returns the final CRC value once the computation is done
********************************************************************************/
uint32_t ${DMA_INSTANCE_NAME}_CRCCalculate(void *buffer, uint32_t length, DMAC_CRC_SETUP CRCSetup)
{
    uint8_t beatSize    = (uint8_t)DMAC_CRC_BEAT_SIZE_BYTE;
    uint32_t counter    = 0U;
    uint8_t *buffer_8   = (uint8_t *)buffer;
    uint16_t *buffer_16 = (uint16_t *)buffer;
    uint32_t *buffer_32 = (uint32_t *)buffer;

    /* Calculate the beatsize to be used basd on buffer length */
    if ((length & 0x3U) == 0U)
    {
        beatSize = (uint8_t)DMAC_CRC_BEAT_SIZE_WORD;
        length = length >> 0x2U;
    }
    else if ((length & 0x1U) == 0U)
    {
        beatSize = (uint8_t)DMAC_CRC_BEAT_SIZE_HWORD;
        length = length >> 0x1U;
    }
    else
    {


         /* No action required */

    }

    /* Disable CRC Engine and clear the CRC Control register before configuring */
    ${DMA_INSTANCE_NAME}_CRCDisable();

    ${DMA_INSTANCE_NAME}_REGS->DMAC_CRCCHKSUM = CRCSetup.seed;

    /* Setup the CRC engine to use IO Mode.
     * CRC engine is enabled by writing the IO mode to the DMAC_CRCCTRL_CRCSRC bits
     */
    ${DMA_INSTANCE_NAME}_REGS->DMAC_CRCCTRL = (DMAC_CRCCTRL_CRCPOLY((uint16_t)CRCSetup.polynomial_type) | DMAC_CRCCTRL_CRCBEATSIZE(beatSize) | DMAC_CRCCTRL_CRCSRC_IO );

    /* Start the CRC calculation by writing the buffer into CRCDATAIN register based
     * on the beat size configured
     */
    for (counter = 0U; counter < length; counter++)
    {
        if (beatSize == DMAC_CRC_BEAT_SIZE_BYTE)
        {
            ${DMA_INSTANCE_NAME}_REGS->DMAC_CRCDATAIN = buffer_8[counter];
        }
        else if (beatSize == DMAC_CRC_BEAT_SIZE_HWORD)
        {
            ${DMA_INSTANCE_NAME}_REGS->DMAC_CRCDATAIN = buffer_16[counter];
        }
        else if (beatSize == DMAC_CRC_BEAT_SIZE_WORD)
        {
            ${DMA_INSTANCE_NAME}_REGS->DMAC_CRCDATAIN = buffer_32[counter];
        }
        else
        {
              /* No action required */
        }

        /* Wait until CRC Calculation is completed for the current data in CRCDATAIN */
        while ((${DMA_INSTANCE_NAME}_REGS->DMAC_CRCSTATUS & DMAC_CRCSTATUS_CRCBUSY_Msk) == 0U)
        {
            ;
        }

        /* Clear the busy bit */
        ${DMA_INSTANCE_NAME}_REGS->DMAC_CRCSTATUS = DMAC_CRCSTATUS_CRCBUSY_Msk;
    }

    /* Return the final CRC calculated for the entire buffer */
    return (${DMA_INSTANCE_NAME}_REGS->DMAC_CRCCHKSUM);
}

<#if DMA_INTERRUPT_ENABLED == true>
//*******************************************************************************
//    Functions to handle DMA interrupt events.
//*******************************************************************************
static void DMAC_channel_interruptHandler(uint8_t channel)
{
    DMAC_CH_OBJECT  *dmacChObj = NULL;
    volatile uint32_t chanIntFlagStatus = 0U;
    DMAC_TRANSFER_EVENT event   = DMAC_TRANSFER_EVENT_ERROR;

    dmacChObj = (DMAC_CH_OBJECT *)&dmacChannelObj[channel];

    /* Get the DMAC channel interrupt status */
    chanIntFlagStatus = ${DMA_INSTANCE_NAME}_REGS->CHANNEL[channel].DMAC_CHINTFLAG;

    /* Verify if DMAC Channel Transfer complete flag is set */
    if ((chanIntFlagStatus & DMAC_CHINTENCLR_TCMPL_Msk) != 0U)
    {
        /* Clear the transfer complete flag */
        ${DMA_INSTANCE_NAME}_REGS->CHANNEL[channel].DMAC_CHINTFLAG = DMAC_CHINTENCLR_TCMPL_Msk;

        event = (DMAC_TRANSFER_EVENT)DMAC_TRANSFER_EVENT_COMPLETE;
        dmacChObj->isBusy = false;
    }

    /* Verify if DMAC Channel Error flag is set */
    if ((chanIntFlagStatus & DMAC_CHINTENCLR_TERR_Msk) != 0U)
    {
        /* Clear transfer error flag */
        ${DMA_INSTANCE_NAME}_REGS->CHANNEL[channel].DMAC_CHINTFLAG = DMAC_CHINTENCLR_TERR_Msk;

        event = DMAC_TRANSFER_EVENT_ERROR;
        dmacChObj->isBusy = false;
    }

    /* Execute the callback function */
    if (dmacChObj->callback != NULL)
    {
        dmacChObj->callback (event, dmacChObj->context);
    }
}

<#list 0..DMA_INT_LINES-1 as x>
<#assign DMAC_INT_NAME  = "DMA_INT_NAME_"  + x>
<#assign res =.vars[DMAC_INT_NAME]?matches(r"(\d+)")>
<#assign res2 =.vars[DMAC_INT_NAME]?matches(r"(\d+)_(\d+)")>
<#if (res) && ((res?groups[1])?number <= DMAC_HIGHEST_CHANNEL)>
void ${DMA_INSTANCE_NAME}_${res?groups[1]}_InterruptHandler( void )
{
   DMAC_channel_interruptHandler(${res?groups[1]}U);
}

<#elseif (.vars[DMAC_INT_NAME] == "OTHER") &&  (4 <= DMAC_HIGHEST_CHANNEL) >
void ${DMA_INSTANCE_NAME}_${.vars[DMAC_INT_NAME]}_InterruptHandler( void )
{
    uint8_t channel = 0U;

    for(channel = 4U; channel <= ${DMAC_HIGHEST_CHANNEL}U; channel++)
    {
        if (((${DMA_INSTANCE_NAME}_REGS->DMAC_INTSTATUS >> channel) & 0x1U) != 0U)
        {
            DMAC_channel_interruptHandler(channel);
        }
    }
}

<#elseif (res2) && ((res2?groups[1])?number <= DMAC_HIGHEST_CHANNEL) >
void ${DMA_INSTANCE_NAME}_${.vars[DMAC_INT_NAME]}_InterruptHandler( void )
{
    uint8_t channel = 0U;

    for(channel = ${res2?groups[1]}U; channel <= ${res2?groups[2]}U; channel++)
    {
        if (((${DMA_INSTANCE_NAME}_REGS->DMAC_INTSTATUS >> channel) & 0x1U) != 0U)
        {
           DMAC_channel_interruptHandler(channel);
        }
    }
}
</#if>
</#list>
</#if>