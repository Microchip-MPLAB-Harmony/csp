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

<#if CONFIG_SYS_CLK_CONFIG_SOSCEN == "1">
    /* Enable Secondary Oscillator */
    OSCCONSET = _OSCCON_SOSCEN_MASK;
<#elseif CONFIG_SYS_CLK_CONFIG_SOSCEN == "0">
    /* Disable Secondary Oscillator */
    OSCCONCLR = _OSCCON_SOSCEN_MASK;
</#if>

<#if CONFIG_SYS_CLK_PBCLK1_ENABLE == true>

    /* Enable Peripheral Bus 1 */
    /* PBDIV = ${CONFIG_SYS_CLK_PBDIV1}-1 */
    *(volatile uint32_t *)(&${PBREGNAME1}) = ${PB1DIV_VALUE};
</#if>

<#if CONFIG_SYS_CLK_PBCLK2_ENABLE == true>

    /* Enable Peripheral Bus 2 */
    /* PBDIV = ${CONFIG_SYS_CLK_PBDIV2}-1 */
    /* ON = 1                             */
    *(volatile uint32_t *)(&${PBREGNAME2}) = ${PB2DIV_VALUE};
<#else>
    /* Disable Peripheral Bus 2 */
    /* ON = 0                   */
    *(volatile uint32_t *)(&${PBREGNAME2}CLR) = ${PBONMASK2};
</#if>

<#if CONFIG_SYS_CLK_PBCLK3_ENABLE == true>

    /* Enable Peripheral Bus 3 */
    /* PBDIV = ${CONFIG_SYS_CLK_PBDIV3}-1 */
    /* ON = 1                             */
    *(volatile uint32_t *)(&${PBREGNAME3}) = ${PB3DIV_VALUE};
<#else>
    /* Disable Peripheral Bus 3 */
    /* ON = 0                   */
    *(volatile uint32_t *)(&${PBREGNAME3}CLR) = ${PBONMASK3};
</#if>



<#if CONFIG_SYS_CLK_PBCLK4_ENABLE == true>

    /* Enable Peripheral Bus 4 */
    /* PBDIV = ${CONFIG_SYS_CLK_PBDIV4}-1 */
    /* ON = 1                             */
    *(volatile uint32_t *)(&${PBREGNAME4}) = ${PB4DIV_VALUE};
<#else>
    /* Disable Peripheral Bus 4 */
    /* ON = 0                   */
    *(volatile uint32_t *)(&${PBREGNAME4}CLR) = ${PBONMASK4};
</#if>


<#if CONFIG_SYS_CLK_PBCLK5_ENABLE == true>

    /* Enable Peripheral Bus 5 */
    /* PBDIV = ${CONFIG_SYS_CLK_PBDIV5}-1 */
    /* ON = 1                             */
    *(volatile uint32_t *)(&${PBREGNAME5}) = ${PB5DIV_VALUE};
<#else>
    /* Disable Peripheral Bus 5 */
    /* ON = 0                   */
    *(volatile uint32_t *)(&${PBREGNAME5}CLR) = ${PBONMASK5};
</#if>

<#if CONFIG_SYS_CLK_PBCLK7_ENABLE == true>

    /* Enable Peripheral Bus 7 */
    /* PBDIV = ${CONFIG_SYS_CLK_PBDIV7}-1 */
    /* ON = 1                             */
    *(volatile uint32_t *)(&${PBREGNAME7}) = ${PB7DIV_VALUE};
<#else>
    /* Disable Peripheral Bus 7 */
    /* ON = 0                   */
    *(volatile uint32_t *)(&${PBREGNAME7}CLR) = ${PBONMASK7};
</#if>
<#if CONFIG_SYS_CLK_PBCLK8_ENABLE?has_content>
<#if CONFIG_SYS_CLK_PBCLK8_ENABLE == true>

    /* Enable Peripheral Bus 8 */
    /* PBDIV = ${CONFIG_SYS_CLK_PBDIV8}-1 */
    /* ON = 1                             */
    *(volatile uint32_t *)(&${PBREGNAME8}) = ${PB8DIV_VALUE};
<#else>
    /* Disable Peripheral Bus 8 */
    /* ON = 0                   */
    *(volatile uint32_t *)(&${PBREGNAME8}CLR) = ${PBONMASK8};
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
    *(volatile uint32_t *)(&${.vars[REFCONREG]}) = ${.vars[REFCONVAL]};

    /* REFO${i}TRIM register */
    /* ROTRIM = ${.vars[ROTRIMVAL]} */
    *(volatile uint32_t *)(&${.vars[REFTRIMREG]}) = ${.vars[REFOTRIMVAL]};

    /* ON - enable oscillator */
    *(volatile uint32_t *)(&${.vars[REFCONREG]}SET) = ${.vars[ONMASK]};
<#else>

    /* Disable Reference Clock ${i} */
    /* ON = 0 */
    *(volatile uint32_t *)(&${.vars[REFCONREG]}CLR) = ${.vars[ONMASK]};
</#if>
<#if (.vars[REFCLKOE] == true) && (.vars[ENBL] = true)>  <#-- no need to set OE bit if disabled -->
    /* Set Output Enable bit, OE */
    *(volatile uint32_t *)(&${.vars[REFCONREG]}SET) = ${.vars[OEMASK]};
<#else>
    /* Clear Output Enable bit, OE */
    *(volatile uint32_t *)(&${.vars[REFCONREG]}CLR) = ${.vars[OEMASK]};
</#if>
</#list>
<#-- Initialize MPLL registers that pertain only to certain families -->
<#if PROC_FAMILY == "PIC32MZDA">

    /* CFGMPLL */
    /* MPLLDIS = ${CLK_MPLLDIS_VALUE} */
    /* MPLLODIV2 = ${CLK_MPLLODIV2_VALUE} */
    /* MPLLODIV1 = ${CLK_MPLLODIV1_VALUE} */
    /* MPLLVREGDIS = ${CLK_MPLLVREGDIS_VALUE} */
    /* MPLLMULT = ${CLK_MPLLMULT_VALUE} */
    /* INTVREFCON = ${CLK_MPLLINTVREFCON_VALUE} */
    /* MPLLIDIV = ${CLK_MPLLIDIV_VALUE} */
    *(volatile uint32_t *)(&${CLK_CFGMPLL_REG}) = ${CLK_CFGMPLL_REGVALUE};
</#if>
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
