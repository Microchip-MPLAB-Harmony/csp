/*****************************************************************************
  Company:
    Microchip Technology Inc.

  File Name:
    plib_sdramc${INDEX}.c

  Summary:
    SDRAMC PLIB Source file

  Description:
    None

*******************************************************************************/

/*******************************************************************************
Copyright (c) 2017-18 released Microchip Technology Inc.  All rights reserved.

Microchip licenses to you the right to use, modify, copy and distribute
Software only when embedded on a Microchip microcontroller or digital signal
controller that is integrated into your product or third party product
(pursuant to the sublicense terms in the accompanying license agreement).

You should refer to the license agreement accompanying this Software for
additional information regarding your rights and obligations.

SOFTWARE AND DOCUMENTATION ARE PROVIDED AS IS WITHOUT WARRANTY OF ANY KIND,
EITHER EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION, ANY WARRANTY OF
MERCHANTABILITY, TITLE, NON-INFRINGEMENT AND FITNESS FOR A PARTICULAR PURPOSE.
IN NO EVENT SHALL MICROCHIP OR ITS LICENSORS BE LIABLE OR OBLIGATED UNDER
CONTRACT, NEGLIGENCE, STRICT LIABILITY, CONTRIBUTION, BREACH OF WARRANTY, OR
OTHER LEGAL EQUITABLE THEORY ANY DIRECT OR INDIRECT DAMAGES OR EXPENSES
INCLUDING BUT NOT LIMITED TO ANY INCIDENTAL, SPECIAL, INDIRECT, PUNITIVE OR
CONSEQUENTIAL DAMAGES, LOST PROFITS OR LOST DATA, COST OF PROCUREMENT OF
SUBSTITUTE GOODS, TECHNOLOGY, SERVICES, OR ANY CLAIMS BY THIRD PARTIES
(INCLUDING BUT NOT LIMITED TO ANY DEFENSE THEREOF), OR OTHER SIMILAR COSTS.
*******************************************************************************/
#include "plib_sdramc${INDEX}.h"
#include "${__PROCESSOR?lower_case}.h"

// *****************************************************************************
// *****************************************************************************
// Section: SDRAMC Implementation
// *****************************************************************************
// *****************************************************************************
void SW_DelayUs(uint32_t delay)
{
    uint32_t i, count;

    /* delay * (CPU_FREQ/1000000) / 6 */
    count = delay *  (${SDRAMC_CPU_CLK_FREQ}/1000000)/6;

    /* 6 CPU cycles per iteration */
    for (i = 0; i < count; i++)
        __NOP();
}

void SDRAMC${INDEX?string}_Initialize( void )
{
    uint8_t i;
    uint16_t *pSdramBaseAddress = (uint16_t *)SDRAM_CS_ADDR;

    /* Enable the SDRAMC Chip Select */
    _MATRIX_REGS->CCFG_SMCNFCS.w |= (1 << CCFG_SMCNFCS_SDRAMEN_Pos);

    /* Step 1:
     * Configure SDRAM features and timing parameters */
    _SDRAMC_REGS->SDRAMC_CR.w = SDRAMC_CR_NC_${SDRAMC_CR__NC} | SDRAMC_CR_NR_${SDRAMC_CR__NR} | SDRAMC_CR_NB_${SDRAMC_CR__NB} | SDRAMC_CR_DBW_Msk \
                                | SDRAMC_CR_TRAS(${SDRAMC_CR_TRAS}) |  SDRAMC_CR_TRP(${SDRAMC_CR_TRP}) |  SDRAMC_CR_TRC_TRFC(${SDRAMC_CR_TRC_TRFC}) \
                                | SDRAMC_CR_TRCD(${SDRAMC_CR_TRCD}) | SDRAMC_CR_CAS(${SDRAMC_CR_CAS}) | SDRAMC_CR_TWR(${SDRAMC_CR_TWR}) | SDRAMC_CR_TXSR(${SDRAMC_CR_TXSR});

    _SDRAMC_REGS->SDRAMC_CFR1.w = SDRAMC_CFR1_TMRD(${SDRAMC_CFR1_TMRD}) | SDRAMC_CFR1_UNAL_Msk;

    /* Step 2:
     * For mobile SDRAM, temperature-compensated self refresh (TCSR), drive strength (DS) and partial array
     * self refresh (PASR) must be set in the Low Power Register. */
    <#if SDRAMC_MDR_MD == "LPSDRAM">
    _SDRAMC_REGS->SDRAMC_LPR.w=SDRAMC_LPR_LPCB_${SDRAMC_LPR_LPCB} | SDRAMC_LPR_TIMEOUT_${SDRAMC_LPR_TIMEOUT} | SDRAMC_LPR_PASR(${SDRAMC_LPR_PASR}) | SDRAMC_LPR_TCSR(${SDRAMC_LPR_TCSR}) | SDRAMC_LPR_DS(${SDRAMC_LPR_DS});
    <#else>
    _SDRAMC_REGS->SDRAMC_LPR.w=0;
    </#if>

    /* Step 3:
     * Select the SDRAM memory device type. */
     _SDRAMC_REGS->SDRAMC_MDR.w = SDRAMC_MDR_MD_${SDRAMC_MDR_MD};


    /* Step 4:
     * A pause of at least 200 us must be observed before a signal toggle */
    SW_DelayUs(200);

    /* Step 5:
     * Issue a NOP command to the SDRAM device by writing to the Mode Register.
     * Read back the Mode Register and add a memory barrier assembly instruction just after the read.
     * Write to any SDRAM address to acknowledge this command. Now the clock which drives SDRAM device is enabled */

    _SDRAMC_REGS->SDRAMC_MR.w = SDRAMC_MR_MODE_NOP;
    _SDRAMC_REGS->SDRAMC_MR.w;
    __DMB();
    *pSdramBaseAddress = 0x0;

    /* Step 6:
     * Issue an All banks precharge command by writing to the Mode Register.
     * Read back the Mode Register and add a memory barrier assembly instruction just after the read.
     * Write to any SDRAM address to acknowledge this command. */

    _SDRAMC_REGS->SDRAMC_MR.w = SDRAMC_MR_MODE_ALLBANKS_PRECHARGE;
    _SDRAMC_REGS->SDRAMC_MR.w;
    __DMB();
    *pSdramBaseAddress = 0x0;

    /* Step 7:
     * Issue 8 Auto Refresh(CBR) cycles by writing to the Mode Register.
     * Read back the Mode Register and add a memory barrier assembly instruction just after the read.
     * Perform a write access to any SDRAM address 8 times. */
    _SDRAMC_REGS->SDRAMC_MR.w = SDRAMC_MR_MODE_AUTO_REFRESH;
    _SDRAMC_REGS->SDRAMC_MR.w;
    __DMB();
    for (i = 0; i < 8; i++)
    {
        *pSdramBaseAddress = i;
    }

    /* Step 8:
     * Issue Mode Register Set(MRS) to program the parameters of the SDRAM device, in particular CAS latency and burst length */
    _SDRAMC_REGS->SDRAMC_MR.w = SDRAMC_MR_MODE_LOAD_MODEREG;
    _SDRAMC_REGS->SDRAMC_MR.w;
    __DMB();
    *((uint16_t *)(pSdramBaseAddress + ${SDRAMC_MRS_VALUE})) = 0;

    /* Step 9:
     * Issue Extended Mode Register Set(EMRS) for mobile SDRAM to
     * program the parameters of the SDRAM(TCSR, PASR, DS). Read back the Mode
     * Register and add a memory barrier assembly instruction just after the
     * read. Perform a write access to the SDRAM. The address must be chosen
     * such that BA[1] or BA[0] are set to one. */
    _SDRAMC_REGS->SDRAMC_MR.w = SDRAMC_MR_MODE_EXT_LOAD_MODEREG;
    _SDRAMC_REGS->SDRAMC_MR.w;
    __DMB();
    *((uint16_t *)(pSdramBaseAddress + ${SDRAMC_EMRS_VALUE})) = 0;

    /* Step 10:
     * Transition the SDRAM to NORMAL mode. Read back the Mode
     * Register and add a memory barrier assembly instruction just after the
     * read. Perform a write access to any SDRAM address. */
    _SDRAMC_REGS->SDRAMC_MR.MODE = SDRAMC_MR_MODE_NORMAL;
    _SDRAMC_REGS->SDRAMC_MR.w;
    __DMB();
    *pSdramBaseAddress = 0x0;

    /* Step 11:
     * Configure the Refresh Timer Register. */
    _SDRAMC_REGS->SDRAMC_TR.COUNT = ${SDRAMC_TR_COUNT};

} /* SDRAMC${INDEX?string}_Initialize */
/*******************************************************************************
 End of File
*/
