/*******************************************************************************
  Serial Communication Interface Inter-Integrated Circuit (SERCOM I2C) Library
  Source File

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${SERCOM_INSTANCE_NAME?lower_case}_i2c.c

  Summary:
    SERCOM I2C PLIB Implementation file

  Description:
    This file defines the interface to the SERCOM I2C peripheral library.
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

<#if core.CoreSysIntFile == true>
#include "interrupts.h"
</#if>
#include "plib_${SERCOM_INSTANCE_NAME?lower_case}_i2c_master.h"


// *****************************************************************************
// *****************************************************************************
// Section: Global Data
// *****************************************************************************
// *****************************************************************************

<#assign I2C_PLIB = "SERCOM_INSTANCE_NAME">
<#assign I2C_PLIB_CLOCK_FREQUENCY = "core." + I2C_PLIB?eval + "_CORE_CLOCK_FREQUENCY">

#define ${SERCOM_INSTANCE_NAME}_I2CM_SPEED_HZ           ${I2C_CLOCK_SPEED_HZ}

/* ${SERCOM_INSTANCE_NAME} I2C baud value */
#define ${SERCOM_INSTANCE_NAME}_I2CM_BAUD_VALUE         (0x${I2CM_BAUD?upper_case}U)

<#if (I2C_ADDR_TENBITEN?? && I2C_ADDR_TENBITEN = true)>
#define RIGHT_ALIGNED (8U)
</#if>

volatile static SERCOM_I2C_OBJ ${SERCOM_INSTANCE_NAME?lower_case}I2CObj;

// *****************************************************************************
// *****************************************************************************
// Section: ${SERCOM_INSTANCE_NAME} I2C Implementation
// *****************************************************************************
// *****************************************************************************
// *****************************************************************************

void ${SERCOM_INSTANCE_NAME}_I2C_Initialize(void)
{
    /* Reset the module */
    ${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_CTRLA = SERCOM_I2CM_CTRLA_SWRST_Msk ;

    /* Wait for synchronization */
<#if SERCOM_SYNCBUSY = false>
    while((${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_STATUS & (uint16_t)SERCOM_I2CM_STATUS_SYNCBUSY_Msk) == (uint16_t)SERCOM_I2CM_STATUS_SYNCBUSY_Msk)
    {
        /* Do nothing */
    }
<#else>
    while((${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_SYNCBUSY) != 0U)
    {
        /* Do nothing */
    }
</#if>

    /* Enable smart mode */
    ${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_CTRLB = SERCOM_I2CM_CTRLB_SMEN_Msk;

    /* Wait for synchronization */
<#if SERCOM_SYNCBUSY = false>
    while((${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_STATUS & (uint16_t)SERCOM_I2CM_STATUS_SYNCBUSY_Msk) == (uint16_t)SERCOM_I2CM_STATUS_SYNCBUSY_Msk)
    {
        /* Do nothing */
    }
<#else>
    while((${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_SYNCBUSY) != 0U)
    {
        /* Do nothing */
    }
</#if>

    /* Baud rate - Master Baud Rate*/
    ${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_BAUD = ${SERCOM_INSTANCE_NAME}_I2CM_BAUD_VALUE;

    /* Set Operation Mode (Master), SDA Hold time, run in stand by and i2c master enable */
    <@compress single_line=true>${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_CTRLA =
    SERCOM_I2CM_CTRLA_MODE_${I2C_MASTER_MODE}
    | SERCOM_I2CM_CTRLA_SDAHOLD_${I2C_SDAHOLD_TIME}
    <#if I2CM_MODE??> | SERCOM_I2CM_CTRLA_SPEED_${I2CM_MODE}  </#if>
    <#if I2C_SCLSM??> | SERCOM_I2CM_CTRLA_SCLSM(${I2C_SCLSM}UL) </#if>
    | SERCOM_I2CM_CTRLA_ENABLE_Msk
    ${I2C_RUNSTDBY?then(' | SERCOM_I2CM_CTRLA_RUNSTDBY_Msk','')}
    <#if I2C_SLEWRATE??> | SERCOM_I2CM_CTRLA_SLEWRATE(SERCOM_I2CM_CTRLA_SLEWRATE_${I2C_SLEWRATE}_Val)</#if>;</@compress>

    /* Wait for synchronization */
<#if SERCOM_SYNCBUSY = false>
    while((${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_STATUS & (uint16_t)SERCOM_I2CM_STATUS_SYNCBUSY_Msk) == (uint16_t)SERCOM_I2CM_STATUS_SYNCBUSY_Msk)
    {
        /* Do nothing */
    }
<#else>
    while((${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_SYNCBUSY) != 0U)
    {
        /* Do nothing */
    }
</#if>

    /* Initial Bus State: IDLE */
    ${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_STATUS = (uint16_t)SERCOM_I2CM_STATUS_BUSSTATE(0x01UL);

    /* Wait for synchronization */
<#if SERCOM_SYNCBUSY = false>
    while((${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_STATUS & (uint16_t)SERCOM_I2CM_STATUS_SYNCBUSY_Msk) == (uint16_t)SERCOM_I2CM_STATUS_SYNCBUSY_Msk)
    {
        /* Do nothing */
    }
<#else>
    while((${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_SYNCBUSY) != 0U)
    {
        /* Do nothing */
    }
</#if>

    /* Initialize the ${SERCOM_INSTANCE_NAME} PLib Object */
    ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.error = SERCOM_I2C_ERROR_NONE;
    ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.state = SERCOM_I2C_STATE_IDLE;
<#if (I2CM_MODE?? && I2CM_MODE = "HIGH_SPEED_MODE")>
    ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.masterCode = (uint8_t)(0x08U | ${I2C_MASTER_CODE}U);
</#if>

    /* Enable all Interrupts */
    ${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_INTENSET = (uint8_t)SERCOM_I2CM_INTENSET_Msk;
}

static bool ${SERCOM_INSTANCE_NAME}_I2C_CalculateBaudValue(uint32_t srcClkFreq, uint32_t i2cClkSpeed, uint32_t* baudVal)
{
    uint32_t baudValue = 0U;
    float fSrcClkFreq = (float)srcClkFreq;
    float fI2cClkSpeed = (float)i2cClkSpeed;
    float fBaudValue = 0.0f;

    /* Reference clock frequency must be atleast two times the baud rate */
    if (srcClkFreq < (2U * i2cClkSpeed))
    {
        return false;
    }

<#if I2CM_MODE??>
<#if I2CM_MODE = "HIGH_SPEED_MODE">
    if (i2cClkSpeed > 1000000U)
    {
        /* HS mode baud calculation */
        fBaudValue = (fSrcClkFreq / fI2cClkSpeed) - 2.0f;
        baudValue = (uint32_t)fBaudValue;
    }
    else
    {
        /* Standard, FM and FM+ baud calculation */
        fBaudValue = (fSrcClkFreq / fI2cClkSpeed) - ((fSrcClkFreq * (${I2CM_TRISE}.0f / 1000000000.0f)) + 10.0f);
        baudValue = (uint32_t)fBaudValue;
    }
<#else>
    if (i2cClkSpeed <= 1000000U)
    {
        /* Standard, FM and FM+ baud calculation */
        fBaudValue = (fSrcClkFreq / fI2cClkSpeed) - ((fSrcClkFreq * (${I2CM_TRISE}.0f / 1000000000.0f)) + 10.0f);
        baudValue = (uint32_t)fBaudValue;
    }
    else
    {
        return false;
    }
</#if>
    if (i2cClkSpeed <= 400000U)
    {
        /* For I2C clock speed upto 400 kHz, the value of BAUD<7:0> determines both SCL_L and SCL_H with SCL_L = SCL_H */
        if (baudValue > (0xFFU * 2U))
        {
            /* Set baud rate to the minimum possible value */
            baudValue = 0xFFU;
        }
        else if (baudValue <= 1U)
        {
            /* Baud value cannot be 0. Set baud rate to maximum possible value */
            baudValue = 1U;
        }
        else
        {
            baudValue /= 2U;
        }
    }
    else
    {
        /* To maintain the ratio of SCL_L:SCL_H to 2:1, the max value of BAUD_LOW<15:8>:BAUD<7:0> can be 0xFF:0x7F. Hence BAUD_LOW + BAUD can not exceed 255+127 = 382 */
        if (baudValue >= 382U)
        {
            /* Set baud rate to the minimum possible value while maintaining SCL_L:SCL_H to 2:1 */
            baudValue = (0xFFUL << 8U) | (0x7FU);
        }
        else if (baudValue <= 3U)
        {
            /* Baud value cannot be 0. Set baud rate to maximum possible value while maintaining SCL_L:SCL_H to 2:1 */
            baudValue = (2UL << 8U) | 1U;
        }
        else
        {
            /* For Fm+ mode, I2C SCL_L:SCL_H to 2:1 */
            baudValue  = ((((baudValue * 2U)/3U) << 8U) | (baudValue/3U));
        }
    }
<#else>
    if (i2cClkSpeed <= 400000U)
    {
        /* Standard, FM and FM+ baud calculation */
        fBaudValue = (fSrcClkFreq / fI2cClkSpeed) - ((fSrcClkFreq * (${I2CM_TRISE}.0f / 1000000000.0f)) + 10.0f);
        baudValue = (uint32_t)fBaudValue;

        /* For I2C clock speed upto 400 KHz, the value of BAUD<7:0> determines both SCL_L and SCL_H with SCL_L = SCL_H */
        if (baudValue > (0xFFU * 2U))
        {
            /* Set baud rate to the minimum possible value */
            baudValue = 0xFFU;
        }
        else if (baudValue <= 1U)
        {
            /* Baud value cannot be 0. Set baud rate to maximum possible value */
            baudValue = 1U;
        }
        else
        {
            baudValue /= 2U;
        }
    }
    else
    {
        return false;
    }
</#if>
    *baudVal = baudValue;
    return true;
}

bool ${SERCOM_INSTANCE_NAME}_I2C_TransferSetup(SERCOM_I2C_TRANSFER_SETUP* setup, uint32_t srcClkFreq )
{
    uint32_t baudValue;
    uint32_t i2cClkSpeed;
<#if I2CM_MODE??>
    uint32_t i2cSpeedMode = 0;
<#if I2CM_MODE = "HIGH_SPEED_MODE">
    uint32_t hsbaudValue;
</#if>
</#if>

    if (setup == NULL)
    {
        return false;
    }

    i2cClkSpeed = setup->clkSpeed;

    if( srcClkFreq == 0U)
    {
        srcClkFreq = ${I2C_PLIB_CLOCK_FREQUENCY?eval}UL;
    }

<#if I2CM_MODE?? && I2CM_MODE = "HIGH_SPEED_MODE">
    if (i2cClkSpeed > 1000000U)
    {
        /* HS mode requires baud values for both 400kHz and HS frequency. First calculate baud for 400kHz */
        if (${SERCOM_INSTANCE_NAME}_I2C_CalculateBaudValue(srcClkFreq, 400000, &baudValue) == false)
        {
            return false;
        }
    }
    else
    {
        if (${SERCOM_INSTANCE_NAME}_I2C_CalculateBaudValue(srcClkFreq, i2cClkSpeed, &baudValue) == false)
        {
            return false;
        }
    }
<#else>
    if (${SERCOM_INSTANCE_NAME}_I2C_CalculateBaudValue(srcClkFreq, i2cClkSpeed, &baudValue) == false)
    {
        return false;
    }
</#if>

<#if I2CM_MODE??>
<#if I2CM_MODE = "HIGH_SPEED_MODE">
    if (i2cClkSpeed > 1000000U)
    {
        /* Now calculate HS baud value */
        if (${SERCOM_INSTANCE_NAME}_I2C_CalculateBaudValue(srcClkFreq, i2cClkSpeed, &hsbaudValue) == false)
        {
            return false;
        }
        else
        {
            baudValue |= (hsbaudValue << 16U);
            i2cSpeedMode = 2U;
        }
    }
    else if (i2cClkSpeed > 400000U)
    {
        i2cSpeedMode = 1U;
    }
    else
    {
        /* Do nothing */
    }
<#else>
    if (i2cClkSpeed > 400000U)
    {
        i2cSpeedMode = 1U;
    }
</#if>
</#if>

    /* Disable the I2C before changing the I2C clock speed */
    ${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_CTRLA &= ~SERCOM_I2CM_CTRLA_ENABLE_Msk;

    /* Wait for synchronization */
<#if SERCOM_SYNCBUSY = false>
    while((${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_STATUS & (uint16_t)SERCOM_I2CM_STATUS_SYNCBUSY_Msk) == (uint16_t)SERCOM_I2CM_STATUS_SYNCBUSY_Msk)
    {
        /* Do nothing */
    }
<#else>
    while((${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_SYNCBUSY) != 0U)
    {
        /* Do nothing */
    }
</#if>


    /* Baud rate - Master Baud Rate*/
<#if I2CM_BAUD_SIZE == 2>
    ${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_BAUD = (uint16_t)baudValue;
<#else>
    ${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_BAUD = baudValue;
</#if>

<#if I2CM_MODE??>
    ${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_CTRLA  = ((${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_CTRLA & ~SERCOM_I2CM_CTRLA_SPEED_Msk) | (SERCOM_I2CM_CTRLA_SPEED(i2cSpeedMode)));
</#if>

    /* Re-enable the I2C module */
    ${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_CTRLA |= SERCOM_I2CM_CTRLA_ENABLE_Msk;

    /* Wait for synchronization */
<#if SERCOM_SYNCBUSY = false>
    while((${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_STATUS & (uint16_t)SERCOM_I2CM_STATUS_SYNCBUSY_Msk) == (uint16_t)SERCOM_I2CM_STATUS_SYNCBUSY_Msk)
    {
        /* Do nothing */
    }
<#else>
    while((${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_SYNCBUSY) != 0U)
    {
        /* Do nothing */
    }
</#if>


    /* Since the I2C module was disabled, re-initialize the bus state to IDLE */
    ${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_STATUS = (uint16_t)SERCOM_I2CM_STATUS_BUSSTATE(0x01UL);

    /* Wait for synchronization */
<#if SERCOM_SYNCBUSY = false>
    while((${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_STATUS & (uint16_t)SERCOM_I2CM_STATUS_SYNCBUSY_Msk) == (uint16_t)SERCOM_I2CM_STATUS_SYNCBUSY_Msk)
    {
        /* Do nothing */
    }
<#else>
    while((${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_SYNCBUSY) != 0U)
    {
        /* Do nothing */
    }
</#if>

    return true;
}

void ${SERCOM_INSTANCE_NAME}_I2C_CallbackRegister(SERCOM_I2C_CALLBACK callback, uintptr_t contextHandle)
{
    ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.callback = callback;

    ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.context  = contextHandle;
}

<#if (I2CM_MODE?? && I2CM_MODE = "HIGH_SPEED_MODE")>
<#if (I2C_ADDR_TENBITEN?? && I2C_ADDR_TENBITEN = true)>

static void ${SERCOM_INSTANCE_NAME}_I2C_SendAddress(uint16_t address, bool dir)
{
    bool isTenBitAddress = false;
    bool isHighSpeed = false;
    bool transferDir = dir;
    bool txMasterCode = ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.txMasterCode;

    /* Check for 10-bit address */
    if(address > 0x007FU)
    {
        if ((${SERCOM_INSTANCE_NAME?lower_case}I2CObj.isHighSpeed == true) && (txMasterCode == true))
        {
            /* write: <0000-1nnn> <Sr> <1111-10xxW> <xxxx-xxxx> <write-data> <P>
               read: <0000-1nnn> <Sr> <1111-10xxW> <xxxx-xxxx> <Sr> <1111-10xxR> <read-data> <P>
            */

            /* Next state will be to transmit slave address with HS mode enabled */
            ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.state = SERCOM_I2C_STATE_TRANSFER_ADDR_HS;
        }
        else
        {
            isTenBitAddress = true;
            transferDir = false;

            /* If operation is I2C read */
            if(dir)
            {
                /* <Sr> <1111-10xxW> <xxxx-xxxx> <Sr> <1111-10xxR> <read-data> <P> */

                /* Next state will be to send slave address followed by Sr */
                ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.state = SERCOM_I2C_STATE_ADDR_SEND;

                if (${SERCOM_INSTANCE_NAME?lower_case}I2CObj.isHighSpeed == true)
                {
                    /* We are in HS mode and Master code is already transmitted out */
                    isHighSpeed = true;
                }
            }
            else
            {
                /* <Sr> <1111-10xxW> <xxxx-xxxx> <write-data> <P>  */

                ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.state = SERCOM_I2C_STATE_TRANSFER_WRITE;

                if (${SERCOM_INSTANCE_NAME?lower_case}I2CObj.isHighSpeed == true)
                {
                    /* We are in HS mode and Master code is already transmitted out */
                    isHighSpeed = true;
                }
            }
        }
    }
    else
    {
        if ((${SERCOM_INSTANCE_NAME?lower_case}I2CObj.isHighSpeed == true) && (txMasterCode == true))
        {
            /* write: <0000-1nnn> <Sr> <xxxx-xxxW> <write-data> <P>
               read: <0000-1nnn> <Sr> <xxxx-xxxR> <read-data> <P>
            */

            /* Next state will be to transmit slave address with HS mode enabled */
            ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.state = SERCOM_I2C_STATE_TRANSFER_ADDR_HS;
        }
        else
        {
            /* If operation is I2C read */
            if(dir)
            {
                /* <xxxx-xxxR> <read-data> <P> */

                /* Next state will be to read data */
                ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.state = SERCOM_I2C_STATE_TRANSFER_READ;

                if (${SERCOM_INSTANCE_NAME?lower_case}I2CObj.isHighSpeed == true)
                {
                    /* We are in HS mode and Master code is already transmitted out */
                    isHighSpeed = true;
                }
            }
            else
            {
                /* <xxxx-xxxW> <write-data> <P> */

                /* Next state will be to write data */
                ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.state = SERCOM_I2C_STATE_TRANSFER_WRITE;

                if (${SERCOM_INSTANCE_NAME?lower_case}I2CObj.isHighSpeed == true)
                {
                    /* We are in HS mode and Master code is already transmitted out */
                    isHighSpeed = true;
                }
            }
        }
    }

    if (txMasterCode == true)
    {
        /* Transmit masterCode */
        ${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_ADDR = ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.masterCode;
    }
    else
    {
        ${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_ADDR = SERCOM_I2CM_ADDR_TENBITEN(isTenBitAddress ? 1UL : 0UL) | SERCOM_I2CM_ADDR_HS(isHighSpeed ? 1UL : 0UL) | ((uint32_t)address << 1U) | (transferDir ? 1UL : 0UL);
    }

    /* Wait for synchronization */
<#if SERCOM_SYNCBUSY = false>
    while((${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_STATUS & (uint16_t)SERCOM_I2CM_STATUS_SYNCBUSY_Msk) == (uint16_t)SERCOM_I2CM_STATUS_SYNCBUSY_Msk)
    {
        /* Do nothing */
    }
<#else>
    while((${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_SYNCBUSY) != 0U)
    {
        /* Do nothing */
    }
</#if>

}
<#else>

static void ${SERCOM_INSTANCE_NAME}_I2C_SendAddress(uint16_t address, bool dir)
{
    bool isHighSpeed = false;
    bool transferDir = dir;
    bool txMasterCode = ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.txMasterCode;

    if ((${SERCOM_INSTANCE_NAME?lower_case}I2CObj.isHighSpeed == true) && (txMasterCode == true))
    {
        /* write: <0000-1nnn> <Sr> <xxxx-xxxW> <write-data> <P>
           read: <0000-1nnn> <Sr> <xxxx-xxxR> <read-data> <P>
        */

        /* Next state will be to transmit slave address with HS mode enabled */
        ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.state = SERCOM_I2C_STATE_TRANSFER_ADDR_HS;
    }
    else
    {
        /* If operation is I2C read */
        if(dir)
        {
            /* <xxxx-xxxR> <read-data> <P> */

            /* Next state will be to read data */
            ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.state = SERCOM_I2C_STATE_TRANSFER_READ;

            if (${SERCOM_INSTANCE_NAME?lower_case}I2CObj.isHighSpeed == true)
            {
                /* We are in HS mode and Master code is already transmitted out */
                isHighSpeed = true;
            }
        }
        else
        {
            /* <xxxx-xxxW> <write-data> <P> */

            /* Next state will be to write data */
            ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.state = SERCOM_I2C_STATE_TRANSFER_WRITE;

            if (${SERCOM_INSTANCE_NAME?lower_case}I2CObj.isHighSpeed == true)
            {
                /* We are in HS mode and Master code is already transmitted out */
                isHighSpeed = true;
            }
        }
    }

    if (txMasterCode == true)
    {
        /* Transmit masterCode */
        ${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_ADDR = ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.masterCode;
    }
    else
    {
        ${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_ADDR = SERCOM_I2CM_ADDR_HS(isHighSpeed ? 1UL: 0UL) | ((uint32_t)address << 1U) | (transferDir ? 1UL : 0UL);
    }

    /* Wait for synchronization */
<#if SERCOM_SYNCBUSY = false>
    while((${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_STATUS & (uint16_t)SERCOM_I2CM_STATUS_SYNCBUSY_Msk) == (uint16_t)SERCOM_I2CM_STATUS_SYNCBUSY_Msk)
    {
        /* Do nothing */
    }
<#else>
    while((${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_SYNCBUSY) != 0U)
    {
        /* Do nothing */
    }
</#if>

}
</#if>
<#else>
<#if (I2C_ADDR_TENBITEN?? && I2C_ADDR_TENBITEN = true)>

static void ${SERCOM_INSTANCE_NAME}_I2C_SendAddress(uint16_t address, bool dir)
{
    bool isTenBitAddress = false;
    bool transferDir = dir;

    /* Check for 10-bit address */
    if(address > 0x007FU)
    {
        isTenBitAddress = true;
        transferDir = false;

        /* If operation is I2C read */
        if(dir)
        {
            /* <Sr> <1111-10xxW> <xxxx-xxxx> <Sr> <1111-10xxR> <read-data> <P> */

            /* Next state will be to send slave address followed by Sr */
            ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.state = SERCOM_I2C_STATE_ADDR_SEND;
        }
        else
        {
            /* <Sr> <1111-10xxW> <xxxx-xxxx> <write-data> <P>  */

            ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.state = SERCOM_I2C_STATE_TRANSFER_WRITE;
        }
    }
    else
    {
        /* If operation is I2C read */
        if(dir)
        {
            /* <xxxx-xxxR> <read-data> <P> */

            /* Next state will be to read data */
            ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.state = SERCOM_I2C_STATE_TRANSFER_READ;
        }
        else
        {
            /* <xxxx-xxxW> <write-data> <P> */

            /* Next state will be to write data */
            ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.state = SERCOM_I2C_STATE_TRANSFER_WRITE;
        }
    }

    ${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_ADDR = SERCOM_I2CM_ADDR_TENBITEN(isTenBitAddress ? 1UL: 0UL) | ((uint32_t)address << 1U) | (transferDir ? 1UL : 0UL);

    /* Wait for synchronization */
<#if SERCOM_SYNCBUSY = false>
    while((${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_STATUS & (uint16_t)SERCOM_I2CM_STATUS_SYNCBUSY_Msk) == (uint16_t)SERCOM_I2CM_STATUS_SYNCBUSY_Msk)
    {
        /* Do nothing */
    }
<#else>
    while((${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_SYNCBUSY) != 0U)
    {
        /* Do nothing */
    }
</#if>

}
<#else>

static void ${SERCOM_INSTANCE_NAME}_I2C_SendAddress(uint16_t address, bool dir)
{
    /* If operation is I2C read */
    if(dir)
    {
        /* <xxxx-xxxR> <read-data> <P> */

        /* Next state will be to read data */
        ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.state = SERCOM_I2C_STATE_TRANSFER_READ;
    }
    else
    {
        /* <xxxx-xxxW> <write-data> <P> */

        /* Next state will be to write data */
        ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.state = SERCOM_I2C_STATE_TRANSFER_WRITE;
    }


<#if I2CM_ADDR_SIZE == 1>
    ${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_ADDR = ((uint8_t)address << 1U) | (dir ? 1U :0U);
<#else>
    ${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_ADDR = ((uint32_t)address << 1U) | (dir ? 1UL :0UL);
</#if>

    /* Wait for synchronization */
<#if SERCOM_SYNCBUSY = false>
    while((${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_STATUS & (uint16_t)SERCOM_I2CM_STATUS_SYNCBUSY_Msk) == (uint16_t)SERCOM_I2CM_STATUS_SYNCBUSY_Msk)
    {
        /* Do nothing */
    }
<#else>
    while((${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_SYNCBUSY) != 0U)
    {
        /* Do nothing */
    }
</#if>

}
</#if>
</#if>

static void ${SERCOM_INSTANCE_NAME}_I2C_InitiateTransfer(uint16_t address, bool dir)
{
    ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.writeCount = 0U;
    ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.readCount = 0U;

    /* Clear all flags */
    ${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_INTFLAG = (uint8_t)SERCOM_I2CM_INTFLAG_Msk;

    <#if I2C_SCLSM?? && I2C_SCLSM = 1>
    if(${SERCOM_INSTANCE_NAME?lower_case}I2CObj.readSize == 1U)
    {
        /* Only 1 byte to read. Since SCLSM = 1, setup to send NAK */
        ${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_CTRLB |= SERCOM_I2CM_CTRLB_ACKACT_Msk ;
    }
    else
    {
        /* Smart mode enabled, with SCLSM = 1, - ACK is set to send while receiving the data */
        ${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_CTRLB &= ~SERCOM_I2CM_CTRLB_ACKACT_Msk;
    }
    <#else>
    /* Smart mode enabled with SCLSM = 0, - ACK is set to send while receiving the data */
    ${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_CTRLB &= ~SERCOM_I2CM_CTRLB_ACKACT_Msk;
    </#if>

    /* Wait for synchronization */
<#if SERCOM_SYNCBUSY = false>
    while((${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_STATUS & (uint16_t)SERCOM_I2CM_STATUS_SYNCBUSY_Msk) == (uint16_t)SERCOM_I2CM_STATUS_SYNCBUSY_Msk)
    {
        /* Do nothing */
    }
<#else>
    while((${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_SYNCBUSY) != 0U)
    {
        /* Do nothing */
    }
</#if>


    ${SERCOM_INSTANCE_NAME}_I2C_SendAddress(address, dir);
}

static bool ${SERCOM_INSTANCE_NAME}_I2C_XferSetup(
    uint16_t address,
    uint8_t* wrData,
    uint32_t wrLength,
    uint8_t* rdData,
    uint32_t rdLength,
    bool dir,
    bool isHighSpeed
)
{
    /* Check for ongoing transfer */
    if(${SERCOM_INSTANCE_NAME?lower_case}I2CObj.state != SERCOM_I2C_STATE_IDLE)
    {
        return false;
    }

    ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.address        = address;
    ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.readBuffer     = rdData;
    ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.readSize       = rdLength;
    ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.writeBuffer    = wrData;
    ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.writeSize      = wrLength;
    ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.transferDir    = dir;
    ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.isHighSpeed    = isHighSpeed;
    ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.error          = SERCOM_I2C_ERROR_NONE;

<#if (I2CM_MODE?? && I2CM_MODE = "HIGH_SPEED_MODE")>
    if (isHighSpeed == true)
    {
        ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.txMasterCode = true;
    }
    else
    {
        ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.txMasterCode = false;
    }
</#if>

    ${SERCOM_INSTANCE_NAME}_I2C_InitiateTransfer(address, dir);

    return true;
}

bool ${SERCOM_INSTANCE_NAME}_I2C_Read(uint16_t address, uint8_t* rdData, uint32_t rdLength)
{
    return ${SERCOM_INSTANCE_NAME}_I2C_XferSetup(address, NULL, 0, rdData, rdLength, true, false);
}

bool ${SERCOM_INSTANCE_NAME}_I2C_Write(uint16_t address, uint8_t* wrData, uint32_t wrLength)
{
    return ${SERCOM_INSTANCE_NAME}_I2C_XferSetup(address, wrData, wrLength, NULL, 0, false, false);
}

bool ${SERCOM_INSTANCE_NAME}_I2C_WriteRead(uint16_t address, uint8_t* wrData, uint32_t wrLength, uint8_t* rdData, uint32_t rdLength)
{
    return ${SERCOM_INSTANCE_NAME}_I2C_XferSetup(address, wrData, wrLength, rdData, rdLength, false, false);
}

<#if (I2CM_MODE?? && I2CM_MODE = "HIGH_SPEED_MODE")>
bool ${SERCOM_INSTANCE_NAME}_I2C_Read_HighSpeed(uint16_t address, uint8_t* rdData, uint32_t rdLength)
{
    return ${SERCOM_INSTANCE_NAME}_I2C_XferSetup(address, NULL, 0, rdData, rdLength, true, true);
}

bool ${SERCOM_INSTANCE_NAME}_I2C_Write_HighSpeed(uint16_t address, uint8_t* wrData, uint32_t wrLength)
{
    return ${SERCOM_INSTANCE_NAME}_I2C_XferSetup(address, wrData, wrLength, NULL, 0, false, true);
}

bool ${SERCOM_INSTANCE_NAME}_I2C_WriteRead_HighSpeed(uint16_t address, uint8_t* wrData, uint32_t wrLength, uint8_t* rdData, uint32_t rdLength)
{
    return ${SERCOM_INSTANCE_NAME}_I2C_XferSetup(address, wrData, wrLength, rdData, rdLength, false, true);
}
</#if>

bool ${SERCOM_INSTANCE_NAME}_I2C_BusScan(uint16_t start_addr, uint16_t end_addr, void* pDevicesList, uint8_t* nDevicesFound)
{
    uint8_t* pDevList = (uint8_t*)pDevicesList;
    uint8_t nDevFound = 0;

    /* Check for ongoing transfer */
    if(${SERCOM_INSTANCE_NAME?lower_case}I2CObj.state != SERCOM_I2C_STATE_IDLE)
    {
        return false;
    }

    if (pDevList == NULL)
    {
        return false;
    }

    *nDevicesFound = 0;

    /* Clear all flags */
    ${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_INTFLAG = (uint8_t)SERCOM_I2CM_INTFLAG_Msk;

    /* Disable all interrupts */
    ${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_INTENCLR = (uint8_t)SERCOM_I2CM_INTENCLR_Msk;

    for (uint16_t dev_addr = start_addr; dev_addr <= end_addr; dev_addr++)
    {
        while(((${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_STATUS & SERCOM_I2CM_STATUS_BUSSTATE_Msk) != SERCOM_I2CM_STATUS_BUSSTATE(0x01U)))
        {
            /* Wait for the bus to become IDLE */
        }

        <#if (I2C_ADDR_TENBITEN?? && I2C_ADDR_TENBITEN = true)>
        if (dev_addr > 0x007FU)
        {
            ${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_ADDR = ((uint32_t)dev_addr << 1U) | SERCOM_I2CM_ADDR_TENBITEN_Msk;
        }
        else
        {
            /* Put the 7-bit device address on the bus with WR bit */
            ${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_ADDR = ((uint32_t)dev_addr << 1U);
        }
        <#else>
        /* Put the 7-bit device address on the bus with WR bit */
        ${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_ADDR = ((uint32_t)dev_addr << 1U);
        </#if>

        /* Wait for synchronization */
        <#if SERCOM_SYNCBUSY = false>
        while((${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_STATUS & (uint16_t)SERCOM_I2CM_STATUS_SYNCBUSY_Msk) == (uint16_t)SERCOM_I2CM_STATUS_SYNCBUSY_Msk)
        {
            /* Do nothing */
        }
        <#else>
        while((${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_SYNCBUSY) != 0U)
        {
            /* Do nothing */
        }
        </#if>

        while ((${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_INTFLAG & SERCOM_I2CM_INTFLAG_MB_Msk) == 0)
        {
            /* Wait for the address transfer to complete */
        }

        if ((${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_STATUS & (SERCOM_I2CM_STATUS_ARBLOST_Msk | SERCOM_I2CM_STATUS_BUSERR_Msk | SERCOM_I2CM_STATUS_RXNACK_Msk)) == 0U)
        {
            /* No error and device responded with an ACK. Add the device to the list of found devices. */
            <#if (I2C_ADDR_TENBITEN?? && I2C_ADDR_TENBITEN = true)>
            if (dev_addr > 0x007FU)
            {
                ((uint16_t*)&pDevList)[nDevFound] = dev_addr;
            }
            else
            {
                pDevList[nDevFound] = dev_addr;
            }
            <#else>
            pDevList[nDevFound] = dev_addr;
            </#if>

            nDevFound += 1;
        }

        /* Issue stop condition */
        ${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_CTRLB |= SERCOM_I2CM_CTRLB_CMD(3UL);

        /* Wait for synchronization */
        <#if SERCOM_SYNCBUSY = false>
        while((${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_STATUS & (uint16_t)SERCOM_I2CM_STATUS_SYNCBUSY_Msk) == (uint16_t)SERCOM_I2CM_STATUS_SYNCBUSY_Msk)
        {
            /* Do nothing */
        }
        <#else>
        while((${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_SYNCBUSY) != 0U)
        {
            /* Do nothing */
        }
        </#if>
    }

    *nDevicesFound = nDevFound;

    /* Re-enable all interrupts */
    ${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_INTENSET = (uint8_t)SERCOM_I2CM_INTENSET_Msk;

    return true;
}

bool ${SERCOM_INSTANCE_NAME}_I2C_IsBusy(void)
{
    bool isBusy = true;
    if((${SERCOM_INSTANCE_NAME?lower_case}I2CObj.state == SERCOM_I2C_STATE_IDLE))
    {
        if(((${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_STATUS & SERCOM_I2CM_STATUS_BUSSTATE_Msk) == SERCOM_I2CM_STATUS_BUSSTATE(0x01U)))
        {
           isBusy = false;
        }
    }
    return isBusy;
}

SERCOM_I2C_ERROR ${SERCOM_INSTANCE_NAME}_I2C_ErrorGet(void)
{
    return ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.error;
}

void ${SERCOM_INSTANCE_NAME}_I2C_TransferAbort( void )
{
    ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.error = SERCOM_I2C_ERROR_NONE;

    // Reset the plib to IDLE state
    ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.state = SERCOM_I2C_STATE_IDLE;

    /* Disable the I2C module */
    ${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_CTRLA &= ~SERCOM_I2CM_CTRLA_ENABLE_Msk;

    /* Wait for synchronization */
<#if SERCOM_SYNCBUSY = false>
    while((${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_STATUS & (uint16_t)SERCOM_I2CM_STATUS_SYNCBUSY_Msk) == (uint16_t)SERCOM_I2CM_STATUS_SYNCBUSY_Msk)
    {
        /* Do nothing */
    }
<#else>
    while((${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_SYNCBUSY) != 0U)
    {
        /* Do nothing */
    }
</#if>

    /* Re-enable the I2C module */
    ${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_CTRLA |= SERCOM_I2CM_CTRLA_ENABLE_Msk;

    /* Wait for synchronization */
<#if SERCOM_SYNCBUSY = false>
    while((${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_STATUS & (uint16_t)SERCOM_I2CM_STATUS_SYNCBUSY_Msk) == (uint16_t)SERCOM_I2CM_STATUS_SYNCBUSY_Msk)
    {
        /* Do nothing */
    }
<#else>
    while((${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_SYNCBUSY) != 0U)
    {
        /* Do nothing */
    }
</#if>

    /* Since the I2C module was disabled, re-initialize the bus state to IDLE */
    ${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_STATUS = (uint16_t)SERCOM_I2CM_STATUS_BUSSTATE(0x01UL);

    /* Wait for synchronization */
<#if SERCOM_SYNCBUSY = false>
    while((${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_STATUS & (uint16_t)SERCOM_I2CM_STATUS_SYNCBUSY_Msk) == (uint16_t)SERCOM_I2CM_STATUS_SYNCBUSY_Msk)
    {
        /* Do nothing */
    }
<#else>
    while((${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_SYNCBUSY) != 0U)
    {
        /* Do nothing */
    }
</#if>
}

void __attribute__((used)) ${SERCOM_INSTANCE_NAME}_I2C_InterruptHandler(void)
{
    if(${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_INTENSET != 0U)
    {
        uintptr_t context = ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.context;

        <#if (I2CM_MODE?? && I2CM_MODE = "HIGH_SPEED_MODE")>
        bool isHighSpeed = ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.isHighSpeed;
        bool txMasterCode = ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.txMasterCode;
        </#if>
        /* Checks if the arbitration lost in multi-master scenario */
        if((${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_STATUS & SERCOM_I2CM_STATUS_ARBLOST_Msk) == SERCOM_I2CM_STATUS_ARBLOST_Msk)
        {
            /* Set Error status */
            ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.state = SERCOM_I2C_STATE_ERROR;
            ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.error = SERCOM_I2C_ERROR_BUS;

        }
        /* Check for Bus Error during transmission */
        else if((${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_STATUS & SERCOM_I2CM_STATUS_BUSERR_Msk) == SERCOM_I2CM_STATUS_BUSERR_Msk)
        {
            /* Set Error status */
            ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.state = SERCOM_I2C_STATE_ERROR;
            ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.error = SERCOM_I2C_ERROR_BUS;
        }
        /* Checks slave acknowledge for address or data */
        <#if (I2CM_MODE?? && I2CM_MODE = "HIGH_SPEED_MODE")>
        else if(((${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_STATUS & SERCOM_I2CM_STATUS_RXNACK_Msk) == SERCOM_I2CM_STATUS_RXNACK_Msk) && (txMasterCode == false))
        {
            ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.state = SERCOM_I2C_STATE_ERROR;
            ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.error = SERCOM_I2C_ERROR_NAK;
        }
        <#else>
        else if((${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_STATUS & SERCOM_I2CM_STATUS_RXNACK_Msk) == SERCOM_I2CM_STATUS_RXNACK_Msk)
        {
            ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.state = SERCOM_I2C_STATE_ERROR;
            ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.error = SERCOM_I2C_ERROR_NAK;
        }
        </#if>
        else
        {
            switch(${SERCOM_INSTANCE_NAME?lower_case}I2CObj.state)
            {
                case SERCOM_I2C_REINITIATE_TRANSFER:

                    if (${SERCOM_INSTANCE_NAME?lower_case}I2CObj.writeSize != 0U)
                    {
                        /* Initiate Write transfer */
                        ${SERCOM_INSTANCE_NAME}_I2C_InitiateTransfer(${SERCOM_INSTANCE_NAME?lower_case}I2CObj.address, false);
                    }
                    else
                    {
                        /* Initiate Read transfer */
                        ${SERCOM_INSTANCE_NAME}_I2C_InitiateTransfer(${SERCOM_INSTANCE_NAME?lower_case}I2CObj.address, true);
                    }

                    break;


                case SERCOM_I2C_STATE_IDLE:

                    break;

                <#if (I2C_ADDR_TENBITEN?? && I2C_ADDR_TENBITEN = true)>
                case SERCOM_I2C_STATE_ADDR_SEND:

                    /*
                     * Send slave address for a read operation with 10-bit addressing enabled
                     * Write ADDR[7:0] register to "11110 address[9:8] 1"
                     * ADDR.TENBITEN must be cleared
                     */
                    <#if (I2CM_MODE?? && I2CM_MODE = "HIGH_SPEED_MODE")>

                    ${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_ADDR = SERCOM_I2CM_ADDR_HS(isHighSpeed ? 1UL: 0UL) | (((uint32_t)(${SERCOM_INSTANCE_NAME?lower_case}I2CObj.address) >> RIGHT_ALIGNED) << 1U) | (uint32_t)I2C_TRANSFER_READ;
                    <#else>
                    ${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_ADDR =  (((uint32_t)(${SERCOM_INSTANCE_NAME?lower_case}I2CObj.address) >> RIGHT_ALIGNED) << 1U) | (uint32_t)I2C_TRANSFER_READ;
                    </#if>

                    /* Wait for synchronization */
                    <#if SERCOM_SYNCBUSY = false>
                    while((${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_STATUS & (uint16_t)SERCOM_I2CM_STATUS_SYNCBUSY_Msk) == (uint16_t)SERCOM_I2CM_STATUS_SYNCBUSY_Msk)
                    {
                        /* Do nothing */
                    }
                    <#else>
                    while((${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_SYNCBUSY) != 0U)
                    {
                        /* Do nothing */
                    }
                    </#if>

                    ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.state = SERCOM_I2C_STATE_TRANSFER_READ;

                    break;
                </#if>

                <#if (I2CM_MODE?? && I2CM_MODE = "HIGH_SPEED_MODE")>
                case SERCOM_I2C_STATE_TRANSFER_ADDR_HS:

                    ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.txMasterCode = false;

                    /* At this point, master code is already transmitted out. Now send the slave address (7 or 10-bit) */
                    ${SERCOM_INSTANCE_NAME}_I2C_SendAddress(${SERCOM_INSTANCE_NAME?lower_case}I2CObj.address, ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.transferDir);

                    break;
                </#if>

                case SERCOM_I2C_STATE_TRANSFER_WRITE:
                {
                    size_t writeCount = ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.writeCount;

                    if (writeCount == (${SERCOM_INSTANCE_NAME?lower_case}I2CObj.writeSize))
                    {
                        if(${SERCOM_INSTANCE_NAME?lower_case}I2CObj.readSize != 0U)
                        {
                            <#if I2C_SCLSM?? && I2C_SCLSM = 1>
                            if(${SERCOM_INSTANCE_NAME?lower_case}I2CObj.readSize == 1U)
                            {
                                /* Only 1 byte to read. Since SCLSM = 1, setup to send NAK */
                                ${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_CTRLB |= SERCOM_I2CM_CTRLB_ACKACT_Msk ;

                                /* Wait for synchronization */
                            <#if SERCOM_SYNCBUSY = false>
                                while((${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_STATUS & (uint16_t)SERCOM_I2CM_STATUS_SYNCBUSY_Msk) == (uint16_t)SERCOM_I2CM_STATUS_SYNCBUSY_Msk)
                                {
                                    /* Do nothing */
                                }
                            <#else>
                                while((${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_SYNCBUSY) != 0U)
                                {
                                    /* Do nothing */
                                }
                            </#if>

                            }
                            </#if>

                            <#if (I2CM_MODE?? && I2CM_MODE = "HIGH_SPEED_MODE")>
                            <#if (I2C_ADDR_TENBITEN?? && I2C_ADDR_TENBITEN = true)>
                            if(${SERCOM_INSTANCE_NAME?lower_case}I2CObj.address > 0x007FU)
                            {
                                /*
                                 * Write ADDR[7:0] register to "11110 address[9:8] 1"
                                 * ADDR.TENBITEN must be cleared
                                 */
                                ${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_ADDR = SERCOM_I2CM_ADDR_HS((isHighSpeed == true)? 1UL: 0UL) | (((uint32_t)(${SERCOM_INSTANCE_NAME?lower_case}I2CObj.address) >> RIGHT_ALIGNED) << 1U) | (uint32_t)I2C_TRANSFER_READ;
                            }
                            else
                            {
                                /* Write 7bit address with direction (ADDR.ADDR[0]) equal to 1*/
                                ${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_ADDR = SERCOM_I2CM_ADDR_HS((isHighSpeed == true)? 1UL: 0UL) | ((uint32_t)(${SERCOM_INSTANCE_NAME?lower_case}I2CObj.address) << 1U) | (uint32_t)I2C_TRANSFER_READ;
                            }
                            <#else>
                            /* Write 7bit address with direction (ADDR.ADDR[0]) equal to 1*/
                             ${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_ADDR = SERCOM_I2CM_ADDR_HS((isHighSpeed == true)? 1UL: 0UL) | ((uint32_t)(${SERCOM_INSTANCE_NAME?lower_case}I2CObj.address) << 1UL) | (uint32_t)I2C_TRANSFER_READ;
                            </#if>
                            <#else>
                            <#if (I2C_ADDR_TENBITEN?? && I2C_ADDR_TENBITEN = true)>
                            if(${SERCOM_INSTANCE_NAME?lower_case}I2CObj.address > 0x007FU)
                            {
                                /*
                                 * Write ADDR[7:0] register to "11110 address[9:8] 1"
                                 * ADDR.TENBITEN must be cleared
                                 */
                                ${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_ADDR =  (((uint32_t)(${SERCOM_INSTANCE_NAME?lower_case}I2CObj.address) >> RIGHT_ALIGNED) << 1U) | (uint32_t)I2C_TRANSFER_READ;
                            }
                            else
                            {
                                /* Write 7bit address with direction (ADDR.ADDR[0]) equal to 1*/
                                ${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_ADDR =  ((uint32_t)(${SERCOM_INSTANCE_NAME?lower_case}I2CObj.address) << 1U) | (uint32_t)I2C_TRANSFER_READ;
                            }
                            <#else>
                            /* Write 7bit address with direction (ADDR.ADDR[0]) equal to 1*/
                            <#if I2CM_ADDR_SIZE == 1>
                            ${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_ADDR =  ((uint8_t)(${SERCOM_INSTANCE_NAME?lower_case}I2CObj.address) << 1U) | (uint8_t)I2C_TRANSFER_READ;
                            <#else>
                            ${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_ADDR =  ((uint32_t)(${SERCOM_INSTANCE_NAME?lower_case}I2CObj.address) << 1U) | (uint32_t)I2C_TRANSFER_READ;
                            </#if>
                            </#if>
                            </#if>

                            /* Wait for synchronization */
                        <#if SERCOM_SYNCBUSY = false>
                            while((${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_STATUS & (uint16_t)SERCOM_I2CM_STATUS_SYNCBUSY_Msk) == (uint16_t)SERCOM_I2CM_STATUS_SYNCBUSY_Msk)
                            {
                                /* Do nothing */
                            }
                        <#else>
                            while((${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_SYNCBUSY) != 0U)
                            {
                                /* Do nothing */
                            }
                        </#if>

                            ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.state = SERCOM_I2C_STATE_TRANSFER_READ;

                        }
                        else
                        {
                            ${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_CTRLB |= SERCOM_I2CM_CTRLB_CMD(3UL);

                            /* Wait for synchronization */
                        <#if SERCOM_SYNCBUSY = false>
                            while((${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_STATUS & (uint16_t)SERCOM_I2CM_STATUS_SYNCBUSY_Msk) == (uint16_t)SERCOM_I2CM_STATUS_SYNCBUSY_Msk)
                            {
                                /* Do nothing */
                            }
                        <#else>
                            while((${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_SYNCBUSY) != 0U)
                            {
                                /* Do nothing */
                            }
                        </#if>


                            ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.state = SERCOM_I2C_STATE_TRANSFER_DONE;
                        }
                    }
                    /* Write next byte */
                    else
                    {
                        ${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_DATA = ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.writeBuffer[writeCount];
                        writeCount++;
                        /* Wait for synchronization */
                        <#if SERCOM_SYNCBUSY = false>
                            while((${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_STATUS & (uint16_t)SERCOM_I2CM_STATUS_SYNCBUSY_Msk) == (uint16_t)SERCOM_I2CM_STATUS_SYNCBUSY_Msk)
                            {
                                /* Do nothing */
                            }
                        <#else>
                            while((${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_SYNCBUSY) != 0U)
                            {
                                /* Do nothing */
                            }
                        </#if>
                        ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.writeCount = writeCount;
                    }
                }

                    break;

                case SERCOM_I2C_STATE_TRANSFER_READ:
                {
                    size_t readCount = ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.readCount;

                    <#if I2C_SCLSM?? && I2C_SCLSM = 1>

                    if((readCount + 1U) == (${SERCOM_INSTANCE_NAME?lower_case}I2CObj.readSize - 1U))
                    {
                        /* For the next byte, send NAK to the slave */
                        ${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_CTRLB |= SERCOM_I2CM_CTRLB_ACKACT_Msk ;

                        /* Wait for synchronization */
                    <#if SERCOM_SYNCBUSY = false>
                        while((${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_STATUS & (uint16_t)SERCOM_I2CM_STATUS_SYNCBUSY_Msk) == (uint16_t)SERCOM_I2CM_STATUS_SYNCBUSY_Msk)
                        {
                            /* Do nothing */
                        }
                    <#else>
                        while((${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_SYNCBUSY) != 0U)
                        {
                            /* Do nothing */
                        }
                    </#if>
                    }
                    if ((readCount + 1U) == ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.readSize)
                    {
                        /* All bytes are received, send Stop bit */
                        ${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_CTRLB |= SERCOM_I2CM_CTRLB_CMD(3UL);

                        /* Wait for synchronization */
                    <#if SERCOM_SYNCBUSY = false>
                        while((${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_STATUS & (uint16_t)SERCOM_I2CM_STATUS_SYNCBUSY_Msk) == (uint16_t)SERCOM_I2CM_STATUS_SYNCBUSY_Msk)
                        {
                            /* Do nothing */
                        }
                    <#else>
                        while((${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_SYNCBUSY) != 0U)
                        {
                            /* Do nothing */
                        }
                    </#if>

                        ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.state = SERCOM_I2C_STATE_TRANSFER_DONE;
                    }

                    /* Wait for synchronization */
                    <#if SERCOM_SYNCBUSY = false>
                        while((${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_STATUS & (uint16_t)SERCOM_I2CM_STATUS_SYNCBUSY_Msk) == (uint16_t)SERCOM_I2CM_STATUS_SYNCBUSY_Msk)
                        {
                            /* Do nothing */
                        }
                    <#else>
                        while((${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_SYNCBUSY) != 0U)
                        {
                            /* Do nothing */
                        }
                    </#if>

                    /* Read the received data */
                    ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.readBuffer[readCount] =(uint8_t) ${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_DATA;
                    readCount++;
                    <#else>

                    if(readCount == (${SERCOM_INSTANCE_NAME?lower_case}I2CObj.readSize - 1U))
                    {
                        /* Set NACK and send stop condition to the slave from master */
                        ${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_CTRLB |= SERCOM_I2CM_CTRLB_ACKACT_Msk | SERCOM_I2CM_CTRLB_CMD(3UL);

                        /* Wait for synchronization */
                    <#if SERCOM_SYNCBUSY = false>
                        while((${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_STATUS & (uint16_t)SERCOM_I2CM_STATUS_SYNCBUSY_Msk) == (uint16_t)SERCOM_I2CM_STATUS_SYNCBUSY_Msk)
                        {
                            /* Do nothing */
                        }
                    <#else>
                        while((${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_SYNCBUSY) != 0U)
                        {
                            /* Do nothing */
                        }
                    </#if>

                        ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.state = SERCOM_I2C_STATE_TRANSFER_DONE;
                    }

                    /* Wait for synchronization */
                    <#if SERCOM_SYNCBUSY = false>
                        while((${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_STATUS & (uint16_t)SERCOM_I2CM_STATUS_SYNCBUSY_Msk) == (uint16_t)SERCOM_I2CM_STATUS_SYNCBUSY_Msk)
                        {
                            /* Do nothing */
                        }
                    <#else>
                        while((${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_SYNCBUSY) != 0U)
                        {
                            /* Do nothing */
                        }
                    </#if>

                    /* Read the received data */
                    ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.readBuffer[readCount] = (uint8_t) ${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_DATA;
                    readCount++;
                    </#if>

                    ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.readCount = readCount;
                }

                    break;

                default:

                    /* Do nothing */
                    break;
            }
        }

        /* Error Status */
        if(${SERCOM_INSTANCE_NAME?lower_case}I2CObj.state == SERCOM_I2C_STATE_ERROR)
        {
            /* Reset the PLib objects and Interrupts */
            ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.state = SERCOM_I2C_STATE_IDLE;

            /* Generate STOP condition */
            ${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_CTRLB |= SERCOM_I2CM_CTRLB_CMD(3UL);

            /* Wait for synchronization */
        <#if SERCOM_SYNCBUSY = false>
            while((${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_STATUS & (uint16_t)SERCOM_I2CM_STATUS_SYNCBUSY_Msk) == (uint16_t)SERCOM_I2CM_STATUS_SYNCBUSY_Msk)
            {
                /* Do nothing */
            }
        <#else>
            while((${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_SYNCBUSY) != 0U)
            {
                /* Do nothing */
            }
        </#if>


            ${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_INTFLAG = (uint8_t)SERCOM_I2CM_INTFLAG_Msk;

            if (${SERCOM_INSTANCE_NAME?lower_case}I2CObj.callback != NULL)
            {
                ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.callback(context);
            }
        }
        /* Transfer Complete */
        else if(${SERCOM_INSTANCE_NAME?lower_case}I2CObj.state == SERCOM_I2C_STATE_TRANSFER_DONE)
        {
            /* Reset the PLib objects and interrupts */
            ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.state = SERCOM_I2C_STATE_IDLE;
            ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.error = SERCOM_I2C_ERROR_NONE;

            ${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_INTFLAG = (uint8_t)SERCOM_I2CM_INTFLAG_Msk;

            /* Wait for the NAK and STOP bit to be transmitted out and I2C state machine to rest in IDLE state */
            while((${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_STATUS & SERCOM_I2CM_STATUS_BUSSTATE_Msk) != SERCOM_I2CM_STATUS_BUSSTATE(0x01U))
            {
                /* Do nothing */
            }

            if(${SERCOM_INSTANCE_NAME?lower_case}I2CObj.callback != NULL)
            {
                ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.callback(context);
            }

        }
        else
        {
            /* Do nothing */
        }
    }

    return;
}