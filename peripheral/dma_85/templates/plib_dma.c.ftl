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
* Copyright (C) 2022 Microchip Technology Inc. and its subsidiaries.
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
<#if DMA_LOW_LEVEL_API_ONLY == false>
#include "../ecia/plib_ecia.h"


// *****************************************************************************
// *****************************************************************************
// Section: Global Data
// *****************************************************************************
// *****************************************************************************

#define DMA_CHANNELS_NUMBER        (${DMA_HIGHEST_CHANNEL}U)


/* DMA channels object configuration structure */
typedef struct
{
    DMA_CHANNEL_CALLBACK  callback;
    uintptr_t             context;
    bool                  busyStatus;
    uint32_t              mstartAddr;
} DMA_CH_OBJECT ;

/* DMA Channels object information structure */
static DMA_CH_OBJECT dmaChannelObj[DMA_CHANNELS_NUMBER];
</#if>

#define NOP()    asm("NOP")

static dma_chan00_registers_t* ${DMA_INSTANCE_NAME}_ChannelBaseAddrGet(DMA_CHANNEL ch)
{
    return (dma_chan00_registers_t*)(DMA_CHAN00_BASE_ADDRESS + ((uint32_t)ch * 64U));
}

void ${DMA_INSTANCE_NAME}_Initialize( void )
{
    dma_chan00_registers_t* dmaChRegs;

<#if DMA_LOW_LEVEL_API_ONLY == false>
    /* Initialize DMA Channel objects */
    for(uint32_t channel = 0U; channel < DMA_CHANNELS_NUMBER; channel++)
    {
        dmaChannelObj[channel].callback = NULL;
        dmaChannelObj[channel].context = 0U;
        dmaChannelObj[channel].busyStatus = false;
    }
</#if>

    /* Reset DMA module */
    DMA_MAIN_REGS->DMA_MAIN_ACTRST = DMA_MAIN_ACTRST_SOFT_RST_Msk;

    <#list 0..DMA_HIGHEST_CHANNEL - 1 as i>
        <#assign DMA_CHX_ENABLE             = "DMA_ENABLE_CH_" + i>
        <#assign DMA_ENABLE_HW_FLOW_CTRL    = "DMA_ENABLE_HW_FLOW_CTRL_CH_" + i>
        <#assign DMA_CHX_HW_FLOW_CTRL_DEV   = "DMA_HW_FLOW_CTRL_DEV_CH_" + i>
        <#assign DMA_CHX_TRANS_SIZE         = "DMA_TRANS_SIZE_CH_" + i>
        <#assign DMA_CHX_DEV_ADDR_INC       = "DMA_DEVICE_ADDR_INC_CH_" + i>
        <#assign DMA_CHX_MEM_ADDR_INC       = "DMA_MEMORY_ADDR_INC_CH_" + i>
        <#assign DMA_TRANFER_DIR            = "DMA_TRANFER_DIR_CH_" + i>
        <#if (.vars[DMA_CHX_ENABLE] == true)>
        <#lt>   /***************** Configure DMA channel ${i} ********************/
        <#lt>   dmaChRegs = ${DMA_INSTANCE_NAME}_ChannelBaseAddrGet(DMA_CHANNEL_${i});

        <#lt>   <@compress single_line=true>dmaChRegs->DMA_CHAN00_CTRL = DMA_CHAN00_CTRL_TX_DIR(${.vars[DMA_TRANFER_DIR]}) | <#if .vars[DMA_ENABLE_HW_FLOW_CTRL] == true> DMA_CHAN00_CTRL_DIS_HW_FLOW_CTRL(0) | DMA_CHAN00_CTRL_HW_FLOW_CTRL_DEV(${.vars[DMA_CHX_HW_FLOW_CTRL_DEV]}) <#else> DMA_CHAN00_CTRL_DIS_HW_FLOW_CTRL(1) </#if> | DMA_CHAN00_CTRL_TRANS_SIZE(${.vars[DMA_CHX_TRANS_SIZE]}) | DMA_CHAN00_CTRL_INC_DEV_ADDR(${.vars[DMA_CHX_DEV_ADDR_INC]?c}) | DMA_CHAN00_CTRL_INC_MEM_ADDR(${.vars[DMA_CHX_MEM_ADDR_INC]?c});</@compress>
        <#if i == 0 && DMA_CRC_ENABLE_CH_0 == true>
        <#lt>   dmaChRegs->DMA_CHAN00_CRC_EN |= DMA_CHAN00_CRC_EN_MODE_Msk;
        </#if>
        <#if i == 1 && DMA_FILL_ENABLE_CH_1 == true>
        <#lt>   DMA_CHAN01_REGS->DMA_CHAN01_FILL_EN |= DMA_CHAN01_FILL_EN_MODE_Msk;
        </#if>
        <#lt>   dmaChRegs->DMA_CHAN00_ACTIVATE = DMA_CHAN00_ACTIVATE_CHN_Msk;

        </#if>
    </#list>

    /* Global enable */
    DMA_MAIN_REGS->DMA_MAIN_ACTRST = DMA_MAIN_ACTRST_ACT_Msk;
}

<#if DMA_LOW_LEVEL_API_ONLY == false>
bool ${DMA_INSTANCE_NAME}_ChannelTransfer( DMA_CHANNEL channel, const void *srcAddr, const void *destAddr, size_t blockSize )
{
    bool returnStatus = false;
    dma_chan00_registers_t* dmaChRegs = ${DMA_INSTANCE_NAME}_ChannelBaseAddrGet(channel);

    uint32_t src_addr = (uint32_t)((const uint32_t*)srcAddr);
    uint32_t dst_addr = (uint32_t)((const uint32_t*)destAddr);
    uint32_t transferDir = ((src_addr & EC_DEVICE_REGISTERS_ADDR) != 0U)? 0U:1U;


    if (dmaChannelObj[channel].busyStatus == false)
    {
        dmaChannelObj[channel].busyStatus = true;

        /* Activate channel */
        dmaChRegs->DMA_CHAN00_ACTIVATE |= DMA_CHAN00_ACTIVATE_CHN_Msk;

        if (transferDir == 0U)
        {
            /* Peripheral to memory transfer */
            dmaChRegs->DMA_CHAN00_DSTART = src_addr;
            dmaChRegs->DMA_CHAN00_MSTART = dst_addr;
            dmaChRegs->DMA_CHAN00_MEND = (uint32_t)(dst_addr + blockSize);
        }
        else
        {
            /* Memory to peripheral transfer */
            dmaChRegs->DMA_CHAN00_DSTART = dst_addr;
            dmaChRegs->DMA_CHAN00_MSTART = src_addr;
            dmaChRegs->DMA_CHAN00_MEND = (uint32_t)(src_addr + blockSize);
        }

        dmaChannelObj[channel].mstartAddr = dmaChRegs->DMA_CHAN00_MSTART;

        /* Set the transfer direction */
        dmaChRegs->DMA_CHAN00_CTRL = (dmaChRegs->DMA_CHAN00_CTRL & ~DMA_CHAN00_CTRL_TX_DIR_Msk) | (transferDir << DMA_CHAN00_CTRL_TX_DIR_Pos);

        if ((uint32_t)channel == 0U)
        {
            /* If CRC is enabled, initialize the CRC generator */
            if ((dmaChRegs->DMA_CHAN00_CRC_EN & DMA_CHAN00_CRC_EN_MODE_Msk) != 0U)
            {
                dmaChRegs->DMA_CHAN00_CRC_DATA = 0xFFFFFFFFU;
            }
        }

        /* Enable transfer done and bus error interrupts */
        dmaChRegs->DMA_CHAN00_IEN = (DMA_CHAN00_IEN_STS_EN_DONE_Msk | DMA_CHAN00_IEN_STS_EN_BUS_ERR_Msk);

        /* Start the transfer, check if device is the DMA host or firmware is the DMA host */
        if ((dmaChRegs->DMA_CHAN00_CTRL & DMA_CHAN00_CTRL_DIS_HW_FLOW_CTRL_Msk) != 0U)
        {
            /* DMA controller is under the control of firmware (not the device host) */
            dmaChRegs->DMA_CHAN00_CTRL |= DMA_CHAN00_CTRL_TRANS_GO_Msk;
        }
        else
        {
            /* DMA controller is under the control of device */
            dmaChRegs->DMA_CHAN00_CTRL |= DMA_CHAN00_CTRL_RUN_Msk;
        }

        returnStatus = true;
    }

    return returnStatus;
}

void ${DMA_INSTANCE_NAME}_ChannelCallbackRegister( DMA_CHANNEL channel, const DMA_CHANNEL_CALLBACK callback, const uintptr_t context )
{
    dmaChannelObj[channel].callback = callback;
    dmaChannelObj[channel].context  = context;
}

bool ${DMA_INSTANCE_NAME}_ChannelIsBusy ( DMA_CHANNEL channel )
{
    return (dmaChannelObj[channel].busyStatus);
}

void ${DMA_INSTANCE_NAME}_ChannelEnable ( DMA_CHANNEL channel )
{
    dma_chan00_registers_t* dmaChRegs = ${DMA_INSTANCE_NAME}_ChannelBaseAddrGet(channel);

    /* Activate the DMA channel */
    dmaChRegs->DMA_CHAN00_ACTIVATE |= DMA_CHAN00_ACTIVATE_CHN_Msk;
}

void ${DMA_INSTANCE_NAME}_ChannelDisable ( DMA_CHANNEL channel )
{
    dma_chan00_registers_t* dmaChRegs = ${DMA_INSTANCE_NAME}_ChannelBaseAddrGet(channel);

    dmaChRegs->DMA_CHAN00_ACTIVATE &= ~DMA_CHAN00_ACTIVATE_CHN_Msk;

    dmaChannelObj[channel].busyStatus=false;
}

void ${DMA_INSTANCE_NAME}_ChannelTransferAbort ( DMA_CHANNEL channel )
{
    dma_chan00_registers_t* dmaChRegs = ${DMA_INSTANCE_NAME}_ChannelBaseAddrGet(channel);

    dmaChRegs->DMA_CHAN00_CTRL |= DMA_CHAN00_CTRL_TRANS_ABORT_Msk;

    NOP();NOP();NOP();NOP();NOP();NOP();

    dmaChRegs->DMA_CHAN00_CTRL &= ~DMA_CHAN00_CTRL_TRANS_ABORT_Msk;

    dmaChannelObj[channel].busyStatus=false;
}

uint32_t ${DMA_INSTANCE_NAME}_ChannelGetTransferredCount( DMA_CHANNEL channel )
{
    dma_chan00_registers_t* dmaChRegs = ${DMA_INSTANCE_NAME}_ChannelBaseAddrGet(channel);

    uint32_t transferWidth = (dmaChRegs->DMA_CHAN00_CTRL & DMA_CHAN00_CTRL_TRANS_SIZE_Msk) >> DMA_CHAN00_CTRL_TRANS_SIZE_Pos;

    return ((dmaChRegs->DMA_CHAN00_MSTART - dmaChannelObj[channel].mstartAddr)/transferWidth);
}

void ${DMA_INSTANCE_NAME}_ChannelInterruptEnable ( DMA_CHANNEL channel, DMA_INT intSources )
{
    dma_chan00_registers_t* dmaChRegs = ${DMA_INSTANCE_NAME}_ChannelBaseAddrGet(channel);

    /* Enable transfer done and bus error interrupts */
    dmaChRegs->DMA_CHAN00_IEN |= intSources;
}

void ${DMA_INSTANCE_NAME}_ChannelInterruptDisable ( DMA_CHANNEL channel, DMA_INT intSources )
{
    dma_chan00_registers_t* dmaChRegs = ${DMA_INSTANCE_NAME}_ChannelBaseAddrGet(channel);

    /* Enable transfer done and bus error interrupts */
    dmaChRegs->DMA_CHAN00_IEN &= ~(intSources);
}

DMA_INT ${DMA_INSTANCE_NAME}_ChannelInterruptFlagsGet ( DMA_CHANNEL channel )
{
    dma_chan00_registers_t* dmaChRegs = ${DMA_INSTANCE_NAME}_ChannelBaseAddrGet(channel);

    return (dmaChRegs->DMA_CHAN00_ISTS & DMA_CHAN00_ISTS_Msk);
}

DMA_CHANNEL_CONFIG ${DMA_INSTANCE_NAME}_ChannelSettingsGet (DMA_CHANNEL channel)
{
    dma_chan00_registers_t* dmaChRegs = ${DMA_INSTANCE_NAME}_ChannelBaseAddrGet(channel);

    return dmaChRegs->DMA_CHAN00_CTRL;
}

bool ${DMA_INSTANCE_NAME}_ChannelSettingsSet (DMA_CHANNEL channel, DMA_CHANNEL_CONFIG setting)
{
    dma_chan00_registers_t* dmaChRegs = ${DMA_INSTANCE_NAME}_ChannelBaseAddrGet(channel);

    dmaChRegs->DMA_CHAN00_CTRL = setting;

    return true;
}

<#if DMA_CRC_ENABLE_CH_0 == true>
void ${DMA_INSTANCE_NAME}_CRCEnable( void )
{
    dma_chan00_registers_t* dmaChRegs = ${DMA_INSTANCE_NAME}_ChannelBaseAddrGet(0);

    dmaChRegs->DMA_CHAN00_CRC_EN |= DMA_CHAN00_CRC_EN_MODE_Msk;
}

void ${DMA_INSTANCE_NAME}_CRCDisable( void )
{
    dma_chan00_registers_t* dmaChRegs = ${DMA_INSTANCE_NAME}_ChannelBaseAddrGet(0);

    dmaChRegs->DMA_CHAN00_CRC_EN &= ~DMA_CHAN00_CRC_EN_MODE_Msk;
}

uint32_t ${DMA_INSTANCE_NAME}_CRCRead( void )
{
    dma_chan00_registers_t* dmaChRegs = ${DMA_INSTANCE_NAME}_ChannelBaseAddrGet(0);

    return dmaChRegs->DMA_CHAN00_CRC_DATA;
}
</#if>

<#if DMA_FILL_ENABLE_CH_1 == true>
void ${DMA_INSTANCE_NAME}_FillDataSet( uint32_t fillData )
{
    DMA_CHAN01_REGS->DMA_CHAN01_FILL_DATA = fillData;
}
</#if>

static void DMA_interruptHandler(DMA_CHANNEL channel)
{
    DMA_CH_OBJECT  *dmacChObj = NULL;
    volatile uint8_t chIntFlagStatus = 0U;

    DMA_TRANSFER_EVENT event = 0U;

    dmacChObj = (DMA_CH_OBJECT *)&dmaChannelObj[channel];

    dma_chan00_registers_t* dmaChRegs = ${DMA_INSTANCE_NAME}_ChannelBaseAddrGet(channel);

    /* Get the DMA channel interrupt flag status */
    chIntFlagStatus = dmaChRegs->DMA_CHAN00_ISTS;

    if (((chIntFlagStatus & DMA_CHAN00_ISTS_DONE_Msk) != 0U) && ((dmaChRegs->DMA_CHAN00_IEN & DMA_CHAN00_IEN_STS_EN_DONE_Msk) != 0U))
    {
        event = DMA_TRANSFER_EVENT_COMPLETE;
    }
    else if (((chIntFlagStatus & DMA_CHAN00_ISTS_BUS_ERR_Msk) != 0U) && ((dmaChRegs->DMA_CHAN00_IEN & DMA_CHAN00_IEN_STS_EN_BUS_ERR_Msk) != 0U))
    {
        event = DMA_TRANSFER_EVENT_ERROR;
    }
    else
    {
        /* Do nothing */
    }

    /* Clear the interrupt status flags (Write 1 to clear) */
    dmaChRegs->DMA_CHAN00_ISTS = chIntFlagStatus;

    dmaChannelObj[channel].busyStatus=false;

    /* Execute the callback function */
    if ((dmacChObj->callback != NULL) && ((uint32_t)event != 0U))
    {
        dmacChObj->callback (event, dmacChObj->context);
    }
}

<#list 0..DMA_HIGHEST_CHANNEL - 1 as i>
<#assign DMA_CHX_ENABLE = "DMA_ENABLE_CH_" + i>
<#if (.vars[DMA_CHX_ENABLE] == true)>
<#if DMA_INTERRUPT_TYPE == "AGGREGATE">
<#assign DMA_CHX_INTERRUPT_NAME = "DMA_CH" + i?string["00"] + "_GRP">
<#assign DMA_CHX_INT_SRC_NAME = "ECIA_AGG_INT_SRC_DMA_CH" + i?string["00"]>
<#else>
<#assign DMA_CHX_INTERRUPT_NAME = "DMA_CH" + i?string["00"]>
<#assign DMA_CHX_INT_SRC_NAME = "ECIA_DIR_INT_SRC_DMA_CH" + i?string["00"]>
</#if>
void ${DMA_CHX_INTERRUPT_NAME}_InterruptHandler( void )
{
    if (ECIA_GIRQResultGet(${DMA_CHX_INT_SRC_NAME}))
    {
        ECIA_GIRQSourceClear(${DMA_CHX_INT_SRC_NAME});
        DMA_interruptHandler(DMA_CHANNEL_${i});
    }
}
</#if>
</#list>

<#else>

void ${DMA_INSTANCE_NAME}_MemIncrCfg(DMA_CHANNEL channel, uint8_t mem_incr_sts)
{
    dma_chan00_registers_t* dmaChRegs = ${DMA_INSTANCE_NAME}_ChannelBaseAddrGet(channel);

    dmaChRegs->DMA_CHAN00_CTRL = DMA_CHAN00_CTRL_INC_MEM_ADDR((bool)mem_incr_sts);
}

void ${DMA_INSTANCE_NAME}_ChannelAbort(DMA_CHANNEL channel)
{
    dma_chan00_registers_t* dmaChRegs = ${DMA_INSTANCE_NAME}_ChannelBaseAddrGet(channel);

    dmaChRegs->DMA_CHAN00_CTRL |= DMA_CHAN00_CTRL_TRANS_ABORT_Msk;

    NOP();NOP();NOP();NOP();NOP();NOP();

    dmaChRegs->DMA_CHAN00_CTRL &= ~DMA_CHAN00_CTRL_TRANS_ABORT_Msk;
}

void ${DMA_INSTANCE_NAME}_Activate(uint8_t activate)
{
    DMA_MAIN_REGS->DMA_MAIN_ACTRST |= activate;
}

void ${DMA_INSTANCE_NAME}_SoftReset(void)
{
    /* soft reset DMA */
    DMA_MAIN_REGS->DMA_MAIN_ACTRST |= DMA_MAIN_ACTRST_SOFT_RST_Msk;
    DMA_MAIN_REGS->DMA_MAIN_ACTRST |= DMA_MAIN_ACTRST_ACT_Msk;
}

void ${DMA_INSTANCE_NAME}_Enable(void)
{
    DMA_MAIN_REGS->DMA_MAIN_ACTRST |= DMA_MAIN_ACTRST_ACT_Msk;
}

void ${DMA_INSTANCE_NAME}_Disable(void)
{
    DMA_MAIN_REGS->DMA_MAIN_ACTRST &= ~DMA_MAIN_ACTRST_ACT_Msk;
}

void ${DMA_INSTANCE_NAME}_ChannelActivate(DMA_CHANNEL channel)
{
    dma_chan00_registers_t* dmaChRegs = ${DMA_INSTANCE_NAME}_ChannelBaseAddrGet(channel);
    dmaChRegs->DMA_CHAN00_ACTIVATE |= DMA_CHAN00_ACTIVATE_CHN_Msk;
}/* HW_DMA::activate */

/******************************************************************************/
/** HW_DMA::deactivate function.
 * This function clears the ACTIVATE bit
 * @param None
 * @return None
*******************************************************************************/
void ${DMA_INSTANCE_NAME}_ChannelDeactivate(DMA_CHANNEL channel)
{
    dma_chan00_registers_t* dmaChRegs = ${DMA_INSTANCE_NAME}_ChannelBaseAddrGet(channel);
    dmaChRegs->DMA_CHAN00_ACTIVATE &= ~DMA_CHAN00_ACTIVATE_CHN_Msk;
}/* HW_DMA::deactivate */

/******************************************************************************/
/** HW_DMA::stop function.
 * This function clears the RUN bit
 * @param None
 * @return None
*******************************************************************************/
void ${DMA_INSTANCE_NAME}_Stop(DMA_CHANNEL channel)
{
    dma_chan00_registers_t* dmaChRegs = ${DMA_INSTANCE_NAME}_ChannelBaseAddrGet(channel);
    dmaChRegs->DMA_CHAN00_CTRL &= ~DMA_CHAN00_CTRL_RUN_Msk;
}/* HW_DMA::stop */

/******************************************************************************/
/** HW_DMA::start function.
 * This function sets the RUN bit
 * @param None
 * @return None
*******************************************************************************/
void ${DMA_INSTANCE_NAME}_Start(DMA_CHANNEL channel)
{
    dma_chan00_registers_t* dmaChRegs = ${DMA_INSTANCE_NAME}_ChannelBaseAddrGet(channel);
    dmaChRegs->DMA_CHAN00_CTRL |= DMA_CHAN00_CTRL_RUN_Msk;
}/* HW_DMA::start */

uint8_t ${DMA_INSTANCE_NAME}_WaitTillFree(DMA_CHANNEL channel)
{
    uint32_t timeoutCounter=0;
    uint8_t retVal = 1;
    dma_chan00_registers_t* dmaChRegs = ${DMA_INSTANCE_NAME}_ChannelBaseAddrGet(channel);

    while((dmaChRegs->DMA_CHAN00_CTRL & DMA_CHAN00_CTRL_BUSY_Msk) != 0U)
    {
        if (timeoutCounter++ >= BUSY_TIMEOUT_COUNTER)
        {
            retVal = 0;
            break;
        }
    }
    return retVal;
}/* HW_DMA::wait_till_free */

void ${DMA_INSTANCE_NAME}_SetupTx(DMA_CHANNEL channel, const uint8_t device, const uint32_t dataAHBAddress, uint32_t dma_buffer_tx, const uint8_t transfer_bytes_count)
{
    /* Set the activate bit for the channel to operate */
    /* Activate bit is used to activate the dma device for the particular channel.
       It is relevant when setup_tx is called for the first time and
       the channel is not activated */

    dma_chan00_registers_t* dmaChRegs = ${DMA_INSTANCE_NAME}_ChannelBaseAddrGet(channel);

    ${DMA_INSTANCE_NAME}_ChannelActivate(channel);

    DMA_MAIN_REGS->DMA_MAIN_ACTRST = DMA_MAIN_ACTRST_ACT_Msk;

    /* Stop the Tx DMA before configuring it*/
    ${DMA_INSTANCE_NAME}_Stop(channel);

    if (0U == ${DMA_INSTANCE_NAME}_WaitTillFree(channel))
    {
        /* This should never happen, the trace here
         * will help to detect this condition during testing */
    }

    dmaChRegs->DMA_CHAN00_DSTART  = dataAHBAddress;

    /* Set DMI Start Address Register to beginning of buffer */
    dmaChRegs->DMA_CHAN00_MSTART = ((uint32_t)dma_buffer_tx);

    /* Set DMI End Address Register */
    dmaChRegs->DMA_CHAN00_MEND = ((uint32_t)(dma_buffer_tx + transfer_bytes_count));

    /* select device,direction */
    dmaChRegs->DMA_CHAN00_CTRL = (uint32_t)(((uint32_t)device<<DMA_CHAN00_CTRL_HW_FLOW_CTRL_DEV_Pos) | DMA_CHAN00_CTRL_TX_DIR_Msk
                                     | DMA_CHAN00_CTRL_INC_MEM_ADDR_Msk | DMA_CHAN00_CTRL_TRANS_SIZE(1));
}
void ${DMA_INSTANCE_NAME}_SetupRx(DMA_CHANNEL channel, const uint8_t device, const uint32_t dataAHBAddress, uint32_t dma_buffer_rx, const uint8_t transfer_bytes_count, const bool incrMemAddrFlag)
{
    uint32_t control_reg_value;
    dma_chan00_registers_t* dmaChRegs = ${DMA_INSTANCE_NAME}_ChannelBaseAddrGet(channel);

    /* Set the activate bit for the channel to operate */
    ${DMA_INSTANCE_NAME}_ChannelActivate(channel);

    /* Stop the Rx DMA before configuring it*/
    ${DMA_INSTANCE_NAME}_Stop(channel);

    if (0U == ${DMA_INSTANCE_NAME}_WaitTillFree(channel))
    {
        /* This should never happen, the trace here
         * will help to detect this condition during testing */
    }

    /* Assign DMA AHB Address */
    dmaChRegs->DMA_CHAN00_DSTART  = dataAHBAddress;

    /* Set DMI Start Address Register to beginning of receive buffer */
    dmaChRegs->DMA_CHAN00_MSTART = ((uint32_t)dma_buffer_rx);

    /* Set DMI End Address Register */
    dmaChRegs->DMA_CHAN00_MEND = ((uint32_t)(dma_buffer_rx + transfer_bytes_count));

    control_reg_value = (uint32_t)(((uint32_t)device<<DMA_CHAN00_CTRL_HW_FLOW_CTRL_DEV_Pos) | DMA_CHAN00_CTRL_TRANS_SIZE(1));

    if (incrMemAddrFlag)
    {
        control_reg_value |= DMA_CHAN00_CTRL_INC_MEM_ADDR_Msk;
    }

    /* select device,direction */
    dmaChRegs->DMA_CHAN00_CTRL = control_reg_value;
}

void ${DMA_INSTANCE_NAME}_SwitchTxToRx(DMA_CHANNEL channel, const uint8_t device, const uint32_t dataAHBAddress)
{
    dma_chan00_registers_t* dmaChRegs = ${DMA_INSTANCE_NAME}_ChannelBaseAddrGet(channel);

    /* Stop the Rx DMA before configuring it*/
    ${DMA_INSTANCE_NAME}_Stop(channel);

    if (0U == ${DMA_INSTANCE_NAME}_WaitTillFree(channel))
    {
        /* This should never happen, the trace here
         * will help to detect this condition during testing */
    }

    /* Assign DMA AHB Address */
    dmaChRegs->DMA_CHAN00_DSTART  = dataAHBAddress;

    /* Reset the control reg to ensure that subsequent OR operations are
     * reflected correctly. Most relevant when DMA switches over from Tx to Rx
     * with DIR changing from 1 to 0*/
    dmaChRegs->DMA_CHAN00_CTRL = 0;

    /* select device,direction */
    dmaChRegs->DMA_CHAN00_CTRL = (uint32_t)(((uint32_t)device<<DMA_CHAN00_CTRL_HW_FLOW_CTRL_DEV_Pos) |
                      DMA_CHAN00_CTRL_INC_MEM_ADDR_Msk | DMA_CHAN00_CTRL_TRANS_SIZE(1));
}

uint8_t ${DMA_INSTANCE_NAME}_GetDeviceId(const uint8_t device_name, const uint8_t device_instance)
{
    uint8_t device_id = 0;

    switch (device_name)
    {
        case 0:
            device_id = (uint8_t)(2U * device_instance);
            break;

        case 1:
            device_id = 1U + (uint8_t)(2U * device_instance);
            break;

        case 2:
            device_id = 4U;
            break;

        default:
            /* invalid device name */
            break;
    }

    return device_id;
}

void ${DMA_INSTANCE_NAME}_EnableInterrupt(DMA_CHANNEL channel)
{
    dma_chan00_registers_t* dmaChRegs = ${DMA_INSTANCE_NAME}_ChannelBaseAddrGet(channel);

    dmaChRegs->DMA_CHAN00_ISTS = DMA_CHAN00_ISTS_DONE_Msk;
    dmaChRegs->DMA_CHAN00_IEN = DMA_CHAN00_IEN_STS_EN_DONE_Msk;
}
void ${DMA_INSTANCE_NAME}_DisableInterrupt(DMA_CHANNEL channel)
{
    dma_chan00_registers_t* dmaChRegs = ${DMA_INSTANCE_NAME}_ChannelBaseAddrGet(channel);

    dmaChRegs->DMA_CHAN00_ISTS = DMA_CHAN00_ISTS_DONE_Msk;
    dmaChRegs->DMA_CHAN00_IEN = 0;
}
</#if>