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
Copyright (c) 2018 released Microchip Technology Inc.  All rights reserved.

Microchip licenses to you the right to use, modify, copy and distribute
Software only when embedded on a Microchip microcontroller or digital signal
controller that is integrated into your product or third party product
(pursuant to the sublicense terms in the accompanying license agreement).

You should refer to the license agreement accompanying this Software for
additional information regarding your rights and obligations.

SOFTWARE AND DOCUMENTATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND,
EITHER EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION, ANY WARRANTY OF
MERCHANTABILITY, TITLE, NON-INFRINGEMENT AND FITNESS FOR A PARTICULAR PURPOSE.
IN NO EVENT SHALL MICROCHIP OR ITS LICENSORS BE LIABLE OR OBLIGATED UNDER
CONTRACT, NEGLIGENCE, STRICT LIABILITY, CONTRIBUTION, BREACH OF WARRANTY, OR
OTHER LEGAL EQUITABLE THEORY ANY DIRECT OR INDIRECT DAMAGES OR EXPENSES
INCLUDING BUT NOT LIMITED TO ANY INCIDENTAL, SPECIAL, INDIRECT, PUNITIVE OR
CONSEQUENTIAL DAMAGES, LOST PROFITS OR LOST DATA, COST OF PROCUREMENT OF
SUBSTITUTE GOODS, TECHNOLOGY, SERVICES, OR ANY CLAIMS BY THIRD PARTIES
(INCLUDING BUT NOT LIMITED TO ANY DEFENSE THEREOF), OR OTHER SIMILAR COSTS.
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
#include <string.h>


/* Application's state machine enum */
typedef enum
{
	APP_STATE_INITIALIZE,
    APP_STATE_EEPROM_WRITE_ENABLE,
    APP_STATE_EEPROM_WRITE,
    APP_STATE_EEPROM_READ_STATUS,
    APP_STATE_EEPROM_CHECK_STATUS,
    APP_STATE_EEPROM_READ,
    APP_STATE_IDLE,
    APP_STATE_DATA_COMPARISON,
    APP_STATE_XFER_SUCCESSFUL,
    APP_STATE_XFER_ERROR

} APP_STATES;

/* EEPROM Commands */
#define EEPROM_CMD_WREN                       0x06
#define EEPROM_CMD_WRITE                      0x02
#define EEPROM_CMD_RDSR                       0x05
#define EEPROM_CMD_READ                       0x03

#define EEPROM_ADDRESS                        0x000000


/* Global variables */
uint8_t  txData[]  = "----WRITING AND READING DATA FROM EEPROM!";
uint8_t  rxData[sizeof(txData)];
volatile APP_STATES state = APP_STATE_INITIALIZE;

/* This function will be called by SPI PLIB when transfer is completed */
void SPIEventHandler(uintptr_t context )
{
    /* De-assert the chip select */
    EEPROM_CS_Set();

    /* Change application state based on current state.
     * Context has current state value passed while registering the callbacks.*/
    switch ((APP_STATES)context)
    {
        case APP_STATE_EEPROM_WRITE_ENABLE:
        {
            state = APP_STATE_EEPROM_WRITE;
            break;
        }
        case APP_STATE_EEPROM_WRITE:
        {
            state = APP_STATE_EEPROM_READ_STATUS;
            break;
        }
        case APP_STATE_EEPROM_READ_STATUS:
        {
            state = APP_STATE_EEPROM_CHECK_STATUS;
            break;
        }
        case APP_STATE_EEPROM_READ:
        {
            state = APP_STATE_DATA_COMPARISON;
            break;
        }
        default:
            break;
    }
}

void EEPROM_Initialize (void)
{
    EEPROM_HOLD_Set();
    EEPROM_WP_Set();
    EEPROM_CS_Set();
}
// *****************************************************************************
// *****************************************************************************
// Section: Main Entry Point
// *****************************************************************************
// *****************************************************************************

int main ( void )
{
    uint32_t eepromAddr = EEPROM_ADDRESS;

    /* Initialize all modules */
    SYS_Initialize ( NULL );

    while(1)
    {
        /* Check the application's current state. */
        switch (state)
        {
            case APP_STATE_INITIALIZE:
            {
                EEPROM_Initialize();

                state = APP_STATE_EEPROM_WRITE_ENABLE;
            }
            case APP_STATE_EEPROM_WRITE_ENABLE:
            {
                //Enable Writes to EEPROM
                txData[0] = EEPROM_CMD_WREN;

                /* Register SPI Callback with current state as context */
                SPI0_CallbackRegister(&SPIEventHandler, (uintptr_t)APP_STATE_EEPROM_WRITE_ENABLE);
                state = APP_STATE_IDLE;

                EEPROM_CS_Clear();
                SPI0_Write(txData, 1);

                break;
            }
            case APP_STATE_EEPROM_WRITE:
            {
                //Write to EEPROM
                txData[0] = EEPROM_CMD_WRITE;
                txData[1] = (uint8_t)(eepromAddr>>16);
                txData[2] = (uint8_t)(eepromAddr>>8);
                txData[3] = (uint8_t)(eepromAddr);

                SPI0_CallbackRegister(&SPIEventHandler, (uintptr_t)APP_STATE_EEPROM_WRITE);
                state = APP_STATE_IDLE;
                EEPROM_CS_Clear();
                SPI0_Write(txData, sizeof(txData));
                break;
            }
            case APP_STATE_EEPROM_READ_STATUS:
            {
                /* Read Status  */
                txData[0] = EEPROM_CMD_RDSR;
                SPI0_CallbackRegister(&SPIEventHandler, (uintptr_t)APP_STATE_EEPROM_READ_STATUS);
                state = APP_STATE_IDLE;

                EEPROM_CS_Clear();
                SPI0_WriteRead(txData, 1, rxData, 2);
                break;
            }
            case APP_STATE_EEPROM_CHECK_STATUS:
            {
                if(!(rxData[1] & 0x01))
                {
                    /* It means write has been completed */
                    state = APP_STATE_EEPROM_READ;
                }
                else
                {
                    state = APP_STATE_EEPROM_READ_STATUS;
                }
                break;
            }
            case APP_STATE_EEPROM_READ:
            {
                //Read from EEPROM
                txData[0] = EEPROM_CMD_READ;
                txData[1] = (uint8_t)(eepromAddr>>16);
                txData[2] = (uint8_t)(eepromAddr>>8);
                txData[3] = (uint8_t)(eepromAddr);

                SPI0_CallbackRegister(&SPIEventHandler, (uintptr_t)APP_STATE_EEPROM_READ);
                state = APP_STATE_IDLE;
                EEPROM_CS_Clear();
                SPI0_WriteRead(txData, 4, rxData, sizeof(rxData));
                break;
            }
            case APP_STATE_IDLE:
            {
                /* Application can do other task here */
                break;
            }
            case APP_STATE_DATA_COMPARISON:
            {
                if (memcmp(&txData[4], &rxData[4], sizeof(txData)-4) != 0)
                {
                    /* It means received data is not same as transmitted data */
                    state = APP_STATE_XFER_ERROR;
                }
                else
                {
                    /* It means received data is same as transmitted data */
                    state = APP_STATE_XFER_SUCCESSFUL;
                }
                break;
            }
            case APP_STATE_XFER_SUCCESSFUL:
            {
                LED2_Clear();
                break;
            }
            case APP_STATE_XFER_ERROR:
            {
                LED2_Set();
                break;
            }
            default:
                break;
        }
    }
}

/*******************************************************************************
 End of File
*/