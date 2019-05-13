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
#include "definitions.h"               // SYS function prototypes

#define RESET_REASON_ALL    (RCON_RESET_CAUSE_POR | RCON_RESET_CAUSE_BOR | RCON_RESET_CAUSE_IDLE | RCON_RESET_CAUSE_SLEEP | RCON_RESET_CAUSE_WDTO | \
                            RCON_RESET_CAUSE_SWR | RCON_RESET_CAUSE_EXTR | RCON_RESET_CAUSE_VREGS | RCON_RESET_CAUSE_CMR | RCON_RESET_CAUSE_HVDR)

volatile bool switch_pressed = false;

void switch_handler( GPIO_PIN pin, uintptr_t context )
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
    RCON_RESET_CAUSE ResetCause = RCON_ResetCauseGet();

    /* Initialize all modules */
    SYS_Initialize ( NULL );

    printf ("\n\r -------------------------------------------------------------");
    printf ("\n\r                          RCON DEMO                           ");
    printf ("\n\r -------------------------------------------------------------");

    GPIO_PinInterruptCallbackRegister(SWITCH_PIN, &switch_handler, (uintptr_t) NULL );
    GPIO_PinInterruptEnable(SWITCH_PIN);

    if ((ResetCause & RCON_RESET_CAUSE_WDTO) == RCON_RESET_CAUSE_WDTO)
    {
        printf("\r\n Reset type is Watch Dog Timer Reset");
    }
    if (((ResetCause & RCON_RESET_CAUSE_EXTR) == RCON_RESET_CAUSE_EXTR) || ((ResetCause & RCON_RESET_CAUSE_POR) == RCON_RESET_CAUSE_POR))
    {
        printf("\r\n Reset type is Master Clear Reset(MCLR) or Power on Reset(POR)");
    }
    printf("\r\n Reset Cause = 0x%08X", (unsigned char)ResetCause);

    RCON_ResetCauseClear(RESET_REASON_ALL);
    ResetCause = RCON_ResetCauseGet();
    printf("\r\n After clear all RCON, Reset Cause = 0x%02X", (unsigned char)ResetCause);

    printf ("\n\n\r Press the Switch to emulate Watchdog Timer Reset");
    CORETIMER_Start();
    CORETIMER_DelayMs(1000);
    switch_pressed  = false;
    WDT_Enable();
    while ( true )
    {
        if(switch_pressed == false)
        {
            CORETIMER_DelayMs(1000);
            LED1_Toggle();
            WDT_Clear();
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
