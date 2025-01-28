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
#include "plib_i2c${instance}_host.h"
<#if core.CoreSysIntFile == true>
#include "interrupts.h"
</#if>

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

#define NOP asm(" NOP")
volatile static I2C_HOST_OBJ ${moduleName?lower_case}Obj;
void ${i2cErrorInterruptHandler}(void);
void ${i2cCommonInterruptHandler}(void);

void ${moduleName}_Initialize(void)
{

    _${moduleName}IE = 0U;
    _${moduleName}EIE = 0U;

    ${moduleName}HBRG = 0x${brgValueInHex}UL; 
    ${moduleName}LBRG = 0x${brgValueInHex}UL;

    ${moduleName}CON1 = (I2C${instance}CON1_SMBEN_${smbenOptions[.vars["I2C_CON1__SMBEN"]?number]}
                        |I2C${instance}CON1_SDAHT_${sdhatOptions[.vars["I2C_CON1__SDAHT"]?number]}
                        |_I2C${instance}CON1_SCLREL_MASK<#if I2C_CON1__DISSLW?number != 0>
                        |_I2C${instance}CON1_DISSLW_MASK</#if>);
    ${moduleName}INTC = (_I2C${instance}INTC_BCLIE_MASK
                        |_I2C${instance}INTC_HPCIE_MASK
                        |_I2C${instance}INTC_HSCIE_MASK
                        |_I2C${instance}INTC_HACKSIE_MASK
                        |_I2C${instance}INTC_HDTXIE_MASK
                        |_I2C${instance}INTC_HDRXIE_MASK
                        |_I2C${instance}INTC_HSTIE_MASK);   

    /* Clear host interrupt flag */
    _I2C${instance}IF = 0U;

    /* Clear fault interrupt flag */
    _I2C${instance}EIF = 0U;

    /* Turn on the I2C module */
    I2C${instance}CON1bits.ON = 1U;
    
    ${moduleName?lower_case}Obj.callback = NULL;  

    /* Set the initial state of the I2C state machine */
    ${moduleName?lower_case}Obj.state = I2C_STATE_IDLE;
}

void ${moduleName}_Deinitialize(void)
{
    /* Turn off the I2C module */
    I2C${instance}CON1bits.ON = 0U;
    
    /* Clear host interrupt flag */
    _I2C${instance}IF = 0U;
    /* Clear fault interrupt flag */
    _I2C${instance}EIF = 0U;
    
    ${moduleName}CON1 = (_I2C${instance}CON1_SCLREL_MASK);
    ${moduleName}INTC = 0x0UL;  
    
    ${moduleName}HBRG = 0x0UL; 
    ${moduleName}LBRG = 0x0UL;
    
    ${moduleName?lower_case}Obj.callback = NULL;  

}

/* I2C state machine */
static void ${moduleName}_TransferSM(void)
{
    uint8_t tempVar = 0;
    _I2C${instance}IF = 0;
<#if I2C_INCLUDE_FORCED_WRITE == true>
    bool forcedWrite = ${moduleName?lower_case}Obj.forcedWrite;
</#if>
    switch (${moduleName?lower_case}Obj.state)
    {
        case I2C_STATE_START_CONDITION:
            /* Generate Start Condition */
            _I2C${instance}IE = 1U;
            _I2C${instance}EIE= 1U;
            I2C${instance}CON1bits.SEN = 1;
            ${moduleName?lower_case}Obj.state = I2C_STATE_ADDR_BYTE_1_SEND;
            break;

        case I2C_STATE_ADDR_BYTE_1_SEND:
            /* Is transmit buffer full? */
            if (I2C${instance}STAT1bits.TBF == 0U)
            {
                if (${moduleName?lower_case}Obj.address > 0x007FU)
                {
                    tempVar = (((volatile uint8_t*)&${moduleName?lower_case}Obj.address)[1] << 1);
                    /* Transmit the MSB 2 bits of the 10-bit slave address, with R/W = 0 */
                    I2C${instance}TRN = (uint32_t)( 0xF0U | (uint32_t)tempVar);
                    ${moduleName?lower_case}Obj.state = I2C_STATE_ADDR_BYTE_2_SEND;
                }
                else
                {
                    /* 8-bit addressing mode */
                    I2C_TRANSFER_TYPE transferType = ${moduleName?lower_case}Obj.transferType;
                    I2C${instance}TRN = (((uint32_t)${moduleName?lower_case}Obj.address << 1U) | (uint32_t)transferType);
                    if (${moduleName?lower_case}Obj.transferType == I2C_TRANSFER_TYPE_WRITE)
                    {
                        ${moduleName?lower_case}Obj.state = I2C_STATE_WRITE;
                    }
                    else
                    {
                        ${moduleName?lower_case}Obj.state = I2C_STATE_READ;
                    }
                }
            }
            break;

        case I2C_STATE_ADDR_BYTE_2_SEND:
            /* Transmit the 2nd byte of the 10-bit slave address */
<#if I2C_INCLUDE_FORCED_WRITE == true>
            if ((I2C${instance}STAT1bits.ACKSTAT == 0U) || (forcedWrite == true))
<#else>
            if (I2C${instance}STAT1bits.ACKSTAT == 0U)
</#if>
            {
                if (I2C${instance}STAT1bits.TBF == 0U)
                {
                    /* Transmit the remaining 8-bits of the 10-bit address */
                    I2C${instance}TRN = ${moduleName?lower_case}Obj.address;

                    if (${moduleName?lower_case}Obj.transferType == I2C_TRANSFER_TYPE_WRITE)
                    {
                        ${moduleName?lower_case}Obj.state = I2C_STATE_WRITE;
                    }
                    else
                    {
                        ${moduleName?lower_case}Obj.state = I2C_STATE_READ_10BIT_MODE;
                    }
                }
            }
            else
            {
                /* NAK received. Generate Stop Condition. */
                ${moduleName?lower_case}Obj.error = I2C_ERROR_NACK;
                I2C${instance}CON1bits.PEN = 1U;
                ${moduleName?lower_case}Obj.state = I2C_STATE_WAIT_STOP_CONDITION_COMPLETE;
            }
            break;

        case I2C_STATE_READ_10BIT_MODE:
            if (I2C${instance}STAT1bits.ACKSTAT == 0U)
            {
                /* Generate repeated start condition */
                I2C${instance}CON1bits.RSEN = 1U;
                ${moduleName?lower_case}Obj.state = I2C_STATE_ADDR_BYTE_1_SEND_10BIT_ONLY;
            }
            else
            {
                /* NAK received. Generate Stop Condition. */
                ${moduleName?lower_case}Obj.error = I2C_ERROR_NACK;
                I2C${instance}CON1bits.PEN = 1U;
                ${moduleName?lower_case}Obj.state = I2C_STATE_WAIT_STOP_CONDITION_COMPLETE;
            }
            break;

        case I2C_STATE_ADDR_BYTE_1_SEND_10BIT_ONLY:
            /* Is transmit buffer full? */
            if (${moduleName}STAT1bits.TBF == 0U)
            {
                tempVar = (((volatile uint8_t*)&${moduleName?lower_case}Obj.address)[1] << 1);
                /* Transmit the first byte of the 10-bit slave address, with R/W = 1 */
                I2C${instance}TRN = (uint32_t)( 0xF1U | (uint32_t)tempVar);
                ${moduleName?lower_case}Obj.state = I2C_STATE_READ;
            }
            else
            {
                /* NAK received. Generate Stop Condition. */
                ${moduleName?lower_case}Obj.error = I2C_ERROR_NACK;
                I2C${instance}CON1bits.PEN = 1U;
                ${moduleName?lower_case}Obj.state = I2C_STATE_WAIT_STOP_CONDITION_COMPLETE;
            }
            break;

        case I2C_STATE_WRITE:
<#if I2C_INCLUDE_FORCED_WRITE == true>
            if ((I2C${instance}STAT1bits.ACKSTAT == 0U) || (forcedWrite == true))
<#else>
            if (I2C${instance}STAT1bits.ACKSTAT == 0U)
</#if>
            {
                size_t writeCount = ${moduleName?lower_case}Obj.writeCount;

                /* ACK received */
                if (writeCount < ${moduleName?lower_case}Obj.writeSize)
                {
                    if (I2C${instance}STAT1bits.TBF == 0U)
                    {
                        /* Transmit the data from writeBuffer[] */
                        I2C${instance}TRN = ${moduleName?lower_case}Obj.writeBuffer[writeCount];
                        ${moduleName?lower_case}Obj.writeCount++;
                    }
                }
                else
                {
                    size_t readSize = ${moduleName?lower_case}Obj.readSize;

                    if (${moduleName?lower_case}Obj.readCount < readSize)
                    {
                        /* Generate repeated start condition */
                        I2C${instance}CON1bits.RSEN = 1U;

                        ${moduleName?lower_case}Obj.transferType = I2C_TRANSFER_TYPE_READ;

                        if (${moduleName?lower_case}Obj.address > 0x007FU)
                        {
                            /* Send the I2C slave address with R/W = 1 */
                            ${moduleName?lower_case}Obj.state = I2C_STATE_ADDR_BYTE_1_SEND_10BIT_ONLY;
                        }
                        else
                        {
                            /* Send the I2C slave address with R/W = 1 */
                            ${moduleName?lower_case}Obj.state = I2C_STATE_ADDR_BYTE_1_SEND;
                        }

                    }
                    else
                    {
                        /* Transfer Complete. Generate Stop Condition */
                        I2C${instance}CON1bits.PEN = 1U;
                        ${moduleName?lower_case}Obj.state = I2C_STATE_WAIT_STOP_CONDITION_COMPLETE;
                    }
                }
            }
            else
            {
                /* NAK received. Generate Stop Condition. */
                ${moduleName?lower_case}Obj.error = I2C_ERROR_NACK;
                I2C${instance}CON1bits.PEN = 1U;
                ${moduleName?lower_case}Obj.state = I2C_STATE_WAIT_STOP_CONDITION_COMPLETE;
            }
            break;

        case I2C_STATE_READ:
            if (${moduleName}STAT1bits.ACKSTAT == 0U)
            {
                /* Slave ACK'd the device address. Enable receiver. */
                I2C${instance}CON1bits.RCEN = 1U;
                ${moduleName?lower_case}Obj.state = I2C_STATE_READ_BYTE;
            }
            else
            {
                /* NAK received. Generate Stop Condition. */
                ${moduleName?lower_case}Obj.error = I2C_ERROR_NACK;
                I2C${instance}CON1bits.PEN = 1U;
                ${moduleName?lower_case}Obj.state = I2C_STATE_WAIT_STOP_CONDITION_COMPLETE;
            }
            break;

        case I2C_STATE_READ_BYTE:
            /* Data received from the slave */
            if (I2C${instance}STAT1bits.RBF != 0U)
            {
                size_t readCount = ${moduleName?lower_case}Obj.readCount;

                ${moduleName?lower_case}Obj.readBuffer[readCount] = (uint8_t)${moduleName}RCV;
                readCount++;
                if (readCount == ${moduleName?lower_case}Obj.readSize)
                {
                    /* Send NAK */
                    I2C${instance}CON1bits.ACKDT = 1U;
                    I2C${instance}CON1bits.ACKEN = 1U;
                }
                else
                {
                    /* Send ACK */
                    I2C${instance}CON1bits.ACKDT = 0U;
                    I2C${instance}CON1bits.ACKEN = 1U;
                }
                ${moduleName?lower_case}Obj.readCount = readCount;
                ${moduleName?lower_case}Obj.state = I2C_STATE_WAIT_ACK_COMPLETE;
            }
            break;

        case I2C_STATE_WAIT_ACK_COMPLETE:
            {
                size_t readSize = ${moduleName?lower_case}Obj.readSize;
                /* ACK or NAK sent to the I2C slave */
                if (${moduleName?lower_case}Obj.readCount < readSize)
                {
                    /* Enable receiver */
                    I2C${instance}CON1bits.RCEN = 1U;
                    ${moduleName?lower_case}Obj.state = I2C_STATE_READ_BYTE;
                }
                else
                {
                    /* Generate Stop Condition */
                    I2C${instance}CON1bits.PEN = 1U;
                    ${moduleName?lower_case}Obj.state = I2C_STATE_WAIT_STOP_CONDITION_COMPLETE;
                }
            }
            break;

        case I2C_STATE_WAIT_STOP_CONDITION_COMPLETE:
            ${moduleName?lower_case}Obj.state = I2C_STATE_IDLE;
            _I2C${instance}IE = 0;
            _I2C${instance}EIE = 0;
            if (${moduleName?lower_case}Obj.callback != NULL)
            {
                uintptr_t context = ${moduleName?lower_case}Obj.context;

                ${moduleName?lower_case}Obj.callback(context);
            }
            break;

        default:
                   /*Do Nothing*/
            break;
    }
}


void ${moduleName}_CallbackRegister(I2C_CALLBACK callback, uintptr_t contextHandle)
{
    if (callback != NULL)
    {
       ${moduleName?lower_case}Obj.callback = callback;
       ${moduleName?lower_case}Obj.context = contextHandle;
    }
    return;
}

bool ${moduleName}_IsBusy(void)
{
    bool busycheck = false;
    uint32_t tempVar = I2C${instance}CON1;
    uint32_t tempVar1 = I2C${instance}STAT1;
    if( (${moduleName?lower_case}Obj.state != I2C_STATE_IDLE ) || ((tempVar & 0x0000001FU) != 0U) ||
        ((tempVar1 & _I2C${instance}STAT1_TRSTAT_MASK) != 0U) || ((tempVar1 & _I2C${instance}STAT1_S_MASK) != 0U) )
    {
        busycheck = true;
    }
    return busycheck;
}

bool ${moduleName}_Read(uint16_t address, uint8_t* rdata, size_t rlength)
{
    bool statusRead = false;
    uint32_t tempVar = I2C${instance}STAT1;
    /* State machine must be idle and I2C module should not have detected a start bit on the bus */
    if((${moduleName?lower_case}Obj.state == I2C_STATE_IDLE) && (( tempVar & _I2C${instance}STAT1_S_MASK) == 0U))
    {
        ${moduleName?lower_case}Obj.address             = address;
        ${moduleName?lower_case}Obj.readBuffer          = rdata;
        ${moduleName?lower_case}Obj.readSize            = rlength;
        ${moduleName?lower_case}Obj.writeBuffer         = NULL;
        ${moduleName?lower_case}Obj.writeSize           = 0;
        ${moduleName?lower_case}Obj.writeCount          = 0;
        ${moduleName?lower_case}Obj.readCount           = 0;
        ${moduleName?lower_case}Obj.transferType        = I2C_TRANSFER_TYPE_READ;
        ${moduleName?lower_case}Obj.error               = I2C_ERROR_NONE;
        ${moduleName?lower_case}Obj.state               = I2C_STATE_ADDR_BYTE_1_SEND;
<#if I2C_INCLUDE_FORCED_WRITE == true>
        ${moduleName?lower_case}Obj.forcedWrite         = false;
</#if>
        I2C${instance}CON1bits.SEN = 1U;
        _I2C${instance}IE = 1U;
        _I2C${instance}EIE = 1U;
        statusRead = true;
    }
    return statusRead;
}


bool ${moduleName}_Write(uint16_t address, uint8_t* wdata, size_t wlength)
{
    bool statusWrite = false;
    uint32_t tempVar = I2C${instance}STAT1;
    /* State machine must be idle and I2C module should not have detected a start bit on the bus */
    if((${moduleName?lower_case}Obj.state == I2C_STATE_IDLE) && (( tempVar & _${moduleName}STAT1_S_MASK) == 0U))
    {
        ${moduleName?lower_case}Obj.address             = address;
        ${moduleName?lower_case}Obj.readBuffer          = NULL;
        ${moduleName?lower_case}Obj.readSize            = 0;
        ${moduleName?lower_case}Obj.writeBuffer         = wdata;
        ${moduleName?lower_case}Obj.writeSize           = wlength;
        ${moduleName?lower_case}Obj.writeCount          = 0;
        ${moduleName?lower_case}Obj.readCount           = 0;
        ${moduleName?lower_case}Obj.transferType        = I2C_TRANSFER_TYPE_WRITE;
        ${moduleName?lower_case}Obj.error               = I2C_ERROR_NONE;
        ${moduleName?lower_case}Obj.state               = I2C_STATE_ADDR_BYTE_1_SEND;
<#if I2C_INCLUDE_FORCED_WRITE == true>
        ${moduleName?lower_case}Obj.forcedWrite         = false;
</#if>
        
        I2C${instance}CON1bits.SEN = 1U;
        _I2C${instance}IE = 1U;
        _I2C${instance}EIE= 1U;
        statusWrite = true;
    }
    return statusWrite;
}

<#if I2C_INCLUDE_FORCED_WRITE == true>
bool ${moduleName}_WriteForced(uint16_t address, uint8_t* wdata, size_t wlength)
{
     bool statusWriteForced = false;
     uint32_t tempVar = ${moduleName}STAT1;
    /* State machine must be idle and I2C module should not have detected a start bit on the bus */
    if((${moduleName?lower_case}Obj.state == I2C_STATE_IDLE) &&
       ((tempVar & _${moduleName}STAT1_S_MASK) == 0U))
    {

        ${moduleName?lower_case}Obj.address             = address;
        ${moduleName?lower_case}Obj.readBuffer          = NULL;
        ${moduleName?lower_case}Obj.readSize            = 0;
        ${moduleName?lower_case}Obj.writeBuffer         = wdata;
        ${moduleName?lower_case}Obj.writeSize           = wlength;
        ${moduleName?lower_case}Obj.writeCount          = 0;
        ${moduleName?lower_case}Obj.readCount           = 0;
        ${moduleName?lower_case}Obj.transferType        = I2C_TRANSFER_TYPE_WRITE;
        ${moduleName?lower_case}Obj.error               = I2C_ERROR_NONE;
        ${moduleName?lower_case}Obj.state               = I2C_STATE_ADDR_BYTE_1_SEND;
        ${moduleName?lower_case}Obj.forcedWrite         = true;

        I2C${instance}CON1bits.SEN = 1U;
        _I2C${instance}IE = 1U;
        _I2C${instance}EIE = 1U;
        statusWriteForced = true;
    }

    return statusWriteForced;
}
</#if>

bool ${moduleName}_WriteRead(uint16_t address, uint8_t* wdata, size_t wlength, uint8_t* rdata, size_t rlength)
{
    bool statusWriteread = false;
    uint32_t tempVar = ${moduleName}STAT1;
    /* State machine must be idle and I2C module should not have detected a start bit on the bus */
    if((${moduleName?lower_case}Obj.state == I2C_STATE_IDLE) &&
       ((tempVar & _${moduleName}STAT1_S_MASK) == 0U))
    {
        ${moduleName?lower_case}Obj.address             = address;
        ${moduleName?lower_case}Obj.readBuffer          = rdata;
        ${moduleName?lower_case}Obj.readSize            = rlength;
        ${moduleName?lower_case}Obj.writeBuffer         = wdata;
        ${moduleName?lower_case}Obj.writeSize           = wlength;
        ${moduleName?lower_case}Obj.writeCount          = 0;
        ${moduleName?lower_case}Obj.readCount           = 0;
        ${moduleName?lower_case}Obj.transferType        = I2C_TRANSFER_TYPE_WRITE;
        ${moduleName?lower_case}Obj.error               = I2C_ERROR_NONE;
        ${moduleName?lower_case}Obj.state               = I2C_STATE_ADDR_BYTE_1_SEND;
<#if I2C_INCLUDE_FORCED_WRITE == true>
        ${moduleName?lower_case}Obj.forcedWrite         = false;
</#if>

        I2C${instance}CON1bits.SEN = 1U;
        _I2C${instance}IE = 1U;
        _I2C${instance}EIE = 1U;
        statusWriteread = true;
    }
    return statusWriteread;
}

I2C_ERROR ${moduleName}_ErrorGet(void)
{
    I2C_ERROR error;

    error = ${moduleName?lower_case}Obj.error;
    ${moduleName?lower_case}Obj.error = I2C_ERROR_NONE;

    return error;
}

bool ${moduleName}_TransferSetup(I2C_TRANSFER_SETUP* setup, uint32_t srcClkFreq )
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
    if (i2cClkSpeed > 1000000UL)
    {
        return false;
    }

    if( srcClkFreq == 0U)
    {
        srcClkFreq = 100000000UL;
    }
    
    fBaudValue = (float)((((1.0f / (2.0f * (float)i2cClkSpeed)) - 0.0000002f) * (float)srcClkFreq) - 3.0f);
    baudValue = (uint32_t)fBaudValue;

    /* I2CxBRG value cannot be from 0 to 3 or more than the size of the baud rate register */
    if ((baudValue < 0x4UL) || (baudValue > 0xFFFFFFUL))
    {
        return false;
    }

    I2C${instance}HBRG = baudValue;
    I2C${instance}LBRG = baudValue;

    /* Enable slew rate for 400 kHz clock speed; disable for all other speeds */

    if (i2cClkSpeed == 400000U)
    {
        I2C${instance}CON1bits.DISSLW = 0U;
    }
    else
    {
        I2C${instance}CON1bits.DISSLW = 1U;
    }

    return true;
}

void ${moduleName}_TransferAbort( void )
{
    ${moduleName?lower_case}Obj.error = I2C_ERROR_NONE;

    // Reset the PLib objects and Interrupts
    ${moduleName?lower_case}Obj.state = I2C_STATE_IDLE;
    _I2C${instance}IE = 0U;
    _I2C${instance}EIE = 0U;

    // Disable and Enable I2C Host
    I2C${instance}CON1bits.ON = 0U;
    NOP;NOP;
    I2C${instance}CON1bits.ON = 1U;
}

void __attribute__((used)) ${i2cErrorInterruptHandler}(void)
{
    /* ACK the bus interrupt */
    _I2C${instance}EIF = 0;
    
    if(I2C${instance}STAT1bits.BCL == 1U)
    {
        /* Clear the bus collision error status bit */
        I2C${instance}STAT1bits.BCL = 0U;

        ${moduleName?lower_case}Obj.state = I2C_STATE_IDLE;

        ${moduleName?lower_case}Obj.error = I2C_ERROR_BUS_COLLISION;
    }

    if (${moduleName?lower_case}Obj.callback != NULL)
    {
        uintptr_t context = ${moduleName?lower_case}Obj.context;

        ${moduleName?lower_case}Obj.callback(context);
    }
}

void __attribute__((used)) ${i2cCommonInterruptHandler}(void)
{
    ${moduleName}_TransferSM();
}
