/*******************************************************************************
  Main Source File

  Company:
    Microchip Technology Inc.

  File Name:
    main_d2x.c

  Summary:
    This file contains the "main" function for a project.

  Description:
    This file contains the "main" function for a project. The "main" function
    calls the "SYS_Initialize" function to initialize the state machines of all 
    modules in the system.

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

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

#include <stddef.h>                     // Defines NULL
#include <stdbool.h>                    // Defines true
#include <stdlib.h>                     // Defines EXIT_FAILURE
#include "definitions.h"                // SYS function prototypes

// *****************************************************************************
// *****************************************************************************
// Section: Global Data Definitions
// *****************************************************************************
// *****************************************************************************

#define NUM_OF_SAMPLES (100)

const uint16_t sine_wave[NUM_OF_SAMPLES] = {
0x200,	0x210,	0x220,	0x230,	0x240,	0x24F,	0x25E,	0x26D,	0x27B,	0x289,
0x297,	0x2A3,	0x2AF,	0x2BB,	0x2C5,	0x2CF,	0x2D8,	0x2E0,	0x2E8,	0x2EE,
0x2F4,	0x2F8,	0x2FC,	0x2FE,	0x300,	0x300,	0x300,	0x2FE,	0x2FC,	0x2F8,
0x2F4,	0x2EE,	0x2E8,	0x2E0,	0x2D8,	0x2CF,	0x2C5,	0x2BB,	0x2AF,	0x2A3,
0x297,	0x289,	0x27B,	0x26D,	0x25E,	0x24F,	0x240,	0x230,	0x220,	0x210,
0x200,	0x1F0,	0x1E0,	0x1D0,	0x1C0,	0x1B1,	0x1A2,	0x193,	0x185,	0x177,
0x16A,	0x15D,	0x151,	0x146,	0x13B,	0x131,	0x128,	0x120,	0x118,	0x112,
0x10D,	0x108,	0x105,	0x102,	0x101,	0x100,	0x101,	0x102,	0x105,	0x108,
0x10D,	0x112,	0x118,	0x120,	0x128,	0x131,	0x13B,	0x146,	0x151,	0x15D,
0x16A,	0x177,	0x185,	0x193,	0x1A2,	0x1B1,	0x1C0,	0x1D0,	0x1E0,	0x1F0,
};


__attribute__((__aligned__(16))) static dmac_descriptor_registers_t pTxLinkedListDesc[1];

#define BUFFER_TX_BTCTRL    (DMAC_BTCTRL_STEPSIZE_X2 | DMAC_BTCTRL_SRCINC_Msk |     \
                             DMAC_BTCTRL_BEATSIZE_HWORD | DMAC_BTCTRL_BLOCKACT_INT | DMAC_BTCTRL_VALID_Msk)


void InitializeTxLinkedListDescriptor(void)
{
    pTxLinkedListDesc[0].DMAC_BTCTRL     = (uint16_t)BUFFER_TX_BTCTRL;
    pTxLinkedListDesc[0].DMAC_BTCNT      = NUM_OF_SAMPLES;
    pTxLinkedListDesc[0].DMAC_DESCADDR   = (uint32_t)&pTxLinkedListDesc[0];
    pTxLinkedListDesc[0].DMAC_DSTADDR    = (uint32_t)&DAC_REGS->DAC_DATABUF;
    pTxLinkedListDesc[0].DMAC_SRCADDR    = (uint32_t)sine_wave + sizeof(sine_wave);  
}

// *****************************************************************************
// *****************************************************************************
// Section: Main Entry Point
// *****************************************************************************
// *****************************************************************************

int main ( void )
{   
    /* Initialize all modules */
    SYS_Initialize ( NULL );

    InitializeTxLinkedListDescriptor();
    
    DMAC_ChannelLinkedListTransfer(DMAC_CHANNEL_0, &pTxLinkedListDesc[0]);         
    TC3_TimerStart();

    while ( true )
    {
        /* Maintain state machines of all polled MPLAB Harmony modules. */       
    }

    /* Execution should not come here during normal operation */

    return ( EXIT_FAILURE );
}


/*******************************************************************************
 End of File
*/

