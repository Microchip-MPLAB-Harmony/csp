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

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

#include <stddef.h>                     // Defines NULL
#include <stdbool.h>                    // Defines true
#include <stdlib.h>                     // Defines EXIT_FAILURE
#include <stdio.h>
#include "definitions.h"                // SYS function prototypes

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
    RSTC_RESET_CAUSE ResetCause = RSTC_ResetCauseGet();
    
    /* Initialize all modules */
    SYS_Initialize ( NULL );
    
    printf ("\n\r -------------------------------------------------------------");
    printf ("\n\r                           RSTC DEMO                           ");
    printf ("\n\r -------------------------------------------------------------");
    printf ("\n\r Press RESET button to emulate External Reset"); 
    printf ("\n\r Press SW0 button to emulate Watchdog Timer Reset"); 
    printf ("\n\r Load and run in debug mode to emulate System Reset"); 
    printf ("\n\r ------------------------------------------------------------- \r\n");
    
    SYSTICK_TimerStart();
    EIC_CallbackRegister(EIC_PIN_15,EIC_User_Handler, 0);
    
    switch_pressed = false;
    
    switch(ResetCause)
    {
        case RSTC_RESET_CAUSE_EXT_RESET:
            printf("\r\n Reset type is External Reset");
            break;
        case RSTC_RESET_CAUSE_WDT_RESET:
            printf("\r\n Reset type is Watch Dog Timer Reset");
            break;
        case RSTC_RESET_CAUSE_SYST_RESET:
            printf("\r\n Reset type is System Reset");
            break;
        default:
            printf("\r\n Reset Cause = 0x%02X", (unsigned char)ResetCause);
            break;
    }
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
            printf ("\n\r WDT should reset device in 4 seconds and you will see reset reason as WDT Reset");           
            while(1);
        }
    }

    /* Execution should not come here during normal operation */

    return ( EXIT_FAILURE );
}


/*******************************************************************************
 End of File
*/

