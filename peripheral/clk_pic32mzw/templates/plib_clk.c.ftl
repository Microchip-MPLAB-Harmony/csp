/*******************************************************************************
  SYS CLK Static Functions for Clock System Service

  Company:
    Microchip Technology Inc.

  File Name:
    plib_clk.c

  Summary:
    SYS CLK static function implementations for the Clock System Service.

  Description:
    The Clock System Service provides a simple interface to manage the
    oscillators on Microchip microcontrollers. This file defines the static
    implementation for the Clock System Service.

  Remarks:
    Static functions incorporate all system clock configuration settings as
    determined by the user via the Microchip Harmony Configurator GUI.
    It provides static version of the routines, eliminating the need for an
    object ID or object handle.

    Static single-open interfaces also eliminate the need for the open handle.

*******************************************************************************/

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

// *****************************************************************************
// *****************************************************************************
// Section: Include Files
// *****************************************************************************
// *****************************************************************************

#include "device.h"
#include "plib_clk.h"

// *****************************************************************************
// *****************************************************************************
// Section: File Scope Functions
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Function:
    void CLK_Initialize( void )

  Summary:
    Initializes hardware and internal data structure of the System Clock.

  Description:
    This function initializes the hardware and internal data structure of System
    Clock Service.

  Remarks:
    This is configuration values for the static version of the Clock System
    Service module is determined by the user via the MHC GUI.

    The objective is to eliminate the user's need to be knowledgeable in the
    function of the 'configuration bits' to configure the system oscillators.
*/

#define EWPLLCON_MSK 0x0438080c
#define EWPLL_PWRON 0x808

static void DelayMs ( uint32_t delay_ms)
{
    uint32_t startCount, endCount;
    /* Calculate the end count for the given delay */
    endCount=(CORE_TIMER_FREQ/1000)*delay_ms;
    startCount=_CP0_GET_COUNT();
    while((_CP0_GET_COUNT()-startCount)<endCount);
}

 void wifi_spi_write(unsigned int spi_addr, unsigned int data)
{
    unsigned int  addr_bit, data_bit, bit_idx;
    unsigned int cs_high, clk_high, en_bit_bang;
    unsigned int *wifi_spi_ctrl_reg = (unsigned int *)0xBF8C8028;
    clk_high = 0x1 ;
    cs_high  = 0x2;
    en_bit_bang  = 0x1 << 31;
    addr_bit = 0; data_bit = 0;

    *wifi_spi_ctrl_reg = en_bit_bang | cs_high ;
    *wifi_spi_ctrl_reg = (en_bit_bang | cs_high | clk_high );
     *wifi_spi_ctrl_reg = (en_bit_bang);
     *wifi_spi_ctrl_reg = (en_bit_bang | clk_high);

    for (bit_idx=0;bit_idx<=7;bit_idx++) {
        addr_bit = (spi_addr>>(7-bit_idx)) & 0x1;
        *wifi_spi_ctrl_reg = (en_bit_bang | (addr_bit << 2 ));               // Falling edge of clk
        *wifi_spi_ctrl_reg = (en_bit_bang | (addr_bit << 2 ) | clk_high);    // Rising edge of clk
    }

    for (bit_idx=0;bit_idx<=15;bit_idx++) {
        data_bit = (data>>(15-bit_idx)) & 0x1;
        *wifi_spi_ctrl_reg = (en_bit_bang | (data_bit << 2 ));                // Falling edge of clk with data bit
        *wifi_spi_ctrl_reg = (en_bit_bang | (data_bit << 2 ) | clk_high);     // Rising edge of clk
    }

    *wifi_spi_ctrl_reg = (en_bit_bang | cs_high | clk_high); // Rising edge of clk
    *wifi_spi_ctrl_reg = 0;                                // Set the RF override bit and CS_n high
}

unsigned int wifi_spi_read(unsigned int spi_addr)
{
    unsigned int  addr_bit, bit_idx, read_data;
    unsigned int cs_high, clk_high, cmd_high, en_bit_bang;
    unsigned int *wifi_spi_ctrl_reg = (unsigned int *)0xBF8C8028;

    clk_high = 0x1 ;
    cs_high  = 0x2;
    cmd_high = 0x8;
    en_bit_bang  = 0x1 << 31;
    addr_bit = 0;


    *wifi_spi_ctrl_reg = (en_bit_bang | cs_high);            // Set the RF override bit and CS_n high
    *wifi_spi_ctrl_reg = (en_bit_bang | cs_high | clk_high); // Rising edge of clk
    *wifi_spi_ctrl_reg = ((en_bit_bang)| cmd_high | (0x1 << 2));                // Falling edge of clk with CS going low and command bit 1
    *wifi_spi_ctrl_reg = ((en_bit_bang | cmd_high | (0x1 << 2) | clk_high));     // Falling edge of clk with CS going low and command bit 1

    for (bit_idx=0;bit_idx<=7;bit_idx++) {
        addr_bit = (spi_addr>>(7-bit_idx)) & 0x1;
        *wifi_spi_ctrl_reg = ((en_bit_bang | cmd_high | (addr_bit << 2 )));               // Falling edge of clk
        *wifi_spi_ctrl_reg =((en_bit_bang | cmd_high | (addr_bit << 2 ) | clk_high));    // Rising edge of clk
    }

    for (bit_idx=0;bit_idx<=16;bit_idx++) {
        *wifi_spi_ctrl_reg = ((en_bit_bang | cmd_high ));               // Falling edge of clk
        *wifi_spi_ctrl_reg = ((en_bit_bang | cmd_high | clk_high));     // Rising edge of clk
    }

    *wifi_spi_ctrl_reg = 0;                                // Set the RF override bit and CS_n high

    read_data = *wifi_spi_ctrl_reg ; //soc_reg_rd(0xBF8C8130,15,0) & 0xFFFF;
    return read_data;
}

void CLK_Initialize( void )
{
    volatile unsigned int *PLLDBG = (unsigned int*) 0xBF8000E0;
    volatile unsigned int *PMDRCLR = (unsigned int *) 0xBF8000B4;
	volatile unsigned int *RFSPICTL = (unsigned int *) 0xBF8C8028;

    /* unlock system for clock configuration */
    SYSKEY = 0x00000000;
    SYSKEY = 0xAA996655;
    SYSKEY = 0x556699AA;

    if(((DEVID & 0x0FF00000) >> 20) == PIC32MZW1_B0)
    {
        if((!CLKSTATbits.SPLLRDY && RCONbits.POR == 1 && RCONbits.EXTR == 1)
            || (1 == CLKSTATbits.SPLLRDY && 0 == RCONbits.POR &&
            ((1 == RCONbits.EXTR) || (1 == RCONbits.SWR))))
		{
			EWPLLCON = 0x808; // Start with PWR-OFF PLL
			SPLLCON  = 0x808; // Start with PWR-OFF PLL
			DelayMs(5);

			CFGCON2  |= 0x300; // Start with POSC Turned OFF
			/* if POSC was on give some time for POSC to shut off */
			DelayMs(5);
			/* make sure we properly reset SPI to a known state */
			*RFSPICTL = 0x80000022;
			/* make sure we properly take out of reset */
			*RFSPICTL = 0x80000002;

			if(1 == DEVIDbits.VER)
			{
                wifi_spi_write(0x85, 0x00F2); /* MBIAS filter and A31 analog_test */
                wifi_spi_write(0x84, 0x0001); /* A31 Analog test */
                wifi_spi_write(0x1e, 0x510); /* MBIAS reference adjustment */
                wifi_spi_write(0x82, 0x6000); /* XTAL LDO feedback divider (1.3+v) */
			}
			else
            {
                wifi_spi_write(0x85, 0x00F0); /* MBIAS filter and A31 analog_test */
                wifi_spi_write(0x84, 0x0001); /* A31 Analog test */
                wifi_spi_write(0x1e, 0x510); /* MBIAS reference adjustment */
                wifi_spi_write(0x82, 0x6400); /* XTAL LDO feedback divider (1.3+v) */
			}
            DelayMs(2);
			/* Enable POSC */
			CFGCON2  &= 0xFFFFFCFF; // enable POSC
			DelayMs(5);

			/*Configure SPLL*/
			${CFGCON3_NAME} = ${CFGCON3_VALUE};
			CFGCON0bits.SPLLHWMD = 1;

			/* SPLLBSWSEL   = ${SPLLCON_SPLLBSWSEL_VALUE}   */
			/* SPLLPWDN     = ${SPLLCON_SPLLPWDN_VALUE}     */
			/* SPLLPOSTDIV1 = ${SPLLCON_SPLLPOSTDIV1_VALUE} */
			/* SPLLFLOCK    = ${SPLLCON_SPLLFLOCK_VALUE}    */
			/* SPLLRST      = ${SPLLCON_SPLLRST_VALUE}      */
			/* SPLLFBDIV    = ${SPLLCON_SPLLFBDIV_VALUE}  */
			/* SPLLREFDIV   = ${SPLLCON_SPLLREFDIV_VALUE}   */
			/* SPLLICLK     = ${SPLLCON_SPLLICLK_VALUE}     */
			/* SPLL_BYP     = ${SPLLCON_SPLL_BYP_VALUE}     */
			${SPLLCON_REG} = 0x${SPLLCON_VALUE};

			/* OSWEN    = ${OSCCON_OSWEN_VALUE}    */
			/* SOSCEN   = ${OSCCON_SOSCEN_VALUE}   */
			/* UFRCEN   = ${OSCCON_UFRCEN_VALUE}   */
			/* CF       = ${OSCCON_CF_VALUE}       */
			/* SLPEN    = ${OSCCON_SLPEN_VALUE}    */
			/* CLKLOCK  = ${OSCCON_CLKLOCK_VALUE}  */
			/* NOSC     = ${OSCCON_NOSC_VALUE}     */
			/* WAKE2SPD = ${OSCCON_WAKE2SPD_VALUE} */
			/* DRMEN    = ${OSCCON_DRMEN_VALUE}    */
			/* FRCDIV   = ${OSCCON_FRCDIV_VALUE}   */
			${OSCCON_REG} = 0x${OSCCON_VALUE};

			OSCCONSET = _OSCCON_OSWEN_MASK;  /* request oscillator switch to occur */

			while( OSCCONbits.OSWEN );
			/****************************************************************
			* check to see if PLL locked; indicates POSC must have started
			*****************************************************************/
			if(0 == (*PLLDBG & 0x1))
			{
				/*POSC failed to start!*/
				while(1);
			}
			if(1 == DEVIDbits.VER)
			{
				/*Disabling internal schmitt-trigger to increase noise immunity */
				wifi_spi_write(0x85, 0x00F4);
			}
<#if APP_RECONFIG_SPLL??>
/* Leaving this disabled as there is no absolute use-case as yet.
 * Placeholder for cases where a bootloader uses a different frequency
 * compared to the application code.
*/
            OSCCONbits.NOSC = 0; //Select FRC as SYS_CLK source
            OSCCONSET = _OSCCON_OSWEN_MASK;  /* request oscillator switch to occur */
            while( OSCCONbits.OSWEN );

            SPLLCON  = 0x808; // Start with PWR-OFF PLL

            /*Configure SPLL*/
			${CFGCON3_NAME} = ${CFGCON3_VALUE};
			CFGCON0bits.SPLLHWMD = 1;

			/* SPLLBSWSEL   = ${SPLLCON_SPLLBSWSEL_VALUE}   */
			/* SPLLPWDN     = ${SPLLCON_SPLLPWDN_VALUE}     */
			/* SPLLPOSTDIV1 = ${SPLLCON_SPLLPOSTDIV1_VALUE} */
			/* SPLLFLOCK    = ${SPLLCON_SPLLFLOCK_VALUE}    */
			/* SPLLRST      = ${SPLLCON_SPLLRST_VALUE}      */
			/* SPLLFBDIV    = ${SPLLCON_SPLLFBDIV_VALUE}  */
			/* SPLLREFDIV   = ${SPLLCON_SPLLREFDIV_VALUE}   */
			/* SPLLICLK     = ${SPLLCON_SPLLICLK_VALUE}     */
			/* SPLL_BYP     = ${SPLLCON_SPLL_BYP_VALUE}     */
			${SPLLCON_REG} = 0x${SPLLCON_VALUE};

			/* OSWEN    = ${OSCCON_OSWEN_VALUE}    */
			/* SOSCEN   = ${OSCCON_SOSCEN_VALUE}   */
			/* UFRCEN   = ${OSCCON_UFRCEN_VALUE}   */
			/* CF       = ${OSCCON_CF_VALUE}       */
			/* SLPEN    = ${OSCCON_SLPEN_VALUE}    */
			/* CLKLOCK  = ${OSCCON_CLKLOCK_VALUE}  */
			/* NOSC     = ${OSCCON_NOSC_VALUE}     */
			/* WAKE2SPD = ${OSCCON_WAKE2SPD_VALUE} */
			/* DRMEN    = ${OSCCON_DRMEN_VALUE}    */
			/* FRCDIV   = ${OSCCON_FRCDIV_VALUE}   */
			${OSCCON_REG} = 0x${OSCCON_VALUE};
            OSCCONSET = _OSCCON_OSWEN_MASK;  /* request oscillator switch to occur */
			while( OSCCONbits.OSWEN );

            /****************************************************************
			* check to see if PLL locked; indicates POSC must have started
			*****************************************************************/
            if(0 == (*PLLDBG & 0x1))
			{
				/*POSC failed to start!*/
				while(1);
			}
</#if>
		}
<#if EWPLL_ENABLE == true>
		/* Configure EWPLL */
		/* EWPLLBSWSEL   = ${EWPLLCON_EWPLLBSWSEL_VALUE} */
		/* EWPLLPWDN     = ${EWPLLCON_EWPLLPWDN_VALUE} */
		/* EWPLLPOSTDIV1 = ${EWPLLCON_EWPLLPOSTDIV1_VALUE} */
		/* EWPLLFLOCK    = ${EWPLLCON_EWPLLFLOCK_VALUE} */
		/* EWPLLRST      = ${EWPLLCON_EWPLLRST_VALUE} */
		/* EWPLLFBDIV    = ${EWPLLCON_EWPLLFBDIV_VALUE} */
		/* EWPLLREFDIV   = ${EWPLLCON_EWPLLREFDIV_VALUE} */
		/* EWPLLICLK     = ${EWPLLCON_EWPLLICLK_VALUE} */
		/* ETHCLKOUTEN   = ${EWPLLCON_ETHCLKOUTEN_VALUE} */
		/* EWPLL_BYP     = ${EWPLLCON_EWPLL_BYP_VALUE} */
		${EWPLLCON_REG} = 0x${EWPLLCON_VALUE} ^ EWPLLCON_MSK;
		DelayMs(1);
		${EWPLLCON_REG} &= ~EWPLL_PWRON;
		/****************************************************************
		* check to see if PLL locked; indicates POSC must have started
		*****************************************************************/
		if(0 == (*PLLDBG & 0x5))
		{
			/*POSC failed to start!*/
			while(1);
		}
<#else>
		/* Power down the EWPLL */
		EWPLLCONbits.EWPLLPWDN = 1;
</#if>

<#if USBPLL_ENABLE == true>
		/* Configure UPLL */
		/* UPLLBSWSEL   = ${UPLLCON_UPLLBSWSEL_VALUE} */
		/* UPLLPWDN     = ${UPLLCON_UPLLPWDN_VALUE} */
		/* UPLLPOSTDIV1 = ${UPLLCON_UPLLPOSTDIV1_VALUE} */
		/* UPLLFLOCK    = ${UPLLCON_UPLLFLOCK_VALUE} */
		/* UPLLRST      = ${UPLLCON_UPLLRST_VALUE} */
		/* UPLLFBDIV    = ${UPLLCON_UPLLFBDIV_VALUE} */
		/* UPLLREFDIV   = ${UPLLCON_UPLLREFDIV_VALUE} */
		/* UPLL_BYP     = ${UPLLCON_UPLL_BYP_VALUE} */
		${UPLLCON_REG} = 0x${UPLLCON_VALUE};
<#else>
		/* Power down the UPLL */
		UPLLCONbits.UPLLPWDN = 1;
</#if>

<#if BTPLL_ENABLE == true>
		/* Configure BYPLL */
		/* BTPLLBSWSEL   = ${BTPLLCON_BTPLLBSWSEL_VALUE} */
		/* BTPLLPWDN     = ${BTPLLCON_BTPLLPWDN_VALUE} */
		/* BTPLLPOSTDIV1 = ${BTPLLCON_BTPLLPOSTDIV1_VALUE} */
		/* BTPLLFLOCK    = ${BTPLLCON_BTPLLFLOCK_VALUE} */
		/* BTPLLRST      = ${BTPLLCON_BTPLLRST_VALUE} */
		/* BTPLLFBDIV    = ${BTPLLCON_BTPLLFBDIV_VALUE} */
		/* BTPLLREFDIV   = ${BTPLLCON_BTPLLREFDIV_VALUE} */
		/* BTCLKOUTEN    = ${BTPLLCON_BTCLKOUTEN_VALUE} */
		/* BTPLLICLK     = ${BTPLLCON_BTPLLCLK_VALUE} */
		/* BTPLL_BYP     = ${BTPLLCON_BTPLL_BYP_VALUE} */
		${BTPLLCON_REG} = 0x${BTPLLCON_VALUE};
<#else>
		/* Power down the BTPLL */
		BTPLLCONbits.BTPLLPWDN = 1;
</#if>

        *(PMDRCLR)  = 0x1000;
    }
    else if(((DEVID & 0x0FF00000) >> 20) == PIC32MZW1_A1)
    {

		CFGCON2  |= 0x300; // Start with POSC Turned OFF
		DelayMs(2);

		/* make sure we properly reset SPI to a known state */
		*RFSPICTL = 0x80000022;
		/* now wifi is properly reset enable POSC */
		CFGCON2  &= 0xFFFFFCFF; // enable POSC

		DelayMs(2);

        /* make sure we properly take out of reset */
        *RFSPICTL = 0x80000002;

        wifi_spi_write(0x85, 0x00F0); // MBIAS filter and A31 analog_test
        wifi_spi_write(0x84, 0x0001); // A31 Analog test
        wifi_spi_write(0x1e, 0x510); // MBIAS reference adjustment
        wifi_spi_write(0x82, 0x6000); // XTAL LDO feedback divider (1.3+v)

		 /* Wait for POSC ready */
        while(!(CLKSTAT & 0x00000004)) ;

    	OSCCONbits.FRCDIV = ${SYS_CLK_FRCDIV};

		${CFGCON3_NAME} = ${CFGCON3_VALUE};
        CFGCON0bits.SPLLHWMD = 1;
		/* SPLLCON = 0x01496869 */
		/* SPLLBSWSEL   = ${SPLLCON_SPLLBSWSEL_VALUE}   */
		/* SPLLPWDN     = ${SPLLCON_SPLLPWDN_VALUE}     */
		/* SPLLPOSTDIV1 = ${SPLLCON_SPLLPOSTDIV1_VALUE} */
		/* SPLLFLOCK    = ${SPLLCON_SPLLFLOCK_VALUE}    */
		/* SPLLRST      = ${SPLLCON_SPLLRST_VALUE}      */
		/* SPLLFBDIV    = ${SPLLCON_SPLLFBDIV_VALUE}  */
		/* SPLLREFDIV   = ${SPLLCON_SPLLREFDIV_VALUE}   */
		/* SPLLICLK     = ${SPLLCON_SPLLICLK_VALUE}     */
		/* SPLL_BYP     = ${SPLLCON_SPLL_BYP_VALUE}     */
		${SPLLCON_REG} = 0x${SPLLCON_VALUE};


<#if USBPLL_ENABLE == true>
		/* Configure UPLL */
		/* UPLLBSWSEL   = ${UPLLCON_UPLLBSWSEL_VALUE} */
		/* UPLLPWDN     = ${UPLLCON_UPLLPWDN_VALUE} */
		/* UPLLPOSTDIV1 = ${UPLLCON_UPLLPOSTDIV1_VALUE} */
		/* UPLLFLOCK    = ${UPLLCON_UPLLFLOCK_VALUE} */
		/* UPLLRST      = ${UPLLCON_UPLLRST_VALUE} */
		/* UPLLFBDIV    = ${UPLLCON_UPLLFBDIV_VALUE} */
		/* UPLLREFDIV   = ${UPLLCON_UPLLREFDIV_VALUE} */
		/* UPLL_BYP     = ${UPLLCON_UPLL_BYP_VALUE} */
		${UPLLCON_REG} = 0x${UPLLCON_VALUE};
<#else>
		/* Power down the UPLL */
		UPLLCONbits.UPLLPWDN = 1;
</#if>

<#if EWPLL_ENABLE == true>
		/* Configure EWPLL */
		/* EWPLLBSWSEL   = ${EWPLLCON_EWPLLBSWSEL_VALUE} */
		/* EWPLLPWDN     = ${EWPLLCON_EWPLLPWDN_VALUE} */
		/* EWPLLPOSTDIV1 = ${EWPLLCON_EWPLLPOSTDIV1_VALUE} */
		/* EWPLLFLOCK    = ${EWPLLCON_EWPLLFLOCK_VALUE} */
		/* EWPLLRST      = ${EWPLLCON_EWPLLRST_VALUE} */
		/* EWPLLFBDIV    = ${EWPLLCON_EWPLLFBDIV_VALUE} */
		/* EWPLLREFDIV   = ${EWPLLCON_EWPLLREFDIV_VALUE} */
		/* EWPLLICLK     = ${EWPLLCON_EWPLLICLK_VALUE} */
		/* ETHCLKOUTEN   = ${EWPLLCON_ETHCLKOUTEN_VALUE} */
		/* EWPLL_BYP     = ${EWPLLCON_EWPLL_BYP_VALUE} */
		${EWPLLCON_REG} = 0x${EWPLLCON_VALUE} ^ 0x438080c;
		CFGCON0bits.ETHPLLHWMD = 1;
		while(!((*PLLDBG) & 0x4));
<#else>
		/* Power down the EWPLL */
		EWPLLCONbits.EWPLLPWDN = 1;
</#if>

<#if BTPLL_ENABLE == true>
		/* Configure BYPLL */
		/* BTPLLBSWSEL   = ${BTPLLCON_BTPLLBSWSEL_VALUE} */
		/* BTPLLPWDN     = ${BTPLLCON_BTPLLPWDN_VALUE} */
		/* BTPLLPOSTDIV1 = ${BTPLLCON_BTPLLPOSTDIV1_VALUE} */
		/* BTPLLFLOCK    = ${BTPLLCON_BTPLLFLOCK_VALUE} */
		/* BTPLLRST      = ${BTPLLCON_BTPLLRST_VALUE} */
		/* BTPLLFBDIV    = ${BTPLLCON_BTPLLFBDIV_VALUE} */
		/* BTPLLREFDIV   = ${BTPLLCON_BTPLLREFDIV_VALUE} */
		/* BTCLKOUTEN    = ${BTPLLCON_BTCLKOUTEN_VALUE} */
		/* BTPLLICLK     = ${BTPLLCON_BTPLLCLK_VALUE} */
		/* BTPLL_BYP     = ${BTPLLCON_BTPLL_BYP_VALUE} */
		${BTPLLCON_REG} = 0x${BTPLLCON_VALUE};
<#else>
		/* Power down the BTPLL */
		BTPLLCONbits.BTPLLPWDN = 1;
</#if>

		/* ETHPLLPOSTDIV2 = ${CFG_ETHPLLPOSTDIV2} */
		/* SPLLPOSTDIV2   = ${CFG_SPLLPOSTDIV2} */
		/* BTPLLPOSTDIV2  = ${CFG_BTPLLPOSTDIV2} */
		${CFGCON3_NAME} = ${CFGCON3_VALUE};

		/* OSWEN    = ${OSCCON_OSWEN_VALUE}    */
		/* SOSCEN   = ${OSCCON_SOSCEN_VALUE}   */
		/* UFRCEN   = ${OSCCON_UFRCEN_VALUE}   */
		/* CF       = ${OSCCON_CF_VALUE}       */
		/* SLPEN    = ${OSCCON_SLPEN_VALUE}    */
		/* CLKLOCK  = ${OSCCON_CLKLOCK_VALUE}  */
		/* NOSC     = ${OSCCON_NOSC_VALUE}     */
		/* WAKE2SPD = ${OSCCON_WAKE2SPD_VALUE} */
		/* DRMEN    = ${OSCCON_DRMEN_VALUE}    */
		/* FRCDIV   = ${OSCCON_FRCDIV_VALUE}   */
		${OSCCON_REG} = 0x${OSCCON_VALUE};

		OSCCONSET = _OSCCON_OSWEN_MASK;  /* request oscillator switch to occur */

		Nop();
		Nop();

		while( OSCCONbits.OSWEN );        /* wait for indication of successful clock change before proceeding */
	}
<#if CONFIG_SYS_CLK_PBCLK1_ENABLE == true && CONFIG_SYS_CLK_PBDIV1 != 2>
    <#lt>    /* Peripheral Bus 1 is by default enabled, set its divisor */
    <#lt>    /* PBDIV = ${CONFIG_SYS_CLK_PBDIV1} */
    <#lt>    ${PBREGNAME1}bits.PBDIV = ${CONFIG_SYS_CLK_PBDIV1 - 1};

</#if>
<#if CONFIG_SYS_CLK_PBCLK2_ENABLE == true>
    <#if CONFIG_SYS_CLK_PBDIV2 != 2>
        <#lt>    /* Peripheral Bus 2 is by default enabled, set its divisor */
        <#lt>    /* PBDIV = ${CONFIG_SYS_CLK_PBDIV2} */
        <#lt>    ${PBREGNAME2}bits.PBDIV = ${CONFIG_SYS_CLK_PBDIV2 - 1};

    </#if>
<#else>
    /* Disable Peripheral Bus 2 */
    ${PBREGNAME2}CLR = ${PBONMASK2};

</#if>
<#if CONFIG_SYS_CLK_PBCLK3_ENABLE == true>
    <#if CONFIG_SYS_CLK_PBDIV3 != 2>
        <#lt>    /* Peripheral Bus 3 is by default enabled, set its divisor */
        <#lt>    /* PBDIV = ${CONFIG_SYS_CLK_PBDIV3} */
        <#lt>    ${PBREGNAME3}bits.PBDIV = ${CONFIG_SYS_CLK_PBDIV3 - 1};

    </#if>
<#else>
    /* Disable Peripheral Bus 3 */
    ${PBREGNAME3}CLR = ${PBONMASK3};

</#if>
<#if CONFIG_SYS_CLK_PBCLK4_ENABLE == true>
    <#if CONFIG_SYS_CLK_PBDIV4 != 2>
        <#lt>    /* Peripheral Bus 4 is by default enabled, set its divisor */
        <#lt>    /* PBDIV = ${CONFIG_SYS_CLK_PBDIV4} */
        <#lt>    ${PBREGNAME4}bits.PBDIV = ${CONFIG_SYS_CLK_PBDIV4 - 1};

    </#if>
<#else>
    /* Disable Peripheral Bus 4 */
    ${PBREGNAME4}CLR = ${PBONMASK4};

</#if>
<#if CONFIG_SYS_CLK_PBCLK5_ENABLE == true>
    <#if CONFIG_SYS_CLK_PBDIV5 != 2>
        <#lt>    /* Peripheral Bus 5 is by default enabled, set its divisor */
        <#lt>    /* PBDIV = ${CONFIG_SYS_CLK_PBDIV5} */
        <#lt>    ${PBREGNAME5}bits.PBDIV = ${CONFIG_SYS_CLK_PBDIV5 - 1};

    </#if>
<#else>
    /* Disable Peripheral Bus 5 */
    ${PBREGNAME5}CLR = ${PBONMASK5};

</#if>
<#if CONFIG_SYS_CLK_PBCLK6_ENABLE == true>
    <#if CONFIG_SYS_CLK_PBDIV6 != 1>
        <#lt>    /* Peripheral Bus 6 is by default enabled, set its divisor */
        <#lt>    /* PBDIV = ${CONFIG_SYS_CLK_PBDIV6} */
        <#lt>    ${PBREGNAME6}bits.PBDIV = ${CONFIG_SYS_CLK_PBDIV6 - 1};

    </#if>
<#else>
    /* Disable Peripheral Bus 6 */
    ${PBREGNAME6}CLR = ${PBONMASK6};

</#if>

<#if CONFIG_HAVE_REFCLOCK == true>
<#list 1..NUM_REFOSC_ELEMENTS as i>
    <#assign ENBL = "CONFIG_SYS_CLK_REFCLK"+i+"_ENABLE">
    <#assign REFCONREG = "REFCON"+i+"REG">
    <#assign ROSELVAL = "CONFIG_SYS_CLK_REFCLK_SOURCE"+i>
    <#assign REFTRIMREG = "REFTRIM"+i+"REG">
    <#assign ROTRIMVAL = "CONFIG_SYS_CLK_ROTRIM"+i>
    <#assign ONMASK = "REFOCON_ONMASK"+i>
    <#assign REFCLKOE = "CONFIG_SYS_CLK_REFCLK"+i+"_OE">
    <#assign OEMASK = "REFOCON_OEMASK"+i>
    <#assign REFCONVAL = "REFOCON"+i+"_VALUE">
    <#assign REFOTRIMVAL = "REFO"+i+"TRIM_VALUE">
    <#assign REFOCONRODIV = "CONFIG_SYS_CLK_RODIV"+i>
<#if .vars[ENBL] = true>
    /* Set up Reference Clock ${i} */
        <#lt>    /* REFO${i}CON register */
        <#lt>    /* ROSEL =  ${.vars[ROSELVAL]} */
        <#lt>    /* DIVSWEN = 1 */
        <#lt>    /* RODIV = ${.vars[REFOCONRODIV]} */
        <#lt>    ${.vars[REFCONREG]} = ${.vars[REFCONVAL]};

    <#if .vars[REFOTRIMVAL] != "0x0">
        <#lt>    /* REFO${i}TRIM register */
        <#lt>    /* ROTRIM = ${.vars[ROTRIMVAL]} */
        <#lt>    ${.vars[REFTRIMREG]} = ${.vars[REFOTRIMVAL]};

    </#if>
    <#if (.vars[REFCLKOE]?has_content) && (.vars[REFCLKOE] == true)>
        <#lt>    /* Enable oscillator (ON bit) and Enable Output (OE bit) */
        <#lt>    ${.vars[REFCONREG]}SET = ${.vars[OEMASK]} | ${.vars[ONMASK]};

    <#else>
        <#lt>    /* Enable oscillator (ON bit) */
        <#lt>    ${.vars[REFCONREG]}SET = ${.vars[ONMASK]};

    </#if>
</#if>
</#list>
</#if>  <#-- CONFIG_HAVE_REFCLOCK == true -->

    /* Peripheral Module Disable Configuration */

<#if PMDLOCK_ENABLE?? && PMDLOCK_ENABLE == true>
    CFGCON0bits.PMDLOCK = 0;
</#if>

<#list 1..PMD_COUNT + 1 as i>
    <#assign PMDREG_VALUE = "PMD" + i + "_REG_VALUE">
    <#if .vars[PMDREG_VALUE]?? && .vars[PMDREG_VALUE] != "None">
        <#lt>    PMD${i} = 0x${.vars[PMDREG_VALUE]};
    </#if>
</#list>

<#if PMDLOCK_ENABLE?? && PMDLOCK_ENABLE == true>
    CFGCON0bits.PMDLOCK = 1;
</#if>
	if(1 == RCONbits.POR)
		RCONbits.POR = 0;
	if(1 == RCONbits.EXTR)
		RCONbits.EXTR = 0;
    if(1 == RCONbits.SWR)
        RCONbits.SWR = 0;

    /* Lock system since done with clock configuration */
    SYSKEY = 0x33333333;
}
