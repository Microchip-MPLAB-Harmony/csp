/*******************************************************************************
  Real Time Counter (${RTC_INSTANCE_NAME}) PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${RTC_INSTANCE_NAME?lower_case}_timer.c

  Summary:
    ${RTC_INSTANCE_NAME} PLIB Implementation file

  Description:
    This file defines the interface to the RTC peripheral library. This
    library provides access to and control of the associated peripheral
    instance in timer mode.

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

#include "plib_${RTC_INSTANCE_NAME?lower_case}.h"
#include "device.h"
#include <stdlib.h>
<#if core.CoreSysIntFile == true>
#include "interrupts.h"
</#if>

<#if ( RTC_MODE0_INTERRUPT = true && RTC_MODULE_SELECTION = "MODE0" ) ||
     ( RTC_MODE1_INTERRUPT = true && RTC_MODULE_SELECTION = "MODE1" ) >
    <#lt> static volatile RTC_OBJECT ${RTC_INSTANCE_NAME?lower_case}Obj;

</#if>
static void ${RTC_INSTANCE_NAME}_CountReadSynchronization(void)
{
<#if RTC_COUNT_CLOCK_RCONT >
    <#lt>   /* Enable continuous read-synchronization for COUNT register */
    <#lt>   if( (${RTC_INSTANCE_NAME}_REGS->${RTC_MODULE_SELECTION}.RTC_READREQ & RTC_READREQ_RCONT_Msk) != RTC_READREQ_RCONT_Msk)
    <#lt>   {
    <#lt>       ${RTC_INSTANCE_NAME}_REGS->${RTC_MODULE_SELECTION}.RTC_READREQ = RTC_READREQ_RCONT_Msk | RTC_READREQ_ADDR(0x10U);
    <#lt>       ${RTC_INSTANCE_NAME}_REGS->${RTC_MODULE_SELECTION}.RTC_READREQ |= RTC_READREQ_RREQ_Msk;
    <#lt>       while((${RTC_INSTANCE_NAME}_REGS->${RTC_MODULE_SELECTION}.RTC_STATUS & RTC_STATUS_SYNCBUSY_Msk) == RTC_STATUS_SYNCBUSY_Msk)
    <#lt>       {
    <#lt>           /* Wait for Read-Synchronization */
    <#lt>       }
    <#lt>   }
<#else>
    <#lt>   /* Read-synchronization for COUNT register */
    <#lt>   ${RTC_INSTANCE_NAME}_REGS->${RTC_MODULE_SELECTION}.RTC_READREQ = RTC_READREQ_RREQ_Msk | RTC_READREQ_ADDR(0x10U);
    <#lt>   while((${RTC_INSTANCE_NAME}_REGS->${RTC_MODULE_SELECTION}.RTC_STATUS & RTC_STATUS_SYNCBUSY_Msk) == RTC_STATUS_SYNCBUSY_Msk)
    <#lt>   {
    <#lt>       /* Wait for Read-Synchronization */
    <#lt>   }
</#if>
}

void ${RTC_INSTANCE_NAME}_Initialize(void)
{
    <#lt>   /* Writing to CTRL register will trigger write-synchronization */
    <#lt>   ${RTC_INSTANCE_NAME}_REGS->${RTC_MODULE_SELECTION}.RTC_CTRL = RTC_${RTC_MODULE_SELECTION}_CTRL_SWRST_Msk;
    <#lt>   while((${RTC_INSTANCE_NAME}_REGS->${RTC_MODULE_SELECTION}.RTC_STATUS & RTC_STATUS_SYNCBUSY_Msk) == RTC_STATUS_SYNCBUSY_Msk)
    <#lt>   {
    <#lt>       /* Wait for Write-Synchronization */
    <#lt>   }

    <#if RTC_MODULE_SELECTION = "MODE0">
        <#lt>   /* Writing to CTRL register will trigger write-synchronization */
        <#lt>   <@compress single_line=true>${RTC_INSTANCE_NAME}_REGS->MODE0.RTC_CTRL = RTC_MODE0_CTRL_MODE(0U) |
                                                            RTC_MODE0_CTRL_PRESCALER(${RTC_MODE0_PRESCALER}U)
                                                            ${RTC_MODE0_MATCHCLR?then("| RTC_MODE0_CTRL_MATCHCLR_Msk", "")};</@compress>
        <#lt>   while((${RTC_INSTANCE_NAME}_REGS->${RTC_MODULE_SELECTION}.RTC_STATUS & RTC_STATUS_SYNCBUSY_Msk) == RTC_STATUS_SYNCBUSY_Msk)
        <#lt>   {
        <#lt>       /* Wait for Write-Synchronization */
        <#lt>   }

        <#lt>   /* Writing to COMP register will trigger write-synchronization */
        <#lt>   ${RTC_INSTANCE_NAME}_REGS->MODE0.RTC_COMP = 0x${RTC_MODE0_TIMER_COMPARE}U;
        <#lt>   while((${RTC_INSTANCE_NAME}_REGS->${RTC_MODULE_SELECTION}.RTC_STATUS & RTC_STATUS_SYNCBUSY_Msk) == RTC_STATUS_SYNCBUSY_Msk)
        <#lt>   {
        <#lt>       /* Wait for Write-Synchronization */
        <#lt>   }

        <#if (RTC_MODE0_INTERRUPT = true) && (RTC_MODE0_INTENSET != "0")>
            <#lt>   ${RTC_INSTANCE_NAME}_REGS->MODE0.RTC_INTENSET = 0x${RTC_MODE0_INTENSET}U;
        </#if>
        <#if RTC_MODE0_EVCTRL != "0">
            <#lt>   ${RTC_INSTANCE_NAME}_REGS->MODE0.RTC_EVCTRL = 0x${RTC_MODE0_EVCTRL}U;
        </#if>
    <#else>
        <#lt>   /* Writing to CTRL register will trigger write-synchronization */
        <#lt>   <@compress single_line=true>${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_CTRL = RTC_MODE1_CTRL_MODE(1U) |
        <#lt>                                                        RTC_MODE1_CTRL_PRESCALER(${RTC_MODE1_PRESCALER}U);</@compress>

        <#lt>   /* Writing to COMP register will trigger write-synchronization */
        <#lt>   ${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_COMP[0] = 0x${RTC_MODE1_COMPARE0_MATCH_VALUE}U;
        <#lt>   while((${RTC_INSTANCE_NAME}_REGS->${RTC_MODULE_SELECTION}.RTC_STATUS & RTC_STATUS_SYNCBUSY_Msk) == RTC_STATUS_SYNCBUSY_Msk)
        <#lt>   {
        <#lt>       /* Wait for Write-Synchronization */
        <#lt>   }

        <#lt>   /* Writing to COMP register will trigger write-synchronization */
        <#lt>   ${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_COMP[1] = 0x${RTC_MODE1_COMPARE1_MATCH_VALUE}U;
        <#lt>   while((${RTC_INSTANCE_NAME}_REGS->${RTC_MODULE_SELECTION}.RTC_STATUS & RTC_STATUS_SYNCBUSY_Msk) == RTC_STATUS_SYNCBUSY_Msk)
        <#lt>   {
        <#lt>       /* Wait for Write-Synchronization */
        <#lt>   }

        <#lt>   /* Writing to PER register will trigger write-synchronization */
        <#lt>   ${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_PER = 0x${RTC_MODE1_TIMER_COUNTER_PERIOD}U;
        <#lt>   while((${RTC_INSTANCE_NAME}_REGS->${RTC_MODULE_SELECTION}.RTC_STATUS & RTC_STATUS_SYNCBUSY_Msk) == RTC_STATUS_SYNCBUSY_Msk)
        <#lt>   {
        <#lt>       /* Wait for Write-Synchronization */
        <#lt>   }

        <#if (RTC_MODE1_INTERRUPT = true) && (RTC_MODE1_INTENSET != "0")>
            <#lt>   ${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_INTENSET = 0x${RTC_MODE1_INTENSET}U;
        </#if>
        <#if RTC_MODE1_EVCTRL != "0">
            <#lt>   ${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_EVCTRL = 0x${RTC_MODE1_EVCTRL}U;
        </#if>
    </#if>

    <#if RTC_COUNT_CLOCK_RCONT >
        <#lt>   /* Enable continuous read request for COUNT register */
        <#lt>   ${RTC_INSTANCE_NAME}_CountReadSynchronization();
    </#if>
}


<#if RTC_FREQCORR >
    <#lt>void ${RTC_INSTANCE_NAME}_FrequencyCorrect (int8_t correction)
    <#lt>{
    <#lt>    uint8_t abs_correction  = (((uint8_t)correction & 0x80U) != 0U) ? \
    <#lt>                ((0xFFU - (uint8_t)correction) + 0x1U) : (uint8_t)correction;

    <#lt>    /* Convert to positive value and adjust Register sign bit. */
    <#lt>    if (correction < 0)
    <#lt>    {
    <#lt>        abs_correction |= RTC_FREQCORR_SIGN_Msk;
    <#lt>    }

    <#lt>    ${RTC_INSTANCE_NAME}_REGS->${RTC_MODULE_SELECTION}.RTC_FREQCORR = abs_correction;
    <#lt>    while((${RTC_INSTANCE_NAME}_REGS->${RTC_MODULE_SELECTION}.RTC_STATUS & RTC_STATUS_SYNCBUSY_Msk) == RTC_STATUS_SYNCBUSY_Msk)
    <#lt>    {
    <#lt>        /* Wait for Write-Synchronization */
    <#lt>    }
    <#lt>}
</#if>
<#if RTC_MODE0_INTERRUPT = false && RTC_MODULE_SELECTION = "MODE0" ||
     RTC_MODE1_INTERRUPT = false && RTC_MODULE_SELECTION = "MODE1" >

    <#if RTC_MODULE_SELECTION = "MODE0">

    <#lt>bool ${RTC_INSTANCE_NAME}_Timer32CompareHasMatched(void)
    <#lt>{
    <#lt>   bool status = false;

    <#lt>   if((${RTC_INSTANCE_NAME}_REGS->MODE0.RTC_INTFLAG & RTC_MODE0_INTFLAG_CMP0_Msk) == RTC_MODE0_INTFLAG_CMP0_Msk)
    <#lt>   {
    <#lt>       status = true;

    <#lt>       ${RTC_INSTANCE_NAME}_REGS->MODE0.RTC_INTFLAG = RTC_MODE0_INTFLAG_CMP0_Msk;
    <#lt>   }

    <#lt>   return status;
    <#lt>}

    <#lt>bool ${RTC_INSTANCE_NAME}_Timer32CounterHasOverflowed ( void )
    <#lt>{
    <#lt>   bool status = false;

    <#lt>   if((${RTC_INSTANCE_NAME}_REGS->MODE0.RTC_INTFLAG & RTC_MODE0_INTFLAG_OVF_Msk) == RTC_MODE0_INTFLAG_OVF_Msk)
    <#lt>   {
    <#lt>       status = true;

    <#lt>       ${RTC_INSTANCE_NAME}_REGS->MODE0.RTC_INTFLAG = RTC_MODE0_INTFLAG_OVF_Msk;
    <#lt>   }

    <#lt>   return status;
    <#lt>}
    </#if>

    <#if RTC_MODULE_SELECTION = "MODE1">

    <#lt>bool ${RTC_INSTANCE_NAME}_Timer16CounterHasOverflowed ( void )
    <#lt>{
    <#lt>   bool status = false;

    <#lt>   if((${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_INTFLAG & RTC_MODE1_INTFLAG_OVF_Msk ) == RTC_MODE1_INTFLAG_OVF_Msk)
    <#lt>   {
    <#lt>       status = true;
    <#lt>
    <#lt>       /* Clear Counter Overflow Interrupt */
    <#lt>       ${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_INTFLAG = RTC_MODE1_INTFLAG_OVF_Msk;
    <#lt>   }

    <#lt>   return status;
    <#lt>}

    <#lt>bool ${RTC_INSTANCE_NAME}_Timer16Compare0HasMatched(void)
    <#lt>{
    <#lt>   bool status = false;

    <#lt>   if((${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_INTFLAG & RTC_MODE1_INTFLAG_CMP0_Msk ) == RTC_MODE1_INTFLAG_CMP0_Msk)
    <#lt>   {
    <#lt>       status = true;

    <#lt>       /* Clear Compare 0 Match Flag */
    <#lt>       ${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_INTFLAG = RTC_MODE1_INTFLAG_CMP0_Msk;
    <#lt>   }

    <#lt>   return status;
    <#lt>}

    <#lt>bool ${RTC_INSTANCE_NAME}_Timer16Compare1HasMatched(void)
    <#lt>{
    <#lt>   bool status = false;

    <#lt>   if((${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_INTFLAG & RTC_MODE1_INTFLAG_CMP1_Msk ) == RTC_MODE1_INTFLAG_CMP1_Msk)
    <#lt>   {
    <#lt>       status = true;

    <#lt>       /* Clear Compare 1 Match Flag */
    <#lt>       ${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_INTFLAG = RTC_MODE1_INTFLAG_CMP1_Msk;
    <#lt>   }

    <#lt>   return status;
    <#lt>}
    </#if>
</#if>
<#if RTC_MODULE_SELECTION = "MODE0">

    <#lt>void ${RTC_INSTANCE_NAME}_Timer32Start ( void )
    <#lt>{
    <#lt>   /* Writing to CTRL register will trigger write-synchronization */
    <#lt>   ${RTC_INSTANCE_NAME}_REGS->MODE0.RTC_CTRL |= RTC_MODE0_CTRL_ENABLE_Msk;
    <#lt>   while((${RTC_INSTANCE_NAME}_REGS->${RTC_MODULE_SELECTION}.RTC_STATUS & RTC_STATUS_SYNCBUSY_Msk) == RTC_STATUS_SYNCBUSY_Msk)
    <#lt>   {
    <#lt>       /* Wait for Write-synchronization */
    <#lt>   }
    <#lt>}

    <#lt>void ${RTC_INSTANCE_NAME}_Timer32Stop ( void )
    <#lt>{
    <#lt>   /* Writing to CTRL register will trigger write-synchronization */
    <#lt>   ${RTC_INSTANCE_NAME}_REGS->MODE0.RTC_CTRL &= (uint16_t)(~(RTC_MODE0_CTRL_ENABLE_Msk));
    <#lt>   while((${RTC_INSTANCE_NAME}_REGS->${RTC_MODULE_SELECTION}.RTC_STATUS & RTC_STATUS_SYNCBUSY_Msk) == RTC_STATUS_SYNCBUSY_Msk)
    <#lt>   {
    <#lt>       /* Wait for Write-Synchronization */
    <#lt>   }
    <#lt>}

    <#lt>void ${RTC_INSTANCE_NAME}_Timer32CounterSet ( uint32_t count )
    <#lt>{
    <#lt>   /* Writing to COUNT register will trigger write-synchronization */
    <#lt>   ${RTC_INSTANCE_NAME}_REGS->MODE0.RTC_COUNT = count;
    <#lt>   while((${RTC_INSTANCE_NAME}_REGS->${RTC_MODULE_SELECTION}.RTC_STATUS & RTC_STATUS_SYNCBUSY_Msk) == RTC_STATUS_SYNCBUSY_Msk)
    <#lt>   {
    <#lt>       /* Wait for Write-Synchronization */
    <#lt>   }
    <#lt>}

    <#lt>void ${RTC_INSTANCE_NAME}_Timer32CompareSet ( uint32_t compareValue )
    <#lt>{
    <#lt>   /* Writing to COMP register will trigger write-synchronization */
    <#lt>   ${RTC_INSTANCE_NAME}_REGS->MODE0.RTC_COMP = compareValue;
    <#lt>   while((${RTC_INSTANCE_NAME}_REGS->${RTC_MODULE_SELECTION}.RTC_STATUS & RTC_STATUS_SYNCBUSY_Msk) == RTC_STATUS_SYNCBUSY_Msk)
    <#lt>   {
    <#lt>       /* Wait for Write-Synchronization */
    <#lt>   }
    <#lt>}

    <#lt>uint32_t ${RTC_INSTANCE_NAME}_Timer32CounterGet ( void )
    <#lt>{
    <#lt>   /* Enable read-synchronization for COUNT register to avoid CPU stall */
    <#lt>   ${RTC_INSTANCE_NAME}_CountReadSynchronization();
    <#if SYS_TIME_COMPONENT_ID == "sys_time">
        <#lt>   return(${RTC_INSTANCE_NAME}_REGS->MODE0.RTC_COUNT) + 6U;
    <#else>
        <#lt>   return(${RTC_INSTANCE_NAME}_REGS->MODE0.RTC_COUNT);
    </#if>
    <#lt>}

    <#lt>uint32_t ${RTC_INSTANCE_NAME}_Timer32PeriodGet ( void )
    <#lt>{
    <#lt>   <#if RTC_MODE0_MATCHCLR == true>
    <#lt>   return ${RTC_INSTANCE_NAME}_REGS->MODE0.RTC_COMP;
    <#lt>   <#else>
    <#lt>   /* Get 32Bit Compare Value */
    <#lt>   return (RTC_MODE0_COUNT_COUNT_Msk);
    <#lt>   </#if>
    <#lt>}

    <#lt>uint32_t ${RTC_INSTANCE_NAME}_Timer32FrequencyGet ( void )
    <#lt>{
    <#lt>   /* Return Frequency of RTC Clock */
    <#lt>   return RTC_COUNTER_CLOCK_FREQUENCY;
    <#lt>}

    <#if RTC_MODE0_INTERRUPT = true>
        <#lt>void ${RTC_INSTANCE_NAME}_Timer32InterruptEnable(RTC_TIMER32_INT_MASK interrupt)
        <#lt>{
        <#lt>   ${RTC_INSTANCE_NAME}_REGS->MODE0.RTC_INTENSET = (uint8_t)interrupt;
        <#lt>}

        <#lt>void ${RTC_INSTANCE_NAME}_Timer32InterruptDisable(RTC_TIMER32_INT_MASK interrupt)
        <#lt>{
        <#lt>   ${RTC_INSTANCE_NAME}_REGS->MODE0.RTC_INTENCLR = (uint8_t)interrupt;
        <#lt>}
    </#if>
<#else>

    <#lt>void ${RTC_INSTANCE_NAME}_Timer16Start ( void )
    <#lt>{
    <#lt>   /* Writing to CTRL register will trigger write-synchronization */
    <#lt>   ${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_CTRL |= RTC_MODE1_CTRL_ENABLE_Msk;
    <#lt>   while((${RTC_INSTANCE_NAME}_REGS->${RTC_MODULE_SELECTION}.RTC_STATUS & RTC_STATUS_SYNCBUSY_Msk) == RTC_STATUS_SYNCBUSY_Msk)
    <#lt>   {
    <#lt>       /* Wait for Write-Synchronization */
    <#lt>   }
    <#lt>}

    <#lt>void ${RTC_INSTANCE_NAME}_Timer16Stop ( void )
    <#lt>{
    <#lt>   /* Writing to CTRL register will trigger write-synchronization */
    <#lt>   ${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_CTRL &= ~(RTC_MODE1_CTRL_ENABLE_Msk);
    <#lt>   while((${RTC_INSTANCE_NAME}_REGS->${RTC_MODULE_SELECTION}.RTC_STATUS & RTC_STATUS_SYNCBUSY_Msk) == RTC_STATUS_SYNCBUSY_Msk)
    <#lt>   {
    <#lt>       /* Wait for Write-Synchronization */
    <#lt>   }
    <#lt>}

    <#lt>void ${RTC_INSTANCE_NAME}_Timer16CounterSet ( uint16_t count )
    <#lt>{
    <#lt>   /* Writing to COUNT register will trigger write-synchronization */
    <#lt>   ${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_COUNT = count;
    <#lt>   while((${RTC_INSTANCE_NAME}_REGS->${RTC_MODULE_SELECTION}.RTC_STATUS & RTC_STATUS_SYNCBUSY_Msk) == RTC_STATUS_SYNCBUSY_Msk)
    <#lt>   {
    <#lt>       /* Wait for Write-Synchronization */
    <#lt>   }
    <#lt>}

    <#lt>void ${RTC_INSTANCE_NAME}_Timer16PeriodSet ( uint16_t period )
    <#lt>{
    <#lt>   /* Writing to PER register will trigger write-synchronization */
    <#lt>   ${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_PER = period;
    <#lt>   while((${RTC_INSTANCE_NAME}_REGS->${RTC_MODULE_SELECTION}.RTC_STATUS & RTC_STATUS_SYNCBUSY_Msk) == RTC_STATUS_SYNCBUSY_Msk)
    <#lt>   {
    <#lt>       /* Wait for Write-Synchronization */
    <#lt>   }
    <#lt>}

    <#lt>uint16_t ${RTC_INSTANCE_NAME}_Timer16CounterGet ( void )
    <#lt>{
    <#lt>   /* Enable read-synchronization for COUNT register to avoid CPU stall */
    <#lt>   ${RTC_INSTANCE_NAME}_CountReadSynchronization();

    <#if SYS_TIME_COMPONENT_ID == "sys_time">
        <#lt>   return(${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_COUNT) + 6U;
    <#else>
        <#lt>   return(${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_COUNT);
    </#if>
    <#lt>}

    <#lt>uint16_t ${RTC_INSTANCE_NAME}_Timer16PeriodGet ( void )
    <#lt>{
    <#lt>   return (${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_PER);
    <#lt>}

    <#lt>void ${RTC_INSTANCE_NAME}_Timer16Compare0Set ( uint16_t comparisionValue )
    <#lt>{
    <#lt>   /* Writing to COMP register will trigger write-synchronization */
    <#lt>   ${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_COMP[0] = comparisionValue;
    <#lt>   while((${RTC_INSTANCE_NAME}_REGS->${RTC_MODULE_SELECTION}.RTC_STATUS & RTC_STATUS_SYNCBUSY_Msk) == RTC_STATUS_SYNCBUSY_Msk)
    <#lt>   {
    <#lt>       /* Wait for Write-Synchronization */
    <#lt>   }
    <#lt>}

    <#lt>void ${RTC_INSTANCE_NAME}_Timer16Compare1Set ( uint16_t comparisionValue )
    <#lt>{
    <#lt>   /* Writing to COMP register will trigger write-synchronization */
    <#lt>   ${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_COMP[1] = comparisionValue;
    <#lt>   while((${RTC_INSTANCE_NAME}_REGS->${RTC_MODULE_SELECTION}.RTC_STATUS & RTC_STATUS_SYNCBUSY_Msk) == RTC_STATUS_SYNCBUSY_Msk)
    <#lt>   {
    <#lt>       /* Wait for Write-Synchronization */
    <#lt>   }
    <#lt>}

    <#lt>uint32_t ${RTC_INSTANCE_NAME}_Timer16FrequencyGet ( void )
    <#lt>{
    <#lt>   return RTC_COUNTER_CLOCK_FREQUENCY;
    <#lt>}

    <#if RTC_MODE1_INTERRUPT = true>

        <#lt>void ${RTC_INSTANCE_NAME}_Timer16InterruptEnable(RTC_TIMER16_INT_MASK interrupt)
        <#lt>{
        <#lt>   ${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_INTENSET = (uint8_t)interrupt;
        <#lt>}

        <#lt>void ${RTC_INSTANCE_NAME}_Timer16InterruptDisable(RTC_TIMER16_INT_MASK interrupt)
        <#lt>{
        <#lt>   ${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_INTENCLR = (uint8_t)interrupt;
        <#lt>}

    </#if>
</#if>

<#if ( RTC_MODE0_INTERRUPT = true && RTC_MODULE_SELECTION = "MODE0" ) ||
     ( RTC_MODE1_INTERRUPT = true && RTC_MODULE_SELECTION = "MODE1" ) >
    <#if RTC_MODULE_SELECTION = "MODE0" >
        <#lt>void ${RTC_INSTANCE_NAME}_Timer32CallbackRegister ( RTC_TIMER32_CALLBACK callback, uintptr_t context )
        <#lt>{
        <#lt>   ${RTC_INSTANCE_NAME?lower_case}Obj.timer32BitCallback = callback;
        <#lt>   ${RTC_INSTANCE_NAME?lower_case}Obj.context            = context;
        <#lt>}
    <#else>

        <#lt>void ${RTC_INSTANCE_NAME}_Timer16CallbackRegister ( RTC_TIMER16_CALLBACK callback, uintptr_t context )
        <#lt>{
        <#lt>   ${RTC_INSTANCE_NAME?lower_case}Obj.timer16BitCallback = callback;

        <#lt>   ${RTC_INSTANCE_NAME?lower_case}Obj.context            = context;
        <#lt>}
    </#if>

    <#lt>void __attribute__((used)) ${RTC_INSTANCE_NAME}_InterruptHandler(void)
    <#lt>{
    <#if RTC_MODULE_SELECTION = "MODE0">
        <#lt>   ${RTC_INSTANCE_NAME?lower_case}Obj.timer32intCause = (RTC_TIMER32_INT_MASK) ${RTC_INSTANCE_NAME}_REGS->MODE0.RTC_INTFLAG;
        <#lt>   ${RTC_INSTANCE_NAME}_REGS->MODE0.RTC_INTFLAG = RTC_MODE0_INTFLAG_Msk;

        <#lt>   /* Invoke registered Callback function */
        <#lt>   if(${RTC_INSTANCE_NAME?lower_case}Obj.timer32BitCallback != NULL)
        <#lt>   {
        <#lt>       RTC_TIMER32_INT_MASK timer32intCause = ${RTC_INSTANCE_NAME?lower_case}Obj.timer32intCause;
        <#lt>       uintptr_t context = ${RTC_INSTANCE_NAME?lower_case}Obj.context;
        <#lt>       ${RTC_INSTANCE_NAME?lower_case}Obj.timer32BitCallback( timer32intCause, context );
        <#lt>   }
    <#else>
        <#lt>   /* Update the event in RTC Peripheral Callback object */
        <#lt>   ${RTC_INSTANCE_NAME?lower_case}Obj.timer16intCause = (RTC_TIMER16_INT_MASK) ${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_INTFLAG;
        <#lt>   ${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_INTFLAG = RTC_MODE1_INTFLAG_Msk;

        <#lt>   /* Invoke registered Callback function */
        <#lt>   if(${RTC_INSTANCE_NAME?lower_case}Obj.timer16BitCallback != NULL)
        <#lt>   {
        <#lt>       RTC_TIMER16_INT_MASK timer16intCause = ${RTC_INSTANCE_NAME?lower_case}Obj.timer16intCause;
        <#lt>       uintptr_t context = ${RTC_INSTANCE_NAME?lower_case}Obj.context;
        <#lt>       ${RTC_INSTANCE_NAME?lower_case}Obj.timer16BitCallback( timer16intCause, context );
        <#lt>   }
    </#if>
    <#lt>}
</#if>
