/*******************************************************************************
  Interface definition of RTC PLIB.

  Company:
    Microchip Technology Inc.

  File Name:
    plib_rtc.h

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

#ifndef RTC_H    // Guards against multiple inclusion
#define RTC_H

#include <stdint.h>
#include <stdbool.h>
#include <stddef.h>
#include <time.h>
#include "plib_rtc_common.h"

#ifdef __cplusplus // Provide C++ Compatibility
 extern "C" {
#endif


// *****************************************************************************
// *****************************************************************************
// Section: Interface
// *****************************************************************************
// *****************************************************************************

/***************************** RTC API *******************************/
void RTC_Initialize( void );
bool RTC_TimeSet( struct tm *Time );
void RTC_TimeGet( struct tm *Time );
bool RTC_AlarmSet( struct tm *alarmTime, RTC_ALARM_MASK mask );
void RTC_CallbackRegister( RTC_CALLBACK callback, uintptr_t context );
void RTC_InterruptDisable(RTC_INT_MASK interrupt);
void RTC_InterruptEnable(RTC_INT_MASK interrupt);
	
#ifdef __cplusplus // Provide C++ Compatibility
 }
#endif

#endif
