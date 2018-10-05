/*******************************************************************************
  Main Source File

  Company:
    Microchip Technology Inc.

  File Name:
    main.c

  Summary:
    This file contains the "main" function for a project.

  Description:
    This file contains the "main" function for a project. The "main" function
    calls the "SYS_Initialize" function to initialize the state machines of all 
    modules in the system.

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
volatile uint8_t sampleNumber = 0;

uint16_t sineWave[NUM_OF_SAMPLES] = {
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

// *****************************************************************************
// *****************************************************************************
// Section: Application Callback Functions
// *****************************************************************************
// *****************************************************************************

void TC0_CallBack_Function (TC_TIMER_STATUS status, uintptr_t context)
{
    if (DACC_IsReady (0) == true)
    {
        DACC_DataWrite (DACC_CHANNEL_0, sineWave[sampleNumber]);
        sampleNumber++;
        
        if (sampleNumber >= NUM_OF_SAMPLES)
        {
            sampleNumber = 0;
        }
    }
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

    TC0_CH0_TimerCallbackRegister(TC0_CallBack_Function, (uintptr_t)NULL);
    TC0_CH0_TimerStart();
    
    while ( true )
    {
        /* Maintain state machines of all polled MPLAB Harmony modules */
        if (ACC_StatusGet(ACC_STATUS_SOURCE_COMPARATOR_OUTPUT))
        {
            Compare_Pin_Set ();            
        }
        else
        {
            Compare_Pin_Clear ();                        
        }
    }

    /* Execution should not come here during normal operation */

    return ( EXIT_FAILURE );
}


/*******************************************************************************
 End of File
*/

