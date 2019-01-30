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
#include "plib_${RTCC_INSTANCE_NAME?lower_case}.h"

#define decimaltobcd(x)                 (((x/10)<<4)+((x - ((x/10)*10))))
#define bcdtodecimal(x)                 ((x & 0xF0) >> 4) * 10 + (x & 0x0F)

// *****************************************************************************
/* Real Time Clock System Service Object
*/
typedef struct _SYS_RTCC_OBJ_STRUCT
{
    /* - Call back function for RTCC. Happens at ALARMED */
    RTC_CALLBACK  callback;

    /* - Client data (Event Context) that will be passed to callback */
    uintptr_t context;

    /* - RTCC Alarm handle */
    RTCC_ALARM_HANDLE handle;

    /* - Interrupt source */
    uint32_t interruptSource;

} RTCC_OBJECT;

static RTCC_OBJECT rtc;

// *****************************************************************************
/* Function:
   void ${RTCC_INSTANCE_NAME}_Initialize ( void )

  Summary:
    Initializes hardware and data for the instance of the RTCC module and opens
    the specific module instance.

  Description:
    This function initializes hardware for the instance of the RTCC module,
    using the specified hardware initialization data. It also initializes any
    internal data structures.

  Parameters:
    none

  Returns:
    void
*/
void ${RTCC_INSTANCE_NAME}_Initialize ( void )
{
    /* Unlock System */
    SYSKEY = 0x00000000;
    SYSKEY = 0xAA996655;
    SYSKEY = 0x556699AA;


    /* Initialize RTCC */
    RTCCONSET = _RTCCON_RTCWREN_MASK;  /* Enable writes to RTCC */

    RTCCONCLR = _RTCCON_ON_MASK;   /* Disable clock to RTCC */

    /* wait for clock to stop. Block too long? */
    while(RTCCONbits.RTCCLKON);  /* clock disabled? */

    /* initialize the time, date and alarm */
    RTCTIME = 0x${RTCTIME_TIME}00;   /* Set RTCC time */

    RTCDATE = 0x${RTCTIME_DATE}0${RTCTIME_WEEKDAY};  /* Set RTCC date */

    RTCALRMCLR = _RTCALRM_ALRMEN_MASK;  /* Disable alarm */

    while(RTCALRMbits.ALRMSYNC);  /* Wait for disable */

    ALRMTIME = 0x${RTCALRM_TIME}00;   /* Set alarm time */

    ALRMDATE = 0x00${RTCALRM_DATE}0${RTCALRM_DAY};   /* Set alarm date */

    /* repeat forever or 0-255 times */
    <#if RTCC_ALARM_REPEAT_FOREVER == true>
    RTCALRMSET = _RTCALRM_CHIME_MASK;  /* Set alarm to repeat forever */
    <#else>
    RTCALRMCLR = _RTCALRM_CHIME_MASK;  /* Set alarm to repeat finite number of times */
    RTCALRMbits.ARPT = ${RTCALRM_ARPT};
    </#if>

    RTCALRMbits.AMASK = ${RTCC_ALARM_MASK};

    <#if RTCC_OUTPUT_ENABLE == true>
    /* Initialize the output */
    /* Select ouput to be placed on output pin */
    RTCCONbits.RTCOUTSEL = ${RTCC_OUTPUT_SELECT};
    RTCCONSET = _RTCCON_RTCOE_MASK;  /* Enable RTCC output */
    <#else>
    RTCCONCLR = _RTCCON_RTCOE_MASK;  /* Enable RTCC output */
    </#if>

    /* Set RTCC clock source (LPRC/SOSC) */
    RTCCONbits.RTCCLKSEL = ${RTCC_CLOCK_SOURCE};

    rtc.interruptSource = ${RTCC_VECTOR_NUMBER};

    /* start the RTC */
    RTCCONSET = _RTCCON_ON_MASK;
}

// *****************************************************************************
/* Function:
  bool ${RTCC_INSTANCE_NAME}_TimeSet( struct tm *Time )

  Summary:
    Sets the Real Time Clock Calendar time.

  Description:
    The function sets the time for the RTCC.

  Precondition:
    None.

  Parameters:
    time    time is in standard time format

  Returns:
    bool    always returns true
*/
bool ${RTCC_INSTANCE_NAME}_TimeSet ( struct tm *Time )
{
    uint32_t timeField, dateField;

    timeField = (decimaltobcd(Time->tm_hour) << _RTCTIME_HR01_POSITION) & (_RTCTIME_HR10_MASK | _RTCTIME_HR01_MASK);
    timeField |= (decimaltobcd(Time->tm_min) << _RTCTIME_MIN01_POSITION) & (_RTCTIME_MIN10_MASK | _RTCTIME_MIN01_MASK);
    timeField |= (decimaltobcd(Time->tm_sec) << _RTCTIME_SEC01_POSITION) & (_RTCTIME_SEC10_MASK | _RTCTIME_SEC01_MASK);

    RTCTIME = timeField;

    dateField = (decimaltobcd(Time->tm_year % 100) << _RTCDATE_YEAR01_POSITION) & (_RTCDATE_YEAR01_MASK | _RTCDATE_YEAR10_MASK);
    dateField |= (decimaltobcd(Time->tm_mon) << _RTCDATE_MONTH01_POSITION)&(_RTCDATE_MONTH01_MASK | _RTCDATE_MONTH10_MASK);
    dateField |= (decimaltobcd(Time->tm_mday) << _RTCDATE_DAY01_POSITION) & (_RTCDATE_DAY01_MASK | _RTCDATE_DAY10_MASK);
    dateField |= decimaltobcd(Time->tm_wday) & _RTCDATE_WDAY01_MASK;

    RTCDATE = dateField;

    RTCCONSET = _RTCCON_ON_MASK;  /* Start the RTCC module */

    return true;    /* This PLIB has no way of indicating wrong device operation so always return true */
}

// *****************************************************************************
/* Function:
  void ${RTCC_INSTANCE_NAME}_TimeGet( struct tm  *Time )

  Summary:
    Gets the Real Time Clock Calendar time.

  Description:
    The function gets the time from the RTCC.

  Precondition:
    None.

  Parameters:
    *Time    a pointer to a time type

  Returns:
    void
*/

void ${RTCC_INSTANCE_NAME}_TimeGet (struct tm  *Time )
{
    uint32_t dataTime, dataDate;

    dataTime = RTCTIME;  /* read the time from the RTC */

    Time->tm_hour = 10 * (bcdtodecimal((dataTime & _RTCTIME_HR10_MASK) >> _RTCTIME_HR10_POSITION)) +
                         bcdtodecimal((dataTime & _RTCTIME_HR01_MASK) >> _RTCTIME_HR01_POSITION);
    Time->tm_min =  10 * (bcdtodecimal((dataTime & _RTCTIME_MIN10_MASK) >> _RTCTIME_MIN10_POSITION)) +
                         bcdtodecimal((dataTime & _RTCTIME_MIN01_MASK) >> _RTCTIME_MIN01_POSITION);
    Time->tm_sec =  10 * (bcdtodecimal((dataTime & _RTCTIME_SEC10_MASK) >> _RTCTIME_SEC10_POSITION)) +
                         bcdtodecimal((dataTime & _RTCTIME_SEC01_MASK) >> _RTCTIME_SEC01_POSITION);

    dataDate = RTCDATE;  /* read the date from the RTC */

    Time->tm_year = 10 * (bcdtodecimal((dataDate & _RTCDATE_YEAR10_MASK) >> _RTCDATE_YEAR10_POSITION)) +
                         bcdtodecimal((dataDate & _RTCDATE_YEAR01_MASK) >> _RTCDATE_YEAR01_POSITION);
    Time->tm_year += 2000;  /* This RTC designed for 0-99 year range.  Need to add 2000 to that. */
    Time->tm_mon =  10 * (bcdtodecimal((dataDate & _RTCDATE_MONTH10_MASK) >> _RTCDATE_MONTH10_POSITION)) +
                         bcdtodecimal((dataDate & _RTCDATE_MONTH01_MASK) >> _RTCDATE_MONTH01_POSITION);
    Time->tm_mday = 10 * (bcdtodecimal((dataDate & _RTCDATE_DAY10_MASK) >> _RTCDATE_DAY10_POSITION)) +
                         bcdtodecimal((dataDate & _RTCDATE_DAY01_MASK) >> _RTCDATE_DAY01_POSITION);

    Time->tm_wday = bcdtodecimal((dataDate & _RTCDATE_WDAY01_MASK) >> _RTCDATE_WDAY01_POSITION);
    Time->tm_yday = 0;  /* not used */
    Time->tm_isdst = 0;    /* not used */
}

// *****************************************************************************
/* Function:
  bool ${RTCC_INSTANCE_NAME}_AlarmSet( struct tm *alarmTime, RTC_ALARM_MASK alarmFreq )

  Summary:
    Sets the Real Time Clock Calendar alarm time.

  Description:
    The function sets the time for the RTCC alarm.

  Precondition:
    None.

  Parameters:
    *alarmTime  *alarmTime  in time format

    alarmFreq   frequency alarm repeats itself for generating alarm condition

  Returns:
    bool        always returns true
*/
bool ${RTCC_INSTANCE_NAME}_AlarmSet( struct tm *alarmTime, RTC_ALARM_MASK alarmFreq )
{
    uint32_t dataDate, dataTime;

    <#lt><#if RTCC_INTERRUPT_MODE == true>
    /* Disable interrupt, if enabled, before setting up alarm */
    ${RTCC_INSTANCE_NAME}_InterruptDisable(0x00);
    <#lt></#if>

    if(RTC_ALARM_MASK_OFF != alarmFreq)
    {
        dataDate  = (decimaltobcd(alarmTime->tm_mon) << _RTCDATE_MONTH01_POSITION) & (_RTCDATE_MONTH01_MASK | _RTCDATE_MONTH10_MASK);
        dataDate |= (decimaltobcd(alarmTime->tm_mday) << _RTCDATE_DAY01_POSITION) & (_RTCDATE_DAY01_MASK | _RTCDATE_DAY10_MASK);
        dataDate |= decimaltobcd(alarmTime->tm_wday) & _RTCDATE_WDAY01_MASK;

        dataTime  = (decimaltobcd(alarmTime->tm_hour) << _RTCTIME_HR01_POSITION) & (_RTCTIME_HR10_MASK | _RTCTIME_HR01_MASK);
        dataTime |= (decimaltobcd(alarmTime->tm_min) << _RTCTIME_MIN01_POSITION) & (_RTCTIME_MIN10_MASK | _RTCTIME_MIN01_MASK);
        dataTime |= (decimaltobcd(alarmTime->tm_sec) << _RTCTIME_SEC01_POSITION) & (_RTCTIME_SEC10_MASK | _RTCTIME_SEC01_MASK);

        ALRMDATE = dataDate;
        ALRMTIME = dataTime;

        /* AMASK = maskVal */
        RTCALRMSET = (alarmFreq << _RTCALRM_AMASK_POSITION) & _RTCALRM_AMASK_MASK;

        /* ALRMEN = 1 */
        RTCALRMSET = _RTCALRM_ALRMEN_MASK;  /* Enable the alarm */
    }
    else
    {
        /* ALRMEN = 0 */
        RTCALRMCLR = _RTCALRM_ALRMEN_MASK;  /* Disable the alarm */
    }
    <#lt><#if RTCC_INTERRUPT_MODE == true>
    ${RTCC_INSTANCE_NAME}_InterruptEnable(0x00);  /* Enable the interrupt to the interrupt controller */
    <#lt></#if>
    return true;  /* This PLIB has no way of indicating wrong device operation so always return true */
}

// *****************************************************************************
/* Function:
  void ${RTCC_INSTANCE_NAME}_CallbackRegister( RTC_CALLBACK callback, uintptr_t context )

  Summary:
    Sets the callback function for an alarm.

  Description:
    This function sets the callback function that will be called when the RTCC
    alarm is reached.

  Precondition:
    None.

  Parameters:
    *callback   - a pointer to the function to be called when alarm is reached.
                  Use NULL to Un Register the alarm callback

    context     - a pointer to user defined data to be used when the callback
                  function is called. NULL can be passed in if no data needed.

  Returns:
    void
*/
void ${RTCC_INSTANCE_NAME}_CallbackRegister( RTC_CALLBACK callback, uintptr_t context )
{
    /* - Un-register callback if NULL */
    if (callback == NULL)
    {
        rtc.callback = NULL;
        rtc.context = (uintptr_t) NULL;
    }
    /* - Save callback and context in local memory */
    rtc.callback = callback;
    rtc.context = context;
    rtc.handle = (RTCC_ALARM_HANDLE)&rtc;
}

// *****************************************************************************
/* Function:
   void RTCC_InterruptHandler (void)

  Summary:
    Interrupt handler for RTCC interrupts.

  Description:
    This function calls the user-registered callback, if registered.
    Also clears the interrupt source bit to allow future RTCC interrupts to occur.

  Parameters:
    none

  Returns:
    void
*/
void RTCC_InterruptHandler(void)
{
    ${RTCC_IFS_REG}CLR = ${RTCC_STATREG_SHIFT_VALUE}; /* clear the status flag */

    if((rtc.callback != NULL))
    {
        rtc.callback(rtc.handle, rtc.context);
    }
}

// *****************************************************************************
/* Function:
   void ${RTCC_INSTANCE_NAME}_InterruptEnable(RTC_INT_MASK interrupt)

  Summary:
    Enable RTCC interrupts.

  Description:
    This function enables RTCC interrupts.  The mask is not used in the PIC32MZ
    family, so the argument is ignored.  This maintains the existing API for H3.

  Parameters:
    none

  Returns:
    void
*/
void ${RTCC_INSTANCE_NAME}_InterruptEnable(RTC_INT_MASK interrupt)
{
    ${RTCC_IEC_REG}SET = ${RTCC_ENBLREG_ENABLE_VALUE};
}

// *****************************************************************************
/* Function:
   void ${RTCC_INSTANCE_NAME}_InterruptDisable(RTC_INT_MASK interrupt)

  Summary:
    Disable RTCC interrupts.

  Description:
    This function disables RTCC interrupts.  The mask is not used in the PIC32MZ
    family, so the argument is ignored.  This maintains the existing API for H3.

  Parameters:
    none

  Returns:
    void
*/
void ${RTCC_INSTANCE_NAME}_InterruptDisable(RTC_INT_MASK interrupt)
{
    ${RTCC_IEC_REG}CLR = ${RTCC_ENBLREG_ENABLE_VALUE};
}

<#--
/*******************************************************************************
 End of File
*/
-->