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

// DOM-IGNORE-BEGIN
/*******************************************************************************
Copyright (c) 2017 released Microchip Technology Inc.  All rights reserved.

Microchip licenses to you the right to use, modify, copy and distribute
Software only when embedded on a Microchip microcontroller or digital signal
controller that is integrated into your product or third party product
(pursuant to the sublicense terms in the accompanying license agreement).

You should refer to the license agreement accompanying this Software for
additional information regarding your rights and obligations.

SOFTWARE AND DOCUMENTATION ARE PROVIDED AS IS  WITHOUT  WARRANTY  OF  ANY  KIND,
EITHER EXPRESS  OR  IMPLIED,  INCLUDING  WITHOUT  LIMITATION,  ANY  WARRANTY  OF
MERCHANTABILITY, TITLE, NON-INFRINGEMENT AND FITNESS FOR A  PARTICULAR  PURPOSE.
IN NO EVENT SHALL MICROCHIP OR  ITS  LICENSORS  BE  LIABLE  OR  OBLIGATED  UNDER
CONTRACT, NEGLIGENCE, STRICT LIABILITY, CONTRIBUTION,  BREACH  OF  WARRANTY,  OR
OTHER LEGAL  EQUITABLE  THEORY  ANY  DIRECT  OR  INDIRECT  DAMAGES  OR  EXPENSES
INCLUDING BUT NOT LIMITED TO ANY  INCIDENTAL,  SPECIAL,  INDIRECT,  PUNITIVE  OR
CONSEQUENTIAL DAMAGES, LOST  PROFITS  OR  LOST  DATA,  COST  OF  PROCUREMENT  OF
SUBSTITUTE  GOODS,  TECHNOLOGY,  SERVICES,  OR  ANY  CLAIMS  BY  THIRD   PARTIES
(INCLUDING BUT NOT LIMITED TO ANY DEFENSE  THEREOF),  OR  OTHER  SIMILAR  COSTS.
*******************************************************************************/
// DOM-IGNORE-END


// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

#include <stddef.h>                     // Defines NULL
#include <stdbool.h>                    // Defines true
#include <stdlib.h>                     // Defines EXIT_FAILURE
#include "definitions.h"         		// SYS function prototypes

void RTC_Callback( uintptr_t context, uint32_t int_cause )
{
	if (int_cause & RTC_INT_ALARM)
	{
		printf("\n\rAlarm Triggered !!!!!!!!\n\r");
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
    //15-01-2018 12:00:00 Monday
    sys_time.tm_hour = 12;
    sys_time.tm_sec = 00;
    sys_time.tm_min = 00;
    sys_time.tm_mon = 0;
    sys_time.tm_year = 118;
    sys_time.tm_mday = 15;
    sys_time.tm_wday = 1;
    
    //15-01-2018 12:00:20 Monday
    alarm_time.tm_hour = 12;
    alarm_time.tm_sec = 20;
    alarm_time.tm_min = 00;
    alarm_time.tm_mon = 0;
    alarm_time.tm_year = 118;
    alarm_time.tm_mday = 15;
    alarm_time.tm_wday = 1;

    printf("\n\r---------------------------------------------------------");
    printf("\n\r                    RTC Demo                 ");
    printf("\n\r---------------------------------------------------------\n\r");

    RTC_CallbackRegister(RTC_Callback, (uintptr_t) NULL);
    
    if (RTC_TimeSet(&sys_time) == false)
    {
        printf("\n\rError setting up time\n");
        while(1);
    }
    
    if (RTC_AlarmSet(&alarm_time, RTC_ALARM_MASK_HHMISS)== false)
    {
        printf("\n\rError setting up alarm\n");
        while(1);
    }
    printf("\n\rThe Alarm will Trigger at 12:00:20\n\n\r");
    
    while ( true )
    {
        RTC_TimeGet(&sys_time);
        printf("System time is:   %02d:%02d:%02d\r",sys_time.tm_hour, sys_time.tm_min, sys_time.tm_sec);
    }

    /* Execution should not come here during normal operation */

    return ( EXIT_FAILURE );
}


/*******************************************************************************
 End of File
*/
