<#--
/*******************************************************************************
Copyright (c) 2019 released Microchip Technology Inc.  All rights reserved.

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

 /*******************************************************************************
  SYS CLK Static Functions for Clock System Service

  Company:
    Microchip Technology Inc.

  File Name:
    plib_clk.c.ftl

  Summary:
    SYS CLK static function implementations for the Clock System Service.

  Description:
    The Clock System Service provides a simple interface to manage the oscillators
    on Microchip microcontrollers. This file defines the static implementation for the
    Clock System Service.

  Remarks:
    Static functions incorporate all system clock configuration settings as
    determined by the user via the Microchip Harmony Configurator GUI.  It provides
    static version of the routines, eliminating the need for an object ID or
    object handle.

    Static single-open interfaces also eliminate the need for the open handle.
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
    void CLK_Initialize ( void )

  Summary:
    Initializes hardware and internal data structure of the System Clock.

  Description:
    This function initializes the hardware and internal data structure of System
    Clock Service.

  Remarks:
    This is configuration values for the static version of the Clock System Service
    module is determined by the user via the Microchip Harmony Configurator GUI.

    The objective is to eliminate the user's need to be knowledgeable in the function of
    the 'configuration bits' to configure the system oscillators.
*/

void CLK_Initialize( void )
{
    bool int_flag = false;

    int_flag = (bool)__builtin_disable_interrupts();
    /* unlock system for clock configuration */
    SYSKEY = 0x00000000;
    SYSKEY = 0xAA996655;
    SYSKEY = 0x556699AA;
    if (int_flag)
    {
        __builtin_mtc0(12, 0,(__builtin_mfc0(12, 0) | 0x0001)); /* enable interrupts */
    }

    OSCCONbits.FRCDIV = ${SYS_CLK_FRCDIV};
<#if UPLL_EN == true>  <#-- UPLL_EN is dependent on DEVCFG2:UPLLEN -->
    /* Configure UPLL */
    /* UPOSCEN = ${UPOSCEN_VAL} */
    /* PLLODIV = ${PLLODIV_VAL} */
    /* PLLMULT = ${PLLMULT_VAL} */
    /* PLLIDIV = ${PLLIDIV_VAL} */
    /* PLLRANGE = ${PLLRANGE_VAL} */
    ${UPLLCON_REG} = 0x${UPLLCON_REG_VALUE};
</#if>
<#if UFRCEN_VAL == "FRC">
    /* Make FRC as the input clock for USB */
    OSCCONSET = _OSCCON_UFRCEN_MASK;
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
    <#if CONFIG_SYS_CLK_PBDIV6 != 4>
        <#lt>    /* Peripheral Bus 6 is by default enabled, set its divisor */
        <#lt>    ${PBREGNAME6}bits.PBDIV = ${CONFIG_SYS_CLK_PBDIV6 -1};
    </#if>
<#else>
    /* Disable Peripheral Bus 6 */
    ${PBREGNAME6}CLR = ${PBONMASK6};
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
    /* Lock system since done with clock configuration */
    int_flag = (bool)__builtin_disable_interrupts();
    SYSKEY = 0x33333333;
    if (int_flag) /* if interrupts originally were enabled, re-enable them */
    {
        __builtin_mtc0(12, 0,(__builtin_mfc0(12, 0) | 0x0001));
    }
}




<#--
/*******************************************************************************
 End of File
*/
-->
