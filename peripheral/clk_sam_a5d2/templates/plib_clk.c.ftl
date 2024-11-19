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


<#compress>
<#assign PMC_SCDR_PCKX_MSK = "">
<#assign PMC_SCER_PCKX_MSK = "">
<#assign PMC_SR_PCKRDYX_MSK = "">

<#list 0..2 as i>
<#assign ENABLE = "PMC_SCER_PCK" + i>

<#if .vars[ENABLE] == true>

    <#if PMC_SCER_PCKX_MSK != "">
        <#assign PMC_SCER_PCKX_MSK = PMC_SCER_PCKX_MSK + " | " + "PMC_SCER_PCK" + i +"_Msk">
        <#assign PMC_SCDR_PCKX_MSK = PMC_SCDR_PCKX_MSK + " | " + "PMC_SCDR_PCK" + i +"_Msk">
        <#assign PMC_SR_PCKRDYX_MSK = PMC_SR_PCKRDYX_MSK + " | " + "PMC_SR_PCKRDY" + i +"_Msk">
    <#else>
        <#assign PMC_SCER_PCKX_MSK = "PMC_SCER_PCK" + i +"_Msk">
        <#assign PMC_SCDR_PCKX_MSK = "PMC_SCDR_PCK" + i +"_Msk">
        <#assign PMC_SR_PCKRDYX_MSK = "PMC_SR_PCKRDY" + i +"_Msk">
    </#if>

</#if>

</#list>

<#macro CONFIGURE_PCK INDEX ENABLED CSS PRES>
    <#if ENABLED>
    PMC_REGS->PMC_PCK[${INDEX}]= PMC_PCK_CSS_${CSS} | PMC_PCK_PRES(${PRES-1}U);
    </#if>
</#macro>
</#compress>

<#if CLK_GENERATOR_CODE>
/*********************************************************************************
Initialize Slow clock
*********************************************************************************/
static void initSlowClk(void)
{
    SCKC_REGS->SCKC_CR = (SCKC_REGS->SCKC_CR & ~SCKC_CR_OSCSEL_Msk) | SCKC_CR_OSCSEL_${SCK_CR_OSCSEL};
}

/*********************************************************************************
Initialize Main clock
*********************************************************************************/
static void initMainClk(void)
{
<#if CKGR_MOR_MOSCXTBY>
    /* Disable Main Crystal Oscillator and Enable External Clock Signal on XIN pin  */
    PMC_REGS->CKGR_MOR = (PMC_REGS->CKGR_MOR & ~CKGR_MOR_MOSCXTEN_Msk) | CKGR_MOR_KEY_PASSWD | CKGR_MOR_MOSCXTBY_Msk | CKGR_MOR_ONE_Msk;

    <#if CKGR_MOR_MOSCSEL == "XTAL">
     /* External clock signal (XIN pin) is selected as the Main Clock (MAINCK) source.
        Switch Main Clock (MAINCK) to External signal on XIN pin */
    PMC_REGS->CKGR_MOR |= CKGR_MOR_KEY_PASSWD | CKGR_MOR_MOSCSEL_Msk;

    /* Wait until MAINCK is switched to External Clock Signal (XIN pin) */
    while ( (PMC_REGS->PMC_SR & PMC_SR_MOSCSELS_Msk) != PMC_SR_MOSCSELS_Msk)
    {
        /* Nothing to do */
    }
    </#if>

<#elseif CKGR_MOR_MOSCXTEN>
    /* Enable Main Crystal Oscillator */
    PMC_REGS->CKGR_MOR = (PMC_REGS->CKGR_MOR & ~CKGR_MOR_MOSCXTST_Msk) | CKGR_MOR_KEY_PASSWD | CKGR_MOR_MOSCXTST(${CKGR_MOR_MOSCXTST}) | CKGR_MOR_MOSCXTEN_Msk | CKGR_MOR_ONE_Msk;

    /* Wait until the main oscillator clock is ready */
    while ( (PMC_REGS->PMC_SR & PMC_SR_MOSCXTS_Msk) != PMC_SR_MOSCXTS_Msk)
    {
        /* Nothing to do */
    }

    <#if CKGR_MOR_MOSCSEL == "XTAL">
    /* Main Crystal Oscillator is selected as the Main Clock (MAINCK) source.
    Switch Main Clock (MAINCK) to Main Crystal Oscillator clock */
    PMC_REGS->CKGR_MOR |= CKGR_MOR_KEY_PASSWD | CKGR_MOR_MOSCSEL_Msk;

    /* Wait until MAINCK is switched to Main Crystal Oscillator */
    while ( (PMC_REGS->PMC_SR & PMC_SR_MOSCSELS_Msk) != PMC_SR_MOSCSELS_Msk)
    {
        /* Nothing to do */
    }

    </#if>
</#if>

<#if CKGR_MOR_MOSCRCEN>
    /* Enable the RC Oscillator */
    PMC_REGS->CKGR_MOR |= CKGR_MOR_KEY_PASSWD | CKGR_MOR_MOSCRCEN_Msk;

    /* Wait until the RC oscillator clock is ready. */
    while( (PMC_REGS->PMC_SR & PMC_SR_MOSCRCS_Msk) != PMC_SR_MOSCRCS_Msk)
    {
        /* Nothing to do */
    }

    <#if CKGR_MOR_MOSCSEL != "XTAL">
    /* Main RC Oscillator is selected as the Main Clock (MAINCK) source.
       Switch Main Clock (MAINCK) to the RC Oscillator clock */
    PMC_REGS->CKGR_MOR = (PMC_REGS->CKGR_MOR & ~CKGR_MOR_MOSCSEL_Msk) | CKGR_MOR_KEY_PASSWD | CKGR_MOR_ONE_Msk;
    </#if>
<#else>
    /* Disable the RC Oscillator */
    PMC_REGS->CKGR_MOR = CKGR_MOR_KEY_PASSWD | (PMC_REGS->CKGR_MOR & ~CKGR_MOR_MOSCRCEN_Msk);
</#if>
}

<#if CKGR_PLLAR_MULA0>
/*********************************************************************************
Initialize PLLA (PLLACK)
*********************************************************************************/
<#assign PMC_CKGR_PLLAR_MULA_VAL = CKGR_PLLA_MULA - 1>
static void CLK_PLLAInitialize(void)
{
    /* Configure and Enable PLLA */
    PMC_REGS->CKGR_PLLAR = CKGR_PLLAR_ONE_Msk | CKGR_PLLAR_PLLACOUNT(${CKGR_PLLAR_PLLACOUNT}U) |
                              CKGR_PLLAR_MULA(${PMC_CKGR_PLLAR_MULA_VAL}) |
                              CKGR_PLLAR_DIVA(${CKGR_PLLAR_DIVA}U)|
                              CKGR_PLLAR_OUTA(${CKGR_PLLAR_PLLDIVA2}U);

    while ( (PMC_REGS->PMC_SR & PMC_SR_LOCKA_Msk) != PMC_SR_LOCKA_Msk)
    {
        /* Nothing to do */
    }

}
</#if>

<#if (PMC_MCKR_CSS != "MAIN_CLK") || ( PMC_MCKR_PRES != "CLOCK")>
/*********************************************************************************
Initialize Master clock (MCK)
*********************************************************************************/

static void CLK_MasterClockInitialize(void)
{
<#if PMC_MCKR_CSS == "PLLA_CLK" || PMC_MCKR_CSS == "UPLL_CLK">
    /* Program PMC_MCKR.PRES and wait for PMC_SR.MCKRDY to be set   */
    PMC_REGS->PMC_MCKR = (PMC_REGS->PMC_MCKR & ~PMC_MCKR_PRES_Msk) | PMC_MCKR_PRES_${PMC_MCKR_PRES};
    while ((PMC_REGS->PMC_SR & PMC_SR_MCKRDY_Msk) != PMC_SR_MCKRDY_Msk)
    {
        /* Nothing to do */
    }

    /* Program PMC_MCKR.MDIV and Wait for PMC_SR.MCKRDY to be set   */
    PMC_REGS->PMC_MCKR = (PMC_REGS->PMC_MCKR & ~PMC_MCKR_MDIV_Msk) | PMC_MCKR_MDIV_${PMC_MCKR_MDIV};
    while ((PMC_REGS->PMC_SR & PMC_SR_MCKRDY_Msk) != PMC_SR_MCKRDY_Msk)
    {
        /* Nothing to do */
    }

    /* Program PMC_MCKR.CSS and Wait for PMC_SR.MCKRDY to be set    */
    PMC_REGS->PMC_MCKR = (PMC_REGS->PMC_MCKR & ~PMC_MCKR_CSS_Msk) | PMC_MCKR_CSS_${PMC_MCKR_CSS};
    while ((PMC_REGS->PMC_SR & PMC_SR_MCKRDY_Msk) != PMC_SR_MCKRDY_Msk)
    {
        /* Nothing to do */
    }
</#if>

<#if PMC_MCKR_CSS == "SLOW_CLK" || PMC_MCKR_CSS == "MAIN_CLK">
    /* Program PMC_MCKR.CSS and Wait for PMC_SR.MCKRDY to be set    */
    PMC_REGS->PMC_MCKR = (PMC_REGS->PMC_MCKR & ~PMC_MCKR_CSS_Msk) | PMC_MCKR_CSS_${PMC_MCKR_CSS};
    while ((PMC_REGS->PMC_SR & PMC_SR_MCKRDY_Msk) != PMC_SR_MCKRDY_Msk)
    {
        /* Nothing to do */
    }

    /* Program PMC_MCKR.PRES and wait for PMC_SR.MCKRDY to be set   */
    PMC_REGS->PMC_MCKR = (PMC_REGS->PMC_MCKR & ~PMC_MCKR_PRES_Msk) | PMC_MCKR_PRES_${PMC_MCKR_PRES};
    while ((PMC_REGS->PMC_SR & PMC_SR_MCKRDY_Msk) != PMC_SR_MCKRDY_Msk)
    {
        /* Nothing to do */
    }

    /* Program PMC_MCKR.MDIV and Wait for PMC_SR.MCKRDY to be set   */
    PMC_REGS->PMC_MCKR = (PMC_REGS->PMC_MCKR & ~PMC_MCKR_MDIV_Msk) | PMC_MCKR_MDIV_${PMC_MCKR_MDIV};
    while ((PMC_REGS->PMC_SR & PMC_SR_MCKRDY_Msk) != PMC_SR_MCKRDY_Msk)
    {
        /* Nothing to do */
    }
</#if>
}
</#if>
</#if>

<#if PMC_CKGR_UCKR_UPLLEN>
/*********************************************************************************
Initialize UTMI PLL  (UPLLCK)
*********************************************************************************/

static void CLK_UTMIPLLInitialize(void)
{
    /* Set the UTMI reference clock */
    uint32_t sfr_utmiclktrim_val = SFR_REGS->SFR_UTMICKTRIM & ~SFR_UTMICKTRIM_FREQ_Msk;
    SFR_REGS->SFR_UTMICKTRIM = sfr_utmiclktrim_val | SFR_UTMICKTRIM_FREQ${UTMI_CKTRIM_FREQ};

    /* Enable UPLL and configure UPLL lock time */
    PMC_REGS->CKGR_UCKR = CKGR_UCKR_UPLLEN_Msk | CKGR_UCKR_UPLLCOUNT(${PMC_CKGR_UCKR_UPLLCOUNT}U);

    /* Wait until PLL Lock occurs */
    while ((PMC_REGS->PMC_SR & PMC_SR_LOCKU_Msk) != PMC_SR_LOCKU_Msk)
    {
        /* Wait for PLL lock to rise */
    }
}
</#if>

/*********************************************************************************
UTMI PLL Enable/Disable
*********************************************************************************/
void CLK_UTMIPLLEnable(void)
{
    /* Enable the UTMI PLL */
    PMC_REGS->CKGR_UCKR |= CKGR_UCKR_UPLLEN_Msk;

    /* Wait until PLL Lock occurs */
    while ((PMC_REGS->PMC_SR & PMC_SR_LOCKU_Msk) != PMC_SR_LOCKU_Msk)
    {
        /* Wait for PLL lock to rise */
    }
}

void CLK_UTMIPLLDisable(void)
{
    /* Disable the UTMI PLL */
    PMC_REGS->CKGR_UCKR &= ~CKGR_UCKR_UPLLEN_Msk;
}

<#if PMC_AUDIO_PLL0_PLLEN>
/*********************************************************************************
Initialize AUDIO PLL
*********************************************************************************/

static void CLK_AudioPLLInitialize(void)
{
    /* Disable PLL */
    PMC_REGS->PMC_AUDIO_PLL0 = 0;

    /* Release PLL from reset */
    PMC_REGS->PMC_AUDIO_PLL0 |= PMC_AUDIO_PLL0_RESETN(1);

    /* Configure PLL parameters */
    PMC_REGS->PMC_AUDIO_PLL0 |= PMC_AUDIO_PLL0_QDPMC(${PMC_AUDIO_PLL0_QDPMC}) | PMC_AUDIO_PLL0_ND(${PMC_AUDIO_PLL0_ND});
    PMC_REGS->PMC_AUDIO_PLL1 = PMC_AUDIO_PLL1_QDAUDIO(${PMC_AUDIO_PLL1_QDAUDIO}) | PMC_AUDIO_PLL1_DIV(${PMC_AUDIO_PLL1_DIV}) | PMC_AUDIO_PLL1_FRACR(${PMC_AUDIO_PLL1_FRACR});

    /* Enable PLL */
    PMC_REGS->PMC_AUDIO_PLL0 |= PMC_AUDIO_PLL0_PLLEN(1) | PMC_AUDIO_PLL0_PADEN(${PMC_AUDIO_PLL0_PADEN?then(1,0)}) | PMC_AUDIO_PLL0_PMCEN(${PMC_AUDIO_PLL0_PMCEN?then(1,0)});

    /* Wait for 100 us for PLL in Calling/Driver code */
}
</#if>

<#if PMC_SCER_UHPCLK>
/*********************************************************************************
Initialize USB FS clock
*********************************************************************************/

static void CLK_USBClockInitialize ( void )
{
    /* Configure Full-Speed USB Clock source and Clock Divider */
    PMC_REGS->PMC_USB = PMC_USB_USBDIV(${PMC_USB_USBDIV-1}) <#if PMC_USB_USBS == "UPLL_CLK"> | PMC_USB_USBS_Msk</#if>;

    /* Enable Full-Speed USB Clock Output */
    PMC_REGS->PMC_SCER = PMC_SCER_UHP(1);
}
</#if>

/*********************************************************************************
Initialize Generic clock
*********************************************************************************/
<#assign PMC_PCR_GCLK_EN = false>
<#list 1..79 as pid>
    <#assign GEN_ENABLE = "PMC_PCR_PID"+pid+"_GCKEN">
    <#if .vars[GEN_ENABLE]?? && .vars[GEN_ENABLE]>
        <#assign PMC_PCR_GCLK_EN = true>
    <#break>
    </#if>
</#list>

<#if PMC_PCR_GCLK_EN>
static void CLK_GenericClockInitialize(void)
{
<#list 1..79 as pid>
<#assign GEN_ENABLE = "PMC_PCR_PID"+pid+"_GCKEN">
<#if .vars[GEN_ENABLE]??>
<#assign GEN_CSS = "PMC_PCR_PID"+pid+"_GCKCSS">
<#assign GEN_CSS_VAL = .vars[GEN_CSS]>
<#assign GEN_DIV = "PMC_PCR_PID"+pid+"_GCKDIV">
<#assign GEN_DIV_VAL = .vars[GEN_DIV] - 1>
    <#if .vars[GEN_ENABLE] == true>
    /* Enable GCLK for peripheral ID ${pid} */
    PMC_REGS->PMC_PCR = PMC_PCR_PID(${pid}) | PMC_PCR_GCKCSS(${GEN_CSS_VAL}) | PMC_PCR_CMD_Msk | PMC_PCR_GCKDIV(${GEN_DIV_VAL}) | PMC_PCR_EN_Msk | PMC_PCR_GCKEN_Msk;
    </#if>
</#if>
</#list>
}
</#if>

<#if PMC_SCER_PCK0 || PMC_SCER_PCK1 || PMC_SCER_PCK2>
/*********************************************************************************
Initialize Programmable Clock (PCKx)
*********************************************************************************/

static void CLK_ProgrammableClockInitialize(void)
{
    /* Disable selected programmable clock  */
    PMC_REGS->PMC_SCDR = ${PMC_SCDR_PCKX_MSK};

    /* Configure selected programmable clock    */
<@CONFIGURE_PCK INDEX=0 ENABLED=PMC_SCER_PCK0 CSS=PMC_PCK0_CSS PRES=PMC_PCK0_PRES />
<@CONFIGURE_PCK INDEX=1 ENABLED=PMC_SCER_PCK1 CSS=PMC_PCK1_CSS PRES=PMC_PCK1_PRES />
<@CONFIGURE_PCK INDEX=2 ENABLED=PMC_SCER_PCK2 CSS=PMC_PCK2_CSS PRES=PMC_PCK2_PRES />

    /* Enable selected programmable clock   */
    PMC_REGS->PMC_SCER = ${PMC_SCER_PCKX_MSK};

    /* Wait for clock to be ready   */
    while((PMC_REGS->PMC_SR & (${PMC_SR_PCKRDYX_MSK}) ) != (${PMC_SR_PCKRDYX_MSK}))
    {
        /* Wait for PCKRDY */
    }
}
</#if>


/*********************************************************************************
Initialize Peripheral clock
*********************************************************************************/

static void CLK_PeripheralClockInitialize(void)
{
    /* Enable clock for the selected peripherals, since the rom boot will turn on
     * certain clocks turn off all clocks not expressly enabled */
    PMC_REGS->PMC_PCER0=0x${PMC_PCER0}U;
    PMC_REGS->PMC_PCDR0=~0x${PMC_PCER0}U;
    PMC_REGS->PMC_PCER1=0x${PMC_PCER1}U;
    PMC_REGS->PMC_PCDR1=~0x${PMC_PCER1}U;
}

<#if PMC_SCER_LCDCK>
/*********************************************************************************
Initialize LCDC clock
*********************************************************************************/

static void CLK_LCDCClockInitialize(void)
{
    PMC_REGS->PMC_SCER = PMC_SCER_LCDCK(1U);
}
</#if>

<#if PMC_SCER_ISCCK>
/*********************************************************************************
Initialize LCDC clock
*********************************************************************************/

static void CLK_ISCClockInitialize(void)
{
    PMC_REGS->PMC_SCER = PMC_SCER_ISCCK(1U);
}
</#if>

<#if CLK_GENERATOR_CODE && PMC_SCER_DDRCK>

/*********************************************************************************
Initialize DDR Clock
*********************************************************************************/
static void initDDRClk(void)
{
    PMC_REGS->PMC_SCER |= PMC_SCER_DDRCK_Msk;
}
</#if>

/*********************************************************************************
Clock Initialize
*********************************************************************************/

void CLK_Initialize( void )
{
<#if CLK_GENERATOR_CODE>
    /* Initialize slow clock generator */
    initSlowClk();

    /* Initialize main clock generator */
    initMainClk();
    <#if CKGR_PLLAR_MULA0>

    /* Initialize PLLA clock generator */
    CLK_PLLAInitialize();
    </#if>
    <#if PMC_CKGR_UCKR_UPLLEN>

    /* Initialize UTMI PLL */
    CLK_UTMIPLLInitialize();
    </#if>
    <#if (PMC_MCKR_CSS != "MAIN_CLK") || ( PMC_MCKR_PRES != "CLOCK")>

    /* Initialize Master Clock */
    CLK_MasterClockInitialize();
    </#if>
</#if>
<#if PMC_AUDIO_PLL0_PLLEN>
    /* Initialize Audio PLL */
    CLK_AudioPLLInitialize();

</#if>
<#if PMC_CKGR_UCKR_UPLLEN && !CLK_GENERATOR_CODE>
    /* Initialize UTMI PLL */
    CLK_UTMIPLLInitialize();

</#if>
<#if PMC_SCER_UHPCLK>
    /* Initialize USB Clock */
    CLK_USBClockInitialize();

</#if>
<#if PMC_PCR_GCLK_EN>
    /* Initialize Generic Clock */
    CLK_GenericClockInitialize();

</#if>
<#if PMC_SCER_PCK0 || PMC_SCER_PCK1 || PMC_SCER_PCK2>
    /* Initialize Programmable Clock */
    CLK_ProgrammableClockInitialize();

</#if>
    /* Initialize Peripheral Clock */
    CLK_PeripheralClockInitialize();
<#if CLK_GENERATOR_CODE && PMC_SCER_DDRCK>

    /* Initialize DDR Clock */
    initDDRClk();
</#if>

<#if PMC_SCER_LCDCK>
    /* Initialize LCDC (MCKx2) Clock */
    CLK_LCDCClockInitialize();

</#if>
<#if PMC_SCER_ISCCK>
    /* Initialize ISC (MCKx2) Clock */
    CLK_ISCClockInitialize();

</#if>
}

<#--
/*******************************************************************************
 End of File
*/
-->
