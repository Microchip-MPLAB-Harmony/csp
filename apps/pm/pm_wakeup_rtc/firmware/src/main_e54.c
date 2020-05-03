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
#define LED_ON LED_Clear
#define LED_OFF LED_Set

enum
{
  IDLE_SLEEP_MODE = 'a',
  STANDBY_SLEEP_MODE = 'b',
  HIBERNATE_SLEEP_MODE = 'c',
  OFF_SLEEP_MODE ='d',
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

void configure_alarm(void)
{
    RTC_Timer32Stop();
    RTC_Timer32CounterSet(0);
    RTC_Timer32Start();
}

void display_menu (void)
{
    printf("\n\n\n\rSelect the low power mode to enter");
    printf("\n\ra) Idle Sleep Mode");
    printf("\n\rb) Standby Sleep Mode"); 
    printf("\n\rc) Hibernate Sleep Mode");
    printf("\n\rd) Off Sleep Mode");
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
    RSTC_RESET_CAUSE reset_cause;
    RSTC_BKUPEXIT_CAUSE reset_cause_bkup;
    /* Initialize all modules */
    SYS_Initialize ( NULL );
    SUPC_SelectVoltageRegulator(SUPC_VREGSEL_BUCK);

    reset_cause_bkup = RSTC_BackupExitCauseGet();
    reset_cause = RSTC_ResetCauseGet();
   
    
    printf("\n\n\r----------------------------------------------");
    printf("\n\r             Low power demo using RTC           ");
    printf("\n\r----------------------------------------------"); 
          
    if(reset_cause_bkup == RSTC_BKUPEXIT_HIB_Msk)
        printf("\n\n\rDevice exited from Hibernate mode\n");
    else if(reset_cause == RSTC_RCAUSE_POR_Msk)
        printf("\n\n\rDevice exited from OFF mode\n");

    SYSTICK_TimerCallbackSet(&timeout, (uintptr_t) NULL);
    SYSTICK_TimerStart();
    RTC_Timer32InterruptEnable(RTC_TIMER32_INT_MASK_CMP0);
    display_menu();
    while(1)
    {
        switch(cmd)
        {
            case IDLE_SLEEP_MODE:
            {
                printf("\n\n\rConfiguring RTC Compare Match for wake up.......");
                configure_alarm();
                SYSTICK_TimerStop();
                printf("\n\rEntering Idle Mode");
                LED_OFF();
                PM_IdleModeEnter();
                printf("\n\rRTC Compare Match triggered waking up device from Idle mode");
                SYSTICK_TimerStart();
                display_menu();
                break;
            }
            case STANDBY_SLEEP_MODE:
            {
                printf("\n\n\rConfiguring RTC Compare Match for wake up.......");
                configure_alarm();
                SYSTICK_TimerStop();
                printf("\n\rEntering Standby Mode");
                LED_OFF();
                PM_StandbyModeEnter();
                printf("\n\rRTC Compare Match triggered waking up device from Standby mode");
                SYSTICK_TimerStart();
                display_menu();
                break;
            }
            case HIBERNATE_SLEEP_MODE:
            {
                printf("\n\n\rConfiguring RTC Compare Match for wake up.......");
                configure_alarm();
                SYSTICK_TimerStop();
                printf("\n\rEntering Hibernate Mode   ");
                LED_OFF();
                PM_HibernateModeEnter();
                break;
            }
            case OFF_SLEEP_MODE:
            {
                printf("\n\n\rConfiguring RTC Compare Match for wake up.......");
                configure_alarm();
                SYSTICK_TimerStop();
                printf("\n\rEntering OFF Mode");
                printf("\n\rPress Reset button to wakeup the device   ");   
                LED_OFF();
                PM_OffModeEnter();
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

