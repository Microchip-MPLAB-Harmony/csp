/*******************************************************************************
* Copyright (C) 2022 Microchip Technology Inc. and its subsidiaries.
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
#include <stdbool.h>
#include "plib_clk.h"
<#if CPU_CORE_ID == 0>
#include "peripheral/rstc/plib_rstc.h"

#define PLLA_RECOMMENDED_ACR    0x0F020038U
#define PLLB_RECOMMENDED_ACR    0x28020038U
#define PLLC_RECOMMENDED_ACR    0x28020038U

#define PLLA_UPDT_STUPTIM_VAL   0x02U
#define PLLB_UPDT_STUPTIM_VAL   0x00U
#define PLLC_UPDT_STUPTIM_VAL   0x00U

typedef struct pmc_pll_cfg_tag
{
    uint32_t ctrl0;
    uint32_t ctrl1;
    uint32_t ctrl2;
    uint32_t ssr;
    uint32_t acr;
    uint32_t stuptim;
}pmc_pll_cfg_t;

<#assign PLL_LIST = ["PLLA", "PLLB", "PLLC"]>
<#assign PLL_USED = false>
<#list PLL_LIST as PLL_NAME>
<#assign ENPLL = .vars["CLK_" + PLL_NAME + "_ENPLL"]>
<#assign PLLMS = .vars["CLK_" + PLL_NAME + "_PLLMS"]>
<#assign MUL = .vars["CLK_" + PLL_NAME + "_MUL"]>
<#assign FRACR = .vars["CLK_" + PLL_NAME + "_FRACR"]>
<#assign ENPLLO0 = .vars["CLK_" + PLL_NAME + "_ENPLLO0"]>
<#assign DIVPMCO0 = .vars["CLK_" + PLL_NAME + "_DIVPMC0"]>
<#if .vars["CLK_" + PLL_NAME + "_ENPLLO1"]??>
<#assign ENPLLO1 = .vars["CLK_" + PLL_NAME + "_ENPLLO1"]>
<#assign DIVPMCO1 = .vars["CLK_" + PLL_NAME + "_DIVPMC1"]>
<#else>
<#assign ENPLLO1 = false>
<#assign DIVPMCO1 = "">
</#if>
<#assign ENSPREAD = .vars["CLK_" + PLL_NAME + "_ENSPREAD"]>
<#assign SS_STEP = .vars["CLK_" + PLL_NAME + "_STEP"]>
<#assign SS_NSTEP = .vars["CLK_" + PLL_NAME + "_NSTEP"]>

<#if ENPLL>
<#assign PLL_USED = true>

static const pmc_pll_cfg_t ${PLL_NAME?lower_case}_cfg = {
    .ctrl0   = (PMC_PLL_CTRL0_ENLOCK_Msk | PMC_PLL_CTRL0_ENPLL_Msk | PMC_PLL_CTRL0_PLLMS(${PLLMS}U)
               ${ENPLLO1?string("| PMC_PLL_CTRL0_ENPLLO1_Msk | PMC_PLL_CTRL0_DIVPMC1(" + DIVPMCO1 +"U)", "")}${ENPLLO0?string("| PMC_PLL_CTRL0_ENPLLO0_Msk | PMC_PLL_CTRL0_DIVPMC0(" + DIVPMCO0 +"U)", "")}),
    .ctrl1   = PMC_PLL_CTRL1_MUL(${MUL}U),
    .ctrl2   = PMC_PLL_CTRL2_FRACR(${FRACR}U),
    .ssr     = ${ENSPREAD?string("PMC_PLL_SSR_ENSPREAD_Msk | PMC_PLL_SSR_STEP(" + SS_STEP +"U) | PMC_PLL_SSR_NSTEP(" + SS_NSTEP + "U)", "0U")},
    .acr     = ${PLL_NAME}_RECOMMENDED_ACR,
    .stuptim = ${PLL_NAME}_UPDT_STUPTIM_VAL
};


</#if>
</#list>

<#if PLL_USED>
<#if ALLOW_CLK_CONFIG?? &&  ALLOW_CLK_CONFIG>
const static uint32_t PLL_RECOMMENDED_ACR[]  = {PLLA_RECOMMENDED_ACR, PLLB_RECOMMENDED_ACR, PLLC_RECOMMENDED_ACR};
const static uint8_t PLL_UPDT_STUPTIM_VAL[] = {PLLA_UPDT_STUPTIM_VAL, PLLB_UPDT_STUPTIM_VAL, PLLC_UPDT_STUPTIM_VAL};
</#if>
static bool spreadRestoreStatus[3] = {false, false, false};
</#if>

<#if CLK_TDXTALSEL == "XTAL">
/*********************************************************************************
                            Initialize Slow Clock (SLCK)
*********************************************************************************/
static void SlowClockInitialize(void)
{
<#if CLK_OSCBYPASS>
    /* External clock signal on XIN32 pin is selected as the Slow Clock (SLCK) source.
       Bypass 32K Crystal Oscillator  */
    SUPC_REGS->SUPC_MR |= SUPC_MR_KEY_PASSWD | SUPC_MR_OSCBYPASS_BYPASS;
<#else>
    /* 32KHz Crystal Oscillator is selected as the Slow Clock (SLCK) source.
       Enable 32KHz Crystal Oscillator  */
</#if>
    SUPC_REGS->SUPC_CR |= SUPC_CR_KEY_PASSWD | SUPC_CR_TDXTALSEL_XTAL;

    /* Wait until Slow Clock (SLCK) is switched from RC */
    while ((SUPC_REGS->SUPC_SR & SUPC_SR_TDOSCSEL_XTAL) == 0U)
    {
        /* Wait for status to set */
    }
}
</#if>

void CLK_TDSCLKSelectXTAL(void)
{
    /* 32KHz Crystal Oscillator is selected as the Slow Clock (SLCK) source.
    Enable 32KHz Crystal Oscillator  */

    SUPC_REGS->SUPC_CR |= SUPC_CR_KEY_PASSWD | SUPC_CR_TDXTALSEL_XTAL;

    /* Wait until Slow Clock (SLCK) is switched from RC */
    while ((SUPC_REGS->SUPC_SR & SUPC_SR_TDOSCSEL_XTAL) == 0U)
    {
        /* Wait for status to set */
    }
}


<#if (CLK_MOSCXTBY || CLK_MOSCXTEN)>
/*********************************************************************************
                            Initialize Main Clock (MAINCK)
*********************************************************************************/
static void MainClockInitialize(void)
{
<#if CLK_MOSCXTBY>
    /* Disable Main Crystal Oscillator and Enable External Clock Signal on XIN pin  */
    PMC_REGS->CKGR_MOR = (PMC_REGS->CKGR_MOR & ~CKGR_MOR_MOSCXTEN_Msk) | CKGR_MOR_KEY_PASSWD | CKGR_MOR_MOSCXTBY_Msk;
</#if>
<#if CLK_MOSCXTEN>
    /* Enable Main Crystal Oscillator */
    PMC_REGS->CKGR_MOR = (PMC_REGS->CKGR_MOR & ~CKGR_MOR_MOSCXTST_Msk) | CKGR_MOR_KEY_PASSWD | CKGR_MOR_MOSCXTST(${CLK_MOSCXTST}U) | CKGR_MOR_MOSCXTEN_Msk;

    while ((PMC_REGS->PMC_SR & PMC_SR_MOSCXTS_Msk) == 0U)
    {
        /* Wait until the main oscillator clock is ready */
    }
</#if>
<#if CLK_MOSCSEL == "XT">
    /* Main Crystal Oscillator is selected as the Main Clock (MAINCK) source.
    Switch Main Clock (MAINCK) to Main Crystal Oscillator clock */
    PMC_REGS->CKGR_MOR|= CKGR_MOR_KEY_PASSWD | CKGR_MOR_MOSCSEL_Msk;
    while ((PMC_REGS->PMC_SR & PMC_SR_MOSCSELS_Msk) != PMC_SR_MOSCSELS_Msk)
    {
        /* Wait until MAINCK is switched to Main Crystal Oscillator */
    }
</#if>
}


</#if>

void CLK_EnableMainRCOscillator(void)
{
    /* Enable the RC Oscillator */
    PMC_REGS->CKGR_MOR = PMC_REGS->CKGR_MOR | (CKGR_MOR_KEY_PASSWD | CKGR_MOR_MOSCRCEN_Msk);

    while ((PMC_REGS->PMC_SR & PMC_SR_MOSCRCS_Msk) != PMC_SR_MOSCRCS_Msk)
    {
        /* Wait for the RC Oscillator to stabilize */
    }
}

void CLK_DisableMainRCOscillator(void)
{
    /* Disable the RC Oscillator */
    PMC_REGS->CKGR_MOR = CKGR_MOR_KEY_PASSWD | (PMC_REGS->CKGR_MOR & ~CKGR_MOR_MOSCRCEN_Msk);
}

void CLK_EnableMainXTALOscillator(void)
{
    /* Enable Main Crystal Oscillator */
    PMC_REGS->CKGR_MOR = (PMC_REGS->CKGR_MOR & ~CKGR_MOR_MOSCXTST_Msk) | CKGR_MOR_KEY_PASSWD | CKGR_MOR_MOSCXTST(${CLK_MOSCXTST}U) | CKGR_MOR_MOSCXTEN_Msk;

    while ((PMC_REGS->PMC_SR & PMC_SR_MOSCXTS_Msk) == 0U)
    {
        /* Wait until the main oscillator clock is ready */
    }
}

void CLK_DisableMainXTALOscillator(void)
{
    /* Disable the XTAL Oscillator */
    PMC_REGS->CKGR_MOR = CKGR_MOR_KEY_PASSWD | (PMC_REGS->CKGR_MOR & ~CKGR_MOR_MOSCXTEN_Msk);
}

void CLK_MainOscillatorSelectXTAL(void)
{
    /* Main Crystal Oscillator is selected as the Main Clock (MAINCK) source.
    Switch Main Clock (MAINCK) to Main Crystal Oscillator clock */

    PMC_REGS->CKGR_MOR = (PMC_REGS->CKGR_MOR | CKGR_MOR_MOSCSEL_Msk) | CKGR_MOR_KEY_PASSWD;
    while ((PMC_REGS->PMC_SR & PMC_SR_MOSCSELS_Msk) != PMC_SR_MOSCSELS_Msk)
    {
        /* Wait until MAINCK is switched to Main Crystal Oscillator */
    }
}

void CLK_MainOscillatorSelectRC(void)
{
    /* RC Oscillator is selected as the Main Clock (MAINCK) source.
    Switch Main Clock (MAINCK) to RC Oscillator clock */

    PMC_REGS->CKGR_MOR = (PMC_REGS->CKGR_MOR & ~CKGR_MOR_MOSCSEL_Msk) | CKGR_MOR_KEY_PASSWD;
    while ((PMC_REGS->PMC_SR & PMC_SR_MOSCSELS_Msk) != PMC_SR_MOSCSELS_Msk)
    {
        /* Wait until MAINCK is switched to RC Oscillator */
    }
}

<#if PLL_USED>
static void spreadDisable(PLL_ID pllID)
{
    uint32_t nstep = 0;
    bool isSpreadEn = false;

    PMC_REGS->PMC_PLL_UPDT |= (PMC_REGS->PMC_PLL_UPDT & ~(PMC_PLL_UPDT_UPDATE_Msk | PMC_PLL_UPDT_ID_Msk)) | PMC_PLL_UPDT_ID(pllID);

    /* Disable spread if enabled */
    if ((PMC_REGS->PMC_PLL_SSR & PMC_PLL_SSR_ENSPREAD_Msk) != 0U)
    {
        PMC_REGS->PMC_PLL_SSR &= ~PMC_PLL_SSR_ENSPREAD_Msk;

        /* Wait for 2 x NSTEP cycles of the source clock of the PLL */
        nstep = (PMC_REGS->PMC_PLL_SSR & PMC_PLL_SSR_NSTEP_Msk) >> PMC_PLL_SSR_NSTEP_Pos;

        if ((PMC_REGS->PMC_PLL_CTRL0 & PMC_PLL_CTRL0_PLLMS_Msk) != 0U)
        {
            nstep *= 7U;
        }
        else
        {
            nstep *= 2500U;
        }

        for (uint32_t i = 0; i < nstep; i++)
        {
            asm("nop");asm("nop");asm("nop");asm("nop");asm("nop");
        }

        isSpreadEn = true;
    }

    spreadRestoreStatus[pllID] = isSpreadEn;
}

static void spreadRestore(PLL_ID pllID)
{
    if (spreadRestoreStatus[pllID] == true)
    {
        PMC_REGS->PMC_PLL_UPDT |= (PMC_REGS->PMC_PLL_UPDT & ~(PMC_PLL_UPDT_UPDATE_Msk | PMC_PLL_UPDT_ID_Msk)) | PMC_PLL_UPDT_ID(pllID);
        PMC_REGS->PMC_PLL_SSR |= PMC_PLL_SSR_ENSPREAD_Msk;
    }
}

/*********************************************************************************
                                    Initialize PLL
*********************************************************************************/
static void PLLInitialize(uint32_t pll_id, const pmc_pll_cfg_t *pll_cfg)
{
    /* STEP 1: Define the ID and startup time by configuring the fields
    PMC_PLL_UPDT.ID and PMC_PLL_UPDT.STUPTIM. Set PMC_PLL_UPDT.UPDATE to 0 */
    uint32_t reg = PMC_REGS->PMC_PLL_UPDT & ~(PMC_PLL_UPDT_Msk);
    reg |= (PMC_PLL_UPDT_ID(pll_id)  | PMC_PLL_UPDT_STUPTIM(pll_cfg->stuptim));
    PMC_REGS->PMC_PLL_UPDT = reg;

    /* STEP 2: Configure PMC_PLL_ACR.LOOP_FILTER */
    PMC_REGS->PMC_PLL_ACR = pll_cfg->acr;

    /* STEP 3: Define the MUL and FRACR to be applied to PLL(n) in PMC_PLL_CTRL1 */
    PMC_REGS->PMC_PLL_CTRL1 = pll_cfg->ctrl1;
    PMC_REGS->PMC_PLL_CTRL2 = pll_cfg->ctrl2;

    /* STEP 4: Set PMC_PLL_UPDT.UPDATE to 1 */
    PMC_REGS->PMC_PLL_UPDT |= PMC_PLL_UPDT_UPDATE_Msk;

    /* STEP 5: In PMC_PLL_CTRL0, Enable PLL and configure outputs and dividers*/
    reg = PMC_REGS->PMC_PLL_CTRL0 & ~(PMC_PLL_CTRL0_Msk);
    reg |= pll_cfg->ctrl0;
    PMC_REGS->PMC_PLL_CTRL0 = reg;

    /* STEP 6: Set PMC_PLL_UPDT.UPDATE to 1 */
    PMC_REGS->PMC_PLL_UPDT |= PMC_PLL_UPDT_UPDATE_Msk;

    /* STEP 7: Wait for PLL initialization */
    while ((PMC_REGS->PMC_PLL_ISR0 & (1UL << (uint32_t)pll_id)) == 0U)
    {
        /* Wait for PLL lock to rise */
    }

    /* STEP 8: Setup spread spectrum, if enabled */
    if(pll_cfg->ssr != 0U)
    {
        reg = PMC_REGS->PMC_PLL_SSR & ~(PMC_PLL_SSR_Msk);
        reg |= pll_cfg->ssr;
        PMC_REGS->PMC_PLL_SSR = reg;
        if ((PMC_REGS->PMC_PLL_SSR & PMC_PLL_SSR_ENSPREAD_Msk) != 0U)
        {
            spreadRestoreStatus[pll_id] = true;
        }
    }
}

void CLK_PLLEnable(PLL_ID pllID)
{
    PMC_REGS->PMC_PLL_UPDT |= (PMC_REGS->PMC_PLL_UPDT & ~(PMC_PLL_UPDT_UPDATE_Msk | PMC_PLL_UPDT_ID_Msk)) | PMC_PLL_UPDT_ID(pllID);

    if (pllID == 0)
    {
        PMC_REGS->PMC_PLL_CTRL0 |= (PMC_PLL_CTRL0_ENPLL_Msk | PMC_PLL_CTRL0_ENPLLO0_Msk | PMC_PLL_CTRL0_ENPLLO1_Msk);
    }
    else
    {
        PMC_REGS->PMC_PLL_CTRL0 |= (PMC_PLL_CTRL0_ENPLL_Msk | PMC_PLL_CTRL0_ENPLLO0_Msk);
    }

    PMC_REGS->PMC_PLL_UPDT |= PMC_PLL_UPDT_UPDATE_Msk;

    while ((PMC_REGS->PMC_PLL_ISR0 & (1UL << (uint32_t)pllID)) == 0U)
    {
        /* Wait for PLL lock to rise */
    }

    spreadRestore(pllID);
}

void CLK_PLLDisable(PLL_ID pllID)
{
    PMC_REGS->PMC_PLL_UPDT |= (PMC_REGS->PMC_PLL_UPDT & ~(PMC_PLL_UPDT_UPDATE_Msk | PMC_PLL_UPDT_ID_Msk)) | PMC_PLL_UPDT_ID(pllID);

    spreadDisable(pllID);

    if (pllID == 0)
    {
        PMC_REGS->PMC_PLL_CTRL0 = PMC_REGS->PMC_PLL_CTRL0 & ~(PMC_PLL_CTRL0_ENPLLO0_Msk | PMC_PLL_CTRL0_ENPLLO1_Msk);
    }
    else
    {
        PMC_REGS->PMC_PLL_CTRL0 = PMC_REGS->PMC_PLL_CTRL0 & ~PMC_PLL_CTRL0_ENPLLO0_Msk;
    }

    PMC_REGS->PMC_PLL_UPDT |= PMC_PLL_UPDT_UPDATE_Msk;

    PMC_REGS->PMC_PLL_CTRL0 &= ~PMC_PLL_CTRL0_ENPLL_Msk;
}

<#if ALLOW_CLK_CONFIG?? &&  ALLOW_CLK_CONFIG>
void CLK_PLLConfig(PLL_ID pllID, uint8_t clkSrc, uint32_t mul, uint32_t fracr, uint8_t output0Div, uint8_t output1Div)
{
    uint32_t ctrl0;
    pmc_pll_cfg_t pllCfg;

    ctrl0 = PMC_REGS->PMC_PLL_CTRL0 & PMC_PLL_CTRL0_ENPLLO0_Msk;
    ctrl0 |= PMC_PLL_CTRL0_ENLOCK_Msk | PMC_PLL_CTRL0_ENPLL_Msk  | PMC_PLL_CTRL0_PLLMS(clkSrc) | PMC_PLL_CTRL0_DIVPMC0(output0Div);

    if (pllID == PLLA)
    {
        ctrl0 |= PMC_REGS->PMC_PLL_CTRL0 & PMC_PLL_CTRL0_ENPLLO1_Msk;
        ctrl0 |= PMC_PLL_CTRL0_DIVPMC1(output1Div);
    }

    pllCfg.ctrl0 = ctrl0;
    pllCfg.ctrl1 = PMC_PLL_CTRL1_MUL(mul);
    pllCfg.ctrl2 = PMC_PLL_CTRL2_FRACR(fracr);
    pllCfg.acr = PLL_RECOMMENDED_ACR[pllID];
    pllCfg.stuptim = PLL_UPDT_STUPTIM_VAL[pllID];
    pllCfg.ssr = 0;

    spreadDisable(pllID);

    PLLInitialize(pllID, &pllCfg);

    spreadRestore(pllID);

}
</#if>
</#if>

<#compress>
<#assign GEN_CPU_CLK = !((CLK_CPU_CKR_CSS == "MAINCK")  && ( CLK_CPU_CKR_PRES != "CLK_1"))>
<#assign GEN_CPU_CLK = GEN_CPU_CLK || CLK_CPU_CKR_RATIO_MCK0DIV || CLK_CPU_CKR_RATIO_MCK0DIV2 || CLK_CPU_CKR_CPBMCK>
</#compress>
<#if GEN_CPU_CLK>
/*********************************************************************************
                                Initialize CPU clock
*********************************************************************************/
static void CPUClockInitialize(void)
{
<#if CLK_CPU_CKR_CSS == "PLLACK1" || CLK_CPU_CKR_CSS == "PLLBCK">
    /* Program PMC_CPU_CKR.PRES and wait for PMC_SR.MCKRDY to be set   */
    uint32_t reg = (PMC_REGS->PMC_CPU_CKR & ~PMC_CPU_CKR_PRES_Msk);
    PMC_REGS->PMC_CPU_CKR = (reg | PMC_CPU_CKR_PRES_${CLK_CPU_CKR_PRES});
    while ((PMC_REGS->PMC_SR & PMC_SR_MCKRDY_Msk) != PMC_SR_MCKRDY_Msk)
    {
        /* Wait for status MCKRDY */
    }

    /* Program PMC_CPU_CKR.CSS and MCK dividers and Wait for PMC_SR.MCKRDY to be set    */
    reg = (PMC_REGS->PMC_CPU_CKR & ~(PMC_CPU_CKR_CSS_Msk |
                                     PMC_CPU_CKR_RATIO_MCK0DIV_Msk |
                                     PMC_CPU_CKR_RATIO_MCK0DIV2_Msk));
    <@compress single_line=true>reg |= (PMC_CPU_CKR_CSS_${CLK_CPU_CKR_CSS}
        ${CLK_CPU_CKR_RATIO_MCK0DIV?string(" | PMC_CPU_CKR_RATIO_MCK0DIV_Msk","")}
        ${CLK_CPU_CKR_RATIO_MCK0DIV2?string(" | PMC_CPU_CKR_RATIO_MCK0DIV2_Msk", "")});</@compress>
    PMC_REGS->PMC_CPU_CKR = reg;
    while ((PMC_REGS->PMC_SR & PMC_SR_MCKRDY_Msk) != PMC_SR_MCKRDY_Msk)
    {
        /* Wait for status MCKRDY */
    }

</#if>
<#if CLK_CPU_CKR_CSS == "MD_SLOW_CLK" || CLK_CPU_CKR_CSS == "MAINCK">
    /* Program PMC_CPU_CKR.CSS and Wait for PMC_SR.MCKRDY to be set    */
    uint32_t reg = (PMC_REGS->PMC_CPU_CKR & ~PMC_CPU_CKR_CSS_Msk);
    PMC_REGS->PMC_CPU_CKR = (reg | PMC_CPU_CKR_CSS_${CLK_CPU_CKR_CSS});
    while ((PMC_REGS->PMC_SR & PMC_SR_MCKRDY_Msk) != PMC_SR_MCKRDY_Msk)
    {
        /* Wait for status MCKRDY */
    }

    /* Program PMC_CPU_CKR.PRES and wait for PMC_SR.MCKRDY to be set   */
    reg = (PMC_REGS->PMC_CPU_CKR & ~(PMC_CPU_CKR_PRES_Msk |
                                     PMC_CPU_CKR_RATIO_MCK0DIV_Msk |
                                     PMC_CPU_CKR_RATIO_MCK0DIV2_Msk));
    <@compress single_line=true>reg |= (PMC_CPU_CKR_PRES_${CLK_CPU_CKR_PRES}
        ${CLK_CPU_CKR_RATIO_MCK0DIV?string(" | PMC_CPU_CKR_RATIO_MCK0DIV_Msk","")}
        ${CLK_CPU_CKR_RATIO_MCK0DIV2?string(" | PMC_CPU_CKR_RATIO_MCK0DIV2_Msk", "")});</@compress>
    PMC_REGS->PMC_CPU_CKR = reg;
    while ((PMC_REGS->PMC_SR & PMC_SR_MCKRDY_Msk) != PMC_SR_MCKRDY_Msk)
    {
        /* Wait for status MCKRDY */
    }

</#if>
<#if CLK_SCER_CPBMCK>
<#assign DUMMY_CPPRES = "CLK_2">
<#if CLK_CPU_CKR_CPPRES == DUMMY_CPPRES>
<#assign DUMMY_CPPRES = "CLK_3">
</#if>
    /* Set coprocessor clock dummy prescaler */
    reg = (PMC_REGS->PMC_CPU_CKR & ~(PMC_CPU_CKR_CPPRES_Msk | PMC_CPU_CKR_RATIO_MCK1DIV_Msk));
    reg |= (PMC_CPU_CKR_CPPRES_${DUMMY_CPPRES} | PMC_CPU_CKR_RATIO_MCK1DIV_Msk);
    PMC_REGS->PMC_CPU_CKR = reg;

    /* Program PMC_CPU_CKR.CPCSS and Wait for PMC_SR.CPMCKRDY to be set    */
    reg = (PMC_REGS->PMC_CPU_CKR & ~PMC_CPU_CKR_CPCSS_Msk);
    PMC_REGS->PMC_CPU_CKR = (reg | PMC_CPU_CKR_CPCSS_${CLK_CPU_CKR_CPCSS});
    while ((PMC_REGS->PMC_SR & PMC_SR_CPMCKRDY_Msk) != PMC_SR_CPMCKRDY_Msk)
    {
        /* Wait for status CPMCKRDY */
    }

    /* Program PMC_CPU_CKR.CPPRES and wait for PMC_SR.CPMCKRDY to be set   */
    reg = (PMC_REGS->PMC_CPU_CKR & ~(PMC_CPU_CKR_CPPRES_Msk | PMC_CPU_CKR_RATIO_MCK1DIV_Msk));
    <@compress single_line=true>reg |= (PMC_CPU_CKR_CPPRES_${CLK_CPU_CKR_CPPRES}
        ${CLK_CPU_CKR_RATIO_MCK1DIV?string(" | PMC_CPU_CKR_RATIO_MCK1DIV_Msk", "")});</@compress>
    PMC_REGS->PMC_CPU_CKR = reg;
    while ((PMC_REGS->PMC_SR & PMC_SR_CPMCKRDY_Msk) != PMC_SR_CPMCKRDY_Msk)
    {
        /* Wait for status CPMCKRDY */
    }

    /* Enable co-processor bus clock <#if CLK_SCER_CPCK??>${CLK_SCER_CPCK?string(" and co-processor clock", "")}</#if> */
    PMC_REGS->PMC_SCER = (PMC_SCER_CPKEY_PASSWD | PMC_SCER_CPBMCK_Msk<#if CLK_SCER_CPCK?? && CLK_SCER_CPCK == true> | PMC_SCER_CPCK_Msk</#if>);
</#if><#-- CLK_SCER_CPBMCK -->
}


</#if><#-- GEN_CPU_CLK -->

<#if ALLOW_CLK_CONFIG?? &&  ALLOW_CLK_CONFIG>
void CLK_Core0ClkConfig(CPU0_CLK_SRC clkSrc, CPU0_CLK_PRESCALER prescaler, bool mck0DivBy2, bool mck0Div2By2)
{
    PMC_REGS->PMC_CPU_CKR = (PMC_REGS->PMC_CPU_CKR & ~PMC_CPU_CKR_CSS_Msk) | PMC_CPU_CKR_CSS(clkSrc);

    while ((PMC_REGS->PMC_SR & PMC_SR_MCKRDY_Msk) != PMC_SR_MCKRDY_Msk)
    {
        /* Wait for status MCKRDY */
    }

    PMC_REGS->PMC_CPU_CKR = (PMC_REGS->PMC_CPU_CKR & ~(PMC_CPU_CKR_PRES_Msk | PMC_CPU_CKR_RATIO_MCK0DIV_Msk | PMC_CPU_CKR_RATIO_MCK0DIV2_Msk)) | PMC_CPU_CKR_PRES(prescaler) | PMC_CPU_CKR_RATIO_MCK0DIV(mck0DivBy2) | PMC_CPU_CKR_RATIO_MCK0DIV2(mck0Div2By2);

    while ((PMC_REGS->PMC_SR & PMC_SR_MCKRDY_Msk) != PMC_SR_MCKRDY_Msk)
    {
        /* Wait for status MCKRDY */
    }
}
</#if>

void CLK_Core1BusMasterClkEnable(void)
{
    PMC_REGS->PMC_SCER = (PMC_SCER_CPKEY_PASSWD | PMC_SCER_CPBMCK_Msk);

    while ((PMC_REGS->PMC_SR & PMC_SR_CPMCKRDY_Msk) != PMC_SR_CPMCKRDY_Msk)
    {
        /* Wait for status CPMCKRDY */
    }
}

void CLK_Core1BusMasterClkDisable(void)
{
    PMC_REGS->PMC_SCDR = (PMC_SCDR_CPKEY_PASSWD | PMC_SCDR_CPBMCK_Msk);
}

<#if CLK_SCER_CPCK??>
<#if ALLOW_CLK_CONFIG?? &&  ALLOW_CLK_CONFIG>
void CLK_Core1ClkConfig(CPU1_CLK_SRC clkSrc, CPU1_CLK_PRESCALER prescaler, bool mck1DivBy2 )
{
    PMC_REGS->PMC_CPU_CKR = (PMC_REGS->PMC_CPU_CKR & ~PMC_CPU_CKR_CPCSS_Msk) | PMC_CPU_CKR_CPCSS(clkSrc);

    while ((PMC_REGS->PMC_SR & PMC_SR_CPMCKRDY_Msk) != PMC_SR_CPMCKRDY_Msk)
    {
        /* Wait for status CPMCKRDY */
    }

    PMC_REGS->PMC_CPU_CKR = (PMC_REGS->PMC_CPU_CKR & ~(PMC_CPU_CKR_CPPRES_Msk | PMC_CPU_CKR_RATIO_MCK1DIV_Msk)) | PMC_CPU_CKR_CPPRES(prescaler) | PMC_CPU_CKR_RATIO_MCK1DIV(mck1DivBy2);

    while ((PMC_REGS->PMC_SR & PMC_SR_CPMCKRDY_Msk) != PMC_SR_CPMCKRDY_Msk)
    {
        /* Wait for status CPMCKRDY */
    }
}
</#if>

void CLK_Core1ProcessorClkEnable(void)
{
    PMC_REGS->PMC_SCER = (PMC_SCER_CPKEY_PASSWD | PMC_SCER_CPCK_Msk);
}

void CLK_Core1ProcessorClkDisable(void)
{
    PMC_REGS->PMC_SCDR = (PMC_SCDR_CPKEY_PASSWD | PMC_SCDR_CPCK_Msk);
}
</#if>

/*********************************************************************************
                    Enable/Disable flash patch based on core frequency
*********************************************************************************/
static void CLK_ApplyFlashPatch(uint32_t cpuCLKFreq)
{
    SFR_REGS->SFR_WPMR = SFR_WPMR_WPKEY_PASSWD;

    if (cpuCLKFreq >= 160000000U)
    {
        /*Enable Flash high speed patch */
        SFR_REGS->SFR_FLASH = 0x0U;
    }
    else
    {
        /*Disable Flash high speed patch */;
        SFR_REGS->SFR_FLASH = SFR_FLASH_Msk;
    }

    SFR_REGS->SFR_WPMR = (SFR_WPMR_WPKEY_PASSWD | SFR_WPMR_WPEN_Msk);
}


</#if><#-- CPU_CORE_ID -->
<#compress>
<#assign PCK_USED = false>
<#list 0..CLK_NUM_PCKS-1 as i>
<#if .vars["CLK_SCER_PCK"+i]>
<#assign PCK_USED = true>
</#if>
</#list>
</#compress>
<#if PCK_USED>
/*********************************************************************************
                        Initialize Programmable clocks
*********************************************************************************/
static void PCKInitialize(void)
{
    /* Turn off all PCK clocks */
    PMC_REGS->PMC_SCDR = PMC_SCDR_PCK0_Msk | PMC_SCDR_PCK1_Msk | PMC_SCDR_PCK2_Msk;
<#list 0..CLK_NUM_PCKS-1 as i>
<#if .vars["CLK_SCER_PCK"+i]>
<#assign css = .vars["CLK_PCK"+i+"_CSS"]>
<#assign pres = .vars["CLK_PCK"+i+"_PRES"]>
    /* Enable PCK${i} */
    PMC_REGS->PMC_PCK[${i}] = PMC_PCK_CSS_${css} | PMC_PCK_PRES(${pres});
    while ((PMC_REGS->PMC_SR & PMC_SR_PCKRDY${i}_Msk) != PMC_SR_PCKRDY${i}_Msk)
    {
        /* Wait for PCK${i} to be ready */
    }
    PMC_REGS->PMC_SCER = PMC_SCDR_PCK${i}_Msk;
</#if>
</#list>
}

void CLK_PCKConfig(uint8_t pckID, PCK_CLK_SRC clkSrc, uint8_t prescaler)
{
    /* Turn off the PCK clock output */
    PMC_REGS->PMC_SCDR = (PMC_SCDR_PCK0_Msk << pckID);

    PMC_REGS->PMC_PCK[pckID] = PMC_PCK_CSS(clkSrc) | PMC_PCK_PRES(prescaler);

    while ((PMC_REGS->PMC_SR & (PMC_SR_PCKRDY0_Msk << pckID)) != (PMC_SR_PCKRDY0_Msk << pckID))
    {
        /* Wait for PCKx to be ready */
    }

    /* Turn on the PCK clock output */
    PMC_REGS->PMC_SCER = (PMC_SCER_PCK0_Msk << pckID);
}

void CLK_PCKOutputEnable(uint8_t pckID)
{
    /* Turn on the PCK clock output */
    PMC_REGS->PMC_SCER = (PMC_SCER_PCK0_Msk << pckID);
}

void CLK_PCKOutputDisable(uint8_t pckID)
{
    /* Turn off the PCK clock output */
    PMC_REGS->PMC_SCDR = (PMC_SCDR_PCK0_Msk << pckID);
}


</#if><#-- PCK_USED -->
/*********************************************************************************
                        Check Peripheral clock status
*********************************************************************************/
static bool PeripheralClockStatus(uint32_t periph_id)
{
    bool retval = false;
    uint32_t status = 0U;
    const uint32_t csr_offset[] = { PMC_CSR0_REG_OFST,
                                    PMC_CSR1_REG_OFST,
                                    PMC_CSR2_REG_OFST,
                                    PMC_CSR3_REG_OFST
                                    };
    uint32_t index = periph_id / 32U;
    if (index < (sizeof(csr_offset)/sizeof(csr_offset[0])))
    {
        status = (*(volatile uint32_t* const)((PMC_BASE_ADDRESS +
                                                        csr_offset[index])));
        retval = ((status & ((uint32_t)1U << (periph_id % 32U))) != 0U);
    }
    return retval;
}
<#if ALLOW_CLK_CONFIG?? &&  ALLOW_CLK_CONFIG>
static bool PeripheralGCLKStatus(uint32_t periph_id)
{
    bool retval = false;
    uint32_t status = 0U;
    const uint32_t gcsr_offset[] = { PMC_GCSR0_REG_OFST,
                                    PMC_GCSR1_REG_OFST,
                                    PMC_GCSR2_REG_OFST,
                                    PMC_GCSR3_REG_OFST
                                    };
    uint32_t index = periph_id / 32U;
    if (index < (sizeof(gcsr_offset)/sizeof(gcsr_offset[0])))
    {
        status = (*(volatile uint32_t* const)((PMC_BASE_ADDRESS +
                                                        gcsr_offset[index])));
        retval = ((status & (1 << (periph_id % 32U))) != 0U);
    }
    return retval;
}

static const uint8_t modulesWithGCLK[] =
{
    ${MODULES_WITH_GCLK}
};
</#if>
/*********************************************************************************
                        Initialize Peripheral clocks
*********************************************************************************/
static void PeripheralClockInitialize(void)
{
    struct {
        uint8_t id;
        uint8_t clken;
        uint8_t gclken;
        uint8_t css;
        uint8_t divs;
    } periphList[] =
    {
        <#list 0..CLK_MAX_PERIPHERAL_ID as i>
            <#if .vars["CLK_ID_NAME_"+i]?has_content>
                <#assign name = .vars["CLK_ID_NAME_"+i]>
                <#assign clken = .vars[name+"_CLOCK_ENABLE"]>
                <#if .vars["CLK_"+name+"_GCLKEN"]?has_content && .vars["CLK_"+name+"_GCLKEN"]>
                    <#assign gclken = true>
                <#else>
                    <#assign gclken = false>
                </#if>
                <#if gclken>
                    <#assign gclkcss = .vars["CLK_"+name+"_GCLKCSS"]>
                    <#assign gclkdiv = .vars["CLK_"+name+"_GCLKDIV"]>
                <#else>
                    <#assign gclkcss = "0">
                    <#assign gclkdiv = "0">
                </#if>
                <#if clken || gclken>
                    <#lt>        { ID_${name?replace("PIO0", "PIOA")?replace("PIO1", "PIOD")}, ${clken?then("1U", "0U")}, ${gclken?then("1U", "0U")}, ${gclkcss}U, ${gclkdiv}U},

                </#if>
            </#if>
        </#list>
        { ID_PERIPH_MAX + 1, 0, 0, 0, 0}//end of list marker
    };
    uint32_t count = sizeof(periphList)/sizeof(periphList[0]);
    uint32_t i = 0U;

    while((i < count) && (periphList[i].id != ((uint32_t)ID_PERIPH_MAX + 1U)))
    {
        PMC_REGS->PMC_PCR = PMC_PCR_CMD_Msk |\
                            PMC_PCR_GCLKEN(periphList[i].gclken) |\
                            PMC_PCR_EN(periphList[i].clken) |\
                            PMC_PCR_GCLKDIV(periphList[i].divs) |\
                            PMC_PCR_GCLKCSS(periphList[i].css) |\
                            PMC_PCR_PID(periphList[i].id);
        while(PeripheralClockStatus(periphList[i].id) == false)
        {
            /* Wait for clock to be initialized */
        }
        i++;
    }
}

<#if ALLOW_CLK_CONFIG?? &&  ALLOW_CLK_CONFIG>
uint32_t CLK_PeripheralClockConfigGet(ID_PERIPH periphID)
{
    /* Set the command as read */
    PMC_REGS->PMC_PCR &= ~PMC_PCR_CMD_Msk;

    /* Set the PID */
    PMC_REGS->PMC_PCR = (PMC_REGS->PMC_PCR & ~PMC_PCR_PID_Msk) | PMC_PCR_PID(periphID);

    /* Return the clock configuration */
    return PMC_REGS->PMC_PCR;
}

void CLK_PeripheralClockConfigSet(ID_PERIPH periphID, bool periphClkEn, bool gclkEn, GCLK_SRC gclkSrc, uint8_t gclkDiv)
{
    uint8_t index;
    bool peripheralHasGCLK = false;

    for (index = 0; index < sizeof(modulesWithGCLK)/sizeof(modulesWithGCLK[0]); index++)
    {
        if (modulesWithGCLK[index] == periphID)
        {
            peripheralHasGCLK = true;
            break;
        }
    }

    if (peripheralHasGCLK == true)
    {
        PMC_REGS->PMC_PCR = PMC_PCR_CMD_Msk | PMC_PCR_EN((uint32_t)periphClkEn) | PMC_PCR_GCLKEN((uint32_t) gclkEn) | PMC_PCR_GCLKCSS(gclkSrc) | PMC_PCR_GCLKDIV(gclkDiv) | PMC_PCR_PID(periphID);
    }
    else
    {
        PMC_REGS->PMC_PCR = PMC_PCR_CMD_Msk | PMC_PCR_EN((uint32_t)periphClkEn) | PMC_PCR_PID(periphID);
    }

    if (periphClkEn == true)
    {
        while(PeripheralClockStatus(periphID) == false)
        {
            /* Wait for clock to be initialized */
        }
    }

    if ((peripheralHasGCLK == true) && (gclkEn == true))
    {
        while(PeripheralGCLKStatus(periphID) == false)
        {
            /* Wait for GCLK to be initialized */
        }
    }
}

</#if>
/*********************************************************************************
                                Clock Initialize
*********************************************************************************/
void CLK_Initialize( void )
{
<#if CPU_CORE_ID == 0>
    if(RSTC_PMCResetStatusGet())
    {
<#if CLK_TDXTALSEL == "XTAL">
        /* Initialize TD slow clock */
        SlowClockInitialize();

</#if>
<#if (CLK_MOSCXTBY || CLK_MOSCXTEN)>
        /* Initialize MAINCK */
        MainClockInitialize();

</#if>
<#if PLL_USED>
<#list PLL_LIST as PLL_NAME>
<#if .vars["CLK_" + PLL_NAME + "_ENPLL"]>
        /* Initialize ${PLL_NAME} */
        PLLInitialize((uint32_t)${PLL_NAME}, &${PLL_NAME?lower_case}_cfg);

</#if>
</#list>
</#if>
        /* Apply flash patch */
        CLK_ApplyFlashPatch(${CPU_CLOCK_FREQUENCY});

<#if GEN_CPU_CLK>
        /* Initialize CPU clock */
        CPUClockInitialize();

</#if>
<#if PCK_USED>
        /* Initialize Programmable clock */
        PCKInitialize();

</#if>
        /* Initialize Peripheral clock */
        PeripheralClockInitialize();
<#if !CLK_MOSCRCEN>

        /* Disable Main RC Oscillator */
        CLK_DisableMainRCOscillator();
</#if>
    }
    else
    {
        /* Apply flash patch */
        CLK_ApplyFlashPatch(${CPU_CLOCK_FREQUENCY});
    }
<#else><#--CPU_CORE_ID -->
    <#if PCK_USED>
    /* Initialize Programmable clock */
    PCKInitialize();

    </#if>
    /* Initialize Peripheral clock */
    PeripheralClockInitialize();
</#if>
}