/*******************************************************************************
  UART${INDEX?string} PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_uart${INDEX?string}.c

  Summary:
    UART${INDEX?string} PLIB Implementation File

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

#include "plib_uart${INDEX?string}.h"

<#--Implementation-->
// *****************************************************************************
// *****************************************************************************
// Section: UART${INDEX?string} Implementation
// *****************************************************************************
// *****************************************************************************
<#if INTERRUPT_MODE == true>

UART_OBJECT uart${INDEX?string}Obj;
</#if>

void UART${INDEX?string}_Initialize( void )
{   
    /* Reset UART${INDEX?string} */
    _UART${INDEX?string}_REGS->UART_CR.w = (UART_CR_RSTRX_Msk | UART_CR_RSTTX_Msk | UART_CR_RSTSTA_Msk);
    
    /* Enable UART${INDEX?string} */
    _UART${INDEX?string}_REGS->UART_CR.w = (UART_CR_TXEN_Msk | UART_CR_RXEN_Msk);
    
    /* Configure UART${INDEX?string} mode */
    _UART${INDEX?string}_REGS->UART_MR.w = (UART_MR_PAR_${UART_MR_PAR});
    
    /* Configure UART${INDEX?string} Baud Rate */
    _UART${INDEX?string}_REGS->UART_BRGR.w = UART_BRGR_CD(${BRG_VALUE});
<#if INTERRUPT_MODE == true>

    /* Enable Overrun, Parity and Framing error interrupts */
    _UART${INDEX?string}_REGS->UART_IER.w = (UART_IER_FRAME_Msk | UART_IER_PARE_Msk | UART_IER_OVRE_Msk);
    
    /* Initialize instance object */
    uart${INDEX?string}Obj.rxBuffer = NULL;
    uart${INDEX?string}Obj.rxSize = 0;
    uart${INDEX?string}Obj.rxProcessedSize = 0;
    uart${INDEX?string}Obj.rxStatus = UART_TRANSFER_IDLE;
    uart${INDEX?string}Obj.txBuffer = NULL;
    uart${INDEX?string}Obj.txSize = 0;
    uart${INDEX?string}Obj.txProcessedSize = 0;
    uart${INDEX?string}Obj.txStatus = UART_TRANSFER_IDLE;
    uart${INDEX?string}Obj.callback = NULL;
    uart${INDEX?string}Obj.error = UART_ERROR_NONE;
</#if>

    return;
}

UART_ERROR UART${INDEX?string}_ErrorGet( void )
{
    return (UART_ERROR)(_UART${INDEX?string}_REGS->UART_SR.w & (UART_SR_OVRE_Msk | UART_SR_FRAME_Msk | UART_SR_PARE_Msk));
}

int32_t UART${INDEX?string}_Read( void *buffer, const size_t size )
{
    int32_t processedSize = 0;
    uint8_t * lBuffer = (uint8_t *)buffer;
    
    if(NULL != lBuffer)
    {
<#if INTERRUPT_MODE == false>
        while( size > processedSize )
        {
            if(UART_SR_RXRDY_Msk == (_UART${INDEX?string}_REGS->UART_SR.w & UART_SR_RXRDY_Msk))
            {
                *lBuffer++ = (_UART${INDEX?string}_REGS->UART_RHR.w & UART_RHR_RXCHR_Msk);
                processedSize++;
            }
        }
<#else>
        if(uart${INDEX?string}Obj.rxStatus != UART_TRANSFER_PROCESSING)
        {
            uart${INDEX?string}Obj.rxBuffer = lBuffer;
            uart${INDEX?string}Obj.rxSize = size;
            uart${INDEX?string}Obj.rxProcessedSize = 0;
            uart${INDEX?string}Obj.rxStatus = UART_TRANSFER_PROCESSING;
            
            _UART${INDEX?string}_REGS->UART_IER.w = UART_IER_RXRDY_Msk;
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

int32_t UART${INDEX?string}_Write( void *buffer, const size_t size )
{
    int32_t processedSize = 0;
    uint8_t * lBuffer = (uint8_t *)buffer;
    
    if(NULL != lBuffer)
    {
<#if INTERRUPT_MODE == false>
        while( size > processedSize )
        {
            if(UART_SR_TXEMPTY_Msk == (_UART${INDEX?string}_REGS->UART_SR.w & UART_SR_TXEMPTY_Msk))
            {
                _UART${INDEX?string}_REGS->UART_THR.w = (UART_THR_TXCHR(*lBuffer++) & UART_THR_TXCHR_Msk);
                processedSize++;
            }
        }
<#else>
        if(uart${INDEX?string}Obj.txStatus != UART_TRANSFER_PROCESSING)
        {
            uart${INDEX?string}Obj.txBuffer = lBuffer;
            uart${INDEX?string}Obj.txSize = size;
            uart${INDEX?string}Obj.txProcessedSize = 0;
            uart${INDEX?string}Obj.txStatus = UART_TRANSFER_PROCESSING;
            
            /* Initiate the transfer by sending first byte */
            if(UART_SR_TXEMPTY_Msk == (_UART${INDEX?string}_REGS->UART_SR.w & UART_SR_TXEMPTY_Msk))
            {
                _UART${INDEX?string}_REGS->UART_THR.w = (UART_THR_TXCHR(*lBuffer) & UART_THR_TXCHR_Msk);
                uart${INDEX?string}Obj.txProcessedSize++;
            }
            
            _UART${INDEX?string}_REGS->UART_IER.w = UART_IER_TXEMPTY_Msk;
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
void UART${INDEX?string}_CallbackRegister( UART_CALLBACK callback, uintptr_t context )
{
    uart${INDEX?string}Obj.callback = callback;
    uart${INDEX?string}Obj.context = context;
}

UART_TRANSFER_STATUS UART${INDEX?string}_TransferStatusGet( UART_DIRECTION direction )
{ 
    UART_TRANSFER_STATUS status;
    
    if(UART_DIRECTION_TX == direction)
    {
        status = uart${INDEX?string}Obj.txStatus;
    }
    else
    {
        status = uart${INDEX?string}Obj.rxStatus;
    }
    
    return status;
}

size_t UART${INDEX?string}_TransferCountGet( UART_DIRECTION direction )
{
    size_t count;
    
    if(UART_DIRECTION_TX == direction)
    {
        count = uart${INDEX?string}Obj.txProcessedSize;
    }
    else
    {
        count = uart${INDEX?string}Obj.rxProcessedSize;
    }
    
    return count;
}

</#if>
