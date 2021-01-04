/*******************************************************************************
  Serial Communication Interface Inter-Integrated Circuit (SERCOM I2C) Library
  Instance Header File

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${SERCOM_INSTANCE_NAME?lower_case}_i2c.h

  Summary:
    SERCOM I2C PLIB Header file

  Description:
    This file defines the interface to the SERCOM I2C peripheral library. This
    library provides access to and control of the associated peripheral
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

#ifndef PLIB_${SERCOM_INSTANCE_NAME}_I2C_H
#define PLIB_${SERCOM_INSTANCE_NAME}_I2C_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
/* This section lists the other files that are included in this file.
*/

#include "plib_sercom_i2c_master_common.h"

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

void ${SERCOM_INSTANCE_NAME}_I2C_Initialize(void);

bool ${SERCOM_INSTANCE_NAME}_I2C_Read(uint16_t address, uint8_t* rdData, uint32_t rdLength);

bool ${SERCOM_INSTANCE_NAME}_I2C_Write(uint16_t address, uint8_t* wrData, uint32_t wrLength);

bool ${SERCOM_INSTANCE_NAME}_I2C_WriteRead(uint16_t address, uint8_t* wrData, uint32_t wrLength, uint8_t* rdData, uint32_t rdLength);

bool ${SERCOM_INSTANCE_NAME}_I2C_IsBusy(void);

SERCOM_I2C_ERROR ${SERCOM_INSTANCE_NAME}_I2C_ErrorGet(void);

void ${SERCOM_INSTANCE_NAME}_I2C_CallbackRegister(SERCOM_I2C_CALLBACK callback, uintptr_t contextHandle);

bool ${SERCOM_INSTANCE_NAME}_I2C_TransferSetup(SERCOM_I2C_TRANSFER_SETUP* setup, uint32_t srcClkFreq );

<#if (I2CM_MODE?? && I2CM_MODE = "HIGH_SPEED_MODE")>
bool ${SERCOM_INSTANCE_NAME}_I2C_Read_HighSpeed(uint16_t address, uint8_t* rdData, uint32_t rdLength);

bool ${SERCOM_INSTANCE_NAME}_I2C_Write_HighSpeed(uint16_t address, uint8_t* wrData, uint32_t wrLength);

bool ${SERCOM_INSTANCE_NAME}_I2C_WriteRead_HighSpeed(uint16_t address, uint8_t* wrData, uint32_t wrLength, uint8_t* rdData, uint32_t rdLength);
</#if>


// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility
}
#endif
// DOM-IGNORE-END

#endif /* PLIB_${SERCOM_INSTANCE_NAME}_I2C_H */
