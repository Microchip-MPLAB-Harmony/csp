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

/***************************************
 * Check PWM outputs on pins
 * Channel 0 PWMH - PA00
 * Channel 0 PWML - PA19
 * Channel 1 PWMH - PA02
 * Channel 1 PWML - PD25
 * Channel 2 PWMH - PC19
 * Channel 2 PWML - PD26
***************************************/

/* Duty cycle increment value */
#define DUTY_INCREMENT (10U)

/* Save PWM period */
uint16_t period;

/* This function is called after PWM0 counter event */
void PWM0_CounterEventHandler(uintptr_t context)
{
    /* duty cycle values */
    static uint16_t duty0 = 0U;
    static uint16_t duty1 = 2500U;
    static uint16_t duty2 = 5000U;

    PWM0_ChannelDutySet(PWM_CHANNEL_0, duty0);
    PWM0_ChannelDutySet(PWM_CHANNEL_1, duty1);
    PWM0_ChannelDutySet(PWM_CHANNEL_2, duty2);
    
    /* Increment duty cycle values */
    duty0 += DUTY_INCREMENT;
    duty1 += DUTY_INCREMENT;
    duty2 += DUTY_INCREMENT;
    
    if (duty0 > period)
        duty0 = 0U;
    if (duty1 > period)
        duty1 = 0U;
    if (duty2 > period)
        duty2 = 0U;
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
    
    /* Register callback function for Channel 0 counter event */
    PWM0_CallbackRegister(PWM0_CounterEventHandler, (uintptr_t)NULL);
    
    /* Read the period */
    period = PWM0_ChannelPeriodGet(PWM_CHANNEL_0);
    
    /* Start all synchronous channels by starting channel 0*/
    PWM0_ChannelsStart(PWM_CHANNEL_0_MASK);

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

