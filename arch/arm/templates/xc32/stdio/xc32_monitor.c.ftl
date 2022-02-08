/*******************************************************************************
 Debug Console Source file

  Company:
    Microchip Technology Inc.

  File Name:
    xc32_monitor.c

  Summary:
    debug console Source File

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

/* Declaration of these functions are missing in stdio.h for ARM parts*/
/* MISRAC 2012 deviation block start */
/* MISRA C-2012 Rule 21.2 deviated four times.  Deviation record ID -  H3_MISRAC_2012_R_21_2_DR_1 */
<#if COVERITY_SUPPRESS_DEVIATION?? && COVERITY_SUPPRESS_DEVIATION>
#pragma coverity compliance block deviate:4 "MISRA C-2012 Rule 21.2" "H3_MISRAC_2012_R_21_2_DR_1"
</#if>

#ifdef __arm__
int _mon_getc(int canblock);
void _mon_putc(char c);
#endif //__arm__

int _mon_getc(int canblock)
{
    <#if stdio??>
        <#if stdio.DEBUG_PERIPHERAL?has_content>
        <#lt>   int c = 0;
        <#lt>   bool success = false;
        <#lt>   (void)canblock;
        <#lt>   do
        <#lt>   {
        <#lt>       success = ${.vars["${stdio.DEBUG_PERIPHERAL?lower_case}"].USART_PLIB_API_PREFIX}_Read(&c, 1);                
        <#lt>   }while( !success);
        <#lt>   return c;
        <#else>
            <#lt>   return 0;
        </#if>
    <#else>
        <#lt>   (void)canblock;
        <#lt>   return 0;
    </#if>
}

void _mon_putc(char c)
{
    <#if stdio??>
        <#if stdio.DEBUG_PERIPHERAL?has_content>
        <#lt>   bool success = false;
        <#lt>   do
        <#lt>   {
        <#lt>       success = ${.vars["${stdio.DEBUG_PERIPHERAL?lower_case}"].USART_PLIB_API_PREFIX}_Write(&c, 1);
        <#lt>   }while (!success);
        </#if>
    <#else>
        <#lt>   (void)c;
    </#if>
}

<#if COVERITY_SUPPRESS_DEVIATION?? && COVERITY_SUPPRESS_DEVIATION>
#pragma coverity compliance end_block "MISRA C-2012 Rule 21.2"
</#if>
/* MISRAC 2012 deviation block end */