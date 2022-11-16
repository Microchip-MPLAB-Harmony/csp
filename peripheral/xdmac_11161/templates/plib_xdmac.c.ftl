/*******************************************************************************
  XDMAC PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${DMA_INSTANCE_NAME?lower_case}.c

  Summary:
    XDMAC PLIB Implementation File

  Description:
    None

*******************************************************************************/

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

#include "device.h"
#include "plib_${DMA_INSTANCE_NAME?lower_case}.h"
<#if CoreSysIntFile == true>
#include "interrupts.h"
</#if>

/* Macro for limiting XDMAC objects to highest channel enabled */
#define XDMAC_ACTIVE_CHANNELS_MAX (${XDMAC_HIGHEST_CHANNEL}U)
<#if XDMAC_LL_ENABLE == true>

#define XDMAC_UBLEN_BIT_WIDTH     (24)
</#if>

<#assign XDMAC_INTERRUPT_ENABLED = false>
<#list 0..DMA_CHANNEL_COUNT - 1 as i>
    <#assign XDMAC_CH_ENABLE = "XDMAC_CH" + i + "_ENABLE">
    <#assign XDMAC_INT_ENABLE = "XDMAC_CH" + i + "_ENABLE_INTERRUPT">
    <#if .vars[XDMAC_CH_ENABLE] == true && .vars[XDMAC_INT_ENABLE] == true>
        <#assign XDMAC_INTERRUPT_ENABLED = true>
    </#if>
</#list>

typedef struct
{
    uint8_t                inUse;
<#if XDMAC_INTERRUPT_ENABLED == true>
    XDMAC_CHANNEL_CALLBACK callback;
</#if>
    uintptr_t              context;
    bool                busyStatus;
<#if SECURE_INTERRUPT_AVAILABLE>
    bool isSecure;
</#if>
} XDMAC_CH_OBJECT ;

static XDMAC_CH_OBJECT xdmacChannelObj[XDMAC_ACTIVE_CHANNELS_MAX];

<#--Implementation-->
// *****************************************************************************
// *****************************************************************************
// Section: XDMAC Implementation
// *****************************************************************************
// *****************************************************************************
<#if XDMAC_INTERRUPT_ENABLED == true>
void ${DMA_INSTANCE_NAME}_InterruptHandler( void )
{
    XDMAC_CH_OBJECT *xdmacChObj = (XDMAC_CH_OBJECT *)&xdmacChannelObj[0];
    uint8_t channel = 0U;
    volatile uint32_t chanIntStatus = 0U;

    /* Iterate all channels */
    for (channel = 0U; channel < XDMAC_ACTIVE_CHANNELS_MAX; channel++)
    {
        /* Process events only channels that are active and has global interrupt enabled */
        if ((1U == xdmacChObj->inUse)${SECURE_INTERRUPT_AVAILABLE?string("&& !xdmacChObj->isSecure", "")} && ((${DMA_INSTANCE_NAME}_REGS->XDMAC_GIM & (XDMAC_GIM_IM0_Msk << (uint32_t)channel)) != 0U))
        {
            /* Read the interrupt status for the active DMA channel */
            chanIntStatus = ${DMA_INSTANCE_NAME}_REGS->XDMAC_CHID[channel].XDMAC_CIS;

            if ((chanIntStatus & ( XDMAC_CIS_RBEIS_Msk | XDMAC_CIS_WBEIS_Msk | XDMAC_CIS_ROIS_Msk)) != 0U)
            {
                xdmacChObj->busyStatus = false;

                /* It's an error interrupt */
                if (NULL != xdmacChObj->callback)
                {
                    xdmacChObj->callback(XDMAC_TRANSFER_ERROR, xdmacChObj->context);
                }
            }
            else if ((chanIntStatus & XDMAC_CIS_BIS_Msk) != 0U)
            {
                xdmacChObj->busyStatus = false;

                /* It's a block transfer complete interrupt */
                if (NULL != xdmacChObj->callback)
                {
                    xdmacChObj->callback(XDMAC_TRANSFER_COMPLETE, xdmacChObj->context);
                }
            }
            else
            {
                ; /* No action required - ; is optional */
            }

        }

        /* Point to next channel object */
        xdmacChObj++;
    }
}
<#if SECURE_INTERRUPT_AVAILABLE>

void ${DMA_INSTANCE_NAME}_SINT_InterruptHandler( void )
{
    XDMAC_CH_OBJECT *xdmacChObj = (XDMAC_CH_OBJECT *)&xdmacChannelObj[0];
    uint8_t channel = 0U;
    volatile uint32_t chanIntStatus = 0U;

    /* Iterate all channels */
    for (channel = 0U; channel < XDMAC_ACTIVE_CHANNELS_MAX; channel++)
    {
        /* Process events only channels that are active and has global interrupt enabled */
        if ((1U == xdmacChObj->inUse) && (xdmacChObj->isSecure != false) && ((${DMA_INSTANCE_NAME}_REGS->XDMAC_GIM & (XDMAC_GIM_IM0_Msk << channel)) != 0U))
        {
            /* Read the interrupt status for the active DMA channel */
            chanIntStatus = ${DMA_INSTANCE_NAME}_REGS->XDMAC_CHID[channel].XDMAC_CIS;

            if ((chanIntStatus & ( XDMAC_CIS_RBEIS_Msk | XDMAC_CIS_WBEIS_Msk | XDMAC_CIS_ROIS_Msk)) != 0U)
            {
                xdmacChObj->busyStatus = false;

                /* It's an error interrupt */
                if (NULL != xdmacChObj->callback)
                {
                    xdmacChObj->callback(XDMAC_TRANSFER_ERROR, xdmacChObj->context);
                }
            }
            else if ((chanIntStatus & XDMAC_CIS_BIS_Msk) != 0U)
            {
                xdmacChObj->busyStatus = false;

                /* It's a block transfer complete interrupt */
                if (NULL != xdmacChObj->callback)
                {
                    xdmacChObj->callback(XDMAC_TRANSFER_COMPLETE, xdmacChObj->context);
                }
            }
            else
            {
                /* Nothing to do */
            }
        }

        /* Point to next channel object */
        xdmacChObj++;
    }
}
</#if>
</#if>

void ${DMA_INSTANCE_NAME}_Initialize( void )
{
    XDMAC_CH_OBJECT *xdmacChObj = (XDMAC_CH_OBJECT *)&xdmacChannelObj[0];
    uint8_t channel = 0U;

    /* Initialize channel objects */
    for(channel = 0U; channel < XDMAC_ACTIVE_CHANNELS_MAX; channel++)
    {
        xdmacChObj->inUse = 0U;
<#if XDMAC_INTERRUPT_ENABLED == true>
        xdmacChObj->callback = NULL;
</#if>
        xdmacChObj->context = 0U;
        xdmacChObj->busyStatus = false;
        /* Point to next channel object */
        xdmacChObj++;
    }

    <#list 0..DMA_CHANNEL_COUNT as i>
    <#assign XDMAC_CH_ENABLE = "XDMAC_CH" + i + "_ENABLE">
    <#assign XDMAC_CC_TYPE = "XDMAC_CC" + i + "_TYPE">
    <#assign XDMAC_CC_DSYNC = "XDMAC_CC" + i + "_DSYNC">
    <#assign XDMAC_CC_PROT = "XDMAC_CC" + i + "_PROT">
    <#assign XDMAC_CC_SWREQ = "XDMAC_CC" + i + "_SWREQ">
    <#assign XDMAC_CC_DAM = "XDMAC_CC" + i + "_DAM">
    <#assign XDMAC_CC_SAM = "XDMAC_CC" + i + "_SAM">
    <#assign XDMAC_CC_SIF = "XDMAC_CC" + i + "_SIF">
    <#assign XDMAC_CC_DIF = "XDMAC_CC" + i + "_DIF">
    <#assign XDMAC_CC_DWIDTH = "XDMAC_CC" + i + "_DWIDTH">
    <#assign XDMAC_CC_CSIZE = "XDMAC_CC" + i + "_CSIZE">
    <#assign XDMAC_CC_MBSIZE = "XDMAC_CC" + i + "_MBSIZE">
    <#assign XDMAC_CC_PERID_VAL = "XDMAC_CC" + i + "_PERID_VAL">
    <#assign XDMAC_INT_ENABLE = "XDMAC_CH" + i + "_ENABLE_INTERRUPT">
        <#if .vars[XDMAC_CH_ENABLE]?has_content>
            <#if (.vars[XDMAC_CH_ENABLE] != false)>
    /* Configure Channel ${i} */
                <#if .vars[XDMAC_CC_TYPE]?has_content>
                    <#if (.vars[XDMAC_CC_TYPE] == "PER_TRAN")>
    ${DMA_INSTANCE_NAME}_REGS->XDMAC_CHID[${i}].XDMAC_CC =  (XDMAC_CC_TYPE_${.vars[XDMAC_CC_TYPE]} |
                                            XDMAC_CC_PERID(${.vars[XDMAC_CC_PERID_VAL]}U) |
                                            XDMAC_CC_DSYNC_${.vars[XDMAC_CC_DSYNC]} |
<#if .vars[XDMAC_CC_PROT]??>
                                            XDMAC_CC_PROT_${.vars[XDMAC_CC_PROT]} |
</#if>
                                            XDMAC_CC_SWREQ_${.vars[XDMAC_CC_SWREQ]} |
                                            XDMAC_CC_DAM_${.vars[XDMAC_CC_DAM]} |
                                            XDMAC_CC_SAM_${.vars[XDMAC_CC_SAM]} |
<#if .vars[XDMAC_CC_SIF]??>
                                            XDMAC_CC_SIF_${.vars[XDMAC_CC_SIF]} |
</#if>
<#if .vars[XDMAC_CC_DIF]??>
                                            XDMAC_CC_DIF_${.vars[XDMAC_CC_DIF]} |
</#if>
                                            XDMAC_CC_DWIDTH_${.vars[XDMAC_CC_DWIDTH]} |
                                            XDMAC_CC_CSIZE_${.vars[XDMAC_CC_CSIZE]} |\
                                            XDMAC_CC_MBSIZE_${.vars[XDMAC_CC_MBSIZE]});
                    <#elseif (.vars[XDMAC_CC_TYPE] == "MEM_TRAN")>
    ${DMA_INSTANCE_NAME}_REGS->XDMAC_CHID[${i}].XDMAC_CC =  (XDMAC_CC_TYPE_${.vars[XDMAC_CC_TYPE]} |
<#if .vars[XDMAC_CC_PROT]??>
                                            XDMAC_CC_PROT_${.vars[XDMAC_CC_PROT]} |
</#if>
                                            XDMAC_CC_DAM_${.vars[XDMAC_CC_DAM]} |
                                            XDMAC_CC_SAM_${.vars[XDMAC_CC_SAM]} |
<#if .vars[XDMAC_CC_SIF]??>
                                            XDMAC_CC_SIF_${.vars[XDMAC_CC_SIF]} |
</#if>
<#if .vars[XDMAC_CC_DIF]??>
                                            XDMAC_CC_DIF_${.vars[XDMAC_CC_DIF]} |
</#if>
                                            XDMAC_CC_DWIDTH_${.vars[XDMAC_CC_DWIDTH]} |
                                            XDMAC_CC_MBSIZE_${.vars[XDMAC_CC_MBSIZE]});
</#if>
</#if>
    ${DMA_INSTANCE_NAME}_REGS->XDMAC_CHID[${i}].XDMAC_CIE= (XDMAC_CIE_BIE_Msk | XDMAC_CIE_RBIE_Msk | XDMAC_CIE_WBIE_Msk | XDMAC_CIE_ROIE_Msk);
<#if .vars[XDMAC_INT_ENABLE] == true>
    ${DMA_INSTANCE_NAME}_REGS->XDMAC_GIE= (XDMAC_GIE_IE0_Msk << ${i});
</#if>
    xdmacChannelObj[${i}].inUse = 1U;
<#if SECURE_INTERRUPT_AVAILABLE>
    xdmacChannelObj[${i}].isSecure = ${(.vars[XDMAC_CC_PROT] == "SEC")?string("true", "false")};
</#if>
</#if>
</#if>
</#list>
    return;
}

<#if XDMAC_INTERRUPT_ENABLED == true>
void ${DMA_INSTANCE_NAME}_ChannelCallbackRegister( XDMAC_CHANNEL channel, const XDMAC_CHANNEL_CALLBACK eventHandler, const uintptr_t contextHandle )
{
    xdmacChannelObj[channel].callback = eventHandler;
    xdmacChannelObj[channel].context = contextHandle;

    return;
}
</#if>

bool ${DMA_INSTANCE_NAME}_ChannelTransfer( XDMAC_CHANNEL channel, const void *srcAddr, const void *destAddr, size_t blockSize )
{
    volatile uint32_t status = 0U;
    bool returnStatus = false;
    const uint32_t *psrcAddr =   (const uint32_t *)srcAddr;
    const uint32_t *pdestAddr =  (const uint32_t *)destAddr;


    if ((xdmacChannelObj[channel].busyStatus == false) || ((${DMA_INSTANCE_NAME}_REGS->XDMAC_GS & (XDMAC_GS_ST0_Msk << (uint32_t)channel)) == 0U))
    {
        /* Clear channel level status before adding transfer parameters */
        status = ${DMA_INSTANCE_NAME}_REGS->XDMAC_CHID[channel].XDMAC_CIS;
        (void)status;

        xdmacChannelObj[channel].busyStatus = true;

        /*Set source address */
        ${DMA_INSTANCE_NAME}_REGS->XDMAC_CHID[channel].XDMAC_CSA= (uint32_t)psrcAddr;

        /* Set destination address */
        ${DMA_INSTANCE_NAME}_REGS->XDMAC_CHID[channel].XDMAC_CDA= (uint32_t)pdestAddr;

        /* Set block size */
        ${DMA_INSTANCE_NAME}_REGS->XDMAC_CHID[channel].XDMAC_CUBC= XDMAC_CUBC_UBLEN(blockSize);

        /* Make sure all memory transfers are completed before enabling the DMA */
        __DMB();

        /* Enable the channel */
        ${DMA_INSTANCE_NAME}_REGS->XDMAC_GE= (XDMAC_GE_EN0_Msk << (uint32_t)channel);

        returnStatus = true;
    }

    return returnStatus;
}
<#if XDMAC_LL_ENABLE == true>

bool ${DMA_INSTANCE_NAME}_ChannelLinkedListTransfer (XDMAC_CHANNEL channel, uint32_t firstDescriptorAddress, XDMAC_DESCRIPTOR_CONTROL* firstDescriptorControl)
{
    volatile uint32_t status = 0U;
    bool returnStatus = false;

    if ((xdmacChannelObj[channel].busyStatus == false) || ((${DMA_INSTANCE_NAME}_REGS->XDMAC_GS & (XDMAC_GS_ST0_Msk << (uint32_t)channel)) == 0U))
    {
        /* Clear channel level status before adding transfer parameters */
        status = ${DMA_INSTANCE_NAME}_REGS->XDMAC_CHID[channel].XDMAC_CIS;
        (void)status;

        xdmacChannelObj[channel].busyStatus = true;

        /* First descriptor control set */
        ${DMA_INSTANCE_NAME}_REGS->XDMAC_CHID[channel].XDMAC_CNDC= (uint32_t)(firstDescriptorControl->descriptorControl);

        /* First descriptor address set */
        ${DMA_INSTANCE_NAME}_REGS->XDMAC_CHID[channel].XDMAC_CNDA= ( (firstDescriptorAddress & XDMAC_CNDA_NDA_Msk) | XDMAC_CNDA_NDAIF_Msk ) ;

        /* Enable end of linked list interrupt source */
        ${DMA_INSTANCE_NAME}_REGS->XDMAC_CHID[channel].XDMAC_CIE= XDMAC_CIE_LIE_Msk ;

        /* Enable the channel */
        ${DMA_INSTANCE_NAME}_REGS->XDMAC_GE= (XDMAC_GE_EN0_Msk << (uint32_t)channel);

        returnStatus = true;
    }

    return returnStatus;
}
</#if>

bool ${DMA_INSTANCE_NAME}_ChannelIsBusy (XDMAC_CHANNEL channel)
{
    return((xdmacChannelObj[channel].busyStatus == true) && ((${DMA_INSTANCE_NAME}_REGS->XDMAC_GS & (XDMAC_GS_ST0_Msk << (uint32_t)channel)) != 0U));
}

XDMAC_TRANSFER_EVENT ${DMA_INSTANCE_NAME}_ChannelTransferStatusGet(XDMAC_CHANNEL channel)
{
    uint32_t chanIntStatus;

    XDMAC_TRANSFER_EVENT xdmacTransferStatus = XDMAC_TRANSFER_NONE;

    /* Read the interrupt status for the requested DMA channel */
    chanIntStatus = ${DMA_INSTANCE_NAME}_REGS->XDMAC_CHID[channel].XDMAC_CIS;

    if ((chanIntStatus & ( XDMAC_CIS_RBEIS_Msk | XDMAC_CIS_WBEIS_Msk | XDMAC_CIS_ROIS_Msk)) != 0U)
    {
        xdmacTransferStatus = XDMAC_TRANSFER_ERROR;
    }
    else if ((chanIntStatus & XDMAC_CIS_BIS_Msk) != 0U)
    {
        xdmacTransferStatus = XDMAC_TRANSFER_COMPLETE;
    }
    else
    {
        ; /* No action required - ; is optional */
    }
    return xdmacTransferStatus;
}

void ${DMA_INSTANCE_NAME}_ChannelDisable (XDMAC_CHANNEL channel)
{
    /* Disable the channel */
    ${DMA_INSTANCE_NAME}_REGS->XDMAC_GD = (XDMAC_GD_DI0_Msk << (uint32_t)channel);
    xdmacChannelObj[channel].busyStatus = false;
    return;
}

XDMAC_CHANNEL_CONFIG ${DMA_INSTANCE_NAME}_ChannelSettingsGet (XDMAC_CHANNEL channel)
{
    return (XDMAC_CHANNEL_CONFIG)${DMA_INSTANCE_NAME}_REGS->XDMAC_CHID[channel].XDMAC_CC;
}

bool ${DMA_INSTANCE_NAME}_ChannelSettingsSet (XDMAC_CHANNEL channel, XDMAC_CHANNEL_CONFIG setting)
{
    /* Disable the channel */
    ${DMA_INSTANCE_NAME}_REGS->XDMAC_GD= (XDMAC_GD_DI0_Msk << (uint32_t)channel);

    /* Set the new settings */
    ${DMA_INSTANCE_NAME}_REGS->XDMAC_CHID[channel].XDMAC_CC= setting;

    return true;
}

void ${DMA_INSTANCE_NAME}_ChannelBlockLengthSet (XDMAC_CHANNEL channel, uint16_t length)
{
    /* Disable the channel */
    ${DMA_INSTANCE_NAME}_REGS->XDMAC_GD= (XDMAC_GD_DI0_Msk << (uint32_t)channel);

    ${DMA_INSTANCE_NAME}_REGS->XDMAC_CHID[channel].XDMAC_CBC = length;
}

void ${DMA_INSTANCE_NAME}_ChannelSuspend (XDMAC_CHANNEL channel)
{
    /* Suspend the channel */
    ${DMA_INSTANCE_NAME}_REGS->XDMAC_GRWS = (XDMAC_GRWS_RWS0_Msk << (uint32_t)channel);
}

void ${DMA_INSTANCE_NAME}_ChannelResume (XDMAC_CHANNEL channel)
{
    /* Resume the channel */
    ${DMA_INSTANCE_NAME}_REGS->XDMAC_GRWR = (XDMAC_GRWR_RWR0_Msk << (uint32_t)channel);
}
