/*******************************************************************************
  MCAN Peripheral Library (PLIB) header
  
  Company:
    Microchip Technology Inc.

  File Name:
    plib_${MCAN_INSTANCE_NAME?lower_case}.h

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

#ifndef PLIB_${MCAN_INSTANCE_NAME}_H
#define PLIB_${MCAN_INSTANCE_NAME}_H

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
// Section: Interface
// *****************************************************************************
// *****************************************************************************

<#assign USE_INTERRUPTS =
    (INT_RXF0_NEW_ENTRY!false) ||
    (INT_RXF0_WATERMARK!false) ||
    (INT_RXF1_NEW_ENTRY!false) ||
    (INT_RXF1_WATERMARK!false) ||
    (INT_TX_COMPLETED!false)   ||
    (INT_TX_FIFO_EMPTY!false)  ||
    (INT_TX_FIFO_WATERMARK!false) ||
    (INT_TIMEOUT!false)
>

void ${MCAN_INSTANCE_NAME}_Initialize (void);
void ${MCAN_INSTANCE_NAME}_Deinitialize (void);
void ${MCAN_INSTANCE_NAME}_Open (void);
void ${MCAN_INSTANCE_NAME}_Close (void);
bool ${MCAN_INSTANCE_NAME}_ChannelMessageTransmit (MCAN_CHANNEL channelNum, int address, uint8_t DLC, uint8_t* message);
bool ${MCAN_INSTANCE_NAME}_ChannelMessageReceive (MCAN_CHANNEL channelNum, int address, uint8_t DLC, uint8_t* message);


// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility
    }
#endif
// DOM-IGNORE-END

#endif // PLIB_${MCAN_INSTANCE_NAME}_H

/*******************************************************************************
 End of File
*/

