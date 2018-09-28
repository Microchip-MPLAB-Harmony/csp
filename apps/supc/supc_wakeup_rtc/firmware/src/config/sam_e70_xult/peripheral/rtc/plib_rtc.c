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

#include "device.h"
#include "plib_rtc.h"

#define decimaltobcd(x)					(((x/10)<<4)+((x - ((x/10)*10))))
#define bcdtodecimal(x)					((x & 0xF0) >> 4) * 10 + (x & 0x0F)

RTC_OBJECT rtc;

void RTC_Initialize( void )
{
	RTC_REGS->RTC_MR = RTC_MR_OUT0_ALARM_FLAG | RTC_MR_OUT1_NO_WAVE | RTC_MR_THIGH_H_31MS | RTC_MR_TPERIOD_P_1S;
	RTC_REGS->RTC_CR = RTC_CR_TIMEVSEL_MINUTE | RTC_CR_CALEVSEL_WEEK;
}

bool RTC_TimeSet( struct tm *Time )
{
	Time->tm_year += 1900;
	uint32_t data_cal =  (decimaltobcd(Time->tm_year / 100)) | \
			 (decimaltobcd((Time->tm_year - ((Time->tm_year/100)*100)))<< RTC_CALR_YEAR_Pos) | \
			   (decimaltobcd((Time->tm_mon + 1))<<RTC_CALR_MONTH_Pos)| \
			 (decimaltobcd(Time->tm_mday)<<RTC_CALR_DATE_Pos) | \
			 ((Time->tm_wday + 1) << RTC_CALR_DAY_Pos);
	uint32_t data_time = (decimaltobcd(Time->tm_sec)) | (decimaltobcd(Time->tm_min) << RTC_TIMR_MIN_Pos) | (decimaltobcd(Time->tm_hour)<< RTC_TIMR_HOUR_Pos);
	RTC_REGS->RTC_CR&= ~(RTC_CR_UPDCAL_Msk|RTC_CR_UPDTIM_Msk);
	RTC_REGS->RTC_SCCR = (1<<2) ;
	while ((RTC_REGS->RTC_SR& RTC_SR_SEC_Msk) != RTC_SR_SEC_Msk );
		    /* - request RTC Configuration */
	RTC_REGS->RTC_CR|= (RTC_CR_UPDCAL_Msk) | RTC_CR_UPDTIM_Msk;
		    /* - Wait for ack */
	while (!((RTC_REGS->RTC_SR) & (RTC_SR_ACKUPD_Msk)));
		    /* - Clear ACK flag */
	RTC_REGS->RTC_SCCR|= RTC_SCCR_ACKCLR_Msk | RTC_SCCR_ALRCLR_Msk | RTC_SCCR_TIMCLR_Msk;
	RTC_REGS->RTC_CALR = data_cal;
	RTC_REGS->RTC_TIMR = data_time;
	RTC_REGS->RTC_CR&= ~(RTC_CR_UPDCAL_Msk|RTC_CR_UPDTIM_Msk);
	if(RTC_REGS->RTC_VER& 0x3)
	{
		return false;
	}
	
	return true;
}

void RTC_TimeGet( struct tm *Time )
{
	uint32_t data_time = RTC_REGS->RTC_TIMR;
	while (data_time != RTC_REGS->RTC_TIMR) 
	{
		data_time = RTC_REGS->RTC_TIMR;
	}
	uint32_t data_cal  = RTC_REGS->RTC_CALR;
	while (data_cal != RTC_REGS->RTC_CALR) 
	{
		data_cal = RTC_REGS->RTC_CALR;
	}
	
	Time->tm_hour = bcdtodecimal((data_time & RTC_TIMR_HOUR_Msk) >> RTC_TIMR_HOUR_Pos);
	Time->tm_sec = bcdtodecimal(data_time & RTC_TIMR_SEC_Msk);
	Time->tm_min = bcdtodecimal((data_time & RTC_TIMR_MIN_Msk)>>RTC_TIMR_MIN_Pos);
	Time->tm_mday = bcdtodecimal((data_cal & RTC_CALR_DATE_Msk)>>RTC_CALR_DATE_Pos);
	Time->tm_wday = (bcdtodecimal((data_cal & RTC_CALR_DAY_Msk)>>RTC_CALR_DAY_Pos)) - 1;
	Time->tm_mon =  (bcdtodecimal((data_cal & RTC_CALR_MONTH_Msk)>>RTC_CALR_MONTH_Pos)) - 1;
	Time->tm_year = (100 * (bcdtodecimal((data_cal & RTC_CALR_CENT_Msk))) \
            + bcdtodecimal((data_cal & RTC_CALR_YEAR_Msk)>>RTC_CALR_YEAR_Pos)) - 1900;	
}

bool RTC_AlarmSet( struct tm *Time, RTC_ALARM_MASK mask )
{
	uint32_t alarm_cal;
	uint32_t alarm_tmr;	
	uint32_t data_cal =		(decimaltobcd(Time->tm_mon + 1)<<16)| \
									(decimaltobcd(Time->tm_mday)<<24) ;
	uint32_t data_time = (decimaltobcd(Time->tm_sec)) | (decimaltobcd(Time->tm_min) << 8) \
								| (decimaltobcd(Time->tm_hour)<< 16);
	alarm_tmr = RTC_REGS->RTC_TIMALR;
	RTC_REGS->RTC_TIMALR = data_time;
	alarm_cal = RTC_REGS->RTC_CALALR;
	RTC_REGS->RTC_CALALR = data_cal;
	alarm_cal = (mask & 0x10) << 19 | (mask & 0x08) << 28;
	alarm_tmr = (mask & 0x04) << 21 | (mask & 0x02) << 14 | (mask & 0x01) << 7;
	RTC_REGS->RTC_TIMALR|= alarm_tmr;
	RTC_REGS->RTC_CALALR|= alarm_cal;
	if(RTC_REGS->RTC_VER& 0xC)
	{
		return false;
	}
	RTC_REGS->RTC_IER = RTC_IER_ALREN_Msk;
	return true;
}
		
void RTC_InterruptEnable(RTC_INT_MASK interrupt)
{
	RTC_REGS->RTC_IER = interrupt;
}

void RTC_InterruptDisable(RTC_INT_MASK interrupt)
{
	RTC_REGS->RTC_IDR = interrupt;
}

void RTC_CallbackRegister( RTC_CALLBACK callback, uintptr_t context )
{
	rtc.callback = callback;
	rtc.context = context;
}

void RTC_InterruptHandler( void )
{
	volatile uint32_t status = RTC_REGS->RTC_SR;
	RTC_REGS->RTC_SCCR|= RTC_SCCR_ALRCLR_Msk | RTC_SCCR_TIMCLR_Msk |  RTC_SCCR_CALCLR_Msk;
	if(rtc.callback != NULL)
   {
   	rtc.callback(rtc.context, status);
   }
}
