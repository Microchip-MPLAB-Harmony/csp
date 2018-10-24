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
    APP_STATE_DATA_COMPARISON,
    APP_STATE_XFER_SUCCESSFUL,
    APP_STATE_XFER_ERROR

} APP_STATES;

/* EEPROM Commands */
#define EEPROM_CMD_WREN                     0x06
#define EEPROM_CMD_WRITE                    0x02
#define EEPROM_CMD_RDSR                     0x05
#define EEPROM_CMD_READ                     0x03

#define EEPROM_ADDRESS                      0x000000
#define LED_On()                            LED_Clear()
#define LED_Off()                           LED_Set()

#define EEPROM_DATA                         "WRITING AND READING DATA FROM EEPROM!"
#define EEPROM_DATA_LEN                     sizeof(EEPROM_DATA)

/* Global variables */

// EEPROM CMD (1) + EEPROM ADDR (3) + EEPROM_DATA_LEN
uint8_t  txData[(4 + EEPROM_DATA_LEN)];
uint8_t  rxData[(4 + EEPROM_DATA_LEN)];
volatile bool isTransferDone = false;
APP_STATES state = APP_STATE_INITIALIZE;

/* This function will be called by SPI PLIB when transfer is completed */
void SPIEventHandler(uintptr_t context )
{
    /* De-assert the chip select */
    EEPROM_CS_Set();

    isTransferDone = true;
}

void EEPROM_Initialize (void)
{
    EEPROM_HOLD_Set();
    EEPROM_WP_Set();
    EEPROM_CS_Set();
    LED_Off();
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
                EEPROM_Initialize();
                /* Register callback with the SPI PLIB */
                SERCOM5_SPI_CallbackRegister(SPIEventHandler, (uintptr_t) 0);
                state = APP_STATE_EEPROM_WRITE_ENABLE;
                break;

            case APP_STATE_EEPROM_WRITE_ENABLE:
                // Enable Writes to EEPROM
                txData[0] = EEPROM_CMD_WREN;
                EEPROM_CS_Clear();
                SERCOM5_SPI_Write(txData, 1);
                state = APP_STATE_EEPROM_WRITE;
                break;

            case APP_STATE_EEPROM_WRITE:
                if (isTransferDone == true)
                {
                    isTransferDone = false;
                    //Copy the write command and the memory address to write to
                    txData[0] = EEPROM_CMD_WRITE;
                    txData[1] = (uint8_t)(eepromAddr>>16);
                    txData[2] = (uint8_t)(eepromAddr>>8);
                    txData[3] = (uint8_t)(eepromAddr);
                    //Copy the data to be written to EEPROM
                    memcpy(&txData[4], EEPROM_DATA, EEPROM_DATA_LEN);
                    EEPROM_CS_Clear();
                    SERCOM5_SPI_Write(txData, (4 + EEPROM_DATA_LEN));
                    state = APP_STATE_EEPROM_READ_STATUS;
                }
                break;

            case APP_STATE_EEPROM_READ_STATUS:
                if (isTransferDone == true)
                {
                    isTransferDone = false;
                    /* Read the status of the internal write operation  */
                    txData[0] = EEPROM_CMD_RDSR;
                    EEPROM_CS_Clear();
                    SERCOM5_SPI_WriteRead(txData, 1, rxData, 2);
                    state = APP_STATE_EEPROM_CHECK_STATUS;
                }
                break;

            case APP_STATE_EEPROM_CHECK_STATUS:
                if (isTransferDone == true)
                {
                    isTransferDone = false;
                    if(!(rxData[1] & 0x01))
                    {
                        /* It means write has been completed */
                        state = APP_STATE_EEPROM_READ;
                    }
                    else
                    {
                        // Keep reading the status of the internal write operation
                        txData[0] = EEPROM_CMD_RDSR;
                        EEPROM_CS_Clear();
                        SERCOM5_SPI_WriteRead(txData, 1, rxData, 2);
                    }
                }
                break;

            case APP_STATE_EEPROM_READ:

                // Copy the read command and the memory address to read from
                txData[0] = EEPROM_CMD_READ;
                txData[1] = (uint8_t)(eepromAddr>>16);
                txData[2] = (uint8_t)(eepromAddr>>8);
                txData[3] = (uint8_t)(eepromAddr);

                EEPROM_CS_Clear();
                SERCOM5_SPI_WriteRead(txData, 4, rxData, (4 + EEPROM_DATA_LEN));
                state = APP_STATE_DATA_COMPARISON;

                break;

            case APP_STATE_DATA_COMPARISON:
                if (isTransferDone == true)
                {
                    isTransferDone = false;
                    if (memcmp(&txData[4], &rxData[4], EEPROM_DATA_LEN) != 0)
                    {
                        /* It means received data is not same as transmitted data */
                        state = APP_STATE_XFER_ERROR;
                    }
                    else
                    {
                        /* It means received data is same as transmitted data */
                        state = APP_STATE_XFER_SUCCESSFUL;
                    }
                }
                break;

            case APP_STATE_XFER_SUCCESSFUL:
                LED_On();
                break;

            case APP_STATE_XFER_ERROR:
                LED_Off();
                break;

            default:
                break;
        }
    }
}

/*******************************************************************************
 End of File
*/