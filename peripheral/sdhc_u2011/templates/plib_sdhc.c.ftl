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


// *****************************************************************************
// *****************************************************************************
// Section: Include Files
// *****************************************************************************
// *****************************************************************************

#include "plib_sdhc_common.h"

#define ${SDHC_INSTANCE_NAME}_DMA_NUM_DESCR_LINES        ${SDHC_NUM_DESCRIPTOR_LINES}
#define ${SDHC_INSTANCE_NAME}_BASE_CLOCK_FREQUENCY       ${SDHC_CLK_FREQ}

static __attribute__((__aligned__(32))) SDHC_ADMA_DESCR ${SDHC_INSTANCE_NAME?lower_case}DmaDescrTable[${SDHC_INSTANCE_NAME}_DMA_NUM_DESCR_LINES];

static SDHC_OBJECT ${SDHC_INSTANCE_NAME?lower_case}Obj;

static void ${SDHC_INSTANCE_NAME}_VariablesInit ( void )
{
    ${SDHC_INSTANCE_NAME?lower_case}Obj.errorStatus = 0;
    ${SDHC_INSTANCE_NAME?lower_case}Obj.isCmdInProgress = false;
    ${SDHC_INSTANCE_NAME?lower_case}Obj.isDataInProgress = false;
    ${SDHC_INSTANCE_NAME?lower_case}Obj.callback = NULL;
}

static void ${SDHC_INSTANCE_NAME}_TransferModeSet ( uint32_t opcode )
{
    uint16_t transferMode = 0;

    switch(opcode)
    {
        case 51:
        case 6:
        case 17:
            /* Read single block of data from the device. */
            transferMode = (SDHC_TMR_DMAEN_ENABLE | SDHC_TMR_DTDSEL_Msk);
            break;

        case 18:
            /* Read multiple blocks of data from the device. */
            transferMode = (SDHC_TMR_DMAEN_ENABLE | SDHC_TMR_DTDSEL_Msk | SDHC_TMR_MSBSEL_Msk | SDHC_TMR_BCEN_Msk);
            break;

        case 24:
            /* Write single block of data to the device. */
            transferMode = SDHC_TMR_DMAEN_ENABLE;
            break;

        case 25:
            /* Write multiple blocks of data to the device. */
            transferMode = (SDHC_TMR_DMAEN_ENABLE | SDHC_TMR_MSBSEL_Msk | SDHC_TMR_BCEN_Msk);
            break;

        default:
            break;
    }

    ${SDHC_INSTANCE_NAME}_REGS->SDHC_TMR = transferMode;
}

void ${SDHC_INSTANCE_NAME}_InterruptHandler(void)
{
    uint16_t nistr = 0;
    uint16_t eistr = 0;
    SDHC_XFER_STATUS xferStatus = 0;

    nistr = ${SDHC_INSTANCE_NAME}_REGS->SDHC_NISTR;
    eistr = ${SDHC_INSTANCE_NAME}_REGS->SDHC_EISTR;
    /* Save the error in a global variable for later use */
    ${SDHC_INSTANCE_NAME?lower_case}Obj.errorStatus |= eistr;

    if (nistr & SDHC_NISTR_CINS_Msk)
    {
        xferStatus |= SDHC_XFER_STATUS_CARD_INSERTED;
    }
    if (nistr & SDHC_NISTR_CREM_Msk)
    {
        xferStatus |= SDHC_XFER_STATUS_CARD_REMOVED;
    }

    if (${SDHC_INSTANCE_NAME?lower_case}Obj.isCmdInProgress == true)
    {
        if (nistr & (SDHC_NISTR_CMDC_Msk | SDHC_NISTR_TRFC_Msk | SDHC_NISTR_ERRINT_Msk))
        {
            if (nistr & SDHC_NISTR_ERRINT_Msk)
            {
                if (eistr & (SDHC_EISTR_CMDTEO_Msk | \
                                      SDHC_EISTR_CMDCRC_Msk | \
                                      SDHC_EISTR_CMDEND_Msk | \
                                      SDHC_EISTR_CMDIDX_Msk))
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
        if (nistr & (SDHC_NISTR_TRFC_Msk | SDHC_NISTR_DMAINT_Msk | SDHC_NISTR_ERRINT_Msk))
        {
            if (nistr & SDHC_NISTR_ERRINT_Msk)
            {
                if (eistr & (SDHC_EISTR_DATTEO_Msk | \
                            SDHC_EISTR_DATCRC_Msk | \
                            SDHC_EISTR_DATEND_Msk))
                {
                    ${SDHC_INSTANCE_NAME}_ErrorReset (SDHC_RESET_DAT);
                }
            }
            if (nistr & SDHC_NISTR_TRFC_Msk)
            {
                /* Clear the data timeout error as transfer complete has higher priority */
                ${SDHC_INSTANCE_NAME?lower_case}Obj.errorStatus &= ~SDHC_EISTR_DATTEO_Msk;
            }
            ${SDHC_INSTANCE_NAME?lower_case}Obj.isDataInProgress = false;
            xferStatus |= SDHC_XFER_STATUS_DATA_COMPLETED;
        }
    }

    /* Clear normal interrupt and error status bits that have been processed */
    ${SDHC_INSTANCE_NAME}_REGS->SDHC_NISTR = nistr;
    ${SDHC_INSTANCE_NAME}_REGS->SDHC_EISTR = eistr;

    if ((${SDHC_INSTANCE_NAME?lower_case}Obj.callback != NULL) && (xferStatus > 0))
    {
        ${SDHC_INSTANCE_NAME?lower_case}Obj.callback(xferStatus, ${SDHC_INSTANCE_NAME?lower_case}Obj.context);
    }
}

void ${SDHC_INSTANCE_NAME}_ErrorReset ( SDHC_RESET_TYPE resetType )
{
    ${SDHC_INSTANCE_NAME}_REGS->SDHC_SRR = resetType;

    /* Wait until host resets the error status */
    while (${SDHC_INSTANCE_NAME}_REGS->SDHC_SRR & resetType);
}

uint16_t ${SDHC_INSTANCE_NAME}_GetError(void)
{
    return ${SDHC_INSTANCE_NAME?lower_case}Obj.errorStatus;
}

uint16_t ${SDHC_INSTANCE_NAME}_CommandErrorGet(void)
{
    return (${SDHC_INSTANCE_NAME?lower_case}Obj.errorStatus & (SDHC_EISTR_CMDTEO_Msk | SDHC_EISTR_CMDCRC_Msk | \
                SDHC_EISTR_CMDEND_Msk));
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
        ${SDHC_INSTANCE_NAME}_REGS->SDHC_HC1R &= ~SDHC_HC1R_DW_4BIT;
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
       ${SDHC_INSTANCE_NAME}_REGS->SDHC_HC1R &= ~SDHC_HC1R_HSEN_Msk;
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

bool ${SDHC_INSTANCE_NAME}_IsWriteProtected ( void )
{
    return (${SDHC_INSTANCE_NAME}_REGS->SDHC_PSR & SDHC_PSR_WRPPL_Msk) ? false : true;
}

bool ${SDHC_INSTANCE_NAME}_IsCardAttached ( void )
{
    return ((${SDHC_INSTANCE_NAME}_REGS->SDHC_PSR & SDHC_PSR_CARDINS_Msk) == SDHC_PSR_CARDINS_Msk)? true : false;
}

void ${SDHC_INSTANCE_NAME}_BlockSizeSet ( uint16_t blockSize )
{
    ${SDHC_INSTANCE_NAME}_REGS->SDHC_BSR = blockSize;
}

void ${SDHC_INSTANCE_NAME}_BlockCountSet ( uint16_t numBlocks )
{
    ${SDHC_INSTANCE_NAME}_REGS->SDHC_BCR = numBlocks;
}

void ${SDHC_INSTANCE_NAME}_ClockEnable ( void )
{
    ${SDHC_INSTANCE_NAME}_REGS->SDHC_CCR |= (SDHC_CCR_INTCLKEN_Msk | SDHC_CCR_SDCLKEN_Msk);
}

void ${SDHC_INSTANCE_NAME}_ClockDisable ( void )
{
    ${SDHC_INSTANCE_NAME}_REGS->SDHC_CCR &= ~(SDHC_CCR_INTCLKEN_Msk | SDHC_CCR_SDCLKEN_Msk);
}

void ${SDHC_INSTANCE_NAME}_DmaSetup (
    uint8_t* buffer,
    uint32_t numBytes,
    SDHC_DATA_TRANSFER_DIR direction
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

    if (pendingBytes > (65536 * ${SDHC_INSTANCE_NAME}_DMA_NUM_DESCR_LINES))
    {
        /* Too many blocks requested in one go */
        return;
    }

    for (i = 0; (i < ${SDHC_INSTANCE_NAME}_DMA_NUM_DESCR_LINES) && (pendingBytes > 0); i++)
    {
        if (pendingBytes > 65536)
        {
            nBytes = 65536;
        }
        else
        {
            nBytes = pendingBytes;
        }
        ${SDHC_INSTANCE_NAME?lower_case}DmaDescrTable[i].address = (uint32_t)(buffer);
        ${SDHC_INSTANCE_NAME?lower_case}DmaDescrTable[i].length = nBytes;
        ${SDHC_INSTANCE_NAME?lower_case}DmaDescrTable[i].attribute = \
            (SDHC_DESC_TABLE_ATTR_XFER_DATA | SDHC_DESC_TABLE_ATTR_VALID | SDHC_DESC_TABLE_ATTR_INTR);

        pendingBytes = pendingBytes - nBytes;
    }

    /* The last descriptor line must indicate the end of the descriptor list */
    ${SDHC_INSTANCE_NAME?lower_case}DmaDescrTable[i-1].attribute |= (SDHC_DESC_TABLE_ATTR_END);

    /* Set the starting address of the descriptor table */
    ${SDHC_INSTANCE_NAME}_REGS->SDHC_ASAR[0] = (uint32_t)(&${SDHC_INSTANCE_NAME?lower_case}DmaDescrTable[0]);
}

bool ${SDHC_INSTANCE_NAME}_ClockSet ( uint32_t speed)
{
    uint32_t baseclk_frq = 0;
    uint16_t divider = 0;
    uint32_t clkmul = 0;
    SDHC_CLK_MODE clkMode = SDHC_PROGRAMMABLE_CLK_MODE;

    /* Disable clock before changing it */
    if (${SDHC_INSTANCE_NAME}_REGS->SDHC_CCR & SDHC_CCR_SDCLKEN_Msk)
    {
        while (${SDHC_INSTANCE_NAME}_REGS->SDHC_PSR & (SDHC_PSR_CMDINHC_Msk | SDHC_PSR_CMDINHD_Msk));
        ${SDHC_INSTANCE_NAME}_REGS->SDHC_CCR &= ~SDHC_CCR_SDCLKEN_Msk;
    }

    /* Get the base clock frequency */
    baseclk_frq = (${SDHC_INSTANCE_NAME}_REGS->SDHC_CA0R & (SDHC_CA0R_BASECLKF_Msk)) >> SDHC_CA0R_BASECLKF_Pos;
    if (baseclk_frq == 0)
    {
        baseclk_frq = ${SDHC_INSTANCE_NAME}_BASE_CLOCK_FREQUENCY/2;
    }
    else
    {
        baseclk_frq *= 1000000;
    }

    if (clkMode == SDHC_DIVIDED_CLK_MODE)
    {
        /* F_SDCLK = F_BASECLK/(2 x DIV).
           For a given F_SDCLK, DIV = F_BASECLK/(2 x F_SDCLK)
        */

        divider =  baseclk_frq/(2 * speed);
        ${SDHC_INSTANCE_NAME}_REGS->SDHC_CCR &= ~SDHC_CCR_CLKGSEL_Msk;
    }
    else
    {
        clkmul = (${SDHC_INSTANCE_NAME}_REGS->SDHC_CA1R & (SDHC_CA1R_CLKMULT_Msk)) >> SDHC_CA1R_CLKMULT_Pos;
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
            ${SDHC_INSTANCE_NAME}_REGS->SDHC_CCR |= SDHC_CCR_CLKGSEL_Msk;
        }
        else
        {
            /* Programmable clock mode is not supported */
            return false;
        }
    }

    if (speed > SDHC_CLOCK_FREQ_DS_25_MHZ)
    {
        /* Enable the high speed mode */
        ${SDHC_INSTANCE_NAME}_REGS->SDHC_HC1R |= SDHC_HC1R_HSEN_Msk;
    }
    else
    {
        /* Clear the high speed mode */
        ${SDHC_INSTANCE_NAME}_REGS->SDHC_HC1R &= ~SDHC_HC1R_HSEN_Msk;
    }

    if ((${SDHC_INSTANCE_NAME}_REGS->SDHC_HC1R & SDHC_HC1R_HSEN_Msk) && (divider == 0))
    {
        /* IP limitation, if high speed mode is active divider must be non zero */
        divider = 1;
    }

    /* Set the divider */
    ${SDHC_INSTANCE_NAME}_REGS->SDHC_CCR &= ~(SDHC_CCR_SDCLKFSEL_Msk | SDHC_CCR_USDCLKFSEL_Msk);
    ${SDHC_INSTANCE_NAME}_REGS->SDHC_CCR |= SDHC_CCR_SDCLKFSEL((divider & 0xff)) | SDHC_CCR_USDCLKFSEL((divider >> 8));

    /* Enable internal clock */
    ${SDHC_INSTANCE_NAME}_REGS->SDHC_CCR |= SDHC_CCR_INTCLKEN_Msk;

    /* Wait for the internal clock to stabilize */
    while((${SDHC_INSTANCE_NAME}_REGS->SDHC_CCR & SDHC_CCR_INTCLKS_Msk) == 0);

    /* Enable the SDCLK */
    ${SDHC_INSTANCE_NAME}_REGS->SDHC_CCR |= SDHC_CCR_SDCLKEN_Msk;

    return true;
}

void ${SDHC_INSTANCE_NAME}_ResponseRead (
    SDHC_READ_RESPONSE_REG respReg,
    uint32_t* response
)
{
    switch (respReg)
    {
        case SDHC_READ_RESP_REG_0:
        default:
            *response = ${SDHC_INSTANCE_NAME}_REGS->SDHC_RR[0];
            break;

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
    }
}

void ${SDHC_INSTANCE_NAME}_CommandSend (
    uint8_t opCode,
    uint32_t argument,
    uint8_t respType,
    SDHC_DataTransferFlags transferFlags
)
{
    uint16_t cmd = 0;
    uint16_t normalIntSigEnable = 0;
    uint8_t flags = 0;

    /* Clear the flags */
    ${SDHC_INSTANCE_NAME?lower_case}Obj.isCmdInProgress = false;
    ${SDHC_INSTANCE_NAME?lower_case}Obj.isDataInProgress = false;
    ${SDHC_INSTANCE_NAME?lower_case}Obj.errorStatus = 0;

    /* Keep the card insertion and removal interrupts enabled */
    normalIntSigEnable = (SDHC_NISIER_CINS_Msk | SDHC_NISIER_CREM_Msk);

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
    if (respType != SDHC_CMD_RESP_R1B)
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
        ${SDHC_INSTANCE_NAME}_REGS->SDHC_TMR = 0;
    }

    /* Enable the needed normal interrupt signals */
    ${SDHC_INSTANCE_NAME}_REGS->SDHC_NISIER = normalIntSigEnable;

    /* Enable all the error interrupt signals */
    ${SDHC_INSTANCE_NAME}_REGS->SDHC_EISIER = SDHC_EISIER_Msk;

    ${SDHC_INSTANCE_NAME}_REGS->SDHC_ARG1R = argument;

    ${SDHC_INSTANCE_NAME?lower_case}Obj.isCmdInProgress = true;

    cmd = (SDHC_CR_CMDIDX(opCode) | (transferFlags.isDataPresent << SDHC_CR_DPSEL_Pos) | flags);
    ${SDHC_INSTANCE_NAME}_REGS->SDHC_CR = cmd;
}

void ${SDHC_INSTANCE_NAME}_ModuleInit( void )
{
    /* Reset module*/
    ${SDHC_INSTANCE_NAME}_REGS->SDHC_SRR |= SDHC_SRR_SWRSTALL_Msk;
    while((${SDHC_INSTANCE_NAME}_REGS->SDHC_SRR & SDHC_SRR_SWRSTALL_Msk) == SDHC_SRR_SWRSTALL_Msk);

    /* Clear the normal and error interrupt status flags */
    ${SDHC_INSTANCE_NAME}_REGS->SDHC_EISTR = SDHC_EISTR_Msk;
    ${SDHC_INSTANCE_NAME}_REGS->SDHC_NISTR = SDHC_NISTR_Msk;

    /* Enable all the normal interrupt status and error status generation */
    ${SDHC_INSTANCE_NAME}_REGS->SDHC_NISTER = SDHC_NISTER_Msk;
    ${SDHC_INSTANCE_NAME}_REGS->SDHC_EISTER = SDHC_EISTER_Msk;

    /* Set timeout control register */
    ${SDHC_INSTANCE_NAME}_REGS->SDHC_TCR = SDHC_TCR_DTCVAL(0xE);

<#if SDCARD_SDCDEN == false>
    /* If card detect line is not used, enable the card detect test signal */
    ${SDHC_INSTANCE_NAME}_REGS->SDHC_HC1R |= SDHC_HC1R_CARDDTL_YES | SDHC_HC1R_CARDDSEL_TEST | SDHC_HC1R_DMASEL(2);
<#else>
    /* Enable ADMA2 (Check CA0R capability register first) */
    ${SDHC_INSTANCE_NAME}_REGS->SDHC_HC1R |= SDHC_HC1R_DMASEL(2);
</#if>

    /* SD Bus Voltage Select = 3.3V, SD Bus Power = On */
    ${SDHC_INSTANCE_NAME}_REGS->SDHC_PCR = (SDHC_PCR_SDBVSEL_3V3 | SDHC_PCR_SDBPWR_ON);

    /* Set initial clock to 400 KHz*/
    ${SDHC_INSTANCE_NAME}_ClockSet (SDHC_CLOCK_FREQ_400_KHZ);

    /* Clear the high speed bit and set the data width to 1-bit mode */
    ${SDHC_INSTANCE_NAME}_REGS->SDHC_HC1R &= ~(SDHC_HC1R_HSEN_Msk | SDHC_HC1R_DW_Msk);

    /* Enable card inserted and card removed interrupt signals */
    ${SDHC_INSTANCE_NAME}_REGS->SDHC_NISIER = (SDHC_NISIER_CINS_Msk | SDHC_NISIER_CREM_Msk);
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