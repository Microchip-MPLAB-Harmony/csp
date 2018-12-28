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