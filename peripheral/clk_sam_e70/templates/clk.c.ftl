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

#include "${__PROCESSOR?lower_case}.h"
#include "clk.h"

<#macro CONFIGURE_GCLK INDEX PCLKEN GCLKEN GCLKCSS GCLKDIV>
	<#if PCLKEN || GCLKEN>
	/* Setup Generic/Peripheral Clock for I2S${INDEX} */
    regValue = PMC_PCR_CMD_Msk ${PCLKEN?then('| PMC_PCR_EN_Msk', '')}  ${GCLKEN?then('| PMC_PCR_GCLKEN_Msk | PMC_PCR_GCLKCSS_${GCLKCSS} | PMC_PCR_GCLKDIV(${GCLKDIV} - 1)', '')};
	    <#if INDEX == 0>
	regValue |= PMC_PCR_PID(69);
	    <#else>
	regValue |= PMC_PCR_PID(70);
	    </#if>
    PMC_REGS->PMC_PCR = regValue;
	</#if>
</#macro>

<#macro CONFIGURE_PCK INDEX ENABLED CSS PRES>
	<#if ENABLED>
    /* Configure Programmable Clock Generator ${INDEX} Clock Source and Clock Divider */
    PMC_REGS->PMC_SCDR = (1 << ${INDEX}) << PMC_SCDR_PCK_Pos;
	PMC_REGS->PMC_PCK[${INDEX}]= PMC_PCK_CSS_${CSS} | PMC_PCK_PRES(${PRES} - 1);
    PMC_REGS->PMC_SCER = (1 << ${INDEX}) << PMC_SCER_PCK_Pos;
	
   /* Wait until PCK${INDEX} clock output is ready */
    while( !(PMC_REGS->PMC_SR& ((1 << ${INDEX}) << PMC_SR_PCKRDY_Pos) ) )
    {
    }
	
	</#if>
</#macro>

<#if SUPC_CR_XTALSEL>
// *****************************************************************************
/* Function:
    void CLK_SlowClockInitialize ( void )

  Summary:
    Initializes hardware of the Slow Clock.
    
  Description:
    This function initializes the hardware of Slow Clock.

  Parameters:
    None.

  Returns:
    None.

  Remarks:
    None.
*/

static void CLK_SlowClockInitialize(void)
{
<#if SUPC_MR_OSCBYPASS && SUPC_CR_XTALSEL>
    /* External clock signal on XIN32 pin is selected as the Slow Clock (SLCK) source.
	   Bypass 32K Crystal Oscillator  */
    SUPC_REGS->SUPC_MR|= SUPC_MR_OSCBYPASS_BYPASS;
	SUPC_REGS->SUPC_CR|= SUPC_CR_KEY_PASSWD | SUPC_CR_XTALSEL_CRYSTAL_SEL;
	
	/* Wait until the external clock signal is ready and 
	   Slow Clock (SLCK) is switched to external clock signal */
    while (!(SUPC_REGS->SUPC_SR&SUPC_SR_OSCSEL_Msk) &&  !(PMC_REGS->PMC_SR& PMC_SR_MOSCRCS_Msk))
    {
    }
	
<#elseif SUPC_CR_XTALSEL>
	/* 32KHz Crystal Oscillator is selected as the Slow Clock (SLCK) source.
	   Enable 32KHz Crystal Oscillator  */
	SUPC_REGS->SUPC_CR|= SUPC_CR_KEY_PASSWD | SUPC_CR_XTALSEL_CRYSTAL_SEL;
	
	/* Wait until the 32K Crystal oscillator clock is ready and 
	   Slow Clock (SLCK) is switched to 32KHz Oscillator */
    while (!(SUPC_REGS->SUPC_SR&SUPC_SR_OSCSEL_Msk) &&  !(PMC_REGS->PMC_SR& PMC_SR_MOSCRCS_Msk))
    {
    }
</#if>
}
</#if>

// *****************************************************************************
/* Function:
    void CLK_MainClockInitialize ( void )

  Summary:
    Initializes hardware of the Main Clock.
    
  Description:
    This function initializes the hardware of Main Clock.

  Parameters:
    None.

  Returns:
    None.

  Remarks:
    None.
*/

static void CLK_MainClockInitialize(void)
{
    uint32_t regValue;
	
<#if PMC_CKGR_MOR_MOSCRCEN >
    /* Enable the RC Oscillator */
	PMC_REGS->CKGR_MOR|= CKGR_MOR_KEY_PASSWD | CKGR_MOR_MOSCRCEN_Msk;

    /* Wait until the RC oscillator clock is ready. */
    while( !(PMC_REGS->PMC_SR& PMC_SR_MOSCRCS_Msk) )
    {
    }
	
	/* Configure the RC Oscillator frequency */
    regValue = PMC_REGS->CKGR_MOR& ~(uint32_t)CKGR_MOR_MOSCRCF_Msk;
	regValue |= CKGR_MOR_KEY_PASSWD | CKGR_MOR_MOSCRCF_${PMC_CKGR_MOR_MOSCRCF};
	PMC_REGS->CKGR_MOR = regValue;

    /* Wait until the RC oscillator clock is ready */
    while( !(PMC_REGS->PMC_SR& PMC_SR_MOSCRCS_Msk) )
    {
    }

	<#if !PMC_CKGR_MOR_MOSCSEL>
	/* Main RC Oscillator is selected as the Main Clock (MAINCK) source. 
	   Switch Main Clock (MAINCK) to the RC Oscillator clock */
	regValue = 	PMC_REGS->CKGR_MOR& ~CKGR_MOR_MOSCSEL_Msk;
    PMC_REGS->CKGR_MOR = regValue | CKGR_MOR_KEY_PASSWD;
	</#if>
</#if>

<#if PMC_CKGR_MOR_MOSCXTBY>
    /* Disable Main Crystal Oscillator and Enable External Clock Signal on XIN pin  */
	regValue = PMC_REGS->CKGR_MOR& ~(uint32_t)CKGR_MOR_MOSCXTEN_Msk;
	regValue |=CKGR_MOR_KEY_PASSWD | CKGR_MOR_MOSCXTBY_Msk;
    PMC_REGS->CKGR_MOR = regValue;

	<#if PMC_CKGR_MOR_MOSCSEL>
	 /* External clock signal (XIN pin) is selected as the Main Clock (MAINCK) source.
	    Switch Main Clock (MAINCK) to External signal on XIN pin */
    PMC_REGS->CKGR_MOR|= CKGR_MOR_KEY_PASSWD | CKGR_MOR_MOSCSEL_Msk;

	/* Wait until MAINCK is switched to External Clock Signal (XIN pin) */
    while ( !(PMC_REGS->PMC_SR& PMC_SR_MOSCSELS_Msk) )
    {
    }
	</#if>
	
<#elseif PMC_CKGR_MOR_MOSCXTEN>
    /* Enable Main Crystal Oscillator */
	regValue = PMC_REGS->CKGR_MOR& ~(uint32_t)CKGR_MOR_MOSCXTST_Msk;
	regValue |= CKGR_MOR_KEY_PASSWD | CKGR_MOR_MOSCXTST(${PMC_CKGR_MOR_MOSCXTST}) | CKGR_MOR_MOSCXTEN_Msk;
    PMC_REGS->CKGR_MOR = regValue;

	/* Wait until the main oscillator clock is ready */
    while ( !(PMC_REGS->PMC_SR& PMC_SR_MOSCXTS_Msk) )
    {
    }
	
	<#if PMC_CKGR_MOR_MOSCSEL>
    /* Main Crystal Oscillator is selected as the Main Clock (MAINCK) source. 
	Switch Main Clock (MAINCK) to Main Crystal Oscillator clock */
    PMC_REGS->CKGR_MOR|= CKGR_MOR_KEY_PASSWD | CKGR_MOR_MOSCSEL_Msk;

	/* Wait until MAINCK is switched to Main Crystal Oscillator */
    while ( !(PMC_REGS->PMC_SR& PMC_SR_MOSCSELS_Msk) )
    {
    }
	</#if>
</#if>
}

// *****************************************************************************
/* Function:
    void CLK_PLLAInitialize ( void )

  Summary:
    Initializes hardware of PLLA.
    
  Description:
    This function initializes the hardware of PLLA.

  Parameters:
    None.

  Returns:
    None.

  Remarks:
    None.
*/

static void CLK_PLLAInitialize(void)
{
    /* configure PLLA */
<#if CLK_PLLA_ENABLE>
    PMC_REGS->CKGR_PLLAR = CKGR_PLLAR_ONE_Msk | CKGR_PLLAR_PLLACOUNT(0x3f) |
                              CKGR_PLLAR_MULA(${PMC_CKGR_PLLAR_MULA} - 1) |
                              CKGR_PLLAR_DIVA(${PMC_CKGR_PLLAR_DIVA});

    while ( !(PMC_REGS->PMC_SR& PMC_SR_LOCKA_Msk) )
    {
    }
<#else>
	PMC_REGS->CKGR_PLLAR = CKGR_PLLAR_ONE_Msk | CKGR_PLLAR_PLLACOUNT(0) |
							CKGR_PLLAR_MULA(0) | CKGR_PLLAR_DIVA(0);
</#if>
}

<#if PMC_CKGR_UCKR_UPLLEN>
// *****************************************************************************
/* Function:
    void CLK_USBClockInitialize ( void )

  Summary:
    Initializes hardware of the USB Clock.
    
  Description:
    This function initializes the hardware of USB Clock.

  Parameters:
    None.

  Returns:
    None.

  Remarks:
    None.
*/

static void CLK_UTMIPLLInitialize(void)
{
	/* Configure Crystal Clock Frequency (12MHz or 16MHz) to select USB PLL (UPLL) multiplication factor
       UPLL multiplication factor is x40 to generate 480MHz from 12MHz
       UPLL multiplication factor is x30 to generate 480MHz from 16MHz	   */
	<#if UTMI_CKTRIM_FREQ == "XTAL12">
	UTMI_REGS->UTMI_CKTRIM= UTMI_CKTRIM_FREQ_XTAL12;
	<#else>
	UTMI_REGS->UTMI_CKTRIM= UTMI_CKTRIM_FREQ_XTAL16;
	</#if>
	
	/* Enable UPLL and configure UPLL lock time */
	PMC_REGS->CKGR_UCKR = CKGR_UCKR_UPLLEN_Msk | CKGR_UCKR_UPLLCOUNT(0x3F);
	
	/* Wait until PLL Lock occurs */
    while (0 == (PMC_REGS->PMC_SR& PMC_SR_LOCKU_Msk));
	
	<#if PMC_MCKR_UPLLDIV2>
	/* UPLL clock frequency is 240Mhz (Divider=2) */
	PMC_REGS->PMC_MCKR|= PMC_MCKR_UPLLDIV2_Msk;
	<#else>
	/* UPLL clock frequency is 480MHz (Divider=1) */
	PMC_REGS->PMC_MCKR&= ~PMC_MCKR_UPLLDIV2_Msk;
	</#if>
	
	/* Wait until clock is ready */
    while ( !(PMC_REGS->PMC_SR& PMC_SR_MCKRDY_Msk) )
    {
    }
}
</#if>

// *****************************************************************************
/* Function:
    void CLK_MasterClockInitialize ( void )

  Summary:
    Initializes hardware of the Master Clock.
    
  Description:
    This function initializes the hardware of Master Clock.

  Parameters:
    None.

  Returns:
    None.

  Remarks:
    None.
*/

static void CLK_MasterClockInitialize(void)
{
    uint32_t regValue;
<#if PMC_MCKR_CSS == "PLLA_CLK" || PMC_MCKR_CSS == "UPLL_CLK">
	/* Master Clock Configuration when PLL clock is selected as clock source
       a. Program PMC_MCKR.PRES.
       b. Wait for PMC_SR.MCKRDY to be set.
       c. Program PMC_MCKR.MDIV.
       d. Wait for PMC_SR.MCKRDY to be set.
       e. Program PMC_MCKR.CSS.
       f. Wait for PMC_SR.MCKRDY to be set.   */
	   
	regValue = PMC_REGS->PMC_MCKR& ~PMC_MCKR_PRES_Msk;
	regValue|= PMC_MCKR_PRES_${PMC_MCKR_PRES};
    PMC_REGS->PMC_MCKR = regValue;
	
    while ( !(PMC_REGS->PMC_SR& PMC_SR_MCKRDY_Msk) )
    {
    }
	
	regValue = PMC_REGS->PMC_MCKR& ~PMC_MCKR_MDIV_Msk;
	regValue|= PMC_MCKR_MDIV_${PMC_MCKR_MDIV};
    PMC_REGS->PMC_MCKR = regValue;	
	
    while ( !(PMC_REGS->PMC_SR& PMC_SR_MCKRDY_Msk) )
    {
    }

	regValue = PMC_REGS->PMC_MCKR& ~PMC_MCKR_CSS_Msk;
	regValue|= PMC_MCKR_CSS_${PMC_MCKR_CSS};
    PMC_REGS->PMC_MCKR = regValue;
	
    while ( !(PMC_REGS->PMC_SR& PMC_SR_MCKRDY_Msk) )
    {
    }	
</#if>
<#if PMC_MCKR_CSS == "SLOW_CLK" || PMC_MCKR_CSS == "MAIN_CLK">
	/* 	Master Clock Configuration when Slow clock or Main Clock is Selected as Clock Source
		a. Program PMC_MCKR.CSS.
		b. Wait for PMC_SR.MCKRDY to be set.
		c. Program PMC_MCKR.PRES.
		d. Wait for PMC_SR.MCKRDY to be set. 
        e. Program PMC_MCKR.MDIV.
        f. Wait for PMC_SR.MCKRDY to be set.	*/
		
	regValue = PMC_REGS->PMC_MCKR& ~PMC_MCKR_CSS_Msk;
	regValue|= PMC_MCKR_CSS_${PMC_MCKR_CSS};
    PMC_REGS->PMC_MCKR = regValue;
	
    while ( !(PMC_REGS->PMC_SR& PMC_SR_MCKRDY_Msk) )
    {
    }			

		regValue = PMC_REGS->PMC_MCKR& ~PMC_MCKR_PRES_Msk;
	regValue|= PMC_MCKR_PRES_${PMC_MCKR_PRES};
    PMC_REGS->PMC_MCKR = regValue;
	
    while ( !(PMC_REGS->PMC_SR& PMC_SR_MCKRDY_Msk) )
    {
    }

	regValue = PMC_REGS->PMC_MCKR& ~PMC_MCKR_MDIV_Msk;
	regValue|= PMC_MCKR_MDIV_${PMC_MCKR_MDIV};
    PMC_REGS->PMC_MCKR = regValue;	
	
    while ( !(PMC_REGS->PMC_SR& PMC_SR_MCKRDY_Msk) )
    {
    }	
</#if>
}

<#if PMC_SCER_USBCLK>

// *****************************************************************************
/* Function:
    void CLK_USBClockInitialize ( void )

  Summary:
    Initializes hardware of the USB Clock.
    
  Description:
    This function initializes the hardware of USB Clock.

  Parameters:
    None.

  Returns:
    None.

  Remarks:
    None.
*/

static void CLK_USBClockInitialize ( void )
{    
    uint32_t regValue;
	
    /* Configure Full-Speed USB Clock source and Clock Divider */
	regValue = PMC_USB_USBDIV(${PMC_USB_USBDIV} - 1);
    <#if PMC_USB_USBS == "UPLL_CLK">
    regValue |= PMC_USB_USBS_Msk;
    </#if>
    PMC_REGS->PMC_USB= regValue;
	
	/* Enable Full-Speed USB Clock Output */
    PMC_REGS->PMC_SCER = PMC_SCER_USBCLK_Msk;
}
</#if>

<#if PMC_PCR_GCLK0EN || PMC_PCR_EN0 || PMC_PCR_GCLK1EN || PMC_PCR_EN1>
// *****************************************************************************
/* Function:
    void CLK_GenericClockInitialize ( void )

  Summary:
    Initializes hardware of the Generic Clock.
    
  Description:
    This function initializes the hardware of Generic Clock.

  Parameters:
    None.

  Returns:
    None.

  Remarks:
    None.
*/

static void CLK_GenericClockInitialize(void)
{
    uint32_t regValue;

<@CONFIGURE_GCLK 0 PMC_PCR_EN0 PMC_PCR_GCLK0EN PMC_PCR_GCLK0CSS PMC_PCR_GCLK0DIV />
<@CONFIGURE_GCLK 1 PMC_PCR_EN1 PMC_PCR_GCLK1EN PMC_PCR_GCLK1CSS PMC_PCR_GCLK1DIV />
}
</#if>

<#if PMC_SCER_PCK0 || PMC_SCER_PCK1 || PMC_SCER_PCK2 || PMC_SCER_PCK3 ||
     PMC_SCER_PCK4 || PMC_SCER_PCK5 || PMC_SCER_PCK6 || PMC_SCER_PCK7>
// *****************************************************************************
/* Function:
    void CLK_ProgrammableClockInitialize ( void )

  Summary:
    Initializes hardware of the Programmable Clock.
    
  Description:
    This function initializes the hardware of Programmable Clock.

  Parameters:
    None.

  Returns:
    None.

  Remarks:
    None.
*/

static void CLK_ProgrammableClockInitialize(void)
{
<@CONFIGURE_PCK INDEX=0 ENABLED=PMC_SCER_PCK0 CSS=PMC_PCK0_CSS PRES=PMC_PCK0_PRES />
<@CONFIGURE_PCK INDEX=1 ENABLED=PMC_SCER_PCK1 CSS=PMC_PCK1_CSS PRES=PMC_PCK1_PRES />
<@CONFIGURE_PCK INDEX=2 ENABLED=PMC_SCER_PCK2 CSS=PMC_PCK2_CSS PRES=PMC_PCK2_PRES />
<@CONFIGURE_PCK INDEX=3 ENABLED=PMC_SCER_PCK3 CSS=PMC_PCK3_CSS PRES=PMC_PCK3_PRES />
<@CONFIGURE_PCK INDEX=4 ENABLED=PMC_SCER_PCK4 CSS=PMC_PCK4_CSS PRES=PMC_PCK4_PRES />
<@CONFIGURE_PCK INDEX=5 ENABLED=PMC_SCER_PCK5 CSS=PMC_PCK5_CSS PRES=PMC_PCK5_PRES />
<@CONFIGURE_PCK INDEX=6 ENABLED=PMC_SCER_PCK6 CSS=PMC_PCK6_CSS PRES=PMC_PCK6_PRES />
<@CONFIGURE_PCK INDEX=7 ENABLED=PMC_SCER_PCK7 CSS=PMC_PCK7_CSS PRES=PMC_PCK7_PRES />
}
</#if>
// *****************************************************************************
/* Function:
    void CLK_PeripheralClockInitialize ( void )

  Summary:
    Initializes hardware of the Peripheral Clock.
    
  Description:
    This function initializes the hardware of Peripheral Clock.

  Parameters:
    None.

  Returns:
    None.

  Remarks:
    None.
*/

static void CLK_PeripheralClockInitialize(void)
{
    /* - Enable the peripheral clock selected by MHC/peripheral driver */
   	PMC_REGS->PMC_PCER0=${PMC_PCER0};
    PMC_REGS->PMC_PCER1=${PMC_PCER1};
}

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
    /* Set Flash Wait States and 
       Enable Code Loop Optimization */
    EFC_REGS->EEFC_FMR = EEFC_FMR_FWS(${EEFC_FMR_FWS}) | EEFC_FMR_CLOE_Msk;
	
<#if SUPC_CR_XTALSEL>
	/* Initialize Slow Clock */
	CLK_SlowClockInitialize();
</#if>

	/* Initialize Main Clock */
	CLK_MainClockInitialize();
	
	/* Initialize PLLA */
	CLK_PLLAInitialize();
	
<#if PMC_CKGR_UCKR_UPLLEN>
	/* Initialize UTMI PLL */
	CLK_UTMIPLLInitialize();
</#if>

	/* Initialize Master Clock */
	CLK_MasterClockInitialize();
	
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

	/* Initialize Peripheral Clock */
	CLK_PeripheralClockInitialize();
}

<#--
/*******************************************************************************
 End of File
*/
-->
