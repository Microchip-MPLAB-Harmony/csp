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

// *****************************************************************************
// *****************************************************************************
// Global Data
// *****************************************************************************
// *****************************************************************************

#define BYTE_MASK 0xFF
<#if INTERRUPT_MODE == true>
static CAN_OBJ ${CAN_INSTANCE_NAME?lower_case}Obj;
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
    ${CAN_INSTANCE_NAME}_REGS->CAN_BR  = CAN_BR_PHASE2(${PHASE2}) | CAN_BR_PHASE1(${PHASE1}) |
                                         CAN_BR_PROPAG(${PROPAG}) | CAN_BR_BRP(${BRP}) |
                                         CAN_BR_SJW(${SJW});

    /* Configure Mailbox */
    <#list 0..(NUMBER_OF_MAILBOX-1) as mailbox>
    <#assign MMR_MOT = "CAN_MMR" + mailbox + "_MOT">
    <#assign MAM_ID = "CAN_MAM" + mailbox + "_ID">
    ${CAN_INSTANCE_NAME}_REGS->CAN_IDR = CAN_IDR_MB${mailbox}_Msk;
    ${CAN_INSTANCE_NAME}_REGS->CAN_MB[${mailbox}].CAN_MCR = 0;
    <#if .vars[MMR_MOT] == "MB_RX" || .vars[MMR_MOT] == "MB_RX_OVERWRITE" || .vars[MMR_MOT] == "MB_CONSUMER">
    ${CAN_INSTANCE_NAME}_REGS->CAN_MB[${mailbox}].CAN_MAM = ${(.vars[MAM_ID]?number > 2047)?then('${.vars[MAM_ID]} | CAN_MAM_MIDE_Msk', 'CAN_MAM_MIDvA(${.vars[MAM_ID]})')};
    </#if>
    ${CAN_INSTANCE_NAME}_REGS->CAN_MB[${mailbox}].CAN_MMR = CAN_MMR_MOT_${.vars[MMR_MOT]};
    </#list>
<#if INTERRUPT_MODE == true>

    /* Enable CAN interrupts */
    ${CAN_INSTANCE_NAME}_REGS->CAN_IER = CAN_IER_CERR_Msk | CAN_IER_SERR_Msk |
                                         CAN_IER_AERR_Msk | CAN_IER_FERR_Msk |
                                         CAN_IER_BERR_Msk;

    // Initialize the CAN PLib Object
    memset((void *)${CAN_INSTANCE_NAME?lower_case}Obj.rxMsg, 0x00, sizeof(${CAN_INSTANCE_NAME?lower_case}Obj.rxMsg));
    memset((void *)${CAN_INSTANCE_NAME?lower_case}Obj.mbState, CAN_MAILBOX_READY, sizeof(${CAN_INSTANCE_NAME?lower_case}Obj.mbState));
    ${CAN_INSTANCE_NAME?lower_case}Obj.state = CAN_STATE_IDLE;
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
bool ${CAN_INSTANCE_NAME}_MessageTransmit(uint32_t id, uint8_t length, uint8_t* data, CAN_MAILBOX_TX_ATTRIBUTE mailboxAttr)
{
    uint8_t mailbox = 0;
    bool mbIsReady = false;
    uint8_t dataIndex = 0;
    bool status = false;

    for (mailbox = 0; mailbox < CAN_MB_NUMBER; mailbox++)
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
                break;
        }
        if (mbIsReady)
            break;
    }

    if (!mbIsReady)
        return status;

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
    switch (mailboxAttr)
    {
        case CAN_MAILBOX_DATA_FRAME_TX:
        case CAN_MAILBOX_DATA_FRAME_PRODUCER:
            /* Limit length */
            if (length > 8)
            {
                length = 8;
            }
            ${CAN_INSTANCE_NAME}_REGS->CAN_MB[mailbox].CAN_MCR = CAN_MCR_MDLC(length);
            /* Copy the data into the payload */
            for (; dataIndex < length; dataIndex++)
            {
                if (dataIndex == 0)
                {
                    ${CAN_INSTANCE_NAME}_REGS->CAN_MB[mailbox].CAN_MDL = data[dataIndex];
                }
                else if (dataIndex < 4)
                {
                    ${CAN_INSTANCE_NAME}_REGS->CAN_MB[mailbox].CAN_MDL |= (data[dataIndex] << (8 * dataIndex));
                }
                else if (dataIndex == 4)
                {
                    ${CAN_INSTANCE_NAME}_REGS->CAN_MB[mailbox].CAN_MDH = data[dataIndex];
                }
                else
                {
                    ${CAN_INSTANCE_NAME}_REGS->CAN_MB[mailbox].CAN_MDH |= (data[dataIndex] << (8 * (dataIndex - 4)));
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
<#if INTERRUPT_MODE == true>

    ${CAN_INSTANCE_NAME?lower_case}Obj.state = CAN_STATE_TRANSFER_TRANSMIT;
</#if>

    /* Request the transmit */
    ${CAN_INSTANCE_NAME}_REGS->CAN_TCR = 1U << mailbox;
<#if INTERRUPT_MODE == true>
    ${CAN_INSTANCE_NAME}_REGS->CAN_IER = 1U << mailbox;
</#if>
    return status;
}

// *****************************************************************************
/* Function:
    bool ${CAN_INSTANCE_NAME}_MessageReceive(uint32_t *id, uint8_t *length, uint8_t *data, CAN_MAILBOX_RX_ATTRIBUTE mailboxAttr)

   Summary:
    Receives a message from CAN bus.

   Precondition:
    ${CAN_INSTANCE_NAME}_Initialize must have been called for the associated CAN instance.

   Parameters:
    id          - Pointer to 11-bit / 29-bit identifier (ID) to be received.
    length      - Pointer to data length in number of bytes to be received.
    data        - pointer to destination data buffer
    mailboxAttr - Mailbox type either RX Mailbox or RX Mailbox with overwrite

   Returns:
    Request status.
    true  - Request was successful.
    false - Request has failed.
*/
bool ${CAN_INSTANCE_NAME}_MessageReceive(uint32_t *id, uint8_t *length, uint8_t *data, CAN_MAILBOX_RX_ATTRIBUTE mailboxAttr)
{
    uint8_t mailbox = 0;
    bool mbIsReady = false;
<#if INTERRUPT_MODE == false>
    uint8_t dataIndex = 0;
</#if>
    bool status = false;
    for (mailbox = 0; mailbox < CAN_MB_NUMBER; mailbox++)
    {
<#if INTERRUPT_MODE == false>
        if ((${CAN_INSTANCE_NAME}_REGS->CAN_MB[mailbox].CAN_MSR & CAN_MSR_MRDY_Msk) != CAN_MSR_MRDY_Msk)
            continue;
</#if>

        switch (${CAN_INSTANCE_NAME}_REGS->CAN_MB[mailbox].CAN_MMR & CAN_MMR_MOT_Msk)
        {
            case CAN_MMR_MOT_MB_RX:
<#if INTERRUPT_MODE == false>
                if (mailboxAttr == CAN_MAILBOX_DATA_FRAME_RX)
<#else>
                if ((mailboxAttr == CAN_MAILBOX_DATA_FRAME_RX) &&
                    (${CAN_INSTANCE_NAME?lower_case}Obj.mbState[mailbox] == CAN_MAILBOX_READY))
</#if>
                {
                    mbIsReady = true;
                }
                break;
            case CAN_MMR_MOT_MB_RX_OVERWRITE:
<#if INTERRUPT_MODE == false>
                if (mailboxAttr == CAN_MAILBOX_DATA_FRAME_RX_OVERWRITE)
<#else>
                if ((mailboxAttr == CAN_MAILBOX_DATA_FRAME_RX_OVERWRITE) &&
                    (${CAN_INSTANCE_NAME?lower_case}Obj.mbState[mailbox] == CAN_MAILBOX_READY))
</#if>
                {
                    mbIsReady = true;
                }
                break;
            case CAN_MMR_MOT_MB_CONSUMER:
<#if INTERRUPT_MODE == false>
                if (mailboxAttr == CAN_MAILBOX_DATA_FRAME_CONSUMER)
<#else>
                if ((mailboxAttr == CAN_MAILBOX_DATA_FRAME_CONSUMER) &&
                    (${CAN_INSTANCE_NAME?lower_case}Obj.mbState[mailbox] == CAN_MAILBOX_READY))
</#if>
                {
                    mbIsReady = true;
                }
                break;
            default:
                break;
        }
        if (mbIsReady)
            break;
    }

    if (!mbIsReady)
        return status;

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
            *length = (${CAN_INSTANCE_NAME}_REGS->CAN_MB[mailbox].CAN_MSR & CAN_MSR_MDLC_Msk) >> CAN_MSR_MDLC_Pos;
            /* Copy the data into the payload */
            for (; dataIndex < *length; dataIndex++)
            {
                if (dataIndex == 0)
                {
                    data[dataIndex] = ${CAN_INSTANCE_NAME}_REGS->CAN_MB[mailbox].CAN_MDL & BYTE_MASK;
                }
                else if (dataIndex < 4)
                {
                    data[dataIndex] = (${CAN_INSTANCE_NAME}_REGS->CAN_MB[mailbox].CAN_MDL >> (8 * dataIndex)) & BYTE_MASK;
                }
                else if (dataIndex == 4)
                {
                    data[dataIndex] = ${CAN_INSTANCE_NAME}_REGS->CAN_MB[mailbox].CAN_MDH & BYTE_MASK;
                }
                else
                {
                    data[dataIndex] = (${CAN_INSTANCE_NAME}_REGS->CAN_MB[mailbox].CAN_MDH >> (8 * (dataIndex - 4))) & BYTE_MASK;
                }
            }
            ${CAN_INSTANCE_NAME}_REGS->CAN_MB[mailbox].CAN_MCR = CAN_MCR_MTCR_Msk;
            status = true;
</#if>
            break;
        default:
            return status;
    }
<#if INTERRUPT_MODE == true>
    status = true;
    ${CAN_INSTANCE_NAME?lower_case}Obj.mbState[mailbox] = CAN_MAILBOX_BUSY;
    ${CAN_INSTANCE_NAME?lower_case}Obj.state = CAN_STATE_TRANSFER_RECEIVE;
    ${CAN_INSTANCE_NAME?lower_case}Obj.rxMsg[mailbox].id = id;
    ${CAN_INSTANCE_NAME?lower_case}Obj.rxMsg[mailbox].buffer = data;
    ${CAN_INSTANCE_NAME?lower_case}Obj.rxMsg[mailbox].size = length;
    ${CAN_INSTANCE_NAME}_REGS->CAN_IER = 1U << mailbox;
</#if>
    return status;
}

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
    return (${CAN_INSTANCE_NAME}_REGS->CAN_MB[mailbox].CAN_MSR & CAN_MSR_MTIMESTAMP_Msk);
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
    return ((${CAN_INSTANCE_NAME}_REGS->CAN_SR & interruptMask) != 0x0);
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
    uint32_t interruptStatus = ${CAN_INSTANCE_NAME}_REGS->CAN_SR;

    /* Check if error occurred */
    if (interruptStatus &
       (CAN_SR_BOFF_Msk | CAN_SR_CERR_Msk | CAN_SR_SERR_Msk |
        CAN_SR_AERR_Msk | CAN_SR_FERR_Msk | CAN_SR_BERR_Msk))
    {
        ${CAN_INSTANCE_NAME?lower_case}Obj.errorStatus = ((interruptStatus & CAN_SR_BOFF_Msk) |
                                                          (interruptStatus & CAN_SR_CERR_Msk) |
                                                          (interruptStatus & CAN_SR_SERR_Msk) |
                                                          (interruptStatus & CAN_SR_AERR_Msk) |
                                                          (interruptStatus & CAN_SR_FERR_Msk) |
                                                          (interruptStatus & CAN_SR_BERR_Msk));
        ${CAN_INSTANCE_NAME?lower_case}Obj.state = CAN_STATE_ERROR;
        /* Client must call ${CAN_INSTANCE_NAME}_ErrorGet function to get errors */
        if (${CAN_INSTANCE_NAME?lower_case}Obj.callback != NULL)
        {
            ${CAN_INSTANCE_NAME?lower_case}Obj.callback(${CAN_INSTANCE_NAME?lower_case}Obj.context);
            ${CAN_INSTANCE_NAME?lower_case}Obj.state = CAN_STATE_IDLE;
        }
    }
    else
    {
        ${CAN_INSTANCE_NAME?lower_case}Obj.errorStatus = 0;
        for (uint8_t mailbox = 0; mailbox < CAN_MB_NUMBER; mailbox++)
        {
            if ((${CAN_INSTANCE_NAME}_REGS->CAN_MB[mailbox].CAN_MSR & CAN_MSR_MRDY_Msk) == CAN_MSR_MRDY_Msk)
            {
                switch (${CAN_INSTANCE_NAME}_REGS->CAN_MB[mailbox].CAN_MMR & CAN_MMR_MOT_Msk)
                {
                    case CAN_MMR_MOT_MB_RX:
                    case CAN_MMR_MOT_MB_RX_OVERWRITE:
                    case CAN_MMR_MOT_MB_CONSUMER:
                        ${CAN_INSTANCE_NAME}_REGS->CAN_IDR = 1U << mailbox;
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
                            *${CAN_INSTANCE_NAME?lower_case}Obj.rxMsg[mailbox].size = (${CAN_INSTANCE_NAME}_REGS->CAN_MB[mailbox].CAN_MSR & CAN_MSR_MDLC_Msk) >> CAN_MSR_MDLC_Pos;
                            /* Copy the data into the payload */
                            for (uint8_t dataIndex = 0; dataIndex < *${CAN_INSTANCE_NAME?lower_case}Obj.rxMsg[mailbox].size; dataIndex++)
                            {
                                if (dataIndex == 0)
                                {
                                    ${CAN_INSTANCE_NAME?lower_case}Obj.rxMsg[mailbox].buffer[dataIndex] = ${CAN_INSTANCE_NAME}_REGS->CAN_MB[mailbox].CAN_MDL & BYTE_MASK;
                                }
                                else if (dataIndex < 4)
                                {
                                    ${CAN_INSTANCE_NAME?lower_case}Obj.rxMsg[mailbox].buffer[dataIndex] = (${CAN_INSTANCE_NAME}_REGS->CAN_MB[mailbox].CAN_MDL >> (8 * dataIndex)) & BYTE_MASK;
                                }
                                else if (dataIndex == 4)
                                {
                                    ${CAN_INSTANCE_NAME?lower_case}Obj.rxMsg[mailbox].buffer[dataIndex] = ${CAN_INSTANCE_NAME}_REGS->CAN_MB[mailbox].CAN_MDH & BYTE_MASK;
                                }
                                else
                                {
                                    ${CAN_INSTANCE_NAME?lower_case}Obj.rxMsg[mailbox].buffer[dataIndex] = (${CAN_INSTANCE_NAME}_REGS->CAN_MB[mailbox].CAN_MDH >> (8 * (dataIndex - 4))) & BYTE_MASK;
                                }
                            }
                        }
                        ${CAN_INSTANCE_NAME}_REGS->CAN_MB[mailbox].CAN_MCR = CAN_MCR_MTCR_Msk;
                        ${CAN_INSTANCE_NAME?lower_case}Obj.mbState[mailbox] = CAN_MAILBOX_READY;
                        ${CAN_INSTANCE_NAME?lower_case}Obj.state = CAN_STATE_TRANSFER_DONE;
                        if (${CAN_INSTANCE_NAME?lower_case}Obj.state == CAN_STATE_TRANSFER_DONE)
                        {
                            if (${CAN_INSTANCE_NAME?lower_case}Obj.callback != NULL)
                            {
                                ${CAN_INSTANCE_NAME?lower_case}Obj.callback(${CAN_INSTANCE_NAME?lower_case}Obj.context);
                                ${CAN_INSTANCE_NAME?lower_case}Obj.state = CAN_STATE_IDLE;
                            }
                        }
                        break;
                    case CAN_MMR_MOT_MB_TX:
                    case CAN_MMR_MOT_MB_PRODUCER:
                        ${CAN_INSTANCE_NAME}_REGS->CAN_IDR = 1U << mailbox;
                        ${CAN_INSTANCE_NAME?lower_case}Obj.state = CAN_STATE_TRANSFER_DONE;
                        if (${CAN_INSTANCE_NAME?lower_case}Obj.state == CAN_STATE_TRANSFER_DONE)
                        {
                            if (${CAN_INSTANCE_NAME?lower_case}Obj.callback != NULL)
                            {
                                ${CAN_INSTANCE_NAME?lower_case}Obj.callback(${CAN_INSTANCE_NAME?lower_case}Obj.context);
                                ${CAN_INSTANCE_NAME?lower_case}Obj.state = CAN_STATE_IDLE;
                            }
                        }
                        break;
                    default:
                        break;
                }
            }
        }
    }
}
</#if>
