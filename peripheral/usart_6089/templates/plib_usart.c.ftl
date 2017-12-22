/*******************************************************************************
  USART${INDEX?string} PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_usart${INDEX?string}.c

  Summary:
    USART${INDEX?string} PLIB Implementation File

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

#include "plib_usart${INDEX?string}.h"

<#--Implementation-->
// *****************************************************************************
// *****************************************************************************
// Section: USART${INDEX?string} Implementation
// *****************************************************************************
// *****************************************************************************
<#if INTERRUPT_MODE == true>

USART_OBJECT usart${INDEX?string}Obj;
</#if>

void USART${INDEX?string}_Initialize( void )
{   
    /* Reset USART${INDEX?string} */
    _USART${INDEX?string}_REGS->US_CR.w = (US_CR_RSTRX_Msk | US_CR_RSTTX_Msk | US_CR_RSTSTA_Msk);
    
    /* Enable USART${INDEX?string} */
    _USART${INDEX?string}_REGS->US_CR.w = (US_CR_TXEN_Msk | US_CR_RXEN_Msk);
    
    /* Configure USART${INDEX?string} mode */
    _USART${INDEX?string}_REGS->US_MR.w = ((${USART_MR_MODE9?then(1,0)} << US_MR_MODE9_Pos) | US_MR_CHRL${USART_MR_CHRL} | US_MR_PAR_${USART_MR_PAR} | US_MR_NBSTOP${USART_MR_NBSTOP} | (${USART_MR_SYNC?then(1,0)} << US_MR_SYNC_Pos) | (${USART_MR_OVER?string} << US_MR_OVER_Pos));
    
    /* Configure USART${INDEX?string} Baud Rate */
    _USART${INDEX?string}_REGS->US_BRGR.w = US_BRGR_CD(${BRG_VALUE});
<#if INTERRUPT_MODE == true>

    /* Enable Overrun, Parity and Framing error interrupts */
    _USART${INDEX?string}_REGS->US_IER.w = (US_IER_FRAME_Msk | US_IER_PARE_Msk | US_IER_OVRE_Msk);
    
    /* Initialize instance object */
    usart${INDEX?string}Obj.rxBuffer = NULL;
    usart${INDEX?string}Obj.rxSize = 0;
    usart${INDEX?string}Obj.rxProcessedSize = 0;
    usart${INDEX?string}Obj.rxStatus = USART_TRANSFER_IDLE;
    usart${INDEX?string}Obj.txBuffer = NULL;
    usart${INDEX?string}Obj.txSize = 0;
    usart${INDEX?string}Obj.txProcessedSize = 0;
    usart${INDEX?string}Obj.txStatus = USART_TRANSFER_IDLE;
    usart${INDEX?string}Obj.callback = NULL;
    usart${INDEX?string}Obj.error = USART_ERROR_NONE;
</#if>

    return;
}

USART_ERROR USART${INDEX?string}_ErrorGet( void )
{
    return (USART_ERROR)(_USART${INDEX?string}_REGS->US_CSR.w & (US_CSR_OVRE_Msk | US_CSR_FRAME_Msk | US_CSR_PARE_Msk));
}

int32_t USART${INDEX?string}_Read( void *buffer, const size_t size )
{
    int32_t processedSize = 0;
    uint8_t * lBuffer = (uint8_t *)buffer;
    
    if(NULL != lBuffer)
    {
<#if INTERRUPT_MODE == false>
        while( size > processedSize )
        {
            if(US_CSR_RXRDY_Msk == (_USART${INDEX?string}_REGS->US_CSR.w & US_CSR_RXRDY_Msk))
            {
                *lBuffer++ = (_USART${INDEX?string}_REGS->US_RHR.w & US_RHR_RXCHR_Msk);
                processedSize++;
            }
        }
<#else>
        if(usart${INDEX?string}Obj.rxStatus != USART_TRANSFER_PROCESSING)
        {
            usart${INDEX?string}Obj.rxBuffer = lBuffer;
            usart${INDEX?string}Obj.rxSize = size;
            usart${INDEX?string}Obj.rxProcessedSize = 0;
            usart${INDEX?string}Obj.rxStatus = USART_TRANSFER_PROCESSING;
            
            _USART${INDEX?string}_REGS->US_IER.w = US_IER_RXRDY_Msk;
        }
        else
        {
            processedSize = -1;
        }
</#if>
    }
    else
    {
        processedSize = -1;
    }

    return processedSize;
}

int32_t USART${INDEX?string}_Write( void *buffer, const size_t size )
{
    int32_t processedSize = 0;
    uint8_t * lBuffer = (uint8_t *)buffer;
    
    if(NULL != lBuffer)
    {
<#if INTERRUPT_MODE == false>
        while( size > processedSize )
        {
            if(US_CSR_TXEMPTY_Msk == (_USART${INDEX?string}_REGS->US_CSR.w & US_CSR_TXEMPTY_Msk))
            {
                _USART${INDEX?string}_REGS->US_THR.w = (US_THR_TXCHR(*lBuffer++) & US_THR_TXCHR_Msk);
                processedSize++;
            }
        }
<#else>
        if(usart${INDEX?string}Obj.txStatus != USART_TRANSFER_PROCESSING)
        {
            usart${INDEX?string}Obj.txBuffer = lBuffer;
            usart${INDEX?string}Obj.txSize = size;
            usart${INDEX?string}Obj.txProcessedSize = 0;
            usart${INDEX?string}Obj.txStatus = USART_TRANSFER_PROCESSING;
            
            /* Initiate the transfer by sending first byte */
            if(US_CSR_TXEMPTY_Msk == (_USART${INDEX?string}_REGS->US_CSR.w & US_CSR_TXEMPTY_Msk))
            {
                _USART${INDEX?string}_REGS->US_THR.w = (US_THR_TXCHR(*lBuffer) & US_THR_TXCHR_Msk);
                usart${INDEX?string}Obj.txProcessedSize++;
            }
            
            _USART${INDEX?string}_REGS->US_IER.w = US_IER_TXEMPTY_Msk;
        }
        else
        {
            processedSize = -1;
        }
</#if>
    }
    else
    {
        processedSize = -1;
    }

    return processedSize;
}

<#if INTERRUPT_MODE == true>
void USART${INDEX?string}_CallbackRegister( USART_CALLBACK callback, uintptr_t context )
{
    usart${INDEX?string}Obj.callback = callback;
    usart${INDEX?string}Obj.context = context;
}

USART_TRANSFER_STATUS USART${INDEX?string}_TransferStatusGet( USART_DIRECTION direction )
{ 
    USART_TRANSFER_STATUS status;
    
    if(USART_DIRECTION_TX == direction)
    {
        status = usart${INDEX?string}Obj.txStatus;
    }
    else
    {
        status = usart${INDEX?string}Obj.rxStatus;
    }
    
    return status;
}

size_t USART${INDEX?string}_TransferCountGet( USART_DIRECTION direction )
{
    size_t count;
    
    if(USART_DIRECTION_TX == direction)
    {
        count = usart${INDEX?string}Obj.txProcessedSize;
    }
    else
    {
        count = usart${INDEX?string}Obj.rxProcessedSize;
    }
    
    return count;
}

</#if>
