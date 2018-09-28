/*******************************************************************************
  USART0 PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_usart0.c

  Summary:
    USART0 PLIB Implementation File

  Description:
    None

*******************************************************************************/

/*******************************************************************************
Copyright (c) 2017 released Microchip Technology Inc.  All rights reserved.

Microchip licenses to you the right to use, modify, copy and distribute
Software only when embedded on a Microchip microcontroller or digital signal
controller that is integrated into your product or third party product
(pursuant to the sublicense terms in the accompanying license agreement).

You should refer to the license agreement accompanying this Software for
additional information regarding your rights and obligations.

SOFTWARE AND DOCUMENTATION ARE PROVIDED AS IS  WITHOUT  WARRANTY  OF  ANY  KIND,
EITHER EXPRESS  OR  IMPLIED,  INCLUDING  WITHOUT  LIMITATION,  ANY  WARRANTY  OF
MERCHANTABILITY, TITLE, NON-INFRINGEMENT AND FITNESS FOR A  PARTICULAR  PURPOSE.
IN NO EVENT SHALL MICROCHIP OR  ITS  LICENSORS  BE  LIABLE  OR  OBLIGATED  UNDER
CONTRACT, NEGLIGENCE, STRICT LIABILITY, CONTRIBUTION,  BREACH  OF  WARRANTY,  OR
OTHER LEGAL  EQUITABLE  THEORY  ANY  DIRECT  OR  INDIRECT  DAMAGES  OR  EXPENSES
INCLUDING BUT NOT LIMITED TO ANY  INCIDENTAL,  SPECIAL,  INDIRECT,  PUNITIVE  OR
CONSEQUENTIAL DAMAGES, LOST  PROFITS  OR  LOST  DATA,  COST  OF  PROCUREMENT  OF
SUBSTITUTE  GOODS,  TECHNOLOGY,  SERVICES,  OR  ANY  CLAIMS  BY  THIRD   PARTIES
(INCLUDING BUT NOT LIMITED TO ANY DEFENSE  THEREOF),  OR  OTHER  SIMILAR  COSTS.
*******************************************************************************/

#include "device.h"
#include "plib_usart0.h"

// *****************************************************************************
// *****************************************************************************
// Section: USART0 Implementation
// *****************************************************************************
// *****************************************************************************

void static USART0_ErrorClear( void )
{
    uint8_t dummyData = 0u;

    USART0_REGS->US_CR|= US_CR_RSTSTA_Msk;

    /* Flush existing error bytes from the RX FIFO */
    while( US_CSR_RXRDY_Msk == (USART0_REGS->US_CSR& US_CSR_RXRDY_Msk) )
    {
        dummyData = (USART0_REGS->US_RHR& US_RHR_RXCHR_Msk);
    }

    /* Ignore the warning */
    (void)dummyData;

    return;
}

void USART0_Initialize( void )
{
    /* Reset USART0 */
    USART0_REGS->US_CR = (US_CR_RSTRX_Msk | US_CR_RSTTX_Msk | US_CR_RSTSTA_Msk);

    /* Enable USART0 */
    USART0_REGS->US_CR = (US_CR_TXEN_Msk | US_CR_RXEN_Msk);

    /* Configure USART0 mode */
    USART0_REGS->US_MR = ((US_MR_USCLKS_MCK) | (0 << US_MR_MODE9_Pos) | US_MR_CHRL_8_BIT | US_MR_PAR_NO | US_MR_NBSTOP_1_BIT | (0 << US_MR_OVER_Pos));

    /* Configure USART0 Baud Rate */
    USART0_REGS->US_BRGR = US_BRGR_CD(81);

    return;
}

USART_ERROR USART0_ErrorGet( void )
{
    USART_ERROR errors = USART_ERROR_NONE;
    uint32_t status = USART0_REGS->US_CSR;

    errors = status & (US_CSR_OVRE_Msk | US_CSR_PARE_Msk | US_CSR_FRAME_Msk);

    if(errors != USART_ERROR_NONE)
    {
        USART0_ErrorClear();
    }

    /* All errors are cleared, but send the previous error state */
    return errors;
}

bool USART0_SerialSetup( USART_SERIAL_SETUP *setup, uint32_t srcClkFreq )
{
    uint32_t baud = setup->baudRate;
    uint32_t brgVal = 0;
    uint32_t overSampVal = 0;
    uint32_t usartMode;
    bool status = false;

    if (setup != NULL)
    {
        baud = setup->baudRate;
        if(srcClkFreq == 0)
        {
            srcClkFreq = USART0_FrequencyGet();
        }

        /* Calculate BRG value */
        if (srcClkFreq >= (16 * baud))
        {
            brgVal = (srcClkFreq / (16 * baud));
        }
        else
        {
            brgVal = (srcClkFreq / (8 * baud));
            overSampVal = US_MR_OVER(1);
        }

        /* Configure USART0 mode */
        usartMode = USART0_REGS->US_MR;
        usartMode &= ~(US_MR_CHRL_Msk | US_MR_MODE9_Msk | US_MR_PAR_Msk | US_MR_NBSTOP_Msk | US_MR_OVER_Msk);
        USART0_REGS->US_MR = usartMode | (setup->dataWidth | setup->parity | setup->stopBits | overSampVal);

        /* Configure USART0 Baud Rate */
        USART0_REGS->US_BRGR = US_BRGR_CD(brgVal);
        status = true;
    }

    return status;
}

bool USART0_Read( void *buffer, const size_t size )
{
    bool status = false;
    uint32_t errorStatus = 0;
    size_t processedSize = 0;
    uint8_t * lBuffer = (uint8_t *)buffer;

    if(NULL != lBuffer)
    {
        /* Clear errors before submitting the request.
         * ErrorGet clears errors internally. */
        USART0_ErrorGet();

        while( size > processedSize )
        {
            /* Error status */
            errorStatus = (USART0_REGS->US_CSR & (US_CSR_OVRE_Msk | US_CSR_FRAME_Msk | US_CSR_PARE_Msk));

            if(errorStatus != 0)
            {
                break;
            }

            if(US_CSR_RXRDY_Msk == (USART0_REGS->US_CSR & US_CSR_RXRDY_Msk))
            {
                *lBuffer++ = (USART0_REGS->US_RHR& US_RHR_RXCHR_Msk);
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

bool USART0_Write( void *buffer, const size_t size )
{
    bool status = false;
    size_t processedSize = 0;
    uint8_t * lBuffer = (uint8_t *)buffer;

    if(NULL != lBuffer)
    {
        while( size > processedSize )
        {
            if(US_CSR_TXEMPTY_Msk == (USART0_REGS->US_CSR& US_CSR_TXEMPTY_Msk))
            {
                USART0_REGS->US_THR = (US_THR_TXCHR(*lBuffer++) & US_THR_TXCHR_Msk);
                processedSize++;
            }
        }

        status = true;
    }

    return status;
}

int USART0_ReadByte(void)
{
    return(USART0_REGS->US_RHR & US_RHR_RXCHR_Msk);
}

void USART0_WriteByte(int data)
{
    while ((US_CSR_TXEMPTY_Msk == (USART0_REGS->US_CSR& US_CSR_TXEMPTY_Msk)) == 0);
    USART0_REGS->US_THR = (US_THR_TXCHR(data) & US_THR_TXCHR_Msk);
}

void inline USART0_Sync(void)
{
    while ((US_CSR_TXEMPTY_Msk == (USART0_REGS->US_CSR& US_CSR_TXEMPTY_Msk)) == 0);
}

bool USART0_TransmitterIsReady( void )
{
    if(US_CSR_TXEMPTY_Msk == (USART0_REGS->US_CSR & US_CSR_TXEMPTY_Msk))
    {
        return true;
    }

    return false;
}

bool USART0_ReceiverIsReady( void )
{
    if(US_CSR_RXRDY_Msk == (USART0_REGS->US_CSR & US_CSR_RXRDY_Msk))
    {
        return true;
    }

    return false;
}


