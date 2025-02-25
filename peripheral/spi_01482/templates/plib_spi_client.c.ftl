<#assign modeOptions = ["CLIENT_MODE","HOST_MODE"]>
<#assign clkPolarityOptions = ["IDLE_LOW_ACTIVE_HIGH","IDLE_HIGH_ACTIVE_LOW"]>
<#assign clkEdgeOptions = ["IDLE_TO_ACTIVE","ACTIVE_TO_IDLE"]>
<#assign hostClkselOptions = ["UPB_CLOCK","CLOCK_GEN_"+clkSrcGenNumber]>
/*******************************************************************************
  SPI PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${SPI_INSTANCE_NAME?lower_case}_client.c

  Summary:
    ${SPI_INSTANCE_NAME} Client Source File

  Description:
    This file has implementation of all the interfaces provided for particular
    SPI peripheral.

*******************************************************************************/

/*******************************************************************************
* Copyright (C) 2025 Microchip Technology Inc. and its subsidiaries.
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
<#assign SPI_CS_PIN = PLIB_NAME + "_PIN_" + SPIS_CS_PIN>
<#if SPIS_USE_BUSY_PIN == true>
<#assign SPI_BUSY_PIN = PLIB_NAME + "_PIN_" + SPIS_BUSY_PIN>
</#if>
</#if>
#include <string.h>
#include "plib_${SPI_INSTANCE_NAME?lower_case}_client.h"
#include "peripheral/${PLIB_NAME_LC}/plib_${PLIB_NAME_LC}.h"
<#if core.CoreSysIntFile == true>
#include "interrupts.h"
</#if>
// *****************************************************************************
// *****************************************************************************
// Section: ${SPI_INSTANCE_NAME} Slave Implementation
// *****************************************************************************
// *****************************************************************************
<#if SPIS_USE_BUSY_PIN == true>
#define ${SPI_INSTANCE_NAME}_BUSY_PIN                    ${SPI_BUSY_PIN}
</#if>
#define ${SPI_INSTANCE_NAME}_CS_PIN                      ${SPI_CS_PIN}

<#if SPI_SPICON_MODE == "0">

#define ${SPI_INSTANCE_NAME}_READ_BUFFER_SIZE            ${SPIS_RX_BUFFER_SIZE}
#define ${SPI_INSTANCE_NAME}_WRITE_BUFFER_SIZE           ${SPIS_TX_BUFFER_SIZE}

volatile static uint8_t ${SPI_INSTANCE_NAME}_ReadBuffer[${SPI_INSTANCE_NAME}_READ_BUFFER_SIZE];
volatile static uint8_t ${SPI_INSTANCE_NAME}_WriteBuffer[${SPI_INSTANCE_NAME}_WRITE_BUFFER_SIZE];

<#elseif SPI_SPICON_MODE == "1">

#define ${SPI_INSTANCE_NAME}_READ_BUFFER_SIZE            ${SPIS_RX_BUFFER_SIZE/2}
#define ${SPI_INSTANCE_NAME}_WRITE_BUFFER_SIZE           ${SPIS_TX_BUFFER_SIZE/2}

volatile static uint16_t ${SPI_INSTANCE_NAME}_ReadBuffer[${SPI_INSTANCE_NAME}_READ_BUFFER_SIZE];
volatile static uint16_t ${SPI_INSTANCE_NAME}_WriteBuffer[${SPI_INSTANCE_NAME}_WRITE_BUFFER_SIZE];

<#else>

#define ${SPI_INSTANCE_NAME}_READ_BUFFER_SIZE            ${SPIS_RX_BUFFER_SIZE/4}
#define ${SPI_INSTANCE_NAME}_WRITE_BUFFER_SIZE           ${SPIS_TX_BUFFER_SIZE/4}

volatile static uint32_t ${SPI_INSTANCE_NAME}_ReadBuffer[${SPI_INSTANCE_NAME}_READ_BUFFER_SIZE];
volatile static uint32_t ${SPI_INSTANCE_NAME}_WriteBuffer[${SPI_INSTANCE_NAME}_WRITE_BUFFER_SIZE];

</#if>

/* Global object to save SPI Exchange related data */
volatile static SPI_CLIENT_OBJECT ${SPI_INSTANCE_NAME?lower_case}Obj;

// *****************************************************************************
// *****************************************************************************
// Section: Macro Definitions
// *****************************************************************************
// *****************************************************************************

//SPI SPIxCON1 MODE options
<#list modeOptions as options>
#define ${SPI_INSTANCE_NAME}CON1_MSTEN_${options}          ((uint32_t)(_${SPI_INSTANCE_NAME}CON1_MSTEN_MASK & ((uint32_t)(${options_index}) << _${SPI_INSTANCE_NAME}CON1_MSTEN_POSITION))) 
</#list>

//SPI SPIxCON1 Clock Polarity options
<#list clkPolarityOptions as options>
#define ${SPI_INSTANCE_NAME}CON1_CKP_${options}           ((uint32_t)(_${SPI_INSTANCE_NAME}CON1_CKP_MASK & ((uint32_t)(${options_index}) << _${SPI_INSTANCE_NAME}CON1_CKP_POSITION))) 
</#list>

//SPI SPIxCON1 Clock Edge options
<#list clkEdgeOptions as options>
#define ${SPI_INSTANCE_NAME}CON1_CKE_${options}           ((uint32_t)(_${SPI_INSTANCE_NAME}CON1_CKE_MASK & ((uint32_t)(${options_index}) << _${SPI_INSTANCE_NAME}CON1_CKE_POSITION))) 
</#list>

//SPI SPIxCON1 Clock select options
<#list hostClkselOptions as options>
#define ${SPI_INSTANCE_NAME}CON1_MCLKEN_${options}           ((uint32_t)(_${SPI_INSTANCE_NAME}CON1_MCLKEN_MASK & ((uint32_t)(${options_index}) << _${SPI_INSTANCE_NAME}CON1_MCLKEN_POSITION))) 
</#list>

/* Forward declarations */
static void ${SPI_INSTANCE_NAME}_CS_Handler(GPIO_PIN pin, uintptr_t context);

static void mem_copy(volatile void* pDst, volatile void* pSrc, uint32_t nBytes)
{
    volatile uint8_t* pSource = (volatile uint8_t*)pSrc;
    volatile uint8_t* pDest = (volatile uint8_t*)pDst;

    for (uint32_t i = 0U; i < nBytes; i++)
    {
        pDest[i] = pSource[i];
    }
}

void ${SPI_INSTANCE_NAME}_Initialize ( void )
{
    /* Disable ${SPI_INSTANCE_NAME} Interrupts */
    ${errorInterruptEnableBit} = 0U;
    ${rxInterruptEnableBit} = 0U;
    ${txInterruptEnableBit} = 0U;

    /* STOP and Reset the SPI */
    ${SPI_INSTANCE_NAME}CON1 = 0x00U;

    /* Clear ${SPI_INSTANCE_NAME} Interrupt flags */
    ${errorInterruptFlagBit} = 0U;
    ${rxInterruptFlagBit} = 0U;
    ${txInterruptFlagBit} = 0U;

    ${SPI_INSTANCE_NAME}CON1 = (${SPI_INSTANCE_NAME}CON1_MSTEN_${modeOptions[SPI_CON1__MSTEN?number]}
            |${SPI_INSTANCE_NAME}CON1_CKP_${clkPolarityOptions[SPI_CON1__CKP?number]}
            |${SPI_INSTANCE_NAME}CON1_CKE_${clkEdgeOptions[SPI_CON1__CKE?number]}
            |${SPI_INSTANCE_NAME}CON1_MCLKEN_${hostClkselOptions[SPI_CON1__MCLKEN?number]}
            |_${SPI_INSTANCE_NAME}CON1_SSEN_MASK<#if SPI_CON1__SMP == "1">
            |_${SPI_INSTANCE_NAME}CON1_SMP_MASK</#if><#if SPI_CON1__ENHBUF == "1">
            |_${SPI_INSTANCE_NAME}CON1_ENHBUF_MASK</#if>);
            
    /* Enable generation of interrupt on receiver overflow */
    ${SPI_INSTANCE_NAME}IMSKbits.SPIROVEN = 1U;

    ${SPI_INSTANCE_NAME?lower_case}Obj.rdInIndex = 0U;
    ${SPI_INSTANCE_NAME?lower_case}Obj.wrOutIndex = 0U;
    ${SPI_INSTANCE_NAME?lower_case}Obj.nWrBytes = 0U;
    ${SPI_INSTANCE_NAME?lower_case}Obj.errorStatus = SPI_CLIENT_ERROR_NONE;
    ${SPI_INSTANCE_NAME?lower_case}Obj.callback = NULL ;
    ${SPI_INSTANCE_NAME?lower_case}Obj.transferIsBusy = false ;
    ${SPI_INSTANCE_NAME?lower_case}Obj.csInterruptPending = false;
    ${SPI_INSTANCE_NAME?lower_case}Obj.rxInterruptActive = false;

    <#if SPIS_USE_BUSY_PIN == true>
    /* Set the Busy Pin to ready state */
    <#if SPIS_BUSY_PIN_LOGIC_LEVEL == "ACTIVE_HIGH">
    ${PLIB_NAME}_PinWrite((${PLIB_NAME}_PIN)${SPI_INSTANCE_NAME}_BUSY_PIN, 0);
    <#else>
    ${PLIB_NAME}_PinWrite((${PLIB_NAME}_PIN)${SPI_INSTANCE_NAME}_BUSY_PIN, 1);
    </#if>
    </#if>

    /* Register callback and enable notifications on Chip Select logic level change */
    (void)GPIO_PinInterruptCallbackRegister(${SPI_INSTANCE_NAME}_CS_PIN, ${SPI_INSTANCE_NAME}_CS_Handler, 0U);
    GPIO_PinInterruptEnable(${SPI_INSTANCE_NAME}_CS_PIN);

    /* Enable watermark interrupt for one byte reception*/
    ${SPI_INSTANCE_NAME}IMSKbits.RXMSK = 1U;
    ${SPI_INSTANCE_NAME}IMSKbits.RXWIEN = 1U;
    ${SPI_INSTANCE_NAME}IMSKbits.SPITBEN = 1U;

    /* Enable ${SPI_INSTANCE_NAME} RX and Error Interrupts. TX interrupt will be enabled when a SPI write is submitted. */
    ${rxInterruptEnableBit} = 1U;
    ${errorInterruptEnableBit} = 1U;

    /* Enable ${SPI_INSTANCE_NAME} */
    ${SPI_INSTANCE_NAME}CON1bits.ON = 1U;
}

void ${SPI_INSTANCE_NAME}_Deinitialize ( void )
{
    /* Disable ${SPI_INSTANCE_NAME} Interrupts */
    ${errorInterruptEnableBit} = 0U;
    ${rxInterruptEnableBit} = 0U;
    ${txInterruptEnableBit} = 0U;

    /* STOP the SPI */
    ${SPI_INSTANCE_NAME}CON1bits.ON = 0U;

    /* Clear ${SPI_INSTANCE_NAME} Interrupt flags */
    ${errorInterruptFlagBit} = 0U;
    ${rxInterruptFlagBit} = 0U;
    ${txInterruptFlagBit} = 0U;

${regPorSet}
}

/* For 16-bit/32-bit mode, the "size" must be specified in terms of 16-bit/32-bit words */
size_t ${SPI_INSTANCE_NAME}_Read(void* pRdBuffer, size_t size)
{
    size_t rdSize = size;
    size_t rdInIndex = ${SPI_INSTANCE_NAME?lower_case}Obj.rdInIndex;

    if (rdSize > rdInIndex)
    {
        rdSize = rdInIndex;
    }

<#if SPI_SPICON_MODE == "0">
   (void) mem_copy(pRdBuffer, ${SPI_INSTANCE_NAME}_ReadBuffer, rdSize);
<#elseif SPI_SPICON_MODE == "1">
   (void) mem_copy(pRdBuffer, ${SPI_INSTANCE_NAME}_ReadBuffer, (rdSize << 1));
<#else>
   (void) mem_copy(pRdBuffer, ${SPI_INSTANCE_NAME}_ReadBuffer, (rdSize << 2));
</#if>

    return rdSize;
}

/* For 16-bit/32-bit mode, the "size" must be specified in terms of 16-bit/32-bit words */
size_t ${SPI_INSTANCE_NAME}_Write(void* pWrBuffer, size_t size )
{
    uint32_t wrSize = size;
    uint32_t wrOutIndex = 0U;

    ${txInterruptEnableBit} = 0U;

    if (wrSize > (uint32_t)${SPI_INSTANCE_NAME}_WRITE_BUFFER_SIZE)
    {
        wrSize = ${SPI_INSTANCE_NAME}_WRITE_BUFFER_SIZE;
    }

<#if SPI_SPICON_MODE == "0">
    (void) mem_copy(${SPI_INSTANCE_NAME}_WriteBuffer, pWrBuffer, wrSize);
<#elseif SPI_SPICON_MODE == "1">
    (void) mem_copy(${SPI_INSTANCE_NAME}_WriteBuffer, pWrBuffer, (wrSize << 1));
<#else>
    (void) mem_copy(${SPI_INSTANCE_NAME}_WriteBuffer, pWrBuffer, (wrSize << 2));
</#if>

    ${SPI_INSTANCE_NAME?lower_case}Obj.nWrBytes = wrSize;

    /* Fill up the FIFO as long as there are empty elements */
    while ((!(${SPI_INSTANCE_NAME}STAT & _${SPI_INSTANCE_NAME}STAT_SPITBF_MASK)) && (wrOutIndex < wrSize))
    {
        ${SPI_INSTANCE_NAME}BUF = ${SPI_INSTANCE_NAME}_WriteBuffer[wrOutIndex];
        wrOutIndex++;
    }

    ${SPI_INSTANCE_NAME?lower_case}Obj.wrOutIndex = wrOutIndex;

    /* Enable TX interrupt */
    ${txInterruptEnableBit} = 1U;

    return wrSize;
}

/* For 16-bit/32-bit mode, the return value is in terms of 16-bit/32-bit words */
size_t ${SPI_INSTANCE_NAME}_ReadCountGet(void)
{
    return ${SPI_INSTANCE_NAME?lower_case}Obj.rdInIndex;
}

/* For 16-bit/32-bit mode, the return value is in terms of 16-bit/32-bit words */
size_t ${SPI_INSTANCE_NAME}_ReadBufferSizeGet(void)
{
    return ${SPI_INSTANCE_NAME}_READ_BUFFER_SIZE;
}

/* For 16-bit/32-bit mode, the return value is in terms of 16-bit/32-bit words */
size_t ${SPI_INSTANCE_NAME}_WriteBufferSizeGet(void)
{
    return ${SPI_INSTANCE_NAME}_WRITE_BUFFER_SIZE;
}

void ${SPI_INSTANCE_NAME}_CallbackRegister(SPI_CLIENT_CALLBACK callBack, uintptr_t context )
{
    ${SPI_INSTANCE_NAME?lower_case}Obj.callback = callBack;

    ${SPI_INSTANCE_NAME?lower_case}Obj.context = context;
}

/* The status is returned as busy when CS is asserted */
bool ${SPI_INSTANCE_NAME}_IsBusy(void)
{
    return ${SPI_INSTANCE_NAME?lower_case}Obj.transferIsBusy;
}

<#if SPIS_USE_BUSY_PIN == true>
/* Drive the GPIO pin to indicate to SPI Master that the client is ready now */
void ${SPI_INSTANCE_NAME}_Ready(void)
{
<#if SPIS_BUSY_PIN_LOGIC_LEVEL = "ACTIVE_HIGH">
    ${PLIB_NAME}_PinWrite((${PLIB_NAME}_PIN)${SPI_INSTANCE_NAME}_BUSY_PIN, 0);
<#else>
    ${PLIB_NAME}_PinWrite((${PLIB_NAME}_PIN)${SPI_INSTANCE_NAME}_BUSY_PIN, 1);
</#if>
}
</#if>

SPI_CLIENT_ERROR ${SPI_INSTANCE_NAME}_ErrorGet(void)
{
    SPI_CLIENT_ERROR errorStatus = ${SPI_INSTANCE_NAME?lower_case}Obj.errorStatus;

    ${SPI_INSTANCE_NAME?lower_case}Obj.errorStatus = SPI_CLIENT_ERROR_NONE;

    return errorStatus;
}

static void __attribute__((used)) ${SPI_INSTANCE_NAME}_CS_Handler(GPIO_PIN pin, uintptr_t context)
{
    <#if SPIS_CS_PIN_LOGIC_LEVEL == "ACTIVE_LOW">
    bool activeState = false;
    <#else>
    bool activeState = true;
    </#if>

    if (${PLIB_NAME}_PinRead((${PLIB_NAME}_PIN)${SPI_INSTANCE_NAME}_CS_PIN) == activeState)
    {
        /* CS is asserted */
        ${SPI_INSTANCE_NAME?lower_case}Obj.transferIsBusy = true;

<#if SPIS_USE_BUSY_PIN == true && SPIS_BUSY_PIN_LOGIC_LEVEL == "ACTIVE_HIGH">
        /* Drive busy line to active state */
        ${PLIB_NAME}_PinWrite((${PLIB_NAME}_PIN)${SPI_INSTANCE_NAME}_BUSY_PIN, 1);
<#elseif SPIS_USE_BUSY_PIN == true && SPIS_BUSY_PIN_LOGIC_LEVEL == "ACTIVE_LOW">
        /* Drive busy line to active state */
        ${PLIB_NAME}_PinWrite((${PLIB_NAME}_PIN)${SPI_INSTANCE_NAME}_BUSY_PIN, 0);
</#if>
    }
    else
    {
        /* Give application callback only if RX interrupt is not preempted and RX interrupt is not pending to be serviced */

        bool rxInterruptActive = ${SPI_INSTANCE_NAME?lower_case}Obj.rxInterruptActive;

        if ((${rxInterruptFlagBit} == 0U) && (rxInterruptActive == false))
        {
            /* CS is de-asserted */
            ${SPI_INSTANCE_NAME?lower_case}Obj.transferIsBusy = false;

            ${SPI_INSTANCE_NAME?lower_case}Obj.wrOutIndex = 0U;
            ${SPI_INSTANCE_NAME?lower_case}Obj.nWrBytes = 0U;

            if(${SPI_INSTANCE_NAME?lower_case}Obj.callback != NULL)
            {
                uintptr_t context_val = ${SPI_INSTANCE_NAME?lower_case}Obj.context;

                ${SPI_INSTANCE_NAME?lower_case}Obj.callback(context_val);
            }

            /* Clear the read index. Application must read out the data by calling ${SPI_INSTANCE_NAME}_Read API in the callback */
            ${SPI_INSTANCE_NAME?lower_case}Obj.rdInIndex = 0U;
        }
        else
        {
            /* If CS interrupt is serviced by either preempting the RX interrupt or RX interrupt is pending to be serviced,
             * then delegate the responsibility of giving application callback to the RX interrupt handler */

            ${SPI_INSTANCE_NAME?lower_case}Obj.csInterruptPending = true;
        }
    }
}

void __attribute__((used)) ${errorIsrHandlerName} (void)
{
    ${SPI_INSTANCE_NAME?lower_case}Obj.errorStatus =(${SPI_INSTANCE_NAME}STAT & _${SPI_INSTANCE_NAME}STAT_SPIROV_MASK);

    /* Clear the receive overflow flag */
    ${SPI_INSTANCE_NAME}STATbits.SPIROV = 0U;

    ${errorInterruptFlagBit} = 0U;
}

void __attribute__((used)) ${txIsrHandlerName} (void)
{
    size_t wrOutIndex = ${SPI_INSTANCE_NAME?lower_case}Obj.wrOutIndex;
    size_t nWrBytes = ${SPI_INSTANCE_NAME?lower_case}Obj.nWrBytes;

    /* Fill up the FIFO as long as there are empty elements */
    while ((!(${SPI_INSTANCE_NAME}STAT & _${SPI_INSTANCE_NAME}STAT_SPITBF_MASK)) && (wrOutIndex < nWrBytes))
    {
        ${SPI_INSTANCE_NAME}BUF = ${SPI_INSTANCE_NAME}_WriteBuffer[wrOutIndex];
        wrOutIndex++;
    }

    ${SPI_INSTANCE_NAME?lower_case}Obj.wrOutIndex = wrOutIndex;

    /* Clear the transmit interrupt flag */
    ${txInterruptFlagBit} = 0U;

    if (${SPI_INSTANCE_NAME?lower_case}Obj.wrOutIndex == nWrBytes)
    {
        /* Nothing to transmit. Disable transmit interrupt. The last byte sent by the master will be shifted out automatically*/
        ${txInterruptEnableBit} = 0U;
    }
}

void __attribute__((used)) ${rxIsrHandlerName} (void)
{
    uint32_t receivedData = 0;

    ${SPI_INSTANCE_NAME?lower_case}Obj.rxInterruptActive = true;

    size_t rdInIndex = ${SPI_INSTANCE_NAME?lower_case}Obj.rdInIndex;

    while (!(${SPI_INSTANCE_NAME}STAT & _${SPI_INSTANCE_NAME}STAT_SPIRBE_MASK))
    {
        /* Receive buffer is not empty. Read the received data. */
        receivedData = ${SPI_INSTANCE_NAME}BUF;

        if (rdInIndex < (uint32_t)${SPI_INSTANCE_NAME}_READ_BUFFER_SIZE)
        {
            ${SPI_INSTANCE_NAME}_ReadBuffer[rdInIndex] = (uint8_t)receivedData;
            rdInIndex++;
        }
    }

    ${SPI_INSTANCE_NAME?lower_case}Obj.rdInIndex = rdInIndex;

    /* Clear the receive interrupt flag */
    ${rxInterruptFlagBit} = 0U;

    ${SPI_INSTANCE_NAME?lower_case}Obj.rxInterruptActive = false;

    /* Check if CS interrupt occured before the RX interrupt and that CS interrupt delegated the responsibility to give
     * application callback to the RX interrupt */

    if (${SPI_INSTANCE_NAME?lower_case}Obj.csInterruptPending == true)
    {
        ${SPI_INSTANCE_NAME?lower_case}Obj.csInterruptPending = false;
        ${SPI_INSTANCE_NAME?lower_case}Obj.transferIsBusy = false;

        ${SPI_INSTANCE_NAME?lower_case}Obj.wrOutIndex = 0U;
        ${SPI_INSTANCE_NAME?lower_case}Obj.nWrBytes = 0U;

        if(${SPI_INSTANCE_NAME?lower_case}Obj.callback != NULL)
        {
            uintptr_t context = ${SPI_INSTANCE_NAME?lower_case}Obj.context;

            ${SPI_INSTANCE_NAME?lower_case}Obj.callback(context);
        }

        /* Clear the read index. Application must read out the data by calling ${SPI_INSTANCE_NAME}_Read API in the callback */
        ${SPI_INSTANCE_NAME?lower_case}Obj.rdInIndex = 0U;
    }
}
