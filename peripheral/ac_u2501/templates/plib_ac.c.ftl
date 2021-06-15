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
#include "device.h"
#include "plib_${AC_INSTANCE_NAME?lower_case}.h"
<#if core.CoreSysIntFile == true>
#include "interrupts.h"
</#if>
<#assign AC_WINCTRL_VAL = "">
<#assign AC_EVCTRL_VAL = "">
<#assign AC_INTENSET_VAL = "">
<#assign AC_SCALER_REG_PRESENT = false>
<#assign AC_INTERNAL_DAC_ENABLED = false>
<#assign AC_CTRLC_ENABLE = false>

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
            <#assign AC_WINCTRL_VAL = AC_WINCTRL_VAL + " | AC_WINCTRL_WINTSEL0(${AC_WINTSEL0})">
        <#else>
            <#assign AC_WINCTRL_VAL = "AC_WINCTRL_WINTSEL0(${AC_WINTSEL0})">
        </#if>
    </#if>
</#if>

<#list 0..(AC_NUM_COMPARATORS-1) as i>
    <#assign COMP_ENABLE = "ANALOG_COMPARATOR_ENABLE_"+i>
    <#if COMP_ENABLE ?has_content >
        <#if .vars[COMP_ENABLE] == true >
            <#assign AC_COMPEI = "AC_EVCTRL_COMPEI"+i>
            <#assign AC_COMPEO = "AC_EVCTRL_COMPEO"+i>
            <#if .vars[AC_COMPEI] == "1">
                <#if AC_EVCTRL_VAL != "">
                    <#assign AC_EVCTRL_VAL = AC_EVCTRL_VAL + "| AC_EVCTRL_COMPEI"+i+"_Msk">
                <#else>
                    <#assign AC_EVCTRL_VAL = " AC_EVCTRL_COMPEI"+i+"_Msk">
                </#if>
            <#elseif .vars[AC_COMPEI] == "2">
                <#if AC_EVCTRL_VAL != "">
                    <#assign AC_EVCTRL_VAL = AC_EVCTRL_VAL + "| AC_EVCTRL_COMPEI"+i+"_Msk | AC_EVCTRL_INVEI"+i+"_Msk">
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

<#list 0..(AC_NUM_COMPARATORS-1) as i>
    <#assign AC_SCALER_REG = "AC_SCALER_N_" + i>
    <#if .vars[AC_SCALER_REG]?has_content>
        <#assign AC_SCALER_REG_PRESENT = true>
    </#if>
</#list>

<#list 0..(AC_NUM_COMPARATORS-1) as i>
    <#assign ANALOG_COMPARATOR_ENABLE = "ANALOG_COMPARATOR_ENABLE_" + i>
    <#assign AC_COMPCTRL_MUXPOSx = "AC" + i + "_MUXPOS">
    <#assign AC_COMPCTRL_MUXNEGx = "AC" + i + "_MUXNEG">
    <#if .vars[ANALOG_COMPARATOR_ENABLE]?has_content>
    <#if (.vars[ANALOG_COMPARATOR_ENABLE] != false)>
    <#if .vars[AC_COMPCTRL_MUXPOSx] == "INTDAC" || .vars[AC_COMPCTRL_MUXNEGx] == "INTDAC">
        <#assign AC_INTERNAL_DAC_ENABLED = true>
    </#if>
    </#if>
    </#if>
</#list>

<#if (ANALOG_INPUT_CHARGE_PUMP_ENABLE?? && ANALOG_INPUT_CHARGE_PUMP_ENABLE == true) || AC_INTERNAL_DAC_ENABLED == true>
    <#assign AC_CTRLC_ENABLE = true>
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
    ${AC_INSTANCE_NAME}_REGS->AC_CTRLA = AC_CTRLA_SWRST_Msk;
    while((${AC_INSTANCE_NAME}_REGS->AC_SYNCBUSY & AC_SYNCBUSY_SWRST_Msk) == AC_SYNCBUSY_SWRST_Msk)
    {
        /* Wait for Synchronization */
    }

    <#if AC_LOAD_CALIB == 1>
    /*Load Calibration Value*/
    uint8_t calibVal = (uint8_t)((*(uint32_t*)0x00800080) & 0x3);
    calibVal = (((calibVal) == 0x3) ? 0x3 : (calibVal));


    ${AC_INSTANCE_NAME}_REGS->AC_CALIB = calibVal;
    </#if>

    <#if AC_CTRLC_ENABLE == true>
    ${AC_INSTANCE_NAME}_REGS->AC_CTRLC = AC_CTRLC_PRESCALER_${AC_CTRLC_PRESCALER}_Val | AC_CTRLC_PER(${AC_CTRLC_PERIOD}) | AC_CTRLC_WIDTH(${AC_CTRLC_WIDTH}) <#if (ANALOG_INPUT_CHARGE_PUMP_ENABLE?? && ANALOG_INPUT_CHARGE_PUMP_ENABLE == true)> | AC_CTRLC_AIPMPEN_Msk </#if>;
    </#if>

     /* Disable the module and configure COMPCTRL */
    <#list 0..4 as i>
    <#assign ANALOG_COMPARATOR_ENABLE = "ANALOG_COMPARATOR_ENABLE_" + i>
    <#assign AC_COMPCTRL_SINGLE_MODE = "AC_COMPCTRL_" + i +"SINGLE_MODE">
    <#assign AC_COMPCTRL_MUXPOS = "AC" + i + "_MUXPOS">
    <#assign AC_COMPCTRL_MUXNEG = "AC" + i + "_MUXNEG">
    <#assign AC_COMPCTRL_OUTPUT_TYPE = "AC" + i + "_OUTPUT_TYPE">
    <#assign AC_COMPCTRL_INTSEL = "AC" + i + "_ISEL">
    <#assign AC_COMPCTRL_HYSTEN = "AC" + i + "_HYSTEN">
    <#assign AC_COMPCTRL_HYST_VAL = "AC" + i + "_HYST_VAL">
    <#assign AC_COMPCTRL_RUNSTDBY = "AC" + i + "_COMPCTRL_RUNSTDBY">
    <#assign AC_COMPCTRL_SPEED = "AC" + i + "_SPEED">
    <#assign AC_COMPCTRL_FLEN = "AC" + i + "_FLEN_VAL">
    <#assign AC_COMPCTRL_SUT = "AC" + i + "_COMPCTRL_SUT">
    <#assign AC_SCALERn = "AC_SCALER_N_" + i>
    <#assign AC_DACCTRL_VALUE = "AC" + i + "_DACCTRL_VALUE">
    <#assign AC_DACCTRL_SHEN = "AC" + i + "_DACCTRL_SHEN">

        <#if .vars[ANALOG_COMPARATOR_ENABLE]?has_content>
            <#if (.vars[ANALOG_COMPARATOR_ENABLE] != false)>

    /**************** Comparator ${i} Configurations ************************/
    <@compress single_line=true>${AC_INSTANCE_NAME}_REGS->AC_COMPCTRL[${i}] = AC_COMPCTRL_MUXPOS_${.vars[AC_COMPCTRL_MUXPOS]}
                                  | AC_COMPCTRL_MUXNEG_${.vars[AC_COMPCTRL_MUXNEG]}
                                  | AC_COMPCTRL_INTSEL_${.vars[AC_COMPCTRL_INTSEL]}
                                  | AC_COMPCTRL_OUT_${.vars[AC_COMPCTRL_OUTPUT_TYPE]}
                                  | AC_COMPCTRL_SPEED(0x03)
                                  | AC_COMPCTRL_FLEN_${.vars[AC_COMPCTRL_FLEN]}
                                  ${.vars[AC_COMPCTRL_SINGLE_MODE]?then(' | AC_COMPCTRL_SINGLE_Msk','')}
                                  ${.vars[AC_COMPCTRL_RUNSTDBY]?then(' | AC_COMPCTRL_RUNSTDBY_Msk','')}
                                  <#if .vars[AC_COMPCTRL_SUT]?has_content> | AC_COMPCTRL_SUT(${.vars[AC_COMPCTRL_SUT]}) </#if>;</@compress>

    <#if .vars[AC_COMPCTRL_MUXPOS] == "INTDAC" || .vars[AC_COMPCTRL_MUXNEG] == "INTDAC">
    ${AC_INSTANCE_NAME}_REGS->AC_DACCTRL |=  AC_DACCTRL_VALUE${i}(${.vars[AC_DACCTRL_VALUE]}) <#if .vars[AC_DACCTRL_SHEN] == "0x1"> | AC_DACCTRL_SHEN${i}_Msk </#if>;
    </#if>

    <#if AC_COMPCTRL_SINGLE_MODE?has_content>
        <#if (.vars[AC_COMPCTRL_SINGLE_MODE] == false) & (.vars[AC_COMPCTRL_HYSTEN] == true)>
            <#if AC_COMPCTRL_HYST_VAL?has_content>
    ${AC_INSTANCE_NAME}_REGS->AC_COMPCTRL[${i}] |= AC_COMPCTRL_HYST(${.vars[AC_COMPCTRL_HYST_VAL]}) | AC_COMPCTRL_HYSTEN_Msk;
            <#else>
    ${AC_INSTANCE_NAME}_REGS->AC_COMPCTRL[${i}] |= AC_COMPCTRL_HYSTEN_Msk;
            </#if>
        </#if>
    </#if>
    ${AC_INSTANCE_NAME}_REGS->AC_COMPCTRL[${i}] |= AC_COMPCTRL_ENABLE_Msk;	
                <#if .vars[AC_SCALERn]?has_content >
    ${AC_INSTANCE_NAME}_REGS->AC_SCALER[${i}] = ${.vars[AC_SCALERn]};
                </#if>

            </#if>
        </#if>
    </#list>
<#if AC_WINCTRL_VAL?has_content>
    while((${AC_INSTANCE_NAME}_REGS->AC_SYNCBUSY & AC_SYNCBUSY_WINCTRL_Msk) == AC_SYNCBUSY_WINCTRL_Msk)
    {
        /* Wait for Synchronization */
    }
    ${AC_INSTANCE_NAME}_REGS->AC_WINCTRL = ${AC_WINCTRL_VAL};
</#if>
<#if AC_EVCTRL_VAL?has_content>
    ${AC_INSTANCE_NAME}_REGS->AC_EVCTRL = ${AC_EVCTRL_VAL};
</#if>
<#if AC_INTENSET_VAL?has_content>
    ${AC_INSTANCE_NAME}_REGS->AC_INTENSET = ${AC_INTENSET_VAL};
</#if>    
    ${AC_INSTANCE_NAME}_REGS->AC_CTRLA = AC_CTRLA_ENABLE_Msk;
	while((${AC_INSTANCE_NAME}_REGS->AC_SYNCBUSY & AC_SYNCBUSY_ENABLE_Msk) == AC_SYNCBUSY_ENABLE_Msk)
    {
        /* Wait for Synchronization */
    }
}

void ${AC_INSTANCE_NAME}_Start( AC_CHANNEL channel_id )
{
    /* Start Comparison */
    ${AC_INSTANCE_NAME}_REGS->AC_CTRLB |= (1 << channel_id);
}

<#if AC_SCALER_REG_PRESENT == true>
void ${AC_INSTANCE_NAME}_SetVddScalar( AC_CHANNEL channel_id , uint8_t vdd_scalar)
{
    ${AC_INSTANCE_NAME}_REGS->AC_SCALER[channel_id] = vdd_scalar;
}
</#if>

<#if AC_IS_DAC_PRESENT == true>
void ${AC_INSTANCE_NAME}_SetDACOutput( AC_CHANNEL channel_id , uint8_t value)
{
    ${AC_INSTANCE_NAME}_REGS->AC_CTRLA &= ~AC_CTRLA_ENABLE_Msk;
	while((${AC_INSTANCE_NAME}_REGS->AC_SYNCBUSY & AC_SYNCBUSY_ENABLE_Msk) == AC_SYNCBUSY_ENABLE_Msk)
    {
        /* Wait for Synchronization */
    }

    ${AC_INSTANCE_NAME}_REGS->AC_COMPCTRL[channel_id] &= ~AC_COMPCTRL_ENABLE_Msk;

    while((${AC_INSTANCE_NAME}_REGS->AC_SYNCBUSY & AC_SYNCBUSY_ENABLE_Msk) == AC_SYNCBUSY_ENABLE_Msk)
    {
        /* Wait for Synchronization */
    }

    if (channel_id == AC_CHANNEL0)
    {
        ${AC_INSTANCE_NAME}_REGS->AC_DACCTRL = (${AC_INSTANCE_NAME}_REGS->AC_DACCTRL & ~AC_DACCTRL_VALUE0_Msk) | (value);
    }
    else
    {
        ${AC_INSTANCE_NAME}_REGS->AC_DACCTRL = (${AC_INSTANCE_NAME}_REGS->AC_DACCTRL & ~AC_DACCTRL_VALUE1_Msk) | (value << AC_DACCTRL_VALUE1_Pos);
    }

    ${AC_INSTANCE_NAME}_REGS->AC_COMPCTRL[channel_id] |= AC_COMPCTRL_ENABLE_Msk;

    while((${AC_INSTANCE_NAME}_REGS->AC_SYNCBUSY & AC_SYNCBUSY_ENABLE_Msk) == AC_SYNCBUSY_ENABLE_Msk)
    {
        /* Wait for Synchronization */
    }

    ${AC_INSTANCE_NAME}_REGS->AC_CTRLA |= AC_CTRLA_ENABLE_Msk;
	while((${AC_INSTANCE_NAME}_REGS->AC_SYNCBUSY & AC_SYNCBUSY_ENABLE_Msk) == AC_SYNCBUSY_ENABLE_Msk)
    {
        /* Wait for Synchronization */
    }
}
</#if>


void ${AC_INSTANCE_NAME}_SwapInputs( AC_CHANNEL channel_id )
{
    /* Check Synchronization */
    while((${AC_INSTANCE_NAME}_REGS->AC_SYNCBUSY & AC_SYNCBUSY_Msk) == AC_SYNCBUSY_Msk)
    {
        /* Wait for Synchronization */
    }
    /* Disable comparator before swapping */
    ${AC_INSTANCE_NAME}_REGS->AC_COMPCTRL[channel_id] &= ~AC_COMPCTRL_ENABLE_Msk;
    /* Check Synchronization to ensure that the comparator is disabled */
    while((${AC_INSTANCE_NAME}_REGS->AC_SYNCBUSY & AC_SYNCBUSY_Msk) == AC_SYNCBUSY_Msk)
    {
        /* Wait for Synchronization */
    }
    /* Swap inputs of the given comparator */
    ${AC_INSTANCE_NAME}_REGS->AC_COMPCTRL[channel_id] = AC_COMPCTRL_SWAP_Msk;
    ${AC_INSTANCE_NAME}_REGS->AC_COMPCTRL[channel_id] |= AC_COMPCTRL_ENABLE_Msk;
}

void ${AC_INSTANCE_NAME}_ChannelSelect( AC_CHANNEL channel_id , AC_POSINPUT positiveInput, AC_NEGINPUT negativeInput)
{
    /* Disable comparator before swapping */
    ${AC_INSTANCE_NAME}_REGS->AC_COMPCTRL[channel_id] &= ~AC_COMPCTRL_ENABLE_Msk;
    /* Check Synchronization to ensure that the comparator is disabled */
    while((${AC_INSTANCE_NAME}_REGS->AC_SYNCBUSY & AC_SYNCBUSY_Msk) == AC_SYNCBUSY_Msk)
    {
        /* Wait for Synchronization */
    }
    ${AC_INSTANCE_NAME}_REGS->AC_COMPCTRL[channel_id] &= ~(AC_COMPCTRL_MUXPOS_Msk | AC_COMPCTRL_MUXNEG_Msk);
    ${AC_INSTANCE_NAME}_REGS->AC_COMPCTRL[channel_id] |= (positiveInput | negativeInput);

    /* Enable comparator channel */
    ${AC_INSTANCE_NAME}_REGS->AC_COMPCTRL[channel_id] |= AC_COMPCTRL_ENABLE_Msk;
    while((${AC_INSTANCE_NAME}_REGS->AC_SYNCBUSY & AC_SYNCBUSY_Msk) == AC_SYNCBUSY_Msk)
    {
        /* Wait for Synchronization */
    }

}

bool ${AC_INSTANCE_NAME}_StatusGet (AC_CHANNEL channel)
{
    bool breturnVal = false;

    if((${AC_INSTANCE_NAME}_REGS->AC_STATUSB & (AC_STATUSB_READY0_Msk << channel)) == (AC_STATUSB_READY0_Msk << channel))
    {
        if((${AC_INSTANCE_NAME}_REGS->AC_STATUSA & (AC_STATUSA_STATE0_Msk << channel)) == (AC_STATUSA_STATE0_Msk << channel))
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
    acObj.int_flags = ${AC_INSTANCE_NAME}_REGS->AC_STATUSA;
    /* Clear the interrupt flags*/
    ${AC_INSTANCE_NAME}_REGS->AC_INTFLAG = AC_INTFLAG_Msk;

    /* Callback user function */
    if(${AC_INSTANCE_NAME?lower_case}Obj.callback != NULL)
    {
        ${AC_INSTANCE_NAME?lower_case}Obj.callback(${AC_INSTANCE_NAME?lower_case}Obj.int_flags, ${AC_INSTANCE_NAME?lower_case}Obj.context);
    }
}
