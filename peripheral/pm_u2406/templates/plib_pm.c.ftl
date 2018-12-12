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
* Copyright (C) 2018 Microchip Technology Inc. and its subsidiaries.
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
<#assign PM_HIBCFG_VAL = "">
<#if PM_STDBYCFG_RAMCFG?has_content >
        <#if PM_STDBYCFG_VAL != "">
        <#assign PM_STDBYCFG_VAL = PM_STDBYCFG_VAL + "| PM_STDBYCFG_RAMCFG("+PM_STDBYCFG_RAMCFG+")">
        <#else>
        <#assign PM_STDBYCFG_VAL = "PM_STDBYCFG_RAMCFG("+PM_STDBYCFG_RAMCFG+")">
    </#if>
</#if>
<#if PM_STDBYCFG_FASTWKUP?has_content >
        <#if PM_STDBYCFG_VAL != "">
        <#assign PM_STDBYCFG_VAL = PM_STDBYCFG_VAL + "| PM_STDBYCFG_FASTWKUP("+PM_STDBYCFG_FASTWKUP+")">
        <#else>
        <#assign PM_STDBYCFG_VAL = "PM_STDBYCFG_FASTWKUP("+PM_STDBYCFG_RAMCFG+")">
    </#if>
</#if>
<#if PM_HIBCFG_RAMCFG?has_content >
        <#if PM_HIBCFG_VAL != "">
        <#assign PM_HIBCFG_VAL = PM_HIBCFG_VAL + "| PM_HIBCFG_RAMCFG("+PM_HIBCFG_RAMCFG+")">
        <#else>
        <#assign PM_HIBCFG_VAL = "PM_HIBCFG_RAMCFG("+PM_HIBCFG_RAMCFG+")">
    </#if>
</#if>
<#if PM_HIBCFG_BRAMCFG?has_content >
        <#if PM_HIBCFG_VAL != "">
        <#assign PM_HIBCFG_VAL = PM_HIBCFG_VAL + "| PM_HIBCFG_BRAMCFG("+PM_HIBCFG_BRAMCFG+")">
        <#else>
        <#assign PM_HIBCFG_VAL = "PM_HIBCFG_BRAMCFG("+PM_HIBCFG_BRAMCFG+")">
    </#if>
</#if>
void ${PM_INSTANCE_NAME}_Initialize( void )
{
<#if PM_STDBYCFG_VAL?has_content>
    /* Configure PM */
    ${PM_INSTANCE_NAME}_REGS->PM_STDBYCFG = ${PM_STDBYCFG_VAL};
    ${PM_INSTANCE_NAME}_REGS->PM_HIBCFG = ${PM_HIBCFG_VAL};
    <#if PM_HIBCFG_BRAMCFG?has_content >
    ${PM_INSTANCE_NAME}_REGS->PM_BKUPCFG = PM_BKUPCFG_BRAMCFG(${PM_BKUPCFG_BRAMCFG});
    </#if>
</#if>
}

void ${PM_INSTANCE_NAME}_IdleModeEnter( void )
{
    /* Configure Idle Sleep */
    ${PM_INSTANCE_NAME}_REGS->PM_SLEEPCFG = PM_SLEEPCFG_SLEEPMODE_IDLE_Val;
    /* Wait for interrupt instruction execution */
    __WFI();
}

void ${PM_INSTANCE_NAME}_StandbyModeEnter( void )
{
    /* Configure Standby Sleep */
    ${PM_INSTANCE_NAME}_REGS->PM_SLEEPCFG = PM_SLEEPCFG_SLEEPMODE_STANDBY_Val;
    /* Wait till the voltage regulator low power mode is ready */
    while(!${PM_INSTANCE_NAME}_REGS->PM_INTFLAG & PM_INTFLAG_SLEEPRDY_Msk);
    /* Wait for interrupt instruction execution */
    __WFI();
}

void ${PM_INSTANCE_NAME}_HibernateModeEnter( void )
{
    /* Configure Hibernate Sleep */
    ${PM_INSTANCE_NAME}_REGS->PM_SLEEPCFG = PM_SLEEPCFG_SLEEPMODE_HIBERNATE_Val;
    /* Wait till the voltage regulator low power mode is ready */
    while(!${PM_INSTANCE_NAME}_REGS->PM_INTFLAG & PM_INTFLAG_SLEEPRDY_Msk);
    /* Wait for interrupt instruction execution */
    __WFI();
}

void ${PM_INSTANCE_NAME}_BackupModeEnter( void )
{
    /* Configure Backup Sleep */
    ${PM_INSTANCE_NAME}_REGS->PM_SLEEPCFG = PM_SLEEPCFG_SLEEPMODE_BACKUP_Val;
    /* Wait till the voltage regulator low power mode is ready */
    while(!${PM_INSTANCE_NAME}_REGS->PM_INTFLAG & PM_INTFLAG_SLEEPRDY_Msk);
    /* Wait for interrupt instruction execution */
    __WFI();
}

void ${PM_INSTANCE_NAME}_OffModeEnter( void )
{
    /* Configure Off Sleep */
    ${PM_INSTANCE_NAME}_REGS->PM_SLEEPCFG = PM_SLEEPCFG_SLEEPMODE_OFF_Val;
    /* Wait for interrupt instruction execution */
    __WFI();
}

/* ********Important Note********
 * Refer the bit description of PM->CTRLA.IORET
 * in datasheet before using this function.
 * When IORET is enabled, SWD access to the device will not be
 * available after waking up from Hibernate/Backup sleep until
 * the bit is cleared by the application.
 */
void ${PM_INSTANCE_NAME}_IO_RetentionSet( void )
{
    ${PM_INSTANCE_NAME}_REGS->PM_CTRLA |= PM_CTRLA_IORET_Msk;
}

void ${PM_INSTANCE_NAME}_IO_RetentionClear( void )
{
    ${PM_INSTANCE_NAME}_REGS->PM_CTRLA &= (~PM_CTRLA_IORET_Msk);
}


