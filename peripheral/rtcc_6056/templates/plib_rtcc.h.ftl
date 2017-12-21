/*******************************************************************************
  Interface definition of RTCC PLIB.

  Company:
    Microchip Technology Inc.

  File Name:
    plib_rtcc.h

  Summary:
    Interface definition of the Watch Dog Timer Plib (RTCC).

  Description:
    This file defines the interface for the RTCC Plib.
    It allows user to setup alarm duration and access current date and time.
*******************************************************************************/

/*******************************************************************************
Copyright (c) 2016 released Microchip Technology Inc.  All rights reserved.

Microchip licenses to you the right to use, modify, copy and distribute
Software only when embedded on a Microchip microcontroller or digital signal
controller that is integrated into your product or third party product
(pursuant to the sublicense terms in the accompanying license agreement).

You should refer to the license agreement accompanying this Software for
additional information regarding your rights and obligations.

SOFTWARE AND DOCUMENTATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND,
EITHER EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION, ANY WARRANTY OF
MERCHANTABILITY, TITLE, NON-INFRINGEMENT AND FITNESS FOR A PARTICULAR PURPOSE.
IN NO EVENT SHALL MICROCHIP OR ITS LICENSORS BE LIABLE OR OBLIGATED UNDER
CONTRACT, NEGLIGENCE, STRICT LIABILITY, CONTRIBUTION, BREACH OF WARRANTY, OR
OTHER LEGAL EQUITABLE THEORY ANY DIRECT OR INDIRECT DAMAGES OR EXPENSES
INCLUDING BUT NOT LIMITED TO ANY INCIDENTAL, SPECIAL, INDIRECT, PUNITIVE OR
CONSEQUENTIAL DAMAGES, LOST PROFITS OR LOST DATA, COST OF PROCUREMENT OF
SUBSTITUTE GOODS, TECHNOLOGY, SERVICES, OR ANY CLAIMS BY THIRD PARTIES
(INCLUDING BUT NOT LIMITED TO ANY DEFENSE THEREOF), OR OTHER SIMILAR COSTS.
*******************************************************************************/

#ifndef _RTCC_H    // Guards against multiple inclusion
#define _RTCC_H

#include <xc.h>
#include <stdint.h>
#include <stdbool.h>
#include <stddef.h>
#include <sys/attribs.h>
#include <time.h>
#ifdef __cplusplus // Provide C++ Compatibility
 extern "C" {
#endif


// *****************************************************************************
// *****************************************************************************
// Section: Interface
// *****************************************************************************
// *****************************************************************************

<#if rtccEnableInterrupt == true>
	<#lt>typedef void (*RTCC_ALARM_CALLBACK)(uintptr_t context);
</#if>

<#if rtccEnableInterrupt == true>
	<#lt>typedef enum 
	<#lt>{
	<#lt>	RTCC_ALARM_MASK_OFF = 0x00,         // NO Alarm
	<#lt>	RTCC_ALARM_MASK_SS = 0x01 ,          // Every minute, seconds alarm enable
	<#lt>	RTCC_ALARM_MASK_MI = 0x02,          // Minute alarm enable
	<#lt>	RTCC_ALARM_MASK_HH = 0x04,          // Hour alarm enable
	<#lt>	RTCC_ALARM_MASK_DD = 0x08,          // Date alarm enable
	<#lt>	RTCC_ALARM_MASK_MO = 0x10,          // Month alarm enable
	<#lt>	RTCC_ALARM_MASK_MISS = 0x03,        // Every hour
	<#lt>	RTCC_ALARM_MASK_HHMISS = 0x07,      // Every day
	<#lt>	RTCC_ALARM_MASK_DDHHMISS = 0x0f,    // Every month
	<#lt>	RTCC_ALARM_MASK_MODDHHMISS = 0x1f  // Every year
	<#lt>} RTCC_ALARM_MASK;	

	<#lt>typedef struct
	<#lt>{
	<#lt>	RTCC_ALARM_CALLBACK          callback; 
	<#lt>	uintptr_t               context;
	<#lt>} RTCC_OBJECT ;

	<#lt>RTCC_OBJECT RTCC;
</#if>
/***************************** RTCC API *******************************/
void RTCC_TimeSet( struct tm *Time );
void RTCC_TimeGet( struct tm *Time );
<#if rtccEnableInterrupt == true>
	<#lt>void RTCC_AlarmSet( struct tm *alarmTime, RTCC_ALARM_MASK mask );
	<#lt>void RTCC_ALARM_CALLBACKRegister( RTCC_ALARM_CALLBACK callback, uintptr_t context );
</#if>	
<#if rtccEnableInterrupt == true>
	<#lt>void inline RTCC_ALARM_Handler( void )
	<#lt>{
	<#lt>	if(RTCC.callback != NULL)
    <#lt>        {
    <#lt>            RTCC.callback(RTCC.context);
    <#lt>        }
	<#lt>}
</#if>	
#ifdef __cplusplus // Provide C++ Compatibility
 }
#endif

#endif 