/*******************************************************************************
  SPI PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_spi${SPI_INDEX?string}.c

  Summary:
    SPI${SPI_INDEX?string} Source File

  Description:
    This file has implementation of all the interfaces provided for particular
    SPI peripheral.

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
#include "${__PROCESSOR}.h"

// *****************************************************************************
// *****************************************************************************
// Section: SPI${SPI_INDEX?string} Implementation
// *****************************************************************************
// *****************************************************************************
<#if SPI_INTERRUPT_MODE == true>
/* Global object to save SPI Exchange related data */
SPI_OBJECT spi${SPI_INDEX?string}Obj;
</#if>

void SPI${SPI_INDEX?string}_Initialize ( void )
{
    /* Disable and Reset the SPI*/
    _SPI${SPI_INDEX?string}_REGS->SPI_CR.w = SPI_CR_SPIDIS_Msk | SPI_CR_SWRST_Msk;

<#if SPI_MR_MSTR=="_MASTER">   
    /* Enable Master mode, select particular NPCS line for chip select and disable mode fault detection */
    _SPI${SPI_INDEX?string}_REGS->SPI_MR.w =  SPI_MR_MSTR_Msk | SPI_MR_PCS${SPI_MR_PCS} | SPI_MR_MODFDIS_Msk;    
<#else>
    /* SPI is by default in Slave Mode, but disable mode fault detection */
    _SPI${SPI_INDEX?string}_REGS->SPI_MR.w =  SPI_MR_MODFDIS_Msk;
</#if>
    
    /* Set up clock Polarity, data phase, Communication Width and Baud Rate */
<#if SPI_MR_PCS == "_NPCS0" | SPI_MR_PCS == "_NONE" >
    _SPI${SPI_INDEX?string}_REGS->SPI_CSR[0].w = SPI_CSR_CPOL${SPI_CSR_CPOL} | SPI_CSR_NCPHA${SPI_CSR_NCPHA} | SPI_CSR_BITS${SPI_CSR_BITS} | SPI_CSR_SCBR(${SPI_CSR_SCBR_VALUE});
<#elseif SPI_MR_PCS == "_NPCS1">
    _SPI${SPI_INDEX?string}_REGS->SPI_CSR[1].w = SPI_CSR_CPOL${SPI_CSR_CPOL} | SPI_CSR_NCPHA${SPI_CSR_NCPHA} | SPI_CSR_BITS${SPI_CSR_BITS} | SPI_CSR_SCBR(${SPI_CSR_SCBR_VALUE});
<#elseif SPI_MR_PCS == "_NPCS2" >
    _SPI${SPI_INDEX?string}_REGS->SPI_CSR[2].w = SPI_CSR_CPOL${SPI_CSR_CPOL} | SPI_CSR_NCPHA${SPI_CSR_NCPHA} | SPI_CSR_BITS${SPI_CSR_BITS} | SPI_CSR_SCBR(${SPI_CSR_SCBR_VALUE});
<#elseif SPI_MR_PCS == "_NPCS3">
    _SPI${SPI_INDEX?string}_REGS->SPI_CSR[3].w = SPI_CSR_CPOL${SPI_CSR_CPOL} | SPI_CSR_NCPHA${SPI_CSR_NCPHA} | SPI_CSR_BITS${SPI_CSR_BITS} | SPI_CSR_SCBR(${SPI_CSR_SCBR_VALUE});
</#if>        
        
<#if SPI_INTERRUPT_MODE == true>
    /* Initialize global variables */
    spi${SPI_INDEX?string}Obj.exchangeIsBusy = false;
    spi${SPI_INDEX?string}Obj.callback = NULL;
</#if>

    /* Enable SPI${SPI_INDEX?string} */
    _SPI${SPI_INDEX?string}_REGS->SPI_CR.w = SPI_CR_SPIEN_Msk;
    return;
}

bool SPI${SPI_INDEX?string}_Exchange (void* pTransmitData, void* pReceiveData, size_t wordSize)
{
    bool requestAccepted = false;
    
    /* Validate the argument */
    if(((NULL != pTransmitData) || (NULL != pReceiveData )) && (0 != wordSize))
    {
<#if SPI_INTERRUPT_MODE == false>   
    <#if SPI_CSR_BITS == "_8_BIT">
        uint8_t* pTransmitDataLocal = (uint8_t*)pTransmitData;
        uint8_t* pReceiveDataLocal = (uint8_t*)pReceiveData;
    <#else>
        uint16_t* pTransmitDataLocal = (uint16_t*)pTransmitData;
        uint16_t* pReceiveDataLocal = (uint16_t*)pReceiveData;
    </#if>
        uint32_t dataExchangedCount = 0; 
        
        while (dataExchangedCount < wordSize)
        {
            if (NULL == pTransmitDataLocal )
            {
                // do a dummy write
                _SPI${SPI_INDEX?string}_REGS->SPI_TDR.TD = 0xFF;
            }
            else
            {   
                _SPI${SPI_INDEX?string}_REGS->SPI_TDR.TD = pTransmitDataLocal[dataExchangedCount];
            }
            
            /* Wait until data is received */
            while( false == _SPI${SPI_INDEX?string}_REGS->SPI_SR.RDRF );
            
            if (NULL == pReceiveDataLocal )
            {
                // dummy read
                _SPI${SPI_INDEX?string}_REGS->SPI_RDR.RD;
            }
            else
            {
              pReceiveDataLocal[dataExchangedCount] = _SPI${SPI_INDEX?string}_REGS->SPI_RDR.RD;
            }
            dataExchangedCount++;            
        }
        requestAccepted = true;
<#else>
        if (spi${SPI_INDEX?string}Obj.exchangeIsBusy == false)
        {
            requestAccepted = true;
            spi${SPI_INDEX?string}Obj.txBuffer = pTransmitData;
            spi${SPI_INDEX?string}Obj.rxBuffer = pReceiveData;
            spi${SPI_INDEX?string}Obj.exchangeSize = wordSize;
            spi${SPI_INDEX?string}Obj.rxCount = 0;
            spi${SPI_INDEX?string}Obj.txCount = 0;
            spi${SPI_INDEX?string}Obj.exchangeIsBusy = true;
            
    <#if SPI_CSR_BITS == "_8_BIT">        
            /* Start the first write here itself, rest will happen in ISR context */
            if (NULL == spi${SPI_INDEX?string}Obj.txBuffer )
            {   
                // Do a dummy write
                _SPI${SPI_INDEX?string}_REGS->SPI_TDR.TD = 0xFF;
            }
            else
            {
                _SPI${SPI_INDEX?string}_REGS->SPI_TDR.TD = *((uint8_t*)spi${SPI_INDEX?string}Obj.txBuffer);            
            }
    <#else>
            /* Start the first write here itself, rest will happen in ISR context */
            if (NULL == spi${SPI_INDEX?string}Obj.txBuffer )
            {   
                // Do a dummy write
                _SPI${SPI_INDEX?string}_REGS->SPI_TDR.TD = 0xFFFF;
            }
            else
            {
                _SPI${SPI_INDEX?string}_REGS->SPI_TDR.TD = *((uint16_t*)spi${SPI_INDEX?string}Obj.txBuffer);            
            }
    </#if>
            spi${SPI_INDEX?string}Obj.txCount++;
            
            /* Enable transmit interrupt to complete the exchange in ISR context */
            _SPI${SPI_INDEX?string}_REGS->SPI_IER.w = SPI_IER_TDRE_Msk;
        }
</#if>
    }
    return requestAccepted;
}

SPI_ERROR SPI${SPI_INDEX?string}_ErrorGet ( void )
{
    return (SPI_ERROR)(_SPI${SPI_INDEX?string}_REGS->SPI_SR.w & (SPI_SR_OVRES_Msk));
}

void SPI${SPI_INDEX?string}_Setup ( SPI_SETUP * spiSetup )
{
    // TBD: will be implemented while doing SPI driver development.
    return;
}

<#if SPI_INTERRUPT_MODE == true>
void SPI${SPI_INDEX?string}_CallbackRegister (SPI_EVENT_HANDLER eventHandler, void* context)
{
    spi${SPI_INDEX?string}Obj.callback = eventHandler;
    spi${SPI_INDEX?string}Obj.context = context;
}


bool SPI${SPI_INDEX?string}_ExchangeIsBusy()
{  
    return spi${SPI_INDEX?string}Obj.exchangeIsBusy;
}

void SPI${SPI_INDEX?string}_InterruptHandler(void)
{
    <#if SPI_CSR_BITS == "_8_BIT">
        <#lt>    uint8_t* pTransmitDataLocal = (uint8_t*)spi${SPI_INDEX?string}Obj.txBuffer;
        <#lt>    uint8_t* pReceiveDataLocal = (uint8_t*)spi${SPI_INDEX?string}Obj.rxBuffer;
    <#else>
        <#lt>    uint16_t* pTransmitDataLocal = (uint16_t*)spi${SPI_INDEX?string}Obj.txBuffer;
        <#lt>    uint16_t* pReceiveDataLocal = (uint16_t*)spi${SPI_INDEX?string}Obj.rxBuffer;
    </#if>
    
    /* Since the write cycle had started in Exchange API itself, start with read cycle here */
    if ( true == _SPI${SPI_INDEX?string}_REGS->SPI_SR.RDRF )
    {
        if (NULL == pReceiveDataLocal)
        {
            // Dummy Read
            _SPI${SPI_INDEX?string}_REGS->SPI_RDR.RD;
        }
        else
        { 
            pReceiveDataLocal[spi${SPI_INDEX?string}Obj.rxCount] = _SPI${SPI_INDEX?string}_REGS->SPI_RDR.RD;
        }
        spi${SPI_INDEX?string}Obj.rxCount++;
    } 
   
    /* If there are more words to be transmitted, then transmit them here and keep track of the count */
    if((spi${SPI_INDEX?string}Obj.txCount < spi${SPI_INDEX?string}Obj.exchangeSize) && (true == _SPI${SPI_INDEX?string}_REGS->SPI_SR.TDRE))
    {   
        if (NULL == pTransmitDataLocal )
        {   
            // do a dummy write
            _SPI${SPI_INDEX?string}_REGS->SPI_TDR.TD = 0xFFFF;
        }
        else
        {
            _SPI${SPI_INDEX?string}_REGS->SPI_TDR.TD = pTransmitDataLocal[spi${SPI_INDEX?string}Obj.txCount];            
        }
        spi${SPI_INDEX?string}Obj.txCount++;
        if(spi${SPI_INDEX?string}Obj.txCount == spi${SPI_INDEX?string}Obj.exchangeSize)
        {
            /* There is nothing more to be transmitted, but there are couple
            of words yet to be received, so disable TX interrupt and enable
            RX interrupt for optimum calls to ISR */
            //Disable TX interrupt           
            _SPI${SPI_INDEX?string}_REGS->SPI_IDR.w |= SPI_IDR_TDRE_Msk;
            //Enable RX interrupt
            _SPI${SPI_INDEX?string}_REGS->SPI_IER.w |= SPI_IER_RDRF_Msk;        
        }
    }
    
    /* See if Exchange is complete */
    if (spi${SPI_INDEX?string}Obj.rxCount == spi${SPI_INDEX?string}Obj.exchangeSize)
    {
        spi${SPI_INDEX?string}Obj.exchangeIsBusy = false;

        //Disable TX and RX interrupts
        // if it was one word transfer, then RX interrupt should already be disabled, disable both anyways.
        // if it was more than a word transfer, then TX interrupt should already be disabled, disable both anyways.
        _SPI${SPI_INDEX?string}_REGS->SPI_IDR.w |= SPI_IER_TDRE_Msk | SPI_IER_RDRF_Msk;
        
        /* This means the buffer is completed. If there
           is a callback registered with client, then
           call it */
        if(spi${SPI_INDEX?string}Obj.callback != NULL)
        {
            spi${SPI_INDEX?string}Obj.callback(spi${SPI_INDEX?string}Obj.context);
        }             
    } 
}
</#if>


/*******************************************************************************
 End of File
*/

