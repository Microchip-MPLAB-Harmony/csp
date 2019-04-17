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
// Section: Data Types
// *****************************************************************************
// *****************************************************************************
/* ${CAN_INSTANCE_NAME} Message RAM Configuration Size */
<#assign CAN_MESSAGE_RAM_CONFIG_SIZE = 0>
<#if RXF0_USE>
  <#assign RXF0_BYTES_CFG = RXF0_BYTES_CFG!0>
  <#if RXF0_BYTES_CFG?number < 5>
    <#assign RXF0_ELEMENT_BYTES = 16 + RXF0_BYTES_CFG?number * 4>
  <#else>
    <#assign RXF0_ELEMENT_BYTES = 40 + 16 * (RXF0_BYTES_CFG?number - 5)>
  </#if>
  <#assign RX_FIFO0_SIZE = RXF0_ELEMENTS * RXF0_ELEMENT_BYTES>
  <#lt>#define ${CAN_INSTANCE_NAME}_RX_FIFO0_ELEMENT_SIZE       ${RXF0_ELEMENT_BYTES}
  <#lt>#define ${CAN_INSTANCE_NAME}_RX_FIFO0_SIZE               ${RX_FIFO0_SIZE}
  <#assign CAN_MESSAGE_RAM_CONFIG_SIZE = CAN_MESSAGE_RAM_CONFIG_SIZE + RX_FIFO0_SIZE>
</#if>
<#if RXF1_USE>
  <#assign RXF1_BYTES_CFG = RXF1_BYTES_CFG!0>
  <#if RXF1_BYTES_CFG?number < 5>
    <#assign RXF1_ELEMENT_BYTES = 16 + RXF1_BYTES_CFG?number * 4>
  <#else>
    <#assign RXF1_ELEMENT_BYTES = 40 + 16 * (RXF1_BYTES_CFG?number - 5)>
  </#if>
  <#assign RX_FIFO1_SIZE = RXF1_ELEMENTS * RXF1_ELEMENT_BYTES>
  <#lt>#define ${CAN_INSTANCE_NAME}_RX_FIFO1_ELEMENT_SIZE       ${RXF1_ELEMENT_BYTES}
  <#lt>#define ${CAN_INSTANCE_NAME}_RX_FIFO1_SIZE               ${RX_FIFO1_SIZE}
  <#assign CAN_MESSAGE_RAM_CONFIG_SIZE = CAN_MESSAGE_RAM_CONFIG_SIZE + RX_FIFO1_SIZE>
</#if>
<#if RXBUF_USE>
  <#assign RX_BUFFER_BYTES_CFG = RX_BUFFER_BYTES_CFG!0>
  <#if RX_BUFFER_BYTES_CFG?number < 5>
    <#assign RX_BUFFER_ELEMENT_BYTES = 16 + RX_BUFFER_BYTES_CFG?number * 4>
  <#else>
    <#assign RX_BUFFER_ELEMENT_BYTES = 40 + 16 * (RX_BUFFER_BYTES_CFG?number - 5)>
  </#if>
  <#assign RX_BUFFER_SIZE = RX_BUFFER_ELEMENTS * RX_BUFFER_ELEMENT_BYTES>
  <#lt>#define ${CAN_INSTANCE_NAME}_RX_BUFFER_ELEMENT_SIZE      ${RX_BUFFER_ELEMENT_BYTES}
  <#lt>#define ${CAN_INSTANCE_NAME}_RX_BUFFER_SIZE              ${RX_BUFFER_SIZE}
  <#assign CAN_MESSAGE_RAM_CONFIG_SIZE = CAN_MESSAGE_RAM_CONFIG_SIZE + RX_BUFFER_SIZE>
</#if>
<#if TX_USE || TXBUF_USE>
  <#assign TX_FIFO_BYTES_CFG = TX_FIFO_BYTES_CFG!0>
  <#if TX_FIFO_BYTES_CFG?number < 5>
    <#assign TX_ELEMENT_BYTES = 16 + TX_FIFO_BYTES_CFG?number * 4>
  <#else>
    <#assign TX_ELEMENT_BYTES = 40 + 16 * (TX_FIFO_BYTES_CFG?number - 5)>
  </#if>
  <#if TXBUF_USE>
    <#assign TX_FIFO_BUFFER_ELEMENTS = TX_FIFO_ELEMENTS + TX_BUFFER_ELEMENTS>
  <#else>
    <#assign TX_FIFO_BUFFER_ELEMENTS = TX_FIFO_ELEMENTS>
  </#if>
  <#assign TX_FIFO_BUFFER_SIZE = TX_FIFO_BUFFER_ELEMENTS * TX_ELEMENT_BYTES>
  <#lt>#define ${CAN_INSTANCE_NAME}_TX_FIFO_BUFFER_ELEMENT_SIZE ${TX_ELEMENT_BYTES}
  <#lt>#define ${CAN_INSTANCE_NAME}_TX_FIFO_BUFFER_SIZE         ${TX_FIFO_BUFFER_SIZE}
  <#assign TX_EVENT_FIFO_SIZE = TX_FIFO_BUFFER_ELEMENTS * 8>
  <#lt>#define ${CAN_INSTANCE_NAME}_TX_EVENT_FIFO_SIZE          ${TX_EVENT_FIFO_SIZE}
  <#assign CAN_MESSAGE_RAM_CONFIG_SIZE = CAN_MESSAGE_RAM_CONFIG_SIZE + TX_FIFO_BUFFER_SIZE + TX_EVENT_FIFO_SIZE>
</#if>
<#if FILTERS_STD?number gt 0>
  <#assign STD_MSG_ID_FILTER_SIZE = FILTERS_STD * 4>
  <#lt>#define ${CAN_INSTANCE_NAME}_STD_MSG_ID_FILTER_SIZE      ${STD_MSG_ID_FILTER_SIZE}
  <#assign CAN_MESSAGE_RAM_CONFIG_SIZE = CAN_MESSAGE_RAM_CONFIG_SIZE + STD_MSG_ID_FILTER_SIZE>
</#if>
<#if FILTERS_EXT?number gt 0>
  <#assign EXT_MSG_ID_FILTER_SIZE = FILTERS_EXT * 8>
  <#lt>#define ${CAN_INSTANCE_NAME}_EXT_MSG_ID_FILTER_SIZE      ${EXT_MSG_ID_FILTER_SIZE}
  <#assign CAN_MESSAGE_RAM_CONFIG_SIZE = CAN_MESSAGE_RAM_CONFIG_SIZE + EXT_MSG_ID_FILTER_SIZE>
</#if>

/* ${CAN_INSTANCE_NAME}_MESSAGE_RAM_CONFIG_SIZE to be used by application or driver
   for allocating buffer from non-cached contiguous memory */
#define ${CAN_INSTANCE_NAME}_MESSAGE_RAM_CONFIG_SIZE     ${CAN_MESSAGE_RAM_CONFIG_SIZE}

// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************
void ${CAN_INSTANCE_NAME}_Initialize (void);
bool ${CAN_INSTANCE_NAME}_MessageTransmit(uint32_t id, uint8_t length, uint8_t* data, CAN_MODE mode, CAN_MSG_TX_ATTRIBUTE msgAttr);
bool ${CAN_INSTANCE_NAME}_MessageReceive(uint32_t *id, uint8_t *length, uint8_t *data, CAN_MSG_RX_ATTRIBUTE msgAttr);
CAN_ERROR ${CAN_INSTANCE_NAME}_ErrorGet(void);
bool ${CAN_INSTANCE_NAME}_InterruptGet(CAN_INTERRUPT_MASK interruptMask);
void ${CAN_INSTANCE_NAME}_InterruptClear(CAN_INTERRUPT_MASK interruptMask);
void ${CAN_INSTANCE_NAME}_MessageRAMConfigSet(uint8_t *msgRAMConfigBaseAddress);
<#if FILTERS_STD?number gt 0>
bool ${CAN_INSTANCE_NAME}_StandardFilterElementSet(uint8_t filterNumber, can_sidfe_registers_t *stdMsgIDFilterElement);
bool ${CAN_INSTANCE_NAME}_StandardFilterElementGet(uint8_t filterNumber, can_sidfe_registers_t *stdMsgIDFilterElement);
</#if>
<#if FILTERS_EXT?number gt 0>
bool ${CAN_INSTANCE_NAME}_ExtendedFilterElementSet(uint8_t filterNumber, can_xidfe_registers_t *extMsgIDFilterElement);
bool ${CAN_INSTANCE_NAME}_ExtendedFilterElementGet(uint8_t filterNumber, can_xidfe_registers_t *extMsgIDFilterElement);
</#if>
<#if INTERRUPT_MODE == true>
bool ${CAN_INSTANCE_NAME}_IsBusy(void);
void ${CAN_INSTANCE_NAME}_CallbackRegister(CAN_CALLBACK callback, uintptr_t contextHandle);
</#if>
// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility
    }
#endif
// DOM-IGNORE-END

#endif // PLIB_${CAN_INSTANCE_NAME}_H

/*******************************************************************************
 End of File
*/
