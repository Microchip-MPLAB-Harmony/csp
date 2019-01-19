/*******************************************************************************
  Direct Memory Access Controller (DMAC) PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_dmac.c

  Summary
    Source for DMAC peripheral library interface Implementation.

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

#include "plib_dmac.h"

// *****************************************************************************
// *****************************************************************************
// Section: Global Data
// *****************************************************************************
// *****************************************************************************
DMA_CHANNEL_OBJECT  gSysDMAChannelObj[8];

#define ConvertToPhysicalAddress(a) ((uint32_t)KVA_TO_PA(a))
#define ConvertToVirtualAddress(a)  PA_TO_KVA1(a)

/* Enable/disable interrupt mask bits for each DMA channel */
uint32_t dmaIrqEnbl[8] =
{
    0x40, /* DMA0 */
    0x80, /* DMA1 */
    0x100, /* DMA2 */
    0x200, /* DMA3 */
    0x400, /* DMA4 */
    0x800, /* DMA5 */
    0x1000, /* DMA6 */
    0x2000, /* DMA7 */
};

/* Interrupt priority levels for each DMA channel */
uint32_t dmaIrqPriority[8] =
{
    7 << 18,   /* DMA0 */
    0 << 26,   /* DMA1 */
    0 << 2,   /* DMA2 */
    0 << 10,   /* DMA3 */
    0 << 18,   /* DMA4 */
    0 << 26,   /* DMA5 */
    0 << 2,   /* DMA6 */
    0 << 10,   /* DMA7 */
};

/* Interrupt subpriority levels for each DMA channel */
uint32_t dmaIrqSubPriority[8] =
{
    3 << 16,  /* DMA0 */
    0 << 24,  /* DMA1 */
    0 << 0,  /* DMA2 */
    0 << 8,  /* DMA3 */
    0 << 16,  /* DMA4 */
    0 << 24,  /* DMA5 */
    0 << 0,  /* DMA6 */
    0 << 8,  /* DMA7 */
};

/* Indicator of whether peripheral or SW should start a transfer. On a
   per-channel basis, used at runtime in channel-based function call.  */
bool dmaInterruptStartXfer[8] =
{
    1,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
};

// *****************************************************************************
// *****************************************************************************
// Section: DMAC PLib Local Functions
// *****************************************************************************
// *****************************************************************************
/* Function:
   static void DMAC_ChannelSetAddresses

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
static void DMAC_ChannelSetAddresses( DMA_CHANNEL channel, const void *srcAddr, const void *destAddr)
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
    regs = (volatile uint32_t *)(_DMAC_BASE_ADDRESS + 0x60 + (channel * 0xC0) + 0x30);
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
    regs = (volatile uint32_t *)(_DMAC_BASE_ADDRESS + 0x60 + (channel * 0xC0) + 0x40);
    *(volatile uint32_t *)(regs) = destAddress;
}

// *****************************************************************************
// *****************************************************************************
// Section: DMAC PLib Interface Implementations
// *****************************************************************************
// *****************************************************************************


// *****************************************************************************
/* Function:
   void DMAC_ChannelCallbackRegister

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
void DMAC_ChannelCallbackRegister(DMA_CHANNEL channel, const DMA_CHANNEL_CALLBACK eventHandler, const uintptr_t contextHandle)
{
    gSysDMAChannelObj[channel].pEventCallBack = eventHandler;
    gSysDMAChannelObj[channel].hClientArg = contextHandle;
}


// *****************************************************************************
/* Function:
   bool DMAC_ChannelTransfer

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
bool DMAC_ChannelTransfer( DMA_CHANNEL channel, const void *srcAddr, const void *destAddr, size_t blockSize)
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
    DMAC_ChannelSetAddresses(channel, srcAddr, destAddr);
    
    /* Set the source size, DCHxSSIZ */
    regs = (volatile uint32_t *)(_DMAC_BASE_ADDRESS + 0x60 + (channel * 0xC0) + 0x50);
    *(volatile uint32_t *)(regs) = blockSize;
    
    /* Set the destination size (set same as source size), DCHxDSIZ */
    regs = (volatile uint32_t *)(_DMAC_BASE_ADDRESS + 0x60 + (channel * 0xC0) + 0x60);
    *(volatile uint32_t *)(regs) = blockSize;
    
    /* Set the cell size (set same as source size), DCHxCSIZ */
    regs = (volatile uint32_t *)(_DMAC_BASE_ADDRESS + 0x60 + (channel * 0xC0) + 0x90);
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
    regs = (volatile uint32_t *)(_DMAC_BASE_ADDRESS + 0x60 + (channel * 0xC0) + 0x0)+2;
    *(volatile uint32_t *)(regs) = _DCH0CON_CHEN_MASK;
    
    /* Initiate transfer if user did not set up channel for interrupt-initiated transfer. */
    if(dmaInterruptStartXfer[channel] == false)
    {
        /* CFORCE = 1 */
        regs = (volatile uint32_t *)(_DMAC_BASE_ADDRESS + 0x60 + (channel * 0xC0) + 0x10)+2;        
        *(volatile uint32_t *)(regs) = _DCH0ECON_CFORCE_MASK;
    }
    return returnStatus;
}


// *****************************************************************************
/* Function:
   void DMAC_ChannelDisable (DMA_CHANNEL channel)

  Summary:
    This function disables the DMA channel.

  Description:
    Disables the DMA channel specified.

  Parameters:
    DMA_CHANNEL channel - the particular channel to be disabled

  Returns:
    void
*/
void DMAC_ChannelDisable (DMA_CHANNEL channel)
{
    volatile uint32_t * regs;
    
    if(channel < 8)
    {
        /* Disable channel in register DCHxCON */
        /* CHEN = 0 */
        regs = (volatile uint32_t *)(_DMAC_BASE_ADDRESS + 0x60 + (channel * 0xC0) + 0x0)+1;
        *(volatile uint32_t *)(regs) = _DCH0CON_CHEN_MASK;
    }
}

// *****************************************************************************
/* Function:
   bool DMAC_ChannelIsBusy (DMA_CHANNEL channel)

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
bool DMAC_ChannelIsBusy (DMA_CHANNEL channel)
{
    volatile uint32_t * regs;
    
    if(channel < 8)
    {
        /* Read channel busy bit in register DCHxCON */
        regs = (volatile uint32_t *)(_DMAC_BASE_ADDRESS + 0x60 + (channel * 0xC0) + 0x0);
        return (bool)((*regs & _DCH0CON_CHBUSY_MASK) >> _DCH0CON_CHBUSY_POSITION);
    }
    else
    {
        return true;  /* return true for user error condition */
    }
}

// *****************************************************************************
/* Function:
   void DMAC_ChannelBlockLengthSet (DMA_CHANNEL channel, uint16_t length)

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
void DMAC_ChannelBlockLengthSet (DMA_CHANNEL channel, uint16_t length)
{
    volatile uint32_t * regs;
    
    if(channel < 8)
    {    
        /* Disable the channel via register DCHxCON, before applying new setting */
        /* CHEN = 0 */
        regs = (volatile uint32_t *)(_DMAC_BASE_ADDRESS + 0x60 + (channel * 0xC0) + 0x0)+1;
        *(volatile uint32_t *)(regs) = _DCH0CON_CHEN_MASK;
    
        /* Set DCHxCSIZ to new value */
        regs = (volatile uint32_t *)(_DMAC_BASE_ADDRESS + 0x60 + (channel * 0xC0) + 0x90);
        *(volatile uint32_t *)(regs) = length;
    }
}

// *****************************************************************************
/* Function:
   bool DMAC_ChannelSettingsSet (DMA_CHANNEL channel, uint32_t setting)

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
bool DMAC_ChannelSettingsSet (DMA_CHANNEL channel, uint32_t setting)
{
    volatile uint32_t * regs;
    
    if(channel < 8)
    {
        /* Disable the channel via register DCHxCON, before applying new settings */
        /* CHEN = 0 */
        regs = (volatile uint32_t *)(_DMAC_BASE_ADDRESS + 0x60 + (channel * 0xC0) + 0x0)+1;
        *(volatile uint32_t *)(regs) = _DCH0CON_CHEN_MASK;
        
        /* Set DCHxCON with new setting */
        regs = (volatile uint32_t *)(_DMAC_BASE_ADDRESS + 0x60 + (channel * 0xC0) + 0x0);
        *(volatile uint32_t *)(regs) = setting;
    }
    return true;
}

// *****************************************************************************
/* Function:
   DMA_CHANNEL_CONFIG DMAC_ChannelSettingsGet (DMA_CHANNEL channel)

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
DMA_CHANNEL_CONFIG DMAC_ChannelSettingsGet (DMA_CHANNEL channel)
{
    volatile uint32_t * regs;
    
    if(channel < 8)
    {
        /* Get DCHxCON */
        regs = (volatile uint32_t *)(_DMAC_BASE_ADDRESS + 0x60 + (channel * 0xC0) + 0x0);
        return (DMA_CHANNEL_CONFIG)*regs;
    }
    else
    {
        return 0;  /* return 0 for user error case */
    }
}

// *****************************************************************************
/* Function:
   void DMAC_Initialize( void )

  Summary:
    This function initializes the DMAC controller of the device.

  Description:
    Sets up a DMA controller for subsequent transfer activity.

  Parameters:
    none

  Returns:
    void
*/
void DMAC_Initialize( void )
{
    uint8_t chanIndex;
    DMA_CHANNEL_OBJECT *chanObj;
    volatile uint32_t * regs;

    /* Enable the DMA module */
    *(volatile uint32_t *)(&DMACONSET) = _DMACON_ON_MASK;

    /* Initialize the available channel objects */
    chanObj             =   (DMA_CHANNEL_OBJECT *)&gSysDMAChannelObj[0];
    for(chanIndex = 0; chanIndex < 8; chanIndex++)
    {
        chanObj->inUse          =    false;
        chanObj->pEventCallBack =    NULL;
        chanObj->hClientArg     =    0;
        chanObj->errorInfo      =    DMA_ERROR_NONE;
        chanObj                 =    chanObj + 1;  /* linked list 'next' */
    }

    /* DMACON register */
    /* ON = 1          */
    DMACON = 0x8000;

    /* DMA channel-level control registers.  They will have additional settings made when starting a transfer. */
    /* DMA channel 0 */
    /* DCHxCON */
    /* CHEN = 0 */
    /* CHPRI = 2 */
    DCH0CON = 0x2;
    
    /* DCHxECON */
    /* CHSIRQ = 166 */
    /* SIRQEN = 1 */
    DCH0ECON = 0xa610;
    
    /* DCHxCON */
    /* CHBCIE = 1 */
    DCH0INT = 0x80000;

    /* DMA channel 1 - not enabled */
    /* Set registers for disabled configuration */
    DCH1ECON = 0x0;
    DCH1INT = 0x0;
    DCH1CON = 0x0;

    /* DMA channel 2 - not enabled */
    /* Set registers for disabled configuration */
    DCH2ECON = 0x0;
    DCH2INT = 0x0;
    DCH2CON = 0x0;

    /* DMA channel 3 - not enabled */
    /* Set registers for disabled configuration */
    DCH3ECON = 0x0;
    DCH3INT = 0x0;
    DCH3CON = 0x0;

    /* DMA channel 4 - not enabled */
    /* Set registers for disabled configuration */
    DCH4ECON = 0x0;
    DCH4INT = 0x0;
    DCH4CON = 0x0;

    /* DMA channel 5 - not enabled */
    /* Set registers for disabled configuration */
    DCH5ECON = 0x0;
    DCH5INT = 0x0;
    DCH5CON = 0x0;

    /* DMA channel 6 - not enabled */
    /* Set registers for disabled configuration */
    DCH6ECON = 0x0;
    DCH6INT = 0x0;
    DCH6CON = 0x0;

    /* DMA channel 7 - not enabled */
    /* Set registers for disabled configuration */
    DCH7ECON = 0x0;
    DCH7INT = 0x0;
    DCH7CON = 0x0;

}
// *****************************************************************************
/* Function:
   void DMA0_HANDLER (void)

  Summary:
    Interrupt handler for interrupts from DMA0

  Description:
    None

  Parameters:
    none

  Returns:
    void
*/
void __ISR(_DMA0_VECTOR, ipl7AUTO) DMA0_Handler (void)
{
    DMA_CHANNEL_OBJECT *chanObj;
    DMA_TRANSFER_EVENT dmaEvent = DMA_TRANSFER_EVENT_NONE;
    bool retVal;

    /* Find out the channel object */
    chanObj = (DMA_CHANNEL_OBJECT *) &gSysDMAChannelObj[0];
    
    /* Check whether the active DMA channel event has occurred */
    retVal = DCH0INTbits.CHBCIF;
    if(true == retVal) /* irq due to transfer complete */
    {
        /* Channel is by default disabled on completion of a block transfer */


        /* Clear the Block transfer complete flag */
        *(volatile uint32_t *)(&DCH0INTCLR) = _DCH0INT_CHBCIF_MASK;

        /* Update error and event */
        chanObj->errorInfo = DMA_ERROR_NONE;
        dmaEvent = DMA_TRANSFER_EVENT_COMPLETE;
    }
    else if(true == DCH0INTbits.CHTAIF) /* irq due to transfer abort */
    {
        /* Channel is by default disabled on Transfer Abortion */

        /* Clear the Abort transfer complete flag */
        *(volatile uint32_t *)(&DCH0INTCLR) = _DCH0INT_CHTAIF_MASK;

        /* Update error and event */
        chanObj->errorInfo = DMA_ERROR_NONE;
        dmaEvent = DMA_TRANSFER_EVENT_ABORT;
    }
    else if(true == DCH0INTbits.CHERIF)
    {
        /* Clear the Block transfer complete flag */
        *(volatile uint32_t *)(&DCH0INTCLR) = _DCH0INT_CHERIF_MASK;

        /* Update error and event */
        chanObj->errorInfo = DMA_ERROR_ADDRESS_ERROR;
        dmaEvent = DMA_TRANSFER_EVENT_ERROR;
    }
    
    /* Clear the interrupt flag and call event handler */
    if( (NULL != chanObj->pEventCallBack) && (DMA_TRANSFER_EVENT_NONE != dmaEvent) )
    {
        IFS4CLR = 0x40;       
        chanObj->pEventCallBack(dmaEvent, chanObj->hClientArg);
    }      
}
  
  
  
  
  
  
  
  
  
  