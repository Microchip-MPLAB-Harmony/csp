/*******************************************************************************
  Temperature Sensor (${TSENS_INSTANCE_NAME}) PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_${TSENS_INSTANCE_NAME?lower_case}.c

  Summary
    ${TSENS_INSTANCE_NAME} PLIB Implementation File.

  Description
    This file defines the interface to the TSENS peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

  Remarks:
    None.

*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
* Copyright (C) 2023 Microchip Technology Inc. and its subsidiaries.
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

<#if core.CoreSysIntFile == true>
#include "interrupts.h"
</#if>
#include "plib_${TSENS_INSTANCE_NAME?lower_case}.h"
<#compress>
<#assign TSENS_CTRLC_VAL = "">
<#assign TSENS_EVCTRL_VAL = "">
<#assign TSENS_INTENSET_VAL = "">
<#assign TSENS_CTRLA_VAL = "">


<#if TSENS_CONV_TRIGGER == "Free Run">
    <#if TSENS_CTRLC_VAL != "">
        <#assign TSENS_CTRLC_VAL = TSENS_CTRLC_VAL + " | TSENS_CTRLC_FREERUN_Msk">
    <#else>
        <#assign TSENS_CTRLC_VAL = "TSENS_CTRLC_FREERUN_Msk">
    </#if>
</#if>

<#if TSENS_CTRLC_WINMODE != "0" && TSENS_WINDOW_OUTPUT_EVENT == true>
    <#if TSENS_EVCTRL_VAL != "">
        <#assign TSENS_EVCTRL_VAL = TSENS_EVCTRL_VAL + " | TSENS_EVCTRL_WINEO_Msk">
    <#else>
        <#assign TSENS_EVCTRL_VAL = "TSENS_EVCTRL_WINEO_Msk">
    </#if>
</#if>

<#if TSENS_CONV_TRIGGER == "HW Event Trigger">
    <#if TSENS_EVCTRL_START == "1">
        <#if TSENS_EVCTRL_VAL != "">
            <#assign TSENS_EVCTRL_VAL = TSENS_EVCTRL_VAL + " | TSENS_EVCTRL_STARTEI_Msk">
        <#else>
            <#assign TSENS_EVCTRL_VAL = "TSENS_EVCTRL_STARTEI_Msk">
        </#if>
    <#elseif TSENS_EVCTRL_START == "2">
        <#if TSENS_EVCTRL_VAL != "">
            <#assign TSENS_EVCTRL_VAL = TSENS_EVCTRL_VAL + " | TSENS_EVCTRL_STARTEI_Msk | TSENS_EVCTRL_STARTINV_Msk">
        <#else>
            <#assign TSENS_EVCTRL_VAL = "TSENS_EVCTRL_STARTEI_Msk | TSENS_EVCTRL_STARTINV_Msk">
        </#if>
    </#if>
</#if>

<#if TSENS_INTENSET_RESRDY == true>
    <#if TSENS_INTENSET_VAL != "">
        <#assign TSENS_INTENSET_VAL = TSENS_INTENSET_VAL + " | TSENS_INTENSET_RESRDY_Msk">
    <#else>
        <#assign TSENS_INTENSET_VAL = "TSENS_INTENSET_RESRDY_Msk">
    </#if>
</#if>
<#if TSENS_CTRLC_WINMODE != "0" && TSENS_INTENSET_WINMON == true>
    <#if TSENS_INTENSET_VAL != "">
        <#assign TSENS_INTENSET_VAL = TSENS_INTENSET_VAL + " | TSENS_INTENSET_WINMON_Msk">
    <#else>
        <#assign TSENS_INTENSET_VAL = "TSENS_INTENSET_WINMON_Msk">
    </#if>
</#if>

<#if TSENS_CTRLA_RUNSTDBY == true>
    <#assign TSENS_CTRLA_VAL = "TSENS_CTRLA_RUNSTDBY_Msk">
</#if>
</#compress>

// *****************************************************************************
// *****************************************************************************
// Section: Global Data
// *****************************************************************************
// *****************************************************************************
<#if TSENS_INTENSET_RESRDY = true || (TSENS_CTRLC_WINMODE != "0" && TSENS_INTENSET_WINMON = true)>
volatile static TSENS_CALLBACK_OBJ ${TSENS_INSTANCE_NAME}_CallbackObject;
</#if>


// *****************************************************************************
// *****************************************************************************
// Section: ${TSENS_INSTANCE_NAME} Implementation
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Initialize TSENS module */
void ${TSENS_INSTANCE_NAME}_Initialize( void )
{
    /* Reset TSENS */
    ${TSENS_INSTANCE_NAME}_REGS->TSENS_CTRLA = (uint8_t)TSENS_CTRLA_SWRST_Msk;

    while((${TSENS_INSTANCE_NAME}_REGS->TSENS_SYNCBUSY & TSENS_SYNCBUSY_SWRST_Msk) == TSENS_SYNCBUSY_SWRST_Msk)
    {
        /* Wait for Synchronization */
    }

    uint32_t calib_low_word = (uint32_t)(*(uint64_t*)TEMP_LOG_ADDR);
    uint32_t calib_high_word = (uint32_t)((*(uint64_t*)TEMP_LOG_ADDR) >> 32U);

    ${TSENS_INSTANCE_NAME}_REGS->TSENS_CAL = TSENS_CAL_TCAL(calib_low_word & FUSES_TEMP_LOG_WORD_0_TSENS_TCAL_Msk) |
        TSENS_CAL_FCAL((calib_low_word & FUSES_TEMP_LOG_WORD_0_TSENS_FCAL_Msk) >> FUSES_TEMP_LOG_WORD_0_TSENS_FCAL_Pos );
    
    ${TSENS_INSTANCE_NAME}_REGS->TSENS_GAIN = ((calib_high_word & 0xFU) << 20U) | ((calib_low_word & FUSES_TEMP_LOG_WORD_0_TSENS_GAIN_0_Msk) >> FUSES_TEMP_LOG_WORD_0_TSENS_GAIN_0_Pos ) ;
    ${TSENS_INSTANCE_NAME}_REGS->TSENS_OFFSET = calib_high_word >> FUSES_TEMP_LOG_WORD_1_TSENS_OFFSET_Pos;
    
    /* Resolution & Operation Mode */
    <@compress single_line=true>${TSENS_INSTANCE_NAME}_REGS->TSENS_CTRLC = TSENS_CTRLC_WINMODE(${TSENS_CTRLC_WINMODE}UL)
                                     <#if TSENS_CTRLC_VAL?has_content>| ${TSENS_CTRLC_VAL}</#if>;</@compress>
<#if TSENS_CTRLC_WINMODE != "0">
    /* Upper threshold for window mode  */
    ${TSENS_INSTANCE_NAME}_REGS->TSENS_WINUT = (uint32_t)(${TSENS_WINUT});
    /* Lower threshold for window mode  */
    ${TSENS_INSTANCE_NAME}_REGS->TSENS_WINLT = (uint32_t)(${TSENS_WINLT});
</#if>
    /* Clear all interrupt flags */
    ${TSENS_INSTANCE_NAME}_REGS->TSENS_INTFLAG = (uint8_t)TSENS_INTFLAG_Msk;
<#if TSENS_INTENSET_VAL?has_content >
    /* Enable interrupts */
    ${TSENS_INSTANCE_NAME}_REGS->TSENS_INTENSET = (uint8_t)(${TSENS_INTENSET_VAL});
</#if>
<#if TSENS_EVCTRL_VAL?has_content>
    /* Events configuration  */
    ${TSENS_INSTANCE_NAME}_REGS->TSENS_EVCTRL = (uint8_t)(${TSENS_EVCTRL_VAL});
</#if>

<#if TSENS_CTRLA_VAL?has_content>
    <@compress single_line=true>${TSENS_INSTANCE_NAME}_REGS->TSENS_CTRLA |= (uint8_t)(${TSENS_CTRLA_VAL});</@compress>
</#if>
    while(0U != ${TSENS_INSTANCE_NAME}_REGS->TSENS_SYNCBUSY)
    {
        /* Wait for Synchronization */
    }
}

/* Enable TSENS module */
void ${TSENS_INSTANCE_NAME}_Enable( void )
{
    ${TSENS_INSTANCE_NAME}_REGS->TSENS_CTRLA |= (uint8_t)TSENS_CTRLA_ENABLE_Msk;
    while((${TSENS_INSTANCE_NAME}_REGS->TSENS_SYNCBUSY & TSENS_SYNCBUSY_ENABLE_Msk) == TSENS_SYNCBUSY_ENABLE_Msk)
    {
        /* Wait for Synchronization */
    }
}

/* Disable TSENS module */
void ${TSENS_INSTANCE_NAME}_Disable( void )
{
    ${TSENS_INSTANCE_NAME}_REGS->TSENS_CTRLA &= (uint8_t)(~TSENS_CTRLA_ENABLE_Msk);
    while((${TSENS_INSTANCE_NAME}_REGS->TSENS_SYNCBUSY & TSENS_SYNCBUSY_ENABLE_Msk) == TSENS_SYNCBUSY_ENABLE_Msk)
    {
        /* Wait for Synchronization */
    }
}

/* Start the TSENS conversion by SW */
void ${TSENS_INSTANCE_NAME}_ConversionStart( void )
{
    /* Start conversion */
    ${TSENS_INSTANCE_NAME}_REGS->TSENS_CTRLB = (uint8_t)TSENS_CTRLB_START_Msk;

}


/* Configure window comparison threshold values */
void ${TSENS_INSTANCE_NAME}_ComparisonWindowSet(uint32_t low_threshold, uint32_t high_threshold)
{
    ${TSENS_INSTANCE_NAME}_REGS->TSENS_WINLT = low_threshold;
    ${TSENS_INSTANCE_NAME}_REGS->TSENS_WINUT = high_threshold;
}

void ${TSENS_INSTANCE_NAME}_WindowModeSet(TSENS_WINMODE mode)
{
    ${TSENS_INSTANCE_NAME}_REGS->TSENS_CTRLC &= (uint8_t)(~TSENS_CTRLC_WINMODE_Msk);
    ${TSENS_INSTANCE_NAME}_REGS->TSENS_CTRLC |= (uint8_t)((uint32_t)mode << TSENS_CTRLC_WINMODE_Pos);
}

/* Read the conversion result */
uint32_t ${TSENS_INSTANCE_NAME}_ConversionResultGet( void )
{
    return (uint32_t)${TSENS_INSTANCE_NAME}_REGS->TSENS_VALUE;
}

void ${TSENS_INSTANCE_NAME}_InterruptsClear(TSENS_STATUS interruptMask)
{
    ${TSENS_INSTANCE_NAME}_REGS->TSENS_INTFLAG = (uint8_t)interruptMask;
}

void ${TSENS_INSTANCE_NAME}_InterruptsEnable(TSENS_STATUS interruptMask)
{
    ${TSENS_INSTANCE_NAME}_REGS->TSENS_INTENSET = (uint8_t)interruptMask;
}

void ${TSENS_INSTANCE_NAME}_InterruptsDisable(TSENS_STATUS interruptMask)
{
    ${TSENS_INSTANCE_NAME}_REGS->TSENS_INTENCLR = (uint8_t)interruptMask;
}


<#if TSENS_INTENSET_RESRDY == true || (TSENS_CTRLC_WINMODE != "0" && TSENS_INTENSET_WINMON == true)>
/* Register callback function */
void ${TSENS_INSTANCE_NAME}_CallbackRegister( TSENS_CALLBACK callback, uintptr_t context )
{
    ${TSENS_INSTANCE_NAME}_CallbackObject.callback = callback;

    ${TSENS_INSTANCE_NAME}_CallbackObject.context = context;
}


void __attribute__((used)) ${TSENS_INSTANCE_NAME}_InterruptHandler( void )
{
    TSENS_STATUS status;
    status = ${TSENS_INSTANCE_NAME}_REGS->TSENS_INTFLAG;
    /* Clear interrupt flag */
    ${TSENS_INSTANCE_NAME}_REGS->TSENS_INTFLAG = (uint8_t)(${TSENS_INTENSET_VAL});
    if (${TSENS_INSTANCE_NAME}_CallbackObject.callback != NULL)
    {
        uintptr_t context = ${TSENS_INSTANCE_NAME}_CallbackObject.context;
        ${TSENS_INSTANCE_NAME}_CallbackObject.callback(status, context);
    }
}
</#if>
<#if TSENS_INTENSET_RESRDY == false>
/* Check whether result is ready */
bool ${TSENS_INSTANCE_NAME}_ConversionStatusGet( void )
{
    bool status;
    status =  (((${TSENS_INSTANCE_NAME}_REGS->TSENS_INTFLAG & TSENS_INTFLAG_RESRDY_Msk) >> TSENS_INTFLAG_RESRDY_Pos) != 0U);
    if (status == true)
    {
        ${TSENS_INSTANCE_NAME}_REGS->TSENS_INTFLAG = (uint8_t)TSENS_INTFLAG_RESRDY_Msk;
    }
    return status;
}
</#if>
<#if TSENS_CTRLC_WINMODE != "0" && TSENS_INTENSET_WINMON == false>
/* Check whether window monitor result is ready */
bool ${TSENS_INSTANCE_NAME}_WindowMonitorStatusGet( void )
{
    bool status;
    status = (((${TSENS_INSTANCE_NAME}_REGS->TSENS_INTFLAG & TSENS_INTFLAG_WINMON_Msk) >> TSENS_INTFLAG_WINMON_Pos) != 0U);
    if (status == true)
    {
        ${TSENS_INSTANCE_NAME}_REGS->TSENS_INTFLAG = (uint8_t)TSENS_INTFLAG_WINMON_Msk;
    }
    return status;
}
</#if>