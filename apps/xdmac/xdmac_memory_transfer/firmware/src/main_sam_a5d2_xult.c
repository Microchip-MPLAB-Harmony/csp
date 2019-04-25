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
#include <string.h>                     // Defines strncmp
#include "definitions.h"                // SYS function prototypes

#define LED_ON                      LED_Clear
#define LED_OFF                     LED_Set
#define LED_TOGGLE                  LED_Toggle

#define TRANSFER_SIZE               10016

uint8_t __attribute__ ((aligned(32))) srcBuffer[TRANSFER_SIZE];
uint8_t __attribute__ ((aligned(32)))dstBuffer1[TRANSFER_SIZE];
uint8_t __attribute__ ((aligned(32)))dstBuffer2[TRANSFER_SIZE];

volatile bool completeStatus = false;
volatile bool errorStatus = false;
volatile uint8_t transfersDone = 0;
volatile uint32_t timeStamp=0;

uint32_t transferCyclesBurstSize1=0;

uint32_t transferCyclesBurstSize16=0;

void APP_Callback(XDMAC_TRANSFER_EVENT status, uintptr_t context)
{
    transfersDone++;

    timeStamp=PIT_TimerCounterGet()-timeStamp;

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
    L1C_CleanDCacheAll();
    L1C_DisableCaches();

    /* Register a callback with XDMAC PLIB to get transfer complete and error
     * events. */
    XDMAC0_ChannelCallbackRegister(XDMAC_CHANNEL_0, APP_Callback, 0);

    /* Performing first transfer from srcBuffer to dstBuffer1 with configured
     * burst size of 1 data */
    PIT_TimerStart();

    timeStamp=PIT_TimerCounterGet();

    XDMAC0_ChannelTransfer(XDMAC_CHANNEL_0, &srcBuffer, &dstBuffer1, TRANSFER_SIZE);

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
                channelSettings = XDMAC0_ChannelSettingsGet(XDMAC_CHANNEL_0);
                channelSettings = (channelSettings & ~XDMAC_CC_MBSIZE_Msk) | XDMAC_CC_MBSIZE_SIXTEEN;
                XDMAC0_ChannelSettingsSet(XDMAC_CHANNEL_0, channelSettings);

                timeStamp=PIT_TimerCounterGet();

                XDMAC0_ChannelTransfer(XDMAC_CHANNEL_0, &srcBuffer, &dstBuffer2, TRANSFER_SIZE);
            }
            else if(transfersDone == 2)
            {
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

