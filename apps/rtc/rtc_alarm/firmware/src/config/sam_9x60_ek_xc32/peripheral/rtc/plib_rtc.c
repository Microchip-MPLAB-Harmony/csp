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

#include "device.h"
#include "plib_rtc.h"

__STATIC_INLINE uint32_t
decimaltobcd( uint32_t aDecValue )
{
    uint32_t  decValueDiv10 = aDecValue / 10;
    return( (decValueDiv10 << 4) + ( aDecValue - (decValueDiv10 * 10) ) );
}

__STATIC_INLINE uint32_t
bcdtodecimal( uint32_t aBcdValue )
{
    return( (10 * ((aBcdValue & 0xF0) >> 4)) + (aBcdValue & 0x0F) );
}

RTC_OBJECT rtc;

void RTC_Initialize( void )
{
    RTC_REGS->RTC_MR = RTC_MR_TPERIOD_P_1S          // output pulse period
                    | RTC_MR_THIGH_H_31MS           // output pulse duration
                    | RTC_MR_OUT1_NO_WAVE           // ADC last channel trigger event source
                    | RTC_MR_OUT0_NO_WAVE           // ADC all channels trigger event source
                    | RTC_MR_UTC( 0 )
                    | RTC_MR_PERSIAN( 0 )
                    | RTC_MR_HRMOD( 0 )             // 24 hour mode
                    ;   // no HIGH ppm correction, no slow clock correction, no negative ppm correction

    RTC_REGS->RTC_CR = RTC_CR_TIMEVSEL_MINUTE | RTC_CR_CALEVSEL_WEEK;

    RTC_REGS->RTC_IDR = RTC_IDR_Msk;                // disable all interrupts
    RTC_REGS->RTC_SCCR = RTC_SCCR_Msk;              // clear any stale interrupts
}

bool RTC_TimeSet( struct tm * Time )
{
    bool retval = true;
    Time->tm_year += 1900;
    uint32_t data_cal =   (decimaltobcd( Time->tm_mday ) << RTC_CALR_DATE_Pos)
                        | (decimaltobcd( Time->tm_wday + 1 ) << RTC_CALR_DAY_Pos)
                        | (decimaltobcd( Time->tm_mon + 1 ) << RTC_CALR_MONTH_Pos)
                        | (decimaltobcd( Time->tm_year - ( (Time->tm_year/100) * 100 ) ) << RTC_CALR_YEAR_Pos)
                        | (decimaltobcd( Time->tm_year/100 ) << RTC_CALR_CENT_Pos)
                        ;
    uint32_t data_time =  (decimaltobcd( Time->tm_hour ) << RTC_TIMR_HOUR_Pos ) 
                        | (decimaltobcd( Time->tm_min )  << RTC_TIMR_MIN_Pos)
                        | (decimaltobcd( Time->tm_sec )  << RTC_TIMR_SEC_Pos)
                        ;
    RTC_REGS->RTC_CR &= ~(RTC_CR_UPDCAL_Msk | RTC_CR_UPDTIM_Msk);
    RTC_REGS->RTC_SCCR = RTC_SCCR_CALCLR_Msk;

    while( (RTC_REGS->RTC_SR & RTC_SR_SEC_Msk) != RTC_SR_SEC_Msk )
    {
        ;   // spin lock
    }

    /* request RTC Configuration */
    RTC_REGS->RTC_CR |= RTC_CR_UPDCAL_Msk | RTC_CR_UPDTIM_Msk;
    // Wait for ack
    while( !(RTC_REGS->RTC_SR & RTC_SR_ACKUPD_Msk) ) 
    {
        ;   // spin lock
    }

    // clear ack flag
    RTC_REGS->RTC_SCCR |= RTC_SCCR_ACKCLR_Msk | RTC_SCCR_ALRCLR_Msk | RTC_SCCR_TIMCLR_Msk;
    RTC_REGS->RTC_CALR = data_cal;
    RTC_REGS->RTC_TIMR = data_time;
    RTC_REGS->RTC_CR &= ~(RTC_CR_UPDCAL_Msk | RTC_CR_UPDTIM_Msk);
    if( RTC_REGS->RTC_VER & (RTC_VER_NVTIM_Msk | RTC_VER_NVCAL_Msk) ) 
    {
        retval = false;     // valid entry register indicates a problem
    }

    return retval;
}

void RTC_TimeGet( struct tm * Time )
{
    // two sequential read should be the same to insure syncrhonization  
    uint32_t data_time = RTC_REGS->RTC_TIMR;
    while( data_time != RTC_REGS->RTC_TIMR ) 
    {
        data_time = RTC_REGS->RTC_TIMR;
    }

    // two sequential read should be the same to insure synchronization  
    uint32_t data_cal = RTC_REGS->RTC_CALR;
    while( data_cal != RTC_REGS->RTC_CALR ) 
    {
        data_cal = RTC_REGS->RTC_CALR;
    }

    Time->tm_hour = bcdtodecimal( (data_time & RTC_TIMR_HOUR_Msk) >> RTC_TIMR_HOUR_Pos );
    Time->tm_sec =  bcdtodecimal( data_time & RTC_TIMR_SEC_Msk );
    Time->tm_min =  bcdtodecimal( (data_time & RTC_TIMR_MIN_Msk) >> RTC_TIMR_MIN_Pos );
    Time->tm_mday = bcdtodecimal( (data_cal & RTC_CALR_DATE_Msk) >> RTC_CALR_DATE_Pos );
    Time->tm_wday = bcdtodecimal( (data_cal & RTC_CALR_DAY_Msk) >> RTC_CALR_DAY_Pos ) - 1;
    Time->tm_mon =  bcdtodecimal( (data_cal & RTC_CALR_MONTH_Msk) >> RTC_CALR_MONTH_Pos ) - 1;
    Time->tm_year = (   (100 * bcdtodecimal( data_cal & RTC_CALR_CENT_Msk ))
                        + bcdtodecimal( (data_cal & RTC_CALR_YEAR_Msk) >> RTC_CALR_YEAR_Pos )
                    ) - 1900
                    ;    
}

bool RTC_AlarmSet( struct tm * Time, RTC_ALARM_MASK mask )
{
    bool       retval = true;
    uint32_t   alarm_cal;
    uint32_t   alarm_tmr;    
    uint32_t   data_cal =  (decimaltobcd(Time->tm_mon + 1)<<16)
                           | (decimaltobcd(Time->tm_mday)<<24)
                           ;
    uint32_t   data_time = (decimaltobcd(Time->tm_sec)) 
                           | (decimaltobcd(Time->tm_min) << 8)
                           | (decimaltobcd(Time->tm_hour)<< 16)
                           ;
    alarm_tmr = RTC_REGS->RTC_TIMALR;
    alarm_tmr = (mask & 0x04) << 21 | (mask & 0x02) << 14 | (mask & 0x01) << 7;
    RTC_REGS->RTC_TIMALR = data_time;
    RTC_REGS->RTC_TIMALR |= alarm_tmr;

    alarm_cal = RTC_REGS->RTC_CALALR;
    alarm_cal = (mask & 0x10) << 19 | (mask & 0x08) << 28;
    RTC_REGS->RTC_CALALR = data_cal;
    RTC_REGS->RTC_CALALR |= alarm_cal;

    if( RTC_REGS->RTC_VER & (RTC_VER_NVTIMALR_Msk | RTC_VER_NVCALALR_Msk) ) 
    {
        retval = false;        // valid entry register indicates a problem
    }
    else 
    {
        RTC_REGS->RTC_IER = RTC_IER_ALREN_Msk;
    }

    return retval;
}
        
void RTC_InterruptEnable( RTC_INT_MASK interrupt )
{
    RTC_REGS->RTC_IER = interrupt;
}

void RTC_InterruptDisable( RTC_INT_MASK interrupt )
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
    // This handler may be chained with other sys control interrupts.  So 
    // the user call back should only occur if an RTC stimulus is present.
    volatile uint32_t status = RTC_REGS->RTC_SR;
    uint32_t enabledInterrupts = RTC_REGS->RTC_IMR;

    if( status & enabledInterrupts ) 
    {
        RTC_REGS->RTC_SCCR |= enabledInterrupts;
        if( rtc.callback != NULL ) 
        {
            rtc.callback( status, rtc.context );
        }
    }
}
