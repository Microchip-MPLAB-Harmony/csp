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
#define LED_On()                       LED_Clear()
#define LED_Off()                      LED_Set()

// *****************************************************************************
/* I2C Address for the EEPROM 3 CLICK Board.

  Summary:
    Defines the EEPROM 3 CLICK Board's I2C Address.

  Description:
    This #define defines the on-board EEPROM 3 CLICK Board's I2C Address. It is used
    by the TWIHS PLib API's to transmit and receive data.
*/

#define APP_AT24MAC_DEVICE_ADDR             0x0054

// *****************************************************************************
/* EEPROM AT24MAC402 Word Address.

  Summary:
    Defines the EEPROM 3 CLICK Board's Word Address.

  Description:
    This #define defines the EEPROM 3 CLICK Board's Word Address. Data is
    read/write from/to the location starting from this address.
 */

#define APP_AT24MAC_MEMORY_ADDR             0x00
#define APP_AT24MAC_MEMORY_ADDR1            0x00
// *****************************************************************************
/* Transmit data length.

  Summary:
    Defines the length of the data to be transmitted to EEPROM 3 CLICK Board.

  Description:
    This #define defines the length of the data to be tranmitted to the EEPROM 3 CLICK Board.
    This define is used by the TWIHS PLib Write API.
 */

#define APP_TRANSMIT_DATA_LENGTH            6

// *****************************************************************************
/* Acknowledge polling data length.

  Summary:
    Defines the length of the data to be transmitted to EEPROM 3 CLICK Board
    during Acknowledge polling.

  Description:
    This #define defines the length of the data to be tranmitted to the EEPROM 3 CLICK Board
    during Acknowledge polling. This define is used by the TWIHS
    PLib Write API.
 */

#define APP_ACK_DATA_LENGTH                 1

// *****************************************************************************
/* Dummy write data length.

  Summary:
    Defines the length of the dummy bytes to be written to read actual data.

  Description:
    This #define defines the length of the dummy bytes(actually Address bytes)to be written to read actual data from EEPROM 3 CLICK Board.
 *  This define is used by the TWIHS PLib Read API.
 */

#define APP_RECEIVE_DUMMY_WRITE_LENGTH           2

// *****************************************************************************
/* Receive data length.

  Summary:
    Defines the length of the data to be received from EEPROM 3 CLICK Board.

  Description:
    This #define defines the length of the data to be received from the EEPROM 3 CLICK Board.
 *  This define is used by the TWIHS PLib Read API.
 */

#define APP_RECEIVE_DATA_LENGTH           4

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
    APP_AT24MAC_MEMORY_ADDR,APP_AT24MAC_MEMORY_ADDR1,
    'M','C','H','P',
};

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
    APP_STATE_EEPROM_WAIT_WRITE_COMPLETE,
    APP_STATE_EEPROM_CHECK_INTERNAL_WRITE_STATUS,
    APP_STATE_EEPROM_READ,
    APP_STATE_EEPROM_WAIT_READ_COMPLETE,
    APP_STATE_VERIFY,
    APP_STATE_IDLE,
    APP_STATE_XFER_SUCCESSFUL,
    APP_STATE_XFER_ERROR

} APP_STATES;

// *****************************************************************************
/* Transfer status enum

  Summary:
    Enumerator to define transfer status.

  Description:
    This enumerator defines all the possible transfer states.

  Remarks:
    None.
*/
typedef enum
{
    APP_TRANSFER_STATUS_IN_PROGRESS,
    APP_TRANSFER_STATUS_SUCCESS,
    APP_TRANSFER_STATUS_ERROR,
    APP_TRANSFER_STATUS_IDLE,

} APP_TRANSFER_STATUS;

// *****************************************************************************
// *****************************************************************************
// Section: Local functions
// *****************************************************************************
// *****************************************************************************

/* This function will be called by I2C PLIB when transfer is completed */
// *****************************************************************************
/* void APP_I2CCallback(uintptr_t context)

  Summary:
    Function called by I2C PLIB upon transfer completion

  Description:
    This function will be called by I2C PLIB when transfer is completed.
    In this function, current state of the application is obtained by context
    parameter. Based on current state of the application and I2C error
    state, next state of the application is decided.

  Remarks:
    None.
*/
void APP_I2CCallback(uintptr_t context )
{
    APP_TRANSFER_STATUS* transferStatus = (APP_TRANSFER_STATUS*)context;

    if(SERCOM1_I2C_ErrorGet() == SERCOM_I2C_ERROR_NONE)
    {
        if (transferStatus)
        {
            *transferStatus = APP_TRANSFER_STATUS_SUCCESS;
        }
    }
    else
    {
        if (transferStatus)
        {
            *transferStatus = APP_TRANSFER_STATUS_ERROR;
        }
    }
}

// *****************************************************************************
// *****************************************************************************
// Section: Main Entry Point
// *****************************************************************************
// *****************************************************************************

int main ( void )
{
    APP_STATES state = APP_STATE_EEPROM_STATUS_VERIFY;
    volatile APP_TRANSFER_STATUS transferStatus = APP_TRANSFER_STATUS_ERROR;
    uint8_t ackData = 0;

    /* Initialize all modules */
    SYS_Initialize ( NULL );

    while(1)
    {
        /* Check the application's current state. */
        switch (state)
        {
            case APP_STATE_EEPROM_STATUS_VERIFY:

                /* Register the TWIHS Callback with transfer status as context */
                SERCOM1_I2C_CallbackRegister( APP_I2CCallback, (uintptr_t)&transferStatus );

               /* Verify if EEPROM is ready to accept new requests */
                transferStatus = APP_TRANSFER_STATUS_IN_PROGRESS;
                SERCOM1_I2C_Write(APP_AT24MAC_DEVICE_ADDR, &ackData, APP_ACK_DATA_LENGTH);

                state = APP_STATE_EEPROM_WRITE;
                break;

            case APP_STATE_EEPROM_WRITE:

                if (transferStatus == APP_TRANSFER_STATUS_SUCCESS)
                {
                    /* Write data to EEPROM */
                    transferStatus = APP_TRANSFER_STATUS_IN_PROGRESS;
                    SERCOM1_I2C_Write(APP_AT24MAC_DEVICE_ADDR, &testTxData[0], APP_TRANSMIT_DATA_LENGTH);
                    state = APP_STATE_EEPROM_WAIT_WRITE_COMPLETE;
                }
                else if (transferStatus == APP_TRANSFER_STATUS_ERROR)
                {
                    /* EEPROM is not ready to accept new requests */
                    state = APP_STATE_XFER_ERROR;
                }
                break;

            case APP_STATE_EEPROM_WAIT_WRITE_COMPLETE:

                if (transferStatus == APP_TRANSFER_STATUS_SUCCESS)
                {
                    /* Read the status of internal write cycle */
                    transferStatus = APP_TRANSFER_STATUS_IN_PROGRESS;
                    SERCOM1_I2C_Write(APP_AT24MAC_DEVICE_ADDR, &ackData, APP_ACK_DATA_LENGTH);
                    state = APP_STATE_EEPROM_CHECK_INTERNAL_WRITE_STATUS;
                }
                else if (transferStatus == APP_TRANSFER_STATUS_ERROR)
                {
                    state = APP_STATE_XFER_ERROR;
                }
                break;

             case APP_STATE_EEPROM_CHECK_INTERNAL_WRITE_STATUS:

                if (transferStatus == APP_TRANSFER_STATUS_SUCCESS)
                {
                    state = APP_STATE_EEPROM_READ;
                }
                else if (transferStatus == APP_TRANSFER_STATUS_ERROR)
                {
                    /* EEPROM's internal write cycle is not complete. Keep checking. */
                    transferStatus = APP_TRANSFER_STATUS_IN_PROGRESS;
                    SERCOM1_I2C_Write(APP_AT24MAC_DEVICE_ADDR, &ackData, APP_ACK_DATA_LENGTH);
                }
                break;

            case APP_STATE_EEPROM_READ:

                transferStatus = APP_TRANSFER_STATUS_IN_PROGRESS;
                /* Read the data from the page written earlier */
                SERCOM1_I2C_WriteRead(APP_AT24MAC_DEVICE_ADDR, &testTxData[0], APP_RECEIVE_DUMMY_WRITE_LENGTH,  &testRxData[0], APP_RECEIVE_DATA_LENGTH);

                state = APP_STATE_EEPROM_WAIT_READ_COMPLETE;

                break;

            case APP_STATE_EEPROM_WAIT_READ_COMPLETE:

                if (transferStatus == APP_TRANSFER_STATUS_SUCCESS)
                {
                    state = APP_STATE_VERIFY;
                }
                else if (transferStatus == APP_TRANSFER_STATUS_ERROR)
                {
                    state = APP_STATE_XFER_ERROR;
                }
                break;

            case APP_STATE_VERIFY:

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

            case APP_STATE_XFER_SUCCESSFUL:
            {
                LED_On();
                break;
            }
            case APP_STATE_XFER_ERROR:
            {
                LED_Off();
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

