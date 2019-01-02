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

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

#include <stddef.h>                     // Defines NULL
#include <stdbool.h>                    // Defines true
#include <stdlib.h>                     // Defines EXIT_FAILURE
#include "definitions.h"                // SYS function prototypes

static void TransmitCompleteCallback(DMAC_TRANSFER_EVENT event, uintptr_t contextHandle);
static void ReceiveCompleteCallback(DMAC_TRANSFER_EVENT event, uintptr_t contextHandle);

#define RX_BUFFER_SIZE 10
#define LED_ON    LED_Clear
#define LED_OFF   LED_Set

char messageStart[] = "**** DMAC USART echo demo ****\r\n\
**** Type a buffer of 10 characters and observe it echo back using DMA ****\r\n\
**** LED toggles each time the buffer is echoed ****\r\n";
char receiveBuffer[RX_BUFFER_SIZE] = {};
char echoBuffer[RX_BUFFER_SIZE+2] = {};

        
volatile bool writeStatus = false;
volatile bool readStatus = false;

// *****************************************************************************
// *****************************************************************************
// Section: Main Entry Point
// *****************************************************************************
// *****************************************************************************

int main ( void )
{
    /* Initialize all modules */
    SYS_Initialize ( NULL );
    DMAC_ChannelCallbackRegister(DMAC_CHANNEL_0, TransmitCompleteCallback,0);
    DMAC_ChannelCallbackRegister(DMAC_CHANNEL_1, ReceiveCompleteCallback,0);
    DMAC_ChannelTransfer(DMAC_CHANNEL_0, &messageStart, (const void *)&SERCOM2_REGS->USART_INT.SERCOM_DATA, sizeof(messageStart));
            
    while ( true )
    {
        /* Maintain state machines of all polled MPLAB Harmony modules. */
        SYS_Tasks ( );
        if(readStatus == true)
        {
            /* Echo back received buffer and Toggle LED */
            readStatus = false;

            memcpy(echoBuffer, receiveBuffer,sizeof(receiveBuffer));
            echoBuffer[sizeof(receiveBuffer)]='\r';
            echoBuffer[sizeof(receiveBuffer)+1]='\n';


            DMAC_ChannelTransfer(DMAC_CHANNEL_0, &echoBuffer, (const void *)&SERCOM2_REGS->USART_INT.SERCOM_DATA, sizeof(echoBuffer));
            LED_Toggle();
        }
        else if(writeStatus == true)
        {
            /* Submit buffer to read user data */
            writeStatus = false;
            DMAC_ChannelTransfer(DMAC_CHANNEL_1, (const void *)&SERCOM2_REGS->USART_INT.SERCOM_DATA, &receiveBuffer, sizeof(receiveBuffer));            
        }
        else
        {
            /* Repeat the loop */
            ;
        }        
    }

    /* Execution should not come here during normal operation */

    return ( EXIT_FAILURE );
}

static void TransmitCompleteCallback(DMAC_TRANSFER_EVENT event, uintptr_t contextHandle)
{
    writeStatus = true;    
}

static void ReceiveCompleteCallback(DMAC_TRANSFER_EVENT event, uintptr_t contextHandle)
{
    readStatus = true;    
}
/*******************************************************************************
 End of File
*/

