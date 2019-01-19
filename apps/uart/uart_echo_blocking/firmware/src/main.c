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


#define RX_BUFFER_SIZE 256

char messageStart[] = "**** UART Line Echo Demo ****\r\n\
**** Demo uses blocking model of UART PLIB. ****\r\n\
**** Enter a line of characters, press ENTER key and observe it echo back. ****\
\r\n**** LED toggles on each time the line is echoed ****\r\n";
char newline[] = "\r\n";
char errorMessage[] = "\r\n**** UART error has occurred ****\r\n";
char receiveBuffer[RX_BUFFER_SIZE] = {};
char data = 0;

/*LED Toggling subroutines*/
void LED1_Initialize(void)
{
   *(&ODCBSET + (7 - 1) * 0x40) = 0;
    *(&LATB + (7 - 1) * 0x40) = 0;
    *(&TRISBCLR + (7 - 1) * 0x40) = 7;  
    *(&CNCONBSET + (7 - 1) * 0x40) = _CNCONB_ON_MASK;
    *(&ANSELBCLR + (7 - 1) * 0x40) = 0xFF8F;  
    *(&CNENBSET + (7 - 1) * 0x40) = 0;
    *(&CNPUBSET + (7 - 1) * 0x40) = 0;
    *(&CNPDBSET + (7 - 1) * 0x40) = 0;    
}

#define LED1_Toggle()   *(&LATBINV + (7 - 1) * 0x40) = 1<<0;
#define LED1_SET()      *(&LATBSET + (7 - 1) * 0x40) = 1<<0;

 //Convenient macro to do IOUNLOCK
#define PPSUnLock() {SYSKEY=0x0;SYSKEY=0xAA996655;SYSKEY=0x556699AA;CFGCONbits.IOLOCK=0;} 
#define PPSLock() {SYSKEY=0x0;SYSKEY=0xAA996655;SYSKEY=0x556699AA;CFGCONbits.IOLOCK=1;}

void UART2_PortInitialization(void)
{
    /* set RG6 to digital input for UART2*/
    ANSELGCLR = (1<<6); //
    TRISGSET = (1<<6); //
    /* Peripheral Pin Select (PPS) Settings for UART2 */
    PPSUnLock();
    U2RXRbits.U2RXR = 0x1; 
    RPB14Rbits.RPB14R = 0x2;
    PPSLock();     
}
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
    UART2_PortInitialization();
    LED1_Initialize();
    LED1_SET();

    /* Send start message */
    UART2_Write(&messageStart, sizeof(messageStart));
    while ( true )
    {
        /* Check if there is a received character */
        if(UART2_ReceiverIsReady() == true)
        {
            if(UART2_ErrorGet() == UART_ERROR_NONE)
            {
                UART2_Read(&data, 1);

                if((data == '\n') || (data == '\r'))
                {
                    UART2_Write(receiveBuffer,rxCounter);
                    UART2_Write(newline,sizeof(newline));
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
                UART2_Write(errorMessage,sizeof(errorMessage));
            }
        }
    }

    /* Execution should not come here during normal operation */

    return ( EXIT_FAILURE );
}

/*******************************************************************************
 End of File
*/

