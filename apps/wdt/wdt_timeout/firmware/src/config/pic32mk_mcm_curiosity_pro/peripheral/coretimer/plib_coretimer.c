/*******************************************************************************
  Core Timer Peripheral Library

  Company:
    Microchip Technology Inc.

  File Name:
    plib_coretimer.c

  Summary:
    Core timer Source File

  Description:
    None

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

#include "device.h"
#include "peripheral/coretimer/plib_coretimer.h"

CORETIMER_OBJECT coreTmr;
void CORETIMER_Initialize()
{
    // Disable Timer by setting Disable Count (DC) bit
    _CP0_SET_CAUSE(_CP0_GET_CAUSE() | _CP0_CAUSE_DC_MASK);
    coreTmr.period=CORE_TIMER_INTERRUPT_PERIOD_VALUE;
    coreTmr.tickCounter = 0;
    coreTmr.callback = NULL;
}
void CORETIMER_CallbackSet ( CORETIMER_CALLBACK callback, uintptr_t context )
{
    coreTmr.callback = callback;
    coreTmr.context = context;
}
void CORETIMER_PeriodSet ( uint32_t period )
{
    coreTmr.period=period;
}
void CORETIMER_Start()
{
    // Disable Timer by setting Disable Count (DC) bit
    _CP0_SET_CAUSE(_CP0_GET_CAUSE() | _CP0_CAUSE_DC_MASK);
    // Disable Interrupt
    IEC0CLR=0x1;
    // Clear Core Timer
    _CP0_SET_COUNT(0);
    _CP0_SET_COMPARE(coreTmr.period);
    // Enable Timer by clearing Disable Count (DC) bit
    _CP0_SET_CAUSE(_CP0_GET_CAUSE() & (~_CP0_CAUSE_DC_MASK));
    // Enable Interrupt
    IEC0SET=0x1;
}
void CORETIMER_Stop()
{
    // Disable Timer by setting Disable Count (DC) bit
    _CP0_SET_CAUSE(_CP0_GET_CAUSE() | _CP0_CAUSE_DC_MASK);
    // Disable Interrupt
    IEC0CLR=0x1;
}
uint32_t CORETIMER_FrequencyGet ( void )
{
    return (CORE_TIMER_FREQUENCY);
}
void CORETIMER_DelayMs ( uint32_t delay)
{
    uint32_t tickStart, delayTicks;
    tickStart=coreTmr.tickCounter;
    delayTicks=(1000 * delay)/CORE_TIMER_INTERRUPT_PERIOD_IN_US;  // Number of tick interrupts to wait for the delay
    while((coreTmr.tickCounter-tickStart)<delayTicks)
    {
    }
}
void CORE_TIMER_InterruptHandler (void)
{
    uint32_t count, newCompare;
    uint32_t status = IFS0bits.CTIF;
    IFS0CLR = 0x1;
    // Start Critical Section
    __builtin_disable_interrupts();
    count=_CP0_GET_COUNT();
    newCompare=_CP0_GET_COMPARE() + coreTmr.period;
    if (count<newCompare-50)
        _CP0_SET_COMPARE(newCompare);
    else
        _CP0_SET_COMPARE(count+50);
    // End Critical Section
    __builtin_enable_interrupts();
    coreTmr.tickCounter++;
    if(coreTmr.callback != NULL)
    {
        coreTmr.callback(status, coreTmr.context);
    }
}



