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

uintptr_t rtc_context;
uintptr_t adc_context;
volatile uint16_t adc_result = 0;
volatile uint8_t adc_conv_done = 0;
volatile uint8_t adc_window_det = 0;

void adc0_cb(uintptr_t context )
{
   if((ADC0_REGS->ADC_INTFLAG & ADC_INTFLAG_WINMON_Msk) == ADC_INTFLAG_WINMON_Msk)
   {
       adc_window_det = 1;
   }
    adc_result = ADC0_ConversionResultGet();
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
    RTC_Timer32Start();
    RTC_Timer32CompareSet(1500);
    
    printf("\r\nADC SleepWalking example\r\n");
    ADC0_Enable();
    ADC0_CallbackRegister(adc0_cb, adc_context);

    while ( true )
    {
        PM_SleepModeEnter(PM_SLEEPCFG_SLEEPMODE_STANDBY);
        
        if(adc_window_det)
        {
            adc_window_det = 0;
            printf("\r\nADC Window detected \r\n");
            printf("\r\nADC result is %d\r\n", adc_result);
        }
    }

    /* Execution should not come here during normal operation */

    return ( EXIT_FAILURE );
}


/*******************************************************************************
 End of File
*/

