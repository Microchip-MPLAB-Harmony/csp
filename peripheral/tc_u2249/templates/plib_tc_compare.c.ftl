/*******************************************************************************
  Timer/Counter(${TC_INSTANCE_NAME}) PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_${TC_INSTANCE_NAME?lower_case}.c

  Summary
    ${TC_INSTANCE_NAME} PLIB Implementation File.

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
#include "plib_${TC_INSTANCE_NAME?lower_case}.h"

<#assign TC_CTRLBSET_VAL = "">
<#if TC_COMPARE_CTRLBSET_DIR == "1">
    <#assign TC_CTRLBSET_VAL = "TC_CTRLBSET_DIR_Msk">
</#if>
<#if TC_COMPARE_CTRLBSET_ONESHOT == true>
    <#if TC_CTRLBSET_VAL != "">
        <#assign TC_CTRLBSET_VAL = TC_CTRLBSET_VAL + " | TC_CTRLBSET_ONESHOT_Msk">
    <#else>
        <#assign TC_CTRLBSET_VAL = "TC_CTRLBSET_ONESHOT_Msk">
    </#if>
</#if>
<#if TC_COMPARE_CTRLBSET_LUPD == false>
    <#if TC_CTRLBSET_VAL != "">
        <#assign TC_CTRLBSET_VAL = TC_CTRLBSET_VAL + " | TC_CTRLBSET_LUPD_Msk">
    <#else>
        <#assign TC_CTRLBSET_VAL = "TC_CTRLBSET_LUPD_Msk">
    </#if>
</#if>

// *****************************************************************************
// *****************************************************************************
// Section: Global Data
// *****************************************************************************
// *****************************************************************************
volatile static uint32_t ${TC_INSTANCE_NAME}_CompareStatus;

<#if TC_COMPARE_INTENSET_OVF = true>
TC_CALLBACK_OBJ ${TC_INSTANCE_NAME}_CallbackObject;
</#if>

// *****************************************************************************
// *****************************************************************************
// Section: ${TC_INSTANCE_NAME} Implementation
// *****************************************************************************
// *****************************************************************************

/* Initialize TC module in Compare Mode */
void ${TC_INSTANCE_NAME}_CompareInitialize( void )
{
    /* Reset TC */
    ${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_CTRLA = TC_CTRLA_SWRST_Msk;

    while((${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_SYNCBUSY & TC_SYNCBUSY_SWRST_Msk) == TC_SYNCBUSY_SWRST_Msk)
    {
        /* Wait for Write Synchronization */
    }

    /* Configure counter mode & prescaler */
    <@compress single_line=true>${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_CTRLA = TC_CTRLA_MODE_${TC_CTRLA_MODE}
                                | TC_CTRLA_PRESCALER_${TC_CTRLA_PRESCALER}
                                | TC_CTRLA_PRESCSYNC_PRESC
                                ${TC_CTRLA_RUNSTDBY?then('| TC_CTRLA_RUNSTDBY_Msk', '')}
                                ${TC_CTRLA_ONDEMAND?then('| TC_CTRLA_ONDEMAND_Msk', '')};</@compress>

    /* Configure waveform generation mode */
    ${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_WAVE = TC_WAVE_WAVEGEN_${TC_COMPARE_WAVE_WAVEGEN};

    <#if TC_CTRLBSET_VAL?has_content>
    /* Configure timer one shot mode & direction */
    ${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_CTRLBSET = TC_CTRLBSET_VAL;
    </#if>

    ${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_CC[0] = ${TC_COMPARE_PERIOD}U;
    <#if TC_COMPARE_WAVE_WAVEGEN == "MPWM"> 
    ${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_CC[1] = ${TC_COMPARE_CC1}U;
    </#if>
    
    /* Clear all interrupt flags */
    ${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_INTFLAG = TC_INTFLAG_Msk;

    <#if TC_COMPARE_INTENSET_OVF = true>
    /* Enable period Interrupt */
    ${TC_INSTANCE_NAME}_CallbackObject.callback = NULL;
    ${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_INTENSET = TC_INTENSET_OVF_Msk;
    </#if>

    while((${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_SYNCBUSY))
    {
        /* Wait for Write Synchronization */
    }
}

/* Enable the counter */
void ${TC_INSTANCE_NAME}_CompareStart( void )
{
<#if TC_COMPARE_CTRLBSET_ONESHOT == true>
    /* In one-shot mode, first disable the TC and then enable */
    ${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_CTRLA &= ~TC_CTRLA_ENABLE_Msk;
    while((${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_SYNCBUSY & TC_SYNCBUSY_ENABLE_Msk) == TC_SYNCBUSY_ENABLE_Msk)
    {
        /* Wait for Write Synchronization */
    }
</#if>
    ${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_CTRLA |= TC_CTRLA_ENABLE_Msk;
    while((${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_SYNCBUSY & TC_SYNCBUSY_ENABLE_Msk) == TC_SYNCBUSY_ENABLE_Msk)
    {
        /* Wait for Write Synchronization */
    }
}

/* Disable the counter */
void ${TC_INSTANCE_NAME}_CompareStop( void )
{
    ${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_CTRLA &= ~TC_CTRLA_ENABLE_Msk;
    while((${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_SYNCBUSY & TC_SYNCBUSY_ENABLE_Msk) == TC_SYNCBUSY_ENABLE_Msk)
    {
        /* Wait for Write Synchronization */
    }
}

<#if TC_CTRLA_MODE = "COUNT8">
/* Get the current counter value */
uint8_t ${TC_INSTANCE_NAME}_Compare8bitCounterGet( void )
{
    /* Write command to force COUNT register read synchronization */
    ${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_CTRLBSET |= TC_CTRLBSET_CMD_READSYNC;

    while((${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_SYNCBUSY & TC_SYNCBUSY_CTRLB_Msk) == TC_SYNCBUSY_CTRLB_Msk)
    {
        /* Wait for Write Synchronization */
    }

    /* Read current count value */
    return (uint8_t)${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_COUNT;
}

/* Configure counter value */
void ${TC_INSTANCE_NAME}_Compare8bitCounterSet( uint8_t count )
{
    ${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_COUNT = count;

    while((${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_SYNCBUSY & TC_SYNCBUSY_COUNT_Msk) == TC_SYNCBUSY_COUNT_Msk)
    {
        /* Wait for Write Synchronization */
    }
}

/* Configure period value */
void ${TC_INSTANCE_NAME}_Compare8bitPeriodSet( uint8_t period )
{
    <#if TC_COMPARE_CTRLBSET_LUPD == true>
    /* Configure period value */
    ${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_CCBUF[0] = period;
    <#else>
    /* Configure period value */
    ${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_CC[0] = period;
    </#if>
}

/* Read period value */
uint8_t ${TC_INSTANCE_NAME}_Compare8bitPeriodGet( void )
{
    /* Get period value */
    return (uint8_t)${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_CC[0];
}

<#if TC_COMPARE_WAVE_WAVEGEN == "MPWM"> 
/* Configure duty cycle value */
void ${TC_INSTANCE_NAME}_Compare8bitSet( uint8_t compareValue )
{
<#if TC_COMPARE_CTRLBSET_LUPD == true>
    /* Set new compare value for compare channel 1 */
    ${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_CCBUF[1] = compareValue;
<#else>
    /* Set new compare value for compare channel 1 */
    ${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_CC[1] = compareValue;
</#if>
}
</#if>

<#elseif TC_CTRLA_MODE = "COUNT16">
/* Get the current counter value */
uint16_t ${TC_INSTANCE_NAME}_Compare16bitCounterGet( void )
{
    /* Write command to force COUNT register read synchronization */
    ${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_CTRLBSET |= TC_CTRLBSET_CMD_READSYNC;

    while((${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_SYNCBUSY & TC_SYNCBUSY_CTRLB_Msk) == TC_SYNCBUSY_CTRLB_Msk)
    {
        /* Wait for Write Synchronization */
    }

    /* Read current count value */
    return (uint16_t)${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_COUNT;
}

/* Configure counter value */
void ${TC_INSTANCE_NAME}_Compare16bitCounterSet( uint16_t count )
{
    ${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_COUNT = count;

    while((${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_SYNCBUSY & TC_SYNCBUSY_COUNT_Msk) == TC_SYNCBUSY_COUNT_Msk)
    {
        /* Wait for Write Synchronization */
    }
}

/* Configure period value */
void ${TC_INSTANCE_NAME}_Compare16bitPeriodSet( uint16_t period )
{
    <#if TC_COMPARE_CTRLBSET_LUPD == true>
    /* Configure period value */
    ${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_CCBUF[0] = period;
    <#else>
    /* Configure period value */
    ${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_CC[0] = period;
    </#if>
}

/* Read period value */
uint16_t ${TC_INSTANCE_NAME}_Compare16bitPeriodGet( void )
{
    /* Get period value */
    return (uint16_t)${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_CC[0];
}


<#if TC_COMPARE_WAVE_WAVEGEN == "MPWM"> 
/* Configure duty cycle value */
void ${TC_INSTANCE_NAME}_Compare16bitSet( uint16_t compareValue )
{
<#if TC_COMPARE_CTRLBSET_LUPD == true>
    /* Set new compare value for compare channel 1 */
    ${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_CCBUF[1] = compareValue;
<#else>
    /* Set new compare value for compare channel 1 */
    ${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_CC[1] = compareValue;
</#if>
}
</#if>

<#elseif TC_CTRLA_MODE = "COUNT32">
/* Get the current counter value */
uint32_t ${TC_INSTANCE_NAME}_Compare32bitCounterGet( void )
{
    /* Write command to force COUNT register read synchronization */
    ${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_CTRLBSET |= TC_CTRLBSET_CMD_READSYNC;

    while((${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_SYNCBUSY & TC_SYNCBUSY_CTRLB_Msk) == TC_SYNCBUSY_CTRLB_Msk)
    {
        /* Wait for Write Synchronization */
    }

    /* Read current count value */
    return ${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_COUNT;
}

/* Configure counter value */
void ${TC_INSTANCE_NAME}_Compare32bitCounterSet( uint32_t count )
{
    ${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_COUNT = count;

    while((${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_SYNCBUSY & TC_SYNCBUSY_COUNT_Msk) == TC_SYNCBUSY_COUNT_Msk)
    {
        /* Wait for Write Synchronization */
    }
}

/* Configure period value */
void ${TC_INSTANCE_NAME}_Compare32bitPeriodSet( uint32_t period )
{
    <#if TC_COMPARE_CTRLBSET_LUPD == true>
    /* Configure period value */
    ${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_CCBUF[0] = period;
    <#else>
    /* Configure period value */
    ${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_CC[0] = period;
    </#if>
}

/* Read period value */
uint32_t ${TC_INSTANCE_NAME}_Compare32bitPeriodGet( void )
{
    /* Get period value */
    return ${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_CC[0];
}

<#if TC_COMPARE_WAVE_WAVEGEN == "MPWM">
/* Configure duty cycle value */
void ${TC_INSTANCE_NAME}_Compare32bitSet( uint32_t compareValue )
{
    <#if TC_COMPARE_CTRLBSET_LUPD == true>
    /* Set new compare value for compare channel 1 */
    ${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_CCBUF[1] = compareValue;
    <#else>
    /* Set new compare value for compare channel 1 */
    ${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_CC[1] = compareValue;
    </#if>
}
</#if>
</#if>

/* Check ifperiod interrupt flag is set */
bool ${TC_INSTANCE_NAME}_CompareStatusGet( void )
{
    bool compare_status;
    //NVIC_DisableIRQ(${TC_INSTANCE_NAME}_IRQn);
    compare_status = ((${TC_INSTANCE_NAME}_CompareStatus | ${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_INTFLAG) & TC_INTFLAG_OVF_Msk);
    ${TC_INSTANCE_NAME}_CompareStatus = 0U;
    /* Clear timer overflow interrupt */
    ${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_INTFLAG = TC_INTFLAG_OVF_Msk;
    //NVIC_EnableIRQ(${TC_INSTANCE_NAME}_IRQn);
    return compare_status;
}

<#if TC_COMPARE_INTENSET_OVF = true>
/* Register callback function */
void ${TC_INSTANCE_NAME}_CompareCallbackRegister( TC_CALLBACK callback, uintptr_t context )
{
    ${TC_INSTANCE_NAME}_CallbackObject.callback = callback;

    ${TC_INSTANCE_NAME}_CallbackObject.context = context;
}

/* Compare match interrupt handler */
void ${TC_INSTANCE_NAME}_CompareInterruptHandler( void )
{
    if(${TC_INSTANCE_NAME}_CallbackObject.callback != NULL)
    {
        ${TC_INSTANCE_NAME}_CallbackObject.callback(${TC_INSTANCE_NAME}_CallbackObject.context);
    }
    /* clear period interrupt */
    ${TC_INSTANCE_NAME}_REGS->${TC_CTRLA_MODE}.TC_INTFLAG = TC_INTFLAG_OVF_Msk;

}
</#if>



