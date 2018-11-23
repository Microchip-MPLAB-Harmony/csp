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

#define VDDSCALAR_REF_LOW_LIMIT  16
#define VDDSCALAR_REF_HIGH_LIMIT 40

#define NUM_OF_SAMPLES (100)
volatile uint8_t sampleNumber = 0;

const uint16_t sineWave[NUM_OF_SAMPLES] = {
0x200,   0x210,   0x220,   0x230,   0x240,   0x24F,   0x25E,   0x26D,  0x27B,   0x289,
0x297,   0x2A3,  0x2AF,  0x2BB,  0x2C5,   0x2CF,   0x2D8,  0x2E0,   0x2E8,   0x2EE,
0x2F4,   0x2F8,   0x2FC,   0x2FE,   0x300,   0x300,   0x300,   0x2FE,   0x2FC,   0x2F8,
0x2F4,   0x2EE,   0x2E8,   0x2E0,   0x2D8,  0x2CF,   0x2C5,   0x2BB,  0x2AF,  0x2A3,
0x297,   0x289,   0x27B,   0x26D,  0x25E,   0x24F,   0x240,   0x230,   0x220,   0x210,
0x200,   0x1F0,   0x1E0,   0x1D0,  0x1C0,   0x1B1,   0x1A2,  0x193,   0x185,   0x177,
0x16A,  0x15D,  0x151,   0x146,   0x13B,   0x131,   0x128,   0x120,   0x118,   0x112,
0x10D,  0x108,   0x105,   0x102,   0x101,   0x100,   0x101,   0x102,   0x105,   0x108,
0x10D,  0x112,   0x118,   0x120,   0x128,   0x131,   0x13B,   0x146,   0x151,   0x15D,
0x16A,  0x177,   0x185,   0x193,   0x1A2,  0x1B1,   0x1C0,   0x1D0,  0x1E0,   0x1F0,
};


void TC3_CallBack_Function (TC_TIMER_STATUS status, uintptr_t context)
{
        DAC_DataWrite (sineWave[sampleNumber]);
        sampleNumber++;
        
        if (sampleNumber >= NUM_OF_SAMPLES)
        {
            sampleNumber = 0;
        }
}

uint8_t vdd_scalar   = VDDSCALAR_REF_LOW_LIMIT;

void switch_handler(uintptr_t context )
{
    if((vdd_scalar >= VDDSCALAR_REF_LOW_LIMIT) && (vdd_scalar <= VDDSCALAR_REF_HIGH_LIMIT)){
        
        vdd_scalar++;
        
    }else{
        
        vdd_scalar  = VDDSCALAR_REF_LOW_LIMIT;
        
    }
    
    AC_SetVddScalar(AC_CHANNEL0 , vdd_scalar);
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
    
    printf("\n\n\r-----------------------------------------------");
    printf("\n\n\r          AC PWM GENERATION                    ");
    printf("\n\n\r-----------------------------------------------");
    
    printf("\n\n\rConnect pin PA04(comparator0 Input) to pin PA02(DAC output) and observe compare output on pin PA12");
    
    EIC_CallbackRegister(EIC_PIN_15, switch_handler, (uintptr_t) NULL);
    TC3_TimerCallbackRegister(TC3_CallBack_Function, (uintptr_t)NULL);
    TC3_TimerStart();
    
    while ( true )
    {
        SYS_Tasks();
    }

    /* Execution should not come here during normal operation */

    return ( EXIT_FAILURE );
}

/*******************************************************************************
 End of File
*/

