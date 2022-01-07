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

<#if UART_INTERRUPT_MODE_ENABLE == true>
UART_OBJECT ${UART_INSTANCE_NAME?lower_case}Obj;
</#if>

void static ${UART_INSTANCE_NAME}_ErrorClear( void )
{
    UART_ERROR errors = UART_ERROR_NONE;
    uint8_t dummyData = 0u;

    errors = (UART_ERROR)(U${UART_INSTANCE_NUM}STA & (_U${UART_INSTANCE_NUM}STA_OERR_MASK | _U${UART_INSTANCE_NUM}STA_FERR_MASK | _U${UART_INSTANCE_NUM}STA_PERR_MASK));

    if(errors != UART_ERROR_NONE)
    {
        /* If it's a overrun error then clear it to flush FIFO */
        if(U${UART_INSTANCE_NUM}STA & _U${UART_INSTANCE_NUM}STA_OERR_MASK)
        {
            U${UART_INSTANCE_NUM}STACLR = _U${UART_INSTANCE_NUM}STA_OERR_MASK;
        }

        /* Read existing error bytes from FIFO to clear parity and framing error flags */
        while(U${UART_INSTANCE_NUM}STA & _U${UART_INSTANCE_NUM}STA_URXDA_MASK)
        {
            dummyData = U${UART_INSTANCE_NUM}RXREG;
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
    /* UEN = ${UART_UEN_SELECT} */
    U${UART_INSTANCE_NUM}MODE = 0x${UMODE_VALUE};

<#if UART_INTERRUPT_MODE_ENABLE == true>
    /* Enable ${UART_INSTANCE_NAME} Receiver, Transmitter and TX Interrupt selection */
    U${UART_INSTANCE_NUM}STASET = (_U${UART_INSTANCE_NUM}STA_UTXEN_MASK | _U${UART_INSTANCE_NUM}STA_URXEN_MASK | _U${UART_INSTANCE_NUM}STA_UTXISEL1_MASK <#if UART_AUTOMATIC_ADDR_DETECTION_ENABLE == true> | _U${UART_INSTANCE_NUM}STA_ADDEN_MASK | (0x${UART_9BIT_MODE_ADDR} << _U${UART_INSTANCE_NUM}STA_ADDR_POSITION) | (0x${UART_9BIT_MODE_ADDR_MASK} << _U${UART_INSTANCE_NUM}STA_MASK_POSITION) </#if>);
<#else>
    /* Enable ${UART_INSTANCE_NAME} Receiver and Transmitter */
    U${UART_INSTANCE_NUM}STASET = (_U${UART_INSTANCE_NUM}STA_UTXEN_MASK | _U${UART_INSTANCE_NUM}STA_URXEN_MASK <#if UART_AUTOMATIC_ADDR_DETECTION_ENABLE == true> | _U${UART_INSTANCE_NUM}STA_ADDEN_MASK | (0x${UART_9BIT_MODE_ADDR} << _U${UART_INSTANCE_NUM}STA_ADDR_POSITION) | (0x${UART_9BIT_MODE_ADDR_MASK} << _U${UART_INSTANCE_NUM}STA_MASK_POSITION) </#if>);
</#if>

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
    bool brgh = ${UART_BRGH};
    int32_t uxbrg = 0;

<#if UART_INTERRUPT_MODE_ENABLE == true>
    if((${UART_INSTANCE_NAME?lower_case}Obj.rxBusyStatus == true) || (${UART_INSTANCE_NAME?lower_case}Obj.txBusyStatus == true))
    {
        /* Transaction is in progress, so return without updating settings */
        return status;
    }

</#if>
    if (setup != NULL)
    {
        baud = setup->baudRate;

        if ((baud == 0) || ((setup->dataWidth == UART_DATA_9_BIT) && (setup->parity != UART_PARITY_NONE)))
        {
            return status;
        }

        if(srcClkFreq == 0)
        {
            srcClkFreq = ${UART_INSTANCE_NAME}_FrequencyGet();
        }

        /* Calculate BRG value */
        if (brgh == 0)
        {
            uxbrg = (((srcClkFreq >> 4) + (baud >> 1)) / baud ) - 1;
        }
        else
        {
            uxbrg = (((srcClkFreq >> 2) + (baud >> 1)) / baud ) - 1;
        }

        /* Check if the baud value can be set with low baud settings */
        if((uxbrg < 0) || (uxbrg > UINT16_MAX))
        {
            return status;
        }

        /* Turn OFF ${UART_INSTANCE_NAME} */
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

        status = true;
    }

    return status;
}

bool ${UART_INSTANCE_NAME}_Read(void* buffer, const size_t size )
{
    bool status = false;
    uint8_t* lBuffer = (uint8_t* )buffer;
<#if UART_INTERRUPT_MODE_ENABLE == false>
    uint32_t errorStatus = 0;
    size_t processedSize = 0;
</#if>

    if(lBuffer != NULL)
    {
<#if UART_INTERRUPT_MODE_ENABLE == false>

        /* Clear error flags and flush out error data that may have been received when no active request was pending */
        ${UART_INSTANCE_NAME}_ErrorClear();

        while( size > processedSize )
        {
            while(!(U${UART_INSTANCE_NUM}STA & _U${UART_INSTANCE_NUM}STA_URXDA_MASK));

            /* Error status */
            errorStatus = (U${UART_INSTANCE_NUM}STA & (_U${UART_INSTANCE_NUM}STA_OERR_MASK | _U${UART_INSTANCE_NUM}STA_FERR_MASK | _U${UART_INSTANCE_NUM}STA_PERR_MASK));

            if(errorStatus != 0)
            {
                break;
            }
<#if UART_AUTOMATIC_ADDR_DETECTION_ENABLE == true>
            /* 8-bit mode */
            *lBuffer++ = (U${UART_INSTANCE_NUM}RXREG );
<#else>
            if (( U${UART_INSTANCE_NUM}MODE & (_U${UART_INSTANCE_NUM}MODE_PDSEL0_MASK | _U${UART_INSTANCE_NUM}MODE_PDSEL1_MASK)) == (_U${UART_INSTANCE_NUM}MODE_PDSEL0_MASK | _U${UART_INSTANCE_NUM}MODE_PDSEL1_MASK))
            {
                /* 9-bit mode */
                *(uint16_t*)lBuffer = (U${UART_INSTANCE_NUM}RXREG );
                lBuffer += 2;
            }
            else
            {
                /* 8-bit mode */
                *lBuffer++ = (U${UART_INSTANCE_NUM}RXREG );
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

            ${UART_INSTANCE_NAME?lower_case}Obj.rxBuffer = lBuffer;
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
    uint8_t* lBuffer = (uint8_t*)buffer;
<#if UART_INTERRUPT_MODE_ENABLE == false>
    size_t processedSize = 0;
</#if>

    if(lBuffer != NULL)
    {
<#if UART_INTERRUPT_MODE_ENABLE == false>
        while( size > processedSize )
        {
            /* Wait while TX buffer is full */
            while (U${UART_INSTANCE_NUM}STA & _U${UART_INSTANCE_NUM}STA_UTXBF_MASK);

            if (( U${UART_INSTANCE_NUM}MODE & (_U${UART_INSTANCE_NUM}MODE_PDSEL0_MASK | _U${UART_INSTANCE_NUM}MODE_PDSEL1_MASK)) == (_U${UART_INSTANCE_NUM}MODE_PDSEL0_MASK | _U${UART_INSTANCE_NUM}MODE_PDSEL1_MASK))
            {
                /* 9-bit mode */
                U${UART_INSTANCE_NUM}TXREG = *(uint16_t*)lBuffer;
                lBuffer += 2;
            }
            else
            {
                /* 8-bit mode */
                U${UART_INSTANCE_NUM}TXREG = *lBuffer++;
            }

            processedSize++;
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

            /* Initiate the transfer by writing as many bytes as we can */
             while((!(U${UART_INSTANCE_NUM}STA & _U${UART_INSTANCE_NUM}STA_UTXBF_MASK)) && (${UART_INSTANCE_NAME?lower_case}Obj.txSize > ${UART_INSTANCE_NAME?lower_case}Obj.txProcessedSize) )
            {
                if (( U${UART_INSTANCE_NUM}MODE & (_U${UART_INSTANCE_NUM}MODE_PDSEL0_MASK | _U${UART_INSTANCE_NUM}MODE_PDSEL1_MASK)) == (_U${UART_INSTANCE_NUM}MODE_PDSEL0_MASK | _U${UART_INSTANCE_NUM}MODE_PDSEL1_MASK))
                {
                    /* 9-bit mode */
                    U${UART_INSTANCE_NUM}TXREG = ((uint16_t*)${UART_INSTANCE_NAME?lower_case}Obj.txBuffer)[${UART_INSTANCE_NAME?lower_case}Obj.txProcessedSize++];
                }
                else
                {
                    /* 8-bit mode */
                    U${UART_INSTANCE_NUM}TXREG = ${UART_INSTANCE_NAME?lower_case}Obj.txBuffer[${UART_INSTANCE_NAME?lower_case}Obj.txProcessedSize++];
                }
            }

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

    errors = (UART_ERROR)(U${UART_INSTANCE_NUM}STA & (_U${UART_INSTANCE_NUM}STA_OERR_MASK | _U${UART_INSTANCE_NUM}STA_FERR_MASK | _U${UART_INSTANCE_NUM}STA_PERR_MASK));

    if(errors != UART_ERROR_NONE)
    {
        ${UART_INSTANCE_NAME}_ErrorClear();
    }

    /* All errors are cleared, but send the previous error state */
    return errors;
}
</#if>

bool ${UART_INSTANCE_NAME}_AutoBaudQuery( void )
{
    if(U${UART_INSTANCE_NUM}MODE & _U${UART_INSTANCE_NUM}MODE_ABAUD_MASK)
        return true;
    else
        return false;
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

<#if UART_INTERRUPT_COUNT == 1>
static void ${UART_INSTANCE_NAME}_FAULT_InterruptHandler (void)
<#else>
void ${UART_INSTANCE_NAME}${UART_ERROR_NAME}_InterruptHandler (void)
</#if>
{
    /* Save the error to be reported later */
    ${UART_INSTANCE_NAME?lower_case}Obj.errors = (UART_ERROR)(U${UART_INSTANCE_NUM}STA & (_U${UART_INSTANCE_NUM}STA_OERR_MASK | _U${UART_INSTANCE_NUM}STA_FERR_MASK | _U${UART_INSTANCE_NUM}STA_PERR_MASK));

    /* Disable the fault interrupt */
    ${UART_FAULT_IEC_REG}CLR = _${UART_FAULT_IEC_REG}_U${UART_INSTANCE_NUM}EIE_MASK;

    /* Disable the receive interrupt */
    ${UART_RX_IEC_REG}CLR = _${UART_RX_IEC_REG}_U${UART_INSTANCE_NUM}RXIE_MASK;

    /* Clear size and rx status */
    ${UART_INSTANCE_NAME?lower_case}Obj.rxBusyStatus = false;

    ${UART_INSTANCE_NAME}_ErrorClear();

    /* Client must call UARTx_ErrorGet() function to get the errors */
    if( ${UART_INSTANCE_NAME?lower_case}Obj.rxCallback != NULL )
    {
        ${UART_INSTANCE_NAME?lower_case}Obj.rxCallback(${UART_INSTANCE_NAME?lower_case}Obj.rxContext);
    }
}

<#if UART_INTERRUPT_COUNT == 1>
static void ${UART_INSTANCE_NAME}_RX_InterruptHandler (void)
<#else>
void ${UART_INSTANCE_NAME}_RX_InterruptHandler (void)
</#if>
{
    if(${UART_INSTANCE_NAME?lower_case}Obj.rxBusyStatus == true)
    {
<#if (core.PRODUCT_FAMILY == "PIC32MK1402") || (core.PRODUCT_FAMILY == "PIC32MZW")>
        /* Clear ${UART_INSTANCE_NAME} RX Interrupt flag */
        ${UART_RX_IFS_REG}CLR = _${UART_RX_IFS_REG}_U${UART_INSTANCE_NUM}RXIF_MASK;

        while((_U${UART_INSTANCE_NUM}STA_URXDA_MASK == (U${UART_INSTANCE_NUM}STA & _U${UART_INSTANCE_NUM}STA_URXDA_MASK)) && (${UART_INSTANCE_NAME?lower_case}Obj.rxSize > ${UART_INSTANCE_NAME?lower_case}Obj.rxProcessedSize) )
        {
<#if UART_AUTOMATIC_ADDR_DETECTION_ENABLE == true>
            /* 8-bit mode */
            ${UART_INSTANCE_NAME?lower_case}Obj.rxBuffer[${UART_INSTANCE_NAME?lower_case}Obj.rxProcessedSize++] = (uint8_t )(U${UART_INSTANCE_NUM}RXREG);
<#else>
            if (( U${UART_INSTANCE_NUM}MODE & (_U${UART_INSTANCE_NUM}MODE_PDSEL0_MASK | _U${UART_INSTANCE_NUM}MODE_PDSEL1_MASK)) == (_U${UART_INSTANCE_NUM}MODE_PDSEL0_MASK | _U${UART_INSTANCE_NUM}MODE_PDSEL1_MASK))
            {
                /* 9-bit mode */
                ((uint16_t*)${UART_INSTANCE_NAME?lower_case}Obj.rxBuffer)[${UART_INSTANCE_NAME?lower_case}Obj.rxProcessedSize++] = (uint16_t )(U${UART_INSTANCE_NUM}RXREG);
            }
            else
            {
                /* 8-bit mode */
                ${UART_INSTANCE_NAME?lower_case}Obj.rxBuffer[${UART_INSTANCE_NAME?lower_case}Obj.rxProcessedSize++] = (uint8_t )(U${UART_INSTANCE_NUM}RXREG);
            }
</#if>
        }
<#else>
        while((_U${UART_INSTANCE_NUM}STA_URXDA_MASK == (U${UART_INSTANCE_NUM}STA & _U${UART_INSTANCE_NUM}STA_URXDA_MASK)) && (${UART_INSTANCE_NAME?lower_case}Obj.rxSize > ${UART_INSTANCE_NAME?lower_case}Obj.rxProcessedSize) )
        {
<#if UART_AUTOMATIC_ADDR_DETECTION_ENABLE == true>
            /* 8-bit mode */
            ${UART_INSTANCE_NAME?lower_case}Obj.rxBuffer[${UART_INSTANCE_NAME?lower_case}Obj.rxProcessedSize++] = (uint8_t )(U${UART_INSTANCE_NUM}RXREG);
<#else>
            if (( U${UART_INSTANCE_NUM}MODE & (_U${UART_INSTANCE_NUM}MODE_PDSEL0_MASK | _U${UART_INSTANCE_NUM}MODE_PDSEL1_MASK)) == (_U${UART_INSTANCE_NUM}MODE_PDSEL0_MASK | _U${UART_INSTANCE_NUM}MODE_PDSEL1_MASK))
            {
                /* 9-bit mode */
                ((uint16_t*)${UART_INSTANCE_NAME?lower_case}Obj.rxBuffer)[${UART_INSTANCE_NAME?lower_case}Obj.rxProcessedSize++] = (uint16_t )(U${UART_INSTANCE_NUM}RXREG);
            }
            else
            {
                /* 8-bit mode */
                ${UART_INSTANCE_NAME?lower_case}Obj.rxBuffer[${UART_INSTANCE_NAME?lower_case}Obj.rxProcessedSize++] = (uint8_t )(U${UART_INSTANCE_NUM}RXREG);
            }
</#if>
        }

        /* Clear ${UART_INSTANCE_NAME} RX Interrupt flag */
        ${UART_RX_IFS_REG}CLR = _${UART_RX_IFS_REG}_U${UART_INSTANCE_NUM}RXIF_MASK;
</#if>


        /* Check if the buffer is done */
        if(${UART_INSTANCE_NAME?lower_case}Obj.rxProcessedSize >= ${UART_INSTANCE_NAME?lower_case}Obj.rxSize)
        {
            ${UART_INSTANCE_NAME?lower_case}Obj.rxBusyStatus = false;

            /* Disable the fault interrupt */
            ${UART_FAULT_IEC_REG}CLR = _${UART_FAULT_IEC_REG}_U${UART_INSTANCE_NUM}EIE_MASK;

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
<#if (core.PRODUCT_FAMILY == "PIC32MK1402") || (core.PRODUCT_FAMILY == "PIC32MZW")>
        /* Clear ${UART_INSTANCE_NAME}TX Interrupt flag */
        ${UART_TX_IFS_REG}CLR = _${UART_TX_IFS_REG}_U${UART_INSTANCE_NUM}TXIF_MASK;

        while((!(U${UART_INSTANCE_NUM}STA & _U${UART_INSTANCE_NUM}STA_UTXBF_MASK)) && (${UART_INSTANCE_NAME?lower_case}Obj.txSize > ${UART_INSTANCE_NAME?lower_case}Obj.txProcessedSize) )
        {
            if (( U${UART_INSTANCE_NUM}MODE & (_U${UART_INSTANCE_NUM}MODE_PDSEL0_MASK | _U${UART_INSTANCE_NUM}MODE_PDSEL1_MASK)) == (_U${UART_INSTANCE_NUM}MODE_PDSEL0_MASK | _U${UART_INSTANCE_NUM}MODE_PDSEL1_MASK))
            {
                /* 9-bit mode */
                U${UART_INSTANCE_NUM}TXREG = ((uint16_t*)${UART_INSTANCE_NAME?lower_case}Obj.txBuffer)[${UART_INSTANCE_NAME?lower_case}Obj.txProcessedSize++];
            }
            else
            {
                /* 8-bit mode */
                U${UART_INSTANCE_NUM}TXREG = ${UART_INSTANCE_NAME?lower_case}Obj.txBuffer[${UART_INSTANCE_NAME?lower_case}Obj.txProcessedSize++];
            }
        }

<#else>
        while((!(U${UART_INSTANCE_NUM}STA & _U${UART_INSTANCE_NUM}STA_UTXBF_MASK)) && (${UART_INSTANCE_NAME?lower_case}Obj.txSize > ${UART_INSTANCE_NAME?lower_case}Obj.txProcessedSize) )
        {
            if (( U${UART_INSTANCE_NUM}MODE & (_U${UART_INSTANCE_NUM}MODE_PDSEL0_MASK | _U${UART_INSTANCE_NUM}MODE_PDSEL1_MASK)) == (_U${UART_INSTANCE_NUM}MODE_PDSEL0_MASK | _U${UART_INSTANCE_NUM}MODE_PDSEL1_MASK))
            {
                /* 9-bit mode */
                U${UART_INSTANCE_NUM}TXREG = ((uint16_t*)${UART_INSTANCE_NAME?lower_case}Obj.txBuffer)[${UART_INSTANCE_NAME?lower_case}Obj.txProcessedSize++];
            }
            else
            {
                /* 8-bit mode */
                U${UART_INSTANCE_NUM}TXREG = ${UART_INSTANCE_NAME?lower_case}Obj.txBuffer[${UART_INSTANCE_NAME?lower_case}Obj.txProcessedSize++];
            }
        }

        /* Clear ${UART_INSTANCE_NAME}TX Interrupt flag */
        ${UART_TX_IFS_REG}CLR = _${UART_TX_IFS_REG}_U${UART_INSTANCE_NUM}TXIF_MASK;
</#if>

        /* Check if the buffer is done */
        if(${UART_INSTANCE_NAME?lower_case}Obj.txProcessedSize >= ${UART_INSTANCE_NAME?lower_case}Obj.txSize)
        {
            ${UART_INSTANCE_NAME?lower_case}Obj.txBusyStatus = false;

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
    /* Call Error handler if Error interrupt flag is set */
    if ((${UART_FAULT_IFS_REG} & _${UART_FAULT_IFS_REG}_U${UART_INSTANCE_NUM}EIF_MASK) && (${UART_FAULT_IEC_REG} & _${UART_FAULT_IEC_REG}_U${UART_INSTANCE_NUM}EIE_MASK))
    {
        ${UART_INSTANCE_NAME}_FAULT_InterruptHandler();
    }

    /* Call RX handler if RX interrupt flag is set */
    if ((${UART_RX_IFS_REG} & _${UART_RX_IFS_REG}_U${UART_INSTANCE_NUM}RXIF_MASK) && (${UART_RX_IEC_REG} & _${UART_RX_IEC_REG}_U${UART_INSTANCE_NUM}RXIE_MASK))
    {
        ${UART_INSTANCE_NAME}_RX_InterruptHandler();
    }

    /* Call TX handler if TX interrupt flag is set */
    if ((${UART_TX_IFS_REG} & _${UART_TX_IFS_REG}_U${UART_INSTANCE_NUM}TXIF_MASK) && (${UART_TX_IEC_REG} & _${UART_TX_IEC_REG}_U${UART_INSTANCE_NUM}TXIE_MASK))
    {
        ${UART_INSTANCE_NAME}_TX_InterruptHandler();
    }

}
</#if>

<#else>  <#--Not interrupt mode-->
void ${UART_INSTANCE_NAME}_WriteByte(int data)
{
    while ((U${UART_INSTANCE_NUM}STA & _U${UART_INSTANCE_NUM}STA_UTXBF_MASK));

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

bool ${UART_INSTANCE_NAME}_TransmitComplete( void )
{
    bool transmitComplete = false;

    if((U${UART_INSTANCE_NUM}STA & _U${UART_INSTANCE_NUM}STA_TRMT_MASK))
    {
        transmitComplete = true;
    }

    return transmitComplete;
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
