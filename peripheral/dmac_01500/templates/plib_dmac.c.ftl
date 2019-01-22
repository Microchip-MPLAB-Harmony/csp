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
<#-- Decide whether to generate code for this system service.
     If no channels are enabled, then no need to generate code. -->
<#assign DMA_ENABLE = "false">
<#list 0..NUM_DMA_CHANS-1 as i>
<#assign CHANENABLE = "DMAC_CHAN"+i+"_ENBL">
<#if .vars[CHANENABLE]?c == "true">
<#assign DMA_ENABLE = "true">
</#if>
</#list>

<#if DMA_ENABLE == "true">
// *****************************************************************************
// *****************************************************************************
// Section: Global Data
// *****************************************************************************
// *****************************************************************************
DMA_CHANNEL_OBJECT  gSysDMAChannelObj[${NUM_DMA_CHANS}];

#define ConvertToPhysicalAddress(a) ((uint32_t)KVA_TO_PA(a))
#define ConvertToVirtualAddress(a)  PA_TO_KVA1(a)

/* Enable/disable interrupt mask bits for each DMA channel */
uint32_t dmaIrqEnbl[${NUM_DMA_CHANS}] =
{
<#list 0..NUM_DMA_CHANS-1 as i>
<#assign TARGET = "DMA"+i+"_ENBLREG_ENABLE_VALUE">
    ${.vars[TARGET]}, /* DMA${i} */
</#list>
};

/* Interrupt priority levels for each DMA channel */
uint32_t dmaIrqPriority[${NUM_DMA_CHANS}] =
{
<#list 0..NUM_DMA_CHANS-1 as i>
<#assign TARGET = "DMA_"+i+"_IRQ_PRIORITY">
<#assign SHIFT = "DMA"+i+"_PRIOREG_SHIFT">
    ${.vars[TARGET]} << ${.vars[SHIFT]},   /* DMA${i} */
</#list>
};

/* Interrupt subpriority levels for each DMA channel */
uint32_t dmaIrqSubPriority[${NUM_DMA_CHANS}] =
{
<#list 0..NUM_DMA_CHANS-1 as i>
<#assign TARGET = "DMA"+i+"_SUBPRIORITY">
<#assign SHIFT = "DMA"+i+"_SUBPRIOREG_SHIFT">
    ${.vars[TARGET]} << ${.vars[SHIFT]},  /* DMA${i} */
</#list>
};

/* Indicator of whether peripheral or SW should start a transfer. On a
   per-channel basis, used at runtime in channel-based function call.  */
bool dmaInterruptStartXfer[${NUM_DMA_CHANS}] =
{
<#list 0..NUM_DMA_CHANS-1 as i>
<#assign VALUE = "DCH"+i+"_ECON_SIRQEN_VALUE">
    ${.vars[VALUE]},
</#list>
};

// *****************************************************************************
// *****************************************************************************
// Section: DMAC PLib Local Functions
// *****************************************************************************
// *****************************************************************************
/* Function:
   static void ${DMA_INSTANCE_NAME}_ChannelSetAddresses

  Summary:
    Converter to physical start addresses for DMA address registers to use

  Description:
    Calculates physical start addresses and stores into source and destination
    address registers DCHxSSA and DCHxDSA.

  Parameters:
    DMA_CHANNEL channel - DMA channel this function call pertains to
    const void *srcAddr - starting address of source buffer to transfer
    const void *destAddr - starting address of destination buffer to transfer

  Returns:
    void
*/
static void ${DMA_INSTANCE_NAME}_ChannelSetAddresses( DMA_CHANNEL channel, const void *srcAddr, const void *destAddr)
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
    { /* Check if the address lies in the KSEG3 for MZ devices */
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
        /*For KSEG0 and KSEG1, The translation is done by KVA_TO_PA */
        destAddress = ConvertToPhysicalAddress(destAddress);
    }
    
    /* Set destination address, DCHxDSA */
    regs = (volatile uint32_t *)(_DMAC_BASE_ADDRESS + ${DMAC_CHAN_OFST} + (channel * ${DMAC_CH_SPACING}) + ${DMAC_DSA_OFST});
    *(volatile uint32_t *)(regs) = destAddress;
}

// *****************************************************************************
// *****************************************************************************
// Section: DMAC PLib Interface Implementations
// *****************************************************************************
// *****************************************************************************


// *****************************************************************************
/* Function:
   void ${DMA_INSTANCE_NAME}_ChannelCallbackRegister

  Summary:
    Callback function registration function

  Description:
    Registers the callback function (and context pointer, if used) for a given DMA interrupt.

  Parameters:
    DMA_CHANNEL channel - DMA channel this callback pertains to
    const DMA_CHANNEL_TRANSFER_EVENT_HANDLER eventHandler - pointer to callback function
    const uintptr_t contextHandle - pointer of context information callback is to use (set to NULL if not used)

  Returns:
    void
*/
void ${DMA_INSTANCE_NAME}_ChannelCallbackRegister(DMA_CHANNEL channel, const DMA_CHANNEL_CALLBACK eventHandler, const uintptr_t contextHandle)
{
    gSysDMAChannelObj[channel].pEventCallBack = eventHandler;
    gSysDMAChannelObj[channel].hClientArg = contextHandle;
}


// *****************************************************************************
/* Function:
   bool ${DMA_INSTANCE_NAME}_ChannelTransfer

  Summary:
    DMA channel transfer function

  Description:
    Sets up a DMA transfer, and starts the transfer if user specified a 
    software-initiated transfer in Harmony.

  Parameters:
    DMA_CHANNEL channel - DMA channel to use for this transfer
    const void *srcAddr - pointer to source data
    const void *destAddr - pointer to where data is to be moved to
    size_t blockSize - the transfer size to use

  Returns:
    false, if DMA already is busy / true, if DMA is not busy before calling function
*/
bool ${DMA_INSTANCE_NAME}_ChannelTransfer( DMA_CHANNEL channel, const void *srcAddr, const void *destAddr, size_t blockSize)
{
    volatile uint32_t status = 0;
    bool returnStatus = false;
    volatile uint32_t *regs;

    if(gSysDMAChannelObj[channel].inUse == false)
    {
        gSysDMAChannelObj[channel].inUse = true;
        returnStatus = true;
    }
    
    /* Set the source / destination addresses, DCHxSSA and DCHxDSA */
    ${DMA_INSTANCE_NAME}_ChannelSetAddresses(channel, srcAddr, destAddr);
    
    /* Set the source size, DCHxSSIZ */
    regs = (volatile uint32_t *)(_DMAC_BASE_ADDRESS + ${DMAC_CHAN_OFST} + (channel * ${DMAC_CH_SPACING}) + ${DMAC_SSIZ_OFST});
    *(volatile uint32_t *)(regs) = blockSize;
    
    /* Set the destination size (set same as source size), DCHxDSIZ */
    regs = (volatile uint32_t *)(_DMAC_BASE_ADDRESS + ${DMAC_CHAN_OFST} + (channel * ${DMAC_CH_SPACING}) + ${DMAC_DSIZ_OFST});
    *(volatile uint32_t *)(regs) = blockSize;
    
    /* Set the cell size (set same as source size), DCHxCSIZ */
    regs = (volatile uint32_t *)(_DMAC_BASE_ADDRESS + ${DMAC_CHAN_OFST} + (channel * ${DMAC_CH_SPACING}) + ${DMAC_CSIZ_OFST});
    *(volatile uint32_t *)(regs) = blockSize;
    
    /* Set the DMA interrupt priority and subpriority.  The particular IPCxx register depends on the
       particular DMA channel being enabled in this function call.                                   */
    if(channel < 2)
    {
        IPC33SET = dmaIrqPriority[channel] + dmaIrqSubPriority[channel];
    }
    else if(channel < 6)
    {
        IPC34SET = dmaIrqPriority[channel] + dmaIrqSubPriority[channel];    
    }
    else
    {
        IPC35SET = dmaIrqPriority[channel] + dmaIrqSubPriority[channel];
    }
    
    /* Enable the DMA interrupt.  There's one interrupt per channel; use the particular bitmask for this channel. */
    IEC4SET = dmaIrqEnbl[channel];
    
    /* Enable the channel */
    /* CHEN = 1 */
    regs = (volatile uint32_t *)(_DMAC_BASE_ADDRESS + ${DMAC_CHAN_OFST} + (channel * ${DMAC_CH_SPACING}) + ${DMAC_CON_OFST})+2;
    *(volatile uint32_t *)(regs) = _DCH0CON_CHEN_MASK;
    
    /* Initiate transfer if user did not set up channel for interrupt-initiated transfer. */
    if(dmaInterruptStartXfer[channel] == false)
    {
        /* CFORCE = 1 */
        regs = (volatile uint32_t *)(_DMAC_BASE_ADDRESS + ${DMAC_CHAN_OFST} + (channel * ${DMAC_CH_SPACING}) + ${DMAC_ECON_OFST})+2;        
        *(volatile uint32_t *)(regs) = _DCH0ECON_CFORCE_MASK;
    }
    return returnStatus;
}


// *****************************************************************************
/* Function:
   void ${DMA_INSTANCE_NAME}_ChannelDisable (DMA_CHANNEL channel)

  Summary:
    This function disables the DMA channel.

  Description:
    Disables the DMA channel specified.

  Parameters:
    DMA_CHANNEL channel - the particular channel to be disabled

  Returns:
    void
*/
void ${DMA_INSTANCE_NAME}_ChannelDisable (DMA_CHANNEL channel)
{
    volatile uint32_t * regs;
    
    if(channel < ${NUM_DMA_CHANS})
    {
        /* Disable channel in register DCHxCON */
        /* CHEN = 0 */
        regs = (volatile uint32_t *)(_DMAC_BASE_ADDRESS + ${DMAC_CHAN_OFST} + (channel * ${DMAC_CH_SPACING}) + ${DMAC_CON_OFST})+1;
        *(volatile uint32_t *)(regs) = _DCH0CON_CHEN_MASK;
    }
}

// *****************************************************************************
/* Function:
   bool ${DMA_INSTANCE_NAME}_ChannelIsBusy (DMA_CHANNEL channel)

  Summary:
    Reads the busy status of a channel.

  Description:
    Reads the busy status of a channel and returns status to caller.

  Parameters:
    DMA_CHANNEL channel - the particular channel to be interrogated

  Returns:
    true - channel is busy
    false - channel is not busy
*/
bool ${DMA_INSTANCE_NAME}_ChannelIsBusy (DMA_CHANNEL channel)
{
    volatile uint32_t * regs;
    
    if(channel < ${NUM_DMA_CHANS})
    {
        /* Read channel busy bit in register DCHxCON */
        regs = (volatile uint32_t *)(_DMAC_BASE_ADDRESS + ${DMAC_CHAN_OFST} + (channel * ${DMAC_CH_SPACING}) + ${DMAC_CON_OFST});
        return (bool)((*regs & _DCH0CON_CHBUSY_MASK) >> _DCH0CON_CHBUSY_POSITION);
    }
    else
    {
        return true;  /* return true for user error condition */
    }
}

// *****************************************************************************
/* Function:
   void ${DMA_INSTANCE_NAME}_ChannelBlockLengthSet (DMA_CHANNEL channel, uint16_t length)

  Summary:
    Sets the size of data to send.

  Description:
    Sets the chunk size for the indicated DMA channel.

  Parameters:
    DMA_CHANNEL channel - the particular channel to be set
    uint16_t length - new size of data to send out

  Returns:
    void
*/
void ${DMA_INSTANCE_NAME}_ChannelBlockLengthSet (DMA_CHANNEL channel, uint16_t length)
{
    volatile uint32_t * regs;
    
    if(channel < ${NUM_DMA_CHANS})
    {    
        /* Disable the channel via register DCHxCON, before applying new setting */
        /* CHEN = 0 */
        regs = (volatile uint32_t *)(_DMAC_BASE_ADDRESS + ${DMAC_CHAN_OFST} + (channel * ${DMAC_CH_SPACING}) + ${DMAC_CON_OFST})+1;
        *(volatile uint32_t *)(regs) = _DCH0CON_CHEN_MASK;
    
        /* Set DCHxCSIZ to new value */
        regs = (volatile uint32_t *)(_DMAC_BASE_ADDRESS + ${DMAC_CHAN_OFST} + (channel * ${DMAC_CH_SPACING}) + ${DMAC_CSIZ_OFST});
        *(volatile uint32_t *)(regs) = length;
    }
}

// *****************************************************************************
/* Function:
   bool ${DMA_INSTANCE_NAME}_ChannelSettingsSet (DMA_CHANNEL channel, uint32_t setting)

  Summary:
    DMA channel settings set function.

  Description:
    Sets the indicated DMA channel with user-specified settings.  Overwrites 
    DCHxCON register with new settings.

  Parameters:
    DMA_CHANNEL channel - the particular channel to be set
    uint16_t setting - new settins for channel

  Returns:
    true
*/
bool ${DMA_INSTANCE_NAME}_ChannelSettingsSet (DMA_CHANNEL channel, uint32_t setting)
{
    volatile uint32_t * regs;
    
    if(channel < ${NUM_DMA_CHANS})
    {
        /* Disable the channel via register DCHxCON, before applying new settings */
        /* CHEN = 0 */
        regs = (volatile uint32_t *)(_DMAC_BASE_ADDRESS + ${DMAC_CHAN_OFST} + (channel * ${DMAC_CH_SPACING}) + ${DMAC_CON_OFST})+1;
        *(volatile uint32_t *)(regs) = _DCH0CON_CHEN_MASK;
        
        /* Set DCHxCON with new setting */
        regs = (volatile uint32_t *)(_DMAC_BASE_ADDRESS + ${DMAC_CHAN_OFST} + (channel * ${DMAC_CH_SPACING}) + ${DMAC_CON_OFST});
        *(volatile uint32_t *)(regs) = setting;
    }
    return true;
}

// *****************************************************************************
/* Function:
   DMA_CHANNEL_CONFIG ${DMA_INSTANCE_NAME}_ChannelSettingsGet (DMA_CHANNEL channel)

  Summary:
    DMA channel settings get function.

  Description:
    Gets the indicated DMA channel settings in DCHxCON register and returns value
    to user.

  Parameters:
    DMA_CHANNEL channel - the particular channel to be set

  Returns:
    DMA_CHANNEL_CONFIG - DCHxCON value
    0 - user error condition where channel was specified out-of-bounds
*/
DMA_CHANNEL_CONFIG ${DMA_INSTANCE_NAME}_ChannelSettingsGet (DMA_CHANNEL channel)
{
    volatile uint32_t * regs;
    
    if(channel < ${NUM_DMA_CHANS})
    {
        /* Get DCHxCON */
        regs = (volatile uint32_t *)(_DMAC_BASE_ADDRESS + ${DMAC_CHAN_OFST} + (channel * ${DMAC_CH_SPACING}) + ${DMAC_CON_OFST});
        return (DMA_CHANNEL_CONFIG)*regs;
    }
    else
    {
        return 0;  /* return 0 for user error case */
    }
}

// *****************************************************************************
/* Function:
   void ${DMA_INSTANCE_NAME}_Initialize( void )

  Summary:
    This function initializes the DMAC controller of the device.

  Description:
    Sets up a DMA controller for subsequent transfer activity.

  Parameters:
    none

  Returns:
    void
*/
void ${DMA_INSTANCE_NAME}_Initialize( void )
{
    uint8_t chanIndex;
    DMA_CHANNEL_OBJECT *chanObj;

    /* Enable the DMA module */
    *(volatile uint32_t *)(&DMACONSET) = _DMACON_ON_MASK;

    /* Initialize the available channel objects */
    chanObj             =   (DMA_CHANNEL_OBJECT *)&gSysDMAChannelObj[0];
    for(chanIndex = 0; chanIndex < ${NUM_DMA_CHANS}; chanIndex++)
    {
        chanObj->inUse          =    false;
        chanObj->pEventCallBack =    NULL;
        chanObj->hClientArg     =    0;
        chanObj->errorInfo      =    DMA_ERROR_NONE;
        chanObj                 =    chanObj + 1;  /* linked list 'next' */
    }

    /* DMACON register */
    /* ON = 1          */
    DMACON = 0x${DMACON_REG_VALUE};

    /* DMA channel-level control registers.  They will have additional settings made when starting a transfer. */
<#list 0..NUM_DMA_CHANS-1 as i>
<#assign CHANENABLE = "DMAC_CHAN"+i+"_ENBL">
<#assign DMACONREG = "DCH"+i+"CON">
<#assign DMAECONREG = "DCH"+i+"ECON">
<#assign DMAINTREG = "DCH"+i+"INT">
<#assign DMACONVAL = "DCH"+i+"_CON_VALUE">
<#assign DMAECONVAL = "DCH"+i+"_ECON_VALUE">
<#assign DMAINTVAL = "DCH"+i+"_INT_VALUE">
<#assign CHSIRQ = "DMAC_REQUEST_"+i+"_SOURCE_VALUE">
<#assign SIRQEN = "DCH"+i+"_ECON_SIRQEN_VALUE">
<#assign CHBSIE = "DCH"+i+"_INT_CHBCIE_VALUE">
<#assign CHEN = "DCH"+i+"_CON_CHEN_VALUE">
<#assign CHPRI = "DCH"+i+"_CON_CHPRI_VALUE">
<#if .vars[CHANENABLE]?c == "true">
    /* DMA channel ${i} */
    /* DCHxCON */
    /* CHEN = ${.vars[CHEN]} */
    /* CHPRI = ${.vars[CHPRI]} */
    ${DMACONREG} = 0x${.vars[DMACONVAL]};
    
    /* DCHxECON */
    /* CHSIRQ = ${.vars[CHSIRQ]} */
    /* SIRQEN = ${.vars[SIRQEN]} */
    ${DMAECONREG} = 0x${.vars[DMAECONVAL]};
    
    /* DCHxCON */
    /* CHBCIE = ${.vars[CHBSIE]} */
    ${DMAINTREG} = 0x${.vars[DMAINTVAL]};

<#else>
    /* DMA channel ${i} - not enabled */
    /* Set registers for disabled configuration */
    ${DMAECONREG} = 0x${.vars[DMAECONVAL]};
    ${DMAINTREG} = 0x${.vars[DMAINTVAL]};
    ${DMACONREG} = 0x${.vars[DMACONVAL]};

</#if>
</#list>
}
<#list 0..NUM_DMA_CHANS-1 as i>
<#assign ENABLE = "DMA_"+i+"_INTERRUPT_ENABLE">
<#assign CHANENABLE = "DMAC_CHAN"+i+"_ENBL">
<#if .vars[ENABLE]?c == "true">
<#if .vars[CHANENABLE]?c == "true">
<#assign HANDLER = "DMA_"+i+"_IRQ_HANDLER">
<#assign VECTOR = "_DMA"+i+"_VECTOR">
<#assign PRIORITY = "DMA_"+i+"_IRQ_PRIORITY">
<#assign INTBITSREG = "DCH"+i+"INTbits_REG">
<#assign INTREG = "DCH"+i+"INT_REG">
<#assign STATCLRREG = "DMA"+i+"_STATREG_CLR">
<#assign STATREGMASK = "DMA"+i+"_STATREG_MASK">
<#assign DMATASKNAME = "DMA"+i+"_Tasks">
// *****************************************************************************
/* Function:
   void ${DMATASKNAME} (void)

  Summary:
    Interrupt handler for interrupts from DMA${i}.

  Description:
    None

  Parameters:
    none

  Returns:
    void
*/
void ${DMATASKNAME} (void)
{
<#assign DMACHAN = "DMA_CHANNEL_"+i>
    DMA_CHANNEL_OBJECT *chanObj;
    DMA_TRANSFER_EVENT dmaEvent = DMA_TRANSFER_EVENT_NONE;
    bool retVal;

    /* Find out the channel object */
    chanObj = (DMA_CHANNEL_OBJECT *) &gSysDMAChannelObj[${i}];
    
    /* Check whether the active DMA channel event has occurred */
    retVal = ${.vars[INTBITSREG]}.CHBCIF;
    if(true == retVal) /* irq due to transfer complete */
    {
        /* Channel is by default disabled on completion of a block transfer */


        /* Clear the Block transfer complete flag */
        *(volatile uint32_t *)(&${.vars[INTREG]}CLR) = _DCH${i}INT_CHBCIF_MASK;

        /* Update error and event */
        chanObj->errorInfo = DMA_ERROR_NONE;
        dmaEvent = DMA_TRANSFER_EVENT_COMPLETE;
    }
    else if(true == ${.vars[INTBITSREG]}.CHTAIF) /* irq due to transfer abort */
    {
        /* Channel is by default disabled on Transfer Abortion */

        /* Clear the Abort transfer complete flag */
        *(volatile uint32_t *)(&${.vars[INTREG]}CLR) = _DCH${i}INT_CHTAIF_MASK;

        /* Update error and event */
        chanObj->errorInfo = DMA_ERROR_NONE;
        dmaEvent = DMA_TRANSFER_EVENT_ABORT;
    }
    else if(true == ${.vars[INTBITSREG]}.CHERIF)
    {
        /* Clear the Block transfer complete flag */
        *(volatile uint32_t *)(&${.vars[INTREG]}CLR) = _DCH${i}INT_CHERIF_MASK;

        /* Update error and event */
        chanObj->errorInfo = DMA_ERROR_ADDRESS_ERROR;
        dmaEvent = DMA_TRANSFER_EVENT_ERROR;
    }
    
    /* Clear the interrupt flag and call event handler */
    if( (NULL != chanObj->pEventCallBack) && (DMA_TRANSFER_EVENT_NONE != dmaEvent) )
    {
        ${.vars[STATCLRREG]} = ${.vars[STATREGMASK]};       
        chanObj->pEventCallBack(dmaEvent, chanObj->hClientArg);
    }      
}
</#if>  <#-- .vars[ENABLE]?c == "true" -->
</#if>  <#-- .vars[CHANENABLE]?c == "true" -->
</#list>
</#if>  <#-- DMA_ENABLE == true -->
