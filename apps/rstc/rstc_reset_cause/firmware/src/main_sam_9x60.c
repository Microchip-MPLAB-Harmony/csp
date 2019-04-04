/*******************************************************************************
  Main Source File

  Company:
    Microchip Technology Inc.

  File Name:
    main_sam_9x60.c

  Summary:
    This file contains a demonstration of the rstc_44161 peripheral used in the
    SAM_9x60.

  Description:
    User prompts and the reason for the last reset are displayed.
    A simple loop process blinks the LED for user feedback.  Within the loop
    the watch dog receives a 'pet' until the user presses a test push button. 

    The PIT is used to provide a delay for the led blink and is not otherwise
    applicable to the demonstration

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
    MsgSw1Prompt,
    MsgSw3Prompt,
    MsgSwInputResult,
    MsgPettingWatchDog,
    MsgPettingWatchDogStopped,
    MsgRstcCausedByGeneralReset,
    MsgRstcCausedByWakeUpReset,
    MsgRstcCausedByWatchDogReset,
    MsgRstcCausedBySoftwareReset,
    MsgRstcCausedByUserReset,
    MsgRstcCausedByCpuFailureReset,
    MsgRstcCausedByXtalFailureReset,
    MsgRstcCauseUnknown,
    MsgSentinel,                        // must be last
} MsgId;

char * message[ MsgSentinel ] = {
    "",                                                                         // MsgNone
    "\r\n-------------------------------------------------------------\r\n",    // MsgBannerBreak
    "                          RSTC DEMO",                                      // MsgBannerTitle
    "Press SW1 to create a process starvation and a watch dog reset\r\n",       // MsgSw1Prompt
    "Press the SW3 switch to create the user reset input\r\n",                  // MsgSw3Prompt
    "   The SW1 interrupt handler will change the LED and user message\r\n\r\n",// MsgSwInputResult
    "Petting watch dog...\r\n",                                                 // MsgPettingWatchDog
    "Petting watch dog STOPPED!...\r\n",                                        // MsgPettingWatchDogStopped
    "Last reset caused by general reset -- first power\r\n",                    // MsgRstcCausedByGeneralReset
    "Last reset caused by wake up -- return from backup\r\n",                   // MsgRstcCausedByWakeUpReset
    "Last reset caused by watch dog reset\r\n",                                 // MsgRstcCausedByWatchDogReset
    "Last reset caused by software reset -- software instruction\r\n",          // MsgRstcCausedBySoftwareReset
    "Last reset caused by user reset -- NRST pin detected low\r\n",             // MsgRstcCausedByUserReset
    "Last reset caused by cpu failure\r\n",                                     // MsgRstcCausedByCpuFailureReset
    "Last reset caused by slck xtal failure\r\n",                               // MsgRstcCausedByXtalFailureReset
    "Last reset cause is unknown\r\n",                                          // MsgRstcCauseUnknown
};

volatile bool           petWatchDog = true;
volatile LedColorType   ledColorType = LedOff;
volatile MsgId          msgId = MsgNone;

/////
void sw1Callback( PIO_PIN pin, uintptr_t context )
{
    (void) pin;
    (void) context;

    petWatchDog = !petWatchDog;
    if( petWatchDog )
    {
        ledColorType = LedGreenFlash;
        msgId = MsgPettingWatchDog;
    } 
    else
    {
        ledColorType = LedBlueFlash;
        msgId = MsgPettingWatchDogStopped;
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
    uint32_t pitMs = 500;
    
    /* Initialize all modules */
    SYS_Initialize( NULL );

    PIO_PinInterruptCallbackRegister( SW1_PIN, &sw1Callback, (uintptr_t) NULL );
    PIO_PinInterruptEnable( SW1_PIN );

    PIT_DelayMs( pitMs );
    ledColorType = LedGreenFlash;
    petWatchDog = true;

    msgId = MsgBannerBreak;
    showMsg();
    msgId = MsgBannerTitle;
    showMsg();
    msgId = MsgBannerBreak;
    showMsg();
    msgId = MsgSw1Prompt;
    showMsg();
    msgId = MsgSw3Prompt;
    showMsg();
    msgId = MsgSwInputResult;
    showMsg();

    switch( RSTC_ResetCauseGet() )
    {
        case RSTC_GENERAL_RESET:
            msgId = MsgRstcCausedByGeneralReset;
            break;
        case RSTC_WAKEUP_RESET:
            msgId = MsgRstcCausedByWakeUpReset;
            break;
        case RSTC_WATCHDOG_RESET:
            msgId = MsgRstcCausedByWatchDogReset;
            break;
        case RSTC_SOFTWARE_RESET:
            msgId = MsgRstcCausedBySoftwareReset;
            break;
        case RSTC_USER_RESET:
            msgId = MsgRstcCausedByUserReset;
            break;
        case RSTC_CPU_FAIL_RESET:
            msgId = MsgRstcCausedByCpuFailureReset;
            break;
        case RSTC_SLCK_XTAL_RESET:
            msgId = MsgRstcCausedByXtalFailureReset;
            break;
        default:
            msgId = MsgRstcCauseUnknown;
            break;
    }
    showMsg();

    // Watch dog pet and led toggle with delay for reasonable blink
    while( 1 )
    {
        PIT_DelayMs( pitMs );
        ledUpdate();
        showMsg();
        if( petWatchDog )
        {
            WDT_Clear();    
        }
    }

    /* Execution should not come here during normal operation */
    return( EXIT_FAILURE );
}


/*******************************************************************************
 End of File
*/
