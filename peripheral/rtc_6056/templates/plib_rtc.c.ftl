/*******************************************************************************
  RTC Peripheral Library

  Company:
    Microchip Technology Inc.

  File Name:
    plib_rtc.c

  Summary:
    RTC Source File

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

#include "plib_rtc.h"

#define decimaltobcd(x)					(((x/10)<<4)+((x - ((x/10)*10))))
#define bcdtodecimal(x)					((x & 0xF0) >> 4) * 10 + (x & 0x0F)

void RTC_Initialize( void )
{
	_RTC_REGS->RTC_MR.w = RTC_MR_${RTC_MR_OUT0}_Msk | RTC_MR_${RTC_MR_OUT1}_Msk | RTC_MR_${RTC_MR_THIGH}_Msk | RTC_MR_${RTC_MR_TPERIOD}_Msk;
	_RTC_REGS->RTC_CR.w = RTC_CR_${RTC_CR_TIMEVSEL}_Msk | RTC_CR_${RTC_CR_CALEVSEL}_Msk;
}

void RTC_TimeSet( struct tm *Time )
{
	uint32_t data_cal =  (decimaltobcd(Time->tm_year / 100)) | \
			 (decimaltobcd((Time->tm_year - ((Time->tm_year/100)*100)))<< 8) | \
			   (decimaltobcd(Time->tm_mon)<<16)| \
			 (decimaltobcd(Time->tm_mday)<<24) | \
			 (decimaltobcd(Time->tm_wday)<<21);
	uint32_t data_time = (decimaltobcd(Time->tm_sec)) | (decimaltobcd(Time->tm_min) << 8) | (decimaltobcd(Time->tm_hour)<< 16);
		    _RTC_REGS->RTC_SCCR.w = (1<<2) ;
	while (_RTC_REGS->RTC_SR.SEC != true );
		    /* - request RTC Configuration */
	_RTC_REGS->RTC_CR.w |= (RTC_CR_UPDCAL_Msk) | RTC_CR_UPDTIM_Msk;
		    /* - Wait for ack */
	while (!(_RTC_REGS->RTC_SR.w & RTC_SR_ACKUPD_Msk));
		    /* - Clear ACK flag */
	_RTC_REGS->RTC_SCCR.w |= RTC_SCCR_ACKCLR_Msk;
	_RTC_REGS->RTC_CALR.w = data_cal;
	_RTC_REGS->RTC_TIMR.w = data_time;
	_RTC_REGS->RTC_CR.w &= ~(RTC_CR_UPDCAL_Msk|RTC_CR_UPDTIM_Msk);	
}
void RTC_TimeGet( struct tm *Time )
{
	uint32_t data_time = _RTC_REGS->RTC_TIMR.w;
	uint32_t data_cal  = _RTC_REGS->RTC_CALR.w;
	
	Time->tm_hour = bcdtodecimal((data_time & 0x003f0000) >> 16);
	Time->tm_sec = bcdtodecimal(data_time & 0x0000007f);
	Time->tm_min = bcdtodecimal((data_time & 0x00007f00)>>8);
	Time->tm_mday = bcdtodecimal((data_cal & 0x3f000000)>>24);
	Time->tm_wday = bcdtodecimal((data_cal & 0x00E00000)>>21);
	Time->tm_mon =  bcdtodecimal((data_cal & 0x001F0000)>>16);
	Time->tm_year = 100 * (bcdtodecimal((data_cal & 0x0000007f))) + bcdtodecimal((data_cal & 0x0000ff00)>>8);
	
	
}
<#if rtcEnableInterrupt == true>
	<#lt>void RTC_AlarmSet( struct tm *Time, RTC_ALARM_MASK mask )
	<#lt>{
	<#lt>	uint32_t alarm_cal;
	<#lt>	uint32_t alarm_tmr;	
	<#lt>	uint32_t data_cal =		(decimaltobcd(Time->tm_mon)<<16)| \
	<#lt>									(decimaltobcd(Time->tm_mday)<<24) ;
	<#lt>	uint32_t data_time = (decimaltobcd(Time->tm_sec)) | (decimaltobcd(Time->tm_min) << 8) \
									| (decimaltobcd(Time->tm_hour)<< 16);
	<#lt>	alarm_tmr = _RTC_REGS->RTC_TIMALR.w;
	<#lt>	_RTC_REGS->RTC_TIMALR.w = data_time;
	<#lt>	alarm_cal = _RTC_REGS->RTC_CALALR.w;
	<#lt>	_RTC_REGS->RTC_CALALR.w = data_cal;
	<#lt>	alarm_cal = (mask & 0x10) << 19 | (mask & 0x08) << 28;
	<#lt>	alarm_tmr = (mask & 0x04) << 21 | (mask & 0x02) << 14 | (mask & 0x01) << 7;
	  
	<#lt>	_RTC_REGS->RTC_TIMALR.w |= alarm_tmr;
	<#lt>	_RTC_REGS->RTC_CALALR.w |= alarm_cal;
	<#lt>	_RTC_REGS->RTC_IER.w |= RTC_IER_ALREN_Msk;
	<#lt>}

	<#lt>void RTC_ALARM_CALLBACKRegister( RTC_ALARM_CALLBACK callback, uintptr_t context )
	<#lt>{
	<#lt>	RTC.callback = callback;
	<#lt>	RTC.context = context;
	<#lt>}
</#if>