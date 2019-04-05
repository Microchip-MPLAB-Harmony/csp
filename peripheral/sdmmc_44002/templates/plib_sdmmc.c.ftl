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
<#compress>
<#if SDCARD_SDCDEN??>
<#assign USE_CARD_DETECT = SDCARD_SDCDEN>
<#else>
<#assign USE_CARD_DETECT = false>
</#if>
<#if SDCARD_SDWPEN??>
<#assign USE_WRITE_PROTECT = SDCARD_SDWPEN>
<#else>
<#assign USE_WRITE_PROTECT = false>
</#if>
</#compress>

#include "device.h"
#include "plib_${SDMMC_INSTANCE_NAME?lower_case}.h"

// *****************************************************************************
// *****************************************************************************
// Section: Include Files
// *****************************************************************************
// *****************************************************************************

#include "plib_sdmmc_common.h"

#define ${SDMMC_INSTANCE_NAME}_DMA_NUM_DESCR_LINES              ${SDMMC_NUM_DESCRIPTOR_LINES}
#define ${SDMMC_INSTANCE_NAME}_HCLOCK_FREQUENCY                 ${SDMMC_HCLOCK_FREQ}
#define ${SDMMC_INSTANCE_NAME}_BASECLK_FREQUENCY                ${SDMMC_BASECLK_FREQ}
#define ${SDMMC_INSTANCE_NAME}_MULTCLK_FREQUENCY                ${SDMMC_MULTCLK_FREQ}

#define ${SDMMC_INSTANCE_NAME}_MAX_SUPPORTED_SDCLK_FREQUENCY    50000000UL
#define ${SDMMC_INSTANCE_NAME}_MAX_SUPPORTED_DIVIDER            0x3FF

/* Absolute difference between two 32 bit integers */
static inline uint32_t ${SDMMC_INSTANCE_NAME}_ABS_DIFF_U32(uint32_t a, uint32_t b)
{
  return (a < b) ? (b - a) : (a - b);
}

/* Divide two 32 bit integers with dividend rounded upto the next divisor */
static inline uint32_t ${SDMMC_INSTANCE_NAME}_CEIL_INT_DIV_U32(uint32_t n, uint32_t d)
{
  return  ((n + d - 1) / d);
}

/* Minimum value among two 32 bit integers */
static inline uint32_t ${SDMMC_INSTANCE_NAME}_MIN_U32 (uint32_t a, uint32_t b)
{
  return a > b ? b : a;
}

static __attribute__((__aligned__(32))) SDMMC_ADMA_DESCR ${SDMMC_INSTANCE_NAME?lower_case}DmaDescrTable[${SDMMC_INSTANCE_NAME}_DMA_NUM_DESCR_LINES];

static SDMMC_OBJECT ${SDMMC_INSTANCE_NAME?lower_case}Obj;

static void ${SDMMC_INSTANCE_NAME}_InitVariables ( void )
{
    ${SDMMC_INSTANCE_NAME?lower_case}Obj.errorStatus = 0;
    ${SDMMC_INSTANCE_NAME?lower_case}Obj.isCmdInProgress = false;
    ${SDMMC_INSTANCE_NAME?lower_case}Obj.isDataInProgress = false;
    ${SDMMC_INSTANCE_NAME?lower_case}Obj.callback = NULL;
}

static void ${SDMMC_INSTANCE_NAME}_SetTransferMode ( uint32_t opcode )
{
    uint16_t transferMode = 0;

    switch (opcode)
    {
        case SDMMC_CMD_READ_SCR:
        case SDMMC_CMD_SET_BUS_WIDTH:
        case SDMMC_CMD_READ_SINGLE_BLOCK:
            /* Read single block of data from the device. */
            transferMode = (SDMMC_TMR_DMAEN_ENABLED | SDMMC_TMR_DTDSEL_Msk);
            break;

        case SDMMC_CMD_READ_MULTI_BLOCK:
            /* Read multiple blocks of data from the device. */
            transferMode = (SDMMC_TMR_DMAEN_ENABLED | SDMMC_TMR_DTDSEL_Msk | SDMMC_TMR_MSBSEL_Msk | SDMMC_TMR_BCEN_Msk);
            break;

        case SDMMC_CMD_WRITE_SINGLE_BLOCK:
            /* Write single block of data to the device. */
            transferMode = SDMMC_TMR_DMAEN_ENABLED;
            break;

        case SDMMC_CMD_WRITE_MULTI_BLOCK:
            /* Write multiple blocks of data to the device. */
            transferMode = (SDMMC_TMR_DMAEN_ENABLED | SDMMC_TMR_MSBSEL_Msk | SDMMC_TMR_BCEN_Msk);
            break;

        default:
            break;
    }

    ${SDMMC_INSTANCE_NAME}_REGS->SDMMC_TMR = transferMode;
}

void ${SDMMC_INSTANCE_NAME}_InterruptHandler( void )
{
    uint16_t nistr = 0;
    uint16_t eistr = 0;
    SDMMC_XFER_STATUS xferStatus = SDMMC_XFER_STATUS_IDLE;

    nistr = ${SDMMC_INSTANCE_NAME}_REGS->SDMMC_NISTR;
    eistr = ${SDMMC_INSTANCE_NAME}_REGS->SDMMC_EISTR;
    /* Save the error in a global variable for later use */
    ${SDMMC_INSTANCE_NAME?lower_case}Obj.errorStatus |= eistr;
    
    <#if USE_CARD_DETECT == true>

    if (nistr & SDMMC_NISTR_SD_SDIO_CINS_Msk)
    {
        xferStatus |= SDMMC_XFER_STATUS_CARD_INSERTED;
    }
    if (nistr & SDMMC_NISTR_SD_SDIO_CREM_Msk)
    {
        xferStatus |= SDMMC_XFER_STATUS_CARD_REMOVED;
    }
    
    </#if>

    if (${SDMMC_INSTANCE_NAME?lower_case}Obj.isCmdInProgress == true)
    {
        if (nistr & (SDMMC_NISTR_SD_SDIO_CMDC_Msk | SDMMC_NISTR_SD_SDIO_TRFC_Msk | SDMMC_NISTR_SD_SDIO_ERRINT_Msk))
        {
            if (nistr & SDMMC_NISTR_SD_SDIO_ERRINT_Msk)
            {
                if (eistr & (SDMMC_EISTR_SD_SDIO_CMDTEO_Msk | \
                                      SDMMC_EISTR_SD_SDIO_CMDCRC_Msk | \
                                      SDMMC_EISTR_SD_SDIO_CMDEND_Msk | \
                                      SDMMC_EISTR_SD_SDIO_CMDIDX_Msk))
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
        if (nistr & (SDMMC_NISTR_SD_SDIO_TRFC_Msk | SDMMC_NISTR_SD_SDIO_DMAINT_Msk | SDMMC_NISTR_SD_SDIO_ERRINT_Msk))
        {
            if (nistr & SDMMC_NISTR_SD_SDIO_ERRINT_Msk)
            {
                if (eistr & (SDMMC_EISTR_SD_SDIO_DATTEO_Msk | \
                            SDMMC_EISTR_SD_SDIO_DATCRC_Msk | \
                            SDMMC_EISTR_SD_SDIO_DATEND_Msk))
                {
                    ${SDMMC_INSTANCE_NAME}_ErrorReset (SDMMC_RESET_DAT);
                }
            }
            if (nistr & SDMMC_NISTR_SD_SDIO_TRFC_Msk)
            {
                /* Clear the data timeout error as transfer complete has higher priority */
                ${SDMMC_INSTANCE_NAME?lower_case}Obj.errorStatus &= ~SDMMC_EISTR_SD_SDIO_DATTEO_Msk;
            }
            ${SDMMC_INSTANCE_NAME?lower_case}Obj.isDataInProgress = false;
            xferStatus |= SDMMC_XFER_STATUS_DATA_COMPLETED;
        }
    }

    /* Clear normal interrupt and error status bits that have been processed */
    ${SDMMC_INSTANCE_NAME}_REGS->SDMMC_NISTR = nistr;
    ${SDMMC_INSTANCE_NAME}_REGS->SDMMC_EISTR = eistr;

    if ((${SDMMC_INSTANCE_NAME?lower_case}Obj.callback != NULL) && (xferStatus != SDMMC_XFER_STATUS_IDLE))
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

uint16_t ${SDMMC_INSTANCE_NAME}_ErrorGet( void )
{
    return ${SDMMC_INSTANCE_NAME?lower_case}Obj.errorStatus;
}

uint16_t ${SDMMC_INSTANCE_NAME}_CommandErrorGet( void )
{
    return (${SDMMC_INSTANCE_NAME?lower_case}Obj.errorStatus & (SDMMC_EISTR_SD_SDIO_CMDTEO_Msk | SDMMC_EISTR_SD_SDIO_CMDCRC_Msk | \
                SDMMC_EISTR_SD_SDIO_CMDEND_Msk));
}

uint16_t ${SDMMC_INSTANCE_NAME}_DataErrorGet( void )
{
    return (${SDMMC_INSTANCE_NAME?lower_case}Obj.errorStatus & (SDMMC_EISTR_SD_SDIO_ADMA_Msk | SDMMC_EISTR_SD_SDIO_DATTEO_Msk | \
            SDMMC_EISTR_SD_SDIO_DATCRC_Msk | SDMMC_EISTR_SD_SDIO_DATEND_Msk));
}

void ${SDMMC_INSTANCE_NAME}_BusWidthSet ( SDMMC_BUS_WIDTH busWidth )
{
    if (busWidth == SDMMC_BUS_WIDTH_4_BIT)
    {
       ${SDMMC_INSTANCE_NAME}_REGS->SDMMC_HC1R |= SDMMC_HC1R_SD_SDIO_DW_4_BIT;
    }
    else
    {
        ${SDMMC_INSTANCE_NAME}_REGS->SDMMC_HC1R &= ~SDMMC_HC1R_SD_SDIO_DW_4_BIT;
    }
}

void ${SDMMC_INSTANCE_NAME}_SpeedModeSet ( SDMMC_SPEED_MODE speedMode )
{
    if (speedMode == SDMMC_SPEED_MODE_HIGH)
    {
       ${SDMMC_INSTANCE_NAME}_REGS->SDMMC_HC1R |= SDMMC_HC1R_SD_SDIO_HSEN_Msk;
    }
    else
    {
       ${SDMMC_INSTANCE_NAME}_REGS->SDMMC_HC1R &= ~SDMMC_HC1R_SD_SDIO_HSEN_Msk;
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

bool ${SDMMC_INSTANCE_NAME}_IsWriteProtected ( void )
{
<#if USE_WRITE_PROTECT == true>
    return (${SDMMC_INSTANCE_NAME}_REGS->SDMMC_PSR & SDMMC_PSR_WRPPL_Msk) ? false : true;
<#else>
	return false;    
</#if>
}

bool ${SDMMC_INSTANCE_NAME}_IsCardAttached ( void )
{
<#if USE_CARD_DETECT == true>
    return ((${SDMMC_INSTANCE_NAME}_REGS->SDMMC_PSR & SDMMC_PSR_CARDINS_Msk) == SDMMC_PSR_CARDINS_Msk)? true : false;
<#else>
	return true;
</#if>	    
}


void ${SDMMC_INSTANCE_NAME}_BlockSizeSet ( uint16_t blockSize )
{
    ${SDMMC_INSTANCE_NAME}_REGS->SDMMC_BSR = blockSize;
}

void ${SDMMC_INSTANCE_NAME}_BlockCountSet ( uint16_t numBlocks )
{
    ${SDMMC_INSTANCE_NAME}_REGS->SDMMC_BCR = numBlocks;
}

void ${SDMMC_INSTANCE_NAME}_ClockEnable ( void )
{
    ${SDMMC_INSTANCE_NAME}_REGS->SDMMC_CCR |= (SDMMC_CCR_INTCLKEN_Msk | SDMMC_CCR_SDCLKEN_Msk);
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

    /* Set the starting address of the descriptor table */
    ${SDMMC_INSTANCE_NAME}_REGS->SDMMC_ASAR0 = (uint32_t)(&${SDMMC_INSTANCE_NAME?lower_case}DmaDescrTable[0]);
}


bool ${SDMMC_INSTANCE_NAME}_ClockSet ( uint32_t freq )
{
    const uint32_t base_clk_freq = ${SDMMC_INSTANCE_NAME}_BASECLK_FREQUENCY;
    const uint32_t mult_clk_freq = ${SDMMC_INSTANCE_NAME}_MULTCLK_FREQUENCY;
    uint32_t div = 0;
    uint32_t new_div_freq = 0;
    uint32_t prog_div = 0;
    uint32_t new_prog_freq = 0;
    uint16_t reg_val = 0;
    bool use_prog_mode = false;
    bool hs_mode = freq > SDMMC_CLOCK_FREQ_DS_25_MHZ;

    /* Limit frequency to max supported */
    freq = ${SDMMC_INSTANCE_NAME}_MIN_U32(freq, ${SDMMC_INSTANCE_NAME}_MAX_SUPPORTED_SDCLK_FREQUENCY);

    /* Find the divider in the divided clock mode: DIV = FBASECLK / (2 * FSDCLK)  */
    div = ${SDMMC_INSTANCE_NAME}_CEIL_INT_DIV_U32(base_clk_freq, 2 * freq);

    /* Limit the divider to maximum supported */
    if (div > ${SDMMC_INSTANCE_NAME}_MAX_SUPPORTED_DIVIDER)
    {
        div = ${SDMMC_INSTANCE_NAME}_MAX_SUPPORTED_DIVIDER;
    }

    /* IP limitation: if high speed mode is active, divider must be non zero */
    else if (hs_mode && (0 == div))
    {
        div =  1;
    }

    /* target frequency if divider mode is used */
	new_div_freq = base_clk_freq / (div == 0 ? 1UL : 2 * div);

    /* Check if programmable clock mode is supported and programmable clock is enabled */
    if((0 != mult_clk_freq) &&
      (0 != ((${SDMMC_INSTANCE_NAME}_REGS->SDMMC_CA1R & SDMMC_CA1R_CLKMULT_Msk) >> SDMMC_CA1R_CLKMULT_Pos)))
    {
      /*Find the divider in the programmable clock mode: DIV = (FMULTCLK / FSDCLK) - 1 */
      prog_div = ${SDMMC_INSTANCE_NAME}_CEIL_INT_DIV_U32(mult_clk_freq, freq);

      /* Limit the divider to the maximum possible value */
      if(prog_div > ${SDMMC_INSTANCE_NAME}_MAX_SUPPORTED_DIVIDER)
      {
        prog_div = ${SDMMC_INSTANCE_NAME}_MAX_SUPPORTED_DIVIDER;
      }
      /* IP limitation, if high speed mode is active divider must be non zero */
      else if (hs_mode && (prog_div <= 1))
      {
          prog_div = 1;
      }
      /* DIV counts from zero */
      else if (prog_div > 0)
      {
        prog_div = prog_div - 1;
      }


      /* target frequency if programmable clock mode is used */
      new_prog_freq = mult_clk_freq / (prog_div + 1);

      /* decide on what mode to use based on the least delta from target */
      use_prog_mode = (${SDMMC_INSTANCE_NAME}_ABS_DIFF_U32(freq, new_prog_freq) < ${SDMMC_INSTANCE_NAME}_ABS_DIFF_U32(freq, new_div_freq));
    }

     /* Stop the output clock, so we can change the frequency.
	 * Deviation from the SD Host Controller Specification: if the internal
	 * clock was temporarily disabled, the controller would then switch to
	 * an irrelevant clock frequency, hence keep the SDMMC internal clock enabled. */
	reg_val = ${SDMMC_INSTANCE_NAME}_REGS->SDMMC_CCR & ~SDMMC_CCR_SDCLKEN_Msk;
	${SDMMC_INSTANCE_NAME}_REGS->SDMMC_CCR = reg_val;

	if (hs_mode)
    {
        /* Enable the high speed mode */
        ${SDMMC_INSTANCE_NAME}_REGS->SDMMC_HC1R |= SDMMC_HC1R_SD_SDIO_HSEN_Msk;
    }
    else
    {
        /* Clear the high speed mode */
        SDMMC1_REGS->SDMMC_HC1R &= ~SDMMC_HC1R_SD_SDIO_HSEN_Msk;
    }

    /* Select the clock mode and divider */
	if (use_prog_mode)
    {
		reg_val |= SDMMC_CCR_CLKGSEL_Msk;
        reg_val =   (reg_val & ~SDMMC_CCR_USDCLKFSEL_Msk & ~SDMMC_CCR_SDCLKFSEL_Msk)
                    | SDMMC_CCR_USDCLKFSEL(prog_div >> 8)
                    | SDMMC_CCR_SDCLKFSEL(prog_div & 0xff)
                    | SDMMC_CCR_INTCLKEN_Msk;
    }
	else
    {
		reg_val &= ~SDMMC_CCR_CLKGSEL_Msk;
        reg_val =   (reg_val & ~SDMMC_CCR_USDCLKFSEL_Msk & ~SDMMC_CCR_SDCLKFSEL_Msk)
                    | SDMMC_CCR_USDCLKFSEL(div >> 8)
                    | SDMMC_CCR_SDCLKFSEL(div & 0xff)
                    | SDMMC_CCR_INTCLKEN_Msk;
    }


    /* Start the internal clock (if not started already) and wait for it to stabilize */
    ${SDMMC_INSTANCE_NAME}_REGS->SDMMC_CCR = reg_val;
	while (!(${SDMMC_INSTANCE_NAME}_REGS->SDMMC_CCR & SDMMC_CCR_INTCLKS_Msk)) ;

    /* Start the output clock */
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

<#if USE_CARD_DETECT == true>
    /* Keep the card insertion and removal interrupts enabled */
    normalIntSigEnable = (SDMMC_NISIER_SD_SDIO_CINS_Msk | SDMMC_NISIER_SD_SDIO_CREM_Msk);
</#if>    

    switch (respType)
    {
        case SDMMC_CMD_RESP_R1:
        case SDMMC_CMD_RESP_R5:
        case SDMMC_CMD_RESP_R6:
        case SDMMC_CMD_RESP_R7:
            flags = (SDMMC_CR_RESPTYP_RL48 | SDMMC_CR_CMDCCEN_Msk | SDMMC_CR_CMDICEN_Msk);
            break;

        case SDMMC_CMD_RESP_R3:
        case SDMMC_CMD_RESP_R4:
            flags = SDMMC_CR_RESPTYP_RL48;
            break;

        case SDMMC_CMD_RESP_R1B:
            flags = (SDMMC_CR_RESPTYP_RL48BUSY | SDMMC_CR_CMDCCEN_Msk | SDMMC_CR_CMDICEN_Msk);

            /* Commands with busy response will wait for transfer complete bit */
            normalIntSigEnable |= SDMMC_NISIER_SD_SDIO_TRFC_Msk;
            break;

        case SDMMC_CMD_RESP_R2:
            flags = (SDMMC_CR_RESPTYP_RL136 | SDMMC_CR_CMDCCEN_Msk);
            break;

        default:
            flags = SDMMC_CR_RESPTYP_NORESP;
            break;
    }

    /* Enable command complete interrupt, for commands that do not have busy response type */
    if (respType != SDMMC_CMD_RESP_R1B)
    {
        normalIntSigEnable |= SDMMC_NISIER_SD_SDIO_CMDC_Msk;
    }

    if (transferFlags.isDataPresent == true)
    {
        ${SDMMC_INSTANCE_NAME?lower_case}Obj.isDataInProgress = true;
        ${SDMMC_INSTANCE_NAME}_SetTransferMode(opCode);
        /* Enable data transfer complete and DMA interrupt */
        normalIntSigEnable |= (SDMMC_NISIER_SD_SDIO_TRFC_Msk | SDMMC_NISIER_SD_SDIO_DMAINT_Msk);
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

void ${SDMMC_INSTANCE_NAME}_ModuleInit( void )
{
    /* Reset module*/
    ${SDMMC_INSTANCE_NAME}_REGS->SDMMC_SRR |= SDMMC_SRR_SWRSTALL_Msk;
    while((${SDMMC_INSTANCE_NAME}_REGS->SDMMC_SRR & SDMMC_SRR_SWRSTALL_Msk) == SDMMC_SRR_SWRSTALL_Msk);

    /* Clear the normal and error interrupt status flags */
    ${SDMMC_INSTANCE_NAME}_REGS->SDMMC_EISTR = SDMMC_EISTR_SD_SDIO_Msk;
    ${SDMMC_INSTANCE_NAME}_REGS->SDMMC_NISTR = SDMMC_NISTR_SD_SDIO_Msk;

    /* Enable all the normal interrupt status and error status generation */
    ${SDMMC_INSTANCE_NAME}_REGS->SDMMC_NISTER = SDMMC_NISTER_SD_SDIO_Msk;
    ${SDMMC_INSTANCE_NAME}_REGS->SDMMC_EISTER = SDMMC_EISTER_SD_SDIO_Msk;

    /* Set timeout control register */
    ${SDMMC_INSTANCE_NAME}_REGS->SDMMC_TCR = SDMMC_TCR_DTCVAL(0xE);

    /* Enable ADMA2 (Check CA0R capability register first) */
    ${SDMMC_INSTANCE_NAME}_REGS->SDMMC_HC1R |= SDMMC_HC1R_SD_SDIO_DMASEL(2);

    /* Set SD Bus Power On */
    ${SDMMC_INSTANCE_NAME}_REGS->SDMMC_PCR |= SDMMC_PCR_SDBPWR_Msk;

    /* Set initial clock to 400 KHz*/
    ${SDMMC_INSTANCE_NAME}_ClockSet (SDMMC_CLOCK_FREQ_400_KHZ);

    /* Clear the high speed bit and set the data width to 1-bit mode */
    ${SDMMC_INSTANCE_NAME}_REGS->SDMMC_HC1R &= ~(SDMMC_HC1R_SD_SDIO_HSEN_Msk | SDMMC_HC1R_SD_SDIO_DW_Msk);

<#if USE_CARD_DETECT == true>
    /* Enable card inserted and card removed interrupt signals */
    ${SDMMC_INSTANCE_NAME}_REGS->SDMMC_NISIER = (SDMMC_NISIER_SD_SDIO_CINS_Msk | SDMMC_NISIER_SD_SDIO_CREM_Msk);
</#if>    
}

void ${SDMMC_INSTANCE_NAME}_Initialize( void )
{
    ${SDMMC_INSTANCE_NAME}_InitVariables();
    ${SDMMC_INSTANCE_NAME}_ModuleInit();
}

void ${SDMMC_INSTANCE_NAME}_CallbackRegister( SDMMC_CALLBACK callback, uintptr_t contextHandle )
{
    if (callback != NULL)
    {
        ${SDMMC_INSTANCE_NAME?lower_case}Obj.callback = callback;
        ${SDMMC_INSTANCE_NAME?lower_case}Obj.context = contextHandle;
    }
}
