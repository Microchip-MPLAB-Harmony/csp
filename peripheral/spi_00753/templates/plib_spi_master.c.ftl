/*******************************************************************************
  SPI PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${SPI_INSTANCE_NAME?lower_case}_master.c

  Summary:
    ${SPI_INSTANCE_NAME} Master Source File

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

#include "plib_${SPI_INSTANCE_NAME?lower_case}_master.h"
<#if core.CoreSysIntFile == true>
#include "interrupts.h"
</#if>

// *****************************************************************************
// *****************************************************************************
// Section: ${SPI_INSTANCE_NAME} Implementation
// *****************************************************************************
// *****************************************************************************

<#if SPI_INTERRUPT_MODE == true>
/* Global object to save SPI Exchange related data */
static volatile SPI_OBJECT ${SPI_INSTANCE_NAME?lower_case}Obj;
</#if>

#define ${SPI_INSTANCE_NAME}_CON_MSTEN                      (${SPI_MSTR_MODE_EN}UL << _${SPI_INSTANCE_NAME}CON_MSTEN_POSITION)
#define ${SPI_INSTANCE_NAME}_CON_CKP                        (${SPI_SPICON_CLK_POL}UL << _${SPI_INSTANCE_NAME}CON_CKP_POSITION)
#define ${SPI_INSTANCE_NAME}_CON_CKE                        (${SPI_SPICON_CLK_PH}UL << _${SPI_INSTANCE_NAME}CON_CKE_POSITION)
#define ${SPI_INSTANCE_NAME}_CON_MODE_32_MODE_16            (${SPI_SPICON_MODE}UL << _${SPI_INSTANCE_NAME}CON_MODE16_POSITION)
#define ${SPI_INSTANCE_NAME}_CON_ENHBUF                     (1UL << _${SPI_INSTANCE_NAME}CON_ENHBUF_POSITION)
#define ${SPI_INSTANCE_NAME}_CON_MSSEN                      (${SPI_SPICON_MSSEN}UL << _${SPI_INSTANCE_NAME}CON_MSSEN_POSITION)
#define ${SPI_INSTANCE_NAME}_CON_SMP                        (${SPI_SPICON_SMP}UL << _${SPI_INSTANCE_NAME}CON_SMP_POSITION)

void ${SPI_INSTANCE_NAME}_Initialize ( void )
{
    uint32_t rdata;

    /* Disable ${SPI_INSTANCE_NAME} Interrupts */
    ${SPI_FLT_IEC_REG}CLR = ${SPI_FLT_IEC_REG_MASK};
    ${SPI_RX_IEC_REG}CLR = ${SPI_RX_IEC_REG_MASK};
    ${SPI_TX_IEC_REG}CLR = ${SPI_TX_IEC_REG_MASK};

    /* STOP and Reset the SPI */
    ${SPI_INSTANCE_NAME}CON = 0;

    /* Clear the Receiver buffer */
    rdata = ${SPI_INSTANCE_NAME}BUF;
    rdata = rdata;

    /* Clear ${SPI_INSTANCE_NAME} Interrupt flags */
    ${SPI_FLT_IFS_REG}CLR = ${SPI_FLT_IFS_REG_MASK};
    ${SPI_RX_IFS_REG}CLR = ${SPI_RX_IFS_REG_MASK};
    ${SPI_TX_IFS_REG}CLR = ${SPI_TX_IFS_REG_MASK};

    /* BAUD Rate register Setup */
    ${SPI_INSTANCE_NAME}BRG = ${SPI_BRG_VALUE};

    /* CLear the Overflow */
    ${SPI_INSTANCE_NAME}STATCLR = _${SPI_INSTANCE_NAME}STAT_SPIROV_MASK;

    /*
    MSTEN = ${SPI_MSTR_MODE_EN}
    CKP = ${SPI_SPICON_CLK_POL}
    CKE = ${SPI_SPICON_CLK_PH}
    MODE<32,16> = ${SPI_SPICON_MODE}
    ENHBUF = 1
    MSSEN = ${SPI_SPICON_MSSEN}
    */
    ${SPI_INSTANCE_NAME}CONSET = (${SPI_INSTANCE_NAME}_CON_MSSEN | ${SPI_INSTANCE_NAME}_CON_ENHBUF | ${SPI_INSTANCE_NAME}_CON_MODE_32_MODE_16 | ${SPI_INSTANCE_NAME}_CON_CKE | ${SPI_INSTANCE_NAME}_CON_CKP | ${SPI_INSTANCE_NAME}_CON_MSTEN | ${SPI_INSTANCE_NAME}_CON_SMP);

    /* Enable transmit interrupt when transmit buffer is completely empty (STXISEL = '01') */
    /* Enable receive interrupt when the receive buffer is not empty (SRXISEL = '01') */
    ${SPI_INSTANCE_NAME}CONSET = 0x00000005;

<#if SPI_INTERRUPT_MODE == true>
    /* Initialize global variables */
    ${SPI_INSTANCE_NAME?lower_case}Obj.transferIsBusy = false;
    ${SPI_INSTANCE_NAME?lower_case}Obj.callback = NULL;
</#if>

    /* Enable ${SPI_INSTANCE_NAME} */
    ${SPI_INSTANCE_NAME}CONSET = _${SPI_INSTANCE_NAME}CON_ON_MASK;
}

bool ${SPI_INSTANCE_NAME}_TransferSetup (SPI_TRANSFER_SETUP* setup, uint32_t spiSourceClock )
{
<#assign spiClockSymbol = "core." + SPI_INSTANCE_NAME + "_CLOCK_FREQUENCY">
    uint32_t t_brg;
    uint32_t baudHigh;
    uint32_t baudLow;
    uint32_t errorHigh;
    uint32_t errorLow;

    if ((setup == NULL) || (setup->clockFrequency == 0U))
    {
        return false;
    }

    if(spiSourceClock == 0U)
    {
        // Use Master Clock Frequency set in GUI
        spiSourceClock = ${spiClockSymbol?eval};
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

    if(t_brg > ${SPI_MAX_BRG}U)
    {
        return false;
    }

    ${SPI_INSTANCE_NAME}BRG = t_brg;
    ${SPI_INSTANCE_NAME}CON = (${SPI_INSTANCE_NAME}CON & (~(_${SPI_INSTANCE_NAME}CON_MODE16_MASK | _${SPI_INSTANCE_NAME}CON_MODE32_MASK | _${SPI_INSTANCE_NAME}CON_CKP_MASK | _${SPI_INSTANCE_NAME}CON_CKE_MASK))) |
                            ((uint32_t)setup->clockPolarity | (uint32_t)setup->clockPhase | (uint32_t)setup->dataBits);

    return true;
}

bool ${SPI_INSTANCE_NAME}_Write(void* pTransmitData, size_t txSize)
{
    return(${SPI_INSTANCE_NAME}_WriteRead(pTransmitData, txSize, NULL, 0));
}

bool ${SPI_INSTANCE_NAME}_Read(void* pReceiveData, size_t rxSize)
{
    return(${SPI_INSTANCE_NAME}_WriteRead(NULL, 0, pReceiveData, rxSize));
}

bool ${SPI_INSTANCE_NAME}_IsTransmitterBusy (void)
{
    return ((${SPI_INSTANCE_NAME}STAT & _${SPI_INSTANCE_NAME}STAT_SRMT_MASK) == 0U)? true : false;
}

<#if SPI_INTERRUPT_MODE == false>
bool ${SPI_INSTANCE_NAME}_WriteRead(void* pTransmitData, size_t txSize, void* pReceiveData, size_t rxSize)
{
    size_t txCount = 0;
    size_t rxCount = 0;
    size_t dummySize = 0;
    size_t dummyRxCntr = 0;
    size_t receivedData;
    bool isSuccess = false;

    /* Verify the request */
    if (((txSize > 0U) && (pTransmitData != NULL)) || ((rxSize > 0U) && (pReceiveData != NULL)))
    {
        if (pTransmitData == NULL)
        {
            txSize = 0;
        }
        if (pReceiveData == NULL)
        {
            rxSize = 0;
        }

        /* Clear the receive overflow error if any */
        ${SPI_INSTANCE_NAME}STATCLR = _${SPI_INSTANCE_NAME}STAT_SPIROV_MASK;

        /* Flush out any unread data in SPI read buffer from the previous transfer */
        while ((${SPI_INSTANCE_NAME}STAT & _${SPI_INSTANCE_NAME}STAT_SPIRBE_MASK) == 0U)
        {
            (void)${SPI_INSTANCE_NAME}BUF;
        }

        if (rxSize > txSize)
        {
            dummySize = rxSize - txSize;
        }

        /* If dataBit size is 32 bits */
        if (_${SPI_INSTANCE_NAME}CON_MODE32_MASK == (${SPI_INSTANCE_NAME}CON & _${SPI_INSTANCE_NAME}CON_MODE32_MASK))
        {
            rxSize >>= 2;
            txSize >>= 2;
            dummySize >>= 2;
        }
        /* If dataBit size is 16 bits */
        else if (_${SPI_INSTANCE_NAME}CON_MODE16_MASK == (${SPI_INSTANCE_NAME}CON & _${SPI_INSTANCE_NAME}CON_MODE16_MASK))
        {
            rxSize >>= 1;
            txSize >>= 1;
            dummySize >>= 1;
        }
        else
        {
             /* Nothing to process */
        }

        while((${SPI_INSTANCE_NAME}STAT & _${SPI_INSTANCE_NAME}STAT_SPITBE_MASK) == 0U)
        {
            /* Wait for transmit buffer to be empty */
        }

        while ((txCount != txSize) || (dummySize != 0U))
        {
            if (txCount != txSize)
            {
                if((_${SPI_INSTANCE_NAME}CON_MODE32_MASK) == (${SPI_INSTANCE_NAME}CON & (_${SPI_INSTANCE_NAME}CON_MODE32_MASK)))
                {
                    ${SPI_INSTANCE_NAME}BUF = ((uint32_t*)pTransmitData)[txCount];
                }
                else if((_${SPI_INSTANCE_NAME}CON_MODE16_MASK) == (${SPI_INSTANCE_NAME}CON & (_${SPI_INSTANCE_NAME}CON_MODE16_MASK)))
                {
                    ${SPI_INSTANCE_NAME}BUF = ((uint16_t*)pTransmitData)[txCount];
                }
                else
                {
                    ${SPI_INSTANCE_NAME}BUF = ((uint8_t*)pTransmitData)[txCount];
                }
                txCount++;
            }
            else if (dummySize > 0U)
            {
                ${SPI_INSTANCE_NAME}BUF = 0x${SPI_DUMMY_DATA};
                dummySize--;
            }
            else
            {
                 /* Nothing to process */
            }

            if (rxCount == rxSize)
            {
                /* If inside this if condition, then it means that txSize > rxSize and all RX bytes are received */

                /* For transmit only request, wait for buffer to become empty */
                while((${SPI_INSTANCE_NAME}STAT & _${SPI_INSTANCE_NAME}STAT_SPITBE_MASK) == 0U)
                {
                    /* Wait for buffer empty */
                }

                /* Read until the receive buffer is not empty */
                while ((${SPI_INSTANCE_NAME}STAT & _${SPI_INSTANCE_NAME}STAT_SPIRBE_MASK) == 0U)
                {
                    (void)${SPI_INSTANCE_NAME}BUF;
                    dummyRxCntr++;
                }
            }
            else
            {
                /* If data is read, wait for the Receiver Data the data to become available */
                while((${SPI_INSTANCE_NAME}STAT & _${SPI_INSTANCE_NAME}STAT_SPIRBE_MASK) == _${SPI_INSTANCE_NAME}STAT_SPIRBE_MASK)
                {
                  /* Do Nothing */
                }

                /* We have data waiting in the SPI buffer */
                receivedData = ${SPI_INSTANCE_NAME}BUF;

                if (rxCount < rxSize)
                {
                    if((_${SPI_INSTANCE_NAME}CON_MODE32_MASK) == (${SPI_INSTANCE_NAME}CON & (_${SPI_INSTANCE_NAME}CON_MODE32_MASK)))
                    {
                        ((uint32_t*)pReceiveData)[rxCount]  = receivedData;
                        rxCount++;
                    }
                    else if((_${SPI_INSTANCE_NAME}CON_MODE16_MASK) == (${SPI_INSTANCE_NAME}CON & (_${SPI_INSTANCE_NAME}CON_MODE16_MASK)))
                    {
                        ((uint16_t*)pReceiveData)[rxCount]  = (uint16_t)receivedData;
                        rxCount++;
                    }
                    else
                    {
                        ((uint8_t*)pReceiveData)[rxCount]  = (uint8_t)receivedData;
                        rxCount++;
                    }
                }
            }
        }

        /* Make sure no data is pending in the shift register */
        while((${SPI_INSTANCE_NAME}STAT & _${SPI_INSTANCE_NAME}STAT_SRMT_MASK) == 0U)
        {
            /* Data pending in shift register */
        }

        /* Make sure for every character transmitted a character is also received back.
         * If this is not done, we may prematurely exit this routine with the last bit still being
         * transmitted out. As a result, the application may prematurely deselect the CS line and also
         * the next request can receive last character of previous request as its first character.
         */
        if (txSize > rxSize)
        {
            while (dummyRxCntr != (txSize - rxSize))
            {
                /* Wait for all the RX bytes to be received. */
                while ((bool)(${SPI_INSTANCE_NAME}STAT & _${SPI_INSTANCE_NAME}STAT_SPIRBE_MASK) == false)
                {
                    (void)${SPI_INSTANCE_NAME}BUF;
                    dummyRxCntr++;
                }
            }
        }
        isSuccess = true;
    }
    return isSuccess;
}
<#else>
bool ${SPI_INSTANCE_NAME}_WriteRead (void* pTransmitData, size_t txSize, void* pReceiveData, size_t rxSize)
{
    bool isRequestAccepted = false;

    /* Verify the request */
    if((${SPI_INSTANCE_NAME?lower_case}Obj.transferIsBusy == false) && (((txSize > 0U) && (pTransmitData != NULL)) || ((rxSize > 0U) && (pReceiveData != NULL))))
    {
        isRequestAccepted = true;
        ${SPI_INSTANCE_NAME?lower_case}Obj.txBuffer = pTransmitData;
        ${SPI_INSTANCE_NAME?lower_case}Obj.rxBuffer = pReceiveData;
        ${SPI_INSTANCE_NAME?lower_case}Obj.rxCount = 0;
        ${SPI_INSTANCE_NAME?lower_case}Obj.txCount = 0;
        ${SPI_INSTANCE_NAME?lower_case}Obj.dummySize = 0;

        if (pTransmitData != NULL)
        {
            ${SPI_INSTANCE_NAME?lower_case}Obj.txSize = txSize;
        }
        else
        {
            ${SPI_INSTANCE_NAME?lower_case}Obj.txSize = 0;
        }

        if (pReceiveData != NULL)
        {
            ${SPI_INSTANCE_NAME?lower_case}Obj.rxSize = rxSize;
        }
        else
        {
            ${SPI_INSTANCE_NAME?lower_case}Obj.rxSize = 0;
        }

        ${SPI_INSTANCE_NAME?lower_case}Obj.transferIsBusy = true;

        size_t txSz = ${SPI_INSTANCE_NAME?lower_case}Obj.txSize;
        if (${SPI_INSTANCE_NAME?lower_case}Obj.rxSize > txSz)
        {
            ${SPI_INSTANCE_NAME?lower_case}Obj.dummySize = ${SPI_INSTANCE_NAME?lower_case}Obj.rxSize - txSz;
        }

        /* Clear the receive overflow error if any */
        ${SPI_INSTANCE_NAME}STATCLR = _${SPI_INSTANCE_NAME}STAT_SPIROV_MASK;

        /* Make sure there is no data pending in the RX FIFO */
        /* Depending on 8/16/32 bit mode, there may be 16/8/4 bytes in the FIFO */
        while ((${SPI_INSTANCE_NAME}STAT & _${SPI_INSTANCE_NAME}STAT_SPIRBE_MASK) == 0U)
        {
            (void)${SPI_INSTANCE_NAME}BUF;
        }

        /* Configure SPI to generate receive interrupt when receive buffer is empty (SRXISEL = '01') */
        ${SPI_INSTANCE_NAME}CONCLR = _${SPI_INSTANCE_NAME}CON_SRXISEL_MASK;
        ${SPI_INSTANCE_NAME}CONSET = 0x00000001;

        /* Configure SPI to generate transmit interrupt when the transmit shift register is empty (STXISEL = '00')*/
        ${SPI_INSTANCE_NAME}CONCLR = _${SPI_INSTANCE_NAME}CON_STXISEL_MASK;

        /* Disable the receive interrupt */
        ${SPI_RX_IEC_REG}CLR = ${SPI_RX_IEC_REG_MASK};

        /* Disable the transmit interrupt */
        ${SPI_TX_IEC_REG}CLR = ${SPI_TX_IEC_REG_MASK};

        /* Clear the receive interrupt flag */
        ${SPI_RX_IFS_REG}CLR = ${SPI_RX_IFS_REG_MASK};

        /* Clear the transmit interrupt flag */
        ${SPI_TX_IFS_REG}CLR = ${SPI_TX_IFS_REG_MASK};

        /* Start the first write here itself, rest will happen in ISR context */
        if((_${SPI_INSTANCE_NAME}CON_MODE32_MASK) == (${SPI_INSTANCE_NAME}CON & (_${SPI_INSTANCE_NAME}CON_MODE32_MASK)))
        {
            ${SPI_INSTANCE_NAME?lower_case}Obj.txSize >>= 2;
            ${SPI_INSTANCE_NAME?lower_case}Obj.dummySize >>= 2;
            ${SPI_INSTANCE_NAME?lower_case}Obj.rxSize >>= 2;

            txSz = ${SPI_INSTANCE_NAME?lower_case}Obj.txSize;
            if(${SPI_INSTANCE_NAME?lower_case}Obj.txCount < txSz)
            {
                ${SPI_INSTANCE_NAME}BUF = *((uint32_t*)${SPI_INSTANCE_NAME?lower_case}Obj.txBuffer);
                ${SPI_INSTANCE_NAME?lower_case}Obj.txCount++;
            }
            else if (${SPI_INSTANCE_NAME?lower_case}Obj.dummySize > 0U)
            {
                ${SPI_INSTANCE_NAME}BUF = (uint32_t)(0x${SPI_DUMMY_DATA}U);
                ${SPI_INSTANCE_NAME?lower_case}Obj.dummySize--;
            }
            else
            {
                /* Nothing to process */
            }
        }
        else if((_${SPI_INSTANCE_NAME}CON_MODE16_MASK) == (${SPI_INSTANCE_NAME}CON & (_${SPI_INSTANCE_NAME}CON_MODE16_MASK)))
        {
            ${SPI_INSTANCE_NAME?lower_case}Obj.txSize >>= 1;
            ${SPI_INSTANCE_NAME?lower_case}Obj.dummySize >>= 1;
            ${SPI_INSTANCE_NAME?lower_case}Obj.rxSize >>= 1;

            txSz = ${SPI_INSTANCE_NAME?lower_case}Obj.txSize;
            if (${SPI_INSTANCE_NAME?lower_case}Obj.txCount < txSz)
            {
                ${SPI_INSTANCE_NAME}BUF = *((uint16_t*)${SPI_INSTANCE_NAME?lower_case}Obj.txBuffer);
                ${SPI_INSTANCE_NAME?lower_case}Obj.txCount++;
            }
            else if (${SPI_INSTANCE_NAME?lower_case}Obj.dummySize > 0U)
            {
                ${SPI_INSTANCE_NAME}BUF = (uint16_t)(0x${SPI_DUMMY_DATA}U);
                ${SPI_INSTANCE_NAME?lower_case}Obj.dummySize--;
            }
            else
            {
                /* Nothing to process */
            }
        }
        else
        {
            if (${SPI_INSTANCE_NAME?lower_case}Obj.txCount < txSz)
            {
                ${SPI_INSTANCE_NAME}BUF = *((uint8_t*)${SPI_INSTANCE_NAME?lower_case}Obj.txBuffer);
                ${SPI_INSTANCE_NAME?lower_case}Obj.txCount++;
            }
            else if (${SPI_INSTANCE_NAME?lower_case}Obj.dummySize > 0U)
            {
                ${SPI_INSTANCE_NAME}BUF = (uint8_t)(0x${SPI_DUMMY_DATA}U);
                ${SPI_INSTANCE_NAME?lower_case}Obj.dummySize--;
            }
            else
            {
                /* Nothing to process */
            }
        }

        if (rxSize > 0U)
        {
            /* Enable receive interrupt to complete the transfer in ISR context.
             * Keep the transmit interrupt disabled. Transmit interrupt will be
             * enabled later if txCount < txSize, when rxCount = rxSize.
             */
            ${SPI_RX_IEC_REG}SET = ${SPI_RX_IEC_REG_MASK};
        }
        else
        {
            if (${SPI_INSTANCE_NAME?lower_case}Obj.txCount != txSz)
            {
                /* Configure SPI to generate transmit buffer empty interrupt only if more than
                 * data is pending (STXISEL = '01')  */
                ${SPI_INSTANCE_NAME}CONSET = 0x00000004;
            }
            /* Enable transmit interrupt to complete the transfer in ISR context */
            ${SPI_TX_IEC_REG}SET = ${SPI_TX_IEC_REG_MASK};
        }
    }

    return isRequestAccepted;
}

bool ${SPI_INSTANCE_NAME}_IsBusy (void)
{
    bool transferIsBusy = ${SPI_INSTANCE_NAME?lower_case}Obj.transferIsBusy;

    return (((${SPI_INSTANCE_NAME}STAT & _${SPI_INSTANCE_NAME}STAT_SRMT_MASK) == 0) || (transferIsBusy));
}

void ${SPI_INSTANCE_NAME}_CallbackRegister (SPI_CALLBACK callback, uintptr_t context)
{
    ${SPI_INSTANCE_NAME?lower_case}Obj.callback = callback;

    ${SPI_INSTANCE_NAME?lower_case}Obj.context = context;
}

<#if SPI_INTERRUPT_COUNT == 1>
static void __attribute__((used)) ${SPI_INSTANCE_NAME}_RX_InterruptHandler (void)
<#else>
void __attribute__((used)) ${SPI_INSTANCE_NAME}_RX_InterruptHandler (void)
</#if>
{
    uint32_t receivedData = 0;

    /* Check if the receive buffer is empty or not */
    if ((${SPI_INSTANCE_NAME}STAT & _${SPI_INSTANCE_NAME}STAT_SPIRBE_MASK) == 0U)
    {
        /* Receive buffer is not empty. Read the received data. */
        receivedData = ${SPI_INSTANCE_NAME}BUF;

        size_t rxCount = ${SPI_INSTANCE_NAME?lower_case}Obj.rxCount;
        size_t txCount = ${SPI_INSTANCE_NAME?lower_case}Obj.txCount;

        if (rxCount < ${SPI_INSTANCE_NAME?lower_case}Obj.rxSize)
        {
            /* Copy the received data to the user buffer */
            if((_${SPI_INSTANCE_NAME}CON_MODE32_MASK) == (${SPI_INSTANCE_NAME}CON & (_${SPI_INSTANCE_NAME}CON_MODE32_MASK)))
            {
                ((uint32_t*)${SPI_INSTANCE_NAME?lower_case}Obj.rxBuffer)[rxCount] = receivedData;
                rxCount++;
            }
            else if((_${SPI_INSTANCE_NAME}CON_MODE16_MASK) == (${SPI_INSTANCE_NAME}CON & (_${SPI_INSTANCE_NAME}CON_MODE16_MASK)))
            {
                ((uint16_t*)${SPI_INSTANCE_NAME?lower_case}Obj.rxBuffer)[rxCount] = (uint16_t)receivedData;
                rxCount++;
            }
            else
            {
                ((uint8_t*)${SPI_INSTANCE_NAME?lower_case}Obj.rxBuffer)[rxCount] = (uint8_t)receivedData;
                rxCount++;
            }

            ${SPI_INSTANCE_NAME?lower_case}Obj.rxCount = rxCount;

            if (rxCount == ${SPI_INSTANCE_NAME?lower_case}Obj.rxSize)
            {
                if (txCount < ${SPI_INSTANCE_NAME?lower_case}Obj.txSize)
                {
                    /* Reception of all bytes is complete. However, there are few more
                     * bytes to be transmitted as txCount != txSize. Finish the
                     * transmission of the remaining bytes from the transmit interrupt. */

                    /* Disable the receive interrupt */
                    ${SPI_RX_IEC_REG}CLR = ${SPI_RX_IEC_REG_MASK};

                    /* Generate TX interrupt when buffer is completely empty (STXISEL = '00') */
                    ${SPI_INSTANCE_NAME}CONCLR = _${SPI_INSTANCE_NAME}CON_STXISEL_MASK;
                    ${SPI_INSTANCE_NAME}CONSET = 0x00000004;

                    /* Enable the transmit interrupt. Callback will be given from the
                     * transmit interrupt, when all bytes are shifted out. */
                    ${SPI_TX_IEC_REG}SET = ${SPI_TX_IEC_REG_MASK};
                }
            }
        }
        if (rxCount < ${SPI_INSTANCE_NAME?lower_case}Obj.rxSize)
        {
            /* More bytes pending to be received .. */
            if((_${SPI_INSTANCE_NAME}CON_MODE32_MASK) == (${SPI_INSTANCE_NAME}CON & (_${SPI_INSTANCE_NAME}CON_MODE32_MASK)))
            {
                if (txCount < ${SPI_INSTANCE_NAME?lower_case}Obj.txSize)
                {
                    ${SPI_INSTANCE_NAME}BUF = ((uint32_t*)${SPI_INSTANCE_NAME?lower_case}Obj.txBuffer)[txCount];
                    txCount++;
                }
                else if (${SPI_INSTANCE_NAME?lower_case}Obj.dummySize > 0U)
                {
                    ${SPI_INSTANCE_NAME}BUF = (uint32_t)(0x${SPI_DUMMY_DATA}U);
                    ${SPI_INSTANCE_NAME?lower_case}Obj.dummySize--;
                }
               else
                {
                   /* Do Nothing */
                }
            }
            else if((_${SPI_INSTANCE_NAME}CON_MODE16_MASK) == (${SPI_INSTANCE_NAME}CON & (_${SPI_INSTANCE_NAME}CON_MODE16_MASK)))
            {
                if (txCount < ${SPI_INSTANCE_NAME?lower_case}Obj.txSize)
                {
                    ${SPI_INSTANCE_NAME}BUF = ((uint16_t*)${SPI_INSTANCE_NAME?lower_case}Obj.txBuffer)[txCount];
                    txCount++;
                }
                else if (${SPI_INSTANCE_NAME?lower_case}Obj.dummySize > 0U)
                {
                    ${SPI_INSTANCE_NAME}BUF = (uint16_t)(0x${SPI_DUMMY_DATA}U);
                    ${SPI_INSTANCE_NAME?lower_case}Obj.dummySize--;
                }
               else
                {
                      /* Do Nothing */
                }
            }
            else
            {
                if (txCount < ${SPI_INSTANCE_NAME?lower_case}Obj.txSize)
                {
                    ${SPI_INSTANCE_NAME}BUF = ((uint8_t*)${SPI_INSTANCE_NAME?lower_case}Obj.txBuffer)[txCount];
                    txCount++;
                }
                else if (${SPI_INSTANCE_NAME?lower_case}Obj.dummySize > 0U)
                {
                    ${SPI_INSTANCE_NAME}BUF = (uint8_t)(0x${SPI_DUMMY_DATA}U);
                    ${SPI_INSTANCE_NAME?lower_case}Obj.dummySize--;
                }
               else
                {
                    /* Do Nothing */
                }
            }

            ${SPI_INSTANCE_NAME?lower_case}Obj.txCount = txCount;
        }
        else
        {
            if(rxCount == ${SPI_INSTANCE_NAME?lower_case}Obj.rxSize)
            {
                if (txCount == ${SPI_INSTANCE_NAME?lower_case}Obj.txSize)
                {
                    /* Clear receiver overflow error if any */
                    ${SPI_INSTANCE_NAME}STATCLR = _${SPI_INSTANCE_NAME}STAT_SPIROV_MASK;

                    /* Disable receive interrupt */
                    ${SPI_RX_IEC_REG}CLR = ${SPI_RX_IEC_REG_MASK};

                    /* Transfer complete. Give a callback */
                    ${SPI_INSTANCE_NAME?lower_case}Obj.transferIsBusy = false;

                    if(${SPI_INSTANCE_NAME?lower_case}Obj.callback != NULL)
                    {
                        uintptr_t context = ${SPI_INSTANCE_NAME?lower_case}Obj.context;

                        ${SPI_INSTANCE_NAME?lower_case}Obj.callback(context);
                    }
                }
            }
        }
    }

    /* Clear ${SPI_INSTANCE_NAME} RX Interrupt flag */
    /* This flag should cleared only after reading buffer */
    ${SPI_RX_IFS_REG}CLR = ${SPI_RX_IFS_REG_MASK};
}

<#if SPI_INTERRUPT_COUNT == 1>
static void __attribute__((used)) ${SPI_INSTANCE_NAME}_TX_InterruptHandler (void)
<#else>
void __attribute__((used)) ${SPI_INSTANCE_NAME}_TX_InterruptHandler (void)
</#if>
{
    /* If there are more words to be transmitted, then transmit them here and keep track of the count */
    if((${SPI_INSTANCE_NAME}STAT & _${SPI_INSTANCE_NAME}STAT_SPITBE_MASK) == _${SPI_INSTANCE_NAME}STAT_SPITBE_MASK)
    {
        size_t txCount = ${SPI_INSTANCE_NAME?lower_case}Obj.txCount;

        if (txCount < ${SPI_INSTANCE_NAME?lower_case}Obj.txSize)
        {
            if((_${SPI_INSTANCE_NAME}CON_MODE32_MASK) == (${SPI_INSTANCE_NAME}CON & (_${SPI_INSTANCE_NAME}CON_MODE32_MASK)))
            {
                ${SPI_INSTANCE_NAME}BUF = ((uint32_t*)${SPI_INSTANCE_NAME?lower_case}Obj.txBuffer)[txCount];
                txCount++;
            }
            else if((_${SPI_INSTANCE_NAME}CON_MODE16_MASK) == (${SPI_INSTANCE_NAME}CON & (_${SPI_INSTANCE_NAME}CON_MODE16_MASK)))
            {
                ${SPI_INSTANCE_NAME}BUF = ((uint16_t*)${SPI_INSTANCE_NAME?lower_case}Obj.txBuffer)[txCount];
                txCount++;
            }
            else
            {
                ${SPI_INSTANCE_NAME}BUF = ((uint8_t*)${SPI_INSTANCE_NAME?lower_case}Obj.txBuffer)[txCount];
                txCount++;
            }

            ${SPI_INSTANCE_NAME?lower_case}Obj.txCount = txCount;

            if (txCount == ${SPI_INSTANCE_NAME?lower_case}Obj.txSize)
            {
                /* All bytes are submitted to the SPI module. Now, enable transmit
                 * interrupt when the shift register is empty (STXISEL = '00')*/
                ${SPI_INSTANCE_NAME}CONCLR = _${SPI_INSTANCE_NAME}CON_STXISEL_MASK;
            }
        }
        else if (txCount == ${SPI_INSTANCE_NAME?lower_case}Obj.txSize)
        {
            if ((${SPI_INSTANCE_NAME}STAT & _${SPI_INSTANCE_NAME}STAT_SRMT_MASK) != 0U)
            {
                /* This part of code is executed when the shift register is empty. */

                /* Clear receiver overflow error if any */
                ${SPI_INSTANCE_NAME}STATCLR = _${SPI_INSTANCE_NAME}STAT_SPIROV_MASK;

                /* Disable transmit interrupt */
                ${SPI_TX_IEC_REG}CLR = ${SPI_TX_IEC_REG_MASK};

                /* Transfer complete. Give a callback */
                ${SPI_INSTANCE_NAME?lower_case}Obj.transferIsBusy = false;

                if(${SPI_INSTANCE_NAME?lower_case}Obj.callback != NULL)
                {
                    uintptr_t context = ${SPI_INSTANCE_NAME?lower_case}Obj.context;

                    ${SPI_INSTANCE_NAME?lower_case}Obj.callback(context);
                }
            }
        }
        else
        {
            /* Do Nothing */
        }
    }
    /* Clear the transmit interrupt flag */
    ${SPI_TX_IFS_REG}CLR = ${SPI_TX_IFS_REG_MASK};
}

<#if SPI_INTERRUPT_COUNT == 1>
void __attribute__((used)) SPI_${SPI_INSTANCE_NUM}_InterruptHandler (void)
{
    uint32_t iec_reg_read = ${SPI_RX_IEC_REG};
    if (((${SPI_RX_IFS_REG} & _${SPI_RX_IFS_REG}_${SPI_INSTANCE_NAME}RXIF_MASK) != 0U) && (( iec_reg_read & _${SPI_RX_IEC_REG}_${SPI_INSTANCE_NAME}RXIE_MASK)!= 0U))
    {
        /* RX interrupt is enabled and RX buffer is not empty */
        ${SPI_INSTANCE_NAME}_RX_InterruptHandler();
    }
    iec_reg_read = ${SPI_TX_IEC_REG};
    if (((${SPI_TX_IFS_REG} & _${SPI_TX_IFS_REG}_${SPI_INSTANCE_NAME}TXIF_MASK) != 0U) && ((iec_reg_read & _${SPI_TX_IEC_REG}_${SPI_INSTANCE_NAME}TXIE_MASK) != 0U))
    {
        /* TX interrupt is enabled and TX buffer is empty */
        ${SPI_INSTANCE_NAME}_TX_InterruptHandler();
    }
}
</#if>
</#if>