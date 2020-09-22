/*******************************************************************************
  TWIHS Peripheral Library Interface Header File

  Company
    Microchip Technology Inc.

  File Name
    plib_${TWIHS_INSTANCE_NAME?lower_case}_slave.h

  Summary
    TWIHS Slave peripheral library interface.

  Description
    This file defines the interface to the TWIHS peripheral library.  This
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

#ifndef PLIB_${TWIHS_INSTANCE_NAME}_SLAVE_H
#define PLIB_${TWIHS_INSTANCE_NAME}_SLAVE_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

#include "plib_twihs_slave_common.h"

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

void ${TWIHS_INSTANCE_NAME}_Initialize( void );

uint8_t ${TWIHS_INSTANCE_NAME}_ReadByte(void);

void ${TWIHS_INSTANCE_NAME}_WriteByte(uint8_t wrByte);

TWIHS_SLAVE_TRANSFER_DIR ${TWIHS_INSTANCE_NAME}_TransferDirGet(void);

TWIHS_SLAVE_ACK_STATUS ${TWIHS_INSTANCE_NAME}_LastByteAckStatusGet(void);

void ${TWIHS_INSTANCE_NAME}_NACKDataPhase(bool isNACKEnable);

<#if TWIHS_INTERRUPT_MODE = true>

void ${TWIHS_INSTANCE_NAME}_CallbackRegister(TWIHS_SLAVE_CALLBACK callback, uintptr_t contextHandle);

bool ${TWIHS_INSTANCE_NAME}_IsBusy(void);

<#else>

TWIHS_SLAVE_STATUS_FLAG ${TWIHS_INSTANCE_NAME}_StatusGet(void);

</#if>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END

#endif //PLIB_${TWIHS_INSTANCE_NAME}_SLAVE_H
