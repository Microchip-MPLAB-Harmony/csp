/*******************************************************************************
  DBGU PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_dbgu.c

  Summary:
    DBGU PLIB Implementation File

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
#include "plib_dbgu.h"

// *****************************************************************************
// *****************************************************************************
// Section: DBGU Implementation
// *****************************************************************************
// *****************************************************************************

void static DBGU_ErrorClear(void)
{
    uint8_t dummyData = 0u;

    DBGU_REGS->DBGU_CR = DBGU_CR_RSTSTA_Msk;

    /* Flush existing error bytes from the RX FIFO */
    while (DBGU_SR_RXRDY_Msk == (DBGU_REGS->DBGU_SR & DBGU_SR_RXRDY_Msk))
    {
        dummyData = (DBGU_REGS->DBGU_RHR & DBGU_RHR_RXCHR_Msk);
    }

    /* Ignore the warning */
    (void)dummyData;

    return;
}

void DBGU_Initialize(void)
{
    /* Reset DBGU */
    DBGU_REGS->DBGU_CR = (DBGU_CR_RSTRX_Msk | DBGU_CR_RSTTX_Msk | DBGU_CR_RSTSTA_Msk);

    /* Enable DBGU */
    DBGU_REGS->DBGU_CR = (DBGU_CR_TXEN_Msk | DBGU_CR_RXEN_Msk);

    /* Configure DBGU mode */
    DBGU_REGS->DBGU_MR = (DBGU_MR_BRSRCCK(0) | (DBGU_MR_PAR_NO) | (0 << DBGU_MR_FILTER_Pos));

    /* Configure DBGU Baud Rate */
    DBGU_REGS->DBGU_BRGR = DBGU_BRGR_CD(108);

    return;
}

DBGU_ERROR DBGU_ErrorGet(void)
{
    DBGU_ERROR errors = DBGU_ERROR_NONE;
    uint32_t status = DBGU_REGS->DBGU_SR;

    errors = (DBGU_ERROR)(status & (DBGU_SR_OVRE_Msk | DBGU_SR_PARE_Msk | DBGU_SR_FRAME_Msk));

    if (errors != DBGU_ERROR_NONE)
    {
        DBGU_ErrorClear();
    }

    /* All errors are cleared, but send the previous error state */
    return errors;
}

bool DBGU_SerialSetup(DBGU_SERIAL_SETUP *setup, uint32_t srcClkFreq)
{
    bool status = false;
    uint32_t baud = setup->baudRate;
    uint32_t brgVal = 0;
    uint32_t dbguMode;

    if (setup != NULL)
    {
        if (srcClkFreq == 0)
        {
            srcClkFreq = DBGU_FrequencyGet();
        }

        /* Calculate BRG value */
        brgVal = srcClkFreq / (16 * baud);

        /* If the target baud rate is acheivable using this clock */
        if (brgVal <= 65535)
        {
            /* Configure DBGU mode */
            dbguMode = DBGU_REGS->DBGU_MR;
            dbguMode &= ~DBGU_MR_PAR_Msk;
            DBGU_REGS->DBGU_MR = dbguMode | setup->parity ;

            /* Configure DBGU Baud Rate */
            DBGU_REGS->DBGU_BRGR = DBGU_BRGR_CD(brgVal);

            status = true;
        }
    }

    return status;
}

bool DBGU_Read(void *buffer, const size_t size)
{
    bool status = false;
    uint32_t errorStatus = 0;
    size_t processedSize = 0;

    uint8_t * lBuffer = (uint8_t *)buffer;

    if (NULL != lBuffer)
    {
        /* Clear errors before submitting the request.
         * ErrorGet clears errors internally. */
        DBGU_ErrorGet();

        while (size > processedSize)
        {
            /* Error status */
            errorStatus = (DBGU_REGS->DBGU_SR & (DBGU_SR_OVRE_Msk | DBGU_SR_FRAME_Msk | DBGU_SR_PARE_Msk));

            if (errorStatus != 0)
            {
                break;
            }

            if (DBGU_SR_RXRDY_Msk == (DBGU_REGS->DBGU_SR & DBGU_SR_RXRDY_Msk))
            {
                *lBuffer++ = (DBGU_REGS->DBGU_RHR & DBGU_RHR_RXCHR_Msk);
                processedSize++;
            }
        }

        if (size == processedSize)
        {
            status = true;
        }
    }

    return status;
}

bool DBGU_Write(void *buffer, const size_t size)
{
    bool status = false;
    size_t processedSize = 0;
    uint8_t * lBuffer = (uint8_t *)buffer;

    if (NULL != lBuffer)
    {
        while (size > processedSize)
        {
            if (DBGU_SR_TXEMPTY_Msk == (DBGU_REGS->DBGU_SR & DBGU_SR_TXEMPTY_Msk))
            {
                DBGU_REGS->DBGU_THR = (DBGU_THR_TXCHR(*lBuffer++) & DBGU_THR_TXCHR_Msk);
                processedSize++;
            }
        }

        status = true;
    }

    return status;
}

uint8_t DBGU_ReadByte(void)
{
    return (DBGU_REGS->DBGU_RHR & DBGU_RHR_RXCHR_Msk);
}

void DBGU_WriteByte(uint8_t data)
{
    while ((DBGU_REGS->DBGU_SR & DBGU_SR_TXEMPTY_Msk) != DBGU_SR_TXEMPTY_Msk);
    DBGU_REGS->DBGU_THR = (DBGU_THR_TXCHR(data) & DBGU_THR_TXCHR_Msk);
}

bool DBGU_TransmitterIsReady(void)
{
    return ((DBGU_REGS->DBGU_SR & DBGU_SR_TXEMPTY_Msk) == DBGU_SR_TXEMPTY_Msk);
}

bool DBGU_ReceiverIsReady(void)
{
    return ((DBGU_REGS->DBGU_SR & DBGU_SR_RXRDY_Msk) == DBGU_SR_RXRDY_Msk);
}

