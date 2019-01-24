/*******************************************************************************
  EVIC PLIB Implementation

  Company:
    Microchip Technology Inc.

  File Name:
    plib_evic.c

  Summary:
    EVIC PLIB Source File

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

#include "device.h"
#include "plib_evic.h"

// *****************************************************************************
// *****************************************************************************
// Section: IRQ Implementation
// *****************************************************************************
// *****************************************************************************

void EVIC_Initialize( void )
{
    INTCONSET = _INTCON_MVEC_MASK;
    
    /* Set up priority / subpriority of enabled interrupts */
<#list EVIC_VECTOR_MIN..EVIC_VECTOR_MAX as i>
    <#lt><#assign ENABLE = "EVIC_" + i + "_ENABLE">
    <#lt><#assign IPCREG = "EVIC_" + i + "_REGNAME">  <#-- IPCx register for given interrupt -->
    <#lt><#assign PRIOVALUE = "EVIC_" + i + "_PRIORITY">
    <#lt><#assign SUBPRIOVALUE = "EVIC_" + i + "_SUBPRIORITY">
    <#lt><#assign PRIOVALUE_SHIFTED = "EVIC_" + i + "_PRIVALUE">  <#-- priority, shifted to correct place in IPCx register -->
    <#lt><#assign SUBPRIOVALUE_SHIFTED = "EVIC_" + i + "_SUBPRIVALUE">  <#-- subpriority, shifted to correct place in IPCx register -->
    <#lt><#assign INT_NAME = "EVIC_" + i + "_NAME">
    <#lt><#if .vars[ENABLE]?? && .vars[ENABLE] == true>
    <#lt>    ${.vars[IPCREG]}SET = 0x${.vars[PRIOVALUE_SHIFTED]} | 0x${.vars[SUBPRIOVALUE_SHIFTED]};  /* ${.vars[INT_NAME]}:  Priority ${.vars[PRIOVALUE]} / Subpriority ${.vars[SUBPRIOVALUE]} */
    <#lt></#if>
</#list>
}



