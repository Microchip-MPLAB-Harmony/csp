<#--
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
 -->


#include "clk.h"

<#macro CONFIGURE_GCLK INDEX PCLKEN GCLKEN GCLKCSS GCLKDIV>
	<#if PCLKEN || GCLKEN>
	/* Setup Generic/Peripheral Clock for I2S${INDEX} */
    pcr = PMC_PCR_CMD_Msk;
	    <#if INDEX == 0>
	pcr |= PMC_PCR_PID(69);
	    <#else>
	pcr |= PMC_PCR_PID(70);
	    </#if>
		<#if PCLKEN>
	pcr |= PMC_PCR_EN_Msk;
		</#if>
		<#if GCLKEN>
	pcr |= PMC_PCR_GCLKEN_Msk | PMC_PCR_GCLKCSS_${GCLKCSS} | PMC_PCR_GCLKDIV(${GCLKDIV} - 1);
		</#if>
    _PMC_REGS->PMC_PCR.w = pcr;
	</#if>
</#macro>

<#macro CONFIGURE_PCK INDEX ENABLED CSS PRES>
	<#if ENABLED>
    /* Setup Programmable Clock Generator ${INDEX} */
    _PMC_REGS->PMC_SCDR.w = PMC_SCDR_PCK(1 << ${INDEX});
	_PMC_REGS->PMC_PCK[${INDEX}].w = PMC_PCK_CSS_${CSS} | PMC_PCK_PRES(${PRES} - 1);
    _PMC_REGS->PMC_SCER.w = PMC_SCER_PCK(1 << ${INDEX});
	
	while( !(_PMC_REGS->PMC_SCSR.w & PMC_SCSR_PCK(1 << ${INDEX})))
    {
    }
	</#if>
</#macro>

// *****************************************************************************
/* Function:
    void CLK_Initialize ( void )

  Summary:
    Initializes hardware of the System Clock and Peripheral Clock.
    
  Description:
    This function initializes the hardware of System Clock and Peripheral Clocks.

  Parameters:
    None.

  Returns:
    None.

  Remarks:
    None.
*/

void CLK_Initialize( void )
{
#if 0
    uint32_t mckr;
<#if PMC_CKGR_MOR_MOSCRCEN>
    uint32_t mor;
</#if>
<#if PMC_PCR_EN0 || PMC_PCR_EN1 || PMC_PCR_GCLK0EN || PMC_PCR_GCLK1EN>
    uint32_t pcr;
</#if>
<#if PMC_SCER_USBCLK>
    uint32_t pmc_usb;
</#if>

    /* Set maximum possible Flash Wait States value */
    _EFC_REGS->EEFC_FMR.w = EEFC_FMR_FWS(6);
<#if SUPC_CR_XTALSEL>
    /* Slow Clock Setup */
	<#if SUPC_MR_OSCBYPASS>
    _SUPC_REGS->SUPC_MR.w |= SUPC_MR_OSCBYPASS_BYPASS;
	</#if>
	
	/* Select external crystal as source */
	_SUPC_REGS->SUPC_CR.w |= SUPC_CR_KEY_PASSWD | SUPC_CR_XTALSEL_CRYSTAL_SEL;

    while (_SUPC_REGS->SUPC_SR.OSCSEL == 0)
    {
    }
</#if>
    /* Main Clock Setup */
<#if PMC_CKGR_MOR_MOSCRCEN>
    /*Enables Main RC Oscillator */
    _PMC_REGS->CKGR_MOR.w |= CKGR_MOR_KEY_PASSWD | CKGR_MOR_MOSCRCEN_Msk;

    /* Polls whether Main RC oscillator is stabilized 
       after it is enabled. */
    while( !(_PMC_REGS->PMC_SR.w & PMC_SR_MOSCRCS_Msk) )
    {
    }
	
	/* Changes RC Oscillator frequency only if Main RC is stabilized */
    if( _PMC_REGS->PMC_SR.w & PMC_SR_MOSCRCS_Msk )
    {
        mor = _PMC_REGS->CKGR_MOR.w & ~(uint32_t)CKGR_MOR_MOSCRCF_Msk;
		mor |= CKGR_MOR_MOSCRCF${PMC_CKGR_MOR_MOSCRCF};
		
		_PMC_REGS->CKGR_MOR.w = mor;

        /* Polls whether Main RC oscillator is stabilized 
           after changing frequency. */
        while( !(_PMC_REGS->PMC_SR.w & PMC_SR_MOSCRCS_Msk) )
        {
        }
	}
</#if>
<#if PMC_CKGR_MOR_MOSCXTBY>
    /* Enables Main Crystal oscillator Bypass and
       clears the Main Crystal oscillator enable bit */
    _PMC_REGS->CKGR_MOR.w = CKGR_MOR_KEY_PASSWD | CKGR_MOR_MOSCXTBY_Msk | 
                            (_PMC_REGS->CKGR_MOR.w & ~(uint32_t)CKGR_MOR_MOSCXTEN_Msk);
<#elseif PMC_CKGR_MOR_MOSCXTEN>
    /* Enables the Main Crystal Oscillator and 
       sets the Main Crystal Oscillator Startup Time */
    _PMC_REGS->CKGR_MOR.w = CKGR_MOR_KEY_PASSWD | CKGR_MOR_MOSCXTST(${PMC_CKGR_MOR_MOSCXTST}) |
                            CKGR_MOR_MOSCXTEN_Msk | (_PMC_REGS->CKGR_MOR.w & ~(uint32_t)CKGR_MOR_MOSCXTST_Msk);

    while ( !(_PMC_REGS->PMC_SR.w & PMC_SR_MOSCXTS_Msk) )
    {
    }
</#if>
<#if PMC_CKGR_MOR_MOSCSEL>
    /* Selects the Main Crystal Oscillator */
    _PMC_REGS->CKGR_MOR.w |= CKGR_MOR_KEY_PASSWD | CKGR_MOR_MOSCSEL_Msk;

    while ( !(_PMC_REGS->PMC_SR.w & PMC_SR_MOSCSELS_Msk) )
    {
    }
</#if>
    /* configure PLLA */
<#if CLK_PLLA_ENABLE>
    _PMC_REGS->CKGR_PLLAR.w = CKGR_PLLAR_ONE_Msk | CKGR_PLLAR_PLLACOUNT(0x3f) |
                              CKGR_PLLAR_MULA(${PMC_CKGR_PLLAR_MULA} - 1) |
                              CKGR_PLLAR_DIVA(${PMC_CKGR_PLLAR_DIVA});

    while ( !(_PMC_REGS->PMC_SR.w & PMC_SR_LOCKA_Msk) )
    {
    }
<#else>
	_PMC_REGS->CKGR_PLLAR.w = CKGR_PLLAR_ONE_Msk | CKGR_PLLAR_PLLACOUNT(0) |
							CKGR_PLLAR_MULA(0) | CKGR_PLLAR_DIVA(0);
</#if>
    /* Master Clock Setup */
    mckr = _PMC_REGS->PMC_MCKR.w & ~(uint32_t)(PMC_MCKR_PRES_Msk | PMC_MCKR_MDIV_Msk);
	
	mckr |= PMC_MCKR_PRES_${PMC_MCKR_PRES} | PMC_MCKR_MDIV_${PMC_MCKR_MDIV};

	_PMC_REGS->PMC_MCKR.w = mckr;

    while ( !(_PMC_REGS->PMC_SR.w & PMC_SR_MCKRDY_Msk) )
    {
    }

    _PMC_REGS->PMC_MCKR.w = (mckr & ~(uint32_t)PMC_MCKR_CSS_Msk) | PMC_MCKR_CSS_${PMC_MCKR_CSS};

    while ( !(_PMC_REGS->PMC_SR.w & PMC_SR_MCKRDY_Msk) )
    {
    }
	
<#if PMC_CKGR_UCKR_UPLLEN>
    /* configure UPLL */
	/* Disable UPLL to get a predictable starting point */
    _PMC_REGS->CKGR_UCKR.w = 0;
	<#if UTMI_CKTRIM_FREQ == "XTAL12">
	_UTMI_REGS->UTMI_CKTRIM.w = UTMI_CKTRIM_FREQ_XTAL12;
	<#else>
	_UTMI_REGS->UTMI_CKTRIM.w = UTMI_CKTRIM_FREQ_XTAL16;
	</#if>
	<#if PMC_MCKR_UPLLDIV2>
	_PMC_REGS->PMC_MCKR.UPLLDIV2 = 1;
	<#else>
	_PMC_REGS->PMC_MCKR.UPLLDIV2 = 0;
	</#if>
	_PMC_REGS->CKGR_UCKR.w = CKGR_UCKR_UPLLEN_Msk | CKGR_UCKR_UPLLCOUNT(3);
    while (0 == (_PMC_REGS->PMC_SR.w & PMC_SR_LOCKU_Msk));
</#if>

<#if PMC_SCER_USBCLK>
    /* Setup Full-Speed USB clock output */
	_PMC_REGS->PMC_SCER.USBCLK = 0;
	
	pmc_usb = PMC_USB_USBDIV(${PMC_USB_USBDIV} - 1);

    <#if PMC_USB_USBS == "UPLL_CLK">
    pmc_usb |= PMC_USB_USBS_Msk;
    </#if>

    _PMC_REGS->PMC_USB.w = pmc_usb;
    _PMC_REGS->PMC_SCER.USBCLK = 1;
</#if>
    

<@CONFIGURE_GCLK 0 PMC_PCR_EN0 PMC_PCR_GCLK0EN PMC_PCR_GCLK0CSS PMC_PCR_GCLK0DIV />
<@CONFIGURE_GCLK 1 PMC_PCR_EN1 PMC_PCR_GCLK1EN PMC_PCR_GCLK1CSS PMC_PCR_GCLK1DIV />

<@CONFIGURE_PCK INDEX=0 ENABLED=PMC_SCER_PCK0 CSS=PMC_PCK0_CSS PRES=PMC_PCK0_PRES />
<@CONFIGURE_PCK INDEX=1 ENABLED=PMC_SCER_PCK1 CSS=PMC_PCK1_CSS PRES=PMC_PCK1_PRES />
<@CONFIGURE_PCK INDEX=2 ENABLED=PMC_SCER_PCK2 CSS=PMC_PCK2_CSS PRES=PMC_PCK2_PRES />
<@CONFIGURE_PCK INDEX=3 ENABLED=PMC_SCER_PCK3 CSS=PMC_PCK3_CSS PRES=PMC_PCK3_PRES />
<@CONFIGURE_PCK INDEX=4 ENABLED=PMC_SCER_PCK4 CSS=PMC_PCK4_CSS PRES=PMC_PCK4_PRES />
<@CONFIGURE_PCK INDEX=5 ENABLED=PMC_SCER_PCK5 CSS=PMC_PCK5_CSS PRES=PMC_PCK5_PRES />
<@CONFIGURE_PCK INDEX=6 ENABLED=PMC_SCER_PCK6 CSS=PMC_PCK6_CSS PRES=PMC_PCK6_PRES />
<#--@CONFIGURE_PCK INDEX=7 ENABLED=PMC_SCER_PCK7 CSS=PMC_PCK7_CSS PRES=PMC_PCK7_PRES /-->

    /* - Enable the peripheral clock selected by MHC/peripheral driver */
   	_PMC_REGS->PMC_PCER0.w=${PMC_PCER0};
    _PMC_REGS->PMC_PCER1.w=${PMC_PCER1};
	
#endif
}


<#--
/*******************************************************************************
 End of File
*/
-->
