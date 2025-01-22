<#assign smbenOptions = ["DISABLED","SMBUS_2_0","SMBUS_3_0"]>
<#assign sdhatOptions = ["100NS","300NS"]>
/*******************************************************************************
  ${moduleName?lower_case} PLIB
 
  Company:
    Microchip Technology Inc.
 
  File Name:
    plib_${moduleName?lower_case}.c
 
  Summary:
    ${moduleName?lower_case} PLIB Source File
 
  Description:
    None
 
*******************************************************************************/
 
/*******************************************************************************
* Copyright (C) 2024 Microchip Technology Inc. and its subsidiaries.
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

// Section: Included Files

#include "device.h"
#include "plib_${moduleName?lower_case}_client.h"
#include "interrupts.h"

// Section: Macro Definitions

//I2CxCON SMBEN options
<#list smbenOptions as options>
<#if options != "">
#define I2C${instance}CON1_SMBEN_${options}          ((uint32_t)(_I2C${instance}CON1_SMBEN_MASK & ((uint32_t)(${options_index}) << _I2C${instance}CON1_SMBEN_POSITION))) 
</#if>
</#list>

//I2CxCON SDHAT options
<#list sdhatOptions as options>
<#if options != "">
#define I2C${instance}CON1_SDAHT_${options}          ((uint32_t)(_I2C${instance}CON1_SDAHT_MASK & ((uint32_t)(${options_index}) << _I2C${instance}CON1_SDAHT_POSITION))) 
</#if>
</#list>

// Section: Global Data

volatile static I2C_CLIENT_OBJ ${moduleName?lower_case}Obj;
void ${i2cErrorInterruptHandler}(void);
void ${i2cCommonInterruptHandler}(void);

void ${moduleName}_Initialize(void)
{
    _${moduleName}IE = 0U;
    _${moduleName}EIE = 0U;

    I2C${instance}CON1 = (_I2C${instance}CON1_PCIE_MASK
                |_I2C${instance}CON1_SCIE_MASK<#if ENABLE_CLOCK_STRETCHING==true>
                |_I2C${instance}CON1_STREN_MASK</#if><#if I2CS_AHEN_SUPPORT==true>
                |_I2C${instance}CON1_AHEN_MASK</#if><#if I2CS_DHEN_SUPPORT==true>
                |_I2C${instance}CON1_DHEN_MASK</#if><#if ENABLE_10BIT_ADDRESS==true> 
                |_I2C${instance}CON1_A10M_MASK</#if><#if I2C_CON1__DISSLW?number != 0>
                |_I2C${instance}CON1_DISSLW_MASK</#if>
                |I2C${instance}CON1_SMBEN_${smbenOptions[.vars["I2C_CON1__SMBEN"]?number]}
                |I2C${instance}CON1_SDAHT_${sdhatOptions[.vars["I2C_CON1__SDAHT"]?number]});
                
    I2C${instance}INTC = (_I2C${instance}INTC_BCLIE_MASK
                |_I2C${instance}INTC_CADDRIE_MASK
                |_I2C${instance}INTC_CDTXIE_MASK
                |_I2C${instance}INTC_CDRXIE_MASK
                |_I2C${instance}INTC_CLTIE_MASK);

    I2C${instance}ADD = 0x${CLIENT_ADDDRESS}UL;
    I2C${instance}MSK = 0x${CLIENT_MASK}UL;

    /* Clear client interrupt flag */
    _I2C${instance}IF = 0U;

    /* Clear fault interrupt flag */
    _I2C${instance}EIF = 0U;

    /* Enable the I2C Client interrupt */
    _I2C${instance}IE = 1U;

    /* Enable the I2C Bus collision interrupt */
    _I2C${instance}EIE = 1U;

    ${moduleName?lower_case}Obj.callback = NULL;

    /* Turn on the I2C module */
    ${moduleName}CON1bits.ON = 1U;
}

void ${moduleName}_Deinitialize(void)
{
    /* Turn on the I2C module */
    ${moduleName}CON1bits.ON = 0U;
    
    /* Enable the I2C Bus collision interrupt */
    _I2C${instance}EIE = 0U;
    /* Enable the I2C Client interrupt */
    _I2C${instance}IE = 0U;
    
    I2C${instance}CON1 = (_I2C${instance}CON1_SCLREL_MASK);
    I2C${instance}INTC = 0x0UL;  

    I2C${instance}ADD = 0x0UL;
    I2C${instance}MSK = 0x0UL;

    ${moduleName?lower_case}Obj.callback = NULL;  
}

/* I2C client state machine */
static void ${moduleName}_TransferSM(void)
{
    uint32_t i2c_addr;
    uintptr_t context = ${moduleName?lower_case}Obj.context;

    /* ACK the client interrupt */
    IFS2bits.${moduleName}IF = 0U;

    if (I2C${instance}STAT1bits.I2COV != 0U)
    {
        if (${moduleName?lower_case}Obj.callback != NULL)
        {
            (void)${moduleName?lower_case}Obj.callback(I2C_CLIENT_TRANSFER_EVENT_STOP_BIT_RECEIVED, context);
        }
    }
    else if (I2C${instance}STAT1bits.D_A == 0U)
    {
        if (I2C${instance}STAT1bits.RBF != 0U)
        {
            /* Received I2C address must be read out */
            i2c_addr = I2C${instance}RCV;
            (void)i2c_addr;
<#if ENABLE_10BIT_ADDRESS == true>
            if(I2C${instance}STAT1bits.ADD10 != 0U)
            {
                /* Notify that a address match event has occurred */
                if (${moduleName?lower_case}Obj.callback != NULL)
                {
                    if (${moduleName?lower_case}Obj.callback(I2C_CLIENT_TRANSFER_EVENT_ADDR_MATCH, context) == true)
                    {
                        if (I2C${instance}STAT1bits.R_W != 0U)
                        {
                            /* I2C master wants to read */
                            if (I2C${instance}STAT1bits.TBF == 0U)
                            {
                                /* In the callback, client must write to transmit register by calling I2Cx_WriteByte() */
                                (void)${moduleName?lower_case}Obj.callback(I2C_CLIENT_TRANSFER_EVENT_TX_READY, context);
                            }
                        }
                        /* Send ACK */
                        I2C${instance}CON1bits.ACKDT = 0U;
                    }
                    else
                    {
                        /* Send NAK */
                        I2C${instance}CON1bits.ACKDT = 1U;
                    }
                }
            }
<#else>
            /* Notify that a address match event has occurred */
            if (${moduleName?lower_case}Obj.callback != NULL)
            {
                if (${moduleName?lower_case}Obj.callback(I2C_CLIENT_TRANSFER_EVENT_ADDR_MATCH, context) == true)
                {
                    if (I2C${instance}STAT1bits.R_W != 0U)
                    {
                        /* I2C master wants to read */
                        if (I2C${instance}STAT1bits.TBF == 0U)
                        {
                            /* In the callback, client must write to transmit register by calling I2Cx_WriteByte() */
                            (void)${moduleName?lower_case}Obj.callback(I2C_CLIENT_TRANSFER_EVENT_TX_READY, context);
                        }
                    }
                    /* Send ACK */
                    I2C${instance}CON1bits.ACKDT = 0U;
                }
                else
                {
                    /* Send NAK */
                    I2C${instance}CON1bits.ACKDT = 1U;
                }
            }
</#if>
<#if I2CS_AHEN_SUPPORT==true>
        /* Data written by the application release the clock stretch if DHEN is enabled*/
        I2C${instance}CON1bits.SCLREL = 1U;
</#if>
        }
    }
    else
    {
        /* Master reads from client, client transmits */
        if (I2C${instance}STAT1bits.R_W != 0U)
        {
            if (((I2C${instance}STAT1 & (_I2C${instance}STAT1_TBF_MASK | _I2C${instance}STAT1_ACKSTAT_MASK))  == 0U))
            {
                if (${moduleName?lower_case}Obj.callback != NULL)
                {
                    /* I2C master wants to read. In the callback, client must write to transmit register */
                    (void)${moduleName?lower_case}Obj.callback(I2C_CLIENT_TRANSFER_EVENT_TX_READY, context);

                }
<#if I2CS_DHEN_SUPPORT==true>
                /* Data written by the application; release the clock stretch if DHEN is enabled */
                I2C${instance}CON1bits.SCLREL = 1U;
</#if>
            }
        }
        /* Master writes to client, client receives */
        else
        {
            if ((I2C${instance}STAT1 & _I2C${instance}STAT1_RBF_MASK) != 0U)
            {
                if (${moduleName?lower_case}Obj.callback != NULL)
                {
                    /* I2C master wants to write. In the callback, client must read data by calling I2Cx_ReadByte()  */
                    if (${moduleName?lower_case}Obj.callback(I2C_CLIENT_TRANSFER_EVENT_RX_READY, context) == true)
                    {
                        /* Send ACK */
                        I2C${instance}CON1bits.ACKDT = 0U;
                    }
                    else
                    {
                        /* Send NAK */
                        I2C${instance}CON1bits.ACKDT = 1U;
                    }

                }
<#if I2CS_DHEN_SUPPORT==true>
                /* Data read by the application; release the clock stretch if DHEN is enabled*/
                I2C${instance}CON1bits.SCLREL = 1U;
</#if>
            }
        }
    }
    // Release clock stretch on 9th bit
    if(I2C${instance}CON1bits.STREN == 1U || I2C${instance}CON1bits.SCLREL == 0U)
    {
        // Clock stretch release
        I2C${instance}CON1bits.SCLREL = 1U;
    }
}

void ${moduleName}_CallbackRegister(I2C_CLIENT_CALLBACK callback, uintptr_t contextHandle)
{
    if (callback != NULL)
    {
        ${moduleName?lower_case}Obj.callback = callback;
        ${moduleName?lower_case}Obj.context = contextHandle;
    }
}

bool ${moduleName}_IsBusy(void)
{
    return ((I2C${instance}STAT1 & _I2C${instance}STAT1_S_MASK) != 0U);
}

uint8_t ${moduleName}_ReadByte(void)
{
    return (uint8_t)${moduleName}RCV;
}

void ${moduleName}_WriteByte(uint8_t wrByte)
{
    if ((I2C${instance}STAT1 & _I2C${instance}STAT1_TBF_MASK)  == 0U)
    {
        I2C${instance}TRN = wrByte;
        ${moduleName?lower_case}Obj.lastByteWritten = wrByte;
    }
}

I2C_CLIENT_TRANSFER_DIR ${moduleName}_TransferDirGet(void)
{
    return ((I2C${instance}STAT1 & _I2C${instance}STAT1_R_W_MASK) != 0U) ? I2C_CLIENT_TRANSFER_DIR_READ : I2C_CLIENT_TRANSFER_DIR_WRITE;
}

I2C_CLIENT_ACK_STATUS ${moduleName}_LastByteAckStatusGet(void)
{
    return ((I2C${instance}STAT1 & _I2C${instance}STAT1_ACKSTAT_MASK) != 0U) ? I2C_CLIENT_ACK_STATUS_RECEIVED_NAK : I2C_CLIENT_ACK_STATUS_RECEIVED_ACK;
}

I2C_CLIENT_ERROR ${moduleName}_ErrorGet(void)
{
    I2C_CLIENT_ERROR error;

    error = ${moduleName?lower_case}Obj.error;
    ${moduleName?lower_case}Obj.error = I2C_CLIENT_ERROR_NONE;

    return error;
}

void __attribute__((used)) ${i2cErrorInterruptHandler}(void)
{
    /* Clear the bus collision error status bit */
    I2C${instance}STAT1bits.BCL = 0U;

    /* ACK the bus interrupt */
    _I2C${instance}EIF = 0U;

    ${moduleName?lower_case}Obj.error = I2C_CLIENT_ERROR_BUS_COLLISION;

    if (${moduleName?lower_case}Obj.callback != NULL)
    {
        uintptr_t context = ${moduleName?lower_case}Obj.context;

        (void) ${moduleName?lower_case}Obj.callback(I2C_CLIENT_TRANSFER_EVENT_ERROR, context);
    }
}

void __attribute__((used)) ${i2cCommonInterruptHandler}(void)
{
    ${moduleName}_TransferSM();
}
