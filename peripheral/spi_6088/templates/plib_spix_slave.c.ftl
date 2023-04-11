/*******************************************************************************
  SPI PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${SPI_INSTANCE_NAME?lower_case}_slave.c

  Summary:
    ${SPI_INSTANCE_NAME} Slave Source File

  Description:
    This file has implementation of all the interfaces provided for particular
    SPI peripheral.

*******************************************************************************/

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
<#if core.PORT_API_PREFIX??>
<#assign PLIB_NAME  = core.PORT_API_PREFIX?string>
<#assign PLIB_NAME_LC  = core.PORT_API_PREFIX?lower_case>
<#assign SPI_BUSY_PIN = PLIB_NAME + "_PIN_" + SPIS_BUSY_PIN>
</#if>

#include "plib_${SPI_INSTANCE_NAME?lower_case}_slave.h"
<#if SPIS_USE_BUSY_PIN == true>
#include "peripheral/${PLIB_NAME_LC}/plib_${PLIB_NAME_LC}.h"
</#if>
<#if core.CoreSysIntFile == true>
#include "interrupts.h"
</#if>
#include <string.h>

<#if SPI_CSR0_BITS = "_8_BIT">
#define ${SPI_INSTANCE_NAME}_READ_BUFFER_SIZE            ${SPIS_RX_BUFFER_SIZE}U
#define ${SPI_INSTANCE_NAME}_WRITE_BUFFER_SIZE           ${SPIS_TX_BUFFER_SIZE}U

volatile static uint8_t ${SPI_INSTANCE_NAME}_ReadBuffer[${SPI_INSTANCE_NAME}_READ_BUFFER_SIZE];
volatile static uint8_t ${SPI_INSTANCE_NAME}_WriteBuffer[${SPI_INSTANCE_NAME}_WRITE_BUFFER_SIZE];

<#else>

#define ${SPI_INSTANCE_NAME}_READ_BUFFER_SIZE            ${SPIS_RX_BUFFER_SIZE/2}U
#define ${SPI_INSTANCE_NAME}_WRITE_BUFFER_SIZE           ${SPIS_TX_BUFFER_SIZE/2}U

volatile static uint16_t ${SPI_INSTANCE_NAME}_ReadBuffer[${SPI_INSTANCE_NAME}_READ_BUFFER_SIZE];
volatile static uint16_t ${SPI_INSTANCE_NAME}_WriteBuffer[${SPI_INSTANCE_NAME}_WRITE_BUFFER_SIZE];
</#if>

#define NOP asm("nop")


#define SPI_TDR_8BIT_REG      (*(volatile uint8_t* const)((${SPI_INSTANCE_NAME}_BASE_ADDRESS + SPI_TDR_REG_OFST)))

#define SPI_TDR_9BIT_REG      (*(volatile uint16_t* const)((${SPI_INSTANCE_NAME}_BASE_ADDRESS + SPI_TDR_REG_OFST)))



#define SPI_RDR_8BIT_REG      (*(volatile uint8_t* const)((${SPI_INSTANCE_NAME}_BASE_ADDRESS + SPI_RDR_REG_OFST)))

#define SPI_RDR_9BIT_REG      (*(volatile uint16_t* const)((${SPI_INSTANCE_NAME}_BASE_ADDRESS + SPI_RDR_REG_OFST)))
// *****************************************************************************
// *****************************************************************************
// Section: ${SPI_INSTANCE_NAME} Implementation
// *****************************************************************************
// *****************************************************************************

/* Global object to save SPI Exchange related data */
volatile static SPI_SLAVE_OBJECT ${SPI_INSTANCE_NAME?lower_case}Obj;

static void mem_copy(volatile void* pDst, volatile void* pSrc, uint32_t nBytes)
{
    volatile uint8_t* pSource = (volatile uint8_t*)pSrc;
    volatile uint8_t* pDest = (volatile uint8_t*)pDst;

    for (uint32_t i = 0U; i < nBytes; i++)
    {
        pDest[i] = pSource[i];
    }
}

void ${SPI_INSTANCE_NAME}_Initialize( void )
{
    /* Disable and Reset the SPI*/
    ${SPI_INSTANCE_NAME}_REGS->SPI_CR = SPI_CR_SPIDIS_Msk | SPI_CR_SWRST_Msk;

<#if SPI_FIFO_ENABLE == true>
    /* Enable FIFO support */
    ${SPI_INSTANCE_NAME}_REGS->SPI_CR = SPI_CR_FIFOEN_Msk;
</#if>

    /* SPI is by default in Slave Mode, disable mode fault detection */
    ${SPI_INSTANCE_NAME}_REGS->SPI_MR = SPI_MR_MODFDIS_Msk;

    /* Set up clock Polarity, data phase, Communication Width */
    ${SPI_INSTANCE_NAME}_REGS->SPI_CSR[0] = SPI_CSR_CPOL_${SPI_CSR0_CPOL} | SPI_CSR_NCPHA_${SPI_CSR0_NCPHA} | SPI_CSR_BITS${SPI_CSR0_BITS};

    ${SPI_INSTANCE_NAME?lower_case}Obj.rdInIndex = 0;
    ${SPI_INSTANCE_NAME?lower_case}Obj.wrOutIndex = 0;
    ${SPI_INSTANCE_NAME?lower_case}Obj.nWrBytes = 0;
    ${SPI_INSTANCE_NAME?lower_case}Obj.errorStatus = SPI_SLAVE_ERROR_NONE;
    ${SPI_INSTANCE_NAME?lower_case}Obj.callback = NULL ;
    ${SPI_INSTANCE_NAME?lower_case}Obj.transferIsBusy = false ;

    <#if SPIS_USE_BUSY_PIN == true>
    /* Set the Busy Pin to ready state */
    <#if SPIS_BUSY_PIN_LOGIC_LEVEL = "ACTIVE_HIGH">
    ${PLIB_NAME}_PinWrite((${PLIB_NAME}_PIN)${SPI_BUSY_PIN}, 0);
    <#else>
    ${PLIB_NAME}_PinWrite((${PLIB_NAME}_PIN)${SPI_BUSY_PIN}, 1);
    </#if>
    </#if>

    /* Enable Receive full and chip deselect interrupt */
    ${SPI_INSTANCE_NAME}_REGS->SPI_IER = (SPI_IER_RDRF_Msk | SPI_IER_NSSR_Msk);

    /* Enable ${SPI_INSTANCE_NAME} */
    ${SPI_INSTANCE_NAME}_REGS->SPI_CR = SPI_CR_SPIEN_Msk;
}

/* For 9-bit mode, the "size" must be specified in terms of 16-bit words */
size_t ${SPI_INSTANCE_NAME}_Read(void* pRdBuffer, size_t size)
{
    size_t rdSize = size;
    size_t rdInIndex = ${SPI_INSTANCE_NAME?lower_case}Obj.rdInIndex;

    if (rdSize > rdInIndex)
    {
        rdSize = rdInIndex;
    }
<#if SPI_CSR0_BITS = "_8_BIT">
    (void) mem_copy(pRdBuffer, (void*)${SPI_INSTANCE_NAME}_ReadBuffer, rdSize);
<#else>
    (void) mem_copy(pRdBuffer, (void*)${SPI_INSTANCE_NAME}_ReadBuffer, (rdSize << 1));
</#if>

    return rdSize;
}

/* For 9-bit mode, the "size" must be specified in terms of 16-bit words */
size_t ${SPI_INSTANCE_NAME}_Write(void* pWrBuffer, size_t size )
{
    uint32_t intState = ${SPI_INSTANCE_NAME}_REGS->SPI_IMR;
    size_t wrSize = size;
    uint32_t wrOutIndex = 0;

    ${SPI_INSTANCE_NAME}_REGS->SPI_IDR = intState;

    if (wrSize > ${SPI_INSTANCE_NAME}_WRITE_BUFFER_SIZE)
    {
        wrSize = ${SPI_INSTANCE_NAME}_WRITE_BUFFER_SIZE;
    }

<#if SPI_CSR0_BITS = "_8_BIT">
   (void) mem_copy((void*)${SPI_INSTANCE_NAME}_WriteBuffer, pWrBuffer, wrSize);
<#else>
    (void) mem_copy((void*)${SPI_INSTANCE_NAME}_WriteBuffer, pWrBuffer, (wrSize << 1));
</#if>

    ${SPI_INSTANCE_NAME?lower_case}Obj.nWrBytes = wrSize;

    while (((${SPI_INSTANCE_NAME}_REGS->SPI_SR & SPI_SR_TDRE_Msk) != 0U) && (wrOutIndex < wrSize))
    {
<#if SPI_CSR0_BITS = "_8_BIT">
        SPI_TDR_8BIT_REG = ${SPI_INSTANCE_NAME}_WriteBuffer[wrOutIndex];
        wrOutIndex++;
<#else>
        SPI_TDR_9BIT_REG = ${SPI_INSTANCE_NAME}_WriteBuffer[wrOutIndex];
        wrOutIndex++;
</#if>
        NOP;
    }

    ${SPI_INSTANCE_NAME?lower_case}Obj.wrOutIndex = wrOutIndex;

    /* Restore interrupt enable state and also enable TDRE interrupt */
    ${SPI_INSTANCE_NAME}_REGS->SPI_IER = (intState | SPI_IER_TDRE_Msk);

    return wrSize;
}

/* For 9-bit mode, the return value is in terms of 16-bit words */
size_t ${SPI_INSTANCE_NAME}_ReadCountGet(void)
{
    return ${SPI_INSTANCE_NAME?lower_case}Obj.rdInIndex;
}

/* For 9-bit mode, the return value is in terms of 16-bit words */
size_t ${SPI_INSTANCE_NAME}_ReadBufferSizeGet(void)
{
    return ${SPI_INSTANCE_NAME}_READ_BUFFER_SIZE;
}

/* For 9-bit mode, the return value is in terms of 16-bit words */
size_t ${SPI_INSTANCE_NAME}_WriteBufferSizeGet(void)
{
    return ${SPI_INSTANCE_NAME}_WRITE_BUFFER_SIZE;
}

void ${SPI_INSTANCE_NAME}_CallbackRegister(SPI_SLAVE_CALLBACK callBack, uintptr_t context )
{
    ${SPI_INSTANCE_NAME?lower_case}Obj.callback = callBack;

    ${SPI_INSTANCE_NAME?lower_case}Obj.context = context;
}

/* The status is returned busy during the period the chip-select remains asserted */
bool ${SPI_INSTANCE_NAME}_IsBusy(void)
{
    return ${SPI_INSTANCE_NAME?lower_case}Obj.transferIsBusy;
}

<#if SPIS_USE_BUSY_PIN == true>
/* Drive the GPIO pin to indicate to SPI Master that the slave is ready now */
void ${SPI_INSTANCE_NAME}_Ready(void)
{
<#if SPIS_BUSY_PIN_LOGIC_LEVEL = "ACTIVE_HIGH">
    ${PLIB_NAME}_PinWrite((${PLIB_NAME}_PIN)${SPI_BUSY_PIN}, 0);
<#else>
    ${PLIB_NAME}_PinWrite((${PLIB_NAME}_PIN)${SPI_BUSY_PIN}, 1);
</#if>
}
</#if>

SPI_SLAVE_ERROR ${SPI_INSTANCE_NAME}_ErrorGet(void)
{
    SPI_SLAVE_ERROR errorStatus = ${SPI_INSTANCE_NAME?lower_case}Obj.errorStatus;

    ${SPI_INSTANCE_NAME?lower_case}Obj.errorStatus = SPI_SLAVE_ERROR_NONE;

    return errorStatus;
}

void __attribute__((used)) ${SPI_INSTANCE_NAME}_InterruptHandler(void)
{
<#if SPI_CSR0_BITS = "_8_BIT">
    uint8_t txRxData = 0;
<#else>
    uint16_t txRxData = 0;
</#if>

    volatile uint32_t statusFlags = ${SPI_INSTANCE_NAME}_REGS->SPI_SR;

    if ((statusFlags & SPI_SR_OVRES_Msk)  != 0U)
    {
        /*OVRES flag is cleared on reading SPI SR*/

        /* Save the error to report it to application later */
        ${SPI_INSTANCE_NAME?lower_case}Obj.errorStatus = SPI_SR_OVRES_Msk;
    }

    if((statusFlags & SPI_SR_RDRF_Msk) != 0U)
    {
        if (${SPI_INSTANCE_NAME?lower_case}Obj.transferIsBusy == false)
        {
            ${SPI_INSTANCE_NAME?lower_case}Obj.transferIsBusy = true;

            <#if SPIS_USE_BUSY_PIN == true && SPIS_BUSY_PIN_LOGIC_LEVEL = "ACTIVE_HIGH">
            ${PLIB_NAME}_PinWrite((${PLIB_NAME}_PIN)${SPI_BUSY_PIN}, 1);
            <#elseif SPIS_USE_BUSY_PIN == true && SPIS_BUSY_PIN_LOGIC_LEVEL = "ACTIVE_LOW">
            ${PLIB_NAME}_PinWrite((${PLIB_NAME}_PIN)${SPI_BUSY_PIN}, 0);
            </#if>
        }

        /* Note: statusFlags must be updated every time SPI_SR is read. This is because the NSSR flag
         * is cleared on SPI_SR read. If statusFlags is not updated, there is a possibility of missing
         * NSSR event flag.
         */
        uint32_t rdInIndex = ${SPI_INSTANCE_NAME?lower_case}Obj.rdInIndex;

        while (((statusFlags |= ${SPI_INSTANCE_NAME}_REGS->SPI_SR)  & SPI_SR_RDRF_Msk) != 0U)
        {
<#if SPI_CSR0_BITS = "_8_BIT">
            /* Reading DATA register will also clear the RDRF flag */
            txRxData = SPI_RDR_8BIT_REG;
<#else>
            /* Reading DATA register will also clear the RDRF flag */
            txRxData = SPI_RDR_9BIT_REG;
</#if>

            if (rdInIndex < ${SPI_INSTANCE_NAME}_READ_BUFFER_SIZE)
            {
                ${SPI_INSTANCE_NAME}_ReadBuffer[rdInIndex] = txRxData;
                rdInIndex++;
            }

            /* Only clear RDRF flag so as not to clear NSSR flag which may have been set */
            statusFlags &= ~SPI_SR_RDRF_Msk;
        }

        ${SPI_INSTANCE_NAME?lower_case}Obj.rdInIndex = rdInIndex;
    }

    if((statusFlags & SPI_SR_TDRE_Msk) != 0U)
    {
        uint32_t wrOutIndex = ${SPI_INSTANCE_NAME?lower_case}Obj.wrOutIndex;
        uint32_t nWrBytes = ${SPI_INSTANCE_NAME?lower_case}Obj.nWrBytes;

        while ((((statusFlags |= ${SPI_INSTANCE_NAME}_REGS->SPI_SR) & SPI_SR_TDRE_Msk) != 0U) && (wrOutIndex < nWrBytes))
        {
<#if SPI_CSR0_BITS = "_8_BIT">
            SPI_TDR_8BIT_REG = ${SPI_INSTANCE_NAME}_WriteBuffer[wrOutIndex];
            wrOutIndex++;
<#else>
            SPI_TDR_9BIT_REG = ${SPI_INSTANCE_NAME}_WriteBuffer[wrOutIndex];
            wrOutIndex++;
</#if>
            /* Only clear TDRE flag so as not to clear NSSR flag which may have been set */
            statusFlags &= ~SPI_SR_TDRE_Msk;
        }

        ${SPI_INSTANCE_NAME?lower_case}Obj.wrOutIndex = wrOutIndex;

        if (wrOutIndex >= ${SPI_INSTANCE_NAME?lower_case}Obj.nWrBytes)
        {
            /* Disable TDRE interrupt. The last byte sent by the master will be shifted out automatically */
            ${SPI_INSTANCE_NAME}_REGS->SPI_IDR = SPI_IDR_TDRE_Msk;
        }
    }

    if((statusFlags & SPI_SR_NSSR_Msk) != 0U)
    {
        /* NSSR flag is cleared on reading SPI SR */

        ${SPI_INSTANCE_NAME?lower_case}Obj.transferIsBusy = false;

        ${SPI_INSTANCE_NAME?lower_case}Obj.wrOutIndex = 0;
        ${SPI_INSTANCE_NAME?lower_case}Obj.nWrBytes = 0;

        if(${SPI_INSTANCE_NAME?lower_case}Obj.callback != NULL)
        {
            uintptr_t context = ${SPI_INSTANCE_NAME?lower_case}Obj.context;

            ${SPI_INSTANCE_NAME?lower_case}Obj.callback(context);
        }

        /* Clear the rdInIndex. Application must read the received data in the callback. */
        ${SPI_INSTANCE_NAME?lower_case}Obj.rdInIndex = 0;
    }
}