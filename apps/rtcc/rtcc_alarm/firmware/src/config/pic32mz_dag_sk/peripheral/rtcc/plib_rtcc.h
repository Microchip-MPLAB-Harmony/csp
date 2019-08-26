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

#ifndef PLIB_RTCC_H
#define PLIB_RTCC_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

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
// Section: Data Types
// *****************************************************************************
// *****************************************************************************

typedef enum
{
    RTCC_ALARM_MASK_HALF_SECOND = 0x00,   // Every half-second
    RTCC_ALARM_MASK_SECOND = 0x01,        // Every second
    RTCC_ALARM_MASK_10_SECONDS = 0x02,    // Every 10 seconds
    RTCC_ALARM_MASK_SS = 0x03,            // Every minute
    RTCC_ALARM_MASK_10_MINUTES = 0x04,    // Every 10 minutes
    RTCC_ALARM_MASK_HOUR = 0x05,          // Every hour
    RTCC_ALARM_MASK_HHMISS = 0x06,        // Once a day
    RTCC_ALARM_MASK_WEEK = 0x07,          // Once a week
    RTCC_ALARM_MASK_MONTH = 0x08,         // Once a month
    RTCC_ALARM_MASK_YEAR = 0x09,          // Once a year
    RTCC_ALARM_MASK_OFF = 0xFF            // Disabled

} RTCC_ALARM_MASK;

typedef enum
{
    RTCC_INT_ALARM = 0x40

} RTCC_INT_MASK;

typedef void (*RTCC_CALLBACK)( uintptr_t context );

// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************

void RTCC_Initialize( void );

bool RTCC_TimeSet( struct tm *Time );

void RTCC_TimeGet(struct tm  *Time );

bool RTCC_AlarmSet( struct tm *alarmTime, RTCC_ALARM_MASK alarmFreq );

void RTCC_CallbackRegister( RTCC_CALLBACK callback, uintptr_t context );

void RTCC_InterruptEnable( RTCC_INT_MASK interrupt );

void RTCC_InterruptDisable( RTCC_INT_MASK interrupt );

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END

#endif // PLIB_RTCC_H
