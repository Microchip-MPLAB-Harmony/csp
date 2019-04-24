/*******************************************************************************
  TMR1 Peripheral Library Interface Source File

  Company
    Microchip Technology Inc.

  File Name
    plib_${TMR1_INSTANCE_NAME?lower_case}.c

  Summary
    ${TMR1_INSTANCE_NAME} peripheral library source file.

  Description
    This file implements the interface to the TMR1 peripheral library.  This
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
#include "plib_${TMR1_INSTANCE_NAME?lower_case}.h"

<#if TMR1_INTERRUPT_MODE == true>
static TMR1_TIMER_OBJECT ${TMR1_INSTANCE_NAME?lower_case}Obj;
</#if>

void ${TMR1_INSTANCE_NAME}_Initialize(void)
{
    /* Disable Timer */
    T1CONCLR = _T1CON_ON_MASK;

    /*
    SIDL = ${TIMER1_SIDL}
    TWDIS = ${TIMER1_TWDIS}
    TECS = ${TIMER1_TECS}
    TGATE = ${TIMER1_TGATE}
    TCKPS = ${TIMER1_PRE_SCALER}
    TSYNC = ${TIMER1_TSYNC}
    TCS = ${TIMER1_SRC_SEL}
    */
    T1CONSET = 0x${TCON_REG_VALUE};

    /* Clear counter */
    TMR1 = 0x0;

    /*Set period */
    PR1 = ${TIMER1_PERIOD};

    <#if TMR1_INTERRUPT_MODE == true>
    /* Setup TMR1 Interrupt */
    ${TMR1_INSTANCE_NAME}_InterruptEnable();  /* Enable interrupt on the way out */
    </#if>
}


void ${TMR1_INSTANCE_NAME}_Start (void)
{
    T1CONSET = _T1CON_ON_MASK;
}


void ${TMR1_INSTANCE_NAME}_Stop (void)
{
    T1CONCLR = _T1CON_ON_MASK;
}


void ${TMR1_INSTANCE_NAME}_PeriodSet(uint16_t period)
{
    PR1 = period;
}


uint16_t ${TMR1_INSTANCE_NAME}_PeriodGet(void)
{
    return (uint16_t)PR1;
}


uint16_t ${TMR1_INSTANCE_NAME}_CounterGet(void)
{
    return(TMR1);
}

uint32_t ${TMR1_INSTANCE_NAME}_FrequencyGet(void)
{
    return (${TIMER1_CLOCK_FREQ});
}

<#if TMR1_INTERRUPT_MODE == true>
void TIMER_1_InterruptHandler (void)
{
    uint32_t status = ${TMR1_IFS_REG}bits.T1IF;
    ${TMR1_IFS_REG}CLR = _${TMR1_IFS_REG}_T1IF_MASK;

    if((${TMR1_INSTANCE_NAME?lower_case}Obj.callback_fn != NULL))
    {
        ${TMR1_INSTANCE_NAME?lower_case}Obj.callback_fn(status, ${TMR1_INSTANCE_NAME?lower_case}Obj.context);
    }
}


void ${TMR1_INSTANCE_NAME}_InterruptEnable(void)
{
    ${TMR1_IEC_REG}SET = _${TMR1_IEC_REG}_T1IE_MASK;
}


void ${TMR1_INSTANCE_NAME}_InterruptDisable(void)
{
    ${TMR1_IEC_REG}CLR = _${TMR1_IEC_REG}_T1IE_MASK;
}


void ${TMR1_INSTANCE_NAME}_CallbackRegister( TMR1_CALLBACK callback_fn, uintptr_t context )
{
    /* - Save callback_fn and context in local memory */
    ${TMR1_INSTANCE_NAME?lower_case}Obj.callback_fn = callback_fn;
    ${TMR1_INSTANCE_NAME?lower_case}Obj.context = context;
}
</#if>
