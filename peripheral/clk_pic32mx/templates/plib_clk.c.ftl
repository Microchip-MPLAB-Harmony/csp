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
<#if DEVICE_FAMILY == "DS60001404">
    <#assign REFOTRIMreg = "REFO1TRIM">
    <#assign REFOCONreg = "REFO1CON">
<#else>
    <#assign REFOTRIMreg = "REFOTRIM">
    <#assign REFOCONreg = "REFOCON">
</#if>

<#if (CONFIG_SYS_CLK_FRCDIV != FRCDIV_DEFAULT) ||
     ((USB_PART = true) && (CONFIG_SYS_CLK_UFRCEN == "ON")) ||
     ((CONFIG_SYS_CLK_REFCLK_ENABLE?has_content) && (CONFIG_SYS_CLK_REFCLK_ENABLE == true)) ||
     ((DEVICE_FAMILY == "DS60001404") && (UPLLCON_VALUE != UPLLCON_DEFAULT_VALUE))>
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
    <#if CONFIG_SYS_CLK_FRCDIV != FRCDIV_DEFAULT>
    OSCCONbits.FRCDIV = ${CONFIG_SYS_CLK_FRCDIV};

    </#if>
    <#if USB_PART = true && CONFIG_SYS_CLK_UFRCEN == "ON">
    /* Make FRC as the input clock for USB */
    OSCCONSET = _OSCCON_UFRCEN_MASK;

    </#if>

<#if CONFIG_SYS_CLK_REFCLK_ENABLE?has_content>
    <#if CONFIG_SYS_CLK_REFCLK_ENABLE == true>
        <#if REFOCON_VALUE != REFOCON_DEFAULT>
            <#lt>    /* Set up Reference Clock */
            <#lt>    /* ROSEL =  ${CONFIG_SYS_CLK_ROSEL} */
            <#lt>    /* RODIV = ${CONFIG_SYS_CLK_RODIV} */
            <#lt>    ${REFOCONreg} = 0x${REFOCON_VALUE};
        </#if>
        <#if REFOTRIM_VALUE != "0">
            <#lt>    /* ROTRIM  = ${CONFIG_SYS_CLK_ROTRIM} */
            <#lt>    ${REFOTRIMreg} = 0x${REFOTRIM_VALUE};
        </#if>
        <#if (CONFIG_SYS_CLK_OE?has_content) && (CONFIG_SYS_CLK_OE == true)>
            <#lt>    /* Enable Reference Oscillator (ON bit) and Enable its Output (OE bit) */
            <#lt>    ${REFOCONreg}SET = ${OE_MASK} | ${ON_MASK};
        <#else>
            <#lt>    /* Enable Reference Oscillator (ON bit) */
            <#lt>    ${REFOCONreg}SET = ${ON_MASK};
        </#if>
    </#if>
</#if>

<#if (DEVICE_FAMILY == "DS60001404") && (UPLLCON_VALUE != UPLLCON_DEFAULT_VALUE)>
    /* PLLODIV  = ${CONFIG_SYS_CLK_UPLLODIV} */
    /* PLLMULT  = ${CONFIG_SYS_CLK_UPLLMULT} */
    /* PLLIDIV  = ${CONFIG_SYS_CLK_UPLLIDIV} */
    UPLLCON = 0x${UPLLCON_VALUE};
</#if>

    /* Lock system since done with clock configuration */
    int_flag = (bool)__builtin_disable_interrupts();

    SYSKEY = 0x33333333;

    if (int_flag) /* if interrupts originally were enabled, re-enable them */
    {
        __builtin_mtc0(12, 0,(__builtin_mfc0(12, 0) | 0x0001));
    }
<#else>
    /* Default clock setting is used, hence no code is generated */
    /* Code for fuse settings can be found in "initialization.c" */
</#if>

    /* Peripheral Module Disable Configuration */
<#list 1..PMD_COUNT + 1 as i>
    <#assign PMDREG_VALUE = "PMD" + i + "_REG_VALUE">
    <#if .vars[PMDREG_VALUE]?? && .vars[PMDREG_VALUE] != "None">
        <#lt>    PMD${i}SET = 0x${.vars[PMDREG_VALUE]};
    </#if>
</#list>
}
