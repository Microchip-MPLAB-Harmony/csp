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
Copyright (c) 2018 released Microchip Technology Inc.  All rights reserved.

Microchip licenses to you the right to use, modify, copy and distribute
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
#include "definitions.h"                // SYS function prototypes
#include "string.h"

#define DMA_CHANNEL_RECEIVE         XDMAC_CHANNEL_0
#define DMA_CHANNEL_TRANSMIT        XDMAC_CHANNEL_1

#define SPI0_RECEIVE_ADDRESS    (&SPI0_REGS->SPI_RDR)
#define SPI0_TRANSMIT_ADDRESS   (&SPI0_REGS->SPI_TDR)

typedef enum
{
    APP_STATE_INITIALIZE,
	APP_STATE_SPI_IDLE,
    VERIFY_AND_UPDATE_PING_BUFFER,
    VERIFY_AND_UPDATE_PONG_BUFFER,
    APP_STATE_SPI_XFER_SUCCESSFUL,
    APP_STATE_SPI_XFER_ERROR

} APP_STATES;

typedef enum
{
    BUFFER_TYPE_PING,
    BUFFER_TYPE_PONG
}BUFFER_TYPE;

uint8_t txPingBuffer[] = "INITIAL_DMA_DATA_FROM_PING_BUFFER";
uint8_t rxPingBuffer[sizeof(txPingBuffer)];

uint8_t txPongBuffer[] = "initial_dma_data_from_pong_buffer";
uint8_t rxPongBuffer[sizeof(txPongBuffer)];

volatile APP_STATES state = APP_STATE_INITIALIZE;

XDMAC_DESCRIPTOR_VIEW_1 pTxLinkedListDesc[2], pRxLinkedListDesc[2];

__attribute__((__aligned__(4))) static XDMAC_DESCRIPTOR_CONTROL txFirstDescriptorControl =
{
    .fetchEnable = 1,
    .sourceUpdate = 1,
    .destinationUpdate = 1,
    .view = 1
};

__attribute__((__aligned__(4))) static XDMAC_DESCRIPTOR_CONTROL rxFirstDescriptorControl =
{
    .fetchEnable = 1,
    .sourceUpdate = 1,
    .destinationUpdate = 1,
    .view = 1
};

void APP_InitializeTxLinkedListDescriptor(void)
{
    pTxLinkedListDesc[0].mbr_nda = (uint32_t)&pTxLinkedListDesc[1];
    pTxLinkedListDesc[0].mbr_sa = (uint32_t)&txPingBuffer;
    pTxLinkedListDesc[0].mbr_da = (uint32_t)SPI0_TRANSMIT_ADDRESS;
    pTxLinkedListDesc[0].mbr_ubc.blockDataLength = sizeof(txPingBuffer);
    pTxLinkedListDesc[0].mbr_ubc.nextDescriptorControl.fetchEnable = 1;
    pTxLinkedListDesc[0].mbr_ubc.nextDescriptorControl.sourceUpdate = 1;
    pTxLinkedListDesc[0].mbr_ubc.nextDescriptorControl.destinationUpdate = 0;
    pTxLinkedListDesc[0].mbr_ubc.nextDescriptorControl.view = 1;


    pTxLinkedListDesc[1].mbr_nda = (uint32_t)&pTxLinkedListDesc[0];
    pTxLinkedListDesc[1].mbr_sa = (uint32_t)&txPongBuffer;
    pTxLinkedListDesc[1].mbr_da = (uint32_t)SPI0_TRANSMIT_ADDRESS;
    pTxLinkedListDesc[1].mbr_ubc.blockDataLength = sizeof(txPongBuffer);
    pTxLinkedListDesc[1].mbr_ubc.nextDescriptorControl.fetchEnable = 1;
    pTxLinkedListDesc[1].mbr_ubc.nextDescriptorControl.sourceUpdate = 1;
    pTxLinkedListDesc[1].mbr_ubc.nextDescriptorControl.destinationUpdate = 0;
    pTxLinkedListDesc[1].mbr_ubc.nextDescriptorControl.view = 1;
}

void APP_InitializeRxLinkedListDescriptor(void)
{
    pRxLinkedListDesc[0].mbr_nda = (uint32_t)&pRxLinkedListDesc[1];
    pRxLinkedListDesc[0].mbr_sa = (uint32_t)SPI0_RECEIVE_ADDRESS;
    pRxLinkedListDesc[0].mbr_da = (uint32_t)&rxPingBuffer;
    pRxLinkedListDesc[0].mbr_ubc.blockDataLength = sizeof(rxPingBuffer);
    pRxLinkedListDesc[0].mbr_ubc.nextDescriptorControl.fetchEnable= 1;
    pRxLinkedListDesc[0].mbr_ubc.nextDescriptorControl.sourceUpdate = 1;
    pRxLinkedListDesc[0].mbr_ubc.nextDescriptorControl.destinationUpdate = 0;
    pRxLinkedListDesc[0].mbr_ubc.nextDescriptorControl.view= 1;


    pRxLinkedListDesc[1].mbr_nda = (uint32_t)&pRxLinkedListDesc[0];
    pRxLinkedListDesc[1].mbr_sa = (uint32_t)SPI0_RECEIVE_ADDRESS;
    pRxLinkedListDesc[1].mbr_da = (uint32_t)&rxPongBuffer;
    pRxLinkedListDesc[1].mbr_ubc.blockDataLength = sizeof(rxPongBuffer);
    pRxLinkedListDesc[1].mbr_ubc.nextDescriptorControl.fetchEnable = 0;
    pRxLinkedListDesc[1].mbr_ubc.nextDescriptorControl.sourceUpdate = 1;
    pRxLinkedListDesc[1].mbr_ubc.nextDescriptorControl.destinationUpdate= 0;
    pRxLinkedListDesc[1].mbr_ubc.nextDescriptorControl.view = 1;
}

static void APP_DMA_TxCallbackHandler(XDMAC_TRANSFER_EVENT event, uintptr_t context)
{
    if(event == XDMAC_TRANSFER_ERROR)
    {
        state = APP_STATE_SPI_XFER_ERROR;
    }
}

static void APP_DMA_RxCallbackHandler(XDMAC_TRANSFER_EVENT event, uintptr_t context)
{
    static BUFFER_TYPE bufferType = BUFFER_TYPE_PING;

    if(event == XDMAC_TRANSFER_COMPLETE)
    {
        if(bufferType == BUFFER_TYPE_PING)
        {
            state = VERIFY_AND_UPDATE_PING_BUFFER;
            bufferType = BUFFER_TYPE_PONG;
        }
        else
        {
            state = VERIFY_AND_UPDATE_PONG_BUFFER;
            bufferType = BUFFER_TYPE_PING;
        }
    }
    else
    {
        /* It means XDMAC_TRANSFER_ERROR event */
        state = APP_STATE_SPI_XFER_ERROR;
    }
}
// *****************************************************************************
// *****************************************************************************
// Section: Main Entry Point
// *****************************************************************************
// *****************************************************************************

int main ( void )
{
    static uint8_t pingData=0, pongData=0x44;
    uint8_t i=0;

    /* Initialize all modules */
    SYS_Initialize ( NULL );

    while ( true )
    {
        switch (state)
        {
            case APP_STATE_INITIALIZE:
            {
                /* Initialize linked list descriptors for transmission and reception both */
                APP_InitializeTxLinkedListDescriptor();
                APP_InitializeRxLinkedListDescriptor();

                /* Setup the callbacks */
                XDMAC_ChannelCallbackRegister(DMA_CHANNEL_TRANSMIT, APP_DMA_TxCallbackHandler, (uintptr_t)NULL);
                XDMAC_ChannelCallbackRegister(DMA_CHANNEL_RECEIVE, APP_DMA_RxCallbackHandler, (uintptr_t)NULL);

                /* Start the DMA in linked list mode */
                XDMAC_ChannelLinkedListTransfer(DMA_CHANNEL_RECEIVE, (uint32_t)&pRxLinkedListDesc[0], &rxFirstDescriptorControl);
                XDMAC_ChannelLinkedListTransfer(DMA_CHANNEL_TRANSMIT, (uint32_t)&pTxLinkedListDesc[0], &txFirstDescriptorControl);

                state = APP_STATE_SPI_IDLE;
                break;
            }
            case APP_STATE_SPI_IDLE:
            {
                /* Application can do other task here */
                break;
            }
            case VERIFY_AND_UPDATE_PING_BUFFER:
            {
                if (memcmp(&txPingBuffer[0], &rxPingBuffer[0], sizeof(txPingBuffer) != 0))
                {
                    /* It means received data is not same as transmitted data */
                    state = APP_STATE_SPI_XFER_ERROR;
                }
                else
                {
                    /* It means received data is same as transmitted data.
                     * Change the data for next transfer */
                    for(i=0; i<sizeof(txPingBuffer); i++)
                    {
                        txPingBuffer[i] = pingData++;
                    }
                    state = APP_STATE_SPI_XFER_SUCCESSFUL;
                }
                break;
            }
            case VERIFY_AND_UPDATE_PONG_BUFFER:
            {
                if (memcmp(&txPongBuffer[0], &rxPongBuffer[0], sizeof(txPongBuffer) != 0))
                {
                    /* It means received data is not same as transmitted data */
                    state = APP_STATE_SPI_XFER_ERROR;
                }
                else
                {
                    /* It means received data is same as transmitted data.
                     * Change the data for next transfer */
                    for(i=0; i<sizeof(txPongBuffer); i++)
                    {
                        txPongBuffer[i] = pongData++;
                    }
                    state = APP_STATE_SPI_XFER_SUCCESSFUL;
                }
                break;
            }
            case APP_STATE_SPI_XFER_SUCCESSFUL:
            {
                LED1_Clear();
                break;
            }
            case APP_STATE_SPI_XFER_ERROR:
            {
                /* Abort DMA */
                XDMAC_ChannelDisable(DMA_CHANNEL_TRANSMIT);
                XDMAC_ChannelDisable(DMA_CHANNEL_RECEIVE);

                /* Turn Off the LED */
                LED1_Set();
                break;
            }
            default:
                break;
        }
    }

    /* Execution should not come here during normal operation */

    return ( EXIT_FAILURE );
}


/*******************************************************************************
 End of File
*/

