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
* Copyright (C) 2024 Microchip Technology Inc. and its subsidiaries.
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
<#assign TX_EVENT_FIFO_ELEMENTS = TX_FIFO_ELEMENTS>
<#if TXBUF_USE>
<#assign TX_EVENT_FIFO_ELEMENTS = TX_BUFFER_ELEMENTS + TX_FIFO_ELEMENTS>
</#if>
#define CAN_STD_ID_Msk        0x7FFU

static CAN_OBJ ${CAN_INSTANCE_NAME?lower_case}Obj;
<#if FILTERS_STD?number gt 0>
<#assign numInstance=FILTERS_STD?number>

static const can_mram_sidfe_registers_t ${CAN_INSTANCE_NAME?lower_case}StdFilter[] =
{
    <#list 1..(numInstance) as idx>
    {
        .CAN_S0 = CAN_S0_SFT(${.vars["${CAN_INSTANCE_NAME}_STD_FILTER${idx}_TYPE"]}UL) |
                  CAN_S0_SFID1(0x${.vars["${CAN_INSTANCE_NAME}_STD_FILTER${idx}_SFID1"]}UL) |
                  CAN_S0_SFID2(0x${.vars["${CAN_INSTANCE_NAME}_STD_FILTER${idx}_SFID2"]}UL) |
                  CAN_S0_SFEC(${.vars["${CAN_INSTANCE_NAME}_STD_FILTER${idx}_CONFIG"]}UL)
    },
     </#list>
};
</#if>
<#if FILTERS_EXT?number gt 0>
<#assign numInstance=FILTERS_EXT?number>

static const can_mram_xidfe_registers_t ${CAN_INSTANCE_NAME?lower_case}ExtFilter[] =
{
    <#list 1..(numInstance) as idx>
    {
        .CAN_F0 = CAN_F0_EFID1(0x${.vars["${CAN_INSTANCE_NAME}_EXT_FILTER${idx}_EFID1"]}UL) | CAN_F0_EFEC(${.vars["${CAN_INSTANCE_NAME}_EXT_FILTER${idx}_CONFIG"]}UL),
        .CAN_F1 = CAN_F1_EFID2(0x${.vars["${CAN_INSTANCE_NAME}_EXT_FILTER${idx}_EFID2"]}UL) | CAN_F1_EFT(${.vars["${CAN_INSTANCE_NAME}_EXT_FILTER${idx}_TYPE"]}UL),
    },
     </#list>
};
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
    ${CAN_INSTANCE_NAME}_REGS->CAN_TSCC = CAN_TSCC_TCP(${TIMESTAMP_PRESCALER}UL)<#if TIMESTAMP_ENABLE == true> | CAN_TSCC_TSS_${TIMESTAMP_MODE}</#if>;
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

   (void) memset(&${CAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig, 0x00, sizeof(CAN_MSG_RAM_CONFIG));
}

<#if TXBUF_USE>
// *****************************************************************************
/* Function:
    bool ${CAN_INSTANCE_NAME}_MessageTransmit(uint8_t bufferNumber, CAN_TX_BUFFER *txBuffer)

   Summary:
    Transmits a message into CAN bus from the specific Tx buffer.

   Precondition:
    ${CAN_INSTANCE_NAME}_Initialize must have been called for the associated CAN instance.

   Parameters:
    bufferNumber - Tx buffer number.
    txBuffer     - Pointer to Tx buffer

   Returns:
    Request status.
    true  - Request was successful.
    false - Request has failed.
*/
bool ${CAN_INSTANCE_NAME}_MessageTransmit(uint8_t bufferNumber, CAN_TX_BUFFER *txBuffer)
{
    uint8_t *txBuf = NULL;
    bool message_transmit_event = false;

    if (!((bufferNumber >= ${TX_BUFFER_ELEMENTS}U) || (txBuffer == NULL)))
    {
        txBuf = (uint8_t *)((uint8_t*)${CAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.txBuffersAddress + ((uint32_t)bufferNumber * ${CAN_INSTANCE_NAME}_TX_FIFO_BUFFER_ELEMENT_SIZE));

       (void) memcpy(txBuf, (uint8_t *)txBuffer, ${CAN_INSTANCE_NAME}_TX_FIFO_BUFFER_ELEMENT_SIZE);

        __DSB();

        /* Set Transmission request */
        ${CAN_INSTANCE_NAME}_REGS->CAN_TXBAR = 1UL << bufferNumber;

        message_transmit_event = true;
    }
    return message_transmit_event;
}
</#if>

<#if TX_USE>
// *****************************************************************************
/* Function:
    bool ${CAN_INSTANCE_NAME}_MessageTransmitFifo(uint8_t numberOfMessage, CAN_TX_BUFFER *txBuffer)

   Summary:
    Transmit multiple messages into CAN bus from Tx FIFO.

   Precondition:
    ${CAN_INSTANCE_NAME}_Initialize must have been called for the associated CAN instance.

   Parameters:
    numberOfMessage - Total number of message.
    txBuffer        - Pointer to Tx buffer

   Returns:
    Request status.
    true  - Request was successful.
    false - Request has failed.
*/
bool ${CAN_INSTANCE_NAME}_MessageTransmitFifo(uint8_t numberOfMessage, CAN_TX_BUFFER *txBuffer)
{
    uint8_t  *txFifo = NULL;
    uint8_t  *txBuf = (uint8_t *)txBuffer;
    uint32_t bufferNumber = 0U;
    uint8_t  tfqpi = 0U;
    uint8_t  count = 0U;
    bool transmitFifo_event = false;

    if (!(((numberOfMessage < 1U) || (numberOfMessage > ${TX_FIFO_ELEMENTS}U)) || (txBuffer == NULL)))
    {

        tfqpi = (uint8_t)((${CAN_INSTANCE_NAME}_REGS->CAN_TXFQS & CAN_TXFQS_TFQPI_Msk) >> CAN_TXFQS_TFQPI_Pos);

        for (count = 0U; count < numberOfMessage; count++)
        {
            txFifo = (uint8_t *)((uint8_t*)${CAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.txBuffersAddress + ((uint32_t)tfqpi * ${CAN_INSTANCE_NAME}_TX_FIFO_BUFFER_ELEMENT_SIZE));

            (void) memcpy(txFifo, txBuf, ${CAN_INSTANCE_NAME}_TX_FIFO_BUFFER_ELEMENT_SIZE);

            txBuf += ${CAN_INSTANCE_NAME}_TX_FIFO_BUFFER_ELEMENT_SIZE;
            bufferNumber |= (1UL << tfqpi);
            tfqpi++;
            <#if TXBUF_USE>
            if (tfqpi == (${TX_BUFFER_ELEMENTS}U + ${TX_FIFO_ELEMENTS}U))
            {
                tfqpi = ${TX_BUFFER_ELEMENTS}U;
            }
            <#else>
            if (tfqpi == ${TX_FIFO_ELEMENTS}U)
            {
                tfqpi = 0U;
            }
            </#if>
        }

        __DSB();

        /* Set Transmission request */
        ${CAN_INSTANCE_NAME}_REGS->CAN_TXBAR = bufferNumber;

        transmitFifo_event = true;
    }
    return transmitFifo_event;
}

// *****************************************************************************
/* Function:
    uint8_t ${CAN_INSTANCE_NAME}_TxFifoFreeLevelGet(void)

   Summary:
    Returns Tx FIFO Free Level.

   Precondition:
    ${CAN_INSTANCE_NAME}_Initialize must have been called for the associated CAN instance.

   Parameters:
    None.

   Returns:
    Tx FIFO Free Level.
*/
uint8_t ${CAN_INSTANCE_NAME}_TxFifoFreeLevelGet(void)
{
    return (uint8_t)(${CAN_INSTANCE_NAME}_REGS->CAN_TXFQS & CAN_TXFQS_TFFL_Msk);
}
</#if>

<#if TX_USE || TXBUF_USE>
// *****************************************************************************
/* Function:
    bool ${CAN_INSTANCE_NAME}_TxBufferIsBusy(uint8_t bufferNumber)

   Summary:
    Check if Transmission request is pending for the specific Tx buffer.

   Precondition:
    ${CAN_INSTANCE_NAME}_Initialize must have been called for the associated CAN instance.

   Parameters:
    None.

   Returns:
    true  - Transmission request is pending.
    false - Transmission request is not pending.
*/
bool ${CAN_INSTANCE_NAME}_TxBufferIsBusy(uint8_t bufferNumber)
{
    return ((${CAN_INSTANCE_NAME}_REGS->CAN_TXBRP & (1UL << bufferNumber)) != 0U);
}

// *****************************************************************************
/* Function:
    bool ${CAN_INSTANCE_NAME}_TxEventFifoRead(uint8_t numberOfTxEvent, CAN_TX_EVENT_FIFO *txEventFifo)

   Summary:
    Read Tx Event FIFO for the transmitted messages.

   Precondition:
    ${CAN_INSTANCE_NAME}_Initialize must have been called for the associated CAN instance.

   Parameters:
    numberOfTxEvent - Total number of Tx Event
    txEventFifo     - Pointer to Tx Event FIFO

   Returns:
    Request status.
    true  - Request was successful.
    false - Request has failed.
*/
bool ${CAN_INSTANCE_NAME}_TxEventFifoRead(uint8_t numberOfTxEvent, CAN_TX_EVENT_FIFO *txEventFifo)
{
    uint8_t txefgi     = 0U;
    uint8_t count      = 0U;
    uint8_t *txEvent   = NULL;
    uint8_t *txEvtFifo = (uint8_t *)txEventFifo;
    bool txFifo_event = false;

    if (txEventFifo != NULL)
    {
        /* Read data from the Rx FIFO0 */
        txefgi = (uint8_t)((${CAN_INSTANCE_NAME}_REGS->CAN_TXEFS & CAN_TXEFS_EFGI_Msk) >> CAN_TXEFS_EFGI_Pos);
        for (count = 0U; count < numberOfTxEvent; count++)
        {
            txEvent = (uint8_t *) ((uint8_t *)${CAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.txEventFIFOAddress + ((uint32_t)txefgi * sizeof(CAN_TX_EVENT_FIFO)));

            (void) memcpy(txEvtFifo, txEvent, sizeof(CAN_TX_EVENT_FIFO));

            if ((count + 1U) == numberOfTxEvent)
            {
                break;
            }
            txEvtFifo += sizeof(CAN_TX_EVENT_FIFO);
            txefgi++;
            if (txefgi == ${TX_EVENT_FIFO_ELEMENTS}U)
            {
                txefgi = 0U;
            }
        }

        /* Ack the Tx Event FIFO position */
        ${CAN_INSTANCE_NAME}_REGS->CAN_TXEFA = CAN_TXEFA_EFAI((uint32_t)txefgi);

        txFifo_event = true;
    }
    return txFifo_event;
}

// *****************************************************************************
/* Function:
    uint8_t ${CAN_INSTANCE_NAME}_TxEventFifoFillLevelGet(void)

   Summary:
    Returns Tx Event FIFO Fill Level.

   Precondition:
    ${CAN_INSTANCE_NAME}_Initialize must have been called for the associated CAN instance.

   Parameters:
    None.

   Returns:
    Tx Event FIFO Fill Level.
*/
uint8_t ${CAN_INSTANCE_NAME}_TxEventFifoFillLevelGet(void)
{
    return (uint8_t)(${CAN_INSTANCE_NAME}_REGS->CAN_TXEFS & CAN_TXEFS_EFFL_Msk);
}
</#if>

<#if RXBUF_USE>
// *****************************************************************************
/* Function:
    bool ${CAN_INSTANCE_NAME}_MessageReceive(uint8_t bufferNumber, CAN_RX_BUFFER *rxBuffer)

   Summary:
    Read a message from the specific Rx Buffer.

   Precondition:
    ${CAN_INSTANCE_NAME}_Initialize must have been called for the associated CAN instance.

   Parameters:
    bufferNumber - Rx buffer number
    rxBuffer     - Pointer to Rx buffer

   Returns:
    Request status.
    true  - Request was successful.
    false - Request has failed.
*/
bool ${CAN_INSTANCE_NAME}_MessageReceive(uint8_t bufferNumber, CAN_RX_BUFFER *rxBuffer)
{
    uint8_t *rxBuf = NULL;
    bool message_receive_event = false;

    if((rxBuffer != NULL) && (bufferNumber < ${RX_BUFFER_ELEMENTS}U))
    {
        rxBuf = (uint8_t *) ((uint8_t *)${CAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.rxBuffersAddress + ((uint32_t)bufferNumber * ${CAN_INSTANCE_NAME}_RX_BUFFER_ELEMENT_SIZE));

        (void) memcpy((uint8_t *)rxBuffer, rxBuf, ${CAN_INSTANCE_NAME}_RX_BUFFER_ELEMENT_SIZE);

        /* Clear new data flag */
<#if RX_BUFFER_ELEMENTS gt 32>
        if (bufferNumber < 32U)
        {
            ${CAN_INSTANCE_NAME}_REGS->CAN_NDAT1 = (1UL << bufferNumber);
        }
        else
        {
            ${CAN_INSTANCE_NAME}_REGS->CAN_NDAT2 = (1UL << (bufferNumber - 32U));
        }
<#else>
        ${CAN_INSTANCE_NAME}_REGS->CAN_NDAT1 = (1UL << bufferNumber);
</#if>
        message_receive_event = true;
    }
    return message_receive_event;
}

// *****************************************************************************
/* Function:
    bool ${CAN_INSTANCE_NAME}_RxBufferNumberGet(uint8_t* bufferNumber)

   Summary:
    Get Rx Buffer Number.

   Precondition:
    ${CAN_INSTANCE_NAME}_Initialize must have been called for the associated CAN instance.

   Parameters:
    None.

   Returns:
    Request status.
    true  - Request was successful.
    false - Request has failed.
*/
bool ${CAN_INSTANCE_NAME}_RxBufferNumberGet(uint8_t* bufferNumber)
{
    bool     status = false;
    uint8_t  bufferNum = 0U;
    uint32_t newData1 = ${CAN_INSTANCE_NAME}_REGS->CAN_NDAT1;
    <#if RX_BUFFER_ELEMENTS gt 32>
    uint32_t newData2 = ${CAN_INSTANCE_NAME}_REGS->CAN_NDAT2;
    </#if>

    if (newData1 != 0U)
    {
        <#assign BUF_NUM = 32>
        <#if RX_BUFFER_ELEMENTS lt 32>
        <#assign BUF_NUM = RX_BUFFER_ELEMENTS>
        </#if>
        for (bufferNum = 0U; bufferNum < ${BUF_NUM}U; bufferNum++)
        {
            if ((newData1 & (1UL << bufferNum)) == (1UL << bufferNum))
            {
                *bufferNumber = bufferNum;
                status = true;
                break;
            }
        }
    }
    <#if RX_BUFFER_ELEMENTS gt 32>
    if ((newData2 != 0U) && (status == false))
    {
        for (bufferNum = 0U; bufferNum < (${RX_BUFFER_ELEMENTS}U - 32U); bufferNum++)
        {
            if ((newData2 & (1UL << bufferNum)) == (1UL << bufferNum))
            {
                *bufferNumber = (bufferNum + 32U);
                status = true;
                break;
            }
        }
    }
    </#if>

    return status;
}
</#if>

<#if RXF0_USE || RXF1_USE>
// *****************************************************************************
/* Function:
    bool ${CAN_INSTANCE_NAME}_MessageReceiveFifo(CAN_RX_FIFO_NUM rxFifoNum, uint8_t numberOfMessage, CAN_RX_BUFFER *rxBuffer)

   Summary:
    Read messages from Rx FIFO0/FIFO1.

   Precondition:
    ${CAN_INSTANCE_NAME}_Initialize must have been called for the associated CAN instance.

   Parameters:
    rxFifoNum       - Rx FIFO number
    numberOfMessage - Total number of message
    rxBuffer        - Pointer to Rx buffer

   Returns:
    Request status.
    true  - Request was successful.
    false - Request has failed.
*/
bool ${CAN_INSTANCE_NAME}_MessageReceiveFifo(CAN_RX_FIFO_NUM rxFifoNum, uint8_t numberOfMessage, CAN_RX_BUFFER *rxBuffer)
{
    uint8_t rxgi = 0U;
    uint8_t count = 0U;
    uint8_t *rxFifo = NULL;
    uint8_t *rxBuf = (uint8_t *)rxBuffer;
    bool status = false;

    if (rxBuffer != NULL)
    {
        switch (rxFifoNum)
        {
        <#if RXF0_USE>
            case CAN_RX_FIFO_0:
                /* Read data from the Rx FIFO0 */
                rxgi = (uint8_t)((${CAN_INSTANCE_NAME}_REGS->CAN_RXF0S & CAN_RXF0S_F0GI_Msk) >> CAN_RXF0S_F0GI_Pos);
                for (count = 0U; count < numberOfMessage; count++)
                {
                    rxFifo = (uint8_t *) ((uint8_t *)${CAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.rxFIFO0Address + ((uint32_t)rxgi * ${CAN_INSTANCE_NAME}_RX_FIFO0_ELEMENT_SIZE));

                    (void) memcpy(rxBuf, rxFifo, ${CAN_INSTANCE_NAME}_RX_FIFO0_ELEMENT_SIZE);

                    if ((count + 1U) == numberOfMessage)
                    {
                        break;
                    }
                    rxBuf += ${CAN_INSTANCE_NAME}_RX_FIFO0_ELEMENT_SIZE;
                    rxgi++;
                    if (rxgi == ${RXF0_ELEMENTS}U)
                    {
                        rxgi = 0U;
                    }
                }

                /* Ack the fifo position */
                ${CAN_INSTANCE_NAME}_REGS->CAN_RXF0A = CAN_RXF0A_F0AI((uint32_t)rxgi);

                status = true;
                break;
        </#if>
        <#if RXF1_USE>
            case CAN_RX_FIFO_1:
                /* Read data from the Rx FIFO1 */
                rxgi = (uint8_t)((${CAN_INSTANCE_NAME}_REGS->CAN_RXF1S & CAN_RXF1S_F1GI_Msk) >> CAN_RXF1S_F1GI_Pos);
                for (count = 0U; count < numberOfMessage; count++)
                {
                    rxFifo = (uint8_t *) ((uint8_t *)${CAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.rxFIFO1Address + ((uint32_t)rxgi * ${CAN_INSTANCE_NAME}_RX_FIFO1_ELEMENT_SIZE));

                    (void) memcpy(rxBuf, rxFifo, ${CAN_INSTANCE_NAME}_RX_FIFO1_ELEMENT_SIZE);

                    if ((count + 1U) == numberOfMessage)
                    {
                        break;
                    }
                    rxBuf += ${CAN_INSTANCE_NAME}_RX_FIFO1_ELEMENT_SIZE;
                    rxgi++;
                    if (rxgi == ${RXF1_ELEMENTS}U)
                    {
                        rxgi = 0U;
                    }
                }
                /* Ack the fifo position */
                ${CAN_INSTANCE_NAME}_REGS->CAN_RXF1A = CAN_RXF1A_F1AI((uint32_t)rxgi);

                status = true;
                break;
        </#if>
            default:
                /* Do nothing */
                break;
        }
    }
    return status;
}

// *****************************************************************************
/* Function:
    uint8_t ${CAN_INSTANCE_NAME}_RxFifoFillLevelGet(CAN_RX_FIFO_NUM rxFifoNum)

   Summary:
    Returns Rx FIFO0/FIFO1 Fill Level.

   Precondition:
    ${CAN_INSTANCE_NAME}_Initialize must have been called for the associated CAN instance.

   Parameters:
    None.

   Returns:
    Rx FIFO0/FIFO1 Fill Level.
*/
uint8_t ${CAN_INSTANCE_NAME}_RxFifoFillLevelGet(CAN_RX_FIFO_NUM rxFifoNum)
{
    uint8_t fillLevel = 0U;

    if (rxFifoNum == CAN_RX_FIFO_0)
    {
        fillLevel = (uint8_t)(${CAN_INSTANCE_NAME}_REGS->CAN_RXF0S & CAN_RXF0S_F0FL_Msk);
    }
    else
    {
        fillLevel = (uint8_t)(${CAN_INSTANCE_NAME}_REGS->CAN_RXF1S & CAN_RXF1S_F1FL_Msk);
    }
    return fillLevel;
}
</#if>

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
<#assign DEV_COUNT_11_3 = 0>
<#if RXF0_USE>
<#assign DEV_COUNT_11_3 = DEV_COUNT_11_3 + 1>
</#if>
<#if RXF1_USE>
<#assign DEV_COUNT_11_3 = DEV_COUNT_11_3 + 1>
</#if>
<#if RXBUF_USE>
<#assign DEV_COUNT_11_3 = DEV_COUNT_11_3 + 1>
</#if>
<#if TX_USE || TXBUF_USE>
<#assign DEV_COUNT_11_3 = DEV_COUNT_11_3 + 2>
</#if>
<#if FILTERS_STD?number gt 0>
<#assign DEV_COUNT_11_3 = DEV_COUNT_11_3 + 1>
</#if>
<#if FILTERS_EXT?number gt 0>
<#assign DEV_COUNT_11_3 = DEV_COUNT_11_3 + 1>
</#if>
/* MISRA C-2012 Rule 11.3 violated ${DEV_COUNT_11_3} times below. Deviation record ID - H3_MISRAC_2012_R_11_3_DR_1*/
<#if core.COVERITY_SUPPRESS_DEVIATION?? && core.COVERITY_SUPPRESS_DEVIATION>
<#if core.COMPILER_CHOICE == "XC32">
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wunknown-pragmas"
</#if>
#pragma coverity compliance block deviate:${DEV_COUNT_11_3} "MISRA C-2012 Rule 11.3" "H3_MISRAC_2012_R_11_3_DR_1"
</#if>
void ${CAN_INSTANCE_NAME}_MessageRAMConfigSet(uint8_t *msgRAMConfigBaseAddress)
{
    uint32_t offset = 0U;
    uint32_t msgRAMConfigBaseAddr = (uint32_t)msgRAMConfigBaseAddress;

    (void) memset(msgRAMConfigBaseAddress, 0x00, ${CAN_INSTANCE_NAME}_MESSAGE_RAM_CONFIG_SIZE);

    /* Set CAN CCCR Init for Message RAM Configuration */
    ${CAN_INSTANCE_NAME}_REGS->CAN_CCCR |= CAN_CCCR_INIT_Msk;
    while ((${CAN_INSTANCE_NAME}_REGS->CAN_CCCR & CAN_CCCR_INIT_Msk) != CAN_CCCR_INIT_Msk)
    {
        /* Wait for initialization complete */
    }

    /* Set CCE to unlock the configuration registers */
    ${CAN_INSTANCE_NAME}_REGS->CAN_CCCR |= CAN_CCCR_CCE_Msk;

<#if CAN_MRCFG_OFFSET_ENABLE??>
    /* Message RAM Base Address Offset */
    ${CAN_INSTANCE_NAME}_REGS->CAN_MRCFG = (msgRAMConfigBaseAddr & CAN_MRCFG_OFFSET_Msk);

</#if>
<#if RXF0_USE>
    ${CAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.rxFIFO0Address = (can_mram_rxbe_registers_t *)msgRAMConfigBaseAddr;
    offset = ${CAN_INSTANCE_NAME}_RX_FIFO0_SIZE;
    /* Receive FIFO 0 Configuration Register */
    ${CAN_INSTANCE_NAME}_REGS->CAN_RXF0C = CAN_RXF0C_F0S(${RXF0_ELEMENTS}UL) | CAN_RXF0C_F0WM(${RXF0_WATERMARK}UL)<#if RXF0_OVERWRITE> | CAN_RXF0C_F0OM_Msk</#if> |
            CAN_RXF0C_F0SA(((uint32_t)${CAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.rxFIFO0Address >> 2));

</#if>
<#if RXF1_USE>
    ${CAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.rxFIFO1Address = (can_mram_rxbe_registers_t *)(msgRAMConfigBaseAddr + offset);
    offset += ${CAN_INSTANCE_NAME}_RX_FIFO1_SIZE;
    /* Receive FIFO 1 Configuration Register */
    ${CAN_INSTANCE_NAME}_REGS->CAN_RXF1C = CAN_RXF1C_F1S(${RXF1_ELEMENTS}UL) | CAN_RXF1C_F1WM(${RXF1_WATERMARK}UL)<#if RXF1_OVERWRITE> | CAN_RXF1C_F1OM_Msk</#if> |
            CAN_RXF1C_F1SA(((uint32_t)${CAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.rxFIFO1Address >> 2));

</#if>
<#if RXBUF_USE>
    ${CAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.rxBuffersAddress = (can_mram_rxbe_registers_t *)(msgRAMConfigBaseAddr + offset);
    offset += ${CAN_INSTANCE_NAME}_RX_BUFFER_SIZE;
    ${CAN_INSTANCE_NAME}_REGS->CAN_RXBC = CAN_RXBC_RBSA(((uint32_t)${CAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.rxBuffersAddress >> 2));

</#if>
<#if TX_USE || TXBUF_USE>
    ${CAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.txBuffersAddress = (can_mram_txbe_registers_t *)(msgRAMConfigBaseAddr + offset);
    offset += ${CAN_INSTANCE_NAME}_TX_FIFO_BUFFER_SIZE;
    /* Transmit Buffer/FIFO Configuration Register */
    ${CAN_INSTANCE_NAME}_REGS->CAN_TXBC = CAN_TXBC_TFQS(${TX_FIFO_ELEMENTS}UL)<#if TXBUF_USE> | CAN_TXBC_NDTB(${TX_BUFFER_ELEMENTS}UL)</#if> |
            CAN_TXBC_TBSA(((uint32_t)${CAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.txBuffersAddress >> 2));

    ${CAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.txEventFIFOAddress =  (can_mram_txefe_registers_t *)(msgRAMConfigBaseAddr + offset);
    offset += ${CAN_INSTANCE_NAME}_TX_EVENT_FIFO_SIZE;
    /* Transmit Event FIFO Configuration Register */
    ${CAN_INSTANCE_NAME}_REGS->CAN_TXEFC = CAN_TXEFC_EFWM(${TX_FIFO_WATERMARK}UL) | CAN_TXEFC_EFS(${TX_FIFO_ELEMENTS}UL) |
            CAN_TXEFC_EFSA(((uint32_t)${CAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.txEventFIFOAddress >> 2));

</#if>
<#if FILTERS_STD?number gt 0>
    ${CAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.stdMsgIDFilterAddress = (can_mram_sidfe_registers_t *)(msgRAMConfigBaseAddr + offset);
    (void) memcpy((void*)${CAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.stdMsgIDFilterAddress,
           (const void*)${CAN_INSTANCE_NAME?lower_case}StdFilter,
           ${CAN_INSTANCE_NAME}_STD_MSG_ID_FILTER_SIZE);
    offset += ${CAN_INSTANCE_NAME}_STD_MSG_ID_FILTER_SIZE;
    /* Standard ID Filter Configuration Register */
    ${CAN_INSTANCE_NAME}_REGS->CAN_SIDFC = CAN_SIDFC_LSS(${FILTERS_STD}UL) |
            CAN_SIDFC_FLSSA(((uint32_t)${CAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.stdMsgIDFilterAddress >> 2));

</#if>
<#if FILTERS_EXT?number gt 0>
    ${CAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.extMsgIDFilterAddress = (can_mram_xidfe_registers_t *)(msgRAMConfigBaseAddr + offset);
    (void) memcpy((void*)${CAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.extMsgIDFilterAddress,
           (const void*)${CAN_INSTANCE_NAME?lower_case}ExtFilter,
           ${CAN_INSTANCE_NAME}_EXT_MSG_ID_FILTER_SIZE);
    /* Extended ID Filter Configuration Register */
    ${CAN_INSTANCE_NAME}_REGS->CAN_XIDFC = CAN_XIDFC_LSE(${FILTERS_EXT}UL) |
            CAN_XIDFC_FLESA(((uint32_t)${CAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.extMsgIDFilterAddress >> 2));

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
<#if core.COVERITY_SUPPRESS_DEVIATION?? && core.COVERITY_SUPPRESS_DEVIATION>
#pragma coverity compliance end_block "MISRA C-2012 Rule 11.3"
<#if core.COMPILER_CHOICE == "XC32">
#pragma GCC diagnostic pop
</#if>
</#if>
/* MISRAC 2012 deviation block end for 11.3 */


<#if FILTERS_STD?number gt 0>
// *****************************************************************************
/* Function:
    bool ${CAN_INSTANCE_NAME}_StandardFilterElementSet(uint8_t filterNumber, can_mram_sidfe_registers_t *stdMsgIDFilterElement)

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
bool ${CAN_INSTANCE_NAME}_StandardFilterElementSet(uint8_t filterNumber, can_mram_sidfe_registers_t *stdMsgIDFilterElement)
{
    bool retval = false;
    if (!((filterNumber > ${FILTERS_STD}U) || (stdMsgIDFilterElement == NULL)))
    {
        ${CAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.stdMsgIDFilterAddress[filterNumber - 1U].CAN_S0 = stdMsgIDFilterElement->CAN_S0;
        retval = true;
    }
    return retval;
}

// *****************************************************************************
/* Function:
    bool ${CAN_INSTANCE_NAME}_StandardFilterElementGet(uint8_t filterNumber, can_mram_sidfe_registers_t *stdMsgIDFilterElement)

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
bool ${CAN_INSTANCE_NAME}_StandardFilterElementGet(uint8_t filterNumber, can_mram_sidfe_registers_t *stdMsgIDFilterElement)
{
    bool retval = false;
    if (!((filterNumber > ${FILTERS_STD}U) || (stdMsgIDFilterElement == NULL)))
    {
        stdMsgIDFilterElement->CAN_S0 = ${CAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.stdMsgIDFilterAddress[filterNumber - 1U].CAN_S0;
        retval = true;
    }
    return retval;
}
</#if>

<#if FILTERS_EXT?number gt 0>
// *****************************************************************************
/* Function:
    bool ${CAN_INSTANCE_NAME}_ExtendedFilterElementSet(uint8_t filterNumber, can_mram_xidfe_registers_t *extMsgIDFilterElement)

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
bool ${CAN_INSTANCE_NAME}_ExtendedFilterElementSet(uint8_t filterNumber, can_mram_xidfe_registers_t *extMsgIDFilterElement)
{
    bool retval = false;
    if (!((filterNumber > ${FILTERS_EXT}U) || (extMsgIDFilterElement == NULL)))
    {
        ${CAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.extMsgIDFilterAddress[filterNumber - 1U].CAN_F0 = extMsgIDFilterElement->CAN_F0;
        ${CAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.extMsgIDFilterAddress[filterNumber - 1U].CAN_F1 = extMsgIDFilterElement->CAN_F1;
        retval = true;
    }

    return retval;
}

// *****************************************************************************
/* Function:
    bool ${CAN_INSTANCE_NAME}_ExtendedFilterElementGet(uint8_t filterNumber, can_mram_xidfe_registers_t *extMsgIDFilterElement)

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
bool ${CAN_INSTANCE_NAME}_ExtendedFilterElementGet(uint8_t filterNumber, can_mram_xidfe_registers_t *extMsgIDFilterElement)
{
    bool retval = false;
    if (!((filterNumber > ${FILTERS_EXT}U) || (extMsgIDFilterElement == NULL)))
    {
        extMsgIDFilterElement->CAN_F0 = ${CAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.extMsgIDFilterAddress[filterNumber - 1U].CAN_F0;
        extMsgIDFilterElement->CAN_F1 = ${CAN_INSTANCE_NAME?lower_case}Obj.msgRAMConfig.extMsgIDFilterAddress[filterNumber - 1U].CAN_F1;
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

bool ${CAN_INSTANCE_NAME}_BitTimingCalculationGet(CAN_BIT_TIMING_SETUP *setup, CAN_BIT_TIMING *bitTiming)
{
    bool status = false;
    uint32_t numOfTimeQuanta;
    uint8_t tseg1;
    float temp1;
    float temp2;

    if ((setup != NULL) && (bitTiming != NULL))
    {
        if (setup->nominalBitTimingSet == true)
        {
            numOfTimeQuanta = ${CAN_INSTANCE_NAME}_CLOCK_FREQUENCY / (setup->nominalBitRate * ((uint32_t)setup->nominalPrescaler + 1U));
            if ((numOfTimeQuanta >= 4U) && (numOfTimeQuanta <= 385U))
            {
                if (setup->nominalSamplePoint < 50.0f)
                {
                    setup->nominalSamplePoint = 50.0f;
                }
                temp1 = (float)numOfTimeQuanta;
                temp2 = (temp1 * setup->nominalSamplePoint) / 100.0f;
                tseg1 = (uint8_t)temp2;
                bitTiming->nominalBitTiming.nominalTimeSegment2 = (uint8_t)(numOfTimeQuanta - tseg1 - 1U);
                bitTiming->nominalBitTiming.nominalTimeSegment1 = tseg1 - 2U;
                bitTiming->nominalBitTiming.nominalSJW = bitTiming->nominalBitTiming.nominalTimeSegment2;
                bitTiming->nominalBitTiming.nominalPrescaler = setup->nominalPrescaler;
                bitTiming->nominalBitTimingSet = true;
                status = true;
            }
            else
            {
                bitTiming->nominalBitTimingSet = false;
            }
        }
<#if CAN_OPMODE != "NORMAL">
        if (setup->dataBitTimingSet == true)
        {
            numOfTimeQuanta = ${CAN_INSTANCE_NAME}_CLOCK_FREQUENCY / (setup->dataBitRate * ((uint32_t)setup->dataPrescaler + 1U));
            if ((numOfTimeQuanta >= 4U) && (numOfTimeQuanta <= 49U))
            {
                if (setup->dataSamplePoint < 50.0f)
                {
                    setup->dataSamplePoint = 50.0f;
                }
                temp1 = (float)numOfTimeQuanta;
                temp2 = (temp1 * setup->dataSamplePoint) / 100.0f;
                tseg1 = (uint8_t)temp2;
                bitTiming->dataBitTiming.dataTimeSegment2 = (uint8_t)(numOfTimeQuanta - tseg1 - 1U);
                bitTiming->dataBitTiming.dataTimeSegment1 = tseg1 - 2U;
                bitTiming->dataBitTiming.dataSJW = bitTiming->dataBitTiming.dataTimeSegment2;
                bitTiming->dataBitTiming.dataPrescaler = setup->dataPrescaler;
                bitTiming->dataBitTimingSet = true;
                status = true;
            }
            else
            {
                bitTiming->dataBitTimingSet = false;
                status = false;
            }
        }
</#if>
    }

    return status;
}

bool ${CAN_INSTANCE_NAME}_BitTimingSet(CAN_BIT_TIMING *bitTiming)
{
    bool status = false;
    bool nominalBitTimingSet = false;
<#if CAN_OPMODE != "NORMAL">
    bool dataBitTimingSet = false;
</#if>

    if ((bitTiming->nominalBitTimingSet == true)
    && (bitTiming->nominalBitTiming.nominalTimeSegment1 >= 0x1U)
    && (bitTiming->nominalBitTiming.nominalTimeSegment2 <= 0x7FU)
    && (bitTiming->nominalBitTiming.nominalPrescaler <= 0x1FFU)
    && (bitTiming->nominalBitTiming.nominalSJW <= 0x7FU))
    {
        nominalBitTimingSet = true;
    }

<#if CAN_OPMODE != "NORMAL">
    if  ((bitTiming->dataBitTimingSet == true)
    &&  ((bitTiming->dataBitTiming.dataTimeSegment1 >= 0x1U) && (bitTiming->dataBitTiming.dataTimeSegment1 <= 0x1FU))
    &&  (bitTiming->dataBitTiming.dataTimeSegment2 <= 0xFU)
    &&  (bitTiming->dataBitTiming.dataPrescaler <= 0x1FU)
    &&  (bitTiming->dataBitTiming.dataSJW <= 0xFU))
    {
        dataBitTimingSet = true;
    }

</#if>
<#if CAN_OPMODE != "NORMAL">
    if ((nominalBitTimingSet == true) || (dataBitTimingSet == true))
<#else>
    if (nominalBitTimingSet == true)
</#if>
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
        if (dataBitTimingSet == true)
        {
            /* Set Data Bit Timing and Prescaler Register */
            ${CAN_INSTANCE_NAME}_REGS->CAN_DBTP = CAN_DBTP_DTSEG2(bitTiming->dataBitTiming.dataTimeSegment2) | CAN_DBTP_DTSEG1(bitTiming->dataBitTiming.dataTimeSegment1) | CAN_DBTP_DBRP(bitTiming->dataBitTiming.dataPrescaler) | CAN_DBTP_DSJW(bitTiming->dataBitTiming.dataSJW);
        }
</#if>
        if (nominalBitTimingSet == true)
        {
            /* Set Nominal Bit timing and Prescaler Register */
            ${CAN_INSTANCE_NAME}_REGS->CAN_NBTP  = CAN_NBTP_NTSEG2(bitTiming->nominalBitTiming.nominalTimeSegment2) | CAN_NBTP_NTSEG1(bitTiming->nominalBitTiming.nominalTimeSegment1) | CAN_NBTP_NBRP(bitTiming->nominalBitTiming.nominalPrescaler) | CAN_NBTP_NSJW(bitTiming->nominalBitTiming.nominalSJW);
        }

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
        status = true;
    }
    return status;
}

/*******************************************************************************
 End of File
*/
