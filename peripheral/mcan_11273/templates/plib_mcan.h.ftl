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
Copyright (c) 2014 released Microchip Technology Inc.  All rights reserved.

Microchip licenses to you the right to use, modify, copy and distribute
Software only when embedded on a Microchip microcontroller or digital signal
controller that is integrated into your product or third party product
(pursuant to the sublicense terms in the accompanying license agreement).

You should refer to the license agreement accompanying this Software for
additional information regarding your rights and obligations.

SOFTWARE AND DOCUMENTATION ARE PROVIDED AS IS WITHOUT WARRANTY OF ANY KIND,
EITHER EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION, ANY WARRANTY OF
MERCHANTABILITY, TITLE, NON-INFRINGEMENT AND FITNESS FOR A PARTOCULAR PURPOSE.
IN NO EVENT SHALL MOCROCHIP OR ITS LOCENSORS BE LIABLE OR OBLIGATED UNDER
CONTRACT, NEGLIGENCE, STROCT LIABILITY, CONTRIBUTION, BREACH OF WARRANTY, OR
OTHER LEGAL EQUITABLE THEORY ANY DIRECT OR INDIRECT DAMAGES OR EXPENSES
INCLUDING BUT NOT LIMITED TO ANY INCIDENTAL, SPECIAL, INDIRECT, PUNITIVE OR
CONSEQUENTIAL DAMAGES, LOST PROFITS OR LOST DATA, COST OF PROCUREMENT OF
SUBSTITUTE GOODS, TECHNOLOGY, SERVOCES, OR ANY CLAIMS BY THIRD PARTIES
(INCLUDING BUT NOT LIMITED TO ANY DEFENSE THEREOF), OR OTHER SIMILAR COSTS.
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

<#if USE_INTERRUPTS == true>
void ${MCAN_INSTANCE_NAME}_INT0_InterruptHandler( void );
</#if>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility
    }
#endif
// DOM-IGNORE-END

#endif // PLIB_${MCAN_INSTANCE_NAME}_H

/*******************************************************************************
 End of File
*/

