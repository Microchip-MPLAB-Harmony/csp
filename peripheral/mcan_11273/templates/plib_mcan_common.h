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
// Section: Preprocessor macros
// *****************************************************************************
// *****************************************************************************

 // *****************************************************************************
/* MCAN Transfer Errors

   Summary:
    MCAN Transfer Error macros.

   Description:
    Helper macros to identify MCAN errors.

   Remarks:
    None.
*/

#define MCAN_ERROR_NONE                      0x0U
#define MCAN_ERROR_LEC_STUFF                 0x1U
#define MCAN_ERROR_LEC_FORM                  0x2U
#define MCAN_ERROR_LEC_ACK                   0x3U
#define MCAN_ERROR_LEC_BIT1                  0x4U
#define MCAN_ERROR_LEC_BIT0                  0x5U
#define MCAN_ERROR_LEC_CRC                   0x6U
#define MCAN_ERROR_LEC_NO_CHANGE             0x7U
#define MCAN_ERROR_PASSIVE                   0x20U
#define MCAN_ERROR_WARNING_STATUS            0x40U
#define MCAN_ERROR_BUS_OFF                   0x80U
#define MCAN_ERROR_DLEC_STUFF                0x100U
#define MCAN_ERROR_DLEC_FORM                 0x200U
#define MCAN_ERROR_DLEC_ACK                  0x300U
#define MCAN_ERROR_DLEC_BIT1                 0x400U
#define MCAN_ERROR_DLEC_BIT0                 0x500U
#define MCAN_ERROR_DLEC_CRC                  0x600U
#define MCAN_ERROR_DLEC_NO_CHANGE            0x700U
#define MCAN_ERROR_PROTOCOL_EXCEPTION_EVENT  0x4000U
#define MCAN_ERROR_INVALID                   0xFFFFFFFFU

// *****************************************************************************
// *****************************************************************************
// Section: Data Types
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* MCAN Rx FIFO Number

   Summary:
    MCAN Rx FIFO Number.

   Description:
    This data type defines MCAN Rx FIFO number for Rx FIFO0 and FIFO1.

   Remarks:
    None.
*/
typedef enum
{
    MCAN_RX_FIFO_0 = 0U,
    MCAN_RX_FIFO_1
} MCAN_RX_FIFO_NUM;

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
    MCAN_INTERRUPT_RF0N_MASK = (1UL << 0U),
    MCAN_INTERRUPT_RF0W_MASK = (1UL << 1U),
    MCAN_INTERRUPT_RF0F_MASK = (1UL << 2U),
    MCAN_INTERRUPT_RF0L_MASK = (1UL << 3U),
    MCAN_INTERRUPT_RF1N_MASK = (1UL << 4U),
    MCAN_INTERRUPT_RF1W_MASK = (1UL << 5U),
    MCAN_INTERRUPT_RF1F_MASK = (1UL << 6U),
    MCAN_INTERRUPT_RF1L_MASK = (1UL << 7U),
    MCAN_INTERRUPT_HPM_MASK = (1UL << 8U),
    MCAN_INTERRUPT_TC_MASK = (1UL << 9U),
    MCAN_INTERRUPT_TCF_MASK = (1UL << 10U),
    MCAN_INTERRUPT_TFE_MASK = (1UL << 11U),
    MCAN_INTERRUPT_TEFN_MASK = (1UL << 12U),
    MCAN_INTERRUPT_TEFW_MASK = (1UL << 13U),
    MCAN_INTERRUPT_TEFF_MASK = (1UL << 14U),
    MCAN_INTERRUPT_TEFL_MASK = (1UL << 15U),
    MCAN_INTERRUPT_TSW_MASK = (1UL << 16U),
    MCAN_INTERRUPT_MRAF_MASK = (1UL << 17U),
    MCAN_INTERRUPT_TOO_MASK = (1UL << 18U),
    MCAN_INTERRUPT_DRX_MASK = (1UL << 19U),
    MCAN_INTERRUPT_ELO_MASK = (1UL << 22U),
    MCAN_INTERRUPT_EP_MASK = (1UL << 23U),
    MCAN_INTERRUPT_EW_MASK = (1UL << 24U),
    MCAN_INTERRUPT_BO_MASK = (1UL << 25U),
    MCAN_INTERRUPT_WDI_MASK = (1UL << 26U),
    MCAN_INTERRUPT_PEA_MASK = (1UL << 27U),
    MCAN_INTERRUPT_PED_MASK = (1UL << 28U),
    MCAN_INTERRUPT_ARA_MASK = (1UL << 29U)
}MCAN_INTERRUPT_MASK;

// *****************************************************************************
/* MCAN Transfer Error

   Summary:
    MCAN Transfer Error data type.

   Description:
    This data type defines the MCAN Transfer Error.

   Remarks:
    None.
*/
typedef uint32_t MCAN_ERROR;

// *****************************************************************************
/* MCAN Tx FIFO Callback

   Summary:
    MCAN Callback Function Pointer for Tx FIFO.

   Description:
    This data type defines the MCAN Callback Function Pointer for Tx FIFO.

   Remarks:
    None.
*/
typedef void (*MCAN_TX_FIFO_CALLBACK) (uintptr_t contextHandle);

// *****************************************************************************
/* MCAN TX/RX Buffers Callback

   Summary:
    MCAN Callback Function Pointer for TX/RX Buffers.

   Description:
    This data type defines the MCAN Callback Function Pointer for TX/RX Buffers.

   Remarks:
    None.
*/
typedef void (*MCAN_TXRX_BUFFERS_CALLBACK) (uint8_t bufferNumber, uintptr_t contextHandle);

// *****************************************************************************
/* MCAN Tx Event FIFO Callback

   Summary:
    MCAN Callback Function Pointer for Tx Event FIFO.

   Description:
    This data type defines the MCAN Callback Function Pointer for Tx Event FIFO.

   Remarks:
    None.
*/
typedef void (*MCAN_TX_EVENT_FIFO_CALLBACK) (uint8_t numberOfTxEvent, uintptr_t contextHandle);

// *****************************************************************************
/* MCAN Rx FIFO0/FIFO1 Callback

   Summary:
    MCAN Callback Function Pointer for Rx FIFO0/FIFO1.

   Description:
    This data type defines the MCAN Callback Function Pointer for Rx FIFO0/FIFO1.

   Remarks:
    None.
*/
typedef void (*MCAN_RX_FIFO_CALLBACK) (uint8_t numberOfMessage, uintptr_t contextHandle);

// *****************************************************************************
/* MCAN Callback

   Summary:
    MCAN Callback Function Pointer.

   Description:
    This data type defines the MCAN Callback Function Pointer.

   Remarks:
    None.
*/
typedef void (*MCAN_CALLBACK) (uint32_t interruptStatus, uintptr_t contextHandle);

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
/* MCAN Rx Buffer and FIFO Element

   Summary:
    MCAN Rx Buffer and FIFO Element Structure.

   Description:
    This data structure defines MCAN Rx Buffer and FIFO Element.

   Remarks:
    None.
*/
typedef struct
{
    /* Identifier */
    uint32_t id:29;
    /* Remote Transmission Request */
    uint32_t rtr:1;
    /* Extended Identifier */
    uint32_t xtd:1;
    /* Error State Indicator */
    uint32_t esi:1;

    /* Rx Timestamp */
    uint32_t rxts:16;
    /* Data Length Code */
    uint32_t dlc:4;
    /* Bit Rate Switching */
    uint32_t brs:1;
    /* FD Format */
    uint32_t fdf:1;
    /* Reserved */
    uint32_t :2;
    /* Filter Index */
    uint32_t fidx:7;
    /* Accepted Non-matching Frame */
    uint32_t anmf:1;

    /* Data field */
    uint8_t data[8];

} MCAN_RX_BUFFER;

// *****************************************************************************
/* MCAN Tx Buffer Element

   Summary:
    MCAN Tx Buffer Element Structure.

   Description:
    This data structure defines MCAN Tx Buffer Element.

   Remarks:
    None.
*/
typedef struct
{
    /* Identifier */
    uint32_t id:29;
    /* Remote Transmission Request */
    uint32_t rtr:1;
    /* Extended Identifier */
    uint32_t xtd:1;
    /* Error State Indicator */
    uint32_t esi:1;

    /* Reserved */
    uint32_t :16;
    /* Data Length Code */
    uint32_t dlc:4;
    /* Bit Rate Switching */
    uint32_t brs:1;
    /* FD Format */
    uint32_t fdf:1;
    /* Reserved */
    uint32_t :1;
    /* Event FIFO Control */
    uint32_t efc:1;
    /* Message Marker */
    uint32_t mm:8;

    /* Data field */
    uint8_t data[8];

} MCAN_TX_BUFFER;

// *****************************************************************************
/* MCAN Tx Event FIFO Element

   Summary:
    MCAN Tx Event FIFO Element Structure.

   Description:
    This data structure defines MCAN Tx Event FIFO Element.

   Remarks:
    None.
*/
typedef struct
{
    /* Identifier */
    uint32_t id:29;
    /* Remote Transmission Request */
    uint32_t rtr:1;
    /* Extended Identifier */
    uint32_t xtd:1;
    /* Error State Indicator */
    uint32_t esi:1;

    /* Tx Timestamp */
    uint32_t txts:16;
    /* Data Length Code */
    uint32_t dlc:4;
    /* Bit Rate Switch */
    uint32_t brs:1;
    /* FD Format */
    uint32_t fdf:1;
    /* Event Type */
    uint32_t et:2;
    /* Message Marker */
    uint32_t mm:8;

} MCAN_TX_EVENT_FIFO;

// *****************************************************************************
/* MCAN Tx FIFO Callback Object

   Summary:
    MCAN transfer event callback structure for Tx FIFO.

   Description:
    This data structure stores transfer event callback and it's context.

   Remarks:
    None.
*/
typedef struct
{
    /* Transfer Event Callback */
    MCAN_TX_FIFO_CALLBACK callback;

    /* Transfer Event Callback Context */
    uintptr_t context;
} MCAN_TX_FIFO_CALLBACK_OBJ;

// *****************************************************************************
/* MCAN Tx/Rx Buffers Callback Object

   Summary:
    MCAN transfer event callback structure for Tx/Rx Buffers.

   Description:
    This data structure stores transfer event callback and it's context.

   Remarks:
    None.
*/
typedef struct
{
    /* Transfer Event Callback */
    MCAN_TXRX_BUFFERS_CALLBACK callback;

    /* Transfer Event Callback Context */
    uintptr_t context;
} MCAN_TXRX_BUFFERS_CALLBACK_OBJ;

// *****************************************************************************
/* MCAN Tx Event FIFO Callback Object

   Summary:
    MCAN transfer event callback structure for Tx Event FIFO.

   Description:
    This data structure stores transfer event callback and it's context.

   Remarks:
    None.
*/
typedef struct
{
    /* Transfer Event Callback */
    MCAN_TX_EVENT_FIFO_CALLBACK callback;

    /* Transfer Event Callback Context */
    uintptr_t context;
} MCAN_TX_EVENT_FIFO_CALLBACK_OBJ;

// *****************************************************************************
/* MCAN Rx FIFO0/FIFO1 Callback Object

   Summary:
    MCAN transfer event callback structure for Rx FIFO0/FIFO1.

   Description:
    This data structure stores transfer event callback and it's context.

   Remarks:
    None.
*/
typedef struct
{
    /* Transfer Event Callback */
    MCAN_RX_FIFO_CALLBACK callback;

    /* Transfer Event Callback Context */
    uintptr_t context;
} MCAN_RX_FIFO_CALLBACK_OBJ;

// *****************************************************************************
/* MCAN Callback Object

   Summary:
    MCAN interrupt status callback structure.

   Description:
    This data structure stores interrupt status callback and it's context.

   Remarks:
    None.
*/
typedef struct
{
    /* MCAN Interrupt Status Callback */
    MCAN_CALLBACK callback;

    /* MCAN Interrupt Status Callback Context */
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
