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

<#if USART_INTERRUPT_MODE_ENABLE = true>
static SERCOM_USART_OBJECT ${SERCOM_INSTANCE_NAME?lower_case}USARTObj;
</#if>

// *****************************************************************************
// *****************************************************************************
// Section: ${SERCOM_INSTANCE_NAME} USART Interface Routines
// *****************************************************************************
// *****************************************************************************

void static ${SERCOM_INSTANCE_NAME}_USART_ErrorClear( void )
{
    uint8_t  u8dummyData = 0U;
    USART_ERROR errorStatus = (USART_ERROR) (${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_STATUS & (uint16_t)(SERCOM_USART_INT_STATUS_PERR_Msk | SERCOM_USART_INT_STATUS_FERR_Msk | SERCOM_USART_INT_STATUS_BUFOVF_Msk ));

    if(errorStatus != USART_ERROR_NONE)
    {
<#if USART_INTENSET_ERROR = true>
        /* Clear error flag */
        ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_INTFLAG = (uint8_t)SERCOM_USART_INT_INTFLAG_ERROR_Msk;
</#if>
        /* Clear all errors */
        ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_STATUS = (uint16_t)(SERCOM_USART_INT_STATUS_PERR_Msk | SERCOM_USART_INT_STATUS_FERR_Msk | SERCOM_USART_INT_STATUS_BUFOVF_Msk);

        /* Flush existing error bytes from the RX FIFO */
        while((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_INTFLAG & (uint8_t)SERCOM_USART_INT_INTFLAG_RXC_Msk) == (uint8_t)SERCOM_USART_INT_INTFLAG_RXC_Msk)
        {
            u8dummyData = (uint8_t)${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_DATA;
        }
    }

    /* Ignore the warning */
    (void)u8dummyData;
}

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
	   <#if USART_INTERRUPT_MODE_ENABLE = true> ${USART_SFDE?then('| SERCOM_USART_INT_CTRLB_SFDE_Msk', '')} </#if>
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
<#if USART_INTERRUPT_MODE_ENABLE = true>

    /* Initialize instance object */
    ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxBuffer = NULL;
    ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxSize = 0;
    ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxProcessedSize = 0;
    ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxBusyStatus = false;
    ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxCallback = NULL;
    ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.txBuffer = NULL;
    ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.txSize = 0;
    ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.txProcessedSize = 0;
    ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.txBusyStatus = false;
    ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.txCallback = NULL;
    ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.errorStatus = USART_ERROR_NONE;
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
<#if USART_FORM == "0x2">
    float f_baudValue      = 0.0f;
    float f_temp           = 0.0f;
    uint32_t fractionPart  = 0U;
</#if>

<#if USART_INTERRUPT_MODE_ENABLE == true>
    bool transferProgress = ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.txBusyStatus;
    transferProgress = ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxBusyStatus || transferProgress; 
    if(transferProgress)
    {
        /* Transaction is in progress, so return without updating settings */
        return setupStatus;
    }

</#if>
    if((serialSetup != NULL) && (serialSetup->baudRate != 0U))
    {
        if(clkFrequency == 0U)
        {
            clkFrequency = ${SERCOM_INSTANCE_NAME}_USART_FrequencyGet();
        }

        <#if USART_SAMPLE_RATE??>
        <#if USART_FORM == "0x2">
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

        if(baudValue != 0U)
        {
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

            <#if USART_FORM == "0x2">
            ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_CTRLA = (${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_CTRLA & ~SERCOM_USART_INT_CTRLA_SAMPR_Msk) | SERCOM_USART_INT_CTRLA_SAMPR(sampleRate);

            ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_CTRLB = (${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_CTRLB & ~(SERCOM_USART_INT_CTRLB_CHSIZE_Msk | SERCOM_USART_INT_CTRLB_SBMODE_Msk)) | ((uint32_t) serialSetup->dataWidth | (uint32_t) serialSetup->stopBits);
            <#else>
            /* Configure Parity Options */
            if(serialSetup->parity == USART_PARITY_NONE)
            {
                ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_CTRLA = <#if USART_SAMPLE_RATE??> (${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_CTRLA & ~(SERCOM_USART_INT_CTRLA_SAMPR_Msk | SERCOM_USART_INT_CTRLA_FORM_Msk)) | SERCOM_USART_INT_CTRLA_FORM(0x0UL) | SERCOM_USART_INT_CTRLA_SAMPR((uint32_t)sampleRate); <#else>
                (${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_CTRLA & ~SERCOM_USART_INT_CTRLA_FORM_Msk) | SERCOM_USART_INT_CTRLA_FORM(0x0);
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

            setupStatus = true;
        }
    }

    return setupStatus;
}

<#if USART_INTERRUPT_MODE_ENABLE = true>
USART_ERROR ${SERCOM_INSTANCE_NAME}_USART_ErrorGet( void )
{
    USART_ERROR errorStatus = ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.errorStatus;

    ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.errorStatus = USART_ERROR_NONE;

    return errorStatus;
}
<#else>
USART_ERROR ${SERCOM_INSTANCE_NAME}_USART_ErrorGet( void )
{
    USART_ERROR errorStatus = (USART_ERROR) (${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_STATUS & (uint16_t)(SERCOM_USART_INT_STATUS_PERR_Msk | SERCOM_USART_INT_STATUS_FERR_Msk | SERCOM_USART_INT_STATUS_BUFOVF_Msk ));

    if(errorStatus != USART_ERROR_NONE)
    {
        ${SERCOM_INSTANCE_NAME}_USART_ErrorClear();
    }

    return errorStatus;
}
</#if>

<#if USART_TX_ENABLE = true>

void ${SERCOM_INSTANCE_NAME}_USART_TransmitterEnable( void )
{
    ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_CTRLB |= SERCOM_USART_INT_CTRLB_TXEN_Msk;

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
}

void ${SERCOM_INSTANCE_NAME}_USART_TransmitterDisable( void )
{
    ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_CTRLB &= ~SERCOM_USART_INT_CTRLB_TXEN_Msk;

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
}

bool ${SERCOM_INSTANCE_NAME}_USART_Write( void *buffer, const size_t size )
{
    bool writeStatus      = false;
<#if USART_INTERRUPT_MODE_ENABLE = false>
    uint8_t *pu8Data      = (uint8_t*)buffer;
    uint16_t *pu16Data    = (uint16_t*)buffer;
    uint32_t u32Index     = 0U;
<#else>
    uint32_t processedSize = 0U;
</#if>

    if(buffer != NULL)
    {
<#if USART_INTERRUPT_MODE_ENABLE = false>
        /* Blocks while buffer is being transferred */
        while(u32Index < size)
        {
            /* Check if USART is ready for new data */
            while((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_INTFLAG & (uint8_t)SERCOM_USART_INT_INTFLAG_DRE_Msk) == 0U)
            {
                /* Do nothing */
            }

            /* Write data to USART module */
            if (((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_CTRLB & SERCOM_USART_INT_CTRLB_CHSIZE_Msk) >> SERCOM_USART_INT_CTRLB_CHSIZE_Pos) != 0x01U)
            {
                /* 8-bit mode */
                ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_DATA = pu8Data[u32Index];
            }
            else
            {
                /* 9-bit mode */
                ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_DATA = pu16Data[u32Index];
            }

            /* Increment index */
            u32Index++;
        }
        writeStatus = true;
<#else>
        if(${SERCOM_INSTANCE_NAME?lower_case}USARTObj.txBusyStatus == false)
        {
            ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.txBuffer = buffer;
            ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.txSize = size;
            ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.txBusyStatus = true;

            /* Initiate the transfer by sending first byte */
            while (((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_INTFLAG & SERCOM_USART_INT_INTFLAG_DRE_Msk) == SERCOM_USART_INT_INTFLAG_DRE_Msk) &&
                    (processedSize < ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.txSize))
            {
                if (((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_CTRLB & SERCOM_USART_INT_CTRLB_CHSIZE_Msk) >> SERCOM_USART_INT_CTRLB_CHSIZE_Pos) != 0x01U)
                {
                    /* 8-bit mode */
                    ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_DATA = ((uint8_t*)(buffer))[processedSize];
                }
                else
                {
                    /* 9-bit mode */
                    ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_DATA = ((uint16_t*)(buffer))[processedSize];
                }
                processedSize += 1U;
            }
            ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.txProcessedSize = processedSize;
            ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_INTENSET = (uint8_t)SERCOM_USART_INT_INTFLAG_DRE_Msk;

            writeStatus = true;
        }
</#if>
    }

    return writeStatus;
}

<#if USART_FORM == "0x2">
bool ${SERCOM_INSTANCE_NAME}_USART_LIN_CommandSet(USART_LIN_MASTER_CMD cmd)
{
    /* Command strobe bits cannot be set while transmitter is busy */

    <#if USART_INTERRUPT_MODE_ENABLE = true>
    if((${SERCOM_INSTANCE_NAME?lower_case}USARTObj.txBusyStatus == false) && ((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_STATUS & SERCOM_USART_INT_STATUS_TXE_Msk)!= 0U))
    <#else>
    if((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_STATUS & SERCOM_USART_INT_STATUS_TXE_Msk) != 0U)
    </#if>
    {
        /* Clear the flag */
        ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_STATUS = SERCOM_USART_INT_STATUS_TXE_Msk;

        ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_CTRLB |= ((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_CTRLB & ~SERCOM_USART_INT_CTRLB_LINCMD_Msk) | (uint16_t)cmd);

        return true;
    }
    else
    {
        return false;
    }
}
</#if>

<#if USART_INTERRUPT_MODE_ENABLE = true>
bool ${SERCOM_INSTANCE_NAME}_USART_WriteIsBusy( void )
{
    return ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.txBusyStatus;
}

size_t ${SERCOM_INSTANCE_NAME}_USART_WriteCountGet( void )
{
    return ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.txProcessedSize;
}

void ${SERCOM_INSTANCE_NAME}_USART_WriteCallbackRegister( SERCOM_USART_CALLBACK callback, uintptr_t context )
{
    ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.txCallback = callback;

    ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.txContext = context;
}

<#else>
bool ${SERCOM_INSTANCE_NAME}_USART_TransmitterIsReady( void )
{
    bool transmitterStatus = false;

    if ((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_INTFLAG & SERCOM_USART_INT_INTFLAG_DRE_Msk) == SERCOM_USART_INT_INTFLAG_DRE_Msk)
    {
        transmitterStatus = true;
    }

    return transmitterStatus;
}

void ${SERCOM_INSTANCE_NAME}_USART_WriteByte( int data )
{
    /* Check if USART is ready for new data */
    while((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_INTFLAG & SERCOM_USART_INT_INTFLAG_DRE_Msk) == 0U)
    {
        /* Do nothing */
    }

    ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_DATA = (uint16_t)data;
}
</#if>
</#if>

bool ${SERCOM_INSTANCE_NAME}_USART_TransmitComplete( void )
{
    bool transmitComplete = false;

    if ((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_INTFLAG & SERCOM_USART_INT_INTFLAG_TXC_Msk) == SERCOM_USART_INT_INTFLAG_TXC_Msk)
    {
        transmitComplete = true;
    }

    return transmitComplete;
}

<#if USART_RX_ENABLE = true>
void ${SERCOM_INSTANCE_NAME}_USART_ReceiverEnable( void )
{
    ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_CTRLB |= SERCOM_USART_INT_CTRLB_RXEN_Msk;

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
}

void ${SERCOM_INSTANCE_NAME}_USART_ReceiverDisable( void )
{
    ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_CTRLB &= ~SERCOM_USART_INT_CTRLB_RXEN_Msk;

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
}

bool ${SERCOM_INSTANCE_NAME}_USART_Read( void *buffer, const size_t size )
{
    bool readStatus         = false;
<#if USART_INTERRUPT_MODE_ENABLE = false>
    uint8_t* pu8Data        = (uint8_t*)buffer;
    uint16_t *pu16Data      = (uint16_t*)buffer;
    uint32_t u32Index       = 0U;
    USART_ERROR errorStatus = USART_ERROR_NONE;
</#if>

    if(buffer != NULL)
    {
<#if USART_INTERRUPT_MODE_ENABLE = false>

        /* Clear error flags and flush out error data that may have been received when no active request was pending */
        ${SERCOM_INSTANCE_NAME}_USART_ErrorClear();

        while(u32Index < size)
        {
            /* Check if USART has new data */
            while((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_INTFLAG & SERCOM_USART_INT_INTFLAG_RXC_Msk) == 0U)
            {
                /* Do nothing */
            }

            errorStatus = (USART_ERROR) (${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_STATUS & (uint16_t)(SERCOM_USART_INT_STATUS_PERR_Msk | SERCOM_USART_INT_STATUS_FERR_Msk | SERCOM_USART_INT_STATUS_BUFOVF_Msk));

            if(errorStatus != USART_ERROR_NONE)
            {
                break;
            }

            if (((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_CTRLB & SERCOM_USART_INT_CTRLB_CHSIZE_Msk) >> SERCOM_USART_INT_CTRLB_CHSIZE_Pos) != 0x01U)
            {
                /* 8-bit mode */
                pu8Data[u32Index] = (uint8_t)${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_DATA;
            }
            else
            {
                /* 9-bit mode */
                pu16Data[u32Index] = (uint16_t)${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_DATA;
            }

            /* Increment index */
            u32Index++;
        }

        if(size == u32Index)
        {
            readStatus = true;
        }
<#else>
        if(${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxBusyStatus == false)
        {
            /* Clear error flags and flush out error data that may have been received when no active request was pending */
            ${SERCOM_INSTANCE_NAME}_USART_ErrorClear();

            ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxBuffer = buffer;
            ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxSize = size;
            ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxProcessedSize = 0U;
            ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxBusyStatus = true;
            ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.errorStatus = USART_ERROR_NONE;

            readStatus = true;

            <#if USART_INTENSET_ERROR = true>
            /* Enable receive and error interrupt */
            ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_INTENSET = (uint8_t)(SERCOM_USART_INT_INTENSET_ERROR_Msk | SERCOM_USART_INT_INTENSET_RXC_Msk);
            <#else>
            /* Enable Receive Complete interrupt */
            ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_INTENSET =  (uint8_t)SERCOM_USART_INT_INTENSET_RXC_Msk;
            </#if>
        }
</#if>
    }

    return readStatus;
}

<#if USART_INTERRUPT_MODE_ENABLE = true>
bool ${SERCOM_INSTANCE_NAME}_USART_ReadIsBusy( void )
{
    return ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxBusyStatus;
}

size_t ${SERCOM_INSTANCE_NAME}_USART_ReadCountGet( void )
{
    return ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxProcessedSize;
}

bool ${SERCOM_INSTANCE_NAME}_USART_ReadAbort(void)
{
    if (${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxBusyStatus == true)
    {
        <#if USART_INTENSET_ERROR = true>
        /* Disable receive and error interrupt */
        ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_INTENCLR = (uint8_t)(SERCOM_USART_INT_INTENCLR_ERROR_Msk | SERCOM_USART_INT_INTENCLR_RXC_Msk);
        <#else>
         /* Disable the receive interrupt */
        ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_INTENCLR = (uint8_t)(SERCOM_USART_INT_INTENCLR_RXC_Msk);
        </#if>

        ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxBusyStatus = false;

        /* If required application should read the num bytes processed prior to calling the read abort API */
        ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxSize = ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxProcessedSize = 0U;
    }

    return true;
}

void ${SERCOM_INSTANCE_NAME}_USART_ReadCallbackRegister( SERCOM_USART_CALLBACK callback, uintptr_t context )
{
    ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxCallback = callback;

    ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxContext = context;
}
<#else>
bool ${SERCOM_INSTANCE_NAME}_USART_ReceiverIsReady( void )
{
    bool receiverStatus = false;

    if ((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_INTFLAG & SERCOM_USART_INT_INTFLAG_RXC_Msk) == SERCOM_USART_INT_INTFLAG_RXC_Msk)
    {
        receiverStatus = true;
    }

    return receiverStatus;
}

int ${SERCOM_INSTANCE_NAME}_USART_ReadByte( void )
{
    return (int)${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_DATA;
}
</#if>
</#if>

<#if USART_INTERRUPT_MODE_ENABLE = true>

<#if USART_INTENSET_ERROR = true>
void static ${SERCOM_INSTANCE_NAME}_USART_ISR_ERR_Handler( void )
{
    USART_ERROR errorStatus = USART_ERROR_NONE;

    errorStatus = (USART_ERROR) (${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_STATUS & (uint16_t)(SERCOM_USART_INT_STATUS_PERR_Msk | SERCOM_USART_INT_STATUS_FERR_Msk | SERCOM_USART_INT_STATUS_BUFOVF_Msk));

    if(errorStatus != USART_ERROR_NONE)
    {
        /* Save the error to be reported later */
        ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.errorStatus = errorStatus;

        /* Clear the error flags and flush out the error bytes */
        ${SERCOM_INSTANCE_NAME}_USART_ErrorClear();

        /* Disable error and receive interrupt to abort on-going transfer */
        ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_INTENCLR = (uint8_t)(SERCOM_USART_INT_INTENCLR_ERROR_Msk | SERCOM_USART_INT_INTENCLR_RXC_Msk);

        /* Clear the RX busy flag */
        ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxBusyStatus = false;

        if(${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxCallback != NULL)
        {
            ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxCallback(${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxContext);
        }
    }
}
</#if>

<#if USART_RX_ENABLE = true>
void static ${SERCOM_INSTANCE_NAME}_USART_ISR_RX_Handler( void )
{
    uint16_t temp;

<#if USART_INTENSET_ERROR = false>
    USART_ERROR errorStatus = (USART_ERROR) (${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_STATUS & (uint16_t)(SERCOM_USART_INT_STATUS_PERR_Msk | SERCOM_USART_INT_STATUS_FERR_Msk | SERCOM_USART_INT_STATUS_BUFOVF_Msk));
</#if>

    if(${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxBusyStatus == true)
    {
        if(${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxProcessedSize < ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxSize)
        {
            <#if USART_INTENSET_ERROR = false>
            if (errorStatus != USART_ERROR_NONE)
            {
                /* Save the error to be reported later */
                ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.errorStatus = errorStatus;

                /* Clear the error flags and flush out the error bytes */
                ${SERCOM_INSTANCE_NAME}_USART_ErrorClear();

                ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxBusyStatus = false;
                ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxSize = 0U;

                ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_INTENCLR = (uint8_t)SERCOM_USART_INT_INTENCLR_RXC_Msk;

                if(${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxCallback != NULL)
                {
                    ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxCallback(${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxContext);
                }
            }
            else
            {
                temp = (uint16_t)${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_DATA;

                if (((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_CTRLB & SERCOM_USART_INT_CTRLB_CHSIZE_Msk) >> SERCOM_USART_INT_CTRLB_CHSIZE_Pos) != 0x01U)
                {
                    /* 8-bit mode */
                    ((uint8_t*)${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxBuffer)[${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxProcessedSize] = (uint8_t)(temp);
                }
                else
                {
                    /* 9-bit mode */
                    ((uint16_t*)${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxBuffer)[${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxProcessedSize] = temp;
                }

                /* Increment processed size */
                ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxProcessedSize++;

                if(${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxProcessedSize == ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxSize)
                {
                    ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxBusyStatus = false;
                    ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxSize = 0U;
                    ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_INTENCLR = (uint8_t)SERCOM_USART_INT_INTENCLR_RXC_Msk;

                    if(${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxCallback != NULL)
                    {
                        ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxCallback(${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxContext);
                    }
                }
            }
            <#else>
            temp = (uint16_t)${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_DATA;

            if (((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_CTRLB & SERCOM_USART_INT_CTRLB_CHSIZE_Msk) >> SERCOM_USART_INT_CTRLB_CHSIZE_Pos) != 0x01U)
            {
                /* 8-bit mode */
                ((uint8_t*)${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxBuffer)[${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxProcessedSize] = (uint8_t) (temp);
            }
            else
            {
                /* 9-bit mode */
                ((uint16_t*)${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxBuffer)[${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxProcessedSize] = temp;
            }

            /* Increment processed size */
            ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxProcessedSize++;

            if(${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxProcessedSize == ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxSize)
            {
                ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxBusyStatus = false;
                ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxSize = 0U;
                ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_INTENCLR = (uint8_t)(SERCOM_USART_INT_INTENCLR_RXC_Msk | SERCOM_USART_INT_INTENCLR_ERROR_Msk);

                if(${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxCallback != NULL)
                {
                    ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxCallback(${SERCOM_INSTANCE_NAME?lower_case}USARTObj.rxContext);
                }
            }
            </#if>

        }
    }
}
</#if>

<#if USART_TX_ENABLE = true>
void static ${SERCOM_INSTANCE_NAME}_USART_ISR_TX_Handler( void )
{
    bool  dataRegisterEmpty= false;
    bool  dataAvailable = false;
    if(${SERCOM_INSTANCE_NAME?lower_case}USARTObj.txBusyStatus == true)
    {
        dataAvailable = (${SERCOM_INSTANCE_NAME?lower_case}USARTObj.txProcessedSize < ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.txSize);
        dataRegisterEmpty = ((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_INTFLAG & SERCOM_USART_INT_INTFLAG_DRE_Msk) == SERCOM_USART_INT_INTFLAG_DRE_Msk);
        
        while(dataRegisterEmpty && dataAvailable)
        {
            if (((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_CTRLB & SERCOM_USART_INT_CTRLB_CHSIZE_Msk) >> SERCOM_USART_INT_CTRLB_CHSIZE_Pos) != 0x01U)
            {
                /* 8-bit mode */
                ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_DATA = ((uint8_t*)${SERCOM_INSTANCE_NAME?lower_case}USARTObj.txBuffer)[${SERCOM_INSTANCE_NAME?lower_case}USARTObj.txProcessedSize];
            }
            else
            {
                /* 9-bit mode */
                ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_DATA = ((uint16_t*)${SERCOM_INSTANCE_NAME?lower_case}USARTObj.txBuffer)[${SERCOM_INSTANCE_NAME?lower_case}USARTObj.txProcessedSize];
            }
            /* Increment processed size */
            ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.txProcessedSize++;

            dataAvailable = (${SERCOM_INSTANCE_NAME?lower_case}USARTObj.txProcessedSize < ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.txSize);
            dataRegisterEmpty = ((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_INTFLAG & SERCOM_USART_INT_INTFLAG_DRE_Msk) == SERCOM_USART_INT_INTFLAG_DRE_Msk);
        }

        if(${SERCOM_INSTANCE_NAME?lower_case}USARTObj.txProcessedSize >= ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.txSize)
        {
            ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.txBusyStatus = false;
            ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.txSize = 0U;
            ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_INTENCLR = (uint8_t)SERCOM_USART_INT_INTENCLR_DRE_Msk;

            if(${SERCOM_INSTANCE_NAME?lower_case}USARTObj.txCallback != NULL)
            {
                ${SERCOM_INSTANCE_NAME?lower_case}USARTObj.txCallback(${SERCOM_INSTANCE_NAME?lower_case}USARTObj.txContext);
            }
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
        testCondition = ((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_INTFLAG & SERCOM_USART_INT_INTFLAG_RXC_Msk) == SERCOM_USART_INT_INTFLAG_RXC_Msk);
        testCondition = ((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_INTENSET & SERCOM_USART_INT_INTENSET_RXC_Msk) == SERCOM_USART_INT_INTENSET_RXC_Msk) && testCondition;
        /* Checks for receive complete empty flag */
        if(testCondition)
        {
            ${SERCOM_INSTANCE_NAME}_USART_ISR_RX_Handler();
        }
        </#if>
    }
}
</#if>
