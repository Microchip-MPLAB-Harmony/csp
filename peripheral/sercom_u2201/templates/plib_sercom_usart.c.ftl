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
* © 2018 Microchip Technology Inc. and its subsidiaries.
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
/* This section lists the other files that are included in this file.
*/

#include "plib_${SERCOM_INSTANCE_NAME?lower_case}_usart.h"

// *****************************************************************************
// *****************************************************************************
// Section: Global Data
// *****************************************************************************
// *****************************************************************************

/* Macros to be added to the header file in the packs */
/* 5 Bits character size frame for data transfer */
#define SERCOM_USART_CTRLB_CHSIZE_5BITS                                 (0x5u)

/* 6 Bits character size frame for data transfer */
#define SERCOM_USART_CTRLB_CHSIZE_6BITS                                 (0x6u)

/* 7 Bits character size frame for data transfer */
#define SERCOM_USART_CTRLB_CHSIZE_7BITS                                 (0x7u)

/* 8 Bits character size frame for data transfer */
#define SERCOM_USART_CTRLB_CHSIZE_8BITS                                 (0x0u)

/* 9 Bits character size frame for data transfer */
#define SERCOM_USART_CTRLB_CHSIZE_9BITS                                 (0x1u)

/* 1 Stop Bit mode frame for data transfer */
#define SERCOM_USART_CTRLB_SBMODE_1BIT                                  (0x0u)

/* 2 Bits Stop mode frame for data transfer */
#define SERCOM_USART_CTRLB_SBMODE_2BITS                                 (0x1u)

/* USART Frame without Parity */
#define SERCOM_USART_FRAME_PARITY_NONE                                  (0x2u)

/* USART Frame with Odd Parity */
#define SERCOM_USART_FRAME_PARITY_ODD                                   (0x1u)

/* USART Frame with Even Parity */
#define SERCOM_USART_FRAME_PARITY_EVEN                                  (0x0u)

/* USART External Clock Mode */
#define SERCOM_USART_EXT_CLK                                            (0x0u)

/* USART Internal Clock Mode */
#define SERCOM_USART_INT_CLK                                            (0x1u)

/* USART Even Parity */
#define SERCOM_USART_CTRLB_PMODE_EVEN                                   (0x0u)

/* USART Odd Parity */
#define SERCOM_USART_CTRLB_PMODE_ODD                                    (0x1u)

/* SERCOM PAD 0 RXPO */
#define SERCOM_PAD0_RXPO                                                (0x0u)

/* SERCOM PAD 1 RXPO */
#define SERCOM_PAD1_RXPO                                                (0x1u)

/* SERCOM PAD 2 RXPO */
#define SERCOM_PAD2_RXPO                                                (0x2u)

/* SERCOM PAD 3 RXPO */
#define SERCOM_PAD3_RXPO                                                (0x3u)

/* SERCOM PAD 0 TXPO */
#define SERCOM_PAD0_TXPO                                                (0x0u)

/* SERCOM PAD 1 TXPO */
#define SERCOM_PAD2_TXPO                                                (0x1u)

/* SERCOM ERROR MASK */
#define SERCOM_USART_ERROR_Msk                                          (0x3u)

/* SERCOM BAUD MAX RANGE */
#define SERCOM_BAUD_RATE_MAX_RANGE                                (0xFFFFFFFF)

/* Baud rate arithmetic part max value */
#define SERCOM_BAUD_RATE_ARITHMETIC_PART_MAX                         (0x1FFFu)

/* Baud rate fractional part max value */
#define SERCOM_BAUD_RATE_FRACTIONAL_PART_MAX                            (0x7u)

/* Calculation for arithmetic part of baud value */
#define BAUD_VAL                         (4000000 / (16 * ${USART_BAUD_RATE}))

/* Calculation for fractional part of baud value */
#define FP_VAL            ((4000000 / ${USART_BAUD_RATE} - 16 * BAUD_VAL) / 2)

<#if USART_SERIAL_SETUP_ENABLE = true>
USART_SERIAL_SETUP ${SERCOM_INSTANCE_NAME?lower_case}usartSerialConf;
</#if>

SERCOM_USART_OBJECT ${SERCOM_INSTANCE_NAME?lower_case}usartObj;

<#if USART_INTERRUPT_MODE = true>
// *****************************************************************************
// *****************************************************************************
// Section: Interrupt Routines
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Function:
    void ${SERCOM_INSTANCE_NAME}_USART_ISR_ERR_Handler( void )

  Summary:
    Handles error interrupt.

  Description:
    This function reads the errors occured during transfer and after clearing
    the errors in the hardware invokes the callback.

  Remarks:
    None.
*/

void static ${SERCOM_INSTANCE_NAME}_USART_ISR_ERR_Handler( void )
{
    USART_ERROR errorStatus = USART_ERROR_NONE;
    uint8_t  u8dummyData = 0;

    errorStatus = (${SERCOM_INSTANCE_NAME}_REGS->USART.STATUS &
                  (SERCOM_USART_STATUS_PERR_Msk |
                  SERCOM_USART_STATUS_FERR_Msk |
                  SERCOM_USART_STATUS_BUFOVF_Msk));

    if(errorStatus != USART_ERROR_NONE)
    {
        /* Clear all error flags */
        ${SERCOM_INSTANCE_NAME}_REGS->USART.INTFLAG = SERCOM_USART_INTFLAG_ERROR_Msk;

        /* Clear error statuses */
        ${SERCOM_INSTANCE_NAME}_REGS->USART.STATUS = SERCOM_USART_STATUS_Msk;

        /* Flush existing error bytes from the RX FIFO */
        while((${SERCOM_INSTANCE_NAME}_REGS->USART.INTFLAG & SERCOM_USART_INTFLAG_RXC_Msk) == SERCOM_USART_INTFLAG_RXC_Msk)
        {
            u8dummyData = ${SERCOM_INSTANCE_NAME}_REGS->USART.DATA;
        }

        /* Ignore the warning */
        (void)u8dummyData;

        if( ${SERCOM_INSTANCE_NAME?lower_case}usartObj.rxCallback != NULL )
        {
            ${SERCOM_INSTANCE_NAME?lower_case}usartObj.rxCallback(${SERCOM_INSTANCE_NAME?lower_case}usartObj.rxContext);
        }
    }
}

<#if USART_RX_ENABLE = true>
// *****************************************************************************
/* Function:
    void ${SERCOM_INSTANCE_NAME}_USART_ISR_RX_Handler( void )

  Summary:
    Handles USART receive interrupt.

  Description:
    This function reads the data once the receive interrupt occurs.
    Once the transaction is completed it invokes the callback.

  Remarks:
    None.
*/

void static ${SERCOM_INSTANCE_NAME}_USART_ISR_RX_Handler( void )
{
    if(${SERCOM_INSTANCE_NAME?lower_case}usartObj.rxBusyStatus == true)
    {
        if(${SERCOM_INSTANCE_NAME?lower_case}usartObj.rxSize >= ${SERCOM_INSTANCE_NAME?lower_case}usartObj.rxProcessedSize)
        {
            if(${SERCOM_INSTANCE_NAME?lower_case}usartObj.rxSize == ${SERCOM_INSTANCE_NAME?lower_case}usartObj.rxProcessedSize)
            {
                ${SERCOM_INSTANCE_NAME?lower_case}usartObj.rxBusyStatus = false;
                ${SERCOM_INSTANCE_NAME?lower_case}usartObj.rxSize = 0;
                ${SERCOM_INSTANCE_NAME}_REGS->USART.INTENCLR = SERCOM_USART_INTENCLR_RXC_Msk;

                if(${SERCOM_INSTANCE_NAME?lower_case}usartObj.rxCallback != NULL)
                {
                    ${SERCOM_INSTANCE_NAME?lower_case}usartObj.rxCallback(${SERCOM_INSTANCE_NAME?lower_case}usartObj.rxContext);
                }
            }
            else
            {
                ${SERCOM_INSTANCE_NAME}_REGS->USART.INTFLAG = SERCOM_USART_INTFLAG_RXC_Msk;

                ${SERCOM_INSTANCE_NAME?lower_case}usartObj.rxBuffer[${SERCOM_INSTANCE_NAME?lower_case}usartObj.rxProcessedSize++] = ${SERCOM_INSTANCE_NAME}_REGS->USART.DATA;
            }
        }
    }
}
</#if>

<#if USART_TX_ENABLE = true>
// *****************************************************************************
/* Function:
    void ${SERCOM_INSTANCE_NAME}_USART_ISR_TX_Handler( void )

  Summary:
    Handles USART Transmit interrupt .

  Description:
    This function transmits the data once the transmit interrupt occurs.
    Once the transaction is completed it invokes the callback.

  Remarks:
    None.
*/

void static ${SERCOM_INSTANCE_NAME}_USART_ISR_TX_Handler( void )
{
    if(${SERCOM_INSTANCE_NAME?lower_case}usartObj.txBusyStatus == true)
    {
        if(${SERCOM_INSTANCE_NAME?lower_case}usartObj.txSize >= ${SERCOM_INSTANCE_NAME?lower_case}usartObj.txProcessedSize)
        {
            if(${SERCOM_INSTANCE_NAME?lower_case}usartObj.txSize == ${SERCOM_INSTANCE_NAME?lower_case}usartObj.txProcessedSize)
            {
                ${SERCOM_INSTANCE_NAME?lower_case}usartObj.txBusyStatus = false;
                ${SERCOM_INSTANCE_NAME?lower_case}usartObj.txSize = 0;
                ${SERCOM_INSTANCE_NAME}_REGS->USART.INTENCLR = SERCOM_USART_INTENCLR_DRE_Msk;

                if(${SERCOM_INSTANCE_NAME?lower_case}usartObj.txCallback != NULL)
                {
                    ${SERCOM_INSTANCE_NAME?lower_case}usartObj.txCallback(${SERCOM_INSTANCE_NAME?lower_case}usartObj.txContext);
                }
            }
            else
            {
                ${SERCOM_INSTANCE_NAME}_REGS->USART.INTFLAG = SERCOM_USART_INTFLAG_DRE_Msk;

                ${SERCOM_INSTANCE_NAME}_REGS->USART.DATA = ${SERCOM_INSTANCE_NAME?lower_case}usartObj.txBuffer[${SERCOM_INSTANCE_NAME?lower_case}usartObj.txProcessedSize++];
            }
        }
    }
}
</#if>
</#if>

// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************
/* The following functions make up the methods (set of possible operations) of
this interface.
*/

// *****************************************************************************
/* Function:
    void ${SERCOM_INSTANCE_NAME}_USART_Initialize( void )

  Summary:
    Initializes given instance of the USART peripheral.

  Description:
    This function initializes the given instance of the USART peripheral as
    configured by the user from within the MHC.

  Remarks:
    Refer plib_${SERCOM_INSTANCE_NAME?lower_case}_usart.h file for more information.
*/

void ${SERCOM_INSTANCE_NAME}_USART_Initialize( void )
{
    /* Disable the USART before configurations */
    ${SERCOM_INSTANCE_NAME}_REGS->USART.CTRLA &= ~SERCOM_USART_CTRLA_ENABLE_Msk;

    while((${SERCOM_INSTANCE_NAME}_REGS->USART.SYNCBUSY & SERCOM_USART_SYNCBUSY_ENABLE_Msk) == SERCOM_USART_SYNCBUSY_ENABLE_Msk)
    {
        /* Wait for sync */
    }

    /* Configures USART Clock Mode */
    ${SERCOM_INSTANCE_NAME}_REGS->USART.CTRLA |= SERCOM_USART_CTRLA_MODE(${(SERCOM_MODE == "USART_EXT")?then('SERCOM_USART_EXT_CLK' , 'SERCOM_USART_INT_CLK')});

    /*
     * Configures TXPO and RXPO
     * Configures Data Order
     * Configures Standby Mode
     * Configures sampling rate
     * Configures IBON
     */
    <@compress single_line=true>${SERCOM_INSTANCE_NAME}_REGS->USART.CTRLA |= SERCOM_USART_CTRLA_RXPO(${USART_RXPO}_RXPO) |
                                                                             SERCOM_USART_CTRLA_TXPO(${USART_TXPO}_TXPO) |
                                                                             SERCOM_USART_CTRLA_DORD_Msk |
                                                                             SERCOM_USART_CTRLA_SAMPR(1) |
                                                                             SERCOM_USART_CTRLA_IBON_Msk
                                                                             ${USART_RUNSTDBY?then('| SERCOM_USART_CTRLA_RUNSTDBY_Msk', '')};</@compress>

<#if USART_PARITY_MODE = "ODD">
    /* Configure Parity */
    ${SERCOM_INSTANCE_NAME}_REGS->USART.CTRLA |= SERCOM_USART_CTRLA_FORM(1);
    ${SERCOM_INSTANCE_NAME}_REGS->USART.CTRLB |= SERCOM_USART_CTRLB_PMODE_Msk;
</#if>
<#if USART_PARITY_MODE = "EVEN">
    ${SERCOM_INSTANCE_NAME}_REGS->USART.CTRLA |= SERCOM_USART_CTRLA_FORM(1);
</#if>
<#if USART_PARITY_MODE = "NONE">
    ${SERCOM_INSTANCE_NAME}_REGS->USART.CTRLA |= SERCOM_USART_CTRLA_FORM(0);
</#if>

<#if USART_STOP_BIT = "2BITS">
    /* Configure Stop bits */
    ${SERCOM_INSTANCE_NAME}_REGS->USART.CTRLB |= SERCOM_USART_CTRLB_SBMODE_Msk;
</#if>

    /* Configure Baud Rate */
    ${SERCOM_INSTANCE_NAME}_REGS->USART.BAUD = SERCOM_USART_BAUD_BAUD_FRAC_MODE(BAUD_VAL) | SERCOM_USART_BAUD_FP(FP_VAL);

    /* Enable transmitter and receive enable RXEN TXEN */
    <@compress single_line=true>${SERCOM_INSTANCE_NAME}_REGS->USART.CTRLB |= SERCOM_USART_CTRLB_CHSIZE(SERCOM_USART_CTRLB_CHSIZE_${USART_CHARSIZE_BITS})
                                                                             ${USART_RX_ENABLE?then('| SERCOM_USART_CTRLB_RXEN_Msk', '')}
                                                                             ${USART_TX_ENABLE?then('| SERCOM_USART_CTRLB_TXEN_Msk', '')};</@compress>

    while((${SERCOM_INSTANCE_NAME}_REGS->USART.SYNCBUSY & SERCOM_USART_SYNCBUSY_CTRLB_Msk) == SERCOM_USART_SYNCBUSY_CTRLB_Msk)
    {
        /* Wait for sync */
    }

    /* Enable the UART after the configurations */
    ${SERCOM_INSTANCE_NAME}_REGS->USART.CTRLA |= SERCOM_USART_CTRLA_ENABLE_Msk;

    while((${SERCOM_INSTANCE_NAME}_REGS->USART.SYNCBUSY & SERCOM_USART_SYNCBUSY_ENABLE_Msk) == SERCOM_USART_SYNCBUSY_ENABLE_Msk)
    {
        /* Wait for sync */
    }

<#if USART_SERIAL_SETUP_ENABLE = true>
    ${SERCOM_INSTANCE_NAME?lower_case}usartSerialConf.baud = ${USART_BAUD_RATE};
    ${SERCOM_INSTANCE_NAME?lower_case}usartSerialConf.charSize = SERCOM_USART_CTRLB_CHSIZE_${USART_CHARSIZE_BITS};
<#if USART_PARITY_MODE = "EVEN" | USART_PARITY_MODE = "ODD">
    ${SERCOM_INSTANCE_NAME?lower_case}usartSerialConf.parityEnable = true;
    ${SERCOM_INSTANCE_NAME?lower_case}usartSerialConf.parity = SERCOM_USART_CTRLB_PMODE_${USART_PARITY_MODE};
<#else>
    ${SERCOM_INSTANCE_NAME?lower_case}usartSerialConf.parityEnable = false;
</#if>
    ${SERCOM_INSTANCE_NAME?lower_case}usartSerialConf.stopBits = SERCOM_USART_CTRLB_SBMODE_${USART_STOP_BIT};
</#if>

<#if USART_INTERRUPT_MODE = true>
    /* Initialize instance object */
    ${SERCOM_INSTANCE_NAME?lower_case}usartObj.rxBuffer = NULL;
    ${SERCOM_INSTANCE_NAME?lower_case}usartObj.rxSize = 0;
    ${SERCOM_INSTANCE_NAME?lower_case}usartObj.rxProcessedSize = 0;
    ${SERCOM_INSTANCE_NAME?lower_case}usartObj.rxBusyStatus = false;
    ${SERCOM_INSTANCE_NAME?lower_case}usartObj.rxCallback = NULL;
    ${SERCOM_INSTANCE_NAME?lower_case}usartObj.txBuffer = NULL;
    ${SERCOM_INSTANCE_NAME?lower_case}usartObj.txSize = 0;
    ${SERCOM_INSTANCE_NAME?lower_case}usartObj.txProcessedSize = 0;
    ${SERCOM_INSTANCE_NAME?lower_case}usartObj.txBusyStatus = false;
    ${SERCOM_INSTANCE_NAME?lower_case}usartObj.txCallback = NULL;
</#if>
}

<#if USART_SERIAL_SETUP_ENABLE = true>
// *****************************************************************************
/* Function:
    bool ${SERCOM_INSTANCE_NAME}_USART_SerialSetup( uint32_t clkFrequency,
                                              USART_SERIAL_SETUP * serialSetup )

  Summary:
    Sets up serial configurations for usart peripheral.

  Description:
    This function sets all the serial configurations of the peripheral.
    It provides run-time interface to configure the baud, parity,
    stop bits and data character size parameters of the serial connection

  Remarks:
    Refer plib_${SERCOM_INSTANCE_NAME?lower_case}_usart.h file for more information.
*/

bool ${SERCOM_INSTANCE_NAME}_USART_SerialSetup( uint32_t clkFrequency, USART_SERIAL_SETUP * serialSetup )
{
    bool bretVal          = false;
    uint32_t u32baudVal   = 0;
    uint32_t u32fpVal     = 0;
    uint32_t u32confVal   = 0;

    u32baudVal = (clkFrequency / (16 * serialSetup->baud));
    u32fpVal = ((clkFrequency / serialSetup->baud - 16 * u32baudVal) / 2);

    /* Disable the UART before configurations */
    ${SERCOM_INSTANCE_NAME}_REGS->USART.CTRLA &= ~SERCOM_USART_CTRLA_ENABLE_Msk;

    while((${SERCOM_INSTANCE_NAME}_REGS->USART.SYNCBUSY & SERCOM_USART_SYNCBUSY_ENABLE_Msk) == SERCOM_USART_SYNCBUSY_ENABLE_Msk)
    {
        /* Wait for sync */
    }

    if((serialSetup != NULL) && (serialSetup->baud < SERCOM_BAUD_RATE_MAX_RANGE))
    {
        /* Configure Baud Rate */
        ${SERCOM_INSTANCE_NAME}_REGS->USART.BAUD = SERCOM_USART_BAUD_BAUD_FRAC_MODE(u32baudVal) | SERCOM_USART_BAUD_FP(u32fpVal);

        /* Configure Character Size */
        u32confVal |= SERCOM_USART_CTRLB_CHSIZE(serialSetup->charSize);

        /* Configure Stop bits */
        if(serialSetup->stopBits == SERCOM_USART_CTRLB_SBMODE_2BITS)
        {
            u32confVal |= SERCOM_USART_CTRLB_SBMODE_2BITS;
        }
        else
        {
            u32confVal |= SERCOM_USART_CTRLB_SBMODE_1BIT;
        }

        /* Configure Parity Options */
        if((serialSetup->parityEnable == true) && (serialSetup->parity == SERCOM_USART_CTRLB_PMODE_ODD))
        {
            ${SERCOM_INSTANCE_NAME}_REGS->USART.CTRLA |= SERCOM_USART_CTRLA_FORM(1);

            u32confVal |= SERCOM_USART_CTRLB_PMODE_ODD;
        }
        else if((serialSetup->parityEnable == true) && (serialSetup->parity == SERCOM_USART_CTRLB_PMODE_EVEN))
        {
            ${SERCOM_INSTANCE_NAME}_REGS->USART.CTRLA |= SERCOM_USART_CTRLA_FORM(1);

            u32confVal |= SERCOM_USART_CTRLB_PMODE_EVEN;
        }
        else
        {
            /* If No Parity Selected */
            ${SERCOM_INSTANCE_NAME}_REGS->USART.CTRLA |= SERCOM_USART_CTRLA_FORM(0);
        }

        /* Writing the configurations to register */
        ${SERCOM_INSTANCE_NAME}_REGS->USART.CTRLB |= u32confVal;

        while((${SERCOM_INSTANCE_NAME}_REGS->USART.SYNCBUSY & SERCOM_USART_SYNCBUSY_CTRLB_Msk) == SERCOM_USART_SYNCBUSY_CTRLB_Msk)
        {
            /* Wait for sync */
        }

        bretVal = true;
    }

    /* Enable the UART after the configurations */
    ${SERCOM_INSTANCE_NAME}_REGS->USART.CTRLA |= SERCOM_USART_CTRLA_ENABLE_Msk;

    while((${SERCOM_INSTANCE_NAME}_REGS->USART.SYNCBUSY & SERCOM_USART_SYNCBUSY_ENABLE_Msk) == SERCOM_USART_SYNCBUSY_ENABLE_Msk)
    {
        /* Wait for sync */
    }

    return bretVal;
}
</#if>

<#if USART_TX_ENABLE = true>
// *****************************************************************************
/* Function:
    bool ${SERCOM_INSTANCE_NAME}_USART_Write( void *buffer, const size_t size )

  Summary:
    Submits a write buffer to the given USART peripheral to transfer.

  Description
    This function submits a write buffer to the USART peripheral to transfer.
    The behavior of this function call will vary based on the mode
    selected within MHC.

    If the peripheral is configured for the interrupt mode, this function call
    is always non-blocking. Call to this function submits the buffer and the
    size to the peripheral library and returns immediately. User can check the
    transfer status either through callback mechanism or by calling
    USARTx_TransferStatusGet.

    If the peripheral is configured for the non-interrupt mode, this
    function call returns only after requested size is transferred.

  Remarks:
    Refer plib_${SERCOM_INSTANCE_NAME?lower_case}_usart.h file for more information.
*/

bool ${SERCOM_INSTANCE_NAME}_USART_Write( void *buffer, const size_t size )
{
<#if USART_INTERRUPT_MODE = false>
    uint32_t u32Length    = size;
    uint32_t u32TxPos     = 0;
</#if>
    uint8_t *pu8Data     = (uint8_t*)buffer;
    bool bReturnVal      = false;

    if(pu8Data != NULL)
    {
<#if USART_INTERRUPT_MODE = false>
        /* Blocks while buffer is being transferred */
        while (u32Length--)
        {
            while ((${SERCOM_INSTANCE_NAME}_REGS->USART.INTFLAG & SERCOM_USART_INTFLAG_DRE_Msk) != SERCOM_USART_INTFLAG_DRE_Msk)
            {
                /* Check if USART is ready for new data */
            }

            /* Write data to USART module */
            ${SERCOM_INSTANCE_NAME}_REGS->USART.DATA = pu8Data[u32TxPos++];
        }

        bReturnVal = true;
<#else>
        if(${SERCOM_INSTANCE_NAME?lower_case}usartObj.txBusyStatus == false)
        {
            ${SERCOM_INSTANCE_NAME?lower_case}usartObj.txBuffer = pu8Data;
            ${SERCOM_INSTANCE_NAME?lower_case}usartObj.txSize = size;
            ${SERCOM_INSTANCE_NAME?lower_case}usartObj.txProcessedSize = 0;
            ${SERCOM_INSTANCE_NAME?lower_case}usartObj.txBusyStatus = true;

            if(size == 0)
            {
                bReturnVal = true;
            }
            else
            {
                /* Initiate the transfer by sending first byte */
                if((${SERCOM_INSTANCE_NAME}_REGS->USART.INTFLAG & SERCOM_USART_INTFLAG_DRE_Msk) == SERCOM_USART_INTFLAG_DRE_Msk)
                {
                    ${SERCOM_INSTANCE_NAME}_REGS->USART.DATA = ${SERCOM_INSTANCE_NAME?lower_case}usartObj.txBuffer[${SERCOM_INSTANCE_NAME?lower_case}usartObj.txProcessedSize++];
                }

                bReturnVal = true;

                ${SERCOM_INSTANCE_NAME}_REGS->USART.INTENSET = SERCOM_USART_INTFLAG_DRE_Msk ;
            }
        }
</#if>
    }

    return bReturnVal;
}
</#if>

<#if USART_RX_ENABLE = true>
// *****************************************************************************
/* Function:
    bool ${SERCOM_INSTANCE_NAME}_USART_Read( void *buffer, const size_t size )

  Summary:
    Submits a read buffer to the given USART peripheral to process.

  Description:
    This function submits a read buffer to the USART peripheral to process.
    The behavior of this function call will vary based on the mode
    selected within MHC.

    If the peripheral is configured for the interrupt mode, this function call
    is always non-blocking. Call to this function submits the buffer and the
    size to the peripheral library and returns immediately. User can check the
    transfer status either through callback mechanism or by calling
    USARTx_TransferStatusGet.

    If the peripheral is configured for the non-interrupt mode, this
    function call returns only after requested size is processed.

  Remarks:
    Refer plib_${SERCOM_INSTANCE_NAME?lower_case}_usart.h file for more information.
*/

bool ${SERCOM_INSTANCE_NAME}_USART_Read( void *buffer, const size_t size )
{
<#if USART_INTERRUPT_MODE = false>
    uint32_t u32Length    = size;
    uint32_t u32RxPos     = 0;
</#if>
    bool bReturnVal       = false;
    uint8_t *pu8Data      = (uint8_t*)buffer;
    uint8_t u8dummyData   = 0;

    if(pu8Data != NULL)
    {
<#if USART_INTERRUPT_MODE = false>
        /* Checks for error before receiving */
        if(${SERCOM_INSTANCE_NAME}_USART_ErrorGet() != USART_ERROR_NONE)
        {
            /* Clear all error flags */
            ${SERCOM_INSTANCE_NAME}_REGS->USART.INTFLAG = SERCOM_USART_INTFLAG_ERROR_Msk;

            /* Clear error statuses */
            ${SERCOM_INSTANCE_NAME}_REGS->USART.STATUS = SERCOM_USART_STATUS_Msk;

            /* Flush existing error bytes from the RX FIFO */
            while((${SERCOM_INSTANCE_NAME}_REGS->USART.INTFLAG & SERCOM_USART_INTFLAG_RXC_Msk) == SERCOM_USART_INTFLAG_RXC_Msk)
            {
                u8dummyData = ${SERCOM_INSTANCE_NAME}_REGS->USART.DATA;
            }

            /* Ignore the warning */
            (void)u8dummyData;
        }

        while(u32Length--)
        {
            while((${SERCOM_INSTANCE_NAME}_REGS->USART.INTFLAG & SERCOM_USART_INTFLAG_RXC_Msk) != SERCOM_USART_INTFLAG_RXC_Msk)
            {
                /* Check if USART has new data */
            }

            /* Read data from USART module */
            *pu8Data++ = ${SERCOM_INSTANCE_NAME}_REGS->USART.DATA;
            u32RxPos++;

            if(${SERCOM_INSTANCE_NAME}_USART_ErrorGet() != USART_ERROR_NONE)
            {
                break;
            }
            else
            {
                bReturnVal = true;
            }
        }
<#else>
        if(${SERCOM_INSTANCE_NAME?lower_case}usartObj.rxBusyStatus == false)
        {
            /* Checks for error before receiving */
            if(${SERCOM_INSTANCE_NAME}_USART_ErrorGet() != USART_ERROR_NONE)
            {
                /* Clear all error flags */
                ${SERCOM_INSTANCE_NAME}_REGS->USART.INTFLAG = SERCOM_USART_INTFLAG_ERROR_Msk;

                /* Clear error statuses */
                ${SERCOM_INSTANCE_NAME}_REGS->USART.STATUS = SERCOM_USART_STATUS_Msk;

                /* Flush existing error bytes from the RX FIFO */
                while((${SERCOM_INSTANCE_NAME}_REGS->USART.INTFLAG & SERCOM_USART_INTFLAG_RXC_Msk) == SERCOM_USART_INTFLAG_RXC_Msk)
                {
                    u8dummyData = ${SERCOM_INSTANCE_NAME}_REGS->USART.DATA;
                }

                /* Ignore the warning */
                (void)u8dummyData;
            }

            ${SERCOM_INSTANCE_NAME?lower_case}usartObj.rxBuffer = pu8Data;
            ${SERCOM_INSTANCE_NAME?lower_case}usartObj.rxSize = size;
            ${SERCOM_INSTANCE_NAME?lower_case}usartObj.rxProcessedSize = 0;
            ${SERCOM_INSTANCE_NAME?lower_case}usartObj.rxBusyStatus = true;
            bReturnVal = true;

            /* Enable error interrupts */
            ${SERCOM_INSTANCE_NAME}_REGS->USART.INTENSET |= SERCOM_USART_INTENSET_ERROR_Msk;

            /* Enable Receive Complete interrupt */
            ${SERCOM_INSTANCE_NAME}_REGS->USART.INTENSET = SERCOM_USART_INTENSET_RXC_Msk;
        }
</#if>
    }

    return bReturnVal;
}
</#if>

<#if USART_INTERRUPT_MODE = true>
<#if USART_TX_ENABLE = true>
// *****************************************************************************
/* Function:
    bool ${SERCOM_INSTANCE_NAME}_USART_WriteIsBusy( void )

  Summary:
    Returns the write request status associated with the given USART peripheral
    instance.

  Description:
    This function returns the write request status associated with the given
    USART peripheral instance.

    This function is available only in interrupt or non-blocking mode of
    operation.

  Remarks:
    Refer plib_${SERCOM_INSTANCE_NAME?lower_case}_usart.h file for more information.
*/

bool ${SERCOM_INSTANCE_NAME}_USART_WriteIsBusy ( void )
{
    return ${SERCOM_INSTANCE_NAME?lower_case}usartObj.txBusyStatus;
}
</#if>

<#if USART_RX_ENABLE = true>
// *****************************************************************************
/* Function:
    bool ${SERCOM_INSTANCE_NAME}_USART_ReadIsBusy( void )

  Summary:
    Returns the read request status associated with the given USART peripheral
    instance.

  Description:
    This function returns the read request status associated with the given
    USART peripheral instance.

    This function is available only in interrupt or non-blocking mode of
    operation.

  Remarks:
    Refer plib_${SERCOM_INSTANCE_NAME?lower_case}_usart.h file for more information.
*/

bool ${SERCOM_INSTANCE_NAME}_USART_ReadIsBusy ( void )
{
    return ${SERCOM_INSTANCE_NAME?lower_case}usartObj.rxBusyStatus;
}
</#if>
</#if>

<#if USART_INTERRUPT_MODE = true>
<#if USART_TX_ENABLE = true>
// *****************************************************************************
/* Function:
    size_t ${SERCOM_INSTANCE_NAME}_USART_WriteCountGet( void )

  Summary:
    Gets the count of number of bytes processed for a given USART write
    operation.

  Description:
    This function gets the count of number of bytes processed for a given
    USART write operation.

    This function is available only in interrupt or non-blocking mode of
    operation.

  Remarks:
    Refer plib_${SERCOM_INSTANCE_NAME?lower_case}_usart.h file for more information.
*/

size_t ${SERCOM_INSTANCE_NAME}_USART_WriteCountGet( void )
{
    return ${SERCOM_INSTANCE_NAME?lower_case}usartObj.txProcessedSize;
}
</#if>

<#if USART_RX_ENABLE = true>
// *****************************************************************************
/* Function:
    size_t ${SERCOM_INSTANCE_NAME}_USART_ReadCountGet( void )

  Summary:
    Gets the count of number of bytes processed for a given USART read
    operation.

  Description:
    This function gets the count of number of bytes processed for a given
    USART read operation.

    This function is available only in interrupt or non-blocking mode of
    operation.

  Remarks:
    Refer plib_${SERCOM_INSTANCE_NAME?lower_case}_usart.h file for more information.
*/

size_t ${SERCOM_INSTANCE_NAME}_USART_ReadCountGet( void )
{
    return ${SERCOM_INSTANCE_NAME?lower_case}usartObj.rxProcessedSize;
}
</#if>
</#if>

<#if USART_INTERRUPT_MODE = false>
<#if USART_TX_ENABLE = true>
// *****************************************************************************
/* Function:
    bool ${SERCOM_INSTANCE_NAME}_USART_TransmitterIsReady( void )

  Summary:
    Returns the hardware status of the USART Transmitter.

  Description:
    This function returns the hardware status associated with the Transmit
    hardware FIFO of the given USART peripheral instance.

    When Transmitter is ready, user can submit data to transmit.

    This function is available only in non-interrupt mode of operation. And can
    be used to achieve non-blocking behavior of write request. User has to check
    the Transmit ready status by calling this function and can submit write
    request for the buffer size of 1.

  Remarks:
   Refer plib_${SERCOM_INSTANCE_NAME?lower_case}_usart.h file for more information.
*/

bool ${SERCOM_INSTANCE_NAME}_USART_TransmitterIsReady ( void )
{
    bool bstatus = false;

    if((${SERCOM_INSTANCE_NAME}_REGS->USART.INTFLAG & SERCOM_USART_INTFLAG_DRE_Msk) == SERCOM_USART_INTFLAG_DRE_Msk)
    {
        bstatus = true;
    }

    return bstatus;
}
</#if>
<#if USART_RX_ENABLE = true>
// *****************************************************************************
/* Function:
    bool ${SERCOM_INSTANCE_NAME}_USART_ReceiverIsReady( void )

  Summary:
    Returns the hardware status of the USART Receiver.

  Description:
    This function returns the hardware status associated with the Receive
    hardware FIFO of the given USART peripheral instance.

    When Receiver is ready, user can read the available data.

    This function is available only in non-interrupt mode of operation. And can
    be used to achieve non-blocking behavior of read request. User has to check
    the Receiver ready status by calling this function and can submit a read
    request for the buffer size of 1.

  Remarks:
    Refer plib_${SERCOM_INSTANCE_NAME?lower_case}_usart.h file for more information.
*/

bool ${SERCOM_INSTANCE_NAME}_USART_ReceiverIsReady ( void )
{
    bool bstatus = false;

    if((${SERCOM_INSTANCE_NAME}_REGS->USART.INTFLAG & SERCOM_USART_INTFLAG_RXC_Msk) == SERCOM_USART_INTFLAG_RXC_Msk)
    {
        bstatus = true;
    }

    return bstatus;
}
</#if>
</#if>

// *****************************************************************************
/* Function:
    USART_ERROR ${SERCOM_INSTANCE_NAME}_USART_ErrorGet( void )

  Summary:
    Gets the error of the given USART peripheral instance.

  Description:
    This function returns the errors associated with the given USART peripheral
    instance. The call to this function also clears all the associated errors.

  Remarks:
    Refer plib_${SERCOM_INSTANCE_NAME?lower_case}_usart.h file for more information.
*/

USART_ERROR ${SERCOM_INSTANCE_NAME}_USART_ErrorGet( void )
{
    uint32_t u32status = 0;

    u32status = ${SERCOM_INSTANCE_NAME}_REGS->USART.STATUS & (SERCOM_USART_STATUS_PERR_Msk | SERCOM_USART_STATUS_FERR_Msk | SERCOM_USART_STATUS_BUFOVF_Msk);

    /* Clear Errors */
    ${SERCOM_INSTANCE_NAME}_REGS->USART.STATUS = SERCOM_USART_STATUS_PERR_Msk | SERCOM_USART_STATUS_FERR_Msk | SERCOM_USART_STATUS_BUFOVF_Msk;

    return (USART_ERROR) u32status;
}

<#if USART_INTERRUPT_MODE = true>
// *****************************************************************************
// *****************************************************************************
// Section: Callback Interface
// *****************************************************************************
// *****************************************************************************

<#if USART_TX_ENABLE = true>
// *****************************************************************************
/* Function:
    void ${SERCOM_INSTANCE_NAME}_USART_WriteCallbackRegister
                          ( SERCOM_USART_CALLBACK callback, uintptr_t context )

  Summary:
    Sets the pointer to the function (and it's context) to be called when the
    given USART's write events occur.

  Description:
    This function sets the pointer to a client function to be called "back"
    when the given USART's write events occur. It also passes a context value
    (usually a pointer to a context structure) that is passed into the
    function when it is called.

    This function is available only in interrupt or non-blocking mode of
    operation.

  Remarks:
    Refer plib_${SERCOM_INSTANCE_NAME?lower_case}_usart.h file for more information.
*/

void ${SERCOM_INSTANCE_NAME}_USART_WriteCallbackRegister( SERCOM_USART_CALLBACK callback, uintptr_t context )
{
    ${SERCOM_INSTANCE_NAME?lower_case}usartObj.txCallback = callback;

    ${SERCOM_INSTANCE_NAME?lower_case}usartObj.txContext = context;
}
</#if>
<#if USART_TX_ENABLE = true>
// *****************************************************************************
/* Function:
    void ${SERCOM_INSTANCE_NAME}_USART_ReadCallbackRegister
                          ( SERCOM_USART_CALLBACK callback, uintptr_t context )

  Summary:
    Sets the pointer to the function (and it's context) to be called when the
    given USART's read events occur.

  Description:
    This function sets the pointer to a client function to be called "back"
    when the given USART's read events occur. It also passes a context value
    (usually a pointer to a context structure) that is passed into the
    function when it is called.

    This function is available only in interrupt or non-blocking mode of
    operation.

  Remarks:
    Refer plib_${SERCOM_INSTANCE_NAME?lower_case}_usart.h file for more information.
*/

void ${SERCOM_INSTANCE_NAME}_USART_ReadCallbackRegister( SERCOM_USART_CALLBACK callback, uintptr_t context )
{
    ${SERCOM_INSTANCE_NAME?lower_case}usartObj.rxCallback = callback;

    ${SERCOM_INSTANCE_NAME?lower_case}usartObj.rxContext = context;
}
</#if>
</#if>

<#if USART_INTERRUPT_MODE = true>
// *****************************************************************************
/* Function:
    void ${SERCOM_INSTANCE_NAME}_USART_InterruptHandler( void )

  Summary:
    Sercom Handler, handles all sercom interrupt.

  Description:
    This function handles all the operations post interrupt for
    all sercom USART interrupts.

  Remarks:
    Refer plib_${SERCOM_INSTANCE_NAME?lower_case}_usart.h file for more information.
*/

void ${SERCOM_INSTANCE_NAME}_USART_InterruptHandler( void )
{
    /* Checks for data register empty flag */
    if((${SERCOM_INSTANCE_NAME}_REGS->USART.INTFLAG & SERCOM_USART_INTFLAG_DRE_Msk) == SERCOM_USART_INTFLAG_DRE_Msk)
    {
        ${SERCOM_INSTANCE_NAME}_USART_ISR_TX_Handler();
    }

    /* Checks for receive complete empty flag */
    if((${SERCOM_INSTANCE_NAME}_REGS->USART.INTFLAG & SERCOM_USART_INTFLAG_RXC_Msk) == SERCOM_USART_INTFLAG_RXC_Msk)
    {
        ${SERCOM_INSTANCE_NAME}_USART_ISR_RX_Handler();
    }

    /* Checks for error flag */
    if((${SERCOM_INSTANCE_NAME}_REGS->USART.INTFLAG & SERCOM_USART_INTFLAG_ERROR_Msk) == SERCOM_USART_INTFLAG_ERROR_Msk)
    {
        ${SERCOM_INSTANCE_NAME}_USART_ISR_ERR_Handler();
    }
}
</#if>
