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

<#if TMR_INTERRUPT_MODE == true>
static TMR_TIMER_OBJECT ${TMR_INSTANCE_NAME?lower_case}Obj;
</#if>


void ${TMR_INSTANCE_NAME}_Initialize(void)
{
    /* Disable Timer */
    T${TMR_INSTANCE_NUM}CONCLR = _T${TMR_INSTANCE_NUM}CON_ON_MASK;

    /*
    SIDL = ${TIMER_SIDL}
    SYNC = ${TIMER_SYNC}
    TGATE = ${TIMER_TGATE}
    TCKPS =${TIMER_PRE_SCALER}
    T32   = ${TIMER_32BIT_MODE_SEL}
    TCS = ${TIMER_SRC_SEL}
    */
    T${TMR_INSTANCE_NUM}CONSET = 0x${TCON_REG_VALUE};

    /* Clear counter */
    TMR${TMR_INSTANCE_NUM} = 0x0;

    /*Set period */
    PR${TMR_INSTANCE_NUM} = ${TIMER_PERIOD}U;

    <#if TMR_INTERRUPT_MODE == true>
    ${TMR_IEC_REG}SET = _${TMR_IEC_REG}_T${TMR_INSTANCE_NUM}IE_MASK;
    </#if>

    /* start the TMR */
    T${TMR_INSTANCE_NUM}CONSET = _T${TMR_INSTANCE_NUM}CON_ON_MASK;
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

<#if TMR_INTERRUPT_MODE == true>
void TIMER_${TMR_INSTANCE_NUM}_InterruptHandler (void)
{
    uint32_t status = ${TMR_IFS_REG}bits.T${TMR_INSTANCE_NUM}IF;
    ${TMR_IFS_REG}CLR = _${TMR_IFS_REG}_T${TMR_INSTANCE_NUM}IF_MASK;

    if((${TMR_INSTANCE_NAME?lower_case}Obj.callback_fn != NULL))
    {
        ${TMR_INSTANCE_NAME?lower_case}Obj.callback_fn(status, ${TMR_INSTANCE_NAME?lower_case}Obj.context);
    }
}


void ${TMR_INSTANCE_NAME}_InterruptEnable(void)
{

    ${TMR_IEC_REG}SET = _${TMR_IEC_REG}_T${TMR_INSTANCE_NUM}IE_MASK;
}


void ${TMR_INSTANCE_NAME}_InterruptDisable(void)
{
    ${TMR_IEC_REG}CLR = _${TMR_IEC_REG}_T${TMR_INSTANCE_NUM}IE_MASK;
}


void ${TMR_INSTANCE_NAME}_CallbackRegister( TMR_CALLBACK callback_fn, uintptr_t context )
{
    /* Save callback_fn and context in local memory */
    ${TMR_INSTANCE_NAME?lower_case}Obj.callback_fn = callback_fn;
    ${TMR_INSTANCE_NAME?lower_case}Obj.context = context;
}
</#if>
