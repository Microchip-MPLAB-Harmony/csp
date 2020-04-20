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
#include <string.h>
#include "definitions.h"                // SYS function prototypes

/********************************************************************
 * This demo demonstrates auto-baud feature. To start the baud rate 
 * detection, enter character ASCII 'U' (0x55) on the host terminal.
 *********************************************************************/

const char baudRateDetectedMsg[] = {
    "Auto-Baud detection complete! \r\n"
    "Enter a character to echo it back on the terminal \r\n"
};

bool uartReadDone = false;
bool uartWriteDone = false;

void UART_WriteCallback(uintptr_t context)
{
    uartWriteDone = true;
}

void UART_ReadCallback(uintptr_t context)
{
    uartReadDone = true;
}

// *****************************************************************************
// *****************************************************************************
// Section: Main Entry Point
// *****************************************************************************
// *****************************************************************************
int main ( void )
{
    char received_char;
    
    /* Initialize all modules */
    SYS_Initialize ( NULL );
    
    UART6_ReadCallbackRegister( UART_ReadCallback, NULL );    
    UART6_WriteCallbackRegister( UART_WriteCallback, NULL );    
       
    /* Start up auto-baud sensing feature */
    UART6_AutoBaudSet(true);
    while(UART6_AutoBaudQuery()==true);     
    
    UART6_Write((void*)baudRateDetectedMsg, sizeof(baudRateDetectedMsg));
    
    while ( true )
    {   
        if(uartWriteDone == true)
        {   
            uartWriteDone = false;    
            UART6_Read(&received_char, 1);
        }                       
        if(uartReadDone == true)
        {
            uartReadDone = false;
            /* Echo the received character back */
            UART6_Write(&received_char, 1);
        }
    }

    /* Execution should not come here during normal operation */
    return ( EXIT_FAILURE );
}
/*******************************************************************************
 End of File
*/

