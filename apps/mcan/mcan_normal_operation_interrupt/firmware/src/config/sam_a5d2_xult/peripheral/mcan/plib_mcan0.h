/*******************************************************************************
  MCAN Peripheral Library Interface Header File

  Company:
    Microchip Technology Inc.

  File Name:
    plib_mcan0.h

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

#ifndef PLIB_MCAN0_H
#define PLIB_MCAN0_H

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
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************
void MCAN0_Initialize (void);
bool MCAN0_MessageTransmit(uint32_t address, uint8_t length, uint8_t* data, MCAN_MODE mode, MCAN_MSG_TX_ATTRIBUTE msgAttr);
bool MCAN0_MessageReceive(uint32_t *address, uint8_t *length, uint8_t *data, MCAN_MSG_RX_ATTRIBUTE msgAttr);
MCAN_ERROR MCAN0_ErrorGet(void);
bool MCAN0_InterruptGet(MCAN_INTERRUPT_MASK interruptMask);
void MCAN0_InterruptClear(MCAN_INTERRUPT_MASK interruptMask);
void MCAN0_MessageRAMConfigGet(MCAN_MSG_RAM_CONFIG *msgRAMConfig);
bool MCAN0_IsBusy(void);
void MCAN0_CallbackRegister(MCAN_CALLBACK callback, uintptr_t contextHandle);
// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility
    }
#endif
// DOM-IGNORE-END

#endif // PLIB_MCAN0_H

/*******************************************************************************
 End of File
*/
