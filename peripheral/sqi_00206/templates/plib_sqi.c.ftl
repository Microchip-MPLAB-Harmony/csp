/*******************************************************************************
  ${SQI_INSTANCE_NAME} Peripheral Library Source File

  Company
    Microchip Technology Inc.

  File Name
    plib_${SQI_INSTANCE_NAME?lower_case}.c

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

#include "plib_${SQI_INSTANCE_NAME?lower_case}.h"

#define ${SQI_INSTANCE_NAME}_INTERRUPT_ENABLE_MASK   ${SQI_IEC_REG_VALUE}
#define ${SQI_INSTANCE_NAME}_INTERRUPT_FLAG_MASK     ${SQI_IFS_REG_VALUE}

#define ${SQI_INSTANCE_NAME}_CFG_DMA_MODE            (SQI_DMA_MODE << _${SQI_INSTANCE_NAME}CFG_MODE_POSITION)
#define ${SQI_INSTANCE_NAME}_CFG_XIP_MODE            (SQI_XIP_MODE << _${SQI_INSTANCE_NAME}CFG_MODE_POSITION)
#define ${SQI_INSTANCE_NAME}_CFG_DATAEN              (QUAD_MODE << _${SQI_INSTANCE_NAME}CFG_DATAEN_POSITION)

#define ${SQI_INSTANCE_NAME}_CFG_CHIP_SELECT         (${SQI_CSEN} << _${SQI_INSTANCE_NAME}CFG_CSEN_POSITION)

#define ${SQI_INSTANCE_NAME}_CLKCON_CLK_DIV          (${SQI_CLKDIV} << _${SQI_INSTANCE_NAME}CLKCON_CLKDIV_POSITION)

#define ${SQI_INSTANCE_NAME}_CMDTHR_RXCMDTHR(val)    (val << _${SQI_INSTANCE_NAME}CMDTHR_RXCMDTHR_POSITION)
#define ${SQI_INSTANCE_NAME}_CMDTHR_TXCMDTHR(val)    (val << _${SQI_INSTANCE_NAME}CMDTHR_TXCMDTHR_POSITION)

#define ${SQI_INSTANCE_NAME}_INTTHR_RXINTTHR(val)    (val << _${SQI_INSTANCE_NAME}INTTHR_RXINTTHR_POSITION)
#define ${SQI_INSTANCE_NAME}_INTTHR_TXINTTHR(val)    (val << _${SQI_INSTANCE_NAME}INTTHR_TXINTTHR_POSITION)

#define ${SQI_INSTANCE_NAME}_THR_THRES(val)          (val << _${SQI_INSTANCE_NAME}THR_THRES_POSITION)

<#if SQI_FLASH_STATUS_CHECK >
    <#lt>#define ${SQI_INSTANCE_NAME}_MEMSTAT_STATCMD_VAL     (0x${SQI_STATCMD} << _${SQI_INSTANCE_NAME}MEMSTAT_STATCMD_POSITION)
    <#lt>#define ${SQI_INSTANCE_NAME}_MEMSTAT_STATBYTES_VAL   (${SQI_STATBYTES} << _${SQI_INSTANCE_NAME}MEMSTAT_STATBYTES_POSITION)
    <#lt>#define ${SQI_INSTANCE_NAME}_MEMSTAT_STATTYPE_VAL    (${SQI_STATTYPE}_MODE << _${SQI_INSTANCE_NAME}MEMSTAT_STATTYPE_POSITION)
    <#lt>#define ${SQI_INSTANCE_NAME}_MEMSTAT_STATPOS_VAL     (${SQI_STATPOS} << _${SQI_INSTANCE_NAME}MEMSTAT_STATPOS_POSITION)
</#if>

SQI_EVENT_HANDLER ${SQI_INSTANCE_NAME}EventHandler = NULL;

uintptr_t ${SQI_INSTANCE_NAME}Context = (uintptr_t)NULL;

void ${SQI_INSTANCE_NAME}_Initialize(void)
{
    // Reset and Disable SQI
    ${SQI_INSTANCE_NAME}CFG = _${SQI_INSTANCE_NAME}CFG_RESET_MASK;

    // Set Config Register values
    ${SQI_INSTANCE_NAME}CFG = ( ${SQI_INSTANCE_NAME}_CFG_DMA_MODE | _${SQI_INSTANCE_NAME}CFG_BURSTEN_MASK |
           <#lt>                ${SQI_INSTANCE_NAME}_CFG_DATAEN | ${SQI_INSTANCE_NAME}_CFG_CHIP_SELECT)<#if SQI_LSBF =="LSB"> | _${SQI_INSTANCE_NAME}CFG_LSBF_MASK </#if> <#if SQI_CPOL=="HIGH"> | _${SQI_INSTANCE_NAME}CFG_CPOL_MASK </#if> <#if SQI_CPHA=="TRAILING"> | _${SQI_INSTANCE_NAME}CFG_CPHA_MASK </#if>;

     // SQICLK configuration
    ${SQI_INSTANCE_NAME}CLKCON      = _${SQI_INSTANCE_NAME}CLKCON_EN_MASK;              // Enable Clock

    while (!(${SQI_INSTANCE_NAME}CLKCON & _${SQI_INSTANCE_NAME}CLKCON_STABLE_MASK));    // Wait for clock to become stable

    ${SQI_INSTANCE_NAME}CLKCON      |= ${SQI_INSTANCE_NAME}_CLKCON_CLK_DIV;

    // Enable the SQI Module
    ${SQI_INSTANCE_NAME}CFG         |= _${SQI_INSTANCE_NAME}CFG_SQIEN_MASK;

    ${SQI_INSTANCE_NAME}INTSIGEN    = 0x00000000;
    ${SQI_INSTANCE_NAME}INTEN       = 0x00000000;
    ${SQI_INSTANCE_NAME}INTSTAT     = 0;

    ${SQI_INSTANCE_NAME}CMDTHR      = (${SQI_INSTANCE_NAME}_CMDTHR_RXCMDTHR(0x20) | ${SQI_INSTANCE_NAME}_CMDTHR_TXCMDTHR(0x20));
    ${SQI_INSTANCE_NAME}INTTHR      = (${SQI_INSTANCE_NAME}_INTTHR_RXINTTHR(0x01) | ${SQI_INSTANCE_NAME}_INTTHR_TXINTTHR(0x01));
    ${SQI_INSTANCE_NAME}THR         = ${SQI_INSTANCE_NAME}_THR_THRES(0x01);

    ${SQI_INSTANCE_NAME}INTEN       = (_${SQI_INSTANCE_NAME}INTEN_PKTCOMPIE_MASK | _${SQI_INSTANCE_NAME}INTEN_BDDONEIE_MASK);
    ${SQI_INSTANCE_NAME}INTSIGEN    = (_${SQI_INSTANCE_NAME}INTSIGEN_PKTCOMPISE_MASK | _${SQI_INSTANCE_NAME}INTSIGEN_BDDONEISE_MASK);

<#if SQI_FLASH_STATUS_CHECK >
    // Flash status check
    ${SQI_INSTANCE_NAME}MEMSTAT     = ${SQI_INSTANCE_NAME}_MEMSTAT_STATCMD_VAL | ${SQI_INSTANCE_NAME}_MEMSTAT_STATBYTES_VAL |
                      ${SQI_INSTANCE_NAME}_MEMSTAT_STATTYPE_VAL | ${SQI_INSTANCE_NAME}_MEMSTAT_STATPOS_VAL;
</#if>

    ${SQI_IEC_REG}SET         = ${SQI_INSTANCE_NAME}_INTERRUPT_ENABLE_MASK;

}

void ${SQI_INSTANCE_NAME}_DMASetup(void)
{
    ${SQI_INSTANCE_NAME}CFGbits.MODE            = SQI_DMA_MODE;

    ${SQI_INSTANCE_NAME}INTENbits.PKTCOMPIE     = 0;
    ${SQI_INSTANCE_NAME}INTENbits.PKTCOMPIE     = 1;

    ${SQI_INSTANCE_NAME}INTENbits.BDDONEIE      = 0;
    ${SQI_INSTANCE_NAME}INTENbits.BDDONEIE      = 1;

    ${SQI_IEC_REG}SET                     = ${SQI_INSTANCE_NAME}_INTERRUPT_ENABLE_MASK;
}

void ${SQI_INSTANCE_NAME}_DMATransfer(sqi_dma_desc_t *sqiDmaDesc)
{
    // Initialize the root buffer descriptor
    ${SQI_INSTANCE_NAME}BDBASEADD   = (uint32_t)sqiDmaDesc;

    // Enable DMA and start the Buffer descriptor processing
    ${SQI_INSTANCE_NAME}BDCON       = _${SQI_INSTANCE_NAME}BDCON_START_MASK | _${SQI_INSTANCE_NAME}BDCON_DMAEN_MASK;
}

void ${SQI_INSTANCE_NAME}_XIPSetup(uint32_t sqiXcon1Val, uint32_t sqiXcon2Val)
{
    ${SQI_INSTANCE_NAME}XCON1           = sqiXcon1Val;
    ${SQI_INSTANCE_NAME}XCON2           = sqiXcon2Val;

    ${SQI_INSTANCE_NAME}CFGbits.MODE    = SQI_XIP_MODE;
}

void ${SQI_INSTANCE_NAME}_RegisterCallback(SQI_EVENT_HANDLER event_handler, uintptr_t context)
{
    ${SQI_INSTANCE_NAME}EventHandler = event_handler;
    ${SQI_INSTANCE_NAME}Context      = context;
}

void ${SQI_INSTANCE_NAME}_InterruptHandler(void)
{
    ${SQI_IFS_REG}CLR  = ${SQI_INSTANCE_NAME}_INTERRUPT_FLAG_MASK;

    if (${SQI_INSTANCE_NAME}INTSTATbits.PKTCOMPIF || ${SQI_INSTANCE_NAME}INTSTATbits.BDDONEIF)
    {
        ${SQI_INSTANCE_NAME}INTSTATbits.PKTCOMPIF   = 0;
        ${SQI_INSTANCE_NAME}INTENbits.PKTCOMPIE     = 0;
        ${SQI_INSTANCE_NAME}INTENbits.PKTCOMPIE     = 1;

        ${SQI_INSTANCE_NAME}INTSTATbits.BDDONEIF    = 0;
        ${SQI_INSTANCE_NAME}INTENbits.BDDONEIE      = 0;
        ${SQI_INSTANCE_NAME}INTENbits.BDDONEIE      = 1;

        // Disable DMA
        ${SQI_INSTANCE_NAME}BDCON                   = 0x0;

        if (${SQI_INSTANCE_NAME}EventHandler != NULL)
        {
            ${SQI_INSTANCE_NAME}EventHandler(${SQI_INSTANCE_NAME}Context);
        }
    }
}
