/*******************************************************************************
  SERCOM Universal Synchronous/Asynchrnous Receiver/Transmitter PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_${SERCOM_INSTANCE_NAME?lower_case}_usart.c

  Summary
    USART peripheral library interface.

  Description
    This file defines the interface to the USART peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

  Remarks:
    None.
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

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

<#if core.CoreSysIntFile == true>
#include "interrupts.h"
</#if>
#include "plib_${SERCOM_INSTANCE_NAME?lower_case}_usart.h"

// *****************************************************************************
// *****************************************************************************
// Section: Global Data
// *****************************************************************************
// *****************************************************************************

<#assign USART_PLIB = "SERCOM_INSTANCE_NAME">
<#assign USART_PLIB_CLOCK_FREQUENCY = "core." + USART_PLIB?eval + "_CORE_CLOCK_FREQUENCY">

/* ${SERCOM_INSTANCE_NAME} USART baud value for ${USART_BAUD_RATE} Hz baud rate */
#define ${SERCOM_INSTANCE_NAME}_USART_INT_BAUD_VALUE            (${USART_BAUD_VALUE}UL)

static SERCOM_USART_RING_BUFFER_OBJECT ${SERCOM_INSTANCE_NAME?lower_case}USARTObj;

// *****************************************************************************
// *****************************************************************************
// Section: ${SERCOM_INSTANCE_NAME} USART Interface Routines
// *****************************************************************************
// *****************************************************************************

<#if USART_RX_ENABLE = true>
#define ${SERCOM_INSTANCE_NAME}_USART_READ_BUFFER_SIZE      ${USART_RX_RING_BUFFER_SIZE}U
#define ${SERCOM_INSTANCE_NAME}_USART_READ_BUFFER_9BIT_SIZE     (${USART_RX_RING_BUFFER_SIZE}U >> 1U)
#define ${SERCOM_INSTANCE_NAME}_USART_RX_INT_DISABLE()      ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_INTENCLR = SERCOM_USART_INT_INTENCLR_RXC_Msk
#define ${SERCOM_INSTANCE_NAME}_USART_RX_INT_ENABLE()       ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_INTENSET = SERCOM_USART_INT_INTENSET_RXC_Msk

static uint8_t ${SERCOM_INSTANCE_NAME}_USART_ReadBuffer[${SERCOM_INSTANCE_NAME}_USART_READ_BUFFER_SIZE];
</#if>

<#if USART_TX_ENABLE = true>
#define ${SERCOM_INSTANCE_NAME}_USART_WRITE_BUFFER_SIZE     ${USART_TX_RING_BUFFER_SIZE}U
#define ${SERCOM_INSTANCE_NAME}_USART_WRITE_BUFFER_9BIT_SIZE  (${USART_TX_RING_BUFFER_SIZE}U >> 1U)
#define ${SERCOM_INSTANCE_NAME}_USART_TX_INT_DISABLE()      ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_INTENCLR = SERCOM_USART_INT_INTENCLR_DRE_Msk
#define ${SERCOM_INSTANCE_NAME}_USART_TX_INT_ENABLE()       ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_INTENSET = SERCOM_USART_INT_INTENSET_DRE_Msk

static uint8_t ${SERCOM_INSTANCE_NAME}_USART_WriteBuffer[${SERCOM_INSTANCE_NAME}_USART_WRITE_BUFFER_SIZE];
</#if>

void ${SERCOM_INSTANCE_NAME}_USART_Initialize( void )
{
    /*
     * Configures USART Clock Mode
     * Configures TXPO and RXPO
     * Configures Data Order
     * Configures Standby Mode
     * Configures Sampling rate
     * Configures IBON
     */
    <@compress single_line=true>${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_CTRLA =      SERCOM_USART_INT_CTRLA_MODE_USART_INT_CLK |
    SERCOM_USART_INT_CTRLA_RXPO(${USART_RXPO}UL) |
    SERCOM_USART_INT_CTRLA_TXPO(${USART_TXPO}UL) |
    SERCOM_USART_INT_CTRLA_DORD_Msk |
    SERCOM_USART_INT_CTRLA_IBON_Msk |
    SERCOM_USART_INT_CTRLA_FORM(${USART_FORM}UL)
    <#if USART_SAMPLE_RATE??>| SERCOM_USART_INT_CTRLA_SAMPR(${USART_SAMPLE_RATE}UL)</#if>
    ${USART_RUNSTDBY?then('| SERCOM_USART_INT_CTRLA_RUNSTDBY_Msk', '')};</@compress>

    /* Configure Baud Rate */
    ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_BAUD = (uint16_t)SERCOM_USART_INT_BAUD_BAUD(${SERCOM_INSTANCE_NAME}_USART_INT_BAUD_VALUE);

    /*
     * Configures RXEN
     * Configures TXEN
     * Configures CHSIZE
     * Configures Parity
     * Configures Stop bits
     */
    <@compress single_line=true>${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_CTRLB = SERCOM_USART_INT_CTRLB_CHSIZE_${USART_CHARSIZE_BITS} |
       SERCOM_USART_INT_CTRLB_SBMODE_${USART_STOP_BIT}
       ${(USART_PARITY_MODE == "ODD")?then('| SERCOM_USART_INT_CTRLB_PMODE_Msk', '')}
       ${USART_RX_ENABLE?then('| SERCOM_USART_INT_CTRLB_RXEN_Msk', '')}
       ${USART_SFDE?then('| SERCOM_USART_INT_CTRLB_SFDE_Msk', '')}
       ${USART_TX_ENABLE?then('| SERCOM_USART_INT_CTRLB_TXEN_Msk', '')};</@compress>

    /* Wait for sync */
<#if SERCOM_SYNCBUSY = false>
    while((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_STATUS & (uint16_t)SERCOM_USART_INT_STATUS_SYNCBUSY_Msk) == (uint16_t)SERCOM_USART_INT_STATUS_SYNCBUSY_Msk)
    {
        /* Do nothing */
    }
<#else>
    while((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_SYNCBUSY) != 0U)
    {
        /* Do nothing */
    }
</#if>

<#if ((USART_FORM == "0x0" || USART_FORM == "0x1") && USART_CTRLC_GTIME?? && USART_TXPO == "0x3")>
    /* Configures RS485 Guard Time */
    <@compress single_line=true>${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_CTRLC =
        SERCOM_USART_INT_CTRLC_GTIME(${USART_CTRLC_GTIME}UL);</@compress>
</#if>
<#if (USART_FORM == "0x2" && USART_LIN_MASTER_HDRDLY?? && USART_LIN_MASTER_BREAK_LEN??)>
    /* Configures hardware delay and break length */
    <@compress single_line=true>${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_CTRLC =
        SERCOM_USART_INT_CTRLC_HDRDLY(${USART_LIN_MASTER_HDRDLY}UL)
        | SERCOM_USART_INT_CTRLC_BRKLEN(${USART_LIN_MASTER_BREAK_LEN}UL);</@compress>
</#if>

    /* Enable the UART after the configurations */
    ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_CTRLA |= SERCOM_USART_INT_CTRLA_ENABLE_Msk;

    /* Wait for sync */
<#if SERCOM_SYNCBUSY = false>
    while((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_STATUS & (uint16_t)SERCOM_USART_INT_STATUS_SYNCBUSY_Msk) == (uint16_t)SERCOM_USART_INT_STATUS_SYNCBUSY_Msk)
    {
        /* Do nothing */
    }
<#else>
    while((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_SYNCBUSY) != 0U)
    {
        /* Do nothing */
    }
</#if>

<#if USART_RX_ENABLE = true>
    /* Initialize instance object */
    ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rdCallback = NULL;
    ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rdInIndex = 0U;
    ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rdOutIndex = 0U;
    ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.isRdNotificationEnabled = false;
    ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.isRdNotifyPersistently = false;
    ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rdThreshold = 0U;
    ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.errorStatus = USART_ERROR_NONE;
</#if>
<#if USART_TX_ENABLE = true>
    ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.wrCallback = NULL;
    ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.wrInIndex = 0U;
    ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.wrOutIndex = 0U;
    ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.isWrNotificationEnabled = false;
    ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.isWrNotifyPersistently = false;
    ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.wrThreshold = 0U;
</#if>
    if (((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_CTRLB & SERCOM_USART_INT_CTRLB_CHSIZE_Msk) >> SERCOM_USART_INT_CTRLB_CHSIZE_Pos) != 0x01U)
    {
<#if USART_RX_ENABLE == true>
        ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rdBufferSize = ${SERCOM_INSTANCE_NAME}_USART_READ_BUFFER_SIZE;
</#if>
<#if USART_TX_ENABLE == true>
        ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.wrBufferSize = ${SERCOM_INSTANCE_NAME}_USART_WRITE_BUFFER_SIZE;
</#if>
    }
    else
    {
<#if USART_RX_ENABLE == true>
        ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rdBufferSize = ${SERCOM_INSTANCE_NAME}_USART_READ_BUFFER_9BIT_SIZE;
</#if>
<#if USART_TX_ENABLE == true>
        ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.wrBufferSize = ${SERCOM_INSTANCE_NAME}_USART_WRITE_BUFFER_9BIT_SIZE;
</#if>
    }
<#if USART_RX_ENABLE = true>
<#if USART_INTENSET_ERROR = true>
    /* Enable error interrupt */
    ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_INTENSET = (uint8_t)SERCOM_USART_INT_INTENSET_ERROR_Msk;

</#if>
<#if USART_FORM == "0x4" || USART_FORM == "0x5">
    ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_INTENSET = (uint8_t)(SERCOM_USART_INT_INTENSET_RXBRK_Msk | SERCOM_USART_INT_INTENSET_RXC_Msk);
<#else>
    /* Enable Receive Complete interrupt */
    ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_INTENSET = (uint8_t)SERCOM_USART_INT_INTENSET_RXC_Msk;
</#if>
</#if>
}

uint32_t ${SERCOM_INSTANCE_NAME}_USART_FrequencyGet( void )
{
<#if USART_PLIB_CLOCK_FREQUENCY?eval??>
    return ${USART_PLIB_CLOCK_FREQUENCY?eval}UL;
<#else>
    return 0U;
</#if>
}

bool ${SERCOM_INSTANCE_NAME}_USART_SerialSetup( USART_SERIAL_SETUP * serialSetup, uint32_t clkFrequency )
{
    bool setupStatus       = false;
    uint32_t baudValue     = 0U;
<#if USART_SAMPLE_RATE??>
    uint32_t sampleRate    = 0U;
</#if>
<#if (USART_FORM == "0x2" || USART_FORM == "0x4" || USART_FORM == "0x5")>
    float f_baudValue      = 0.0f;
    float f_temp           = 0.0f;
    uint32_t fractionPart  = 0U;
</#if>

    if((serialSetup != NULL) && (serialSetup->baudRate != 0U))
    {
        if(clkFrequency == 0U)
        {
            clkFrequency = ${SERCOM_INSTANCE_NAME}_USART_FrequencyGet();
        }

        <#if USART_SAMPLE_RATE??>
        <#if (USART_FORM == "0x2" || USART_FORM == "0x4" || USART_FORM == "0x5")>
        if(clkFrequency >= (16U * serialSetup->baudRate))
        {
            f_baudValue = (float)clkFrequency/(16.0f * (float)serialSetup->baudRate);
            f_temp = ((f_baudValue - ((float)((int)f_baudValue))) * 8.0f);
            fractionPart = ((uint32_t)f_temp & 0xFFU);
            baudValue = (uint32_t)f_baudValue;
            if ((baudValue == 0U) || (baudValue >= 8192U))
            {
                baudValue = 0U;
            }
            else
            {
                baudValue |= (fractionPart << 13U);
            }
            sampleRate = 1U;
        }
        <#else>
        if(clkFrequency >= (16U * serialSetup->baudRate))
        {
            baudValue = 65536U - (uint32_t)(((uint64_t)65536U * 16U * serialSetup->baudRate) / clkFrequency);
            sampleRate = 0U;
        }
        else if(clkFrequency >= (8U * serialSetup->baudRate))
        {
            baudValue = 65536U - (uint32_t)(((uint64_t)65536U * 8U * serialSetup->baudRate) / clkFrequency);
            sampleRate = 2U;
        }
        else if(clkFrequency >= (3U * serialSetup->baudRate))
        {
            baudValue = 65536U - (uint32_t)(((uint64_t)65536U * 3U * serialSetup->baudRate) / clkFrequency);
            sampleRate = 4U;
        }
        else
        {
            /* Do nothing */
        }
        </#if>
        <#else>
        if(clkFrequency >= (16U * serialSetup->baudRate))
        {
            baudValue = 65536U - (uint32_t)(((uint64_t)65536U * 16U * serialSetup->baudRate) / clkFrequency);
        }
        </#if>

        /* Disable the USART before configurations */
        ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_CTRLA &= ~SERCOM_USART_INT_CTRLA_ENABLE_Msk;

        /* Wait for sync */
        <#if SERCOM_SYNCBUSY = false>
        while((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_STATUS & (uint16_t)SERCOM_USART_INT_STATUS_SYNCBUSY_Msk) == SERCOM_USART_INT_STATUS_SYNCBUSY_Msk)
        {
            /* Do nothing */
        }
        <#else>
        while((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_SYNCBUSY) != 0U)
        {
            /* Do nothing */
        }
        </#if>

        /* Configure Baud Rate */
        ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_BAUD = (uint16_t)SERCOM_USART_INT_BAUD_BAUD(baudValue);

        <#if (USART_FORM == "0x2" || USART_FORM == "0x4" || USART_FORM == "0x5")>
        ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_CTRLA = (${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_CTRLA & ~SERCOM_USART_INT_CTRLA_SAMPR_Msk) | SERCOM_USART_INT_CTRLA_SAMPR((uint32_t)sampleRate);

        ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_CTRLB = (${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_CTRLB & ~(SERCOM_USART_INT_CTRLB_CHSIZE_Msk | SERCOM_USART_INT_CTRLB_SBMODE_Msk)) | ((uint32_t) serialSetup->dataWidth | (uint32_t) serialSetup->stopBits);
        <#else>
        /* Configure Parity Options */
        if(serialSetup->parity == USART_PARITY_NONE)
        {
            ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_CTRLA = <#if USART_SAMPLE_RATE??> (${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_CTRLA & ~(SERCOM_USART_INT_CTRLA_SAMPR_Msk | SERCOM_USART_INT_CTRLA_FORM_Msk)) | SERCOM_USART_INT_CTRLA_FORM(0x0UL) | SERCOM_USART_INT_CTRLA_SAMPR((uint32_t)sampleRate); <#else>
            (${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_CTRLA & ~SERCOM_USART_INT_CTRLA_FORM_Msk) | SERCOM_USART_INT_CTRLA_FORM(0x0UL);
            </#if>

            ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_CTRLB = (${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_CTRLB & ~(SERCOM_USART_INT_CTRLB_CHSIZE_Msk | SERCOM_USART_INT_CTRLB_SBMODE_Msk)) | ((uint32_t) serialSetup->dataWidth | (uint32_t) serialSetup->stopBits);
        }
        else
        {
            ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_CTRLA = <#if USART_SAMPLE_RATE??> (${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_CTRLA & ~(SERCOM_USART_INT_CTRLA_SAMPR_Msk | SERCOM_USART_INT_CTRLA_FORM_Msk)) | SERCOM_USART_INT_CTRLA_FORM(0x1UL) | SERCOM_USART_INT_CTRLA_SAMPR((uint32_t)sampleRate); <#else>
            (${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_CTRLA & ~SERCOM_USART_INT_CTRLA_FORM_Msk) | SERCOM_USART_INT_CTRLA_FORM(0x1UL);
            </#if>

            ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_CTRLB = (${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_CTRLB & ~(SERCOM_USART_INT_CTRLB_CHSIZE_Msk | SERCOM_USART_INT_CTRLB_SBMODE_Msk | SERCOM_USART_INT_CTRLB_PMODE_Msk)) | (uint32_t) serialSetup->dataWidth | (uint32_t) serialSetup->stopBits | (uint32_t) serialSetup->parity ;
        }
        </#if>

        /* Wait for sync */
        <#if SERCOM_SYNCBUSY = false>
        while((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_STATUS & SERCOM_USART_INT_STATUS_SYNCBUSY_Msk) == SERCOM_USART_INT_STATUS_SYNCBUSY_Msk)
        {
            /* Do nothing */
        }
        <#else>
        while((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_SYNCBUSY) != 0U)
        {
            /* Do nothing */
        }
        </#if>

        /* Enable the USART after the configurations */
        ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_CTRLA |= SERCOM_USART_INT_CTRLA_ENABLE_Msk;

        /* Wait for sync */
        <#if SERCOM_SYNCBUSY = false>
        while((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_STATUS & SERCOM_USART_INT_STATUS_SYNCBUSY_Msk) == SERCOM_USART_INT_STATUS_SYNCBUSY_Msk)
        {
            /* Do nothing */
        }
        <#else>
        while((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_SYNCBUSY) != 0U)
        {
            /* Do nothing */
        }
        </#if>


        if (((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_CTRLB & SERCOM_USART_INT_CTRLB_CHSIZE_Msk) >> SERCOM_USART_INT_CTRLB_CHSIZE_Pos) != 0x01U)
        {
<#if USART_RX_ENABLE == true>
            ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rdBufferSize = ${SERCOM_INSTANCE_NAME}_USART_READ_BUFFER_SIZE;
</#if>
<#if USART_TX_ENABLE == true>
            ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.wrBufferSize = ${SERCOM_INSTANCE_NAME}_USART_WRITE_BUFFER_SIZE;
</#if>
        }
        else
        {
<#if USART_RX_ENABLE == true>
            ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rdBufferSize = ${SERCOM_INSTANCE_NAME}_USART_READ_BUFFER_9BIT_SIZE;
</#if>
<#if USART_TX_ENABLE == true>
            ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.wrBufferSize = ${SERCOM_INSTANCE_NAME}_USART_WRITE_BUFFER_9BIT_SIZE;
</#if>
        }

        setupStatus = true;
    }

    return setupStatus;
}

void static ${SERCOM_INSTANCE_NAME}_USART_ErrorClear( void )
{
    uint16_t  u16dummyData = 0;

<#if USART_INTENSET_ERROR = true>
    /* Clear error flag */
    ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_INTFLAG = SERCOM_USART_INT_INTFLAG_ERROR_Msk;

</#if>
    /* Clear all errors */
    ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_STATUS = SERCOM_USART_INT_STATUS_PERR_Msk | SERCOM_USART_INT_STATUS_FERR_Msk | SERCOM_USART_INT_STATUS_BUFOVF_Msk <#if USART_FORM == "0x4" || USART_FORM == "0x5"> | SERCOM_USART_INT_STATUS_ISF_Msk </#if>;

    /* Flush existing error bytes from the RX FIFO */
    while((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_INTFLAG & SERCOM_USART_INT_INTFLAG_RXC_Msk) == SERCOM_USART_INT_INTFLAG_RXC_Msk)
    {
        u16dummyData = (uint16_t)${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_DATA;
    }

    /* Ignore the warning */
    (void)u16dummyData;
}

USART_ERROR ${SERCOM_INSTANCE_NAME}_USART_ErrorGet( void )
{
    USART_ERROR errorStatus = ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.errorStatus;

    ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.errorStatus = USART_ERROR_NONE;

    return errorStatus;
}

<#if USART_RX_ENABLE = true>

/* This routine is only called from ISR. Hence do not disable/enable USART interrupts. */
static inline bool ${SERCOM_INSTANCE_NAME}_USART_RxPushByte(uint16_t rdByte)
{
    uint32_t tempInIndex;
    uint32_t rdInIdx;
    bool isSuccess = false;

    tempInIndex = ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rdInIndex + 1U;

    if (tempInIndex >= ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rdBufferSize)
    {
        tempInIndex = 0U;
    }

    if (tempInIndex == ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rdOutIndex)
    {
        /* Queue is full - Report it to the application. Application gets a chance to free up space by reading data out from the RX ring buffer */
        if(${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rdCallback != NULL)
        {
            ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rdCallback(SERCOM_USART_EVENT_READ_BUFFER_FULL, ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rdContext);

            /* Read the indices again in case application has freed up space in RX ring buffer */
            tempInIndex = ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rdInIndex + 1U;

            if (tempInIndex >= ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rdBufferSize)
            {
                tempInIndex = 0U;
            }
        }
    }

    /* Attempt to push the data into the ring buffer */
    if (tempInIndex != ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rdOutIndex)
    {
        if (((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_CTRLB & SERCOM_USART_INT_CTRLB_CHSIZE_Msk) >> SERCOM_USART_INT_CTRLB_CHSIZE_Pos) != 0x01U)
        {
            /* 8-bit */
            ${SERCOM_INSTANCE_NAME}_USART_ReadBuffer[${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rdInIndex] = (uint8_t)rdByte;
        }
        else
        {
            /* 9-bit */
            rdInIdx = ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rdInIndex << 1U;

            ${SERCOM_INSTANCE_NAME}_USART_ReadBuffer[rdInIdx] = (uint8_t)rdByte;
            ${SERCOM_INSTANCE_NAME}_USART_ReadBuffer[rdInIdx + 1U] = (uint8_t)(rdByte >> 8U);
        }

        ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rdInIndex = tempInIndex;
        isSuccess = true;
    }
    else
    {
        /* Queue is full. Data will be lost. */
    }

    return isSuccess;
}

/* This routine is only called from ISR. Hence do not disable/enable USART interrupts. */
static void ${SERCOM_INSTANCE_NAME}_USART_ReadNotificationSend(void)
{
    uint32_t nUnreadBytesAvailable;

    if (${SERCOM_INSTANCE_NAME?lower_case}USARTObj.isRdNotificationEnabled == true)
    {
        nUnreadBytesAvailable = ${SERCOM_INSTANCE_NAME}_USART_ReadCountGet();

        if(${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rdCallback != NULL)
        {
            if (${SERCOM_INSTANCE_NAME?lower_case}USARTObj.isRdNotifyPersistently == true)
            {
                if (nUnreadBytesAvailable >= ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rdThreshold)
                {
                    ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rdCallback(SERCOM_USART_EVENT_READ_THRESHOLD_REACHED, ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rdContext);
                }
            }
            else
            {
                if (nUnreadBytesAvailable == ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rdThreshold)
                {
                    ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rdCallback(SERCOM_USART_EVENT_READ_THRESHOLD_REACHED, ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rdContext);
                }
            }
        }
    }
}

size_t ${SERCOM_INSTANCE_NAME}_USART_Read(uint8_t* pRdBuffer, const size_t size)
{
    size_t nBytesRead = 0U;
    uint32_t rdOutIndex;
    uint32_t rdInIndex;
    uint32_t rdOutIdx;
    uint32_t nBytesReadIdx;

    /* Take a snapshot of indices to avoid creation of critical section */

    rdOutIndex = ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rdOutIndex;
    rdInIndex = ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rdInIndex;

    while (nBytesRead < size)
    {
        if (rdOutIndex != rdInIndex)
        {
            if (((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_CTRLB & SERCOM_USART_INT_CTRLB_CHSIZE_Msk) >> SERCOM_USART_INT_CTRLB_CHSIZE_Pos) != 0x01U)
            {
                pRdBuffer[nBytesRead] = ${SERCOM_INSTANCE_NAME}_USART_ReadBuffer[rdOutIndex];
                nBytesRead += 1U;
                rdOutIndex += 1U;
            }
            else
            {
                rdOutIdx = rdOutIndex << 1U;
                nBytesReadIdx = nBytesRead << 1U;

                pRdBuffer[nBytesReadIdx] = ${SERCOM_INSTANCE_NAME}_USART_ReadBuffer[rdOutIdx];
                pRdBuffer[nBytesReadIdx + 1U] = ${SERCOM_INSTANCE_NAME}_USART_ReadBuffer[rdOutIdx + 1U];

                rdOutIndex += 1U;
                nBytesRead += 1U;
            }

            if (rdOutIndex >= ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rdBufferSize)
            {
                rdOutIndex = 0U;
            }
        }
        else
        {
            /* No more data available in the RX buffer */
            break;
        }
    }

    ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rdOutIndex = rdOutIndex;

    return nBytesRead;
}

size_t ${SERCOM_INSTANCE_NAME}_USART_ReadCountGet(void)
{
    size_t nUnreadBytesAvailable;
    uint32_t rdOutIndex;
    uint32_t rdInIndex;

    /* Take a snapshot of indices to avoid creation of critical section */
    rdOutIndex = ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rdOutIndex;
    rdInIndex = ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rdInIndex;

    if ( rdInIndex >=  rdOutIndex)
    {
        nUnreadBytesAvailable =  rdInIndex - rdOutIndex;
    }
    else
    {
        nUnreadBytesAvailable =  (${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rdBufferSize -  rdOutIndex) + rdInIndex;
    }

    return nUnreadBytesAvailable;
}

size_t ${SERCOM_INSTANCE_NAME}_USART_ReadFreeBufferCountGet(void)
{
    return (${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rdBufferSize - 1U) - ${SERCOM_INSTANCE_NAME}_USART_ReadCountGet();
}

size_t ${SERCOM_INSTANCE_NAME}_USART_ReadBufferSizeGet(void)
{
    return (${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rdBufferSize - 1U);
}

bool ${SERCOM_INSTANCE_NAME}_USART_ReadNotificationEnable(bool isEnabled, bool isPersistent)
{
    bool previousStatus = ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.isRdNotificationEnabled;

    ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.isRdNotificationEnabled = isEnabled;

    ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.isRdNotifyPersistently = isPersistent;

    return previousStatus;
}

void ${SERCOM_INSTANCE_NAME}_USART_ReadThresholdSet(uint32_t nBytesThreshold)
{
    if (nBytesThreshold > 0U)
    {
        ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rdThreshold = nBytesThreshold;
    }
}

void ${SERCOM_INSTANCE_NAME}_USART_ReadCallbackRegister( SERCOM_USART_RING_BUFFER_CALLBACK callback, uintptr_t context)
{
    ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rdCallback = callback;

    ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rdContext = context;
}
</#if>

<#if USART_TX_ENABLE = true>

bool ${SERCOM_INSTANCE_NAME}_USART_TransmitComplete( void )
{
    bool transmitComplete = false;

    if ((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_INTFLAG & SERCOM_USART_INT_INTFLAG_TXC_Msk) == SERCOM_USART_INT_INTFLAG_TXC_Msk)
    {
        transmitComplete = true;
    }

    return transmitComplete;
}

/* This routine is only called from ISR. Hence do not disable/enable USART interrupts. */
static bool ${SERCOM_INSTANCE_NAME}_USART_TxPullByte(void* pWrData)
{
    bool isSuccess = false;
    uint32_t wrInIndex = ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.wrInIndex;
    uint32_t wrOutIndex = ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.wrOutIndex;
    uint32_t wrOutIdx;
    uint8_t* pWrByte = (uint8_t*)pWrData;

    if (wrOutIndex != wrInIndex)
    {
        if (((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_CTRLB & SERCOM_USART_INT_CTRLB_CHSIZE_Msk) >> SERCOM_USART_INT_CTRLB_CHSIZE_Pos) != 0x01U)
        {
            *pWrByte = ${SERCOM_INSTANCE_NAME}_USART_WriteBuffer[wrOutIndex];
            wrOutIndex++;
        }
        else
        {
            wrOutIdx = wrOutIndex << 1U;
            pWrByte[0] = ${SERCOM_INSTANCE_NAME}_USART_WriteBuffer[wrOutIdx];
            pWrByte[1] = ${SERCOM_INSTANCE_NAME}_USART_WriteBuffer[wrOutIdx + 1U];

            wrOutIndex++;
        }


        if (wrOutIndex >= ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.wrBufferSize)
        {
            wrOutIndex = 0U;
        }

        ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.wrOutIndex = wrOutIndex;

        isSuccess = true;
    }

    return isSuccess;
}

static inline bool ${SERCOM_INSTANCE_NAME}_USART_TxPushByte(uint16_t wrByte)
{
    uint32_t tempInIndex;
    uint32_t wrInIndex = ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.wrInIndex;
    uint32_t wrOutIndex = ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.wrOutIndex;
    uint32_t wrInIdx;

    bool isSuccess = false;

    tempInIndex = wrInIndex + 1U;

    if (tempInIndex >= ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.wrBufferSize)
    {
        tempInIndex = 0U;
    }
    if (tempInIndex != wrOutIndex)
    {
        if (((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_CTRLB & SERCOM_USART_INT_CTRLB_CHSIZE_Msk) >> SERCOM_USART_INT_CTRLB_CHSIZE_Pos) != 0x01U)
        {
            ${SERCOM_INSTANCE_NAME}_USART_WriteBuffer[wrInIndex] = (uint8_t)wrByte;
        }
        else
        {
            wrInIdx = wrInIndex << 1U;

            ${SERCOM_INSTANCE_NAME}_USART_WriteBuffer[wrInIdx] = (uint8_t)wrByte;
            wrInIdx++;
            ${SERCOM_INSTANCE_NAME}_USART_WriteBuffer[wrInIdx] = (uint8_t)(wrByte >> 8U);
        }

        ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.wrInIndex = tempInIndex;

        isSuccess = true;
    }
    else
    {
        /* Queue is full. Report Error. */
    }

    return isSuccess;
}

/* This routine is only called from ISR. Hence do not disable/enable USART interrupts. */
static void ${SERCOM_INSTANCE_NAME}_USART_SendWriteNotification(void)
{
    uint32_t nFreeWrBufferCount;

    if (${SERCOM_INSTANCE_NAME?lower_case}USARTObj.isWrNotificationEnabled == true)
    {
        nFreeWrBufferCount = ${SERCOM_INSTANCE_NAME}_USART_WriteFreeBufferCountGet();

        if(${SERCOM_INSTANCE_NAME?lower_case}USARTObj.wrCallback != NULL)
        {
            if (${SERCOM_INSTANCE_NAME?lower_case}USARTObj.isWrNotifyPersistently == true)
            {
                if (nFreeWrBufferCount >= ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.wrThreshold)
                {
                    ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.wrCallback(SERCOM_USART_EVENT_WRITE_THRESHOLD_REACHED, ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.wrContext);
                }
            }
            else
            {
                if (nFreeWrBufferCount == ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.wrThreshold)
                {
                    ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.wrCallback(SERCOM_USART_EVENT_WRITE_THRESHOLD_REACHED, ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.wrContext);
                }
            }
        }
    }
}

static size_t ${SERCOM_INSTANCE_NAME}_USART_WritePendingBytesGet(void)
{
    size_t nPendingTxBytes;

    /* Take a snapshot of indices to avoid creation of critical section */
    uint32_t wrInIndex = ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.wrInIndex;
    uint32_t wrOutIndex = ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.wrOutIndex;

    if ( wrInIndex >= wrOutIndex)
    {
        nPendingTxBytes =  wrInIndex - wrOutIndex;
    }
    else
    {
        nPendingTxBytes =  (${SERCOM_INSTANCE_NAME?lower_case}USARTObj.wrBufferSize -  wrOutIndex) + wrInIndex;
    }

    return nPendingTxBytes;
}

size_t ${SERCOM_INSTANCE_NAME}_USART_WriteCountGet(void)
{
    size_t nPendingTxBytes;

    nPendingTxBytes = ${SERCOM_INSTANCE_NAME}_USART_WritePendingBytesGet();

    return nPendingTxBytes;
}

size_t ${SERCOM_INSTANCE_NAME}_USART_Write(uint8_t* pWrBuffer, const size_t size )
{
    size_t nBytesWritten  = 0U;

    while (nBytesWritten < size)
    {
        if (((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_CTRLB & SERCOM_USART_INT_CTRLB_CHSIZE_Msk) >> SERCOM_USART_INT_CTRLB_CHSIZE_Pos) != 0x01U)
        {
            if (${SERCOM_INSTANCE_NAME}_USART_TxPushByte(pWrBuffer[nBytesWritten]) == true)
            {
                nBytesWritten++;
            }
            else
            {
                /* Queue is full, exit the loop */
                break;
            }
        }
        else
        {
            uint16_t halfWordData = (uint16_t)(pWrBuffer[(2U * nBytesWritten) + 1U]);
            halfWordData <<= 8U;
            halfWordData |= (uint16_t)pWrBuffer[2U * nBytesWritten];
            if (${SERCOM_INSTANCE_NAME}_USART_TxPushByte(halfWordData) == true)
            {
                nBytesWritten++;
            }
            else
            {
                /* Queue is full, exit the loop */
                break;
            }
        }
    }

    /* Check if any data is pending for transmission */
    if (${SERCOM_INSTANCE_NAME}_USART_WritePendingBytesGet() > 0U)
    {
        /* Enable TX interrupt as data is pending for transmission */
        ${SERCOM_INSTANCE_NAME}_USART_TX_INT_ENABLE();
    }

    return nBytesWritten;
}

size_t ${SERCOM_INSTANCE_NAME}_USART_WriteFreeBufferCountGet(void)
{
    return (${SERCOM_INSTANCE_NAME?lower_case}USARTObj.wrBufferSize - 1U) - ${SERCOM_INSTANCE_NAME}_USART_WriteCountGet();
}

size_t ${SERCOM_INSTANCE_NAME}_USART_WriteBufferSizeGet(void)
{
    return (${SERCOM_INSTANCE_NAME?lower_case}USARTObj.wrBufferSize - 1U);
}

bool ${SERCOM_INSTANCE_NAME}_USART_WriteNotificationEnable(bool isEnabled, bool isPersistent)
{
    bool previousStatus = ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.isWrNotificationEnabled;

    ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.isWrNotificationEnabled = isEnabled;

    ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.isWrNotifyPersistently = isPersistent;

    return previousStatus;
}

void ${SERCOM_INSTANCE_NAME}_USART_WriteThresholdSet(uint32_t nBytesThreshold)
{
    if (nBytesThreshold > 0U)
    {
        ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.wrThreshold = nBytesThreshold;
    }
}

void ${SERCOM_INSTANCE_NAME}_USART_WriteCallbackRegister( SERCOM_USART_RING_BUFFER_CALLBACK callback, uintptr_t context)
{
    ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.wrCallback = callback;

    ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.wrContext = context;
}

<#if USART_FORM == "0x2">
bool ${SERCOM_INSTANCE_NAME}_USART_LIN_CommandSet(USART_LIN_MASTER_CMD cmd)
{
    /* Command strobe bits cannot be set while transmitter is busy */

    if((${SERCOM_INSTANCE_NAME}_USART_WriteCountGet() == 0U) && (${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_STATUS & SERCOM_USART_INT_STATUS_TXE_Msk))
    {
        /* Clear the flag */
        ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_STATUS = (uint16_t)SERCOM_USART_INT_STATUS_TXE_Msk;

        ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_CTRLB |= (${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_CTRLB & ~SERCOM_USART_INT_CTRLB_LINCMD_Msk) | cmd;

        return true;
    }
    else
    {
        return false;
    }
}
</#if>

</#if>

<#if USART_INTENSET_ERROR = true>
void static ${SERCOM_INSTANCE_NAME}_USART_ISR_ERR_Handler( void )
{
    USART_ERROR errorStatus = (USART_ERROR)(${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_STATUS & (SERCOM_USART_INT_STATUS_PERR_Msk | SERCOM_USART_INT_STATUS_FERR_Msk | SERCOM_USART_INT_STATUS_BUFOVF_Msk <#if USART_FORM == "0x4" || USART_FORM ==     "0x5">| SERCOM_USART_INT_STATUS_ISF_Msk </#if>));

    if(errorStatus != USART_ERROR_NONE)
    {
        /* Save the error to report later */
        ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.errorStatus = errorStatus;

        /* Clear error flags and flush the error bytes */
        ${SERCOM_INSTANCE_NAME}_USART_ErrorClear();

        if(${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rdCallback != NULL)
        {
            ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rdCallback(SERCOM_USART_EVENT_READ_ERROR, ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rdContext);
        }
    }
}
</#if>

<#if USART_RX_ENABLE = true>
void static ${SERCOM_INSTANCE_NAME}_USART_ISR_RX_Handler( void )
{
    <#if USART_INTENSET_ERROR = false>

    USART_ERROR errorStatus = (USART_ERROR)(${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_STATUS & (SERCOM_USART_INT_STATUS_PERR_Msk | SERCOM_USART_INT_STATUS_FERR_Msk | SERCOM_USART_INT_STATUS_BUFOVF_Msk <#if USART_FORM == "0x4" || USART_FORM ==     "0x5">| SERCOM_USART_INT_STATUS_ISF_Msk </#if>));

    if(errorStatus != USART_ERROR_NONE)
    {
        /* Save the error to report later */
        ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.errorStatus = errorStatus;

        /* Clear error flags and flush the error bytes */
        ${SERCOM_INSTANCE_NAME}_USART_ErrorClear();

        if(${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rdCallback != NULL)
        {
            ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rdCallback(SERCOM_USART_EVENT_READ_ERROR, ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rdContext);
        }
    }
    else
    {
        <#if USART_FORM == "0x4" || USART_FORM == "0x5">

        if ((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_INTFLAG & SERCOM_USART_INT_INTFLAG_RXBRK_Msk) == SERCOM_USART_INT_INTFLAG_RXBRK_Msk)
        {
            /* Clear the receive break interrupt flag */
            ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_INTFLAG = (uint8_t)SERCOM_USART_INT_INTFLAG_RXBRK_Msk;

            ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rdCallback(SERCOM_USART_EVENT_BREAK_SIGNAL_DETECTED, ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rdContext);
        }
        if ((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_INTFLAG & SERCOM_USART_INT_INTFLAG_RXC_Msk) == SERCOM_USART_INT_INTFLAG_RXC_Msk)
        {
            if (${SERCOM_INSTANCE_NAME}_USART_RxPushByte( (uint16_t)${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_DATA) == true)
            {
                ${SERCOM_INSTANCE_NAME}_USART_ReadNotificationSend();
            }
            else
            {
                /* UART RX buffer is full */
            }
        }
        <#else>

        while ((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_INTFLAG & SERCOM_USART_INT_INTFLAG_RXC_Msk) == SERCOM_USART_INT_INTFLAG_RXC_Msk)
        {
            if (${SERCOM_INSTANCE_NAME}_USART_RxPushByte( (uint16_t)${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_DATA) == true)
            {
                ${SERCOM_INSTANCE_NAME}_USART_ReadNotificationSend();
            }
            else
            {
                /* UART RX buffer is full */
            }
        }
        </#if>
    }

    <#else>

    <#if USART_FORM == "0x4" || USART_FORM == "0x5">

    if ((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_INTFLAG & SERCOM_USART_INT_INTFLAG_RXBRK_Msk) == SERCOM_USART_INT_INTFLAG_RXBRK_Msk)
    {
        /* Clear the receive break interrupt flag */
        ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_INTFLAG = (uint8_t)SERCOM_USART_INT_INTFLAG_RXBRK_Msk;

        ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rdCallback(SERCOM_USART_EVENT_BREAK_SIGNAL_DETECTED, ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rdContext);
    }
    while ((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_INTFLAG & SERCOM_USART_INT_INTFLAG_RXC_Msk) == SERCOM_USART_INT_INTFLAG_RXC_Msk)
    {
        if (${SERCOM_INSTANCE_NAME}_USART_RxPushByte( (uint16_t)${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_DATA) == true)
        {
            ${SERCOM_INSTANCE_NAME}_USART_ReadNotificationSend();
        }
        else
        {
            /* UART RX buffer is full */
        }
    }
    <#else>

    while ((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_INTFLAG & SERCOM_USART_INT_INTFLAG_RXC_Msk) == SERCOM_USART_INT_INTFLAG_RXC_Msk)
    {
        if (${SERCOM_INSTANCE_NAME}_USART_RxPushByte( (uint16_t)${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_DATA) == true)
        {
            ${SERCOM_INSTANCE_NAME}_USART_ReadNotificationSend();
        }
        else
        {
            /* UART RX buffer is full */
        }
    }
    </#if>
    </#if>
}
</#if>

<#if USART_TX_ENABLE = true>
void static ${SERCOM_INSTANCE_NAME}_USART_ISR_TX_Handler( void )
{
    uint16_t wrByte;

    while ((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_INTFLAG & SERCOM_USART_INT_INTFLAG_DRE_Msk) == SERCOM_USART_INT_INTFLAG_DRE_Msk)
    {
        if (${SERCOM_INSTANCE_NAME}_USART_TxPullByte(&wrByte) == true)
        {
            if (((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_CTRLB & SERCOM_USART_INT_CTRLB_CHSIZE_Msk) >> SERCOM_USART_INT_CTRLB_CHSIZE_Pos) != 0x01U)
            {
                ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_DATA = (uint8_t)wrByte;
            }
            else
            {
                ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_DATA = wrByte;
            }

            ${SERCOM_INSTANCE_NAME}_USART_SendWriteNotification();
        }
        else
        {
            /* Nothing to transmit. Disable the data register empty interrupt. */
            ${SERCOM_INSTANCE_NAME}_USART_TX_INT_DISABLE();
            break;
        }
    }
}
</#if>

void ${SERCOM_INSTANCE_NAME}_USART_InterruptHandler( void )
{
<#if USART_INTENSET_ERROR || USART_TX_ENABLE || USART_RX_ENABLE>
    bool testCondition = false;
</#if>
    if(${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_INTENSET != 0U)
    {
        <#if USART_INTENSET_ERROR = true>
        /* Checks for error flag */
        testCondition = ((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_INTFLAG & SERCOM_USART_INT_INTFLAG_ERROR_Msk) == SERCOM_USART_INT_INTFLAG_ERROR_Msk);
        testCondition = ((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_INTENSET & SERCOM_USART_INT_INTENSET_ERROR_Msk) == SERCOM_USART_INT_INTENSET_ERROR_Msk) && testCondition;
        if(testCondition)
        {
            ${SERCOM_INSTANCE_NAME}_USART_ISR_ERR_Handler();
        }
        </#if>

        <#if USART_TX_ENABLE = true>
        testCondition = ((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_INTFLAG & SERCOM_USART_INT_INTFLAG_DRE_Msk) == SERCOM_USART_INT_INTFLAG_DRE_Msk);
        testCondition = ((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_INTENSET & SERCOM_USART_INT_INTENSET_DRE_Msk) == SERCOM_USART_INT_INTENSET_DRE_Msk) && testCondition;
        /* Checks for data register empty flag */
        if(testCondition)
        {
            ${SERCOM_INSTANCE_NAME}_USART_ISR_TX_Handler();
        }
        </#if>

        <#if USART_RX_ENABLE = true>
        <#if USART_FORM == "0x4" || USART_FORM == "0x5">
        /* Checks for receive complete empty flag */
        testCondition = ((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_INTFLAG & (SERCOM_USART_INT_INTFLAG_RXC_Msk | SERCOM_USART_INT_INTFLAG_RXBRK_Msk)) != 0U);
        testCondition = ((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_INTENSET & (SERCOM_USART_INT_INTENSET_RXC_Msk | SERCOM_USART_INT_INTENSET_RXBRK_Msk)) != 0U) && testCondition;
        if(testCondition)
        {
            ${SERCOM_INSTANCE_NAME}_USART_ISR_RX_Handler();
        }
        <#else>
        /* Checks for receive complete empty flag */
        testCondition = ((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_INTFLAG & SERCOM_USART_INT_INTFLAG_RXC_Msk) != 0U);
        testCondition = ((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_INTENSET & SERCOM_USART_INT_INTENSET_RXC_Msk) != 0U) && testCondition;
        if(testCondition)
        {
            ${SERCOM_INSTANCE_NAME}_USART_ISR_RX_Handler();
        }
        </#if>
        </#if>
    }
}