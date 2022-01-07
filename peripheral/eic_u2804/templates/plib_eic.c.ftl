/*******************************************************************************
  External Interrupt Controller (EIC) PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_${EIC_INSTANCE_NAME?lower_case}.c

  Summary
    Source for EIC peripheral library interface Implementation.

  Description
    This file defines the interface to the EIC peripheral library. This
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
<#assign EIC_REG_NAME = EIC_INSTANCE_NAME>
<#if __TRUSTZONE_ENABLED?? && __TRUSTZONE_ENABLED == "true">
    <#assign EIC_REG_NAME = EIC_INSTANCE_NAME + "_SEC">
</#if>

#include "plib_${EIC_INSTANCE_NAME?lower_case}.h"
<#if core.CoreSysIntFile == true>
#include "interrupts.h"
</#if>

// *****************************************************************************
// *****************************************************************************
// Section: Global Data
// *****************************************************************************
// *****************************************************************************

<#if EIC_INT != "0">
/* EIC Channel Callback object */
EIC_CALLBACK_OBJ    ${EIC_INSTANCE_NAME?lower_case}CallbackObject[EXTINT_COUNT];
</#if>

<#if __TRUSTZONE_ENABLED?? && __TRUSTZONE_ENABLED == "true">
<#if (NMI_IS_NON_SECURE == "SECURE") && (NMI_CTRL == true)>
/* EIC NMI Callback object */
EIC_NMI_CALLBACK_OBJ ${EIC_INSTANCE_NAME?lower_case}NMICallbackObject;

</#if>
<#else>
<#if NMI_CTRL == true>
/* EIC NMI Callback object */
EIC_NMI_CALLBACK_OBJ ${EIC_INSTANCE_NAME?lower_case}NMICallbackObject;

</#if>
</#if>

void ${EIC_INSTANCE_NAME}_Initialize (void)
{
    /* Reset all registers in the EIC module to their initial state and
       EIC will be disabled. */
    ${EIC_REG_NAME}_REGS->EIC_CTRLA |= EIC_CTRLA_SWRST_Msk;

    while((${EIC_REG_NAME}_REGS->EIC_SYNCBUSY & EIC_SYNCBUSY_SWRST_Msk) == EIC_SYNCBUSY_SWRST_Msk)
    {
        /* Wait for sync */
    }

    <#if EIC_CLKSEL == "1">
    /* EIC is clocked by ultra low power clock */
    ${EIC_REG_NAME}_REGS->EIC_CTRLA |= EIC_CTRLA_CKSEL_Msk;
    <#else>
    /* EIC is by default clocked by GCLK */
    </#if>

    /* NMI Control register */
    <#if NMI_CTRL == true>
    <@compress single_line=true>${EIC_REG_NAME}_REGS->EIC_NMICTRL =  EIC_NMICTRL_NMIASYNCH(${NMI_ASYNCH})
                                                        | EIC_NMICTRL_NMISENSE_${NMI_SENSE}
                                                        ${NMI_FILTEN?then('| EIC_NMICTRL_NMIFILTEN_Msk', '')};</@compress>
    </#if>

    /* Interrupt sense type and filter control for EXTINT channels 0 to (${EIC_INT_COUNT}-1) */
    <#if EIC_INT_COUNT < 9>
    ${EIC_REG_NAME}_REGS->EIC_CONFIG =  EIC_CONFIG_SENSE0_${EIC_CONFIG_SENSE_0} ${EIC_CONFIG_FILTEN_0?then('| EIC_CONFIG_FILTEN0_Msk', '')}
        <#if EIC_CONFIG_SENSE_1??>| EIC_CONFIG_SENSE1_${EIC_CONFIG_SENSE_1} ${EIC_CONFIG_FILTEN_1?then('| EIC_CONFIG_FILTEN1_Msk', '')}</#if>
        <#if EIC_CONFIG_SENSE_2??>| EIC_CONFIG_SENSE2_${EIC_CONFIG_SENSE_2} ${EIC_CONFIG_FILTEN_2?then('| EIC_CONFIG_FILTEN2_Msk', '')}</#if>
        <#if EIC_CONFIG_SENSE_3??>| EIC_CONFIG_SENSE3_${EIC_CONFIG_SENSE_3} ${EIC_CONFIG_FILTEN_3?then('| EIC_CONFIG_FILTEN3_Msk', '')}</#if>
        <#if EIC_CONFIG_SENSE_4??>| EIC_CONFIG_SENSE4_${EIC_CONFIG_SENSE_4} ${EIC_CONFIG_FILTEN_4?then('| EIC_CONFIG_FILTEN4_Msk', '')}</#if>
        <#if EIC_CONFIG_SENSE_5??>| EIC_CONFIG_SENSE5_${EIC_CONFIG_SENSE_5} ${EIC_CONFIG_FILTEN_5?then('| EIC_CONFIG_FILTEN5_Msk', '')}</#if>
        <#if EIC_CONFIG_SENSE_6??>| EIC_CONFIG_SENSE6_${EIC_CONFIG_SENSE_6} ${EIC_CONFIG_FILTEN_6?then('| EIC_CONFIG_FILTEN6_Msk', '')}</#if>
        <#if EIC_CONFIG_SENSE_7??>| EIC_CONFIG_SENSE7_${EIC_CONFIG_SENSE_7} ${EIC_CONFIG_FILTEN_7?then('| EIC_CONFIG_FILTEN7_Msk', '')}</#if>;
    <#else>
    ${EIC_REG_NAME}_REGS->EIC_CONFIG0 =  EIC_CONFIG0_SENSE0_${EIC_CONFIG_SENSE_0} ${EIC_CONFIG_FILTEN_0?then('| EIC_CONFIG0_FILTEN0_Msk', '')}
        | EIC_CONFIG0_SENSE1_${EIC_CONFIG_SENSE_1} ${EIC_CONFIG_FILTEN_1?then('| EIC_CONFIG0_FILTEN1_Msk', '')}
        | EIC_CONFIG0_SENSE2_${EIC_CONFIG_SENSE_2} ${EIC_CONFIG_FILTEN_2?then('| EIC_CONFIG0_FILTEN2_Msk', '')}
        | EIC_CONFIG0_SENSE3_${EIC_CONFIG_SENSE_3} ${EIC_CONFIG_FILTEN_3?then('| EIC_CONFIG0_FILTEN3_Msk', '')}
        | EIC_CONFIG0_SENSE4_${EIC_CONFIG_SENSE_4} ${EIC_CONFIG_FILTEN_4?then('| EIC_CONFIG0_FILTEN4_Msk', '')}
        | EIC_CONFIG0_SENSE5_${EIC_CONFIG_SENSE_5} ${EIC_CONFIG_FILTEN_5?then('| EIC_CONFIG0_FILTEN5_Msk', '')}
        | EIC_CONFIG0_SENSE6_${EIC_CONFIG_SENSE_6} ${EIC_CONFIG_FILTEN_6?then('| EIC_CONFIG0_FILTEN6_Msk', '')}
        | EIC_CONFIG0_SENSE7_${EIC_CONFIG_SENSE_7} ${EIC_CONFIG_FILTEN_7?then('| EIC_CONFIG0_FILTEN7_Msk', '')};

    ${EIC_REG_NAME}_REGS->EIC_CONFIG1 =  EIC_CONFIG1_SENSE8_${EIC_CONFIG_SENSE_8} ${EIC_CONFIG_FILTEN_8?then('| EIC_CONFIG1_FILTEN8_Msk', '')}
        <#if EIC_CONFIG_SENSE_9??>| EIC_CONFIG1_SENSE9_${EIC_CONFIG_SENSE_9} ${EIC_CONFIG_FILTEN_9?then('| EIC_CONFIG1_FILTEN9_Msk', '')}</#if>
        <#if EIC_CONFIG_SENSE_10??>| EIC_CONFIG1_SENSE10_${EIC_CONFIG_SENSE_10} ${EIC_CONFIG_FILTEN_10?then('| EIC_CONFIG1_FILTEN10_Msk', '')}</#if>
        <#if EIC_CONFIG_SENSE_11??>| EIC_CONFIG1_SENSE11_${EIC_CONFIG_SENSE_11} ${EIC_CONFIG_FILTEN_11?then('| EIC_CONFIG1_FILTEN11_Msk', '')}</#if>
        <#if EIC_CONFIG_SENSE_12??>| EIC_CONFIG1_SENSE12_${EIC_CONFIG_SENSE_12} ${EIC_CONFIG_FILTEN_12?then('| EIC_CONFIG1_FILTEN12_Msk', '')}</#if>
        <#if EIC_CONFIG_SENSE_13??>| EIC_CONFIG1_SENSE13_${EIC_CONFIG_SENSE_13} ${EIC_CONFIG_FILTEN_13?then('| EIC_CONFIG1_FILTEN13_Msk', '')}</#if>
        <#if EIC_CONFIG_SENSE_14??>| EIC_CONFIG1_SENSE14_${EIC_CONFIG_SENSE_14} ${EIC_CONFIG_FILTEN_14?then('| EIC_CONFIG1_FILTEN14_Msk', '')}</#if>
        <#if EIC_CONFIG_SENSE_15??>| EIC_CONFIG1_SENSE15_${EIC_CONFIG_SENSE_15} ${EIC_CONFIG_FILTEN_15?then('| EIC_CONFIG1_FILTEN15_Msk', '')}</#if>;
    </#if>

    <#if EIC_ASYNCH != "0">
    /* External Interrupt Asynchronous Mode enable */
    ${EIC_REG_NAME}_REGS->EIC_ASYNCH = 0x${EIC_ASYNCH};
    </#if>

    <#if EIC_DEBOUNCEN?? && EIC_DEBOUNCEN != "0">
    /* Debouncer enable */
    ${EIC_REG_NAME}_REGS->EIC_DEBOUNCEN = 0x${EIC_DEBOUNCEN};
    </#if>

    <#if EIC_EXTINTEO != "0">
    /* Event Control Output enable */
    ${EIC_REG_NAME}_REGS->EIC_EVCTRL = 0x${EIC_EXTINTEO};
    </#if>

    <#if EIC_DEBOUNCEN?? && EIC_DEBOUNCEN != "0">
    /* Debouncer Setting */
    <@compress single_line=true>${EIC_REG_NAME}_REGS->EIC_DPRESCALER = EIC_DPRESCALER_PRESCALER0(${EIC_DEBOUNCER_PRESCALER_0})
                                                        <#if EIC_DEBOUNCER_PRESCALER_1??>
                                                        | EIC_DPRESCALER_PRESCALER1(${EIC_DEBOUNCER_PRESCALER_1})
                                                        </#if>
                                                        ${(EIC_PRESCALER_TICKON == "1")?then('| EIC_DPRESCALER_TICKON_Msk' , '')}
                                                        ${(EIC_DEBOUNCER_NO_STATES_0 == "1")?then('| EIC_DPRESCALER_STATES0_Msk' , '')}
                                                        <#if EIC_DEBOUNCER_NO_STATES_1??>
                                                        ${(EIC_DEBOUNCER_NO_STATES_1 == "1")?then('| EIC_DPRESCALER_STATES1_Msk' , '')}
                                                        </#if>;</@compress>
    </#if>

    <#if EIC_INT != "0">
    /* External Interrupt enable*/
    ${EIC_REG_NAME}_REGS->EIC_INTENSET = 0x${EIC_INT};
<#if __TRUSTZONE_ENABLED?? && __TRUSTZONE_ENABLED == "true">
    /* Callbacks for enabled interrupts */
    <#list 0..EIC_INT_COUNT as i>
        <#assign EIC_INT_CHANNEL = "EIC_CHAN_" + i>
        <#assign EIC_NON_SEC_CHANNEL = "EIC_NONSEC_" + i>
            <#if .vars[EIC_INT_CHANNEL]?has_content>
                <#if (.vars[EIC_INT_CHANNEL] != false) && .vars[EIC_NON_SEC_CHANNEL] == "SECURE">
                    <#lt>    ${EIC_INSTANCE_NAME?lower_case}CallbackObject[${i}].eicPinNo = EIC_PIN_${i};
                <#else>
                    <#lt>    ${EIC_INSTANCE_NAME?lower_case}CallbackObject[${i}].eicPinNo = EIC_PIN_MAX;
                </#if>
            </#if>
    </#list>
<#else>
    /* Callbacks for enabled interrupts */
    <#list 0..EIC_INT_COUNT as i>
        <#assign EIC_INT_CHANNEL = "EIC_CHAN_" + i>
            <#if .vars[EIC_INT_CHANNEL]?has_content>
                <#if (.vars[EIC_INT_CHANNEL] != false)>
                    <#lt>    ${EIC_INSTANCE_NAME?lower_case}CallbackObject[${i}].eicPinNo = EIC_PIN_${i};
                <#else>
                    <#lt>    ${EIC_INSTANCE_NAME?lower_case}CallbackObject[${i}].eicPinNo = EIC_PIN_MAX;
                </#if>
            </#if>
    </#list>
    </#if>
</#if>

<#if __TRUSTZONE_ENABLED?? && __TRUSTZONE_ENABLED == "true" && (NMI_IS_NON_SECURE == "NON-SECURE" || EIC_NONSEC != "0")>
    ${EIC_REG_NAME}_REGS->EIC_NONSEC = 0x${EIC_NONSEC} <#if NMI_IS_NON_SECURE == "NON-SECURE">| EIC_NONSEC_NMI_Msk</#if>;
</#if>
    /* Enable the EIC */
    ${EIC_REG_NAME}_REGS->EIC_CTRLA |= EIC_CTRLA_ENABLE_Msk;

    while((${EIC_REG_NAME}_REGS->EIC_SYNCBUSY & EIC_SYNCBUSY_ENABLE_Msk) == EIC_SYNCBUSY_ENABLE_Msk)
    {
        /* Wait for sync */
    }
}
<#if EIC_INT != "0">

void ${EIC_INSTANCE_NAME}_InterruptEnable (EIC_PIN pin)
{
    ${EIC_REG_NAME}_REGS->EIC_INTENSET = (1UL << pin);
}

void ${EIC_INSTANCE_NAME}_InterruptDisable (EIC_PIN pin)
{
    ${EIC_REG_NAME}_REGS->EIC_INTENCLR = (1UL << pin);
}

void ${EIC_INSTANCE_NAME}_CallbackRegister(EIC_PIN pin, EIC_CALLBACK callback, uintptr_t context)
{
    if (${EIC_INSTANCE_NAME?lower_case}CallbackObject[pin].eicPinNo == pin)
    {
        ${EIC_INSTANCE_NAME?lower_case}CallbackObject[pin].callback = callback;

        ${EIC_INSTANCE_NAME?lower_case}CallbackObject[pin].context  = context;
    }
}

</#if>
<#if __TRUSTZONE_ENABLED?? && __TRUSTZONE_ENABLED == "true" && NMI_IS_NON_SECURE == "NON-SECURE">
<#else>
<#if NMI_CTRL == true>
void ${EIC_INSTANCE_NAME}_NMICallbackRegister(EIC_NMI_CALLBACK callback, uintptr_t context)
{
    ${EIC_INSTANCE_NAME?lower_case}NMICallbackObject.callback = callback;

    ${EIC_INSTANCE_NAME?lower_case}NMICallbackObject.context  = context;
}
</#if>

</#if>
<#if __TRUSTZONE_ENABLED?? && __TRUSTZONE_ENABLED == "true">
    <#if EIC_INT != "0">
    <#if NUM_INT_LINES == 0>
void ${EIC_INSTANCE_NAME}_InterruptHandler(void)
{
    uint8_t currentChannel = 0;
    uint32_t eicIntFlagStatus = 0;

    /* Find any triggered channels, run associated callback handlers */
    for (currentChannel = 0; currentChannel < EXTINT_COUNT; currentChannel++)
    {
        /* Verify if the EXTINT x Interrupt Pin is enabled */
        if ((${EIC_INSTANCE_NAME?lower_case}CallbackObject[currentChannel].eicPinNo == currentChannel))
        {
            /* Read the interrupt flag status */
            eicIntFlagStatus = ${EIC_REG_NAME}_REGS->EIC_INTFLAG & (1UL << currentChannel);

            if (eicIntFlagStatus)
            {
                /* Find any associated callback entries in the callback table */
                if ((${EIC_INSTANCE_NAME?lower_case}CallbackObject[currentChannel].callback != NULL))
                {
                    ${EIC_INSTANCE_NAME?lower_case}CallbackObject[currentChannel].callback(${EIC_INSTANCE_NAME?lower_case}CallbackObject[currentChannel].context);
                }

                /* Clear interrupt flag */
                ${EIC_REG_NAME}_REGS->EIC_INTFLAG = (1UL << currentChannel);
            }
        }
    }
}
    <#else>
    <#list 0..(NUM_INT_LINES-1) as x>
    <#assign Enable = "EIC_INT_" + x>
    <#assign EIC_NON_SEC = "EIC_NONSEC_" + x>
    <#if .vars[Enable] && (.vars[EIC_NON_SEC] == "SECURE")>
void ${EIC_INSTANCE_NAME}_EXTINT_${x}_InterruptHandler(void)
{
    /* Clear interrupt flag */
    ${EIC_REG_NAME}_REGS->EIC_INTFLAG = (1UL << ${x});
    /* Find any associated callback entries in the callback table */
    if ((${EIC_INSTANCE_NAME?lower_case}CallbackObject[${x}].callback != NULL))
    {
        ${EIC_INSTANCE_NAME?lower_case}CallbackObject[${x}].callback(${EIC_INSTANCE_NAME?lower_case}CallbackObject[${x}].context);
    }

}
    </#if>
    </#list>
    <#if EIC_OTHER_HANDLER_ACTIVE??>
    <#if EIC_OTHER_HANDLER_ACTIVE &&  (EIC_OTHER_HANDLER_IS_NON_SEC == false)>
void ${EIC_INSTANCE_NAME}_OTHER_InterruptHandler(void)
{
    uint8_t currentChannel = 0;
    uint32_t eicIntFlagStatus = 0;

    /* Find any triggered channels, run associated callback handlers */
    for (currentChannel = ${NUM_INT_LINES}; currentChannel < EXTINT_COUNT; currentChannel++)
    {
        /* Verify if the EXTINT x Interrupt Pin is enabled */
        if ((${EIC_INSTANCE_NAME?lower_case}CallbackObject[currentChannel].eicPinNo == currentChannel))
        {
            /* Read the interrupt flag status */
            eicIntFlagStatus = ${EIC_REG_NAME}_REGS->EIC_INTFLAG & (1UL << currentChannel);

            if (eicIntFlagStatus)
            {
                /* Find any associated callback entries in the callback table */
                if ((${EIC_INSTANCE_NAME?lower_case}CallbackObject[currentChannel].callback != NULL))
                {
                    ${EIC_INSTANCE_NAME?lower_case}CallbackObject[currentChannel].callback(${EIC_INSTANCE_NAME?lower_case}CallbackObject[currentChannel].context);
                }

                /* Clear interrupt flag */
                ${EIC_REG_NAME}_REGS->EIC_INTFLAG = (1UL << currentChannel);
            }
        }
    }
}
    </#if>
    </#if>
    </#if>

</#if>
<#else>
    <#if EIC_INT != "0">
    <#if NUM_INT_LINES == 0>
void ${EIC_INSTANCE_NAME}_InterruptHandler(void)
{
    uint8_t currentChannel = 0;
    uint32_t eicIntFlagStatus = 0;

    /* Find any triggered channels, run associated callback handlers */
    for (currentChannel = 0; currentChannel < EXTINT_COUNT; currentChannel++)
    {
        /* Verify if the EXTINT x Interrupt Pin is enabled */
        if ((${EIC_INSTANCE_NAME?lower_case}CallbackObject[currentChannel].eicPinNo == currentChannel))
        {
            /* Read the interrupt flag status */
            eicIntFlagStatus = ${EIC_REG_NAME}_REGS->EIC_INTFLAG & (1UL << currentChannel);

            if (eicIntFlagStatus)
            {
                /* Find any associated callback entries in the callback table */
                if ((${EIC_INSTANCE_NAME?lower_case}CallbackObject[currentChannel].callback != NULL))
                {
                    ${EIC_INSTANCE_NAME?lower_case}CallbackObject[currentChannel].callback(${EIC_INSTANCE_NAME?lower_case}CallbackObject[currentChannel].context);
                }

                /* Clear interrupt flag */
                ${EIC_REG_NAME}_REGS->EIC_INTFLAG = (1UL << currentChannel);
            }
        }
    }
}
    <#else>
    <#list 0..(NUM_INT_LINES-1) as x>
    <#assign Enable = "EIC_INT_" + x>
    <#if .vars[Enable]>
void ${EIC_INSTANCE_NAME}_EXTINT_${x}_InterruptHandler(void)
{
    /* Clear interrupt flag */
    ${EIC_REG_NAME}_REGS->EIC_INTFLAG = (1UL << ${x});
    /* Find any associated callback entries in the callback table */
    if ((${EIC_INSTANCE_NAME?lower_case}CallbackObject[${x}].callback != NULL))
    {
        ${EIC_INSTANCE_NAME?lower_case}CallbackObject[${x}].callback(${EIC_INSTANCE_NAME?lower_case}CallbackObject[${x}].context);
    }

}
    </#if>
    </#list>
    <#if EIC_OTHER_HANDLER_ACTIVE??>
    <#if EIC_OTHER_HANDLER_ACTIVE>
void ${EIC_INSTANCE_NAME}_OTHER_InterruptHandler(void)
{
    uint8_t currentChannel = 0;
    uint32_t eicIntFlagStatus = 0;

    /* Find any triggered channels, run associated callback handlers */
    for (currentChannel = ${NUM_INT_LINES}; currentChannel < EXTINT_COUNT; currentChannel++)
    {
        /* Verify if the EXTINT x Interrupt Pin is enabled */
        if ((${EIC_INSTANCE_NAME?lower_case}CallbackObject[currentChannel].eicPinNo == currentChannel))
        {
            /* Read the interrupt flag status */
            eicIntFlagStatus = ${EIC_REG_NAME}_REGS->EIC_INTFLAG & (1UL << currentChannel);

            if (eicIntFlagStatus)
            {
                /* Find any associated callback entries in the callback table */
                if ((${EIC_INSTANCE_NAME?lower_case}CallbackObject[currentChannel].callback != NULL))
                {
                    ${EIC_INSTANCE_NAME?lower_case}CallbackObject[currentChannel].callback(${EIC_INSTANCE_NAME?lower_case}CallbackObject[currentChannel].context);
                }

                /* Clear interrupt flag */
                ${EIC_REG_NAME}_REGS->EIC_INTFLAG = (1UL << currentChannel);
            }
        }
    }
}
    </#if>
    </#if>
    </#if>

</#if>
</#if>
<#if __TRUSTZONE_ENABLED?? && __TRUSTZONE_ENABLED == "true">
<#if (NMI_IS_NON_SECURE == "SECURE") && (NMI_CTRL == true)>
void NMI_InterruptHandler(void)
{
    /* Find the triggered, run associated callback handlers */
    if ((${EIC_REG_NAME}_REGS->EIC_NMIFLAG & EIC_NMIFLAG_NMI_Msk) == EIC_NMIFLAG_NMI_Msk)
    {
        /* Clear flag */
        ${EIC_REG_NAME}_REGS->EIC_NMIFLAG = EIC_NMIFLAG_NMI_Msk;

        /* Find any associated callback entries in the callback table */
        if (${EIC_INSTANCE_NAME?lower_case}NMICallbackObject.callback != NULL)
        {
            ${EIC_INSTANCE_NAME?lower_case}NMICallbackObject.callback(${EIC_INSTANCE_NAME?lower_case}NMICallbackObject.context);
        }
    }
}
</#if>
<#else>
<#if NMI_CTRL == true>
void NMI_InterruptHandler(void)
{
    /* Find the triggered, run associated callback handlers */
    if ((${EIC_REG_NAME}_REGS->EIC_NMIFLAG & EIC_NMIFLAG_NMI_Msk) == EIC_NMIFLAG_NMI_Msk)
    {
        /* Clear flag */
        ${EIC_REG_NAME}_REGS->EIC_NMIFLAG = EIC_NMIFLAG_NMI_Msk;

        /* Find any associated callback entries in the callback table */
        if (${EIC_INSTANCE_NAME?lower_case}NMICallbackObject.callback != NULL)
        {
            ${EIC_INSTANCE_NAME?lower_case}NMICallbackObject.callback(${EIC_INSTANCE_NAME?lower_case}NMICallbackObject.context);
        }
    }
}
</#if>
</#if>