/*******************************************************************************
  USART2 PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_usart2.c

  Summary:
    USART2 PLIB Implementation File

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
#include "plib_usart2.h"

// *****************************************************************************
// *****************************************************************************
// Section: USART2 Implementation
// *****************************************************************************
// *****************************************************************************

void static USART2_ErrorClear( void )
{
    uint8_t dummyData = 0u;

    USART2_REGS->US_CR|= US_CR_RSTSTA_Msk;

    /* Flush existing error bytes from the RX FIFO */
    while( US_CSR_RXRDY_Msk == (USART2_REGS->US_CSR& US_CSR_RXRDY_Msk) )
    {
        dummyData = (USART2_REGS->US_RHR& US_RHR_RXCHR_Msk);
    }

    /* Ignore the warning */
    (void)dummyData;

    return;
}

void USART2_Initialize( void )
{
    /* Reset USART2 */
    USART2_REGS->US_CR = (US_CR_RSTRX_Msk | US_CR_RSTTX_Msk | US_CR_RSTSTA_Msk);

    /* Enable USART2 */
    USART2_REGS->US_CR = (US_CR_TXEN_Msk | US_CR_RXEN_Msk);

    /* Configure USART2 mode */
    USART2_REGS->US_MR = ((US_MR_USCLKS_MCK) | (0 << US_MR_MODE9_Pos) | US_MR_CHRL_8_BIT | US_MR_PAR_NO | US_MR_NBSTOP_1_BIT | (0 << US_MR_OVER_Pos));

    /* Configure USART2 Baud Rate */
    USART2_REGS->US_BRGR = US_BRGR_CD(976);

    return;
}

USART_ERROR USART2_ErrorGet( void )
{
    USART_ERROR errors = USART_ERROR_NONE;
    uint32_t status = USART2_REGS->US_CSR;

    errors = status & (US_CSR_OVRE_Msk | US_CSR_PARE_Msk | US_CSR_FRAME_Msk);

    if(errors != USART_ERROR_NONE)
    {
        USART2_ErrorClear();
    }

    /* All errors are cleared, but send the previous error state */
    return errors;
}

bool USART2_SerialSetup( USART_SERIAL_SETUP *setup, uint32_t srcClkFreq )
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
            srcClkFreq = USART2_FrequencyGet();
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

        /* Configure USART2 mode */
        usartMode = USART2_REGS->US_MR;
        usartMode &= ~(US_MR_CHRL_Msk | US_MR_MODE9_Msk | US_MR_PAR_Msk | US_MR_NBSTOP_Msk | US_MR_OVER_Msk);
        USART2_REGS->US_MR = usartMode | (setup->dataWidth | setup->parity | setup->stopBits | overSampVal);

        /* Configure USART2 Baud Rate */
        USART2_REGS->US_BRGR = US_BRGR_CD(brgVal);
        status = true;
    }

    return status;
}

bool USART2_Read( void *buffer, const size_t size )
{
    bool status = false;
    uint32_t errorStatus = 0;
    size_t processedSize = 0;
    uint8_t * lBuffer = (uint8_t *)buffer;

    if(NULL != lBuffer)
    {
        /* Clear errors before submitting the request.
         * ErrorGet clears errors internally. */
        USART2_ErrorGet();

        while( size > processedSize )
        {
            /* Error status */
            errorStatus = (USART2_REGS->US_CSR & (US_CSR_OVRE_Msk | US_CSR_FRAME_Msk | US_CSR_PARE_Msk));

            if(errorStatus != 0)
            {
                break;
            }

            if(US_CSR_RXRDY_Msk == (USART2_REGS->US_CSR & US_CSR_RXRDY_Msk))
            {
                *lBuffer++ = (USART2_REGS->US_RHR& US_RHR_RXCHR_Msk);
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

bool USART2_Write( void *buffer, const size_t size )
{
    bool status = false;
    size_t processedSize = 0;
    uint8_t * lBuffer = (uint8_t *)buffer;

    if(NULL != lBuffer)
    {
        while( size > processedSize )
        {
            if(US_CSR_TXEMPTY_Msk == (USART2_REGS->US_CSR& US_CSR_TXEMPTY_Msk))
            {
                USART2_REGS->US_THR = (US_THR_TXCHR(*lBuffer++) & US_THR_TXCHR_Msk);
                processedSize++;
            }
        }

        status = true;
    }

    return status;
}

int USART2_ReadByte(void)
{
    return(USART2_REGS->US_RHR & US_RHR_RXCHR_Msk);
}

void USART2_WriteByte(int data)
{
    while ((US_CSR_TXEMPTY_Msk == (USART2_REGS->US_CSR& US_CSR_TXEMPTY_Msk)) == 0);
    USART2_REGS->US_THR = (US_THR_TXCHR(data) & US_THR_TXCHR_Msk);
}

void inline USART2_Sync(void)
{
    while ((US_CSR_TXEMPTY_Msk == (USART2_REGS->US_CSR& US_CSR_TXEMPTY_Msk)) == 0);
}

bool USART2_TransmitterIsReady( void )
{
    if(US_CSR_TXEMPTY_Msk == (USART2_REGS->US_CSR & US_CSR_TXEMPTY_Msk))
    {
        return true;
    }

    return false;
}

bool USART2_ReceiverIsReady( void )
{
    if(US_CSR_RXRDY_Msk == (USART2_REGS->US_CSR & US_CSR_RXRDY_Msk))
    {
        return true;
    }

    return false;
}


