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

// Define a constant array in Flash.
// It must be aligned to block boundary and size has to be in multiple of blocks
const uint8_t nvm_user_start_address[NVMCTRL_FLASH_BLOCKSIZE] __attribute__((aligned(NVMCTRL_FLASH_BLOCKSIZE),keep,externally_visible,space(prog)))= {0};


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

    /* Erase the block */
    NVMCTRL_BlockErase((uint32_t)nvm_user_start_address);

    while(NVMCTRL_IsBusy());

    /* Program 512 byte page */
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

