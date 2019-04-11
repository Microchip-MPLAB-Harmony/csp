/*******************************************************************************
  Main Source File

  Company:
    Microchip Technology Inc.

  File Name:
    main_sam_9x60.c

  Summary:
    This file contains a demonstration of the rtc_44154 peripheral used in the
    SAM_9x60.

  Description:
    A simple loop process sets the LED for user feedback.  The user is prompted 
    and told the alarm settings.  When the user alarm occurs the configured 
    interrupt handler signals a change to the LED color and user messaging.

*******************************************************************************/

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

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
#include <stddef.h>                     // NULL
#include <stdbool.h>                    // true
#include <stdlib.h>                		// EXIT_FAILURE
#include <string.h>                     // strlen
#include "definitions.h"                // SYS function prototypes

typedef enum {
    LedInvalid = -1,
    LedOff,
    LedRedFlash,    LedGreenFlash,  LedBlueFlash,
    LedRedSolid,    LedGreenSolid,  LedBlueSolid,
}  LedColorType;

typedef enum {
    MsgNone,
    MsgBannerBreak,
    MsgBannerTitle,
    MsgPrompt,
    MsgInputResult,
    MsgRtcInterruptOccurred,
    MsgRtcErrorSettingTime,
    MsgRtcErrorSettingAlarm,
    MsgRtcStartTime,
    MsgRtcAlarmSetting,
    MsgInVariableBuffer,
    MsgSentinel,                        // must be last
} MsgId;

char msgVariableBuffer[ 80 ];
char * message[ MsgSentinel ] = {
    "",                                                                         // MsgNone
    "\r\n-------------------------------------------------------------\r\n",    // MsgBannerBreak
    "                          RTC DEMO",                                       // MsgBannerTitle
    "Wait for the alarm after midnight\r\n",                                    // MsgPrompt
    "   The interrupt handler will change the LED and user message\r\n\r\n",    // MsgInputResult
    "RTC interrupt occurred!\r\n",                                              // MsgRtcInterruptOccurred
    "RTC error setting time\r\n",                                               // MsgRtcErrorSettingTime
    "RTC error setting alarm\r\n",                                              // MsgRtcErrorSettingAlarm
    "RTC starting: 03-31-2019 23:59:50 Sunday\r\n",                             // MsgRtcStartTime
    "RTC alarm:    04-01-2019 00:00:10 Monday\r\n",                             // MsgRtcAlarmSetting
    msgVariableBuffer,                                                          // MsgInVariableBuffer
};

char * dayOfWeek[] = { 
    "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday" 
};

volatile LedColorType   ledColorType = LedOff;
volatile MsgId          msgId = MsgNone;
volatile MsgId          interruptMsgId = MsgNone;
/////
void rtcCallback( uint32_t cause, uintptr_t context )
{
    (void) context;
	if( cause & RTC_INT_ALARM )
	{
        interruptMsgId = MsgRtcInterruptOccurred;
        if( LedBlueSolid == ledColorType )
        {
            ledColorType = LedGreenSolid;
        }
        else
        {
            ledColorType = LedBlueSolid;
        }
	}
}

void ledUpdate( void )
{
    static LedColorType lastLedColorType = LedInvalid;
    if( ledColorType != lastLedColorType )
    {
        lastLedColorType = ledColorType;
        LED_RED_Clear();
        LED_GREEN_Clear();
        LED_BLUE_Clear();
    }
    
    switch( ledColorType )
    {
        case LedRedFlash:
            LED_RED_Toggle();
            break;
        case LedGreenFlash:
            LED_GREEN_Toggle();
            break;
        case LedBlueFlash:
            LED_BLUE_Toggle();
            break;
        case LedRedSolid:
            LED_RED_Set();
            break;
        case LedGreenSolid:
            LED_GREEN_Set();
            break;
        case LedBlueSolid:
            LED_BLUE_Set();
            break;
        default:
        case LedInvalid:
        case LedOff:
            LED_RED_Clear();
            LED_GREEN_Clear();
            LED_BLUE_Clear();
            break;
    }
}

void showMsg( void )
{
    if( MsgNone != msgId )
    {
        int jj = strlen( message[ msgId ] );
        while( !DBGU_Write( (void *) message[ msgId ], jj ) )
        {
            ;   // spin lock
        }
        msgId = MsgNone;
    }
}

// *****************************************************************************
// *****************************************************************************
// Section: Main Entry Point
// *****************************************************************************
// *****************************************************************************
int main( void )
{
    struct tm       currentTime;
    struct tm       alarmTime;
    int             lastSecond = 61;    // an invalid value

    /* Initialize all modules */
    SYS_Initialize( NULL );

    RTC_CallbackRegister( rtcCallback, (uintptr_t) NULL );

    ledColorType = LedGreenFlash;
    
    msgId = MsgBannerBreak;
    showMsg();
    msgId = MsgBannerTitle;
    showMsg();
    msgId = MsgBannerBreak;
    showMsg();
    msgId = MsgPrompt;
    showMsg();
    msgId = MsgInputResult;
    showMsg();
    msgId = MsgRtcStartTime;
    showMsg();
    msgId = MsgRtcAlarmSetting;
    showMsg();

    // Using a 24hr clock, with 0 based day of week and month (0=Sunday, 0=January)
    // 3-31-2019 23:59:50 Sunday
    currentTime.tm_hour = 23;
    currentTime.tm_min = 59;
    currentTime.tm_sec = 50;
    currentTime.tm_year = 119;
    currentTime.tm_mon = 2;
    currentTime.tm_mday = 31;
    currentTime.tm_wday = 0;
    // 4-01-2019 00:00:10 Monday
    alarmTime.tm_hour = 00;
    alarmTime.tm_min = 00;
    alarmTime.tm_sec = 10;
    alarmTime.tm_year = 119;
    alarmTime.tm_mon = 3;
    alarmTime.tm_mday = 1;
    alarmTime.tm_wday = 1;

    if( false == RTC_TimeSet( &currentTime ) )
    {
        msgId = MsgRtcErrorSettingTime;
        showMsg();
        while( 1 )
        {
            ;       // spin lock
        }
    }
    
    if( false == RTC_AlarmSet( &alarmTime, RTC_ALARM_MASK_HHMISS ) )
    {
        msgId = MsgRtcErrorSettingAlarm;
        showMsg();
        while( 1 )
        {
            ;       // spin lock
        }
    }
    
    while( 1 )
    {
        RTC_TimeGet( &currentTime );
        if( lastSecond != currentTime.tm_sec )
        {
            lastSecond = currentTime.tm_sec;
            msgId = interruptMsgId;
            interruptMsgId = MsgNone;
            if( MsgNone == msgId )
            {
                msgId = MsgInVariableBuffer;
                sprintf( msgVariableBuffer, "%s %02d/%02d/%04d, %02d:%02d:%02d\r\n",
                            dayOfWeek[ currentTime.tm_wday ],
                            1 + currentTime.tm_mon,
                            currentTime.tm_mday,
                            1900 + currentTime.tm_year,
                            currentTime.tm_hour,
                            currentTime.tm_min,
                            lastSecond 
                            );
            }
        }
        showMsg();
    }

    /* Execution should not come here during normal operation */
    return( EXIT_FAILURE );
}


/*******************************************************************************
 End of File
*/
