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

#define decimaltobcd(x)                 (((((uint32_t)x) / (10UL)) << 4) + ((((uint32_t)x) - ((((uint32_t)x) / (10U)) * (10U)))))
#define bcdtodecimal(x)                 (((((uint32_t)x) & (0xF0UL)) >> 4) * (10U) + (((uint32_t)x) & (0x0FU)))

<#if RTCC_INTERRUPT_MODE == true>
/* Real Time Clock System Service Object */
typedef struct SYS_RTCC_OBJ_STRUCT
{
    /* Call back function for RTCC.*/
    RTCC_CALLBACK  callback;

    /* Client data (Event Context) that will be passed to callback */
    uintptr_t context;

} RTCC_OBJECT;

static RTCC_OBJECT rtcc;

</#if>
// *****************************************************************************
// *****************************************************************************
// Section: ${RTCC_INSTANCE_NAME} Implementation
// *****************************************************************************
// *****************************************************************************

void ${RTCC_INSTANCE_NAME}_Initialize( void )
{
    /* Unlock System */
    SYSKEY = 0x00000000;
    SYSKEY = 0xAA996655;
    SYSKEY = 0x556699AA;

    RTCCONSET = _RTCCON_RTCWREN_MASK;  /* Enable writes to RTCC */

    /* Lock System */
    SYSKEY = 0x00000000;

    <#if RTCC_OUTPUT_ENABLE == true>
    /* Select output to be placed on output pin */
    RTCCONbits.${RTCC_OUTPUT_SELECT_BITNAME} = ${RTCC_OUTPUT_SELECT};
    RTCCONSET = _RTCCON_RTCOE_MASK;  /* Enable RTCC output */
    <#else>
    RTCCONbits.RTCOE= 0;  /* Disable RTCC output */
    </#if>

    <#if RTCC_CLOCK_SOURCE??>
    /* Set RTCC clock source (LPRC/SOSC) */
    RTCCONbits.RTCCLKSEL = ${RTCC_CLOCK_SOURCE};
    </#if>

    <#if RTC_TIMEANDDATE == true>
        <#lt>    RTCCONbits.ON = 0;   /* Disable clock to RTCC */
        <#lt>    while((RTCCONbits.RTCCLKON) != 0U)  /* Wait for clock to stop */
        <#lt>    {
        <#lt>      /* Do Nothing */
        <#lt>    }

        <#lt>    RTCTIME = 0x${RTCTIME_TIME}00;   /* Set RTCC time */
        <#lt>    RTCDATE = 0x${RTCTIME_DATE}0${RTCTIME_WEEKDAY};  /* Set RTCC date */
    </#if>

    <#if RTCC_ALARM_REPEAT_FOREVER == true>
        <#lt>    RTCALRMSET = _RTCALRM_CHIME_MASK;  /* Set alarm to repeat forever */
    <#else>
        <#lt>    /* Set alarm to repeat finite number of times */
        <#lt>    RTCALRMCLR = _RTCALRM_CHIME_MASK;
        <#lt>    RTCALRMbits.ARPT = ${RTCALRM_ARPT};
    </#if>

    <#if RTC_ALARM == true>
        <#lt>    RTCALRMCLR = _RTCALRM_ALRMEN_MASK;  /* Disable alarm */
        <#lt>    while((RTCALRMbits.ALRMSYNC) != 0U)  /* Wait for disable */
        <#lt>    {
        <#lt>       /* Do Nothing */
        <#lt>    }

        <#lt>    ALRMTIME = 0x${RTCALRM_TIME}00;   /* Set alarm time */
        <#lt>    ALRMDATE = 0x00${RTCALRM_DATE}0${RTCALRM_DAY};   /* Set alarm date */
        <#lt>    RTCALRMbits.AMASK = ${RTCC_ALARM_MASK}; /* Set alarm frequency */
    
        <#if RTCC_INTERRUPT_MODE == true>
            <#lt>    ${RTCC_IEC_REG}SET = (uint32_t)RTCC_INT_ALARM; /* Enable RTC Alarma interrupt */
        </#if>
    
        <#lt>    RTCALRMSET = _RTCALRM_ALRMEN_MASK;  /* Enable the alarm */
    </#if>

    /* start the RTC */
    RTCCONSET = _RTCCON_ON_MASK;
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

    timeField = (decimaltobcd(Time->tm_hour) << _RTCTIME_HR01_POSITION) & (_RTCTIME_HR10_MASK | _RTCTIME_HR01_MASK);
    timeField |= (decimaltobcd(Time->tm_min) << _RTCTIME_MIN01_POSITION) & (_RTCTIME_MIN10_MASK | _RTCTIME_MIN01_MASK);
    timeField |= (decimaltobcd(Time->tm_sec) << _RTCTIME_SEC01_POSITION) & (_RTCTIME_SEC10_MASK | _RTCTIME_SEC01_MASK);

    while((RTCCON & _RTCCON_RTCSYNC_MASK) != 0U)
    {
       /* Do Nothing */
     }

    RTCTIME = timeField;

    dateField = (decimaltobcd(Time->tm_year % 100) << _RTCDATE_YEAR01_POSITION) & (_RTCDATE_YEAR01_MASK | _RTCDATE_YEAR10_MASK);
    dateField |= (decimaltobcd((Time->tm_mon + 1U)) << _RTCDATE_MONTH01_POSITION)&(_RTCDATE_MONTH01_MASK | _RTCDATE_MONTH10_MASK);
    dateField |= (decimaltobcd(Time->tm_mday) << _RTCDATE_DAY01_POSITION) & (_RTCDATE_DAY01_MASK | _RTCDATE_DAY10_MASK);
    dateField |= decimaltobcd(Time->tm_wday) & _RTCDATE_WDAY01_MASK;

    while((RTCCON & _RTCCON_RTCSYNC_MASK) != 0U)
    {
        /* Do Nothing */
    }

    RTCDATE = dateField;

    RTCCONSET = _RTCCON_ON_MASK;  /* Start the RTCC module */

    return true;    /* This PLIB has no way of indicating wrong device operation so always return true */
}

void ${RTCC_INSTANCE_NAME}_TimeGet( struct tm  *Time )
{
    uint32_t dataTime, dataDate;
    uint32_t tempHour,tempMin, tempSec, tempYear, tempMon, tempMday, tempWday;

    while((RTCCON & _RTCCON_RTCSYNC_MASK) != 0U)
    {
       /* Do Nothing */
    }

    dataTime = RTCTIME;  /* read the time from the RTC */

    tempHour =   (10U * (bcdtodecimal((dataTime & _RTCTIME_HR10_MASK) >> _RTCTIME_HR10_POSITION)) +
                         (bcdtodecimal((dataTime & _RTCTIME_HR01_MASK) >> _RTCTIME_HR01_POSITION)));
    Time->tm_hour = (int)tempHour;
    
    tempMin =   (10U * (bcdtodecimal((dataTime & _RTCTIME_MIN10_MASK) >> _RTCTIME_MIN10_POSITION)) +
                         (bcdtodecimal((dataTime & _RTCTIME_MIN01_MASK) >> _RTCTIME_MIN01_POSITION)));
    Time->tm_min =  (int)tempMin;
    
    tempSec =   (10U * (bcdtodecimal((dataTime & _RTCTIME_SEC10_MASK) >> _RTCTIME_SEC10_POSITION)) +
                         (bcdtodecimal((dataTime & _RTCTIME_SEC01_MASK) >> _RTCTIME_SEC01_POSITION)));
    Time->tm_sec =  (int)tempSec;

    while((RTCCON & _RTCCON_RTCSYNC_MASK) != 0U)
    {
        /* Do Nothing */
    }

    dataDate = RTCDATE;  /* read the date from the RTC */

    tempYear =   (10U * (bcdtodecimal((dataDate & _RTCDATE_YEAR10_MASK) >> _RTCDATE_YEAR10_POSITION)) +
                         (bcdtodecimal((dataDate & _RTCDATE_YEAR01_MASK) >> _RTCDATE_YEAR01_POSITION)));
    Time->tm_year =  (int)tempYear;
    
    Time->tm_year += 2000;  /* This RTC designed for 0-99 year range.  Need to add 2000 to that. */
    
    tempMon =   (10U * (bcdtodecimal((dataDate & _RTCDATE_MONTH10_MASK) >> _RTCDATE_MONTH10_POSITION)) +
                         (bcdtodecimal((dataDate & _RTCDATE_MONTH01_MASK) >> _RTCDATE_MONTH01_POSITION))) - 1U;
    Time->tm_mon =  (int)tempMon;
    
    tempMday =   (10U * (bcdtodecimal((dataDate & _RTCDATE_DAY10_MASK) >> _RTCDATE_DAY10_POSITION)) +
                         (bcdtodecimal((dataDate & _RTCDATE_DAY01_MASK) >> _RTCDATE_DAY01_POSITION)));
    Time->tm_mday = (int)tempMday;

    tempWday =    bcdtodecimal((dataDate & _RTCDATE_WDAY01_MASK) >> _RTCDATE_WDAY01_POSITION);
    Time->tm_wday = (int)tempWday;
    
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

    RTCALRMCLR = _RTCALRM_ALRMEN_MASK;  /* Disable alarm */
    while((RTCALRMbits.ALRMSYNC) != 0U)  /* Wait for disable */
    {
       /* Do Nothing */
    }

    if(RTCC_ALARM_MASK_OFF != alarmFreq)
    {
        dataDate  = (decimaltobcd((alarmTime->tm_mon + 1U)) << _RTCDATE_MONTH01_POSITION) & (_RTCDATE_MONTH01_MASK | _RTCDATE_MONTH10_MASK);
        dataDate |= (decimaltobcd(alarmTime->tm_mday) << _RTCDATE_DAY01_POSITION) & (_RTCDATE_DAY01_MASK | _RTCDATE_DAY10_MASK);
        dataDate |= decimaltobcd(alarmTime->tm_wday) & _RTCDATE_WDAY01_MASK;

        dataTime  = (decimaltobcd(alarmTime->tm_hour) << _RTCTIME_HR01_POSITION) & (_RTCTIME_HR10_MASK | _RTCTIME_HR01_MASK);
        dataTime |= (decimaltobcd(alarmTime->tm_min) << _RTCTIME_MIN01_POSITION) & (_RTCTIME_MIN10_MASK | _RTCTIME_MIN01_MASK);
        dataTime |= (decimaltobcd(alarmTime->tm_sec) << _RTCTIME_SEC01_POSITION) & (_RTCTIME_SEC10_MASK | _RTCTIME_SEC01_MASK);

        while((RTCCON & _RTCCON_RTCSYNC_MASK) != 0U)
        {
           /* Do Nothing */
        }

        ALRMDATE = dataDate;

        while((RTCCON & _RTCCON_RTCSYNC_MASK) != 0U)
        {
           /* Do Nothing */
         }

        ALRMTIME = dataTime;

        /* Configure alarm repetition */
        RTCALRMbits.AMASK = (uint8_t)alarmFreq;

        /* ALRMEN = 1 */
        RTCALRMSET = _RTCALRM_ALRMEN_MASK;  /* Enable the alarm */
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

void ${RTCC_INSTANCE_NAME}_InterruptHandler( void )
{
    /* Clear the status flag */
    ${RTCC_IFS_REG}CLR = ${RTCC_STATREG_SHIFT_VALUE};

    if(rtcc.callback != NULL)
    {
        rtcc.callback(rtcc.context);
    }
}

</#if>