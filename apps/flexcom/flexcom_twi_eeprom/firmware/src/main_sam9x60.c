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
#include "definitions.h"                // SYS function prototypes
#include <string.h>

/*************************************************************************************
FLEXCOM TWI   - Connect EEPROM 3 click board to mikrobus Connector.
*************************************************************************************/

#define LED_ON()                       LED_GREEN_Set()
#define LED_OFF()                      LED_GREEN_Clear()

// *****************************************************************************
/* I2C Address for the EEPROM 3 click board.

  Summary:
    Defines the EEPROM 3 click board's I2C Address.

  Description:
    This macro defines the EEPROM 3 click board's I2C Address. 
*/

#define APP_AT24CM_DEVICE_ADDR             (0x54)

// *****************************************************************************
/* EEPROM 3 click board (AT24CM02) memory address.

  Summary:
    Defines the EEPROM 3 click board (AT24CM02) memory address.

  Description:
    This macro defines the EEPROM 3 click board (AT24CM02) memory Address.
    Data is read/write from/to the location starting from this address.
 */

#define APP_AT24CM_MEMORY_ADDR             (0x0000)
#define APP_AT24CM_HIGH_MEMORY_ADDR        ((APP_AT24CM_MEMORY_ADDR >> 8) & 0xffu)
#define APP_AT24CM_LOW_MEMORY_ADDR         (APP_AT24CM_MEMORY_ADDR & 0xffu)

// *****************************************************************************
/* Transmit data length.

  Summary:
    Defines the length of the data to be transmitted to EEPROM 3 click board.

  Description:
    This macro defines the size of one page on the AT24 EEPROM.
 */

#define APP_AT24MAC_PAGE_SIZE               (20)

// *****************************************************************************
/* Transmit data length.

  Summary:
    Defines the length of the data to be transmitted to EEPROM 3 click board.

  Description:
    This macro defines the length of the data to be tranmitted to the 
    EEPROM 3 click board (AT24CM02). The length must be sufficient to hold the
    data and the AT24 memory address.
 */

#define APP_TRANSMIT_DATA_LENGTH            (APP_AT24MAC_PAGE_SIZE + 2)

// *****************************************************************************
/* Receive data length.

  Summary:
    Defines the length of the data to be received from EEPROM 3 click board.

  Description:
    This macro defines the length of the data to be received from the
    EEPROM 3 click board (AT24CM02). 
 */

#define APP_RECEIVE_DATA_LENGTH             (APP_AT24MAC_PAGE_SIZE)

// *****************************************************************************
/* Acknowledge polling data length.

  Summary:
    Defines the length of the data to be transmitted to EEPROM 3 click board
    during Acknowledge polling.

  Description:
    This macro defines the length of the data to be tranmitted to the
    EEPROM 3 click board (AT24CM02) during Acknowledge polling. This define is
    used by the FLEXCOM TWI PLib Write API.
 */

#define APP_ACK_DATA_LENGTH                 (1)

// *****************************************************************************
/* Application Test Transmit Data array

  Summary:
    Holds the application test transmit data.

  Description:
    This array holds the application's test transmit data.

  Remarks:
    None.
*/

static uint8_t testTxData[APP_TRANSMIT_DATA_LENGTH] =
{
    APP_AT24CM_HIGH_MEMORY_ADDR, APP_AT24CM_LOW_MEMORY_ADDR,
    'S', 'A', 'M', ' ', 'F', 'L', 'E', 'X', 'C', 'O', 'M', ' ',
    'T', 'W', 'I', ' ', 'D', 'e', 'm', 'o'
};

// *****************************************************************************
/* Application Acknowledge polling Data byte.

  Summary:
    Holds the application acknowledge polling data byte.

  Description:
    This array holds the application's acknowledge polling data byte.

  Remarks:
    None.
*/

static uint8_t ackData = 0;

// *****************************************************************************
/* Application Test receive Data array.

  Summary:
    Holds the application received test data.

  Description:
    This array holds the application's received test data.

  Remarks:
    None.
*/

static uint8_t  testRxData[APP_RECEIVE_DATA_LENGTH];

// *****************************************************************************
/* Application's state machine enum 

  Summary:
    Enumerator to define app states.

  Description:
    This enumerator defines all the possible application states.

  Remarks:
    None.
*/
typedef enum
{    
    APP_STATE_EEPROM_STATUS_VERIFY,
    APP_STATE_EEPROM_WRITE,
    APP_STATE_EEPROM_READ_STATUS,
    APP_STATE_EEPROM_READ,
    APP_STATE_IDLE,
    APP_STATE_DATA_COMPARISON,
    APP_STATE_XFER_SUCCESSFUL,
    APP_STATE_XFER_ERROR
            
} APP_STATES;

// *****************************************************************************
// *****************************************************************************
// Section: Local functions
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Application's state variable 

  Summary:
    Variable to save application state

  Description:
    This variable holds the current state information of the application.
    It is initialized with the first state of the application.

  Remarks:
    None.
*/
volatile APP_STATES state = APP_STATE_EEPROM_STATUS_VERIFY;

// *****************************************************************************
// *****************************************************************************
// Section: Local functions
// *****************************************************************************
// *****************************************************************************

/* This function will be called by FLEXCOM TWI PLIB when transfer is completed */
// *****************************************************************************
/* void APP_FLEXCOM_TWI_Callback(uintptr_t context)

  Summary:
    Function called by FLEXCOM TWI PLIB upon transfer completion

  Description:
    This function will be called by FLEXCOM TWI PLIB when transfer is completed.
    In this function, current state of the application is obtained by context
    parameter. Based on current state of the application and FLEXCOM TWI error
    state, next state of the application is decided.

  Remarks:
    None.
*/
void APP_FLEXCOM_TWI_Callback(uintptr_t context )
{
    if ((FLEXCOM0_TWI_ErrorGet() != FLEXCOM_TWI_ERROR_NONE) && ((APP_STATES)context == APP_STATE_EEPROM_READ_STATUS))
    {
        state = APP_STATE_EEPROM_READ_STATUS;
    }
    else if(FLEXCOM0_TWI_ErrorGet() == FLEXCOM_TWI_ERROR_NONE)
    {
        switch ((APP_STATES)context)
        {
            case APP_STATE_EEPROM_STATUS_VERIFY:
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
                state = APP_STATE_EEPROM_READ;
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
    else
    {
        state = APP_STATE_XFER_ERROR;
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

    LED_RED_Clear();
    LED_GREEN_Clear();
    LED_BLUE_Clear();

    while(1)
    {
        /* Check the application's current state. */
        switch (state)
        {
            case APP_STATE_EEPROM_STATUS_VERIFY:
            {
                /* Register the FLEXCOM TWI Callback with current state as context */
                FLEXCOM0_TWI_CallbackRegister( APP_FLEXCOM_TWI_Callback, (uintptr_t)APP_STATE_EEPROM_STATUS_VERIFY );

                state = APP_STATE_IDLE;

                /* verify if EEPROM is free */
                FLEXCOM0_TWI_Write(APP_AT24CM_DEVICE_ADDR, &ackData, APP_ACK_DATA_LENGTH);

                break;
            }
            case APP_STATE_EEPROM_WRITE:
            {
                FLEXCOM0_TWI_CallbackRegister( APP_FLEXCOM_TWI_Callback, (uintptr_t)APP_STATE_EEPROM_WRITE );
                state = APP_STATE_IDLE;
                
                /* writes data into EEPROM page */
                FLEXCOM0_TWI_Write(APP_AT24CM_DEVICE_ADDR, &testTxData[0], APP_TRANSMIT_DATA_LENGTH);
                
                break;
            }
            case APP_STATE_EEPROM_READ_STATUS:
            {
                FLEXCOM0_TWI_CallbackRegister( APP_FLEXCOM_TWI_Callback, (uintptr_t)APP_STATE_EEPROM_READ_STATUS );
                state = APP_STATE_IDLE;
                
                /* Checks whether EEPROM's write cycle is complete */
                FLEXCOM0_TWI_Write(APP_AT24CM_DEVICE_ADDR, &testTxData[0], 2);

                break;
            }

            case APP_STATE_EEPROM_READ:
            {
                FLEXCOM0_TWI_CallbackRegister( APP_FLEXCOM_TWI_Callback, (uintptr_t)APP_STATE_EEPROM_READ );
                state = APP_STATE_IDLE;

                /* Read the data from the page written earlier */
                FLEXCOM0_TWI_Read(APP_AT24CM_DEVICE_ADDR, &testRxData[0], APP_RECEIVE_DATA_LENGTH);
                
                break;
            }
            case APP_STATE_IDLE:
            {
                /* Application can do other task here */
                break;
            }
            case APP_STATE_DATA_COMPARISON:
            {
                if (memcmp(&testTxData[2], &testRxData[0], APP_RECEIVE_DATA_LENGTH != 0))
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
                LED_ON();
                break;
            }
            case APP_STATE_XFER_ERROR:
            {
                LED_OFF();
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

