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
* Copyright (C) 2021 Microchip Technology Inc. and its subsidiaries.
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
// Section: Preprocessor macros
// *****************************************************************************
// *****************************************************************************

 // *****************************************************************************
/* CAN Transfer Errors

   Summary:
    CAN Transfer Error macros.

   Description:
    Helper macros to identify CAN errors.

   Remarks:
    None.
*/

#define CAN_ERROR_NONE                      0x0U
#define CAN_ERROR_LEC_STUFF                 0x1U
#define CAN_ERROR_LEC_FORM                  0x2U
#define CAN_ERROR_LEC_ACK                   0x3U
#define CAN_ERROR_LEC_BIT1                  0x4U
#define CAN_ERROR_LEC_BIT0                  0x5U
#define CAN_ERROR_LEC_CRC                   0x6U
#define CAN_ERROR_LEC_NC                    0x7U
#define CAN_ERROR_PASSIVE                   0x20U
#define CAN_ERROR_WARNING_STATUS            0x40U
#define CAN_ERROR_BUS_OFF                   0x80U
#define CAN_ERROR_DLEC_STUFF                0x100U
#define CAN_ERROR_DLEC_FORM                 0x200U
#define CAN_ERROR_DLEC_ACK                  0x300U
#define CAN_ERROR_DLEC_BIT1                 0x400U
#define CAN_ERROR_DLEC_BIT0                 0x500U
#define CAN_ERROR_DLEC_CRC                  0x600U
#define CAN_ERROR_DLEC_NC                   0x700U
#define CAN_ERROR_PROTOCOL_EXCEPTION_EVENT  0x4000U
#define CAN_ERROR_INVALID                   0xFFFFFFFFU

// *****************************************************************************
// *****************************************************************************
// Section: Data Types
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* CAN Rx FIFO Number

   Summary:
    CAN Rx FIFO Number.

   Description:
    This data type defines CAN Rx FIFO number for Rx FIFO0 and FIFO1.

   Remarks:
    None.
*/
typedef enum
{
    CAN_RX_FIFO_0 = 0U,
    CAN_RX_FIFO_1
} CAN_RX_FIFO_NUM;

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
    CAN_INTERRUPT_RF0N_MASK = (1UL << 0U),
    CAN_INTERRUPT_RF0W_MASK = (1UL << 1U),
    CAN_INTERRUPT_RF0F_MASK = (1UL << 2U),
    CAN_INTERRUPT_RF0L_MASK = (1UL << 3U),
    CAN_INTERRUPT_RF1N_MASK = (1UL << 4U),
    CAN_INTERRUPT_RF1W_MASK = (1UL << 5U),
    CAN_INTERRUPT_RF1F_MASK = (1UL << 6U),
    CAN_INTERRUPT_RF1L_MASK = (1UL << 7U),
    CAN_INTERRUPT_HPM_MASK = (1UL << 8U),
    CAN_INTERRUPT_TC_MASK = (1UL << 9U),
    CAN_INTERRUPT_TCF_MASK = (1UL << 10U),
    CAN_INTERRUPT_TFE_MASK = (1UL << 11U),
    CAN_INTERRUPT_TEFN_MASK = (1UL << 12U),
    CAN_INTERRUPT_TEFW_MASK = (1UL << 13U),
    CAN_INTERRUPT_TEFF_MASK = (1UL << 14U),
    CAN_INTERRUPT_TEFL_MASK = (1UL << 15U),
    CAN_INTERRUPT_TSW_MASK = (1UL << 16U),
    CAN_INTERRUPT_MRAF_MASK = (1UL << 17U),
    CAN_INTERRUPT_TOO_MASK = (1UL << 18U),
    CAN_INTERRUPT_DRX_MASK = (1UL << 19U),
    CAN_INTERRUPT_ELO_MASK = (1UL << 22U),
    CAN_INTERRUPT_EP_MASK = (1UL << 23U),
    CAN_INTERRUPT_EW_MASK = (1UL << 24U),
    CAN_INTERRUPT_BO_MASK = (1UL << 25U),
    CAN_INTERRUPT_WDI_MASK = (1UL << 26U),
    CAN_INTERRUPT_PEA_MASK = (1UL << 27U),
    CAN_INTERRUPT_PED_MASK = (1UL << 28U),
    CAN_INTERRUPT_ARA_MASK = (1UL << 29U)
}CAN_INTERRUPT_MASK;

// *****************************************************************************
/* CAN Transfer Error

   Summary:
    CAN Transfer Error data type.

   Description:
    This data type defines the CAN Transfer Error.

   Remarks:
    None.
*/
typedef uint32_t CAN_ERROR;

// *****************************************************************************
/* CAN Tx FIFO Callback

   Summary:
    CAN Callback Function Pointer for Tx FIFO.

   Description:
    This data type defines the CAN Callback Function Pointer for Tx FIFO.

   Remarks:
    None.
*/
typedef void (*CAN_TX_FIFO_CALLBACK) (uintptr_t contextHandle);

// *****************************************************************************
/* CAN TX/RX Buffers Callback

   Summary:
    CAN Callback Function Pointer for TX/RX Buffers.

   Description:
    This data type defines the CAN Callback Function Pointer for TX/RX Buffers.

   Remarks:
    None.
*/
typedef void (*CAN_TXRX_BUFFERS_CALLBACK) (uint8_t bufferNumber, uintptr_t contextHandle);

// *****************************************************************************
/* CAN Tx Event FIFO Callback

   Summary:
    CAN Callback Function Pointer for Tx Event FIFO.

   Description:
    This data type defines the CAN Callback Function Pointer for Tx Event FIFO.

   Remarks:
    None.
*/
typedef void (*CAN_TX_EVENT_FIFO_CALLBACK) (uint8_t numberOfTxEvent, uintptr_t contextHandle);

// *****************************************************************************
/* CAN Rx FIFO0/FIFO1 Callback

   Summary:
    CAN Callback Function Pointer for Rx FIFO0/FIFO1.

   Description:
    This data type defines the CAN Callback Function Pointer for Rx FIFO0/FIFO1.

   Remarks:
    None.
*/
typedef void (*CAN_RX_FIFO_CALLBACK) (uint8_t numberOfMessage, uintptr_t contextHandle);

// *****************************************************************************
/* CAN Callback

   Summary:
    CAN Callback Function Pointer.

   Description:
    This data type defines the CAN Callback Function Pointer.

   Remarks:
    None.
*/
typedef void (*CAN_CALLBACK) (uint32_t interruptStatus, uintptr_t contextHandle);

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
/* CAN Rx Buffer and FIFO Element

   Summary:
    CAN Rx Buffer and FIFO Element Structure.

   Description:
    This data structure defines CAN Rx Buffer and FIFO Element.

   Remarks:
    None.
*/
typedef struct
{
    /* Identifier */
    unsigned int id:29;
    /* Remote Transmission Request */
    unsigned int rtr:1;
    /* Extended Identifier */
    unsigned int xtd:1;
    /* Error State Indicator */
    unsigned int esi:1;

    /* Rx Timestamp */
    unsigned int rxts:16;
    /* Data Length Code */
    unsigned int dlc:4;
    /* Bit Rate Switching */
    unsigned int brs:1;
    /* FD Format */
    unsigned int fdf:1;
    /* Reserved */
    unsigned int :2;
    /* Filter Index */
    unsigned int fidx:7;
    /* Accepted Non-matching Frame */
    unsigned int anmf:1;

    /* Data field */
    uint8_t data[8];

} CAN_RX_BUFFER;

// *****************************************************************************
/* CAN Tx Buffer Element

   Summary:
    CAN Tx Buffer Element Structure.

   Description:
    This data structure defines CAN Tx Buffer Element.

   Remarks:
    None.
*/
typedef struct
{
    /* Identifier */
    unsigned int id:29;
    /* Remote Transmission Request */
    unsigned int rtr:1;
    /* Extended Identifier */
    unsigned int xtd:1;
    /* Error State Indicator */
    unsigned int esi:1;

    /* Reserved */
    unsigned int :16;
    /* Data Length Code */
    unsigned int dlc:4;
    /* Bit Rate Switching */
    unsigned int brs:1;
    /* FD Format */
    unsigned int fdf:1;
    /* Reserved */
    unsigned int :1;
    /* Event FIFO Control */
    unsigned int efc:1;
    /* Message Marker */
    unsigned int mm:8;

    /* Data field */
    uint8_t data[8];

} CAN_TX_BUFFER;

// *****************************************************************************
/* CAN Tx Event FIFO Element

   Summary:
    CAN Tx Event FIFO Element Structure.

   Description:
    This data structure defines CAN Tx Event FIFO Element.

   Remarks:
    None.
*/
typedef struct
{
    /* Identifier */
    unsigned int id:29;
    /* Remote Transmission Request */
    unsigned int rtr:1;
    /* Extended Identifier */
    unsigned int xtd:1;
    /* Error State Indicator */
    unsigned int esi:1;

    /* Tx Timestamp */
    unsigned int txts:16;
    /* Data Length Code */
    unsigned int dlc:4;
    /* Bit Rate Switch */
    unsigned int brs:1;
    /* FD Format */
    unsigned int fdf:1;
    /* Event Type */
    unsigned int et:2;
    /* Message Marker */
    unsigned int mm:8;

} CAN_TX_EVENT_FIFO;

// *****************************************************************************
/* CAN Nominal Bit Timing Parameters

   Summary:
    CAN Nominal Bit Timing Parameter structure.

   Description:
    This data structure defines Nominal Bit Timing Parameters.

   Remarks:
    None.
*/
typedef struct
{
    /* Nominal Time segment after sample point */
    uint8_t nominalTimeSegment2;

    /* Nominal Time segment before sample point */
    uint8_t nominalTimeSegment1;

    /* Nominal Baud Rate Prescaler */
    uint16_t nominalPrescaler;

    /* Nominal Syncronization Jump Width */
    uint8_t nominalSJW;

} CAN_NOMINAL_BIT_TIMING;

// *****************************************************************************
/* CAN Data Bit Timing Parameters

   Summary:
    CAN Data Bit Timing Parameter structure.

   Description:
    This data structure defines Data Bit Timing Parameters.

   Remarks:
    None.
*/
typedef struct
{
    /* Data Time segment after sample point */
    uint8_t dataTimeSegment2;

    /* Data Time segment before sample point */
    uint8_t dataTimeSegment1;

    /* Data Baud Rate Prescaler */
    uint8_t dataPrescaler;

    /* Data Syncronization Jump Width */
    uint8_t dataSJW;

} CAN_DATA_BIT_TIMING;

// *****************************************************************************
/* CAN Bit Timing Parameters

   Summary:
    CAN Bit Timing Parameter structure.

   Description:
    This data structure defines Bit Timing Parameters.

   Remarks:
    None.
*/
typedef struct
{
    /* Nominal bit timing set flag */
    bool nominalBitTimingSet;

    /* Nominal bit timing parameters */
    CAN_NOMINAL_BIT_TIMING nominalBitTiming;

    /* Data bit timing set flag */
    bool dataBitTimingSet;

    /* Data bit timing parameters */
    CAN_DATA_BIT_TIMING dataBitTiming;
} CAN_BIT_TIMING;

// *****************************************************************************
/* CAN Bit Timing Setup

   Summary:
    CAN Bit Timing Setup structure.

   Description:
    This data structure defines Bit Timing Setup parameters.

   Remarks:
    None.
*/
typedef struct
{
    /* Nominal bit timing set flag */
    bool nominalBitTimingSet;

    /* Nominal bit rate */
    uint32_t nominalBitRate;

    /* Nominal Sample Point */
    float nominalSamplePoint;

    /* Nominal Baud Rate Prescaler */
    uint16_t nominalPrescaler;

    /* Data bit timing set flag */
    bool dataBitTimingSet;

    /* Data bit rate */
    uint32_t dataBitRate;

    /* Data Sample Point */
    float dataSamplePoint;

    /* Data Baud Rate Prescaler */
    uint8_t dataPrescaler;

} CAN_BIT_TIMING_SETUP;

// *****************************************************************************
/* CAN Tx FIFO Callback Object

   Summary:
    CAN transfer event callback structure for Tx FIFO.

   Description:
    This data structure stores transfer event callback and it's context.

   Remarks:
    None.
*/
typedef struct
{
    /* Transfer Event Callback */
    CAN_TX_FIFO_CALLBACK callback;

    /* Transfer Event Callback Context */
    uintptr_t context;
} CAN_TX_FIFO_CALLBACK_OBJ;

// *****************************************************************************
/* CAN Tx/Rx Buffers Callback Object

   Summary:
    CAN transfer event callback structure for Tx/Rx Buffers.

   Description:
    This data structure stores transfer event callback and it's context.

   Remarks:
    None.
*/
typedef struct
{
    /* Transfer Event Callback */
    CAN_TXRX_BUFFERS_CALLBACK callback;

    /* Transfer Event Callback Context */
    uintptr_t context;
} CAN_TXRX_BUFFERS_CALLBACK_OBJ;

// *****************************************************************************
/* CAN Tx Event FIFO Callback Object

   Summary:
    CAN transfer event callback structure for Tx Event FIFO.

   Description:
    This data structure stores transfer event callback and it's context.

   Remarks:
    None.
*/
typedef struct
{
    /* Transfer Event Callback */
    CAN_TX_EVENT_FIFO_CALLBACK callback;

    /* Transfer Event Callback Context */
    uintptr_t context;
} CAN_TX_EVENT_FIFO_CALLBACK_OBJ;

// *****************************************************************************
/* CAN Rx FIFO0/FIFO1 Callback Object

   Summary:
    CAN transfer event callback structure for Rx FIFO0/FIFO1.

   Description:
    This data structure stores transfer event callback and it's context.

   Remarks:
    None.
*/
typedef struct
{
    /* Transfer Event Callback */
    CAN_RX_FIFO_CALLBACK callback;

    /* Transfer Event Callback Context */
    uintptr_t context;
} CAN_RX_FIFO_CALLBACK_OBJ;

// *****************************************************************************
/* CAN Callback Object

   Summary:
    CAN interrupt status callback structure.

   Description:
    This data structure stores interrupt status callback and it's context.

   Remarks:
    None.
*/
typedef struct
{
    /* CAN Interrupt Status Callback */
    CAN_CALLBACK callback;

    /* CAN Interrupt Status Callback Context */
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
