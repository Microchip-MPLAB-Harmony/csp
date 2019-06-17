/*******************************************************************************
  Real Time Counter (RTC) PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_rtc.h

  Summary:
    RTC PLIB Header file

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

#ifndef PLIB_RTC_H
#define PLIB_RTC_H

#include "device.h"
#include <stddef.h>
#include <stdbool.h>
#include <stdint.h>
#include <time.h>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility
extern "C" {
#endif
// DOM-IGNORE-END


typedef enum
{
    RTC_ALARM_MASK_SS = 0x1,    //Alarm every minute
    RTC_ALARM_MASK_MMSS,        //Alarm every Hour
    RTC_ALARM_MASK_HHMMSS,      //Alarm Every Day
    RTC_ALARM_MASK_DDHHMMSS,    //Alarm Every Month
    RTC_ALARM_MASK_MMDDHHMMSS,  //Alarm Every year
    RTC_ALARM_MASK_YYMMDDHHMMSS //Alarm Once
} RTC_ALARM_MASK;

typedef enum
{
    RTC_CLOCK_INT_MASK_PER0 = RTC_MODE2_INTENSET_PER0_Msk,
    RTC_CLOCK_INT_MASK_PER1 = RTC_MODE2_INTENSET_PER1_Msk,
    RTC_CLOCK_INT_MASK_PER2 = RTC_MODE2_INTENSET_PER2_Msk,
    RTC_CLOCK_INT_MASK_PER3 = RTC_MODE2_INTENSET_PER3_Msk,
    RTC_CLOCK_INT_MASK_PER4 = RTC_MODE2_INTENSET_PER4_Msk,
    RTC_CLOCK_INT_MASK_PER5 = RTC_MODE2_INTENSET_PER5_Msk,
    RTC_CLOCK_INT_MASK_PER6 = RTC_MODE2_INTENSET_PER6_Msk,
    RTC_CLOCK_INT_MASK_PER7 = RTC_MODE2_INTENSET_PER7_Msk,
    RTC_CLOCK_INT_MASK_ALARM0 = RTC_MODE2_INTENSET_ALARM0_Msk,
    RTC_CLOCK_INT_MASK_ALARM1 = RTC_MODE2_INTENSET_ALARM1_Msk,
    RTC_CLOCK_INT_MASK_TAMPER = RTC_MODE2_INTENSET_TAMPER_Msk,
    RTC_CLOCK_INT_MASK_OVF = RTC_MODE2_INTENSET_OVF_Msk,
   /* Force the compiler to reserve 32-bit memory for enum */
    RTC_CLOCK_INT_MASK_INVALID = 0xFFFFFFFF
} RTC_CLOCK_INT_MASK;

typedef enum
{
    BACKUP_REGISTER_0 = 0,
    BACKUP_REGISTER_1 = 1,
    BACKUP_REGISTER_2 = 2,
    BACKUP_REGISTER_3 = 3,
    BACKUP_REGISTER_4 = 4,
    BACKUP_REGISTER_5 = 5,
    BACKUP_REGISTER_6 = 6,
    BACKUP_REGISTER_7 = 7
} BACKUP_REGISTER;
typedef enum
{
    TAMPER_CHANNEL_0 = 0,
    TAMPER_CHANNEL_1 = 1,
    TAMPER_CHANNEL_2 = 2,
    TAMPER_CHANNEL_3 = 3,
    TAMPER_CHANNEL_4 = 4
} TAMPER_CHANNEL;
typedef void (*RTC_CALLBACK)( RTC_CLOCK_INT_MASK intCause, uintptr_t context );

typedef struct
{
    /* RTC Clock*/
    RTC_CLOCK_INT_MASK intCause;
    RTC_CALLBACK alarmCallback;
    uintptr_t context;
} RTC_OBJECT;

void RTC_Initialize(void);
bool RTC_RTCCTimeSet (struct tm * initialTime );
void RTC_RTCCTimeGet ( struct tm * currentTime );
bool RTC_RTCCAlarm0Set ( struct tm * alarmTime, RTC_ALARM_MASK mask );
bool RTC_RTCCAlarm1Set ( struct tm * alarmTime, RTC_ALARM_MASK mask );
void RTC_BackupRegisterSet( BACKUP_REGISTER reg, uint32_t value );
uint32_t RTC_BackupRegisterGet( BACKUP_REGISTER reg );
TAMPER_CHANNEL RTC_TamperSourceGet( void );
void RTC_RTCCTimeStampGet( struct tm * timeStamp );
void RTC_RTCCCallbackRegister ( RTC_CALLBACK callback, uintptr_t context);

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility
}
#endif
// DOM-IGNORE-END

#endif /* PLIB_RTC_H */
