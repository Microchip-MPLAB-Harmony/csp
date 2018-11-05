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
    This header is for documentation only.  The actual plib_mcan<x>
    headers will be generated as required by the MCC (where <x> is the
    peripheral instance number).

    Every interface symbol has a lower-case 'x' in it following the "MCAN"
    abbreviation.  This 'x' will be replaced by the peripheral instance number
    in the generated headers.  These are the actual functions that should be
    used.
*******************************************************************************/

//DOM-IGNORE-BEGIN
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
     bool MCANx_MessageTransmit(uint32_t address, uint8_t length,
                   uint8_t* data, MCAN_MODE mode, MCAN_MSG_TX_ATTRIBUTE msgAttr);

  Summary:
    Transmits a message into CAN bus.

  Description:
    This routine transmits a data buffer on the MCAN bus according to the
    mode, msgAttr, address, data and length given.

  Precondition:
    MCANx_Initialize has been called.

  Parameters:
    address - 11-bit / 29-bit identifier (ID).
    length  - length of data buffer in number of bytes.
    data    - pointer to source data buffer
    mode    - MCAN mode Classic CAN or CAN FD without BRS or CAN FD with BRS
    msgAttr - Data Frame or Remote frame using Tx FIFO or Tx Buffer

  Returns:
    Boolean "true" when a message has been transmitted.

  Example:
    <code>
    uint8_t buf[] = {0xAA, 0x55};
    MCAN0_Initialize();
    MCAN0_MessageTransmit(0x555, sizeof(buf), buf, MCAN_MODE_NORMAL, MCAN_MSG_ATTR_TX_FIFO_DATA_FRAME);
    </code>

  Remarks:
    This routine transmits a standard or extended messages based upon the CAN
    plib setup.
*/
bool MCANx_MessageTransmit(uint32_t address, uint8_t length, uint8_t* data, MCAN_MODE mode, MCAN_MSG_TX_ATTRIBUTE msgAttr);

// *****************************************************************************
/* Function:
    bool MCANx_MessageReceive(uint32_t *address, uint8_t *length, uint8_t *data,
	                          MCAN_MSG_RX_ATTRIBUTE msgAttr);

  Summary:
    Receives a message from CAN bus.

  Description:
   This routine receives data into a buffer from the MCAN bus according to the
   msgAttr given.

  Precondition:
    MCANx_Initialize has been called.

  Parameters:
    address - Pointer to 11-bit / 29-bit identifier (ID) to be received.
    length  - Pointer to data length in number of bytes to be received.
    data    - pointer to destination data buffer
    msgAttr - Message to be read from Rx FIFO0 or Rx FIFO1 or Rx Buffer

  Returns:
    true  - When a message has been received
    false - When a message has not been received

  Example:
    <code>
    uint8_t buf[64], address, length;
    MCAN0_Initialize();
    MCAN0_MessageReceive(&address, &length, buf, MCAN_MSG_ATTR_RX_FIFO0);
    </code>

  Remarks:
    This routine receives a standard or extended messages based upon the MCAN
    Plib setup.
*/
bool MCANx_MessageReceive(uint32_t *address, uint8_t *length, uint8_t *data, MCAN_MSG_RX_ATTRIBUTE msgAttr);

// *****************************************************************************
/* Function:
    MCAN_ERROR MCANx_ErrorGet(void)

   Summary:
    Returns the error during transfer.

   Precondition:
    MCANx_Initialize must have been called for the associated MCAN instance.

   Parameters:
    None.

  Example:
    <code>
    MCAN_ERROR error;
    error = MCAN0_ErrorGet();
    </code>

   Returns:
    Error during transfer.
*/
MCAN_ERROR MCANx_ErrorGet(void);

// *****************************************************************************
/* Function:
    bool MCANx_InterruptGet(MCAN_INTERRUPT_MASK interruptMask)

   Summary:
    Returns the Interrupt status.

   Precondition:
    MCANx_Initialize must have been called for the associated MCAN instance.

   Parameters:
    interruptMask - Interrupt source number

  Example:
    <code>
    MCAN_INTERRUPT_MASK interruptMask = MCAN_INTERRUPT_RF0W_MASK;
    if (MCAN0_InterruptGet(interruptMask))
    {
    }
    </code>

   Returns:
    true - Requested interrupt is occurred.
    false - Requested interrupt is not occurred.
*/
bool MCANx_InterruptGet(MCAN_INTERRUPT_MASK interruptMask);

// *****************************************************************************
/* Function:
    void MCANx_InterruptClear(MCAN_INTERRUPT_MASK interruptMask)

   Summary:
    Clears Interrupt status.

   Precondition:
    MCANx_Initialize must have been called for the associated MCAN instance.

   Parameters:
    interruptMask - Interrupt to be cleared

  Example:
    <code>
    MCAN_INTERRUPT_MASK interruptMask = MCAN_INTERRUPT_RF0W_MASK;
    MCAN0_InterruptClear(interruptMask);
    </code>

   Returns:
    None
*/
void MCANx_InterruptClear(MCAN_INTERRUPT_MASK interruptMask);

// *****************************************************************************
/* Function:
    void MCANx_MessageRAMConfigGet(MCAN_MSG_RAM_CONFIG *msgRAMConfig)

   Summary:
    Get the Message RAM Configuration.

   Precondition:
    ${MCAN_INSTANCE_NAME}_Initialize must have been called for the associated MCAN instance.

   Parameters:
    msgRAMConfig - Pointer to the Message RAM Configuration object

   Example:
    <code>
    MCAN_MSG_RAM_CONFIG messageRAMConfig;
    MCAN0_MessageRAMConfigGet(&messageRAMConfig);
    </code>

   Returns:
    None
*/
void MCANx_MessageRAMConfigGet(MCAN_MSG_RAM_CONFIG *msgRAMConfig);

// *****************************************************************************
/* Function:
    bool MCANx_IsBusy(void)

   Summary:
    Returns the Peripheral busy status.

   Precondition:
    MCANx_Initialize must have been called for the associated MCAN instance.

   Parameters:
    None.

  Example:
    <code>
    if (MCAN0_IsBusy())
    {
    }
    </code>

   Returns:
    true - Busy.
    false - Not busy.
*/
bool MCANx_IsBusy(void);

// *****************************************************************************
/* Function:
    void MCANx_CallbackRegister(MCAN_CALLBACK callback, uintptr_t contextHandle)

   Summary:
    Sets the pointer to the function (and it's context) to be called when the
    given MCAN's transfer events occur.

   Precondition:
    MCANx_Initialize must have been called for the associated MCAN instance.

   Parameters:
    callback - A pointer to a function with a calling signature defined
    by the MCAN_CALLBACK data type.

    context - A value (usually a pointer) passed (unused) into the function
    identified by the callback parameter.

  Example:
    <code>
    void MCAN0_callbackHandler (uintptr_t context)
    {
    }
    MCAN0_CallbackRegister(MCAN0_callbackHandler, 0);
    </code>

   Returns:
    None.
*/
void MCANx_CallbackRegister(MCAN_CALLBACK callback, uintptr_t contextHandle);


// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END

#endif // #ifndef PLIB_MCANx_H
/*******************************************************************************
 End of File
*/
