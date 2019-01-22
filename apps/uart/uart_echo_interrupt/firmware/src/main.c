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
* Copyright (C) 2018-19 Microchip Technology Inc. and its subsidiaries.
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
#include "device.h"

#define RX_BUFFER_SIZE 10
char messageStart[] = "**** UART echo interrupt demo ****\r\n\
**** Type a buffer of 10 characters and observe it echo back ****\r\n\
**** LED toggles on each time the buffer is echoed ****\r\n";
char receiveBuffer[RX_BUFFER_SIZE] = {};
char echoBuffer[2*RX_BUFFER_SIZE] = {};
char messageError[] = "**** UART error occurred ****\r\n";

bool errorStatus = false;
bool writeStatus = false;
bool readStatus = false;

/*LED Toggling subroutines*/
void LED1_Initialize(void)
{
    *(&ODCBSET + (7 - 1) * 0x40) = 0;
    *(&LATB + (7 - 1) * 0x40) = 0;
    *(&TRISBCLR + (7 - 1) * 0x40) = 7;  //think mask val is right
    *(&CNCONBSET + (7 - 1) * 0x40) = _CNCONB_ON_MASK;
    *(&ANSELBCLR + (7 - 1) * 0x40) = 0xFF8F;  //think mask val is right
    *(&CNENBSET + (7 - 1) * 0x40) = 0;
    *(&CNPUBSET + (7 - 1) * 0x40) = 0;
    *(&CNPDBSET + (7 - 1) * 0x40) = 0;    
}

#define LED1_Toggle()   *(&LATBINV + (7 - 1) * 0x40) = 1<<0;
#define LED1_SET()      *(&LATBSET + (7 - 1) * 0x40) = 1<<0;

 //Convenient macrso to do IOUNLOCK
#define PPSUnLock() {SYSKEY=0x0;SYSKEY=0xAA996655;SYSKEY=0x556699AA;CFGCONbits.IOLOCK=0;} 
#define PPSLock() {SYSKEY=0x0;SYSKEY=0xAA996655;SYSKEY=0x556699AA;CFGCONbits.IOLOCK=1;}

void UART2_PortInitialization(void)
{
     /* RG6 as RX set RG6 to digital;*/
    ANSELGCLR = (1<<6); 
    TRISGSET =  (1<<6); 
    U2RXRbits.U2RXR = 0b0001;
    /* RB14 as TX */
    RPB14Rbits.RPB14R = 0b0010;   
    PPSLock();     
}
        
void APP_WriteCallback(uintptr_t context)
{
    writeStatus = true;
}

void APP_ReadCallback(uintptr_t context)
{
    if(UART2_ErrorGet() != UART_ERROR_NONE)
    {
        /* ErrorGet clears errors, set error flag to notify console */
        errorStatus = true;
    }
    else
    {
        readStatus = true;
    }
}

void APP_FaultCallback(uintptr_t context)
{
    if(UART2_ErrorGet() != UART_ERROR_NONE)
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
    UART2_PortInitialization();
    //LED1_Initialize();

    /* Register callback functions and send start message */
    UART2_FaultCallbackRegister(APP_FaultCallback, 0);
    UART2_WriteCallbackRegister(APP_WriteCallback, 0);
    UART2_ReadCallbackRegister(APP_ReadCallback, 0);
    UART2_Write(&messageStart, sizeof(messageStart));
   // writeStatus = true;
    LED1_SET(); 
    while ( true )
    {
        if(errorStatus == true)
        {
            /* Send error message to console */
            errorStatus = false;
            UART2_Write(&messageError, sizeof(messageError));
        }
        else if(readStatus == true)
        {
            /* Echo back received buffer and Toggle LED */
            readStatus = false;

            strcpy(echoBuffer, receiveBuffer);
            strcat(echoBuffer, "\r\n");

            UART2_Write(&echoBuffer, sizeof(echoBuffer));
            LED1_Toggle();
        }
        else if(writeStatus == true)
        {
            /* Submit buffer to read user data */
            writeStatus = false;
            UART2_Read(&receiveBuffer, sizeof(receiveBuffer));
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

