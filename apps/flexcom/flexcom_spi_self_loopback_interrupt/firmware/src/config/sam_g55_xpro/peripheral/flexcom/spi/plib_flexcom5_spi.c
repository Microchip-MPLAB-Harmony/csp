/*******************************************************************************
  FLEXCOM5 SPI PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_flexcom5_spi.c

  Summary:
    FLEXCOM5 SPI PLIB Implementation File.

  Description:
    This file defines the interface to the FLEXCOM SPI peripheral library.
    This library provides access to and control of the associated
    peripheral instance.

  Remarks:
    None.

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

#include "plib_flexcom5_spi.h"

// *****************************************************************************
// *****************************************************************************
// Section: FLEXCOM5 SPI Implementation
// *****************************************************************************
// *****************************************************************************

/* Global object to save FLEXCOM SPI Exchange related data */
FLEXCOM_SPI_OBJECT flexcom5SpiObj;

void FLEXCOM5_SPI_Initialize( void )
{
    /* Set FLEXCOM SPI operating mode */
    FLEXCOM5_REGS->FLEXCOM_MR = FLEXCOM_MR_OPMODE_SPI;

    /* Disable and Reset the FLEXCOM SPI */
    SPI5_REGS->SPI_CR = SPI_CR_SPIDIS_Msk | SPI_CR_SWRST_Msk;

    /* Enable Master mode, select clock source, select particular NPCS line for chip select and disable mode fault detection */
    SPI5_REGS->SPI_MR = SPI_MR_MSTR_Msk | SPI_MR_BRSRCCLK_PERIPH_CLK | SPI_MR_PCS(0) | SPI_MR_MODFDIS_Msk;

    /* Set up clock Polarity, data phase, Communication Width, Baud Rate and Chip select active after transfer */
    SPI5_REGS->SPI_CSR[0] = SPI_CSR_CPOL(0) | SPI_CSR_NCPHA(1) | SPI_CSR_BITS_8_BIT | SPI_CSR_SCBR(119) | SPI_CSR_CSAAT_Msk;

    /* Initialize global variables */
    flexcom5SpiObj.transferIsBusy = false;
    flexcom5SpiObj.callback = NULL;

    /* Enable FLEXCOM5 SPI */
    SPI5_REGS->SPI_CR = SPI_CR_SPIEN_Msk;
}

bool FLEXCOM5_SPI_WriteRead( void* pTransmitData, size_t txSize, void* pReceiveData, size_t rxSize )
{
    bool isRequestAccepted = false;
    uint32_t dummyData;

    /* Verify the request */
    if((((txSize > 0) && (pTransmitData != NULL)) || ((rxSize > 0) && (pReceiveData != NULL))) && (flexcom5SpiObj.transferIsBusy == false))
    {
        isRequestAccepted = true;

        flexcom5SpiObj.txBuffer = pTransmitData;
        flexcom5SpiObj.rxBuffer = pReceiveData;
        flexcom5SpiObj.rxCount = 0;
        flexcom5SpiObj.txCount = 0;
        flexcom5SpiObj.dummySize = 0;

        if (pTransmitData != NULL)
        {
            flexcom5SpiObj.txSize = txSize;
        }
        else
        {
            flexcom5SpiObj.txSize = 0;
        }

        if (pReceiveData != NULL)
        {
            flexcom5SpiObj.rxSize = rxSize;
        }
        else
        {
            flexcom5SpiObj.rxSize = 0;
        }

        flexcom5SpiObj.transferIsBusy = true;

        /* Flush out any unread data in SPI read buffer */
        dummyData = (SPI5_REGS->SPI_RDR & SPI_RDR_RD_Msk) >> SPI_RDR_RD_Pos;
        (void)dummyData;

        if (flexcom5SpiObj.rxSize > flexcom5SpiObj.txSize)
        {
            flexcom5SpiObj.dummySize = flexcom5SpiObj.rxSize - flexcom5SpiObj.txSize;
        }

        /* Start the first write here itself, rest will happen in ISR context */
        if((SPI5_REGS->SPI_CSR[0] & SPI_CSR_BITS_Msk) == SPI_CSR_BITS_8_BIT)
        {
            if (flexcom5SpiObj.txCount < flexcom5SpiObj.txSize)
            {
                SPI5_REGS->SPI_TDR = *((uint8_t*)flexcom5SpiObj.txBuffer);
                flexcom5SpiObj.txCount++;
            }
            else if (flexcom5SpiObj.dummySize > 0)
            {
                SPI5_REGS->SPI_TDR = (uint8_t)(0xff);
                flexcom5SpiObj.dummySize--;
            }
        }
        else
        {
            flexcom5SpiObj.txSize >>= 1;
            flexcom5SpiObj.dummySize >>= 1;
            flexcom5SpiObj.rxSize >>= 1;

            if (flexcom5SpiObj.txCount < flexcom5SpiObj.txSize)
            {
                SPI5_REGS->SPI_TDR = *((uint16_t*)flexcom5SpiObj.txBuffer);
                flexcom5SpiObj.txCount++;
            }
            else if (flexcom5SpiObj.dummySize > 0)
            {
                SPI5_REGS->SPI_TDR = (uint16_t)(0xff);
                flexcom5SpiObj.dummySize--;
            }
        }

        if (rxSize > 0)
        {
            /* Enable receive interrupt to complete the transfer in ISR context */
            SPI5_REGS->SPI_IER = SPI_IER_RDRF_Msk;
        }
        else
        {
            /* Enable transmit interrupt to complete the transfer in ISR context */
            SPI5_REGS->SPI_IER = SPI_IER_TDRE_Msk;
        }
    }

    return isRequestAccepted;
}

bool FLEXCOM5_SPI_TransferSetup( FLEXCOM_SPI_TRANSFER_SETUP * setup, uint32_t spiSourceClock )
{
    uint32_t scbr;

    if ((setup == NULL) || (setup->clockFrequency == 0))
    {
        return false;
    }
    if(spiSourceClock == 0)
    {
        // Fetch Master Clock Frequency directly
        spiSourceClock = 119996416;
    }

    scbr = spiSourceClock/setup->clockFrequency;

    if(scbr == 0)
    {
        scbr = 1;
    }
    else if(scbr > 255)
    {
        scbr = 255;
    }

    SPI5_REGS->SPI_CSR[0] = (uint32_t)setup->clockPolarity | (uint32_t)setup->clockPhase | (uint32_t)setup->dataBits | SPI_CSR_SCBR(scbr);

    return true;
}

bool FLEXCOM5_SPI_Write( void* pTransmitData, size_t txSize )
{
    return (FLEXCOM5_SPI_WriteRead(pTransmitData, txSize, NULL, 0));
}

bool FLEXCOM5_SPI_Read( void* pReceiveData, size_t rxSize )
{
    return (FLEXCOM5_SPI_WriteRead(NULL, 0, pReceiveData, rxSize));
}

void FLEXCOM5_SPI_CallbackRegister( FLEXCOM_SPI_CALLBACK callback, uintptr_t context )
{
    flexcom5SpiObj.callback = callback;
    flexcom5SpiObj.context = context;
}

bool FLEXCOM5_SPI_IsBusy( void )
{
    return ((flexcom5SpiObj.transferIsBusy) || ((SPI5_REGS->SPI_SR & SPI_SR_TXEMPTY_Msk) == 0));
}

void FLEXCOM5_InterruptHandler( void )
{
    uint32_t dataBits;
    uint32_t receivedData;
    dataBits = SPI5_REGS->SPI_CSR[0] & SPI_CSR_BITS_Msk;

    static bool isLastByteTransferInProgress = false;

    /* save the status in global object before it gets cleared */
    flexcom5SpiObj.status = SPI5_REGS->SPI_SR;


    if ((SPI5_REGS->SPI_SR & SPI_SR_RDRF_Msk) == SPI_SR_RDRF_Msk)
    {
        receivedData = (SPI5_REGS->SPI_RDR & SPI_RDR_RD_Msk) >> SPI_RDR_RD_Pos;

        if (flexcom5SpiObj.rxCount < flexcom5SpiObj.rxSize)
        {
            if(dataBits == SPI_CSR_BITS_8_BIT)
            {
                ((uint8_t*)flexcom5SpiObj.rxBuffer)[flexcom5SpiObj.rxCount++] = receivedData;
            }
            else
            {
                ((uint16_t*)flexcom5SpiObj.rxBuffer)[flexcom5SpiObj.rxCount++] = receivedData;
            }
        }
    }

    /* If there are more words to be transmitted, then transmit them here and keep track of the count */
    if((SPI5_REGS->SPI_SR & SPI_SR_TDRE_Msk) == SPI_SR_TDRE_Msk)
    {
        /* Disable the TDRE interrupt. This will be enabled back if more than
         * one byte is pending to be transmitted */
        SPI5_REGS->SPI_IDR = SPI_IDR_TDRE_Msk;

        if(dataBits == SPI_CSR_BITS_8_BIT)
        {
            if (flexcom5SpiObj.txCount < flexcom5SpiObj.txSize)
            {
                SPI5_REGS->SPI_TDR = ((uint8_t*)flexcom5SpiObj.txBuffer)[flexcom5SpiObj.txCount++];
            }
            else if (flexcom5SpiObj.dummySize > 0)
            {
                SPI5_REGS->SPI_TDR = (uint8_t)(0xff);
                flexcom5SpiObj.dummySize--;
            }
        }
        else
        {
            if (flexcom5SpiObj.txCount < flexcom5SpiObj.txSize)
            {
                SPI5_REGS->SPI_TDR = ((uint16_t*)flexcom5SpiObj.txBuffer)[flexcom5SpiObj.txCount++];
            }
            else if (flexcom5SpiObj.dummySize > 0)
            {
                SPI5_REGS->SPI_TDR = (uint16_t)(0xff);
                flexcom5SpiObj.dummySize--;
            }
        }
        if ((flexcom5SpiObj.txCount == flexcom5SpiObj.txSize) && (flexcom5SpiObj.dummySize == 0))
        {
            /* At higher baud rates, the data in the shift register can be
             * shifted out and TXEMPTY flag can get set resulting in a
             * callback been given to the application with the SPI interrupt
             * pending with the application. This will then result in the
             * interrupt handler being called again with nothing to transmit.
             * To avoid the above mentioned issue, a software flag is set, but
             * the TXEMPTY interrupt is not enabled until the very end.
             * At higher baud rates, if the software flag is set and the
             * TXEMPTY status bit is set, then it means that the transfer is
             * complete and a callback can be given to the application. Since
             * the TXEMPTY interrupt is not enabled there is no need to
             * explicitly clear the pending interrupt from the Interrupt controller.
             */
            isLastByteTransferInProgress = true;

            /* Set Last transfer to deassert NPCS after the last byte written in TDR has been transferred. */
            SPI5_REGS->SPI_CR = SPI_CR_LASTXFER_Msk;
        }
        else if (flexcom5SpiObj.rxCount == flexcom5SpiObj.rxSize)
        {
            /* Enable TDRE interrupt as all the requested bytes are received
             * and can now make use of the internal transmit shift register.
             */
            SPI5_REGS->SPI_IDR = SPI_IDR_RDRF_Msk;
            SPI5_REGS->SPI_IER = SPI_IDR_TDRE_Msk;
        }
    }

    /* See if Exchange is complete */
    if ((isLastByteTransferInProgress == true) && ((SPI5_REGS->SPI_SR & SPI_SR_TXEMPTY_Msk) == SPI_SR_TXEMPTY_Msk))
    {
        if (flexcom5SpiObj.rxCount == flexcom5SpiObj.rxSize)
        {
            flexcom5SpiObj.transferIsBusy = false;

            /* Disable TDRE, RDRF and TXEMPTY interrupts */
            SPI5_REGS->SPI_IDR = SPI_IDR_TDRE_Msk | SPI_IDR_RDRF_Msk | SPI_IDR_TXEMPTY_Msk;

            isLastByteTransferInProgress = false;

            if(flexcom5SpiObj.callback != NULL)
            {
                flexcom5SpiObj.callback(flexcom5SpiObj.context);
            }
        }
    }
    if (isLastByteTransferInProgress == true)
    {
        /* For the last byte transfer, the TDRE interrupt is already disabled.
         * Enable TXEMPTY interrupt to ensure no data is present in the shift
         * register before application callback is called.
         */
        SPI5_REGS->SPI_IER = SPI_IER_TXEMPTY_Msk;
    }
}
