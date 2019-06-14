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

/* Define aliases for the LCD data and command registers */
#define DATAREG         1  /* Data register */
#define CMDREG          0  /* Command register */

// *****************************************************************************
// *****************************************************************************
// Section: Main Entry Point
// *****************************************************************************
// *****************************************************************************

static void LCD_Initialize( void )
{
    /* Configure general PMP options - enable read/write strobes, long waits, etc */
    PMP_AddressSet(0x1);
    PMP_AddressPortEnable(0x1);

    /* LCD needs 60ms to power on and perform startup functions */
    CORETIMER_DelayMs(60);

    /* Access the LCD command register */
    PMP_AddressSet(CMDREG);

    /* LCD Function Set - 8-bit interface, 2 lines, 5*7 Pixels */
    PMP_MasterSend(0x38);
    
    /* Needs a 40us delay to complete */
    CORETIMER_DelayMs(1);

    /* Turn on display (with cursor hidden) */
    PMP_MasterSend(0x0C);
    
    /* Needs a 40us delay to complete */
    CORETIMER_DelayMs(1);

    /* Clear the display */
    PMP_MasterSend(0x01);
    
    /* Needs a 1.64ms delay to complete */
    CORETIMER_DelayMs(2);

    /* Set text entry mode - auto increment, no shift */
    PMP_MasterSend(0x06);

    /* Needs a 40us delay to complete */
    CORETIMER_DelayMs(1);
}

static void LCD_Write( int reg, char c )
{
    /* Either 'DATAREG' or 'CMDREG' */
    PMP_AddressSet(reg);

    PMP_MasterSend(c);

    while(PMP_PortIsBusy() == true);
    
    /* 40us needed in between each write */
    CORETIMER_DelayMs(100);
}

static void writeString( char *string )
{
    while(*string)
    {
        /* Send characters one by one */
        LCD_Write(DATAREG, *string++);
    }
}

static void newLine( void )
{
    /* Cursor address 0x80 + 0x40 = 0xC0 */
    LCD_Write(CMDREG, 0xC0);
}

int main ( void )
{
    /* Initialize all modules */
    SYS_Initialize ( NULL );

    CORETIMER_Start();
    
    /* Initialize LCD */
    LCD_Initialize();

    /* Turn on blinking cursor */
    LCD_Write(CMDREG, 0x0F);
    
    /* Write string to the LCD */
    writeString("WELCOME");

    /* Set cursor to line two */
    newLine();

    /* Print another string */
    writeString("HARMONY 3!!!");
    
    while ( true )
    {
        /* Maintain state machines of all polled MPLAB Harmony modules. */
        SYS_Tasks ( );
    }

    /* Execution should not come here during normal operation */

    return ( EXIT_FAILURE );
}


/*******************************************************************************
 End of File
*/

