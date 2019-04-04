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
#include "plib_${SUPC_INSTANCE_NAME?lower_case}.h"
<#assign SUPC_BKOUT_VAL = "">
<#assign SUPC_VREF_SEL_VAL = "">
<#assign SUPC_VREF_VAL = "">
<#assign SUPC_BOD33_PSEL_VAL = "">
<#assign SUPC_BOD33_VAL = "">
<#assign SUPC_BOD33_FACTORY_DATA_MASK = "SUPC_BOD33_ENABLE_Msk | SUPC_BOD33_ACTION_Msk | SUPC_BOD33_HYST_Msk | SUPC_BOD33_LEVEL_Msk">
<#assign SUPC_VREG_FACTORY_DATA_MASK = "SUPC_VREG_SEL_Msk | SUPC_VREG_ENABLE_Msk">
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
<#if SUPC_BOD33_RUNHIB == true || SUPC_BOD33_RUNBKUP == true || SUPC_BOD33_STDBYCFG == "1">
    <#if SUPC_BOD33_PSEL?has_content >
        <#assign SUPC_BOD33_PSEL_VAL = "SUPC_BOD33_PSEL("+SUPC_BOD33_PSEL+")">
        <#assign SUPC_BOD33_VAL = SUPC_BOD33_PSEL_VAL>
    </#if>
</#if>
<#if SUPC_BOD33_RUNHIB?has_content >
    <#if SUPC_BOD33_RUNHIB == true>
        <#if SUPC_BOD33_VAL != "">
        <#assign SUPC_BOD33_VAL = SUPC_BOD33_VAL + " | SUPC_BOD33_RUNHIB_Msk">
        <#else>
        <#assign SUPC_BOD33_VAL = "SUPC_BOD33_RUNHIB_Msk">
        </#if>
    </#if>
</#if>
<#if SUPC_BOD33_RUNBKUP?has_content >
    <#if SUPC_BOD33_RUNBKUP == true>
        <#if SUPC_BOD33_VAL != "">
        <#assign SUPC_BOD33_VAL = SUPC_BOD33_VAL + " | SUPC_BOD33_RUNBKUP_Msk">
        <#else>
        <#assign SUPC_BOD33_VAL = "SUPC_BOD33_RUNBKUP_Msk">
        </#if>
    </#if>
</#if>
<#if SUPC_BOD33_RUNSTDBY?has_content >
    <#if SUPC_BOD33_RUNSTDBY == true>
        <#if SUPC_BOD33_VAL != "">
        <#assign SUPC_BOD33_VAL = SUPC_BOD33_VAL + " | SUPC_BOD33_RUNSTDBY_Msk">
        <#else>
        <#assign SUPC_BOD33_VAL = "SUPC_BOD33_RUNSTDBY_Msk">
        </#if>
    </#if>
</#if>
<#if SUPC_BOD33_STDBYCFG?has_content >
    <#if SUPC_BOD33_STDBYCFG == "1">
        <#if SUPC_BOD33_VAL != "">
        <#assign SUPC_BOD33_VAL = SUPC_BOD33_VAL + " | SUPC_BOD33_STDBYCFG_Msk">
        <#else>
        <#assign SUPC_BOD33_VAL = "SUPC_BOD33_STDBYCFG_Msk">
        </#if>
    </#if>
</#if>

<#if SUPC_VREF_SEL?has_content >
<#assign SUPC_VREF_SEL_VAL = "SUPC_VREF_SEL("+SUPC_VREF_SEL+")">
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
<#if SUPC_INTERRUPT_ENABLE = true>
typedef struct
{
    SUPC_BOD33_CALLBACK callback;
    uintptr_t context;
} SUPC_BOD33_CALLBACK_OBJ;

SUPC_BOD33_CALLBACK_OBJ ${SUPC_INSTANCE_NAME?lower_case}CallbackObject;
</#if>

void ${SUPC_INSTANCE_NAME}_Initialize( void )
{
<#if SUPC_BOD33_VAL?has_content>
    /* Configure BOD33. Mask the values loaded from NVM during reset. */
    ${SUPC_INSTANCE_NAME}_REGS->SUPC_BOD33 = (${SUPC_INSTANCE_NAME}_REGS->SUPC_BOD33 & (${SUPC_BOD33_FACTORY_DATA_MASK})) | ${SUPC_BOD33_VAL};

</#if>
<#if SUPC_VREF_VAL?has_content>
    /* Configure VREF */
    ${SUPC_INSTANCE_NAME}_REGS->SUPC_VREF = ${SUPC_VREF_VAL};

</#if>
<#if SUPC_BKOUT_VAL?has_content>
    /* Configure BKOUT */
    ${SUPC_INSTANCE_NAME}_REGS->SUPC_BKOUT = ${SUPC_BKOUT_VAL};

</#if>
<#if SUPC_BBPS_WAKEEN == true>
    /* Configure device wake on BBPS */
    ${SUPC_INSTANCE_NAME}_REGS->SUPC_BBPS = SUPC_BBPS_WAKEEN_Msk;

</#if>
<#if SUPC_INTERRUPT_ENABLE = true>
    /* Enable BOD33 detect interrupt */
    ${SUPC_INSTANCE_NAME}_REGS->SUPC_INTENSET = SUPC_INTFLAG_BOD33DET_Msk;

</#if>
    /* Configure VREG. Mask the values loaded from NVM during reset.*/
    <@compress single_line=true>${SUPC_INSTANCE_NAME}_REGS->SUPC_VREG = (${SUPC_INSTANCE_NAME}_REGS->SUPC_VREG & (${SUPC_VREG_FACTORY_DATA_MASK}))
                                                          | SUPC_VREG_VSPER(${SUPC_VREG_VSPER})
                                                          ${(SUPC_VREG_RUNBKUP == "1")?then ('| SUPC_VREG_RUNBKUP_Msk', '')}
                                                          ${SUPC_VREG_VSEN?then('| SUPC_VREG_VSEN_Msk', '')};</@compress>
}

void ${SUPC_INSTANCE_NAME}_SelectTempSenorChannel( SUPC_TSSEL sensor )
{
    ${SUPC_INSTANCE_NAME}_REGS->SUPC_VREF = (${SUPC_INSTANCE_NAME}_REGS->SUPC_VREF & (~SUPC_VREF_TSSEL_Msk)) | (sensor << SUPC_VREF_TSSEL_Pos);
}

void ${SUPC_INSTANCE_NAME}_SetOutputPin( SUPC_OUTPIN pin )
{
    ${SUPC_INSTANCE_NAME}_REGS->SUPC_BKOUT |= SUPC_BKOUT_SETOUT(1 << pin);
}

void ${SUPC_INSTANCE_NAME}_SelectVoltageRegulator(SUPC_VREGSEL regsel)
{
    ${SUPC_INSTANCE_NAME}_REGS->SUPC_VREG |= (regsel << SUPC_VREG_SEL_Pos);
    while(!(${SUPC_INSTANCE_NAME}_REGS->SUPC_STATUS & SUPC_STATUS_VREGRDY_Msk));
}


void ${SUPC_INSTANCE_NAME}_ClearOutputPin( SUPC_OUTPIN pin )
{
    ${SUPC_INSTANCE_NAME}_REGS->SUPC_BKOUT |= SUPC_BKOUT_CLROUT(1 << pin);
}

<#if SUPC_INTERRUPT_ENABLE = true>
void ${SUPC_INSTANCE_NAME}_BOD33CallbackRegister( SUPC_BOD33_CALLBACK callback, uintptr_t context )
{
    ${SUPC_INSTANCE_NAME?lower_case}CallbackObject.callback = callback;
    ${SUPC_INSTANCE_NAME?lower_case}CallbackObject.context = context;
}

void ${SUPC_INSTANCE_NAME}_BODDET_InterruptHandler( void )
{
    ${SUPC_INSTANCE_NAME}_REGS->SUPC_INTFLAG = SUPC_INTFLAG_BOD33DET_Msk;

    if (${SUPC_INSTANCE_NAME?lower_case}CallbackObject.callback != NULL)
    {
        ${SUPC_INSTANCE_NAME?lower_case}CallbackObject.callback(${SUPC_INSTANCE_NAME?lower_case}CallbackObject.context);
    }
}
</#if>
