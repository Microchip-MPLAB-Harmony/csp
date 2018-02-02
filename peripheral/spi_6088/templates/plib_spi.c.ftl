/*******************************************************************************
  SPI Primitive

  Company:
    Microchip Technology Inc.

  File Name:
    plib_spi.c

  Summary:
    SPI Primitive Source File

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

#include "plib_spi${SPI_INDEX?string}.h"


// *****************************************************************************
// *****************************************************************************
// Section: SPI${SPI_INDEX?string} Implementation
// *****************************************************************************
// *****************************************************************************
<#if SPI_INTERRUPT_MODE == true>

SPI_OBJECT spi${SPI_INDEX?string}Obj;
</#if>

void SPI${SPI_INDEX?string}_Initialize ( void )
{   
    uint32_t dummy;

    /* Disable and Reset the SPI*/
    _SPI${SPI_INDEX?string}_REGS->SPI_CR.w = SPI_CR_SPIDIS_Msk | SPI_CR_SWRST_Msk;

    
<#if SPI_MR_MSTR=="Master">   
    /* Fixed Peripheral Select */
    _SPI${SPI_INDEX?string}_REGS->SPI_MR.w &= ~SPI_MR_PS_Msk;
    /* No Decoder used for chip select */
    _SPI${SPI_INDEX?string}_REGS->SPI_MR.w &= ~SPI_MR_PCSDEC_Msk;
    /* Fixed NPCS0 line for chip select */
    _SPI${SPI_INDEX?string}_REGS->SPI_MR.w = ( (_SPI${SPI_INDEX?string}_REGS->SPI_MR.w & (~SPI_MR_PCS_Msk)) | SPI_MR_PCS(0x0E) );
    
    /* Enable Master mode */
    _SPI${SPI_INDEX?string}_REGS->SPI_MR.w |= SPI_MR_MSTR_Msk;
</#if>
<#if SPI_MR_MSTR=="Slave">
    /* Enable Slave mode */
    _SPI${SPI_INDEX?string}_REGS->SPI_MR.w &= ~SPI_MR_MSTR_Msk;
</#if>

     /* Disable Mode Fault Detection. */
    _SPI${SPI_INDEX?string}_REGS->SPI_MR.w |= SPI_MR_MODFDIS_Msk;
    
    /* Using Chip select line NPCS0, hence CSR[0] register for clock configuration for now */
    /* Set up clock Polarity, data phase, Communication Width and Baud Rate */
    _SPI${SPI_INDEX?string}_REGS->SPI_CSR[0].w = ((${SPI_CSR_CPOL_VALUE} << SPI_CSR_CPOL_Pos) | (${SPI_CSR_NCPHA_VALUE} << SPI_CSR_NCPHA_Pos) | SPI_CSR_BITS${SPI_CSR_BITS} | SPI_CSR_SCBR(${SPI_CSR_SCBR_VALUE}));


    /* Flush the RX buffer */
    dummy = _SPI${SPI_INDEX?string}_REGS->SPI_RDR.RD;
    (void)dummy;
        
<#if SPI_INTERRUPT_MODE == true>

    /* Enable Transmit and Receive Interrupts */
    _SPI${SPI_INDEX?string}_REGS->SPI_IER.w = 0x03;
    
    spi${SPI_INDEX?string}Obj.txBuffer = NULL;
    spi${SPI_INDEX?string}Obj.rxBuffer = NULL;
    spi${SPI_INDEX?string}Obj.exchangeSize = 0;
    spi${SPI_INDEX?string}Obj.exchangedCount = 0;
    spi${SPI_INDEX?string}Obj.exchangeStatus = SPI_EXCHANGE_SUCCESS;
    spi${SPI_INDEX?string}Obj.dataInProgress = false;
    
    spi${SPI_INDEX?string}Obj.callback = NULL;
    spi${SPI_INDEX?string}Obj.error = SPI_ERROR_NONE;
</#if>

    return;
}

void SPI${SPI_INDEX?string}_ConfigSet ( SPI_CONFIG * config )
{
    return;
}

SPI_ERROR SPI${SPI_INDEX?string}_ErrorGet ( void )
{
    return (SPI_ERROR)(_SPI${SPI_INDEX?string}_REGS->SPI_SR.w & (SPI_SR_OVRES_Msk | SPI_SR_MODF_Msk | SPI_SR_UNDES_Msk));
}

bool SPI${SPI_INDEX?string}_Exchange (void* pTransmitData, void* pReceiveData, size_t wordCount)
{
    bool requestAccepted = false;
    /* Validate the argument */
    if((NULL != pTransmitData) || (NULL != pReceiveData ))
    {
    
<#if SPI_INTERRUPT_MODE == false>
        uint32_t dataExchangedCount = 0;
        bool dataInProgress = false;
        
        /* Enable SPI${SPI_INDEX?string} */
        _SPI${SPI_INDEX?string}_REGS->SPI_CR.w = SPI_CR_SPIEN_Msk;
        while (dataExchangedCount < wordCount)
        {
            if ((false == dataInProgress) && (true  == _SPI${SPI_INDEX?string}_REGS->SPI_SR.TDRE ))
            {
                if (NULL == pTransmitData )
                {
                    // do a dummy write
                    _SPI${SPI_INDEX?string}_REGS->SPI_TDR.TD = 0xFF;
                }
                else
                {
                    _SPI${SPI_INDEX?string}_REGS->SPI_TDR.TD = *((uint8_t*)pTransmitData);
                    pTransmitData += 1;
                }
                dataInProgress = true;
            }
            if ( true == _SPI${SPI_INDEX?string}_REGS->SPI_SR.RDRF )
            {
                if (NULL == pReceiveData )
                {
                    // dummy read
                    _SPI${SPI_INDEX?string}_REGS->SPI_RDR.RD;
                }
                else
                {
                    *((uint8_t*)pReceiveData) = _SPI${SPI_INDEX?string}_REGS->SPI_RDR.RD;
                    pReceiveData += 1;
                }
                dataInProgress = false;
                dataExchangedCount++;
            }
        }
        requestAccepted = true;
<#else>
        if (spi${SPI_INDEX?string}Obj.exchangeStatus != SPI_EXCHANGE_BUSY)
        {
            requestAccepted = true;
            spi${SPI_INDEX?string}Obj.txBuffer = pTransmitData;
            spi${SPI_INDEX?string}Obj.rxBuffer = pReceiveData;
            spi${SPI_INDEX?string}Obj.exchangeSize = wordCount;
            spi${SPI_INDEX?string}Obj.exchangedCount = 0;
            spi${SPI_INDEX?string}Obj.exchangeStatus = SPI_EXCHANGE_BUSY;
            
            _SPI${SPI_INDEX?string}_REGS->SPI_IER.w |= SPI_IER_TDRE_Msk;
        }
</#if>
    }

    return requestAccepted;
}



<#if SPI_INTERRUPT_MODE == true>
void SPI${SPI_INDEX?string}_CallbackRegister (SPI_EVENT_HANDLER eventHandler, void* context)
{
    spi${SPI_INDEX?string}Obj.callback = eventHandler;
    spi${SPI_INDEX?string}Obj.context = context;
}


SPI_EXCHANGE_STATUS SPI${SPI_INDEX?string}_ExchangeStatusGet()
{  
    return spi${SPI_INDEX?string}Obj.exchangeStatus;
}

size_t SPI${SPI_INDEX?string}_ExchangeCountGet()
{
    return spi${SPI_INDEX?string}Obj.exchangedCount;
}
</#if>


/*******************************************************************************
 End of File
*/

