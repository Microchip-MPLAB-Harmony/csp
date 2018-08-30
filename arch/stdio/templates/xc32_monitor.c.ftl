/*******************************************************************************
 Debug Console Source file 

  Company:
    Microchip Technology Inc.

  File Name:
    debug_console.c

  Summary:
    RSTC Source File

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

<#if stdio??>
    <#if stdio.DEBUG_PERIPHERAL?has_content>
        <#lt>#include "definitions.h"
    </#if>
</#if>

int _mon_getc(int canblock)
{
    <#if stdio??>
        <#if stdio.DEBUG_PERIPHERAL?has_content>
        <#lt>   volatile int c = 0;
        <#lt>   while(${.vars["${stdio.DEBUG_PERIPHERAL?lower_case}"].USART_PLIB_API_PREFIX}_Read((void*)&c, 1) != true);
        <#lt>   return c;
        <#else>
            <#lt>   return 0;
        </#if>
    <#else>
        <#lt>   return 0;
    </#if>
}

void _mon_putc(char c)
{
    <#if stdio??>
        <#if stdio.DEBUG_PERIPHERAL?has_content>
        <#lt>   uint8_t size = 0;
        <#lt>   do
        <#lt>   {
        <#lt>       size = ${.vars["${stdio.DEBUG_PERIPHERAL?lower_case}"].USART_PLIB_API_PREFIX}_Write((void*)&c, 1);
        <#lt>   }while (size != 1);
        </#if>
    </#if>
}