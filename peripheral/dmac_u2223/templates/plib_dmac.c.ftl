/*******************************************************************************
  Direct Memory Access Controller (DMAC) PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_dmac${DMAC_INDEX}.c

  Summary
    Source for DMAC${DMAC_INDEX} peripheral library interface Implementation.

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

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
/* This section lists the other files that are included in this file.
*/

#include "plib_dmac${DMAC_INDEX}.h"

// *****************************************************************************
// *****************************************************************************
// Section: Global Data
// *****************************************************************************
// *****************************************************************************

/* DMAC Descriptor */
#define SECTION_DMAC_DESCRIPTOR

// *****************************************************************************
/* DMAC channel User configuration structure

  Summary:
    DMAC channel User configuration.

  Description:
    This Configuration structure for the user selection of the DMAC
    channel configuration.

  Remarks:
    None.
*/

typedef struct
{
    /* BT Control Register */
    uint16_t    dmacBTCTRLReg;

    /* DMAC Channel Trigger */
    uint8_t     dmacTrigSrc;

} DMAC_CONFIG_VAL;

// *****************************************************************************
/* DMAC channels object configuration structure

  Summary:
    DMAC channel DMAC channels object configuration.

  Description:
    This Configuration structure for the DMAC channels object, status,
    callback and associated context.

  Remarks:
    None.
*/

typedef struct
{
    /* DMAC Channel status */
    uint8_t                inUse;

    /* DMAC Channel callback */
    DMAC_CHANNEL_CALLBACK   callback;

    /* DMAC Channel callback context parameter */
    uintptr_t               context;

    /* DMAC Channel busy status */
    uint8_t                busyStatus;

} DMAC_CH_OBJECT ;

/* Descriptor section for DMAC */
static  dmacdescriptor_registers_t  descriptor_section[DMAC_CHANNELS_NUMBER]    SECTION_DMAC_DESCRIPTOR;

/* Initial write back memory section for DMAC */
static  dmacdescriptor_registers_t _write_back_section[DMAC_CHANNELS_NUMBER]    SECTION_DMAC_DESCRIPTOR;

/* DMAC User configuration */
DMAC_CONFIG_VAL   strDMACRegUserVal[DMAC_CHANNELS_NUMBER];

/* DMAC Channels object information structure */
DMAC_CH_OBJECT dmacChannelObj[DMAC_CHANNELS_NUMBER];

// *****************************************************************************
// *****************************************************************************
// Section: DMAC PLib Interface Implementations
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Function:
    void DMAC${DMAC_INDEX}_Initialize (void);

  Summary:
    Initializes the DMAC controller of the device.

  Description:
    This function initializes the DMAC controller of the device as configured
    by the user from within the DMAC manager of MHC.

  Remarks:
    Refer plib_dmac${DMAC_INDEX}.h for usage information.
*/

void DMAC${DMAC_INDEX}_Initialize( void )
{
    DMAC_CH_OBJECT *dmacChObj = (DMAC_CH_OBJECT *)&dmacChannelObj[0];
    DMAC_CHANNEL channel = DMAC_CHANNEL_0;

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
    <#if DMAC_CRC_ENABLE = true>
    /* If CRC is enabled, Set the input source, polynomial type and beat size */
    DMAC_REGS->DMAC_CRCCTRL = DMAC_QOSCTRL_CRCSRC_${DMAC_CRC_SRC}
                            | DMAC_QOSCTRL_CRCPOLY_${DMAC_CRC_POLY_TYPE}
                            | DMAC_QOSCTRL_CRCBEATSIZE_${DMAC_CRC_BEAT_SIZE};

    /* Quality of Service register update */
    DMAC_REGS->DMAC_QOSCTRL = DMAC_QOSCTRL_WRBQOS_${DMAC_WRITE_BACK_QOS}
                            | DMAC_QOSCTRL_FQOS_${DMAC_FETCH_QOS}
                            | DMAC_QOSCTRL_DQOS_${DMAC_DATA_XFER_QOS};
    </#if>

    /* Disable the DMAC and CRC module */
    DMAC_REGS->DMAC_CTRL &= ~DMAC_CTRL_DMAENABLE_Msk;
    DMAC_REGS->DMAC_CTRL &= ~DMAC_CTRL_CRCENABLE_Msk;

    /* Reset the DMAC module */
    DMAC_REGS->DMAC_CTRL |= DMAC_CTRL_SWRST_Msk;

    /* Update the Base address and Write Back address register */
    DMAC_REGS->DMAC_BASEADDR = (uint32_t) descriptor_section;
    DMAC_REGS->DMAC_WRBADDR  = (uint32_t)_write_back_section;

    /* Update the Priority Control register */
    DMAC_REGS->DMAC_PRICTRL0 = DMAC_PRICTRL0_LVLPRI0(${DMAC_LVLXPRIO_0})
                            | DMAC_PRICTRL0_LVLPRI1(${DMAC_LVLXPRIO_1})
                            | DMAC_PRICTRL0_LVLPRI2(${DMAC_LVLXPRIO_2})
                            | DMAC_PRICTRL0_LVLPRI3(${DMAC_LVLXPRIO_3});

    <#list 0..DMAC_CHAN_ENABLE_CNT - 1 as i>
        <#assign DMAC_CHCTRLA_ENABLE    = "DMAC_ENABLE_CH_"           + i>
        <#assign DMAC_CHCTRLA_RUNSTDBY  = "DMAC_CHCTRLA_RUNSTDBY_CH_" + i>
        <#assign DMAC_CHCTRLB_TRIGSRC   = "DMAC_CHCTRLB_TRIGSRC_CH_"  + i>
        <#assign DMAC_CHCTRLB_TRIGACT   = "DMAC_CHCTRLB_TRIGACT_CH_"  + i>
        <#assign DMAC_CHCTRLB_LVL       = "DMAC_CHCTRLB_LVL_CH_"      + i>
        <#assign DMAC_BTCTRL_STEPSIZE   = "DMAC_BTCTRL_STEPSIZE_CH_"  + i>
        <#assign DMAC_BTCTRL_STEPSEL    = "DMAC_BTCTRL_STEPSEL_CH_"   + i>
        <#assign DMAC_BTCTRL_SRCINC     = "DMAC_BTCTRL_SRCINC_CH_"    + i>
        <#assign DMAC_BTCTRL_DSTINC     = "DMAC_BTCTRL_DSTINC_CH_"    + i>
        <#assign DMAC_BTCTRL_BEATSIZE   = "DMAC_BTCTRL_BEATSIZE_CH_"  + i>
        <#assign DMAC_BTCTRL_BLOCKACT   = "DMAC_BTCTRL_BLOCKACT_CH_"  + i>
        <#assign DMAC_TRIGSRC_PERID_VAL = "DMAC_CHCTRLB_TRIGSRC_CH_" + i + "_PERID_VAL">

    <#if (.vars[DMAC_CHCTRLA_ENABLE] == true)>
    /* Set the DMA channel */
    DMAC_REGS->DMAC_CHID = ${i};

    /* Configure Channel Control A register for Channel ${i} */
    DMAC_REGS->DMAC_CHCTRLA = ${.vars[DMAC_CHCTRLA_RUNSTDBY]?then('DMAC_CHCTRLA_RUNSTDBY_Msk','0')} ;

    /*
     * Configure Channel Control B register
     * --> Software command (CMD)
     * --> Trigger Action (TRIGACT)
     * --> Trigger Source (TRIGSRC)
     * --> Channel Arbitration Level (LVL)
     * --> Channel Event Output Enable (EVOE)
     * --> Channel Event Input Enable (EVIE)
     * --> Event Input Action (EVACT)
     */
    <@compress single_line=true>DMAC_REGS->DMAC_CHCTRLB = DMAC_CHCTRLB_TRIGACT(${.vars[DMAC_CHCTRLB_TRIGACT]})
                                                        | DMAC_CHCTRLB_TRIGSRC(${.vars[DMAC_TRIGSRC_PERID_VAL]})
                                                        | DMAC_CHCTRLB_LVL(${.vars[DMAC_CHCTRLB_LVL]});</@compress>

    strDMACRegUserVal[${i}].dmacTrigSrc = ${.vars[DMAC_TRIGSRC_PERID_VAL]};

    /*
     * Configure BT Control register
     * --> Address Increment Step Size
     * --> Step Selection
     * --> Destination Address Increment Enable
     * --> Source Address Increment Enable
     * --> Beat Size
     * --> Block Action
     * --> Event Output Selection
     * --> Descriptor Valid
     */
    <@compress single_line=true>strDMACRegUserVal[${i}].dmacBTCTRLReg = DMAC_DESCRIPTOR_BTCTRL_BLOCKACT_NOACT
                                                                        | DMAC_DESCRIPTOR_BTCTRL_STEPSIZE_${.vars[DMAC_BTCTRL_STEPSIZE]}
                                                                        | DMAC_DESCRIPTOR_BTCTRL_STEPSEL_${.vars[DMAC_BTCTRL_STEPSEL]}
                                                                        | DMAC_DESCRIPTOR_BTCTRL_BEATSIZE_${.vars[DMAC_BTCTRL_BEATSIZE]}_Val
                                                                        | DMAC_DESCRIPTOR_BTCTRL_VALID_Msk
                                                                        ${.vars[DMAC_BTCTRL_SRCINC]?then('| DMAC_DESCRIPTOR_BTCTRL_SRCINC_Msk','')}
                                                                        ${.vars[DMAC_BTCTRL_DSTINC]?then('| DMAC_DESCRIPTOR_BTCTRL_DSTINC_Msk','')};</@compress>

    dmacChannelObj[${i}].inUse = 1;

    /*
     * Enable Interrupts -
     * --> Channel Transfer Error interrupt enable (TERR) and
     * --> Channel Transfer Complete interrupt enable (TCMPL)
     */
    DMAC_REGS->DMAC_CHINTENSET = (DMAC_CHINTENSET_TERR_Msk | DMAC_CHINTENSET_TCMPL_Msk);

    </#if>
    </#list>
    /* Enable the DMAC module & Priority Level x Enable */
    DMAC_REGS->DMAC_CTRL = DMAC_CTRL_DMAENABLE_Msk
                        | DMAC_CTRL_LVLEN0_Msk
                        | DMAC_CTRL_LVLEN1_Msk
                        | DMAC_CTRL_LVLEN2_Msk
                        | DMAC_CTRL_LVLEN3_Msk;

}

// *****************************************************************************
/* Function:
    void DMAC${DMAC_INDEX}_ChannelTransfer  (DMAC_CHANNEL channel,
                                            const void *srcAddr,
                                            const void *destAddr,
                                            size_t blockSize );

  Summary:
    Schedules a DMA transfer on the specified DMA channel.

  Description:
    This function schedules a DMA transfer on the specified DMA channel and
    starts the transfer when the configured trigger is received. The transfer is
    processed based on the channel configuration performed in the DMA manager.
    The channel parameter specifies the channel to be used for the transfer.

    The srcAddr parameter specifies the source address from where data will be
    transferred. This address will override the source address which was
    specified at the time of configuring the channel in DMA Manager. When a
    trigger is received, the module will transfer beat size of data from the
    source address. In such a case, the source address is typically a result
    register of the peripheral generating the trigger. For a memory to memory
    transfer, the srcAddress parameter points to the source address location in
    RAM.

    The destAddr parameter specifies the address location where the data will be
    stored. This parameter will override the setting in MHC. If the destination
    address is a peripheral register, the channel trigger may be an interrupt
    generated by the peripheral. In case of a memory to memory transfer, this is
    the address where the data will be stored.

    If the channel is configured for software trigger, calling the channel
    transfer function will set the source and destination address and will also
    start the transfer. If the channel was configured for a peripheral trigger,
    the channel transfer function will set the source and destination address
    and will transfer data when a trigger has occurred.

    If the requesting client registered an event callback function before
    calling the channel transfer function, this function will be called when the
    transfer completes. The callback function will be called with a
    DMAC_TRANSFER_COMPLETE event if the transfer was processed successfully and
    a DMAC_TRANSFER_ERROR event if the transfer was not processed successfully.

    When the transfer is in progress, the DMAC${DMAC_INDEX}_ChannelIsBusy
    function will return true. The channel transfer function should not be
    called while a transfer is already in progress. The contents of the source
    and the destination memory location should not be modified while the
    transfer is in progress.

  Remarks:
    Refer plib_dmac${DMAC_INDEX}.h for usage information.
*/

void DMAC${DMAC_INDEX}_ChannelTransfer( DMAC_CHANNEL channel, const void *srcAddr, const void *destAddr, size_t blockSize )
{
    /* Get a pointer to the module hardware instance */
    dmacdescriptor_registers_t *const dmacDescReg = &descriptor_section[channel];

    dmacChannelObj[channel].busyStatus = true;

    /*Set BT Control register */
    dmacDescReg->BTCTRL = strDMACRegUserVal[channel].dmacBTCTRLReg;

    /*Set source address */
    dmacDescReg->SRCADDR = (uint32_t) (srcAddr + blockSize);

    /* Set destination address */
    dmacDescReg->DSTADDR = (uint32_t) (destAddr + blockSize);

    /* Set block size */
    dmacDescReg->BTCNT = blockSize;

    /* Set the DMA channel */
    DMAC_REGS->DMAC_CHID = channel;

    /* Enable the channel */
    DMAC_REGS->DMAC_CHCTRLA |= DMAC_CHCTRLA_ENABLE_Msk;

    /* Verify if Trigger source is Software Trigger */
    if (strDMACRegUserVal[channel].dmacTrigSrc == 0x00)
    {
        /* Trigger the DMA transfer */
        DMAC_REGS->DMAC_SWTRIGCTRL |= (1 << channel);
    }
}

// *****************************************************************************
/* Function:
    bool DMAC${DMAC_INDEX}_ChannelIsBusy  (DMAC_CHANNEL channel );

  Summary:
    The function returns the busy status of the channel.

  Description:
    The function returns true if the specified channel is busy with a transfer.
    This function can be used to poll for the completion of transfer that was
    started by calling the DMAC${DMAC_INDEX}_ChannelTransfer() function. This
    function can be used as a polling alternative to the setting a callback
    function and receiving an asynchronous notification for transfer
    notification.

  Remarks:
    Refer plib_dmac${DMAC_INDEX}.h for usage information.
*/

bool DMAC${DMAC_INDEX}_ChannelIsBusy ( DMAC_CHANNEL channel )
{
    return (bool)dmacChannelObj[channel].busyStatus;
}

// *****************************************************************************
/* Function:
    void DMAC${DMAC_INDEX}_ChannelDisable  (DMAC_CHANNEL channel );

  Summary:
    The function disables the specified DMAC channel.

  Description:
    The function disables the specified DMAC channel. Once disabled, the channel
    will ignore triggers and will not transfer data till the next time a
    DMAC${DMAC_INDEX}_ChannelTransfer function is called.  If there is a
    transfer already in progress, this will aborted. If there were multiple
    linked transfers assigned on the channel, the on-going transfer will be
    aborted and the other descriptors will be discarded.

  Remarks:
    Refer plib_dmac${DMAC_INDEX}.h for usage information.
*/

void DMAC${DMAC_INDEX}_ChannelDisable ( DMAC_CHANNEL channel )
{
    /* Set the DMA Channel ID */
    DMAC_REGS->DMAC_CHID = channel;

    /* Disable the DMA channel */
    DMAC_REGS->DMAC_CHCTRLA &= (~DMAC_CHCTRLA_ENABLE_Pos);
}

<#if DMAC_DESC_LINKING = true>

// *****************************************************************************
/* Function:
    void DMAC${DMAC_INDEX}_ChannelLinkedListTransfer (DMAC_CHANNEL channel,
                                dmacdescriptor_registers_t* channelDesc);

  Summary:
    The function submit a list of DMA transfers.

  Description:
    The function will submit a list of DMA transfers. The DMA channel will
    process all transfers in the list. The transfers will be processed in the
    order in which they added to the list. Each transfer in the list is
    specified by a DmacDescriptor type descriptor. The list is formed by linking
    of the descriptors. While processing each descriptor in the linked list, the
    DMA transfer settings will be updated based on the settings contained in the
    descriptor.

    It is possible to link the last descriptor in the list to the first
    descriptor. This results in an un-distrupted transfer sequence. Such type of
    circular linked descriptor list are useful in audio applications. The DMAC
    module will generate a callback for each transfer in the descriptor list.
    The application must keep track of transfer being completed and should only
    modify the descriptors which have been processed.

    The application must submit the entire list while calling the function.
    Adding or inserting of descriptors to a submitted list is not supported. The
    application can change the transfer parameters such as transfer beat size,
    source and address increment step size. This will override the transfer
    setting defined in MHC.

    The BLOCKACT field of the last DMA transfer descriptor in the descriptor
    linked list should be set to the value 0x0 i.e. this should be set to
    disable the channel when the last transfer has been completed. Setting this
    field to any other value will interfere with the operation of the DMAC
    peripheral library.

  Remarks:
    Refer plib_dmac${DMAC_INDEX}.h for usage information.
*/

void DMAC${DMAC_INDEX}_ChannelLinkedListTransfer (DMAC_CHANNEL channel, dmacdescriptor_registers_t* channelDesc)
{
    /* Set the DMA channel */
    DMAC_REGS->DMAC_CHID = channel;

    dmacChannelObj[channel].busyStatus = true;

    /*Set BT Control register */
    channelDesc[channel].BTCTRL |= DMAC_DESCRIPTOR_BTCTRL_BLOCKACT_NOACT;

    memcpy(&descriptor_section[channel], channelDesc, sizeof(dmacdescriptor_registers_t));

    /* Enable the channel */
    DMAC_REGS->DMAC_CHCTRLA |= DMAC_CHCTRLA_ENABLE_Msk;

    /* Verify if Trigger source is Software Trigger */
    if (strDMACRegUserVal[channel].dmacTrigSrc == 0x00)
    {
        /* Trigger the DMA transfer */
        DMAC_REGS->DMAC_SWTRIGCTRL |= (1 << channel);
    }
}

</#if>

// *****************************************************************************
/* Function:
    void DMAC${DMAC_INDEX}_ChannelCallbackRegister( DMAC_CHANNEL channel,
                                    const DMAC_CHANNEL_CALLBACK callback,
                                    const uintptr_t context);

  Summary:
    This function allows a DMAC PLIB client to set an event handler.

  Description:
    This function allows a client to set an event handler. The client may want
    to receive transfer related events in cases when it submits a DMAC PLIB
    transfer request. The event handler should be set before the client
    intends to perform operations that could generate events.

    In case of linked transfer descriptors, the callback function will be called
    for every transfer in the transfer descriptor chain. The application must
    implement it's own logic to link the callback to the the transfer descriptor
    being completed.

    This function accepts a contextHandle parameter. This parameter could be
    set by the client to contain (or point to) any client specific data object
    that should be associated with this DMAC channel.

   Remarks:
    Refer plib_dmac${DMAC_INDEX}.h for usage information.
*/

void DMAC${DMAC_INDEX}_ChannelCallbackRegister( DMAC_CHANNEL channel, const DMAC_CHANNEL_CALLBACK callback, const uintptr_t context )
{
    dmacChannelObj[channel].callback = callback;

    dmacChannelObj[channel].context  = context;
}

// ******************************************************************************
/* Function:
    DMAC_CHANNEL_CONFIG  DMAC${DMAC_INDEX}_ChannelSettingsGet ( DMAC_CHANNEL channel );

  Summary:
    Returns the current channel settings for the specified DMAC Channel

  Description:
    This function returns the current channel setting for the specified DMAC
    channel. The application can use this function along with the
    DMAC${DMAC_INDEX}_ChannelSettingsSet function to analyze and if required
    change the transfer parameters of the DMAC channel at run time.

  Remarks:
    None.
*/

DMAC_CHANNEL_CONFIG DMAC${DMAC_INDEX}_ChannelSettingsGet (DMAC_CHANNEL channel)
{
    /* Get a pointer to the module hardware instance */
    dmacdescriptor_registers_t *const dmacDescReg = &descriptor_section[0];

    return (dmacDescReg->BTCTRL);
}

// ******************************************************************************
/* Function:
    bool  DMAC${DMAC_INDEX}_ChannelSettingsSet ( DMAC_CHANNEL channel, DMAC_CHANNEL_CONFIG settings );

  Summary:
    Changes the current transfer settings of the specified DMAC channel.

  Description:
    This function changes the current transfer settings of the specified DMAC
    channel.  The application can use this function along with the
    DMAC${DMAC_INDEX}_ChannelSettingsGet function to analyze and if required
    change the transfer parameters of the DMAC channel at run time.

    Calling this function while a transfer is in progress could result in
    unpredictable module operation. The application can use the
    DMAC${DMAC_INDEX}_ChannelTransfer() function to check if the channel is not
    busy and then change the channel settings. The new channel settings will be
    applicable on the next transfer that is schedule using the
    DMAC${DMAC_INDEX}_ChannelTransfer() function.

  Remarks:
    None.
*/

bool DMAC${DMAC_INDEX}_ChannelSettingsSet (DMAC_CHANNEL channel, DMAC_CHANNEL_CONFIG setting)
{
    /* Get a pointer to the module hardware instance */
    dmacdescriptor_registers_t *const dmacDescReg = &descriptor_section[0];

    /* Disable the channel */
    /* Set the DMA Channel ID */
    DMAC_REGS->DMAC_CHID = channel;

    /* Disable the DMA channel */
    DMAC_REGS->DMAC_CHCTRLA &= (~DMAC_CHCTRLA_ENABLE_Pos);

    /* Set the new settings */
    dmacDescReg->BTCTRL = setting;

    return true;
}

// *****************************************************************************
/* Function:
    void inline DMAC${DMAC_INDEX}_ISRHandler( void );

  Summary:
    Handles the DMA interrupt events.

  Description:
    This function handles the DMA interrupt events.

  Remarks:
    None.
*/

void DMAC${DMAC_INDEX}_ISRHandler( void )
{
    DMAC_CH_OBJECT  *dmacChObj = (DMAC_CH_OBJECT *)&dmacChannelObj[0];
    uint8_t channel = 0;
    volatile uint32_t chanIntStatus = 0;
    DMAC_TRANSFER_EVENT event   = DMAC_TRANSFER_EVENT_ERROR;

    for (channel = 0; channel < DMAC_CHANNELS_NUMBER; channel++)
    {
        /* Process events only on active channels */
        if (1 == dmacChObj->inUse)
        {
            /* Read the interrupt status for the active DMA channel */
            chanIntStatus = DMAC_REGS->DMAC_CHINTFLAG;

            /* It's an error interrupt */
            /* DMA channel interrupt handler */
            if (chanIntStatus & DMAC_CHINTENCLR_TERR_Msk)
            {
                /* Clear transfer error flag */
                DMAC_REGS->DMAC_CHINTFLAG = DMAC_CHINTENCLR_TERR_Msk;

                event = DMAC_TRANSFER_EVENT_ERROR;
                dmacChObj->busyStatus = false;
            }
            else if (chanIntStatus & DMAC_CHINTENCLR_TCMPL_Msk)
            {
                /* Clear the transfer complete flag */
                DMAC_REGS->DMAC_CHINTFLAG = DMAC_CHINTENCLR_TCMPL_Msk;

                event = DMAC_TRANSFER_EVENT_COMPLETE;
                dmacChObj->busyStatus = false;
            }
            else if (chanIntStatus & DMAC_CHINTENCLR_SUSP_Msk)
            {
                /* Clear the transfer suspend flag */
                DMAC_REGS->DMAC_CHINTFLAG = DMAC_CHINTENCLR_SUSP_Msk;

                dmacChObj->busyStatus = false;
            }

            /* Execute the callback function */
            if (dmacChObj[channel].callback)
            {
                dmacChObj[channel].callback (event, (uintptr_t) NULL);
            }
        }
    }
}
