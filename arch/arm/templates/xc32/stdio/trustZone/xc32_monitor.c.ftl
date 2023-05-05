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
#include <stddef.h>
<#if stdio_s??>
    <#if stdio_s.SECURE_DEBUG_PERIPHERAL?has_content>
        <#lt>#include "definitions.h"
    </#if>
</#if>

/* Declaration of these functions are missing in stdio_s.h for ARM parts*/
/* MISRAC 2012 deviation block start */
/* MISRA C-2012 Rule 21.2 deviated four times.  Deviation record ID -  H3_MISRAC_2012_R_21_2_DR_1 */
<#if COVERITY_SUPPRESS_DEVIATION?? && COVERITY_SUPPRESS_DEVIATION>
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wunknown-pragmas"
#pragma coverity compliance block deviate:4 "MISRA C-2012 Rule 21.2" "H3_MISRAC_2012_R_21_2_DR_1"
</#if>

<#if stdio_s??>
<#if stdio_s.SECURE_DEBUG_PERIPHERAL?has_content>
<#assign USART_PLIB = "stdio_s.SECURE_DEBUG_PERIPHERAL">
<#assign USART_PLIB_RX_ENABLED = USART_PLIB?eval + ".USART_RX_ENABLE">
<#assign USART_PLIB_TX_ENABLED = USART_PLIB?eval + ".USART_TX_ENABLE">
</#if>
</#if>

int read(int handle, void *buffer, unsigned int len)
{
    <#if stdio_s??>
        <#if stdio_s.SECURE_DEBUG_PERIPHERAL?has_content>
            <#if USART_PLIB_RX_ENABLED?eval??>
                <#if USART_PLIB_RX_ENABLED?eval>
                    <#lt>    int nChars = 0;
                    <#lt>    bool success = false;
                    <#lt>    (void)len;
                    <#lt>    if ((handle == 0)  && (len > 0))
                    <#lt>    {
                    <#lt>        do
                    <#lt>        {
                    <#lt>            success = ${.vars["${stdio_s.SECURE_DEBUG_PERIPHERAL?lower_case}"].USART_PLIB_API_PREFIX}_Read(buffer, 1);
                    <#lt>        }while( !success);
                    <#lt>        nChars = 1;
                    <#lt>    }
                    <#lt>    return nChars;
                <#else>
                    <#lt>    return -1;
                </#if>
            <#else>
                <#lt>    int nChars = 0;
                <#lt>    bool success = false;
                <#lt>    (void)len;
                <#lt>    if ((handle == 0)  && (len > 0))
                <#lt>    {
                <#lt>        do
                <#lt>        {
                <#lt>            success = ${.vars["${stdio_s.SECURE_DEBUG_PERIPHERAL?lower_case}"].USART_PLIB_API_PREFIX}_Read(buffer, 1);
                <#lt>        }while( !success);
                <#lt>        nChars = 1;
                <#lt>    }
                <#lt>    return nChars;
            </#if>
        <#else>
            <#lt>   return -1;
        </#if>
    <#else>
        <#lt>   return -1;
    </#if>
}

int write(int handle, void * buffer, size_t count)
{
    <#if stdio_s??>
        <#if stdio_s.SECURE_DEBUG_PERIPHERAL?has_content>
            <#if USART_PLIB_TX_ENABLED?eval??>
                <#if USART_PLIB_TX_ENABLED?eval>
                    <#lt>   bool success = false;
                    <#lt>   if (handle == 1)
                    <#lt>   {
                    <#lt>       do
                    <#lt>       {
                    <#lt>           success = ${.vars["${stdio_s.SECURE_DEBUG_PERIPHERAL?lower_case}"].USART_PLIB_API_PREFIX}_Write(buffer, count);
                    <#lt>       }while( !success);
                    <#lt>   }
                    <#lt>   return count;
                <#else>
                    <#lt>   return -1;
                </#if>
            <#else>
                <#lt>   bool success = false;
                <#lt>   if (handle == 1)
                <#lt>   {
                <#lt>       do
                <#lt>       {
                <#lt>           success = ${.vars["${stdio_s.SECURE_DEBUG_PERIPHERAL?lower_case}"].USART_PLIB_API_PREFIX}_Write(buffer, count);
                <#lt>       }while( !success);
                <#lt>   }
                <#lt>   return count;
            </#if>
        <#else>
            <#lt>   return -1;
        </#if>
    <#else>
        <#lt>   return -1;
    </#if>
}

<#if COVERITY_SUPPRESS_DEVIATION?? && COVERITY_SUPPRESS_DEVIATION>
#pragma coverity compliance end_block "MISRA C-2012 Rule 21.2"
#pragma GCC diagnostic pop
</#if>
/* MISRAC 2012 deviation block end */