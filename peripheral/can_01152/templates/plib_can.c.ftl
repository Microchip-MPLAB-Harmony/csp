/*******************************************************************************
  Controller Area Network (CAN) Peripheral Library Source File

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${CAN_INSTANCE_NAME?lower_case}.c

  Summary:
    CAN peripheral library interface.

  Description:
    This file defines the interface to the CAN peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

  Remarks:
    None.
*******************************************************************************/

//DOM-IGNORE-BEGIN
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
//DOM-IGNORE-END
// *****************************************************************************
// *****************************************************************************
// Header Includes
// *****************************************************************************
// *****************************************************************************
#include <sys/kmem.h>
#include "plib_${CAN_INSTANCE_NAME?lower_case}.h"
<#if core.CoreSysIntFile == true>
#include "interrupts.h"
</#if>

// *****************************************************************************
// *****************************************************************************
// Global Data
// *****************************************************************************
// *****************************************************************************
<#assign CAN_PROPAG = PROPAG - 1>
<#assign CAN_PHASE1 = PHASE1 - 1>
<#assign CAN_PHASE2 = PHASE2 - 1>
<#assign CAN_SJW    = SJW - 1>
/* Number of configured FIFO */
#define CAN_NUM_OF_FIFO              (${NUMBER_OF_FIFO}U)
/* Maximum number of CAN Message buffers in each FIFO */
#define CAN_FIFO_MESSAGE_BUFFER_MAX  (32U)

#define CAN_CONFIGURATION_MODE       (0x4UL)
#define CAN_OPERATION_MODE           (${CAN_OPMODE}UL)
#define CAN_NUM_OF_FILTER            (${NUMBER_OF_FILTER}U)
/* FIFO Offset in word (4 bytes) */
#define CAN_FIFO_OFFSET              (0x10U)
/* Filter Offset in word (4 bytes) */
#define CAN_FILTER_OFFSET            (0x4U)
/* Acceptance Mask Offset in word (4 bytes) */
#define CAN_ACCEPTANCE_MASK_OFFSET   (0x4U)
<#assign MESSAGE_RAM_SIZE = 0>
<#list 0..(NUMBER_OF_FIFO-1) as fifo>
<#assign MESSAGE_BUFFER_SIZE = CAN_INSTANCE_NAME + "_FIFO" + fifo + "_SIZE">
<#assign MESSAGE_RAM_SIZE = (MESSAGE_RAM_SIZE + .vars[MESSAGE_BUFFER_SIZE])>
</#list>
#define CAN_MESSAGE_RAM_CONFIG_SIZE (${MESSAGE_RAM_SIZE}U)
#define CAN_MSG_IDE_MASK            (0x10000000U)
#define CAN_MSG_SID_MASK            (0x7FFU)
#define CAN_MSG_TIMESTAMP_MASK      (0xFFFF0000U)
#define CAN_MSG_EID_MASK            (0x1FFFFFFFU)
#define CAN_MSG_DLC_MASK            (0xFU)
#define CAN_MSG_RTR_MASK            (0x200U)
#define CAN_MSG_SRR_MASK            (0x20000000U)

<#if CAN_INTERRUPT_MODE == true>
static volatile CAN_OBJ ${CAN_INSTANCE_NAME?lower_case}Obj;
static volatile CAN_RX_MSG ${CAN_INSTANCE_NAME?lower_case}RxMsg[CAN_NUM_OF_FIFO][CAN_FIFO_MESSAGE_BUFFER_MAX];
static volatile CAN_CALLBACK_OBJ ${CAN_INSTANCE_NAME?lower_case}CallbackObj[CAN_NUM_OF_FIFO];
static volatile CAN_CALLBACK_OBJ ${CAN_INSTANCE_NAME?lower_case}ErrorCallbackObj;
static volatile uint32_t ${CAN_INSTANCE_NAME?lower_case}MsgIndex[CAN_NUM_OF_FIFO];
</#if>
static CAN_TX_RX_MSG_BUFFER __attribute__((coherent, aligned(32))) can_message_buffer[CAN_MESSAGE_RAM_CONFIG_SIZE];

/******************************************************************************
Local Functions
******************************************************************************/
static inline void ${CAN_INSTANCE_NAME}_ZeroInitialize(volatile void* pData, size_t dataSize)
{
    volatile uint8_t* data = (volatile uint8_t*)pData;
    for (uint32_t index = 0; index < dataSize; index++)
    {
        data[index] = 0U;
    }
}

<#assign COUNT_11_6_DEVIATION = 3>
/* MISRAC 2012 deviation block start */
/* MISRA C-2012 Rule 11.6 deviated ${COUNT_11_6_DEVIATION} times. Deviation record ID -  H3_MISRAC_2012_R_11_6_DR_1 */
/* MISRA C-2012 Rule 5.1 deviated 1 time. Deviation record ID -  H3_MISRAC_2012_R_5_1_DR_1 */
<#if core.COVERITY_SUPPRESS_DEVIATION?? && core.COVERITY_SUPPRESS_DEVIATION>
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wunknown-pragmas"
#pragma coverity compliance block \
(deviate:${COUNT_11_6_DEVIATION} "MISRA C-2012 Rule 11.6" "H3_MISRAC_2012_R_11_6_DR_1") \
(deviate:1 "MISRA C-2012 Rule 5.1" "H3_MISRAC_2012_R_5_1_DR_1")
</#if>
// *****************************************************************************
// *****************************************************************************
// ${CAN_INSTANCE_NAME} PLib Interface Routines
// *****************************************************************************
// *****************************************************************************
// *****************************************************************************
/* Function:
    void ${CAN_INSTANCE_NAME}_Initialize(void)

   Summary:
    Initializes given instance of the CAN peripheral.

   Precondition:
    None.

   Parameters:
    None.

   Returns:
    None
*/
void ${CAN_INSTANCE_NAME}_Initialize(void)
{
    /* Switch the CAN module ON */
    C${CAN_INSTANCE_NUM}CONSET = _C${CAN_INSTANCE_NUM}CON_ON_MASK;

    /* Switch the CAN module to Configuration mode. Wait until the switch is complete */
    C${CAN_INSTANCE_NUM}CON = (C${CAN_INSTANCE_NUM}CON & ~_C${CAN_INSTANCE_NUM}CON_REQOP_MASK) | ((CAN_CONFIGURATION_MODE << _C${CAN_INSTANCE_NUM}CON_REQOP_POSITION) & _C${CAN_INSTANCE_NUM}CON_REQOP_MASK);
    while(((C${CAN_INSTANCE_NUM}CON & _C${CAN_INSTANCE_NUM}CON_OPMOD_MASK) >> _C${CAN_INSTANCE_NUM}CON_OPMOD_POSITION) != CAN_CONFIGURATION_MODE)
    {
         /* Do Nothing */
    }

    /* Set the Bitrate to ${NOMINAL_BITRATE} Kbps */
    C${CAN_INSTANCE_NUM}CFG = ((${BRP}UL << _C${CAN_INSTANCE_NUM}CFG_BRP_POSITION) & _C${CAN_INSTANCE_NUM}CFG_BRP_MASK)
                            | ((${CAN_SJW}UL << _C${CAN_INSTANCE_NUM}CFG_SJW_POSITION) & _C${CAN_INSTANCE_NUM}CFG_SJW_MASK)
                            | ((${CAN_PHASE2}UL << _C${CAN_INSTANCE_NUM}CFG_SEG2PH_POSITION) & _C${CAN_INSTANCE_NUM}CFG_SEG2PH_MASK)
                            | ((${CAN_PHASE1}UL << _C${CAN_INSTANCE_NUM}CFG_SEG1PH_POSITION) & _C${CAN_INSTANCE_NUM}CFG_SEG1PH_MASK)
                            | ((${CAN_PROPAG}UL << _C${CAN_INSTANCE_NUM}CFG_PRSEG_POSITION) & _C${CAN_INSTANCE_NUM}CFG_PRSEG_MASK)
                            | _C${CAN_INSTANCE_NUM}CFG_SEG2PHTS_MASK<#if CAN_CFG_SAM == "0x1"> | _C${CAN_INSTANCE_NUM}CFG_SAM_MASK</#if>;

    /* Set FIFO base address for all message buffers */
    C${CAN_INSTANCE_NUM}FIFOBA = (uint32_t)KVA_TO_PA(can_message_buffer);

    /* Configure CAN FIFOs */
    <#list 0..(NUMBER_OF_FIFO-1) as fifo>
    <#assign FIFO_SIZE = CAN_INSTANCE_NAME + "_FIFO" + fifo + "_SIZE">
    <#assign TX_FIFO_ENABLE = CAN_INSTANCE_NAME + "_FIFO" + fifo + "_TXEN" >
    <#assign TX_FIFO_PRIORITY = CAN_INSTANCE_NAME + "_FIFO" + fifo + "_TXPR">
    <#assign TX_FIFO_RTREN = CAN_INSTANCE_NAME + "_FIFO" + fifo + "_RTREN">
    C${CAN_INSTANCE_NUM}FIFOCON${fifo} = (((${.vars[FIFO_SIZE]}UL - 1UL) << _C${CAN_INSTANCE_NUM}FIFOCON${fifo}_FSIZE_POSITION) & _C${CAN_INSTANCE_NUM}FIFOCON${fifo}_FSIZE_MASK)<#if .vars[TX_FIFO_ENABLE] == "0x1"> | _C${CAN_INSTANCE_NUM}FIFOCON${fifo}_TXEN_MASK | ((${.vars[TX_FIFO_PRIORITY]}UL << _C${CAN_INSTANCE_NUM}FIFOCON${fifo}_TXPRI_POSITION) & _C${CAN_INSTANCE_NUM}FIFOCON${fifo}_TXPRI_MASK) | ((${.vars[TX_FIFO_RTREN]}UL << _C${CAN_INSTANCE_NUM}FIFOCON${fifo}_RTREN_POSITION) & _C${CAN_INSTANCE_NUM}FIFOCON${fifo}_RTREN_MASK)</#if>;
    </#list>

    /* Configure CAN Filters */
    <#list 0..(NUMBER_OF_FILTER-1) as filter>
    <#assign FILTER_REG_INDEX = filter/4>
    <#assign FILTER_ID = CAN_INSTANCE_NAME + "_FILTER" + filter + "_ID_DECIMAL">
    <#assign FILTER_FIFO_SELECT = CAN_INSTANCE_NAME + "_FILTER" + filter + "_FIFO_SELECT">
    <#assign FILTER_MASK_SELECT = CAN_INSTANCE_NAME + "_FILTER" + filter + "_MASK_SELECT">
    <#assign FILTER_ENABLE = CAN_INSTANCE_NAME + "_FILTER" + filter + "_ENABLE">
    C${CAN_INSTANCE_NUM}RXF${filter} = ${(.vars[FILTER_ID]?number > 2047)?then('(${.vars[FILTER_ID]}UL & _C${CAN_INSTANCE_NUM}RXF${filter}_EID_MASK) | (((${.vars[FILTER_ID]} & 0x1FFC0000u) >> 18u) << _C${CAN_INSTANCE_NUM}RXF${filter}_SID_POSITION) | _C${CAN_INSTANCE_NUM}RXF${filter}_EXID_MASK','(${.vars[FILTER_ID]}UL & CAN_MSG_SID_MASK) << _C${CAN_INSTANCE_NUM}RXF${filter}_SID_POSITION')};
    C${CAN_INSTANCE_NUM}FLTCON${FILTER_REG_INDEX?int}SET = ((${.vars[FILTER_FIFO_SELECT]}UL << _C${CAN_INSTANCE_NUM}FLTCON${FILTER_REG_INDEX?int}_FSEL${filter}_POSITION) & _C${CAN_INSTANCE_NUM}FLTCON${FILTER_REG_INDEX?int}_FSEL${filter}_MASK)
                                                         | ((${.vars[FILTER_MASK_SELECT]}UL << _C${CAN_INSTANCE_NUM}FLTCON${FILTER_REG_INDEX?int}_MSEL${filter}_POSITION) & _C${CAN_INSTANCE_NUM}FLTCON${FILTER_REG_INDEX?int}_MSEL${filter}_MASK)<#if .vars[FILTER_ENABLE] == true>| _C${CAN_INSTANCE_NUM}FLTCON${FILTER_REG_INDEX?int}_FLTEN${filter}_MASK</#if>;
    </#list>

    /* Configure CAN Acceptance Filter Masks */
    <#list 0..(NUMBER_OF_ACCEPTANCE_FILTER_MASK-1) as mask>
    <#assign FILTER_MASK_ID = CAN_INSTANCE_NAME + "_MASK" + mask + "_ID_DECIMAL">
    C${CAN_INSTANCE_NUM}RXM${mask} = ${(.vars[FILTER_MASK_ID]?number > 2047)?then('(${.vars[FILTER_MASK_ID]}UL & _C${CAN_INSTANCE_NUM}RXM${mask}_EID_MASK) | (((${.vars[FILTER_MASK_ID]} & 0x1FFC0000u) >> 18u) << _C${CAN_INSTANCE_NUM}RXM${mask}_SID_POSITION) | _C${CAN_INSTANCE_NUM}RXM${mask}_MIDE_MASK','(${.vars[FILTER_MASK_ID]}UL & CAN_MSG_SID_MASK) << _C${CAN_INSTANCE_NUM}RXM${mask}_SID_POSITION')};
    </#list>

<#if CAN_TIMESTAMP_ENABLE == true>
    /* Enable Timestamp */
    C${CAN_INSTANCE_NUM}CONSET = _C${CAN_INSTANCE_NUM}CON_CANCAP_MASK;
    C${CAN_INSTANCE_NUM}TMR = ${CAN_TIMESTAMP_PRESCALER}U & _C${CAN_INSTANCE_NUM}TMR_CANTSPRE_MASK;

</#if>
<#if CAN_INTERRUPT_MODE == true>
    /* Set Interrupts */
    ${CAN_IEC_REG}SET = _${CAN_IEC_REG}_CAN${CAN_INSTANCE_NUM}IE_MASK;
    C${CAN_INSTANCE_NUM}INTSET = _C${CAN_INSTANCE_NUM}INT_SERRIE_MASK | _C${CAN_INSTANCE_NUM}INT_CERRIE_MASK | _C${CAN_INSTANCE_NUM}INT_IVRIE_MASK;

    /* Initialize the CAN PLib Object */
    ${CAN_INSTANCE_NAME}_ZeroInitialize((void *)${CAN_INSTANCE_NAME?lower_case}RxMsg, sizeof(${CAN_INSTANCE_NAME?lower_case}RxMsg));

</#if>
    /* Switch the CAN module to CAN_OPERATION_MODE. Wait until the switch is complete */
    <#if CAN_OPMODE == "0x1">
    C${CAN_INSTANCE_NUM}CON = (C${CAN_INSTANCE_NUM}CON & ~_C${CAN_INSTANCE_NUM}CON_REQOP_MASK);
    while(((C${CAN_INSTANCE_NUM}CON & _C${CAN_INSTANCE_NUM}CON_OPMOD_MASK) >> _C${CAN_INSTANCE_NUM}CON_OPMOD_POSITION) != 0)
    {
        /* Do Nothing */
    }
    </#if>
    C${CAN_INSTANCE_NUM}CON = (C${CAN_INSTANCE_NUM}CON & ~_C${CAN_INSTANCE_NUM}CON_REQOP_MASK) | ((CAN_OPERATION_MODE << _C${CAN_INSTANCE_NUM}CON_REQOP_POSITION) & _C${CAN_INSTANCE_NUM}CON_REQOP_MASK);
    while(((C${CAN_INSTANCE_NUM}CON & _C${CAN_INSTANCE_NUM}CON_OPMOD_MASK) >> _C${CAN_INSTANCE_NUM}CON_OPMOD_POSITION) != CAN_OPERATION_MODE)
    {
        /* Do Nothing */
    }
}

// *****************************************************************************
/* Function:
    bool ${CAN_INSTANCE_NAME}_MessageTransmit(uint32_t id, uint8_t length, uint8_t* data, uint8_t fifoNum, CAN_MSG_TX_ATTRIBUTE msgAttr)

   Summary:
    Transmits a message into CAN bus.

   Precondition:
    ${CAN_INSTANCE_NAME}_Initialize must have been called for the associated CAN instance.

   Parameters:
    id          - 11-bit / 29-bit identifier (ID).
    length      - length of data buffer in number of bytes.
    data        - pointer to source data buffer
    fifoNum     - FIFO number
    msgAttr     - Data frame or Remote frame to be transmitted

   Returns:
    Request status.
    true  - Request was successful.
    false - Request has failed.
*/
bool ${CAN_INSTANCE_NAME}_MessageTransmit(uint32_t id, uint8_t length, uint8_t* data, uint8_t fifoNum, CAN_MSG_TX_ATTRIBUTE msgAttr)
{
    CAN_TX_RX_MSG_BUFFER *txMessage = NULL;
    uint8_t count = 0;
    bool status = false;

    if ((fifoNum > (CAN_NUM_OF_FIFO - 1U)) || (data == NULL))
    {
        return status;
    }

    if ((*(volatile uint32_t *)(&C${CAN_INSTANCE_NUM}FIFOINT0 + (fifoNum * CAN_FIFO_OFFSET)) & _C${CAN_INSTANCE_NUM}FIFOINT0_TXNFULLIF_MASK) == _C${CAN_INSTANCE_NUM}FIFOINT0_TXNFULLIF_MASK)
    {
        txMessage = (CAN_TX_RX_MSG_BUFFER *)PA_TO_KVA1(*(volatile uint32_t *)(&C${CAN_INSTANCE_NUM}FIFOUA0 + (fifoNum * CAN_FIFO_OFFSET)));

        /* Check the id whether it falls under SID or EID,
         * SID max limit is 0x7FF, so anything beyond that is EID */
        if (id > CAN_MSG_SID_MASK)
        {
            txMessage->msgSID = (id & CAN_MSG_EID_MASK) >> 18;
            txMessage->msgEID = ((id & 0x3FFFFUL) << 10) | CAN_MSG_IDE_MASK | CAN_MSG_SRR_MASK;
        }
        else
        {
            txMessage->msgSID = id;
            txMessage->msgEID = 0U;
        }

        if (msgAttr == CAN_MSG_TX_REMOTE_FRAME)
        {
            txMessage->msgEID |= CAN_MSG_RTR_MASK;
        }
        else
        {
            if (length > 8U)
            {
                length = 8U;
            }
            txMessage->msgEID |= length;

            while(count < length)
            {
                txMessage->msgData[count++] = *data++;
            }
        }

<#if CAN_INTERRUPT_MODE == true>
        *(volatile uint32_t *)(&C${CAN_INSTANCE_NUM}FIFOINT0SET + (fifoNum * CAN_FIFO_OFFSET)) = _C${CAN_INSTANCE_NUM}FIFOINT0_TXEMPTYIE_MASK;

</#if>
        /* Request the transmit */
        *(volatile uint32_t *)(&C${CAN_INSTANCE_NUM}FIFOCON0SET + (fifoNum * CAN_FIFO_OFFSET)) = _C${CAN_INSTANCE_NUM}FIFOCON0_UINC_MASK;
        *(volatile uint32_t *)(&C${CAN_INSTANCE_NUM}FIFOCON0SET + (fifoNum * CAN_FIFO_OFFSET)) = _C${CAN_INSTANCE_NUM}FIFOCON0_TXREQ_MASK;

<#if CAN_INTERRUPT_MODE == true>
        C${CAN_INSTANCE_NUM}INTSET = _C${CAN_INSTANCE_NUM}INT_TBIE_MASK;

</#if>
        status = true;
    }
    return status;
}

// *****************************************************************************
/* Function:
    bool ${CAN_INSTANCE_NAME}_MessageReceive(uint32_t *id, uint8_t *length, uint8_t *data, uint16_t *timestamp, uint8_t fifoNum, CAN_MSG_RX_ATTRIBUTE *msgAttr)

   Summary:
    Receives a message from CAN bus.

   Precondition:
    ${CAN_INSTANCE_NAME}_Initialize must have been called for the associated CAN instance.

   Parameters:
    id          - Pointer to 11-bit / 29-bit identifier (ID) to be received.
    length      - Pointer to data length in number of bytes to be received.
    data        - Pointer to destination data buffer
    timestamp   - Pointer to Rx message timestamp, timestamp value is 0 if Timestamp is disabled in C${CAN_INSTANCE_NUM}CON
    fifoNum     - FIFO number
    msgAttr     - Data frame or Remote frame to be received

   Returns:
    Request status.
    true  - Request was successful.
    false - Request has failed.
*/
bool ${CAN_INSTANCE_NAME}_MessageReceive(uint32_t *id, uint8_t *length, uint8_t *data, uint16_t *timestamp, uint8_t fifoNum, CAN_MSG_RX_ATTRIBUTE *msgAttr)
{
<#if CAN_INTERRUPT_MODE == false>
    CAN_TX_RX_MSG_BUFFER *rxMessage = NULL;
    uint8_t count = 0;
</#if>
    bool status = false;
<#if CAN_INTERRUPT_MODE == true>
    uint8_t msgIndex = 0;
    uint8_t fifoSize = 0;
</#if>

    if ((fifoNum > (CAN_NUM_OF_FIFO - 1U)) || (data == NULL) || (length == NULL) || (id == NULL))
    {
        return status;
    }

<#if CAN_INTERRUPT_MODE == false>
    /* Check if there is a message available in FIFO */
    if ((*(volatile uint32_t *)(&C${CAN_INSTANCE_NUM}FIFOINT0 + (fifoNum * CAN_FIFO_OFFSET)) & _C${CAN_INSTANCE_NUM}FIFOINT0_RXNEMPTYIF_MASK) == _C${CAN_INSTANCE_NUM}FIFOINT0_RXNEMPTYIF_MASK)
    {
        /* Get a pointer to RX message buffer */
        rxMessage = (CAN_TX_RX_MSG_BUFFER *)PA_TO_KVA1(*(volatile uint32_t *)(&C${CAN_INSTANCE_NUM}FIFOUA0 + (fifoNum * CAN_FIFO_OFFSET)));

        /* Check if it's a extended message type */
        if ((rxMessage->msgEID & CAN_MSG_IDE_MASK) != 0U)
        {
            *id = ((rxMessage->msgSID & CAN_MSG_SID_MASK) << 18) | ((rxMessage->msgEID >> 10) & _C${CAN_INSTANCE_NUM}RXM0_EID_MASK);
            if ((rxMessage->msgEID & CAN_MSG_RTR_MASK) != 0U)
            {
                *msgAttr = CAN_MSG_RX_REMOTE_FRAME;
            }
            else
            {
                *msgAttr = CAN_MSG_RX_DATA_FRAME;
            }
        }
        else
        {
            *id = rxMessage->msgSID & CAN_MSG_SID_MASK;
            if ((rxMessage->msgEID & CAN_MSG_SRR_MASK) != 0U)
            {
                *msgAttr = CAN_MSG_RX_REMOTE_FRAME;
            }
            else
            {
                *msgAttr = CAN_MSG_RX_DATA_FRAME;
            }
        }

        *length = (uint8_t)(rxMessage->msgEID & CAN_MSG_DLC_MASK);

        /* Copy the data into the payload */
        while (count < *length)
        {
           *data++ = rxMessage->msgData[count++];
        }

        if (timestamp != NULL)
        {
            *timestamp = (uint16_t)((rxMessage->msgSID & CAN_MSG_TIMESTAMP_MASK) >> 16);
        }

        /* Message processing is done, update the message buffer pointer. */
        *(volatile uint32_t *)(&C${CAN_INSTANCE_NUM}FIFOCON0SET + (fifoNum * CAN_FIFO_OFFSET)) = _C${CAN_INSTANCE_NUM}FIFOCON0_UINC_MASK;

        /* Message is processed successfully, so return true */
        status = true;
    }
</#if>
<#if CAN_INTERRUPT_MODE == true>
    fifoSize = (uint8_t)((*(volatile uint32_t *)(&C${CAN_INSTANCE_NUM}FIFOCON0 + (fifoNum * CAN_FIFO_OFFSET)) & _C${CAN_INSTANCE_NUM}FIFOCON0_FSIZE_MASK) >> _C${CAN_INSTANCE_NUM}FIFOCON0_FSIZE_POSITION);
    for (msgIndex = 0U; msgIndex <= fifoSize; msgIndex++)
    {
        if ((${CAN_INSTANCE_NAME?lower_case}MsgIndex[fifoNum] & (1UL << (msgIndex & 0x1FU))) == 0U)
        {
            ${CAN_INSTANCE_NAME?lower_case}MsgIndex[fifoNum] |= (1UL << (msgIndex & 0x1FU));
            break;
        }
    }
    if(msgIndex > fifoSize)
    {
        /* FIFO is full */
        return false;
    }
    ${CAN_INSTANCE_NAME?lower_case}RxMsg[fifoNum][msgIndex].id = id;
    ${CAN_INSTANCE_NAME?lower_case}RxMsg[fifoNum][msgIndex].buffer = data;
    ${CAN_INSTANCE_NAME?lower_case}RxMsg[fifoNum][msgIndex].size = length;
    ${CAN_INSTANCE_NAME?lower_case}RxMsg[fifoNum][msgIndex].timestamp = timestamp;
    ${CAN_INSTANCE_NAME?lower_case}RxMsg[fifoNum][msgIndex].msgAttr = msgAttr;
    *(volatile uint32_t *)(&C${CAN_INSTANCE_NUM}FIFOINT0SET + (fifoNum * CAN_FIFO_OFFSET)) = _C${CAN_INSTANCE_NUM}FIFOINT0_RXNEMPTYIE_MASK;
    C${CAN_INSTANCE_NUM}INTSET = _C${CAN_INSTANCE_NUM}INT_RBIE_MASK;
    status = true;
</#if>

    return status;
}

// *****************************************************************************
/* Function:
    void ${CAN_INSTANCE_NAME}_MessageAbort(uint8_t fifoNum)

   Summary:
    Abort request for a FIFO.

   Precondition:
    ${CAN_INSTANCE_NAME}_Initialize must have been called for the associated CAN instance.

   Parameters:
    fifoNum - FIFO number

   Returns:
    None.
*/
void ${CAN_INSTANCE_NAME}_MessageAbort(uint8_t fifoNum)
{
    if (fifoNum > (CAN_NUM_OF_FIFO - 1U))
    {
        return;
    }
    *(volatile uint32_t *)(&C${CAN_INSTANCE_NUM}FIFOCON0CLR + (fifoNum * CAN_FIFO_OFFSET)) = _C${CAN_INSTANCE_NUM}FIFOCON0_TXREQ_MASK;
}

// *****************************************************************************
/* Function:
    void ${CAN_INSTANCE_NAME}_MessageAcceptanceFilterSet(uint8_t filterNum, uint32_t id)

   Summary:
    Set Message acceptance filter configuration.

   Precondition:
    ${CAN_INSTANCE_NAME}_Initialize must have been called for the associated CAN instance.

   Parameters:
    filterNum - Filter number
    id        - 11-bit or 29-bit identifier

   Returns:
    None.
*/
void ${CAN_INSTANCE_NAME}_MessageAcceptanceFilterSet(uint8_t filterNum, uint32_t id)
{
    uint32_t filterEnableBit = 0;
    uint8_t filterRegIndex = 0;

    if (filterNum < CAN_NUM_OF_FILTER)
    {
        filterRegIndex = filterNum >> 2;
<#if NUMBER_OF_FILTER gt 1>
        filterEnableBit = ((filterNum % 4U) == 0U)? _C${CAN_INSTANCE_NUM}FLTCON0_FLTEN0_MASK : (1UL << ((((filterNum % 4U) + 1U) * 8U) - 1U));
<#else>
        filterEnableBit = _C${CAN_INSTANCE_NUM}FLTCON0_FLTEN0_MASK;
</#if>
        *(volatile uint32_t *)(&C${CAN_INSTANCE_NUM}FLTCON0CLR + (filterRegIndex * CAN_FILTER_OFFSET)) = filterEnableBit;

        if (id > CAN_MSG_SID_MASK)
        {
            *(volatile uint32_t *)(&C${CAN_INSTANCE_NUM}RXF0 + (filterNum * CAN_FILTER_OFFSET)) = (id & _C${CAN_INSTANCE_NUM}RXF0_EID_MASK)
                                                                           | (((id & 0x1FFC0000u) >> 18) << _C${CAN_INSTANCE_NUM}RXF0_SID_POSITION)
                                                                           | _C${CAN_INSTANCE_NUM}RXF0_EXID_MASK;
        }
        else
        {
            *(volatile uint32_t *)(&C${CAN_INSTANCE_NUM}RXF0 + (filterNum * CAN_FILTER_OFFSET)) = (id & CAN_MSG_SID_MASK) << _C${CAN_INSTANCE_NUM}RXF0_SID_POSITION;
        }
        *(volatile uint32_t *)(&C${CAN_INSTANCE_NUM}FLTCON0SET + (filterRegIndex * CAN_FILTER_OFFSET)) = filterEnableBit;
    }
}

// *****************************************************************************
/* Function:
    uint32_t ${CAN_INSTANCE_NAME}_MessageAcceptanceFilterGet(uint8_t filterNum)

   Summary:
    Get Message acceptance filter configuration.

   Precondition:
    ${CAN_INSTANCE_NAME}_Initialize must have been called for the associated CAN instance.

   Parameters:
    filterNum - Filter number

   Returns:
    Returns Message acceptance filter identifier
*/
uint32_t ${CAN_INSTANCE_NAME}_MessageAcceptanceFilterGet(uint8_t filterNum)
{
    uint32_t id = 0;

    if (filterNum < CAN_NUM_OF_FILTER)
    {
        if ((*(volatile uint32_t *)(&C${CAN_INSTANCE_NUM}RXF0 + (filterNum * CAN_FILTER_OFFSET)) & _C${CAN_INSTANCE_NUM}RXF0_EXID_MASK) != 0U)
        {
            id = (*(volatile uint32_t *)(&C${CAN_INSTANCE_NUM}RXF0 + (filterNum * CAN_FILTER_OFFSET)) & _C${CAN_INSTANCE_NUM}RXF0_EID_MASK);
            id = id | ((*(volatile uint32_t *)(&C${CAN_INSTANCE_NUM}RXF0 + (filterNum * CAN_FILTER_OFFSET)) & _C${CAN_INSTANCE_NUM}RXF0_SID_MASK) >> 3);
        }
        else
        {
            id = (*(volatile uint32_t *)(&C${CAN_INSTANCE_NUM}RXF0 + (filterNum * CAN_FILTER_OFFSET)) & _C${CAN_INSTANCE_NUM}RXF0_SID_MASK) >> _C${CAN_INSTANCE_NUM}RXF0_SID_POSITION;
        }
    }
    return id;
}

// *****************************************************************************
/* Function:
    void ${CAN_INSTANCE_NAME}_MessageAcceptanceFilterMaskSet(uint8_t acceptanceFilterMaskNum, uint32_t id)

   Summary:
    Set Message acceptance filter mask configuration.

   Precondition:
    ${CAN_INSTANCE_NAME}_Initialize must have been called for the associated CAN instance.

   Parameters:
    acceptanceFilterMaskNum - Acceptance Filter Mask number (0 to 3)
    id                      - 11-bit or 29-bit identifier

   Returns:
    None.
*/
void ${CAN_INSTANCE_NAME}_MessageAcceptanceFilterMaskSet(uint8_t acceptanceFilterMaskNum, uint32_t id)
{
    /* Switch the CAN module to Configuration mode. Wait until the switch is complete */
    C${CAN_INSTANCE_NUM}CON = (C${CAN_INSTANCE_NUM}CON & ~_C${CAN_INSTANCE_NUM}CON_REQOP_MASK) | ((CAN_CONFIGURATION_MODE << _C${CAN_INSTANCE_NUM}CON_REQOP_POSITION) & _C${CAN_INSTANCE_NUM}CON_REQOP_MASK);
    while(((C${CAN_INSTANCE_NUM}CON & _C${CAN_INSTANCE_NUM}CON_OPMOD_MASK) >> _C${CAN_INSTANCE_NUM}CON_OPMOD_POSITION) != CAN_CONFIGURATION_MODE)
    {
        /* Do Nothing */
    }

    if (id > CAN_MSG_SID_MASK)
    {
        *(volatile uint32_t *)(&C${CAN_INSTANCE_NUM}RXM0 + (acceptanceFilterMaskNum * CAN_ACCEPTANCE_MASK_OFFSET)) = (id & _C${CAN_INSTANCE_NUM}RXM0_EID_MASK)
                                                                       | (((id & 0x1FFC0000u) >> 18) << _C${CAN_INSTANCE_NUM}RXM0_SID_POSITION) | _C${CAN_INSTANCE_NUM}RXM0_MIDE_MASK;
    }
    else
    {
        *(volatile uint32_t *)(&C${CAN_INSTANCE_NUM}RXM0 + (acceptanceFilterMaskNum * CAN_ACCEPTANCE_MASK_OFFSET)) = (id & CAN_MSG_SID_MASK) << _C${CAN_INSTANCE_NUM}RXM0_SID_POSITION;
    }

    /* Switch the CAN module to CAN_OPERATION_MODE. Wait until the switch is complete */
    C${CAN_INSTANCE_NUM}CON = (C${CAN_INSTANCE_NUM}CON & ~_C${CAN_INSTANCE_NUM}CON_REQOP_MASK) | ((CAN_OPERATION_MODE << _C${CAN_INSTANCE_NUM}CON_REQOP_POSITION) & _C${CAN_INSTANCE_NUM}CON_REQOP_MASK);
    while(((C${CAN_INSTANCE_NUM}CON & _C${CAN_INSTANCE_NUM}CON_OPMOD_MASK) >> _C${CAN_INSTANCE_NUM}CON_OPMOD_POSITION) != CAN_OPERATION_MODE)
    {
       /* Do Nothing */
    }
}

// *****************************************************************************
/* Function:
    uint32_t ${CAN_INSTANCE_NAME}_MessageAcceptanceFilterMaskGet(uint8_t acceptanceFilterMaskNum)

   Summary:
    Get Message acceptance filter mask configuration.

   Precondition:
    ${CAN_INSTANCE_NAME}_Initialize must have been called for the associated CAN instance.

   Parameters:
    acceptanceFilterMaskNum - Acceptance Filter Mask number (0 to 3)

   Returns:
    Returns Message acceptance filter mask.
*/
uint32_t ${CAN_INSTANCE_NAME}_MessageAcceptanceFilterMaskGet(uint8_t acceptanceFilterMaskNum)
{
    uint32_t id = 0;

    if ((*(volatile uint32_t *)(&C${CAN_INSTANCE_NUM}RXM0 + (acceptanceFilterMaskNum * CAN_ACCEPTANCE_MASK_OFFSET)) & _C${CAN_INSTANCE_NUM}RXM0_MIDE_MASK) != 0U)
    {
        id = (*(volatile uint32_t *)(&C${CAN_INSTANCE_NUM}RXM0 + (acceptanceFilterMaskNum * CAN_ACCEPTANCE_MASK_OFFSET)) & _C${CAN_INSTANCE_NUM}RXM0_EID_MASK);
        id = id | ((*(volatile uint32_t *)(&C${CAN_INSTANCE_NUM}RXM0 + (acceptanceFilterMaskNum * CAN_ACCEPTANCE_MASK_OFFSET)) & _C${CAN_INSTANCE_NUM}RXM0_SID_MASK) >> 3);
    }
    else
    {
        id = (*(volatile uint32_t *)(&C${CAN_INSTANCE_NUM}RXM0 + (acceptanceFilterMaskNum * CAN_ACCEPTANCE_MASK_OFFSET)) & _C${CAN_INSTANCE_NUM}RXM0_SID_MASK) >> _C${CAN_INSTANCE_NUM}RXM0_SID_POSITION;
    }
    return id;
}

// *****************************************************************************
/* Function:
    CAN_ERROR ${CAN_INSTANCE_NAME}_ErrorGet(void)

   Summary:
    Returns the error during transfer.

   Precondition:
    ${CAN_INSTANCE_NAME}_Initialize must have been called for the associated CAN instance.

   Parameters:
    None.

   Returns:
    Error during transfer.
*/
CAN_ERROR ${CAN_INSTANCE_NAME}_ErrorGet(void)
{
<#if CAN_INTERRUPT_MODE == false>
    uint32_t error = (uint32_t)CAN_ERROR_NONE;
    uint32_t errorStatus = C${CAN_INSTANCE_NUM}TREC;

    /* Check if error occurred */
    error = ((errorStatus & _C${CAN_INSTANCE_NUM}TREC_EWARN_MASK) |
                (errorStatus & _C${CAN_INSTANCE_NUM}TREC_RXWARN_MASK) |
                (errorStatus & _C${CAN_INSTANCE_NUM}TREC_TXWARN_MASK) |
                (errorStatus & _C${CAN_INSTANCE_NUM}TREC_RXBP_MASK) |
                (errorStatus & _C${CAN_INSTANCE_NUM}TREC_TXBP_MASK) |
                (errorStatus & _C${CAN_INSTANCE_NUM}TREC_TXBO_MASK));

</#if>
<#if CAN_INTERRUPT_MODE == false>
    return (CAN_ERROR)error;
<#else>
    return (CAN_ERROR)${CAN_INSTANCE_NAME?lower_case}Obj.errorStatus;
</#if>
}

// *****************************************************************************
/* Function:
    void ${CAN_INSTANCE_NAME}_ErrorCountGet(uint8_t *txErrorCount, uint8_t *rxErrorCount)

   Summary:
    Returns the transmit and receive error count during transfer.

   Precondition:
    ${CAN_INSTANCE_NAME}_Initialize must have been called for the associated CAN instance.

   Parameters:
    txErrorCount - Transmit Error Count to be received
    rxErrorCount - Receive Error Count to be received

   Returns:
    None.
*/
void ${CAN_INSTANCE_NAME}_ErrorCountGet(uint8_t *txErrorCount, uint8_t *rxErrorCount)
{
    *txErrorCount = (uint8_t)((C${CAN_INSTANCE_NUM}TREC & _C${CAN_INSTANCE_NUM}TREC_TERRCNT_MASK) >> _C${CAN_INSTANCE_NUM}TREC_TERRCNT_POSITION);
    *rxErrorCount = (uint8_t)(C${CAN_INSTANCE_NUM}TREC & _C${CAN_INSTANCE_NUM}TREC_RERRCNT_MASK);
}

// *****************************************************************************
/* Function:
    bool ${CAN_INSTANCE_NAME}_InterruptGet(uint8_t fifoNum, CAN_FIFO_INTERRUPT_FLAG_MASK fifoInterruptFlagMask)

   Summary:
    Returns the FIFO Interrupt status.

   Precondition:
    ${CAN_INSTANCE_NAME}_Initialize must have been called for the associated CAN instance.

   Parameters:
    fifoNum               - FIFO number
    fifoInterruptFlagMask - FIFO interrupt flag mask

   Returns:
    true - Requested fifo interrupt is occurred.
    false - Requested fifo interrupt is not occurred.
*/
bool ${CAN_INSTANCE_NAME}_InterruptGet(uint8_t fifoNum, CAN_FIFO_INTERRUPT_FLAG_MASK fifoInterruptFlagMask)
{
    if (fifoNum > (CAN_NUM_OF_FIFO - 1U))
    {
        return false;
    }
    return ((*(volatile uint32_t *)(&C${CAN_INSTANCE_NUM}FIFOINT0 + (fifoNum * CAN_FIFO_OFFSET)) & fifoInterruptFlagMask) != 0x0U);
}

// *****************************************************************************
/* Function:
    bool ${CAN_INSTANCE_NAME}_TxFIFOIsFull(uint8_t fifoNum)

   Summary:
    Returns true if Tx FIFO is full otherwise false.

   Precondition:
    ${CAN_INSTANCE_NAME}_Initialize must have been called for the associated CAN instance.

   Parameters:
    fifoNum - FIFO number

   Returns:
    true  - Tx FIFO is full.
    false - Tx FIFO is not full.
*/
bool ${CAN_INSTANCE_NAME}_TxFIFOIsFull(uint8_t fifoNum)
{
    return ((*(volatile uint32_t *)(&C${CAN_INSTANCE_NUM}FIFOINT0 + (fifoNum * CAN_FIFO_OFFSET)) & _C${CAN_INSTANCE_NUM}FIFOINT0_TXNFULLIF_MASK) != _C${CAN_INSTANCE_NUM}FIFOINT0_TXNFULLIF_MASK);
}

// *****************************************************************************
/* Function:
    bool ${CAN_INSTANCE_NAME}_AutoRTRResponseSet(uint32_t id, uint8_t length, uint8_t* data, uint8_t fifoNum)

   Summary:
    Set the Auto RTR response for remote transmit request.

   Precondition:
    ${CAN_INSTANCE_NAME}_Initialize must have been called for the associated CAN instance.
    Auto RTR Enable must be set to 0x1 for the requested Transmit FIFO in MHC configuration.

   Parameters:
    id          - 11-bit / 29-bit identifier (ID).
    length      - length of data buffer in number of bytes.
    data        - pointer to source data buffer
    fifoNum     - FIFO number

   Returns:
    Request status.
    true  - Request was successful.
    false - Request has failed.
*/
bool ${CAN_INSTANCE_NAME}_AutoRTRResponseSet(uint32_t id, uint8_t length, uint8_t* data, uint8_t fifoNum)
{
    CAN_TX_RX_MSG_BUFFER *txMessage = NULL;
    uint8_t count = 0;
    bool status = false;

    if ((*(volatile uint32_t *)(&C${CAN_INSTANCE_NUM}FIFOINT0 + (fifoNum * CAN_FIFO_OFFSET)) & _C${CAN_INSTANCE_NUM}FIFOINT0_TXNFULLIF_MASK) == _C${CAN_INSTANCE_NUM}FIFOINT0_TXNFULLIF_MASK)
    {
        txMessage = (CAN_TX_RX_MSG_BUFFER *)PA_TO_KVA1(*(volatile uint32_t *)(&C${CAN_INSTANCE_NUM}FIFOUA0 + (fifoNum * CAN_FIFO_OFFSET)));

        /* Check the id whether it falls under SID or EID,
         * SID max limit is 0x7FF, so anything beyond that is EID */
        if (id > CAN_MSG_SID_MASK)
        {
            txMessage->msgSID = (id & CAN_MSG_EID_MASK) >> 18;
            txMessage->msgEID = ((id & 0x3FFFFUL) << 10) | CAN_MSG_IDE_MASK | CAN_MSG_SRR_MASK;
        }
        else
        {
            txMessage->msgSID = id;
            txMessage->msgEID = 0U;
        }

        if (length > 8U)
        {
            length = 8U;
        }
        txMessage->msgEID |= length;

        while(count < length)
        {
            txMessage->msgData[count++] = *data++;
        }

<#if CAN_INTERRUPT_MODE == true>
        *(volatile uint32_t *)(&C${CAN_INSTANCE_NUM}FIFOINT0SET + (fifoNum * CAN_FIFO_OFFSET)) = _C${CAN_INSTANCE_NUM}FIFOINT0_TXEMPTYIE_MASK;

</#if>
        /* Set UINC to respond to RTR */
        *(volatile uint32_t *)(&C${CAN_INSTANCE_NUM}FIFOCON0SET + (fifoNum * CAN_FIFO_OFFSET)) = _C${CAN_INSTANCE_NUM}FIFOCON0_UINC_MASK;

<#if CAN_INTERRUPT_MODE == true>
        C${CAN_INSTANCE_NUM}INTSET = _C${CAN_INSTANCE_NUM}INT_TBIE_MASK;

</#if>
        status = true;
    }
    return status;
}

bool ${CAN_INSTANCE_NAME}_BitTimingCalculationGet(CAN_BIT_TIMING_SETUP *setup, CAN_BIT_TIMING *bitTiming)
{
    bool status = false;
    uint32_t numOfTimeQuanta;
    uint8_t phase1;
    float temp1;
    float temp2;

    if ((setup != NULL) && (bitTiming != NULL))
    {
        if (setup->nominalBitTimingSet == true)
        {
            numOfTimeQuanta = ${CAN_INSTANCE_NAME}_CLOCK_FREQUENCY / (setup->nominalBitRate * (2U * ((uint32_t)setup->nominalPrescaler + 1U)));
            if ((numOfTimeQuanta >= 8U) && (numOfTimeQuanta <= 25U))
            {
                if (setup->nominalSamplePoint < 50.0f)
                {
                    setup->nominalSamplePoint = 50.0f;
                }
                temp1 = (float)numOfTimeQuanta;
                temp2 = (temp1 * setup->nominalSamplePoint) / 100.0f;
                phase1 = (uint8_t)temp2;
                bitTiming->nominalBitTiming.phase2Segment = (uint8_t)(numOfTimeQuanta - phase1 - 1U);
                /* The propagation segment time is equal to twice the sum of the signal's propagation time on the bus line,
                   the receiver delay and the output driver delay */
                temp2 = (((float)numOfTimeQuanta * ((float)setup->nominalBitRate / 1000.0f) * (float)setup->nominalPropagTime) / 1000000.0f);
                bitTiming->nominalBitTiming.propagationSegment = ((uint8_t)temp2 - 1U);
                bitTiming->nominalBitTiming.phase1Segment = phase1 - (bitTiming->nominalBitTiming.propagationSegment + 1U) - 2U;
                if ((bitTiming->nominalBitTiming.phase2Segment + 1U) > 4U)
                {
                    bitTiming->nominalBitTiming.sjw = 3U;
                }
                else
                {
                    bitTiming->nominalBitTiming.sjw = bitTiming->nominalBitTiming.phase2Segment;
                }
                bitTiming->nominalBitTiming.Prescaler = setup->nominalPrescaler;
                bitTiming->nominalBitTimingSet = true;
                status = true;
            }
            else
            {
                bitTiming->nominalBitTimingSet = false;
            }
        }
    }

    return status;
}

bool ${CAN_INSTANCE_NAME}_BitTimingSet(CAN_BIT_TIMING *bitTiming)
{
    bool status = false;

    if ((bitTiming->nominalBitTimingSet == true)
    && (bitTiming->nominalBitTiming.phase1Segment <= 0x7U)
    && (bitTiming->nominalBitTiming.phase2Segment <= 0x7U)
    && (bitTiming->nominalBitTiming.propagationSegment <= 0x7U)
    && ((bitTiming->nominalBitTiming.Prescaler >= 0x1U) && (bitTiming->nominalBitTiming.Prescaler <= 0x3FU))
    && (bitTiming->nominalBitTiming.sjw <= 0x3U))
    {
        /* Switch the CAN module to Configuration mode. Wait until the switch is complete */
        C${CAN_INSTANCE_NUM}CON = (C${CAN_INSTANCE_NUM}CON & ~_C${CAN_INSTANCE_NUM}CON_REQOP_MASK) | ((CAN_CONFIGURATION_MODE << _C${CAN_INSTANCE_NUM}CON_REQOP_POSITION) & _C${CAN_INSTANCE_NUM}CON_REQOP_MASK);
        while(((C${CAN_INSTANCE_NUM}CON & _C${CAN_INSTANCE_NUM}CON_OPMOD_MASK) >> _C${CAN_INSTANCE_NUM}CON_OPMOD_POSITION) != CAN_CONFIGURATION_MODE)
        {
             /* Do Nothing */
        }

        /* Set the Bitrate */
        C${CAN_INSTANCE_NUM}CFG = (((uint32_t)bitTiming->nominalBitTiming.Prescaler << _C${CAN_INSTANCE_NUM}CFG_BRP_POSITION) & _C${CAN_INSTANCE_NUM}CFG_BRP_MASK)
                                | (((uint32_t)bitTiming->nominalBitTiming.sjw << _C${CAN_INSTANCE_NUM}CFG_SJW_POSITION) & _C${CAN_INSTANCE_NUM}CFG_SJW_MASK)
                                | (((uint32_t)bitTiming->nominalBitTiming.phase2Segment << _C${CAN_INSTANCE_NUM}CFG_SEG2PH_POSITION) & _C${CAN_INSTANCE_NUM}CFG_SEG2PH_MASK)
                                | (((uint32_t)bitTiming->nominalBitTiming.phase1Segment << _C${CAN_INSTANCE_NUM}CFG_SEG1PH_POSITION) & _C${CAN_INSTANCE_NUM}CFG_SEG1PH_MASK)
                                | (((uint32_t)bitTiming->nominalBitTiming.propagationSegment << _C${CAN_INSTANCE_NUM}CFG_PRSEG_POSITION) & _C${CAN_INSTANCE_NUM}CFG_PRSEG_MASK)
                                | _C${CAN_INSTANCE_NUM}CFG_SEG2PHTS_MASK<#if CAN_CFG_SAM == "0x1"> | _C${CAN_INSTANCE_NUM}CFG_SAM_MASK</#if>;

        /* Switch the CAN module to CAN_OPERATION_MODE. Wait until the switch is complete */
        <#if CAN_OPMODE == "0x1">
        C${CAN_INSTANCE_NUM}CON = (C${CAN_INSTANCE_NUM}CON & ~_C${CAN_INSTANCE_NUM}CON_REQOP_MASK);
        while(((C${CAN_INSTANCE_NUM}CON & _C${CAN_INSTANCE_NUM}CON_OPMOD_MASK) >> _C${CAN_INSTANCE_NUM}CON_OPMOD_POSITION) != 0)
        {
            /* Do Nothing */
        }
        </#if>
        C${CAN_INSTANCE_NUM}CON = (C${CAN_INSTANCE_NUM}CON & ~_C${CAN_INSTANCE_NUM}CON_REQOP_MASK) | ((CAN_OPERATION_MODE << _C${CAN_INSTANCE_NUM}CON_REQOP_POSITION) & _C${CAN_INSTANCE_NUM}CON_REQOP_MASK);
        while(((C${CAN_INSTANCE_NUM}CON & _C${CAN_INSTANCE_NUM}CON_OPMOD_MASK) >> _C${CAN_INSTANCE_NUM}CON_OPMOD_POSITION) != CAN_OPERATION_MODE)
        {
            /* Do Nothing */
        }
        status = true;
    }
    return status;
}

<#if CAN_INTERRUPT_MODE == true>
// *****************************************************************************
/* Function:
    void ${CAN_INSTANCE_NAME}_CallbackRegister(CAN_CALLBACK callback, uintptr_t contextHandle, uint8_t fifoNum)

   Summary:
    Sets the pointer to the function (and it's context) to be called when the
    given CAN's transfer events occur.

   Precondition:
    ${CAN_INSTANCE_NAME}_Initialize must have been called for the associated CAN instance.

   Parameters:
    callback - A pointer to a function with a calling signature defined
    by the CAN_CALLBACK data type.

    fifoNum - Tx/Rx FIFO number

    context - A value (usually a pointer) passed (unused) into the function
    identified by the callback parameter.

   Returns:
    None.
*/
void ${CAN_INSTANCE_NAME}_CallbackRegister(CAN_CALLBACK callback, uintptr_t contextHandle, uint8_t fifoNum)
{
    if (callback != NULL)
    {
        ${CAN_INSTANCE_NAME?lower_case}CallbackObj[fifoNum].callback = callback;
        ${CAN_INSTANCE_NAME?lower_case}CallbackObj[fifoNum].context = contextHandle;
    }
    return;
}

// *****************************************************************************
/* Function:
    void ${CAN_INSTANCE_NAME}_ErrorCallbackRegister(CAN_CALLBACK callback, uintptr_t contextHandle)

   Summary:
    Sets the pointer to the function (and it's context) to be called when the
    given CAN's transfer events occur.

   Precondition:
    ${CAN_INSTANCE_NAME}_Initialize must have been called for the associated CAN instance.

   Parameters:
    callback - A pointer to a function with a calling signature defined
    by the CAN_CALLBACK data type.

    context - A value (usually a pointer) passed (unused) into the function
    identified by the callback parameter.

   Returns:
    None.
*/
void ${CAN_INSTANCE_NAME}_ErrorCallbackRegister(CAN_CALLBACK callback, uintptr_t contextHandle)
{
    if (callback != NULL)
    {
        ${CAN_INSTANCE_NAME?lower_case}ErrorCallbackObj.callback = callback;
        ${CAN_INSTANCE_NAME?lower_case}ErrorCallbackObj.context = contextHandle;
    }
    return;
}

// *****************************************************************************
/* Function:
    void __attribute__((used)) ${CAN_INSTANCE_NAME}_InterruptHandler(void)

   Summary:
    ${CAN_INSTANCE_NAME} Peripheral Interrupt Handler.

   Description:
    This function is ${CAN_INSTANCE_NAME} Peripheral Interrupt Handler and will
    called on every ${CAN_INSTANCE_NAME} interrupt.

   Precondition:
    None.

   Parameters:
    None.

   Returns:
    None.

   Remarks:
    The function is called as peripheral instance's interrupt handler if the
    instance interrupt is enabled. If peripheral instance's interrupt is not
    enabled user need to call it from the main while loop of the application.
*/
void __attribute__((used)) ${CAN_INSTANCE_NAME}_InterruptHandler(void)
{
    uint8_t  msgIndex = 0;
    uint8_t  fifoNum = 0;
    uint8_t  fifoSize = 0;
    uint8_t  count = 0;
    CAN_TX_RX_MSG_BUFFER *rxMessage = NULL;
    uint32_t interruptStatus = 0;
    /* Additional temporary variable used to prevent MISRA violations (Rule 13.x) */
    uintptr_t context;

    interruptStatus = C${CAN_INSTANCE_NUM}INT;
    /* Check if error occurred */
    if ((interruptStatus & (_C${CAN_INSTANCE_NUM}INT_SERRIF_MASK | _C${CAN_INSTANCE_NUM}INT_CERRIF_MASK | _C${CAN_INSTANCE_NUM}INT_IVRIF_MASK)) != 0U)
    {
        C${CAN_INSTANCE_NUM}INTCLR = _C${CAN_INSTANCE_NUM}INT_SERRIE_MASK | _C${CAN_INSTANCE_NUM}INT_CERRIE_MASK | _C${CAN_INSTANCE_NUM}INT_IVRIE_MASK
                 | _C${CAN_INSTANCE_NUM}INT_SERRIF_MASK | _C${CAN_INSTANCE_NUM}INT_CERRIF_MASK | _C${CAN_INSTANCE_NUM}INT_IVRIF_MASK;
        ${CAN_IFS_REG}CLR = _${CAN_IFS_REG}_CAN${CAN_INSTANCE_NUM}IF_MASK;
        C${CAN_INSTANCE_NUM}INTSET = _C${CAN_INSTANCE_NUM}INT_SERRIE_MASK | _C${CAN_INSTANCE_NUM}INT_CERRIE_MASK | _C${CAN_INSTANCE_NUM}INT_IVRIE_MASK;
        uint32_t errorStatus = C${CAN_INSTANCE_NUM}TREC;

        /* Check if error occurred */
        ${CAN_INSTANCE_NAME?lower_case}Obj.errorStatus = ((errorStatus & _C${CAN_INSTANCE_NUM}TREC_EWARN_MASK) |
                                                          (errorStatus & _C${CAN_INSTANCE_NUM}TREC_RXWARN_MASK) |
                                                          (errorStatus & _C${CAN_INSTANCE_NUM}TREC_TXWARN_MASK) |
                                                          (errorStatus & _C${CAN_INSTANCE_NUM}TREC_RXBP_MASK) |
                                                          (errorStatus & _C${CAN_INSTANCE_NUM}TREC_TXBP_MASK) |
                                                          (errorStatus & _C${CAN_INSTANCE_NUM}TREC_TXBO_MASK));

        /* Client must call ${CAN_INSTANCE_NAME}_ErrorGet and ${CAN_INSTANCE_NAME}_ErrorCountGet functions to get errors */
        if (${CAN_INSTANCE_NAME?lower_case}ErrorCallbackObj.callback != NULL)
        {
            context = ${CAN_INSTANCE_NAME?lower_case}ErrorCallbackObj.context;
            ${CAN_INSTANCE_NAME?lower_case}ErrorCallbackObj.callback(context);
        }
    }
    else
    {
        ${CAN_INSTANCE_NAME?lower_case}Obj.errorStatus = 0U;
        if ((C${CAN_INSTANCE_NUM}INT & _C${CAN_INSTANCE_NUM}INT_RBIF_MASK) != 0U)
        {
            fifoNum = (uint8_t)C${CAN_INSTANCE_NUM}VEC & (uint8_t)_C${CAN_INSTANCE_NUM}VEC_ICODE_MASK;
            if (fifoNum < CAN_NUM_OF_FIFO)
            {
                fifoSize = (uint8_t)((*(volatile uint32_t *)(&C${CAN_INSTANCE_NUM}FIFOCON0 + (fifoNum * CAN_FIFO_OFFSET)) & _C${CAN_INSTANCE_NUM}FIFOCON0_FSIZE_MASK) >> _C${CAN_INSTANCE_NUM}FIFOCON0_FSIZE_POSITION);
                for (msgIndex = 0U; msgIndex <= fifoSize; msgIndex++)
                {
                    if ((${CAN_INSTANCE_NAME?lower_case}MsgIndex[fifoNum] & (1UL << (msgIndex & 0x1FU))) == (1UL << (msgIndex & 0x1FU)))
                    {
                        ${CAN_INSTANCE_NAME?lower_case}MsgIndex[fifoNum] &= ~(1UL << (msgIndex & 0x1FU));
                        break;
                    }
                }
                /* Get a pointer to RX message buffer */
                rxMessage = (CAN_TX_RX_MSG_BUFFER *)PA_TO_KVA1(*(volatile uint32_t *)(&C${CAN_INSTANCE_NUM}FIFOUA0 + (fifoNum * CAN_FIFO_OFFSET)));

                /* Check if it's a extended message type */
                if ((rxMessage->msgEID & CAN_MSG_IDE_MASK) != 0U)
                {
                    *${CAN_INSTANCE_NAME?lower_case}RxMsg[fifoNum][msgIndex].id = ((rxMessage->msgSID & CAN_MSG_SID_MASK) << 18) | ((rxMessage->msgEID >> 10) & _C${CAN_INSTANCE_NUM}RXM0_EID_MASK);
                    if ((rxMessage->msgEID & CAN_MSG_RTR_MASK) != 0U)
                    {
                        *${CAN_INSTANCE_NAME?lower_case}RxMsg[fifoNum][msgIndex].msgAttr = CAN_MSG_RX_REMOTE_FRAME;
                    }
                    else
                    {
                        *${CAN_INSTANCE_NAME?lower_case}RxMsg[fifoNum][msgIndex].msgAttr = CAN_MSG_RX_DATA_FRAME;
                    }
                }
                else
                {
                    *${CAN_INSTANCE_NAME?lower_case}RxMsg[fifoNum][msgIndex].id = rxMessage->msgSID & CAN_MSG_SID_MASK;
                    if ((rxMessage->msgEID & CAN_MSG_SRR_MASK) != 0U)
                    {
                        *${CAN_INSTANCE_NAME?lower_case}RxMsg[fifoNum][msgIndex].msgAttr = CAN_MSG_RX_REMOTE_FRAME;
                    }
                    else
                    {
                        *${CAN_INSTANCE_NAME?lower_case}RxMsg[fifoNum][msgIndex].msgAttr = CAN_MSG_RX_DATA_FRAME;
                    }
                }

                *${CAN_INSTANCE_NAME?lower_case}RxMsg[fifoNum][msgIndex].size = (uint8_t)(rxMessage->msgEID & CAN_MSG_DLC_MASK);

                /* Copy the data into the payload */
                while (count < *${CAN_INSTANCE_NAME?lower_case}RxMsg[fifoNum][msgIndex].size)
                {
                    *${CAN_INSTANCE_NAME?lower_case}RxMsg[fifoNum][msgIndex].buffer++ = rxMessage->msgData[count++];
                }

                if (${CAN_INSTANCE_NAME?lower_case}RxMsg[fifoNum][msgIndex].timestamp != NULL)
                {
                    *${CAN_INSTANCE_NAME?lower_case}RxMsg[fifoNum][msgIndex].timestamp = (uint16_t)((rxMessage->msgSID & CAN_MSG_TIMESTAMP_MASK) >> 16);
                }

                /* Message processing is done, update the message buffer pointer. */
                *(volatile uint32_t *)(&C${CAN_INSTANCE_NUM}FIFOCON0SET + (fifoNum * CAN_FIFO_OFFSET)) = _C${CAN_INSTANCE_NUM}FIFOCON0_UINC_MASK;

                if (((*(volatile uint32_t *)(&C${CAN_INSTANCE_NUM}FIFOINT0 + (fifoNum * CAN_FIFO_OFFSET)) & _C${CAN_INSTANCE_NUM}FIFOINT0_RXNEMPTYIF_MASK) != _C${CAN_INSTANCE_NUM}FIFOINT0_RXNEMPTYIF_MASK) ||
                    (${CAN_INSTANCE_NAME?lower_case}MsgIndex[fifoNum] == 0U))
                {
                    *(volatile uint32_t *)(&C${CAN_INSTANCE_NUM}FIFOINT0CLR + (fifoNum * CAN_FIFO_OFFSET)) = _C${CAN_INSTANCE_NUM}FIFOINT0_RXNEMPTYIE_MASK;
                }
            }
            ${CAN_IFS_REG}CLR = _${CAN_IFS_REG}_CAN${CAN_INSTANCE_NUM}IF_MASK;

            if (${CAN_INSTANCE_NAME?lower_case}CallbackObj[fifoNum].callback != NULL)
            {
                context = ${CAN_INSTANCE_NAME?lower_case}CallbackObj[fifoNum].context;
                ${CAN_INSTANCE_NAME?lower_case}CallbackObj[fifoNum].callback(context);
            }
        }
        if ((C${CAN_INSTANCE_NUM}INT & _C${CAN_INSTANCE_NUM}INT_TBIF_MASK) != 0U)
        {
            fifoNum = (uint8_t)(C${CAN_INSTANCE_NUM}VEC & _C${CAN_INSTANCE_NUM}VEC_ICODE_MASK);
            if (fifoNum < CAN_NUM_OF_FIFO)
            {
                *(volatile uint32_t *)(&C${CAN_INSTANCE_NUM}FIFOINT0CLR + (fifoNum * CAN_FIFO_OFFSET)) = _C${CAN_INSTANCE_NUM}FIFOINT0_TXEMPTYIE_MASK;
            }
            C${CAN_INSTANCE_NUM}INTCLR = _C${CAN_INSTANCE_NUM}INT_TBIE_MASK;
            ${CAN_IFS_REG}CLR = _${CAN_IFS_REG}_CAN${CAN_INSTANCE_NUM}IF_MASK;

            if (${CAN_INSTANCE_NAME?lower_case}CallbackObj[fifoNum].callback != NULL)
            {
                context = ${CAN_INSTANCE_NAME?lower_case}CallbackObj[fifoNum].context;
                ${CAN_INSTANCE_NAME?lower_case}CallbackObj[fifoNum].callback(context);
            }
        }
    }
}
</#if>
<#if core.COVERITY_SUPPRESS_DEVIATION?? && core.COVERITY_SUPPRESS_DEVIATION>
#pragma coverity compliance end_block "MISRA C-2012 Rule 11.6"
#pragma coverity compliance end_block "MISRA C-2012 Rule 5.1"
#pragma GCC diagnostic pop
</#if>
/* MISRAC 2012 deviation block end */