/*******************************************************************************
  Analog Comparator Controller (ACC) PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_${ACC_INSTANCE_NAME?lower_case}.c

  Summary
    Source for ACC peripheral library interface Implementation.

  Description
    This file defines the interface to the ACC peripheral library. This
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
<#compress>
<#assign MODE_REG_VAL = "ACC_MR_SELPLUS_" + ACC_INPUT_SELPLUS + "|ACC_MR_SELMINUS_" + ACC_INPUT_SELMINUS +"|">
<#if ACC_OUTPUT_INVERT>
<#assign MODE_REG_VAL = MODE_REG_VAL + "ACC_MR_INV_Msk|">
</#if>
<#if ACC_FAULT_ENABLE>
<#assign MODE_REG_VAL = MODE_REG_VAL + "ACC_MR_FE_Msk|ACC_MR_SELFS_" + ACC_FAULT_SOURCE +"|">
</#if>
<#if ACC_INTERRUPT_ENABLE>
<#assign MODE_REG_VAL = MODE_REG_VAL + "ACC_MR_EDGETYP_" + ACC_INTERRUPT_EDGETYPE + "|">
</#if>
<#assign MODE_REG_VAL = MODE_REG_VAL?remove_ending("|")?split("|")>
</#compress>

#include <stddef.h>
<#if core.CoreSysIntFile == true>
#include "interrupts.h"
</#if>
#include "device.h"
#include "plib_${ACC_INSTANCE_NAME?lower_case}.h"


<#if ACC_INTERRUPT_ENABLE>
typedef struct
{
    ACC_CALLBACK pCallback;
    uintptr_t context;
}ACC_CALLBACK_OBJ;

static volatile ACC_CALLBACK_OBJ accCallbackObj;


</#if>
void ${ACC_INSTANCE_NAME}_Initialize(void)
{
    /* Configure mode */
    uint32_t regVal = ${ACC_INSTANCE_NAME}_REGS->ACC_MR & ~(ACC_MR_Msk);
    regVal = (<#list MODE_REG_VAL as REG_VAL>  ${REG_VAL} ${REG_VAL?is_last?string(""," |")}
            </#list>  );
    ${ACC_INSTANCE_NAME}_REGS->ACC_MR = regVal;

    /* Configure Output mask duration */
<#if ACC_OUTPUT_MASK == "0">
    ${ACC_INSTANCE_NAME}_REGS->ACC_ACR &= ~(ACC_ACR_MSEL_Msk);
<#else>
    ${ACC_INSTANCE_NAME}_REGS->ACC_ACR |= (ACC_ACR_MSEL_Msk);
</#if>

    /* Configure interrupt */
<#if ACC_INTERRUPT_ENABLE>
    ${ACC_INSTANCE_NAME}_REGS->ACC_IER |= ACC_IER_CE_Msk;
<#else>
    ${ACC_INSTANCE_NAME}_REGS->ACC_IDR |= ACC_IDR_CE_Msk;
</#if>

    /* Enable write protect */
    ${ACC_INSTANCE_NAME}_REGS->ACC_WPMR = (ACC_WPMR_WPKEY_PASSWD | ACC_WPMR_WPEN_Msk);
}


void ${ACC_INSTANCE_NAME}_Enable(void)
{
    /* Disable write protect */
    ${ACC_INSTANCE_NAME}_REGS->ACC_WPMR = (ACC_WPMR_WPKEY_PASSWD);

    /* Enable comparator */
    ${ACC_INSTANCE_NAME}_REGS->ACC_MR |= ACC_MR_ACEN_Msk;

    /* Enable write protect */
    ${ACC_INSTANCE_NAME}_REGS->ACC_WPMR = (ACC_WPMR_WPKEY_PASSWD | ACC_WPMR_WPEN_Msk);
}


void ${ACC_INSTANCE_NAME}_Disable(void)
{
    /* Disable write protect */
    ${ACC_INSTANCE_NAME}_REGS->ACC_WPMR = (ACC_WPMR_WPKEY_PASSWD);

    /* Enable comparator */
    ${ACC_INSTANCE_NAME}_REGS->ACC_MR &= ~ACC_MR_ACEN_Msk;

    /* Enable write protect */
    ${ACC_INSTANCE_NAME}_REGS->ACC_WPMR = (ACC_WPMR_WPKEY_PASSWD | ACC_WPMR_WPEN_Msk);
}
<#if ACC_INTERRUPT_ENABLE>


void ${ACC_INSTANCE_NAME}_CallbackRegister(ACC_CALLBACK pCallback, uintptr_t context)
{
    accCallbackObj.pCallback = pCallback;
    accCallbackObj.context = context;
}


void __attribute__((used)) ${ACC_INSTANCE_NAME}_InterruptHandler(void)
{
    uint32_t isr = ${ACC_INSTANCE_NAME}_REGS->ACC_ISR;
    /* Additional temporary variable used to prevent MISRA violations (Rule 13.x) */
    uintptr_t context = accCallbackObj.context;
    if ((accCallbackObj.pCallback != NULL) && ((isr & ACC_ISR_MASK_Msk) == 0U))
    {
        accCallbackObj.pCallback(((isr & ACC_ISR_SCO_Msk) != 0U), context);
    }
}
<#else>


bool ${ACC_INSTANCE_NAME}_StatusGet(ACC_STATUS_SOURCE status)
{
    uint32_t isr = ${ACC_INSTANCE_NAME}_REGS->ACC_ISR;
    return (((isr & ACC_ISR_MASK_Msk) == 0U) && ((isr & (uint32_t)status) != 0U));
}
</#if>
