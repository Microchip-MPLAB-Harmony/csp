/*******************************************************************************
  ${SDHC_INSTANCE_NAME} PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${SDHC_INSTANCE_NAME?lower_case}.c

  Summary:
    ${SDHC_INSTANCE_NAME} PLIB Implementation File

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
#include "plib_${SDHC_INSTANCE_NAME?lower_case}.h"
<#if core.CoreSysIntFile == true>
#include "interrupts.h"
</#if>


// *****************************************************************************
// *****************************************************************************
// Section: Include Files
// *****************************************************************************
// *****************************************************************************

#include "plib_sdhc_common.h"

#define SDHC_INTEN_Msk                                          0x03FF01FFU
#define SDHC_EISIER_Msk                                         0x03FF0000U
#define SDHC_MODE_RESPTYPE_48_BIT_BUSY                          (0x03UL << 16)
#define SDHC_MODE_RESPTYPE_48_BIT                               (0x02UL << 16)
#define SDHC_MODE_RESPTYPE_136_BIT                              (0x01UL << 16)
#define SDHC_MODE_RESPTYPE_NONE                                 (0x00UL << 16)

#define ${SDHC_INSTANCE_NAME}_DMA_NUM_DESCR_LINES               ${SDHC_NUM_DESCRIPTOR_LINES}U
#define ${SDHC_INSTANCE_NAME}_BASE_CLOCK_FREQUENCY              ${SDHC_CLK_FREQ}
#define ${SDHC_INSTANCE_NAME}_MAX_BLOCK_SIZE                    0x200U

typedef unsigned long paddr_t; /* a physical address */
#define KVA_TO_PA(v)    ((paddr_t)(v) & 0x1fffffffU)

static __attribute__((coherent, aligned(32))) SDHC_ADMA_DESCR ${SDHC_INSTANCE_NAME?lower_case}DmaDescrTable[${SDHC_INSTANCE_NAME}_DMA_NUM_DESCR_LINES];

static volatile SDHC_OBJECT ${SDHC_INSTANCE_NAME?lower_case}Obj;

static void ${SDHC_INSTANCE_NAME}_VariablesInit ( void )
{
    ${SDHC_INSTANCE_NAME?lower_case}Obj.errorStatus = 0;
    ${SDHC_INSTANCE_NAME?lower_case}Obj.isCmdInProgress = false;
    ${SDHC_INSTANCE_NAME?lower_case}Obj.isDataInProgress = false;
    ${SDHC_INSTANCE_NAME?lower_case}Obj.callback = NULL;
}

static void ${SDHC_INSTANCE_NAME}_Delay(uint16_t timeout)
{
    while (timeout > 0U)
    {
        timeout --;
        Nop ();
    }
}

static uint16_t ${SDHC_INSTANCE_NAME}_TransferModeSet ( uint32_t opcode, SDHC_DataTransferFlags transferFlags )
{
    uint16_t transfer_mode_reg = 0;

    switch(opcode)
    {
<#if !SDCARD_EMMCEN>
        case (uint32_t)SDHC_CMD_READ_SCR:
        case (uint32_t)SDHC_CMD_SET_BUS_WIDTH:
<#else>
        case (uint32_t)SDHC_CMD_SEND_EXT_CSD:
</#if>
        case (uint32_t)SDHC_CMD_READ_SINGLE_BLOCK:
            /* Read single block of data from the device. */
            transfer_mode_reg = (_SDHCMODE_DMAEN_MASK | _SDHCMODE_DTXDSEL_MASK);
            break;

        case (uint32_t)SDHC_CMD_READ_MULTI_BLOCK:
            /* Read multiple blocks of data from the device. */
            transfer_mode_reg = (_SDHCMODE_DMAEN_MASK | _SDHCMODE_DTXDSEL_MASK | _SDHCMODE_BSEL_MASK | _SDHCMODE_BCEN_MASK);
            break;

        case (uint32_t)SDHC_CMD_WRITE_SINGLE_BLOCK:
            /* Write single block of data to the device. */
            transfer_mode_reg = _SDHCMODE_DMAEN_MASK;
            break;

        case (uint32_t)SDHC_CMD_WRITE_MULTI_BLOCK:
            /* Write multiple blocks of data to the device. */
            transfer_mode_reg = (_SDHCMODE_DMAEN_MASK | _SDHCMODE_BSEL_MASK | _SDHCMODE_BCEN_MASK);
            break;

        case (uint32_t)SDHC_CMD_IO_RW_EXT:
            if (transferFlags.transferType == SDHC_DATA_TRANSFER_TYPE_SDIO_BLOCK)
            {
                transfer_mode_reg = _SDHCMODE_BSEL_MASK | _SDHCMODE_BCEN_MASK;
            }
            if (transferFlags.transferDir == SDHC_DATA_TRANSFER_DIR_READ)
            {
                transfer_mode_reg |= _SDHCMODE_DTXDSEL_MASK;
            }
            transfer_mode_reg |= _SDHCMODE_DMAEN_MASK;
            break;
        default:
                 /* Nothing to do */
            break;
    }

    return transfer_mode_reg;
}

void __attribute__((used)) ${SDHC_INSTANCE_NAME}_InterruptHandler(void)
{
    uint32_t nistr = 0;
    uint32_t eistr = 0;
    SDHC_XFER_STATUS xferStatus = 0;

    nistr = (${SDHC_INSTANCE_NAME}INTSTAT & 0x0000FFFFU);
    eistr = (${SDHC_INSTANCE_NAME}INTSTAT & 0xFFFF0000U);

    /* Clear the transmit interrupt flag */
    ${SDHC_IFS_REG}CLR = ${SDHC_IFS_REG_MASK}U;

    /* Save the error in a global variable for later use */
    ${SDHC_INSTANCE_NAME?lower_case}Obj.errorStatus |= eistr;
    <#if SDCARD_EMMCEN == false>

    if ((nistr & _SDHCINTSTAT_CARDIIF_MASK) != 0U)
    {
        xferStatus |= SDHC_XFER_STATUS_CARD_INSERTED;
    }
    if ((nistr & _SDHCINTSTAT_CARDRIF_MASK) != 0U)
    {
        xferStatus |= SDHC_XFER_STATUS_CARD_REMOVED;
    }
    </#if>

    if (${SDHC_INSTANCE_NAME?lower_case}Obj.isCmdInProgress == true)
    {
        if ((nistr & (_SDHCINTSTAT_CCIF_MASK | _SDHCINTSTAT_TXCIF_MASK | _SDHCINTSTAT_EIF_MASK)) != 0U)
        {
            if ((nistr & _SDHCINTSTAT_EIF_MASK) != 0U)
            {
                if ((eistr & (_SDHCINTSTAT_CTOEIF_MASK |
                                      _SDHCINTSTAT_CCRCEIF_MASK |
                                      _SDHCINTSTAT_CEBEIF_MASK |
                                      _SDHCINTSTAT_CIDXEIF_MASK)) != 0U)
                {
                    ${SDHC_INSTANCE_NAME}_ErrorReset (SDHC_RESET_CMD);
                }
            }
            ${SDHC_INSTANCE_NAME?lower_case}Obj.isCmdInProgress = false;
            xferStatus |= SDHC_XFER_STATUS_CMD_COMPLETED;
        }
    }

    if (${SDHC_INSTANCE_NAME?lower_case}Obj.isDataInProgress == true)
    {
        if ((nistr & (_SDHCINTSTAT_TXCIF_MASK | _SDHCINTSTAT_DMAIF_MASK | _SDHCINTSTAT_EIF_MASK)) != 0U)
        {
            if ((nistr & _SDHCINTSTAT_EIF_MASK) != 0U)
            {
                if ((eistr & (_SDHCINTSTAT_DTOEIF_MASK |
                            _SDHCINTSTAT_DCRCEIF_MASK |
                            _SDHCINTSTAT_DEBEIF_MASK)) != 0U)
                {
                    ${SDHC_INSTANCE_NAME}_ErrorReset (SDHC_RESET_DAT);
                }
            }
            if ((nistr & _SDHCINTSTAT_TXCIF_MASK) != 0U)
            {
                /* Clear the data timeout error as transfer complete has higher priority */
                ${SDHC_INSTANCE_NAME?lower_case}Obj.errorStatus &= ~_SDHCINTSTAT_DTOEIF_MASK;
            }
            ${SDHC_INSTANCE_NAME?lower_case}Obj.isDataInProgress = false;
            xferStatus |= SDHC_XFER_STATUS_DATA_COMPLETED;
        }
    }

    /* Clear normal interrupt and error status bits that have been processed */
    ${SDHC_INSTANCE_NAME}INTSTAT = (nistr | eistr);

    if ((${SDHC_INSTANCE_NAME?lower_case}Obj.callback != NULL) && (xferStatus > 0U))
    {
        uintptr_t context = ${SDHC_INSTANCE_NAME?lower_case}Obj.context;
        ${SDHC_INSTANCE_NAME?lower_case}Obj.callback(xferStatus, context);
    }
}

void ${SDHC_INSTANCE_NAME}_ErrorReset ( SDHC_RESET_TYPE resetType )
{
    ${SDHC_INSTANCE_NAME}CON2 |= ((uint32_t)resetType << 24);

    /* Wait until host resets the error status */
    while ((${SDHC_INSTANCE_NAME}CON2 & ((uint32_t)resetType << 24)) != 0U)
    {
        /* Nothing to do */
    }
}

uint16_t ${SDHC_INSTANCE_NAME}_GetError(void)
{
    return (uint16_t)${SDHC_INSTANCE_NAME?lower_case}Obj.errorStatus;
}

uint16_t ${SDHC_INSTANCE_NAME}_CommandErrorGet(void)
{
    uint32_t errorStatus = ${SDHC_INSTANCE_NAME?lower_case}Obj.errorStatus;

    errorStatus &= (_SDHCINTSTAT_CTOEIF_MASK | _SDHCINTSTAT_CCRCEIF_MASK | _SDHCINTSTAT_CEBEIF_MASK | _SDHCINTSTAT_CIDXEIF_MASK);

    return (uint16_t)(errorStatus >> 16);
}

uint16_t ${SDHC_INSTANCE_NAME}_DataErrorGet(void)
{
    uint32_t errorStatus = ${SDHC_INSTANCE_NAME?lower_case}Obj.errorStatus;

    errorStatus &= (_SDHCINTSTAT_ADEIF_MASK | _SDHCINTSTAT_DTOEIF_MASK | _SDHCINTSTAT_DCRCEIF_MASK | _SDHCINTSTAT_DEBEIF_MASK);

    return (uint16_t)(errorStatus >> 16);
}

void ${SDHC_INSTANCE_NAME}_BusWidthSet ( SDHC_BUS_WIDTH busWidth )
{
    if (busWidth == SDHC_BUS_WIDTH_4_BIT)
    {
        ${SDHC_INSTANCE_NAME}CON1 |= _SDHCCON1_DTXWIDTH_MASK;
    }
    else
    {
        ${SDHC_INSTANCE_NAME}CON1 &= ~(_SDHCCON1_DTXWIDTH_MASK);
    }
}

void ${SDHC_INSTANCE_NAME}_SpeedModeSet ( SDHC_SPEED_MODE speedMode )
{
    if (speedMode == SDHC_SPEED_MODE_HIGH)
    {
        ${SDHC_INSTANCE_NAME}CON1 |= _SDHCCON1_HSEN_MASK;
    }
    else
    {
       ${SDHC_INSTANCE_NAME}CON1 &= ~(_SDHCCON1_HSEN_MASK);
    }
}

bool ${SDHC_INSTANCE_NAME}_IsCmdLineBusy ( void )
{
    return(((${SDHC_INSTANCE_NAME}STAT1 & _SDHCSTAT1_CINHCMD_MASK) == _SDHCSTAT1_CINHCMD_MASK)? true : false);
}

bool ${SDHC_INSTANCE_NAME}_IsDatLineBusy ( void )
{
    return (((${SDHC_INSTANCE_NAME}STAT1 & _SDHCSTAT1_CINHDAT_MASK) == _SDHCSTAT1_CINHDAT_MASK)? true : false);
}
<#if SDCARD_EMMCEN == false>

void ${SDHC_INSTANCE_NAME}_WriteProtectEnable(void)
{
    CFGCON2bits.SDWPEN = 0x1;
}

void ${SDHC_INSTANCE_NAME}_WriteProtectDisable(void)
{
    CFGCON2bits.SDWPEN = 0x0;
}


bool ${SDHC_INSTANCE_NAME}_IsWriteProtected ( void )
{
    bool writeProtechCheck = false;
    if ((CFGCON2bits.SDWPEN) != 0U)
    {
        /* Write-protect status indication through the WPSLVL bit (SDHCSTAT1<19>) is inverted (See Errata) */
        writeProtechCheck = ((${SDHC_INSTANCE_NAME}STAT1 & _SDHCSTAT1_WPSLVL_MASK) != 0U);
    }
    return writeProtechCheck;
}

void ${SDHC_INSTANCE_NAME}_CardDetectEnable(void)
{
    CFGCON2bits.SDCDEN = 0x1;
}

void ${SDHC_INSTANCE_NAME}_CardDetectDisable(void)
{
    CFGCON2bits.SDCDEN = 0x0;
}

bool ${SDHC_INSTANCE_NAME}_IsCardAttached ( void )
{
    return (((${SDHC_INSTANCE_NAME}STAT1 & _SDHCSTAT1_CARDINS_MASK) == _SDHCSTAT1_CARDINS_MASK) != 0U);
}
</#if>

void ${SDHC_INSTANCE_NAME}_BlockSizeSet ( uint16_t blockSize )
{
    if (blockSize > ${SDHC_INSTANCE_NAME}_MAX_BLOCK_SIZE)
    {
        blockSize = ${SDHC_INSTANCE_NAME}_MAX_BLOCK_SIZE;
    }

    ${SDHC_INSTANCE_NAME}BLKCON = ((${SDHC_INSTANCE_NAME}BLKCON & ~_SDHCBLKCON_BSIZE_MASK) | (blockSize));
}

void ${SDHC_INSTANCE_NAME}_BlockCountSet ( uint16_t numBlocks )
{
    ${SDHC_INSTANCE_NAME}BLKCON = ((${SDHC_INSTANCE_NAME}BLKCON & ~_SDHCBLKCON_BCOUNT_MASK) | ((uint32_t)numBlocks << 16));
}

void ${SDHC_INSTANCE_NAME}_ClockEnable ( void )
{
    /* Enable internal clock */
    ${SDHC_INSTANCE_NAME}CON2 |= _SDHCCON2_ICLKEN_MASK;

    /* Wait for the internal clock to stabilize */
    ${SDHC_INSTANCE_NAME}_Delay(1000);

    /* Enable the SDCLK */
    ${SDHC_INSTANCE_NAME}CON2 |= _SDHCCON2_SDCLKEN_MASK;
}

void ${SDHC_INSTANCE_NAME}_ClockDisable ( void )
{
    ${SDHC_INSTANCE_NAME}CON2 &= ~(_SDHCCON2_ICLKEN_MASK | _SDHCCON2_SDCLKEN_MASK);
}

void ${SDHC_INSTANCE_NAME}_DmaSetup (
    uint8_t* buffer,
    uint32_t numBytes,
    SDHC_DATA_TRANSFER_DIR direction
)
{
    (void)direction;

    /* Each ADMA2 descriptor can transfer 65536 bytes (or 128 blocks) of data.
     * Block count register being a 16 bit register, maximum number of blocks is
     * limited to 65536 blocks. Hence, combined length of data that can be
     * transferred by all the descriptors is 512 bytes x 65536 blocks, assuming
     * a block size of 512 bytes.
     */
<#if SDHC_NUM_DESCRIPTOR_LINES == 1>
    if (numBytes <= 65536U)
    {
        ${SDHC_INSTANCE_NAME?lower_case}DmaDescrTable[0].address = (uint32_t)KVA_TO_PA(buffer);
        ${SDHC_INSTANCE_NAME?lower_case}DmaDescrTable[0].length = (uint16_t)numBytes;
        ${SDHC_INSTANCE_NAME?lower_case}DmaDescrTable[0].attribute = \
            (SDHC_DESC_TABLE_ATTR_XFER_DATA | SDHC_DESC_TABLE_ATTR_VALID | SDHC_DESC_TABLE_ATTR_INTR);

            /* The last descriptor line must indicate the end of the descriptor list */
        ${SDHC_INSTANCE_NAME?lower_case}DmaDescrTable[0].attribute |= (uint16_t)(SDHC_DESC_TABLE_ATTR_END);

          /* Set the starting address of the descriptor table */
        ${SDHC_INSTANCE_NAME}AADDR = (uint32_t)KVA_TO_PA(&${SDHC_INSTANCE_NAME?lower_case}DmaDescrTable[0]);
    }
<#else>
    uint32_t i = 0;
    uint32_t pendingBytes = numBytes;
    uint32_t nBytes = 0;

    if ((pendingBytes > 0U) && (pendingBytes <= (65536U * ${SDHC_INSTANCE_NAME}_DMA_NUM_DESCR_LINES)))
    {
        do
        {
            if (pendingBytes > 65536U)
            {
                nBytes = 65536U;
            }
            else
            {
                nBytes = pendingBytes;
            }
            ${SDHC_INSTANCE_NAME?lower_case}DmaDescrTable[i].address = (uint32_t)KVA_TO_PA(buffer);
            ${SDHC_INSTANCE_NAME?lower_case}DmaDescrTable[i].length = (uint16_t)nBytes;
            ${SDHC_INSTANCE_NAME?lower_case}DmaDescrTable[i].attribute = \
                (SDHC_DESC_TABLE_ATTR_XFER_DATA | SDHC_DESC_TABLE_ATTR_VALID | SDHC_DESC_TABLE_ATTR_INTR);

            pendingBytes = pendingBytes - nBytes;
            i++;
        }while((i < ${SDHC_INSTANCE_NAME}_DMA_NUM_DESCR_LINES) && (pendingBytes > 0U));


        /* The last descriptor line must indicate the end of the descriptor list */
        ${SDHC_INSTANCE_NAME?lower_case}DmaDescrTable[i-1U].attribute |= (uint16_t)(SDHC_DESC_TABLE_ATTR_END);

        /* Set the starting address of the descriptor table */
        ${SDHC_INSTANCE_NAME}AADDR = (uint32_t)KVA_TO_PA(&${SDHC_INSTANCE_NAME?lower_case}DmaDescrTable[0]);
    }
</#if>
}

<#assign SDHC_CLOCK = "core." + SDHC_INSTANCE_NAME + "_CLOCK_FREQUENCY">

bool ${SDHC_INSTANCE_NAME}_ClockSet ( uint32_t speed)
{
    uint32_t divs = 0;
    uint32_t sdhc_clk = ${SDHC_CLOCK?eval};

    /* Disable clock before changing it */
    if ((${SDHC_INSTANCE_NAME}CON2 & _SDHCCON2_SDCLKEN_MASK) != 0U)
    {
        while ((${SDHC_INSTANCE_NAME}STAT1 & (_SDHCSTAT1_CINHCMD_MASK | _SDHCSTAT1_CINHCMD_MASK)) != 0U)
        {
            /* Nothing to do */
        }
        ${SDHC_INSTANCE_NAME}CON2 &= ~(_SDHCCON2_SDCLKEN_MASK | _SDHCCON2_ICLKEN_MASK);
    }

    if (speed < sdhc_clk)
    {
        divs = sdhc_clk / speed;
        divs >>= 1;
    }

    /* Bits 15-8 sdclock frequency select */
    ${SDHC_INSTANCE_NAME}CON2 = ((${SDHC_INSTANCE_NAME}CON2 & ~_SDHCCON2_SDCLKDIV_MASK) | ((divs & 0xFFU) << 8));

    /* Bits 7-6 Upper bits of sdclock frequency select */
    ${SDHC_INSTANCE_NAME}CON2 = ((${SDHC_INSTANCE_NAME}CON2 & ~(0x000000C0U)) | (((divs & 0x3FFU) >> 8) << 6));

    /* Enable internal clock */
    ${SDHC_INSTANCE_NAME}CON2 |= _SDHCCON2_ICLKEN_MASK;

    return true;
}

void ${SDHC_INSTANCE_NAME}_ResponseRead (
    SDHC_READ_RESPONSE_REG respReg,
    uint32_t* response
)
{
    switch (respReg)
    {
        case SDHC_READ_RESP_REG_1:
            *response = ${SDHC_INSTANCE_NAME}RESP1;
            break;

        case SDHC_READ_RESP_REG_2:
            *response = ${SDHC_INSTANCE_NAME}RESP2;
            break;

        case SDHC_READ_RESP_REG_3:
            *response = ${SDHC_INSTANCE_NAME}RESP3;
            break;

        case SDHC_READ_RESP_REG_ALL:
            response[0] = ${SDHC_INSTANCE_NAME}RESP0;
            response[1] = ${SDHC_INSTANCE_NAME}RESP1;
            response[2] = ${SDHC_INSTANCE_NAME}RESP2;
            response[3] = ${SDHC_INSTANCE_NAME}RESP3;
            break;

        case SDHC_READ_RESP_REG_0:
        default:
            *response = ${SDHC_INSTANCE_NAME}RESP0;
            break;
    }
}

void ${SDHC_INSTANCE_NAME}_CommandSend (
    uint8_t opCode,
    uint32_t argument,
    uint8_t respType,
    SDHC_DataTransferFlags transferFlags
)
{
    uint32_t mode_reg = 0;
    uint32_t cmd_reg = 0;
    uint32_t transfer_mode_reg = 0;
    uint16_t normal_int_sig_enable_reg = 0;

    /* Clear the flags */
    ${SDHC_INSTANCE_NAME?lower_case}Obj.isCmdInProgress = false;
    ${SDHC_INSTANCE_NAME?lower_case}Obj.isDataInProgress = false;
    ${SDHC_INSTANCE_NAME?lower_case}Obj.errorStatus = 0;

<#if SDCARD_EMMCEN == false>
    /* Keep the card insertion and removal interrupts enabled */
    normal_int_sig_enable_reg = (_SDHCINTSEN_CARDIISE_MASK | _SDHCINTSEN_CARDRISE_MASK);
</#if>

    switch (respType)
    {
        case (uint8_t)SDHC_CMD_RESP_R1:
        case (uint8_t)SDHC_CMD_RESP_R5:
        case (uint8_t)SDHC_CMD_RESP_R6:
        case (uint8_t)SDHC_CMD_RESP_R7:
            cmd_reg = (SDHC_MODE_RESPTYPE_48_BIT | _SDHCMODE_CCRCCEN_MASK | _SDHCMODE_CIDXCEN_MASK);
            break;

        case (uint8_t)SDHC_CMD_RESP_R3:
        case (uint8_t)SDHC_CMD_RESP_R4:
            cmd_reg = SDHC_MODE_RESPTYPE_48_BIT;
            break;

        case (uint8_t)SDHC_CMD_RESP_R1B:
            cmd_reg = (SDHC_MODE_RESPTYPE_48_BIT_BUSY | _SDHCMODE_CCRCCEN_MASK | _SDHCMODE_CIDXCEN_MASK);

            /* Commands with busy response will wait for transfer complete bit */
            normal_int_sig_enable_reg |= _SDHCINTSEN_TXCISE_MASK;
            break;

        case (uint8_t)SDHC_CMD_RESP_R2:
            cmd_reg = (SDHC_MODE_RESPTYPE_136_BIT | _SDHCMODE_CCRCCEN_MASK);
            break;

        default:
            cmd_reg = SDHC_MODE_RESPTYPE_NONE;
            break;
    }

    /* Enable command complete interrupt, for commands that do not have busy response type */
    if (respType != (uint8_t)SDHC_CMD_RESP_R1B)
    {
        normal_int_sig_enable_reg |= _SDHCINTSEN_CCISE_MASK;
    }

    if (transferFlags.isDataPresent == true)
    {
        ${SDHC_INSTANCE_NAME?lower_case}Obj.isDataInProgress = true;
        cmd_reg |= ((uint32_t)transferFlags.isDataPresent << _SDHCMODE_DPSEL_POSITION);
        transfer_mode_reg = ${SDHC_INSTANCE_NAME}_TransferModeSet(opCode, transferFlags);
        /* Enable data transfer complete and DMA interrupt */
        normal_int_sig_enable_reg |= (_SDHCINTSEN_TXCISE_MASK | _SDHCINTSEN_DMAISE_MASK);
    }

    /* Enable all error interrupt signals and required normal interrupt signals */
    ${SDHC_INSTANCE_NAME}INTSEN = (SDHC_EISIER_Msk | normal_int_sig_enable_reg);

    ${SDHC_INSTANCE_NAME}ARG = argument;

    ${SDHC_INSTANCE_NAME?lower_case}Obj.isCmdInProgress = true;

    mode_reg = ( ((uint32_t)opCode << _SDHCMODE_CIDX_POSITION) | cmd_reg | transfer_mode_reg);
    ${SDHC_INSTANCE_NAME}MODE = mode_reg;
}

void ${SDHC_INSTANCE_NAME}_ModuleInit( void )
{
<#if SDCARD_EMMCEN == false && SDCARD_SDWPEN == true>
    /* Enable SDWPEN# pin */
    CFGCON2bits.SDWPEN = 0x1;
<#else>
    /* Disable SDWPEN# pin */
    CFGCON2bits.SDWPEN = 0x0;
</#if>

    CFGCON2bits.SDRDFTHR = 0x200;
    CFGCON2bits.SDWRFTHR = 0x200;

    /* Reset module*/
    ${SDHC_INSTANCE_NAME}CON2 |= _SDHCCON2_SWRALL_MASK;
    while((${SDHC_INSTANCE_NAME}CON2 & _SDHCCON2_SWRALL_MASK) == _SDHCCON2_SWRALL_MASK)
    {
        /* Nothing to do */
    }

    /* Clear the normal and error interrupt status flags */
    ${SDHC_INSTANCE_NAME}INTSTAT = ${SDHC_INSTANCE_NAME}INTSTAT;

    /* Enable all the normal interrupt status and error status generation */
    ${SDHC_INSTANCE_NAME}INTEN = SDHC_INTEN_Msk;

    /* Set timeout control register */
    ${SDHC_INSTANCE_NAME}CON2 = ((${SDHC_INSTANCE_NAME}CON2 & ~_SDHCCON2_DTOC_MASK) | (0x0EUL << _SDHCCON2_DTOC_POSITION));

    /* Enable ADMA2 (Check CA0R capability register first) */
    ${SDHC_INSTANCE_NAME}CON1 = ((${SDHC_INSTANCE_NAME}CON1 & ~_SDHCCON1_DMASEL_MASK) | (0x02UL << _SDHCCON1_DMASEL_POSITION));

<#if SDCARD_EMMCEN == false && SDCARD_SDCDEN == true>
    /* Enable the card detect line SDCD */
    CFGCON2bits.SDCDEN = 0x1;

    /* SD Bus Voltage Select = 3.3V, SD Bus Power = On */
    ${SDHC_INSTANCE_NAME}CON1 |= _SDHCCON1_SDBP_MASK;
<#else>
    /* Disable the card detect line SDCD */
    CFGCON2bits.SDCDEN = 0x0;

    /* If card detect has not been enabled then enable the card detect
     * signal select. Refer to the SDHC errata. SD Bus Power = On */
    ${SDHC_INSTANCE_NAME}CON1 |= (_SDHCCON1_CDSSEL_MASK | _SDHCCON1_SDBP_MASK);
</#if>

    /* Set initial clock to 400 KHz*/
   (void) ${SDHC_INSTANCE_NAME}_ClockSet (SDHC_CLOCK_FREQ_400_KHZ);

    /* Wait for the internal clock to stabilize */
    ${SDHC_INSTANCE_NAME}_Delay(1000);

    /* Enable the SDCLK */
    ${SDHC_INSTANCE_NAME}CON2 |= _SDHCCON2_SDCLKEN_MASK;

    /* Clear the high speed bit and set the data width to 1-bit mode */
    ${SDHC_INSTANCE_NAME}CON1 &= ~(_SDHCCON1_HSEN_MASK | _SDHCCON1_DTXWIDTH_MASK);
<#if SDCARD_EMMCEN == false>

    /* Enable card inserted and card removed interrupt signals */
    ${SDHC_INSTANCE_NAME}INTSEN = (_SDHCINTSEN_CARDIISE_MASK | _SDHCINTSEN_CARDRISE_MASK);
</#if>
    /* Enable SDHC interrupt */
    ${SDHC_IEC_REG}SET = ${SDHC_IEC_REG_MASK}U;
}

void ${SDHC_INSTANCE_NAME}_Initialize( void )
{
    ${SDHC_INSTANCE_NAME}_VariablesInit();
    ${SDHC_INSTANCE_NAME}_ModuleInit();
}

void ${SDHC_INSTANCE_NAME}_CallbackRegister(SDHC_CALLBACK callback, uintptr_t contextHandle)
{
    if (callback != NULL)
    {
        ${SDHC_INSTANCE_NAME?lower_case}Obj.callback = callback;
        ${SDHC_INSTANCE_NAME?lower_case}Obj.context = contextHandle;
    }
}