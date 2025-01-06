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
<#if core.CoreSysIntFile == true>
#include "interrupts.h"
</#if>

<#if rtcEnableInterrupt == true>
static volatile RTC_OBJECT rtc;
</#if>

__STATIC_INLINE uint32_t decimaltobcd( uint32_t aDecValue )
{
    uint32_t  decValueDiv10 = aDecValue / 10U;

    return( (decValueDiv10 << 4U) + ( aDecValue - (decValueDiv10 * 10U) ) );
}

__STATIC_INLINE uint32_t bcdtodecimal( uint32_t aBcdValue )
{
    return( (10U * ((aBcdValue & 0xF0U) >> 4U)) + (aBcdValue & 0x0FU) );
}

void ${RTC_INSTANCE_NAME}_Initialize( void )
{
    <@compress single_line=true>${RTC_INSTANCE_NAME}_REGS->RTC_MR = RTC_MR_OUT1_${RTC_MR_OUT1} | RTC_MR_OUT0_${RTC_MR_OUT0}
                                                                   <#if RTC_MR_TPERIOD??>| RTC_MR_TPERIOD_${RTC_MR_TPERIOD}</#if>
                                                                   <#if RTC_MR_THIGH??>| RTC_MR_THIGH_${RTC_MR_THIGH}</#if>
                                                                   <#if RTC_MR_UTC??>| RTC_MR_UTC(${RTC_MR_UTC?then('1', '0')})</#if>
                                                                   | RTC_MR_HRMOD(${RTC_12HR_MODE?then('1', '0')}U);</@compress>

    ${RTC_INSTANCE_NAME}_REGS->RTC_CR = RTC_CR_TIMEVSEL_${RTC_CR_TIMEVSEL} | RTC_CR_CALEVSEL_${RTC_CR_CALEVSEL};

    // disable all interrupts
    ${RTC_INSTANCE_NAME}_REGS->RTC_IDR = RTC_IDR_Msk;

    // clear any stale interrupts
    ${RTC_INSTANCE_NAME}_REGS->RTC_SCCR = RTC_SCCR_Msk;
}

bool ${RTC_INSTANCE_NAME}_TimeSet( struct tm * sysTime )
{
    bool retval = true;
    sysTime->tm_year += 1900;
    uint32_t data_cal = (decimaltobcd((uint32_t)sysTime->tm_mday ) << RTC_CALR_DATE_Pos)
                        | (decimaltobcd(((uint32_t)sysTime->tm_wday + 1U )) << RTC_CALR_DAY_Pos)
                        | (decimaltobcd(((uint32_t)sysTime->tm_mon + 1U )) << RTC_CALR_MONTH_Pos)
                        | (decimaltobcd(((uint32_t)sysTime->tm_year - (((uint32_t)sysTime->tm_year/100U) * 100U ))) << RTC_CALR_YEAR_Pos)
                        | (decimaltobcd(((uint32_t)sysTime->tm_year/100U) ) << RTC_CALR_CENT_Pos);

    uint32_t data_time = (decimaltobcd((uint32_t)sysTime->tm_hour) << RTC_TIMR_HOUR_Pos )
                        | (decimaltobcd((uint32_t)sysTime->tm_min) << RTC_TIMR_MIN_Pos)
                        | (decimaltobcd((uint32_t)sysTime->tm_sec) << RTC_TIMR_SEC_Pos);

    ${RTC_INSTANCE_NAME}_REGS->RTC_CR &= ~(RTC_CR_UPDCAL_Msk | RTC_CR_UPDTIM_Msk);

    ${RTC_INSTANCE_NAME}_REGS->RTC_SCCR = RTC_SCCR_CALCLR_Msk;

    while( (${RTC_INSTANCE_NAME}_REGS->RTC_SR & RTC_SR_SEC_Msk) != RTC_SR_SEC_Msk )
    {
        ;   // spin lock
    }

    // request RTC Configuration
    ${RTC_INSTANCE_NAME}_REGS->RTC_CR |= RTC_CR_UPDCAL_Msk | RTC_CR_UPDTIM_Msk;

    // Wait for ack
    while( (${RTC_INSTANCE_NAME}_REGS->RTC_SR & RTC_SR_ACKUPD_Msk) == 0U )
    {
        ;   // spin lock
    }

    // clear ack flag
    ${RTC_INSTANCE_NAME}_REGS->RTC_SCCR |= RTC_SCCR_ACKCLR_Msk | RTC_SCCR_ALRCLR_Msk | RTC_SCCR_TIMCLR_Msk;
    ${RTC_INSTANCE_NAME}_REGS->RTC_CALR = data_cal;
    ${RTC_INSTANCE_NAME}_REGS->RTC_TIMR = data_time;
    ${RTC_INSTANCE_NAME}_REGS->RTC_CR &= ~(RTC_CR_UPDCAL_Msk | RTC_CR_UPDTIM_Msk);

    if( (${RTC_INSTANCE_NAME}_REGS->RTC_VER & (RTC_VER_NVTIM_Msk | RTC_VER_NVCAL_Msk)) != 0U )
    {
        retval = false;     // valid entry register indicates a problem
    }

    return retval;
}

void ${RTC_INSTANCE_NAME}_TimeGet( struct tm * sysTime )
{
    uint32_t temp;
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
    temp = bcdtodecimal( (data_time & RTC_TIMR_HOUR_Msk) >> RTC_TIMR_HOUR_Pos );
    sysTime->tm_hour = (int32_t)temp;
    temp = bcdtodecimal( data_time & RTC_TIMR_SEC_Msk );
    sysTime->tm_sec = (int32_t)temp;
    temp = bcdtodecimal( (data_time & RTC_TIMR_MIN_Msk) >> RTC_TIMR_MIN_Pos );
    sysTime->tm_min = (int32_t)temp;
    temp = bcdtodecimal( (data_cal & RTC_CALR_DATE_Msk) >> RTC_CALR_DATE_Pos );
    sysTime->tm_mday = (int32_t)temp;
    temp = bcdtodecimal( (data_cal & RTC_CALR_DAY_Msk) >> RTC_CALR_DAY_Pos ) - 1U;
    sysTime->tm_wday = (int32_t)temp;
    temp = bcdtodecimal( (data_cal & RTC_CALR_MONTH_Msk) >> RTC_CALR_MONTH_Pos ) - 1U;
    sysTime->tm_mon = (int32_t)temp;
    temp = (( (100U * bcdtodecimal( data_cal & RTC_CALR_CENT_Msk ))
                        + bcdtodecimal( (data_cal & RTC_CALR_YEAR_Msk) >> RTC_CALR_YEAR_Pos )
                    ) - 1900U);
    sysTime->tm_year = (int32_t)temp;
}

<#if rtcEnableInterrupt == true>
bool ${RTC_INSTANCE_NAME}_AlarmSet( struct tm * alarmTime, RTC_ALARM_MASK mask )
{
    bool     retval = true;
    volatile uint32_t temp;
    uint32_t alarm_cal;
    uint32_t alarm_tmr;
    uint32_t data_cal = (decimaltobcd(((uint32_t)alarmTime->tm_mon + 1U)) << 16U) | (decimaltobcd((uint32_t)alarmTime->tm_mday) << 24U);
    uint32_t data_time = (decimaltobcd((uint32_t)alarmTime->tm_sec)) | (decimaltobcd((uint32_t)alarmTime->tm_min) << 8U) | (decimaltobcd((uint32_t)alarmTime->tm_hour) << 16U);

    temp = ${RTC_INSTANCE_NAME}_REGS->RTC_TIMALR;
    (void)temp;
    alarm_tmr = (((uint32_t)mask & 0x04U) << 21) | (((uint32_t)mask & 0x02U) << 14) | (((uint32_t)mask & 0x01U) << 7);

    ${RTC_INSTANCE_NAME}_REGS->RTC_TIMALR = data_time;
    ${RTC_INSTANCE_NAME}_REGS->RTC_TIMALR |= alarm_tmr;

    temp = ${RTC_INSTANCE_NAME}_REGS->RTC_CALALR;
    (void)temp;
    alarm_cal = (((uint32_t)mask & 0x10U) << 19) | (((uint32_t)mask & 0x08U) << 28);

    ${RTC_INSTANCE_NAME}_REGS->RTC_CALALR = data_cal;
    ${RTC_INSTANCE_NAME}_REGS->RTC_CALALR |= alarm_cal;

    if( (${RTC_INSTANCE_NAME}_REGS->RTC_VER & (RTC_VER_NVTIMALR_Msk | RTC_VER_NVCALALR_Msk)) != 0U )
    {
        retval = false;        // valid entry register indicates a problem
    }
    else
    {
        ${RTC_INSTANCE_NAME}_REGS->RTC_IER = RTC_IER_ALREN_Msk;
    }

    return retval;
}

void ${RTC_INSTANCE_NAME}_InterruptEnable( RTC_INT_MASK interrupt )
{
    ${RTC_INSTANCE_NAME}_REGS->RTC_IER = (uint32_t)interrupt;
}

void ${RTC_INSTANCE_NAME}_InterruptDisable( RTC_INT_MASK interrupt )
{
    ${RTC_INSTANCE_NAME}_REGS->RTC_IDR = (uint32_t)interrupt;
}

void ${RTC_INSTANCE_NAME}_CallbackRegister( RTC_CALLBACK callback, uintptr_t context )
{
    rtc.callback = callback;

    rtc.context = context;
}

void __attribute__((used)) ${RTC_INSTANCE_NAME}_InterruptHandler( void )
{
    // This handler may be chained with other sys control interrupts. So
    // the user call back should only occur if an RTC stimulus is present.
    uint32_t rtc_status = ${RTC_INSTANCE_NAME}_REGS->RTC_SR;
    uint32_t enabledInterrupts = ${RTC_INSTANCE_NAME}_REGS->RTC_IMR;

    /* Additional temporary variable used to prevent MISRA violations (Rule 13.x) */
    uintptr_t context = rtc.context;

    if((rtc_status & enabledInterrupts) != 0U)
    {
        ${RTC_INSTANCE_NAME}_REGS->RTC_SCCR |= enabledInterrupts;

        if( rtc.callback != NULL)
        {
            rtc.callback(rtc_status, context);
        }
    }
}
</#if>
