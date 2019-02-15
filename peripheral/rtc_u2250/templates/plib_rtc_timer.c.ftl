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
#include <stdlib.h>

<#if ( RTC_MODE0_INTERRUPT = true && RTC_MODULE_SELECTION = "MODE0" ) ||
     ( RTC_MODE1_INTERRUPT = true && RTC_MODULE_SELECTION = "MODE1" ) >
    <#lt>RTC_OBJECT ${RTC_INSTANCE_NAME?lower_case}Obj;

</#if>

void ${RTC_INSTANCE_NAME}_Initialize(void)
{
    ${RTC_INSTANCE_NAME}_REGS->${RTC_MODULE_SELECTION}.RTC_CTRLA = RTC_${RTC_MODULE_SELECTION}_CTRLA_SWRST_Msk;

    while((${RTC_INSTANCE_NAME}_REGS->${RTC_MODULE_SELECTION}.RTC_SYNCBUSY & RTC_${RTC_MODULE_SELECTION}_SYNCBUSY_SWRST_Msk) == RTC_${RTC_MODULE_SELECTION}_SYNCBUSY_SWRST_Msk)
    {
        /* Wait for Synchronization after Software Reset */
    }

    <#if RTC_MODULE_SELECTION = "MODE0">
    <#if TAMP_DETECTION_SUPPORTED??>
        <#if TAMP_DETECTION_SUPPORTED>
            <#if (TAMP_DEBOUNCE_MAJ != "0") || (TAMP_DEBOUNCE_ASYNCH != "0") || TAMP_OUT || TAMP_DMA || (TAMP_DEBOUNCE_FREQUENCY != "0x0") || (TAMP_ACTIVE_FREQUENCY != "0x0")>
            <#lt>    <@compress single_line=true>${RTC_INSTANCE_NAME}_REGS->MODE0.RTC_CTRLB = RTC_MODE0_CTRLB_DEBF(${TAMP_DEBOUNCE_FREQUENCY})|
                                                                    RTC_MODE0_CTRLB_ACTF(${TAMP_ACTIVE_FREQUENCY})
                                                                    ${TAMP_OUT?then("| RTC_MODE0_CTRLB_RTCOUT_Msk", "")}
                                                                    ${TAMP_DMA?then("| RTC_MODE0_CTRLB_DMAEN_Msk", "")}
                                                                    ${(TAMP_DEBOUNCE_ASYNCH != "0")?then("| RTC_MODE0_CTRLB_DEBASYNC_Msk", "")}
                                                                    ${(TAMP_DEBOUNCE_MAJ != "0")?then("| RTC_MODE0_CTRLB_DEBMAJ_Msk", "")};</@compress>
              </#if>

            <#if (TAMP_CHANNEL0_ACTION != '0') || (TAMP_CHANNEL1_ACTION != '0') ||(TAMP_CHANNEL2_ACTION != '0') ||(TAMP_CHANNEL3_ACTION != '0') ||(TAMP_CHANNEL4_ACTION != '0')>
            <#lt>    ${RTC_INSTANCE_NAME}_REGS->MODE0.RTC_TAMPCTRL = RTC_TAMPCTRL_IN0ACT(${TAMP_CHANNEL0_ACTION}) ${(TAMP_CHANNEL0_LEVEL != "0")?then("| RTC_TAMPCTRL_TAMPLVL0_Msk", "")} ${(TAMP_CHANNEL0_DEBNC)?then("| RTC_TAMPCTRL_DEBNC0_Msk", "")} | \
            <#lt>                                   RTC_TAMPCTRL_IN1ACT(${TAMP_CHANNEL1_ACTION}) ${(TAMP_CHANNEL1_LEVEL != "0")?then("| RTC_TAMPCTRL_TAMPLVL1_Msk", "")}${(TAMP_CHANNEL1_DEBNC)?then("| RTC_TAMPCTRL_DEBNC1_Msk", "")} | \
            <#lt>                                   RTC_TAMPCTRL_IN2ACT(${TAMP_CHANNEL2_ACTION}) ${(TAMP_CHANNEL2_LEVEL != "0")?then("| RTC_TAMPCTRL_TAMPLVL2_Msk", "")}${(TAMP_CHANNEL2_DEBNC)?then("| RTC_TAMPCTRL_DEBNC2_Msk", "")} | \
            <#lt>                                   RTC_TAMPCTRL_IN3ACT(${TAMP_CHANNEL3_ACTION}) ${(TAMP_CHANNEL3_LEVEL != "0")?then("| RTC_TAMPCTRL_TAMPLVL3_Msk", "")}${(TAMP_CHANNEL3_DEBNC)?then("| RTC_TAMPCTRL_DEBNC3_Msk", "")} | \
            <#lt>                                   RTC_TAMPCTRL_IN4ACT(${TAMP_CHANNEL4_ACTION}) ${(TAMP_CHANNEL4_LEVEL != "0")?then("| RTC_TAMPCTRL_TAMPLVL4_Msk", "")}${(TAMP_CHANNEL4_DEBNC)?then("| RTC_TAMPCTRL_DEBNC4_Msk", "")};
            </#if>
        </#if>
    </#if>

        <#lt>    <@compress single_line=true>${RTC_INSTANCE_NAME}_REGS->MODE0.RTC_CTRLA = RTC_MODE0_CTRLA_MODE(0) |
                                                                RTC_MODE0_CTRLA_PRESCALER(${RTC_MODE0_PRESCALER}) |
                                                                RTC_MODE0_CTRLA_COUNTSYNC_Msk
                                                                ${RTC_MODE0_MATCHCLR?then("|RTC_MODE0_CTRLA_MATCHCLR_Msk", "")}
                                                                <#if TAMP_DETECTION_SUPPORTED??>
                                                                    <#if TAMP_DETECTION_SUPPORTED>
                                                                        ${TAMP_RESET_GP?then("| RTC_MODE0_CTRLA_GPTRST_Msk", "")}
                                                                        ${TAMP_RESET_BACKUP?then("| RTC_MODE0_CTRLA_BKTRST_Msk", "")}
                                                                    </#if>
                                                                </#if>;</@compress>

        <#if RTC_MODE0_NUM_COMP == 1>
        <#lt>   ${RTC_INSTANCE_NAME}_REGS->MODE0.RTC_COMP = 0x${RTC_MODE0_TIMER_COMPARE};

        <#else>
        <#list 0..(RTC_MODE0_NUM_COMP - 1) as i>
        <#assign compareReg = "RTC_MODE0_TIMER_COMPARE" + i>
        <#lt>    ${RTC_INSTANCE_NAME}_REGS->MODE0.RTC_COMP[${i}] = 0x${.vars[compareReg]};

        </#list>
        </#if>
        <#if (RTC_MODE0_INTERRUPT = true) && (RTC_MODE0_INTENSET != "0")>
            <#lt>    ${RTC_INSTANCE_NAME}_REGS->MODE0.RTC_INTENSET = 0x${RTC_MODE0_INTENSET};

        </#if>
        <#if RTC_MODE0_EVCTRL != "0">
            <#lt>    ${RTC_INSTANCE_NAME}_REGS->MODE0.RTC_EVCTRL = 0x${RTC_MODE0_EVCTRL};
        </#if>
    <#else>
    <#if TAMP_DETECTION_SUPPORTED??>
        <#if TAMP_DETECTION_SUPPORTED>
            <#if (TAMP_DEBOUNCE_MAJ != "0") || (TAMP_DEBOUNCE_ASYNCH != "0") || TAMP_OUT || TAMP_DMA || (TAMP_DEBOUNCE_FREQUENCY != "0x0") || (TAMP_ACTIVE_FREQUENCY != "0x0")>
            <#lt>    <@compress single_line=true>${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_CTRLB = RTC_MODE1_CTRLB_DEBF(${TAMP_DEBOUNCE_FREQUENCY})|
                                                                    RTC_MODE1_CTRLB_ACTF(${TAMP_ACTIVE_FREQUENCY})
                                                                    ${TAMP_OUT?then("| RTC_MODE1_CTRLB_RTCOUT_Msk", "")}
                                                                    ${TAMP_DMA?then("| RTC_MODE1_CTRLB_DMAEN_Msk", "")}
                                                                    ${(TAMP_DEBOUNCE_ASYNCH != "0")?then("| RTC_MODE1_CTRLB_DEBASYNC_Msk", "")}
                                                                    ${(TAMP_DEBOUNCE_MAJ != "0")?then("| RTC_MODE1_CTRLB_DEBMAJ_Msk", "")};</@compress>
              </#if>

            <#if (TAMP_CHANNEL0_ACTION != '0') || (TAMP_CHANNEL1_ACTION != '0') ||(TAMP_CHANNEL2_ACTION != '0') ||(TAMP_CHANNEL3_ACTION != '0') ||(TAMP_CHANNEL4_ACTION != '0')>
            <#lt>    ${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_TAMPCTRL = RTC_TAMPCTRL_IN0ACT(${TAMP_CHANNEL0_ACTION}) ${(TAMP_CHANNEL0_LEVEL != "0")?then("| RTC_TAMPCTRL_TAMPLVL0_Msk", "")} ${(TAMP_CHANNEL0_DEBNC)?then("| RTC_TAMPCTRL_DEBNC0_Msk", "")} | \
            <#lt>                                   RTC_TAMPCTRL_IN1ACT(${TAMP_CHANNEL1_ACTION}) ${(TAMP_CHANNEL1_LEVEL != "0")?then("| RTC_TAMPCTRL_TAMPLVL1_Msk", "")}${(TAMP_CHANNEL1_DEBNC)?then("| RTC_TAMPCTRL_DEBNC1_Msk", "")} | \
            <#lt>                                   RTC_TAMPCTRL_IN2ACT(${TAMP_CHANNEL2_ACTION}) ${(TAMP_CHANNEL2_LEVEL != "0")?then("| RTC_TAMPCTRL_TAMPLVL2_Msk", "")}${(TAMP_CHANNEL2_DEBNC)?then("| RTC_TAMPCTRL_DEBNC2_Msk", "")} | \
            <#lt>                                   RTC_TAMPCTRL_IN3ACT(${TAMP_CHANNEL3_ACTION}) ${(TAMP_CHANNEL3_LEVEL != "0")?then("| RTC_TAMPCTRL_TAMPLVL3_Msk", "")}${(TAMP_CHANNEL3_DEBNC)?then("| RTC_TAMPCTRL_DEBNC3_Msk", "")} | \
            <#lt>                                   RTC_TAMPCTRL_IN4ACT(${TAMP_CHANNEL4_ACTION}) ${(TAMP_CHANNEL4_LEVEL != "0")?then("| RTC_TAMPCTRL_TAMPLVL4_Msk", "")}${(TAMP_CHANNEL4_DEBNC)?then("| RTC_TAMPCTRL_DEBNC4_Msk", "")};
            </#if>
        </#if>
    </#if>

        <#lt>    <@compress single_line=true>${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_CTRLA = RTC_MODE1_CTRLA_MODE(1) |
        <#lt>                                                        RTC_MODE1_CTRLA_PRESCALER(${RTC_MODE1_PRESCALER}) |
        <#lt>                                                        RTC_MODE1_CTRLA_COUNTSYNC_Msk                                                             <#if TAMP_DETECTION_SUPPORTED??>
                                                                        <#if TAMP_DETECTION_SUPPORTED>
                                                                            ${TAMP_RESET_GP?then("| RTC_MODE1_CTRLA_GPTRST_Msk", "")}
                                                                            ${TAMP_RESET_BACKUP?then("| RTC_MODE1_CTRLA_BKTRST_Msk", "")}
                                                                        </#if>
                                                                    </#if>;</@compress>

        <#list 0..(RTC_MODE1_NUM_COMP - 1) as i>
        <#assign compareReg = "RTC_MODE1_COMPARE" + i + "_MATCH_VALUE">
        <#lt>    ${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_COMP[${i}] = 0x${.vars[compareReg]};

        </#list>
        <#lt>    ${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_PER = 0x${RTC_MODE1_TIMER_COUNTER_PERIOD};

        <#if (RTC_MODE1_INTERRUPT = true) && (RTC_MODE1_INTENSET != "0")>
        <#lt>    ${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_INTENSET = 0x${RTC_MODE1_INTENSET};

        </#if>
        <#if    RTC_MODE1_EVCTRL != "0">
            <#lt>    ${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_EVCTRL = 0x${RTC_MODE1_EVCTRL};
        </#if>
    </#if>
}

<#if RTC_FREQCORR >
    <#lt>void ${RTC_INSTANCE_NAME}_FrequencyCorrect (int8_t correction)
    <#lt>{
    <#lt>    uint32_t newCorrectionValue = 0;

    <#lt>    newCorrectionValue = abs(correction);

    <#lt>    /* Convert to positive value and adjust register sign bit. */
    <#lt>    if (correction < 0)
    <#lt>    {
    <#lt>        newCorrectionValue |= RTC_FREQCORR_SIGN_Msk;
    <#lt>    }

    <#lt>    ${RTC_INSTANCE_NAME}_REGS->${RTC_MODULE_SELECTION}.RTC_FREQCORR = newCorrectionValue;
    <#lt>    while((${RTC_INSTANCE_NAME}_REGS->${RTC_MODULE_SELECTION}.RTC_SYNCBUSY & RTC_${RTC_MODULE_SELECTION}_SYNCBUSY_FREQCORR_Msk) == RTC_${RTC_MODULE_SELECTION}_SYNCBUSY_FREQCORR_Msk)
    <#lt>    {
    <#lt>        /* Wait for Synchronization after writing Value to FREQCORR */
    <#lt>    }
    <#lt>}
</#if>
<#if RTC_MODE0_INTERRUPT = false && RTC_MODULE_SELECTION = "MODE0" ||
     RTC_MODE1_INTERRUPT = false && RTC_MODULE_SELECTION = "MODE1" >

    <#lt>bool ${RTC_INSTANCE_NAME}_PeriodicIntervalHasCompleted (RTC_PERIODIC_INT_MASK period)
    <#lt>{
    <#lt>   bool periodIntervalComplete = false;
        <#if RTC_MODULE_SELECTION = "MODE0" >
    <#lt>   if( (${RTC_INSTANCE_NAME}_REGS->MODE0.RTC_INTFLAG & period) == period)
    <#lt>   {
    <#lt>       periodIntervalComplete = true;

    <#lt>       /* Clear Periodic Interval Interrupt */
    <#lt>       ${RTC_INSTANCE_NAME}_REGS->MODE0.RTC_INTFLAG = period;
    <#lt>   }
        <#elseif RTC_MODULE_SELECTION = "MODE1" >
    <#lt>   if( (${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_INTFLAG & period) == period)
    <#lt>   {
    <#lt>       periodIntervalComplete = true;

    <#lt>       /* Clear Periodic Interval Interrupt */
    <#lt>       ${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_INTFLAG = period;
    <#lt>   }
        </#if>

    <#lt>    return periodIntervalComplete;
    <#lt>}

    <#if RTC_MODULE_SELECTION = "MODE0">
        <#if RTC_MODE0_NUM_COMP == 1>
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
        <#else>
            <#list 0..(RTC_MODE0_NUM_COMP - 1) as i>
                <#lt>bool ${RTC_INSTANCE_NAME}_Timer32Compare${i}HasMatched(void)
                <#lt>{
                <#lt>   bool status = false;

                <#lt>   if((${RTC_INSTANCE_NAME}_REGS->MODE0.RTC_INTFLAG & RTC_MODE0_INTFLAG_CMP${i}_Msk) == RTC_MODE0_INTFLAG_CMP${i}_Msk)
                <#lt>   {
                <#lt>       status = true;
                <#lt>       ${RTC_INSTANCE_NAME}_REGS->MODE0.RTC_INTFLAG = RTC_MODE0_INTFLAG_CMP${i}_Msk;
                <#lt>   }

                <#lt>   return status;
                <#lt>}

            </#list>
        </#if>
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
        <#lt>bool ${RTC_INSTANCE_NAME}_Timer16PeriodHasExpired ( void )
        <#lt>{
        <#lt>   bool status = false;

        <#lt>   if((${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_INTFLAG & RTC_MODE1_INTFLAG_OVF_Msk ) == RTC_MODE1_INTFLAG_OVF_Msk)
        <#lt>   {
        <#lt>       status = true;
        <#lt>       ${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_INTFLAG = RTC_MODE1_INTFLAG_OVF_Msk;
        <#lt>   }
        <#lt>   return status;
        <#lt>}

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

        <#list 0..(RTC_MODE1_NUM_COMP - 1) as i>
            <#lt>bool ${RTC_INSTANCE_NAME}_Timer16Compare${i}HasMatched(void)
            <#lt>{
            <#lt>   bool status = false;

            <#lt>   if((${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_INTFLAG & RTC_MODE1_INTFLAG_CMP${i}_Msk ) == RTC_MODE1_INTFLAG_CMP${i}_Msk)
            <#lt>   {
            <#lt>       status = true;

            <#lt>       /* Clear Compare ${i} Match Flag */
            <#lt>       ${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_INTFLAG = RTC_MODE1_INTFLAG_CMP${i}_Msk;
            <#lt>   }
            <#lt>   return status;
            <#lt>}

        </#list>
    </#if>
</#if>
<#if RTC_MODULE_SELECTION = "MODE0">

    <#lt>void ${RTC_INSTANCE_NAME}_Timer32Start ( void )
    <#lt>{
    <#lt>    ${RTC_INSTANCE_NAME}_REGS->MODE0.RTC_CTRLA |= RTC_MODE0_CTRLA_ENABLE_Msk;

    <#lt>    while((${RTC_INSTANCE_NAME}_REGS->MODE0.RTC_SYNCBUSY & RTC_MODE0_SYNCBUSY_ENABLE_Msk) == RTC_MODE0_SYNCBUSY_ENABLE_Msk)
    <#lt>    {
    <#lt>        /* Wait for synchronization after Enabling RTC */
    <#lt>    }
    <#lt>}


    <#lt>void ${RTC_INSTANCE_NAME}_Timer32Stop ( void )
    <#lt>{
    <#lt>    ${RTC_INSTANCE_NAME}_REGS->MODE0.RTC_CTRLA &= ~(RTC_MODE0_CTRLA_ENABLE_Msk);

    <#lt>    while((${RTC_INSTANCE_NAME}_REGS->MODE0.RTC_SYNCBUSY & RTC_MODE0_SYNCBUSY_ENABLE_Msk) == RTC_MODE0_SYNCBUSY_ENABLE_Msk)
    <#lt>    {
    <#lt>        /* Wait for Synchronization after Disabling RTC */
    <#lt>    }
    <#lt>}

    <#lt>void ${RTC_INSTANCE_NAME}_Timer32CounterSet ( uint32_t count )
    <#lt>{
    <#lt>    ${RTC_INSTANCE_NAME}_REGS->MODE0.RTC_COUNT = count;

    <#lt>    while((${RTC_INSTANCE_NAME}_REGS->MODE0.RTC_SYNCBUSY & RTC_MODE0_SYNCBUSY_COUNT_Msk) == RTC_MODE0_SYNCBUSY_COUNT_Msk)
    <#lt>    {
    <#lt>        /* Wait for Synchronization after writing value to Count Register */
    <#lt>    }
    <#lt>}

    <#if RTC_MODE0_NUM_COMP == 1>
        <#lt>void ${RTC_INSTANCE_NAME}_Timer32CompareSet ( uint32_t compareValue )
        <#lt>{
        <#lt>    ${RTC_INSTANCE_NAME}_REGS->MODE0.RTC_COMP = compareValue;

        <#lt>    while((${RTC_INSTANCE_NAME}_REGS->MODE0.RTC_SYNCBUSY & RTC_MODE0_SYNCBUSY_COMP0_Msk) == RTC_MODE0_SYNCBUSY_COMP0_Msk)
        <#lt>    {
        <#lt>        /* Wait for Synchronization after writing Compare Value */
        <#lt>    }
        <#lt>}
    <#else>
        <#list 0..(RTC_MODE0_NUM_COMP - 1) as i>
            <#lt>void ${RTC_INSTANCE_NAME}_Timer32Compare${i}Set ( uint32_t compareValue )
            <#lt>{
            <#lt>    ${RTC_INSTANCE_NAME}_REGS->MODE0.RTC_COMP[${i}] = compareValue;

            <#lt>    while((${RTC_INSTANCE_NAME}_REGS->MODE0.RTC_SYNCBUSY & RTC_MODE0_SYNCBUSY_COMP${i}_Msk) == RTC_MODE0_SYNCBUSY_COMP${i}_Msk)
            <#lt>    {
            <#lt>        /* Wait for Synchronization after writing Compare Value */
            <#lt>    }
            <#lt>}
        </#list>
    </#if>
    <#lt>uint32_t ${RTC_INSTANCE_NAME}_Timer32CounterGet ( void )
    <#lt>{
    <#lt>    while((${RTC_INSTANCE_NAME}_REGS->MODE0.RTC_SYNCBUSY & RTC_MODE0_SYNCBUSY_COUNT_Msk) == RTC_MODE0_SYNCBUSY_COUNT_Msk)
    <#lt>    {
    <#lt>        /* Wait for Synchronization before reading value from Count Register */
    <#lt>    }

    <#lt>    return(${RTC_INSTANCE_NAME}_REGS->MODE0.RTC_COUNT + 4);
    <#lt>}

    <#lt>uint32_t ${RTC_INSTANCE_NAME}_Timer32PeriodGet ( void )
    <#lt>{
    <#lt>    /* Get 32Bit Compare Value */
    <#lt>    return (RTC_MODE0_COUNT_COUNT_Msk);
    <#lt>}

    <#lt>uint32_t ${RTC_INSTANCE_NAME}_Timer32FrequencyGet ( void )
    <#lt>{
    <#lt>    /* Return Frequency of RTC Clock */
    <#lt>    return RTC_COUNTER_CLOCK_FREQUENCY;
    <#lt>}

    <#if RTC_MODE0_INTERRUPT = true>
        <#lt>void ${RTC_INSTANCE_NAME}_Timer32InterruptEnable(RTC_TIMER32_INT_MASK interrupt)
        <#lt>{
        <#lt>    ${RTC_INSTANCE_NAME}_REGS->MODE0.RTC_INTENSET = interrupt;
        <#lt>}

        <#lt>void ${RTC_INSTANCE_NAME}_Timer32InterruptDisable(RTC_TIMER32_INT_MASK interrupt)
        <#lt>{
        <#lt>    ${RTC_INSTANCE_NAME}_REGS->MODE0.RTC_INTENCLR = interrupt;
        <#lt>}

    </#if>
<#else>

    <#lt>void ${RTC_INSTANCE_NAME}_Timer16Start ( void )
    <#lt>{
    <#lt>    ${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_CTRLA |= RTC_MODE1_CTRLA_ENABLE_Msk;

    <#lt>    while((${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_SYNCBUSY & RTC_MODE1_SYNCBUSY_ENABLE_Msk) == RTC_MODE1_SYNCBUSY_ENABLE_Msk)
    <#lt>    {
    <#lt>        /* Wait for Synchronization after Enabling RTC */
    <#lt>    }
    <#lt>}

    <#lt>void ${RTC_INSTANCE_NAME}_Timer16Stop ( void )
    <#lt>{
    <#lt>    ${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_CTRLA &= ~(RTC_MODE1_CTRLA_ENABLE_Msk);

    <#lt>    while((${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_SYNCBUSY & RTC_MODE1_SYNCBUSY_ENABLE_Msk) == RTC_MODE1_SYNCBUSY_ENABLE_Msk)
    <#lt>    {
    <#lt>        /* Wait for Synchronization after Disabling RTC */
    <#lt>    }
    <#lt>}


    <#lt>void ${RTC_INSTANCE_NAME}_Timer16CounterSet ( uint16_t count )
    <#lt>{
    <#lt>    ${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_COUNT = count;

    <#lt>    while((${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_SYNCBUSY & RTC_MODE1_SYNCBUSY_COUNT_Msk) == RTC_MODE1_SYNCBUSY_COUNT_Msk)
    <#lt>    {
    <#lt>        /* Wait for Synchronization after writing value to Count Register */
    <#lt>    }
    <#lt>}


    <#lt>void ${RTC_INSTANCE_NAME}_Timer16PeriodSet ( uint16_t period )
    <#lt>{
    <#lt>    ${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_PER = period;

    <#lt>    while((${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_SYNCBUSY & RTC_MODE1_SYNCBUSY_PER_Msk) == RTC_MODE1_SYNCBUSY_PER_Msk)
    <#lt>    {
    <#lt>        /* Wait for Synchronization after writing Counter Period */
    <#lt>    }
    <#lt>}

    <#lt>uint16_t ${RTC_INSTANCE_NAME}_Timer16CounterGet ( void )
    <#lt>{
    <#lt>    while((${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_SYNCBUSY & RTC_MODE1_SYNCBUSY_COUNT_Msk) == RTC_MODE1_SYNCBUSY_COUNT_Msk)
    <#lt>    {
    <#lt>        /* Wait for Synchronization after reading value from Count Register */
    <#lt>    }
    <#lt>    return (${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_COUNT);
    <#lt>}

    <#lt>uint16_t ${RTC_INSTANCE_NAME}_Timer16PeriodGet ( void )
    <#lt>{
    <#lt>    return (${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_PER);
    <#lt>}

    <#list 0..(RTC_MODE1_NUM_COMP - 1) as i>
        <#lt>void ${RTC_INSTANCE_NAME}_Timer16Compare${i}Set ( uint16_t comparisionValue )
        <#lt>{
        <#lt>   ${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_COMP[${i}] = comparisionValue;

        <#lt>   while((${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_SYNCBUSY & RTC_MODE1_SYNCBUSY_COMP${i}_Msk) == RTC_MODE1_SYNCBUSY_COMP${i}_Msk)
        <#lt>   {
        <#lt>       /* Wait for Synchronization after writing Compare Value */
        <#lt>   }
        <#lt>}
    </#list>

    <#lt>uint32_t ${RTC_INSTANCE_NAME}_Timer16FrequencyGet ( void )
    <#lt>{
    <#lt>    return RTC_COUNTER_CLOCK_FREQUENCY;
    <#lt>}

    <#if RTC_MODE1_INTERRUPT = true>

        <#lt>void ${RTC_INSTANCE_NAME}_Timer16InterruptEnable( RTC_TIMER16_INT_MASK interrupt )
        <#lt>{
        <#lt>    ${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_INTENSET = interrupt;
        <#lt>}

        <#lt>void ${RTC_INSTANCE_NAME}_Timer16InterruptDisable( RTC_TIMER16_INT_MASK interrupt )
        <#lt>{
        <#lt>    ${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_INTENCLR = interrupt;
        <#lt>}

    </#if>
</#if>
<#if RTC_MODULE_SELECTION = "MODE0">
    <#assign mode = 0>
<#else>
    <#assign mode = 1>
</#if>
<#if TAMP_DETECTION_SUPPORTED??>
        <#if TAMP_DETECTION_SUPPORTED>
        <#lt>void ${RTC_INSTANCE_NAME}_BackupRegisterSet( BACKUP_REGISTER reg, uint32_t value )
        <#lt>{
        <#lt>    ${RTC_INSTANCE_NAME}_REGS->MODE${mode}.RTC_BKUP[reg] = value;
        <#lt>}

        <#lt>uint32_t ${RTC_INSTANCE_NAME}_BackupRegisterGet( BACKUP_REGISTER reg )
        <#lt>{
        <#lt>    return(${RTC_INSTANCE_NAME}_REGS->MODE${mode}.RTC_BKUP[reg]);
        <#lt>}

        <#lt> TAMPER_CHANNEL ${RTC_INSTANCE_NAME}_TamperSourceGet( void )
        <#lt>{
        <#lt>    return((${RTC_INSTANCE_NAME}_REGS->MODE${mode}.RTC_TAMPID) & (0xFF));
        <#lt>}

        <#if RTC_MODULE_SELECTION = "MODE0">
            <#lt>uint32_t ${RTC_INSTANCE_NAME}_Timer32TimeStampGet( void )
            <#lt>{
            <#lt>    return(${RTC_INSTANCE_NAME}_REGS->MODE0.RTC_COUNT);
            <#lt>}
        <#else>
            <#lt>uint16_t ${RTC_INSTANCE_NAME}_Timer16TimeStampGet( void )
            <#lt>{
            <#lt>    return(${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_COUNT);
            <#lt>}
        </#if>
    </#if>
</#if>

<#if ( RTC_MODE0_INTERRUPT = true && RTC_MODULE_SELECTION = "MODE0" ) ||
     ( RTC_MODE1_INTERRUPT = true && RTC_MODULE_SELECTION = "MODE1" ) >
    <#if RTC_MODULE_SELECTION = "MODE0" >
        <#lt>void ${RTC_INSTANCE_NAME}_Timer32CallbackRegister ( RTC_TIMER32_CALLBACK callback, uintptr_t context )
        <#lt>{
        <#lt>    ${RTC_INSTANCE_NAME?lower_case}Obj.timer32BitCallback = callback;
        <#lt>    ${RTC_INSTANCE_NAME?lower_case}Obj.context            = context;
        <#lt>}
    <#else>

        <#lt>void ${RTC_INSTANCE_NAME}_Timer16CallbackRegister ( RTC_TIMER16_CALLBACK callback, uintptr_t context )
        <#lt>{
        <#lt>    ${RTC_INSTANCE_NAME?lower_case}Obj.timer16BitCallback = callback;
        <#lt>    ${RTC_INSTANCE_NAME?lower_case}Obj.context            = context;
        <#lt>}
    </#if>

    <#lt>void ${RTC_INSTANCE_NAME}_InterruptHandler( void )
    <#lt>{
    <#if RTC_MODULE_SELECTION = "MODE0">
        <#lt>    ${RTC_INSTANCE_NAME?lower_case}Obj.timer32intCause = ${RTC_INSTANCE_NAME}_REGS->MODE0.RTC_INTFLAG;

        <#lt>    /* Invoke registered Callback function */
        <#lt>    if(${RTC_INSTANCE_NAME?lower_case}Obj.timer32BitCallback != NULL)
        <#lt>    {
        <#lt>        ${RTC_INSTANCE_NAME?lower_case}Obj.timer32BitCallback( ${RTC_INSTANCE_NAME?lower_case}Obj.timer32intCause, ${RTC_INSTANCE_NAME?lower_case}Obj.context );
        <#lt>    }

        <#lt>    ${RTC_INSTANCE_NAME}_REGS->MODE0.RTC_INTFLAG = RTC_MODE0_INTFLAG_Msk;
    <#else>
        <#lt>    /* Update the event in RTC Peripheral Callback object */
        <#lt>    ${RTC_INSTANCE_NAME?lower_case}Obj.timer16intCause = ${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_INTFLAG;

        <#lt>    /* Invoke registered Callback function */
        <#lt>    if(${RTC_INSTANCE_NAME?lower_case}Obj.timer16BitCallback != NULL)
        <#lt>    {
        <#lt>        ${RTC_INSTANCE_NAME?lower_case}Obj.timer16BitCallback( ${RTC_INSTANCE_NAME?lower_case}Obj.timer16intCause, ${RTC_INSTANCE_NAME?lower_case}Obj.context );
        <#lt>    }

        <#lt>    ${RTC_INSTANCE_NAME}_REGS->MODE1.RTC_INTFLAG = RTC_MODE1_INTFLAG_Msk;
    </#if>
    <#lt>}
</#if>
