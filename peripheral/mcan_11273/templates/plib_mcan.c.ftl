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

static MCAN_OBJ ${MCAN_INSTANCE_NAME?lower_case}Obj;

<#if RXF0_USE>
<#assign RXF0_BYTES_CFG = RXF0_BYTES_CFG!0>
<#if RXF0_BYTES_CFG?number < 5>
  <#assign RXF0_ELEMENT_BYTES = 16 + RXF0_BYTES_CFG?number * 4>
<#else>
  <#assign RXF0_ELEMENT_BYTES = 40 + 16 * (RXF0_BYTES_CFG?number - 5)>
</#if>
/* Configuration for the bytes in each element of RX FIFOs */
static uint8_t ${MCAN_INSTANCE_NAME?lower_case}_rx0_fifo[${RXF0_ELEMENTS} * ${RXF0_ELEMENT_BYTES}]__attribute__((aligned (4))) __attribute__((__section__(".region_nocache")));

</#if>
<#if RXF1_USE>
<#assign RXF1_BYTES_CFG = RXF1_BYTES_CFG!0>
<#if RXF1_BYTES_CFG?number < 5>
  <#assign RXF1_ELEMENT_BYTES = 16 + RXF1_BYTES_CFG?number * 4>
<#else>
  <#assign RXF1_ELEMENT_BYTES = 40 + 16 * (RXF1_BYTES_CFG?number - 5)>
</#if>
static uint8_t ${MCAN_INSTANCE_NAME?lower_case}_rx1_fifo[${RXF1_ELEMENTS} * ${RXF1_ELEMENT_BYTES}]__attribute__((aligned (4))) __attribute__((__section__(".region_nocache")));

</#if>
<#if RXBUF_USE>
<#assign RX_BUFFER_BYTES_CFG = RX_BUFFER_BYTES_CFG!0>
<#if RX_BUFFER_BYTES_CFG?number < 5>
  <#assign RX_BUFFER_ELEMENT_BYTES = 16 + RX_BUFFER_BYTES_CFG?number * 4>
<#else>
  <#assign RX_BUFFER_ELEMENT_BYTES = 40 + 16 * (RX_BUFFER_BYTES_CFG?number - 5)>
</#if>
static uint8_t ${MCAN_INSTANCE_NAME?lower_case}_rx_buffer[${RX_BUFFER_ELEMENTS} * ${RX_BUFFER_ELEMENT_BYTES}]__attribute__((aligned (4))) __attribute__((__section__(".region_nocache")));

</#if>
<#if TX_USE || TXBUF_USE>
<#assign TX_FIFO_BYTES_CFG = TX_FIFO_BYTES_CFG!0>
<#if TX_FIFO_BYTES_CFG?number < 5>
  <#assign TX_ELEMENT_BYTES = 16 + TX_FIFO_BYTES_CFG?number * 4>
<#else>
  <#assign TX_ELEMENT_BYTES = 40 + 16 * (TX_FIFO_BYTES_CFG?number - 5)>
</#if>
/* Configuration for the bytes in each element of TX FIFOs */
static uint8_t ${MCAN_INSTANCE_NAME?lower_case}_tx_fifo[${TX_FIFO_ELEMENTS} * ${TX_ELEMENT_BYTES!0}]__attribute__((aligned (4))) __attribute__((__section__(".region_nocache")));
static MCAN_TX_EVENT_FIFO_ENTRY ${MCAN_INSTANCE_NAME?lower_case}_tx_event_fifo[${TX_FIFO_ELEMENTS}]__attribute__((aligned (4))) __attribute__((__section__(".region_nocache")));

</#if>
<#if FILTERS_STD?number gt 0>
<#assign numInstance=FILTERS_STD?number>
__attribute__((aligned (32))) __attribute__((__section__(".region_cache_aligned_const"))) static MCAN_STANDARD_MESSAGE_ID_FILTER
        ${MCAN_INSTANCE_NAME?lower_case}_std_filter[] =
{
    <#list 1..(numInstance) as idx>
    {
        .S0.val = MCAN_SMF_SFT(${.vars["${MCAN_INSTANCE_NAME}_STD_FILTER${idx}_TYPE"]}) |
                  MCAN_SMF_SFID1(${.vars["${MCAN_INSTANCE_NAME}_STD_FILTER${idx}_SFID1"]}) |
                  MCAN_SMF_SFID2(${.vars["${MCAN_INSTANCE_NAME}_STD_FILTER${idx}_SFID2"]}) |
                  MCAN_SMF_SFEC(${.vars["${MCAN_INSTANCE_NAME}_STD_FILTER${idx}_CONFIG"]}),
    },
     </#list>
};


</#if>
<#if FILTERS_EXT?number gt 0>
#define CONF_${MCAN_INSTANCE_NAME}_XIDAM 0x1FFFFFFF

<#assign numInstance=FILTERS_EXT?number>
__attribute__((aligned (32))) __attribute__((__section__(".region_cache_aligned_const"))) static MCAN_EXTENDED_MESSAGE_ID_FILTER
    ${MCAN_INSTANCE_NAME?lower_case}_ext_filter[] =
{
    <#list 1..(numInstance) as idx>
    {
        .F0.val = MCAN_EFID1(${.vars["${MCAN_INSTANCE_NAME}_EXT_FILTER${idx}_EFID1"]}) | MCAN_EFEC(${.vars["${MCAN_INSTANCE_NAME}_EXT_FILTER${idx}_CONFIG"]}),
        .F1.val = MCAN_EFID2(${.vars["${MCAN_INSTANCE_NAME}_EXT_FILTER${idx}_EFID2"]}) | MCAN_EFT(${.vars["${MCAN_INSTANCE_NAME}_EXT_FILTER${idx}_TYPE"]}),
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
    ${MCAN_INSTANCE_NAME}_REGS->MCAN_FBTP = MCAN_FBTP_FTSEG2(${FBTP_FTSEG2}) | MCAN_FBTP_FTSEG1(${FBTP_FTSEG1}) | MCAN_FBTP_FBRP(${FBTP_FBRP}) | MCAN_FBTP_FSJW(${FBTP_FSJW});

<#else>
    /* Set Data Bit Timing and Prescaler Register */
    ${MCAN_INSTANCE_NAME}_REGS->MCAN_DBTP = MCAN_DBTP_DTSEG2(${FBTP_FTSEG2}) | MCAN_DBTP_DTSEG1(${FBTP_FTSEG1}) | MCAN_DBTP_DBRP(${FBTP_FBRP}) | MCAN_DBTP_DSJW(${FBTP_FSJW});

</#if>
</#if>
<#if MCAN_REVISION_A_ENABLE == true>
    /* Set Bit timing and Prescaler Register */
    ${MCAN_INSTANCE_NAME}_REGS->MCAN_BTP  = MCAN_BTP_TSEG2(${BTP_TSEG2}) | MCAN_BTP_TSEG1(${BTP_TSEG1}) | MCAN_BTP_BRP(${BTP_BRP}) | MCAN_BTP_SJW(${BTP_SJW});
<#else>
    /* Set Nominal Bit timing and Prescaler Register */
    ${MCAN_INSTANCE_NAME}_REGS->MCAN_NBTP  = MCAN_NBTP_NTSEG2(${BTP_TSEG2}) | MCAN_NBTP_NTSEG1(${BTP_TSEG1}) | MCAN_NBTP_NBRP(${BTP_BRP}) | MCAN_NBTP_NSJW(${BTP_SJW});
</#if>

<#if RXF0_USE>
    /* Receive FIFO 0 Configuration Register */
    ${MCAN_INSTANCE_NAME}_REGS->MCAN_RXF0C = MCAN_RXF0C_F0S(${RXF0_ELEMENTS}) | MCAN_RXF0C_F0WM(${RXF0_WATERMARK})<#if RXF0_OVERWRITE> | MCAN_RXF0C_F0OM_Msk</#if> |
            MCAN_RXF0C_F0SA(((uint32_t)${MCAN_INSTANCE_NAME?lower_case}_rx0_fifo >> 2));

</#if>
<#if RXF1_USE>
    /* Receive FIFO 1 Configuration Register */
    ${MCAN_INSTANCE_NAME}_REGS->MCAN_RXF1C = MCAN_RXF1C_F1S(${RXF1_ELEMENTS}) | MCAN_RXF1C_F1WM(${RXF1_WATERMARK})<#if RXF1_OVERWRITE> | MCAN_RXF1C_F1OM_Msk</#if> |
            MCAN_RXF1C_F1SA(((uint32_t)${MCAN_INSTANCE_NAME?lower_case}_rx1_fifo >> 2));

</#if>
<#if RXF0_USE || RXF1_USE || RXBUF_USE>
    /* Receive Buffer / FIFO Element Size Configuration Register */
    ${MCAN_INSTANCE_NAME}_REGS->MCAN_RXESC = 0 <#if RXF0_USE> | MCAN_RXESC_F0DS(${RXF0_BYTES_CFG!0})</#if><#if RXF1_USE> | MCAN_RXESC_F1DS(${RXF1_BYTES_CFG!0})</#if><#if RXBUF_USE> | MCAN_RXESC_RBDS(${RX_BUFFER_BYTES_CFG!0})</#if>;

</#if>
<#if RXBUF_USE>
    ${MCAN_INSTANCE_NAME}_REGS->MCAN_RXBC = MCAN_RXBC_RBSA(((uint32_t)${MCAN_INSTANCE_NAME?lower_case}_rx_buffer >> 2));
    ${MCAN_INSTANCE_NAME}_REGS->MCAN_NDAT1 = MCAN_NDAT1_Msk;
    ${MCAN_INSTANCE_NAME}_REGS->MCAN_NDAT2 = MCAN_NDAT2_Msk;

</#if>
<#if TX_USE || TXBUF_USE>
    /* Transmit Buffer/FIFO Configuration Register */
    ${MCAN_INSTANCE_NAME}_REGS->MCAN_TXBC = MCAN_TXBC_TFQS(${TX_FIFO_ELEMENTS}) | MCAN_TXBC_NDTB(${TX_BUFFER_ELEMENTS}) |
            MCAN_TXBC_TBSA(((uint32_t)${MCAN_INSTANCE_NAME?lower_case}_tx_fifo >> 2));

    /* Transmit Buffer/FIFO Element Size Configuration Register */
    ${MCAN_INSTANCE_NAME}_REGS->MCAN_TXESC = MCAN_TXESC_TBDS(${TX_FIFO_BYTES_CFG});

    /* Transmit Event FIFO Configuration Register */
    ${MCAN_INSTANCE_NAME}_REGS->MCAN_TXEFC = MCAN_TXEFC_EFWM(${TX_FIFO_WATERMARK}) | MCAN_TXEFC_EFS(${TX_FIFO_ELEMENTS}) |
            MCAN_TXEFC_EFSA(((uint32_t)${MCAN_INSTANCE_NAME?lower_case}_tx_event_fifo >> 2));
</#if>

    /* Global Filter Configuration Register */
    ${MCAN_INSTANCE_NAME}_REGS->MCAN_GFC = ${FILTERS_STD_NOMATCH} | ${FILTERS_EXT_NOMATCH}<#if FILTERS_STD_REJECT> | MCAN_GFC_RRFS_REJECT</#if><#if FILTERS_EXT_REJECT> | MCAN_GFC_RRFE_REJECT</#if>;
<#if FILTERS_STD?number gt 0>

    /* Standard ID Filter Configuration Register */
    ${MCAN_INSTANCE_NAME}_REGS->MCAN_SIDFC = MCAN_SIDFC_LSS(${FILTERS_STD}) |
            MCAN_SIDFC_FLSSA(((uint32_t)${MCAN_INSTANCE_NAME?lower_case}_std_filter >> 2));
</#if>
<#if FILTERS_EXT?number gt 0>

    /* Extended ID Filter Configuration Register */
    ${MCAN_INSTANCE_NAME}_REGS->MCAN_XIDFC = MCAN_XIDFC_LSE(${FILTERS_EXT}) |
            MCAN_XIDFC_FLESA(((uint32_t)${MCAN_INSTANCE_NAME?lower_case}_ext_filter >> 2));

    /* Extended ID AND Mask Register */
    ${MCAN_INSTANCE_NAME}_REGS->MCAN_XIDAM = CONF_${MCAN_INSTANCE_NAME}_XIDAM;
</#if>

    /* Timestamp Counter Configuration Register */
    ${MCAN_INSTANCE_NAME}_REGS->MCAN_TSCC = ${TIMESTAMP_MODE} | MCAN_TSCC_TCP(${TIMESTAMP_PRESCALER});
<#if MCAN_TIMEOUT>

    /* Timeout Counter Configuration Register */
    ${MCAN_INSTANCE_NAME}_REGS->MCAN_TOCC = ${TIMEOUT_SELECT} | MCAN_TOCC_ETOC_TOS_CONTROLLED;

    /* Timeout Counter Value Register */
    ${MCAN_INSTANCE_NAME}_REGS->MCAN_TOCV = MCAN_TOCV_TOC(${TIMEOUT_COUNT});
</#if>

    /* Set 16-bit MSB of ${MCAN_INSTANCE_NAME?lower_case} base address */
<#if MCAN_SFR_CAN_ENABLE == true>
<#if MCAN_INSTANCE_NAME?lower_case == "mcan0">
    SFR_REGS->SFR_CAN = (SFR_REGS->SFR_CAN & ~SFR_CAN_EXT_MEM_CAN0_ADDR_Msk)
                       | SFR_CAN_EXT_MEM_CAN0_ADDR((uint32_t)${MCAN_INSTANCE_NAME?lower_case}_rx0_fifo >> 16);
<#else>
    SFR_REGS->SFR_CAN = (SFR_REGS->SFR_CAN & ~SFR_CAN_EXT_MEM_CAN1_ADDR_Msk)
                       | SFR_CAN_EXT_MEM_CAN1_ADDR((uint32_t)${MCAN_INSTANCE_NAME?lower_case}_rx0_fifo >> 16);
</#if>
<#elseif MCAN_MATRIX_CAN_ENABLE == true>
<#if MCAN_INSTANCE_NAME?lower_case == "mcan0">
        MATRIX_REGS->CCFG_CAN0 = (uint32_t)${MCAN_INSTANCE_NAME?lower_case}_rx0_fifo & 0xFFFF0000;
<#else>
        MATRIX_REGS->CCFG_SYSIO = (MATRIX_REGS->CCFG_SYSIO & 0x0000FFFF) | ((uint32_t)${MCAN_INSTANCE_NAME?lower_case}_rx0_fifo & 0xFFFF0000);
</#if>
</#if>

    /* Clear Tx/Rx FIFO */
<#if RXF0_USE>
    memset((void*)${MCAN_INSTANCE_NAME?lower_case}_rx0_fifo, 0x00, (${RXF0_ELEMENTS} * ${RXF0_ELEMENT_BYTES}));
</#if>
<#if RXF1_USE>
    memset((void*)${MCAN_INSTANCE_NAME?lower_case}_rx1_fifo, 0x00, (${RXF1_ELEMENTS} * ${RXF1_ELEMENT_BYTES}));
</#if>
<#if RXBUF_USE>
    memset((void*)${MCAN_INSTANCE_NAME?lower_case}_rx_buffer, 0x00, (${RX_BUFFER_ELEMENTS} * ${RX_BUFFER_ELEMENT_BYTES}));
</#if>
<#if TX_USE || TXBUF_USE>
    memset((void*)${MCAN_INSTANCE_NAME?lower_case}_tx_fifo, 0x00, (${TX_FIFO_ELEMENTS} * ${TX_ELEMENT_BYTES!0}));
    memset((void*)${MCAN_INSTANCE_NAME?lower_case}_tx_event_fifo, 0x00, (sizeof(MCAN_TX_EVENT_FIFO_ENTRY) * ${TX_FIFO_ELEMENTS}));
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
    ${MCAN_INSTANCE_NAME?lower_case}Obj.rxAddress = 0;
    ${MCAN_INSTANCE_NAME?lower_case}Obj.rxBuffer = 0;
    ${MCAN_INSTANCE_NAME?lower_case}Obj.rxsize = 0;
    ${MCAN_INSTANCE_NAME?lower_case}Obj.state = MCAN_STATE_IDLE;
</#if>
}

// *****************************************************************************
/* Function:
    bool ${MCAN_INSTANCE_NAME}_MessageTransmit(uint32_t address, uint8_t length, uint8_t* data, MCAN_MODE mode, MCAN_MSG_TX_ATTRIBUTE msgAttr)

   Summary:
    Transmits a message into CAN bus.

   Precondition:
    ${MCAN_INSTANCE_NAME}_Initialize must have been called for the associated MCAN instance.

   Parameters:
    address - 11-bit / 29-bit identifier (ID).
    length  - length of data buffer in number of bytes.
    data    - pointer to source data buffer
    mode    - MCAN mode Classic CAN or CAN FD without BRS or CAN FD with BRS
    msgAttr - Data Frame or Remote frame using Tx FIFO or Tx Buffer

   Returns:
    Request status.
    true  - Request was successful.
    false - Request has failed.
*/
bool ${MCAN_INSTANCE_NAME}_MessageTransmit(uint32_t address, uint8_t length, uint8_t* data, MCAN_MODE mode, MCAN_MSG_TX_ATTRIBUTE msgAttr)
{
<#if MCAN_OPMODE =="CAN FD">
    uint8_t dlc = 0;
</#if>
<#if TXBUF_USE>
    uint8_t bufferIndex = 0;
</#if>
    uint8_t tfqpi = 0;
<#if TX_USE || TXBUF_USE>
    MCAN_TX_BUFFER_FIFO_ENTRY *fifo = NULL;
</#if>

    switch (msgAttr)
    {
<#if TXBUF_USE>
        case MCAN_MSG_ATTR_TX_BUFFER_DATA_FRAME:
        case MCAN_MSG_ATTR_TX_BUFFER_RTR_FRAME:
            for (bufferIndex = 0; bufferIndex < (${TX_BUFFER_ELEMENTS} + ${TX_FIFO_ELEMENTS}); bufferIndex++)
            {
                if ((${MCAN_INSTANCE_NAME?lower_case}Obj.txBufferIndex & (1 << (bufferIndex & 0x1F))) == 0)
                {
                    ${MCAN_INSTANCE_NAME?lower_case}Obj.txBufferIndex |= (1 << (bufferIndex & 0x1F));
                    tfqpi = bufferIndex;
                    break;
                }
                else if(bufferIndex == (${TX_BUFFER_ELEMENTS} + ${TX_FIFO_ELEMENTS}))
                {
                    /* The Tx buffers are full */
                    return false;
                }
            }
            fifo = (MCAN_TX_BUFFER_FIFO_ENTRY *) (${MCAN_INSTANCE_NAME?lower_case}_tx_fifo + tfqpi * ${TX_ELEMENT_BYTES!0});
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
            ${MCAN_INSTANCE_NAME?lower_case}Obj.txBufferIndex |= (1 << ((tfqpi - ${TX_BUFFER_ELEMENTS}) & 0x1F));
            fifo = (MCAN_TX_BUFFER_FIFO_ENTRY *) (${MCAN_INSTANCE_NAME?lower_case}_tx_fifo + tfqpi * ${TX_ELEMENT_BYTES!0});
            break;
</#if>
        default:
            /* Invalid Message Attribute */
            return false;
    }

    /* If the address is longer than 11 bits, it is considered as extended identifier */
    if (address > MCAN_STD_ID_Msk)
    {
        /* An extended identifier is stored into ID */
        fifo->T0.val = (address & MCAN_EXT_ID_Msk) | MCAN_TX_XTD_Msk;
    }
    else
    {
        /* A standard identifier is stored into ID[28:18] */
        fifo->T0.val = address << 18;
    }
<#if MCAN_OPMODE =="CAN FD">
    if (length > 64)
        length = 64;

    MCANLengthToDlcGet(length, &dlc);

    fifo->T1.val = MCAN_TXFE_DLC(dlc);

<#if MCAN_REVISION_A_ENABLE == false>
    if(mode == MCAN_MODE_FD_WITH_BRS)
    {
        fifo->T1.val |= MCAN_TX_FDF_Msk | MCAN_TX_BRS_Msk;
    }
    else if (mode == MCAN_MODE_FD_WITHOUT_BRS)
    {
        fifo->T1.val |= MCAN_TX_FDF_Msk;
    }
</#if>
<#else>

    /* Limit length */
    if (length > 8)
        length = 8;
    fifo->T1.val = MCAN_TXFE_DLC(length);
</#if>

    if (msgAttr == MCAN_MSG_ATTR_TX_BUFFER_DATA_FRAME || msgAttr == MCAN_MSG_ATTR_TX_FIFO_DATA_FRAME)
    {
        /* copy the data into the payload */
        memcpy((uint8_t *)&fifo->data, data, length);
    }
    else if (msgAttr == MCAN_MSG_ATTR_TX_BUFFER_RTR_FRAME || msgAttr == MCAN_MSG_ATTR_TX_FIFO_RTR_FRAME)
    {
        fifo->T0.val |= MCAN_TX_RTR_Msk;
    }
<#if INTERRUPT_MODE == true>

    ${MCAN_INSTANCE_NAME}_REGS->MCAN_TXBTIE = 1U << tfqpi;
    ${MCAN_INSTANCE_NAME?lower_case}Obj.state = MCAN_STATE_TRANSFER_TRANSMIT;
</#if>

    /* request the transmit */
    ${MCAN_INSTANCE_NAME}_REGS->MCAN_TXBAR = 1U << tfqpi;

<#if INTERRUPT_MODE == true>
    ${MCAN_INSTANCE_NAME}_REGS->MCAN_IE = MCAN_IE_TCE_Msk;
</#if>
    return true;
}

// *****************************************************************************
/* Function:
    bool ${MCAN_INSTANCE_NAME}_MessageReceive(uint32_t *address, uint8_t *length, uint8_t *data, MCAN_MSG_RX_ATTRIBUTE msgAttr)

   Summary:
    Receives a message from CAN bus.

   Precondition:
    ${MCAN_INSTANCE_NAME}_Initialize must have been called for the associated MCAN instance.

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
bool ${MCAN_INSTANCE_NAME}_MessageReceive(uint32_t *address, uint8_t *length, uint8_t *data, MCAN_MSG_RX_ATTRIBUTE msgAttr)
{
<#if INTERRUPT_MODE == false>
    uint8_t msgLength = 0;
    uint8_t rxgi = 0;
    MCAN_RX_BUFFER_FIFO_ENTRY *fifo = NULL;
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
            fifo = (MCAN_RX_BUFFER_FIFO_ENTRY *) (${MCAN_INSTANCE_NAME?lower_case}_rx_buffer + rxgi * ${RX_BUFFER_ELEMENT_BYTES!0});

            /* Get received identifier */
            if (MCAN_RX_XTD(fifo->R0.val))
            {
                *address = fifo->R0.val & MCAN_EXT_ID_Msk;
            }
            else
            {
                *address = (fifo->R0.val >> 18) & MCAN_STD_ID_Msk;
            }

            /* Get received data length */
            msgLength = MCANDlcToLengthGet((MCAN_RX_DLC(fifo->R1.val)));

            /* Copy data to user buffer */
            memcpy(data, (uint8_t *)&fifo->data, msgLength);
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
            fifo = (MCAN_RX_BUFFER_FIFO_ENTRY *) (${MCAN_INSTANCE_NAME?lower_case}_rx0_fifo + rxgi * ${RXF0_ELEMENT_BYTES!16});

            /* Get received identifier */
            if (MCAN_RX_XTD(fifo->R0.val))
            {
                *address = fifo->R0.val & MCAN_EXT_ID_Msk;
            }
            else
            {
                *address = (fifo->R0.val >> 18) & MCAN_STD_ID_Msk;
            }

            /* Get received data length */
            msgLength = MCANDlcToLengthGet((MCAN_RX_DLC(fifo->R1.val)));

            /* Copy data to user buffer */
            memcpy(data, (uint8_t *)&fifo->data, msgLength);
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
            fifo = (MCAN_RX_BUFFER_FIFO_ENTRY *) (${MCAN_INSTANCE_NAME?lower_case}_rx1_fifo + rxgi * ${RXF1_ELEMENT_BYTES!16});

            /* Get received identifier */
            if (MCAN_RX_XTD(fifo->R0.val))
            {
                *address = fifo->R0.val & MCAN_EXT_ID_Msk;
            }
            else
            {
                *address = (fifo->R0.val >> 18) & MCAN_STD_ID_Msk;
            }

            /* Get received data length */
            msgLength = MCANDlcToLengthGet((MCAN_RX_DLC(fifo->R1.val)));

            /* Copy data to user buffer */
            memcpy(data, (uint8_t *)&fifo->data, msgLength);
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
    ${MCAN_INSTANCE_NAME?lower_case}Obj.rxAddress = address;
    ${MCAN_INSTANCE_NAME?lower_case}Obj.rxBuffer = data;
    ${MCAN_INSTANCE_NAME?lower_case}Obj.rxsize = length;
    ${MCAN_INSTANCE_NAME}_REGS->MCAN_IE = rxInterrupt;
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
    void ${MCAN_INSTANCE_NAME}_MessageRAMConfigGet(MCAN_MSG_RAM_CONFIG *msgRAMConfig)

   Summary:
    Get the Message RAM Configuration.

   Precondition:
    ${MCAN_INSTANCE_NAME}_Initialize must have been called for the associated MCAN instance.

   Parameters:
    msgRAMConfig - Pointer to the Message RAM Configuration object

   Returns:
    None
*/
void ${MCAN_INSTANCE_NAME}_MessageRAMConfigGet(MCAN_MSG_RAM_CONFIG *msgRAMConfig)
{
    memset((void*)msgRAMConfig, 0x00, sizeof(MCAN_MSG_RAM_CONFIG));

<#if RXF0_USE>
    msgRAMConfig->rxFIFO0Address = (MCAN_RX_BUFFER_FIFO_ENTRY *)${MCAN_INSTANCE_NAME?lower_case}_rx0_fifo;
    msgRAMConfig->rxFIFO0Size = (${RXF0_ELEMENTS} * ${RXF0_ELEMENT_BYTES});
</#if>
<#if RXF1_USE>
    msgRAMConfig->rxFIFO1Address = (MCAN_RX_BUFFER_FIFO_ENTRY *)${MCAN_INSTANCE_NAME?lower_case}_rx1_fifo;
    msgRAMConfig->rxFIFO1Size = (${RXF1_ELEMENTS} * ${RXF1_ELEMENT_BYTES});
</#if>
<#if RXBUF_USE>
    msgRAMConfig->rxBuffersAddress = (MCAN_RX_BUFFER_FIFO_ENTRY *)${MCAN_INSTANCE_NAME?lower_case}_rx_buffer;
    msgRAMConfig->rxBuffersSize = (${RX_BUFFER_ELEMENTS} * ${RX_BUFFER_ELEMENT_BYTES});
</#if>
<#if TX_USE || TXBUF_USE>
    msgRAMConfig->txBuffersAddress = (MCAN_TX_BUFFER_FIFO_ENTRY *)${MCAN_INSTANCE_NAME?lower_case}_tx_fifo;
    msgRAMConfig->txBuffersSize = (${TX_FIFO_ELEMENTS} * ${TX_ELEMENT_BYTES!0});
    msgRAMConfig->txEventFIFOAddress =  (MCAN_TX_EVENT_FIFO_ENTRY *)${MCAN_INSTANCE_NAME?lower_case}_tx_event_fifo;
    msgRAMConfig->txEventFIFOSize = (${TX_FIFO_ELEMENTS} * sizeof(MCAN_TX_EVENT_FIFO_ENTRY));
</#if>
<#if FILTERS_STD?number gt 0>
    msgRAMConfig->stdMsgIDFilterAddress = (MCAN_STANDARD_MESSAGE_ID_FILTER *)${MCAN_INSTANCE_NAME?lower_case}_std_filter;
    msgRAMConfig->stdMsgIDFilterSize = (${FILTERS_STD} * sizeof(MCAN_STANDARD_MESSAGE_ID_FILTER));
</#if>
<#if FILTERS_EXT?number gt 0>
    msgRAMConfig->extMsgIDFilterAddress = (MCAN_EXTENDED_MESSAGE_ID_FILTER *)${MCAN_INSTANCE_NAME?lower_case}_ext_filter;
    msgRAMConfig->extMsgIDFilterSize = (${FILTERS_EXT} * sizeof(MCAN_EXTENDED_MESSAGE_ID_FILTER));
</#if>
}

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
    MCAN_RX_BUFFER_FIFO_ENTRY *fifo = NULL;
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
            fifo = (MCAN_RX_BUFFER_FIFO_ENTRY *) (${MCAN_INSTANCE_NAME?lower_case}_rx0_fifo + rxgi * ${RXF0_ELEMENT_BYTES!16});

            /* Get received identifier */
            if (MCAN_RX_XTD(fifo->R0.val))
            {
                *${MCAN_INSTANCE_NAME?lower_case}Obj.rxAddress = fifo->R0.val & MCAN_EXT_ID_Msk;
            }
            else
            {
                *${MCAN_INSTANCE_NAME?lower_case}Obj.rxAddress = (fifo->R0.val >> 18) & MCAN_STD_ID_Msk;
            }

            /* Get received data length */
            length = MCANDlcToLengthGet((MCAN_RX_DLC(fifo->R1.val)));

            /* Copy data to user buffer */
            memcpy(${MCAN_INSTANCE_NAME?lower_case}Obj.rxBuffer, (uint8_t *)&fifo->data, length);
            *${MCAN_INSTANCE_NAME?lower_case}Obj.rxsize = length;

            /* Ack the fifo position */
            ${MCAN_INSTANCE_NAME}_REGS->MCAN_RXF0A = MCAN_RXF0A_F0AI(rxgi);
            ${MCAN_INSTANCE_NAME?lower_case}Obj.state = MCAN_STATE_TRANSFER_DONE;
        }

        if (${MCAN_INSTANCE_NAME?lower_case}Obj.callback != NULL)
        {
            ${MCAN_INSTANCE_NAME?lower_case}Obj.callback(${MCAN_INSTANCE_NAME?lower_case}Obj.context);
            ${MCAN_INSTANCE_NAME?lower_case}Obj.state = MCAN_STATE_IDLE;
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
            fifo = (MCAN_RX_BUFFER_FIFO_ENTRY *) (${MCAN_INSTANCE_NAME?lower_case}_rx1_fifo + rxgi * ${RXF1_ELEMENT_BYTES!16});

            /* Get received identifier */
            if (MCAN_RX_XTD(fifo->R0.val))
            {
                *${MCAN_INSTANCE_NAME?lower_case}Obj.rxAddress = fifo->R0.val & MCAN_EXT_ID_Msk;
            }
            else
            {
                *${MCAN_INSTANCE_NAME?lower_case}Obj.rxAddress = (fifo->R0.val >> 18) & MCAN_STD_ID_Msk;
            }

            /* Get received data length */
            length = MCANDlcToLengthGet((MCAN_RX_DLC(fifo->R1.val)));

            /* Copy data to user buffer */
            memcpy(${MCAN_INSTANCE_NAME?lower_case}Obj.rxBuffer, (uint8_t *)&fifo->data, length);
            *${MCAN_INSTANCE_NAME?lower_case}Obj.rxsize = length;

            /* Ack the fifo position */
            ${MCAN_INSTANCE_NAME}_REGS->MCAN_RXF1A = MCAN_RXF1A_F1AI(rxgi);
            ${MCAN_INSTANCE_NAME?lower_case}Obj.state = MCAN_STATE_TRANSFER_DONE;
        }

        if (${MCAN_INSTANCE_NAME?lower_case}Obj.callback != NULL)
        {
            ${MCAN_INSTANCE_NAME?lower_case}Obj.callback(${MCAN_INSTANCE_NAME?lower_case}Obj.context);
            ${MCAN_INSTANCE_NAME?lower_case}Obj.state = MCAN_STATE_IDLE;
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
        fifo = (MCAN_RX_BUFFER_FIFO_ENTRY *) (${MCAN_INSTANCE_NAME?lower_case}_rx_buffer + rxgi * ${RX_BUFFER_ELEMENT_BYTES!0});

        /* Get received identifier */
        if (MCAN_RX_XTD(fifo->R0.val))
        {
            *${MCAN_INSTANCE_NAME?lower_case}Obj.rxAddress = fifo->R0.val & MCAN_EXT_ID_Msk;
        }
        else
        {
            *${MCAN_INSTANCE_NAME?lower_case}Obj.rxAddress = (fifo->R0.val >> 18) & MCAN_STD_ID_Msk;
        }

        /* Get received data length */
        length = MCANDlcToLengthGet((MCAN_RX_DLC(fifo->R1.val)));

        /* Copy data to user buffer */
        memcpy(${MCAN_INSTANCE_NAME?lower_case}Obj.rxBuffer, (uint8_t *)&fifo->data, length);
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
    }
</#if>

<#if TX_USE || TXBUF_USE >
    /* TX Completed */
    if (ir & MCAN_IR_TC_Msk)
    {
        ${MCAN_INSTANCE_NAME}_REGS->MCAN_IR = MCAN_IR_TC_Msk;
        ${MCAN_INSTANCE_NAME}_REGS->MCAN_IE &= (~MCAN_IE_TCE_Msk);
        for (uint8_t bufferIndex = 0; bufferIndex < (${TX_BUFFER_ELEMENTS} + ${TX_FIFO_ELEMENTS}); bufferIndex++)
        {
            if ((${MCAN_INSTANCE_NAME}_REGS->MCAN_TXBTO & (1 << (bufferIndex & 0x1F))) &&
                (${MCAN_INSTANCE_NAME}_REGS->MCAN_TXBTIE & (1 << (bufferIndex & 0x1F))))
            {
                ${MCAN_INSTANCE_NAME}_REGS->MCAN_TXBTIE &= ~(1 << (bufferIndex & 0x1F));
                if (0 != (${MCAN_INSTANCE_NAME?lower_case}Obj.txBufferIndex & (1 << (bufferIndex & 0x1F))))
                {
                    ${MCAN_INSTANCE_NAME?lower_case}Obj.txBufferIndex &= (~(1 << (bufferIndex & 0x1F)));
                }
                ${MCAN_INSTANCE_NAME?lower_case}Obj.state = MCAN_STATE_TRANSFER_DONE;
            }
        }
        if (${MCAN_INSTANCE_NAME?lower_case}Obj.callback != NULL)
        {
            ${MCAN_INSTANCE_NAME?lower_case}Obj.callback(${MCAN_INSTANCE_NAME?lower_case}Obj.context);
            ${MCAN_INSTANCE_NAME?lower_case}Obj.state = MCAN_STATE_IDLE;
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
            if (fifoIndex >= (${TX_BUFFER_ELEMENTS} + ${TX_FIFO_ELEMENTS}))
            {
                fifoIndex = ${TX_BUFFER_ELEMENTS};
            }
            if (fifoIndex >= putIndex)
            {
                break;
            }
            if (0 != (${MCAN_INSTANCE_NAME?lower_case}Obj.txBufferIndex & (1 << ((fifoIndex - ${TX_BUFFER_ELEMENTS}) & 0x1F))))
            {
                ${MCAN_INSTANCE_NAME?lower_case}Obj.txBufferIndex &= (~(1 << ((fifoIndex - ${TX_BUFFER_ELEMENTS}) & 0x1F)));
            }
            ${MCAN_INSTANCE_NAME?lower_case}Obj.state = MCAN_STATE_TRANSFER_DONE;
        }
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
