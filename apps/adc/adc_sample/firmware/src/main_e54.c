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

#define ADC_VREF                (3.3f)
#define DAC_COUNT_INCREMENT     (170U)  // Equivalent to 0.1V with the given DAC reference 
#define DAC_COUNT_MAX           (4095U)

uint16_t adc_count;
float input_voltage;
/* Initial value of dac count which is midpoint = 1.2 V*/
uint16_t dac_count = 2048;   

void switch_handler(uintptr_t context )
{
    /* Write next data sample */
    dac_count = dac_count + DAC_COUNT_INCREMENT;
    
    if (dac_count > DAC_COUNT_MAX)
            dac_count = 2048;    
    
    DAC_DataWrite(DAC_CHANNEL_0, dac_count);
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
    
    printf("\n\r---------------------------------------------------------");
    printf("\n\r                    ADC Sample Demo                 ");
    printf("\n\r---------------------------------------------------------\n\r");
    
    ADC0_Enable();
    SYSTICK_TimerStart();
    EIC_CallbackRegister(EIC_PIN_15, switch_handler, (uintptr_t) NULL);
    DAC_DataWrite(DAC_CHANNEL_0, dac_count);
    while (1)
    {
        /* Start ADC conversion */
        ADC0_ConversionStart();

        /* Wait till ADC conversion result is available */
        while(!ADC0_ConversionStatusGet())
        {

        };

        /* Read the ADC result */
        adc_count = ADC0_ConversionResultGet();
        input_voltage = (float)adc_count * ADC_VREF / 4095U;

        printf("ADC Count = 0x%03x, ADC Input Voltage = %d.%02d V \r", adc_count, (int)input_voltage, (int)((input_voltage - (int)input_voltage)*100.0));
        
        SYSTICK_DelayMs(500);
    }

    /* Execution should not come here during normal operation */

    return ( EXIT_FAILURE );
}


/*******************************************************************************
 End of File
*/

