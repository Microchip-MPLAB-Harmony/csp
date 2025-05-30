/*******************************************************************************
  TMR Peripheral Library Interface Source File

  Company
    Microchip Technology Inc.

  File Name
    plib_${TMR_INSTANCE_NAME?lower_case}.c

  Summary
    ${TMR_INSTANCE_NAME} peripheral library source file.

  Description
    This file implements the interface to the TMR peripheral library.  This
    library provides access to and control of the associated peripheral
    instance.

*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
* Copyright (C) 2019 Microchip Technology Inc. and its subsidiaries.
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

#include "device.h"
#include "plib_${TMR_INSTANCE_NAME?lower_case}.h"
<#if core.CoreSysIntFile == true>
#include "interrupts.h"
</#if>

<#assign interrupt = false>
<#if (TIMER_32BIT_MODE_SEL == "0" && TMR_INTERRUPT_MODE == true) || (TIMER_32BIT_MODE_SEL == "1" && TMR_SLAVE_INTERRUPT_MODE == true)>
    <#assign interrupt = true>
</#if>

<#if  interrupt == true>
static volatile TMR_TIMER_OBJECT ${TMR_INSTANCE_NAME?lower_case}Obj;
</#if>


void ${TMR_INSTANCE_NAME}_Initialize(void)
{
    /* Disable Timer */
    T${TMR_INSTANCE_NUM}CONCLR = _T${TMR_INSTANCE_NUM}CON_ON_MASK;

    /*
    SIDL = ${TIMER_SIDL}
    TCKPS =${TIMER_PRE_SCALER}
    T32   = ${TIMER_32BIT_MODE_SEL}
    <#if TIMER_SRC_SEL?has_content>
        <#lt>    TCS = ${TIMER_SRC_SEL}
    </#if>
    */
    T${TMR_INSTANCE_NUM}CONSET = 0x${TCON_REG_VALUE};

    /* Clear counter */
    TMR${TMR_INSTANCE_NUM} = 0x0;

    /*Set period */
    PR${TMR_INSTANCE_NUM} = ${TIMER_PERIOD}U;

    <#if interrupt == true>
    <#if TIMER_32BIT_MODE_SEL =="0">
    /* Enable TMR Interrupt */
    ${TMR_IEC_REG}SET = _${TMR_IEC_REG}_T${TMR_INSTANCE_NUM}IE_MASK;
    <#else>
    /* Enable TMR Interrupt of odd numbered timer in 32-bit mode */
    ${TMR_IEC_REG}SET = _${TMR_IEC_REG}_T${TMR_INSTANCE_NUM?number + 1}IE_MASK;
    </#if>
    </#if>

}


void ${TMR_INSTANCE_NAME}_Start(void)
{
    T${TMR_INSTANCE_NUM}CONSET = _T${TMR_INSTANCE_NUM}CON_ON_MASK;
}


void ${TMR_INSTANCE_NAME}_Stop (void)
{
    T${TMR_INSTANCE_NUM}CONCLR = _T${TMR_INSTANCE_NUM}CON_ON_MASK;
}

<#if TIMER_32BIT_MODE_SEL =="0">
void ${TMR_INSTANCE_NAME}_PeriodSet(uint16_t period)
{
    PR${TMR_INSTANCE_NUM}  = period;
}

uint16_t ${TMR_INSTANCE_NAME}_PeriodGet(void)
{
    return (uint16_t)PR${TMR_INSTANCE_NUM};
}

uint16_t ${TMR_INSTANCE_NAME}_CounterGet(void)
{
    return (uint16_t)(TMR${TMR_INSTANCE_NUM});
}

<#else>
void ${TMR_INSTANCE_NAME}_PeriodSet(uint32_t period)
{
    PR${TMR_INSTANCE_NUM}  = period;
}

uint32_t ${TMR_INSTANCE_NAME}_PeriodGet(void)
{
    return PR${TMR_INSTANCE_NUM};
}

uint32_t ${TMR_INSTANCE_NAME}_CounterGet(void)
{
    return (TMR${TMR_INSTANCE_NUM});
}

</#if>

uint32_t ${TMR_INSTANCE_NAME}_FrequencyGet(void)
{
    return (${TIMER_CLOCK_FREQ});
}

<#if TIMER_32BIT_MODE_SEL =="1" && TMR_INTERRUPT_MODE == true>
void __attribute__((used)) TIMER_${TMR_INSTANCE_NUM}_InterruptHandler (void)
{
    /* In 32-bit mode, master interrupt handler is ignored */
    ${TMR_IFS_REG}CLR = _${TMR_IFS_REG}_T${TMR_INSTANCE_NUM}IF_MASK;
}
</#if>

<#if interrupt == true>
<#if TIMER_32BIT_MODE_SEL =="0">
void __attribute__((used)) TIMER_${TMR_INSTANCE_NUM}_InterruptHandler (void)
<#else>
void __attribute__((used)) TIMER_${TMR_INSTANCE_NUM?number + 1}_InterruptHandler (void)
</#if>
{
    uint32_t status  = 0U;
<#if TIMER_32BIT_MODE_SEL =="0">
    status = ${TMR_IFS_REG}bits.T${TMR_INSTANCE_NUM}IF;
    ${TMR_IFS_REG}CLR = _${TMR_IFS_REG}_T${TMR_INSTANCE_NUM}IF_MASK;
<#else>
    status = ${TMR_IFS_REG}bits.T${TMR_INSTANCE_NUM?number + 1}IF;
    ${TMR_IFS_REG}CLR = _${TMR_IFS_REG}_T${TMR_INSTANCE_NUM?number + 1}IF_MASK;
</#if>

    if((${TMR_INSTANCE_NAME?lower_case}Obj.callback_fn != NULL))
    {
        uintptr_t context = ${TMR_INSTANCE_NAME?lower_case}Obj.context;
        ${TMR_INSTANCE_NAME?lower_case}Obj.callback_fn(status, context);
    }
}


void ${TMR_INSTANCE_NAME}_InterruptEnable(void)
{
<#if TIMER_32BIT_MODE_SEL =="0">
    ${TMR_IEC_REG}SET = _${TMR_IEC_REG}_T${TMR_INSTANCE_NUM}IE_MASK;
<#else>
    ${TMR_IEC_REG}SET = _${TMR_IEC_REG}_T${TMR_INSTANCE_NUM?number + 1}IE_MASK;
</#if>
}


void ${TMR_INSTANCE_NAME}_InterruptDisable(void)
{
<#if TIMER_32BIT_MODE_SEL =="0">
    ${TMR_IEC_REG}CLR = _${TMR_IEC_REG}_T${TMR_INSTANCE_NUM}IE_MASK;
<#else>
    ${TMR_IEC_REG}CLR = _${TMR_IEC_REG}_T${TMR_INSTANCE_NUM?number + 1}IE_MASK;
</#if>
}


void ${TMR_INSTANCE_NAME}_CallbackRegister( TMR_CALLBACK callback_fn, uintptr_t context )
{
    /* Save callback_fn and context in local memory */
    ${TMR_INSTANCE_NAME?lower_case}Obj.callback_fn = callback_fn;
    ${TMR_INSTANCE_NAME?lower_case}Obj.context = context;
}
<#else>

bool ${TMR_INSTANCE_NAME}_PeriodHasExpired(void)
{
    bool status;
    <#if TIMER_32BIT_MODE_SEL =="0">
        status = (${TMR_IFS_REG}bits.T${TMR_INSTANCE_NUM}IF != 0U);
        ${TMR_IFS_REG}CLR = _${TMR_IFS_REG}_T${TMR_INSTANCE_NUM}IF_MASK;
    <#else>
        status = (${TMR_IFS_REG}bits.T${TMR_INSTANCE_NUM?number + 1}IF != 0U);
        ${TMR_IFS_REG}CLR = _${TMR_IFS_REG}_T${TMR_INSTANCE_NUM?number + 1}IF_MASK;
    </#if>

    return status;
}
</#if>
