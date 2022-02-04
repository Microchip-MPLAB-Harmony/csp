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

#define ${SDHC_INSTANCE_NAME}_DMA_NUM_DESCR_LINES        (${SDHC_NUM_DESCRIPTOR_LINES}U)
#define ${SDHC_INSTANCE_NAME}_BASE_CLOCK_FREQUENCY       (${SDHC_CLK_FREQ}U)
#define ${SDHC_INSTANCE_NAME}_MAX_BLOCK_SIZE             (0x200U)
#define ${SDHC_INSTANCE_NAME}_DMA_DESC_TABLE_SIZE	     (8U * ${SDHC_NUM_DESCRIPTOR_LINES})
#define ${SDHC_INSTANCE_NAME}_DMA_DESC_TABLE_SIZE_CACHE_ALIGN	 (${SDHC_INSTANCE_NAME}_DMA_DESC_TABLE_SIZE + ((${SDHC_INSTANCE_NAME}_DMA_DESC_TABLE_SIZE % CACHE_LINE_SIZE)? (CACHE_LINE_SIZE - (${SDHC_INSTANCE_NAME}_DMA_DESC_TABLE_SIZE % CACHE_LINE_SIZE)) : 0U))

static CACHE_ALIGN SDHC_ADMA_DESCR ${SDHC_INSTANCE_NAME?lower_case}DmaDescrTable[(${SDHC_INSTANCE_NAME}_DMA_DESC_TABLE_SIZE_CACHE_ALIGN/8U)];

static SDHC_OBJECT ${SDHC_INSTANCE_NAME?lower_case}Obj;

static void ${SDHC_INSTANCE_NAME}_VariablesInit ( void )
{
    ${SDHC_INSTANCE_NAME?lower_case}Obj.errorStatus = 0U;
    ${SDHC_INSTANCE_NAME?lower_case}Obj.isCmdInProgress = false;
    ${SDHC_INSTANCE_NAME?lower_case}Obj.isDataInProgress = false;
    ${SDHC_INSTANCE_NAME?lower_case}Obj.callback = NULL;
}

static void ${SDHC_INSTANCE_NAME}_TransferModeSet ( uint32_t opcode )
{
    uint16_t transferMode = 0U;

    switch(opcode)
    {
<#if !SDCARD_EMMCEN>
        case SDHC_CMD_READ_SCR:
        case SDHC_CMD_SET_BUS_WIDTH:
<#else>
        case SDHC_CMD_SEND_EXT_CSD:
</#if>
        case SDHC_CMD_READ_SINGLE_BLOCK:
            /* Read single block of data from the device. */
            transferMode = (SDHC_TMR_DMAEN_ENABLE | SDHC_TMR_DTDSEL_Msk);
            break;

        case SDHC_CMD_READ_MULTI_BLOCK:
            /* Read multiple blocks of data from the device. */
            transferMode = (SDHC_TMR_DMAEN_ENABLE | SDHC_TMR_DTDSEL_Msk | SDHC_TMR_MSBSEL_Msk | SDHC_TMR_BCEN_Msk);
            break;

        case SDHC_CMD_WRITE_SINGLE_BLOCK:
            /* Write single block of data to the device. */
            transferMode = SDHC_TMR_DMAEN_ENABLE;
            break;

        case SDHC_CMD_WRITE_MULTI_BLOCK:
            /* Write multiple blocks of data to the device. */
            transferMode = (SDHC_TMR_DMAEN_ENABLE | SDHC_TMR_MSBSEL_Msk | SDHC_TMR_BCEN_Msk);
            break;

        default:
		   /* Do Nothing here */
            break;
    }

    ${SDHC_INSTANCE_NAME}_REGS->SDHC_TMR = transferMode;
}

void ${SDHC_INSTANCE_NAME}_InterruptHandler(void)
{
    uint16_t nistr = 0U;
    uint16_t eistr = 0U;
    SDHC_XFER_STATUS xferStatus = (SDHC_XFER_STATUS) 0;

    nistr = ${SDHC_INSTANCE_NAME}_REGS->SDHC_NISTR;
    eistr = ${SDHC_INSTANCE_NAME}_REGS->SDHC_EISTR;
    /* Save the error in a global variable for later use */
    ${SDHC_INSTANCE_NAME?lower_case}Obj.errorStatus |= eistr;
    <#if SDCARD_EMMCEN == false && SDCARD_SDCDEN == true>

    if ((nistr & SDHC_NISTR_CINS_Msk) != 0U)
    {
        xferStatus |= SDHC_XFER_STATUS_CARD_INSERTED;
    }
    if ((nistr & SDHC_NISTR_CREM_Msk) != 0U)
    {
        xferStatus |= SDHC_XFER_STATUS_CARD_REMOVED;
    }
    </#if>

    if (${SDHC_INSTANCE_NAME?lower_case}Obj.isCmdInProgress == true)
    {
        if ((nistr & (SDHC_NISTR_CMDC_Msk | SDHC_NISTR_TRFC_Msk | SDHC_NISTR_ERRINT_Msk)) != 0U)
        {
            if ((nistr & SDHC_NISTR_ERRINT_Msk) != 0U)
            {
                if (((eistr & (SDHC_EISTR_CMDTEO_Msk | \
                                      SDHC_EISTR_CMDCRC_Msk | \
                                      SDHC_EISTR_CMDEND_Msk | \
                                      SDHC_EISTR_CMDIDX_Msk))) != 0U)
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
        if ((nistr & (SDHC_NISTR_TRFC_Msk | SDHC_NISTR_DMAINT_Msk | SDHC_NISTR_ERRINT_Msk)) != 0U)
        {
            if ((nistr & SDHC_NISTR_ERRINT_Msk) != 0U)
            {
                if ((eistr & (SDHC_EISTR_DATTEO_Msk | \
                            SDHC_EISTR_DATCRC_Msk | \
                            SDHC_EISTR_DATEND_Msk)) != 0U)
                {
                    ${SDHC_INSTANCE_NAME}_ErrorReset (SDHC_RESET_DAT);
                }
            }
            if ((nistr & SDHC_NISTR_TRFC_Msk) != 0U)
            {
                /* Clear the data timeout error as transfer complete has higher priority */
                ${SDHC_INSTANCE_NAME?lower_case}Obj.errorStatus &= (uint16_t)(~SDHC_EISTR_DATTEO_Msk);
            }
            ${SDHC_INSTANCE_NAME?lower_case}Obj.isDataInProgress = false;
            xferStatus |= SDHC_XFER_STATUS_DATA_COMPLETED;
        }
    }

    /* Clear normal interrupt and error status bits that have been processed */
    ${SDHC_INSTANCE_NAME}_REGS->SDHC_NISTR = nistr;
    ${SDHC_INSTANCE_NAME}_REGS->SDHC_EISTR = eistr;

    if ((${SDHC_INSTANCE_NAME?lower_case}Obj.callback != NULL) && ((uint32_t)xferStatus > 0U))
    {
        ${SDHC_INSTANCE_NAME?lower_case}Obj.callback(xferStatus, ${SDHC_INSTANCE_NAME?lower_case}Obj.context);
    }
}

void ${SDHC_INSTANCE_NAME}_ErrorReset ( SDHC_RESET_TYPE resetType )
{
    ${SDHC_INSTANCE_NAME}_REGS->SDHC_SRR = (uint8_t)resetType;

    /* Wait until host resets the error status */
    while ((${SDHC_INSTANCE_NAME}_REGS->SDHC_SRR & (uint8_t)resetType) != 0U)
	{

	}
}

uint16_t ${SDHC_INSTANCE_NAME}_GetError(void)
{
    return ${SDHC_INSTANCE_NAME?lower_case}Obj.errorStatus;
}

uint16_t ${SDHC_INSTANCE_NAME}_CommandErrorGet(void)
{
    return (${SDHC_INSTANCE_NAME?lower_case}Obj.errorStatus & (SDHC_EISTR_CMDTEO_Msk | SDHC_EISTR_CMDCRC_Msk | \
                SDHC_EISTR_CMDEND_Msk | SDHC_EISTR_CMDIDX_Msk));
}

uint16_t ${SDHC_INSTANCE_NAME}_DataErrorGet(void)
{
    return (${SDHC_INSTANCE_NAME?lower_case}Obj.errorStatus & (SDHC_EISTR_ADMA_Msk | SDHC_EISTR_DATTEO_Msk | \
            SDHC_EISTR_DATCRC_Msk | SDHC_EISTR_DATEND_Msk));
}

void ${SDHC_INSTANCE_NAME}_BusWidthSet ( SDHC_BUS_WIDTH busWidth )
{
    if (busWidth == SDHC_BUS_WIDTH_4_BIT)
    {
       ${SDHC_INSTANCE_NAME}_REGS->SDHC_HC1R |= SDHC_HC1R_DW_4BIT;
    }
    else
    {
        ${SDHC_INSTANCE_NAME}_REGS->SDHC_HC1R &= (uint8_t)(~SDHC_HC1R_DW_4BIT);
    }
}

void ${SDHC_INSTANCE_NAME}_SpeedModeSet ( SDHC_SPEED_MODE speedMode )
{
    if (speedMode == SDHC_SPEED_MODE_HIGH)
    {
       ${SDHC_INSTANCE_NAME}_REGS->SDHC_HC1R |= SDHC_HC1R_HSEN_Msk;
    }
    else
    {
       ${SDHC_INSTANCE_NAME}_REGS->SDHC_HC1R &= (uint8_t)(~SDHC_HC1R_HSEN_Msk);
    }
}

bool ${SDHC_INSTANCE_NAME}_IsCmdLineBusy ( void )
{
    return(((${SDHC_INSTANCE_NAME}_REGS->SDHC_PSR & SDHC_PSR_CMDINHC_Msk) == SDHC_PSR_CMDINHC_Msk)? true : false);
}

bool ${SDHC_INSTANCE_NAME}_IsDatLineBusy ( void )
{
    return (((${SDHC_INSTANCE_NAME}_REGS->SDHC_PSR & SDHC_PSR_CMDINHD_Msk) == SDHC_PSR_CMDINHD_Msk)? true : false);
}
<#if SDCARD_EMMCEN == false && SDCARD_SDWPEN == true>

bool ${SDHC_INSTANCE_NAME}_IsWriteProtected ( void )
{
    return (${SDHC_INSTANCE_NAME}_REGS->SDHC_PSR & SDHC_PSR_WRPPL_Msk) ? false : true;
}
</#if>
<#if SDCARD_EMMCEN == false && SDCARD_SDCDEN == true>

bool ${SDHC_INSTANCE_NAME}_IsCardAttached ( void )
{
    return ((${SDHC_INSTANCE_NAME}_REGS->SDHC_PSR & SDHC_PSR_CARDINS_Msk) == SDHC_PSR_CARDINS_Msk)? true : false;
}
</#if>

void ${SDHC_INSTANCE_NAME}_BlockSizeSet ( uint16_t blockSize )
{
    if(blockSize == 0U)
    {
        blockSize = 1U;
    }
    else if(blockSize > ${SDHC_INSTANCE_NAME}_MAX_BLOCK_SIZE)
    {
        blockSize = ${SDHC_INSTANCE_NAME}_MAX_BLOCK_SIZE;
    }
    else
    {
      /* Do not modify the block size */
    }
    ${SDHC_INSTANCE_NAME}_REGS->SDHC_BSR = (SDHC_BSR_BOUNDARY_4K | SDHC_BSR_BLOCKSIZE(blockSize));
}

void ${SDHC_INSTANCE_NAME}_BlockCountSet ( uint16_t numBlocks )
{
    ${SDHC_INSTANCE_NAME}_REGS->SDHC_BCR = numBlocks;
}

void ${SDHC_INSTANCE_NAME}_ClockEnable ( void )
{
    /* Start the internal clock  */
    ${SDHC_INSTANCE_NAME}_REGS->SDHC_CCR |= SDHC_CCR_INTCLKEN_Msk;

    while ((${SDHC_INSTANCE_NAME}_REGS->SDHC_CCR & SDHC_CCR_INTCLKS_Msk) == 0U)
	{
        /* Wait for the internal clock to stabilize */
	}

    /* Enable the SD Clock */
    ${SDHC_INSTANCE_NAME}_REGS->SDHC_CCR |= SDHC_CCR_SDCLKEN_Msk;
}

void ${SDHC_INSTANCE_NAME}_ClockDisable ( void )
{
    ${SDHC_INSTANCE_NAME}_REGS->SDHC_CCR &= (uint16_t)(~(SDHC_CCR_INTCLKEN_Msk | SDHC_CCR_SDCLKEN_Msk));
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
        ${SDHC_INSTANCE_NAME?lower_case}DmaDescrTable[0].address = (uint32_t)(buffer);
        ${SDHC_INSTANCE_NAME?lower_case}DmaDescrTable[0].length = (uint16_t)numBytes;
        ${SDHC_INSTANCE_NAME?lower_case}DmaDescrTable[0].attribute = \
            (SDHC_DESC_TABLE_ATTR_XFER_DATA | SDHC_DESC_TABLE_ATTR_VALID | SDHC_DESC_TABLE_ATTR_INTR);


         /* The last descriptor line must indicate the end of the descriptor list */
        ${SDHC_INSTANCE_NAME?lower_case}DmaDescrTable[0].attribute |= (uint16_t)(SDHC_DESC_TABLE_ATTR_END);

        /* Clean the cache associated with the modified descriptors */
        DCACHE_CLEAN_BY_ADDR((uint32_t*)(${SDHC_INSTANCE_NAME?lower_case}DmaDescrTable), (sizeof(SDHC_ADMA_DESCR)));

        /* Set the starting address of the descriptor table */
        ${SDHC_INSTANCE_NAME}_REGS->SDHC_ASAR[0] = (uint32_t)(&${SDHC_INSTANCE_NAME?lower_case}DmaDescrTable[0]);
    }
<#else>
    uint32_t i = 0U;
    uint32_t pendingBytes = numBytes;
    uint32_t nBytes = 0U;

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
            ${SDHC_INSTANCE_NAME?lower_case}DmaDescrTable[i].address = (uint32_t)(buffer);
            ${SDHC_INSTANCE_NAME?lower_case}DmaDescrTable[i].length = (uint16_t)nBytes;
            ${SDHC_INSTANCE_NAME?lower_case}DmaDescrTable[i].attribute = \
                (SDHC_DESC_TABLE_ATTR_XFER_DATA | SDHC_DESC_TABLE_ATTR_VALID | SDHC_DESC_TABLE_ATTR_INTR);

            pendingBytes = pendingBytes - nBytes;
            i++;
        }while((i < ${SDHC_INSTANCE_NAME}_DMA_NUM_DESCR_LINES) && (pendingBytes > 0U));

        /* The last descriptor line must indicate the end of the descriptor list */
        ${SDHC_INSTANCE_NAME?lower_case}DmaDescrTable[i-1U].attribute |= (uint16_t)(SDHC_DESC_TABLE_ATTR_END);

        /* Clean the cache associated with the modified descriptors */
        DCACHE_CLEAN_BY_ADDR((uint32_t*)(${SDHC_INSTANCE_NAME?lower_case}DmaDescrTable), (i * sizeof(SDHC_ADMA_DESCR)));

        /* Set the starting address of the descriptor table */
        ${SDHC_INSTANCE_NAME}_REGS->SDHC_ASAR[0] = (uint32_t)(&${SDHC_INSTANCE_NAME?lower_case}DmaDescrTable[0]);
    }
</#if>
}

bool ${SDHC_INSTANCE_NAME}_ClockSet ( uint32_t speed)
{
    uint32_t baseclk_frq = 0U;
    uint16_t divider = 0U;
    uint32_t clkmul = 0U;
    bool retval = false;

    /* Disable clock before changing it */
    if ((${SDHC_INSTANCE_NAME}_REGS->SDHC_CCR & SDHC_CCR_SDCLKEN_Msk) != 0U)
    {
        while ((${SDHC_INSTANCE_NAME}_REGS->SDHC_PSR & (SDHC_PSR_CMDINHC_Msk | SDHC_PSR_CMDINHD_Msk)) != 0U)
		{
            /* Wait for clock status to clear */
		}
        ${SDHC_INSTANCE_NAME}_REGS->SDHC_CCR &= (uint16_t)(~SDHC_CCR_SDCLKEN_Msk);
    }

    /* Get the base clock frequency */
    baseclk_frq = (${SDHC_INSTANCE_NAME}_REGS->SDHC_CA0R & (SDHC_CA0R_BASECLKF_Msk)) >> SDHC_CA0R_BASECLKF_Pos;
    if (baseclk_frq == 0U)
    {
        baseclk_frq = (uint32_t)(${SDHC_INSTANCE_NAME}_BASE_CLOCK_FREQUENCY/2U);
    }
    else
    {
        baseclk_frq *= 1000000U;
    }

    clkmul = (${SDHC_INSTANCE_NAME}_REGS->SDHC_CA1R & (SDHC_CA1R_CLKMULT_Msk)) >> SDHC_CA1R_CLKMULT_Pos;
    if (clkmul > 0U)
    {
        /* F_SDCLK = F_MULTCLK/(DIV+1), where F_MULTCLK = F_BASECLK x (CLKMULT+1)
            F_SDCLK = (F_BASECLK x (CLKMULT + 1))/(DIV + 1)
            For a given F_SDCLK, DIV = [(F_BASECLK x (CLKMULT + 1))/F_SDCLK] - 1
        */
        divider = (uint16_t)((baseclk_frq * (clkmul + 1U)) / speed);
        if (divider > 0U)
        {
            divider = divider - 1U;
        }
        ${SDHC_INSTANCE_NAME}_REGS->SDHC_CCR |= SDHC_CCR_CLKGSEL_Msk;

        if (speed > SDHC_CLOCK_FREQ_DS_25_MHZ)
        {
            /* Enable the high speed mode */
            ${SDHC_INSTANCE_NAME}_REGS->SDHC_HC1R |= SDHC_HC1R_HSEN_Msk;
        }
        else
        {
            /* Clear the high speed mode */
            ${SDHC_INSTANCE_NAME}_REGS->SDHC_HC1R &= (uint8_t)(~SDHC_HC1R_HSEN_Msk);
        }

        if (((${SDHC_INSTANCE_NAME}_REGS->SDHC_HC1R & SDHC_HC1R_HSEN_Msk) != 0U) && (divider == 0U))
        {
            /* IP limitation, if high speed mode is active divider must be non zero */
            divider = 1;
        }

        /* Set the divider */
        ${SDHC_INSTANCE_NAME}_REGS->SDHC_CCR &= (uint16_t)(~(SDHC_CCR_SDCLKFSEL_Msk | SDHC_CCR_USDCLKFSEL_Msk));
        ${SDHC_INSTANCE_NAME}_REGS->SDHC_CCR |= SDHC_CCR_SDCLKFSEL((divider & 0xffU)) | SDHC_CCR_USDCLKFSEL((divider >> 8U));

        /* Enable internal clock */
        ${SDHC_INSTANCE_NAME}_REGS->SDHC_CCR |= SDHC_CCR_INTCLKEN_Msk;

        while((${SDHC_INSTANCE_NAME}_REGS->SDHC_CCR & SDHC_CCR_INTCLKS_Msk) == 0U)
        {
            /* Wait for the internal clock to stabilize */
        }

        /* Enable the SDCLK */
        ${SDHC_INSTANCE_NAME}_REGS->SDHC_CCR |= SDHC_CCR_SDCLKEN_Msk;

        retval = true;
    }
    return retval;
}

void ${SDHC_INSTANCE_NAME}_ResponseRead (
    SDHC_READ_RESPONSE_REG respReg,
    uint32_t* response
)
{
    switch (respReg)
    {
        case SDHC_READ_RESP_REG_1:
            *response = ${SDHC_INSTANCE_NAME}_REGS->SDHC_RR[1];
            break;

        case SDHC_READ_RESP_REG_2:
            *response = ${SDHC_INSTANCE_NAME}_REGS->SDHC_RR[2];
            break;

        case SDHC_READ_RESP_REG_3:
            *response = ${SDHC_INSTANCE_NAME}_REGS->SDHC_RR[3];
            break;

        case SDHC_READ_RESP_REG_ALL:
            response[0] = ${SDHC_INSTANCE_NAME}_REGS->SDHC_RR[0];
            response[1] = ${SDHC_INSTANCE_NAME}_REGS->SDHC_RR[1];
            response[2] = ${SDHC_INSTANCE_NAME}_REGS->SDHC_RR[2];
            response[3] = ${SDHC_INSTANCE_NAME}_REGS->SDHC_RR[3];
            break;

		case SDHC_READ_RESP_REG_0:
        default:
            *response = ${SDHC_INSTANCE_NAME}_REGS->SDHC_RR[0];
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
    uint16_t cmd = 0U;
    uint16_t normalIntSigEnable = 0U;
    uint16_t flags = 0U;

    /* Clear the flags */
    ${SDHC_INSTANCE_NAME?lower_case}Obj.isCmdInProgress = false;
    ${SDHC_INSTANCE_NAME?lower_case}Obj.isDataInProgress = false;
    ${SDHC_INSTANCE_NAME?lower_case}Obj.errorStatus = 0U;

<#if SDCARD_EMMCEN == false && SDCARD_SDCDEN == true>
    /* Keep the card insertion and removal interrupts enabled */
    normalIntSigEnable = (SDHC_NISIER_CINS_Msk | SDHC_NISIER_CREM_Msk);
</#if>

    switch (respType)
    {
        case SDHC_CMD_RESP_R1:
        case SDHC_CMD_RESP_R5:
        case SDHC_CMD_RESP_R6:
        case SDHC_CMD_RESP_R7:
            flags = (SDHC_CR_RESPTYP_48_BIT_Val | SDHC_CR_CMDCCEN_Msk | SDHC_CR_CMDICEN_Msk);
            break;

        case SDHC_CMD_RESP_R3:
        case SDHC_CMD_RESP_R4:
            flags = SDHC_CR_RESPTYP_48_BIT_Val;
            break;

        case SDHC_CMD_RESP_R1B:
            flags = (SDHC_CR_RESPTYP_48_BIT_BUSY_Val | SDHC_CR_CMDCCEN_Msk | SDHC_CR_CMDICEN_Msk);

            /* Commands with busy response will wait for transfer complete bit */
            normalIntSigEnable |= SDHC_NISIER_TRFC_Msk;
            break;

        case SDHC_CMD_RESP_R2:
            flags = (SDHC_CR_RESPTYP_136_BIT_Val | SDHC_CR_CMDCCEN_Msk);
            break;

        default:
            flags = SDHC_CR_RESPTYP_NONE_Val;
            break;
    }

    /* Enable command complete interrupt, for commands that do not have busy response type */
    if (respType != (uint8_t)SDHC_CMD_RESP_R1B)
    {
        normalIntSigEnable |= SDHC_NISIER_CMDC_Msk;
    }

    if (transferFlags.isDataPresent == true)
    {
        ${SDHC_INSTANCE_NAME?lower_case}Obj.isDataInProgress = true;
        ${SDHC_INSTANCE_NAME}_TransferModeSet(opCode);
        /* Enable data transfer complete and DMA interrupt */
        normalIntSigEnable |= (SDHC_NISIER_TRFC_Msk | SDHC_NISIER_DMAINT_Msk);
    }
    else
    {
        ${SDHC_INSTANCE_NAME}_REGS->SDHC_TMR = 0U;
    }

    /* Enable the needed normal interrupt signals */
    ${SDHC_INSTANCE_NAME}_REGS->SDHC_NISIER = normalIntSigEnable;

    /* Enable all the error interrupt signals */
    ${SDHC_INSTANCE_NAME}_REGS->SDHC_EISIER = SDHC_EISIER_Msk;

    ${SDHC_INSTANCE_NAME}_REGS->SDHC_ARG1R = argument;

    ${SDHC_INSTANCE_NAME?lower_case}Obj.isCmdInProgress = true;

    cmd = (SDHC_CR_CMDIDX((uint16_t)opCode) | (transferFlags.isDataPresent ? (1U << SDHC_CR_DPSEL_Pos) : 0U) | (uint16_t)flags);
    ${SDHC_INSTANCE_NAME}_REGS->SDHC_CR = cmd;
}

<#compress>
<#-- Enable FCD if the mode of operation is EMMC or if CD capability exists but is not enabled  -->
<#assign USE_FCD = SDCARD_EMMCEN || (SDCARD_SDCD_SUPPORT && !SDCARD_SDCDEN)>
</#compress>
void ${SDHC_INSTANCE_NAME}_ModuleInit( void )
{
    /* Reset module*/
    ${SDHC_INSTANCE_NAME}_REGS->SDHC_SRR |= SDHC_SRR_SWRSTALL_Msk;
    while((${SDHC_INSTANCE_NAME}_REGS->SDHC_SRR & SDHC_SRR_SWRSTALL_Msk) == SDHC_SRR_SWRSTALL_Msk)
	{
        /* Wait for reset to complete */
	}

    /* Clear the normal and error interrupt status flags */
    ${SDHC_INSTANCE_NAME}_REGS->SDHC_EISTR = SDHC_EISTR_Msk;
    ${SDHC_INSTANCE_NAME}_REGS->SDHC_NISTR = SDHC_NISTR_Msk;

    /* Enable all the normal interrupt status and error status generation */
    ${SDHC_INSTANCE_NAME}_REGS->SDHC_NISTER = SDHC_NISTER_Msk;
    ${SDHC_INSTANCE_NAME}_REGS->SDHC_EISTER = SDHC_EISTER_Msk;

    /* Set timeout control register */
    ${SDHC_INSTANCE_NAME}_REGS->SDHC_TCR = SDHC_TCR_DTCVAL(0xEU);

<#if SDCARD_SDCDEN == false>
    /* If card detect line is not used, enable the card detect test signal */
    ${SDHC_INSTANCE_NAME}_REGS->SDHC_HC1R |= SDHC_HC1R_CARDDTL_YES | SDHC_HC1R_CARDDSEL_TEST | SDHC_HC1R_DMASEL(2U);
<#else>
    /* Enable ADMA2 (Check CA0R capability register first) */
    ${SDHC_INSTANCE_NAME}_REGS->SDHC_HC1R |= SDHC_HC1R_DMASEL(2U);
</#if>
<#if USE_FCD>

    /* Enable force card detect */
    ${SDHC_INSTANCE_NAME}_REGS->SDHC_MC1R = SDHC_MC1R_FCD_Msk;
</#if>

    /* SD Bus Voltage Select = 3.3V, SD Bus Power = On */
    ${SDHC_INSTANCE_NAME}_REGS->SDHC_PCR = (SDHC_PCR_SDBVSEL_3V3 | SDHC_PCR_SDBPWR_ON);

    /* Set initial clock to 400 KHz*/
    (void)${SDHC_INSTANCE_NAME}_ClockSet (SDHC_CLOCK_FREQ_400_KHZ);

    /* Clear the high speed bit and set the data width to 1-bit mode */
    ${SDHC_INSTANCE_NAME}_REGS->SDHC_HC1R &= (uint8_t)(~(SDHC_HC1R_HSEN_Msk | SDHC_HC1R_DW_Msk));
<#if SDCARD_EMMCEN == false && SDCARD_SDCDEN == true>

    /* Enable card inserted and card removed interrupt signals */
    ${SDHC_INSTANCE_NAME}_REGS->SDHC_NISIER = (SDHC_NISIER_CINS_Msk | SDHC_NISIER_CREM_Msk);
</#if>
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