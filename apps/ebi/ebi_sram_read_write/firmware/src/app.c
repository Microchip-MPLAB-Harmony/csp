/*******************************************************************************
  MPLAB Harmony Application 
  
  Company:
    Microchip Technology Inc.
  
  File Name:
    app.c

  Summary:
    Application Template

  Description:
    This file contains the application logic.
 *******************************************************************************/


// DOM-IGNORE-BEGIN
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
// DOM-IGNORE-END


// *****************************************************************************
// *****************************************************************************
// Section: Included Files 
// *****************************************************************************
// *****************************************************************************

#include "app.h"
#include "peripheral/gpio/plib_gpio.h"
// *****************************************************************************
// *****************************************************************************
// Section: Global Variable Definitions
// *****************************************************************************
// *****************************************************************************
#define SRAM_ADDR_CS0  0xE0000000
#define RAM_SIZE       2*1024*1024

uint32_t loop;
uint16_t loop_16;
uint16_t *addr_16;
uint16_t val_16;

/*****************************************************
 * Initialize the application data structure. All
 * application related variables are stored in this
 * data structure.
 *****************************************************/

APP_DATA appData;

// *****************************************************************************
/* Driver objects.

  Summary:
    Contains driver objects.

  Description:
    This structure contains driver objects returned by the driver init routines
    to the application. These objects are passed to the driver tasks routines.
*/


APP_DRV_OBJECTS appDrvObject;

// *****************************************************************************
// *****************************************************************************
// Section: Application Local Routines
// *****************************************************************************
// *****************************************************************************


// *****************************************************************************
// *****************************************************************************
// Section: Application Callback Routines
// *****************************************************************************
// *****************************************************************************



// *****************************************************************************
// *****************************************************************************
// Section: Application Initialization and State Machine
// *****************************************************************************
// *****************************************************************************

/******************************************************************************
  Function:
    void APP_Initialize ( void )

  Remarks:
    See prototype in app.h.
 */

void APP_Initialize ( void )
{
    /* TODO: Initialize your application's state machine and other
     * parameters.
     */

    /* Place the App state machine in its initial state. */
    appData.state = APP_STATE_WRITE;
}

/**********************************************************
 * Application tasks routine. This function implements the
 * application state machine.
 ***********************************************************/
void APP_Tasks ( void )
{
    volatile uint32_t val = 0;
    uint32_t *addr;

    switch ( appData.state )
    {
        case APP_STATE_WRITE:
            /*Sets EBI address back to the begining*/
            addr = (uint32_t *)SRAM_ADDR_CS0;

            /*this loop writes the data to SRAM*/
            for (loop=0; loop < RAM_SIZE/4; loop++)
            {
                /*writing address of memory location into the memory location*/
                *addr = (uint32_t)addr;
                /*incrementing the address to the next address*/
                addr++;
            }
            appData.state = APP_STATE_READBACK;
            break;

        case APP_STATE_READBACK:
            /*Sets EBI address back to the begining*/
            addr = (uint32_t *)SRAM_ADDR_CS0;

            /*Loop reads back written data*/
            for (loop=0 ; loop < RAM_SIZE/4; loop++)
            {
                val = *addr;
                if (val != (uint32_t)addr)
                {
                    /*If this fails the value read doesn't match the written value*/
                    appData.state = APP_STATE_FAIL;
                    break;
                }
                else
                {
                    appData.state = APP_STATE_DONE;
                }
                addr++;
            }
            break;

       case APP_STATE_DONE:
        {
            LED3_Set();
            /* Test PASSED */
            Nop();
        }
        break;

        case APP_STATE_FAIL:
        {
           LED1_Set();
            /* Test FAILED */
            Nop();
        }
        break;

        default:
            break;
    }
} 

/*******************************************************************************
 End of File
 */
