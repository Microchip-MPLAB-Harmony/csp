/*******************************************************************************
  NVIC PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_nvic.h

  Summary:
    NVIC PLIB Header File

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

#ifndef PLIB_NVIC_H
#define PLIB_NVIC_H

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    extern "C" {

#endif
// DOM-IGNORE-END


/***************************** NVIC Inline *******************************/

void static inline NVIC_Initialize( void )
{
	/* Priority 0 to 7 and no sub-priority. 0 is the highest priority */
	NVIC_SetPriorityGrouping( 0x04 );

	/* Enable NVIC Controller */
    __DMB();
    __enable_irq();

	/* Enable the interrupt sources and configure the priorities as configured
	 * from within the "Interrupt Manager" of MCC. */
<#list 0..100 as i>
	<#assign NVIC_VECTOR_ENABLE = "NVIC_" + i + "_ENABLE">
    <#assign NVIC_VECTOR_NAME = "NVIC_" + i + "_VECTOR">
	<#assign NVIC_VECTOR_PRIORITY = "NVIC_" + i + "_PRIORITY">
        <#if .vars[NVIC_VECTOR_ENABLE]?has_content>
            <#if (.vars[NVIC_VECTOR_ENABLE] != false)>
	NVIC_EnableIRQ(${.vars[NVIC_VECTOR_NAME]}_IRQn);
	NVIC_SetPriority(${.vars[NVIC_VECTOR_NAME]}_IRQn, ${.vars[NVIC_VECTOR_PRIORITY]});
            </#if>
        </#if>
</#list>

    return;
}


// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END
#endif // PLIB_NVIC_H
