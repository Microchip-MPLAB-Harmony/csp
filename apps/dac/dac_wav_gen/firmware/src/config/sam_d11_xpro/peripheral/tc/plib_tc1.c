/*******************************************************************************
  Timer/Counter(TC1) PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_tc1.c

  Summary
    TC1 PLIB Implementation File.

  Description
    This file defines the interface to the TC peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

  Remarks:
    None.

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
/* This section lists the other files that are included in this file.
*/

#include "plib_tc1.h"


// *****************************************************************************
// *****************************************************************************
// Section: Global Data
// *****************************************************************************
// *****************************************************************************

TC_TIMER_CALLBACK_OBJ TC1_CallbackObject;

// *****************************************************************************
// *****************************************************************************
// Section: TC1 Implementation
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Initialize the TC module in Timer mode */
void TC1_TimerInitialize( void )
{
    /* Reset TC */
    TC1_REGS->COUNT16.TC_CTRLA = TC_CTRLA_SWRST_Msk;

    while((TC1_REGS->COUNT16.TC_STATUS & TC_STATUS_SYNCBUSY_Msk))
    {
        /* Wait for Write Synchronization */
    }

    /* Configure counter mode & prescaler */
    TC1_REGS->COUNT16.TC_CTRLA = TC_CTRLA_MODE_COUNT16 | TC_CTRLA_PRESCALER_DIV1 | TC_CTRLA_WAVEGEN_MPWM ;

    /* Configure timer period */
    TC1_REGS->COUNT16.TC_CC[0U] = 479U;

    /* Clear all interrupt flags */
    TC1_REGS->COUNT16.TC_INTFLAG = TC_INTFLAG_Msk;

    TC1_CallbackObject.callback = NULL;
    /* Enable interrupt*/
    TC1_REGS->COUNT16.TC_INTENSET = TC_INTENSET_OVF_Msk;


    while((TC1_REGS->COUNT16.TC_STATUS & TC_STATUS_SYNCBUSY_Msk))
    {
        /* Wait for Write Synchronization */
    }
}

/* Enable the TC counter */
void TC1_TimerStart( void )
{
    TC1_REGS->COUNT16.TC_CTRLA |= TC_CTRLA_ENABLE_Msk;
    while((TC1_REGS->COUNT16.TC_STATUS & TC_STATUS_SYNCBUSY_Msk))
    {
        /* Wait for Write Synchronization */
    }
}

/* Disable the TC counter */
void TC1_TimerStop( void )
{
    TC1_REGS->COUNT16.TC_CTRLA &= ~TC_CTRLA_ENABLE_Msk;
    while((TC1_REGS->COUNT16.TC_STATUS & TC_STATUS_SYNCBUSY_Msk))
    {
        /* Wait for Write Synchronization */
    }
}

uint32_t TC1_TimerFrequencyGet( void )
{
    return (uint32_t)(48000000UL);
}

/* Get the current timer counter value */
uint16_t TC1_Timer16bitCounterGet( void )
{
    /* Write command to force COUNT register read synchronization */
    TC1_REGS->COUNT16.TC_READREQ = TC_READREQ_RREQ_Msk | TC_COUNT16_COUNT_REG_OFST;

    while((TC1_REGS->COUNT16.TC_STATUS & TC_STATUS_SYNCBUSY_Msk))
    {
        /* Wait for Write Synchronization */
    }

    /* Read current count value */
    return (uint16_t)TC1_REGS->COUNT16.TC_COUNT;
}

/* Configure timer counter value */
void TC1_Timer16bitCounterSet( uint16_t count )
{
    TC1_REGS->COUNT16.TC_COUNT = count;

    while((TC1_REGS->COUNT16.TC_STATUS & TC_STATUS_SYNCBUSY_Msk))
    {
        /* Wait for Write Synchronization */
    }
}

/* Configure timer period */
void TC1_Timer16bitPeriodSet( uint16_t period )
{
    TC1_REGS->COUNT16.TC_CC[0] = period;
    while((TC1_REGS->COUNT16.TC_STATUS & TC_STATUS_SYNCBUSY_Msk))
    {
        /* Wait for Write Synchronization */
    }
}

/* Read the timer period value */
uint16_t TC1_Timer16bitPeriodGet( void )
{
    /* Write command to force CC register read synchronization */
    TC1_REGS->COUNT16.TC_READREQ = TC_READREQ_RREQ_Msk | TC_COUNT16_CC_REG_OFST;

    while((TC1_REGS->COUNT16.TC_STATUS & TC_STATUS_SYNCBUSY_Msk))
    {
        /* Wait for Write Synchronization */
    }
    return (uint16_t)TC1_REGS->COUNT16.TC_CC[0];
}



/* Register callback function */
void TC1_TimerCallbackRegister( TC_TIMER_CALLBACK callback, uintptr_t context )
{
    TC1_CallbackObject.callback = callback;

    TC1_CallbackObject.context = context;
}

/* Timer Interrupt handler */
void TC1_TimerInterruptHandler( void )
{
    TC_TIMER_STATUS status;
    status = (TC_TIMER_STATUS) (TC1_REGS->COUNT16.TC_INTFLAG);
    /* Clear interrupt flags */
    TC1_REGS->COUNT16.TC_INTFLAG = TC_INTFLAG_Msk;
    if(TC1_CallbackObject.callback != NULL)
    {
        TC1_CallbackObject.callback(status, TC1_CallbackObject.context);
    }
}

