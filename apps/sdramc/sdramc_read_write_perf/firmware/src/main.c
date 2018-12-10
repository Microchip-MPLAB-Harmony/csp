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
#include <string.h>

#include <sdram_data.h>                 // sdram_480x272_data[261120]

#define IMAGE_SIZE_BYTES    (sizeof(sdram_480x272_data))
#define BUFFER_SIZE         256
#define SYSTICK_MAX         0x00ffffff

uint32_t readBuf[261120/4];
uint32_t i = 0;
volatile bool result = true;

uint32_t writeCycles = 0, readCycles = 0, startCount = 0;
volatile bool completeStatus = false;

void APP_Callback(XDMAC_TRANSFER_EVENT status, uintptr_t context)
{
    completeStatus = true;
}

// *****************************************************************************
// *****************************************************************************
// Section: Main Entry Point
// *****************************************************************************
// *****************************************************************************

int main ( void )
{
    uint32_t    *addr;
    uint8_t     * charPtr;

    /* Step: 1. Initialize all modules */
    SYS_Initialize ( NULL );
    XDMAC_ChannelCallbackRegister(XDMAC_CHANNEL_0, APP_Callback, 0);

    addr = (uint32_t *)SDRAM_CS_ADDR;

    printf("\n\r-------------------------------------------------------");
    printf("\n\r         SDRAM Performance Benchmark Example           ");
    printf("\n\r-------------------------------------------------------");

    while(1)
    {
        /* Step: 2. Copy image data from program flash to buffer in SRAM */
        memcpy(readBuf, (void*)sdram_480x272_data, IMAGE_SIZE_BYTES);

        /* Step: 3. Verify that copy passed */
        if (memcmp(readBuf, sdram_480x272_data, IMAGE_SIZE_BYTES) != 0)
        {
            result = false;
        }

        /* Step: 4. Use DMA to write to SDRAM */
        SYSTICK_TimerPeriodSet(SYSTICK_MAX);
        SYSTICK_TimerStart();
        startCount = SYSTICK_TimerCounterGet();

        XDMAC_ChannelTransfer(XDMAC_CHANNEL_0, &readBuf, addr, IMAGE_SIZE_BYTES/4);
        
        while(completeStatus == false);

        completeStatus = false;

        writeCycles = startCount - SYSTICK_TimerCounterGet();
        SYSTICK_TimerStop();


        /* Step: 5. Use DMA to read from SDRAM */
        SYSTICK_TimerPeriodSet(SYSTICK_MAX);
        SYSTICK_TimerStart();
        startCount = SYSTICK_TimerCounterGet();

        XDMAC_ChannelTransfer(XDMAC_CHANNEL_0, addr, &readBuf,  IMAGE_SIZE_BYTES/4);

        while(completeStatus == false);

        completeStatus = false;

        readCycles = startCount - SYSTICK_TimerCounterGet();
        SYSTICK_TimerStop();

        /* Step: 6. Manually compare each byte in SRAM with image data in program flash */
        charPtr = (uint8_t *) readBuf;
        for(i = 0; i < IMAGE_SIZE_BYTES; i++)
        {
            if (charPtr[i] != sdram_480x272_data[i])
            {
                // Manual check failed
                result = false;
                break;
            }
        }

        /* Step: 7. Use memcmp to compare data between buffer in SRAM and image data in program flash */
        if (memcmp(readBuf, sdram_480x272_data, IMAGE_SIZE_BYTES) != 0)
        {
            // Memcmp also fails!
            result = false;
        }

        if(result)
        {
            printf("\n\r Test Passed....!\n");
        }
        else
        {
            printf("\n\r Test Failed....!\n");
        }
        printf("\n");
        printf("\n\r SDRAM Performance Benchmark results based on the below DMA configurations");
        printf("\n\r Data Width = 32-bits");
        printf("\n\r Chunk Size = 1-transfers per request");
        printf("\n\r Burst Size = 16-transfers per burst\n");
        printf("\n\r Write Time in CPU cycles = %d", (int)writeCycles);
        printf("\n\r Read Time in CPU cycles  = %d", (int)readCycles);

        while(1);
    }
}

