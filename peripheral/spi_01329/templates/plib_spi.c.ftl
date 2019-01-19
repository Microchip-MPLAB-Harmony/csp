/*******************************************************************************
  SPI PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${SPI_INSTANCE_NAME?lower_case}.c

  Summary:
    ${SPI_INSTANCE_NAME} Source File

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

#include "plib_${SPI_INSTANCE_NAME?lower_case}.h"

// *****************************************************************************
// *****************************************************************************
// Section: ${SPI_INSTANCE_NAME} Implementation
// *****************************************************************************
// *****************************************************************************
<#if (SPI_INTERRUPT_MODE == true) >
/* Global object to save SPI Exchange related data */
SPI_OBJECT ${SPI_INSTANCE_NAME?lower_case}Obj;
</#if>

void ${SPI_INSTANCE_NAME}_Initialize ( void )
{
    uint32_t rdata;
    /*Disable ${SPI_INSTANCE_NAME}_FAULT Interrupt, */
    /*Disable ${SPI_INSTANCE_NAME}_RX Interrupt, */
    /*Disable ${SPI_INSTANCE_NAME}_TX Interrupt */
    ${SPI_FLT_IEC_REG}CLR = _${SPI_FLT_IEC_REG}_${SPI_INSTANCE_NAME}EIE_MASK;
    ${SPI_RX_IEC_REG}CLR = _${SPI_RX_IEC_REG}_${SPI_INSTANCE_NAME}RXIE_MASK;
    ${SPI_TX_IEC_REG}CLR = _${SPI_TX_IEC_REG}_${SPI_INSTANCE_NAME}TXIE_MASK;
 
    /* STOP and Reset the SPI*/
    ${SPI_INSTANCE_NAME}CON = 0;

    /*Clear the Receiver buffer */
    rdata = ${SPI_INSTANCE_NAME}BUF;

    /*clear ${SPI_INSTANCE_NAME}_FAULT Interrupt flag */
    /*clear ${SPI_INSTANCE_NAME}_RX Interrupt flag */
    /*Clear ${SPI_INSTANCE_NAME}_TX Interrupt flag*/
    ${SPI_FLT_IFS_REG}CLR = _${SPI_FLT_IFS_REG}_${SPI_INSTANCE_NAME}EIF_MASK;
    ${SPI_RX_IFS_REG}CLR = _${SPI_RX_IFS_REG}_${SPI_INSTANCE_NAME}RXIF_MASK;
    ${SPI_TX_IFS_REG}CLR = _${SPI_TX_IFS_REG}_${SPI_INSTANCE_NAME}TXIF_MASK;

 <#if (SPI_INTERRUPT_MODE == true)> 
    /*Clear ${SPI_INSTANCE_NAME} Fault Priority and Sub-priority*/
    ${SPI_FLT_IPC_REG}CLR = _${SPI_FLT_IPC_REG}_${SPI_INSTANCE_NAME}EIP_MASK | _${SPI_FLT_IPC_REG}_${SPI_INSTANCE_NAME}EIS_MASK;
    /*Clear ${SPI_INSTANCE_NAME} RX Priority and Sub-priority*/
    ${SPI_RX_IPC_REG}CLR = _${SPI_RX_IPC_REG}_${SPI_INSTANCE_NAME}RXIP_MASK | _${SPI_RX_IPC_REG}_${SPI_INSTANCE_NAME}RXIS_MASK;
     /*Clear ${SPI_INSTANCE_NAME} TX Priority and Sub-priority*/
    ${SPI_TX_IPC_REG}CLR = _${SPI_TX_IPC_REG}_${SPI_INSTANCE_NAME}TXIP_MASK | _${SPI_TX_IPC_REG}_${SPI_INSTANCE_NAME}TXIS_MASK;

    /* Priority	= ${SPI_FLT_IPC_PRI_VALUE}	*/
	/* Sub-priority	= ${SPI_FLT_IPC_SUBPRI_VALUE}	*/
    ${SPI_FLT_IPC_REG}SET = 0x${SPI_FLT_IPC_VALUE}; 

    /* Priority	= ${SPI_RX_IPC_PRI_VALUE}	*/
	/* Sub-priority	= ${SPI_RX_IPC_SUBPRI_VALUE}	*/
    ${SPI_RX_IPC_REG}SET = 0x${SPI_RX_IPC_VALUE}; 

     /* Priority	= ${SPI_TX_IPC_PRI_VALUE}	*/
	/* Sub-priority	= ${SPI_TX_IPC_SUBPRI_VALUE}	*/
    ${SPI_TX_IPC_REG}SET = 0x${SPI_TX_IPC_VALUE}; 

    /*Enable ${SPI_INSTANCE_NAME}_FAULT Interrupt, */
    /*Enable ${SPI_INSTANCE_NAME}_RX Interrupt, */

    ${SPI_FLT_IEC_REG}SET = _${SPI_FLT_IEC_REG}_${SPI_INSTANCE_NAME}EIE_MASK;
    ${SPI_RX_IEC_REG}SET = _${SPI_RX_IEC_REG}_${SPI_INSTANCE_NAME}RXIE_MASK;
    
</#if>
     /* BAUD Rate register Setup */
    ${SPI_INSTANCE_NAME}BRG = ${SPI_BRG_VALUE};

    /* CLear the Overflow */
    ${SPI_INSTANCE_NAME}STATCLR = _${SPI_INSTANCE_NAME}STAT_SPIROV_MASK;
    
    /*
    MSTEN = ${SPI_MSTR_MODE_EN}
    CKP = ${SPI_SPICON_CLK_POL}
    CKE = ${SPI_SPICON_CLK_PH}
    MODE<32,16> = ${SPI_SPICON_MODE}
    MSSEN = ${SPI_SPICON_MSSEN}
    MCLKSEL = ${SPI_MASTER_CLOCK}
    */
    ${SPI_INSTANCE_NAME}CONSET = 0x${SPICON_REG_VALUE};

<#if (SPI_INTERRUPT_MODE == true) >
    /* Initialize global variables */
    ${SPI_INSTANCE_NAME?lower_case}Obj.transferIsBusy = false;
    ${SPI_INSTANCE_NAME?lower_case}Obj.faultcallback = NULL;
    ${SPI_INSTANCE_NAME?lower_case}Obj.rxcallback = NULL;
    ${SPI_INSTANCE_NAME?lower_case}Obj.txcallback = NULL;

</#if>

    /* Enable ${SPI_INSTANCE_NAME} */
     ${SPI_INSTANCE_NAME}CONSET= _${SPI_INSTANCE_NAME}CON_ON_MASK;
    return;
}

<#if (SPI_INTERRUPT_MODE == false) >

bool ${SPI_INSTANCE_NAME}_WriteRead(void* pTransmitData, size_t txSize, void* pReceiveData, size_t rxSize)
{
    size_t txCount = 0;
    size_t rxCount = 0;
    size_t dummySize = 0;
    size_t receivedData;
    uint32_t dataBits;
    bool isSuccess = false;

    /* Verify the request */
    if (((txSize > 0) && (pTransmitData != NULL)) || ((rxSize > 0) && (pReceiveData != NULL)))
    {
        if (pTransmitData == NULL)
        {
            txSize = 0;
        }
        if (pReceiveData == NULL)
        {
            rxSize = 0;
        }

        dataBits = ${SPI_INSTANCE_NAME}CON & (_${SPI_INSTANCE_NAME}CON_MODE32_MASK | _${SPI_INSTANCE_NAME}CON_MODE16_MASK);

        /* Flush out any unread data in SPI read buffer from the previous transfer */
        receivedData = ${SPI_INSTANCE_NAME}BUF;

        if (rxSize > txSize)
        {
            dummySize = rxSize - txSize;
        }
        /* If dataBit size is 32 bits */
        if (_${SPI_INSTANCE_NAME}CON_MODE32_MASK == ${SPI_INSTANCE_NAME}CON & _${SPI_INSTANCE_NAME}CON_MODE32_MASK)
        {
            rxSize >>= 2;
            txSize >>= 2;
            dummySize >>= 2;
        }
        /* If dataBit size is 16 bits */
        else if (_${SPI_INSTANCE_NAME}CON_MODE16_MASK == ${SPI_INSTANCE_NAME}CON & _${SPI_INSTANCE_NAME}CON_MODE16_MASK)
        {
            rxSize >>= 1;
            txSize >>= 1;
            dummySize >>= 1;
        }

        /* Make sure transmit buffer is empty */
        while((bool)(${SPI_INSTANCE_NAME}STAT & _${SPI_INSTANCE_NAME}STAT_SPITBE_MASK) == false)
        {
            ;
        }

        while ((txCount != txSize) || (dummySize != 0))
        {
            if (txCount != txSize)
            {
                if((_${SPI_INSTANCE_NAME}CON_MODE32_MASK) == ${SPI_INSTANCE_NAME}CON & (_${SPI_INSTANCE_NAME}CON_MODE32_MASK))
                {
                    ${SPI_INSTANCE_NAME}BUF= ((uint32_t*)pTransmitData)[txCount++];
                }
                else if((_${SPI_INSTANCE_NAME}CON_MODE16_MASK) == ${SPI_INSTANCE_NAME}CON & (_${SPI_INSTANCE_NAME}CON_MODE16_MASK)) 
                {
                    ${SPI_INSTANCE_NAME}BUF= ((uint16_t*)pTransmitData)[txCount++];
                }
                else
                {
                    ${SPI_INSTANCE_NAME}BUF= ((uint8_t*)pTransmitData)[txCount++];
                }            
            }
            else if (dummySize > 0)
            {
             ${SPI_INSTANCE_NAME}BUF= 0x${SPI_DUMMY_DATA};
                dummySize--;
            }

            if (rxSize == 0)
            {
               /* For transmit only request, wait for buffer to become empty */
               while((bool)(${SPI_INSTANCE_NAME}STAT & _${SPI_INSTANCE_NAME}STAT_SPITBE_MASK) == false)
               {
                 ;
               }
            }
            else
            {
                /* If data is read, wait for the Receiver Data Register to become full*/
                while((bool)(${SPI_INSTANCE_NAME}STAT & _${SPI_INSTANCE_NAME}STAT_SPIRBF_MASK) == false)
				{
                    ;
				}
				 /* We have data waiting in the SPI buffer */
                receivedData = ${SPI_INSTANCE_NAME}BUF;
                if (rxCount < rxSize)
                {
                    if((_${SPI_INSTANCE_NAME}CON_MODE32_MASK) == ${SPI_INSTANCE_NAME}CON & (_${SPI_INSTANCE_NAME}CON_MODE32_MASK))
                    {
                        ((uint32_t*)pReceiveData)[rxCount++]  = receivedData;
                    }
                    else if((_${SPI_INSTANCE_NAME}CON_MODE16_MASK) == ${SPI_INSTANCE_NAME}CON & (_${SPI_INSTANCE_NAME}CON_MODE16_MASK)) 
                    {
                        ((uint16_t*)pReceiveData)[rxCount++]  = receivedData;
                    }
                    else
                    {
                        ((uint8_t*)pReceiveData)[rxCount++]  = receivedData;
                    }
                }
            }
        }
        if(_${SPI_INSTANCE_NAME}CON_ENHBUF_MASK == (${SPI_INSTANCE_NAME}CON & _${SPI_INSTANCE_NAME}CON_ENHBUF_MASK))
        {
            /* Make sure no data is pending in the shift register */
            while ((bool)(${SPI_INSTANCE_NAME}STAT & _${SPI_INSTANCE_NAME}STAT_SRMT_MASK == false))
            {
                ;
            }
        }
        isSuccess = true;
    }
	    return isSuccess;
}
<#else>
bool ${SPI_INSTANCE_NAME}_WriteRead (void* pTransmitData, size_t txSize, void* pReceiveData, size_t rxSize)
{
    bool isRequestAccepted = false;
    uint32_t dummyData;

    /* Verify the request */
    if((((txSize > 0) && (pTransmitData != NULL)) || ((rxSize > 0) && (pReceiveData != NULL))) && (${SPI_INSTANCE_NAME?lower_case}Obj.transferIsBusy == false))
    {
        isRequestAccepted = true;
        ${SPI_INSTANCE_NAME?lower_case}Obj.txBuffer = pTransmitData;
        ${SPI_INSTANCE_NAME?lower_case}Obj.rxBuffer = pReceiveData;
        ${SPI_INSTANCE_NAME?lower_case}Obj.rxCount = 0;
        ${SPI_INSTANCE_NAME?lower_case}Obj.txCount = 0;
        ${SPI_INSTANCE_NAME?lower_case}Obj.dummySize = 0;
        if (pTransmitData != NULL)
        {
            ${SPI_INSTANCE_NAME?lower_case}Obj.txSize = txSize;
        }
        else
        {
            ${SPI_INSTANCE_NAME?lower_case}Obj.txSize = 0;
        }

        if (pReceiveData != NULL)
        {
            ${SPI_INSTANCE_NAME?lower_case}Obj.rxSize = rxSize;
        }
        else
        {
            ${SPI_INSTANCE_NAME?lower_case}Obj.rxSize = 0;
        }

        ${SPI_INSTANCE_NAME?lower_case}Obj.transferIsBusy = true;

        /* Flush out any unread data in SPI read buffer */
        dummyData = ${SPI_INSTANCE_NAME}BUF;
        (void)dummyData;

        if (${SPI_INSTANCE_NAME?lower_case}Obj.rxSize > ${SPI_INSTANCE_NAME?lower_case}Obj.txSize)
        {
            ${SPI_INSTANCE_NAME?lower_case}Obj.dummySize = ${SPI_INSTANCE_NAME?lower_case}Obj.rxSize - ${SPI_INSTANCE_NAME?lower_case}Obj.txSize;
        }

        /* Start the first write here itself, rest will happen in ISR context */
         if((_${SPI_INSTANCE_NAME}CON_MODE32_MASK) == ${SPI_INSTANCE_NAME}CON & (_${SPI_INSTANCE_NAME}CON_MODE32_MASK))
         {
            ${SPI_INSTANCE_NAME?lower_case}Obj.txSize >>= 2;
            ${SPI_INSTANCE_NAME?lower_case}Obj.dummySize >>= 2;
            ${SPI_INSTANCE_NAME?lower_case}Obj.rxSize >>= 2;

            if(${SPI_INSTANCE_NAME?lower_case}Obj.txCount < ${SPI_INSTANCE_NAME?lower_case}Obj.txSize)
            {
                ${SPI_INSTANCE_NAME}BUF= *((uint32_t*)${SPI_INSTANCE_NAME?lower_case}Obj.txBuffer);
                ${SPI_INSTANCE_NAME?lower_case}Obj.txCount++;
            }
            else if (${SPI_INSTANCE_NAME?lower_case}Obj.dummySize > 0)
            {
                ${SPI_INSTANCE_NAME}BUF= (uint32_t)(0x${SPI_DUMMY_DATA});
                ${SPI_INSTANCE_NAME?lower_case}Obj.dummySize--;
            }
         }
         else if((_${SPI_INSTANCE_NAME}CON_MODE16_MASK) == ${SPI_INSTANCE_NAME}CON & (_${SPI_INSTANCE_NAME}CON_MODE16_MASK))
         {
            ${SPI_INSTANCE_NAME?lower_case}Obj.txSize >>= 1;
            ${SPI_INSTANCE_NAME?lower_case}Obj.dummySize >>= 1;
            ${SPI_INSTANCE_NAME?lower_case}Obj.rxSize >>= 1;

            if (${SPI_INSTANCE_NAME?lower_case}Obj.txCount < ${SPI_INSTANCE_NAME?lower_case}Obj.txSize)
            {
                ${SPI_INSTANCE_NAME}BUF= *((uint16_t*)${SPI_INSTANCE_NAME?lower_case}Obj.txBuffer);
                ${SPI_INSTANCE_NAME?lower_case}Obj.txCount++;
            }
            else if (${SPI_INSTANCE_NAME?lower_case}Obj.dummySize > 0)
            {
                ${SPI_INSTANCE_NAME}BUF= (uint16_t)(0x${SPI_DUMMY_DATA});
                ${SPI_INSTANCE_NAME?lower_case}Obj.dummySize--;
            }
        }
        else
        {
            if (${SPI_INSTANCE_NAME?lower_case}Obj.txCount < ${SPI_INSTANCE_NAME?lower_case}Obj.txSize)
            {
                ${SPI_INSTANCE_NAME}BUF= *((uint8_t*)${SPI_INSTANCE_NAME?lower_case}Obj.txBuffer);
                ${SPI_INSTANCE_NAME?lower_case}Obj.txCount++;
            }
            else if (${SPI_INSTANCE_NAME?lower_case}Obj.dummySize > 0)
            {
                ${SPI_INSTANCE_NAME}BUF= (uint8_t)(0x${SPI_DUMMY_DATA});
                ${SPI_INSTANCE_NAME?lower_case}Obj.dummySize--;
            }
        }
        
        if (rxSize > 0)
        {
            /* Enable receive interrupt to complete the transfer in ISR context */
            ${SPI_RX_IEC_REG}SET = _${SPI_RX_IEC_REG}_${SPI_INSTANCE_NAME}RXIE_MASK;
        }
        else
        {
            /* Enable transmit interrupt to complete the transfer in ISR context */
            ${SPI_TX_IEC_REG}SET = _${SPI_TX_IEC_REG}_${SPI_INSTANCE_NAME}TXIE_MASK;
        }

    }

    return isRequestAccepted;
}
</#if>

bool ${SPI_INSTANCE_NAME}_TransferSetup (SPI_TRANSFER_SETUP * setup, uint32_t spiSourceClock )
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
        spiSourceClock = ${SPI_MASTER_FREQ_VALUE};
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

    ${SPI_INSTANCE_NAME}BRG = t_brg;
    ${SPI_INSTANCE_NAME}CONSET = setup->clockPolarity | setup->clockPhase | setup->dataBits;

    return true;
}

<#if (SPI_INTERRUPT_MODE == true) >


void ${SPI_INSTANCE_NAME}_FaultCallbackRegister (SPI_CALLBACK callback, uintptr_t context)
{
    ${SPI_INSTANCE_NAME?lower_case}Obj.faultcallback = callback;
    ${SPI_INSTANCE_NAME?lower_case}Obj.faultcontext = context;
}

void ${SPI_INSTANCE_NAME}_FAULT_Tasks (void)
{
        
    /* Client must call ${SPI_INSTANCE_NAME}_ErrorGet( void ) function to clear the errors first */
    if(${SPI_INSTANCE_NAME?lower_case}Obj.faultcallback != NULL)
        {
            ${SPI_INSTANCE_NAME?lower_case}Obj.rxcallback(${SPI_INSTANCE_NAME?lower_case}Obj.faultcontext);
        }
         /* Clear receiver overflow error*/
    ${SPI_INSTANCE_NAME}STATCLR = _${SPI_INSTANCE_NAME}STAT_SPIROV_MASK;
    /*Clear ${SPI_INSTANCE_NAME} Fault Interrupt flag */
    ${SPI_FLT_IFS_REG}CLR = _${SPI_FLT_IFS_REG}_${SPI_INSTANCE_NAME}EIF_MASK;
    
}

SPI_ERROR ${SPI_INSTANCE_NAME}_ErrorGet( void )
{
    SPI_ERROR error = SPI_ERROR_NONE;
    uint32_t dummy;
     if (_${SPI_INSTANCE_NAME}STAT_SPIROV_MASK  == (${SPI_INSTANCE_NAME}STAT & _${SPI_INSTANCE_NAME}STAT_SPIROV_MASK))
     {
        /* Read the SPIxBUF to flush it */
        dummy =  ${SPI_INSTANCE_NAME}BUF;
     }
     return error;
}
    
bool ${SPI_INSTANCE_NAME}_IsBusy()
{
    return ${SPI_INSTANCE_NAME?lower_case}Obj.transferIsBusy;
}


void ${SPI_INSTANCE_NAME}_ReadCallbackRegister (SPI_CALLBACK callback, uintptr_t context)
{
    ${SPI_INSTANCE_NAME?lower_case}Obj.rxcallback = callback;
    ${SPI_INSTANCE_NAME?lower_case}Obj.rxcontext = context;
}

void ${SPI_INSTANCE_NAME}_RX_Tasks (void)
{
     uint32_t receivedData =0 ;

    if (_${SPI_INSTANCE_NAME}STAT_SPIRBF_MASK  == (${SPI_INSTANCE_NAME}STAT & _${SPI_INSTANCE_NAME}STAT_SPIRBF_MASK))
    {
       /* We have data waiting in the SPI buffer */
        receivedData = ${SPI_INSTANCE_NAME}BUF;
        /*Clear ${SPI_INSTANCE_NAME} RX Interrupt flag */
        /* This flag should cleared only after reading buffer*/
        ${SPI_RX_IFS_REG}CLR = _${SPI_RX_IFS_REG}_${SPI_INSTANCE_NAME}RXIF_MASK;  

        if (${SPI_INSTANCE_NAME?lower_case}Obj.rxCount < ${SPI_INSTANCE_NAME?lower_case}Obj.rxSize)
        {
              /* Enable Transmit interrupt for transmit*/
               ${SPI_TX_IEC_REG}SET = _${SPI_TX_IEC_REG}_${SPI_INSTANCE_NAME}TXIE_MASK;

            if((_${SPI_INSTANCE_NAME}CON_MODE32_MASK) == ${SPI_INSTANCE_NAME}CON & (_${SPI_INSTANCE_NAME}CON_MODE32_MASK))
            {
                ((uint32_t*)${SPI_INSTANCE_NAME?lower_case}Obj.rxBuffer)[${SPI_INSTANCE_NAME?lower_case}Obj.rxCount++] = receivedData;
            }
            else if((_${SPI_INSTANCE_NAME}CON_MODE16_MASK) == ${SPI_INSTANCE_NAME}CON & (_${SPI_INSTANCE_NAME}CON_MODE16_MASK)) 
            {
                ((uint16_t*)${SPI_INSTANCE_NAME?lower_case}Obj.rxBuffer)[${SPI_INSTANCE_NAME?lower_case}Obj.rxCount++] = receivedData;
            }
            else
            {
                ((uint8_t*)${SPI_INSTANCE_NAME?lower_case}Obj.rxBuffer)[${SPI_INSTANCE_NAME?lower_case}Obj.rxCount++] = receivedData;
            }
        }

        if (${SPI_INSTANCE_NAME?lower_case}Obj.rxCount == ${SPI_INSTANCE_NAME?lower_case}Obj.rxSize)
        {
            ${SPI_INSTANCE_NAME?lower_case}Obj.transferIsBusy = false;

            if(${SPI_INSTANCE_NAME?lower_case}Obj.rxcallback != NULL)
            {
                ${SPI_RX_IEC_REG}CLR = _${SPI_RX_IEC_REG}_${SPI_INSTANCE_NAME}RXIE_MASK;
                ${SPI_INSTANCE_NAME?lower_case}Obj.rxcallback(${SPI_INSTANCE_NAME?lower_case}Obj.rxcontext);
            }
        } 
                           
    }
    
}

void ${SPI_INSTANCE_NAME}_WriteCallbackRegister (SPI_CALLBACK callback, uintptr_t context)
{
    ${SPI_INSTANCE_NAME?lower_case}Obj.txcallback = callback;
    ${SPI_INSTANCE_NAME?lower_case}Obj.txcontext = context;
}

void ${SPI_INSTANCE_NAME}_TX_Tasks (void)
{
    uint32_t dataBits ;
    uint32_t receivedData;
    static bool isLastByteTransferInProgress = false;
     
     /* If there are more words to be transmitted, then transmit them here and keep track of the count */
    if(_${SPI_INSTANCE_NAME}STAT_SPITBE_MASK  == (${SPI_INSTANCE_NAME}STAT & _${SPI_INSTANCE_NAME}STAT_SPITBE_MASK))
    {       
         /* Disable the Transmit interrupt if bytes needs to be received. This will be enabled back if more than
         * one byte is pending to be transmitted */
         if (${SPI_INSTANCE_NAME?lower_case}Obj.rxCount < ${SPI_INSTANCE_NAME?lower_case}Obj.rxSize)
         {
                ${SPI_TX_IEC_REG}CLR = _${SPI_TX_IEC_REG}_${SPI_INSTANCE_NAME}TXIE_MASK;
         }

        if((_${SPI_INSTANCE_NAME}CON_MODE32_MASK) == ${SPI_INSTANCE_NAME}CON & (_${SPI_INSTANCE_NAME}CON_MODE32_MASK))
        {
             if (${SPI_INSTANCE_NAME?lower_case}Obj.txCount < ${SPI_INSTANCE_NAME?lower_case}Obj.txSize)
            {
              ${SPI_INSTANCE_NAME}BUF = ((uint32_t*)${SPI_INSTANCE_NAME?lower_case}Obj.txBuffer)[${SPI_INSTANCE_NAME?lower_case}Obj.txCount++];
            }
            else if (${SPI_INSTANCE_NAME?lower_case}Obj.dummySize > 0)
            {
              ${SPI_INSTANCE_NAME}BUF = (uint32_t)(0x${SPI_DUMMY_DATA});
              ${SPI_INSTANCE_NAME?lower_case}Obj.dummySize--;
            }    
        }
        else if((_${SPI_INSTANCE_NAME}CON_MODE16_MASK) == ${SPI_INSTANCE_NAME}CON & (_${SPI_INSTANCE_NAME}CON_MODE16_MASK)) 
        {
            if (${SPI_INSTANCE_NAME?lower_case}Obj.txCount < ${SPI_INSTANCE_NAME?lower_case}Obj.txSize)
            {
              ${SPI_INSTANCE_NAME}BUF = ((uint16_t*)${SPI_INSTANCE_NAME?lower_case}Obj.txBuffer)[${SPI_INSTANCE_NAME?lower_case}Obj.txCount++];
            }
            else if (${SPI_INSTANCE_NAME?lower_case}Obj.dummySize > 0)
            {
              ${SPI_INSTANCE_NAME}BUF = (uint16_t)(0x${SPI_DUMMY_DATA});
              ${SPI_INSTANCE_NAME?lower_case}Obj.dummySize--;
            }
        }    
        else
        { 
            if (${SPI_INSTANCE_NAME?lower_case}Obj.txCount < ${SPI_INSTANCE_NAME?lower_case}Obj.txSize)
            {
              ${SPI_INSTANCE_NAME}BUF = ((uint8_t*)${SPI_INSTANCE_NAME?lower_case}Obj.txBuffer)[${SPI_INSTANCE_NAME?lower_case}Obj.txCount++];
            }
            else if (${SPI_INSTANCE_NAME?lower_case}Obj.dummySize > 0)
            {
              ${SPI_INSTANCE_NAME}BUF = (uint8_t)(0x${SPI_DUMMY_DATA});
                ${SPI_INSTANCE_NAME?lower_case}Obj.dummySize--;
            }
        }
        
        /*Clear ${SPI_INSTANCE_NAME} TX Interrupt flag after writing on buffer */
        ${SPI_TX_IFS_REG}CLR = _${SPI_TX_IFS_REG}_${SPI_INSTANCE_NAME}TXIF_MASK;

        if ((${SPI_INSTANCE_NAME?lower_case}Obj.txCount == ${SPI_INSTANCE_NAME?lower_case}Obj.txSize) && (${SPI_INSTANCE_NAME?lower_case}Obj.dummySize == 0))
        {
              /* all bytes are transmitted. Disable Transmit Interrupt */
            ${SPI_TX_IEC_REG}CLR = _${SPI_TX_IEC_REG}_${SPI_INSTANCE_NAME}TXIE_MASK;
            if(${SPI_INSTANCE_NAME?lower_case}Obj.txcallback != NULL)
            {
                ${SPI_INSTANCE_NAME?lower_case}Obj.txcallback(${SPI_INSTANCE_NAME?lower_case}Obj.txcontext);
            }
        }
    }

}
</#if>


/*******************************************************************************
 End of File
*/

