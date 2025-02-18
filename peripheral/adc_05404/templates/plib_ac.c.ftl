/*******************************************************************************
  Analog Comparator PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${AC_INSTANCE_NAME?lower_case}.c

  Summary:
    ${AC_INSTANCE_NAME} Source File

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
#include "device.h"
#include "plib_${AC_INSTANCE_NAME?lower_case}.h"
<#if core.CoreSysIntFile == true>
#include "interrupts.h"
</#if>
<#assign AC_WINCTRL_VAL = "">
<#assign AC_EVCTRL_VAL = "">
<#assign AC_INTENSET_VAL = "">
<#assign AC_CTRLA_VAL = "">
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
            <#assign AC_WINCTRL_VAL = AC_WINCTRL_VAL + " | AC_WINCTRL_WINTSEL0(${AC_WINTSEL0}U)">
        <#else>
            <#assign AC_WINCTRL_VAL = "AC_WINCTRL_WINTSEL0(${AC_WINTSEL0}U)">
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
        <#assign AC_INTENSET_VAL = "AC_INTENSET_WIN0_Msk">
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
<#if AC_LPMUX_ENABLE?has_content >
    <#if AC_LPMUX_ENABLE == true>
        <#if AC_CTRLA_VAL != "">
        <#assign AC_CTRLA_VAL = AC_CTRLA_VAL + " | AC_CTRLA_LPMUX_Msk">
        <#else>
        <#assign AC_CTRLA_VAL = "AC_CTRLA_LPMUX_Msk">
        </#if>
    </#if>
</#if>
<#if AC_RUNSTDBY?has_content >
    <#if AC_RUNSTDBY == true>
        <#if AC_CTRLA_VAL != "">
        <#assign AC_CTRLA_VAL = AC_CTRLA_VAL + " | AC_CTRLA_RUNSTDBY_Msk">
        <#else>
        <#assign AC_CTRLA_VAL = "AC_CTRLA_RUNSTDBY_Msk">
        </#if>
    </#if>
</#if>
volatile static AC_OBJECT ${AC_INSTANCE_NAME?lower_case}Obj;

// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************

void ${AC_INSTANCE_NAME}_Initialize(void)
{
    /*Reset AC registers*/
    ${AC_INSTANCE_NAME}_REGS->AC_CTRLA = AC_CTRLA_SWRST_Msk;
    while((${AC_INSTANCE_NAME}_REGS->AC_STATUSB & AC_STATUSB_SYNCBUSY_Msk) == AC_STATUSB_SYNCBUSY_Msk)
    {
        /* Wait for Synchronization */
    }

    <#list 0..4 as i>
    <#assign ANALOG_COMPARATOR_ENABLE = "ANALOG_COMPARATOR_ENABLE_" + i>
    <#assign AC_COMPCTRL_SINGLE_MODE = "AC_COMPCTRL_" + i +"SINGLE_MODE">
    <#assign AC_COMPCTRL_MUX_POS = "AC" + i + "_MUX_POS">
    <#assign AC_COMPCTRL_MUX_NEG = "AC" + i + "_MUX_NEG">
    <#assign AC_COMPCTRL_OUTPUT_TYPE = "AC" + i + "_OUTPUT_TYPE">
    <#assign AC_COMPCTRL_INTSEL = "AC" + i + "_ISEL">
    <#assign AC_COMPCTRL_HYSTEN = "AC" + i + "_HYSTEN">
    <#assign AC_COMPCTRL_SPEED = "AC" + i + "_SPEED">
    <#assign AC_COMPCTRL_FLEN = "AC" + i + "_FLEN_VAL">
    <#assign AC_SCALERn = "AC_SCALER_N_" + i>
        <#if .vars[ANALOG_COMPARATOR_ENABLE]?has_content>
            <#if (.vars[ANALOG_COMPARATOR_ENABLE] != false)>
    /**************** Comparator ${i} Configurations ************************/
    <@compress single_line=true>${AC_INSTANCE_NAME}_REGS->AC_COMPCTRL[${i}] = AC_COMPCTRL_MUXPOS_${.vars[AC_COMPCTRL_MUX_POS]}
                                  | AC_COMPCTRL_MUXNEG_${.vars[AC_COMPCTRL_MUX_NEG]}
                                  | AC_COMPCTRL_INTSEL_${.vars[AC_COMPCTRL_INTSEL]}
                                  | AC_COMPCTRL_OUT_${.vars[AC_COMPCTRL_OUTPUT_TYPE]}
                                  | AC_COMPCTRL_SPEED(${.vars[AC_COMPCTRL_SPEED]}U)
                                  | AC_COMPCTRL_FLEN_${.vars[AC_COMPCTRL_FLEN]}
                                  ${.vars[AC_COMPCTRL_SINGLE_MODE]?then(' | AC_COMPCTRL_SINGLE_Msk','')};</@compress>
    <#if (.vars[AC_COMPCTRL_HYSTEN]) && (!.vars[AC_COMPCTRL_SINGLE_MODE])>
    ${AC_INSTANCE_NAME}_REGS->AC_COMPCTRL[${i}] |= AC_COMPCTRL_HYST_Msk;
    </#if>
    ${AC_INSTANCE_NAME}_REGS->AC_COMPCTRL[${i}] |= AC_COMPCTRL_ENABLE_Msk;
                <#if .vars[AC_SCALERn]?has_content >
    ${AC_INSTANCE_NAME}_REGS->AC_SCALER[${i}] = ${.vars[AC_SCALERn]}U;
                </#if>

            </#if>
        </#if>
    </#list>
<#if AC_WINCTRL_VAL?has_content>

    ${AC_INSTANCE_NAME}_REGS->AC_WINCTRL = ${AC_WINCTRL_VAL};
    while((${AC_INSTANCE_NAME}_REGS->AC_STATUSB & AC_STATUSB_SYNCBUSY_Msk) == AC_STATUSB_SYNCBUSY_Msk)
    {
        /* Wait for Synchronization */
    }    
</#if>
<#if AC_EVCTRL_VAL?has_content>
    ${AC_INSTANCE_NAME}_REGS->AC_EVCTRL = ${AC_EVCTRL_VAL};
</#if>
<#if AC_INTENSET_VAL?has_content>
    ${AC_INSTANCE_NAME}_REGS->AC_INTENSET = ${AC_INTENSET_VAL};
</#if>
<#if AC_CTRLA_VAL?has_content>
    ${AC_INSTANCE_NAME}_REGS->AC_CTRLA = ${AC_CTRLA_VAL};
</#if>

    ${AC_INSTANCE_NAME}_REGS->AC_CTRLA |= AC_CTRLA_ENABLE_Msk;
    while((${AC_INSTANCE_NAME}_REGS->AC_STATUSB & AC_STATUSB_SYNCBUSY_Msk) == AC_STATUSB_SYNCBUSY_Msk)
    {
        /* Wait for Synchronization */
    }    
}

void ${AC_INSTANCE_NAME}_Start( AC_CHANNEL channel_id )
{
    /* Start Comparison */
    ${AC_INSTANCE_NAME}_REGS->AC_CTRLB |= (1U << (uint8_t)channel_id);
}

void ${AC_INSTANCE_NAME}_SetVddScalar( AC_CHANNEL channel_id , uint8_t vdd_scalar)
{
    ${AC_INSTANCE_NAME}_REGS->AC_SCALER[channel_id] = vdd_scalar;
}

void ${AC_INSTANCE_NAME}_SwapInputs( AC_CHANNEL channel_id )
{
    /* Disable comparator before swapping */
    ${AC_INSTANCE_NAME}_REGS->AC_COMPCTRL[channel_id] &= ~AC_COMPCTRL_ENABLE_Msk;
    /* Check Synchronization to ensure that the comparator is disabled */
    while((${AC_INSTANCE_NAME}_REGS->AC_STATUSB & AC_STATUSB_SYNCBUSY_Msk) == AC_STATUSB_SYNCBUSY_Msk)
    {
        /* Wait for Synchronization */
    }
    /* Swap inputs of the given comparator */
    ${AC_INSTANCE_NAME}_REGS->AC_COMPCTRL[channel_id] |= AC_COMPCTRL_SWAP_Msk;
    ${AC_INSTANCE_NAME}_REGS->AC_COMPCTRL[channel_id] |= AC_COMPCTRL_ENABLE_Msk;
    while((${AC_INSTANCE_NAME}_REGS->AC_STATUSB & AC_STATUSB_SYNCBUSY_Msk) == AC_STATUSB_SYNCBUSY_Msk)
    {
        /* Wait for Synchronization */
    }    
}

void ${AC_INSTANCE_NAME}_ChannelSelect( AC_CHANNEL channel_id , AC_POSINPUT positiveInput, AC_NEGINPUT negativeInput)
{
    /* Disable comparator before swapping */
    ${AC_INSTANCE_NAME}_REGS->AC_COMPCTRL[channel_id] &= ~AC_COMPCTRL_ENABLE_Msk;
    /* Check Synchronization to ensure that the comparator is disabled */
    while((${AC_INSTANCE_NAME}_REGS->AC_STATUSB & AC_STATUSB_SYNCBUSY_Msk) == AC_STATUSB_SYNCBUSY_Msk)
    {
        /* Wait for Synchronization */
    }
    ${AC_INSTANCE_NAME}_REGS->AC_COMPCTRL[channel_id] &= ~(AC_COMPCTRL_MUXPOS_Msk | AC_COMPCTRL_MUXNEG_Msk);
    ${AC_INSTANCE_NAME}_REGS->AC_COMPCTRL[channel_id] |= ((uint32_t)positiveInput | (uint32_t)negativeInput);

    /* Enable comparator channel */
    ${AC_INSTANCE_NAME}_REGS->AC_COMPCTRL[channel_id] |= AC_COMPCTRL_ENABLE_Msk;
    while((${AC_INSTANCE_NAME}_REGS->AC_STATUSB & AC_STATUSB_SYNCBUSY_Msk) == AC_STATUSB_SYNCBUSY_Msk)
    {
        /* Wait for Synchronization */
    }

}

bool ${AC_INSTANCE_NAME}_StatusGet (AC_CHANNEL channel)
{
    bool breturnVal = false;

    if((${AC_INSTANCE_NAME}_REGS->AC_STATUSB & (AC_STATUSB_READY0_Msk << (uint8_t)channel)) == (AC_STATUSB_READY0_Msk << (uint8_t)channel))
    {
        if((${AC_INSTANCE_NAME}_REGS->AC_STATUSA & (AC_STATUSA_STATE0_Msk << (uint8_t)channel)) == (AC_STATUSA_STATE0_Msk << (uint8_t)channel))
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
<#if AC_INTENSET_VAL != "">

void __attribute__((used)) ${AC_INSTANCE_NAME}_InterruptHandler( void )
{
    /* Additional local variable to prevent MISRA C violations (Rule 13.x) */
    uintptr_t context;
    uint8_t status;
    context = ${AC_INSTANCE_NAME?lower_case}Obj.context;      
    /* Copy the status to use inside the callback */
    ${AC_INSTANCE_NAME?lower_case}Obj.int_flags = ${AC_INSTANCE_NAME}_REGS->AC_STATUSA;
    status = ${AC_INSTANCE_NAME?lower_case}Obj.int_flags;
    /* Clear the interrupt flags*/
    ${AC_INSTANCE_NAME}_REGS->AC_INTFLAG = AC_INTFLAG_Msk;

    /* Callback user function */
    if(${AC_INSTANCE_NAME?lower_case}Obj.callback != NULL)
    {
        ${AC_INSTANCE_NAME?lower_case}Obj.callback(status, context);
    }
}
</#if>