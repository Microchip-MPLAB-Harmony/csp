/*******************************************************************************
  CANFD Peripheral Library Interface Header File

  Company
    Microchip Technology Inc.

  File Name
    plib_canfd_common.h

  Summary
    CANFD peripheral library interface.

  Description
    This file defines the interface to the CANFD peripheral library. This
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

#ifndef PLIB_CANFD_COMMON_H
#define PLIB_CANFD_COMMON_H

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

// *****************************************************************************
/* CANFD Mode

   Summary:
    CANFD Mode for Classic CAN and CAN FD.

   Description:
    This data type defines CANFD mode Classic CAN, CAN FD without BRS(Bit rate switching)
    and CAN FD with BRS.

   Remarks:
    None.
*/
typedef enum
{
    CANFD_MODE_NORMAL = 0,
    CANFD_MODE_FD_WITHOUT_BRS,
    CANFD_MODE_FD_WITH_BRS
} CANFD_MODE;

// *****************************************************************************
/* CANFD Tx Message Attribute

   Summary:
    CANFD Tx Message Attribute for Tx FIFO and Tx Queue.

   Description:
    This data type defines CANFD Message TX Attribute for Data Frame and Remote Frame.
    Only One attribute need to be passed as parameter value while invoking
    message transmit function.

   Remarks:
    None.
*/
typedef enum
{
    CANFD_MSG_TX_DATA_FRAME = 0,
    CANFD_MSG_TX_REMOTE_FRAME
} CANFD_MSG_TX_ATTRIBUTE;

// *****************************************************************************
/* CANFD Message Object Type RX Attribute

   Summary:
    CANFD Message RX Attribute for Data Frame and Remote Frame.

   Description:
    This data type defines CANFD Message RX Attribute for Data Frame and Remote Frame.

   Remarks:
    None.
*/
typedef enum
{
    CANFD_MSG_RX_DATA_FRAME = 0,
    CANFD_MSG_RX_REMOTE_FRAME
} CANFD_MSG_RX_ATTRIBUTE;

// *****************************************************************************
/* CANFD FIFO Interrupt Status Flag Mask

   Summary:
    CANFD FIFO Interrupt Status Flag Mask.

   Description:
    This data type defines the CANFD FIFO Interrupt Status Flag Mask.

   Remarks:
    None.
*/
typedef enum
{
    /* Receive FIFO Not Empty / Transmit FIFO Not Full Interrupt Mask */
    CANFD_FIFO_INTERRUPT_TFNRFNIF_MASK = 0x1,

    /* Transmit FIFO Half Empty / Receive FIFO Half Full Interrupt Mask */
    CANFD_FIFO_INTERRUPT_TFHRFHIF_MASK = 0x2,

    /* Transmit FIFO Empty / Receive FIFO Full Interrupt Mask */
    CANFD_FIFO_INTERRUPT_TFERFFIF_MASK = 0x4,

    /* Receive FIFO Overflow Interrupt Mask */
    CANFD_FIFO_INTERRUPT_RXOVIF_MASK = 0x8,

    /* Transmit Attempts Exhausted Interrupt Pending Mask */
    CANFD_FIFO_INTERRUPT_TXATIF_MASK = 0x10
} CANFD_FIFO_INTERRUPT_FLAG_MASK;

// *****************************************************************************
/* CANFD Transfer Error

   Summary:
    CANFD Transfer Error data type.

   Description:
    This data type defines the CANFD Transfer Error.

   Remarks:
    None.
*/
typedef enum
{
    CANFD_ERROR_NONE = 0x0,
    CANFD_ERROR_TX_RX_WARNING_STATE = 0x10000,
    CANFD_ERROR_RX_WARNING_STATE = 0x20000,
    CANFD_ERROR_TX_WARNING_STATE = 0x40000,
    CANFD_ERROR_RX_BUS_PASSIVE_STATE = 0x80000,
    CANFD_ERROR_TX_BUS_PASSIVE_STATE = 0x100000,
    CANFD_ERROR_TX_BUS_OFF_STATE = 0x200000
} CANFD_ERROR;

// *****************************************************************************
/* CANFD Callback

   Summary:
    CANFD Callback Function Pointer.

   Description:
    This data type defines the CANFD Callback Function Pointer.

   Remarks:
    None.
*/
typedef void (*CANFD_CALLBACK) (uintptr_t contextHandle);

// *****************************************************************************
/* CANFD RX Message

   Summary:
    CANFD RX Message Buffer structure.

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
    uint32_t *timestamp;
    /* Rx Message attribute */
    CANFD_MSG_RX_ATTRIBUTE *msgAttr;
} CANFD_RX_MSG;

// *****************************************************************************
/* CANFD Receive Message Object

   Summary:
    CANFD Receive Message Object structure.

   Description:
    This data structure defines the CANFD Rx Message Object format.

   Remarks:
    None.
*/
typedef struct
{
    /* CANFD Rx message - SID[10:0] and EID[28:11]  */
    uint32_t r0;

    /* CANFD Rx message - DLC[3:0], IDE[4], RTR[5], BRS[6], FDF[7]
                          ESI[8] and FILHIT[15:11]    */
    uint32_t r1;

    /* CANFD Rx message - RXMSGTS and Receive Buffer Data Bytes */
    uint8_t data[];
} CANFD_RX_MSG_OBJECT;

// *****************************************************************************
/* CANFD Trasmit Message Object

   Summary:
    CANFD Transmit Message Object structure.

   Description:
    This data structure defines the CANFD Tx Message Object format.

   Remarks:
    None.
*/
typedef struct
{
    /* CANFD Tx message - SID[10:0] and EID[28:11] */
    uint32_t t0;

    /* CANFD Tx message - DLC[3:0], IDE[4], RTR[5], BRS[6], FDF[7]
                          ESI[8] and SEQ[31:9] */
    uint32_t t1;

    /* CANFD Tx message - Transmit Buffer Data Bytes */
    uint8_t data[];
} CANFD_TX_MSG_OBJECT;

// *****************************************************************************
/* CANFD Trasmit Event FIFO Element

   Summary:
    CANFD Trasmit Event FIFO Element structure.

   Description:
    This data structure defines the CANFD Tx Event FIFO Element format.

   Remarks:
    None.
*/
typedef struct
{
    /* CANFD Tx Event FIFO - SID[10:0] and EID[28:11] */
    uint32_t te0;

    /* CANFD Tx Event FIFO - DLC[3:0], IDE[4], RTR[5], BRS[6], FDF[7]
                             ESI[8] and SEQ[31:9] */
    uint32_t te1;

    /* CANFD Tx Event FIFO - Transmit Message Time Stamp */
    uint8_t timestamp[];
} CANFD_TX_EVENT_FIFO_ELEMENT;

// *****************************************************************************
/* CANFD Callback Object

   Summary:
    CANFD transfer event callback structure.

   Description:
    This data structure stores transfer event callback and it's context.

   Remarks:
    None.
*/
typedef struct
{
    /* Transfer Event Callback */
    CANFD_CALLBACK callback;

    /* Transfer Event Callback Context */
    uintptr_t context;
} CANFD_CALLBACK_OBJ;

// *****************************************************************************
/* CANFD PLib Instance Object

   Summary:
    CANFD PLib Object structure.

   Description:
    This data structure defines the CANFD PLib Instance Object.

   Remarks:
    None.
*/
typedef struct
{
    /* CANFD Error Status */
    uint32_t errorStatus;
} CANFD_OBJ;

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility
}
#endif
// DOM-IGNORE-END

#endif //PLIB_CANFD_COMMON_H
