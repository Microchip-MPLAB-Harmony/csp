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
#include "definitions.h"         		// SYS function prototypes

bool tamper_detected;

void RTC_Callback(RTC_CLOCK_INT_MASK int_cause , uintptr_t  context)
{
    if (int_cause & RTC_CLOCK_INT_MASK_TAMPER)
	{
        tamper_detected = true;
        RTC_REGS->MODE2.RTC_TAMPID = RTC_TAMPID_Msk;
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
    struct tm tampered_time;
 
    tamper_detected = false;
            
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

    printf("\n\r---------------------------------------------------------");
    printf("\n\r                    RTC Tamper Demo                 ");
    printf("\n\r---------------------------------------------------------\n\r");

    RTC_RTCCCallbackRegister(RTC_Callback, (uintptr_t) NULL);
    RTC_RTCCTimeSet(&sys_time);
    
    
    while ( true )
    {
        RTC_RTCCTimeGet(&sys_time);
        printf("System time is:   %02d:%02d:%02d\r",sys_time.tm_hour, 
                sys_time.tm_min, sys_time.tm_sec);

        if(tamper_detected == true)
        {
            RTC_RTCCTimeStampGet(&tampered_time);
            printf("\n\rTamper Detected !!!! & ");
            printf("Tampered time is:   %02d:%02d:%02d",tampered_time.tm_hour, tampered_time.tm_min, tampered_time.tm_sec);
            printf("\n\r---------------------------------------------------------\n\r");
            tamper_detected = false;
        }
    }

    /* Execution should not come here during normal operation */

    return ( EXIT_FAILURE );
}


/*******************************************************************************
 End of File
*/
