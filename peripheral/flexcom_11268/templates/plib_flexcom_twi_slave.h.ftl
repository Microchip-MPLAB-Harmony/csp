/*******************************************************************************
  FLEXCOM TWI Peripheral Library Interface Header File

  Company
    Microchip Technology Inc.

  File Name
    plib_${FLEXCOM_INSTANCE_NAME?lower_case}_twi_slave.h

  Summary
    FLEXCOM TWI Slave peripheral library interface.

  Description
    This file defines the interface to the FLEXCOM TWI peripheral library.  This
    library provides access to and control of the associated peripheral
    instance.

  Remarks:

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

#ifndef PLIB_${FLEXCOM_INSTANCE_NAME}_TWI_SLAVE_H
#define PLIB_${FLEXCOM_INSTANCE_NAME}_TWI_SLAVE_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

#include "plib_flexcom_twi_slave_common.h"

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    extern "C" {

#endif
// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************
/* The following functions make up the methods (set of possible operations) of
   this interface.
*/

void ${FLEXCOM_INSTANCE_NAME}_TWI_Initialize( void );

uint8_t ${FLEXCOM_INSTANCE_NAME}_TWI_ReadByte(void);

void ${FLEXCOM_INSTANCE_NAME}_TWI_WriteByte(uint8_t wrByte);

FLEXCOM_TWI_SLAVE_TRANSFER_DIR ${FLEXCOM_INSTANCE_NAME}_TWI_TransferDirGet(void);

FLEXCOM_TWI_SLAVE_ACK_STATUS ${FLEXCOM_INSTANCE_NAME}_TWI_LastByteAckStatusGet(void);

void ${FLEXCOM_INSTANCE_NAME}_TWI_NACKDataPhase(bool isNACKEnable);

<#if TWI_INTERRUPT_MODE == true>

void ${FLEXCOM_INSTANCE_NAME}_TWI_CallbackRegister(FLEXCOM_TWI_SLAVE_CALLBACK callback, uintptr_t contextHandle);

bool ${FLEXCOM_INSTANCE_NAME}_TWI_IsBusy(void);

<#else>

FLEXCOM_TWI_SLAVE_STATUS_FLAG ${FLEXCOM_INSTANCE_NAME}_TWI_StatusGet(void);

</#if>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END

#endif //PLIB_${FLEXCOM_INSTANCE_NAME}_TWI_SLAVE_H
