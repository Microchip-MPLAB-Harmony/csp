/*******************************************************************************
  Main Source File

  Company:
    Microchip Technology Inc.

  File Name:
    main_sam_9x60.c

  Summary:
    This file contains a demonstration of the wdt_44154 peripheral used in the
    SAM_9x60.

  Description:
    A simple loop process blinks the LED for user feedback.  Within the loop
    the watch dog receives a 'pet' until the user presses a test push button. 
    The process will then stop the watch dog petting and the processor will 
    reset after the configured delay.

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
    MsgPettingWatchDog,
    MsgPettingWatchDogStopped,
    MsgWdtEarlyResetOccurred,
    MsgWdtWindowLevelOccurred,
    MsgWdtWindowPeriodOccurred,
    MsgWdtUnknownInterruptOccurred,
    MsgSentinel,                        // must be last
} MsgId;

char * message[ MsgSentinel ] = {
    "",                                                                         // MsgNone
    "\r\n-------------------------------------------------------------\r\n",    // MsgBannerBreak
    "                          WDT DEMO",                                       // MsgBannerTitle
    "Press SW1 to create a process starvation and a watch dog reset\r\n",       // MsgSw1Prompt
    "Petting watch dog...\r\n",                                                 // MsgPettingWatchDog
    "Petting watch dog STOPPED!...\r\n",                                        // MsgPettingWatchDogStopped
    "WDT early reset interrupt occurred\r\n",                                   // MsgWdtEarlyResetOccurred
    "WDT window level interrupt occurred\r\n",                                  // MsgWdtWindowLevelOccurred
    "WDT window period interrupt occurred\r\n",                                 // MsgWdtWindowPeriodOccurred
    "WDT unknown interrupt occurred!\r\n",                                      // MsgWdtUnknownInterruptOccurred
};

volatile bool           petWatchDog = true;
volatile LedColorType   ledColorType = LedOff;
volatile MsgId          msgId = MsgNone;

/////
void sw1Callback( PIO_PIN pin, uintptr_t context )
{
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

void wdtCallback( uintptr_t context, uint32_t interruptStatus )
{
    (void) context;
    if( interruptStatus & WDT_ISR_RPTHINT_Msk )
    {
        msgId = MsgWdtEarlyResetOccurred;
        ledColorType = LedRedSolid;
    }
    else if( interruptStatus & WDT_ISR_LVLINT_Msk )
    {
        msgId = MsgWdtWindowLevelOccurred;
        ledColorType = LedRedFlash;
    }
    else if( interruptStatus & WDT_ISR_PERINT_Msk )
    {
        msgId = MsgWdtWindowPeriodOccurred;
        ledColorType = LedRedSolid;
    }
    else
    {
        msgId = MsgWdtUnknownInterruptOccurred;
    }
}

void ledUpdate( void )
{
    static LedColorType lastledColorType = LedInvalid;
    if( ledColorType != lastledColorType )
    {
        lastledColorType = ledColorType;
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
    volatile bool   workToDo = true;    // avoid unreachable code warning
    uint32_t        pitMs = 500;
    
    while( !workToDo )
    {                                   // possible debug entry point
        ;   // spin lock
    }
    /* Initialize all modules */
    SYS_Initialize( NULL );

    PIO_PinInterruptCallbackRegister( SW1_PIN, &sw1Callback, (uintptr_t) NULL );
    PIO_PinInterruptEnable( SW1_PIN );
    WDT_CallbackRegister( wdtCallback, NULL );

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

    // Watch dog pet and led toggle with delay for reasonable blink
    while( workToDo )
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
