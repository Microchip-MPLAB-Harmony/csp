/*******************************************************************************
  FLEXCOM TWI Peripheral Library Source File

  Company
    Microchip Technology Inc.

  File Name
    plib_${FLEXCOM_INSTANCE_NAME?lower_case}_twi_slave.c

  Summary
    FLEXCOM TWI Slave peripheral library interface.

  Description
    This file defines the interface to the FLEXCOM TWI peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

  Remarks:

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

// *****************************************************************************
// *****************************************************************************
// Included Files
// *****************************************************************************
// *****************************************************************************

#include "device.h"
#include "plib_${FLEXCOM_INSTANCE_NAME?lower_case}_twi_slave.h"

// *****************************************************************************
// *****************************************************************************
// Global Data
// *****************************************************************************
// *****************************************************************************

static FLEXCOM_TWI_SLAVE_OBJ ${FLEXCOM_INSTANCE_NAME?lower_case}TWIObj;
static flexcom_registers_t *${FLEXCOM_INSTANCE_NAME}_TWI_Module = ${FLEXCOM_INSTANCE_NAME}_REGS;

// *****************************************************************************
// *****************************************************************************
// ${FLEXCOM_INSTANCE_NAME} TWI PLib Interface Routines
// *****************************************************************************
// *****************************************************************************

void ${FLEXCOM_INSTANCE_NAME}_TWI_Initialize(void)
{
    /* Set FLEXCOM TWI operating mode */
    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEX_MR = FLEX_MR_OPMODE_TWI;

    // Reset the i2c Module
    ${FLEXCOM_INSTANCE_NAME}_TWI_Module->FLEX_TWI_CR = FLEX_TWI_CR_SWRST_Msk;

    // Disable the I2C Master/Slave Mode
    ${FLEXCOM_INSTANCE_NAME}_TWI_Module->FLEX_TWI_CR = FLEX_TWI_CR_MSDIS_Msk | FLEX_TWI_CR_SVDIS_Msk;

    /* Configure slave address */
    ${FLEXCOM_INSTANCE_NAME}_TWI_Module->FLEX_TWI_SMR = FLEX_TWI_SMR_SADR(0x${FLEXCOM_TWI_SLAVE_ADDRESS});

    /* Clear the Transmit Holding Register and set TXRDY, TXCOMP flags */
    ${FLEXCOM_INSTANCE_NAME}_TWI_Module->FLEX_TWI_CR = FLEX_TWI_CR_THRCLR_Msk;

<#if TWI_INTERRUPT_MODE == true>
    /* Enable interrupt for Slave Access and End of Slave Access */
    ${FLEXCOM_INSTANCE_NAME}_TWI_Module->FLEX_TWI_IER = FLEX_TWI_IER_SVACC_Msk | FLEX_TWI_IER_EOSACC_Msk;

    /* Initialize the TWI PLIB Object */
    ${FLEXCOM_INSTANCE_NAME?lower_case}TWIObj.callback = NULL;
    ${FLEXCOM_INSTANCE_NAME?lower_case}TWIObj.isBusy = false;
    ${FLEXCOM_INSTANCE_NAME?lower_case}TWIObj.isAddrMatchEventNotified = false;
    ${FLEXCOM_INSTANCE_NAME?lower_case}TWIObj.isFirstTxPending = false;
</#if>

    /* Enable Slave Mode */
    ${FLEXCOM_INSTANCE_NAME}_TWI_Module->FLEX_TWI_CR = FLEX_TWI_CR_SVEN_Msk;
}

uint8_t ${FLEXCOM_INSTANCE_NAME}_TWI_ReadByte(void)
{
    return (uint8_t)(${FLEXCOM_INSTANCE_NAME}_TWI_Module->FLEX_TWI_RHR & FLEX_TWI_RHR_RXDATA_Msk);
}

void ${FLEXCOM_INSTANCE_NAME}_TWI_WriteByte(uint8_t wrByte)
{
    ${FLEXCOM_INSTANCE_NAME}_TWI_Module->FLEX_TWI_THR = FLEX_TWI_THR_TXDATA(wrByte);
}

FLEXCOM_TWI_SLAVE_TRANSFER_DIR ${FLEXCOM_INSTANCE_NAME}_TWI_TransferDirGet(void)
{
    return (${FLEXCOM_INSTANCE_NAME}_TWI_Module->FLEX_TWI_SR & FLEX_TWI_SR_SVREAD_Msk)? FLEXCOM_TWI_SLAVE_TRANSFER_DIR_READ: FLEXCOM_TWI_SLAVE_TRANSFER_DIR_WRITE;
}

FLEXCOM_TWI_SLAVE_ACK_STATUS ${FLEXCOM_INSTANCE_NAME}_TWI_LastByteAckStatusGet(void)
{
    return (${FLEXCOM_INSTANCE_NAME}_TWI_Module->FLEX_TWI_SR & FLEX_TWI_SR_NACK_Msk)? FLEXCOM_TWI_SLAVE_ACK_STATUS_RECEIVED_NAK : FLEXCOM_TWI_SLAVE_ACK_STATUS_RECEIVED_ACK;
}

void ${FLEXCOM_INSTANCE_NAME}_TWI_NACKDataPhase(bool isNACKEnable)
{
    if (isNACKEnable == true)
    {
        ${FLEXCOM_INSTANCE_NAME}_TWI_Module->FLEX_TWI_SMR = (${FLEXCOM_INSTANCE_NAME}_TWI_Module->FLEX_TWI_SMR & ~FLEX_TWI_SMR_NACKEN_Msk) | FLEX_TWI_SMR_NACKEN_Msk;
    }
    else
    {
        ${FLEXCOM_INSTANCE_NAME}_TWI_Module->FLEX_TWI_SMR = (${FLEXCOM_INSTANCE_NAME}_TWI_Module->FLEX_TWI_SMR & ~FLEX_TWI_SMR_NACKEN_Msk);
    }
}

<#if TWI_INTERRUPT_MODE == true>

void ${FLEXCOM_INSTANCE_NAME}_TWI_CallbackRegister(FLEXCOM_TWI_SLAVE_CALLBACK callback, uintptr_t contextHandle)
{
    ${FLEXCOM_INSTANCE_NAME?lower_case}TWIObj.callback = callback;

    ${FLEXCOM_INSTANCE_NAME?lower_case}TWIObj.context  = contextHandle;
}

bool ${FLEXCOM_INSTANCE_NAME}_TWI_IsBusy(void)
{
    return ${FLEXCOM_INSTANCE_NAME?lower_case}TWIObj.isBusy;
}

void ${FLEXCOM_INSTANCE_NAME}_InterruptHandler( void )
{
    uint32_t status = ${FLEXCOM_INSTANCE_NAME}_TWI_Module->FLEX_TWI_SR;

    if (status & ${FLEXCOM_INSTANCE_NAME}_TWI_Module->FLEX_TWI_IMR)
    {
        if(status & FLEX_TWI_SR_SVACC_Msk)
        {
            if (${FLEXCOM_INSTANCE_NAME?lower_case}TWIObj.isAddrMatchEventNotified == false)
            {
                ${FLEXCOM_INSTANCE_NAME}_TWI_Module->FLEX_TWI_IDR = FLEX_TWI_IDR_SVACC_Msk;

                if (${FLEXCOM_INSTANCE_NAME}_TWI_TransferDirGet() == FLEXCOM_TWI_SLAVE_TRANSFER_DIR_READ)
                {
                    ${FLEXCOM_INSTANCE_NAME}_TWI_Module->FLEX_TWI_IER = FLEX_TWI_IER_TXRDY_Msk | FLEX_TWI_IER_TXCOMP_Msk;

                    /* Set flag so that we do not check for NAK from master before transmitting the first byte */
                    ${FLEXCOM_INSTANCE_NAME?lower_case}TWIObj.isFirstTxPending = true;
                }
                else
                {
                    ${FLEXCOM_INSTANCE_NAME}_TWI_Module->FLEX_TWI_IER = FLEX_TWI_IER_RXRDY_Msk | FLEX_TWI_IER_TXCOMP_Msk;
                }

                ${FLEXCOM_INSTANCE_NAME?lower_case}TWIObj.isBusy = true;

                if (${FLEXCOM_INSTANCE_NAME?lower_case}TWIObj.callback != NULL)
                {
                    ${FLEXCOM_INSTANCE_NAME?lower_case}TWIObj.callback(FLEXCOM_TWI_SLAVE_TRANSFER_EVENT_ADDR_MATCH, ${FLEXCOM_INSTANCE_NAME?lower_case}TWIObj.context);
                }

                ${FLEXCOM_INSTANCE_NAME?lower_case}TWIObj.isAddrMatchEventNotified = true;
            }

            /* I2C Master reads from slave */
            if (${FLEXCOM_INSTANCE_NAME}_TWI_TransferDirGet() == FLEXCOM_TWI_SLAVE_TRANSFER_DIR_READ)
            {
                if (status & FLEX_TWI_SR_TXRDY_Msk)
                {
                    if ((${FLEXCOM_INSTANCE_NAME?lower_case}TWIObj.isFirstTxPending == true) || (!(status & FLEX_TWI_SR_NACK_Msk)))
                    {
                        if (${FLEXCOM_INSTANCE_NAME?lower_case}TWIObj.callback != NULL)
                        {
                            ${FLEXCOM_INSTANCE_NAME?lower_case}TWIObj.callback(FLEXCOM_TWI_SLAVE_TRANSFER_EVENT_TX_READY, ${FLEXCOM_INSTANCE_NAME?lower_case}TWIObj.context);
                        }
                        ${FLEXCOM_INSTANCE_NAME?lower_case}TWIObj.isFirstTxPending = false;
                    }
                    else
                    {
                        /* NAK received. Turn off TXRDY interrupt. */
                        ${FLEXCOM_INSTANCE_NAME}_TWI_Module->FLEX_TWI_IDR = FLEX_TWI_IDR_TXRDY_Msk;
                    }
                }
            }
            else
            {
                /* I2C Master writes to slave */
                if (status & FLEX_TWI_SR_RXRDY_Msk)
                {
                    if (${FLEXCOM_INSTANCE_NAME?lower_case}TWIObj.callback != NULL)
                    {
                        ${FLEXCOM_INSTANCE_NAME?lower_case}TWIObj.callback(FLEXCOM_TWI_SLAVE_TRANSFER_EVENT_RX_READY, ${FLEXCOM_INSTANCE_NAME?lower_case}TWIObj.context);
                    }
                }
            }
        }
        else if (status & FLEX_TWI_SR_EOSACC_Msk)
        {
            /* Either Repeated Start or Stop condition received */

            ${FLEXCOM_INSTANCE_NAME?lower_case}TWIObj.isAddrMatchEventNotified = false;

            ${FLEXCOM_INSTANCE_NAME}_TWI_Module->FLEX_TWI_IDR = FLEX_TWI_IDR_TXRDY_Msk | FLEX_TWI_IDR_RXRDY_Msk;
            ${FLEXCOM_INSTANCE_NAME}_TWI_Module->FLEX_TWI_IER = FLEX_TWI_IER_SVACC_Msk;

            if (status & FLEX_TWI_SR_TXCOMP_Msk)
            {
                /* Stop condition received OR start condition with other slave address detected */

                ${FLEXCOM_INSTANCE_NAME?lower_case}TWIObj.isBusy = true;

                if (${FLEXCOM_INSTANCE_NAME?lower_case}TWIObj.callback != NULL)
                {
                    ${FLEXCOM_INSTANCE_NAME?lower_case}TWIObj.callback(FLEXCOM_TWI_SLAVE_TRANSFER_EVENT_TRANSMISSION_COMPLETE, ${FLEXCOM_INSTANCE_NAME?lower_case}TWIObj.context);
                }

                ${FLEXCOM_INSTANCE_NAME}_TWI_Module->FLEX_TWI_IDR = FLEX_TWI_IDR_TXCOMP_Msk;
            }
        }
    }
}
<#else>
FLEXCOM_TWI_SLAVE_STATUS_FLAG ${FLEXCOM_INSTANCE_NAME}_TWI_StatusGet(void)
{
    return (${FLEXCOM_INSTANCE_NAME}_TWI_Module->FLEX_TWI_SR & (FLEX_TWI_SR_SVACC_Msk | FLEX_TWI_SR_EOSACC_Msk | FLEX_TWI_SR_SVREAD_Msk | FLEX_TWI_SR_TXRDY_Msk | FLEX_TWI_SR_RXRDY_Msk | FLEX_TWI_SR_NACK_Msk | FLEX_TWI_SR_TXCOMP_Msk));
}
</#if>