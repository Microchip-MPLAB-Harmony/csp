/*******************************************************************************
  CAN Driver Interface Declarations for Static Single Instance Driver

  Company:
    Microchip Technology Inc.

  File Name:
    drv_can.h

  Summary:
    CAN driver interface declarations for the static single instance driver.

  Description:
    The CAN device driver provides a simple interface to manage the CAN module on
    Microchip microcontrollers. This file defines the interface Declarations for the
    CAN driver.

  Remarks:
    Static interfaces incorporate the driver instance number within the names
    of the routines, eliminating the need for an object ID or object handle.

    Static single-open interfaces also eliminate the need for the open handle.
*******************************************************************************/

//DOM-IGNORE-BEGIN
/*******************************************************************************
Copyright (c) 2015 released Microchip Technology Inc.  All rights reserved.

Microchip licenses to you the right to use, modify, copy and distribute
Software only when embedded on a Microchip microcontroller or digital signal
controller that is integrated into your product or third party product
(pursuant to the sublicense terms in the accompanying license agreement).

You should refer to the license agreement accompanying this Software for
additional information regarding your rights and obligations.

SOFTWARE AND DOCUMENTATION ARE PROVIDED AS IS WITHOUT WARRANTY OF ANY KIND,
EITHER EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION, ANY WARRANTY OF
MERCHANTABILITY, TITLE, NON-INFRINGEMENT AND FITNESS FOR A PARTICULAR PURPOSE.
IN NO EVENT SHALL MICROCHIP OR ITS LICENSORS BE LIABLE OR OBLIGATED UNDER
CONTRACT, NEGLIGENCE, STRICT LIABILITY, CONTRIBUTION, BREACH OF WARRANTY, OR
OTHER LEGAL EQUITABLE THEORY ANY DIRECT OR INDIRECT DAMAGES OR EXPENSES
INCLUDING BUT NOT LIMITED TO ANY INCIDENTAL, SPECIAL, INDIRECT, PUNITIVE OR
CONSEQUENTIAL DAMAGES, LOST PROFITS OR LOST DATA, COST OF PROCUREMENT OF
SUBSTITUTE GOODS, TECHNOLOGY, SERVICES, OR ANY CLAIMS BY THIRD PARTIES
(INCLUDING BUT NOT LIMITED TO ANY DEFENSE THEREOF), OR OTHER SIMILAR COSTS.
*******************************************************************************/
//DOM-IGNORE-END
#ifndef _DRV_CAN_H
#define _DRV_CAN_H

// *****************************************************************************
// *****************************************************************************
// Section: Data Types
// *****************************************************************************
// *****************************************************************************
#include <stdint.h>
#include <stdbool.h>
#include "system_config.h"
#include "system/system.h"
#include "driver/driver.h"
#if defined(__PIC32C__)
#include "peripheral/can/processor/can_processor.h"
#else
#include "peripheral/can/plib_can.h"
#endif

// *****************************************************************************
/* CAN Driver Module Index Numbers

  Summary:
    CAN driver index definitions.

  Description:
    These constants provide CAN Driver index definitions.

  Remarks:
    These constants should be used in place of hard-coded numeric literals.

    These values should be passed into the DRV_CAN_Initialize and
    DRV_CAN_Open routines to identify the driver instance in use.
*/

#define DRV_CAN_INDEX_0         0
#define DRV_CAN_INDEX_1         1
#define DRV_CAN_INDEX_2         2
#define DRV_CAN_INDEX_3         3

// *****************************************************************************
// *****************************************************************************
// Section: System Interface Routines
// *****************************************************************************
// *****************************************************************************
// *****************************************************************************
/* Function:
    SYS_MODULE_OBJ DRV_CAN_Initialize( const SYS_MODULE_INDEX        index,
                                        const SYS_MODULE_INIT * const init )

  Summary:
    Initializes the CAN instance for the specified driver index.
    <p><b>Implementation:</b> Static</p>

  Description:
    This routine initializes the CAN Driver instance for the specified driver
    instance, making it ready for clients to use it. The initialization
    routine is specified by the MHC parameters.

  Precondition:
    None.

  Parameters:
    drvIndex        - Index for the driver instance to be initialized

    init            - Pointer to a data structure containing any data necessary
                      to initialize the driver. This pointer may be null if no
                      data is required because static overrides have been
                      provided.

  Returns:
    If successful, returns a valid handle to a driver object.  Otherwise, it
    returns SYS_MODULE_OBJ_INVALID. The returned object must be passed as
    argument to DRV_SAMPLE_Reinitialize, DRV_SAMPLE_Deinitialize, DRV_SAMPLE_Tasks and
    DRV_SAMPLE_Status functions.

  Remarks:
    This routine must be called before any other CAN routine is called.
    This routine should only be called once during system initialization.
*/
SYS_MODULE_OBJ DRV_CAN_Initialize( const SYS_MODULE_INDEX        index,
                                    const SYS_MODULE_INIT * const init );

// *****************************************************************************
/* Function:
    void DRV_CAN_Deinitialize ( SYS_MODULE_OBJ object )

  Summary:
    Deinitializes the DRV_CAN_Initialize instance that has been called for the
	specified driver index.
    <p><b>Implementation:</b> Static</p>

  Description:
    This routine deinitializes the CAN Driver instance for the specified driver
    instance, making it ready for clients to use it. The initialization
    routine is specified by the MHC parameters.

  Precondition:
    None.

  Parameters:
    None.

  Returns:
    None.

  Remarks:

*/
void DRV_CAN_Deinitialize( SYS_MODULE_OBJ object );

// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines - Client Level
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Function:
    DRV_HANDLE DRV_CAN_Open( const SYS_MODULE_INDEX drvIndex,
                             const DRV_IO_INTENT    intent )

  Summary:
    Opens the CAN instance for the specified driver index.
    <p><b>Implementation:</b> Static</p>

  Description:
    This routine opens the CAN Driver instance for the specified driver
    instance, making it ready for clients to use it.

  Precondition:
    DRV_CAN_Initialize has been called.

  Parameters:
    None.

  Returns:
    None.

  Remarks:

*/
DRV_HANDLE DRV_CAN_Open( const SYS_MODULE_INDEX drvIndex,
                         const DRV_IO_INTENT    intent );

// *****************************************************************************
/* Function:
    void DRV_CAN_Close( DRV_HANDLE handle )

  Summary:
    Closes the CAN instance for the specified driver index.
    <p><b>Implementation:</b> Static</p>

  Description:
    This routine closes the CAN driver instance for the specified driver
    instance, making it ready for clients to use it.

  Precondition:
    DRV_CAN_Initialize has been called.

  Parameters:
    handle       - A valid open-instance handle, returned from the driver's
                   open function
  Returns:
    If successful, the function returns a valid open-instance handle (a number
    identifying both the caller and the module instance).

    If an error occurs, the return value is DRV_HANDLE_INVALID.

  Remarks:

*/
void DRV_CAN_Close( DRV_HANDLE handle );

// *****************************************************************************
/* Function:
     bool DRV_CAN_ChannelMessageTransmit(DRV_HANDLE handle, CAN_CHANNEL channelNum, int address,
                                         uint8_t DLC, uint8_t* message);

  Summary:
    Transmits a message on a channel for the specified driver index.
    <p><b>Implementation:</b> Static</p>

  Description:
    This routine transmits a data buffer on the CAN bus according to the channel,
	address, and data length given.

  Precondition:
    DRV_CAN_Initialize has been called.

  Parameters:
    CAN_CHANNEL channelNum - CAN channel to use
    int         address    - CAN address to transmit on
    uint8_t     DLC        - Data Length Code of Message
    uint8_t*    message    - Pointer to the message data to send

  Returns:
    Boolean "true" when a message has been transmitted.

  Remarks:
    This routine receives a standard or extended messages based upon the CAN
	Driver setup.
*/
bool DRV_CAN_ChannelMessageTransmit(DRV_HANDLE handle, CAN_CHANNEL channelNum, int address,
                                    uint8_t DLC, uint8_t* message);

// *****************************************************************************
/* Function:
     bool DRV_CAN_ChannelMessageReceive(DRV_HANDLE handle, CAN_CHANNEL channelNum, int address,
                                        uint8_t DLC, uint8_t* message);

  Summary:
    Receives a message on a channel for the specified driver index.
    <p><b>Implementation:</b> Static</p>

  Description:
   This routine receives data into a buffer from the CAN bus according to the
   channel, address, and data length given.

  Precondition:
    DRV_CAN_Initialize has been called.

  Parameters:
    CAN_CHANNEL channelNum - CAN channel to use
    int         address    - CAN address to receive on
    uint8_t     DLC        - Data Length Code of Message
    uint8_t*    message    - Pointer to put the message data to receive

  Returns:
    * true  - When a message has been received
    * false - When a message has not been received

  Remarks:
    This routine receives a standard or extended messages based upon the CAN
	Driver setup.
*/
bool DRV_CAN_ChannelMessageReceive(DRV_HANDLE handle, CAN_CHANNEL channelNum, int address,
                                   uint8_t DLC, uint8_t* message);

#ifdef DRV_CAN_DRIVER_MODE_STATIC
#include "framework/driver/can/drv_can_static.h"
#endif

#endif // #ifndef _DRV_CAN_H
/*******************************************************************************
 End of File
*/
