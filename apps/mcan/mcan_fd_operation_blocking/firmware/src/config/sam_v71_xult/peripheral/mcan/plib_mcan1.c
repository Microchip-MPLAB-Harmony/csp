/*******************************************************************************
  Controller Area Network (MCAN) Peripheral Library Source File

  Company:
    Microchip Technology Inc.

  File Name:
    plib_mcan1.c

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
#include "plib_mcan1.h"

// *****************************************************************************
// *****************************************************************************
// Global Data
// *****************************************************************************
// *****************************************************************************
#define MCAN_STD_ID_Msk        0x7FF
static MCAN_OBJ mcan1Obj;

static const mcan_sidfe_registers_t mcan1StdFilter[] =
{
    {
        .MCAN_SIDFE_0 = MCAN_SIDFE_0_SFT(0) |
                  MCAN_SIDFE_0_SFID1(0x0) |
                  MCAN_SIDFE_0_SFID2(0x0) |
                  MCAN_SIDFE_0_SFEC(1)
    },
    {
        .MCAN_SIDFE_0 = MCAN_SIDFE_0_SFT(0) |
                  MCAN_SIDFE_0_SFID1(0x0) |
                  MCAN_SIDFE_0_SFID2(0x0) |
                  MCAN_SIDFE_0_SFEC(7)
    },
};

static const mcan_xidfe_registers_t mcan1ExtFilter[] =
{
    {
        .MCAN_XIDFE_0 = MCAN_XIDFE_0_EFID1(0x0) | MCAN_XIDFE_0_EFEC(7),
        .MCAN_XIDFE_1 = MCAN_XIDFE_1_EFID2(0x0) | MCAN_XIDFE_1_EFT(0),
    },
    {
        .MCAN_XIDFE_0 = MCAN_XIDFE_0_EFID1(0x0) | MCAN_XIDFE_0_EFEC(2),
        .MCAN_XIDFE_1 = MCAN_XIDFE_1_EFID2(0x0) | MCAN_XIDFE_1_EFT(0),
    },
};

/******************************************************************************
Local Functions
******************************************************************************/

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
static uint8_t MCANDlcToLengthGet(uint8_t dlc)
{
    uint8_t msgLength[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 12, 16, 20, 24, 32, 48, 64};
    return msgLength[dlc];
}

// *****************************************************************************
// *****************************************************************************
// MCAN1 PLib Interface Routines
// *****************************************************************************
// *****************************************************************************
// *****************************************************************************
/* Function:
    void MCAN1_Initialize(void)

   Summary:
    Initializes given instance of the MCAN peripheral.

   Precondition:
    None.

   Parameters:
    None.

   Returns:
    None
*/
void MCAN1_Initialize(void)
{
    /* Start MCAN initialization */
    MCAN1_REGS->MCAN_CCCR = MCAN_CCCR_INIT_ENABLED;
    while ((MCAN1_REGS->MCAN_CCCR & MCAN_CCCR_INIT_Msk) != MCAN_CCCR_INIT_Msk);

    /* Set CCE to unlock the configuration registers */
    MCAN1_REGS->MCAN_CCCR |= MCAN_CCCR_CCE_Msk;

    /* Set Data Bit Timing and Prescaler Register */
    MCAN1_REGS->MCAN_DBTP = MCAN_DBTP_DTSEG2(9) | MCAN_DBTP_DTSEG1(25) | MCAN_DBTP_DBRP(0) | MCAN_DBTP_DSJW(3);

    /* Set Nominal Bit timing and Prescaler Register */
    MCAN1_REGS->MCAN_NBTP  = MCAN_NBTP_NTSEG2(37) | MCAN_NBTP_NTSEG1(110) | MCAN_NBTP_NBRP(0) | MCAN_NBTP_NSJW(3);

    /* Receive Buffer / FIFO Element Size Configuration Register */
    MCAN1_REGS->MCAN_RXESC = 0  | MCAN_RXESC_F0DS(7) | MCAN_RXESC_F1DS(7) | MCAN_RXESC_RBDS(7);
    MCAN1_REGS->MCAN_NDAT1 = MCAN_NDAT1_Msk;
    MCAN1_REGS->MCAN_NDAT2 = MCAN_NDAT2_Msk;

    /* Transmit Buffer/FIFO Element Size Configuration Register */
    MCAN1_REGS->MCAN_TXESC = MCAN_TXESC_TBDS(7);

    /* Global Filter Configuration Register */
    MCAN1_REGS->MCAN_GFC = MCAN_GFC_ANFS(2) | MCAN_GFC_ANFE(2);

    /* Extended ID AND Mask Register */
    MCAN1_REGS->MCAN_XIDAM = MCAN_XIDAM_Msk;

    /* Set the operation mode */
    MCAN1_REGS->MCAN_CCCR = MCAN_CCCR_INIT_DISABLED | MCAN_CCCR_FDOE_ENABLED | MCAN_CCCR_BRSE_ENABLED;
    while ((MCAN1_REGS->MCAN_CCCR & MCAN_CCCR_INIT_Msk) == MCAN_CCCR_INIT_Msk);
    memset((void*)&mcan1Obj.msgRAMConfig, 0x00, sizeof(MCAN_MSG_RAM_CONFIG));
}

// *****************************************************************************
/* Function:
    bool MCAN1_MessageTransmit(uint32_t id, uint8_t length, uint8_t* data, MCAN_MODE mode, MCAN_MSG_TX_ATTRIBUTE msgAttr)

   Summary:
    Transmits a message into CAN bus.

   Precondition:
    MCAN1_Initialize must have been called for the associated MCAN instance.

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
bool MCAN1_MessageTransmit(uint32_t id, uint8_t length, uint8_t* data, MCAN_MODE mode, MCAN_MSG_TX_ATTRIBUTE msgAttr)
{
    uint8_t dlc = 0;
    uint8_t tfqpi = 0;
    mcan_txbe_registers_t *fifo = NULL;
    static uint8_t messageMarker = 0;

    switch (msgAttr)
    {
        case MCAN_MSG_ATTR_TX_FIFO_DATA_FRAME:
        case MCAN_MSG_ATTR_TX_FIFO_RTR_FRAME:
            if (MCAN1_REGS->MCAN_TXFQS & MCAN_TXFQS_TFQF_Msk)
            {
                /* The FIFO is full */
                return false;
            }
            tfqpi = (uint8_t)((MCAN1_REGS->MCAN_TXFQS & MCAN_TXFQS_TFQPI_Msk) >> MCAN_TXFQS_TFQPI_Pos);
            fifo = (mcan_txbe_registers_t *) ((uint8_t *)mcan1Obj.msgRAMConfig.txBuffersAddress + tfqpi * MCAN1_TX_FIFO_BUFFER_ELEMENT_SIZE);
            break;
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
    if (length > 64)
        length = 64;

    MCANLengthToDlcGet(length, &dlc);

    fifo->MCAN_TXBE_1 = MCAN_TXBE_1_DLC(dlc);

    if(mode == MCAN_MODE_FD_WITH_BRS)
    {
        fifo->MCAN_TXBE_1 |= MCAN_TXBE_1_FDF_Msk | MCAN_TXBE_1_BRS_Msk;
    }
    else if (mode == MCAN_MODE_FD_WITHOUT_BRS)
    {
        fifo->MCAN_TXBE_1 |= MCAN_TXBE_1_FDF_Msk;
    }

    if (msgAttr == MCAN_MSG_ATTR_TX_BUFFER_DATA_FRAME || msgAttr == MCAN_MSG_ATTR_TX_FIFO_DATA_FRAME)
    {
        /* copy the data into the payload */
        memcpy((uint8_t *)&fifo->MCAN_TXBE_DATA, data, length);
    }
    else if (msgAttr == MCAN_MSG_ATTR_TX_BUFFER_RTR_FRAME || msgAttr == MCAN_MSG_ATTR_TX_FIFO_RTR_FRAME)
    {
        fifo->MCAN_TXBE_0 |= MCAN_TXBE_0_RTR_Msk;
    }

    fifo->MCAN_TXBE_1 |= ((++messageMarker << MCAN_TXBE_1_MM_Pos) & MCAN_TXBE_1_MM_Msk);

    /* request the transmit */
    MCAN1_REGS->MCAN_TXBAR = 1U << tfqpi;

    return true;
}

// *****************************************************************************
/* Function:
    bool MCAN1_MessageReceive(uint32_t *id, uint8_t *length, uint8_t *data, uint16_t *timestamp,
                                              MCAN_MSG_RX_ATTRIBUTE msgAttr, MCAN_MSG_RX_FRAME_ATTRIBUTE *msgFrameAttr)

   Summary:
    Receives a message from CAN bus.

   Precondition:
    MCAN1_Initialize must have been called for the associated MCAN instance.

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
bool MCAN1_MessageReceive(uint32_t *id, uint8_t *length, uint8_t *data, uint16_t *timestamp,
                                          MCAN_MSG_RX_ATTRIBUTE msgAttr, MCAN_MSG_RX_FRAME_ATTRIBUTE *msgFrameAttr)
{
    uint8_t msgLength = 0;
    uint8_t rxgi = 0;
    mcan_rxbe_registers_t *rxbeFifo = NULL;
    mcan_rxf0e_registers_t *rxf0eFifo = NULL;
    mcan_rxf1e_registers_t *rxf1eFifo = NULL;
    bool status = false;

    switch (msgAttr)
    {
        case MCAN_MSG_ATTR_RX_BUFFER:
            /* Check and return false if nothing to be read */
            if ((MCAN1_REGS->MCAN_NDAT1 == 0) && (MCAN1_REGS->MCAN_NDAT2 == 0))
            {
                return status;
            }
            /* Read data from the Rx Buffer */
            if (MCAN1_REGS->MCAN_NDAT1 != 0)
            {
                for (rxgi = 0; rxgi <= 0x1F; rxgi++)
                {
                    if ((MCAN1_REGS->MCAN_NDAT1 & (1 << rxgi)) == (1 << rxgi))
                        break;
                }
            }
            else
            {
                for (rxgi = 0; rxgi <= 0x1F; rxgi++)
                {
                    if ((MCAN1_REGS->MCAN_NDAT2 & (1 << rxgi)) == (1 << rxgi))
                    {
                        rxgi = rxgi + 32;
                        break;
                    }
                }
            }
            rxbeFifo = (mcan_rxbe_registers_t *) ((uint8_t *)mcan1Obj.msgRAMConfig.rxBuffersAddress + rxgi * MCAN1_RX_BUFFER_ELEMENT_SIZE);

            /* Get received identifier */
            if (rxbeFifo->MCAN_RXBE_0 & MCAN_RXBE_0_XTD_Msk)
            {
                *id = rxbeFifo->MCAN_RXBE_0 & MCAN_RXBE_0_ID_Msk;
            }
            else
            {
                *id = (rxbeFifo->MCAN_RXBE_0 >> 18) & MCAN_STD_ID_Msk;
            }

            /* Check RTR and FDF bits for Remote/Data Frame */
            if ((rxbeFifo->MCAN_RXBE_0 & MCAN_RXBE_0_RTR_Msk) && ((rxbeFifo->MCAN_RXBE_1 & MCAN_RXBE_1_FDF_Msk) == 0))
            {
                *msgFrameAttr = MCAN_MSG_RX_REMOTE_FRAME;
            }
            else
            {
                *msgFrameAttr = MCAN_MSG_RX_DATA_FRAME;
            }

            /* Get received data length */
            msgLength = MCANDlcToLengthGet(((rxbeFifo->MCAN_RXBE_1 & MCAN_RXBE_1_DLC_Msk) >> MCAN_RXBE_1_DLC_Pos));

            /* Copy data to user buffer */
            memcpy(data, (uint8_t *)&rxbeFifo->MCAN_RXBE_DATA, msgLength);
            *length = msgLength;

            /* Clear new data flag */
            if (rxgi < 32)
            {
                MCAN1_REGS->MCAN_NDAT1 = (1 << rxgi);
            }
            else
            {
                MCAN1_REGS->MCAN_NDAT2 = (1 << (rxgi - 32));
            }
            status = true;
            break;
        case MCAN_MSG_ATTR_RX_FIFO0:
            /* Check and return false if nothing to be read */
            if ((MCAN1_REGS->MCAN_RXF0S & MCAN_RXF0S_F0FL_Msk) == 0)
            {
                return status;
            }
            /* Read data from the Rx FIFO0 */
            rxgi = (uint8_t)((MCAN1_REGS->MCAN_RXF0S & MCAN_RXF0S_F0GI_Msk) >> MCAN_RXF0S_F0GI_Pos);
            rxf0eFifo = (mcan_rxf0e_registers_t *) ((uint8_t *)mcan1Obj.msgRAMConfig.rxFIFO0Address + rxgi * MCAN1_RX_FIFO0_ELEMENT_SIZE);

            /* Get received identifier */
            if (rxf0eFifo->MCAN_RXF0E_0 & MCAN_RXF0E_0_XTD_Msk)
            {
                *id = rxf0eFifo->MCAN_RXF0E_0 & MCAN_RXF0E_0_ID_Msk;
            }
            else
            {
                *id = (rxf0eFifo->MCAN_RXF0E_0 >> 18) & MCAN_STD_ID_Msk;
            }

            /* Check RTR and FDF bits for Remote/Data Frame */
            if ((rxf0eFifo->MCAN_RXF0E_0 & MCAN_RXF0E_0_RTR_Msk) && ((rxf0eFifo->MCAN_RXF0E_1 & MCAN_RXF0E_1_FDF_Msk) == 0))
            {
                *msgFrameAttr = MCAN_MSG_RX_REMOTE_FRAME;
            }
            else
            {
                *msgFrameAttr = MCAN_MSG_RX_DATA_FRAME;
            }

            /* Get received data length */
            msgLength = MCANDlcToLengthGet(((rxf0eFifo->MCAN_RXF0E_1 & MCAN_RXF0E_1_DLC_Msk) >> MCAN_RXF0E_1_DLC_Pos));

            /* Copy data to user buffer */
            memcpy(data, (uint8_t *)&rxf0eFifo->MCAN_RXF0E_DATA, msgLength);
            *length = msgLength;

            /* Ack the fifo position */
            MCAN1_REGS->MCAN_RXF0A = MCAN_RXF0A_F0AI(rxgi);
            status = true;
            break;
        case MCAN_MSG_ATTR_RX_FIFO1:
            /* Check and return false if nothing to be read */
            if ((MCAN1_REGS->MCAN_RXF1S & MCAN_RXF1S_F1FL_Msk) == 0)
            {
                return status;
            }
            /* Read data from the Rx FIFO1 */
            rxgi = (uint8_t)((MCAN1_REGS->MCAN_RXF1S & MCAN_RXF1S_F1GI_Msk) >> MCAN_RXF1S_F1GI_Pos);
            rxf1eFifo = (mcan_rxf1e_registers_t *) ((uint8_t *)mcan1Obj.msgRAMConfig.rxFIFO1Address + rxgi * MCAN1_RX_FIFO1_ELEMENT_SIZE);

            /* Get received identifier */
            if (rxf1eFifo->MCAN_RXF1E_0 & MCAN_RXF1E_0_XTD_Msk)
            {
                *id = rxf1eFifo->MCAN_RXF1E_0 & MCAN_RXF1E_0_ID_Msk;
            }
            else
            {
                *id = (rxf1eFifo->MCAN_RXF1E_0 >> 18) & MCAN_STD_ID_Msk;
            }

            /* Check RTR and FDF bits for Remote/Data Frame */
            if ((rxf1eFifo->MCAN_RXF1E_0 & MCAN_RXF1E_0_RTR_Msk) && ((rxf1eFifo->MCAN_RXF1E_1 & MCAN_RXF1E_1_FDF_Msk) == 0))
            {
                *msgFrameAttr = MCAN_MSG_RX_REMOTE_FRAME;
            }
            else
            {
                *msgFrameAttr = MCAN_MSG_RX_DATA_FRAME;
            }

            /* Get received data length */
            msgLength = MCANDlcToLengthGet(((rxf1eFifo->MCAN_RXF1E_1 & MCAN_RXF1E_1_DLC_Msk) >> MCAN_RXF1E_1_DLC_Pos));

            /* Copy data to user buffer */
            memcpy(data, (uint8_t *)&rxf1eFifo->MCAN_RXF1E_DATA, msgLength);
            *length = msgLength;

            /* Ack the fifo position */
            MCAN1_REGS->MCAN_RXF1A = MCAN_RXF1A_F1AI(rxgi);
            status = true;
            break;
        default:
            return status;
    }
    return status;
}

// *****************************************************************************
/* Function:
    bool MCAN1_TransmitEventFIFOElementGet(uint32_t *id, uint8_t *messageMarker, uint16_t *timestamp)

   Summary:
    Get the Transmit Event FIFO Element for the transmitted message.

   Precondition:
    MCAN1_Initialize must have been called for the associated MCAN instance.

   Parameters:
    id            - Pointer to 11-bit / 29-bit identifier (ID) to be received.
    messageMarker - Pointer to Tx message message marker number to be received
    timestamp     - Pointer to Tx message timestamp to be received, timestamp value is 0 if Timestamp is disabled

   Returns:
    Request status.
    true  - Request was successful.
    false - Request has failed.
*/
bool MCAN1_TransmitEventFIFOElementGet(uint32_t *id, uint8_t *messageMarker, uint16_t *timestamp)
{
    mcan_txefe_registers_t *txEventFIFOElement = NULL;
    uint8_t txefgi = 0;
    bool status = false;

    /* Check if Tx Event FIFO Element available */
    if ((MCAN1_REGS->MCAN_TXEFS & MCAN_TXEFS_EFFL_Msk) != 0)
    {
        /* Get a pointer to Tx Event FIFO Element */
        txefgi = (uint8_t)((MCAN1_REGS->MCAN_TXEFS & MCAN_TXEFS_EFGI_Msk) >> MCAN_TXEFS_EFGI_Pos);
        txEventFIFOElement = (mcan_txefe_registers_t *) ((uint8_t *)mcan1Obj.msgRAMConfig.txEventFIFOAddress + txefgi * sizeof(mcan_txefe_registers_t));

        /* Check if it's a extended message type */
        if (txEventFIFOElement->MCAN_TXEFE_0 & MCAN_TXEFE_0_XTD_Msk)
        {
            *id = txEventFIFOElement->MCAN_TXEFE_0 & MCAN_TXEFE_0_ID_Msk;
        }
        else
        {
            *id = (txEventFIFOElement->MCAN_TXEFE_0 >> 18) & MCAN_STD_ID_Msk;
        }

        *messageMarker = ((txEventFIFOElement->MCAN_TXEFE_1 & MCAN_TXEFE_1_MM_Msk) >> MCAN_TXEFE_1_MM_Pos);

        /* Get timestamp from transmitted message */
        if (timestamp != NULL)
        {
            *timestamp = (uint16_t)(txEventFIFOElement->MCAN_TXEFE_1 & MCAN_TXEFE_1_TXTS_Msk);
        }

        /* Ack the Tx Event FIFO position */
        MCAN1_REGS->MCAN_TXEFA = MCAN_TXEFA_EFAI(txefgi);

        /* Tx Event FIFO Element read successfully, so return true */
        status = true;
    }
    return status;
}

// *****************************************************************************
/* Function:
    MCAN_ERROR MCAN1_ErrorGet(void)

   Summary:
    Returns the error during transfer.

   Precondition:
    MCAN1_Initialize must have been called for the associated MCAN instance.

   Parameters:
    None.

   Returns:
    Error during transfer.
*/
MCAN_ERROR MCAN1_ErrorGet(void)
{
    MCAN_ERROR error;
    uint32_t   errorStatus = MCAN1_REGS->MCAN_PSR;

    error = (MCAN_ERROR) ((errorStatus & MCAN_PSR_LEC_Msk) | (errorStatus & MCAN_PSR_EP_Msk) | (errorStatus & MCAN_PSR_EW_Msk)
            | (errorStatus & MCAN_PSR_BO_Msk) | (errorStatus & MCAN_PSR_DLEC_Msk) | (errorStatus & MCAN_PSR_PXE_Msk));

    if ((MCAN1_REGS->MCAN_CCCR & MCAN_CCCR_INIT_Msk) == MCAN_CCCR_INIT_Msk)
    {
        MCAN1_REGS->MCAN_CCCR |= MCAN_CCCR_CCE_Msk;
        MCAN1_REGS->MCAN_CCCR = MCAN_CCCR_INIT_DISABLED | MCAN_CCCR_FDOE_ENABLED | MCAN_CCCR_BRSE_ENABLED;
        while ((MCAN1_REGS->MCAN_CCCR & MCAN_CCCR_INIT_Msk) == MCAN_CCCR_INIT_Msk);
    }

    return error;
}

// *****************************************************************************
/* Function:
    void MCAN1_ErrorCountGet(uint8_t *txErrorCount, uint8_t *rxErrorCount)

   Summary:
    Returns the transmit and receive error count during transfer.

   Precondition:
    MCAN1_Initialize must have been called for the associated MCAN instance.

   Parameters:
    txErrorCount - Transmit Error Count to be received
    rxErrorCount - Receive Error Count to be received

   Returns:
    None.
*/
void MCAN1_ErrorCountGet(uint8_t *txErrorCount, uint8_t *rxErrorCount)
{
    *txErrorCount = (uint8_t)(MCAN1_REGS->MCAN_ECR & MCAN_ECR_TEC_Msk);
    *rxErrorCount = (uint8_t)((MCAN1_REGS->MCAN_ECR & MCAN_ECR_REC_Msk) >> MCAN_ECR_REC_Pos);
}

// *****************************************************************************
/* Function:
    bool MCAN1_InterruptGet(MCAN_INTERRUPT_MASK interruptMask)

   Summary:
    Returns the Interrupt status.

   Precondition:
    MCAN1_Initialize must have been called for the associated MCAN instance.

   Parameters:
    interruptMask - Interrupt source number

   Returns:
    true - Requested interrupt is occurred.
    false - Requested interrupt is not occurred.
*/
bool MCAN1_InterruptGet(MCAN_INTERRUPT_MASK interruptMask)
{
    return ((MCAN1_REGS->MCAN_IR & interruptMask) != 0x0);
}

// *****************************************************************************
/* Function:
    void MCAN1_InterruptClear(MCAN_INTERRUPT_MASK interruptMask)

   Summary:
    Clears Interrupt status.

   Precondition:
    MCAN1_Initialize must have been called for the associated MCAN instance.

   Parameters:
    interruptMask - Interrupt to be cleared

   Returns:
    None
*/
void MCAN1_InterruptClear(MCAN_INTERRUPT_MASK interruptMask)
{
    MCAN1_REGS->MCAN_IR = interruptMask;
}

// *****************************************************************************
/* Function:
    bool MCAN1_TxFIFOIsFull(void)

   Summary:
    Returns true if Tx FIFO is full otherwise false.

   Precondition:
    MCAN1_Initialize must have been called for the associated MCAN instance.

   Parameters:
    None

   Returns:
    true  - Tx FIFO is full.
    false - Tx FIFO is not full.
*/
bool MCAN1_TxFIFOIsFull(void)
{
    return (MCAN1_REGS->MCAN_TXFQS & MCAN_TXFQS_TFQF_Msk);
}

// *****************************************************************************
/* Function:
    void MCAN1_MessageRAMConfigSet(uint8_t *msgRAMConfigBaseAddress)

   Summary:
    Set the Message RAM Configuration.

   Precondition:
    MCAN1_Initialize must have been called for the associated MCAN instance.

   Parameters:
    msgRAMConfigBaseAddress - Pointer to application allocated buffer base address.
                              Application must allocate buffer from non-cached
                              contiguous memory and buffer size must be
                              MCAN1_MESSAGE_RAM_CONFIG_SIZE

   Returns:
    None
*/
void MCAN1_MessageRAMConfigSet(uint8_t *msgRAMConfigBaseAddress)
{
    uint32_t offset = 0;

    memset((void*)msgRAMConfigBaseAddress, 0x00, MCAN1_MESSAGE_RAM_CONFIG_SIZE);

    /* Set MCAN CCCR Init for Message RAM Configuration */
    MCAN1_REGS->MCAN_CCCR = MCAN_CCCR_INIT_ENABLED;
    while ((MCAN1_REGS->MCAN_CCCR & MCAN_CCCR_INIT_Msk) != MCAN_CCCR_INIT_Msk);

    /* Set CCE to unlock the configuration registers */
    MCAN1_REGS->MCAN_CCCR |= MCAN_CCCR_CCE_Msk;

    mcan1Obj.msgRAMConfig.rxFIFO0Address = (mcan_rxf0e_registers_t *)msgRAMConfigBaseAddress;
    offset = MCAN1_RX_FIFO0_SIZE;
    /* Receive FIFO 0 Configuration Register */
    MCAN1_REGS->MCAN_RXF0C = MCAN_RXF0C_F0S(1) | MCAN_RXF0C_F0WM(0) | MCAN_RXF0C_F0OM_Msk |
            MCAN_RXF0C_F0SA(((uint32_t)mcan1Obj.msgRAMConfig.rxFIFO0Address >> 2));

    mcan1Obj.msgRAMConfig.rxFIFO1Address = (mcan_rxf1e_registers_t *)(msgRAMConfigBaseAddress + offset);
    offset += MCAN1_RX_FIFO1_SIZE;
    /* Receive FIFO 1 Configuration Register */
    MCAN1_REGS->MCAN_RXF1C = MCAN_RXF1C_F1S(1) | MCAN_RXF1C_F1WM(0) | MCAN_RXF1C_F1OM_Msk |
            MCAN_RXF1C_F1SA(((uint32_t)mcan1Obj.msgRAMConfig.rxFIFO1Address >> 2));

    mcan1Obj.msgRAMConfig.rxBuffersAddress = (mcan_rxbe_registers_t *)(msgRAMConfigBaseAddress + offset);
    offset += MCAN1_RX_BUFFER_SIZE;
    MCAN1_REGS->MCAN_RXBC = MCAN_RXBC_RBSA(((uint32_t)mcan1Obj.msgRAMConfig.rxBuffersAddress >> 2));

    mcan1Obj.msgRAMConfig.txBuffersAddress = (mcan_txbe_registers_t *)(msgRAMConfigBaseAddress + offset);
    offset += MCAN1_TX_FIFO_BUFFER_SIZE;
    /* Transmit Buffer/FIFO Configuration Register */
    MCAN1_REGS->MCAN_TXBC = MCAN_TXBC_TFQS(1) |
            MCAN_TXBC_TBSA(((uint32_t)mcan1Obj.msgRAMConfig.txBuffersAddress >> 2));

    mcan1Obj.msgRAMConfig.txEventFIFOAddress =  (mcan_txefe_registers_t *)(msgRAMConfigBaseAddress + offset);
    offset += MCAN1_TX_EVENT_FIFO_SIZE;
    /* Transmit Event FIFO Configuration Register */
    MCAN1_REGS->MCAN_TXEFC = MCAN_TXEFC_EFWM(0) | MCAN_TXEFC_EFS(1) |
            MCAN_TXEFC_EFSA(((uint32_t)mcan1Obj.msgRAMConfig.txEventFIFOAddress >> 2));

    mcan1Obj.msgRAMConfig.stdMsgIDFilterAddress = (mcan_sidfe_registers_t *)(msgRAMConfigBaseAddress + offset);
    memcpy((void *)mcan1Obj.msgRAMConfig.stdMsgIDFilterAddress,
           (const void *)mcan1StdFilter,
           MCAN1_STD_MSG_ID_FILTER_SIZE);
    offset += MCAN1_STD_MSG_ID_FILTER_SIZE;
    /* Standard ID Filter Configuration Register */
    MCAN1_REGS->MCAN_SIDFC = MCAN_SIDFC_LSS(2) |
            MCAN_SIDFC_FLSSA(((uint32_t)mcan1Obj.msgRAMConfig.stdMsgIDFilterAddress >> 2));

    mcan1Obj.msgRAMConfig.extMsgIDFilterAddress = (mcan_xidfe_registers_t *)(msgRAMConfigBaseAddress + offset);
    memcpy((void *)mcan1Obj.msgRAMConfig.extMsgIDFilterAddress,
           (const void *)mcan1ExtFilter,
           MCAN1_EXT_MSG_ID_FILTER_SIZE);
    /* Extended ID Filter Configuration Register */
    MCAN1_REGS->MCAN_XIDFC = MCAN_XIDFC_LSE(2) |
            MCAN_XIDFC_FLESA(((uint32_t)mcan1Obj.msgRAMConfig.extMsgIDFilterAddress >> 2));

    /* Set 16-bit MSB of mcan1 base address */
    MATRIX_REGS->CCFG_SYSIO = (MATRIX_REGS->CCFG_SYSIO & ~CCFG_SYSIO_CAN1DMABA_Msk)
                            | CCFG_SYSIO_CAN1DMABA(((uint32_t)msgRAMConfigBaseAddress >> 16));

    /* Complete Message RAM Configuration by clearing MCAN CCCR Init */
    MCAN1_REGS->MCAN_CCCR = MCAN_CCCR_INIT_DISABLED | MCAN_CCCR_FDOE_ENABLED | MCAN_CCCR_BRSE_ENABLED;
    while ((MCAN1_REGS->MCAN_CCCR & MCAN_CCCR_INIT_Msk) == MCAN_CCCR_INIT_Msk);
}

// *****************************************************************************
/* Function:
    bool MCAN1_StandardFilterElementSet(uint8_t filterNumber, mcan_sidfe_registers_t *stdMsgIDFilterElement)

   Summary:
    Set a standard filter element configuration.

   Precondition:
    MCAN1_Initialize and MCAN1_MessageRAMConfigSet must have been called
    for the associated MCAN instance.

   Parameters:
    filterNumber          - Standard Filter number to be configured.
    stdMsgIDFilterElement - Pointer to Standard Filter Element configuration to be set on specific filterNumber.

   Returns:
    Request status.
    true  - Request was successful.
    false - Request has failed.
*/
bool MCAN1_StandardFilterElementSet(uint8_t filterNumber, mcan_sidfe_registers_t *stdMsgIDFilterElement)
{
    if ((filterNumber > 2) || (stdMsgIDFilterElement == NULL))
    {
        return false;
    }
    mcan1Obj.msgRAMConfig.stdMsgIDFilterAddress[filterNumber - 1].MCAN_SIDFE_0 = stdMsgIDFilterElement->MCAN_SIDFE_0;

    return true;
}

// *****************************************************************************
/* Function:
    bool MCAN1_StandardFilterElementGet(uint8_t filterNumber, mcan_sidfe_registers_t *stdMsgIDFilterElement)

   Summary:
    Get a standard filter element configuration.

   Precondition:
    MCAN1_Initialize and MCAN1_MessageRAMConfigSet must have been called
    for the associated MCAN instance.

   Parameters:
    filterNumber          - Standard Filter number to get filter configuration.
    stdMsgIDFilterElement - Pointer to Standard Filter Element configuration for storing filter configuration.

   Returns:
    Request status.
    true  - Request was successful.
    false - Request has failed.
*/
bool MCAN1_StandardFilterElementGet(uint8_t filterNumber, mcan_sidfe_registers_t *stdMsgIDFilterElement)
{
    if ((filterNumber > 2) || (stdMsgIDFilterElement == NULL))
    {
        return false;
    }
    stdMsgIDFilterElement->MCAN_SIDFE_0 = mcan1Obj.msgRAMConfig.stdMsgIDFilterAddress[filterNumber - 1].MCAN_SIDFE_0;

    return true;
}

// *****************************************************************************
/* Function:
    bool MCAN1_ExtendedFilterElementSet(uint8_t filterNumber, mcan_xidfe_registers_t *extMsgIDFilterElement)

   Summary:
    Set a Extended filter element configuration.

   Precondition:
    MCAN1_Initialize and MCAN1_MessageRAMConfigSet must have been called
    for the associated MCAN instance.

   Parameters:
    filterNumber          - Extended Filter number to be configured.
    extMsgIDFilterElement - Pointer to Extended Filter Element configuration to be set on specific filterNumber.

   Returns:
    Request status.
    true  - Request was successful.
    false - Request has failed.
*/
bool MCAN1_ExtendedFilterElementSet(uint8_t filterNumber, mcan_xidfe_registers_t *extMsgIDFilterElement)
{
    if ((filterNumber > 2) || (extMsgIDFilterElement == NULL))
    {
        return false;
    }
    mcan1Obj.msgRAMConfig.extMsgIDFilterAddress[filterNumber - 1].MCAN_XIDFE_0 = extMsgIDFilterElement->MCAN_XIDFE_0;
    mcan1Obj.msgRAMConfig.extMsgIDFilterAddress[filterNumber - 1].MCAN_XIDFE_1 = extMsgIDFilterElement->MCAN_XIDFE_1;

    return true;
}

// *****************************************************************************
/* Function:
    bool MCAN1_ExtendedFilterElementGet(uint8_t filterNumber, mcan_xidfe_registers_t *extMsgIDFilterElement)

   Summary:
    Get a Extended filter element configuration.

   Precondition:
    MCAN1_Initialize and MCAN1_MessageRAMConfigSet must have been called
    for the associated MCAN instance.

   Parameters:
    filterNumber          - Extended Filter number to get filter configuration.
    extMsgIDFilterElement - Pointer to Extended Filter Element configuration for storing filter configuration.

   Returns:
    Request status.
    true  - Request was successful.
    false - Request has failed.
*/
bool MCAN1_ExtendedFilterElementGet(uint8_t filterNumber, mcan_xidfe_registers_t *extMsgIDFilterElement)
{
    if ((filterNumber > 2) || (extMsgIDFilterElement == NULL))
    {
        return false;
    }
    extMsgIDFilterElement->MCAN_XIDFE_0 = mcan1Obj.msgRAMConfig.extMsgIDFilterAddress[filterNumber - 1].MCAN_XIDFE_0;
    extMsgIDFilterElement->MCAN_XIDFE_1 = mcan1Obj.msgRAMConfig.extMsgIDFilterAddress[filterNumber - 1].MCAN_XIDFE_1;

    return true;
}



/*******************************************************************************
 End of File
*/
