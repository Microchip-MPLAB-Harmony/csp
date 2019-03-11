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
#include <string.h>
#include "definitions.h"                // SYS function prototypes

#define READ_WRITE_SIZE         (NVM_FLASH_PAGESIZE)
#define BUFFER_SIZE             (READ_WRITE_SIZE / sizeof(uint32_t))

#define APP_FLASH_ADDRESS       (NVM_FLASH_START_ADDRESS + (NVM_FLASH_SIZE / 2))

#define LED_ON                  LED1_Set
#define LED_OFF                 LED1_Clear
#define LED_TOGGLE              LED1_Toggle

uint32_t writeData[BUFFER_SIZE] CACHE_ALIGN;
uint32_t readData[BUFFER_SIZE];

static volatile bool xferDone = false;

static void populate_buffer(void)
{
    uint32_t i = 0;

    for (i = 0; i < BUFFER_SIZE; i++)
    {
        writeData[i] = i;
    }
}

static void eventHandler(uintptr_t context)
{
    xferDone = true;
}

// *****************************************************************************
// *****************************************************************************
// Section: Main Entry Point
// *****************************************************************************
// *****************************************************************************

int main ( void )
{
    uint32_t address = APP_FLASH_ADDRESS;
    uint8_t *writePtr = (uint8_t *)writeData;
    uint32_t i = 0;

    /* Initialize all modules */
    SYS_Initialize ( NULL );

    /*Populate random data to programmed*/
    populate_buffer();

    NVM_CallbackRegister(eventHandler, (uintptr_t)NULL);
    
    while(NVM_IsBusy() == true);
    
    /* Erase the Page */
    NVM_PageErase(address);
    
    while(xferDone == false);
    
    xferDone = false;

    for (i = 0; i < READ_WRITE_SIZE; i+= NVM_FLASH_ROWSIZE)
    {
        /* Program a row of data */
        NVM_RowWrite((uint32_t *)writePtr, address);

        while(xferDone == false);

        xferDone = false;

        writePtr += NVM_FLASH_ROWSIZE;
        address  += NVM_FLASH_ROWSIZE;
    }
    
    NVM_Read(readData, sizeof(writeData), APP_FLASH_ADDRESS);

    /* Verify the programmed content*/
    if (!memcmp(writeData, readData, sizeof(writeData)))
    {
        LED_ON();
    }
    
    while ( true )
    {
    }

    /* Execution should not come here during normal operation */
    return ( EXIT_FAILURE );
}
