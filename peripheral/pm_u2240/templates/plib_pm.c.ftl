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
        <#assign PM_STDBYCFG_VAL = PM_STDBYCFG_VAL + "| PM_STDBYCFG_BBIASLP("+PM_STDBYCFG_BBIASLP+"UL)">
    <#else>
        <#assign PM_STDBYCFG_VAL = "PM_STDBYCFG_BBIASLP("+PM_STDBYCFG_BBIASLP+")">
    </#if>
</#if>
<#if PM_STDBYCFG_BBIASHS?has_content >
    <#if HAS_BBIASHS_FIELD??>
        <#assign BBIASHS_VAL = PM_STDBYCFG_BBIASHS>
        <#if PM_STDBYCFG_VAL != "">
            <#assign PM_STDBYCFG_VAL = PM_STDBYCFG_VAL + "| PM_STDBYCFG_BBIASHS("+BBIASHS_VAL+"UL)">
        <#else>
            <#assign PM_STDBYCFG_VAL = "PM_STDBYCFG_BBIASHS("+BBIASHS_VAL+"UL)">
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
        <#assign PM_STDBYCFG_VAL = PM_STDBYCFG_VAL + "| PM_STDBYCFG_LINKPD("+PM_STDBYCFG_LINKPD+"UL)">
    <#else>
        <#assign PM_STDBYCFG_VAL = "PM_STDBYCFG_LINKPD("+PM_STDBYCFG_LINKPD+"UL)">
    </#if>
</#if>
<#if PM_STDBYCFG_VREGSMOD?has_content >
    <#if PM_STDBYCFG_VAL != "">
        <#assign PM_STDBYCFG_VAL = PM_STDBYCFG_VAL + "| PM_STDBYCFG_VREGSMOD("+PM_STDBYCFG_VREGSMOD+"UL)">
    <#else>
        <#assign PM_STDBYCFG_VAL = "PM_STDBYCFG_VREGSMOD("+PM_STDBYCFG_VREGSMOD+"UL)">
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
        <#assign PM_STDBYCFG_VAL = PM_STDBYCFG_VAL + "| PM_STDBYCFG_PDCFG("+PM_STDBYCFG_PDCFG+"UL)">
    <#else>
        <#assign PM_STDBYCFG_VAL = "PM_STDBYCFG_PDCFG("+PM_STDBYCFG_PDCFG+"UL)">
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
<#if __TRUSTZONE_ENABLED?? &&  __TRUSTZONE_ENABLED == "true" && core.PM_IS_NON_SECURE >
<#else>
void ${PM_INSTANCE_NAME}_Initialize( void )
{
<#if PM_STDBYCFG_VAL?has_content>
    /* Configure PM */
    ${PM_INSTANCE_NAME}_REGS->PM_STDBYCFG = (uint16_t)(${PM_STDBYCFG_VAL});
</#if>

<#if HAS_PLCFG??>
<#if PLCFG_PLDIS>
    ${PM_INSTANCE_NAME}_REGS->PM_PLCFG = (uint8_t)PM_PLCFG_PLDIS_Msk;
<#else>
    /* Clear INTFLAG.PLRDY */
    ${PM_INSTANCE_NAME}_REGS->PM_INTFLAG |= (uint8_t)PM_INTENCLR_PLRDY_Msk;

    if ((${PM_INSTANCE_NAME}_REGS->PM_PLCFG & PM_PLCFG_PLSEL_Msk) != PM_PLCFG_PLSEL_${PM_PLCFG_PLSEL})
    {
        /* Configure performance level */
        ${PM_INSTANCE_NAME}_REGS->PM_PLCFG = (uint8_t)PM_PLCFG_PLSEL_${PM_PLCFG_PLSEL};

        while((${PM_INSTANCE_NAME}_REGS->PM_INTFLAG & PM_INTFLAG_PLRDY_Msk) == 0U)
        {
            /* Wait for performance level transition to complete */
        }
    }
</#if>
</#if>
<#if HAS_PWCFG??>
    <#if PM_PWCFG_RAMPSWC != "0x0">
        /* Clear INTFLAG.PLRDY */
    <#lt>    ${PM_INSTANCE_NAME}_REGS->PM_PWCFG = (uint8_t)PM_PWCFG_RAMPSWC(${PM_PWCFG_RAMPSWC}UL);
    </#if>
</#if>
}
</#if>

void ${PM_INSTANCE_NAME}_IdleModeEnter( void )
{
    <#if PM_IDLE_OPTION ? has_content>
    ${PM_INSTANCE_NAME}_REGS->PM_SLEEPCFG = (uint8_t)PM_SLEEPCFG_SLEEPMODE(${PM_IDLE_OPTION}UL);

    
    while ((${PM_INSTANCE_NAME}_REGS->PM_SLEEPCFG & PM_SLEEPCFG_SLEEPMODE_Msk) != PM_SLEEPCFG_SLEEPMODE(${PM_IDLE_OPTION}UL))
    {
        /* Ensure that SLEEPMODE bits are configured with the given value */
    }
    <#else>
    /* Configure Idle Sleep mode */
    ${PM_INSTANCE_NAME}_REGS->PM_SLEEPCFG = (uint8_t)PM_SLEEPCFG_SLEEPMODE_IDLE_Val;

    while ((${PM_INSTANCE_NAME}_REGS->PM_SLEEPCFG & PM_SLEEPCFG_SLEEPMODE_IDLE_Val) == 0U)
    {
        /* Ensure that SLEEPMODE bits are configured with the given value */
    }
    </#if>
    /* Wait for interrupt instruction execution */
    __WFI();
}

void ${PM_INSTANCE_NAME}_StandbyModeEnter( void )
{
    /* Configure Standby Sleep */
    ${PM_INSTANCE_NAME}_REGS->PM_SLEEPCFG = (uint8_t)PM_SLEEPCFG_SLEEPMODE_STANDBY_Val;
  
    while ((${PM_INSTANCE_NAME}_REGS->PM_SLEEPCFG & PM_SLEEPCFG_SLEEPMODE_STANDBY_Val) == 0U)
    {
        /* Ensure that SLEEPMODE bits are configured with the given value */
    }

    /* Wait for interrupt instruction execution */
    __WFI();
}

<#if HAS_BACKUP_SLEEP??>
void ${PM_INSTANCE_NAME}_BackupModeEnter( void )
{
    /* Configure Backup Sleep */
    ${PM_INSTANCE_NAME}_REGS->PM_SLEEPCFG = (uint8_t)PM_SLEEPCFG_SLEEPMODE_BACKUP_Val;
    
    while ((${PM_INSTANCE_NAME}_REGS->PM_SLEEPCFG & PM_SLEEPCFG_SLEEPMODE_BACKUP_Val) == 0U)
    {
        /* Ensure that SLEEPMODE bits are configured with the given value */
    }

    /* Wait for interrupt instruction execution */
    __WFI();
}
</#if>

<#if HAS_OFF_SLEEP??>
void ${PM_INSTANCE_NAME}_OffModeEnter( void )
{
    /* Configure Off Sleep */
    ${PM_INSTANCE_NAME}_REGS->PM_SLEEPCFG = (uint8_t)PM_SLEEPCFG_SLEEPMODE_OFF_Val;

    while ((${PM_INSTANCE_NAME}_REGS->PM_SLEEPCFG & PM_SLEEPCFG_SLEEPMODE_OFF_Val) == 0U)
    {
        /* Ensure that SLEEPMODE bits are configured with the given value */
    }

    /* Wait for interrupt instruction execution */
    __WFI();
}
</#if>
<#if HAS_IORET_BIT??>

/* ********Important Note********
 * When IORET is enabled, SWD access to the device will not be
 * available after waking up from Backup sleep until
 * the bit is cleared by the application.
 */
void ${PM_INSTANCE_NAME}_IO_RetentionSet( void )
{
    ${PM_INSTANCE_NAME}_REGS->PM_CTRLA |= (uint8_t)PM_CTRLA_IORET_Msk;
}

void ${PM_INSTANCE_NAME}_IO_RetentionClear( void )
{
    ${PM_INSTANCE_NAME}_REGS->PM_CTRLA &= (uint8_t)(~PM_CTRLA_IORET_Msk);
}
</#if>

<#if HAS_PLCFG??>
bool ${PM_INSTANCE_NAME}_ConfigurePerformanceLevel(PLCFG_PLSEL plsel)
{
    bool status = false;

    /* Write the value only if Performance Level Disable is not set */
    if ((${PM_INSTANCE_NAME}_REGS->PM_PLCFG & PM_PLCFG_PLDIS_Msk) == 0U)
    {
        if((${PM_INSTANCE_NAME}_REGS->PM_PLCFG & PM_PLCFG_PLSEL_Msk) != (uint8_t)plsel)
        {
            /* Clear INTFLAG.PLRDY */
            ${PM_INSTANCE_NAME}_REGS->PM_INTFLAG |= (uint8_t)PM_INTENCLR_PLRDY_Msk;

            /* Write PLSEL bits */
            ${PM_INSTANCE_NAME}_REGS->PM_PLCFG  = (uint8_t)plsel;

            while((${PM_INSTANCE_NAME}_REGS->PM_INTFLAG & PM_INTFLAG_PLRDY_Msk) == 0U)
            {
                /* Wait for performance level transition to complete */
            }

            status = true;
        }
    }

    return status;
}

</#if>
