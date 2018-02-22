/*******************************************************************************
  CAN Driver Interface Declarations for Static Single Instance Driver

  Company:
    Microchip Technology Inc.

  File Name:
    drv_can${INDEX}.h

  Summary:
    CAN driver interface declarations for the static single instance driver.

  Description:
    The CAN device driver provides a simple interface to manage the CAN
    modules on Microchip microcontrollers. This file defines the interface
    Declarations for the CAN driver.

  Remarks:
    Static interfaces incorporate the driver instance number within the names
    of the routines, eliminating the need for an object ID or object handle.

    Static single-open interfaces also eliminate the need for the open handle.
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

#ifndef _DRV_CAN${INDEX}_H_
#define _DRV_CAN${INDEX}_H_

#include "peripheral/mcan/drv_can_local.h"


#ifdef __cplusplus
extern "C" {
#endif

// *****************************************************************************
// *****************************************************************************
// Section: Interface Headers for Instance ${INDEX} for the static driver
// *****************************************************************************
// *****************************************************************************
void DRV_CAN${INDEX}_Initialize(void);
void DRV_CAN${INDEX}_Deinitialize(void);
void DRV_CAN${INDEX}_Open(void);
void DRV_CAN${INDEX}_Close(void);
bool DRV_CAN${INDEX}_ChannelMessageTransmit(CAN_CHANNEL channelNum, int address, uint8_t DLC, uint8_t* message);
bool DRV_CAN${INDEX}_ChannelMessageReceive(CAN_CHANNEL channelNum, int address, uint8_t DLC, uint8_t* message);

#ifdef __cplusplus
}
#endif

#endif

/*******************************************************************************
 End of File
*/

