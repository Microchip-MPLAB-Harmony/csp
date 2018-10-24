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

const uint8_t nvm_user_start_address[NVMCTRL_FLASH_PAGESIZE] __attribute__((address(NVMCTRL_FLASH_START_ADDRESS+0x20000)))= {0};

void populate_buffer(uint8_t* data)
{
    int i = 0;

    for (i = 0; i < (NVMCTRL_FLASH_PAGESIZE); i++)
    {
        *(data + i) = i;
    }
}

// *****************************************************************************
// *****************************************************************************
// Section: Main Entry Point
// *****************************************************************************
// *****************************************************************************

int main ( void )
{
    uint8_t data [NVMCTRL_FLASH_PAGESIZE] = {0};    
    
    /* Initialize all modules */
    SYS_Initialize ( NULL );
    
    LED_OFF();

    /*Populate random data to programmed*/
    populate_buffer(data);    
    
    while(NVMCTRL_IsBusy());

    /* Erase the row */
    NVMCTRL_RowErase((uint32_t)nvm_user_start_address);

    while(NVMCTRL_IsBusy());

    /* Program 64 byte page */
    NVMCTRL_PageWrite((uint32_t *)data, (uint32_t)nvm_user_start_address);
    while(NVMCTRL_IsBusy());
    
    /* Verify the programmed content*/
    if (!memcmp(data, (void *)nvm_user_start_address, NVMCTRL_FLASH_PAGESIZE))
    {
        LED_ON();
    }
    
    while ( true )
    {
        /* Maintain state machines of all polled MPLAB Harmony modules. */
        SYS_Tasks ( );
    }

    /* Execution should not come here during normal operation */

    return ( EXIT_FAILURE );
}


/*******************************************************************************
 End of File
*/

