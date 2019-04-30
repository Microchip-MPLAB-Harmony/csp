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
#define sys_mem_ddr_round_up(x,y) (((x) + (y) - 1) / (y))
#define sys_mem_ddr_hc_clk_dly(dly) (sys_mem_ddr_max((sys_mem_ddr_round_up((dly),${DDR_CLK_PER})),2)-2)

#ifndef round_up
#define round_up(x,y) (((x) + (y) - 1) / (y))
#endif

static void DDR_Init(void)
{
    uint32_t tmp;
    uint32_t ba_field, ma_field;

    /* Target Arbitration */
	DDRTSELbits.TSEL = (DDR_TARGET_0 * 5);
	DDRMINLIMbits.MINLIMIT = 0x${DDR_MINLIM_TGT0};
	DDRTSELbits.TSEL = DDR_TARGET_0 * 8;
	DDRRQPERbits.RQPER = 0x${DDR_REQPER_TGT0};
	DDRTSELbits.TSEL = DDR_TARGET_0 * 8;
	DDRMINCMDbits.MINCMD = 0x${DDR_MINCMD_TGT0};

	DDRTSELbits.TSEL = (DDR_TARGET_1 * 5);
	DDRMINLIMbits.MINLIMIT = 0x${DDR_MINLIM_TGT1};
	DDRTSELbits.TSEL = DDR_TARGET_1 * 8;
	DDRRQPERbits.RQPER = 0x${DDR_REQPER_TGT1};
	DDRTSELbits.TSEL = DDR_TARGET_1 * 8;
	DDRMINCMDbits.MINCMD = 0x${DDR_MINCMD_TGT1};

	DDRTSELbits.TSEL = (DDR_TARGET_2* 5);
	DDRMINLIMbits.MINLIMIT = 0x${DDR_MINLIM_TGT2};
	DDRTSELbits.TSEL = DDR_TARGET_2 * 8;
	DDRRQPERbits.RQPER = 0x${DDR_REQPER_TGT2};
	DDRTSELbits.TSEL = DDR_TARGET_2 * 8;
	DDRMINCMDbits.MINCMD = 0x${DDR_MINCMD_TGT2};
	
	DDRTSELbits.TSEL = (DDR_TARGET_3 * 5);
	DDRMINLIMbits.MINLIMIT = 0x${DDR_MINLIM_TGT3};
	DDRTSELbits.TSEL = DDR_TARGET_3 * 8;
	DDRRQPERbits.RQPER = 0x${DDR_REQPER_TGT3};
	DDRTSELbits.TSEL = DDR_TARGET_3 * 8;
	DDRMINCMDbits.MINCMD = 0x${DDR_MINCMD_TGT3};

	DDRTSELbits.TSEL = (DDR_TARGET_4 * 5);
	DDRMINLIMbits.MINLIMIT = 0x${DDR_MINLIM_TGT4};
	DDRTSELbits.TSEL = DDR_TARGET_4 * 8;
	DDRRQPERbits.RQPER = 0x${DDR_REQPER_TGT4};
	DDRTSELbits.TSEL = DDR_TARGET_4 * 8;
	DDRMINCMDbits.MINCMD = 0x${DDR_MINCMD_TGT4};

    /* Addressing */
	DDRMEMCFG0bits.RWADDR = ROW_ADDR_RSHIFT;
	DDRMEMCFG1bits.RWADDRMSK = ROW_ADDR_MASK;
    DDRMEMCFG0bits.CLHADDR = COL_HI_RSHFT;
	DDRMEMCFG3bits.CLADDRLMSK = COL_LO_MASK;
	DDRMEMCFG2bits.CLADDRHMSK = COL_HI_MASK;
	DDRMEMCFG0bits.BNKADDR = BA_RSHFT;
	DDRMEMCFG4bits.BNKADDRMSK = BANK_ADDR_MASK;
	DDRMEMCFG0bits.CSADDR = CS_ADDR_RSHIFT;
	DDRMEMCFG4bits.CSADDRMSK = CS_ADDR_MASK;

    /* Refresh */
	DDRREFCFGbits.REFCNT = (${DDR_TRFI} + CTRL_CLK_PERIOD - 1) / CTRL_CLK_PERIOD - 2;
	DDRREFCFGbits.REFDLY = (${DDR_TRFC} + CTRL_CLK_PERIOD - 1) / CTRL_CLK_PERIOD - 2;
	DDRREFCFGbits.MAXREFS = ${DDR_MAX_PEND_REFS};
	DDRPWRCFGbits.ASLFREFEN = 0;

    /* Power */
<#if DDR_AUTO_PWR_DOWN = true>
	DDRPWRCFGbits.APWRDNEN = 1;
<#else>
	DDRPWRCFGbits.APWRDNEN = 0;
</#if>
<#if DDR_AUTO_PCHRG = true>
	DDRMEMCFG0bits.APCHRGEN = 1;
<#else>
	DDRMEMCFG0bits.APCHRGEN = 0;
</#if>
<#if DDR_AUTO_PCHRG = true>
	DDRPWRCFGbits.PCHRGPWRDN = 1;
<#else>
	DDRPWRCFGbits.PCHRGPWRDN = 0;
</#if>

    /* Timing */
	DDRDLYCFG0bits.R2WDLY = ${DDR_BRST_LEN} + 2u;
	DDRDLYCFG0bits.RMWDLY = ${DDR_CAS_LAT} - ${DDR_WR_LAT} + 3u;

    uint32_t w2rdly, w2rcsdly;

    w2rdly = round_up(${DDR_TWTR}, CTRL_CLK_PERIOD) + ${DDR_WR_LAT} + ${DDR_BRST_LEN};
    w2rcsdly = ((w2rdly - 1u) > 3u) ? (w2rdly - 1u) : 3u;

	DDRDLYCFG0bits.W2RDLY = w2rdly & 0x0Fu;
	DDRDLYCFG1bits.W2RDLY4 = ((w2rdly & 0x10u) != 0) ? 1 : 0;
	DDRDLYCFG0bits.W2RCSDLY = w2rcsdly & 0x0Fu;
	DDRDLYCFG1bits.W2RCSDLY4 = ((w2rcsdly & 0x10u) != 0) ? 1 : 0;
	DDRDLYCFG0bits.R2RDLY = ${DDR_BRST_LEN} - 1u;
	DDRDLYCFG0bits.R2RCSDLY = ${DDR_BRST_LEN};
	DDRDLYCFG0bits.W2WDLY = ${DDR_BRST_LEN} - 1u;
	DDRDLYCFG0bits.W2WCSDLY = ${DDR_BRST_LEN} - 1u;
	DDRPWRCFGbits.SLFREFDLY = ${DDR_SELF_REFRESH_DELAY};
	DDRDLYCFG1bits.SLFREFMINDLY = ${DDR_TCKE} - 1u;
	DDRDLYCFG1bits.SLFREFEXDLY = (round_up(${DDR_TDLLK}, 2u) - 2u) & 0xFFu;
	DDRDLYCFG1bits.SLFREFEXDLY8 = ((round_up(${DDR_TDLLK}, 2u) & 0x100u) != 0) ? 1u : 0;
	DDRPWRCFGbits.PWRDNDLY = ${DDR_PWR_DOWN_DELAY};
	DDRDLYCFG1bits.PWRDNMINDLY = ${DDR_TCKE} - 1;	
	DDRDLYCFG1bits.PWRDNEXDLY = (${DDR_TCKE} > ${DDR_TXP} ? ${DDR_TCKE} : ${DDR_TXP}) - 1; 
	DDRDLYCFG2bits.PCHRGALLDLY = round_up(${DDR_TRP}, CTRL_CLK_PERIOD); 
	DDRDLYCFG2bits.R2PCHRGDLY = round_up(${DDR_TRTP}, CTRL_CLK_PERIOD) + ${DDR_BRST_LEN} - 2; 
	DDRDLYCFG2bits.W2PCHRGDLY = (round_up(${DDR_TWR}, CTRL_CLK_PERIOD) + ${DDR_WR_LAT} + ${DDR_BRST_LEN}) & 0x0F;
	DDRDLYCFG1bits.W2PCHRGDLY4 = (((round_up(${DDR_TWR}, CTRL_CLK_PERIOD) + ${DDR_WR_LAT} + ${DDR_BRST_LEN}) & 0x10u) != 0) ? 1 : 0;
	DDRDLYCFG2bits.PCHRG2RASDLY = round_up(${DDR_TRP}, CTRL_CLK_PERIOD) - 1; 
	DDRDLYCFG3bits.RAS2PCHRGDLY = round_up(${DDR_TRAS}, CTRL_CLK_PERIOD) - 1;
	DDRDLYCFG3bits.RAS2RASSBNKDLY = round_up(${DDR_TRC}, CTRL_CLK_PERIOD) - 1;
	DDRDLYCFG2bits.RAS2RASDLY = round_up(${DDR_TRRD}, CTRL_CLK_PERIOD) - 1;
	DDRDLYCFG2bits.RAS2CASDLY = round_up(${DDR_TRCD}, CTRL_CLK_PERIOD) - 1;
	DDRDLYCFG2bits.RBENDDLY = ${DDR_CAS_LAT} + 3u;
	DDRXFERCFGbits.NXTDATRQDLY = 2;
	DDRXFERCFGbits.NXTDATAVDLY = 4;
	DDRDLYCFG1bits.NXTDATAVDLY4 = (((${DDR_CAS_LAT} + 5u) & 0x10u) != 0) ? 1 : 0;
	DDRXFERCFGbits.RDATENDLY = 2;/*${DDR_CAS_LAT} - 1*/
	DDRDLYCFG3bits.FAWTDLY = round_up(${DDR_TFAW}, CTRL_CLK_PERIOD) - 1;

    /* On-Die Termination */
<#if DDR_ODT_READ_ENABLE == true>
	DDRODTCFGbits.ODTCSEN = 0;
	DDRODTENCFGbits.ODTREN = 1;
	DDRODTCFGbits.ODTRLEN = ${DDR_ODT_READ_CLOCKS};
	DDRODTCFGbits.ODTRDLY = ${DDR_ODT_READ_DLY};
<#else>
	DDRODTCFGbits.ODTCSEN = 0;
	DDRODTENCFGbits.ODTREN = 0;
</#if>
<#if DDR_ODT_WRITE_ENABLE == true>
	DDRODTCFGbits.ODTCSEN = 0;
	DDRODTENCFGbits.ODTWEN = 1;
	DDRODTCFGbits.ODTWLEN = ${DDR_ODT_WRITE_CLOCKS};
	DDRODTCFGbits.ODTWDLY = ${DDR_ODT_WRITE_DLY};
<#else>
	DDRODTCFGbits.ODTCSEN = 0;
	DDRODTENCFGbits.ODTWEN = 0;
</#if>

    /* Controller Settings */
	DDRXFERCFGbits.BIGENDIAN = 0;
	DDRMEMWIDTHbits.HALFRATE = 1;
	DDRXFERCFGbits.MAXBURST = 3;
	DDRCMDISSUEbits.NUMHOSTCMDS = 12;

    /* DRAM Initialization */

    /* bring CKE high after reset and wait 400 nsec */
	*(&DDRCMD10 + DDR_HOST_CMD_REG_10) = DRV_DDR_IDLE_NOP;
	*(&DDRCMD10 + DDR_HOST_CMD_REG_20) = (0x00 | (0x00 << 8) | (sys_mem_ddr_hc_clk_dly(400000) << 11));

    /* issue precharge all command */
	*(&DDRCMD10 + DDR_HOST_CMD_REG_11) = DRV_DDR_PRECH_ALL_CMD;
	*(&DDRCMD10 + DDR_HOST_CMD_REG_21) = (0x04 | (0x00 << 8) | (sys_mem_ddr_hc_clk_dly(${DDR_TRP} + ${DDR_CLK_PER}) << 11));

    /* initialize EMR2 */
	*(&DDRCMD10 + DDR_HOST_CMD_REG_12) = DRV_DDR_LOAD_MODE_CMD;
	*(&DDRCMD10 + DDR_HOST_CMD_REG_22) = (0x00 | (0x02 << 8) | (sys_mem_ddr_hc_clk_dly(${DDR_TMRD} * ${DDR_CLK_PER}) << 11));

    /* initialize EMR3 */
	*(&DDRCMD10 + DDR_HOST_CMD_REG_13) = DRV_DDR_LOAD_MODE_CMD;
	*(&DDRCMD10 + DDR_HOST_CMD_REG_23) = (0x00 | (0x03 << 8) | (sys_mem_ddr_hc_clk_dly(${DDR_TMRD} * ${DDR_CLK_PER}) << 11));

    /* RDQS disable, DQSB enable, OCD exit, 150 ohm termination, AL=0, DLL enable */
	*(&DDRCMD10 + DDR_HOST_CMD_REG_14) = (DRV_DDR_LOAD_MODE_CMD | (0x40 << 24));
	*(&DDRCMD10 + DDR_HOST_CMD_REG_24) = (0x00 | (0x01 << 8) | (sys_mem_ddr_hc_clk_dly(${DDR_TMRD} * ${DDR_CLK_PER}) << 11));

    tmp = ((sys_mem_ddr_round_up(${DDR_TWR}, ${DDR_CLK_PER}) -1 ) << 1) | 1;
    ma_field = tmp & 0xFF;
    ba_field = (tmp >> 8) & 0x03;

    /* PD fast exit, WR REC = tWR in clocks -1, DLL reset, CAS = RL, burst = 4 */
	*(&DDRCMD10 + DDR_HOST_CMD_REG_15) = (DRV_DDR_LOAD_MODE_CMD | (((${DDR_CAS_LAT} << 4) | 2) << 24));
	*(&DDRCMD10 + DDR_HOST_CMD_REG_25) = (ma_field | (ba_field << 8) | (sys_mem_ddr_hc_clk_dly(${DDR_TMRD} * ${DDR_CLK_PER}) << 11));

    /* issue precharge all command */
	*(&DDRCMD10 + DDR_HOST_CMD_REG_16) = DRV_DDR_PRECH_ALL_CMD;
	*(&DDRCMD10 + DDR_HOST_CMD_REG_26) = (0x04 | (0x00 << 8) | (sys_mem_ddr_hc_clk_dly(${DDR_TRP} + ${DDR_CLK_PER}) << 11));

    /* issue refresh command */
	*(&DDRCMD10 + DDR_HOST_CMD_REG_17) = DRV_DDR_REF_CMD;
	*(&DDRCMD10 + DDR_HOST_CMD_REG_27) = (0x00 | (0x00 << 8) | (sys_mem_ddr_hc_clk_dly(${DDR_TRFC}) << 11));

    /* issue refresh command */
	*(&DDRCMD10 + DDR_HOST_CMD_REG_18) = DRV_DDR_REF_CMD;
	*(&DDRCMD10 + DDR_HOST_CMD_REG_28) = (0x00 | (0x00 << 8) | (sys_mem_ddr_hc_clk_dly(${DDR_TRFC}) << 11));
	
    tmp = ((sys_mem_ddr_round_up(15000, 2500) -1 ) << 1);
    ma_field = tmp & 0xFF;
    ba_field = (tmp >> 8) & 0x03;

    /* Mode register programming as before without DLL reset */
	*(&DDRCMD10 + DDR_HOST_CMD_REG_19) = (DRV_DDR_LOAD_MODE_CMD | (((${DDR_CAS_LAT} << 4) | 3) << 24));
	*(&DDRCMD10 + DDR_HOST_CMD_REG_29) = (ma_field | (ba_field << 8) | (sys_mem_ddr_hc_clk_dly(${DDR_TMRD} * ${DDR_CLK_PER}) << 11));
	
    /* extended mode register same as before with OCD default */
	*(&DDRCMD10 + DDR_HOST_CMD_REG_110) = (DRV_DDR_LOAD_MODE_CMD | (0xC0 << 24));
	*(&DDRCMD10 + DDR_HOST_CMD_REG_210) = (0x03 | (0x01 << 8) | (sys_mem_ddr_hc_clk_dly(${DDR_TMRD} * ${DDR_CLK_PER}) << 11));
	
    /* extended mode register same as before with OCD exit */
	*(&DDRCMD10 + DDR_HOST_CMD_REG_111) = (DRV_DDR_LOAD_MODE_CMD | (0x40 << 24));
	*(&DDRCMD10 + DDR_HOST_CMD_REG_211) = (0x00 | (0x01 << 8) | (sys_mem_ddr_hc_clk_dly(140 * ${DDR_CLK_PER}) << 11));

	/* Set number of host commands */
	DDRCMDISSUEbits.NUMHOSTCMDS = 0x${DDR_NUM_CMDS};
	DDRCMDISSUEbits.VALID = 1;
	DDRMEMCONbits.STINIT = 1;
	while (DDRCMDISSUEbits.VALID);
	DDRMEMCONbits.INITDN = 1;
}

static void DDR_PHY_Init(void)
{
<#if DDR_PHY_ODT_ENABLE == true>
	DDRPHYPADCONbits.ODTSEL = ${DDR_PHY_ODT_VALUE};
	DDRPHYPADCONbits.ODTEN = 1;
<#else>
	DDRPHYPADCONbits.ODTEN = 0;
</#if>

	DDRPHYPADCONbits.DATDRVSEL = ${DDR_PHY_SYS_MEMORY_STRENGTH_DATA};
	DDRPHYPADCONbits.ADDCDRVSEL = ${DDR_PHY_SYS_MEMORY_STRENGTH_ADDC};
	DDRPHYPADCONbits.ODTPUCAL = ${DDR_PHY_ODT_PU_CAL};
	DDRPHYPADCONbits.ODTPDCAL = ${DDR_PHY_ODT_PD_CAL};
	DDRPHYPADCONbits.DRVSTRNFET = ${DDR_PHY_SYS_MEMORY_STR_NFET_CAL};
	DDRPHYPADCONbits.DRVSTRPFET = ${DDR_PHY_SYS_MEMORY_STR_PFET_CAL};
	
	DDRPHYPADCONbits.NOEXTDLL = 1;
	
<#if DDR_PHY_EXTRA_CLK == true>
	DDRPHYPADCONbits.EOENCLKCYC = 1; 
<#else>
	DDRPHYPADCONbits.EOENCLKCYC = 0;
</#if>

<#if DDR_PHY_RCVREN == true>
	DDRPHYPADCONbits.RCVREN = 1;
<#else>
	DDRPHYPADCONbits.RCVREN = 0;
</#if>
	DDRPHYPADCONbits.PREAMBDLY = ${DDR_PHY_PRE_DLY};
	DDRPHYPADCONbits.HALFRATE = 1;
<#if DDR_PHY_WR_CMD_DLY == true>
	DDRPHYPADCONbits.WRCMDDLY = 1;
<#else>
	DDRPHYPADCONbits.WRCMDDLY = 0;
</#if>
<#if DDR_PHY_RECALIB_EN == true>
	DDRPHYDLLRbits.RECALIBCNT = ${DDR_PHY_RECALIB_COUNT};
	DDRPHYDLLRbits.DISRECALIB = 0;
<#else>
	DDRPHYDLLRbits.DISRECALIB = 1;
</#if>
	DDRPHYDLLRbits.DLYSTVAL = ${DDR_PHY_DLL_MASTER_DELAY_START};
	DDRSCLCFG0bits.BURST8 = ${DDR_PHY_SCL_BURST_MODE};
	DDRSCLCFG0bits.DDR2 = !${DDR_PHY_DDR_TYPE};
	DDRSCLCFG0bits.RCASLAT = ${DDR_CAS_LAT};
	DDRSCLCFG1bits.WCASLAT = ${DDR_WR_LAT};

<#if DDR_PHY_ODT_CS_EN == true>
	DDRSCLCFG0bits.ODTCSW = 1;
<#else>
	DDRSCLCFG0bits.ODTCSW = 0;
</#if>
	DDRSCLCFG1bits.DBLREFDLY = ${DDR_PHY_SCL_DLY};
	DDRSCLLATbits.DDRCLKDLY = ${DDR_PHY_SCL_MAIN_CLK_DELAY};
	DDRSCLLATbits.CAPCLKDLY = ${DDR_PHY_SCL_CAP_CLK_DELAY};

<#if DDR_SCL_CS_EN>
	/* Chip select 0 enabled by hardware. Other chip selects not available. */
	/* DDRSCLCFG1bits.SCLCSEN = 0;*/
</#if>
}

static void DDR_PHY_Calib(void)
{
	DDRSCLSTARTbits.SCLEN = 1;
	DDRSCLSTARTbits.SCLSTART = 1;

	while (!((DDRSCLSTARTbits.SCLLBPASS & DDRSCLSTARTbits.SCLUBPASS) == 0x01));
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
