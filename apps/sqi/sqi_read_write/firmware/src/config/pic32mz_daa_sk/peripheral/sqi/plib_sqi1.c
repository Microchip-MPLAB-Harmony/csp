/*******************************************************************************
  SQI1 Peripheral Library Source File

  Company
    Microchip Technology Inc.

  File Name
    plib_sqi1.c

  Summary
    SQI1 peripheral library interface.

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

#include "plib_sqi1.h"

#define SQI1_INTERRUPT_ENABLE_MASK   0x200
#define SQI1_INTERRUPT_FLAG_MASK     0x200

#define SQI1_CFG_DMA_MODE            (SQI_DMA_MODE << _SQI1CFG_MODE_POSITION)
#define SQI1_CFG_XIP_MODE            (SQI_XIP_MODE << _SQI1CFG_MODE_POSITION)
#define SQI1_CFG_DATAEN              (QUAD_MODE << _SQI1CFG_DATAEN_POSITION)

#define SQI1_CFG_CHIP_SELECT         (0x3 << _SQI1CFG_CSEN_POSITION)

#define SQI1_CLKCON_CLK_DIV          (0x0 << _SQI1CLKCON_CLKDIV_POSITION)

#define SQI1_CMDTHR_RXCMDTHR(val)    (val << _SQI1CMDTHR_RXCMDTHR_POSITION)
#define SQI1_CMDTHR_TXCMDTHR(val)    (val << _SQI1CMDTHR_TXCMDTHR_POSITION)

#define SQI1_INTTHR_RXINTTHR(val)    (val << _SQI1INTTHR_RXINTTHR_POSITION)
#define SQI1_INTTHR_TXINTTHR(val)    (val << _SQI1INTTHR_TXINTTHR_POSITION)

#define SQI1_THR_THRES(val)          (val << _SQI1THR_THRES_POSITION)

#define SQI1_MEMSTAT_STATCMD_VAL     (0x5 << _SQI1MEMSTAT_STATCMD_POSITION)
#define SQI1_MEMSTAT_STATBYTES_VAL   (0x2 << _SQI1MEMSTAT_STATBYTES_POSITION)
#define SQI1_MEMSTAT_STATTYPE_VAL    (QUAD_MODE << _SQI1MEMSTAT_STATTYPE_POSITION)
#define SQI1_MEMSTAT_STATPOS_VAL     (0x1 << _SQI1MEMSTAT_STATPOS_POSITION)

SQI_EVENT_HANDLER SQI1EventHandler = NULL;

uintptr_t SQI1Context = (uintptr_t)NULL;

void SQI1_Initialize(void)
{
    // Reset and Disable SQI
    SQI1CFG = _SQI1CFG_RESET_MASK;

    // Set Config Register values
    SQI1CFG = ( SQI1_CFG_DMA_MODE | _SQI1CFG_BURSTEN_MASK |
                SQI1_CFG_DATAEN | SQI1_CFG_CHIP_SELECT)  ;

     // SQICLK configuration
    SQI1CLKCON      = _SQI1CLKCON_EN_MASK;              // Enable Clock

    while (!(SQI1CLKCON & _SQI1CLKCON_STABLE_MASK));    // Wait for clock to become stable

    SQI1CLKCON      |= SQI1_CLKCON_CLK_DIV;

    // Enable the SQI Module
    SQI1CFG         |= _SQI1CFG_SQIEN_MASK;

    SQI1INTSIGEN    = 0x00000000;
    SQI1INTEN       = 0x00000000;
    SQI1INTSTAT     = 0;

    SQI1CMDTHR      = (SQI1_CMDTHR_RXCMDTHR(0x20) | SQI1_CMDTHR_TXCMDTHR(0x20));
    SQI1INTTHR      = (SQI1_INTTHR_RXINTTHR(0x01) | SQI1_INTTHR_TXINTTHR(0x01));
    SQI1THR         = SQI1_THR_THRES(0x01);

    SQI1INTEN       = (_SQI1INTEN_PKTCOMPIE_MASK | _SQI1INTEN_BDDONEIE_MASK);
    SQI1INTSIGEN    = (_SQI1INTSIGEN_PKTCOMPISE_MASK | _SQI1INTSIGEN_BDDONEISE_MASK);

    // Flash status check
    SQI1MEMSTAT     = SQI1_MEMSTAT_STATCMD_VAL | SQI1_MEMSTAT_STATBYTES_VAL |
                      SQI1_MEMSTAT_STATTYPE_VAL | SQI1_MEMSTAT_STATPOS_VAL;

    IEC5SET         = SQI1_INTERRUPT_ENABLE_MASK;

}

void SQI1_DMASetup(void)
{
    SQI1CFGbits.MODE            = SQI_DMA_MODE;

    SQI1INTENbits.PKTCOMPIE     = 0;
    SQI1INTENbits.PKTCOMPIE     = 1;

    SQI1INTENbits.BDDONEIE      = 0;
    SQI1INTENbits.BDDONEIE      = 1;

    IEC5SET                     = SQI1_INTERRUPT_ENABLE_MASK;
}

void SQI1_DMATransfer(sqi_dma_desc_t *sqiDmaDesc)
{
    // Reset RX FIFO before starting DMA
    SQI1CFGbits.RXBUFRST = 1;

    // Initialize the root buffer descriptor
    SQI1BDBASEADD   = (uint32_t)sqiDmaDesc;

    // Enable DMA and start the Buffer descriptor processing
    SQI1BDCON       = _SQI1BDCON_START_MASK | _SQI1BDCON_DMAEN_MASK;
}

void SQI1_XIPSetup(uint32_t sqiXcon1Val, uint32_t sqiXcon2Val)
{
    SQI1XCON1           = sqiXcon1Val;
    SQI1XCON2           = sqiXcon2Val;

    SQI1CFGbits.MODE    = SQI_XIP_MODE;
}

void SQI1_RegisterCallback(SQI_EVENT_HANDLER event_handler, uintptr_t context)
{
    SQI1EventHandler = event_handler;
    SQI1Context      = context;
}

void SQI1_InterruptHandler(void)
{
    IFS5CLR  = SQI1_INTERRUPT_FLAG_MASK;

    if (SQI1INTSTATbits.PKTCOMPIF || SQI1INTSTATbits.BDDONEIF)
    {
        SQI1INTSTATbits.PKTCOMPIF   = 0;
        SQI1INTENbits.PKTCOMPIE     = 0;
        SQI1INTENbits.PKTCOMPIE     = 1;

        SQI1INTSTATbits.BDDONEIF    = 0;
        SQI1INTENbits.BDDONEIE      = 0;
        SQI1INTENbits.BDDONEIE      = 1;

        // Disable DMA
        SQI1BDCON                   = 0x0;

        if (SQI1EventHandler != NULL)
        {
            SQI1EventHandler(SQI1Context);
        }
    }
}
