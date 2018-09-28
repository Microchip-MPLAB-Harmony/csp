/*******************************************************************************
  Main Source File

  Company:
    Microchip Technology Inc.

  File Name:
    main.c

  Summary:
    This file contains the "main" function for a project.

  Description:
    This file contains the "main" function for a project. The "main" function
    calls the "SYS_Initialize" function to initialize the state machines of all 
    modules in the system.

*******************************************************************************/

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
// Section: Global Variable and defines
// *****************************************************************************
// *****************************************************************************

#define LED_ON LED_Clear
#define LED_OFF LED_Set

enum
{
    SLEEP_MODE = 'a',
    WAIT_MODE = 'b',
    BACKUP_MODE = 'c'
}SLEEP_MODES;

uint8_t cmd = 0;

// *****************************************************************************
// *****************************************************************************
// Section: Application Callback Functions
// *****************************************************************************
// *****************************************************************************
void timeout (uintptr_t context)
{
    LED_Toggle();    
}

void configure_alarm()
{
    RTT_Disable();
    RTT_AlarmValueSet(10);
    RTT_Enable();
}

void display_menu (void)
{
    printf("\n\n\n\rSelect the low power mode to enter");
    printf("\n\ra) Sleep Mode");
    printf("\n\rb) Wait Mode");
    printf("\n\rc) Backup Mode");   
    
    printf("\n\rEnter your choice");    
    scanf("%c", &cmd);
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

    printf("\n\n\r----------------------------------------------");
    printf("\n\r                 LOW power demo"               );
    printf("\n\r----------------------------------------------"); 
    
    SYSTICK_TimerCallbackSet(&timeout, (uintptr_t) NULL);
    SYSTICK_TimerStart();
    
    display_menu();
    while(1)
    {
        switch(cmd)
        {
            case SLEEP_MODE:
            {
                printf("\n\n\rConfiguring RTT Alarm for wake up.......");
                configure_alarm();
                SYSTICK_TimerStop();
                printf("\n\rEntering SLEEP Mode");
                LED_OFF();
                SUPC_SleepModeEnter();
                printf("\n\rRTT ALARM triggered waking up device from Sleep mode");
                SYSTICK_TimerStart();
                display_menu();
                break;
            }
            case WAIT_MODE:
            {
                printf("\n\n\rConfiguring RTT Alarm for wake up.......");
                configure_alarm();
                SYSTICK_TimerStop();
                printf("\n\rEntering WAIT Mode");
                LED_OFF();
                SUPC_WaitModeEnter (PMC_FSMR_FLPM_FLASH_DEEP_POWERDOWN, WAITMODE_WKUP_RTT);
                printf("\n\rRTT ALARM triggered waking up device from Wait mode");
                SYSTICK_TimerStart();
                display_menu();
                break;
            }
            case BACKUP_MODE:
            {
                printf("\n\n\rConfiguring RTT Alarm for wake up.......");
                configure_alarm();
                SYSTICK_TimerStop();
                printf("\n\rEntering Backup Mode \n");
                LED_OFF();
                SUPC_BackupModeEnter();
                break;
            }
            default:
            {
                printf("\n\rInvalid choice");
                display_menu();
                break;
            }
        } 
    }

    /* Execution should not come here during normal operation */

    return ( EXIT_FAILURE );
}


/*******************************************************************************
 End of File
*/

