/*******************************************************************************
  Periodic Interval Timer (PIT64B) 

  Company:
    Microchip Technology Inc.

  File Name:
    plib_pit64b.h

  Summary:
    Periodic Interval Timer (PIT64B) PLIB.

  Description:
    This file declares the interface for the Periodic Interval Timer (PIT64B).
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

#include "plib_pit64b.h"

typedef struct
{
    PIT64B_CALLBACK callback;
    uintptr_t context;
    volatile uint32_t tickCounter;
    bool running;
} PIT64B_OBJECT;

static PIT64B_OBJECT pit64b;

void PIT64B_TimerInitialize(void)
{
    PIT64B_REGS->PIT64B_CR = PIT64B_CR_SWRST_Msk;
    PIT64B_REGS->PIT64B_MR = PIT64B_MR_CONT(1) | PIT64B_MR_SGCLK(0) | PIT64B_MR_PRESCALER(0);
    PIT64B_REGS->PIT64B_MSBPR = 0;
    PIT64B_REGS->PIT64B_LSBPR = 0;
    PIT64B_REGS->PIT64B_MR |= PIT64B_MR_SMOD(0);
    pit64b.running = 0;
}

void PIT64B_TimerRestart(void)
{
    PIT64B_TimerInitialize();
    PIT64B_TimerStart();
    pit64b.running = 1;
}

void PIT64B_TimerStart(void)
{
    PIT64B_REGS->PIT64B_CR = PIT64B_CR_START_Msk;
    pit64b.running = 1;
}

void PIT64B_TimerStop(void)
{
    PIT64B_TimerInitialize();
    pit64b.running = 0;
}

void PIT64B_TimerPeriodSet(uint64_t period)
{
    PIT64B_REGS->PIT64B_MSBPR = (period & 0xFFFFFFFF00000000)>>32;
    PIT64B_REGS->PIT64B_LSBPR = (period & 0xFFFFFFFF);
}

uint64_t PIT64B_TimerPeriodGet(void)
{
    uint64_t reg = PIT64B_REGS->PIT64B_MSBPR;
    reg = reg<<32;
    reg |= PIT64B_REGS->PIT64B_LSBPR;
    return reg;
}

uint64_t PIT64B_TimerCounterGet(void)
{
    uint64_t reg = PIT64B_REGS->PIT64B_TMSBR;
    reg = reg<<32;
    reg |= PIT64B_REGS->PIT64B_TLSBR;
    return reg;
}

uint32_t PIT64B_TimerFrequencyGet(void)
{
    return 200000000;
}

void PIT64B_DelayMs(uint32_t delay)
{
    uint32_t tickStart;
    uint32_t delayTicks;

    if (pit64b.running && ((PIT64B_REGS->PIT64B_IMR & PIT64B_IMR_PERIOD_Msk) == PIT64B_IMR_PERIOD_Msk)) {
        tickStart=pit64b.tickCounter;
        delayTicks=1000*delay/1000;

        while((pit64b.tickCounter-tickStart) < delayTicks);
    }
}

void PIT64B_TimerCallbackSet(PIT64B_CALLBACK callback, uintptr_t context)
{
    pit64b.callback = callback;
    pit64b.context = context;
}

void PIT64B_InterruptHandler(void)
{
    uint32_t reg = PIT64B_REGS->PIT64B_ISR;
    pit64b.tickCounter++;
    if(pit64b.callback)
        pit64b.callback(pit64b.context);
}
