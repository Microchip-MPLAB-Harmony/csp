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


// *****************************************************************************
// *****************************************************************************
// Section: Main Entry Point
// *****************************************************************************
// *****************************************************************************

#define PWM_CHANNEL_MASK_ALL (PWM_CHANNEL_0_MASK | PWM_CHANNEL_1_MASK | PWM_CHANNEL_2_MASK | PWM_CHANNEL_3_MASK)

volatile bool counter_event = false;

void pwm_callback(uint32_t status, uintptr_t context )
{
  counter_event = true;
}
int main ( void )
{
    /* Initialize all modules */
    SYS_Initialize ( NULL );
    
    printf("************** ***PWM Applications Demo **********************\r\n");
    printf("*Generates 3 PWM signals and one counter event as follows ****\r\n");
    printf("*******PWM0: Period= 1ms , Duty = 25%, Active High ***********\r\n");
    printf("*******PWM1: Period= 10ms , Duty = 50%, Active Low ***********\r\n");
    printf("*******PWM2: Period= 100ms , Duty = 75%, Active High *********\r\n");
    printf("*******Counter event: 1000ms counter overflow ****************\r\n");
    
    PWM_CallbackRegister(pwm_callback, NULL);
    
    PWM_ChannelsStart(PWM_CHANNEL_MASK_ALL);

    while ( true )
    {
       if(counter_event)
       {
         printf("Counter overflow occured on PWM Channel\r\n");
         counter_event = false;       
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

