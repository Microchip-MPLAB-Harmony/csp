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
Copyright (c) 2018-2019 released Microchip Technology Inc.  All rights reserved.

Microchip licenses to you the right to use, modify, copy and distribute
Software only when embedded on a Microchip microcontroller or digital signal
controller that is integrated into your product or third party product
(pursuant to the sublicense terms in the accompanying license agreement).

You should refer to the license agreement accompanying this Software for
additional information regarding your rights and obligations.

SOFTWARE AND DOCUMENTATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND,
EITHER EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION, ANY WARRANTY OF
MERCHANTABILITY, TITLE, NON-INFRINGEMENT AND FITNESS FOR A PARTICULAR PURPOSE.
IN NO EVENT SHALL MICROCHIP OR ITS LICENSORS BE LIABLE OR OBLIGATED UNDER
CONTRACT, NEGLIGENCE, STRICT LIABILITY, CONTRIBUTION, BREACH OF WARRANTY, OR
OTHER LEGAL EQUITABLE THEORY ANY DIRECT OR INDIRECT DAMAGES OR EXPENSES
INCLUDING BUT NOT LIMITED TO ANY INCIDENTAL, SPECIAL, INDIRECT, PUNITIVE OR
CONSEQUENTIAL DAMAGES, LOST PROFITS OR LOST DATA, COST OF PROCUREMENT OF
SUBSTITUTE GOODS, TECHNOLOGY, SERVICES, OR ANY CLAIMS BY THIRD PARTIES
(INCLUDING BUT NOT LIMITED TO ANY DEFENSE THEREOF), OR OTHER SIMILAR COSTS.
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
#include "definitions.h"                // SYS function prototypes
#include <string.h>
#include "device.h"
// *****************************************************************************
// *****************************************************************************
// Section: Main Entry Point
// *****************************************************************************
// *****************************************************************************

uint8_t txData[]  = "LOOPBACK DEMO FOR SPI3!";
uint8_t rxData[sizeof(txData)];

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
#define LED1_CLEAR()      *(&LATBCLR + (7 - 1) * 0x40) = 1<<0;
 
/* Convenient macros to do IOUNLOCK */
#define PPSUnLock() {SYSKEY=0x0;SYSKEY=0xAA996655;SYSKEY=0x556699AA;CFGCONbits.IOLOCK=0;} 
#define PPSLock() {SYSKEY=0x0;SYSKEY=0xAA996655;SYSKEY=0x556699AA;CFGCONbits.IOLOCK=1;}

void SPI_PortInitialization(void)
{
   //Peripheral Pin Select (PPS) Settings for SPI
   
   PPSUnLock(); 
    /* CLK SCK3 = J12->10*/
   /*Set RA14 for SDI3 J12-7 */
   SDI3Rbits.SDI3R = 0x000D; // 
   /*Set RD10 for SDO3 J12-37 */
   RPD10Rbits.RPD10R = 0x0007; 
   /* Set RG6 for CS3 J12-8 */
   RPG6Rbits.RPG6R = 0x0007;
   PPSLock();   
}

/* To perform this demo connect pin 7 and 37 at connector J12 on stater kit*/ 
int main ( void )
{
    /* Initialize all modules */
    SYS_Initialize ( NULL );
    SPI_PortInitialization();
    /* SPI Write Read */
    SPI3_WriteRead(&txData, sizeof(txData), &rxData, sizeof(rxData));
    /* Compare received data with the transmitted data */
    if ((memcmp(txData, rxData, sizeof(txData)) == 0))
    {
            /* Pass: Received data is same as transmitted data */
            LED1_CLEAR();
    }
    else
    {
			/* Fail: Received data is not same as transmitted data */
            LED1_SET();
    }

    while ( true )
    {

    }

    /* Execution should not come here during normal operation */

    return ( EXIT_FAILURE );
}

/*******************************************************************************
 End of File
*/
