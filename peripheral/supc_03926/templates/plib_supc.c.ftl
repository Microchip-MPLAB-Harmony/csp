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
* Copyright (C) 2021 Microchip Technology Inc. and its subsidiaries.
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
<#if core.CoreSysIntFile == true>
#include "interrupts.h"
</#if>
<#assign SUPC_BOR_VAL = "">
<#assign SUPC_BKOUT_VAL = "">
<#assign SUPC_VREF_VAL = "">
<#assign SUPC_LVD_VAL = "">
<#assign SUPC_VREG_VAL = "">
<#if SUPC_BOR_DCBORPSEL?has_content>
    <#if SUPC_BOR_VAL != "">
        <#assign SUPC_BOR_VAL = SUPC_BOR_VAL + " | SUPC_BOR_DCBORPSEL("+SUPC_BOR_DCBORPSEL+")">
    <#else>
        <#assign SUPC_BOR_VAL = "SUPC_BOR_DCBORPSEL("+SUPC_BOR_DCBORPSEL+"U)">
    </#if>
</#if>
<#if SUPC_BOR_BORFILT?has_content>
    <#if SUPC_BOR_VAL != "">
        <#assign SUPC_BOR_VAL = SUPC_BOR_VAL + " | SUPC_BOR_BORFILT("+SUPC_BOR_BORFILT+"U)">
    <#else>
        <#assign SUPC_BOR_VAL = "SUPC_BOR_BORFILT("+SUPC_BOR_BORFILT+")">
    </#if>
</#if>
<#if SUPC_LVD_ENABLE == true>
    <#assign SUPC_LVD_VAL = "SUPC_LVD_ENABLE_Msk">
    <#if SUPC_LVD_DIR?has_content>
        <#if SUPC_LVD_VAL != "">
            <#assign SUPC_LVD_VAL = SUPC_LVD_VAL + " | SUPC_LVD_DIR("+SUPC_LVD_DIR+"U)">
        <#else>
            <#assign SUPC_LVD_VAL = "SUPC_LVD_DIR("+SUPC_LVD_DIR+")">
        </#if>
    </#if>
    <#if SUPC_LVD_OEVEN == true>
        <#if SUPC_LVD_VAL != "">
            <#assign SUPC_LVD_VAL = SUPC_LVD_VAL + " | SUPC_LVD_OEVEN_Msk">
        <#else>
            <#assign SUPC_LVD_VAL = "SUPC_LVD_OEVEN_Msk">
        </#if>
    </#if>
    <#if SUPC_LVD_RUNSTDBY == true>
        <#if SUPC_LVD_VAL != "">
            <#assign SUPC_LVD_VAL = SUPC_LVD_VAL + " | SUPC_LVD_RUNSTDBY_Msk">
        <#else>
            <#assign SUPC_LVD_VAL = "SUPC_LVD_RUNSTDBY_Msk">
        </#if>
    </#if>
</#if>
<#if SUPC_BKOUT_0 == true>
    <#if SUPC_BKOUT_VAL != "">
        <#assign SUPC_BKOUT_VAL = SUPC_BKOUT_VAL + " | SUPC_BKOUT_EN0_Msk">
    <#else>
        <#assign SUPC_BKOUT_VAL = "SUPC_BKOUT_EN0_Msk">
    </#if>
</#if>
<#if SUPC_BKOUT_1 == true>
    <#if SUPC_BKOUT_VAL != "">
        <#assign SUPC_BKOUT_VAL = SUPC_BKOUT_VAL + " | SUPC_BKOUT_EN1_Msk">
    <#else>
        <#assign SUPC_BKOUT_VAL = "SUPC_BKOUT_EN1_Msk">
    </#if>
</#if>
<#if SUPC_BKOUT_TGLOM0?has_content>
        <#if SUPC_BKOUT_VAL != "">
            <#assign SUPC_BKOUT_VAL = SUPC_BKOUT_VAL + " | SUPC_BKOUT_TGLOM0("+SUPC_BKOUT_TGLOM0+")">
        <#else>
            <#assign SUPC_BKOUT_VAL = "SUPC_BKOUT_TGLOM0("+SUPC_BKOUT_TGLOM0+"U)">
        </#if>
</#if>
<#if SUPC_BKOUT_TGLOM1?has_content>
        <#if SUPC_BKOUT_VAL != "">
            <#assign SUPC_BKOUT_VAL = SUPC_BKOUT_VAL + " | SUPC_BKOUT_TGLOM1("+SUPC_BKOUT_TGLOM1+"U)">
        <#else>
            <#assign SUPC_BKOUT_VAL = "SUPC_BKOUT_TGLOM1("+SUPC_BKOUT_TGLOM1+")">
        </#if>
</#if>
<#if SUPC_VREF_LPSTDBY?has_content>
    <#if SUPC_VREF_VAL != "">
        <#assign SUPC_VREF_VAL = SUPC_VREF_VAL + " | SUPC_VREFCTRL_LPSTDBY("+SUPC_VREF_LPSTDBY+")">
    <#else>
        <#assign SUPC_VREF_VAL = "SUPC_VREFCTRL_LPSTDBY("+SUPC_VREF_LPSTDBY+"U)">
    </#if>
</#if>
<#if SUPC_VREF_LPHIB?has_content>
    <#if SUPC_VREF_VAL != "">
        <#assign SUPC_VREF_VAL = SUPC_VREF_VAL + " | SUPC_VREFCTRL_LPHIB("+SUPC_VREF_LPHIB+"U)">
    <#else>
        <#assign SUPC_VREF_VAL = "SUPC_VREFCTRL_LPHIB("+SUPC_VREF_LPHIB+")">
    </#if>
</#if>
<#if SUPC_VREF_TSEN == true>
    <#if SUPC_VREF_VAL != "">
        <#assign SUPC_VREF_VAL = SUPC_VREF_VAL + " | SUPC_VREFCTRL_TSEN_Msk">
    <#else>
        <#assign SUPC_VREF_VAL = "SUPC_VREFCTRL_TSEN_Msk">
    </#if>
</#if>
<#if SUPC_VREGCTRL_VREGOUT?has_content>
    <#if SUPC_VREG_VAL != "">
        <#assign SUPC_VREG_VAL = SUPC_VREG_VAL + " | SUPC_VREGCTRL_VREGOUT("+SUPC_VREGCTRL_VREGOUT+")">
    <#else>
        <#assign SUPC_VREG_VAL = "SUPC_VREGCTRL_VREGOUT("+SUPC_VREGCTRL_VREGOUT+"U)">
    </#if>
</#if>
<#if SUPC_VREGCTRL_OFFSTDBY == true>
    <#if SUPC_VREG_VAL != "">
        <#assign SUPC_VREG_VAL = SUPC_VREG_VAL + " | SUPC_VREGCTRL_OFFSTDBY_Msk">
    <#else>
        <#assign SUPC_VREG_VAL = "SUPC_VREGCTRL_OFFSTDBY_Msk">
    </#if>
</#if>
<#if SUPC_VREGCTRL_LVSTDBY == true>
    <#if SUPC_VREG_VAL != "">
        <#assign SUPC_VREG_VAL = SUPC_VREG_VAL + " | SUPC_VREGCTRL_LVSTDBY_Msk">
    <#else>
        <#assign SUPC_VREG_VAL = "SUPC_VREGCTRL_LVSTDBY_Msk">
    </#if>
</#if>
<#if SUPC_VREGCTRL_LVHIB == true>
    <#if SUPC_VREG_VAL != "">
        <#assign SUPC_VREG_VAL = SUPC_VREG_VAL + " | SUPC_VREGCTRL_LVHIB_Msk">
    <#else>
        <#assign SUPC_VREG_VAL = "SUPC_VREGCTRL_LVHIB_Msk">
    </#if>
</#if>
<#if SUPC_VREGCTRL_CPEN == true>
    <#if SUPC_VREG_VAL != "">
        <#assign SUPC_VREG_VAL = SUPC_VREG_VAL + " | SUPC_VREGCTRL_CPEN_Msk">
    <#else>
        <#assign SUPC_VREG_VAL = "SUPC_VREGCTRL_CPEN_Msk">
    </#if>
</#if>
<#if SUPC_VREGCTRL_AVREGEN == true>
    <#if SUPC_VREG_VAL != "">
        <#assign SUPC_VREG_VAL = SUPC_VREG_VAL + " | SUPC_VREGCTRL_AVREGEN_Msk">
    <#else>
        <#assign SUPC_VREG_VAL = "SUPC_VREGCTRL_AVREGEN_Msk">
    </#if>
</#if>
<#if SUPC_VREGCTRL_AVREGSTDBY?has_content>
    <#if SUPC_VREG_VAL != "">
        <#assign SUPC_VREG_VAL = SUPC_VREG_VAL + " | SUPC_VREGCTRL_AVREGSTDBY("+SUPC_VREGCTRL_AVREGSTDBY+"U)">
    <#else>
        <#assign SUPC_VREG_VAL = "SUPC_VREGCTRL_AVREGSTDBY("+SUPC_VREGCTRL_AVREGSTDBY+")">
    </#if>
</#if>

<#if SUPC_INTERRUPT_ENABLE = true>
typedef struct
{
    SUPC_CALLBACK callback;
    uintptr_t context;
} SUPC_CALLBACK_OBJ;

SUPC_CALLBACK_OBJ ${SUPC_INSTANCE_NAME?lower_case}CallbackObject;
</#if>

void ${SUPC_INSTANCE_NAME}_Initialize( void )
{
<#if SUPC_BOR_VAL?has_content>
    /* Configure BOR */
    ${SUPC_INSTANCE_NAME}_REGS->SUPC_BOR = ${SUPC_BOR_VAL};

</#if>
<#if SUPC_LVD_ENABLE == true>
    /* Configure LVD */
    ${SUPC_INSTANCE_NAME}_REGS->SUPC_LVD = ${SUPC_LVD_VAL};

</#if>
<#if SUPC_VREF_VAL?has_content>
    /* Configure VREF */
    ${SUPC_INSTANCE_NAME}_REGS->SUPC_VREFCTRL = ${SUPC_VREF_VAL};

</#if>
<#if SUPC_BKOUT_VAL?has_content>
    /* Configure BKOUT */
    ${SUPC_INSTANCE_NAME}_REGS->SUPC_BKOUT = ${SUPC_BKOUT_VAL};

</#if>
<#if SUPC_INTERRUPT_ENABLE = true>
    /* Enable BORVDDUSB interrupt */
    ${SUPC_INSTANCE_NAME}_REGS->SUPC_INTENSET = SUPC_INTENSET_BORVDDUSB_Msk;

</#if>
<#if SUPC_VREG_VAL?has_content>
    /* Configure VREG */
    ${SUPC_INSTANCE_NAME}_REGS->SUPC_VREGCTRL = ${SUPC_VREG_VAL};
</#if>
}

void ${SUPC_INSTANCE_NAME}_SetOutputPin( SUPC_OUTPIN pin )
{
    if (pin == SUPC_OUTPIN_OUT0)
    {
        ${SUPC_INSTANCE_NAME}_REGS->SUPC_BKOUT |= SUPC_BKOUT_SET0_Msk;
    }
    else
    {
        ${SUPC_INSTANCE_NAME}_REGS->SUPC_BKOUT |= SUPC_BKOUT_SET1_Msk;
    }
}

void ${SUPC_INSTANCE_NAME}_ClearOutputPin( SUPC_OUTPIN pin )
{
    if (pin == SUPC_OUTPIN_OUT0)
    {
        ${SUPC_INSTANCE_NAME}_REGS->SUPC_BKOUT |= SUPC_BKOUT_CLR0_Msk;
    }
    else
    {
        ${SUPC_INSTANCE_NAME}_REGS->SUPC_BKOUT |= SUPC_BKOUT_CLR1_Msk;
    }
}

<#if SUPC_INTERRUPT_ENABLE = true>
void ${SUPC_INSTANCE_NAME}_CallbackRegister(SUPC_CALLBACK callback, uintptr_t context)
{
    ${SUPC_INSTANCE_NAME?lower_case}CallbackObject.callback = callback;
    ${SUPC_INSTANCE_NAME?lower_case}CallbackObject.context = context;
}

void ${SUPC_INSTANCE_NAME}_InterruptHandler(void)
{
    ${SUPC_INSTANCE_NAME}_REGS->SUPC_INTFLAG = SUPC_INTFLAG_BORVDDUSB_Msk;

    if (${SUPC_INSTANCE_NAME?lower_case}CallbackObject.callback != NULL)
    {
        ${SUPC_INSTANCE_NAME?lower_case}CallbackObject.callback(${SUPC_INSTANCE_NAME?lower_case}CallbackObject.context);
    }
}
</#if>
