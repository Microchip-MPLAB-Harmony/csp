<#assign uconModeOptions = ["8_BIT_NONE","7_BIT","8_BIT_ODD","8_BIT_EVEN"]>
<#assign uconStpOptions = ["1_SENT_1_RECEIVE","1_5_SENT_1_5_RECEIVE","2_SENT_2_RECEIVE","2_SENT_1_RECEIVE"]>
<#assign uconClkselOptions = ["UPB_CLOCK","CLOCK_GEN_"+clkSrcGenNumber]>
/*******************************************************************************
  ${moduleName?lower_case} PLIB
 
  Company:
    Microchip Technology Inc.
 
  File Name:
    plib_${moduleName?lower_case}.c
 
  Summary:
    ${moduleName?lower_case} PLIB Source File
 
  Description:
    None
 
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


// Section: Included Files

#include <stdint.h>
#include <stddef.h>
#include <stdbool.h>
#include "device.h"
#include "interrupts.h"
#include "plib_${moduleName?lower_case}.h"

<#if intEnable == true>
volatile static UART_OBJECT ${moduleName?lower_case}Obj;
</#if>

// Section: Macro Definitions

//UART UxCON MODE options
<#list uconModeOptions as options>
#define U${instanceNumber}CON_MODE_${options}          ((uint32_t)(_U${instanceNumber}CON_MODE_MASK & ((uint32_t)(${options_index}) << _U${instanceNumber}CON_MODE_POSITION))) 
</#list>

//UART UxCON STP options
<#list uconStpOptions as options>
#define U${instanceNumber}CON_STP_${options}           ((uint32_t)(_U${instanceNumber}CON_STP_MASK & ((uint32_t)(${options_index}) << _U${instanceNumber}CON_STP_POSITION))) 
</#list>

//UART UxCON CLKSEL options
<#list uconClkselOptions as options>
#define U${instanceNumber}CON_CLKSEL_${options}        ((uint32_t)(_U${instanceNumber}CON_CLKSEL_MASK & ((uint32_t)(${options_index}) << _U${instanceNumber}CON_CLKSEL_POSITION))) 
</#list>

//UART UxCON FLO options
#define U${instanceNumber}CON_FLO_NONE        ((uint32_t)(_U${instanceNumber}CON_FLO_MASK & ((uint32_t)(0) << _U${instanceNumber}CON_FLO_POSITION))) 

#define UART_MAX_BAUD 0xFFFFFUL
#define UART_MIN_FRACTIONAL_BAUD 16U

<#if intEnable == true>
void ${errorIsrHandlerName}(void);
void ${rxIsrHandlerName}(void);
void ${txIsrHandlerName}(void);
</#if>

// Section: ${moduleName} Implementation

void static ${moduleName}_ErrorClear( void )
{
    UART_ERROR errors = UART_ERROR_NONE;
    uint8_t dummyData = 0u;

    errors = (UART_ERROR)(U${instanceNumber}STAT & (_U${instanceNumber}STAT_RXFOIF_MASK | _U${instanceNumber}STAT_FERIF_MASK | _U${instanceNumber}STAT_PERIF_MASK));

    if(errors != UART_ERROR_NONE)
    {
        /* If it's a overrun error then clear it to flush FIFO */
        if(U${instanceNumber}STATbits.RXFOIF != 0U)
        {
            U${instanceNumber}STATbits.RXFOIF = 0U;
        }

        /* Read existing error bytes from FIFO to clear parity and framing error flags */
        while(U${instanceNumber}STATbits.RXBE != 1U)
        {
            dummyData = (uint8_t)U${instanceNumber}RXB;
        }

<#if intEnable == true >
        /* Clear error interrupt flag */
        ${errorInterruptFlagBit} = 0;

        /* Clear up the receive interrupt flag so that RX interrupt is not
         * triggered for error bytes */
        ${rxInterruptFlagBit} = 0;
</#if>
    }

    // Ignore the warning
    (void)dummyData;
}

void ${moduleName}_Initialize( void )
{
    /*
    Baud Rate:      ${calcBaudRateVal}
    */
    U${instanceNumber}CON = (U${instanceNumber}CON_MODE_${uconModeOptions[U_CON__MODE?number]}<#if U_CON__BRGS == "1">
            |_U${instanceNumber}CON_BRGS_MASK</#if>
            |U${instanceNumber}CON_STP_${uconStpOptions[U_CON__STP?number]}<#if U_CON__CLKMOD == "1">
            |_U${instanceNumber}CON_CLKMOD_MASK</#if>
            |U${instanceNumber}CON_FLO_NONE
            |U${instanceNumber}CON_CLKSEL_${uconClkselOptions[U_CON__CLKSEL?number]});
<#if intEnable == true>
    U${instanceNumber}STAT = (_U${instanceNumber}STAT_RXFOIE_MASK
            |_U${instanceNumber}STAT_FERIE_MASK
            |_U${instanceNumber}STAT_PERIE_MASK);
</#if>

    /* BAUD Rate register Setup */
    U${instanceNumber}BRG = ${brgRegValue};

<#if intEnable == true>
    /* Disable Interrupts */
    ${errorInterruptEnableBit} = 0U;
    ${rxInterruptEnableBit} = 0U;
    ${txInterruptEnableBit} = 0U;

    /* Initialize instance object */
    ${moduleName?lower_case}Obj.rxBuffer = NULL;
    ${moduleName?lower_case}Obj.rxSize = 0;
    ${moduleName?lower_case}Obj.rxProcessedSize = 0;
    ${moduleName?lower_case}Obj.rxBusyStatus = false;
    ${moduleName?lower_case}Obj.rxCallback = NULL;
    ${moduleName?lower_case}Obj.txBuffer = NULL;
    ${moduleName?lower_case}Obj.txSize = 0;
    ${moduleName?lower_case}Obj.txProcessedSize = 0;
    ${moduleName?lower_case}Obj.txBusyStatus = false;
    ${moduleName?lower_case}Obj.txCallback = NULL;
    ${moduleName?lower_case}Obj.errors = UART_ERROR_NONE;

</#if>
    /* Turn ON ${moduleName} */
    U${instanceNumber}CON |= (_U${instanceNumber}CON_ON_MASK
                 |_U${instanceNumber}CON_TXEN_MASK
                 |_U${instanceNumber}CON_RXEN_MASK);
}

bool ${moduleName}_SerialSetup(UART_SERIAL_SETUP *setup, uint32_t srcClkFreq)
{
    bool status = false;
    uint32_t baud;
    uint32_t ctrlReg;
    uint32_t uxbrg;

<#if intEnable == true>
    if(${moduleName?lower_case}Obj.rxBusyStatus == true)
    {
        /* Transaction is in progress, so return without updating settings */
        return status;
    }
    if (${moduleName?lower_case}Obj.txBusyStatus == true)
    {
        /* Transaction is in progress, so return without updating settings */
        return status;
    }

</#if>
    if (setup != NULL)
    {
        baud = setup->baudRate;

        if ((baud == 0U) || ((setup->dataWidth == UART_DATA_7_BIT) && (setup->parity != UART_PARITY_NONE)))
        {
            return status;
        }


        srcClkFreq = ${moduleName}_FrequencyGet();

        
        /* Turn OFF ${moduleName}. Save UTXEN, URXEN bits as these are cleared upon disabling UART */
        ctrlReg = U${instanceNumber}CON & (_U${instanceNumber}CON_TXEN_MASK | _U${instanceNumber}CON_RXEN_MASK );
        U${instanceNumber}CONbits.ON = 0U;
        
        /* Calculate BRG value in fractional mode as it has least error rate */
        uxbrg = (srcClkFreq/baud);
        /* Check if the valid baud value is set */
        if(uxbrg < UART_MIN_FRACTIONAL_BAUD)
        {
            /* Baud rate cannot be achieved with current clock source value */
            return status;
        }
        else if(uxbrg > UART_MAX_BAUD)
        {
            /* Calculate BRG value for high speed mode*/
            uxbrg = (srcClkFreq/(4U*baud)) - 1U;
            U${instanceNumber}CONbits.BRGS = 1U;
            
            if(uxbrg > UART_MAX_BAUD)
            {
                /* Calculate BRG value for low speed mode*/
                uxbrg = (srcClkFreq/(16U*baud)) - 1U;
                U${instanceNumber}CONbits.BRGS = 0U;
                if(uxbrg > UART_MAX_BAUD)
                {
                    /* Baud rate cannot be achieved with current clock source value */
                    return status;
                }
            }
        }
        else
        {
            U${instanceNumber}CONbits.CLKMOD = 1U;
        }
        
        if(setup->dataWidth == UART_DATA_8_BIT)
        {
            /* Configure ${moduleName} mode with parity if mode is 8 bit */
            U${instanceNumber}CONbits.MODE = setup->parity;
        }
        else
        {
            /* Configure ${moduleName} mode to 7 bit */
            U${instanceNumber}CONbits.MODE = setup->dataWidth;
        }

        /* Configure ${moduleName} mode */
        U${instanceNumber}CONbits.STP = setup->stopBits;

        /* Configure ${moduleName} Baud Rate */
        U${instanceNumber}BRG = uxbrg;

        /* Restore UTXEN, URXEN bits. */
        U${instanceNumber}CON |= ctrlReg;
        
        U${instanceNumber}CONbits.ON = 1U;

        status = true;
    }

    return status;
}

bool ${moduleName}_Read(void* buffer, const size_t size)
{
    bool status = false;
<#if intEnable == false>
    uint32_t errorStatus;
    size_t processedSize = 0;
</#if>

    if(buffer != NULL)
    {
<#if intEnable == false>

        /* Clear error flags and flush out error data that may have been received when no active request was pending */
        ${moduleName}_ErrorClear();

        while( size > processedSize )
        {
            while((U${instanceNumber}STATbits.RXBE) != 0U)
            {
                /* Wait for receiver to be ready */
            }

            /* Error status */
            errorStatus = (U${instanceNumber}STAT & (_U${instanceNumber}STAT_RXFOIF_MASK | _U${instanceNumber}STAT_FERIF_MASK | _U${instanceNumber}STAT_PERIF_MASK));

            if(errorStatus != 0U)
            {
                break;
            }
            
            /* 8-bit and 7-bit mode */
            ((uint8_t*)(buffer))[processedSize] = (uint8_t)(U${instanceNumber}RXB);
            processedSize++;
        }

        if(size == processedSize)
        {
            status = true;
        }
<#else>
        /* Check if receive request is in progress */
        if(${moduleName?lower_case}Obj.rxBusyStatus == false)
        {
            /* Clear error flags and flush out error data that may have been received when no active request was pending */
            ${moduleName}_ErrorClear();

            ${moduleName?lower_case}Obj.rxBuffer = buffer;
            ${moduleName?lower_case}Obj.rxSize = size;
            ${moduleName?lower_case}Obj.rxProcessedSize = 0;
            ${moduleName?lower_case}Obj.rxBusyStatus = true;
            ${moduleName?lower_case}Obj.errors = UART_ERROR_NONE;
            status = true;

            /* Enable ${moduleName}_FAULT Interrupt */
            ${errorInterruptEnableBit} = 1U;

            /* Enable ${moduleName}_RX Interrupt */
            ${rxInterruptEnableBit} = 1U;
        }
</#if>
    }

    return status;
}

bool ${moduleName}_Write( void* buffer, const size_t size )
{
    bool status = false;
<#if intEnable == false>
    size_t processedSize = 0;
</#if>

    if(buffer != NULL)
    {
<#if intEnable == false>
        while( size > processedSize )
        {
            /* Wait while TX buffer is full */
            while (U${instanceNumber}STATbits.TXBF != 0U)
            {
                /* Wait for transmitter to be ready */
            }

            /* 7-bit and 8-bit mode */
            U${instanceNumber}TXB = ((uint8_t*)(buffer))[processedSize];

            processedSize++;
        }

        status = true;
<#else>
        /* Check if transmit request is in progress */
        if(${moduleName?lower_case}Obj.txBusyStatus == false)
        {
            ${moduleName?lower_case}Obj.txBuffer = buffer;
            ${moduleName?lower_case}Obj.txSize = size;
            ${moduleName?lower_case}Obj.txProcessedSize = 0;
            ${moduleName?lower_case}Obj.txBusyStatus = true;
            status = true;

            size_t txProcessedSize = ${moduleName?lower_case}Obj.txProcessedSize;
            size_t txSize = ${moduleName?lower_case}Obj.txSize;

            /* Initiate the transfer by writing as many bytes as we can */
            while((U${instanceNumber}STATbits.TXBF == 0U) && (txSize > txProcessedSize) )
            {
                
                /* 7-bit and 8-bit mode */
                U${instanceNumber}TXB = ((uint8_t*)${moduleName?lower_case}Obj.txBuffer)[txProcessedSize];
                txProcessedSize++;
            }

            ${moduleName?lower_case}Obj.txProcessedSize = txProcessedSize;

            ${txInterruptEnableBit} = 1U;
        }
</#if>
    }

    return status;
}

<#if intEnable == true>
UART_ERROR ${moduleName}_ErrorGet( void )
{
    UART_ERROR errors = ${moduleName?lower_case}Obj.errors;

    ${moduleName?lower_case}Obj.errors = UART_ERROR_NONE;

    /* All errors are cleared, but send the previous error state */
    return errors;
}
<#else>
UART_ERROR ${moduleName}_ErrorGet( void )
{
    UART_ERROR errors = UART_ERROR_NONE;

    errors = (U${instanceNumber}STAT & (_U${instanceNumber}STAT_RXFOIF_MASK | _U${instanceNumber}STAT_FERIF_MASK | _U${instanceNumber}STAT_PERIF_MASK));

    if(errors != UART_ERROR_NONE)
    {
        ${moduleName}_ErrorClear();
    }

    /* All errors are cleared, but send the previous error state */
    return errors;
}
</#if>

bool ${moduleName}_AutoBaudQuery( void )
{
    bool autobaudcheck = false;
    if(U${instanceNumber}CONbits.ABDEN != 0U)
    {

      autobaudcheck = true;

    }
    return autobaudcheck;
}

void ${moduleName}_AutoBaudSet( bool enable )
{
    if( enable == true )
    {
        U${instanceNumber}CONbits.ABDEN =  1U;
    }
}

<#if intEnable == true>
void ${moduleName}_ReadCallbackRegister( UART_CALLBACK callback, uintptr_t context )
{
    ${moduleName?lower_case}Obj.rxCallback = callback;

    ${moduleName?lower_case}Obj.rxContext = context;
}

bool ${moduleName}_ReadIsBusy( void )
{
    return ${moduleName?lower_case}Obj.rxBusyStatus;
}

size_t ${moduleName}_ReadCountGet( void )
{
    return ${moduleName?lower_case}Obj.rxProcessedSize;
}

bool ${moduleName}_ReadAbort(void)
{
    if (${moduleName?lower_case}Obj.rxBusyStatus == true)
    {
        /* Disable the fault interrupt */
        ${errorInterruptEnableBit} = 0U;

        /* Disable the receive interrupt */
        ${rxInterruptEnableBit} = 0U;

        ${moduleName?lower_case}Obj.rxBusyStatus = false;

        /* If required application should read the num bytes processed prior to calling the read abort API */
        ${moduleName?lower_case}Obj.rxSize = 0U;
        ${moduleName?lower_case}Obj.rxProcessedSize = 0U;
    }

    return true;
}

void ${moduleName}_WriteCallbackRegister( UART_CALLBACK callback, uintptr_t context )
{
    ${moduleName?lower_case}Obj.txCallback = callback;

    ${moduleName?lower_case}Obj.txContext = context;
}

bool ${moduleName}_WriteIsBusy( void )
{
    return ${moduleName?lower_case}Obj.txBusyStatus;
}

size_t ${moduleName}_WriteCountGet( void )
{
    return ${moduleName?lower_case}Obj.txProcessedSize;
}

void ${errorIsrHandlerName}(void)
{
    /* Save the error to be reported later */
    ${moduleName?lower_case}Obj.errors = (U${instanceNumber}STAT & (_U${instanceNumber}STAT_RXFOIF_MASK | _U${instanceNumber}STAT_FERIF_MASK | _U${instanceNumber}STAT_PERIF_MASK));

    /* Disable the fault interrupt */
    ${errorInterruptEnableBit} = 0U;

    /* Disable the receive interrupt */
    ${rxInterruptEnableBit} = 0U;

    /* Clear size and rx status */
    ${moduleName?lower_case}Obj.rxBusyStatus = false;

    ${moduleName}_ErrorClear();

    /* Client must call UARTx_ErrorGet() function to get the errors */
    if( ${moduleName?lower_case}Obj.rxCallback != NULL )
    {
        uintptr_t rxContext = ${moduleName?lower_case}Obj.rxContext;

        ${moduleName?lower_case}Obj.rxCallback(rxContext);
    }
}

void ${rxIsrHandlerName}(void)
{
    if(${moduleName?lower_case}Obj.rxBusyStatus == true)
    {
        size_t rxProcessedSize = ${moduleName?lower_case}Obj.rxProcessedSize;
        size_t rxSize = ${moduleName?lower_case}Obj.rxSize;

        while((U${instanceNumber}STATbits.RXBE != 1U) && (rxSize > rxProcessedSize))
        {

            /* 8-bit mode */
            ((uint8_t*)${moduleName?lower_case}Obj.rxBuffer)[rxProcessedSize] = (uint8_t )(U${instanceNumber}RXB);
            rxProcessedSize++;
        }

        ${moduleName?lower_case}Obj.rxProcessedSize = rxProcessedSize;

        /* Clear ${moduleName} RX Interrupt flag */
        ${rxInterruptFlagBit} = 0U;
        
        /* Check if the buffer is done */
        if(rxProcessedSize >= ${moduleName?lower_case}Obj.rxSize)
        {
            ${moduleName?lower_case}Obj.rxBusyStatus = false;

            /* Disable the fault interrupt */
            ${errorInterruptEnableBit} = 0U;

            /* Disable the receive interrupt */
            ${rxInterruptEnableBit} = 0U;

            if(${moduleName?lower_case}Obj.rxCallback != NULL)
            {
                uintptr_t rxContext = ${moduleName?lower_case}Obj.rxContext;

                ${moduleName?lower_case}Obj.rxCallback(rxContext);
            }
        }
    }
    else
    {
        /* Nothing to process */
    }
}

void ${txIsrHandlerName}(void)
{
    if(${moduleName?lower_case}Obj.txBusyStatus == true)
    {
        size_t txSize = ${moduleName?lower_case}Obj.txSize;
        size_t txProcessedSize = ${moduleName?lower_case}Obj.txProcessedSize;

        /* Clear ${moduleName} TX Interrupt flag */
        ${txInterruptFlagBit} = 0u;
        
        while((U${instanceNumber}STATbits.TXBF == 0U) && (txSize > txProcessedSize) )
        {
            /* 8-bit mode */
            U${instanceNumber}TXB = ((uint8_t*)${moduleName?lower_case}Obj.txBuffer)[txProcessedSize];
            txProcessedSize++;
        }

        ${moduleName?lower_case}Obj.txProcessedSize = txProcessedSize;

        /* Check if the buffer is done */
        if(txProcessedSize >= ${moduleName?lower_case}Obj.txSize)
        {
            ${moduleName?lower_case}Obj.txBusyStatus = false;

            /* Disable the transmit interrupt, to avoid calling ISR continuously */
            ${txInterruptEnableBit} = 0U;

            if(${moduleName?lower_case}Obj.txCallback != NULL)
            {
                uintptr_t txContext = ${moduleName?lower_case}Obj.txContext;

                ${moduleName?lower_case}Obj.txCallback(txContext);
            }
        }
    }
    else
    {
        // Nothing to process
        ;
    }
}
<#else>

int ${moduleName}_ReadByte( void )
{
    return(int)(U${instanceNumber}RXB);
}

bool ${moduleName}_ReceiverIsReady( void )
{
    return (bool)(U${instanceNumber}STATbits.RXBE == 0U);
}

void ${moduleName}_WriteByte( int data )
{
    while (U${instanceNumber}STATbits.TXBF != 0U)
    {
        /* Do Nothing */
    }

    U${instanceNumber}TXB = (uint32_t)data;
}

bool ${moduleName}_TransmitterIsReady( void )
{
    return (bool)(U${instanceNumber}STATbits.TXBF == 0U);
}
</#if>

bool ${moduleName}_TransmitComplete( void )
{
    bool transmitComplete = false;

    if(U${instanceNumber}STATbits.TXMTIF != 0U)
    {
        transmitComplete = true;
    }

    return transmitComplete;
}