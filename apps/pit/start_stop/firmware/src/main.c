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

static int timerState = 1;

void togglePIT(PIO_PIN pin, uintptr_t context)
{
    (void)context;
    (void)pin;
    if (timerState){
        PIT_TimerStop();
        timerState = 0;
    }else {
        PIT_TimerStart();
        timerState = 1;
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

    PIO_PinInterruptCallbackRegister(USER_PB_PIN, togglePIT, 0);
    PIO_PinInterruptEnable(USER_PB_PIN);

    while ( true )
    {
        PIT_DelayMs(1000);
        LED_BLUE_Toggle();
        /* Maintain state machines of all polled MPLAB Harmony modules. */
        SYS_Tasks ( );
    }

    /* Execution should not come here during normal operation */

    return ( EXIT_FAILURE );
}


/*******************************************************************************
 End of File
*/

