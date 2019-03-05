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
//  This program demonstrates the capture feature of the Timer controller. It 
//  generates a PWM signal on one timer channel. The duty cycle of the signal 
//  is changed dynamically. Signal is then is provided as input to to another  
//  timer channel configured in capture mode and the measured duty cycle is 
//  output on the console. 
//  PWM signal is generated on Timer 1 Channel 0 (Pin PD30 accessible through
//  8th pin of connector J8). Signal is captured on Timer 0 Channel 2 (PIN PB22
//  accessible through 6th pin of connector J22).
// *****************************************************************************
// *****************************************************************************

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
#define CMP_VAL_INCREMENT (345U)

/* Calculated duty cycle of the input waveform in %*/
float duty;
/* Calculated frequency of the input waveform in Hz*/
float frequency;

/* Interrupt counter */
volatile uint32_t interrupt_counter = 0;

// *****************************************************************************
// *****************************************************************************
// Section: Main Entry Point
// *****************************************************************************
// *****************************************************************************

void TC1_DelayMs(uint32_t delay);


/* This function is called after period expires */
void TC1_CH1_TimerInterruptHandler(TC_TIMER_STATUS status, uintptr_t context)
{
   if(interrupt_counter > 0)
   {
     interrupt_counter --;
   }
}

int main ( void )
{
    uint16_t period, on_time, off_time;
    uint16_t cmp_period, cmp_val=0; 
    
    /* Initialize all modules */
    SYS_Initialize ( NULL );
    
    /* Register callback function for TC1 CH1 period interrupt, it is used for
       timing operations*/
    TC1_CH1_TimerCallbackRegister(TC1_CH1_TimerInterruptHandler, (uintptr_t)NULL);
    
    /* Start the timer channel 0*/
    TC1_CH1_TimerStart();

    cmp_period = TC1_CH0_ComparePeriodGet();
    TC0_CH2_CaptureStart();
    TC1_CH0_CompareStart();
    
    /* Wait for 1 second  for UART to initialize */ 
    TC1_DelayMs(1000);

    printf("\n\r---------------------------------------------------------");
    printf("\n\r                    TC Capture Demo                 ");
    printf("\n\r---------------------------------------------------------\n\r"); 
    
    printf("Connect input signal to Timer 0 Channel 2 (Pin PB22).\n\n\r");
    
    while ( true )
    {
        /* Change the duty cycle of the input waveform  */
        cmp_val += CMP_VAL_INCREMENT;
        if (cmp_val >= cmp_period)
        {
            cmp_val = CMP_VAL_INCREMENT;
        }
        TC1_CH0_CompareBSet(cmp_val);
        
        /* Wait for compare event */
        while((TC0_CH2_CaptureStatusGet() & TC_CAPTURE_B_LOAD) != TC_CAPTURE_B_LOAD);
        
        /* Read Captured values */ 
        off_time = TC0_CH2_CaptureAGet();
        period = TC0_CH2_CaptureBGet();

        /* Compute Duty Cycle in percentage and Frequency in Hz */
        on_time = period - off_time;
        duty = ((on_time) * 100U) / period;
        frequency = (TC0_CH2_CaptureFrequencyGet() / period);
        
        /* Send the measured data to console for display  */
        printf("Frequency of waveform: %.2f Hz \t Duty Cycle of waveform: %.2f %%", frequency, duty);
        printf("\r\n"); 
                
        /* Wait for 1 second */ 
        TC1_DelayMs(1000);
    }

    /* Execution should not come here during normal operation */
    return ( EXIT_FAILURE );
}

/* Delay function */
void TC1_DelayMs(uint32_t delay)
{
  interrupt_counter = delay;
  while(interrupt_counter > 0);
}


/*******************************************************************************
 End of File
*/

