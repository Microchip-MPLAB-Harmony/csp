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
#include <string.h>
#include <stdio.h>

/* Value of RTC_COMPARE_VAL defines the interval at which AC is triggered
 * by the RTC
 */
#define RTC_COMPARE_VAL 2000

uintptr_t comparator_context;
volatile uint32_t change_detect = 0;
volatile uint32_t ac_comparison_done = 0;


void ac_callBack(uintptr_t ac_context)
{
    ac_comparison_done = 1;
    
    /* Indication that a comparison is done */
    PORT_PinToggle(PORT_PIN_PC05);
    
    /* Check the comparator output state */
    if(ac_context & AC_STATUSA_STATE0_Msk)
    {
        change_detect  = 1;
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
    RTC_Timer32Start();
    RTC_Timer32CompareSet(RTC_COMPARE_VAL);
    AC_CallbackRegister(ac_callBack,comparator_context);
    printf("\r\n\r\nAC Demo - RTC triggers AC comparison on PA04\r\n");

    while ( true )
    {
        PM_SleepModeEnter(PM_SLEEPCFG_SLEEPMODE_STANDBY);
        /* Maintain state machines of all polled MPLAB Harmony modules. */
        SYS_Tasks ( );
        if(ac_comparison_done)
        {
            ac_comparison_done = 0;
            if(change_detect)
            {
                change_detect = 0;
                printf("\r\nPA04 voltage is above detect level\r\n");
            }
            else
            {
                printf("\r\nPA04 voltage is below detect level\r\n");
            }
        }
    }

    /* Execution should not come here during normal operation */

    return ( EXIT_FAILURE );
}


/*******************************************************************************
 End of File
*/

