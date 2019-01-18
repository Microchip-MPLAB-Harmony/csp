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

uint8_t Mcan0MessageRAM[MCAN0_MESSAGE_RAM_CONFIG_SIZE] __attribute__((aligned (32))) __attribute__((__section__(".region_nocache")));

char messageStart[] = "**** MCAN Normal Operation Blocking Demo ****\r\n\
**** Demo uses blocking model of MCAN PLIB. ****\r\n\
**** Receive message from CAN Bus and transmit back received message to CAN Bus and UART1 serial port ****\r\n\
**** LED toggles on each time the message is transmitted back ****\r\n";

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
    uint32_t status = 0;

    /* Initialize all modules */
    SYS_Initialize ( NULL );
    LED_Off();

    /* Set Message RAM Configuration */
    MCAN0_MessageRAMConfigSet(Mcan0MessageRAM);

    /* Send start message */
    UART1_Write(&messageStart, sizeof(messageStart));

    while (1)
    {
        /* Check if there is a receive FIFO 0 New Message */
        if (MCAN0_InterruptGet(MCAN_INTERRUPT_RF0N_MASK))
        {
            MCAN0_InterruptClear(MCAN_INTERRUPT_RF0N_MASK);

            /* Check MCAN Status */
            status = MCAN0_ErrorGet();

            if (((status & MCAN_PSR_LEC_Msk) == MCAN_ERROR_NONE) || ((status & MCAN_PSR_LEC_Msk) == MCAN_PSR_LEC_NO_CHANGE))
            {
                memset(message, 0x00, sizeof(message));
                /* Receive FIFO 0 New Message */
                if (MCAN0_MessageReceive(&messageID, &messageLength, message, MCAN_MSG_ATTR_RX_FIFO0))
                {
                    /* Transmit back received Message */
                    if (!MCAN0_MessageTransmit(messageID, messageLength, message, MCAN_MODE_NORMAL, MCAN_MSG_ATTR_TX_FIFO_DATA_FRAME))
                    {
                        printf("MCAN0_MessageTransmit request has failed\r\n");
                    }
                    else if (MCAN0_InterruptGet(MCAN_INTERRUPT_TC_MASK))
                    {
                        MCAN0_InterruptClear(MCAN_INTERRUPT_TC_MASK);
                    }
                    /* Check MCAN Status */
                    status = MCAN0_ErrorGet();
                    if (((status & MCAN_PSR_LEC_Msk) == MCAN_ERROR_NONE) || ((status & MCAN_PSR_LEC_Msk) == MCAN_PSR_LEC_NO_CHANGE))
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
                    }
                    else
                    {
                        printf("MCAN Tx Error : 0x%x\r\n", status);
                    }
                }
                else
                {
                    printf("MCAN0_MessageReceive request has failed\r\n");
                }
            }
            else
            {
                printf("MCAN Rx Error : 0x%x\r\n", status);
            }
        }
    }

    /* Execution should not come here during normal operation */

    return ( EXIT_FAILURE );
}


/*******************************************************************************
 End of File
*/

