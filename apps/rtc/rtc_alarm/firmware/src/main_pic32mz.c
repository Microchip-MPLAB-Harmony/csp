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
bool callback_reached = false;
void RTC_Callback( uintptr_t context, uint32_t int_cause )
{
    /* Place a breakpoint here to see that the callback was called, thereby
       demonstrating the RTCC timer alarm went off, generated an RTCC interrupt,
       and called a registered callback function. */
    callback_reached = true;
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
    
    /* This app will set the LED 20 seconds after program starts. */
    struct tm sys_time;
    struct tm alarm_time;
    //15-01-2018 12:00:00 Monday
    sys_time.tm_hour = 12;
    sys_time.tm_min = 00;
    sys_time.tm_sec = 00;
    sys_time.tm_mon = 1;
    sys_time.tm_year = 18;
    sys_time.tm_mday = 15;
    sys_time.tm_wday = 1;
    
    //15-01-2018 12:00:20 Monday
    alarm_time.tm_hour = 12;
    alarm_time.tm_sec = 20;
    alarm_time.tm_min = 00;
    alarm_time.tm_mon = 1;
    alarm_time.tm_year = 18;
    alarm_time.tm_mday = 15;
    alarm_time.tm_wday = 1;

    RTCC_CallbackRegister(RTC_Callback, (uintptr_t) NULL);
    
    if (RTCC_TimeSet(&sys_time) == false)
    {
        /* Error setting up time */
        while(1);
    }
    
    if (RTCC_AlarmSet(&alarm_time, RTC_ALARM_MASK_SS)== false)
    {
        /* Error setting up alarm */
        while(1);
    }
    /* The Alarm will Trigger at 12:00:20 */
    
    while ( true )
    {
        ;
    }

    /* Execution should not come here during normal operation */

    return ( EXIT_FAILURE );
}

/*******************************************************************************
 End of File
*/

