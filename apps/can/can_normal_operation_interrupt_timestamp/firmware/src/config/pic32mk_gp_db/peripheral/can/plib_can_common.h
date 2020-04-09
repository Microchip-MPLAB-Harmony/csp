/*******************************************************************************
  CAN Peripheral Library Interface Header File

  Company
    Microchip Technology Inc.

  File Name
    plib_can_common.h

  Summary
    CAN peripheral library interface.

  Description
    This file defines the interface to the CAN peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

  Remarks:

*******************************************************************************/

// DOM-IGNORE-BEGIN
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
// DOM-IGNORE-END

#ifndef PLIB_CAN_COMMON_H
#define PLIB_CAN_COMMON_H

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    extern "C" {

#endif
// DOM-IGNORE-END

// *****************************************************************************
/* CAN Message Object Type TX Attribute

   Summary:
    CAN Message TX Attribute for Data Frame and Remote Frame.

   Description:
    This data type defines CAN Message TX Attribute for Data Frame and Remote Frame.
    Only One attribute need to be passed as parameter value while invoking
    message transmit function.

   Remarks:
    None.
*/
typedef enum
{
    CAN_MSG_TX_DATA_FRAME = 0,
    CAN_MSG_TX_REMOTE_FRAME
} CAN_MSG_TX_ATTRIBUTE;

// *****************************************************************************
/* CAN Message Object Type RX Attribute

   Summary:
    CAN Message RX Attribute for Data Frame and Remote Frame.

   Description:
    This data type defines CAN Message RX Attribute for Data Frame and Remote Frame.

   Remarks:
    None.
*/
typedef enum
{
    CAN_MSG_RX_DATA_FRAME = 0,
    CAN_MSG_RX_REMOTE_FRAME
} CAN_MSG_RX_ATTRIBUTE;

// *****************************************************************************
/* CAN FIFO Interrupt Status Flag Mask

   Summary:
    CAN FIFO Interrupt Status Flag Mask.

   Description:
    This data type defines the CAN FIFO Interrupt Status Flag Mask.

   Remarks:
    None.
*/
typedef enum
{
    CAN_FIFO_INTERRUPT_RXNEMPTYIF_MASK = 0x1,
    CAN_FIFO_INTERRUPT_RXHALFIF_MASK = 0x2,
    CAN_FIFO_INTERRUPT_RXFULLIF_MASK = 0x4,
    CAN_FIFO_INTERRUPT_RXOVFLIF_MASK = 0x8,
    CAN_FIFO_INTERRUPT_TXEMPTYIF_MASK = 0x100,
    CAN_FIFO_INTERRUPT_TXHALFIF_MASK = 0x200,
    CAN_FIFO_INTERRUPT_TXNFULLIF_MASK = 0x400
} CAN_FIFO_INTERRUPT_FLAG_MASK;

// *****************************************************************************
/* CAN Transfer Error

   Summary:
    CAN Transfer Error data type.

   Description:
    This data type defines the CAN Transfer Error.

   Remarks:
    None.
*/
typedef enum
{
    CAN_ERROR_NONE = 0x0,
    CAN_ERROR_TX_RX_WARNING_STATE = 0x10000,
    CAN_ERROR_RX_WARNING_STATE = 0x20000,
    CAN_ERROR_TX_WARNING_STATE = 0x40000,
    CAN_ERROR_RX_BUS_PASSIVE_STATE = 0x80000,
    CAN_ERROR_TX_BUS_PASSIVE_STATE = 0x100000,
    CAN_ERROR_TX_BUS_OFF_STATE = 0x200000
} CAN_ERROR;

// *****************************************************************************
/* CAN Callback

   Summary:
    CAN Callback Function Pointer.

   Description:
    This data type defines the CAN Callback Function Pointer.

   Remarks:
    None.
*/
typedef void (*CAN_CALLBACK) (uintptr_t contextHandle);

// *****************************************************************************
/* CAN RX Message

   Summary:
    CAN RX Message Buffer structure.

   Description:
    This data structure stores RX Message.

   Remarks:
    None.
*/
typedef struct
{
    /* Rx Message ID */
    uint32_t *id;
    /* Rx Message buffer */
    uint8_t  *buffer;
    /* Rx Message size */
    uint8_t  *size;
    /* Rx Message timestamp */
    uint16_t *timestamp;
    /* Rx Message attribute */
    CAN_MSG_RX_ATTRIBUTE *msgAttr;
} CAN_RX_MSG;

// *****************************************************************************
/* CAN Message Buffer

   Summary:
    CAN Message Buffer structure.

   Description:
    This data structure defines the CAN TX and RX Message Buffer format.

   Remarks:
    None.
*/
typedef struct
{
    /* This is SID portion of the CAN message */
    uint32_t msgSID;

    /* This is EID portion of the CAN message */
    uint32_t msgEID;

    /* This is the data portion of the CAN message */
    uint8_t msgData[8];
} CAN_TX_RX_MSG_BUFFER;

// *****************************************************************************
/* CAN Callback Object

   Summary:
    CAN transfer event callback structure.

   Description:
    This data structure stores transfer event callback and it's context.

   Remarks:
    None.
*/
typedef struct
{
    /* Transfer Event Callback */
    CAN_CALLBACK callback;

    /* Transfer Event Callback Context */
    uintptr_t context;
} CAN_CALLBACK_OBJ;

// *****************************************************************************
/* CAN PLib Instance Object

   Summary:
    CAN PLib Object structure.

   Description:
    This data structure defines the CAN PLib Instance Object.

   Remarks:
    None.
*/
typedef struct
{
    /* CAN Error Status */
    uint32_t errorStatus;

} CAN_OBJ;

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility
}
#endif
// DOM-IGNORE-END

#endif //PLIB_CAN_COMMON_H
