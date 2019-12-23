/*******************************************************************************
  Watchdog Timer PLIB.

  Company:
    Microchip Technology Inc.

  File Name:
    plib_wdt.c

  Summary:
    Interface definition of WDT PLIB.

  Description:
    This file defines the interface for the WDT Plib.
    It allows user to setup timeout duration and restart watch dog timer.
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

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

#include "plib_wdt.h"

WDT_CALLBACK_OBJECT wdtCallbackObj;

// *****************************************************************************
// *****************************************************************************
// Section: WDT Interface Implementations
// *****************************************************************************
// *****************************************************************************

void WDT_Enable( void )
{
    /* Checking if Always On Bit is Enabled */
    if((WDT_REGS->WDT_CTRLA & WDT_CTRLA_ALWAYSON_Msk) != WDT_CTRLA_ALWAYSON_Msk)
    {
        /* Enable Watchdog Timer */
        WDT_REGS->WDT_CTRLA |= WDT_CTRLA_ENABLE_Msk;

        /* Wait for synchronization */
        while(WDT_REGS->WDT_SYNCBUSY);
    }

    /* Enable early warning interrupt */
    WDT_REGS->WDT_INTENSET = WDT_INTENSET_EW_Msk;
}

void WDT_Disable( void )
{
    /* Disable Watchdog Timer */
    WDT_REGS->WDT_CTRLA &= ~(WDT_CTRLA_ENABLE_Msk);

    /* Disable Early Watchdog Interrupt */
    WDT_REGS->WDT_INTENCLR = WDT_INTENCLR_EW_Msk;
}

void WDT_Clear( void )
{
    if ((WDT_REGS->WDT_SYNCBUSY & WDT_SYNCBUSY_CLEAR_Msk) != WDT_SYNCBUSY_CLEAR_Msk)
    {
        /* Clear WDT and reset the WDT timer before the
        timeout occurs */
        WDT_REGS->WDT_CLEAR = WDT_CLEAR_CLEAR_KEY;
    }
}

void WDT_CallbackRegister( WDT_CALLBACK callback, uintptr_t context)
{
    wdtCallbackObj.callback = callback;

    wdtCallbackObj.context = context;
}

void WDT_InterruptHandler( void )
{
    /* Clear Early Watchdog Interrupt */
    WDT_REGS->WDT_INTFLAG = WDT_INTFLAG_EW_Msk;

    if( wdtCallbackObj.callback != NULL )
    {
        wdtCallbackObj.callback(wdtCallbackObj.context);
    }
}
