/*******************************************************************************
  Memory System Service Functions for DDR Initialization

  Company:
    Microchip Technology Inc.

  File Name:
    plib_ddr.c

  Summary:
    Memory System Service implementation for the DDR controller.

  Description:
    The Memory System Service initializes the DDR Controller and PHY to 
    provide access to external DDR2 SDRAM.
    
  Remarks:
    Static interfaces incorporate the driver instance number within the names
    of the routines, eliminating the need for an object ID or object handle.
    Static single-open interfaces also eliminate the need for the open handle.
*******************************************************************************/

//DOM-IGNORE-BEGIN
/*******************************************************************************
Copyright (c) 2013 released Microchip Technology Inc.  All rights reserved.

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
//DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Header Includes
// *****************************************************************************
// *****************************************************************************
#include "peripheral/ddr/plib_ddr.h"

// *****************************************************************************
// *****************************************************************************
// Section: Memory System Service DDR static functions
// *****************************************************************************
// *****************************************************************************

#define sys_mem_ddr_max(a,b) (((a)>(b))?(a):(b))
#define sys_mem_ddr_round_up(x,y) (((x) + (y) - 1UL) / (y))
#define sys_mem_ddr_hc_clk_dly(dly) (sys_mem_ddr_max((sys_mem_ddr_round_up((dly),${DDR_CLK_PER}UL)),2UL)-2UL)

#ifndef round_up
#define round_up(x,y) (((x) + (y) - 1U) / (y))
#endif

//----------------------------------------------------------------------------//
//                          DDR2 SCL Configuration
//----------------------------------------------------------------------------//
/* SCL START */
#define SCL_START_PH_DLY          0x30000000
#define SCL_START_DLY             0x10000000
#define SCL_DONE                  0x10000000U
#define SCL_LUBPASS               3U

static void DDR_Init(void)
{
    uint32_t tmp;
    uint32_t ba_field, ma_field;

    /* Target Arbitration */
    DDRTSELbits.TSEL = ((uint8_t)DDR_TARGET_0 * 5U);
    DDRMINLIMbits.MINLIMIT = 0x${DDR_MINLIM_TGT0}U;
    DDRTSELbits.TSEL = (uint8_t)DDR_TARGET_0 * 8U;
    DDRRQPERbits.RQPER = 0x${DDR_REQPER_TGT0}U;
    DDRTSELbits.TSEL = (uint8_t)DDR_TARGET_0 * 8U;
    DDRMINCMDbits.MINCMD = 0x${DDR_MINCMD_TGT0}U;

    DDRTSELbits.TSEL = ((uint8_t)DDR_TARGET_1 * 5U);
    DDRMINLIMbits.MINLIMIT = 0x${DDR_MINLIM_TGT1}U;
    DDRTSELbits.TSEL = (uint8_t)DDR_TARGET_1 * 8U;
    DDRRQPERbits.RQPER = 0x${DDR_REQPER_TGT1}U;
    DDRTSELbits.TSEL = (uint8_t)DDR_TARGET_1 * 8U;
    DDRMINCMDbits.MINCMD = 0x${DDR_MINCMD_TGT1}U;

    DDRTSELbits.TSEL = ((uint8_t)DDR_TARGET_2* 5U);
    DDRMINLIMbits.MINLIMIT = 0x${DDR_MINLIM_TGT2}U;
    DDRTSELbits.TSEL = (uint8_t)DDR_TARGET_2 * 8U;
    DDRRQPERbits.RQPER = 0x${DDR_REQPER_TGT2}U;
    DDRTSELbits.TSEL = (uint8_t)DDR_TARGET_2 * 8U;
    DDRMINCMDbits.MINCMD = 0x${DDR_MINCMD_TGT2}U;
    
    DDRTSELbits.TSEL = ((uint8_t)DDR_TARGET_3 * 5U);
    DDRMINLIMbits.MINLIMIT = 0x${DDR_MINLIM_TGT3}U;
    DDRTSELbits.TSEL = (uint8_t)DDR_TARGET_3 * 8U;
    DDRRQPERbits.RQPER = 0x${DDR_REQPER_TGT3}U;
    DDRTSELbits.TSEL = (uint8_t)DDR_TARGET_3 * 8U;
    DDRMINCMDbits.MINCMD = 0x${DDR_MINCMD_TGT3}U;

    DDRTSELbits.TSEL = ((uint8_t)DDR_TARGET_4 * 5U);
    DDRMINLIMbits.MINLIMIT = 0x${DDR_MINLIM_TGT4}U;
    DDRTSELbits.TSEL = (uint8_t)DDR_TARGET_4 * 8U;
    DDRRQPERbits.RQPER = 0x${DDR_REQPER_TGT4}U;
    DDRTSELbits.TSEL = (uint8_t)DDR_TARGET_4 * 8U;
    DDRMINCMDbits.MINCMD = 0x${DDR_MINCMD_TGT4}U;

    /* Addressing */
    DDRMEMCFG0bits.RWADDR = ROW_ADDR_RSHIFT;
    DDRMEMCFG1bits.RWADDRMSK = (uint16_t)ROW_ADDR_MASK;
    DDRMEMCFG0bits.CLHADDR = COL_HI_RSHFT;
    DDRMEMCFG3bits.CLADDRLMSK = (uint16_t)COL_LO_MASK;
    DDRMEMCFG2bits.CLADDRHMSK = COL_HI_MASK;
    DDRMEMCFG0bits.BNKADDR = BA_RSHFT;
    DDRMEMCFG4bits.BNKADDRMSK = (uint8_t)BANK_ADDR_MASK;
    DDRMEMCFG0bits.CSADDR = CS_ADDR_RSHIFT;
    DDRMEMCFG4bits.CSADDRMSK = CS_ADDR_MASK;

    /* Refresh */
    DDRREFCFGbits.REFCNT = ((${DDR_TRFI}U + CTRL_CLK_PERIOD - 1U) / CTRL_CLK_PERIOD) - (2U);
    DDRREFCFGbits.REFDLY = ((${DDR_TRFC}U + CTRL_CLK_PERIOD - 1U) / CTRL_CLK_PERIOD) - (2U);
    DDRREFCFGbits.MAXREFS = ${DDR_MAX_PEND_REFS}U;
    DDRPWRCFGbits.ASLFREFEN = 0U;

    /* Power */
<#if DDR_AUTO_PWR_DOWN = true>
    DDRPWRCFGbits.APWRDNEN = 1U;
<#else>
    DDRPWRCFGbits.APWRDNEN = 0U;
</#if>
<#if DDR_AUTO_PCHRG = true>
    DDRMEMCFG0bits.APCHRGEN = 1U;
<#else>
    DDRMEMCFG0bits.APCHRGEN = 0U;
</#if>
<#if DDR_AUTO_PCHRG = true>
    DDRPWRCFGbits.PCHRGPWRDN = 1U;
<#else>
    DDRPWRCFGbits.PCHRGPWRDN = 0U;
</#if>

    /* Timing */
    DDRDLYCFG0bits.R2WDLY = ${DDR_BRST_LEN}U + 2u;
    DDRDLYCFG0bits.RMWDLY = ${DDR_CAS_LAT}U - ${DDR_WR_LAT}U + 3u;

    uint32_t w2rdly, w2rcsdly;

    w2rdly = round_up(${DDR_TWTR}U, CTRL_CLK_PERIOD) + ${DDR_WR_LAT}U + ${DDR_BRST_LEN}U;
    w2rcsdly = ((w2rdly - 1u) > 3u) ? (w2rdly - 1u) : 3u;

    DDRDLYCFG0bits.W2RDLY = (uint8_t)(w2rdly & 0x0Fu);
    DDRDLYCFG1bits.W2RDLY4 = (uint8_t)(((w2rdly & 0x10u) != 0U) ? 1U : 0U);
    DDRDLYCFG0bits.W2RCSDLY = (uint8_t)(w2rcsdly & 0x0Fu);
    DDRDLYCFG1bits.W2RCSDLY4 = (uint8_t)(((w2rcsdly & 0x10u) != 0U) ? 1U : 0U);
    DDRDLYCFG0bits.R2RDLY = ${DDR_BRST_LEN}U - 1u;
    DDRDLYCFG0bits.R2RCSDLY = ${DDR_BRST_LEN}U;
    DDRDLYCFG0bits.W2WDLY = ${DDR_BRST_LEN}U - 1u;
    DDRDLYCFG0bits.W2WCSDLY = ${DDR_BRST_LEN}U - 1u;
    DDRPWRCFGbits.SLFREFDLY = ${DDR_SELF_REFRESH_DELAY}U;
    DDRDLYCFG1bits.SLFREFMINDLY = ${DDR_TCKE}U - 1u;
    DDRDLYCFG1bits.SLFREFEXDLY = (round_up(${DDR_TDLLK}U, 2u) - 2u) & 0xFFu;
    DDRDLYCFG1bits.SLFREFEXDLY8 = (uint8_t)(((round_up(${DDR_TDLLK}U, 2u) & 0x100u) != 0U) ? 1U : 0U);
    DDRPWRCFGbits.PWRDNDLY = ${DDR_PWR_DOWN_DELAY}U;
    DDRDLYCFG1bits.PWRDNMINDLY = ${DDR_TCKE}U - 1U; 
<#if  DDR_TCKE gt DDR_TXP>   
    DDRDLYCFG1bits.PWRDNEXDLY = ${DDR_TCKE};
<#else>
    DDRDLYCFG1bits.PWRDNEXDLY = ${DDR_TXP}) - 1U; 
</#if>   
    DDRDLYCFG2bits.PCHRGALLDLY = round_up(${DDR_TRP}U, CTRL_CLK_PERIOD); 
    DDRDLYCFG2bits.R2PCHRGDLY = round_up(${DDR_TRTP}U, CTRL_CLK_PERIOD) + ${DDR_BRST_LEN}U - 2U; 
    DDRDLYCFG2bits.W2PCHRGDLY = (round_up(${DDR_TWR}U, CTRL_CLK_PERIOD) + ${DDR_WR_LAT}U + ${DDR_BRST_LEN}U) & 0x0FU;
    DDRDLYCFG1bits.W2PCHRGDLY4 = (uint8_t)((((round_up(${DDR_TWR}U, CTRL_CLK_PERIOD) + ${DDR_WR_LAT}U + ${DDR_BRST_LEN}U) & 0x10u) != 0U) ? 1U : 0U);
    DDRDLYCFG2bits.PCHRG2RASDLY = round_up(${DDR_TRP}U, CTRL_CLK_PERIOD) - 1U; 
    DDRDLYCFG3bits.RAS2PCHRGDLY = round_up(${DDR_TRAS}U, CTRL_CLK_PERIOD) - 1U;
    DDRDLYCFG3bits.RAS2RASSBNKDLY = round_up(${DDR_TRC}U, CTRL_CLK_PERIOD) - 1U;
    DDRDLYCFG2bits.RAS2RASDLY = round_up(${DDR_TRRD}U, CTRL_CLK_PERIOD) - 1U;
    DDRDLYCFG2bits.RAS2CASDLY = round_up(${DDR_TRCD}U, CTRL_CLK_PERIOD) - 1U;
    DDRDLYCFG2bits.RBENDDLY = ${DDR_CAS_LAT}U + 3u;
    DDRXFERCFGbits.NXTDATRQDLY = 2U;
    DDRXFERCFGbits.NXTDATAVDLY = 4U;
    DDRDLYCFG1bits.NXTDATAVDLY4 = (uint8_t)((((${DDR_CAS_LAT}U + 5u) & 0x10u) != 0U) ? 1U : 0U);
    DDRXFERCFGbits.RDATENDLY = 2U;/*${DDR_CAS_LAT} - 1*/
    DDRDLYCFG3bits.FAWTDLY = round_up(${DDR_TFAW}U, CTRL_CLK_PERIOD) - 1U;

    /* On-Die Termination */
<#if DDR_ODT_READ_ENABLE == true>
    DDRODTCFGbits.ODTCSEN = 0U;
    DDRODTENCFGbits.ODTREN = 1U;
    DDRODTCFGbits.ODTRLEN = ${DDR_ODT_READ_CLOCKS}U;
    DDRODTCFGbits.ODTRDLY = ${DDR_ODT_READ_DLY}U;
<#else>
    DDRODTCFGbits.ODTCSEN = 0U;
    DDRODTENCFGbits.ODTREN = 0U;
</#if>
<#if DDR_ODT_WRITE_ENABLE == true>
    DDRODTCFGbits.ODTCSEN = 0U;
    DDRODTENCFGbits.ODTWEN = 1U;
    DDRODTCFGbits.ODTWLEN = ${DDR_ODT_WRITE_CLOCKS}U;
    DDRODTCFGbits.ODTWDLY = ${DDR_ODT_WRITE_DLY}U;
<#else>
    DDRODTCFGbits.ODTCSEN = 0U;
    DDRODTENCFGbits.ODTWEN = 0U;
</#if>

    /* Controller Settings */
    DDRXFERCFGbits.BIGENDIAN = 0U;
    DDRMEMWIDTHbits.HALFRATE = 1U;
    DDRXFERCFGbits.MAXBURST = 3U;
    DDRCMDISSUEbits.NUMHOSTCMDS = 12U;

    /* DRAM Initialization */

    /* bring CKE high after reset and wait 400 nsec */
    *(&DDRCMD10 + DDR_HOST_CMD_REG_10) = DRV_DDR_IDLE_NOP;
    *(&DDRCMD10 + DDR_HOST_CMD_REG_20) = (0x00U | (0x00UL << 8) | (sys_mem_ddr_hc_clk_dly(400000UL) << 11));

    /* issue precharge all command */
    *(&DDRCMD10 + DDR_HOST_CMD_REG_11) = DRV_DDR_PRECH_ALL_CMD;
    *(&DDRCMD10 + DDR_HOST_CMD_REG_21) = (0x04U | (0x00UL << 8) | (sys_mem_ddr_hc_clk_dly(${DDR_TRP}U + ${DDR_CLK_PER}U) << 11));

    /* initialize EMR2 */
    *(&DDRCMD10 + DDR_HOST_CMD_REG_12) = DRV_DDR_LOAD_MODE_CMD;
    *(&DDRCMD10 + DDR_HOST_CMD_REG_22) = (0x00U | (0x02UL << 8) | (sys_mem_ddr_hc_clk_dly(${DDR_TMRD}U * ${DDR_CLK_PER}U) << 11));

    /* initialize EMR3 */
    *(&DDRCMD10 + DDR_HOST_CMD_REG_13) = DRV_DDR_LOAD_MODE_CMD;
    *(&DDRCMD10 + DDR_HOST_CMD_REG_23) = (0x00U | (0x03UL << 8) | (sys_mem_ddr_hc_clk_dly(${DDR_TMRD}U * ${DDR_CLK_PER}U) << 11));

    /* RDQS disable, DQSB enable, OCD exit, 150 ohm termination, AL=0, DLL enable */
    *(&DDRCMD10 + DDR_HOST_CMD_REG_14) = (DRV_DDR_LOAD_MODE_CMD | (0x40UL << 24));
    *(&DDRCMD10 + DDR_HOST_CMD_REG_24) = (0x00U | (0x01UL << 8) | (sys_mem_ddr_hc_clk_dly(${DDR_TMRD}U * ${DDR_CLK_PER}U) << 11));

    tmp = ((sys_mem_ddr_round_up(${DDR_TWR}U, ${DDR_CLK_PER}U) -1U ) << 1) | 1U;
    ma_field = tmp & 0xFFU;
    ba_field = (tmp >> 8) & 0x03U;

    /* PD fast exit, WR REC = tWR in clocks -1, DLL reset, CAS = RL, burst = 4 */
    *(&DDRCMD10 + DDR_HOST_CMD_REG_15) = (DRV_DDR_LOAD_MODE_CMD | (((${DDR_CAS_LAT}UL << 4) | 2UL) << 24));
    *(&DDRCMD10 + DDR_HOST_CMD_REG_25) = (ma_field | (ba_field << 8) | (sys_mem_ddr_hc_clk_dly(${DDR_TMRD}U * ${DDR_CLK_PER}U) << 11));

    /* issue precharge all command */
    *(&DDRCMD10 + DDR_HOST_CMD_REG_16) = DRV_DDR_PRECH_ALL_CMD;
    *(&DDRCMD10 + DDR_HOST_CMD_REG_26) = (0x04U | (0x00UL << 8) | (sys_mem_ddr_hc_clk_dly(${DDR_TRP}U + ${DDR_CLK_PER}U) << 11));

    /* issue refresh command */
    *(&DDRCMD10 + DDR_HOST_CMD_REG_17) = DRV_DDR_REF_CMD;
    *(&DDRCMD10 + DDR_HOST_CMD_REG_27) = (0x00U | (0x00UL << 8) | (sys_mem_ddr_hc_clk_dly(${DDR_TRFC}U) << 11));

    /* issue refresh command */
    *(&DDRCMD10 + DDR_HOST_CMD_REG_18) = DRV_DDR_REF_CMD;
    *(&DDRCMD10 + DDR_HOST_CMD_REG_28) = (0x00U | (0x00UL << 8) | (sys_mem_ddr_hc_clk_dly(${DDR_TRFC}U) << 11));
    
    tmp = ((sys_mem_ddr_round_up(15000U, 2500U) -1U) << 1);
    ma_field = tmp & 0xFFU;
    ba_field = (tmp >> 8) & 0x03U;

    /* Mode register programming as before without DLL reset */
    *(&DDRCMD10 + DDR_HOST_CMD_REG_19) = (DRV_DDR_LOAD_MODE_CMD | (((${DDR_CAS_LAT}UL << 4) | 3U) << 24));
    *(&DDRCMD10 + DDR_HOST_CMD_REG_29) = (ma_field | (ba_field << 8) | (sys_mem_ddr_hc_clk_dly(${DDR_TMRD}U * ${DDR_CLK_PER}U) << 11));
    
    /* extended mode register same as before with OCD default */
    *(&DDRCMD10 + DDR_HOST_CMD_REG_110) = (DRV_DDR_LOAD_MODE_CMD | (0xC0UL << 24U));
    *(&DDRCMD10 + DDR_HOST_CMD_REG_210) = (0x03U | (0x01UL << 8) | (sys_mem_ddr_hc_clk_dly(${DDR_TMRD}U * ${DDR_CLK_PER}U) << 11));
    
    /* extended mode register same as before with OCD exit */
    *(&DDRCMD10 + DDR_HOST_CMD_REG_111) = (DRV_DDR_LOAD_MODE_CMD | (0x40UL << 24));
    *(&DDRCMD10 + DDR_HOST_CMD_REG_211) = (0x00U | (0x01UL << 8) | (sys_mem_ddr_hc_clk_dly(140U * ${DDR_CLK_PER}U) << 11));

    /* Set number of host commands */
    DDRCMDISSUEbits.NUMHOSTCMDS = 0x${DDR_NUM_CMDS}U;
    DDRCMDISSUEbits.VALID = 1U;
    DDRMEMCONbits.STINIT = 1U;
    while (DDRCMDISSUEbits.VALID != 0U)
    {
        /* Nothing to do */
    }
    DDRMEMCONbits.INITDN = 1U;
}

static void DDR_PHY_Init(void)
{
<#if DDR_PHY_ODT_ENABLE == true>
    DDRPHYPADCONbits.ODTSEL = ${DDR_PHY_ODT_VALUE}U;
    DDRPHYPADCONbits.ODTEN = 1U;
<#else>
    DDRPHYPADCONbits.ODTEN = 0U;
</#if>

    DDRPHYPADCONbits.DATDRVSEL = ${DDR_PHY_SYS_MEMORY_STRENGTH_DATA}U;
    DDRPHYPADCONbits.ADDCDRVSEL = ${DDR_PHY_SYS_MEMORY_STRENGTH_ADDC}U;
    DDRPHYPADCONbits.ODTPUCAL = ${DDR_PHY_ODT_PU_CAL}U;
    DDRPHYPADCONbits.ODTPDCAL = ${DDR_PHY_ODT_PD_CAL}U;
    DDRPHYPADCONbits.DRVSTRNFET = ${DDR_PHY_SYS_MEMORY_STR_NFET_CAL}U;
    DDRPHYPADCONbits.DRVSTRPFET = ${DDR_PHY_SYS_MEMORY_STR_PFET_CAL}U;
    
    DDRPHYPADCONbits.NOEXTDLL = 1U;
    
<#if DDR_PHY_EXTRA_CLK == true>
    DDRPHYPADCONbits.EOENCLKCYC = 1U; 
<#else>
    DDRPHYPADCONbits.EOENCLKCYC = 0U;
</#if>

<#if DDR_PHY_RCVREN == true>
    DDRPHYPADCONbits.RCVREN = 1U;
<#else>
    DDRPHYPADCONbits.RCVREN = 0U;
</#if>
    DDRPHYPADCONbits.PREAMBDLY = ${DDR_PHY_PRE_DLY}U;
    DDRPHYPADCONbits.HALFRATE = 1U;
<#if DDR_PHY_WR_CMD_DLY == true>
    DDRPHYPADCONbits.WRCMDDLY = 1U;
<#else>
    DDRPHYPADCONbits.WRCMDDLY = 0U;
</#if>
<#if DDR_PHY_RECALIB_EN == true>
    DDRPHYDLLRbits.RECALIBCNT = ${DDR_PHY_RECALIB_COUNT}U;
    DDRPHYDLLRbits.DISRECALIB = 0U;
<#else>
    DDRPHYDLLRbits.DISRECALIB = 1U;
</#if>
    DDRPHYDLLRbits.DLYSTVAL = ${DDR_PHY_DLL_MASTER_DELAY_START}U;
    DDRSCLCFG0bits.BURST8 = (uint8_t)${DDR_PHY_SCL_BURST_MODE};
    DDRSCLCFG0bits.DDR2 = (uint8_t)((uint8_t)${DDR_PHY_DDR_TYPE} == 0U);
    DDRSCLCFG0bits.RCASLAT = ${DDR_CAS_LAT}U;
    DDRSCLCFG1bits.WCASLAT = ${DDR_WR_LAT}U;

<#if DDR_PHY_ODT_CS_EN == true>
    DDRSCLCFG0bits.ODTCSW = 1U;
<#else>
    DDRSCLCFG0bits.ODTCSW = 0U;
</#if>
    DDRSCLCFG1bits.DBLREFDLY = ${DDR_PHY_SCL_DLY}U;
    DDRSCLLATbits.DDRCLKDLY = ${DDR_PHY_SCL_MAIN_CLK_DELAY}U;
    DDRSCLLATbits.CAPCLKDLY = ${DDR_PHY_SCL_CAP_CLK_DELAY}U;

<#if DDR_SCL_CS_EN>
    /* Chip select 0 enabled by hardware. Other chip selects not available. */
    /* DDRSCLCFG1bits.SCLCSEN = 0;*/
</#if>
}

static void DDR_PHY_Calib(void)
{
    /* SCL Start */
    DDRSCLSTART = SCL_START_PH_DLY;  //START SCL DELAY and phase calibration
    for (;;)
    {
        while ((DDRSCLSTART & SCL_DONE) != 0U) //Wait for the Calibration to finish
        {
           /* Nothing to do */ 
        }

        DDRSCLSTART = SCL_START_DLY;
        while ((DDRSCLSTART & SCL_DONE) != 0U) //Wait for the Calibration to finish
        {
            /* Nothing to do */
        }

        if ((DDRSCLSTART & SCL_LUBPASS) != SCL_LUBPASS) //If Calibration fails, retry
        {
            DDRPHYCLKDLY = 0x10;
            DDRSCLSTART = SCL_START_PH_DLY;
        } 
        else
        {
            break;   //If Calibration passes, continue with the rest of the program
        }
    }
}

void DDR_Initialize(void)
{
    DDR_PHY_Init();
    DDR_Init();
    DDR_PHY_Calib();
}

/*******************************************************************************
 End of File
*/
