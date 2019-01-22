/*******************************************************************************
  PIC32MZ PLIB Implementation

  Company:
    Microchip Technology Inc.

  File Name:
    plib_int.c

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

#include "device.h"
#include "plib_int.h"

// *****************************************************************************
// *****************************************************************************
// Section: IRQ Implementation
// *****************************************************************************
// *****************************************************************************
void INT_Initialize( void )
{
    INTCONSET = _INTCON_MVEC_MASK;
    
    /* Set up priority / subpriority of enabled interrupts */
<#list INT_VECTOR_MIN..INT_VECTOR_MAX as i>
    <#lt><#assign INT_FIRST_NAME_KEY =  "INT_FIRST_NAME_KEY_" + i?string >
    <#lt><#if .vars[INT_FIRST_NAME_KEY]??>
        <#lt><#assign ENABLE = "NVIC_"+i+"_0_ENABLE">
        <#lt><#assign IPCREG = "NVIC_"+i+"_0_REGNAME">  <#-- IPCx register for given interrupt -->
        <#lt><#assign PRIOVALUE = "NVIC_" + i + "_0_PRIORITY">
        <#lt><#assign SUBPRIOVALUE = "NVIC_" + i + "_0_SUBPRIORITY">
        <#lt><#assign PRIOVALUE_SHIFTED = "NVIC_"+i+"_0_PRIVALUE">  <#-- priority, shifted to correct place in IPCx register -->
        <#lt><#assign SUBPRIOVALUE_SHIFTED = "NVIC_"+i+"_0_SUBPRIVALUE">  <#-- subpriority, shifted to correct place in IPCx register -->
        <#lt><#assign INTNAME = "INT_FIRST_NAME_STRING_"+i>
        <#lt><#if .vars[ENABLE]?c == "true">
        <#lt>    ${.vars[IPCREG]}SET = 0x${.vars[PRIOVALUE_SHIFTED]} | 0x${.vars[SUBPRIOVALUE_SHIFTED]};  /* ${.vars[INTNAME]}:  Priority ${.vars[PRIOVALUE]} / Subpriority ${.vars[SUBPRIOVALUE]} */
        <#lt></#if>
    <#lt></#if>
</#list>
}



