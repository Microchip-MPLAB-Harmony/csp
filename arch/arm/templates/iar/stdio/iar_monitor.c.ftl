/*******************************************************************************
 Debug Console Source file 

  Company:
    Microchip Technology Inc.

  File Name:
    iar_monitor.c

  Summary:
    iar monitor file with IAR compiler support

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
<#lt>#include <stddef.h>    // size_t
<#lt><#if stdio?? && stdio.DEBUG_PERIPHERAL?has_content>
    <#lt>#include <yfuns.h>      // _LLIO_ERROR, _LLIO_STDOUT, _LLIO_STDIN, _LLIO_STDERR
    <#lt>#include <stdbool.h>    // true
    <#lt>#include "definitions.h"
<#lt></#if>

<#if stdio??>
<#if stdio.DEBUG_PERIPHERAL?has_content>
<#assign USART_PLIB = "stdio.DEBUG_PERIPHERAL">
<#assign USART_PLIB_RX_ENABLED = USART_PLIB?eval + ".USART_RX_ENABLE">
<#assign USART_PLIB_TX_ENABLED = USART_PLIB?eval + ".USART_TX_ENABLE">
</#if>
</#if>

/*******************
 *
 * Copyright 1998-2003 IAR Systems.  All rights reserved.
 *
 * $Revision: 38614 $
 *
 * This is a template implementation of the "__write" function used by
 * the standard library.  Replace it with a system-specific
 * implementation.
 *
 * The "__write" function should output "size" number of bytes from
 * "buffer" in some application-specific way.  It should return the
 * number of characters written, or _LLIO_ERROR on failure.
 *
 * If "buffer" is zero then __write should perform flushing of
 * internal buffers, if any.  In this case "handle" can be -1 to
 * indicate that all handles should be flushed.
 *
 * The template implementation below assumes that the application
 * provides the function "MyLowLevelPutchar".  It should return the
 * character written, or -1 on failure.
 *
 ********************/
/*
 * Note: "handle == -1" means that all handles should be flushed
 *
 * This code only writes to "standard out" and "standard err",
 * for all other file handles it returns failure, (_LLIO_ERROR), 
 * -- a low level IO error
*/

size_t 
__write( int handle, const unsigned char * buffer, size_t size )
{
<#lt><#if stdio?? && stdio.DEBUG_PERIPHERAL?has_content>
    <#if USART_PLIB_RX_ENABLED?eval??>
        <#if USART_PLIB_RX_ENABLED?eval>
            <#lt>    size_t nChars = _LLIO_ERROR;
            <#lt>    if(     handle == _LLIO_STDOUT 
            <#lt>        ||  handle == _LLIO_STDERR 
            <#lt>    ){
            <#lt>        nChars = 0;
            <#lt>        if( buffer ){
            <#lt>           nChars = ${.vars["${stdio.DEBUG_PERIPHERAL?lower_case}"].USART_PLIB_API_PREFIX}_Write( (void*) buffer, size );      // "MyLowLevelPutchar"
            <#lt>        }
            <#lt>    }
        </#if>
    <#else>
        <#lt>    size_t nChars = _LLIO_ERROR;
        <#lt>    if(     handle == _LLIO_STDOUT 
        <#lt>        ||  handle == _LLIO_STDERR 
        <#lt>    ){
        <#lt>        nChars = 0;
        <#lt>        if( buffer ){
        <#lt>           nChars = ${.vars["${stdio.DEBUG_PERIPHERAL?lower_case}"].USART_PLIB_API_PREFIX}_Write( (void*) buffer, size );      // "MyLowLevelPutchar"
        <#lt>        }
        <#lt>    }
    </#if>
<#lt><#else>
    <#lt>    (void) handle;      // avoid compiler warning
    <#lt>    (void) buffer;      // avoid compiler warning
    <#lt>    (void) size;        // avoid compiler warning
    <#lt>    size_t nChars = 0;
<#lt></#if>

    return( nChars );
}

/*******************
 *
 * Copyright 1998-2003 IAR Systems.  All rights reserved.
 *
 * $Revision: 38614 $
 *
 * This is a template implementation of the "__read" function used by
 * the standard library.  Replace it with a system-specific
 * implementation.
 *
 * The "__read" function reads a number of bytes, at most "size" into
 * the memory area pointed to by "buffer".  It returns the number of
 * bytes read, 0 at the end of the file, or _LLIO_ERROR if failure
 * occurs.
 *
 * The template implementation below assumes that the application
 * provides the function "MyLowLevelGetchar".  It should return a
 * character value, or -1 on failure.
 *
********************/
/* Note: This template only reads from "standard in"; for all other file 
 * handles it returns failure. 
*/

size_t
__read( int handle, unsigned char * buffer, size_t size )
{
<#lt><#if stdio?? && stdio.DEBUG_PERIPHERAL?has_content>
    <#if USART_PLIB_TX_ENABLED?eval??>
        <#if USART_PLIB_TX_ENABLED?eval>
            <#lt>    size_t nChars = _LLIO_ERROR;
            <#lt>    if( handle == _LLIO_STDIN ){
            <#lt>        unsigned char cc = 0;
            <#lt>        for( nChars = 0; nChars < size; ++nChars ){
            <#lt>            while( ${.vars["${stdio.DEBUG_PERIPHERAL?lower_case}"].USART_PLIB_API_PREFIX}_Read( (void*) &cc, 1 ) != true );     // "MyLowLevelGetchar"
            <#lt>            if( cc ){
            <#lt>                buffer[ nChars ] = cc;
            <#lt>            }
            <#lt>            else{
            <#lt>                break;
            <#lt>            }
            <#lt>        }
            <#lt>    }
        </#if>
    <#else>
        <#lt>    size_t nChars = _LLIO_ERROR;
        <#lt>    if( handle == _LLIO_STDIN ){
        <#lt>        unsigned char cc = 0;
        <#lt>        for( nChars = 0; nChars < size; ++nChars ){
        <#lt>            while( ${.vars["${stdio.DEBUG_PERIPHERAL?lower_case}"].USART_PLIB_API_PREFIX}_Read( (void*) &cc, 1 ) != true );     // "MyLowLevelGetchar"
        <#lt>            if( cc ){
        <#lt>                buffer[ nChars ] = cc;
        <#lt>            }
        <#lt>            else{
        <#lt>                break;
        <#lt>            }
        <#lt>        }
        <#lt>    }
    </#if>
<#lt><#else>        
    <#lt>    (void) handle;      // avoid compiler warning
    <#lt>    (void) buffer;      // avoid compiler warning
    <#lt>    (void) size;        // avoid compiler warning
    <#lt>    size_t nChars = 0;
<#lt></#if>

    return( nChars );
}
