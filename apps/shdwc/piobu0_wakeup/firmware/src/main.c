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
void switchHandler( PIO_PIN pin, uintptr_t context)
{
    SHDWC_Shutdown();
}

int main ( void )
{
    /* Initialize all modules */
    SYS_Initialize ( NULL );
    PIO_PinInterruptCallbackRegister(SWITCH_PIN, switchHandler, 0);
    PIO_PinInterruptEnable(SWITCH_PIN);

    while ( true )
    {
        PIT_DelayMs(500);
        LED_Toggle();
        /* Maintain state machines of all polled MPLAB Harmony modules. */
        SYS_Tasks ( );
    }

    /* Execution should not come here during normal operation */

    return ( EXIT_FAILURE );
}


/*******************************************************************************
  End of File
  */

