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


#include "plib_${EIC_INSTANCE_NAME?lower_case}.h"

// *****************************************************************************
// *****************************************************************************
// Section: Global Data
// *****************************************************************************
// *****************************************************************************

<#if EIC_INT != "0">
/* EIC Channel Callback object */
EIC_CALLBACK_OBJ    ${EIC_INSTANCE_NAME?lower_case}CallbackObject[EXTINT_COUNT];
</#if>

<#if (NMI_IS_NON_SECURE == "NON-SECURE") && (NMI_CTRL == true)>
/* EIC NMI Callback object */
EIC_NMI_CALLBACK_OBJ ${EIC_INSTANCE_NAME?lower_case}NMICallbackObject;

</#if>
void ${EIC_INSTANCE_NAME}_Initialize (void)
{
    /* Callbacks for enabled interrupts */
    <#if EIC_INT != "0">
    <#list 0..EIC_INT_COUNT as i>
        <#assign EIC_INT_CHANNEL = "EIC_CHAN_" + i>
        <#assign EIC_NON_SEC_CHANNEL = "EIC_NONSEC_" + i>
            <#if .vars[EIC_INT_CHANNEL]?has_content>
                <#if (.vars[EIC_INT_CHANNEL] != false) && (.vars[EIC_NON_SEC_CHANNEL] == "NON-SECURE")>
                    <#lt>    ${EIC_INSTANCE_NAME?lower_case}CallbackObject[${i}].eicPinNo = EIC_PIN_${i};
                <#else>
                    <#lt>    ${EIC_INSTANCE_NAME?lower_case}CallbackObject[${i}].eicPinNo = EIC_PIN_MAX;
                </#if>
            </#if>
    </#list>
    </#if>
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
<#if (NMI_IS_NON_SECURE == "NON-SECURE") && (NMI_CTRL == true)>
void ${EIC_INSTANCE_NAME}_NMICallbackRegister(EIC_NMI_CALLBACK callback, uintptr_t context)
{
    ${EIC_INSTANCE_NAME?lower_case}NMICallbackObject.callback = callback;

    ${EIC_INSTANCE_NAME?lower_case}NMICallbackObject.context  = context;
}

</#if>
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
<#if .vars[Enable] && (.vars[EIC_NON_SEC] == "NON-SECURE")>
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
<#if EIC_OTHER_HANDLER_ACTIVE && EIC_OTHER_HANDLER_IS_NON_SEC>
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
<#if (NMI_IS_NON_SECURE == "NON-SECURE") && (NMI_CTRL == true)>
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
