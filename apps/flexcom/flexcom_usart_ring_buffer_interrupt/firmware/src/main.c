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


#include <stddef.h>                     // Defines NULL
#include <stdbool.h>                    // Defines true
#include <stdlib.h>                     // Defines EXIT_FAILURE
#include <string.h>
#include <stdio.h>
#include "definitions.h"                // SYS function prototypes

uint8_t txBuffer[50];
uint8_t rxBuffer[10];
volatile uint32_t nBytesRead = 0;
volatile bool txThresholdEventReceived = false;
volatile bool rxThresholdEventReceived = false;

// *****************************************************************************
// *****************************************************************************
// Section: Main Entry Point
// *****************************************************************************
// *****************************************************************************

void usartReadEventHandler(FLEXCOM_USART_EVENT event, uintptr_t context )
{
    uint32_t nBytesAvailable = 0;
    
    if (event == FLEXCOM_USART_EVENT_READ_THRESHOLD_REACHED)
    {
        /* Receiver should atleast have the thershold number of bytes in the ring buffer */
        nBytesAvailable = FLEXCOM1_USART_ReadCountGet();
        
        nBytesRead += FLEXCOM1_USART_Read((uint8_t*)&rxBuffer[nBytesRead], nBytesAvailable);                          
    }
}

void usartWriteEventHandler(FLEXCOM_USART_EVENT event, uintptr_t context )
{
    txThresholdEventReceived = true;
}

int main ( void )
{
    uint32_t nBytes = 0;        
    
    /* Initialize all modules */
    SYS_Initialize ( NULL );          
    
    /* Register a callback for write events */
    FLEXCOM1_USART_WriteCallbackRegister(usartWriteEventHandler, (uintptr_t) NULL);
    
    /* Register a callback for read events */
    FLEXCOM1_USART_ReadCallbackRegister(usartReadEventHandler, (uintptr_t) NULL);              
    
    /* Print the size of the read buffer on the terminal */
    nBytes = sprintf((char*)txBuffer, "RX Buffer Size = %d\r\n", (int)FLEXCOM1_USART_ReadBufferSizeGet());
    
    FLEXCOM1_USART_Write((uint8_t*)txBuffer, nBytes);  
    
    /* Print the size of the write buffer on the terminal */
    nBytes = sprintf((char*)txBuffer, "TX Buffer Size = %d\r\n", (int)FLEXCOM1_USART_WriteBufferSizeGet());
    
    FLEXCOM1_USART_Write((uint8_t*)txBuffer, nBytes);    
    
    FLEXCOM1_USART_Write((uint8_t*)"Adding 10 characters to the TX buffer - ", sizeof("Adding 10 characters to the TX buffer - "));    
    
    /* Wait for all bytes to be transmitted out */
    while (FLEXCOM1_USART_WriteCountGet() != 0);    
    
    FLEXCOM1_USART_Write((uint8_t*)"0123456789", 10);           
        
    /* Print the amount of free space available in the TX buffer. This should be 10 bytes less than the configured write buffer size. */
    nBytes = sprintf((char*)txBuffer, "\r\nFree Space in Transmit Buffer = %d\r\n", (int)FLEXCOM1_USART_WriteFreeBufferCountGet());

    FLEXCOM1_USART_Write((uint8_t*)txBuffer, nBytes);    
    
    /* Let's enable notifications to get notified when the TX buffer is empty */
    FLEXCOM1_USART_WriteThresholdSet(FLEXCOM1_USART_WriteBufferSizeGet());   
    
    /* Enable notifications */
    FLEXCOM1_USART_WriteNotificationEnable(true, false);
   
    /* Wait for the TX buffer to become empty. Flag "txThresholdEventReceived" is set in the callback. */
    while (txThresholdEventReceived == false);
    
    txThresholdEventReceived = false;    
    
    /* Disable TX notifications */
    FLEXCOM1_USART_WriteNotificationEnable(false, false);
    
    FLEXCOM1_USART_Write((uint8_t*)"Enter 10 characters. The received characters are echoed back. \r\n>", sizeof("Enter 10 characters. The received characters are echoed back. \r\n>"));               
            
    /* Wait till 10 (or more) characters are received */
    while (FLEXCOM1_USART_ReadCountGet() < 10);
    
    /* At-least 10 characters are available in the RX buffer. Read out into the application buffer */
    FLEXCOM1_USART_Read((uint8_t*)rxBuffer, 10);  
    
    /* Echo the received data */
    FLEXCOM1_USART_Write((uint8_t*)rxBuffer, 10);    
    
    /* Now demonstrating receiver notifications */
    FLEXCOM1_USART_Write((uint8_t*)"\r\n Now turning on RX notifications \r\n>", sizeof("\r\n Now turning on RX notifications \r\n>"));
    
    /* For demonstration purpose, set a threshold value to receive a callback after every 5 characters are received */
    FLEXCOM1_USART_ReadThresholdSet(5);
    
    /* Enable RX event notifications */
    FLEXCOM1_USART_ReadNotificationEnable(true, false);
                   
    while(1)
    {
        /* Wait until at-least 10 characters are entered by the user */
        while (nBytesRead < 10);    
    
        /* Echo the received data */
        FLEXCOM1_USART_Write((uint8_t*)rxBuffer, nBytesRead);
        
        FLEXCOM1_USART_Write((uint8_t*)"\r\n>", 3);

        nBytesRead = 0;
    }

    /* Execution should not come here during normal operation */

    return ( EXIT_FAILURE );
}

/*******************************************************************************
 End of File
*/

