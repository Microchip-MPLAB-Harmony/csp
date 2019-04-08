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

/*************************************************************************************
FLEXCOM USART - Connect USB UART click board to mikroBUS Xplained Pro extension Board.
              - Connect mikroBUS Xplained Pro extension Board to XPRO EXT2 Connector.
*************************************************************************************/

#define RX_BUFFER_SIZE 255

#define LED_Toggle()                       LED_GREEN_Toggle()

char messageStart[] = "**** FLEXCOM USART Line Echo Demo ****\r\n\
**** Demo uses blocking model of FLEXCOM USART PLIB. ****\r\n\
**** Enter a line of characters, press ENTER key and observe it echo back. ****\
\r\n**** LED toggles on each time the line is echoed ****\r\n";
char newline[] = "\r\n";
char errorMessage[] = "\r\n**** FLEXCOM USART error has occurred ****\r\n";
char receiveBuffer[RX_BUFFER_SIZE];
uint8_t rxCounter = 0;
char data = 0;

// *****************************************************************************
// *****************************************************************************
// Section: Main Entry Point
// *****************************************************************************
// *****************************************************************************
//
static void echoBuffer(void)
{
    FLEXCOM5_USART_Write(receiveBuffer,rxCounter);
    FLEXCOM5_USART_Write(newline,sizeof(newline));
    rxCounter = 0;
}

int main ( void )
{

    /* Initialize all modules */
    SYS_Initialize ( NULL );

    /* LED Off */
    LED_RED_Clear();
    LED_GREEN_Clear();
    LED_BLUE_Clear();

    /* Send start message */
    FLEXCOM5_USART_Write(&messageStart, sizeof(messageStart));

    while ( true )
    {
        /* Check if there is a received character */
        if(FLEXCOM5_USART_ReceiverIsReady() == true)
        {
            if(FLEXCOM5_USART_ErrorGet() == FLEXCOM_USART_ERROR_NONE)
            {
                FLEXCOM5_USART_Read(&data, 1);

                if((data == '\n') || (data == '\r'))
                {
                    echoBuffer();
                    LED_Toggle();
                }
                else
                {
                    receiveBuffer[rxCounter++] = data;
                    if(rxCounter == RX_BUFFER_SIZE)
                      echoBuffer();
                }
            }
            else
            {
                FLEXCOM5_USART_Write(errorMessage,sizeof(errorMessage));
            }
        }
    }

    /* Execution should not come here during normal operation */

    return ( EXIT_FAILURE );
}


/*******************************************************************************
 End of File
*/

