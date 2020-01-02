/*******************************************************************************
  Serial Communication Interface Inter-Integrated Circuit (SERCOM I2C) Library
  Source File

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${SERCOM_INSTANCE_NAME?lower_case}_i2c_slave.c

  Summary:
    SERCOM I2C PLIB Slave Implementation file

  Description:
    This file defines the interface to the SERCOM I2C Slave peripheral library.
    This library provides access to and control of the associated peripheral
    instance.

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
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

#include "plib_${SERCOM_INSTANCE_NAME?lower_case}_i2c_slave.h"

// *****************************************************************************
// *****************************************************************************
// Section: Global Data
// *****************************************************************************
// *****************************************************************************
<#if I2CS_INTERRUPT_MODE = true>
static SERCOM_I2C_SLAVE_OBJ ${SERCOM_INSTANCE_NAME?lower_case}I2CSObj;
</#if>
// *****************************************************************************
// *****************************************************************************
// Section: ${SERCOM_INSTANCE_NAME} I2C Implementation
// *****************************************************************************
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Function:
    void ${SERCOM_INSTANCE_NAME}_I2C_Initialize(void)

  Summary:
    Initializes the instance of the SERCOM peripheral operating in I2C mode.

  Description:
    This function initializes the given instance of the SERCOM I2C peripheral as
    configured by the user from the MHC.

  Remarks:
    Refer plib_${SERCOM_INSTANCE_NAME}_i2c.h for more information.
*/

void ${SERCOM_INSTANCE_NAME}_I2C_Initialize(void)
{
    /* Reset the module */
    ${SERCOM_INSTANCE_NAME}_REGS->I2CS.SERCOM_CTRLA = SERCOM_I2CS_CTRLA_SWRST_Msk ;

    /* Wait for synchronization */
    <#if SERCOM_SYNCBUSY = false>
    while((${SERCOM_INSTANCE_NAME}_REGS->I2CS.SERCOM_STATUS & SERCOM_I2CS_STATUS_SYNCBUSY_Msk) & SERCOM_I2CS_STATUS_SYNCBUSY_Msk);
    <#else>
    while(${SERCOM_INSTANCE_NAME}_REGS->I2CS.SERCOM_SYNCBUSY);
    </#if>

     /* Set Operation Mode to I2C Slave */
    <@compress single_line=true>${SERCOM_INSTANCE_NAME}_REGS->I2CS.SERCOM_CTRLA = SERCOM_I2CS_CTRLA_MODE_I2C_SLAVE |
                                                                                  SERCOM_I2CS_CTRLA_SDAHOLD_${I2CS_SDAHOLD_TIME}
                                                                                  ${I2CS_RUNSTDBY?then(' | SERCOM_I2CS_CTRLA_RUNSTDBY_Msk', '')}
                                                                                  <#if I2CS_LOWTOUT_SUPPORT??>${I2CS_LOWTOUT_SUPPORT?then(' | SERCOM_I2CS_CTRLA_LOWTOUTEN_Msk', '')}</#if>
                                                                                  <#if I2CS_SEXTTOEN_SUPPORT??>${I2CS_SEXTTOEN_SUPPORT?then(' | SERCOM_I2CS_CTRLA_SEXTTOEN_Msk', '')}</#if>;
                                                                                  </@compress>

    /* Wait for synchronization */
    <#if SERCOM_SYNCBUSY = false>
    while((${SERCOM_INSTANCE_NAME}_REGS->I2CS.SERCOM_STATUS & SERCOM_I2CS_STATUS_SYNCBUSY_Msk) & SERCOM_I2CS_STATUS_SYNCBUSY_Msk);
    <#else>
    while(${SERCOM_INSTANCE_NAME}_REGS->I2CS.SERCOM_SYNCBUSY);
    </#if>

    /* Set the slave address */
    ${SERCOM_INSTANCE_NAME}_REGS->I2CS.SERCOM_ADDR = SERCOM_I2CS_ADDR_ADDR(0x${I2CS_SLAVE_ADDDRESS}) <#if I2CS_TENBITEN_SUPPORT??>${I2CS_TENBITEN_SUPPORT?then(' | SERCOM_I2CS_ADDR_TENBITEN_Msk', '')}</#if>;

    <#if I2CS_SMEN == true>
    /* Enable Smart Mode */
    ${SERCOM_INSTANCE_NAME}_REGS->I2CS.SERCOM_CTRLB |= SERCOM_I2CM_CTRLB_SMEN_Msk;

    /* Wait for synchronization */
    <#if SERCOM_SYNCBUSY = false>
    while((${SERCOM_INSTANCE_NAME}_REGS->I2CS.SERCOM_STATUS & SERCOM_I2CS_STATUS_SYNCBUSY_Msk) & SERCOM_I2CS_STATUS_SYNCBUSY_Msk);
    <#else>
    while(${SERCOM_INSTANCE_NAME}_REGS->I2CS.SERCOM_SYNCBUSY);
    </#if>
    </#if>

    <#if I2CS_INTERRUPT_MODE = true>
    /* Enable all I2C slave Interrupts */
    ${SERCOM_INSTANCE_NAME}_REGS->I2CS.SERCOM_INTENSET = SERCOM_I2CS_INTENSET_Msk;
    </#if>

    /* Enable peripheral */
    ${SERCOM_INSTANCE_NAME}_REGS->I2CS.SERCOM_CTRLA |= SERCOM_I2CS_CTRLA_ENABLE_Msk ;

    /* Wait for synchronization */
    <#if SERCOM_SYNCBUSY = false>
    while((${SERCOM_INSTANCE_NAME}_REGS->I2CS.SERCOM_STATUS & SERCOM_I2CS_STATUS_SYNCBUSY_Msk) & SERCOM_I2CS_STATUS_SYNCBUSY_Msk);
    <#else>
    while(${SERCOM_INSTANCE_NAME}_REGS->I2CS.SERCOM_SYNCBUSY);
    </#if>
}

<#if I2CS_INTERRUPT_MODE = true>
void ${SERCOM_INSTANCE_NAME}_I2C_CallbackRegister(SERCOM_I2C_SLAVE_CALLBACK callback, uintptr_t contextHandle)
{
    ${SERCOM_INSTANCE_NAME?lower_case}I2CSObj.callback = callback;

    ${SERCOM_INSTANCE_NAME?lower_case}I2CSObj.context  = contextHandle;
}

bool ${SERCOM_INSTANCE_NAME}_I2C_IsBusy(void)
{
    return ${SERCOM_INSTANCE_NAME?lower_case}I2CSObj.isBusy;
}

<#else>
SERCOM_I2C_SLAVE_INTFLAG ${SERCOM_INSTANCE_NAME}_I2C_InterruptFlagsGet(void)
{
    return (SERCOM_I2C_SLAVE_INTFLAG)${SERCOM_INSTANCE_NAME}_REGS->I2CS.SERCOM_INTFLAG;
}

void ${SERCOM_INSTANCE_NAME}_I2C_InterruptFlagsClear(SERCOM_I2C_SLAVE_INTFLAG intFlags)
{
    ${SERCOM_INSTANCE_NAME}_REGS->I2CS.SERCOM_INTFLAG = intFlags;
}
</#if>

uint8_t ${SERCOM_INSTANCE_NAME}_I2C_ReadByte(void)
{
    /* Wait for synchronization */
    <#if SERCOM_SYNCBUSY = false>
    while((${SERCOM_INSTANCE_NAME}_REGS->I2CS.SERCOM_STATUS & SERCOM_I2CS_STATUS_SYNCBUSY_Msk) & SERCOM_I2CS_STATUS_SYNCBUSY_Msk);
    <#else>
    while(${SERCOM_INSTANCE_NAME}_REGS->I2CS.SERCOM_SYNCBUSY);
    </#if>

    return ${SERCOM_INSTANCE_NAME}_REGS->I2CS.SERCOM_DATA;
}

void ${SERCOM_INSTANCE_NAME}_I2C_WriteByte(uint8_t wrByte)
{
    ${SERCOM_INSTANCE_NAME}_REGS->I2CS.SERCOM_DATA = wrByte;

    /* Wait for synchronization */
    <#if SERCOM_SYNCBUSY = false>
    while((${SERCOM_INSTANCE_NAME}_REGS->I2CS.SERCOM_STATUS & SERCOM_I2CS_STATUS_SYNCBUSY_Msk) & SERCOM_I2CS_STATUS_SYNCBUSY_Msk);
    <#else>
    while(${SERCOM_INSTANCE_NAME}_REGS->I2CS.SERCOM_SYNCBUSY);
    </#if>
}

SERCOM_I2C_SLAVE_ERROR ${SERCOM_INSTANCE_NAME}_I2C_ErrorGet(void)
{
    return (${SERCOM_INSTANCE_NAME}_REGS->I2CS.SERCOM_STATUS & SERCOM_I2C_SLAVE_ERROR_ALL);
}

SERCOM_I2C_SLAVE_TRANSFER_DIR ${SERCOM_INSTANCE_NAME}_I2C_TransferDirGet(void)
{
    return (${SERCOM_INSTANCE_NAME}_REGS->I2CS.SERCOM_STATUS & SERCOM_I2CS_STATUS_DIR_Msk)? SERCOM_I2C_SLAVE_TRANSFER_DIR_READ: SERCOM_I2C_SLAVE_TRANSFER_DIR_WRITE;
}

SERCOM_I2C_SLAVE_ACK_STATUS ${SERCOM_INSTANCE_NAME}_I2C_LastByteAckStatusGet(void)
{
    return (${SERCOM_INSTANCE_NAME}_REGS->I2CS.SERCOM_STATUS & SERCOM_I2CS_STATUS_RXNACK_Msk)? SERCOM_I2C_SLAVE_ACK_STATUS_RECEIVED_NAK : SERCOM_I2C_SLAVE_ACK_STATUS_RECEIVED_ACK;
}

<#if I2CS_SMEN == true>
void ${SERCOM_INSTANCE_NAME}_I2C_AckActionSet(SERCOM_I2C_SLAVE_ACK_ACTION_SEND ackAction)
{
    if (ackAction == SERCOM_I2C_SLAVE_ACK_ACTION_SEND_ACK)
    {
        ${SERCOM_INSTANCE_NAME}_REGS->I2CS.SERCOM_CTRLB &= ~SERCOM_I2CS_CTRLB_ACKACT_Msk;
    }
    else
    {
        ${SERCOM_INSTANCE_NAME}_REGS->I2CS.SERCOM_CTRLB |= SERCOM_I2CS_CTRLB_ACKACT_Msk;
    }
}
<#else>
void ${SERCOM_INSTANCE_NAME}_I2C_CommandSet(SERCOM_I2C_SLAVE_COMMAND command)
{
    if (command == SERCOM_I2C_SLAVE_COMMAND_SEND_ACK)
    {
        ${SERCOM_INSTANCE_NAME}_REGS->I2CS.SERCOM_CTRLB = (${SERCOM_INSTANCE_NAME}_REGS->I2CS.SERCOM_CTRLB | SERCOM_I2CS_CTRLB_CMD(0x03)) & (~SERCOM_I2CS_CTRLB_ACKACT_Msk);
    }
    else if (command == SERCOM_I2C_SLAVE_COMMAND_SEND_NAK)
    {
        ${SERCOM_INSTANCE_NAME}_REGS->I2CS.SERCOM_CTRLB |= (SERCOM_I2CS_CTRLB_CMD(0x03) | (SERCOM_I2CS_CTRLB_ACKACT_Msk));
    }
    else if (command == SERCOM_I2C_SLAVE_COMMAND_RECEIVE_ACK_NAK)
    {
        ${SERCOM_INSTANCE_NAME}_REGS->I2CS.SERCOM_CTRLB = (${SERCOM_INSTANCE_NAME}_REGS->I2CS.SERCOM_CTRLB | SERCOM_I2CS_CTRLB_CMD(0x03));
    }
    else if (command == SERCOM_I2C_SLAVE_COMMAND_WAIT_FOR_START)
    {
        ${SERCOM_INSTANCE_NAME}_REGS->I2CS.SERCOM_CTRLB = (${SERCOM_INSTANCE_NAME}_REGS->I2CS.SERCOM_CTRLB & ~SERCOM_I2CS_CTRLB_CMD_Msk) | SERCOM_I2CS_CTRLB_CMD(0x02);
    }
    else
    {
        /* Do nothing, return */
    }
}
</#if>

<#if I2CS_INTERRUPT_MODE = true>
<#if I2CS_SMEN == true>
void ${SERCOM_INSTANCE_NAME}_I2C_InterruptHandler(void)
{
    uint32_t intFlags = ${SERCOM_INSTANCE_NAME}_REGS->I2CS.SERCOM_INTFLAG;
    SERCOM_I2C_SLAVE_TRANSFER_EVENT event;

    if(intFlags & ${SERCOM_INSTANCE_NAME}_REGS->I2CS.SERCOM_INTENSET)
    {
        if (intFlags & SERCOM_I2CS_INTFLAG_AMATCH_Msk)
        {
            ${SERCOM_INSTANCE_NAME?lower_case}I2CSObj.isBusy = true;

            ${SERCOM_INSTANCE_NAME?lower_case}I2CSObj.isFirstRxAfterAddressPending = true;

            ${SERCOM_INSTANCE_NAME?lower_case}I2CSObj.isRepeatedStart = ${SERCOM_INSTANCE_NAME}_REGS->I2CS.SERCOM_STATUS & SERCOM_I2CS_STATUS_SR_Msk ? true : false;

            event = SERCOM_I2C_SLAVE_TRANSFER_EVENT_ADDR_MATCH;
        }
        if (intFlags & SERCOM_I2CS_INTFLAG_DRDY_Msk)
        {
            if (${SERCOM_INSTANCE_NAME}_I2C_TransferDirGet() == SERCOM_I2C_SLAVE_TRANSFER_DIR_WRITE)
            {
                event = SERCOM_I2C_SLAVE_TRANSFER_EVENT_RX_READY;
            }
            else
            {
                if ((${SERCOM_INSTANCE_NAME?lower_case}I2CSObj.isFirstRxAfterAddressPending == true) || (${SERCOM_INSTANCE_NAME}_I2C_LastByteAckStatusGet() == SERCOM_I2C_SLAVE_ACK_STATUS_RECEIVED_ACK))
                {
                    ${SERCOM_INSTANCE_NAME?lower_case}I2CSObj.isFirstRxAfterAddressPending = false;
                    event = SERCOM_I2C_SLAVE_TRANSFER_EVENT_TX_READY;
                }
            }
        }
        if (intFlags & SERCOM_I2CS_INTFLAG_PREC_Msk)
        {
            ${SERCOM_INSTANCE_NAME?lower_case}I2CSObj.isBusy = false;
            event = SERCOM_I2C_SLAVE_TRANSFER_EVENT_STOP_BIT_RECEIVED;
        }

        if (${SERCOM_INSTANCE_NAME?lower_case}I2CSObj.callback != NULL)
        {
            ${SERCOM_INSTANCE_NAME?lower_case}I2CSObj.callback(event, ${SERCOM_INSTANCE_NAME?lower_case}I2CSObj.context);
        }
    }
    ${SERCOM_INSTANCE_NAME}_REGS->I2CS.SERCOM_INTFLAG = intFlags;
}
<#else>
void ${SERCOM_INSTANCE_NAME}_I2C_InterruptHandler(void)
{
    uint32_t intFlags = ${SERCOM_INSTANCE_NAME}_REGS->I2CS.SERCOM_INTFLAG;

    if(intFlags & ${SERCOM_INSTANCE_NAME}_REGS->I2CS.SERCOM_INTENSET)
    {
        if (intFlags & SERCOM_I2CS_INTFLAG_AMATCH_Msk)
        {
            ${SERCOM_INSTANCE_NAME?lower_case}I2CSObj.isBusy = true;

            ${SERCOM_INSTANCE_NAME?lower_case}I2CSObj.isFirstRxAfterAddressPending = true;

            ${SERCOM_INSTANCE_NAME?lower_case}I2CSObj.isRepeatedStart = ${SERCOM_INSTANCE_NAME}_REGS->I2CS.SERCOM_STATUS & SERCOM_I2CS_STATUS_SR_Msk ? true : false;

            if (${SERCOM_INSTANCE_NAME?lower_case}I2CSObj.callback != NULL)
            {
                if (${SERCOM_INSTANCE_NAME?lower_case}I2CSObj.callback(SERCOM_I2C_SLAVE_TRANSFER_EVENT_ADDR_MATCH, ${SERCOM_INSTANCE_NAME?lower_case}I2CSObj.context) == true)
                {
                    ${SERCOM_INSTANCE_NAME}_I2C_CommandSet(SERCOM_I2C_SLAVE_COMMAND_SEND_ACK);
                }
                else
                {
                    ${SERCOM_INSTANCE_NAME}_I2C_CommandSet(SERCOM_I2C_SLAVE_COMMAND_SEND_NAK);
                }
            }
        }
        if (intFlags & SERCOM_I2CS_INTFLAG_DRDY_Msk)
        {
            if (${SERCOM_INSTANCE_NAME?lower_case}I2CSObj.callback != NULL)
            {
                if (${SERCOM_INSTANCE_NAME}_I2C_TransferDirGet() == SERCOM_I2C_SLAVE_TRANSFER_DIR_WRITE)
                {
                    if (${SERCOM_INSTANCE_NAME?lower_case}I2CSObj.callback(SERCOM_I2C_SLAVE_TRANSFER_EVENT_RX_READY, ${SERCOM_INSTANCE_NAME?lower_case}I2CSObj.context) == true)
                    {
                        ${SERCOM_INSTANCE_NAME}_I2C_CommandSet(SERCOM_I2C_SLAVE_COMMAND_SEND_ACK);
                    }
                    else
                    {
                        ${SERCOM_INSTANCE_NAME}_I2C_CommandSet(SERCOM_I2C_SLAVE_COMMAND_SEND_NAK);
                    }
                }
                else
                {
                    if ((${SERCOM_INSTANCE_NAME?lower_case}I2CSObj.isFirstRxAfterAddressPending == true) || (${SERCOM_INSTANCE_NAME}_I2C_LastByteAckStatusGet() == SERCOM_I2C_SLAVE_ACK_STATUS_RECEIVED_ACK))
                    {
                        ${SERCOM_INSTANCE_NAME?lower_case}I2CSObj.callback(SERCOM_I2C_SLAVE_TRANSFER_EVENT_TX_READY, ${SERCOM_INSTANCE_NAME?lower_case}I2CSObj.context);
                        ${SERCOM_INSTANCE_NAME?lower_case}I2CSObj.isFirstRxAfterAddressPending = false;
                        ${SERCOM_INSTANCE_NAME}_I2C_CommandSet(SERCOM_I2C_SLAVE_COMMAND_RECEIVE_ACK_NAK);
                    }
                    else
                    {
                        ${SERCOM_INSTANCE_NAME}_I2C_CommandSet(SERCOM_I2C_SLAVE_COMMAND_WAIT_FOR_START);
                    }
                }
            }
        }
        if (intFlags & SERCOM_I2CS_INTFLAG_PREC_Msk)
        {
            ${SERCOM_INSTANCE_NAME?lower_case}I2CSObj.isBusy = false;

            if (${SERCOM_INSTANCE_NAME?lower_case}I2CSObj.callback != NULL)
            {
                ${SERCOM_INSTANCE_NAME?lower_case}I2CSObj.callback(SERCOM_I2C_SLAVE_TRANSFER_EVENT_STOP_BIT_RECEIVED, ${SERCOM_INSTANCE_NAME?lower_case}I2CSObj.context);
            }

            ${SERCOM_INSTANCE_NAME}_REGS->I2CS.SERCOM_INTFLAG = SERCOM_I2CS_INTFLAG_PREC_Msk;
        }
        <#if I2CS_INTENSET_ERROR = true>
        if (intFlags & SERCOM_I2CS_INTFLAG_ERROR_Msk)
        {
            if (${SERCOM_INSTANCE_NAME?lower_case}I2CSObj.callback != NULL)
            {
                ${SERCOM_INSTANCE_NAME?lower_case}I2CSObj.callback(SERCOM_I2C_SLAVE_TRANSFER_EVENT_ERROR, ${SERCOM_INSTANCE_NAME?lower_case}I2CSObj.context);
            }
        }
        </#if>
    }
}
</#if>
</#if>
