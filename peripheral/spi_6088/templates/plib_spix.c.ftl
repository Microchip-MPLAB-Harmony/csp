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

<#if SPI_MR_MSTR=="MASTER">   
    /* Enable Master mode, variable peripheral select and disable mode fault detection */
    _SPI${SPI_INDEX?string}_REGS->SPI_MR.w =  SPI_MR_MSTR_Msk | SPI_MR_PS_Msk | SPI_MR_MODFDIS_Msk;    
<#else>
    /* SPI is by default in Slave Mode, disable mode fault detection */
    _SPI${SPI_INDEX?string}_REGS->SPI_MR.w =  SPI_MR_MODFDIS_Msk;
</#if>
    
    /* Set up clock Polarity, data phase, Communication Width and Baud Rate for different Chip Selects */
<#if SPI_CHIP_SELECT0 == true >
    _SPI${SPI_INDEX?string}_REGS->SPI_CSR[0].w = SPI_CSR_CPOL_${SPI_CSR_CPOL0} | SPI_CSR_NCPHA_${SPI_CSR_NCPHA0} | SPI_CSR_BITS${SPI_CSR_BITS0} | SPI_CSR_SCBR(${SPI_CSR_SCBR_VALUE0});
</#if> 
<#if SPI_CHIP_SELECT1 == true >
    _SPI${SPI_INDEX?string}_REGS->SPI_CSR[1].w = SPI_CSR_CPOL_${SPI_CSR_CPOL1} | SPI_CSR_NCPHA_${SPI_CSR_NCPHA1} | SPI_CSR_BITS${SPI_CSR_BITS1} | SPI_CSR_SCBR(${SPI_CSR_SCBR_VALUE1});
</#if> 
<#if SPI_CHIP_SELECT2 == true >
    _SPI${SPI_INDEX?string}_REGS->SPI_CSR[2].w = SPI_CSR_CPOL_${SPI_CSR_CPOL2} | SPI_CSR_NCPHA_${SPI_CSR_NCPHA2} | SPI_CSR_BITS${SPI_CSR_BITS2} | SPI_CSR_SCBR(${SPI_CSR_SCBR_VALUE2});
</#if> 
<#if SPI_CHIP_SELECT3 == true >
    _SPI${SPI_INDEX?string}_REGS->SPI_CSR[3].w = SPI_CSR_CPOL_${SPI_CSR_CPOL3} | SPI_CSR_NCPHA_${SPI_CSR_NCPHA3} | SPI_CSR_BITS${SPI_CSR_BITS3} | SPI_CSR_SCBR(${SPI_CSR_SCBR_VALUE3});
</#if>        
        
<#if SPI_INTERRUPT_MODE == true >
    /* Initialize global variables */
    spi${SPI_INDEX?string}Obj.exchangeIsBusy = false;
    spi${SPI_INDEX?string}Obj.callback = NULL;
</#if>

    /* Enable SPI${SPI_INDEX?string} */
    _SPI${SPI_INDEX?string}_REGS->SPI_CR.w = SPI_CR_SPIEN_Msk;
    return;
}

bool SPI${SPI_INDEX?string}_Exchange (void* pTransmitData, void* pReceiveData, size_t size, SPI_CHIP_SELECT chipSelect)
{
    bool requestAccepted = false;

<#if SPI_INTERRUPT_MODE == false >
    uint32_t dataExchangedCount = 0; 
    uint32_t wordSize;
        
    /* Validate the argument */
    if(0 != size)
    {
        if(SPI_CSR_BITS_8_BIT == (_SPI${SPI_INDEX?string}_REGS->SPI_CSR[chipSelect & 0xFF].w & SPI_CSR_BITS_Msk))
        {
            wordSize = size;
        }
        else
        {
            wordSize = size >> 1;
        }     
        while(dataExchangedCount < wordSize)
        {
            if (NULL == pTransmitData )
            {
                // do a dummy write
                _SPI${SPI_INDEX?string}_REGS->SPI_TDR.w = 0xFFFF | (chipSelect & 0x000F0000);
            }
            else if(SPI_CSR_BITS_8_BIT == (_SPI${SPI_INDEX?string}_REGS->SPI_CSR[chipSelect & 0xFF].w & SPI_CSR_BITS_Msk))
            {
                _SPI${SPI_INDEX?string}_REGS->SPI_TDR.w = ((uint8_t*)pTransmitData)[dataExchangedCount] | (chipSelect & 0x000F0000);
            }
            else
            {
                _SPI${SPI_INDEX?string}_REGS->SPI_TDR.w = ((uint16_t*)pTransmitData)[dataExchangedCount] | (chipSelect & 0x000F0000);
            }
            
            /* Wait until data is received */
            while( false == _SPI${SPI_INDEX?string}_REGS->SPI_SR.RDRF );
            
            if (NULL == pReceiveData )
            {
                // dummy read
                _SPI${SPI_INDEX?string}_REGS->SPI_RDR.RD;
            }
            else if(SPI_CSR_BITS_8_BIT == (_SPI${SPI_INDEX?string}_REGS->SPI_CSR[chipSelect & 0xFF].w & SPI_CSR_BITS_Msk))
            {
                ((uint8_t*)pReceiveData)[dataExchangedCount] = _SPI${SPI_INDEX?string}_REGS->SPI_RDR.RD;
            }
            else
            {
                ((uint16_t*)pReceiveData)[dataExchangedCount] = _SPI${SPI_INDEX?string}_REGS->SPI_RDR.RD;
            }          
            dataExchangedCount++;            
        }
        requestAccepted = true;
    }
<#else>
    /* Validate the argument */
    if((0 != size) && (false == spi${SPI_INDEX?string}Obj.exchangeIsBusy))
    {
        requestAccepted = true;
        spi${SPI_INDEX?string}Obj.txBuffer = pTransmitData;
        spi${SPI_INDEX?string}Obj.rxBuffer = pReceiveData;
        spi${SPI_INDEX?string}Obj.chipSelect = chipSelect;
        spi${SPI_INDEX?string}Obj.rxCount = 0;
        spi${SPI_INDEX?string}Obj.txCount = 0;
        spi${SPI_INDEX?string}Obj.exchangeIsBusy = true;
              
        /* Start the first write here itself, rest will happen in ISR context */
        if (NULL == spi${SPI_INDEX?string}Obj.txBuffer )
        {   
            // Do a dummy write
            _SPI${SPI_INDEX?string}_REGS->SPI_TDR.w = 0xFFFF | (chipSelect & 0x000F0000);
        }
        else if(SPI_CSR_BITS_8_BIT == (_SPI${SPI_INDEX?string}_REGS->SPI_CSR[chipSelect & 0xFF].w & SPI_CSR_BITS_Msk))
        {
            _SPI${SPI_INDEX?string}_REGS->SPI_TDR.w = *((uint8_t*)spi${SPI_INDEX?string}Obj.txBuffer) | (chipSelect & 0x000F0000);
            spi${SPI_INDEX?string}Obj.exchangeSize = size;
        }
        else
        {
            _SPI${SPI_INDEX?string}_REGS->SPI_TDR.w = *((uint16_t*)spi${SPI_INDEX?string}Obj.txBuffer) | (chipSelect & 0x000F0000);
            spi${SPI_INDEX?string}Obj.exchangeSize = size >> 1;
        }
        spi${SPI_INDEX?string}Obj.txCount++;
        
        /* Enable transmit interrupt to complete the exchange in ISR context */
        _SPI${SPI_INDEX?string}_REGS->SPI_IER.w = SPI_IER_TDRE_Msk;
    }
</#if>
    return requestAccepted;
}

SPI_ERROR SPI${SPI_INDEX?string}_ErrorGet ( void )
{
    return (SPI_ERROR)(_SPI${SPI_INDEX?string}_REGS->SPI_SR.w & (SPI_SR_OVRES_Msk));
}

bool SPI${SPI_INDEX?string}_SlaveSetup ( uint32_t spiSourceClock, SPI_SLAVE_SETUP * setup )
{
    uint32_t scbr;
    if(0 == spiSourceClock)
    {
        // Fetch Master Clock Frequency directly
        spiSourceClock = ${SPI_MASTER_CLOCK};
    }
    scbr = spiSourceClock/ setup->clockFrequency;
    if ((0 == scbr) || (scbr > 255)) 
    {
        return false;
    }
    _SPI${SPI_INDEX?string}_REGS->SPI_CSR[setup->chipSelect & 0xFF].w = setup->clockPolarity | setup->clockPhase | SPI_CSR_BITS(setup->dataBits) | SPI_CSR_SCBR(scbr);
    return true;
}

<#if SPI_INTERRUPT_MODE == true >
void SPI${SPI_INDEX?string}_CallbackRegister (SPI_EVENT_HANDLER eventHandler, void* context)
{
    spi${SPI_INDEX?string}Obj.callback = eventHandler;
    spi${SPI_INDEX?string}Obj.context = context;
}


bool SPI${SPI_INDEX?string}_IsBusy()
{  
    return spi${SPI_INDEX?string}Obj.exchangeIsBusy;
}

void SPI${SPI_INDEX?string}_InterruptHandler(void)
{    
    /* Since the write cycle had started in Exchange API itself, start with read cycle here */
    if ( true == _SPI${SPI_INDEX?string}_REGS->SPI_SR.RDRF )
    {
        if (NULL == spi${SPI_INDEX?string}Obj.rxBuffer)
        {
            // Dummy Read
            _SPI${SPI_INDEX?string}_REGS->SPI_RDR.RD;
        }
        else if(SPI_CSR_BITS_8_BIT == (_SPI${SPI_INDEX?string}_REGS->SPI_CSR[spi${SPI_INDEX?string}Obj.chipSelect & 0xFF].w & SPI_CSR_BITS_Msk))
        {
            ((uint8_t*)spi${SPI_INDEX?string}Obj.rxBuffer)[spi${SPI_INDEX?string}Obj.rxCount] = _SPI${SPI_INDEX?string}_REGS->SPI_RDR.RD;
        }
        else
        {
            ((uint16_t*)spi${SPI_INDEX?string}Obj.rxBuffer)[spi${SPI_INDEX?string}Obj.rxCount] = _SPI${SPI_INDEX?string}_REGS->SPI_RDR.RD;
        }
        spi${SPI_INDEX?string}Obj.rxCount++;
    } 
   
    /* If there are more words to be transmitted, then transmit them here and keep track of the count */
    if((spi${SPI_INDEX?string}Obj.txCount < spi${SPI_INDEX?string}Obj.exchangeSize) && (true == _SPI${SPI_INDEX?string}_REGS->SPI_SR.TDRE))
    {   
        if (NULL == spi${SPI_INDEX?string}Obj.txBuffer )
        {   
            // do a dummy write
            _SPI${SPI_INDEX?string}_REGS->SPI_TDR.w = 0xFFFF | (spi${SPI_INDEX?string}Obj.chipSelect & 0x000F0000);
        }
        else if(SPI_CSR_BITS_8_BIT == (_SPI${SPI_INDEX?string}_REGS->SPI_CSR[spi${SPI_INDEX?string}Obj.chipSelect & 0xFF].w & SPI_CSR_BITS_Msk))
        {
            _SPI${SPI_INDEX?string}_REGS->SPI_TDR.w = ((uint8_t*)spi${SPI_INDEX?string}Obj.txBuffer)[spi${SPI_INDEX?string}Obj.txCount] | (spi${SPI_INDEX?string}Obj.chipSelect & 0x000F0000);
        }
        else
        {
            _SPI${SPI_INDEX?string}_REGS->SPI_TDR.w = ((uint16_t*)spi${SPI_INDEX?string}Obj.txBuffer)[spi${SPI_INDEX?string}Obj.txCount] | (spi${SPI_INDEX?string}Obj.chipSelect & 0x000F0000);
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

