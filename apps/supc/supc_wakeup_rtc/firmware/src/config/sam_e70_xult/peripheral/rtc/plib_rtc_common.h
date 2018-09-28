/*******************************************************************************
  Interface definition of RTC PLIB.

  Company:
    Microchip Technology Inc.

  File Name:
    plib_rtc_common.h

  Summary:
    Interface definition of the Real Time Counter Plib (RTC).

  Description:
    This file defines the interface for the RTC Plib.
    It allows user to setup alarm duration and access current date and time.
*******************************************************************************/

/*******************************************************************************
Copyright (c) 2016 released Microchip Technology Inc.  All rights reserved.

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

#ifndef PLIB_RTC_COMMON_H    // Guards against multiple inclusion
#define PLIB_RTC_COMMON_H

#include <stdint.h>
#include <stdbool.h>
#include <stddef.h>
#include <time.h>

#ifdef __cplusplus // Provide C++ Compatibility
 extern "C" {
#endif


// *****************************************************************************
// *****************************************************************************
// Section: Interface
// *****************************************************************************
// *****************************************************************************

typedef void (*RTC_CALLBACK)(uintptr_t context, uint32_t int_cause);


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

typedef enum 
{
    RTC_INT_ALARM = 0x02,          // Alarm Event
    RTC_INT_TIME = 0x08 ,          // Time Event
    RTC_INT_CALENDAR = 0x10,          // Calendar enable
} RTC_INT_MASK;	

typedef struct
{
    RTC_CALLBACK          callback; 
    uintptr_t               context;
} RTC_OBJECT ;


	
#ifdef __cplusplus // Provide C++ Compatibility
 }
#endif

#endif
