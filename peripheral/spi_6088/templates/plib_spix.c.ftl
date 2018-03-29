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
    SPI${SPI_INDEX?string}_REGS->SPI_CR = SPI_CR_SPIDIS_Msk | SPI_CR_SWRST_Msk;

<#if SPI_MR_MSTR =="MASTER">   
    /* Enable Master mode, select particular NPCS line for chip select and disable mode fault detection */
    SPI${SPI_INDEX?string}_REGS->SPI_MR =  SPI_MR_MSTR_Msk | SPI_MR_PCS_${SPI_MR_PCS} | SPI_MR_MODFDIS_Msk;       
<#else>
    /* SPI is by default in Slave Mode, disable mode fault detection */
    SPI${SPI_INDEX?string}_REGS->SPI_MR =  SPI_MR_MODFDIS_Msk;
</#if>
 
    /* Set up clock Polarity, data phase, Communication Width and Baud Rate */
    SPI${SPI_INDEX?string}_REGS->SPI_CSR[${SPI_CSR_INDEX}]= SPI_CSR_CPOL_${SPI_CSR_CPOL} | SPI_CSR_NCPHA_${SPI_CSR_NCPHA} | SPI_CSR_BITS${SPI_CSR_BITS} | SPI_CSR_SCBR(${SPI_CSR_SCBR_VALUE});
       
<#if SPI_INTERRUPT_MODE == true >
    /* Initialize global variables */
    spi${SPI_INDEX?string}Obj.transferIsBusy = false;
    spi${SPI_INDEX?string}Obj.callback = NULL;
    spi${SPI_INDEX?string}Obj.status = SPI_ERROR_NONE;
</#if>

    /* Enable SPI${SPI_INDEX?string} */
    SPI${SPI_INDEX?string}_REGS->SPI_CR = SPI_CR_SPIEN_Msk;
    return;
}

<#if SPI_INTERRUPT_MODE == false >
bool SPI${SPI_INDEX?string}_WriteRead(void* pTransmitData, size_t txSize, void* pReceiveData, size_t rxSize)
{
    size_t txCount = 0;
    size_t rxCount = 0;
    size_t dummySize = 0;
    size_t receivedData;
    uint32_t dataBits;
    bool isSuccess = false;
    
    /* Verify the request */
    if (((txSize > 0) && (NULL != pTransmitData)) || ((rxSize > 0) && (NULL != pReceiveData)))
    {                
        dataBits = SPI${SPI_INDEX?string}_REGS->SPI_CSR[${SPI_CSR_INDEX}] & SPI_CSR_BITS_Msk;    

        /* Flush out any unread data in SPI read buffer from the previous transfer */
        receivedData = (SPI${SPI_INDEX?string}_REGS->SPI_RDR & SPI_RDR_RD_Msk) >> SPI_RDR_RD_Pos;     

        if (rxSize > txSize)
        {
            dummySize = rxSize - txSize;
        }
        if (SPI_CSR_BITS_8_BIT != dataBits)
        {
            rxSize >>= 1;
            txSize >>= 1;
            dummySize >>= 1;
        }
        
        /* Make sure TDR is empty */
        while(false == (bool)((SPI${SPI_INDEX?string}_REGS->SPI_SR & SPI_SR_TDRE_Msk) >> SPI_SR_TDRE_Pos));

        while ((txCount != txSize) || (dummySize != 0))
        {            
            if (txCount != txSize)
            {
                if(SPI_CSR_BITS_8_BIT == dataBits)
                {
                    SPI${SPI_INDEX?string}_REGS->SPI_TDR = ((uint8_t*)pTransmitData)[txCount++];
                }
                else
                {
                    SPI${SPI_INDEX?string}_REGS->SPI_TDR = ((uint16_t*)pTransmitData)[txCount++];
                }
            }
            else if (dummySize > 0)
            {                        
                if(SPI_CSR_BITS_8_BIT == dataBits)
                {
                    SPI${SPI_INDEX?string}_REGS->SPI_TDR = 0xFF;            
                }
                else
                {
                    SPI${SPI_INDEX?string}_REGS->SPI_TDR = 0xFFFF;            
                }            
                dummySize--;
            }
            
            if (0 == rxSize)
            {            
                /* For transmit only request, wait for TDR to become empty */
                while(false == (bool)((SPI${SPI_INDEX?string}_REGS->SPI_SR & SPI_SR_TDRE_Msk) >> SPI_SR_TDRE_Pos));
            }
            else
            {
                /* If data is read, wait for the Receiver Data Register to become full*/
                while(false == (bool)((SPI${SPI_INDEX?string}_REGS->SPI_SR & SPI_SR_RDRF_Msk) >> SPI_SR_RDRF_Pos))
				{
				}
				
				receivedData = (SPI${SPI_INDEX?string}_REGS->SPI_RDR & SPI_RDR_RD_Msk) >> SPI_RDR_RD_Pos;
				
                if (rxCount < rxSize)
                {
                    if(SPI_CSR_BITS_8_BIT == dataBits)
                    {
                        ((uint8_t*)pReceiveData)[rxCount++] = receivedData;
                    }
                    else
                    {
                        ((uint16_t*)pReceiveData)[rxCount++] = receivedData;
                    }
                }
            }
        }

        /* Make sure no data is pending in the shift register */
        while (false == (bool)((SPI${SPI_INDEX?string}_REGS->SPI_SR & SPI_SR_TXEMPTY_Msk) >> SPI_SR_TXEMPTY_Pos));
        
        isSuccess = true;                
    }
	    return isSuccess;
}
<#else>
bool SPI${SPI_INDEX?string}_WriteRead (void* pTransmitData, size_t txSize, void* pReceiveData, size_t rxSize)
{
    bool isRequestAccepted = false; 
    uint32_t dummyData;        
    
    /* Verify the request */
    if(((txSize > 0) && (NULL != pTransmitData)) || ((rxSize > 0) && (NULL != pReceiveData)))
    {
        return isRequestAccepted;
    }
    
    /* Validate the argument */
    if(false == spi${SPI_INDEX?string}Obj.transferIsBusy)
    {        
        isRequestAccepted = true;
        spi${SPI_INDEX?string}Obj.txBuffer = pTransmitData;
        spi${SPI_INDEX?string}Obj.rxBuffer = pReceiveData;
        spi${SPI_INDEX?string}Obj.rxCount = 0;
        spi${SPI_INDEX?string}Obj.txCount = 0;
        spi${SPI_INDEX?string}Obj.dummySize = 0;
        spi${SPI_INDEX?string}Obj.txSize = txSize;
        spi${SPI_INDEX?string}Obj.rxSize = rxSize;
        spi${SPI_INDEX?string}Obj.transferIsBusy = true;        
        spi${SPI_INDEX?string}Obj.status = SPI_ERROR_NONE;
        
        /* Flush out any unread data in SPI read buffer */
        dummyData = (SPI${SPI_INDEX?string}_REGS->SPI_RDR & SPI_RDR_RD_Msk) >> SPI_RDR_RD_Pos; 
        (void)dummyData;
        
        if (spi${SPI_INDEX?string}Obj.rxSize > spi${SPI_INDEX?string}Obj.txSize)
        {
            spi${SPI_INDEX?string}Obj.dummySize = spi${SPI_INDEX?string}Obj.rxSize - spi${SPI_INDEX?string}Obj.txSize;
        }
                
        /* Start the first write here itself, rest will happen in ISR context */
        if(SPI_CSR_BITS_8_BIT == (SPI${SPI_INDEX?string}_REGS->SPI_CSR[${SPI_CSR_INDEX}] & SPI_CSR_BITS_Msk))
        {
            if (spi${SPI_INDEX?string}Obj.txCount < spi${SPI_INDEX?string}Obj.txSize)
            {
                SPI${SPI_INDEX?string}_REGS->SPI_TDR = *((uint8_t*)spi${SPI_INDEX?string}Obj.txBuffer);
                spi${SPI_INDEX?string}Obj.txCount++;
            }
            else if (spi${SPI_INDEX?string}Obj.dummySize > 0)
            {
                SPI${SPI_INDEX?string}_REGS->SPI_TDR = 0xFF;
                spi${SPI_INDEX?string}Obj.dummySize--;
            }           
        }
        else
        {
            spi${SPI_INDEX?string}Obj.txSize >>= 1;
            spi${SPI_INDEX?string}Obj.dummySize >>= 1;
            spi${SPI_INDEX?string}Obj.rxSize >>= 1;
            
            if (spi${SPI_INDEX?string}Obj.txCount < spi${SPI_INDEX?string}Obj.txSize)
            {
                SPI${SPI_INDEX?string}_REGS->SPI_TDR = *((uint16_t*)spi${SPI_INDEX?string}Obj.txBuffer);                
                spi${SPI_INDEX?string}Obj.txCount++;                
            }
            else if (spi${SPI_INDEX?string}Obj.dummySize > 0)
            {
                SPI${SPI_INDEX?string}_REGS->SPI_TDR = 0xFFFF;                
                spi${SPI_INDEX?string}Obj.dummySize--;                                
            }                        
        }       
                                        
        if (rxSize > 0)
        {
            /* Enable receive interrupt to complete the transfer in ISR context */                    
            SPI${SPI_INDEX?string}_REGS->SPI_IER = SPI_IER_RDRF_Msk;                        
        }
        else
        {
            /* Enable transmit interrupt to complete the transfer in ISR context */        
            SPI${SPI_INDEX?string}_REGS->SPI_IER = SPI_IER_TDRE_Msk;
        }       
    }
    
    return isRequestAccepted;
}
</#if>

bool SPI${SPI_INDEX?string}_TransferSetup (SPI_TRANSFER_SETUP * setup, uint32_t spiSourceClock )
{
    uint32_t scbr;
    if (0 == setup->clockFrequency)
	{
		return false;
	}
    if(0 == spiSourceClock)
    {
        // Fetch Master Clock Frequency directly
        spiSourceClock = ${SPI_MASTER_CLOCK};
    }

    scbr = spiSourceClock/setup->clockFrequency;
    
    if(0 == scbr)
    {
        scbr = 1;
    }
    else if(scbr > 255)
    {
        scbr = 255;
    }
    
    SPI${SPI_INDEX?string}_REGS->SPI_CSR[${SPI_CSR_INDEX}]= setup->clockPolarity | setup->clockPhase | SPI_CSR_BITS(setup->dataBits) | SPI_CSR_SCBR(scbr);

    return true;
}

<#if SPI_INTERRUPT_MODE == true >
SPI_ERROR SPI${SPI_INDEX?string}_ErrorGet ( void )
{
    return (SPI_ERROR)(spi${SPI_INDEX?string}Obj.status & (SPI_SR_OVRES_Msk));
}

void SPI${SPI_INDEX?string}_CallbackRegister (SPI_CALLBACK callback, void* context)
{
    spi${SPI_INDEX?string}Obj.callback = callback;
    spi${SPI_INDEX?string}Obj.context = context;
}

bool SPI${SPI_INDEX?string}_IsBusy()
{  
    return spi${SPI_INDEX?string}Obj.transferIsBusy;
}

void SPI${SPI_INDEX?string}_InterruptHandler(void)
{   
    uint32_t dataBits ;
    uint32_t receivedData;    
    dataBits = SPI${SPI_INDEX?string}_REGS->SPI_CSR[${SPI_CSR_INDEX}] & SPI_CSR_BITS_Msk;    
    
    /* save the status in global object before it gets cleared */
    spi${SPI_INDEX?string}Obj.status = SPI${SPI_INDEX?string}_REGS->SPI_SR;              
        
    if ( SPI_SR_RDRF_Msk == (SPI${SPI_INDEX?string}_REGS->SPI_SR & SPI_SR_RDRF_Msk ))
    {                                           
        receivedData = (SPI${SPI_INDEX?string}_REGS->SPI_RDR & SPI_RDR_RD_Msk) >> SPI_RDR_RD_Pos; 
            
        if (spi${SPI_INDEX?string}Obj.rxCount < spi${SPI_INDEX?string}Obj.rxSize)
        {
            if(SPI_CSR_BITS_8_BIT == dataBits)
            {
                ((uint8_t*)spi${SPI_INDEX?string}Obj.rxBuffer)[spi${SPI_INDEX?string}Obj.rxCount++] = receivedData;
            }
            else
            {
                ((uint16_t*)spi${SPI_INDEX?string}Obj.rxBuffer)[spi${SPI_INDEX?string}Obj.rxCount++] = receivedData;
            }                
        }                                   
    }    
        
    /* If there are more words to be transmitted, then transmit them here and keep track of the count */
    if(SPI_SR_TDRE_Msk == (SPI${SPI_INDEX?string}_REGS->SPI_SR & SPI_SR_TDRE_Msk))
    {                           
        if(SPI_CSR_BITS_8_BIT == dataBits)
        {
            if (spi${SPI_INDEX?string}Obj.txCount < spi${SPI_INDEX?string}Obj.txSize)
            {
                SPI${SPI_INDEX?string}_REGS->SPI_TDR = ((uint8_t*)spi${SPI_INDEX?string}Obj.txBuffer)[spi${SPI_INDEX?string}Obj.txCount++];                
            }
            else if (spi${SPI_INDEX?string}Obj.dummySize > 0)
            {
                SPI${SPI_INDEX?string}_REGS->SPI_TDR = 0xFF;
                spi${SPI_INDEX?string}Obj.dummySize--;
            }                                          
        }
        else
        {
            if (spi${SPI_INDEX?string}Obj.txCount < spi${SPI_INDEX?string}Obj.txSize)
            {
                SPI${SPI_INDEX?string}_REGS->SPI_TDR = ((uint16_t*)spi${SPI_INDEX?string}Obj.txBuffer)[spi${SPI_INDEX?string}Obj.txCount++];                
            }
            else if (spi${SPI_INDEX?string}Obj.dummySize > 0)
            {
                SPI${SPI_INDEX?string}_REGS->SPI_TDR = 0xFFFF;
                spi${SPI_INDEX?string}Obj.dummySize--;
            }              
        }       
        if ((spi${SPI_INDEX?string}Obj.txCount == spi${SPI_INDEX?string}Obj.txSize) && (0 == spi${SPI_INDEX?string}Obj.dummySize))
        {            
            /* Disable the TDRE interrupt and enable TXEMPTY interrupt to ensure
             * no data is present in the shift register before CS is de-selected  
             */
            SPI${SPI_INDEX?string}_REGS->SPI_IDR = SPI_IDR_TDRE_Msk; 
            SPI${SPI_INDEX?string}_REGS->SPI_IER = SPI_IER_TXEMPTY_Msk;                                         
        }     
    }       
                    
    /* See if Exchange is complete */        
    if ((SPI_IMR_TXEMPTY_Msk == (SPI${SPI_INDEX?string}_REGS->SPI_IMR & SPI_IMR_TXEMPTY_Msk)) && (SPI_SR_TXEMPTY_Msk == (SPI${SPI_INDEX?string}_REGS->SPI_SR & SPI_SR_TXEMPTY_Msk)))        
    {        
        if (spi${SPI_INDEX?string}Obj.rxCount == spi${SPI_INDEX?string}Obj.rxSize)
        {
            spi${SPI_INDEX?string}Obj.transferIsBusy = false;                        
            
            /* Disable TDRE, RDRF and TXEMPTY interrupts */
            SPI${SPI_INDEX?string}_REGS->SPI_IDR = SPI_IDR_TDRE_Msk | SPI_IDR_RDRF_Msk | SPI_IDR_TXEMPTY_Msk;                  
            
            /* Flush out any pending SPI IRQ with NVIC */
            NVIC_ClearPendingIRQ(SPI0_IRQn);                        
                                           
            if(spi${SPI_INDEX?string}Obj.callback != NULL)
            {
                spi${SPI_INDEX?string}Obj.callback(spi${SPI_INDEX?string}Obj.context);
            }                                   
        }
    }
}
</#if>


/*******************************************************************************
 End of File
*/

