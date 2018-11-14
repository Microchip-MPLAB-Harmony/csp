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

/* Message RAM Tx/Rx */
#define MCAN_TX_XTD_Msk      (1u << 30)                       /* Extended identifier flag */
#define MCAN_STD_ID_Msk      (0x7ffu)                         /* ID mask for standard identifier */
#define MCAN_EXT_ID_Msk      (0x1fffffffu)                    /* ID mask for extended identifier */
#define MCAN_TXFE_DLC(value) ((0xfu << 16) & ((value) << 16)) /* Tx Data Length Code */
#define MCAN_TX_BRS_Msk      (0x1u << 20)                     /* Bit rate switching */
#define MCAN_TX_FDF_Msk      (0x1u << 21)                     /* CAN FD format */
#define MCAN_TX_RTR_Msk      (0x1u << 29)                     /* Remote Transmission Request */
#define MCAN_RX_DLC(value)   (((value) >> 16) & 0xfu)         /* Rx Data Length Code */
#define MCAN_RX_XTD(value)   (((value) >> 30) & 0x1u)         /* Rx Extended Identifier */

/* Message RAM Standard Filter Element */
#define MCAN_SMF_SFID2_Pos     (0)
#define MCAN_SMF_SFID2_Msk     (0x7FFU << MCAN_SMF_SFID2_Pos)
#define MCAN_SMF_SFID2(value)  (MCAN_SMF_SFID2_Msk & ((value) << MCAN_SMF_SFID2_Pos))
#define MCAN_SMF_SFID1_Pos     (16)
#define MCAN_SMF_SFID1_Msk     (0x7FFU << MCAN_SMF_SFID1_Pos)
#define MCAN_SMF_SFID1(value)  (MCAN_SMF_SFID1_Msk & ((value) << MCAN_SMF_SFID1_Pos))
#define MCAN_SMF_SFEC_Pos      (27)
#define MCAN_SMF_SFEC_Msk      (0x7U << MCAN_SMF_SFEC_Pos)
#define MCAN_SMF_SFEC(value)   (MCAN_SMF_SFEC_Msk & ((value) << MCAN_SMF_SFEC_Pos))
#define MCAN_SMF_SFT_Pos       (30)
#define MCAN_SMF_SFT_Msk       (0x3U << MCAN_SMF_SFT_Pos)
#define MCAN_SMF_SFT(value)    (MCAN_SMF_SFT_Msk & ((value) << MCAN_SMF_SFT_Pos))

#define _MCAN_SFT_RANGE   0 /* Range filter from SFID1 to SFID2 */
#define _MCAN_SFT_DUAL    1 /* Dual ID filter for SFID1 or SFID2 */
#define _MCAN_SFT_CLASSIC 2 /* Classic filter: SFID1 = filter, SFID2 = mask */
#define _MCAN_SFEC_DISABLE  0 /* Disable filter element */
#define _MCAN_SFEC_STF0M    1 /* Store in Rx FIFO 0 if filter matches */
#define _MCAN_SFEC_STF1M    2 /* Store in Rx FIFO 1 if filter matches */
#define _MCAN_SFEC_REJECT   3 /* Reject ID if filter matches */
#define _MCAN_SFEC_PRIORITY 4 /* Set priority if filter matches. */
#define _MCAN_SFEC_PRIF0M   5 /* Set priority and store in FIFO 0 if filter matches */
#define _MCAN_SFEC_PRIF1M   6 /* Set priority and store in FIFO 1 if filter matches. */
#define _MCAN_SFEC_STRXBUF  7 /* Store into Rx Buffer or as debug message, configuration of SFT[1:0] ignored. */

/* Message RAM Extended Filter Element */
#define MCAN_EFID2_Pos     (0)
#define MCAN_EFID2_Msk     (0x1FFFFFFFUL << MCAN_EFID2_Pos)
#define MCAN_EFID2(value)  (MCAN_EFID2_Msk & ((value) << MCAN_EFID2_Pos))
#define MCAN_EFID1_Pos     (0)
#define MCAN_EFID1_Msk     (0x1FFFFFFFUL << MCAN_EFID1_Pos)
#define MCAN_EFID1(value)  (MCAN_EFID1_Msk & ((value) << MCAN_EFID1_Pos))
#define MCAN_EFEC_Pos      (29)
#define MCAN_EFEC_Msk      (0x7UL << MCAN_EFEC_Pos)
#define MCAN_EFEC(value)   (MCAN_EFEC_Msk & ((value) << MCAN_EFEC_Pos))
#define MCAN_EFT_Pos       (30)
#define MCAN_EFT_Msk       (0x3UL << MCAN_EFT_Pos)
#define MCAN_EFT(value)    (MCAN_EFT_Msk & ((value) << MCAN_EFT_Pos))

#define _MCAN_EFT_RANGE   0 /* Range filter from SFID1 to SFID2 */
#define _MCAN_EFT_DUAL    1 /* Dual ID filter for SFID1 or SFID2 */
#define _MCAN_EFT_CLASSIC 2 /* Classic filter: SFID1 = filter, SFID2 = mask */
#define _MCAN_EFEC_DISABLE  0 /* Disable filter element */
#define _MCAN_EFEC_STF0M    1 /* Store in Rx FIFO 0 if filter matches */
#define _MCAN_EFEC_STF1M    2 /* Store in Rx FIFO 1 if filter matches */
#define _MCAN_EFEC_REJECT   3 /* Reject ID if filter matches */
#define _MCAN_EFEC_PRIORITY 4 /* Set priority if filter matches. */
#define _MCAN_EFEC_PRIF0M   5 /* Set priority and store in FIFO 0 if filter matches */
#define _MCAN_EFEC_PRIF1M   6 /* Set priority and store in FIFO 1 if filter matches. */
#define _MCAN_EFEC_STRXBUF  7 /* Store into Rx Buffer or as debug message, configuration of SFT[1:0] ignored. */


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
/* MCAN Standard Filter Type

   Summary:
    MCAN Standard Filter Type.

   Description:
    This data type defines MCAN Rx Standard Filter Type.

   Remarks:
    None.
*/
typedef enum
{
    MCAN_STD_FILTER_RANGE = 0,
    MCAN_STD_FILTER_DUAL,
    MCAN_STD_FILTER_CLASSIC
} MCAN_STD_TYPE;

// *****************************************************************************
/* MCAN Filter Configuration

   Summary:
    MCAN Filter Configuration.

   Description:
    This data type defines MCAN Rx Filter Configuration.

   Remarks:
    None.
*/
typedef enum
{
    MCAN_FILTER_CONFIG_DISABLED = 0,
    MCAN_FILTER_CONFIG_FIFO_0,
    MCAN_FILTER_CONFIG_FIFO_1,
    MCAN_FILTER_CONFIG_REJECT,
    MCAN_FILTER_CONFIG_PRIORITY,
    MCAN_FILTER_CONFIG_PRIORITY_FIFO_0,
    MCAN_FILTER_CONFIG_PRIORITY_FIFO_1,
} MCAN_CONFIG;

// *****************************************************************************
/* MCAN Extended Filter Type

   Summary:
    MCAN Extended Filter Type.

   Description:
    This data type defines MCAN Rx Extended Filter Type.

   Remarks:
    None.
*/
typedef enum
{
    MCAN_EXT_FILTER_RANGE=0,
    MCAN_EXT_FILTER_DUAL,
    MCAN_EXT_FILTER_CLASSIC,
    MCAN_EXT_FILTER_UNMASKED
} MCAN_EXT_TYPE;

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
    /* 0x7 - No Error */
    MCAN_ERROR_PASSIVE = 0x20,
    MCAN_ERROR_WARNING_STATUS = 0x40,
    MCAN_ERROR_BUS_OFF = 0x80,
    MCAN_ERROR_DLEC_STUFF = 0x100,
    MCAN_ERROR_DLEC_FORM = 0x200,
    MCAN_ERROR_DLEC_ACK = 0x300,
    MCAN_ERROR_DLEC_BIT1 = 0x400,
    MCAN_ERROR_DLEC_BIT0 = 0x500,
    MCAN_ERROR_DLEC_CRC = 0x600,
    /* 0x700 - No Error */
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
/* MCAN State.

   Summary:
    MCAN PLib Task State.

   Description:
    This data type defines the MCAN Task State.

   Remarks:
    None.

*/
typedef enum {

    /* MCAN PLib Task Error State */
    MCAN_STATE_ERROR = -1,

    /* MCAN PLib Task Idle State */
    MCAN_STATE_IDLE,

    /* MCAN PLib Task Transfer Transmit State */
    MCAN_STATE_TRANSFER_TRANSMIT,

    /* MCAN PLib Task Transfer Receive State */
    MCAN_STATE_TRANSFER_RECEIVE,

    /* MCAN PLib Task Transfer Done State */
    MCAN_STATE_TRANSFER_DONE

} MCAN_STATE;

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

    /* Rx Message address, buffer and size */
    uint32_t *rxAddress;
    uint8_t *rxBuffer;
    uint8_t *rxsize;

    /* Transfer State */
    MCAN_STATE state;

    /* Transfer Event Callback */
    MCAN_CALLBACK callback;

    /* Transfer Event Callback Context */
    uintptr_t context;

} MCAN_OBJ;

// *****************************************************************************
/* MCAN Rx Buffer and FIFO element

   Summary:
    MCAN Rx Buffer, Rx FIFO0 and Rx FIFO1 element.

   Description:
    This data structure defines the Rx Buffer, Rx FIFO0 and Rx FIFO1 element.

   Remarks:
    None.
*/
typedef struct
{
    union
    {
        struct
        {
            uint32_t ID:29;      /* Identifier */
            uint32_t RTR:1;      /* Remote Transmission Request */
            uint32_t XTD:1;      /* Extended Identifier */
            uint32_t ESI:1;      /* Error State Indicator */
        } bit;
        uint32_t val;            /* Type used for register access */
    } R0;
    union
    {
        struct
        {
            uint32_t RXTS:16;    /* Rx Timestamp */
            uint32_t DLC:4;      /* Data Length Code */
            uint32_t BRS:1;      /* Bit Rate Switch */
            uint32_t FDF:1;      /* FD Format */
            uint32_t reserved:2; /* Reserved */
            uint32_t FIDX:7;     /* Filter Index */
            uint32_t ANMF:1;     /* Accepted Non-matching Frame */
        } bit;
        uint32_t val;            /* Type used for register access */
    } R1;
    uint8_t *data;               /* Up to 64 data bytes */
} MCAN_RX_BUFFER_FIFO_ENTRY;

// *****************************************************************************
/* MCAN Tx Buffer and FIFO element

   Summary:
    MCAN Tx Buffer and Tx FIFO element.

   Description:
    This data structure defines the Tx Buffer and Tx FIFO element.

   Remarks:
    None.
*/
typedef struct
{
    union
    {
        struct
        {
            uint32_t ID:29;      /* Identifier */
            uint32_t RTR:1;      /* Remote Transmission Request */
            uint32_t XTD:1;      /* Extended Identifier */
            uint32_t ESI:1;      /* Error State Indicator */
        } bit;
        uint32_t val;            /* Type used for register access */
    } T0;
    union
    {
        struct
        {
            uint32_t reserved:16;/* Reserved */
            uint32_t DLC:4;      /* Data Length Code */
            uint32_t BRS:1;      /* Bit Rate Switch */
            uint32_t FDF:1;      /* FD Format */
            uint32_t reserved1:1;/* Reserved */
            uint32_t EFC:1;      /* Event FIFO Control */
            uint32_t MM:8;       /* Message Marker */
        } bit;
        uint32_t val;            /* Type used for register access */
    } T1;
    uint8_t *data;               /* Up to 64 data bytes */
} MCAN_TX_BUFFER_FIFO_ENTRY;

// *****************************************************************************
/* MCAN Tx Event FIFO element

   Summary:
    MCAN Tx Event FIFO element.

   Description:
    This data structure defines the Tx Event FIFO element.

   Remarks:
    None.
*/
typedef struct
{
    union
    {
        struct
        {
            uint32_t ID:29;    /* Identifier */
            uint32_t RTR:1;    /* Remote Transmission Request */
            uint32_t XTD:1;    /* Extended Identifier */
            uint32_t ESI:1;    /* Error State Indicator */
        } bit;
        uint32_t val;          /* Type used for register access */
    } E0;
    union
    {
        struct
        {
            uint32_t TXTS:16;  /* Tx Timestamp */
            uint32_t DLC:4;    /* Data Length Code */
            uint32_t BRS:1;    /* Bit Rate Switch */
            uint32_t FDF:1;    /* FD Format */
            uint32_t ET:2;     /* Event Type */
            uint32_t MM:8;     /* Message Marker */
        } bit;
        uint32_t val;          /* Type used for register access */
    } E1;
} MCAN_TX_EVENT_FIFO_ENTRY;

// *****************************************************************************
/* MCAN Standard Message ID Filter element

   Summary:
    MCAN Standard Message ID Filter element.

   Description:
    This data structure defines the MCAN Standard Message ID Filter element.

   Remarks:
    None.
*/
typedef struct
{
    union
    {
        struct
        {
            uint32_t SFID2:11;   /* Standard Filter ID 2 */
            uint32_t reserved:5; /* Reserved */
            uint32_t SFID1:11;   /* Standard Filter ID 1 */
            uint32_t SFEC:3;     /* Standard Filter Configuration */
            uint32_t SFT:2;      /* Standard Filter Type */
        } bit;
        uint32_t val;            /* Type used for register access */
    } S0;
} MCAN_STANDARD_MESSAGE_ID_FILTER;

// *****************************************************************************
/* MCAN extended Message ID Filter element

   Summary:
    MCAN extended Message ID Filter element.

   Description:
    This data structure defines the MCAN extended Message ID Filter element.

   Remarks:
    None.
*/
typedef struct
{
    union
    {
        struct
        {
            uint32_t EFID1:29;  /* Extended Filter ID 1 */
            uint32_t EFEC:3;    /* Extended Filter Configuration */
        } bit;
        uint32_t val;           /* Type used for register access */
    } F0;
    union
    {
        struct
        {
            uint32_t EFID2:29;  /* Extended Filter ID 2 */
            uint32_t reserved:1;/* Reserved */
            uint32_t EFT:2;     /* Extended Filter Type */
        } bit;
        uint32_t val;           /* Type used for register access */
    } F1;
} MCAN_EXTENDED_MESSAGE_ID_FILTER;

// *****************************************************************************
/* MCAN Message RAM Configuration

   Summary:
    MCAN Message RAM Configuration structure.

   Description:
    This data structure defines the MCAN Message RAM Base address and Size for Rx FIFO0,
    Rx FIFO1, Rx Buffers, Tx Buffers/FIFO, Tx Event FIFO, Standard Message ID Filter and
    Extended Message ID Filter configuration.

   Remarks:
    None.
*/
typedef struct
{
    /* Rx FIFO0 base address and size(in bytes) */
    MCAN_RX_BUFFER_FIFO_ENTRY *rxFIFO0Address;
    uint32_t rxFIFO0Size;

    /* Rx FIFO1 base address and size(in bytes) */
    MCAN_RX_BUFFER_FIFO_ENTRY *rxFIFO1Address;
    uint32_t rxFIFO1Size;

    /* Rx Buffer base address and size(in bytes) */
    MCAN_RX_BUFFER_FIFO_ENTRY *rxBuffersAddress;
    uint32_t rxBuffersSize;

    /* Tx Buffers/FIFO base address and size(in bytes) */
    MCAN_TX_BUFFER_FIFO_ENTRY *txBuffersAddress;
    uint32_t txBuffersSize;

    /* Tx Event FIFO base address and size(in bytes) */
    MCAN_TX_EVENT_FIFO_ENTRY *txEventFIFOAddress;
    uint32_t txEventFIFOSize;

    /* Standard Message ID Filter base address and size(in bytes) */
    MCAN_STANDARD_MESSAGE_ID_FILTER *stdMsgIDFilterAddress;
    uint32_t stdMsgIDFilterSize;

    /* Extended Message ID Filter base address and size(in bytes) */
    MCAN_EXTENDED_MESSAGE_ID_FILTER *extMsgIDFilterAddress;
    uint32_t extMsgIDFilterSize;

} MCAN_MSG_RAM_CONFIG;

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility
}
#endif
// DOM-IGNORE-END

#endif //PLIB_MCAN_COMMON_H
/*******************************************************************************
 End of File
*/
