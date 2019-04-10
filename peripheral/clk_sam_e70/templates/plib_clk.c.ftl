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

<#list 0..7 as i>
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



<#macro CONFIGURE_GCLK INDEX PCLKEN GCLKEN GCLKCSS GCLKDIV>
    <#if PCLKEN || GCLKEN>
    /* Setup Generic/Peripheral Clock for I2S${INDEX} */
    PMC_REGS->PMC_PCR = <#if INDEX == 0> PMC_PCR_PID(69) <#else> PMC_PCR_PID(70)</#if> | PMC_PCR_CMD_Msk ${PCLKEN?then('| PMC_PCR_EN_Msk', '')}  ${GCLKEN?then('| PMC_PCR_GCLKEN_Msk |  PMC_PCR_EN_Msk | PMC_PCR_GCLKCSS_${GCLKCSS} | PMC_PCR_GCLKDIV(${GCLKDIV-1})', '')};
    </#if>

    <#if GCLKEN>
    MATRIX_REGS->CCFG_PCCR |= <#if INDEX == 0> CCFG_PCCR_I2SC0CC_Msk <#else> CCFG_PCCR_I2SC1CC_Msk </#if>;
    </#if>

</#macro>

<#macro CONFIGURE_PCK INDEX ENABLED CSS PRES>
    <#if ENABLED>
    PMC_REGS->PMC_PCK[${INDEX}]= PMC_PCK_CSS_${CSS} | PMC_PCK_PRES(${PRES-1});
    </#if>
</#macro>
</#compress>


<#if SUPC_CR_XTALSEL>
/*********************************************************************************
Initialize Slow Clock (SLCK)
*********************************************************************************/

static void CLK_SlowClockInitialize(void)
{
<#if SUPC_MR_OSCBYPASS && SUPC_CR_XTALSEL>
    /* External clock signal on XIN32 pin is selected as the Slow Clock (SLCK) source.
       Bypass 32K Crystal Oscillator  */
    SUPC_REGS->SUPC_MR |= SUPC_MR_KEY_PASSWD | SUPC_MR_OSCBYPASS_BYPASS;
    SUPC_REGS->SUPC_CR |= SUPC_CR_KEY_PASSWD | SUPC_CR_XTALSEL_CRYSTAL_SEL;

    /* Wait until the external clock signal is ready and
       Slow Clock (SLCK) is switched to external clock signal */
    while (!(SUPC_REGS->SUPC_SR & SUPC_SR_OSCSEL_Msk) &&  !(PMC_REGS->PMC_SR & PMC_SR_MOSCRCS_Msk))
    {
    }

<#elseif SUPC_CR_XTALSEL>
    /* 32KHz Crystal Oscillator is selected as the Slow Clock (SLCK) source.
       Enable 32KHz Crystal Oscillator  */
    SUPC_REGS->SUPC_CR |= SUPC_CR_KEY_PASSWD | SUPC_CR_XTALSEL_CRYSTAL_SEL;

    /* Wait until the 32K Crystal oscillator clock is ready and
       Slow Clock (SLCK) is switched to 32KHz Oscillator */
    while (!(SUPC_REGS->SUPC_SR & SUPC_SR_OSCSEL_Msk) &&  !(PMC_REGS->PMC_SR & PMC_SR_MOSCRCS_Msk))
    {
    }
</#if>
}
</#if>


<#if (PMC_CKGR_MOR_MOSCXTBY || PMC_CKGR_MOR_MOSCXTEN || (PMC_CKGR_MOR_MOSCRCEN == false) || (PMC_CKGR_MOR_MOSCRCEN && PMC_CKGR_MOR_MOSCRCF != "_12_MHz"))>
/*********************************************************************************
Initialize Main Clock (MAINCK)
*********************************************************************************/
static void CLK_MainClockInitialize(void)
{
<#if PMC_CKGR_MOR_MOSCXTBY>
    /* Disable Main Crystal Oscillator and Enable External Clock Signal on XIN pin  */
    PMC_REGS->CKGR_MOR = (PMC_REGS->CKGR_MOR & ~CKGR_MOR_MOSCXTEN_Msk) | CKGR_MOR_KEY_PASSWD | CKGR_MOR_MOSCXTBY_Msk;

    <#if PMC_CKGR_MOR_MOSCSEL>
     /* External clock signal (XIN pin) is selected as the Main Clock (MAINCK) source.
        Switch Main Clock (MAINCK) to External signal on XIN pin */
    PMC_REGS->CKGR_MOR |= CKGR_MOR_KEY_PASSWD | CKGR_MOR_MOSCSEL_Msk;

    /* Wait until MAINCK is switched to External Clock Signal (XIN pin) */
    while ( (PMC_REGS->PMC_SR & PMC_SR_MOSCSELS_Msk) != PMC_SR_MOSCSELS_Msk);
    </#if>

<#elseif PMC_CKGR_MOR_MOSCXTEN>
    /* Enable Main Crystal Oscillator */
    PMC_REGS->CKGR_MOR = (PMC_REGS->CKGR_MOR & ~CKGR_MOR_MOSCXTST_Msk) | CKGR_MOR_KEY_PASSWD | CKGR_MOR_MOSCXTST(${PMC_CKGR_MOR_MOSCXTST}) | CKGR_MOR_MOSCXTEN_Msk;

    /* Wait until the main oscillator clock is ready */
    while ( (PMC_REGS->PMC_SR & PMC_SR_MOSCXTS_Msk) != PMC_SR_MOSCXTS_Msk);

    <#if PMC_CKGR_MOR_MOSCSEL>
    /* Main Crystal Oscillator is selected as the Main Clock (MAINCK) source.
    Switch Main Clock (MAINCK) to Main Crystal Oscillator clock */
    PMC_REGS->CKGR_MOR|= CKGR_MOR_KEY_PASSWD | CKGR_MOR_MOSCSEL_Msk;

    /* Wait until MAINCK is switched to Main Crystal Oscillator */
    while ( (PMC_REGS->PMC_SR & PMC_SR_MOSCSELS_Msk) != PMC_SR_MOSCSELS_Msk);

    </#if>
</#if>

<#if PMC_CKGR_MOR_MOSCRCEN>
    /* Enable the RC Oscillator */
    PMC_REGS->CKGR_MOR|= CKGR_MOR_KEY_PASSWD | CKGR_MOR_MOSCRCEN_Msk;

    /* Wait until the RC oscillator clock is ready. */
    while( (PMC_REGS->PMC_SR & PMC_SR_MOSCRCS_Msk) != PMC_SR_MOSCRCS_Msk);

    /* Configure the RC Oscillator frequency */
    PMC_REGS->CKGR_MOR = (PMC_REGS->CKGR_MOR & ~CKGR_MOR_MOSCRCF_Msk) | CKGR_MOR_KEY_PASSWD | CKGR_MOR_MOSCRCF${PMC_CKGR_MOR_MOSCRCF};

    /* Wait until the RC oscillator clock is ready */
    while( (PMC_REGS->PMC_SR& PMC_SR_MOSCRCS_Msk) != PMC_SR_MOSCRCS_Msk);

    <#if !PMC_CKGR_MOR_MOSCSEL>
    /* Main RC Oscillator is selected as the Main Clock (MAINCK) source.
       Switch Main Clock (MAINCK) to the RC Oscillator clock */
    PMC_REGS->CKGR_MOR = (PMC_REGS->CKGR_MOR & ~CKGR_MOR_MOSCSEL_Msk) | CKGR_MOR_KEY_PASSWD;
    </#if>
<#else>
    /* Disable the RC Oscillator */
    PMC_REGS->CKGR_MOR = CKGR_MOR_KEY_PASSWD | (PMC_REGS->CKGR_MOR & ~CKGR_MOR_MOSCRCEN_Msk);
</#if>

}
</#if>

<#if CLK_PLLA_ENABLE>
/*********************************************************************************
Initialize PLLA (PLLACK)
*********************************************************************************/

static void CLK_PLLAInitialize(void)
{
    /* Configure and Enable PLLA */
    PMC_REGS->CKGR_PLLAR = CKGR_PLLAR_ONE_Msk | CKGR_PLLAR_PLLACOUNT(0x3f) |
                              CKGR_PLLAR_MULA(${PMC_CKGR_PLLAR_MULA} - 1) |
                              CKGR_PLLAR_DIVA(${PMC_CKGR_PLLAR_DIVA});

    while ( (PMC_REGS->PMC_SR & PMC_SR_LOCKA_Msk) != PMC_SR_LOCKA_Msk);

}
</#if>


<#if PMC_CKGR_UCKR_UPLLEN>
/*********************************************************************************
Initialize UTMI PLL  (UPLLCK)
*********************************************************************************/

static void CLK_UTMIPLLInitialize(void)
{

    /* Configure Crystal Clock Frequency (12MHz or 16MHz) to select USB PLL (UPLL) multiplication factor
       UPLL multiplication factor is x40 to generate 480MHz from 12MHz
       UPLL multiplication factor is x30 to generate 480MHz from 16MHz  */
    <#if UTMI_CKTRIM_FREQ == "XTAL12">
    UTMI_REGS->UTMI_CKTRIM= UTMI_CKTRIM_FREQ_XTAL12;
    <#else>
    UTMI_REGS->UTMI_CKTRIM= UTMI_CKTRIM_FREQ_XTAL16;
    </#if>

    /* Enable UPLL and configure UPLL lock time */
    PMC_REGS->CKGR_UCKR = CKGR_UCKR_UPLLEN_Msk | CKGR_UCKR_UPLLCOUNT(0x3F);

    /* Wait until PLL Lock occurs */
    while ((PMC_REGS->PMC_SR & PMC_SR_LOCKU_Msk) != PMC_SR_LOCKU_Msk);

    <#if PMC_MCKR_UPLLDIV2>
    /* UPLL clock frequency is 240Mhz (Divider=2) */
    PMC_REGS->PMC_MCKR |= PMC_MCKR_UPLLDIV2_Msk;
    <#else>
    /* UPLL clock frequency is 480MHz (Divider=1) */
    PMC_REGS->PMC_MCKR &= (~PMC_MCKR_UPLLDIV2_Msk);
    </#if>

    /* Wait until clock is ready */
    while ( (PMC_REGS->PMC_SR & PMC_SR_MCKRDY_Msk) != PMC_SR_MCKRDY_Msk);
}
</#if>

<#if (PMC_MCKR_CSS != "MAIN_CLK") || (PMC_MCKR_MDIV != "EQ_PCK") || ( PMC_MCKR_PRES != "CLK_1")>
/*********************************************************************************
Initialize Master clock (MCK)
*********************************************************************************/

static void CLK_MasterClockInitialize(void)
{
<#if PMC_MCKR_CSS == "PLLA_CLK" || PMC_MCKR_CSS == "UPLL_CLK">
    /* Program PMC_MCKR.PRES and wait for PMC_SR.MCKRDY to be set   */
    PMC_REGS->PMC_MCKR = (PMC_REGS->PMC_MCKR & ~PMC_MCKR_PRES_Msk) | PMC_MCKR_PRES_${PMC_MCKR_PRES};
    while ((PMC_REGS->PMC_SR & PMC_SR_MCKRDY_Msk) != PMC_SR_MCKRDY_Msk);

    /* Program PMC_MCKR.MDIV and Wait for PMC_SR.MCKRDY to be set   */
    PMC_REGS->PMC_MCKR = (PMC_REGS->PMC_MCKR & ~PMC_MCKR_MDIV_Msk) | PMC_MCKR_MDIV_${PMC_MCKR_MDIV};
    while ((PMC_REGS->PMC_SR & PMC_SR_MCKRDY_Msk) != PMC_SR_MCKRDY_Msk);

    /* Program PMC_MCKR.CSS and Wait for PMC_SR.MCKRDY to be set    */
    PMC_REGS->PMC_MCKR = (PMC_REGS->PMC_MCKR & ~PMC_MCKR_CSS_Msk) | PMC_MCKR_CSS_${PMC_MCKR_CSS};
    while ((PMC_REGS->PMC_SR & PMC_SR_MCKRDY_Msk) != PMC_SR_MCKRDY_Msk);
</#if>

<#if PMC_MCKR_CSS == "SLOW_CLK" || PMC_MCKR_CSS == "MAIN_CLK">
    /* Program PMC_MCKR.CSS and Wait for PMC_SR.MCKRDY to be set    */
    PMC_REGS->PMC_MCKR = (PMC_REGS->PMC_MCKR & ~PMC_MCKR_CSS_Msk) | PMC_MCKR_CSS_${PMC_MCKR_CSS};
    while ((PMC_REGS->PMC_SR & PMC_SR_MCKRDY_Msk) != PMC_SR_MCKRDY_Msk);


    /* Program PMC_MCKR.PRES and wait for PMC_SR.MCKRDY to be set   */
    PMC_REGS->PMC_MCKR = (PMC_REGS->PMC_MCKR & ~PMC_MCKR_PRES_Msk) | PMC_MCKR_PRES_${PMC_MCKR_PRES};
    while ((PMC_REGS->PMC_SR & PMC_SR_MCKRDY_Msk) != PMC_SR_MCKRDY_Msk);


    /* Program PMC_MCKR.MDIV and Wait for PMC_SR.MCKRDY to be set   */
    PMC_REGS->PMC_MCKR = (PMC_REGS->PMC_MCKR & ~PMC_MCKR_MDIV_Msk) | PMC_MCKR_MDIV_${PMC_MCKR_MDIV};
    while ((PMC_REGS->PMC_SR & PMC_SR_MCKRDY_Msk) != PMC_SR_MCKRDY_Msk);
</#if>
}
</#if>


<#if PMC_SCER_USBCLK>
/*********************************************************************************
Initialize USB FS clock
*********************************************************************************/

static void CLK_USBClockInitialize ( void )
{
    /* Configure Full-Speed USB Clock source and Clock Divider */
    PMC_REGS->PMC_USB = PMC_USB_USBDIV(${PMC_USB_USBDIV-1}) <#if PMC_USB_USBS == "UPLL_CLK"> | PMC_USB_USBS_Msk</#if>;


    /* Enable Full-Speed USB Clock Output */
    PMC_REGS->PMC_SCER = PMC_SCER_USBCLK_Msk;
}
</#if>

<#if PMC_PCR_GCLK0EN || PMC_PCR_EN0 || PMC_PCR_GCLK1EN || PMC_PCR_EN1>
/*********************************************************************************
Initialize Generic clock
*********************************************************************************/

static void CLK_GenericClockInitialize(void)
{
<@CONFIGURE_GCLK 0 PMC_PCR_EN0 PMC_PCR_GCLK0EN PMC_PCR_GCLK0CSS PMC_PCR_GCLK0DIV />
<@CONFIGURE_GCLK 1 PMC_PCR_EN1 PMC_PCR_GCLK1EN PMC_PCR_GCLK1CSS PMC_PCR_GCLK1DIV />
}
</#if>



<#if PMC_SCER_PCK0 || PMC_SCER_PCK1 || PMC_SCER_PCK2 || PMC_SCER_PCK3 ||
     PMC_SCER_PCK4 || PMC_SCER_PCK5 || PMC_SCER_PCK6 || PMC_SCER_PCK7>
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
<@CONFIGURE_PCK INDEX=3 ENABLED=PMC_SCER_PCK3 CSS=PMC_PCK3_CSS PRES=PMC_PCK3_PRES />
<@CONFIGURE_PCK INDEX=4 ENABLED=PMC_SCER_PCK4 CSS=PMC_PCK4_CSS PRES=PMC_PCK4_PRES />
<@CONFIGURE_PCK INDEX=5 ENABLED=PMC_SCER_PCK5 CSS=PMC_PCK5_CSS PRES=PMC_PCK5_PRES />
<@CONFIGURE_PCK INDEX=6 ENABLED=PMC_SCER_PCK6 CSS=PMC_PCK6_CSS PRES=PMC_PCK6_PRES />
<@CONFIGURE_PCK INDEX=7 ENABLED=PMC_SCER_PCK7 CSS=PMC_PCK7_CSS PRES=PMC_PCK7_PRES />

    /* Enable selected programmable clock   */
    PMC_REGS->PMC_SCER =    ${PMC_SCER_PCKX_MSK};

    /* Wait for clock to be ready   */
    while( (PMC_REGS->PMC_SR & (${PMC_SR_PCKRDYX_MSK}) ) != (${PMC_SR_PCKRDYX_MSK}));


}
</#if>


/*********************************************************************************
Clock Initialize
*********************************************************************************/
void CLK_Initialize( void )
{

<#if SUPC_CR_XTALSEL>
    /* Initialize Slow Clock */
    CLK_SlowClockInitialize();
</#if>

<#if (PMC_CKGR_MOR_MOSCXTBY || PMC_CKGR_MOR_MOSCXTEN || (PMC_CKGR_MOR_MOSCRCEN == false) || (PMC_CKGR_MOR_MOSCRCEN && PMC_CKGR_MOR_MOSCRCF != "_12_MHz"))>
    /* Initialize Main Clock */
    CLK_MainClockInitialize();
</#if>

<#if CLK_PLLA_ENABLE>
    /* Initialize PLLA */
    CLK_PLLAInitialize();
</#if>

<#if PMC_CKGR_UCKR_UPLLEN>
    /* Initialize UTMI PLL */
    CLK_UTMIPLLInitialize();
</#if>

<#if (PMC_MCKR_CSS != "MAIN_CLK") || (PMC_MCKR_MDIV != "EQ_PCK") || ( PMC_MCKR_PRES != "CLK_1")>
    /* Initialize Master Clock */
    CLK_MasterClockInitialize();
</#if>

<#if PMC_SCER_USBCLK>
    /* Initialize USB Clock */
    CLK_USBClockInitialize();
</#if>

<#if PMC_PCR_GCLK0EN || PMC_PCR_EN0 || PMC_PCR_GCLK1EN || PMC_PCR_EN1>
    /* Initialize Generic Clock */
    CLK_GenericClockInitialize();
</#if>

<#if PMC_SCER_PCK0 || PMC_SCER_PCK1 || PMC_SCER_PCK2 || PMC_SCER_PCK3 ||
     PMC_SCER_PCK4 || PMC_SCER_PCK5 || PMC_SCER_PCK6 || PMC_SCER_PCK7>
    /* Initialize Programmable Clock */
    CLK_ProgrammableClockInitialize();
</#if>

    /* Enable Peripheral Clock */
<#if (PMC_PCER0 != "0")>
    PMC_REGS->PMC_PCER0=0x${PMC_PCER0};
</#if>
<#if (PMC_PCER1 != "0")>
    PMC_REGS->PMC_PCER1=0x${PMC_PCER1};
</#if>
}
<#--
/*******************************************************************************
 End of File
*/
-->
