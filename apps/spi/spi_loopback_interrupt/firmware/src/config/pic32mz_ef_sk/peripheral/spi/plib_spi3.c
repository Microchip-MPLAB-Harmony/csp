/*******************************************************************************
  SPI PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_spi3.c

  Summary:
    SPI3 Source File

  Description:
    This file has implementation of all the interfaces provided for particular
    SPI peripheral.

*******************************************************************************/

/*******************************************************************************
* Copyright (C) 2018-2019 Microchip Technology Inc. and its subsidiaries.
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

#include "plib_spi3.h"

// *****************************************************************************
// *****************************************************************************
// Section: SPI3 Implementation
// *****************************************************************************
// *****************************************************************************
/* Global object to save SPI Exchange related data */
SPI_OBJECT spi3Obj;

void SPI3_Initialize ( void )
{
    uint32_t rdata;
    /*Disable SPI3_FAULT Interrupt, */
    /*Disable SPI3_RX Interrupt, */
    /*Disable SPI3_TX Interrupt */
    IEC4CLR = _IEC4_SPI3EIE_MASK;
    IEC4CLR = _IEC4_SPI3RXIE_MASK;
    IEC4CLR = _IEC4_SPI3TXIE_MASK;
 
    /* STOP and Reset the SPI*/
    SPI3CON = 0;

    /*Clear the Receiver buffer */
    rdata = SPI3BUF;

    /*clear SPI3_FAULT Interrupt flag */
    /*clear SPI3_RX Interrupt flag */
    /*Clear SPI3_TX Interrupt flag*/
    IFS4CLR = _IFS4_SPI3EIF_MASK;
    IFS4CLR = _IFS4_SPI3RXIF_MASK;
    IFS4CLR = _IFS4_SPI3TXIF_MASK;

    /*Clear SPI3 Fault Priority and Sub-priority*/
    IPC38CLR = _IPC38_SPI3EIP_MASK | _IPC38_SPI3EIS_MASK;
    /*Clear SPI3 RX Priority and Sub-priority*/
    IPC38CLR = _IPC38_SPI3RXIP_MASK | _IPC38_SPI3RXIS_MASK;
     /*Clear SPI3 TX Priority and Sub-priority*/
    IPC39CLR = _IPC39_SPI3TXIP_MASK | _IPC39_SPI3TXIS_MASK;

    /* Priority	= 7	*/
	/* Sub-priority	= 3	*/
    IPC38SET = 0x1f0000; 

    /* Priority	= 7	*/
	/* Sub-priority	= 3	*/
    IPC38SET = 0x1f000000; 

     /* Priority	= 7	*/
	/* Sub-priority	= 3	*/
    IPC39SET = 0x1f; 

    /*Enable SPI3_FAULT Interrupt, */
    /*Enable SPI3_RX Interrupt, */

    IEC4SET = _IEC4_SPI3EIE_MASK;
    IEC4SET = _IEC4_SPI3RXIE_MASK;
    
     /* BAUD Rate register Setup */
    SPI3BRG = 49;

    /* CLear the Overflow */
    SPI3STATCLR = _SPI3STAT_SPIROV_MASK;
    
    /*
    MSTEN = 1
    CKP = 0
    CKE = 0
    MODE<32,16> = 0
    MSSEN = 1
    MCLKSEL = 0
    */
    SPI3CONSET = 0x10000020;

    /* Initialize global variables */
    spi3Obj.transferIsBusy = false;
    spi3Obj.faultcallback = NULL;
    spi3Obj.rxcallback = NULL;
    spi3Obj.txcallback = NULL;


    /* Enable SPI3 */
     SPI3CONSET= _SPI3CON_ON_MASK;
    return;
}

bool SPI3_WriteRead (void* pTransmitData, size_t txSize, void* pReceiveData, size_t rxSize)
{
    bool isRequestAccepted = false;
    uint32_t dummyData;

    /* Verify the request */
    if((((txSize > 0) && (pTransmitData != NULL)) || ((rxSize > 0) && (pReceiveData != NULL))) && (spi3Obj.transferIsBusy == false))
    {
        isRequestAccepted = true;
        spi3Obj.txBuffer = pTransmitData;
        spi3Obj.rxBuffer = pReceiveData;
        spi3Obj.rxCount = 0;
        spi3Obj.txCount = 0;
        spi3Obj.dummySize = 0;
        if (pTransmitData != NULL)
        {
            spi3Obj.txSize = txSize;
        }
        else
        {
            spi3Obj.txSize = 0;
        }

        if (pReceiveData != NULL)
        {
            spi3Obj.rxSize = rxSize;
        }
        else
        {
            spi3Obj.rxSize = 0;
        }

        spi3Obj.transferIsBusy = true;

        /* Flush out any unread data in SPI read buffer */
        dummyData = SPI3BUF;
        (void)dummyData;

        if (spi3Obj.rxSize > spi3Obj.txSize)
        {
            spi3Obj.dummySize = spi3Obj.rxSize - spi3Obj.txSize;
        }

        /* Start the first write here itself, rest will happen in ISR context */
         if((_SPI3CON_MODE32_MASK) == SPI3CON & (_SPI3CON_MODE32_MASK))
         {
            spi3Obj.txSize >>= 2;
            spi3Obj.dummySize >>= 2;
            spi3Obj.rxSize >>= 2;

            if(spi3Obj.txCount < spi3Obj.txSize)
            {
                SPI3BUF= *((uint32_t*)spi3Obj.txBuffer);
                spi3Obj.txCount++;
            }
            else if (spi3Obj.dummySize > 0)
            {
                SPI3BUF= (uint32_t)(0xff);
                spi3Obj.dummySize--;
            }
         }
         else if((_SPI3CON_MODE16_MASK) == SPI3CON & (_SPI3CON_MODE16_MASK))
         {
            spi3Obj.txSize >>= 1;
            spi3Obj.dummySize >>= 1;
            spi3Obj.rxSize >>= 1;

            if (spi3Obj.txCount < spi3Obj.txSize)
            {
                SPI3BUF= *((uint16_t*)spi3Obj.txBuffer);
                spi3Obj.txCount++;
            }
            else if (spi3Obj.dummySize > 0)
            {
                SPI3BUF= (uint16_t)(0xff);
                spi3Obj.dummySize--;
            }
        }
        else
        {
            if (spi3Obj.txCount < spi3Obj.txSize)
            {
                SPI3BUF= *((uint8_t*)spi3Obj.txBuffer);
                spi3Obj.txCount++;
            }
            else if (spi3Obj.dummySize > 0)
            {
                SPI3BUF= (uint8_t)(0xff);
                spi3Obj.dummySize--;
            }
        }
        
        if (rxSize > 0)
        {
            /* Enable receive interrupt to complete the transfer in ISR context */
            IEC4SET = _IEC4_SPI3RXIE_MASK;
        }
        else
        {
            /* Enable transmit interrupt to complete the transfer in ISR context */
            IEC4SET = _IEC4_SPI3TXIE_MASK;
        }

    }

    return isRequestAccepted;
}

bool SPI3_TransferSetup (SPI_TRANSFER_SETUP * setup, uint32_t spiSourceClock )
{
    uint32_t t_brg;
    uint32_t baudHigh;
    uint32_t baudLow;
    uint32_t errorHigh;
    uint32_t errorLow;

    if ((setup == NULL) || (setup->clockFrequency == 0))
	{
		return false;
	}
    if(spiSourceClock == 0)
    {
        // Use Master Clock Frequency set in GUI
        spiSourceClock = 100000000;
    }

    t_brg = (((spiSourceClock/(setup->clockFrequency))/2u)-1u);
    baudHigh = spiSourceClock / (2u * (t_brg + 1u));
    baudLow = spiSourceClock / (2u * (t_brg + 2u));
    errorHigh = baudHigh - setup->clockFrequency;
    errorLow = setup->clockFrequency - baudLow;

    if (errorHigh > errorLow)
    {
        t_brg++;
    }
    if(t_brg > 8191)
    {
        return false;
    } 

    SPI3BRG = t_brg;
    SPI3CONSET = setup->clockPolarity | setup->clockPhase | setup->dataBits;

    return true;
}



void SPI3_FaultCallbackRegister (SPI_CALLBACK callback, uintptr_t context)
{
    spi3Obj.faultcallback = callback;
    spi3Obj.faultcontext = context;
}

void SPI3_FAULT_Tasks (void)
{
        
    /* Client must call SPI3_ErrorGet( void ) function to clear the errors first */
    if(spi3Obj.faultcallback != NULL)
        {
            spi3Obj.rxcallback(spi3Obj.faultcontext);
        }
         /* Clear receiver overflow error*/
    SPI3STATCLR = _SPI3STAT_SPIROV_MASK;
    /*Clear SPI3 Fault Interrupt flag */
    IFS4CLR = _IFS4_SPI3EIF_MASK;
    
}

SPI_ERROR SPI3_ErrorGet( void )
{
    SPI_ERROR error = SPI_ERROR_NONE;
    uint32_t dummy;
     if (_SPI3STAT_SPIROV_MASK  == (SPI3STAT & _SPI3STAT_SPIROV_MASK))
     {
        /* Read the SPIxBUF to flush it */
        dummy =  SPI3BUF;
     }
     return error;
}
    
bool SPI3_IsBusy()
{
    return spi3Obj.transferIsBusy;
}


void SPI3_ReadCallbackRegister (SPI_CALLBACK callback, uintptr_t context)
{
    spi3Obj.rxcallback = callback;
    spi3Obj.rxcontext = context;
}

void SPI3_RX_Tasks (void)
{
     uint32_t receivedData =0 ;

    if (_SPI3STAT_SPIRBF_MASK  == (SPI3STAT & _SPI3STAT_SPIRBF_MASK))
    {
       /* We have data waiting in the SPI buffer */
        receivedData = SPI3BUF;
        /*Clear SPI3 RX Interrupt flag */
        /* This flag should cleared only after reading buffer*/
        IFS4CLR = _IFS4_SPI3RXIF_MASK;  

        if (spi3Obj.rxCount < spi3Obj.rxSize)
        {
              /* Enable Transmit interrupt for transmit*/
               IEC4SET = _IEC4_SPI3TXIE_MASK;

            if((_SPI3CON_MODE32_MASK) == SPI3CON & (_SPI3CON_MODE32_MASK))
            {
                ((uint32_t*)spi3Obj.rxBuffer)[spi3Obj.rxCount++] = receivedData;
            }
            else if((_SPI3CON_MODE16_MASK) == SPI3CON & (_SPI3CON_MODE16_MASK)) 
            {
                ((uint16_t*)spi3Obj.rxBuffer)[spi3Obj.rxCount++] = receivedData;
            }
            else
            {
                ((uint8_t*)spi3Obj.rxBuffer)[spi3Obj.rxCount++] = receivedData;
            }
        }

        if (spi3Obj.rxCount == spi3Obj.rxSize)
        {
            spi3Obj.transferIsBusy = false;

            if(spi3Obj.rxcallback != NULL)
            {
                IEC4CLR = _IEC4_SPI3RXIE_MASK;
                spi3Obj.rxcallback(spi3Obj.rxcontext);
            }
        } 
                           
    }
    
}

void SPI3_WriteCallbackRegister (SPI_CALLBACK callback, uintptr_t context)
{
    spi3Obj.txcallback = callback;
    spi3Obj.txcontext = context;
}

void SPI3_TX_Tasks (void)
{
    uint32_t dataBits ;
    uint32_t receivedData;
    static bool isLastByteTransferInProgress = false;
     
     /* If there are more words to be transmitted, then transmit them here and keep track of the count */
    if(_SPI3STAT_SPITBE_MASK  == (SPI3STAT & _SPI3STAT_SPITBE_MASK))
    {       
         /* Disable the Transmit interrupt if bytes needs to be received. This will be enabled back if more than
         * one byte is pending to be transmitted */
         if (spi3Obj.rxCount < spi3Obj.rxSize)
         {
                IEC4CLR = _IEC4_SPI3TXIE_MASK;
         }

        if((_SPI3CON_MODE32_MASK) == SPI3CON & (_SPI3CON_MODE32_MASK))
        {
             if (spi3Obj.txCount < spi3Obj.txSize)
            {
              SPI3BUF = ((uint32_t*)spi3Obj.txBuffer)[spi3Obj.txCount++];
            }
            else if (spi3Obj.dummySize > 0)
            {
              SPI3BUF = (uint32_t)(0xff);
              spi3Obj.dummySize--;
            }    
        }
        else if((_SPI3CON_MODE16_MASK) == SPI3CON & (_SPI3CON_MODE16_MASK)) 
        {
            if (spi3Obj.txCount < spi3Obj.txSize)
            {
              SPI3BUF = ((uint16_t*)spi3Obj.txBuffer)[spi3Obj.txCount++];
            }
            else if (spi3Obj.dummySize > 0)
            {
              SPI3BUF = (uint16_t)(0xff);
              spi3Obj.dummySize--;
            }
        }    
        else
        { 
            if (spi3Obj.txCount < spi3Obj.txSize)
            {
              SPI3BUF = ((uint8_t*)spi3Obj.txBuffer)[spi3Obj.txCount++];
            }
            else if (spi3Obj.dummySize > 0)
            {
              SPI3BUF = (uint8_t)(0xff);
                spi3Obj.dummySize--;
            }
        }
        
        /*Clear SPI3 TX Interrupt flag after writing on buffer */
        IFS4CLR = _IFS4_SPI3TXIF_MASK;

        if ((spi3Obj.txCount == spi3Obj.txSize) && (spi3Obj.dummySize == 0))
        {
              /* all bytes are transmitted. Disable Transmit Interrupt */
            IEC4CLR = _IEC4_SPI3TXIE_MASK;
            if(spi3Obj.txcallback != NULL)
            {
                spi3Obj.txcallback(spi3Obj.txcontext);
            }
        }
    }

}


/*******************************************************************************
 End of File
*/

