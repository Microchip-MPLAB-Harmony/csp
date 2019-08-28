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
    EIC_CallbackRegister(EIC_PIN_15,EIC_User_Handler, 0);
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