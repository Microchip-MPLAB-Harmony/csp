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
#include <string.h>                     // Defines String functions
#include "definitions.h"                // SYS function prototypes

#define BUFFER_SIZE             (128)
#define APP_EEPROM_ADDRESS      (0)

#define LED_ON                  LED1_Set
#define LED_OFF                 LED1_Clear
#define LED_TOGGLE              LED1_Toggle

uint32_t writeData[BUFFER_SIZE] CACHE_ALIGN;
uint32_t readData[BUFFER_SIZE];

volatile bool switch_pressed = false;

typedef enum {
    EEPROM_OPERATION_WORD_WRITE_READ_CMP = 0,
    EEPROM_OPERATION_PAGE_ERASE_READ_CMP,
    EEPROM_OPERATION_BULK_ERASE_READ_CMP,
    EEPROM_OPERATION_SUCCESS,
    EEPROM_OPERATION_ERROR
} EEPROM_OPERATION_STATE;

void switch_handler( GPIO_PIN pin, uintptr_t context )
{
    switch_pressed = true;
}

static void populate_buffer(void)
{
    uint32_t i = 0;

    for (i = 0; i < BUFFER_SIZE; i++)
    {
        writeData[i] = i;
    }
}

// *****************************************************************************
// *****************************************************************************
// Section: Main Entry Point
// *****************************************************************************
// *****************************************************************************

int main ( void )
{
    uint32_t i = 0;
    uint32_t address = APP_EEPROM_ADDRESS;
    bool result = false;

    EEPROM_OPERATION_STATE state = EEPROM_OPERATION_WORD_WRITE_READ_CMP;

    LED_OFF();

    /* Initialize all modules */
    SYS_Initialize ( NULL );

    /* Populate the EEPROM data to be programmed */
    populate_buffer();

    GPIO_PinInterruptCallbackRegister( SWITCH1_PIN, &switch_handler, ( uintptr_t ) NULL );
    GPIO_PinInterruptEnable( SWITCH1_PIN );
    switch_pressed = false;

    while ( true )
    {
        if(switch_pressed == true)
        {
            switch(state)
            {
                case EEPROM_OPERATION_WORD_WRITE_READ_CMP:
                {
                    /* Step 1: Write populated date to EEPROM */
                    for ( i = 0; i < BUFFER_SIZE; i++ )
                    {
                        result = EEPROM_WordWrite( address, writeData[i] );
                        if (result == true)
                        {
                            address = address + 4;
                        }
                        else
                        {
                            state = EEPROM_OPERATION_ERROR;
                            break;
                        }
                    }

                    /* Reset the start address of EEPROM */
                    address = APP_EEPROM_ADDRESS;

                    /* Step 2: Read-back the data from EEPROM */
                    for (  i = 0; i < BUFFER_SIZE; i++ )
                    {
                        result = EEPROM_WordRead( address, &readData[i] );
                        if (result == true)
                        {
                            address = address + 4;
                        }
                        else
                        {
                            state = EEPROM_OPERATION_ERROR;
                            break;
                        }
                    }

                    /* Step 3: Verify the programmed content */
                    if ( !memcmp( writeData, readData, sizeof( writeData ) ) )
                    {
                        state = EEPROM_OPERATION_PAGE_ERASE_READ_CMP;
                    }
                    else
                    {
                        state = EEPROM_OPERATION_ERROR;
                    }
                    break;
                }

                case EEPROM_OPERATION_PAGE_ERASE_READ_CMP:
                {
                    /* Step 4: Fill the writeData with 0xFFFFFFFF */
                    memset(&writeData, 0xFFFFFFFF, sizeof(writeData));

                    /* Reset the start address of EEPROM */
                    address = APP_EEPROM_ADDRESS;

                    /* Step 5: Erase EEPROM data */
                    for (  i = 0; i < BUFFER_SIZE; i++ )
                    {
                        result = EEPROM_PageErase( address );
                        address = address + 4;
                    }

                    /* Reset the start address of EEPROM */
                    address = APP_EEPROM_ADDRESS;

                    /* Step 6: Read-back the data from EEPROM */
                    for (  i = 0; i < BUFFER_SIZE; i++ )
                    {
                        result = EEPROM_WordRead( address, &readData[i] );
                        if (result == true)
                        {
                            address = address + 4;
                        }
                        else
                        {
                            state = EEPROM_OPERATION_ERROR;
                            break;
                        }
                    }

                    /* Step 7: Verify the programmed content */
                    if ( !memcmp( writeData, readData, sizeof( writeData ) ) )
                    {
                        state = EEPROM_OPERATION_BULK_ERASE_READ_CMP;
                    }
                    else
                    {
                        state = EEPROM_OPERATION_ERROR;
                    }
                    break;
                }

                case EEPROM_OPERATION_BULK_ERASE_READ_CMP:
                {
                    /* Populate the EEPROM data to be programmed */
                    populate_buffer();

                    /* Step 8: Write populated date to EEPROM */
                    for ( i = 0; i < BUFFER_SIZE; i++ )
                    {
                        result = EEPROM_WordWrite( address, writeData[i] );
                        if (result == true)
                        {
                            address = address + 4;
                        }
                        else
                        {
                            state = EEPROM_OPERATION_ERROR;
                            break;
                        }
                    }

                    /* Step 9: Erase EEPROM data */
                    result = EEPROM_BulkErase();
                    if (result != true)
                    {
                        state = EEPROM_OPERATION_ERROR;
                        break;
                    }

                    /* Reset the start address of EEPROM */
                    address = APP_EEPROM_ADDRESS;

                    /* Step 10: Read-back the data from EEPROM */
                    for (  i = 0; i < BUFFER_SIZE; i++ )
                    {
                        result = EEPROM_WordRead( address, &readData[i] );
                        if (result == true)
                        {
                            address = address + 4;
                        }
                        else
                        {
                            state = EEPROM_OPERATION_ERROR;
                            break;
                        }
                    }

                    /* Fill the writeData with 0xFFFFFFFF */
                    memset(&writeData, 0xFFFFFFFF, sizeof(writeData));

                    /* Step 11: Verify whether the data is erased properly */
                    if ( !memcmp( writeData, readData, sizeof( writeData ) ) )
                    {
                        state = EEPROM_OPERATION_SUCCESS;
                    }
                    else
                    {
                        state = EEPROM_OPERATION_ERROR;
                    }
                    break;
                }

                case EEPROM_OPERATION_SUCCESS:
                {
                    LED_ON();
                    while(1);
                }

                case EEPROM_OPERATION_ERROR:
                default:
                {
                    LED_OFF();
                    while(1);
                }
            }
        }
        else // If switch is not pressed, turn off the LED
        {
            LED_OFF();
        }
    }

    /* Execution should not come here during normal operation */
    return ( EXIT_FAILURE );
}
