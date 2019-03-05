/*******************************************************************************
  ${HSMCI_INSTANCE_NAME} PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${HSMCI_INSTANCE_NAME?lower_case}.c

  Summary:
    ${HSMCI_INSTANCE_NAME} PLIB Implementation File

  Description:
    None

*******************************************************************************/

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

#include "device.h"
#include "plib_${HSMCI_INSTANCE_NAME?lower_case}.h"
#include "peripheral/xdmac/plib_${XDMAC_INSTANCE_NAME?lower_case}.h"

#define ${HSMCI_INSTANCE_NAME}_DMA_CHANNEL      ${HSMCI_DMA}

// *****************************************************************************
// *****************************************************************************
// Section: Include Files
// *****************************************************************************
// *****************************************************************************
static HSMCI_OBJECT ${HSMCI_INSTANCE_NAME?lower_case}Obj;

static void ${HSMCI_INSTANCE_NAME}_VariablesInit ( void )
{
    ${HSMCI_INSTANCE_NAME?lower_case}Obj.errorStatus = 0;
    ${HSMCI_INSTANCE_NAME?lower_case}Obj.isCmdInProgress = false;
    ${HSMCI_INSTANCE_NAME?lower_case}Obj.isDataInProgress = false;
    ${HSMCI_INSTANCE_NAME?lower_case}Obj.callback = false;
}

void ${HSMCI_INSTANCE_NAME}_InterruptHandler(void)
{
    volatile uint32_t intMask = 0;
    volatile uint32_t intFlags = 0;
    HSMCI_XFER_STATUS xferStatus = 0;

    intMask = ${HSMCI_INSTANCE_NAME}_REGS->HSMCI_IMR;
    intFlags = ${HSMCI_INSTANCE_NAME}_REGS->HSMCI_SR;

    if ((intMask & intFlags) == 0)
    {
        return;
    }

    if (${HSMCI_INSTANCE_NAME?lower_case}Obj.isCmdInProgress == true)
    {
        if (intFlags & (HSMCI_SR_CMDRDY_Msk | HSMCI_CMD_ERROR))
        {
            if (intFlags & HSMCI_CMD_ERROR)
            {
                if ((intFlags & HSMCI_SR_RTOE_Msk) && (intMask & HSMCI_SR_RTOE_Msk))
                {
                    /* Response Timeout Error */
                    ${HSMCI_INSTANCE_NAME?lower_case}Obj.errorStatus |= HSMCI_CMD_TIMEOUT_ERROR;
                }
                if ((intFlags & HSMCI_SR_RCRCE_Msk) && (intMask & HSMCI_SR_RCRCE_Msk))
                {
                    /* Response CRC Error */
                    ${HSMCI_INSTANCE_NAME?lower_case}Obj.errorStatus |= HSMCI_CMD_CRC_ERROR;
                }
                if ((intFlags & HSMCI_SR_RINDE_Msk) && (intMask & HSMCI_SR_RINDE_Msk))
                {
                    /* Response Index Error */
                    ${HSMCI_INSTANCE_NAME?lower_case}Obj.errorStatus |= HSMCI_CMD_INDEX_ERROR;
                }
                if ((intFlags & (HSMCI_SR_RENDE_Msk | HSMCI_SR_RDIRE_Msk)) && \
                        (intMask & (HSMCI_SR_RENDE_Msk | HSMCI_SR_RDIRE_Msk)))
                {
                    /* Response End bit Error/Response direction bit error */
                    ${HSMCI_INSTANCE_NAME?lower_case}Obj.errorStatus |= HSMCI_CMD_END_BIT_ERROR;
                }
            }
            ${HSMCI_INSTANCE_NAME?lower_case}Obj.isCmdInProgress = false;
            /* Disable the response interrupt sources */
            ${HSMCI_INSTANCE_NAME}_REGS->HSMCI_IDR |= (HSMCI_IDR_CMDRDY_Msk | HSMCI_CMD_ERROR);
            xferStatus |= HSMCI_XFER_STATUS_CMD_COMPLETED;
        }
    }

    if (${HSMCI_INSTANCE_NAME?lower_case}Obj.isDataInProgress == true)
    {
        if (intFlags & (HSMCI_SR_XFRDONE_Msk | HSMCI_DATA_ERROR))
        {
            if (intFlags & HSMCI_DATA_ERROR)
            {
                if (intFlags & HSMCI_SR_UNRE_Msk)
                {
                    ${HSMCI_INSTANCE_NAME?lower_case}Obj.errorStatus |= HSMCI_DATA_UNDERRUN_ERROR;
                }
                if (intFlags & HSMCI_SR_OVRE_Msk)
                {
                    ${HSMCI_INSTANCE_NAME?lower_case}Obj.errorStatus |= HSMCI_DATA_OVERRUN_ERROR;
                }
                if (intFlags & HSMCI_SR_DTOE_Msk)
                {
                    ${HSMCI_INSTANCE_NAME?lower_case}Obj.errorStatus |= HSMCI_DATA_TIMEOUT_ERROR;
                }
                if (intFlags & HSMCI_SR_DCRCE_Msk)
                {
                    ${HSMCI_INSTANCE_NAME?lower_case}Obj.errorStatus |= HSMCI_DATA_CRC_ERROR;
                }
            }
            ${HSMCI_INSTANCE_NAME?lower_case}Obj.isDataInProgress = false;
            /* Disable data transfer related error sources */
            ${HSMCI_INSTANCE_NAME}_REGS->HSMCI_IDR |= (HSMCI_IDR_XFRDONE_Msk | HSMCI_DATA_ERROR);
            xferStatus |= HSMCI_XFER_STATUS_DATA_COMPLETED;
        }
    }

    if (${HSMCI_INSTANCE_NAME?lower_case}Obj.callback)
    {
        ${HSMCI_INSTANCE_NAME?lower_case}Obj.callback(xferStatus, ${HSMCI_INSTANCE_NAME?lower_case}Obj.context);
    }
}

uint16_t ${HSMCI_INSTANCE_NAME}_CommandErrorGet(void)
{
    /* Error status variable is cleared when a new command is sent */
    return (uint16_t)(${HSMCI_INSTANCE_NAME?lower_case}Obj.errorStatus & (HSMCI_CMD_TIMEOUT_ERROR | HSMCI_CMD_CRC_ERROR | \
                HSMCI_CMD_END_BIT_ERROR | HSMCI_CMD_INDEX_ERROR));
}

uint16_t ${HSMCI_INSTANCE_NAME}_DataErrorGet(void)
{
    /* Error status variable is cleared when a new command is sent */
    return (uint16_t)(${HSMCI_INSTANCE_NAME?lower_case}Obj.errorStatus & (HSMCI_DATA_TIMEOUT_ERROR | HSMCI_DATA_CRC_ERROR | \
            HSMCI_DATA_UNDERRUN_ERROR | HSMCI_DATA_OVERRUN_ERROR));
}

bool ${HSMCI_INSTANCE_NAME}_IsCmdLineBusy ( void )
{
    return (!(${HSMCI_INSTANCE_NAME}_REGS->HSMCI_SR & HSMCI_SR_CMDRDY_Msk));
}

bool ${HSMCI_INSTANCE_NAME}_IsDatLineBusy ( void )
{
    if ((!(${HSMCI_INSTANCE_NAME}_REGS->HSMCI_SR & HSMCI_SR_XFRDONE_Msk)) || (!(${HSMCI_INSTANCE_NAME}_REGS->HSMCI_SR & HSMCI_SR_TXRDY_Msk)))
    {
        return true;
    }
    else
    {
        return false;
    }
}

void ${HSMCI_INSTANCE_NAME}_BusWidthSet ( HSMCI_BUS_WIDTH busWidth )
{
    if (busWidth == HSMCI_BUS_WIDTH_4_BIT)
    {
        ${HSMCI_INSTANCE_NAME}_REGS->HSMCI_SDCR &= ~HSMCI_SDCR_SDCBUS_Msk;
        ${HSMCI_INSTANCE_NAME}_REGS->HSMCI_SDCR |= HSMCI_SDCR_SDCBUS_4;
    }
    else
    {
       ${HSMCI_INSTANCE_NAME}_REGS->HSMCI_SDCR &= ~HSMCI_SDCR_SDCBUS_Msk;
       ${HSMCI_INSTANCE_NAME}_REGS->HSMCI_SDCR |= HSMCI_SDCR_SDCBUS_1;
    }
}

void ${HSMCI_INSTANCE_NAME}_SpeedModeSet ( HSMCI_SPEED_MODE speedMode )
{
    if (speedMode == HSMCI_SPEED_MODE_HIGH)
    {
       ${HSMCI_INSTANCE_NAME}_REGS->HSMCI_CFG |= HSMCI_CFG_HSMODE_Msk;
    }
    else
    {
        ${HSMCI_INSTANCE_NAME}_REGS->HSMCI_CFG &= ~HSMCI_CFG_HSMODE_Msk;
    }
}

void ${HSMCI_INSTANCE_NAME}_DmaSetup (
    uint8_t* buffer,
    uint32_t numBytes,
    HSMCI_DATA_TRANSFER_DIR operation
)
{
    ${HSMCI_INSTANCE_NAME}_REGS->HSMCI_DMA = HSMCI_DMA_DMAEN_Msk;

    if (operation == HSMCI_DATA_TRANSFER_DIR_READ)
    {
        ${XDMAC_INSTANCE_NAME}_ChannelSettingsSet(${HSMCI_INSTANCE_NAME}_DMA_CHANNEL,
                            XDMAC_CC_TYPE_PER_TRAN
                            | XDMAC_CC_MBSIZE_SINGLE
                            | XDMAC_CC_DSYNC_PER2MEM
                            | XDMAC_CC_CSIZE_CHK_1
                            | XDMAC_CC_DWIDTH_WORD
                            | XDMAC_CC_SIF_AHB_IF1
                            | XDMAC_CC_DIF_AHB_IF0
                            | XDMAC_CC_SAM_FIXED_AM
                            | XDMAC_CC_DAM_INCREMENTED_AM
                            | XDMAC_CC_PERID(${HSMCI_INSTANCE_NAME}_DMA_CHANNEL)
        );

        ${XDMAC_INSTANCE_NAME}_ChannelTransfer(
            ${HSMCI_INSTANCE_NAME}_DMA_CHANNEL,
            (const void *)&(${HSMCI_INSTANCE_NAME}_REGS->HSMCI_FIFO[0]),
            (const void *)buffer,
            (numBytes/4)
        );
    }
    else
    {
        ${XDMAC_INSTANCE_NAME}_ChannelSettingsSet(${HSMCI_INSTANCE_NAME}_DMA_CHANNEL,
                    XDMAC_CC_TYPE_PER_TRAN
                    | XDMAC_CC_MBSIZE_SINGLE
                    | XDMAC_CC_DSYNC_MEM2PER
                    | XDMAC_CC_CSIZE_CHK_1
                    | XDMAC_CC_DWIDTH_WORD
                    | XDMAC_CC_SIF_AHB_IF0
                    | XDMAC_CC_DIF_AHB_IF1
                    | XDMAC_CC_SAM_INCREMENTED_AM
                    | XDMAC_CC_DAM_FIXED_AM
                    | XDMAC_CC_PERID(${HSMCI_INSTANCE_NAME}_DMA_CHANNEL)
        );

        ${XDMAC_INSTANCE_NAME}_ChannelTransfer(
            ${HSMCI_INSTANCE_NAME}_DMA_CHANNEL,
            (const void *)buffer,
            (const void *)&(${HSMCI_INSTANCE_NAME}_REGS->HSMCI_FIFO[0]),
            (numBytes/4)
        );
   }
}

void ${HSMCI_INSTANCE_NAME}_BlockSizeSet ( uint16_t blockSize )
{
    ${HSMCI_INSTANCE_NAME?lower_case}Obj.blockSize = blockSize;
    ${HSMCI_INSTANCE_NAME}_REGS->HSMCI_BLKR &= ~(HSMCI_BLKR_BLKLEN_Msk);
    ${HSMCI_INSTANCE_NAME}_REGS->HSMCI_BLKR |= (blockSize << HSMCI_BLKR_BLKLEN_Pos);
}

void ${HSMCI_INSTANCE_NAME}_BlockCountSet ( uint16_t numBlocks )
{
    ${HSMCI_INSTANCE_NAME}_REGS->HSMCI_BLKR &= ~(HSMCI_BLKR_BCNT_Msk);
    ${HSMCI_INSTANCE_NAME}_REGS->HSMCI_BLKR |= (numBlocks << HSMCI_BLKR_BCNT_Pos);
}

void ${HSMCI_INSTANCE_NAME}_ClockSet ( uint32_t clock )
{
    uint32_t mck = ${HSMCI_CLK};
    uint32_t clkdiv = 0;
    uint32_t rest = 0;

    /* Speed = MCK clock / (2 * (CLKDIV + 1)) */

    if ((clock * 2) < mck)
    {
        clkdiv = mck / (2 * clock);
        rest = mck - (2*clock)*clkdiv;

        if (rest > 0)
        {
             /* Ensure that the card speed not be higher than expected */
            clkdiv++;
        }

        if (clkdiv > 0)
        {
            clkdiv -= 1;
        }
    }
    else
    {
        clkdiv = 0;
    }

    ${HSMCI_INSTANCE_NAME}_REGS->HSMCI_MR &= ~HSMCI_MR_CLKDIV_Msk;
    ${HSMCI_INSTANCE_NAME}_REGS->HSMCI_MR |= HSMCI_MR_CLKDIV(clkdiv);
}

void ${HSMCI_INSTANCE_NAME}_ResponseRead (
    HSMCI_READ_RESPONSE_REG respReg,
    uint32_t* response
)
{
    if (response == NULL)
    {
        return;
    }

    switch (respReg)
    {
        case HSMCI_READ_RESP_REG_0:
            *response = ${HSMCI_INSTANCE_NAME}_REGS->HSMCI_RSPR[0];
            break;

        case HSMCI_READ_RESP_REG_1:
            *response = ${HSMCI_INSTANCE_NAME}_REGS->HSMCI_RSPR[1];
            break;

        case HSMCI_READ_RESP_REG_2:
            *response = ${HSMCI_INSTANCE_NAME}_REGS->HSMCI_RSPR[2];
            break;

        case HSMCI_READ_RESP_REG_3:
            *response = ${HSMCI_INSTANCE_NAME}_REGS->HSMCI_RSPR[3];
            break;

        case HSMCI_READ_RESP_REG_ALL:
            response[3] = ${HSMCI_INSTANCE_NAME}_REGS->HSMCI_RSPR[0];
            response[2] = ${HSMCI_INSTANCE_NAME}_REGS->HSMCI_RSPR[1];
            response[1] = ${HSMCI_INSTANCE_NAME}_REGS->HSMCI_RSPR[2];
            response[0] = ${HSMCI_INSTANCE_NAME}_REGS->HSMCI_RSPR[3];

            /* Drop the CRC byte.
             * The CRC byte for the CID and CSD response is not copied.
             */
            memcpy((void*)response, (void*)((char*)response + 1),31);

            break;

        default:
            break;
    }
}

void ${HSMCI_INSTANCE_NAME}_CommandSend (
    uint8_t opCode,
    uint32_t argument,
    uint8_t respType,
    HSMCI_DataTransferFlags transferFlags
)
{
    uint32_t ier_reg = 0;
    uint32_t cmd_reg = 0;

    /* Clear the flags */
    ${HSMCI_INSTANCE_NAME?lower_case}Obj.isCmdInProgress = false;
    ${HSMCI_INSTANCE_NAME?lower_case}Obj.isDataInProgress = false;
    ${HSMCI_INSTANCE_NAME?lower_case}Obj.errorStatus = 0;

    switch (respType)
    {
        case HSMCI_CMD_RESP_R1:
        case HSMCI_CMD_RESP_R5:
        case HSMCI_CMD_RESP_R6:
        case HSMCI_CMD_RESP_R7:
            cmd_reg |= (HSMCI_CMDR_RSPTYP_48_BIT | HSMCI_CMDR_MAXLAT_Msk);
            ier_reg |= (HSMCI_IER_RCRCE_Msk | HSMCI_IER_RINDE_Msk | \
                    HSMCI_IER_RTOE_Msk | HSMCI_IER_RENDE_Msk | HSMCI_IER_RDIRE_Msk);
            break;

        case HSMCI_CMD_RESP_R3:
        case HSMCI_CMD_RESP_R4:
            cmd_reg |= (HSMCI_CMDR_RSPTYP_48_BIT | HSMCI_CMDR_MAXLAT_Msk);
            ier_reg |= (HSMCI_IER_RTOE_Msk | HSMCI_IER_RENDE_Msk | HSMCI_IER_RDIRE_Msk);
            break;

        case HSMCI_CMD_RESP_R1B:
            cmd_reg |= (HSMCI_CMDR_RSPTYP_R1B | HSMCI_CMDR_MAXLAT_Msk);
            ier_reg |= (HSMCI_IER_RCRCE_Msk | HSMCI_IER_RINDE_Msk | \
                    HSMCI_IER_RTOE_Msk | HSMCI_IER_RENDE_Msk | HSMCI_IER_RDIRE_Msk);
            break;

        case HSMCI_CMD_RESP_R2:
            cmd_reg |= (HSMCI_CMDR_RSPTYP_136_BIT | HSMCI_CMDR_MAXLAT_Msk);
            ier_reg |= (HSMCI_IER_RCRCE_Msk | HSMCI_IER_RTOE_Msk | \
                    HSMCI_IER_RENDE_Msk | HSMCI_IER_RDIRE_Msk);
            break;

        case HSMCI_CMD_RESP_NONE:
        default:
            cmd_reg |= HSMCI_CMDR_RSPTYP_NORESP;
            break;
    }
    /* Standard command + Opcode */
    cmd_reg |= HSMCI_CMDR_CMDNB(opCode) | HSMCI_CMDR_SPCMD_STD;

    /* Enable command ready interrupt */
    ier_reg |= HSMCI_IER_CMDRDY_Msk;

    if (transferFlags.isDataPresent == true)
    {
        /* Set the transfer command */
        cmd_reg |= HSMCI_CMDR_TRCMD_START_DATA;

        if (transferFlags.transferType == HSMCI_DATA_TRANSFER_TYPE_SINGLE)
        {
            cmd_reg |= HSMCI_CMDR_TRTYP_SINGLE;
        }
        else
        {
            cmd_reg |= HSMCI_CMDR_TRTYP_MULTIPLE;
        }

        if (transferFlags.transferDir == HSMCI_DATA_TRANSFER_DIR_READ)
        {
            cmd_reg |= HSMCI_CMDR_TRDIR_READ;
        }
        else
        {
            cmd_reg |= HSMCI_CMDR_TRDIR_WRITE;
        }

        ${HSMCI_INSTANCE_NAME}_REGS->HSMCI_MR |= HSMCI_MR_WRPROOF_Msk | HSMCI_MR_RDPROOF_Msk;

        if (${HSMCI_INSTANCE_NAME?lower_case}Obj.blockSize & 0x03)
        {
            /* Block length is not a multiple of 4 bytes, set the FBYTE bit */
            ${HSMCI_INSTANCE_NAME}_REGS->HSMCI_MR |= HSMCI_MR_FBYTE_Msk;
        }
        else
        {
            ${HSMCI_INSTANCE_NAME}_REGS->HSMCI_MR &= ~HSMCI_MR_FBYTE_Msk;
        }

        /* Enable interrupt sources for data*/
        ier_reg |= (HSMCI_IER_XFRDONE_Msk | HSMCI_IER_UNRE_Msk | HSMCI_IER_OVRE_Msk | \
                HSMCI_IER_DTOE_Msk | HSMCI_IER_DCRCE_Msk);

        ${HSMCI_INSTANCE_NAME?lower_case}Obj.isDataInProgress = true;
    }
    else
    {
        ${HSMCI_INSTANCE_NAME}_REGS->HSMCI_DMA = 0;
        ${HSMCI_INSTANCE_NAME}_REGS->HSMCI_MR &= ~(HSMCI_MR_WRPROOF_Msk | HSMCI_MR_RDPROOF_Msk | HSMCI_MR_FBYTE_Msk);
    }

    ${HSMCI_INSTANCE_NAME?lower_case}Obj.isCmdInProgress = true;

    /* Disable all the interrupt sources to begin with */
    ${HSMCI_INSTANCE_NAME}_REGS->HSMCI_IDR = HSMCI_IDR_Msk;

    /* Enable the needed interrupts */
    ${HSMCI_INSTANCE_NAME}_REGS->HSMCI_IER = ier_reg;

    /* Write the argument register */
    ${HSMCI_INSTANCE_NAME}_REGS->HSMCI_ARGR = argument;

    /* Write to the command register and the operation */
    ${HSMCI_INSTANCE_NAME}_REGS->HSMCI_CMDR = cmd_reg;
}

void ${HSMCI_INSTANCE_NAME}_ModuleInit ( void )
{
    /* Set the Data Timeout Register to 2 Mega Cycles */
    ${HSMCI_INSTANCE_NAME}_REGS->HSMCI_DTOR = HSMCI_DTOR_DTOMUL_1048576 | HSMCI_DTOR_DTOCYC(2);

    /* Set Completion Signal Timeout to 2 Mega Cycles */
    ${HSMCI_INSTANCE_NAME}_REGS->HSMCI_CSTOR = HSMCI_CSTOR_CSTOMUL_1048576 | HSMCI_CSTOR_CSTOCYC(2);

    /* Set Configuration Register */
    ${HSMCI_INSTANCE_NAME}_REGS->HSMCI_CFG = HSMCI_CFG_FIFOMODE_Msk | HSMCI_CFG_FERRCTRL_Msk;

    /* Set power saving to maximum value */
    ${HSMCI_INSTANCE_NAME}_REGS->HSMCI_MR = HSMCI_MR_PWSDIV_Msk;

    /* Enable the HSMCI and the Power Saving */
    ${HSMCI_INSTANCE_NAME}_REGS->HSMCI_CR = HSMCI_CR_MCIEN_Msk | HSMCI_CR_PWSEN_Msk;

    /* Reset the high speed mode */
    ${HSMCI_INSTANCE_NAME}_REGS->HSMCI_CFG &= ~HSMCI_CFG_HSMODE_Msk;

    /* Set bus width to 1 bit mode */
    ${HSMCI_INSTANCE_NAME}_REGS->HSMCI_SDCR &= ~HSMCI_SDCR_SDCBUS_Msk;

    /* Set clock to 400 KHz */
    ${HSMCI_INSTANCE_NAME}_ClockSet (HSMCI_CLOCK_FREQ_400_KHZ);

    /* Configure command */
    ${HSMCI_INSTANCE_NAME}_REGS->HSMCI_MR &= ~(HSMCI_MR_WRPROOF_Msk | HSMCI_MR_RDPROOF_Msk | HSMCI_MR_FBYTE_Msk);

    /* Write argument */
    ${HSMCI_INSTANCE_NAME}_REGS->HSMCI_ARGR = 0;

    /* Write and start initialization command */
    ${HSMCI_INSTANCE_NAME}_REGS->HSMCI_CMDR = HSMCI_CMDR_RSPTYP_NORESP
            | HSMCI_CMDR_SPCMD_INIT
            | HSMCI_CMDR_OPDCMD_OPENDRAIN;

    /* Wait end of initialization command */
    while (!(${HSMCI_INSTANCE_NAME}_REGS->HSMCI_SR & HSMCI_SR_CMDRDY_Msk));
}

void ${HSMCI_INSTANCE_NAME}_Initialize( void )
{
    ${HSMCI_INSTANCE_NAME}_VariablesInit();
    ${HSMCI_INSTANCE_NAME}_ModuleInit();
}

void ${HSMCI_INSTANCE_NAME}_CallbackRegister(HSMCI_CALLBACK callback, uintptr_t contextHandle)
{
    if (callback != NULL)
    {
        ${HSMCI_INSTANCE_NAME?lower_case}Obj.callback = callback;
        ${HSMCI_INSTANCE_NAME?lower_case}Obj.context = contextHandle;
    }
}
