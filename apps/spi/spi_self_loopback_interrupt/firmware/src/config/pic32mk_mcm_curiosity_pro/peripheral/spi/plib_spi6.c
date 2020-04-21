/*******************************************************************************
  SPI PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_spi6.c

  Summary:
    SPI6 Source File

  Description:
    This file has implementation of all the interfaces provided for particular
    SPI peripheral.

*******************************************************************************/

/*******************************************************************************
* Copyright (C) 2018-2019 Microchip Technology Inc. and its subsidiaries.
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

#include "plib_spi6.h"

// *****************************************************************************
// *****************************************************************************
// Section: SPI6 Implementation
// *****************************************************************************
// *****************************************************************************

/* Global object to save SPI Exchange related data */
SPI_OBJECT spi6Obj;

#define SPI6_CON_MSTEN                      (1 << _SPI6CON_MSTEN_POSITION)
#define SPI6_CON_CKP                        (0 << _SPI6CON_CKP_POSITION)
#define SPI6_CON_CKE                        (1 << _SPI6CON_CKE_POSITION)
#define SPI6_CON_MODE_32_MODE_16            (0 << _SPI6CON_MODE16_POSITION)
#define SPI6_CON_ENHBUF                     (1 << _SPI6CON_ENHBUF_POSITION)
#define SPI6_CON_MCLKSEL                    (0 << _SPI6CON_MCLKSEL_POSITION)
#define SPI6_CON_MSSEN                      (0 << _SPI6CON_MSSEN_POSITION)
#define SPI6_CON_SMP                        (0 << _SPI6CON_SMP_POSITION)

void SPI6_Initialize ( void )
{
    uint32_t rdata;

    /* Disable SPI6 Interrupts */
    IEC7CLR = 0x8;
    IEC7CLR = 0x10;
    IEC7CLR = 0x20;

    /* STOP and Reset the SPI */
    SPI6CON = 0;

    /* Clear the Receiver buffer */
    rdata = SPI6BUF;
    rdata = rdata;

    /* Clear SPI6 Interrupt flags */
    IFS7CLR = 0x8;
    IFS7CLR = 0x10;
    IFS7CLR = 0x20;

    /* BAUD Rate register Setup */
    SPI6BRG = 29;

    /* CLear the Overflow */
    SPI6STATCLR = _SPI6STAT_SPIROV_MASK;

    /*
    MSTEN = 1
    CKP = 0
    CKE = 1
    MODE<32,16> = 0
    ENHBUF = 1
    MSSEN = 0
    MCLKSEL = 0
    */
    SPI6CONSET = (SPI6_CON_MSSEN | SPI6_CON_MCLKSEL | SPI6_CON_ENHBUF | SPI6_CON_MODE_32_MODE_16 | SPI6_CON_CKE | SPI6_CON_CKP | SPI6_CON_MSTEN | SPI6_CON_SMP);

    /* Enable transmit interrupt when transmit buffer is completely empty (STXISEL = '01') */
    /* Enable receive interrupt when the receive buffer is not empty (SRXISEL = '01') */
    SPI6CONSET = 0x00000005;

    /* Initialize global variables */
    spi6Obj.transferIsBusy = false;
    spi6Obj.callback = NULL;

    /* Enable SPI6 */
    SPI6CONSET = _SPI6CON_ON_MASK;
}

bool SPI6_TransferSetup (SPI_TRANSFER_SETUP* setup, uint32_t spiSourceClock )
{
    uint32_t t_brg;
    uint32_t baudHigh;
    uint32_t baudLow;
    uint32_t errorHigh;
    uint32_t errorLow;

    if ((setup == NULL) || (setup->clockFrequency == 0))
    {
        return false;
    }

    if(spiSourceClock == 0)
    {
        // Use Master Clock Frequency set in GUI
        spiSourceClock = 60000000;
    }

    t_brg = (((spiSourceClock / (setup->clockFrequency)) / 2u) - 1u);
    baudHigh = spiSourceClock / (2u * (t_brg + 1u));
    baudLow = spiSourceClock / (2u * (t_brg + 2u));
    errorHigh = baudHigh - setup->clockFrequency;
    errorLow = setup->clockFrequency - baudLow;

    if (errorHigh > errorLow)
    {
        t_brg++;
    }

    if(t_brg > 8191)
    {
        return false;
    }

    SPI6BRG = t_brg;
    SPI6CON = (SPI6CON & (~(_SPI6CON_MODE16_MASK | _SPI6CON_MODE32_MASK | _SPI6CON_CKP_MASK | _SPI6CON_CKE_MASK))) |
                            (setup->clockPolarity | setup->clockPhase | setup->dataBits);

    return true;
}

bool SPI6_Write(void* pTransmitData, size_t txSize)
{
    return(SPI6_WriteRead(pTransmitData, txSize, NULL, 0));
}

bool SPI6_Read(void* pReceiveData, size_t rxSize)
{
    return(SPI6_WriteRead(NULL, 0, pReceiveData, rxSize));
}

bool SPI6_WriteRead (void* pTransmitData, size_t txSize, void* pReceiveData, size_t rxSize)
{
    bool isRequestAccepted = false;
    uint32_t dummyData;

    /* Verify the request */
    if((((txSize > 0) && (pTransmitData != NULL)) || ((rxSize > 0) && (pReceiveData != NULL))) && (spi6Obj.transferIsBusy == false))
    {
        isRequestAccepted = true;
        spi6Obj.txBuffer = pTransmitData;
        spi6Obj.rxBuffer = pReceiveData;
        spi6Obj.rxCount = 0;
        spi6Obj.txCount = 0;
        spi6Obj.dummySize = 0;

        if (pTransmitData != NULL)
        {
            spi6Obj.txSize = txSize;
        }
        else
        {
            spi6Obj.txSize = 0;
        }

        if (pReceiveData != NULL)
        {
            spi6Obj.rxSize = rxSize;
        }
        else
        {
            spi6Obj.rxSize = 0;
        }

        spi6Obj.transferIsBusy = true;

        if (spi6Obj.rxSize > spi6Obj.txSize)
        {
            spi6Obj.dummySize = spi6Obj.rxSize - spi6Obj.txSize;
        }

        /* Clear the receive overflow error if any */
        SPI6STATCLR = _SPI6STAT_SPIROV_MASK;

        /* Make sure there is no data pending in the RX FIFO */
        /* Depending on 8/16/32 bit mode, there may be 16/8/4 bytes in the FIFO */
        while ((bool)(SPI6STAT & _SPI6STAT_SPIRBE_MASK) == false)
        {
            dummyData = SPI6BUF;
            (void)dummyData;
        }

        /* Configure SPI to generate receive interrupt when receive buffer is empty (SRXISEL = '01') */
        SPI6CONCLR = _SPI6CON_SRXISEL_MASK;
        SPI6CONSET = 0x00000001;

        /* Configure SPI to generate transmit interrupt when the transmit shift register is empty (STXISEL = '00')*/
        SPI6CONCLR = _SPI6CON_STXISEL_MASK;

        /* Disable the receive interrupt */
        IEC7CLR = 0x10;

        /* Disable the transmit interrupt */
        IEC7CLR = 0x20;

        /* Clear the receive interrupt flag */
        IFS7CLR = 0x10;

        /* Clear the transmit interrupt flag */
        IFS7CLR = 0x20;

        /* Start the first write here itself, rest will happen in ISR context */
        if((_SPI6CON_MODE32_MASK) == (SPI6CON & (_SPI6CON_MODE32_MASK)))
        {
            spi6Obj.txSize >>= 2;
            spi6Obj.dummySize >>= 2;
            spi6Obj.rxSize >>= 2;

            if(spi6Obj.txCount < spi6Obj.txSize)
            {
                SPI6BUF = *((uint32_t*)spi6Obj.txBuffer);
                spi6Obj.txCount++;
            }
            else if (spi6Obj.dummySize > 0)
            {
                SPI6BUF = (uint32_t)(0xff);
                spi6Obj.dummySize--;
            }
        }
        else if((_SPI6CON_MODE16_MASK) == (SPI6CON & (_SPI6CON_MODE16_MASK)))
        {
            spi6Obj.txSize >>= 1;
            spi6Obj.dummySize >>= 1;
            spi6Obj.rxSize >>= 1;

            if (spi6Obj.txCount < spi6Obj.txSize)
            {
                SPI6BUF = *((uint16_t*)spi6Obj.txBuffer);
                spi6Obj.txCount++;
            }
            else if (spi6Obj.dummySize > 0)
            {
                SPI6BUF = (uint16_t)(0xff);
                spi6Obj.dummySize--;
            }
        }
        else
        {
            if (spi6Obj.txCount < spi6Obj.txSize)
            {
                SPI6BUF = *((uint8_t*)spi6Obj.txBuffer);
                spi6Obj.txCount++;
            }
            else if (spi6Obj.dummySize > 0)
            {
                SPI6BUF = (uint8_t)(0xff);
                spi6Obj.dummySize--;
            }
        }

        if (rxSize > 0)
        {
            /* Enable receive interrupt to complete the transfer in ISR context.
             * Keep the transmit interrupt disabled. Transmit interrupt will be
             * enabled later if txCount < txSize, when rxCount = rxSize.
             */
            IEC7SET = 0x10;
        }
        else
        {
            if (spi6Obj.txCount != spi6Obj.txSize)
            {
                /* Configure SPI to generate transmit buffer empty interrupt only if more than
                 * data is pending (STXISEL = '01')  */
                SPI6CONSET = 0x00000004;
            }
            /* Enable transmit interrupt to complete the transfer in ISR context */
            IEC7SET = 0x20;
        }
    }

    return isRequestAccepted;
}

bool SPI6_IsBusy (void)
{
    return ( (spi6Obj.transferIsBusy) || ((SPI6STAT & _SPI6STAT_SRMT_MASK) == 0));
}

void SPI6_CallbackRegister (SPI_CALLBACK callback, uintptr_t context)
{
    spi6Obj.callback = callback;

    spi6Obj.context = context;
}

void SPI6_RX_InterruptHandler (void)
{
    uint32_t receivedData = 0;

    /* Check if the receive buffer is empty or not */
    if ((bool)(SPI6STAT & _SPI6STAT_SPIRBE_MASK) == false)
    {
        /* Receive buffer is not empty. Read the received data. */
        receivedData = SPI6BUF;

        if (spi6Obj.rxCount < spi6Obj.rxSize)
        {
            /* Copy the received data to the user buffer */
            if((_SPI6CON_MODE32_MASK) == (SPI6CON & (_SPI6CON_MODE32_MASK)))
            {
                ((uint32_t*)spi6Obj.rxBuffer)[spi6Obj.rxCount++] = receivedData;
            }
            else if((_SPI6CON_MODE16_MASK) == (SPI6CON & (_SPI6CON_MODE16_MASK)))
            {
                ((uint16_t*)spi6Obj.rxBuffer)[spi6Obj.rxCount++] = receivedData;
            }
            else
            {
                ((uint8_t*)spi6Obj.rxBuffer)[spi6Obj.rxCount++] = receivedData;
            }
            if ((spi6Obj.rxCount == spi6Obj.rxSize) && (spi6Obj.txCount < spi6Obj.txSize))
            {
                /* Reception of all bytes is complete. However, there are few more
                 * bytes to be transmitted as txCount != txSize. Finish the
                 * transmission of the remaining bytes from the transmit interrupt. */

                /* Disable the receive interrupt */
                IEC7CLR = 0x10;

                /* Generate TX interrupt when buffer is completely empty (STXISEL = '00') */
                SPI6CONCLR = _SPI6CON_STXISEL_MASK;
                SPI6CONSET = 0x00000004;

                /* Enable the transmit interrupt. Callback will be given from the
                 * transmit interrupt, when all bytes are shifted out. */
                IEC7SET = 0x20;
            }
        }
        if (spi6Obj.rxCount < spi6Obj.rxSize)
        {
            /* More bytes pending to be received .. */
            if((_SPI6CON_MODE32_MASK) == (SPI6CON & (_SPI6CON_MODE32_MASK)))
            {
                if (spi6Obj.txCount < spi6Obj.txSize)
                {
                    SPI6BUF = ((uint32_t*)spi6Obj.txBuffer)[spi6Obj.txCount++];
                }
                else if (spi6Obj.dummySize > 0)
                {
                    SPI6BUF = (uint32_t)(0xff);
                    spi6Obj.dummySize--;
                }
            }
            else if((_SPI6CON_MODE16_MASK) == (SPI6CON & (_SPI6CON_MODE16_MASK)))
            {
                if (spi6Obj.txCount < spi6Obj.txSize)
                {
                    SPI6BUF = ((uint16_t*)spi6Obj.txBuffer)[spi6Obj.txCount++];
                }
                else if (spi6Obj.dummySize > 0)
                {
                    SPI6BUF = (uint16_t)(0xff);
                    spi6Obj.dummySize--;
                }
            }
            else
            {
                if (spi6Obj.txCount < spi6Obj.txSize)
                {
                    SPI6BUF = ((uint8_t*)spi6Obj.txBuffer)[spi6Obj.txCount++];
                }
                else if (spi6Obj.dummySize > 0)
                {
                    SPI6BUF = (uint8_t)(0xff);
                    spi6Obj.dummySize--;
                }
            }
        }
        else
        {
            if((spi6Obj.rxCount == spi6Obj.rxSize) && (spi6Obj.txCount == spi6Obj.txSize))
            {
                /* Clear receiver overflow error if any */
                SPI6STATCLR = _SPI6STAT_SPIROV_MASK;

                /* Disable receive interrupt */
                IEC7CLR = 0x10;

                /* Transfer complete. Give a callback */
                spi6Obj.transferIsBusy = false;

                if(spi6Obj.callback != NULL)
                {
                    spi6Obj.callback(spi6Obj.context);
                }
            }
        }
    }

    /* Clear SPI6 RX Interrupt flag */
    /* This flag should cleared only after reading buffer */
    IFS7CLR = 0x10;
}

void SPI6_TX_InterruptHandler (void)
{
    /* If there are more words to be transmitted, then transmit them here and keep track of the count */
    if((SPI6STAT & _SPI6STAT_SPITBE_MASK) == _SPI6STAT_SPITBE_MASK)
    {
        if (spi6Obj.txCount < spi6Obj.txSize)
        {
            if((_SPI6CON_MODE32_MASK) == (SPI6CON & (_SPI6CON_MODE32_MASK)))
            {
                SPI6BUF = ((uint32_t*)spi6Obj.txBuffer)[spi6Obj.txCount++];
            }
            else if((_SPI6CON_MODE16_MASK) == (SPI6CON & (_SPI6CON_MODE16_MASK)))
            {
                SPI6BUF = ((uint16_t*)spi6Obj.txBuffer)[spi6Obj.txCount++];
            }
            else
            {
                SPI6BUF = ((uint8_t*)spi6Obj.txBuffer)[spi6Obj.txCount++];
            }

            if (spi6Obj.txCount == spi6Obj.txSize)
            {
                /* All bytes are submitted to the SPI module. Now, enable transmit
                 * interrupt when the shift register is empty (STXISEL = '00')*/
                SPI6CONCLR = _SPI6CON_STXISEL_MASK;
            }
        }
        else if ((spi6Obj.txCount == spi6Obj.txSize) && (SPI6STAT & _SPI6STAT_SRMT_MASK))
        {
            /* This part of code is executed when the shift register is empty. */

            /* Clear receiver overflow error if any */
            SPI6STATCLR = _SPI6STAT_SPIROV_MASK;

            /* Disable transmit interrupt */
            IEC7CLR = 0x20;

            /* Transfer complete. Give a callback */
            spi6Obj.transferIsBusy = false;

            if(spi6Obj.callback != NULL)
            {
                spi6Obj.callback(spi6Obj.context);
            }
        }
    }
    /* Clear the transmit interrupt flag */
    IFS7CLR = 0x20;
}

