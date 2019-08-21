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
#include "string.h"

/* Macro definitions */
#define LED_On      LED_Clear
#define LED_Off     LED_Set

#define DMA_CHANNEL_RECEIVE         DMAC_CHANNEL_0
#define DMA_CHANNEL_TRANSMIT        DMAC_CHANNEL_1

typedef enum
{
    APP_STATE_INITIALIZE,
	APP_STATE_SPI_IDLE,
    APP_STATE_VERIFY_AND_UPDATE_PING_BUFFER,
    APP_STATE_VERIFY_AND_UPDATE_PONG_BUFFER,
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

dmac_descriptor_registers_t pTxLinkedListDesc[2] __attribute__((aligned(16),space(data),address(0x30000500),keep,externally_visible));
dmac_descriptor_registers_t pRxLinkedListDesc[2] __attribute__((aligned(16),space(data),address(0x30000520),keep,externally_visible));

#define PING_BUFEER0_TX_BTCTRL  (DMAC_BTCTRL_STEPSIZE_X1 | DMAC_BTCTRL_SRCINC_Msk |     \
                                DMAC_BTCTRL_BEATSIZE_BYTE | DMAC_BTCTRL_BLOCKACT_INT | DMAC_BTCTRL_VALID_Msk)
#define PING_BUFEER1_TX_BTCTRL  (DMAC_BTCTRL_STEPSIZE_X1 | DMAC_BTCTRL_SRCINC_Msk |     \
                                DMAC_BTCTRL_BEATSIZE_BYTE | DMAC_BTCTRL_BLOCKACT_INT | DMAC_BTCTRL_VALID_Msk)
#define PING_BUFEER0_RX_BTCTRL  (DMAC_BTCTRL_STEPSIZE_X1 | DMAC_BTCTRL_DSTINC_Msk |     \
                                DMAC_BTCTRL_BEATSIZE_BYTE | DMAC_BTCTRL_BLOCKACT_INT | DMAC_BTCTRL_VALID_Msk)
#define PING_BUFEER1_RX_BTCTRL  (DMAC_BTCTRL_STEPSIZE_X1 | DMAC_BTCTRL_DSTINC_Msk |     \
                                DMAC_BTCTRL_BEATSIZE_BYTE | DMAC_BTCTRL_BLOCKACT_INT | DMAC_BTCTRL_VALID_Msk)

void APP_InitializeTxLinkedListDescriptor(void)
{
    pTxLinkedListDesc[0].DMAC_BTCTRL     = (uint16_t)PING_BUFEER0_TX_BTCTRL;
    pTxLinkedListDesc[0].DMAC_BTCNT      = (uint16_t)sizeof(txPingBuffer);
    pTxLinkedListDesc[0].DMAC_DESCADDR   = (uint32_t)&pTxLinkedListDesc[1];
    pTxLinkedListDesc[0].DMAC_DSTADDR    = (uint32_t)&SERCOM0_REGS->SPIM.SERCOM_DATA;
    pTxLinkedListDesc[0].DMAC_SRCADDR    = (uint32_t)txPingBuffer + sizeof(txPingBuffer);

    pTxLinkedListDesc[1].DMAC_BTCTRL     = (uint16_t)PING_BUFEER1_TX_BTCTRL;
    pTxLinkedListDesc[1].DMAC_BTCNT      = (uint16_t)sizeof(txPongBuffer);
    pTxLinkedListDesc[1].DMAC_DESCADDR   = (uint32_t)&pTxLinkedListDesc[0];
    pTxLinkedListDesc[1].DMAC_DSTADDR    = (uint32_t)&SERCOM0_REGS->SPIM.SERCOM_DATA;
    pTxLinkedListDesc[1].DMAC_SRCADDR    = (uint32_t)txPongBuffer + sizeof(txPongBuffer);
}

void APP_InitializeRxLinkedListDescriptor(void)
{
    pRxLinkedListDesc[0].DMAC_BTCTRL     = (uint16_t)PING_BUFEER0_RX_BTCTRL;
    pRxLinkedListDesc[0].DMAC_BTCNT      = (uint16_t)sizeof(rxPingBuffer);
    pRxLinkedListDesc[0].DMAC_DESCADDR   = (uint32_t)&pRxLinkedListDesc[1];
    pRxLinkedListDesc[0].DMAC_SRCADDR    = (uint32_t)&SERCOM0_REGS->SPIM.SERCOM_DATA;
    pRxLinkedListDesc[0].DMAC_DSTADDR    = (uint32_t)rxPingBuffer + sizeof(rxPingBuffer);

    pRxLinkedListDesc[1].DMAC_BTCTRL     = (uint16_t)PING_BUFEER1_RX_BTCTRL;
    pRxLinkedListDesc[1].DMAC_BTCNT      = (uint16_t)sizeof(rxPongBuffer);
    pRxLinkedListDesc[1].DMAC_DESCADDR   = (uint32_t)&pRxLinkedListDesc[0];
    pRxLinkedListDesc[1].DMAC_SRCADDR    = (uint32_t)&SERCOM0_REGS->SPIM.SERCOM_DATA;
    pRxLinkedListDesc[1].DMAC_DSTADDR    = (uint32_t)rxPongBuffer + sizeof(rxPongBuffer);
}

static void APP_DMA_TxCallbackHandler(DMAC_TRANSFER_EVENT event, uintptr_t context)
{
    if(event == DMAC_TRANSFER_EVENT_ERROR)
    {
        state = APP_STATE_SPI_XFER_ERROR;
    }
}

static void APP_DMA_RxCallbackHandler(DMAC_TRANSFER_EVENT event, uintptr_t context)
{
    static BUFFER_TYPE bufferType = BUFFER_TYPE_PING;

    if(event == DMAC_TRANSFER_EVENT_COMPLETE)
    {
        if(bufferType == BUFFER_TYPE_PING)
        {
            state = APP_STATE_VERIFY_AND_UPDATE_PING_BUFFER;
            bufferType = BUFFER_TYPE_PONG;
        }
        else
        {
            state = APP_STATE_VERIFY_AND_UPDATE_PONG_BUFFER;
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
    uint8_t pingData=0, pongData=0x44;
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
                DMAC_ChannelCallbackRegister(DMA_CHANNEL_TRANSMIT, APP_DMA_TxCallbackHandler, (uintptr_t)NULL);
                DMAC_ChannelCallbackRegister(DMA_CHANNEL_RECEIVE, APP_DMA_RxCallbackHandler, (uintptr_t)NULL);

                /* Start the DMA in linked list mode */
                DMAC_ChannelLinkedListTransfer(DMA_CHANNEL_RECEIVE, &pRxLinkedListDesc[0]);
                DMAC_ChannelLinkedListTransfer(DMA_CHANNEL_TRANSMIT, &pTxLinkedListDesc[0]);

                state = APP_STATE_SPI_IDLE;
                break;
            }            
            case APP_STATE_VERIFY_AND_UPDATE_PING_BUFFER:
            {
                if (memcmp(&txPingBuffer[0], &rxPingBuffer[0], sizeof(txPingBuffer)) != 0)
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
                    state = APP_STATE_SPI_IDLE;
                }
                break;
            }
            case APP_STATE_VERIFY_AND_UPDATE_PONG_BUFFER:
            {
                if (memcmp(&txPongBuffer[0], &rxPongBuffer[0], sizeof(txPongBuffer)) != 0)
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
                state = APP_STATE_SPI_IDLE;
                break;
            }
            case APP_STATE_SPI_XFER_ERROR:
            {
                /* Abort DMA */
                DMAC_ChannelDisable(DMA_CHANNEL_TRANSMIT);
                DMAC_ChannelDisable(DMA_CHANNEL_RECEIVE);

                /* Turn Off the LED */
                LED_Off();
                state = APP_STATE_SPI_IDLE;
                break;
            }
            case APP_STATE_SPI_IDLE:
            {
                /* Application can do other task here */
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

