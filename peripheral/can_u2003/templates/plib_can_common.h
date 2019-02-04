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
Copyright (c) 2018 released Microchip Technology Inc.  All rights reserved.

Microchip licenses to you the right to use, modify, copy and distribute
Software only when embedded on a Microchip microcontroller or digital signal
controller that is integrated into your product or third party product
(pursuant to the sublicense terms in the accompanying license agreement).

You should refer to the license agreement accompanying this Software for
additional information regarding your rights and obligations.

SOFTWARE AND DOCUMENTATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND,
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
// DOM-IGNORE-END

#ifndef PLIB_CAN_COMMON_H
#define PLIB_CAN_COMMON_H

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
/* CAN Mode

   Summary:
    CAN Mode for Classic CAN and CAN FD.

   Description:
    This data type defines CAN mode Classic CAN, CAN FD without BRS(Bit rate switching)
    and CAN FD with BRS.

   Remarks:
    None.
*/
typedef enum
{
    CAN_MODE_NORMAL = 0,
    CAN_MODE_FD_WITHOUT_BRS,
    CAN_MODE_FD_WITH_BRS
} CAN_MODE;

// *****************************************************************************
/* CAN Tx Message Attribute

   Summary:
    CAN Tx Message Attribute for Tx Buffer/FIFO.

   Description:
    This data type defines CAN Tx Message Attribute. Only One attribute
    need to be passed as parameter value while invoking message transmit function.

   Remarks:
    None.
*/
typedef enum
{
    CAN_MSG_ATTR_TX_FIFO_DATA_FRAME = 0,
    CAN_MSG_ATTR_TX_FIFO_RTR_FRAME,
    CAN_MSG_ATTR_TX_BUFFER_DATA_FRAME,
    CAN_MSG_ATTR_TX_BUFFER_RTR_FRAME
} CAN_MSG_TX_ATTRIBUTE;

// *****************************************************************************
/* CAN Rx Message Attribute

   Summary:
    CAN Rx Message Attribute for Rx Buffer/FIFO0/FIFO1.

   Description:
    This data type defines CAN Rx Message Attribute. Only One attribute
    need to be passed as parameter value while invoking message receive function.

   Remarks:
    None.
*/
typedef enum
{
    CAN_MSG_ATTR_RX_FIFO0 = 0,
    CAN_MSG_ATTR_RX_FIFO1,
    CAN_MSG_ATTR_RX_BUFFER
} CAN_MSG_RX_ATTRIBUTE;

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
    CAN_ERROR_LEC_STUFF = 0x1,
    CAN_ERROR_LEC_FORM = 0x2,
    CAN_ERROR_LEC_ACK = 0x3,
    CAN_ERROR_LEC_BIT1 = 0x4,
    CAN_ERROR_LEC_BIT0 = 0x5,
    CAN_ERROR_LEC_CRC = 0x6,
    CAN_ERROR_LEC_NC = 0x7,
    CAN_ERROR_PASSIVE = 0x20,
    CAN_ERROR_WARNING_STATUS = 0x40,
    CAN_ERROR_BUS_OFF = 0x80,
    CAN_ERROR_DLEC_STUFF = 0x100,
    CAN_ERROR_DLEC_FORM = 0x200,
    CAN_ERROR_DLEC_ACK = 0x300,
    CAN_ERROR_DLEC_BIT1 = 0x400,
    CAN_ERROR_DLEC_BIT0 = 0x500,
    CAN_ERROR_DLEC_CRC = 0x600,
    CAN_ERROR_DLEC_NC = 0x700,
    CAN_ERROR_PROTOCOL_EXCEPTION_EVENT = 0x4000,
    /* Force the compiler to reserve 32-bit space for each enum value */
    CAN_ERROR_INVALID = 0xFFFFFFFF
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
    CAN_INTERRUPT_RF0N_MASK = (1U << 0U),
    CAN_INTERRUPT_RF0W_MASK = (1U << 1U),
    CAN_INTERRUPT_RF0F_MASK = (1U << 2U),
    CAN_INTERRUPT_RF0L_MASK = (1U << 3U),
    CAN_INTERRUPT_RF1N_MASK = (1U << 4U),
    CAN_INTERRUPT_RF1W_MASK = (1U << 5U),
    CAN_INTERRUPT_RF1F_MASK = (1U << 6U),
    CAN_INTERRUPT_RF1L_MASK = (1U << 7U),
    CAN_INTERRUPT_HPM_MASK = (1U << 8U),
    CAN_INTERRUPT_TC_MASK = (1U << 9U),
    CAN_INTERRUPT_TCF_MASK = (1U << 10U),
    CAN_INTERRUPT_TFE_MASK = (1U << 11U),
    CAN_INTERRUPT_TEFN_MASK = (1U << 12U),
    CAN_INTERRUPT_TEFW_MASK = (1U << 13U),
    CAN_INTERRUPT_TEFF_MASK = (1U << 14U),
    CAN_INTERRUPT_TEFL_MASK = (1U << 15U),
    CAN_INTERRUPT_TSW_MASK = (1U << 16U),
    CAN_INTERRUPT_MRAF_MASK = (1U << 17U),
    CAN_INTERRUPT_TOO_MASK = (1U << 18U),
    CAN_INTERRUPT_DRX_MASK = (1U << 19U),
    CAN_INTERRUPT_ELO_MASK = (1U << 22U),
    CAN_INTERRUPT_EP_MASK = (1U << 23U),
    CAN_INTERRUPT_EW_MASK = (1U << 24U),
    CAN_INTERRUPT_BO_MASK = (1U << 25U),
    CAN_INTERRUPT_WDI_MASK = (1U << 26U),
    CAN_INTERRUPT_PEA_MASK = (1U << 27U),
    CAN_INTERRUPT_PED_MASK = (1U << 28U),
    CAN_INTERRUPT_ARA_MASK = (1U << 29U)
}CAN_INTERRUPT_MASK;

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
/* CAN Message RAM Configuration

   Summary:
    CAN Message RAM Configuration structure.

   Description:
    This data structure defines the CAN Message RAM Base address for Rx FIFO0,
    Rx FIFO1, Rx Buffers, Tx Buffers/FIFO, Tx Event FIFO, Standard Message ID Filter and
    Extended Message ID Filter configuration.

   Remarks:
    None.
*/
typedef struct
{
    /* Rx FIFO0 base address */
    can_rxf0e_registers_t *rxFIFO0Address;

    /* Rx FIFO1 base address */
    can_rxf1e_registers_t *rxFIFO1Address;

    /* Rx Buffer base address */
    can_rxbe_registers_t *rxBuffersAddress;

    /* Tx Buffers/FIFO base address */
    can_txbe_registers_t *txBuffersAddress;

    /* Tx Event FIFO base address */
    can_txefe_registers_t *txEventFIFOAddress;

    /* Standard Message ID Filter base address */
    can_sidfe_registers_t *stdMsgIDFilterAddress;

    /* Extended Message ID Filter base address */
    can_xidfe_registers_t *extMsgIDFilterAddress;
} CAN_MSG_RAM_CONFIG;

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
    /* Tx Buffer Index */
    uint32_t txBufferIndex;

    /* Rx Message ID, buffer and size */
    uint32_t *rxId;
    uint8_t *rxBuffer;
    uint8_t *rxsize;

    /* Transfer State */
    CAN_STATE state;

    /* Transfer Event Callback */
    CAN_CALLBACK callback;

    /* Transfer Event Callback Context */
    uintptr_t context;

    /* Message RAM Configuration */
    CAN_MSG_RAM_CONFIG msgRAMConfig;

} CAN_OBJ;

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility
}
#endif
// DOM-IGNORE-END

#endif //PLIB_CAN_COMMON_H
/*******************************************************************************
 End of File
*/
