/*******************************************************************************
  UART1 PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_uart1.c

  Summary:
    UART1 PLIB Implementation File

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
#include "plib_uart1.h"

// *****************************************************************************
// *****************************************************************************
// Section: UART1 Implementation
// *****************************************************************************
// *****************************************************************************

UART_RING_BUFFER_OBJECT uart1Obj;

#define UART1_READ_BUFFER_SIZE      20
#define UART1_RX_INT_DISABLE()      IEC1CLR = _IEC1_U1RXIE_MASK;
#define UART1_RX_INT_ENABLE()       IEC1SET = _IEC1_U1RXIE_MASK;

static uint8_t UART1_ReadBuffer[UART1_READ_BUFFER_SIZE];

#define UART1_WRITE_BUFFER_SIZE     128
#define UART1_TX_INT_DISABLE()      IEC1CLR = _IEC1_U1TXIE_MASK;
#define UART1_TX_INT_ENABLE()       IEC1SET = _IEC1_U1TXIE_MASK;

static uint8_t UART1_WriteBuffer[UART1_WRITE_BUFFER_SIZE];

void static UART1_ErrorClear( void )
{
    /* rxBufferLen = (FIFO level + RX register) */
    uint8_t rxBufferLen = UART_RXFIFO_DEPTH;
    uint8_t dummyData = 0u;

    /* If it's a overrun error then clear it to flush FIFO */
    if(U1STA & _U1STA_OERR_MASK)
    {
        U1STACLR = _U1STA_OERR_MASK;
    }

    /* Read existing error bytes from FIFO to clear parity and framing error flags */
    while(U1STA & (_U1STA_FERR_MASK | _U1STA_PERR_MASK))
    {
        dummyData = (uint8_t )(U1RXREG );
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

    /* Clear error interrupt flag */
    IFS1CLR = _IFS1_U1EIF_MASK;

    /* Clear up the receive interrupt flag so that RX interrupt is not
     * triggered for error bytes */
    IFS1CLR = _IFS1_U1RXIF_MASK;

    return;
}

void UART1_Initialize( void )
{
    /* Set up UxMODE bits */
    /* STSEL  = 0*/
    /* PDSEL = 0 */
    /* BRGH = 0 */
    /* RXINV = 0 */
    /* ABAUD = 0 */
    /* LPBACK = 0 */
    /* WAKE = 0 */
    /* SIDL = 0 */
    /* RUNOVF = 0 */
    /* CLKSEL = 0 */
    /* SLPEN = 0 */
    U1MODE = 0x0;

    /* Enable UART1 Receiver, Transmitter and TX Interrupt selection */
    U1STASET = (_U1STA_UTXEN_MASK | _U1STA_URXEN_MASK | _U1STA_UTXISEL0_MASK);

    /* BAUD Rate register Setup */
    U1BRG = 19;

    IEC1CLR = _IEC1_U1TXIE_MASK;

    /* Initialize instance object */
    uart1Obj.rdCallback = NULL;
    uart1Obj.rdInIndex = uart1Obj.rdOutIndex = 0;
    uart1Obj.isRdNotificationEnabled = false;
    uart1Obj.isRdNotifyPersistently = false;
    uart1Obj.rdThreshold = 0;

    uart1Obj.wrCallback = NULL;
    uart1Obj.wrInIndex = uart1Obj.wrOutIndex = 0;
    uart1Obj.isWrNotificationEnabled = false;
    uart1Obj.isWrNotifyPersistently = false;
    uart1Obj.wrThreshold = 0;

    /* Turn ON UART1 */
    U1MODESET = _U1MODE_ON_MASK;

    /* Enable UART1_FAULT Interrupt */
    IEC1SET = _IEC1_U1EIE_MASK;

    /* Enable UART1_RX Interrupt */
    IEC1SET = _IEC1_U1RXIE_MASK;
}

bool UART1_SerialSetup( UART_SERIAL_SETUP *setup, uint32_t srcClkFreq )
{
    bool status = false;
    uint32_t baud = setup->baudRate;
    uint32_t brgValHigh = 0;
    uint32_t brgValLow = 0;
    uint32_t brgVal = 0;
    uint32_t uartMode;

    if (setup != NULL)
    {
        /* Turn OFF UART1 */
        U1MODECLR = _U1MODE_ON_MASK;

        if(srcClkFreq == 0)
        {
            srcClkFreq = UART1_FrequencyGet();
        }

        /* Calculate BRG value */
        brgValLow = ((srcClkFreq / baud) >> 4) - 1;
        brgValHigh = ((srcClkFreq / baud) >> 2) - 1;

        /* Check if the baud value can be set with low baud settings */
        if((brgValHigh >= 0) && (brgValHigh <= UINT16_MAX))
        {
            brgVal =  (((srcClkFreq >> 2) + (baud >> 1)) / baud ) - 1;
            U1MODESET = _U1MODE_BRGH_MASK;
        }
        else if ((brgValLow >= 0) && (brgValLow <= UINT16_MAX))
        {
            brgVal = ( ((srcClkFreq >> 4) + (baud >> 1)) / baud ) - 1;
            U1MODECLR = _U1MODE_BRGH_MASK;
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
               /* Configure UART1 mode */
               uartMode = U1MODE;
               uartMode &= ~_U1MODE_PDSEL_MASK;
               U1MODE = uartMode | setup->dataWidth;
            }
        }
        else
        {
            /* Configure UART1 mode */
            uartMode = U1MODE;
            uartMode &= ~_U1MODE_PDSEL_MASK;
            U1MODE = uartMode | setup->parity ;
        }

        /* Configure UART1 mode */
        uartMode = U1MODE;
        uartMode &= ~_U1MODE_STSEL_MASK;
        U1MODE = uartMode | setup->stopBits ;

        /* Configure UART1 Baud Rate */
        U1BRG = brgVal;

        U1MODESET = _U1MODE_ON_MASK;

        status = true;
    }

    return status;
}

/* This routine is only called from ISR. Hence do not disable/enable USART interrupts. */
static inline bool UART1_RxPushByte(uint8_t rdByte)
{
    uint32_t tempInIndex;
    bool isSuccess = false;

    tempInIndex = uart1Obj.rdInIndex + 1;

    if (tempInIndex >= UART1_READ_BUFFER_SIZE)
    {
        tempInIndex = 0;
    }

    if (tempInIndex == uart1Obj.rdOutIndex)
    {
        /* Queue is full - Report it to the application. Application gets a chance to free up space by reading data out from the RX ring buffer */
        if(uart1Obj.rdCallback != NULL)
        {
            uart1Obj.rdCallback(UART_EVENT_READ_BUFFER_FULL, uart1Obj.rdContext);

            /* Read the indices again in case application has freed up space in RX ring buffer */
            tempInIndex = uart1Obj.rdInIndex + 1;

            if (tempInIndex >= UART1_READ_BUFFER_SIZE)
            {
                tempInIndex = 0;
            }
        }
    }

    if (tempInIndex != uart1Obj.rdOutIndex)
    {
        UART1_ReadBuffer[uart1Obj.rdInIndex] = rdByte;
        uart1Obj.rdInIndex = tempInIndex;
        isSuccess = true;
    }
    else
    {
        /* Queue is full. Data will be lost. */
    }

    return isSuccess;
}

/* This routine is only called from ISR. Hence do not disable/enable USART interrupts. */
static void UART1_ReadNotificationSend(void)
{
    uint32_t nUnreadBytesAvailable;

    if (uart1Obj.isRdNotificationEnabled == true)
    {
        nUnreadBytesAvailable = UART1_ReadCountGet();

        if(uart1Obj.rdCallback != NULL)
        {
            if (uart1Obj.isRdNotifyPersistently == true)
            {
                if (nUnreadBytesAvailable >= uart1Obj.rdThreshold)
                {
                    uart1Obj.rdCallback(UART_EVENT_READ_THRESHOLD_REACHED, uart1Obj.rdContext);
                }
            }
            else
            {
                if (nUnreadBytesAvailable == uart1Obj.rdThreshold)
                {
                    uart1Obj.rdCallback(UART_EVENT_READ_THRESHOLD_REACHED, uart1Obj.rdContext);
                }
            }
        }
    }
}

size_t UART1_Read(uint8_t* pRdBuffer, const size_t size)
{
    size_t nBytesRead = 0;

    while (nBytesRead < size)
    {
        UART1_RX_INT_DISABLE();

        if (uart1Obj.rdOutIndex != uart1Obj.rdInIndex)
        {
            pRdBuffer[nBytesRead++] = UART1_ReadBuffer[uart1Obj.rdOutIndex++];

            if (uart1Obj.rdOutIndex >= UART1_READ_BUFFER_SIZE)
            {
                uart1Obj.rdOutIndex = 0;
            }
            UART1_RX_INT_ENABLE();
        }
        else
        {
            UART1_RX_INT_ENABLE();
            break;
        }
    }

    return nBytesRead;
}

size_t UART1_ReadCountGet(void)
{
    size_t nUnreadBytesAvailable;

    UART1_RX_INT_DISABLE();

    if ( uart1Obj.rdInIndex >=  uart1Obj.rdOutIndex)
    {
        nUnreadBytesAvailable =  uart1Obj.rdInIndex -  uart1Obj.rdOutIndex;
    }
    else
    {
        nUnreadBytesAvailable =  (UART1_READ_BUFFER_SIZE -  uart1Obj.rdOutIndex) + uart1Obj.rdInIndex;
    }

    UART1_RX_INT_ENABLE();

    return nUnreadBytesAvailable;
}

size_t UART1_ReadFreeBufferCountGet(void)
{
    return (UART1_READ_BUFFER_SIZE - 1) - UART1_ReadCountGet();
}

size_t UART1_ReadBufferSizeGet(void)
{
    return (UART1_READ_BUFFER_SIZE - 1);
}

bool UART1_ReadNotificationEnable(bool isEnabled, bool isPersistent)
{
    bool previousStatus = uart1Obj.isRdNotificationEnabled;

    uart1Obj.isRdNotificationEnabled = isEnabled;

    uart1Obj.isRdNotifyPersistently = isPersistent;

    return previousStatus;
}

void UART1_ReadThresholdSet(uint32_t nBytesThreshold)
{
    if (nBytesThreshold > 0)
    {
        uart1Obj.rdThreshold = nBytesThreshold;
    }
}

void UART1_ReadCallbackRegister( UART_RING_BUFFER_CALLBACK callback, uintptr_t context)
{
    uart1Obj.rdCallback = callback;

    uart1Obj.rdContext = context;
}

/* This routine is only called from ISR. Hence do not disable/enable USART interrupts. */
static bool UART1_TxPullByte(uint8_t* pWrByte)
{
    bool isSuccess = false;

    if (uart1Obj.wrOutIndex != uart1Obj.wrInIndex)
    {
        *pWrByte = UART1_WriteBuffer[uart1Obj.wrOutIndex++];

        if (uart1Obj.wrOutIndex >= UART1_WRITE_BUFFER_SIZE)
        {
            uart1Obj.wrOutIndex = 0;
        }
        isSuccess = true;
    }

    return isSuccess;
}

static inline bool UART1_TxPushByte(uint8_t wrByte)
{
    uint32_t tempInIndex;
    bool isSuccess = false;

    tempInIndex = uart1Obj.wrInIndex + 1;

    if (tempInIndex >= UART1_WRITE_BUFFER_SIZE)
    {
        tempInIndex = 0;
    }
    if (tempInIndex != uart1Obj.wrOutIndex)
    {
        UART1_WriteBuffer[uart1Obj.wrInIndex] = wrByte;
        uart1Obj.wrInIndex = tempInIndex;
        isSuccess = true;
    }
    else
    {
        /* Queue is full. Report Error. */
    }

    return isSuccess;
}

/* This routine is only called from ISR. Hence do not disable/enable USART interrupts. */
static void UART1_WriteNotificationSend(void)
{
    uint32_t nFreeWrBufferCount;

    if (uart1Obj.isWrNotificationEnabled == true)
    {
        nFreeWrBufferCount = UART1_WriteFreeBufferCountGet();

        if(uart1Obj.wrCallback != NULL)
        {
            if (uart1Obj.isWrNotifyPersistently == true)
            {
                if (nFreeWrBufferCount >= uart1Obj.wrThreshold)
                {
                    uart1Obj.wrCallback(UART_EVENT_WRITE_THRESHOLD_REACHED, uart1Obj.wrContext);
                }
            }
            else
            {
                if (nFreeWrBufferCount == uart1Obj.wrThreshold)
                {
                    uart1Obj.wrCallback(UART_EVENT_WRITE_THRESHOLD_REACHED, uart1Obj.wrContext);
                }
            }
        }
    }
}

static size_t UART1_WritePendingBytesGet(void)
{
    size_t nPendingTxBytes;

    if ( uart1Obj.wrInIndex >=  uart1Obj.wrOutIndex)
    {
        nPendingTxBytes =  uart1Obj.wrInIndex -  uart1Obj.wrOutIndex;
    }
    else
    {
        nPendingTxBytes =  (UART1_WRITE_BUFFER_SIZE -  uart1Obj.wrOutIndex) + uart1Obj.wrInIndex;
    }

    return nPendingTxBytes;
}

size_t UART1_WriteCountGet(void)
{
    size_t nPendingTxBytes;

    UART1_TX_INT_DISABLE();

    nPendingTxBytes = UART1_WritePendingBytesGet();

    /* Enable transmit interrupt only if any data is pending for transmission */
    if (UART1_WritePendingBytesGet() > 0)
    {
        UART1_TX_INT_ENABLE();
    }

    return nPendingTxBytes;
}

size_t UART1_Write(uint8_t* pWrBuffer, const size_t size )
{
    size_t nBytesWritten  = 0;

    UART1_TX_INT_DISABLE();

    while (nBytesWritten < size)
    {
        if (UART1_TxPushByte(pWrBuffer[nBytesWritten]) == true)
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
    if (UART1_WritePendingBytesGet() > 0)
    {
        /* Enable TX interrupt as data is pending for transmission */
        UART1_TX_INT_ENABLE();
    }

    return nBytesWritten;
}

size_t UART1_WriteFreeBufferCountGet(void)
{
    return (UART1_WRITE_BUFFER_SIZE - 1) - UART1_WriteCountGet();
}

size_t UART1_WriteBufferSizeGet(void)
{
    return (UART1_WRITE_BUFFER_SIZE - 1);
}

bool UART1_WriteNotificationEnable(bool isEnabled, bool isPersistent)
{
    bool previousStatus = uart1Obj.isWrNotificationEnabled;

    uart1Obj.isWrNotificationEnabled = isEnabled;

    uart1Obj.isWrNotifyPersistently = isPersistent;

    return previousStatus;
}

void UART1_WriteThresholdSet(uint32_t nBytesThreshold)
{
    if (nBytesThreshold > 0)
    {
        uart1Obj.wrThreshold = nBytesThreshold;
    }
}

void UART1_WriteCallbackRegister( UART_RING_BUFFER_CALLBACK callback, uintptr_t context)
{
    uart1Obj.wrCallback = callback;

    uart1Obj.wrContext = context;
}

UART_ERROR UART1_ErrorGet( void )
{
    UART_ERROR errors = UART_ERROR_NONE;
    uint32_t status = U1STA;

    errors = (UART_ERROR)(status & (_U1STA_OERR_MASK | _U1STA_FERR_MASK | _U1STA_PERR_MASK));

    if(errors != UART_ERROR_NONE)
    {
        UART1_ErrorClear();
    }

    /* All errors are cleared, but send the previous error state */
    return errors;
}

bool UART1_AutoBaudQuery( void )
{
    if(U1MODE & _U1MODE_ABAUD_MASK)
        return true;
    else
        return false;
}

void UART1_AutoBaudSet( bool enable )
{
    if( enable == true )
    {
        U1MODESET = _U1MODE_ABAUD_MASK;
    }

    /* Turning off ABAUD if it was on can lead to unpredictable behavior, so that
       direction of control is not allowed in this function.                      */
}

static void UART1_FAULT_InterruptHandler (void)
{
    /* Disable the fault interrupt */
    IEC1CLR = _IEC1_U1EIE_MASK;
    /* Disable the receive interrupt */
    IEC1CLR = _IEC1_U1RXIE_MASK;

    /* Client must call UARTx_ErrorGet() function to clear the errors */
    if( uart1Obj.rdCallback != NULL )
    {
        uart1Obj.rdCallback(UART_EVENT_READ_ERROR, uart1Obj.rdContext);
    }
}

static void UART1_RX_InterruptHandler (void)
{
    /* Clear UART1 RX Interrupt flag */
    IFS1CLR = _IFS1_U1RXIF_MASK;

    /* Keep reading until there is a character availabe in the RX FIFO */
    while((U1STA & _U1STA_URXDA_MASK) == _U1STA_URXDA_MASK)
    {
        if (UART1_RxPushByte( (uint8_t )(U1RXREG) ) == true)
        {
            UART1_ReadNotificationSend();
        }
        else
        {
            /* UART RX buffer is full */
        }
    }
}

static void UART1_TX_InterruptHandler (void)
{
    uint8_t wrByte;

    /* Clear UART1TX Interrupt flag */
    IFS1CLR = _IFS1_U1TXIF_MASK;

    /* Keep writing to the TX FIFO as long as there is space */
    while(!(U1STA & _U1STA_UTXBF_MASK))
    {
        if (UART1_TxPullByte(&wrByte) == true)
        {
            U1TXREG = wrByte;

            /* Send notification */
            UART1_WriteNotificationSend();
        }
        else
        {
            /* Nothing to transmit. Disable the data register empty interrupt. */
            UART1_TX_INT_DISABLE();
            break;
        }
    }
}

void UART_1_InterruptHandler (void)
{
    /* Call RX handler if RX interrupt flag is set */
    if ((IFS1 & _IFS1_U1RXIF_MASK) && (IEC1 & _IEC1_U1RXIE_MASK))
    {
        UART1_RX_InterruptHandler();
    }
    /* Call TX handler if TX interrupt flag is set */
    else if ((IFS1 & _IFS1_U1TXIF_MASK) && (IEC1 & _IEC1_U1TXIE_MASK))
    {
        UART1_TX_InterruptHandler();
    }
    /* Call Error handler if Error interrupt flag is set */
    else if ((IFS1 & _IFS1_U1EIF_MASK) && (IEC1 & _IEC1_U1EIE_MASK))
    {
        UART1_FAULT_InterruptHandler();
    }
}
