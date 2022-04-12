/*******************************************************************************
  TWIHS Peripheral Library Source File

  Company
    Microchip Technology Inc.

  File Name
    plib_${TWIHS_INSTANCE_NAME?lower_case}_slave.c

  Summary
    TWIHS Slave peripheral library interface.

  Description

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
#include "plib_${TWIHS_INSTANCE_NAME?lower_case}_slave.h"

// *****************************************************************************
// *****************************************************************************
// Global Data
// *****************************************************************************
// *****************************************************************************

<#if TWIHS_INTERRUPT_MODE = true>
static TWIHS_SLAVE_OBJ ${TWIHS_INSTANCE_NAME?lower_case}Obj;
</#if>

// *****************************************************************************
// *****************************************************************************
// ${TWIHS_INSTANCE_NAME} PLib Interface Routines
// *****************************************************************************
// *****************************************************************************

void ${TWIHS_INSTANCE_NAME}_Initialize( void )
{
    /* Reset the TWIHS Module */
    ${TWIHS_INSTANCE_NAME}_REGS->TWIHS_CR = TWIHS_CR_SWRST_Msk;

    /* Disable the TWIHS Master/Slave Mode */
    ${TWIHS_INSTANCE_NAME}_REGS->TWIHS_CR = TWIHS_CR_MSDIS_Msk | TWIHS_CR_SVDIS_Msk;

    /* Configure slave address */
    ${TWIHS_INSTANCE_NAME}_REGS->TWIHS_SMR = TWIHS_SMR_SADR(0x${TWIHS_SLAVE_ADDRESS});

<#if TWIHS_CR_THRCLR>
    /* Clear the Transmit Holding Register and set TXRDY, TXCOMP flags */
    ${TWIHS_INSTANCE_NAME}_REGS->TWIHS_CR = TWIHS_CR_THRCLR_Msk;
</#if>

    /* Initialize the TWIHS PLIB Object */
<#if TWIHS_INTERRUPT_MODE = true>
    /* Enable interrupt for Slave Access and End of Slave Access */
    ${TWIHS_INSTANCE_NAME}_REGS->TWIHS_IER = TWIHS_IER_SVACC_Msk | TWIHS_IER_EOSACC_Msk;

    ${TWIHS_INSTANCE_NAME?lower_case}Obj.callback = NULL;
    ${TWIHS_INSTANCE_NAME?lower_case}Obj.isBusy = false;
    ${TWIHS_INSTANCE_NAME?lower_case}Obj.isFirstTxPending = false;
    ${TWIHS_INSTANCE_NAME?lower_case}Obj.isAddrMatchEventNotified = false;
</#if>

    /* Enable Slave Mode */
    ${TWIHS_INSTANCE_NAME}_REGS->TWIHS_CR = TWIHS_CR_SVEN_Msk;
}

uint8_t ${TWIHS_INSTANCE_NAME}_ReadByte(void)
{
    return (uint8_t)(${TWIHS_INSTANCE_NAME}_REGS->TWIHS_RHR & TWIHS_RHR_RXDATA_Msk);
}

void ${TWIHS_INSTANCE_NAME}_WriteByte(uint8_t wrByte)
{
    ${TWIHS_INSTANCE_NAME}_REGS->TWIHS_THR = TWIHS_THR_TXDATA(wrByte);
}

TWIHS_SLAVE_TRANSFER_DIR ${TWIHS_INSTANCE_NAME}_TransferDirGet(void)
{
    return ((${TWIHS_INSTANCE_NAME}_REGS->TWIHS_SR & TWIHS_SR_SVREAD_Msk) != 0U)? TWIHS_SLAVE_TRANSFER_DIR_READ: TWIHS_SLAVE_TRANSFER_DIR_WRITE;
}

TWIHS_SLAVE_ACK_STATUS ${TWIHS_INSTANCE_NAME}_LastByteAckStatusGet(void)
{
    return ((${TWIHS_INSTANCE_NAME}_REGS->TWIHS_SR & TWIHS_SR_NACK_Msk) != 0U)? TWIHS_SLAVE_ACK_STATUS_RECEIVED_NAK : TWIHS_SLAVE_ACK_STATUS_RECEIVED_ACK;
}

<#if TWIHS_SMR_NACKEN == true>
void ${TWIHS_INSTANCE_NAME}_NACKDataPhase(bool isNACKEnable)
{
    if (isNACKEnable == true)
    {
        ${TWIHS_INSTANCE_NAME}_REGS->TWIHS_SMR = (${TWIHS_INSTANCE_NAME}_REGS->TWIHS_SMR & ~TWIHS_SMR_NACKEN_Msk) | TWIHS_SMR_NACKEN_Msk;
    }
    else
    {
        ${TWIHS_INSTANCE_NAME}_REGS->TWIHS_SMR = (${TWIHS_INSTANCE_NAME}_REGS->TWIHS_SMR & ~TWIHS_SMR_NACKEN_Msk);
    }
}
</#if>

<#if TWIHS_INTERRUPT_MODE = true>

void ${TWIHS_INSTANCE_NAME}_CallbackRegister(TWIHS_SLAVE_CALLBACK callback, uintptr_t contextHandle)
{
    ${TWIHS_INSTANCE_NAME?lower_case}Obj.callback = callback;

    ${TWIHS_INSTANCE_NAME?lower_case}Obj.context  = contextHandle;
}

bool ${TWIHS_INSTANCE_NAME}_IsBusy(void)
{
    return ${TWIHS_INSTANCE_NAME?lower_case}Obj.isBusy;
}

void ${TWIHS_INSTANCE_NAME}_InterruptHandler( void )
{
    uint32_t status = ${TWIHS_INSTANCE_NAME}_REGS->TWIHS_SR;

    if ((status & ${TWIHS_INSTANCE_NAME}_REGS->TWIHS_IMR) != 0U)
    {
        if((status & TWIHS_SR_SVACC_Msk) != 0U)
        {
            if (${TWIHS_INSTANCE_NAME?lower_case}Obj.isAddrMatchEventNotified == false)
            {
                ${TWIHS_INSTANCE_NAME}_REGS->TWIHS_IDR = TWIHS_IDR_SVACC_Msk;

                if (${TWIHS_INSTANCE_NAME}_TransferDirGet() == TWIHS_SLAVE_TRANSFER_DIR_READ)
                {
                    ${TWIHS_INSTANCE_NAME}_REGS->TWIHS_IER = TWIHS_IER_TXRDY_Msk | TWIHS_IER_TXCOMP_Msk;

                    /* Set flag so that we do not check for NAK from master before transmitting the first byte */
                    ${TWIHS_INSTANCE_NAME?lower_case}Obj.isFirstTxPending = true;
                }
                else
                {
                    ${TWIHS_INSTANCE_NAME}_REGS->TWIHS_IER = TWIHS_IER_RXRDY_Msk | TWIHS_IER_TXCOMP_Msk;
                }

                ${TWIHS_INSTANCE_NAME?lower_case}Obj.isBusy = true;

                if (${TWIHS_INSTANCE_NAME?lower_case}Obj.callback != NULL)
                {
                    (void) ${TWIHS_INSTANCE_NAME?lower_case}Obj.callback(TWIHS_SLAVE_TRANSFER_EVENT_ADDR_MATCH, ${TWIHS_INSTANCE_NAME?lower_case}Obj.context);
                }

                ${TWIHS_INSTANCE_NAME?lower_case}Obj.isAddrMatchEventNotified = true;
            }

            /* I2C Master reads from slave */
            if (${TWIHS_INSTANCE_NAME}_TransferDirGet() == TWIHS_SLAVE_TRANSFER_DIR_READ)
            {
                if ((status & TWIHS_SR_TXRDY_Msk) != 0U)
                {
                    if ((${TWIHS_INSTANCE_NAME?lower_case}Obj.isFirstTxPending == true) || ((status & TWIHS_SR_NACK_Msk) == 0U))
                    {
                        if (${TWIHS_INSTANCE_NAME?lower_case}Obj.callback != NULL)
                        {
                            (void) ${TWIHS_INSTANCE_NAME?lower_case}Obj.callback(TWIHS_SLAVE_TRANSFER_EVENT_TX_READY, ${TWIHS_INSTANCE_NAME?lower_case}Obj.context);
                        }
                        ${TWIHS_INSTANCE_NAME?lower_case}Obj.isFirstTxPending = false;
                    }
                    else
                    {
                        /* NAK received. Turn off TXRDY interrupt. */
                        ${TWIHS_INSTANCE_NAME}_REGS->TWIHS_IDR = TWIHS_IDR_TXRDY_Msk;
                    }
                }
            }
            else
            {
                /* I2C Master writes to slave */
                if ((status & TWIHS_SR_RXRDY_Msk) != 0U)
                {
                    if (${TWIHS_INSTANCE_NAME?lower_case}Obj.callback != NULL)
                    {
                        (void) ${TWIHS_INSTANCE_NAME?lower_case}Obj.callback(TWIHS_SLAVE_TRANSFER_EVENT_RX_READY, ${TWIHS_INSTANCE_NAME?lower_case}Obj.context);
                    }
                }
            }
        }
        else if ((status & TWIHS_SR_EOSACC_Msk) != 0U)
        { 
            /* Either Repeated Start or Stop condition received */

            ${TWIHS_INSTANCE_NAME?lower_case}Obj.isAddrMatchEventNotified = false;

            ${TWIHS_INSTANCE_NAME}_REGS->TWIHS_IDR = TWIHS_IDR_TXRDY_Msk | TWIHS_IDR_RXRDY_Msk;
            ${TWIHS_INSTANCE_NAME}_REGS->TWIHS_IER = TWIHS_IER_SVACC_Msk;

            if ((status & TWIHS_SR_TXCOMP_Msk) != 0U)
            {
                /* Stop condition received OR start condition with other slave address detected */

                ${TWIHS_INSTANCE_NAME?lower_case}Obj.isBusy = true;

                if (${TWIHS_INSTANCE_NAME?lower_case}Obj.callback != NULL)
                {
                    (void) ${TWIHS_INSTANCE_NAME?lower_case}Obj.callback(TWIHS_SLAVE_TRANSFER_EVENT_TRANSMISSION_COMPLETE, ${TWIHS_INSTANCE_NAME?lower_case}Obj.context);
                }

                ${TWIHS_INSTANCE_NAME}_REGS->TWIHS_IDR = TWIHS_IDR_TXCOMP_Msk;
            }
        }
		else
		{
			/* Do Nothing*/
		}
    }
}
<#else>
TWIHS_SLAVE_STATUS_FLAG ${TWIHS_INSTANCE_NAME}_StatusGet(void)
{
    return (${TWIHS_INSTANCE_NAME}_REGS->TWIHS_SR & (TWIHS_SR_SVACC_Msk | TWIHS_SR_EOSACC_Msk | TWIHS_SR_SVREAD_Msk | TWIHS_SR_TXRDY_Msk | TWIHS_SR_RXRDY_Msk | TWIHS_SR_NACK_Msk | TWIHS_SR_TXCOMP_Msk));
}
</#if>