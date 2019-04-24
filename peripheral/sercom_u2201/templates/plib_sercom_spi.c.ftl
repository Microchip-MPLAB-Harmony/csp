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

#include "plib_${SERCOM_INSTANCE_NAME?lower_case}_spi.h"

// *****************************************************************************
// *****************************************************************************
// Section: MACROS Definitions
// *****************************************************************************
// *****************************************************************************

<#assign SPI_PLIB = "SERCOM_INSTANCE_NAME">
<#assign SPI_PLIB_CLOCK_FREQUENCY = "core." + SPI_PLIB?eval + "_CORE_CLOCK_FREQUENCY">

/* ${SERCOM_INSTANCE_NAME} clk freq value for the baud calculation */
<#if SPI_PLIB_CLOCK_FREQUENCY?eval??>
    <#lt>#define ${SERCOM_INSTANCE_NAME}_Frequency      (uint32_t) (${SPI_PLIB_CLOCK_FREQUENCY?eval}UL)
<#else>
    <#lt>#define ${SERCOM_INSTANCE_NAME}_Frequency      0
</#if>

/* ${SERCOM_INSTANCE_NAME} SPI baud value for ${SPI_BAUD_RATE} Hz baud rate */
#define ${SERCOM_INSTANCE_NAME}_SPIM_BAUD_VALUE         (${SPI_BAUD_REG_VALUE}U)

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
</#if>

    /* Selection of the Character Size and Receiver Enable */
    <@compress single_line=true>${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_CTRLB = SERCOM_SPIM_CTRLB_CHSIZE_${SPI_CHARSIZE_BITS}
                                                                                  ${SPI_RECIEVER_ENABLE?then('| SERCOM_SPIM_CTRLB_RXEN_Msk', '')}
                                                                                  <#if (SPI_MSSEN??) && (SPI_MSSEN = true)> | SERCOM_SPIM_CTRLB_MSSEN_Msk</#if>;</@compress>

    /* Wait for synchronization */
    <#if SERCOM_SYNCBUSY = false>
    while((${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_STATUS & SERCOM_SPIM_STATUS_SYNCBUSY_Msk) & SERCOM_SPIM_STATUS_SYNCBUSY_Msk);
    <#else>
    while(${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_SYNCBUSY);
    </#if>

    /* Selection of the Baud Value */
    ${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_BAUD = SERCOM_SPIM_BAUD_BAUD(${SERCOM_INSTANCE_NAME}_SPIM_BAUD_VALUE);

    /* Configure Data Out Pin Out , Master Mode,
     * Data In and Pin Out,Data Order and Standby mode if configured
     * and Selection of the Clock Phase and Polarity and Enable the SPI Module
     */
    <@compress single_line=true>${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_CTRLA = SERCOM_SPIM_CTRLA_MODE_SPI_MASTER |
                                                                                  SERCOM_SPIM_CTRLA_DOPO_${SPI_DOPO} |
                                                                                  SERCOM_SPIM_CTRLA_DIPO_${SPI_DIPO} |
                                                                                  SERCOM_SPIM_CTRLA_CPOL_${SPI_CLOCK_POLARITY} |
                                                                                  SERCOM_SPIM_CTRLA_CPHA_${SPI_CLOCK_PHASE} |
                                                                                  SERCOM_SPIM_CTRLA_DORD_${SPI_DATA_ORDER} |
                                                                                  SERCOM_SPIM_CTRLA_ENABLE_Msk
                                                                                  ${SPI_RUNSTDBY?then(' | SERCOM_SPIM_CTRLA_RUNSTDBY_Msk', '')};</@compress>

    /* Wait for synchronization */
    <#if SERCOM_SYNCBUSY = false>
    while((${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_STATUS & SERCOM_SPIM_STATUS_SYNCBUSY_Msk) & SERCOM_SPIM_STATUS_SYNCBUSY_Msk);
    <#else>
    while(${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_SYNCBUSY);
    </#if>
}

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
        spiSourceClock = ${SERCOM_INSTANCE_NAME}_Frequency;
    }

    /* Disable the SPI Module */
    ${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_CTRLA &= ~(SERCOM_SPIM_CTRLA_ENABLE_Msk);

    /* Wait for synchronization */
    <#if SERCOM_SYNCBUSY = false>
    while((${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_STATUS & SERCOM_SPIM_STATUS_SYNCBUSY_Msk) & SERCOM_SPIM_STATUS_SYNCBUSY_Msk);
    <#else>
    while(${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_SYNCBUSY);
    </#if>

    if(setup != NULL)
    {
        baudValue = (spiSourceClock/(2*(setup->clockFrequency))) - 1;

        if((baudValue > 0) & (baudValue <= 255))
        {
            /* Selection of the Clock Polarity and Clock Phase */
            ${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_CTRLA |= setup->clockPolarity | setup->clockPhase;

            /* Selection of the Baud Value */
            ${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_BAUD = baudValue;

            /* Selection of the Character Size */
            ${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_CTRLB |= setup->dataBits;

            /* Wait for synchronization */
            <#if SERCOM_SYNCBUSY = false>
            while((${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_STATUS & SERCOM_SPIM_STATUS_SYNCBUSY_Msk) & SERCOM_SPIM_STATUS_SYNCBUSY_Msk);
            <#else>
            while(${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_SYNCBUSY);
            </#if>

            statusValue = true;
        }
    }

    /* Enabling the SPI Module */
    ${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_CTRLA |= SERCOM_SPIM_CTRLA_ENABLE_Msk;

    /* Wait for synchronization */
    <#if SERCOM_SYNCBUSY = false>
    while((${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_STATUS & SERCOM_SPIM_STATUS_SYNCBUSY_Msk) & SERCOM_SPIM_STATUS_SYNCBUSY_Msk);
    <#else>
    while(${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_SYNCBUSY);
    </#if>

    return statusValue;
}


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
    size_t receivedData;
    uint32_t dataBits;
    bool isSuccess = false;

    /* Verify the request */
    if(((txSize > 0) && (pTransmitData != NULL)) || ((rxSize > 0) && (pReceiveData != NULL)))
    {
        dataBits = ${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_CTRLB & SERCOM_SPIM_CTRLB_CHSIZE_Msk;

        if(dataBits != SPI_DATA_BITS_8)
        {
            /* For 9-bit transmission, the txSize and rxSize must be an even number. */
            if(((txSize > 0) && (txSize & 0x01)) || ((rxSize > 0) && (rxSize & 0x01)))
            {
                return isSuccess;
            }
        }

        if(pTransmitData == NULL)
        {
            txSize = 0;
        }

        if(pReceiveData == NULL)
        {
            rxSize = 0;
        }

        /* Flush out any unread data in SPI DATA Register from the previous transfer */
        while(${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_INTFLAG & SERCOM_SPIM_INTFLAG_RXC_Msk)
        {
            receivedData = ${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_DATA;
        }

        ${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_STATUS |= SERCOM_SPIM_STATUS_BUFOVF_Msk;

        <#if SPI_INTENSET_ERROR = true>
        ${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_INTFLAG |= SERCOM_SPIM_INTFLAG_ERROR_Msk;

        </#if>
        if(rxSize > txSize)
        {
            dummySize = rxSize - txSize;
        }

        if(dataBits != SPI_DATA_BITS_8)
        {
            rxSize >>= 1;
            txSize >>= 1;
            dummySize >>= 1;
        }

        /* Make sure DRE is empty */
        while((${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_INTFLAG & SERCOM_SPIM_INTFLAG_DRE_Msk) != SERCOM_SPIM_INTFLAG_DRE_Msk);

        while((txCount != txSize) || (dummySize != 0))
        {
            if(txCount != txSize)
            {
                if(dataBits == SPI_DATA_BITS_8)
                {
                    ${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_DATA = ((uint8_t*)pTransmitData)[txCount++];
                }
                else
                {
                    ${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_DATA = ((uint16_t*)pTransmitData)[txCount++] & SERCOM_SPIM_DATA_Msk;
                }
            }
            else if(dummySize > 0)
            {
                if(dataBits == SPI_DATA_BITS_8)
                {
                    ${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_DATA = 0xFF;
                }
                else
                {
                    ${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_DATA = 0xFFFF & SERCOM_SPIM_DATA_Msk;
                }

                dummySize--;
            }

            if(rxSize == 0)
            {
                /* For transmit only request, wait for DRE to become empty */
                while((${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_INTFLAG & SERCOM_SPIM_INTFLAG_DRE_Msk) != SERCOM_SPIM_INTFLAG_DRE_Msk);
            }
            else
            {
                /* If data is read, wait for the Receiver Data Register to become full */
                while((${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_INTFLAG & SERCOM_SPIM_INTFLAG_RXC_Msk) != SERCOM_SPIM_INTFLAG_RXC_Msk);

                receivedData = ${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_DATA;

                if(rxCount < rxSize)
                {
                    if(dataBits == SPI_DATA_BITS_8)
                    {
                        ((uint8_t*)pReceiveData)[rxCount++] = receivedData;
                    }
                    else
                    {
                        ((uint16_t*)pReceiveData)[rxCount++] = receivedData & SERCOM_SPIM_DATA_Msk;
                    }
                }
            }
        }

        /* Make sure no data is pending in the shift register */
        while((${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_INTFLAG & SERCOM_SPIM_INTFLAG_TXC_Msk) != SERCOM_SPIM_INTFLAG_TXC_Msk);

        isSuccess = true;
    }

    return isSuccess;
}
<#else>
bool ${SERCOM_INSTANCE_NAME}_SPI_WriteRead (void* pTransmitData, size_t txSize, void* pReceiveData, size_t rxSize)
{
    bool isRequestAccepted = false;
    uint32_t dummyData = 0;

    /* Verify the request */
    if((((txSize > 0) && (pTransmitData != NULL)) || ((rxSize > 0) && (pReceiveData != NULL))) && (${SERCOM_INSTANCE_NAME?lower_case}SPIObj.transferIsBusy == false))
    {
        if((${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_CTRLB & SERCOM_SPIM_CTRLB_CHSIZE_Msk) == SPI_DATA_BITS_9)
        {
            /* For 9-bit transmission, the txSize and rxSize must be an even number. */
            if(((txSize > 0) && (txSize & 0x01)) || ((rxSize > 0) && (rxSize & 0x01)))
            {
                return isRequestAccepted;
            }
        }

        isRequestAccepted = true;
        ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.txBuffer = pTransmitData;
        ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.rxBuffer = pReceiveData;
        ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.rxCount = 0;
        ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.txCount = 0;
        ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.dummySize = 0;

        if(pTransmitData != NULL)
        {
            ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.txSize = txSize;
        }
        else
        {
            ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.txSize = 0;
        }

        if(pReceiveData != NULL)
        {
            ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.rxSize = rxSize;
        }
        else
        {
            ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.rxSize = 0;
        }

        ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.transferIsBusy = true;

        /* Flush out any unread data in SPI read buffer */
        while(${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_INTFLAG & SERCOM_SPIM_INTFLAG_RXC_Msk)
        {
            dummyData = ${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_DATA;
            (void)dummyData;
        }

        ${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_STATUS |= SERCOM_SPIM_STATUS_BUFOVF_Msk;

        <#if SPI_INTENSET_ERROR = true>
        ${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_INTFLAG |= SERCOM_SPIM_INTFLAG_ERROR_Msk;

        </#if>
        if(${SERCOM_INSTANCE_NAME?lower_case}SPIObj.rxSize > ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.txSize)
        {
            ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.dummySize = ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.rxSize - ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.txSize;
        }

        /* Start the first write here itself, rest will happen in ISR context */
        if((${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_CTRLB & SERCOM_SPIM_CTRLB_CHSIZE_Msk) == SPI_DATA_BITS_8)
        {
            if(${SERCOM_INSTANCE_NAME?lower_case}SPIObj.txCount < ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.txSize)
            {
                ${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_DATA = *((uint8_t*)${SERCOM_INSTANCE_NAME?lower_case}SPIObj.txBuffer);

                ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.txCount++;
            }
            else if(${SERCOM_INSTANCE_NAME?lower_case}SPIObj.dummySize > 0)
            {
                ${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_DATA = 0xFF;

                ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.dummySize--;
            }
        }
        else
        {
            ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.txSize >>= 1;
            ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.dummySize >>= 1;
            ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.rxSize >>= 1;

            if(${SERCOM_INSTANCE_NAME?lower_case}SPIObj.txCount < ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.txSize)
            {
                ${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_DATA = *((uint16_t*)${SERCOM_INSTANCE_NAME?lower_case}SPIObj.txBuffer) & SERCOM_SPIM_DATA_Msk;

                ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.txCount++;
            }
            else if(${SERCOM_INSTANCE_NAME?lower_case}SPIObj.dummySize > 0)
            {
                ${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_DATA = 0xFFFF & SERCOM_SPIM_DATA_Msk;

                ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.dummySize--;
            }
        }

        if(rxSize > 0)
        {
            /* Enable ReceiveComplete  */
            ${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_INTENSET = SERCOM_SPIM_INTENSET_RXC_Msk;
        }
        else
        {
            /* Enable the DataRegisterEmpty  */
            ${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_INTENSET = SERCOM_SPIM_INTENSET_DRE_Msk;
        }
    }

    return isRequestAccepted;
}
</#if>

bool ${SERCOM_INSTANCE_NAME}_SPI_Write(void* pTransmitData, size_t txSize)
{
    return ${SERCOM_INSTANCE_NAME}_SPI_WriteRead(pTransmitData, txSize, NULL, 0);
}

bool ${SERCOM_INSTANCE_NAME}_SPI_Read(void* pReceiveData, size_t rxSize)
{
    return ${SERCOM_INSTANCE_NAME}_SPI_WriteRead(NULL, 0, pReceiveData, rxSize);
}

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
    static bool isLastByteTransferInProgress = false;

    if(${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_INTENSET != 0)
    {
        dataBits = ${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_CTRLB & SERCOM_SPIM_CTRLB_CHSIZE_Msk;

        if((${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_INTFLAG & SERCOM_SPIM_INTFLAG_RXC_Msk) == SERCOM_SPIM_INTFLAG_RXC_Msk)
        {
            receivedData =  ${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_DATA;

            if(${SERCOM_INSTANCE_NAME?lower_case}SPIObj.rxCount < ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.rxSize)
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

        /* If there are more words to be transmitted, then transmit them here and keep track of the count */
        if((${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_INTFLAG & SERCOM_SPIM_INTFLAG_DRE_Msk) == SERCOM_SPIM_INTFLAG_DRE_Msk)
        {
            /* Disable the DRE interrupt. This will be enabled back if more than
             * one byte is pending to be transmitted */
            ${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_INTENCLR = SERCOM_SPIM_INTENCLR_DRE_Msk;

            if(dataBits == SPI_DATA_BITS_8)
            {
                if(${SERCOM_INSTANCE_NAME?lower_case}SPIObj.txCount < ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.txSize)
                {
                    ${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_DATA = ((uint8_t*)${SERCOM_INSTANCE_NAME?lower_case}SPIObj.txBuffer)[${SERCOM_INSTANCE_NAME?lower_case}SPIObj.txCount++];
                }
                else if(${SERCOM_INSTANCE_NAME?lower_case}SPIObj.dummySize > 0)
                {
                    ${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_DATA = 0xFF;

                    ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.dummySize--;
                }
            }
            else
            {
                if(${SERCOM_INSTANCE_NAME?lower_case}SPIObj.txCount < ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.txSize)
                {
                    ${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_DATA = ((uint16_t*)${SERCOM_INSTANCE_NAME?lower_case}SPIObj.txBuffer)[${SERCOM_INSTANCE_NAME?lower_case}SPIObj.txCount++];
                }
                else if(${SERCOM_INSTANCE_NAME?lower_case}SPIObj.dummySize > 0)
                {
                    ${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_DATA = 0xFFFF;

                    ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.dummySize--;
                }
            }

            if((${SERCOM_INSTANCE_NAME?lower_case}SPIObj.txCount == ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.txSize) && (${SERCOM_INSTANCE_NAME?lower_case}SPIObj.dummySize == 0))
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
            else if(${SERCOM_INSTANCE_NAME?lower_case}SPIObj.rxCount == ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.rxSize)
            {
                ${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_INTENSET = SERCOM_SPIM_INTENSET_DRE_Msk;

                ${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_INTENCLR = SERCOM_SPIM_INTENCLR_RXC_Msk;
            }
        }

        if(((${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_INTFLAG & SERCOM_SPIM_INTFLAG_TXC_Msk) == SERCOM_SPIM_INTFLAG_TXC_Msk) && (isLastByteTransferInProgress == true))
        {
            if(${SERCOM_INSTANCE_NAME?lower_case}SPIObj.rxCount == ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.rxSize)
            {
                ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.transferIsBusy = false;

                /* Disable the Data Register empty and Receive Complete Interrupt flags */
                ${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_INTENCLR = SERCOM_SPIM_INTENCLR_DRE_Msk | SERCOM_SPIM_INTENCLR_RXC_Msk | SERCOM_SPIM_INTENSET_TXC_Msk;

                isLastByteTransferInProgress = false;

                if(${SERCOM_INSTANCE_NAME?lower_case}SPIObj.callback != NULL)
                {
                    ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.callback(${SERCOM_INSTANCE_NAME?lower_case}SPIObj.context);
                }
            }
        }

        if(isLastByteTransferInProgress == true)
        {
            /* For the last byte transfer, the DRE interrupt is already disabled.
             * Enable TXC interrupt to ensure no data is present in the shift
             * register before application callback is called.
             */
            ${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_INTENSET = SERCOM_SPIM_INTENSET_TXC_Msk;
        }
    }
}
</#if>
