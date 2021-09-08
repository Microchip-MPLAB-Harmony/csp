/*******************************************************************************
  MCAN Peripheral Library Interface Header File

  Company
    Microchip Technology Inc.

  File Name
    plib_mcan_common.h

  Summary
    MCAN peripheral library interface.

  Description
    This file defines the interface to the MCAN peripheral library. This
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

#ifndef PLIB_MCAN_COMMON_H
#define PLIB_MCAN_COMMON_H

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
/* MCAN Mode

   Summary:
    MCAN Mode for Classic CAN and CAN FD.

   Description:
    This data type defines MCAN mode Classic CAN, CAN FD without BRS(Bit rate switching)
    and CAN FD with BRS.

   Remarks:
    None.
*/
typedef enum
{
    MCAN_MODE_NORMAL = 0,
    MCAN_MODE_FD_WITHOUT_BRS,
    MCAN_MODE_FD_WITH_BRS
} MCAN_MODE;

// *****************************************************************************
/* MCAN Tx Message Attribute

   Summary:
    MCAN Tx Message Attribute for Tx Buffer/FIFO.

   Description:
    This data type defines MCAN Tx Message Attribute. Only One attribute
    need to be passed as parameter value while invoking message transmit function.

   Remarks:
    None.
*/
typedef enum
{
    MCAN_MSG_ATTR_TX_FIFO_DATA_FRAME = 0,
    MCAN_MSG_ATTR_TX_FIFO_RTR_FRAME,
    MCAN_MSG_ATTR_TX_BUFFER_DATA_FRAME,
    MCAN_MSG_ATTR_TX_BUFFER_RTR_FRAME
} MCAN_MSG_TX_ATTRIBUTE;

// *****************************************************************************
/* MCAN Rx Message Attribute

   Summary:
    MCAN Rx Message Attribute for Rx Buffer/FIFO0/FIFO1.

   Description:
    This data type defines MCAN Rx Message Attribute. Only One attribute
    need to be passed as parameter value while invoking message receive function.

   Remarks:
    None.
*/
typedef enum
{
    MCAN_MSG_ATTR_RX_FIFO0 = 0,
    MCAN_MSG_ATTR_RX_FIFO1,
    MCAN_MSG_ATTR_RX_BUFFER
} MCAN_MSG_RX_ATTRIBUTE;

// *****************************************************************************
/* MCAN Message Object Type RX Frame Attribute

   Summary:
    MCAN Message RX Frame Attribute for Data Frame and Remote Frame.

   Description:
    This data type defines MCAN Message RX Frame Attribute for Data Frame and Remote Frame.

   Remarks:
    None.
*/
typedef enum
{
    MCAN_MSG_RX_DATA_FRAME = 0,
    MCAN_MSG_RX_REMOTE_FRAME
} MCAN_MSG_RX_FRAME_ATTRIBUTE;

// *****************************************************************************
/* MCAN Transfer Error

   Summary:
    MCAN Transfer Error data type.

   Description:
    This data type defines the MCAN Transfer Error.

   Remarks:
    None.
*/
typedef enum
{
    MCAN_ERROR_NONE = 0x0,
    MCAN_ERROR_LEC_STUFF = 0x1,
    MCAN_ERROR_LEC_FORM = 0x2,
    MCAN_ERROR_LEC_ACK = 0x3,
    MCAN_ERROR_LEC_BIT1 = 0x4,
    MCAN_ERROR_LEC_BIT0 = 0x5,
    MCAN_ERROR_LEC_CRC = 0x6,
    MCAN_ERROR_LEC_NO_CHANGE = 0x7,
    MCAN_ERROR_PASSIVE = 0x20,
    MCAN_ERROR_WARNING_STATUS = 0x40,
    MCAN_ERROR_BUS_OFF = 0x80,
    MCAN_ERROR_DLEC_STUFF = 0x100,
    MCAN_ERROR_DLEC_FORM = 0x200,
    MCAN_ERROR_DLEC_ACK = 0x300,
    MCAN_ERROR_DLEC_BIT1 = 0x400,
    MCAN_ERROR_DLEC_BIT0 = 0x500,
    MCAN_ERROR_DLEC_CRC = 0x600,
    MCAN_ERROR_DLEC_NO_CHANGE = 0x700,
    MCAN_ERROR_PROTOCOL_EXCEPTION_EVENT = 0x4000,
    /* Force the compiler to reserve 32-bit space for each enum value */
    MCAN_ERROR_INVALID = 0xFFFFFFFF
} MCAN_ERROR;

// *****************************************************************************
/* MCAN Interrupt Mask

   Summary:
    MCAN Interrupt Mask.

   Description:
    This data type defines the MCAN Interrupt sources number.

   Remarks:
    None.
*/
typedef enum
{
    MCAN_INTERRUPT_RF0N_MASK = (1U << 0U),
    MCAN_INTERRUPT_RF0W_MASK = (1U << 1U),
    MCAN_INTERRUPT_RF0F_MASK = (1U << 2U),
    MCAN_INTERRUPT_RF0L_MASK = (1U << 3U),
    MCAN_INTERRUPT_RF1N_MASK = (1U << 4U),
    MCAN_INTERRUPT_RF1W_MASK = (1U << 5U),
    MCAN_INTERRUPT_RF1F_MASK = (1U << 6U),
    MCAN_INTERRUPT_RF1L_MASK = (1U << 7U),
    MCAN_INTERRUPT_HPM_MASK = (1U << 8U),
    MCAN_INTERRUPT_TC_MASK = (1U << 9U),
    MCAN_INTERRUPT_TCF_MASK = (1U << 10U),
    MCAN_INTERRUPT_TFE_MASK = (1U << 11U),
    MCAN_INTERRUPT_TEFN_MASK = (1U << 12U),
    MCAN_INTERRUPT_TEFW_MASK = (1U << 13U),
    MCAN_INTERRUPT_TEFF_MASK = (1U << 14U),
    MCAN_INTERRUPT_TEFL_MASK = (1U << 15U),
    MCAN_INTERRUPT_TSW_MASK = (1U << 16U),
    MCAN_INTERRUPT_MRAF_MASK = (1U << 17U),
    MCAN_INTERRUPT_TOO_MASK = (1U << 18U),
    MCAN_INTERRUPT_DRX_MASK = (1U << 19U),
    MCAN_INTERRUPT_ELO_MASK = (1U << 22U),
    MCAN_INTERRUPT_EP_MASK = (1U << 23U),
    MCAN_INTERRUPT_EW_MASK = (1U << 24U),
    MCAN_INTERRUPT_BO_MASK = (1U << 25U),
    MCAN_INTERRUPT_WDI_MASK = (1U << 26U),
    MCAN_INTERRUPT_PEA_MASK = (1U << 27U),
    MCAN_INTERRUPT_PED_MASK = (1U << 28U),
    MCAN_INTERRUPT_ARA_MASK = (1U << 29U)
}MCAN_INTERRUPT_MASK;

// *****************************************************************************
/* MCAN Callback

   Summary:
    MCAN Callback Function Pointer.

   Description:
    This data type defines the MCAN Callback Function Pointer.

   Remarks:
    None.
*/
typedef void (*MCAN_CALLBACK) (uintptr_t contextHandle);

// *****************************************************************************
/* MCAN Message RAM Configuration

   Summary:
    MCAN Message RAM Configuration structure.

   Description:
    This data structure defines the MCAN Message RAM Base address for Rx FIFO0,
    Rx FIFO1, Rx Buffers, Tx Buffers/FIFO, Tx Event FIFO, Standard Message ID Filter and
    Extended Message ID Filter configuration.

   Remarks:
    None.
*/
typedef struct
{
    /* Rx FIFO0 base address */
    mcan_rxf0e_registers_t *rxFIFO0Address;

    /* Rx FIFO1 base address */
    mcan_rxf1e_registers_t *rxFIFO1Address;

    /* Rx Buffer base address */
    mcan_rxbe_registers_t *rxBuffersAddress;

    /* Tx Buffers/FIFO base address */
    mcan_txbe_registers_t *txBuffersAddress;

    /* Tx Event FIFO base address */
    mcan_txefe_registers_t *txEventFIFOAddress;

    /* Standard Message ID Filter base address */
    mcan_sidfe_registers_t *stdMsgIDFilterAddress;

    /* Extended Message ID Filter base address */
    mcan_xidfe_registers_t *extMsgIDFilterAddress;
} MCAN_MSG_RAM_CONFIG;

// *****************************************************************************
/* MCAN RX Message

   Summary:
    MCAN RX Message Buffer structure.

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
    MCAN_MSG_RX_FRAME_ATTRIBUTE *msgFrameAttr;
} MCAN_RX_MSG;

// *****************************************************************************
/* MCAN Callback Object

   Summary:
    MCAN transfer event callback structure.

   Description:
    This data structure stores transfer event callback and it's context.

   Remarks:
    None.
*/
typedef struct
{
    /* Transfer Event Callback */
    MCAN_CALLBACK callback;

    /* Transfer Event Callback Context */
    uintptr_t context;
} MCAN_CALLBACK_OBJ;

// *****************************************************************************
/* MCAN PLib Instance Object

   Summary:
    MCAN PLib Object structure.

   Description:
    This data structure defines the MCAN PLib Instance Object.

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
    MCAN_MSG_RAM_CONFIG msgRAMConfig;

} MCAN_OBJ;

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility
}
#endif
// DOM-IGNORE-END

#endif //PLIB_MCAN_COMMON_H
/*******************************************************************************
 End of File
*/
