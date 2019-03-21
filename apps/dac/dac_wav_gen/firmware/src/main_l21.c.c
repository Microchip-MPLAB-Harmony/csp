/*******************************************************************************
  Main Source File

  Company:
    Microchip Technology Inc.

  File Name:
    main_l21.c

  Summary:
    This file contains the "main" function for a project.

  Description:
    This file contains the "main" function for a project.  The
    "main" function calls the "SYS_Initialize" function to initialize the state
    machines of all modules in the system
 *******************************************************************************/

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
// Section: Global Data Definitions
// *****************************************************************************
// *****************************************************************************
#define NUM_OF_SAMPLES (100)

typedef enum 
{    
    SINE_WAVE,
    TRIANGLE_WAVE
} WAVE_TYPE; 

volatile WAVE_TYPE wave = SINE_WAVE;
volatile uint8_t sample_number = 0;

const uint16_t sine_wave[NUM_OF_SAMPLES] = {
0x200,	0x210,	0x220,	0x230,	0x240,	0x24F,	0x25E,	0x26D,	0x27B,	0x289,
0x297,	0x2A3,	0x2AF,	0x2BB,	0x2C5,	0x2CF,	0x2D8,	0x2E0,	0x2E8,	0x2EE,
0x2F4,	0x2F8,	0x2FC,	0x2FE,	0x300,	0x300,	0x300,	0x2FE,	0x2FC,	0x2F8,
0x2F4,	0x2EE,	0x2E8,	0x2E0,	0x2D8,	0x2CF,	0x2C5,	0x2BB,	0x2AF,	0x2A3,
0x297,	0x289,	0x27B,	0x26D,	0x25E,	0x24F,	0x240,	0x230,	0x220,	0x210,
0x200,	0x1F0,	0x1E0,	0x1D0,	0x1C0,	0x1B1,	0x1A2,	0x193,	0x185,	0x177,
0x16A,	0x15D,	0x151,	0x146,	0x13B,	0x131,	0x128,	0x120,	0x118,	0x112,
0x10D,	0x108,	0x105,	0x102,	0x101,	0x100,	0x101,	0x102,	0x105,	0x108,
0x10D,	0x112,	0x118,	0x120,	0x128,	0x131,	0x13B,	0x146,	0x151,	0x15D,
0x16A,	0x177,	0x185,	0x193,	0x1A2,	0x1B1,	0x1C0,	0x1D0,	0x1E0,	0x1F0,
};

const uint16_t triangle_wave[NUM_OF_SAMPLES] = {
0x100,	0x105,	0x10A,	0x10F,	0x115,	0x11A,	0x11F,	0x124,	0x129,	0x12E,
0x133,	0x138,	0x13E,	0x143,	0x148,	0x14D,	0x152,	0x157,	0x15C,	0x161,
0x167,	0x16C,	0x171,	0x176,	0x17B,	0x180,	0x185,	0x18A,	0x18F,	0x195,
0x19A,	0x19F,	0x1A4,	0x1A9,	0x1AE,	0x1B3,	0x1B8,	0x1BE,	0x1C3,	0x1C8,
0x1CD,	0x1D2,	0x1D7,	0x1DC,	0x1E1,	0x1E7,	0x1EC,	0x1F1,	0x1F6,	0x1FB,
0x200,	0x205,	0x20A,	0x20F,	0x215,	0x21A,	0x21F,	0x224,	0x229,	0x22E,
0x233,	0x238,	0x23E,	0x243,	0x248,	0x24D,	0x252,	0x257,	0x25C,	0x261,
0x267,	0x26C,	0x271,	0x276,	0x27B,	0x280,	0x285,	0x28A,	0x28F,	0x295,
0x29A,	0x29F,	0x2A4,	0x2A9,	0x2AE,	0x2B3,	0x2B8,	0x2BE,	0x2C3,	0x2C8,
0x2CD,	0x2D2,	0x2D7,	0x2DC,	0x2E1,	0x2E7,	0x2EC,	0x2F1,	0x2F6,	0x2FB,
};

// *****************************************************************************
// *****************************************************************************
// Section: Application Callback Functions
// *****************************************************************************
// *****************************************************************************

void TC0_CallBack_Function (TC_TIMER_STATUS status, uintptr_t context)
{ 
    if ((DAC_IsReady(DAC_CHANNEL_1) == true))
    {	
		if (wave == SINE_WAVE)
		{
            DAC_DataWrite (DAC_CHANNEL_1, sine_wave[sample_number]);
		}
		else
		{
            DAC_DataWrite (DAC_CHANNEL_1, triangle_wave[sample_number]);
		}	

        sample_number++;

        if (sample_number >= 100)
        {
           sample_number = 0;
        }
    }
}

void Button_CallBack_Function (uintptr_t context)
{ 
    (wave == SINE_WAVE)?(wave = TRIANGLE_WAVE):(wave = SINE_WAVE);
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
    EIC_CallbackRegister(EIC_PIN_2,Button_CallBack_Function, 0);
    TC0_TimerCallbackRegister(TC0_CallBack_Function, (uintptr_t)NULL);
    TC0_TimerStart();
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

