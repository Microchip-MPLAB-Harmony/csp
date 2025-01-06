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

#include "device.h"
#include "plib_${UART_INSTANCE_NAME?lower_case}.h"
<#if core.CoreSysIntFile == true>
#include "interrupts.h"
</#if>

<#--Implementation-->
// *****************************************************************************
// *****************************************************************************
// Section: ${UART_INSTANCE_NAME} Implementation
// *****************************************************************************
// *****************************************************************************

<#if UART_INTERRUPT_MODE_ENABLE == true>
static volatile UART_OBJECT ${UART_INSTANCE_NAME?lower_case}Obj;
</#if>

static void ${UART_INSTANCE_NAME}_ErrorClear( void )
{
    UART_ERROR errors = UART_ERROR_NONE;
    uint8_t dummyData = 0u;

    errors = (UART_ERROR)(U${UART_INSTANCE_NUM}STA & (_U${UART_INSTANCE_NUM}STA_OERR_MASK | _U${UART_INSTANCE_NUM}STA_FERR_MASK | _U${UART_INSTANCE_NUM}STA_PERR_MASK));

    if(errors != UART_ERROR_NONE)
    {
        /* If it's a overrun error then clear it to flush FIFO */
        if((U${UART_INSTANCE_NUM}STA & _U${UART_INSTANCE_NUM}STA_OERR_MASK) != 0U)
        {
            U${UART_INSTANCE_NUM}STACLR = _U${UART_INSTANCE_NUM}STA_OERR_MASK;
        }

        /* Read existing error bytes from FIFO to clear parity and framing error flags */
        while((U${UART_INSTANCE_NUM}STA & _U${UART_INSTANCE_NUM}STA_URXDA_MASK) != 0U)
        {
            dummyData = (uint8_t)U${UART_INSTANCE_NUM}RXREG;
        }

<#if UART_INTERRUPT_MODE_ENABLE == true >
        /* Clear error interrupt flag */
        ${UART_FAULT_IFS_REG}CLR = _${UART_FAULT_IFS_REG}_U${UART_INSTANCE_NUM}EIF_MASK;

        /* Clear up the receive interrupt flag so that RX interrupt is not
         * triggered for error bytes */
        ${UART_FAULT_IFS_REG}CLR = _${UART_FAULT_IFS_REG}_U${UART_INSTANCE_NUM}RXIF_MASK;
</#if>
    }

    // Ignore the warning
    (void)dummyData;
}

void ${UART_INSTANCE_NAME}_Initialize( void )
{
    /* Set up UxMODE bits */
    /* STSEL  = ${UART_STOPBIT_SELECT} */
    /* PDSEL = ${UART_PDBIT_SELECT} */
    /* UEN = ${UART_UEN_SELECT} */

    U${UART_INSTANCE_NUM}MODE = 0x${UMODE_VALUE};

    /* Enable ${UART_INSTANCE_NAME} Receiver and Transmitter */
    U${UART_INSTANCE_NUM}STASET = (_U${UART_INSTANCE_NUM}STA_UTXEN_MASK | _U${UART_INSTANCE_NUM}STA_URXEN_MASK | _U${UART_INSTANCE_NUM}STA_UTXISEL1_MASK <#if UART_AUTOMATIC_ADDR_DETECTION_ENABLE == true> | _U${UART_INSTANCE_NUM}STA_ADM_EN_MASK | _U${UART_INSTANCE_NUM}STA_ADDEN_MASK | (${UART_9BIT_MODE_ADDR}UL << _U${UART_INSTANCE_NUM}STA_ADDR_POSITION)</#if>);

    /* BAUD Rate register Setup */
    U${UART_INSTANCE_NUM}BRG = ${BRG_VALUE};

<#if UART_INTERRUPT_MODE_ENABLE == true>
    /* Disable Interrupts */
    ${UART_FAULT_IEC_REG}CLR = _${UART_FAULT_IEC_REG}_U${UART_INSTANCE_NUM}EIE_MASK;

    ${UART_RX_IEC_REG}CLR = _${UART_RX_IEC_REG}_U${UART_INSTANCE_NUM}RXIE_MASK;

    ${UART_TX_IEC_REG}CLR = _${UART_TX_IEC_REG}_U${UART_INSTANCE_NUM}TXIE_MASK;

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
    U${UART_INSTANCE_NUM}MODESET = _U${UART_INSTANCE_NUM}MODE_ON_MASK;
}

bool ${UART_INSTANCE_NAME}_SerialSetup( UART_SERIAL_SETUP *setup, uint32_t srcClkFreq )
{
    bool status = false;
    uint32_t baud;
    uint32_t status_ctrl;
    uint32_t uxbrg = 0;

<#if UART_INTERRUPT_MODE_ENABLE == true>
    if(${UART_INSTANCE_NAME?lower_case}Obj.rxBusyStatus == true)
    {
        /* Transaction is in progress, so return without updating settings */
        return status;
    }
    if (${UART_INSTANCE_NAME?lower_case}Obj.txBusyStatus == true)
    {
        /* Transaction is in progress, so return without updating settings */
        return status;
    }

</#if>
    if (setup != NULL)
    {
        baud = setup->baudRate;

        if ((baud == 0U) || ((setup->dataWidth == UART_DATA_9_BIT) && (setup->parity != UART_PARITY_NONE)))
        {
            return status;
        }

        if(srcClkFreq == 0U)
        {
            srcClkFreq = ${UART_INSTANCE_NAME}_FrequencyGet();
        }

        /* Calculate BRG value */
<#if UART_BRGH?number == 0>
        uxbrg = (((srcClkFreq >> 4) + (baud >> 1)) / baud);
<#else>
        uxbrg = (((srcClkFreq >> 2) + (baud >> 1)) / baud);
</#if>
        /* Check if the baud value can be set with low baud settings */
        if (uxbrg < 1U)
        {
            return status;
        }

        uxbrg -= 1U;

        if (uxbrg > UINT16_MAX)
        {
            return status;
        }

        /* Turn OFF ${UART_INSTANCE_NAME}. Save UTXEN, URXEN and UTXBRK bits as these are cleared upon disabling UART */

        status_ctrl = U${UART_INSTANCE_NUM}STA & (_U${UART_INSTANCE_NUM}STA_UTXEN_MASK | _U${UART_INSTANCE_NUM}STA_URXEN_MASK | _U${UART_INSTANCE_NUM}STA_UTXBRK_MASK);

        U${UART_INSTANCE_NUM}MODECLR = _U${UART_INSTANCE_NUM}MODE_ON_MASK;

        if(setup->dataWidth == UART_DATA_9_BIT)
        {
            /* Configure ${UART_INSTANCE_NAME} mode */
            U${UART_INSTANCE_NUM}MODE = (U${UART_INSTANCE_NUM}MODE & (~_U${UART_INSTANCE_NUM}MODE_PDSEL_MASK)) | setup->dataWidth;
        }
        else
        {
            /* Configure ${UART_INSTANCE_NAME} mode */
            U${UART_INSTANCE_NUM}MODE = (U${UART_INSTANCE_NUM}MODE & (~_U${UART_INSTANCE_NUM}MODE_PDSEL_MASK)) | setup->parity;
        }

        /* Configure ${UART_INSTANCE_NAME} mode */
        U${UART_INSTANCE_NUM}MODE = (U${UART_INSTANCE_NUM}MODE & (~_U${UART_INSTANCE_NUM}MODE_STSEL_MASK)) | setup->stopBits;

        /* Configure ${UART_INSTANCE_NAME} Baud Rate */
        U${UART_INSTANCE_NUM}BRG = uxbrg;

        U${UART_INSTANCE_NUM}MODESET = _U${UART_INSTANCE_NUM}MODE_ON_MASK;

        /* Restore UTXEN, URXEN and UTXBRK bits. */
        U${UART_INSTANCE_NUM}STASET = status_ctrl;

        status = true;
    }

    return status;
}

bool ${UART_INSTANCE_NAME}_AutoBaudQuery( void )
{
    bool autobaudqcheck = false;
    if((U${UART_INSTANCE_NUM}MODE & _U${UART_INSTANCE_NUM}MODE_ABAUD_MASK) != 0U)
    {

       autobaudqcheck = true;
    }
    return autobaudqcheck;
}

void ${UART_INSTANCE_NAME}_AutoBaudSet( bool enable )
{
    if( enable == true )
    {
        U${UART_INSTANCE_NUM}MODESET = _U${UART_INSTANCE_NUM}MODE_ABAUD_MASK;
    }

    /* Turning off ABAUD if it was on can lead to unpredictable behavior, so that
       direction of control is not allowed in this function.                      */
}

bool ${UART_INSTANCE_NAME}_Read(void* buffer, const size_t size )
{
    bool status = false;
<#if UART_INTERRUPT_MODE_ENABLE == false>
    uint32_t errorStatus = 0;
    size_t processedSize = 0;
</#if>

    if(buffer != NULL)
    {
<#if UART_INTERRUPT_MODE_ENABLE == false>

        /* Clear error flags and flush out error data that may have been received when no active request was pending */
        ${UART_INSTANCE_NAME}_ErrorClear();

        while( size > processedSize )
        {
            while((U${UART_INSTANCE_NUM}STA & _U${UART_INSTANCE_NUM}STA_URXDA_MASK) == 0U)
            {
                /* Wait for receiver to be ready */
            }

            /* Error status */
            errorStatus = (U${UART_INSTANCE_NUM}STA & (_U${UART_INSTANCE_NUM}STA_OERR_MASK | _U${UART_INSTANCE_NUM}STA_FERR_MASK | _U${UART_INSTANCE_NUM}STA_PERR_MASK));

            if(errorStatus != 0U)
            {
                break;
            }
<#if UART_AUTOMATIC_ADDR_DETECTION_ENABLE == true>
            /* 8-bit mode */
            ((uint8_t*)(buffer))[processedSize] = (uint8_t)(U${UART_INSTANCE_NUM}RXREG);
<#else>
            if (( U${UART_INSTANCE_NUM}MODE & (_U${UART_INSTANCE_NUM}MODE_PDSEL0_MASK | _U${UART_INSTANCE_NUM}MODE_PDSEL1_MASK)) == (_U${UART_INSTANCE_NUM}MODE_PDSEL0_MASK | _U${UART_INSTANCE_NUM}MODE_PDSEL1_MASK))
            {
                /* 9-bit mode */
                ((uint16_t*)(buffer))[processedSize] = (uint16_t)(U${UART_INSTANCE_NUM}RXREG );
            }
            else
            {
                /* 8-bit mode */
                ((uint8_t*)(buffer))[processedSize] = (uint8_t)(U${UART_INSTANCE_NUM}RXREG);
            }
</#if>

            processedSize++;
        }

        if(size == processedSize)
        {
            status = true;
        }
<#else>
        /* Check if receive request is in progress */
        if(${UART_INSTANCE_NAME?lower_case}Obj.rxBusyStatus == false)
        {
            /* Clear error flags and flush out error data that may have been received when no active request was pending */
            ${UART_INSTANCE_NAME}_ErrorClear();

            ${UART_INSTANCE_NAME?lower_case}Obj.rxBuffer = buffer;
            ${UART_INSTANCE_NAME?lower_case}Obj.rxSize = size;
            ${UART_INSTANCE_NAME?lower_case}Obj.rxProcessedSize = 0;
            ${UART_INSTANCE_NAME?lower_case}Obj.rxBusyStatus = true;
            ${UART_INSTANCE_NAME?lower_case}Obj.errors = UART_ERROR_NONE;
            status = true;

            /* Enable ${UART_INSTANCE_NAME}_FAULT Interrupt */
            ${UART_FAULT_IEC_REG}SET = _${UART_FAULT_IEC_REG}_U${UART_INSTANCE_NUM}EIE_MASK;

            /* Enable ${UART_INSTANCE_NAME}_RX Interrupt */
            ${UART_RX_IEC_REG}SET = _${UART_RX_IEC_REG}_U${UART_INSTANCE_NUM}RXIE_MASK;
        }
</#if>
    }

    return status;
}

bool ${UART_INSTANCE_NAME}_Write( void* buffer, const size_t size )
{
    bool status = false;
<#if UART_INTERRUPT_MODE_ENABLE == false>
    size_t processedSize = 0;
</#if>

    if(buffer != NULL)
    {
<#if UART_INTERRUPT_MODE_ENABLE == false>
        while( size > processedSize )
        {
            /* Wait while TX buffer is full */
            while ((U${UART_INSTANCE_NUM}STA & _U${UART_INSTANCE_NUM}STA_UTXBF_MASK) != 0U)
            {
                /* Wait for transmitter to be ready */
            }

            if (( U${UART_INSTANCE_NUM}MODE & (_U${UART_INSTANCE_NUM}MODE_PDSEL0_MASK | _U${UART_INSTANCE_NUM}MODE_PDSEL1_MASK)) == (_U${UART_INSTANCE_NUM}MODE_PDSEL0_MASK | _U${UART_INSTANCE_NUM}MODE_PDSEL1_MASK))
            {
                /* 9-bit mode */
                U${UART_INSTANCE_NUM}TXREG = ((uint16_t*)(buffer))[processedSize];
            }
            else
            {
                /* 8-bit mode */
                U${UART_INSTANCE_NUM}TXREG = ((uint8_t*)(buffer))[processedSize];
            }

            processedSize++;
        }

        status = true;
<#else>
        /* Check if transmit request is in progress */
        if(${UART_INSTANCE_NAME?lower_case}Obj.txBusyStatus == false)
        {
            ${UART_INSTANCE_NAME?lower_case}Obj.txBuffer = buffer;
            ${UART_INSTANCE_NAME?lower_case}Obj.txSize = size;
            ${UART_INSTANCE_NAME?lower_case}Obj.txProcessedSize = 0;
            ${UART_INSTANCE_NAME?lower_case}Obj.txBusyStatus = true;
            status = true;

            size_t txProcessedSize = ${UART_INSTANCE_NAME?lower_case}Obj.txProcessedSize;
            size_t txSize = ${UART_INSTANCE_NAME?lower_case}Obj.txSize;

            /* Initiate the transfer by writing as many bytes as we can */
            while(((U${UART_INSTANCE_NUM}STA & _U${UART_INSTANCE_NUM}STA_UTXBF_MASK) == 0U) && (txSize > txProcessedSize) )
            {
                if (( U${UART_INSTANCE_NUM}MODE & (_U${UART_INSTANCE_NUM}MODE_PDSEL0_MASK | _U${UART_INSTANCE_NUM}MODE_PDSEL1_MASK)) == (_U${UART_INSTANCE_NUM}MODE_PDSEL0_MASK | _U${UART_INSTANCE_NUM}MODE_PDSEL1_MASK))
                {
                    /* 9-bit mode */
                    U${UART_INSTANCE_NUM}TXREG = ((uint16_t*)${UART_INSTANCE_NAME?lower_case}Obj.txBuffer)[txProcessedSize];
                    txProcessedSize++;
                }
                else
                {
                    /* 8-bit mode */
                    U${UART_INSTANCE_NUM}TXREG = ((uint8_t*)${UART_INSTANCE_NAME?lower_case}Obj.txBuffer)[txProcessedSize];
                    txProcessedSize++;
                }
            }

            ${UART_INSTANCE_NAME?lower_case}Obj.txProcessedSize = txProcessedSize;

            ${UART_TX_IEC_REG}SET = _${UART_TX_IEC_REG}_U${UART_INSTANCE_NUM}TXIE_MASK;
        }
</#if>
    }

    return status;
}

<#if UART_INTERRUPT_MODE_ENABLE == true>
UART_ERROR ${UART_INSTANCE_NAME}_ErrorGet( void )
{
    UART_ERROR errors = ${UART_INSTANCE_NAME?lower_case}Obj.errors;

    ${UART_INSTANCE_NAME?lower_case}Obj.errors = UART_ERROR_NONE;

    /* All errors are cleared, but send the previous error state */
    return errors;
}
<#else>
UART_ERROR ${UART_INSTANCE_NAME}_ErrorGet( void )
{
    UART_ERROR errors = UART_ERROR_NONE;

    errors = (U${UART_INSTANCE_NUM}STA & (_U${UART_INSTANCE_NUM}STA_OERR_MASK | _U${UART_INSTANCE_NUM}STA_FERR_MASK | _U${UART_INSTANCE_NUM}STA_PERR_MASK));

    if(errors != UART_ERROR_NONE)
    {
        ${UART_INSTANCE_NAME}_ErrorClear();
    }

    /* All errors are cleared, but send the previous error state */
    return errors;
}
</#if>

<#if UART_INTERRUPT_MODE_ENABLE == true>
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
        /* Disable the fault interrupt */
        ${UART_FAULT_IEC_REG}CLR = _${UART_FAULT_IEC_REG}_U${UART_INSTANCE_NUM}EIE_MASK;

        /* Disable the receive interrupt */
        ${UART_RX_IEC_REG}CLR = _${UART_RX_IEC_REG}_U${UART_INSTANCE_NUM}RXIE_MASK;

        ${UART_INSTANCE_NAME?lower_case}Obj.rxBusyStatus = false;

        /* If required application should read the num bytes processed prior to calling the read abort API */
        ${UART_INSTANCE_NAME?lower_case}Obj.rxSize = 0U;
        ${UART_INSTANCE_NAME?lower_case}Obj.rxProcessedSize = 0U;
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

<#if UART_INTERRUPT_COUNT == 1>
static void __attribute__((used)) ${UART_INSTANCE_NAME}_FAULT_InterruptHandler (void)
<#else>
void __attribute__((used)) ${UART_INSTANCE_NAME}_FAULT_InterruptHandler (void)
</#if>
{
    /* Save the error to be reported later */
    ${UART_INSTANCE_NAME?lower_case}Obj.errors = (U${UART_INSTANCE_NUM}STA & (_U${UART_INSTANCE_NUM}STA_OERR_MASK | _U${UART_INSTANCE_NUM}STA_FERR_MASK | _U${UART_INSTANCE_NUM}STA_PERR_MASK));

    /* Disable the fault interrupt */
    ${UART_FAULT_IEC_REG}CLR = _${UART_FAULT_IEC_REG}_U${UART_INSTANCE_NUM}EIE_MASK;

    /* Disable the receive interrupt */
    ${UART_RX_IEC_REG}CLR = _${UART_RX_IEC_REG}_U${UART_INSTANCE_NUM}RXIE_MASK;

    /* Clear rx status */
    ${UART_INSTANCE_NAME?lower_case}Obj.rxBusyStatus = false;

    ${UART_INSTANCE_NAME}_ErrorClear();

    /* Client must call UARTx_ErrorGet() function to get the errors */
    if( ${UART_INSTANCE_NAME?lower_case}Obj.rxCallback != NULL )
    {
        uintptr_t rxContext = ${UART_INSTANCE_NAME?lower_case}Obj.rxContext;

        ${UART_INSTANCE_NAME?lower_case}Obj.rxCallback(rxContext);
    }
}

<#if UART_INTERRUPT_COUNT == 1>
static void __attribute__((used)) ${UART_INSTANCE_NAME}_RX_InterruptHandler (void)
<#else>
void __attribute__((used)) ${UART_INSTANCE_NAME}_RX_InterruptHandler (void)
</#if>
{
    if(${UART_INSTANCE_NAME?lower_case}Obj.rxBusyStatus == true)
    {
        size_t rxSize = ${UART_INSTANCE_NAME?lower_case}Obj.rxSize;
        size_t rxProcessedSize = ${UART_INSTANCE_NAME?lower_case}Obj.rxProcessedSize;

        while((_U${UART_INSTANCE_NUM}STA_URXDA_MASK == (U${UART_INSTANCE_NUM}STA & _U${UART_INSTANCE_NUM}STA_URXDA_MASK)) && (rxSize > rxProcessedSize) )
        {
<#if UART_AUTOMATIC_ADDR_DETECTION_ENABLE == true>
            /* 8-bit mode */
            ${UART_INSTANCE_NAME?lower_case}Obj.rxBuffer[rxProcessedSize] = (uint8_t )(U${UART_INSTANCE_NUM}RXREG);
<#else>
            if (( U${UART_INSTANCE_NUM}MODE & (_U${UART_INSTANCE_NUM}MODE_PDSEL0_MASK | _U${UART_INSTANCE_NUM}MODE_PDSEL1_MASK)) == (_U${UART_INSTANCE_NUM}MODE_PDSEL0_MASK | _U${UART_INSTANCE_NUM}MODE_PDSEL1_MASK))
            {
                /* 9-bit mode */
                ((uint16_t*)${UART_INSTANCE_NAME?lower_case}Obj.rxBuffer)[rxProcessedSize] = (uint16_t)(U${UART_INSTANCE_NUM}RXREG);
            }
            else
            {
                /* 8-bit mode */
                ((uint8_t*)${UART_INSTANCE_NAME?lower_case}Obj.rxBuffer)[rxProcessedSize] = (uint8_t)(U${UART_INSTANCE_NUM}RXREG);
            }
</#if>
            rxProcessedSize++;
        }

        ${UART_INSTANCE_NAME?lower_case}Obj.rxProcessedSize = rxProcessedSize;

        /* Clear ${UART_INSTANCE_NAME} RX Interrupt flag */
        ${UART_RX_IFS_REG}CLR = _${UART_RX_IFS_REG}_U${UART_INSTANCE_NUM}RXIF_MASK;

        /* Check if the buffer is done */
        if(${UART_INSTANCE_NAME?lower_case}Obj.rxProcessedSize >= rxSize)
        {
            ${UART_INSTANCE_NAME?lower_case}Obj.rxBusyStatus = false;

            /* Disable the fault interrupt */
            ${UART_FAULT_IEC_REG}CLR = _${UART_FAULT_IEC_REG}_U${UART_INSTANCE_NUM}EIE_MASK;

            /* Disable the receive interrupt */
            ${UART_RX_IEC_REG}CLR = _${UART_RX_IEC_REG}_U${UART_INSTANCE_NUM}RXIE_MASK;


            if(${UART_INSTANCE_NAME?lower_case}Obj.rxCallback != NULL)
            {
                uintptr_t rxContext = ${UART_INSTANCE_NAME?lower_case}Obj.rxContext;

                ${UART_INSTANCE_NAME?lower_case}Obj.rxCallback(rxContext);
            }
        }
    }
    else
    {
        /* Nothing to process */
    }
}

<#if UART_INTERRUPT_COUNT == 1>
static void __attribute__((used)) ${UART_INSTANCE_NAME}_TX_InterruptHandler (void)
<#else>
void __attribute__((used)) ${UART_INSTANCE_NAME}_TX_InterruptHandler (void)
</#if>
{
    if(${UART_INSTANCE_NAME?lower_case}Obj.txBusyStatus == true)
    {
        size_t txSize = ${UART_INSTANCE_NAME?lower_case}Obj.txSize;
        size_t txProcessedSize = ${UART_INSTANCE_NAME?lower_case}Obj.txProcessedSize;

        while(((U${UART_INSTANCE_NUM}STA & _U${UART_INSTANCE_NUM}STA_UTXBF_MASK) == 0U) && (txSize > txProcessedSize) )
        {
            if (( U${UART_INSTANCE_NUM}MODE & (_U${UART_INSTANCE_NUM}MODE_PDSEL0_MASK | _U${UART_INSTANCE_NUM}MODE_PDSEL1_MASK)) == (_U${UART_INSTANCE_NUM}MODE_PDSEL0_MASK | _U${UART_INSTANCE_NUM}MODE_PDSEL1_MASK))
            {
                /* 9-bit mode */
                U${UART_INSTANCE_NUM}TXREG = ((uint16_t*)${UART_INSTANCE_NAME?lower_case}Obj.txBuffer)[txProcessedSize];
            }
            else
            {
                /* 8-bit mode */
                U${UART_INSTANCE_NUM}TXREG = ((uint8_t*)${UART_INSTANCE_NAME?lower_case}Obj.txBuffer)[txProcessedSize];
            }
            txProcessedSize++;
        }

        ${UART_INSTANCE_NAME?lower_case}Obj.txProcessedSize = txProcessedSize;

        /* Clear ${UART_INSTANCE_NAME}TX Interrupt flag */
        ${UART_TX_IFS_REG}CLR = _${UART_TX_IFS_REG}_U${UART_INSTANCE_NUM}TXIF_MASK;

        /* Check if the buffer is done */
        if(${UART_INSTANCE_NAME?lower_case}Obj.txProcessedSize >= txSize)
        {
            ${UART_INSTANCE_NAME?lower_case}Obj.txBusyStatus = false;

            /* Disable the transmit interrupt, to avoid calling ISR continuously */
            ${UART_TX_IEC_REG}CLR = _${UART_TX_IEC_REG}_U${UART_INSTANCE_NUM}TXIE_MASK;

            if(${UART_INSTANCE_NAME?lower_case}Obj.txCallback != NULL)
            {
                uintptr_t txContext = ${UART_INSTANCE_NAME?lower_case}Obj.txContext;

                ${UART_INSTANCE_NAME?lower_case}Obj.txCallback(txContext);
            }
        }
    }
    else
    {
        // Nothing to process
        ;
    }
}

<#if UART_INTERRUPT_COUNT == 1>
void __attribute__((used)) UART_${UART_INSTANCE_NUM}_InterruptHandler (void)
{
    /* As per 13_5_violation using this temp variable */
    uint32_t temp = 0;

    temp = ${UART_FAULT_IEC_REG};
    /* Call Error handler if Error interrupt flag is set */
    if (((${UART_FAULT_IFS_REG} & _${UART_FAULT_IFS_REG}_U${UART_INSTANCE_NUM}EIF_MASK) != 0U) && ((temp & _${UART_FAULT_IEC_REG}_U${UART_INSTANCE_NUM}EIE_MASK) != 0U))
    {
        ${UART_INSTANCE_NAME}_FAULT_InterruptHandler();
    }
    temp = ${UART_FAULT_IEC_REG};
    /* Call RX handler if RX interrupt flag is set */
    if (((${UART_RX_IFS_REG} & _${UART_RX_IFS_REG}_U${UART_INSTANCE_NUM}RXIF_MASK) != 0U) && ((temp & _${UART_RX_IEC_REG}_U${UART_INSTANCE_NUM}RXIE_MASK) != 0U))
    {
        ${UART_INSTANCE_NAME}_RX_InterruptHandler();
    }
    temp = ${UART_FAULT_IEC_REG};
    /* Call TX handler if TX interrupt flag is set */
    if (((${UART_TX_IFS_REG} & _${UART_TX_IFS_REG}_U${UART_INSTANCE_NUM}TXIF_MASK) != 0U) && ((temp & _${UART_TX_IEC_REG}_U${UART_INSTANCE_NUM}TXIE_MASK) != 0U))
    {
        ${UART_INSTANCE_NAME}_TX_InterruptHandler();
    }
}
</#if>

<#else>
void ${UART_INSTANCE_NAME}_WriteByte(int data)
{
    while (((U${UART_INSTANCE_NUM}STA & _U${UART_INSTANCE_NUM}STA_UTXBF_MASK) != 0U))
    {
        /* Do Nothing */
    }

    U${UART_INSTANCE_NUM}TXREG = (uint32_t)data;
}

bool ${UART_INSTANCE_NAME}_TransmitterIsReady( void )
{
    bool status = false;

    if((U${UART_INSTANCE_NUM}STA & _U${UART_INSTANCE_NUM}STA_UTXBF_MASK) == 0U)
    {
        status = true;
    }

    return status;
}

int ${UART_INSTANCE_NAME}_ReadByte( void )
{
    return (int)(U${UART_INSTANCE_NUM}RXREG);
}

bool ${UART_INSTANCE_NAME}_ReceiverIsReady( void )
{
    bool status = false;

    if(_U${UART_INSTANCE_NUM}STA_URXDA_MASK == (U${UART_INSTANCE_NUM}STA & _U${UART_INSTANCE_NUM}STA_URXDA_MASK))
    {
        status = true;
    }

    return status;
}
</#if>

bool ${UART_INSTANCE_NAME}_TransmitComplete( void )
{
    bool transmitComplete = false;

    if((U${UART_INSTANCE_NUM}STA & _U${UART_INSTANCE_NUM}STA_TRMT_MASK) != 0U)
    {
        transmitComplete = true;
    }

    return transmitComplete;
}