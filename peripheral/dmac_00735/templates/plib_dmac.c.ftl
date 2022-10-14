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
<#if CoreSysIntFile == true>
#include "interrupts.h"
</#if>


<#assign DMA_INTERRUPT_ENABLED = false>
<#list 0..NUM_DMA_CHANS - 1 as i>
    <#assign CHANENABLE = "DMAC_CHAN" + i + "_ENBL">
    <#assign CHANINTENABLE = "DMAC_" + i + "_ENABLE_INTERRUPT">
    <#if .vars[CHANENABLE] == true && .vars[CHANINTENABLE] == true>
        <#assign DMA_INTERRUPT_ENABLED = true>
    </#if>
</#list>
// *****************************************************************************
// *****************************************************************************
// Section: Global Data
// *****************************************************************************
// *****************************************************************************

static DMAC_CHANNEL_OBJECT  gDMAChannelObj[${NUM_DMA_CHANS}];
static DMAC_CRC_SETUP gCRCSetup;

#define ConvertToPhysicalAddress(a) ((uint32_t)KVA_TO_PA(a))
#define ConvertToVirtualAddress(a)  PA_TO_KVA1(a)

// *****************************************************************************
// *****************************************************************************
// Section: ${DMA_INSTANCE_NAME} PLib Local Functions
// *****************************************************************************
// *****************************************************************************

static void ${DMA_INSTANCE_NAME}_ChannelSetAddresses(DMAC_CHANNEL channel, const void *srcAddr, const void *destAddr)
{
    const uint32_t *xsrcAddr = (const uint32_t *)srcAddr;
    const uint32_t *xdestAddr = (const uint32_t *)destAddr;

    uint32_t sourceAddress = (uint32_t)xsrcAddr;
    uint32_t destAddress = (uint32_t)xdestAddr;
    volatile uint32_t * regs;

    /* Set the source address */
    /* Check if the address lies in the KSEG2 for MZ devices */
    if ((sourceAddress >> 29) == 0x6U)
    {
        if ((sourceAddress >> 28)== 0xcU)
        {
            // EBI Address translation
            sourceAddress = ((sourceAddress | 0x20000000U) & 0x2FFFFFFFU);
        }
        else if((sourceAddress >> 28)== 0xDU)
        {
            //SQI Address translation
            sourceAddress = ((sourceAddress | 0x30000000U) & 0x3FFFFFFFU);
        }
		else
		{
			/* Do Nothing */
		}
    }
    else if ((sourceAddress >> 29) == 0x7U)
    {
        if ((sourceAddress >> 28)== 0xEU)
        {
            // EBI Address translation
            sourceAddress = ((sourceAddress | 0x20000000U) & 0x2FFFFFFFU);
        }
        else if ((sourceAddress >> 28)== 0xFU)
        {
            // SQI Address translation
            sourceAddress = ((sourceAddress | 0x30000000U) & 0x3FFFFFFFU);
        }
		else
		{
			/* Do Nothing */
		}
    }
    else
    {
        /* For KSEG0 and KSEG1, The translation is done by KVA_TO_PA */
        sourceAddress = ConvertToPhysicalAddress(sourceAddress);
    }

    /* Set the source address, DCHxSSA */
    regs = (volatile uint32_t *)(_DMAC_BASE_ADDRESS + ${DMAC_CHAN_OFST}U + (channel * ${DMAC_CH_SPACING}U) + ${DMAC_SSA_OFST}U);
    *(volatile uint32_t *)(regs) = sourceAddress;

    /* Set the destination address */
    /* Check if the address lies in the KSEG2 for MZ devices */
    if ((destAddress >> 29) == 0x6U)
    {
        // EBI Address translation
        if ((destAddress >> 28)== 0xcU)
        {
            destAddress = ((destAddress | 0x20000000U) & 0x2FFFFFFFU);
        }
        //SQI Address translation
        else if ((destAddress >> 28)== 0xdU)
        {
            destAddress = ((destAddress | 0x30000000U) & 0x3FFFFFFFU);
        }
		else
		{
			/* Do Nothing */
		}
    }
    else if ((destAddress >> 29) == 0x7U)
    {   /* Check if the address lies in the KSEG3 for MZ devices */
        // EBI Address translation
        if ((destAddress >> 28)== 0xeU)
        {
            destAddress = ((destAddress | 0x20000000U) & 0x2FFFFFFFU);
        }
        //SQI Address translation
        else if ((destAddress >> 28)== 0xfU)
        {
            destAddress = ((destAddress | 0x30000000U) & 0x3FFFFFFFU);
        }
		else
		{
			/* Do Nothing */
		}
    }
    else
    {
        /* For KSEG0 and KSEG1, The translation is done by KVA_TO_PA */
        destAddress = ConvertToPhysicalAddress(destAddress);
    }

    /* Set destination address, DCHxDSA */
    regs = (volatile uint32_t *)(_DMAC_BASE_ADDRESS + ${DMAC_CHAN_OFST}U + (channel * ${DMAC_CH_SPACING}U) + ${DMAC_DSA_OFST}U);
    *(volatile uint32_t *)(regs) = destAddress;
}

// *****************************************************************************
/* Function:
   static uint32_t ${DMA_INSTANCE_NAME}_BitReverse( uint32_t num, uint32_t bits)

  Summary:
    Reverses the bits in the given number

  Description:
    Reverses the bits in the given number based on the size of the number.
    Example:
        number  = 10110011
        reverse = 11001101

  Parameters:
    num - Number to be reversed
    bits - size of the number (8, 16, 32)

  Returns:
    reversed number
*/
static uint32_t ${DMA_INSTANCE_NAME}_BitReverse( uint32_t num, uint32_t bits)
{
    uint32_t out = 0;
    uint32_t i;

    for( i = 0U; i < bits; i++ )
    {
        out <<= 1;

        if(( num & 1U ) != 0U)
        {
            out |= 1U;
        }

        num >>= 1;
    }

    return out;
}

// *****************************************************************************
// *****************************************************************************
// Section: DMAC PLib Interface Implementations
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

    for(chanIndex = 0U; chanIndex < ${NUM_DMA_CHANS}U; chanIndex++)
    {
        chanObj->inUse          =    false;
<#if DMA_INTERRUPT_ENABLED == true>
        chanObj->pEventCallBack =    NULL;
        chanObj->hClientArg     =    0;
</#if>
        chanObj->errorInfo      =    DMAC_ERROR_NONE;
        chanObj++; /* linked list 'next' */
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
        <#assign INTREGVAL = "DCH" + i + "_INT_VALUE">
        <#assign CHSIRQ = "DMAC_REQUEST_" + i + "_SOURCE_VALUE">
        <#assign SIRQEN = "DCH" + i + "_ECON_SIRQEN_VALUE">
        <#assign CHBSIE = "DCH" + i + "_INT_CHBCIE_VALUE">
        <#assign CHPRI = "DCH" + i + "_CON_CHPRI_VALUE">
        <#assign CHSHIE = "DMAC_" + i + "_SOURCE_HALF_EMPTY_INT_ENABLE">
        <#assign CHDHIE = "DMAC_" + i + "_DESTINATION_HALF_FULL_INT_ENABLE">
        <#assign CHAEN = "DMAC_" + i + "_ALWAYS_ENABLE">
        <#assign CHCHN = "DMAC_" + i + "_CHAIN_ENABLE">
        <#assign CHCHNS = "DMAC_" + i + "_CHAIN_DIRECTION">
        <#assign CHAED = "DMAC_" + i + "_EVENTS_WHEN_DISABLED">
        <#assign STATCLRREG = "DMA" + i + "_STATREG_RD">
        <#lt>    /* DMA channel ${i} configuration */
        <#lt>    /* CHPRI = ${.vars[CHPRI]}, CHAEN= ${.vars[CHAEN]?then("1","0")}, CHCHN= ${.vars[CHCHN]?then("1","0")}, CHCHNS= ${.vars[CHCHNS]}, CHAED= ${.vars[CHAED]?then("1","0")} */
        <#lt>    ${DMACONREG} = 0x${.vars[DMACONVAL]};
        <#lt>    /* CHSIRQ = ${.vars[CHSIRQ]}, SIRQEN = ${.vars[SIRQEN]} */
        <#lt>    ${DMAECONREG} = 0x${.vars[DMAECONVAL]};
        <#lt>    /* CHBCIE = 1, CHTAIE=1, CHERIE=1, CHSHIE= ${.vars[CHSHIE]?then("1","0")}, CHDHIE= ${.vars[CHDHIE]?then("1","0")} */
        <#lt>    ${DMAINTREG} = 0x${.vars[INTREGVAL]};

    </#if>
</#list>
<#lt>    /* Enable DMA channel interrupts */
<#lt>    <@compress single_line=true>
<#lt>    IEC${.vars[STATCLRREG]}SET = 0U
<#list 0..NUM_DMA_CHANS - 1 as i>
    <#assign CHANENABLE = "DMAC_CHAN" + i + "_ENBL">
    <#assign CHANINTENABLE = "DMAC_" + i + "_ENABLE_INTERRUPT">
    <#if .vars[CHANENABLE] == true && .vars[CHANINTENABLE] == true>
        <#assign STATREGMASK = "DMA" + i + "_STATREG_MASK">
         | ${.vars[STATREGMASK]}U
    </#if>
</#list>
;
</@compress>

}

<#if DMA_INTERRUPT_ENABLED == true>
void ${DMA_INSTANCE_NAME}_ChannelCallbackRegister(DMAC_CHANNEL channel, const DMAC_CHANNEL_CALLBACK eventHandler, const uintptr_t contextHandle)
{
    gDMAChannelObj[channel].pEventCallBack = eventHandler;

    gDMAChannelObj[channel].hClientArg = contextHandle;
}
</#if>

bool ${DMA_INSTANCE_NAME}_ChannelTransfer(DMAC_CHANNEL channel, const void *srcAddr, size_t srcSize, const void *destAddr, size_t destSize, size_t cellSize)
{
    bool returnStatus = false;
    volatile uint32_t *regs;
    uint32_t DCHxINT_Flags;

    regs = ((volatile uint32_t *)(_DMAC_BASE_ADDRESS + ${DMAC_CHAN_OFST}U + (channel * ${DMAC_CH_SPACING}U) + ${DMAC_INT_OFST}U));
    DCHxINT_Flags = *(volatile uint32_t *)(regs) & (_DCH0INT_CHERIF_MASK | _DCH0INT_CHTAIF_MASK | _DCH0INT_CHBCIF_MASK);

    if((gDMAChannelObj[channel].inUse == false) || (DCHxINT_Flags != 0U))
    {
        /* Clear all the interrupt flags */
        regs = (volatile uint32_t *)(_DMAC_BASE_ADDRESS + ${DMAC_CHAN_OFST}U + (channel * ${DMAC_CH_SPACING}U) + ${DMAC_INT_OFST}U) + 1U;
        *(volatile uint32_t *)(regs) = (_DCH0INT_CHSHIF_MASK |_DCH0INT_CHDHIF_MASK | _DCH0INT_CHBCIF_MASK | _DCH0INT_CHTAIF_MASK| _DCH0INT_CHERIF_MASK);

        gDMAChannelObj[channel].inUse = true;
        returnStatus = true;

        /* Set the source / destination addresses, DCHxSSA and DCHxDSA */
        ${DMA_INSTANCE_NAME}_ChannelSetAddresses(channel, srcAddr, destAddr);

        /* Set the source size, DCHxSSIZ */
        regs = (volatile uint32_t *)(_DMAC_BASE_ADDRESS + ${DMAC_CHAN_OFST}U + (channel * ${DMAC_CH_SPACING}U) + ${DMAC_SSIZ_OFST}U);
        *(volatile uint32_t *)(regs) = srcSize;

        /* Set the destination size, DCHxDSIZ */
        regs = (volatile uint32_t *)(_DMAC_BASE_ADDRESS + ${DMAC_CHAN_OFST}U + (channel * ${DMAC_CH_SPACING}U) + ${DMAC_DSIZ_OFST}U);
        *(volatile uint32_t *)(regs) = destSize;

        /* Set the cell size, DCHxCSIZ */
        regs = (volatile uint32_t *)(_DMAC_BASE_ADDRESS + ${DMAC_CHAN_OFST}U + (channel * ${DMAC_CH_SPACING}U) + ${DMAC_CSIZ_OFST}U);
        *(volatile uint32_t *)(regs) = cellSize;

        /* Enable the channel */
        /* CHEN = 1 */
        regs = (volatile uint32_t *)(_DMAC_BASE_ADDRESS + ${DMAC_CHAN_OFST}U + (channel * ${DMAC_CH_SPACING}U) + ${DMAC_CON_OFST}U)+2U;
        *(volatile uint32_t *)(regs) = _DCH0CON_CHEN_MASK;

        /* Check Channel Start IRQ Enable bit - SIRQEN */
         regs = (volatile uint32_t *)(_DMAC_BASE_ADDRESS + ${DMAC_CHAN_OFST}U + (channel * ${DMAC_CH_SPACING}U) + ${DMAC_ECON_OFST}U);

        /* Initiate transfer if user did not set up channel for interrupt-initiated transfer. */
        if((*(volatile uint32_t *)(regs) & _DCH1ECON_SIRQEN_MASK) == 0U)
        {
            /* CFORCE = 1 */
            regs = (volatile uint32_t *)(_DMAC_BASE_ADDRESS + ${DMAC_CHAN_OFST}U + (channel * ${DMAC_CH_SPACING}U) + ${DMAC_ECON_OFST}U)+2U;
            *(volatile uint32_t *)(regs) = _DCH0ECON_CFORCE_MASK;
        }
    }

    return returnStatus;
}

bool ${DMA_INSTANCE_NAME}_ChainTransferSetup( DMAC_CHANNEL channel, const void *srcAddr, size_t srcSize, const void *destAddr, size_t destSize, size_t cellSize)
{
    bool returnStatus = false;
    volatile uint32_t *regs;
    uint32_t DCHxINT_Flags;

    regs = ((volatile uint32_t *)(_DMAC_BASE_ADDRESS + ${DMAC_CHAN_OFST}U + (channel * ${DMAC_CH_SPACING}U) + ${DMAC_INT_OFST}U));
    DCHxINT_Flags = *(volatile uint32_t *)(regs) & (_DCH0INT_CHERIF_MASK | _DCH0INT_CHTAIF_MASK | _DCH0INT_CHBCIF_MASK);

    if((gDMAChannelObj[channel].inUse == false) || (DCHxINT_Flags != 0U))
    {
        /* Clear all the interrupt flags */
        regs = (volatile uint32_t *)(_DMAC_BASE_ADDRESS + ${DMAC_CHAN_OFST}U + (channel * ${DMAC_CH_SPACING}U) + ${DMAC_INT_OFST}U) + 1U;
        *(volatile uint32_t *)(regs) = (_DCH0INT_CHSHIF_MASK |_DCH0INT_CHDHIF_MASK | _DCH0INT_CHBCIF_MASK | _DCH0INT_CHTAIF_MASK| _DCH0INT_CHERIF_MASK);

        gDMAChannelObj[channel].inUse = true;
        returnStatus = true;

        /* Set the source / destination addresses, DCHxSSA and DCHxDSA */
        ${DMA_INSTANCE_NAME}_ChannelSetAddresses(channel, srcAddr, destAddr);

        /* Set the source size, DCHxSSIZ */
        regs = (volatile uint32_t *)(_DMAC_BASE_ADDRESS + ${DMAC_CHAN_OFST}U + (channel * ${DMAC_CH_SPACING}U) + ${DMAC_SSIZ_OFST}U);
        *(volatile uint32_t *)(regs) = srcSize;

        /* Set the destination size, DCHxDSIZ */
        regs = (volatile uint32_t *)(_DMAC_BASE_ADDRESS + ${DMAC_CHAN_OFST}U + (channel * ${DMAC_CH_SPACING}U) + ${DMAC_DSIZ_OFST}U);
        *(volatile uint32_t *)(regs) = destSize;

        /* Set the cell size, DCHxCSIZ */
        regs = (volatile uint32_t *)(_DMAC_BASE_ADDRESS + ${DMAC_CHAN_OFST}U + (channel * ${DMAC_CH_SPACING}U) + ${DMAC_CSIZ_OFST}U);
        *(volatile uint32_t *)(regs) = cellSize;
    }

    return returnStatus;
}

void ${DMA_INSTANCE_NAME}_ChannelPatternMatchSetup(DMAC_CHANNEL channel, uint8_t patternMatchData)
{
    volatile uint32_t * patternRegs;
    patternRegs = (volatile uint32_t *)(_DMAC_BASE_ADDRESS + ${DMAC_CHAN_OFST}U + (channel * ${DMAC_CH_SPACING}U) + ${DMAC_PATTERN_DATA_OFST}U);
    *(volatile uint32_t *)(patternRegs) = patternMatchData;

    /* Enable Pattern Match */
    volatile uint32_t * eventConRegs;
    eventConRegs = (volatile uint32_t *)(_DMAC_BASE_ADDRESS + ${DMAC_CHAN_OFST}U + (channel * ${DMAC_CH_SPACING}U) + ${DMAC_ECON_OFST}U)+2U;
    *(volatile uint32_t *)(eventConRegs) = _DCH0ECON_PATEN_MASK;
}

void ${DMA_INSTANCE_NAME}_ChannelPatternMatchDisable(DMAC_CHANNEL channel)
{
    volatile uint32_t * eventConRegs;
    eventConRegs = (volatile uint32_t *)(_DMAC_BASE_ADDRESS + ${DMAC_CHAN_OFST}U + (channel * ${DMAC_CH_SPACING}U) + ${DMAC_ECON_OFST}U)+1U;
    *(volatile uint32_t *)(eventConRegs) = _DCH0ECON_PATEN_MASK;
}
void ${DMA_INSTANCE_NAME}_ChannelDisable(DMAC_CHANNEL channel)
{
    volatile uint32_t * regs;

    if(channel < ${NUM_DMA_CHANS}U)
    {
        /* Disable channel in register DCHxCON */
        /* CHEN = 0 */
        regs = (volatile uint32_t *)(_DMAC_BASE_ADDRESS + ${DMAC_CHAN_OFST}U + (channel * ${DMAC_CH_SPACING}U) + ${DMAC_CON_OFST}U)+1U;
        *(volatile uint32_t *)(regs) = _DCH0CON_CHEN_MASK;

        gDMAChannelObj[channel].inUse = false;
    }
}

bool ${DMA_INSTANCE_NAME}_ChannelIsBusy(DMAC_CHANNEL channel)
{
    uint32_t DCHxINT_Flags;
	bool channelstatus = false;

    DCHxINT_Flags = *(volatile uint32_t *)(_DMAC_BASE_ADDRESS + ${DMAC_CHAN_OFST}U + (channel * ${DMAC_CH_SPACING}U) + ${DMAC_INT_OFST}U);
    DCHxINT_Flags = DCHxINT_Flags & (_DCH0INT_CHERIF_MASK | _DCH0INT_CHTAIF_MASK | _DCH0INT_CHBCIF_MASK);

    if ((gDMAChannelObj[channel].inUse == true) && (DCHxINT_Flags == 0U))
    {
        channelstatus = true;
    }

    return channelstatus;
}

DMAC_TRANSFER_EVENT ${DMA_INSTANCE_NAME}_ChannelTransferStatusGet(DMAC_CHANNEL channel)
{
    uint32_t DCHxINT_Flags;

    DMAC_TRANSFER_EVENT dmaEvent = DMAC_TRANSFER_EVENT_NONE;

    DCHxINT_Flags = *(volatile uint32_t *)(_DMAC_BASE_ADDRESS + ${DMAC_CHAN_OFST}U + (channel * ${DMAC_CH_SPACING}U) + ${DMAC_INT_OFST}U);

    if ((DCHxINT_Flags & (_DCH0INT_CHSHIF_MASK | _DCH0INT_CHDHIF_MASK)) != 0U)  /* Dest Half-full or Src Half-empty flags */
    {
        dmaEvent = DMAC_TRANSFER_EVENT_HALF_COMPLETE;
    }
    if ((DCHxINT_Flags & (_DCH0INT_CHTAIF_MASK | _DCH0INT_CHERIF_MASK)) != 0U)  /* Abort or Error flags*/
    {
        dmaEvent = DMAC_TRANSFER_EVENT_ERROR;
    }
    if ((DCHxINT_Flags & _DCH0INT_CHBCIF_MASK) != 0U)   /* Block Transfer complete flag */
    {
        dmaEvent = DMAC_TRANSFER_EVENT_COMPLETE;
    }

    return dmaEvent;
}

void ${DMA_INSTANCE_NAME}_ChannelCRCSetup( DMAC_CHANNEL channel, DMAC_CRC_SETUP CRCSetup )
{
    uint32_t mask = 0;

    gCRCSetup.append_mode           = CRCSetup.append_mode;
    gCRCSetup.reverse_crc_input     = CRCSetup.reverse_crc_input;
    gCRCSetup.polynomial_length     = CRCSetup.polynomial_length;
    gCRCSetup.polynomial            = CRCSetup.polynomial;
    gCRCSetup.non_direct_seed       = CRCSetup.non_direct_seed;
    gCRCSetup.final_xor_value       = CRCSetup.final_xor_value;
    gCRCSetup.reverse_crc_output    = CRCSetup.reverse_crc_output;

    if (gCRCSetup.append_mode == true)
    {
        mask |= _DCRCCON_CRCAPP_MASK;
    }

    if (gCRCSetup.reverse_crc_input == true)
    {
        mask |= _DCRCCON_BITO_MASK;
    }

    mask |= (channel | _DCRCCON_CRCEN_MASK | (((uint32_t)gCRCSetup.polynomial_length - 1U) << _DCRCCON_PLEN_POSITION));

    /* Setup the DMA CRCCON register */
    DCRCCON = mask;

    /* Store the polynomial value */
    DCRCXOR = gCRCSetup.polynomial;

    /* Store the Initial seed value */
    DCRCDATA = gCRCSetup.non_direct_seed;
}

void ${DMA_INSTANCE_NAME}_CRCDisable( void )
{
    DCRCCONCLR = _DCRCCON_CRCEN_MASK;
}

uint32_t ${DMA_INSTANCE_NAME}_CRCRead( void )
{
    uint32_t crc = 0;

    /* Read the generated CRC value.
     * Once read ${DMA_INSTANCE_NAME}_CRCEnable() has to be called again before DMA Transfer for new CRC.
    */
    crc = DCRCDATA;

    /* Reverse the final crc value */
    if (gCRCSetup.reverse_crc_output == true)
    {
        crc = ${DMA_INSTANCE_NAME}_BitReverse(crc, gCRCSetup.polynomial_length);
    }

    crc ^= gCRCSetup.final_xor_value;

    return crc;
}

<#list 0..NUM_DMA_CHANS - 1 as i>
    <#assign CHANENABLE = "DMAC_CHAN" + i + "_ENBL">
    <#assign CHANINTENABLE = "DMAC_" + i + "_ENABLE_INTERRUPT">
    <#if .vars[CHANENABLE] == true && .vars[CHANINTENABLE] ==true>
        <#assign INTBITSREG = "DCH" + i + "INTbits_REG">
        <#assign INTREG = "DCH" + i + "INT_REG">
        <#assign STATCLRREG = "DMA" + i + "_STATREG_RD">
        <#assign STATREGMASK = "DMA" + i + "_STATREG_MASK">
<#if PRODUCT_FAMILY?contains("PIC32MM")>
void DMA${i}_InterruptHandler(void)
<#else>
void DMA_${i}_InterruptHandler(void)
</#if>
{
    DMAC_CHANNEL_OBJECT *chanObj;
    DMAC_TRANSFER_EVENT dmaEvent = DMAC_TRANSFER_EVENT_NONE;
    uint32_t VarRead = 0;

    /* Find out the channel object */
    chanObj = (DMAC_CHANNEL_OBJECT *) &gDMAChannelObj[${i}];

    /* Check whether the active DMA channel event has occurred */
    VarRead = ${.vars[INTBITSREG]}.CHDHIF;
    if((${.vars[INTBITSREG]}.CHSHIF == 1U) || ( VarRead == 1U))/* irq due to half complete */
    {
        /* Do not clear the flag here, it should be cleared with block transfer complete flag*/

        /* Update error and event */
        chanObj->errorInfo = DMAC_ERROR_NONE;
        dmaEvent = DMAC_TRANSFER_EVENT_HALF_COMPLETE;
        /* Since transfer is only half done yet, do not make inUse flag false */
    }
    if(${.vars[INTBITSREG]}.CHTAIF == 1U) /* irq due to transfer abort */
    {
        /* Channel is by default disabled on Transfer Abortion */
        /* Clear the Abort transfer complete flag */
        ${.vars[INTREG]}CLR = _DCH${i}INT_CHTAIF_MASK;

        /* Update error and event */
        chanObj->errorInfo = DMAC_ERROR_NONE;
        dmaEvent = DMAC_TRANSFER_EVENT_ERROR;
        chanObj->inUse = false;
    }
    if(${.vars[INTBITSREG]}.CHBCIF == 1U) /* irq due to transfer complete */
    {
        /* Channel is by default disabled on completion of a block transfer */
        /* Clear the Block transfer complete, half empty and half full interrupt flag */
        ${.vars[INTREG]}CLR = _DCH${i}INT_CHBCIF_MASK | _DCH${i}INT_CHSHIF_MASK | _DCH${i}INT_CHDHIF_MASK;

        /* Update error and event */
        chanObj->errorInfo = DMAC_ERROR_NONE;
        dmaEvent = DMAC_TRANSFER_EVENT_COMPLETE;
        chanObj->inUse = false;
    }
    if(${.vars[INTBITSREG]}.CHERIF == 1U) /* irq due to address error */
    {
        /* Clear the address error flag */
        ${.vars[INTREG]}CLR = _DCH${i}INT_CHERIF_MASK;

        /* Update error and event */
        chanObj->errorInfo = DMAC_ERROR_ADDRESS_ERROR;
        dmaEvent = DMAC_TRANSFER_EVENT_ERROR;
        chanObj->inUse = false;
    }

    /* Clear the interrupt flag and call event handler */
    IFS${.vars[STATCLRREG]}CLR = ${.vars[STATREGMASK]};

    if((chanObj->pEventCallBack != NULL) && (dmaEvent != DMAC_TRANSFER_EVENT_NONE))
    {
        chanObj->pEventCallBack(dmaEvent, chanObj->hClientArg);
    }
}
</#if>
</#list>
