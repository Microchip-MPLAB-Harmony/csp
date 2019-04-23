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



/* Initialize enabled PWM channels */
void PWM_Initialize (void)
{
    /* Clock configuration */
    PWM_REGS->PWM_MR = PWM_MR_PREA_MCK | PWM_MR_DIVA(200);


    /************** Channel 0 *************************/
    /* Channel Mode */
    PWM_REGS->PWM_CH_NUM[0].PWM_CMR = PWM_CMR_CPRE_CLKA | PWM_CMR_CALG_LEFT_ALIGNED | \
                                                               PWM_CMR_CPOL_LOW_POLARITY;

    /* Channel Period */
    PWM_REGS->PWM_CH_NUM[0].PWM_CPRD = 1000U;

    /* Channel Duty */
    PWM_REGS->PWM_CH_NUM[0].PWM_CDTY  = 100U;
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

void PWM_ChannelInterruptEnable (PWM_CHANNEL_MASK channelMask)
{
    PWM_REGS->PWM_IER = channelMask;
}

void PWM_ChannelInterruptDisable (PWM_CHANNEL_MASK channelMask)
{
    PWM_REGS->PWM_IDR = channelMask;
}


/* Check the status of counter event */
bool PWM_ChannelCounterEventStatusGet (PWM_CHANNEL_NUM channel)
{
    bool status;
    status = (PWM_REGS->PWM_ISR >> channel) & 0x1U;
    return status;
}

/**
 End of File
*/
