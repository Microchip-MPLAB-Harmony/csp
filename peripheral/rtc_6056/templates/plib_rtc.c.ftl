/*******************************************************************************
  RTC Peripheral Library

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${RTC_INSTANCE_NAME?lower_case}.c

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
#include "plib_${RTC_INSTANCE_NAME?lower_case}.h"

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

<#if rtcEnableInterrupt == true>
    <#lt>RTC_OBJECT rtc;
</#if>

void ${RTC_INSTANCE_NAME}_Initialize( void )
{
    ${RTC_INSTANCE_NAME}_REGS->RTC_MR = RTC_MR_TPERIOD_${RTC_MR_TPERIOD?right_pad(12)}  // output pulse period
                    | RTC_MR_THIGH_${RTC_MR_THIGH?right_pad(13)}    // output pulse duration
                    | RTC_MR_OUT1_${RTC_MR_OUT1?right_pad(12)}      // ADC last channel trigger event source
                    | RTC_MR_OUT0_${RTC_MR_OUT0?right_pad(12)}      // ADC all channels trigger event source
                    <#lt><#if RTC_MR_UTC?? >
                        <#lt><#if RTC_MR_UTC == true>
                            <#lt>                    | RTC_MR_UTC( 1 )
                        <#lt><#else>
                            <#lt>                    | RTC_MR_UTC( 0 )
                        <#lt></#if>
                    <#lt></#if>
                    | RTC_MR_PERSIAN( 0 )
                    <#lt><#if RTC_12HR_MODE == true>
                        <#lt>                    | RTC_MR_HRMOD( 1 )             // 12 hour mode
                    <#lt><#else>
                        <#lt>                    | RTC_MR_HRMOD( 0 )             // 24 hour mode
                    <#lt></#if>
                    ;   // no HIGH ppm correction, no slow clock correction, no negative ppm correction

    ${RTC_INSTANCE_NAME}_REGS->RTC_CR = RTC_CR_TIMEVSEL_${RTC_CR_TIMEVSEL} | RTC_CR_CALEVSEL_${RTC_CR_CALEVSEL};

    ${RTC_INSTANCE_NAME}_REGS->RTC_IDR = RTC_IDR_Msk;                // disable all interrupts
    ${RTC_INSTANCE_NAME}_REGS->RTC_SCCR = RTC_SCCR_Msk;              // clear any stale interrupts
}

bool ${RTC_INSTANCE_NAME}_TimeSet( struct tm * Time )
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
    ${RTC_INSTANCE_NAME}_REGS->RTC_CR &= ~(RTC_CR_UPDCAL_Msk | RTC_CR_UPDTIM_Msk);
    ${RTC_INSTANCE_NAME}_REGS->RTC_SCCR = RTC_SCCR_CALCLR_Msk;

    while( (${RTC_INSTANCE_NAME}_REGS->RTC_SR & RTC_SR_SEC_Msk) != RTC_SR_SEC_Msk )
    {
        ;   // spin lock
    }

    /* request RTC Configuration */
    ${RTC_INSTANCE_NAME}_REGS->RTC_CR |= RTC_CR_UPDCAL_Msk | RTC_CR_UPDTIM_Msk;
    // Wait for ack
    while( !(${RTC_INSTANCE_NAME}_REGS->RTC_SR & RTC_SR_ACKUPD_Msk) ) 
    {
        ;   // spin lock
    }

    // clear ack flag
    ${RTC_INSTANCE_NAME}_REGS->RTC_SCCR |= RTC_SCCR_ACKCLR_Msk | RTC_SCCR_ALRCLR_Msk | RTC_SCCR_TIMCLR_Msk;
    ${RTC_INSTANCE_NAME}_REGS->RTC_CALR = data_cal;
    ${RTC_INSTANCE_NAME}_REGS->RTC_TIMR = data_time;
    ${RTC_INSTANCE_NAME}_REGS->RTC_CR &= ~(RTC_CR_UPDCAL_Msk | RTC_CR_UPDTIM_Msk);
    if( ${RTC_INSTANCE_NAME}_REGS->RTC_VER & (RTC_VER_NVTIM_Msk | RTC_VER_NVCAL_Msk) ) 
    {
        retval = false;     // valid entry register indicates a problem
    }

    return retval;
}

void ${RTC_INSTANCE_NAME}_TimeGet( struct tm * Time )
{
    // two sequential read should be the same to insure syncrhonization  
    uint32_t data_time = ${RTC_INSTANCE_NAME}_REGS->RTC_TIMR;
    while( data_time != ${RTC_INSTANCE_NAME}_REGS->RTC_TIMR ) 
    {
        data_time = ${RTC_INSTANCE_NAME}_REGS->RTC_TIMR;
    }

    // two sequential read should be the same to insure synchronization  
    uint32_t data_cal = ${RTC_INSTANCE_NAME}_REGS->RTC_CALR;
    while( data_cal != ${RTC_INSTANCE_NAME}_REGS->RTC_CALR ) 
    {
        data_cal = ${RTC_INSTANCE_NAME}_REGS->RTC_CALR;
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

<#if rtcEnableInterrupt == true>
    <#lt>bool ${RTC_INSTANCE_NAME}_AlarmSet( struct tm * Time, RTC_ALARM_MASK mask )
    <#lt>{
    <#lt>    bool       retval = true;
    <#lt>    uint32_t   alarm_cal;
    <#lt>    uint32_t   alarm_tmr;    
    <#lt>    uint32_t   data_cal =  (decimaltobcd(Time->tm_mon + 1)<<16)
    <#lt>                           | (decimaltobcd(Time->tm_mday)<<24)
    <#lt>                           ;
    <#lt>    uint32_t   data_time = (decimaltobcd(Time->tm_sec)) 
    <#lt>                           | (decimaltobcd(Time->tm_min) << 8)
    <#lt>                           | (decimaltobcd(Time->tm_hour)<< 16)
    <#lt>                           ;
    <#lt>
    <#lt>    alarm_tmr = ${RTC_INSTANCE_NAME}_REGS->RTC_TIMALR;
    <#lt>    alarm_tmr = (mask & 0x04) << 21 | (mask & 0x02) << 14 | (mask & 0x01) << 7;
    <#lt>    ${RTC_INSTANCE_NAME}_REGS->RTC_TIMALR = data_time;
    <#lt>    ${RTC_INSTANCE_NAME}_REGS->RTC_TIMALR |= alarm_tmr;

    <#lt>    alarm_cal = ${RTC_INSTANCE_NAME}_REGS->RTC_CALALR;
    <#lt>    alarm_cal = (mask & 0x10) << 19 | (mask & 0x08) << 28;
    <#lt>    ${RTC_INSTANCE_NAME}_REGS->RTC_CALALR = data_cal;
    <#lt>    ${RTC_INSTANCE_NAME}_REGS->RTC_CALALR |= alarm_cal;

    <#lt>    if( ${RTC_INSTANCE_NAME}_REGS->RTC_VER & (RTC_VER_NVTIMALR_Msk | RTC_VER_NVCALALR_Msk) ) 
    <#lt>    {
    <#lt>        retval = false;        // valid entry register indicates a problem
    <#lt>    }
    <#lt>    else 
    <#lt>    {
    <#lt>        ${RTC_INSTANCE_NAME}_REGS->RTC_IER = RTC_IER_ALREN_Msk;
    <#lt>    }

    <#lt>    return retval;
    <#lt>}
        
    <#lt>void ${RTC_INSTANCE_NAME}_InterruptEnable( RTC_INT_MASK interrupt )
    <#lt>{
    <#lt>    ${RTC_INSTANCE_NAME}_REGS->RTC_IER = interrupt;
    <#lt>}

    <#lt>void ${RTC_INSTANCE_NAME}_InterruptDisable( RTC_INT_MASK interrupt )
    <#lt>{
    <#lt>    ${RTC_INSTANCE_NAME}_REGS->RTC_IDR = interrupt;
    <#lt>}

    <#lt>void ${RTC_INSTANCE_NAME}_CallbackRegister( RTC_CALLBACK callback, uintptr_t context )
    <#lt>{
    <#lt>    rtc.callback = callback;
    <#lt>    rtc.context = context;
    <#lt>}
</#if>

<#if rtcEnableInterrupt == true>
    <#lt>void ${RTC_INSTANCE_NAME}_InterruptHandler( void )
    <#lt>{
    <#lt>    // This handler may be chained with other sys control interrupts.  So 
    <#lt>    // the user call back should only occur if an RTC stimulus is present.
    <#lt>    volatile uint32_t status = ${RTC_INSTANCE_NAME}_REGS->RTC_SR;
    <#lt>    uint32_t enabledInterrupts = ${RTC_INSTANCE_NAME}_REGS->RTC_IMR;

    <#lt>    if( status & enabledInterrupts ) 
    <#lt>    {
    <#lt>        ${RTC_INSTANCE_NAME}_REGS->RTC_SCCR |= enabledInterrupts;
    <#lt>        if( rtc.callback != NULL ) 
    <#lt>        {
    <#lt>            rtc.callback( status, rtc.context );
    <#lt>        }
    <#lt>    }
    <#lt>}
</#if>    
