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

// DOM-IGNORE-BEGIN
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
// DOM-IGNORE-END

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

#define RX_BUFFER_SIZE 10
#define LED_ON    LED_Clear
#define LED_OFF   LED_Set

char messageStart[] = "****  USART echo demo: Non-blocking Transfer with the interrupt  ****\r\n\
**** Type 10 characters. The received characters are echoed back, and the LED is toggled ****\r\n";
char receiveBuffer[RX_BUFFER_SIZE] = {};
char echoBuffer[RX_BUFFER_SIZE+4] = {};
char messageError[] = "**** USART error occurred ****\r\n";

bool errorStatus = false;
bool writeStatus = false;
bool readStatus = false;


void APP_WriteCallback(uintptr_t context)
{
    writeStatus = true;
}

void APP_ReadCallback(uintptr_t context)
{
    if(SERCOM3_USART_ErrorGet() != USART_ERROR_NONE)
    {
        /* ErrorGet clears errors, set error flag to notify console */
        errorStatus = true;
    }
    else
    {
        readStatus = true;
    }
}

// *****************************************************************************
// *****************************************************************************
// Section: Main Entry Point
// *****************************************************************************
// *****************************************************************************

int main ( void )
{
    /* Initialize all modules */
    SYS_Initialize ( NULL );

    /* Register callback functions and send start message */
    SERCOM3_USART_WriteCallbackRegister(APP_WriteCallback, 0);
    SERCOM3_USART_ReadCallbackRegister(APP_ReadCallback, 0);
    SERCOM3_USART_Write(&messageStart[0], sizeof(messageStart));

    while ( true )
    {
        if(errorStatus == true)
        {
            /* Send error message to console */
            errorStatus = false;
            SERCOM3_USART_Write(&messageError[0], sizeof(messageError));
        }
        else if(readStatus == true)
        {
            /* Echo back received buffer and Toggle LED */
            readStatus = false;

            echoBuffer[0] = '\n';
            echoBuffer[1] = '\r';
            memcpy(&echoBuffer[2], receiveBuffer,sizeof(receiveBuffer));
            echoBuffer[RX_BUFFER_SIZE+2] = '\n';
            echoBuffer[RX_BUFFER_SIZE+3] = '\r';

            SERCOM3_USART_Write(&echoBuffer[0], sizeof(echoBuffer));
            LED_Toggle();
        }
        else if(writeStatus == true)
        {
            /* Submit buffer to read user data */
            writeStatus = false;
            SERCOM3_USART_Read(&receiveBuffer[0], sizeof(receiveBuffer));
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


/*******************************************************************************
 End of File
*/

