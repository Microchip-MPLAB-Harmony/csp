/*******************************************************************************
  SPI Plib

  Company:
    Microchip Technology Inc.

  File Name:
    plib_spi.h

  Summary:
    SPI Plib Header File

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

#ifndef PLIB_SPI${SPI_INDEX?string}_H
#define PLIB_SPI${SPI_INDEX?string}_H

#include "plib_spi.h"

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    extern "C" {

#endif
// DOM-IGNORE-END


/****************************** SPI${SPI_INDEX?string} API *********************************/
void SPI${SPI_INDEX?string}_Initialize ( void );

void SPI${SPI_INDEX?string}_ConfigSet ( SPI_CONFIG * spiConfig );

SPI_ERROR SPI${SPI_INDEX?string}_ErrorGet ( void );

bool SPI${SPI_INDEX?string}_Exchange(void* pTransmitData,void* pReceiveData, size_t wordCount);

 <#if SPI_INTERRUPT_MODE == true>     
SPI_EXCHANGE_STATUS SPI${SPI_INDEX?string}_ExchangeStatusGet (void);

size_t SPI${SPI_INDEX?string}_ExchangeCountGet (void);

void SPI${SPI_INDEX?string}_CallbackRegister(const SPI_EVENT_HANDLER eventHandler, void* context);



/***************************** SPI${SPI_INDEX?string} Inline *******************************/

extern SPI_OBJECT spi${SPI_INDEX?string}Obj;

void inline SPI${SPI_INDEX?string}_ISR_Error_Handler(void)
{        
    /* Read the error if any, error flag will be cleared by reading it */
    spi${SPI_INDEX?string}Obj.error = (_SPI${SPI_INDEX?string}_REGS->SPI_SR.w & (SPI_SR_OVRES_Msk | SPI_SR_MODF_Msk | SPI_SR_UNDES_Msk));
   
    if(spi${SPI_INDEX?string}Obj.error != SPI_ERROR_NONE)
    {            
        spi${SPI_INDEX?string}Obj.exchangeStatus = SPI_EXCHANGE_ERROR;
    
        /* Callback operations */
        if( spi${SPI_INDEX?string}Obj.callback != NULL )
        {            
            spi${SPI_INDEX?string}Obj.callback(SPI_EXCHANGE_ERROR, spi${SPI_INDEX?string}Obj.context);
        }
    }
}

void inline SPI${SPI_INDEX?string}_ISR_Exchange_Handler(void)
{
    if(spi${SPI_INDEX?string}Obj.exchangeStatus == SPI_EXCHANGE_BUSY)
    {
        if(spi${SPI_INDEX?string}Obj.exchangedCount < spi${SPI_INDEX?string}Obj.exchangeSize)
        {
            if ((false == spi${SPI_INDEX?string}Obj.dataInProgress) && (true  == _SPI${SPI_INDEX?string}_REGS->SPI_SR.TDRE ))
            {
                if (NULL == spi${SPI_INDEX?string}Obj.txBuffer )
                {   
                    // do a dummy write
                    _SPI${SPI_INDEX?string}_REGS->SPI_TDR.TD = 0xFF;
                }
                else
                {
                    _SPI${SPI_INDEX?string}_REGS->SPI_TDR.TD = *((uint8_t*)spi${SPI_INDEX?string}Obj.txBuffer);
                    spi${SPI_INDEX?string}Obj.txBuffer += 1;
                }
                spi${SPI_INDEX?string}Obj.dataInProgress = true;
            }
            if ( true == _SPI${SPI_INDEX?string}_REGS->SPI_SR.RDRF )
            {
                if (NULL == spi${SPI_INDEX?string}Obj.rxBuffer )
                {
                    // Dummy Read
                    _SPI${SPI_INDEX?string}_REGS->SPI_RDR.RD;
                }
                else
                { 
                    *((uint8_t*)spi${SPI_INDEX?string}Obj.rxBuffer) = _SPI${SPI_INDEX?string}_REGS->SPI_RDR.RD;
                    spi${SPI_INDEX?string}Obj.rxBuffer += 1;
                }
                spi${SPI_INDEX?string}Obj.dataInProgress = false;
                spi${SPI_INDEX?string}Obj.exchangedCount++;
            }
        }  
        else if(spi${SPI_INDEX?string}Obj.exchangedCount == spi${SPI_INDEX?string}Obj.exchangeSize)
        {
            spi${SPI_INDEX?string}Obj.exchangeStatus = SPI_EXCHANGE_SUCCESS;
            spi${SPI_INDEX?string}Obj.exchangeSize = 0;
            spi${SPI_INDEX?string}Obj.exchangedCount = 0;
            _SPI${SPI_INDEX?string}_REGS->SPI_IDR.w |= SPI_IDR_TDRE_Msk;
            
            /* This means the buffer is completed. If there
               is a callback registered with client, then
               call it */
            if(spi${SPI_INDEX?string}Obj.callback != NULL)
            {
                spi${SPI_INDEX?string}Obj.callback(SPI_EXCHANGE_SUCCESS, spi${SPI_INDEX?string}Obj.context);
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
#endif // PLIB_SPI${SPI_INDEX?string}_H

/*******************************************************************************
 End of File
*/