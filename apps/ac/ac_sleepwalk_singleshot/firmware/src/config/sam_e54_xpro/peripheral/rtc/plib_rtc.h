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

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility
extern "C" {
#endif
// DOM-IGNORE-END

/* Frequency of Counter Clock for RTC */
#define RTC_COUNTER_CLOCK_FREQUENCY        (1024 / (1 << (0x1 - 1)))

typedef enum
{
    RTC_PER0_MASK = 0x0001,
    RTC_PER1_MASK = 0x0002,
    RTC_PER2_MASK = 0x0004,
    RTC_PER3_MASK = 0x0008,
    RTC_PER4_MASK = 0x0010,
    RTC_PER5_MASK = 0x0020,
    RTC_PER6_MASK = 0x0040,
    RTC_PER7_MASK = 0x0080
} RTC_PERIODIC_INT_MASK;
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


void RTC_Initialize(void);
bool RTC_PeriodicIntervalHasCompleted ( RTC_PERIODIC_INT_MASK period );
bool RTC_Timer32CounterHasOverflowed ( void );
bool RTC_Timer32Compare0HasMatched( void );
bool RTC_Timer32Compare1HasMatched( void );
void RTC_Timer32Start ( void );
void RTC_Timer32Stop ( void );
void RTC_Timer32CounterSet ( uint32_t count );
uint32_t RTC_Timer32CounterGet ( void );
uint32_t RTC_Timer32FrequencyGet ( void );
void RTC_Timer32Compare0Set ( uint32_t compareValue );
void RTC_Timer32Compare1Set ( uint32_t compareValue );
uint32_t RTC_Timer32PeriodGet ( void );
void RTC_BackupRegisterSet( BACKUP_REGISTER reg, uint32_t value );
uint32_t RTC_BackupRegisterGet( BACKUP_REGISTER reg );
TAMPER_CHANNEL RTC_TamperSourceGet( void );
uint32_t RTC_Timer32TimeStampGet( void );

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility
}
#endif
// DOM-IGNORE-END

#endif /* PLIB_RTC_H */
