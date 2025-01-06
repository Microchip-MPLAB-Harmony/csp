/*******************************************************************************
  MCSPI PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${MCSPI_INSTANCE_NAME?lower_case}_slave.c

  Summary:
    ${MCSPI_INSTANCE_NAME} Slave Source File

  Description:
    This file has implementation of all the interfaces provided for particular
    MCSPI peripheral.

*******************************************************************************/

/*******************************************************************************
* Copyright (C) 2022 Microchip Technology Inc. and its subsidiaries.
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
<#if core.PORT_API_PREFIX??>
<#assign PLIB_NAME  = core.PORT_API_PREFIX?string>
<#assign PLIB_NAME_LC  = core.PORT_API_PREFIX?lower_case>
<#assign MCSPI_BUSY_PIN = PLIB_NAME + "_PIN_" + MCSPIS_BUSY_PIN>
</#if>

#include "plib_${MCSPI_INSTANCE_NAME?lower_case}_slave.h"
<#if MCSPIS_USE_BUSY_PIN == true>
#include "peripheral/${PLIB_NAME_LC}/plib_${PLIB_NAME_LC}.h"
</#if>
#include <string.h>
<#if core.CoreSysIntFile == true>
#include "interrupts.h"
</#if>

#define MCSPI_TDR_8BIT_REG      (*(volatile uint8_t* const)((${MCSPI_INSTANCE_NAME}_BASE_ADDRESS + MCSPI_TDR_REG_OFST)))
#define MCSPI_TDR_16BIT_REG     (*(volatile uint16_t* const)((${MCSPI_INSTANCE_NAME}_BASE_ADDRESS + MCSPI_TDR_REG_OFST)))

#define MCSPI_RDR_8BIT_REG      (*(volatile uint8_t* const)((${MCSPI_INSTANCE_NAME}_BASE_ADDRESS + MCSPI_RDR_REG_OFST)))
#define MCSPI_RDR_16BIT_REG     (*(volatile uint16_t* const)((${MCSPI_INSTANCE_NAME}_BASE_ADDRESS + MCSPI_RDR_REG_OFST)))

<#if MCSPI_CSR0_BITS = "_8_BIT">
#define ${MCSPI_INSTANCE_NAME}_READ_BUFFER_SIZE            (${MCSPIS_RX_BUFFER_SIZE}U)
#define ${MCSPI_INSTANCE_NAME}_WRITE_BUFFER_SIZE           (${MCSPIS_TX_BUFFER_SIZE}U)

static volatile uint8_t ${MCSPI_INSTANCE_NAME}_ReadBuffer[${MCSPI_INSTANCE_NAME}_READ_BUFFER_SIZE];
static volatile uint8_t ${MCSPI_INSTANCE_NAME}_WriteBuffer[${MCSPI_INSTANCE_NAME}_WRITE_BUFFER_SIZE];

<#else>

#define ${MCSPI_INSTANCE_NAME}_READ_BUFFER_SIZE            (${MCSPIS_RX_BUFFER_SIZE/2}U)
#define ${MCSPI_INSTANCE_NAME}_WRITE_BUFFER_SIZE           (${MCSPIS_TX_BUFFER_SIZE/2}U)

static volatile uint16_t ${MCSPI_INSTANCE_NAME}_ReadBuffer[${MCSPI_INSTANCE_NAME}_READ_BUFFER_SIZE];
static volatile uint16_t ${MCSPI_INSTANCE_NAME}_WriteBuffer[${MCSPI_INSTANCE_NAME}_WRITE_BUFFER_SIZE];
</#if>

// *****************************************************************************
// *****************************************************************************
// Section: ${MCSPI_INSTANCE_NAME} Implementation
// *****************************************************************************
// *****************************************************************************

/* Global object to save MCSPI Exchange related data */
static volatile MCSPI_SLAVE_OBJECT ${MCSPI_INSTANCE_NAME?lower_case}Obj;

void ${MCSPI_INSTANCE_NAME}_Initialize( void )
{
    /* Disable and Reset the MCSPI*/
    ${MCSPI_INSTANCE_NAME}_REGS->MCSPI_CR = MCSPI_CR_SPIDIS_Msk | MCSPI_CR_SWRST_Msk;

<#if MCSPI_FIFO_ENABLE == true>
    /* Enable FIFO support */
    ${MCSPI_INSTANCE_NAME}_REGS->MCSPI_CR = MCSPI_CR_FIFOEN_Msk;
</#if>

    /* MCSPI is by default in Slave Mode, disable mode fault detection */
    ${MCSPI_INSTANCE_NAME}_REGS->MCSPI_MR = MCSPI_MR_MODFDIS_Msk;

    /* Set up clock Polarity, data phase, Communication Width */
    ${MCSPI_INSTANCE_NAME}_REGS->MCSPI_CSR[0] = MCSPI_CSR_CPOL(${MCSPI_CSR0_CPOL}) | MCSPI_CSR_NCPHA(${MCSPI_CSR0_NCPHA}) | MCSPI_CSR_BITS${MCSPI_CSR0_BITS};

    ${MCSPI_INSTANCE_NAME?lower_case}Obj.rdInIndex = 0;
    ${MCSPI_INSTANCE_NAME?lower_case}Obj.wrOutIndex = 0;
    ${MCSPI_INSTANCE_NAME?lower_case}Obj.nWrBytes = 0;
    ${MCSPI_INSTANCE_NAME?lower_case}Obj.errorStatus = MCSPI_SLAVE_ERROR_NONE;
    ${MCSPI_INSTANCE_NAME?lower_case}Obj.callback = NULL ;
    ${MCSPI_INSTANCE_NAME?lower_case}Obj.transferIsBusy = false ;

    <#if MCSPIS_USE_BUSY_PIN == true>
    /* Set the Busy Pin to ready state */
    <#if MCSPIS_BUSY_PIN_LOGIC_LEVEL = "ACTIVE_HIGH">
    ${PLIB_NAME}_PinWrite((${PLIB_NAME}_PIN)${MCSPI_BUSY_PIN}, 0);
    <#else>
    ${PLIB_NAME}_PinWrite((${PLIB_NAME}_PIN)${MCSPI_BUSY_PIN}, 1);
    </#if>
    </#if>

    /* Enable Receive full and chip deselect interrupt */
    ${MCSPI_INSTANCE_NAME}_REGS->MCSPI_IER = (MCSPI_IER_RDRF_Msk | MCSPI_IER_NSSR_Msk);

    /* Enable ${MCSPI_INSTANCE_NAME} */
    ${MCSPI_INSTANCE_NAME}_REGS->MCSPI_CR = MCSPI_CR_SPIEN_Msk;
}

/* For 9-bit mode, the "size" must be specified in terms of 16-bit words */
size_t ${MCSPI_INSTANCE_NAME}_Read(void* pRdBuffer, size_t size)
{
    size_t rdSize = size;
    size_t rdInIndex = ${MCSPI_INSTANCE_NAME?lower_case}Obj.rdInIndex;

    if (rdSize > rdInIndex)
    {
        rdSize = rdInIndex;
    }
<#if MCSPI_CSR0_BITS = "_8_BIT">
    (void) memcpy(pRdBuffer, (void *)${MCSPI_INSTANCE_NAME}_ReadBuffer, rdSize);
<#else>
    (void) memcpy(pRdBuffer, (void *)${MCSPI_INSTANCE_NAME}_ReadBuffer, (rdSize << 1));
</#if>

    return rdSize;
}

/* For 9-bit mode, the "size" must be specified in terms of 16-bit words */
size_t ${MCSPI_INSTANCE_NAME}_Write(void* pWrBuffer, size_t size )
{
    uint32_t intState = ${MCSPI_INSTANCE_NAME}_REGS->MCSPI_IMR;
    size_t wrSize = size;
    uint32_t wrOutIndex = 0;

    ${MCSPI_INSTANCE_NAME}_REGS->MCSPI_IDR = intState;

    if (wrSize > ${MCSPI_INSTANCE_NAME}_WRITE_BUFFER_SIZE)
    {
        wrSize = ${MCSPI_INSTANCE_NAME}_WRITE_BUFFER_SIZE;
    }

<#if MCSPI_CSR0_BITS = "_8_BIT">
    (void) memcpy((void *)${MCSPI_INSTANCE_NAME}_WriteBuffer, pWrBuffer, wrSize);
<#else>
    (void) memcpy((void *)${MCSPI_INSTANCE_NAME}_WriteBuffer, pWrBuffer, (wrSize << 1));
</#if>

    ${MCSPI_INSTANCE_NAME?lower_case}Obj.nWrBytes = wrSize;

    while (((${MCSPI_INSTANCE_NAME}_REGS->MCSPI_SR & MCSPI_SR_TDRE_Msk) != 0U) && (wrOutIndex < wrSize))
    {
<#if MCSPI_CSR0_BITS = "_8_BIT">
        MCSPI_TDR_8BIT_REG = ${MCSPI_INSTANCE_NAME}_WriteBuffer[wrOutIndex];
        wrOutIndex++;
<#else>
        MCSPI_TDR_16BIT_REG = ${MCSPI_INSTANCE_NAME}_WriteBuffer[wrOutIndex];
        wrOutIndex++;
</#if>
    }

    ${MCSPI_INSTANCE_NAME?lower_case}Obj.wrOutIndex = wrOutIndex;

    /* Restore interrupt enable state and also enable TDRE interrupt */
    ${MCSPI_INSTANCE_NAME}_REGS->MCSPI_IER = (intState | MCSPI_IER_TDRE_Msk);

    return wrSize;
}

/* For 9-bit mode, the return value is in terms of 16-bit words */
size_t ${MCSPI_INSTANCE_NAME}_ReadCountGet(void)
{
    return ${MCSPI_INSTANCE_NAME?lower_case}Obj.rdInIndex;
}

/* For 9-bit mode, the return value is in terms of 16-bit words */
size_t ${MCSPI_INSTANCE_NAME}_ReadBufferSizeGet(void)
{
    return ${MCSPI_INSTANCE_NAME}_READ_BUFFER_SIZE;
}

/* For 9-bit mode, the return value is in terms of 16-bit words */
size_t ${MCSPI_INSTANCE_NAME}_WriteBufferSizeGet(void)
{
    return ${MCSPI_INSTANCE_NAME}_WRITE_BUFFER_SIZE;
}

void ${MCSPI_INSTANCE_NAME}_CallbackRegister(MCSPI_SLAVE_CALLBACK callBack, uintptr_t context )
{
    ${MCSPI_INSTANCE_NAME?lower_case}Obj.callback = callBack;

    ${MCSPI_INSTANCE_NAME?lower_case}Obj.context = context;
}

/* The status is returned busy during the period the chip-select remains asserted */
bool ${MCSPI_INSTANCE_NAME}_IsBusy(void)
{
    return ${MCSPI_INSTANCE_NAME?lower_case}Obj.transferIsBusy;
}

<#if MCSPIS_USE_BUSY_PIN == true>
/* Drive the GPIO pin to indicate to MCSPI Master that the slave is ready now */
void ${MCSPI_INSTANCE_NAME}_Ready(void)
{
<#if MCSPIS_BUSY_PIN_LOGIC_LEVEL = "ACTIVE_HIGH">
    ${PLIB_NAME}_PinWrite((${PLIB_NAME}_PIN)${MCSPI_BUSY_PIN}, 0);
<#else>
    ${PLIB_NAME}_PinWrite((${PLIB_NAME}_PIN)${MCSPI_BUSY_PIN}, 1);
</#if>
}
</#if>

MCSPI_SLAVE_ERROR ${MCSPI_INSTANCE_NAME}_ErrorGet(void)
{
    MCSPI_SLAVE_ERROR errorStatus = ${MCSPI_INSTANCE_NAME?lower_case}Obj.errorStatus;

    ${MCSPI_INSTANCE_NAME?lower_case}Obj.errorStatus = MCSPI_SLAVE_ERROR_NONE;

    return errorStatus;
}

void __attribute__((used)) ${MCSPI_INSTANCE_NAME}_InterruptHandler(void)
{
<#if MCSPI_CSR0_BITS = "_8_BIT">
    uint8_t txRxData = 0;
<#else>
    uint16_t txRxData = 0;
</#if>

    uint32_t statusFlags = ${MCSPI_INSTANCE_NAME}_REGS->MCSPI_SR;

    if ((statusFlags & MCSPI_SR_OVRES_Msk) != 0U)
    {
        /*OVRES flag is cleared on reading MCSPI SR*/

        /* Save the error to report it to application later */
        ${MCSPI_INSTANCE_NAME?lower_case}Obj.errorStatus = (MCSPI_SLAVE_ERROR)MCSPI_SR_OVRES_Msk;
    }

    if ((statusFlags & MCSPI_SR_RDRF_Msk) != 0U)
    {
        if (${MCSPI_INSTANCE_NAME?lower_case}Obj.transferIsBusy == false)
        {
            ${MCSPI_INSTANCE_NAME?lower_case}Obj.transferIsBusy = true;

            <#if MCSPIS_USE_BUSY_PIN == true && MCSPIS_BUSY_PIN_LOGIC_LEVEL = "ACTIVE_HIGH">
            ${PLIB_NAME}_PinWrite((${PLIB_NAME}_PIN)${MCSPI_BUSY_PIN}, 1);
            <#elseif MCSPIS_USE_BUSY_PIN == true && MCSPIS_BUSY_PIN_LOGIC_LEVEL = "ACTIVE_LOW">
            ${PLIB_NAME}_PinWrite((${PLIB_NAME}_PIN)${MCSPI_BUSY_PIN}, 0);
            </#if>
        }

        /* Note: statusFlags must be updated every time MCSPI_SR is read. This is because the NSSR flag
         * is cleared on MCSPI_SR read. If statusFlags is not updated, there is a possibility of missing
         * NSSR event flag.
         */

        uint32_t rdInIndex = ${MCSPI_INSTANCE_NAME?lower_case}Obj.rdInIndex;

        while (((statusFlags |= ${MCSPI_INSTANCE_NAME}_REGS->MCSPI_SR) & MCSPI_SR_RDRF_Msk) != 0U)
        {
<#if MCSPI_CSR0_BITS = "_8_BIT">
            /* Reading DATA register will also clear the RDRF flag */
            txRxData = MCSPI_TDR_8BIT_REG;
<#else>
            /* Reading DATA register will also clear the RDRF flag */
            txRxData = MCSPI_RDR_16BIT_REG;
</#if>

            if (${MCSPI_INSTANCE_NAME?lower_case}Obj.rdInIndex < ${MCSPI_INSTANCE_NAME}_READ_BUFFER_SIZE)
            {

                ${MCSPI_INSTANCE_NAME}_ReadBuffer[rdInIndex] = txRxData;
                rdInIndex++;
            }

            /* Only clear RDRF flag so as not to clear NSSR flag which may have been set */
            statusFlags &= ~MCSPI_SR_RDRF_Msk;
        }

        ${MCSPI_INSTANCE_NAME?lower_case}Obj.rdInIndex = rdInIndex;
    }

    if((statusFlags & MCSPI_SR_TDRE_Msk) != 0U)
    {
        uint32_t wrOutIndex = ${MCSPI_INSTANCE_NAME?lower_case}Obj.wrOutIndex;
        uint32_t nWrBytes = ${MCSPI_INSTANCE_NAME?lower_case}Obj.nWrBytes;

        while ((((statusFlags |= ${MCSPI_INSTANCE_NAME}_REGS->MCSPI_SR) & MCSPI_SR_TDRE_Msk) != 0U) && (wrOutIndex < nWrBytes))
        {
<#if MCSPI_CSR0_BITS = "_8_BIT">
            MCSPI_TDR_8BIT_REG = ${MCSPI_INSTANCE_NAME}_WriteBuffer[wrOutIndex];
            wrOutIndex++;
<#else>
            MCSPI_TDR_16BIT_REG = ${MCSPI_INSTANCE_NAME}_WriteBuffer[wrOutIndex];
            wrOutIndex++;
</#if>
            /* Only clear TDRE flag so as not to clear NSSR flag which may have been set */
            statusFlags &= ~MCSPI_SR_TDRE_Msk;
        }

        if (wrOutIndex >= nWrBytes)
        {
            /* Disable TDRE interrupt. The last byte sent by the master will be shifted out automatically */
            ${MCSPI_INSTANCE_NAME}_REGS->MCSPI_IDR = MCSPI_IDR_TDRE_Msk;
        }

        ${MCSPI_INSTANCE_NAME?lower_case}Obj.wrOutIndex = wrOutIndex;
    }

    if((statusFlags & MCSPI_SR_NSSR_Msk) != 0U)
    {
        /* NSSR flag is cleared on reading MCSPI SR */

        ${MCSPI_INSTANCE_NAME?lower_case}Obj.transferIsBusy = false;

        ${MCSPI_INSTANCE_NAME?lower_case}Obj.wrOutIndex = 0;
        ${MCSPI_INSTANCE_NAME?lower_case}Obj.nWrBytes = 0;

        if(${MCSPI_INSTANCE_NAME?lower_case}Obj.callback != NULL)
        {
            uintptr_t context = ${MCSPI_INSTANCE_NAME?lower_case}Obj.context;
            ${MCSPI_INSTANCE_NAME?lower_case}Obj.callback(context);
        }

        /* Clear the rdInIndex. Application must read the received data in the callback. */
        ${MCSPI_INSTANCE_NAME?lower_case}Obj.rdInIndex = 0;
    }
}