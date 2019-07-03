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
#include "definitions.h"                // SYS function prototypes

/***************************************
 * Check PWM outputs on pins
 * Channel 1 PWMH - PB14
 * Channel 1 PWML - PB15
 * Channel 2 PWMH - PB12
 * Channel 2 PWML - PB13
 * Channel 3 PWMH - PB10
 * Channel 3 PWML - PB11
***************************************/

/* Duty cycle increment value */
#define DUTY_INCREMENT (10U)

/* Save PWM period */
uint16_t period;

/* This function is called after PWM0 counter event */
void PWM_PeriodHandler(uint32_t status, uintptr_t context)
{
    /* duty cycle values */
    static uint16_t duty0 = 0U;
    static uint16_t duty1 = 1000U;
    static uint16_t duty2 = 2000U;

    MCPWM_ChannelPrimaryDutySet(MCPWM_CH_1, duty0);
    MCPWM_ChannelPrimaryDutySet(MCPWM_CH_2, duty1);
    MCPWM_ChannelPrimaryDutySet(MCPWM_CH_3, duty2);
    
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
    MCPWM_CallbackRegister(MCPWM_CH_1, PWM_PeriodHandler, (uintptr_t)NULL);
    
    /* Read the period */
    period = MCPWM_PrimaryPeriodGet();
    
    /* Start all synchronous channels by starting channel 0*/
    MCPWM_Start();

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

