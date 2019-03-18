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
/* CAN Mailbox Object Type TX Attribute

   Summary:
    CAN Mailbox TX Attribute for Transmit mailbox, Producer Tx Mailbox and
    Consumer Tx Mailbox.

   Description:
    This data type defines CAN Mailbox TX Attribute. Only One attribute
    need to be passed as parameter value while invoking message transmit function.

   Remarks:
    None.
*/
typedef enum
{
    CAN_MAILBOX_DATA_FRAME_TX = 0,
    CAN_MAILBOX_DATA_FRAME_PRODUCER,
    CAN_MAILBOX_REMOTE_FRAME_CONSUMER
} CAN_MAILBOX_TX_ATTRIBUTE;

// *****************************************************************************
/* CAN Mailbox Object Type RX Attribute

   Summary:
    CAN Mailbox RX Attribute for Reception Mailbox, Reception Mailbox
    with overwrite, Consumer Rx Mailbox and Producer Rx Mailbox.

   Description:
    This data type defines CAN Mailbox RX Attribute. Only One attribute
    need to be passed as parameter value while invoking message receive function.

   Remarks:
    None.
*/
typedef enum
{
    CAN_MAILBOX_DATA_FRAME_RX = 0,
    CAN_MAILBOX_DATA_FRAME_RX_OVERWRITE,
    CAN_MAILBOX_DATA_FRAME_CONSUMER
} CAN_MAILBOX_RX_ATTRIBUTE;

// *****************************************************************************
/* CAN Mailbox Number

   Summary:
    CAN Mailbox Number.

   Description:
    This data type defines CAN Mailbox Number 0 to 7.

   Remarks:
    None.
*/
typedef enum
{
    CAN_MAILBOX_0 = 0,
    CAN_MAILBOX_1,
    CAN_MAILBOX_2,
    CAN_MAILBOX_3,
    CAN_MAILBOX_4,
    CAN_MAILBOX_5,
    CAN_MAILBOX_6,
    CAN_MAILBOX_7
} CAN_MAILBOX_NUM;

// *****************************************************************************
/* CAN Mailbox Mask

   Summary:
    CAN Mailbox Mask.

   Description:
    This data type defines CAN Mailbox mask.

   Remarks:
    None.
*/
typedef enum
{
    CAN_MAILBOX_0_MASK = (1U << 0U),
    CAN_MAILBOX_1_MASK = (1U << 1U),
    CAN_MAILBOX_2_MASK = (1U << 2U),
    CAN_MAILBOX_3_MASK = (1U << 3U),
    CAN_MAILBOX_4_MASK = (1U << 4U),
    CAN_MAILBOX_5_MASK = (1U << 5U),
    CAN_MAILBOX_6_MASK = (1U << 6U),
    CAN_MAILBOX_7_MASK = (1U << 7U)
} CAN_MAILBOX_MASK;

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
    CAN_ERROR_BOFF = (1U << 19U),
    CAN_ERROR_CERR = (1U << 24U),
    CAN_ERROR_SERR = (1U << 25U),
    CAN_ERROR_AERR = (1U << 26U),
    CAN_ERROR_FERR = (1U << 27U),
    CAN_ERROR_BERR = (1U << 28U)
} CAN_ERROR;

// *****************************************************************************
/* CAN Interrupt Mask

   Summary:
    CAN Interrupt Mask.

   Description:
    This data type defines the CAN Interrupt sources number.

   Remarks:
    None.
*/
typedef enum
{
    CAN_INTERRUPT_MB0_MASK = (1U << 0U),
    CAN_INTERRUPT_MB1_MASK = (1U << 1U),
    CAN_INTERRUPT_MB2_MASK = (1U << 2U),
    CAN_INTERRUPT_MB3_MASK = (1U << 3U),
    CAN_INTERRUPT_MB4_MASK = (1U << 4U),
    CAN_INTERRUPT_MB5_MASK = (1U << 5U),
    CAN_INTERRUPT_MB6_MASK = (1U << 6U),
    CAN_INTERRUPT_MB7_MASK = (1U << 7U),
    CAN_INTERRUPT_ERRA_MASK = (1U << 16U),
    CAN_INTERRUPT_WARN_MASK = (1U << 17U),
    CAN_INTERRUPT_ERRP_MASK = (1U << 18U),
    CAN_INTERRUPT_BOFF_MASK = (1U << 19U),
    CAN_INTERRUPT_SLEEP_MASK = (1U << 20U),
    CAN_INTERRUPT_WAKEUP_MASK = (1U << 21U),
    CAN_INTERRUPT_TOVF_MASK = (1U << 22U),
    CAN_INTERRUPT_TSTP_MASK = (1U << 23U),
    CAN_INTERRUPT_CERR_MASK = (1U << 24U),
    CAN_INTERRUPT_SERR_MASK = (1U << 25U),
    CAN_INTERRUPT_AERR_MASK = (1U << 26U),
    CAN_INTERRUPT_FERR_MASK = (1U << 27U),
    CAN_INTERRUPT_BERR_MASK = (1U << 28U)
} CAN_INTERRUPT_MASK;

// *****************************************************************************
/* CAN Mailbox State.

   Summary:
    CAN Mailbox State.

   Description:
    This data type defines the CAN Mailbox State.
    CAN_MAILBOX_READY - Mailbox is available for Tx/Rx transfer request.
    CAN_MAILBOX_BUSY  - Mailbox is not available for Tx/Rx transfer request
                        as Mailbox is in busy state due to previous transfer request.

   Remarks:
    None.

*/
typedef enum
{
    CAN_MAILBOX_READY = 0,
    CAN_MAILBOX_BUSY
} CAN_MAILBOX_STATE;

// *****************************************************************************
/* CAN State.

   Summary:
    CAN PLib Task State.

   Description:
    This data type defines the CAN Task State.

   Remarks:
    None.

*/
typedef enum {

    /* CAN PLib Task Error State */
    CAN_STATE_ERROR = -1,

    /* CAN PLib Task Idle State */
    CAN_STATE_IDLE,

    /* CAN PLib Task Transfer Transmit State */
    CAN_STATE_TRANSFER_TRANSMIT,

    /* CAN PLib Task Transfer Receive State */
    CAN_STATE_TRANSFER_RECEIVE,

    /* CAN PLib Task Transfer Done State */
    CAN_STATE_TRANSFER_DONE

} CAN_STATE;

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
    /* Rx Message ID, buffer and size */
    uint32_t *id;
    uint8_t  *buffer;
    uint8_t  *size;
} CAN_RX_MSG;

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
    /* Rx Messages */
    CAN_RX_MSG rxMsg[CAN_MB_NUMBER];

    /* CAN Mailbox State */
    CAN_MAILBOX_STATE mbState[CAN_MB_NUMBER];

    /* Transfer State */
    CAN_STATE state;

    /* Transfer Event Callback */
    CAN_CALLBACK callback;

    /* Transfer Event Callback Context */
    uintptr_t context;

    /* CAN Error Status */
    uint32_t errorStatus;

} CAN_OBJ;

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility
}
#endif
// DOM-IGNORE-END

#endif //PLIB_CAN_COMMON_H
