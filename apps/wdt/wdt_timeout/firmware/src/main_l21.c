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
Copyright (c) 2013-2014 released Microchip Technology Inc.  All rights reserved.

//Microchip licenses to you the right to use, modify, copy and distribute
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
#include "definitions.h"               // SYS function prototypes

volatile bool switch_pressed = false;
void EIC_User_Handler(uintptr_t context)
{
    switch_pressed = true;
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
    printf ("\n\r -------------------------------------------------------------");
    printf ("\n\r                           WDT DEMO                           ");
    printf ("\n\r -------------------------------------------------------------");
    printf ("\n\r Press SW0 to emulate deadlock "); 
    SYSTICK_TimerStart();
    EIC_CallbackRegister(EIC_PIN_2,EIC_User_Handler, 0);
    switch_pressed = false;
    while ( true )
    {
        if(switch_pressed == false)
        {
            if(SYSTICK_TimerPeriodHasExpired())
            {
                LED_Toggle();
                WDT_Clear();
            }
        }
        else
        {   
            printf ("\n\r Emulating deadlock................ ");
            printf ("\n\r WDT should reset device in 4 seconds ");           
            while(1);
        }
    }

    /* Execution should not come here during normal operation */

    return ( EXIT_FAILURE );
}



/*******************************************************************************
 End of File
*/