/*******************************************************************************
  Watchdog Timer PLIB.

  Company:
    Microchip Technology Inc.

  File Name:
    plib_wdt.c

  Summary:
    Interface definition of WDT PLIB.

  Description:
    This implements the interface for the WDT Plib based on wdt_44154.
    It allows user to setup timeout duration and restart watch dog timer.
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

#include "device.h"
#include "plib_wdt.h"


void WDT_Initialize( void )
{
    // insure writes will take effect -- unlock the registers
    WDT_REGS->WDT_CR = WDT_CR_KEY_PASSWD;
    WDT_Disable();
    // set counter values:
    //    WDT_WLR_RPTH =   1000 (mSecs) = 250 (counts)
    //    WDT_WLR_PERIOD = 16000 (mSecs) = 4000 (counts)
    //    WDT_ILR_LVLTH =  15000 (mSecs) = 3750 (counts)
    WDT_REGS->WDT_WLR = WDT_WLR_RPTH( 250 ) | WDT_WLR_PERIOD( 4000 );
    WDT_REGS->WDT_ILR = WDT_ILR_LVLTH( 3750 );
    // clear interrupt status
    (void) WDT_REGS->WDT_ISR;
    // enable appropriate interrupts
    WDT_REGS->WDT_IER = 0;
    // enable WDT and set other mode bits desired 
    WDT_REGS->WDT_MR =  0 | WDT_MR_WDIDLEHLT_Msk | WDT_MR_WDDBGHLT_Msk;
}

void WDT_Clear( void )
{
    // When WDT is enabled, clear and reset the watch dog timer before the period 
    // counter reaches its floor.  But, not within three clock cycles of last restart, or before the
    // repeat threshold, currently 250 counts, has expired.
    // Note: Due to the asynchronous operation of the WDT with respect to the rest of the chip
    //    a minimum of two, possibly three, value register reads must be performed. 
    if( !(WDT_MR_WDDIS_Msk & WDT_REGS->WDT_MR) )
    {
        const uint32_t  minWait = 250;
        uint32_t        countDownValue = WDT_VR_COUNTER( WDT_REGS->WDT_VR );
        if( countDownValue != WDT_VR_COUNTER( WDT_REGS->WDT_VR ) )
            countDownValue = WDT_VR_COUNTER( WDT_REGS->WDT_VR );
    
        // initial WDT_WLR_PERIOD = 4000 (counts)
        if( 4000 > (minWait + countDownValue) )
        {
            WDT_REGS->WDT_CR = WDT_CR_KEY_PASSWD | WDT_CR_WDRSTT_Msk;
        }
    }
}

void WDT_Enable( void )
{   // Note: WDT_MR modifications should have at least 3 slow clock cycles between updates.
    // An interval check is not in place here and should be enforced externally.

    // enable WDT
    WDT_REGS->WDT_MR &= ~WDT_MR_WDDIS_Msk;
    // clear interrupt status
    (void) WDT_REGS->WDT_ISR;
    // enable appropriate interrupts
    WDT_REGS->WDT_IER = 0;
}

void WDT_Disable( void )
{   // Note: WDT_MR modifications should have at least 3 slow clock cycles between updates.
    // An interval check is not in place here and should be enforced externally.

    // disable all interrupts
    WDT_REGS->WDT_IDR = WDT_IDR_LVLINT_Msk | WDT_IDR_RPTHINT_Msk | WDT_IDR_PERINT_Msk;
    // disable WDT
    WDT_REGS->WDT_MR |= WDT_MR_WDDIS_Msk;
}

