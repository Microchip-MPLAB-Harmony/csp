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
// *****************************************************************************
// *****************************************************************************
// Header Includes
// *****************************************************************************
// *****************************************************************************

#include "device.h"
<#if core.CoreSysIntFile == true>
#include "interrupts.h"
</#if>
#include "plib_${CAN_INSTANCE_NAME?lower_case}.h"

// *****************************************************************************
// *****************************************************************************
// Global Data
// *****************************************************************************
// *****************************************************************************
<#assign CAN_NBTP_NTSEG1  = NBTP_NTSEG1 - 1>
<#assign CAN_NBTP_NTSEG2  = NBTP_NTSEG2 - 1>
<#assign CAN_NBTP_NSJW    = NBTP_NSJW - 1>
<#assign CAN_DBTP_DTSEG1  = DBTP_DTSEG1 - 1>
<#assign CAN_DBTP_DTSEG2  = DBTP_DTSEG2 - 1>
<#assign CAN_DBTP_DSJW    = DBTP_DSJW - 1>
#define CAN_STD_ID_Msk        0x7FFU
<#if INTERRUPT_MODE == true>
#define CAN_CALLBACK_TX_INDEX 3U
<#assign NUM_OF_FIFO = 2>
<#assign NUM_OF_ELEMENTS = 1>
 <#if RXF0_USE>
  <#assign NUM_OF_ELEMENTS = RXF0_ELEMENTS>
 </#if>
 <#if RXF1_USE>
  <#if NUM_OF_ELEMENTS?number < RXF1_ELEMENTS>
   <#assign NUM_OF_ELEMENTS = RXF1_ELEMENTS>
  </#if>
 </#if>
 <#if RXBUF_USE>
 <#assign NUM_OF_FIFO = NUM_OF_FIFO + 1>
  <#if NUM_OF_ELEMENTS?number < RX_BUFFER_ELEMENTS>
   <#assign NUM_OF_ELEMENTS = RX_BUFFER_ELEMENTS>
  </#if>
 </#if>
#define NUM_RX_FIFOS ${NUM_OF_FIFO}U
#define NUM_RX_BUFFER_ELEMENTS ${NUM_OF_ELEMENTS}U
static CAN_RX_MSG ${CAN_INSTANCE_NAME?lower_case}RxMsg[NUM_RX_FIFOS][NUM_RX_BUFFER_ELEMENTS];
static CAN_CALLBACK_OBJ ${CAN_INSTANCE_NAME?lower_case}CallbackObj[4];
</#if>
static CAN_OBJ ${CAN_INSTANCE_NAME?lower_case}Obj;
<#if FILTERS_STD?number gt 0>
<#assign numInstance=FILTERS_STD?number>

static const can_sidfe_registers_t ${CAN_INSTANCE_NAME?lower_case}StdFilter[] =
{
    <#list 1..(numInstance) as idx>
    {
        .CAN_SIDFE_0 = CAN_SIDFE_0_SFT(${.vars["${CAN_INSTANCE_NAME}_STD_FILTER${idx}_TYPE"]}UL) |
                  CAN_SIDFE_0_SFID1(0x${.vars["${CAN_INSTANCE_NAME}_STD_FILTER${idx}_SFID1"]}UL) |
                  CAN_SIDFE_0_SFID2(0x${.vars["${CAN_INSTANCE_NAME}_STD_FILTER${idx}_SFID2"]}UL) |
                  CAN_SIDFE_0_SFEC(${.vars["${CAN_INSTANCE_NAME}_STD_FILTER${idx}_CONFIG"]}UL)
    },
     </#list>
};
</#if>
<#if FILTERS_EXT?number gt 0>
<#assign numInstance=FILTERS_EXT?number>

static const can_xidfe_registers_t ${CAN_INSTANCE_NAME?lower_case}ExtFilter[] =
{
    <#list 1..(numInstance) as idx>
    {
        .CAN_XIDFE_0 = CAN_XIDFE_0_EFID1(0x${.vars["${CAN_INSTANCE_NAME}_EXT_FILTER${idx}_EFID1"]}UL) | CAN_XIDFE_0_EFEC(${.vars["${CAN_INSTANCE_NAME}_EXT_FILTER${idx}_CONFIG"]}UL),
        .CAN_XIDFE_1 = CAN_XIDFE_1_EFID2(0x${.vars["${CAN_INSTANCE_NAME}_EXT_FILTER${idx}_EFID2"]}UL) | CAN_XIDFE_1_EFT(${.vars["${CAN_INSTANCE_NAME}_EXT_FILTER${idx}_TYPE"]}UL),
    },
     </#list>
};
</#if>

/******************************************************************************
Local Functions
******************************************************************************/

<#if CAN_OPMODE != "NORMAL">
static void CANLengthToDlcGet(uint8_t length, uint8_t *dlc)
{
    if (length <= 8U)
    {
        *dlc = length;
    }
    else if (length <= 12U)
    {
        *dlc = 0x9U;
    }
    else if (length <= 16U)
    {
        *dlc = 0xAU;
    }
    else if (length <= 20U)
    {
        *dlc = 0xBU;
    }
    else if (length <= 24U)
    {
        *dlc = 0xCU;
    }
    else if (length <= 32U)
    {
        *dlc = 0xDU;
    }
    else if (length <= 48U)
    {
        *dlc = 0xEU;
    }
    else
    {
        *dlc = 0xFU;
    }
}
</#if>
static uint8_t CANDlcToLengthGet(uint8_t dlc)
{
    const uint8_t msgLength[] = {0U, 1U, 2U, 3U, 4U, 5U, 6U, 7U, 8U, 12U, 16U, 20U, 24U, 32U, 48U, 64U};
    return msgLength[dlc];
}

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
    /* Start CAN initialization */
    ${CAN_INSTANCE_NAME}_REGS->CAN_CCCR = CAN_CCCR_INIT_Msk;
    while ((${CAN_INSTANCE_NAME}_REGS->CAN_CCCR & CAN_CCCR_INIT_Msk) != CAN_CCCR_INIT_Msk)
    {
        /* Wait for initialization complete */
    }

    /* Set CCE to unlock the configuration registers */
    ${CAN_INSTANCE_NAME}_REGS->CAN_CCCR |= CAN_CCCR_CCE_Msk;

<#if CAN_OPMODE != "NORMAL">
    /* Set Data Bit Timing and Prescaler Register */
    ${CAN_INSTANCE_NAME}_REGS->CAN_DBTP = CAN_DBTP_DTSEG2(${CAN_DBTP_DTSEG2}UL) | CAN_DBTP_DTSEG1(${CAN_DBTP_DTSEG1}UL) | CAN_DBTP_DBRP(${DBTP_DBRP}UL) | CAN_DBTP_DSJW(${CAN_DBTP_DSJW}UL);

</#if>
    /* Set Nominal Bit timing and Prescaler Register */
    ${CAN_INSTANCE_NAME}_REGS->CAN_NBTP  = CAN_NBTP_NTSEG2(${CAN_NBTP_NTSEG2}UL) | CAN_NBTP_NTSEG1(${CAN_NBTP_NTSEG1}UL) | CAN_NBTP_NBRP(${NBTP_NBRP}UL) | CAN_NBTP_NSJW(${CAN_NBTP_NSJW}UL);

<#if RXF0_USE || RXF1_USE || RXBUF_USE>
  <#if CAN_OPMODE != "NORMAL">
    /* Receive Buffer / FIFO Element Size Configuration Register */
    ${CAN_INSTANCE_NAME}_REGS->CAN_RXESC = 0UL <#if RXF0_USE> | CAN_RXESC_F0DS(${RXF0_BYTES_CFG!0}UL)</#if><#if RXF1_USE> | CAN_RXESC_F1DS(${RXF1_BYTES_CFG!0}UL)</#if><#if RXBUF_USE> | CAN_RXESC_RBDS(${RX_BUFFER_BYTES_CFG!0}UL)</#if>;
  </#if>
</#if>
<#if RXBUF_USE>
    /*lint -e{9048} PC lint incorrectly reports a missing 'U' Suffix */
    ${CAN_INSTANCE_NAME}_REGS->CAN_NDAT1 = CAN_NDAT1_Msk;
    /*lint -e{9048} PC lint incorrectly reports a missing 'U' Suffix */
    ${CAN_INSTANCE_NAME}_REGS->CAN_NDAT2 = CAN_NDAT2_Msk;

</#if>
<#if TX_USE || TXBUF_USE>
  <#if CAN_OPMODE != "NORMAL">
    /* Transmit Buffer/FIFO Element Size Configuration Register */
    ${CAN_INSTANCE_NAME}_REGS->CAN_TXESC = CAN_TXESC_TBDS(${TX_FIFO_BYTES_CFG}UL);
  </#if>
</#if>

    /* Global Filter Configuration Register */
    ${CAN_INSTANCE_NAME}_REGS->CAN_GFC = ${FILTERS_STD_NOMATCH} | ${FILTERS_EXT_NOMATCH}<#if FILTERS_STD_REJECT> | CAN_GFC_RRFS_Msk</#if><#if FILTERS_EXT_REJECT> | CAN_GFC_RRFE_Msk</#if>;
<#if FILTERS_EXT?number gt 0>

    /* Extended ID AND Mask Register */
    ${CAN_INSTANCE_NAME}_REGS->CAN_XIDAM = CAN_XIDAM_Msk;
</#if>
<#if TIMESTAMP_ENABLE || CAN_TIMEOUT>

    /* Timestamp Counter Configuration Register */
    ${CAN_INSTANCE_NAME}_REGS->CAN_TSCC = CAN_TSCC_TCP(${TIMESTAMP_PRESCALER}UL)<#if TIMESTAMP_ENABLE == true> | ${TIMESTAMP_MODE}</#if>;
</#if>
<#if CAN_TIMEOUT>

    /* Timeout Counter Configuration Register */
    ${CAN_INSTANCE_NAME}_REGS->CAN_TOCC = ${TIMEOUT_SELECT} | CAN_TOCC_ETOC_Msk | CAN_TOCC_TOP(${TIMEOUT_COUNT}UL);
</#if>

    /* Set the operation mode */
    <#if CAN_OPMODE != "NORMAL">
    ${CAN_INSTANCE_NAME}_REGS->CAN_CCCR |= CAN_CCCR_FDOE_Msk | CAN_CCCR_BRSE_Msk<#rt>
                                           <#lt><#if CAN_OPMODE == "Restricted Operation Mode"> | CAN_CCCR_ASM_Msk</#if><#rt>
                                           <#lt><#if CAN_OPMODE == "Bus Monitoring Mode"> | CAN_CCCR_MON_Msk</#if><#rt>
                                           <#lt><#if CAN_OPMODE == "External Loop Back Mode"> | CAN_CCCR_TEST_Msk</#if><#rt>
                                           <#lt><#if CAN_OPMODE == "Internal Loop Back Mode"> | CAN_CCCR_TEST_Msk | CAN_CCCR_MON_Msk</#if>;
    </#if>
    <#if TX_PAUSE == true>
    ${CAN_INSTANCE_NAME}_REGS->CAN_CCCR |= CAN_CCCR_TXP_Msk;
    </#if>

    <#if CAN_OPMODE == "External Loop Back Mode" || CAN_OPMODE == "Internal Loop Back Mode">
    ${CAN_INSTANCE_NAME}_REGS->CAN_TEST |= CAN_TEST_LBCK_Msk;
    </#if>

    ${CAN_INSTANCE_NAME}_REGS->CAN_CCCR &= ~CAN_CCCR_INIT_Msk;
    while ((${CAN_INSTANCE_NAME}_REGS->CAN_CCCR & CAN_CCCR_INIT_Msk) == CAN_CCCR_INIT_Msk)
    {
        /* Wait for initialization complete */
    }
<#if INTERRUPT_MODE == true>

    /* Select interrupt line */
    ${CAN_INSTANCE_NAME}_REGS->CAN_ILS = 0x0U;

    /* Enable interrupt line */
    ${CAN_INSTANCE_NAME}_REGS->CAN_ILE = CAN_ILE_EINT0_Msk;

    /* Enable CAN interrupts */
    ${CAN_INSTANCE_NAME}_REGS->CAN_IE = CAN_IE_BOE_Msk;

    // Initialize the CAN PLib Object
    ${CAN_INSTANCE_NAME?lower_case}Obj.txBufferIndex = 0U;
    ${CAN_INSTANCE_NAME?lower_case}Obj.rxBufferIndex1 = 0U;
    ${CAN_INSTANCE_NAME?lower_case}Obj.rxBufferIndex2 = 0U;
    (void) memset(${CAN_INSTANCE_NAME?lower_case}RxMsg, 0x00, sizeof(${CAN_INSTANCE_NAME?lower_case}RxMsg));
</#if>
    (void) memset(&${CAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig, 0x00, sizeof(CAN_MSG_RAM_CONFIG));
}

// *****************************************************************************
/* Function:
    bool ${CAN_INSTANCE_NAME}_MessageTransmit(uint32_t id, uint8_t length, uint8_t* data, CAN_MODE mode, CAN_MSG_TX_ATTRIBUTE msgAttr)

   Summary:
    Transmits a message into CAN bus.

   Precondition:
    ${CAN_INSTANCE_NAME}_Initialize must have been called for the associated CAN instance.

   Parameters:
    id      - 11-bit / 29-bit identifier (ID).
    length  - length of data buffer in number of bytes.
    data    - pointer to source data buffer
    mode    - CAN mode Classic CAN or CAN FD without BRS or CAN FD with BRS
    msgAttr - Data Frame or Remote frame using Tx FIFO or Tx Buffer

   Returns:
    Request status.
    true  - Request was successful.
    false - Request has failed.
*/
bool ${CAN_INSTANCE_NAME}_MessageTransmit(uint32_t id, uint8_t length, uint8_t* data, CAN_MODE mode, CAN_MSG_TX_ATTRIBUTE msgAttr)
{
<#if CAN_OPMODE != "NORMAL">
    uint8_t dlc = 0U;
</#if>
<#if TXBUF_USE>
    uint8_t bufferIndex = 0U;
</#if>
    uint8_t tfqpi = 0U;
<#if TX_USE || TXBUF_USE>
    can_txbe_registers_t *fifo = NULL;
</#if>
    static uint8_t messageMarker = 0U;
    bool op_success = false;
    (void) mode;

    switch (msgAttr)
    {
<#if TXBUF_USE>
        case CAN_MSG_ATTR_TX_BUFFER_DATA_FRAME:
        case CAN_MSG_ATTR_TX_BUFFER_RTR_FRAME:
            for (bufferIndex = 0U; bufferIndex < ${TX_BUFFER_ELEMENTS}U; bufferIndex++)
            {
                if ((${CAN_INSTANCE_NAME?lower_case}Obj.txBufferIndex & (1UL << (bufferIndex & 0x1FU))) == 0U)
                {
                    ${CAN_INSTANCE_NAME?lower_case}Obj.txBufferIndex |= (uint8_t)(1UL << (bufferIndex & 0x1FU));
                    tfqpi = bufferIndex;
                    break;
                }
            }
            /* The Tx buffers are not full */
            if(bufferIndex != ${TX_BUFFER_ELEMENTS}U)
            {

                fifo = (can_txbe_registers_t *) ((uint8_t*)${CAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.txBuffersAddress + ((uint32_t)tfqpi * ${CAN_INSTANCE_NAME}_TX_FIFO_BUFFER_ELEMENT_SIZE));
                op_success = true;
            }
            break;
</#if>
<#if TX_USE>
        case CAN_MSG_ATTR_TX_FIFO_DATA_FRAME:
        case CAN_MSG_ATTR_TX_FIFO_RTR_FRAME:
            /* The FIFO is not full */
            if (0U == (${CAN_INSTANCE_NAME}_REGS->CAN_TXFQS & CAN_TXFQS_TFQF_Msk))
            {
                tfqpi = (uint8_t)((${CAN_INSTANCE_NAME}_REGS->CAN_TXFQS & CAN_TXFQS_TFQPI_Msk) >> CAN_TXFQS_TFQPI_Pos);
<#if TXBUF_USE>
                ${CAN_INSTANCE_NAME?lower_case}Obj.txBufferIndex |= (1UL << ((tfqpi + ${TX_BUFFER_ELEMENTS}U) & 0x1FU));
</#if>
                fifo = (can_txbe_registers_t *) ((uint8_t*)${CAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.txBuffersAddress + ((uint32_t)tfqpi * ${CAN_INSTANCE_NAME}_TX_FIFO_BUFFER_ELEMENT_SIZE));
                op_success = true;
            }
            break;
</#if>
        default:
            /* Invalid Message Attribute */
            break;
    }
    if (op_success)
    {
        /* If the id is longer than 11 bits, it is considered as extended identifier */
        if (id > CAN_STD_ID_Msk)
        {
            /* An extended identifier is stored into ID */
            fifo->CAN_TXBE_0 = (id & CAN_TXBE_0_ID_Msk) | CAN_TXBE_0_XTD_Msk;
        }
        else
        {
            /* A standard identifier is stored into ID[28:18] */
            fifo->CAN_TXBE_0 = id << 18U;
        }
<#if CAN_OPMODE != "NORMAL">
        if (length > 64U)
        {
            length = 64U;
        }

        CANLengthToDlcGet(length, &dlc);

        fifo->CAN_TXBE_1 = CAN_TXBE_1_DLC((uint32_t)dlc);

        if(mode == CAN_MODE_FD_WITH_BRS)
        {
            fifo->CAN_TXBE_1 |= CAN_TXBE_1_FDF_Msk | CAN_TXBE_1_BRS_Msk;
        }
        else if (mode == CAN_MODE_FD_WITHOUT_BRS)
        {
            fifo->CAN_TXBE_1 |= CAN_TXBE_1_FDF_Msk;
        }
        else
        {
            /* Do nothing */
        }
<#else>
        /* Limit length */
        if (length > 8U)
        {
            length = 8U;
        }
        fifo->CAN_TXBE_1 = CAN_TXBE_1_DLC((uint32_t)length);
</#if>
        if ((msgAttr == CAN_MSG_ATTR_TX_BUFFER_DATA_FRAME) || (msgAttr == CAN_MSG_ATTR_TX_FIFO_DATA_FRAME))
        {
            /* copy the data into the payload */
            (void) memcpy((uint8_t *)&fifo->CAN_TXBE_DATA, data, length);
        }
        else if ((msgAttr == CAN_MSG_ATTR_TX_BUFFER_RTR_FRAME) || (msgAttr == CAN_MSG_ATTR_TX_FIFO_RTR_FRAME))
        {
            fifo->CAN_TXBE_0 |= CAN_TXBE_0_RTR_Msk;
        }
        else
        {
            /* Do nothing */
        }

        messageMarker++;
        fifo->CAN_TXBE_1 |= (((uint32_t)(messageMarker) << CAN_TXBE_1_MM_Pos) & CAN_TXBE_1_MM_Msk) | CAN_TXBE_1_EFC_Msk;
<#if INTERRUPT_MODE == true>

        ${CAN_INSTANCE_NAME}_REGS->CAN_TXBTIE = 1UL << tfqpi;
</#if>

        /* request the transmit */
        ${CAN_INSTANCE_NAME}_REGS->CAN_TXBAR = 1UL << tfqpi;

<#if INTERRUPT_MODE == true>
        ${CAN_INSTANCE_NAME}_REGS->CAN_IE |= CAN_IE_TCE_Msk;
</#if>
<#if TXBUF_USE && INTERRUPT_MODE == false>
        for (bufferIndex = 0U; bufferIndex < (${CAN_INSTANCE_NAME}_TX_FIFO_BUFFER_SIZE/${CAN_INSTANCE_NAME}_TX_FIFO_BUFFER_ELEMENT_SIZE); bufferIndex++)
        {
            if (${CAN_INSTANCE_NAME}_REGS->CAN_TXBTO & (1UL << (bufferIndex & 0x1FU)))
            {
                if (0U != (${CAN_INSTANCE_NAME?lower_case}Obj.txBufferIndex & (1UL << (bufferIndex & 0x1FU))))
                {
                    ${CAN_INSTANCE_NAME?lower_case}Obj.txBufferIndex &= (~(1UL << (bufferIndex & 0x1FU)));
                }
            }
        }
</#if>
    }
    return op_success;
}

// *****************************************************************************
/* Function:
    bool ${CAN_INSTANCE_NAME}_MessageReceive(uint32_t *id, uint8_t *length, uint8_t *data, uint16_t *timestamp,
                                             CAN_MSG_RX_ATTRIBUTE msgAttr, CAN_MSG_RX_FRAME_ATTRIBUTE *msgFrameAttr)

   Summary:
    Receives a message from CAN bus.

   Precondition:
    ${CAN_INSTANCE_NAME}_Initialize must have been called for the associated CAN instance.

   Parameters:
    id           - Pointer to 11-bit / 29-bit identifier (ID) to be received.
    length       - Pointer to data length in number of bytes to be received.
    data         - pointer to destination data buffer
    timestamp    - Pointer to Rx message timestamp, timestamp value is 0 if timestamp is disabled
    msgAttr      - Message to be read from Rx FIFO0 or Rx FIFO1 or Rx Buffer
    msgFrameAttr - Data frame or Remote frame to be received

   Returns:
    Request status.
    true  - Request was successful.
    false - Request has failed.
*/
bool ${CAN_INSTANCE_NAME}_MessageReceive(uint32_t *id, uint8_t *length, uint8_t *data, uint16_t *timestamp,
                                         CAN_MSG_RX_ATTRIBUTE msgAttr, CAN_MSG_RX_FRAME_ATTRIBUTE *msgFrameAttr)
{
<#if INTERRUPT_MODE == false>
    uint8_t msgLength = 0U;
    uint8_t rxgi = 0U;
    bool testCondition = false;
<#if RXBUF_USE>
    can_rxbe_registers_t *rxbeFifo = NULL;
</#if>
<#if RXF0_USE>
    can_rxf0e_registers_t *rxf0eFifo = NULL;
</#if>
<#if RXF1_USE>
    can_rxf1e_registers_t *rxf1eFifo = NULL;
</#if>
<#else>
    uint8_t bufferIndex = 0U;
</#if>
    bool status = false;

    switch (msgAttr)
    {
<#if RXBUF_USE>
        case CAN_MSG_ATTR_RX_BUFFER:
<#if INTERRUPT_MODE == false>
            /* Check and return false if nothing to be read */
            testCondition = (${CAN_INSTANCE_NAME}_REGS->CAN_NDAT2 == 0U);
            testCondition = (${CAN_INSTANCE_NAME}_REGS->CAN_NDAT1 == 0U) && testCondition;
            if (testCondition)
            {
                return status;
            }
            /* Read data from the Rx Buffer */
            if (${CAN_INSTANCE_NAME}_REGS->CAN_NDAT1 != 0U)
            {
                for (rxgi = 0U; rxgi <= 0x1FU; rxgi++)
                {
                    if ((${CAN_INSTANCE_NAME}_REGS->CAN_NDAT1 & (1UL << rxgi)) == (1UL << rxgi))
                    {
                        break;
                    }
                }
            }
            else
            {
                for (rxgi = 0U; rxgi <= 0x1FU; rxgi++)
                {
                    if ((${CAN_INSTANCE_NAME}_REGS->CAN_NDAT2 & (1UL << rxgi)) == (1UL << rxgi))
                    {
                        rxgi = rxgi + 32U;
                        break;
                    }
                }
            }
            rxbeFifo = (can_rxbe_registers_t *) ((uint8_t *)${CAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.rxBuffersAddress + ((uint32_t)rxgi * ${CAN_INSTANCE_NAME}_RX_BUFFER_ELEMENT_SIZE));

            /* Get received identifier */
            if ((rxbeFifo->CAN_RXBE_0 & CAN_RXBE_0_XTD_Msk) != 0U)
            {
                *id = rxbeFifo->CAN_RXBE_0 & CAN_RXBE_0_ID_Msk;
            }
            else
            {
                *id = (rxbeFifo->CAN_RXBE_0 >> 18U) & CAN_STD_ID_Msk;
            }

            /* Check RTR and FDF bits for Remote/Data Frame */
            testCondition = ((rxbeFifo->CAN_RXBE_0 & CAN_RXBE_0_RTR_Msk) != 0U);
            testCondition = ((rxbeFifo->CAN_RXBE_1 & CAN_RXBE_1_FDF_Msk) == 0U) && testCondition;
            if (testCondition)
            {
                *msgFrameAttr = CAN_MSG_RX_REMOTE_FRAME;
            }
            else
            {
                *msgFrameAttr = CAN_MSG_RX_DATA_FRAME;
            }

            /* Get received data length */
            msgLength = CANDlcToLengthGet((uint8_t)((rxbeFifo->CAN_RXBE_1 & CAN_RXBE_1_DLC_Msk) >> CAN_RXBE_1_DLC_Pos));

            /* Copy data to user buffer */
            (void) memcpy(data, (uint8_t *)&rxbeFifo->CAN_RXBE_DATA, msgLength);
            *length = msgLength;

<#if TIMESTAMP_ENABLE>
            /* Get timestamp from received message */
            if (timestamp != NULL)
            {
                *timestamp = (uint16_t)(rxbeFifo->CAN_RXBE_1 & CAN_RXBE_1_RXTS_Msk);
            }

</#if>
            /* Clear new data flag */
            if (rxgi < 32U)
            {
                ${CAN_INSTANCE_NAME}_REGS->CAN_NDAT1 = (1UL << rxgi);
            }
            else
            {
                ${CAN_INSTANCE_NAME}_REGS->CAN_NDAT2 = (1UL << (rxgi - 32U));
            }
<#else>
            for (bufferIndex = 0U; bufferIndex < ${RX_BUFFER_ELEMENTS}U; bufferIndex++)
            {
                if (bufferIndex < 32U)
                {
                    if ((${CAN_INSTANCE_NAME?lower_case}Obj.rxBufferIndex1 & (1UL << (bufferIndex & 0x1FU))) == 0U)
                    {
                        ${CAN_INSTANCE_NAME?lower_case}Obj.rxBufferIndex1 |= (1UL << (bufferIndex & 0x1FU));
                        break;
                    }
                }
                else if ((${CAN_INSTANCE_NAME?lower_case}Obj.rxBufferIndex2 & (1UL << ((bufferIndex - 32U) & 0x1FU))) == 0U)
                {
                    ${CAN_INSTANCE_NAME?lower_case}Obj.rxBufferIndex2 |= (1UL << ((bufferIndex - 32U) & 0x1FU));
                    break;
                }
                else
                {
                    /* Do nothing */
                }
            }
            if(bufferIndex == ${RX_BUFFER_ELEMENTS}U)
            {
                /* The Rx buffers are full */
                return false;
            }
            ${CAN_INSTANCE_NAME?lower_case}RxMsg[msgAttr][bufferIndex].rxId = id;
            ${CAN_INSTANCE_NAME?lower_case}RxMsg[msgAttr][bufferIndex].rxBuffer = data;
            ${CAN_INSTANCE_NAME?lower_case}RxMsg[msgAttr][bufferIndex].rxsize = length;
            ${CAN_INSTANCE_NAME?lower_case}RxMsg[msgAttr][bufferIndex].timestamp = timestamp;
            ${CAN_INSTANCE_NAME?lower_case}RxMsg[msgAttr][bufferIndex].msgFrameAttr = msgFrameAttr;
            ${CAN_INSTANCE_NAME}_REGS->CAN_IE |= CAN_IE_DRXE_Msk;
</#if>
            status = true;
            break;
</#if>
<#if RXF0_USE>
        case CAN_MSG_ATTR_RX_FIFO0:
<#if INTERRUPT_MODE == false>
            /* Check and return false if nothing to be read */
            if ((${CAN_INSTANCE_NAME}_REGS->CAN_RXF0S & CAN_RXF0S_F0FL_Msk) == 0U)
            {
                return status;
            }
            /* Read data from the Rx FIFO0 */
            rxgi = (uint8_t)((${CAN_INSTANCE_NAME}_REGS->CAN_RXF0S & CAN_RXF0S_F0GI_Msk) >> CAN_RXF0S_F0GI_Pos);
            rxf0eFifo = (can_rxf0e_registers_t *) ((uint8_t *)${CAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.rxFIFO0Address + ((uint32_t)rxgi * ${CAN_INSTANCE_NAME}_RX_FIFO0_ELEMENT_SIZE));

            /* Get received identifier */
            if ((rxf0eFifo->CAN_RXF0E_0 & CAN_RXF0E_0_XTD_Msk) != 0U)
            {
                *id = rxf0eFifo->CAN_RXF0E_0 & CAN_RXF0E_0_ID_Msk;
            }
            else
            {
                *id = (rxf0eFifo->CAN_RXF0E_0 >> 18U) & CAN_STD_ID_Msk;
            }

            /* Check RTR and FDF bits for Remote/Data Frame */
            testCondition = ((rxf0eFifo->CAN_RXF0E_0 & CAN_RXF0E_0_RTR_Msk) != 0U);
            testCondition = ((rxf0eFifo->CAN_RXF0E_1 & CAN_RXF0E_1_FDF_Msk) == 0U) && testCondition;
            if (testCondition)
            {
                *msgFrameAttr = CAN_MSG_RX_REMOTE_FRAME;
            }
            else
            {
                *msgFrameAttr = CAN_MSG_RX_DATA_FRAME;
            }

            /* Get received data length */
            msgLength = CANDlcToLengthGet((uint8_t)((rxf0eFifo->CAN_RXF0E_1 & CAN_RXF0E_1_DLC_Msk) >> CAN_RXF0E_1_DLC_Pos));

            /* Copy data to user buffer */
            (void) memcpy(data, (uint8_t *)&rxf0eFifo->CAN_RXF0E_DATA, msgLength);
            *length = msgLength;

<#if TIMESTAMP_ENABLE>
            /* Get timestamp from received message */
            if (timestamp != NULL)
            {
                *timestamp = (uint16_t)(rxf0eFifo->CAN_RXF0E_1 & CAN_RXF0E_1_RXTS_Msk);
            }

</#if>
            /* Ack the fifo position */
            ${CAN_INSTANCE_NAME}_REGS->CAN_RXF0A = CAN_RXF0A_F0AI((uint32_t)rxgi);
<#else>
            bufferIndex = (uint8_t)((${CAN_INSTANCE_NAME}_REGS->CAN_RXF0S & CAN_RXF0S_F0GI_Msk) >> CAN_RXF0S_F0GI_Pos);
            ${CAN_INSTANCE_NAME?lower_case}RxMsg[msgAttr][bufferIndex].rxId = id;
            ${CAN_INSTANCE_NAME?lower_case}RxMsg[msgAttr][bufferIndex].rxBuffer = data;
            ${CAN_INSTANCE_NAME?lower_case}RxMsg[msgAttr][bufferIndex].rxsize = length;
            ${CAN_INSTANCE_NAME?lower_case}RxMsg[msgAttr][bufferIndex].timestamp = timestamp;
            ${CAN_INSTANCE_NAME?lower_case}RxMsg[msgAttr][bufferIndex].msgFrameAttr = msgFrameAttr;
            ${CAN_INSTANCE_NAME}_REGS->CAN_IE |= CAN_IE_RF0NE_Msk;
</#if>
            status = true;
            break;
</#if>
<#if RXF1_USE>
        case CAN_MSG_ATTR_RX_FIFO1:
<#if INTERRUPT_MODE == false>
            /* Check and return false if nothing to be read */
            if ((${CAN_INSTANCE_NAME}_REGS->CAN_RXF1S & CAN_RXF1S_F1FL_Msk) == 0U)
            {
                return status;
            }
            /* Read data from the Rx FIFO1 */
            rxgi = (uint8_t)((${CAN_INSTANCE_NAME}_REGS->CAN_RXF1S & CAN_RXF1S_F1GI_Msk) >> CAN_RXF1S_F1GI_Pos);
            rxf1eFifo = (can_rxf1e_registers_t *) ((uint8_t *)${CAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.rxFIFO1Address + ((uint32_t)rxgi * ${CAN_INSTANCE_NAME}_RX_FIFO1_ELEMENT_SIZE));

            /* Get received identifier */
            if ((rxf1eFifo->CAN_RXF1E_0 & CAN_RXF1E_0_XTD_Msk) != 0U)
            {
                *id = rxf1eFifo->CAN_RXF1E_0 & CAN_RXF1E_0_ID_Msk;
            }
            else
            {
                *id = (rxf1eFifo->CAN_RXF1E_0 >> 18U) & CAN_STD_ID_Msk;
            }

            /* Check RTR and FDF bits for Remote/Data Frame */
            testCondition = ((rxf1eFifo->CAN_RXF1E_0 & CAN_RXF1E_0_RTR_Msk) != 0U);
            testCondition = ((rxf1eFifo->CAN_RXF1E_1 & CAN_RXF1E_1_FDF_Msk) == 0U) && testCondition;
            if (testCondition)
            {
                *msgFrameAttr = CAN_MSG_RX_REMOTE_FRAME;
            }
            else
            {
                *msgFrameAttr = CAN_MSG_RX_DATA_FRAME;
            }

            /* Get received data length */
            msgLength = CANDlcToLengthGet((uint8_t)((rxf1eFifo->CAN_RXF1E_1 & CAN_RXF1E_1_DLC_Msk) >> CAN_RXF1E_1_DLC_Pos));

            /* Copy data to user buffer */
            (void) memcpy(data, (uint8_t *)&rxf1eFifo->CAN_RXF1E_DATA, msgLength);
            *length = msgLength;

<#if TIMESTAMP_ENABLE>
            /* Get timestamp from received message */
            if (timestamp != NULL)
            {
                *timestamp = (uint16_t)(rxf1eFifo->CAN_RXF1E_1 & CAN_RXF1E_1_RXTS_Msk);
            }

</#if>
            /* Ack the fifo position */
            ${CAN_INSTANCE_NAME}_REGS->CAN_RXF1A = CAN_RXF1A_F1AI((uint32_t)rxgi);
<#else>
            bufferIndex = (uint8_t)((${CAN_INSTANCE_NAME}_REGS->CAN_RXF1S & CAN_RXF1S_F1GI_Msk) >> CAN_RXF1S_F1GI_Pos);
            ${CAN_INSTANCE_NAME?lower_case}RxMsg[msgAttr][bufferIndex].rxId = id;
            ${CAN_INSTANCE_NAME?lower_case}RxMsg[msgAttr][bufferIndex].rxBuffer = data;
            ${CAN_INSTANCE_NAME?lower_case}RxMsg[msgAttr][bufferIndex].rxsize = length;
            ${CAN_INSTANCE_NAME?lower_case}RxMsg[msgAttr][bufferIndex].timestamp = timestamp;
            ${CAN_INSTANCE_NAME?lower_case}RxMsg[msgAttr][bufferIndex].msgFrameAttr = msgFrameAttr;
            ${CAN_INSTANCE_NAME}_REGS->CAN_IE |= CAN_IE_RF1NE_Msk;
</#if>
            status = true;
            break;
</#if>
        default:
            /* Do nothing */
            break;
    }
    return status;
}

// *****************************************************************************
/* Function:
    bool ${CAN_INSTANCE_NAME}_TransmitEventFIFOElementGet(uint32_t *id, uint8_t *messageMarker, uint16_t *timestamp)

   Summary:
    Get the Transmit Event FIFO Element for the transmitted message.

   Precondition:
    ${CAN_INSTANCE_NAME}_Initialize must have been called for the associated CAN instance.

   Parameters:
    id            - Pointer to 11-bit / 29-bit identifier (ID) to be received.
    messageMarker - Pointer to Tx message message marker number to be received
    timestamp     - Pointer to Tx message timestamp to be received, timestamp value is 0 if Timestamp is disabled

   Returns:
    Request status.
    true  - Request was successful.
    false - Request has failed.
*/
bool ${CAN_INSTANCE_NAME}_TransmitEventFIFOElementGet(uint32_t *id, uint8_t *messageMarker, uint16_t *timestamp)
{
    can_txefe_registers_t *txEventFIFOElement = NULL;
    uint8_t txefgi = 0U;
    bool status = false;

    /* Check if Tx Event FIFO Element available */
    if ((${CAN_INSTANCE_NAME}_REGS->CAN_TXEFS & CAN_TXEFS_EFFL_Msk) != 0U)
    {
        /* Get a pointer to Tx Event FIFO Element */
        txefgi = (uint8_t)((${CAN_INSTANCE_NAME}_REGS->CAN_TXEFS & CAN_TXEFS_EFGI_Msk) >> CAN_TXEFS_EFGI_Pos);
        txEventFIFOElement = (can_txefe_registers_t *) ((uint8_t *)${CAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.txEventFIFOAddress + ((uint32_t)txefgi * sizeof(can_txefe_registers_t)));

        /* Check if it's a extended message type */
        if (0U != (txEventFIFOElement->CAN_TXEFE_0 & CAN_TXEFE_0_XTD_Msk))
        {
            *id = txEventFIFOElement->CAN_TXEFE_0 & CAN_TXEFE_0_ID_Msk;
        }
        else
        {
            *id = (txEventFIFOElement->CAN_TXEFE_0 >> 18U) & CAN_STD_ID_Msk;
        }

        *messageMarker = (uint8_t)((txEventFIFOElement->CAN_TXEFE_1 & CAN_TXEFE_1_MM_Msk) >> CAN_TXEFE_1_MM_Pos);

        /* Get timestamp from transmitted message */
        if (timestamp != NULL)
        {
            *timestamp = (uint16_t)(txEventFIFOElement->CAN_TXEFE_1 & CAN_TXEFE_1_TXTS_Msk);
        }

        /* Ack the Tx Event FIFO position */
        ${CAN_INSTANCE_NAME}_REGS->CAN_TXEFA = CAN_TXEFA_EFAI((uint32_t)txefgi);

        /* Tx Event FIFO Element read successfully, so return true */
        status = true;
    }
    return status;
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
    CAN_ERROR error;
    uint32_t   errorStatus = ${CAN_INSTANCE_NAME}_REGS->CAN_PSR;

    error = (CAN_ERROR) ((errorStatus & CAN_PSR_LEC_Msk) | (errorStatus & CAN_PSR_EP_Msk) | (errorStatus & CAN_PSR_EW_Msk)
            | (errorStatus & CAN_PSR_BO_Msk) | (errorStatus & CAN_PSR_DLEC_Msk) | (errorStatus & CAN_PSR_PXE_Msk));

    if ((${CAN_INSTANCE_NAME}_REGS->CAN_CCCR & CAN_CCCR_INIT_Msk) == CAN_CCCR_INIT_Msk)
    {
        ${CAN_INSTANCE_NAME}_REGS->CAN_CCCR &= ~CAN_CCCR_INIT_Msk;
        while ((${CAN_INSTANCE_NAME}_REGS->CAN_CCCR & CAN_CCCR_INIT_Msk) == CAN_CCCR_INIT_Msk)
        {
            /* Wait for initialization complete */
        }
    }

    return error;
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
    *txErrorCount = (uint8_t)(${CAN_INSTANCE_NAME}_REGS->CAN_ECR & CAN_ECR_TEC_Msk);
    *rxErrorCount = (uint8_t)((${CAN_INSTANCE_NAME}_REGS->CAN_ECR & CAN_ECR_REC_Msk) >> CAN_ECR_REC_Pos);
}

// *****************************************************************************
/* Function:
    bool ${CAN_INSTANCE_NAME}_InterruptGet(CAN_INTERRUPT_MASK interruptMask)

   Summary:
    Returns the Interrupt status.

   Precondition:
    ${CAN_INSTANCE_NAME}_Initialize must have been called for the associated CAN instance.

   Parameters:
    interruptMask - Interrupt source number

   Returns:
    true - Requested interrupt is occurred.
    false - Requested interrupt is not occurred.
*/
bool ${CAN_INSTANCE_NAME}_InterruptGet(CAN_INTERRUPT_MASK interruptMask)
{
    return ((${CAN_INSTANCE_NAME}_REGS->CAN_IR & (uint32_t)interruptMask) != 0x0U);
}

// *****************************************************************************
/* Function:
    void ${CAN_INSTANCE_NAME}_InterruptClear(CAN_INTERRUPT_MASK interruptMask)

   Summary:
    Clears Interrupt status.

   Precondition:
    ${CAN_INSTANCE_NAME}_Initialize must have been called for the associated CAN instance.

   Parameters:
    interruptMask - Interrupt to be cleared

   Returns:
    None
*/
void ${CAN_INSTANCE_NAME}_InterruptClear(CAN_INTERRUPT_MASK interruptMask)
{
    ${CAN_INSTANCE_NAME}_REGS->CAN_IR = (uint32_t)interruptMask;
}

// *****************************************************************************
/* Function:
    bool ${CAN_INSTANCE_NAME}_TxFIFOIsFull(void)

   Summary:
    Returns true if Tx FIFO is full otherwise false.

   Precondition:
    ${CAN_INSTANCE_NAME}_Initialize must have been called for the associated CAN instance.

   Parameters:
    None

   Returns:
    true  - Tx FIFO is full.
    false - Tx FIFO is not full.
*/
bool ${CAN_INSTANCE_NAME}_TxFIFOIsFull(void)
{
    return ((${CAN_INSTANCE_NAME}_REGS->CAN_TXFQS & CAN_TXFQS_TFQF_Msk) == CAN_TXFQS_TFQF_Msk);
}

// *****************************************************************************
/* Function:
    void ${CAN_INSTANCE_NAME}_MessageRAMConfigSet(uint8_t *msgRAMConfigBaseAddress)

   Summary:
    Set the Message RAM Configuration.

   Precondition:
    ${CAN_INSTANCE_NAME}_Initialize must have been called for the associated CAN instance.

   Parameters:
    msgRAMConfigBaseAddress - Pointer to application allocated buffer base address.
                              Application must allocate buffer from non-cached
                              contiguous memory and buffer size must be
                              ${CAN_INSTANCE_NAME}_MESSAGE_RAM_CONFIG_SIZE

   Returns:
    None
*/
void ${CAN_INSTANCE_NAME}_MessageRAMConfigSet(uint8_t *msgRAMConfigBaseAddress)
{
    uint32_t offset = 0U;

    (void) memset(msgRAMConfigBaseAddress, 0x00, ${CAN_INSTANCE_NAME}_MESSAGE_RAM_CONFIG_SIZE);

    /* Set CAN CCCR Init for Message RAM Configuration */
    ${CAN_INSTANCE_NAME}_REGS->CAN_CCCR |= CAN_CCCR_INIT_Msk;
    while ((${CAN_INSTANCE_NAME}_REGS->CAN_CCCR & CAN_CCCR_INIT_Msk) != CAN_CCCR_INIT_Msk)
    {
        /* Wait for initialization complete */
    }

    /* Set CCE to unlock the configuration registers */
    ${CAN_INSTANCE_NAME}_REGS->CAN_CCCR |= CAN_CCCR_CCE_Msk;

<#if RXF0_USE>
    ${CAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.rxFIFO0Address = (can_rxf0e_registers_t *)msgRAMConfigBaseAddress;
    offset = ${CAN_INSTANCE_NAME}_RX_FIFO0_SIZE;
    /* Receive FIFO 0 Configuration Register */
    ${CAN_INSTANCE_NAME}_REGS->CAN_RXF0C = CAN_RXF0C_F0S(${RXF0_ELEMENTS}UL) | CAN_RXF0C_F0WM(${RXF0_WATERMARK}UL)<#if RXF0_OVERWRITE> | CAN_RXF0C_F0OM_Msk</#if> |
            CAN_RXF0C_F0SA((uint32_t)${CAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.rxFIFO0Address);

</#if>
<#if RXF1_USE>
    ${CAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.rxFIFO1Address = (can_rxf1e_registers_t *)(msgRAMConfigBaseAddress + offset);
    offset += ${CAN_INSTANCE_NAME}_RX_FIFO1_SIZE;
    /* Receive FIFO 1 Configuration Register */
    ${CAN_INSTANCE_NAME}_REGS->CAN_RXF1C = CAN_RXF1C_F1S(${RXF1_ELEMENTS}UL) | CAN_RXF1C_F1WM(${RXF1_WATERMARK}UL)<#if RXF1_OVERWRITE> | CAN_RXF1C_F1OM_Msk</#if> |
            CAN_RXF1C_F1SA((uint32_t)${CAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.rxFIFO1Address);

</#if>
<#if RXBUF_USE>
    ${CAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.rxBuffersAddress = (can_rxbe_registers_t *)(msgRAMConfigBaseAddress + offset);
    offset += ${CAN_INSTANCE_NAME}_RX_BUFFER_SIZE;
    ${CAN_INSTANCE_NAME}_REGS->CAN_RXBC = CAN_RXBC_RBSA((uint32_t)${CAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.rxBuffersAddress);

</#if>
<#if TX_USE || TXBUF_USE>
    ${CAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.txBuffersAddress = (can_txbe_registers_t *)(msgRAMConfigBaseAddress + offset);
    offset += ${CAN_INSTANCE_NAME}_TX_FIFO_BUFFER_SIZE;
    /* Transmit Buffer/FIFO Configuration Register */
    ${CAN_INSTANCE_NAME}_REGS->CAN_TXBC = CAN_TXBC_TFQS(${TX_FIFO_ELEMENTS}UL)<#if TXBUF_USE> | CAN_TXBC_NDTB(${TX_BUFFER_ELEMENTS}UL)</#if> |
            CAN_TXBC_TBSA((uint32_t)${CAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.txBuffersAddress);

    ${CAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.txEventFIFOAddress =  (can_txefe_registers_t *)(msgRAMConfigBaseAddress + offset);
    offset += ${CAN_INSTANCE_NAME}_TX_EVENT_FIFO_SIZE;
    /* Transmit Event FIFO Configuration Register */
    ${CAN_INSTANCE_NAME}_REGS->CAN_TXEFC = CAN_TXEFC_EFWM(${TX_FIFO_WATERMARK}UL) | CAN_TXEFC_EFS(${TX_FIFO_ELEMENTS}UL) |
            CAN_TXEFC_EFSA((uint32_t)${CAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.txEventFIFOAddress);

</#if>
<#if FILTERS_STD?number gt 0>
    ${CAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.stdMsgIDFilterAddress = (can_sidfe_registers_t *)(msgRAMConfigBaseAddress + offset);
    (void) memcpy(${CAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.stdMsgIDFilterAddress,
           (const void *)${CAN_INSTANCE_NAME?lower_case}StdFilter,
           ${CAN_INSTANCE_NAME}_STD_MSG_ID_FILTER_SIZE);
    offset += ${CAN_INSTANCE_NAME}_STD_MSG_ID_FILTER_SIZE;
    /* Standard ID Filter Configuration Register */
    ${CAN_INSTANCE_NAME}_REGS->CAN_SIDFC = CAN_SIDFC_LSS(${FILTERS_STD}UL) |
            CAN_SIDFC_FLSSA((uint32_t)${CAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.stdMsgIDFilterAddress);

</#if>
<#if FILTERS_EXT?number gt 0>
    ${CAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.extMsgIDFilterAddress = (can_xidfe_registers_t *)(msgRAMConfigBaseAddress + offset);
    (void) memcpy(${CAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.extMsgIDFilterAddress,
           (const void *)${CAN_INSTANCE_NAME?lower_case}ExtFilter,
           ${CAN_INSTANCE_NAME}_EXT_MSG_ID_FILTER_SIZE);
    /* Extended ID Filter Configuration Register */
    ${CAN_INSTANCE_NAME}_REGS->CAN_XIDFC = CAN_XIDFC_LSE(${FILTERS_EXT}UL) |
            CAN_XIDFC_FLESA((uint32_t)${CAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.extMsgIDFilterAddress);
</#if>

    /* Reference offset variable once to remove warning about the variable not being used after increment */
    (void)offset;

    /* Complete Message RAM Configuration by clearing CAN CCCR Init */
    ${CAN_INSTANCE_NAME}_REGS->CAN_CCCR &= ~CAN_CCCR_INIT_Msk;
    while ((${CAN_INSTANCE_NAME}_REGS->CAN_CCCR & CAN_CCCR_INIT_Msk) == CAN_CCCR_INIT_Msk)
    {
        /* Wait for configuration complete */
    }
}

<#if FILTERS_STD?number gt 0>
// *****************************************************************************
/* Function:
    bool ${CAN_INSTANCE_NAME}_StandardFilterElementSet(uint8_t filterNumber, can_sidfe_registers_t *stdMsgIDFilterElement)

   Summary:
    Set a standard filter element configuration.

   Precondition:
    ${CAN_INSTANCE_NAME}_Initialize and ${CAN_INSTANCE_NAME}_MessageRAMConfigSet must have been called
    for the associated CAN instance.

   Parameters:
    filterNumber          - Standard Filter number to be configured.
    stdMsgIDFilterElement - Pointer to Standard Filter Element configuration to be set on specific filterNumber.

   Returns:
    Request status.
    true  - Request was successful.
    false - Request has failed.
*/
bool ${CAN_INSTANCE_NAME}_StandardFilterElementSet(uint8_t filterNumber, can_sidfe_registers_t *stdMsgIDFilterElement)
{
    bool retval = false;
    if (!((filterNumber > ${FILTERS_STD}U) || (stdMsgIDFilterElement == NULL)))
    {
        ${CAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.stdMsgIDFilterAddress[filterNumber - 1U].CAN_SIDFE_0 = stdMsgIDFilterElement->CAN_SIDFE_0;
        retval = true;
    }

    return retval;
}

// *****************************************************************************
/* Function:
    bool ${CAN_INSTANCE_NAME}_StandardFilterElementGet(uint8_t filterNumber, can_sidfe_registers_t *stdMsgIDFilterElement)

   Summary:
    Get a standard filter element configuration.

   Precondition:
    ${CAN_INSTANCE_NAME}_Initialize and ${CAN_INSTANCE_NAME}_MessageRAMConfigSet must have been called
    for the associated CAN instance.

   Parameters:
    filterNumber          - Standard Filter number to get filter configuration.
    stdMsgIDFilterElement - Pointer to Standard Filter Element configuration for storing filter configuration.

   Returns:
    Request status.
    true  - Request was successful.
    false - Request has failed.
*/
bool ${CAN_INSTANCE_NAME}_StandardFilterElementGet(uint8_t filterNumber, can_sidfe_registers_t *stdMsgIDFilterElement)
{
    bool retval = false;
    if (!((filterNumber > ${FILTERS_STD}U) || (stdMsgIDFilterElement == NULL)))
    {
        stdMsgIDFilterElement->CAN_SIDFE_0 = ${CAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.stdMsgIDFilterAddress[filterNumber - 1U].CAN_SIDFE_0;
        retval = true;
    }
    return retval;
}
</#if>

<#if FILTERS_EXT?number gt 0>
// *****************************************************************************
/* Function:
    bool ${CAN_INSTANCE_NAME}_ExtendedFilterElementSet(uint8_t filterNumber, can_xidfe_registers_t *extMsgIDFilterElement)

   Summary:
    Set a Extended filter element configuration.

   Precondition:
    ${CAN_INSTANCE_NAME}_Initialize and ${CAN_INSTANCE_NAME}_MessageRAMConfigSet must have been called
    for the associated CAN instance.

   Parameters:
    filterNumber          - Extended Filter number to be configured.
    extMsgIDFilterElement - Pointer to Extended Filter Element configuration to be set on specific filterNumber.

   Returns:
    Request status.
    true  - Request was successful.
    false - Request has failed.
*/
bool ${CAN_INSTANCE_NAME}_ExtendedFilterElementSet(uint8_t filterNumber, can_xidfe_registers_t *extMsgIDFilterElement)
{
    bool retval = false;
    if (!((filterNumber > ${FILTERS_EXT}U) || (extMsgIDFilterElement == NULL)))
    {
        ${CAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.extMsgIDFilterAddress[filterNumber - 1U].CAN_XIDFE_0 = extMsgIDFilterElement->CAN_XIDFE_0;
        ${CAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.extMsgIDFilterAddress[filterNumber - 1U].CAN_XIDFE_1 = extMsgIDFilterElement->CAN_XIDFE_1;
        retval = true;
    }
    return retval;
}

// *****************************************************************************
/* Function:
    bool ${CAN_INSTANCE_NAME}_ExtendedFilterElementGet(uint8_t filterNumber, can_xidfe_registers_t *extMsgIDFilterElement)

   Summary:
    Get a Extended filter element configuration.

   Precondition:
    ${CAN_INSTANCE_NAME}_Initialize and ${CAN_INSTANCE_NAME}_MessageRAMConfigSet must have been called
    for the associated CAN instance.

   Parameters:
    filterNumber          - Extended Filter number to get filter configuration.
    extMsgIDFilterElement - Pointer to Extended Filter Element configuration for storing filter configuration.

   Returns:
    Request status.
    true  - Request was successful.
    false - Request has failed.
*/
bool ${CAN_INSTANCE_NAME}_ExtendedFilterElementGet(uint8_t filterNumber, can_xidfe_registers_t *extMsgIDFilterElement)
{
    bool retval = false;
    if (!((filterNumber > ${FILTERS_EXT}U) || (extMsgIDFilterElement == NULL)))
    {
         extMsgIDFilterElement->CAN_XIDFE_0 = ${CAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.extMsgIDFilterAddress[filterNumber - 1U].CAN_XIDFE_0;
         extMsgIDFilterElement->CAN_XIDFE_1 = ${CAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.extMsgIDFilterAddress[filterNumber - 1U].CAN_XIDFE_1;
         retval = true;
    }
    return retval;
}
</#if>

void ${CAN_INSTANCE_NAME}_SleepModeEnter(void)
{
    ${CAN_INSTANCE_NAME}_REGS->CAN_CCCR |=  CAN_CCCR_CSR_Msk;
    while ((${CAN_INSTANCE_NAME}_REGS->CAN_CCCR & CAN_CCCR_CSA_Msk) != CAN_CCCR_CSA_Msk)
    {
        /* Wait for clock stop request to complete */
    }
}

void ${CAN_INSTANCE_NAME}_SleepModeExit(void)
{
    ${CAN_INSTANCE_NAME}_REGS->CAN_CCCR &=  ~CAN_CCCR_CSR_Msk;
    while ((${CAN_INSTANCE_NAME}_REGS->CAN_CCCR & CAN_CCCR_CSA_Msk) == CAN_CCCR_CSA_Msk)
    {
        /* Wait for no clock stop */
    }
    ${CAN_INSTANCE_NAME}_REGS->CAN_CCCR &= ~CAN_CCCR_INIT_Msk;
    while ((${CAN_INSTANCE_NAME}_REGS->CAN_CCCR & CAN_CCCR_INIT_Msk) == CAN_CCCR_INIT_Msk)
    {
        /* Wait for initialization complete */
    }
}

<#if INTERRUPT_MODE == true>
// *****************************************************************************
/* Function:
    void ${CAN_INSTANCE_NAME}_TxCallbackRegister(CAN_CALLBACK callback, uintptr_t contextHandle)

   Summary:
    Sets the pointer to the function (and it's context) to be called when the
    given CAN's transfer events occur.

   Precondition:
    ${CAN_INSTANCE_NAME}_Initialize must have been called for the associated CAN instance.

   Parameters:
    callback - A pointer to a function with a calling signature defined
    by the CAN_CALLBACK data type.

    contextHandle - A value (usually a pointer) passed (unused) into the function
    identified by the callback parameter.

   Returns:
    None.
*/
void ${CAN_INSTANCE_NAME}_TxCallbackRegister(CAN_CALLBACK callback, uintptr_t contextHandle)
{
    if (callback != NULL)
    {
        ${CAN_INSTANCE_NAME?lower_case}CallbackObj[CAN_CALLBACK_TX_INDEX].callback = callback;
        ${CAN_INSTANCE_NAME?lower_case}CallbackObj[CAN_CALLBACK_TX_INDEX].context = contextHandle;
    }
}

// *****************************************************************************
/* Function:
    void ${CAN_INSTANCE_NAME}_RxCallbackRegister(CAN_CALLBACK callback, uintptr_t contextHandle, CAN_MSG_RX_ATTRIBUTE msgAttr)

   Summary:
    Sets the pointer to the function (and it's context) to be called when the
    given CAN's transfer events occur.

   Precondition:
    ${CAN_INSTANCE_NAME}_Initialize must have been called for the associated CAN instance.

   Parameters:
    callback - A pointer to a function with a calling signature defined
    by the CAN_CALLBACK data type.

    contextHandle - A value (usually a pointer) passed (unused) into the function
    identified by the callback parameter.

    msgAttr   - Message to be read from Rx FIFO0 or Rx FIFO1 or Rx Buffer

   Returns:
    None.
*/
void ${CAN_INSTANCE_NAME}_RxCallbackRegister(CAN_CALLBACK callback, uintptr_t contextHandle, CAN_MSG_RX_ATTRIBUTE msgAttr)
{
    if (callback != NULL)
    {
        ${CAN_INSTANCE_NAME?lower_case}CallbackObj[msgAttr].callback = callback;
        ${CAN_INSTANCE_NAME?lower_case}CallbackObj[msgAttr].context = contextHandle;
    }
}

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
    uint8_t length = 0U;
    uint8_t rxgi = 0U;
    uint8_t bufferIndex = 0U;
    bool testCondition = false;
<#if RXBUF_USE>
    can_rxbe_registers_t *rxbeFifo = NULL;
</#if>
<#if RXF0_USE>
    can_rxf0e_registers_t *rxf0eFifo = NULL;
</#if>
<#if RXF1_USE>
    can_rxf1e_registers_t *rxf1eFifo = NULL;
</#if>
    uint32_t ir = ${CAN_INSTANCE_NAME}_REGS->CAN_IR;

    /* Check if error occurred */
    if ((ir & CAN_IR_BO_Msk) != 0U)
    {
        ${CAN_INSTANCE_NAME}_REGS->CAN_IR = CAN_IR_BO_Msk;
    }
<#if RXF0_USE>
    /* New Message in Rx FIFO 0 */
    if ((ir & CAN_IR_RF0N_Msk) != 0U)
    {
        ${CAN_INSTANCE_NAME}_REGS->CAN_IR = CAN_IR_RF0N_Msk;
        ${CAN_INSTANCE_NAME}_REGS->CAN_IE &= (~CAN_IE_RF0NE_Msk);

        if ((${CAN_INSTANCE_NAME}_REGS->CAN_RXF0S & CAN_RXF0S_F0FL_Msk) != 0U)
        {
            /* Read data from the Rx FIFO0 */
            rxgi = (uint8_t)((${CAN_INSTANCE_NAME}_REGS->CAN_RXF0S & CAN_RXF0S_F0GI_Msk) >> CAN_RXF0S_F0GI_Pos);
            rxf0eFifo = (can_rxf0e_registers_t *) ((uint8_t *)${CAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.rxFIFO0Address + ((uint32_t)rxgi * ${CAN_INSTANCE_NAME}_RX_FIFO0_ELEMENT_SIZE));

            /* Get received identifier */
            if ((rxf0eFifo->CAN_RXF0E_0 & CAN_RXF0E_0_XTD_Msk) != 0U)
            {
                *${CAN_INSTANCE_NAME?lower_case}RxMsg[CAN_MSG_ATTR_RX_FIFO0][rxgi].rxId = rxf0eFifo->CAN_RXF0E_0 & CAN_RXF0E_0_ID_Msk;
            }
            else
            {
                *${CAN_INSTANCE_NAME?lower_case}RxMsg[CAN_MSG_ATTR_RX_FIFO0][rxgi].rxId = (rxf0eFifo->CAN_RXF0E_0 >> 18U) & CAN_STD_ID_Msk;
            }

            /* Check RTR and FDF bits for Remote/Data Frame */
            testCondition = ((rxf0eFifo->CAN_RXF0E_0 & CAN_RXF0E_0_RTR_Msk) != 0U);
            testCondition = ((rxf0eFifo->CAN_RXF0E_1 & CAN_RXF0E_1_FDF_Msk) == 0U) && testCondition;
            if (testCondition)
            {
                *${CAN_INSTANCE_NAME?lower_case}RxMsg[CAN_MSG_ATTR_RX_FIFO0][rxgi].msgFrameAttr = CAN_MSG_RX_REMOTE_FRAME;
            }
            else
            {
                *${CAN_INSTANCE_NAME?lower_case}RxMsg[CAN_MSG_ATTR_RX_FIFO0][rxgi].msgFrameAttr = CAN_MSG_RX_DATA_FRAME;
            }

            /* Get received data length */
            length = CANDlcToLengthGet((uint8_t)((rxf0eFifo->CAN_RXF0E_1 & CAN_RXF0E_1_DLC_Msk) >> CAN_RXF0E_1_DLC_Pos));

            /* Copy data to user buffer */
            (void) memcpy(${CAN_INSTANCE_NAME?lower_case}RxMsg[CAN_MSG_ATTR_RX_FIFO0][rxgi].rxBuffer, (uint8_t *)&rxf0eFifo->CAN_RXF0E_DATA, length);
            *${CAN_INSTANCE_NAME?lower_case}RxMsg[CAN_MSG_ATTR_RX_FIFO0][rxgi].rxsize = length;

            <#if TIMESTAMP_ENABLE>
            /* Get timestamp from received message */
            if (${CAN_INSTANCE_NAME?lower_case}RxMsg[CAN_MSG_ATTR_RX_FIFO0][rxgi].timestamp != NULL)
            {
                *${CAN_INSTANCE_NAME?lower_case}RxMsg[CAN_MSG_ATTR_RX_FIFO0][rxgi].timestamp = (uint16_t)(rxf0eFifo->CAN_RXF0E_1 & CAN_RXF0E_1_RXTS_Msk);
            }

            </#if>
            /* Ack the fifo position */
            ${CAN_INSTANCE_NAME}_REGS->CAN_RXF0A = CAN_RXF0A_F0AI((uint32_t)rxgi);

            if (${CAN_INSTANCE_NAME?lower_case}CallbackObj[CAN_MSG_ATTR_RX_FIFO0].callback != NULL)
            {
                ${CAN_INSTANCE_NAME?lower_case}CallbackObj[CAN_MSG_ATTR_RX_FIFO0].callback(${CAN_INSTANCE_NAME?lower_case}CallbackObj[CAN_MSG_ATTR_RX_FIFO0].context);
            }
        }
    }
</#if>
<#if RXF1_USE>
    /* New Message in Rx FIFO 1 */
    if ((ir & CAN_IR_RF1N_Msk) != 0U)
    {
        ${CAN_INSTANCE_NAME}_REGS->CAN_IR = CAN_IR_RF1N_Msk;
        ${CAN_INSTANCE_NAME}_REGS->CAN_IE &= (~CAN_IE_RF1NE_Msk);

        if ((${CAN_INSTANCE_NAME}_REGS->CAN_RXF1S & CAN_RXF1S_F1FL_Msk) != 0U)
        {
            /* Read data from the Rx FIFO1 */
            rxgi = (uint8_t)((${CAN_INSTANCE_NAME}_REGS->CAN_RXF1S & CAN_RXF1S_F1GI_Msk) >> CAN_RXF1S_F1GI_Pos);
            rxf1eFifo = (can_rxf1e_registers_t *) ((uint8_t *)${CAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.rxFIFO1Address + ((uint32_t)rxgi * ${CAN_INSTANCE_NAME}_RX_FIFO1_ELEMENT_SIZE));

            /* Get received identifier */
            if ((rxf1eFifo->CAN_RXF1E_0 & CAN_RXF1E_0_XTD_Msk) != 0U)
            {
                *${CAN_INSTANCE_NAME?lower_case}RxMsg[CAN_MSG_ATTR_RX_FIFO1][rxgi].rxId = rxf1eFifo->CAN_RXF1E_0 & CAN_RXF1E_0_ID_Msk;
            }
            else
            {
                *${CAN_INSTANCE_NAME?lower_case}RxMsg[CAN_MSG_ATTR_RX_FIFO1][rxgi].rxId = (rxf1eFifo->CAN_RXF1E_0 >> 18U) & CAN_STD_ID_Msk;
            }

            /* Check RTR and FDF bits for Remote/Data Frame */
            testCondition = ((rxf1eFifo->CAN_RXF1E_0 & CAN_RXF1E_0_RTR_Msk) != 0U);
            testCondition = ((rxf1eFifo->CAN_RXF1E_1 & CAN_RXF1E_1_FDF_Msk) == 0U) && testCondition;
            if (testCondition)
            {
                *${CAN_INSTANCE_NAME?lower_case}RxMsg[CAN_MSG_ATTR_RX_FIFO1][rxgi].msgFrameAttr = CAN_MSG_RX_REMOTE_FRAME;
            }
            else
            {
                *${CAN_INSTANCE_NAME?lower_case}RxMsg[CAN_MSG_ATTR_RX_FIFO1][rxgi].msgFrameAttr = CAN_MSG_RX_DATA_FRAME;
            }

            /* Get received data length */
            length = CANDlcToLengthGet((uint8_t)((rxf1eFifo->CAN_RXF1E_1 & CAN_RXF1E_1_DLC_Msk) >> CAN_RXF1E_1_DLC_Pos));

            /* Copy data to user buffer */
            (void) memcpy(${CAN_INSTANCE_NAME?lower_case}RxMsg[CAN_MSG_ATTR_RX_FIFO1][rxgi].rxBuffer, (uint8_t *)&rxf1eFifo->CAN_RXF1E_DATA, length);
            *${CAN_INSTANCE_NAME?lower_case}RxMsg[CAN_MSG_ATTR_RX_FIFO1][rxgi].rxsize = length;

            <#if TIMESTAMP_ENABLE>
            /* Get timestamp from received message */
            if (${CAN_INSTANCE_NAME?lower_case}RxMsg[CAN_MSG_ATTR_RX_FIFO1][rxgi].timestamp != NULL)
            {
                *${CAN_INSTANCE_NAME?lower_case}RxMsg[CAN_MSG_ATTR_RX_FIFO1][rxgi].timestamp = (uint16_t)(rxf1eFifo->CAN_RXF1E_1 & CAN_RXF1E_1_RXTS_Msk);
            }

            </#if>
            /* Ack the fifo position */
            ${CAN_INSTANCE_NAME}_REGS->CAN_RXF1A = CAN_RXF1A_F1AI((uint32_t)rxgi);

            if (${CAN_INSTANCE_NAME?lower_case}CallbackObj[CAN_MSG_ATTR_RX_FIFO1].callback != NULL)
            {
                ${CAN_INSTANCE_NAME?lower_case}CallbackObj[CAN_MSG_ATTR_RX_FIFO1].callback(${CAN_INSTANCE_NAME?lower_case}CallbackObj[CAN_MSG_ATTR_RX_FIFO1].context);
            }
        }
    }
</#if>
<#if RXBUF_USE>
    /* New Message in Dedicated Rx Buffer */
    if ((ir & CAN_IR_DRX_Msk) != 0U)
    {
        ${CAN_INSTANCE_NAME}_REGS->CAN_IR = CAN_IR_DRX_Msk;
        ${CAN_INSTANCE_NAME}_REGS->CAN_IE &= (~CAN_IE_DRXE_Msk);

        /* Read data from the Rx Buffer */
        if (${CAN_INSTANCE_NAME}_REGS->CAN_NDAT1 != 0U)
        {
            for (rxgi = 0U; rxgi <= 0x1FU; rxgi++)
            {
                if ((${CAN_INSTANCE_NAME}_REGS->CAN_NDAT1 & (1UL << rxgi)) == (1UL << rxgi))
                {
                    break;
                }
            }
        }
        else
        {
            for (rxgi = 0U; rxgi <= 0x1FU; rxgi++)
            {
                if ((${CAN_INSTANCE_NAME}_REGS->CAN_NDAT2 & (1UL << rxgi)) == (1UL << rxgi))
                {
                    rxgi = rxgi + 32U;
                    break;
                }
            }
        }
        rxbeFifo = (can_rxbe_registers_t *) ((uint8_t *)${CAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.rxBuffersAddress + ((uint32_t)rxgi * ${CAN_INSTANCE_NAME}_RX_BUFFER_ELEMENT_SIZE));

        for (bufferIndex = 0U; bufferIndex < ${RX_BUFFER_ELEMENTS}U; bufferIndex++)
        {
            if (bufferIndex < 32U)
            {
                if ((${CAN_INSTANCE_NAME?lower_case}Obj.rxBufferIndex1 & (1UL << (bufferIndex & 0x1FU))) == (1UL << (bufferIndex & 0x1FU)))
                {
                    ${CAN_INSTANCE_NAME?lower_case}Obj.rxBufferIndex1 &= ~(1UL << (bufferIndex & 0x1FU));
                    break;
                }
            }
            else if ((${CAN_INSTANCE_NAME?lower_case}Obj.rxBufferIndex2 & (1UL << ((bufferIndex - 32U) & 0x1FU))) == (1UL << ((bufferIndex - 32U) & 0x1FU)))
            {
                ${CAN_INSTANCE_NAME?lower_case}Obj.rxBufferIndex2 &= ~(1UL << ((bufferIndex - 32U) & 0x1FU));
                break;
            }
            else
            {
                /* Do nothing */
            }
        }

        if(bufferIndex >= NUM_RX_BUFFER_ELEMENTS)
        {
            bufferIndex = (uint8_t)(NUM_RX_BUFFER_ELEMENTS - 1U);
        }

        /* Get received identifier */
        if ((rxbeFifo->CAN_RXBE_0 & CAN_RXBE_0_XTD_Msk) != 0U)
        {
            *${CAN_INSTANCE_NAME?lower_case}RxMsg[CAN_MSG_ATTR_RX_BUFFER][bufferIndex].rxId = rxbeFifo->CAN_RXBE_0 & CAN_RXBE_0_ID_Msk;
        }
        else
        {
            *${CAN_INSTANCE_NAME?lower_case}RxMsg[CAN_MSG_ATTR_RX_BUFFER][bufferIndex].rxId = (rxbeFifo->CAN_RXBE_0 >> 18U) & CAN_STD_ID_Msk;
        }

        /* Check RTR and FDF bits for Remote/Data Frame */
        testCondition = ((rxbeFifo->CAN_RXBE_0 & CAN_RXBE_0_RTR_Msk) != 0U);
        testCondition  = ((rxbeFifo->CAN_RXBE_1 & CAN_RXBE_1_FDF_Msk) == 0U) && testCondition;
        if (testCondition)
        {
            *${CAN_INSTANCE_NAME?lower_case}RxMsg[CAN_MSG_ATTR_RX_BUFFER][bufferIndex].msgFrameAttr = CAN_MSG_RX_REMOTE_FRAME;
        }
        else
        {
            *${CAN_INSTANCE_NAME?lower_case}RxMsg[CAN_MSG_ATTR_RX_BUFFER][bufferIndex].msgFrameAttr = CAN_MSG_RX_DATA_FRAME;
        }

        /* Get received data length */
        length = CANDlcToLengthGet((uint8_t)((rxbeFifo->CAN_RXBE_1 & CAN_RXBE_1_DLC_Msk) >> CAN_RXBE_1_DLC_Pos));

        /* Copy data to user buffer */
        (void) memcpy(${CAN_INSTANCE_NAME?lower_case}RxMsg[CAN_MSG_ATTR_RX_BUFFER][bufferIndex].rxBuffer, (uint8_t *)&rxbeFifo->CAN_RXBE_DATA, length);
        *${CAN_INSTANCE_NAME?lower_case}RxMsg[CAN_MSG_ATTR_RX_BUFFER][bufferIndex].rxsize = length;

        <#if TIMESTAMP_ENABLE>
        /* Get timestamp from received message */
        if (${CAN_INSTANCE_NAME?lower_case}RxMsg[CAN_MSG_ATTR_RX_BUFFER][bufferIndex].timestamp != NULL)
        {
            *${CAN_INSTANCE_NAME?lower_case}RxMsg[CAN_MSG_ATTR_RX_BUFFER][bufferIndex].timestamp = (uint16_t)(rxbeFifo->CAN_RXBE_1 & CAN_RXBE_1_RXTS_Msk);
        }

        </#if>
        /* Clear new data flag */
        if (rxgi < 32U)
        {
            ${CAN_INSTANCE_NAME}_REGS->CAN_NDAT1 = (1UL << rxgi);
        }
        else
        {
            ${CAN_INSTANCE_NAME}_REGS->CAN_NDAT2 = (1UL << (rxgi - 32U));
        }
        if (${CAN_INSTANCE_NAME?lower_case}CallbackObj[CAN_MSG_ATTR_RX_BUFFER].callback != NULL)
        {
            ${CAN_INSTANCE_NAME?lower_case}CallbackObj[CAN_MSG_ATTR_RX_BUFFER].callback(${CAN_INSTANCE_NAME?lower_case}CallbackObj[CAN_MSG_ATTR_RX_BUFFER].context);
        }
    }
</#if>

<#if TX_USE || TXBUF_USE >
    /* TX Completed */
    if ((ir & CAN_IR_TC_Msk) != 0U)
    {
        ${CAN_INSTANCE_NAME}_REGS->CAN_IR = CAN_IR_TC_Msk;
        ${CAN_INSTANCE_NAME}_REGS->CAN_IE &= (~CAN_IE_TCE_Msk);
        for (bufferIndex = 0U; bufferIndex < (${CAN_INSTANCE_NAME}_TX_FIFO_BUFFER_SIZE/${CAN_INSTANCE_NAME}_TX_FIFO_BUFFER_ELEMENT_SIZE); bufferIndex++)
        {
            uint32_t txbufferMask = (1UL << ((uint32_t)bufferIndex & 0x1FU));
            testCondition = ((${CAN_INSTANCE_NAME}_REGS->CAN_TXBTO & txbufferMask) != 0U);
            testCondition = ((${CAN_INSTANCE_NAME}_REGS->CAN_TXBTIE & txbufferMask) != 0U) && testCondition;
            if (testCondition)
            {
                ${CAN_INSTANCE_NAME}_REGS->CAN_TXBTIE &= ~txbufferMask;
                <#if TXBUF_USE>
                if (0U != (${CAN_INSTANCE_NAME?lower_case}Obj.txBufferIndex & txbufferMask))
                {
                    ${CAN_INSTANCE_NAME?lower_case}Obj.txBufferIndex &= (~txbufferMask);
                }
                </#if>
            }
        }
        if (${CAN_INSTANCE_NAME?lower_case}CallbackObj[CAN_CALLBACK_TX_INDEX].callback != NULL)
        {
            ${CAN_INSTANCE_NAME?lower_case}CallbackObj[CAN_CALLBACK_TX_INDEX].callback(${CAN_INSTANCE_NAME?lower_case}CallbackObj[CAN_CALLBACK_TX_INDEX].context);
        }
    }

    /* TX FIFO is empty */
    if ((ir & CAN_IR_TFE_Msk) != 0U)
    {
        ${CAN_INSTANCE_NAME}_REGS->CAN_IR = CAN_IR_TFE_Msk;
        uint8_t getIndex = (uint8_t)((${CAN_INSTANCE_NAME}_REGS->CAN_TXFQS & CAN_TXFQS_TFGI_Msk) >> CAN_TXFQS_TFGI_Pos);
        uint8_t putIndex = (uint8_t)((${CAN_INSTANCE_NAME}_REGS->CAN_TXFQS & CAN_TXFQS_TFQPI_Msk) >> CAN_TXFQS_TFQPI_Pos);
        uint8_t fifoIndex = getIndex;
        while(true)
        {
            <#if TXBUF_USE>
            if (fifoIndex >= (${TX_BUFFER_ELEMENTS}U + ${TX_FIFO_ELEMENTS}U))
            {
                fifoIndex = ${TX_BUFFER_ELEMENTS}U;
            }
            </#if>
            if (fifoIndex >= putIndex)
            {
                break;
            }
            <#if TXBUF_USE>
            if (0U != (${CAN_INSTANCE_NAME?lower_case}Obj.txBufferIndex & (1UL << ((fifoIndex + ${TX_BUFFER_ELEMENTS}U) & 0x1FU))))
            {
                ${CAN_INSTANCE_NAME?lower_case}Obj.txBufferIndex &= (~(1UL << ((fifoIndex + ${TX_BUFFER_ELEMENTS}U) & 0x1FU)));
            }
            </#if>
            fifoIndex++;
        }
    }
</#if>
}
</#if>


/*******************************************************************************
 End of File
*/
