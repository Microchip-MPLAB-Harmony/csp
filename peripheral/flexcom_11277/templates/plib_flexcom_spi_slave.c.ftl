/*******************************************************************************
  SPI${FLEXCOM_INSTANCE_NAME} SPI PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${FLEXCOM_INSTANCE_NAME?lower_case}_spi_slave.c

  Summary:
    SPI${FLEXCOM_INSTANCE_NAME} SPI Slave PLIB Implementation File.

  Description:
    This file defines the interface to the FLEXCOM SPI peripheral library.
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
<#if core.PORT_API_PREFIX??>
<#assign PLIB_NAME  = core.PORT_API_PREFIX?string>
<#assign PLIB_NAME_LC  = core.PORT_API_PREFIX?lower_case>
<#assign SPI_BUSY_PIN = PLIB_NAME + "_PIN_" + FLEXCOM_SPIS_BUSY_PIN>
</#if>

#include "plib_${FLEXCOM_INSTANCE_NAME?lower_case}_spi_slave.h"
<#if FLEXCOM_SPIS_USE_BUSY_PIN == true>
#include "peripheral/${PLIB_NAME_LC}/plib_${PLIB_NAME_LC}.h"
</#if>
#include <string.h>
<#if core.CoreSysIntFile == true>
#include "interrupts.h"
</#if>

<#if FLEXCOM_SPI_CSR0_BITS = "8_BIT">
#define ${FLEXCOM_INSTANCE_NAME}_READ_BUFFER_SIZE            ${FLEXCOM_SPIS_RX_BUFFER_SIZE}
#define ${FLEXCOM_INSTANCE_NAME}_WRITE_BUFFER_SIZE           ${FLEXCOM_SPIS_TX_BUFFER_SIZE}

static uint8_t ${FLEXCOM_INSTANCE_NAME}_ReadBuffer[${FLEXCOM_INSTANCE_NAME}_READ_BUFFER_SIZE];
static uint8_t ${FLEXCOM_INSTANCE_NAME}_WriteBuffer[${FLEXCOM_INSTANCE_NAME}_WRITE_BUFFER_SIZE];

<#else>

#define ${FLEXCOM_INSTANCE_NAME}_READ_BUFFER_SIZE            ${FLEXCOM_SPIS_RX_BUFFER_SIZE/2}
#define ${FLEXCOM_INSTANCE_NAME}_WRITE_BUFFER_SIZE           ${FLEXCOM_SPIS_TX_BUFFER_SIZE/2}

static uint16_t ${FLEXCOM_INSTANCE_NAME}_ReadBuffer[${FLEXCOM_INSTANCE_NAME}_READ_BUFFER_SIZE];
static uint16_t ${FLEXCOM_INSTANCE_NAME}_WriteBuffer[${FLEXCOM_INSTANCE_NAME}_WRITE_BUFFER_SIZE];
</#if>

// *****************************************************************************
// *****************************************************************************
// Section: SPI${FLEXCOM_INSTANCE_NAME} SPI Implementation
// *****************************************************************************
// *****************************************************************************

/* Global object to save FLEXCOM SPI Exchange related data */
FLEXCOM_SPI_SLAVE_OBJECT ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj;

void ${FLEXCOM_INSTANCE_NAME}_SPI_Initialize( void )
{
    /* Set FLEXCOM SPI operating mode */
    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEXCOM_MR = FLEXCOM_MR_OPMODE_SPI;

    /* Disable and Reset the SPI*/
    SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_CR = SPI_CR_SPIDIS_Msk | SPI_CR_SWRST_Msk;

    /* SPI is by default in Slave Mode, disable mode fault detection */
    SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_MR = SPI_MR_MODFDIS_Msk;

    /* Set up clock Polarity, data phase, Communication Width */
    SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_CSR[0] = SPI_CSR_CPOL(${FLEXCOM_SPI_CSR0_CPOL}) | SPI_CSR_NCPHA(${FLEXCOM_SPI_CSR0_NCPHA}) | SPI_CSR_BITS${FLEXCOM_SPI_CSR0_BITS};

    ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.rdInIndex = 0;
    ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.wrOutIndex = 0;
    ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.nWrBytes = 0;
    ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.errorStatus = FLEXCOM_SPI_SLAVE_ERROR_NONE;
    ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.callback = NULL ;
    ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.transferIsBusy = false ;

    <#if FLEXCOM_SPIS_USE_BUSY_PIN == true>
    /* Set the Busy Pin to ready state */
    <#if FLEXCOM_SPIS_BUSY_PIN_LOGIC_LEVEL = "ACTIVE_HIGH">
    ${PLIB_NAME}_PinWrite((${PLIB_NAME}_PIN)${PLIB_NAME}_PIN_${FLEXCOM_SPIS_BUSY_PIN}, 0);
    <#else>
    ${PLIB_NAME}_PinWrite((${PLIB_NAME}_PIN)${PLIB_NAME}_PIN_${FLEXCOM_SPIS_BUSY_PIN}, 1);
    </#if>
    </#if>

    /* Enable Receive full and chip deselect interrupt */
    SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_IER = (SPI_IER_RDRF_Msk | SPI_IER_NSSR_Msk);

    /* Enable SPI${FLEXCOM_INSTANCE_NAME} */
    SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_CR = SPI_CR_SPIEN_Msk;
}

/* For 9-bit mode, the "size" must be specified in terms of 16-bit words */
size_t ${FLEXCOM_INSTANCE_NAME}_SPI_Read(void* pRdBuffer, size_t size)
{
    size_t rdSize = size;
    size_t rdInIndex = ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.rdInIndex;

    if (rdSize > rdInIndex)
    {
        rdSize = rdInIndex;
    }

<#if FLEXCOM_SPI_CSR0_BITS = "8_BIT">
    memcpy(pRdBuffer, ${FLEXCOM_INSTANCE_NAME}_ReadBuffer, rdSize);
<#else>
    memcpy(pRdBuffer, ${FLEXCOM_INSTANCE_NAME}_ReadBuffer, (rdSize << 1));
</#if>

    return rdSize;
}

/* For 9-bit mode, the "size" must be specified in terms of 16-bit words */
size_t ${FLEXCOM_INSTANCE_NAME}_SPI_Write(void* pWrBuffer, size_t size )
{
    uint32_t intState = SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_IMR;
    size_t wrSize = size;

    SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_IDR = intState;

    if (wrSize > ${FLEXCOM_INSTANCE_NAME}_WRITE_BUFFER_SIZE)
    {
        wrSize = ${FLEXCOM_INSTANCE_NAME}_WRITE_BUFFER_SIZE;
    }

<#if FLEXCOM_SPI_CSR0_BITS = "8_BIT">
    memcpy(${FLEXCOM_INSTANCE_NAME}_WriteBuffer, pWrBuffer, wrSize);
<#else>
    memcpy(${FLEXCOM_INSTANCE_NAME}_WriteBuffer, pWrBuffer, (wrSize << 1));
</#if>

    ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.nWrBytes = wrSize;
    ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.wrOutIndex = 0;

    while ((SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_SR & SPI_SR_TDRE_Msk) && (${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.wrOutIndex < ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.nWrBytes))
    {
<#if FLEXCOM_SPI_CSR0_BITS = "8_BIT">
        *((uint8_t*)&SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_TDR) = ${FLEXCOM_INSTANCE_NAME}_WriteBuffer[${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.wrOutIndex++];
<#else>
        *((uint16_t*)&SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_TDR) = ${FLEXCOM_INSTANCE_NAME}_WriteBuffer[${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.wrOutIndex++];
</#if>
    }

    /* Restore interrupt enable state and also enable TDRE interrupt */
    SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_IER = (intState | SPI_IER_TDRE_Msk);

    return wrSize;
}

/* For 9-bit mode, the return value is in terms of 16-bit words */
size_t ${FLEXCOM_INSTANCE_NAME}_SPI_ReadCountGet(void)
{
    return ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.rdInIndex;
}

/* For 9-bit mode, the return value is in terms of 16-bit words */
size_t ${FLEXCOM_INSTANCE_NAME}_SPI_ReadBufferSizeGet(void)
{
    return ${FLEXCOM_INSTANCE_NAME}_READ_BUFFER_SIZE;
}

/* For 9-bit mode, the return value is in terms of 16-bit words */
size_t ${FLEXCOM_INSTANCE_NAME}_SPI_WriteBufferSizeGet(void)
{
    return ${FLEXCOM_INSTANCE_NAME}_WRITE_BUFFER_SIZE;
}

void ${FLEXCOM_INSTANCE_NAME}_SPI_CallbackRegister(FLEXCOM_SPI_SLAVE_CALLBACK callBack, uintptr_t context )
{
    ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.callback = callBack;

    ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.context = context;
}

/* The status is returned busy during the period the chip-select remains asserted */
bool ${FLEXCOM_INSTANCE_NAME}_SPI_IsBusy(void)
{
    return ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.transferIsBusy;
}

<#if FLEXCOM_SPIS_USE_BUSY_PIN == true>
/* Drive the GPIO pin to indicate to SPI Master that the slave is ready now */
void ${FLEXCOM_INSTANCE_NAME}_SPI_Ready(void)
{
<#if FLEXCOM_SPIS_BUSY_PIN_LOGIC_LEVEL = "ACTIVE_HIGH">
    ${PLIB_NAME}_PinWrite((${PLIB_NAME}_PIN)${PLIB_NAME}_PIN_${FLEXCOM_SPIS_BUSY_PIN}, 0);
<#else>
    ${PLIB_NAME}_PinWrite((${PLIB_NAME}_PIN)${PLIB_NAME}_PIN_${FLEXCOM_SPIS_BUSY_PIN}, 1);
</#if>
}
</#if>

FLEXCOM_SPI_SLAVE_ERROR ${FLEXCOM_INSTANCE_NAME}_SPI_ErrorGet(void)
{
    FLEXCOM_SPI_SLAVE_ERROR errorStatus = ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.errorStatus;

    ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.errorStatus = FLEXCOM_SPI_SLAVE_ERROR_NONE;

    return errorStatus;
}

void ${FLEXCOM_INSTANCE_NAME}_InterruptHandler(void)
{
<#if FLEXCOM_SPI_CSR0_BITS = "8_BIT">
    uint8_t txRxData = 0;
<#else>
    uint16_t txRxData = 0;
</#if>

    uint32_t statusFlags = SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_SR;

    if (statusFlags & SPI_SR_OVRES_Msk)
    {
        /*OVRES flag is cleared on reading SPI SR*/

        /* Save the error to report it to application later */
        ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.errorStatus = SPI_SR_OVRES_Msk;
    }

    if(statusFlags & SPI_SR_RDRF_Msk)
    {
        if (${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.transferIsBusy == false)
        {
            ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.transferIsBusy = true;

            <#if FLEXCOM_SPIS_USE_BUSY_PIN == true && FLEXCOM_SPIS_BUSY_PIN_LOGIC_LEVEL = "ACTIVE_HIGH">
            ${PLIB_NAME}_PinWrite((${PLIB_NAME}_PIN)${PLIB_NAME}_PIN_${FLEXCOM_SPIS_BUSY_PIN}, 1);
            <#elseif FLEXCOM_SPIS_USE_BUSY_PIN == true && FLEXCOM_SPIS_BUSY_PIN_LOGIC_LEVEL = "ACTIVE_LOW">
            ${PLIB_NAME}_PinWrite((${PLIB_NAME}_PIN)${PLIB_NAME}_PIN_${FLEXCOM_SPIS_BUSY_PIN}, 0);
            </#if>
        }

        while ((statusFlags |= SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_SR) & SPI_SR_RDRF_Msk)
        {
<#if FLEXCOM_SPI_CSR0_BITS = "8_BIT">
            /* Reading DATA register will also clear the RDRF flag */
            txRxData = *((uint8_t*)&SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_RDR);
<#else>
            txRxData = *((uint16_t*)&SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_RDR);
</#if>

            if (${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.rdInIndex < ${FLEXCOM_INSTANCE_NAME}_READ_BUFFER_SIZE)
            {
                ${FLEXCOM_INSTANCE_NAME}_ReadBuffer[${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.rdInIndex++] = txRxData;
            }

            statusFlags &= ~SPI_SR_RDRF_Msk;
        }
    }

    if(statusFlags & SPI_SR_TDRE_Msk)
    {
        while (((statusFlags |= SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_SR) & SPI_SR_TDRE_Msk) && (${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.wrOutIndex < ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.nWrBytes))
        {
<#if FLEXCOM_SPI_CSR0_BITS = "8_BIT">
            *((uint8_t*)&SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_TDR) = ${FLEXCOM_INSTANCE_NAME}_WriteBuffer[${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.wrOutIndex++];
<#else>
            *((uint16_t*)&SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_TDR) = ${FLEXCOM_INSTANCE_NAME}_WriteBuffer[${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.wrOutIndex++];
</#if>
            statusFlags &= ~SPI_SR_TDRE_Msk;
        }

        if (${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.wrOutIndex >= ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.nWrBytes)
        {
            /* Disable TDRE interrupt. The last byte sent by the master will be shifted out automatically */
            SPI${FLEXCOM_INSTANCE_NUMBER}_REGS->SPI_IDR = SPI_IDR_TDRE_Msk;
        }
    }

    if(statusFlags & SPI_SR_NSSR_Msk)
    {
        /* NSSR flag is cleared on reading SPI SR */

        ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.transferIsBusy = false;

        ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.wrOutIndex = 0;
        ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.nWrBytes = 0;

        if(${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.callback != NULL)
        {
            ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.callback(${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.context);
        }

        /* Clear the rdInIndex. Application must read the received data in the callback. */
        ${FLEXCOM_INSTANCE_NAME?lower_case}SpiObj.rdInIndex = 0;
    }
}