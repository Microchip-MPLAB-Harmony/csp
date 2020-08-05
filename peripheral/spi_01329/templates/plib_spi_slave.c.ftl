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
* Copyright (C) 2019-2020 Microchip Technology Inc. and its subsidiaries.
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
#include "plib_${SPI_INSTANCE_NAME?lower_case}_slave.h"
#include "peripheral/${PLIB_NAME_LC}/plib_${PLIB_NAME_LC}.h"
#include <string.h>
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

static uint8_t ${SPI_INSTANCE_NAME}_ReadBuffer[${SPI_INSTANCE_NAME}_READ_BUFFER_SIZE];
static uint8_t ${SPI_INSTANCE_NAME}_WriteBuffer[${SPI_INSTANCE_NAME}_WRITE_BUFFER_SIZE];

<#elseif SPI_SPICON_MODE == "1">

#define ${SPI_INSTANCE_NAME}_READ_BUFFER_SIZE            ${SPIS_RX_BUFFER_SIZE/2}
#define ${SPI_INSTANCE_NAME}_WRITE_BUFFER_SIZE           ${SPIS_TX_BUFFER_SIZE/2}

static uint16_t ${SPI_INSTANCE_NAME}_ReadBuffer[${SPI_INSTANCE_NAME}_READ_BUFFER_SIZE];
static uint16_t ${SPI_INSTANCE_NAME}_WriteBuffer[${SPI_INSTANCE_NAME}_WRITE_BUFFER_SIZE];

<#else>

#define ${SPI_INSTANCE_NAME}_READ_BUFFER_SIZE            ${SPIS_RX_BUFFER_SIZE/4}
#define ${SPI_INSTANCE_NAME}_WRITE_BUFFER_SIZE           ${SPIS_TX_BUFFER_SIZE/4}

static uint32_t ${SPI_INSTANCE_NAME}_ReadBuffer[${SPI_INSTANCE_NAME}_READ_BUFFER_SIZE];
static uint32_t ${SPI_INSTANCE_NAME}_WriteBuffer[${SPI_INSTANCE_NAME}_WRITE_BUFFER_SIZE];

</#if>

/* Global object to save SPI Exchange related data */
SPI_SLAVE_OBJECT ${SPI_INSTANCE_NAME?lower_case}Obj;

#define ${SPI_INSTANCE_NAME}_CON_CKP                        (${SPI_SPICON_CLK_POL} << _${SPI_INSTANCE_NAME}CON_CKP_POSITION)
#define ${SPI_INSTANCE_NAME}_CON_CKE                        (${SPI_SPICON_CLK_PH} << _${SPI_INSTANCE_NAME}CON_CKE_POSITION)
#define ${SPI_INSTANCE_NAME}_CON_MODE_32_MODE_16            (${SPI_SPICON_MODE} << _${SPI_INSTANCE_NAME}CON_MODE16_POSITION)
#define ${SPI_INSTANCE_NAME}_CON_ENHBUF                     (1 << _${SPI_INSTANCE_NAME}CON_ENHBUF_POSITION)
#define ${SPI_INSTANCE_NAME}_CON_STXISEL                    (3 << _${SPI_INSTANCE_NAME}CON_STXISEL_POSITION)
#define ${SPI_INSTANCE_NAME}_CON_SRXISEL                    (1 << _${SPI_INSTANCE_NAME}CON_SRXISEL_POSITION)

#define ${SPI_INSTANCE_NAME}_ENABLE_RX_INT()                ${SPI_RX_IEC_REG}SET = ${SPI_RX_IEC_REG_MASK}
#define ${SPI_INSTANCE_NAME}_CLEAR_RX_INT_FLAG()            ${SPI_RX_IFS_REG}CLR = ${SPI_RX_IFS_REG_MASK}

#define ${SPI_INSTANCE_NAME}_DISABLE_TX_INT()               ${SPI_TX_IEC_REG}CLR = ${SPI_TX_IEC_REG_MASK}
#define ${SPI_INSTANCE_NAME}_ENABLE_TX_INT()                ${SPI_TX_IEC_REG}SET = ${SPI_TX_IEC_REG_MASK}
#define ${SPI_INSTANCE_NAME}_CLEAR_TX_INT_FLAG()            ${SPI_TX_IFS_REG}CLR = ${SPI_TX_IFS_REG_MASK}

#define ${SPI_INSTANCE_NAME}_ENABLE_ERR_INT()               ${SPI_FLT_IEC_REG}SET = ${SPI_FLT_IEC_REG_MASK}
#define ${SPI_INSTANCE_NAME}_CLEAR_ERR_INT_FLAG()           ${SPI_FLT_IEC_REG}CLR = ${SPI_FLT_IEC_REG_MASK}

/* Forward declarations */
static void ${SPI_INSTANCE_NAME}_CS_Handler(GPIO_PIN pin, uintptr_t context);

void ${SPI_INSTANCE_NAME}_Initialize ( void )
{
    /* Disable ${SPI_INSTANCE_NAME} Interrupts */
    ${SPI_FLT_IEC_REG}CLR = ${SPI_FLT_IEC_REG_MASK};
    ${SPI_RX_IEC_REG}CLR = ${SPI_RX_IEC_REG_MASK};
    ${SPI_TX_IEC_REG}CLR = ${SPI_TX_IEC_REG_MASK};

    /* STOP and Reset the SPI */
    ${SPI_INSTANCE_NAME}CON = 0;

    /* Clear ${SPI_INSTANCE_NAME} Interrupt flags */
    ${SPI_FLT_IFS_REG}CLR = ${SPI_FLT_IFS_REG_MASK};
    ${SPI_RX_IFS_REG}CLR = ${SPI_RX_IFS_REG_MASK};
    ${SPI_TX_IFS_REG}CLR = ${SPI_TX_IFS_REG_MASK};

    /* CLear the receiver overflow error flag */
    ${SPI_INSTANCE_NAME}STATCLR = _${SPI_INSTANCE_NAME}STAT_SPIROV_MASK;

    /*
    SRXISEL = 1 (Receive buffer is not empty)
    STXISEL = 3 (Transmit buffer is not full)
    MSTEN = ${SPI_MSTR_MODE_EN}
    CKP = ${SPI_SPICON_CLK_POL}
    CKE = ${SPI_SPICON_CLK_PH}
    MODE<32,16> = ${SPI_SPICON_MODE}
    ENHBUF = 1
    */

    ${SPI_INSTANCE_NAME}CONSET = (${SPI_INSTANCE_NAME}_CON_ENHBUF | ${SPI_INSTANCE_NAME}_CON_MODE_32_MODE_16 | ${SPI_INSTANCE_NAME}_CON_CKE | ${SPI_INSTANCE_NAME}_CON_CKP | ${SPI_INSTANCE_NAME}_CON_STXISEL | ${SPI_INSTANCE_NAME}_CON_SRXISEL);

    <#if SPI_CON2_SPIROVEN??>
    /* Enable generation of interrupt on receiver overflow */
    ${SPI_INSTANCE_NAME}CON2SET = _${SPI_INSTANCE_NAME}CON2_SPIROVEN_MASK;
    </#if>

    ${SPI_INSTANCE_NAME?lower_case}Obj.rdInIndex = 0;
    ${SPI_INSTANCE_NAME?lower_case}Obj.wrOutIndex = 0;
    ${SPI_INSTANCE_NAME?lower_case}Obj.nWrBytes = 0;
    ${SPI_INSTANCE_NAME?lower_case}Obj.errorStatus = SPI_SLAVE_ERROR_NONE;
    ${SPI_INSTANCE_NAME?lower_case}Obj.callback = NULL ;
    ${SPI_INSTANCE_NAME?lower_case}Obj.transferIsBusy = false ;
    ${SPI_INSTANCE_NAME?lower_case}Obj.csInterruptPending = false;
    ${SPI_INSTANCE_NAME?lower_case}Obj.rxInterruptActive = false;

    <#if SPIS_USE_BUSY_PIN == true>
    /* Set the Busy Pin to ready state */
    <#if SPIS_BUSY_PIN_LOGIC_LEVEL == "ACTIVE_HIGH">
    ${PLIB_NAME}_PinWrite((${PLIB_NAME}_PIN)${SPI_INSTANCE_NAME}_BUSY_PIN, 0);
    <#else>
    {PLIB_NAME}_PinWrite((${PLIB_NAME}_PIN)${SPI_INSTANCE_NAME}_BUSY_PIN, 1);
    </#if>
    </#if>

    /* Register callback and enable notifications on Chip Select logic level change */
    GPIO_PinInterruptCallbackRegister(${SPI_INSTANCE_NAME}_CS_PIN, ${SPI_INSTANCE_NAME}_CS_Handler, (uintptr_t)NULL);
    GPIO_PinInterruptEnable(${SPI_INSTANCE_NAME}_CS_PIN);

    /* Enable ${SPI_INSTANCE_NAME} RX and Error Interrupts. TX interrupt will be enabled when a SPI write is submitted. */
    ${SPI_INSTANCE_NAME}_ENABLE_RX_INT();
    ${SPI_INSTANCE_NAME}_ENABLE_ERR_INT();

    /* Enable ${SPI_INSTANCE_NAME} */
    ${SPI_INSTANCE_NAME}CONSET = _${SPI_INSTANCE_NAME}CON_ON_MASK;
}

/* For 16-bit/32-bit mode, the "size" must be specified in terms of 16-bit/32-bit words */
size_t ${SPI_INSTANCE_NAME}_Read(void* pRdBuffer, size_t size)
{
    size_t rdSize = size;
    uint32_t rdInIndex = ${SPI_INSTANCE_NAME?lower_case}Obj.rdInIndex;

    if (rdSize > rdInIndex)
    {
        rdSize = rdInIndex;
    }

    memcpy(pRdBuffer, ${SPI_INSTANCE_NAME}_ReadBuffer, rdSize);

    return rdSize;
}

/* For 16-bit/32-bit mode, the "size" must be specified in terms of 16-bit/32-bit words */
size_t ${SPI_INSTANCE_NAME}_Write(void* pWrBuffer, size_t size )
{
    size_t wrSize = size;

    ${SPI_INSTANCE_NAME}_DISABLE_TX_INT();

    if (wrSize > ${SPI_INSTANCE_NAME}_WRITE_BUFFER_SIZE)
    {
        wrSize = ${SPI_INSTANCE_NAME}_WRITE_BUFFER_SIZE;
    }

    memcpy(${SPI_INSTANCE_NAME}_WriteBuffer, pWrBuffer, wrSize);

    ${SPI_INSTANCE_NAME?lower_case}Obj.nWrBytes = wrSize;
    ${SPI_INSTANCE_NAME?lower_case}Obj.wrOutIndex = 0;

    /* Fill up the FIFO as long as there are empty elements */
    while ((!(${SPI_INSTANCE_NAME}STAT & _${SPI_INSTANCE_NAME}STAT_SPITBF_MASK)) && (${SPI_INSTANCE_NAME?lower_case}Obj.wrOutIndex < ${SPI_INSTANCE_NAME?lower_case}Obj.nWrBytes))
    {
        ${SPI_INSTANCE_NAME}BUF = ${SPI_INSTANCE_NAME}_WriteBuffer[${SPI_INSTANCE_NAME?lower_case}Obj.wrOutIndex++];
    }

    /* Enable TX interrupt */
    ${SPI_INSTANCE_NAME}_ENABLE_TX_INT();

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

void ${SPI_INSTANCE_NAME}_CallbackRegister(SPI_SLAVE_CALLBACK callBack, uintptr_t context )
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
/* Drive the GPIO pin to indicate to SPI Master that the slave is ready now */
void ${SPI_INSTANCE_NAME}_Ready(void)
{
<#if SPIS_BUSY_PIN_LOGIC_LEVEL = "ACTIVE_HIGH">
    ${PLIB_NAME}_PinWrite((${PLIB_NAME}_PIN)${SPI_INSTANCE_NAME}_BUSY_PIN, 0);
<#else>
    ${PLIB_NAME}_PinWrite((${PLIB_NAME}_PIN)${SPI_INSTANCE_NAME}_BUSY_PIN, 1);
</#if>
}
</#if>

SPI_SLAVE_ERROR ${SPI_INSTANCE_NAME}_ErrorGet(void)
{
    SPI_SLAVE_ERROR errorStatus = ${SPI_INSTANCE_NAME?lower_case}Obj.errorStatus;

    ${SPI_INSTANCE_NAME?lower_case}Obj.errorStatus = SPI_SLAVE_ERROR_NONE;

    return errorStatus;
}

static void ${SPI_INSTANCE_NAME}_CS_Handler(GPIO_PIN pin, uintptr_t context)
{
    <#if SPIS_CS_PIN_LOGIC_LEVEL == "ACTIVE_LOW">
    bool activeState = 0;
    <#else>
    bool activeState = 1;
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

        if ((${SPI_INSTANCE_NAME?lower_case}Obj.rxInterruptActive == false) && ((${SPI_RX_IFS_REG} & _${SPI_RX_IFS_REG}_${SPI_INSTANCE_NAME}RXIF_MASK) == 0))
        {
            /* CS is de-asserted */
            ${SPI_INSTANCE_NAME?lower_case}Obj.transferIsBusy = false;

            ${SPI_INSTANCE_NAME?lower_case}Obj.wrOutIndex = 0;
            ${SPI_INSTANCE_NAME?lower_case}Obj.nWrBytes = 0;

            if(${SPI_INSTANCE_NAME?lower_case}Obj.callback != NULL)
            {
                ${SPI_INSTANCE_NAME?lower_case}Obj.callback(${SPI_INSTANCE_NAME?lower_case}Obj.context);
            }

            /* Clear the read index. Application must read out the data by calling ${SPI_INSTANCE_NAME}_Read API in the callback */
            ${SPI_INSTANCE_NAME?lower_case}Obj.rdInIndex = 0;
        }
        else
        {
            /* If CS interrupt is serviced by either preempting the RX interrupt or RX interrupt is pending to be serviced,
             * then delegate the responsibility of giving application callback to the RX interrupt handler */

            ${SPI_INSTANCE_NAME?lower_case}Obj.csInterruptPending = true;
        }
    }
}

<#if SPI_INTERRUPT_COUNT == 1>
static void ${SPI_INSTANCE_NAME}_ERR_InterruptHandler (void)
<#else>
void ${SPI_INSTANCE_NAME}_ERR_InterruptHandler (void)
</#if>
{
    ${SPI_INSTANCE_NAME?lower_case}Obj.errorStatus = (${SPI_INSTANCE_NAME}STAT & _${SPI_INSTANCE_NAME}STAT_SPIROV_MASK);

    /* Clear the receive overflow flag */
    ${SPI_INSTANCE_NAME}STATCLR = _${SPI_INSTANCE_NAME}STAT_SPIROV_MASK;

    ${SPI_INSTANCE_NAME}_CLEAR_ERR_INT_FLAG();
}

<#if SPI_INTERRUPT_COUNT == 1>
static void ${SPI_INSTANCE_NAME}_TX_InterruptHandler (void)
<#else>
void ${SPI_INSTANCE_NAME}_TX_InterruptHandler (void)
</#if>
{
    /* Fill up the FIFO as long as there are empty elements */
    while ((!(${SPI_INSTANCE_NAME}STAT & _${SPI_INSTANCE_NAME}STAT_SPITBF_MASK)) && (${SPI_INSTANCE_NAME?lower_case}Obj.wrOutIndex < ${SPI_INSTANCE_NAME?lower_case}Obj.nWrBytes))
    {
        ${SPI_INSTANCE_NAME}BUF = ${SPI_INSTANCE_NAME}_WriteBuffer[${SPI_INSTANCE_NAME?lower_case}Obj.wrOutIndex++];
    }

    /* Clear the transmit interrupt flag */
    ${SPI_INSTANCE_NAME}_CLEAR_TX_INT_FLAG();

    if (${SPI_INSTANCE_NAME?lower_case}Obj.wrOutIndex == ${SPI_INSTANCE_NAME?lower_case}Obj.nWrBytes)
    {
        /* Nothing to transmit. Disable transmit interrupt. The last byte sent by the master will be shifted out automatically*/
        ${SPI_INSTANCE_NAME}_DISABLE_TX_INT();
    }
}

<#if SPI_INTERRUPT_COUNT == 1>
static void ${SPI_INSTANCE_NAME}_RX_InterruptHandler (void)
<#else>
void ${SPI_INSTANCE_NAME}_RX_InterruptHandler (void)
</#if>
{
    uint32_t receivedData = 0;

    ${SPI_INSTANCE_NAME?lower_case}Obj.rxInterruptActive = true;

    while (!(${SPI_INSTANCE_NAME}STAT & _${SPI_INSTANCE_NAME}STAT_SPIRBE_MASK))
    {
        /* Receive buffer is not empty. Read the received data. */
        receivedData = ${SPI_INSTANCE_NAME}BUF;

        if (${SPI_INSTANCE_NAME?lower_case}Obj.rdInIndex < ${SPI_INSTANCE_NAME}_READ_BUFFER_SIZE)
        {
            ${SPI_INSTANCE_NAME}_ReadBuffer[${SPI_INSTANCE_NAME?lower_case}Obj.rdInIndex++] = receivedData;
        }
    }

    /* Clear the receive interrupt flag */
    ${SPI_INSTANCE_NAME}_CLEAR_RX_INT_FLAG();

    ${SPI_INSTANCE_NAME?lower_case}Obj.rxInterruptActive = false;

    /* Check if CS interrupt occured before the RX interrupt and that CS interrupt delegated the responsibility to give
     * application callback to the RX interrupt */

    if (${SPI_INSTANCE_NAME?lower_case}Obj.csInterruptPending == true)
    {
        ${SPI_INSTANCE_NAME?lower_case}Obj.csInterruptPending = false;
        ${SPI_INSTANCE_NAME?lower_case}Obj.transferIsBusy = false;

        ${SPI_INSTANCE_NAME?lower_case}Obj.wrOutIndex = 0;
        ${SPI_INSTANCE_NAME?lower_case}Obj.nWrBytes = 0;

        if(${SPI_INSTANCE_NAME?lower_case}Obj.callback != NULL)
        {
            ${SPI_INSTANCE_NAME?lower_case}Obj.callback(${SPI_INSTANCE_NAME?lower_case}Obj.context);
        }

        /* Clear the read index. Application must read out the data by calling ${SPI_INSTANCE_NAME}_Read API in the callback */
        ${SPI_INSTANCE_NAME?lower_case}Obj.rdInIndex = 0;
    }
}

<#if SPI_INTERRUPT_COUNT == 1>
void SPI_${SPI_INSTANCE_NUM}_InterruptHandler (void)
{
    if ((${SPI_FLT_IFS_REG} & _${SPI_FLT_IFS_REG}_${SPI_INSTANCE_NAME}EIF_MASK) && (${SPI_FLT_IEC_REG} & _${SPI_FLT_IEC_REG}_${SPI_INSTANCE_NAME}EIE_MASK))
    {
        /* Call error interrupt handler */
        ${SPI_INSTANCE_NAME}_ERR_InterruptHandler();
    }
    if ((${SPI_RX_IFS_REG} & _${SPI_RX_IFS_REG}_${SPI_INSTANCE_NAME}RXIF_MASK) && (${SPI_RX_IEC_REG} & _${SPI_RX_IEC_REG}_${SPI_INSTANCE_NAME}RXIE_MASK))
    {
        /* RX interrupt is enabled and RX buffer is not empty */
        ${SPI_INSTANCE_NAME}_RX_InterruptHandler();
    }
    if ((${SPI_TX_IFS_REG} & _${SPI_TX_IFS_REG}_${SPI_INSTANCE_NAME}TXIF_MASK) && (${SPI_TX_IEC_REG} & _${SPI_TX_IEC_REG}_${SPI_INSTANCE_NAME}TXIE_MASK))
    {
        /* TX interrupt is enabled and TX buffer is empty */
        ${SPI_INSTANCE_NAME}_TX_InterruptHandler();
    }
}
</#if>