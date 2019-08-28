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

typedef enum {
    EEPROM_OPERATION_WORD_WRITE_READ_CMP = 0,
    EEPROM_OPERATION_PAGE_ERASE_READ_CMP,
    EEPROM_OPERATION_BULK_ERASE_READ_CMP,
    EEPROM_OPERATION_SUCCESS,
    EEPROM_OPERATION_ERROR,
    EEPROM_OPERATION_IDLE
} EEPROM_OPERATION_STATE;


static void populate_buffer(void)
{
    uint32_t i = 0;

    for (i = 0; i < BUFFER_SIZE; i++)
    {
        writeData[i] = i;
    }
}

static void APP_EepromWordWrite(uint32_t address)
{
    uint32_t i = 0;

    /* Populate buffer before writing to EEPROM */
    populate_buffer();

    for ( i = 0; i < BUFFER_SIZE; i++ )
    {
        EEPROM_WordWrite( address, writeData[i] );
        while ( EEPROM_IsBusy() == true );
        address = address + 4;
    }
}

static void APP_EepromWordRead(uint32_t address)
{
    uint32_t i = 0;

    for (  i = 0; i < BUFFER_SIZE; i++ )
    {
        EEPROM_WordRead( address, &readData[i] );
        while ( EEPROM_IsBusy() == true );
        address = address + 4;
    }
}

static void APP_EepromPageErase(uint32_t address)
{
    uint32_t i = 0;

    for (  i = 0; i < BUFFER_SIZE; i++ )
    {
        EEPROM_PageErase( address );
        while ( EEPROM_IsBusy() == true );
        address = address + 4;
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

    LED_OFF();

    /* Check whether EEPROM is busy */
    while ( EEPROM_IsBusy() == true );

    EEPROM_OPERATION_STATE state = EEPROM_OPERATION_WORD_WRITE_READ_CMP;

    while (true)
    {
        switch(state)
        {
            case EEPROM_OPERATION_WORD_WRITE_READ_CMP:
            {
                /* Populate buffer and Write data to EEPROM */
                APP_EepromWordWrite(APP_EEPROM_ADDRESS);

                /* Read the data from EEPROM */
                APP_EepromWordRead(APP_EEPROM_ADDRESS);

                /* Verify the programmed data */
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
                /* Fill the writeData with 0xFFFFFFFF */
                memset(&writeData, 0xFFFFFFFF, sizeof(writeData));

                /* Erase EEPROM data */
                APP_EepromPageErase(APP_EEPROM_ADDRESS);

                /* Read the data from EEPROM */
                APP_EepromWordRead(APP_EEPROM_ADDRESS);

                /* Verify the programmed data */
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
                /* Populate buffer and Write data to EEPROM */
                APP_EepromWordWrite(APP_EEPROM_ADDRESS);

                /* Bulk erase EEPROM */
                EEPROM_BulkErase();
                while ( EEPROM_IsBusy() == true );

                /* Read the data from EEPROM */
                APP_EepromWordRead(APP_EEPROM_ADDRESS);

                /* Fill the writeData with 0xFFFFFFFF */
                memset(&writeData, 0xFFFFFFFF, sizeof(writeData));

                /* Verify whether the data is erased properly */
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
                state = EEPROM_OPERATION_IDLE;
                break;
            }

            case EEPROM_OPERATION_ERROR:
            {
                LED_OFF();
                break;
            }

            case EEPROM_OPERATION_IDLE:
            default:
            {
               break;
            }
        }
    }
    /* Execution should not come here during normal operation */
    return ( EXIT_FAILURE );
}
