/*******************************************************************************
  ${QSPI_INSTANCE_NAME} Peripheral Library Source File

  Company
    Microchip Technology Inc.

  File Name
    plib_${QSPI_INSTANCE_NAME?lower_case}_spi.c

  Summary
    ${QSPI_INSTANCE_NAME} peripheral library interface when in SPI mode.

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

#include "plib_${QSPI_INSTANCE_NAME?lower_case}_spi.h"
#include "string.h" // memmove
<#if core.CoreSysIntFile == true>
#include "interrupts.h"
</#if>

static volatile qspi_spi_obj qspiObj;


void ${QSPI_INSTANCE_NAME}_Initialize(void)
{
    /* Reset and Disable the qspi Module */
    ${QSPI_INSTANCE_NAME}_REGS->QSPI_CTRLA = QSPI_CTRLA_SWRST_Msk;

    // Set Mode Register values
    /* MODE = ${QSPI_SMM} */
    /* LOOPEN = ${QSPI_LOOPEN} */
    /* WDRBT = 0 */
    /* SMEMREG = 0 */
    /* CSMODE = ${QSPI_CSMODE} */
    /* DATALEN = ${QSPI_DATALEN} */
    /* DLYCBT = 0 */
    /* DLYCS = 0 */
    ${QSPI_INSTANCE_NAME}_REGS->QSPI_CTRLB = QSPI_CTRLB_MODE_${QSPI_SMM} | QSPI_CTRLB_CSMODE_${QSPI_CSMODE} | QSPI_CTRLB_DATALEN(${QSPI_DATALEN}U) | QSPI_CTRLB_LOOPEN(${QSPI_LOOPEN}U);

    // Set serial clock register
    ${QSPI_INSTANCE_NAME}_REGS->QSPI_BAUD = (QSPI_BAUD_BAUD(${QSPI_SCBR}U)) <#if QSPI_CPOL=="HIGH"> | QSPI_BAUD_CPOL_Msk </#if> <#if QSPI_CPHA=="TRAILING"> | QSPI_BAUD_CPHA_Msk </#if>;

    // Enable the qspi Module
    /* LASTXFER = 0 */
    ${QSPI_INSTANCE_NAME}_REGS->QSPI_CTRLA = QSPI_CTRLA_ENABLE_Msk;

    while((${QSPI_INSTANCE_NAME}_REGS->QSPI_STATUS & QSPI_STATUS_ENABLE_Msk) != QSPI_STATUS_ENABLE_Msk)
    {
        /* Wait for QSPI enable flag to set */
    }
}

bool ${QSPI_INSTANCE_NAME}_WriteRead (void* pTransmitData, size_t txSize, void* pReceiveData, size_t rxSize)
{
    bool isRequestAccepted = false;
    uint32_t dummyData;

    /* Verify the request */
    if((qspiObj.transferIsBusy == false) && (((txSize > 0U) && (pTransmitData != NULL)) || ((rxSize > 0U) && (pReceiveData != NULL))))
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
        dummyData = (${QSPI_INSTANCE_NAME}_REGS->QSPI_RXDATA & QSPI_RXDATA_DATA_Msk) >> QSPI_RXDATA_DATA_Pos;
        (void)dummyData;

        size_t txSz = qspiObj.txSize;

        if (qspiObj.rxSize > txSz)
        {
            qspiObj.dummySize = qspiObj.rxSize - txSz;
        }

        /* Start the first write here itself, rest will happen in ISR context */
        if((${QSPI_INSTANCE_NAME}_REGS->QSPI_CTRLB & QSPI_CTRLB_DATALEN_Msk) == QSPI_CTRLB_DATALEN_8BITS)
        {
            if (qspiObj.txCount < txSz)
            {
                ${QSPI_INSTANCE_NAME}_REGS->QSPI_TXDATA = *((uint8_t*)qspiObj.txBuffer);
                qspiObj.txCount++;
            }
            else if (qspiObj.dummySize > 0U)
            {
                ${QSPI_INSTANCE_NAME}_REGS->QSPI_TXDATA = (uint8_t)(0xff);
                qspiObj.dummySize--;
            }
            else
            {
                /* No action required */
            }
        }
        else
        {
            qspiObj.txSize >>= 1;
            qspiObj.dummySize >>= 1;
            qspiObj.rxSize >>= 1;

            txSz = qspiObj.txSize;

            if (qspiObj.txCount < txSz)
            {
                ${QSPI_INSTANCE_NAME}_REGS->QSPI_TXDATA = *((uint16_t*)qspiObj.txBuffer);
                qspiObj.txCount++;
            }
            else if (qspiObj.dummySize > 0U)
            {
                ${QSPI_INSTANCE_NAME}_REGS->QSPI_TXDATA = (uint16_t)(0xff);
                qspiObj.dummySize--;
            }
            else
            {
                /* No action required */
            }
        }

        if ((int32_t)rxSize > 0)
        {
            /* Enable receive interrupt to complete the transfer in ISR context */
            ${QSPI_INSTANCE_NAME}_REGS->QSPI_INTENSET = QSPI_INTENSET_RXC_Msk;
        }
        else
        {
            /* Enable transmit interrupt to complete the transfer in ISR context */
            ${QSPI_INSTANCE_NAME}_REGS->QSPI_INTENSET = QSPI_INTENSET_DRE_Msk;
        }
    }

    return isRequestAccepted;
}

bool ${QSPI_INSTANCE_NAME}_Write(void* pTransmitData, size_t txSize)
{
    return(${QSPI_INSTANCE_NAME}_WriteRead(pTransmitData, txSize, NULL, 0));
}

bool ${QSPI_INSTANCE_NAME}_Read(void* pReceiveData, size_t rxSize)
{
    return(${QSPI_INSTANCE_NAME}_WriteRead(NULL, 0, pReceiveData, rxSize));
}

bool ${QSPI_INSTANCE_NAME}_TransferSetup (QSPI_TRANSFER_SETUP * setup, uint32_t spiSourceClock )
{
    uint32_t scbr;
    bool setup_status = false;
    if ((setup != NULL) && (setup->clockFrequency != 0U))
    {
        /* Disable the module */
        ${QSPI_INSTANCE_NAME}_REGS->QSPI_CTRLA &= ~QSPI_CTRLA_ENABLE_Msk;

        if(spiSourceClock == 0U)
        {
            // Fetch Master Clock Frequency directly
            spiSourceClock = ${QSPI_BAUD_RATE};
        }

        scbr = spiSourceClock/setup->clockFrequency;

        if(scbr > 255U)
        {
            scbr = 255;
        }

        /* Set up clock polarity, phase, and baud rate */
        ${QSPI_INSTANCE_NAME}_REGS->QSPI_BAUD= (uint32_t)setup->clockPolarity | (uint32_t)setup->clockPhase | QSPI_BAUD_BAUD(scbr);

        /* Set up number of bits per transfer */
        ${QSPI_INSTANCE_NAME}_REGS->QSPI_CTRLB = (${QSPI_INSTANCE_NAME}_REGS->QSPI_CTRLB & ~QSPI_CTRLB_DATALEN_Msk) | (uint32_t)setup->dataBits;

        /* Enable the module */
        ${QSPI_INSTANCE_NAME}_REGS->QSPI_CTRLA = QSPI_CTRLA_ENABLE_Msk;

        while((${QSPI_INSTANCE_NAME}_REGS->QSPI_STATUS & QSPI_STATUS_ENABLE_Msk) != QSPI_STATUS_ENABLE_Msk)
        {
            /* Wait for QSPI enable flag to set */
        }
        setup_status = true;
    }
    return setup_status;
}

void ${QSPI_INSTANCE_NAME}_CallbackRegister (QSPI_CALLBACK callback, uintptr_t context)
{
    qspiObj.callback = callback;
    qspiObj.context = context;
}

bool ${QSPI_INSTANCE_NAME}_IsBusy(void)
{
    bool transferIsBusy = qspiObj.transferIsBusy;

    return (((${QSPI_INSTANCE_NAME}_REGS->QSPI_INTFLAG & QSPI_INTFLAG_DRE_Msk ) == 0U) || (transferIsBusy));
}

bool ${QSPI_INSTANCE_NAME}_IsTransmitterBusy(void)
{
    return ((${QSPI_INSTANCE_NAME}_REGS->QSPI_INTFLAG & QSPI_INTFLAG_TXC_Msk ) == 0U);
}

void __attribute__((used)) ${QSPI_INSTANCE_NAME}_InterruptHandler(void)
{
    uint32_t dataBits ;
    uint32_t receivedData;
    static bool isLastByteTransferInProgress = false;
    size_t rxCount = qspiObj.rxCount;
    size_t txCount = qspiObj.txCount;
    size_t txSize = qspiObj.txSize;

    dataBits = ${QSPI_INSTANCE_NAME}_REGS->QSPI_CTRLB & QSPI_CTRLB_DATALEN_Msk;


    /* See if there's received data (MOSI) to be processed */
    if ((${QSPI_INSTANCE_NAME}_REGS->QSPI_INTFLAG & QSPI_INTFLAG_RXC_Msk ) == QSPI_INTFLAG_RXC_Msk)
    {
        receivedData = (${QSPI_INSTANCE_NAME}_REGS->QSPI_RXDATA & QSPI_RXDATA_DATA_Msk) >> QSPI_RXDATA_DATA_Pos;

        if (rxCount < qspiObj.rxSize)
        {
            if(dataBits == QSPI_CTRLB_DATALEN_8BITS)
            {
                ((uint8_t*)qspiObj.rxBuffer)[rxCount] = (uint8_t)receivedData;
                rxCount++;
            }
            else
            {
                ((uint16_t*)qspiObj.rxBuffer)[rxCount] = (uint16_t)receivedData;
                rxCount++;
            }

            qspiObj.rxCount = rxCount;
        }
    }

    /* If there are more words to be transmitted, then transmit them here and keep track of the count */
    if((${QSPI_INSTANCE_NAME}_REGS->QSPI_INTFLAG & QSPI_INTFLAG_DRE_Msk) == QSPI_INTFLAG_DRE_Msk)
    {
        /* Disable the TDRE interrupt. This will be enabled back if more than
         * one byte is pending to be transmitted */
        ${QSPI_INSTANCE_NAME}_REGS->QSPI_INTENCLR = QSPI_INTENCLR_DRE_Msk;

        if(dataBits == QSPI_CTRLB_DATALEN_8BITS)
        {
            if (txCount < qspiObj.txSize)
            {
                ${QSPI_INSTANCE_NAME}_REGS->QSPI_TXDATA = ((uint8_t*)qspiObj.txBuffer)[txCount];
                txCount++;
            }
            else if (qspiObj.dummySize > 0U)
            {
                ${QSPI_INSTANCE_NAME}_REGS->QSPI_TXDATA = (uint8_t)(0xff);
                qspiObj.dummySize--;
            }
            else
            {
                /* No action required */
            }
        }
        else
        {
            if (txCount < qspiObj.txSize)
            {
                ${QSPI_INSTANCE_NAME}_REGS->QSPI_TXDATA = ((uint16_t*)qspiObj.txBuffer)[txCount];
                txCount++;
            }
            else if (qspiObj.dummySize > 0U)
            {
                ${QSPI_INSTANCE_NAME}_REGS->QSPI_TXDATA = (uint16_t)(0xff);
                qspiObj.dummySize--;
            }
            else
            {
                /* No action required */
            }
        }

        qspiObj.txCount = txCount;

        if ((qspiObj.dummySize == 0U) && (txCount == txSize))
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
            ${QSPI_INSTANCE_NAME}_REGS->QSPI_CTRLA = QSPI_CTRLA_LASTXFER_Msk | QSPI_CTRLA_ENABLE_Msk;
        }
        else if (rxCount == qspiObj.rxSize)
        {
            /* Enable TDRE interrupt as all the requested bytes are received
             * and can now make use of the internal transmit shift register.
             */
            ${QSPI_INSTANCE_NAME}_REGS->QSPI_INTENCLR = QSPI_INTENCLR_RXC_Msk;
            ${QSPI_INSTANCE_NAME}_REGS->QSPI_INTENSET = QSPI_INTENSET_DRE_Msk;
        }
        else
        {
            /* No action required */
        }
    }

    /* See if Exchange is complete */
    if (((${QSPI_INSTANCE_NAME}_REGS->QSPI_INTFLAG & QSPI_INTFLAG_TXC_Msk) == QSPI_INTFLAG_TXC_Msk) && (isLastByteTransferInProgress == true))
    {
        if (rxCount == qspiObj.rxSize)
        {
            qspiObj.transferIsBusy = false;

            /* Disable TDRE, RDRF and TXEMPTY interrupts */
            ${QSPI_INSTANCE_NAME}_REGS->QSPI_INTENCLR = QSPI_INTENCLR_DRE_Msk | QSPI_INTENCLR_RXC_Msk | QSPI_INTENCLR_TXC_Msk;

            isLastByteTransferInProgress = false;

            if(qspiObj.callback != NULL)
            {
                uintptr_t context = qspiObj.context;

                qspiObj.callback(context);
            }
        }
    }
    if (isLastByteTransferInProgress == true)
    {
        /* For the last byte transfer, the TDRE interrupt is already disabled.
         * Enable TXEMPTY interrupt to ensure no data is present in the shift
         * register before application callback is called.
         */
        ${QSPI_INSTANCE_NAME}_REGS->QSPI_INTENSET = QSPI_INTENSET_TXC_Msk;
    }

}
/*******************************************************************************
 End of File
*/