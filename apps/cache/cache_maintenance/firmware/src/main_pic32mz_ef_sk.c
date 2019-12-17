/*******************************************************************************
  Main Source File

  Company:
    Microchip Technology Inc.

  File Name:
    main_pic32mz_ef_sk.c

  Summary:
    This file contains the "main" function for PIC32MZ EF Starter Kit project.

  Description:
    This file contains the "main" function for a project.  The
    "main" function calls the "SYS_Initialize" function to initialize the state
    machines of all modules in the system
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

#include <stddef.h>                     // Defines NULL
#include <stdbool.h>                    // Defines true
#include <stdlib.h>                     // Defines EXIT_FAILURE
#include <string.h>
#include "definitions.h"                // SYS function prototypes
#include "device.h"
#include "device_cache.h"

#define LED_ON()                LED1_Set()
#define LED_OFF()               LED1_Clear()
#define LED_TOGGLE()            LED1_Toggle()

#define READ_SIZE               10
#define BUFFER_SIZE             (2*CACHE_LINE_SIZE)     // Buffer size in terms of cache lines

char __attribute__ ((aligned (16))) messageStart[] = "**** CACHE maintenance demo with UART ****\r\n\
**** Type a buffer of 10 characters and observe it echo back ****\r\n\
**** LED toggles on each time the buffer is echoed ****\r\n";
char __attribute__ ((aligned (16))) receiveBuffer[BUFFER_SIZE] = {};
char __attribute__ ((aligned (16))) echoBuffer[BUFFER_SIZE] = {};
char __attribute__ ((aligned (16))) messageError[BUFFER_SIZE] = "**** UART error occurred ****\r\n";

bool errorStatus  = false;
bool writeStatus  = false;
bool readStatus   = false;

void APP_WriteCallback(uintptr_t context)
{
    writeStatus = true;
}

void APP_ReadCallback(uintptr_t context)
{
    if(UART2_ErrorGet() != UART_ERROR_NONE)
    {
        /* ErrorGet clears errors, set error flag to notify console */
        errorStatus = true;
    }
    else
    {
        readStatus = true;
    }
}

void APP_FaultCallback(uintptr_t context)
{
    if(UART2_ErrorGet() != UART_ERROR_NONE)
    {
        /* ErrorGet clears errors, set error flag to notify console */
        errorStatus = true;
    }
    else
    {
        readStatus = true;
    }
}

void TX_DMAC_Callback(DMAC_TRANSFER_EVENT status, uintptr_t contextHandle)
{
    writeStatus = true;
}

void RX_DMAC_Callback(DMAC_TRANSFER_EVENT status, uintptr_t contextHandle)
{
    readStatus = true;
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
    LED_ON();

    /* Register callback functions for both write and read contexts */
    DMAC_ChannelCallbackRegister(DMAC_CHANNEL_0, TX_DMAC_Callback, 0);
    DMAC_ChannelCallbackRegister(DMAC_CHANNEL_1, RX_DMAC_Callback, 1);

    DCACHE_CLEAN_BY_ADDR((uint32_t)messageStart, sizeof(messageStart));

    DMAC_ChannelTransfer(DMAC_CHANNEL_0, &messageStart, sizeof(messageStart), (const void *)&U2TXREG, 1, 1);

    while(1)
    {
        if(readStatus == true)
        {
            readStatus = false;

            memcpy(echoBuffer, receiveBuffer, READ_SIZE);
            echoBuffer[READ_SIZE] = '\r';
            echoBuffer[(READ_SIZE + 1)] = '\n';

            DCACHE_CLEAN_BY_ADDR((uint32_t)echoBuffer, sizeof(echoBuffer));

            DMAC_ChannelTransfer(DMAC_CHANNEL_0, echoBuffer, READ_SIZE+2, (const void *)&U2TXREG, 1, 1);
            LED_TOGGLE();
        }
        else if(writeStatus == true)
        {
            writeStatus = false;

            /* Invalidate cache lines having received buffer before using it
             * to load the latest data in the actual memory to the cache */
            DCACHE_INVALIDATE_BY_ADDR((uint32_t)receiveBuffer, sizeof(receiveBuffer));

            DMAC_ChannelTransfer(DMAC_CHANNEL_1, (const void *)&U2RXREG, 1, receiveBuffer, READ_SIZE, 1);
        }
    }

      /* Execution should not come here during normal operation */

    return ( EXIT_FAILURE );
}


/*******************************************************************************
 End of File
*/
