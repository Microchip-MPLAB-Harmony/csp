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

#include <stddef.h>                     // Defines NULL
#include <stdbool.h>                    // Defines true
#include <stdlib.h>                     // Defines EXIT_FAILURE
#include "definitions.h"                // SYS function prototypes

/* Input waveform - compare value increment*/
#define CMP_VAL_INCREMENT (600U)

/* Calculated duty cycle of the input waveform in %*/
int duty;
/* Calculated frequency of the input waveform in Hz*/
int frequency;

volatile bool tc_buffer_ready = false;

void capture_handler( TC_CAPTURE_STATUS status, uintptr_t context)
{   
    if ((status  & TC_CAPTURE_STAUTS_CAPTURE0_READY) == TC_CAPTURE_STAUTS_CAPTURE0_READY)
    {
     tc_buffer_ready = true;
    }
}

// *****************************************************************************
// *****************************************************************************
// Section: Main Entry Point
// *****************************************************************************
// *****************************************************************************

int main ( void )
{
    uint16_t period,on_time;
    uint16_t cmp_period, cmp_val=0; 
    
    /* Initialize all modules */
    SYS_Initialize ( NULL );
    
    SYSTICK_TimerStart();
    cmp_period = TC0_Compare16bitPeriodGet();
    TC0_CompareStart();
    TC1_CaptureStart();
    
    TC1_CaptureCallbackRegister(capture_handler, (uintptr_t)NULL);

    while (true )
    {
        /* Change the duty cycle of the input waveform  */
        cmp_val += CMP_VAL_INCREMENT;
        if (cmp_val >= cmp_period)
        {
            cmp_val = CMP_VAL_INCREMENT;
        }
        TC0_Compare16bitSet(cmp_val);
        
        /* Wait for compare event */
        while(tc_buffer_ready != true);
        
        /* Read Captured values */ 
        period = TC1_Capture16bitChannel0Get();
        on_time = TC1_Capture16bitChannel1Get();

        /* Compute Duty Cycle in percentage and Frequency in Hz */
        duty = ((on_time) * 100U) / period;
        frequency = (TC1_CaptureFrequencyGet() / period);
        
        /* Send the measured data to console for display  */
        printf("Frequency of waveform: %d Hz \t Duty Cycle of waveform: %d ",(int) frequency,(int) duty);
        printf("\r\n"); 
                
        /* Wait for 1 second */ 
        SYSTICK_DelayMs(1000);
        
        tc_buffer_ready = false;
    }

    /* Execution should not come here during normal operation */

    return ( EXIT_FAILURE );
}


/*******************************************************************************
 End of File
*/

