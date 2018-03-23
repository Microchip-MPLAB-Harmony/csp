/*******************************************************************************
  NVIC PLIB Implementation

  Company:
    Microchip Technology Inc.

  File Name:
    plib_nvic.h

  Summary:
    NVIC PLIB Source File

  Description:
    None

*******************************************************************************/

/*******************************************************************************
Copyright (c) 2017 released Microchip Technology Inc.  All rights reserved.

Microchip licenses to you the right to use, modify, copy and distribute
Software only when embedded on a Microchip microcontroller or digital signal
controller that is integrated into your product or third party product
(pursuant to the sublicense terms in the accompanying license agreement).

You should refer to the license agreement accompanying this Software for
additional information regarding your rights and obligations.

SOFTWARE AND DOCUMENTATION ARE PROVIDED AS IS  WITHOUT  WARRANTY  OF  ANY  KIND,
EITHER EXPRESS  OR  IMPLIED,  INCLUDING  WITHOUT  LIMITATION,  ANY  WARRANTY  OF
MERCHANTABILITY, TITLE, NON-INFRINGEMENT AND FITNESS FOR A  PARTICULAR  PURPOSE.
IN NO EVENT SHALL MICROCHIP OR  ITS  LICENSORS  BE  LIABLE  OR  OBLIGATED  UNDER
CONTRACT, NEGLIGENCE, STRICT LIABILITY, CONTRIBUTION,  BREACH  OF  WARRANTY,  OR
OTHER LEGAL  EQUITABLE  THEORY  ANY  DIRECT  OR  INDIRECT  DAMAGES  OR  EXPENSES
INCLUDING BUT NOT LIMITED TO ANY  INCIDENTAL,  SPECIAL,  INDIRECT,  PUNITIVE  OR
CONSEQUENTIAL DAMAGES, LOST  PROFITS  OR  LOST  DATA,  COST  OF  PROCUREMENT  OF
SUBSTITUTE  GOODS,  TECHNOLOGY,  SERVICES,  OR  ANY  CLAIMS  BY  THIRD   PARTIES
(INCLUDING BUT NOT LIMITED TO ANY DEFENSE  THEREOF),  OR  OTHER  SIMILAR  COSTS.
*******************************************************************************/

#include "${__PROCESSOR?lower_case}.h"
#include "plib_nvic.h"

// *****************************************************************************
// *****************************************************************************
// Section: NVIC Implementation
// *****************************************************************************
// *****************************************************************************

void NVIC_Initialize( void )
{
    /* Priority 0 to 7 and no sub-priority. 0 is the highest priority */
    NVIC_SetPriorityGrouping( 0x04 );

    /* Enable NVIC Controller */
    __DMB();
    __enable_irq();

    /* Enable the interrupt sources and configure the priorities as configured
     * from within the "Interrupt Manager" of MCC. */
<#list NVIC_VECTOR_MIN..NVIC_VECTOR_MAX as i>
    <#assign NVIC_VECTOR_ENABLE = "NVIC_" + i + "_ENABLE">
    <#assign NVIC_VECTOR_NAME = "NVIC_" + i + "_VECTOR">
    <#assign NVIC_VECTOR_CORE = "NVIC_" + i + "_CORE">
    <#assign NVIC_VECTOR_CORE_FIXED = "NVIC_" + i + "_CORE_FIXED">
    <#assign NVIC_VECTOR_PRIORITY = "NVIC_" + i + "_PRIORITY">
        <#if .vars[NVIC_VECTOR_CORE_FIXED]?has_content && (.vars[NVIC_VECTOR_CORE_FIXED] == false)>
            <#if .vars[NVIC_VECTOR_ENABLE]?has_content && (.vars[NVIC_VECTOR_ENABLE] != false)>
                <#if .vars[NVIC_VECTOR_PRIORITY]?has_content && (.vars[NVIC_VECTOR_PRIORITY]?number != 0)>
    NVIC_SetPriority(${.vars[NVIC_VECTOR_NAME]}_IRQn, ${.vars[NVIC_VECTOR_PRIORITY]});
                </#if>
                <#if .vars[NVIC_VECTOR_CORE]?has_content && (.vars[NVIC_VECTOR_CORE] == false)>
    NVIC_EnableIRQ(${.vars[NVIC_VECTOR_NAME]}_IRQn);
                </#if>
            </#if>
        </#if>
</#list>

    return;
}
