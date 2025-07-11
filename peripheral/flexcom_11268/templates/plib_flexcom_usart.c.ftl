/*******************************************************************************
  ${FLEXCOM_INSTANCE_NAME} USART PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${FLEXCOM_INSTANCE_NAME?lower_case}_usart.c

  Summary:
    ${FLEXCOM_INSTANCE_NAME} USART PLIB Implementation File

  Description
    This file defines the interface to the ${FLEXCOM_INSTANCE_NAME} USART peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

  Remarks:
    None.
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
/* This section lists the other files that are included in this file.
*/
#include "plib_${FLEXCOM_INSTANCE_NAME?lower_case}_${FLEXCOM_MODE?lower_case}.h"
<#if core.CoreSysIntFile == true>
#include "interrupts.h"
</#if>
<#if FLEXCOM_USART_MR_USART_MODE == "IS07816_T_0">
#include "peripheral/pio/plib_pio.h"
#include "definitions.h"

enum{
    CMD_LEN_4 = 4U,
    CMD_LEN_5,
    CMD_LEN_6,
    CMD_LEN_7
};
#define OUTPUT_CLOCK    ${FLEXCOM_USART_OUTPUTCLOCK}U

#define USART_SEND      0U
#define USART_RCV       1U

/** Case for APDU commands. */
/* Application Protocol Data Unit */
#define CASE1           1U
#define CASE2           2U
#define CASE3           3U

/** NULL byte to restart byte procedure. */
#define ISO_NULL_VAL    0x60U

static uint8_t usart_state = USART_RCV;
</#if>

<#if FLEXCOM_USART_FIFO_ENABLE == true>
#define ${FLEXCOM_INSTANCE_NAME}_USART_HW_RX_FIFO_THRES                 ${FLEXCOM_USART_RX_FIFO_THRESHOLD}U
#define ${FLEXCOM_INSTANCE_NAME}_USART_HW_TX_FIFO_THRES                 ${FLEXCOM_USART_TX_FIFO_THRESHOLD}U
</#if>

#define FLEXCOM_USART_RHR_8BIT_REG      (*(volatile uint8_t* const)((${FLEXCOM_INSTANCE_NAME}_BASE_ADDRESS + FLEX_US_RHR_REG_OFST)))
#define FLEXCOM_USART_RHR_9BIT_REG      (*(volatile uint16_t* const)((${FLEXCOM_INSTANCE_NAME}_BASE_ADDRESS + FLEX_US_RHR_REG_OFST)))

#define FLEXCOM_USART_THR_8BIT_REG      (*(volatile uint8_t* const)((${FLEXCOM_INSTANCE_NAME}_BASE_ADDRESS + FLEX_US_THR_REG_OFST)))
#define FLEXCOM_USART_THR_9BIT_REG      (*(volatile uint16_t* const)((${FLEXCOM_INSTANCE_NAME}_BASE_ADDRESS + FLEX_US_THR_REG_OFST)))

<#--Implementation-->
// *****************************************************************************
// *****************************************************************************
// Section: ${FLEXCOM_INSTANCE_NAME} ${FLEXCOM_MODE} Implementation
// *****************************************************************************
// *****************************************************************************
<#if FLEXCOM_USART_INTERRUPT_MODE_ENABLE == true>
static volatile FLEXCOM_USART_OBJECT ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj;
</#if>

static void ${FLEXCOM_INSTANCE_NAME}_USART_ErrorClear( void )
{
    if ((${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_CSR & (FLEX_US_CSR_OVRE_Msk | FLEX_US_CSR_FRAME_Msk | FLEX_US_CSR_PARE_Msk)) != 0U)
    {
        /* Clear the error flags */
        ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_CR = FLEX_US_CR_RSTSTA_Msk;

        /* Flush existing error bytes from the RX FIFO */
        while((${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_CSR & FLEX_US_CSR_RXRDY_Msk) != 0U)
        {
            if ((${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_MR & FLEX_US_MR_MODE9_Msk) != 0U)
            {
                (void)(FLEXCOM_USART_RHR_9BIT_REG);
            }
            else
            {
                (void)(FLEXCOM_USART_RHR_8BIT_REG);
            }
        }
    }
}

<#if FLEXCOM_USART_INTERRUPT_MODE_ENABLE == true>

<#if !(USE_USART_RECEIVE_DMA??) || (USE_USART_RECEIVE_DMA == false)>
static void __attribute__((used)) ${FLEXCOM_INSTANCE_NAME}_USART_ISR_RX_Handler( void )
{
<#if FLEXCOM_USART_FIFO_ENABLE == true>
    uint32_t rxPending = 0;
    uint32_t rxThreshold = 0;
</#if>
    size_t rxProcessedSize = ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxProcessedSize;
    size_t rxSize = ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxSize;

    if(${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxBusyStatus == true)
    {
        while(((${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_CSR & FLEX_US_CSR_RXRDY_Msk) != 0U) && (rxProcessedSize < rxSize))
        {
            if ((${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_MR & FLEX_US_MR_MODE9_Msk) != 0U)
            {
                ((uint16_t*)${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxBuffer)[rxProcessedSize] = (FLEXCOM_USART_RHR_9BIT_REG & (uint16_t)FLEX_US_RHR_RXCHR_Msk);
                rxProcessedSize++;
            }
            else
            {
                ((uint8_t*)${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxBuffer)[rxProcessedSize] = (FLEXCOM_USART_RHR_8BIT_REG);
                rxProcessedSize++;
            }
        }
<#if FLEXCOM_USART_FIFO_ENABLE == true>

        rxPending = rxSize - rxProcessedSize;
        if (rxPending > 0U)
        {
            rxThreshold = (${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_FMR & FLEX_US_FMR_RXFTHRES_Msk) >> FLEX_US_FMR_RXFTHRES_Pos;
            if (rxPending < rxThreshold)
            {
                ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_FMR = (${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_FMR & ~FLEX_US_FMR_RXFTHRES_Msk) | FLEX_US_FMR_RXFTHRES(rxPending);
            }
        }
</#if>

        ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxProcessedSize = rxProcessedSize;

        /* Check if the buffer is done */
        if(rxProcessedSize >= rxSize)
        {
            ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxBusyStatus = false;

            /* Disable Read, Overrun, Parity and Framing error interrupts */
<#if FLEXCOM_USART_FIFO_ENABLE == true>
            ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_FIDR = FLEX_US_FIDR_RXFTHF_Msk;
            ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_IDR = (FLEX_US_IDR_FRAME_Msk | FLEX_US_IDR_PARE_Msk | FLEX_US_IDR_OVRE_Msk);
<#else>
            ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_IDR = (FLEX_US_IDR_RXRDY_Msk | FLEX_US_IDR_FRAME_Msk | FLEX_US_IDR_PARE_Msk | FLEX_US_IDR_OVRE_Msk);
</#if>

            if(${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxCallback != NULL)
            {
                uintptr_t rxContext = ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxContext;

                ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxCallback(rxContext);
            }
        }
    }
    else
    {
        /* Nothing to process */
    }
}

</#if>
<#if !(USE_USART_TRANSMIT_DMA??) || (USE_USART_TRANSMIT_DMA == false)>
static void __attribute__((used)) ${FLEXCOM_INSTANCE_NAME}_USART_ISR_TX_Handler( void )
{
    if(${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txBusyStatus == true)
    {
        size_t txProcessedSize = ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txProcessedSize;
        size_t txSize = ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txSize;

        while( ((${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_CSR & FLEX_US_CSR_TXRDY_Msk) != 0U) && (txProcessedSize < txSize))
        {
            if ((${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_MR & FLEX_US_MR_MODE9_Msk) != 0U)
            {
                FLEXCOM_USART_THR_9BIT_REG =  ((uint16_t*)${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txBuffer)[txProcessedSize] & (uint16_t)FLEX_US_THR_TXCHR_Msk;
                txProcessedSize++;
            }
            else
            {
                FLEXCOM_USART_THR_8BIT_REG =  ((uint8_t*)${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txBuffer)[txProcessedSize];
                txProcessedSize++;
            }
        }

        ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txProcessedSize = txProcessedSize;

        /* Check if the buffer is done */
        if(txProcessedSize >= txSize)
        {
<#if FLEXCOM_USART_FIFO_ENABLE == true>
            if ((${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_CSR & FLEX_US_CSR_TXEMPTY_Msk) != 0U)
            {
                ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txBusyStatus = false;

                ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_FIDR = FLEX_US_FIDR_TXFTHF_Msk;

                ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_IDR = FLEX_US_IDR_TXEMPTY_Msk;

                if(${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txCallback != NULL)
                {
                    uintptr_t txContext = ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txContext;

                    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txCallback(txContext);
                }
            }
            else
            {
                ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_FIDR = FLEX_US_FIDR_TXFTHF_Msk;

                ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_IER = FLEX_US_IER_TXEMPTY_Msk;
            }
<#else>
            ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txBusyStatus = false;

            ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_IDR = FLEX_US_IDR_TXRDY_Msk;

            if(${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txCallback != NULL)
            {
                uintptr_t txContext = ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txContext;

                ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txCallback(txContext);
            }
</#if>
        }
    }
    else
    {
        /* Nothing to process */
    }
}
</#if>

void __attribute__((used)) ${FLEXCOM_INSTANCE_NAME}_InterruptHandler( void )
{
    /* Channel status */
    uint32_t channelStatus = ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_CSR;

    <#if !(USE_USART_RECEIVE_DMA??) || (USE_USART_RECEIVE_DMA == false)>
    uint32_t interruptMask = ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_IMR;
    </#if>

    <#if (USE_USART_TRANSMIT_DMA?? && USE_USART_TRANSMIT_DMA == true) || (USE_USART_RECEIVE_DMA?? && USE_USART_RECEIVE_DMA == true)>
    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_PTCR = FLEX_PTCR_ERRCLR_Msk;
    </#if>

    <#if USE_USART_RECEIVE_DMA?? && USE_USART_RECEIVE_DMA == true>
    if (((${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_PTSR & FLEX_PTSR_RXTEN_Msk) != 0U) && ((channelStatus & FLEX_US_CSR_ENDRX_Msk) != 0U))
    {
        if(${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxBusyStatus == true)
        {
            ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxBusyStatus = false;
            ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_PTCR = FLEX_PTCR_RXTDIS_Msk;
            ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_IDR = FLEX_US_IDR_ENDRX_Msk;

            if( ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxCallback != NULL )
            {
                uintptr_t rxContext = ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxContext;

                ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxCallback(rxContext);
            }
        }
    }
    <#else>
    /* Error status */
    uint32_t errorStatus = (channelStatus & (FLEX_US_CSR_OVRE_Msk | FLEX_US_CSR_FRAME_Msk | FLEX_US_CSR_PARE_Msk));

    if((errorStatus != 0U) && ((interruptMask & (FLEX_US_IMR_RXRDY_Msk | FLEX_US_IMR_FRAME_Msk | FLEX_US_IMR_PARE_Msk | FLEX_US_IMR_OVRE_Msk)) != 0U))
    {
        /* Save error to report it later */
        ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.errorStatus = errorStatus;

        /* Clear error flags and flush the error data */
        ${FLEXCOM_INSTANCE_NAME}_USART_ErrorClear();

        /* Transfer complete. Clear the busy flag. */
        ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxBusyStatus = false;

<#if FLEXCOM_USART_FIFO_ENABLE == true>
        ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_FIDR = FLEX_US_FIDR_RXFTHF_Msk;
</#if>

        /* Disable Read, Overrun, Parity and Framing error interrupts */
        ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_IDR = (FLEX_US_IDR_RXRDY_Msk | FLEX_US_IDR_FRAME_Msk | FLEX_US_IDR_PARE_Msk | FLEX_US_IDR_OVRE_Msk);

        /* USART errors are normally associated with the receiver, hence calling receiver context */
        if( ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxCallback != NULL )
        {
            uintptr_t rxContext = ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxContext;

            ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxCallback(rxContext);
        }
    }

    /* Receiver status */
    if((channelStatus & FLEX_US_CSR_RXRDY_Msk) != 0U)
    {
        ${FLEXCOM_INSTANCE_NAME}_USART_ISR_RX_Handler();
    }
    </#if>

<#if FLEXCOM_USART_FIFO_ENABLE == true>

    /* Clear the FIFO related interrupt flags */
    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_CR = FLEX_US_CR_RSTSTA_Msk;
</#if>

    <#if USE_USART_TRANSMIT_DMA?? && USE_USART_TRANSMIT_DMA == true>
    if (((${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_PTSR & FLEX_PTSR_TXTEN_Msk) != 0U) && ((channelStatus & FLEX_US_CSR_ENDTX_Msk) != 0U))
    {
        if(${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txBusyStatus == true)
        {
            ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txBusyStatus = false;
            ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_PTCR = FLEX_PTCR_TXTDIS_Msk;
            ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_IDR = FLEX_US_IDR_ENDTX_Msk;

            if( ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txCallback != NULL )
            {
                uintptr_t txContext = ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txContext;

                ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txCallback(txContext);
            }
        }
    }
    <#else>
    /* Transmitter status */
    if((channelStatus & FLEX_US_CSR_TXRDY_Msk) != 0U)
    {
        ${FLEXCOM_INSTANCE_NAME}_USART_ISR_TX_Handler();
    }
    </#if>

}

</#if>

void ${FLEXCOM_INSTANCE_NAME}_USART_Initialize( void )
{
    /* Set FLEXCOM USART operating mode */
    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_MR = FLEX_MR_OPMODE_USART;

    /* Reset ${FLEXCOM_INSTANCE_NAME} USART */
    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_CR = (FLEX_US_CR_RSTRX_Msk | FLEX_US_CR_RSTTX_Msk | FLEX_US_CR_RSTSTA_Msk <#if FLEXCOM_USART_FIFO_ENABLE == true> | FLEX_US_CR_FIFOEN_Msk </#if>);

<#if FLEXCOM_USART_FIFO_ENABLE == true>
    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_FMR = FLEX_US_FMR_TXFTHRES(${FLEXCOM_INSTANCE_NAME}_USART_HW_TX_FIFO_THRES) | FLEX_US_FMR_RXFTHRES(${FLEXCOM_INSTANCE_NAME}_USART_HW_RX_FIFO_THRES) <#if FLEXCOM_USART_MR_USART_MODE == "HW_HANDSHAKING"> | FLEX_US_FMR_RXFTHRES2(${FLEXCOM_USART_RX_FIFO_THRESHOLD_2}) | FLEX_US_FMR_FRTSC_Msk </#if>;
</#if>

    /* Setup transmitter timeguard register */
    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_TTGR = ${FLEXCOM_USART_TTGR};

<#if FLEXCOM_USART_MR_USART_MODE == "IS07816_T_0">
    /* ISO7816 */
    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_FIDI = 372;

    /* ISO7816 */   
    /* Configure ${FLEXCOM_INSTANCE_NAME} USART mode for ISO7816 */
    /* When operating in ISO7816, either in T = 0 or T = 1 modes, the character format is partially predefined.
     * The configuration is forced to 8 data bits, and 1 or 2 stop bits, regardless of the values programmed in 
     * the FLEX_US_MR_CHRL, FLEX_US_MR_MODE9 and FLEX_US_MR_CHMODE fields.
     * FLEX_US_MR_MSBF can be used to transmit LSB or MSB first.
     * FLEX_US_MR_INVDATA can be used to transmit in Normal or Inverse mode. */
    /* T = 0 only (t=0) */
    /* ISO7816 */
    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_MR = ( FLEX_US_MR_USART_MODE_${FLEXCOM_USART_MR_USART_MODE} | FLEX_US_MR_USCLKS_${FLEXCOM_USART_MR_USCLKS} | FLEX_US_MR_CHRL_8_BIT 
            | FLEX_US_MR_CLKO_Msk | FLEX_US_MR_PAR_EVEN | FLEX_US_MR_NBSTOP_1_BIT | FLEX_US_MR_OVER(0));

    /* Configure ${FLEXCOM_INSTANCE_NAME} USART Baud Rate */
    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_BRGR = ${FLEX_USART_CLOCK_FREQ}U / OUTPUT_CLOCK;

<#else>
<#if FLEXCOM_USART_MR_USART_MODE == "LON">
    /* Configure ${FLEXCOM_INSTANCE_NAME} USART ${FLEXCOM_USART_MR_USART_MODE} mode */
    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_MR = ( FLEX_US_MR_USART_MODE_${FLEXCOM_USART_MR_USART_MODE} | FLEX_US_MR_USCLKS_${FLEXCOM_USART_MR_USCLKS} ${(FLEX_USART_MR_MODE9 == true)?then('| FLEX_US_MR_MODE9_Msk', '| FLEX_US_MR_CHRL_${FLEX_USART_MR_CHRL}')} | FLEX_US_MR_PAR_${FLEX_USART_MR_PAR} | FLEX_US_MR_NBSTOP_${FLEX_USART_MR_NBSTOP} | (${FLEXCOM_USART_MR_OVER}UL << FLEX_US_MR_OVER_Pos));

    /* Configure ${FLEXCOM_INSTANCE_NAME} USART Baud Rate */
    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_BRGR = FLEX_US_BRGR_CD(${BRG_VALUE}) | FLEX_US_BRGR_FP(${FP_VALUE});

<#else>
<#if FLEXCOM_USART_MR_USART_MODE == "LIN_MASTER">
    /* Configure ${FLEXCOM_INSTANCE_NAME} USART ${FLEXCOM_USART_MR_USART_MODE} mode */
    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_MR = ( FLEX_US_MR_USART_MODE_${FLEXCOM_USART_MR_USART_MODE} | FLEX_US_MR_USCLKS_${FLEXCOM_USART_MR_USCLKS} ${(FLEX_USART_MR_MODE9 == true)?then('| FLEX_US_MR_MODE9_Msk', '| FLEX_US_MR_CHRL_${FLEX_USART_MR_CHRL}')} | FLEX_US_MR_PAR_${FLEX_USART_MR_PAR} | FLEX_US_MR_NBSTOP_${FLEX_USART_MR_NBSTOP} | (${FLEXCOM_USART_MR_OVER}UL << FLEX_US_MR_OVER_Pos));

    /* Configure ${FLEXCOM_INSTANCE_NAME} USART Baud Rate */
    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_BRGR = FLEX_US_BRGR_CD(${BRG_VALUE}) | FLEX_US_BRGR_FP(${FP_VALUE});

<#else>
<#if FLEXCOM_USART_MR_USART_MODE == "LIN_SLAVE">
    /* Configure ${FLEXCOM_INSTANCE_NAME} USART ${FLEXCOM_USART_MR_USART_MODE} mode */
    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_MR = ( FLEX_US_MR_USART_MODE_${FLEXCOM_USART_MR_USART_MODE} | FLEX_US_MR_USCLKS_${FLEXCOM_USART_MR_USCLKS} ${(FLEX_USART_MR_MODE9 == true)?then('| FLEX_US_MR_MODE9_Msk', '| FLEX_US_MR_CHRL_${FLEX_USART_MR_CHRL}')} | FLEX_US_MR_PAR_${FLEX_USART_MR_PAR} | FLEX_US_MR_NBSTOP_${FLEX_USART_MR_NBSTOP} | (${FLEXCOM_USART_MR_OVER}UL << FLEX_US_MR_OVER_Pos));

    /* Configure ${FLEXCOM_INSTANCE_NAME} USART Baud Rate */
    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_BRGR = FLEX_US_BRGR_CD(${BRG_VALUE}) | FLEX_US_BRGR_FP(${FP_VALUE});

<#else>
    /* Configure ${FLEXCOM_INSTANCE_NAME} USART mode */
    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_MR = ( FLEX_US_MR_USART_MODE_${FLEXCOM_USART_MR_USART_MODE} | FLEX_US_MR_USCLKS_${FLEXCOM_USART_MR_USCLKS} ${(FLEX_USART_MR_MODE9 == true)?then('| FLEX_US_MR_MODE9_Msk', '| FLEX_US_MR_CHRL_${FLEX_USART_MR_CHRL}')} | FLEX_US_MR_PAR_${FLEX_USART_MR_PAR} | FLEX_US_MR_NBSTOP_${FLEX_USART_MR_NBSTOP} | (${FLEXCOM_USART_MR_OVER}UL << FLEX_US_MR_OVER_Pos));

    /* Configure ${FLEXCOM_INSTANCE_NAME} USART Baud Rate */
    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_BRGR = FLEX_US_BRGR_CD(${BRG_VALUE}) | FLEX_US_BRGR_FP(${FP_VALUE});

</#if>
</#if>
</#if>
</#if>
<#if FLEXCOM_USART_MR_USART_MODE == "IRDA">
    /* Setup IR Filter value*/
    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_IF = ${FLEX_USART_IRDA_FILTER_VAL};

    /* Enable ${FLEXCOM_INSTANCE_NAME} USART */
    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_CR = FLEX_US_CR_RXEN_Msk;
<#else>
    /* Enable ${FLEXCOM_INSTANCE_NAME} USART */
    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_CR = (FLEX_US_CR_TXEN_Msk | FLEX_US_CR_RXEN_Msk);
</#if>

<#if FLEXCOM_USART_INTERRUPT_MODE_ENABLE == true>

    /* Initialize instance object */
    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxBuffer = NULL;
    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxSize = 0;
    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxProcessedSize = 0;
    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxBusyStatus = false;
    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxCallback = NULL;
    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.errorStatus = FLEXCOM_USART_ERROR_NONE;
    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txBuffer = NULL;
    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txSize = 0;
    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txProcessedSize = 0;
    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txBusyStatus = false;
    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txCallback = NULL;
</#if>
}

<#if FLEXCOM_USART_INTERRUPT_MODE_ENABLE == true>
FLEXCOM_USART_ERROR ${FLEXCOM_INSTANCE_NAME}_USART_ErrorGet( void )
{
    FLEXCOM_USART_ERROR errorStatus = ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.errorStatus;

    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.errorStatus = FLEXCOM_USART_ERROR_NONE;

    /* All errors are cleared, but send the previous error state */
    return errorStatus;
}
<#else>
FLEXCOM_USART_ERROR ${FLEXCOM_INSTANCE_NAME}_USART_ErrorGet( void )
{
    FLEXCOM_USART_ERROR errors = FLEXCOM_USART_ERROR_NONE;
    uint32_t status = ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_CSR;

    /* Collect all errors */
    if((status & FLEX_US_CSR_OVRE_Msk) != 0U)
    {
        errors = FLEXCOM_USART_ERROR_OVERRUN;
    }
    if((status & FLEX_US_CSR_PARE_Msk) != 0U)
    {
        errors |= FLEXCOM_USART_ERROR_PARITY;
    }
    if((status & FLEX_US_CSR_FRAME_Msk) != 0U)
    {
        errors |= FLEXCOM_USART_ERROR_FRAMING;
    }

    if(errors != FLEXCOM_USART_ERROR_NONE)
    {
        ${FLEXCOM_INSTANCE_NAME}_USART_ErrorClear();
    }

    /* All errors are cleared, but send the previous error state */
    return errors;
}
</#if>

static void ${FLEXCOM_INSTANCE_NAME}_USART_BaudCalculate(uint32_t srcClkFreq, uint32_t reqBaud, uint8_t overSamp, uint32_t* cd, uint32_t* fp, uint32_t* baudError)
{
    uint32_t actualBaud = 0U;

    *cd = srcClkFreq / (reqBaud * 8U * (2U - overSamp));

    if (*cd > 0U)
    {
        *fp = ((srcClkFreq / (reqBaud * (2U - (uint32_t)overSamp))) - ((*cd) * 8U));
        actualBaud = (srcClkFreq / (((*cd) * 8U) + (*fp))) / (2U - overSamp);
        *baudError = ((100U * actualBaud)/reqBaud) - 100U;
    }
}

bool ${FLEXCOM_INSTANCE_NAME}_USART_SerialSetup( FLEXCOM_USART_SERIAL_SETUP *setup, uint32_t srcClkFreq )
{
    uint32_t baud = 0;
    uint32_t overSampVal = 0;
    uint32_t usartMode;
    uint32_t cd0, fp0, cd1, fp1, baudError0, baudError1;
    bool status = false;

    cd0 = fp0 = cd1 = fp1 = baudError0 = baudError1 = 0U;

<#if FLEXCOM_USART_INTERRUPT_MODE_ENABLE == true>
    bool rxBusyStatus = ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxBusyStatus;

    if((${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txBusyStatus == true) || (rxBusyStatus == true))
    {
        /* Transaction is in progress, so return without updating settings */
        return false;
    }

</#if>
    if (setup != NULL)
    {
        baud = setup->baudRate;

        if(srcClkFreq == 0U)
        {
            srcClkFreq = ${FLEXCOM_INSTANCE_NAME}_USART_FrequencyGet();
        }

        /* Calculate baud register values for 8x/16x oversampling values */

        ${FLEXCOM_INSTANCE_NAME}_USART_BaudCalculate(srcClkFreq, baud, 0, &cd0, &fp0, &baudError0);
        ${FLEXCOM_INSTANCE_NAME}_USART_BaudCalculate(srcClkFreq, baud, 1, &cd1, &fp1, &baudError1);

        if ( (!(cd0 > 0U && cd0 <= 65535U)) && (!(cd1 > 0U && cd1 <= 65535U)) )
        {
            /* Requested baud cannot be generated with current clock settings */
            return status;
        }

        if ( ((cd0 > 0U) && (cd0 <= 65535U)) && ((cd1 > 0U) && (cd1 <= 65535U)) )
        {
            /* Requested baud can be generated with both 8x and 16x oversampling. Select the one with less % error. */
            if (baudError1 < baudError0)
            {
                cd0 = cd1;
                fp0 = fp1;
                overSampVal = (1UL << FLEX_US_MR_OVER_Pos) & FLEX_US_MR_OVER_Msk;
            }
        }
        else
        {
            /* Requested baud can be generated with either with 8x oversampling or with 16x oversampling. Select valid one. */
            if ((cd1 > 0U) && (cd1 <= 65535U))
            {
                cd0 = cd1;
                fp0 = fp1;
                overSampVal = (1UL << FLEX_US_MR_OVER_Pos) & FLEX_US_MR_OVER_Msk;
            }
        }

        /* Configure ${FLEXCOM_INSTANCE_NAME} USART mode */
        usartMode = ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_MR;
        usartMode &= ~(FLEX_US_MR_CHRL_Msk | FLEX_US_MR_MODE9_Msk | FLEX_US_MR_PAR_Msk | FLEX_US_MR_NBSTOP_Msk | FLEX_US_MR_OVER_Msk);
        ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_MR = usartMode | ((uint32_t)setup->dataWidth | (uint32_t)setup->parity | (uint32_t)setup->stopBits | overSampVal);

        /* Configure ${FLEXCOM_INSTANCE_NAME} USART Baud Rate */
        ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_BRGR = FLEX_US_BRGR_CD(cd0) | FLEX_US_BRGR_FP(fp0);
        status = true;
    }

    return status;
}

<#if FLEXCOM_USART_INTERRUPT_MODE_ENABLE == false>
bool ${FLEXCOM_INSTANCE_NAME}_USART_Read( void *buffer, const size_t size )
{
    bool status = false;
    uint32_t errorStatus = 0;
    size_t processedSize = 0;

    if(buffer != NULL)
    {
        /* Clear errors that may have got generated when there was no active read request pending */
        ${FLEXCOM_INSTANCE_NAME}_USART_ErrorClear();

        while( processedSize < size )
        {
            while((${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_CSR & FLEX_US_CSR_RXRDY_Msk) == 0U)
            {
                /* Do Nothing */
            }

            /* Read error status */
            errorStatus = (${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_CSR & (FLEX_US_CSR_OVRE_Msk | FLEX_US_CSR_FRAME_Msk | FLEX_US_CSR_PARE_Msk));

            if(errorStatus != 0U)
            {
                break;
            }

            if ((${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_MR & FLEX_US_MR_MODE9_Msk) != 0U)
            {
                ((uint16_t*)buffer)[processedSize] = FLEXCOM_USART_RHR_9BIT_REG & (uint16_t)FLEX_US_RHR_RXCHR_Msk;
            }
            else
            {
                ((uint8_t*)buffer)[processedSize] = FLEXCOM_USART_RHR_8BIT_REG;
            }
            processedSize++;
        }

        if(size == processedSize)
        {
            status = true;
        }
    }

    return status;
}

bool ${FLEXCOM_INSTANCE_NAME}_USART_Write( void *buffer, const size_t size )
{
    bool status = false;
    size_t processedSize = 0;

    if(buffer != NULL)
    {
        while( processedSize < size )
        {
            while ((${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_CSR & FLEX_US_CSR_TXRDY_Msk) == 0U)
            {
                /* Do Nothing */
            }

            if ((${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_MR & FLEX_US_MR_MODE9_Msk) != 0U)
            {
                FLEXCOM_USART_THR_9BIT_REG = ((uint16_t*)buffer)[processedSize] & (uint16_t)FLEX_US_THR_TXCHR_Msk;
            }
            else
            {
                FLEXCOM_USART_THR_8BIT_REG = ((uint8_t*)buffer)[processedSize];
            }
            processedSize++;
        }

        status = true;
    }

    return status;
}

<#else>
bool ${FLEXCOM_INSTANCE_NAME}_USART_Read( void *buffer, const size_t size )
{
    bool status = false;
    if(buffer != NULL)
    {
        /* Check if receive request is in progress */
        if(${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxBusyStatus == false)
        {
            /* Clear errors that may have got generated when there was no active read request pending */
            ${FLEXCOM_INSTANCE_NAME}_USART_ErrorClear();

            /* Clear the errors related to pervious read requests */
            ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.errorStatus = FLEXCOM_USART_ERROR_NONE;

            ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxBuffer = buffer;
            ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxSize = size;
            ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxProcessedSize = 0;
            ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxBusyStatus = true;
            status = true;

<#if USE_USART_RECEIVE_DMA?? && USE_USART_RECEIVE_DMA == true>
            ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_RPR = (uint32_t)(uint8_t*)buffer;
            ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_RCR = (uint32_t) size;
            ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_PTCR = FLEX_PTCR_RXTEN_Msk;
            ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_IER = FLEX_US_IER_ENDRX_Msk;
<#else>

<#if FLEXCOM_USART_FIFO_ENABLE == true>

            size_t rxSize = ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxSize;
            /* Clear RX FIFO */
            ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_CR = FLEX_US_CR_RXFCLR_Msk;

            if (rxSize < ${FLEXCOM_INSTANCE_NAME}_USART_HW_RX_FIFO_THRES)
            {
                ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_FMR = (${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_FMR & ~FLEX_US_FMR_RXFTHRES_Msk) | FLEX_US_FMR_RXFTHRES(rxSize);
            }
            else
            {
                ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_FMR = (${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_FMR & ~FLEX_US_FMR_RXFTHRES_Msk) | FLEX_US_FMR_RXFTHRES(${FLEXCOM_INSTANCE_NAME}_USART_HW_RX_FIFO_THRES);
            }

            /* Enable Read, Overrun, Parity and Framing error interrupts */
            ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_IER = (FLEX_US_IER_FRAME_Msk | FLEX_US_IER_PARE_Msk | FLEX_US_IER_OVRE_Msk);

            /* Enable RX FIFO Threshold interrupt */
            ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_FIER = FLEX_US_FIER_RXFTHF_Msk;

<#else>
            /* Enable Read, Overrun, Parity and Framing error interrupts */
            ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_IER = (FLEX_US_IER_RXRDY_Msk | FLEX_US_IER_FRAME_Msk | FLEX_US_IER_PARE_Msk | FLEX_US_IER_OVRE_Msk);
</#if>

</#if>
        }
    }

    return status;
}

bool ${FLEXCOM_INSTANCE_NAME}_USART_Write( void *buffer, const size_t size )
{
    bool status = false;
    if(buffer != NULL)
    {
        /* Check if transmit request is in progress */
        if(${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txBusyStatus == false)
        {
            ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txBuffer = buffer;
            ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txSize = size;
            ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txProcessedSize = 0;
            ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txBusyStatus = true;
            status = true;

        <#if USE_USART_TRANSMIT_DMA?? && USE_USART_TRANSMIT_DMA == true>
            ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_TPR = (uint32_t)(uint8_t*)buffer;
            ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_TCR = (uint32_t) size;
            ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_PTCR = FLEX_PTCR_TXTEN_Msk;
            ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_IER = FLEX_US_IER_ENDTX_Msk;
        <#else>

            size_t txProcessedSize = ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txProcessedSize;
            size_t txSize = ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txSize;

            /* Initiate the transfer by sending first byte */
            while(((${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_CSR & FLEX_US_CSR_TXRDY_Msk) != 0U) && (txProcessedSize < txSize))
            {
                if ((${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_MR & FLEX_US_MR_MODE9_Msk) != 0U)
                {
                    FLEXCOM_USART_THR_9BIT_REG = ((uint16_t*)${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txBuffer)[txProcessedSize] & (uint16_t)FLEX_US_THR_TXCHR_Msk;
                }
                else
                {
                    FLEXCOM_USART_THR_8BIT_REG = ((uint8_t*)${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txBuffer)[txProcessedSize];
                }
                txProcessedSize++;
            }

            ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txProcessedSize = txProcessedSize;

<#if FLEXCOM_USART_FIFO_ENABLE == true>
            if ( ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txProcessedSize >= txSize)
            {
                ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_IER = FLEX_US_IER_TXEMPTY_Msk;
            }
            else
            {
                ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_FIER = FLEX_US_FIER_TXFTHF_Msk;
            }
<#else>
            ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_IER = FLEX_US_IER_TXRDY_Msk;
</#if>
</#if>
        }
    }

    return status;
}
</#if>

<#if FLEXCOM_USART_INTERRUPT_MODE_ENABLE == true>
void ${FLEXCOM_INSTANCE_NAME}_USART_WriteCallbackRegister( FLEXCOM_USART_CALLBACK callback, uintptr_t context )
{
    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txCallback = callback;
    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txContext = context;
}

void ${FLEXCOM_INSTANCE_NAME}_USART_ReadCallbackRegister( FLEXCOM_USART_CALLBACK callback, uintptr_t context )
{
    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxCallback = callback;
    ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxContext = context;
}

bool ${FLEXCOM_INSTANCE_NAME}_USART_WriteIsBusy( void )
{
    return ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txBusyStatus;
}

bool ${FLEXCOM_INSTANCE_NAME}_USART_ReadIsBusy( void )
{
    return ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxBusyStatus;
}

size_t ${FLEXCOM_INSTANCE_NAME}_USART_WriteCountGet( void )
{
    return ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.txProcessedSize;
}

size_t ${FLEXCOM_INSTANCE_NAME}_USART_ReadCountGet( void )
{
    return ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxProcessedSize;
}

bool ${FLEXCOM_INSTANCE_NAME}_USART_ReadAbort(void)
{
    if (${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxBusyStatus == true)
    {
        /* Disable Read, Overrun, Parity and Framing error interrupts */
        ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_IDR = (FLEX_US_IDR_RXRDY_Msk | FLEX_US_IDR_FRAME_Msk | FLEX_US_IDR_PARE_Msk | FLEX_US_IDR_OVRE_Msk);

        ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxBusyStatus = false;

        /* If required application should read the num bytes processed prior to calling the read abort API */
        ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxSize = 0U;
        ${FLEXCOM_INSTANCE_NAME?lower_case}UsartObj.rxProcessedSize = 0U;
    }

    return true;
}

</#if>
<#if FLEXCOM_USART_INTERRUPT_MODE_ENABLE == false>
uint8_t ${FLEXCOM_INSTANCE_NAME}_USART_ReadByte(void)
{
    return((uint8_t)(${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_RHR & FLEX_US_RHR_RXCHR_Msk));
}

void ${FLEXCOM_INSTANCE_NAME}_USART_WriteByte(uint8_t data)
{
    while ((${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_CSR & FLEX_US_CSR_TXRDY_Msk) == 0U)
    {
        /* Do Nothing */
    }

    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_THR = (FLEX_US_THR_TXCHR(data) & FLEX_US_THR_TXCHR_Msk);
}

bool ${FLEXCOM_INSTANCE_NAME}_USART_TransmitterIsReady( void )
{
    return ((${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_CSR & FLEX_US_CSR_TXRDY_Msk) != 0U);
}

bool ${FLEXCOM_INSTANCE_NAME}_USART_ReceiverIsReady( void )
{
    return ((${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_CSR & FLEX_US_CSR_RXRDY_Msk) != 0U);
}

</#if>

bool ${FLEXCOM_INSTANCE_NAME}_USART_TransmitComplete( void )
{
    return ((${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_CSR & FLEX_US_CSR_TXEMPTY_Msk) != 0U);
}

<#if FLEXCOM_USART_MR_USART_MODE == "IRDA">
void ${FLEXCOM_INSTANCE_NAME}_USART_IrDA_DirectionSet(FLEXCOM_IRDA_DIR dir)
{
    if (dir == FLEXCOM_IRDA_DIR_TRANSMIT)
    {
        ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_CR = (FLEX_US_CR_TXEN_Msk | FLEX_US_CR_RXDIS_Msk);
    }
    else
    {
        ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_CR = (FLEX_US_CR_RXEN_Msk | FLEX_US_CR_TXDIS_Msk);
    }
}
</#if>

<#if FLEXCOM_USART_MR_USART_MODE == "IS07816_T_0">
void ${FLEXCOM_INSTANCE_NAME}_ISO7816_Icc_Power_On( void )
{
    CARD_RESET_Set();
}

void ${FLEXCOM_INSTANCE_NAME}_ISO7816_Icc_Power_Off( void )
{
    CARD_RESET_Clear();
}

bool ${FLEXCOM_INSTANCE_NAME}_ISO7816_Card_Detect(void)
{
    if(CARD_DETECT_Get() == true)
    {
        return true;
    }
    else
    {
        return false;
    }
}

void ${FLEXCOM_INSTANCE_NAME}_ISO7816_Vcc_Enable( void )
{
    CARD_VCC_Set();
}

void ${FLEXCOM_INSTANCE_NAME}_ISO7816_Vcc_Disable( void )
{
    CARD_VCC_Clear();
}

static uint32_t Send_Receive_Timeout(void)
{
    /* wait 40.000 cycles */
    return ((CPU_CLOCK_FREQUENCY/OUTPUT_CLOCK)*40000U);
}

/* Wait cold reset */
static uint32_t Reset_Waitcount(void)
{
    /* wait 400 cycles */
    return ((CPU_CLOCK_FREQUENCY/OUTPUT_CLOCK)*400U);
}

static void ${FLEXCOM_INSTANCE_NAME}_ISO7816_Cold_Reset(void)
{
    uint32_t i, rst_wait_time;

    rst_wait_time = Reset_Waitcount();

    /* The card is reset by maintaining RST at state L for at least 400 clock cycles (tb) after the
     * clock signal is applied to CLK (time tb after Ta). */
    for (i = 0; i < rst_wait_time; i++)
    {
    }

    //Read all the leftover data from card
    while(${FLEXCOM_INSTANCE_NAME}_USART_ReadByte() != 0){
    }

    /* RSTSTA  Reset Status Bits */
    /* RSTIT   Reset Iterations */
    /* RSTNACK Reset Non Acknowledge */
    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_CR = FLEX_US_CR_RSTSTA_Msk | FLEX_US_CR_RSTIT_Msk | FLEX_US_CR_RSTNACK_Msk;

    /* ISO7816 reset iterations */
    if((${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_MR & FLEX_US_MR_MAX_ITERATION_Msk) != 0U)
    {
        /* Defines the maximum number of iterations in mode ISO7816, protocol T = 0. */
        ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_MR |= FLEX_US_MR_MAX_ITERATION_Msk;
    }

    /* Enable Reset pin to high */
    ${FLEXCOM_INSTANCE_NAME}_ISO7816_Icc_Power_On();
}


void ${FLEXCOM_INSTANCE_NAME}_ISO7816_Warm_Reset(void)
{
    //Enable Reset pin to high
    /* Disable card reset */
    ${FLEXCOM_INSTANCE_NAME}_ISO7816_Icc_Power_Off();

    ${FLEXCOM_INSTANCE_NAME}_ISO7816_Cold_Reset();
}


/******************************************************************************/
static uint8_t ${FLEXCOM_INSTANCE_NAME}_ISO7816_Get_Char(uint8_t *p_char_received)
{
    uint32_t timeout = 0, rx_timeout;
    uint32_t status;

    rx_timeout = Send_Receive_Timeout();

    if (usart_state == USART_SEND)
    {
        timeout = 0;
        // All transmit finish
        while ((${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_CSR & FLEX_US_CSR_TXEMPTY_Msk) == 0)
        {
            if (timeout++ > rx_timeout)
            {
                printf("TX");
                timeout = 0;
                return (0);
            }
        }
        ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_CR = FLEX_US_CR_RSTSTA_Msk | FLEX_US_CR_RSTIT_Msk | FLEX_US_CR_RSTNACK_Msk;
        ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_CR = FLEX_US_CR_TXDIS_Msk;
        usart_state = USART_RCV;
    }
            
    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_CR = FLEX_US_CR_RXEN_Msk;

    /* Wait USART ready for reception */
    timeout = 0;
    while((${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_CSR & FLEX_US_CSR_RXRDY_Msk) == 0U)
    {
        /* 0: Receive FIFO is empty; no data to read */
        if (timeout++ > rx_timeout)
        {
            timeout = 0;
            return (0);
        }
    }

    /* Receive a char */
    *p_char_received = (uint8_t) ${FLEXCOM_INSTANCE_NAME}_USART_ReadByte();

    status = (${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_CSR & (FLEX_US_CSR_OVRE_Msk | FLEX_US_CSR_FRAME_Msk | FLEX_US_CSR_PARE_Msk 
            | FLEX_US_CSR_TIMEOUT_Msk | FLEX_US_CSR_NACK_Msk | FLEX_US_CSR_ITER_Msk));

    // Disable receiver
    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_CR = FLEX_US_CR_RXDIS_Msk;

    if (status != 0) 
    {
        printf("GetCharError:0x%08X ", (unsigned)${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_CSR);
        return (0);
    }
    return (1);
}

/******************************************************************************/
static uint8_t ${FLEXCOM_INSTANCE_NAME}_ISO7816_Send_Char(uint8_t uc_char)
{
    uint32_t timeout = 0, rx_timeout;
    uint32_t status;

    rx_timeout = Send_Receive_Timeout();

    if (usart_state == USART_RCV)
    {
        ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_CR = FLEX_US_CR_RSTSTA_Msk | FLEX_US_CR_RSTIT_Msk | FLEX_US_CR_RSTNACK_Msk;

        timeout = 0;
        while((${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_CSR & FLEX_US_CSR_RXRDY_Msk) != 0U)
        {
            (void)${FLEXCOM_INSTANCE_NAME}_USART_ReadByte();
            if (timeout++ > rx_timeout)
            {
                printf("TS");
                timeout = 0;
                return (0);
            }
        }
        /* ISO7816 reset iterations */
        if((${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_MR & FLEX_US_MR_MAX_ITERATION_Msk) != 0U)
        {
            /* Defines the maximum number of iterations in mode ISO7816, protocol T = 0. */
            ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_MR |= FLEX_US_MR_MAX_ITERATION_Msk;
        }
        ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_CR = FLEX_US_CR_RXDIS_Msk;
        usart_state = USART_SEND;
    }

    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_CR = FLEX_US_CR_TXEN_Msk;

    /* Wait flexcom ready for transmit */
    timeout = 0;
    while ((${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_CSR & FLEX_US_CSR_TXEMPTY_Msk) == 0)
    {
        // There are characters in either FLEX_US_THR or the Transmit Shift Register, or the transmitter is disabled.
        if (timeout++ > rx_timeout)
        {
            printf("TS");
            timeout = 0;
            return (0);
        }
    }
    /* Transmit a char */
    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_THR = uc_char;
   
    status = (${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_CSR & (FLEX_US_CSR_OVRE_Msk | FLEX_US_CSR_FRAME_Msk | FLEX_US_CSR_PARE_Msk 
            | FLEX_US_CSR_TIMEOUT_Msk | FLEX_US_CSR_NACK_Msk | FLEX_US_CSR_ITER_Msk));
    if (status != 0) 
    {
        printf("SendCharError:0x%08X ", (unsigned)${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_US_CSR);
        return (0);
    }
    return (1);
}

uint8_t ${FLEXCOM_INSTANCE_NAME}_ISO7816_Data_Read_Atr( uint8_t *p_atr )
{
    uint8_t j, response_length, uc_value;
    uint8_t status;

    /* Read ATR TS. */
    status = ${FLEXCOM_INSTANCE_NAME}_ISO7816_Get_Char(&p_atr[0]);
    if (status == 0U)
    {
        printf("\r\nError ATR TS");
        return 0;
    }

    /* Read ATR T0. */
    status = ${FLEXCOM_INSTANCE_NAME}_ISO7816_Get_Char(&p_atr[1]);
    if (status == 0U)
    {
        printf("\r\nError ATR T0");
        return 0;
    }

    uc_value = p_atr[1] & 0xF0U;
    response_length = 2;

    /* Read ATR Ti. */
    while (uc_value != 0U)
    {
        if ((uc_value & 0x10U) == 0x10U)
        { /* TA[response_length] */
            status = ${FLEXCOM_INSTANCE_NAME}_ISO7816_Get_Char(&p_atr[response_length++]);
            if (status == 0U)
            {
                printf("\r\nError ATR TA");
                return 0;
            }
        }

        if ((uc_value & 0x20U) == 0x20U)
        { /* TB[response_length] */
            status = ${FLEXCOM_INSTANCE_NAME}_ISO7816_Get_Char(&p_atr[response_length++]);
            if (status == 0U)
            {
                printf("\r\nError ATR TB");
                return 0;
            }
        }

        if ((uc_value & 0x40U) == 0x40U)
        { /* TC[response_length] */
            status = ${FLEXCOM_INSTANCE_NAME}_ISO7816_Get_Char(&p_atr[response_length++]);
            if (status == 0U)
            {
                printf("\r\nError ATR TC");
                return 0;
            }
        }

        if ((uc_value & 0x80U) == 0X80U)
        { /* TD[response_length] */
            status = ${FLEXCOM_INSTANCE_NAME}_ISO7816_Get_Char(&p_atr[response_length]);
            if (status == 0U)
            {
                printf("\r\nError ATR TD");
                return 0;
            }

            uc_value = p_atr[response_length++] & 0xF0U;
        } 
        else
        {
            uc_value = 0;
        }
    }

    /* Historical Bytes. */
    uc_value = p_atr[1] & 0x0FU;
    for (j = 0; j < uc_value; j++)
    {
        status = ${FLEXCOM_INSTANCE_NAME}_ISO7816_Get_Char(&p_atr[response_length++]);
        if (status == 0U)
        {
            printf("\r\nError ATR Hist Bytes");
            return 0;
        }
    }

    /* TCK (optional) */
    status = ${FLEXCOM_INSTANCE_NAME}_ISO7816_Get_Char(&p_atr[response_length]);
    if (status != 0U)
    {
        response_length++;
    }

    return (response_length);
}



/**
 * Decode ATR trace
 * \param pAtr pointer on ATR buffer
 */
void ${FLEXCOM_INSTANCE_NAME}_ISO7816_Decode_Atr(uint8_t * pAtr, uint8_t size)
{
    uint32_t i, j, y, z;
    uint8_t offset;

    printf("\n\r");
    printf("ATR: Answer To Reset:\n\r");
    printf("  TS = 0x%X Initial character ", pAtr[0]);

    switch (pAtr[0])
    {
        case 0x3B:
            printf("Direct Convention\n\r");
            break;
        case 0x3F:
            printf("Inverse Convention\n\r");
            break;
        default:
            printf("BAD Convention\n\r");
            break;
    }
    printf("  T0 = 0x%X Format character\n\r", pAtr[1]);
    printf("    Number of historical bytes: K = %d\n\r", pAtr[1] & 0x0F);
    printf("    Presence further interface byte:");
    if (pAtr[1] & 0x10)
    {
        printf("  TA ");
    }
    if (pAtr[1] & 0x20)
    {
        printf("  TB ");
    }
    if (pAtr[1] & 0x40)
    {
        printf("  TC ");
    }
    if (pAtr[1] & 0x80)
    {
        printf("  TD ");
    }
    if (pAtr[1] != 0)
    {
        printf(" present(s)\n\r");
    }

    i = 2;
    y = pAtr[1] & 0xF0;

    /* Read ATR Ti */
    offset = 1;
    while (y)
    {
        if (y & 0x10) 
        {    /* TA[i] */
            printf("  TA[%d] = 0x%X ", offset, pAtr[i]);
            if (offset == 1)
            {
                printf("FI = %d, ", (pAtr[i] >> 4));
                printf("DI = %d", (pAtr[i] & 0x0F));
            }
            if( offset == 2)
            {
                /* TA[2] */
                if(0x80 == (pAtr[i]&0x80))
                {
                    printf("  Unable to change: protocol T=%d", pAtr[i]&0xF);
                }
                else
                {
                    printf("  Capable to change: protocol T=%d", pAtr[i]&0xF);
                }
            }
            printf("\n\r");
            i++;
        }
        if (y & 0x20)
        {    /* TB[i] */
            printf("  TB[%d] = 0x%X\n\r", offset, pAtr[i]);
            i++;
        }
        if (y & 0x40)
        {    /* TC[i] */
            printf("  TC[%d] = 0x%X ", offset, pAtr[i]);
            if (offset == 1) {
                printf("Extra Guard Time: N = %d", pAtr[i]);
            }
            printf("\n\r");
            i++;
        }
        if (y & 0x80)
        {    /* TD[i] */
            printf("  TD[%d] = 0x%X ", offset, pAtr[i]);
            printf("Protocol T = %d\n\r", (pAtr[i]&0x0F) );
            y = pAtr[i++] & 0xF0;
        } 
        else
        {
            y = 0;
        }
        offset++;
    }

    /* Historical Bytes */
    printf("  Historical bytes:");
    y = pAtr[1] & 0x0F;
    z = i;
    for (j = 0; j < y; j++)
    {
        printf(" 0x%X", pAtr[i]);
        i++;
    }
    printf("\n\r    ASCII: ");
    i = z;
    for (j = 0; j < y; j++)
    {
        if ((pAtr[i] > 0x21) && (pAtr[i] < 0x7D)) 
        {    
            /* ASCII */
            printf("%c", pAtr[i]);
        }
        i++;
    }
    if(size < i)
    {
        printf("\n\rTCK present");
    }
    else
    {
        printf("\n\r  no TCK");
    }
}


uint16_t ${FLEXCOM_INSTANCE_NAME}_ISO7816_Xfr_Block_Tpdu( uint8_t *apdu_cmd_buffer, uint8_t *apdu_res_buffer, const size_t apdu_cmd_length )
{
    uint16_t us_ne_nc, cmd_index = 4;
    uint16_t resp_index = 0;
    uint8_t sw1_rcvd = 0, cmd_type, status;
    uint8_t proc_byte;

    (void)${FLEXCOM_INSTANCE_NAME}_ISO7816_Send_Char(apdu_cmd_buffer[0]);    /* CLA */
    (void)${FLEXCOM_INSTANCE_NAME}_ISO7816_Send_Char(apdu_cmd_buffer[1]);    /* INS */
    (void)${FLEXCOM_INSTANCE_NAME}_ISO7816_Send_Char(apdu_cmd_buffer[2]);    /* P1 */
    (void)${FLEXCOM_INSTANCE_NAME}_ISO7816_Send_Char(apdu_cmd_buffer[3]);    /* P2 */
    (void)${FLEXCOM_INSTANCE_NAME}_ISO7816_Send_Char(apdu_cmd_buffer[4]);    /* P3 */

    /* Handle the four structures of command APDU. */
    switch (apdu_cmd_length)
    {
        case CMD_LEN_4:

            cmd_type = CASE1;
            us_ne_nc = 0;

            break;

        case CMD_LEN_5:

            cmd_type = CASE2;
            us_ne_nc = apdu_cmd_buffer[4];                                                              /* C5, only Standard Le */
            if (us_ne_nc == 0U)
            {
                us_ne_nc = 256;
            }
            break;

        case CMD_LEN_6:

            us_ne_nc = apdu_cmd_buffer[4];                                                              /* C5, only Standard Lc */
            cmd_type = CASE3;

            break;

        case CMD_LEN_7:

            us_ne_nc = apdu_cmd_buffer[4];                                                              /* C5 */
            if (us_ne_nc == 0U)
            {
                cmd_type = CASE2;
                us_ne_nc = ((uint16_t)apdu_cmd_buffer[5] << 8) + (uint16_t)apdu_cmd_buffer[6];          /*Extended Le */
            }
            else
            {
                cmd_type = CASE3;                                                                       /*Standard Lc*/
            }
            break;

        default:

            us_ne_nc = apdu_cmd_buffer[4];                                                              /* C5 */

            if (us_ne_nc == 0U)
            {
                cmd_type = CASE3;
                us_ne_nc = ((uint16_t)apdu_cmd_buffer[5] << 8) + (uint16_t)apdu_cmd_buffer[6];          /*Extended Lc */
            }
            else
            {
                cmd_type = CASE3;                                                                       /*Standard Lc*/
            }

            break;
    }

    /* Handle Procedure Bytes. */
    do{
        status = ${FLEXCOM_INSTANCE_NAME}_ISO7816_Get_Char(&proc_byte);
        if(status == 0U)
        {
            return 0;
        }

        /* Handle NULL. */
        if (ISO_NULL_VAL == proc_byte) {
            continue;
        }
        /* Handle sw1. */
        else if (((proc_byte & 0xF0U) == 0x60U) || ((proc_byte & 0xF0U) == 0x90U))
        {
            sw1_rcvd = 1;
        }
        /* Handle INS. */
        else if (apdu_cmd_buffer[1] == proc_byte)
        {
            if (cmd_type == CASE2)
            {
                /* Receive data from card. */
                do {
                    status = ${FLEXCOM_INSTANCE_NAME}_ISO7816_Get_Char(&apdu_res_buffer[resp_index]);
                    resp_index++;
                } while (0U != --us_ne_nc);
            }
            else
            {
                /* Send data. */
                do {
                    cmd_index++;
                    (void)${FLEXCOM_INSTANCE_NAME}_ISO7816_Send_Char(apdu_cmd_buffer[cmd_index]);
                } while (0U != --us_ne_nc);
            }
        }
        /* Handle INS ^ 0xff. */
        else if ((apdu_cmd_buffer[1] ^ 0xffU) == proc_byte)
        {
            if (cmd_type == CASE2)
            {
                /* receive data from card. */
                status = ${FLEXCOM_INSTANCE_NAME}_ISO7816_Get_Char(&apdu_res_buffer[resp_index]);
                resp_index++;
            }
            else
            {
                (void)${FLEXCOM_INSTANCE_NAME}_ISO7816_Send_Char(apdu_cmd_buffer[cmd_index]);
                cmd_index++;
            }
            us_ne_nc--;
        }
        else
        {
            break;
        }
    } while (us_ne_nc != 0U);

    /* Status Bytes. */
    if (sw1_rcvd == 0U)
    {
        (void)${FLEXCOM_INSTANCE_NAME}_ISO7816_Get_Char(&apdu_res_buffer[resp_index]);                 /* sw1_rcvd */
        resp_index++;
    }
    else
    {
        apdu_res_buffer[resp_index] = proc_byte;
        resp_index++;
    }
    (void)${FLEXCOM_INSTANCE_NAME}_ISO7816_Get_Char(&apdu_res_buffer[resp_index]);                     /* SW2 */

    resp_index++;

    return (resp_index);
}
</#if>

