/*******************************************************************************
  UART6 PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_uart6.c

  Summary:
    UART6 PLIB Implementation File

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
#include "plib_uart6.h"

// *****************************************************************************
// *****************************************************************************
// Section: UART6 Implementation
// *****************************************************************************
// *****************************************************************************


void static UART6_ErrorClear( void )
{
    /* rxBufferLen = (FIFO level + RX register) */
    uint8_t rxBufferLen = UART_RXFIFO_DEPTH;
    uint8_t dummyData = 0u;

    /* If it's a overrun error then clear it to flush FIFO */
    if(U6STA & _U6STA_OERR_MASK)
    {
        U6STACLR = _U6STA_OERR_MASK;
    }

    /* Read existing error bytes from FIFO to clear parity and framing error flags */
    while(U6STA & (_U6STA_FERR_MASK | _U6STA_PERR_MASK))
    {
        dummyData = (uint8_t )(U6RXREG );
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

    return;
}

void UART6_Initialize( void )
{
    /* Set up UxMODE bits */
    /* STSEL  = 0*/
    /* PDSEL = 0 */
    /* BRGH = 1 */
    /* RXINV = 0 */
    /* ABAUD = 0 */
    /* LPBACK = 0 */
    /* WAKE = 0 */
    /* SIDL = 0 */
    /* RUNOVF = 0 */
    /* CLKSEL = 0 */
    /* SLPEN = 0 */
    U6MODE = 0x8;

    /* Enable UART6 Receiver and Transmitter */
    U6STASET = (_U6STA_UTXEN_MASK | _U6STA_URXEN_MASK);

    /* BAUD Rate register Setup */
    U6BRG = 129;

    /* Turn ON UART6 */
    U6MODESET = _U6MODE_ON_MASK;
}

bool UART6_SerialSetup( UART_SERIAL_SETUP *setup, uint32_t srcClkFreq )
{
    bool status = false;
    uint32_t baud = setup->baudRate;
    uint32_t brgValHigh = 0;
    uint32_t brgValLow = 0;
    uint32_t brgVal = 0;
    uint32_t uartMode;

    if (setup != NULL)
    {
        /* Turn OFF UART6 */
        U6MODECLR = _U6MODE_ON_MASK;

        if(srcClkFreq == 0)
        {
            srcClkFreq = UART6_FrequencyGet();
        }

        /* Calculate BRG value */
        brgValLow = ((srcClkFreq / baud) >> 4) - 1;
        brgValHigh = ((srcClkFreq / baud) >> 2) - 1;

        /* Check if the baud value can be set with low baud settings */
        if((brgValHigh >= 0) && (brgValHigh <= UINT16_MAX))
        {
            brgVal =  (((srcClkFreq >> 2) + (baud >> 1)) / baud ) - 1;
            U6MODESET = _U6MODE_BRGH_MASK;
        }
        else if ((brgValLow >= 0) && (brgValLow <= UINT16_MAX))
        {
            brgVal = ( ((srcClkFreq >> 4) + (baud >> 1)) / baud ) - 1;
            U6MODECLR = _U6MODE_BRGH_MASK;
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
               /* Configure UART6 mode */
               uartMode = U6MODE;
               uartMode &= ~_U6MODE_PDSEL_MASK;
               U6MODE = uartMode | setup->dataWidth;
            }
        }
        else
        {
            /* Configure UART6 mode */
            uartMode = U6MODE;
            uartMode &= ~_U6MODE_PDSEL_MASK;
            U6MODE = uartMode | setup->parity ;
        }

        /* Configure UART6 mode */
        uartMode = U6MODE;
        uartMode &= ~_U6MODE_STSEL_MASK;
        U6MODE = uartMode | setup->stopBits ;

        /* Configure UART6 Baud Rate */
        U6BRG = brgVal;

        U6MODESET = _U6MODE_ON_MASK;

        status = true;
    }

    return status;
}

bool UART6_Read(void* buffer, const size_t size )
{
    bool status = false;
    uint8_t* lBuffer = (uint8_t* )buffer;
    uint32_t errorStatus = 0;
    size_t processedSize = 0;

    if(lBuffer != NULL)
    {
        /* Clear errors before submitting the request.
         * ErrorGet clears errors internally. */
        UART6_ErrorGet();

        while( size > processedSize )
        {
            /* Error status */
            errorStatus = (U6STA & (_U6STA_OERR_MASK | _U6STA_FERR_MASK | _U6STA_PERR_MASK));

            if(errorStatus != 0)
            {
                break;
            }

            /* Receiver buffer has data */
            if((U6STA & _U6STA_URXDA_MASK) == _U6STA_URXDA_MASK)
            {
                *lBuffer++ = (U6RXREG );
                processedSize++;
            }
        }

        if(size == processedSize)
        {
            status = true;
        }
    }

    return status;
}

bool UART6_Write( void* buffer, const size_t size )
{
    bool status = false;
    uint8_t* lBuffer = (uint8_t*)buffer;
    size_t processedSize = 0;

    if(lBuffer != NULL)
    {
        while( size > processedSize )
        {
            if(!(U6STA & _U6STA_UTXBF_MASK))
            {
                U6TXREG = *lBuffer++;
                processedSize++;
            }
        }

        status = true;
    }

    return status;
}

UART_ERROR UART6_ErrorGet( void )
{
    UART_ERROR errors = UART_ERROR_NONE;
    uint32_t status = U6STA;

    errors = (UART_ERROR)(status & (_U6STA_OERR_MASK | _U6STA_FERR_MASK | _U6STA_PERR_MASK));

    if(errors != UART_ERROR_NONE)
    {
        UART6_ErrorClear();
    }

    /* All errors are cleared, but send the previous error state */
    return errors;
}

void UART6_WriteByte(int data)
{
    while ((U6STA & _U6STA_UTXBF_MASK));

    U6TXREG = data;
}

bool UART6_TransmitterIsReady( void )
{
    bool status = false;

    if(!(U6STA & _U6STA_UTXBF_MASK))
    {
        status = true;
    }

    return status;
}

bool UART6_TransmitComplete( void )
{
    bool transmitComplete = false;

    if((U6STA & _U6STA_TRMT_MASK))
    {
        transmitComplete = true;
    }

    return transmitComplete;
}

int UART6_ReadByte( void )
{
    return(U6RXREG);
}

bool UART6_ReceiverIsReady( void )
{
    bool status = false;

    if(_U6STA_URXDA_MASK == (U6STA & _U6STA_URXDA_MASK))
    {
        status = true;
    }

    return status;
}
