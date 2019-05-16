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
* Copyright (C) 2018 Microchip Technology Inc. and its subsidiaries.
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
    
    printf("\n\rEnter your choice ");    
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
                printf("\n\rEntering WAIT Mode ");
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

