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

#define RX_BUFFER_SIZE 256

char messageStart[] = "**** USART Line Echo Demo ****\r\n\
**** Demo uses blocking model of USART PLIB. ****\r\n\
**** Enter a line of characters, press ENTER key and observe it echo back. ****\
\r\n**** LED toggles on each time the line is echoed ****\r\n";
char newline[] = "\r\n";
char errorMessage[] = "\r\n**** USART error has occurred ****\r\n";
char receiveBuffer[RX_BUFFER_SIZE] = {};
char data = 0;

// *****************************************************************************
// *****************************************************************************
// Section: Main Entry Point
// *****************************************************************************
// *****************************************************************************

int main ( void )
{
    uint8_t rxCounter=0;

    /* Initialize all modules */
    SYS_Initialize ( NULL );
    LED1_Set();

    /* Send start message */
    USART1_Write(&messageStart, sizeof(messageStart));

    while ( true )
    {
        /* Check if there is a received character */
        if(USART1_ReceiverIsReady() == true)
        {
            if(USART1_ErrorGet() == USART_ERROR_NONE)
            {
                USART1_Read(&data, 1);

                if((data == '\n') || (data == '\r'))
                {
                    USART1_Write(receiveBuffer,rxCounter);
                    USART1_Write(newline,sizeof(newline));
                    rxCounter = 0;
                    LED1_Toggle();
                }
                else
                {
                    receiveBuffer[rxCounter++] = data;
                }
            }
            else
            {
                USART1_Write(errorMessage,sizeof(errorMessage));
            }
        }
    }

    /* Execution should not come here during normal operation */

    return ( EXIT_FAILURE );
}


/*******************************************************************************
 End of File
*/

