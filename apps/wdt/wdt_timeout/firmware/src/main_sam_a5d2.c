/*******************************************************************************
  Main Source File

  Company:
    Microchip Technology Inc.
  
  File Name:
    main_sam_a5d2.c

  Summary:
    This file contains a demonstration of the WDT periopheral for the SAM_A5D2.

  Description:
    A simple loop process blinks the LED for user feedback.  Within the loop
    the watch dog receives a 'pet' until the user presses the test push button. 
    The process will then starve the watch petting and the processor will reset.
    A spin lock creates a process starvation emulating a dead lock. 

    The PIT is used to provide a delay for the led blink and is not otherwise
    applicable to the demonstration

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
#include <stdlib.h>                		// Defines EXIT_FAILURE
#include "definitions.h"                // SYS function prototypes

volatile bool switchPressed = false;

void switchHandler( PIO_PIN pin, uintptr_t context )
{
    switchPressed = true;
}
// *****************************************************************************
// *****************************************************************************
// Section: Main Entry Point
// *****************************************************************************
// *****************************************************************************
int main( void )
{
    /* Initialize all modules */
    SYS_Initialize( NULL );
    PIO_PinInterruptCallbackRegister( SWITCH_PIN, switchHandler, (uintptr_t) NULL );
    PIO_PinInterruptEnable( SWITCH_PIN );
    PIT_DelayMs( 500 );

    printf( "\r\n-------------------------------------------------------------" );
    printf( "\r\n                          WDT DEMO" );
    printf( "\r\n-------------------------------------------------------------" );
    printf( "\r\nLED process running.\r\nPress the switch to create a process starvation\r\n" );
    switchPressed = false;
    while( true )
    {
        // watchdog pet
    	WDT_Clear();
        // Led toggle with timer for reasonable blink
        LED_Toggle();
        PIT_DelayMs( 500 );
        if( switchPressed )
        {   
            printf( "Process starvation .................\r\n" );
            printf( "\tDevice reset will occur in 4 seconds\r\n" );
            while( true )
            {
                PIT_DelayMs( 50 );
            }
        }
    }

    /* Execution should not come here during normal operation */
    return( EXIT_FAILURE );
}


/*******************************************************************************
 End of File
*/
