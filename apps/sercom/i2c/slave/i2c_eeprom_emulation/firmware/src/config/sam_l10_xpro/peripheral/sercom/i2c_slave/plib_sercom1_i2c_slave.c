/*******************************************************************************
  Serial Communication Interface Inter-Integrated Circuit (SERCOM I2C) Library
  Source File

  Company:
    Microchip Technology Inc.

  File Name:
    plib_sercom1_i2c_slave.c

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

#include "plib_sercom1_i2c_slave.h"

// *****************************************************************************
// *****************************************************************************
// Section: Global Data
// *****************************************************************************
// *****************************************************************************
static SERCOM_I2C_SLAVE_OBJ sercom1I2CSObj;
// *****************************************************************************
// *****************************************************************************
// Section: SERCOM1 I2C Implementation
// *****************************************************************************
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Function:
    void SERCOM1_I2C_Initialize(void)

  Summary:
    Initializes the instance of the SERCOM peripheral operating in I2C mode.

  Description:
    This function initializes the given instance of the SERCOM I2C peripheral as
    configured by the user from the MHC.

  Remarks:
    Refer plib_SERCOM1_i2c.h for more information.
*/

void SERCOM1_I2C_Initialize(void)
{
    /* Reset the module */
    SERCOM1_REGS->I2CS.SERCOM_CTRLA = SERCOM_I2CS_CTRLA_SWRST_Msk ;

    /* Wait for synchronization */
    while(SERCOM1_REGS->I2CS.SERCOM_SYNCBUSY);

     /* Set Operation Mode to I2C Slave */
    SERCOM1_REGS->I2CS.SERCOM_CTRLA = SERCOM_I2CS_CTRLA_MODE_I2C_SLAVE | SERCOM_I2CS_CTRLA_SDAHOLD_75NS ;
    /* Wait for synchronization */
    while(SERCOM1_REGS->I2CS.SERCOM_SYNCBUSY);

    /* Set the slave address */
    SERCOM1_REGS->I2CS.SERCOM_ADDR = SERCOM_I2CS_ADDR_ADDR(0x54) ;


    /* Enable all I2C slave Interrupts */
    SERCOM1_REGS->I2CS.SERCOM_INTENSET = SERCOM_I2CS_INTENSET_Msk;

    /* Enable peripheral */
    SERCOM1_REGS->I2CS.SERCOM_CTRLA |= SERCOM_I2CS_CTRLA_ENABLE_Msk ;

    /* Wait for synchronization */
    while(SERCOM1_REGS->I2CS.SERCOM_SYNCBUSY);
}

void SERCOM1_I2C_CallbackRegister(SERCOM_I2C_SLAVE_CALLBACK callback, uintptr_t contextHandle)
{
    sercom1I2CSObj.callback = callback;

    sercom1I2CSObj.context  = contextHandle;
}

bool SERCOM1_I2C_IsBusy(void)
{
    return sercom1I2CSObj.isBusy;
}


uint8_t SERCOM1_I2C_ReadByte(void)
{
    /* Wait for synchronization */
    while(SERCOM1_REGS->I2CS.SERCOM_SYNCBUSY);

    return SERCOM1_REGS->I2CS.SERCOM_DATA;
}

void SERCOM1_I2C_WriteByte(uint8_t wrByte)
{
    SERCOM1_REGS->I2CS.SERCOM_DATA = wrByte;

    /* Wait for synchronization */
    while(SERCOM1_REGS->I2CS.SERCOM_SYNCBUSY);
}

SERCOM_I2C_SLAVE_ERROR SERCOM1_I2C_ErrorGet(void)
{
    return (SERCOM1_REGS->I2CS.SERCOM_STATUS & SERCOM_I2C_SLAVE_ERROR_ALL);
}

SERCOM_I2C_SLAVE_TRANSFER_DIR SERCOM1_I2C_TransferDirGet(void)
{
    return (SERCOM1_REGS->I2CS.SERCOM_STATUS & SERCOM_I2CS_STATUS_DIR_Msk)? SERCOM_I2C_SLAVE_TRANSFER_DIR_READ: SERCOM_I2C_SLAVE_TRANSFER_DIR_WRITE;
}

SERCOM_I2C_SLAVE_ACK_STATUS SERCOM1_I2C_LastByteAckStatusGet(void)
{
    return (SERCOM1_REGS->I2CS.SERCOM_STATUS & SERCOM_I2CS_STATUS_RXNACK_Msk)? SERCOM_I2C_SLAVE_ACK_STATUS_RECEIVED_NAK : SERCOM_I2C_SLAVE_ACK_STATUS_RECEIVED_ACK;
}

void SERCOM1_I2C_CommandSet(SERCOM_I2C_SLAVE_COMMAND command)
{
    if (command == SERCOM_I2C_SLAVE_COMMAND_SEND_ACK)
    {
        SERCOM1_REGS->I2CS.SERCOM_CTRLB = (SERCOM1_REGS->I2CS.SERCOM_CTRLB | SERCOM_I2CS_CTRLB_CMD(0x03)) & (~SERCOM_I2CS_CTRLB_ACKACT_Msk);
    }
    else if (command == SERCOM_I2C_SLAVE_COMMAND_SEND_NAK)
    {
        SERCOM1_REGS->I2CS.SERCOM_CTRLB |= (SERCOM_I2CS_CTRLB_CMD(0x03) | (SERCOM_I2CS_CTRLB_ACKACT_Msk));
    }
    else if (command == SERCOM_I2C_SLAVE_COMMAND_RECEIVE_ACK_NAK)
    {
        SERCOM1_REGS->I2CS.SERCOM_CTRLB = (SERCOM1_REGS->I2CS.SERCOM_CTRLB | SERCOM_I2CS_CTRLB_CMD(0x03));
    }
    else if (command == SERCOM_I2C_SLAVE_COMMAND_WAIT_FOR_START)
    {
        SERCOM1_REGS->I2CS.SERCOM_CTRLB = (SERCOM1_REGS->I2CS.SERCOM_CTRLB & ~SERCOM_I2CS_CTRLB_CMD_Msk) | SERCOM_I2CS_CTRLB_CMD(0x02);
    }
    else
    {
        /* Do nothing, return */
    }
}

void SERCOM1_I2C_InterruptHandler(void)
{
    uint32_t intFlags = SERCOM1_REGS->I2CS.SERCOM_INTFLAG;

    if(intFlags & SERCOM1_REGS->I2CS.SERCOM_INTENSET)
    {
        if (intFlags & SERCOM_I2CS_INTFLAG_AMATCH_Msk)
        {
            sercom1I2CSObj.isBusy = true;

            sercom1I2CSObj.isFirstRxAfterAddressPending = true;

            sercom1I2CSObj.isRepeatedStart = SERCOM1_REGS->I2CS.SERCOM_STATUS & SERCOM_I2CS_STATUS_SR_Msk ? true : false;

            if (sercom1I2CSObj.callback != NULL)
            {
                if (sercom1I2CSObj.callback(SERCOM_I2C_SLAVE_TRANSFER_EVENT_ADDR_MATCH, sercom1I2CSObj.context) == true)
                {
                    SERCOM1_I2C_CommandSet(SERCOM_I2C_SLAVE_COMMAND_SEND_ACK);
                }
                else
                {
                    SERCOM1_I2C_CommandSet(SERCOM_I2C_SLAVE_COMMAND_SEND_NAK);
                }
            }
        }
        if (intFlags & SERCOM_I2CS_INTFLAG_DRDY_Msk)
        {
            if (sercom1I2CSObj.callback != NULL)
            {
                if (SERCOM1_I2C_TransferDirGet() == SERCOM_I2C_SLAVE_TRANSFER_DIR_WRITE)
                {
                    if (sercom1I2CSObj.callback(SERCOM_I2C_SLAVE_TRANSFER_EVENT_RX_READY, sercom1I2CSObj.context) == true)
                    {
                        SERCOM1_I2C_CommandSet(SERCOM_I2C_SLAVE_COMMAND_SEND_ACK);
                    }
                    else
                    {
                        SERCOM1_I2C_CommandSet(SERCOM_I2C_SLAVE_COMMAND_SEND_NAK);
                    }
                }
                else
                {
                    if ((sercom1I2CSObj.isFirstRxAfterAddressPending == true) || (SERCOM1_I2C_LastByteAckStatusGet() == SERCOM_I2C_SLAVE_ACK_STATUS_RECEIVED_ACK))
                    {
                        sercom1I2CSObj.callback(SERCOM_I2C_SLAVE_TRANSFER_EVENT_TX_READY, sercom1I2CSObj.context);
                        sercom1I2CSObj.isFirstRxAfterAddressPending = false;
                        SERCOM1_I2C_CommandSet(SERCOM_I2C_SLAVE_COMMAND_RECEIVE_ACK_NAK);
                    }
                    else
                    {
                        SERCOM1_I2C_CommandSet(SERCOM_I2C_SLAVE_COMMAND_WAIT_FOR_START);
                    }
                }
            }
        }
        if (intFlags & SERCOM_I2CS_INTFLAG_PREC_Msk)
        {
            sercom1I2CSObj.isBusy = false;

            if (sercom1I2CSObj.callback != NULL)
            {
                sercom1I2CSObj.callback(SERCOM_I2C_SLAVE_TRANSFER_EVENT_STOP_BIT_RECEIVED, sercom1I2CSObj.context);
            }

            SERCOM1_REGS->I2CS.SERCOM_INTFLAG = SERCOM_I2CS_INTFLAG_PREC_Msk;
        }
        if (intFlags & SERCOM_I2CS_INTFLAG_ERROR_Msk)
        {
            if (sercom1I2CSObj.callback != NULL)
            {
                sercom1I2CSObj.callback(SERCOM_I2C_SLAVE_TRANSFER_EVENT_ERROR, sercom1I2CSObj.context);
            }
        }
    }
}
