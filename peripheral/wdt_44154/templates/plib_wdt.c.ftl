/*******************************************************************************
  Watchdog Timer PLIB.

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${WDT_INSTANCE_NAME?lower_case}.c

  Summary:
    Interface definition of ${WDT_INSTANCE_NAME} PLIB.

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
#include "plib_${WDT_INSTANCE_NAME?lower_case}.h"

<#if WDT_EARLY_RESET_ACTION == 'Interrupt'
    || WDT_LEVEL_EXPIRATION == 'Interrupt'
    || WDT_PERIOD_EXPIRATION == 'Interrupt'
    >
    <#lt>// private structure type
    <#lt>typedef struct
    <#lt>{
    <#lt>    WDT_CALLBACK    callback; 
    <#lt>    uintptr_t       context;
    <#lt>} WDT_CALLBACK_OBJECT;
    
    <#lt>WDT_CALLBACK_OBJECT ${WDT_INSTANCE_NAME?lower_case}CallbackObj;
        
    <#lt>void ${WDT_INSTANCE_NAME}_CallbackRegister( WDT_CALLBACK callback, uintptr_t context )
    <#lt>{
    <#lt>    ${WDT_INSTANCE_NAME?lower_case}CallbackObj.callback = callback;
    <#lt>    ${WDT_INSTANCE_NAME?lower_case}CallbackObj.context =  context;
    <#lt>}

    <#lt>void ${WDT_INSTANCE_NAME}_InterruptHandler( void )
    <#lt>{
    <#lt>    // Capture and clear interrupt status
    <#lt>    uint32_t interruptStatus = ${WDT_INSTANCE_NAME}_REGS->WDT_ISR;

    <#lt>    if( interruptStatus && (${WDT_INSTANCE_NAME?lower_case}CallbackObj.callback != NULL) )
    <#lt>    {
    <#lt>        ${WDT_INSTANCE_NAME?lower_case}CallbackObj.callback( ${WDT_INSTANCE_NAME?lower_case}CallbackObj.context, interruptStatus );
    <#lt>    }
    <#lt>}
</#if>

void ${WDT_INSTANCE_NAME}_Initialize( void )
{
    // insure writes will take effect -- unlock the registers
    ${WDT_INSTANCE_NAME}_REGS->WDT_CR = WDT_CR_KEY_PASSWD;
    ${WDT_INSTANCE_NAME}_Disable();
    // set counter values:
    //    WDT_WLR_RPTH =   ${WDT_EARLY_RESET_THRESHOLD_MILLISECONDS} (mSecs) = ${WDT_EARLY_RESET_THRESHOLD_COUNT} (counts)
    //    WDT_WLR_PERIOD = ${WDT_PERIOD_MILLISECONDS} (mSecs) = ${WDT_PERIOD_COUNT} (counts)
    //    WDT_ILR_LVLTH =  ${WDT_LEVEL_THRESHOLD_MILLISECONDS} (mSecs) = ${WDT_LEVEL_THRESHOLD_COUNT} (counts)
    ${WDT_INSTANCE_NAME}_REGS->WDT_WLR = WDT_WLR_RPTH( ${WDT_EARLY_RESET_THRESHOLD_COUNT} ) | WDT_WLR_PERIOD( ${WDT_PERIOD_COUNT} );
    ${WDT_INSTANCE_NAME}_REGS->WDT_ILR = WDT_ILR_LVLTH( ${WDT_LEVEL_THRESHOLD_COUNT} );
    // clear interrupt status
    (void) ${WDT_INSTANCE_NAME}_REGS->WDT_ISR;
    // enable appropriate interrupts
    ${WDT_INSTANCE_NAME}_REGS->WDT_IER = 0${(WDT_LEVEL_EXPIRATION=='Interrupt')?then(' | WDT_IER_LVLINT_Msk','')}${(WDT_EARLY_RESET_ACTION=='Interrupt')?then(' | WDT_IER_RPTHINT_Msk','')}${(WDT_PERIOD_EXPIRATION=='Interrupt')?then(' | WDT_IER_PERINT_Msk','')};
    // enable WDT and set other mode bits desired 
    ${WDT_INSTANCE_NAME}_REGS->WDT_MR =  0${WDT_STOP_WHEN_IDLE?then(' | WDT_MR_WDIDLEHLT_Msk','')}${WDT_STOP_WHEN_DEBUGGING?then(' | WDT_MR_WDDBGHLT_Msk','')}${(WDT_EARLY_RESET_ACTION=='Reset')?then(' | WDT_MR_RPTHRST_Msk','')}${(WDT_PERIOD_EXPIRATION=='Reset')?then(' | WDT_MR_PERIODRST_Msk','')};
}

void ${WDT_INSTANCE_NAME}_Clear( void )
{
    // When WDT is enabled, clear and reset the watch dog timer before the period 
    // counter reaches its floor.  But, not within three clock cycles of last restart, or before the
    // repeat threshold, currently ${WDT_EARLY_RESET_THRESHOLD_COUNT} counts, has expired.
    // Note: Due to the asynchronous operation of the WDT with respect to the rest of the chip
    //    a minimum of two, possibly three, value register reads must be performed. 
    if( !(WDT_MR_WDDIS_Msk & ${WDT_INSTANCE_NAME}_REGS->WDT_MR) )
    {
        <#if (3 < WDT_EARLY_RESET_THRESHOLD_COUNT)>
        const uint32_t  minWait = ${WDT_EARLY_RESET_THRESHOLD_COUNT};
        <#else>
        const uint32_t  minWait = 3;
        </#if>
        uint32_t        countDownValue = WDT_VR_COUNTER( WDT_REGS->WDT_VR );
        if( countDownValue != WDT_VR_COUNTER( WDT_REGS->WDT_VR ) )
            countDownValue = WDT_VR_COUNTER( WDT_REGS->WDT_VR );
    
        // initial WDT_WLR_PERIOD = ${WDT_PERIOD_COUNT} (counts)
        if( ${WDT_PERIOD_COUNT} > (minWait + countDownValue) )
        {
            ${WDT_INSTANCE_NAME}_REGS->WDT_CR = WDT_CR_KEY_PASSWD | WDT_CR_WDRSTT_Msk;
        }
    }
}

void ${WDT_INSTANCE_NAME}_Enable( void )
{   // Note: WDT_MR modifications should have at least 3 slow clock cycles between updates.
    // An interval check is not in place here and should be enforced externally.

    // enable WDT
    ${WDT_INSTANCE_NAME}_REGS->WDT_MR &= ~WDT_MR_WDDIS_Msk;
    // clear interrupt status
    (void) ${WDT_INSTANCE_NAME}_REGS->WDT_ISR;
    // enable appropriate interrupts
    ${WDT_INSTANCE_NAME}_REGS->WDT_IER = 0${(WDT_LEVEL_EXPIRATION=='Interrupt')?then(' | WDT_IER_LVLINT_Msk','')}${(WDT_EARLY_RESET_ACTION=='Interrupt')?then(' | WDT_IER_RPTHINT_Msk','')}${(WDT_PERIOD_EXPIRATION=='Interrupt')?then(' | WDT_IER_PERINT_Msk','')};
}

void ${WDT_INSTANCE_NAME}_Disable( void )
{   // Note: WDT_MR modifications should have at least 3 slow clock cycles between updates.
    // An interval check is not in place here and should be enforced externally.

    // disable all interrupts
    ${WDT_INSTANCE_NAME}_REGS->WDT_IDR = WDT_IDR_LVLINT_Msk | WDT_IDR_RPTHINT_Msk | WDT_IDR_PERINT_Msk;
    // disable WDT
    ${WDT_INSTANCE_NAME}_REGS->WDT_MR |= WDT_MR_WDDIS_Msk;
}

