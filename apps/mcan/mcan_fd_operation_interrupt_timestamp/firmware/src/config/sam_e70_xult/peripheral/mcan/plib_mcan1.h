/*******************************************************************************
  MCAN Peripheral Library Interface Header File

  Company:
    Microchip Technology Inc.

  File Name:
    plib_mcan1.h

  Summary:
    MCAN PLIB interface declarations.

  Description:
    The MCAN plib provides a simple interface to manage the MCAN modules on
    Microchip microcontrollers. This file defines the interface declarations
    for the MCAN plib.

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

#ifndef PLIB_MCAN1_H
#define PLIB_MCAN1_H

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
#include "plib_mcan_common.h"

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
/* MCAN1 Message RAM Configuration Size */
#define MCAN1_RX_FIFO0_ELEMENT_SIZE       72
#define MCAN1_RX_FIFO0_SIZE               72
#define MCAN1_RX_FIFO1_ELEMENT_SIZE       72
#define MCAN1_RX_FIFO1_SIZE               72
#define MCAN1_RX_BUFFER_ELEMENT_SIZE      72
#define MCAN1_RX_BUFFER_SIZE              72
#define MCAN1_TX_FIFO_BUFFER_ELEMENT_SIZE 72
#define MCAN1_TX_FIFO_BUFFER_SIZE         72
#define MCAN1_TX_EVENT_FIFO_SIZE          8
#define MCAN1_STD_MSG_ID_FILTER_SIZE      8
#define MCAN1_EXT_MSG_ID_FILTER_SIZE      16

/* MCAN1_MESSAGE_RAM_CONFIG_SIZE to be used by application or driver
   for allocating buffer from non-cached contiguous memory */
#define MCAN1_MESSAGE_RAM_CONFIG_SIZE     320

// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************
void MCAN1_Initialize (void);
bool MCAN1_MessageTransmit(uint32_t id, uint8_t length, uint8_t* data, MCAN_MODE mode, MCAN_MSG_TX_ATTRIBUTE msgAttr);
bool MCAN1_MessageReceive(uint32_t *id, uint8_t *length, uint8_t *data, uint16_t *timestamp,
                                          MCAN_MSG_RX_ATTRIBUTE msgAttr, MCAN_MSG_RX_FRAME_ATTRIBUTE *msgFrameAttr);
bool MCAN1_TransmitEventFIFOElementGet(uint32_t *id, uint8_t *messageMarker, uint16_t *timestamp);
MCAN_ERROR MCAN1_ErrorGet(void);
void MCAN1_ErrorCountGet(uint8_t *txErrorCount, uint8_t *rxErrorCount);
bool MCAN1_InterruptGet(MCAN_INTERRUPT_MASK interruptMask);
void MCAN1_InterruptClear(MCAN_INTERRUPT_MASK interruptMask);
bool MCAN1_TxFIFOIsFull(void);
void MCAN1_MessageRAMConfigSet(uint8_t *msgRAMConfigBaseAddress);
bool MCAN1_StandardFilterElementSet(uint8_t filterNumber, mcan_sidfe_registers_t *stdMsgIDFilterElement);
bool MCAN1_StandardFilterElementGet(uint8_t filterNumber, mcan_sidfe_registers_t *stdMsgIDFilterElement);
bool MCAN1_ExtendedFilterElementSet(uint8_t filterNumber, mcan_xidfe_registers_t *extMsgIDFilterElement);
bool MCAN1_ExtendedFilterElementGet(uint8_t filterNumber, mcan_xidfe_registers_t *extMsgIDFilterElement);
void MCAN1_TxCallbackRegister(MCAN_CALLBACK callback, uintptr_t contextHandle);
void MCAN1_RxCallbackRegister(MCAN_CALLBACK callback, uintptr_t contextHandle, MCAN_MSG_RX_ATTRIBUTE msgAttr);
// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility
    }
#endif
// DOM-IGNORE-END

#endif // PLIB_MCAN1_H

/*******************************************************************************
 End of File
*/
