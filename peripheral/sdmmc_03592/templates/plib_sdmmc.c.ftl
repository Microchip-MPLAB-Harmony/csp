/*******************************************************************************
  ${SDMMC_INSTANCE_NAME} PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${SDMMC_INSTANCE_NAME?lower_case}.c

  Summary:
    ${SDMMC_INSTANCE_NAME} PLIB Implementation File

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
#include "plib_${SDMMC_INSTANCE_NAME?lower_case}.h"
<#if core.CoreSysIntFile == true>
#include "interrupts.h"
</#if>

// *****************************************************************************
// *****************************************************************************
// Section: Include Files
// *****************************************************************************
// *****************************************************************************

#include "plib_sdmmc_common.h"

#define ${SDMMC_INSTANCE_NAME}_DMA_NUM_DESCR_LINES        ${SDMMC_NUM_DESCRIPTOR_LINES}
#define ${SDMMC_INSTANCE_NAME}_BASE_CLOCK_FREQUENCY       ${SDMMC_CLK_FREQ}
#define ${SDMMC_INSTANCE_NAME}_MAX_BLOCK_SIZE                   0x200

static       SDMMC_ADMA_DESCR ${SDMMC_INSTANCE_NAME?lower_case}DmaDescrTable[${SDMMC_INSTANCE_NAME}_DMA_NUM_DESCR_LINES] __ALIGNED(32);

static SDMMC_OBJECT ${SDMMC_INSTANCE_NAME?lower_case}Obj;

static void ${SDMMC_INSTANCE_NAME}_VariablesInit ( void )
{
    ${SDMMC_INSTANCE_NAME?lower_case}Obj.errorStatus = 0;
    ${SDMMC_INSTANCE_NAME?lower_case}Obj.isCmdInProgress = false;
    ${SDMMC_INSTANCE_NAME?lower_case}Obj.isDataInProgress = false;
    ${SDMMC_INSTANCE_NAME?lower_case}Obj.callback = NULL;
}

static void ${SDMMC_INSTANCE_NAME}_TransferModeSet ( uint32_t opcode )
{
    uint16_t transferMode = 0;

    switch(opcode)
    {
<#if !SDCARD_EMMCEN>
        case SDMMC_CMD_READ_SCR:
        case SDMMC_CMD_SET_BUS_WIDTH:
<#else>
        case SDMMC_CMD_SEND_EXT_CSD:
</#if>
        case SDMMC_CMD_READ_SINGLE_BLOCK:
            /* Read single block of data from the device. */
            transferMode = (SDMMC_TMR_DMAEN_ENABLE | SDMMC_TMR_DTDSEL_Msk);
            break;

        case SDMMC_CMD_READ_MULTI_BLOCK:
            /* Read multiple blocks of data from the device. */
            transferMode = (SDMMC_TMR_DMAEN_ENABLE | SDMMC_TMR_DTDSEL_Msk | SDMMC_TMR_MSBSEL_Msk | SDMMC_TMR_BCEN_Msk);
            break;

        case SDMMC_CMD_WRITE_SINGLE_BLOCK:
            /* Write single block of data to the device. */
            transferMode = SDMMC_TMR_DMAEN_ENABLE;
            break;

        case SDMMC_CMD_WRITE_MULTI_BLOCK:
            /* Write multiple blocks of data to the device. */
            transferMode = (SDMMC_TMR_DMAEN_ENABLE | SDMMC_TMR_MSBSEL_Msk | SDMMC_TMR_BCEN_Msk);
            break;

        default:
            break;
    }

    ${SDMMC_INSTANCE_NAME}_REGS->SDMMC_TMR = transferMode;
}

void ${SDMMC_INSTANCE_NAME}_InterruptHandler(void)
{
    uint16_t nistr = 0;
    uint16_t eistr = 0;
    SDMMC_XFER_STATUS xferStatus = (SDMMC_XFER_STATUS) 0;

    nistr = ${SDMMC_INSTANCE_NAME}_REGS->SDMMC_NISTR;
    eistr = ${SDMMC_INSTANCE_NAME}_REGS->SDMMC_EISTR;
    /* Save the error in a global variable for later use */
    ${SDMMC_INSTANCE_NAME?lower_case}Obj.errorStatus |= eistr;
    <#if SDCARD_EMMCEN == false && SDCARD_SDCDEN == true>

    if (nistr & SDMMC_NISTR_CINS_Msk)
    {
        xferStatus |= SDMMC_XFER_STATUS_CARD_INSERTED;
    }
    if (nistr & SDMMC_NISTR_CREM_Msk)
    {
        xferStatus |= SDMMC_XFER_STATUS_CARD_REMOVED;
    }
    </#if>

    if (${SDMMC_INSTANCE_NAME?lower_case}Obj.isCmdInProgress == true)
    {
        if (nistr & (SDMMC_NISTR_CMDC_Msk | SDMMC_NISTR_TRFC_Msk | SDMMC_NISTR_ERRINT_Msk))
        {
            if (nistr & SDMMC_NISTR_ERRINT_Msk)
            {
                if (eistr & (SDMMC_EISTR_CMDTEO_Msk | \
                                      SDMMC_EISTR_CMDCRC_Msk | \
                                      SDMMC_EISTR_CMDEND_Msk | \
                                      SDMMC_EISTR_CMDIDX_Msk))
                {
                    ${SDMMC_INSTANCE_NAME}_ErrorReset (SDMMC_RESET_CMD);
                }
            }
            ${SDMMC_INSTANCE_NAME?lower_case}Obj.isCmdInProgress = false;
            xferStatus |= SDMMC_XFER_STATUS_CMD_COMPLETED;
        }
    }

    if (${SDMMC_INSTANCE_NAME?lower_case}Obj.isDataInProgress == true)
    {
        if (nistr & (SDMMC_NISTR_TRFC_Msk | SDMMC_NISTR_DMAINT_Msk | SDMMC_NISTR_ERRINT_Msk))
        {
            if (nistr & SDMMC_NISTR_ERRINT_Msk)
            {
                if (eistr & (SDMMC_EISTR_DATTEO_Msk | \
                            SDMMC_EISTR_DATCRC_Msk | \
                            SDMMC_EISTR_DATEND_Msk))
                {
                    ${SDMMC_INSTANCE_NAME}_ErrorReset (SDMMC_RESET_DAT);
                }
            }
            if (nistr & SDMMC_NISTR_TRFC_Msk)
            {
                /* Clear the data timeout error as transfer complete has higher priority */
                ${SDMMC_INSTANCE_NAME?lower_case}Obj.errorStatus &= ~SDMMC_EISTR_DATTEO_Msk;
            }
            ${SDMMC_INSTANCE_NAME?lower_case}Obj.isDataInProgress = false;
            xferStatus |= SDMMC_XFER_STATUS_DATA_COMPLETED;
        }
    }

    /* Clear normal interrupt and error status bits that have been processed */
    ${SDMMC_INSTANCE_NAME}_REGS->SDMMC_NISTR = nistr;
    ${SDMMC_INSTANCE_NAME}_REGS->SDMMC_EISTR = eistr;

    if ((${SDMMC_INSTANCE_NAME?lower_case}Obj.callback != NULL) && (xferStatus > 0))
    {
        ${SDMMC_INSTANCE_NAME?lower_case}Obj.callback(xferStatus, ${SDMMC_INSTANCE_NAME?lower_case}Obj.context);
    }
}

void ${SDMMC_INSTANCE_NAME}_ErrorReset ( SDMMC_RESET_TYPE resetType )
{
    ${SDMMC_INSTANCE_NAME}_REGS->SDMMC_SRR = resetType;

    /* Wait until host resets the error status */
    while (${SDMMC_INSTANCE_NAME}_REGS->SDMMC_SRR & resetType);
}

uint16_t ${SDMMC_INSTANCE_NAME}_GetError(void)
{
    return ${SDMMC_INSTANCE_NAME?lower_case}Obj.errorStatus;
}

uint16_t ${SDMMC_INSTANCE_NAME}_CommandErrorGet(void)
{
    return (${SDMMC_INSTANCE_NAME?lower_case}Obj.errorStatus & (SDMMC_EISTR_CMDTEO_Msk | SDMMC_EISTR_CMDCRC_Msk | \
                SDMMC_EISTR_CMDEND_Msk | SDMMC_EISTR_CMDIDX_Msk));
}

uint16_t ${SDMMC_INSTANCE_NAME}_DataErrorGet(void)
{
    return (${SDMMC_INSTANCE_NAME?lower_case}Obj.errorStatus & (SDMMC_EISTR_ADMA_Msk | SDMMC_EISTR_DATTEO_Msk | \
            SDMMC_EISTR_DATCRC_Msk | SDMMC_EISTR_DATEND_Msk));
}

void ${SDMMC_INSTANCE_NAME}_BusWidthSet ( SDMMC_BUS_WIDTH busWidth )
{
    if (busWidth == SDMMC_BUS_WIDTH_4_BIT)
    {
       ${SDMMC_INSTANCE_NAME}_REGS->SDMMC_HC1R |= SDMMC_HC1R_DW_4BIT;
    }
    else
    {
        ${SDMMC_INSTANCE_NAME}_REGS->SDMMC_HC1R &= ~SDMMC_HC1R_DW_4BIT;
    }
}

void ${SDMMC_INSTANCE_NAME}_SpeedModeSet ( SDMMC_SPEED_MODE speedMode )
{
    if (speedMode == SDMMC_SPEED_MODE_HIGH)
    {
       ${SDMMC_INSTANCE_NAME}_REGS->SDMMC_HC1R |= SDMMC_HC1R_HSEN_Msk;
    }
    else
    {
       ${SDMMC_INSTANCE_NAME}_REGS->SDMMC_HC1R &= ~SDMMC_HC1R_HSEN_Msk;
    }
}

bool ${SDMMC_INSTANCE_NAME}_IsCmdLineBusy ( void )
{
    return(((${SDMMC_INSTANCE_NAME}_REGS->SDMMC_PSR & SDMMC_PSR_CMDINHC_Msk) == SDMMC_PSR_CMDINHC_Msk)? true : false);
}

bool ${SDMMC_INSTANCE_NAME}_IsDatLineBusy ( void )
{
    return (((${SDMMC_INSTANCE_NAME}_REGS->SDMMC_PSR & SDMMC_PSR_CMDINHD_Msk) == SDMMC_PSR_CMDINHD_Msk)? true : false);
}
<#if SDCARD_EMMCEN == false && SDCARD_SDWPEN == true>

bool ${SDMMC_INSTANCE_NAME}_IsWriteProtected ( void )
{
    return (${SDMMC_INSTANCE_NAME}_REGS->SDMMC_PSR & SDMMC_PSR_WRPPL_Msk) ? false : true;
}
</#if>
<#if SDCARD_EMMCEN == false && SDCARD_SDCDEN == true>

bool ${SDMMC_INSTANCE_NAME}_IsCardAttached ( void )
{
    return ((${SDMMC_INSTANCE_NAME}_REGS->SDMMC_PSR & SDMMC_PSR_CARDINS_Msk) == SDMMC_PSR_CARDINS_Msk)? true : false;
}
</#if>

void ${SDMMC_INSTANCE_NAME}_BlockSizeSet ( uint16_t blockSize )
{
    if(blockSize == 0)
    {
        blockSize = 1;
    }
    else if(blockSize > ${SDMMC_INSTANCE_NAME}_MAX_BLOCK_SIZE)
    {
        blockSize = ${SDMMC_INSTANCE_NAME}_MAX_BLOCK_SIZE;
    }
    else
    {
      /* Do not modify the block size */
    }
    ${SDMMC_INSTANCE_NAME}_REGS->SDMMC_BSR = (SDMMC_BSR_BOUNDARY_4K | SDMMC_BSR_BLOCKSIZE(blockSize));
}

void ${SDMMC_INSTANCE_NAME}_BlockCountSet ( uint16_t numBlocks )
{
    ${SDMMC_INSTANCE_NAME}_REGS->SDMMC_BCR = numBlocks;
}

void ${SDMMC_INSTANCE_NAME}_ClockEnable ( void )
{
    /* Start the internal clock  */
    ${SDMMC_INSTANCE_NAME}_REGS->SDMMC_CCR |= SDMMC_CCR_INTCLKEN_Msk;

    /* Wait for the internal clock to stabilize */
    while (!(${SDMMC_INSTANCE_NAME}_REGS->SDMMC_CCR & SDMMC_CCR_INTCLKS_Msk)) ;

    /* Enable the SD Clock */
    ${SDMMC_INSTANCE_NAME}_REGS->SDMMC_CCR |= SDMMC_CCR_SDCLKEN_Msk;
}

void ${SDMMC_INSTANCE_NAME}_ClockDisable ( void )
{
    ${SDMMC_INSTANCE_NAME}_REGS->SDMMC_CCR &= ~(SDMMC_CCR_INTCLKEN_Msk | SDMMC_CCR_SDCLKEN_Msk);
}

void ${SDMMC_INSTANCE_NAME}_DmaSetup (
    uint8_t* buffer,
    uint32_t numBytes,
    SDMMC_DATA_TRANSFER_DIR direction
)
{
    uint32_t i;
    uint32_t pendingBytes = numBytes;
    uint32_t nBytes = 0;

    (void)direction;

    /* Each ADMA2 descriptor can transfer 65536 bytes (or 128 blocks) of data.
     * Block count register being a 16 bit register, maximum number of blocks is
     * limited to 65536 blocks. Hence, combined length of data that can be
     * transferred by all the descriptors is 512 bytes x 65536 blocks, assuming
     * a block size of 512 bytes.
     */

    if (pendingBytes > (65536 * ${SDMMC_INSTANCE_NAME}_DMA_NUM_DESCR_LINES))
    {
        /* Too many blocks requested in one go */
        return;
    }

    for (i = 0; (i < ${SDMMC_INSTANCE_NAME}_DMA_NUM_DESCR_LINES) && (pendingBytes > 0); i++)
    {
        if (pendingBytes > 65536)
        {
            nBytes = 65536;
        }
        else
        {
            nBytes = pendingBytes;
        }
        ${SDMMC_INSTANCE_NAME?lower_case}DmaDescrTable[i].address = (uint32_t)(buffer);
        ${SDMMC_INSTANCE_NAME?lower_case}DmaDescrTable[i].length = nBytes;
        ${SDMMC_INSTANCE_NAME?lower_case}DmaDescrTable[i].attribute = \
            (SDMMC_DESC_TABLE_ATTR_XFER_DATA | SDMMC_DESC_TABLE_ATTR_VALID | SDMMC_DESC_TABLE_ATTR_INTR);

        pendingBytes = pendingBytes - nBytes;
    }

    /* The last descriptor line must indicate the end of the descriptor list */
    ${SDMMC_INSTANCE_NAME?lower_case}DmaDescrTable[i-1].attribute |= (SDMMC_DESC_TABLE_ATTR_END);

    /* Clean the cache associated with the modified descriptors */
    DCACHE_CLEAN_BY_ADDR((uint32_t*)(${SDMMC_INSTANCE_NAME?lower_case}DmaDescrTable), (i * sizeof(SDMMC_ADMA_DESCR)));

    /* Set the starting address of the descriptor table */
    ${SDMMC_INSTANCE_NAME}_REGS->SDMMC_ASAR = (uint32_t)(&${SDMMC_INSTANCE_NAME?lower_case}DmaDescrTable[0]);
}

bool ${SDMMC_INSTANCE_NAME}_ClockSet ( uint32_t speed)
{
    uint32_t baseclk_frq = 0;
    uint16_t divider = 0;
    uint32_t clkmul = 0;
    SDMMC_CLK_MODE clkMode = SDMMC_PROGRAMMABLE_CLK_MODE;

    /* Disable clock before changing it */
    if (${SDMMC_INSTANCE_NAME}_REGS->SDMMC_CCR & SDMMC_CCR_SDCLKEN_Msk)
    {
        while (${SDMMC_INSTANCE_NAME}_REGS->SDMMC_PSR & (SDMMC_PSR_CMDINHC_Msk | SDMMC_PSR_CMDINHD_Msk));
        ${SDMMC_INSTANCE_NAME}_REGS->SDMMC_CCR &= ~SDMMC_CCR_SDCLKEN_Msk;
    }

    /* Get the base clock frequency */
    baseclk_frq = (${SDMMC_INSTANCE_NAME}_REGS->SDMMC_CA0R & (SDMMC_CA0R_BASECLKF_Msk)) >> SDMMC_CA0R_BASECLKF_Pos;
    if (baseclk_frq == 0)
    {
        baseclk_frq = ${SDMMC_INSTANCE_NAME}_BASE_CLOCK_FREQUENCY/2;
    }
    else
    {
        baseclk_frq *= 1000000;
    }

    if (clkMode == SDMMC_DIVIDED_CLK_MODE)
    {
        /* F_SDCLK = F_BASECLK/(2 x DIV).
           For a given F_SDCLK, DIV = F_BASECLK/(2 x F_SDCLK)
        */

        divider =  baseclk_frq/(2 * speed);
        ${SDMMC_INSTANCE_NAME}_REGS->SDMMC_CCR &= ~SDMMC_CCR_CLKGSEL_Msk;
    }
    else
    {
        clkmul = (${SDMMC_INSTANCE_NAME}_REGS->SDMMC_CA1R & (SDMMC_CA1R_CLKMULT_Msk)) >> SDMMC_CA1R_CLKMULT_Pos;
        if (clkmul > 0)
        {
            /* F_SDCLK = F_MULTCLK/(DIV+1), where F_MULTCLK = F_BASECLK x (CLKMULT+1)
               F_SDCLK = (F_BASECLK x (CLKMULT + 1))/(DIV + 1)
               For a given F_SDCLK, DIV = [(F_BASECLK x (CLKMULT + 1))/F_SDCLK] - 1
            */
            divider = (baseclk_frq * (clkmul + 1)) / speed;
            if (divider > 0)
            {
                divider = divider - 1;
            }
            ${SDMMC_INSTANCE_NAME}_REGS->SDMMC_CCR |= SDMMC_CCR_CLKGSEL_Msk;
        }
        else
        {
            /* Programmable clock mode is not supported */
            return false;
        }
    }

    if (speed > SDMMC_CLOCK_FREQ_DS_25_MHZ)
    {
        /* Enable the high speed mode */
        ${SDMMC_INSTANCE_NAME}_REGS->SDMMC_HC1R |= SDMMC_HC1R_HSEN_Msk;
    }
    else
    {
        /* Clear the high speed mode */
        ${SDMMC_INSTANCE_NAME}_REGS->SDMMC_HC1R &= ~SDMMC_HC1R_HSEN_Msk;
    }

    if ((${SDMMC_INSTANCE_NAME}_REGS->SDMMC_HC1R & SDMMC_HC1R_HSEN_Msk) && (divider == 0))
    {
        /* IP limitation, if high speed mode is active divider must be non zero */
        divider = 1;
    }

    /* Set the divider */
    ${SDMMC_INSTANCE_NAME}_REGS->SDMMC_CCR &= ~(SDMMC_CCR_SDCLKFSEL_Msk | SDMMC_CCR_USDCLKFSEL_Msk);
    ${SDMMC_INSTANCE_NAME}_REGS->SDMMC_CCR |= SDMMC_CCR_SDCLKFSEL((divider & 0xff)) | SDMMC_CCR_USDCLKFSEL((divider >> 8));

    /* Enable internal clock */
    ${SDMMC_INSTANCE_NAME}_REGS->SDMMC_CCR |= SDMMC_CCR_INTCLKEN_Msk;

    /* Wait for the internal clock to stabilize */
    while((${SDMMC_INSTANCE_NAME}_REGS->SDMMC_CCR & SDMMC_CCR_INTCLKS_Msk) == 0);

    /* Enable the SDCLK */
    ${SDMMC_INSTANCE_NAME}_REGS->SDMMC_CCR |= SDMMC_CCR_SDCLKEN_Msk;

    return true;
}

void ${SDMMC_INSTANCE_NAME}_ResponseRead (
    SDMMC_READ_RESPONSE_REG respReg,
    uint32_t* response
)
{
    switch (respReg)
    {
        case SDMMC_READ_RESP_REG_0:
        default:
            *response = ${SDMMC_INSTANCE_NAME}_REGS->SDMMC_RR[0];
            break;

        case SDMMC_READ_RESP_REG_1:
            *response = ${SDMMC_INSTANCE_NAME}_REGS->SDMMC_RR[1];
            break;

        case SDMMC_READ_RESP_REG_2:
            *response = ${SDMMC_INSTANCE_NAME}_REGS->SDMMC_RR[2];
            break;

        case SDMMC_READ_RESP_REG_3:
            *response = ${SDMMC_INSTANCE_NAME}_REGS->SDMMC_RR[3];
            break;

        case SDMMC_READ_RESP_REG_ALL:
            response[0] = ${SDMMC_INSTANCE_NAME}_REGS->SDMMC_RR[0];
            response[1] = ${SDMMC_INSTANCE_NAME}_REGS->SDMMC_RR[1];
            response[2] = ${SDMMC_INSTANCE_NAME}_REGS->SDMMC_RR[2];
            response[3] = ${SDMMC_INSTANCE_NAME}_REGS->SDMMC_RR[3];
            break;
    }
}

void ${SDMMC_INSTANCE_NAME}_CommandSend (
    uint8_t opCode,
    uint32_t argument,
    uint8_t respType,
    SDMMC_DataTransferFlags transferFlags
)
{
    uint16_t cmd = 0;
    uint16_t normalIntSigEnable = 0;
    uint8_t flags = 0;

    /* Clear the flags */
    ${SDMMC_INSTANCE_NAME?lower_case}Obj.isCmdInProgress = false;
    ${SDMMC_INSTANCE_NAME?lower_case}Obj.isDataInProgress = false;
    ${SDMMC_INSTANCE_NAME?lower_case}Obj.errorStatus = 0;

<#if SDCARD_EMMCEN == false && SDCARD_SDCDEN == true>
    /* Keep the card insertion and removal interrupts enabled */
    normalIntSigEnable = (SDMMC_NISIER_CINS_Msk | SDMMC_NISIER_CREM_Msk);
</#if>

    switch (respType)
    {
        case SDMMC_CMD_RESP_R1:
        case SDMMC_CMD_RESP_R5:
        case SDMMC_CMD_RESP_R6:
        case SDMMC_CMD_RESP_R7:
            flags = (SDMMC_CR_RESPTYP_48_BIT_Val | SDMMC_CR_CMDCCEN_Msk | SDMMC_CR_CMDICEN_Msk);
            break;

        case SDMMC_CMD_RESP_R3:
        case SDMMC_CMD_RESP_R4:
            flags = SDMMC_CR_RESPTYP_48_BIT_Val;
            break;

        case SDMMC_CMD_RESP_R1B:
            flags = (SDMMC_CR_RESPTYP_48_BIT_BUSY_Val | SDMMC_CR_CMDCCEN_Msk | SDMMC_CR_CMDICEN_Msk);

            /* Commands with busy response will wait for transfer complete bit */
            normalIntSigEnable |= SDMMC_NISIER_TRFC_Msk;
            break;

        case SDMMC_CMD_RESP_R2:
            flags = (SDMMC_CR_RESPTYP_136_BIT_Val | SDMMC_CR_CMDCCEN_Msk);
            break;

        default:
            flags = SDMMC_CR_RESPTYP_NONE_Val;
            break;
    }

    /* Enable command complete interrupt, for commands that do not have busy response type */
    if (respType != SDMMC_CMD_RESP_R1B)
    {
        normalIntSigEnable |= SDMMC_NISIER_CMDC_Msk;
    }

    if (transferFlags.isDataPresent == true)
    {
        ${SDMMC_INSTANCE_NAME?lower_case}Obj.isDataInProgress = true;
        ${SDMMC_INSTANCE_NAME}_TransferModeSet(opCode);
        /* Enable data transfer complete and DMA interrupt */
        normalIntSigEnable |= (SDMMC_NISIER_TRFC_Msk | SDMMC_NISIER_DMAINT_Msk);
    }
    else
    {
        ${SDMMC_INSTANCE_NAME}_REGS->SDMMC_TMR = 0;
    }

    /* Enable the needed normal interrupt signals */
    ${SDMMC_INSTANCE_NAME}_REGS->SDMMC_NISIER = normalIntSigEnable;

    /* Enable all the error interrupt signals */
    ${SDMMC_INSTANCE_NAME}_REGS->SDMMC_EISIER = SDMMC_EISIER_Msk;

    ${SDMMC_INSTANCE_NAME}_REGS->SDMMC_ARG1R = argument;

    ${SDMMC_INSTANCE_NAME?lower_case}Obj.isCmdInProgress = true;

    cmd = (SDMMC_CR_CMDIDX(opCode) | (transferFlags.isDataPresent << SDMMC_CR_DPSEL_Pos) | flags);
    ${SDMMC_INSTANCE_NAME}_REGS->SDMMC_CR = cmd;
}

<#compress>
<#-- Enable FCD if the mode of operation is EMMC or if CD capability exists but is not enabled  -->
<#assign USE_FCD = SDCARD_EMMCEN || (SDCARD_SDCD_SUPPORT && !SDCARD_SDCDEN)>
</#compress>
void ${SDMMC_INSTANCE_NAME}_ModuleInit( void )
{
    /* Reset module*/
    ${SDMMC_INSTANCE_NAME}_REGS->SDMMC_SRR |= SDMMC_SRR_SWRSTALL_Msk;
    while((${SDMMC_INSTANCE_NAME}_REGS->SDMMC_SRR & SDMMC_SRR_SWRSTALL_Msk) == SDMMC_SRR_SWRSTALL_Msk);

    /* Clear the normal and error interrupt status flags */
    ${SDMMC_INSTANCE_NAME}_REGS->SDMMC_EISTR = SDMMC_EISTR_Msk;
    ${SDMMC_INSTANCE_NAME}_REGS->SDMMC_NISTR = SDMMC_NISTR_Msk;

    /* Enable all the normal interrupt status and error status generation */
    ${SDMMC_INSTANCE_NAME}_REGS->SDMMC_NISTER = SDMMC_NISTER_Msk;
    ${SDMMC_INSTANCE_NAME}_REGS->SDMMC_EISTER = SDMMC_EISTER_Msk;

    /* Set timeout control register */
    ${SDMMC_INSTANCE_NAME}_REGS->SDMMC_TCR = SDMMC_TCR_DTCVAL(0xE);

<#if SDCARD_SDCDEN == false>
    /* If card detect line is not used, enable the card detect test signal */
    ${SDMMC_INSTANCE_NAME}_REGS->SDMMC_HC1R |= SDMMC_HC1R_CARDDTL_YES | SDMMC_HC1R_CARDDSEL_TEST | SDMMC_HC1R_DMASEL(2);
<#else>
    /* Enable ADMA2 (Check CA0R capability register first) */
    ${SDMMC_INSTANCE_NAME}_REGS->SDMMC_HC1R |= SDMMC_HC1R_DMASEL(2);
</#if>
<#if USE_FCD>

    /* Enable force card detect */
    ${SDMMC_INSTANCE_NAME}_REGS->SDMMC_MC1R = SDMMC_MC1R_FCD_Msk;
</#if>

    /* SD Bus Voltage Select = 3.3V, SD Bus Power = On */
    ${SDMMC_INSTANCE_NAME}_REGS->SDMMC_PCR = (SDMMC_PCR_SDBVSEL_3V3 | SDMMC_PCR_SDBPWR_ON);

    /* Set initial clock to 400 KHz*/
    ${SDMMC_INSTANCE_NAME}_ClockSet (SDMMC_CLOCK_FREQ_400_KHZ);

    /* Clear the high speed bit and set the data width to 1-bit mode */
    ${SDMMC_INSTANCE_NAME}_REGS->SDMMC_HC1R &= ~(SDMMC_HC1R_HSEN_Msk | SDMMC_HC1R_DW_Msk);
<#if SDCARD_EMMCEN == false && SDCARD_SDCDEN == true>

    /* Enable card inserted and card removed interrupt signals */
    ${SDMMC_INSTANCE_NAME}_REGS->SDMMC_NISIER = (SDMMC_NISIER_CINS_Msk | SDMMC_NISIER_CREM_Msk);
</#if>
}

void ${SDMMC_INSTANCE_NAME}_Initialize( void )
{
    ${SDMMC_INSTANCE_NAME}_VariablesInit();
    ${SDMMC_INSTANCE_NAME}_ModuleInit();
}

void ${SDMMC_INSTANCE_NAME}_CallbackRegister(SDMMC_CALLBACK callback, uintptr_t contextHandle)
{
    if (callback != NULL)
    {
        ${SDMMC_INSTANCE_NAME?lower_case}Obj.callback = callback;
        ${SDMMC_INSTANCE_NAME?lower_case}Obj.context = contextHandle;
    }
}