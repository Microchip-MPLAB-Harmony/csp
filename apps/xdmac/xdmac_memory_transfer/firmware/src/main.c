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
Copyright (c) 2017 released Microchip Technology Inc.  All rights reserved.

//Microchip licenses to you the right to use, modify, copy and distribute
Software only when embedded on a Microchip microcontroller or digital signal
controller that is integrated into your product or third party product
(pursuant to the sublicense terms in the accompanying license agreement).

You should refer to the license agreement accompanying this Software for
additional information regarding your rights and obligations.

SOFTWARE AND DOCUMENTATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND,
EITHER EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION, ANY WARRANTY OF
MERCHANTABILITY, TITLE, NON-INFRINGEMENT AND FITNESS FOR A PARTICULAR PURPOSE.
IN NO EVENT SHALL MICROCHIP OR ITS LICENSORS BE LIABLE OR OBLIGATED UNDER
CONTRACT, NEGLIGENCE, STRICT LIABILITY, CONTRIBUTION, BREACH OF WARRANTY, OR
OTHER LEGAL EQUITABLE THEORY ANY DIRECT OR INDIRECT DAMAGES OR EXPENSES
INCLUDING BUT NOT LIMITED TO ANY INCIDENTAL, SPECIAL, INDIRECT, PUNITIVE OR
CONSEQUENTIAL DAMAGES, LOST PROFITS OR LOST DATA, COST OF PROCUREMENT OF
SUBSTITUTE GOODS, TECHNOLOGY, SERVICES, OR ANY CLAIMS BY THIRD PARTIES
(INCLUDING BUT NOT LIMITED TO ANY DEFENSE THEREOF), OR OTHER SIMILAR COSTS.
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
#include <string.h>                     // Defines strncmp
#include "definitions.h"                // SYS function prototypes

#define LED_ON                      LED_Clear
#define LED_OFF                     LED_Set
#define LED_TOGGLE                  LED_Toggle

#define TRANSFER_SIZE               10016

uint8_t __attribute__ ((aligned(32))) srcBuffer[TRANSFER_SIZE] = {};
uint8_t __attribute__ ((aligned(32)))dstBuffer1[TRANSFER_SIZE] = {};
uint8_t __attribute__ ((aligned(32)))dstBuffer2[TRANSFER_SIZE] = {};

volatile bool completeStatus = false;
volatile bool errorStatus = false;
volatile uint8_t transfersDone = 0;
volatile uint32_t timeStamp=0;

uint32_t transferCyclesBurstSize1=0;

uint32_t transferCyclesBurstSize16=0;

void APP_Callback(XDMAC_TRANSFER_EVENT status, uintptr_t context)
{
    transfersDone++;

    timeStamp=timeStamp-SYSTICK_TimerCounterGet();

    if(status == XDMAC_TRANSFER_COMPLETE)
    {
        completeStatus = true;
    }
    else
    {
        errorStatus = true;
    }
}

// *****************************************************************************
// *****************************************************************************
// Section: Main Entry Point
// *****************************************************************************
// *****************************************************************************

int main ( void )
{
    uint32_t i = 0;
    uint32_t channelSettings = 0;

    /* Initialize all modules */
    SYS_Initialize ( NULL );

    LED_OFF();

    /* Build the srcBuffer */
    while(i < TRANSFER_SIZE)
    {
        srcBuffer[i] = i&0xFF;
        i++;
    }

    printf("\n\r-------------------------------------------------------------");
    printf("\n\r\t\t XDMAC Memory Transfer DEMO\t\t");
    printf("\n\r-------------------------------------------------------------");

    /* Clean cache lines having source buffer before submitting a transfer
     * request to DMA to load the latest data in the cache to the actual
     * memory */
    SCB_CleanDCache_by_Addr((uint32_t *)srcBuffer, TRANSFER_SIZE);

    /* Register a callback with XDMAC PLIB to get transfer complete and error
     * events. */
    XDMAC_ChannelCallbackRegister(XDMAC_CHANNEL_0, APP_Callback, 0);

    /* Performing first transfer from srcBuffer to dstBuffer1 with configured
     * burst size of 1 data */
    SYSTICK_TimerStart();

    timeStamp=SYSTICK_TimerCounterGet();

    XDMAC_ChannelTransfer(XDMAC_CHANNEL_0, &srcBuffer, &dstBuffer1, TRANSFER_SIZE);

    while ( true )
    {
        if(completeStatus == true)
        {
            completeStatus = false;

            if(transfersDone == 1)
            {
                transferCyclesBurstSize1=timeStamp;

                /* Perform the second transfer from srcBuffer to dstBuffer2 by
                 * re-configuring burst size to 16 data to increase the
                 * performance */
                channelSettings = XDMAC_ChannelSettingsGet(XDMAC_CHANNEL_0);
                channelSettings = (channelSettings & ~XDMAC_CC_MBSIZE_Msk) | XDMAC_CC_MBSIZE_SIXTEEN;
                XDMAC_ChannelSettingsSet(XDMAC_CHANNEL_0, channelSettings);

                timeStamp=SYSTICK_TimerCounterGet();

                XDMAC_ChannelTransfer(XDMAC_CHANNEL_0, &srcBuffer, &dstBuffer2, TRANSFER_SIZE);
            }
            else if(transfersDone == 2)
            {
                /* Invalidate cache lines having received buffer before using it
                 * to load the latest data in the actual memory to the cache */
                SCB_InvalidateDCache_by_Addr((uint32_t *)dstBuffer1, TRANSFER_SIZE);
                SCB_InvalidateDCache_by_Addr((uint32_t *)dstBuffer2, TRANSFER_SIZE);

                transferCyclesBurstSize16=timeStamp;

                /* Verify both the transfers */
                if( (memcmp(srcBuffer, dstBuffer1, TRANSFER_SIZE) == 0) && (memcmp(srcBuffer, dstBuffer2, TRANSFER_SIZE) == 0))
                {
                    /* Successfully transferred the data using XDMAC */
                    printf("\n\r XDMAC Memory Transfer Successful with Data Match\n\r");
                    LED_ON();
                }
                else
                {
                    /* Data transfers done, but data mismatch occurred */
                    printf("\n\r XDMAC Memory Transfer Successful with Data Mismatch !!!\n\r");
                }

                printf("\n\r Number of Transfer Cycles with Burst Size 1  --> %lu", transferCyclesBurstSize1);
                printf("\n\r Number of Transfer Cycles with Burst Size 16 --> %lu", transferCyclesBurstSize16);
            }
        }
        else if(errorStatus == true)
        {
            /* Error occurred during the transfers */
            errorStatus = false;
            printf("\n\r XDMAC Memory Transfer Error !!!");
        }
        else
        {
            /* Nothing to do, loop */
            ;
        }
    }

    /* Execution should not come here during normal operation */

    return ( EXIT_FAILURE );
}


/*******************************************************************************
 End of File
*/

