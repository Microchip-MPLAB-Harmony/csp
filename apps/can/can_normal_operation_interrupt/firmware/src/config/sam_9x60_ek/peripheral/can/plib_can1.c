/*******************************************************************************
  Controller Area Network (CAN) Peripheral Library Source File

  Company:
    Microchip Technology Inc.

  File Name:
    plib_can1.c

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

#include "plib_can1.h"

// *****************************************************************************
// *****************************************************************************
// Global Data
// *****************************************************************************
// *****************************************************************************

#define BYTE_MASK 0xFF
static CAN_OBJ can1Obj;

// *****************************************************************************
// *****************************************************************************
// CAN1 PLib Interface Routines
// *****************************************************************************
// *****************************************************************************
// *****************************************************************************
/* Function:
    void CAN1_Initialize(void)

   Summary:
    Initializes given instance of the CAN peripheral.

   Precondition:
    None.

   Parameters:
    None.

   Returns:
    None
*/
void CAN1_Initialize(void)
{
    /* Disable CAN Controller */
    CAN1_REGS->CAN_MR &= ~CAN_MR_CANEN_Msk;

    /* Set CAN Baudrate */
    CAN1_REGS->CAN_BR  = CAN_BR_PHASE2(3) | CAN_BR_PHASE1(7) |
                                         CAN_BR_PROPAG(2) | CAN_BR_BRP(24) |
                                         CAN_BR_SJW(3);

    /* Configure Mailbox */
    CAN1_REGS->CAN_IDR = CAN_IDR_MB0_Msk;
    CAN1_REGS->CAN_MB[0].CAN_MCR = 0;
    CAN1_REGS->CAN_MB[0].CAN_MMR = CAN_MMR_MOT_MB_TX;
    CAN1_REGS->CAN_IDR = CAN_IDR_MB1_Msk;
    CAN1_REGS->CAN_MB[1].CAN_MCR = 0;
    CAN1_REGS->CAN_MB[1].CAN_MAM = CAN_MAM_MIDvA(0);
    CAN1_REGS->CAN_MB[1].CAN_MMR = CAN_MMR_MOT_MB_RX_OVERWRITE;
    CAN1_REGS->CAN_IDR = CAN_IDR_MB2_Msk;
    CAN1_REGS->CAN_MB[2].CAN_MCR = 0;
    CAN1_REGS->CAN_MB[2].CAN_MMR = CAN_MMR_MOT_MB_DISABLED;
    CAN1_REGS->CAN_IDR = CAN_IDR_MB3_Msk;
    CAN1_REGS->CAN_MB[3].CAN_MCR = 0;
    CAN1_REGS->CAN_MB[3].CAN_MMR = CAN_MMR_MOT_MB_DISABLED;
    CAN1_REGS->CAN_IDR = CAN_IDR_MB4_Msk;
    CAN1_REGS->CAN_MB[4].CAN_MCR = 0;
    CAN1_REGS->CAN_MB[4].CAN_MMR = CAN_MMR_MOT_MB_DISABLED;
    CAN1_REGS->CAN_IDR = CAN_IDR_MB5_Msk;
    CAN1_REGS->CAN_MB[5].CAN_MCR = 0;
    CAN1_REGS->CAN_MB[5].CAN_MMR = CAN_MMR_MOT_MB_DISABLED;
    CAN1_REGS->CAN_IDR = CAN_IDR_MB6_Msk;
    CAN1_REGS->CAN_MB[6].CAN_MCR = 0;
    CAN1_REGS->CAN_MB[6].CAN_MMR = CAN_MMR_MOT_MB_DISABLED;
    CAN1_REGS->CAN_IDR = CAN_IDR_MB7_Msk;
    CAN1_REGS->CAN_MB[7].CAN_MCR = 0;
    CAN1_REGS->CAN_MB[7].CAN_MMR = CAN_MMR_MOT_MB_DISABLED;

    /* Enable CAN interrupts */
    CAN1_REGS->CAN_IER = CAN_IER_CERR_Msk | CAN_IER_SERR_Msk |
                                         CAN_IER_AERR_Msk | CAN_IER_FERR_Msk |
                                         CAN_IER_BERR_Msk;

    // Initialize the CAN PLib Object
    memset((void *)can1Obj.rxMsg, 0x00, sizeof(can1Obj.rxMsg));
    memset((void *)can1Obj.mbState, CAN_MAILBOX_READY, sizeof(can1Obj.mbState));
    can1Obj.state = CAN_STATE_IDLE;

    /* Enable CAN Controller */
    CAN1_REGS->CAN_MR |= CAN_MR_CANEN_Msk;
}

// *****************************************************************************
/* Function:
    bool CAN1_MessageTransmit(uint32_t id, uint8_t length, uint8_t* data, CAN_MAILBOX_TX_ATTRIBUTE mailboxAttr)

   Summary:
    Transmits a message into CAN bus.

   Precondition:
    CAN1_Initialize must have been called for the associated CAN instance.

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
bool CAN1_MessageTransmit(uint32_t id, uint8_t length, uint8_t* data, CAN_MAILBOX_TX_ATTRIBUTE mailboxAttr)
{
    uint8_t mailbox = 0;
    bool mbIsReady = false;
    uint8_t dataIndex = 0;
    bool status = false;

    for (mailbox = 0; mailbox < CAN_MB_NUMBER; mailbox++)
    {
        switch (CAN1_REGS->CAN_MB[mailbox].CAN_MMR & CAN_MMR_MOT_Msk)
        {
            case CAN_MMR_MOT_MB_TX:
                if ((mailboxAttr == CAN_MAILBOX_DATA_FRAME_TX) &&
                   ((CAN1_REGS->CAN_MB[mailbox].CAN_MSR & CAN_MSR_MRDY_Msk) == CAN_MSR_MRDY_Msk))
                {
                    mbIsReady = true;
                }
                break;
            case CAN_MMR_MOT_MB_PRODUCER:
                if ((mailboxAttr == CAN_MAILBOX_DATA_FRAME_PRODUCER) &&
                   ((CAN1_REGS->CAN_MB[mailbox].CAN_MSR & CAN_MSR_MRDY_Msk) == CAN_MSR_MRDY_Msk))
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
        CAN1_REGS->CAN_MB[mailbox].CAN_MID = (id & CAN_MFID_Msk) | CAN_MID_MIDE_Msk;
    }
    else
    {
        /* A standard identifier is stored into MID[28:18] */
        CAN1_REGS->CAN_MB[mailbox].CAN_MID = CAN_MID_MIDvA(id);
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
            CAN1_REGS->CAN_MB[mailbox].CAN_MCR = CAN_MCR_MDLC(length);
            /* Copy the data into the payload */
            for (; dataIndex < length; dataIndex++)
            {
                if (dataIndex == 0)
                {
                    CAN1_REGS->CAN_MB[mailbox].CAN_MDL = data[dataIndex];
                }
                else if (dataIndex < 4)
                {
                    CAN1_REGS->CAN_MB[mailbox].CAN_MDL |= (data[dataIndex] << (8 * dataIndex));
                }
                else if (dataIndex == 4)
                {
                    CAN1_REGS->CAN_MB[mailbox].CAN_MDH = data[dataIndex];
                }
                else
                {
                    CAN1_REGS->CAN_MB[mailbox].CAN_MDH |= (data[dataIndex] << (8 * (dataIndex - 4)));
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

    can1Obj.state = CAN_STATE_TRANSFER_TRANSMIT;

    /* Request the transmit */
    CAN1_REGS->CAN_TCR = 1U << mailbox;
    CAN1_REGS->CAN_IER = 1U << mailbox;
    return status;
}

// *****************************************************************************
/* Function:
    bool CAN1_MessageReceive(uint32_t *id, uint8_t *length, uint8_t *data, CAN_MAILBOX_RX_ATTRIBUTE mailboxAttr)

   Summary:
    Receives a message from CAN bus.

   Precondition:
    CAN1_Initialize must have been called for the associated CAN instance.

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
bool CAN1_MessageReceive(uint32_t *id, uint8_t *length, uint8_t *data, CAN_MAILBOX_RX_ATTRIBUTE mailboxAttr)
{
    uint8_t mailbox = 0;
    bool mbIsReady = false;
    bool status = false;
    for (mailbox = 0; mailbox < CAN_MB_NUMBER; mailbox++)
    {

        switch (CAN1_REGS->CAN_MB[mailbox].CAN_MMR & CAN_MMR_MOT_Msk)
        {
            case CAN_MMR_MOT_MB_RX:
                if ((mailboxAttr == CAN_MAILBOX_DATA_FRAME_RX) &&
                    (can1Obj.mbState[mailbox] == CAN_MAILBOX_READY))
                {
                    mbIsReady = true;
                }
                break;
            case CAN_MMR_MOT_MB_RX_OVERWRITE:
                if ((mailboxAttr == CAN_MAILBOX_DATA_FRAME_RX_OVERWRITE) &&
                    (can1Obj.mbState[mailbox] == CAN_MAILBOX_READY))
                {
                    mbIsReady = true;
                }
                break;
            case CAN_MMR_MOT_MB_CONSUMER:
                if ((mailboxAttr == CAN_MAILBOX_DATA_FRAME_CONSUMER) &&
                    (can1Obj.mbState[mailbox] == CAN_MAILBOX_READY))
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
            break;
        default:
            return status;
    }
    status = true;
    can1Obj.mbState[mailbox] = CAN_MAILBOX_BUSY;
    can1Obj.state = CAN_STATE_TRANSFER_RECEIVE;
    can1Obj.rxMsg[mailbox].id = id;
    can1Obj.rxMsg[mailbox].buffer = data;
    can1Obj.rxMsg[mailbox].size = length;
    CAN1_REGS->CAN_IER = 1U << mailbox;
    return status;
}

// *****************************************************************************
/* Function:
    void CAN1_MessageAbort(CAN_MAILBOX_MASK mailboxMask)

   Summary:
    Abort request for a Mailbox.

   Precondition:
    CAN1_Initialize must have been called for the associated CAN instance.

   Parameters:
    mailboxMask - Mailbox mask

   Returns:
    None.
*/
void CAN1_MessageAbort(CAN_MAILBOX_MASK mailboxMask)
{
    CAN1_REGS->CAN_ACR = mailboxMask;
}

// *****************************************************************************
/* Function:
    void CAN1_MessageAcceptanceMaskSet(CAN_MAILBOX_NUM mailbox, uint32_t id)

   Summary:
    Set Message acceptance identifier mask in mailbox.

   Precondition:
    CAN1_Initialize must have been called for the associated CAN instance.

   Parameters:
    mailbox - Mailbox number
    id      - 11-bit or 29-bit identifier

   Returns:
    None.
*/
void CAN1_MessageAcceptanceMaskSet(CAN_MAILBOX_NUM mailbox, uint32_t id)
{
    if (id > (CAN_MAM_MIDvA_Msk >> CAN_MAM_MIDvA_Pos))
    {
        CAN1_REGS->CAN_MB[mailbox].CAN_MAM = (id & CAN_MFID_Msk) | CAN_MAM_MIDE_Msk;
    }
    else
    {
        CAN1_REGS->CAN_MB[mailbox].CAN_MAM = CAN_MAM_MIDvA(id);
    }
}

// *****************************************************************************
/* Function:
    uint32_t CAN1_MessageAcceptanceMaskGet(CAN_MAILBOX_NUM mailbox)

   Summary:
    Get Message acceptance identifier mask from mailbox.

   Precondition:
    CAN1_Initialize must have been called for the associated CAN instance.

   Parameters:
    mailbox - Mailbox number

   Returns:
    Returns Message acceptance identifier mask
*/
uint32_t CAN1_MessageAcceptanceMaskGet(CAN_MAILBOX_NUM mailbox)
{
    uint32_t id = 0;

    if ((CAN1_REGS->CAN_MB[mailbox].CAN_MAM & CAN_MAM_MIDE_Msk) == CAN_MAM_MIDE_Msk)
    {
        id = CAN1_REGS->CAN_MB[mailbox].CAN_MAM & CAN_MFID_Msk;
    }
    else
    {
        id = (CAN1_REGS->CAN_MB[mailbox].CAN_MAM & CAN_MAM_MIDvA_Msk) >> CAN_MAM_MIDvA_Pos;
    }
    return id;
}

// *****************************************************************************
/* Function:
    uint16_t CAN1_MessageTimestampGet(CAN_MAILBOX_NUM mailbox)

   Summary:
    Get the message timestamp from a mailbox.

   Precondition:
    CAN1_Initialize must have been called for the associated CAN instance.

   Parameters:
    mailbox - Mailbox number

   Returns:
    Returns the message timestamp from a mailbox.
*/
uint16_t CAN1_MessageTimestampGet(CAN_MAILBOX_NUM mailbox)
{
    return (CAN1_REGS->CAN_MB[mailbox].CAN_MSR & CAN_MSR_MTIMESTAMP_Msk);
}

// *****************************************************************************
/* Function:
    CAN_ERROR CAN1_ErrorGet(void)

   Summary:
    Returns the error during transfer.

   Precondition:
    CAN1_Initialize must have been called for the associated CAN instance.

   Parameters:
    None.

   Returns:
    Error during transfer.
*/
CAN_ERROR CAN1_ErrorGet(void)
{
    if ((can1Obj.errorStatus & CAN_SR_BOFF_Msk) == CAN_SR_BOFF_Msk)
    {
        /* Reset CAN Controller if Bus off */
        CAN1_REGS->CAN_MR &= ~CAN_MR_CANEN_Msk;
        CAN1_REGS->CAN_MR |= CAN_MR_CANEN_Msk;
    }

    return (CAN_ERROR)can1Obj.errorStatus;
}

// *****************************************************************************
/* Function:
    bool CAN1_InterruptGet(CAN_INTERRUPT_MASK interruptMask)

   Summary:
    Returns the Interrupt status.

   Precondition:
    CAN1_Initialize must have been called for the associated CAN instance.

   Parameters:
    interruptMask - Interrupt source number

   Returns:
    true - Requested interrupt is occurred.
    false - Requested interrupt is not occurred.
*/
bool CAN1_InterruptGet(CAN_INTERRUPT_MASK interruptMask)
{
    return ((CAN1_REGS->CAN_SR & interruptMask) != 0x0);
}

// *****************************************************************************
/* Function:
    void CAN1_InterruptEnable(CAN_INTERRUPT_MASK interruptMask)

   Summary:
    Enables CAN Interrupt.

   Precondition:
    CAN1_Initialize must have been called for the associated CAN instance.

   Parameters:
    interruptMask - Interrupt to be enabled

   Returns:
    None
*/
void CAN1_InterruptEnable(CAN_INTERRUPT_MASK interruptMask)
{
    CAN1_REGS->CAN_IER = interruptMask;
}

// *****************************************************************************
/* Function:
    void CAN1_InterruptDisable(CAN_INTERRUPT_MASK interruptMask)

   Summary:
    Disables CAN Interrupt.

   Precondition:
    CAN1_Initialize must have been called for the associated CAN instance.

   Parameters:
    interruptMask - Interrupt to be disabled

   Returns:
    None
*/
void CAN1_InterruptDisable(CAN_INTERRUPT_MASK interruptMask)
{
    CAN1_REGS->CAN_IDR = interruptMask;
}

// *****************************************************************************
/* Function:
    bool CAN1_IsBusy(void)

   Summary:
    Returns the Peripheral busy status.

   Precondition:
    CAN1_Initialize must have been called for the associated CAN instance.

   Parameters:
    None.

   Returns:
    true - Busy.
    false - Not busy.
*/
bool CAN1_IsBusy(void)
{
    if (can1Obj.state == CAN_STATE_IDLE)
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
    void CAN1_CallbackRegister(CAN_CALLBACK callback, uintptr_t contextHandle)

   Summary:
    Sets the pointer to the function (and it's context) to be called when the
    given CAN's transfer events occur.

   Precondition:
    CAN1_Initialize must have been called for the associated CAN instance.

   Parameters:
    callback - A pointer to a function with a calling signature defined
    by the CAN_CALLBACK data type.

    context - A value (usually a pointer) passed (unused) into the function
    identified by the callback parameter.

   Returns:
    None.
*/
void CAN1_CallbackRegister(CAN_CALLBACK callback, uintptr_t contextHandle)
{
    if (callback == NULL)
    {
        return;
    }

    can1Obj.callback = callback;
    can1Obj.context = contextHandle;
}

// *****************************************************************************
/* Function:
    void CAN1_InterruptHandler(void)

   Summary:
    CAN1 Peripheral Interrupt Handler.

   Description:
    This function is CAN1 Peripheral Interrupt Handler and will
    called on every CAN1 interrupt.

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
void CAN1_InterruptHandler(void)
{
    uint32_t interruptStatus = CAN1_REGS->CAN_SR;

    /* Check if error occurred */
    if (interruptStatus &
       (CAN_SR_BOFF_Msk | CAN_SR_CERR_Msk | CAN_SR_SERR_Msk |
        CAN_SR_AERR_Msk | CAN_SR_FERR_Msk | CAN_SR_BERR_Msk))
    {
        can1Obj.errorStatus = ((interruptStatus & CAN_SR_BOFF_Msk) |
                                                          (interruptStatus & CAN_SR_CERR_Msk) |
                                                          (interruptStatus & CAN_SR_SERR_Msk) |
                                                          (interruptStatus & CAN_SR_AERR_Msk) |
                                                          (interruptStatus & CAN_SR_FERR_Msk) |
                                                          (interruptStatus & CAN_SR_BERR_Msk));
        can1Obj.state = CAN_STATE_ERROR;
        /* Client must call CAN1_ErrorGet function to get errors */
        if (can1Obj.callback != NULL)
        {
            can1Obj.callback(can1Obj.context);
            can1Obj.state = CAN_STATE_IDLE;
        }
    }
    else
    {
        can1Obj.errorStatus = 0;
        for (uint8_t mailbox = 0; mailbox < CAN_MB_NUMBER; mailbox++)
        {
            if ((CAN1_REGS->CAN_MB[mailbox].CAN_MSR & CAN_MSR_MRDY_Msk) == CAN_MSR_MRDY_Msk)
            {
                switch (CAN1_REGS->CAN_MB[mailbox].CAN_MMR & CAN_MMR_MOT_Msk)
                {
                    case CAN_MMR_MOT_MB_RX:
                    case CAN_MMR_MOT_MB_RX_OVERWRITE:
                    case CAN_MMR_MOT_MB_CONSUMER:
                        CAN1_REGS->CAN_IDR = 1U << mailbox;
                        if (can1Obj.rxMsg[mailbox].buffer != NULL)
                        {
                            if ((CAN1_REGS->CAN_MB[mailbox].CAN_MID & CAN_MID_MIDE_Msk) == CAN_MID_MIDE_Msk)
                            {
                                *can1Obj.rxMsg[mailbox].id = CAN1_REGS->CAN_MB[mailbox].CAN_MID & CAN_MFID_Msk;
                            }
                            else
                            {
                                *can1Obj.rxMsg[mailbox].id = (CAN1_REGS->CAN_MB[mailbox].CAN_MID & CAN_MID_MIDvA_Msk) >> CAN_MID_MIDvA_Pos;
                            }
                            *can1Obj.rxMsg[mailbox].size = (CAN1_REGS->CAN_MB[mailbox].CAN_MSR & CAN_MSR_MDLC_Msk) >> CAN_MSR_MDLC_Pos;
                            /* Copy the data into the payload */
                            for (uint8_t dataIndex = 0; dataIndex < *can1Obj.rxMsg[mailbox].size; dataIndex++)
                            {
                                if (dataIndex == 0)
                                {
                                    can1Obj.rxMsg[mailbox].buffer[dataIndex] = CAN1_REGS->CAN_MB[mailbox].CAN_MDL & BYTE_MASK;
                                }
                                else if (dataIndex < 4)
                                {
                                    can1Obj.rxMsg[mailbox].buffer[dataIndex] = (CAN1_REGS->CAN_MB[mailbox].CAN_MDL >> (8 * dataIndex)) & BYTE_MASK;
                                }
                                else if (dataIndex == 4)
                                {
                                    can1Obj.rxMsg[mailbox].buffer[dataIndex] = CAN1_REGS->CAN_MB[mailbox].CAN_MDH & BYTE_MASK;
                                }
                                else
                                {
                                    can1Obj.rxMsg[mailbox].buffer[dataIndex] = (CAN1_REGS->CAN_MB[mailbox].CAN_MDH >> (8 * (dataIndex - 4))) & BYTE_MASK;
                                }
                            }
                        }
                        CAN1_REGS->CAN_MB[mailbox].CAN_MCR = CAN_MCR_MTCR_Msk;
                        can1Obj.mbState[mailbox] = CAN_MAILBOX_READY;
                        can1Obj.state = CAN_STATE_TRANSFER_DONE;
                        if (can1Obj.state == CAN_STATE_TRANSFER_DONE)
                        {
                            if (can1Obj.callback != NULL)
                            {
                                can1Obj.callback(can1Obj.context);
                                can1Obj.state = CAN_STATE_IDLE;
                            }
                        }
                        break;
                    case CAN_MMR_MOT_MB_TX:
                    case CAN_MMR_MOT_MB_PRODUCER:
                        CAN1_REGS->CAN_IDR = 1U << mailbox;
                        can1Obj.state = CAN_STATE_TRANSFER_DONE;
                        if (can1Obj.state == CAN_STATE_TRANSFER_DONE)
                        {
                            if (can1Obj.callback != NULL)
                            {
                                can1Obj.callback(can1Obj.context);
                                can1Obj.state = CAN_STATE_IDLE;
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
