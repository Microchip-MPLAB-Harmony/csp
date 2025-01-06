/*******************************************************************************
  Real Time Counter (${RTCC_INSTANCE_NAME}) PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${RTCC_INSTANCE_NAME?lower_case}.c

  Summary:
    ${RTCC_INSTANCE_NAME} PLIB Implementation file

  Description:
    This file defines the interface to the RTC peripheral library. This
    library provides access to and control of the associated peripheral
    instance in clock/calendar mode.

*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
* Copyright (C) 2019 Microchip Technology Inc. and its subsidiaries.
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
// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

#include "plib_${RTCC_INSTANCE_NAME?lower_case}.h"
<#if core.CoreSysIntFile == true>
#include "interrupts.h"
</#if>

// *****************************************************************************
// *****************************************************************************
// Section: Global Data
// *****************************************************************************
// *****************************************************************************

<#if RTCC_INTERRUPT_MODE == true>
/* Real Time Clock System Service Object */
typedef struct SYS_RTCC_OBJ_STRUCT
{
    /* Call back function for RTCC.*/
    RTCC_CALLBACK  callback;

    /* Client data (Event Context) that will be passed to callback */
    uintptr_t context;

} RTCC_OBJECT;

static volatile RTCC_OBJECT rtcc;

</#if>

// *****************************************************************************
// *****************************************************************************
// Section: Local functions
// *****************************************************************************
// *****************************************************************************
__STATIC_INLINE uint32_t decimaltobcd( uint32_t aDecValue )
{
    uint32_t  decValueDiv10 = aDecValue / 10U;

    return( (decValueDiv10 << 4U) + ( aDecValue - (decValueDiv10 * 10U) ) );
}

__STATIC_INLINE uint32_t bcdtodecimal( uint32_t aBcdValue )
{
    return( (10U * ((aBcdValue & 0xF0U) >> 4U)) + (aBcdValue & 0x0FU) );
}

// *****************************************************************************
// *****************************************************************************
// Section: ${RTCC_INSTANCE_NAME} Implementation
// *****************************************************************************
// *****************************************************************************

void ${RTCC_INSTANCE_NAME}_Initialize( void )
{
    /* Unlock System */
    SYSKEY = 0x00000000;
    SYSKEY = 0xAA996655U;
    SYSKEY = 0x556699AA;
    RTCCON1CLR = _RTCCON1_WRLOCK_MASK;  /* Enable writes to RTCC */

    /* Lock System */
    SYSKEY = 0x00000000;
    <#if RTCC_OUTPUT_ENABLE == true>
    /* Select output to be placed on output pin */
    RTCCON1bits.OUTSEL = ${RTCC_OUTPUT_SELECT};
    RTCCON1SET = _RTCCON1_RTCOE_MASK;  /* Enable RTCC output */
    <#else>
    RTCCON1CLR = _RTCCON1_RTCOE_MASK;  /* Disable RTCC output */
    </#if>

    /* Set RTCC clock configuration */
    RTCCON2 = 0x${RTCCON2_REG_VALUE};

    <#if RTC_TIMEANDDATE == true>
        <#lt>    RTCCON1CLR = _RTCCON1_ON_MASK;   /* Disable clock to RTCC */
        <#lt>    while((RTCCON1bits.ON) != 0U)  /* Wait for clock to stop */
        <#lt>    {
        <#lt>       /* Do Nothing */
        <#lt>    }

        <#lt>    RTCTIME = 0x${RTCTIME_TIME}00;   /* Set RTCC time */
        <#lt>    RTCDATE = 0x${RTCTIME_DATE}0${RTCTIME_WEEKDAY};  /* Set RTCC date */
    </#if>

    <#if RTCC_ALARM_REPEAT_FOREVER == true>
        <#lt>    RTCCON1SET = _RTCCON1_CHIME_MASK;  /* Set alarm to repeat forever */
    <#else>
        <#lt>    /* Set alarm to repeat finite number of times */
        <#lt>    RTCCON1CLR = _RTCCON1_CHIME_MASK;
        <#lt>    RTCCON1bits.ALMRPT = ${RTCALRM_ARPT};
    </#if>

    <#if RTC_ALARM == true>
        <#lt>    RTCCON1CLR = _RTCCON1_ALRMEN_MASK;  /* Disable alarm */
        <#lt>    while((RTCSTATbits.ALMSYNC) != 0U)  /* Wait for disable */
        <#lt>    {
        <#lt>       /* Do Nothing */
        <#lt>    }

        <#lt>    ALMTIME = 0x${RTCALRM_TIME}00;   /* Set alarm time */
        <#lt>    ALMDATE = 0x00${RTCALRM_DATE}0${RTCALRM_DAY};   /* Set alarm date */
        <#lt>    RTCCON1bits.AMASK = ${RTCC_ALARM_MASK}; /* Set alarm frequency */

        <#if RTCC_INTERRUPT_MODE == true>
            <#lt>    ${RTCC_IEC_REG}SET = (uint32_t)RTCC_INT_ALARM; /* Enable RTC Alarma interrupt */
        </#if>

        <#lt>    RTCCON1SET = _RTCCON1_ALRMEN_MASK;  /* Enable the alarm */
    </#if>

    /* start the RTC */
    RTCCON1SET = _RTCCON1_ON_MASK;
}

<#if RTCC_INTERRUPT_MODE == true>
void ${RTCC_INSTANCE_NAME}_InterruptEnable( RTCC_INT_MASK interrupt )
{
    ${RTCC_IEC_REG}SET = (uint32_t)interrupt;
}

void ${RTCC_INSTANCE_NAME}_InterruptDisable( RTCC_INT_MASK interrupt )
{
    ${RTCC_IEC_REG}CLR = (uint32_t)interrupt;
}

</#if>
bool ${RTCC_INSTANCE_NAME}_TimeSet( struct tm *Time )
{
    uint32_t timeField = 0, dateField = 0;

    timeField = (decimaltobcd((uint32_t)Time->tm_hour) << _RTCTIME_HRONE_POSITION) & (_RTCTIME_HRTEN_MASK | _RTCTIME_HRONE_MASK);
    timeField |= (decimaltobcd((uint32_t)Time->tm_min) << _RTCTIME_MINONE_POSITION) & (_RTCTIME_MINTEN_MASK | _RTCTIME_MINONE_MASK);
    timeField |= (decimaltobcd((uint32_t)Time->tm_sec) << _RTCTIME_SECONE_POSITION) & (_RTCTIME_SECTEN_MASK | _RTCTIME_SECONE_MASK);

    while((RTCSTAT & _RTCSTAT_SYNC_MASK) != 0U)
    {
        /* Wait for synchronization */
    }

    RTCTIME = timeField;

    dateField = (decimaltobcd((uint32_t)Time->tm_year % 100U) << _RTCDATE_YRONE_POSITION) & (_RTCDATE_YRONE_MASK | _RTCDATE_YRTEN_MASK);
    dateField |= (decimaltobcd(((uint32_t)Time->tm_mon + 1U)) << _RTCDATE_MTHONE_POSITION)&(_RTCDATE_MTHONE_MASK | _RTCDATE_MTHTEN_MASK);
    dateField |= (decimaltobcd((uint32_t)Time->tm_mday) << _RTCDATE_DAYONE_POSITION) & (_RTCDATE_DAYONE_MASK | _RTCDATE_DAYTEN_MASK);
    dateField |= decimaltobcd((uint32_t)Time->tm_wday) & _RTCDATE_WDAY_MASK;

    while((RTCSTAT & _RTCSTAT_SYNC_MASK) != 0U)
    {
        /* Wait for synchronization */
    }

    RTCDATE = dateField;

    RTCCON1SET = _RTCCON1_ON_MASK;  /* Start the RTCC module */

    return true;    /* This PLIB has no way of indicating wrong device operation so always return true */
}

void ${RTCC_INSTANCE_NAME}_TimeGet( struct tm  *Time )
{
    uint32_t dataTime, dataDate;
    uint32_t tmp;

    while((RTCSTAT & _RTCSTAT_SYNC_MASK) != 0U)
    {
        /* Wait for synchronization */
    }

    dataTime = RTCTIME;  /* read the time from the RTC */

    tmp = (10U * (bcdtodecimal((dataTime & _RTCTIME_HRTEN_MASK) >> _RTCTIME_HRTEN_POSITION)) +
                         (bcdtodecimal((dataTime & _RTCTIME_HRONE_MASK) >> _RTCTIME_HRONE_POSITION)));
    Time->tm_hour = (int)tmp;
    tmp = (10U * (bcdtodecimal((dataTime & _RTCTIME_MINTEN_MASK) >> _RTCTIME_MINTEN_POSITION)) +
                         (bcdtodecimal((dataTime & _RTCTIME_MINONE_MASK) >> _RTCTIME_MINONE_POSITION)));
    Time->tm_min = (int)tmp;
    tmp = (10U * (bcdtodecimal((dataTime & _RTCTIME_SECTEN_MASK) >> _RTCTIME_SECTEN_POSITION)) +
                         (bcdtodecimal((dataTime & _RTCTIME_SECONE_MASK) >> _RTCTIME_SECONE_POSITION)));
    Time->tm_sec = (int)tmp;

    while((RTCSTAT & _RTCSTAT_SYNC_MASK) != 0U)
    {
        /* Wait for synchronization */
    }

    dataDate = RTCDATE;  /* read the date from the RTC */

    tmp = (10U * (bcdtodecimal((dataDate & _RTCDATE_YRTEN_MASK) >> _RTCDATE_YRTEN_POSITION)) +
                         (bcdtodecimal((dataDate & _RTCDATE_YRONE_MASK) >> _RTCDATE_YRONE_POSITION)));
    tmp += 2000U; /* This RTC designed for 0-99 year range.  Need to add 2000 to that. */
    Time->tm_year = (int)tmp;

    tmp = (10U * (bcdtodecimal((dataDate & _RTCDATE_MTHTEN_MASK) >> _RTCDATE_MTHTEN_POSITION)) +
                         (bcdtodecimal((dataDate & _RTCDATE_MTHONE_MASK) >> _RTCDATE_MTHONE_POSITION))) - 1U;
    Time->tm_mon = (int)tmp;
    tmp = (10U * (bcdtodecimal((dataDate & _RTCDATE_DAYTEN_MASK) >> _RTCDATE_DAYTEN_POSITION)) +
                         (bcdtodecimal((dataDate & _RTCDATE_DAYONE_MASK) >> _RTCDATE_DAYONE_POSITION)));
    Time->tm_mday = (int)tmp;

    tmp = bcdtodecimal((dataDate & _RTCDATE_WDAY_MASK) >> _RTCDATE_WDAY_POSITION);
    Time->tm_wday = (int)tmp;
    Time->tm_yday = 0;  /* not used */
    Time->tm_isdst = 0;    /* not used */
}

bool ${RTCC_INSTANCE_NAME}_AlarmSet( struct tm *alarmTime, RTCC_ALARM_MASK alarmFreq )
{
    uint32_t dataDate, dataTime;

    <#if RTCC_INTERRUPT_MODE == true>
    /* Disable interrupt, if enabled, before setting up alarm */
    ${RTCC_INSTANCE_NAME}_InterruptDisable(RTCC_INT_ALARM);
    </#if>

    RTCCON1CLR = _RTCCON1_ALRMEN_MASK;  /* Disable alarm */
    while((RTCSTATbits.ALMSYNC) != 0U)
    {
        /* Wait for disable */
    }

    if(RTCC_ALARM_MASK_OFF != alarmFreq)
    {
        dataDate  = (decimaltobcd(((uint32_t)alarmTime->tm_mon + 1U)) << _RTCDATE_MTHONE_POSITION) & (_RTCDATE_MTHONE_MASK | _RTCDATE_MTHTEN_MASK);
        dataDate |= (decimaltobcd((uint32_t)alarmTime->tm_mday) << _RTCDATE_DAYONE_POSITION) & (_RTCDATE_DAYONE_MASK | _RTCDATE_DAYTEN_MASK);
        dataDate |= decimaltobcd((uint32_t)alarmTime->tm_wday) & _RTCDATE_WDAY_MASK;

        dataTime  = (decimaltobcd((uint32_t)alarmTime->tm_hour) << _RTCTIME_HRONE_POSITION) & (_RTCTIME_HRTEN_MASK | _RTCTIME_HRONE_MASK);
        dataTime |= (decimaltobcd((uint32_t)alarmTime->tm_min) << _RTCTIME_MINONE_POSITION) & (_RTCTIME_MINTEN_MASK | _RTCTIME_MINONE_MASK);
        dataTime |= (decimaltobcd((uint32_t)alarmTime->tm_sec) << _RTCTIME_SECONE_POSITION) & (_RTCTIME_SECTEN_MASK | _RTCTIME_SECONE_MASK);

        while((RTCSTAT & _RTCSTAT_SYNC_MASK) != 0U)
        {
            /* Wait for synchronization */
        }

        ALMDATE = dataDate;

        while((RTCSTAT & _RTCSTAT_SYNC_MASK) != 0U)
        {
            /* Wait for synchronization */
        }

        ALMTIME = dataTime;

        /* Configure alarm repetition */
        RTCCON1bits.AMASK = (uint8_t)alarmFreq;

        /* ALRMEN = 1 */
        RTCCON1SET = _RTCCON1_ALRMEN_MASK;  /* Enable the alarm */
    }

    <#if RTCC_INTERRUPT_MODE == true>
    ${RTCC_INSTANCE_NAME}_InterruptEnable(RTCC_INT_ALARM);  /* Enable the interrupt to the interrupt controller */
    </#if>

    return true;  /* This PLIB has no way of indicating wrong device operation so always return true */
}

<#if RTCC_INTERRUPT_MODE == true>
void ${RTCC_INSTANCE_NAME}_CallbackRegister( RTCC_CALLBACK callback, uintptr_t context )
{
    rtcc.callback = callback;

    rtcc.context = context;
}

void __attribute__((used)) ${RTCC_INSTANCE_NAME}_InterruptHandler( void )
{
    /* Clear the status flag */
    ${RTCC_IFS_REG}CLR = ${RTCC_STATREG_SHIFT_VALUE};

    if(rtcc.callback != NULL)
    {
        uintptr_t context = rtcc.context;
        rtcc.callback(context);
    }
}

</#if>