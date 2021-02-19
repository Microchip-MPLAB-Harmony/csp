/*******************************************************************************
  CANFD Peripheral Library Interface Source File

  Company:
    Microchip Technology Inc.

  File Name:
    plib_canfd${CAN_INSTANCE_NUM}.c

  Summary:
    CANFD peripheral library interface.

  Description:
    This file defines the interface to the CANFD peripheral library. This
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
#include "plib_canfd${CAN_INSTANCE_NUM}.h"

<#assign CAN_NBT_TSEG1  = NBT_TSEG1 - 1>
<#assign CAN_NBT_TSEG2  = NBT_TSEG2 - 1>
<#assign CAN_NBT_SJW    = NBT_SJW - 1>
<#assign CAN_DBT_TSEG1  = DBT_TSEG1 - 1>
<#assign CAN_DBT_TSEG2  = DBT_TSEG2 - 1>
<#assign CAN_DBT_SJW    = DBT_SJW - 1>
<#-- Message memory configuration -->
<#assign MESSAGE_RAM_SIZE = 0>
<#assign NUMBER_OF_RX_FIFO = 0>
<#if TX_EVENT_FIFO_USE == true>
    <#if CAN_TIMESTAMP_ENABLE == true>
        <#assign MESSAGE_RAM_SIZE = MESSAGE_RAM_SIZE + (TX_EVENT_FIFO_MESSAGE_BUFFER * 12)>
    <#else>
        <#assign MESSAGE_RAM_SIZE = MESSAGE_RAM_SIZE + (TX_EVENT_FIFO_MESSAGE_BUFFER * 8)>
    </#if>
</#if>
<#if TX_QUEUE_USE == true>
    <#if TX_QUEUE_PAYLOAD_SIZE?keep_after("0x")?number < 5>
        <#assign TX_QUEUE_OBJECT_SIZE = 16 + TX_QUEUE_PAYLOAD_SIZE?keep_after("0x")?number * 4>
    <#else>
        <#assign TX_QUEUE_OBJECT_SIZE = 40 + 16 * (TX_QUEUE_PAYLOAD_SIZE?keep_after("0x")?number - 5)>
    </#if>
    <#assign MESSAGE_RAM_SIZE = MESSAGE_RAM_SIZE + (TX_QUEUE_MESSAGE_BUFFER * TX_QUEUE_OBJECT_SIZE)>
</#if>
<#list 1..NUMBER_OF_FIFO as fifo>
    <#assign TX_FIFO_ENABLE = CAN_INSTANCE_NAME + "_FIFO" + fifo + "_TXEN">
    <#assign FIFO_PAYLOAD_SIZE = CAN_INSTANCE_NAME + "_FIFO" + fifo + "_PAYLOAD_SIZE">
    <#assign FIFO_MESSAGE_BUFFER_NUM = CAN_INSTANCE_NAME + "_FIFO" + fifo + "_SIZE">
    <#if .vars[TX_FIFO_ENABLE] == "0x1">
        <#if .vars[FIFO_PAYLOAD_SIZE]?keep_after("0x")?number < 5>
            <#assign TX_FIFO_OBJECT_SIZE = 16 + .vars[FIFO_PAYLOAD_SIZE]?keep_after("0x")?number * 4>
        <#else>
            <#assign TX_FIFO_OBJECT_SIZE = 40 + 16 * (.vars[FIFO_PAYLOAD_SIZE]?keep_after("0x")?number - 5)>
        </#if>
        <#assign MESSAGE_RAM_SIZE = MESSAGE_RAM_SIZE + (.vars[FIFO_MESSAGE_BUFFER_NUM] * TX_FIFO_OBJECT_SIZE)>
    <#else>
        <#assign NUMBER_OF_RX_FIFO += 1>
        <#if .vars[FIFO_PAYLOAD_SIZE]?keep_after("0x")?number < 5>
            <#if CAN_TIMESTAMP_ENABLE == true>
                <#assign RX_FIFO_OBJECT_SIZE = 20 + .vars[FIFO_PAYLOAD_SIZE]?keep_after("0x")?number * 4>
            <#else>
                <#assign RX_FIFO_OBJECT_SIZE = 16 + .vars[FIFO_PAYLOAD_SIZE]?keep_after("0x")?number * 4>
            </#if>
        <#else>
            <#if CAN_TIMESTAMP_ENABLE == true>
                <#assign RX_FIFO_OBJECT_SIZE = 44 + 16 * (.vars[FIFO_PAYLOAD_SIZE]?keep_after("0x")?number - 5)>
            <#else>
                <#assign RX_FIFO_OBJECT_SIZE = 40 + 16 * (.vars[FIFO_PAYLOAD_SIZE]?keep_after("0x")?number - 5)>
            </#if>
        </#if>
        <#assign MESSAGE_RAM_SIZE = MESSAGE_RAM_SIZE + (.vars[FIFO_MESSAGE_BUFFER_NUM] * RX_FIFO_OBJECT_SIZE)>
    </#if>
</#list>

// *****************************************************************************
// *****************************************************************************
// Global Data
// *****************************************************************************
// *****************************************************************************
/* ${CAN_INSTANCE_NAME} Message memory size */
#define CANFD_MESSAGE_RAM_CONFIG_SIZE ${MESSAGE_RAM_SIZE}
/* Number of configured FIFO */
#define CANFD_NUM_OF_FIFO             ${NUMBER_OF_FIFO}
/* Maximum number of CAN Message buffers in each FIFO */
#define CANFD_FIFO_MESSAGE_BUFFER_MAX 32

#define CANFD_CONFIGURATION_MODE      0x4
#define CANFD_OPERATION_MODE          ${CAN_OPMODE}
#define CANFD_NUM_OF_FILTER           ${NUMBER_OF_FILTER}
/* FIFO Offset in word (4 bytes) */
#define CANFD_FIFO_OFFSET             ${FIFO_OFFSET}
/* Filter Offset in word (4 bytes) */
#define CANFD_FILTER_OFFSET           ${FILTER_OFFSET}
#define CANFD_FILTER_OBJ_OFFSET       ${FILTER_OBJ_MASK_OFFSET}
/* Acceptance Mask Offset in word (4 bytes) */
#define CANFD_ACCEPTANCE_MASK_OFFSET  ${FILTER_OBJ_MASK_OFFSET}
#define CANFD_MSG_SID_MASK            0x7FF
#define CANFD_MSG_EID_MASK            0x1FFFFFFF
#define CANFD_MSG_DLC_MASK            0x0000000F
#define CANFD_MSG_IDE_MASK            0x00000010
#define CANFD_MSG_RTR_MASK            0x00000020
#define CANFD_MSG_BRS_MASK            0x00000040
#define CANFD_MSG_FDF_MASK            0x00000080
#define CANFD_MSG_SEQ_MASK            0xFFFFFE00
#define CANFD_MSG_TX_EXT_SID_MASK     0x1FFC0000
#define CANFD_MSG_TX_EXT_EID_MASK     0x0003FFFF
#define CANFD_MSG_RX_EXT_SID_MASK     0x000007FF
#define CANFD_MSG_RX_EXT_EID_MASK     0x1FFFF800
#define CANFD_MSG_FLT_EXT_SID_MASK    0x1FFC0000
#define CANFD_MSG_FLT_EXT_EID_MASK    0x0003FFFF

<#if CAN_INTERRUPT_MODE == true>
static CANFD_OBJ ${CAN_INSTANCE_NAME?lower_case}Obj;
static CANFD_RX_MSG ${CAN_INSTANCE_NAME?lower_case}RxMsg[CANFD_NUM_OF_FIFO][CANFD_FIFO_MESSAGE_BUFFER_MAX];
static CANFD_CALLBACK_OBJ ${CAN_INSTANCE_NAME?lower_case}CallbackObj[CANFD_NUM_OF_FIFO + 1];
static CANFD_CALLBACK_OBJ ${CAN_INSTANCE_NAME?lower_case}ErrorCallbackObj;
static uint32_t ${CAN_INSTANCE_NAME?lower_case}MsgIndex[CANFD_NUM_OF_FIFO];
</#if>
static uint8_t __attribute__((coherent, aligned(16))) can_message_buffer[CANFD_MESSAGE_RAM_CONFIG_SIZE];
static const uint8_t dlcToLength[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 12, 16, 20, 24, 32, 48, 64};

<#if CAN_OPMODE != "0x6">
/******************************************************************************
Local Functions
******************************************************************************/
static void CANLengthToDlcGet(uint8_t length, uint8_t *dlc)
{
    if (length <= 8)
    {
        *dlc = length;
    }
    else if (length <= 12)
    {
        *dlc = 0x9;
    }
    else if (length <= 16)
    {
        *dlc = 0xA;
    }
    else if (length <= 20)
    {
        *dlc = 0xB;
    }
    else if (length <= 24)
    {
        *dlc = 0xC;
    }
    else if (length <= 32)
    {
        *dlc = 0xD;
    }
    else if (length <= 48)
    {
        *dlc = 0xE;
    }
    else
    {
        *dlc = 0xF;
    }
}
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
    CFD${CAN_INSTANCE_NUM}CON |= _CFD${CAN_INSTANCE_NUM}CON_ON_MASK<#if CAN_CORE_SELECT_CLOCK_SOURCE == "0x1"> | _CFD${CAN_INSTANCE_NUM}CON_CLKSEL0_MASK</#if>;

    /* Switch the CAN module to Configuration mode. Wait until the switch is complete */
    CFD${CAN_INSTANCE_NUM}CON = (CFD${CAN_INSTANCE_NUM}CON & ~_CFD${CAN_INSTANCE_NUM}CON_REQOP_MASK) | ((CANFD_CONFIGURATION_MODE << _CFD${CAN_INSTANCE_NUM}CON_REQOP_POSITION) & _CFD${CAN_INSTANCE_NUM}CON_REQOP_MASK);
    while(((CFD${CAN_INSTANCE_NUM}CON & _CFD${CAN_INSTANCE_NUM}CON_OPMOD_MASK) >> _CFD${CAN_INSTANCE_NUM}CON_OPMOD_POSITION) != CANFD_CONFIGURATION_MODE);

<#if CAN_OPMODE != "0x6">
    /* Set the Data bitrate to ${DATA_BITRATE} Kbps */
    CFD${CAN_INSTANCE_NUM}DBTCFG = ((${DBT_BRP} << _CFD${CAN_INSTANCE_NUM}DBTCFG_BRP_POSITION) & _CFD${CAN_INSTANCE_NUM}DBTCFG_BRP_MASK)
               | ((${CAN_DBT_TSEG1} << _CFD${CAN_INSTANCE_NUM}DBTCFG_TSEG1_POSITION) & _CFD${CAN_INSTANCE_NUM}DBTCFG_TSEG1_MASK)
               | ((${CAN_DBT_TSEG2} << _CFD${CAN_INSTANCE_NUM}DBTCFG_TSEG2_POSITION) & _CFD${CAN_INSTANCE_NUM}DBTCFG_TSEG2_MASK)
               | ((${CAN_DBT_SJW} << _CFD${CAN_INSTANCE_NUM}DBTCFG_SJW_POSITION) & _CFD${CAN_INSTANCE_NUM}DBTCFG_SJW_MASK);

</#if>
    /* Set the Nominal bitrate to ${NOMINAL_BITRATE} Kbps */
    CFD${CAN_INSTANCE_NUM}NBTCFG = ((${NBT_BRP} << _CFD${CAN_INSTANCE_NUM}NBTCFG_BRP_POSITION) & _CFD${CAN_INSTANCE_NUM}NBTCFG_BRP_MASK)
               | ((${CAN_NBT_TSEG1} << _CFD${CAN_INSTANCE_NUM}NBTCFG_TSEG1_POSITION) & _CFD${CAN_INSTANCE_NUM}NBTCFG_TSEG1_MASK)
               | ((${CAN_NBT_TSEG2} << _CFD${CAN_INSTANCE_NUM}NBTCFG_TSEG2_POSITION) & _CFD${CAN_INSTANCE_NUM}NBTCFG_TSEG2_MASK)
               | ((${CAN_NBT_SJW} << _CFD${CAN_INSTANCE_NUM}NBTCFG_SJW_POSITION) & _CFD${CAN_INSTANCE_NUM}NBTCFG_SJW_MASK);

    /* Set Message memory base address for all FIFOs/Queue */
    CFD${CAN_INSTANCE_NUM}FIFOBA = (uint32_t)KVA_TO_PA(can_message_buffer);

<#if TX_EVENT_FIFO_USE == true>
    /* Tx Event FIFO Configuration */
    CFD${CAN_INSTANCE_NUM}TEFCON = (((${TX_EVENT_FIFO_MESSAGE_BUFFER} - 1) << _CFD${CAN_INSTANCE_NUM}TEFCON_FSIZE_POSITION) & _CFD${CAN_INSTANCE_NUM}TEFCON_FSIZE_MASK)<#if CAN_TIMESTAMP_ENABLE == true> | _CFD${CAN_INSTANCE_NUM}TEFCON_TEFTSEN_MASK</#if>;
    CFD${CAN_INSTANCE_NUM}CON |= _CFD${CAN_INSTANCE_NUM}CON_STEF_MASK;

<#else>
    CFD${CAN_INSTANCE_NUM}CON &= ~_CFD${CAN_INSTANCE_NUM}CON_STEF_MASK;

</#if>
<#if TX_QUEUE_USE == true>
    /* Tx Queue Configuration */
    CFD${CAN_INSTANCE_NUM}TXQCON = (((${TX_QUEUE_MESSAGE_BUFFER} - 1) << _CFD${CAN_INSTANCE_NUM}TXQCON_FSIZE_POSITION) & _CFD${CAN_INSTANCE_NUM}TXQCON_FSIZE_MASK)
               | ((${TX_QUEUE_PAYLOAD_SIZE} << _CFD${CAN_INSTANCE_NUM}TXQCON_PLSIZE_POSITION) & _CFD${CAN_INSTANCE_NUM}TXQCON_PLSIZE_MASK)
               | ((${TX_QUEUE_MESSAGE_PRIORITY} << _CFD${CAN_INSTANCE_NUM}TXQCON_TXPRI_POSITION) & _CFD${CAN_INSTANCE_NUM}TXQCON_TXPRI_MASK);
    CFD${CAN_INSTANCE_NUM}CON |= _CFD${CAN_INSTANCE_NUM}CON_TXQEN_MASK;

<#else>
    CFD${CAN_INSTANCE_NUM}CON &= ~_CFD${CAN_INSTANCE_NUM}CON_TXQEN_MASK;

</#if>

    /* Configure CAN FIFOs */
    <#list 1..NUMBER_OF_FIFO as fifo>
    <#assign FIFO_SIZE = CAN_INSTANCE_NAME + "_FIFO" + fifo + "_SIZE">
    <#assign TX_FIFO_ENABLE = CAN_INSTANCE_NAME + "_FIFO" + fifo + "_TXEN" >
    <#assign FIFO_PAYLOAD_SIZE = CAN_INSTANCE_NAME + "_FIFO" + fifo + "_PAYLOAD_SIZE" >
    <#assign TX_FIFO_PRIORITY = CAN_INSTANCE_NAME + "_FIFO" + fifo + "_MESSAGE_PRIORITY">
    <#assign TX_FIFO_RTREN = CAN_INSTANCE_NAME + "_FIFO" + fifo + "_RTREN">
    CFD${CAN_INSTANCE_NUM}FIFOCON${fifo} = (((${.vars[FIFO_SIZE]} - 1) << _CFD${CAN_INSTANCE_NUM}FIFOCON${fifo}_FSIZE_POSITION) & _CFD${CAN_INSTANCE_NUM}FIFOCON${fifo}_FSIZE_MASK)<#rt>
                 <#lt><#if .vars[TX_FIFO_ENABLE] == "0x1"> | _CFD${CAN_INSTANCE_NUM}FIFOCON${fifo}_TXEN_MASK | ((${.vars[TX_FIFO_PRIORITY]} << _CFD${CAN_INSTANCE_NUM}FIFOCON${fifo}_TXPRI_POSITION) & _CFD${CAN_INSTANCE_NUM}FIFOCON${fifo}_TXPRI_MASK) | ((${.vars[TX_FIFO_RTREN]} << _CFD${CAN_INSTANCE_NUM}FIFOCON${fifo}_RTREN_POSITION) & _CFD${CAN_INSTANCE_NUM}FIFOCON${fifo}_RTREN_MASK)</#if><#rt>
                 <#lt><#if .vars[TX_FIFO_ENABLE] == "0x0" && CAN_TIMESTAMP_ENABLE == true> | _CFD${CAN_INSTANCE_NUM}FIFOCON${fifo}_RXTSEN_MASK </#if><#rt>
                 <#lt> | ((${.vars[FIFO_PAYLOAD_SIZE]} << _CFD${CAN_INSTANCE_NUM}FIFOCON${fifo}_PLSIZE_POSITION) & _CFD${CAN_INSTANCE_NUM}FIFOCON${fifo}_PLSIZE_MASK);
    </#list>

    /* Configure CAN Filters */
    <#list 0..(NUMBER_OF_FILTER-1) as filter>
    <#assign FILTER_REG_INDEX = filter/4>
    <#assign FILTER_ID = CAN_INSTANCE_NAME + "_FILTER" + filter + "_ID_DECIMAL">
    <#assign FILTER_MASK_ID = CAN_INSTANCE_NAME + "_FILTER" + filter + "_MASK_ID_DECIMAL">
    <#assign FILTER_FIFO_SELECT = CAN_INSTANCE_NAME + "_FILTER" + filter + "_FIFO_SELECT">
    <#assign FILTER_ENABLE = CAN_INSTANCE_NAME + "_FILTER" + filter + "_ENABLE">
    /* Filter ${filter} configuration */
    CFD${CAN_INSTANCE_NUM}FLTOBJ${filter} = ${(.vars[FILTER_ID]?number > 2047)?then('((((${.vars[FILTER_ID]} & CANFD_MSG_FLT_EXT_SID_MASK) >> 18) | ((${.vars[FILTER_ID]} & CANFD_MSG_FLT_EXT_EID_MASK) << 11)) & CANFD_MSG_EID_MASK) | _CFD${CAN_INSTANCE_NUM}FLTOBJ${filter}_EXIDE_MASK','(${.vars[FILTER_ID]} & CANFD_MSG_SID_MASK)')};
    CFD${CAN_INSTANCE_NUM}MASK${filter} = ${(.vars[FILTER_MASK_ID]?number > 2047)?then('((((${.vars[FILTER_MASK_ID]} & CANFD_MSG_FLT_EXT_SID_MASK) >> 18) | ((${.vars[FILTER_MASK_ID]} & CANFD_MSG_FLT_EXT_EID_MASK) << 11)) & CANFD_MSG_EID_MASK) | _CFD${CAN_INSTANCE_NUM}MASK${filter}_MIDE_MASK','(${.vars[FILTER_MASK_ID]} & CANFD_MSG_SID_MASK)')};
    CFD${CAN_INSTANCE_NUM}FLTCON${FILTER_REG_INDEX?int} |= (((${.vars[FILTER_FIFO_SELECT]} << _CFD${CAN_INSTANCE_NUM}FLTCON${FILTER_REG_INDEX?int}_F${filter}BP_POSITION) & _CFD${CAN_INSTANCE_NUM}FLTCON${FILTER_REG_INDEX?int}_F${filter}BP_MASK)<#if .vars[FILTER_ENABLE] == true>| _CFD${CAN_INSTANCE_NUM}FLTCON${FILTER_REG_INDEX?int}_FLTEN${filter}_MASK</#if>);
    </#list>

<#if CAN_TIMESTAMP_ENABLE == true>
    /* Enable Timestamp */
    CFD${CAN_INSTANCE_NUM}TSCON = (${CAN_TIMESTAMP_PRESCALER} & _CFD${CAN_INSTANCE_NUM}TSCON_TBCPRE_MASK)
                                | ((${CAN_TIMESTAMP_EOF} << _CFD${CAN_INSTANCE_NUM}TSCON_TSEOF_POSITION) & _CFD${CAN_INSTANCE_NUM}TSCON_TSEOF_MASK)
                                <#if CAN_OPMODE != "0x6" && CAN_TIMESTAMP_EOF == "0x0">| ((${CAN_TIMESTAMP_TSRES} << _CFD${CAN_INSTANCE_NUM}TSCON_TSRES_POSITION) & _CFD${CAN_INSTANCE_NUM}TSCON_TSRES_MASK)</#if><#lt>
                                | _CFD${CAN_INSTANCE_NUM}TSCON_TBCEN_MASK;

</#if>
<#if CAN_INTERRUPT_MODE == true>
    /* Set Interrupts */
    ${CAN_IEC_REG}SET = _${CAN_IEC_REG}_CAN${CAN_INSTANCE_NUM}IE_MASK<#if CAN_MULTI_VECTOR_INTERRUPT == true> | _${CAN_IEC_REG}_CAN${CAN_INSTANCE_NUM}RXIE_MASK | _${CAN_IEC_REG}_CAN${CAN_INSTANCE_NUM}TXIE_MASK</#if>;
    CFD${CAN_INSTANCE_NUM}INT |= _CFD${CAN_INSTANCE_NUM}INT_SERRIE_MASK | _CFD${CAN_INSTANCE_NUM}INT_CERRIE_MASK | _CFD${CAN_INSTANCE_NUM}INT_IVMIE_MASK;

    /* Initialize the CAN PLib Object */
    memset((void *)${CAN_INSTANCE_NAME?lower_case}RxMsg, 0x00, sizeof(${CAN_INSTANCE_NAME?lower_case}RxMsg));

</#if>
    /* Switch the CAN module to CANFD_OPERATION_MODE. Wait until the switch is complete */
    <#if CAN_OPMODE == "0x1">
    CFD${CAN_INSTANCE_NUM}CON = (CFD${CAN_INSTANCE_NUM}CON & ~_CFD${CAN_INSTANCE_NUM}CON_REQOP_MASK) | ((0 << _CFD${CAN_INSTANCE_NUM}CON_REQOP_POSITION) & _CFD${CAN_INSTANCE_NUM}CON_REQOP_MASK);
    while(((CFD${CAN_INSTANCE_NUM}CON & _CFD${CAN_INSTANCE_NUM}CON_OPMOD_MASK) >> _CFD${CAN_INSTANCE_NUM}CON_OPMOD_POSITION) != 0);
    </#if>
    CFD${CAN_INSTANCE_NUM}CON = (CFD${CAN_INSTANCE_NUM}CON & ~_CFD${CAN_INSTANCE_NUM}CON_REQOP_MASK) | ((CANFD_OPERATION_MODE << _CFD${CAN_INSTANCE_NUM}CON_REQOP_POSITION) & _CFD${CAN_INSTANCE_NUM}CON_REQOP_MASK);
    while(((CFD${CAN_INSTANCE_NUM}CON & _CFD${CAN_INSTANCE_NUM}CON_OPMOD_MASK) >> _CFD${CAN_INSTANCE_NUM}CON_OPMOD_POSITION) != CANFD_OPERATION_MODE);
}

// *****************************************************************************
/* Function:
    bool ${CAN_INSTANCE_NAME}_MessageTransmit(uint32_t id, uint8_t length, uint8_t* data, uint8_t fifoQueueNum, CANFD_MODE mode, CANFD_MSG_TX_ATTRIBUTE msgAttr)

   Summary:
    Transmits a message into CAN bus.

   Precondition:
    ${CAN_INSTANCE_NAME}_Initialize must have been called for the associated CAN instance.

   Parameters:
    id           - 11-bit / 29-bit identifier (ID).
    length       - Length of data buffer in number of bytes.
    data         - Pointer to source data buffer
    fifoQueueNum - If fifoQueueNum is 0 then Transmit Queue otherwise FIFO
    mode         - CAN mode Classic CAN or CAN FD without BRS or CAN FD with BRS
    msgAttr      - Data frame or Remote frame to be transmitted

   Returns:
    Request status.
    true  - Request was successful.
    false - Request has failed.
*/
bool ${CAN_INSTANCE_NAME}_MessageTransmit(uint32_t id, uint8_t length, uint8_t* data, uint8_t fifoQueueNum, CANFD_MODE mode, CANFD_MSG_TX_ATTRIBUTE msgAttr)
{
    CANFD_TX_MSG_OBJECT *txMessage = NULL;
<#if TX_EVENT_FIFO_USE == true>
    static uint32_t sequence = 0;
</#if>
    uint8_t count = 0;
<#if CAN_OPMODE != "0x6">
    uint8_t dlc = 0;
</#if>
    bool status = false;

    if (fifoQueueNum == 0)
    {
<#if TX_QUEUE_USE == true>
        if ((CFD${CAN_INSTANCE_NUM}TXQSTA & _CFD${CAN_INSTANCE_NUM}TXQSTA_TXQNIF_MASK) == _CFD${CAN_INSTANCE_NUM}TXQSTA_TXQNIF_MASK)
        {
            txMessage = (CANFD_TX_MSG_OBJECT *)PA_TO_KVA1(CFD${CAN_INSTANCE_NUM}TXQUA);
            status = true;
        }
</#if>
    }
    else if (fifoQueueNum <= CANFD_NUM_OF_FIFO)
    {
        if ((*(volatile uint32_t *)(&CFD${CAN_INSTANCE_NUM}FIFOSTA1 + ((fifoQueueNum - 1) * CANFD_FIFO_OFFSET)) & _CFD${CAN_INSTANCE_NUM}FIFOSTA1_TFNRFNIF_MASK) == _CFD${CAN_INSTANCE_NUM}FIFOSTA1_TFNRFNIF_MASK)
        {
            txMessage = (CANFD_TX_MSG_OBJECT *)PA_TO_KVA1(*(volatile uint32_t *)(&CFD${CAN_INSTANCE_NUM}FIFOUA1 + ((fifoQueueNum - 1) * CANFD_FIFO_OFFSET)));
            status = true;
        }
    }

    if (status)
    {
        /* Check the id whether it falls under SID or EID,
         * SID max limit is 0x7FF, so anything beyond that is EID */
        if (id > CANFD_MSG_SID_MASK)
        {
            txMessage->t0 = (((id & CANFD_MSG_TX_EXT_SID_MASK) >> 18) | ((id & CANFD_MSG_TX_EXT_EID_MASK) << 11)) & CANFD_MSG_EID_MASK;
            txMessage->t1 = CANFD_MSG_IDE_MASK;
        }
        else
        {
            txMessage->t0 = id;
            txMessage->t1 = 0;
        }
<#if CAN_OPMODE != "0x6">
        if (length > 64)
            length = 64;

        CANLengthToDlcGet(length, &dlc);

        txMessage->t1 |= (dlc & CANFD_MSG_DLC_MASK);

        if(mode == CANFD_MODE_FD_WITH_BRS)
        {
            txMessage->t1 |= CANFD_MSG_FDF_MASK | CANFD_MSG_BRS_MASK;
        }
        else if (mode == CANFD_MODE_FD_WITHOUT_BRS)
        {
            txMessage->t1 |= CANFD_MSG_FDF_MASK;
        }
<#else>
        /* Limit length */
        if (length > 8)
            length = 8;
        txMessage->t1 |= length;
</#if>
        if (msgAttr == CANFD_MSG_TX_REMOTE_FRAME)
        {
            txMessage->t1 |= CANFD_MSG_RTR_MASK;
        }
        else
        {
            while(count < length)
            {
                txMessage->data[count++] = *data++;
            }
        }

<#if TX_EVENT_FIFO_USE == true>
        txMessage->t1 |= ((++sequence << 9) & CANFD_MSG_SEQ_MASK);

</#if>
        if (fifoQueueNum == 0)
        {
<#if TX_QUEUE_USE == true>
<#if CAN_INTERRUPT_MODE == true>
            CFD${CAN_INSTANCE_NUM}TXQCON |= _CFD${CAN_INSTANCE_NUM}TXQCON_TXQEIE_MASK;

</#if>
            /* Request the transmit */
            CFD${CAN_INSTANCE_NUM}TXQCON |= _CFD${CAN_INSTANCE_NUM}TXQCON_UINC_MASK;
            CFD${CAN_INSTANCE_NUM}TXQCON |= _CFD${CAN_INSTANCE_NUM}TXQCON_TXREQ_MASK;
</#if>
        }
        else
        {
<#if CAN_INTERRUPT_MODE == true>
            *(volatile uint32_t *)(&CFD${CAN_INSTANCE_NUM}FIFOCON1 + ((fifoQueueNum - 1) * CANFD_FIFO_OFFSET)) |= _CFD${CAN_INSTANCE_NUM}FIFOCON1_TFERFFIE_MASK;

</#if>
            /* Request the transmit */
            *(volatile uint32_t *)(&CFD${CAN_INSTANCE_NUM}FIFOCON1 + ((fifoQueueNum - 1) * CANFD_FIFO_OFFSET)) |= _CFD${CAN_INSTANCE_NUM}FIFOCON1_UINC_MASK;
            *(volatile uint32_t *)(&CFD${CAN_INSTANCE_NUM}FIFOCON1 + ((fifoQueueNum - 1) * CANFD_FIFO_OFFSET)) |= _CFD${CAN_INSTANCE_NUM}FIFOCON1_TXREQ_MASK;
        }
<#if CAN_INTERRUPT_MODE == true>
        CFD${CAN_INSTANCE_NUM}INT |= _CFD${CAN_INSTANCE_NUM}INT_TXIE_MASK;
</#if>
    }
    return status;
}

// *****************************************************************************
/* Function:
    bool ${CAN_INSTANCE_NAME}_MessageReceive(uint32_t *id, uint8_t *length, uint8_t *data, uint32_t *timestamp, uint8_t fifoNum, CANFD_MSG_RX_ATTRIBUTE *msgAttr)

   Summary:
    Receives a message from CAN bus.

   Precondition:
    ${CAN_INSTANCE_NAME}_Initialize must have been called for the associated CAN instance.

   Parameters:
    id          - Pointer to 11-bit / 29-bit identifier (ID) to be received.
    length      - Pointer to data length in number of bytes to be received.
    data        - Pointer to destination data buffer
    timestamp   - Pointer to Rx message timestamp, timestamp value is 0 if Timestamp is disabled in CFD${CAN_INSTANCE_NUM}TSCON
    fifoNum     - FIFO number
    msgAttr     - Data frame or Remote frame to be received

   Returns:
    Request status.
    true  - Request was successful.
    false - Request has failed.
*/
bool ${CAN_INSTANCE_NAME}_MessageReceive(uint32_t *id, uint8_t *length, uint8_t *data, uint32_t *timestamp, uint8_t fifoNum, CANFD_MSG_RX_ATTRIBUTE *msgAttr)
{
<#if CAN_INTERRUPT_MODE == false>
    CANFD_RX_MSG_OBJECT *rxMessage = NULL;
    uint8_t count = 0;
<#if CAN_TIMESTAMP_ENABLE == true>
    uint8_t dataIndex = 4;
</#if>
</#if>
    bool status = false;
<#if CAN_INTERRUPT_MODE == true>
    uint8_t msgIndex = 0;
    uint8_t fifoSize = 0;
</#if>

    if ((fifoNum > CANFD_NUM_OF_FIFO) || (id == NULL))
    {
        return status;
    }

<#if CAN_INTERRUPT_MODE == false>
    /* Check if there is a message available in FIFO */
    if ((*(volatile uint32_t *)(&CFD${CAN_INSTANCE_NUM}FIFOSTA1 + ((fifoNum - 1) * CANFD_FIFO_OFFSET)) & _CFD${CAN_INSTANCE_NUM}FIFOSTA1_TFNRFNIF_MASK) == _CFD${CAN_INSTANCE_NUM}FIFOSTA1_TFNRFNIF_MASK)
    {
        /* Get a pointer to RX message buffer */
        rxMessage = (CANFD_RX_MSG_OBJECT *)PA_TO_KVA1(*(volatile uint32_t *)(&CFD${CAN_INSTANCE_NUM}FIFOUA1 + ((fifoNum - 1) * CANFD_FIFO_OFFSET)));

        /* Check if it's a extended message type */
        if (rxMessage->r1 & CANFD_MSG_IDE_MASK)
        {
            *id = (((rxMessage->r0 & CANFD_MSG_RX_EXT_SID_MASK) << 18) | ((rxMessage->r0 & CANFD_MSG_RX_EXT_EID_MASK) >> 11)) & CANFD_MSG_EID_MASK;
        }
        else
        {
            *id = rxMessage->r0 & CANFD_MSG_SID_MASK;
        }

        if ((rxMessage->r1 & CANFD_MSG_RTR_MASK) && ((rxMessage->r1 & CANFD_MSG_FDF_MASK) == 0))
        {
            *msgAttr = CANFD_MSG_RX_REMOTE_FRAME;
        }
        else
        {
            *msgAttr = CANFD_MSG_RX_DATA_FRAME;
        }

        *length = dlcToLength[(rxMessage->r1 & CANFD_MSG_DLC_MASK)];

        if (timestamp != NULL)
        {
<#if CAN_TIMESTAMP_ENABLE == true>
            *timestamp =  (rxMessage->data[3] << 24) | (rxMessage->data[2] << 16) | (rxMessage->data[1] << 8) | rxMessage->data[0];
</#if>
        }

        /* Copy the data into the payload */
        while (count < *length)
        {
<#if CAN_TIMESTAMP_ENABLE == true>
            *data++ = rxMessage->data[dataIndex + count++];
<#else>
            *data++ = rxMessage->data[count++];
</#if>
        }

        /* Message processing is done, update the message buffer pointer. */
        *(volatile uint32_t *)(&CFD${CAN_INSTANCE_NUM}FIFOCON1 + ((fifoNum - 1) * CANFD_FIFO_OFFSET)) |= _CFD${CAN_INSTANCE_NUM}FIFOCON1_UINC_MASK;

        /* Message is processed successfully, so return true */
        status = true;
    }
</#if>
<#if CAN_INTERRUPT_MODE == true>
    fifoSize = (*(volatile uint32_t *)(&CFD${CAN_INSTANCE_NUM}FIFOCON1 + ((fifoNum - 1) * CANFD_FIFO_OFFSET)) & _CFD${CAN_INSTANCE_NUM}FIFOCON1_FSIZE_MASK) >> _CFD${CAN_INSTANCE_NUM}FIFOCON1_FSIZE_POSITION;
    for (msgIndex = 0; msgIndex <= fifoSize; msgIndex++)
    {
        if ((${CAN_INSTANCE_NAME?lower_case}MsgIndex[fifoNum-1] & (1UL << (msgIndex & 0x1F))) == 0)
        {
            ${CAN_INSTANCE_NAME?lower_case}MsgIndex[fifoNum-1] |= (1UL << (msgIndex & 0x1F));
            break;
        }
    }
    if(msgIndex > fifoSize)
    {
        /* FIFO is full */
        return false;
    }
    ${CAN_INSTANCE_NAME?lower_case}RxMsg[fifoNum-1][msgIndex].id = id;
    ${CAN_INSTANCE_NAME?lower_case}RxMsg[fifoNum-1][msgIndex].buffer = data;
    ${CAN_INSTANCE_NAME?lower_case}RxMsg[fifoNum-1][msgIndex].size = length;
    ${CAN_INSTANCE_NAME?lower_case}RxMsg[fifoNum-1][msgIndex].timestamp = timestamp;
    ${CAN_INSTANCE_NAME?lower_case}RxMsg[fifoNum-1][msgIndex].msgAttr = msgAttr;
    *(volatile uint32_t *)(&CFD${CAN_INSTANCE_NUM}FIFOCON1 + ((fifoNum - 1) * CANFD_FIFO_OFFSET)) |= _CFD${CAN_INSTANCE_NUM}FIFOCON1_TFNRFNIE_MASK;
    CFD${CAN_INSTANCE_NUM}INT |= _CFD${CAN_INSTANCE_NUM}INT_RXIE_MASK;
    status = true;
</#if>

    return status;
}

// *****************************************************************************
/* Function:
    void ${CAN_INSTANCE_NAME}_MessageAbort(uint8_t fifoQueueNum)

   Summary:
    Abort request for a Queue/FIFO.

   Precondition:
    ${CAN_INSTANCE_NAME}_Initialize must have been called for the associated CAN instance.

   Parameters:
    fifoQueueNum - If fifoQueueNum is 0 then Transmit Queue otherwise FIFO

   Returns:
    None.
*/
void ${CAN_INSTANCE_NAME}_MessageAbort(uint8_t fifoQueueNum)
{
    if (fifoQueueNum == 0)
    {
<#if TX_QUEUE_USE == true>
        CFD${CAN_INSTANCE_NUM}TXQCON &= ~_CFD${CAN_INSTANCE_NUM}TXQCON_TXREQ_MASK;
</#if>
    }
    else if (fifoQueueNum <= CANFD_NUM_OF_FIFO)
    {
        *(volatile uint32_t *)(&CFD${CAN_INSTANCE_NUM}FIFOCON1 + ((fifoQueueNum - 1) * CANFD_FIFO_OFFSET)) &= ~_CFD${CAN_INSTANCE_NUM}FIFOCON1_TXREQ_MASK;
    }
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

    if (filterNum < CANFD_NUM_OF_FILTER)
    {
        filterRegIndex = filterNum >> 2;
        filterEnableBit = (filterNum % 4 == 0)? _CFD${CAN_INSTANCE_NUM}FLTCON0_FLTEN0_MASK : 1 << ((((filterNum % 4) + 1) * 8) - 1);

        *(volatile uint32_t *)(&CFD${CAN_INSTANCE_NUM}FLTCON0 + (filterRegIndex * CANFD_FILTER_OFFSET)) &= ~filterEnableBit;

        if (id > CANFD_MSG_SID_MASK)
        {
            *(volatile uint32_t *)(&CFD${CAN_INSTANCE_NUM}FLTOBJ0 + (filterNum * CANFD_FILTER_OBJ_OFFSET)) = ((((id & CANFD_MSG_FLT_EXT_SID_MASK) >> 18) | ((id & CANFD_MSG_FLT_EXT_EID_MASK) << 11)) & CANFD_MSG_EID_MASK) | _CFD${CAN_INSTANCE_NUM}FLTOBJ0_EXIDE_MASK;
        }
        else
        {
            *(volatile uint32_t *)(&CFD${CAN_INSTANCE_NUM}FLTOBJ0 + (filterNum * CANFD_FILTER_OBJ_OFFSET)) = id & CANFD_MSG_SID_MASK;
        }
        *(volatile uint32_t *)(&CFD${CAN_INSTANCE_NUM}FLTCON0 + (filterRegIndex * CANFD_FILTER_OFFSET)) |= filterEnableBit;
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

    if (filterNum < CANFD_NUM_OF_FILTER)
    {
        if (*(volatile uint32_t *)(&CFD${CAN_INSTANCE_NUM}FLTOBJ0 + (filterNum * CANFD_FILTER_OBJ_OFFSET)) & _CFD${CAN_INSTANCE_NUM}FLTOBJ0_EXIDE_MASK)
        {
            id = (((*(volatile uint32_t *)(&CFD${CAN_INSTANCE_NUM}FLTOBJ0 + (filterNum * CANFD_FILTER_OBJ_OFFSET)) & CANFD_MSG_RX_EXT_SID_MASK) << 18)
               | ((*(volatile uint32_t *)(&CFD${CAN_INSTANCE_NUM}FLTOBJ0 + (filterNum * CANFD_FILTER_OBJ_OFFSET)) & CANFD_MSG_RX_EXT_EID_MASK) >> 11))
               & CANFD_MSG_EID_MASK;
        }
        else
        {
            id = (*(volatile uint32_t *)(&CFD${CAN_INSTANCE_NUM}FLTOBJ0 + (filterNum * CANFD_FILTER_OBJ_OFFSET)) & CANFD_MSG_SID_MASK);
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
    acceptanceFilterMaskNum - Acceptance Filter Mask number
    id                      - 11-bit or 29-bit identifier

   Returns:
    None.
*/
void ${CAN_INSTANCE_NAME}_MessageAcceptanceFilterMaskSet(uint8_t acceptanceFilterMaskNum, uint32_t id)
{
    /* Switch the CAN module to Configuration mode. Wait until the switch is complete */
    CFD${CAN_INSTANCE_NUM}CON = (CFD${CAN_INSTANCE_NUM}CON & ~_CFD${CAN_INSTANCE_NUM}CON_REQOP_MASK) | ((CANFD_CONFIGURATION_MODE << _CFD${CAN_INSTANCE_NUM}CON_REQOP_POSITION) & _CFD${CAN_INSTANCE_NUM}CON_REQOP_MASK);
    while(((CFD${CAN_INSTANCE_NUM}CON & _CFD${CAN_INSTANCE_NUM}CON_OPMOD_MASK) >> _CFD${CAN_INSTANCE_NUM}CON_OPMOD_POSITION) != CANFD_CONFIGURATION_MODE);

    if (id > CANFD_MSG_SID_MASK)
    {
        *(volatile uint32_t *)(&CFD${CAN_INSTANCE_NUM}MASK0 + (acceptanceFilterMaskNum * CANFD_ACCEPTANCE_MASK_OFFSET)) = ((((id & CANFD_MSG_FLT_EXT_SID_MASK) >> 18) | ((id & CANFD_MSG_FLT_EXT_EID_MASK) << 11)) & CANFD_MSG_EID_MASK) | _CFD${CAN_INSTANCE_NUM}MASK0_MIDE_MASK;
    }
    else
    {
        *(volatile uint32_t *)(&CFD${CAN_INSTANCE_NUM}MASK0 + (acceptanceFilterMaskNum * CANFD_ACCEPTANCE_MASK_OFFSET)) = id & CANFD_MSG_SID_MASK;
    }

    /* Switch the CAN module to CANFD_OPERATION_MODE. Wait until the switch is complete */
    CFD${CAN_INSTANCE_NUM}CON = (CFD${CAN_INSTANCE_NUM}CON & ~_CFD${CAN_INSTANCE_NUM}CON_REQOP_MASK) | ((CANFD_OPERATION_MODE << _CFD${CAN_INSTANCE_NUM}CON_REQOP_POSITION) & _CFD${CAN_INSTANCE_NUM}CON_REQOP_MASK);
    while(((CFD${CAN_INSTANCE_NUM}CON & _CFD${CAN_INSTANCE_NUM}CON_OPMOD_MASK) >> _CFD${CAN_INSTANCE_NUM}CON_OPMOD_POSITION) != CANFD_OPERATION_MODE);
}

// *****************************************************************************
/* Function:
    uint32_t ${CAN_INSTANCE_NAME}_MessageAcceptanceFilterMaskGet(uint8_t acceptanceFilterMaskNum)

   Summary:
    Get Message acceptance filter mask configuration.

   Precondition:
    ${CAN_INSTANCE_NAME}_Initialize must have been called for the associated CAN instance.

   Parameters:
    acceptanceFilterMaskNum - Acceptance Filter Mask number

   Returns:
    Returns Message acceptance filter mask.
*/
uint32_t ${CAN_INSTANCE_NAME}_MessageAcceptanceFilterMaskGet(uint8_t acceptanceFilterMaskNum)
{
    uint32_t id = 0;

    if (*(volatile uint32_t *)(&CFD${CAN_INSTANCE_NUM}MASK0 + (acceptanceFilterMaskNum * CANFD_ACCEPTANCE_MASK_OFFSET)) & _CFD${CAN_INSTANCE_NUM}MASK0_MIDE_MASK)
    {
        id = (((*(volatile uint32_t *)(&CFD${CAN_INSTANCE_NUM}MASK0 + (acceptanceFilterMaskNum * CANFD_ACCEPTANCE_MASK_OFFSET)) & CANFD_MSG_RX_EXT_SID_MASK) << 18)
           | ((*(volatile uint32_t *)(&CFD${CAN_INSTANCE_NUM}MASK0 + (acceptanceFilterMaskNum * CANFD_ACCEPTANCE_MASK_OFFSET)) & CANFD_MSG_RX_EXT_EID_MASK) >> 11))
           & CANFD_MSG_EID_MASK;
    }
    else
    {
        id = (*(volatile uint32_t *)(&CFD${CAN_INSTANCE_NUM}MASK0 + (acceptanceFilterMaskNum * CANFD_ACCEPTANCE_MASK_OFFSET)) & CANFD_MSG_SID_MASK);
    }
    return id;
}

<#if TX_EVENT_FIFO_USE == true>
// *****************************************************************************
/* Function:
    bool ${CAN_INSTANCE_NAME}_TransmitEventFIFOElementGet(uint32_t *id, uint32_t *sequence, uint32_t *timestamp)

   Summary:
    Get the Transmit Event FIFO Element for the transmitted message.

   Precondition:
    ${CAN_INSTANCE_NAME}_Initialize must have been called for the associated CAN instance.

   Parameters:
    id          - Pointer to 11-bit / 29-bit identifier (ID) to be received.
    sequence    - Pointer to Tx message sequence number to be received
    timestamp   - Pointer to Tx message timestamp to be received, timestamp value is 0 if Timestamp is disabled in CFD${CAN_INSTANCE_NUM}TSCON

   Returns:
    Request status.
    true  - Request was successful.
    false - Request has failed.
*/
bool ${CAN_INSTANCE_NAME}_TransmitEventFIFOElementGet(uint32_t *id, uint32_t *sequence, uint32_t *timestamp)
{
    CANFD_TX_EVENT_FIFO_ELEMENT *txEventFIFOElement = NULL;
    bool status = false;

    /* Check if there is a message available in Tx Event FIFO */
    if ((CFD${CAN_INSTANCE_NUM}TEFSTA & _CFD${CAN_INSTANCE_NUM}TEFSTA_TEFNEIF_MASK) == _CFD${CAN_INSTANCE_NUM}TEFSTA_TEFNEIF_MASK)
    {
        /* Get a pointer to Tx Event FIFO Element */
        txEventFIFOElement = (CANFD_TX_EVENT_FIFO_ELEMENT *)PA_TO_KVA1(CFD${CAN_INSTANCE_NUM}TEFUA);

        /* Check if it's a extended message type */
        if (txEventFIFOElement->te1 & CANFD_MSG_IDE_MASK)
        {
            *id = txEventFIFOElement->te0 & CANFD_MSG_EID_MASK;
        }
        else
        {
            *id = txEventFIFOElement->te0 & CANFD_MSG_SID_MASK;
        }

        *sequence = ((txEventFIFOElement->te1 & CANFD_MSG_SEQ_MASK) >> 9);

        if (timestamp != NULL)
        {
<#if CAN_TIMESTAMP_ENABLE == true>
            *timestamp =  (txEventFIFOElement->timestamp[3] << 24) | (txEventFIFOElement->timestamp[2] << 16) | (txEventFIFOElement->timestamp[1] << 8) | txEventFIFOElement->timestamp[0];
</#if>
        }

        /* Tx Event FIFO Element read done, update the Tx Event FIFO tail */
        CFD${CAN_INSTANCE_NUM}TEFCON |= _CFD${CAN_INSTANCE_NUM}TEFCON_UINC_MASK;

        /* Tx Event FIFO Element read successfully, so return true */
        status = true;
    }
    return status;
}
</#if>

// *****************************************************************************
/* Function:
    CANFD_ERROR ${CAN_INSTANCE_NAME}_ErrorGet(void)

   Summary:
    Returns the error during transfer.

   Precondition:
    ${CAN_INSTANCE_NAME}_Initialize must have been called for the associated CAN instance.

   Parameters:
    None.

   Returns:
    Error during transfer.
*/
CANFD_ERROR ${CAN_INSTANCE_NAME}_ErrorGet(void)
{
<#if CAN_INTERRUPT_MODE == false>
    CANFD_ERROR error = CANFD_ERROR_NONE;
    uint32_t errorStatus = CFD${CAN_INSTANCE_NUM}TREC;

    /* Check if error occurred */
    error = (CANFD_ERROR)((errorStatus & _CFD${CAN_INSTANCE_NUM}TREC_EWARN_MASK) |
                        (errorStatus & _CFD${CAN_INSTANCE_NUM}TREC_RXWARN_MASK) |
                        (errorStatus & _CFD${CAN_INSTANCE_NUM}TREC_TXWARN_MASK) |
                        (errorStatus & _CFD${CAN_INSTANCE_NUM}TREC_RXBP_MASK) |
                        (errorStatus & _CFD${CAN_INSTANCE_NUM}TREC_TXBP_MASK) |
                        (errorStatus & _CFD${CAN_INSTANCE_NUM}TREC_TXBO_MASK));

</#if>
<#if CAN_INTERRUPT_MODE == false>
    return error;
<#else>
    return (CANFD_ERROR)${CAN_INSTANCE_NAME?lower_case}Obj.errorStatus;
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
    *txErrorCount = (uint8_t)((CFD${CAN_INSTANCE_NUM}TREC & _CFD${CAN_INSTANCE_NUM}TREC_TERRCNT_MASK) >> _CFD${CAN_INSTANCE_NUM}TREC_TERRCNT_POSITION);
    *rxErrorCount = (uint8_t)(CFD${CAN_INSTANCE_NUM}TREC & _CFD${CAN_INSTANCE_NUM}TREC_RERRCNT_MASK);
}

// *****************************************************************************
/* Function:
    bool ${CAN_INSTANCE_NAME}_InterruptGet(uint8_t fifoQueueNum, CANFD_FIFO_INTERRUPT_FLAG_MASK fifoInterruptFlagMask)

   Summary:
    Returns the FIFO Interrupt status.

   Precondition:
    ${CAN_INSTANCE_NAME}_Initialize must have been called for the associated CAN instance.

   Parameters:
    fifoQueueNum          - FIFO number
    fifoInterruptFlagMask - FIFO interrupt flag mask

   Returns:
    true - Requested fifo interrupt is occurred.
    false - Requested fifo interrupt is not occurred.
*/
bool ${CAN_INSTANCE_NAME}_InterruptGet(uint8_t fifoQueueNum, CANFD_FIFO_INTERRUPT_FLAG_MASK fifoInterruptFlagMask)
{
    if (fifoQueueNum == 0)
    {
<#if TX_QUEUE_USE == true>
        return ((CFD${CAN_INSTANCE_NUM}TXQSTA & fifoInterruptFlagMask) != 0x0);
<#else>
        return false;
</#if>
    }
    else
    {
        return ((*(volatile uint32_t *)(&CFD${CAN_INSTANCE_NUM}FIFOSTA1 + ((fifoQueueNum - 1) * CANFD_FIFO_OFFSET)) & fifoInterruptFlagMask) != 0x0);
    }
}

// *****************************************************************************
/* Function:
    bool ${CAN_INSTANCE_NAME}_TxFIFOQueueIsFull(uint8_t fifoQueueNum)

   Summary:
    Returns true if Tx FIFO/Queue is full otherwise false.

   Precondition:
    ${CAN_INSTANCE_NAME}_Initialize must have been called for the associated CAN instance.

   Parameters:
    fifoQueueNum - FIFO/Queue number

   Returns:
    true  - Tx FIFO/Queue is full.
    false - Tx FIFO/Queue is not full.
*/
bool ${CAN_INSTANCE_NAME}_TxFIFOQueueIsFull(uint8_t fifoQueueNum)
{
    if (fifoQueueNum == 0)
    {
        return ((CFD${CAN_INSTANCE_NUM}TXQSTA & _CFD${CAN_INSTANCE_NUM}TXQSTA_TXQNIF_MASK) != _CFD${CAN_INSTANCE_NUM}TXQSTA_TXQNIF_MASK);
    }
    else
    {
        return ((*(volatile uint32_t *)(&CFD${CAN_INSTANCE_NUM}FIFOSTA1 + ((fifoQueueNum - 1) * CANFD_FIFO_OFFSET)) & _CFD${CAN_INSTANCE_NUM}FIFOSTA1_TFNRFNIF_MASK) != _CFD${CAN_INSTANCE_NUM}FIFOSTA1_TFNRFNIF_MASK);
    }
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
    id           - 11-bit / 29-bit identifier (ID).
    length       - Length of data buffer in number of bytes.
    data         - Pointer to source data buffer
    fifoNum      - FIFO Number

   Returns:
    Request status.
    true  - Request was successful.
    false - Request has failed.
*/
bool ${CAN_INSTANCE_NAME}_AutoRTRResponseSet(uint32_t id, uint8_t length, uint8_t* data, uint8_t fifoNum)
{
    CANFD_TX_MSG_OBJECT *txMessage = NULL;
    uint8_t count = 0;
    bool status = false;

    if (fifoNum <= CANFD_NUM_OF_FIFO)
    {
        if ((*(volatile uint32_t *)(&CFD${CAN_INSTANCE_NUM}FIFOSTA1 + ((fifoNum - 1) * CANFD_FIFO_OFFSET)) & _CFD${CAN_INSTANCE_NUM}FIFOSTA1_TFNRFNIF_MASK) == _CFD${CAN_INSTANCE_NUM}FIFOSTA1_TFNRFNIF_MASK)
        {
            txMessage = (CANFD_TX_MSG_OBJECT *)PA_TO_KVA1(*(volatile uint32_t *)(&CFD${CAN_INSTANCE_NUM}FIFOUA1 + ((fifoNum - 1) * CANFD_FIFO_OFFSET)));
            status = true;
        }
    }

    if (status)
    {
        /* Check the id whether it falls under SID or EID,
         * SID max limit is 0x7FF, so anything beyond that is EID */
        if (id > CANFD_MSG_SID_MASK)
        {
            txMessage->t0 = (((id & CANFD_MSG_TX_EXT_SID_MASK) >> 18) | ((id & CANFD_MSG_TX_EXT_EID_MASK) << 11)) & CANFD_MSG_EID_MASK;
            txMessage->t1 = CANFD_MSG_IDE_MASK;
        }
        else
        {
            txMessage->t0 = id;
            txMessage->t1 = 0;
        }

        /* Limit length */
        if (length > 8)
            length = 8;
        txMessage->t1 |= length;

        while(count < length)
        {
            txMessage->data[count++] = *data++;
        }

<#if CAN_INTERRUPT_MODE == true>
        *(volatile uint32_t *)(&CFD${CAN_INSTANCE_NUM}FIFOCON1 + ((fifoNum - 1) * CANFD_FIFO_OFFSET)) |= _CFD${CAN_INSTANCE_NUM}FIFOCON1_TFERFFIE_MASK;

</#if>
        /* Set UINC to respond to RTR */
        *(volatile uint32_t *)(&CFD${CAN_INSTANCE_NUM}FIFOCON1 + ((fifoNum - 1) * CANFD_FIFO_OFFSET)) |= _CFD${CAN_INSTANCE_NUM}FIFOCON1_UINC_MASK;
<#if CAN_INTERRUPT_MODE == true>
        CFD${CAN_INSTANCE_NUM}INT |= _CFD${CAN_INSTANCE_NUM}INT_TXIE_MASK;
</#if>
    }
    return status;
}

<#if CAN_INTERRUPT_MODE == true>
// *****************************************************************************
/* Function:
    void ${CAN_INSTANCE_NAME}_CallbackRegister(CANFD_CALLBACK callback, uintptr_t contextHandle, uint8_t fifoQueueNum)

   Summary:
    Sets the pointer to the function (and it's context) to be called when the
    given CAN's transfer events occur.

   Precondition:
    ${CAN_INSTANCE_NAME}_Initialize must have been called for the associated CAN instance.

   Parameters:
    callback - A pointer to a function with a calling signature defined
    by the CANFD_CALLBACK data type.
    fifoQueueNum - Tx Queue or Tx/Rx FIFO number

    context - A value (usually a pointer) passed (unused) into the function
    identified by the callback parameter.

   Returns:
    None.
*/
void ${CAN_INSTANCE_NAME}_CallbackRegister(CANFD_CALLBACK callback, uintptr_t contextHandle, uint8_t fifoQueueNum)
{
    if (callback == NULL)
    {
        return;
    }

    ${CAN_INSTANCE_NAME?lower_case}CallbackObj[fifoQueueNum].callback = callback;
    ${CAN_INSTANCE_NAME?lower_case}CallbackObj[fifoQueueNum].context = contextHandle;
}

// *****************************************************************************
/* Function:
    void ${CAN_INSTANCE_NAME}_ErrorCallbackRegister(CANFD_CALLBACK callback, uintptr_t contextHandle)

   Summary:
    Sets the pointer to the function (and it's context) to be called when the
    given CAN's transfer events occur.

   Precondition:
    ${CAN_INSTANCE_NAME}_Initialize must have been called for the associated CAN instance.

   Parameters:
    callback - A pointer to a function with a calling signature defined
    by the CANFD_CALLBACK data type.

    context - A value (usually a pointer) passed (unused) into the function
    identified by the callback parameter.

   Returns:
    None.
*/
void ${CAN_INSTANCE_NAME}_ErrorCallbackRegister(CANFD_CALLBACK callback, uintptr_t contextHandle)
{
    if (callback == NULL)
    {
        return;
    }

    ${CAN_INSTANCE_NAME?lower_case}ErrorCallbackObj.callback = callback;
    ${CAN_INSTANCE_NAME?lower_case}ErrorCallbackObj.context = contextHandle;
}

<#if CAN_INTERRUPT_COUNT == 1>
static void ${CAN_INSTANCE_NAME}_RX_InterruptHandler(void)
<#else>
void ${CAN_INSTANCE_NAME}_RX_InterruptHandler(void)
</#if>
{
    uint8_t  msgIndex = 0;
    uint8_t  fifoNum = 0;
    uint8_t  fifoSize = 0;
    uint8_t  count = 0;
    CANFD_RX_MSG_OBJECT *rxMessage = NULL;
<#if CAN_TIMESTAMP_ENABLE == true>
    uint8_t dataIndex = 4;
</#if>

    fifoNum = (uint8_t)CFD${CAN_INSTANCE_NUM}VEC & _CFD${CAN_INSTANCE_NUM}VEC_ICODE_MASK;
    if (fifoNum <= CANFD_NUM_OF_FIFO)
    {
        fifoSize = (*(volatile uint32_t *)(&CFD${CAN_INSTANCE_NUM}FIFOCON1 + ((fifoNum - 1) * CANFD_FIFO_OFFSET)) & _CFD${CAN_INSTANCE_NUM}FIFOCON1_FSIZE_MASK) >> _CFD${CAN_INSTANCE_NUM}FIFOCON1_FSIZE_POSITION;
        for (msgIndex = 0; msgIndex <= fifoSize; msgIndex++)
        {
            if ((${CAN_INSTANCE_NAME?lower_case}MsgIndex[fifoNum-1] & (1 << (msgIndex & 0x1F))) == (1 << (msgIndex & 0x1F)))
            {
                ${CAN_INSTANCE_NAME?lower_case}MsgIndex[fifoNum-1] &= ~(1 << (msgIndex & 0x1F));
                break;
            }
        }
        /* Get a pointer to RX message buffer */
        rxMessage = (CANFD_RX_MSG_OBJECT *)PA_TO_KVA1(*(volatile uint32_t *)(&CFD${CAN_INSTANCE_NUM}FIFOUA1 + ((fifoNum - 1) * CANFD_FIFO_OFFSET)));

        /* Check if it's a extended message type */
        if (rxMessage->r1 & CANFD_MSG_IDE_MASK)
        {
            *${CAN_INSTANCE_NAME?lower_case}RxMsg[fifoNum-1][msgIndex].id = (((rxMessage->r0 & CANFD_MSG_RX_EXT_SID_MASK) << 18) | ((rxMessage->r0 & CANFD_MSG_RX_EXT_EID_MASK) >> 11)) & CANFD_MSG_EID_MASK;
        }
        else
        {
            *${CAN_INSTANCE_NAME?lower_case}RxMsg[fifoNum-1][msgIndex].id = rxMessage->r0 & CANFD_MSG_SID_MASK;
        }

        if ((rxMessage->r1 & CANFD_MSG_RTR_MASK) && ((rxMessage->r1 & CANFD_MSG_FDF_MASK) == 0))
        {
            *${CAN_INSTANCE_NAME?lower_case}RxMsg[fifoNum-1][msgIndex].msgAttr = CANFD_MSG_RX_REMOTE_FRAME;
        }
        else
        {
            *${CAN_INSTANCE_NAME?lower_case}RxMsg[fifoNum-1][msgIndex].msgAttr = CANFD_MSG_RX_DATA_FRAME;
        }

        *${CAN_INSTANCE_NAME?lower_case}RxMsg[fifoNum-1][msgIndex].size = dlcToLength[(rxMessage->r1 & CANFD_MSG_DLC_MASK)];

        if (${CAN_INSTANCE_NAME?lower_case}RxMsg[fifoNum-1][msgIndex].timestamp != NULL)
        {
            <#if CAN_TIMESTAMP_ENABLE == true>
            *${CAN_INSTANCE_NAME?lower_case}RxMsg[fifoNum-1][msgIndex].timestamp =  (rxMessage->data[3] << 24) | (rxMessage->data[2] << 16) | (rxMessage->data[1] << 8) | rxMessage->data[0];
            </#if>
        }

        /* Copy the data into the payload */
        while (count < *${CAN_INSTANCE_NAME?lower_case}RxMsg[fifoNum-1][msgIndex].size)
        {
            <#if CAN_TIMESTAMP_ENABLE == true>
            *${CAN_INSTANCE_NAME?lower_case}RxMsg[fifoNum-1][msgIndex].buffer++ = rxMessage->data[dataIndex + count++];
            <#else>
            *${CAN_INSTANCE_NAME?lower_case}RxMsg[fifoNum-1][msgIndex].buffer++ = rxMessage->data[count++];
            </#if>
        }

        /* Message processing is done, update the message buffer pointer. */
        *(volatile uint32_t *)(&CFD${CAN_INSTANCE_NUM}FIFOCON1 + ((fifoNum - 1) * CANFD_FIFO_OFFSET)) |= _CFD${CAN_INSTANCE_NUM}FIFOCON1_UINC_MASK;

        if (((*(volatile uint32_t *)(&CFD${CAN_INSTANCE_NUM}FIFOSTA1 + ((fifoNum - 1) * CANFD_FIFO_OFFSET)) & _CFD${CAN_INSTANCE_NUM}FIFOSTA1_TFNRFNIF_MASK) != _CFD${CAN_INSTANCE_NUM}FIFOSTA1_TFNRFNIF_MASK) ||
            (${CAN_INSTANCE_NAME?lower_case}MsgIndex[fifoNum-1] == 0))
        {
            *(volatile uint32_t *)(&CFD${CAN_INSTANCE_NUM}FIFOCON1 + ((fifoNum - 1) * CANFD_FIFO_OFFSET)) &= ~_CFD${CAN_INSTANCE_NUM}FIFOCON1_TFNRFNIE_MASK;
        }
        ${CAN_INSTANCE_NAME?lower_case}Obj.errorStatus = 0;
    }
    <#if CAN_MULTI_VECTOR_INTERRUPT == true>
    ${CAN_IFS_REG}CLR = _${CAN_IFS_REG}_CAN${CAN_INSTANCE_NUM}RXIF_MASK;
    <#else>
    ${CAN_IFS_REG}CLR = _${CAN_IFS_REG}_CAN${CAN_INSTANCE_NUM}IF_MASK;
    </#if>

    if (${CAN_INSTANCE_NAME?lower_case}CallbackObj[fifoNum].callback != NULL)
    {
        ${CAN_INSTANCE_NAME?lower_case}CallbackObj[fifoNum].callback(${CAN_INSTANCE_NAME?lower_case}CallbackObj[fifoNum].context);
    }
}

<#if CAN_INTERRUPT_COUNT == 1>
static void ${CAN_INSTANCE_NAME}_TX_InterruptHandler(void)
<#else>
void ${CAN_INSTANCE_NAME}_TX_InterruptHandler(void)
</#if>
{
    uint8_t  fifoNum = 0;

    fifoNum = (uint8_t)CFD${CAN_INSTANCE_NUM}VEC & _CFD${CAN_INSTANCE_NUM}VEC_ICODE_MASK;
    if (fifoNum <= CANFD_NUM_OF_FIFO)
    {
        if (fifoNum == 0)
        {
            <#if TX_QUEUE_USE == true>
            CFD${CAN_INSTANCE_NUM}TXQCON &= ~_CFD${CAN_INSTANCE_NUM}TXQCON_TXQEIE_MASK;
            </#if>
        }
        else
        {
            *(volatile uint32_t *)(&CFD${CAN_INSTANCE_NUM}FIFOCON1 + ((fifoNum - 1) * CANFD_FIFO_OFFSET)) &= ~_CFD${CAN_INSTANCE_NUM}FIFOCON1_TFERFFIE_MASK;
        }
        ${CAN_INSTANCE_NAME?lower_case}Obj.errorStatus = 0;
    }
    <#if CAN_MULTI_VECTOR_INTERRUPT == true>
    ${CAN_IFS_REG}CLR = _${CAN_IFS_REG}_CAN${CAN_INSTANCE_NUM}TXIF_MASK;
    <#else>
    ${CAN_IFS_REG}CLR = _${CAN_IFS_REG}_CAN${CAN_INSTANCE_NUM}IF_MASK;
    </#if>

    if (${CAN_INSTANCE_NAME?lower_case}CallbackObj[fifoNum].callback != NULL)
    {
        ${CAN_INSTANCE_NAME?lower_case}CallbackObj[fifoNum].callback(${CAN_INSTANCE_NAME?lower_case}CallbackObj[fifoNum].context);
    }
}

<#if CAN_INTERRUPT_COUNT == 1>
static void ${CAN_INSTANCE_NAME}_MISC_InterruptHandler(void)
<#else>
void ${CAN_INSTANCE_NAME}_MISC_InterruptHandler(void)
</#if>
{
    uint32_t errorStatus = 0;

    CFD${CAN_INSTANCE_NUM}INT &= ~(_CFD${CAN_INSTANCE_NUM}INT_SERRIF_MASK | _CFD${CAN_INSTANCE_NUM}INT_CERRIF_MASK | _CFD${CAN_INSTANCE_NUM}INT_IVMIF_MASK);
    ${CAN_IFS_REG}CLR = _${CAN_IFS_REG}_CAN${CAN_INSTANCE_NUM}IF_MASK;
    errorStatus = CFD${CAN_INSTANCE_NUM}TREC;

    /* Check if error occurred */
    ${CAN_INSTANCE_NAME?lower_case}Obj.errorStatus = ((errorStatus & _CFD${CAN_INSTANCE_NUM}TREC_EWARN_MASK) |
                                                      (errorStatus & _CFD${CAN_INSTANCE_NUM}TREC_RXWARN_MASK) |
                                                      (errorStatus & _CFD${CAN_INSTANCE_NUM}TREC_TXWARN_MASK) |
                                                      (errorStatus & _CFD${CAN_INSTANCE_NUM}TREC_RXBP_MASK) |
                                                      (errorStatus & _CFD${CAN_INSTANCE_NUM}TREC_TXBP_MASK) |
                                                      (errorStatus & _CFD${CAN_INSTANCE_NUM}TREC_TXBO_MASK));

    /* Client must call ${CAN_INSTANCE_NAME}_ErrorGet and ${CAN_INSTANCE_NAME}_ErrorCountGet functions to get errors */
    if (${CAN_INSTANCE_NAME?lower_case}ErrorCallbackObj.callback != NULL)
    {
        ${CAN_INSTANCE_NAME?lower_case}ErrorCallbackObj.callback(${CAN_INSTANCE_NAME?lower_case}ErrorCallbackObj.context);
    }
}

<#if CAN_INTERRUPT_COUNT == 1>
// *****************************************************************************
/* Function:
    void ${CAN_INSTANCE_NAME}_InterruptHandler(void)

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
void ${CAN_INSTANCE_NAME}_InterruptHandler(void)
{
    /* Call CAN MISC interrupt handler if SERRIF/CERRIF/IVMIF interrupt flag is set */
    if (CFD${CAN_INSTANCE_NUM}INT & (_CFD${CAN_INSTANCE_NUM}INT_SERRIF_MASK | _CFD${CAN_INSTANCE_NUM}INT_CERRIF_MASK | _CFD${CAN_INSTANCE_NUM}INT_IVMIF_MASK))
    {
        ${CAN_INSTANCE_NAME}_MISC_InterruptHandler();
    }

    /* Call CAN RX interrupt handler if RXIF interrupt flag is set */
    if (CFD${CAN_INSTANCE_NUM}INT & _CFD${CAN_INSTANCE_NUM}INT_RXIF_MASK)
    {
        ${CAN_INSTANCE_NAME}_RX_InterruptHandler();
    }

    /* Call CAN TX interrupt handler if TXIF interrupt flag is set */
    if (CFD${CAN_INSTANCE_NUM}INT & _CFD${CAN_INSTANCE_NUM}INT_TXIF_MASK)
    {
        ${CAN_INSTANCE_NAME}_TX_InterruptHandler();
    }
}
</#if>
</#if>
