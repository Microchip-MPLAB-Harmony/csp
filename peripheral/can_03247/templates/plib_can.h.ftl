/*******************************************************************************
  CAN Peripheral Library Interface Header File

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${CAN_INSTANCE_NAME?lower_case}.h

  Summary:
    CAN PLIB interface declarations.

  Description:
    The CAN plib provides a simple interface to manage the CAN modules on
    Microchip microcontrollers. This file defines the interface declarations
    for the CAN plib.

  Remarks:
    None.

*******************************************************************************/
//DOM-IGNORE-BEGIN
/*******************************************************************************
* Copyright (C) 2019 Microchip Technology Inc. and its subsidiaries.
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
//DOM-IGNORE-END

#ifndef PLIB_${CAN_INSTANCE_NAME}_H
#define PLIB_${CAN_INSTANCE_NAME}_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

/*
 * This section lists the other files that are included in this file.
 */
#include <stdbool.h>
#include <string.h>
#include "device.h"
#include "plib_can_common.h"

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
void ${CAN_INSTANCE_NAME}_Initialize(void);
bool ${CAN_INSTANCE_NAME}_MessageTransmit(uint32_t id, uint8_t length, uint8_t* data, uint8_t fifoQueueNum, CAN_MODE mode, CAN_MSG_TX_ATTRIBUTE msgAttr);
bool ${CAN_INSTANCE_NAME}_MessageReceive(uint32_t *id, uint8_t *length, uint8_t *data, uint32_t *timestamp, uint8_t fifoNum, CAN_MSG_RX_ATTRIBUTE *msgAttr);
void ${CAN_INSTANCE_NAME}_MessageAbort(uint8_t fifoQueueNum);
void ${CAN_INSTANCE_NAME}_MessageAcceptanceFilterSet(uint8_t filterNum, uint32_t id);
uint32_t ${CAN_INSTANCE_NAME}_MessageAcceptanceFilterGet(uint8_t filterNum);
void ${CAN_INSTANCE_NAME}_MessageAcceptanceFilterMaskSet(uint8_t acceptanceFilterMaskNum, uint32_t id);
uint32_t ${CAN_INSTANCE_NAME}_MessageAcceptanceFilterMaskGet(uint8_t acceptanceFilterMaskNum);
<#if TX_EVENT_FIFO_USE == true>
bool ${CAN_INSTANCE_NAME}_TransmitEventFIFOElementGet(uint32_t *id, uint32_t *sequence, uint32_t *timestamp);
</#if>
CAN_ERROR ${CAN_INSTANCE_NAME}_ErrorGet(void);
void ${CAN_INSTANCE_NAME}_ErrorCountGet(uint8_t *txErrorCount, uint8_t *rxErrorCount);
bool ${CAN_INSTANCE_NAME}_InterruptGet(uint8_t fifoQueueNum, CAN_FIFO_INTERRUPT_FLAG_MASK fifoInterruptFlagMask);
bool ${CAN_INSTANCE_NAME}_TxFIFOQueueIsFull(uint8_t fifoQueueNum);
bool ${CAN_INSTANCE_NAME}_AutoRTRResponseSet(uint32_t id, uint8_t length, uint8_t* data, uint8_t fifoNum);
<#if CAN_INTERRUPT_MODE == true>
void ${CAN_INSTANCE_NAME}_CallbackRegister(CAN_CALLBACK callback, uintptr_t contextHandle, uint8_t fifoQueueNum);
void ${CAN_INSTANCE_NAME}_ErrorCallbackRegister(CAN_CALLBACK callback, uintptr_t contextHandle);
</#if>
// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility
    }
#endif
// DOM-IGNORE-END

#endif // PLIB_${CAN_INSTANCE_NAME}_H
