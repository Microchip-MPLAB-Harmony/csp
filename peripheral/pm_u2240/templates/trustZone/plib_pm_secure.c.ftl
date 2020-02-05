/*******************************************************************************
  Power Manager(${PM_INSTANCE_NAME}) PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_${PM_INSTANCE_NAME?lower_case}.c

  Summary
    ${PM_INSTANCE_NAME} PLIB Implementation File.

  Description
    This file defines the interface to the PM peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

  Remarks:
    None.

*******************************************************************************/

// DOM-IGNORE-BEGIN
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
// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
/* This section lists the other files that are included in this file.
*/

#include "device.h"
#include "plib_${PM_INSTANCE_NAME?lower_case}.h"
<#assign PM_STDBYCFG_VAL = "">
<#if PM_STDBYCFG_BBIASLP?has_content >
    <#if PM_STDBYCFG_VAL != "">
        <#assign PM_STDBYCFG_VAL = PM_STDBYCFG_VAL + "| PM_STDBYCFG_BBIASLP("+PM_STDBYCFG_BBIASLP+")">
    <#else>
        <#assign PM_STDBYCFG_VAL = "PM_STDBYCFG_BBIASLP("+PM_STDBYCFG_BBIASLP+")">
    </#if>
</#if>
<#if PM_STDBYCFG_BBIASHS?has_content >
    <#if HAS_BBIASHS_FIELD??>
        <#assign BBIASHS_VAL = PM_STDBYCFG_BBIASHS>
        <#if PM_STDBYCFG_VAL != "">
            <#assign PM_STDBYCFG_VAL = PM_STDBYCFG_VAL + "| PM_STDBYCFG_BBIASHS("+BBIASHS_VAL+")">
        <#else>
            <#assign PM_STDBYCFG_VAL = "PM_STDBYCFG_BBIASHS("+BBIASHS_VAL+")">
        </#if>
    <#else>
        <#if PM_STDBYCFG_BBIASHS>
            <#if PM_STDBYCFG_VAL != "">
                <#assign PM_STDBYCFG_VAL = PM_STDBYCFG_VAL + "| PM_STDBYCFG_BBIASHS_Msk">
            <#else>
                <#assign PM_STDBYCFG_VAL = "PM_STDBYCFG_BBIASHS_Msk">
            </#if>
        </#if>
    </#if>
</#if>
<#if PM_STDBYCFG_LINKPD?has_content >
    <#if PM_STDBYCFG_VAL != "">
        <#assign PM_STDBYCFG_VAL = PM_STDBYCFG_VAL + "| PM_STDBYCFG_LINKPD("+PM_STDBYCFG_LINKPD+")">
    <#else>
        <#assign PM_STDBYCFG_VAL = "PM_STDBYCFG_LINKPD("+PM_STDBYCFG_LINKPD+")">
    </#if>
</#if>
<#if PM_STDBYCFG_VREGSMOD?has_content >
    <#if PM_STDBYCFG_VAL != "">
        <#assign PM_STDBYCFG_VAL = PM_STDBYCFG_VAL + "| PM_STDBYCFG_VREGSMOD("+PM_STDBYCFG_VREGSMOD+")">
    <#else>
        <#assign PM_STDBYCFG_VAL = "PM_STDBYCFG_VREGSMOD("+PM_STDBYCFG_VREGSMOD+")">
    </#if>
</#if>
<#if PM_STDBYCFG_DPGPD1?has_content >
    <#if PM_STDBYCFG_DPGPD1>
        <#if PM_STDBYCFG_VAL != "">
            <#assign PM_STDBYCFG_VAL = PM_STDBYCFG_VAL + "| PM_STDBYCFG_DPGPD1_Msk">
        <#else>
            <#assign PM_STDBYCFG_VAL = "PM_STDBYCFG_DPGPD1_Msk">
        </#if>
    </#if>
</#if>
<#if PM_STDBYCFG_DPGPD0?has_content >
    <#if PM_STDBYCFG_DPGPD0>
        <#if PM_STDBYCFG_VAL != "">
            <#assign PM_STDBYCFG_VAL = PM_STDBYCFG_VAL + "| PM_STDBYCFG_DPGPD0_Msk">
        <#else>
            <#assign PM_STDBYCFG_VAL = "PM_STDBYCFG_DPGPD0_Msk">
        </#if>
    </#if>
</#if>
<#if PM_STDBYCFG_DPGPD?has_content >
    <#if PM_STDBYCFG_DPGPD>
        <#if PM_STDBYCFG_VAL != "">
            <#assign PM_STDBYCFG_VAL = PM_STDBYCFG_VAL + "| PM_STDBYCFG_DPGPDSW_Msk">
        <#else>
            <#assign PM_STDBYCFG_VAL = "PM_STDBYCFG_DPGPDSW_Msk">
        </#if>
    </#if>
</#if>
<#if PM_STDBYCFG_BBIASTR?has_content >
    <#if PM_STDBYCFG_BBIASTR>
        <#if PM_STDBYCFG_VAL != "">
            <#assign PM_STDBYCFG_VAL = PM_STDBYCFG_VAL + "| PM_STDBYCFG_BBIASTR_Msk">
        <#else>
            <#assign PM_STDBYCFG_VAL = "PM_STDBYCFG_BBIASTR_Msk">
        </#if>
    </#if>
</#if>
<#if HAS_PDCFG_FIELD??>
<#if PM_STDBYCFG_PDCFG?has_content >
    <#if PM_STDBYCFG_VAL != "">
        <#assign PM_STDBYCFG_VAL = PM_STDBYCFG_VAL + "| PM_STDBYCFG_PDCFG("+PM_STDBYCFG_PDCFG+")">
    <#else>
        <#assign PM_STDBYCFG_VAL = "PM_STDBYCFG_PDCFG("+PM_STDBYCFG_PDCFG+")">
    </#if>
</#if>
</#if>
<#if HAS_PDCFG_BIT??>
<#if PM_STDBYCFG_PDCFG?has_content >
    <#if PM_STDBYCFG_PDCFG != "0">
        <#if PM_STDBYCFG_VAL != "">
            <#assign PM_STDBYCFG_VAL = PM_STDBYCFG_VAL + "| PM_STDBYCFG_PDCFG_Msk">
        <#else>
            <#assign PM_STDBYCFG_VAL = "PM_STDBYCFG_PDCFG_Msk">
        </#if>
    </#if>
</#if>
</#if>
void ${PM_INSTANCE_NAME}_Initialize( void )
{
<#if PM_STDBYCFG_VAL?has_content>
    /* Configure PM */
    ${PM_INSTANCE_NAME}_REGS->PM_STDBYCFG = ${PM_STDBYCFG_VAL};
</#if>

<#if HAS_PLCFG??>
<#if PLCFG_PLDIS>
    ${PM_INSTANCE_NAME}_REGS->PM_PLCFG = PM_PLCFG_PLDIS_Msk;
<#else>
    /* Clear INTFLAG.PLRDY */
    ${PM_INSTANCE_NAME}_REGS->PM_INTFLAG |= PM_INTENCLR_PLRDY_Msk;

    /* Configure performance level */
    ${PM_INSTANCE_NAME}_REGS->PM_PLCFG = PM_PLCFG_PLSEL_${PM_PLCFG_PLSEL};

    /* Wait for performance level transition to complete */
    while(!(${PM_INSTANCE_NAME}_REGS->PM_INTFLAG & PM_INTFLAG_PLRDY_Msk));
</#if>
</#if>
<#if HAS_PWCFG??>
    <#if PM_PWCFG_RAMPSWC != "0x0">
        /* Clear INTFLAG.PLRDY */
    <#lt>    ${PM_INSTANCE_NAME}_REGS->PM_PWCFG = PM_PWCFG_RAMPSWC(${PM_PWCFG_RAMPSWC});
    </#if>
</#if>
}

