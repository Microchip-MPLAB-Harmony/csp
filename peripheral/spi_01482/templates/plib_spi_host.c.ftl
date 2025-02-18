<#assign modeOptions = ["CLIENT_MODE","HOST_MODE"]>
<#assign clkPolarityOptions = ["IDLE_LOW_ACTIVE_HIGH","IDLE_HIGH_ACTIVE_LOW"]>
<#assign clkEdgeOptions = ["IDLE_TO_ACTIVE","ACTIVE_TO_IDLE"]>
<#assign hostClkselOptions = ["UPB_CLOCK","CLOCK_GEN_"+clkSrcGenNumber]>
/*******************************************************************************
  SPI PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${SPI_INSTANCE_NAME?lower_case}_host.c

  Summary:
    ${SPI_INSTANCE_NAME} Host Source File

  Description:
    This file has implementation of all the interfaces provided for particular
    SPI peripheral.

*******************************************************************************/

/*******************************************************************************
* Copyright (C) 2024 Microchip Technology Inc. and its subsidiaries.
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

#include "plib_${SPI_INSTANCE_NAME?lower_case}_host.h"
<#if core.CoreSysIntFile == true>
#include "interrupts.h"
</#if>

<#if SPI_INTERRUPT_MODE == true>
/* Global object to save SPI Exchange related data */
volatile static SPI_OBJECT ${SPI_INSTANCE_NAME?lower_case}Obj;

void ${rxIsrHandlerName} (void);
void ${errorIsrHandlerName} (void);
void ${txIsrHandlerName} (void);
</#if>

// *****************************************************************************
// *****************************************************************************
// Section: Macro Definitions
// *****************************************************************************
// *****************************************************************************

//SPI SPIxCON1 MODE options
<#list modeOptions as options>
#define ${SPI_INSTANCE_NAME}CON1_MSTEN_${options}          ((uint32_t)(_${SPI_INSTANCE_NAME}CON1_MSTEN_MASK & ((uint32_t)(${options_index}) << _${SPI_INSTANCE_NAME}CON1_MSTEN_POSITION)))
</#list>

//SPI SPIxCON1 Clock Polarity options
<#list clkPolarityOptions as options>
#define ${SPI_INSTANCE_NAME}CON1_CKP_${options}           ((uint32_t)(_${SPI_INSTANCE_NAME}CON1_CKP_MASK & ((uint32_t)(${options_index}) << _${SPI_INSTANCE_NAME}CON1_CKP_POSITION)))
</#list>

//SPI SPIxCON1 Clock Edge options
<#list clkEdgeOptions as options>
#define ${SPI_INSTANCE_NAME}CON1_CKE_${options}           ((uint32_t)(_${SPI_INSTANCE_NAME}CON1_CKE_MASK & ((uint32_t)(${options_index}) << _${SPI_INSTANCE_NAME}CON1_CKE_POSITION)))
</#list>

//SPI SPIxCON1 Clock select options
<#list hostClkselOptions as options>
#define ${SPI_INSTANCE_NAME}CON1_MCLKEN_${options}           ((uint32_t)(_${SPI_INSTANCE_NAME}CON1_MCLKEN_MASK & ((uint32_t)(${options_index}) << _${SPI_INSTANCE_NAME}CON1_MCLKEN_POSITION)))
</#list>

/**
* @brief  Macro to define ${SPI_INSTANCE_NAME} FIFO Size available
*/
#define ${SPI_INSTANCE_NAME}_FIFO_SIZE               4U

/**
* @brief  Macro to define dummy data used for SPI transfer
*/
#define ${SPI_INSTANCE_NAME}_DUMMY_DATA              0x${SPI_DUMMY_DATA}UL


// *****************************************************************************
// *****************************************************************************
// Section: ${SPI_INSTANCE_NAME} Implementation
// *****************************************************************************
// *****************************************************************************

void ${SPI_INSTANCE_NAME}_Initialize ( void )
{
<#if SPI_INTERRUPT_MODE == true>
    /* Disable ${SPI_INSTANCE_NAME} Interrupts */
    ${errorInterruptEnableBit} = 0U;
    ${rxInterruptEnableBit} = 0U;
    ${txInterruptEnableBit} = 0U;

</#if>
    /* STOP and Reset the SPI */
    ${SPI_INSTANCE_NAME}CON1 = 0x00UL;

<#if SPI_INTERRUPT_MODE == true>
    /* Clear ${SPI_INSTANCE_NAME} Interrupt flags */
    ${errorInterruptFlagBit} = 0U;
    ${rxInterruptFlagBit} = 0U;
    ${txInterruptFlagBit} = 0U;

</#if>
    /* BAUD Rate register Setup */
    ${SPI_INSTANCE_NAME}BRG = 0x${SPI_BRG_VALUE}UL;

    ${SPI_INSTANCE_NAME}CON1 = (${SPI_INSTANCE_NAME}CON1_MSTEN_${modeOptions[SPI_CON1__MSTEN?number]}
            |${SPI_INSTANCE_NAME}CON1_CKP_${clkPolarityOptions[SPI_CON1__CKP?number]}
            |${SPI_INSTANCE_NAME}CON1_CKE_${clkEdgeOptions[SPI_CON1__CKE?number]}
            |${SPI_INSTANCE_NAME}CON1_MCLKEN_${hostClkselOptions[SPI_CON1__MCLKEN?number]}<#if SPI_CON1__SMP == "1">
            |_${SPI_INSTANCE_NAME}CON1_SMP_MASK</#if><#if SPI_CON1__ENHBUF == "1">
            |_${SPI_INSTANCE_NAME}CON1_ENHBUF_MASK</#if>);

<#if SPI_INTERRUPT_MODE == true>
    /* Initialize global variables */
    ${SPI_INSTANCE_NAME?lower_case}Obj.transferIsBusy = false;
    ${SPI_INSTANCE_NAME?lower_case}Obj.callback = NULL;

</#if>
    /* Enable ${SPI_INSTANCE_NAME} */
    ${SPI_INSTANCE_NAME}CON1bits.ON = 1U;
}

void ${SPI_INSTANCE_NAME}_Deinitialize ( void )
{
<#if SPI_INTERRUPT_MODE == true>
    /* Disable ${SPI_INSTANCE_NAME} Interrupts */
    ${errorInterruptEnableBit} = 0U;
    ${rxInterruptEnableBit} = 0U;
    ${txInterruptEnableBit} = 0U;
</#if>
    /* STOP the SPI */
    ${SPI_INSTANCE_NAME}CON1bits.ON = 0U;

<#if SPI_INTERRUPT_MODE == true>
    /* Clear ${SPI_INSTANCE_NAME} Interrupt flags */
    ${errorInterruptFlagBit} = 0U;
    ${rxInterruptFlagBit} = 0U;
    ${txInterruptFlagBit} = 0U;

</#if>

${regPorSet}


}

bool ${SPI_INSTANCE_NAME}_TransferSetup (SPI_TRANSFER_SETUP* setup, uint32_t spiSourceClock )
{
    uint32_t t_brg;
    uint32_t baudHigh;
    uint32_t baudLow;
    uint32_t errorHigh;
    uint32_t errorLow;

    if ((setup == NULL) || (setup->clockFrequency == 0U) || (setup->dataBits != SPI_DATA_BITS_8))
    {
        return false;
    }

    spiSourceClock =  ${SPI_INSTANCE_NAME}_FrequencyGet();

    t_brg = (((spiSourceClock / (setup->clockFrequency)) / 2u) - 1u);
    baudHigh = spiSourceClock / (2u * (t_brg + 1u));
    baudLow = spiSourceClock / (2u * (t_brg + 2u));
    errorHigh = baudHigh - setup->clockFrequency;
    errorLow = setup->clockFrequency - baudLow;

    if (errorHigh > errorLow)
    {
        t_brg++;
    }

    if(t_brg > 0x${SPI_MAX_BRG}UL)
    {
        return false;
    }

    /* STOP and Reset the SPI */
    ${SPI_INSTANCE_NAME}CON1bits.ON = 0U;

    ${SPI_INSTANCE_NAME}BRG = t_brg;

    ${SPI_INSTANCE_NAME}CON1 = (${SPI_INSTANCE_NAME}CON1 & (~(_${SPI_INSTANCE_NAME}CON1_MODE16_MASK | _${SPI_INSTANCE_NAME}CON1_MODE32_MASK | _${SPI_INSTANCE_NAME}CON1_CKP_MASK | _${SPI_INSTANCE_NAME}CON1_CKE_MASK))) |
                            ((uint32_t)setup->clockPolarity | (uint32_t)setup->clockPhase | (uint32_t)setup->dataBits);

    ${SPI_INSTANCE_NAME}CON1bits.ON = 1U;

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
    size_t txCount = 0U;
    size_t rxCount = 0U;
    size_t dummySize = 0U;
    size_t dummyRxCntr = 0U;
    bool isSuccess = false;

    /* Verify the request */
    if (((txSize > 0U) && (pTransmitData != NULL)) || ((rxSize > 0U) && (pReceiveData != NULL)))
    {
        if (pTransmitData == NULL)
        {
            txSize = 0U;
        }
        if (pReceiveData == NULL)
        {
            rxSize = 0U;
        }

        /* Clear receiver overflow error if any */
        ${SPI_INSTANCE_NAME}STATbits.SPIROV = 0U;

        /* Flush out any unread data in SPI read buffer from the previous transfer */
        while ((${SPI_INSTANCE_NAME}STAT & _${SPI_INSTANCE_NAME}STAT_SPIRBE_MASK) == 0U)
        {
            (void)${SPI_INSTANCE_NAME}BUF;
        }

        if (rxSize > txSize)
        {
            dummySize = rxSize - txSize;
        }

        while ((txCount < txSize) || (dummySize != 0U))
        {
            if (txCount < txSize && ${SPI_INSTANCE_NAME}STATbits.SPITBF == 0U)
            {
                ${SPI_INSTANCE_NAME}BUF = ((uint8_t*)pTransmitData)[txCount];
                txCount++;
            }
            else if (dummySize > 0U && ${SPI_INSTANCE_NAME}STATbits.SPITBF == 0U)
            {
                ${SPI_INSTANCE_NAME}BUF = ${SPI_INSTANCE_NAME}_DUMMY_DATA;
                dummySize--;
            }
            else
            {
                 /* Nothing to process */
            }

            if (rxSize == 0U)
            {
                /* Read until the receive buffer is not empty */
                if ((${SPI_INSTANCE_NAME}STAT & _${SPI_INSTANCE_NAME}STAT_SPIRBE_MASK) == 0U)
                {
                    (void)${SPI_INSTANCE_NAME}BUF;
                    dummyRxCntr++;
                }
            }
            else
            {
                /* If data is read, wait for the Receiver Data the data to become available */
                if (${SPI_INSTANCE_NAME}STATbits.SPIRBE == false)
                {
                    if (rxCount < rxSize)
                    {
                        /* We have data waiting in the SPI buffer */
                        ((uint8_t*)pReceiveData)[rxCount]  = ${SPI_INSTANCE_NAME}BUF;
                        rxCount++;
                    }
                }
            }
        }

        while(rxCount < rxSize)
        {
            if (${SPI_INSTANCE_NAME}STATbits.SPIRBE == false)
            {
                ((uint8_t*)pReceiveData)[rxCount]  = ${SPI_INSTANCE_NAME}BUF;
                rxCount++;
            }
        }

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

        /* Make sure no data is pending in the shift register */
        while((${SPI_INSTANCE_NAME}STAT & _${SPI_INSTANCE_NAME}STAT_SRMT_MASK) == 0U)
        {
            /* Data pending in shift register */
        }
        isSuccess = true;
    }
    return isSuccess;
}
<#else>

bool ${SPI_INSTANCE_NAME}_IsBusy (void)
{
    uint32_t StatRead = ${SPI_INSTANCE_NAME}STAT;
    return (((${SPI_INSTANCE_NAME?lower_case}Obj.transferIsBusy) != false) || (( StatRead & _${SPI_INSTANCE_NAME}STAT_SRMT_MASK) == 0U));
}

void ${SPI_INSTANCE_NAME}_CallbackRegister (SPI_CALLBACK callback, uintptr_t context)
{
    ${SPI_INSTANCE_NAME?lower_case}Obj.callback = callback;

    ${SPI_INSTANCE_NAME?lower_case}Obj.context = context;
}

static void SPI_FIFO_Fill(void)
{
    uint8_t nDataCopiedToFIFO = 0U;

    while ((nDataCopiedToFIFO < ${SPI_INSTANCE_NAME}_FIFO_SIZE) && (${SPI_INSTANCE_NAME}STATbits.SPITBF == 0U))
    {
        if (${SPI_INSTANCE_NAME?lower_case}Obj.txCount < ${SPI_INSTANCE_NAME?lower_case}Obj.txSize)
        {
            ${SPI_INSTANCE_NAME}BUF = ((uint8_t*)${SPI_INSTANCE_NAME?lower_case}Obj.txBuffer)[${SPI_INSTANCE_NAME?lower_case}Obj.txCount];
            ${SPI_INSTANCE_NAME?lower_case}Obj.txCount++;
        }
        else if (${SPI_INSTANCE_NAME?lower_case}Obj.dummySize > 0U)
        {
            ${SPI_INSTANCE_NAME}BUF = ${SPI_INSTANCE_NAME}_DUMMY_DATA;
            ${SPI_INSTANCE_NAME?lower_case}Obj.dummySize--;
        }
        else
        {
            break;
        }
        nDataCopiedToFIFO++;
    }
}

bool ${SPI_INSTANCE_NAME}_WriteRead (void* pTransmitData, size_t txSize, void* pReceiveData, size_t rxSize)
{
    bool isRequestAccepted = false;

    /* Verify the request */
    if((${SPI_INSTANCE_NAME?lower_case}Obj.transferIsBusy == false) && (((txSize > 0U) && (pTransmitData != NULL)) || ((rxSize > 0U) && (pReceiveData != NULL))))
    {
        isRequestAccepted = true;
        ${SPI_INSTANCE_NAME?lower_case}Obj.txBuffer = pTransmitData;
        ${SPI_INSTANCE_NAME?lower_case}Obj.rxBuffer = pReceiveData;
        ${SPI_INSTANCE_NAME?lower_case}Obj.rxCount = 0U;
        ${SPI_INSTANCE_NAME?lower_case}Obj.txCount = 0U;
        ${SPI_INSTANCE_NAME?lower_case}Obj.dummySize = 0U;

        if (pTransmitData != NULL)
        {
            ${SPI_INSTANCE_NAME?lower_case}Obj.txSize = txSize;
        }
        else
        {
            ${SPI_INSTANCE_NAME?lower_case}Obj.txSize = 0U;
        }

        if (pReceiveData != NULL)
        {
            ${SPI_INSTANCE_NAME?lower_case}Obj.rxSize = rxSize;
        }
        else
        {
            ${SPI_INSTANCE_NAME?lower_case}Obj.rxSize = 0U;
        }

        ${SPI_INSTANCE_NAME?lower_case}Obj.transferIsBusy = true;

        size_t txSz = ${SPI_INSTANCE_NAME?lower_case}Obj.txSize;
        if (${SPI_INSTANCE_NAME?lower_case}Obj.rxSize > txSz)
        {
            ${SPI_INSTANCE_NAME?lower_case}Obj.dummySize = ${SPI_INSTANCE_NAME?lower_case}Obj.rxSize - txSz;
        }

        /* Clear the receive overflow error if any */
        ${SPI_INSTANCE_NAME}STATbits.SPIROV = 0U;

        /* Make sure there is no data pending in the RX FIFO */

        while ((${SPI_INSTANCE_NAME}STAT & _${SPI_INSTANCE_NAME}STAT_SPIRBE_MASK) == 0U)
        {
            (void)${SPI_INSTANCE_NAME}BUF;
        }
        /* Configure SPI to generate receive interrupt when receive buffer is empty */
        ${SPI_INSTANCE_NAME}IMSKbits.RXMSK = 1U;
        ${SPI_INSTANCE_NAME}IMSKbits.RXWIEN = 1U;

        /* Configure SPI to generate transmit interrupt when the transmit buffer is empty*/
        ${SPI_INSTANCE_NAME}IMSKbits.SPITBEN = 1U;

        /* Disable the receive interrupt */
        ${rxInterruptEnableBit} = 0U;

        /* Disable the transmit interrupt */
        ${txInterruptEnableBit} = 0U;

        /* Disable the error interrupt */
        ${errorInterruptEnableBit} = 0U;

        /* Clear the receive interrupt flag */
        ${rxInterruptFlagBit} = 0U;

        /* Clear the transmit interrupt flag */
        ${txInterruptFlagBit} = 0U;

        /* Clear the error interrupt flag */
        ${errorInterruptFlagBit} = 0U;

        /* Start the first write here itself, rest will happen in ISR context */
        SPI_FIFO_Fill();

        if (rxSize > 0U)
        {
            if(rxSize < ${SPI_INSTANCE_NAME}_FIFO_SIZE)
            {
                ${SPI_INSTANCE_NAME}IMSKbits.RXMSK = rxSize;
            }
            else
            {
                ${SPI_INSTANCE_NAME}IMSKbits.RXMSK = ${SPI_INSTANCE_NAME}_FIFO_SIZE;
            }
            /* Enable receive interrupt to complete the transfer in ISR context.
             * Keep the transmit interrupt disabled. Transmit interrupt will be
             * enabled later if txCount < txSize, when rxCount = rxSize.
             */
            ${rxInterruptEnableBit} = 1U;
        }
        else
        {
            if (${SPI_INSTANCE_NAME?lower_case}Obj.txCount != txSz)
            {
                /* Configure SPI to generate interrupt when transmit buffer is completely empty */
                ${SPI_INSTANCE_NAME}IMSKbits.SPITBEN = 1U;

                /* ignore receive overflow for transmit only operation*/
                ${SPI_INSTANCE_NAME}CON1bits.IGNROV = 1U;

                /* Enable transmit interrupt to complete the transfer in ISR context */
                ${txInterruptEnableBit} = 1U;

            }
            else
            {
                /* Enable error interrupt for SRMT(last byte transfer in shift register)*/
                ${SPI_INSTANCE_NAME}IMSKbits.SRMTEN = 1U;
                ${errorInterruptEnableBit} = 1U;
            }

        }
    }

    return isRequestAccepted;
}

void __attribute__((used)) ${rxIsrHandlerName} (void)
{
    uint32_t nRxPending;

    /* Check Receive Buffer Element Count for watermark interrupt */
    if ((${SPI_INSTANCE_NAME}STAT & _${SPI_INSTANCE_NAME}STAT_RXELM_MASK) != 0U)
    {
        size_t txCount = ${SPI_INSTANCE_NAME?lower_case}Obj.txCount;
        size_t rxCount = ${SPI_INSTANCE_NAME?lower_case}Obj.rxCount;
        while(${SPI_INSTANCE_NAME}STATbits.SPIRBE == false)
        {
            if (rxCount < ${SPI_INSTANCE_NAME?lower_case}Obj.rxSize)
            {
                /* Receive buffer is not empty. Read the received data. */
                ((uint8_t*)${SPI_INSTANCE_NAME?lower_case}Obj.rxBuffer)[rxCount] = ${SPI_INSTANCE_NAME}BUF;
                rxCount++;

                ${SPI_INSTANCE_NAME?lower_case}Obj.rxCount = rxCount;

                if (rxCount == ${SPI_INSTANCE_NAME?lower_case}Obj.rxSize)
                {
                    if (txCount < ${SPI_INSTANCE_NAME?lower_case}Obj.txSize)
                    {
                        /* Reception of all bytes is complete. However, there are few more
                         * bytes to be transmitted as txCount != txSize. Finish the
                         * transmission of the remaining bytes from the transmit interrupt. */

                        /* Disable the receive interrupt */
                        ${rxInterruptEnableBit} = 0U;

                        /* Generate TX interrupt when buffer is completely empty */
                        ${SPI_INSTANCE_NAME}IMSKbits.SPITBEN = 1U;

                        /* Enable the transmit interrupt. Callback will be given from the
                         * transmit interrupt, when all bytes are shifted out. */
                        ${txInterruptEnableBit} = 1U;
                    }
                }
            }
        }
        if (rxCount < ${SPI_INSTANCE_NAME?lower_case}Obj.rxSize)
        {
            /* More bytes pending to be received .. */
            SPI_FIFO_Fill();

            nRxPending = ${SPI_INSTANCE_NAME?lower_case}Obj.rxSize - rxCount;

            if(nRxPending <= ${SPI_INSTANCE_NAME}_FIFO_SIZE)
            {
                ${SPI_INSTANCE_NAME}IMSKbits.RXMSK = nRxPending;
            }
            else
            {
                ${SPI_INSTANCE_NAME}IMSKbits.RXMSK = ${SPI_INSTANCE_NAME}_FIFO_SIZE;
            }
        }
        else
        {
            if(rxCount == ${SPI_INSTANCE_NAME?lower_case}Obj.rxSize)
            {
                if (txCount == ${SPI_INSTANCE_NAME?lower_case}Obj.txSize)
                {
                    /* Clear receiver overflow error if any */
                    ${SPI_INSTANCE_NAME}STATbits.SPIROV = 0U;

                    /* Disable receive interrupt */
                    ${rxInterruptEnableBit} = 0U;

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
    ${rxInterruptFlagBit} = 0U;
}

void __attribute__((used)) ${errorIsrHandlerName}(void)
{
    size_t txCount = ${SPI_INSTANCE_NAME?lower_case}Obj.txCount;
    if (txCount == ${SPI_INSTANCE_NAME?lower_case}Obj.txSize)
    {
        if ((${SPI_INSTANCE_NAME}STAT & _${SPI_INSTANCE_NAME}STAT_SRMT_MASK) != 0U)
        {
            /* Clear receiver overflow error if any */
            ${SPI_INSTANCE_NAME}STATbits.SPIROV = 0U;

            /* Disable transmit interrupt */
            ${txInterruptEnableBit} = 0U;

            /* Transfer complete. Give a callback */
            ${SPI_INSTANCE_NAME?lower_case}Obj.transferIsBusy = false;

            if(${SPI_INSTANCE_NAME?lower_case}Obj.callback != NULL)
            {
                uintptr_t context = ${SPI_INSTANCE_NAME?lower_case}Obj.context;
                ${SPI_INSTANCE_NAME?lower_case}Obj.callback(context);
            }
        }
    }

    ${errorInterruptFlagBit} = 0U;
}

void __attribute__((used)) ${txIsrHandlerName} (void)
{
    /* If there are more words to be transmitted, then transmit them here and keep track of the count */
    if((${SPI_INSTANCE_NAME}STAT & _${SPI_INSTANCE_NAME}STAT_SPITBE_MASK) == _${SPI_INSTANCE_NAME}STAT_SPITBE_MASK)
    {
        size_t txCount = ${SPI_INSTANCE_NAME?lower_case}Obj.txCount;

        while ((txCount < ${SPI_INSTANCE_NAME?lower_case}Obj.txSize) && (!${SPI_INSTANCE_NAME}STATbits.SPITBF))
        {
            ${SPI_INSTANCE_NAME}BUF = ((uint8_t*)${SPI_INSTANCE_NAME?lower_case}Obj.txBuffer)[txCount];
            txCount++;

            ${SPI_INSTANCE_NAME?lower_case}Obj.txCount = txCount;
            if (txCount == ${SPI_INSTANCE_NAME?lower_case}Obj.txSize)
            {
                /* All bytes are submitted to the SPI module. Now, enable transmit
                 * interrupt for the shift register to empty  */
                ${SPI_INSTANCE_NAME}IMSKbits.SPITBEN = 0U;
                ${SPI_INSTANCE_NAME}IMSKbits.SRMTEN = 1U;

                /* Enable the error interrupt and disable the transmit interrupt*/
                ${errorInterruptEnableBit} = 1U;
                ${txInterruptEnableBit} = 0U;
            }

        }
    }
    /* Clear the transmit interrupt flag */
    ${txInterruptFlagBit} = 0U;
}

</#if>