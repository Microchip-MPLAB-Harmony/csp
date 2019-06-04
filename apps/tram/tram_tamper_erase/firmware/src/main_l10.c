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
* Copyright (C) 2019 Microchip Technology Inc. and its subsidiaries.
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
#include "definitions.h"         		// SYS function prototypes

volatile bool tamper_detected;

void RTC_Callback(RTC_TIMER32_INT_MASK int_cause , uintptr_t  context)
{
    if (int_cause & RTC_TIMER32_INT_MASK_TAMPER)
	{
        tamper_detected = true;
        RTC_REGS->MODE0.RTC_TAMPID = RTC_TAMPID_Msk;
        LED_Toggle();
	}
}
// *****************************************************************************
// *****************************************************************************
// Section: Main Entry Point
// *****************************************************************************
// *****************************************************************************
void populateTram(void)
{
    printf("\n\rPopulating TRAM:-");
    for(uint8_t i = 0; i < 31; i++)
    {
        TRAM_REGS->TRAM_RAM[i] = ~(1 << i);
        if(i < 10)
        {
            printf("\n\rTRAM register %d value:-    0x%08lx", i, TRAM_REGS->TRAM_RAM[i]);
        }
        else
        {
            printf("\n\rTRAM register %d value:-   0x%08lx", i, TRAM_REGS->TRAM_RAM[i]);
        }
        
    }
}
int main ( void )
{
    /* Initialize all modules */
    SYS_Initialize ( NULL );
    tamper_detected = false;
    printf("\n\r---------------------------------------------------------");
    printf("\n\r                    TRAM Tamper Demo                 ");
    printf("\n\r---------------------------------------------------------\n\r");

    populateTram();
    
    RTC_Timer32CallbackRegister(RTC_Callback, (uintptr_t) NULL);
    RTC_Timer32Start();
    
    while ( true )
    {
        if(tamper_detected == true)
        {
            printf("\n\r---------------------------------------------------------");
            printf("\n\rTamper Detected !!!!!!!!! ");
            printf("\n\r---------------------------------------------------------");
            for(uint8_t i = 0; i < 31; i++)
            {
                if(i < 10)
                {
                    printf("\n\rTRAM register %d value:-    0x%08lx", i, TRAM_REGS->TRAM_RAM[i]);
                }
                else
                {
                    printf("\n\rTRAM register %d value:-   0x%08lx", i, TRAM_REGS->TRAM_RAM[i]);
                }
            }
            tamper_detected = false;
        }
    }

    /* Execution should not come here during normal operation */

    return ( EXIT_FAILURE );
}


/*******************************************************************************
 End of File
*/