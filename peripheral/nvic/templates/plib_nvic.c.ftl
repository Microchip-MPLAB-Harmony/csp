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
* © 2018 Microchip Technology Inc. and its subsidiaries.
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

// *****************************************************************************
// *****************************************************************************
// Section: NVIC Implementation
// *****************************************************************************
// *****************************************************************************

void NVIC_Initialize( void )
{
    <#if CoreArchitecture != "CORTEX-M0+">
    /* Priority 0 to 7 and no sub-priority. 0 is the highest priority */
    NVIC_SetPriorityGrouping( 0x04 );
    </#if>

    /* Enable NVIC Controller */
    __DMB();
    __enable_irq();

    /* Enable the interrupt sources and configure the priorities as configured
     * from within the "Interrupt Manager" of MCC. */
<#list NVIC_VECTOR_MIN..NVIC_VECTOR_MAX as i>
    <#list 0..NVIC_VECTOR_MAX_MULTIPLE_HANDLERS as j>
        <#assign NVIC_VECTOR_NAME = "NVIC_" + i + "_" + j + "_VECTOR">
        <#assign NVIC_VECTOR_ENABLE = "NVIC_" + i + "_" + j + "_ENABLE">
        <#assign NVIC_VECTOR_ENABLE_GENERATE = "NVIC_" + i + "_" + j + "_ENABLE_GENERATE">
        <#assign NVIC_VECTOR_PRIORITY = "NVIC_" + i + "_" + j + "_PRIORITY">
        <#assign NVIC_VECTOR_PRIORITY_GENERATE = "NVIC_" + i + "_" + j + "_PRIORITY_GENERATE">
            <#if .vars[NVIC_VECTOR_ENABLE]?has_content && (.vars[NVIC_VECTOR_ENABLE] != false)>
                <#if .vars[NVIC_VECTOR_PRIORITY_GENERATE]?has_content && (.vars[NVIC_VECTOR_PRIORITY_GENERATE] != false)>
                    <#if .vars[NVIC_VECTOR_PRIORITY]?has_content && (.vars[NVIC_VECTOR_PRIORITY]?number != 0)>
    NVIC_SetPriority(${.vars[NVIC_VECTOR_NAME]}_IRQn, ${.vars[NVIC_VECTOR_PRIORITY]});
                    </#if>
                    <#if .vars[NVIC_VECTOR_ENABLE_GENERATE]?has_content && (.vars[NVIC_VECTOR_ENABLE_GENERATE] != false)>
    NVIC_EnableIRQ(${.vars[NVIC_VECTOR_NAME]}_IRQn);
                    </#if>
                    <#break>
                </#if>
            </#if>
    </#list>    
</#list>

    return;
}