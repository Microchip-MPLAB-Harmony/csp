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

/* LED Toggle */
#define LED_Toggle() LED_GREEN_Toggle()

/* Variable to save application state */
static APP_STATES state = APP_STATE_CAN_USER_INPUT;
/* Variable to save Tx/Rx transfer status and context */
static uint32_t status = 0;
static uint32_t xferContext = 0;
/* Variable to save Tx/Rx message */
static uint32_t messageID = 0;
static uint8_t message[8];
static uint8_t messageLength = 0;
static uint8_t rx_message[8];
static uint32_t rx_messageID = 0;
static uint8_t rx_messageLength = 0;

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
    xferContext = context;

    /* Check CAN Status */
    status = CAN1_ErrorGet();

    if ((status & (CAN_ERROR_BOFF | CAN_ERROR_CERR |
                   CAN_ERROR_SERR | CAN_ERROR_AERR |
                   CAN_ERROR_FERR | CAN_ERROR_BERR)) == CAN_ERROR_NONE)
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

void print_menu(void)
{
    printf(" ------------------------------ \r\n");   
    printf(" Press '1' to Transmit message \r\n");
    printf(" Press '2' to Receive message \r\n");
}

// *****************************************************************************
// *****************************************************************************
// Section: Main Entry Point
// *****************************************************************************
// *****************************************************************************

int main ( void )
{
    uint8_t user_input = 0;
    
    /* Initialize all modules */
    SYS_Initialize ( NULL );

    LED_RED_Clear();
    LED_GREEN_Clear();
    LED_BLUE_Clear();

    printf(" ------------------------------ \r\n");
    printf("            CAN Demo            \r\n");
    printf(" ------------------------------ \r\n");
    
    print_menu();
    
    /* Prepare the message to send*/
    messageID = 0x469;
    messageLength = 8;
    for (uint8_t count = 8; count >=1; count--){
        message[count - 1] = count;
    }
    
    while ( true )
    {
        if (state == APP_STATE_CAN_USER_INPUT)
        {
            /* Read user input */
            DBGU_Read(&user_input, 1);
            
            switch (user_input)
            {
                case '1': 
                    printf(" Transmitting Message:");
                    CAN1_CallbackRegister( APP_CAN_Callback, (uintptr_t)APP_STATE_CAN_TRANSMIT );
                    state = APP_STATE_CAN_IDLE;
                    if (!CAN1_MessageTransmit(messageID, messageLength, message, CAN_MAILBOX_DATA_FRAME_TX) == true)
                    {
                        printf("CAN1_MessageTransmit request has failed\r\n");
                    }             
                    break;
                case '2':
                    printf(" Waiting for message: \r\n");
                    CAN1_CallbackRegister( APP_CAN_Callback, (uintptr_t)APP_STATE_CAN_RECEIVE );
                    state = APP_STATE_CAN_IDLE;
                    memset(rx_message, 0x00, sizeof(rx_message));
                    /* Receive New Message */
                    if (!CAN1_MessageReceive(&rx_messageID, &rx_messageLength, rx_message, CAN_MAILBOX_DATA_FRAME_RX_OVERWRITE) == true)  
                    {
                        printf("CAN1_MessageReceive request has failed\r\n");
                    }
                    break;
                default:
                    printf(" Invalid Input \r\n");
                    break;
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
                if ((APP_STATES)xferContext == APP_STATE_CAN_RECEIVE)
                {
                    /* Print message to Console */
                    printf(" New Message Received    \r\n");
                    uint8_t length = rx_messageLength;
                    printf(" Message - ID : 0x%x Length : 0x%x ", (unsigned int) rx_messageID,(unsigned int) rx_messageLength);
                    printf("Message : ");
                    while(length)
                    {
                        printf("0x%x ", rx_message[rx_messageLength - length--]);
                    }
                    printf("\r\n");
                } 
                else if ((APP_STATES)xferContext == APP_STATE_CAN_TRANSMIT)
                {
                    printf("Success \r\n");
                }
                LED_Toggle();
                print_menu();
                state = APP_STATE_CAN_USER_INPUT;
                break;
            }
            case APP_STATE_CAN_XFER_ERROR:
            {
                if ((APP_STATES)xferContext == APP_STATE_CAN_RECEIVE)
                {
                    printf("Error in received message");
                }
                else
                {
                    printf("Failed \r\n");
                }
                print_menu();
                state = APP_STATE_CAN_USER_INPUT;
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
