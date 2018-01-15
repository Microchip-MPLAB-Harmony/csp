/*******************************************************************************
  Interface definition of RTC PLIB.
 
  Company:
    Microchip Technology Inc.
 
  File Name:
    plib_rtc.h
 
  Summary:
    Interface definition of the Real Time Counter and Calendar (RTC) Plib.
 
  Description:
    This file defines the interface for the RTC Plib.
    It allows user to setup alarm and retrieve current date and time.
*******************************************************************************/
 
// DOM-IGNORE-BEGIN
/*******************************************************************************
Copyright (c) 2017 released Microchip Technology Inc.  All rights reserved.
 
Microchip licenses to you the right to use, modify, copy and distribute
Software only when embedded on a Microchip microcontroller or digital signal
controller that is integrated into your product or third party product
(pursuant to the sublicense terms in the accompanying license agreement).
 
You should refer to the license agreement accompanying this Software for
additional information regarding your rights and obligations.
 
SOFTWARE AND DOCUMENTATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND,
EITHER EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION, ANY WARRANTY OF
MERCHANTABILITY, TITLE, NON-INFRINGEMENT AND FITNESS FOR A PARTICULAR PURPOSE.
IN NO EVENT SHALL MICROCHIP OR ITS LICENSORS BE LIABLE OR OBLIGATED UNDER
CONTRACT, NEGLIGENCE, STRICT LIABILITY, CONTRIBUTION, BREACH OF WARRANTY, OR
OTHER LEGAL EQUITABLE THEORY ANY DIRECT OR INDIRECT DAMAGES OR EXPENSES
INCLUDING BUT NOT LIMITED TO ANY INCIDENTAL, SPECIAL, INDIRECT, PUNITIVE OR
CONSEQUENTIAL DAMAGES, LOST PROFITS OR LOST DATA, COST OF PROCUREMENT OF
SUBSTITUTE GOODS, TECHNOLOGY, SERVICES, OR ANY CLAIMS BY THIRD PARTIES
(INCLUDING BUT NOT LIMITED TO ANY DEFENSE THEREOF), OR OTHER SIMILAR COSTS.
*******************************************************************************/
// DOM-IGNORE-END
 
#ifndef RTC_H    // Guards against multiple inclusion
#define RTC_H
 
// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
 
/*  This section lists the other files that are included in this file.
*/
 
#include <xc.h>
#include <stdint.h>
#include <stdbool.h>
#include <stddef.h>
#include <sys/attribs.h>
#include <time.h>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility
	extern "C" {
#endif
// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Section: Data Types
// *****************************************************************************
// *****************************************************************************
 
 /* RTC Alarm Mask

   Summary:
    Defines the data type for the RTC_Alarm Mask.

   Description:
    This is used to set up the alarm for RTC.

   Remarks:
    None.
*/

 typedef enum
 {
 RTC_ALARM_MASK_OFF = 0x00,         // NO Alarm
 RTC_ALARM_MASK_SS = 0x01 ,          // Every minute, seconds alarm enable
 RTC_ALARM_MASK_MI = 0x02,          // Minute alarm enable
 RTC_ALARM_MASK_HH = 0x04,          // Hour alarm enable
 RTC_ALARM_MASK_DD = 0x08,          // Date alarm enable
 RTC_ALARM_MASK_MO = 0x10,          // Month alarm enable
 RTC_ALARM_MASK_MISS = 0x03,        // Every hour
 RTC_ALARM_MASK_HHMISS = 0x07,      // Every day
 RTC_ALARM_MASK_DDHHMISS = 0x0f,    // Every month
 RTC_ALARM_MASK_MODDHHMISS = 0x1f  // Every year
 } RTC_ALARM_MASK;
 
 /* RTC Interrupt Mask

   Summary:
    Defines the Interrupt mask for RTC events.

   Description:
    This may be used to check the interrupt source for RTC.

   Remarks:
    None.
*/

 typedef enum 
{
	RTC_INT_ALARM = 0x02,          // Alarm Event
	RTC_INT_TIME = 0x08 ,          // Time Event
	RTC_INT_CALENDAR = 0x10,          // Calendar enable
} RTC_INT_MASK;	
 
// *****************************************************************************
// *****************************************************************************
/* Callback Function Pointer
 Summary:
	Defines the data type and function signature for the RTC peripheral
	callback function.
 
 Description:
	This data type defines the function signature for the RTC peripheral
	callback function. The RTC peripheral will call back the client's
	function with this signature once the alarm match occurs.
 
 Precondition:
	RTC_CallbackRegister must have been called to set the
	function to be called.
 
 Parameters:
	context - Allows the caller to provide a context value (usually a pointer
	to the callers context for multi-instance clients).
 
 Returns:
	None.
*/
typedef void (*RTC_ALARM_CALLBACK)(uintptr_t context);
 
// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************

/* The following functions make up the methods (set of possible operations) of
 this interface.
*/
// *****************************************************************************

/* Function:
    void RTCx_Initialize( void )

   Summary:
     Initializes given instance of the RTC peripheral.

   Description:
     This function initializes the given instance of the RTC peripheral as
     configured by the user from within the MCC.  

   Precondition:
     None.

   Parameters:
    None.
  
   Returns:
    None.

   Example:
    <code>
    RTC0_Initialize();
    </code>

*/

void RTCx_Initialize( void );


/* Function:
	void RTCx_TimeSet( struct tm *time )
	
 Summary:
	Sets the Time for the RTC peripheral.
	
 Description:
	This function updates the time for RTC peripheral as
	configured by the user.
	
 Precondition:
	None.
	
 Parameters:
	time:- Pointer to struct tm.
 
 Returns:
	None.
 Example:
	<code>
		struct tm dateTime;
        //Hour
        dateTime.tm_hour = 12;
        //second
        dateTime.tm_sec = 0;
        //Minute
        dateTime.tm_min = 34;
        //Month
        dateTime.tm_mon = 11;
        //Year
        dateTime.tm_year = 2017;
        //day of the month
        dateTime.tm_mday = 14;
        //day of the week
        dateTime.tm_wday = 1;
        RTC0_TimeSet( &dateTime );
	</code>
 Remarks:
	The structure can be deleted once the API returns to free up the memory
 
*/
 void RTCx_TimeSet( struct tm *time );
 
/* Function:
	void RTCx_TimeGet( struct tm *time );
	
 Summary:
	Reads the current time
	
 Description:
	This function is used to read the current date and time from the RTC.
	
 Precondition:
	None.
	
 Parameters:
	time:- This is an output parameter that will be filled with the current date and time.
 
 Returns:
	None
 Example:
	<code>
		struct tm dateTime;
		//get the current date and time
		RTC0_TimeGet( &dateTime );
	</code>
*/
void RTCx_TimeGet( struct tm *time );
 
/* Function:
	void RTCx_AlarmSet( struct tm *alarmTime, RTC_ALARM_MASK mask );
	
 Summary:
	Sets up the Alarm
 
 Description:
	This function is used to set up the alarm time and Alarm mask based on
	user input.
	
 Precondition:
	None
	
 Parameters:
	alarmTime:- Alarm Time
	mask:-              Alarm mask to be used for notification
 
 Returns:
	None.
	
 Example:
	<code>
		struct tm alarmTime;
        //Hour
        alarmTime.tm_hour = 12;
        //second
        alarmTime.tm_sec = 0;
        //Minute
        alarmTime.tm_min = 34;
        //Month
        alarmTime.tm_mon = 11;
        //Year
        alarmTime.tm_year = 2017;
        //day of the month
        alarmTime.tm_mday = 14;
        //set up alarm for every month
        RTC0_AlarmSet( &alarmTime, RTC_ALARM_MASK_DDHHMISS );
	</code>
	
 Remark:
	The structure can be deleted once the API returns to free up the memory
*/
void RTCx_AlarmSet( struct tm *alarmTime, RTC_ALARM_MASK mask );

/* Function:
	void RTCx_InterruptDisable(RTC_INT_MASK interrupt)
	
 Summary:
	Disables the specified RTC interrupt
	
 Description:
	This function is used to disable a specific RTC interrupt source
	
 Precondition:
	None.
	
 Parameters:
	interrupt:- Interrupt source to be disabled.
 
 Returns:
	None.
 Example:
	<code>
		RTC0_InterruptDisable(RTC_INT_ALARM);
	</code>
 
*/
void RTCx_InterruptDisable(RTC_INT_MASK interrupt);
 
/* Function:
	void RTCx_InterruptEnable(RTC_INT_MASK interrupt)
	
 Summary:
	Enables the specified RTC interrupt
	
 Description:
	This function is used to enable a specific RTC interrupt source
	
 Precondition:
	None.
	
 Parameters:
	interrupt:- Interrupt source to be enabled.
 
 Returns:
	None.
 Example:
	<code>
		RTC0_InterruptEnable(RTC_INT_ALARM);
	</code>
 
*/
void RTCx_InterruptEnable(RTC_INT_MASK interrupt);
  
/* Function:
	void RTCx_CallbackRegister( RTC_CALLBACK callback, uintptr_t context )
	
 Summary:
	Sets the pointer to the function (and it's context) to be called when the
	Timeout events occur.
	
 Description:
	This function sets the pointer to a client function to be called "back"
	when the Alarm occurs. It also passes a context value that is passed into the
	function when it is called.
	This function is available only in interrupt mode of operation.
	
 Precondition:
	None.
	
 Parameters:
	callback - A pointer to a function with a calling signature defined
				by the RTC_CALLBACK data type.
	context - A value (usually a pointer) passed (unused) into the function
				identified by the callback parameter.
				
 Returns:
	None.
	
 Example:
	<code>
		RTC0_CallbackRegister(MyCallback, &myData);
	</code>
	
 Remarks:
	The context value may be set to NULL if it is not required. In this case the
	value NULL will be passed to the callback function.
	To disable the callback function, pass a NULL for the callback parameter.
	See the RTC_CALLBACK type definition for additional information.
*/
void RTCx_CallbackRegister( RTC_ALARM_CALLBACK callback, uintptr_t context );
 
// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility
 }
#endif
// DOM-IGNORE-END
#endif