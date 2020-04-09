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

// *****************************************************************************
// *****************************************************************************
// Section: Main Entry Point
// *****************************************************************************
// *****************************************************************************

int main ( void )
{
    uint32_t messageID = 0;
    uint32_t rx_messageID = 0;
    uint8_t message[8];
    uint8_t rx_message[8];
    uint32_t status = 0;
    uint8_t messageLength = 0;
    uint8_t rx_messageLength = 0;
    uint8_t count = 0;
    CAN_MSG_RX_ATTRIBUTE msgAttr = CAN_MSG_RX_DATA_FRAME;

    /* Initialize all modules */
    SYS_Initialize ( NULL );

    /* Prepare the message to send*/
    messageID = 0x469;
    messageLength = 8;
    for (count = 8; count >=1; count--){
        message[count - 1] = count;
    }

    while ( true )
    {
        if(SW1_Get() == SW1_PRESSED_STATE)
        {
            while(SW1_Get() == SW1_PRESSED_STATE);
            /* Transmit a Message */
            if (CAN1_MessageTransmit(messageID, messageLength, message, 0, CAN_MSG_TX_DATA_FRAME) == true)
            {
                LED1_Toggle();
            }
        }
        if (CAN1_InterruptGet(1, CAN_FIFO_INTERRUPT_RXNEMPTYIF_MASK))
        {
            /* Check CAN Status */
            status = CAN1_ErrorGet();

            if (status == CAN_ERROR_NONE)
            {
                memset(rx_message, 0x00, sizeof(rx_message));

                /* Receive New Message */
                if (CAN1_MessageReceive(&rx_messageID, &rx_messageLength, rx_message, 0, 1, &msgAttr) == true)
                {
                    status = CAN1_ErrorGet();
                    if (status == CAN_ERROR_NONE)
                    {
                        LED1_Toggle();
                    }
                }
            }
        }
    }

    /* Execution should not come here during normal operation */

    return ( EXIT_FAILURE );
}


/*******************************************************************************
 End of File
*/

