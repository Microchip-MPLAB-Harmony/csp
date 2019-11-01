/*******************************************************************************
  TC Peripheral Library Interface Source File

  Company
    Microchip Technology Inc.

  File Name
    plib_tc0.c

  Summary
    TC peripheral library source file.

  Description
    This file implements the interface to the TC peripheral library.  This
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
#include "plib_tc0.h"

 
 

 

 

/* Initialize channel in capture mode */
void TC0_CH0_CaptureInitialize (void)
{
    /* clock selection and capture configurations */
    TC0_REGS->TC_CHANNEL[0].TC_CMR = TC_CMR_TCCLKS_TIMER_CLOCK3 | TC_CMR_CAPTURE_LDRA_RISING \
        | TC_CMR_CAPTURE_LDRB_FALLING ;

    /* external reset event configurations */
    TC0_REGS->TC_CHANNEL[0].TC_CMR |=  TC_CMR_CAPTURE_ABETRG_Msk |  TC_CMR_CAPTURE_ETRGEDG_FALLING;

}

/* Start the capture mode */
void TC0_CH0_CaptureStart (void)
{
    TC0_REGS->TC_CHANNEL[0].TC_CCR = (TC_CCR_CLKEN_Msk | TC_CCR_SWTRG_Msk);
}

/* Stop the capture mode */
void TC0_CH0_CaptureStop (void)
{
    TC0_REGS->TC_CHANNEL[0].TC_CCR = (TC_CCR_CLKDIS_Msk);
}

uint32_t TC0_CH0_CaptureFrequencyGet( void )
{
    return (uint32_t)(6250000UL);
}

/* Read last captured value of Capture A */
uint32_t TC0_CH0_CaptureAGet (void)
{
    return TC0_REGS->TC_CHANNEL[0].TC_RA;
}

/* Read last captured value of Capture B */
uint32_t TC0_CH0_CaptureBGet (void)
{
    return TC0_REGS->TC_CHANNEL[0].TC_RB;
}

/*Get the capture status */
TC_CAPTURE_STATUS TC0_CH0_CaptureStatusGet(void)
{
    return (TC_CAPTURE_STATUS)(TC0_REGS->TC_CHANNEL[0].TC_SR & TC_CAPTURE_STATUS_MSK);
}
 
 
 
 


/* Callback object for channel 1 */
TC_TIMER_CALLBACK_OBJECT TC0_CH1_CallbackObj;

/* Initialize channel in timer mode */
void TC0_CH1_TimerInitialize (void)
{
    /* clock selection and waveform selection */
    TC0_REGS->TC_CHANNEL[1].TC_CMR = TC_CMR_TCCLKS_TIMER_CLOCK5 | TC_CMR_WAVEFORM_WAVSEL_UP_RC | \
                                                        TC_CMR_WAVE_Msk ;

    /* write period */
    TC0_REGS->TC_CHANNEL[1].TC_RC = 32000U;


    /* enable interrupt */
    TC0_REGS->TC_CHANNEL[1].TC_IER = TC_IER_CPCS_Msk;
    TC0_CH1_CallbackObj.callback_fn = NULL;
}

/* Start the timer */
void TC0_CH1_TimerStart (void)
{
    TC0_REGS->TC_CHANNEL[1].TC_CCR = (TC_CCR_CLKEN_Msk | TC_CCR_SWTRG_Msk);
}

/* Stop the timer */
void TC0_CH1_TimerStop (void)
{
    TC0_REGS->TC_CHANNEL[1].TC_CCR = (TC_CCR_CLKDIS_Msk);
}

uint32_t TC0_CH1_TimerFrequencyGet( void )
{
    return (uint32_t)(32000UL);
}

/* Configure timer period */
void TC0_CH1_TimerPeriodSet (uint32_t period)
{
    TC0_REGS->TC_CHANNEL[1].TC_RC = period;
}


/* Read timer period */
uint32_t TC0_CH1_TimerPeriodGet (void)
{
    return TC0_REGS->TC_CHANNEL[1].TC_RC;
}

/* Read timer counter value */
uint32_t TC0_CH1_TimerCounterGet (void)
{
    return TC0_REGS->TC_CHANNEL[1].TC_CV;
}

/* Register callback for period interrupt */
void TC0_CH1_TimerCallbackRegister(TC_TIMER_CALLBACK callback, uintptr_t context)
{
    TC0_CH1_CallbackObj.callback_fn = callback;
    TC0_CH1_CallbackObj.context = context;
}

/* Interrupt handler for Channel 1 */
void TC0_CH1_InterruptHandler(void)
{
    TC_TIMER_STATUS timer_status = (TC_TIMER_STATUS)(TC0_REGS->TC_CHANNEL[1].TC_SR & TC_TIMER_STATUS_MSK);
    /* Call registered callback function */
    if ((TC_TIMER_NONE != timer_status) && TC0_CH1_CallbackObj.callback_fn != NULL)
    {
        TC0_CH1_CallbackObj.callback_fn(timer_status, TC0_CH1_CallbackObj.context);
    }
}

 
 
 
 
 

 

/* Interrupt handler for TC0 */
void TC0_InterruptHandler(void)
{

	TC0_CH1_InterruptHandler();
}
 
 
/**
 End of File
*/
