/*******************************************************************************
  SERIAL COMMUNICATION SERIAL PERIPHERAL INTERFACE(SERCOM5_SPI) PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_sercom5_spi.c

  Summary
    SERCOM5_SPI PLIB Implementation File.

  Description
    This file defines the interface to the SERCOM SPI peripheral library.
    This library provides access to and control of the associated
    peripheral instance.

  Remarks:
    None.

*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
* Copyright (C) 2018 Microchip Technology Inc. and its subsidiaries.
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
// DOM-IGNORE-END

#include "plib_sercom5_spi.h"
#include "device.h"

// *****************************************************************************
// *****************************************************************************
// Section: MACROS Definitions
// *****************************************************************************
// *****************************************************************************
/* Sercom clk freq value for the baud calculation */
#define SERCOM5_Frequency      (uint32_t) (48000000UL)

/*Global object to save SPI Exchange related data  */
SPI_OBJECT sercom5SPIObj;

// *****************************************************************************
// *****************************************************************************
// Section: SERCOM5_SPI Implementation
// *****************************************************************************
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Function:
    void SERCOM5_SPI_Initialize(void);

  Summary:
    Initializes instance SERCOM5 of the SERCOM module operating in SPI mode.

  Description:
    This function initializes instance SERCOM5 of SERCOM module operating in SPI mode.
    This function should be called before any other library function. The SERCOM
    module will be configured as per the MHC settings.

  Remarks:
    Refer plib_sercom5_spi.h file for more information.
*/

void SERCOM5_SPI_Initialize(void)
{
    /* Instantiate the SERCOM5 SPI object */
    sercom5SPIObj.callback = NULL ;
    sercom5SPIObj.transferIsBusy = false ;

    /* Selection of the Character Size and Receiver Enable */
    SERCOM5_REGS->SPI.CTRLB = SERCOM_SPI_CTRLB_CHSIZE(0x0) | SERCOM_SPI_CTRLB_RXEN_Msk ;

    /* Wait for synchronization */
    while(SERCOM5_REGS->SPI.SYNCBUSY);

    /* Selection of the Baud Value */
    SERCOM5_REGS->SPI.BAUD = 23;

    /* Configure Data Out Pin Out , Master Mode,
     * Data In and Pin Out,Data Order and Standby mode if configured
     * and Selection of the Clock Phase and Polarity and Enable the SPI Module
     */
    SERCOM5_REGS->SPI.CTRLA = SERCOM_SPI_CTRLA_MODE(0x03)| SERCOM_SPI_CTRLA_DOPO(0x1) | SERCOM_SPI_CTRLA_DIPO(0x0)| SPI_CLOCK_POLARITY_IDLE_LOW | SPI_CLOCK_PHASE_LEADING_EDGE | SERCOM_SPI_CTRLA_ENABLE_Msk ;

    /* Wait for synchronization */
    while(SERCOM5_REGS->SPI.SYNCBUSY);

}

// *****************************************************************************
/* Function:
    bool SERCOM5_SPI_TransferSetup(SPI_TRANSFER_SETUP *setup,
                                                uint32_t spiSourceClock);

 Summary:
    Configure SERCOM SPI operational parameters at run time.

  Description:
    This function allows the application to change the SERCOM SPI operational
    parameter at run time. The application can thus override the MHC defined
    configuration for these parameters. The parameter are specified via the
    SPI_TRANSFER_SETUP type setup parameter. Each member of this parameter
    should be initialized to the desired value.

    The application may feel need to call this function in situation where
    multiple SPI slaves, each with different operation parameters, are connected
    to one SPI master. This function can thus be used to setup the SPI Master to
    meet the communication needs of the slave.

    Calling this function will affect any ongoing communication. The application
    must thus ensure that there is no on-going communication on the SPI before
    calling this function.

  Remarks:
    Refer plib_sercom5_spi.h file for more information.
*/

bool SERCOM5_SPI_TransferSetup(SPI_TRANSFER_SETUP *setup, uint32_t spiSourceClock)
{
    uint32_t baudValue = 0;

    bool statusValue = false;

    if(spiSourceClock == 0)
    {
        /* Fetch Master Clock Frequency directly */
        spiSourceClock = SERCOM5_Frequency;
    }

    /* Disable the SPI Module */
    SERCOM5_REGS->SPI.CTRLA &= ~(SERCOM_SPI_CTRLA_ENABLE_Msk);

     /* Wait for synchronization */
    while(SERCOM5_REGS->SPI.SYNCBUSY);

    if ( setup != NULL )
    {
        baudValue = (spiSourceClock/(2*(setup->clockFrequency))) - 1;

        if ((baudValue > 0) & (baudValue <= 255))
        {
            /* Selection of the Clock Polarity and Clock Phase */
            SERCOM5_REGS->SPI.CTRLA |= setup->clockPolarity | setup->clockPhase;

            /* Selection of the Baud Value */
            SERCOM5_REGS->SPI.BAUD = baudValue;

            /* Selection of the Character Size */
            SERCOM5_REGS->SPI.CTRLB |= setup->dataBits;

            /* Wait for synchronization */
            while(SERCOM5_REGS->SPI.SYNCBUSY);

            statusValue = true;
        }
    }

    /* Enabling the SPI Module */
    SERCOM5_REGS->SPI.CTRLA |= SERCOM_SPI_CTRLA_ENABLE_Msk;

    /* Wait for synchronization */
    while(SERCOM5_REGS->SPI.SYNCBUSY);

    return statusValue;
}


// *****************************************************************************
/* Function:
    void SERCOM5_SPI_CallbackRegister(const SERCOM_SPI_CALLBACK* callBack,
                                                    uintptr_t context);

  Summary:
    Allows application to register callback with PLIB.

  Description:
    This function allows application to register an event handling function
    for the PLIB to call back when requested data exchange operation has
    completed or any error has occurred.
    The callback should be registered before the client performs exchange
    operation.
    At any point if application wants to stop the callback, it can use this
    function with "callBack" value as NULL.

  Remarks:
    Refer plib_sercom5_spi.h file for more information.
*/

void SERCOM5_SPI_CallbackRegister(SERCOM_SPI_CALLBACK callBack, uintptr_t context )
{
    sercom5SPIObj.callback = callBack;

    sercom5SPIObj.context = context;
}

// *****************************************************************************
/* Function:
    bool SERCOM5_SPI_IsBusy(void);

  Summary:
    Returns transfer status of SERCOM SERCOM5SPI.

  Description:
    This function ture if the SERCOM SERCOM5SPI module is busy with a transfer. The
    application can use the function to check if SERCOM SERCOM5SPI module is busy
    before calling any of the data transfer functions. The library does not
    allow a data transfer operation if another transfer operation is already in
    progress.

    This function can be used as an alternative to the callback function when
    the library is operating interrupt mode. The allow the application to
    implement a synchronous interface to the library.

  Remarks:
    Refer plib_sercom5_spi.h file for more information.
*/

bool SERCOM5_SPI_IsBusy(void)
{
    return sercom5SPIObj.transferIsBusy;
}

// *****************************************************************************
/* Function:
    bool SERCOM5_SPI_WriteRead (void* pTransmitData, size_t txSize
                                        void* pReceiveData, size_t rxSize);

  Summary:
    Write and Read data on SERCOM SERCOM5 SPI peripheral.

  Description:
    This function transmits "txSize" number of bytes and receives "rxSize"
    number of bytes on SERCOM SERCOM5 SPI module. Data pointed by pTransmitData is
    transmitted and received data is saved in the location pointed by
    pReceiveData. The function will transfer the maximum of "txSize" or "rxSize"
    data units towards completion.

    When "Interrupt Mode" option is unchecked in MHC, this function will be
    blocking in nature.  In this mode, the function will not return until all
    the requested data is transferred.  The function returns true after
    transferring all the data.  This indicates that the operation has been
    completed.

    When "Interrupt Mode" option is selected in MHC, the function will be
    non-blocking in nature.  The function returns immediately. The data transfer
    process continues in the peripheral interrupt.  The application specified
    transmit and receive buffer  are ownerd by the library until the data
    transfer is complete and should not be modified by the application till the
    transfer is complete.  Only one transfer is allowed at any time. The
    Application can use a callback function or a polling function to check for
    completion of the transfer. If a callback is required, this should be
    registered prior to calling the SERCOM5_SPI_WriteRead() function. The
    application can use the SERCOM5_SPI_IsBusy() to poll for completion.

  Remarks:
    Refer plib_sercom5_spi.h file for more information.
*/

bool SERCOM5_SPI_WriteRead (void* pTransmitData, size_t txSize, void* pReceiveData, size_t rxSize)
{
    bool isRequestAccepted = false;
    uint32_t dummyData = 0;

    /* Verify the request */
    if((((txSize > 0) && (pTransmitData != NULL)) || ((rxSize > 0) && (pReceiveData != NULL))) && (sercom5SPIObj.transferIsBusy == false))
    {
        if((SERCOM5_REGS->SPI.CTRLB & SERCOM_SPI_CTRLB_CHSIZE_Msk) == SPI_DATA_BITS_9)
        {
            /* For 9-bit transmission, the txSize and rxSize must be an even number. */
            if ( ((txSize > 0) && (txSize & 0x01)) || ((rxSize > 0) && (rxSize & 0x01)))
            {
                return isRequestAccepted;
            }
        }

        isRequestAccepted = true;
        sercom5SPIObj.txBuffer = pTransmitData;
        sercom5SPIObj.rxBuffer = pReceiveData;
        sercom5SPIObj.rxCount = 0;
        sercom5SPIObj.txCount = 0;
        sercom5SPIObj.dummySize = 0;
        if (pTransmitData != NULL)
        {
            sercom5SPIObj.txSize = txSize;
        }
        else
        {
            sercom5SPIObj.txSize = 0;
        }

        if (pReceiveData != NULL)
        {
            sercom5SPIObj.rxSize = rxSize;
        }
        else
        {
            sercom5SPIObj.rxSize = 0;
        }

        sercom5SPIObj.transferIsBusy = true;

        /* Flush out any unread data in SPI read buffer */
        dummyData = SERCOM5_REGS->SPI.DATA;
        (void)dummyData;

        if (sercom5SPIObj.rxSize > sercom5SPIObj.txSize)
        {
            sercom5SPIObj.dummySize = sercom5SPIObj.rxSize - sercom5SPIObj.txSize;
        }

        /* Start the first write here itself, rest will happen in ISR context */
        if((SERCOM5_REGS->SPI.CTRLB & SERCOM_SPI_CTRLB_CHSIZE_Msk) == SPI_DATA_BITS_8)
        {
            if (sercom5SPIObj.txCount < sercom5SPIObj.txSize)
            {
                SERCOM5_REGS->SPI.DATA = *((uint8_t*)sercom5SPIObj.txBuffer);
                sercom5SPIObj.txCount++;
            }
            else if (sercom5SPIObj.dummySize > 0)
            {
                SERCOM5_REGS->SPI.DATA = 0xFF;
                sercom5SPIObj.dummySize--;
            }
        }
        else
        {
            sercom5SPIObj.txSize >>= 1;
            sercom5SPIObj.dummySize >>= 1;
            sercom5SPIObj.rxSize >>= 1;

            if (sercom5SPIObj.txCount < sercom5SPIObj.txSize)
            {
                SERCOM5_REGS->SPI.DATA = *((uint16_t*)sercom5SPIObj.txBuffer) & SERCOM_SPI_DATA_Msk;
                sercom5SPIObj.txCount++;
            }
            else if (sercom5SPIObj.dummySize > 0)
            {
                SERCOM5_REGS->SPI.DATA = 0xFFFF & SERCOM_SPI_DATA_Msk;
                sercom5SPIObj.dummySize--;
            }
        }

        if (rxSize > 0)
        {
            /* Enable ReceiveComplete  */
            SERCOM5_REGS->SPI.INTENSET = SERCOM_SPI_INTENSET_RXC_Msk;
        }
        else
        {
            /* Enable the DataRegisterEmpty  */
            SERCOM5_REGS->SPI.INTENSET = SERCOM_SPI_INTENSET_DRE_Msk;
        }
    }

    return isRequestAccepted;
}

// *****************************************************************************
/* Function:
    void SERCOM5_SPI_InterruptHandler(void);

  Summary:
    Handler that handles the SPI interrupts

  Description:
    This Function is called from the handler to handle the exchange based on the
    Interrupts.

  Remarks:
    Refer plib_sercom5_spi.h file for more information.
*/

void SERCOM5_SPI_InterruptHandler(void)
{
    uint32_t dataBits = 0;
    uint32_t receivedData = 0;
    static bool isLastByteTransferInProgress = false;

    if(SERCOM5_REGS->SPI.INTENSET != 0)
    {
        dataBits = SERCOM5_REGS->SPI.CTRLB & SERCOM_SPI_CTRLB_CHSIZE_Msk;

        if ((SERCOM5_REGS->SPI.INTFLAG & SERCOM_SPI_INTFLAG_RXC_Msk) == SERCOM_SPI_INTFLAG_RXC_Msk)
        {
            receivedData =  SERCOM5_REGS->SPI.DATA;

            if (sercom5SPIObj.rxCount < sercom5SPIObj.rxSize)
            {
                if(dataBits == SPI_DATA_BITS_8)
                {
                    ((uint8_t*)sercom5SPIObj.rxBuffer)[sercom5SPIObj.rxCount++] = receivedData;
                }
                else
                {
                    ((uint16_t*)sercom5SPIObj.rxBuffer)[sercom5SPIObj.rxCount++] = receivedData;
                }
            }
        }


        /* If there are more words to be transmitted, then transmit them here and keep track of the count */
        if((SERCOM5_REGS->SPI.INTFLAG & SERCOM_SPI_INTFLAG_DRE_Msk) == SERCOM_SPI_INTFLAG_DRE_Msk)
        {
            /* Disable the DRE interrupt. This will be enabled back if more than
             * one byte is pending to be transmitted */

            SERCOM5_REGS->SPI.INTENCLR =  SERCOM_SPI_INTENCLR_DRE_Msk;

            if(dataBits == SPI_DATA_BITS_8)
            {
                if (sercom5SPIObj.txCount < sercom5SPIObj.txSize)
                {
                    SERCOM5_REGS->SPI.DATA = ((uint8_t*)sercom5SPIObj.txBuffer)[sercom5SPIObj.txCount++];
                }
                else if (sercom5SPIObj.dummySize > 0)
                {
                    SERCOM5_REGS->SPI.DATA = 0xFF;
                    sercom5SPIObj.dummySize--;
                }
            }
            else
            {
                if (sercom5SPIObj.txCount < sercom5SPIObj.txSize)
                {
                    SERCOM5_REGS->SPI.DATA = ((uint16_t*)sercom5SPIObj.txBuffer)[sercom5SPIObj.txCount++];
                }
                else if (sercom5SPIObj.dummySize > 0)
                {
                    SERCOM5_REGS->SPI.DATA = 0xFFFF;
                    sercom5SPIObj.dummySize--;
                }
            }


            if ((sercom5SPIObj.txCount == sercom5SPIObj.txSize) && (0 == sercom5SPIObj.dummySize))
            {
                 /* At higher baud rates, the data in the shift register can be
                 * shifted out and TXC flag can get set resulting in a
                 * callback been given to the application with the SPI interrupt
                 * pending with the application. This will then result in the
                 * interrupt handler being called again with nothing to transmit.
                 * To avoid this, a software flag is set, but
                 * the TXC interrupt is not enabled until the very end.
                 */

                isLastByteTransferInProgress = true;

            }
            else if(sercom5SPIObj.rxCount == sercom5SPIObj.rxSize)
            {
                SERCOM5_REGS->SPI.INTENSET = SERCOM_SPI_INTENSET_DRE_Msk;
                SERCOM5_REGS->SPI.INTENCLR = SERCOM_SPI_INTENCLR_RXC_Msk;
            }
        }


        if(((SERCOM5_REGS->SPI.INTFLAG & SERCOM_SPI_INTFLAG_TXC_Msk) == SERCOM_SPI_INTFLAG_TXC_Msk) && (isLastByteTransferInProgress == true))
        {
            if (sercom5SPIObj.rxCount == sercom5SPIObj.rxSize)
            {
                sercom5SPIObj.transferIsBusy = false;

                /* Disable the Data Register empty and Receive Complete Interrupt flags */
                SERCOM5_REGS->SPI.INTENCLR = SERCOM_SPI_INTENCLR_DRE_Msk | SERCOM_SPI_INTENCLR_RXC_Msk | SERCOM_SPI_INTENSET_TXC_Msk;

                 isLastByteTransferInProgress = false;

                if(sercom5SPIObj.callback != NULL)
                {
                    sercom5SPIObj.callback(sercom5SPIObj.context);
                }
            }
        }

        if(isLastByteTransferInProgress == true)
        {
            /* For the last byte transfer, the TDRE interrupt is already disabled.
             * Enable TXC interrupt to ensure no data is present in the shift
             * register before application callback is called.
             */
             SERCOM5_REGS->SPI.INTENSET = SERCOM_SPI_INTENSET_TXC_Msk;
        }
    }
}
