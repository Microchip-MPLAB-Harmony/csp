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

bool alarm_triggered;
void RTC_Callback(RTC_CLOCK_INT_MASK int_cause , uintptr_t  context)
{
    if (int_cause & RTC_CLOCK_INT_MASK_ALARM)
    {
        alarm_triggered = true;
        LED_Toggle();
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
    struct tm sys_time;
    struct tm alarm_time;

    alarm_triggered = false;

    //15-01-2018 12:00:00 Monday
    sys_time.tm_hour = 12;      /* hour [0,23] */
    sys_time.tm_sec = 00;       /* seconds [0,61] */
    sys_time.tm_min = 00;       /* minutes [0,59] */
    sys_time.tm_mon = 0;        /* month of year [0,11] */
    sys_time.tm_year = 118;     /* years since 1900 */
    sys_time.tm_mday = 15;      /* day of month [1,31] */
    sys_time.tm_wday = 1;       /* day of week [0,6] (Sunday = 0) */
                                /* tm_yday - day of year [0,365] */
                                /* tm_isdst - daylight savings flag */

    //15-01-2018 12:00:20 Monday
    alarm_time.tm_hour = 12;
    alarm_time.tm_sec = 20;
    alarm_time.tm_min = 00;
    alarm_time.tm_mon = 0;
    alarm_time.tm_year = 118;
    alarm_time.tm_mday = 15;
    alarm_time.tm_wday = 1;

    printf("\n\r---------------------------------------------------------%s","");
    printf("\n\r                    RTC Demo                 %s","");
    printf("\n\r---------------------------------------------------------\n\r%s","");

    RTC_RTCCCallbackRegister(RTC_Callback, (uintptr_t) NULL);

    RTC_RTCCTimeSet(&sys_time);
    RTC_RTCCAlarmSet(&alarm_time, RTC_ALARM_MASK_HHMMSS);

    printf("\n\rThe Alarm will Trigger at 12:00:20\n\n\r %s","");

    while ( true )
    {
        RTC_RTCCTimeGet(&sys_time);
        printf("System time is:   %02d:%02d:%02d \r",sys_time.tm_hour, sys_time.tm_min, sys_time.tm_sec);

        if(alarm_triggered == true)
        {
            printf("\n\rAlarm Triggered !!!!!!!!\n\r%s","");
            alarm_triggered = false;
        }
    }

    /* Execution should not come here during normal operation */

    return ( EXIT_FAILURE );
}

/*******************************************************************************
 End of File
*/

