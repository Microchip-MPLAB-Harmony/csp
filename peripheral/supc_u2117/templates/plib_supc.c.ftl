/*******************************************************************************
  Supply Controller(${SUPC_INSTANCE_NAME}) PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_${SUPC_INSTANCE_NAME?lower_case}.c

  Summary
    ${SUPC_INSTANCE_NAME} PLIB Implementation File.

  Description
    This file defines the interface to the SUPC peripheral library. This
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

<#if core.CoreSysIntFile == true>
#include "interrupts.h"
</#if>
#include "device.h"
#include "plib_${SUPC_INSTANCE_NAME?lower_case}.h"

<#assign SUPC_BKOUT_VAL = "">
<#assign SUPC_VREF_SEL_VAL = "">
<#assign SUPC_VREF_VAL = "">
<#assign SUPC_VREG_VAL = "">
<#assign SUPC_BOD_REGNAME = "SUPC_"+SUPC_BOD_NAME>
<#assign SUPC_BOD_PSEL_VAL = "">
<#assign SUPC_BOD_PSEL = "SUPC_"+SUPC_BOD_NAME+"_PSEL">
<#assign SUPC_BOD_VAL = "">
<#assign SUPC_BOD_FACTORY_DATA_MASK = "SUPC_${SUPC_BOD_NAME}_ENABLE_Msk | SUPC_${SUPC_BOD_NAME}_ACTION_Msk | SUPC_${SUPC_BOD_NAME}_HYST_Msk | SUPC_${SUPC_BOD_NAME}_LEVEL_Msk">
<#assign SUPC_VREG_FACTORY_DATA_MASK = "SUPC_VREG_ENABLE_Msk">
<#assign SUPC_BOD_RUNBKUP = "SUPC_"+SUPC_BOD_NAME+"_RUNBKUP">
<#assign SUPC_BOD_RUNSTDBY = "SUPC_"+SUPC_BOD_NAME+"_RUNSTDBY">
<#assign SUPC_BOD_STDBYCFG = "SUPC_"+SUPC_BOD_NAME+"_STDBYCFG">
<#assign SUPC_BOD_ACTCFG = "SUPC_"+SUPC_BOD_NAME+"_ACTCFG">
<#if HAS_BKOUT_REG??>
    <#if SUPC_BKOUT_0 == true>
        <#if SUPC_BKOUT_VAL != "">
            <#assign SUPC_BKOUT_VAL = SUPC_BKOUT_VAL + " | SUPC_BKOUT_ENOUT0_Msk">
        <#else>
            <#assign SUPC_BKOUT_VAL = "SUPC_BKOUT_ENOUT0_Msk">
        </#if>
    </#if>
    <#if SUPC_BKOUT_1 == true>
        <#if SUPC_BKOUT_VAL != "">
            <#assign SUPC_BKOUT_VAL = SUPC_BKOUT_VAL + " | SUPC_BKOUT_ENOUT1_Msk">
        <#else>
            <#assign SUPC_BKOUT_VAL = "SUPC_BKOUT_ENOUT1_Msk">
        </#if>
    </#if>
    <#if SUPC_BKOUT_RTCTGCL0 == true>
        <#if SUPC_BKOUT_RTCTGCL0 == true>
            <#if SUPC_BKOUT_VAL != "">
                <#assign SUPC_BKOUT_VAL = SUPC_BKOUT_VAL + " | SUPC_BKOUT_RTCTGLOUT0_Msk">
            <#else>
                <#assign SUPC_BKOUT_VAL = "SUPC_BKOUT_RTCTGLOUT0_Msk">
            </#if>
        </#if>
    </#if>
    <#if SUPC_BKOUT_RTCTGCL1 == true>
        <#if SUPC_BKOUT_RTCTGCL1 == true>
            <#if SUPC_BKOUT_VAL != "">
                <#assign SUPC_BKOUT_VAL = SUPC_BKOUT_VAL + " | SUPC_BKOUT_RTCTGLOUT1_Msk">
            <#else>
                <#assign SUPC_BKOUT_VAL = "SUPC_BKOUT_RTCTGLOUT0_Msk">
            </#if>
        </#if>
    </#if>
    <#if .vars[SUPC_BOD_RUNBKUP]?has_content >
        <#if .vars[SUPC_BOD_RUNBKUP] == true>
            <#if SUPC_BOD_VAL != "">
            <#assign SUPC_BOD_VAL = SUPC_BOD_VAL + " | SUPC_BOD33_RUNBKUP_Msk">
            <#else>
            <#assign SUPC_BOD_VAL = "SUPC_BOD33_RUNBKUP_Msk">
            </#if>
        </#if>
    </#if>
</#if>

<#if SUPC_BOD_PSEL??>
    <#assign SUPC_BOD_PSEL_VAL = "${SUPC_BOD_PSEL}(${.vars[SUPC_BOD_PSEL]}UL)">
    <#assign SUPC_BOD_VAL = SUPC_BOD_PSEL_VAL>
</#if>

<#if HAS_VREFSEL_BIT??>
    <#assign SUPC_BOD_VREFSEL = "SUPC_"+SUPC_BOD_NAME+"_VREFSEL">
    <#if .vars[SUPC_BOD_VREFSEL]?has_content >
        <#if (.vars[SUPC_BOD_VREFSEL] == "1")>
            <#if SUPC_BOD_VAL != "">
                <#assign SUPC_BOD_VAL = SUPC_BOD_VAL + " | SUPC_${SUPC_BOD_NAME}_VREFSEL_Msk">
            <#else>
                <#assign SUPC_BOD_VAL = "SUPC_${SUPC_BOD_NAME}_VREFSEL_Msk">
            </#if>
        </#if>
    </#if>
</#if>
<#if .vars[SUPC_BOD_RUNSTDBY]?has_content >
    <#if .vars[SUPC_BOD_RUNSTDBY] == true>
        <#if SUPC_BOD_VAL != "">
        <#assign SUPC_BOD_VAL = SUPC_BOD_VAL + " | SUPC_${SUPC_BOD_NAME}_RUNSTDBY_Msk">
        <#else>
        <#assign SUPC_BOD_VAL = "SUPC_${SUPC_BOD_NAME}_RUNSTDBY_Msk">
        </#if>
    </#if>
</#if>
<#if .vars[SUPC_BOD_STDBYCFG]?has_content >
    <#if .vars[SUPC_BOD_STDBYCFG] == "1">
        <#if SUPC_BOD_VAL != "">
        <#assign SUPC_BOD_VAL = SUPC_BOD_VAL + " | SUPC_${SUPC_BOD_NAME}_STDBYCFG_Msk">
        <#else>
        <#assign SUPC_BOD_VAL = "SUPC_${SUPC_BOD_NAME}_STDBYCFG_Msk">
        </#if>
    </#if>
</#if>
<#if .vars[SUPC_BOD_ACTCFG]?has_content >
    <#if .vars[SUPC_BOD_ACTCFG] == "1">
        <#if SUPC_BOD_VAL != "">
        <#assign SUPC_BOD_VAL = SUPC_BOD_VAL + " | SUPC_${SUPC_BOD_NAME}_ACTCFG_Msk">
        <#else>
        <#assign SUPC_BOD_VAL = "SUPC_${SUPC_BOD_NAME}_ACTCFG_Msk">
        </#if>
    </#if>
</#if>
<#if SUPC_VREG_SEL??>
    <#if SUPC_VREG_SEL == true >
        <#if SUPC_VREG_VAL != "">
        <#assign SUPC_VREG_VAL = SUPC_VREG_VAL + " | SUPC_VREG_SEL_BUCK">
        <#else>
        <#assign SUPC_VREG_VAL = " SUPC_VREG_SEL_BUCK">
        </#if>
    </#if>
</#if>
<#if SUPC_VREG_RUNSTDBY?has_content >
    <#if SUPC_VREG_RUNSTDBY == "1">
        <#if SUPC_VREG_VAL != "">
        <#assign SUPC_VREG_VAL = SUPC_VREG_VAL + " | SUPC_VREG_RUNSTDBY_Msk">
        <#else>
        <#assign SUPC_VREG_VAL = "SUPC_VREG_RUNSTDBY_Msk">
        </#if>
    </#if>
</#if>
<#if SUPC_VREG_VSVSTEP??>
    <#if SUPC_VREG_VAL != "">
    <#assign SUPC_VREG_VAL = SUPC_VREG_VAL + " | SUPC_VREG_VSVSTEP(${SUPC_VREG_VSVSTEP}UL)">
    <#else>
    <#assign SUPC_VREG_VAL = "SUPC_VREG_VSVSTEP(${SUPC_VREG_VSVSTEP})">
    </#if>
</#if>
<#if SUPC_VREG_VSPER??>
    <#if SUPC_VREG_VAL != "">
    <#assign SUPC_VREG_VAL = SUPC_VREG_VAL + " | SUPC_VREG_VSPER(${SUPC_VREG_VSPER}UL)">
    <#else>
    <#assign SUPC_VREG_VAL = "SUPC_VREG_VSPER(${SUPC_VREG_VSPER})">
    </#if>
</#if>
<#if HAS_LPEFF_BIT??>
    <#if SUPC_VREG_LPEFF?has_content >
        <#if SUPC_VREG_LPEFF == true >
            <#if SUPC_VREG_VAL != "">
            <#assign SUPC_VREG_VAL = SUPC_VREG_VAL + " | SUPC_VREG_LPEFF_Msk">
            <#else>
            <#assign SUPC_VREG_VAL = " SUPC_VREG_LPEFF_Msk">
            </#if>
        </#if>
    </#if>
</#if>
<#if HAS_VREFSEL_BIT??>
    <#if SUPC_VREG_VREFSEL?has_content >
        <#if SUPC_VREG_VREFSEL == "1" >
            <#if SUPC_VREG_VAL != "">
                <#assign SUPC_VREG_VAL = SUPC_VREG_VAL + " | SUPC_VREG_VREFSEL_Msk">
            <#else>
                <#assign SUPC_VREG_VAL = "SUPC_VREG_VREFSEL_Msk">
            </#if>
        </#if>
    </#if>
</#if>
<#if HAS_STDBYPL0_BIT??>
    <#if SUPC_VREG_STDBYPL0?has_content >
        <#if SUPC_VREG_STDBYPL0 == true >
            <#if SUPC_VREG_VAL != "">
            <#assign SUPC_VREG_VAL = SUPC_VREG_VAL + " | SUPC_VREG_STDBYPL0_Msk">
            <#else>
            <#assign SUPC_VREG_VAL = "SUPC_VREG_STDBYPL0_Msk">
            </#if>
        </#if>
    </#if>
</#if>
<#if SUPC_VREF_SEL?has_content >
<#assign SUPC_VREF_SEL_VAL = "SUPC_VREF_SEL("+SUPC_VREF_SEL+"UL)">
<#assign SUPC_VREF_VAL = SUPC_VREF_SEL_VAL>
</#if>
<#if SUPC_VREF_ONDEMAND?has_content >
    <#if SUPC_VREF_ONDEMAND == true>
        <#if SUPC_VREF_VAL != "">
        <#assign SUPC_VREF_VAL = SUPC_VREF_VAL + " | SUPC_VREF_ONDEMAND_Msk">
        <#else>
        <#assign SUPC_VREF_VAL = "SUPC_VREF_ONDEMAND_Msk">
        </#if>
    </#if>
</#if>
<#if SUPC_VREF_RUNSTDBY?has_content >
    <#if SUPC_VREF_RUNSTDBY == true>
        <#if SUPC_VREF_VAL != "">
        <#assign SUPC_VREF_VAL = SUPC_VREF_VAL + " | SUPC_VREF_RUNSTDBY_Msk">
        <#else>
        <#assign SUPC_VREF_VAL = "SUPC_VREF_RUNSTDBY_Msk">
        </#if>
    </#if>
</#if>
<#if SUPC_VREF_TSEN?has_content >
    <#if SUPC_VREF_TSEN == true>
        <#if SUPC_VREF_VAL != "">
        <#assign SUPC_VREF_VAL = SUPC_VREF_VAL + " | SUPC_VREF_TSEN_Msk">
        <#else>
        <#assign SUPC_VREF_VAL = "SUPC_VREF_TSEN_Msk">
        </#if>
    </#if>
</#if>
<#if SUPC_VREF_VREFOE?has_content >
    <#if SUPC_VREF_VREFOE == true>
        <#if SUPC_VREF_VAL != "">
        <#assign SUPC_VREF_VAL = SUPC_VREF_VAL + " | SUPC_VREF_VREFOE_Msk">
        <#else>
        <#assign SUPC_VREF_VAL = "SUPC_VREF_VREFOE_Msk">
        </#if>
    </#if>
</#if>
<#assign SUPC_BOD_SRDY = "B33SRDY">
<#if SUPC_BOD_NAME == "BODVDD">
<#assign SUPC_BOD_SRDY = "BVDDSRDY">
</#if>

void ${SUPC_INSTANCE_NAME}_Initialize( void )
{
<#if SUPC_BOD_VAL?has_content>
    uint32_t bodEnable = ${SUPC_INSTANCE_NAME}_REGS->${SUPC_BOD_REGNAME} & SUPC_${SUPC_BOD_NAME}_ENABLE_Msk;

    /* Configure ${SUPC_BOD_NAME}. Mask the values loaded from NVM during reset. */
    ${SUPC_INSTANCE_NAME}_REGS->${SUPC_BOD_REGNAME} &= ~SUPC_${SUPC_BOD_NAME}_ENABLE_Msk;
    ${SUPC_INSTANCE_NAME}_REGS->${SUPC_BOD_REGNAME} = (${SUPC_INSTANCE_NAME}_REGS->${SUPC_BOD_REGNAME} & (${SUPC_BOD_FACTORY_DATA_MASK})) | ${SUPC_BOD_VAL};
    if (bodEnable != 0U)
    {
        ${SUPC_INSTANCE_NAME}_REGS->${SUPC_BOD_REGNAME} |= SUPC_${SUPC_BOD_NAME}_ENABLE_Msk;

        /* Wait for ${SUPC_BOD_NAME} Synchronization Ready */
        while((${SUPC_INSTANCE_NAME}_REGS->SUPC_STATUS & SUPC_STATUS_${SUPC_BOD_SRDY}_Msk) == 0U)
        {
        }

        /* If ${SUPC_BOD_NAME} in continuous mode then wait for ${SUPC_BOD_NAME} Ready */
        if((${SUPC_INSTANCE_NAME}_REGS->${SUPC_BOD_REGNAME} & SUPC_${SUPC_BOD_NAME}_ACTCFG_Msk) == 0U)
        {
            while((${SUPC_INSTANCE_NAME}_REGS->SUPC_STATUS & SUPC_STATUS_${SUPC_BOD_NAME}RDY_Msk) == 0U)
            {
            }
        }
    }

</#if>
<#if SUPC_VREG_VAL?has_content>
    /* Configure VREG. Mask the values loaded from NVM during reset.*/
    <@compress single_line=true>${SUPC_INSTANCE_NAME}_REGS->SUPC_VREG = SUPC_VREG_ENABLE_Msk | ${SUPC_VREG_VAL};</@compress>

</#if>
<#if SUPC_VREF_VAL?has_content>
    /* Configure VREF */
    ${SUPC_INSTANCE_NAME}_REGS->SUPC_VREF = ${SUPC_VREF_VAL};

</#if>
<#if SUPC_BKOUT_VAL?has_content>
    /* Configure BKOUT */
    ${SUPC_INSTANCE_NAME}_REGS->SUPC_BKOUT = ${SUPC_BKOUT_VAL};

</#if>
<#if SUPC_BBPS_WAKEEN?has_content>
    <#if SUPC_BBPS_WAKEEN == true>
    /* Configure device wake on BBPS */
    ${SUPC_INSTANCE_NAME}_REGS->SUPC_BBPS = SUPC_BBPS_WAKEEN_Msk;
    </#if>
</#if>
<#if SUPC_INTERRUPT_ENABLE = true>
    /* Enable BOD33 detect interrupt */
    ${SUPC_INSTANCE_NAME}_REGS->SUPC_INTENSET = SUPC_INTFLAG_${SUPC_BOD_NAME}DET_Msk;
</#if>
}

<#if HAS_BKOUT_REG??>
void ${SUPC_INSTANCE_NAME}_SetOutputPin( SUPC_OUTPIN pin )
{
    ${SUPC_INSTANCE_NAME}_REGS->SUPC_BKOUT |= SUPC_BKOUT_SETOUT(1UL <<(uint32_t)pin);
}

void ${SUPC_INSTANCE_NAME}_ClearOutputPin( SUPC_OUTPIN pin )
{
    ${SUPC_INSTANCE_NAME}_REGS->SUPC_BKOUT |= SUPC_BKOUT_CLROUT(1UL <<(uint32_t)pin);
}
</#if>

<#if HAS_SEL_BIT??>
void ${SUPC_INSTANCE_NAME}_SelectVoltageRegulator(SUPC_VREGSEL regsel)
{
    if(SUPC_VREGSEL_BUCK == regsel)
    {
        ${SUPC_INSTANCE_NAME}_REGS->SUPC_VREG |= (1UL << SUPC_VREG_SEL_Pos);
    }
    else
    {
        ${SUPC_INSTANCE_NAME}_REGS->SUPC_VREG &= ~(1UL << SUPC_VREG_SEL_Pos);
    }
    while((${SUPC_INSTANCE_NAME}_REGS->SUPC_STATUS & SUPC_STATUS_VREGRDY_Msk) == 0U)
    {
        /* Do nothing */
    }
}
</#if>

<#if SUPC_INTERRUPT_ENABLE>
typedef struct
{
    SUPC_${SUPC_BOD_NAME}_CALLBACK callback;
    uintptr_t context;
} SUPC_${SUPC_BOD_NAME}_CALLBACK_OBJ;

static volatile SUPC_${SUPC_BOD_NAME}_CALLBACK_OBJ ${SUPC_INSTANCE_NAME?lower_case}CallbackObject;
</#if>

<#if SUPC_INTERRUPT_ENABLE>
void ${SUPC_INSTANCE_NAME}_${SUPC_BOD_NAME}CallbackRegister( SUPC_${SUPC_BOD_NAME}_CALLBACK callback, uintptr_t context )
{
    ${SUPC_INSTANCE_NAME?lower_case}CallbackObject.callback = callback;
    ${SUPC_INSTANCE_NAME?lower_case}CallbackObject.context = context;
}

void __attribute__((used)) ${SUPC_INSTANCE_NAME}_InterruptHandler( void )
{
    uintptr_t context = ${SUPC_INSTANCE_NAME?lower_case}CallbackObject.context;
    if ((${SUPC_INSTANCE_NAME}_REGS->SUPC_INTFLAG & SUPC_INTFLAG_${SUPC_BOD_NAME}DET_Msk) == SUPC_INTFLAG_${SUPC_BOD_NAME}DET_Msk)
    {
        ${SUPC_INSTANCE_NAME}_REGS->SUPC_INTFLAG = SUPC_INTFLAG_${SUPC_BOD_NAME}DET_Msk;

        if (${SUPC_INSTANCE_NAME?lower_case}CallbackObject.callback != NULL)
        {
            ${SUPC_INSTANCE_NAME?lower_case}CallbackObject.callback(context);
        }
    }
}
</#if>
