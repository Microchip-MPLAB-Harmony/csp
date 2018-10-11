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

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

#include <stddef.h>                     // Defines NULL
#include <stdbool.h>                    // Defines true
#include <stdlib.h>                     // Defines EXIT_FAILURE
#include <stdio.h>
#include <string.h>
#include "definitions.h"                // SYS function prototypes

#define DMAC_TRANSFER_BYTECOUNT 32
#define RTC_COMPARE_VAL 100

volatile uint8_t dma_ch0Done = 0;
uint32_t myAppObj = 0;
uint8_t adc_result_array[DMAC_TRANSFER_BYTECOUNT];

void DmacCh0Cb(DMAC_TRANSFER_EVENT returned_evnt, uintptr_t MyDmacContext)
{
    if (DMAC_TRANSFER_EVENT_COMPLETE == returned_evnt)
    {
        dma_ch0Done = 1;
    }
    else if (DMAC_TRANSFER_EVENT_ERROR == returned_evnt)
    {
        PORT_PinSet(PORT_PIN_PC05);
        while(1);
    }
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
    ADC0_Enable();
    RTC_Timer32Start();
    RTC_Timer32CompareSet(RTC_COMPARE_VAL);
    DMAC_ChannelCallbackRegister(DMAC_CHANNEL_0, DmacCh0Cb, (uintptr_t)&myAppObj);
    DMAC_ChannelTransfer(DMAC_CHANNEL_0, (const void *)&ADC0_REGS->ADC_RESULT, (const void *)adc_result_array, DMAC_TRANSFER_BYTECOUNT);
    printf("\r\n\r\nADC Demo - Wake CPU after 'n' samples are taken\r\n");
    
    while ( true )
    {
        PM_SleepModeEnter(PM_SLEEPCFG_SLEEPMODE_STANDBY);

        if(dma_ch0Done)
        {
            printf("\r\nTransferred 16 results to array in SRAM\r\n");
            dma_ch0Done = 0;
            /* Configure the next transfer */
            DMAC_ChannelTransfer(DMAC_CHANNEL_0, (const void *)&ADC0_REGS->ADC_RESULT, (const void *)adc_result_array, DMAC_TRANSFER_BYTECOUNT);
        }
    }

    /* Execution should not come here during normal operation */

    return ( EXIT_FAILURE );
}


/*******************************************************************************
 End of File
*/
