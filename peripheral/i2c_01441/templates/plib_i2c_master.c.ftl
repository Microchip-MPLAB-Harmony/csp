/*******************************************************************************
  Inter-Integrated Circuit (I2C) Library
  Source File

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${I2C_INSTANCE_NAME?lower_case}_master.c

  Summary:
    I2C PLIB Master Mode Implementation file

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
#include "plib_${I2C_INSTANCE_NAME?lower_case}_master.h"
<#if core.CoreSysIntFile == true>
#include "interrupts.h"
</#if>

// *****************************************************************************
// *****************************************************************************
// Section: Global Data
// *****************************************************************************
// *****************************************************************************
#define NOP asm(" NOP")

<#assign I2C_PLIB = "I2C_INSTANCE_NAME">
<#assign I2C_PLIB_CLOCK_FREQUENCY = "core." + I2C_PLIB?eval + "_CLOCK_FREQUENCY">

static I2C_OBJ ${I2C_INSTANCE_NAME?lower_case}Obj;

void ${I2C_INSTANCE_NAME}_Initialize(void)
{
    /* Disable the I2C Master interrupt */
    ${I2C_MASTER_IEC_REG}CLR = _${I2C_MASTER_IEC_REG}_${I2C_INSTANCE_NAME}MIE_MASK;

    /* Disable the I2C Bus collision interrupt */
    ${I2C_BUS_IEC_REG}CLR = _${I2C_BUS_IEC_REG}_${I2C_BUS_COLLISION_INT_ENABLE_BIT_NAME}_MASK;

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
    ${I2C_BUS_IFS_REG}CLR = _${I2C_BUS_IFS_REG}_${I2C_BUS_COLLISION_INT_FLAG_BIT_NAME}_MASK;

    /* Turn on the I2C module */
    ${I2C_INSTANCE_NAME}CONSET = _${I2C_INSTANCE_NAME}CON_ON_MASK;

    /* Set the initial state of the I2C state machine */
    ${I2C_INSTANCE_NAME?lower_case}Obj.state = I2C_STATE_IDLE;
}

/* I2C state machine */
static void ${I2C_INSTANCE_NAME}_TransferSM(void)
{
    uint8_t tempVar = 0;
    ${I2C_MASTER_IFS_REG}CLR = _${I2C_MASTER_IFS_REG}_${I2C_INSTANCE_NAME}MIF_MASK;

    switch (${I2C_INSTANCE_NAME?lower_case}Obj.state)
    {
        case I2C_STATE_START_CONDITION:
            /* Generate Start Condition */
            ${I2C_INSTANCE_NAME}CONSET = _${I2C_INSTANCE_NAME}CON_SEN_MASK;
            ${I2C_MASTER_IEC_REG}SET = _${I2C_MASTER_IEC_REG}_${I2C_INSTANCE_NAME}MIE_MASK;
            ${I2C_BUS_IEC_REG}SET = _${I2C_BUS_IEC_REG}_${I2C_BUS_COLLISION_INT_ENABLE_BIT_NAME}_MASK;
            ${I2C_INSTANCE_NAME?lower_case}Obj.state = I2C_STATE_ADDR_BYTE_1_SEND;
            break;

        case I2C_STATE_ADDR_BYTE_1_SEND:
            /* Is transmit buffer full? */
            if ((${I2C_INSTANCE_NAME}STAT & _${I2C_INSTANCE_NAME}STAT_TBF_MASK) == 0U)
            {
                if (${I2C_INSTANCE_NAME?lower_case}Obj.address > 0x007FU)
                {
                    tempVar = (((uint8_t*)&${I2C_INSTANCE_NAME?lower_case}Obj.address)[1] << 1);
                    /* Transmit the MSB 2 bits of the 10-bit slave address, with R/W = 0 */
                    ${I2C_INSTANCE_NAME}TRN = (uint32_t)( 0xF0U | (uint32_t)tempVar);

                    ${I2C_INSTANCE_NAME?lower_case}Obj.state = I2C_STATE_ADDR_BYTE_2_SEND;
                }
                else
                {
                    /* 8-bit addressing mode */
                    ${I2C_INSTANCE_NAME}TRN = (((uint32_t)${I2C_INSTANCE_NAME?lower_case}Obj.address << 1) | (uint32_t)${I2C_INSTANCE_NAME?lower_case}Obj.transferType);

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
            <#if I2C_INCLUDE_FORCED_WRITE_API == true>
            if (((${I2C_INSTANCE_NAME}STAT & _${I2C_INSTANCE_NAME}STAT_ACKSTAT_MASK) == 0U) || (${I2C_INSTANCE_NAME?lower_case}Obj.forcedWrite == true))
            <#else>
            if ((${I2C_INSTANCE_NAME}STAT & _${I2C_INSTANCE_NAME}STAT_ACKSTAT_MASK) == 0U)
            </#if>
            {
                if ((${I2C_INSTANCE_NAME}STAT & _${I2C_INSTANCE_NAME}STAT_TBF_MASK) == 0U)
                {
                    /* Transmit the remaining 8-bits of the 10-bit address */
                    ${I2C_INSTANCE_NAME}TRN = ${I2C_INSTANCE_NAME?lower_case}Obj.address;

                    if (${I2C_INSTANCE_NAME?lower_case}Obj.transferType == I2C_TRANSFER_TYPE_WRITE)
                    {
                        ${I2C_INSTANCE_NAME?lower_case}Obj.state = I2C_STATE_WRITE;
                    }
                    else
                    {
                        ${I2C_INSTANCE_NAME?lower_case}Obj.state = I2C_STATE_READ_10BIT_MODE;
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

        case I2C_STATE_READ_10BIT_MODE:
            if ((${I2C_INSTANCE_NAME}STAT & _${I2C_INSTANCE_NAME}STAT_ACKSTAT_MASK) == 0U)
            {
                /* Generate repeated start condition */
                ${I2C_INSTANCE_NAME}CONSET = _${I2C_INSTANCE_NAME}CON_RSEN_MASK;
                ${I2C_INSTANCE_NAME?lower_case}Obj.state = I2C_STATE_ADDR_BYTE_1_SEND_10BIT_ONLY;
            }
            else
            {
                /* NAK received. Generate Stop Condition. */
                ${I2C_INSTANCE_NAME?lower_case}Obj.error = I2C_ERROR_NACK;
                ${I2C_INSTANCE_NAME}CONSET = _${I2C_INSTANCE_NAME}CON_PEN_MASK;
                ${I2C_INSTANCE_NAME?lower_case}Obj.state = I2C_STATE_WAIT_STOP_CONDITION_COMPLETE;
            }
            break;

        case I2C_STATE_ADDR_BYTE_1_SEND_10BIT_ONLY:
            /* Is transmit buffer full? */
            if ((${I2C_INSTANCE_NAME}STAT & _${I2C_INSTANCE_NAME}STAT_TBF_MASK) == 0U)
            {
                tempVar = (((uint8_t*)&${I2C_INSTANCE_NAME?lower_case}Obj.address)[1] << 1);
                /* Transmit the first byte of the 10-bit slave address, with R/W = 1 */
                ${I2C_INSTANCE_NAME}TRN = (uint32_t)( 0xF1U | (uint32_t)tempVar);
                ${I2C_INSTANCE_NAME?lower_case}Obj.state = I2C_STATE_READ;
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
            <#if I2C_INCLUDE_FORCED_WRITE_API == true>
            if (((${I2C_INSTANCE_NAME}STAT & _${I2C_INSTANCE_NAME}STAT_ACKSTAT_MASK) == 0U) || (${I2C_INSTANCE_NAME?lower_case}Obj.forcedWrite == true))
            <#else>
            if ((${I2C_INSTANCE_NAME}STAT & _${I2C_INSTANCE_NAME}STAT_ACKSTAT_MASK) == 0U)
            </#if>
            {
                /* ACK received */
                if (${I2C_INSTANCE_NAME?lower_case}Obj.writeCount < ${I2C_INSTANCE_NAME?lower_case}Obj.writeSize)
                {
                    if ((${I2C_INSTANCE_NAME}STAT & _${I2C_INSTANCE_NAME}STAT_TBF_MASK) == 0U)
                    {
                        /* Transmit the data from writeBuffer[] */
                        ${I2C_INSTANCE_NAME}TRN = ${I2C_INSTANCE_NAME?lower_case}Obj.writeBuffer[${I2C_INSTANCE_NAME?lower_case}Obj.writeCount];
                        ${I2C_INSTANCE_NAME?lower_case}Obj.writeCount++;

                    }
                }
                else
                {
                    if (${I2C_INSTANCE_NAME?lower_case}Obj.readCount < ${I2C_INSTANCE_NAME?lower_case}Obj.readSize)
                    {
                        /* Generate repeated start condition */
                        ${I2C_INSTANCE_NAME}CONSET = _${I2C_INSTANCE_NAME}CON_RSEN_MASK;

                        ${I2C_INSTANCE_NAME?lower_case}Obj.transferType = I2C_TRANSFER_TYPE_READ;

                        if (${I2C_INSTANCE_NAME?lower_case}Obj.address > 0x007FU)
                        {
                            /* Send the I2C slave address with R/W = 1 */
                            ${I2C_INSTANCE_NAME?lower_case}Obj.state = I2C_STATE_ADDR_BYTE_1_SEND_10BIT_ONLY;
                        }
                        else
                        {
                            /* Send the I2C slave address with R/W = 1 */
                            ${I2C_INSTANCE_NAME?lower_case}Obj.state = I2C_STATE_ADDR_BYTE_1_SEND;
                        }

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
            if ((${I2C_INSTANCE_NAME}STAT & _${I2C_INSTANCE_NAME}STAT_ACKSTAT_MASK) == 0U)
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
            if ((${I2C_INSTANCE_NAME}STAT & _${I2C_INSTANCE_NAME}STAT_RBF_MASK) != 0U)
            {
                ${I2C_INSTANCE_NAME?lower_case}Obj.readBuffer[${I2C_INSTANCE_NAME?lower_case}Obj.readCount] = (uint8_t)${I2C_INSTANCE_NAME}RCV;
                ${I2C_INSTANCE_NAME?lower_case}Obj.readCount++;
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
            ${I2C_BUS_IEC_REG}CLR = _${I2C_BUS_IEC_REG}_${I2C_BUS_COLLISION_INT_ENABLE_BIT_NAME}_MASK;
            if (${I2C_INSTANCE_NAME?lower_case}Obj.callback != NULL)
            {
                ${I2C_INSTANCE_NAME?lower_case}Obj.callback(${I2C_INSTANCE_NAME?lower_case}Obj.context);
            }
            break;

        default:
                   /*Do Nothing*/
            break;
    }
}


void ${I2C_INSTANCE_NAME}_CallbackRegister(I2C_CALLBACK callback, uintptr_t contextHandle)
{
    if (callback != NULL)
    {
       ${I2C_INSTANCE_NAME?lower_case}Obj.callback = callback;
       ${I2C_INSTANCE_NAME?lower_case}Obj.context = contextHandle;
    }
    return;
}

bool ${I2C_INSTANCE_NAME}_IsBusy(void)
{
    bool busycheck = false;
    uint32_t tempVar = ${I2C_INSTANCE_NAME}CON;
    uint32_t tempVar1 = ${I2C_INSTANCE_NAME}STAT;
    if( (${I2C_INSTANCE_NAME?lower_case}Obj.state != I2C_STATE_IDLE ) || ((tempVar & 0x0000001FU) != 0U) ||
        ((tempVar1 & _${I2C_INSTANCE_NAME}STAT_TRSTAT_MASK) != 0U) || ((tempVar1 & _${I2C_INSTANCE_NAME}STAT_S_MASK) != 0U) )
    {
        busycheck = true;
    }
    return busycheck;
}

bool ${I2C_INSTANCE_NAME}_Read(uint16_t address, uint8_t* rdata, size_t rlength)
{
    bool statusRead = false;
    uint32_t tempVar = ${I2C_INSTANCE_NAME}STAT;
    /* State machine must be idle and I2C module should not have detected a start bit on the bus */
    if((${I2C_INSTANCE_NAME?lower_case}Obj.state == I2C_STATE_IDLE) && (( tempVar & _${I2C_INSTANCE_NAME}STAT_S_MASK) == 0U))
    {
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
        <#if I2C_INCLUDE_FORCED_WRITE_API == true>
        ${I2C_INSTANCE_NAME?lower_case}Obj.forcedWrite         = false;
        </#if>

        ${I2C_INSTANCE_NAME}CONSET                  = _${I2C_INSTANCE_NAME}CON_SEN_MASK;
        ${I2C_MASTER_IEC_REG}SET                     = _${I2C_MASTER_IEC_REG}_${I2C_INSTANCE_NAME}MIE_MASK;
        ${I2C_BUS_IEC_REG}SET                     = _${I2C_BUS_IEC_REG}_${I2C_BUS_COLLISION_INT_ENABLE_BIT_NAME}_MASK;
        statusRead = true;
    }
    return statusRead;
}


bool ${I2C_INSTANCE_NAME}_Write(uint16_t address, uint8_t* wdata, size_t wlength)
{
    bool statusWrite = false;
    uint32_t tempVar = ${I2C_INSTANCE_NAME}STAT;
    /* State machine must be idle and I2C module should not have detected a start bit on the bus */
    if((${I2C_INSTANCE_NAME?lower_case}Obj.state == I2C_STATE_IDLE) && (( tempVar & _${I2C_INSTANCE_NAME}STAT_S_MASK) == 0U))
    {
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
        <#if I2C_INCLUDE_FORCED_WRITE_API == true>
        ${I2C_INSTANCE_NAME?lower_case}Obj.forcedWrite         = false;
        </#if>

        ${I2C_INSTANCE_NAME}CONSET                  = _${I2C_INSTANCE_NAME}CON_SEN_MASK;
        ${I2C_MASTER_IEC_REG}SET                     = _${I2C_MASTER_IEC_REG}_${I2C_INSTANCE_NAME}MIE_MASK;
        ${I2C_BUS_IEC_REG}SET                     = _${I2C_BUS_IEC_REG}_${I2C_BUS_COLLISION_INT_ENABLE_BIT_NAME}_MASK;
        statusWrite = true;
    }
    return statusWrite;
}

<#if I2C_INCLUDE_FORCED_WRITE_API == true>
bool ${I2C_INSTANCE_NAME}_WriteForced(uint16_t address, uint8_t* wdata, size_t wlength)
{
     bool statusWriteForced = false;
     uint32_t tempVar = ${I2C_INSTANCE_NAME}STAT;
    /* State machine must be idle and I2C module should not have detected a start bit on the bus */
    if((${I2C_INSTANCE_NAME?lower_case}Obj.state == I2C_STATE_IDLE) &&
       ((tempVar & _${I2C_INSTANCE_NAME}STAT_S_MASK) == 0U))
    {

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
        ${I2C_INSTANCE_NAME?lower_case}Obj.forcedWrite         = true;

        ${I2C_INSTANCE_NAME}CONSET                  = _${I2C_INSTANCE_NAME}CON_SEN_MASK;
        ${I2C_MASTER_IEC_REG}SET                     = _${I2C_MASTER_IEC_REG}_${I2C_INSTANCE_NAME}MIE_MASK;
        ${I2C_BUS_IEC_REG}SET                     = _${I2C_BUS_IEC_REG}_${I2C_BUS_COLLISION_INT_ENABLE_BIT_NAME}_MASK;
        statusWriteForced = true;
    }

    return statusWriteForced;
}
</#if>

bool ${I2C_INSTANCE_NAME}_WriteRead(uint16_t address, uint8_t* wdata, size_t wlength, uint8_t* rdata, size_t rlength)
{
    bool statusWriteread = false;
    uint32_t tempVar = ${I2C_INSTANCE_NAME}STAT;
    /* State machine must be idle and I2C module should not have detected a start bit on the bus */
    if((${I2C_INSTANCE_NAME?lower_case}Obj.state == I2C_STATE_IDLE) &&
       ((tempVar & _${I2C_INSTANCE_NAME}STAT_S_MASK) == 0U))
    {
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
        <#if I2C_INCLUDE_FORCED_WRITE_API == true>
        ${I2C_INSTANCE_NAME?lower_case}Obj.forcedWrite         = false;
        </#if>

        ${I2C_INSTANCE_NAME}CONSET                  = _${I2C_INSTANCE_NAME}CON_SEN_MASK;
        ${I2C_MASTER_IEC_REG}SET                     = _${I2C_MASTER_IEC_REG}_${I2C_INSTANCE_NAME}MIE_MASK;
        ${I2C_BUS_IEC_REG}SET                     = _${I2C_BUS_IEC_REG}_${I2C_BUS_COLLISION_INT_ENABLE_BIT_NAME}_MASK;
        statusWriteread = true;
    }
    return statusWriteread;
}

I2C_ERROR ${I2C_INSTANCE_NAME}_ErrorGet(void)
{
    I2C_ERROR error;

    error = ${I2C_INSTANCE_NAME?lower_case}Obj.error;
    ${I2C_INSTANCE_NAME?lower_case}Obj.error = I2C_ERROR_NONE;

    return error;
}

bool ${I2C_INSTANCE_NAME}_TransferSetup(I2C_TRANSFER_SETUP* setup, uint32_t srcClkFreq )
{
    uint32_t baudValue;
    uint32_t i2cClkSpeed;

    if (setup == NULL)
    {
        return false;
    }

    i2cClkSpeed = setup->clkSpeed;

    /* Maximum I2C clock speed cannot be greater than 1 MHz */
    if (i2cClkSpeed > 1000000U)
    {
        return false;
    }

    if( srcClkFreq == 0U)
    {
        srcClkFreq = ${I2C_PLIB_CLOCK_FREQUENCY?eval}UL;
    }

    baudValue = (uint32_t)((float)((float)srcClkFreq/2.0) * ((1/(float)i2cClkSpeed) - 0.000000130f)) - 1U;

    /* I2CxBRG value cannot be from 0 to 3 or more than the size of the baud rate register */
    if ((baudValue < 4U) || (baudValue > ${I2C_MAX_BRG}U))
    {
        return false;
    }

    ${I2C_INSTANCE_NAME}BRG = baudValue;

    /* Enable slew rate for 400 kHz clock speed; disable for all other speeds */

    if (i2cClkSpeed == 400000U)
    {
        ${I2C_INSTANCE_NAME}CONCLR = _${I2C_INSTANCE_NAME}CON_DISSLW_MASK;;
    }
    else
    {
        ${I2C_INSTANCE_NAME}CONSET = _${I2C_INSTANCE_NAME}CON_DISSLW_MASK;;
    }

    return true;
}

void ${I2C_INSTANCE_NAME}_TransferAbort( void )
{
    ${I2C_INSTANCE_NAME?lower_case}Obj.error = I2C_ERROR_NONE;

    // Reset the PLib objects and Interrupts
    ${I2C_INSTANCE_NAME?lower_case}Obj.state = I2C_STATE_IDLE;
    ${I2C_MASTER_IEC_REG}CLR = _${I2C_MASTER_IEC_REG}_${I2C_INSTANCE_NAME}MIE_MASK;
    ${I2C_BUS_IEC_REG}CLR = _${I2C_BUS_IEC_REG}_${I2C_BUS_COLLISION_INT_ENABLE_BIT_NAME}_MASK;

    // Disable and Enable I2C Master
    ${I2C_INSTANCE_NAME}CONCLR = _${I2C_INSTANCE_NAME}CON_ON_MASK;
    NOP;NOP;
    ${I2C_INSTANCE_NAME}CONSET = _${I2C_INSTANCE_NAME}CON_ON_MASK;
}

void ${I2C_INSTANCE_NAME}_BUS_InterruptHandler(void)
{
    /* Clear the bus collision error status bit */
    ${I2C_INSTANCE_NAME}STATCLR = _${I2C_INSTANCE_NAME}STAT_BCL_MASK;

    /* ACK the bus interrupt */
    ${I2C_MASTER_IFS_REG}CLR = _${I2C_MASTER_IFS_REG}_${I2C_BUS_COLLISION_INT_FLAG_BIT_NAME}_MASK;

    ${I2C_INSTANCE_NAME?lower_case}Obj.state = I2C_STATE_IDLE;

    ${I2C_INSTANCE_NAME?lower_case}Obj.error = I2C_ERROR_BUS_COLLISION;

    if (${I2C_INSTANCE_NAME?lower_case}Obj.callback != NULL)
    {
        ${I2C_INSTANCE_NAME?lower_case}Obj.callback(${I2C_INSTANCE_NAME?lower_case}Obj.context);
    }
}

void ${I2C_INSTANCE_NAME}_MASTER_InterruptHandler(void)
{
    ${I2C_INSTANCE_NAME}_TransferSM();
}
