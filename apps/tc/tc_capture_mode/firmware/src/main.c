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
Copyright (c) 2017 released Microchip Technology Inc.  All rights reserved.

Microchip licenses to you the right to use, modify, copy and distribute
Software only when embedded on a Microchip microcontroller or digital signal
controller that is integrated into your product or third party product
(pursuant to the sublicense terms in the accompanying license agreement).

You should refer to the license agreement accompanying this Software for
additional information regarding your rights and obligations.

SOFTWARE AND DOCUMENTATION ARE PROVIDED AS IS  WITHOUT  WARRANTY  OF  ANY  KIND,
EITHER EXPRESS  OR  IMPLIED,  INCLUDING  WITHOUT  LIMITATION,  ANY  WARRANTY  OF
MERCHANTABILITY, TITLE, NON-INFRINGEMENT AND FITNESS FOR A  PARTICULAR  PURPOSE.
IN NO EVENT SHALL MICROCHIP OR  ITS  LICENSORS  BE  LIABLE  OR  OBLIGATED  UNDER
CONTRACT, NEGLIGENCE, STRICT LIABILITY, CONTRIBUTION,  BREACH  OF  WARRANTY,  OR
OTHER LEGAL  EQUITABLE  THEORY  ANY  DIRECT  OR  INDIRECT  DAMAGES  OR  EXPENSES
INCLUDING BUT NOT LIMITED TO ANY  INCIDENTAL,  SPECIAL,  INDIRECT,  PUNITIVE  OR
CONSEQUENTIAL DAMAGES, LOST  PROFITS  OR  LOST  DATA,  COST  OF  PROCUREMENT  OF
SUBSTITUTE  GOODS,  TECHNOLOGY,  SERVICES,  OR  ANY  CLAIMS  BY  THIRD   PARTIES
(INCLUDING BUT NOT LIMITED TO ANY DEFENSE  THEREOF),  OR  OTHER  SIMILAR  COSTS.
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

/* Input waveform - compare value increment*/
#define CMP_VAL_INCREMENT (600U)

/* Calculated duty cycle of the input waveform in %*/
float duty;
/* Calculated frequency of the input waveform in Hz*/
float frequency;

// *****************************************************************************
// *****************************************************************************
// Section: Main Entry Point
// *****************************************************************************
// *****************************************************************************

int main ( void )
{
    uint16_t period, on_time, off_time;
    uint16_t cmp_period, cmp_val=0; 
    
    /* Initialize all modules */
    SYS_Initialize ( NULL );

    SYSTICK_TimerStart();
    cmp_period = TC1_CH2_ComparePeriodGet();
    TC0_CH0_CaptureStart();
    TC1_CH2_CompareStart();

    printf("*********** CAPTURE DEMO **************");
    printf("\r\n"); 
    
    while ( true )
    {
        /* Change the duty cycle of the input waveform  */
        cmp_val += CMP_VAL_INCREMENT;
        if (cmp_val >= cmp_period)
        {
            cmp_val = CMP_VAL_INCREMENT;
        }
        TC1_CH2_CompareBSet(cmp_val);
        
        /* Wait for compare event */
        while((TC0_CH0_CaptureStatusGet() & TC_CAPTURE_B_LOAD) != TC_CAPTURE_B_LOAD);
        
        /* Read Captured values */ 
        off_time = TC0_CH0_CaptureAGet();
        period = TC0_CH0_CaptureBGet();

        /* Compute Duty Cycle in percentage and Frequency in Hz */
        on_time = period - off_time;
        duty = ((on_time) * 100U) / period;
        frequency = (TC0_CH0_CaptureFrequencyGet() / period);
        
        /* Send the measured data to console for display  */
        printf("Frequency of waveform: %.2f Hz \t Duty Cycle of waveform: %.2f %%", frequency, duty);
        printf("\r\n"); 
                
        /* Wait for 1 second */ 
        SYSTICK_DelayMs(1000);
    }

    /* Execution should not come here during normal operation */

    return ( EXIT_FAILURE );
}


/*******************************************************************************
 End of File
*/

