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
    A simple loop process sets the LED for user feedback.  The user is prompted 
    to provide a user reset stimulus.  When the user reset is detected the configured 
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
    MsgSw3Prompt,
    MsgInputResult,
    MsgRstcResetInterruptOccurred,
    MsgSentinel,                        // must be last
} MsgId;

char * message[ MsgSentinel ] = {
    "",                                                                         // MsgNone
    "\r\n-------------------------------------------------------------\r\n",    // MsgBannerBreak
    "                          RSTC DEMO",                                      // MsgBannerTitle
    "Press the SW3 switch to create the user reset input\r\n",                  // MsgSw3Prompt
    "   The interrupt handler will change the LED and user message\r\n\r\n",    // MsgInputResult
    "RSTC reset interrupt occurred\r\n",                                        // MsgRstcResetInterruptOccurred
};

volatile LedColorType   ledColorType = LedOff;
volatile MsgId          msgId = MsgNone;

/////
void rstcCallback( uintptr_t context )
{
    (void) context;
    msgId = MsgRstcResetInterruptOccurred;
    if( LedBlueSolid == ledColorType )
    {
        ledColorType = LedGreenSolid;
    }
    else
    {
        ledColorType = LedBlueSolid;
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
    /* Initialize all modules */
    SYS_Initialize( NULL );

    RSTC_CallbackRegister( &rstcCallback, (uintptr_t) NULL );

    ledColorType = LedGreenFlash;

    msgId = MsgBannerBreak;
    showMsg();
    msgId = MsgBannerTitle;
    showMsg();
    msgId = MsgBannerBreak;
    showMsg();
    msgId = MsgSw3Prompt;
    showMsg();
    msgId = MsgInputResult;
    showMsg();

    while( 1 )
    {
        ledUpdate();
        showMsg();
    }

    /* Execution should not come here during normal operation */
    return( EXIT_FAILURE );
}


/*******************************************************************************
 End of File
*/
