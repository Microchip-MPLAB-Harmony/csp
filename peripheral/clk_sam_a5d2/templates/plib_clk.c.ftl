/*******************************************************************************
Copyright (c) 2018 released Microchip Technology Inc.  All rights reserved.

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
	PMC_REGS->PMC_PCK[${INDEX}]= PMC_PCK_CSS_${CSS} | PMC_PCK_PRES(${PRES-1});
	</#if>
</#macro>
</#compress>

<#if PMC_CKGR_UCKR_UPLLEN && !USE_BOOTLOADER_CLOCKS>
/*********************************************************************************
Initialize UTMI PLL  (UPLLCK)
*********************************************************************************/

static void CLK_UTMIPLLInitialize(void)
{
    /* Set the UTMI reference clock */
    uint32_t sfr_utmiclktrim_val = SFR_REGS->SFR_UTMICKTRIM & ~SFR_UTMICKTRIM_FREQ_Msk;
	SFR_REGS->SFR_UTMICKTRIM = sfr_utmiclktrim_val | SFR_UTMICKTRIM_FREQ_${UTMI_CKTRIM_FREQ};
	
	/* Enable UPLL and configure UPLL lock time */
	PMC_REGS->CKGR_UCKR = CKGR_UCKR_UPLLEN_Msk | CKGR_UCKR_UPLLCOUNT(${PMC_CKGR_UCKR_UPLLCOUNT});
	
	/* Wait until PLL Lock occurs */
    while ((PMC_REGS->PMC_SR & PMC_SR_LOCKU_Msk) != PMC_SR_LOCKU_Msk);
}
</#if>

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

<#if PMC_SCER_UDPCLK || PMC_SCER_UHPCLK>
/*********************************************************************************
Initialize USB FS clock 
*********************************************************************************/

static void CLK_USBClockInitialize ( void )
{    	
    /* Configure Full-Speed USB Clock source and Clock Divider */
	PMC_REGS->PMC_USB = PMC_USB_USBDIV(${PMC_USB_USBDIV-1}) <#if PMC_USB_USBS == "UPLL_CLK"> | PMC_USB_USBS_Msk</#if>;
	
	
	/* Enable Full-Speed USB Clock Output */
    PMC_REGS->PMC_SCER |= PMC_SCER_UDP(${PMC_SCER_UDPCLK?then(1,0)}) | PMC_SCER_UHP(${PMC_SCER_UHPCLK?then(1,0)});
}
</#if>

/*********************************************************************************
Initialize Generic clock
*********************************************************************************/

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

<#if PMC_SCER_PCK0 || PMC_SCER_PCK1 || PMC_SCER_PCK2>
/*********************************************************************************
Initialize Programmable Clock (PCKx)
*********************************************************************************/

static void CLK_ProgrammableClockInitialize(void)
{
	/* Disable selected programmable clock	*/
	PMC_REGS->PMC_SCDR = ${PMC_SCDR_PCKX_MSK};

	/* Configure selected programmable clock	*/
<@CONFIGURE_PCK INDEX=0 ENABLED=PMC_SCER_PCK0 CSS=PMC_PCK0_CSS PRES=PMC_PCK0_PRES />
<@CONFIGURE_PCK INDEX=1 ENABLED=PMC_SCER_PCK1 CSS=PMC_PCK1_CSS PRES=PMC_PCK1_PRES />
<@CONFIGURE_PCK INDEX=2 ENABLED=PMC_SCER_PCK2 CSS=PMC_PCK2_CSS PRES=PMC_PCK2_PRES />

	/* Enable selected programmable clock	*/
	PMC_REGS->PMC_SCER = ${PMC_SCER_PCKX_MSK};
	
	/* Wait for clock to be ready	*/	
	while((PMC_REGS->PMC_SR & (${PMC_SR_PCKRDYX_MSK}) ) != (${PMC_SR_PCKRDYX_MSK}));
}
</#if>


/*********************************************************************************
Initialize Peripheral clock
*********************************************************************************/

static void CLK_PeripheralClockInitialize(void)
{
    /* Enable clock for the selected peripherals, since the rom boot will turn on
     * certain clocks turn off all clocks not expressly enabled */
   	PMC_REGS->PMC_PCER0=0x${PMC_PCER0};
    PMC_REGS->PMC_PCDR0=~0x${PMC_PCER0};
    PMC_REGS->PMC_PCER1=0x${PMC_PCER1};
    PMC_REGS->PMC_PCDR1=~0x${PMC_PCER1};
}

<#if PMC_SCER_LCDCK>
/*********************************************************************************
Initialize LCDC clock
*********************************************************************************/

static void CLK_LCDCClockInitialize(void)
{
    PMC_REGS->PMC_SCER |= PMC_SCER_LCDCK(1);
}
</#if>

<#if PMC_SCER_ISCCK>
/*********************************************************************************
Initialize LCDC clock
*********************************************************************************/

static void CLK_ISCClockInitialize(void)
{
    PMC_REGS->PMC_SCER |= PMC_SCER_ISCCK(1);
}
</#if>

/*********************************************************************************
Clock Initialize
*********************************************************************************/

void CLK_Initialize( void )
{ 
<#if PMC_AUDIO_PLL0_PLLEN>
    /* Initialize Audio PLL */
    CLK_AudioPLLInitialize();

</#if>
<#if PMC_CKGR_UCKR_UPLLEN && !USE_BOOTLOADER_CLOCKS>
	/* Initialize UTMI PLL */
	CLK_UTMIPLLInitialize();

</#if>
<#if PMC_SCER_UDPCLK || PMC_SCER_UHPCLK>
	/* Initialize USB Clock */
	CLK_USBClockInitialize();

</#if>
	/* Initialize Generic Clock */
	CLK_GenericClockInitialize();

<#if PMC_SCER_PCK0 || PMC_SCER_PCK1 || PMC_SCER_PCK2>
	/* Initialize Programmable Clock */
	CLK_ProgrammableClockInitialize();

</#if>
	/* Initialize Peripheral Clock */
	CLK_PeripheralClockInitialize();

<#if PMC_SCER_LCDCK>
    /* Initalize LCDC (MCKx2) Clock */
    CLK_LCDCClockInitialize();

</#if>
<#if PMC_SCER_ISCCK>
    /* Initalize ISC (MCKx2) Clock */
    CLK_ISCClockInitialize();

</#if>
}

<#--
/*******************************************************************************
 End of File
*/
-->
