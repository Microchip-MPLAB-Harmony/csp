/*******************************************************************************
  Analog Comparator PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${AC_INSTANCE_NAME?lower_case}.c

  Summary:
    AC Source File

  Description:
    This file defines the interface to the AC peripheral library.
    This library provides access to and control of the associated
    Analog Comparator.

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
#include "plib_${AC_INSTANCE_NAME?lower_case}.h"
<#assign AC_WINCTRL_VAL = "">
<#assign AC_EVCTRL_VAL = "">
<#assign AC_INTENSET_VAL = "">
<#if AC_WINCTRL_WIN0 == true>
    <#if AC_WINCTRL_VAL != "">
        <#assign AC_WINCTRL_VAL = AC_WINCTRL_VAL + " | AC_WINCTRL_WEN0_Msk">
    <#else>
        <#assign AC_WINCTRL_VAL = "AC_WINCTRL_WEN0_Msk">
    </#if>
</#if>
<#if AC_WINCTRL_WIN0 == true>
    <#if AC_WINTSEL0 ?has_content >
        <#if AC_WINCTRL_VAL != "">
            <#assign AC_WINCTRL_VAL = AC_WINCTRL_VAL + " | AC_WINCTRL_WEN0(${AC_WINTSEL0})">
        <#else>
            <#assign AC_WINCTRL_VAL = "AC_WINCTRL_WEN0(${AC_WINTSEL0})">
        </#if>
    </#if>
</#if>
<#if AC_WINCTRL_WIN1 == true>
    <#if AC_WINCTRL_VAL != "">
        <#assign AC_WINCTRL_VAL = AC_WINCTRL_VAL + " | AC_WINCTRL_WEN1_Msk">
    <#else>
        <#assign AC_WINCTRL_VAL = "AC_WINCTRL_WEN1_Msk">
    </#if>
</#if>
<#if AC_WINCTRL_WIN1 == true>
    <#if AC_WINTSEL1 ?has_content >
        <#if AC_WINCTRL_VAL != "">
            <#assign AC_WINCTRL_VAL = AC_WINCTRL_VAL + " | AC_WINCTRL_WEN1(${AC_WINTSEL1})">
        <#else>
            <#assign AC_WINCTRL_VAL = "AC_WINCTRL_WEN1(${AC_WINTSEL1})">
        </#if>
    </#if>
</#if>
<#list 0..(AC_NUM_COMPARATORS-1) as i>
    <#assign COMP_ENABLE = "ANALOG_COMPARATOR_ENABLE_"+i>
    <#if COMP_ENABLE ?has_content >
        <#if .vars[COMP_ENABLE] == true >
            <#assign AC_COMPEI = "AC_EVCTRL_COMPEI"+i>
            <#assign AC_COMPEO = "AC_EVCTRL_COMPEO"+i>
            <#if .vars[AC_COMPEI] == true>
                <#if AC_EVCTRL_VAL != "">
                    <#assign AC_EVCTRL_VAL = AC_EVCTRL_VAL + "| AC_EVCTRL_COMPEI"+i+"_Msk">
                <#else>
                    <#assign AC_EVCTRL_VAL = " AC_EVCTRL_COMPEI"+i+"_Msk">
                </#if>
            </#if>
            <#if .vars[AC_COMPEO] == true>
                <#if AC_EVCTRL_VAL != "">
                    <#assign AC_EVCTRL_VAL = AC_EVCTRL_VAL + "| AC_EVCTRL_COMPEO"+i+"_Msk">
                <#else>
                    <#assign AC_EVCTRL_VAL = " AC_EVCTRL_COMPEO"+i+"_Msk">
                </#if>
            </#if>
        </#if>
    </#if>
</#list>
<#list 0..(AC_NUM_COMPARATORS-1) as i>
    <#assign COMP_ENABLE = "ANALOG_COMPARATOR_ENABLE_"+i>
    <#if COMP_ENABLE ?has_content >
        <#if .vars[COMP_ENABLE] == true >
            <#if AC_EVCTRL_WINEO0 == true>
                <#if AC_EVCTRL_VAL != "">
                <#assign AC_EVCTRL_VAL = AC_EVCTRL_VAL + " | AC_EVCTRL_WINEO0_Msk">
                <#else>
                <#assign AC_EVCTRL_VAL = "AC_EVCTRL_WINEO0_Msk">
                </#if>
            </#if>
            <#if AC_EVCTRL_WINEO1 == true>
                <#if AC_EVCTRL_VAL != "">
                <#assign AC_EVCTRL_VAL = AC_EVCTRL_VAL + " | AC_EVCTRL_WINEO1_Msk">
                <#else>
                <#assign AC_EVCTRL_VAL = "AC_EVCTRL_WINEO1_Msk">
                </#if>
            </#if>
        </#if>
    </#if>
</#list>
<#list 0..(AC_NUM_COMPARATORS-1) as i>
    <#assign COMP_ENABLE = "ANALOG_COMPARATOR_ENABLE_"+i>
    <#if COMP_ENABLE ?has_content >
        <#if .vars[COMP_ENABLE] == true >
            <#assign AC_COMP_INT_EN = "COMP"+i+"INTERRUPT_ENABLE">
            <#if AC_COMP_INT_EN ?has_content >
                <#if .vars[AC_COMP_INT_EN] == true>
                    <#if AC_INTENSET_VAL != "">
                        <#assign AC_INTENSET_VAL = AC_INTENSET_VAL + "| AC_INTENSET_COMP"+i+"_Msk">
                    <#else>
                        <#assign AC_INTENSET_VAL = " AC_INTENSET_COMP"+i+"_Msk">
                    </#if>
                </#if>
            </#if>
        </#if>
    </#if>
</#list>
<#if AC_INTENSET_WIN0?has_content >
    <#if AC_INTENSET_WIN0 == true>
        <#if AC_INTENSET_VAL != "">
        <#assign AC_INTENSET_VAL = AC_INTENSET_VAL + " | AC_INTENSET_WIN0_Msk">
        <#else>
        <#assign AC_INTENSET_VAL = "AC_EVCTRL_WINEO0_Msk">
        </#if>
    </#if>
</#if>
<#if AC_INTENSET_WIN1?has_content >
    <#if AC_INTENSET_WIN1 == true>
        <#if AC_INTENSET_VAL != "">
        <#assign AC_INTENSET_VAL = AC_INTENSET_VAL + " | AC_INTENSET_WIN1_Msk">
        <#else>
        <#assign AC_INTENSET_VAL = "AC_INTENSET_WIN1_Msk">
        </#if>
    </#if>
</#if>
AC_OBJECT ${AC_INSTANCE_NAME?lower_case}Obj;

// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************

void ${AC_INSTANCE_NAME}_Initialize(void)
{
    /*Reset AC registers*/
     AC_REGS->AC_CTRLA = AC_CTRLA_SWRST_Msk;

     /* Disable the module and configure COMPCTRL */
    <#list 0..4 as i>
    <#assign ANALOG_COMPARATOR_ENABLE = "ANALOG_COMPARATOR_ENABLE_" + i>
    <#assign AC_COMPCTRL_SINGLE_MODE = "AC_COMPCTRL_" + i +"SINGLE_MODE">
    <#assign AC_COMPCTRL_MUX_POS = "AC" + i + "_MUX_POS">
    <#assign AC_COMPCTRL_MUX_NEG = "AC" + i + "_MUX_NEG">
    <#assign AC_COMPCTRL_OUTPUT_TYPE = "AC" + i + "_OUTPUT_TYPE">
    <#assign AC_COMPCTRL_INTSEL = "AC" + i + "_ISEL">
    <#assign AC_COMPCTRL_HYSTEN = "AC" + i + "_HYSTEN">
    <#assign AC_SCALERn = "AC_SCALER_N_" + i>
        <#if .vars[ANALOG_COMPARATOR_ENABLE]?has_content>
            <#if (.vars[ANALOG_COMPARATOR_ENABLE] != false)>
    AC_REGS->AC_COMPCTRL[${i}] &= ~(AC_COMPCTRL_ENABLE_Msk);
    <@compress single_line=true>AC_REGS->AC_COMPCTRL[${i}] = AC_COMPCTRL_MUXPOS_${.vars[AC_COMPCTRL_MUX_POS]}
                                  | AC_COMPCTRL_MUXNEG_${.vars[AC_COMPCTRL_MUX_NEG]}
                                  | AC_COMPCTRL_INTSEL_${.vars[AC_COMPCTRL_INTSEL]}
                                  | AC_COMPCTRL_OUT_${.vars[AC_COMPCTRL_OUTPUT_TYPE]}
                                    ${.vars[AC_COMPCTRL_SINGLE_MODE]?then(' | AC_COMPCTRL_SINGLE_Msk','')}
                                    ${.vars[AC_COMPCTRL_HYSTEN]?then(' | AC_COMPCTRL_HYSTEN_Msk','')};</@compress>
    AC_REGS->AC_COMPCTRL[${i}] |= AC_COMPCTRL_ENABLE_Msk;
                <#if .vars[AC_SCALERn]?has_content >
    AC_REGS->AC_SCALER[${i}] = ${.vars[AC_SCALERn]};
                </#if>

            </#if>
        </#if>
    </#list>
<#if AC_WINCTRL_VAL?has_content>
    AC_REGS->AC_WINCTRL = ${AC_WINCTRL_VAL};
</#if>
<#if AC_EVCTRL_VAL?has_content>
    AC_REGS->AC_EVCTRL = ${AC_EVCTRL_VAL};
</#if>
<#if AC_INTENSET_VAL?has_content>
    AC_REGS->AC_INTENSET = ${AC_INTENSET_VAL};
</#if>
    AC_REGS->AC_CTRLA = AC_CTRLA_ENABLE_Msk;
}

void ${AC_INSTANCE_NAME}_Start( AC_CHANNEL channel_id )
{
    /* Start Comparison */
    AC_REGS->AC_CTRLB |= (1 << channel_id);
}

void ${AC_INSTANCE_NAME}_SwapInputs( AC_CHANNEL channel_id )
{
    /* Disable comparator before swapping */
    AC_REGS->AC_COMPCTRL[channel_id] &= ~AC_COMPCTRL_ENABLE_Msk;
    /* Swap inputs of the given comparator */
    AC_REGS->AC_COMPCTRL[channel_id] = AC_COMPCTRL_SWAP_Msk;
    AC_REGS->AC_COMPCTRL[channel_id] |= AC_COMPCTRL_ENABLE_Msk;
}

bool ${AC_INSTANCE_NAME}_StatusGet ( AC_STATUS status, AC_CHANNEL channel)
{
    bool breturnVal = false;

    if((AC_REGS->AC_STATUSB & (AC_STATUSB_READY0_Msk << channel)) == (AC_STATUSB_READY0_Msk << channel))
    {
        if((AC_REGS->AC_STATUSA & (AC_STATUSA_STATE0_Msk << channel)) == (AC_STATUSA_STATE0_Msk << channel))
        {
            breturnVal = true;
        }
        else
        {
            breturnVal = false;
        }
    }
    
    return breturnVal;
}

void ${AC_INSTANCE_NAME}_CallbackRegister (AC_CALLBACK callback, uintptr_t context)
{
    ${AC_INSTANCE_NAME?lower_case}Obj.callback = callback;
    ${AC_INSTANCE_NAME?lower_case}Obj.context = context;
}

void ${AC_INSTANCE_NAME}_InterruptHandler( void )
{
    /* Copy the status to use inside the callback */
    acObj.context = AC_REGS->AC_STATUSA;
    /* Clear the interrupt flags*/
    AC_REGS->AC_INTFLAG = AC_INTFLAG_Msk;

    /* Callback user function */
    if(${AC_INSTANCE_NAME?lower_case}Obj.callback != NULL)
    {
        ${AC_INSTANCE_NAME?lower_case}Obj.callback(${AC_INSTANCE_NAME?lower_case}Obj.context);
    }
}
