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

#include "device.h"
#include "plib_clk.h"
<#if (CLK_MAINCK_MOSCRCEN && CLK_MAINCK_RC_TRIM_FROM_GPNVM) || (CLK_RC2CK_EN && CLK_RC2_TRIM_FROM_GPNVM)>
#include <stdbool.h>
#include <string.h>
</#if>
<#compress>

<#assign PERIPERAL_INIT = false>

<#list 0..127 as i>
<#if .vars["CLK_ID_NAME_"+i]?has_content>
    <#assign INST_NAME   = .vars["CLK_ID_NAME_"+i]>
    <#if (.vars[INST_NAME+"_GCLK_ENABLE"]?has_content  && .vars[INST_NAME+"_GCLK_ENABLE"]) ||
         (.vars[INST_NAME+"_CLOCK_ENABLE"]?has_content && .vars[INST_NAME+"_CLOCK_ENABLE"])>
        <#assign PERIPERAL_INIT = true>
    </#if>
</#if>
</#list>

<#assign PMC_SCER_PCKX_MSK = "">
<#assign PMC_SCDR_PCKX_MSK = "">
<#assign PMC_SR_PCKRDYX_MSK = "">

<#list 0..3 as i>
<#if .vars["CLK_PCK"+i+"_EN"]>
    <#if PMC_SCER_PCKX_MSK != "">
        <#assign PMC_SCER_PCKX_MSK  = PMC_SCER_PCKX_MSK  + " | " + "PMC_SCER_PCK"  + i + "_Msk">
        <#assign PMC_SCDR_PCKX_MSK  = PMC_SCDR_PCKX_MSK  + " | " + "PMC_SCDR_PCK"  + i + "_Msk">
        <#assign PMC_SR_PCKRDYX_MSK = PMC_SR_PCKRDYX_MSK + " | " + "PMC_SR_PCKRDY" + i + "_Msk">
    <#else>
        <#assign PMC_SCER_PCKX_MSK  = "PMC_SCER_PCK"  + i + "_Msk">
        <#assign PMC_SCDR_PCKX_MSK  = "PMC_SCDR_PCK"  + i + "_Msk">
        <#assign PMC_SR_PCKRDYX_MSK = "PMC_SR_PCKRDY" + i + "_Msk">
    </#if>
</#if>
</#list>

</#compress>

<#if (CLK_MAINCK_MOSCRCEN && CLK_MAINCK_RC_TRIM_FROM_GPNVM) || (CLK_RC2CK_EN && CLK_RC2_TRIM_FROM_GPNVM)>
static volatile uint32_t gpnvm_table[4] = {0};
static bool crc_valid = false;

static bool checkGpnvmWordCrc(void)
{
    uint8_t count = 0U;

    /* Read GPNVM bits */
    HEFC_REGS->HEFC_FCR = (HEFC_FCR_FKEY(0x5AU) | HEFC_FCR_FCMD_GGPB );
    while ( (HEFC_REGS-> HEFC_FSR & HEFC_FSR_FRDY_Msk) != HEFC_FSR_FRDY_Msk)
    {
        /* Waiting for the Flash Ready state */
    }
    for (count = 0U; count < 4U; count++)
    {
        gpnvm_table[count] = HEFC_REGS->HEFC_FRR;
    }

    __DSB();
    __ISB();

    if ( (gpnvm_table[1] == gpnvm_table[2]) && (gpnvm_table[2] == gpnvm_table[3]))
    {
        crc_valid = true;
    }
    return crc_valid;
}
</#if>
<#if (CLK_MAINCK_MOSCRCEN && CLK_MAINCK_RC_TRIM_FROM_GPNVM)>
static void rcTrimCalibrationSequence(void)
{
    // Compute calibration value using ftrim and ttrim from GPNVM_WORD
    uint32_t calibMain4 = ( ((gpnvm_table[1] & FUSES_USER_WORD_1_RC_FTRIM_4MHZ_Msk) >> FUSES_USER_WORD_1_RC_FTRIM_4MHZ_Pos) << 2U ) |\
                          ((gpnvm_table[1] & FUSES_USER_WORD_1_RC_TTRIM_Msk) >> FUSES_USER_WORD_1_RC_TTRIM_Pos) ;
    uint32_t calibMain8 = ( ((gpnvm_table[1] & FUSES_USER_WORD_1_RC_FTRIM_8MHZ_Msk) >> FUSES_USER_WORD_1_RC_FTRIM_8MHZ_Pos) << 2U ) |\
                          ((gpnvm_table[1] & FUSES_USER_WORD_1_RC_TTRIM_Msk) >> FUSES_USER_WORD_1_RC_TTRIM_Pos) ;
    uint32_t calibMain10 = ( ((gpnvm_table[1] & FUSES_USER_WORD_1_RC_FTRIM_10MHZ_Msk) >> FUSES_USER_WORD_1_RC_FTRIM_10MHZ_Pos) << 2U ) |\
                  ((gpnvm_table[1] & FUSES_USER_WORD_1_RC_TTRIM_Msk) >> FUSES_USER_WORD_1_RC_TTRIM_Pos) ;
    uint32_t calibMain12 = ( ((gpnvm_table[1] & FUSES_USER_WORD_1_RC_FTRIM_12MHZ_Msk) >> FUSES_USER_WORD_1_RC_FTRIM_12MHZ_Pos) << 2U ) |\
                  ((gpnvm_table[1] & FUSES_USER_WORD_1_RC_TTRIM_Msk) >> FUSES_USER_WORD_1_RC_TTRIM_Pos) ;

    /* Configure the RC Oscillator frequency to select 4MHz */
    PMC_REGS->CKGR_MOR = (PMC_REGS->CKGR_MOR & ~CKGR_MOR_MOSCRCF_Msk) | CKGR_MOR_KEY_PASSWD | CKGR_MOR_MOSCRCF_4_MHZ;

    /* Wait until the RC oscillator clock is ready */
    while( (PMC_REGS->PMC_SR & PMC_SR_MOSCRCS_Msk) != PMC_SR_MOSCRCS_Msk)
    {
        /* Waiting for the RC oscillator clock is ready */
    }

    __DSB();
    __ISB();

    /* Set SEL for 8/10/12 MHz */
    PMC_REGS->PMC_OCR1 |= (PMC_OCR1_SEL8_Msk | PMC_OCR1_SEL10_Msk | PMC_OCR1_SEL12_Msk);

    /* Set Calib values for 8/10/12 MHz */
    PMC_REGS->PMC_OSC2 = (PMC_REGS->PMC_OSC2 | CKGR_MOR_KEY_PASSWD) | PMC_OSC2_EN_WR_CALIB_Msk;
    PMC_REGS->PMC_OCR1 = (PMC_REGS->PMC_OCR1 & ~(PMC_OCR1_CAL8_Msk | PMC_OCR1_CAL10_Msk | PMC_OCR1_CAL12_Msk) ) | \
                         PMC_OCR1_CAL8(calibMain8) | PMC_OCR1_CAL10(calibMain10) | PMC_OCR1_CAL12(calibMain12);
    PMC_REGS->PMC_OSC2 = (PMC_REGS->PMC_OSC2 | CKGR_MOR_KEY_PASSWD) & (~PMC_OSC2_EN_WR_CALIB_Msk);

    __DSB();
    __ISB();

    /* Configure the RC Oscillator frequency to select 8MHz */
    PMC_REGS->CKGR_MOR = (PMC_REGS->CKGR_MOR & ~CKGR_MOR_MOSCRCF_Msk) | CKGR_MOR_KEY_PASSWD | CKGR_MOR_MOSCRCF_8_MHZ;

    /* Wait until the RC oscillator clock is ready */
    while( (PMC_REGS->PMC_SR & PMC_SR_MOSCRCS_Msk) != PMC_SR_MOSCRCS_Msk)
    {
        /* Waiting for the RC oscillator clock is ready */
    }

    __DSB();
    __ISB();

    /* Set SEL for 4 MHz */
    PMC_REGS->PMC_OCR1 |= PMC_OCR1_SEL4_Msk;

    /* Set Calib values for 4 MHz */
    PMC_REGS->PMC_OSC2 = (PMC_REGS->PMC_OSC2 | CKGR_MOR_KEY_PASSWD) | PMC_OSC2_EN_WR_CALIB_Msk;
    PMC_REGS->PMC_OCR1 = (PMC_REGS->PMC_OCR1 & ~(PMC_OCR1_CAL4_Msk)) | PMC_OCR1_CAL4(calibMain4);
    PMC_REGS->PMC_OSC2 = (PMC_REGS->PMC_OSC2 | CKGR_MOR_KEY_PASSWD) & (~PMC_OSC2_EN_WR_CALIB_Msk);

    __DSB();
    __ISB();
}
</#if>
<#if (CLK_RC2CK_EN && CLK_RC2_TRIM_FROM_GPNVM)>
static void rc2ckTrimCalibrationSequence(void)
{
    // Compute calibration value using ftrim and ttrim from GPNVM_WORD
    uint32_t calibSec4 = ( ((gpnvm_table[1] & FUSES_USER_WORD_1_RC2_FTRIM_4MHZ_Msk) >> FUSES_USER_WORD_1_RC2_FTRIM_4MHZ_Pos) << 2U ) |\
                          ((gpnvm_table[1] & FUSES_USER_WORD_1_RC2_TTRIM_Msk) >> FUSES_USER_WORD_1_RC2_TTRIM_Pos) ;
    uint32_t calibSec8 = ( ((gpnvm_table[1] & FUSES_USER_WORD_1_RC2_FTRIM_8MHZ_Msk) >> FUSES_USER_WORD_1_RC2_FTRIM_8MHZ_Pos) << 2U ) |\
                          ((gpnvm_table[1] & FUSES_USER_WORD_1_RC2_TTRIM_Msk) >> FUSES_USER_WORD_1_RC2_TTRIM_Pos) ;
    uint32_t calibSec10 = ( ((gpnvm_table[1] & FUSES_USER_WORD_1_RC2_FTRIM_10MHZ_Msk) >> FUSES_USER_WORD_1_RC2_FTRIM_10MHZ_Pos) << 2U ) |\
                  ((gpnvm_table[1] & FUSES_USER_WORD_1_RC2_TTRIM_Msk) >> FUSES_USER_WORD_1_RC2_TTRIM_Pos) ;
    uint32_t calibSec12 = ( ((gpnvm_table[1] & FUSES_USER_WORD_1_RC2_FTRIM_12MHZ_Msk) >> FUSES_USER_WORD_1_RC2_FTRIM_12MHZ_Pos) << 2U ) |\
                  ((gpnvm_table[1] & FUSES_USER_WORD_1_RC2_TTRIM_Msk) >> FUSES_USER_WORD_1_RC2_TTRIM_Pos) ;

    /* Configure the RC Oscillator frequency to select 4MHz */
    PMC_REGS->PMC_OSC2 = (PMC_REGS->PMC_OSC2 & ~PMC_OSC2_OSCRCF_Msk) | PMC_OSC2_KEY_PASSWD | PMC_OSC2_OSCRCF_4_MHZ;

    __DSB();
    __ISB();

    /* Set SEL for 8/10/12 MHz */
    PMC_REGS->PMC_OCR2 |= (PMC_OCR2_SEL8_Msk | PMC_OCR2_SEL10_Msk | PMC_OCR2_SEL12_Msk);

    /* Set Calib values for 8/10/12 MHz */
    PMC_REGS->PMC_OSC2 = (PMC_REGS->PMC_OSC2 | CKGR_MOR_KEY_PASSWD) | PMC_OSC2_EN_WR_CALIB_Msk;
    PMC_REGS->PMC_OCR2 = (PMC_REGS->PMC_OCR2 & ~(PMC_OCR2_CAL8_Msk | PMC_OCR2_CAL10_Msk | PMC_OCR2_CAL12_Msk) ) | \
                         PMC_OCR2_CAL8(calibSec8) | PMC_OCR2_CAL10(calibSec10) | PMC_OCR2_CAL12(calibSec12);
    PMC_REGS->PMC_OSC2 = (PMC_REGS->PMC_OSC2 | CKGR_MOR_KEY_PASSWD) & (~PMC_OSC2_EN_WR_CALIB_Msk);

    __DSB();
    __ISB();

    /* Configure the RC Oscillator frequency to select 8MHz */
    PMC_REGS->PMC_OSC2 = (PMC_REGS->PMC_OSC2 & ~PMC_OSC2_OSCRCF_Msk) | PMC_OSC2_KEY_PASSWD | PMC_OSC2_OSCRCF_8_MHZ;

    __DSB();
    __ISB();

    /* Set SEL for 4 MHz */
    PMC_REGS->PMC_OCR2 |= PMC_OCR2_SEL4_Msk;

    /* Set Calib values for 4 MHz */
    PMC_REGS->PMC_OSC2 = (PMC_REGS->PMC_OSC2 | CKGR_MOR_KEY_PASSWD) | PMC_OSC2_EN_WR_CALIB_Msk;
    PMC_REGS->PMC_OCR2 = (PMC_REGS->PMC_OCR2 & ~(PMC_OCR2_CAL4_Msk)) | PMC_OCR2_CAL4(calibSec4);
    PMC_REGS->PMC_OSC2 = (PMC_REGS->PMC_OSC2 | CKGR_MOR_KEY_PASSWD) & (~PMC_OSC2_EN_WR_CALIB_Msk);
}
</#if>
/*********************************************************************************
Initialize Slow Clock (SLCK)
*********************************************************************************/
static void CLK_SlowClockInitialize(void)
{
    <#if CLK_SLCK_OSCBYPASS>
    /* Set bypass mode before selecting xtal select (preserve supply monitor settings)*/
    SUPC_REGS->SUPC_MR = (SUPC_REGS->SUPC_MR & (SUPC_MR_CORSMDIS_Msk | SUPC_MR_CORSMRSTEN_Msk)) | SUPC_MR_KEY_PASSWD | SUPC_MR_OSCBYPASS_BYPASS;
    </#if>
    <#if CLK_SLCK_TDXTALSEL != "0">
    /* Select xtal for TD_SLCK */
    SUPC_REGS->SUPC_CR = SUPC_CR_KEY_PASSWD | SUPC_CR_TDXTALSEL_CRYSTAL_SEL;
    <#else>
    SUPC_REGS->SUPC_CR = SUPC_CR_KEY_PASSWD;
    </#if>
    <#if !CLK_SLCK_OSCBYPASS>
        <#if CLK_SLCK_TDXTALSEL != "0">
    /* Wait for xtal selection to become effective for TD_SLCK */
    while (!(SUPC_REGS->SUPC_SR & SUPC_SR_TDOSCSEL_Msk));
        </#if>
    </#if>
}


/*********************************************************************************
Initialize Main Clock (MAINCK)
*********************************************************************************/
static void CLK_MainClockInitialize(void)
{
<#if CLK_MAINCK_MOSCXTBY>
    /* Disable Main Crystal Oscillator and Enable External Clock Signal on XIN pin  */
    PMC_REGS->CKGR_MOR = (PMC_REGS->CKGR_MOR & ~CKGR_MOR_MOSCXTEN_Msk) | CKGR_MOR_KEY_PASSWD | CKGR_MOR_MOSCXTBY_Msk;

    <#if CLK_MAINCK_MOSCSEL != "0">
     /* External clock signal (XIN pin) is selected as the Main Clock (MAINCK) source.
        Switch Main Clock (MAINCK) to External signal on XIN pin */
    PMC_REGS->CKGR_MOR |= CKGR_MOR_KEY_PASSWD | CKGR_MOR_MOSCSEL_Msk;

    /* Wait until MAINCK is switched to External Clock Signal (XIN pin) */
    while ( (PMC_REGS->PMC_SR & PMC_SR_MOSCSELS_Msk) != PMC_SR_MOSCSELS_Msk);

    </#if>
<#elseif CLK_MAINCK_MOSCXTEN>
    /* Enable Main Crystal Oscillator */
    PMC_REGS->CKGR_MOR = (PMC_REGS->CKGR_MOR & ~CKGR_MOR_MOSCXTST_Msk) | CKGR_MOR_KEY_PASSWD | CKGR_MOR_MOSCXTST(${CLK_MAINCK_MOSCXTST}) | CKGR_MOR_MOSCXTEN_Msk;

    /* Wait until the main oscillator clock is ready */
    while ( (PMC_REGS->PMC_SR & PMC_SR_MOSCXTS_Msk) != PMC_SR_MOSCXTS_Msk);

    <#if CLK_MAINCK_MOSCSEL != "0">
    /* Main Crystal Oscillator is selected as the Main Clock (MAINCK) source.
    Switch Main Clock (MAINCK) to Main Crystal Oscillator clock */
    PMC_REGS->CKGR_MOR |= CKGR_MOR_KEY_PASSWD | CKGR_MOR_MOSCSEL_Msk;

    /* Wait until MAINCK is switched to Main Crystal Oscillator */
    while ( (PMC_REGS->PMC_SR & PMC_SR_MOSCSELS_Msk) != PMC_SR_MOSCSELS_Msk);

    </#if>
</#if>
<#if CLK_MAINCK_MOSCRCEN>
    /* Enable the RC Oscillator */
    PMC_REGS->CKGR_MOR|= CKGR_MOR_KEY_PASSWD | CKGR_MOR_MOSCRCEN_Msk;

    /* Wait until the RC oscillator clock is ready. */
    while( (PMC_REGS->PMC_SR & PMC_SR_MOSCRCS_Msk) != PMC_SR_MOSCRCS_Msk)
    {

    }

<#if CLK_MAINCK_RC_TRIM_FROM_GPNVM>
    if (checkGpnvmWordCrc())
    {
        rcTrimCalibrationSequence();
    }
</#if>
    /* Configure the RC Oscillator frequency */
    PMC_REGS->CKGR_MOR = (PMC_REGS->CKGR_MOR & ~CKGR_MOR_MOSCRCF_Msk) | CKGR_MOR_KEY_PASSWD | CKGR_MOR_MOSCRCF${CLK_MAINCK_MOSCRCF};

    /* Wait until the RC oscillator clock is ready */
    while( (PMC_REGS->PMC_SR & PMC_SR_MOSCRCS_Msk) != PMC_SR_MOSCRCS_Msk)
    {

    }

    <#if CLK_MAINCK_MOSCSEL == "0">
    /* Main RC Oscillator is selected as the Main Clock (MAINCK) source.
       Switch Main Clock (MAINCK) to the RC Oscillator clock */
    PMC_REGS->CKGR_MOR = (PMC_REGS->CKGR_MOR & ~CKGR_MOR_MOSCSEL_Msk) | CKGR_MOR_KEY_PASSWD;

    </#if>
<#else>
    /* Disable the RC Oscillator */
    PMC_REGS->CKGR_MOR = CKGR_MOR_KEY_PASSWD | (PMC_REGS->CKGR_MOR & ~CKGR_MOR_MOSCRCEN_Msk);

</#if>

    while ((PMC_REGS->PMC_SR & PMC_SR_MCKRDY_Msk) != PMC_SR_MCKRDY_Msk)
    {

    }
}


/*********************************************************************************
Initialize RC2 Clock (RC2CK)
*********************************************************************************/
static void CLK_RC2ClockInitialize(void)
{
    <#if CLK_RC2CK_EN>
    PMC_REGS->PMC_OSC2 |= PMC_OSC2_EN_Msk | PMC_OSC2_KEY_PASSWD;
<#if ((CLK_RC2CK_EN && CLK_RC2_TRIM_FROM_GPNVM) && (CLK_MAINCK_MOSCRCEN && CLK_MAINCK_RC_TRIM_FROM_GPNVM))>
    if (crc_valid)
    {
        rc2ckTrimCalibrationSequence();
    }
<#elseif (CLK_RC2CK_EN && CLK_RC2_TRIM_FROM_GPNVM)>
    if (checkGpnvmWordCrc())
    {
        rc2ckTrimCalibrationSequence();
    }
</#if>
    PMC_REGS->PMC_OSC2 = (PMC_REGS->PMC_OSC2 & ~PMC_OSC2_OSCRCF_Msk) | PMC_OSC2_OSCRCF${CLK_RC2CK_OSCRCF} | PMC_OSC2_KEY_PASSWD;
    <#else>
    PMC_REGS->PMC_OSC2 = PMC_OSC2_OSCRCF${CLK_RC2CK_OSCRCF} | PMC_OSC2_KEY_PASSWD;
    </#if>
}

<#if (CLK_PLLACK_DIVA!=0 && CLK_PLLACK_MULA!=0) || (CLK_PLLBCK_DIVB!=0 && CLK_PLLBCK_MULB!=0)>
/*********************************************************************************
Initialize PLLACK/PLLBCK
*********************************************************************************/
static void CLK_PLLxClockInitialize(void)
{
    <#if CLK_PLLBCK_SRB != "SR_VAL_24K" || CLK_PLLBCK_SCB != "SC_VAL_20p" || CLK_PLLBCK_OUTCUR != "ICP0" ||
         CLK_PLLACK_SRA != "SR_VAL_24K" || CLK_PLLACK_SCA != "SC_VAL_20p" || CLK_PLLACK_OUTCUR != "ICP0">
    PMC_REGS->PMC_PLL_CFG = PMC_PLL_CFG_SRB_${CLK_PLLBCK_SRB} |
                            PMC_PLL_CFG_SCB_${CLK_PLLBCK_SCB} |
                            PMC_PLL_CFG_OUTCUR_PLLB_${CLK_PLLBCK_OUTCUR} |
                            PMC_PLL_CFG_SRA_${CLK_PLLACK_SRA} |
                            PMC_PLL_CFG_SCA_${CLK_PLLACK_SCA} |
                            PMC_PLL_CFG_OUTCUR_PLLA_${CLK_PLLACK_OUTCUR};

    </#if>
    <#if CLK_PLLACK_DIVA!=0 && CLK_PLLACK_MULA!=0>
    /* Configure and Enable PLLA */
    PMC_REGS->CKGR_PLLAR =  CKGR_PLLAR_ONE_Msk |
                            CKGR_PLLAR_FREQ_VCO_${CLK_PLLACK_FREQ_VCO} |
                            CKGR_PLLAR_PLLACOUNT(0x3fU) |
                            CKGR_PLLAR_MULA(${CLK_PLLACK_MULA}U) |
                            CKGR_PLLAR_DIVA(${CLK_PLLACK_DIVA}U);

    while ( (PMC_REGS->PMC_SR & PMC_SR_LOCKA_Msk) != PMC_SR_LOCKA_Msk)
    {

    }

    </#if>
    <#if CLK_PLLBCK_DIVB!=0 && CLK_PLLBCK_MULB!=0>
    /* Configure and Enable PLLB */
    PMC_REGS->CKGR_PLLBR =  CKGR_PLLBR_SRCB_${CLK_PLLBCK_SRCB} |
                            CKGR_PLLBR_FREQ_VCO_${CLK_PLLBCK_FREQ_VCO} |
                            CKGR_PLLBR_PLLBCOUNT(0x3f) |
                            CKGR_PLLBR_MULB(${CLK_PLLBCK_MULB}) |
                            CKGR_PLLBR_DIVB(${CLK_PLLBCK_DIVB});

    while ( (PMC_REGS->PMC_SR & PMC_SR_LOCKB_Msk) != PMC_SR_LOCKB_Msk);
    </#if>
}

</#if>
<#if CLK_MCK_CSS != "MAIN_CLK" || CLK_MCK_PRES != "CLK_1" || CLK_MCK_MDIV != "EQ_PCK">
/*********************************************************************************
Initialize Master clock (MCK)
*********************************************************************************/
static void CLK_MasterClockInitialize(void)
{
<#if CLK_MCK_CSS == "PLLA_CLK">
    /* Program PMC_MCKR.PRES and wait for PMC_SR.MCKRDY to be set   */
    PMC_REGS->PMC_MCKR = (PMC_REGS->PMC_MCKR & ~PMC_MCKR_PRES_Msk) | PMC_MCKR_PRES_${CLK_MCK_PRES};
    while ((PMC_REGS->PMC_SR & PMC_SR_MCKRDY_Msk) != PMC_SR_MCKRDY_Msk)
    {

    }

    /* Program PMC_MCKR.MDIV and Wait for PMC_SR.MCKRDY to be set   */
    PMC_REGS->PMC_MCKR = (PMC_REGS->PMC_MCKR & ~PMC_MCKR_MDIV_Msk) | PMC_MCKR_MDIV_${CLK_MCK_MDIV};
    while ((PMC_REGS->PMC_SR & PMC_SR_MCKRDY_Msk) != PMC_SR_MCKRDY_Msk)
    {

    }

    /* Program PMC_MCKR.CSS and Wait for PMC_SR.MCKRDY to be set    */
    PMC_REGS->PMC_MCKR = (PMC_REGS->PMC_MCKR & ~PMC_MCKR_CSS_Msk) | PMC_MCKR_CSS_${CLK_MCK_CSS};
    while ((PMC_REGS->PMC_SR & PMC_SR_MCKRDY_Msk) != PMC_SR_MCKRDY_Msk)
    {

    }

</#if>
<#if CLK_MCK_CSS == "SLOW_CLK" || CLK_MCK_CSS == "MAIN_CLK">
    /* Program PMC_MCKR.CSS and Wait for PMC_SR.MCKRDY to be set    */
    PMC_REGS->PMC_MCKR = (PMC_REGS->PMC_MCKR & ~PMC_MCKR_CSS_Msk) | PMC_MCKR_CSS_${CLK_MCK_CSS};
    while ((PMC_REGS->PMC_SR & PMC_SR_MCKRDY_Msk) != PMC_SR_MCKRDY_Msk);


    /* Program PMC_MCKR.PRES and wait for PMC_SR.MCKRDY to be set   */
    PMC_REGS->PMC_MCKR = (PMC_REGS->PMC_MCKR & ~PMC_MCKR_PRES_Msk) | PMC_MCKR_PRES_${CLK_MCK_PRES};
    while ((PMC_REGS->PMC_SR & PMC_SR_MCKRDY_Msk) != PMC_SR_MCKRDY_Msk);


    /* Program PMC_MCKR.MDIV and Wait for PMC_SR.MCKRDY to be set   */
    PMC_REGS->PMC_MCKR = (PMC_REGS->PMC_MCKR & ~PMC_MCKR_MDIV_Msk) | PMC_MCKR_MDIV_${CLK_MCK_MDIV};
    while ((PMC_REGS->PMC_SR & PMC_SR_MCKRDY_Msk) != PMC_SR_MCKRDY_Msk);

</#if>
}

</#if>
<#if PMC_SCER_PCKX_MSK!="">
/*********************************************************************************
Initialize Programmable Clock (PCKx)
*********************************************************************************/
static void CLK_ProgrammableClockInitialize(void)
{
    /* Disable selected programmable clock  */
    PMC_REGS->PMC_SCDR = ${PMC_SCDR_PCKX_MSK};

    /* Configure selected programmable clock */
<#list 0..3 as i>
<#if .vars["CLK_PCK"+i+"_EN"]>
    <#assign PCK_CSS  = .vars["CLK_PCK"+i+"_CSS"]>
    <#assign PCK_PRES = .vars["CLK_PCK"+i+"_PRES"]>
    PMC_REGS->PMC_PCK[${i}]= PMC_PCK_CSS_${PCK_CSS} | PMC_PCK_PRES(${PCK_PRES});
</#if>
</#list>

    /* Enable selected programmable clock */
    PMC_REGS->PMC_SCER = ${PMC_SCER_PCKX_MSK};

    /* Wait for clock to be ready */
    while( (PMC_REGS->PMC_SR & (${PMC_SR_PCKRDYX_MSK}) ) != (${PMC_SR_PCKRDYX_MSK}));

}

</#if>
<#if PERIPERAL_INIT>
/*********************************************************************************
Initialize Peripheral Clock
*********************************************************************************/
static void CLK_PeripheralClockInitialize(void)
{
<#list 0..127 as i>
<#if .vars["CLK_ID_NAME_"+i]?has_content>
    <#assign INST_NAME   = .vars["CLK_ID_NAME_"+i]>
    <#if .vars[INST_NAME+"_GCLK_ENABLE"]?has_content && .vars[INST_NAME+"_GCLK_ENABLE"]>
        <#assign GCLK_CSS = .vars[INST_NAME+"_GCLK_CSS"]>
        <#assign GCLK_DIV = .vars[INST_NAME+"_GCLK_DIV"]>
    PMC_REGS->PMC_PCR = PMC_PCR_EN_Msk | PMC_PCR_CMD_Msk | PMC_PCR_PID(${i})  /* ${INST_NAME} */
        | PMC_PCR_GCLKEN_Msk | PMC_PCR_GCLKCSS_${GCLK_CSS} | PMC_PCR_GCLKDIV(${GCLK_DIV});
    <#elseif .vars[INST_NAME+"_CLOCK_ENABLE"]?has_content && .vars[INST_NAME+"_CLOCK_ENABLE"]>
    PMC_REGS->PMC_PCR = PMC_PCR_EN_Msk | PMC_PCR_CMD_Msk | PMC_PCR_PID(${i}U); /* ${INST_NAME} */
    </#if>
</#if>
</#list>
}

</#if>
/*********************************************************************************
Clock Initialize
*********************************************************************************/
void CLOCK_Initialize( void )
{
    <#if (DATA_CACHE_ENABLE)>
    SCB_DisableDCache();
    </#if>
    <#if INSTRUCTION_CACHE_ENABLE>
    SCB_DisableICache();
    </#if>

    /* Initialize Slow Clock */
    CLK_SlowClockInitialize();

    /* Initialize Main Clock */
    CLK_MainClockInitialize();

    /* Initialize RC2 */
    CLK_RC2ClockInitialize();

<#if (CLK_PLLACK_DIVA!=0 && CLK_PLLACK_MULA!=0) || (CLK_PLLBCK_DIVB!=0 && CLK_PLLBCK_MULB!=0)>
    /* Initialize PLLA/PLLB */
    CLK_PLLxClockInitialize();

</#if>
<#if CLK_MCK_CSS != "MAIN_CLK" || CLK_MCK_PRES != "CLK_1" || CLK_MCK_MDIV != "EQ_PCK">
    /* Initialize Master Clock */
    CLK_MasterClockInitialize();

</#if>
<#if PMC_SCER_PCKX_MSK!="">
    /* Initialize Programmable Clock */
    CLK_ProgrammableClockInitialize();

</#if>
<#if PERIPERAL_INIT>
    /* Initialize Peripheral Clock */
    CLK_PeripheralClockInitialize();

</#if>

    <#if (DATA_CACHE_ENABLE)>
    SCB_EnableDCache();
    </#if>
    <#if INSTRUCTION_CACHE_ENABLE>
    SCB_EnableICache();
    </#if>
}
<#--
/*******************************************************************************
 End of File
*/
-->
