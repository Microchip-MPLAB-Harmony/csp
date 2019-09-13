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


// *****************************************************************************
// *****************************************************************************
// Section: Main Entry Point
// *****************************************************************************
// *****************************************************************************

#define PWM_CHANNEL_MASK_ALL (PWM_CHANNEL_MASK)(PWM_CHANNEL_0_MASK | PWM_CHANNEL_1_MASK | PWM_CHANNEL_2_MASK | PWM_CHANNEL_3_MASK)

volatile bool counter_event = false;

void pwm_callback(uint32_t status, uintptr_t context )
{
  counter_event = true;
}
int main ( void )
{
    /* Initialize all modules */
    SYS_Initialize ( NULL );
    
    printf("************** ***PWM Applications Demo **********************\r\n");
    printf("*Generates 3 PWM signals and one counter event as follows ****\r\n");
    printf("*******PWM0: Period= 1ms , Duty = 25%, Active High ***********\r\n");
    printf("*******PWM1: Period= 10ms , Duty = 50%, Active Low ***********\r\n");
    printf("*******PWM2: Period= 100ms , Duty = 75%, Active High *********\r\n");
    printf("*******Counter event: 1000ms counter overflow ****************\r\n");
    
    PWM_CallbackRegister(pwm_callback, NULL);
   
    PWM_ChannelCounterEventEnable(PWM_CHANNEL_3_MASK);
    
    PWM_ChannelsStart(PWM_CHANNEL_MASK_ALL);
    

    while ( true )
    {
       if(counter_event)
       {
         printf("Counter overflow occured on PWM Channel\r\n");
         counter_event = false;       
       }
        /* Maintain state machines of all polled MPLAB Harmony modules. */
        SYS_Tasks ( );
    }

    /* Execution should not come here during normal operation */

    return ( EXIT_FAILURE );
}


/*******************************************************************************
 End of File
*/

