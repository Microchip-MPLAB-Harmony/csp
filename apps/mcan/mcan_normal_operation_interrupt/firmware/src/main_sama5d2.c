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

/*************************************************************************************
MCAN - Connect ATA6563 click board to SAMA5D2 Xplained Ultra board as below.
       Connect CANTX0 (PC10) to TX (PIN 13) of ATA6563 click board
       Connect CANRX0 (PC11) to RX (PIN 14) of ATA6563 click board
       Connect GND, 5V and 3.3V to ATA6563 click board
       Connect Microchip CAN Bus Analyzer to PC using USB Male-A to Male Mini-B cable.
       Connect Microchip CAN Bus Analyzer to ATA6563 click board using female to female DB9 serial cable.
       Install Microchip CAN Bus Analyzer software on PC.
MCAN - Normal operation mode, MCAN clock source is 8 MHz and bitrate is 500 Kbps.
*************************************************************************************/

/* LED ON and OFF macros */
#define LED_On()                        LED_Clear()
#define LED_Off()                       LED_Set()

/* Application's state machine enum */
typedef enum
{
    APP_STATE_MCAN_RECEIVE,
    APP_STATE_MCAN_TRANSMIT,
    APP_STATE_MCAN_IDLE,
    APP_STATE_MCAN_XFER_SUCCESSFUL,
    APP_STATE_MCAN_XFER_ERROR
} APP_STATES;

/* Global variables */
char messageStart[] = "**** MCAN Normal Operation Interrupt Demo ****\r\n\
**** Demo uses interrupt model of MCAN PLIB. ****\r\n\
**** Receive message from CAN Bus and transmit back received message to CAN Bus and UART1 serial port ****\r\n\
**** LED toggles on each time the message is transmitted back ****\r\n";
/* Variable to save application state */
static APP_STATES state = APP_STATE_MCAN_RECEIVE;
/* Variable to save Tx/Rx transfer status and context */
static uint32_t status = 0;
static uint32_t xferContext = 0;

// *****************************************************************************
// *****************************************************************************
// Section: Local functions
// *****************************************************************************
// *****************************************************************************

/* This function will be called by MCAN PLIB when transfer is completed */
// *****************************************************************************
/* void APP_MCAN_Callback(uintptr_t context)

  Summary:
    Function called by MCAN PLIB upon transfer completion

  Description:
    This function will be called by MCAN PLIB when transfer is completed.
    In this function, current state of the application is obtained by context
    parameter. Based on current state of the application and MCAN error
    state, next state of the application is decided.

  Remarks:
    None.
*/
void APP_MCAN_Callback(uintptr_t context)
{
    /* Check MCAN Status */
    status = MCAN0_ErrorGet();

    if (((status & MCAN_PSR_LEC_Msk) == MCAN_ERROR_NONE) || ((status & MCAN_PSR_LEC_Msk) == MCAN_PSR_LEC_NO_CHANGE))
    {
        switch ((APP_STATES)context)
        {
            case APP_STATE_MCAN_RECEIVE:
            {
                state = APP_STATE_MCAN_TRANSMIT;
                break;
            }
            case APP_STATE_MCAN_TRANSMIT:
            {
                state = APP_STATE_MCAN_XFER_SUCCESSFUL;
                break;
            }
            default:
                break;
        }
    }
    else
    {
        state = APP_STATE_MCAN_XFER_ERROR;
        xferContext = context;
    }
}

// *****************************************************************************
// *****************************************************************************
// Section: Main Entry Point
// *****************************************************************************
// *****************************************************************************
int main ( void )
{
    uint32_t messageID = 0;
    uint8_t message[64];
    uint8_t messageLength = 0;

    /* Initialize all modules */
    SYS_Initialize ( NULL );
    LED_Off();

    /* Send start message */
    UART1_Write(&messageStart, sizeof(messageStart));

    while(1)
    {
        /* Check the application's current state. */
        switch (state)
        {
            case APP_STATE_MCAN_RECEIVE:
            {
                MCAN0_CallbackRegister( APP_MCAN_Callback, (uintptr_t)APP_STATE_MCAN_RECEIVE );

                state = APP_STATE_MCAN_IDLE;

                /* Receive FIFO 0 New Message */
                if (!MCAN0_MessageReceive(&messageID, &messageLength, message, MCAN_MSG_ATTR_RX_FIFO0))
                {
                    printf("MCAN0_MessageReceive request has failed\r\n");
                }
                break;
            }
            case APP_STATE_MCAN_TRANSMIT:
            {
                MCAN0_CallbackRegister( APP_MCAN_Callback, (uintptr_t)APP_STATE_MCAN_TRANSMIT );

                state = APP_STATE_MCAN_IDLE;

                /* Transmit back received Message */
                if (!MCAN0_MessageTransmit(messageID, messageLength, message, MCAN_MODE_NORMAL, MCAN_MSG_ATTR_TX_FIFO_DATA_FRAME))
                {
                    printf("MCAN0_MessageTransmit request has failed\r\n");
                }
                break;
            }
            case APP_STATE_MCAN_IDLE:
            {
                /* Application can do other task here */
                break;
            }
            case APP_STATE_MCAN_XFER_SUCCESSFUL:
            {
                /* Print message to UART1 */
                uint8_t length = messageLength;
                printf("Message - ID : 0x%x Length : 0x%x ", messageID, messageLength);
                printf("Message : ");
                while(length)
                {
                    printf("0x%x ", message[messageLength - length--]);
                }
                printf("\r\n");
                LED_Toggle();
                state = APP_STATE_MCAN_RECEIVE;
                break;
            }
            case APP_STATE_MCAN_XFER_ERROR:
            {
                if ((APP_STATES)xferContext == APP_STATE_MCAN_RECEIVE)
                {
                    printf("MCAN Rx Error : 0x%x\r\n", status);
                }
                else
                {
                    printf("MCAN Tx Error : 0x%x\r\n", status);
                }
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

