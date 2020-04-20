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

static uint8_t message[64];
static uint8_t rx_message[64];

void print_menu(void)
{
	printf("Menu :\r\n"
	       "  -- Select the action:\r\n"
	       "  1: Send FD standard message with ID: 0x45A and 64 byte data 0 to 63. \r\n"
	       "  2: Send normal standard message with ID: 0x469 and 8 byte data 0 to 7. \r\n"
	       "  3: To receive CAN FD or Normal message \r\n"
	       "  m: Display menu \r\n\r\n");
}

// *****************************************************************************
// *****************************************************************************
// Section: Main Entry Point
// *****************************************************************************
// *****************************************************************************

int main ( void )
{
    uint32_t messageID = 0;
    uint32_t rx_messageID = 0;
    uint32_t status = 0;
    uint8_t messageLength = 0;
    uint8_t rx_messageLength = 0;
    uint8_t count = 0;
    uint8_t user_input = 0;
    CAN_MSG_RX_ATTRIBUTE msgAttr = CAN_MSG_RX_DATA_FRAME;

    /* Initialize all modules */
    SYS_Initialize ( NULL );

    printf(" ------------------------------ \r\n");
    printf("            CAN FD Demo         \r\n");
    printf(" ------------------------------ \r\n");

    print_menu();

    /* Prepare the message to send*/
    for (count = 0; count < 64; count++)
    {
        message[count] = count;
    }

    while ( true )
    {
        /* Maintain state machines of all polled Harmony modules. */
        /* Check if there is a received character */
        if(UART6_ReceiverIsReady() == true)
        {
            if(UART6_ErrorGet() == UART_ERROR_NONE)
            {
                UART6_Read((void *)&user_input, 1);
            }
            switch (user_input)
            {
                case '1':
                    printf(" Transmitting CAN FD Message:");
                    messageID = 0x45A;
                    messageLength = 64;
                    if (CAN1_MessageTransmit(messageID, messageLength, message, 1, CAN_MODE_FD_WITH_BRS, CAN_MSG_TX_DATA_FRAME) == true)
                    {
                        printf("Success \r\n");
                        LED_Toggle();
                    }
                    else
                    {
                        printf("Failed \r\n");
                    }
                    break;
                case '2':
                    printf(" Transmitting CAN Normal Message:");
                    messageID = 0x469;
                    messageLength = 8;
                    if (CAN1_MessageTransmit(messageID, messageLength, message, 1, CAN_MODE_NORMAL, CAN_MSG_TX_DATA_FRAME) == true)
                    {
                        printf("Success \r\n");
                        LED_Toggle();
                    }
                    else
                    {
                        printf("Failed \r\n");
                    }
                    break;
                case '3':
                    printf(" Waiting for message: \r\n");
                    while (true)
                    {
                        if (CAN1_InterruptGet(2, CAN_FIFO_INTERRUPT_TFNRFNIF_MASK))
                        {
                            /* Check CAN Status */
                            status = CAN1_ErrorGet();

                            if (status == CAN_ERROR_NONE)
                            {
                                memset(rx_message, 0x00, sizeof(rx_message));

                                /* Receive New Message */
                                if (CAN1_MessageReceive(&rx_messageID, &rx_messageLength, rx_message, 0, 2, &msgAttr) == true)
                                {
                                    printf(" New Message Received    \r\n");
                                    status = CAN1_ErrorGet();
                                    if (status == CAN_ERROR_NONE)
                                    {
                                        /* Print message to Console */
                                        uint8_t length = rx_messageLength;
                                        printf(" Message - ID : 0x%x Length : 0x%x ", (unsigned int) rx_messageID,(unsigned int) rx_messageLength);
                                        printf("Message : ");
                                        while(length)
                                        {
                                            printf("0x%x ", rx_message[rx_messageLength - length--]);
                                        }
                                        printf("\r\n");
                                        LED_Toggle();
                                        break;
                                    }
                                    else
                                    {
                                        printf("Error in received message");
                                    }
                                }
                                else
                                {
                                    printf("Message Reception Failed \r");
                                }
                            }
                            else
                            {
                                printf("Error in last received message");
                            }
                        }
                    }
                    break;
                case 'm':
                    break;
                default:
                    printf(" Invalid Input \r\n");
                    break;
            }
            print_menu();
        }
    }

    /* Execution should not come here during normal operation */

    return ( EXIT_FAILURE );
}


/*******************************************************************************
 End of File
*/

