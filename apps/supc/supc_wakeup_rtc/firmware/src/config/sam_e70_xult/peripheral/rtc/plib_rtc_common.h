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

typedef void (*RTC_CALLBACK)(uint32_t int_cause, uintptr_t context);


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
    uintptr_t             context;
} RTC_OBJECT ;


	
#ifdef __cplusplus // Provide C++ Compatibility
 }
#endif

#endif
