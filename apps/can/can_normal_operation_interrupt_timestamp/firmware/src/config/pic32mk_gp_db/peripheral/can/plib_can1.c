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
#include <sys/kmem.h>
#include "plib_can1.h"

// *****************************************************************************
// *****************************************************************************
// Global Data
// *****************************************************************************
// *****************************************************************************
/* Number of configured FIFO */
#define CAN_NUM_OF_FIFO             2
/* Maximum number of CAN Message buffers in each FIFO */
#define CAN_FIFO_MESSAGE_BUFFER_MAX 32

#define CAN_CONFIGURATION_MODE      0x4
#define CAN_OPERATION_MODE          0x0
#define CAN_NUM_OF_FILTER           1
/* FIFO Offset in word (4 bytes) */
#define CAN_FIFO_OFFSET             0x10
/* Filter Offset in word (4 bytes) */
#define CAN_FILTER_OFFSET           0x4
/* Acceptance Mask Offset in word (4 bytes) */
#define CAN_ACCEPTANCE_MASK_OFFSET  0x4
#define CAN_MESSAGE_RAM_CONFIG_SIZE 2
#define CAN_MSG_IDE_MASK            0x10000000
#define CAN_MSG_SID_MASK            0x7FF
#define CAN_MSG_TIMESTAMP_MASK      0xFFFF0000
#define CAN_MSG_EID_MASK            0x1FFFFFFF
#define CAN_MSG_DLC_MASK            0xF
#define CAN_MSG_RTR_MASK            0x200
#define CAN_MSG_SRR_MASK            0x20000000

static CAN_OBJ can1Obj;
static CAN_RX_MSG can1RxMsg[CAN_NUM_OF_FIFO][CAN_FIFO_MESSAGE_BUFFER_MAX];
static CAN_CALLBACK_OBJ can1CallbackObj[CAN_NUM_OF_FIFO];
static CAN_CALLBACK_OBJ can1ErrorCallbackObj;
static CAN_TX_RX_MSG_BUFFER __attribute__((coherent, aligned(32))) can_message_buffer[CAN_MESSAGE_RAM_CONFIG_SIZE];

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
    /* Switch the CAN module ON */
    C1CONSET = _C1CON_ON_MASK;

    /* Switch the CAN module to Configuration mode. Wait until the switch is complete */
    C1CON = (C1CON & ~_C1CON_REQOP_MASK) | ((CAN_CONFIGURATION_MODE << _C1CON_REQOP_POSITION) & _C1CON_REQOP_MASK);
    while(((C1CON & _C1CON_OPMOD_MASK) >> _C1CON_OPMOD_POSITION) != CAN_CONFIGURATION_MODE);

    /* Set the Bitrate to 500 Kbps */
    C1CFG = ((4 << _C1CFG_BRP_POSITION) & _C1CFG_BRP_MASK)
                            | ((2 << _C1CFG_SJW_POSITION) & _C1CFG_SJW_MASK)
                            | ((2 << _C1CFG_SEG2PH_POSITION) & _C1CFG_SEG2PH_MASK)
                            | ((6 << _C1CFG_SEG1PH_POSITION) & _C1CFG_SEG1PH_MASK)
                            | ((0 << _C1CFG_PRSEG_POSITION) & _C1CFG_PRSEG_MASK)
                            | _C1CFG_SEG2PHTS_MASK;

    /* Set FIFO base address for all message buffers */
    C1FIFOBA = (uint32_t)KVA_TO_PA(can_message_buffer);

    /* Configure CAN FIFOs */
    C1FIFOCON0 = (((1 - 1) << _C1FIFOCON0_FSIZE_POSITION) & _C1FIFOCON0_FSIZE_MASK) | _C1FIFOCON0_TXEN_MASK | ((0x0 << _C1FIFOCON0_TXPRI_POSITION) & _C1FIFOCON0_TXPRI_MASK) | ((0x0 << _C1FIFOCON0_RTREN_POSITION) & _C1FIFOCON0_RTREN_MASK);
    C1FIFOCON1 = (((1 - 1) << _C1FIFOCON1_FSIZE_POSITION) & _C1FIFOCON1_FSIZE_MASK);

    /* Configure CAN Filters */
    C1RXF0 = (0 & CAN_MSG_SID_MASK) << _C1RXF0_SID_POSITION;
    C1FLTCON0SET = ((0x1 << _C1FLTCON0_FSEL0_POSITION) & _C1FLTCON0_FSEL0_MASK)
                                                         | ((0x0 << _C1FLTCON0_MSEL0_POSITION) & _C1FLTCON0_MSEL0_MASK)| _C1FLTCON0_FLTEN0_MASK;

    /* Configure CAN Acceptance Filter Masks */
    C1RXM0 = (0 & CAN_MSG_SID_MASK) << _C1RXM0_SID_POSITION;

    /* Enable Timestamp */
    C1CONSET = _C1CON_CANCAP_MASK;
    C1TMR = 0 & _C1TMR_CANTSPRE_MASK;

    /* Set Interrupts */
    IEC5SET = _IEC5_CAN1IE_MASK;
    C1INTSET = _C1INT_SERRIE_MASK | _C1INT_CERRIE_MASK | _C1INT_IVRIE_MASK;

    /* Initialize the CAN PLib Object */
    memset((void *)can1RxMsg, 0x00, sizeof(can1RxMsg));

    /* Switch the CAN module to CAN_OPERATION_MODE. Wait until the switch is complete */
    C1CON = (C1CON & ~_C1CON_REQOP_MASK) | ((CAN_OPERATION_MODE << _C1CON_REQOP_POSITION) & _C1CON_REQOP_MASK);
    while(((C1CON & _C1CON_OPMOD_MASK) >> _C1CON_OPMOD_POSITION) != CAN_OPERATION_MODE);
}

// *****************************************************************************
/* Function:
    bool CAN1_MessageTransmit(uint32_t id, uint8_t length, uint8_t* data, uint8_t fifoNum, CAN_MSG_TX_ATTRIBUTE msgAttr)

   Summary:
    Transmits a message into CAN bus.

   Precondition:
    CAN1_Initialize must have been called for the associated CAN instance.

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
bool CAN1_MessageTransmit(uint32_t id, uint8_t length, uint8_t* data, uint8_t fifoNum, CAN_MSG_TX_ATTRIBUTE msgAttr)
{
    CAN_TX_RX_MSG_BUFFER *txMessage = NULL;
    uint8_t count = 0;
    bool status = false;

    if ((fifoNum > (CAN_NUM_OF_FIFO - 1)) || (data == NULL))
    {
        return status;
    }

    if ((*(volatile uint32_t *)(&C1FIFOINT0 + (fifoNum * CAN_FIFO_OFFSET)) & _C1FIFOINT0_TXNFULLIF_MASK) == _C1FIFOINT0_TXNFULLIF_MASK)
    {
        txMessage = (CAN_TX_RX_MSG_BUFFER *)PA_TO_KVA1(*(volatile uint32_t *)(&C1FIFOUA0 + (fifoNum * CAN_FIFO_OFFSET)));

        /* Check the id whether it falls under SID or EID,
         * SID max limit is 0x7FF, so anything beyond that is EID */
        if (id > CAN_MSG_SID_MASK)
        {
            txMessage->msgSID = (id & CAN_MSG_EID_MASK) >> 18;
            txMessage->msgEID = ((id & 0x3FFFF) << 10) | CAN_MSG_IDE_MASK;
        }
        else
        {
            txMessage->msgSID = id;
            txMessage->msgEID = 0;
        }

        if (msgAttr == CAN_MSG_TX_REMOTE_FRAME)
        {
            txMessage->msgEID |= CAN_MSG_RTR_MASK;
        }
        else
        {
            if (length > 8)
            {
                length = 8;
            }
            txMessage->msgEID |= length;

            while(count < length)
            {
                txMessage->msgData[count++] = *data++;
            }
        }

        *(volatile uint32_t *)(&C1FIFOINT0SET + (fifoNum * CAN_FIFO_OFFSET)) = _C1FIFOINT0_TXEMPTYIE_MASK;

        /* Request the transmit */
        *(volatile uint32_t *)(&C1FIFOCON0SET + (fifoNum * CAN_FIFO_OFFSET)) = _C1FIFOCON0_UINC_MASK;
        *(volatile uint32_t *)(&C1FIFOCON0SET + (fifoNum * CAN_FIFO_OFFSET)) = _C1FIFOCON0_TXREQ_MASK;

        C1INTSET = _C1INT_TBIE_MASK;

        status = true;
    }
    return status;
}

// *****************************************************************************
/* Function:
    bool CAN1_MessageReceive(uint32_t *id, uint8_t *length, uint8_t *data, uint16_t *timestamp, uint8_t fifoNum, CAN_MSG_RX_ATTRIBUTE *msgAttr)

   Summary:
    Receives a message from CAN bus.

   Precondition:
    CAN1_Initialize must have been called for the associated CAN instance.

   Parameters:
    id          - Pointer to 11-bit / 29-bit identifier (ID) to be received.
    length      - Pointer to data length in number of bytes to be received.
    data        - Pointer to destination data buffer
    timestamp   - Pointer to Rx message timestamp, timestamp value is 0 if Timestamp is disabled in C1CON
    fifoNum     - FIFO number
    msgAttr     - Data frame or Remote frame to be received

   Returns:
    Request status.
    true  - Request was successful.
    false - Request has failed.
*/
bool CAN1_MessageReceive(uint32_t *id, uint8_t *length, uint8_t *data, uint16_t *timestamp, uint8_t fifoNum, CAN_MSG_RX_ATTRIBUTE *msgAttr)
{
    bool status = false;
    uint8_t msgIndex = 0;

    if ((fifoNum > (CAN_NUM_OF_FIFO - 1)) || (data == NULL) || (length == NULL) || (id == NULL))
    {
        return status;
    }

    msgIndex = (uint8_t)(*(volatile uint32_t *)(&C1FIFOCI0 + (fifoNum * CAN_FIFO_OFFSET)) & _C1FIFOCI0_CFIFOCI_MASK);
    can1RxMsg[fifoNum][msgIndex].id = id;
    can1RxMsg[fifoNum][msgIndex].buffer = data;
    can1RxMsg[fifoNum][msgIndex].size = length;
    can1RxMsg[fifoNum][msgIndex].timestamp = timestamp;
    can1RxMsg[fifoNum][msgIndex].msgAttr = msgAttr;
    *(volatile uint32_t *)(&C1FIFOINT0SET + (fifoNum * CAN_FIFO_OFFSET)) = _C1FIFOINT0_RXNEMPTYIE_MASK;
    C1INTSET = _C1INT_RBIE_MASK;
    status = true;

    return status;
}

// *****************************************************************************
/* Function:
    void CAN1_MessageAbort(uint8_t fifoNum)

   Summary:
    Abort request for a FIFO.

   Precondition:
    CAN1_Initialize must have been called for the associated CAN instance.

   Parameters:
    fifoNum - FIFO number

   Returns:
    None.
*/
void CAN1_MessageAbort(uint8_t fifoNum)
{
    if (fifoNum > (CAN_NUM_OF_FIFO - 1))
    {
        return;
    }
    *(volatile uint32_t *)(&C1FIFOCON0CLR + (fifoNum * CAN_FIFO_OFFSET)) = _C1FIFOCON0_TXREQ_MASK;
}

// *****************************************************************************
/* Function:
    void CAN1_MessageAcceptanceFilterSet(uint8_t filterNum, uint32_t id)

   Summary:
    Set Message acceptance filter configuration.

   Precondition:
    CAN1_Initialize must have been called for the associated CAN instance.

   Parameters:
    filterNum - Filter number
    id        - 11-bit or 29-bit identifier

   Returns:
    None.
*/
void CAN1_MessageAcceptanceFilterSet(uint8_t filterNum, uint32_t id)
{
    uint32_t filterEnableBit = 0;
    uint8_t filterRegIndex = 0;

    if (filterNum < CAN_NUM_OF_FILTER)
    {
        filterRegIndex = filterNum >> 2;
        filterEnableBit = (filterNum % 4 == 0)? _C1FLTCON0_FLTEN0_MASK : 1 << ((((filterNum % 4) + 1) * 8) - 1);

        *(volatile uint32_t *)(&C1FLTCON0CLR + (filterRegIndex * CAN_FILTER_OFFSET)) = filterEnableBit;

        if (id > CAN_MSG_SID_MASK)
        {
            *(volatile uint32_t *)(&C1RXF0 + (filterNum * CAN_FILTER_OFFSET)) = (id & _C1RXF0_EID_MASK)
                                                                           | (((id & 0x1FFC0000u) >> 18) << _C1RXF0_SID_POSITION)
                                                                           | _C1RXF0_EXID_MASK;
        }
        else
        {
            *(volatile uint32_t *)(&C1RXF0 + (filterNum * CAN_FILTER_OFFSET)) = (id & CAN_MSG_SID_MASK) << _C1RXF0_SID_POSITION;
        }
        *(volatile uint32_t *)(&C1FLTCON0SET + (filterRegIndex * CAN_FILTER_OFFSET)) = filterEnableBit;
    }
}

// *****************************************************************************
/* Function:
    uint32_t CAN1_MessageAcceptanceFilterGet(uint8_t filterNum)

   Summary:
    Get Message acceptance filter configuration.

   Precondition:
    CAN1_Initialize must have been called for the associated CAN instance.

   Parameters:
    filterNum - Filter number

   Returns:
    Returns Message acceptance filter identifier
*/
uint32_t CAN1_MessageAcceptanceFilterGet(uint8_t filterNum)
{
    uint32_t id = 0;

    if (filterNum < CAN_NUM_OF_FILTER)
    {
        if (*(volatile uint32_t *)(&C1RXF0 + (filterNum * CAN_FILTER_OFFSET)) & _C1RXF0_EXID_MASK)
        {
            id = (*(volatile uint32_t *)(&C1RXF0 + (filterNum * CAN_FILTER_OFFSET)) & _C1RXF0_EID_MASK)
               | ((*(volatile uint32_t *)(&C1RXF0 + (filterNum * CAN_FILTER_OFFSET)) & _C1RXF0_SID_MASK) >> 3);
        }
        else
        {
            id = (*(volatile uint32_t *)(&C1RXF0 + (filterNum * CAN_FILTER_OFFSET)) & _C1RXF0_SID_MASK) >> _C1RXF0_SID_POSITION;
        }
    }
    return id;
}

// *****************************************************************************
/* Function:
    void CAN1_MessageAcceptanceFilterMaskSet(uint8_t acceptanceFilterMaskNum, uint32_t id)

   Summary:
    Set Message acceptance filter mask configuration.

   Precondition:
    CAN1_Initialize must have been called for the associated CAN instance.

   Parameters:
    acceptanceFilterMaskNum - Acceptance Filter Mask number (0 to 3)
    id                      - 11-bit or 29-bit identifier

   Returns:
    None.
*/
void CAN1_MessageAcceptanceFilterMaskSet(uint8_t acceptanceFilterMaskNum, uint32_t id)
{
    /* Switch the CAN module to Configuration mode. Wait until the switch is complete */
    C1CON = (C1CON & ~_C1CON_REQOP_MASK) | ((CAN_CONFIGURATION_MODE << _C1CON_REQOP_POSITION) & _C1CON_REQOP_MASK);
    while(((C1CON & _C1CON_OPMOD_MASK) >> _C1CON_OPMOD_POSITION) != CAN_CONFIGURATION_MODE);

    if (id > CAN_MSG_SID_MASK)
    {
        *(volatile uint32_t *)(&C1RXM0 + (acceptanceFilterMaskNum * CAN_ACCEPTANCE_MASK_OFFSET)) = (id & _C1RXM0_EID_MASK)
                                                                       | (((id & 0x1FFC0000u) >> 18) << _C1RXM0_SID_POSITION) | _C1RXM0_MIDE_MASK;
    }
    else
    {
        *(volatile uint32_t *)(&C1RXM0 + (acceptanceFilterMaskNum * CAN_ACCEPTANCE_MASK_OFFSET)) = (id & CAN_MSG_SID_MASK) << _C1RXM0_SID_POSITION;
    }

    /* Switch the CAN module to CAN_OPERATION_MODE. Wait until the switch is complete */
    C1CON = (C1CON & ~_C1CON_REQOP_MASK) | ((CAN_OPERATION_MODE << _C1CON_REQOP_POSITION) & _C1CON_REQOP_MASK);
    while(((C1CON & _C1CON_OPMOD_MASK) >> _C1CON_OPMOD_POSITION) != CAN_OPERATION_MODE);
}

// *****************************************************************************
/* Function:
    uint32_t CAN1_MessageAcceptanceFilterMaskGet(uint8_t acceptanceFilterMaskNum)

   Summary:
    Get Message acceptance filter mask configuration.

   Precondition:
    CAN1_Initialize must have been called for the associated CAN instance.

   Parameters:
    acceptanceFilterMaskNum - Acceptance Filter Mask number (0 to 3)

   Returns:
    Returns Message acceptance filter mask.
*/
uint32_t CAN1_MessageAcceptanceFilterMaskGet(uint8_t acceptanceFilterMaskNum)
{
    uint32_t id = 0;

    if (*(volatile uint32_t *)(&C1RXM0 + (acceptanceFilterMaskNum * CAN_ACCEPTANCE_MASK_OFFSET)) & _C1RXM0_MIDE_MASK)
    {
        id = (*(volatile uint32_t *)(&C1RXM0 + (acceptanceFilterMaskNum * CAN_ACCEPTANCE_MASK_OFFSET)) & _C1RXM0_EID_MASK)
           | ((*(volatile uint32_t *)(&C1RXM0 + (acceptanceFilterMaskNum * CAN_ACCEPTANCE_MASK_OFFSET)) & _C1RXM0_SID_MASK) >> 3);
    }
    else
    {
        id = (*(volatile uint32_t *)(&C1RXM0 + (acceptanceFilterMaskNum * CAN_ACCEPTANCE_MASK_OFFSET)) & _C1RXM0_SID_MASK) >> _C1RXM0_SID_POSITION;
    }
    return id;
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
    return (CAN_ERROR)can1Obj.errorStatus;
}

// *****************************************************************************
/* Function:
    void CAN1_ErrorCountGet(uint8_t *txErrorCount, uint8_t *rxErrorCount)

   Summary:
    Returns the transmit and receive error count during transfer.

   Precondition:
    CAN1_Initialize must have been called for the associated CAN instance.

   Parameters:
    txErrorCount - Transmit Error Count to be received
    rxErrorCount - Receive Error Count to be received

   Returns:
    None.
*/
void CAN1_ErrorCountGet(uint8_t *txErrorCount, uint8_t *rxErrorCount)
{
    *txErrorCount = (uint8_t)((C1TREC & _C1TREC_TERRCNT_MASK) >> _C1TREC_TERRCNT_POSITION);
    *rxErrorCount = (uint8_t)(C1TREC & _C1TREC_RERRCNT_MASK);
}

// *****************************************************************************
/* Function:
    bool CAN1_InterruptGet(uint8_t fifoNum, CAN_FIFO_INTERRUPT_FLAG_MASK fifoInterruptFlagMask)

   Summary:
    Returns the FIFO Interrupt status.

   Precondition:
    CAN1_Initialize must have been called for the associated CAN instance.

   Parameters:
    fifoNum               - FIFO number
    fifoInterruptFlagMask - FIFO interrupt flag mask

   Returns:
    true - Requested fifo interrupt is occurred.
    false - Requested fifo interrupt is not occurred.
*/
bool CAN1_InterruptGet(uint8_t fifoNum, CAN_FIFO_INTERRUPT_FLAG_MASK fifoInterruptFlagMask)
{
    if (fifoNum > (CAN_NUM_OF_FIFO - 1))
    {
        return false;
    }
    return ((*(volatile uint32_t *)(&C1FIFOINT0 + (fifoNum * CAN_FIFO_OFFSET)) & fifoInterruptFlagMask) != 0x0);
}

// *****************************************************************************
/* Function:
    bool CAN1_TxFIFOIsFull(uint8_t fifoNum)

   Summary:
    Returns true if Tx FIFO is full otherwise false.

   Precondition:
    CAN1_Initialize must have been called for the associated CAN instance.

   Parameters:
    fifoNum - FIFO number

   Returns:
    true  - Tx FIFO is full.
    false - Tx FIFO is not full.
*/
bool CAN1_TxFIFOIsFull(uint8_t fifoNum)
{
    return ((*(volatile uint32_t *)(&C1FIFOINT0 + (fifoNum * CAN_FIFO_OFFSET)) & _C1FIFOINT0_TXNFULLIF_MASK) != _C1FIFOINT0_TXNFULLIF_MASK);
}

// *****************************************************************************
/* Function:
    bool CAN1_AutoRTRResponseSet(uint32_t id, uint8_t length, uint8_t* data, uint8_t fifoNum)

   Summary:
    Set the Auto RTR response for remote transmit request.

   Precondition:
    CAN1_Initialize must have been called for the associated CAN instance.
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
bool CAN1_AutoRTRResponseSet(uint32_t id, uint8_t length, uint8_t* data, uint8_t fifoNum)
{
    CAN_TX_RX_MSG_BUFFER *txMessage = NULL;
    uint8_t count = 0;
    bool status = false;

    if ((*(volatile uint32_t *)(&C1FIFOINT0 + (fifoNum * CAN_FIFO_OFFSET)) & _C1FIFOINT0_TXNFULLIF_MASK) == _C1FIFOINT0_TXNFULLIF_MASK)
    {
        txMessage = (CAN_TX_RX_MSG_BUFFER *)PA_TO_KVA1(*(volatile uint32_t *)(&C1FIFOUA0 + (fifoNum * CAN_FIFO_OFFSET)));

        /* Check the id whether it falls under SID or EID,
         * SID max limit is 0x7FF, so anything beyond that is EID */
        if (id > CAN_MSG_SID_MASK)
        {
            txMessage->msgSID = (id & CAN_MSG_EID_MASK) >> 18;
            txMessage->msgEID = ((id & 0x3FFFF) << 10) | CAN_MSG_IDE_MASK;
        }
        else
        {
            txMessage->msgSID = id;
            txMessage->msgEID = 0;
        }

        if (length > 8)
        {
            length = 8;
        }
        txMessage->msgEID |= length;

        while(count < length)
        {
            txMessage->msgData[count++] = *data++;
        }

        *(volatile uint32_t *)(&C1FIFOINT0SET + (fifoNum * CAN_FIFO_OFFSET)) = _C1FIFOINT0_TXEMPTYIE_MASK;

        /* Set UINC to respond to RTR */
        *(volatile uint32_t *)(&C1FIFOCON0SET + (fifoNum * CAN_FIFO_OFFSET)) = _C1FIFOCON0_UINC_MASK;

        C1INTSET = _C1INT_TBIE_MASK;

        status = true;
    }
    return status;
}

// *****************************************************************************
/* Function:
    void CAN1_CallbackRegister(CAN_CALLBACK callback, uintptr_t contextHandle, uint8_t fifoNum)

   Summary:
    Sets the pointer to the function (and it's context) to be called when the
    given CAN's transfer events occur.

   Precondition:
    CAN1_Initialize must have been called for the associated CAN instance.

   Parameters:
    callback - A pointer to a function with a calling signature defined
    by the CAN_CALLBACK data type.

    fifoNum - Tx/Rx FIFO number

    context - A value (usually a pointer) passed (unused) into the function
    identified by the callback parameter.

   Returns:
    None.
*/
void CAN1_CallbackRegister(CAN_CALLBACK callback, uintptr_t contextHandle, uint8_t fifoNum)
{
    if (callback == NULL)
    {
        return;
    }

    can1CallbackObj[fifoNum].callback = callback;
    can1CallbackObj[fifoNum].context = contextHandle;
}

// *****************************************************************************
/* Function:
    void CAN1_ErrorCallbackRegister(CAN_CALLBACK callback, uintptr_t contextHandle)

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
void CAN1_ErrorCallbackRegister(CAN_CALLBACK callback, uintptr_t contextHandle)
{
    if (callback == NULL)
    {
        return;
    }

    can1ErrorCallbackObj.callback = callback;
    can1ErrorCallbackObj.context = contextHandle;
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
    uint8_t  msgIndex = 0;
    uint8_t  fifoNum = 0;
    uint8_t  fifoSize = 0;
    uint8_t  count = 0;
    CAN_TX_RX_MSG_BUFFER *rxMessage = NULL;
    uint32_t interruptStatus = 0;

    interruptStatus = C1INT;
    /* Check if error occurred */
    if (interruptStatus & (_C1INT_SERRIF_MASK | _C1INT_CERRIF_MASK | _C1INT_IVRIF_MASK))
    {
        C1INTCLR = _C1INT_SERRIE_MASK | _C1INT_CERRIE_MASK | _C1INT_IVRIE_MASK
                 | _C1INT_SERRIF_MASK | _C1INT_CERRIF_MASK | _C1INT_IVRIF_MASK;
        IFS5CLR = _IFS5_CAN1IF_MASK;
        C1INTSET = _C1INT_SERRIE_MASK | _C1INT_CERRIE_MASK | _C1INT_IVRIE_MASK;
        uint32_t errorStatus = C1TREC;

        /* Check if error occurred */
        can1Obj.errorStatus = ((errorStatus & _C1TREC_EWARN_MASK) |
                                                          (errorStatus & _C1TREC_RXWARN_MASK) |
                                                          (errorStatus & _C1TREC_TXWARN_MASK) |
                                                          (errorStatus & _C1TREC_RXBP_MASK) |
                                                          (errorStatus & _C1TREC_TXBP_MASK) |
                                                          (errorStatus & _C1TREC_TXBO_MASK));

        /* Client must call CAN1_ErrorGet and CAN1_ErrorCountGet functions to get errors */
        if (can1ErrorCallbackObj.callback != NULL)
        {
            can1ErrorCallbackObj.callback(can1ErrorCallbackObj.context);
        }
    }
    else
    {
        can1Obj.errorStatus = 0;
        if (C1INT & _C1INT_RBIF_MASK)
        {
            fifoNum = (uint8_t)C1VEC & _C1VEC_ICODE_MASK;
            if (fifoNum < CAN_NUM_OF_FIFO)
            {
                *(volatile uint32_t *)(&C1FIFOINT0CLR + (fifoNum * CAN_FIFO_OFFSET)) = _C1FIFOINT0_RXNEMPTYIE_MASK;
                IFS5CLR = _IFS5_CAN1IF_MASK;
                fifoSize = (*(volatile uint32_t *)(&C1FIFOCON0 + (fifoNum * CAN_FIFO_OFFSET)) & _C1FIFOCON0_FSIZE_MASK) >> _C1FIFOCON0_FSIZE_POSITION;
                for (msgIndex = 0; msgIndex <= fifoSize; msgIndex++)
                {
                    /* Get a pointer to RX message buffer */
                    rxMessage = (CAN_TX_RX_MSG_BUFFER *)PA_TO_KVA1(*(volatile uint32_t *)(&C1FIFOUA0 + (fifoNum * CAN_FIFO_OFFSET)));

                    if (can1RxMsg[fifoNum][msgIndex].buffer != NULL)
                    {
                        /* Check if it's a extended message type */
                        if (rxMessage->msgEID & CAN_MSG_IDE_MASK)
                        {
                            *can1RxMsg[fifoNum][msgIndex].id = ((rxMessage->msgSID & CAN_MSG_SID_MASK) << 18) | ((rxMessage->msgEID >> 10) & _C1RXM0_EID_MASK);
                            if (rxMessage->msgEID & CAN_MSG_RTR_MASK)
                            {
                                *can1RxMsg[fifoNum][msgIndex].msgAttr = CAN_MSG_RX_REMOTE_FRAME;
                            }
                            else
                            {
                                *can1RxMsg[fifoNum][msgIndex].msgAttr = CAN_MSG_RX_DATA_FRAME;
                            }
                        }
                        else
                        {
                            *can1RxMsg[fifoNum][msgIndex].id = rxMessage->msgSID & CAN_MSG_SID_MASK;
                            if (rxMessage->msgEID & CAN_MSG_SRR_MASK)
                            {
                                *can1RxMsg[fifoNum][msgIndex].msgAttr = CAN_MSG_RX_REMOTE_FRAME;
                            }
                            else
                            {
                                *can1RxMsg[fifoNum][msgIndex].msgAttr = CAN_MSG_RX_DATA_FRAME;
                            }
                        }

                        *can1RxMsg[fifoNum][msgIndex].size = rxMessage->msgEID & CAN_MSG_DLC_MASK;

                        /* Copy the data into the payload */
                        while (count < *can1RxMsg[fifoNum][msgIndex].size)
                        {
                            *can1RxMsg[fifoNum][msgIndex].buffer++ = rxMessage->msgData[count++];
                        }

                        if (can1RxMsg[fifoNum][msgIndex].timestamp != NULL)
                        {
                            *can1RxMsg[fifoNum][msgIndex].timestamp = (rxMessage->msgSID & CAN_MSG_TIMESTAMP_MASK) >> 16;
                        }
                    }
                    /* Message processing is done, update the message buffer pointer. */
                    *(volatile uint32_t *)(&C1FIFOCON0SET + (fifoNum * CAN_FIFO_OFFSET)) = _C1FIFOCON0_UINC_MASK;
                }
            }
            C1INTCLR = _C1INT_RBIF_MASK | _C1INT_RBIE_MASK;
            if (can1CallbackObj[fifoNum].callback != NULL)
            {
                can1CallbackObj[fifoNum].callback(can1CallbackObj[fifoNum].context);
            }
        }
        if (C1INT & _C1INT_TBIF_MASK)
        {
            fifoNum = (uint8_t)C1VEC & _C1VEC_ICODE_MASK;
            if (fifoNum < CAN_NUM_OF_FIFO)
            {
                *(volatile uint32_t *)(&C1FIFOINT0CLR + (fifoNum * CAN_FIFO_OFFSET)) = _C1FIFOINT0_TXEMPTYIE_MASK;
            }
            IFS5CLR = _IFS5_CAN1IF_MASK;
            C1INTCLR = _C1INT_TBIF_MASK | _C1INT_TBIE_MASK;
            if (can1CallbackObj[fifoNum].callback != NULL)
            {
                can1CallbackObj[fifoNum].callback(can1CallbackObj[fifoNum].context);
            }
        }
    }
}
