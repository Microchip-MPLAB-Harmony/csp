/*******************************************************************************
  Analog Comparator Controller (ACC) Peripheral Library (PLIB)

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${ACC_INSTANCE_NAME?lower_case}.c

  Summary:
    ACC Source File

  Description:
    None

*******************************************************************************/

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
#include "plib_${ACC_INSTANCE_NAME?lower_case}.h"

<#--Implementation-->
// *****************************************************************************
// *****************************************************************************
// Section: ACC Implementation
// *****************************************************************************
// *****************************************************************************

void ${ACC_INSTANCE_NAME}_Initialize (void)
{
    uint32_t regValue = 0U;
    /*Reset ACC registers*/
    ${ACC_INSTANCE_NAME}_REGS->ACC_CR = ACC_CR_SWRST_Msk;

    /*Set Comparator Positive and Negative Input, Output Invert status to
      Enable/Disable, Fault Generation to Enable/Disable, Set Fault source and
      Output Edge type*/
    <#if HAS_MINUS_COMPARATOR_SELECTION??>
    regValue |= ACC_MR_SELMINUS(${ACC_MR_SELMINUS}U);
    </#if>
    <#if HAS_PLUS_COMPARATOR_SELECTION??>
    regValue |= ACC_MR_SELPLUS(${ACC_MR_SELPLUS}U);
    </#if>
    <#if HAS_EDGETYPE??>
    regValue |= ACC_MR_EDGETYP(${ACC_MR_EDGETYP}U);
    </#if>
    <#if HAS_INVERTED_COMPARATOR??>
    regValue |= ${ACC_ACR_INV?then('ACC_MR_INV_Msk', '0U')};
    </#if>
    <#if HAS_FAULT_ENABLE??>
    regValue |= ${ACC_ACR_FE?then('ACC_MR_FE_Msk', '0U')};
    regValue |= ACC_MR_SELFS_${ACC_MR_SELFS};
    </#if>
    regValue |= ACC_MR_ACEN_Msk;
    ${ACC_INSTANCE_NAME}_REGS->ACC_MR = regValue;

    <#if HAS_CURRENT_SELECTION?? && HAS_HYSTERESIS??>
    /*Set Current level and Hysteresis level*/
    ${ACC_INSTANCE_NAME}_REGS->ACC_ACR = ACC_ACR_ISEL_${ACC_ACR_ISEL} | ACC_ACR_HYST(${ACC_ACR_HYST}U);
    </#if>

    <#if HAS_INTERRUPTS??>
    <#if INTERRUPT_MODE == true>
    /* Enable Interrupt     */
    ${ACC_INSTANCE_NAME}_REGS->ACC_IER = ACC_IER_CE_Msk;
    </#if>

    /*Wait till output mask period gets over*/
    while ((${ACC_INSTANCE_NAME}_REGS->ACC_ISR & ACC_ISR_MASK_Msk) != 0U)
    {
        /* Do nothing */
    }
    </#if>
}

<#if HAS_INTERRUPTS??>
bool ${ACC_INSTANCE_NAME}_StatusGet (ACC_STATUS_SOURCE status_var)
{
    return ((${ACC_INSTANCE_NAME}_REGS->ACC_ISR & (uint32_t)status_var) != 0U);
}

<#if INTERRUPT_MODE == true>

static ACC_OBJECT ${ACC_INSTANCE_NAME?lower_case}Obj;

void ${ACC_INSTANCE_NAME}_CallbackRegister (ACC_CALLBACK callback, uintptr_t context)
{
    ${ACC_INSTANCE_NAME?lower_case}Obj.callback = callback;
    ${ACC_INSTANCE_NAME?lower_case}Obj.context = context;
}

void ${ACC_INSTANCE_NAME}_InterruptHandler( void )
{
    // Clear the interrupt
    ${ACC_INSTANCE_NAME}_REGS->ACC_ISR;

    // Callback user function
    if(${ACC_INSTANCE_NAME?lower_case}Obj.callback != NULL)
    {
        ${ACC_INSTANCE_NAME?lower_case}Obj.callback(${ACC_INSTANCE_NAME?lower_case}Obj.context);
    }
}
</#if>
</#if>

