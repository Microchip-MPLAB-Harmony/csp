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
#include "definitions.h"                // SYS function prototypes

/*****************************************************
 ADC CH0 - PD19 - Connect to Vcc
 ADC CH5 - PD24 - connect to Vcc
 ADC_CH6 - PD25 - Connect to GND
 *****************************************************/

#define ADC_VREF               (3.3f)

uint16_t adc_ch0_count, adc_ch5_count, adc_ch6_count;

float adc_ch0_voltage, adc_ch5_voltage, adc_ch6_voltage;

volatile bool result_ready;

/* This function is called after conversion of last channel in the user sequence */
void ADC_EventHandler(uintptr_t context)
{
    /* Read the result of 3 channels*/
    adc_ch5_count = ADC_ChannelResultGet(ADC_CH5);
    adc_ch6_count = ADC_ChannelResultGet(ADC_CH6);
    adc_ch0_count = ADC_ChannelResultGet(ADC_CH0);
       
    result_ready = true;

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
    
    /* Register callback function for ADC end of conversion interrupt*/
    ADC_CallbackRegister(ADC_EventHandler, (uintptr_t)NULL);
    
    printf("\n\r---------------------------------------------------------");
    printf("\n\r                    ADC User Sequence Demo                 ");
    printf("\n\r---------------------------------------------------------\n\r");
    printf("CH0 Count  CH0 Voltage  CH5 Count  CH5 Voltage  CH6 Count  CH6 Voltage \n\r");           

    while ( true )
    {
         /* Start ADC conversion */
        ADC_ConversionStart();
 
        /* Check if result is ready to be transmitted to console */
        if (result_ready == true)
        {
            adc_ch5_voltage = (float)adc_ch5_count * ADC_VREF/4095U;
            adc_ch6_voltage = (float)adc_ch6_count * ADC_VREF/4095U;
            adc_ch0_voltage = (float)adc_ch0_count * ADC_VREF/4095U;
            printf("0x%03x      %0.2f V       0x%03x      %0.2f V       0x%03x      %0.2f V \t\r",
                    adc_ch0_count, adc_ch0_voltage, adc_ch5_count, adc_ch5_voltage, adc_ch6_count, adc_ch6_voltage);
                           
                
            result_ready = false;
 
            PIT_DelayMs(500);
        }
    }

    /* Execution should not come here during normal operation */

    return ( EXIT_FAILURE );
}



/*******************************************************************************
 End of File
*/

