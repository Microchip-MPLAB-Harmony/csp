/*******************************************************************************
  SERIAL COMMUNICATION SERIAL PERIPHERAL INTERFACE(${SERCOM_INSTANCE_NAME}_SPI) PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_${SERCOM_INSTANCE_NAME?lower_case}_spi_slave.c

  Summary
    ${SERCOM_INSTANCE_NAME}_SPI PLIB Slave Implementation File.

  Description
    This file defines the interface to the SERCOM SPI Slave peripheral library.
    This library provides access to and control of the associated
    peripheral instance.

  Remarks:
    None.

*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
* Copyright (C) 2020 Microchip Technology Inc. and its subsidiaries.
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
<#if core.PORT_API_PREFIX??>
<#assign PLIB_NAME  = core.PORT_API_PREFIX?string>
<#assign PLIB_NAME_LC  = core.PORT_API_PREFIX?lower_case>
<#assign SPI_BUSY_PIN = PLIB_NAME + "_PIN_" + SPIS_BUSY_PIN>
</#if>

<#if core.CoreSysIntFile == true>
#include "interrupts.h"
</#if>
#include "plib_${SERCOM_INSTANCE_NAME?lower_case}_spi_slave.h"
<#if SPIS_USE_BUSY_PIN == true>
#include "peripheral/${PLIB_NAME_LC}/plib_${PLIB_NAME_LC}.h"
</#if>
#include <string.h>

// *****************************************************************************
// *****************************************************************************
// Section: MACROS Definitions
// *****************************************************************************
// *****************************************************************************
<#if SPIS_CHARSIZE_BITS = "8_BIT">
<#assign TXRX_DATA_T = "uint8_t">
#define ${SERCOM_INSTANCE_NAME}_SPI_READ_BUFFER_SIZE            ${SPIS_RX_BUFFER_SIZE}U
#define ${SERCOM_INSTANCE_NAME}_SPI_WRITE_BUFFER_SIZE           ${SPIS_TX_BUFFER_SIZE}U
<#else>
<#assign TXRX_DATA_T = "uint16_t">
#define ${SERCOM_INSTANCE_NAME}_SPI_READ_BUFFER_SIZE            ${SPIS_RX_BUFFER_SIZE/2}U
#define ${SERCOM_INSTANCE_NAME}_SPI_WRITE_BUFFER_SIZE           ${SPIS_TX_BUFFER_SIZE/2}U
</#if>

static ${TXRX_DATA_T} ${SERCOM_INSTANCE_NAME}_SPI_ReadBuffer[${SERCOM_INSTANCE_NAME}_SPI_READ_BUFFER_SIZE];
static ${TXRX_DATA_T} ${SERCOM_INSTANCE_NAME}_SPI_WriteBuffer[${SERCOM_INSTANCE_NAME}_SPI_WRITE_BUFFER_SIZE];


/* Global object to save SPI Exchange related data  */
static SPI_SLAVE_OBJECT ${SERCOM_INSTANCE_NAME?lower_case}SPISObj;

// *****************************************************************************
// *****************************************************************************
// Section: ${SERCOM_INSTANCE_NAME}_SPI Slave Implementation
// *****************************************************************************
// *****************************************************************************
// *****************************************************************************

void ${SERCOM_INSTANCE_NAME}_SPI_Initialize(void)
{
    /* CHSIZE - ${SPIS_CHARSIZE_BITS}
     * PLOADEN - 1
     * <#if (SPIS_SSDE??) && (SPIS_SSDE = true)> SSDE - 1 </#if>
     * RXEN - 1
     */
    <@compress single_line=true>${SERCOM_INSTANCE_NAME}_REGS->SPIS.SERCOM_CTRLB =
    SERCOM_SPIS_CTRLB_CHSIZE_${SPIS_CHARSIZE_BITS}
    | SERCOM_SPIS_CTRLB_PLOADEN_Msk
    | SERCOM_SPIS_CTRLB_RXEN_Msk
    <#if (SPIS_SSDE??) && (SPIS_SSDE = true)> | SERCOM_SPIS_CTRLB_SSDE_Msk</#if>;</@compress>

    /* Wait for synchronization */
    <#if SERCOM_SYNCBUSY = false>
    while((${SERCOM_INSTANCE_NAME}_REGS->SPIS.SERCOM_STATUS & (uint16_t)SERCOM_SPIS_STATUS_SYNCBUSY_Msk) == (uint16_t)SERCOM_SPIS_STATUS_SYNCBUSY_Msk)
    {
        /* Do nothing */
    }
    <#else>
    while(${SERCOM_INSTANCE_NAME}_REGS->SPIS.SERCOM_SYNCBUSY != 0U)
    {
        /* Do nothing */
    }
    </#if>

    /* Mode - SPI Slave
     * IBON - 1 (Set immediately upon buffer overflow)
     * DOPO - ${SPIS_DOPO}
     * DIPO - ${SPIS_DIPO}
     * CPHA - ${SPIS_CLOCK_PHASE}
     * COPL - ${SPIS_CLOCK_POLARITY}
     * DORD - ${SPIS_DATA_ORDER}
     * ENABLE - 1
     */
    <@compress single_line=true>${SERCOM_INSTANCE_NAME}_REGS->SPIS.SERCOM_CTRLA =
    SERCOM_SPIS_CTRLA_MODE_SPI_SLAVE |
    SERCOM_SPIS_CTRLA_IBON_Msk |
    SERCOM_SPIS_CTRLA_DOPO_${SPIS_DOPO} |
    SERCOM_SPIS_CTRLA_DIPO_${SPIS_DIPO} |
    SERCOM_SPIS_CTRLA_CPOL_${SPIS_CLOCK_POLARITY} |
    SERCOM_SPIS_CTRLA_CPHA_${SPIS_CLOCK_PHASE} |
    SERCOM_SPIS_CTRLA_DORD_${SPIS_DATA_ORDER} |
    SERCOM_SPIS_CTRLA_ENABLE_Msk
    ${SPIS_RUNSTDBY?then(' | SERCOM_SPIS_CTRLA_RUNSTDBY_Msk', '')};</@compress>

    /* Wait for synchronization */
    <#if SERCOM_SYNCBUSY = false>
    while((${SERCOM_INSTANCE_NAME}_REGS->SPIS.SERCOM_STATUS & (uint16_t)SERCOM_SPIS_STATUS_SYNCBUSY_Msk) == (uint16_t)SERCOM_SPIS_STATUS_SYNCBUSY_Msk)
    {
        /* Do nothing */
    }
    <#else>
    while(${SERCOM_INSTANCE_NAME}_REGS->SPIS.SERCOM_SYNCBUSY != 0U)
    {
        /* Do nothing */
    }
    </#if>

    ${SERCOM_INSTANCE_NAME?lower_case}SPISObj.rdInIndex = 0U;
    ${SERCOM_INSTANCE_NAME?lower_case}SPISObj.wrOutIndex = 0U;
    ${SERCOM_INSTANCE_NAME?lower_case}SPISObj.nWrBytes = 0U;
    ${SERCOM_INSTANCE_NAME?lower_case}SPISObj.errorStatus = SPI_SLAVE_ERROR_NONE;
    ${SERCOM_INSTANCE_NAME?lower_case}SPISObj.callback = NULL ;
    ${SERCOM_INSTANCE_NAME?lower_case}SPISObj.transferIsBusy = false ;

    <#if (SPIS_SSDE??) && (SPIS_SSDE = true)>
    ${SERCOM_INSTANCE_NAME}_REGS->SPIS.SERCOM_INTENSET = (uint8_t)(SERCOM_SPIS_INTENSET_SSL_Msk | SERCOM_SPIS_INTENCLR_RXC_Msk);
    <#else>
    ${SERCOM_INSTANCE_NAME}_REGS->SPIS.SERCOM_INTENSET = (uint8_t)(SERCOM_SPIS_INTENCLR_RXC_Msk| SERCOM_SPIS_INTENSET_TXC_Msk);
    </#if>

    <#if SPIS_USE_BUSY_PIN == true>
    /* Set the Busy Pin to ready state */
    <#if SPIS_BUSY_PIN_LOGIC_LEVEL = "ACTIVE_HIGH">
    ${PLIB_NAME}_PinWrite(${SPI_BUSY_PIN}, false);
    <#else>
    ${PLIB_NAME}_PinWrite(${SPI_BUSY_PIN}, true);
    </#if>
    </#if>
}

/* For 9-bit mode, the "size" must be specified in terms of 16-bit words */
size_t ${SERCOM_INSTANCE_NAME}_SPI_Read(void* pRdBuffer, size_t size)
{
    uint8_t intState = ${SERCOM_INSTANCE_NAME}_REGS->SPIS.SERCOM_INTENSET;
    size_t rdSize = size;

    ${SERCOM_INSTANCE_NAME}_REGS->SPIS.SERCOM_INTENCLR = intState;

    if (rdSize > ${SERCOM_INSTANCE_NAME?lower_case}SPISObj.rdInIndex)
    {
        rdSize = ${SERCOM_INSTANCE_NAME?lower_case}SPISObj.rdInIndex;
    }

<#if SPIS_CHARSIZE_BITS == "8_BIT">
    (void) memcpy(pRdBuffer, ${SERCOM_INSTANCE_NAME}_SPI_ReadBuffer, rdSize);
<#else>
    (void) memcpy(pRdBuffer, ${SERCOM_INSTANCE_NAME}_SPI_ReadBuffer, (rdSize << 1U));
</#if>

    ${SERCOM_INSTANCE_NAME}_REGS->SPIS.SERCOM_INTENSET = intState;

    return rdSize;
}

/* For 9-bit mode, the "size" must be specified in terms of 16-bit words */
size_t ${SERCOM_INSTANCE_NAME}_SPI_Write(void* pWrBuffer, size_t size )
{
    uint8_t intState = ${SERCOM_INSTANCE_NAME}_REGS->SPIS.SERCOM_INTENSET;
    size_t wrSize = size;
    bool writeReady = false;

    ${SERCOM_INSTANCE_NAME}_REGS->SPIS.SERCOM_INTENCLR = intState;

    if (wrSize > ${SERCOM_INSTANCE_NAME}_SPI_WRITE_BUFFER_SIZE)
    {
        wrSize = ${SERCOM_INSTANCE_NAME}_SPI_WRITE_BUFFER_SIZE;
    }

<#if SPIS_CHARSIZE_BITS == "8_BIT">
   (void) memcpy(${SERCOM_INSTANCE_NAME}_SPI_WriteBuffer, pWrBuffer, wrSize);
<#else>
   (void) memcpy(${SERCOM_INSTANCE_NAME}_SPI_WriteBuffer, pWrBuffer, (wrSize << 1U));
</#if>

    ${SERCOM_INSTANCE_NAME?lower_case}SPISObj.nWrBytes = wrSize;
    ${SERCOM_INSTANCE_NAME?lower_case}SPISObj.wrOutIndex = 0U;

    writeReady = (${SERCOM_INSTANCE_NAME?lower_case}SPISObj.wrOutIndex < ${SERCOM_INSTANCE_NAME?lower_case}SPISObj.nWrBytes);
    writeReady = ((${SERCOM_INSTANCE_NAME}_REGS->SPIS.SERCOM_INTFLAG & SERCOM_SPIS_INTFLAG_DRE_Msk) == SERCOM_SPIS_INTFLAG_DRE_Msk) && writeReady;
    while (writeReady)
    {
        ${SERCOM_INSTANCE_NAME}_REGS->SPIS.SERCOM_DATA = ${SERCOM_INSTANCE_NAME}_SPI_WriteBuffer[${SERCOM_INSTANCE_NAME?lower_case}SPISObj.wrOutIndex];
		${SERCOM_INSTANCE_NAME?lower_case}SPISObj.wrOutIndex++;
        writeReady = (${SERCOM_INSTANCE_NAME?lower_case}SPISObj.wrOutIndex < ${SERCOM_INSTANCE_NAME?lower_case}SPISObj.nWrBytes);
        writeReady = ((${SERCOM_INSTANCE_NAME}_REGS->SPIS.SERCOM_INTFLAG & SERCOM_SPIS_INTFLAG_DRE_Msk) == SERCOM_SPIS_INTFLAG_DRE_Msk) && writeReady;
    }

    /* Restore interrupt enable state and also enable DRE interrupt to start pre-loading of DATA register */
    ${SERCOM_INSTANCE_NAME}_REGS->SPIS.SERCOM_INTENSET = (intState | (uint8_t)SERCOM_SPIS_INTENSET_DRE_Msk);

    return wrSize;
}

/* For 9-bit mode, the return value is in terms of 16-bit words */
size_t ${SERCOM_INSTANCE_NAME}_SPI_ReadCountGet(void)
{
    return ${SERCOM_INSTANCE_NAME?lower_case}SPISObj.rdInIndex;
}

/* For 9-bit mode, the return value is in terms of 16-bit words */
size_t ${SERCOM_INSTANCE_NAME}_SPI_ReadBufferSizeGet(void)
{
    return ${SERCOM_INSTANCE_NAME}_SPI_READ_BUFFER_SIZE;
}

/* For 9-bit mode, the return value is in terms of 16-bit words */
size_t ${SERCOM_INSTANCE_NAME}_SPI_WriteBufferSizeGet(void)
{
    return ${SERCOM_INSTANCE_NAME}_SPI_WRITE_BUFFER_SIZE;
}

void ${SERCOM_INSTANCE_NAME}_SPI_CallbackRegister(SERCOM_SPI_SLAVE_CALLBACK callBack, uintptr_t context )
{
    ${SERCOM_INSTANCE_NAME?lower_case}SPISObj.callback = callBack;

    ${SERCOM_INSTANCE_NAME?lower_case}SPISObj.context = context;
}

/* The status is returned busy during the period the chip-select remains asserted */
bool ${SERCOM_INSTANCE_NAME}_SPI_IsBusy(void)
{
    return ${SERCOM_INSTANCE_NAME?lower_case}SPISObj.transferIsBusy;
}

<#if SPIS_USE_BUSY_PIN == true>
/* Drive the GPIO pin to indicate to SPI Master that the slave is ready now */
void ${SERCOM_INSTANCE_NAME}_SPI_Ready(void)
{
<#if SPIS_BUSY_PIN_LOGIC_LEVEL = "ACTIVE_HIGH">
    ${PLIB_NAME}_PinWrite(${SPI_BUSY_PIN}, false);
<#else>
    ${PLIB_NAME}_PinWrite(${SPI_BUSY_PIN}, true);
</#if>
}
</#if>

SPI_SLAVE_ERROR ${SERCOM_INSTANCE_NAME}_SPI_ErrorGet(void)
{
    SPI_SLAVE_ERROR errorStatus = ${SERCOM_INSTANCE_NAME?lower_case}SPISObj.errorStatus;

    ${SERCOM_INSTANCE_NAME?lower_case}SPISObj.errorStatus = SPI_SLAVE_ERROR_NONE;

    return errorStatus;
}

void ${SERCOM_INSTANCE_NAME}_SPI_InterruptHandler(void)
{
    ${TXRX_DATA_T} txRxData;
    uint8_t intFlag = ${SERCOM_INSTANCE_NAME}_REGS->SPIS.SERCOM_INTFLAG;

<#if (SPIS_SSDE??) && (SPIS_SSDE = true)>
    if((${SERCOM_INSTANCE_NAME}_REGS->SPIS.SERCOM_INTFLAG & SERCOM_SPIS_INTFLAG_SSL_Msk) == SERCOM_SPIS_INTFLAG_SSL_Msk)
    {
        /* Clear the SSL flag and enable TXC interrupt */
        ${SERCOM_INSTANCE_NAME}_REGS->SPIS.SERCOM_INTFLAG = (uint8_t)SERCOM_SPIS_INTFLAG_SSL_Msk;
        ${SERCOM_INSTANCE_NAME}_REGS->SPIS.SERCOM_INTENSET = (uint8_t)SERCOM_SPIS_INTENSET_TXC_Msk;
        ${SERCOM_INSTANCE_NAME?lower_case}SPISObj.rdInIndex = 0U;
        ${SERCOM_INSTANCE_NAME?lower_case}SPISObj.transferIsBusy = true;
<#if SPIS_USE_BUSY_PIN == true && SPIS_BUSY_PIN_LOGIC_LEVEL = "ACTIVE_HIGH">
        ${PLIB_NAME}_PinWrite(${SPI_BUSY_PIN}, true);
<#elseif SPIS_USE_BUSY_PIN == true && SPIS_BUSY_PIN_LOGIC_LEVEL = "ACTIVE_LOW">
        ${PLIB_NAME}_PinWrite(${SPI_BUSY_PIN}, false);
</#if>
    }
</#if>

    if ((${SERCOM_INSTANCE_NAME}_REGS->SPIS.SERCOM_STATUS & SERCOM_SPIS_STATUS_BUFOVF_Msk) == SERCOM_SPIS_STATUS_BUFOVF_Msk)
    {
        /* Save the error to report it to application later, when the transfer is complete (TXC = 1) */
        ${SERCOM_INSTANCE_NAME?lower_case}SPISObj.errorStatus = SERCOM_SPIS_STATUS_BUFOVF_Msk;

        /* Clear the status register */
        ${SERCOM_INSTANCE_NAME}_REGS->SPIS.SERCOM_STATUS = SERCOM_SPIS_STATUS_BUFOVF_Msk;

        /* Flush out the received data until RXC flag is set */
        while((${SERCOM_INSTANCE_NAME}_REGS->SPIS.SERCOM_INTFLAG & SERCOM_SPIS_INTFLAG_RXC_Msk) == SERCOM_SPIS_INTFLAG_RXC_Msk)
        {
            /* Reading DATA register will also clear the RXC flag */
            txRxData = (${TXRX_DATA_T})${SERCOM_INSTANCE_NAME}_REGS->SPIS.SERCOM_DATA;
        }

        <#if SPIS_INTENSET_ERROR??>
        /* Clear the Error Interrupt Flag */
        ${SERCOM_INSTANCE_NAME}_REGS->SPIS.SERCOM_INTFLAG = (uint8_t)SERCOM_SPIS_INTFLAG_ERROR_Msk;
        </#if>
    }

    if((${SERCOM_INSTANCE_NAME}_REGS->SPIS.SERCOM_INTFLAG & SERCOM_SPIS_INTFLAG_RXC_Msk) == SERCOM_SPIS_INTFLAG_RXC_Msk)
    {
<#if !(SPIS_SSDE??) >
        ${SERCOM_INSTANCE_NAME?lower_case}SPISObj.transferIsBusy = true;
<#if SPIS_USE_BUSY_PIN == true && SPIS_BUSY_PIN_LOGIC_LEVEL = "ACTIVE_HIGH">
        ${PLIB_NAME}_PinWrite(${SPI_BUSY_PIN}, true);
<#elseif SPIS_USE_BUSY_PIN == true && SPIS_BUSY_PIN_LOGIC_LEVEL = "ACTIVE_LOW">
        ${PLIB_NAME}_PinWrite(${SPI_BUSY_PIN}, false);
</#if>
</#if>
        /* Reading DATA register will also clear the RXC flag */
        txRxData = (${TXRX_DATA_T})${SERCOM_INSTANCE_NAME}_REGS->SPIS.SERCOM_DATA;     

        if (${SERCOM_INSTANCE_NAME?lower_case}SPISObj.rdInIndex < ${SERCOM_INSTANCE_NAME}_SPI_READ_BUFFER_SIZE)
        {
            ${SERCOM_INSTANCE_NAME}_SPI_ReadBuffer[${SERCOM_INSTANCE_NAME?lower_case}SPISObj.rdInIndex] = txRxData;
			${SERCOM_INSTANCE_NAME?lower_case}SPISObj.rdInIndex++;
        }
    }

    if((${SERCOM_INSTANCE_NAME}_REGS->SPIS.SERCOM_INTFLAG & SERCOM_SPIS_INTFLAG_DRE_Msk) == SERCOM_SPIS_INTFLAG_DRE_Msk)
    {
        if (${SERCOM_INSTANCE_NAME?lower_case}SPISObj.wrOutIndex < ${SERCOM_INSTANCE_NAME?lower_case}SPISObj.nWrBytes)
        {
            txRxData = ${SERCOM_INSTANCE_NAME}_SPI_WriteBuffer[${SERCOM_INSTANCE_NAME?lower_case}SPISObj.wrOutIndex];
			${SERCOM_INSTANCE_NAME?lower_case}SPISObj.wrOutIndex++;

            /* Before writing to DATA register (which clears TXC flag), check if TXC flag is set */
            if((${SERCOM_INSTANCE_NAME}_REGS->SPIS.SERCOM_INTFLAG & SERCOM_SPIS_INTFLAG_TXC_Msk) == SERCOM_SPIS_INTFLAG_TXC_Msk)
            {
                intFlag = (uint8_t)SERCOM_SPIS_INTFLAG_TXC_Msk;
            }
            ${SERCOM_INSTANCE_NAME}_REGS->SPIS.SERCOM_DATA = (uint32_t)txRxData;
        }
        else
        {
            /* Disable DRE interrupt. The last byte sent by the master will be shifted out automatically */
            ${SERCOM_INSTANCE_NAME}_REGS->SPIS.SERCOM_INTENCLR = (uint8_t)SERCOM_SPIS_INTENCLR_DRE_Msk;
        }
    }

    if((intFlag & SERCOM_SPIS_INTFLAG_TXC_Msk) == SERCOM_SPIS_INTFLAG_TXC_Msk)
    {
        /* Clear TXC flag */
        ${SERCOM_INSTANCE_NAME}_REGS->SPIS.SERCOM_INTFLAG = (uint8_t)SERCOM_SPIS_INTFLAG_TXC_Msk;

        ${SERCOM_INSTANCE_NAME?lower_case}SPISObj.transferIsBusy = false;

        ${SERCOM_INSTANCE_NAME?lower_case}SPISObj.wrOutIndex = 0U;
        ${SERCOM_INSTANCE_NAME?lower_case}SPISObj.nWrBytes = 0U;

        if(${SERCOM_INSTANCE_NAME?lower_case}SPISObj.callback != NULL)
        {
            ${SERCOM_INSTANCE_NAME?lower_case}SPISObj.callback(${SERCOM_INSTANCE_NAME?lower_case}SPISObj.context);
        }
        <#if !(SPIS_SSDE??) >
        ${SERCOM_INSTANCE_NAME?lower_case}SPISObj.rdInIndex = 0U;
        </#if>
    }
}
