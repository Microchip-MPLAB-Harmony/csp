/*******************************************************************************
  Inter-Integrated Circuit (I2C) Library
  Source File

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${I2C_INSTANCE_NAME?lower_case}.c

  Summary:
    I2C PLIB Implementation file

  Description:
    This file defines the interface to the I2C peripheral library.
    This library provides access to and control of the associated peripheral
    instance.

*******************************************************************************/
// DOM-IGNORE-BEGIN
/*******************************************************************************
* Copyright (C) 2018-2019 Microchip Technology Inc. and its subsidiaries.
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

#include "device.h"
#include "plib_${I2C_INSTANCE_NAME?lower_case}.h"

// *****************************************************************************
// *****************************************************************************
// Section: Global Data
// *****************************************************************************
// *****************************************************************************

static I2C_OBJ ${I2C_INSTANCE_NAME?lower_case}Obj;

void ${I2C_INSTANCE_NAME}_Initialize(void)
{
    /* Disable the I2C Master interrupt */
    ${I2C_MASTER_IEC_REG}CLR = _${I2C_MASTER_IEC_REG}_${I2C_INSTANCE_NAME}MIE_MASK;

    /* Disable the I2C Bus collision interrupt */
    ${I2C_BUS_IEC_REG}CLR = _${I2C_BUS_IEC_REG}_${I2C_INSTANCE_NAME}BIE_MASK;

    ${I2C_INSTANCE_NAME}BRG = ${BRG_VALUE};

<#if I2C_SIDL == true>
    ${I2C_INSTANCE_NAME}CONSET = _${I2C_INSTANCE_NAME}CON_SIDL_MASK;
<#else>
    ${I2C_INSTANCE_NAME}CONCLR = _${I2C_INSTANCE_NAME}CON_SIDL_MASK;
</#if>
<#if I2C_DISSLW == true>
    ${I2C_INSTANCE_NAME}CONSET = _${I2C_INSTANCE_NAME}CON_DISSLW_MASK;
<#else>
    ${I2C_INSTANCE_NAME}CONCLR = _${I2C_INSTANCE_NAME}CON_DISSLW_MASK;
</#if>
<#if I2C_SMEN == true>
    ${I2C_INSTANCE_NAME}CONSET = _${I2C_INSTANCE_NAME}CON_SMEN_MASK;
<#else>
    ${I2C_INSTANCE_NAME}CONCLR = _${I2C_INSTANCE_NAME}CON_SMEN_MASK;
</#if>

    /* Clear master interrupt flag */
    ${I2C_MASTER_IFS_REG}CLR = _${I2C_MASTER_IFS_REG}_${I2C_INSTANCE_NAME}MIF_MASK;

    /* Clear fault interrupt flag */
    ${I2C_BUS_IFS_REG}CLR = _${I2C_BUS_IFS_REG}_${I2C_INSTANCE_NAME}BIF_MASK;

    /* Turn on the I2C module */
    ${I2C_INSTANCE_NAME}CONSET = _${I2C_INSTANCE_NAME}CON_ON_MASK;

    /* Set the initial state of the I2C state machine */
    ${I2C_INSTANCE_NAME?lower_case}Obj.state = I2C_STATE_IDLE;
}

/* I2C state machine */
static void ${I2C_INSTANCE_NAME}_TransferSM(void)
{
    switch (${I2C_INSTANCE_NAME?lower_case}Obj.state)
    {
        case I2C_STATE_START_CONDITION:
            /* Generate Start Condition */
            ${I2C_INSTANCE_NAME}CONSET = _${I2C_INSTANCE_NAME}CON_SEN_MASK;
            ${I2C_MASTER_IEC_REG}SET = _${I2C_MASTER_IEC_REG}_${I2C_INSTANCE_NAME}MIE_MASK;
            ${I2C_BUS_IEC_REG}SET = _${I2C_BUS_IEC_REG}_${I2C_INSTANCE_NAME}BIE_MASK;
            ${I2C_INSTANCE_NAME?lower_case}Obj.state = I2C_STATE_ADDR_BYTE_1_SEND;
            break;
        case I2C_STATE_ADDR_BYTE_1_SEND:
            /* Is transmit buffer full? */
            if (!(${I2C_INSTANCE_NAME}STAT & _${I2C_INSTANCE_NAME}STAT_TBF_MASK))
            {
                if (${I2C_INSTANCE_NAME?lower_case}Obj.address > 0x007F)
                {
                    /* Transmit the first byte of the 10-bit slave address */
                    ${I2C_INSTANCE_NAME}TRN = ( 0xF0 | (((uint8_t*)&${I2C_INSTANCE_NAME?lower_case}Obj.address)[1] << 1) | (${I2C_INSTANCE_NAME?lower_case}Obj.transferType) );

                    if (${I2C_INSTANCE_NAME?lower_case}Obj.transferType == I2C_TRANSFER_TYPE_WRITE)
                    {
                        ${I2C_INSTANCE_NAME?lower_case}Obj.state = I2C_STATE_ADDR_BYTE_2_SEND;
                    }
                    else
                    {
                        ${I2C_INSTANCE_NAME?lower_case}Obj.state = I2C_STATE_READ;
                    }
                }
                else
                {
                    /* 8-bit addressing mode */
                    ${I2C_INSTANCE_NAME}TRN = ((${I2C_INSTANCE_NAME?lower_case}Obj.address << 1) | ${I2C_INSTANCE_NAME?lower_case}Obj.transferType);

                    if (${I2C_INSTANCE_NAME?lower_case}Obj.transferType == I2C_TRANSFER_TYPE_WRITE)
                    {
                        ${I2C_INSTANCE_NAME?lower_case}Obj.state = I2C_STATE_WRITE;
                    }
                    else
                    {
                        ${I2C_INSTANCE_NAME?lower_case}Obj.state = I2C_STATE_READ;
                    }
                }
            }
            break;
        case I2C_STATE_ADDR_BYTE_2_SEND:
            /* Transmit the 2nd byte of the 10-bit slave address */
            if (!(${I2C_INSTANCE_NAME}STAT & _${I2C_INSTANCE_NAME}STAT_ACKSTAT_MASK))
            {
                if (!(${I2C_INSTANCE_NAME}STAT & _${I2C_INSTANCE_NAME}STAT_TBF_MASK))
                {
                    ${I2C_INSTANCE_NAME}TRN = ${I2C_INSTANCE_NAME?lower_case}Obj.address;
                    ${I2C_INSTANCE_NAME?lower_case}Obj.state = I2C_STATE_WRITE;
                }
            }
            else
            {
                /* NAK received. Generate Stop Condition. */
                ${I2C_INSTANCE_NAME?lower_case}Obj.error = I2C_ERROR_NACK;
                ${I2C_INSTANCE_NAME}CONSET = _${I2C_INSTANCE_NAME}CON_PEN_MASK;
                ${I2C_INSTANCE_NAME?lower_case}Obj.state = I2C_STATE_WAIT_STOP_CONDITION_COMPLETE;
            }
            break;
        case I2C_STATE_WRITE:
            if (!(${I2C_INSTANCE_NAME}STAT & _${I2C_INSTANCE_NAME}STAT_ACKSTAT_MASK))
            {
                /* ACK received */
                if (${I2C_INSTANCE_NAME?lower_case}Obj.writeCount < ${I2C_INSTANCE_NAME?lower_case}Obj.writeSize)
                {
                    if (!(${I2C_INSTANCE_NAME}STAT & _${I2C_INSTANCE_NAME}STAT_TBF_MASK))
                    {
                        /* Transmit the data from writeBuffer[] */
                        ${I2C_INSTANCE_NAME}TRN = ${I2C_INSTANCE_NAME?lower_case}Obj.writeBuffer[${I2C_INSTANCE_NAME?lower_case}Obj.writeCount++];
                    }
                }
                else
                {
                    if (${I2C_INSTANCE_NAME?lower_case}Obj.readCount < ${I2C_INSTANCE_NAME?lower_case}Obj.readSize)
                    {
                        /* Generate repeated start condition */
                        ${I2C_INSTANCE_NAME}CONSET = _${I2C_INSTANCE_NAME}CON_RSEN_MASK;
                        ${I2C_INSTANCE_NAME?lower_case}Obj.transferType = I2C_TRANSFER_TYPE_READ;
                        /* Send the I2C slave address with R/W = 1*/
                        ${I2C_INSTANCE_NAME?lower_case}Obj.state = I2C_STATE_ADDR_BYTE_1_SEND;
                    }
                    else
                    {
                        /* Transfer Complete. Generate Stop Condition */
                        ${I2C_INSTANCE_NAME}CONSET = _${I2C_INSTANCE_NAME}CON_PEN_MASK;
                        ${I2C_INSTANCE_NAME?lower_case}Obj.state = I2C_STATE_WAIT_STOP_CONDITION_COMPLETE;
                    }
                }
            }
            else
            {
                /* NAK received. Generate Stop Condition. */
                ${I2C_INSTANCE_NAME?lower_case}Obj.error = I2C_ERROR_NACK;
                ${I2C_INSTANCE_NAME}CONSET = _${I2C_INSTANCE_NAME}CON_PEN_MASK;
                ${I2C_INSTANCE_NAME?lower_case}Obj.state = I2C_STATE_WAIT_STOP_CONDITION_COMPLETE;
            }
            break;
        case I2C_STATE_READ:
            if (!(${I2C_INSTANCE_NAME}STAT & _${I2C_INSTANCE_NAME}STAT_ACKSTAT_MASK))
            {
                /* Slave ACK'd the device address. Enable receiver. */
                ${I2C_INSTANCE_NAME}CONSET = _${I2C_INSTANCE_NAME}CON_RCEN_MASK;
                ${I2C_INSTANCE_NAME?lower_case}Obj.state = I2C_STATE_READ_BYTE;
            }
            else
            {
                /* NAK received. Generate Stop Condition. */
                ${I2C_INSTANCE_NAME?lower_case}Obj.error = I2C_ERROR_NACK;
                ${I2C_INSTANCE_NAME}CONSET = _${I2C_INSTANCE_NAME}CON_PEN_MASK;
                ${I2C_INSTANCE_NAME?lower_case}Obj.state = I2C_STATE_WAIT_STOP_CONDITION_COMPLETE;
            }
            break;

        case I2C_STATE_READ_BYTE:
            /* Data received from the slave */
            if (${I2C_INSTANCE_NAME}STAT & _${I2C_INSTANCE_NAME}STAT_RBF_MASK)
            {
                ${I2C_INSTANCE_NAME?lower_case}Obj.readBuffer[${I2C_INSTANCE_NAME?lower_case}Obj.readCount++] = ${I2C_INSTANCE_NAME}RCV;
                if (${I2C_INSTANCE_NAME?lower_case}Obj.readCount == ${I2C_INSTANCE_NAME?lower_case}Obj.readSize)
                {
                    /* Send NAK */
                    ${I2C_INSTANCE_NAME}CONSET = _${I2C_INSTANCE_NAME}CON_ACKDT_MASK;
                    ${I2C_INSTANCE_NAME}CONSET = _${I2C_INSTANCE_NAME}CON_ACKEN_MASK;
                }
                else
                {
                    /* Send ACK */
                    ${I2C_INSTANCE_NAME}CONCLR = _${I2C_INSTANCE_NAME}CON_ACKDT_MASK;
                    ${I2C_INSTANCE_NAME}CONSET = _${I2C_INSTANCE_NAME}CON_ACKEN_MASK;
                }
                ${I2C_INSTANCE_NAME?lower_case}Obj.state = I2C_STATE_WAIT_ACK_COMPLETE;
            }
            break;

        case I2C_STATE_WAIT_ACK_COMPLETE:
            /* ACK or NAK sent to the I2C slave */
            if (${I2C_INSTANCE_NAME?lower_case}Obj.readCount < ${I2C_INSTANCE_NAME?lower_case}Obj.readSize)
            {
                /* Enable receiver */
                ${I2C_INSTANCE_NAME}CONSET = _${I2C_INSTANCE_NAME}CON_RCEN_MASK;
                ${I2C_INSTANCE_NAME?lower_case}Obj.state = I2C_STATE_READ_BYTE;
            }
            else
            {
                /* Generate Stop Condition */
                ${I2C_INSTANCE_NAME}CONSET = _${I2C_INSTANCE_NAME}CON_PEN_MASK;
                ${I2C_INSTANCE_NAME?lower_case}Obj.state = I2C_STATE_WAIT_STOP_CONDITION_COMPLETE;
            }
            break;

        case I2C_STATE_WAIT_STOP_CONDITION_COMPLETE:
            ${I2C_INSTANCE_NAME?lower_case}Obj.state = I2C_STATE_IDLE;
            ${I2C_MASTER_IEC_REG}CLR = _${I2C_MASTER_IEC_REG}_${I2C_INSTANCE_NAME}MIE_MASK;
            ${I2C_BUS_IEC_REG}CLR = _${I2C_BUS_IEC_REG}_${I2C_INSTANCE_NAME}BIE_MASK;
            if (${I2C_INSTANCE_NAME?lower_case}Obj.callback != NULL)
            {
                ${I2C_INSTANCE_NAME?lower_case}Obj.callback(${I2C_INSTANCE_NAME?lower_case}Obj.context);
            }
            break;

        default:
            break;
    }
    ${I2C_MASTER_IFS_REG}CLR = _${I2C_MASTER_IFS_REG}_${I2C_INSTANCE_NAME}MIF_MASK;
}


void ${I2C_INSTANCE_NAME}_CallbackRegister(I2C_CALLBACK callback, uintptr_t contextHandle)
{
    if (callback == NULL)
    {
        return;
    }

    ${I2C_INSTANCE_NAME?lower_case}Obj.callback = callback;
    ${I2C_INSTANCE_NAME?lower_case}Obj.context = contextHandle;
}

bool ${I2C_INSTANCE_NAME}_IsBusy(void)
{
    if( (${I2C_INSTANCE_NAME?lower_case}Obj.state != I2C_STATE_IDLE ) || (${I2C_INSTANCE_NAME}CON & 0x0000001F) ||
        (${I2C_INSTANCE_NAME}STAT & _${I2C_INSTANCE_NAME}STAT_TRSTAT_MASK) || (${I2C_INSTANCE_NAME}STAT & _${I2C_INSTANCE_NAME}STAT_S_MASK) )
    {
        return true;
    }
    else
    {
        return false;
    }
}

bool ${I2C_INSTANCE_NAME}_Read(uint16_t address, uint8_t* rdata, size_t rlength)
{
    /* State machine must be idle and I2C module should not have detected a start bit on the bus */
    if((${I2C_INSTANCE_NAME?lower_case}Obj.state != I2C_STATE_IDLE) || (${I2C_INSTANCE_NAME}STAT & _${I2C_INSTANCE_NAME}STAT_S_MASK))
    {
        return false;
    }

    ${I2C_INSTANCE_NAME?lower_case}Obj.address             = address;
    ${I2C_INSTANCE_NAME?lower_case}Obj.readBuffer          = rdata;
    ${I2C_INSTANCE_NAME?lower_case}Obj.readSize            = rlength;
    ${I2C_INSTANCE_NAME?lower_case}Obj.writeBuffer         = NULL;
    ${I2C_INSTANCE_NAME?lower_case}Obj.writeSize           = 0;
    ${I2C_INSTANCE_NAME?lower_case}Obj.writeCount          = 0;
    ${I2C_INSTANCE_NAME?lower_case}Obj.readCount           = 0;
    ${I2C_INSTANCE_NAME?lower_case}Obj.transferType        = I2C_TRANSFER_TYPE_READ;
    ${I2C_INSTANCE_NAME?lower_case}Obj.error               = I2C_ERROR_NONE;
    ${I2C_INSTANCE_NAME?lower_case}Obj.state               = I2C_STATE_ADDR_BYTE_1_SEND;

    ${I2C_INSTANCE_NAME}CONSET                  = _${I2C_INSTANCE_NAME}CON_SEN_MASK;
    ${I2C_MASTER_IEC_REG}SET                     = _${I2C_MASTER_IEC_REG}_${I2C_INSTANCE_NAME}MIE_MASK;
    ${I2C_BUS_IEC_REG}SET                     = _${I2C_BUS_IEC_REG}_${I2C_INSTANCE_NAME}BIE_MASK;

    return true;
}


bool ${I2C_INSTANCE_NAME}_Write(uint16_t address, uint8_t* wdata, size_t wlength)
{
    /* State machine must be idle and I2C module should not have detected a start bit on the bus */
    if((${I2C_INSTANCE_NAME?lower_case}Obj.state != I2C_STATE_IDLE) || (${I2C_INSTANCE_NAME}STAT & _${I2C_INSTANCE_NAME}STAT_S_MASK))
    {
        return false;
    }

    ${I2C_INSTANCE_NAME?lower_case}Obj.address             = address;
    ${I2C_INSTANCE_NAME?lower_case}Obj.readBuffer          = NULL;
    ${I2C_INSTANCE_NAME?lower_case}Obj.readSize            = 0;
    ${I2C_INSTANCE_NAME?lower_case}Obj.writeBuffer         = wdata;
    ${I2C_INSTANCE_NAME?lower_case}Obj.writeSize           = wlength;
    ${I2C_INSTANCE_NAME?lower_case}Obj.writeCount          = 0;
    ${I2C_INSTANCE_NAME?lower_case}Obj.readCount           = 0;
    ${I2C_INSTANCE_NAME?lower_case}Obj.transferType        = I2C_TRANSFER_TYPE_WRITE;
    ${I2C_INSTANCE_NAME?lower_case}Obj.error               = I2C_ERROR_NONE;
    ${I2C_INSTANCE_NAME?lower_case}Obj.state               = I2C_STATE_ADDR_BYTE_1_SEND;

    ${I2C_INSTANCE_NAME}CONSET                  = _${I2C_INSTANCE_NAME}CON_SEN_MASK;
    ${I2C_MASTER_IEC_REG}SET                     = _${I2C_MASTER_IEC_REG}_${I2C_INSTANCE_NAME}MIE_MASK;
    ${I2C_BUS_IEC_REG}SET                     = _${I2C_BUS_IEC_REG}_${I2C_INSTANCE_NAME}BIE_MASK;

    return true;
}

bool ${I2C_INSTANCE_NAME}_WriteRead(uint16_t address, uint8_t* wdata, size_t wlength, uint8_t* rdata, size_t rlength)
{
    /* State machine must be idle and I2C module should not have detected a start bit on the bus */
    if((${I2C_INSTANCE_NAME?lower_case}Obj.state != I2C_STATE_IDLE) || (${I2C_INSTANCE_NAME}STAT & _${I2C_INSTANCE_NAME}STAT_S_MASK))
    {
        return false;
    }

    ${I2C_INSTANCE_NAME?lower_case}Obj.address             = address;
    ${I2C_INSTANCE_NAME?lower_case}Obj.readBuffer          = rdata;
    ${I2C_INSTANCE_NAME?lower_case}Obj.readSize            = rlength;
    ${I2C_INSTANCE_NAME?lower_case}Obj.writeBuffer         = wdata;
    ${I2C_INSTANCE_NAME?lower_case}Obj.writeSize           = wlength;
    ${I2C_INSTANCE_NAME?lower_case}Obj.writeCount          = 0;
    ${I2C_INSTANCE_NAME?lower_case}Obj.readCount           = 0;
    ${I2C_INSTANCE_NAME?lower_case}Obj.transferType        = I2C_TRANSFER_TYPE_WRITE;
    ${I2C_INSTANCE_NAME?lower_case}Obj.error               = I2C_ERROR_NONE;
    ${I2C_INSTANCE_NAME?lower_case}Obj.state               = I2C_STATE_ADDR_BYTE_1_SEND;

    ${I2C_INSTANCE_NAME}CONSET                  = _${I2C_INSTANCE_NAME}CON_SEN_MASK;
    ${I2C_MASTER_IEC_REG}SET                     = _${I2C_MASTER_IEC_REG}_${I2C_INSTANCE_NAME}MIE_MASK;
    ${I2C_BUS_IEC_REG}SET                     = _${I2C_BUS_IEC_REG}_${I2C_INSTANCE_NAME}BIE_MASK;

    return true;
}

I2C_ERROR ${I2C_INSTANCE_NAME}_ErrorGet(void)
{
    I2C_ERROR error;

    error = ${I2C_INSTANCE_NAME?lower_case}Obj.error;
    ${I2C_INSTANCE_NAME?lower_case}Obj.error = I2C_ERROR_NONE;

    return error;
}

static void ${I2C_INSTANCE_NAME}_BUS_InterruptHandler(void)
{
    /* Clear the bus collision error status bit */
    ${I2C_INSTANCE_NAME}STATCLR = _${I2C_INSTANCE_NAME}STAT_BCL_MASK;

    /* ACK the bus interrupt */
    ${I2C_MASTER_IFS_REG}CLR = _${I2C_MASTER_IFS_REG}_${I2C_INSTANCE_NAME}BIF_MASK;

    ${I2C_INSTANCE_NAME?lower_case}Obj.state = I2C_STATE_IDLE;

    ${I2C_INSTANCE_NAME?lower_case}Obj.error = I2C_ERROR_BUS_COLLISION;

    if (${I2C_INSTANCE_NAME?lower_case}Obj.callback != NULL)
    {
        ${I2C_INSTANCE_NAME?lower_case}Obj.callback(${I2C_INSTANCE_NAME?lower_case}Obj.context);
    }
}

static void ${I2C_INSTANCE_NAME}_MASTER_InterruptHandler(void)
{
    ${I2C_INSTANCE_NAME}_TransferSM();
}

void I2C_${I2C_INSTANCE_NUM}_InterruptHandler(void)
{
    if ((${I2C_BUS_IFS_REG} & _${I2C_BUS_IFS_REG}_${I2C_INSTANCE_NAME}BIF_MASK) && (${I2C_BUS_IEC_REG} & _${I2C_BUS_IEC_REG}_${I2C_INSTANCE_NAME}BIE_MASK))
    {
        ${I2C_INSTANCE_NAME}_BUS_InterruptHandler();
    }
    else if ((${I2C_MASTER_IFS_REG} & _${I2C_MASTER_IFS_REG}_${I2C_INSTANCE_NAME}MIF_MASK) && (${I2C_MASTER_IEC_REG} & _${I2C_MASTER_IEC_REG}_${I2C_INSTANCE_NAME}MIE_MASK))
    {
        ${I2C_INSTANCE_NAME}_MASTER_InterruptHandler();
    }
}