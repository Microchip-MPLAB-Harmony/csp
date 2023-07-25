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
<#if I2C_SMEN == true>
#include <string.h>
#include "peripheral/i2c/plib_i2c_smbus_common.h"
</#if>

<#assign I2C_API_PREFIX = I2C_INSTANCE_NAME + "_">
<#if I2C_OPERATING_MODE == "Master and Slave">
<#assign I2C_API_PREFIX = I2C_INSTANCE_NAME + "_Master">
</#if>

// *****************************************************************************
// *****************************************************************************
// Section: Global Data
// *****************************************************************************
// *****************************************************************************
#define NOP asm(" NOP")

<#assign I2C_PLIB = "I2C_INSTANCE_NAME">
<#assign I2C_PLIB_CLOCK_FREQUENCY = "core." + I2C_PLIB?eval + "_CLOCK_FREQUENCY">

volatile static I2C_OBJ ${I2C_INSTANCE_NAME?lower_case}MasterObj;

<#if I2C_SMEN == true>
/* <cmd> <blocklen n> <data 1> ... <data n> <pec>*/
/* Total 1 + 1 + 255 + 1 = 258 bytes*/
volatile static uint8_t ${I2C_INSTANCE_NAME?lower_case}SMBUSWrBuffer[258];
/* <blocklen n> <data 1> ... <data n> <pec>*/
/* Total 1 + 255 + 1 = 257 bytes*/
volatile static uint8_t ${I2C_INSTANCE_NAME?lower_case}SMBUSRdBuffer[257];
</#if>

void ${I2C_API_PREFIX}Initialize(void)
{
    /* Disable the I2C Master interrupt */
    ${I2C_MASTER_IEC_REG}CLR = _${I2C_MASTER_IEC_REG}_${I2C_INSTANCE_NAME}MIE_MASK;

    /* Disable the I2C Bus collision interrupt */
    ${I2C_BUS_IEC_REG}CLR = _${I2C_BUS_IEC_REG}_${I2C_BUS_COLLISION_INT_ENABLE_BIT_NAME}_MASK;

    ${I2C_INSTANCE_NAME}BRG = ${BRG_VALUE};

<#if I2C_OPERATING_MODE != "Master and Slave">
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
</#if>

    /* Clear master interrupt flag */
    ${I2C_MASTER_IFS_REG}CLR = _${I2C_MASTER_IFS_REG}_${I2C_INSTANCE_NAME}MIF_MASK;

    /* Clear fault interrupt flag */
    ${I2C_BUS_IFS_REG}CLR = _${I2C_BUS_IFS_REG}_${I2C_BUS_COLLISION_INT_FLAG_BIT_NAME}_MASK;

<#if I2C_OPERATING_MODE != "Master and Slave">
    /* Turn on the I2C module */
    ${I2C_INSTANCE_NAME}CONSET = _${I2C_INSTANCE_NAME}CON_ON_MASK;
</#if>

    /* Set the initial state of the I2C state machine */
    ${I2C_INSTANCE_NAME?lower_case}MasterObj.state = I2C_STATE_IDLE;
}

/* I2C state machine */
static void ${I2C_API_PREFIX}TransferSM(void)
{
    uint8_t tempVar = 0;
    ${I2C_MASTER_IFS_REG}CLR = _${I2C_MASTER_IFS_REG}_${I2C_INSTANCE_NAME}MIF_MASK;
    <#if I2C_INCLUDE_FORCED_WRITE_API == true>
    bool forcedWrite = ${I2C_INSTANCE_NAME?lower_case}MasterObj.forcedWrite;
    </#if>

    switch (${I2C_INSTANCE_NAME?lower_case}MasterObj.state)
    {
        case I2C_STATE_START_CONDITION:
            /* Generate Start Condition */
            ${I2C_INSTANCE_NAME}CONSET = _${I2C_INSTANCE_NAME}CON_SEN_MASK;
            ${I2C_MASTER_IEC_REG}SET = _${I2C_MASTER_IEC_REG}_${I2C_INSTANCE_NAME}MIE_MASK;
            ${I2C_BUS_IEC_REG}SET = _${I2C_BUS_IEC_REG}_${I2C_BUS_COLLISION_INT_ENABLE_BIT_NAME}_MASK;
            ${I2C_INSTANCE_NAME?lower_case}MasterObj.state = I2C_STATE_ADDR_BYTE_1_SEND;
            break;

        case I2C_STATE_ADDR_BYTE_1_SEND:
            /* Is transmit buffer full? */
            if ((${I2C_INSTANCE_NAME}STAT & _${I2C_INSTANCE_NAME}STAT_TBF_MASK) == 0U)
            {
                if (${I2C_INSTANCE_NAME?lower_case}MasterObj.address > 0x007FU)
                {
                    tempVar = (((volatile uint8_t*)&${I2C_INSTANCE_NAME?lower_case}MasterObj.address)[1] << 1);
                    /* Transmit the MSB 2 bits of the 10-bit slave address, with R/W = 0 */
                    ${I2C_INSTANCE_NAME}TRN = (uint32_t)( 0xF0U | (uint32_t)tempVar);

                    ${I2C_INSTANCE_NAME?lower_case}MasterObj.state = I2C_STATE_ADDR_BYTE_2_SEND;
                }
                else
                {
                    /* 8-bit addressing mode */
                    I2C_TRANSFER_TYPE transferType = ${I2C_INSTANCE_NAME?lower_case}MasterObj.transferType;

                    ${I2C_INSTANCE_NAME}TRN = (((uint32_t)${I2C_INSTANCE_NAME?lower_case}MasterObj.address << 1) | transferType);

                    if (${I2C_INSTANCE_NAME?lower_case}MasterObj.transferType == I2C_TRANSFER_TYPE_WRITE)
                    {
                        ${I2C_INSTANCE_NAME?lower_case}MasterObj.state = I2C_STATE_WRITE;
                    }
                    else
                    {
                        ${I2C_INSTANCE_NAME?lower_case}MasterObj.state = I2C_STATE_READ;
                    }
                }
            }
            break;

        case I2C_STATE_ADDR_BYTE_2_SEND:
            /* Transmit the 2nd byte of the 10-bit slave address */
            <#if I2C_INCLUDE_FORCED_WRITE_API == true>
            if (((${I2C_INSTANCE_NAME}STAT & _${I2C_INSTANCE_NAME}STAT_ACKSTAT_MASK) == 0U) || (forcedWrite == true))
            <#else>
            if ((${I2C_INSTANCE_NAME}STAT & _${I2C_INSTANCE_NAME}STAT_ACKSTAT_MASK) == 0U)
            </#if>
            {
                if ((${I2C_INSTANCE_NAME}STAT & _${I2C_INSTANCE_NAME}STAT_TBF_MASK) == 0U)
                {
                    /* Transmit the remaining 8-bits of the 10-bit address */
                    ${I2C_INSTANCE_NAME}TRN = ${I2C_INSTANCE_NAME?lower_case}MasterObj.address;

                    if (${I2C_INSTANCE_NAME?lower_case}MasterObj.transferType == I2C_TRANSFER_TYPE_WRITE)
                    {
                        ${I2C_INSTANCE_NAME?lower_case}MasterObj.state = I2C_STATE_WRITE;
                    }
                    else
                    {
                        ${I2C_INSTANCE_NAME?lower_case}MasterObj.state = I2C_STATE_READ_10BIT_MODE;
                    }
                }
            }
            else
            {
                /* NAK received. Generate Stop Condition. */
                ${I2C_INSTANCE_NAME?lower_case}MasterObj.error = I2C_ERROR_NACK;
                ${I2C_INSTANCE_NAME}CONSET = _${I2C_INSTANCE_NAME}CON_PEN_MASK;
                ${I2C_INSTANCE_NAME?lower_case}MasterObj.state = I2C_STATE_WAIT_STOP_CONDITION_COMPLETE;
            }
            break;

        case I2C_STATE_READ_10BIT_MODE:
            if ((${I2C_INSTANCE_NAME}STAT & _${I2C_INSTANCE_NAME}STAT_ACKSTAT_MASK) == 0U)
            {
                /* Generate repeated start condition */
                ${I2C_INSTANCE_NAME}CONSET = _${I2C_INSTANCE_NAME}CON_RSEN_MASK;
                ${I2C_INSTANCE_NAME?lower_case}MasterObj.state = I2C_STATE_ADDR_BYTE_1_SEND_10BIT_ONLY;
            }
            else
            {
                /* NAK received. Generate Stop Condition. */
                ${I2C_INSTANCE_NAME?lower_case}MasterObj.error = I2C_ERROR_NACK;
                ${I2C_INSTANCE_NAME}CONSET = _${I2C_INSTANCE_NAME}CON_PEN_MASK;
                ${I2C_INSTANCE_NAME?lower_case}MasterObj.state = I2C_STATE_WAIT_STOP_CONDITION_COMPLETE;
            }
            break;

        case I2C_STATE_ADDR_BYTE_1_SEND_10BIT_ONLY:
            /* Is transmit buffer full? */
            if ((${I2C_INSTANCE_NAME}STAT & _${I2C_INSTANCE_NAME}STAT_TBF_MASK) == 0U)
            {
                tempVar = (((volatile uint8_t*)&${I2C_INSTANCE_NAME?lower_case}MasterObj.address)[1] << 1);
                /* Transmit the first byte of the 10-bit slave address, with R/W = 1 */
                ${I2C_INSTANCE_NAME}TRN = (uint32_t)( 0xF1U | (uint32_t)tempVar);
                ${I2C_INSTANCE_NAME?lower_case}MasterObj.state = I2C_STATE_READ;
            }
            else
            {
                /* NAK received. Generate Stop Condition. */
                ${I2C_INSTANCE_NAME?lower_case}MasterObj.error = I2C_ERROR_NACK;
                ${I2C_INSTANCE_NAME}CONSET = _${I2C_INSTANCE_NAME}CON_PEN_MASK;
                ${I2C_INSTANCE_NAME?lower_case}MasterObj.state = I2C_STATE_WAIT_STOP_CONDITION_COMPLETE;
            }
            break;

        case I2C_STATE_WRITE:
            <#if I2C_INCLUDE_FORCED_WRITE_API == true>
            if (((${I2C_INSTANCE_NAME}STAT & _${I2C_INSTANCE_NAME}STAT_ACKSTAT_MASK) == 0U) || (forcedWrite == true))
            <#else>
            if ((${I2C_INSTANCE_NAME}STAT & _${I2C_INSTANCE_NAME}STAT_ACKSTAT_MASK) == 0U)
            </#if>
            {
                size_t writeCount = ${I2C_INSTANCE_NAME?lower_case}MasterObj.writeCount;

                /* ACK received */
                if (writeCount < ${I2C_INSTANCE_NAME?lower_case}MasterObj.writeSize)
                {
                    if ((${I2C_INSTANCE_NAME}STAT & _${I2C_INSTANCE_NAME}STAT_TBF_MASK) == 0U)
                    {
                        /* Transmit the data from writeBuffer[] */
                        ${I2C_INSTANCE_NAME}TRN = ${I2C_INSTANCE_NAME?lower_case}MasterObj.writeBuffer[writeCount];
                        ${I2C_INSTANCE_NAME?lower_case}MasterObj.writeCount++;
                    }
                }
                else
                {
                    size_t readSize = ${I2C_INSTANCE_NAME?lower_case}MasterObj.readSize;

                    if (${I2C_INSTANCE_NAME?lower_case}MasterObj.readCount < readSize)
                    {
                        /* Generate repeated start condition */
                        ${I2C_INSTANCE_NAME}CONSET = _${I2C_INSTANCE_NAME}CON_RSEN_MASK;

                        ${I2C_INSTANCE_NAME?lower_case}MasterObj.transferType = I2C_TRANSFER_TYPE_READ;

                        if (${I2C_INSTANCE_NAME?lower_case}MasterObj.address > 0x007FU)
                        {
                            /* Send the I2C slave address with R/W = 1 */
                            ${I2C_INSTANCE_NAME?lower_case}MasterObj.state = I2C_STATE_ADDR_BYTE_1_SEND_10BIT_ONLY;
                        }
                        else
                        {
                            /* Send the I2C slave address with R/W = 1 */
                            ${I2C_INSTANCE_NAME?lower_case}MasterObj.state = I2C_STATE_ADDR_BYTE_1_SEND;
                        }

                    }
                    else
                    {
                        /* Transfer Complete. Generate Stop Condition */
                        ${I2C_INSTANCE_NAME}CONSET = _${I2C_INSTANCE_NAME}CON_PEN_MASK;
                        ${I2C_INSTANCE_NAME?lower_case}MasterObj.state = I2C_STATE_WAIT_STOP_CONDITION_COMPLETE;
                    }
                }
            }
            else
            {
                /* NAK received. Generate Stop Condition. */
                ${I2C_INSTANCE_NAME?lower_case}MasterObj.error = I2C_ERROR_NACK;
                ${I2C_INSTANCE_NAME}CONSET = _${I2C_INSTANCE_NAME}CON_PEN_MASK;
                ${I2C_INSTANCE_NAME?lower_case}MasterObj.state = I2C_STATE_WAIT_STOP_CONDITION_COMPLETE;
            }
            break;

        case I2C_STATE_READ:
            if ((${I2C_INSTANCE_NAME}STAT & _${I2C_INSTANCE_NAME}STAT_ACKSTAT_MASK) == 0U)
            {
                /* Slave ACK'd the device address. Enable receiver. */
                ${I2C_INSTANCE_NAME}CONSET = _${I2C_INSTANCE_NAME}CON_RCEN_MASK;
                ${I2C_INSTANCE_NAME?lower_case}MasterObj.state = I2C_STATE_READ_BYTE;
            }
            else
            {
                /* NAK received. Generate Stop Condition. */
                ${I2C_INSTANCE_NAME?lower_case}MasterObj.error = I2C_ERROR_NACK;
                ${I2C_INSTANCE_NAME}CONSET = _${I2C_INSTANCE_NAME}CON_PEN_MASK;
                ${I2C_INSTANCE_NAME?lower_case}MasterObj.state = I2C_STATE_WAIT_STOP_CONDITION_COMPLETE;
            }
            break;

        case I2C_STATE_READ_BYTE:
            /* Data received from the slave */
            if ((${I2C_INSTANCE_NAME}STAT & _${I2C_INSTANCE_NAME}STAT_RBF_MASK) != 0U)
            {
                size_t readCount = ${I2C_INSTANCE_NAME?lower_case}MasterObj.readCount;
                uint8_t readByte = (uint8_t)${I2C_INSTANCE_NAME}RCV;

                ${I2C_INSTANCE_NAME?lower_case}MasterObj.readBuffer[readCount] = readByte;

                <#if I2C_SMEN == true>
                if (${I2C_INSTANCE_NAME?lower_case}MasterObj.smbusReadBlk == true)
                {
                    ${I2C_INSTANCE_NAME?lower_case}MasterObj.readSize += readByte;

                    if (${I2C_INSTANCE_NAME?lower_case}MasterObj.smbusReadPEC == true)
                    {
                        ${I2C_INSTANCE_NAME?lower_case}MasterObj.readSize += 1;
                    }

                    ${I2C_INSTANCE_NAME?lower_case}MasterObj.smbusReadBlk = false;
                }
                </#if>

                readCount++;
                if (readCount == ${I2C_INSTANCE_NAME?lower_case}MasterObj.readSize)
                {
                    /* Send NAK */
                    ${I2C_INSTANCE_NAME}CONSET = _${I2C_INSTANCE_NAME}CON_ACKDT_MASK;
                    ${I2C_INSTANCE_NAME}CONSET = _${I2C_INSTANCE_NAME}CON_ACKEN_MASK;
                }
                else
                {
                    <#if I2C_SMEN == true>
                    if (${I2C_INSTANCE_NAME?lower_case}MasterObj.smbusReadPEC == true)
                    {
                        ${I2C_INSTANCE_NAME?lower_case}MasterObj.pec = SMBUSCRC8Byte(${I2C_INSTANCE_NAME?lower_case}MasterObj.pec, readByte);
                    }
                    </#if>

                    /* Send ACK */
                    ${I2C_INSTANCE_NAME}CONCLR = _${I2C_INSTANCE_NAME}CON_ACKDT_MASK;
                    ${I2C_INSTANCE_NAME}CONSET = _${I2C_INSTANCE_NAME}CON_ACKEN_MASK;
                }
                ${I2C_INSTANCE_NAME?lower_case}MasterObj.readCount = readCount;
                ${I2C_INSTANCE_NAME?lower_case}MasterObj.state = I2C_STATE_WAIT_ACK_COMPLETE;
            }
            break;

        case I2C_STATE_WAIT_ACK_COMPLETE:
            {
                size_t readSize = ${I2C_INSTANCE_NAME?lower_case}MasterObj.readSize;
                /* ACK or NAK sent to the I2C slave */
                if (${I2C_INSTANCE_NAME?lower_case}MasterObj.readCount < readSize)
                {
                    /* Enable receiver */
                    ${I2C_INSTANCE_NAME}CONSET = _${I2C_INSTANCE_NAME}CON_RCEN_MASK;
                    ${I2C_INSTANCE_NAME?lower_case}MasterObj.state = I2C_STATE_READ_BYTE;
                }
                else
                {
                    /* Generate Stop Condition */
                    ${I2C_INSTANCE_NAME}CONSET = _${I2C_INSTANCE_NAME}CON_PEN_MASK;
                    ${I2C_INSTANCE_NAME?lower_case}MasterObj.state = I2C_STATE_WAIT_STOP_CONDITION_COMPLETE;
                }
            }
            break;

        case I2C_STATE_WAIT_STOP_CONDITION_COMPLETE:
            ${I2C_INSTANCE_NAME?lower_case}MasterObj.state = I2C_STATE_IDLE;
            ${I2C_MASTER_IEC_REG}CLR = _${I2C_MASTER_IEC_REG}_${I2C_INSTANCE_NAME}MIE_MASK;
            ${I2C_BUS_IEC_REG}CLR = _${I2C_BUS_IEC_REG}_${I2C_BUS_COLLISION_INT_ENABLE_BIT_NAME}_MASK;

            if ((${I2C_INSTANCE_NAME?lower_case}MasterObj.callback != NULL) && (${I2C_INSTANCE_NAME?lower_case}MasterObj.busScanInProgress == false))
            {
                uintptr_t context = ${I2C_INSTANCE_NAME?lower_case}MasterObj.context;

                ${I2C_INSTANCE_NAME?lower_case}MasterObj.callback(context);
            }
            break;

        default:
                   /*Do Nothing*/
            break;
    }
}

static void ${I2C_API_PREFIX}XferStart(void)
{
    ${I2C_INSTANCE_NAME}CONSET      = _${I2C_INSTANCE_NAME}CON_SEN_MASK;
    ${I2C_MASTER_IEC_REG}SET        = _${I2C_MASTER_IEC_REG}_${I2C_INSTANCE_NAME}MIE_MASK;
    ${I2C_BUS_IEC_REG}SET           = _${I2C_BUS_IEC_REG}_${I2C_BUS_COLLISION_INT_ENABLE_BIT_NAME}_MASK;
}

static bool ${I2C_API_PREFIX}XferSetup(
    uint16_t address,
    uint8_t* wdata,
    size_t wlength,
    uint8_t* rdata,
    size_t rlength,
    bool forcedWrite,
    bool smbusReadBlk,
    bool smbusReadPEC
)
{
    bool status = false;
    uint32_t tempVar = ${I2C_INSTANCE_NAME}STAT;

    /* State machine must be idle and I2C module should not have detected a start bit on the bus */

    if((${I2C_INSTANCE_NAME?lower_case}MasterObj.state == I2C_STATE_IDLE) &&
       ((tempVar & _${I2C_INSTANCE_NAME}STAT_S_MASK) == 0U) &&
       ((wdata != NULL && wlength != 0) || (rdata != NULL && rlength != 0)))
    {
        ${I2C_INSTANCE_NAME?lower_case}MasterObj.address             = address;
        ${I2C_INSTANCE_NAME?lower_case}MasterObj.readBuffer          = rdata;
        ${I2C_INSTANCE_NAME?lower_case}MasterObj.readSize            = rlength;
        ${I2C_INSTANCE_NAME?lower_case}MasterObj.writeBuffer         = wdata;
        ${I2C_INSTANCE_NAME?lower_case}MasterObj.writeSize           = wlength;
        ${I2C_INSTANCE_NAME?lower_case}MasterObj.writeCount          = 0;
        ${I2C_INSTANCE_NAME?lower_case}MasterObj.readCount           = 0;
        if (wdata != NULL && wlength != 0)
        {
            ${I2C_INSTANCE_NAME?lower_case}MasterObj.transferType    = I2C_TRANSFER_TYPE_WRITE;
        }
        else
        {
            ${I2C_INSTANCE_NAME?lower_case}MasterObj.transferType    = I2C_TRANSFER_TYPE_READ;
        }
        ${I2C_INSTANCE_NAME?lower_case}MasterObj.error               = I2C_ERROR_NONE;
        ${I2C_INSTANCE_NAME?lower_case}MasterObj.state               = I2C_STATE_ADDR_BYTE_1_SEND;
        <#if I2C_INCLUDE_FORCED_WRITE_API == true>
        ${I2C_INSTANCE_NAME?lower_case}MasterObj.forcedWrite         = forcedWrite;
        </#if>
        ${I2C_INSTANCE_NAME?lower_case}MasterObj.smbusReadBlk        = smbusReadBlk;
        ${I2C_INSTANCE_NAME?lower_case}MasterObj.smbusReadPEC        = smbusReadPEC;

        status = true;
    }
    return status;
}

void ${I2C_API_PREFIX}CallbackRegister(I2C_CALLBACK callback, uintptr_t contextHandle)
{
    if (callback != NULL)
    {
       ${I2C_INSTANCE_NAME?lower_case}MasterObj.callback = callback;
       ${I2C_INSTANCE_NAME?lower_case}MasterObj.context = contextHandle;
    }
    return;
}

bool ${I2C_API_PREFIX}IsBusy(void)
{
    bool busycheck = false;
    uint32_t tempVar = ${I2C_INSTANCE_NAME}CON;
    uint32_t tempVar1 = ${I2C_INSTANCE_NAME}STAT;
    if( (${I2C_INSTANCE_NAME?lower_case}MasterObj.state != I2C_STATE_IDLE ) || ((tempVar & 0x0000001FU) != 0U) ||
        ((tempVar1 & _${I2C_INSTANCE_NAME}STAT_TRSTAT_MASK) != 0U) || ((tempVar1 & _${I2C_INSTANCE_NAME}STAT_S_MASK) != 0U) )
    {
        busycheck = true;
    }
    return busycheck;
}

bool ${I2C_API_PREFIX}Read(uint16_t address, uint8_t* rdata, size_t rlength)
{
    bool statusRead = false;
    statusRead = ${I2C_API_PREFIX}XferSetup(address, NULL, 0, rdata, rlength, false, false, false);

    if (statusRead == true)
    {
        ${I2C_API_PREFIX}XferStart();
    }

    return statusRead;
}

bool ${I2C_API_PREFIX}Write(uint16_t address, uint8_t* wdata, size_t wlength)
{
    bool statusWrite = false;
    statusWrite = ${I2C_API_PREFIX}XferSetup(address, wdata, wlength, NULL, 0, false, false, false);

    if (statusWrite == true)
    {
        ${I2C_API_PREFIX}XferStart();
    }

    return statusWrite;
}

<#if I2C_INCLUDE_FORCED_WRITE_API == true>
bool ${I2C_API_PREFIX}WriteForced(uint16_t address, uint8_t* wdata, size_t wlength)
{
    bool statusWriteForced = false;
    statusWriteForced = ${I2C_API_PREFIX}XferSetup(address, wdata, wlength, NULL, 0, false, false, false);

    if (statusWriteForced == true)
    {
        ${I2C_API_PREFIX}XferStart();
    }

    return statusWriteForced;
}
</#if>

bool ${I2C_API_PREFIX}WriteRead(uint16_t address, uint8_t* wdata, size_t wlength, uint8_t* rdata, size_t rlength)
{
    bool statusWriteRead = false;
    statusWriteRead = ${I2C_API_PREFIX}XferSetup(address, wdata, wlength, rdata, rlength, false, false, false);

    if (statusWriteRead == true)
    {
        ${I2C_API_PREFIX}XferStart();
    }

    return statusWriteRead;
}

bool ${I2C_API_PREFIX}BusScan(uint16_t start_addr, uint16_t end_addr, void* pDevicesList, uint8_t* nDevicesFound)
{
    uint8_t* pDevList = (uint8_t*)pDevicesList;
    uint8_t nDevFound = 0;

    if (${I2C_INSTANCE_NAME?lower_case}MasterObj.state != I2C_STATE_IDLE)
    {
        return false;
    }

    if ((pDevList == NULL) || (nDevicesFound == NULL))
    {
        return false;
    }

    ${I2C_INSTANCE_NAME?lower_case}MasterObj.busScanInProgress = true;

    *nDevicesFound = 0;

    for (uint16_t dev_addr = start_addr; dev_addr <= end_addr; dev_addr++)
    {
        while (${I2C_API_PREFIX}Write(dev_addr, NULL, 0) == false)
        {

        }

        while (${I2C_INSTANCE_NAME?lower_case}MasterObj.state != I2C_STATE_IDLE)
        {
            /* Wait for the transfer to complete */
        }

        if (${I2C_INSTANCE_NAME?lower_case}MasterObj.error == I2C_ERROR_NONE)
        {
            /* No error and device responded with an ACK. Add the device to the list of found devices. */
            if (dev_addr > 0x007FU)
            {
                ((uint16_t*)&pDevList)[nDevFound] = dev_addr;
            }
            else
            {
                pDevList[nDevFound] = dev_addr;
            }

            nDevFound += 1;
        }
    }

    *nDevicesFound = nDevFound;

    ${I2C_INSTANCE_NAME?lower_case}MasterObj.busScanInProgress = false;

    return true;
}

<#if I2C_SMEN == true>

<#-- SMBUS related APIs -->

bool ${I2C_API_PREFIX}SMBUSSendByte(uint8_t address, void* pWrdata, bool enPEC)
{
    bool status = false;
    uint32_t xferLen = 0;
    uint8_t crc = 0;    //initial value of crc

    if (${I2C_INSTANCE_NAME?lower_case}MasterObj.state == I2C_STATE_IDLE)
    {
        /* <slave_add> <data1> <pec_from_master> */
        ${I2C_INSTANCE_NAME?lower_case}SMBUSWrBuffer[xferLen++] = *((uint8_t*)pWrdata);
        if (enPEC)
        {
            crc = SMBUSCRC8Byte(crc, (address << 1));
            crc = SMBUSCRC8Byte(crc, *((uint8_t*)pWrdata));

            ${I2C_INSTANCE_NAME?lower_case}SMBUSWrBuffer[xferLen++] = crc;
            ${I2C_INSTANCE_NAME?lower_case}MasterObj.pec = crc;
        }

        status = ${I2C_API_PREFIX}XferSetup(address, (uint8_t*)${I2C_INSTANCE_NAME?lower_case}SMBUSWrBuffer, xferLen, NULL, 0, false, false, false);

        if (status == true)
        {
            ${I2C_API_PREFIX}XferStart();
        }
    }

    return status;
}

bool ${I2C_API_PREFIX}SMBUSWriteByte(uint8_t address, uint8_t cmd, void* pWrdata, bool enPEC)
{
    bool status = false;
    uint32_t xferLen = 0;
    uint8_t crc = 0;    //initial value of crc

    if (${I2C_INSTANCE_NAME?lower_case}MasterObj.state == I2C_STATE_IDLE)
    {
        /* <slave_add> <cmd> <data1> <pec_from_master> */
        ${I2C_INSTANCE_NAME?lower_case}SMBUSWrBuffer[xferLen++] = cmd;
        ${I2C_INSTANCE_NAME?lower_case}SMBUSWrBuffer[xferLen++] = *((uint8_t*)pWrdata);
        if (enPEC)
        {
            crc = SMBUSCRC8Byte(crc, (address << 1));
            crc = SMBUSCRC8Buffer(crc, (uint8_t*)${I2C_INSTANCE_NAME?lower_case}SMBUSWrBuffer, xferLen);

            ${I2C_INSTANCE_NAME?lower_case}SMBUSWrBuffer[xferLen++] = crc;
            ${I2C_INSTANCE_NAME?lower_case}MasterObj.pec = crc;
        }

        status = ${I2C_API_PREFIX}XferSetup(address, (uint8_t*)${I2C_INSTANCE_NAME?lower_case}SMBUSWrBuffer, xferLen, NULL, 0, false, false, false);

        if (status == true)
        {
            ${I2C_API_PREFIX}XferStart();
        }
    }

    return status;
}

bool ${I2C_API_PREFIX}SMBUSWriteWord(uint8_t address, uint8_t cmd, void* pWrdata, bool enPEC)
{
    uint8_t* wrData = (uint8_t*)pWrdata;
    bool status = false;
    uint32_t xferLen = 0;
    uint8_t crc = 0;    //initial value of crc

    if (${I2C_INSTANCE_NAME?lower_case}MasterObj.state == I2C_STATE_IDLE)
    {
        /* <slave_add> <cmd> <data1> <data2> <pec_from_master> */
        ${I2C_INSTANCE_NAME?lower_case}SMBUSWrBuffer[xferLen++] = cmd;
        ${I2C_INSTANCE_NAME?lower_case}SMBUSWrBuffer[xferLen++] = wrData[0];
        ${I2C_INSTANCE_NAME?lower_case}SMBUSWrBuffer[xferLen++] = wrData[1];
        if (enPEC)
        {
            crc = SMBUSCRC8Byte(crc, (address << 1));
            crc = SMBUSCRC8Buffer(crc, (uint8_t*)${I2C_INSTANCE_NAME?lower_case}SMBUSWrBuffer, xferLen);

            ${I2C_INSTANCE_NAME?lower_case}SMBUSWrBuffer[xferLen++] = crc;
            ${I2C_INSTANCE_NAME?lower_case}MasterObj.pec = crc;
        }

        status = ${I2C_API_PREFIX}XferSetup(address, (uint8_t*)(uint8_t*)${I2C_INSTANCE_NAME?lower_case}SMBUSWrBuffer, xferLen, NULL, 0, false, false, false);

        if (status == true)
        {
            ${I2C_API_PREFIX}XferStart();
        }
    }

    return status;
}

bool ${I2C_API_PREFIX}SMBUSWriteBlock(uint8_t address, uint8_t cmd, void* pWrdata, uint32_t nWrBytes, bool enPEC)
{
    bool status = false;
    uint32_t xferLen = 0;
    uint8_t crc = 0;    //initial value of crc

    if (${I2C_INSTANCE_NAME?lower_case}MasterObj.state == I2C_STATE_IDLE)
    {
        /* <slave_add> <cmd> <wr_block_sz n> <data1> <data2> .. <datan> <pec_from_master>*/
        ${I2C_INSTANCE_NAME?lower_case}SMBUSWrBuffer[xferLen++] = cmd;
        ${I2C_INSTANCE_NAME?lower_case}SMBUSWrBuffer[xferLen++] = nWrBytes;

        memcpy((void*)&${I2C_INSTANCE_NAME?lower_case}SMBUSWrBuffer[xferLen], (const void*)pWrdata, nWrBytes);
        xferLen += nWrBytes;

        if (enPEC)
        {
            crc = SMBUSCRC8Byte(crc, (address << 1));
            crc = SMBUSCRC8Buffer(crc, (uint8_t*)${I2C_INSTANCE_NAME?lower_case}SMBUSWrBuffer, xferLen);

            ${I2C_INSTANCE_NAME?lower_case}SMBUSWrBuffer[xferLen++] = crc;
            ${I2C_INSTANCE_NAME?lower_case}MasterObj.pec = crc;
        }

        status = ${I2C_API_PREFIX}XferSetup(address, (uint8_t*)${I2C_INSTANCE_NAME?lower_case}SMBUSWrBuffer, xferLen, NULL, 0, false, false, false);

        if (status == true)
        {
            ${I2C_API_PREFIX}XferStart();
        }
    }

    return status;
}

bool ${I2C_API_PREFIX}SMBUSReceiveByte(uint8_t address, bool enPEC)
{
    bool status = false;
    uint8_t crc = 0;    //initial value of crc

    if (${I2C_INSTANCE_NAME?lower_case}MasterObj.state == I2C_STATE_IDLE)
    {
        /* <slave_add> <data1> <pec_from_slave>*/

        if (enPEC)
        {
            /*PEC will be sent by slave and will be calculated over all the bytes in this transfer. Here master only calculates the CRC on the bytes it is transmitting. */
            crc = SMBUSCRC8Byte(crc, ((address << 1) | 1));

            ${I2C_INSTANCE_NAME?lower_case}MasterObj.pec = crc;
        }

        status = ${I2C_API_PREFIX}XferSetup(address, NULL, 0, (uint8_t*)${I2C_INSTANCE_NAME?lower_case}SMBUSRdBuffer, enPEC == true? 2 : 1, false, false, enPEC == true? true : false);

        if (status == true)
        {
            ${I2C_API_PREFIX}XferStart();
        }
    }

    return status;
}

bool ${I2C_API_PREFIX}SMBUSReadByte(uint8_t address, uint8_t cmd, bool enPEC)
{
    bool status = false;
    uint32_t xferLen = 0;
    uint8_t crc = 0;    //initial value of crc

    if (${I2C_INSTANCE_NAME?lower_case}MasterObj.state == I2C_STATE_IDLE)
    {
        /* <slave_add> <cmd> <slave_add> <data1> <pec_from_slave>*/
        ${I2C_INSTANCE_NAME?lower_case}SMBUSWrBuffer[xferLen++] = cmd;

        if (enPEC)
        {
            /*PEC will be sent by slave and will be calculated over all the bytes in this transfer. Here master only calculates the CRC on the bytes it is transmitting. */
            crc = SMBUSCRC8Byte(crc, (address << 1));
            crc = SMBUSCRC8Buffer(crc, (uint8_t*)${I2C_INSTANCE_NAME?lower_case}SMBUSWrBuffer, xferLen);
            crc = SMBUSCRC8Byte(crc, ((address << 1) | 1));

            ${I2C_INSTANCE_NAME?lower_case}MasterObj.pec = crc;
        }

        status = ${I2C_API_PREFIX}XferSetup(address, (uint8_t*)${I2C_INSTANCE_NAME?lower_case}SMBUSWrBuffer, xferLen, (uint8_t*)${I2C_INSTANCE_NAME?lower_case}SMBUSRdBuffer, enPEC == true? 2 : 1, false, false, enPEC == true? true : false);

        if (status == true)
        {
            ${I2C_API_PREFIX}XferStart();
        }
    }

    return status;
}

bool ${I2C_API_PREFIX}SMBUSReadWord(uint8_t address, uint8_t cmd, bool enPEC)
{
    bool status = false;
    uint32_t xferLen = 0;
    uint8_t crc = 0;    //initial value of crc

    if (${I2C_INSTANCE_NAME?lower_case}MasterObj.state == I2C_STATE_IDLE)
    {
        /* <slave_add> <cmd> <slave_add> <data1> <data2> <pec_from_slave> */
        ${I2C_INSTANCE_NAME?lower_case}SMBUSWrBuffer[xferLen++] = cmd;

        if (enPEC)
        {
            /*PEC will be sent by slave and will be calculated over all the bytes in this transfer. Here master only calculates the CRC on the bytes it is transmitting. */
            crc = SMBUSCRC8Byte(crc, (address << 1));
            crc = SMBUSCRC8Buffer(crc, (uint8_t*)${I2C_INSTANCE_NAME?lower_case}SMBUSWrBuffer, xferLen);
            crc = SMBUSCRC8Byte(crc, ((address << 1) | 1));

            ${I2C_INSTANCE_NAME?lower_case}MasterObj.pec = crc;
        }

        status = ${I2C_API_PREFIX}XferSetup(address, (uint8_t*)${I2C_INSTANCE_NAME?lower_case}SMBUSWrBuffer, 1, (uint8_t*)${I2C_INSTANCE_NAME?lower_case}SMBUSRdBuffer, enPEC == true? 3 : 2, false, false, enPEC == true? true : false);

        if (status == true)
        {
            ${I2C_API_PREFIX}XferStart();
        }
    }

    return status;
}

bool ${I2C_API_PREFIX}SMBUSProcessCall(uint8_t address, uint8_t cmd, void* pWrdata, bool enPEC)
{
    uint8_t* wrData = (uint8_t*)pWrdata;
    bool status = false;
    uint32_t xferLen = 0;
    uint8_t crc = 0;    //initial value of crc

    if (${I2C_INSTANCE_NAME?lower_case}MasterObj.state == I2C_STATE_IDLE)
    {
        /* <slave_add> <cmd> <data1> <data2> <slave_add> <data1> <data2> <pec_from_slave> */
        ${I2C_INSTANCE_NAME?lower_case}SMBUSWrBuffer[xferLen++] = cmd;
        ${I2C_INSTANCE_NAME?lower_case}SMBUSWrBuffer[xferLen++] = wrData[0];
        ${I2C_INSTANCE_NAME?lower_case}SMBUSWrBuffer[xferLen++] = wrData[1];
        if (enPEC)
        {
            /*PEC will be sent by slave and will be calculated over all the bytes in this transfer. Here master only calculates the CRC on the bytes it is transmitting. */
            crc = SMBUSCRC8Byte(crc, (address << 1));
            crc = SMBUSCRC8Buffer(crc, (uint8_t*)${I2C_INSTANCE_NAME?lower_case}SMBUSWrBuffer, xferLen);
            crc = SMBUSCRC8Byte(crc, ((address << 1) | 1));

            ${I2C_INSTANCE_NAME?lower_case}MasterObj.pec = crc;
        }

        status = ${I2C_API_PREFIX}XferSetup(address, (uint8_t*)${I2C_INSTANCE_NAME?lower_case}SMBUSWrBuffer, xferLen, (uint8_t*)${I2C_INSTANCE_NAME?lower_case}SMBUSRdBuffer, enPEC == true? 3 : 2, false, false, enPEC == true? true : false);

        if (status == true)
        {
            ${I2C_API_PREFIX}XferStart();
        }
    }

    return status;
}

bool ${I2C_API_PREFIX}SMBUSReadBlock(uint8_t address, uint8_t cmd, bool enPEC)
{
    bool status = false;
    uint32_t xferLen = 0;
    uint8_t crc = 0;    //initial value of crc

    if (${I2C_INSTANCE_NAME?lower_case}MasterObj.state == I2C_STATE_IDLE)
    {
        /* <slave_add> <cmd> <slave_add> <rd_block_sz n> <data1> <data2> .. <datan><pec_from_slave>*/
        ${I2C_INSTANCE_NAME?lower_case}SMBUSWrBuffer[xferLen++] = cmd;

        if (enPEC)
        {
            /*PEC will be sent by slave and will be calculated over all the bytes in this transfer. Here master only calculates the CRC on the bytes it is transmitting. */
            crc = SMBUSCRC8Byte(crc, (address << 1));
            crc = SMBUSCRC8Buffer(crc, (uint8_t*)${I2C_INSTANCE_NAME?lower_case}SMBUSWrBuffer, xferLen);
            crc = SMBUSCRC8Byte(crc, ((address << 1) | 1));

            ${I2C_INSTANCE_NAME?lower_case}MasterObj.pec = crc;
        }

        status = ${I2C_API_PREFIX}XferSetup(address, (uint8_t*)${I2C_INSTANCE_NAME?lower_case}SMBUSWrBuffer, 1, (uint8_t*)${I2C_INSTANCE_NAME?lower_case}SMBUSRdBuffer, 1, false, true, enPEC == true? true : false);

        if (status == true)
        {
            ${I2C_API_PREFIX}XferStart();
        }
    }

    return status;
}

bool ${I2C_API_PREFIX}SMBUSWriteReadBlock(uint8_t address, uint8_t cmd, void* pWrdata, uint32_t nWrBytes, bool enPEC)
{
    bool status = false;
    uint32_t xferLen = 0;
    uint8_t crc = 0;    //initial value of crc

    if (${I2C_INSTANCE_NAME?lower_case}MasterObj.state == I2C_STATE_IDLE)
    {
        /* <slave_add> <cmd> <wr_block_sz n> <data1> <data2> .. <datan> <slave_add> <rd_block_sz n> <data1> <data1> .. <datan><pec_from_slave>*/
        ${I2C_INSTANCE_NAME?lower_case}SMBUSWrBuffer[xferLen++] = cmd;
        ${I2C_INSTANCE_NAME?lower_case}SMBUSWrBuffer[xferLen++] = nWrBytes;
        memcpy((void*)&${I2C_INSTANCE_NAME?lower_case}SMBUSWrBuffer[xferLen], (const void*)pWrdata, nWrBytes);
        xferLen += nWrBytes;

        if (enPEC)
        {
            /*PEC will be sent by slave and will be calculated over all the bytes in this transfer. Here master only calculates the CRC on the bytes it is transmitting. */
            crc = SMBUSCRC8Byte(crc, (address << 1));
            crc = SMBUSCRC8Buffer(crc, (uint8_t*)${I2C_INSTANCE_NAME?lower_case}SMBUSWrBuffer, xferLen);
            crc = SMBUSCRC8Byte(crc, ((address << 1) | 1));

            ${I2C_INSTANCE_NAME?lower_case}MasterObj.pec = crc;
        }

        status = ${I2C_API_PREFIX}XferSetup(address, (uint8_t*)${I2C_INSTANCE_NAME?lower_case}SMBUSWrBuffer, xferLen, (uint8_t*)${I2C_INSTANCE_NAME?lower_case}SMBUSRdBuffer, 1, false, true, enPEC == true? true : false);

        if (status == true)
        {
            ${I2C_API_PREFIX}XferStart();
        }
    }

    return status;
}

uint32_t ${I2C_API_PREFIX}SMBUSTransferCountGet(void)
{
    return ${I2C_INSTANCE_NAME?lower_case}MasterObj.readCount;
}

uint32_t ${I2C_API_PREFIX}SMBUSBufferRead(void* pBuffer)
{
    uint32_t i;
    uint32_t numBytesAvailable = ${I2C_INSTANCE_NAME?lower_case}MasterObj.readCount;

    for (i = 0; i < numBytesAvailable; i++)
    {
        ((uint8_t*)pBuffer)[i] = ${I2C_INSTANCE_NAME?lower_case}SMBUSRdBuffer[i];
    }

    return numBytesAvailable;
}

/* Must be called to check if the PEC sent by target matches with the PEC calculated by host */
bool ${I2C_API_PREFIX}SMBUSIsPECMatch(void)
{
    uint8_t lastRcvdByteIndex = ${I2C_INSTANCE_NAME?lower_case}MasterObj.readCount - 1;

    uint8_t rcvdPEC = ${I2C_INSTANCE_NAME?lower_case}SMBUSRdBuffer[lastRcvdByteIndex];

    return ${I2C_INSTANCE_NAME?lower_case}MasterObj.pec == rcvdPEC;
}

</#if>

I2C_ERROR ${I2C_API_PREFIX}ErrorGet(void)
{
    I2C_ERROR error;

    error = ${I2C_INSTANCE_NAME?lower_case}MasterObj.error;
    ${I2C_INSTANCE_NAME?lower_case}MasterObj.error = I2C_ERROR_NONE;

    return error;
}

bool ${I2C_API_PREFIX}TransferSetup(I2C_TRANSFER_SETUP* setup, uint32_t srcClkFreq )
{
    uint32_t baudValue;
    uint32_t i2cClkSpeed;
    float fBaudValue;

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

    fBaudValue = (((float)srcClkFreq / 2.0f) * ((1.0f / (float)i2cClkSpeed) - 0.000000130f)) - 1.0f;
    baudValue = (uint32_t)fBaudValue;

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

void ${I2C_API_PREFIX}TransferAbort( void )
{
    ${I2C_INSTANCE_NAME?lower_case}MasterObj.error = I2C_ERROR_NONE;

    // Reset the PLib objects and Interrupts
    ${I2C_INSTANCE_NAME?lower_case}MasterObj.state = I2C_STATE_IDLE;
    ${I2C_MASTER_IEC_REG}CLR = _${I2C_MASTER_IEC_REG}_${I2C_INSTANCE_NAME}MIE_MASK;
    ${I2C_BUS_IEC_REG}CLR = _${I2C_BUS_IEC_REG}_${I2C_BUS_COLLISION_INT_ENABLE_BIT_NAME}_MASK;

    // Disable and Enable I2C Master
    ${I2C_INSTANCE_NAME}CONCLR = _${I2C_INSTANCE_NAME}CON_ON_MASK;
    NOP;NOP;
    ${I2C_INSTANCE_NAME}CONSET = _${I2C_INSTANCE_NAME}CON_ON_MASK;
}

<#if I2C_OPERATING_MODE == "Master and Slave">
void __attribute__((used)) ${I2C_API_PREFIX}BUS_InterruptHandler(void)
{
    ${I2C_INSTANCE_NAME?lower_case}MasterObj.state = I2C_STATE_IDLE;

    ${I2C_INSTANCE_NAME?lower_case}MasterObj.error = I2C_ERROR_BUS_COLLISION;

    if (${I2C_INSTANCE_NAME?lower_case}MasterObj.callback != NULL)
    {
        uintptr_t context = ${I2C_INSTANCE_NAME?lower_case}MasterObj.context;

        ${I2C_INSTANCE_NAME?lower_case}MasterObj.callback(context);
    }
}
<#else>
void __attribute__((used)) ${I2C_API_PREFIX}BUS_InterruptHandler(void)
{
    /* Clear the bus collision error status bit */
    ${I2C_INSTANCE_NAME}STATCLR = _${I2C_INSTANCE_NAME}STAT_BCL_MASK;

    /* ACK the bus interrupt */
    ${I2C_MASTER_IFS_REG}CLR = _${I2C_MASTER_IFS_REG}_${I2C_BUS_COLLISION_INT_FLAG_BIT_NAME}_MASK;

    ${I2C_INSTANCE_NAME?lower_case}MasterObj.state = I2C_STATE_IDLE;

    ${I2C_INSTANCE_NAME?lower_case}MasterObj.error = I2C_ERROR_BUS_COLLISION;

    if ((${I2C_INSTANCE_NAME?lower_case}MasterObj.callback != NULL) && (${I2C_INSTANCE_NAME?lower_case}MasterObj.busScanInProgress == false))
    {
        uintptr_t context = ${I2C_INSTANCE_NAME?lower_case}MasterObj.context;

        ${I2C_INSTANCE_NAME?lower_case}MasterObj.callback(context);
    }
}
</#if>

void __attribute__((used)) ${I2C_INSTANCE_NAME}_MASTER_InterruptHandler(void)
{
    ${I2C_API_PREFIX}TransferSM();
}
