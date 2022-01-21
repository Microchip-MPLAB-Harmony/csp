/*******************************************************************************
  SERIAL COMMUNICATION SERIAL PERIPHERAL INTERFACE(${SERCOM_INSTANCE_NAME}_SPI) PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_${SERCOM_INSTANCE_NAME?lower_case}_spi_master.c

  Summary
    ${SERCOM_INSTANCE_NAME}_SPI Master PLIB Implementation File.

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

<#if core.CoreSysIntFile == true>
#include "interrupts.h"
</#if>
#include "plib_${SERCOM_INSTANCE_NAME?lower_case}_spi_master.h"

// *****************************************************************************
// *****************************************************************************
// Section: MACROS Definitions
// *****************************************************************************
// *****************************************************************************

<#assign SPI_PLIB = "SERCOM_INSTANCE_NAME">
<#assign SPI_PLIB_CLOCK_FREQUENCY = "core." + SPI_PLIB?eval + "_CORE_CLOCK_FREQUENCY">

/* ${SERCOM_INSTANCE_NAME} clk freq value for the baud calculation */
<#if SPI_PLIB_CLOCK_FREQUENCY?eval??>
    <#lt>#define ${SERCOM_INSTANCE_NAME}_Frequency      (${SPI_PLIB_CLOCK_FREQUENCY?eval}UL)
<#else>
    <#lt>#define ${SERCOM_INSTANCE_NAME}_Frequency      0U
</#if>

/* ${SERCOM_INSTANCE_NAME} SPI baud value for ${SPI_BAUD_RATE} Hz baud rate */
#define ${SERCOM_INSTANCE_NAME}_SPIM_BAUD_VALUE         (${SPI_BAUD_REG_VALUE}UL)

<#if SPI_INTERRUPT_MODE = true>
/*Global object to save SPI Exchange related data  */
static SPI_OBJECT ${SERCOM_INSTANCE_NAME?lower_case}SPIObj;
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
    ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.txSize = 0U;
    ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.rxSize = 0U;
</#if>

    /* Selection of the Character Size and Receiver Enable */
    <@compress single_line=true>${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_CTRLB = SERCOM_SPIM_CTRLB_CHSIZE_${SPI_CHARSIZE_BITS}
                                                                                  ${SPI_RECIEVER_ENABLE?then('| SERCOM_SPIM_CTRLB_RXEN_Msk', '')}
                                                                                  <#if (SPI_MSSEN??) && (SPI_MSSEN = true)> | SERCOM_SPIM_CTRLB_MSSEN_Msk</#if>;</@compress>

    /* Wait for synchronization */
    <#if SERCOM_SYNCBUSY = false>
    while((${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_STATUS & (uint16_t)SERCOM_SPIM_STATUS_SYNCBUSY_Msk) == (uint16_t)SERCOM_SPIM_STATUS_SYNCBUSY_Msk)
    {
        /* Do nothing */
    }
    <#else>
    while((${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_SYNCBUSY) != 0U)
    {
        /* Do nothing */
    }
    </#if>

    /* Selection of the Baud Value */
    ${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_BAUD = (uint8_t)SERCOM_SPIM_BAUD_BAUD(${SERCOM_INSTANCE_NAME}_SPIM_BAUD_VALUE);

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
    while((${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_STATUS & (uint16_t)SERCOM_SPIM_STATUS_SYNCBUSY_Msk) == (uint16_t)SERCOM_SPIM_STATUS_SYNCBUSY_Msk)
    {
        /* Do nothing */
    }
    <#else>
    while((${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_SYNCBUSY) != 0U)
    {
        /* Do nothing */
    }
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
    uint32_t baudValue = 0U;

    bool statusValue = false;

    if(spiSourceClock == 0U)
    {
        /* Fetch Master Clock Frequency directly */
        spiSourceClock = ${SERCOM_INSTANCE_NAME}_Frequency;
    }

    /* Disable the SPI Module */
    ${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_CTRLA &= ~(SERCOM_SPIM_CTRLA_ENABLE_Msk);

    /* Wait for synchronization */
    <#if SERCOM_SYNCBUSY = false>
    while((${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_STATUS & (uint16_t)SERCOM_SPIM_STATUS_SYNCBUSY_Msk) == (uint16_t)SERCOM_SPIM_STATUS_SYNCBUSY_Msk)
    {
        /* Do nothing */
    }
    <#else>
    while((${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_SYNCBUSY) != 0U)
    {
        /* Do nothing */
    }
    </#if>

    if(setup != NULL)
    {
        baudValue = (spiSourceClock/(2U*(setup->clockFrequency))) - 1U;

        if((baudValue > 0U) && (baudValue <= 255U))
        {
            /* Selection of the Clock Polarity and Clock Phase */
            ${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_CTRLA &= ~(SERCOM_SPIM_CTRLA_CPOL_Msk | SERCOM_SPIM_CTRLA_CPHA_Msk);
            ${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_CTRLA |= (uint32_t)setup->clockPolarity | (uint32_t)setup->clockPhase;

            /* Selection of the Baud Value */
            ${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_BAUD = (uint8_t)baudValue;

            /* Selection of the Character Size */
            ${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_CTRLB &= ~SERCOM_SPIM_CTRLB_CHSIZE_Msk;
            ${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_CTRLB |= (uint32_t)setup->dataBits;

            /* Wait for synchronization */
            <#if SERCOM_SYNCBUSY = false>
            while((${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_STATUS & (uint16_t)SERCOM_SPIM_STATUS_SYNCBUSY_Msk) == (uint16_t)SERCOM_SPIM_STATUS_SYNCBUSY_Msk)
            {
                /* Do nothing */
            }
            <#else>
            while((${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_SYNCBUSY) != 0U)
            {
                /* Do nothing */
            }
            </#if>

            statusValue = true;
        }
    }

    /* Enabling the SPI Module */
    ${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_CTRLA |= SERCOM_SPIM_CTRLA_ENABLE_Msk;

    /* Wait for synchronization */
    <#if SERCOM_SYNCBUSY = false>
    while((${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_STATUS & (uint16_t)SERCOM_SPIM_STATUS_SYNCBUSY_Msk) == (uint16_t)SERCOM_SPIM_STATUS_SYNCBUSY_Msk)
    {
        /* Do nothing */
    }
    <#else>
    while((${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_SYNCBUSY) != 0U)
    {
        /* Do nothing */
    }
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
    bool isBusy = false;
	if ((${SERCOM_INSTANCE_NAME?lower_case}SPIObj.txSize == 0U) && (${SERCOM_INSTANCE_NAME?lower_case}SPIObj.rxSize == 0U))
	{
		/* This means no transfer has been requested yet; hence SPI is not busy. */
		isBusy = false;
	}
	else
	{
        /* if transmit is not complete or if the state flag is not set, SPI is busy */
        isBusy = (((${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_INTFLAG & SERCOM_SPIM_INTFLAG_TXC_Msk) == 0U) || ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.transferIsBusy);
	}
    return isBusy;
}
</#if>

bool ${SERCOM_INSTANCE_NAME}_SPI_IsTransmitterBusy(void)
{
    return ((${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_INTFLAG & SERCOM_SPIM_INTFLAG_TXC_Msk) == 0U)? true : false;
}

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
    size_t txCount = 0U;
    size_t rxCount = 0U;
    size_t dummySize = 0U;
    size_t receivedData;
    uint32_t dataBits;
    bool isSuccess = false;

    /* Verify the request */
    if(((txSize > 0U) && (pTransmitData != NULL)) || ((rxSize > 0U) && (pReceiveData != NULL)))
    {
        dataBits = ${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_CTRLB & SERCOM_SPIM_CTRLB_CHSIZE_Msk;

        if(dataBits != (uint32_t)SPI_DATA_BITS_8)
        {
            /* For 9-bit transmission, the txSize and rxSize must be an even number. */
            if(((txSize > 0U) && ((txSize & 0x01U) != 0U)) || ((rxSize > 0U) && ((rxSize & 0x01U) != 0U)))
            {
                return isSuccess;
            }
        }

        if(pTransmitData == NULL)
        {
            txSize = 0U;
        }

        if(pReceiveData == NULL)
        {
            rxSize = 0U;
        }

        /* Flush out any unread data in SPI DATA Register from the previous transfer */
        while((${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_INTFLAG & SERCOM_SPIM_INTFLAG_RXC_Msk) == SERCOM_SPIM_INTFLAG_RXC_Msk)
        {
            receivedData = ${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_DATA;
        }

        ${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_STATUS |= (uint16_t)SERCOM_SPIM_STATUS_BUFOVF_Msk;

        <#if SPI_INTENSET_ERROR = true>
        ${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_INTFLAG |= (uint8_t)SERCOM_SPIM_INTFLAG_ERROR_Msk;

        </#if>
        if(rxSize > txSize)
        {
            dummySize = rxSize - txSize;
        }

        if(dataBits != (uint32_t)SPI_DATA_BITS_8)
        {
            rxSize >>= 1U;
            txSize >>= 1U;
            dummySize >>= 1U;
        }

        /* Make sure DRE is empty */
        while((${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_INTFLAG & SERCOM_SPIM_INTFLAG_DRE_Msk) != SERCOM_SPIM_INTFLAG_DRE_Msk)
        {
            /* Do nothing */
        }

        while((txCount != txSize) || (dummySize != 0U))
        {
            if(txCount != txSize)
            {
                if(dataBits == (uint32_t)SPI_DATA_BITS_8)
                {
                    ${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_DATA = ((uint8_t*)pTransmitData)[txCount];
					txCount++;
                }
                else
                {
                    ${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_DATA = ((uint16_t*)pTransmitData)[txCount] & SERCOM_SPIM_DATA_Msk;
					txCount++;
                }
            }
            else if(dummySize > 0U)
            {
                if(dataBits == (uint32_t)SPI_DATA_BITS_8)
                {
                    ${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_DATA = 0xFFU;
                }
                else
                {
                    ${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_DATA = 0xFFFFU & SERCOM_SPIM_DATA_Msk;
                }

                dummySize--;
            }
            else
            {
                /* Do nothing */
            }

            if(rxSize == 0U)
            {
                /* For transmit only request, wait for DRE to become empty */
                while((${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_INTFLAG & SERCOM_SPIM_INTFLAG_DRE_Msk) != SERCOM_SPIM_INTFLAG_DRE_Msk)
                {
                    /* Do nothing */
                }
            }
            else
            {
                /* If data is read, wait for the Receiver Data Register to become full */
                while((${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_INTFLAG & SERCOM_SPIM_INTFLAG_RXC_Msk) != SERCOM_SPIM_INTFLAG_RXC_Msk)
                {
                    /* Do nothing */
                }

                receivedData = ${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_DATA;

                if(rxCount < rxSize)
                {
                    if(dataBits == (uint32_t)SPI_DATA_BITS_8)
                    {
                        ((uint8_t*)pReceiveData)[rxCount++] = (uint8_t)receivedData;
                    }
                    else
                    {
                        ((uint16_t*)pReceiveData)[rxCount++] = (uint16_t)(receivedData & SERCOM_SPIM_DATA_Msk);
                    }
                }
            }
        }

        /* Make sure no data is pending in the shift register */
        while((${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_INTFLAG & SERCOM_SPIM_INTFLAG_TXC_Msk) != SERCOM_SPIM_INTFLAG_TXC_Msk)
        {
            /* Do nothing */
        }

        isSuccess = true;
    }

    return isSuccess;
}
<#else>
bool ${SERCOM_INSTANCE_NAME}_SPI_WriteRead (void* pTransmitData, size_t txSize, void* pReceiveData, size_t rxSize)
{
    bool isRequestAccepted = false;
    uint32_t dummyData = 0U;

    /* Verify the request */
    if((((txSize > 0U) && (pTransmitData != NULL)) || ((rxSize > 0U) && (pReceiveData != NULL))) && (${SERCOM_INSTANCE_NAME?lower_case}SPIObj.transferIsBusy == false))
    {
        if((${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_CTRLB & SERCOM_SPIM_CTRLB_CHSIZE_Msk) == (uint32_t)SPI_DATA_BITS_9)
        {
            /* For 9-bit transmission, the txSize and rxSize must be an even number. */
            if(((txSize > 0U) && ((txSize & 0x01U) != 0U)) || ((rxSize > 0U) && ((rxSize & 0x01U) != 0U)))
            {
                return isRequestAccepted;
            }
        }

        isRequestAccepted = true;
        ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.txBuffer = pTransmitData;
        ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.rxBuffer = pReceiveData;
        ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.rxCount = 0U;
        ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.txCount = 0U;
        ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.dummySize = 0U;

        if(pTransmitData != NULL)
        {
            ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.txSize = txSize;
        }
        else
        {
            ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.txSize = 0U;
        }

        if(pReceiveData != NULL)
        {
            ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.rxSize = rxSize;
        }
        else
        {
            ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.rxSize = 0U;
        }

        ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.transferIsBusy = true;

        /* Flush out any unread data in SPI read buffer */
        while((${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_INTFLAG & SERCOM_SPIM_INTFLAG_RXC_Msk) == SERCOM_SPIM_INTFLAG_RXC_Msk)
        {
            dummyData = ${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_DATA;
            (void)dummyData;
        }

        ${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_STATUS |= SERCOM_SPIM_STATUS_BUFOVF_Msk;

        <#if SPI_INTENSET_ERROR = true>
        ${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_INTFLAG |= (uint8_t)SERCOM_SPIM_INTFLAG_ERROR_Msk;

        </#if>
        if(${SERCOM_INSTANCE_NAME?lower_case}SPIObj.rxSize > ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.txSize)
        {
            ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.dummySize = ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.rxSize - ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.txSize;
        }

        /* Start the first write here itself, rest will happen in ISR context */
        if((${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_CTRLB & SERCOM_SPIM_CTRLB_CHSIZE_Msk) == (uint32_t)SPI_DATA_BITS_8)
        {
            if(${SERCOM_INSTANCE_NAME?lower_case}SPIObj.txCount < ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.txSize)
            {
                ${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_DATA = *((uint8_t*)${SERCOM_INSTANCE_NAME?lower_case}SPIObj.txBuffer);

                ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.txCount++;
            }
            else if(${SERCOM_INSTANCE_NAME?lower_case}SPIObj.dummySize > 0U)
            {
                ${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_DATA = 0xFFU;

                ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.dummySize--;
            }
            else
            {
                /* Do nothing */
            }
        }
        else
        {
            ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.txSize >>= 1U;
            ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.dummySize >>= 1U;
            ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.rxSize >>= 1U;

            if(${SERCOM_INSTANCE_NAME?lower_case}SPIObj.txCount < ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.txSize)
            {
                ${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_DATA = *((uint16_t*)${SERCOM_INSTANCE_NAME?lower_case}SPIObj.txBuffer) & SERCOM_SPIM_DATA_Msk;

                ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.txCount++;
            }
            else if(${SERCOM_INSTANCE_NAME?lower_case}SPIObj.dummySize > 0U)
            {
                ${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_DATA = 0xFFFFU & SERCOM_SPIM_DATA_Msk;

                ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.dummySize--;
            }
            else
            {
                /* Do nothing */
            }
        }

        if(rxSize > 0U)
        {
            /* Enable ReceiveComplete  */
            ${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_INTENSET = (uint8_t)SERCOM_SPIM_INTENSET_RXC_Msk;
        }
        else
        {
            /* Enable the DataRegisterEmpty  */
            ${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_INTENSET = (uint8_t)SERCOM_SPIM_INTENSET_DRE_Msk;
        }
    }

    return isRequestAccepted;
}
</#if>

bool ${SERCOM_INSTANCE_NAME}_SPI_Write(void* pTransmitData, size_t txSize)
{
    return ${SERCOM_INSTANCE_NAME}_SPI_WriteRead(pTransmitData, txSize, NULL, 0U);
}

bool ${SERCOM_INSTANCE_NAME}_SPI_Read(void* pReceiveData, size_t rxSize)
{
    return ${SERCOM_INSTANCE_NAME}_SPI_WriteRead(NULL, 0U, pReceiveData, rxSize);
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
    uint32_t dataBits = 0U;
    uint32_t receivedData = 0U;
    static bool isLastByteTransferInProgress = false;

    if(${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_INTENSET != 0U)
    {
        dataBits = ${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_CTRLB & SERCOM_SPIM_CTRLB_CHSIZE_Msk;

        if((${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_INTFLAG & SERCOM_SPIM_INTFLAG_RXC_Msk) == SERCOM_SPIM_INTFLAG_RXC_Msk)
        {
            receivedData =  ${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_DATA;

            if(${SERCOM_INSTANCE_NAME?lower_case}SPIObj.rxCount < ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.rxSize)
            {
                if(dataBits == (uint32_t)SPI_DATA_BITS_8)
                {
                    ((uint8_t*)${SERCOM_INSTANCE_NAME?lower_case}SPIObj.rxBuffer)[${SERCOM_INSTANCE_NAME?lower_case}SPIObj.rxCount] = (uint8_t)receivedData;
					${SERCOM_INSTANCE_NAME?lower_case}SPIObj.rxCount++;
                }
                else
                {
                    ((uint16_t*)${SERCOM_INSTANCE_NAME?lower_case}SPIObj.rxBuffer)[${SERCOM_INSTANCE_NAME?lower_case}SPIObj.rxCount] = (uint16_t)receivedData;
					${SERCOM_INSTANCE_NAME?lower_case}SPIObj.rxCount++;
                }
            }
        }

        /* If there are more words to be transmitted, then transmit them here and keep track of the count */
        if((${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_INTFLAG & SERCOM_SPIM_INTFLAG_DRE_Msk) == SERCOM_SPIM_INTFLAG_DRE_Msk)
        {
            /* Disable the DRE interrupt. This will be enabled back if more than
             * one byte is pending to be transmitted */
            ${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_INTENCLR = (uint8_t)SERCOM_SPIM_INTENCLR_DRE_Msk;

            if(dataBits == (uint32_t)SPI_DATA_BITS_8)
            {
                if(${SERCOM_INSTANCE_NAME?lower_case}SPIObj.txCount < ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.txSize)
                {
                    ${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_DATA = ((uint8_t*)${SERCOM_INSTANCE_NAME?lower_case}SPIObj.txBuffer)[${SERCOM_INSTANCE_NAME?lower_case}SPIObj.txCount];
					${SERCOM_INSTANCE_NAME?lower_case}SPIObj.txCount++;
                }
                else if(${SERCOM_INSTANCE_NAME?lower_case}SPIObj.dummySize > 0U)
                {
                    ${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_DATA = 0xFFU;

                    ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.dummySize--;
                }
                else
                {
                    /* Do nothing */
                }
            }
            else
            {
                if(${SERCOM_INSTANCE_NAME?lower_case}SPIObj.txCount < ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.txSize)
                {
                    ${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_DATA = ((uint16_t*)${SERCOM_INSTANCE_NAME?lower_case}SPIObj.txBuffer)[${SERCOM_INSTANCE_NAME?lower_case}SPIObj.txCount];
					${SERCOM_INSTANCE_NAME?lower_case}SPIObj.txCount++;
                }
                else if(${SERCOM_INSTANCE_NAME?lower_case}SPIObj.dummySize > 0U)
                {
                    ${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_DATA = 0xFFFFU;

                    ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.dummySize--;
                }
                else
                {
                    /* Do nothing */
                }
            }

            if((${SERCOM_INSTANCE_NAME?lower_case}SPIObj.txCount == ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.txSize) && (${SERCOM_INSTANCE_NAME?lower_case}SPIObj.dummySize == 0U))
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
                ${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_INTENSET = (uint8_t)SERCOM_SPIM_INTENSET_DRE_Msk;

                ${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_INTENCLR = (uint8_t)SERCOM_SPIM_INTENCLR_RXC_Msk;
            }
            else
            {
                /* Do nothing */
            }
        }

        if(((${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_INTFLAG & SERCOM_SPIM_INTFLAG_TXC_Msk) == SERCOM_SPIM_INTFLAG_TXC_Msk) && (isLastByteTransferInProgress == true))
        {
            if(${SERCOM_INSTANCE_NAME?lower_case}SPIObj.rxCount == ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.rxSize)
            {
                ${SERCOM_INSTANCE_NAME?lower_case}SPIObj.transferIsBusy = false;

                /* Disable the Data Register empty and Receive Complete Interrupt flags */
                ${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_INTENCLR = (uint8_t)(SERCOM_SPIM_INTENCLR_DRE_Msk | SERCOM_SPIM_INTENCLR_RXC_Msk | SERCOM_SPIM_INTENSET_TXC_Msk);

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
            ${SERCOM_INSTANCE_NAME}_REGS->SPIM.SERCOM_INTENSET = (uint8_t)SERCOM_SPIM_INTENSET_TXC_Msk;
        }
    }
}
</#if>
