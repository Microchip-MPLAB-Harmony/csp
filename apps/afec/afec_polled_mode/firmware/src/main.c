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
// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

#include <stddef.h>                     // Defines NULL
#include <stdbool.h>                    // Defines true
#include <stdlib.h>                     // Defines EXIT_FAILURE
#include <stdio.h>
#include "definitions.h"                // SYS function prototypes

#define AFEC_VREF               (3.3f)
#define DAC_COUNT_INCREMENT     (124U)  // equivalent to 0.1V 
#define DAC_COUNT_MAX           (4095U)

uint16_t adc_count;
float input_voltage;
/* Initial value of dac count which is midpoint = 1.65 V*/
uint16_t dac_count = 0x800;   


void switch_handler( PIO_PIN pin, uintptr_t context )
{
    /* Write next data sample */
    dac_count = dac_count + DAC_COUNT_INCREMENT;
    
    if (dac_count > DAC_COUNT_MAX)
            dac_count=0;    
    
    DACC_DataWrite(DACC_CHANNEL_0, dac_count);
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
    
    PIO_PinInterruptCallbackRegister(PIO_PIN_PA11, &switch_handler, (uintptr_t) NULL );
    PIO_PinInterruptEnable(SWITCH_PIN);
    
    printf("\n\r---------------------------------------------------------");
    printf("\n\r                    AFEC Demo                 ");
    printf("\n\r---------------------------------------------------------\n\r");
    printf("Press switch to change the DAC output. \r\n");
    
    SYSTICK_TimerStart();

    DACC_DataWrite(DACC_CHANNEL_0, dac_count);
        
    while (1)
    {
        /* Start ADC conversion */
        AFEC1_ConversionStart();

        /* Wait till ADC conversion result is available */
        while(!AFEC1_ChannelResultIsReady(AFEC_CH0))
        {

        };

        /* Read the ADC result */
        adc_count = AFEC1_ChannelResultGet(AFEC_CH0);
        input_voltage = (float)adc_count * AFEC_VREF / 4095U;

        printf("ADC Count = 0x%03x, ADC Input Voltage = %0.2f V \r",adc_count, input_voltage);    
        
        SYSTICK_DelayMs(500);
    }
    
    /* Execution should not come here during normal operation */

    return ( EXIT_FAILURE );
}


/*******************************************************************************
 End of File
*/


