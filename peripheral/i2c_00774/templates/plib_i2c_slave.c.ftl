/*******************************************************************************
  Inter-Integrated Circuit (I2C) Library
  Source File

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${I2C_INSTANCE_NAME?lower_case}_slave.c

  Summary:
    I2C PLIB Slave Implementation file

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
#include "plib_${I2C_INSTANCE_NAME?lower_case}_slave.h"

// *****************************************************************************
// *****************************************************************************
// Section: Global Data
// *****************************************************************************
// *****************************************************************************
#define ${I2C_INSTANCE_NAME}_SLAVE_DATA_SETUP_TIME_CORE_TIMER_CNTS          ${I2CS_SETUP_TIME_CORE_TIMER_CNTS}
#define ${I2C_INSTANCE_NAME}_SLAVE_RISE_TIME_CORE_TIMER_CNTS                ${I2CS_RISE_TIME_CORE_TIMER_CNTS}

static I2C_SLAVE_OBJ ${I2C_INSTANCE_NAME?lower_case}Obj;

void ${I2C_INSTANCE_NAME}_Initialize(void)
{
    /* Turn off the I2C module */
    ${I2C_INSTANCE_NAME}CONCLR = _${I2C_INSTANCE_NAME}CON_ON_MASK;

    <@compress single_line=true>${I2C_INSTANCE_NAME}CON =
    (_${I2C_INSTANCE_NAME}CON_STREN_MASK
    <#if (I2CS_AHEN_DHEN_SUPPORT?? && I2CS_AHEN_DHEN_SUPPORT ==true) >
    | _${I2C_INSTANCE_NAME}CON_AHEN_MASK | _${I2C_INSTANCE_NAME}CON_DHEN_MASK </#if>
    <#if I2CS_PCIE_SUPPORT??>
    | _${I2C_INSTANCE_NAME}CON_PCIE_MASK </#if>
    <#if I2CS_A10M_SUPPORT == true>
    | _${I2C_INSTANCE_NAME}CON_A10M_MASK </#if>
    <#if I2C_SIDL == true>
    | _${I2C_INSTANCE_NAME}CON_SIDL_MASK </#if>
    <#if I2C_DISSLW == true>
    | _${I2C_INSTANCE_NAME}CON_DISSLW_MASK </#if>
    <#if I2C_SMEN == true>
    | _${I2C_INSTANCE_NAME}CON_SMEN_MASK </#if>
    <#if (I2CS_SDAHT_SUPPORT?? && I2CS_SDAHT_SUPPORT == "0x1") >
    | _${I2C_INSTANCE_NAME}CON_SDAHT_MASK </#if>);</@compress>

    ${I2C_INSTANCE_NAME}ADD = 0x${I2C_SLAVE_ADDDRESS};

    ${I2C_INSTANCE_NAME}MSK = 0x00;

    /* Clear slave interrupt flag */
    ${I2C_SLAVE_IFS_REG}CLR = _${I2C_SLAVE_IFS_REG}_${I2C_INSTANCE_NAME}SIF_MASK;

    /* Clear fault interrupt flag */
    ${I2C_BUS_IFS_REG}CLR = _${I2C_BUS_IFS_REG}_${I2C_INSTANCE_NAME}BIF_MASK;

    /* Enable the I2C Slave interrupt */
    ${I2C_SLAVE_IEC_REG}SET = _${I2C_SLAVE_IEC_REG}_${I2C_INSTANCE_NAME}SIE_MASK;

    /* Enable the I2C Bus collision interrupt */
    ${I2C_BUS_IEC_REG}SET = _${I2C_BUS_IEC_REG}_${I2C_INSTANCE_NAME}BIE_MASK;

    ${I2C_INSTANCE_NAME?lower_case}Obj.callback = NULL;

    /* Turn on the I2C module */
    ${I2C_INSTANCE_NAME}CONSET = _${I2C_INSTANCE_NAME}CON_ON_MASK;
}

static void ${I2C_INSTANCE_NAME}_RiseAndSetupTime(uint8_t sdaState)
{
    uint32_t startCount, endCount;

    if (sdaState == 0)
    {
        endCount = ${I2C_INSTANCE_NAME}_SLAVE_DATA_SETUP_TIME_CORE_TIMER_CNTS;
    }
    else
    {
        endCount = ${I2C_INSTANCE_NAME}_SLAVE_DATA_SETUP_TIME_CORE_TIMER_CNTS + ${I2C_INSTANCE_NAME}_SLAVE_RISE_TIME_CORE_TIMER_CNTS;
    }

    startCount =_CP0_GET_COUNT();

    while((_CP0_GET_COUNT()- startCount) < endCount);
}

/* I2C slave state machine */
static void ${I2C_INSTANCE_NAME}_TransferSM(void)
{
    uint32_t i2c_addr;
    uint8_t sdaValue = 0;

    /* ACK the slave interrupt */
    ${I2C_SLAVE_IFS_REG}CLR = _${I2C_SLAVE_IFS_REG}_${I2C_INSTANCE_NAME}SIF_MASK;

<#if I2CS_PCIE_SUPPORT??>
    if (${I2C_INSTANCE_NAME}STAT & _${I2C_INSTANCE_NAME}STAT_P_MASK)
    {
        if (${I2C_INSTANCE_NAME?lower_case}Obj.callback != NULL)
        {
            (void)${I2C_INSTANCE_NAME?lower_case}Obj.callback(I2C_SLAVE_TRANSFER_EVENT_STOP_BIT_RECEIVED, ${I2C_INSTANCE_NAME?lower_case}Obj.context);
        }
    }
    else if ((${I2C_INSTANCE_NAME}STAT & _${I2C_INSTANCE_NAME}STAT_D_A_MASK) == 0)
<#else>
    if ((${I2C_INSTANCE_NAME}STAT & _${I2C_INSTANCE_NAME}STAT_D_A_MASK) == 0)
</#if>
    {
        if (${I2C_INSTANCE_NAME}STAT & _${I2C_INSTANCE_NAME}STAT_RBF_MASK)
        {
            /* Received I2C address must be read out */
            i2c_addr = ${I2C_INSTANCE_NAME}RCV;
            (void)i2c_addr;

<#if I2CS_A10M_SUPPORT == true>
            if (${I2C_INSTANCE_NAME}STAT & _${I2C_INSTANCE_NAME}STAT_ADD10_MASK)
            {
                /* Notify that a address match event has occurred */
                if (${I2C_INSTANCE_NAME?lower_case}Obj.callback != NULL)
                {
<#if (I2CS_AHEN_DHEN_SUPPORT?? && I2CS_AHEN_DHEN_SUPPORT ==true) >
                    if (${I2C_INSTANCE_NAME?lower_case}Obj.callback(I2C_SLAVE_TRANSFER_EVENT_ADDR_MATCH, ${I2C_INSTANCE_NAME?lower_case}Obj.context) == true)
                    {
                        if (${I2C_INSTANCE_NAME}STAT & _${I2C_INSTANCE_NAME}STAT_R_W_MASK)
                        {
                            /* I2C master wants to read */
                            if (!(${I2C_INSTANCE_NAME}STAT & _${I2C_INSTANCE_NAME}STAT_TBF_MASK))
                            {
                                /* In the callback, slave must write to transmit register by calling I2Cx_WriteByte() */
                                (void)${I2C_INSTANCE_NAME?lower_case}Obj.callback(I2C_SLAVE_TRANSFER_EVENT_TX_READY, ${I2C_INSTANCE_NAME?lower_case}Obj.context);
                            }
                        }
                        /* Send ACK */
                        ${I2C_INSTANCE_NAME}CONCLR = _${I2C_INSTANCE_NAME}CON_ACKDT_MASK;
                    }
                    else
                    {
                        /* Send NAK */
                        ${I2C_INSTANCE_NAME}CONSET = _${I2C_INSTANCE_NAME}CON_ACKDT_MASK;
                        sdaValue = 1;
                    }
                    ${I2C_INSTANCE_NAME}_RiseAndSetupTime(sdaValue);
<#else>
                    (void)${I2C_INSTANCE_NAME?lower_case}Obj.callback(I2C_SLAVE_TRANSFER_EVENT_ADDR_MATCH, ${I2C_INSTANCE_NAME?lower_case}Obj.context);

                    if (${I2C_INSTANCE_NAME}STAT & _${I2C_INSTANCE_NAME}STAT_R_W_MASK)
                    {
                        /* I2C master wants to read */
                        if (!(${I2C_INSTANCE_NAME}STAT & _${I2C_INSTANCE_NAME}STAT_TBF_MASK))
                        {
                            /* In the callback, slave must write to transmit register by calling I2Cx_WriteByte() */
                            (void)${I2C_INSTANCE_NAME?lower_case}Obj.callback(I2C_SLAVE_TRANSFER_EVENT_TX_READY, ${I2C_INSTANCE_NAME?lower_case}Obj.context);

                            sdaValue = (${I2C_INSTANCE_NAME?lower_case}Obj.lastByteWritten & 0x80);
                            ${I2C_INSTANCE_NAME}_RiseAndSetupTime(sdaValue);
                        }
                    }
</#if>
                }
            }
<#else>
            if (${I2C_INSTANCE_NAME?lower_case}Obj.callback != NULL)
            {
<#if (I2CS_AHEN_DHEN_SUPPORT?? && I2CS_AHEN_DHEN_SUPPORT ==true) >
                /* Notify that a address match event has occurred */
                if (${I2C_INSTANCE_NAME?lower_case}Obj.callback(I2C_SLAVE_TRANSFER_EVENT_ADDR_MATCH, ${I2C_INSTANCE_NAME?lower_case}Obj.context) == true)
                {
                    if (${I2C_INSTANCE_NAME}STAT & _${I2C_INSTANCE_NAME}STAT_R_W_MASK)
                    {
                        /* I2C master wants to read */
                        if (!(${I2C_INSTANCE_NAME}STAT & _${I2C_INSTANCE_NAME}STAT_TBF_MASK))
                        {
                            /* In the callback, slave must write to transmit register by calling I2Cx_WriteByte() */
                            (void)${I2C_INSTANCE_NAME?lower_case}Obj.callback(I2C_SLAVE_TRANSFER_EVENT_TX_READY, ${I2C_INSTANCE_NAME?lower_case}Obj.context);
                        }
                    }
                    /* Send ACK */
                    ${I2C_INSTANCE_NAME}CONCLR = _${I2C_INSTANCE_NAME}CON_ACKDT_MASK;
                }
                else
                {
                    /* Send NAK */
                    ${I2C_INSTANCE_NAME}CONSET = _${I2C_INSTANCE_NAME}CON_ACKDT_MASK;
                    sdaValue = 1;
                }
                ${I2C_INSTANCE_NAME}_RiseAndSetupTime(sdaValue);
<#else>
                /* Notify that a address match event has occurred */
                ${I2C_INSTANCE_NAME?lower_case}Obj.callback(I2C_SLAVE_TRANSFER_EVENT_ADDR_MATCH, ${I2C_INSTANCE_NAME?lower_case}Obj.context);

                if (${I2C_INSTANCE_NAME}STAT & _${I2C_INSTANCE_NAME}STAT_R_W_MASK)
                {
                    /* I2C master wants to read */
                    if (!(${I2C_INSTANCE_NAME}STAT & _${I2C_INSTANCE_NAME}STAT_TBF_MASK))
                    {
                        /* In the callback, slave must write to transmit register by calling I2Cx_WriteByte() */
                        (void)${I2C_INSTANCE_NAME?lower_case}Obj.callback(I2C_SLAVE_TRANSFER_EVENT_TX_READY, ${I2C_INSTANCE_NAME?lower_case}Obj.context);

                        sdaValue = (${I2C_INSTANCE_NAME?lower_case}Obj.lastByteWritten & 0x80);
                        ${I2C_INSTANCE_NAME}_RiseAndSetupTime(sdaValue);
                    }
                }
</#if>
            }
</#if>
        /* Data written by the application; release the clock stretch */
        ${I2C_INSTANCE_NAME}CONSET = _${I2C_INSTANCE_NAME}CON_SCLREL_MASK;
        }
    }
    else
    {
        /* Master reads from slave, slave transmits */
        if (${I2C_INSTANCE_NAME}STAT & _${I2C_INSTANCE_NAME}STAT_R_W_MASK)
        {
            if ((!(${I2C_INSTANCE_NAME}STAT & _${I2C_INSTANCE_NAME}STAT_TBF_MASK)) && (!(${I2C_INSTANCE_NAME}STAT & _${I2C_INSTANCE_NAME}STAT_ACKSTAT_MASK)))
            {
                if (${I2C_INSTANCE_NAME?lower_case}Obj.callback != NULL)
                {
                    /* I2C master wants to read. In the callback, slave must write to transmit register */
                    (void)${I2C_INSTANCE_NAME?lower_case}Obj.callback(I2C_SLAVE_TRANSFER_EVENT_TX_READY, ${I2C_INSTANCE_NAME?lower_case}Obj.context);

                    sdaValue = (${I2C_INSTANCE_NAME?lower_case}Obj.lastByteWritten & 0x80);
                }

                ${I2C_INSTANCE_NAME}_RiseAndSetupTime(sdaValue);

                /* Data written by the application; release the clock stretch */
                ${I2C_INSTANCE_NAME}CONSET = _${I2C_INSTANCE_NAME}CON_SCLREL_MASK;
            }
        }
        /* Master writes to slave, slave receives */
        else
        {
            if (${I2C_INSTANCE_NAME}STAT & _${I2C_INSTANCE_NAME}STAT_RBF_MASK)
            {
                if (${I2C_INSTANCE_NAME?lower_case}Obj.callback != NULL)
                {
<#if (I2CS_AHEN_DHEN_SUPPORT?? && I2CS_AHEN_DHEN_SUPPORT ==true) >
                    /* I2C master wants to write. In the callback, slave must read data by calling I2Cx_ReadByte()  */
                    if (${I2C_INSTANCE_NAME?lower_case}Obj.callback(I2C_SLAVE_TRANSFER_EVENT_RX_READY, ${I2C_INSTANCE_NAME?lower_case}Obj.context) == true)
                    {
                        /* Send ACK */
                        ${I2C_INSTANCE_NAME}CONCLR = _${I2C_INSTANCE_NAME}CON_ACKDT_MASK;
                    }
                    else
                    {
                        /* Send NAK */
                        ${I2C_INSTANCE_NAME}CONSET = _${I2C_INSTANCE_NAME}CON_ACKDT_MASK;
                        sdaValue = 1;
                    }

                    ${I2C_INSTANCE_NAME}_RiseAndSetupTime(sdaValue);
<#else>
                    /* I2C master wants to write. In the callback, slave must read data by calling I2Cx_ReadByte()  */
                    (void)${I2C_INSTANCE_NAME?lower_case}Obj.callback(I2C_SLAVE_TRANSFER_EVENT_RX_READY, ${I2C_INSTANCE_NAME?lower_case}Obj.context);
</#if>
                }
                /* Data read by the application; release the clock stretch */
                ${I2C_INSTANCE_NAME}CONSET = _${I2C_INSTANCE_NAME}CON_SCLREL_MASK;
            }
        }
    }
}

void ${I2C_INSTANCE_NAME}_CallbackRegister(I2C_SLAVE_CALLBACK callback, uintptr_t contextHandle)
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
    if(${I2C_INSTANCE_NAME}STAT & _${I2C_INSTANCE_NAME}STAT_S_MASK)
    {
        return true;
    }
    else
    {
        return false;
    }
}

uint8_t ${I2C_INSTANCE_NAME}_ReadByte(void)
{
    return ${I2C_INSTANCE_NAME}RCV;
}

void ${I2C_INSTANCE_NAME}_WriteByte(uint8_t wrByte)
{
    if (!(${I2C_INSTANCE_NAME}STAT & _${I2C_INSTANCE_NAME}STAT_TBF_MASK))
    {
        ${I2C_INSTANCE_NAME}TRN = wrByte;
        ${I2C_INSTANCE_NAME?lower_case}Obj.lastByteWritten = wrByte;
    }
}

I2C_SLAVE_TRANSFER_DIR ${I2C_INSTANCE_NAME}_TransferDirGet(void)
{
    return (${I2C_INSTANCE_NAME}STAT & _${I2C_INSTANCE_NAME}STAT_R_W_MASK) ? I2C_SLAVE_TRANSFER_DIR_READ : I2C_SLAVE_TRANSFER_DIR_WRITE;
}

I2C_SLAVE_ACK_STATUS ${I2C_INSTANCE_NAME}_LastByteAckStatusGet(void)
{
    return (${I2C_INSTANCE_NAME}STAT & _${I2C_INSTANCE_NAME}STAT_ACKSTAT_MASK) ? I2C_SLAVE_ACK_STATUS_RECEIVED_NAK : I2C_SLAVE_ACK_STATUS_RECEIVED_ACK;
}

I2C_SLAVE_ERROR ${I2C_INSTANCE_NAME}_ErrorGet(void)
{
    I2C_SLAVE_ERROR error;

    error = ${I2C_INSTANCE_NAME?lower_case}Obj.error;
    ${I2C_INSTANCE_NAME?lower_case}Obj.error = I2C_SLAVE_ERROR_NONE;

    return error;
}

static void ${I2C_INSTANCE_NAME}_BUS_InterruptHandler(void)
{
    /* Clear the bus collision error status bit */
    ${I2C_INSTANCE_NAME}STATCLR = _${I2C_INSTANCE_NAME}STAT_BCL_MASK;

    /* ACK the bus interrupt */
    ${I2C_SLAVE_IFS_REG}CLR = _${I2C_SLAVE_IFS_REG}_${I2C_INSTANCE_NAME}BIF_MASK;

    ${I2C_INSTANCE_NAME?lower_case}Obj.error = I2C_SLAVE_ERROR_BUS_COLLISION;

    if (${I2C_INSTANCE_NAME?lower_case}Obj.callback != NULL)
    {
        ${I2C_INSTANCE_NAME?lower_case}Obj.callback(I2C_SLAVE_TRANSFER_EVENT_ERROR, ${I2C_INSTANCE_NAME?lower_case}Obj.context);
    }
}

static void ${I2C_INSTANCE_NAME}_SLAVE_InterruptHandler(void)
{
    ${I2C_INSTANCE_NAME}_TransferSM();
}

void I2C_${I2C_INSTANCE_NUM}_InterruptHandler(void)
{
    if ((${I2C_BUS_IFS_REG} & _${I2C_BUS_IFS_REG}_${I2C_INSTANCE_NAME}BIF_MASK) && (${I2C_BUS_IEC_REG} & _${I2C_BUS_IEC_REG}_${I2C_INSTANCE_NAME}BIE_MASK))
    {
        ${I2C_INSTANCE_NAME}_BUS_InterruptHandler();
    }
    else if ((${I2C_SLAVE_IFS_REG} & _${I2C_SLAVE_IFS_REG}_${I2C_INSTANCE_NAME}SIF_MASK) && (${I2C_SLAVE_IEC_REG} & _${I2C_SLAVE_IEC_REG}_${I2C_INSTANCE_NAME}SIE_MASK))
    {
        ${I2C_INSTANCE_NAME}_SLAVE_InterruptHandler();
    }
}