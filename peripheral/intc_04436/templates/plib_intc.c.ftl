/*******************************************************************************
  INTC PLIB Implementation

  Company:
    Microchip Technology Inc.

  File Name:
    plib_intc.c

  Summary:
    INTC PLIB Source File

  Description:
    None

*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
* Copyright (C) 2024 Microchip Technology Inc. and its subsidiaries.
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

#include "${fileNameLowerCase}.h"
<#if CoreSysIntFile == true>
#include "interrupts.h"
</#if>

<#assign numOfEnabledExtInt = 0>
<#list 0..MAX_EXTERNAL_INT_COUNT as i>
    <#assign EXT_INT_PIN = "EXTERNAL_" + i + "_EXTERNAL_INTERRUPT_UPDATE">
    <#if .vars[EXT_INT_PIN]?has_content && .vars[EXT_INT_PIN] == true>
        <#assign numOfEnabledExtInt = numOfEnabledExtInt + 1>
        <#lt>volatile static EXT_INT_PIN_CALLBACK_OBJ extInt${i}CbObj;
    </#if>
</#list>

void ${moduleNameUpperCase}_Initialize( void )
{
<#if getInterruptPriorityData != "">
    /* Configure Interrupt priority */
    ${getInterruptPriorityData}
</#if>

<#list 0..MAX_EXTERNAL_INT_COUNT as i>
    <#assign EXT_INT_PIN = "EXTERNAL_" + i + "_EXTERNAL_INTERRUPT_UPDATE">
    <#if .vars[EXT_INT_PIN]?has_content && .vars[EXT_INT_PIN] == true>
            <#lt>    /* Initialize External interrupt ${i} callback object */
            <#lt>    extInt${i}CbObj.callback = NULL;
    </#if>
</#list>

<#if 0 < numOfEnabledExtInt>
<#if getExtInterruptEdgePolarity != "">
    /* Configure External Interrupt Edge Polarity */
    ${getExtInterruptEdgePolarity}
</#if>
</#if>
}

void ${moduleNameUpperCase}_SourceEnable( INT_SOURCE source )
{
    volatile uint32_t *IECx = (volatile uint32_t *)((uint32_t)&IEC0 + ((uint32_t)(0x10U * (source / 32U)) / 4U));
    *IECx |= 1UL << (source & 0x1fU);
}

void ${moduleNameUpperCase}_SourceDisable( INT_SOURCE source )
{
    volatile uint32_t *IECx = (volatile uint32_t *)((uint32_t)&IEC0 + ((uint32_t)(0x10U * (source / 32U)) / 4U));
    *IECx &= ~(1UL << (source & 0x1fU));
}

bool ${moduleNameUpperCase}_SourceIsEnabled( INT_SOURCE source )
{
    volatile uint32_t *IECx = (volatile uint32_t *)((uint32_t)&IEC0 + ((uint32_t)(0x10U * (source / 32U)) / 4U));

    return (((*IECx >> (source & 0x1fU)) & 0x01U) != 0U);
}

bool ${moduleNameUpperCase}_SourceStatusGet( INT_SOURCE source )
{
    volatile uint32_t *IFSx = (volatile uint32_t *)((uint32_t)&IFS0 + ((uint32_t)(0x10U * (source / 32U)) / 4U));

    return (((*IFSx >> (source & 0x1fU)) & 0x1U) != 0U);
}

void ${moduleNameUpperCase}_SourceStatusSet( INT_SOURCE source )
{
    volatile uint32_t *IFSx = (volatile uint32_t *) ((uint32_t)&IFS0 + ((uint32_t)(0x10U * (source / 32U)) / 4U));
    *IFSx |= 1UL << (source & 0x1fU);
}

void ${moduleNameUpperCase}_SourceStatusClear( INT_SOURCE source )
{
    volatile uint32_t *IFSx = (volatile uint32_t *) ((uint32_t)&IFS0 + ((uint32_t)(0x10U * (source / 32U)) / 4U));
    *IFSx &= ~(1UL << (source & 0x1fU));
}

void ${moduleNameUpperCase}_Enable( void )
{
    (void)__builtin_enable_interrupts();
}

bool ${moduleNameUpperCase}_Disable( void )
{
    bool processorStatus;
    
    /* Save the current processor status and then Disable the global interrupt */
    processorStatus = (${GIEStatusbit} != 0U);
            
    (void)__builtin_disable_interrupts();

    /* return the processor status */
    return processorStatus;
}

void ${moduleNameUpperCase}_Restore( bool state )
{
    if (state)
    {
        /* restore the state of Global Interrupts before the disable occurred */
       (void)__builtin_enable_interrupts();
    }
}

<#if 0 < numOfEnabledExtInt>
void ${moduleNameUpperCase}_ExternalInterruptEnable( EXTERNAL_INT_PIN extIntPin )
{
    switch (extIntPin)
    {
    <#list 0..MAX_EXTERNAL_INT_COUNT as i>
        <#assign EXT_INT_PIN = "EXTERNAL_" + i + "_EXTERNAL_INTERRUPT_UPDATE">
        <#if .vars[EXT_INT_PIN]?has_content && .vars[EXT_INT_PIN] == true>
        case EXTERNAL_INT_${i}: 
            _INT${i}IE = 1U; 
            break;

        </#if>
    </#list>
        default: /* Invalid pin, do nothing */ 
            break;
    }
}

void ${moduleNameUpperCase}_ExternalInterruptDisable( EXTERNAL_INT_PIN extIntPin )
{
    switch (extIntPin)
    {
    <#list 0..MAX_EXTERNAL_INT_COUNT as i>
        <#assign EXT_INT_PIN = "EXTERNAL_" + i + "_EXTERNAL_INTERRUPT_UPDATE">
        <#if .vars[EXT_INT_PIN]?has_content && .vars[EXT_INT_PIN] == true>
        case EXTERNAL_INT_${i}: 
            _INT${i}IE = 0U; 
            break;
            
        </#if>
    </#list>
        default: /* Invalid pin, do nothing */ 
            break;
    }
}

bool ${moduleNameUpperCase}_ExternalInterruptCallbackRegister(
    EXTERNAL_INT_PIN extIntPin,
    const EXTERNAL_INT_PIN_CALLBACK callback,
    uintptr_t context
)
{
    bool status = true;
    switch (extIntPin)
        {
<#list 0..MAX_EXTERNAL_INT_COUNT as i>
    <#assign EXT_INT_PIN = "EXTERNAL_" + i + "_EXTERNAL_INTERRUPT_UPDATE">
    <#if .vars[EXT_INT_PIN]?has_content && .vars[EXT_INT_PIN] == true>
        case EXTERNAL_INT_${i}:
            extInt${i}CbObj.callback = callback;
            extInt${i}CbObj.context  = context;
            break;
    </#if>
</#list>
        default:
            status = false;
            break;
        }

    return status;
}

<#list 0..MAX_EXTERNAL_INT_COUNT as i>
    <#assign EXT_INT_PIN = "EXTERNAL_" + i + "_EXTERNAL_INTERRUPT_UPDATE">
    <#if .vars[EXT_INT_PIN]?has_content && .vars[EXT_INT_PIN] == true>
/**
 @brief    Interrupt Handler for External Interrupt pin ${i}.

 @Note     It is an internal function called from ISR, user should not call it directly.
 */
void __attribute__((used)) INT${i}_InterruptHandler(void)
{
    uintptr_t context_var;
    if(extInt${i}CbObj.callback != NULL)
    {
        context_var = extInt${i}CbObj.context;
        extInt${i}CbObj.callback (EXTERNAL_INT_${i}, context_var);
    }
    _INT${i}IF = 0U;
}
    </#if>
</#list>
</#if>

/* End of file */