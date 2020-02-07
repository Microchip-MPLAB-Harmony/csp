/*******************************************************************************
  QSPI Peripheral Library Source File

  Company
    Microchip Technology Inc.

  File Name
    plib_qspi_spi.c

  Summary
    QSPI peripheral library interface when in SPI mode.

  Description

  Remarks:
    
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

#include "plib_qspi_spi.h"
#include "string.h" // memmove

qspi_spi_obj qspiObj;


void QSPI_Initialize(void)
{
    /* Reset and Disable the qspi Module */
    QSPI_REGS->QSPI_CTRLA = QSPI_CTRLA_SWRST_Msk;

    // Set Mode Register values
    /* MODE = SPI */
    /* LOOPEN = 0 */
    /* WDRBT = 0 */
    /* SMEMREG = 0 */
    /* CSMODE = NORELOAD */
    /* DATALEN = 0x0 */
    /* DLYCBT = 0 */
    /* DLYCS = 0 */
    QSPI_REGS->QSPI_CTRLB = QSPI_CTRLB_MODE_SPI | QSPI_CTRLB_CSMODE_NORELOAD | QSPI_CTRLB_DATALEN(0x0) | QSPI_CTRLB_LOOPEN(0);

    // Set serial clock register
    QSPI_REGS->QSPI_BAUD = (QSPI_BAUD_BAUD(119))  ;

    // Enable the qspi Module
    /* LASTXFER = 0 */
    QSPI_REGS->QSPI_CTRLA = QSPI_CTRLA_ENABLE_Msk;

    while((QSPI_REGS->QSPI_STATUS & QSPI_STATUS_ENABLE_Msk) != QSPI_STATUS_ENABLE_Msk)
    {
        /* Wait for QSPI enable flag to set */
    }
}

bool QSPI_WriteRead (void* pTransmitData, size_t txSize, void* pReceiveData, size_t rxSize)
{
    bool isRequestAccepted = false;
    uint32_t dummyData;

    /* Verify the request */
    if((((txSize > 0) && (pTransmitData != NULL)) || ((rxSize > 0) && (pReceiveData != NULL))) && (qspiObj.transferIsBusy == false))
    {
        isRequestAccepted = true;
        qspiObj.txBuffer = pTransmitData;
        qspiObj.rxBuffer = pReceiveData;
        qspiObj.rxCount = 0;
        qspiObj.txCount = 0;
        qspiObj.dummySize = 0;
        if (pTransmitData != NULL)
        {
            qspiObj.txSize = txSize;
        }
        else
        {
            qspiObj.txSize = 0;
        }

        if (pReceiveData != NULL)
        {
            qspiObj.rxSize = rxSize;
        }
        else
        {
            qspiObj.rxSize = 0;
        }

        qspiObj.transferIsBusy = true;

        /* Flush out any unread data in SPI read buffer */
        dummyData = (QSPI_REGS->QSPI_RXDATA & QSPI_RXDATA_DATA_Msk) >> QSPI_RXDATA_DATA_Pos;
        (void)dummyData;

        if (qspiObj.rxSize > qspiObj.txSize)
        {
            qspiObj.dummySize = qspiObj.rxSize - qspiObj.txSize;
        }

        /* Start the first write here itself, rest will happen in ISR context */
        if((QSPI_REGS->QSPI_CTRLB & QSPI_CTRLB_DATALEN_Msk) == QSPI_CTRLB_DATALEN_8BITS)
        {
            if (qspiObj.txCount < qspiObj.txSize)
            {
                QSPI_REGS->QSPI_TXDATA = *((uint8_t*)qspiObj.txBuffer);
                qspiObj.txCount++;
            }
            else if (qspiObj.dummySize > 0)
            {
                QSPI_REGS->QSPI_TXDATA = (uint8_t)(0xff);
                qspiObj.dummySize--;
            }
        }
        else
        {
            qspiObj.txSize >>= 1;
            qspiObj.dummySize >>= 1;
            qspiObj.rxSize >>= 1;

            if (qspiObj.txCount < qspiObj.txSize)
            {
                QSPI_REGS->QSPI_TXDATA = *((uint16_t*)qspiObj.txBuffer);
                qspiObj.txCount++;
            }
            else if (qspiObj.dummySize > 0)
            {
                QSPI_REGS->QSPI_TXDATA = (uint16_t)(0xff);
                qspiObj.dummySize--;
            }
        }

        if ((int)rxSize > 0)
        {
            /* Enable receive interrupt to complete the transfer in ISR context */
            QSPI_REGS->QSPI_INTENSET = QSPI_INTENSET_RXC_Msk;
        }
        else
        {
            /* Enable transmit interrupt to complete the transfer in ISR context */
            QSPI_REGS->QSPI_INTENSET = QSPI_INTENSET_DRE_Msk;
        }
    }

    return isRequestAccepted;
}

bool QSPI_Write(void* pTransmitData, size_t txSize)
{
    return(QSPI_WriteRead(pTransmitData, txSize, NULL, 0));
}

bool QSPI_Read(void* pReceiveData, size_t rxSize)
{
    return(QSPI_WriteRead(NULL, 0, pReceiveData, rxSize));
}

bool QSPI_TransferSetup (QSPI_TRANSFER_SETUP * setup, uint32_t spiSourceClock )
{
    uint32_t scbr;
    if ((setup == NULL) || (setup->clockFrequency == 0))
    {
        return false;
    }
    
    /* Disable the module */
    QSPI_REGS->QSPI_CTRLA &= ~QSPI_CTRLA_ENABLE_Msk;
    
    if(spiSourceClock == 0)
    {
        // Fetch Master Clock Frequency directly
        spiSourceClock = 1000000;
    }

    scbr = spiSourceClock/setup->clockFrequency;

    if(scbr > 255)
    {
        scbr = 255;
    }

    /* Set up clock polarity, phase, and baud rate */
    QSPI_REGS->QSPI_BAUD= (uint32_t)setup->clockPolarity | (uint32_t)setup->clockPhase | QSPI_BAUD_BAUD(scbr);

    /* Set up number of bits per transfer */
    QSPI_REGS->QSPI_CTRLB = (QSPI_REGS->QSPI_CTRLB & ~QSPI_CTRLB_DATALEN_Msk) | (uint32_t)setup->dataBits;

    /* Enable the module */
    QSPI_REGS->QSPI_CTRLA = QSPI_CTRLA_ENABLE_Msk;
    
    while((QSPI_REGS->QSPI_STATUS & QSPI_STATUS_ENABLE_Msk) != QSPI_STATUS_ENABLE_Msk)
    {
        /* Wait for QSPI enable flag to set */
    }
    
    return true;
}

void QSPI_CallbackRegister (QSPI_CALLBACK callback, uintptr_t context)
{
    qspiObj.callback = callback;
    qspiObj.context = context;
}

bool QSPI_IsBusy()
{
    return ((qspiObj.transferIsBusy) || ((QSPI_REGS->QSPI_INTFLAG & QSPI_INTFLAG_DRE_Msk ) == 0));
}

void QSPI_InterruptHandler(void)
{
    uint32_t dataBits ;
    uint32_t receivedData;
    static bool isLastByteTransferInProgress = false;

    dataBits = QSPI_REGS->QSPI_CTRLB & QSPI_CTRLB_DATALEN_Msk;

    /* See if there's received data (MOSI) to be processed */
    if ((QSPI_REGS->QSPI_INTFLAG & QSPI_INTFLAG_RXC_Msk ) == QSPI_INTFLAG_RXC_Msk)
    {
        receivedData = (QSPI_REGS->QSPI_RXDATA & QSPI_RXDATA_DATA_Msk) >> QSPI_RXDATA_DATA_Pos;

        if (qspiObj.rxCount < qspiObj.rxSize)
        {
            if(dataBits == QSPI_CTRLB_DATALEN_8BITS)
            {
                ((uint8_t*)qspiObj.rxBuffer)[qspiObj.rxCount++] = receivedData;
            }
            else
            {
                ((uint16_t*)qspiObj.rxBuffer)[qspiObj.rxCount++] = receivedData;
            }
        }
    }

    /* If there are more words to be transmitted, then transmit them here and keep track of the count */
    if((QSPI_REGS->QSPI_INTFLAG & QSPI_INTFLAG_DRE_Msk) == QSPI_INTFLAG_DRE_Msk)
    {
        /* Disable the TDRE interrupt. This will be enabled back if more than
         * one byte is pending to be transmitted */
        QSPI_REGS->QSPI_INTENCLR = QSPI_INTENCLR_DRE_Msk;

        if(dataBits == QSPI_CTRLB_DATALEN_8BITS)
        {
            if (qspiObj.txCount < qspiObj.txSize)
            {
                QSPI_REGS->QSPI_TXDATA = ((uint8_t*)qspiObj.txBuffer)[qspiObj.txCount++];
            }
            else if (qspiObj.dummySize > 0)
            {
                QSPI_REGS->QSPI_TXDATA = (uint8_t)(0xff);
                qspiObj.dummySize--;
            }
        }
        else
        {
            if (qspiObj.txCount < qspiObj.txSize)
            {
                QSPI_REGS->QSPI_TXDATA = ((uint16_t*)qspiObj.txBuffer)[qspiObj.txCount++];
            }
            else if (qspiObj.dummySize > 0)
            {
                QSPI_REGS->QSPI_TXDATA = (uint16_t)(0xff);
                qspiObj.dummySize--;
            }
        }
        if ((qspiObj.txCount == qspiObj.txSize) && (qspiObj.dummySize == 0))
        {
            /* At higher baud rates, the data in the shift register can be
             * shifted out and TXEMPTY flag can get set resulting in a
             * callback been given to the application with the SPI interrupt
             * pending with the application. This will then result in the
             * interrupt handler being called again with nothing to transmit.
             * To avoid this, a software flag is set, but
             * the TXEMPTY interrupt is not enabled until the very end.
             */

            isLastByteTransferInProgress = true;
            /* Set Last transfer to deassert NPCS after the last byte written in TDR has been transferred. */
            QSPI_REGS->QSPI_CTRLA = QSPI_CTRLA_LASTXFER_Msk | QSPI_CTRLA_ENABLE_Msk;
        }
        else if (qspiObj.rxCount == qspiObj.rxSize)
        {
            /* Enable TDRE interrupt as all the requested bytes are received
             * and can now make use of the internal transmit shift register.
             */
            QSPI_REGS->QSPI_INTENCLR = QSPI_INTENCLR_RXC_Msk;
            QSPI_REGS->QSPI_INTENSET = QSPI_INTENSET_DRE_Msk;
        }
    }

    /* See if Exchange is complete */
    if ((isLastByteTransferInProgress == true) && ((QSPI_REGS->QSPI_INTFLAG & QSPI_INTFLAG_TXC_Msk) == QSPI_INTFLAG_TXC_Msk))
    {
        if (qspiObj.rxCount == qspiObj.rxSize)
        {
            qspiObj.transferIsBusy = false;

            /* Disable TDRE, RDRF and TXEMPTY interrupts */
            QSPI_REGS->QSPI_INTENCLR = QSPI_INTENCLR_DRE_Msk | QSPI_INTENCLR_RXC_Msk | QSPI_INTENCLR_TXC_Msk;

            isLastByteTransferInProgress = false;

            if(qspiObj.callback != NULL)
            {
                qspiObj.callback(qspiObj.context);
            }
        }
    }
    if (isLastByteTransferInProgress == true)
    {
        /* For the last byte transfer, the TDRE interrupt is already disabled.
         * Enable TXEMPTY interrupt to ensure no data is present in the shift
         * register before application callback is called.
         */
        QSPI_REGS->QSPI_INTENSET = QSPI_INTENSET_TXC_Msk;
    }

}
/*******************************************************************************
 End of File
*/