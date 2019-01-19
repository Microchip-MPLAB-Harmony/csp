/*******************************************************************************
  Real Time Counter (RTCC) PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_rtcc.h

  Summary:
    RTCC PLIB Header file

  Description:
    This file defines the interface to the RTC peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

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

#ifndef PLIB_RTCC_H
#define PLIB_RTCC_H

#include <stddef.h>
#include <stdbool.h>
#include <stdint.h>
#include "device.h"
#include <time.h>


// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility
extern "C" {
#endif
// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Section: type definitions
// *****************************************************************************
// *****************************************************************************
typedef enum 
{
    RTC_ALARM_MASK_HALF_SECOND = 0x00,   // Every half-second
    RTC_ALARM_MASK_SECOND = 0x01,        // Every second
    RTC_ALARM_MASK_10_SECONDS = 0x02,    // Every 10 seconds
    RTC_ALARM_MASK_SS = 0x03,            // Every minute
    RTC_ALARM_MASK_10_MINUTES = 0x04,    // Every 10 minutes
    RTC_ALARM_MASK_HOUR = 0x05,          // Every hour
    RTC_ALARM_MASK_HHMISS = 0x06,        // Once a day
    RTC_ALARM_MASK_WEEK = 0x07,          // Once a week
    RTC_ALARM_MASK_MONTH = 0x08,         // Once a month
    RTC_ALARM_MASK_YEAR = 0x09,          // Once a year
    RTC_ALARM_MASK_OFF = 0xFF            // Disabled
} RTC_ALARM_MASK;	

// *****************************************************************************
/* RTCC_ALARM_HANDLE

  Summary:
	Holds a handle for an alarm.
	
  Description:
	RTCC_ALARM_HANDLE holds a handle to an alarm.
	
  Remarks:
    Use RTCC_ALARM_HANDLE to receive a handle from AlarmRegister function.
*/

typedef uintptr_t RTCC_ALARM_HANDLE;

// *****************************************************************************
/* RTC_CALLBACK

  Summary:
    Use to register a callback with the RTCC.

  Description:
    When the alarm is asserted, a callback can be activated. 
    Use RTC_CALLBACK as the function pointer to register the callback
    with the alarm.

  Remarks:
    The callback should look like: 
      void callback(handle, context);
	Make sure the return value and parameters of the callback are correct.
*/
typedef void (*RTC_CALLBACK)(RTCC_ALARM_HANDLE handle, uintptr_t context);

typedef enum  /* Not used by this DOSID, but kept to preserve API interface */
{
    RTC_INT_ALARM = 0x02,          // Alarm Event
    RTC_INT_TIME = 0x08 ,          // Not supported by this PLIB
    RTC_INT_CALENDAR = 0x10,       // Not supported by this PLIB
} RTC_INT_MASK;	

// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************

/*  Functions to support the system service for RTCC.
*/
void RTCC_InterruptEnable(RTC_INT_MASK interrupt);
void RTCC_InterruptDisable(RTC_INT_MASK interrupt);

// *****************************************************************************
/* Function:
  bool RTCC_TimeSet( struct tm *Time )

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

  Example:
    <code>
    struct tm time;
    time.tm_hour = 13;
    time.tm_min = 23;
    time.tm_sec = 39;
    time.tm_year = 18;
    time.tm_mon = 10;
    time.tm_mday = 29;
    time.tm_wday = 1;   
    status = RTCC_TimeSet(&time);
    </code>
*/
bool RTCC_TimeSet ( struct tm *Time );

// *****************************************************************************
/* Function:
  void RTCC_TimeGet( struct tm  *Time )

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

  Example:
    <code>
    struct tm time;
    RTCC_TimeGet(&time);
    </code>
*/
void RTCC_TimeGet (struct tm  *Time );

// *****************************************************************************
/* Function:
  bool RTCC_AlarmSet( struct tm *alarmTime, RTC_ALARM_MASK alarmFreq )

  Summary:
    Sets the Real Time Clock Calendar alarm time.

  Description:
    The function sets the time for the RTCC alarm.

  Precondition:
    None.

  Parameters:
    *alarmTime  in time format

    alarmFreq   frequency alarm repeats itself for generating alarm condition         

  Returns:
    bool        always returns true
    
  Example:
    <code>
    struct tm time;
    time.tm_hour = 13;
    time.tm_min = 23;
    time.tm_sec = 50;
    time.tm_year = 18;
    time.tm_mon = 10;
    time.tm_mday = 29;
    time.tm_wday = 1;
    RTCC_AlarmSet(&time, RTC_ALARM_MASK_SS);
    </code>
*/
bool RTCC_AlarmSet( struct tm *alarmTime, RTC_ALARM_MASK alarmFreq );

// *****************************************************************************
/* Function:
  void RTCC_CallbackRegister( RTC_CALLBACK callback, uintptr_t context )

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
    
  Example:
    <code>
    RTCC_CallbackRegister(myfunction, (uintptr_t) NULL);
    </code>
*/
void RTCC_CallbackRegister( RTC_CALLBACK callback, uintptr_t context );

//*******************************************************************************
/*
  Function:
    void RTCC_Initialize ( void )

  Summary:
    Real-Time Clock Calendar System Service initialization function.

  Description:
    This function initializes the RTCC Service.  It ensures that RTCC
	is stable and places the RTCC service in its initial state.

  Precondition:
    None

  Parameters:
    None

  Returns:
    None

  Example:
    <code>
    RTCC_Initialize();
    </code>

  Remarks:
    This function loops and blocks until initialization sequence is complete.
*/
void RTCC_Initialize ( void );

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility
}
#endif
// DOM-IGNORE-END

#endif /* PLIB_RTCC_H */
