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

uint16_t sine_wave[NUM_OF_SAMPLES] = {
        0x800, 0x840, 0x880, 0x8C0, 0x8FF, 0x93C, 0x979, 0x9B4, 0x9ED, 0xA25,
        0xA5A, 0xA8D, 0xABD, 0xAEA, 0xB15, 0xB3C, 0xB61, 0xB81, 0xB9F, 0xBB8,
        0xBCE, 0xBE0, 0xBEE, 0xBF8, 0xBFE, 0xC00, 0xBFE, 0xBF8, 0xBEE, 0xBE0,
        0xBCE, 0xBB8, 0xB9F, 0xB81, 0xB61, 0xB3C, 0xB15, 0xAEA, 0xABD, 0xA8D,
        0xA5A, 0xA25, 0x9ED, 0x9B4, 0x979, 0x93C, 0x8FF, 0x8C0, 0x880, 0x840,
        0x800, 0x7C0, 0x780, 0x740, 0x701, 0x6C4, 0x687, 0x64C, 0x613, 0x5DB,
        0x5A6, 0x573, 0x543, 0x516, 0x4EB, 0x4C4, 0x49F, 0x47F, 0x461, 0x448,
        0x432, 0x420, 0x412, 0x408, 0x402, 0x400, 0x402, 0x408, 0x412, 0x420,
        0x432, 0x448, 0x461, 0x47F, 0x49F, 0x4C4, 0x4EB, 0x516, 0x543, 0x573,
        0x5A6, 0x5DB, 0x613, 0x64C, 0x687, 0x6C4, 0x701, 0x740, 0x780, 0x7C0
};

uint16_t triangle_wave[NUM_OF_SAMPLES] = {
        0x400, 0x414, 0x429, 0x43D, 0x452, 0x466, 0x47B, 0x48F, 0x4A4, 0x4B8,
        0x4CD, 0x4E1, 0x4F6, 0x50A, 0x51F, 0x533, 0x548, 0x55C, 0x571, 0x585,
        0x59A, 0x5AE, 0x5C3, 0x5D7, 0x5EC, 0x600, 0x614, 0x629, 0x63D, 0x652,
        0x666, 0x67B, 0x68F, 0x6A4, 0x6B8, 0x6CD, 0x6E1, 0x6F6, 0x70A, 0x71F,
        0x733, 0x748, 0x75C, 0x771, 0x785, 0x79A, 0x7AE, 0x7C3, 0x7D7, 0x7EC,
        0x800, 0x814, 0x829, 0x83D, 0x852, 0x866, 0x87B, 0x88F, 0x8A4, 0x8B8,
        0x8CD, 0x8E1, 0x8F6, 0x90A, 0x91F, 0x933, 0x948, 0x95C, 0x971, 0x985,
        0x99A, 0x9AE, 0x9C3, 0x9D7, 0x9EC, 0xA00, 0xA14, 0xA29, 0xA3D, 0xA52,
        0xA66, 0xA7B, 0xA8F, 0xAA4, 0xAB8, 0xACD, 0xAE1, 0xAF6, 0xB0A, 0xB1F,
        0xB33, 0xB48, 0xB5C, 0xB71, 0xB85, 0xB9A, 0xBAE, 0xBC3, 0xBD7, 0xBEC
};

// *****************************************************************************
// *****************************************************************************
// Section: Application Callback Functions
// *****************************************************************************
// *****************************************************************************

void TC0_CallBack_Function (TC_TIMER_STATUS status, uintptr_t context)
{ 
    if ((DAC_IsReady(DAC_CHANNEL_0) == true))
    {	
		if (wave == SINE_WAVE)
		{
            DAC_DataWrite (DAC_CHANNEL_0, sine_wave[sample_number]);
		}
		else
		{
            DAC_DataWrite (DAC_CHANNEL_0, triangle_wave[sample_number]);
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
    EIC_CallbackRegister(EIC_PIN_15,Button_CallBack_Function, 0);
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

