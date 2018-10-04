/*******************************************************************************
  SERIAL COMMUNICATION SERIAL PERIPHERAL INTERFACE(${SERCOM_INSTANCE_NAME}_SPI) PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_${SERCOM_INSTANCE_NAME?lower_case}_spi.c

  Summary
    ${SERCOM_INSTANCE_NAME}_SPI PLIB Implementation File.

  Description
    This file defines the interface to the SERCOM SPI peripheral library.
    This library provides access to and control of the associated
    peripheral instance.

  Remarks:
    None.

*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
* © 2018 Microchip Technology Inc. and its subsidiaries.
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

#include "plib_${SERCOM_INSTANCE_NAME?lower_case}_spi.h"
#include "device.h"

// *****************************************************************************
// *****************************************************************************
// Section: MACROS Definitions
// *****************************************************************************
// *****************************************************************************

/* Macro for the Master Mode value */
#define SPI_MASTER_MODE_VALUE           (0x03)

/* Macro for the Slave Mode value */
#define SPI_SLAVE_MODE_VALUE            (0x02)

/* macro for the spi frame default value */
#define SPI_FRAME_VALUE                 (0x00)

/* CPU freq Value for the baud calculation */
#define CPU_FREQ                        (4000000UL)

/* Transfer Mode(Combination of Clock polarity and Phase */
#define SPI_TRANSFER_MODE               (${SPI_TRANSFER_MODE}U)

/* Calculation of baud value */
#define BAUD_VALUE                      ((4000000/(2*${SPI_BAUD_RATE}))-1)

<#if SPI_INTERRUPT_MODE = true>
/*Global object to save SPI Exchange related data  */
SPI_OBJECT ${SERCOM_INSTANCE_NAME?lower_case}SPIObj;
</#if>

// *****************************************************************************
// *****************************************************************************
// Section: ${SERCOM_INSTANCE_NAME}_SPI Implementation
// *****************************************************************************
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Function:
    void ${SERCOM_INSTANCE_NAME}_SPI_Initialize(void);

  Summary:
    Initializes instance ${SERCOM_INSTANCE_NAME} of the SERCOM module operating in SPI mode.

  Description:
    This function initializes instance ${SERCOM_INSTANCE_NAME} of SERCOM module operating in SPI mode.
    This function should be called before any other library function. The SERCOM
    module will be configured as per the MHC settings.

  Remarks:
    Refer plib_${SERCOM_INSTANCE_NAME?lower_case}_spi.h file for more information.
*/

void ${SERCOM_INSTANCE_NAME}_SPI_Initialize(void)
{
<#if SPI_INTERRUPT_MODE = true>
    /* Instantiate the ${SERCOM_INSTANCE_NAME} SPI object */
    ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.callback = NULL ;
    ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.transferIsBusy = false ;
    ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.status = SPI_ERROR_NONE;
</#if>

    /* Reset the SPI module */
    ${SERCOM_INSTANCE_NAME}_REGS->SPI.CTRLA |= SERCOM_SPI_CTRLA_SWRST_Msk;

    while((${SERCOM_INSTANCE_NAME}_REGS->SPI.SYNCBUSY & SERCOM_SPI_SYNCBUSY_SWRST_Msk) == SERCOM_SPI_SYNCBUSY_SWRST_Msk)
    {
        /* Wait for Module to Reset */
    }

    /* Configure Immediate Buffer Overflow , Data Out Pin Out , Master Mode and
     * Data In and Pin Out
     */

    <@compress single_line=true>${SERCOM_INSTANCE_NAME}_REGS->SPI.CTRLA |= SERCOM_SPI_CTRLA_MODE(SPI_MASTER_MODE_VALUE)| SERCOM_SPI_CTRLA_DOPO(${SPI_DOPO}) |
                                                                           SERCOM_SPI_CTRLA_DIPO(${SPI_DIPO}) | SERCOM_SPI_CTRLA_IBON_Msk
                                                                           ${SPI_RUNSTDBY?then('| SERCOM_SPI_CTRLA_RUNSTDBY_Msk', '')};</@compress>

    /* Selection of the Clock Phase and Polarity */
    ${SERCOM_INSTANCE_NAME}_REGS->SPI.CTRLA |= SPI_TRANSFER_MODE;

    /* Selection of the Character Size and Receiver Enable */
    <@compress single_line=true>${SERCOM_INSTANCE_NAME}_REGS->SPI.CTRLB |= ${(SPI_CHARSIZE_BITS == "_9_BIT")?then('SERCOM_SPI_CTRLB_CHSIZE(0x1)', 'SERCOM_SPI_CTRLB_CHSIZE(0x0)')}
                                                                           ${SPI_RECIEVER_ENABLE?then('| SERCOM_SPI_CTRLB_RXEN_Msk', '')}
                                                                           ${SPI_MSSEN?then('| SERCOM_SPI_CTRLB_MSSEN_Msk', '')};</@compress>

    /* Selection of the Baud Value */
    ${SERCOM_INSTANCE_NAME}_REGS->SPI.BAUD = BAUD_VALUE;

    /* Clearing all the Interrupt Flags */
    ${SERCOM_INSTANCE_NAME}_REGS->SPI.INTFLAG = SERCOM_SPI_INTFLAG_Msk;

    /* Enable the SPI Module */
    ${SERCOM_INSTANCE_NAME}_REGS->SPI.CTRLA |= SERCOM_SPI_CTRLA_ENABLE_Msk;

    while((${SERCOM_INSTANCE_NAME}_REGS->SPI.SYNCBUSY & SERCOM_SPI_SYNCBUSY_ENABLE_Msk) == SERCOM_SPI_SYNCBUSY_ENABLE_Msk)
    {
        /* Wait for SPI Module to Enable */
    }
}

<#if SPI_TRANSFER_SETUP_ENABLE = true >
// *****************************************************************************
/* Function:
    bool ${SERCOM_INSTANCE_NAME}_SPI_TransferSetup(SPI_TRANSFER_SETUP *setup,
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
    Refer plib_${SERCOM_INSTANCE_NAME?lower_case}_spi.h file for more information.
*/

bool ${SERCOM_INSTANCE_NAME}_SPI_TransferSetup(SPI_TRANSFER_SETUP *setup, uint32_t spiSourceClock)
{
    uint32_t baudValue = 0;

    bool statusValue = false;

    if(spiSourceClock == 0)
    {
        /* Fetch Master Clock Frequency directly */
        spiSourceClock = CPU_FREQ;
    }

    /* Disable the SPI Module */
    ${SERCOM_INSTANCE_NAME}_REGS->SPI.CTRLA &= ~(SERCOM_SPI_CTRLA_ENABLE_Msk);

    while((${SERCOM_INSTANCE_NAME}_REGS->SPI.SYNCBUSY & SERCOM_SPI_SYNCBUSY_ENABLE_Msk) == SERCOM_SPI_SYNCBUSY_ENABLE_Msk)
    {
        /* Wait for SPI Module to Disable */
    }

    if ( setup != NULL )
    {
        baudValue = (spiSourceClock/(2*(setup->baudRate))) - 1;

        if ((baudValue > 0) & (baudValue <= 255))
        {
            /* Selection of the Clock Polarity */
            ${SERCOM_INSTANCE_NAME}_REGS->SPI.CTRLA |= (setup->clockPolarity) << SERCOM_SPI_CTRLA_CPOL_Pos;

            /* Selection of the Clock Phase */
            ${SERCOM_INSTANCE_NAME}_REGS->SPI.CTRLA |= (setup->clockPhase) << SERCOM_SPI_CTRLA_CPHA_Pos;

            /* Selection of the Baud Value */
            ${SERCOM_INSTANCE_NAME}_REGS->SPI.BAUD = baudValue ;

            /* Selection of the Character Size */
            ${SERCOM_INSTANCE_NAME}_REGS->SPI.CTRLB |= (setup->dataBits) << SERCOM_SPI_CTRLB_CHSIZE_Pos;

            statusValue = true;
        }
    }

    /* Enabling the SPI Module */
    ${SERCOM_INSTANCE_NAME}_REGS->SPI.CTRLA |= SERCOM_SPI_CTRLA_ENABLE_Msk;

    while((${SERCOM_INSTANCE_NAME}_REGS->SPI.SYNCBUSY & SERCOM_SPI_SYNCBUSY_ENABLE_Msk) == SERCOM_SPI_SYNCBUSY_ENABLE_Msk)
    {
        /* Wait for SPI Module to Enable */
    }

    return statusValue;
}
</#if>

<#if SPI_INTERRUPT_MODE = true>
// *****************************************************************************
/* Function:
    void ${SERCOM_INSTANCE_NAME}_SPI_CallbackRegister(const SERCOM_SPI_CALLBACK* callBack,
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
    Refer plib_${SERCOM_INSTANCE_NAME?lower_case}_spi.h file for more information.
*/

void ${SERCOM_INSTANCE_NAME}_SPI_CallbackRegister(SERCOM_SPI_CALLBACK callBack, uintptr_t context )
{
    ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.callback = callBack;

    ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.context = context;
}

// *****************************************************************************
/* Function:
    bool ${SERCOM_INSTANCE_NAME}_SPI_IsBusy(void);

  Summary:
    Returns transfer status of SERCOM ${SERCOM_INSTANCE_NAME}SPI.

  Description:
    This function ture if the SERCOM ${SERCOM_INSTANCE_NAME}SPI module is busy with a transfer. The
    application can use the function to check if SERCOM ${SERCOM_INSTANCE_NAME}SPI module is busy
    before calling any of the data transfer functions. The library does not
    allow a data transfer operation if another transfer operation is already in
    progress.

    This function can be used as an alternative to the callback function when
    the library is operating interrupt mode. The allow the application to
    implement a synchronous interface to the library.

  Remarks:
    Refer plib_${SERCOM_INSTANCE_NAME?lower_case}_spi.h file for more information.
*/

bool ${SERCOM_INSTANCE_NAME}_SPI_IsBusy(void)
{
    return ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.transferIsBusy;
}
</#if>

// *****************************************************************************
/* Function:
    bool ${SERCOM_INSTANCE_NAME}_SPI_WriteRead (void* pTransmitData, size_t txSize
                                        void* pReceiveData, size_t rxSize);

  Summary:
    Write and Read data on SERCOM ${SERCOM_INSTANCE_NAME} SPI peripheral.

  Description:
    This function transmits "txSize" number of bytes and receives "rxSize"
    number of bytes on SERCOM ${SERCOM_INSTANCE_NAME} SPI module. Data pointed by pTransmitData is
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
    registered prior to calling the ${SERCOM_INSTANCE_NAME}_SPI_WriteRead() function. The
    application can use the ${SERCOM_INSTANCE_NAME}_SPI_IsBusy() to poll for completion.

  Remarks:
    Refer plib_${SERCOM_INSTANCE_NAME?lower_case}_spi.h file for more information.
*/

<#if SPI_INTERRUPT_MODE == false >
bool ${SERCOM_INSTANCE_NAME}_SPI_WriteRead (void* pTransmitData, size_t txSize, void* pReceiveData, size_t rxSize)
{
    size_t txCount = 0;
    size_t rxCount = 0;
    size_t dummySize = 0;
    uint32_t dummyData = 0;
    size_t receivedData = 0;
    uint32_t dataBits = 0;
    bool isSuccess = false;

    /* Verify the request */
    if (((txSize >= 0) && (pTransmitData != NULL)) || ((rxSize >= 0) && (pReceiveData != NULL)))
    {
        dataBits = ${SERCOM_INSTANCE_NAME}_REGS->SPI.CTRLB & SERCOM_SPI_CTRLB_CHSIZE_Msk;

        /* Flush out any unread data in SPI DATA Register from the previous transfer */
        receivedData = ${SERCOM_INSTANCE_NAME}_REGS->SPI.DATA;

        if (rxSize > txSize )
        {
            dummySize = rxSize - txSize;
        }

        if (dataBits != SPI_DATA_BITS_8)
        {
            rxSize >>= 1;
            txSize >>= 1;
            dummySize >>= 1;
        }

        while ((txCount != txSize) || (dummySize != 0))
        {
            if (txCount != txSize)
            {
                if(dataBits == SPI_DATA_BITS_8)
                {
                    ${SERCOM_INSTANCE_NAME}_REGS->SPI.DATA = ((uint8_t*)pTransmitData)[txCount++];
                }
                else
                {
                    ${SERCOM_INSTANCE_NAME}_REGS->SPI.DATA = ((uint16_t*)pTransmitData)[txCount++] & SERCOM_SPI_DATA_Msk;
                }
            }
            else if (dummySize > 0)
            {
                if(dataBits == SPI_DATA_BITS_8)
                {
                    ${SERCOM_INSTANCE_NAME}_REGS->SPI.DATA = 0xFF;
                }
                else
                {
                    ${SERCOM_INSTANCE_NAME}_REGS->SPI.DATA = 0xFFFF & SERCOM_SPI_DATA_Msk;
                }

                dummySize--;
            }

            if (rxSize == 0)
            {
                while((${SERCOM_INSTANCE_NAME}_REGS->SPI.INTFLAG & SERCOM_SPI_INTFLAG_DRE_Msk) != SERCOM_SPI_INTFLAG_DRE_Msk);
                {
                    /* For transmit only request, wait for DRE to become empty */
                }

                /* Flush out any unread data in SPI DATA Register from the previous transfer */
                dummyData = ${SERCOM_INSTANCE_NAME}_REGS->SPI.DATA;
                (void)dummyData;
            }
            else
            {
                /* Checking for the Buffer OverFlow */
                if ((${SERCOM_INSTANCE_NAME}_REGS->SPI.STATUS & SERCOM_SPI_STATUS_BUFOVF_Msk) == SERCOM_SPI_STATUS_BUFOVF_Msk)
                {
                    if ((${SERCOM_INSTANCE_NAME}_REGS->SPI.INTFLAG & SERCOM_SPI_INTFLAG_RXC_Msk) == SERCOM_SPI_INTFLAG_RXC_Msk)
                        {
                            dummyData = ${SERCOM_INSTANCE_NAME}_REGS->SPI.DATA;
                            (void)dummyData;

                            ${SERCOM_INSTANCE_NAME}_REGS->SPI.STATUS = SERCOM_SPI_STATUS_BUFOVF_Msk;
                        }
                }
                else
                {
                    while((${SERCOM_INSTANCE_NAME}_REGS->SPI.INTFLAG & SERCOM_SPI_INTFLAG_RXC_Msk) != SERCOM_SPI_INTFLAG_RXC_Msk)
                    {
                        /* If data is read, wait for the Receiver Data Register to become full */
                    }

                    receivedData = ${SERCOM_INSTANCE_NAME}_REGS->SPI.DATA;

                    if (rxCount < rxSize)
                    {
                        if(dataBits == SPI_DATA_BITS_8)
                        {
                            ((uint8_t*)pReceiveData)[rxCount++] = receivedData;
                        }
                        else
                        {
                            ((uint16_t*)pReceiveData)[rxCount++] = receivedData & SERCOM_SPI_DATA_Msk;
                        }
                    }
                }
            }
        }

        isSuccess = true;
    }

    while ((${SERCOM_INSTANCE_NAME}_REGS->SPI.INTFLAG & SERCOM_SPI_INTFLAG_TXC_Msk) != SERCOM_SPI_INTFLAG_TXC_Msk)
    {
        /* Make sure no data is pending in the shift register */
    }

    return isSuccess;
}
<#else>
bool ${SERCOM_INSTANCE_NAME}_SPI_WriteRead (void* pTransmitData, size_t txSize, void* pReceiveData, size_t rxSize)
{
    bool isRequestAccepted = false;
    uint32_t dummyData = 0;
    uint32_t dataBits = 0;

    /* Verify the request */
    if((((txSize >= 0) && (pTransmitData != NULL)) || ((rxSize >= 0) && (pReceiveData != NULL))) && (${SERCOM_INSTANCE_NAME?lower_case}SPIObj.transferIsBusy == false))
    {
        isRequestAccepted = true;
        ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.txBuffer = pTransmitData;
        ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.rxBuffer = pReceiveData;
        ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.rxCount = 0;
        ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.txCount = 0;
        ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.dummySize = 0;
        ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.txSize = txSize;
        ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.rxSize = rxSize;
        ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.transferIsBusy = true;
        ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.status = SPI_ERROR_NONE;

        dataBits = ${SERCOM_INSTANCE_NAME}_REGS->SPI.CTRLB & SERCOM_SPI_CTRLB_CHSIZE_Msk;

        /* Flush out any unread data in SPI read buffer */
        dummyData = ${SERCOM_INSTANCE_NAME}_REGS->SPI.DATA;
        (void)dummyData;

        if (rxSize > txSize )
        {
            ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.dummySize = rxSize - txSize;
        }

        /* Start the first write here itself, rest will happen in ISR context */
        if(dataBits == SPI_DATA_BITS_8)
        {
            if (${SERCOM_INSTANCE_NAME?lower_case}SPIObj.txCount < ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.txSize)
            {
                ${SERCOM_INSTANCE_NAME}_REGS->SPI.DATA = *((uint8_t*)${SERCOM_INSTANCE_NAME?lower_case}SPIObj.txBuffer);
                ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.txCount++;
            }
            else if (${SERCOM_INSTANCE_NAME?lower_case}SPIObj.dummySize > 0)
            {
                ${SERCOM_INSTANCE_NAME}_REGS->SPI.DATA = 0xFF;
                ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.dummySize--;
            }
        }
        else
        {
            ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.txSize >>= 1;
            ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.dummySize >>= 1;
            ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.rxSize >>= 1;

            if (${SERCOM_INSTANCE_NAME?lower_case}SPIObj.txCount < ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.txSize)
            {
                ${SERCOM_INSTANCE_NAME}_REGS->SPI.DATA = *((uint16_t*)${SERCOM_INSTANCE_NAME?lower_case}SPIObj.txBuffer) & SERCOM_SPI_DATA_Msk;
                ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.txCount++;
            }
            else if (${SERCOM_INSTANCE_NAME?lower_case}SPIObj.dummySize > 0)
            {
                ${SERCOM_INSTANCE_NAME}_REGS->SPI.DATA = 0xFFFF & SERCOM_SPI_DATA_Msk;
                ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.dummySize--;
            }
        }

        if (rxSize > 0)
        {
            /* Enable the DataRegisterEmpty and ReceiveComplete flags */
            ${SERCOM_INSTANCE_NAME}_REGS->SPI.INTENSET = SERCOM_SPI_INTFLAG_DRE_Msk | SERCOM_SPI_INTFLAG_RXC_Msk;
        }
        else
        {
            /* Enable the DataRegisterEmpty  */
            ${SERCOM_INSTANCE_NAME}_REGS->SPI.INTENSET = SERCOM_SPI_INTFLAG_DRE_Msk;
        }
    }

    return isRequestAccepted;
}
</#if>

<#if SPI_INTERRUPT_MODE = true>
// *****************************************************************************
/* Function:
    void ${SERCOM_INSTANCE_NAME}_SPI_InterruptHandler(void);

  Summary:
    Handler that handles the SPI interrupts

  Description:
    This Function is called from the handler to handle the exchange based on the
    Interrupts.

  Remarks:
    Refer plib_${SERCOM_INSTANCE_NAME?lower_case}_spi.h file for more information.
*/

void ${SERCOM_INSTANCE_NAME}_SPI_InterruptHandler(void)
{
    uint32_t dataBits = 0;
    uint32_t receivedData = 0;
    uint32_t dummyData = 0;

    dataBits = ${SERCOM_INSTANCE_NAME}_REGS->SPI.CTRLB & SERCOM_SPI_CTRLB_CHSIZE_Msk;

    /* Save the SPI transfer status in global object before it gets cleared */
    ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.status = ${SERCOM_INSTANCE_NAME}_REGS->SPI.STATUS;

    /* Checking for the Buffer Overflow Status */
    if ((${SERCOM_INSTANCE_NAME}_REGS->SPI.STATUS & SERCOM_SPI_STATUS_BUFOVF_Msk) == SERCOM_SPI_STATUS_BUFOVF_Msk)
    {
        if ((${SERCOM_INSTANCE_NAME}_REGS->SPI.INTFLAG & SERCOM_SPI_INTFLAG_RXC_Msk) == SERCOM_SPI_INTFLAG_RXC_Msk)
        {
            dummyData = ${SERCOM_INSTANCE_NAME}_REGS->SPI.DATA;
            (void)dummyData;

            /* Clearing the Buffer OverFlow Status */
            ${SERCOM_INSTANCE_NAME}_REGS->SPI.STATUS = SERCOM_SPI_STATUS_BUFOVF_Msk;
        }
    }
    else
    {
        if ((${SERCOM_INSTANCE_NAME}_REGS->SPI.INTFLAG & SERCOM_SPI_INTFLAG_RXC_Msk) == SERCOM_SPI_INTFLAG_RXC_Msk)
        {
            receivedData =  ${SERCOM_INSTANCE_NAME}_REGS->SPI.DATA;

            if (${SERCOM_INSTANCE_NAME?lower_case}SPIObj.rxCount < ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.rxSize)
            {
                if(dataBits == SPI_DATA_BITS_8)
                {
                    ((uint8_t*)${SERCOM_INSTANCE_NAME?lower_case}SPIObj.rxBuffer)[${SERCOM_INSTANCE_NAME?lower_case}SPIObj.rxCount++] = receivedData;
                }
                else
                {
                    ((uint16_t*)${SERCOM_INSTANCE_NAME?lower_case}SPIObj.rxBuffer)[${SERCOM_INSTANCE_NAME?lower_case}SPIObj.rxCount++] = receivedData;
                }
            }
        }
    }

    /* If there are more words to be transmitted, then transmit them here and keep track of the count */
    if((${SERCOM_INSTANCE_NAME}_REGS->SPI.INTFLAG & SERCOM_SPI_INTFLAG_TXC_Msk) == SERCOM_SPI_INTFLAG_TXC_Msk)
    {
        if(dataBits == SPI_DATA_BITS_8)
        {
            if (${SERCOM_INSTANCE_NAME?lower_case}SPIObj.txCount < ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.txSize)
            {
                ${SERCOM_INSTANCE_NAME}_REGS->SPI.DATA = ((uint8_t*)${SERCOM_INSTANCE_NAME?lower_case}SPIObj.txBuffer)[${SERCOM_INSTANCE_NAME?lower_case}SPIObj.txCount++];
            }
            else if (${SERCOM_INSTANCE_NAME?lower_case}SPIObj.dummySize > 0)
            {
                ${SERCOM_INSTANCE_NAME}_REGS->SPI.DATA = 0xFF;
                ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.dummySize--;
            }
        }
        else
        {
            if (${SERCOM_INSTANCE_NAME?lower_case}SPIObj.txCount < ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.txSize)
            {
                ${SERCOM_INSTANCE_NAME}_REGS->SPI.DATA = ((uint16_t*)${SERCOM_INSTANCE_NAME?lower_case}SPIObj.txBuffer)[${SERCOM_INSTANCE_NAME?lower_case}SPIObj.txCount++];
            }
            else if (${SERCOM_INSTANCE_NAME?lower_case}SPIObj.dummySize > 0)
            {
                ${SERCOM_INSTANCE_NAME}_REGS->SPI.DATA = 0xFFFF;
                ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.dummySize--;
            }
        }

        if ((${SERCOM_INSTANCE_NAME?lower_case}SPIObj.txCount == ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.txSize) && (0 == ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.dummySize))
        {
            /* Disable the Data Register empty interrupt  */
            ${SERCOM_INSTANCE_NAME}_REGS->SPI.INTENCLR = SERCOM_SPI_INTENCLR_DRE_Msk;

            /* Enabling the Transmit complete Interrupt flag to ensure that
             *  there is no more Data present in the shift register
             */
            ${SERCOM_INSTANCE_NAME}_REGS->SPI.INTENSET = SERCOM_SPI_INTENSET_TXC_Msk;
        }
    }

    if((${SERCOM_INSTANCE_NAME}_REGS->SPI.INTFLAG & SERCOM_SPI_INTFLAG_TXC_Msk) == SERCOM_SPI_INTFLAG_TXC_Msk)
    {
        if (${SERCOM_INSTANCE_NAME?lower_case}SPIObj.rxCount == ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.rxSize)
        {
            ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.transferIsBusy = false;

            /* Disable the Data Register empty and Receive Complete Interrupt flags */
            ${SERCOM_INSTANCE_NAME}_REGS->SPI.INTENCLR &= SERCOM_SPI_INTENCLR_DRE_Msk | SERCOM_SPI_INTENCLR_RXC_Msk | SERCOM_SPI_INTENSET_TXC_Msk;

            /* Flush out any pending ${SERCOM_INSTANCE_NAME} SPI IRQ with NVIC */
            NVIC_ClearPendingIRQ(${SERCOM_INSTANCE_NAME}_IRQn);

            /* If it was only transmit, then ignore receiver overflow error, if any */
            if(${SERCOM_INSTANCE_NAME?lower_case}SPIObj.rxSize == 0)
            {
                ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.status = SPI_ERROR_NONE;
            }

            if(${SERCOM_INSTANCE_NAME?lower_case}SPIObj.callback != NULL)
            {
                ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.callback(${SERCOM_INSTANCE_NAME?lower_case}SPIObj.context);
            }
        }
    }
}

// *****************************************************************************
/* Function:
    SPI_ERROR ${SERCOM_INSTANCE_NAME}_SPI_ErrorGet( void )

  Summary:
    Gets the error of the given SPI peripheral instance.

  Description:
    This function returns the errors associated with the given SPI peripheral
    instance. After reading the error, if any, they will be cleared.

   Remarks:
    Refer plib_${SERCOM_INSTANCE_NAME?lower_case}_spi.h file for more information.
*/

SPI_ERROR ${SERCOM_INSTANCE_NAME}_SPI_ErrorGet(void)
{
    SPI_ERROR statusValue = SPI_ERROR_NONE;

    /* Checking for the Buffer overflow Status */
    if((${SERCOM_INSTANCE_NAME}_REGS->SPI.STATUS & SERCOM_SPI_STATUS_BUFOVF_Msk) == SERCOM_SPI_STATUS_BUFOVF_Msk)
    {
        statusValue = SPI_ERROR_OVERFLOW;
    }

    return statusValue;
}
</#if>

