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

#define LED_ON                      LED_Clear
#define LED_OFF                     LED_Set
#define LED_TOGGLE                  LED_Toggle

const uint8_t nvm_user_start_address[NVMCTRL_FLASH_ROWSIZE] __attribute__((address(NVMCTRL_FLASH_START_ADDRESS+0x20000)))= {0};
const uint8_t nvm_rwwee_user_start_address[NVMCTRL_RWWEEPROM_ROWSIZE] __attribute__((address(NVMCTRL_RWWEEPROM_START_ADDRESS)))= {0};

// *****************************************************************************
// *****************************************************************************
// Section: Main Entry Point
// *****************************************************************************
// *****************************************************************************

int main ( void )
{   
    uint32_t main_read_flag = 0;
    uint32_t rweee_read_flag = 0;
    
    /* Initialize all modules */
    SYS_Initialize ( NULL );
    SYSTICK_TimerStart();
    LED_OFF();
        
    while(NVMCTRL_IsBusy());

    NVMCTRL_RowErase((uint32_t)nvm_user_start_address);
    
    while(NVMCTRL_IsBusy())
    {
        main_read_flag++;
    }
    
    
    NVMCTRL_RWWEEPROM_RowErase((uint32_t)nvm_rwwee_user_start_address);
    while(NVMCTRL_IsBusy())
    {
        rweee_read_flag++;
    }
    
    printf("Value of Flag incremented while erase is happening from main flash area = %ld \r\n", main_read_flag);
    printf("Value of Flag incremented while erase is happening from RWWEE flash area = %ld \r\n", rweee_read_flag);
    
    while ( true )
    {
        /* Maintain state machines of all polled MPLAB Harmony modules. */
        SYS_Tasks ( );

        if(rweee_read_flag > 0)
        {
            SYSTICK_DelayMs(1000);
            LED_TOGGLE();            
        }
    }

    /* Execution should not come here during normal operation */

    return ( EXIT_FAILURE );
}


/*******************************************************************************
 End of File
*/

