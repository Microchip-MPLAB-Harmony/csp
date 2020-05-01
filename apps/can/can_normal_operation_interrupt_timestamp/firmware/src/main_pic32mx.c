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

#define SW1_PRESSED_STATE           0   // Active LOW switch

/* Application's state machine enum */
typedef enum
{
    APP_STATE_CAN_RECEIVE,
    APP_STATE_CAN_TRANSMIT,
    APP_STATE_CAN_IDLE,
    APP_STATE_CAN_USER_INPUT,
    APP_STATE_CAN_XFER_SUCCESSFUL,
    APP_STATE_CAN_XFER_ERROR
} APP_STATES;

/* set format attribute for the vararg function */
void PrintFormattedData (const char * format, ...) __attribute__ ((format (printf, 1, 2)));

/* Variable to save application state */
static APP_STATES state = APP_STATE_CAN_USER_INPUT;
/* Variable to save Tx/Rx transfer status and context */
static uint32_t status = 0;
static uint32_t xferContext = APP_STATE_CAN_IDLE;
/* Variable to save Tx/Rx message */
static uint32_t messageID = 0;
static uint8_t message[8];
static uint8_t messageLength = 0;
static uint8_t rx_message[8];
static uint32_t rx_messageID = 0;
static uint8_t rx_messageLength = 0;
static uint16_t timestamp = 0;
static CAN_MSG_RX_ATTRIBUTE msgAttr = CAN_MSG_RX_DATA_FRAME;

// *****************************************************************************
// *****************************************************************************
// Section: Local functions
// *****************************************************************************
// *****************************************************************************

/* This function will be called by CAN PLIB when transfer is completed */
// *****************************************************************************
/* void APP_CAN_Callback(uintptr_t context)

  Summary:
    Function called by CAN PLIB upon transfer completion

  Description:
    This function will be called by CAN PLIB when transfer is completed.
    In this function, current state of the application is obtained by context
    parameter. Based on current state of the application and CAN error
    state, next state of the application is decided.

  Remarks:
    None.
*/
void APP_CAN_Callback(uintptr_t context)
{
    /* Check CAN Status */
    status = CAN1_ErrorGet();

    if ((status & (CAN_ERROR_TX_RX_WARNING_STATE | CAN_ERROR_RX_WARNING_STATE |
                   CAN_ERROR_TX_WARNING_STATE | CAN_ERROR_RX_BUS_PASSIVE_STATE |
                   CAN_ERROR_TX_BUS_PASSIVE_STATE | CAN_ERROR_TX_BUS_OFF_STATE)) == CAN_ERROR_NONE)
    {
        switch ((APP_STATES)context)
        {
            case APP_STATE_CAN_RECEIVE:
            case APP_STATE_CAN_TRANSMIT:
            {
                state = APP_STATE_CAN_XFER_SUCCESSFUL;
                break;
            }
            default:
                break;
        }
    }
    else
    {
        state = APP_STATE_CAN_XFER_ERROR;
    }
}

// *****************************************************************************
// *****************************************************************************
// Section: Main Entry Point
// *****************************************************************************
// *****************************************************************************

int main ( void )
{
    uint8_t count = 0;

    /* Initialize all modules */
    SYS_Initialize ( NULL );

    /* Prepare the message to send*/
    messageID = 0x469;
    messageLength = 8;
    for (count = 8; count >=1; count--)
    {
        message[count - 1] = count;
    }
    
    while ( true )
    {
        if (state == APP_STATE_CAN_USER_INPUT)
        {
            if(SW1_Get() == SW1_PRESSED_STATE)
            {
                while(SW1_Get() == SW1_PRESSED_STATE);
                xferContext = APP_STATE_CAN_TRANSMIT;
                CAN1_CallbackRegister( APP_CAN_Callback, (uintptr_t)APP_STATE_CAN_TRANSMIT, 0 );
                state = APP_STATE_CAN_IDLE;
                /* Transmit a Message */
                CAN1_MessageTransmit(messageID, messageLength, message, 0, CAN_MSG_TX_DATA_FRAME);
            }
        }
        if (xferContext != APP_STATE_CAN_TRANSMIT)
        {
            if (CAN1_InterruptGet(1, CAN_FIFO_INTERRUPT_RXNEMPTYIF_MASK))
            {
                CAN1_CallbackRegister( APP_CAN_Callback, (uintptr_t)APP_STATE_CAN_RECEIVE, 1 );
                state = APP_STATE_CAN_IDLE;
                memset(rx_message, 0x00, sizeof(rx_message));
                /* Receive New Message */
                CAN1_MessageReceive(&rx_messageID, &rx_messageLength, rx_message, &timestamp, 1, &msgAttr);
            }
        }
        /* Check the application's current state. */
        switch (state)
        {
            case APP_STATE_CAN_IDLE:
            {
                /* Application can do other task here */
                break;
            }
            case APP_STATE_CAN_XFER_SUCCESSFUL:
            {
                LED1_Toggle();
                state = APP_STATE_CAN_USER_INPUT;
                xferContext = APP_STATE_CAN_IDLE;
                break;
            }
            case APP_STATE_CAN_XFER_ERROR:
            {
                state = APP_STATE_CAN_USER_INPUT;
                xferContext = APP_STATE_CAN_IDLE;
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
