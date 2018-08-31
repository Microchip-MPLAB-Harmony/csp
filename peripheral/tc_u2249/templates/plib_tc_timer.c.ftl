/*******************************************************************************
  Timer/Counter(TC${TC_INDEX}) PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_tc${TC_INDEX}.c

  Summary
    TC${TC_INDEX} PLIB Implementation File.

  Description
    This file defines the interface to the TC peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

  Remarks:
    None.

*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
Copyright (c) 2017 released Microchip Technology Inc. All rights reserved.
Microchip licenses to you the right to use, modify, copy and distribute
Software only when embedded on a Microchip microcontroller or digital signal
controller that is integrated into your product or third party product
(pursuant to the sublicense terms in the accompanying license agreement).

You should refer to the license agreement accompanying this Software for
additional information regarding your rights and obligations.

SOFTWARE AND DOCUMENTATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND,
EITHER EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION, ANY WARRANTY OF
MERCHANTABILITY, TITLE, NON-INFRINGEMENT AND FITNESS FOR A PARTICULAR PURPOSE.
IN NO EVENT SHALL MICROCHIP OR ITS LICENSORS BE LIABLE OR OBLIGATED UNDER
CONTRACT, NEGLIGENCE, STRICT LIABILITY, CONTRIBUTION, BREACH OF WARRANTY, OR
OTHER LEGAL EQUITABLE THEORY ANY DIRECT OR INDIRECT DAMAGES OR EXPENSES
INCLUDING BUT NOT LIMITED TO ANY INCIDENTAL, SPECIAL, INDIRECT, PUNITIVE OR
CONSEQUENTIAL DAMAGES, LOST PROFITS OR LOST DATA, COST OF PROCUREMENT OF
SUBSTITUTE GOODS, TECHNOLOGY, SERVICES, OR ANY CLAIMS BY THIRD PARTIES
(INCLUDING BUT NOT LIMITED TO ANY DEFENSE THEREOF), OR OTHER SIMILAR COSTS.
*******************************************************************************/
// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
/* This section lists the other files that are included in this file.
*/

#include "device.h"
#include "plib_tc${TC_INDEX}.h"

// *****************************************************************************
// *****************************************************************************
// Section: Global Data
// *****************************************************************************
// *****************************************************************************
volatile static uint32_t TC${TC_INDEX}_TimerStatus; 

<#if TC_TIMER_INTERRUPT_MODE == true>
TC_CALLBACK_OBJ TC${TC_INDEX}_CallbackObject;
</#if>

// *****************************************************************************
// *****************************************************************************
// Section: TC${TC_INDEX} Implementation
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Initialize the TC module in Timer mode */
void TC${TC_INDEX}_TimerInitialize( void )
{
    /* Reset TC */
    TC${TC_INDEX}_REGS->${TC_CTRLA_MODE}.TC_CTRLA = TC_CTRLA_SWRST_Msk;

    while((TC${TC_INDEX}_REGS->${TC_CTRLA_MODE}.TC_SYNCBUSY & TC_SYNCBUSY_SWRST_Msk) == TC_SYNCBUSY_SWRST_Msk)
    {
        /* Wait for Write Synchronization */
    }

    /* Configure counter mode & prescaler */
    <@compress single_line=true>TC${TC_INDEX}_REGS->${TC_CTRLA_MODE}.TC_CTRLA = TC_CTRLA_MODE_${TC_CTRLA_MODE}
                                | TC_CTRLA_PRESCALER_${TC_CTRLA_PRESCALER}
                                | TC_CTRLA_PRESCSYNC_PRESC
                                ${TC_CTRLA_RUNSTDBY?then('| TC_CTRLA_RUNSTDBY_Msk', '')}
                                ${TC_CTRLA_ONDEMAND?then('| TC_CTRLA_ONDEMAND_Msk', '')};</@compress>

    /* Configure in Match Frequency Mode */
    TC${TC_INDEX}_REGS->${TC_CTRLA_MODE}.TC_WAVE = TC_WAVE_WAVEGEN_MFRQ;

<#if TC_TIMER_CTRLBSET_ONESHOT == true>
    /* Configure timer one shot mode */
    TC${TC_INDEX}_REGS->${TC_CTRLA_MODE}.TC_CTRLBSET = TC_CTRLBSET_ONESHOT_Msk;
</#if>
    /* Configure timer period */
    TC${TC_INDEX}_REGS->${TC_CTRLA_MODE}.TC_CC[0U] = ${TC_TIMER_PERIOD}U;
    
    /* Clear all interrupt flags */
    TC${TC_INDEX}_REGS->${TC_CTRLA_MODE}.TC_INTFLAG = TC_INTFLAG_Msk;

    <#if TC_TIMER_INTERRUPT_MODE = true>
    TC${TC_INDEX}_CallbackObject.callback = NULL;
    /* Enable period interrupt*/
    TC${TC_INDEX}_REGS->${TC_CTRLA_MODE}.TC_INTENSET = TC_INTENSET_OVF_Msk;
    </#if>

    while((TC${TC_INDEX}_REGS->${TC_CTRLA_MODE}.TC_SYNCBUSY))
    {
        /* Wait for Write Synchronization */
    }
}

/* Enable the TC counter */
void TC${TC_INDEX}_TimerStart( void )
{
<#if TC_TIMER_CTRLBSET_ONESHOT == true>
    /* In one-shot timer mode, first disable the timer */
    TC${TC_INDEX}_REGS->${TC_CTRLA_MODE}.TC_CTRLA &= ~TC_CTRLA_ENABLE_Msk;
    while((TC${TC_INDEX}_REGS->${TC_CTRLA_MODE}.TC_SYNCBUSY & TC_SYNCBUSY_ENABLE_Msk) == TC_SYNCBUSY_ENABLE_Msk)
    {
        /* Wait for Write Synchronization */
    }
</#if>
    TC${TC_INDEX}_REGS->${TC_CTRLA_MODE}.TC_CTRLA |= TC_CTRLA_ENABLE_Msk;
    while((TC${TC_INDEX}_REGS->${TC_CTRLA_MODE}.TC_SYNCBUSY & TC_SYNCBUSY_ENABLE_Msk) == TC_SYNCBUSY_ENABLE_Msk)
    {
        /* Wait for Write Synchronization */
    }
}

/* Disable the TC counter */
void TC${TC_INDEX}_TimerStop( void )
{
    TC${TC_INDEX}_REGS->${TC_CTRLA_MODE}.TC_CTRLA &= ~TC_CTRLA_ENABLE_Msk;
    while((TC${TC_INDEX}_REGS->${TC_CTRLA_MODE}.TC_SYNCBUSY & TC_SYNCBUSY_ENABLE_Msk) == TC_SYNCBUSY_ENABLE_Msk)
    {
        /* Wait for Write Synchronization */
    }
}

<#if TC_CTRLA_MODE = "COUNT8">
/* Get the current timer counter value */
uint8_t TC${TC_INDEX}_Timer8bitCounterGet( void )
{
    /* Write command to force COUNT register read synchronization */
    TC${TC_INDEX}_REGS->${TC_CTRLA_MODE}.TC_CTRLBSET |= TC_CTRLBSET_CMD_READSYNC;

    while((TC${TC_INDEX}_REGS->${TC_CTRLA_MODE}.TC_SYNCBUSY & TC_SYNCBUSY_CTRLB_Msk) == TC_SYNCBUSY_CTRLB_Msk)
    {
        /* Wait for Write Synchronization */
    }

    /* Read current count value */
    return (uint8_t)TC${TC_INDEX}_REGS->${TC_CTRLA_MODE}.TC_COUNT;
}

/* Configure timer counter value */
void TC${TC_INDEX}_Timer8bitCounterSet( uint8_t count )
{
    TC${TC_INDEX}_REGS->${TC_CTRLA_MODE}.TC_COUNT = count;

    while((TC${TC_INDEX}_REGS->${TC_CTRLA_MODE}.TC_SYNCBUSY & TC_SYNCBUSY_COUNT_Msk) == TC_SYNCBUSY_COUNT_Msk)
    {
        /* Wait for Write Synchronization */
    }
}

/* Configure timer period */
void TC${TC_INDEX}_Timer8bitPeriodSet( uint8_t period )
{
    TC${TC_INDEX}_REGS->${TC_CTRLA_MODE}.TC_CCBUF[0] = period;
    while((TC${TC_INDEX}_REGS->${TC_CTRLA_MODE}.TC_SYNCBUSY & TC_SYNCBUSY_CC0_Msk) == TC_SYNCBUSY_CC0_Msk)
    {
        /* Wait for Write Synchronization */
    }
}

/* Read the timer period value */
uint8_t TC${TC_INDEX}_Timer8bitPeriodGet( void )
{
    return (uint8_t)TC${TC_INDEX}_REGS->${TC_CTRLA_MODE}.TC_CC[0];
}

<#elseif TC_CTRLA_MODE = "COUNT16">
/* Get the current timer counter value */
uint16_t TC${TC_INDEX}_Timer16bitCounterGet( void )
{
    /* Write command to force COUNT register read synchronization */
    TC${TC_INDEX}_REGS->${TC_CTRLA_MODE}.TC_CTRLBSET |= TC_CTRLBSET_CMD_READSYNC;

    while((TC${TC_INDEX}_REGS->${TC_CTRLA_MODE}.TC_SYNCBUSY & TC_SYNCBUSY_CTRLB_Msk) == TC_SYNCBUSY_CTRLB_Msk)
    {
        /* Wait for Write Synchronization */
    }

    /* Read current count value */
    return (uint16_t)TC${TC_INDEX}_REGS->${TC_CTRLA_MODE}.TC_COUNT;
}

/* Configure timer counter value */
void TC${TC_INDEX}_Timer16bitCounterSet( uint16_t count )
{
    TC${TC_INDEX}_REGS->${TC_CTRLA_MODE}.TC_COUNT = count;

    while((TC${TC_INDEX}_REGS->${TC_CTRLA_MODE}.TC_SYNCBUSY & TC_SYNCBUSY_COUNT_Msk) == TC_SYNCBUSY_COUNT_Msk)
    {
        /* Wait for Write Synchronization */
    }
}

/* Configure timer period */
void TC${TC_INDEX}_Timer16bitPeriodSet( uint16_t period )
{
    TC${TC_INDEX}_REGS->${TC_CTRLA_MODE}.TC_CCBUF[0] = period;
    while((TC${TC_INDEX}_REGS->${TC_CTRLA_MODE}.TC_SYNCBUSY & TC_SYNCBUSY_CC0_Msk) == TC_SYNCBUSY_CC0_Msk)
    {
        /* Wait for Write Synchronization */
    }
}

/* Read the timer period value */
uint16_t TC${TC_INDEX}_Timer16bitPeriodGet( void )
{
    return (uint16_t)TC${TC_INDEX}_REGS->${TC_CTRLA_MODE}.TC_CC[0];
}

<#elseif TC_CTRLA_MODE = "COUNT32">
/* Get the current timer counter value */
uint32_t TC${TC_INDEX}_Timer32bitCounterGet( void )
{
    /* Write command to force COUNT register read synchronization */
    TC${TC_INDEX}_REGS->${TC_CTRLA_MODE}.TC_CTRLBSET |= TC_CTRLBSET_CMD_READSYNC;

    while((TC${TC_INDEX}_REGS->${TC_CTRLA_MODE}.TC_SYNCBUSY & TC_SYNCBUSY_CTRLB_Msk) == TC_SYNCBUSY_CTRLB_Msk)
    {
        /* Wait for Write Synchronization */
    }

    /* Read current count value */
    return TC${TC_INDEX}_REGS->${TC_CTRLA_MODE}.TC_COUNT;

}

/* Configure timer counter value */
void TC${TC_INDEX}_Timer32bitCounterSet( uint32_t count )
{
    TC${TC_INDEX}_REGS->${TC_CTRLA_MODE}.TC_COUNT = count;

    while((TC${TC_INDEX}_REGS->${TC_CTRLA_MODE}.TC_SYNCBUSY & TC_SYNCBUSY_COUNT_Msk) == TC_SYNCBUSY_COUNT_Msk)
    {
        /* Wait for Write Synchronization */
    }
}

/* Configure timer period */
void TC${TC_INDEX}_Timer32bitPeriodSet( uint32_t period )
{
    TC${TC_INDEX}_REGS->${TC_CTRLA_MODE}.TC_CCBUF[0] = period;
    while((TC${TC_INDEX}_REGS->${TC_CTRLA_MODE}.TC_SYNCBUSY & TC_SYNCBUSY_COUNT_Msk) == TC_SYNCBUSY_COUNT_Msk)
    {
        /* Wait for Write Synchronization */
    }
}

/* Read the timer period value */
uint32_t TC${TC_INDEX}_Timer32bitPeriodGet( void )
{
    return TC${TC_INDEX}_REGS->${TC_CTRLA_MODE}.TC_CC[0];
}
</#if>

/* Polling method to check if timer period interrupt flag is set */
bool TC${TC_INDEX}_TimerPeriodHasExpired( void )
{
    bool timer_status;
    //NVIC_DisableIRQ(TC${TC_INDEX}_IRQn);
    timer_status = ((TC${TC_INDEX}_TimerStatus | TC${TC_INDEX}_REGS->${TC_CTRLA_MODE}.TC_INTFLAG) & TC_INTFLAG_OVF_Msk);
    TC${TC_INDEX}_TimerStatus = 0U;
    /* Clear timer overflow interrupt */
    TC${TC_INDEX}_REGS->${TC_CTRLA_MODE}.TC_INTFLAG = TC_INTFLAG_OVF_Msk;
    //NVIC_EnableIRQ(TC${TC_INDEX}_IRQn);
    return timer_status;
}

<#if TC_TIMER_INTERRUPT_MODE = true>
/* Register callback function */
void TC${TC_INDEX}_TimerCallbackRegister( TC_CALLBACK callback, uintptr_t context )
{
    TC${TC_INDEX}_CallbackObject.callback = callback;

    TC${TC_INDEX}_CallbackObject.context = context;
}

/* Timer Interrupt handler */
void TC${TC_INDEX}_TimerInterruptHandler( void )
{
    TC${TC_INDEX}_TimerStatus = TC${TC_INDEX}_REGS->${TC_CTRLA_MODE}.TC_INTFLAG;
    if(TC${TC_INDEX}_CallbackObject.callback != NULL)
    {
        TC${TC_INDEX}_CallbackObject.callback(TC${TC_INDEX}_CallbackObject.context);
    }
    /* Clear timer overflow interrupt */
    TC${TC_INDEX}_REGS->${TC_CTRLA_MODE}.TC_INTFLAG = TC_INTFLAG_OVF_Msk;
}
</#if>



