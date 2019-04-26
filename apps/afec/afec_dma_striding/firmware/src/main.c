/*******************************************************************************
  Main Source File

  Company:
    Microchip Technology Inc.

  File Name:
    main.c

  Summary:
    This file contains the "main" function for a project.

  Description:
    This file contains the "main" function for a project.  The
    "main" function calls the "SYS_Initialize" function to initialize the state
    machines of all modules in the system
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

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

#include <stddef.h>                     // Defines NULL
#include <stdbool.h>                    // Defines true
#include <stdlib.h>                     // Defines EXIT_FAILURE
#include <stdio.h>
#include "definitions.h"                // SYS function prototypes

/*****************************************************
 AFEC CH0 - PB01 - Connect to DACC output PB13
 AFEC CH5 - PC30 - connect to Vcc
 AFEC_CH6 - PC31 - Connect to GND
 *****************************************************/

/* Number of ADC channels */
#define NUM_CHANNELS (3U)

/* Number of conversion samples per channel */
#define NUM_CONVERSIONS_PER_CHANNEL (100U)

#define AFEC_VREF               (3.3f)

#define AFEC_MAX_COUNT          (4095U)     

/* Save the result of 3 ADC channels */
static uint16_t __attribute__ ((aligned (32))) adc_count[320U];

/* transfer done flag */
volatile bool transfer_done = false;

uint8_t sine_index = 0U;

/** 100 points of sinewave samples. DAC output to be connected to AFEC channel 0 */
uint16_t sine_wave[NUM_CONVERSIONS_PER_CHANNEL] = {
    0x800,  0x840,  0x880,  0x8C0,  0x8FF,  0x93C,  0x979,  0x9B4,  0x9ED,  0xA25, 
    0xA5A,  0xA8D,  0xABD,  0xAEA,  0xB15,  0xB3C,  0xB61,  0xB81,  0xB9F,  0xBB8, 
    0xBCE,  0xBE0,  0xBEE,  0xBF8,  0xBFE,  0xC00,  0xBFE,  0xBF8,  0xBEE,  0xBE0, 
    0xBCE,  0xBB8,  0xB9F,  0xB81,  0xB61,  0xB3C,  0xB15,  0xAEA,  0xABD,  0xA8D, 
    0xA5A,  0xA25,  0x9ED,  0x9B4,  0x979,  0x93C,  0x8FF,  0x8C0,  0x880,  0x840, 
    0x800,  0x7C0,  0x780,  0x740,  0x701,  0x6C4,  0x687,  0x64C,  0x613,  0x5DB, 
    0x5A6,  0x573,  0x543,  0x516,  0x4EB,  0x4C4,  0x49F,  0x47F,  0x461,  0x448, 
    0x432,  0x420,  0x412,  0x408,  0x402,  0x400,  0x402,  0x408,  0x412,  0x420, 
    0x432,  0x448,  0x461,  0x47F,  0x49F,  0x4C4,  0x4EB,  0x516,  0x543,  0x573, 
    0x5A6,  0x5DB,  0x613,  0x64C,  0x687,  0x6C4,  0x701,  0x740,  0x780,  0x7C0
};

/* First descriptor control to ensure that view 3 descriptor is fetched */
__attribute__((__aligned__(32))) static XDMAC_DESCRIPTOR_CONTROL first_descriptor_control =
{
    .destinationUpdate = 1,
    .fetchEnable = 1,
    .sourceUpdate = 1,
    .view = 3
};

typedef struct
{
    XDMAC_DESCRIPTOR_VIEW_3 lld_3;
    
    /* Align to the cache line (32-byte) boundary*/
    uint8_t                 dummy[28];
}XDMAC_DESCRIPTORS;

/* View 3 linked list */
__attribute__((__aligned__(32))) static XDMAC_DESCRIPTORS xdmacDescriptor = 
{
    .lld_3 = 
    {
        .mbr_nda = (uint32_t)0,                       /* Next descriptor */
        .mbr_da = (uint32_t)&adc_count[0],              /* Destination address as adc_count array */
        .mbr_sa = (uint32_t)&AFEC1_REGS->AFEC_LCDR,   /* Source address as ADC result register */
        .mbr_bc = NUM_CONVERSIONS_PER_CHANNEL - 1U,   /* Micro-block length */
        .mbr_ds = 198U << XDMAC_CDS_MSP_DDS_MSP_Pos,  /* Data stride in terms of bytes. 99 positions * 2 bytes */
        .mbr_sus = 0U,                                /* Source microblock stride is disabled */
        .mbr_dus = -400,                              /* Destination microblock stride in bytes. 200 positions * 2 bytes */
        /* Enable destination data and micro-block stride */
        .mbr_cfg = XDMAC_CC_TYPE_PER_TRAN | XDMAC_CC_PERID(36U) | XDMAC_CC_MEMSET_NORMAL_MODE | XDMAC_CC_DSYNC_PER2MEM | XDMAC_CC_SWREQ_HWR_CONNECTED | XDMAC_CC_DAM_UBS_DS_AM | XDMAC_CC_SAM_FIXED_AM | XDMAC_CC_SIF_AHB_IF1 | XDMAC_CC_DIF_AHB_IF0 | XDMAC_CC_DWIDTH_HALFWORD | XDMAC_CC_CSIZE_CHK_1 | XDMAC_CC_MBSIZE_SINGLE,
        .mbr_ubc.blockDataLength = NUM_CHANNELS,   /* Number of microblocks */
        .mbr_ubc.nextDescriptorControl.destinationUpdate = 0,     /* Next destination update disabled */
        .mbr_ubc.nextDescriptorControl.sourceUpdate = 0,      /* Next source update disabled */
        .mbr_ubc.nextDescriptorControl.fetchEnable = 0,    /* Next descriptor fetch disabled */
        .mbr_ubc.nextDescriptorControl.view = 0            /* No next descriptor */
    }
};

/* This is called after linked list transfer is done */
void DMA_EventHandler(XDMAC_TRANSFER_EVENT event, uintptr_t context)
{
    if (event == XDMAC_TRANSFER_COMPLETE)
    {
        transfer_done = true;

    }
}

void TC1_CH0_CompareHandler(TC_COMPARE_STATUS status, uintptr_t context)
{
    /* Write next data sample */
    if (sine_index >= NUM_CONVERSIONS_PER_CHANNEL)
    {
        sine_index = 0U;
    } 
    DACC_DataWrite(DACC_CHANNEL_0, sine_wave[sine_index++]);
}

// *****************************************************************************
// *****************************************************************************
// Section: Main Entry Point
// *****************************************************************************
// *****************************************************************************

int main ( void )
{
    uint8_t i;
    float adc_ch0_voltage, adc_ch5_voltage, adc_ch6_voltage;
    
    DCACHE_CLEAN_BY_ADDR((uint32_t *)&xdmacDescriptor, sizeof(xdmacDescriptor));
    /* Initialize all modules */
    SYS_Initialize ( NULL );
    
    XDMAC_ChannelCallbackRegister(XDMAC_CHANNEL_0, DMA_EventHandler, (uintptr_t)NULL);
    XDMAC_ChannelLinkedListTransfer(XDMAC_CHANNEL_0, (uint32_t)&xdmacDescriptor, &first_descriptor_control);
    
    /* Invalidate cache lines having received buffer before using it
     * to load the latest data in the actual memory to the cache */
    DCACHE_INVALIDATE_BY_ADDR((uint32_t *)&adc_count, sizeof(adc_count));    
    
    DACC_DataWrite(DACC_CHANNEL_0, sine_wave[sine_index]);
    
    /* TC1_CH0 triggers ADC conversions every 200 us */
    TC1_CH0_CompareCallbackRegister(TC1_CH0_CompareHandler, (uintptr_t)NULL);
    TC1_CH0_CompareStart();
    
    printf("\n\r---------------------------------------------------------");
    printf("\n\r                    AFEC with DMA Striding Demo                 ");
    printf("\n\r---------------------------------------------------------\n\r");
    printf("CH0 Count  CH0 Voltage  CH5 Count  CH5 Voltage  CH6 Count  CH6 Voltage \n\r");
    
    while ( true )
    {
        if (transfer_done == true)
        {
            transfer_done = false;
             
            for (i = 0U; i < NUM_CONVERSIONS_PER_CHANNEL; i++)
            {
                /* Calculate voltage */ 
                adc_ch0_voltage = (float)adc_count[i] * AFEC_VREF/AFEC_MAX_COUNT;
                adc_ch5_voltage = (float)adc_count[i+NUM_CONVERSIONS_PER_CHANNEL] * AFEC_VREF/AFEC_MAX_COUNT;
                adc_ch6_voltage = (float)adc_count[i+(2*NUM_CONVERSIONS_PER_CHANNEL)] * AFEC_VREF/AFEC_MAX_COUNT;
                /* send data to console */
                printf("0x%03x      %0.2f V       0x%03x      %0.2f V       0x%03x      %0.2f V \n\r", \
                    adc_count[i], adc_ch0_voltage, adc_count[i+NUM_CONVERSIONS_PER_CHANNEL], adc_ch5_voltage, adc_count[i+(2*NUM_CONVERSIONS_PER_CHANNEL)], adc_ch6_voltage);
            }
        }
        
    }

    /* Execution should not come here during normal operation */

    return ( EXIT_FAILURE );
}


/*******************************************************************************
 End of File
*/

