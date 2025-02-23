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

#include <xc.h>
#include <stdint.h>
#include <stddef.h>
#include <stdbool.h>
#include "device.h"
#include "interrupts.h"
#include "plib_${moduleName?lower_case}.h"

// Section: ${moduleName} Implementation

volatile static UART_RING_BUFFER_OBJECT ${moduleName?lower_case}Obj;

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

#define ${moduleName}_READ_BUFFER_SIZE      (${rxBufferSize}U + 1U)
volatile static uint8_t ${moduleName}_ReadBuffer[${moduleName}_READ_BUFFER_SIZE];

#define ${moduleName}_WRITE_BUFFER_SIZE      (${txBufferSize}U + 1U)
volatile static uint8_t ${moduleName}_WriteBuffer[${moduleName}_WRITE_BUFFER_SIZE];

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

        /* Clear error interrupt flag */
        ${rxInterruptFlagBit} = 0;

        /* Clear up the receive interrupt flag so that RX interrupt is not
         * triggered for error bytes */
        ${rxInterruptFlagBit} = 0;

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
    U${instanceNumber}STAT = (_U${instanceNumber}STAT_RXFOIE_MASK
            |_U${instanceNumber}STAT_FERIE_MASK
            |_U${instanceNumber}STAT_PERIE_MASK);

    /* BAUD Rate register Setup */
    U${instanceNumber}BRG = ${brgRegValue};
  
    /* Disable Interrupts */
    ${errorInterruptEnableBit} = 0U;
    ${rxInterruptEnableBit} = 0U;
    ${txInterruptEnableBit} = 0U;

    /* Initialize instance object */
    ${moduleName?lower_case}Obj.rdCallback = NULL;
    ${moduleName?lower_case}Obj.rdInIndex = 0;
    ${moduleName?lower_case}Obj.rdOutIndex = 0;
    ${moduleName?lower_case}Obj.isRdNotificationEnabled = false;
    ${moduleName?lower_case}Obj.isRdNotifyPersistently = false;
    ${moduleName?lower_case}Obj.rdThreshold = 0;

    ${moduleName?lower_case}Obj.wrCallback = NULL;
    ${moduleName?lower_case}Obj.wrInIndex = 0;
    ${moduleName?lower_case}Obj.wrOutIndex = 0;
    ${moduleName?lower_case}Obj.isWrNotificationEnabled = false;
    ${moduleName?lower_case}Obj.isWrNotifyPersistently = false;
    ${moduleName?lower_case}Obj.wrThreshold = 0;

    ${moduleName?lower_case}Obj.errors = UART_ERROR_NONE;


    ${moduleName?lower_case}Obj.rdBufferSize = ${moduleName}_READ_BUFFER_SIZE;
    ${moduleName?lower_case}Obj.wrBufferSize = ${moduleName}_WRITE_BUFFER_SIZE;

    /* Enable ${moduleName}_ERROR Interrupt */
    ${errorInterruptEnableBit} = 1U;

    /* Enable ${moduleName}_RX Interrupt */
    ${rxInterruptEnableBit} = 1U;
    
    /* Turn ON ${moduleName} */
    U${instanceNumber}CON |= (_U${instanceNumber}CON_ON_MASK
                 |_U${instanceNumber}CON_TXEN_MASK
                 |_U${instanceNumber}CON_RXEN_MASK);
}

bool ${moduleName}_SerialSetup( UART_SERIAL_SETUP *setup, uint32_t srcClkFreq )
{
    bool status = false;
    uint32_t baud;
    uint32_t ctrlReg;
    uint32_t uxbrg;

    if (setup != NULL)
    {
        baud = setup->baudRate;

        if (baud == 0U)
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
            U${instanceNumber}CONbits.CLKMOD = 1;
        }
        
        if(setup->dataWidth == UART_DATA_8_BIT)
        {
            /* Configure ${moduleName} mode with parity if mode is 8 bit */
            U${instanceNumber}CONbits.MODE = (uint8_t)setup->parity;
        }
        else
        {
            /* Configure ${moduleName} mode to 7 bit */
            U${instanceNumber}CONbits.MODE = (uint8_t)setup->dataWidth;
        }

        /* Configure ${moduleName} mode */
        U${instanceNumber}CONbits.STP = (uint8_t)setup->stopBits;
        
        /* Configure ${moduleName} Baud Rate */
        U${instanceNumber}BRG = uxbrg;

        ${moduleName?lower_case}Obj.rdBufferSize = ${moduleName}_READ_BUFFER_SIZE;
        ${moduleName?lower_case}Obj.wrBufferSize = ${moduleName}_WRITE_BUFFER_SIZE;

        U${instanceNumber}CONbits.ON = 1U;

        /* Restore UTXEN, URXEN bits. */
        U${instanceNumber}CON |= ctrlReg;

        status = true;
    }

    return status;
}

/* This routine is only called from ISR. Hence do not disable/enable USART interrupts. */
static inline bool ${moduleName}_RxPushByte(uint8_t rdByte)
{
    uint32_t nextIndex;
    bool isSuccess = false;

    // nextIndex is where head will point to after this write.
    nextIndex = ${moduleName?lower_case}Obj.rdInIndex + 1U;

    if (nextIndex >= ${moduleName?lower_case}Obj.rdBufferSize)
    {
        nextIndex = 0U;
    }

    if (nextIndex == ${moduleName?lower_case}Obj.rdOutIndex)
    {
        /* Queue is full - Report it to the application. Application gets a chance to free up space by reading data out from the RX ring buffer */
        if(${moduleName?lower_case}Obj.rdCallback != NULL)
        {
            uintptr_t rdContext = ${moduleName?lower_case}Obj.rdContext;

            ${moduleName?lower_case}Obj.rdCallback(UART_EVENT_READ_BUFFER_FULL, rdContext);

            /* Read the indices again in case application has freed up space in RX ring buffer */
            nextIndex = ${moduleName?lower_case}Obj.rdInIndex + 1U;

            if (nextIndex >= ${moduleName?lower_case}Obj.rdBufferSize)
            {
                nextIndex = 0U;
            }
        }
    }

    /* Attempt to push the data into the ring buffer */
    if (nextIndex != ${moduleName?lower_case}Obj.rdOutIndex)
    {
        uint32_t rdInIndex = ${moduleName?lower_case}Obj.rdInIndex;

        ${moduleName}_ReadBuffer[rdInIndex] = (uint8_t)rdByte;

        ${moduleName?lower_case}Obj.rdInIndex = nextIndex;

        isSuccess = true;
    }
    else
    {
        /* Queue is full. Data will be lost. */
    }

    return isSuccess;
}

/* This routine is only called from ISR. Hence do not disable/enable USART interrupts. */
static void ${moduleName}_ReadNotificationSend(void)
{
    uint32_t nUnreadBytesAvailable;

    if (${moduleName?lower_case}Obj.isRdNotificationEnabled == true)
    {
        nUnreadBytesAvailable = ${moduleName}_ReadCountGet();

        if(${moduleName?lower_case}Obj.rdCallback != NULL)
        {
            uintptr_t rdContext = ${moduleName?lower_case}Obj.rdContext;

            if (${moduleName?lower_case}Obj.isRdNotifyPersistently == true)
            {
                if (nUnreadBytesAvailable >= ${moduleName?lower_case}Obj.rdThreshold)
                {
                    ${moduleName?lower_case}Obj.rdCallback(UART_EVENT_READ_THRESHOLD_REACHED, rdContext);
                }
            }
            else
            {
                if (nUnreadBytesAvailable == ${moduleName?lower_case}Obj.rdThreshold)
                {
                    ${moduleName?lower_case}Obj.rdCallback(UART_EVENT_READ_THRESHOLD_REACHED, rdContext);
                }
            }
        }
    }
}

size_t ${moduleName}_Read(uint8_t* pRdBuffer, const size_t size)
{
    size_t nBytesRead = 0;
    uint32_t rdOutIndex = 0;
    uint32_t rdInIndex = 0;

    /* Take a snapshot of indices to avoid creation of critical section */
    rdOutIndex = ${moduleName?lower_case}Obj.rdOutIndex;
    rdInIndex = ${moduleName?lower_case}Obj.rdInIndex;

    while (nBytesRead < size)
    {
        if (rdOutIndex != rdInIndex)
        {
            pRdBuffer[nBytesRead] = ${moduleName}_ReadBuffer[rdOutIndex];
            nBytesRead++;
            rdOutIndex++;

            if (rdOutIndex >= ${moduleName?lower_case}Obj.rdBufferSize)
            {
                rdOutIndex = 0U;
            }
        }
        else
        {
            /* No more data available in the RX buffer */
            break;
        }
    }

    ${moduleName?lower_case}Obj.rdOutIndex = rdOutIndex;

    return nBytesRead;
}

size_t ${moduleName}_ReadCountGet(void)
{
    size_t nUnreadBytesAvailable;
    uint32_t rdInIndex;
    uint32_t rdOutIndex;

    /* Take a snapshot of indices to avoid processing in critical section */
    rdInIndex = ${moduleName?lower_case}Obj.rdInIndex;
    rdOutIndex = ${moduleName?lower_case}Obj.rdOutIndex;

    if ( rdInIndex >=  rdOutIndex)
    {
        nUnreadBytesAvailable =  (size_t)(rdInIndex -  rdOutIndex);
    }
    else
    {
        nUnreadBytesAvailable =  (size_t)((${moduleName?lower_case}Obj.rdBufferSize -  rdOutIndex) + rdInIndex);
    }

    return nUnreadBytesAvailable;
}

size_t ${moduleName}_ReadFreeBufferCountGet(void)
{
    return (${moduleName?lower_case}Obj.rdBufferSize - 1U) - ${moduleName}_ReadCountGet();
}

size_t ${moduleName}_ReadBufferSizeGet(void)
{
    return (${moduleName?lower_case}Obj.rdBufferSize - 1U);
}

bool ${moduleName}_ReadNotificationEnable(bool isEnabled, bool isPersistent)
{
    bool previousStatus = ${moduleName?lower_case}Obj.isRdNotificationEnabled;

    ${moduleName?lower_case}Obj.isRdNotificationEnabled = isEnabled;

    ${moduleName?lower_case}Obj.isRdNotifyPersistently = isPersistent;

    return previousStatus;
}

void ${moduleName}_ReadThresholdSet(uint32_t nBytesThreshold)
{
    if (nBytesThreshold > 0U)
    {
        ${moduleName?lower_case}Obj.rdThreshold = nBytesThreshold;
    }
}

void ${moduleName}_ReadCallbackRegister( UART_RING_BUFFER_CALLBACK callback, uintptr_t context)
{
    ${moduleName?lower_case}Obj.rdCallback = callback;

    ${moduleName?lower_case}Obj.rdContext = context;
}

/* This routine is only called from ISR. Hence do not disable/enable USART interrupts. */
static bool ${moduleName}_TxPullByte(uint16_t* pWrByte)
{
    bool isSuccess = false;
    uint32_t wrOutIndex = ${moduleName?lower_case}Obj.wrOutIndex;
    uint32_t wrInIndex = ${moduleName?lower_case}Obj.wrInIndex;

    if (wrOutIndex != wrInIndex)
    {

        *pWrByte = ${moduleName}_WriteBuffer[wrOutIndex];
        wrOutIndex++;
        if (wrOutIndex >= ${moduleName?lower_case}Obj.wrBufferSize)
        {
            wrOutIndex = 0U;
        }

        ${moduleName?lower_case}Obj.wrOutIndex = wrOutIndex;

        isSuccess = true;
    }

    return isSuccess;
}

static inline bool ${moduleName}_TxPushByte(uint8_t wrByte)
{
    uint32_t nextIndex;
    bool isSuccess = false;
    uint32_t wrOutIndex = ${moduleName?lower_case}Obj.wrOutIndex;
    uint32_t wrInIndex = ${moduleName?lower_case}Obj.wrInIndex;

    nextIndex = wrInIndex + 1U;

    if (nextIndex >= ${moduleName?lower_case}Obj.wrBufferSize)
    {
        nextIndex = 0U;
    }
    if (nextIndex != wrOutIndex)
    {

        ${moduleName}_WriteBuffer[wrInIndex] = (uint8_t)wrByte;

        ${moduleName?lower_case}Obj.wrInIndex = nextIndex;

        isSuccess = true;
    }
    else
    {
        /* Queue is full. Report Error. */
    }

    return isSuccess;
}

/* This routine is only called from ISR. Hence do not disable/enable USART interrupts. */
static void ${moduleName}_WriteNotificationSend(void)
{
    uint32_t nFreeWrBufferCount;

    if (${moduleName?lower_case}Obj.isWrNotificationEnabled == true)
    {
        nFreeWrBufferCount = ${moduleName}_WriteFreeBufferCountGet();

        if(${moduleName?lower_case}Obj.wrCallback != NULL)
        {
            uintptr_t wrContext = ${moduleName?lower_case}Obj.wrContext;

            if (${moduleName?lower_case}Obj.isWrNotifyPersistently == true)
            {
                if (nFreeWrBufferCount >= ${moduleName?lower_case}Obj.wrThreshold)
                {
                    ${moduleName?lower_case}Obj.wrCallback(UART_EVENT_WRITE_THRESHOLD_REACHED, wrContext);
                }
            }
            else
            {
                if (nFreeWrBufferCount == ${moduleName?lower_case}Obj.wrThreshold)
                {
                    ${moduleName?lower_case}Obj.wrCallback(UART_EVENT_WRITE_THRESHOLD_REACHED, wrContext);
                }
            }
        }
    }
}

static size_t ${moduleName}_WritePendingBytesGet(void)
{
    size_t nPendingTxBytes;

    /* Take a snapshot of indices to avoid processing in critical section */

    uint32_t wrOutIndex = ${moduleName?lower_case}Obj.wrOutIndex;
    uint32_t wrInIndex = ${moduleName?lower_case}Obj.wrInIndex;

    if ( wrInIndex >=  wrOutIndex)
    {
        nPendingTxBytes =  (size_t)(wrInIndex - wrOutIndex);
    }
    else
    {
        nPendingTxBytes =  (size_t)((${moduleName?lower_case}Obj.wrBufferSize -  wrOutIndex) + wrInIndex);
    }

    return nPendingTxBytes;
}

size_t ${moduleName}_WriteCountGet(void)
{
    size_t nPendingTxBytes;

    nPendingTxBytes = ${moduleName}_WritePendingBytesGet();

    return nPendingTxBytes;
}

size_t ${moduleName}_Write(uint8_t* pWrBuffer, const size_t size )
{
    size_t nBytesWritten  = 0U;

    while (nBytesWritten < size)
    {

        if (${moduleName}_TxPushByte(pWrBuffer[nBytesWritten]) == true)
        {
            nBytesWritten++;
        }
        else
        {
            /* Queue is full, exit the loop */
            break;
        }

    }

    /* Check if any data is pending for transmission */
    if (${moduleName}_WritePendingBytesGet() > 0U)
    {
        /* Enable TX interrupt as data is pending for transmission */
        ${txInterruptEnableBit} = 1U;
    }

    return nBytesWritten;
}

size_t ${moduleName}_WriteFreeBufferCountGet(void)
{
    return (${moduleName?lower_case}Obj.wrBufferSize - 1U) - ${moduleName}_WriteCountGet();
}

size_t ${moduleName}_WriteBufferSizeGet(void)
{
    return (${moduleName?lower_case}Obj.wrBufferSize - 1U);
}

bool ${moduleName}_TransmitComplete(void)
{
    bool status = false;

    if(U${instanceNumber}STATbits.TXMTIF != 0U)
    {
        status = true;
    }
    return status;
}

bool ${moduleName}_WriteNotificationEnable(bool isEnabled, bool isPersistent)
{
    bool previousStatus = ${moduleName?lower_case}Obj.isWrNotificationEnabled;

    ${moduleName?lower_case}Obj.isWrNotificationEnabled = isEnabled;

    ${moduleName?lower_case}Obj.isWrNotifyPersistently = isPersistent;

    return previousStatus;
}

void ${moduleName}_WriteThresholdSet(uint32_t nBytesThreshold)
{
    if (nBytesThreshold > 0U)
    {
        ${moduleName?lower_case}Obj.wrThreshold = nBytesThreshold;
    }
}

void ${moduleName}_WriteCallbackRegister( UART_RING_BUFFER_CALLBACK callback, uintptr_t context)
{
    ${moduleName?lower_case}Obj.wrCallback = callback;

    ${moduleName?lower_case}Obj.wrContext = context;
}

UART_ERROR ${moduleName}_ErrorGet( void )
{
    UART_ERROR errors = ${moduleName?lower_case}Obj.errors;

    ${moduleName?lower_case}Obj.errors = UART_ERROR_NONE;

    /* All errors are cleared, but send the previous error state */
    return errors;
}

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

    /* Turning off ABAUD if it was on can lead to unpredictable behavior, so that
       direction of control is not allowed in this function.                      */
}

void ${errorIsrHandlerName}(void)
{
    /* Save the error to be reported later */
    ${moduleName?lower_case}Obj.errors = (U${instanceNumber}STAT & (_U${instanceNumber}STAT_RXFOIF_MASK | _U${instanceNumber}STAT_FERIF_MASK | _U${instanceNumber}STAT_PERIF_MASK));

    /* Disable the fault interrupt */
    ${errorInterruptEnableBit} = 0U;

    /* Disable the receive interrupt */
    ${rxInterruptEnableBit} = 0U;
    
    ${moduleName}_ErrorClear();

    /* Client must call UARTx_ErrorGet() function to clear the errors */
    if( ${moduleName?lower_case}Obj.rdCallback != NULL )
    {
        uintptr_t rdContext = ${moduleName?lower_case}Obj.rdContext;

        ${moduleName?lower_case}Obj.rdCallback(UART_EVENT_READ_ERROR, rdContext);
    }
}


void ${rxIsrHandlerName}(void)
{
    /* Keep reading until there is a character available in the RX FIFO */
    while(U${instanceNumber}STATbits.RXBE != 1U)
    {
        if (${moduleName}_RxPushByte((uint8_t )(U${instanceNumber}RXB)) == true)
        {
            ${moduleName}_ReadNotificationSend();
        }
        else
        {
            /* UART RX buffer is full */
        }
    }

    /* Clear ${moduleName} RX Interrupt flag */
    ${rxInterruptFlagBit} = 0U;
}

void ${txIsrHandlerName}(void)
{
    uint16_t wrByte;

    /* Check if any data is pending for transmission */
    if (${moduleName}_WritePendingBytesGet() > 0U)
    {
        /* Clear ${moduleName}TX Interrupt flag */
        ${txInterruptFlagBit} = 0U;
        
        /* Keep writing to the TX FIFO as long as there is space */
        while(U${instanceNumber}STATbits.TXBF == 0U)
        {
            if (${moduleName}_TxPullByte(&wrByte) == true)
            {
                U${instanceNumber}TXB = (uint8_t)wrByte;

                /* Send notification */
                ${moduleName}_WriteNotificationSend();
            }
            else
            {
                /* Nothing to transmit. Disable the data register empty interrupt. */
                ${txInterruptEnableBit} = 0U;
                break;
            }
        }
    }
    else
    {
        /* Nothing to transmit. Disable the data register empty interrupt. */
        ${txInterruptEnableBit} = 0U;
    }
}
