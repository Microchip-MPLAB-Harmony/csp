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
/* CAN Message Object Type RX Frame Attribute

   Summary:
    CAN Message RX Frame Attribute for Data Frame and Remote Frame.

   Description:
    This data type defines CAN Message RX Frame Attribute for Data Frame and Remote Frame.

   Remarks:
    None.
*/
typedef enum
{
    CAN_MSG_RX_DATA_FRAME = 0,
    CAN_MSG_RX_REMOTE_FRAME
} CAN_MSG_RX_FRAME_ATTRIBUTE;

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
    uint32_t *rxId;
    /* Rx Message buffer */
    uint8_t *rxBuffer;
    /* Rx Message size */
    uint8_t *rxsize;
    /* Rx Message timestamp */
    uint16_t *timestamp;
    /* Rx Message frame attribute */
    CAN_MSG_RX_FRAME_ATTRIBUTE *msgFrameAttr;
} CAN_RX_MSG;

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
    /* Tx Buffer Index */
    uint32_t txBufferIndex;
    /* Rx Buffer Index */
    uint32_t rxBufferIndex1;
    uint32_t rxBufferIndex2;

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
