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
#include <string.h>
#include "definitions.h"                // SYS function prototypes

/*************************************************************************************
FLEXCOM USART - Connect USB UART click board to mikroBUS Connector.
*************************************************************************************/

#define RX_BUFFER_SIZE 10

#define LED_Toggle()                       LED_GREEN_Toggle()

char messageStart[] = "**** FLEXCOM USART echo interrupt demo ****\r\n\
**** Type a buffer of 10 characters and observe it echo back ****\r\n\
**** LED toggles on each time the buffer is echoed ****\r\n";
char receiveBuffer[RX_BUFFER_SIZE];
char echoBuffer[2*RX_BUFFER_SIZE];
char messageError[] = "**** FLEXCOM USART error occurred ****\r\n";

bool errorStatus = false;
bool writeStatus = false;
bool readStatus = false;

void APP_WriteCallback(uintptr_t context)
{
    writeStatus = true;
}

void APP_ReadCallback(uintptr_t context)
{
    if(FLEXCOM5_USART_ErrorGet() != FLEXCOM_USART_ERROR_NONE)
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

    /* LED Off */
    LED_RED_Clear();
    LED_GREEN_Clear();
    LED_BLUE_Clear();

    /* Register callback functions and send start message */
    FLEXCOM5_USART_WriteCallbackRegister(APP_WriteCallback, 0);
    FLEXCOM5_USART_ReadCallbackRegister(APP_ReadCallback, 0);
    FLEXCOM5_USART_Write(&messageStart, sizeof(messageStart));

    while ( true )
    {
        if(errorStatus == true)
        {
            /* Send error message to console */
            errorStatus = false;
            FLEXCOM5_USART_Write(&messageError, sizeof(messageError));
        }
        else if(readStatus == true)
        {
            /* Echo back received buffer and Toggle LED */
            readStatus = false;

            memcpy(echoBuffer, receiveBuffer, sizeof (receiveBuffer));
            memcpy(&echoBuffer[RX_BUFFER_SIZE], "\r\n", 2);            

            FLEXCOM5_USART_Write(&echoBuffer, sizeof(echoBuffer));
            LED_Toggle();
        }
        else if(writeStatus == true)
        {
            /* Submit buffer to read user data */
            writeStatus = false;
            FLEXCOM5_USART_Read(&receiveBuffer, sizeof(receiveBuffer));
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

