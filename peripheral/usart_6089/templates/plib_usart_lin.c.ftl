/*******************************************************************************
  ${USART_INSTANCE_NAME} PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${USART_INSTANCE_NAME?lower_case}_LIN.c

  Summary:
    ${USART_INSTANCE_NAME} PLIB Implementation File in LIN mode

  Description:
    None

*******************************************************************************/

/*******************************************************************************
* Copyright (C) 2018 Microchip Technology Inc. and its subsidiaries.
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
#include "plib_${USART_INSTANCE_NAME?lower_case}_lin.h"
<#if core.CoreSysIntFile == true>
#include "interrupts.h"
</#if>

<#--Implementation-->
// *****************************************************************************
// *****************************************************************************
// Section: ${USART_INSTANCE_NAME} Implementation
// *****************************************************************************
// *****************************************************************************

static void ${USART_INSTANCE_NAME}_ErrorClear( void )
{
    uint32_t dummyData = 0U;

   if ((${USART_INSTANCE_NAME}_REGS->US_CSR & (US_CSR_USART_OVRE_Msk | US_CSR_USART_PARE_Msk | US_CSR_USART_FRAME_Msk)) != 0U)
   {
        /* Clear the error flags */
        ${USART_INSTANCE_NAME}_REGS->US_CR = US_CR_USART_RSTSTA_Msk;

        /* Flush existing error bytes from the RX FIFO */
        while ((${USART_INSTANCE_NAME}_REGS->US_CSR & US_CSR_USART_RXRDY_Msk) != 0U)
        {
            dummyData = ${USART_INSTANCE_NAME}_REGS->US_RHR & US_RHR_RXCHR_Msk;
        }
   }

    /* Ignore the warning */
    (void)dummyData;
}

void ${USART_INSTANCE_NAME}_Initialize( void )
{
    /* Reset ${USART_INSTANCE_NAME} */
    ${USART_INSTANCE_NAME}_REGS->US_CR = (US_CR_USART_RSTRX_Msk | US_CR_USART_RSTTX_Msk | US_CR_USART_RSTSTA_Msk);

    /* Enable ${USART_INSTANCE_NAME} */
    ${USART_INSTANCE_NAME}_REGS->US_CR = (US_CR_USART_TXEN_Msk | US_CR_USART_RXEN_Msk);

    /* Configure ${USART_INSTANCE_NAME} mode */
    <#if USART_MR_MODE9 == true>
    ${USART_INSTANCE_NAME}_REGS->US_MR = (US_MR_USART_USCLKS_${USART_CLK_SRC} | US_MR_USART_MODE9_Msk | US_MR_USART_PAR_${USART_MR_PAR} | US_MR_USART_NBSTOP_${USART_MR_NBSTOP} | US_MR_USART_OVER(${USART_MR_OVER?string}));
    <#else>
    ${USART_INSTANCE_NAME}_REGS->US_MR = (US_MR_USART_USCLKS_${USART_CLK_SRC} | US_MR_USART_CHRL_${USART_MR_CHRL} | US_MR_USART_PAR_${USART_MR_PAR} | US_MR_USART_NBSTOP_${USART_MR_NBSTOP} | US_MR_USART_OVER(${USART_MR_OVER?string}));
    </#if>

    /* Configure ${USART_INSTANCE_NAME} Baud Rate */
    ${USART_INSTANCE_NAME}_REGS->US_BRGR = US_BRGR_CD(${BRG_VALUE}U);

	<#if USART_MODE == "LIN_MASTER" || USART_MODE == "LIN_SLAVE">
    ${USART_INSTANCE_NAME}_REGS->US_MR |= US_MR_USART_MODE_${USART_MODE};
 <@compress>${USART_INSTANCE_NAME}_REGS->US_LINMR = ${USART_LIN_LINMR_PARDIS?then('US_LINMR_PARDIS_Msk |', '')}
        ${USART_LIN_LINMR_CHKDIS?then('US_LINMR_CHKDIS_Msk |', '')}
        ${USART_LIN_LINMR_FSDIS?then('US_LINMR_FSDIS_Msk |', '')}
        ${USART_LIN_LINMR_SYNCDIS?then('US_LINMR_SYNCDIS_Msk |', '')}
        US_LINMR_CHKTYP(${USART_LIN_LINMR_CHKTYP}U) | US_LINMR_DLM(${USART_LIN_LINMR_DLM}U) |
        US_LINMR_DLC(${USART_LIN_LINMR_DLC}U) | US_LINMR_WKUPTYP(${USART_LIN_LINMR_WKUPTYP}U); </@compress>    
    </#if>
}

USART_ERROR ${USART_INSTANCE_NAME}_ErrorGet( void )
{
    USART_ERROR errors = USART_ERROR_NONE;

    uint32_t status = ${USART_INSTANCE_NAME}_REGS->US_CSR;

    errors = (USART_ERROR)(status & (US_CSR_USART_OVRE_Msk | US_CSR_USART_PARE_Msk | US_CSR_USART_FRAME_Msk));

    if(errors != USART_ERROR_NONE)
    {
        ${USART_INSTANCE_NAME}_ErrorClear();
    }

    /* All errors are cleared, but send the previous error state */
    return errors;
}

bool ${USART_INSTANCE_NAME}_SerialSetup( USART_SERIAL_SETUP *setup, uint32_t srcClkFreq )
{
    uint32_t baud;
    uint32_t brgVal = 0;
    uint32_t overSampVal = 0;
    uint32_t usartMode;
    bool status = false;

    if (setup != NULL)
    {
        baud = setup->baudRate;

        if(srcClkFreq == 0U)
        {
            srcClkFreq = ${USART_INSTANCE_NAME}_FrequencyGet();
        }

        /* Calculate BRG value */
        if (srcClkFreq >= (16U * baud))
        {
            brgVal = (srcClkFreq / (16U * baud));
        }
        else if (srcClkFreq >= (8U * baud))
        {
            brgVal = (srcClkFreq / (8U * baud));
            overSampVal = US_MR_USART_OVER(1U);
        }
        else
        {
            return false;
        }

        if (brgVal > 65535U)
        {
            /* The requested baud is so low that the ratio of srcClkFreq to baud exceeds the 16-bit register value of CD register */
            return false;
        }

        /* Configure ${USART_INSTANCE_NAME} mode */
        usartMode = ${USART_INSTANCE_NAME}_REGS->US_MR;
        usartMode &= ~(US_MR_USART_CHRL_Msk | US_MR_USART_MODE9_Msk | US_MR_USART_PAR_Msk | US_MR_USART_NBSTOP_Msk | US_MR_USART_OVER_Msk);
        ${USART_INSTANCE_NAME}_REGS->US_MR = usartMode | ((uint32_t)setup->dataWidth | (uint32_t)setup->parity | (uint32_t)setup->stopBits | (uint32_t)overSampVal);

        /* Configure ${USART_INSTANCE_NAME} Baud Rate */
        ${USART_INSTANCE_NAME}_REGS->US_BRGR = US_BRGR_CD(brgVal);
        status = true;
    }

    return status;
}

bool ${USART_INSTANCE_NAME}_Read( void *buffer, const size_t size )
{
    bool status = false;
    uint32_t errorStatus = 0;
    size_t processedSize = 0;
    if(buffer != NULL)
    {
        uint8_t* pu8Data = (uint8_t *)buffer;
        uint16_t* pu16Data = (uint16_t*)buffer;
        /* Clear errors that may have got generated when there was no active read request pending */
        ${USART_INSTANCE_NAME}_ErrorClear();

        while( size > processedSize )
        {
            while ((${USART_INSTANCE_NAME}_REGS->US_CSR & US_CSR_USART_RXRDY_Msk) == 0U)
            {
                /* Wait for RXRDY flag */
            }

            /* Read error status */
            errorStatus = (${USART_INSTANCE_NAME}_REGS->US_CSR & (US_CSR_USART_OVRE_Msk | US_CSR_USART_FRAME_Msk | US_CSR_USART_PARE_Msk));
            if(errorStatus != 0U)
            {
                break;
            }

            if ((${USART_INSTANCE_NAME}_REGS->US_MR & US_MR_USART_MODE9_Msk) != 0U)
            {
                *pu16Data = (uint16_t)(${USART_INSTANCE_NAME}_REGS->US_RHR & US_RHR_RXCHR_Msk);
                pu16Data++;
            }
            else
            {
                *pu8Data = (uint8_t)(${USART_INSTANCE_NAME}_REGS->US_RHR & US_RHR_RXCHR_Msk);
                pu8Data++;
            }

            processedSize++;
        }

        if(size == processedSize)
        {
            status = true;
        }
    }

    return status;
}

bool ${USART_INSTANCE_NAME}_Write( void *buffer, const size_t size )
{
    bool status = false;
    size_t processedSize = 0;
    if(NULL != buffer)
    {
        uint8_t* pu8Data = (uint8_t *)buffer;
        uint16_t* pu16Data = (uint16_t*)buffer;

        while( size > processedSize )
        {
            while ((${USART_INSTANCE_NAME}_REGS->US_CSR & US_CSR_USART_TXRDY_Msk) == 0U)
            {
                /*Wait for TXRDY */
            }

            if ((${USART_INSTANCE_NAME}_REGS->US_MR & US_MR_USART_MODE9_Msk) != 0U)
            {
                ${USART_INSTANCE_NAME}_REGS->US_THR = pu16Data[processedSize] & US_THR_TXCHR_Msk;
            }
            else
            {
                ${USART_INSTANCE_NAME}_REGS->US_THR = pu8Data[processedSize] & US_THR_TXCHR_Msk;
            }
            processedSize++;
        }

        status = true;
    }
    return status;
}

int ${USART_INSTANCE_NAME}_ReadByte( void )
{
    uint32_t data = ${USART_INSTANCE_NAME}_REGS->US_RHR & US_RHR_RXCHR_Msk;
    return (int)data;
}

void ${USART_INSTANCE_NAME}_WriteByte( int data )
{
    while ((${USART_INSTANCE_NAME}_REGS->US_CSR & US_CSR_USART_TXRDY_Msk) == 0U)
    {
        /* Wait for TXRDY flag */
    }
    ${USART_INSTANCE_NAME}_REGS->US_THR = US_THR_TXCHR(data);
}

bool ${USART_INSTANCE_NAME}_TransmitterIsReady( void )
{
    return ((${USART_INSTANCE_NAME}_REGS->US_CSR & US_CSR_USART_TXRDY_Msk) != 0U);
}

bool ${USART_INSTANCE_NAME}_ReceiverIsReady( void )
{
    return ((${USART_INSTANCE_NAME}_REGS->US_CSR & US_CSR_USART_RXRDY_Msk) != 0U);
}

bool ${USART_INSTANCE_NAME}_TransmitComplete( void )
{
    return((${USART_INSTANCE_NAME}_REGS->US_CSR & US_CSR_USART_TXEMPTY_Msk) != 0U);

}

<#if USART_MODE == "LIN_MASTER" || USART_MODE == "LIN_SLAVE">
void ${USART_INSTANCE_NAME}_LIN_NodeActionSet( USART_LIN_NACT action )
{
    ${USART_INSTANCE_NAME}_REGS->US_LINMR &= ~(US_LINMR_NACT_Msk);
    ${USART_INSTANCE_NAME}_REGS->US_LINMR |= US_LINMR_NACT(action);
}

bool ${USART_INSTANCE_NAME}_LIN_IdentifierWrite( uint8_t id)
{
	bool status = false; 
	${USART_INSTANCE_NAME}_REGS->US_CR = US_CR_USART_RSTSTA_Msk;
    
    if((${USART_INSTANCE_NAME}_REGS->US_CSR & US_CSR_USART_TXRDY_Msk) != 0U)
    {
        ${USART_INSTANCE_NAME}_REGS->US_LINIR = id;
		status = true;
    }
	
	return status;
}

uint8_t ${USART_INSTANCE_NAME}_LIN_IdentifierRead( void)
{
    return ${USART_INSTANCE_NAME}_REGS->US_LINIR;
}

void ${USART_INSTANCE_NAME}_LIN_ParityEnable(bool parityEnable)
{
    if(parityEnable == true)
        USART0_REGS->US_LINMR &= ~US_LINMR_PARDIS_Msk;
    else
        USART0_REGS->US_LINMR |= US_LINMR_PARDIS_Msk;
}

void ${USART_INSTANCE_NAME}_LIN_ChecksumEnable(bool checksumEnable)
{
    if(checksumEnable == true)
        ${USART_INSTANCE_NAME}_REGS->US_LINMR &= ~US_LINMR_CHKDIS_Msk;
    else
        ${USART_INSTANCE_NAME}_REGS->US_LINMR |= US_LINMR_CHKDIS_Msk;
}

void ${USART_INSTANCE_NAME}_LIN_ChecksumTypeSet(USART_LIN_CHECKSUM_TYPE checksumType)
{
	${USART_INSTANCE_NAME}_REGS->US_LINMR &= ~US_LINMR_CHKTYP_Msk;
	${USART_INSTANCE_NAME}_REGS->US_LINMR |= checksumType;
}

<#if USART_MODE == "LIN_MASTER">
void ${USART_INSTANCE_NAME}_LIN_FrameSlotEnable(bool frameSlotEnable)
{
    if(frameSlotEnable == true)
        ${USART_INSTANCE_NAME}_REGS->US_LINMR &= ~US_LINMR_FSDIS_Msk;
    else
        ${USART_INSTANCE_NAME}_REGS->US_LINMR |= US_LINMR_FSDIS_Msk;
}
</#if>

void ${USART_INSTANCE_NAME}_LIN_DataLenModeSet(USART_LIN_DATA_LEN dataLenMode)
{
    ${USART_INSTANCE_NAME}_REGS->US_LINMR &= ~US_LINMR_DLM_Msk;
    ${USART_INSTANCE_NAME}_REGS->US_LINMR |= dataLenMode;    
}

void ${USART_INSTANCE_NAME}_LIN_ResponseDataLenSet(uint8_t len)
{
    ${USART_INSTANCE_NAME}_REGS->US_LINMR &= ~US_LINMR_DLC_Msk;
    ${USART_INSTANCE_NAME}_REGS->US_LINMR |= US_LINMR_DLC(len-1);
}

uint8_t ${USART_INSTANCE_NAME}_LIN_TransferComplete(void)
{
	return ((USART0_REGS->US_CSR & US_CSR_LIN_LINTC_Msk) > 0);
}

</#if>

