/*******************************************************************************
  ${UART_INSTANCE_NAME} PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${UART_INSTANCE_NAME?lower_case}.c

  Summary:
    ${UART_INSTANCE_NAME} PLIB Implementation File

  Description:
    None

*******************************************************************************/

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

<#if core.CoreSysIntFile == true>
#include "interrupts.h"
</#if>
#include "plib_${UART_INSTANCE_NAME?lower_case}.h"
#include "../ecia/plib_ecia.h"

<#--Implementation-->
// *****************************************************************************
// *****************************************************************************
// Section: ${UART_INSTANCE_NAME} Implementation
// *****************************************************************************
// *****************************************************************************

<#if UART_OPERATING_MODE == "NON_BLOCKING">
static UART_OBJECT ${UART_INSTANCE_NAME?lower_case}Obj;
<#else>
static UART_ERROR errorStatus = 0;
</#if>

void ${UART_INSTANCE_NAME}_Initialize( void )
{
    <#if UART_REG_CONFIG_SEL != "0">
    UART${UART_INSTANCE_NUM}_REGS->DATA.UART_CFG_SEL = 0x${UART_REG_CONFIG_SEL};
    </#if>
    UART${UART_INSTANCE_NUM}_REGS->DATA.UART_LCR |= UART_DATA_LCR_DLAB_Msk;
    UART${UART_INSTANCE_NUM}_REGS->DLAB.UART_BAUDRT_MSB = 0x${UART_REG_BAUD_GEN_MSB};
    UART${UART_INSTANCE_NUM}_REGS->DLAB.UART_BAUDRT_LSB = 0x${UART_REG_BAUD_GEN_LSB};
    UART${UART_INSTANCE_NUM}_REGS->DATA.UART_LCR &= ~UART_DATA_LCR_DLAB_Msk;
    UART${UART_INSTANCE_NUM}_REGS->DATA.UART_LCR = 0x${UART_REG_LCR};

<#if UART_OPERATING_MODE == "NON_BLOCKING">
    UART${UART_INSTANCE_NUM}_REGS->DATA.UART_MCR = UART_DATA_MCR_OUT2_Msk;
    /* Initialize instance object */
    ${UART_INSTANCE_NAME?lower_case}Obj.rxBuffer = NULL;
    ${UART_INSTANCE_NAME?lower_case}Obj.rxSize = 0;
    ${UART_INSTANCE_NAME?lower_case}Obj.rxProcessedSize = 0;
    ${UART_INSTANCE_NAME?lower_case}Obj.rxBusyStatus = false;
    ${UART_INSTANCE_NAME?lower_case}Obj.rxCallback = NULL;
    ${UART_INSTANCE_NAME?lower_case}Obj.txBuffer = NULL;
    ${UART_INSTANCE_NAME?lower_case}Obj.txSize = 0;
    ${UART_INSTANCE_NAME?lower_case}Obj.txProcessedSize = 0;
    ${UART_INSTANCE_NAME?lower_case}Obj.txBusyStatus = false;
    ${UART_INSTANCE_NAME?lower_case}Obj.txCallback = NULL;
    ${UART_INSTANCE_NAME?lower_case}Obj.errors = UART_ERROR_NONE;

</#if>
    /* Turn ON ${UART_INSTANCE_NAME} */
    UART${UART_INSTANCE_NUM}_REGS->DATA.UART_ACTIVATE = 0x01;
}

bool ${UART_INSTANCE_NAME}_SerialSetup(UART_SERIAL_SETUP* setup, uint32_t srcClkFreq )
{
    bool status = false;
    uint32_t baud;
    uint32_t baud_clk_src = 1843200;
    uint32_t baud_div;

<#if UART_OPERATING_MODE == "NON_BLOCKING">
    if((${UART_INSTANCE_NAME?lower_case}Obj.rxBusyStatus == true) || (${UART_INSTANCE_NAME?lower_case}Obj.txBusyStatus == true))
    {
        /* Transaction is in progress, so return without updating settings */
        return status;
    }

</#if>
    if (setup != NULL)
    {
        baud = setup->baudRate;

        /* Set DLAB = 1 */
        UART${UART_INSTANCE_NUM}_REGS->DATA.UART_LCR |= UART_DATA_LCR_DLAB_Msk;

        if ((UART${UART_INSTANCE_NUM}_REGS->DLAB.UART_BAUDRT_MSB & 0x80U) != 0U)
        {
            baud_clk_src = 48000000;
        }

        baud_div = (baud_clk_src >> 4)/baud;

        if ((baud_div < 1U) || (baud_div > 32767U))
        {
            /* Set DLAB = 0 */
            UART${UART_INSTANCE_NUM}_REGS->DATA.UART_LCR &= ~UART_DATA_LCR_DLAB_Msk;

            return status;
        }

        UART${UART_INSTANCE_NUM}_REGS->DLAB.UART_BAUDRT_LSB = (uint8_t)baud_div;
        UART${UART_INSTANCE_NUM}_REGS->DLAB.UART_BAUDRT_MSB |= (uint8_t)((baud_div & 0x7F00U) >> 8U);

        /* Set DLAB = 0 */
        UART${UART_INSTANCE_NUM}_REGS->DATA.UART_LCR &= ~UART_DATA_LCR_DLAB_Msk;

        UART${UART_INSTANCE_NUM}_REGS->DATA.UART_LCR = (UART${UART_INSTANCE_NUM}_REGS->DATA.UART_LCR & ~(UART_DATA_LCR_PAR_SEL_Msk | UART_DATA_LCR_STOP_BITS_Msk | UART_DATA_LCR_WORD_LEN_Msk)) | ((uint8_t)setup->parity | (uint8_t)setup->stopBits | (uint8_t)setup->dataWidth);

        if (setup->parity == UART_PARITY_NONE)
        {
            UART${UART_INSTANCE_NUM}_REGS->DATA.UART_LCR &= ~UART_DATA_LCR_EN_PAR_Msk;
        }
        else
        {
            UART${UART_INSTANCE_NUM}_REGS->DATA.UART_LCR |= UART_DATA_LCR_EN_PAR_Msk;
        }

        status = true;
    }

    return status;
}

bool ${UART_INSTANCE_NAME}_Read(void* buffer, const size_t size )
{
    bool status = false;
    uint8_t lsr;
    uint8_t* pRxBuffer = (uint8_t* )buffer;
<#if UART_OPERATING_MODE == "BLOCKING">
    size_t processedSize = 0;
</#if>

    if(pRxBuffer != NULL)
    {
<#if UART_OPERATING_MODE == "BLOCKING">
        /* Clear error flags that may have been received when no active request was pending */
        lsr = UART${UART_INSTANCE_NUM}_REGS->DATA.UART_LSR;

        while( size > processedSize )
        {
            /* Wait for data ready flag */
            do
            {
                lsr = UART${UART_INSTANCE_NUM}_REGS->DATA.UART_LSR;
            }while ((lsr & (UART_DATA_LSR_DATA_READY_Msk | UART_DATA_LSR_OVERRUN_Msk | UART_DATA_LSR_PE_Msk | UART_DATA_LSR_FRAME_ERR_Msk)) == 0U);

            /* Check for overrun, parity and framing errors */
            lsr = (lsr & (UART_DATA_LSR_OVERRUN_Msk | UART_DATA_LSR_PE_Msk | UART_DATA_LSR_FRAME_ERR_Msk));
            errorStatus = lsr;

            if ((uint32_t)errorStatus != 0U)
            {
                break;
            }
            else
            {
                pRxBuffer[processedSize] = UART${UART_INSTANCE_NUM}_REGS->DATA.UART_RX_DAT;
                processedSize++;
            }
        }

        if(size == processedSize)
        {
            status = true;
        }
<#else>
        /* Check if receive request is in progress */
        if(${UART_INSTANCE_NAME?lower_case}Obj.rxBusyStatus == false)
        {
            /* Clear error flags that may have been received when no active request was pending */
            lsr = UART${UART_INSTANCE_NUM}_REGS->DATA.UART_LSR;
            (void)lsr;

            ${UART_INSTANCE_NAME?lower_case}Obj.rxBuffer = pRxBuffer;
            ${UART_INSTANCE_NAME?lower_case}Obj.rxSize = size;
            ${UART_INSTANCE_NAME?lower_case}Obj.rxProcessedSize = 0;
            ${UART_INSTANCE_NAME?lower_case}Obj.rxBusyStatus = true;
            ${UART_INSTANCE_NAME?lower_case}Obj.errors = UART_ERROR_NONE;

            status = true;

            /* Enable ${UART_INSTANCE_NAME} Receive and Line Error Interrupt */
            UART${UART_INSTANCE_NUM}_REGS->DATA.UART_IEN |= (UART_DATA_IEN_ERDAI_Msk | UART_DATA_IEN_ELSI_Msk);
        }
</#if>
    }

    return status;
}

bool ${UART_INSTANCE_NAME}_Write( void* buffer, const size_t size )
{
    bool status = false;
    uint8_t* pTxBuffer = (uint8_t*)buffer;
<#if UART_OPERATING_MODE == "BLOCKING">
    size_t processedSize = 0;
</#if>

    if(pTxBuffer != NULL)
    {
<#if UART_OPERATING_MODE == "BLOCKING">

        while( size > processedSize )
        {
            /* Wait for transmitter to become ready */
            while ((UART${UART_INSTANCE_NUM}_REGS->DATA.UART_LSR & UART_DATA_LSR_TRANS_EMPTY_Msk) == 0U)
            {
            }
            UART${UART_INSTANCE_NUM}_REGS->DATA.UART_TX_DAT = pTxBuffer[processedSize];
            processedSize++;
        }

        status = true;
<#else>
        /* Check if transmit request is in progress */
        if(${UART_INSTANCE_NAME?lower_case}Obj.txBusyStatus == false)
        {
            ${UART_INSTANCE_NAME?lower_case}Obj.txBuffer = pTxBuffer;
            ${UART_INSTANCE_NAME?lower_case}Obj.txSize = size;
            ${UART_INSTANCE_NAME?lower_case}Obj.txProcessedSize = 0;
            ${UART_INSTANCE_NAME?lower_case}Obj.txBusyStatus = true;
            status = true;

            /* Initiate the transfer by writing as many bytes as we can */
            while(((UART${UART_INSTANCE_NUM}_REGS->DATA.UART_LSR & UART_DATA_LSR_TRANS_EMPTY_Msk) != 0U) && (${UART_INSTANCE_NAME?lower_case}Obj.txSize > ${UART_INSTANCE_NAME?lower_case}Obj.txProcessedSize) )
            {
                UART${UART_INSTANCE_NUM}_REGS->DATA.UART_TX_DAT = pTxBuffer[${UART_INSTANCE_NAME?lower_case}Obj.txProcessedSize];
                ${UART_INSTANCE_NAME?lower_case}Obj.txProcessedSize++;
            }

            /* Enable ${UART_INSTANCE_NAME} Transmit holding register empty Interrupt */
            UART${UART_INSTANCE_NUM}_REGS->DATA.UART_IEN |= (UART_DATA_IEN_ETHREI_Msk);
        }
</#if>
    }

    return status;
}

<#if UART_OPERATING_MODE == "BLOCKING">
UART_ERROR ${UART_INSTANCE_NAME}_ErrorGet( void )
{
    UART_ERROR errors = errorStatus;

    errorStatus = UART_ERROR_NONE;

    /* All errors are cleared, but send the previous error state */
    return errors;
}
<#else>
UART_ERROR ${UART_INSTANCE_NAME}_ErrorGet( void )
{
    UART_ERROR errors = ${UART_INSTANCE_NAME?lower_case}Obj.errors;

    ${UART_INSTANCE_NAME?lower_case}Obj.errors = UART_ERROR_NONE;

    /* All errors are cleared, but send the previous error state */
    return errors;
}
</#if>


bool ${UART_INSTANCE_NAME}_TransmitComplete( void )
{
    bool transmitComplete = false;

    if ((UART${UART_INSTANCE_NUM}_REGS->DATA.UART_LSR & UART_DATA_LSR_TRANS_ERR_Msk) != 0U)
    {
        transmitComplete = true;
    }

    return transmitComplete;
}

<#if UART_OPERATING_MODE == "NON_BLOCKING">
void ${UART_INSTANCE_NAME}_ReadCallbackRegister( UART_CALLBACK callback, uintptr_t context )
{
    ${UART_INSTANCE_NAME?lower_case}Obj.rxCallback = callback;

    ${UART_INSTANCE_NAME?lower_case}Obj.rxContext = context;
}

bool ${UART_INSTANCE_NAME}_ReadIsBusy( void )
{
    return ${UART_INSTANCE_NAME?lower_case}Obj.rxBusyStatus;
}

size_t ${UART_INSTANCE_NAME}_ReadCountGet( void )
{
    return ${UART_INSTANCE_NAME?lower_case}Obj.rxProcessedSize;
}

bool ${UART_INSTANCE_NAME}_ReadAbort(void)
{
    if (${UART_INSTANCE_NAME?lower_case}Obj.rxBusyStatus == true)
    {
        /* Disable the Receive and Line Error interrupt */
        UART${UART_INSTANCE_NUM}_REGS->DATA.UART_IEN &= ~(UART_DATA_IEN_ERDAI_Msk | UART_DATA_IEN_ELSI_Msk);

        ${UART_INSTANCE_NAME?lower_case}Obj.rxBusyStatus = false;

        /* If required, application should read the num bytes processed prior to calling the read abort API */
        ${UART_INSTANCE_NAME?lower_case}Obj.rxSize = ${UART_INSTANCE_NAME?lower_case}Obj.rxProcessedSize = 0;
    }

    return true;
}

void ${UART_INSTANCE_NAME}_WriteCallbackRegister( UART_CALLBACK callback, uintptr_t context )
{
    ${UART_INSTANCE_NAME?lower_case}Obj.txCallback = callback;

    ${UART_INSTANCE_NAME?lower_case}Obj.txContext = context;
}

bool ${UART_INSTANCE_NAME}_WriteIsBusy( void )
{
    return ${UART_INSTANCE_NAME?lower_case}Obj.txBusyStatus;
}

size_t ${UART_INSTANCE_NAME}_WriteCountGet( void )
{
    return ${UART_INSTANCE_NAME?lower_case}Obj.txProcessedSize;
}

static void ${UART_INSTANCE_NAME}_ERROR_InterruptHandler (void)
{
    uint8_t lsr;

    lsr = UART${UART_INSTANCE_NUM}_REGS->DATA.UART_LSR;

    /* Check for overrun, parity and framing errors */
    lsr = (lsr & (UART_DATA_LSR_OVERRUN_Msk | UART_DATA_LSR_PE_Msk | UART_DATA_LSR_FRAME_ERR_Msk));
    ${UART_INSTANCE_NAME?lower_case}Obj.errors = lsr;

    if ((${UART_INSTANCE_NAME?lower_case}Obj.rxBusyStatus == true) && ((uint32_t)${UART_INSTANCE_NAME?lower_case}Obj.errors != 0U))
    {
        ${UART_INSTANCE_NAME?lower_case}Obj.rxBusyStatus = false;

        /* Disable the Receive and Line Error interrupt */
        UART${UART_INSTANCE_NUM}_REGS->DATA.UART_IEN &= ~(UART_DATA_IEN_ERDAI_Msk | UART_DATA_IEN_ELSI_Msk);

        if(${UART_INSTANCE_NAME?lower_case}Obj.rxCallback != NULL)
        {
            ${UART_INSTANCE_NAME?lower_case}Obj.rxCallback(${UART_INSTANCE_NAME?lower_case}Obj.rxContext);
        }
    }
}

static void ${UART_INSTANCE_NAME}_RX_InterruptHandler (void)
{
    uint8_t lsr;

    if(${UART_INSTANCE_NAME?lower_case}Obj.rxBusyStatus == true)
    {
        do
        {
            lsr = UART${UART_INSTANCE_NUM}_REGS->DATA.UART_LSR;

            /* Check for overrun, parity and framing errors */
            ${UART_INSTANCE_NAME?lower_case}Obj.errors = (lsr & (UART_DATA_LSR_OVERRUN_Msk | UART_DATA_LSR_PE_Msk | UART_DATA_LSR_FRAME_ERR_Msk));

            if (((lsr & UART_DATA_LSR_DATA_READY_Msk) != 0U) && ((uint32_t)${UART_INSTANCE_NAME?lower_case}Obj.errors == 0U))
            {
                ${UART_INSTANCE_NAME?lower_case}Obj.rxBuffer[${UART_INSTANCE_NAME?lower_case}Obj.rxProcessedSize] = UART${UART_INSTANCE_NUM}_REGS->DATA.UART_RX_DAT;
                ${UART_INSTANCE_NAME?lower_case}Obj.rxProcessedSize++;
            }
        }while(((lsr & UART_DATA_LSR_DATA_READY_Msk) != 0U) && ((uint32_t)${UART_INSTANCE_NAME?lower_case}Obj.errors == 0U) && (${UART_INSTANCE_NAME?lower_case}Obj.rxProcessedSize < ${UART_INSTANCE_NAME?lower_case}Obj.rxSize));

        /* Check if the buffer is done */
        if((${UART_INSTANCE_NAME?lower_case}Obj.rxProcessedSize >= ${UART_INSTANCE_NAME?lower_case}Obj.rxSize) || ((uint32_t)${UART_INSTANCE_NAME?lower_case}Obj.errors != 0U))
        {
            ${UART_INSTANCE_NAME?lower_case}Obj.rxBusyStatus = false;

            /* Disable the Receive and Line Error interrupt */
            UART${UART_INSTANCE_NUM}_REGS->DATA.UART_IEN &= ~(UART_DATA_IEN_ERDAI_Msk | UART_DATA_IEN_ELSI_Msk);

            if(${UART_INSTANCE_NAME?lower_case}Obj.rxCallback != NULL)
            {
                ${UART_INSTANCE_NAME?lower_case}Obj.rxCallback(${UART_INSTANCE_NAME?lower_case}Obj.rxContext);
            }
        }
    }
}

static void ${UART_INSTANCE_NAME}_TX_InterruptHandler (void)
{
    if(${UART_INSTANCE_NAME?lower_case}Obj.txBusyStatus == true)
    {
        UART${UART_INSTANCE_NUM}_REGS->DATA.UART_TX_DAT = ${UART_INSTANCE_NAME?lower_case}Obj.txBuffer[${UART_INSTANCE_NAME?lower_case}Obj.txProcessedSize];
        ${UART_INSTANCE_NAME?lower_case}Obj.txProcessedSize++;

        /* Check if the buffer is done */
        if(${UART_INSTANCE_NAME?lower_case}Obj.txProcessedSize >= ${UART_INSTANCE_NAME?lower_case}Obj.txSize)
        {
            ${UART_INSTANCE_NAME?lower_case}Obj.txBusyStatus = false;

            /* Disable the transmit interrupt, to avoid calling ISR continuously */
            UART${UART_INSTANCE_NUM}_REGS->DATA.UART_IEN &= ~(UART_DATA_IEN_ETHREI_Msk);

            if(${UART_INSTANCE_NAME?lower_case}Obj.txCallback != NULL)
            {
                ${UART_INSTANCE_NAME?lower_case}Obj.txCallback(${UART_INSTANCE_NAME?lower_case}Obj.txContext);
            }
        }
    }
}

void ${UART_NVIC_INTERRUPT_NAME}_InterruptHandler (void)
{
    uint8_t int_id = 0;

    int_id = ((UART${UART_INSTANCE_NUM}_REGS->DATA.UART_INT_ID & UART_DATA_INT_ID_INTID_Msk) >> UART_DATA_INT_ID_INTID_Pos);

    <#if UART_INTERRUPT_TYPE == "AGGREGATE">
    ECIA_GIRQSourceClear(ECIA_AGG_INT_SRC_UART${UART_INSTANCE_NUM});
    <#else>
    ECIA_GIRQSourceClear(ECIA_DIR_INT_SRC_UART${UART_INSTANCE_NUM});
    </#if>

    /* Interrupt type is Receiver Line Status */
    if (int_id == 0x03U)
    {
        ${UART_INSTANCE_NAME}_ERROR_InterruptHandler();
    }
    /* Interrupt type is Received data available */
    else if (int_id == 0x02U)
    {
        ${UART_INSTANCE_NAME}_RX_InterruptHandler();
    }
    /* Interrupt type is Transmit holding register empty */
    else if (int_id == 0x01U)
    {
        ${UART_INSTANCE_NAME}_TX_InterruptHandler();
    }
    else
    {
        /* Do nothing */
    }
}

<#else>
void ${UART_INSTANCE_NAME}_WriteByte(int data)
{
    while ((UART${UART_INSTANCE_NUM}_REGS->DATA.UART_LSR & UART_DATA_LSR_TRANS_EMPTY_Msk) == 0U)
    {
        /* Do nothing */
    }

    UART${UART_INSTANCE_NUM}_REGS->DATA.UART_TX_DAT = (uint8_t)data;
}

bool ${UART_INSTANCE_NAME}_TransmitterIsReady( void )
{
    bool transmitterReady = false;

    if ((UART${UART_INSTANCE_NUM}_REGS->DATA.UART_LSR & UART_DATA_LSR_TRANS_EMPTY_Msk) != 0U)
    {
        transmitterReady = true;
    }

    return transmitterReady;
}

int ${UART_INSTANCE_NAME}_ReadByte( void )
{
    return (int)UART${UART_INSTANCE_NUM}_REGS->DATA.UART_RX_DAT;
}

bool ${UART_INSTANCE_NAME}_ReceiverIsReady( void )
{
    bool receiverReady = false;

    if ((UART${UART_INSTANCE_NUM}_REGS->DATA.UART_LSR & UART_DATA_LSR_DATA_READY_Msk) != 0U)
    {
        receiverReady = true;
    }

    return receiverReady;
}
</#if>