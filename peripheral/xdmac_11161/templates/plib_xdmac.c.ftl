/*******************************************************************************
  XDMAC PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_xdmac.c

  Summary:
    XDMAC PLIB Implementation File

  Description:
    None

*******************************************************************************/

/*******************************************************************************
Copyright (c) 2017 released Microchip Technology Inc.  All rights reserved.

Microchip licenses to you the right to use, modify, copy and distribute
Software only when embedded on a Microchip microcontroller or digital signal
controller that is integrated into your product or third party product
(pursuant to the sublicense terms in the accompanying license agreement).

You should refer to the license agreement accompanying this Software for
additional information regarding your rights and obligations.

SOFTWARE AND DOCUMENTATION ARE PROVIDED AS IS  WITHOUT  WARRANTY  OF  ANY  KIND,
EITHER EXPRESS  OR  IMPLIED,  INCLUDING  WITHOUT  LIMITATION,  ANY  WARRANTY  OF
MERCHANTABILITY, TITLE, NON-INFRINGEMENT AND FITNESS FOR A  PARTICULAR  PURPOSE.
IN NO EVENT SHALL MICROCHIP OR  ITS  LICENSORS  BE  LIABLE  OR  OBLIGATED  UNDER
CONTRACT, NEGLIGENCE, STRICT LIABILITY, CONTRIBUTION,  BREACH  OF  WARRANTY,  OR
OTHER LEGAL  EQUITABLE  THEORY  ANY  DIRECT  OR  INDIRECT  DAMAGES  OR  EXPENSES
INCLUDING BUT NOT LIMITED TO ANY  INCIDENTAL,  SPECIAL,  INDIRECT,  PUNITIVE  OR
CONSEQUENTIAL DAMAGES, LOST  PROFITS  OR  LOST  DATA,  COST  OF  PROCUREMENT  OF
SUBSTITUTE  GOODS,  TECHNOLOGY,  SERVICES,  OR  ANY  CLAIMS  BY  THIRD   PARTIES
(INCLUDING BUT NOT LIMITED TO ANY DEFENSE  THEREOF),  OR  OTHER  SIMILAR  COSTS.
*******************************************************************************/

#include "plib_xdmac.h"

XDMAC_CH_OBJECT xdmacChannelObj[XDMAC_ACTIVE_CHANNELS_MAX];

<#--Implementation-->
// *****************************************************************************
// *****************************************************************************
// Section: XDMAC Implementation
// *****************************************************************************
// *****************************************************************************

void XDMAC_Initialize( void )
{
    XDMAC_CH_OBJECT *xdmacChObj = (XDMAC_CH_OBJECT *)&xdmacChannelObj[0];
    uint8_t channel = 0;

    /* Initialize channel objects */
	for(channel = 0; channel < XDMAC_ACTIVE_CHANNELS_MAX; channel++)
	{
		xdmacChObj->inUse = 0;
		xdmacChObj->event = XDMAC_TRANSFER_ERROR;
		xdmacChObj->callback = NULL;
		xdmacChObj->context = 0;

        /* Point to next channel object */
        xdmacChObj += 1;
	}

    <#list 0..23 as i>
	<#assign XDMAC_CH_ENABLE = "XDMAC_CH" + i + "_ENABLE">
    <#assign XDMAC_CC_TYPE = "XDMAC_CC" + i + "_TYPE">
	<#assign XDMAC_CC_DSYNC = "XDMAC_CC" + i + "_DSYNC">
	<#assign XDMAC_CC_SWREQ = "XDMAC_CC" + i + "_SWREQ">
	<#assign XDMAC_CC_DAM = "XDMAC_CC" + i + "_DAM">
	<#assign XDMAC_CC_SAM = "XDMAC_CC" + i + "_SAM">
	<#assign XDMAC_CC_SIF = "XDMAC_CC" + i + "_SIF">
	<#assign XDMAC_CC_DIF = "XDMAC_CC" + i + "_DIF">
	<#assign XDMAC_CC_DWIDTH = "XDMAC_CC" + i + "_DWIDTH">
	<#assign XDMAC_CC_CSIZE = "XDMAC_CC" + i + "_CSIZE">
	<#assign XDMAC_CC_MBSIZE = "XDMAC_CC" + i + "_MBSIZE">
	<#assign XDMAC_CC_PERID_VAL = "XDMAC_CC" + i + "_PERID_VAL">
        <#if .vars[XDMAC_CH_ENABLE]?has_content>
            <#if (.vars[XDMAC_CH_ENABLE] != false)>
	/* Configure Channel ${i} */
				<#if .vars[XDMAC_CC_TYPE]?has_content>
					<#if (.vars[XDMAC_CC_TYPE] == "PER_TRAN")>
	_XDMAC_REGS->XDMAC_CHID[${i}].XDMAC_CC.w = (XDMAC_CC_TYPE_${.vars[XDMAC_CC_TYPE]} | XDMAC_CC_PERID(${.vars[XDMAC_CC_PERID_VAL]}) | XDMAC_CC_DSYNC_${.vars[XDMAC_CC_DSYNC]} | XDMAC_CC_SWREQ_${.vars[XDMAC_CC_SWREQ]} | XDMAC_CC_DAM_${.vars[XDMAC_CC_DAM]} | XDMAC_CC_SAM_${.vars[XDMAC_CC_SAM]} | XDMAC_CC_SIF_${.vars[XDMAC_CC_SIF]} | XDMAC_CC_DIF_${.vars[XDMAC_CC_DIF]} | XDMAC_CC_DWIDTH_${.vars[XDMAC_CC_DWIDTH]} | XDMAC_CC_CSIZE_${.vars[XDMAC_CC_CSIZE]} | XDMAC_CC_MBSIZE_${.vars[XDMAC_CC_MBSIZE]});
					<#elseif (.vars[XDMAC_CC_TYPE] == "MEM_TRAN")>
	_XDMAC_REGS->XDMAC_CHID[${i}].XDMAC_CC.w = (XDMAC_CC_TYPE_${.vars[XDMAC_CC_TYPE]} | XDMAC_CC_DAM_${.vars[XDMAC_CC_DAM]} | XDMAC_CC_SAM_${.vars[XDMAC_CC_SAM]} | XDMAC_CC_SIF_${.vars[XDMAC_CC_SIF]} | XDMAC_CC_DIF_${.vars[XDMAC_CC_DIF]} | XDMAC_CC_DWIDTH_${.vars[XDMAC_CC_DWIDTH]} | XDMAC_CC_MBSIZE_${.vars[XDMAC_CC_MBSIZE]});
					</#if>
				</#if>
	_XDMAC_REGS->XDMAC_CHID[${i}].XDMAC_CIE.w = (XDMAC_CIE_BIE_Msk | XDMAC_CIE_RBIE_Msk | XDMAC_CIE_WBIE_Msk | XDMAC_CIE_ROIE_Msk);
	_XDMAC_REGS->XDMAC_GIE.w = (XDMAC_GIE_IE0_Msk << ${i});
	xdmacChannelObj[${i}].inUse = 1;

            </#if>
        </#if>
    </#list>
    return;
}

void XDMAC_ChannelCallbackRegister( XDMAC_CHANNEL channel, const XDMAC_CHANNEL_CALLBACK eventHandler, const uintptr_t contextHandle )
{
    xdmacChannelObj[channel].callback = eventHandler;
    xdmacChannelObj[channel].context = contextHandle;

	return;
}

void XDMAC_ChannelTransfer( XDMAC_CHANNEL channel, const void *srcAddr, const void *destAddr, size_t blockSize )
{
    volatile uint32_t status = 0;

    /* Clear channel level status before adding transfer parameters */
    status = _XDMAC_REGS->XDMAC_CHID[channel].XDMAC_CIS.w;
    (void)status;

    /*Set source address */
    _XDMAC_REGS->XDMAC_CHID[channel].XDMAC_CSA.w = (uint32_t)srcAddr;

    /* Set destination address */
    _XDMAC_REGS->XDMAC_CHID[channel].XDMAC_CDA.w = (uint32_t)destAddr;

	/* Set block size */
	_XDMAC_REGS->XDMAC_CHID[channel].XDMAC_CUBC.w = XDMAC_CUBC_UBLEN(blockSize);

	/* Enable the channel */
	_XDMAC_REGS->XDMAC_GE.w = (XDMAC_GE_EN0_Msk << channel);

	return;
}
<#if XDMAC_LL_ENABLE == true>

void XDMAC_ChannelLinkedListTransfer (XDMAC_CHANNEL channel, uint32_t descriptor, XDMAC_DESCRIPTOR_CONTROL* descriptorControl)
{
    volatile uint32_t status = 0;

    /* Clear channel level status before adding transfer parameters */
    status = _XDMAC_REGS->XDMAC_CHID[channel].XDMAC_CIS.w;
    (void)status;

    /* First descriptor control set */
    _XDMAC_REGS->XDMAC_CHID[channel].XDMAC_CNDC.w = (descriptorControl->mbr_ubc >> XDMAC_UBLEN_BIT_WIDTH);

    /* First descriptor address set */
    _XDMAC_REGS->XDMAC_CHID[channel].XDMAC_CNDA.w = ( (descriptor & XDMAC_CNDA_NDA_Msk) | XDMAC_CNDA_NDAIF_Msk ) ;

    /* Enable end of linked list interrupt source */
    _XDMAC_REGS->XDMAC_CHID[channel].XDMAC_CIE.w = XDMAC_CIE_LIE_Msk ;

	/* Enable the channel */
	_XDMAC_REGS->XDMAC_GE.w = (XDMAC_GE_EN0_Msk << channel);

	return;
}
</#if>
