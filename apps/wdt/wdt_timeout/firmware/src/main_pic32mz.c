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

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

#include <stddef.h>                     // Defines NULL
#include <stdbool.h>                    // Defines true
#include <stdlib.h>                     // Defines EXIT_FAILURE
#include "definitions.h"                // SYS function prototypes
#include "device.h"

// *****************************************************************************
// *****************************************************************************
// Section: Main Entry Point
// *****************************************************************************
// *****************************************************************************

/* Replace when pin manager is in place */
void LED_Initialize(void)
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

bool switch_get_state(void)
{
    /* Switch is on PORTA, bit0.  It is pulled up, so a "not pressed" state returns true. */
    return (bool)(*(&PORTA)& 0x1);
}
void switch_Initialize(void)  /* Sets up PortA, bit 0 as GPIO input */
{
    *(&ODCACLR) = 1;
    *(&CNPDACLR) = 1;
    *(&CNPUASET) = 1;
    *(&ANSELACLR) = 1;
    *(&TRISASET) = 1;
}
#define LED_Toggle()   *(&LATBINV + (7 - 1) * 0x40) = 1<<0;
#define LED_On()       *(&LATBSET + (7 - 1) * 0x40) = 1<<0;
#define LED_Off()      *(&LATBCLR + (7 - 1) * 0x40) = 1<<0;
/* end replace when pin manager is in place */

/* Press button S1 to start emulating deadlock condition.  The LED will strobe
   the following sequence:  ON->OFF->ON.  This indicates the board went through
   a reset (and started up main() again)                                       */

/***********************************************************************
   Note about this app:  delay is currently set to about 3 seconds.  
   If WDTPS setting in Harmony (system, DEVCFG1) is less than delay time,
   board will be in constant reset and LED will never turn on.
 ***********************************************************************/
int main ( void )
{
    int ii;   /* Remove when timer PLIB is in place */
    bool switch_state = true;
    
    /* Initialize all modules */
    SYS_Initialize ( NULL );

    switch_Initialize();
    LED_Initialize();  /* Replace when pin manager is in place */
    LED_Off();         /* Turns off upon a reset occurring */
    for(ii=0; ii<5*10e6; ii++)  /* Small delay for user to see LED blink.  Replace when timer PLIB is in place */
        ;    
    LED_On();

    while ( true )
    {
        if(true == switch_state)
        {
            switch_state = switch_get_state();
        }
        if(true == switch_state)  /* If not S1 pressed */
        {
            WDT_Clear();
        }
        else  /* S1 was just pressed by user */
        {
            /* Emulating deadlock:  will timeout a period of WDTPS later. */
            while(1)
                ;
        }
    }

    /* Execution should not come here during normal operation */
    return ( EXIT_FAILURE );
}


/*******************************************************************************
 End of File
*/

