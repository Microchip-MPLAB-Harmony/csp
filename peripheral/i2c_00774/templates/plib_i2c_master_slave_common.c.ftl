/*******************************************************************************
  Inter-Integrated Circuit (I2C) Library
  Source File

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${I2C_INSTANCE_NAME?lower_case}_master_slave_common.c

  Summary:
    I2C PLIB Master Slave Common Implementation file

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
#include "plib_${I2C_INSTANCE_NAME?lower_case}_master_slave_common.h"

extern void ${I2C_INSTANCE_NAME}_MasterBUS_InterruptHandler(void);

extern void ${I2C_INSTANCE_NAME}_SlaveBUS_InterruptHandler(void);

extern void ${I2C_INSTANCE_NAME}_MASTER_InterruptHandler(void);

extern void ${I2C_INSTANCE_NAME}_SLAVE_InterruptHandler(void);

// *****************************************************************************
// *****************************************************************************
// Section: Global Data
// *****************************************************************************
// *****************************************************************************
void ${I2C_INSTANCE_NAME}_Initialize(void)
{
    /* Turn off the I2C module */
    ${I2C_INSTANCE_NAME}CONCLR = _${I2C_INSTANCE_NAME}CON_ON_MASK;
    
    ${I2C_INSTANCE_NAME}_MasterInitialize();
    
    ${I2C_INSTANCE_NAME}_SlaveInitialize();
    
<#if I2C_SIDL == true>
    ${I2C_INSTANCE_NAME}CONSET = _${I2C_INSTANCE_NAME}CON_SIDL_MASK;
</#if>

<#if I2C_DISSLW == true>
    ${I2C_INSTANCE_NAME}CONSET = _${I2C_INSTANCE_NAME}CON_DISSLW_MASK;
</#if>

<#if I2C_SMEN == true>
    ${I2C_INSTANCE_NAME}CONSET = _${I2C_INSTANCE_NAME}CON_SMEN_MASK;
</#if>
    
    /* Turn on the I2C module */
    ${I2C_INSTANCE_NAME}CONSET = _${I2C_INSTANCE_NAME}CON_ON_MASK;
}

void __attribute__((used)) I2C_${I2C_INSTANCE_NUM}_InterruptHandler(void)
{
    uint32_t iec_bus_reg = ${I2C_BUS_IEC_REG};
    uint32_t iec_master_slave_reg = ${I2C_MASTER_IEC_REG};
    if (((${I2C_BUS_IFS_REG} & _${I2C_BUS_IFS_REG}_${I2C_INSTANCE_NAME}BIF_MASK) != 0U) &&
         ((iec_bus_reg & _${I2C_BUS_IEC_REG}_${I2C_INSTANCE_NAME}BIE_MASK) != 0U))
    {
        /* Clear the bus collision error status bit */
        ${I2C_INSTANCE_NAME}STATCLR = _${I2C_INSTANCE_NAME}STAT_BCL_MASK;
        
        /* ACK the bus interrupt */
        ${I2C_MASTER_IFS_REG}CLR = _${I2C_MASTER_IFS_REG}_${I2C_INSTANCE_NAME}BIF_MASK;
    
        ${I2C_INSTANCE_NAME}_MasterBUS_InterruptHandler();
    
        ${I2C_INSTANCE_NAME}_SlaveBUS_InterruptHandler();
    }
    else if (((${I2C_MASTER_IFS_REG} & _${I2C_MASTER_IFS_REG}_${I2C_INSTANCE_NAME}MIF_MASK) != 0U) &&
             ((iec_master_slave_reg & _${I2C_MASTER_IEC_REG}_${I2C_INSTANCE_NAME}MIE_MASK) != 0U))
    {
        ${I2C_INSTANCE_NAME}_MASTER_InterruptHandler();
    }
    else if (((${I2C_SLAVE_IFS_REG} & _${I2C_SLAVE_IFS_REG}_${I2C_INSTANCE_NAME}SIF_MASK) != 0U) &&
             ((iec_master_slave_reg & _${I2C_SLAVE_IEC_REG}_${I2C_INSTANCE_NAME}SIE_MASK) != 0U))
    {
        ${I2C_INSTANCE_NAME}_SLAVE_InterruptHandler();
    }
    else
    {
        /* Do Nothing */
    }
}