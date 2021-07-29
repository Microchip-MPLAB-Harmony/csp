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

void CLK_Initialize( void )
{
    /* unlock system for clock configuration */
    SYSKEY = 0x00000000;
    SYSKEY = 0xAA996655;
    SYSKEY = 0x556699AA;

<#if SYS_CLK_FRCDIV != "0">
    OSCCONbits.FRCDIV = ${SYS_CLK_FRCDIV};

</#if>
<#if CONFIG_FNOSC?contains("PLL")>
    /* Even though SPLL is selected in FNOSC, Harmony generates #pragma code as FRCDIV, not as SPLL, in "initilization.c".
    * Switching to SPLL is done here after appropriate setting of SPLLCON register. 
    * This is done to ensure we don't end-up changing PLL setting when it is ON. */

    /* Configure SPLL */
    /* ${PLLODIV_VAL}, ${PLLMULT_VAL}, PLLSRC= ${CONFIG_PLLSRC} */
    ${SPLLCON_REG} = 0x${SPLLCON_REG_VALUE};

    /* Now switch to the PLL source */
    OSCCON = OSCCON | 0x00000101;    //NOSC = SPLL, initiate clock switch (OSWEN = 1)
    
    /* Wait for PLL to be ready and clock switching operation to complete */
    while(!CLKSTATbits.SPLLRDY || !CLKSTATbits.SPDIVRDY || OSCCONbits.OSWEN);
<#else>
    /* Configure SPLL */
    /* ${PLLODIV_VAL}, ${PLLMULT_VAL}, PLLSRC= ${CONFIG_PLLSRC} */
    ${SPLLCON_REG} = 0x${SPLLCON_REG_VALUE};
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
    /* REFO${i}CON register */
    /* ROSEL =  ${.vars[ROSELVAL]} */
    /* DIVSWEN = 1 */
    /* RODIV = ${.vars[REFOCONRODIV]} */
    ${.vars[REFCONREG]} = ${.vars[REFCONVAL]};

    /* REFO${i}TRIM register */
    /* ROTRIM = ${.vars[ROTRIMVAL]} */
    ${.vars[REFTRIMREG]} = ${.vars[REFOTRIMVAL]};

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
<#if OSCTUN_REG_VALUE != "0">
    /* Configure FRC Self Tuning */
    OSCTUN = 0x${OSCTUN_REG_VALUE};

</#if>
    /* Peripheral Module Disable Configuration */
<#list 1..PMD_COUNT + 1 as i>
    <#assign PMDREG_VALUE = "PMD" + i + "_REG_VALUE">
    <#if .vars[PMDREG_VALUE]?? && .vars[PMDREG_VALUE] != "None">
        <#lt>    PMD${i} = 0x${.vars[PMDREG_VALUE]};
    </#if>
</#list>

    /* Lock system since done with clock configuration */
    SYSKEY = 0x33333333;
}
