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
* Copyright (C) 2021 Microchip Technology Inc. and its subsidiaries.
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

<#assign QSPI_SCR_VALUES = "">
<#if QSPI_CPOL=="HIGH">
    <#if QSPI_SCR_VALUES != "">
        <#assign QSPI_SCR_VALUES = QSPI_SCR_VALUES + " | " + "QSPI_SCR_CPOL_Msk">
    <#else>
        <#assign QSPI_SCR_VALUES = "QSPI_SCR_CPOL_Msk">
    </#if>
</#if>
<#if QSPI_CPHA=="TRAILING">
    <#if QSPI_SCR_VALUES != "">
        <#assign QSPI_SCR_VALUES = QSPI_SCR_VALUES + " | " + "QSPI_SCR_CPHA_Msk">
    <#else>
        <#assign QSPI_SCR_VALUES = "QSPI_SCR_CPHA_Msk">
    </#if>
</#if>

void ${QSPI_INSTANCE_NAME}_Initialize(void)
{
    // Reset and Disable the qspi Module
    ${QSPI_INSTANCE_NAME}_REGS->QSPI_CR = QSPI_CR_SWRST_Msk | QSPI_CR_QSPIDIS_Msk;

    while((${QSPI_INSTANCE_NAME}_REGS->QSPI_SR & QSPI_SR_QSPIENS_Msk) != 0U)
    {
        /* Do Nothing */
    }

<#if QSPI_PCALCFG_CLKDIV??>
    // Pad Calibration Configuration
    ${QSPI_INSTANCE_NAME}_REGS->QSPI_PCALCFG = (${QSPI_INSTANCE_NAME}_REGS->QSPI_PCALCFG & ~QSPI_PCALCFG_CLKDIV_Msk) |
                                                QSPI_PCALCFG_CLKDIV(${QSPI_PCALCFG_CLKDIV}U);

<#if QSPI_CR_DLLON??>
    <#if QSPI_DLLCFG_RANGE>
    /* DLL Range */
    ${QSPI_INSTANCE_NAME}_REGS->QSPI_DLLCFG = QSPI_DLLCFG_RANGE_Msk;
    </#if>

    /* Enable DLL */
    ${QSPI_INSTANCE_NAME}_REGS->QSPI_CR = QSPI_CR_DLLON_Msk;
</#if>
    /* Start Pad Calibration */
    ${QSPI_INSTANCE_NAME}_REGS->QSPI_CR = QSPI_CR_STPCAL_Msk;

<#if QSPI_CR_DLLON??>
    /* Wait for DLL lock */
    while((${QSPI_INSTANCE_NAME}_REGS->QSPI_SR & QSPI_SR_DLOCK_Msk) == 0U)
    {
        /* Do Nothing */
    }

</#if>
    /* Wait for Pad Calibration complete */
    while((${QSPI_INSTANCE_NAME}_REGS->QSPI_SR & QSPI_SR_CALBSY_Msk) != 0U)
    {
        /* Do Nothing */
    }
</#if>

    /* DLYCS  = 0x0 */
    /* DLYBCT = 0x0 */
    <#if (QSPI_NBBITS?has_content)>
    /* NBBITS = ${QSPI_NBBITS} */
    <#else>
    /* NBBITS = 0x0 */
    </#if>
    /* CSMODE = 0x0 */
    /* WDRBT  = 0 */
    /* SMM    = ${QSPI_SMM} */
    <#if (QSPI_NBBITS?has_content)>
    ${QSPI_INSTANCE_NAME}_REGS->QSPI_MR = ( QSPI_MR_SMM_${QSPI_SMM} | QSPI_MR_NBBITS(${QSPI_NBBITS}U) );
    <#else>
    ${QSPI_INSTANCE_NAME}_REGS->QSPI_MR = ( QSPI_MR_SMM_${QSPI_SMM} );
    </#if>

    <#if (QSPI_SCR_VALUES?has_content)>
    /* CPOL = <#if QSPI_CPOL=="HIGH">1 <#else>0 </#if>*/
    /* CPHA = <#if QSPI_CPHA=="TRAILING">1 <#else>0 </#if>*/
    /* DLYBS = 0 */
    ${QSPI_INSTANCE_NAME}_REGS->QSPI_SCR = ${QSPI_SCR_VALUES};
    </#if>

    /* Wait for synchronization Busy */
    while((${QSPI_INSTANCE_NAME}_REGS->QSPI_SR & QSPI_SR_SYNCBSY_Msk) != 0U)
    {
        /* Do Nothing */
    }

    /* Update Configuration */
    ${QSPI_INSTANCE_NAME}_REGS->QSPI_CR = QSPI_CR_UPDCFG_Msk;

    /* Wait for synchronization Busy */
    while((${QSPI_INSTANCE_NAME}_REGS->QSPI_SR & QSPI_SR_SYNCBSY_Msk) != 0U)
    {
        /* Do Nothing */
    }

    // Enable the qspi Module
    ${QSPI_INSTANCE_NAME}_REGS->QSPI_CR = QSPI_CR_QSPIEN_Msk;

    while((${QSPI_INSTANCE_NAME}_REGS->QSPI_SR & QSPI_SR_QSPIENS_Msk) == 0U)
    {
        /* Do Nothing */
    }
}

bool ${QSPI_INSTANCE_NAME}_WriteRead (void* pTransmitData, size_t txSize, void* pReceiveData, size_t rxSize)
{
    bool isRequestAccepted = false;

    /* Verify the request */
    if((qspiObj.transferIsBusy == false) && (((txSize > 0U) && (pTransmitData != NULL)) || ((rxSize > 0U) && (pReceiveData != NULL))))
    {
        isRequestAccepted = true;
        qspiObj.transferIsBusy = true;
        qspiObj.txBuffer = pTransmitData;
        qspiObj.rxBuffer = pReceiveData;
        qspiObj.rxCount = 0;
        qspiObj.txCount = 0;
        if(pTransmitData == NULL)
        {
            txSize = 0U;
        }
        if(pReceiveData == NULL)
        {
            rxSize = 0U;
        }
        if (rxSize > txSize)
        {
            qspiObj.dummySize = rxSize - txSize;
        }
        else
        {
            qspiObj.dummySize = 0U;
        }
        /* Flush out any unread data in SPI read buffer */
        (void)${QSPI_INSTANCE_NAME}_REGS->QSPI_RDR;

        /* Start the first write here itself, rest will happen in ISR context */
        if((${QSPI_INSTANCE_NAME}_REGS->QSPI_MR & QSPI_MR_NBBITS_Msk) == QSPI_MR_NBBITS_8_BIT)
        {
            if(qspiObj.txCount < txSize)
            {
                ${QSPI_INSTANCE_NAME}_REGS->QSPI_TDR = *((uint8_t*)qspiObj.txBuffer);
                qspiObj.txCount++;
            }
            else if(qspiObj.dummySize > 0U)
            {
                ${QSPI_INSTANCE_NAME}_REGS->QSPI_TDR = 0xFFU;
                qspiObj.dummySize--;
            }
            else
            {
                /* Do Nothing */
            }
        }
        else if((${QSPI_INSTANCE_NAME}_REGS->QSPI_MR & QSPI_MR_NBBITS_Msk) == QSPI_MR_NBBITS_16_BIT)
        {
            /* divide by 2 since dealing with 2-byte quantities here */
            txSize >>= 1;
            qspiObj.dummySize >>= 1;
            rxSize >>= 1;

            if (qspiObj.txCount < txSize)
            {
                ${QSPI_INSTANCE_NAME}_REGS->QSPI_TDR = *((uint16_t*)qspiObj.txBuffer);
                qspiObj.txCount++;
            }
            else if (qspiObj.dummySize > 0U)
            {
                ${QSPI_INSTANCE_NAME}_REGS->QSPI_TDR = 0xFFU;
                qspiObj.dummySize--;
            }
            else
            {
                /* Do Nothing */
            }
        }
        else
        {
            /* Do Nothing */
        }

        qspiObj.rxSize = rxSize;
        qspiObj.txSize = txSize;

        if (rxSize > 0U)
        {
            /* Enable receive interrupt to complete the transfer in ISR context */
            ${QSPI_INSTANCE_NAME}_REGS->QSPI_IER = QSPI_IER_RDRF_Msk;
        }
        else
        {
            /* Enable transmit interrupt to complete the transfer in ISR context */
            ${QSPI_INSTANCE_NAME}_REGS->QSPI_IER = QSPI_IER_TDRE_Msk;
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

bool ${QSPI_INSTANCE_NAME}_TransferSetup (QSPI_TRANSFER_SETUP * setup )
{
    bool transfercheck = false;
    if (setup != NULL)
    {
        ${QSPI_INSTANCE_NAME}_REGS->QSPI_SCR= (uint32_t)setup->clockPolarity | (uint32_t)setup->clockPhase;

        ${QSPI_INSTANCE_NAME}_REGS->QSPI_MR = (${QSPI_INSTANCE_NAME}_REGS->QSPI_MR & ~QSPI_MR_NBBITS_Msk) | (uint32_t)setup->dataBits;

        transfercheck = true;
    }
    return transfercheck;
}

void ${QSPI_INSTANCE_NAME}_CallbackRegister (QSPI_CALLBACK callback, uintptr_t context)
{
    qspiObj.callback = callback;
    qspiObj.context = context;
}

bool ${QSPI_INSTANCE_NAME}_IsBusy(void)
{
    return ((qspiObj.transferIsBusy) || ((${QSPI_INSTANCE_NAME}_REGS->QSPI_ISR & QSPI_ISR_TXEMPTY_Msk ) == 0U));
}

bool ${QSPI_INSTANCE_NAME}_IsTransmitterBusy(void)
{
    return ((${QSPI_INSTANCE_NAME}_REGS->QSPI_ISR & QSPI_ISR_TXEMPTY_Msk) == 0U)? true : false;
}

void __attribute__((used)) ${QSPI_INSTANCE_NAME}_InterruptHandler(void)
{
    uint32_t dataBits ;
    uint32_t receivedData;
    static bool isLastByteTransferInProgress = false;

    /* Additional temporary variables used to prevent MISRA violations (Rule 13.x) */
    uintptr_t context = qspiObj.context;
    uint32_t rxSize = qspiObj.rxSize;
    uint32_t txSize = qspiObj.txSize;

    dataBits = ${QSPI_INSTANCE_NAME}_REGS->QSPI_MR & QSPI_MR_NBBITS_Msk;

    /* See if there's received data (MOSI) to be processed */
    if ((${QSPI_INSTANCE_NAME}_REGS->QSPI_ISR & QSPI_ISR_RDRF_Msk ) == QSPI_ISR_RDRF_Msk)
    {
        receivedData = (${QSPI_INSTANCE_NAME}_REGS->QSPI_RDR & QSPI_RDR_RD_Msk) >> QSPI_RDR_RD_Pos;

        if (qspiObj.rxCount < rxSize)
        {
            if(dataBits == QSPI_MR_NBBITS_8_BIT)
            {
                uint8_t* rxBuffer = (uint8_t*)qspiObj.rxBuffer;
                rxBuffer[qspiObj.rxCount] = (uint8_t)receivedData;
            }
            else
            {
                uint16_t* rxBuffer = (uint16_t*)qspiObj.rxBuffer;
                rxBuffer[qspiObj.rxCount] = (uint16_t)receivedData;
            }
            qspiObj.rxCount++;
        }
    }

    /* If there are more words to be transmitted, then transmit them here and keep track of the count */
    if((${QSPI_INSTANCE_NAME}_REGS->QSPI_ISR & QSPI_ISR_TDRE_Msk) == QSPI_ISR_TDRE_Msk)
    {
        /* Disable the TDRE interrupt. This will be enabled back if more than
         * one byte is pending to be transmitted */
        ${QSPI_INSTANCE_NAME}_REGS->QSPI_IDR = QSPI_IDR_TDRE_Msk;

        if(dataBits == QSPI_MR_NBBITS_8_BIT)
        {
            if (qspiObj.txCount < txSize)
            {
                uint8_t* txBuffer = (uint8_t*)qspiObj.txBuffer;
                ${QSPI_INSTANCE_NAME}_REGS->QSPI_TDR = txBuffer[qspiObj.txCount];
                qspiObj.txCount++;
            }
            else if (qspiObj.dummySize > 0U)
            {
                ${QSPI_INSTANCE_NAME}_REGS->QSPI_TDR = 0xFFU;
                qspiObj.dummySize--;
            }
            else
            {
                /* Do Nothing */
            }
        }
        else
        {
            if (qspiObj.txCount < txSize)
            {
                uint16_t* txBuffer = (uint16_t*)qspiObj.txBuffer;
                ${QSPI_INSTANCE_NAME}_REGS->QSPI_TDR = txBuffer[qspiObj.txCount];
                qspiObj.txCount++;
            }
            else if (qspiObj.dummySize > 0U)
            {
                ${QSPI_INSTANCE_NAME}_REGS->QSPI_TDR = 0xFFU;
                qspiObj.dummySize--;
            }
            else
            {
                /* Do Nothing */
            }
        }
        /* Additional temporary variable used to prevent MISRA violations (Rule 13.x) */
        bool dummyTxComplete = (qspiObj.dummySize == 0U);
        if ((qspiObj.txCount == txSize) && dummyTxComplete)
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
            ${QSPI_INSTANCE_NAME}_REGS->QSPI_CR = QSPI_CR_LASTXFER_Msk;
        }
        else if (qspiObj.rxCount == rxSize)
        {
            /* Enable TDRE interrupt as all the requested bytes are received
             * and can now make use of the internal transmit shift register.
             */
            ${QSPI_INSTANCE_NAME}_REGS->QSPI_IDR = QSPI_IDR_RDRF_Msk;
            ${QSPI_INSTANCE_NAME}_REGS->QSPI_IER = QSPI_IER_TDRE_Msk;
        }
        else
        {
            /* Do Nothing */
        }
    }

    /* See if Exchange is complete */
    /* Additional temporary variable used to prevent MISRA violations (Rule 13.x) */
    bool txEmptySet = ((${QSPI_INSTANCE_NAME}_REGS->QSPI_ISR & QSPI_ISR_TXEMPTY_Msk) == QSPI_ISR_TXEMPTY_Msk);
    if (isLastByteTransferInProgress && txEmptySet)
    {
        if (qspiObj.rxCount == rxSize)
        {
            qspiObj.transferIsBusy = false;

            /* Disable TDRE, RDRF and TXEMPTY interrupts */
            ${QSPI_INSTANCE_NAME}_REGS->QSPI_IDR = QSPI_IDR_TDRE_Msk | QSPI_IDR_RDRF_Msk | QSPI_IDR_TXEMPTY_Msk;

            isLastByteTransferInProgress = false;

            if(qspiObj.callback != NULL)
            {
                qspiObj.callback(context);
            }
        }
    }
    if (isLastByteTransferInProgress)
    {
        /* For the last byte transfer, the TDRE interrupt is already disabled.
         * Enable TXEMPTY interrupt to ensure no data is present in the shift
         * register before application callback is called.
         */
        ${QSPI_INSTANCE_NAME}_REGS->QSPI_IER = QSPI_IER_TXEMPTY_Msk;
    }

}
/*******************************************************************************
 End of File
*/