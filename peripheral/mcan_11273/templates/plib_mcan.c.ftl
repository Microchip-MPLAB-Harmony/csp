/*******************************************************************************
  Controller Area Network (MCAN) Peripheral Library Source File

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${MCAN_INSTANCE_NAME?lower_case}.c

  Summary:
    MCAN peripheral library interface.

  Description:
    This file defines the interface to the MCAN peripheral library. This
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
#include "plib_${MCAN_INSTANCE_NAME?lower_case}.h"

// *****************************************************************************
// *****************************************************************************
// Global Data
// *****************************************************************************
// *****************************************************************************
#define MCAN_STD_ID_Msk    0x7FF

static MCAN_OBJ ${MCAN_INSTANCE_NAME?lower_case}Obj;
<#if FILTERS_STD?number gt 0>
<#assign numInstance=FILTERS_STD?number>

static const mcan_sidfe_registers_t ${MCAN_INSTANCE_NAME?lower_case}StdFilter[] =
{
    <#list 1..(numInstance) as idx>
    {
        .MCAN_SIDFE_0 = MCAN_SIDFE_0_SFT(${.vars["${MCAN_INSTANCE_NAME}_STD_FILTER${idx}_TYPE"]}) |
                  MCAN_SIDFE_0_SFID1(${.vars["${MCAN_INSTANCE_NAME}_STD_FILTER${idx}_SFID1"]}) |
                  MCAN_SIDFE_0_SFID2(${.vars["${MCAN_INSTANCE_NAME}_STD_FILTER${idx}_SFID2"]}) |
                  MCAN_SIDFE_0_SFEC(${.vars["${MCAN_INSTANCE_NAME}_STD_FILTER${idx}_CONFIG"]})
    },
     </#list>
};
</#if>
<#if FILTERS_EXT?number gt 0>
<#assign numInstance=FILTERS_EXT?number>

static const mcan_xidfe_registers_t ${MCAN_INSTANCE_NAME?lower_case}ExtFilter[] =
{
    <#list 1..(numInstance) as idx>
    {
        .MCAN_XIDFE_0 = MCAN_XIDFE_0_EFID1(${.vars["${MCAN_INSTANCE_NAME}_EXT_FILTER${idx}_EFID1"]}) | MCAN_XIDFE_0_EFEC(${.vars["${MCAN_INSTANCE_NAME}_EXT_FILTER${idx}_CONFIG"]}),
        .MCAN_XIDFE_1 = MCAN_XIDFE_1_EFID2(${.vars["${MCAN_INSTANCE_NAME}_EXT_FILTER${idx}_EFID2"]}) | MCAN_XIDFE_1_EFT(${.vars["${MCAN_INSTANCE_NAME}_EXT_FILTER${idx}_TYPE"]}),
    },
     </#list>
};
</#if>

/******************************************************************************
Local Functions
******************************************************************************/

<#if MCAN_OPMODE == "CAN FD">
static void MCANLengthToDlcGet(uint8_t length, uint8_t *dlc)
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
static uint8_t MCANDlcToLengthGet(uint8_t dlc)
{
    uint8_t msgLength[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 12, 16, 20, 24, 32, 48, 64};
    return msgLength[dlc];
}

// *****************************************************************************
// *****************************************************************************
// ${MCAN_INSTANCE_NAME} PLib Interface Routines
// *****************************************************************************
// *****************************************************************************
// *****************************************************************************
/* Function:
    void ${MCAN_INSTANCE_NAME}_Initialize(void)

   Summary:
    Initializes given instance of the MCAN peripheral.

   Precondition:
    None.

   Parameters:
    None.

   Returns:
    None
*/
void ${MCAN_INSTANCE_NAME}_Initialize(void)
{
    /* Start MCAN initialization */
    ${MCAN_INSTANCE_NAME}_REGS->MCAN_CCCR = MCAN_CCCR_INIT_ENABLED;
    while ((${MCAN_INSTANCE_NAME}_REGS->MCAN_CCCR & MCAN_CCCR_INIT_Msk) != MCAN_CCCR_INIT_Msk);

    /* Set CCE to unlock the configuration registers */
    ${MCAN_INSTANCE_NAME}_REGS->MCAN_CCCR |= MCAN_CCCR_CCE_Msk;

<#if MCAN_OPMODE == "CAN FD">
<#if MCAN_REVISION_A_ENABLE == true>
    /* Set Fast Bit Timing and Prescaler Register */
    ${MCAN_INSTANCE_NAME}_REGS->MCAN_FBTP = MCAN_FBTP_FTSEG2(${DBTP_DTSEG2}) | MCAN_FBTP_FTSEG1(${DBTP_DTSEG1}) | MCAN_FBTP_FBRP(${DBTP_DBRP}) | MCAN_FBTP_FSJW(${DBTP_DSJW});

<#else>
    /* Set Data Bit Timing and Prescaler Register */
    ${MCAN_INSTANCE_NAME}_REGS->MCAN_DBTP = MCAN_DBTP_DTSEG2(${DBTP_DTSEG2}) | MCAN_DBTP_DTSEG1(${DBTP_DTSEG1}) | MCAN_DBTP_DBRP(${DBTP_DBRP}) | MCAN_DBTP_DSJW(${DBTP_DSJW});

</#if>
</#if>
<#if MCAN_REVISION_A_ENABLE == true>
    /* Set Bit timing and Prescaler Register */
    ${MCAN_INSTANCE_NAME}_REGS->MCAN_BTP  = MCAN_BTP_TSEG2(${NBTP_NTSEG2}) | MCAN_BTP_TSEG1(${NBTP_NTSEG1}) | MCAN_BTP_BRP(${NBTP_NBRP}) | MCAN_BTP_SJW(${NBTP_NSJW});
<#else>
    /* Set Nominal Bit timing and Prescaler Register */
    ${MCAN_INSTANCE_NAME}_REGS->MCAN_NBTP  = MCAN_NBTP_NTSEG2(${NBTP_NTSEG2}) | MCAN_NBTP_NTSEG1(${NBTP_NTSEG1}) | MCAN_NBTP_NBRP(${NBTP_NBRP}) | MCAN_NBTP_NSJW(${NBTP_NSJW});
</#if>

<#if RXF0_USE || RXF1_USE || RXBUF_USE>
  <#if MCAN_OPMODE == "CAN FD">
    /* Receive Buffer / FIFO Element Size Configuration Register */
    ${MCAN_INSTANCE_NAME}_REGS->MCAN_RXESC = 0 <#if RXF0_USE> | MCAN_RXESC_F0DS(${RXF0_BYTES_CFG!0})</#if><#if RXF1_USE> | MCAN_RXESC_F1DS(${RXF1_BYTES_CFG!0})</#if><#if RXBUF_USE> | MCAN_RXESC_RBDS(${RX_BUFFER_BYTES_CFG!0})</#if>;
  </#if>
</#if>
<#if RXBUF_USE>
    ${MCAN_INSTANCE_NAME}_REGS->MCAN_NDAT1 = MCAN_NDAT1_Msk;
    ${MCAN_INSTANCE_NAME}_REGS->MCAN_NDAT2 = MCAN_NDAT2_Msk;

</#if>
<#if TX_USE || TXBUF_USE>
  <#if MCAN_OPMODE == "CAN FD">
    /* Transmit Buffer/FIFO Element Size Configuration Register */
    ${MCAN_INSTANCE_NAME}_REGS->MCAN_TXESC = MCAN_TXESC_TBDS(${TX_FIFO_BYTES_CFG});
  </#if>
</#if>

    /* Global Filter Configuration Register */
    ${MCAN_INSTANCE_NAME}_REGS->MCAN_GFC = ${FILTERS_STD_NOMATCH} | ${FILTERS_EXT_NOMATCH}<#if FILTERS_STD_REJECT> | MCAN_GFC_RRFS_REJECT</#if><#if FILTERS_EXT_REJECT> | MCAN_GFC_RRFE_REJECT</#if>;
<#if FILTERS_EXT?number gt 0>

    /* Extended ID AND Mask Register */
    ${MCAN_INSTANCE_NAME}_REGS->MCAN_XIDAM = MCAN_XIDAM_Msk;
</#if>

    /* Timestamp Counter Configuration Register */
    ${MCAN_INSTANCE_NAME}_REGS->MCAN_TSCC = ${TIMESTAMP_MODE} | MCAN_TSCC_TCP(${TIMESTAMP_PRESCALER});
<#if MCAN_TIMEOUT>

    /* Timeout Counter Configuration Register */
    ${MCAN_INSTANCE_NAME}_REGS->MCAN_TOCC = ${TIMEOUT_SELECT} | MCAN_TOCC_ETOC_TOS_CONTROLLED | MCAN_TOCC_TOP(${TIMEOUT_COUNT});
</#if>

    /* Set the operation mode */
<#if MCAN_REVISION_A_ENABLE == true>
    ${MCAN_INSTANCE_NAME}_REGS->MCAN_CCCR = MCAN_CCCR_INIT_DISABLED${(MCAN_OPMODE == "CAN FD")?then(' | MCAN_CCCR_CME_FD | MCAN_CCCR_CMR_FD_BITRATE_SWITCH','')}<#if TX_PAUSE!false> | MCAN_CCCR_TXP_Msk</#if>;
<#else>
    ${MCAN_INSTANCE_NAME}_REGS->MCAN_CCCR = MCAN_CCCR_INIT_DISABLED${(MCAN_OPMODE == "CAN FD")?then(' | MCAN_CCCR_FDOE_ENABLED | MCAN_CCCR_BRSE_ENABLED','')}<#if TX_PAUSE!false> | MCAN_CCCR_TXP_Msk</#if>;
</#if>
    while ((${MCAN_INSTANCE_NAME}_REGS->MCAN_CCCR & MCAN_CCCR_INIT_Msk) == MCAN_CCCR_INIT_Msk);
<#if INTERRUPT_MODE == true>

    /* Select interrupt line */
    ${MCAN_INSTANCE_NAME}_REGS->MCAN_ILS = 0x0;

    /* Enable interrupt line */
    ${MCAN_INSTANCE_NAME}_REGS->MCAN_ILE = MCAN_ILE_EINT0_Msk;

    /* Enable MCAN interrupts */
    ${MCAN_INSTANCE_NAME}_REGS->MCAN_IE = MCAN_IE_BOE_Msk;

    // Initialize the MCAN PLib Object
    ${MCAN_INSTANCE_NAME?lower_case}Obj.txBufferIndex = 0;
    ${MCAN_INSTANCE_NAME?lower_case}Obj.rxId = 0;
    ${MCAN_INSTANCE_NAME?lower_case}Obj.rxBuffer = 0;
    ${MCAN_INSTANCE_NAME?lower_case}Obj.rxsize = 0;
    ${MCAN_INSTANCE_NAME?lower_case}Obj.state = MCAN_STATE_IDLE;
</#if>
    memset((void*)&${MCAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig, 0x00, sizeof(MCAN_MSG_RAM_CONFIG));
}

// *****************************************************************************
/* Function:
    bool ${MCAN_INSTANCE_NAME}_MessageTransmit(uint32_t id, uint8_t length, uint8_t* data, MCAN_MODE mode, MCAN_MSG_TX_ATTRIBUTE msgAttr)

   Summary:
    Transmits a message into CAN bus.

   Precondition:
    ${MCAN_INSTANCE_NAME}_Initialize must have been called for the associated MCAN instance.

   Parameters:
    id      - 11-bit / 29-bit identifier (ID).
    length  - length of data buffer in number of bytes.
    data    - pointer to source data buffer
    mode    - MCAN mode Classic CAN or CAN FD without BRS or CAN FD with BRS
    msgAttr - Data Frame or Remote frame using Tx FIFO or Tx Buffer

   Returns:
    Request status.
    true  - Request was successful.
    false - Request has failed.
*/
bool ${MCAN_INSTANCE_NAME}_MessageTransmit(uint32_t id, uint8_t length, uint8_t* data, MCAN_MODE mode, MCAN_MSG_TX_ATTRIBUTE msgAttr)
{
<#if MCAN_OPMODE =="CAN FD">
    uint8_t dlc = 0;
</#if>
<#if TXBUF_USE>
    uint8_t bufferIndex = 0;
</#if>
    uint8_t tfqpi = 0;
<#if TX_USE || TXBUF_USE>
    mcan_txbe_registers_t *fifo = NULL;
</#if>

    switch (msgAttr)
    {
<#if TXBUF_USE>
        case MCAN_MSG_ATTR_TX_BUFFER_DATA_FRAME:
        case MCAN_MSG_ATTR_TX_BUFFER_RTR_FRAME:
            for (bufferIndex = 0; bufferIndex < ${TX_BUFFER_ELEMENTS}; bufferIndex++)
            {
                if ((${MCAN_INSTANCE_NAME?lower_case}Obj.txBufferIndex & (1 << (bufferIndex & 0x1F))) == 0)
                {
                    ${MCAN_INSTANCE_NAME?lower_case}Obj.txBufferIndex |= (1 << (bufferIndex & 0x1F));
                    tfqpi = bufferIndex;
                    break;
                }
            }
            if(bufferIndex == ${TX_BUFFER_ELEMENTS})
            {
                /* The Tx buffers are full */
                return false;
            }
            fifo = (mcan_txbe_registers_t *) ((uint8_t *)${MCAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.txBuffersAddress + tfqpi * ${MCAN_INSTANCE_NAME}_TX_FIFO_BUFFER_ELEMENT_SIZE);
            break;
</#if>
<#if TX_USE>
        case MCAN_MSG_ATTR_TX_FIFO_DATA_FRAME:
        case MCAN_MSG_ATTR_TX_FIFO_RTR_FRAME:
            if (${MCAN_INSTANCE_NAME}_REGS->MCAN_TXFQS & MCAN_TXFQS_TFQF_Msk)
            {
                /* The FIFO is full */
                return false;
            }
            tfqpi = (uint8_t)((${MCAN_INSTANCE_NAME}_REGS->MCAN_TXFQS & MCAN_TXFQS_TFQPI_Msk) >> MCAN_TXFQS_TFQPI_Pos);
<#if TXBUF_USE>
            ${MCAN_INSTANCE_NAME?lower_case}Obj.txBufferIndex |= (1 << ((tfqpi + ${TX_BUFFER_ELEMENTS}) & 0x1F));
</#if>
            fifo = (mcan_txbe_registers_t *) ((uint8_t *)${MCAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.txBuffersAddress + tfqpi * ${MCAN_INSTANCE_NAME}_TX_FIFO_BUFFER_ELEMENT_SIZE);
            break;
</#if>
        default:
            /* Invalid Message Attribute */
            return false;
    }

    /* If the id is longer than 11 bits, it is considered as extended identifier */
    if (id > MCAN_STD_ID_Msk)
    {
        /* An extended identifier is stored into ID */
        fifo->MCAN_TXBE_0 = (id & MCAN_TXBE_0_ID_Msk) | MCAN_TXBE_0_XTD_Msk;
    }
    else
    {
        /* A standard identifier is stored into ID[28:18] */
        fifo->MCAN_TXBE_0 = id << 18;
    }
<#if MCAN_OPMODE =="CAN FD">
    if (length > 64)
        length = 64;

    MCANLengthToDlcGet(length, &dlc);

    fifo->MCAN_TXBE_1 = MCAN_TXBE_1_DLC(dlc);

<#if MCAN_REVISION_A_ENABLE == false>
    if(mode == MCAN_MODE_FD_WITH_BRS)
    {
        fifo->MCAN_TXBE_1 |= MCAN_TXBE_1_FDF_Msk | MCAN_TXBE_1_BRS_Msk;
    }
    else if (mode == MCAN_MODE_FD_WITHOUT_BRS)
    {
        fifo->MCAN_TXBE_1 |= MCAN_TXBE_1_FDF_Msk;
    }
</#if>
<#else>

    /* Limit length */
    if (length > 8)
        length = 8;
    fifo->MCAN_TXBE_1 = MCAN_TXBE_1_DLC(length);
</#if>

    if (msgAttr == MCAN_MSG_ATTR_TX_BUFFER_DATA_FRAME || msgAttr == MCAN_MSG_ATTR_TX_FIFO_DATA_FRAME)
    {
        /* copy the data into the payload */
        memcpy((uint8_t *)&fifo->MCAN_TXBE_DATA, data, length);
    }
    else if (msgAttr == MCAN_MSG_ATTR_TX_BUFFER_RTR_FRAME || msgAttr == MCAN_MSG_ATTR_TX_FIFO_RTR_FRAME)
    {
        fifo->MCAN_TXBE_0 |= MCAN_TXBE_0_RTR_Msk;
    }
<#if INTERRUPT_MODE == true>

    ${MCAN_INSTANCE_NAME}_REGS->MCAN_TXBTIE = 1U << tfqpi;
    ${MCAN_INSTANCE_NAME?lower_case}Obj.state = MCAN_STATE_TRANSFER_TRANSMIT;
</#if>

    /* request the transmit */
    ${MCAN_INSTANCE_NAME}_REGS->MCAN_TXBAR = 1U << tfqpi;

<#if INTERRUPT_MODE == true>
    ${MCAN_INSTANCE_NAME}_REGS->MCAN_IE |= MCAN_IE_TCE_Msk;
</#if>
<#if TXBUF_USE && INTERRUPT_MODE == false>
    for (bufferIndex = 0; bufferIndex < (${MCAN_INSTANCE_NAME}_TX_FIFO_BUFFER_SIZE/${MCAN_INSTANCE_NAME}_TX_FIFO_BUFFER_ELEMENT_SIZE); bufferIndex++)
    {
        if (${MCAN_INSTANCE_NAME}_REGS->MCAN_TXBTO & (1 << (bufferIndex & 0x1F)))
        {
            if (0 != (${MCAN_INSTANCE_NAME?lower_case}Obj.txBufferIndex & (1 << (bufferIndex & 0x1F))))
            {
                ${MCAN_INSTANCE_NAME?lower_case}Obj.txBufferIndex &= (~(1 << (bufferIndex & 0x1F)));
            }
        }
    }
</#if>
    return true;
}

// *****************************************************************************
/* Function:
    bool ${MCAN_INSTANCE_NAME}_MessageReceive(uint32_t *id, uint8_t *length, uint8_t *data, MCAN_MSG_RX_ATTRIBUTE msgAttr)

   Summary:
    Receives a message from CAN bus.

   Precondition:
    ${MCAN_INSTANCE_NAME}_Initialize must have been called for the associated MCAN instance.

   Parameters:
    id      - Pointer to 11-bit / 29-bit identifier (ID) to be received.
    length  - Pointer to data length in number of bytes to be received.
    data    - pointer to destination data buffer
    msgAttr - Message to be read from Rx FIFO0 or Rx FIFO1 or Rx Buffer

   Returns:
    Request status.
    true  - Request was successful.
    false - Request has failed.
*/
bool ${MCAN_INSTANCE_NAME}_MessageReceive(uint32_t *id, uint8_t *length, uint8_t *data, MCAN_MSG_RX_ATTRIBUTE msgAttr)
{
<#if INTERRUPT_MODE == false>
    uint8_t msgLength = 0;
    uint8_t rxgi = 0;
<#if RXBUF_USE>
    mcan_rxbe_registers_t *rxbeFifo = NULL;
</#if>
<#if RXF0_USE>
    mcan_rxf0e_registers_t *rxf0eFifo = NULL;
</#if>
<#if RXF1_USE>
    mcan_rxf1e_registers_t *rxf1eFifo = NULL;
</#if>
<#else>
    uint32_t rxInterrupt = 0;
</#if>
    bool status = false;

    switch (msgAttr)
    {
<#if RXBUF_USE>
        case MCAN_MSG_ATTR_RX_BUFFER:
<#if INTERRUPT_MODE == false>
            /* Check and return false if nothing to be read */
            if ((${MCAN_INSTANCE_NAME}_REGS->MCAN_NDAT1 == 0) && (${MCAN_INSTANCE_NAME}_REGS->MCAN_NDAT2 == 0))
            {
                return status;
            }
            /* Read data from the Rx Buffer */
            if (${MCAN_INSTANCE_NAME}_REGS->MCAN_NDAT1 != 0)
            {
                for (rxgi = 0; rxgi <= 0x1F; rxgi++)
                {
                    if ((${MCAN_INSTANCE_NAME}_REGS->MCAN_NDAT1 & (1 << rxgi)) == (1 << rxgi))
                        break;
                }
            }
            else
            {
                for (rxgi = 0; rxgi <= 0x1F; rxgi++)
                {
                    if ((${MCAN_INSTANCE_NAME}_REGS->MCAN_NDAT2 & (1 << rxgi)) == (1 << rxgi))
                    {
                        rxgi = rxgi + 32;
                        break;
                    }
                }
            }
            rxbeFifo = (mcan_rxbe_registers_t *) ((uint8_t *)${MCAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.rxBuffersAddress + rxgi * ${MCAN_INSTANCE_NAME}_RX_BUFFER_ELEMENT_SIZE);

            /* Get received identifier */
            if (rxbeFifo->MCAN_RXBE_0 & MCAN_RXBE_0_XTD_Msk)
            {
                *id = rxbeFifo->MCAN_RXBE_0 & MCAN_RXBE_0_ID_Msk;
            }
            else
            {
                *id = (rxbeFifo->MCAN_RXBE_0 >> 18) & MCAN_STD_ID_Msk;
            }

            /* Get received data length */
            msgLength = MCANDlcToLengthGet(((rxbeFifo->MCAN_RXBE_1 & MCAN_RXBE_1_DLC_Msk) >> MCAN_RXBE_1_DLC_Pos));

            /* Copy data to user buffer */
            memcpy(data, (uint8_t *)&rxbeFifo->MCAN_RXBE_DATA, msgLength);
            *length = msgLength;

            /* Clear new data flag */
            if (rxgi < 32)
            {
                ${MCAN_INSTANCE_NAME}_REGS->MCAN_NDAT1 = (1 << rxgi);
            }
            else
            {
                ${MCAN_INSTANCE_NAME}_REGS->MCAN_NDAT2 = (1 << (rxgi - 32));
            }
<#else>
            rxInterrupt = MCAN_IE_DRXE_Msk;
</#if>
            status = true;
            break;
</#if>
<#if RXF0_USE>
        case MCAN_MSG_ATTR_RX_FIFO0:
<#if INTERRUPT_MODE == false>
            /* Check and return false if nothing to be read */
            if ((${MCAN_INSTANCE_NAME}_REGS->MCAN_RXF0S & MCAN_RXF0S_F0FL_Msk) == 0)
            {
                return status;
            }
            /* Read data from the Rx FIFO0 */
            rxgi = (uint8_t)((${MCAN_INSTANCE_NAME}_REGS->MCAN_RXF0S & MCAN_RXF0S_F0GI_Msk) >> MCAN_RXF0S_F0GI_Pos);
            rxf0eFifo = (mcan_rxf0e_registers_t *) ((uint8_t *)${MCAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.rxFIFO0Address + rxgi * ${MCAN_INSTANCE_NAME}_RX_FIFO0_ELEMENT_SIZE);

            /* Get received identifier */
            if (rxf0eFifo->MCAN_RXF0E_0 & MCAN_RXF0E_0_XTD_Msk)
            {
                *id = rxf0eFifo->MCAN_RXF0E_0 & MCAN_RXF0E_0_ID_Msk;
            }
            else
            {
                *id = (rxf0eFifo->MCAN_RXF0E_0 >> 18) & MCAN_STD_ID_Msk;
            }

            /* Get received data length */
            msgLength = MCANDlcToLengthGet(((rxf0eFifo->MCAN_RXF0E_1 & MCAN_RXF0E_1_DLC_Msk) >> MCAN_RXF0E_1_DLC_Pos));

            /* Copy data to user buffer */
            memcpy(data, (uint8_t *)&rxf0eFifo->MCAN_RXF0E_DATA, msgLength);
            *length = msgLength;

            /* Ack the fifo position */
            ${MCAN_INSTANCE_NAME}_REGS->MCAN_RXF0A = MCAN_RXF0A_F0AI(rxgi);
<#else>
            rxInterrupt = MCAN_IE_RF0NE_Msk;
</#if>
            status = true;
            break;
</#if>
<#if RXF1_USE>
        case MCAN_MSG_ATTR_RX_FIFO1:
<#if INTERRUPT_MODE == false>
            /* Check and return false if nothing to be read */
            if ((${MCAN_INSTANCE_NAME}_REGS->MCAN_RXF1S & MCAN_RXF1S_F1FL_Msk) == 0)
            {
                return status;
            }
            /* Read data from the Rx FIFO1 */
            rxgi = (uint8_t)((${MCAN_INSTANCE_NAME}_REGS->MCAN_RXF1S & MCAN_RXF1S_F1GI_Msk) >> MCAN_RXF1S_F1GI_Pos);
            rxf1eFifo = (mcan_rxf1e_registers_t *) ((uint8_t *)${MCAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.rxFIFO1Address + rxgi * ${MCAN_INSTANCE_NAME}_RX_FIFO1_ELEMENT_SIZE);

            /* Get received identifier */
            if (rxf1eFifo->MCAN_RXF1E_0 & MCAN_RXF1E_0_XTD_Msk)
            {
                *id = rxf1eFifo->MCAN_RXF1E_0 & MCAN_RXF1E_0_ID_Msk;
            }
            else
            {
                *id = (rxf1eFifo->MCAN_RXF1E_0 >> 18) & MCAN_STD_ID_Msk;
            }

            /* Get received data length */
            msgLength = MCANDlcToLengthGet(((rxf1eFifo->MCAN_RXF1E_1 & MCAN_RXF1E_1_DLC_Msk) >> MCAN_RXF1E_1_DLC_Pos));

            /* Copy data to user buffer */
            memcpy(data, (uint8_t *)&rxf1eFifo->MCAN_RXF1E_DATA, msgLength);
            *length = msgLength;

            /* Ack the fifo position */
            ${MCAN_INSTANCE_NAME}_REGS->MCAN_RXF1A = MCAN_RXF1A_F1AI(rxgi);
<#else>
            rxInterrupt = MCAN_IE_RF1NE_Msk;
</#if>
            status = true;
            break;
</#if>
        default:
            return status;
    }
<#if INTERRUPT_MODE == true>
    ${MCAN_INSTANCE_NAME?lower_case}Obj.state = MCAN_STATE_TRANSFER_RECEIVE;
    ${MCAN_INSTANCE_NAME?lower_case}Obj.rxId = id;
    ${MCAN_INSTANCE_NAME?lower_case}Obj.rxBuffer = data;
    ${MCAN_INSTANCE_NAME?lower_case}Obj.rxsize = length;
    ${MCAN_INSTANCE_NAME}_REGS->MCAN_IE |= rxInterrupt;
</#if>
    return status;
}

// *****************************************************************************
/* Function:
    MCAN_ERROR ${MCAN_INSTANCE_NAME}_ErrorGet(void)

   Summary:
    Returns the error during transfer.

   Precondition:
    ${MCAN_INSTANCE_NAME}_Initialize must have been called for the associated MCAN instance.

   Parameters:
    None.

   Returns:
    Error during transfer.
*/
MCAN_ERROR ${MCAN_INSTANCE_NAME}_ErrorGet(void)
{
    MCAN_ERROR error;
    uint32_t   errorStatus = ${MCAN_INSTANCE_NAME}_REGS->MCAN_PSR;

    error = (MCAN_ERROR) ((errorStatus & MCAN_PSR_LEC_Msk) | (errorStatus & MCAN_PSR_EP_Msk) | (errorStatus & MCAN_PSR_EW_Msk)
            | (errorStatus & MCAN_PSR_BO_Msk) | (errorStatus & MCAN_PSR_DLEC_Msk) | (errorStatus & MCAN_PSR_PXE_Msk));

    if ((${MCAN_INSTANCE_NAME}_REGS->MCAN_CCCR & MCAN_CCCR_INIT_Msk) == MCAN_CCCR_INIT_Msk)
    {
        ${MCAN_INSTANCE_NAME}_REGS->MCAN_CCCR |= MCAN_CCCR_CCE_Msk;
<#if MCAN_REVISION_A_ENABLE == true>
        ${MCAN_INSTANCE_NAME}_REGS->MCAN_CCCR = MCAN_CCCR_INIT_DISABLED${(MCAN_OPMODE == "CAN FD")?then(' | MCAN_CCCR_CME_FD | MCAN_CCCR_CMR_FD_BITRATE_SWITCH','')}<#if TX_PAUSE!false> | MCAN_CCCR_TXP_Msk</#if>;
<#else>
        ${MCAN_INSTANCE_NAME}_REGS->MCAN_CCCR = MCAN_CCCR_INIT_DISABLED${(MCAN_OPMODE == "CAN FD")?then(' | MCAN_CCCR_FDOE_ENABLED | MCAN_CCCR_BRSE_ENABLED','')}<#if TX_PAUSE!false> | MCAN_CCCR_TXP_Msk</#if>;
</#if>
        while ((${MCAN_INSTANCE_NAME}_REGS->MCAN_CCCR & MCAN_CCCR_INIT_Msk) == MCAN_CCCR_INIT_Msk);
    }

    return error;
}

// *****************************************************************************
/* Function:
    bool ${MCAN_INSTANCE_NAME}_InterruptGet(MCAN_INTERRUPT_MASK interruptMask)

   Summary:
    Returns the Interrupt status.

   Precondition:
    ${MCAN_INSTANCE_NAME}_Initialize must have been called for the associated MCAN instance.

   Parameters:
    interruptMask - Interrupt source number

   Returns:
    true - Requested interrupt is occurred.
    false - Requested interrupt is not occurred.
*/
bool ${MCAN_INSTANCE_NAME}_InterruptGet(MCAN_INTERRUPT_MASK interruptMask)
{
    return ((${MCAN_INSTANCE_NAME}_REGS->MCAN_IR & interruptMask) != 0x0);
}

// *****************************************************************************
/* Function:
    void ${MCAN_INSTANCE_NAME}_InterruptClear(MCAN_INTERRUPT_MASK interruptMask)

   Summary:
    Clears Interrupt status.

   Precondition:
    ${MCAN_INSTANCE_NAME}_Initialize must have been called for the associated MCAN instance.

   Parameters:
    interruptMask - Interrupt to be cleared

   Returns:
    None
*/
void ${MCAN_INSTANCE_NAME}_InterruptClear(MCAN_INTERRUPT_MASK interruptMask)
{
    ${MCAN_INSTANCE_NAME}_REGS->MCAN_IR = interruptMask;
}

// *****************************************************************************
/* Function:
    void ${MCAN_INSTANCE_NAME}_MessageRAMConfigSet(uint8_t *msgRAMConfigBaseAddress)

   Summary:
    Set the Message RAM Configuration.

   Precondition:
    ${MCAN_INSTANCE_NAME}_Initialize must have been called for the associated MCAN instance.

   Parameters:
    msgRAMConfigBaseAddress - Pointer to application allocated buffer base address.
                              Application must allocate buffer from non-cached
                              contiguous memory and buffer size must be
                              ${MCAN_INSTANCE_NAME}_MESSAGE_RAM_CONFIG_SIZE

   Returns:
    None
*/
void ${MCAN_INSTANCE_NAME}_MessageRAMConfigSet(uint8_t *msgRAMConfigBaseAddress)
{
    uint32_t offset = 0;

    memset((void*)msgRAMConfigBaseAddress, 0x00, ${MCAN_INSTANCE_NAME}_MESSAGE_RAM_CONFIG_SIZE);

    /* Set MCAN CCCR Init for Message RAM Configuration */
    ${MCAN_INSTANCE_NAME}_REGS->MCAN_CCCR = MCAN_CCCR_INIT_ENABLED;
    while ((${MCAN_INSTANCE_NAME}_REGS->MCAN_CCCR & MCAN_CCCR_INIT_Msk) != MCAN_CCCR_INIT_Msk);

    /* Set CCE to unlock the configuration registers */
    ${MCAN_INSTANCE_NAME}_REGS->MCAN_CCCR |= MCAN_CCCR_CCE_Msk;

<#if RXF0_USE>
    ${MCAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.rxFIFO0Address = (mcan_rxf0e_registers_t *)msgRAMConfigBaseAddress;
    offset = ${MCAN_INSTANCE_NAME}_RX_FIFO0_SIZE;
    /* Receive FIFO 0 Configuration Register */
    ${MCAN_INSTANCE_NAME}_REGS->MCAN_RXF0C = MCAN_RXF0C_F0S(${RXF0_ELEMENTS}) | MCAN_RXF0C_F0WM(${RXF0_WATERMARK})<#if RXF0_OVERWRITE> | MCAN_RXF0C_F0OM_Msk</#if> |
            MCAN_RXF0C_F0SA(((uint32_t)${MCAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.rxFIFO0Address >> 2));

</#if>
<#if RXF1_USE>
    ${MCAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.rxFIFO1Address = (mcan_rxf1e_registers_t *)(msgRAMConfigBaseAddress + offset);
    offset += ${MCAN_INSTANCE_NAME}_RX_FIFO1_SIZE;
    /* Receive FIFO 1 Configuration Register */
    ${MCAN_INSTANCE_NAME}_REGS->MCAN_RXF1C = MCAN_RXF1C_F1S(${RXF1_ELEMENTS}) | MCAN_RXF1C_F1WM(${RXF1_WATERMARK})<#if RXF1_OVERWRITE> | MCAN_RXF1C_F1OM_Msk</#if> |
            MCAN_RXF1C_F1SA(((uint32_t)${MCAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.rxFIFO1Address >> 2));

</#if>
<#if RXBUF_USE>
    ${MCAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.rxBuffersAddress = (mcan_rxbe_registers_t *)(msgRAMConfigBaseAddress + offset);
    offset += ${MCAN_INSTANCE_NAME}_RX_BUFFER_SIZE;
    ${MCAN_INSTANCE_NAME}_REGS->MCAN_RXBC = MCAN_RXBC_RBSA(((uint32_t)${MCAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.rxBuffersAddress >> 2));

</#if>
<#if TX_USE || TXBUF_USE>
    ${MCAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.txBuffersAddress = (mcan_txbe_registers_t *)(msgRAMConfigBaseAddress + offset);
    offset += ${MCAN_INSTANCE_NAME}_TX_FIFO_BUFFER_SIZE;
    /* Transmit Buffer/FIFO Configuration Register */
    ${MCAN_INSTANCE_NAME}_REGS->MCAN_TXBC = MCAN_TXBC_TFQS(${TX_FIFO_ELEMENTS})<#if TXBUF_USE> | MCAN_TXBC_NDTB(${TX_BUFFER_ELEMENTS})</#if> |
            MCAN_TXBC_TBSA(((uint32_t)${MCAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.txBuffersAddress >> 2));

    ${MCAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.txEventFIFOAddress =  (mcan_txefe_registers_t *)(msgRAMConfigBaseAddress + offset);
    offset += ${MCAN_INSTANCE_NAME}_TX_EVENT_FIFO_SIZE;
    /* Transmit Event FIFO Configuration Register */
    ${MCAN_INSTANCE_NAME}_REGS->MCAN_TXEFC = MCAN_TXEFC_EFWM(${TX_FIFO_WATERMARK}) | MCAN_TXEFC_EFS(${TX_FIFO_ELEMENTS}) |
            MCAN_TXEFC_EFSA(((uint32_t)${MCAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.txEventFIFOAddress >> 2));

</#if>
<#if FILTERS_STD?number gt 0>
    ${MCAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.stdMsgIDFilterAddress = (mcan_sidfe_registers_t *)(msgRAMConfigBaseAddress + offset);
    memcpy((void *)${MCAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.stdMsgIDFilterAddress,
           (const void *)${MCAN_INSTANCE_NAME?lower_case}StdFilter,
           ${MCAN_INSTANCE_NAME}_STD_MSG_ID_FILTER_SIZE);
    offset += ${MCAN_INSTANCE_NAME}_STD_MSG_ID_FILTER_SIZE;
    /* Standard ID Filter Configuration Register */
    ${MCAN_INSTANCE_NAME}_REGS->MCAN_SIDFC = MCAN_SIDFC_LSS(${FILTERS_STD}) |
            MCAN_SIDFC_FLSSA(((uint32_t)${MCAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.stdMsgIDFilterAddress >> 2));

</#if>
<#if FILTERS_EXT?number gt 0>
    ${MCAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.extMsgIDFilterAddress = (mcan_xidfe_registers_t *)(msgRAMConfigBaseAddress + offset);
    memcpy((void *)${MCAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.extMsgIDFilterAddress,
           (const void *)${MCAN_INSTANCE_NAME?lower_case}ExtFilter,
           ${MCAN_INSTANCE_NAME}_EXT_MSG_ID_FILTER_SIZE);
    /* Extended ID Filter Configuration Register */
    ${MCAN_INSTANCE_NAME}_REGS->MCAN_XIDFC = MCAN_XIDFC_LSE(${FILTERS_EXT}) |
            MCAN_XIDFC_FLESA(((uint32_t)${MCAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.extMsgIDFilterAddress >> 2));

</#if>
    /* Set 16-bit MSB of ${MCAN_INSTANCE_NAME?lower_case} base address */
<#if MCAN_SFR_CAN_ENABLE_VALUE == 1>
  <#if MCAN_INSTANCE_NAME?lower_case == "mcan0">
    SFR_REGS->SFR_CAN = (SFR_REGS->SFR_CAN & ~SFR_CAN_EXT_MEM_CAN0_ADDR_Msk)
                       | SFR_CAN_EXT_MEM_CAN0_ADDR(((uint32_t)msgRAMConfigBaseAddress >> 16));
  <#else>
    SFR_REGS->SFR_CAN = (SFR_REGS->SFR_CAN & ~SFR_CAN_EXT_MEM_CAN1_ADDR_Msk)
                       | SFR_CAN_EXT_MEM_CAN1_ADDR(((uint32_t)msgRAMConfigBaseAddress >> 16));
  </#if>
<#elseif MCAN_SFR_CAN_ENABLE_VALUE == 2>
    SFR_REGS->SFR_CAN[${MCAN_INSTANCE_NAME?lower_case?remove_beginning("mcan")}] =
        (SFR_REGS->SFR_CAN[${MCAN_INSTANCE_NAME?lower_case?remove_beginning("mcan")}] & ~SFR_CAN_EXT_MEM_ADDR_Msk) |
         SFR_CAN_EXT_MEM_ADDR(((uint32_t)msgRAMConfigBaseAddress >> 16));
<#elseif MCAN_MATRIX_CAN_ENABLE == true>
  <#if MCAN_INSTANCE_NAME?lower_case == "mcan0">
    MATRIX_REGS->CCFG_CAN0 = (MATRIX_REGS->CCFG_CAN0 & ~CCFG_CAN0_Msk)
                            | CCFG_CAN0_CAN0DMABA(((uint32_t)msgRAMConfigBaseAddress >> 16));
  <#else>
    MATRIX_REGS->CCFG_SYSIO = (MATRIX_REGS->CCFG_SYSIO & ~CCFG_SYSIO_CAN1DMABA_Msk)
                            | CCFG_SYSIO_CAN1DMABA(((uint32_t)msgRAMConfigBaseAddress >> 16));
  </#if>
</#if>

    /* Complete Message RAM Configuration by clearing MCAN CCCR Init */
<#if MCAN_REVISION_A_ENABLE == true>
    ${MCAN_INSTANCE_NAME}_REGS->MCAN_CCCR = MCAN_CCCR_INIT_DISABLED${(MCAN_OPMODE == "CAN FD")?then(' | MCAN_CCCR_CME_FD | MCAN_CCCR_CMR_FD_BITRATE_SWITCH','')}<#if TX_PAUSE!false> | MCAN_CCCR_TXP_Msk</#if>;
<#else>
    ${MCAN_INSTANCE_NAME}_REGS->MCAN_CCCR = MCAN_CCCR_INIT_DISABLED${(MCAN_OPMODE == "CAN FD")?then(' | MCAN_CCCR_FDOE_ENABLED | MCAN_CCCR_BRSE_ENABLED','')}<#if TX_PAUSE!false> | MCAN_CCCR_TXP_Msk</#if>;
</#if>
    while ((${MCAN_INSTANCE_NAME}_REGS->MCAN_CCCR & MCAN_CCCR_INIT_Msk) == MCAN_CCCR_INIT_Msk);
}

<#if FILTERS_STD?number gt 0>
// *****************************************************************************
/* Function:
    bool ${MCAN_INSTANCE_NAME}_StandardFilterElementSet(uint8_t filterNumber, mcan_sidfe_registers_t *stdMsgIDFilterElement)

   Summary:
    Set a standard filter element configuration.

   Precondition:
    ${MCAN_INSTANCE_NAME}_Initialize and ${MCAN_INSTANCE_NAME}_MessageRAMConfigSet must have been called
    for the associated MCAN instance.

   Parameters:
    filterNumber          - Standard Filter number to be configured.
    stdMsgIDFilterElement - Pointer to Standard Filter Element configuration to be set on specific filterNumber.

   Returns:
    Request status.
    true  - Request was successful.
    false - Request has failed.
*/
bool ${MCAN_INSTANCE_NAME}_StandardFilterElementSet(uint8_t filterNumber, mcan_sidfe_registers_t *stdMsgIDFilterElement)
{
    if ((filterNumber > ${FILTERS_STD}) || (stdMsgIDFilterElement == NULL))
    {
        return false;
    }
    ${MCAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.stdMsgIDFilterAddress[filterNumber - 1].MCAN_SIDFE_0 = stdMsgIDFilterElement->MCAN_SIDFE_0;

    return true;
}

// *****************************************************************************
/* Function:
    bool ${MCAN_INSTANCE_NAME}_StandardFilterElementGet(uint8_t filterNumber, mcan_sidfe_registers_t *stdMsgIDFilterElement)

   Summary:
    Get a standard filter element configuration.

   Precondition:
    ${MCAN_INSTANCE_NAME}_Initialize and ${MCAN_INSTANCE_NAME}_MessageRAMConfigSet must have been called
    for the associated MCAN instance.

   Parameters:
    filterNumber          - Standard Filter number to get filter configuration.
    stdMsgIDFilterElement - Pointer to Standard Filter Element configuration for storing filter configuration.

   Returns:
    Request status.
    true  - Request was successful.
    false - Request has failed.
*/
bool ${MCAN_INSTANCE_NAME}_StandardFilterElementGet(uint8_t filterNumber, mcan_sidfe_registers_t *stdMsgIDFilterElement)
{
    if ((filterNumber > ${FILTERS_STD}) || (stdMsgIDFilterElement == NULL))
    {
        return false;
    }
    stdMsgIDFilterElement->MCAN_SIDFE_0 = ${MCAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.stdMsgIDFilterAddress[filterNumber - 1].MCAN_SIDFE_0;

    return true;
}
</#if>

<#if FILTERS_EXT?number gt 0>
// *****************************************************************************
/* Function:
    bool ${MCAN_INSTANCE_NAME}_ExtendedFilterElementSet(uint8_t filterNumber, mcan_xidfe_registers_t *extMsgIDFilterElement)

   Summary:
    Set a Extended filter element configuration.

   Precondition:
    ${MCAN_INSTANCE_NAME}_Initialize and ${MCAN_INSTANCE_NAME}_MessageRAMConfigSet must have been called
    for the associated MCAN instance.

   Parameters:
    filterNumber          - Extended Filter number to be configured.
    extMsgIDFilterElement - Pointer to Extended Filter Element configuration to be set on specific filterNumber.

   Returns:
    Request status.
    true  - Request was successful.
    false - Request has failed.
*/
bool ${MCAN_INSTANCE_NAME}_ExtendedFilterElementSet(uint8_t filterNumber, mcan_xidfe_registers_t *extMsgIDFilterElement)
{
    if ((filterNumber > ${FILTERS_EXT}) || (extMsgIDFilterElement == NULL))
    {
        return false;
    }
    ${MCAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.extMsgIDFilterAddress[filterNumber - 1].MCAN_XIDFE_0 = extMsgIDFilterElement->MCAN_XIDFE_0;
    ${MCAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.extMsgIDFilterAddress[filterNumber - 1].MCAN_XIDFE_1 = extMsgIDFilterElement->MCAN_XIDFE_1;

    return true;
}

// *****************************************************************************
/* Function:
    bool ${MCAN_INSTANCE_NAME}_ExtendedFilterElementGet(uint8_t filterNumber, mcan_xidfe_registers_t *extMsgIDFilterElement)

   Summary:
    Get a Extended filter element configuration.

   Precondition:
    ${MCAN_INSTANCE_NAME}_Initialize and ${MCAN_INSTANCE_NAME}_MessageRAMConfigSet must have been called
    for the associated MCAN instance.

   Parameters:
    filterNumber          - Extended Filter number to get filter configuration.
    extMsgIDFilterElement - Pointer to Extended Filter Element configuration for storing filter configuration.

   Returns:
    Request status.
    true  - Request was successful.
    false - Request has failed.
*/
bool ${MCAN_INSTANCE_NAME}_ExtendedFilterElementGet(uint8_t filterNumber, mcan_xidfe_registers_t *extMsgIDFilterElement)
{
    if ((filterNumber > ${FILTERS_EXT}) || (extMsgIDFilterElement == NULL))
    {
        return false;
    }
    extMsgIDFilterElement->MCAN_XIDFE_0 = ${MCAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.extMsgIDFilterAddress[filterNumber - 1].MCAN_XIDFE_0;
    extMsgIDFilterElement->MCAN_XIDFE_1 = ${MCAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.extMsgIDFilterAddress[filterNumber - 1].MCAN_XIDFE_1;

    return true;
}
</#if>

<#if INTERRUPT_MODE == true>
// *****************************************************************************
/* Function:
    bool ${MCAN_INSTANCE_NAME}_IsBusy(void)

   Summary:
    Returns the Peripheral busy status.

   Precondition:
    ${MCAN_INSTANCE_NAME}_Initialize must have been called for the associated MCAN instance.

   Parameters:
    None.

   Returns:
    true - Busy.
    false - Not busy.
*/
bool ${MCAN_INSTANCE_NAME}_IsBusy(void)
{
    if (${MCAN_INSTANCE_NAME?lower_case}Obj.state == MCAN_STATE_IDLE)
    {
        return false;
    }
    else
    {
        return true;
    }
}

// *****************************************************************************
/* Function:
    void ${MCAN_INSTANCE_NAME}_CallbackRegister(MCAN_CALLBACK callback, uintptr_t contextHandle)

   Summary:
    Sets the pointer to the function (and it's context) to be called when the
    given MCAN's transfer events occur.

   Precondition:
    ${MCAN_INSTANCE_NAME}_Initialize must have been called for the associated MCAN instance.

   Parameters:
    callback - A pointer to a function with a calling signature defined
    by the MCAN_CALLBACK data type.

    context - A value (usually a pointer) passed (unused) into the function
    identified by the callback parameter.

   Returns:
    None.
*/
void ${MCAN_INSTANCE_NAME}_CallbackRegister(MCAN_CALLBACK callback, uintptr_t contextHandle)
{
    if (callback == NULL)
    {
        return;
    }

    ${MCAN_INSTANCE_NAME?lower_case}Obj.callback = callback;
    ${MCAN_INSTANCE_NAME?lower_case}Obj.context = contextHandle;
}

// *****************************************************************************
/* Function:
    void ${MCAN_INSTANCE_NAME}_INT0_InterruptHandler(void)

   Summary:
    ${MCAN_INSTANCE_NAME} Peripheral Interrupt Handler.

   Description:
    This function is ${MCAN_INSTANCE_NAME} Peripheral Interrupt Handler and will
    called on every ${MCAN_INSTANCE_NAME} interrupt.

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
void ${MCAN_INSTANCE_NAME}_INT0_InterruptHandler(void)
{
    uint8_t length = 0;
    uint8_t rxgi = 0;
<#if RXBUF_USE>
    mcan_rxbe_registers_t *rxbeFifo = NULL;
</#if>
<#if RXF0_USE>
    mcan_rxf0e_registers_t *rxf0eFifo = NULL;
</#if>
<#if RXF1_USE>
    mcan_rxf1e_registers_t *rxf1eFifo = NULL;
</#if>
    uint32_t ir = ${MCAN_INSTANCE_NAME}_REGS->MCAN_IR;

    /* Check if error occurred */
    if (ir & MCAN_IR_BO_Msk)
    {
        ${MCAN_INSTANCE_NAME}_REGS->MCAN_IR = MCAN_IR_BO_Msk;
        ${MCAN_INSTANCE_NAME?lower_case}Obj.state = MCAN_STATE_ERROR;
        /* Client must call ${MCAN_INSTANCE_NAME}_ErrorGet function to get and clear errors */
        if (${MCAN_INSTANCE_NAME?lower_case}Obj.callback != NULL)
        {
            ${MCAN_INSTANCE_NAME?lower_case}Obj.callback(${MCAN_INSTANCE_NAME?lower_case}Obj.context);
            ${MCAN_INSTANCE_NAME?lower_case}Obj.state = MCAN_STATE_IDLE;
        }
    }
<#if RXF0_USE>
    /* New Message in Rx FIFO 0 */
    if (ir & MCAN_IR_RF0N_Msk)
    {
        ${MCAN_INSTANCE_NAME}_REGS->MCAN_IR = MCAN_IR_RF0N_Msk;
        ${MCAN_INSTANCE_NAME}_REGS->MCAN_IE &= (~MCAN_IE_RF0NE_Msk);

        if (${MCAN_INSTANCE_NAME}_REGS->MCAN_RXF0S & MCAN_RXF0S_F0FL_Msk)
        {
            /* Read data from the Rx FIFO0 */
            rxgi = (uint8_t)((${MCAN_INSTANCE_NAME}_REGS->MCAN_RXF0S & MCAN_RXF0S_F0GI_Msk) >> MCAN_RXF0S_F0GI_Pos);
            rxf0eFifo = (mcan_rxf0e_registers_t *) ((uint8_t *)${MCAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.rxFIFO0Address + rxgi * ${MCAN_INSTANCE_NAME}_RX_FIFO0_ELEMENT_SIZE);

            /* Get received identifier */
            if (rxf0eFifo->MCAN_RXF0E_0 & MCAN_RXF0E_0_XTD_Msk)
            {
                *${MCAN_INSTANCE_NAME?lower_case}Obj.rxId = rxf0eFifo->MCAN_RXF0E_0 & MCAN_RXF0E_0_ID_Msk;
            }
            else
            {
                *${MCAN_INSTANCE_NAME?lower_case}Obj.rxId = (rxf0eFifo->MCAN_RXF0E_0 >> 18) & MCAN_STD_ID_Msk;
            }

            /* Get received data length */
            length = MCANDlcToLengthGet(((rxf0eFifo->MCAN_RXF0E_1 & MCAN_RXF0E_1_DLC_Msk) >> MCAN_RXF0E_1_DLC_Pos));

            /* Copy data to user buffer */
            memcpy(${MCAN_INSTANCE_NAME?lower_case}Obj.rxBuffer, (uint8_t *)&rxf0eFifo->MCAN_RXF0E_DATA, length);
            *${MCAN_INSTANCE_NAME?lower_case}Obj.rxsize = length;

            /* Ack the fifo position */
            ${MCAN_INSTANCE_NAME}_REGS->MCAN_RXF0A = MCAN_RXF0A_F0AI(rxgi);
            ${MCAN_INSTANCE_NAME?lower_case}Obj.state = MCAN_STATE_TRANSFER_DONE;
        }
    }
</#if>
<#if RXF1_USE>
    /* New Message in Rx FIFO 1 */
    if (ir & MCAN_IR_RF1N_Msk)
    {
        ${MCAN_INSTANCE_NAME}_REGS->MCAN_IR = MCAN_IR_RF1N_Msk;
        ${MCAN_INSTANCE_NAME}_REGS->MCAN_IE &= (~MCAN_IE_RF1NE_Msk);

        if (${MCAN_INSTANCE_NAME}_REGS->MCAN_RXF1S & MCAN_RXF1S_F1FL_Msk)
        {
            /* Read data from the Rx FIFO1 */
            rxgi = (uint8_t)((${MCAN_INSTANCE_NAME}_REGS->MCAN_RXF1S & MCAN_RXF1S_F1GI_Msk) >> MCAN_RXF1S_F1GI_Pos);
            rxf1eFifo = (mcan_rxf1e_registers_t *) ((uint8_t *)${MCAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.rxFIFO1Address + rxgi * ${MCAN_INSTANCE_NAME}_RX_FIFO1_ELEMENT_SIZE);

            /* Get received identifier */
            if (rxf1eFifo->MCAN_RXF1E_0 & MCAN_RXF1E_0_XTD_Msk)
            {
                *${MCAN_INSTANCE_NAME?lower_case}Obj.rxId = rxf1eFifo->MCAN_RXF1E_0 & MCAN_RXF1E_0_ID_Msk;
            }
            else
            {
                *${MCAN_INSTANCE_NAME?lower_case}Obj.rxId = (rxf1eFifo->MCAN_RXF1E_0 >> 18) & MCAN_STD_ID_Msk;
            }

            /* Get received data length */
            length = MCANDlcToLengthGet(((rxf1eFifo->MCAN_RXF1E_1 & MCAN_RXF1E_1_DLC_Msk) >> MCAN_RXF1E_1_DLC_Pos));

            /* Copy data to user buffer */
            memcpy(${MCAN_INSTANCE_NAME?lower_case}Obj.rxBuffer, (uint8_t *)&rxf1eFifo->MCAN_RXF1E_DATA, length);
            *${MCAN_INSTANCE_NAME?lower_case}Obj.rxsize = length;

            /* Ack the fifo position */
            ${MCAN_INSTANCE_NAME}_REGS->MCAN_RXF1A = MCAN_RXF1A_F1AI(rxgi);
            ${MCAN_INSTANCE_NAME?lower_case}Obj.state = MCAN_STATE_TRANSFER_DONE;
        }
    }
</#if>
<#if RXBUF_USE>
    /* New Message in Dedicated Rx Buffer */
    if (ir & MCAN_IR_DRX_Msk)
    {
        ${MCAN_INSTANCE_NAME}_REGS->MCAN_IR = MCAN_IR_DRX_Msk;
        ${MCAN_INSTANCE_NAME}_REGS->MCAN_IE &= (~MCAN_IE_DRXE_Msk);

        /* Read data from the Rx Buffer */
        if (${MCAN_INSTANCE_NAME}_REGS->MCAN_NDAT1 != 0)
        {
            for (rxgi = 0; rxgi <= 0x1F; rxgi++)
            {
                if ((${MCAN_INSTANCE_NAME}_REGS->MCAN_NDAT1 & (1 << rxgi)) == (1 << rxgi))
                    break;
            }
        }
        else
        {
            for (rxgi = 0; rxgi <= 0x1F; rxgi++)
            {
                if ((${MCAN_INSTANCE_NAME}_REGS->MCAN_NDAT2 & (1 << rxgi)) == (1 << rxgi))
                {
                    rxgi = rxgi + 32;
                    break;
                }
            }
        }
        rxbeFifo = (mcan_rxbe_registers_t *) ((uint8_t *)${MCAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.rxBuffersAddress + rxgi * ${MCAN_INSTANCE_NAME}_RX_BUFFER_ELEMENT_SIZE);

        /* Get received identifier */
        if (rxbeFifo->MCAN_RXBE_0 & MCAN_RXBE_0_XTD_Msk)
        {
            *${MCAN_INSTANCE_NAME?lower_case}Obj.rxId = rxbeFifo->MCAN_RXBE_0 & MCAN_RXBE_0_ID_Msk;
        }
        else
        {
            *${MCAN_INSTANCE_NAME?lower_case}Obj.rxId = (rxbeFifo->MCAN_RXBE_0 >> 18) & MCAN_STD_ID_Msk;
        }

        /* Get received data length */
        length = MCANDlcToLengthGet(((rxbeFifo->MCAN_RXBE_1 & MCAN_RXBE_1_DLC_Msk) >> MCAN_RXBE_1_DLC_Pos));

        /* Copy data to user buffer */
        memcpy(${MCAN_INSTANCE_NAME?lower_case}Obj.rxBuffer, (uint8_t *)&rxbeFifo->MCAN_RXBE_DATA, length);
        *${MCAN_INSTANCE_NAME?lower_case}Obj.rxsize = length;

        /* Clear new data flag */
        if (rxgi < 32)
        {
            ${MCAN_INSTANCE_NAME}_REGS->MCAN_NDAT1 = (1 << rxgi);
        }
        else
        {
            ${MCAN_INSTANCE_NAME}_REGS->MCAN_NDAT2 = (1 << (rxgi - 32));
        }
        ${MCAN_INSTANCE_NAME?lower_case}Obj.state = MCAN_STATE_TRANSFER_DONE;
    }
</#if>

<#if TX_USE || TXBUF_USE >
    /* TX Completed */
    if (ir & MCAN_IR_TC_Msk)
    {
        ${MCAN_INSTANCE_NAME}_REGS->MCAN_IR = MCAN_IR_TC_Msk;
        ${MCAN_INSTANCE_NAME}_REGS->MCAN_IE &= (~MCAN_IE_TCE_Msk);
        for (uint8_t bufferIndex = 0; bufferIndex < (${MCAN_INSTANCE_NAME}_TX_FIFO_BUFFER_SIZE/${MCAN_INSTANCE_NAME}_TX_FIFO_BUFFER_ELEMENT_SIZE); bufferIndex++)
        {
            if ((${MCAN_INSTANCE_NAME}_REGS->MCAN_TXBTO & (1 << (bufferIndex & 0x1F))) &&
                (${MCAN_INSTANCE_NAME}_REGS->MCAN_TXBTIE & (1 << (bufferIndex & 0x1F))))
            {
                ${MCAN_INSTANCE_NAME}_REGS->MCAN_TXBTIE &= ~(1 << (bufferIndex & 0x1F));
                <#if TXBUF_USE>
                if (0 != (${MCAN_INSTANCE_NAME?lower_case}Obj.txBufferIndex & (1 << (bufferIndex & 0x1F))))
                {
                    ${MCAN_INSTANCE_NAME?lower_case}Obj.txBufferIndex &= (~(1 << (bufferIndex & 0x1F)));
                }
                </#if>
                ${MCAN_INSTANCE_NAME?lower_case}Obj.state = MCAN_STATE_TRANSFER_DONE;
            }
        }
    }

    /* TX FIFO is empty */
    if (ir & MCAN_IR_TFE_Msk)
    {
        ${MCAN_INSTANCE_NAME}_REGS->MCAN_IR = MCAN_IR_TFE_Msk;
        uint8_t getIndex = (uint8_t)((${MCAN_INSTANCE_NAME}_REGS->MCAN_TXFQS & MCAN_TXFQS_TFGI_Msk) >> MCAN_TXFQS_TFGI_Pos);
        uint8_t putIndex = (uint8_t)((${MCAN_INSTANCE_NAME}_REGS->MCAN_TXFQS & MCAN_TXFQS_TFQPI_Msk) >> MCAN_TXFQS_TFQPI_Pos);
        for (uint8_t fifoIndex = getIndex; ; fifoIndex++)
        {
            <#if TXBUF_USE>
            if (fifoIndex >= (${TX_BUFFER_ELEMENTS} + ${TX_FIFO_ELEMENTS}))
            {
                fifoIndex = ${TX_BUFFER_ELEMENTS};
            }
            </#if>
            if (fifoIndex >= putIndex)
            {
                break;
            }
            <#if TXBUF_USE>
            if (0 != (${MCAN_INSTANCE_NAME?lower_case}Obj.txBufferIndex & (1 << ((fifoIndex + ${TX_BUFFER_ELEMENTS}) & 0x1F))))
            {
                ${MCAN_INSTANCE_NAME?lower_case}Obj.txBufferIndex &= (~(1 << ((fifoIndex + ${TX_BUFFER_ELEMENTS}) & 0x1F)));
            }
            </#if>
            ${MCAN_INSTANCE_NAME?lower_case}Obj.state = MCAN_STATE_TRANSFER_DONE;
        }
    }
</#if>
<#if RXF0_USE || RXF1_USE || RXBUF_USE || TX_USE || TXBUF_USE>
    if (${MCAN_INSTANCE_NAME?lower_case}Obj.state == MCAN_STATE_TRANSFER_DONE)
    {
        if (${MCAN_INSTANCE_NAME?lower_case}Obj.callback != NULL)
        {
            ${MCAN_INSTANCE_NAME?lower_case}Obj.callback(${MCAN_INSTANCE_NAME?lower_case}Obj.context);
            ${MCAN_INSTANCE_NAME?lower_case}Obj.state = MCAN_STATE_IDLE;
        }
    }
</#if>
}
</#if>


/*******************************************************************************
 End of File
*/
