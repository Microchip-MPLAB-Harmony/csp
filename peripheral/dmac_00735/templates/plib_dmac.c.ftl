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
* Copyright (C) 2019 Microchip Technology Inc. and its subsidiaries.
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

// *****************************************************************************
// *****************************************************************************
// Section: Global Data
// *****************************************************************************
// *****************************************************************************

static DMAC_CHANNEL_OBJECT  gDMAChannelObj[${NUM_DMA_CHANS}];

#define ConvertToPhysicalAddress(a) ((uint32_t)KVA_TO_PA(a))
#define ConvertToVirtualAddress(a)  PA_TO_KVA1(a)

// *****************************************************************************
// *****************************************************************************
// Section: ${DMA_INSTANCE_NAME} PLib Local Functions
// *****************************************************************************
// *****************************************************************************

static void ${DMA_INSTANCE_NAME}_ChannelSetAddresses(DMAC_CHANNEL channel, const void *srcAddr, const void *destAddr)
{
    uint32_t sourceAddress = (uint32_t)srcAddr;
    uint32_t destAddress = (uint32_t)destAddr;
    volatile uint32_t * regs;

    /* Set the source address */
    /* Check if the address lies in the KSEG2 for MZ devices */
    if ((sourceAddress >> 29) == 0x6)
    {
        if ((sourceAddress >> 28)== 0xc)
        {
            // EBI Address translation
            sourceAddress = ((sourceAddress | 0x20000000) & 0x2FFFFFFF);
        }
        else if((sourceAddress >> 28)== 0xD)
        {
            //SQI Address translation
            sourceAddress = ((sourceAddress | 0x30000000) & 0x3FFFFFFF);
        }
    }
    else if ((sourceAddress >> 29) == 0x7)
    {
        if ((sourceAddress >> 28)== 0xE)
        {
            // EBI Address translation
            sourceAddress = ((sourceAddress | 0x20000000) & 0x2FFFFFFF);
        }
        else if ((sourceAddress >> 28)== 0xF)
        {
            // SQI Address translation
            sourceAddress = ((sourceAddress | 0x30000000) & 0x3FFFFFFF);
        }
    }
    else
    {
        /* For KSEG0 and KSEG1, The translation is done by KVA_TO_PA */
        sourceAddress = ConvertToPhysicalAddress(sourceAddress);
    }

    /* Set the source address, DCHxSSA */
    regs = (volatile uint32_t *)(_DMAC_BASE_ADDRESS + ${DMAC_CHAN_OFST} + (channel * ${DMAC_CH_SPACING}) + ${DMAC_SSA_OFST});
    *(volatile uint32_t *)(regs) = sourceAddress;

    /* Set the destination address */
    /* Check if the address lies in the KSEG2 for MZ devices */
    if ((destAddress >> 29) == 0x6)
    {
        // EBI Address translation
        if ((destAddress >> 28)== 0xc)
        {
            destAddress = ((destAddress | 0x20000000) & 0x2FFFFFFF);
        }
        //SQI Address translation
        else if ((destAddress >> 28)== 0xd)
        {
            destAddress = ((destAddress | 0x30000000) & 0x3FFFFFFF);
        }
    }
    else if ((destAddress >> 29) == 0x7)
    {   /* Check if the address lies in the KSEG3 for MZ devices */
        // EBI Address translation
        if ((destAddress >> 28)== 0xe)
        {
            destAddress = ((destAddress | 0x20000000) & 0x2FFFFFFF);
        }
        //SQI Address translation
        else if ((destAddress >> 28)== 0xf)
        {
            destAddress = ((destAddress | 0x30000000) & 0x3FFFFFFF);
        }
    }
    else
    {
        /* For KSEG0 and KSEG1, The translation is done by KVA_TO_PA */
        destAddress = ConvertToPhysicalAddress(destAddress);
    }

    /* Set destination address, DCHxDSA */
    regs = (volatile uint32_t *)(_DMAC_BASE_ADDRESS + ${DMAC_CHAN_OFST} + (channel * ${DMAC_CH_SPACING}) + ${DMAC_DSA_OFST});
    *(volatile uint32_t *)(regs) = destAddress;
}

// *****************************************************************************
// *****************************************************************************
// Section: ${DMA_INSTANCE_NAME} PLib Interface Implementations
// *****************************************************************************
// *****************************************************************************

void ${DMA_INSTANCE_NAME}_Initialize(void)
{
    uint8_t chanIndex;
    DMAC_CHANNEL_OBJECT *chanObj;

    /* Enable the DMA module */
    DMACONSET = _DMACON_ON_MASK;

    /* Initialize the available channel objects */
    chanObj = (DMAC_CHANNEL_OBJECT *)&gDMAChannelObj[0];

    for(chanIndex = 0; chanIndex < ${NUM_DMA_CHANS}; chanIndex++)
    {
        chanObj->inUse          =    false;
        chanObj->pEventCallBack =    NULL;
        chanObj->hClientArg     =    0;
        chanObj->errorInfo      =    DMAC_ERROR_NONE;
        chanObj                 =    chanObj + 1;  /* linked list 'next' */
    }

    /* DMACON register */
    /* ON = 1          */
    DMACON = 0x${DMACON_REG_VALUE};

    /* DMA channel-level control registers.  They will have additional settings made when starting a transfer. */
<#list 0..NUM_DMA_CHANS - 1 as i>
    <#assign CHANENABLE = "DMAC_CHAN" + i + "_ENBL">
    <#if .vars[CHANENABLE] == true>
        <#assign DMACONREG = "DCH" + i + "CON">
        <#assign DMAECONREG = "DCH" + i + "ECON">
        <#assign DMAINTREG = "DCH" + i + "INT">
        <#assign DMACONVAL = "DCH" + i + "_CON_VALUE">
        <#assign DMAECONVAL = "DCH" + i + "_ECON_VALUE">
        <#assign CHSIRQ = "DMAC_REQUEST_" + i + "_SOURCE_VALUE">
        <#assign SIRQEN = "DCH" + i + "_ECON_SIRQEN_VALUE">
        <#assign CHBSIE = "DCH" + i + "_INT_CHBCIE_VALUE">
        <#assign CHPRI = "DCH" + i + "_CON_CHPRI_VALUE">
        <#assign STATCLRREG = "DMA" + i + "_STATREG_RD">
        <#lt>    /* DMA channel ${i} configuration */
        <#lt>    /* CHPRI = ${.vars[CHPRI]} */
        <#lt>    ${DMACONREG} = 0x${.vars[DMACONVAL]};

        <#lt>    /* CHSIRQ = ${.vars[CHSIRQ]}, SIRQEN = ${.vars[SIRQEN]} */
        <#lt>    ${DMAECONREG} = 0x${.vars[DMAECONVAL]};

        <#lt>    /* CHBCIE = 1, CHTAIE=1, CHERIE=1 */
        <#lt>    ${DMAINTREG} = 0xB0000;

    </#if>
</#list>
<#lt>    /* Enable DMA channel interrupts */
<#lt>    <@compress single_line=true>
<#lt>    IEC${.vars[STATCLRREG]}SET = 0
<#list 0..NUM_DMA_CHANS - 1 as i>
    <#assign CHANENABLE = "DMAC_CHAN" + i + "_ENBL">
    <#if .vars[CHANENABLE] == true>
        <#assign STATREGMASK = "DMA" + i + "_STATREG_MASK">
         | ${.vars[STATREGMASK]}
    </#if>
</#list>
;
</@compress>

}

void ${DMA_INSTANCE_NAME}_ChannelCallbackRegister(DMAC_CHANNEL channel, const DMAC_CHANNEL_CALLBACK eventHandler, const uintptr_t contextHandle)
{
    gDMAChannelObj[channel].pEventCallBack = eventHandler;

    gDMAChannelObj[channel].hClientArg = contextHandle;
}

bool ${DMA_INSTANCE_NAME}_ChannelTransfer(DMAC_CHANNEL channel, const void *srcAddr, size_t srcSize, const void *destAddr, size_t destSize, size_t cellSize)
{
    bool returnStatus = false;
    volatile uint32_t *regs;

    if(gDMAChannelObj[channel].inUse == false)
    {
        gDMAChannelObj[channel].inUse = true;
        returnStatus = true;

        /* Set the source / destination addresses, DCHxSSA and DCHxDSA */
        ${DMA_INSTANCE_NAME}_ChannelSetAddresses(channel, srcAddr, destAddr);

        /* Set the source size, DCHxSSIZ */
        regs = (volatile uint32_t *)(_DMAC_BASE_ADDRESS + ${DMAC_CHAN_OFST} + (channel * ${DMAC_CH_SPACING}) + ${DMAC_SSIZ_OFST});
        *(volatile uint32_t *)(regs) = srcSize;

        /* Set the destination size (set same as source size), DCHxDSIZ */
        regs = (volatile uint32_t *)(_DMAC_BASE_ADDRESS + ${DMAC_CHAN_OFST} + (channel * ${DMAC_CH_SPACING}) + ${DMAC_DSIZ_OFST});
        *(volatile uint32_t *)(regs) = destSize;

        /* Set the cell size (set same as source size), DCHxCSIZ */
        regs = (volatile uint32_t *)(_DMAC_BASE_ADDRESS + ${DMAC_CHAN_OFST} + (channel * ${DMAC_CH_SPACING}) + ${DMAC_CSIZ_OFST});
        *(volatile uint32_t *)(regs) = cellSize;

        /* Enable the channel */
        /* CHEN = 1 */
        regs = (volatile uint32_t *)(_DMAC_BASE_ADDRESS + ${DMAC_CHAN_OFST} + (channel * ${DMAC_CH_SPACING}) + ${DMAC_CON_OFST})+2;
        *(volatile uint32_t *)(regs) = _DCH0CON_CHEN_MASK;

        /* Check Channel Start IRQ Enable bit - SIRQEN */
         regs = (volatile uint32_t *)(_DMAC_BASE_ADDRESS + ${DMAC_CHAN_OFST} + (channel * ${DMAC_CH_SPACING}) + ${DMAC_ECON_OFST});

        /* Initiate transfer if user did not set up channel for interrupt-initiated transfer. */
        if((*(volatile uint32_t *)(regs) & _DCH1ECON_SIRQEN_MASK) == 0)
        {
            /* CFORCE = 1 */
            regs = (volatile uint32_t *)(_DMAC_BASE_ADDRESS + ${DMAC_CHAN_OFST} + (channel * ${DMAC_CH_SPACING}) + ${DMAC_ECON_OFST})+2;
            *(volatile uint32_t *)(regs) = _DCH0ECON_CFORCE_MASK;
        }
    }

    return returnStatus;
}

void ${DMA_INSTANCE_NAME}_ChannelDisable(DMAC_CHANNEL channel)
{
    volatile uint32_t * regs;

    if(channel < ${NUM_DMA_CHANS})
    {
        /* Disable channel in register DCHxCON */
        /* CHEN = 0 */
        regs = (volatile uint32_t *)(_DMAC_BASE_ADDRESS + ${DMAC_CHAN_OFST} + (channel * ${DMAC_CH_SPACING}) + ${DMAC_CON_OFST})+1;
        *(volatile uint32_t *)(regs) = _DCH0CON_CHEN_MASK;

        gDMAChannelObj[channel].inUse = false;
    }
}

bool ${DMA_INSTANCE_NAME}_ChannelIsBusy(DMAC_CHANNEL channel)
{
    return (gDMAChannelObj[channel].inUse);
}

<#list 0..NUM_DMA_CHANS - 1 as i>
    <#assign CHANENABLE = "DMAC_CHAN" + i + "_ENBL">
    <#if .vars[CHANENABLE] == true>
        <#assign INTBITSREG = "DCH" + i + "INTbits_REG">
        <#assign INTREG = "DCH" + i + "INT_REG">
        <#assign STATCLRREG = "DMA" + i + "_STATREG_RD">
        <#assign STATREGMASK = "DMA" + i + "_STATREG_MASK">
void DMA_${i}_InterruptHandler(void)
{
    DMAC_CHANNEL_OBJECT *chanObj;
    DMAC_TRANSFER_EVENT dmaEvent = DMAC_TRANSFER_EVENT_NONE;
    bool retVal;

    /* Find out the channel object */
    chanObj = (DMAC_CHANNEL_OBJECT *) &gDMAChannelObj[${i}];

    /* Check whether the active DMA channel event has occurred */
    retVal = ${.vars[INTBITSREG]}.CHBCIF;

    if(retVal == true) /* irq due to transfer complete */
    {
        /* Channel is by default disabled on completion of a block transfer */
        /* Clear the Block transfer complete flag */
        ${.vars[INTREG]}CLR = _DCH${i}INT_CHBCIF_MASK;

        /* Update error and event */
        chanObj->errorInfo = DMAC_ERROR_NONE;
        dmaEvent = DMAC_TRANSFER_EVENT_COMPLETE;
    }
    else if(${.vars[INTBITSREG]}.CHTAIF == true) /* irq due to transfer abort */
    {
        /* Channel is by default disabled on Transfer Abortion */
        /* Clear the Abort transfer complete flag */
        ${.vars[INTREG]}CLR = _DCH${i}INT_CHTAIF_MASK;

        /* Update error and event */
        chanObj->errorInfo = DMAC_ERROR_NONE;
        dmaEvent = DMAC_TRANSFER_EVENT_ERROR;
    }
    else if(${.vars[INTBITSREG]}.CHERIF == true)
    {
        /* Clear the Block transfer complete flag */
        ${.vars[INTREG]}CLR = _DCH${i}INT_CHERIF_MASK;

        /* Update error and event */
        chanObj->errorInfo = DMAC_ERROR_ADDRESS_ERROR;
        dmaEvent = DMAC_TRANSFER_EVENT_ERROR;
    }

    chanObj->inUse = false;

    IFS${.vars[STATCLRREG]}CLR = ${.vars[STATREGMASK]};

    /* Clear the interrupt flag and call event handler */
    if((chanObj->pEventCallBack != NULL) && (dmaEvent != DMAC_TRANSFER_EVENT_NONE))
    {
        chanObj->pEventCallBack(dmaEvent, chanObj->hClientArg);
    }
}

</#if>
</#list>
