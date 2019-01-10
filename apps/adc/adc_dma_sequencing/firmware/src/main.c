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
#include "definitions.h"                // SYS function prototypes

uint32_t  adc_seq_regs[4] = {0x1804, 0x1805, 0x1806, 0x1807};
volatile uint16_t     adc_res[4]      = {0};
volatile bool         adc_dma_done    = 0;

void adc_sram_dma_callback(DMAC_TRANSFER_EVENT event, uintptr_t contextHandle)
{
	adc_dma_done = true;
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
    printf("\r\n *********************************************** \r\n");
    printf("\r\n           ADC DMA SEQUENCING DEMO \r\n");
    printf("\r\n *********************************************** \r\n");

    printf("\r\n Configuring DMA............. \r\n");
    DMAC_ChannelCallbackRegister(DMAC_CHANNEL_1,adc_sram_dma_callback, 0);
    DMAC_ChannelTransfer(DMAC_CHANNEL_1,(const void *)&ADC0_REGS->ADC_RESULT,(const void *)adc_res,8);
    DMAC_ChannelTransfer(DMAC_CHANNEL_0,(const void *)adc_seq_regs,(const void *)&ADC0_REGS->ADC_DSEQDATA,16);
    ADC0_Enable();
    TC0_TimerStart();

    while ( true )
    {
        if (adc_dma_done) {
			adc_dma_done = false;
			printf("\r\n ADC conversion of 4 inputs done \r\n");
			printf("\r\n AIN4: 0x%x\r\n\r\n", adc_res[0]);
			printf("\r\n AIN5: 0x%x\r\n\r\n", adc_res[1]);
            printf("\r\n AIN6: 0x%x\r\n\r\n", adc_res[2]);
            printf("\r\n AIN7: 0x%x\r\n\r\n", adc_res[3]);
		}
        /* Maintain state machines of all polled MPLAB Harmony modules. */
        SYS_Tasks ( );
    }

    /* Execution should not come here during normal operation */

    return ( EXIT_FAILURE );
}


/*******************************************************************************
 End of File
*/

