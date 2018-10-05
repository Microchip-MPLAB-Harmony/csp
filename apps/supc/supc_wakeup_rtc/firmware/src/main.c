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
    struct tm alarm_time; 
    RTC_TimeGet(&alarm_time);
    alarm_time.tm_sec = (alarm_time.tm_sec + 10) % 60;
    RTC_AlarmSet(&alarm_time, RTC_ALARM_MASK_SS);
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

void populate_backupram(void)
{
    printf("\n\rPopulating Backup RAM");
    uint32_t *addr = (uint32_t *)0x40074000;
    for(uint32_t i = 0; i < 256; i++)
    {
        *addr = i;
        addr++;
    }
}

void validate_backupram(void)
{
    bool result = true;
    printf("\n\rValidating Backup RAM");
    uint32_t *addr = (uint32_t *)0x40074000;
    for(uint32_t i = 0; i < 256; i++)
    {
        if( *addr != i)
        {
            result = false;
            break;
        }
        addr++;
    }
    if(result == true)
    {
        printf("\n\rBackup ram content matches");    
    }
    else
    {
        printf("\n\rBackup ram was not retained");
    }
}

void setup_RTC(void)
{
    struct tm sys_time;
    //15-01-2018 12:00:00 Monday
    sys_time.tm_hour = 12;
    sys_time.tm_sec = 00;
    sys_time.tm_min = 00;
    sys_time.tm_mon = 0;
    sys_time.tm_year = 18;
    sys_time.tm_mday = 15;
    sys_time.tm_wday = 1;

    
    //validate if RTC is already configured or not
    if(SUPC_GPBRRead(GPBR_REGS_0) != 1)
    {
        printf("\n\rConfiguring RTC");
        RTC_TimeSet(&sys_time);
        populate_backupram();
    }
    else
    {
        printf("\n\rRTC has been configured previously");
        validate_backupram();
    }
    
    //UPDATE GPBR_REGS_0 to 1 as a Flag for RTC configuration
    SUPC_GPBRWrite(GPBR_REGS_0, 0x1);
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
    
    setup_RTC();
    SYSTICK_TimerCallbackSet(&timeout, (uintptr_t) NULL);
    SYSTICK_TimerStart();
    
    display_menu();
    while(1)
    {
        switch(cmd)
        {
            case SLEEP_MODE:
            {
                printf("\n\n\rConfiguring RTC Alarm for wake up.......");
                configure_alarm();
                SYSTICK_TimerStop();
                printf("\n\rEntering SLEEP Mode");
                LED_OFF();
                SUPC_SleepModeEnter();
                printf("\n\rRTC ALARM triggered waking up device from Sleep Mode");
                SYSTICK_TimerStart();
                display_menu();
                break;
            }
            case WAIT_MODE:
            {
                printf("\n\n\rConfiguring RTC Alarm for wake up.......");
                configure_alarm();
                SYSTICK_TimerStop();
                printf("\n\rEntering WAIT Mode");
                LED_OFF();
                SUPC_WaitModeEnter (PMC_FSMR_FLPM_FLASH_DEEP_POWERDOWN, WAITMODE_WKUP_RTC);
                printf("\n\rRTC ALARM triggered waking up device from Wait Mode");
                SYSTICK_TimerStart();
                display_menu();
                break;
            }
            case BACKUP_MODE:
            {
                printf("\n\n\rConfiguring RTC Alarm for wake up.......");
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

