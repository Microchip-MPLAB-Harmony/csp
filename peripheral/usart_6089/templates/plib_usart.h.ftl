/*******************************************************************************
  USART${INDEX?string} PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_usart${INDEX?string}.h

  Summary:
    USART${INDEX?string} PLIB Header File

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

#ifndef _PLIB_USART${INDEX?string}_H
#define _PLIB_USART${INDEX?string}_H

#include "plib_usart.h"

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    extern "C" {

#endif
// DOM-IGNORE-END

<#--Interface To Use-->
// *****************************************************************************
// *****************************************************************************
// Section: Interface
// *****************************************************************************
// *****************************************************************************

/****************************** USART${INDEX?string} API *********************************/
void USART${INDEX?string}_Initialize( void );

USART_ERROR USART${INDEX?string}_ErrorGet( void );

int32_t USART${INDEX?string}_Read( void *buffer, const size_t size );

int32_t USART${INDEX?string}_Write( void *buffer, const size_t size );

<#if INTERRUPT_MODE == true>
void USART${INDEX?string}_CallbackRegister( USART_CALLBACK callback, uintptr_t context );

USART_TRANSFER_STATUS USART${INDEX?string}_TransferStatusGet( USART_DIRECTION direction );

size_t USART${INDEX?string}_TransferCountGet( USART_DIRECTION direction );


// *****************************************************************************
// *****************************************************************************
// Section: Local: **** Do Not Use ****
// *****************************************************************************
// *****************************************************************************

/***************************** USART${INDEX?string} Inline *******************************/

extern USART_OBJECT usart${INDEX?string}Obj;

void inline USART${INDEX?string}_ISR_ERR_Handler( void )
{
    uint8_t dummyData = 0u;

    usart${INDEX?string}Obj.error = (_USART${INDEX?string}_REGS->US_CSR.w & (US_CSR_OVRE_Msk | US_CSR_FRAME_Msk | US_CSR_PARE_Msk));
   
    if(usart${INDEX?string}Obj.error != USART_ERROR_NONE)
    {   
         /* Clear all error flags */
        _USART${INDEX?string}_REGS->US_CR.w |= US_CR_RSTSTA_Msk;

        /* Flush existing error bytes from the RX FIFO */
        while( US_CSR_RXRDY_Msk == (_USART${INDEX?string}_REGS->US_CSR.w & US_CSR_RXRDY_Msk) )
        {
            dummyData = (_USART${INDEX?string}_REGS->US_RHR.w & US_RHR_RXCHR_Msk);
        }
        
        /* Ignore the warning */
        (void)dummyData;
        
        usart${INDEX?string}Obj.rxStatus = USART_TRANSFER_ERROR;

        if( usart${INDEX?string}Obj.callback != NULL )
        {            
            usart${INDEX?string}Obj.callback(USART_TRANSFER_ERROR, USART_DIRECTION_RX, usart${INDEX?string}Obj.context);
        }
    }
}

void inline USART${INDEX?string}_ISR_RX_Handler( void )
{
    if(usart${INDEX?string}Obj.rxStatus == USART_TRANSFER_PROCESSING)
    {
        while((US_CSR_RXRDY_Msk == (_USART${INDEX?string}_REGS->US_CSR.w & US_CSR_RXRDY_Msk)) && (usart${INDEX?string}Obj.rxSize > usart${INDEX?string}Obj.rxProcessedSize) )
        {
            usart${INDEX?string}Obj.rxBuffer[usart${INDEX?string}Obj.rxProcessedSize++] = (_USART${INDEX?string}_REGS->US_RHR.w & US_RHR_RXCHR_Msk);
        }

        /* Check if the buffer is done */
        if(usart${INDEX?string}Obj.rxProcessedSize >= usart${INDEX?string}Obj.rxSize)
        {
            usart${INDEX?string}Obj.rxStatus = USART_TRANSFER_COMPLETE;
            usart${INDEX?string}Obj.rxSize = 0;
            usart${INDEX?string}Obj.rxProcessedSize = 0;
            _USART${INDEX?string}_REGS->US_IDR.w |= US_IDR_RXRDY_Msk;

            if(usart${INDEX?string}Obj.callback != NULL)
            {
                usart${INDEX?string}Obj.callback(USART_TRANSFER_COMPLETE, USART_DIRECTION_RX, usart${INDEX?string}Obj.context);
            }
        }
    }
    else
    {
        /* Nothing to process */
        ;
    }
}

void inline USART${INDEX?string}_ISR_TX_Handler( void )
{
    if(usart${INDEX?string}Obj.txStatus == USART_TRANSFER_PROCESSING)
    {
        while((US_CSR_TXEMPTY_Msk == (_USART${INDEX?string}_REGS->US_CSR.w & US_CSR_TXEMPTY_Msk)) && (usart${INDEX?string}Obj.txSize > usart${INDEX?string}Obj.txProcessedSize) )
        {
            _USART${INDEX?string}_REGS->US_THR.w |= usart${INDEX?string}Obj.txBuffer[usart${INDEX?string}Obj.txProcessedSize++];
        }

        /* Check if the buffer is done */
        if(usart${INDEX?string}Obj.txProcessedSize >= usart${INDEX?string}Obj.txSize)
        {
            usart${INDEX?string}Obj.txStatus = USART_TRANSFER_COMPLETE;
            usart${INDEX?string}Obj.txSize = 0;
            usart${INDEX?string}Obj.txProcessedSize = 0;
            _USART${INDEX?string}_REGS->US_IDR.w |= US_IDR_TXEMPTY_Msk;
            
            if(usart${INDEX?string}Obj.callback != NULL)
            {
                usart${INDEX?string}Obj.callback(USART_TRANSFER_COMPLETE, USART_DIRECTION_TX, usart${INDEX?string}Obj.context);
            }
        }
    }
    else
    {
        /* Nothing to process */
        ;
    }    
}
</#if>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END
#endif // _PLIB_USART${INDEX?string}_H
