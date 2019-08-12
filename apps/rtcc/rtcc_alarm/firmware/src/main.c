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
* Copyright (C) 2019 Microchip Technology Inc. and its subsidiaries.
*
* Subject to your compliance with these terms, you may use Microchip software
* and any derivatives exclusively with Microchip products. It is your
* responsibility to comply with third party license terms applicable to your
* use of third party software (including open source software) that may
* accompany Microchip software.
*
* THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS". NO WARRANTIES, WHETHER
* EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS SOFTWARE, INCLUDING ANY IMPLIED
* WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A
* PARTICULAR PURPOSE.
*
* IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL, PUNITIVE,
* INCIDENTAL OR CONSEQUENTIAL LOSS, DAMAGE, COST OR EXPENSE OF ANY KIND
* WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF MICROCHIP HAS
* BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO THE
* FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL CLAIMS IN
* ANY WAY RELATED TO THIS SOFTWARE WILL NOT EXCEED THE AMOUNT OF FEES, IF ANY,
* THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS SOFTWARE.
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
#include "definitions.h"                // SYS function prototypes
#include "stdio.h"
#include <string.h>

volatile bool rtcc_alarm = false;

void RTCC_Callback( uintptr_t context)
{
    rtcc_alarm = true;
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

    printf("\r\nRTCC Alarm demo. Alarm triggered once in a day\r\n");

    struct tm sys_time;
    struct tm alarm_time;

    // Time setting 31-12-2018 23:59:58 Monday
    sys_time.tm_hour = 23;
    sys_time.tm_min = 59;
    sys_time.tm_sec = 58;

    sys_time.tm_year = 18;
    sys_time.tm_mon = 12;
    sys_time.tm_mday = 31;
    sys_time.tm_wday = 1;

    // Alarm setting 01-01-2019 00:00:05 Tuesday
    alarm_time.tm_hour = 00;
    alarm_time.tm_min = 00;
    alarm_time.tm_sec = 05;

    alarm_time.tm_year = 19;
    alarm_time.tm_mon = 01;
    alarm_time.tm_mday = 01;
    alarm_time.tm_wday = 2;

    RTCC_CallbackRegister(RTCC_Callback, (uintptr_t) NULL);

    if (RTCC_TimeSet(&sys_time) == false)
    {
        /* Error setting up time */
        while(1);
    }

    if (RTCC_AlarmSet(&alarm_time, RTCC_ALARM_MASK_HHMISS) == false)
    {
        /* Error setting up alarm */
        while(1);
    }

    printf("\r\nAlarm set for Hour:Min:Sec %d:%d:%d\r\n", alarm_time.tm_hour, alarm_time.tm_min, alarm_time.tm_sec);

    while ( true )
    {
        /* Maintain state machines of all polled MPLAB Harmony modules. */
        SYS_Tasks ( );

        if(rtcc_alarm)
        {
            rtcc_alarm = false;
            RTCC_TimeGet(&sys_time);
            printf("\r\nAlarm triggered\r\n");
            printf("\r\nDD:MM:YY %d-%d-%d\r\n", sys_time.tm_mday, sys_time.tm_mon, sys_time.tm_year);
            printf("\r\nHour:Min:Sec %d:%d:%d\r\n", sys_time.tm_hour, sys_time.tm_min, sys_time.tm_sec);
        }
    }

    /* Execution should not come here during normal operation */

    return ( EXIT_FAILURE );
}


/*******************************************************************************
 End of File
*/

