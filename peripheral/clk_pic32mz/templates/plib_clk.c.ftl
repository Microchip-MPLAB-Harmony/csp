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
    SYSKEY = 0x00000000U;
    SYSKEY = 0xAA996655U;
    SYSKEY = 0x556699AAU;

    /* Peripheral Module Disable Configuration */

<#if PMDLOCK_ENABLE?? && PMDLOCK_ENABLE == true>
    CFGCONbits.PMDLOCK = 0;
</#if>

<#list 1..PMD_COUNT + 1 as i>
    <#assign PMDREG_VALUE = "PMD" + i + "_REG_VALUE">
    <#if .vars[PMDREG_VALUE]?? && .vars[PMDREG_VALUE] != "None">
        <#lt>    PMD${i} = 0x${.vars[PMDREG_VALUE]}U;
    </#if>
</#list>

<#if PMDLOCK_ENABLE?? && PMDLOCK_ENABLE == true>
    CFGCONbits.PMDLOCK = 1;
</#if>

<#if SYS_CLK_FRCDIV != "0">
    OSCCONbits.FRCDIV = ${SYS_CLK_FRCDIV};

</#if>
<#if CONFIG_SYS_CLK_PBCLK1_ENABLE == true && CONFIG_SYS_CLK_PBDIV1 != 2>
    /* Peripheral Bus 1 is by default enabled, set its divisor */
    ${PBREGNAME1}bits.PBDIV = ${CONFIG_SYS_CLK_PBDIV1 -1};

</#if>
<#if CONFIG_SYS_CLK_PBCLK2_ENABLE == true>
    <#if CONFIG_SYS_CLK_PBDIV2 != 2>
        <#lt>    /* Peripheral Bus 2 is by default enabled, set its divisor */
        <#lt>    ${PBREGNAME2}bits.PBDIV = ${CONFIG_SYS_CLK_PBDIV2 -1};

    </#if>
<#else>
    /* Disable Peripheral Bus 2 */
    ${PBREGNAME2}CLR = ${PBONMASK2};

</#if>
<#if CONFIG_SYS_CLK_PBCLK3_ENABLE == true>
    <#if CONFIG_SYS_CLK_PBDIV3 != 2>
        <#lt>    /* Peripheral Bus 3 is by default enabled, set its divisor */
        <#lt>    ${PBREGNAME3}bits.PBDIV = ${CONFIG_SYS_CLK_PBDIV3 -1};

    </#if>
<#else>
    /* Disable Peripheral Bus 3 */
    ${PBREGNAME3}CLR = ${PBONMASK3};

</#if>
<#if CONFIG_SYS_CLK_PBCLK4_ENABLE == true>
    <#if CONFIG_SYS_CLK_PBDIV4 != 2>
        <#lt>    /* Peripheral Bus 4 is by default enabled, set its divisor */
        <#lt>    ${PBREGNAME4}bits.PBDIV = ${CONFIG_SYS_CLK_PBDIV4 -1};

    </#if>
<#else>
    /* Disable Peripheral Bus 4 */
    ${PBREGNAME4}CLR = ${PBONMASK4};

</#if>
<#if CONFIG_SYS_CLK_PBCLK5_ENABLE == true>
    <#if CONFIG_SYS_CLK_PBDIV5 != 2>
        <#lt>    /* Peripheral Bus 5 is by default enabled, set its divisor */
        <#lt>    ${PBREGNAME5}bits.PBDIV = ${CONFIG_SYS_CLK_PBDIV5 -1};

    </#if>
<#else>
    /* Disable Peripheral Bus 5 */
    ${PBREGNAME5}CLR = ${PBONMASK5};

</#if>
<#if CONFIG_SYS_CLK_PBCLK6_ENABLE?has_content>
<#if CONFIG_SYS_CLK_PBCLK6_ENABLE == true>
    <#if CONFIG_SYS_CLK_PBDIV6 != 2>
        <#lt>    /* Peripheral Bus 6 is by default enabled, set its divisor */
        <#lt>    ${PBREGNAME6}bits.PBDIV = ${CONFIG_SYS_CLK_PBDIV6 -1};

    </#if>
<#else>
    /* Disable Peripheral Bus 6 */
    ${PBREGNAME6}CLR = ${PBONMASK6};

</#if>
</#if>
<#if CONFIG_SYS_CLK_PBCLK7_ENABLE == true>
    <#if CONFIG_SYS_CLK_PBDIV7 != 1>
        <#lt>    /* Peripheral Bus 7 is by default enabled, set its divisor */
        <#lt>    ${PBREGNAME7}bits.PBDIV = ${CONFIG_SYS_CLK_PBDIV7 -1};

    </#if>
<#else>
    /* Disable Peripheral Bus 7 */
    ${PBREGNAME7}CLR = ${PBONMASK7};

</#if>
<#if CONFIG_SYS_CLK_PBCLK8_ENABLE?has_content>
<#if CONFIG_SYS_CLK_PBCLK8_ENABLE == true>
    <#if CONFIG_SYS_CLK_PBDIV8 != 2>
        <#lt>    /* Peripheral Bus 8 is by default enabled, set its divisor */
        <#lt>    ${PBREGNAME8}bits.PBDIV = ${CONFIG_SYS_CLK_PBDIV8 -1};

    </#if>
<#else>
    /* Disable Peripheral Bus 8 */
    ${PBREGNAME8}CLR = ${PBONMASK8};

</#if>
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
    <#if .vars[REFCONVAL] != "0x200">
        <#lt>    /* REFO${i}CON register */
        <#lt>    /* ROSEL =  ${.vars[ROSELVAL]} */
        <#lt>    /* DIVSWEN = 1 */
        <#lt>    /* RODIV = ${.vars[REFOCONRODIV]} */
        <#lt>    ${.vars[REFCONREG]} = ${.vars[REFCONVAL]};

    </#if>
    <#if .vars[REFOTRIMVAL] != "0x0">
        <#lt>    /* REFO${i}TRIM register */
        <#lt>    /* ROTRIM = ${.vars[ROTRIMVAL]} */
        <#lt>    ${.vars[REFTRIMREG]} = ${.vars[REFOTRIMVAL]};

    </#if>
    <#if (.vars[REFCLKOE]?has_content) && (.vars[REFCLKOE] == true)>
        <#lt>    /* Enable oscillator (ON bit) and Enable Output (OE bit) */
        <#lt>    ${.vars[REFCONREG]}SET = ${.vars[OEMASK]}U | ${.vars[ONMASK]}U;

    <#else>
        <#lt>    /* Enable oscillator (ON bit) */
        <#lt>    ${.vars[REFCONREG]}SET = ${.vars[ONMASK]};

    </#if>
</#if>
</#list>
<#-- Initialize MPLL registers that pertain only to certain families -->
<#if DEVICE_HAS_DDR2 == true && CLK_MPLLDIS_VALUE == "ENABLED" && CLK_MPLLVREGDIS_VALUE == "ENABLED">
    /* CFGMPLL */
    /* MPLLVREGDIS = ${CLK_MPLLVREGDIS_VALUE} */
    /* INTVREFCON = ${CLK_MPLLINTVREFCON_VALUE} */
    /* MPLLIDIV = ${CLK_MPLLIDIV_VALUE} */
    /* MPLLMULT = ${CLK_MPLLMULT_VALUE} */
    /* MPLLODIV2 = ${CLK_MPLLODIV2_VALUE} */
    /* MPLLODIV1 = ${CLK_MPLLODIV1_VALUE} */
    /* MPLLDIS = ${CLK_MPLLDIS_VALUE} */

    CFGMPLLbits.MPLLVREGDIS = ${CLK_MPLLVREGDIS_BIT_VALUE};

    while(CFGMPLLbits.MPLLVREGRDY == 0U)
    {
        /* Wait for completion */
    }

    CFGMPLL = ${CLK_CFGMPLL_REGVALUE};

    while(CFGMPLLbits.MPLLRDY == 0U)
    {
        /* Wait for completion */
    }
</#if>
</#if>  <#-- CONFIG_HAVE_REFCLOCK == true -->    

    /* Lock system since done with clock configuration */
    SYSKEY = 0x33333333U;
}
