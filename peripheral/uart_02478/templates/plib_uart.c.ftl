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

<#--Implementation-->
// *****************************************************************************
// *****************************************************************************
// Section: ${UART_INSTANCE_NAME} Implementation
// *****************************************************************************
// *****************************************************************************

<#if USART_INTERRUPT_MODE == true>
UART_OBJECT ${UART_INSTANCE_NAME?lower_case}Obj;
</#if>

void static ${UART_INSTANCE_NAME}_ErrorClear( void )
{
    /* rxBufferLen = (FIFO level + RX register) */
    uint8_t rxBufferLen = UART_RXFIFO_DEPTH;
    uint8_t dummyData = 0u;

    /* If it's a overrun error then clear it to flush FIFO */
    if(U${UART_INSTANCE_NUM}STA & _U${UART_INSTANCE_NUM}STA_OERR_MASK)
    {
        U${UART_INSTANCE_NUM}STACLR = _U${UART_INSTANCE_NUM}STA_OERR_MASK;
    }

    /* Read existing error bytes from FIFO to clear parity and framing error flags */
    while(U${UART_INSTANCE_NUM}STA & (_U${UART_INSTANCE_NUM}STA_FERR_MASK | _U${UART_INSTANCE_NUM}STA_PERR_MASK))
    {
        dummyData = (uint8_t )(U${UART_INSTANCE_NUM}RXREG );
        rxBufferLen--;

        /* Try to flush error bytes for one full FIFO and exit instead of
         * blocking here if more error bytes are received */
        if(rxBufferLen == 0u)
        {
            break;
        }
    }

    // Ignore the warning
    (void)dummyData;

<#if USART_INTERRUPT_MODE == true >
    /* Clear error interrupt flag */
    ${UART_FAULT_IFS_REG}CLR = _${UART_FAULT_IFS_REG}_U${UART_INSTANCE_NUM}EIF_MASK;

    /* Clear up the receive interrupt flag so that RX interrupt is not
     * triggered for error bytes */
    ${UART_FAULT_IFS_REG}CLR = _${UART_FAULT_IFS_REG}_U${UART_INSTANCE_NUM}RXIF_MASK;

</#if>
    return;
}

void ${UART_INSTANCE_NAME}_Initialize( void )
{
    /* Set up UxMODE bits */
    /* STSEL  = ${UART_STSEL}*/
    /* PDSEL = ${UART_PDSEL} */
    /* BRGH = ${UART_BRGH} */
    /* RXINV = ${UART_RXINV} */
    /* ABAUD = ${UART_ABAUD} */
    /* LPBACK = ${UART_LPBACK} */
    /* WAKE = ${UART_WAKE} */
    /* SIDL = ${UART_SIDL} */
    /* RUNOVF = ${UART_RUNOVF} */
    /* CLKSEL = ${UART_CLKSEL} */
    /* SLPEN = ${UART_SLPEN} */
    U${UART_INSTANCE_NUM}MODE = 0x${UMODE_VALUE};

<#if USART_INTERRUPT_MODE == true>
    /* Enable ${UART_INSTANCE_NAME} Receiver, Transmitter and TX Interrupt selection */
    U${UART_INSTANCE_NUM}STASET = (_U${UART_INSTANCE_NUM}STA_UTXEN_MASK | _U${UART_INSTANCE_NUM}STA_URXEN_MASK | _U${UART_INSTANCE_NUM}STA_UTXISEL0_MASK);
<#else>
    /* Enable ${UART_INSTANCE_NAME} Receiver and Transmitter */
    U${UART_INSTANCE_NUM}STASET = (_U${UART_INSTANCE_NUM}STA_UTXEN_MASK | _U${UART_INSTANCE_NUM}STA_URXEN_MASK);
</#if>

    /* BAUD Rate register Setup */
    U${UART_INSTANCE_NUM}BRG = ${BRG_VALUE};

<#if USART_INTERRUPT_MODE == true>
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

</#if>
    /* Turn ON ${UART_INSTANCE_NAME} */
    U${UART_INSTANCE_NUM}MODESET = _U${UART_INSTANCE_NUM}MODE_ON_MASK;
}

bool ${UART_INSTANCE_NAME}_SerialSetup( UART_SERIAL_SETUP *setup, uint32_t srcClkFreq )
{
    bool status = false;
    uint32_t baud = setup->baudRate;
    uint32_t brgValHigh = 0;
    uint32_t brgValLow = 0;
    uint32_t brgVal = 0;
    uint32_t uartMode;

<#if USART_INTERRUPT_MODE == true>
    if((${UART_INSTANCE_NAME?lower_case}Obj.rxBusyStatus == true) || (${UART_INSTANCE_NAME?lower_case}Obj.txBusyStatus == true))
    {
        /* Transaction is in progress, so return without updating settings */
        return status;
    }

</#if>
    if (setup != NULL)
    {
        /* Turn OFF ${UART_INSTANCE_NAME} */
        U${UART_INSTANCE_NUM}MODECLR = _U${UART_INSTANCE_NUM}MODE_ON_MASK;

        if(srcClkFreq == 0)
        {
            srcClkFreq = ${UART_INSTANCE_NAME}_FrequencyGet();
        }

        /* Calculate BRG value */
        brgValLow = ((srcClkFreq / baud) >> 4) - 1;
        brgValHigh = ((srcClkFreq / baud) >> 2) - 1;

        /* Check if the baud value can be set with low baud settings */
        if((brgValHigh >= 0) && (brgValHigh <= UINT16_MAX))
        {
            brgVal =  (((srcClkFreq >> 2) + (baud >> 1)) / baud ) - 1;
            U${UART_INSTANCE_NUM}MODESET = _U${UART_INSTANCE_NUM}MODE_BRGH_MASK;
        }
        else if ((brgValLow >= 0) && (brgValLow <= UINT16_MAX))
        {
            brgVal = ( ((srcClkFreq >> 4) + (baud >> 1)) / baud ) - 1;
            U${UART_INSTANCE_NUM}MODECLR = _U${UART_INSTANCE_NUM}MODE_BRGH_MASK;
        }
        else
        {
            return status;
        }

        if(setup->dataWidth == UART_DATA_9_BIT)
        {
            if(setup->parity != UART_PARITY_NONE)
            {
               return status;
            }
            else
            {
               /* Configure ${UART_INSTANCE_NAME} mode */
               uartMode = U${UART_INSTANCE_NUM}MODE;
               uartMode &= ~_U${UART_INSTANCE_NUM}MODE_PDSEL_MASK;
               U${UART_INSTANCE_NUM}MODE = uartMode | setup->dataWidth;
            }
        }
        else
        {
            /* Configure ${UART_INSTANCE_NAME} mode */
            uartMode = U${UART_INSTANCE_NUM}MODE;
            uartMode &= ~_U${UART_INSTANCE_NUM}MODE_PDSEL_MASK;
            U${UART_INSTANCE_NUM}MODE = uartMode | setup->parity ;
        }

        /* Configure ${UART_INSTANCE_NAME} mode */
        uartMode = U${UART_INSTANCE_NUM}MODE;
        uartMode &= ~_U${UART_INSTANCE_NUM}MODE_STSEL_MASK;
        U${UART_INSTANCE_NUM}MODE = uartMode | setup->stopBits ;

        /* Configure ${UART_INSTANCE_NAME} Baud Rate */
        U${UART_INSTANCE_NUM}BRG = brgVal;

        U${UART_INSTANCE_NUM}MODESET = _U${UART_INSTANCE_NUM}MODE_ON_MASK;

        status = true;
    }

    return status;
}

bool ${UART_INSTANCE_NAME}_Read( void *buffer, const size_t size )
{
    bool status = false;
    uint8_t * lBuffer = (uint8_t *)buffer;
<#if USART_INTERRUPT_MODE == false>
    uint32_t errorStatus = 0;
    size_t processedSize = 0;
</#if>

    if(lBuffer != NULL)
    {
<#if USART_INTERRUPT_MODE == false>
        /* Clear errors before submitting the request.
         * ErrorGet clears errors internally. */
        ${UART_INSTANCE_NAME}_ErrorGet();

        while( size > processedSize )
        {
            /* Error status */
            errorStatus = (U${UART_INSTANCE_NUM}STA & (_U${UART_INSTANCE_NUM}STA_OERR_MASK | _U${UART_INSTANCE_NUM}STA_FERR_MASK | _U${UART_INSTANCE_NUM}STA_PERR_MASK));

            if(errorStatus != 0)
            {
                break;
            }

            /* Receiver buffer has data */
            if((U${UART_INSTANCE_NUM}STA & _U${UART_INSTANCE_NUM}STA_URXDA_MASK) == _U${UART_INSTANCE_NUM}STA_URXDA_MASK)
            {
                *lBuffer++ = (U${UART_INSTANCE_NUM}RXREG );
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
            /* Clear errors before submitting the request.
             * ErrorGet clears errors internally. */
            ${UART_INSTANCE_NAME}_ErrorGet();

            ${UART_INSTANCE_NAME?lower_case}Obj.rxBuffer = lBuffer;
            ${UART_INSTANCE_NAME?lower_case}Obj.rxSize = size;
            ${UART_INSTANCE_NAME?lower_case}Obj.rxProcessedSize = 0;
            ${UART_INSTANCE_NAME?lower_case}Obj.rxBusyStatus = true;
            status = true;
        }

        /* Enable ${UART_INSTANCE_NAME}_FAULT Interrupt */
        ${UART_FAULT_IEC_REG}SET = _${UART_FAULT_IEC_REG}_U${UART_INSTANCE_NUM}EIE_MASK;

        /* Enable ${UART_INSTANCE_NAME}_RX Interrupt */
        ${UART_RX_IEC_REG}SET = _${UART_RX_IEC_REG}_U${UART_INSTANCE_NUM}RXIE_MASK;
</#if>
    }

    return status;
}

bool ${UART_INSTANCE_NAME}_Write( void *buffer, const size_t size )
{
    bool status = false;
    uint8_t * lBuffer = (uint8_t *)buffer;
<#if USART_INTERRUPT_MODE == false>
    size_t processedSize = 0;
</#if>

    if(lBuffer != NULL)
    {
<#if USART_INTERRUPT_MODE == false>
        while( size > processedSize )
        {
            if(!(U${UART_INSTANCE_NUM}STA & _U${UART_INSTANCE_NUM}STA_UTXBF_MASK))
            {
                U${UART_INSTANCE_NUM}TXREG = *lBuffer++;
                processedSize++;
            }
        }

        status = true;
<#else>
        /* Check if transmit request is in progress */
        if(${UART_INSTANCE_NAME?lower_case}Obj.txBusyStatus == false)
        {
            ${UART_INSTANCE_NAME?lower_case}Obj.txBuffer = lBuffer;
            ${UART_INSTANCE_NAME?lower_case}Obj.txSize = size;
            ${UART_INSTANCE_NAME?lower_case}Obj.txProcessedSize = 0;
            ${UART_INSTANCE_NAME?lower_case}Obj.txBusyStatus = true;
            status = true;

            /* Initiate the transfer by sending first byte */
            if(!(U${UART_INSTANCE_NUM}STA & _U${UART_INSTANCE_NUM}STA_UTXBF_MASK))
            {
                U${UART_INSTANCE_NUM}TXREG = *lBuffer;
                ${UART_INSTANCE_NAME?lower_case}Obj.txProcessedSize++;
            }

            ${UART_TX_IEC_REG}SET = _${UART_TX_IEC_REG}_U${UART_INSTANCE_NUM}TXIE_MASK;
        }
</#if>
    }

    return status;
}

UART_ERROR ${UART_INSTANCE_NAME}_ErrorGet( void )
{
    UART_ERROR errors = UART_ERROR_NONE;
    uint32_t status = U${UART_INSTANCE_NUM}STA;

    errors = (UART_ERROR)(status & (_U${UART_INSTANCE_NUM}STA_OERR_MASK | _U${UART_INSTANCE_NUM}STA_FERR_MASK | _U${UART_INSTANCE_NUM}STA_PERR_MASK));

    if(errors != UART_ERROR_NONE)
    {
        ${UART_INSTANCE_NAME}_ErrorClear();
    }

    /* All errors are cleared, but send the previous error state */
    return errors;
}

<#if USART_INTERRUPT_MODE == true>

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
static void ${UART_INSTANCE_NAME}_FAULT_InterruptHandler (void)
<#else>
void ${UART_INSTANCE_NAME}_FAULT_InterruptHandler (void)
</#if>
{
    /* Client must call UARTx_ErrorGet() function to clear the errors */
    if( ${UART_INSTANCE_NAME?lower_case}Obj.rxCallback != NULL )
    {
        ${UART_INSTANCE_NAME?lower_case}Obj.rxCallback(${UART_INSTANCE_NAME?lower_case}Obj.rxContext);
    }

    /* Clear size and rx status */
    ${UART_INSTANCE_NAME?lower_case}Obj.rxBusyStatus = false;
    ${UART_INSTANCE_NAME?lower_case}Obj.rxSize = 0;
    ${UART_INSTANCE_NAME?lower_case}Obj.rxProcessedSize = 0;

    ${UART_INSTANCE_NAME}_ErrorClear();

    /* Disable the fault interrupt */
    ${UART_FAULT_IEC_REG}CLR = _${UART_FAULT_IEC_REG}_U${UART_INSTANCE_NUM}EIE_MASK;
}

<#if UART_INTERRUPT_COUNT == 1>
static void ${UART_INSTANCE_NAME}_RX_InterruptHandler (void)
<#else>
void ${UART_INSTANCE_NAME}_RX_InterruptHandler (void)
</#if>
{
    if(${UART_INSTANCE_NAME?lower_case}Obj.rxBusyStatus == true)
    {
        while((_U${UART_INSTANCE_NUM}STA_URXDA_MASK == (U${UART_INSTANCE_NUM}STA & _U${UART_INSTANCE_NUM}STA_URXDA_MASK)) && (${UART_INSTANCE_NAME?lower_case}Obj.rxSize > ${UART_INSTANCE_NAME?lower_case}Obj.rxProcessedSize) )
        {
            ${UART_INSTANCE_NAME?lower_case}Obj.rxBuffer[${UART_INSTANCE_NAME?lower_case}Obj.rxProcessedSize++] = (uint8_t )(U${UART_INSTANCE_NUM}RXREG);
        }

        /* Clear ${UART_INSTANCE_NAME} RX Interrupt flag after reading data buffer */
        ${UART_RX_IFS_REG}CLR = _${UART_RX_IFS_REG}_U${UART_INSTANCE_NUM}RXIF_MASK;

        /* Check if the buffer is done */
        if(${UART_INSTANCE_NAME?lower_case}Obj.rxProcessedSize >= ${UART_INSTANCE_NAME?lower_case}Obj.rxSize)
        {
            ${UART_INSTANCE_NAME?lower_case}Obj.rxBusyStatus = false;
            ${UART_INSTANCE_NAME?lower_case}Obj.rxSize = 0;
            ${UART_INSTANCE_NAME?lower_case}Obj.rxProcessedSize = 0;

            /* Disable the receive interrupt */
            ${UART_RX_IEC_REG}CLR = _${UART_RX_IEC_REG}_U${UART_INSTANCE_NUM}RXIE_MASK;

            if(${UART_INSTANCE_NAME?lower_case}Obj.rxCallback != NULL)
            {
                ${UART_INSTANCE_NAME?lower_case}Obj.rxCallback(${UART_INSTANCE_NAME?lower_case}Obj.rxContext);
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
static void ${UART_INSTANCE_NAME}_TX_InterruptHandler (void)
<#else>
void ${UART_INSTANCE_NAME}_TX_InterruptHandler (void)
</#if>
{
    if(${UART_INSTANCE_NAME?lower_case}Obj.txBusyStatus == true)
    {
        while((!(U${UART_INSTANCE_NUM}STA & _U${UART_INSTANCE_NUM}STA_UTXBF_MASK)) && (${UART_INSTANCE_NAME?lower_case}Obj.txSize > ${UART_INSTANCE_NAME?lower_case}Obj.txProcessedSize) )
        {
            U${UART_INSTANCE_NUM}TXREG = ${UART_INSTANCE_NAME?lower_case}Obj.txBuffer[${UART_INSTANCE_NAME?lower_case}Obj.txProcessedSize++];
        }

        /* Clear ${UART_INSTANCE_NAME}TX Interrupt flag after writing to buffer */
        ${UART_TX_IFS_REG}CLR = _${UART_TX_IFS_REG}_U${UART_INSTANCE_NUM}TXIF_MASK;

        /* Check if the buffer is done */
        if(${UART_INSTANCE_NAME?lower_case}Obj.txProcessedSize >= ${UART_INSTANCE_NAME?lower_case}Obj.txSize)
        {
            ${UART_INSTANCE_NAME?lower_case}Obj.txBusyStatus = false;
            ${UART_INSTANCE_NAME?lower_case}Obj.txSize = 0;
            ${UART_INSTANCE_NAME?lower_case}Obj.txProcessedSize = 0;

            /* Disable the transmit interrupt, to avoid calling ISR continuously */
            ${UART_TX_IEC_REG}CLR = _${UART_TX_IEC_REG}_U${UART_INSTANCE_NUM}TXIE_MASK;

            if(${UART_INSTANCE_NAME?lower_case}Obj.txCallback != NULL)
            {
                ${UART_INSTANCE_NAME?lower_case}Obj.txCallback(${UART_INSTANCE_NAME?lower_case}Obj.txContext);
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
void UART_${UART_INSTANCE_NUM}_InterruptHandler (void)
{
    /* Call RX handler if RX interrupt flag is set */
    if ((${UART_RX_IFS_REG} & _${UART_RX_IFS_REG}_U${UART_INSTANCE_NUM}RXIF_MASK) && (${UART_RX_IEC_REG} & _${UART_RX_IEC_REG}_U${UART_INSTANCE_NUM}RXIE_MASK))
    {
        ${UART_INSTANCE_NAME}_RX_InterruptHandler();
    }
    /* Call TX handler if TX interrupt flag is set */
    else if ((${UART_TX_IFS_REG} & _${UART_TX_IFS_REG}_U${UART_INSTANCE_NUM}TXIF_MASK) && (${UART_TX_IEC_REG} & _${UART_TX_IEC_REG}_U${UART_INSTANCE_NUM}TXIE_MASK))
    {
        ${UART_INSTANCE_NAME}_TX_InterruptHandler();
    }
    /* Call Error handler if Error interrupt flag is set */
    else if ((${UART_FAULT_IFS_REG} & _${UART_FAULT_IFS_REG}_U${UART_INSTANCE_NUM}EIF_MASK) && (${UART_FAULT_IEC_REG} & _${UART_FAULT_IEC_REG}_U${UART_INSTANCE_NUM}EIE_MASK))
    {
        ${UART_INSTANCE_NAME}_FAULT_InterruptHandler();
    }
}

</#if>
<#else>
void ${UART_INSTANCE_NAME}_WriteByte(int data)
{
    while (!(U${UART_INSTANCE_NUM}STA & _U${UART_INSTANCE_NUM}STA_UTXBF_MASK));

    U${UART_INSTANCE_NUM}TXREG = data;
}

bool ${UART_INSTANCE_NAME}_TransmitterIsReady( void )
{
    bool status = false;

    if(!(U${UART_INSTANCE_NUM}STA & _U${UART_INSTANCE_NUM}STA_UTXBF_MASK))
    {
        status = true;
    }

    return status;
}

int ${UART_INSTANCE_NAME}_ReadByte( void )
{
    return(U${UART_INSTANCE_NUM}RXREG);
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
