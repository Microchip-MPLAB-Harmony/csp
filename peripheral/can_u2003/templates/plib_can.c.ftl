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
#include "plib_${CAN_INSTANCE_NAME?lower_case}.h"

// *****************************************************************************
// *****************************************************************************
// Global Data
// *****************************************************************************
// *****************************************************************************

static CAN_OBJ ${CAN_INSTANCE_NAME?lower_case}Obj;

<#if RXF0_USE>
<#assign RXF0_BYTES_CFG = RXF0_BYTES_CFG!0>
<#if RXF0_BYTES_CFG?number < 5>
  <#assign RXF0_ELEMENT_BYTES = 16 + RXF0_BYTES_CFG?number * 4>
<#else>
  <#assign RXF0_ELEMENT_BYTES = 40 + 16 * (RXF0_BYTES_CFG?number - 5)>
</#if>
/* Configuration for the bytes in each element of RX FIFOs */
static uint8_t ${CAN_INSTANCE_NAME?lower_case}_rx0_fifo[${RXF0_ELEMENTS} * ${RXF0_ELEMENT_BYTES}]__attribute__((aligned (4))) __attribute__((__section__(".region_nocache")));

</#if>
<#if RXF1_USE>
<#assign RXF1_BYTES_CFG = RXF1_BYTES_CFG!0>
<#if RXF1_BYTES_CFG?number < 5>
  <#assign RXF1_ELEMENT_BYTES = 16 + RXF1_BYTES_CFG?number * 4>
<#else>
  <#assign RXF1_ELEMENT_BYTES = 40 + 16 * (RXF1_BYTES_CFG?number - 5)>
</#if>
static uint8_t ${CAN_INSTANCE_NAME?lower_case}_rx1_fifo[${RXF1_ELEMENTS} * ${RXF1_ELEMENT_BYTES}]__attribute__((aligned (4))) __attribute__((__section__(".region_nocache")));

</#if>
<#if RXBUF_USE>
<#assign RX_BUFFER_BYTES_CFG = RX_BUFFER_BYTES_CFG!0>
<#if RX_BUFFER_BYTES_CFG?number < 5>
  <#assign RX_BUFFER_ELEMENT_BYTES = 16 + RX_BUFFER_BYTES_CFG?number * 4>
<#else>
  <#assign RX_BUFFER_ELEMENT_BYTES = 40 + 16 * (RX_BUFFER_BYTES_CFG?number - 5)>
</#if>
static uint8_t ${CAN_INSTANCE_NAME?lower_case}_rx_buffer[${RX_BUFFER_ELEMENTS} * ${RX_BUFFER_ELEMENT_BYTES}]__attribute__((aligned (4))) __attribute__((__section__(".region_nocache")));

</#if>
<#if TX_USE || TXBUF_USE>
<#assign TX_FIFO_BYTES_CFG = TX_FIFO_BYTES_CFG!0>
<#if TX_FIFO_BYTES_CFG?number < 5>
  <#assign TX_ELEMENT_BYTES = 16 + TX_FIFO_BYTES_CFG?number * 4>
<#else>
  <#assign TX_ELEMENT_BYTES = 40 + 16 * (TX_FIFO_BYTES_CFG?number - 5)>
</#if>
/* Configuration for the bytes in each element of TX FIFOs */
static uint8_t ${CAN_INSTANCE_NAME?lower_case}_tx_fifo[${TX_FIFO_ELEMENTS} * ${TX_ELEMENT_BYTES!0}]__attribute__((aligned (4))) __attribute__((__section__(".region_nocache")));
static CAN_TX_EVENT_FIFO_ENTRY ${CAN_INSTANCE_NAME?lower_case}_tx_event_fifo[${TX_FIFO_ELEMENTS}]__attribute__((aligned (4))) __attribute__((__section__(".region_nocache")));

</#if>
<#if FILTERS_STD?number gt 0>
<#assign numInstance=FILTERS_STD?number>
__attribute__((aligned (32))) __attribute__((__section__(".region_cache_aligned_const"))) static CAN_STANDARD_MESSAGE_ID_FILTER
        ${CAN_INSTANCE_NAME?lower_case}_std_filter[] =
{
    <#list 1..(numInstance) as idx>
    {
        .S0.val = CAN_SMF_SFT(${.vars["${CAN_INSTANCE_NAME}_STD_FILTER${idx}_TYPE"]}) |
                  CAN_SMF_SFID1(${.vars["${CAN_INSTANCE_NAME}_STD_FILTER${idx}_SFID1"]}) |
                  CAN_SMF_SFID2(${.vars["${CAN_INSTANCE_NAME}_STD_FILTER${idx}_SFID2"]}) |
                  CAN_SMF_SFEC(${.vars["${CAN_INSTANCE_NAME}_STD_FILTER${idx}_CONFIG"]}),
    },
     </#list>
};


</#if>
<#if FILTERS_EXT?number gt 0>
#define CONF_${CAN_INSTANCE_NAME}_XIDAM 0x1FFFFFFF

<#assign numInstance=FILTERS_EXT?number>
__attribute__((aligned (32))) __attribute__((__section__(".region_cache_aligned_const"))) static CAN_EXTENDED_MESSAGE_ID_FILTER
    ${CAN_INSTANCE_NAME?lower_case}_ext_filter[] =
{
    <#list 1..(numInstance) as idx>
    {
        .F0.val = CAN_EFID1(${.vars["${CAN_INSTANCE_NAME}_EXT_FILTER${idx}_EFID1"]}) | CAN_EFEC(${.vars["${CAN_INSTANCE_NAME}_EXT_FILTER${idx}_CONFIG"]}),
        .F1.val = CAN_EFID2(${.vars["${CAN_INSTANCE_NAME}_EXT_FILTER${idx}_EFID2"]}) | CAN_EFT(${.vars["${CAN_INSTANCE_NAME}_EXT_FILTER${idx}_TYPE"]}),
    },
     </#list>
};


</#if>

/******************************************************************************
Local Functions
******************************************************************************/

<#if CAN_OPMODE == "CAN FD">
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
static uint8_t CANDlcToLengthGet(uint8_t dlc)
{
    uint8_t msgLength[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 12, 16, 20, 24, 32, 48, 64};
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
    while ((${CAN_INSTANCE_NAME}_REGS->CAN_CCCR & CAN_CCCR_INIT_Msk) != CAN_CCCR_INIT_Msk);

    /* Set CCE to unlock the configuration registers */
    ${CAN_INSTANCE_NAME}_REGS->CAN_CCCR |= CAN_CCCR_CCE_Msk;

<#if CAN_OPMODE == "CAN FD">
    /* Set Data Bit Timing and Prescaler Register */
    ${CAN_INSTANCE_NAME}_REGS->CAN_DBTP = CAN_DBTP_DTSEG2(${DBTP_FTSEG2}) | CAN_DBTP_DTSEG1(${DBTP_FTSEG1}) | CAN_DBTP_DBRP(${DBTP_DBRP}) | CAN_DBTP_DSJW(${DBTP_FSJW});

</#if>
    /* Set Nominal Bit timing and Prescaler Register */
    ${CAN_INSTANCE_NAME}_REGS->CAN_NBTP  = CAN_NBTP_NTSEG2(${NBTP_TSEG2}) | CAN_NBTP_NTSEG1(${NBTP_TSEG1}) | CAN_NBTP_NBRP(${NBTP_BRP}) | CAN_NBTP_NSJW(${NBTP_SJW});

<#if RXF0_USE>
    /* Receive FIFO 0 Configuration Register */
    ${CAN_INSTANCE_NAME}_REGS->CAN_RXF0C = CAN_RXF0C_F0S(${RXF0_ELEMENTS}) | CAN_RXF0C_F0WM(${RXF0_WATERMARK})<#if RXF0_OVERWRITE> | CAN_RXF0C_F0OM_Msk</#if> |
            CAN_RXF0C_F0SA(((uint32_t)${CAN_INSTANCE_NAME?lower_case}_rx0_fifo >> 2));

</#if>
<#if RXF1_USE>
    /* Receive FIFO 1 Configuration Register */
    ${CAN_INSTANCE_NAME}_REGS->CAN_RXF1C = CAN_RXF1C_F1S(${RXF1_ELEMENTS}) | CAN_RXF1C_F1WM(${RXF1_WATERMARK})<#if RXF1_OVERWRITE> | CAN_RXF1C_F1OM_Msk</#if> |
            CAN_RXF1C_F1SA(((uint32_t)${CAN_INSTANCE_NAME?lower_case}_rx1_fifo >> 2));

</#if>
<#if RXF0_USE || RXF1_USE || RXBUF_USE>
    /* Receive Buffer / FIFO Element Size Configuration Register */
    ${CAN_INSTANCE_NAME}_REGS->CAN_RXESC = 0 <#if RXF0_USE> | CAN_RXESC_F0DS(${RXF0_BYTES_CFG!0})</#if><#if RXF1_USE> | CAN_RXESC_F1DS(${RXF1_BYTES_CFG!0})</#if><#if RXBUF_USE> | CAN_RXESC_RBDS(${RX_BUFFER_BYTES_CFG!0})</#if>;

</#if>
<#if RXBUF_USE>
    ${CAN_INSTANCE_NAME}_REGS->CAN_RXBC = CAN_RXBC_RBSA(((uint32_t)${CAN_INSTANCE_NAME?lower_case}_rx_buffer >> 2));
    ${CAN_INSTANCE_NAME}_REGS->CAN_NDAT1 = CAN_NDAT1_Msk;
    ${CAN_INSTANCE_NAME}_REGS->CAN_NDAT2 = CAN_NDAT2_Msk;

</#if>
<#if TX_USE || TXBUF_USE>
    /* Transmit Buffer/FIFO Configuration Register */
    ${CAN_INSTANCE_NAME}_REGS->CAN_TXBC = CAN_TXBC_TFQS(${TX_FIFO_ELEMENTS}) | CAN_TXBC_NDTB(${TX_BUFFER_ELEMENTS}) |
            CAN_TXBC_TBSA(((uint32_t)${CAN_INSTANCE_NAME?lower_case}_tx_fifo >> 2));

    /* Transmit Buffer/FIFO Element Size Configuration Register */
    ${CAN_INSTANCE_NAME}_REGS->CAN_TXESC = CAN_TXESC_TBDS(${TX_FIFO_BYTES_CFG});

    /* Transmit Event FIFO Configuration Register */
    ${CAN_INSTANCE_NAME}_REGS->CAN_TXEFC = CAN_TXEFC_EFWM(${TX_FIFO_WATERMARK}) | CAN_TXEFC_EFS(${TX_FIFO_ELEMENTS}) |
            CAN_TXEFC_EFSA(((uint32_t)${CAN_INSTANCE_NAME?lower_case}_tx_event_fifo >> 2));
</#if>

    /* Global Filter Configuration Register */
    ${CAN_INSTANCE_NAME}_REGS->CAN_GFC = ${FILTERS_STD_NOMATCH} | ${FILTERS_EXT_NOMATCH}<#if FILTERS_STD_REJECT> | CAN_GFC_RRFS_Msk</#if><#if FILTERS_EXT_REJECT> | CAN_GFC_RRFE_Msk</#if>;
<#if FILTERS_STD?number gt 0>

    /* Standard ID Filter Configuration Register */
    ${CAN_INSTANCE_NAME}_REGS->CAN_SIDFC = CAN_SIDFC_LSS(${FILTERS_STD}) |
            CAN_SIDFC_FLSSA(((uint32_t)${CAN_INSTANCE_NAME?lower_case}_std_filter >> 2));
</#if>
<#if FILTERS_EXT?number gt 0>

    /* Extended ID Filter Configuration Register */
    ${CAN_INSTANCE_NAME}_REGS->CAN_XIDFC = CAN_XIDFC_LSE(${FILTERS_EXT}) |
            CAN_XIDFC_FLESA(((uint32_t)${CAN_INSTANCE_NAME?lower_case}_ext_filter >> 2));

    /* Extended ID AND Mask Register */
    ${CAN_INSTANCE_NAME}_REGS->CAN_XIDAM = CONF_${CAN_INSTANCE_NAME}_XIDAM;
</#if>

    /* Timestamp Counter Configuration Register */
    ${CAN_INSTANCE_NAME}_REGS->CAN_TSCC = ${TIMESTAMP_MODE} | CAN_TSCC_TCP(${TIMESTAMP_PRESCALER});
<#if CAN_TIMEOUT>

    /* Timeout Counter Configuration Register */
    ${CAN_INSTANCE_NAME}_REGS->CAN_TOCC = ${TIMEOUT_SELECT} | CAN_TOCC_ETOC_Msk;

    /* Timeout Counter Value Register */
    ${CAN_INSTANCE_NAME}_REGS->CAN_TOCV = CAN_TOCV_TOC(${TIMEOUT_COUNT});
</#if>

    /* Clear Tx/Rx FIFO */
<#if RXF0_USE>
    memset((void*)${CAN_INSTANCE_NAME?lower_case}_rx0_fifo, 0x00, (${RXF0_ELEMENTS} * ${RXF0_ELEMENT_BYTES}));
</#if>
<#if RXF1_USE>
    memset((void*)${CAN_INSTANCE_NAME?lower_case}_rx1_fifo, 0x00, (${RXF1_ELEMENTS} * ${RXF1_ELEMENT_BYTES}));
</#if>
<#if RXBUF_USE>
    memset((void*)${CAN_INSTANCE_NAME?lower_case}_rx_buffer, 0x00, (${RX_BUFFER_ELEMENTS} * ${RX_BUFFER_ELEMENT_BYTES}));
</#if>
<#if TX_USE || TXBUF_USE>
    memset((void*)${CAN_INSTANCE_NAME?lower_case}_tx_fifo, 0x00, (${TX_FIFO_ELEMENTS} * ${TX_ELEMENT_BYTES!0}));
    memset((void*)${CAN_INSTANCE_NAME?lower_case}_tx_event_fifo, 0x00, (sizeof(CAN_TX_EVENT_FIFO_ENTRY) * ${TX_FIFO_ELEMENTS}));
</#if>

    /* Set the operation mode */
    ${CAN_INSTANCE_NAME}_REGS->CAN_CCCR = (${CAN_INSTANCE_NAME}_REGS->CAN_CCCR & ~CAN_CCCR_INIT_Msk)${(CAN_OPMODE == "CAN FD")?then(' | CAN_CCCR_FDOE_Msk | CAN_CCCR_BRSE_Msk','')}<#if TX_PAUSE!false> | CAN_CCCR_TXP_Msk</#if>;
    while ((${CAN_INSTANCE_NAME}_REGS->CAN_CCCR & CAN_CCCR_INIT_Msk) == CAN_CCCR_INIT_Msk);
<#if INTERRUPT_MODE == true>

    /* Select interrupt line */
    ${CAN_INSTANCE_NAME}_REGS->CAN_ILS = 0x0;

    /* Enable interrupt line */
    ${CAN_INSTANCE_NAME}_REGS->CAN_ILE = CAN_ILE_EINT0_Msk;

    /* Enable CAN interrupts */
    ${CAN_INSTANCE_NAME}_REGS->CAN_IE = CAN_IE_BOE_Msk;

    // Initialize the CAN PLib Object
    ${CAN_INSTANCE_NAME?lower_case}Obj.txBufferIndex = 0;
    ${CAN_INSTANCE_NAME?lower_case}Obj.rxAddress = 0;
    ${CAN_INSTANCE_NAME?lower_case}Obj.rxBuffer = 0;
    ${CAN_INSTANCE_NAME?lower_case}Obj.rxsize = 0;
    ${CAN_INSTANCE_NAME?lower_case}Obj.state = CAN_STATE_IDLE;
</#if>
}

// *****************************************************************************
/* Function:
    bool ${CAN_INSTANCE_NAME}_MessageTransmit(uint32_t address, uint8_t length, uint8_t* data, CAN_MODE mode, CAN_MSG_TX_ATTRIBUTE msgAttr)

   Summary:
    Transmits a message into CAN bus.

   Precondition:
    ${CAN_INSTANCE_NAME}_Initialize must have been called for the associated CAN instance.

   Parameters:
    address - 11-bit / 29-bit identifier (ID).
    length  - length of data buffer in number of bytes.
    data    - pointer to source data buffer
    mode    - CAN mode Classic CAN or CAN FD without BRS or CAN FD with BRS
    msgAttr - Data Frame or Remote frame using Tx FIFO or Tx Buffer

   Returns:
    Request status.
    true  - Request was successful.
    false - Request has failed.
*/
bool ${CAN_INSTANCE_NAME}_MessageTransmit(uint32_t address, uint8_t length, uint8_t* data, CAN_MODE mode, CAN_MSG_TX_ATTRIBUTE msgAttr)
{
<#if CAN_OPMODE =="CAN FD">
    uint8_t dlc = 0;
</#if>
<#if TXBUF_USE>
    uint8_t bufferIndex = 0;
</#if>
    uint8_t tfqpi = 0;
<#if TX_USE || TXBUF_USE>
    CAN_TX_BUFFER_FIFO_ENTRY *fifo = NULL;
</#if>

    switch (msgAttr)
    {
<#if TXBUF_USE>
        case CAN_MSG_ATTR_TX_BUFFER_DATA_FRAME:
        case CAN_MSG_ATTR_TX_BUFFER_RTR_FRAME:
            for (bufferIndex = 0; bufferIndex < (${TX_BUFFER_ELEMENTS} + ${TX_FIFO_ELEMENTS}); bufferIndex++)
            {
                if ((${CAN_INSTANCE_NAME?lower_case}Obj.txBufferIndex & (1 << (bufferIndex & 0x1F))) == 0)
                {
                    ${CAN_INSTANCE_NAME?lower_case}Obj.txBufferIndex |= (1 << (bufferIndex & 0x1F));
                    tfqpi = bufferIndex;
                    break;
                }
                else if(bufferIndex == (${TX_BUFFER_ELEMENTS} + ${TX_FIFO_ELEMENTS}))
                {
                    /* The Tx buffers are full */
                    return false;
                }
            }
            fifo = (CAN_TX_BUFFER_FIFO_ENTRY *) (${CAN_INSTANCE_NAME?lower_case}_tx_fifo + tfqpi * ${TX_ELEMENT_BYTES!0});
            break;
</#if>
<#if TX_USE>
        case CAN_MSG_ATTR_TX_FIFO_DATA_FRAME:
        case CAN_MSG_ATTR_TX_FIFO_RTR_FRAME:
            if (${CAN_INSTANCE_NAME}_REGS->CAN_TXFQS & CAN_TXFQS_TFQF_Msk)
            {
                /* The FIFO is full */
                return false;
            }
            tfqpi = (uint8_t)((${CAN_INSTANCE_NAME}_REGS->CAN_TXFQS & CAN_TXFQS_TFQPI_Msk) >> CAN_TXFQS_TFQPI_Pos);
            ${CAN_INSTANCE_NAME?lower_case}Obj.txBufferIndex |= (1 << ((tfqpi - ${TX_BUFFER_ELEMENTS}) & 0x1F));
            fifo = (CAN_TX_BUFFER_FIFO_ENTRY *) (${CAN_INSTANCE_NAME?lower_case}_tx_fifo + tfqpi * ${TX_ELEMENT_BYTES!0});
            break;
</#if>
        default:
            /* Invalid Message Attribute */
            return false;
    }

    /* If the address is longer than 11 bits, it is considered as extended identifier */
    if (address > CAN_STD_ID_Msk)
    {
        /* An extended identifier is stored into ID */
        fifo->T0.val = (address & CAN_EXT_ID_Msk) | CAN_TX_XTD_Msk;
    }
    else
    {
        /* A standard identifier is stored into ID[28:18] */
        fifo->T0.val = address << 18;
    }
<#if CAN_OPMODE =="CAN FD">
    if (length > 64)
        length = 64;

    CANLengthToDlcGet(length, &dlc);

    fifo->T1.val = CAN_TXFE_DLC(dlc);

    if(mode == CAN_MODE_FD_WITH_BRS)
    {
        fifo->T1.val |= CAN_TX_FDF_Msk | CAN_TX_BRS_Msk;
    }
    else if (mode == CAN_MODE_FD_WITHOUT_BRS)
    {
        fifo->T1.val |= CAN_TX_FDF_Msk;
    }
<#else>

    /* Limit length */
    if (length > 8)
        length = 8;
    fifo->T1.val = CAN_TXFE_DLC(length);
</#if>

    if (msgAttr == CAN_MSG_ATTR_TX_BUFFER_DATA_FRAME || msgAttr == CAN_MSG_ATTR_TX_FIFO_DATA_FRAME)
    {
        /* copy the data into the payload */
        memcpy((uint8_t *)&fifo->data, data, length);
    }
    else if (msgAttr == CAN_MSG_ATTR_TX_BUFFER_RTR_FRAME || msgAttr == CAN_MSG_ATTR_TX_FIFO_RTR_FRAME)
    {
        fifo->T0.val |= CAN_TX_RTR_Msk;
    }
<#if INTERRUPT_MODE == true>

    ${CAN_INSTANCE_NAME}_REGS->CAN_TXBTIE = 1U << tfqpi;
    ${CAN_INSTANCE_NAME?lower_case}Obj.state = CAN_STATE_TRANSFER_TRANSMIT;
</#if>

    /* request the transmit */
    ${CAN_INSTANCE_NAME}_REGS->CAN_TXBAR = 1U << tfqpi;

<#if INTERRUPT_MODE == true>
    ${CAN_INSTANCE_NAME}_REGS->CAN_IE = CAN_IE_TCE_Msk;
</#if>
    return true;
}

// *****************************************************************************
/* Function:
    bool ${CAN_INSTANCE_NAME}_MessageReceive(uint32_t *address, uint8_t *length, uint8_t *data, CAN_MSG_RX_ATTRIBUTE msgAttr)

   Summary:
    Receives a message from CAN bus.

   Precondition:
    ${CAN_INSTANCE_NAME}_Initialize must have been called for the associated CAN instance.

   Parameters:
    address - Pointer to 11-bit / 29-bit identifier (ID) to be received.
    length  - Pointer to data length in number of bytes to be received.
    data    - pointer to destination data buffer
    msgAttr - Message to be read from Rx FIFO0 or Rx FIFO1 or Rx Buffer

   Returns:
    Request status.
    true  - Request was successful.
    false - Request has failed.
*/
bool ${CAN_INSTANCE_NAME}_MessageReceive(uint32_t *address, uint8_t *length, uint8_t *data, CAN_MSG_RX_ATTRIBUTE msgAttr)
{
<#if INTERRUPT_MODE == false>
    uint8_t msgLength = 0;
    uint8_t rxgi = 0;
    CAN_RX_BUFFER_FIFO_ENTRY *fifo = NULL;
<#else>
    uint32_t rxInterrupt = 0;
</#if>
    bool status = false;

    switch (msgAttr)
    {
<#if RXBUF_USE>
        case CAN_MSG_ATTR_RX_BUFFER:
<#if INTERRUPT_MODE == false>
            /* Check and return false if nothing to be read */
            if ((${CAN_INSTANCE_NAME}_REGS->CAN_NDAT1 == 0) && (${CAN_INSTANCE_NAME}_REGS->CAN_NDAT2 == 0))
            {
                return status;
            }
            /* Read data from the Rx Buffer */
            if (${CAN_INSTANCE_NAME}_REGS->CAN_NDAT1 != 0)
            {
                for (rxgi = 0; rxgi <= 0x1F; rxgi++)
                {
                    if ((${CAN_INSTANCE_NAME}_REGS->CAN_NDAT1 & (1 << rxgi)) == (1 << rxgi))
                        break;
                }
            }
            else
            {
                for (rxgi = 0; rxgi <= 0x1F; rxgi++)
                {
                    if ((${CAN_INSTANCE_NAME}_REGS->CAN_NDAT2 & (1 << rxgi)) == (1 << rxgi))
                    {
                        rxgi = rxgi + 32;
                        break;
                    }
                }
            }
            fifo = (CAN_RX_BUFFER_FIFO_ENTRY *) (${CAN_INSTANCE_NAME?lower_case}_rx_buffer + rxgi * ${RX_BUFFER_ELEMENT_BYTES!0});

            /* Get received identifier */
            if (CAN_RX_XTD(fifo->R0.val))
            {
                *address = fifo->R0.val & CAN_EXT_ID_Msk;
            }
            else
            {
                *address = (fifo->R0.val >> 18) & CAN_STD_ID_Msk;
            }

            /* Get received data length */
            msgLength = CANDlcToLengthGet((CAN_RX_DLC(fifo->R1.val)));

            /* Copy data to user buffer */
            memcpy(data, (uint8_t *)&fifo->data, msgLength);
            *length = msgLength;

            /* Clear new data flag */
            if (rxgi < 32)
            {
                ${CAN_INSTANCE_NAME}_REGS->CAN_NDAT1 = (1 << rxgi);
            }
            else
            {
                ${CAN_INSTANCE_NAME}_REGS->CAN_NDAT2 = (1 << (rxgi - 32));
            }
<#else>
            rxInterrupt = CAN_IE_DRXE_Msk;
</#if>
            status = true;
            break;
</#if>
<#if RXF0_USE>
        case CAN_MSG_ATTR_RX_FIFO0:
<#if INTERRUPT_MODE == false>
            /* Check and return false if nothing to be read */
            if ((${CAN_INSTANCE_NAME}_REGS->CAN_RXF0S & CAN_RXF0S_F0FL_Msk) == 0)
            {
                return status;
            }
            /* Read data from the Rx FIFO0 */
            rxgi = (uint8_t)((${CAN_INSTANCE_NAME}_REGS->CAN_RXF0S & CAN_RXF0S_F0GI_Msk) >> CAN_RXF0S_F0GI_Pos);
            fifo = (CAN_RX_BUFFER_FIFO_ENTRY *) (${CAN_INSTANCE_NAME?lower_case}_rx0_fifo + rxgi * ${RXF0_ELEMENT_BYTES!16});

            /* Get received identifier */
            if (CAN_RX_XTD(fifo->R0.val))
            {
                *address = fifo->R0.val & CAN_EXT_ID_Msk;
            }
            else
            {
                *address = (fifo->R0.val >> 18) & CAN_STD_ID_Msk;
            }

            /* Get received data length */
            msgLength = CANDlcToLengthGet((CAN_RX_DLC(fifo->R1.val)));

            /* Copy data to user buffer */
            memcpy(data, (uint8_t *)&fifo->data, msgLength);
            *length = msgLength;

            /* Ack the fifo position */
            ${CAN_INSTANCE_NAME}_REGS->CAN_RXF0A = CAN_RXF0A_F0AI(rxgi);
<#else>
            rxInterrupt = CAN_IE_RF0NE_Msk;
</#if>
            status = true;
            break;
</#if>
<#if RXF1_USE>
        case CAN_MSG_ATTR_RX_FIFO1:
<#if INTERRUPT_MODE == false>
            /* Check and return false if nothing to be read */
            if ((${CAN_INSTANCE_NAME}_REGS->CAN_RXF1S & CAN_RXF1S_F1FL_Msk) == 0)
            {
                return status;
            }
            /* Read data from the Rx FIFO1 */
            rxgi = (uint8_t)((${CAN_INSTANCE_NAME}_REGS->CAN_RXF1S & CAN_RXF1S_F1GI_Msk) >> CAN_RXF1S_F1GI_Pos);
            fifo = (CAN_RX_BUFFER_FIFO_ENTRY *) (${CAN_INSTANCE_NAME?lower_case}_rx1_fifo + rxgi * ${RXF1_ELEMENT_BYTES!16});

            /* Get received identifier */
            if (CAN_RX_XTD(fifo->R0.val))
            {
                *address = fifo->R0.val & CAN_EXT_ID_Msk;
            }
            else
            {
                *address = (fifo->R0.val >> 18) & CAN_STD_ID_Msk;
            }

            /* Get received data length */
            msgLength = CANDlcToLengthGet((CAN_RX_DLC(fifo->R1.val)));

            /* Copy data to user buffer */
            memcpy(data, (uint8_t *)&fifo->data, msgLength);
            *length = msgLength;

            /* Ack the fifo position */
            ${CAN_INSTANCE_NAME}_REGS->CAN_RXF1A = CAN_RXF1A_F1AI(rxgi);
<#else>
            rxInterrupt = CAN_IE_RF1NE_Msk;
</#if>
            status = true;
            break;
</#if>
        default:
            return status;
    }
<#if INTERRUPT_MODE == true>
    ${CAN_INSTANCE_NAME?lower_case}Obj.state = CAN_STATE_TRANSFER_RECEIVE;
    ${CAN_INSTANCE_NAME?lower_case}Obj.rxAddress = address;
    ${CAN_INSTANCE_NAME?lower_case}Obj.rxBuffer = data;
    ${CAN_INSTANCE_NAME?lower_case}Obj.rxsize = length;
    ${CAN_INSTANCE_NAME}_REGS->CAN_IE = rxInterrupt;
</#if>
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
        ${CAN_INSTANCE_NAME}_REGS->CAN_CCCR |= CAN_CCCR_CCE_Msk;
        ${CAN_INSTANCE_NAME}_REGS->CAN_CCCR = (${CAN_INSTANCE_NAME}_REGS->CAN_CCCR & ~CAN_CCCR_INIT_Msk)${(CAN_OPMODE == "CAN FD")?then(' | CAN_CCCR_FDOE_Msk | CAN_CCCR_BRSE_Msk','')}<#if TX_PAUSE!false> | CAN_CCCR_TXP_Msk</#if>;
        while ((${CAN_INSTANCE_NAME}_REGS->CAN_CCCR & CAN_CCCR_INIT_Msk) == CAN_CCCR_INIT_Msk);
    }

    return error;
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
    return ((${CAN_INSTANCE_NAME}_REGS->CAN_IR & interruptMask) != 0x0);
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
    ${CAN_INSTANCE_NAME}_REGS->CAN_IR = interruptMask;
}

// *****************************************************************************
/* Function:
    void ${CAN_INSTANCE_NAME}_MessageRAMConfigGet(CAN_MSG_RAM_CONFIG *msgRAMConfig)

   Summary:
    Get the Message RAM Configuration.

   Precondition:
    ${CAN_INSTANCE_NAME}_Initialize must have been called for the associated CAN instance.

   Parameters:
    msgRAMConfig - Pointer to the Message RAM Configuration object

   Returns:
    None
*/
void ${CAN_INSTANCE_NAME}_MessageRAMConfigGet(CAN_MSG_RAM_CONFIG *msgRAMConfig)
{
    memset((void*)msgRAMConfig, 0x00, sizeof(CAN_MSG_RAM_CONFIG));

<#if RXF0_USE>
    msgRAMConfig->rxFIFO0Address = (CAN_RX_BUFFER_FIFO_ENTRY *)${CAN_INSTANCE_NAME?lower_case}_rx0_fifo;
    msgRAMConfig->rxFIFO0Size = (${RXF0_ELEMENTS} * ${RXF0_ELEMENT_BYTES});
</#if>
<#if RXF1_USE>
    msgRAMConfig->rxFIFO1Address = (CAN_RX_BUFFER_FIFO_ENTRY *)${CAN_INSTANCE_NAME?lower_case}_rx1_fifo;
    msgRAMConfig->rxFIFO1Size = (${RXF1_ELEMENTS} * ${RXF1_ELEMENT_BYTES});
</#if>
<#if RXBUF_USE>
    msgRAMConfig->rxBuffersAddress = (CAN_RX_BUFFER_FIFO_ENTRY *)${CAN_INSTANCE_NAME?lower_case}_rx_buffer;
    msgRAMConfig->rxBuffersSize = (${RX_BUFFER_ELEMENTS} * ${RX_BUFFER_ELEMENT_BYTES});
</#if>
<#if TX_USE || TXBUF_USE>
    msgRAMConfig->txBuffersAddress = (CAN_TX_BUFFER_FIFO_ENTRY *)${CAN_INSTANCE_NAME?lower_case}_tx_fifo;
    msgRAMConfig->txBuffersSize = (${TX_FIFO_ELEMENTS} * ${TX_ELEMENT_BYTES!0});
    msgRAMConfig->txEventFIFOAddress =  (CAN_TX_EVENT_FIFO_ENTRY *)${CAN_INSTANCE_NAME?lower_case}_tx_event_fifo;
    msgRAMConfig->txEventFIFOSize = (${TX_FIFO_ELEMENTS} * sizeof(CAN_TX_EVENT_FIFO_ENTRY));
</#if>
<#if FILTERS_STD?number gt 0>
    msgRAMConfig->stdMsgIDFilterAddress = (CAN_STANDARD_MESSAGE_ID_FILTER *)${CAN_INSTANCE_NAME?lower_case}_std_filter;
    msgRAMConfig->stdMsgIDFilterSize = (${FILTERS_STD} * sizeof(CAN_STANDARD_MESSAGE_ID_FILTER));
</#if>
<#if FILTERS_EXT?number gt 0>
    msgRAMConfig->extMsgIDFilterAddress = (CAN_EXTENDED_MESSAGE_ID_FILTER *)${CAN_INSTANCE_NAME?lower_case}_ext_filter;
    msgRAMConfig->extMsgIDFilterSize = (${FILTERS_EXT} * sizeof(CAN_EXTENDED_MESSAGE_ID_FILTER));
</#if>
}

<#if INTERRUPT_MODE == true>
// *****************************************************************************
/* Function:
    bool ${CAN_INSTANCE_NAME}_IsBusy(void)

   Summary:
    Returns the Peripheral busy status.

   Precondition:
    ${CAN_INSTANCE_NAME}_Initialize must have been called for the associated CAN instance.

   Parameters:
    None.

   Returns:
    true - Busy.
    false - Not busy.
*/
bool ${CAN_INSTANCE_NAME}_IsBusy(void)
{
    if (${CAN_INSTANCE_NAME?lower_case}Obj.state == CAN_STATE_IDLE)
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
    void ${CAN_INSTANCE_NAME}_CallbackRegister(CAN_CALLBACK callback, uintptr_t contextHandle)

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
void ${CAN_INSTANCE_NAME}_CallbackRegister(CAN_CALLBACK callback, uintptr_t contextHandle)
{
    if (callback == NULL)
    {
        return;
    }

    ${CAN_INSTANCE_NAME?lower_case}Obj.callback = callback;
    ${CAN_INSTANCE_NAME?lower_case}Obj.context = contextHandle;
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
    uint8_t length = 0;
    uint8_t rxgi = 0;
    CAN_RX_BUFFER_FIFO_ENTRY *fifo = NULL;
    uint32_t ir = ${CAN_INSTANCE_NAME}_REGS->CAN_IR;

    /* Check if error occurred */
    if (ir & CAN_IR_BO_Msk)
    {
        ${CAN_INSTANCE_NAME}_REGS->CAN_IR = CAN_IR_BO_Msk;
        ${CAN_INSTANCE_NAME?lower_case}Obj.state = CAN_STATE_ERROR;
        /* Client must call ${CAN_INSTANCE_NAME}_ErrorGet function to get and clear errors */
        if (${CAN_INSTANCE_NAME?lower_case}Obj.callback != NULL)
        {
            ${CAN_INSTANCE_NAME?lower_case}Obj.callback(${CAN_INSTANCE_NAME?lower_case}Obj.context);
            ${CAN_INSTANCE_NAME?lower_case}Obj.state = CAN_STATE_IDLE;
        }
    }
<#if RXF0_USE>
    /* New Message in Rx FIFO 0 */
    if (ir & CAN_IR_RF0N_Msk)
    {
        ${CAN_INSTANCE_NAME}_REGS->CAN_IR = CAN_IR_RF0N_Msk;
        ${CAN_INSTANCE_NAME}_REGS->CAN_IE &= (~CAN_IE_RF0NE_Msk);

        if (${CAN_INSTANCE_NAME}_REGS->CAN_RXF0S & CAN_RXF0S_F0FL_Msk)
        {
            /* Read data from the Rx FIFO0 */
            rxgi = (uint8_t)((${CAN_INSTANCE_NAME}_REGS->CAN_RXF0S & CAN_RXF0S_F0GI_Msk) >> CAN_RXF0S_F0GI_Pos);
            fifo = (CAN_RX_BUFFER_FIFO_ENTRY *) (${CAN_INSTANCE_NAME?lower_case}_rx0_fifo + rxgi * ${RXF0_ELEMENT_BYTES!16});

            /* Get received identifier */
            if (CAN_RX_XTD(fifo->R0.val))
            {
                *${CAN_INSTANCE_NAME?lower_case}Obj.rxAddress = fifo->R0.val & CAN_EXT_ID_Msk;
            }
            else
            {
                *${CAN_INSTANCE_NAME?lower_case}Obj.rxAddress = (fifo->R0.val >> 18) & CAN_STD_ID_Msk;
            }

            /* Get received data length */
            length = CANDlcToLengthGet((CAN_RX_DLC(fifo->R1.val)));

            /* Copy data to user buffer */
            memcpy(${CAN_INSTANCE_NAME?lower_case}Obj.rxBuffer, (uint8_t *)&fifo->data, length);
            *${CAN_INSTANCE_NAME?lower_case}Obj.rxsize = length;

            /* Ack the fifo position */
            ${CAN_INSTANCE_NAME}_REGS->CAN_RXF0A = CAN_RXF0A_F0AI(rxgi);
            ${CAN_INSTANCE_NAME?lower_case}Obj.state = CAN_STATE_TRANSFER_DONE;
        }

        if (${CAN_INSTANCE_NAME?lower_case}Obj.callback != NULL)
        {
            ${CAN_INSTANCE_NAME?lower_case}Obj.callback(${CAN_INSTANCE_NAME?lower_case}Obj.context);
            ${CAN_INSTANCE_NAME?lower_case}Obj.state = CAN_STATE_IDLE;
        }
    }
</#if>
<#if RXF1_USE>
    /* New Message in Rx FIFO 1 */
    if (ir & CAN_IR_RF1N_Msk)
    {
        ${CAN_INSTANCE_NAME}_REGS->CAN_IR = CAN_IR_RF1N_Msk;
        ${CAN_INSTANCE_NAME}_REGS->CAN_IE &= (~CAN_IE_RF1NE_Msk);

        if (${CAN_INSTANCE_NAME}_REGS->CAN_RXF1S & CAN_RXF1S_F1FL_Msk)
        {
            /* Read data from the Rx FIFO1 */
            rxgi = (uint8_t)((${CAN_INSTANCE_NAME}_REGS->CAN_RXF1S & CAN_RXF1S_F1GI_Msk) >> CAN_RXF1S_F1GI_Pos);
            fifo = (CAN_RX_BUFFER_FIFO_ENTRY *) (${CAN_INSTANCE_NAME?lower_case}_rx1_fifo + rxgi * ${RXF1_ELEMENT_BYTES!16});

            /* Get received identifier */
            if (CAN_RX_XTD(fifo->R0.val))
            {
                *${CAN_INSTANCE_NAME?lower_case}Obj.rxAddress = fifo->R0.val & CAN_EXT_ID_Msk;
            }
            else
            {
                *${CAN_INSTANCE_NAME?lower_case}Obj.rxAddress = (fifo->R0.val >> 18) & CAN_STD_ID_Msk;
            }

            /* Get received data length */
            length = CANDlcToLengthGet((CAN_RX_DLC(fifo->R1.val)));

            /* Copy data to user buffer */
            memcpy(${CAN_INSTANCE_NAME?lower_case}Obj.rxBuffer, (uint8_t *)&fifo->data, length);
            *${CAN_INSTANCE_NAME?lower_case}Obj.rxsize = length;

            /* Ack the fifo position */
            ${CAN_INSTANCE_NAME}_REGS->CAN_RXF1A = CAN_RXF1A_F1AI(rxgi);
            ${CAN_INSTANCE_NAME?lower_case}Obj.state = CAN_STATE_TRANSFER_DONE;
        }

        if (${CAN_INSTANCE_NAME?lower_case}Obj.callback != NULL)
        {
            ${CAN_INSTANCE_NAME?lower_case}Obj.callback(${CAN_INSTANCE_NAME?lower_case}Obj.context);
            ${CAN_INSTANCE_NAME?lower_case}Obj.state = CAN_STATE_IDLE;
        }
    }
</#if>
<#if RXBUF_USE>
    /* New Message in Dedicated Rx Buffer */
    if (ir & CAN_IR_DRX_Msk)
    {
        ${CAN_INSTANCE_NAME}_REGS->CAN_IR = CAN_IR_DRX_Msk;
        ${CAN_INSTANCE_NAME}_REGS->CAN_IE &= (~CAN_IE_DRXE_Msk);

        /* Read data from the Rx Buffer */
        if (${CAN_INSTANCE_NAME}_REGS->CAN_NDAT1 != 0)
        {
            for (rxgi = 0; rxgi <= 0x1F; rxgi++)
            {
                if ((${CAN_INSTANCE_NAME}_REGS->CAN_NDAT1 & (1 << rxgi)) == (1 << rxgi))
                    break;
            }
        }
        else
        {
            for (rxgi = 0; rxgi <= 0x1F; rxgi++)
            {
                if ((${CAN_INSTANCE_NAME}_REGS->CAN_NDAT2 & (1 << rxgi)) == (1 << rxgi))
                {
                    rxgi = rxgi + 32;
                    break;
                }
            }
        }
        fifo = (CAN_RX_BUFFER_FIFO_ENTRY *) (${CAN_INSTANCE_NAME?lower_case}_rx_buffer + rxgi * ${RX_BUFFER_ELEMENT_BYTES!0});

        /* Get received identifier */
        if (CAN_RX_XTD(fifo->R0.val))
        {
            *${CAN_INSTANCE_NAME?lower_case}Obj.rxAddress = fifo->R0.val & CAN_EXT_ID_Msk;
        }
        else
        {
            *${CAN_INSTANCE_NAME?lower_case}Obj.rxAddress = (fifo->R0.val >> 18) & CAN_STD_ID_Msk;
        }

        /* Get received data length */
        length = CANDlcToLengthGet((CAN_RX_DLC(fifo->R1.val)));

        /* Copy data to user buffer */
        memcpy(${CAN_INSTANCE_NAME?lower_case}Obj.rxBuffer, (uint8_t *)&fifo->data, length);
        *${CAN_INSTANCE_NAME?lower_case}Obj.rxsize = length;

        /* Clear new data flag */
        if (rxgi < 32)
        {
            ${CAN_INSTANCE_NAME}_REGS->CAN_NDAT1 = (1 << rxgi);
        }
        else
        {
            ${CAN_INSTANCE_NAME}_REGS->CAN_NDAT2 = (1 << (rxgi - 32));
        }
    }
</#if>

<#if TX_USE || TXBUF_USE >
    /* TX Completed */
    if (ir & CAN_IR_TC_Msk)
    {
        ${CAN_INSTANCE_NAME}_REGS->CAN_IR = CAN_IR_TC_Msk;
        ${CAN_INSTANCE_NAME}_REGS->CAN_IE &= (~CAN_IE_TCE_Msk);
        for (uint8_t bufferIndex = 0; bufferIndex < (${TX_BUFFER_ELEMENTS} + ${TX_FIFO_ELEMENTS}); bufferIndex++)
        {
            if ((${CAN_INSTANCE_NAME}_REGS->CAN_TXBTO & (1 << (bufferIndex & 0x1F))) &&
                (${CAN_INSTANCE_NAME}_REGS->CAN_TXBTIE & (1 << (bufferIndex & 0x1F))))
            {
                ${CAN_INSTANCE_NAME}_REGS->CAN_TXBTIE &= ~(1 << (bufferIndex & 0x1F));
                if (0 != (${CAN_INSTANCE_NAME?lower_case}Obj.txBufferIndex & (1 << (bufferIndex & 0x1F))))
                {
                    ${CAN_INSTANCE_NAME?lower_case}Obj.txBufferIndex &= (~(1 << (bufferIndex & 0x1F)));
                }
                ${CAN_INSTANCE_NAME?lower_case}Obj.state = CAN_STATE_TRANSFER_DONE;
            }
        }
        if (${CAN_INSTANCE_NAME?lower_case}Obj.callback != NULL)
        {
            ${CAN_INSTANCE_NAME?lower_case}Obj.callback(${CAN_INSTANCE_NAME?lower_case}Obj.context);
            ${CAN_INSTANCE_NAME?lower_case}Obj.state = CAN_STATE_IDLE;
        }
    }

    /* TX FIFO is empty */
    if (ir & CAN_IR_TFE_Msk)
    {
        ${CAN_INSTANCE_NAME}_REGS->CAN_IR = CAN_IR_TFE_Msk;
        uint8_t getIndex = (uint8_t)((${CAN_INSTANCE_NAME}_REGS->CAN_TXFQS & CAN_TXFQS_TFGI_Msk) >> CAN_TXFQS_TFGI_Pos);
        uint8_t putIndex = (uint8_t)((${CAN_INSTANCE_NAME}_REGS->CAN_TXFQS & CAN_TXFQS_TFQPI_Msk) >> CAN_TXFQS_TFQPI_Pos);
        for (uint8_t fifoIndex = getIndex; ; fifoIndex++)
        {
            if (fifoIndex >= (${TX_BUFFER_ELEMENTS} + ${TX_FIFO_ELEMENTS}))
            {
                fifoIndex = ${TX_BUFFER_ELEMENTS};
            }
            if (fifoIndex >= putIndex)
            {
                break;
            }
            if (0 != (${CAN_INSTANCE_NAME?lower_case}Obj.txBufferIndex & (1 << ((fifoIndex - ${TX_BUFFER_ELEMENTS}) & 0x1F))))
            {
                ${CAN_INSTANCE_NAME?lower_case}Obj.txBufferIndex &= (~(1 << ((fifoIndex - ${TX_BUFFER_ELEMENTS}) & 0x1F)));
            }
            ${CAN_INSTANCE_NAME?lower_case}Obj.state = CAN_STATE_TRANSFER_DONE;
        }
        if (${CAN_INSTANCE_NAME?lower_case}Obj.callback != NULL)
        {
            ${CAN_INSTANCE_NAME?lower_case}Obj.callback(${CAN_INSTANCE_NAME?lower_case}Obj.context);
            ${CAN_INSTANCE_NAME?lower_case}Obj.state = CAN_STATE_IDLE;
        }
    }
</#if>
}
</#if>


/*******************************************************************************
 End of File
*/
