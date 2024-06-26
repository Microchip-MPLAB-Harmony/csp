/*******************************************************************************
  NVIC PLIB Implementation

  Company:
    Microchip Technology Inc.

  File Name:
    plib_nvic.c

  Summary:
    NVIC PLIB Source File

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

#include "device.h"
#include "plib_nvic.h"

<#assign NVIC_USAGE_FAULT_ENABLE = "NVIC_-10_0_ENABLE">
<#assign NVIC_BUS_FAULT_ENABLE = "NVIC_-11_0_ENABLE">
<#assign NVIC_MEM_MANAGEMENT_FAULT_ENABLE = "NVIC_-12_0_ENABLE">

// *****************************************************************************
// *****************************************************************************
// Section: NVIC Implementation
// *****************************************************************************
// *****************************************************************************

void NVIC_Initialize( void )
{
    <#if CoreArchitecture != "CORTEX-M0PLUS" && CoreArchitecture != "CORTEX-M23">
    /* Priority 0 to 7 and no sub-priority. 0 is the highest priority */
    NVIC_SetPriorityGrouping( 0x00 );
    </#if>

    /* Enable NVIC Controller */
    __DMB();
    __enable_irq();

    /* Enable the interrupt sources and configure the priorities as configured
     * from within the "Interrupt Manager" of MHC. */
<#list NVIC_VECTOR_MIN..NVIC_VECTOR_MAX as i>
    <#list 0..NVIC_VECTOR_MAX_MULTIPLE_HANDLERS as j>
        <#assign NVIC_VECTOR_NAME = "NVIC_" + i + "_" + j + "_VECTOR">
        <#assign NVIC_VECTOR_ENABLE = "NVIC_" + i + "_" + j + "_ENABLE">
        <#assign NVIC_VECTOR_ENABLE_GENERATE = "NVIC_" + i + "_" + j + "_ENABLE_GENERATE">
        <#assign NVIC_VECTOR_PRIORITY = "NVIC_" + i + "_" + j + "_PRIORITY">
        <#assign NVIC_VECTOR_PRIORITY_GENERATE = "NVIC_" + i + "_" + j + "_PRIORITY_GENERATE">
        <#assign NVIC_VECTOR_NONSECURE = "NVIC_" + i + "_" + j + "_SECURITY_TYPE">
            <#if .vars[NVIC_VECTOR_ENABLE]?has_content && (.vars[NVIC_VECTOR_ENABLE] != false)>
                <#if .vars[NVIC_VECTOR_PRIORITY_GENERATE]?has_content && (.vars[NVIC_VECTOR_PRIORITY_GENERATE] != false)>
                    <#if .vars[NVIC_VECTOR_PRIORITY]?has_content && (.vars[NVIC_VECTOR_PRIORITY]?number != 0)>
                        <#if __TRUSTZONE_ENABLED?? && __TRUSTZONE_ENABLED == "true">
                            <#if (.vars[NVIC_VECTOR_NONSECURE] == "SECURE")>
                                <#lt>    NVIC_SetPriority(${.vars[NVIC_VECTOR_NAME]}_IRQn, ${.vars[NVIC_VECTOR_PRIORITY]});
                            </#if>
                        <#else>
                            <#lt>    NVIC_SetPriority(${.vars[NVIC_VECTOR_NAME]}_IRQn, ${.vars[NVIC_VECTOR_PRIORITY]});
                        </#if>
                    </#if>
                    <#if .vars[NVIC_VECTOR_ENABLE_GENERATE]?has_content && (.vars[NVIC_VECTOR_ENABLE_GENERATE] != false)>
                        <#if __TRUSTZONE_ENABLED?? && __TRUSTZONE_ENABLED == "true">
                            <#if (.vars[NVIC_VECTOR_NONSECURE] == "SECURE")>
                                <#lt>    NVIC_EnableIRQ(${.vars[NVIC_VECTOR_NAME]}_IRQn);
                            </#if>
                        <#else>
                            <#lt>    NVIC_EnableIRQ(${.vars[NVIC_VECTOR_NAME]}_IRQn);
                        </#if>
                    </#if>
                    <#if __TRUSTZONE_ENABLED?? && __TRUSTZONE_ENABLED == "true">
                    <#if (.vars[NVIC_VECTOR_NONSECURE] == "NON-SECURE")>
                        <#lt>    NVIC_SetTargetState(${.vars[NVIC_VECTOR_NAME]}_IRQn);
                        </#if>
                    </#if>
                    <#break>
                </#if>
            </#if>
    </#list>
</#list>

<#if .vars[NVIC_USAGE_FAULT_ENABLE]?has_content && (.vars[NVIC_USAGE_FAULT_ENABLE]==true)>
    /* Enable Usage fault */
    SCB->SHCSR |= (SCB_SHCSR_USGFAULTENA_Msk);
    /* Trap divide by zero */
    SCB->CCR   |= SCB_CCR_DIV_0_TRP_Msk;
</#if>

<#if .vars[NVIC_BUS_FAULT_ENABLE]?has_content && (.vars[NVIC_BUS_FAULT_ENABLE]==true)>
    /* Enable Bus fault */
    SCB->SHCSR |= (SCB_SHCSR_BUSFAULTENA_Msk);
</#if>

<#if .vars[NVIC_MEM_MANAGEMENT_FAULT_ENABLE]?has_content && (.vars[NVIC_MEM_MANAGEMENT_FAULT_ENABLE]==true)>
    /* Enable memory management fault */
    SCB->SHCSR |= (SCB_SHCSR_MEMFAULTENA_Msk);
</#if>

}

void NVIC_INT_Enable( void )
{
    __DMB();
    __enable_irq();
}

bool NVIC_INT_Disable( void )
{
    bool processorStatus = (__get_PRIMASK() == 0U);

    __disable_irq();
    __DMB();

    return processorStatus;
}

void NVIC_INT_Restore( bool state )
{
    if( state == true )
    {
        __DMB();
        __enable_irq();
    }
    else
    {
        __disable_irq();
        __DMB();
    }
}

bool NVIC_INT_SourceDisable( IRQn_Type source )
{
    bool processorStatus;
    bool intSrcStatus;

    processorStatus = NVIC_INT_Disable();
    intSrcStatus = (NVIC_GetEnableIRQ(source) != 0U);
    NVIC_DisableIRQ( source );
    NVIC_INT_Restore( processorStatus );

    /* return the source status */
    return intSrcStatus;
}

void NVIC_INT_SourceRestore( IRQn_Type source, bool status )
{
    if( status ) {
       NVIC_EnableIRQ( source );
    }

    return;
}