/*******************************************************************************
  Real Time Counter (${RTC_INSTANCE_NAME}) PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${RTC_INSTANCE_NAME?lower_case}_clock.c

  Summary:
    ${RTC_INSTANCE_NAME} PLIB Implementation file

  Description:
    This file defines the interface to the RTC peripheral library. This
    library provides access to and control of the associated peripheral
    instance in clock/calendar mode.

*******************************************************************************/
// DOM-IGNORE-BEGIN
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
// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
/* This section lists the other files that are included in this file.
*/

#include "plib_${RTC_INSTANCE_NAME?lower_case}.h"
#include "device.h"
#include <stdlib.h>
#include <limits.h>
<#if core.CoreSysIntFile == true>
#include "interrupts.h"
</#if>

/* Reference Year */
#define REFERENCE_YEAR              (${RTC_MODE2_REFERENCE_YEAR}U)

/* Refernce Year in tm structure year (C standard) */
#define TM_STRUCT_REFERENCE_YEAR    (1900U)

/* Adjust user year with respect to tm structure year (C Standard) */
#define ADJUST_TM_YEAR(year)        (year + TM_STRUCT_REFERENCE_YEAR)

/* Adjust user month */
#define ADJUST_MONTH(month)         ((month) + (1U))

/* Adjust to tm structure month */
#define ADJUST_TM_STRUCT_MONTH(mon) ((mon) - (1U))

<#if RTC_MODE2_INTERRUPT = true >
    <#lt>static RTC_OBJECT ${RTC_INSTANCE_NAME?lower_case}Obj;
</#if>

static void ${RTC_INSTANCE_NAME}_ClockReadSynchronization(void)
{
<#if RTC_COUNT_CLOCK_RCONT >
    <#lt>   /* Enable continuous read-synchronization request for CLOCK register */
    <#lt>   if( (${RTC_INSTANCE_NAME}_REGS->${RTC_MODULE_SELECTION}.RTC_READREQ & RTC_READREQ_RCONT_Msk) != RTC_READREQ_RCONT_Msk)
    <#lt>   {
    <#lt>       ${RTC_INSTANCE_NAME}_REGS->${RTC_MODULE_SELECTION}.RTC_READREQ = RTC_READREQ_RCONT_Msk | RTC_READREQ_ADDR(0x10U);
    <#lt>       ${RTC_INSTANCE_NAME}_REGS->${RTC_MODULE_SELECTION}.RTC_READREQ |= RTC_READREQ_RREQ_Msk;
    <#lt>       while((${RTC_INSTANCE_NAME}_REGS->${RTC_MODULE_SELECTION}.RTC_STATUS & RTC_STATUS_SYNCBUSY_Msk) == RTC_STATUS_SYNCBUSY_Msk)
    <#lt>       {
    <#lt>           /* Wait for Read-Synchronization */
    <#lt>       }
    <#lt>   }
<#else>
    <#lt>   /* Read-synchronization for CLOCK register */
    <#lt>   ${RTC_INSTANCE_NAME}_REGS->${RTC_MODULE_SELECTION}.RTC_READREQ = RTC_READREQ_RREQ_Msk | RTC_READREQ_ADDR(0x10U);
    <#lt>   while((${RTC_INSTANCE_NAME}_REGS->${RTC_MODULE_SELECTION}.RTC_STATUS & RTC_STATUS_SYNCBUSY_Msk) == RTC_STATUS_SYNCBUSY_Msk)
    <#lt>   {
    <#lt>       /* Wait for Read-Synchronization */
    <#lt>   }
</#if>
}

void ${RTC_INSTANCE_NAME}_Initialize(void)
{
    /* Writing to CTRL register will trigger write-synchronization */
    ${RTC_INSTANCE_NAME}_REGS->MODE2.RTC_CTRL |= RTC_MODE2_CTRL_SWRST_Msk;
    while((${RTC_INSTANCE_NAME}_REGS->${RTC_MODULE_SELECTION}.RTC_STATUS & RTC_STATUS_SYNCBUSY_Msk) == RTC_STATUS_SYNCBUSY_Msk)
    {
        /* Wait for Write-Synchronization */
    }
    <#if RTC_MODE2_EVCTRL != "0">
        <#lt>   ${RTC_INSTANCE_NAME}_REGS->MODE2.RTC_EVCTRL = 0x${RTC_MODE2_EVCTRL}U;
    </#if>

    /* Writing to CTRL register will trigger write-synchronization */
    <@compress single_line=true>${RTC_INSTANCE_NAME}_REGS->MODE2.RTC_CTRL = RTC_MODE2_CTRL_MODE(2U) |
                                                            RTC_MODE2_CTRL_PRESCALER(${RTC_MODE2_PRESCALER}U) |
                                                            RTC_MODE2_CTRL_ENABLE_Msk;</@compress>
    while((${RTC_INSTANCE_NAME}_REGS->${RTC_MODULE_SELECTION}.RTC_STATUS & RTC_STATUS_SYNCBUSY_Msk) == RTC_STATUS_SYNCBUSY_Msk)
    {
        /* Wait for Write-Synchronization */
    }

    <#if (RTC_MODE2_INTERRUPT = true) && (RTC_MODE2_INTENSET != "0")>
        <#lt>   ${RTC_INSTANCE_NAME}_REGS->MODE2.RTC_INTENSET = 0x${RTC_MODE2_INTENSET}U;
    </#if>
    <#if RTC_COUNT_CLOCK_RCONT >
        <#lt>   /* Enable continuous read request for CLOCK register */
        <#lt>   ${RTC_INSTANCE_NAME}_ClockReadSynchronization();
    </#if>
}
<#if RTC_FREQCORR = true >
    <#lt>void ${RTC_INSTANCE_NAME}_FrequencyCorrect (int8_t correction)
    <#lt>{
    <#lt>    uint8_t abs_correction  = (((uint8_t)correction & 0x80U) != 0U) ? \
    <#lt>            ((0xFFU - (uint8_t)correction) + 0x1U) : (uint8_t)correction;

    <#lt>    /* Convert to positive value and adjust Register sign bit. */
    <#lt>    if (correction < 0)
    <#lt>    {
    <#lt>        abs_correction |= RTC_FREQCORR_SIGN_Msk;
    <#lt>    }

    <#lt>    /* Writing to FREQCORR register will trigger write-synchronization */
    <#lt>    ${RTC_INSTANCE_NAME}_REGS->MODE2.RTC_FREQCORR = abs_correction;
    <#lt>    while((${RTC_INSTANCE_NAME}_REGS->${RTC_MODULE_SELECTION}.RTC_STATUS & RTC_STATUS_SYNCBUSY_Msk) == RTC_STATUS_SYNCBUSY_Msk)
    <#lt>    {
    <#lt>        /* Wait for Write-Synchronization */
    <#lt>    }
    <#lt>}
</#if>

bool ${RTC_INSTANCE_NAME}_RTCCTimeSet (struct tm * initialTime )
{
    /* Writing to CLOCK register will trigger write-synchronization */
    ${RTC_INSTANCE_NAME}_REGS->MODE2.RTC_CLOCK = (((TM_STRUCT_REFERENCE_YEAR + (uint32_t)initialTime->tm_year) - REFERENCE_YEAR) << RTC_MODE2_CLOCK_YEAR_Pos) |
                    ((ADJUST_MONTH((uint32_t)initialTime->tm_mon)) << RTC_MODE2_CLOCK_MONTH_Pos) |
                    ((uint32_t)initialTime->tm_mday << RTC_MODE2_CLOCK_DAY_Pos) |
                    ((uint32_t)initialTime->tm_hour << RTC_MODE2_CLOCK_HOUR_Pos) |
                    ((uint32_t)initialTime->tm_min << RTC_MODE2_CLOCK_MINUTE_Pos) |
                    ((uint32_t)initialTime->tm_sec << RTC_MODE2_CLOCK_SECOND_Pos);
    while((${RTC_INSTANCE_NAME}_REGS->${RTC_MODULE_SELECTION}.RTC_STATUS & RTC_STATUS_SYNCBUSY_Msk) == RTC_STATUS_SYNCBUSY_Msk)
    {
        /* Wait for Write-Synchronization */
    }
    return true;
}

void ${RTC_INSTANCE_NAME}_RTCCTimeGet ( struct tm * currentTime )
{
    uint32_t dataClockCalendar = 0U;

	/* Added temp variable for suppressing MISRA C 2012 Rule : 10.x.
	   Please don't ignore this variable for any future modifications */
	uint32_t temp;

    /* Enable read-synchronization for CLOCK register to avoid CPU stall */
    ${RTC_INSTANCE_NAME}_ClockReadSynchronization();
    dataClockCalendar = ${RTC_INSTANCE_NAME}_REGS->MODE2.RTC_CLOCK;

	temp = ((dataClockCalendar & RTC_MODE2_CLOCK_HOUR_Msk) >> RTC_MODE2_CLOCK_HOUR_Pos);
    currentTime->tm_hour = (int)temp;
	temp = ((dataClockCalendar & RTC_MODE2_CLOCK_MINUTE_Msk) >> RTC_MODE2_CLOCK_MINUTE_Pos);
    currentTime->tm_min  = (int)temp;
	temp = ((dataClockCalendar & RTC_MODE2_CLOCK_SECOND_Msk) >> RTC_MODE2_CLOCK_SECOND_Pos);
    currentTime->tm_sec  = (int)temp;
    temp = (ADJUST_TM_STRUCT_MONTH(((dataClockCalendar & RTC_MODE2_CLOCK_MONTH_Msk) >> RTC_MODE2_CLOCK_MONTH_Pos)));
    currentTime->tm_mon  = (int)temp;
	temp = ((((dataClockCalendar & RTC_MODE2_CLOCK_YEAR_Msk)>> RTC_MODE2_CLOCK_YEAR_Pos) + REFERENCE_YEAR) - TM_STRUCT_REFERENCE_YEAR);
    currentTime->tm_year = (int)temp;
	temp = ((dataClockCalendar & RTC_MODE2_CLOCK_DAY_Msk) >> RTC_MODE2_CLOCK_DAY_Pos);
    currentTime->tm_mday = (int)temp;
}
<#if RTC_MODE2_INTERRUPT = true>

    <#lt>bool ${RTC_INSTANCE_NAME}_RTCCAlarmSet (struct tm * alarmTime, RTC_ALARM_MASK mask)
    <#lt>{
    <#lt>   /* Writing to ALARM register will trigger write-synchronization */
    <#lt>   ${RTC_INSTANCE_NAME}_REGS->MODE2.RTC_ALARM = (((TM_STRUCT_REFERENCE_YEAR + (uint32_t)alarmTime->tm_year) - REFERENCE_YEAR) << RTC_MODE2_CLOCK_YEAR_Pos) |
    <#lt>                    (ADJUST_MONTH((uint32_t)alarmTime->tm_mon) << RTC_MODE2_CLOCK_MONTH_Pos) |
    <#lt>                    ((uint32_t)alarmTime->tm_mday << RTC_MODE2_CLOCK_DAY_Pos) |
    <#lt>                    ((uint32_t)alarmTime->tm_hour << RTC_MODE2_CLOCK_HOUR_Pos) |
    <#lt>                     ((uint32_t)alarmTime->tm_min << RTC_MODE2_CLOCK_MINUTE_Pos) |
    <#lt>                     ((uint32_t)alarmTime->tm_sec << RTC_MODE2_CLOCK_SECOND_Pos);
    <#lt>   while((${RTC_INSTANCE_NAME}_REGS->${RTC_MODULE_SELECTION}.RTC_STATUS & RTC_STATUS_SYNCBUSY_Msk) == RTC_STATUS_SYNCBUSY_Msk)
    <#lt>   {
    <#lt>       /* Wait for Write-Synchronization */
    <#lt>   }

    <#lt>   /* Writing to MASK register will trigger write-synchronization */
    <#lt>   ${RTC_INSTANCE_NAME}_REGS->MODE2.RTC_MASK = (uint8_t)mask;
    <#lt>   while((${RTC_INSTANCE_NAME}_REGS->${RTC_MODULE_SELECTION}.RTC_STATUS & RTC_STATUS_SYNCBUSY_Msk) == RTC_STATUS_SYNCBUSY_Msk)
    <#lt>   {
    <#lt>       /* Wait for Write-Synchronization */
    <#lt>   }

    <#lt>   ${RTC_INSTANCE_NAME}_REGS->MODE2.RTC_INTENSET = RTC_MODE2_INTENSET_ALARM0_Msk;
    <#lt>   return true;
    <#lt>}

    <#lt>void ${RTC_INSTANCE_NAME}_RTCCCallbackRegister ( RTC_CALLBACK callback, uintptr_t context)
    <#lt>{
    <#lt>   ${RTC_INSTANCE_NAME?lower_case}Obj.alarmCallback = callback;
    <#lt>   ${RTC_INSTANCE_NAME?lower_case}Obj.context       = context;
    <#lt>}


    <#lt>void ${RTC_INSTANCE_NAME}_InterruptHandler(void)
    <#lt>{
    <#lt>   ${RTC_INSTANCE_NAME?lower_case}Obj.intCause = (RTC_CLOCK_INT_MASK) ${RTC_INSTANCE_NAME}_REGS->MODE2.RTC_INTFLAG;

    <#lt>   /* Clear All Interrupts */
    <#lt>   ${RTC_INSTANCE_NAME}_REGS->MODE2.RTC_INTFLAG = RTC_MODE2_INTFLAG_Msk;

    <#lt>   if(${RTC_INSTANCE_NAME?lower_case}Obj.alarmCallback != NULL)
    <#lt>   {
    <#lt>       ${RTC_INSTANCE_NAME?lower_case}Obj.alarmCallback(${RTC_INSTANCE_NAME?lower_case}Obj.intCause, ${RTC_INSTANCE_NAME?lower_case}Obj.context);
    <#lt>   }
    <#lt>}
</#if>
