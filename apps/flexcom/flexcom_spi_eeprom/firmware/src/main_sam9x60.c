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

/*************************************************************************************
FLEXCOM SPI   - Connect EEPROM 4 click board to mikrobus Connector.
*************************************************************************************/

/* EEPROM Commands */
#define EEPROM_CMD_WREN                     0x06
#define EEPROM_CMD_WRITE                    0x02
#define EEPROM_CMD_RDSR                     0x05
#define EEPROM_CMD_READ                     0x03

#define EEPROM_ADDRESS                      0x000000
#define LED_On()                            LED_GREEN_Set()
#define LED_Off()                           LED_GREEN_Clear()

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

/* Global variables */
uint8_t  txData[]  = "----WRITING AND READING DATA FROM EEPROM!";
uint8_t  rxData[sizeof(txData)];
volatile APP_STATES state = APP_STATE_INITIALIZE;

/* This function will be called by FLEXCOM SPI PLIB when transfer is completed */
void FLEXCOM_SPI_EventHandler(uintptr_t context )
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
    LED_RED_Clear();
    LED_GREEN_Clear();
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

                /* Register FLEXCOM SPI Callback with current state as context */
                FLEXCOM4_SPI_CallbackRegister(&FLEXCOM_SPI_EventHandler, (uintptr_t)APP_STATE_EEPROM_WRITE_ENABLE);
                state = APP_STATE_IDLE;

                EEPROM_CS_Clear();
                FLEXCOM4_SPI_WriteRead(txData, 1, 0, 0);

                break;
            }
            case APP_STATE_EEPROM_WRITE:
            {
                //Write to EEPROM
                txData[0] = EEPROM_CMD_WRITE;
                txData[1] = (uint8_t)(eepromAddr>>16);
                txData[2] = (uint8_t)(eepromAddr>>8);
                txData[3] = (uint8_t)(eepromAddr);

                FLEXCOM4_SPI_CallbackRegister(&FLEXCOM_SPI_EventHandler, (uintptr_t)APP_STATE_EEPROM_WRITE);
                state = APP_STATE_IDLE;
                EEPROM_CS_Clear();
                FLEXCOM4_SPI_WriteRead(txData, sizeof(txData), 0, 0);
                break;
            }
            case APP_STATE_EEPROM_READ_STATUS:
            {
                /* Read Status  */
                txData[0] = EEPROM_CMD_RDSR;
                FLEXCOM4_SPI_CallbackRegister(&FLEXCOM_SPI_EventHandler, (uintptr_t)APP_STATE_EEPROM_READ_STATUS);
                state = APP_STATE_IDLE;

                EEPROM_CS_Clear();
                FLEXCOM4_SPI_WriteRead(txData, 1, rxData, 2);
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

                FLEXCOM4_SPI_CallbackRegister(&FLEXCOM_SPI_EventHandler, (uintptr_t)APP_STATE_EEPROM_READ);
                state = APP_STATE_IDLE;
                EEPROM_CS_Clear();
                FLEXCOM4_SPI_WriteRead(txData, 4, rxData, sizeof(rxData));
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
                LED_On();            // To turn on LED_GREEN
                EEPROM_HOLD_Clear(); // To turn off LED_BLUE
                break;
            }
            case APP_STATE_XFER_ERROR:
            {
                LED_Off();           // To turn off LED_GREEN
                EEPROM_HOLD_Clear(); // To turn off LED_BLUE
                break;
            }
            default:
                break;
        }
    }
    /* Execution should not come here during normal operation */

    return ( EXIT_FAILURE );
}

/*******************************************************************************
 End of File
*/