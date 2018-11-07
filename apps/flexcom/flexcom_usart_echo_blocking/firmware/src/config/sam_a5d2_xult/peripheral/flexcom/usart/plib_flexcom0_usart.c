/*******************************************************************************
  FLEXCOM0 USART PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_flexcom0_usart.c

  Summary:
    FLEXCOM0 USART PLIB Implementation File

  Description
    This file defines the interface to the FLEXCOM0 USART peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

  Remarks:
    None.
*******************************************************************************/

/*******************************************************************************
Copyright (c) 2018 released Microchip Technology Inc.  All rights reserved.

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

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
/* This section lists the other files that are included in this file.
*/
#include "plib_flexcom0_usart.h"

// *****************************************************************************
// *****************************************************************************
// Section: FLEXCOM0 USART Implementation
// *****************************************************************************
// *****************************************************************************

void static FLEXCOM0_USART_ErrorClear( void )
{
    uint8_t dummyData = 0u;

    FLEXCOM0_REGS->FLEX_US_CR = FLEX_US_CR_RSTSTA_Msk;

    /* Flush existing error bytes from the RX FIFO */
    while( FLEX_US_CSR_RXRDY_Msk == (FLEXCOM0_REGS->FLEX_US_CSR& FLEX_US_CSR_RXRDY_Msk) )
    {
        dummyData = (FLEXCOM0_REGS->FLEX_US_RHR& FLEX_US_RHR_RXCHR_Msk);
    }

    /* Ignore the warning */
    (void)dummyData;

    return;
}

void FLEXCOM0_USART_Initialize( void )
{
    /* Set FLEXCOM USART operating mode */
    FLEXCOM0_REGS->FLEX_MR = FLEX_MR_OPMODE_USART;

    /* Reset FLEXCOM0 USART */
    FLEXCOM0_REGS->FLEX_US_CR = (FLEX_US_CR_RSTRX_Msk | FLEX_US_CR_RSTTX_Msk | FLEX_US_CR_RSTSTA_Msk);

    /* Enable FLEXCOM0 USART */
    FLEXCOM0_REGS->FLEX_US_CR = (FLEX_US_CR_TXEN_Msk | FLEX_US_CR_RXEN_Msk);

    /* Configure FLEXCOM0 USART mode */
    FLEXCOM0_REGS->FLEX_US_MR = ((FLEX_US_MR_USCLKS_MCK) | FLEX_US_MR_CHRL_8_BIT | FLEX_US_MR_PAR_NO | FLEX_US_MR_NBSTOP_1_BIT | (0 << FLEX_US_MR_OVER_Pos));

    /* Configure FLEXCOM0 USART Baud Rate */
    FLEXCOM0_REGS->FLEX_US_BRGR = FLEX_US_BRGR_CD(45);

    return;
}

FLEXCOM_USART_ERROR FLEXCOM0_USART_ErrorGet( void )
{
    FLEXCOM_USART_ERROR errors = FLEXCOM_USART_ERROR_NONE;
    uint32_t status = FLEXCOM0_REGS->FLEX_US_CSR;

    /* Collect all errors */
    if(status & FLEX_US_CSR_OVRE_Msk)
    {
        errors = FLEXCOM_USART_ERROR_OVERRUN;
    }
    if(status & FLEX_US_CSR_PARE_Msk)
    {
        errors |= FLEXCOM_USART_ERROR_PARITY;
    }
    if(status & FLEX_US_CSR_FRAME_Msk)
    {
        errors |= FLEXCOM_USART_ERROR_FRAMING;
    }

    if(errors != FLEXCOM_USART_ERROR_NONE)
    {
        FLEXCOM0_USART_ErrorClear();
    }

    /* All errors are cleared, but send the previous error state */
    return errors;
}

bool FLEXCOM0_USART_SerialSetup( FLEXCOM_USART_SERIAL_SETUP *setup, uint32_t srcClkFreq )
{
    uint32_t baud = 0;
    uint32_t brgVal = 0;
    uint32_t overSampVal = 0;
    uint32_t usartMode;
    bool status = false;

    if (setup != NULL)
    {
        baud = setup->baudRate;
        if(srcClkFreq == 0)
        {
            srcClkFreq = FLEXCOM0_USART_FrequencyGet();
        }

        /* Calculate BRG value */
        if (srcClkFreq >= (16 * baud))
        {
            brgVal = (srcClkFreq / (16 * baud));
        }
        else
        {
            brgVal = (srcClkFreq / (8 * baud));
            overSampVal = (1 << FLEX_US_MR_OVER_Pos) & FLEX_US_MR_OVER_Msk;
        }

        /* Configure FLEXCOM0 USART mode */
        usartMode = FLEXCOM0_REGS->FLEX_US_MR;
        usartMode &= ~(FLEX_US_MR_CHRL_Msk | FLEX_US_MR_MODE9_Msk | FLEX_US_MR_PAR_Msk | FLEX_US_MR_NBSTOP_Msk | FLEX_US_MR_OVER_Msk);
        FLEXCOM0_REGS->FLEX_US_MR = usartMode | ((uint32_t)setup->dataWidth | (uint32_t)setup->parity | (uint32_t)setup->stopBits | overSampVal);

        /* Configure FLEXCOM0 USART Baud Rate */
        FLEXCOM0_REGS->FLEX_US_BRGR = FLEX_US_BRGR_CD(brgVal);
        status = true;
    }

    return status;
}

bool FLEXCOM0_USART_Read( void *buffer, const size_t size )
{
    bool status = false;
    uint32_t errorStatus = 0;
    size_t processedSize = 0;
    uint8_t * lBuffer = (uint8_t *)buffer;

    if(NULL != lBuffer)
    {
        /* Clear errors before submitting the request.
         * ErrorGet clears errors internally. */
        FLEXCOM0_USART_ErrorGet();

        while( size > processedSize )
        {
            /* Error status */
            errorStatus = (FLEXCOM0_REGS->FLEX_US_CSR & (FLEX_US_CSR_OVRE_Msk | FLEX_US_CSR_FRAME_Msk | FLEX_US_CSR_PARE_Msk));

            if(errorStatus != 0)
            {
                break;
            }

            if(FLEX_US_CSR_RXRDY_Msk == (FLEXCOM0_REGS->FLEX_US_CSR & FLEX_US_CSR_RXRDY_Msk))
            {
                *lBuffer++ = (FLEXCOM0_REGS->FLEX_US_RHR& FLEX_US_RHR_RXCHR_Msk);
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

bool FLEXCOM0_USART_Write( void *buffer, const size_t size )
{
    bool status = false;
    size_t processedSize = 0;
    uint8_t * lBuffer = (uint8_t *)buffer;

    if(NULL != lBuffer)
    {
        while( size > processedSize )
        {
            if(FLEX_US_CSR_TXEMPTY_Msk == (FLEXCOM0_REGS->FLEX_US_CSR& FLEX_US_CSR_TXEMPTY_Msk))
            {
                FLEXCOM0_REGS->FLEX_US_THR = (FLEX_US_THR_TXCHR(*lBuffer++) & FLEX_US_THR_TXCHR_Msk);
                processedSize++;
            }
        }

        status = true;
    }

    return status;
}

uint8_t FLEXCOM0_ReadByte(void)
{
    return(FLEXCOM0_REGS->FLEX_US_RHR & FLEX_US_RHR_RXCHR_Msk);
}

void FLEXCOM0_WriteByte(uint8_t data)
{
    while ((FLEX_US_CSR_TXEMPTY_Msk == (FLEXCOM0_REGS->FLEX_US_CSR & FLEX_US_CSR_TXEMPTY_Msk)) == 0);
    FLEXCOM0_REGS->FLEX_US_THR = (FLEX_US_THR_TXCHR(data) & FLEX_US_THR_TXCHR_Msk);
}

void inline FLEXCOM0_Sync(void)
{
    while ((FLEX_US_CSR_TXEMPTY_Msk == (FLEXCOM0_REGS->FLEX_US_CSR & FLEX_US_CSR_TXEMPTY_Msk)) == 0);
}

bool FLEXCOM0_USART_TransmitterIsReady( void )
{
    bool status = false;

    if(FLEX_US_CSR_TXEMPTY_Msk == (FLEXCOM0_REGS->FLEX_US_CSR& FLEX_US_CSR_TXEMPTY_Msk))
    {
        status = true;
    }

    return status;
}

bool FLEXCOM0_USART_ReceiverIsReady( void )
{
    bool status = false;

    if(FLEX_US_CSR_RXRDY_Msk == (FLEXCOM0_REGS->FLEX_US_CSR& FLEX_US_CSR_RXRDY_Msk))
    {
        status = true;
    }

    return status;
}

