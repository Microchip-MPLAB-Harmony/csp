/*******************************************************************************
  Interface definition of RTC PLIB.

  Company:
    Microchip Technology Inc.

  File Name:
    plib_rtc.h

  Summary:
    Interface definition of the Watch Dog Timer Plib (RTC).

  Description:
    This file defines the interface for the RTC Plib.
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

#ifndef RTC${INDEX?string}_H    // Guards against multiple inclusion
#define RTC${INDEX?string}_H


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

<#if rtcEnableInterrupt == true>
	<#lt>typedef void (*RTC_ALARM_CALLBACK)(uintptr_t context, uint32_t int_cause);
</#if>

<#if rtcEnableInterrupt == true>
	<#lt>typedef enum 
	<#lt>{
	<#lt>	RTC_ALARM_MASK_OFF = 0x00,         // NO Alarm
	<#lt>	RTC_ALARM_MASK_SS = 0x01 ,          // Every minute, seconds alarm enable
	<#lt>	RTC_ALARM_MASK_MI = 0x02,          // Minute alarm enable
	<#lt>	RTC_ALARM_MASK_HH = 0x04,          // Hour alarm enable
	<#lt>	RTC_ALARM_MASK_DD = 0x08,          // Date alarm enable
	<#lt>	RTC_ALARM_MASK_MO = 0x10,          // Month alarm enable
	<#lt>	RTC_ALARM_MASK_MISS = 0x03,        // Every hour
	<#lt>	RTC_ALARM_MASK_HHMISS = 0x07,      // Every day
	<#lt>	RTC_ALARM_MASK_DDHHMISS = 0x0f,    // Every month
	<#lt>	RTC_ALARM_MASK_MODDHHMISS = 0x1f  // Every year
	<#lt>} RTC_ALARM_MASK;	

	<#lt>typedef enum 
	<#lt>{
	<#lt>	RTC_INT_ALARM = 0x02,          // Alarm Event
	<#lt>	RTC_INT_TIME = 0x08 ,          // Time Event
	<#lt>	RTC_INT_CALENDAR = 0x10,          // Calendar enable
	<#lt>} RTC_INT_MASK;	
	
	<#lt>typedef struct
	<#lt>{
	<#lt>	RTC_ALARM_CALLBACK          callback; 
	<#lt>	uintptr_t               context;
	<#lt>} RTC_OBJECT ;

	<#lt>RTC_OBJECT rtc;
</#if>
/***************************** RTC API *******************************/
void RTC${INDEX?string}_Initialize( void );
bool RTC${INDEX?string}_TimeSet( struct tm *Time );
void RTC${INDEX?string}_TimeGet( struct tm *Time );
<#if rtcEnableInterrupt == true>
	<#lt>bool RTC${INDEX?string}_AlarmSet( struct tm *alarmTime, RTC_ALARM_MASK mask );
	<#lt>void RTC${INDEX?string}_CallbackRegister( RTC_ALARM_CALLBACK callback, uintptr_t context );
	<#lt>void RTC${INDEX?string}_InterruptDisable(RTC_INT_MASK interrupt);
	<#lt>void RTC${INDEX?string}_InterruptEnable(RTC_INT_MASK interrupt);
</#if>	
<#if rtcEnableInterrupt == true>
	<#lt>static void inline RTC${INDEX?string}_ALARM_Handler( void )
	<#lt>{
	<#lt>	volatile uint32_t status = _RTC_REGS->RTC_SR.w;
	<#lt>	_RTC_REGS->RTC_SCCR |= RTC_SCCR_ALRCLR_Msk | RTC_SCCR_TIMCLR_Msk |  RTC_SCCR_CALCLR_Msk;
	<#lt>	if(rtc.callback != NULL)
    <#lt>        {
    <#lt>            rtc.callback(rtc.context, status);
    <#lt>        }
	<#lt>}
</#if>	
#ifdef __cplusplus // Provide C++ Compatibility
 }
#endif

#endif