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

static void  DelayUs ( uint32_t  delayUs)
{
    uint32_t startCount, endCount;
    /* Calculate the end count for the given delay */
    endCount=((uint32_t)CORE_TIMER_FREQ/1000000U)* delayUs;
    startCount=_CP0_GET_COUNT();
    while((_CP0_GET_COUNT()-startCount)<endCount)
    {
        /* Nothing to do */
    }
}

 static void wifi_spi_write(unsigned int spi_addr, unsigned int data)
{
    unsigned int  addr_bit, data_bit, bit_idx;
    unsigned int cs_high, clk_high, en_bit_bang;
    volatile unsigned int *const wifi_spi_ctrl_reg = (unsigned int *const)0xBF8C8028U;
    clk_high = 0x1 ;
    cs_high  = 0x2;
    en_bit_bang  = 0x1UL << 31;
    addr_bit = 0; data_bit = 0;

    *wifi_spi_ctrl_reg = en_bit_bang | cs_high ;
    *wifi_spi_ctrl_reg = (en_bit_bang | cs_high | clk_high );
     *wifi_spi_ctrl_reg = (en_bit_bang);
     *wifi_spi_ctrl_reg = (en_bit_bang | clk_high);

    for (bit_idx=0;bit_idx<=7U;bit_idx++) {
        addr_bit = (spi_addr>>(7U-bit_idx)) & 0x1U;
        *wifi_spi_ctrl_reg = (en_bit_bang | (addr_bit << 2 ));               // Falling edge of clk
        *wifi_spi_ctrl_reg = (en_bit_bang | (addr_bit << 2 ) | clk_high);    // Rising edge of clk
    }

    for (bit_idx=0;bit_idx<=15U;bit_idx++) {
        data_bit = (data>>(15U-bit_idx)) & 0x1U;
        *wifi_spi_ctrl_reg = (en_bit_bang | (data_bit << 2 ));                // Falling edge of clk with data bit
        *wifi_spi_ctrl_reg = (en_bit_bang | (data_bit << 2 ) | clk_high);     // Rising edge of clk
    }

    *wifi_spi_ctrl_reg = (en_bit_bang | cs_high | clk_high); // Rising edge of clk
    *wifi_spi_ctrl_reg = 0;                                // Set the RF override bit and CS_n high
}
void CLK_Initialize( void )
{
    volatile unsigned int *PLLDBG = (unsigned int*) 0xBF8000E0U;
    volatile unsigned int *PMDRCLR = (unsigned int *) 0xBF8000B4U;
	volatile unsigned int *RFSPICTL = (unsigned int *) 0xBF8C8028U;
    
    /* unlock system for clock configuration */
    SYSKEY = 0x00000000;
    SYSKEY = 0xAA996655U;
    SYSKEY = 0x556699AA;

	if(((DEVID & PART_NUM_MASK) >> PART_NUM_OFFSET == (uint32_t)PIC32MZW1_B0)
            || ((DEVID & PART_NUM_MASK) >> PART_NUM_OFFSET == (uint32_t)PIC32MZW1_G))
    {
		if(SPLLCON_DEFAULT == SPLLCON)
		{
			EWPLLCON = PLL_PWROFF; // Start with PWR-OFF PLL
			SPLLCON  = PLL_PWROFF; // Start with PWR-OFF PLL
			DelayUs(300);

			CFGCON2  |= POSC_DIS; // Start with POSC Turned OFF
			/* if POSC was on give some time for POSC to shut off */
			DelayUs(300);
			/* make sure we properly reset SPI to a known state */
			*RFSPICTL = 0x80000022U;
			/* make sure we properly take out of reset */
			*RFSPICTL = 0x80000002U;

			if((1U == DEVIDbits.VER) || (((DEVID & PART_NUM_MASK) >> 20) == (uint32_t)PIC32MZW1_G))
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
             DelayUs(200);
			/* Enable POSC */
			CFGCON2  &= POSC_EN; // enable POSC
			 DelayUs(300);

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

			while( OSCCONbits.OSWEN != 0U)
            {
                /* Nothing to do */
            }
			/****************************************************************
             * check to see if PLL locked; indicates POSC must have started
             * The recommendation is to use SPLL as the System Clock.
             * Below code assumes that is the case in most practical use cases.
            *****************************************************************/
            if(OSCCONbits.COSC & 0x2U)
            {
                if(0U == (CLKSTATbits.POSCRDY & 0x1U))
                {
                     while(true)
                    {
                        /* Nothing to do */
                    }
                }
            }
            else if(0U == (*PLLDBG & 0x1U))
            {
                /*POSC failed to start!*/
                while(true)
                {
                   /* Nothing to do */
                }
            }       
			if(1U == DEVIDbits.VER || (((DEVID & PART_NUM_MASK) >> PART_NUM_OFFSET) == (uint32_t)PIC32MZW1_G))
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
            while( OSCCONbits.OSWEN != 0U )
            {
                /* Nothing to do */
            }

            SPLLCON  = PLL_PWROFF; // Start with PWR-OFF PLL

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
			while( OSCCONbits.OSWEN != 0U)
            {
                /* Nothing to do */
            }

            /****************************************************************
			* check to see if PLL locked; indicates POSC must have started
			*****************************************************************/
            if(0U == (*PLLDBG & 0x1U))
			{
				/*POSC failed to start!*/
				while(true)
                {
                    /* Nothing to do */
                }
                
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
		${EWPLLCON_REG} = 0x${EWPLLCON_VALUE}U ^ EWPLLCON_MSK;
		 DelayUs(200);
		${EWPLLCON_REG} &= ~PLL_PWROFF;
		/****************************************************************
		* check to see if PLL locked; indicates POSC must have started
		*****************************************************************/
		if(0U == (*PLLDBG & 0x5U))
		{
			/*POSC failed to start!*/
			while(true)
            {
                /* Nothing to do */
            }
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
    else if(((DEVID & PART_NUM_MASK) >> PART_NUM_OFFSET) == (uint32_t)PIC32MZW1_A1)
    {

		CFGCON2  |= POSC_DIS; // Start with POSC Turned OFF
		 DelayUs(200);

		/* make sure we properly reset SPI to a known state */
		*RFSPICTL = 0x80000022U;
		/* now wifi is properly reset enable POSC */
		CFGCON2  &= POSC_EN; // enable POSC

		 DelayUs(200);

        /* make sure we properly take out of reset */
        *RFSPICTL = 0x80000002U;

        wifi_spi_write(0x85, 0x00F0); // MBIAS filter and A31 analog_test
        wifi_spi_write(0x84, 0x0001); // A31 Analog test
        wifi_spi_write(0x1e, 0x510); // MBIAS reference adjustment
        wifi_spi_write(0x82, 0x6000); // XTAL LDO feedback divider (1.3+v)

		 /* Wait for POSC ready */
        while((CLKSTAT & 0x00000004U) == 0U) 
        {
            /* Nothing to do */
        }

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
		${EWPLLCON_REG} = 0x${EWPLLCON_VALUE}U ^ 0x438080cU;
		CFGCON0bits.ETHPLLHWMD = 1;
		while(((*PLLDBG) & 0x4U) == 0U)
        {
            /* Nothing to do */
        }
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

		while( OSCCONbits.OSWEN != 0U)        /* wait for indication of successful clock change before proceeding */
        {
            /* Nothing to do */
        }
	}
    else
    {
        /* Nothing to do */
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

    /* Lock system since done with clock configuration */
    SYSKEY = 0x33333333;
}
