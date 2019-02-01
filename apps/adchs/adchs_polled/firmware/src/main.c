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

#define ADCHS_VREF               (3.3f)

uint16_t adc_count;
float input_voltage;


// *****************************************************************************
// *****************************************************************************
// Section: Main Entry Point
// *****************************************************************************
// *****************************************************************************

int main ( void )
{
    /* Initialize all modules */
    SYS_Initialize ( NULL );

    while ( true )
    {
        /* Maintain state machines of all polled MPLAB Harmony modules. */
        SYS_Tasks ( );
        /* Start ADC conversion */
        ADCHS_ConversionStart();

        /* Wait till ADC conversion result is available */
        while(!ADCHS_ChannelResultIsReady(ADCHS_CH0))
        {

        };

        /* Read the ADC result */
        adc_count = ADCHS_ChannelResultGet(ADCHS_CH0);
        input_voltage = (float)adc_count * ADCHS_VREF / 4095U;

//        printf("ADC Count = 0x%03x, ADC Input Voltage = %0.2f V \r",adc_count, input_voltage);    
        
        //SYSTICK_DelayMs(500);
    }

    /* Execution should not come here during normal operation */

    return ( EXIT_FAILURE );
}


/*******************************************************************************
 End of File
*/

