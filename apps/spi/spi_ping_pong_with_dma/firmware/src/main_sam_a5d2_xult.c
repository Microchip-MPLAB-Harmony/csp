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
#include "string.h"

#define DMA_CHANNEL_RECEIVE             XDMAC_CHANNEL_0
#define DMA_CHANNEL_TRANSMIT            XDMAC_CHANNEL_1

#define SPI1_RECEIVE_ADDRESS            (&SPI1_REGS->SPI_RDR)
#define SPI1_TRANSMIT_ADDRESS           (&SPI1_REGS->SPI_TDR)

#define LED_On()                        LED_Clear()
#define LED_Off()                       LED_Set()

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
    pTxLinkedListDesc[0].mbr_da = (uint32_t)SPI1_TRANSMIT_ADDRESS;
    pTxLinkedListDesc[0].mbr_ubc.blockDataLength = sizeof(txPingBuffer);
    pTxLinkedListDesc[0].mbr_ubc.nextDescriptorControl.fetchEnable = 1;
    pTxLinkedListDesc[0].mbr_ubc.nextDescriptorControl.sourceUpdate = 1;
    pTxLinkedListDesc[0].mbr_ubc.nextDescriptorControl.destinationUpdate = 0;
    pTxLinkedListDesc[0].mbr_ubc.nextDescriptorControl.view = 1;


    pTxLinkedListDesc[1].mbr_nda = (uint32_t)&pTxLinkedListDesc[0];
    pTxLinkedListDesc[1].mbr_sa = (uint32_t)&txPongBuffer;
    pTxLinkedListDesc[1].mbr_da = (uint32_t)SPI1_TRANSMIT_ADDRESS;
    pTxLinkedListDesc[1].mbr_ubc.blockDataLength = sizeof(txPongBuffer);
    pTxLinkedListDesc[1].mbr_ubc.nextDescriptorControl.fetchEnable = 1;
    pTxLinkedListDesc[1].mbr_ubc.nextDescriptorControl.sourceUpdate = 1;
    pTxLinkedListDesc[1].mbr_ubc.nextDescriptorControl.destinationUpdate = 0;
    pTxLinkedListDesc[1].mbr_ubc.nextDescriptorControl.view = 1;
}

void APP_InitializeRxLinkedListDescriptor(void)
{
    pRxLinkedListDesc[0].mbr_nda = (uint32_t)&pRxLinkedListDesc[1];
    pRxLinkedListDesc[0].mbr_sa = (uint32_t)SPI1_RECEIVE_ADDRESS;
    pRxLinkedListDesc[0].mbr_da = (uint32_t)&rxPingBuffer;
    pRxLinkedListDesc[0].mbr_ubc.blockDataLength = sizeof(rxPingBuffer);
    pRxLinkedListDesc[0].mbr_ubc.nextDescriptorControl.fetchEnable= 1;
    pRxLinkedListDesc[0].mbr_ubc.nextDescriptorControl.sourceUpdate = 1;
    pRxLinkedListDesc[0].mbr_ubc.nextDescriptorControl.destinationUpdate = 0;
    pRxLinkedListDesc[0].mbr_ubc.nextDescriptorControl.view= 1;


    pRxLinkedListDesc[1].mbr_nda = (uint32_t)&pRxLinkedListDesc[0];
    pRxLinkedListDesc[1].mbr_sa = (uint32_t)SPI1_RECEIVE_ADDRESS;
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
    LED_Off();
    
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
                XDMAC0_ChannelCallbackRegister(DMA_CHANNEL_TRANSMIT, APP_DMA_TxCallbackHandler, (uintptr_t)NULL);
                XDMAC0_ChannelCallbackRegister(DMA_CHANNEL_RECEIVE, APP_DMA_RxCallbackHandler, (uintptr_t)NULL);

                /* Start the DMA in linked list mode */
                XDMAC0_ChannelLinkedListTransfer(DMA_CHANNEL_RECEIVE, (uint32_t)&pRxLinkedListDesc[0], &rxFirstDescriptorControl);
                XDMAC0_ChannelLinkedListTransfer(DMA_CHANNEL_TRANSMIT, (uint32_t)&pTxLinkedListDesc[0], &txFirstDescriptorControl);

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
                LED_On();
                break;
            }
            case APP_STATE_SPI_XFER_ERROR:
            {
                /* Abort DMA */
                XDMAC0_ChannelDisable(DMA_CHANNEL_TRANSMIT);
                XDMAC0_ChannelDisable(DMA_CHANNEL_RECEIVE);

                /* Turn Off the LED */
                LED_Off();
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

