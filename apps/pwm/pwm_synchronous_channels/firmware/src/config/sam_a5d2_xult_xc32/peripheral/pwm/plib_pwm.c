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

    /* Synchronous channels configuration */
    PWM_REGS->PWM_SCM = PWM_SCM_SYNC0_Msk | PWM_SCM_SYNC1_Msk| PWM_SCM_SYNC2_Msk | PWM_SCM_UPDM_MODE1;
    PWM_REGS->PWM_SCUP = PWM_SCUP_UPR(0U);

    /************** Channel 0 *************************/
    /* PWM channel mode configurations */
    PWM_REGS->PWM_CH_NUM[0].PWM_CMR = PWM_CMR_CPRE_MCK | PWM_CMR_CALG_CENTER_ALIGNED
                    | PWM_CMR_CPOL_LOW_POLARITY | PWM_CMR_UPDS_UPDATE_AT_PERIOD \
                    | PWM_CMR_CES_SINGLE_EVENT | (PWM_CMR_DTE_Msk);

    /* PWM period */
    PWM_REGS->PWM_CH_NUM[0].PWM_CPRD = 2075U;

    /* PWM duty cycle */
    PWM_REGS->PWM_CH_NUM[0].PWM_CDTY = 0U;
    /* Dead time */
    PWM_REGS->PWM_CH_NUM[0].PWM_DT = (100U << PWM_DT_DTL_Pos) | (100U);
         
    /* Enable counter event */
    PWM_REGS->PWM_IER1 = (0x1U << 0U);
    PWM_CallbackObj.callback_fn = NULL;
     
    /************** Channel 1 *************************/

    /* PWM duty cycle */
    PWM_REGS->PWM_CH_NUM[1].PWM_CDTY = 0U;
    PWM_REGS->PWM_CH_NUM[1].PWM_CMR = PWM_CMR_DTE_Msk;
    /* Dead time */
    PWM_REGS->PWM_CH_NUM[1].PWM_DT = (100U << PWM_DT_DTL_Pos) | (100U);
         
     
    /************** Channel 2 *************************/

    /* PWM duty cycle */
    PWM_REGS->PWM_CH_NUM[2].PWM_CDTY = 0U;
    PWM_REGS->PWM_CH_NUM[2].PWM_CMR = PWM_CMR_DTE_Msk;
    /* Dead time */
    PWM_REGS->PWM_CH_NUM[2].PWM_DT = (100U << PWM_DT_DTL_Pos) | (100U);
         
     
 



}

/* Start the PWM generation */
void PWM_ChannelsStart (PWM_CHANNEL_MASK channelMask)
{
    PWM_REGS->PWM_ENA = channelMask;
}

/* Stop the PWM generation */
void PWM_ChannelsStop (PWM_CHANNEL_MASK channelMask)
{
    PWM_REGS->PWM_DIS = channelMask;
}

/* configure PWM period */
void PWM_ChannelPeriodSet (PWM_CHANNEL_NUM channel, uint16_t period)
{
    PWM_REGS->PWM_CH_NUM[channel].PWM_CPRDUPD = period;
}

/* Read PWM period */
uint16_t PWM_ChannelPeriodGet (PWM_CHANNEL_NUM channel)
{
    return (uint16_t)PWM_REGS->PWM_CH_NUM[channel].PWM_CPRD;
}

/* Configure dead time */
void PWM_ChannelDeadTimeSet (PWM_CHANNEL_NUM channel, uint16_t deadtime_high, uint16_t deadtime_low)
{
    PWM_REGS->PWM_CH_NUM[channel].PWM_DTUPD = ((deadtime_low << PWM_DT_DTL_Pos) | deadtime_high);
}

/* Configure compare unit value */
void PWM_CompareValueSet (PWM_COMPARE cmp_unit, uint16_t cmp_value)
{
    PWM_REGS->PWM_CMP[cmp_unit].PWM_CMPVUPD = cmp_value;
}

/* Enable counter event */
void PWM_ChannelCounterEventEnable (PWM_CHANNEL_MASK channelMask)
{
    PWM_REGS->PWM_IER1 = channelMask;
}

/* Disable counter event */
void PWM_ChannelCounterEventDisable (PWM_CHANNEL_MASK channelMask)
{
    PWM_REGS->PWM_IDR1 = channelMask;
}


/* Enable synchronous update */
void PWM_SyncUpdateEnable (void)
{
    PWM_REGS->PWM_SCUC = PWM_SCUC_UPDULOCK_Msk;
}

/* Clear the fault status */
void PWM_FaultStatusClear(PWM_FAULT_ID fault_id)
{
    PWM_REGS->PWM_FCR = 0x1U << fault_id;
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
    status = PWM_REGS->PWM_ISR1;
    if (PWM_CallbackObj.callback_fn != NULL)
    {
        PWM_CallbackObj.callback_fn(status, PWM_CallbackObj.context);
    }
}


/**
 End of File
*/
