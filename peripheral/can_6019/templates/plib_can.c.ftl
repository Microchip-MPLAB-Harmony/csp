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
#define BYTE_MASK  (0xFFU)
<#if INTERRUPT_MODE == true>
volatile static CAN_OBJ ${CAN_INSTANCE_NAME?lower_case}Obj;
</#if>
static const uint32_t can_mb_number = CAN_MB_NUMBER;
<#if INTERRUPT_MODE == true>

static inline void ${CAN_INSTANCE_NAME}_ZeroInitialize(volatile void* pData, size_t dataSize)
{
    volatile uint8_t* data = (volatile uint8_t*)pData;
    for (uint32_t index = 0; index < dataSize; index++)
    {
        data[index] = 0U;
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
    /* Disable CAN Controller */
    ${CAN_INSTANCE_NAME}_REGS->CAN_MR &= ~CAN_MR_CANEN_Msk;

    /* Set CAN Baudrate */
    ${CAN_INSTANCE_NAME}_REGS->CAN_BR  = CAN_BR_PHASE2(${CAN_PHASE2}) | CAN_BR_PHASE1(${CAN_PHASE1}) |
                                         CAN_BR_PROPAG(${CAN_PROPAG}) | CAN_BR_BRP(${BRP}) |
                                         CAN_BR_SJW(${CAN_SJW})<#if CAN_CFG_SMP == "1"> | CAN_BR_SMP_Msk</#if>;

    /* Configure Mailbox */
    <#list 0..(NUMBER_OF_MAILBOX-1) as mailbox>
    <#assign MMR_MOT = "CAN_MMR" + mailbox + "_MOT">
    <#assign MID_ID = "CAN_MID" + mailbox + "_ID_DECIMAL">
    <#assign MAM_ID = "CAN_MAM" + mailbox + "_ID_DECIMAL">
    ${CAN_INSTANCE_NAME}_REGS->CAN_IDR = CAN_IDR_MB${mailbox}_Msk;
    ${CAN_INSTANCE_NAME}_REGS->CAN_MB[${mailbox}].CAN_MCR = 0;
    <#if .vars[MMR_MOT] == "MB_RX" || .vars[MMR_MOT] == "MB_RX_OVERWRITE" || .vars[MMR_MOT] == "MB_CONSUMER">
    ${CAN_INSTANCE_NAME}_REGS->CAN_MB[${mailbox}].CAN_MID = ${(.vars[MID_ID]?number > 2047)?then('${.vars[MID_ID]}', 'CAN_MID_MIDvA(${.vars[MID_ID]})')} | CAN_MID_MIDE_Msk;
    ${CAN_INSTANCE_NAME}_REGS->CAN_MB[${mailbox}].CAN_MAM = ${(.vars[MAM_ID]?number > 2047)?then('${.vars[MAM_ID]}U | CAN_MAM_MIDE_Msk', 'CAN_MAM_MIDvA(${.vars[MAM_ID]})')};
    </#if>
    ${CAN_INSTANCE_NAME}_REGS->CAN_MB[${mailbox}].CAN_MMR = CAN_MMR_MOT_${.vars[MMR_MOT]};
    </#list>
<#if INTERRUPT_MODE == true>

    /* Enable CAN interrupts */
    ${CAN_INSTANCE_NAME}_REGS->CAN_IER = CAN_IER_CERR_Msk | CAN_IER_SERR_Msk |
                                         CAN_IER_AERR_Msk | CAN_IER_FERR_Msk |
                                         CAN_IER_BERR_Msk;

    // Initialize the CAN PLib Object
    ${CAN_INSTANCE_NAME}_ZeroInitialize(${CAN_INSTANCE_NAME?lower_case}Obj.rxMsg, sizeof(${CAN_INSTANCE_NAME?lower_case}Obj.rxMsg));
    ${CAN_INSTANCE_NAME}_ZeroInitialize(${CAN_INSTANCE_NAME?lower_case}Obj.mbState, sizeof(${CAN_INSTANCE_NAME?lower_case}Obj.mbState));
</#if>

<#if TIMESTAMP_ENABLE>
    /* Enable Timestamp */
    ${CAN_INSTANCE_NAME}_REGS->CAN_MR &= ~CAN_MR_TTM_Msk;

</#if>
    /* Enable CAN Controller */
    ${CAN_INSTANCE_NAME}_REGS->CAN_MR |= <#if TIMESTAMP_EOF_MODE == true>CAN_MR_TEOF_Msk | </#if>CAN_MR_CANEN_Msk;
}

// *****************************************************************************
/* Function:
    bool ${CAN_INSTANCE_NAME}_MessageTransmit(uint32_t id, uint8_t length, uint8_t* data, CAN_MAILBOX_TX_ATTRIBUTE mailboxAttr)

   Summary:
    Transmits a message into CAN bus.

   Precondition:
    ${CAN_INSTANCE_NAME}_Initialize must have been called for the associated CAN instance.

   Parameters:
    id          - 11-bit / 29-bit identifier (ID).
    length      - length of data buffer in number of bytes.
    data        - pointer to source data buffer
    mailboxAttr - Mailbox type TX Mailbox or Consumer Mailbox or Producer Mailbox

   Returns:
    Request status.
    true  - Request was successful.
    false - Request has failed.
*/

/* MISRA C-2012 Rule 16.1, 16.3 and 16.6 deviated below. Deviation record ID -
   H3_MISRAC_2012_R_16_1_DR_1, H3_MISRAC_2012_R_16_3_DR_1 & H3_MISRAC_2012_R_16_6_DR_1*/
<#if core.COVERITY_SUPPRESS_DEVIATION?? && core.COVERITY_SUPPRESS_DEVIATION>
<#if core.COMPILER_CHOICE == "XC32">
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wunknown-pragmas"
</#if>
#pragma coverity compliance block \
(deviate:2 "MISRA C-2012 Rule 16.1" "H3_MISRAC_2012_R_16_1_DR_1" )\
(deviate:2 "MISRA C-2012 Rule 16.3" "H3_MISRAC_2012_R_16_3_DR_1" )\
(deviate:1 "MISRA C-2012 Rule 16.6" "H3_MISRAC_2012_R_16_6_DR_1" )
</#if>

bool ${CAN_INSTANCE_NAME}_MessageTransmit(uint32_t id, uint8_t length, uint8_t* data, CAN_MAILBOX_TX_ATTRIBUTE mailboxAttr)
{
    uint8_t mailbox = 0;
    bool mbIsReady = false;
    uint8_t dataIndex = 0;
    bool status = false;

    for (mailbox = 0U; mailbox < can_mb_number; mailbox++)
    {
        switch (${CAN_INSTANCE_NAME}_REGS->CAN_MB[mailbox].CAN_MMR & CAN_MMR_MOT_Msk)
        {
            case CAN_MMR_MOT_MB_TX:
                if ((mailboxAttr == CAN_MAILBOX_DATA_FRAME_TX) &&
                   ((${CAN_INSTANCE_NAME}_REGS->CAN_MB[mailbox].CAN_MSR & CAN_MSR_MRDY_Msk) == CAN_MSR_MRDY_Msk))
                {
                    mbIsReady = true;
                }
                break;
            case CAN_MMR_MOT_MB_PRODUCER:
                if ((mailboxAttr == CAN_MAILBOX_DATA_FRAME_PRODUCER) &&
                   ((${CAN_INSTANCE_NAME}_REGS->CAN_MB[mailbox].CAN_MSR & CAN_MSR_MRDY_Msk) == CAN_MSR_MRDY_Msk))
                {
                    mbIsReady = true;
                }
                break;
            case CAN_MMR_MOT_MB_CONSUMER:
                if (mailboxAttr == CAN_MAILBOX_REMOTE_FRAME_CONSUMER)
                {
                    mbIsReady = true;
                }
                break;
            default:
                     /* Do Nothing */
                break;
        }
        if (mbIsReady)
        {
            break;
        }
    }

    if (!mbIsReady)
    {
        return status;
    }

    /* If the id is longer than 11 bits, it is considered as extended identifier */
    if (id > (CAN_MID_MIDvA_Msk >> CAN_MID_MIDvA_Pos))
    {
        /* An extended identifier is stored into ID */
        ${CAN_INSTANCE_NAME}_REGS->CAN_MB[mailbox].CAN_MID = (id & CAN_MFID_Msk) | CAN_MID_MIDE_Msk;
    }
    else
    {
        /* A standard identifier is stored into MID[28:18] */
        ${CAN_INSTANCE_NAME}_REGS->CAN_MB[mailbox].CAN_MID = CAN_MID_MIDvA(id);
    }

    /* Limit length */
    if (length > 8U)
    {
        length = 8U;
    }
    ${CAN_INSTANCE_NAME}_REGS->CAN_MB[mailbox].CAN_MCR = CAN_MCR_MDLC(length);

    switch (mailboxAttr)
    {
        case CAN_MAILBOX_DATA_FRAME_TX:
        case CAN_MAILBOX_DATA_FRAME_PRODUCER:
            /* Copy the data into the payload */
            for (; dataIndex < length; dataIndex++)
            {
                if (dataIndex == 0U)
                {
                    ${CAN_INSTANCE_NAME}_REGS->CAN_MB[mailbox].CAN_MDL = data[dataIndex];
                }
                else if (dataIndex < 4U)
                {
                    ${CAN_INSTANCE_NAME}_REGS->CAN_MB[mailbox].CAN_MDL |= ((uint32_t)data[dataIndex] << (8U * dataIndex));
                }
                else if (dataIndex == 4U)
                {
                    ${CAN_INSTANCE_NAME}_REGS->CAN_MB[mailbox].CAN_MDH = data[dataIndex];
                }
                else
                {
                    ${CAN_INSTANCE_NAME}_REGS->CAN_MB[mailbox].CAN_MDH |= ((uint32_t)data[dataIndex] << (8U * (dataIndex - 4U)));
                }
            }
            status = true;
            break;
        case CAN_MAILBOX_REMOTE_FRAME_CONSUMER:
            status = true;
            break;
        default:
            return status;
    }

    /* Request the transmit */
    ${CAN_INSTANCE_NAME}_REGS->CAN_TCR = 1UL << mailbox;
<#if INTERRUPT_MODE == true>
    ${CAN_INSTANCE_NAME}_REGS->CAN_IER = 1UL << mailbox;
</#if>
    return status;
}

// *****************************************************************************
/* Function:
    bool ${CAN_INSTANCE_NAME}_MessageReceive(uint32_t *id, uint8_t *length, uint8_t *data, uint16_t *timestamp,
                                             CAN_MAILBOX_RX_ATTRIBUTE mailboxAttr, CAN_MSG_RX_ATTRIBUTE *msgAttr)

   Summary:
    Receives a message from CAN bus.

   Precondition:
    ${CAN_INSTANCE_NAME}_Initialize must have been called for the associated CAN instance.

   Parameters:
    id          - Pointer to 11-bit / 29-bit identifier (ID) to be received.
    length      - Pointer to data length in number of bytes to be received.
    data        - pointer to destination data buffer
    timestamp   - Pointer to Rx message timestamp
    mailboxAttr - Mailbox type either RX Mailbox or RX Mailbox with overwrite
    msgAttr     - Data frame or Remote frame to be received

   Returns:
    Request status.
    true  - Request was successful.
    false - Request has failed.
*/
bool ${CAN_INSTANCE_NAME}_MessageReceive(uint32_t *id, uint8_t *length, uint8_t *data, uint16_t *timestamp,
                                         CAN_MAILBOX_RX_ATTRIBUTE mailboxAttr, CAN_MSG_RX_ATTRIBUTE *msgAttr)
{
    uint8_t mailbox = 0;
    bool mbIsReady = false;
<#if INTERRUPT_MODE == false>
    uint8_t dataIndex = 0;
</#if>
    bool status = false;
    for (mailbox = 0U; mailbox < can_mb_number; mailbox++)
    {
<#if INTERRUPT_MODE == false>
        if ((${CAN_INSTANCE_NAME}_REGS->CAN_MB[mailbox].CAN_MSR & CAN_MSR_MRDY_Msk) != CAN_MSR_MRDY_Msk)
        {
            continue;
        }
</#if>

        switch (${CAN_INSTANCE_NAME}_REGS->CAN_MB[mailbox].CAN_MMR & CAN_MMR_MOT_Msk)
        {
            case CAN_MMR_MOT_MB_RX:
<#if INTERRUPT_MODE == false>
                if (mailboxAttr == CAN_MAILBOX_DATA_FRAME_RX)
<#else>
                if ((${CAN_INSTANCE_NAME?lower_case}Obj.mbState[mailbox] == CAN_MAILBOX_READY) &&
                    (mailboxAttr == CAN_MAILBOX_DATA_FRAME_RX) )
</#if>
                {
                    mbIsReady = true;
                }
                break;
            case CAN_MMR_MOT_MB_RX_OVERWRITE:
<#if INTERRUPT_MODE == false>
                if (mailboxAttr == CAN_MAILBOX_DATA_FRAME_RX_OVERWRITE)
<#else>
                if ((${CAN_INSTANCE_NAME?lower_case}Obj.mbState[mailbox] == CAN_MAILBOX_READY) &&
                    (mailboxAttr == CAN_MAILBOX_DATA_FRAME_RX_OVERWRITE))
</#if>
                {
                    mbIsReady = true;
                }
                break;
            case CAN_MMR_MOT_MB_CONSUMER:
<#if INTERRUPT_MODE == false>
                if (mailboxAttr == CAN_MAILBOX_DATA_FRAME_CONSUMER)
<#else>
                if ((${CAN_INSTANCE_NAME?lower_case}Obj.mbState[mailbox] == CAN_MAILBOX_READY) &&
                    (mailboxAttr == CAN_MAILBOX_DATA_FRAME_CONSUMER))
</#if>
                {
                    mbIsReady = true;
                }
                break;
            default:
                      /* Do Nothing */
                break;
        }
        if (mbIsReady)
        {
            break;
        }
    }

    if (!mbIsReady)
    {
        return status;
    }

    switch (mailboxAttr)
    {
        case CAN_MAILBOX_DATA_FRAME_RX:
        case CAN_MAILBOX_DATA_FRAME_RX_OVERWRITE:
        case CAN_MAILBOX_DATA_FRAME_CONSUMER:
<#if INTERRUPT_MODE == false>
            if ((${CAN_INSTANCE_NAME}_REGS->CAN_MB[mailbox].CAN_MID & CAN_MID_MIDE_Msk) == CAN_MID_MIDE_Msk)
            {
                *id = ${CAN_INSTANCE_NAME}_REGS->CAN_MB[mailbox].CAN_MID & CAN_MFID_Msk;
            }
            else
            {
                *id = (${CAN_INSTANCE_NAME}_REGS->CAN_MB[mailbox].CAN_MID & CAN_MID_MIDvA_Msk) >> CAN_MID_MIDvA_Pos;
            }

            if (((${CAN_INSTANCE_NAME}_REGS->CAN_MB[mailbox].CAN_MSR & CAN_MSR_MRTR_Msk) != 0U) &&
               (mailboxAttr != CAN_MAILBOX_DATA_FRAME_CONSUMER))
            {
                *msgAttr = CAN_MSG_RX_REMOTE_FRAME;
            }
            else
            {
                *msgAttr = CAN_MSG_RX_DATA_FRAME;
            }

            *length = (uint8_t)((${CAN_INSTANCE_NAME}_REGS->CAN_MB[mailbox].CAN_MSR & CAN_MSR_MDLC_Msk) >> CAN_MSR_MDLC_Pos);
            /* Copy the data into the payload */
            for (; dataIndex < *length; dataIndex++)
            {
                if (dataIndex == 0U)
                {
                    data[dataIndex] = (uint8_t)(${CAN_INSTANCE_NAME}_REGS->CAN_MB[mailbox].CAN_MDL & BYTE_MASK);
                }
                else if (dataIndex < 4U)
                {
                    data[dataIndex] = (uint8_t)((${CAN_INSTANCE_NAME}_REGS->CAN_MB[mailbox].CAN_MDL >> (8U * dataIndex)) & BYTE_MASK);
                }
                else if (dataIndex == 4U)
                {
                    data[dataIndex] = (uint8_t)(${CAN_INSTANCE_NAME}_REGS->CAN_MB[mailbox].CAN_MDH & BYTE_MASK);
                }
                else
                {
                    data[dataIndex] = (uint8_t)((${CAN_INSTANCE_NAME}_REGS->CAN_MB[mailbox].CAN_MDH >> (8U * (dataIndex - 4U))) & BYTE_MASK);
                }
            }

<#if TIMESTAMP_ENABLE>
            /* Get timestamp from received message */
            if (timestamp != NULL)
            {
                *timestamp = (uint16_t)(${CAN_INSTANCE_NAME}_REGS->CAN_MB[mailbox].CAN_MSR & CAN_MSR_MTIMESTAMP_Msk);
            }

</#if>
            ${CAN_INSTANCE_NAME}_REGS->CAN_MB[mailbox].CAN_MCR = CAN_MCR_MTCR_Msk;
            status = true;
<#else>
            /* To satisfy the MISRA C 2012*/
</#if>
            break;
        default:
            return status;
    }
<#if INTERRUPT_MODE == true>
    status = true;
    ${CAN_INSTANCE_NAME?lower_case}Obj.mbState[mailbox] = CAN_MAILBOX_BUSY;
    ${CAN_INSTANCE_NAME?lower_case}Obj.rxMsg[mailbox].id = id;
    ${CAN_INSTANCE_NAME?lower_case}Obj.rxMsg[mailbox].buffer = data;
    ${CAN_INSTANCE_NAME?lower_case}Obj.rxMsg[mailbox].size = length;
    ${CAN_INSTANCE_NAME?lower_case}Obj.rxMsg[mailbox].timestamp = timestamp;
    ${CAN_INSTANCE_NAME?lower_case}Obj.rxMsg[mailbox].msgAttr = msgAttr;
    ${CAN_INSTANCE_NAME}_REGS->CAN_IER = 1UL << mailbox;
</#if>
    return status;
}

<#if core.COVERITY_SUPPRESS_DEVIATION?? && core.COVERITY_SUPPRESS_DEVIATION>
#pragma coverity compliance end_block "MISRA C-2012 Rule 16.1"
#pragma coverity compliance end_block "MISRA C-2012 Rule 16.3"
#pragma coverity compliance end_block "MISRA C-2012 Rule 16.6"
<#if core.COMPILER_CHOICE == "XC32">
#pragma GCC diagnostic pop
</#if>
</#if>
/* MISRAC 2012 deviation block end */

// *****************************************************************************
/* Function:
    void ${CAN_INSTANCE_NAME}_MessageAbort(CAN_MAILBOX_MASK mailboxMask)

   Summary:
    Abort request for a Mailbox.

   Precondition:
    ${CAN_INSTANCE_NAME}_Initialize must have been called for the associated CAN instance.

   Parameters:
    mailboxMask - Mailbox mask

   Returns:
    None.
*/
void ${CAN_INSTANCE_NAME}_MessageAbort(CAN_MAILBOX_MASK mailboxMask)
{
    ${CAN_INSTANCE_NAME}_REGS->CAN_ACR = mailboxMask;
}

// *****************************************************************************
/* Function:
    void ${CAN_INSTANCE_NAME}_MessageIDSet(CAN_MAILBOX_NUM mailbox, uint32_t id)

   Summary:
    Set Message ID in mailbox.

   Precondition:
    ${CAN_INSTANCE_NAME}_Initialize must have been called for the associated CAN instance.

   Parameters:
    mailbox - Mailbox number
    id      - 11-bit or 29-bit identifier

   Returns:
    None.
*/
void ${CAN_INSTANCE_NAME}_MessageIDSet(CAN_MAILBOX_NUM mailbox, uint32_t id)
{
    if (id > (CAN_MID_MIDvA_Msk >> CAN_MID_MIDvA_Pos))
    {
        ${CAN_INSTANCE_NAME}_REGS->CAN_MB[mailbox].CAN_MID = (id & CAN_MFID_Msk) | CAN_MID_MIDE_Msk;
    }
    else
    {
        ${CAN_INSTANCE_NAME}_REGS->CAN_MB[mailbox].CAN_MID = CAN_MID_MIDvA(id) | CAN_MID_MIDE_Msk;
    }
}

// *****************************************************************************
/* Function:
    uint32_t ${CAN_INSTANCE_NAME}_MessageIDGet(CAN_MAILBOX_NUM mailbox)

   Summary:
    Get Message ID from mailbox.

   Precondition:
    ${CAN_INSTANCE_NAME}_Initialize must have been called for the associated CAN instance.

   Parameters:
    mailbox - Mailbox number

   Returns:
    Returns Message ID
*/
uint32_t ${CAN_INSTANCE_NAME}_MessageIDGet(CAN_MAILBOX_NUM mailbox)
{
    uint32_t id = 0;

    if ((${CAN_INSTANCE_NAME}_REGS->CAN_MB[mailbox].CAN_MID & CAN_MID_MIDvB_Msk) != 0U)
    {
        id = ${CAN_INSTANCE_NAME}_REGS->CAN_MB[mailbox].CAN_MID & CAN_MFID_Msk;
    }
    else
    {
        id = (${CAN_INSTANCE_NAME}_REGS->CAN_MB[mailbox].CAN_MID & CAN_MID_MIDvA_Msk) >> CAN_MID_MIDvA_Pos;
    }
    return id;
}

// *****************************************************************************
/* Function:
    void ${CAN_INSTANCE_NAME}_MessageAcceptanceMaskSet(CAN_MAILBOX_NUM mailbox, uint32_t id)

   Summary:
    Set Message acceptance identifier mask in mailbox.

   Precondition:
    ${CAN_INSTANCE_NAME}_Initialize must have been called for the associated CAN instance.

   Parameters:
    mailbox - Mailbox number
    id      - 11-bit or 29-bit identifier

   Returns:
    None.
*/
void ${CAN_INSTANCE_NAME}_MessageAcceptanceMaskSet(CAN_MAILBOX_NUM mailbox, uint32_t id)
{
    if (id > (CAN_MAM_MIDvA_Msk >> CAN_MAM_MIDvA_Pos))
    {
        ${CAN_INSTANCE_NAME}_REGS->CAN_MB[mailbox].CAN_MAM = (id & CAN_MFID_Msk) | CAN_MAM_MIDE_Msk;
    }
    else
    {
        ${CAN_INSTANCE_NAME}_REGS->CAN_MB[mailbox].CAN_MAM = CAN_MAM_MIDvA(id);
    }
}

// *****************************************************************************
/* Function:
    uint32_t ${CAN_INSTANCE_NAME}_MessageAcceptanceMaskGet(CAN_MAILBOX_NUM mailbox)

   Summary:
    Get Message acceptance identifier mask from mailbox.

   Precondition:
    ${CAN_INSTANCE_NAME}_Initialize must have been called for the associated CAN instance.

   Parameters:
    mailbox - Mailbox number

   Returns:
    Returns Message acceptance identifier mask
*/
uint32_t ${CAN_INSTANCE_NAME}_MessageAcceptanceMaskGet(CAN_MAILBOX_NUM mailbox)
{
    uint32_t id = 0;

    if ((${CAN_INSTANCE_NAME}_REGS->CAN_MB[mailbox].CAN_MAM & CAN_MAM_MIDE_Msk) == CAN_MAM_MIDE_Msk)
    {
        id = ${CAN_INSTANCE_NAME}_REGS->CAN_MB[mailbox].CAN_MAM & CAN_MFID_Msk;
    }
    else
    {
        id = (${CAN_INSTANCE_NAME}_REGS->CAN_MB[mailbox].CAN_MAM & CAN_MAM_MIDvA_Msk) >> CAN_MAM_MIDvA_Pos;
    }
    return id;
}

// *****************************************************************************
/* Function:
    uint16_t ${CAN_INSTANCE_NAME}_MessageTimestampGet(CAN_MAILBOX_NUM mailbox)

   Summary:
    Get the message timestamp from a mailbox.

   Precondition:
    ${CAN_INSTANCE_NAME}_Initialize must have been called for the associated CAN instance.

   Parameters:
    mailbox - Mailbox number

   Returns:
    Returns the message timestamp from a mailbox.
*/
uint16_t ${CAN_INSTANCE_NAME}_MessageTimestampGet(CAN_MAILBOX_NUM mailbox)
{
    return (uint16_t)(${CAN_INSTANCE_NAME}_REGS->CAN_MB[mailbox].CAN_MSR & CAN_MSR_MTIMESTAMP_Msk);
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
<#if INTERRUPT_MODE == false>
    CAN_ERROR error = CAN_ERROR_NONE;
    uint32_t errorStatus = ${CAN_INSTANCE_NAME}_REGS->CAN_SR;

    /* Check if error occurred */
    error = (CAN_ERROR)((errorStatus & CAN_SR_BOFF_Msk) |
                        (errorStatus & CAN_SR_CERR_Msk) |
                        (errorStatus & CAN_SR_SERR_Msk) |
                        (errorStatus & CAN_SR_AERR_Msk) |
                        (errorStatus & CAN_SR_FERR_Msk) |
                        (errorStatus & CAN_SR_BERR_Msk));

</#if>
<#if INTERRUPT_MODE == false>
    if ((errorStatus & CAN_SR_BOFF_Msk) == CAN_SR_BOFF_Msk)
<#else>
    if ((${CAN_INSTANCE_NAME?lower_case}Obj.errorStatus & CAN_SR_BOFF_Msk) == CAN_SR_BOFF_Msk)
</#if>
    {
        /* Reset CAN Controller if Bus off */
        ${CAN_INSTANCE_NAME}_REGS->CAN_MR &= ~CAN_MR_CANEN_Msk;
        ${CAN_INSTANCE_NAME}_REGS->CAN_MR |= CAN_MR_CANEN_Msk;
    }

<#if INTERRUPT_MODE == false>
    return error;
<#else>
    return (CAN_ERROR)${CAN_INSTANCE_NAME?lower_case}Obj.errorStatus;
</#if>
}

// *****************************************************************************
/* Function:
    void ${CAN_INSTANCE_NAME}_ErrorCountGet(uint16_t *txErrorCount, uint8_t *rxErrorCount)

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
void ${CAN_INSTANCE_NAME}_ErrorCountGet(uint16_t *txErrorCount, uint8_t *rxErrorCount)
{
    *txErrorCount = (uint16_t)((${CAN_INSTANCE_NAME}_REGS->CAN_ECR & CAN_ECR_TEC_Msk) >> CAN_ECR_TEC_Pos);
    *rxErrorCount = (uint8_t)(${CAN_INSTANCE_NAME}_REGS->CAN_ECR & CAN_ECR_REC_Msk);
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
    return ((${CAN_INSTANCE_NAME}_REGS->CAN_SR & interruptMask) != 0x0U);
}

// *****************************************************************************
/* Function:
    void ${CAN_INSTANCE_NAME}_InterruptEnable(CAN_INTERRUPT_MASK interruptMask)

   Summary:
    Enables CAN Interrupt.

   Precondition:
    ${CAN_INSTANCE_NAME}_Initialize must have been called for the associated CAN instance.

   Parameters:
    interruptMask - Interrupt to be enabled

   Returns:
    None
*/
void ${CAN_INSTANCE_NAME}_InterruptEnable(CAN_INTERRUPT_MASK interruptMask)
{
    ${CAN_INSTANCE_NAME}_REGS->CAN_IER = interruptMask;
}

// *****************************************************************************
/* Function:
    void ${CAN_INSTANCE_NAME}_InterruptDisable(CAN_INTERRUPT_MASK interruptMask)

   Summary:
    Disables CAN Interrupt.

   Precondition:
    ${CAN_INSTANCE_NAME}_Initialize must have been called for the associated CAN instance.

   Parameters:
    interruptMask - Interrupt to be disabled

   Returns:
    None
*/
void ${CAN_INSTANCE_NAME}_InterruptDisable(CAN_INTERRUPT_MASK interruptMask)
{
    ${CAN_INSTANCE_NAME}_REGS->CAN_IDR = interruptMask;
}

// *****************************************************************************
/* Function:
    bool ${CAN_INSTANCE_NAME}_MailboxIsReady(CAN_MAILBOX_NUM mailbox)

   Summary:
    Returns true if Mailbox is ready otherwise false.

   Precondition:
    ${CAN_INSTANCE_NAME}_Initialize must have been called for the associated CAN instance.

   Parameters:
    mailbox - Mailbox number

   Returns:
    true  - Mailbox is ready and Mailbox data registers can be read/written.
    false - Mailbox is not ready and Mailbox data registers can not be read/written.
*/
bool ${CAN_INSTANCE_NAME}_MailboxIsReady(CAN_MAILBOX_NUM mailbox)
{
    return ((${CAN_INSTANCE_NAME}_REGS->CAN_MB[mailbox].CAN_MSR & CAN_MSR_MRDY_Msk) == CAN_MSR_MRDY_Msk);
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
            numOfTimeQuanta = ${CAN_INSTANCE_NAME}_CLOCK_FREQUENCY / (setup->nominalBitRate * ((uint32_t)setup->nominalPrescaler + 1U));
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
    && ((bitTiming->nominalBitTiming.Prescaler >= 0x1U) && (bitTiming->nominalBitTiming.Prescaler <= 0x7FU))
    && (bitTiming->nominalBitTiming.sjw <= 0x3U))
    {
        /* Disable CAN Controller */
        ${CAN_INSTANCE_NAME}_REGS->CAN_MR &= ~CAN_MR_CANEN_Msk;

        /* Set CAN Baudrate */
        ${CAN_INSTANCE_NAME}_REGS->CAN_BR  = CAN_BR_PHASE2(bitTiming->nominalBitTiming.phase2Segment) | CAN_BR_PHASE1(bitTiming->nominalBitTiming.phase1Segment) |
                                             CAN_BR_PROPAG(bitTiming->nominalBitTiming.propagationSegment) | CAN_BR_BRP(bitTiming->nominalBitTiming.Prescaler) |
                                             CAN_BR_SJW(bitTiming->nominalBitTiming.sjw)<#if CAN_CFG_SMP == "1"> | CAN_BR_SMP_Msk</#if>;

        /* Enable CAN Controller */
        ${CAN_INSTANCE_NAME}_REGS->CAN_MR |= CAN_MR_CANEN_Msk;

        status = true;
    }
    return status;
}

<#if INTERRUPT_MODE == true>
// *****************************************************************************
/* Function:
    bool ${CAN_INSTANCE_NAME}_TxCallbackRegister(CAN_CALLBACK callback, uintptr_t contextHandle, CAN_MAILBOX_TX_ATTRIBUTE mailboxAttr)

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

    mailboxAttr - Mailbox type TX Mailbox or Consumer Mailbox or Producer Mailbox

   Returns:
    Request status.
    true  - Request was successful.
    false - Request has failed.
*/
bool ${CAN_INSTANCE_NAME}_TxCallbackRegister(CAN_CALLBACK callback, uintptr_t contextHandle, CAN_MAILBOX_TX_ATTRIBUTE mailboxAttr)
{
    uint8_t mailbox = 0;
    bool mbIsReady = false;

    if (callback == NULL)
    {
        return false;
    }

    for (mailbox = 0; mailbox < can_mb_number; mailbox++)
    {
        switch (${CAN_INSTANCE_NAME}_REGS->CAN_MB[mailbox].CAN_MMR & CAN_MMR_MOT_Msk)
        {
            case CAN_MMR_MOT_MB_TX:
                if ((mailboxAttr == CAN_MAILBOX_DATA_FRAME_TX) &&
                   ((${CAN_INSTANCE_NAME}_REGS->CAN_MB[mailbox].CAN_MSR & CAN_MSR_MRDY_Msk) == CAN_MSR_MRDY_Msk))
                {
                    mbIsReady = true;
                }
                break;
            case CAN_MMR_MOT_MB_PRODUCER:
                if ((mailboxAttr == CAN_MAILBOX_DATA_FRAME_PRODUCER) &&
                   ((${CAN_INSTANCE_NAME}_REGS->CAN_MB[mailbox].CAN_MSR & CAN_MSR_MRDY_Msk) == CAN_MSR_MRDY_Msk))
                {
                    mbIsReady = true;
                }
                break;
            case CAN_MMR_MOT_MB_CONSUMER:
                if (mailboxAttr == CAN_MAILBOX_REMOTE_FRAME_CONSUMER)
                {
                    mbIsReady = true;
                }
                break;
            default:
                     /* Do Nothing */
                break;
        }
        if (mbIsReady)
        {

            break;
        }
    }

    if (!mbIsReady)
    {
        return false;
    }

    ${CAN_INSTANCE_NAME?lower_case}Obj.mbCallback[mailbox].callback = callback;
    ${CAN_INSTANCE_NAME?lower_case}Obj.mbCallback[mailbox].context = contextHandle;
    return true;
}

// *****************************************************************************
/* Function:
    bool ${CAN_INSTANCE_NAME}_RxCallbackRegister(CAN_CALLBACK callback, uintptr_t contextHandle, CAN_MAILBOX_RX_ATTRIBUTE mailboxAttr)

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

    mailboxAttr - Mailbox type either RX Mailbox or RX Mailbox with overwrite

   Returns:
    None.
*/
bool ${CAN_INSTANCE_NAME}_RxCallbackRegister(CAN_CALLBACK callback, uintptr_t contextHandle, CAN_MAILBOX_RX_ATTRIBUTE mailboxAttr)
{
    uint8_t mailbox = 0;
    bool mbIsReady = false;

    if (callback == NULL)
    {
        return false;
    }

    for (mailbox = 0U; mailbox < can_mb_number; mailbox++)
    {
        switch (${CAN_INSTANCE_NAME}_REGS->CAN_MB[mailbox].CAN_MMR & CAN_MMR_MOT_Msk)
        {
            case CAN_MMR_MOT_MB_RX:
                if ((${CAN_INSTANCE_NAME?lower_case}Obj.mbState[mailbox] == CAN_MAILBOX_READY) &&
                    (mailboxAttr == CAN_MAILBOX_DATA_FRAME_RX))
                {
                    mbIsReady = true;
                }
                break;
            case CAN_MMR_MOT_MB_RX_OVERWRITE:
                if ((${CAN_INSTANCE_NAME?lower_case}Obj.mbState[mailbox] == CAN_MAILBOX_READY) &&
                    (mailboxAttr == CAN_MAILBOX_DATA_FRAME_RX_OVERWRITE))
                {
                    mbIsReady = true;
                }
                break;
            case CAN_MMR_MOT_MB_CONSUMER:
                if ((${CAN_INSTANCE_NAME?lower_case}Obj.mbState[mailbox] == CAN_MAILBOX_READY) &&
                    (mailboxAttr == CAN_MAILBOX_DATA_FRAME_CONSUMER))
                {
                    mbIsReady = true;
                }
                break;
            default:
                      /* Do Nothing */
                break;
        }
        if (mbIsReady)
        {
            break;
        }
    }

    if (!mbIsReady)
    {
        return false;
    }

    ${CAN_INSTANCE_NAME?lower_case}Obj.mbCallback[mailbox].callback = callback;
    ${CAN_INSTANCE_NAME?lower_case}Obj.mbCallback[mailbox].context = contextHandle;
    return true;
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
void __attribute__((used)) ${CAN_INSTANCE_NAME}_InterruptHandler(void)
{
    uint32_t interruptStatus = ${CAN_INSTANCE_NAME}_REGS->CAN_SR;
    uint8_t dataIndex;

    /* Additional temporary variable used to prevent MISRA violations (Rule 13.x) */
    uintptr_t context;

    /* Check if error occurred */
    if ((interruptStatus &
       (CAN_SR_BOFF_Msk | CAN_SR_CERR_Msk | CAN_SR_SERR_Msk |
        CAN_SR_AERR_Msk | CAN_SR_FERR_Msk | CAN_SR_BERR_Msk)) != 0U)
    {
        /* App must call ${CAN_INSTANCE_NAME}_ErrorGet function to get errors */
        ${CAN_INSTANCE_NAME?lower_case}Obj.errorStatus = ((interruptStatus & CAN_SR_BOFF_Msk) |
                                                          (interruptStatus & CAN_SR_CERR_Msk) |
                                                          (interruptStatus & CAN_SR_SERR_Msk) |
                                                          (interruptStatus & CAN_SR_AERR_Msk) |
                                                          (interruptStatus & CAN_SR_FERR_Msk) |
                                                          (interruptStatus & CAN_SR_BERR_Msk));
    }
    else
    {
        ${CAN_INSTANCE_NAME?lower_case}Obj.errorStatus = 0;
        for (uint8_t mailbox = 0U; mailbox < can_mb_number; mailbox++)
        {
            if ((${CAN_INSTANCE_NAME}_REGS->CAN_MB[mailbox].CAN_MSR & CAN_MSR_MRDY_Msk) == CAN_MSR_MRDY_Msk)
            {
                switch (${CAN_INSTANCE_NAME}_REGS->CAN_MB[mailbox].CAN_MMR & CAN_MMR_MOT_Msk)
                {
                    case CAN_MMR_MOT_MB_RX:
                    case CAN_MMR_MOT_MB_RX_OVERWRITE:
                    case CAN_MMR_MOT_MB_CONSUMER:
                        ${CAN_INSTANCE_NAME}_REGS->CAN_IDR = 1UL << mailbox;
                        if (${CAN_INSTANCE_NAME?lower_case}Obj.rxMsg[mailbox].buffer != NULL)
                        {
                            if ((${CAN_INSTANCE_NAME}_REGS->CAN_MB[mailbox].CAN_MID & CAN_MID_MIDE_Msk) == CAN_MID_MIDE_Msk)
                            {
                                *${CAN_INSTANCE_NAME?lower_case}Obj.rxMsg[mailbox].id = ${CAN_INSTANCE_NAME}_REGS->CAN_MB[mailbox].CAN_MID & CAN_MFID_Msk;
                            }
                            else
                            {
                                *${CAN_INSTANCE_NAME?lower_case}Obj.rxMsg[mailbox].id = (${CAN_INSTANCE_NAME}_REGS->CAN_MB[mailbox].CAN_MID & CAN_MID_MIDvA_Msk) >> CAN_MID_MIDvA_Pos;
                            }

                            if (((${CAN_INSTANCE_NAME}_REGS->CAN_MB[mailbox].CAN_MSR & CAN_MSR_MRTR_Msk) != 0U) &&
                               ((${CAN_INSTANCE_NAME}_REGS->CAN_MB[mailbox].CAN_MMR & CAN_MMR_MOT_Msk) != CAN_MMR_MOT_MB_CONSUMER))
                            {
                                *${CAN_INSTANCE_NAME?lower_case}Obj.rxMsg[mailbox].msgAttr = CAN_MSG_RX_REMOTE_FRAME;
                            }
                            else
                            {
                                *${CAN_INSTANCE_NAME?lower_case}Obj.rxMsg[mailbox].msgAttr = CAN_MSG_RX_DATA_FRAME;
                            }

                            *${CAN_INSTANCE_NAME?lower_case}Obj.rxMsg[mailbox].size = (uint8_t)((${CAN_INSTANCE_NAME}_REGS->CAN_MB[mailbox].CAN_MSR & CAN_MSR_MDLC_Msk) >> CAN_MSR_MDLC_Pos);
                            /* Copy the data into the payload */
                            dataIndex = 0U;
                            while (dataIndex < *${CAN_INSTANCE_NAME?lower_case}Obj.rxMsg[mailbox].size)
                            {
                                if (dataIndex == 0U)
                                {
                                    ${CAN_INSTANCE_NAME?lower_case}Obj.rxMsg[mailbox].buffer[dataIndex] = (uint8_t)(${CAN_INSTANCE_NAME}_REGS->CAN_MB[mailbox].CAN_MDL & BYTE_MASK);
                                }
                                else if (dataIndex < 4U)
                                {
                                    ${CAN_INSTANCE_NAME?lower_case}Obj.rxMsg[mailbox].buffer[dataIndex] =(uint8_t)((${CAN_INSTANCE_NAME}_REGS->CAN_MB[mailbox].CAN_MDL >> (8U * dataIndex)) & BYTE_MASK);
                                }
                                else if (dataIndex == 4U)
                                {
                                    ${CAN_INSTANCE_NAME?lower_case}Obj.rxMsg[mailbox].buffer[dataIndex] = (uint8_t)(${CAN_INSTANCE_NAME}_REGS->CAN_MB[mailbox].CAN_MDH & BYTE_MASK);
                                }
                                else
                                {
                                    ${CAN_INSTANCE_NAME?lower_case}Obj.rxMsg[mailbox].buffer[dataIndex] = (uint8_t)(${CAN_INSTANCE_NAME}_REGS->CAN_MB[mailbox].CAN_MDH >> (8U * (dataIndex - 4U)) & BYTE_MASK);
                                }
                                dataIndex++;
                            }
                            <#if TIMESTAMP_ENABLE>
                            /* Get timestamp from received message */
                            if (${CAN_INSTANCE_NAME?lower_case}Obj.rxMsg[mailbox].timestamp != NULL)
                            {
                                *${CAN_INSTANCE_NAME?lower_case}Obj.rxMsg[mailbox].timestamp = (uint16_t)(${CAN_INSTANCE_NAME}_REGS->CAN_MB[mailbox].CAN_MSR & CAN_MSR_MTIMESTAMP_Msk);
                            }
                            </#if>
                        }
                        ${CAN_INSTANCE_NAME}_REGS->CAN_MB[mailbox].CAN_MCR = CAN_MCR_MTCR_Msk;
                        ${CAN_INSTANCE_NAME?lower_case}Obj.mbState[mailbox] = CAN_MAILBOX_READY;
                        if (${CAN_INSTANCE_NAME?lower_case}Obj.mbCallback[mailbox].callback != NULL)
                        {
                            context = ${CAN_INSTANCE_NAME?lower_case}Obj.mbCallback[mailbox].context;
                            ${CAN_INSTANCE_NAME?lower_case}Obj.mbCallback[mailbox].callback(context);
                        }
                        break;
                    case CAN_MMR_MOT_MB_TX:
                    case CAN_MMR_MOT_MB_PRODUCER:
                        ${CAN_INSTANCE_NAME}_REGS->CAN_IDR = 1UL << mailbox;
                        if (${CAN_INSTANCE_NAME?lower_case}Obj.mbCallback[mailbox].callback != NULL)
                        {
                            context = ${CAN_INSTANCE_NAME?lower_case}Obj.mbCallback[mailbox].context;
                            ${CAN_INSTANCE_NAME?lower_case}Obj.mbCallback[mailbox].callback(context);
                        }
                        break;
                    default:
                             /* Do Nothing */
                        break;
                }
            }
        }
    }
}
</#if>
