/*******************************************************************************
  ${SQI_INSTANCE_NAME} Peripheral Library Source File

  Company
    Microchip Technology Inc.

  File Name
    plib${SQI_INSTANCE_NAME?lower_case}.c

  Summary
    ${SQI_INSTANCE_NAME} peripheral library interface.

  Description

  Remarks:

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
<#if core.CoreSysIntFile == true>
#include "interrupts.h"
</#if>
#include "plib_${SQI_INSTANCE_NAME?lower_case}.h"

#define ${SQI_INSTANCE_NAME}_CFG_CHIP_SELECT         (${SQI_CSEN} << ${SQI_INSTANCE_NAME}CFG_CSEN_POSITION)

static SQI_EVENT_HANDLER ${SQI_INSTANCE_NAME}EventHandler = NULL;

static uintptr_t ${SQI_INSTANCE_NAME}Context = (uintptr_t)NULL;

void ${SQI_INSTANCE_NAME}_Initialize(void)
{
    // Reset and Disable SQI
    ${SQI_INSTANCE_NAME}_REGS->SQI_CTRLA =  SQI_CTRLA_SWRST_Msk <#if SQI_RUN_STANDBY == true> | SQI_CTRLA_RUNSTDBY_Msk </#if> ;

    while((${SQI_INSTANCE_NAME}_REGS->SQI_SYNCBUSY & SQI_SYNCBUSY_SWRST_Msk) == SQI_SYNCBUSY_SWRST_Msk)
    {
        //wait for synchronization
    }

    // Set Config Register values
    ${SQI_INSTANCE_NAME}_REGS->SQI_CFG =  SQI_CFG_MODE(0x02U)  | SQI_CFG_BURSTEN_Msk |
           <#lt>                SQI_CFG_DATAEN(${SQI_LANE_MODE}U) | SQI_CFG_CSEN(${SQI_CSEN}U) <#if SQI_LSBF =="LSB"> | SQI_CFG_LSBF_Msk </#if> <#if SQI_CPOL=="HIGH"> | SQI_CFG_CPOL_Msk </#if> <#if SQI_CPHA=="TRAILING"> | SQI_CFG_CPHA_Msk </#if>;

     // SQICLK configuration
    ${SQI_INSTANCE_NAME}_REGS->SQI_CLKCON      = SQI_CLKCON_EN_Msk;              // Enable Clock

    while ((${SQI_INSTANCE_NAME}_REGS->SQI_CLKCON & SQI_CLKCON_STABLE_Msk) == 0U)
    {
        // Wait for clock to become stable
    }

    ${SQI_INSTANCE_NAME}_REGS->SQI_CLKCON      |= SQI_CLKCON_CLKDIV(${SQI_CLKDIV}U);

    // Enable the SQI Module
    ${SQI_INSTANCE_NAME}_REGS->SQI_CFG         |= SQI_CFG_SQIEN_Msk;

    ${SQI_INSTANCE_NAME}_REGS->SQI_INTSIGEN             = 0x00000000;
    ${SQI_INSTANCE_NAME}_REGS->SQI_INTEN                = 0x00000000;
    ${SQI_INSTANCE_NAME}_REGS->SQI_INTSTAT              = 0;

    ${SQI_INSTANCE_NAME}_REGS->SQI_CMDTHR               = SQI_CMDTHR_RXCMDTHR(0x20U) | SQI_CMDTHR_TXCMDTHR(0x20U);
    ${SQI_INSTANCE_NAME}_REGS->SQI_INTTHR               = SQI_INTTHR_RXINTTHR(0x01U) | SQI_INTTHR_TXINTTHR(0x01U);
    ${SQI_INSTANCE_NAME}_REGS->SQI_THR                  = SQI_THR_THRES(0x01U);

    ${SQI_INSTANCE_NAME}_REGS->SQI_INTEN                = (SQI_INTEN_PKTCOMPIE_Msk | SQI_INTEN_BDDONEIE_Msk);
    ${SQI_INSTANCE_NAME}_REGS->SQI_INTSIGEN             = (SQI_INTSIGEN_PKTCOMPISE_Msk | SQI_INTSIGEN_BDDONEISE_Msk);

<#if SQI_FLASH_STATUS_CHECK >
    // Flash status check
    ${SQI_INSTANCE_NAME}_REGS->SQI_MEMSTAT              = SQI_MEMSTAT_STATCMD(0x${SQI_STATCMD}U) | SQI_MEMSTAT_STATBYTES(${SQI_STATBYTES}U) | SQI_MEMSTAT_TYPESTAT(${SQI_STATTYPE}U) | SQI_MEMSTAT_STATPOS(${SQI_STATPOS}U);
</#if>

    ${SQI_INSTANCE_NAME}_REGS->SQI_INTFLAG              = SQI_INTFLAG_SQI_Msk;
    ${SQI_INSTANCE_NAME}_REGS->SQI_INTENSET             = SQI_INTENSET_SQI_Msk;

}

void ${SQI_INSTANCE_NAME}_DMASetup(void)
{
    ${SQI_INSTANCE_NAME}_REGS->SQI_CFG              |= SQI_CFG_MODE(0x02U);

    ${SQI_INSTANCE_NAME}_REGS->SQI_INTEN            &= ~SQI_INTEN_PKTCOMPIE_Msk;
    ${SQI_INSTANCE_NAME}_REGS->SQI_INTEN            |= SQI_INTEN_PKTCOMPIE_Msk;

    ${SQI_INSTANCE_NAME}_REGS->SQI_INTEN            &= ~SQI_INTEN_BDDONEIE_Msk;
    ${SQI_INSTANCE_NAME}_REGS->SQI_INTEN            |= SQI_INTEN_BDDONEIE_Msk;

    ${SQI_INSTANCE_NAME}_REGS->SQI_INTFLAG          = SQI_INTFLAG_SQI_Msk;
    ${SQI_INSTANCE_NAME}_REGS->SQI_INTENSET         = SQI_INTENSET_SQI_Msk;
}

void ${SQI_INSTANCE_NAME}_DMATransfer(sqi_dma_desc_t *sqiDmaDesc)
{
    // Reset RX FIFO before starting DMA
    ${SQI_INSTANCE_NAME}_REGS->SQI_CFG              |= SQI_CFG_RXBUFRST_Msk;

    // Initialize the root buffer descriptor
    ${SQI_INSTANCE_NAME}_REGS->SQI_BDBASEADD         = (uint32_t)sqiDmaDesc;

    // Enable DMA and start the Buffer descriptor processing
    ${SQI_INSTANCE_NAME}_REGS->SQI_BDCON             = SQI_BDCON_START_Msk | SQI_BDCON_DMAEN_Msk;
}

void ${SQI_INSTANCE_NAME}_XIPSetup(uint32_t sqiXcon1Val, uint32_t sqiXcon2Val)
{
    ${SQI_INSTANCE_NAME}_REGS->SQI_XCON1           = sqiXcon1Val;
    ${SQI_INSTANCE_NAME}_REGS->SQI_XCON2           = sqiXcon2Val;

    ${SQI_INSTANCE_NAME}_REGS->SQI_CFG            |= SQI_CFG_MODE(0x03U);
}

void ${SQI_INSTANCE_NAME}_RegisterCallback(SQI_EVENT_HANDLER event_handler, uintptr_t context)
{
    ${SQI_INSTANCE_NAME}EventHandler = event_handler;
    ${SQI_INSTANCE_NAME}Context      = context;
}

void ${SQI_INSTANCE_NAME}_InterruptHandler(void)
{
    ${SQI_INSTANCE_NAME}_REGS->SQI_INTFLAG          = SQI_INTFLAG_SQI_Msk;

    if (((${SQI_INSTANCE_NAME}_REGS->SQI_INTSTAT & SQI_INTSTAT_PKTCOMPIF_Msk) != 0U) || ((${SQI_INSTANCE_NAME}_REGS->SQI_INTSTAT & SQI_INTSTAT_BDDONEIF_Msk) != 0U))
    {
        ${SQI_INSTANCE_NAME}_REGS->SQI_INTSTAT      &= ~SQI_INTSTAT_PKTCOMPIF_Msk;
        ${SQI_INSTANCE_NAME}_REGS->SQI_INTEN        &= ~SQI_INTEN_PKTCOMPIE_Msk;
        ${SQI_INSTANCE_NAME}_REGS->SQI_INTEN        |= SQI_INTEN_PKTCOMPIE_Msk;

        ${SQI_INSTANCE_NAME}_REGS->SQI_INTSTAT      &= ~SQI_INTSTAT_BDDONEIF_Msk;
        ${SQI_INSTANCE_NAME}_REGS->SQI_INTEN        &= ~SQI_INTEN_BDDONEIE_Msk;
        ${SQI_INSTANCE_NAME}_REGS->SQI_INTEN        |= SQI_INTEN_BDDONEIE_Msk;

        // Disable DMA
        ${SQI_INSTANCE_NAME}_REGS->SQI_BDCON        = 0x0;

        if (${SQI_INSTANCE_NAME}EventHandler != NULL)
        {
            ${SQI_INSTANCE_NAME}EventHandler(${SQI_INSTANCE_NAME}Context);
        }
    }
}
