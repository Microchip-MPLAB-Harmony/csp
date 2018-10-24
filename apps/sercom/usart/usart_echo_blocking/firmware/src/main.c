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
#define LED_ON    LED_Clear
#define LED_OFF   LED_Set


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
    uint16_t rxCounter=0;
    
    /* Initialize all modules */
    SYS_Initialize ( NULL );

    /* Send start message */
    SERCOM4_USART_Write(&messageStart[0], sizeof(messageStart));
    
    while ( true )
    {
        /* Check if there is a received character */
        if(SERCOM4_USART_ReceiverIsReady() == true)
        {
            if(SERCOM4_USART_ErrorGet() == USART_ERROR_NONE)
            {
                SERCOM4_USART_Read(&data, 1);

                if((data == '\n') || (data == '\r'))
                {
                    SERCOM4_USART_Write(&receiveBuffer[0],rxCounter);
                    SERCOM4_USART_Write(&newline[0],sizeof(newline));
                    rxCounter = 0;
                    LED_Toggle();
                }
                else
                {
                    receiveBuffer[rxCounter++] = data;
                }
            }
            else
            {
                SERCOM4_USART_Write(&errorMessage[0],sizeof(errorMessage));
            }
        }
    }



    /* Execution should not come here during normal operation */

    return ( EXIT_FAILURE );
}


/*******************************************************************************
 End of File
*/

