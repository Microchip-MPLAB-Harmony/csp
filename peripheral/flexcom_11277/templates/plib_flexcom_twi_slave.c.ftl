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
<#if core.CoreSysIntFile == true>
#include "interrupts.h"
</#if>

// *****************************************************************************
// *****************************************************************************
// Global Data
// *****************************************************************************
// *****************************************************************************

static FLEXCOM_TWI_SLAVE_OBJ ${FLEXCOM_INSTANCE_NAME?lower_case}TwiObj;
static twi_registers_t *${FLEXCOM_INSTANCE_NAME}_TWI_Module = TWI${FLEXCOM_INSTANCE_NUMBER}_REGS;

// *****************************************************************************
// *****************************************************************************
// ${FLEXCOM_INSTANCE_NAME} TWI PLib Interface Routines
// *****************************************************************************
// *****************************************************************************

void ${FLEXCOM_INSTANCE_NAME}_TWI_Initialize(void)
{
    /* Set FLEXCOM TWI operating mode */
    ${FLEXCOM_INSTANCE_NAME}_REGS->FLEXCOM_MR = FLEXCOM_MR_OPMODE_TWI;

    // Reset the i2c Module
    ${FLEXCOM_INSTANCE_NAME}_TWI_Module->TWI_CR = TWI_CR_SWRST_Msk;

    // Disable the I2C Master/Slave Mode
    ${FLEXCOM_INSTANCE_NAME}_TWI_Module->TWI_CR = TWI_CR_MSDIS_Msk | TWI_CR_SVDIS_Msk;

    /* Configure slave address */
    ${FLEXCOM_INSTANCE_NAME}_TWI_Module->TWI_SMR = TWI_SMR_SADR(0x${FLEXCOM_TWI_SLAVE_ADDRESS});

    /* Clear the Transmit Holding Register and set TXRDY, TXCOMP flags */
    ${FLEXCOM_INSTANCE_NAME}_TWI_Module->TWI_CR = TWI_CR_THRCLR_Msk;

<#if TWI_INTERRUPT_MODE == true>
    /* Enable interrupt for Slave Access and End of Slave Access */
    ${FLEXCOM_INSTANCE_NAME}_TWI_Module->TWI_IER = TWI_IER_SVACC_Msk | TWI_IER_EOSACC_Msk;

    /* Initialize the TWI PLIB Object */
    ${FLEXCOM_INSTANCE_NAME?lower_case}TwiObj.callback = NULL;
    ${FLEXCOM_INSTANCE_NAME?lower_case}TwiObj.isBusy = false;
    ${FLEXCOM_INSTANCE_NAME?lower_case}TwiObj.isAddrMatchEventNotified = false;
    ${FLEXCOM_INSTANCE_NAME?lower_case}TwiObj.isFirstTxPending = false;
</#if>

    /* Enable Slave Mode */
    ${FLEXCOM_INSTANCE_NAME}_TWI_Module->TWI_CR = TWI_CR_SVEN_Msk;
}

uint8_t ${FLEXCOM_INSTANCE_NAME}_TWI_ReadByte(void)
{
    return (uint8_t)(${FLEXCOM_INSTANCE_NAME}_TWI_Module->TWI_RHR & TWI_RHR_RXDATA_Msk);
}

void ${FLEXCOM_INSTANCE_NAME}_TWI_WriteByte(uint8_t wrByte)
{
    ${FLEXCOM_INSTANCE_NAME}_TWI_Module->TWI_THR = TWI_THR_TXDATA(wrByte);
}

FLEXCOM_TWI_SLAVE_TRANSFER_DIR ${FLEXCOM_INSTANCE_NAME}_TWI_TransferDirGet(void)
{
    return (${FLEXCOM_INSTANCE_NAME}_TWI_Module->TWI_SR & TWI_SR_SVREAD_Msk)? FLEXCOM_TWI_SLAVE_TRANSFER_DIR_READ: FLEXCOM_TWI_SLAVE_TRANSFER_DIR_WRITE;
}

FLEXCOM_TWI_SLAVE_ACK_STATUS ${FLEXCOM_INSTANCE_NAME}_TWI_LastByteAckStatusGet(void)
{
    return (${FLEXCOM_INSTANCE_NAME}_TWI_Module->TWI_SR & TWI_SR_NACK_Msk)? FLEXCOM_TWI_SLAVE_ACK_STATUS_RECEIVED_NAK : FLEXCOM_TWI_SLAVE_ACK_STATUS_RECEIVED_ACK;
}

void ${FLEXCOM_INSTANCE_NAME}_TWI_NACKDataPhase(bool isNACKEnable)
{
    if (isNACKEnable == true)
    {
        ${FLEXCOM_INSTANCE_NAME}_TWI_Module->TWI_SMR = (${FLEXCOM_INSTANCE_NAME}_TWI_Module->TWI_SMR & ~TWI_SMR_NACKEN_Msk) | TWI_SMR_NACKEN_Msk;
    }
    else
    {
        ${FLEXCOM_INSTANCE_NAME}_TWI_Module->TWI_SMR = (${FLEXCOM_INSTANCE_NAME}_TWI_Module->TWI_SMR & ~TWI_SMR_NACKEN_Msk);
    }
}

<#if TWI_INTERRUPT_MODE == true>

void ${FLEXCOM_INSTANCE_NAME}_TWI_CallbackRegister(FLEXCOM_TWI_SLAVE_CALLBACK callback, uintptr_t contextHandle)
{
    ${FLEXCOM_INSTANCE_NAME?lower_case}TwiObj.callback = callback;

    ${FLEXCOM_INSTANCE_NAME?lower_case}TwiObj.context  = contextHandle;
}

bool ${FLEXCOM_INSTANCE_NAME}_TWI_IsBusy(void)
{
    return ${FLEXCOM_INSTANCE_NAME?lower_case}TwiObj.isBusy;
}

void ${FLEXCOM_INSTANCE_NAME}_InterruptHandler( void )
{
    uint32_t status = ${FLEXCOM_INSTANCE_NAME}_TWI_Module->TWI_SR;

    if (status & ${FLEXCOM_INSTANCE_NAME}_TWI_Module->TWI_IMR)
    {
        if(status & TWI_SR_SVACC_Msk)
        {
            if (${FLEXCOM_INSTANCE_NAME?lower_case}TwiObj.isAddrMatchEventNotified == false)
            {
                ${FLEXCOM_INSTANCE_NAME}_TWI_Module->TWI_IDR = TWI_IDR_SVACC_Msk;

                if (${FLEXCOM_INSTANCE_NAME}_TWI_TransferDirGet() == FLEXCOM_TWI_SLAVE_TRANSFER_DIR_READ)
                {
                    ${FLEXCOM_INSTANCE_NAME}_TWI_Module->TWI_IER = TWI_IER_TXRDY_Msk | TWI_IER_TXCOMP_Msk;

                    /* Set flag so that we do not check for NAK from master before transmitting the first byte */
                    ${FLEXCOM_INSTANCE_NAME?lower_case}TwiObj.isFirstTxPending = true;
                }
                else
                {
                    ${FLEXCOM_INSTANCE_NAME}_TWI_Module->TWI_IER = TWI_IER_RXRDY_Msk | TWI_IER_TXCOMP_Msk;
                }

                ${FLEXCOM_INSTANCE_NAME?lower_case}TwiObj.isBusy = true;

                if (${FLEXCOM_INSTANCE_NAME?lower_case}TwiObj.callback != NULL)
                {
                    ${FLEXCOM_INSTANCE_NAME?lower_case}TwiObj.callback(FLEXCOM_TWI_SLAVE_TRANSFER_EVENT_ADDR_MATCH, ${FLEXCOM_INSTANCE_NAME?lower_case}TwiObj.context);
                }

                ${FLEXCOM_INSTANCE_NAME?lower_case}TwiObj.isAddrMatchEventNotified = true;
            }

            /* I2C Master reads from slave */
            if (${FLEXCOM_INSTANCE_NAME}_TWI_TransferDirGet() == FLEXCOM_TWI_SLAVE_TRANSFER_DIR_READ)
            {
                if (status & TWI_SR_TXRDY_Msk)
                {
                    if ((${FLEXCOM_INSTANCE_NAME?lower_case}TwiObj.isFirstTxPending == true) || (!(status & TWI_SR_NACK_Msk)))
                    {
                        if (${FLEXCOM_INSTANCE_NAME?lower_case}TwiObj.callback != NULL)
                        {
                            ${FLEXCOM_INSTANCE_NAME?lower_case}TwiObj.callback(FLEXCOM_TWI_SLAVE_TRANSFER_EVENT_TX_READY, ${FLEXCOM_INSTANCE_NAME?lower_case}TwiObj.context);
                        }
                        ${FLEXCOM_INSTANCE_NAME?lower_case}TwiObj.isFirstTxPending = false;
                    }
                    else
                    {
                        /* NAK received. Turn off TXRDY interrupt. */
                        ${FLEXCOM_INSTANCE_NAME}_TWI_Module->TWI_IDR = TWI_IDR_TXRDY_Msk;
                    }
                }
            }
            else
            {
                /* I2C Master writes to slave */
                if (status & TWI_SR_RXRDY_Msk)
                {
                    if (${FLEXCOM_INSTANCE_NAME?lower_case}TwiObj.callback != NULL)
                    {
                        ${FLEXCOM_INSTANCE_NAME?lower_case}TwiObj.callback(FLEXCOM_TWI_SLAVE_TRANSFER_EVENT_RX_READY, ${FLEXCOM_INSTANCE_NAME?lower_case}TwiObj.context);
                    }
                }
            }
        }
        else if (status & TWI_SR_EOSACC_Msk)
        {
            /* Either Repeated Start or Stop condition received */

            ${FLEXCOM_INSTANCE_NAME?lower_case}TwiObj.isAddrMatchEventNotified = false;

            ${FLEXCOM_INSTANCE_NAME}_TWI_Module->TWI_IDR = TWI_IDR_TXRDY_Msk | TWI_IDR_RXRDY_Msk;
            ${FLEXCOM_INSTANCE_NAME}_TWI_Module->TWI_IER = TWI_IER_SVACC_Msk;

            if (status & TWI_SR_TXCOMP_Msk)
            {
                /* Stop condition received OR start condition with other slave address detected */

                ${FLEXCOM_INSTANCE_NAME?lower_case}TwiObj.isBusy = true;

                if (${FLEXCOM_INSTANCE_NAME?lower_case}TwiObj.callback != NULL)
                {
                    ${FLEXCOM_INSTANCE_NAME?lower_case}TwiObj.callback(FLEXCOM_TWI_SLAVE_TRANSFER_EVENT_TRANSMISSION_COMPLETE, ${FLEXCOM_INSTANCE_NAME?lower_case}TwiObj.context);
                }

                ${FLEXCOM_INSTANCE_NAME}_TWI_Module->TWI_IDR = TWI_IDR_TXCOMP_Msk;
            }
        }
    }
}
<#else>
FLEXCOM_TWI_SLAVE_STATUS_FLAG ${FLEXCOM_INSTANCE_NAME}_TWI_StatusGet(void)
{
    return (${FLEXCOM_INSTANCE_NAME}_TWI_Module->TWI_SR & (TWI_SR_SVACC_Msk | TWI_SR_EOSACC_Msk | TWI_SR_SVREAD_Msk | TWI_SR_TXRDY_Msk | TWI_SR_RXRDY_Msk | TWI_SR_NACK_Msk | TWI_SR_TXCOMP_Msk));
}
</#if>