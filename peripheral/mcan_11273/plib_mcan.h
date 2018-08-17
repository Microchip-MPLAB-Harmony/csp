/*******************************************************************************
  MCAN PLIB Interface Header File

  Company:
    Microchip Technology Inc.

  File Name:
    plib_mcan.h

  Summary:
    MCAN peripheral library interface.

  Description:
    The MCAN PLIB provides a simple interface to manage the MCAN module on
    Microchip microcontrollers. This file defines the interface declarations for
    the MCAN peripheral instance.

  Remarks:
    None.
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
#ifndef PLIB_MCANx_H
#define PLIB_MCANx_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

/*  This section lists the other files that are included in this file.
*/

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
/*  The following data type definitions are used by the functions in this 
    interface and should be considered part it.
*/
// *****************************************************************************

// *****************************************************************************
// *****************************************************************************
// Section: System Interface Routines
// *****************************************************************************
// *****************************************************************************
// *****************************************************************************
/* Function:
    void MCANx_Initialize (void)

  Summary:
    Initializes given instance of the MCAN peripheral.

  Description:
     This function initializes the given instance of the MCAN peripheral as
     configured in MCC.

  Precondition:
    None.

  Parameters:
    None.

  Returns:
    None.

  Example:
    <code>
    MCAN0_Initialize();
    </code>

  Remarks:
    None.
*/
void MCANx_Initialize (void);

// *****************************************************************************
/* Function:
    void MCANx_Deinitialize (void)

  Summary:
    TBD

  Description:
    TBD.

  Precondition:
    None.

  Parameters:
    None.

  Returns:
    None.

  Example:
    <code>
    MCANx_Deinitialize();
    </code>

  Remarks:
    None.

*/
void MCANx_Deinitialize (void);

// *****************************************************************************
/* Function:
    void MCANx_Open (void)

  Summary:
    TBD.

  Description:
    TBD.

  Precondition:
    MCANx_Initialize has been called.

  Parameters:
    None.

  Returns:
    None.

  Remarks:
    None.

*/
void MCANx_Open (void);

// *****************************************************************************
/* Function:
    void MCANx_Close (void)

  Summary:
    TBD

  Description:
    TBD

  Precondition:
    MCANx_Initialize has been called.

  Parameters:
    None.

  Returns:
    None.

  Remarks:
    None.
*/
    void MCANx_Close (void)

// *****************************************************************************
/* Function:
     bool MCANx_ChannelMessageTransmit (MCAN_CHANNEL channelNum, int address, 
                                        uint8_t DLC, uint8_t* message);

  Summary:
    Transmits a message on a channel for the specified MCAN index.
    <p><b>Implementation:</b> Static</p>

  Description:
    This routine transmits a data buffer on the MCAN bus according to the 
    channel, address, and data length given.

  Precondition:
    MCANx_Initialize has been called.

  Parameters:
    MCAN_CHANNEL channelNum - MCAN channel to use
    int          address    - MCAN address to transmit on
    uint8_t      DLC        - Data Length Code of Message
    uint8_t*     message    - Pointer to the message data to send

  Returns:
    Boolean "true" when a message has been transmitted.

  Remarks:
    This routine receives a standard or extended messages based upon the CAN
	plib setup.
*/
bool MCANx_ChannelMessageTransmit (MCAN_CHANNEL channelNum, int address, uint8_t DLC, uint8_t* message);

// *****************************************************************************
/* Function:
     bool MCANx_ChannelMessageReceive (MCAN_CHANNEL channelNum, int address, 
                                       uint8_t DLC, uint8_t* message);

  Summary:
    Receives a message on a channel for the specified plib index.
    <p><b>Implementation:</b> Static</p>

  Description:
   This routine receives data into a buffer from the MCAN bus according to the
   channel, address, and data length given.

  Precondition:
    MCANx_Initialize has been called.

  Parameters:
    MCAN_CHANNEL channelNum - MCAN channel to use
    int          address    - MCAN address to receive on
    uint8_t      DLC        - Data Length Code of Message
    uint8_t*     message    - Pointer to put the message data to receive
 
  Returns:
    true  - When a message has been received
    false - When a message has not been received

  Remarks:
    This routine receives a standard or extended messages based upon the MCAN
	Driver setup.
*/
bool MCANx_ChannelMessageReceive (MCAN_CHANNEL channelNum, int address, uint8_t DLC, uint8_t* message);

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END

#endif // #ifndef PLIB_MCANx_H
/*******************************************************************************
 End of File
*/
