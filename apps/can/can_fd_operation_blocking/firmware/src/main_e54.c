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

uint8_t Can1MessageRAM[CAN1_MESSAGE_RAM_CONFIG_SIZE] __attribute__((aligned (32)));
        
void display_menu(void)
{
	printf("Menu :\r\n"
	       "  -- Select the action:\r\n"
	       "  0: Set standard filter ID 0: 0x45A, Wait for message & store into RX Buffer \r\n"
	       "  1: Set standard filter ID 1: 0x469 & Wait for message & store into RX FIFO 0\r\n"
	       "  2: Send FD standard message with ID: 0x45A and 64 byte data 0 to 63. \r\n"
	       "  3: Send FD standard message with ID: 0x469 and 64 byte data 128 to 191. \r\n"
	       "  4: Set extended filter ID 0: 0x100000A5, Wait for message & store into RX buffer\r\n"
	       "  5: Set extended filter ID 1: 0x10000096, Wait for message & store into RX FIFO 1\r\n"
	       "  6: Send FD extended message with ID: 0x100000A5 and 64 byte data 0 to 63. \r\n"
	       "  7: Send FD extended message with ID: 0x10000096 and 64 byte data 128 to 191. \r\n"
	       "  a: Send normal standard message with ID: 0x469 and 8 byte data 0 to 7. \r\n"
	       "  m: Display menu \r\n\r\n");
}

// *****************************************************************************
// *****************************************************************************
// Section: Main Entry Point
// *****************************************************************************
// *****************************************************************************

int main ( void )
{
    uint8_t user_input = 0;
    uint32_t messageID = 0;
    uint8_t message[64];
    uint8_t messageLength = 0;
    uint32_t status = 0;
    
    uint8_t rx_message[64];
    uint32_t rx_messageID = 0;
    uint8_t rx_messageLength = 0;
    
    volatile uint8_t loop_count;
    CAN_MSG_RX_FRAME_ATTRIBUTE msgFrameAttr = CAN_MSG_RX_DATA_FRAME;

    /* Initialize all modules */
    SYS_Initialize ( NULL );

    printf(" ------------------------------ \r\n");
    printf("            CAN FD Demo          \r\n");
    printf(" ------------------------------ \r\n");
    
    /* Set Message RAM Configuration */
    CAN1_MessageRAMConfigSet(Can1MessageRAM);

    display_menu();
     
    while ( true )
    {
        /* Maintain state machines of all polled MPLAB Harmony modules. */
        scanf("%c", (char *) &user_input);
        
        switch (user_input)
        {
            case '2':
                messageID = 0x45A;
                messageLength = 64;
                for (loop_count = 0; loop_count < 64; loop_count++){
                    message[loop_count] = loop_count;
                }                
                printf("  2: Send standard message with ID: 0x45A and 64 byte data 0 to 63. \r\n");
                if (CAN1_InterruptGet(CAN_INTERRUPT_TC_MASK))
                {
                    CAN1_InterruptClear(CAN_INTERRUPT_TC_MASK);
                }
                if (CAN1_MessageTransmit(messageID,messageLength,message, CAN_MODE_FD_WITH_BRS, CAN_MSG_ATTR_TX_FIFO_DATA_FRAME) == true)
                {    
                    printf(" Success \r\n");
                }
                else
                {
                    printf(" Failed \r\n");
                }             
                break;  
            case '3':
                messageID = 0x469;
                messageLength = 64;
                for (loop_count = 128; loop_count <192; loop_count++){
                    message[loop_count - 128] = loop_count;
                }                
                printf("  3: Send standard message with ID: 0x469 and 64 byte data 128 to 191.\r\n");
                if (CAN1_InterruptGet(CAN_INTERRUPT_TC_MASK))
                {
                    CAN1_InterruptClear(CAN_INTERRUPT_TC_MASK);
                }
                if (CAN1_MessageTransmit(messageID,messageLength,message, CAN_MODE_FD_WITH_BRS, CAN_MSG_ATTR_TX_FIFO_DATA_FRAME) == true)
                {    
                    printf(" Success \r\n");
                }
                else
                {
                    printf(" Failed \r\n");
                }             
                break;
              
            case '0':
                printf(" ID set in the range already \r\n");
                printf(" Waiting for message: \r\n");
                while (true)
                {
                    if (CAN1_InterruptGet(CAN_INTERRUPT_DRX_MASK))
                    {    
                        CAN1_InterruptClear(CAN_INTERRUPT_DRX_MASK);

                        /* Check CAN Status */
                        status = CAN1_ErrorGet();

                        if (((status & CAN_PSR_LEC_Msk) == CAN_ERROR_NONE) || ((status & CAN_PSR_LEC_Msk) == CAN_ERROR_LEC_NC))
                        {
                            memset(rx_message, 0x00, sizeof(rx_message));
                            
                            /* Receive FIFO 0 New Message */
                            if (CAN1_MessageReceive(&rx_messageID, &rx_messageLength, rx_message, 0, CAN_MSG_ATTR_RX_BUFFER, &msgFrameAttr) == true)  
                            {
                                printf(" New Message Received    \r\n");
                                status = CAN1_ErrorGet();
                                if (((status & CAN_PSR_LEC_Msk) == CAN_ERROR_NONE) || ((status & CAN_PSR_LEC_Msk) == CAN_ERROR_LEC_NC))
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
                    else
                    {
                        printf(" No new message received \r");
                    }
                }
                break;                
            case '1':
                printf(" ID set in the range already \r\n");
                printf(" Waiting for message: \r\n");
                while (true)
                {
                    if (CAN1_InterruptGet(CAN_INTERRUPT_RF0N_MASK))
                    {    
                        CAN1_InterruptClear(CAN_INTERRUPT_RF0N_MASK);

                        /* Check CAN Status */
                        status = CAN1_ErrorGet();

                        if (((status & CAN_PSR_LEC_Msk) == CAN_ERROR_NONE) || ((status & CAN_PSR_LEC_Msk) == CAN_ERROR_LEC_NC))
                        {
                            memset(rx_message, 0x00, sizeof(rx_message));
                            
                            /* Receive FIFO 0 New Message */
                            if (CAN1_MessageReceive(&rx_messageID, &rx_messageLength, rx_message, 0, CAN_MSG_ATTR_RX_FIFO0, &msgFrameAttr) == true)  
                            {
                                printf(" New Message Received    \r\n");
                                status = CAN1_ErrorGet();
                                if (((status & CAN_PSR_LEC_Msk) == CAN_ERROR_NONE) || ((status & CAN_PSR_LEC_Msk) == CAN_ERROR_LEC_NC))
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
            case '4':
                printf(" ID set in the range already \r\n");
                printf(" Waiting for message: \r\n");
                while (true)
                {
                    if (CAN1_InterruptGet(CAN_INTERRUPT_DRX_MASK))
                    {    
                        CAN1_InterruptClear(CAN_INTERRUPT_DRX_MASK);

                        /* Check CAN Status */
                        status = CAN1_ErrorGet();

                        if (((status & CAN_PSR_LEC_Msk) == CAN_ERROR_NONE) || ((status & CAN_PSR_LEC_Msk) == CAN_ERROR_LEC_NC))
                        {
                            memset(rx_message, 0x00, sizeof(rx_message));
                            
                            /* Receive FIFO 0 New Message */
                            if (CAN1_MessageReceive(&rx_messageID, &rx_messageLength, rx_message, 0, CAN_MSG_ATTR_RX_BUFFER, &msgFrameAttr) == true)  
                            {
                                printf(" New Message Received    \r\n");
                                status = CAN1_ErrorGet();
                                if (((status & CAN_PSR_LEC_Msk) == CAN_ERROR_NONE) || ((status & CAN_PSR_LEC_Msk) == CAN_ERROR_LEC_NC))
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
                    else
                    {
                        printf(" No new message received \r");
                    }
                }
                break;                 
            case '5':
                printf(" ID set in the range already \r\n");
                printf(" Waiting for message: \r\n");
                while (true)
                {
                    if (CAN1_InterruptGet(CAN_INTERRUPT_RF1N_MASK))
                    {    
                        CAN1_InterruptClear(CAN_INTERRUPT_RF1N_MASK);

                        /* Check CAN Status */
                        status = CAN1_ErrorGet();

                        if (((status & CAN_PSR_LEC_Msk) == CAN_ERROR_NONE) || ((status & CAN_PSR_LEC_Msk) == CAN_ERROR_LEC_NC))
                        {
                            memset(rx_message, 0x00, sizeof(rx_message));
                            
                            /* Receive FIFO 0 New Message */
                            if (CAN1_MessageReceive(&rx_messageID, &rx_messageLength, rx_message, 0, CAN_MSG_ATTR_RX_FIFO1, &msgFrameAttr) == true)  
                            {
                                printf(" New Message Received    \r\n");
                                status = CAN1_ErrorGet();
                                if (((status & CAN_PSR_LEC_Msk) == CAN_ERROR_NONE) || ((status & CAN_PSR_LEC_Msk) == CAN_ERROR_LEC_NC))
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
            case '6': 
                messageID = 0x100000A5;
                messageLength = 64;
                for (loop_count = 0; loop_count < 64; loop_count++){
                    message[loop_count] = loop_count;
                }                
                printf("  6: Send extended message with ID: 0x100000A5 and 64 byte data 0 to 63. \r\n");
                if (CAN1_InterruptGet(CAN_INTERRUPT_TC_MASK))
                {
                    CAN1_InterruptClear(CAN_INTERRUPT_TC_MASK);
                }
                if (CAN1_MessageTransmit(messageID,messageLength,message, CAN_MODE_FD_WITH_BRS, CAN_MSG_ATTR_TX_FIFO_DATA_FRAME) == true)
                {    
                    printf(" Success \r\n");
                }
                else
                {
                    printf(" Failed \r\n");
                }             
                break;
            
            case '7': 
                messageID = 0x10000096;
                messageLength = 64;
                for (loop_count = 128; loop_count <192; loop_count++){
                    message[loop_count - 128] = loop_count;
                }
                printf("  7: Send extended message with ID: 0x10000096 and 64 byte data 128 to 191. \r\n");
                if (CAN1_InterruptGet(CAN_INTERRUPT_TC_MASK))
                {
                    CAN1_InterruptClear(CAN_INTERRUPT_TC_MASK);
                }
                if (CAN1_MessageTransmit(messageID,messageLength,message, CAN_MODE_FD_WITH_BRS, CAN_MSG_ATTR_TX_FIFO_DATA_FRAME) == true)
                {    
                    printf(" Success \r\n");
                }
                else
                {
                    printf(" Failed \r\n");
                }             
                break;
            
            case 'a':
            case 'A': 
                messageID = 0x469;
                messageLength = 8;
                for (loop_count = 0; loop_count < 8; loop_count++){
                    message[loop_count] = loop_count;
                }
                printf("  a: Send normal standard message with ID: 0x469 and 8 byte data 0 to 7. \r\n");
                if (CAN1_InterruptGet(CAN_INTERRUPT_TC_MASK))
                {
                    CAN1_InterruptClear(CAN_INTERRUPT_TC_MASK);
                }
                if (CAN1_MessageTransmit(messageID,messageLength,message, CAN_MODE_NORMAL, CAN_MSG_ATTR_TX_FIFO_DATA_FRAME) == true)
                {    
                    printf(" Success \r\n");
                }
                else
                {
                    printf(" Failed \r\n");
                }             
                break;                 

            case 'm':
            case 'M':
                display_menu();
                break;
                
            default:
                printf(" Invalid Input \r\n");
                break;
        }  
    }

    /* Execution should not come here during normal operation */

    return ( EXIT_FAILURE );
}


/*******************************************************************************
 End of File
*/
