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


char messageStart[] = "**** USART Line Echo Demo: Blocking Transfer without the interrupt ****\r\n\
**** Type a line of characters and press the Enter key. **** \r\n\
**** Entered line will be echoed back, and the LED is toggled. ****\r\n";
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
    SERCOM0_USART_Write(&messageStart[0], sizeof(messageStart));
    
    while ( true )
    {
        /* Check if there is a received character */
        if(SERCOM0_USART_ReceiverIsReady() == true)
        {
            if(SERCOM0_USART_ErrorGet() == USART_ERROR_NONE)
            {
                SERCOM0_USART_Read(&data, 1);

                if((data == '\n') || (data == '\r'))
                {
                    SERCOM0_USART_Write(&newline[0],sizeof(newline));
                    SERCOM0_USART_Write(&receiveBuffer[0],rxCounter);
                    SERCOM0_USART_Write(&newline[0],sizeof(newline));
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
                SERCOM0_USART_Write(&errorMessage[0],sizeof(errorMessage));
            }
        }
    }



    /* Execution should not come here during normal operation */

    return ( EXIT_FAILURE );
}



/*******************************************************************************
 End of File
*/

