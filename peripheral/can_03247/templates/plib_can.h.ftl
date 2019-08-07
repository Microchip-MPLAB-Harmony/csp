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

<#-- Message memory configuration -->
<#assign MESSAGE_RAM_SIZE = 0>
<#assign NUMBER_OF_RX_FIFO = 0>
<#if TX_EVENT_FIFO_USE == true>
    <#if CAN_TIMESTAMP_ENABLE == true>
        <#assign MESSAGE_RAM_SIZE = MESSAGE_RAM_SIZE + (TX_EVENT_FIFO_MESSAGE_BUFFER * 12)>
    <#else>
        <#assign MESSAGE_RAM_SIZE = MESSAGE_RAM_SIZE + (TX_EVENT_FIFO_MESSAGE_BUFFER * 8)>
    </#if>
</#if>
<#if TX_QUEUE_USE == true>
    <#if TX_QUEUE_PAYLOAD_SIZE?keep_after("0x")?number < 5>
        <#assign TX_QUEUE_OBJECT_SIZE = 16 + TX_QUEUE_PAYLOAD_SIZE?keep_after("0x")?number * 4>
    <#else>
        <#assign TX_QUEUE_OBJECT_SIZE = 40 + 16 * (TX_QUEUE_PAYLOAD_SIZE?keep_after("0x")?number - 5)>
    </#if>
    <#assign MESSAGE_RAM_SIZE = MESSAGE_RAM_SIZE + (TX_QUEUE_MESSAGE_BUFFER * TX_QUEUE_OBJECT_SIZE)>
</#if>
<#list 1..NUMBER_OF_FIFO as fifo>
    <#assign TX_FIFO_ENABLE = CAN_INSTANCE_NAME + "_FIFO" + fifo + "_TXEN">
    <#assign FIFO_PAYLOAD_SIZE = CAN_INSTANCE_NAME + "_FIFO" + fifo + "_PAYLOAD_SIZE">
    <#assign FIFO_MESSAGE_BUFFER_NUM = CAN_INSTANCE_NAME + "_FIFO" + fifo + "_SIZE">
    <#if .vars[TX_FIFO_ENABLE] == "0x1">
        <#if .vars[FIFO_PAYLOAD_SIZE]?keep_after("0x")?number < 5>
            <#assign TX_FIFO_OBJECT_SIZE = 16 + .vars[FIFO_PAYLOAD_SIZE]?keep_after("0x")?number * 4>
        <#else>
            <#assign TX_FIFO_OBJECT_SIZE = 40 + 16 * (.vars[FIFO_PAYLOAD_SIZE]?keep_after("0x")?number - 5)>
        </#if>
        <#assign MESSAGE_RAM_SIZE = MESSAGE_RAM_SIZE + (.vars[FIFO_MESSAGE_BUFFER_NUM] * TX_FIFO_OBJECT_SIZE)>
    <#else>
        <#assign NUMBER_OF_RX_FIFO += 1>
        <#if .vars[FIFO_PAYLOAD_SIZE]?keep_after("0x")?number < 5>
            <#if CAN_TIMESTAMP_ENABLE == true>
                <#assign RX_FIFO_OBJECT_SIZE = 20 + .vars[FIFO_PAYLOAD_SIZE]?keep_after("0x")?number * 4>
            <#else>
                <#assign RX_FIFO_OBJECT_SIZE = 16 + .vars[FIFO_PAYLOAD_SIZE]?keep_after("0x")?number * 4>
            </#if>
        <#else>
            <#if CAN_TIMESTAMP_ENABLE == true>
                <#assign RX_FIFO_OBJECT_SIZE = 44 + 16 * (.vars[FIFO_PAYLOAD_SIZE]?keep_after("0x")?number - 5)>
            <#else>
                <#assign RX_FIFO_OBJECT_SIZE = 40 + 16 * (.vars[FIFO_PAYLOAD_SIZE]?keep_after("0x")?number - 5)>
            </#if>
        </#if>
        <#assign MESSAGE_RAM_SIZE = MESSAGE_RAM_SIZE + (.vars[FIFO_MESSAGE_BUFFER_NUM] * RX_FIFO_OBJECT_SIZE)>
    </#if>
</#list>
/* ${CAN_INSTANCE_NAME} Message memory size */
#define CAN_MESSAGE_RAM_CONFIG_SIZE ${MESSAGE_RAM_SIZE}
/* Number of configured FIFO */
#define CAN_NUM_OF_FIFO             ${NUMBER_OF_FIFO}
/* Maximum number of CAN Message buffers in each FIFO */
#define CAN_FIFO_MESSAGE_BUFFER_MAX 32

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
bool ${CAN_INSTANCE_NAME}_MessageReceive(uint32_t *id, uint8_t *length, uint8_t *data, uint32_t *timestamp, uint8_t fifoNum);
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
<#if CAN_INTERRUPT_MODE == true>
bool ${CAN_INSTANCE_NAME}_IsBusy(void);
void ${CAN_INSTANCE_NAME}_CallbackRegister(CAN_CALLBACK callback, uintptr_t contextHandle);
</#if>
// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility
    }
#endif
// DOM-IGNORE-END

#endif // PLIB_${CAN_INSTANCE_NAME}_H
