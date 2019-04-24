/*******************************************************************************
  PWM Peripheral Library Interface Source File

  Company
    Microchip Technology Inc.

  File Name
    plib_PWM.c

  Summary
    PWM peripheral library source file.

  Description
    This file implements the interface to the PWM peripheral library.  This
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


// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

/*  This section lists the other files that are included in this file.
*/
#include "device.h"
#include "plib_pwm.h"


/* Object to hold callback function and context */
PWM_CALLBACK_OBJECT PWM_CallbackObj;

/* Initialize enabled PWM channels */
void PWM_Initialize (void)
{
    /* Clock configuration */
    PWM_REGS->PWM_MR = PWM_MR_PREA_MCKDIV4 | PWM_MR_DIVA(5) |
        PWM_MR_PREB_MCKDIV2 | PWM_MR_DIVB(10);


    /************** Channel 0 *************************/
    /* Channel Mode */
    PWM_REGS->PWM_CH_NUM[0].PWM_CMR = PWM_CMR_CPRE_CLKA | PWM_CMR_CALG_LEFT_ALIGNED | \
                                                               PWM_CMR_CPOL_HIGH_POLARITY;

    /* Channel Period */
    PWM_REGS->PWM_CH_NUM[0].PWM_CPRD = 10000U;

    /* Channel Duty */
    PWM_REGS->PWM_CH_NUM[0].PWM_CDTY  = 2500U;

    /************** Channel 1 *************************/
    /* Channel Mode */
    PWM_REGS->PWM_CH_NUM[1].PWM_CMR = PWM_CMR_CPRE_CLKB | PWM_CMR_CALG_CENTER_ALIGNED | \
                                                               PWM_CMR_CPOL_LOW_POLARITY;

    /* Channel Period */
    PWM_REGS->PWM_CH_NUM[1].PWM_CPRD = 50000U;

    /* Channel Duty */
    PWM_REGS->PWM_CH_NUM[1].PWM_CDTY  = 25000U;

    /************** Channel 2 *************************/
    /* Channel Mode */
    PWM_REGS->PWM_CH_NUM[2].PWM_CMR = PWM_CMR_CPRE_MCKDIV4 | PWM_CMR_CALG_LEFT_ALIGNED | \
                                                               PWM_CMR_CPOL_HIGH_POLARITY;

    /* Channel Period */
    PWM_REGS->PWM_CH_NUM[2].PWM_CPRD = 5000000U;

    /* Channel Duty */
    PWM_REGS->PWM_CH_NUM[2].PWM_CDTY  = 3750000U;

    /************** Channel 3 *************************/
    /* Channel Mode */
    PWM_REGS->PWM_CH_NUM[3].PWM_CMR = PWM_CMR_CPRE_MCKDIV8 | PWM_CMR_CALG_LEFT_ALIGNED | \
                                                               PWM_CMR_CPOL_LOW_POLARITY;

    /* Channel Period */
    PWM_REGS->PWM_CH_NUM[3].PWM_CPRD = 25000000U;

    /* Channel Duty */
    PWM_REGS->PWM_CH_NUM[3].PWM_CDTY  = 25000000U;

    /* Enable counter event */
    PWM_REGS->PWM_IER = (0x1U << 3U);

    PWM_CallbackObj.callback_fn = NULL;
}

void PWM_ChannelsStart (PWM_CHANNEL_MASK channelMask)
{
    PWM_REGS->PWM_ENA = channelMask;
}

void PWM_ChannelsStop (PWM_CHANNEL_MASK channelMask)
{
    PWM_REGS->PWM_DIS = channelMask;
}

void PWM_ChannelPeriodSet (PWM_CHANNEL_NUM channel, uint32_t period)
{
    if(0 != ((PWM_REGS->PWM_SR >> channel) & 0x1U))
    {
        PWM_REGS->PWM_CH_NUM[channel].PWM_CMR |= PWM_CMR_CPD_Msk;
        PWM_REGS->PWM_CH_NUM[channel].PWM_CUPD = period;
    }
    else
    {
        PWM_REGS->PWM_CH_NUM[channel].PWM_CPRD = period;
    }
}

uint32_t PWM_ChannelPeriodGet (PWM_CHANNEL_NUM channel)
{
    return PWM_REGS->PWM_CH_NUM[channel].PWM_CPRD;
}

void PWM_ChannelDutySet(PWM_CHANNEL_NUM channel, uint32_t duty)
{
    if(0 != ((PWM_REGS->PWM_SR >> channel) & 0x1U))
    {
        PWM_REGS->PWM_CH_NUM[channel].PWM_CMR &= ~PWM_CMR_CPD_Msk;
        PWM_REGS->PWM_CH_NUM[channel].PWM_CUPD = duty;
    }
    else
    {
        PWM_REGS->PWM_CH_NUM[channel].PWM_CDTY = duty;
    }
}

void PWM_ChannelCounterEventEnable (PWM_CHANNEL_MASK channelMask)
{
    PWM_REGS->PWM_IER = channelMask;
}

void PWM_ChannelCounterEventDisable (PWM_CHANNEL_MASK channelMask)
{
    PWM_REGS->PWM_IDR = channelMask;
}

 /* Register callback function */
void PWM_CallbackRegister(PWM_CALLBACK callback, uintptr_t context)
{
    PWM_CallbackObj.callback_fn = callback;
    PWM_CallbackObj.context = context;
}

/* Interrupt Handler */
void PWM_InterruptHandler(void)
{
    uint32_t status;
    status = PWM_REGS->PWM_ISR;
    if (PWM_CallbackObj.callback_fn != NULL)
    {
        PWM_CallbackObj.callback_fn(status, PWM_CallbackObj.context);
    }
}


/**
 End of File
*/
