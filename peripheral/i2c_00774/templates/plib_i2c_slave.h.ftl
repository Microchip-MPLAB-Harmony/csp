/*******************************************************************************
  Serial Communication Interface Inter-Integrated Circuit (I2C) Library
  Instance Header File

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${I2C_INSTANCE_NAME?lower_case}_slave.h

  Summary:
    I2C PLIB Slave Header file

  Description:
    This file defines the interface to the I2C peripheral library. This
    library provides access to and control of the associated peripheral
    instance.
*******************************************************************************/
// DOM-IGNORE-BEGIN
/*******************************************************************************
* Copyright (C) 2019-2020 Microchip Technology Inc. and its subsidiaries.
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

#ifndef PLIB_${I2C_INSTANCE_NAME}_SLAVE_H
#define PLIB_${I2C_INSTANCE_NAME}_SLAVE_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
/* This section lists the other files that are included in this file.
*/

#include "plib_i2c_slave_common.h"

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility

    extern "C" {

#endif
// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************

/*
 * The following functions make up the methods (set of possible operations) of
 * this interface.
 */

<#assign I2C_API_PREFIX = I2C_INSTANCE_NAME + "_">
<#if I2C_OPERATING_MODE == "Master and Slave">
<#assign I2C_API_PREFIX = I2C_INSTANCE_NAME + "_Slave">
</#if>
void ${I2C_API_PREFIX}Initialize(void);
void ${I2C_API_PREFIX}CallbackRegister(I2C_SLAVE_CALLBACK callback, uintptr_t contextHandle);
bool ${I2C_API_PREFIX}IsBusy(void);
uint8_t ${I2C_API_PREFIX}ReadByte(void);
void ${I2C_API_PREFIX}WriteByte(uint8_t wrByte);
I2C_SLAVE_TRANSFER_DIR ${I2C_API_PREFIX}TransferDirGet(void);
I2C_SLAVE_ACK_STATUS ${I2C_API_PREFIX}LastByteAckStatusGet(void);
I2C_SLAVE_ERROR ${I2C_API_PREFIX}ErrorGet(void);
<#if I2C_SMEN == true>
uint8_t ${I2C_API_PREFIX}CRCGet(void);
</#if>


// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility
}
#endif
// DOM-IGNORE-END

#endif /* PLIB_${I2C_INSTANCE_NAME}_SLAVE_H */