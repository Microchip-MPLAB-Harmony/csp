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
 AFEC CH0 - PB01 - Connect to DACC output PB13
 AFEC CH5 - PC30 - connect to Vcc
 AFEC_CH6 - PC31 - Connect to GND
 *****************************************************/

#define AFEC_VREF               (3.3f)
#define DAC_COUNT_INCREMENT     (124U)  // Equivalent to 0.1V 
#define DAC_COUNT_MAX           (4095U)


volatile uint16_t adc_ch0_count, adc_ch5_count, adc_ch6_count;

float adc_ch0_voltage, adc_ch5_voltage, adc_ch6_voltage;

volatile bool result_ready;
/* Initial DAC count which is midpoint = 1.65V*/
uint16_t dac_count=0x800; 


void switch_handler( PIO_PIN pin, uintptr_t context )
{
    /* Write next data sample */
    dac_count = dac_count + DAC_COUNT_INCREMENT;
    
    if (dac_count > DAC_COUNT_MAX)
            dac_count=0;    
    
    DACC_DataWrite(DACC_CHANNEL_0, dac_count);
}

/* This function is called after conversion of last channel in the user sequence */
void AFEC_EventHandler(uintptr_t context)
{
    /* Read the result of 3 channels*/
    adc_ch5_count = AFEC1_ChannelResultGet(CH5_VDD);
    adc_ch6_count = AFEC1_ChannelResultGet(CH6_GND);
    adc_ch0_count = AFEC1_ChannelResultGet(CH0_SINE_WAVE);
       
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
    
    PIO_PinInterruptCallbackRegister(SWITCH_PIN, &switch_handler, (uintptr_t) NULL );
    PIO_PinInterruptEnable(SWITCH_PIN);

    /* Register callback function for AFEC end of conversion interrupt*/
    AFEC1_CallbackRegister(AFEC_EventHandler, (uintptr_t)NULL);
    
    /* Write first data sample in DAC channel 0 and channel 1*/
    DACC_DataWrite(DACC_CHANNEL_0, dac_count);
    
    /* Start the timer to trigger ADC conversion every 50 ms*/
    TC1_CH0_CompareStart();

    printf("\n\r---------------------------------------------------------");
    printf("\n\r                    AFEC User Sequence Demo                 ");
    printf("\n\r---------------------------------------------------------\n\r");
    printf("CH0 Count  CH0 Voltage  CH5 Count  CH5 Voltage  CH6 Count  CH6 Voltage \n\r");           

    while ( true )
    {
        /* Check if result is ready to be transmitted to console */
        if (result_ready == true)
        {
            adc_ch5_voltage = (float)adc_ch5_count * AFEC_VREF/4095U;
            adc_ch6_voltage = (float)adc_ch6_count * AFEC_VREF/4095U;
            adc_ch0_voltage = (float)adc_ch0_count * AFEC_VREF/4095U;
            printf("0x%03x      %0.2f V       0x%03x      %0.2f V       0x%03x      %0.2f V \t\r", \
                    adc_ch0_count, adc_ch0_voltage, adc_ch5_count, adc_ch5_voltage, adc_ch6_count, adc_ch6_voltage);
                           
                
            result_ready = false;
        }
    }

    /* Execution should not come here during normal operation */

    return ( EXIT_FAILURE );
}



/*******************************************************************************
 End of File
*/

